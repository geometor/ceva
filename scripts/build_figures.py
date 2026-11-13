#!/usr/bin/env python3
"""Generate the 8 interactive .euclid-graphic SVG plates for GEOMETOR Ceva.

Each SVG strictly obeys the ``photon-platform/publish`` ``.euclid-graphic`` contract:
- ``<defs>`` tick markers (``#geom-tick-1..3``)
- Ordered layer groups: ``#elements``, ``#graphics``, ``#highlights``, ``#points``, ``#labels``
- 3-vertex midpoint ``<path d="M x1 y1 L mx my L x2 y2">`` segments
- Canonical ``data-ref`` attributes wired to ``:g:`` roles in the Book Codex
- ``html.escape`` on all ``<text>`` and ``aria-label`` strings
- Exact coordinates evaluated via ``geometor.ceva`` and projected to viewport coordinates
"""

from __future__ import annotations

import html
import math
from pathlib import Path
from typing import Sequence

import sympy as sp

from geometor.ceva import (
    HERONIAN_VERTICES,
    RATIONAL_PENTAGON,
    RATIONAL_TETRAHEDRON,
    evaluate_canonical_centers,
    solve_static_barycentrics,
    solve_tetrahedron_static_equilibrium,
    verify_odd_polygon_ceva,
    verify_spread_ceva,
)

OUT_DIR = Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "figures"

Point2F = tuple[float, float]
Point3F = tuple[float, float, float]

DEFS_BLOCK = """  <defs>
    <marker id="geom-tick-1" viewBox="-2 -6 4 12" refX="0" refY="0" markerWidth="4" markerHeight="12" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-2" viewBox="-4 -6 8 12" refX="0" refY="0" markerWidth="8" markerHeight="12" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto">
      <line x1="-3.4" y1="-4.5" x2="-3.4" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
      <line x1="3.4" y1="-4.5" x2="3.4" y2="4.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round"/>
    </marker>
  </defs>"""


class EuclidSVGBuilder:
    """Assemble a theme-adaptive ``.euclid-graphic`` SVG figure."""

    def __init__(self, width: int, height: int, aria_label: str) -> None:
        """Initialize an empty SVG layer stack.

        Args:
            width: SVG viewBox width in pixels.
            height: SVG viewBox height in pixels.
            aria_label: Accessible description of the plate.
        """
        self.width = width
        self.height = height
        self.aria_label = html.escape(aria_label, quote=True)
        self.elements: list[str] = []
        self.graphics: list[str] = []
        self.highlights: list[str] = []
        self.points: list[str] = []
        self.labels: list[str] = []

    def seg(
        self,
        p1: Point2F,
        p2: Point2F,
        ref: str,
        *,
        cls: str = "geom-line",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
        ticks: int = 0,
    ) -> None:
        """Add a 3-vertex midpoint path segment to ``#elements``.

        Args:
            p1: Start viewport coordinate ``(x1, y1)``.
            p2: End viewport coordinate ``(x2, y2)``.
            ref: ``data-ref`` identifier for ``:g:`` wiring.
            cls: SVG CSS class name.
            stroke: Optional CSS stroke override.
            width: Optional stroke width in pixels.
            dash: Optional ``stroke-dasharray`` specification.
            ticks: Equality tick marker count (``0..3``).
        """
        x1, y1 = p1
        x2, y2 = p2
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        attrs = [
            f'class="{cls}"',
            f'd="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if ticks in (1, 2, 3):
            attrs.append(f'marker-mid="url(#geom-tick-{ticks})"')
        self.elements.append(f"    <path {' '.join(attrs)}/>")

    def circle(
        self,
        center: Point2F,
        radius: float,
        ref: str,
        *,
        cls: str = "geom-circle",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
    ) -> None:
        """Add a circle to ``#elements``.

        Args:
            center: Circle center ``(cx, cy)``.
            radius: Circle radius in viewport pixels.
            ref: ``data-ref`` identifier.
            cls: SVG CSS class name.
            stroke: Optional CSS stroke override.
            width: Optional stroke width.
            dash: Optional ``stroke-dasharray`` specification.
        """
        cx, cy = center
        attrs = [
            f'class="{cls}"',
            f'cx="{cx:.2f}"',
            f'cy="{cy:.2f}"',
            f'r="{radius:.2f}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.elements.append(f"    <circle {' '.join(attrs)}/>")

    def ellipse(
        self,
        center: Point2F,
        rx: float,
        ry: float,
        ref: str,
        *,
        cls: str = "geom-circle",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
    ) -> None:
        """Add an ellipse to ``#elements``.

        Args:
            center: Ellipse center ``(cx, cy)``.
            rx: Horizontal semi-axis in pixels.
            ry: Vertical semi-axis in pixels.
            ref: ``data-ref`` identifier.
            cls: SVG CSS class name.
            stroke: Optional CSS stroke override.
            width: Optional stroke width.
            dash: Optional ``stroke-dasharray`` specification.
        """
        cx, cy = center
        attrs = [
            f'class="{cls}"',
            f'cx="{cx:.2f}"',
            f'cy="{cy:.2f}"',
            f'rx="{rx:.2f}"',
            f'ry="{ry:.2f}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.elements.append(f"    <ellipse {' '.join(attrs)}/>")

    def arc(
        self,
        center: Point2F,
        radius: float,
        deg_start: float,
        deg_end: float,
        ref: str,
        *,
        cls: str = "geom-arc",
        stroke: str | None = None,
        width: float | None = None,
        dash: str | None = None,
        layer: str = "elements",
    ) -> None:
        """Add a circular arc (math CCW degrees converted to SVG y-down coordinates).

        Args:
            center: Arc center ``(cx, cy)``.
            radius: Arc radius in pixels.
            deg_start: Start angle in CCW degrees.
            deg_end: End angle in CCW degrees.
            ref: ``data-ref`` identifier.
            cls: SVG CSS class name.
            stroke: Optional stroke override.
            width: Optional stroke width.
            dash: Optional dash specification.
            layer: Target SVG layer (``"elements"`` or ``"graphics"``).
        """
        cx, cy = center
        a1 = math.radians(deg_start)
        a2 = math.radians(deg_end)
        x1, y1 = cx + radius * math.cos(a1), cy - radius * math.sin(a1)
        x2, y2 = cx + radius * math.cos(a2), cy - radius * math.sin(a2)
        span = (deg_end - deg_start) % 360.0
        large = 1 if span > 180.0 else 0
        d_str = f"M {x1:.2f} {y1:.2f} A {radius:.2f} {radius:.2f} 0 {large} 0 {x2:.2f} {y2:.2f}"
        attrs = [
            f'class="{cls}"',
            f'd="{d_str}"',
            'fill="none"',
            f'data-ref="{html.escape(ref, quote=True)}"',
        ]
        if stroke:
            attrs.append(f'stroke="{stroke}"')
        if width is not None:
            attrs.append(f'stroke-width="{width:.2f}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        target = self.graphics if layer == "graphics" else self.elements
        target.append(f"    <path {' '.join(attrs)}/>")

    def polygon(
        self,
        pts: Sequence[Point2F],
        ref: str,
        *,
        fill: str = "var(--geom-accent, #d97706)",
        fill_opacity: float = 0.12,
    ) -> None:
        """Add a translucent highlight polygon to ``#highlights``.

        Args:
            pts: Ordered polygon vertices in viewport coordinates.
            ref: ``data-ref`` identifier.
            fill: CSS fill color.
            fill_opacity: Opacity in ``[0, 1]``.
        """
        coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.highlights.append(
            f'    <polygon class="geom-polygon" points="{coords}" '
            f'fill="{fill}" fill-opacity="{fill_opacity:.2f}" stroke="none" '
            f'data-ref="{html.escape(ref, quote=True)}"/>'
        )

    def path_highlight(
        self,
        d_str: str,
        ref: str,
        *,
        fill: str = "var(--geom-accent, #d97706)",
        fill_opacity: float = 0.16,
    ) -> None:
        """Add an arbitrary filled path highlight to ``#highlights``.

        Args:
            d_str: SVG path data string.
            ref: ``data-ref`` identifier.
            fill: CSS fill color.
            fill_opacity: Opacity in ``[0, 1]``.
        """
        self.highlights.append(
            f'    <path class="geom-polygon" d="{d_str}" '
            f'fill="{fill}" fill-opacity="{fill_opacity:.2f}" stroke="none" '
            f'data-ref="{html.escape(ref, quote=True)}"/>'
        )

    def point(
        self,
        pt: Point2F,
        ref: str,
        *,
        r: float = 3.6,
        fill: str | None = None,
    ) -> None:
        """Add a point dot to ``#points``.

        Args:
            pt: Viewport point ``(px, py)``.
            ref: ``data-ref`` identifier.
            r: Point radius in pixels.
            fill: Optional CSS fill color.
        """
        px, py = pt
        fill_attr = f' fill="{fill}"' if fill else ""
        self.points.append(
            f'    <circle class="geom-point" cx="{px:.2f}" cy="{py:.2f}" '
            f'r="{r:.2f}"{fill_attr} data-ref="{html.escape(ref, quote=True)}"/>'
        )

    def label(
        self,
        pt: Point2F,
        text: str,
        ref: str,
        *,
        dx: float = 0.0,
        dy: float = 0.0,
        size: int = 14,
        italic: bool = True,
        anchor: str = "middle",
    ) -> None:
        """Add an escaped text label to ``#labels``.

        Args:
            pt: Base viewport coordinate ``(x, y)``.
            text: Raw text label (escaped via ``html.escape``).
            ref: ``data-ref`` identifier.
            dx: Horizontal pixel offset.
            dy: Vertical pixel offset.
            size: Font size in pixels.
            italic: Whether to render italicized math lettering.
            anchor: SVG ``text-anchor`` alignment.
        """
        lx, ly = pt[0] + dx, pt[1] + dy
        style_italic = "font-style: italic; " if italic else ""
        esc_txt = html.escape(text)
        self.labels.append(
            f'    <text class="geom-label" x="{lx:.2f}" y="{ly:.2f}" '
            f'text-anchor="{anchor}" dominant-baseline="central" '
            f'style="{style_italic}font-size: {size}px;" '
            f'data-ref="{html.escape(ref, quote=True)}">{esc_txt}</text>'
        )

    def caption(self, x: float, y: float, text: str, *, size: int = 13) -> None:
        """Add an escaped structural caption inside a plate.

        Args:
            x: Horizontal center coordinate.
            y: Vertical baseline coordinate.
            text: Raw caption string.
            size: Font size in pixels.
        """
        esc_txt = html.escape(text)
        self.labels.append(
            f'    <text class="geom-label" x="{x:.2f}" y="{y:.2f}" '
            f'text-anchor="middle" style="font-size: {size}px; opacity: 0.86;">{esc_txt}</text>'
        )

    def render(self) -> str:
        """Serialize the complete ``.euclid-graphic`` SVG document.

        Returns:
            Formatted XML string ending with a trailing newline.
        """
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
            f'viewBox="0 0 {self.width} {self.height}" role="img" aria-label="{self.aria_label}">',
            DEFS_BLOCK,
            '  <g id="elements">',
            *self.elements,
            "  </g>",
            '  <g id="graphics">',
            *self.graphics,
            "  </g>",
            '  <g id="highlights">',
            *self.highlights,
            "  </g>",
            '  <g id="points">',
            *self.points,
            "  </g>",
            '  <g id="labels">',
            *self.labels,
            "  </g>",
            "</svg>",
            "",
        ]
        return "\n".join(parts)


def _to_xy(pt: sp.Expr | object, ox: float, oy: float, scale: float) -> Point2F:
    """Map an exact SymPy ``Point2D`` or pair to SVG y-down coordinates.

    Args:
        pt: Exact ``Point2D`` or ``(x, y)`` pair.
        ox: Viewport x-origin corresponding to math ``x = 0``.
        oy: Viewport y-origin corresponding to math ``y = 0``.
        scale: Pixels per math unit.

    Returns:
        Projected ``(px, py)`` tuple.
    """
    if hasattr(pt, "x") and hasattr(pt, "y"):
        mx = float(getattr(pt, "x"))
        my = float(getattr(pt, "y"))
    elif isinstance(pt, (tuple, list)) and len(pt) == 2:
        mx = float(pt[0])
        my = float(pt[1])
    else:
        raise TypeError(f"Unsupported 2D point: {pt!r}")
    return (ox + scale * mx, oy - scale * my)


def _proj3d(vec: sp.Matrix | Point3F, ox: float, oy: float, scale: float) -> Point2F:
    """Project a 3D point via clean cabinet-axonometric projection to SVG coordinates.

    Args:
        vec: 3x1 ``sp.Matrix`` or 3-tuple ``(x, y, z)``.
        ox: Viewport x-origin.
        oy: Viewport y-origin.
        scale: Pixels per spatial unit.

    Returns:
        Projected ``(px, py)`` tuple.
    """
    if isinstance(vec, sp.Matrix):
        vx, vy, vz = float(vec[0]), float(vec[1]), float(vec[2])
    else:
        vx, vy, vz = float(vec[0]), float(vec[1]), float(vec[2])
    px = ox + scale * (vx - 0.36 * vy)
    py = oy - scale * (vz + 0.32 * vy)
    return (px, py)


def build_fig01_statica_lever_elements() -> str:
    """Build Figure 1: Archimedes' Law of the Lever & Ceva's Elementum II (tab. 1. figs. 1-6).

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        920,
        430,
        "Ceva Liber Primus Lemmata I-II Archimedean Lever and Elementum II Static Triangle Equilibrium",
    )

    # Left panel: Archimedean lever A -- F -- B with suspended weights mA = 3, mB = 5
    pa = (85.0, 175.0)
    pb = (395.0, 175.0)
    pf = (85.0 + 310.0 * (5.0 / 8.0), 175.0)  # AF : FB = 5 : 3
    wa = (pa[0], 280.0)
    wb = (pb[0], 295.0)

    svg.polygon(
        [(pf[0], pf[1]), (pf[0] - 18.0, pf[1] + 32.0), (pf[0] + 18.0, pf[1] + 32.0)],
        "F",
        fill="#d97706",
        fill_opacity=0.28,
    )
    svg.seg(pa, pb, "AB", width=2.4)
    svg.seg(pa, pf, "AF", stroke="#0284c7", width=2.2)
    svg.seg(pf, pb, "FB", stroke="#16a34a", width=2.2)
    svg.seg(pa, (wa[0], wa[1] - 22.0), "mA", dash="4 3", width=1.4)
    svg.seg(pb, (wb[0], wb[1] - 28.0), "mB", dash="4 3", width=1.4)
    svg.circle(wa, 22.0, "mA", stroke="#0284c7", width=1.9)
    svg.circle(wb, 28.0, "mB", stroke="#16a34a", width=1.9)
    svg.point(pa, "A")
    svg.point(pb, "B")
    svg.point(pf, "F", r=4.4, fill="#d97706")
    svg.label(pa, "A", "A", dy=-18.0)
    svg.label(pb, "B", "B", dy=-18.0)
    svg.label(pf, "F", "F", dy=-18.0)
    svg.label(wa, "u = 3", "mA", size=13, italic=False)
    svg.label(wb, "v = 5", "mB", size=13, italic=False)
    svg.caption(240.0, 38.0, "Lemmata I-II: u * AF = v * FB  (A : B = BF : FA)")
    svg.caption(240.0, 392.0, "Tab. 1, Fig. 1 — Archimedean Equiponderants I.6")

    # Right panel: Elementum II interior three-weight triangle balance (u=3, v=5, w=4)
    sol = solve_static_barycentrics(3, 5, 4, HERONIAN_VERTICES, name="P")
    ox, oy, sc = 505.0, 345.0, 24.5
    ta = _to_xy(sol.vertices[0], ox, oy, sc)
    tb = _to_xy(sol.vertices[1], ox, oy, sc)
    tc = _to_xy(sol.vertices[2], ox, oy, sc)
    td = _to_xy(sol.foot_d, ox, oy, sc)
    te = _to_xy(sol.foot_e, ox, oy, sc)
    tf = _to_xy(sol.foot_f, ox, oy, sc)
    tp = _to_xy(sol.center, ox, oy, sc)

    svg.polygon([ta, tb, tc], "ABC", fill="#0284c7", fill_opacity=0.07)
    svg.seg(ta, tb, "ABC", width=2.0)
    svg.seg(tb, tc, "ABC", width=2.0)
    svg.seg(tc, ta, "ABC", width=2.0)
    svg.seg(ta, td, "AD", stroke="#d97706", width=1.8)
    svg.seg(tb, te, "BE", stroke="#d97706", width=1.8)
    svg.seg(tc, tf, "CF", stroke="#d97706", width=1.8)

    for pt, name, dx, dy in (
        (ta, "A (u=3)", 0.0, -16.0),
        (tb, "B (v=5)", -20.0, 16.0),
        (tc, "C (w=4)", 22.0, 16.0),
        (td, "D", 0.0, 16.0),
        (te, "E", 16.0, -8.0),
        (tf, "F", -16.0, -8.0),
    ):
        ref_key = name.split()[0]
        svg.point(pt, ref_key)
        svg.label(pt, name, ref_key, dx=dx, dy=dy, size=13)

    svg.point(tp, "P", r=4.8, fill="#dc2626")
    svg.label(tp, "P (u+v+w)", "P", dx=34.0, dy=-12.0, size=13)
    svg.caption(680.0, 38.0, "Elementum II: Static Concurrency at Center of Gravity P")
    svg.caption(680.0, 392.0, "Tab. 1, Fig. 5 — (AF/FB)*(BD/DC)*(CE/EA) = (5/3)*(4/5)*(3/4) = 1")
    return svg.render()


def build_fig02_ceva_interior_exterior() -> str:
    """Build Figure 2: Interior Concurrency + Caravaggio Jr. Prop. VI vs Exterior Negative Weight.

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        940,
        440,
        "Ceva Interior Concurrency with Caravaggio Parallel Line vs Exterior Negative Weight J_A",
    )

    # Left panel: Interior concurrency + Caravaggio Jr.'s Prop. VI parallel through A (tab. 1. fig. 10)
    sol_in = solve_static_barycentrics(24, 28, 21, HERONIAN_VERTICES, name="P")
    ox1, oy1, sc1 = 55.0, 355.0, 22.5
    ia = _to_xy(sol_in.vertices[0], ox1, oy1, sc1)
    ib = _to_xy(sol_in.vertices[1], ox1, oy1, sc1)
    ic = _to_xy(sol_in.vertices[2], ox1, oy1, sc1)
    id_pt = _to_xy(sol_in.foot_d, ox1, oy1, sc1)
    ie = _to_xy(sol_in.foot_e, ox1, oy1, sc1)
    if_pt = _to_xy(sol_in.foot_f, ox1, oy1, sc1)
    ip = _to_xy(sol_in.center, ox1, oy1, sc1)

    # Caravaggio Jr. line through A=(5,12) parallel to BC (y=12): meets CF and BE extended!
    # Line CF joins C=(14,0) and F=(u*5/(u+v), u*12/(u+v)); at y=12:
    fx, fy = float(sol_in.foot_f.x), float(sol_in.foot_f.y)
    ex, ey = float(sol_in.foot_e.x), float(sol_in.foot_e.y)
    xk_m = 14.0 + (fx - 14.0) * (12.0 / fy)
    xl_m = 0.0 + ex * (12.0 / ey)
    ik = _to_xy((xk_m, 12.0), ox1, oy1, sc1)
    il = _to_xy((xl_m, 12.0), ox1, oy1, sc1)

    svg.polygon([ia, ib, ic], "ABC", fill="#0284c7", fill_opacity=0.07)
    svg.seg(ik, il, "parA", stroke="#7c3aed", width=1.6, dash="5 4")
    svg.seg(ic, ik, "CF", stroke="#94a3b8", width=1.2, dash="3 3")
    svg.seg(ib, il, "BE", stroke="#94a3b8", width=1.2, dash="3 3")
    svg.seg(ia, ib, "ABC", width=2.0)
    svg.seg(ib, ic, "ABC", width=2.0)
    svg.seg(ic, ia, "ABC", width=2.0)
    svg.seg(ia, id_pt, "AD", stroke="#d97706", width=1.9)
    svg.seg(ib, ie, "BE", stroke="#d97706", width=1.9)
    svg.seg(ic, if_pt, "CF", stroke="#d97706", width=1.9)

    for pt, ref, dx, dy in (
        (ia, "A", 0.0, -15.0),
        (ib, "B", -14.0, 14.0),
        (ic, "C", 14.0, 14.0),
        (id_pt, "D", 0.0, 15.0),
        (ie, "E", 14.0, -6.0),
        (if_pt, "F", -14.0, -6.0),
        (ik, "parA", -10.0, -13.0),
        (il, "parA", 10.0, -13.0),
    ):
        svg.point(pt, ref, r=3.3)
    svg.label(ia, "A", "A", dy=-15.0)
    svg.label(ib, "B", "B", dx=-14.0, dy=14.0)
    svg.label(ic, "C", "C", dx=14.0, dy=14.0)
    svg.label(id_pt, "D", "D", dy=15.0)
    svg.label(ie, "E", "E", dx=14.0, dy=-5.0)
    svg.label(if_pt, "F", "F", dx=-14.0, dy=-5.0)
    svg.label(ik, "K", "parA", dy=-14.0, size=12)
    svg.label(il, "L", "parA", dy=-14.0, size=12)
    svg.point(ip, "P", r=4.5, fill="#dc2626")
    svg.label(ip, "P", "P", dx=14.0, dy=-10.0)
    svg.caption(235.0, 34.0, "Prop. VI (Caravaggio Jr.): Parallel KL || BC")
    svg.caption(235.0, 404.0, "Tab. 1, Fig. 10 — Pure Euclidean Similar-Triangle Proof")

    # Right panel: Elementum III & p. 5 Scholium — Negative weight (-3 : 5 : 4) exterior concurrency!
    sol_ex = solve_static_barycentrics(-3, 5, 4, HERONIAN_VERTICES, name="J_A")
    # Check bounding box: A=(5,12), B=(0,0), C=(14,0), D=(56/9,0), E=(41, -36)? Wait:
    # Let's use weights (-2, 5, 5) or (-14, 15, 13)? Wait: for (-3, 6, 5):
    # w+u = 2, u+v = 3, u+v+w = 8 -> compact coordinates! Let's compute (-3, 6, 6):
    sol_ex = solve_static_barycentrics(-3, 6, 6, HERONIAN_VERTICES, name="J_A")
    # For (-3, 6, 6): u+v=3 -> F=(-5, -12); w+u=3 -> E=(23, -12); v+w=12 -> D=(7, 0);
    # u+v+w = 9 -> J_A = (-3*5 + 0 + 84)/9 = (69/9, -36/9) = (23/3, -4)! Super compact!
    ox2, oy2, sc2 = 585.0, 225.0, 10.6
    ea = _to_xy(sol_ex.vertices[0], ox2, oy2, sc2)
    eb = _to_xy(sol_ex.vertices[1], ox2, oy2, sc2)
    ec = _to_xy(sol_ex.vertices[2], ox2, oy2, sc2)
    ed = _to_xy(sol_ex.foot_d, ox2, oy2, sc2)
    ee = _to_xy(sol_ex.foot_e, ox2, oy2, sc2)
    ef = _to_xy(sol_ex.foot_f, ox2, oy2, sc2)
    ej = _to_xy(sol_ex.center, ox2, oy2, sc2)

    svg.polygon([ea, eb, ec], "ABC", fill="#0284c7", fill_opacity=0.08)
    svg.seg(ea, ef, "F_ext", stroke="#94a3b8", width=1.3, dash="4 3")
    svg.seg(ea, ee, "E_ext", stroke="#94a3b8", width=1.3, dash="4 3")
    svg.seg(ea, eb, "ABC", width=2.0)
    svg.seg(eb, ec, "ABC", width=2.0)
    svg.seg(ec, ea, "ABC", width=2.0)
    svg.seg(ea, ej, "AD", stroke="#dc2626", width=1.8)
    svg.seg(eb, ee, "BE", stroke="#dc2626", width=1.6)
    svg.seg(ec, ef, "CF", stroke="#dc2626", width=1.6)

    svg.point(ea, "A")
    svg.point(eb, "B")
    svg.point(ec, "C")
    svg.point(ed, "D")
    svg.point(ee, "E_ext", fill="#7c3aed")
    svg.point(ef, "F_ext", fill="#7c3aed")
    svg.point(ej, "J_A", r=4.6, fill="#dc2626")

    svg.label(ea, "A (-u)", "A", dy=-15.0, size=13)
    svg.label(eb, "B (+v)", "B", dx=-24.0, dy=-8.0, size=13)
    svg.label(ec, "C (+w)", "C", dx=24.0, dy=-8.0, size=13)
    svg.label(ed, "D", "D", dx=10.0, dy=-12.0, size=12)
    svg.label(ee, "E'", "E_ext", dx=14.0, dy=12.0, size=13)
    svg.label(ef, "F'", "F_ext", dx=-14.0, dy=12.0, size=13)
    svg.label(ej, "J_A (F - A)", "J_A", dx=0.0, dy=18.0, size=13)

    svg.caption(695.0, 34.0, "Elementum III & p. 5 Scholium: Negative Weight F - A")
    svg.caption(695.0, 404.0, "Two Negative Side Ratios (-2)*(1)*(-1/2) = +1 => Exterior Concurrency")
    return svg.render()


def build_fig03_menelaus_harmonic_quadrangle() -> str:
    """Build Figure 3: Ceva + Menelaus Dual Transversal & Harmonic Range (B, C; D, D') = -1.

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        900,
        430,
        "Ceva Props VII-VIII Menelaus Transversal EF meeting BC at Harmonic Conjugate D_prime",
    )
    # Choose weights (4, 5, 2) so D' = EF ∩ BC lies cleanly to the right of C!
    # Check: v=5, w=2 -> D = (10*0 + 28)/7 = (4, 0); D' divides BC in -w/v = -2/5 ->
    # (D' - B)/(C - D') = -2/5 => D' - 0 = -2/5 (14 - D') => 3/5 D' = -28/5 => D' = (-28/3, 0)!
    # Let's check ox=330, sc=32 -> D'=(-9.33, 0) -> x = 330 - 298 = 32, C=(14,0) -> x = 330 + 448 = 778!
    sol = solve_static_barycentrics(4, 5, 2, HERONIAN_VERTICES, name="P")
    ox, oy, sc = 325.0, 345.0, 33.0
    pa = _to_xy(sol.vertices[0], ox, oy, sc)
    pb = _to_xy(sol.vertices[1], ox, oy, sc)
    pc = _to_xy(sol.vertices[2], ox, oy, sc)
    pd = _to_xy(sol.foot_d, ox, oy, sc)
    pe = _to_xy(sol.foot_e, ox, oy, sc)
    pf = _to_xy(sol.foot_f, ox, oy, sc)
    pp = _to_xy(sol.center, ox, oy, sc)
    pdp = _to_xy((sp.Rational(-28, 3), sp.Integer(0)), ox, oy, sc)

    svg.polygon([pa, pb, pc], "ABC", fill="#0284c7", fill_opacity=0.07)
    svg.seg(pdp, pc, "lineBC", stroke="#64748b", width=1.8, dash="5 4")
    svg.seg(pa, pb, "ABC", width=2.1)
    svg.seg(pb, pc, "ABC", width=2.1)
    svg.seg(pc, pa, "ABC", width=2.1)

    svg.seg(pa, pd, "AD", stroke="#d97706", width=1.8)
    svg.seg(pb, pe, "BE", stroke="#d97706", width=1.8)
    svg.seg(pc, pf, "CF", stroke="#d97706", width=1.8)
    svg.seg(pdp, pe, "EF", stroke="#dc2626", width=2.1)

    for pt, ref, lbl, dx, dy in (
        (pa, "A", "A", 0.0, -16.0),
        (pb, "B", "B", 0.0, 18.0),
        (pc, "C", "C", 0.0, 18.0),
        (pd, "D", "D", 0.0, 18.0),
        (pe, "E", "E", 16.0, -8.0),
        (pf, "F", "F", -16.0, -8.0),
    ):
        svg.point(pt, ref)
        svg.label(pt, lbl, ref, dx=dx, dy=dy)

    svg.point(pp, "P", r=4.4, fill="#d97706")
    svg.label(pp, "P", "P", dx=15.0, dy=-10.0)
    svg.point(pdp, "D_prime", r=4.6, fill="#dc2626")
    svg.label(pdp, "D'", "D_prime", dy=18.0)

    svg.caption(
        450.0,
        28.0,
        "Liber Primus Elementum I & Props. VII-VIII: Ceva Concurrency + Menelaus Transversal EF",
    )
    svg.caption(
        450.0,
        402.0,
        "BD/DC = +2/5  and  BD'/D'C = -2/5   =>   Projective Harmonic Cross-Ratio (B, C; D, D') = -1",
    )
    return svg.render()


def build_fig04_isotomic_gergonne_nagel() -> str:
    """Build Figure 4: Liber Secundus Prop. I Incircle Contact X(7) & Isotomic Conjugate X(8).

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        880,
        450,
        "Ceva Liber Secundus Prop I Gergonne Contact Point X(7) and Isotomic Conjugate Nagel Point X(8)",
    )
    sol_g = solve_static_barycentrics(24, 28, 21, HERONIAN_VERTICES, name="X7")
    sol_n = solve_static_barycentrics(7, 6, 8, HERONIAN_VERTICES, name="X8")

    ox, oy, sc = 205.0, 380.0, 27.5
    pa = _to_xy(sol_g.vertices[0], ox, oy, sc)
    pb = _to_xy(sol_g.vertices[1], ox, oy, sc)
    pc = _to_xy(sol_g.vertices[2], ox, oy, sc)
    pd = _to_xy(sol_g.foot_d, ox, oy, sc)
    pe = _to_xy(sol_g.foot_e, ox, oy, sc)
    pf = _to_xy(sol_g.foot_f, ox, oy, sc)
    px7 = _to_xy(sol_g.center, ox, oy, sc)

    pdi = _to_xy(sol_n.foot_d, ox, oy, sc)
    pei = _to_xy(sol_n.foot_e, ox, oy, sc)
    pfi = _to_xy(sol_n.foot_f, ox, oy, sc)
    px8 = _to_xy(sol_n.center, ox, oy, sc)

    # Exact incircle on Heronian (13, 14, 15): Incenter I = (6, 4), inradius r = 4!
    inc = _to_xy((6, 4), ox, oy, sc)

    svg.polygon([pa, pb, pc], "ABC", fill="#0284c7", fill_opacity=0.06)
    svg.circle(inc, 4.0 * sc, "incircle", stroke="#0284c7", width=1.8)

    svg.seg(pa, pb, "ABC", width=2.0)
    svg.seg(pb, pc, "ABC", width=2.0)
    svg.seg(pc, pa, "ABC", width=2.0)

    # Equality ticks showing BD = D*C, CE = E*A, AF = F*B
    svg.seg(pb, pd, "BD_eq", stroke="#0284c7", width=2.2, ticks=1)
    svg.seg(pdi, pc, "BD_eq", stroke="#7c3aed", width=2.2, ticks=1)
    svg.seg(pc, pe, "CE_eq", stroke="#0284c7", width=2.2, ticks=2)
    svg.seg(pei, pa, "CE_eq", stroke="#7c3aed", width=2.2, ticks=2)
    svg.seg(pa, pf, "AF_eq", stroke="#0284c7", width=2.2, ticks=3)
    svg.seg(pfi, pb, "AF_eq", stroke="#7c3aed", width=2.2, ticks=3)

    # Gergonne cevians (solid amber) and Nagel isotomic cevians (dashed violet)
    svg.seg(pa, pd, "AD", stroke="#d97706", width=1.8)
    svg.seg(pb, pe, "BE", stroke="#d97706", width=1.8)
    svg.seg(pc, pf, "CF", stroke="#d97706", width=1.8)

    svg.seg(pa, pdi, "AD_iso", stroke="#7c3aed", width=1.7, dash="6 3")
    svg.seg(pb, pei, "BE_iso", stroke="#7c3aed", width=1.7, dash="6 3")
    svg.seg(pc, pfi, "CF_iso", stroke="#7c3aed", width=1.7, dash="6 3")

    for pt, ref, lbl, dx, dy in (
        (pa, "A", "A (5,12)", 0.0, -16.0),
        (pb, "B", "B (0,0)", -24.0, 16.0),
        (pc, "C", "C (14,0)", 26.0, 16.0),
        (pd, "D", "D", -8.0, 17.0),
        (pdi, "D_iso", "D*", 10.0, 17.0),
        (pe, "E", "E", 16.0, 6.0),
        (pei, "E_iso", "E*", 16.0, -10.0),
        (pf, "F", "F", -16.0, -8.0),
        (pfi, "F_iso", "F*", -18.0, 6.0),
    ):
        svg.point(pt, ref)
        svg.label(pt, lbl, ref, dx=dx, dy=dy, size=13)

    svg.point(px7, "X7", r=4.6, fill="#d97706")
    svg.label(px7, "X(7)", "X7", dx=-26.0, dy=-10.0, size=13)
    svg.point(px8, "X8", r=4.6, fill="#7c3aed")
    svg.label(px8, "X(8)", "X8", dx=28.0, dy=8.0, size=13)

    svg.caption(
        440.0,
        28.0,
        "Liber Secundus Prop. I & Corollarium: Contact Point X(7) (24:28:21) <-> Isotomic Nagel X(8) (7:6:8)",
    )
    svg.caption(
        440.0,
        422.0,
        "Midpoint Reflection Swaps Ratios (AF/FB -> FB/AF), Preserving Unit Ceva Product = 1",
    )
    return svg.render()


def build_fig05_spread_ceva_heronian() -> str:
    """Build Figure 5: Canonical Rational Centers on Heronian (13,14,15) & Spread Ceva.

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        900,
        450,
        "Canonical Rational Triangle Centers and Rational Trigonometry Spread Ceva on Heronian (13,14,15)",
    )
    centers = evaluate_canonical_centers()
    spread_res = verify_spread_ceva()
    sol_x1 = centers["X(1)"]

    ox, oy, sc = 195.0, 380.0, 27.5
    pa = _to_xy(sol_x1.vertices[0], ox, oy, sc)
    pb = _to_xy(sol_x1.vertices[1], ox, oy, sc)
    pc = _to_xy(sol_x1.vertices[2], ox, oy, sc)
    pd = _to_xy(sol_x1.foot_d, ox, oy, sc)
    pe = _to_xy(sol_x1.foot_e, ox, oy, sc)
    pf = _to_xy(sol_x1.foot_f, ox, oy, sc)

    svg.polygon([pa, pb, pc], "ABC", fill="#0284c7", fill_opacity=0.06)
    svg.seg(pa, pb, "ABC", width=2.1)
    svg.seg(pb, pc, "ABC", width=2.1)
    svg.seg(pc, pa, "ABC", width=2.1)

    svg.seg(pa, pd, "AD", stroke="#0284c7", width=1.6)
    svg.seg(pb, pe, "BE", stroke="#0284c7", width=1.6)
    svg.seg(pc, pf, "CF", stroke="#0284c7", width=1.6)

    # Vertex spread arcs around A, B, C
    svg.arc(pa, 34.0, 247.38, 278.13, "sA", stroke="#d97706", width=2.0, layer="graphics")
    svg.arc(pa, 42.0, 278.13, 306.87, "sA", stroke="#16a34a", width=2.0, layer="graphics")
    svg.arc(pb, 38.0, 0.0, 33.69, "sB", stroke="#d97706", width=2.0, layer="graphics")
    svg.arc(pb, 46.0, 33.69, 67.38, "sB", stroke="#16a34a", width=2.0, layer="graphics")
    svg.arc(pc, 38.0, 126.87, 153.43, "sC", stroke="#d97706", width=2.0, layer="graphics")
    svg.arc(pc, 46.0, 153.43, 180.0, "sC", stroke="#16a34a", width=2.0, layer="graphics")

    for pt, ref, lbl, dx, dy in (
        (pa, "A", "A (5,12)", 0.0, -16.0),
        (pb, "B", "B (0,0)", -24.0, 16.0),
        (pc, "C", "C (14,0)", 26.0, 16.0),
        (pd, "D", "D", 0.0, 16.0),
        (pe, "E", "E", 16.0, -6.0),
        (pf, "F", "F", -16.0, -6.0),
    ):
        svg.point(pt, ref)
        svg.label(pt, lbl, ref, dx=dx, dy=dy, size=13)

    # Plot all 6 interior centers in Q^2
    offsets = {
        "X(1)": ("X1", "#0284c7", -26.0, -10.0),
        "X(2)": ("X2", "#16a34a", 28.0, -8.0),
        "X(4)": ("X4", "#dc2626", -28.0, -8.0),
        "X(6)": ("X6", "#7c3aed", -28.0, 10.0),
        "X(7)": ("X7", "#d97706", -26.0, 14.0),
        "X(8)": ("X8", "#0d9488", 28.0, 12.0),
    }
    for key, (ref, col, dx, dy) in offsets.items():
        cpt = _to_xy(centers[key].center, ox, oy, sc)
        svg.point(cpt, ref, r=4.2, fill=col)
        svg.label(cpt, key, ref, dx=dx, dy=dy, size=12, italic=False)

    # Exact rational spread callout panel on the right
    svg.caption(740.0, 110.0, "Exact Spreads over Q (X(1)):", size=13)
    svg.caption(
        740.0,
        138.0,
        f"s(BAD) = {spread_res.spread_bad},  s(DAC) = {spread_res.spread_dac}",
        size=12,
    )
    svg.caption(
        740.0,
        164.0,
        f"s(CBE) = {spread_res.spread_cbe},  s(EBA) = {spread_res.spread_eba}",
        size=12,
    )
    svg.caption(
        740.0,
        190.0,
        f"s(ACF) = {spread_res.spread_acf},  s(FCB) = {spread_res.spread_fcb}",
        size=12,
    )
    svg.caption(740.0, 222.0, "Spread Product = 1  |  Quadrance Product = 1", size=12)

    svg.caption(
        450.0,
        28.0,
        "Heronian Triangle (13, 14, 15): Exact Rational Centers X(1), X(2), X(4), X(6), X(7), X(8)",
    )
    svg.caption(
        450.0,
        422.0,
        "Spread Ceva Theorem: [s(BAD)/s(DAC)] * [s(CBE)/s(EBA)] * [s(ACF)/s(FCB)] = 1  (Zero Radicals)",
    )
    return svg.render()


def build_fig06_pentagon_multilateral_ceva() -> str:
    """Build Figure 6: Odd Pentagon Multilateral Ceva & Circumscribed Ellipse Lemma I.

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        940,
        440,
        "Ceva Liber Secundus Odd Pentagon Concurrency and Lemma I Circumscribed Ellipse Projection",
    )
    pent = verify_odd_polygon_ceva(RATIONAL_PENTAGON, (4, 4))
    ox1, oy1, sc1 = 105.0, 360.0, 25.5
    v_pts = [_to_xy(v, ox1, oy1, sc1) for v in pent.vertices]
    q_pts = [_to_xy(q, ox1, oy1, sc1) for q in pent.feet]
    pp = _to_xy(pent.center, ox1, oy1, sc1)

    svg.polygon(v_pts, "pentagon", fill="#0284c7", fill_opacity=0.07)
    for i in range(5):
        svg.seg(v_pts[i], v_pts[(i + 1) % 5], "pentagon", width=2.0)
        svg.seg(v_pts[i], q_pts[i], f"cev{i}", stroke="#d97706", width=1.65)

    v_offsets = [(0.0, 16.0), (16.0, 14.0), (18.0, 0.0), (0.0, -16.0), (-18.0, 0.0)]
    q_offsets = [(14.0, -8.0), (-10.0, -14.0), (-15.0, 8.0), (0.0, 16.0), (16.0, 8.0)]
    for i in range(5):
        svg.point(v_pts[i], f"V{i}")
        svg.label(v_pts[i], f"V_{i}", f"V{i}", dx=v_offsets[i][0], dy=v_offsets[i][1], size=13)
        svg.point(q_pts[i], f"Q{i}", r=3.2, fill="#0284c7")
        svg.label(q_pts[i], f"Q_{i}", f"Q{i}", dx=q_offsets[i][0], dy=q_offsets[i][1], size=12)

    svg.point(pp, "P", r=4.6, fill="#dc2626")
    svg.label(pp, "P", "P", dx=14.0, dy=-10.0)
    svg.caption(235.0, 32.0, "Liber Secundus: Odd (2m+1)-gon Ceva Concurrency")
    svg.caption(235.0, 406.0, "Cyclic Opposite-Side Product = (5/6)*(2)*(13/10)*(3/4)*(8/13) = 1")

    # Right panel: Liber Secundus Lemma I (tab. 4. figs. 32-35) — Circle -> Cylindrical Ellipse
    # Tangent angles around circle of radius R=1 -> affine squeeze (rx=105, ry=64)
    cx_c, cy_c, r_c = 695.0, 140.0, 56.0
    cx_e, cy_e, sx_e, sy_e = 695.0, 305.0, 102.0, 54.0
    angles = [25.0, 95.0, 168.0, 238.0, 312.0]

    def _tangent_poly(cx: float, cy: float, rx: float, ry: float) -> tuple[list[Point2F], list[Point2F]]:
        t_contacts: list[Point2F] = []
        verts: list[Point2F] = []
        n_a = len(angles)
        for k in range(n_a):
            a_cur = math.radians(angles[k])
            a_prv = math.radians(angles[(k - 1) % n_a])
            t_contacts.append((cx + rx * math.cos(a_cur), cy - ry * math.sin(a_cur)))
            # Intersection of cos(a_prv)*X + sin(a_prv)*Y = 1 and cos(a_cur)*X + sin(a_cur)*Y = 1
            det = math.sin(a_cur - a_prv)
            ux = (math.sin(a_cur) - math.sin(a_prv)) / det
            uy = (math.cos(a_prv) - math.cos(a_cur)) / det
            verts.append((cx + rx * ux, cy - ry * uy))
        return verts, t_contacts

    vc_pts, tc_pts = _tangent_poly(cx_c, cy_c, r_c, r_c)
    ve_pts, te_pts = _tangent_poly(cx_e, cy_e, sx_e, sy_e)

    svg.circle((cx_c, cy_c), r_c, "circleC", stroke="#0284c7", width=1.8)
    svg.ellipse((cx_e, cy_e), sx_e, sy_e, "ellipseE", stroke="#7c3aed", width=1.9)
    for k in range(5):
        svg.seg(vc_pts[k], vc_pts[(k + 1) % 5], "circleC", width=1.5)
        svg.seg(ve_pts[k], ve_pts[(k + 1) % 5], "ellipseE", width=1.7)
        svg.seg(tc_pts[k], te_pts[k], "projCyl", stroke="#94a3b8", width=1.1, dash="4 3")
        svg.point(tc_pts[k], "circleC", r=2.9, fill="#0284c7")
        svg.point(te_pts[k], "ellipseE", r=3.1, fill="#7c3aed")

    svg.caption(695.0, 32.0, "Lib. II Lemma I: Borelli-Serenus Cylindrical Section")
    svg.caption(695.0, 406.0, "Tab. 4, Figs. 32-35 — Affine Projection Preserves Contact Ratios = 1")
    return svg.render()


def build_fig07_tetrahedron_seven_lines() -> str:
    """Build Figure 7: Liber Primus Prop. XXIII 3D Tetrahedron 7-Line Static Equilibrium.

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        880,
        460,
        "Ceva Liber Primus Prop XXIII 3D Tetrahedron Seven-Line Static Equilibrium at Center O",
    )
    tet = solve_tetrahedron_static_equilibrium((2, 3, 5, 8), RATIONAL_TETRAHEDRON)
    ox, oy, sc = 265.0, 375.0, 34.0

    va, vb, vc, vd = (_proj3d(v, ox, oy, sc) for v in tet.vertices)
    po = _proj3d(tet.center_of_gravity, ox, oy, sc)
    v_map = {"A": va, "B": vb, "C": vc, "D": vd}
    g_map = {k: _proj3d(pt, ox, oy, sc) for k, pt in tet.face_centers.items()}
    e_map = {k: _proj3d(pt, ox, oy, sc) for k, pt in tet.edge_fulcrums.items()}

    svg.polygon([va, vb, vd], "tetABCD", fill="#0284c7", fill_opacity=0.06)
    svg.polygon([vb, vc, vd], "tetABCD", fill="#7c3aed", fill_opacity=0.05)

    # 6 Tetrahedron edges (AC hidden-dashed, others solid)
    svg.seg(va, vc, "tetABCD", width=1.6, dash="6 4", stroke="#64748b")
    for p1, p2 in ((va, vb), (vb, vc), (va, vd), (vb, vd), (vc, vd)):
        svg.seg(p1, p2, "tetABCD", width=2.1)

    # 4 Vertex-to-opposite-face-barycenter cevians (amber)
    for k in ("A", "B", "C", "D"):
        svg.seg(v_map[k], g_map[k], f"AG_{k}", stroke="#d97706", width=1.7)
        svg.point(g_map[k], f"G_{k}", r=3.2, fill="#d97706")

    # 3 Opposite-edge fulcrum bimedians (emerald dashed)
    for e1, e2 in (("AB", "CD"), ("AC", "BD"), ("AD", "BC")):
        svg.seg(
            e_map[e1],
            e_map[e2],
            f"B_{e1}_{e2}",
            stroke="#16a34a",
            width=1.75,
            dash="5 3",
        )
        svg.point(e_map[e1], f"E_{e1}", r=3.0, fill="#16a34a")
        svg.point(e_map[e2], f"E_{e2}", r=3.0, fill="#16a34a")

    for k, lbl, dx, dy in (
        ("A", "A (m=2)", -32.0, 14.0),
        ("B", "B (m=3)", 32.0, 14.0),
        ("C", "C (m=5)", -34.0, -10.0),
        ("D", "D (m=8)", 0.0, -18.0),
    ):
        svg.point(v_map[k], k, r=3.8)
        svg.label(v_map[k], lbl, k, dx=dx, dy=dy, size=13)

    svg.point(po, "O", r=5.2, fill="#dc2626")
    svg.label(po, "O", "O", dx=18.0, dy=-10.0, size=15)

    svg.caption(
        440.0,
        28.0,
        "Liber Primus Prop. XXIII (Tab. 3, Fig. 28): 3D Tetrahedron 7-Line Equilibrium ('mira quadam concordia')",
    )
    svg.caption(
        440.0,
        432.0,
        "4 Face-Barycenter Cevians (AG_A..DG_D) + 3 Skew-Edge Bimedians Concur at Unique Center O",
    )
    return svg.render()


def build_fig08_appendix_ungula_indivisibles() -> str:
    """Build Figure 8: Appendix Geometrica Lune, Ungula (2/3 Prism), & Indivisibles Caution.

    Returns:
        Rendered SVG markup.
    """
    svg = EuclidSVGBuilder(
        960,
        430,
        "Ceva Appendix Geometrica Hippocratean Lune, Cylindrical Ungula 2/3 Prism, and Indivisibles Caution",
    )

    # Panel 1 (x: 40..300): Prop. II Hippocratean Lune [Lune] = [Triangle ABC] = 1/2 R^2
    # Right isosceles triangle C_0=(95, 295), A=(95, 165), B=(225, 295) with R=130
    c0 = (95.0, 295.0)
    la = (95.0, 165.0)
    lb = (225.0, 295.0)
    mid_ab = (160.0, 230.0)
    r_quad = 130.0
    r_hyp = 130.0 / math.sqrt(2.0)

    # Lune filled path: semicircle from B(315 deg) CCW to A(135 deg) around mid_ab, then quadrant back to B
    lune_d = (
        f"M {lb[0]:.2f} {lb[1]:.2f} "
        f"A {r_hyp:.2f} {r_hyp:.2f} 0 0 0 {la[0]:.2f} {la[1]:.2f} "
        f"A {r_quad:.2f} {r_quad:.2f} 0 0 1 {lb[0]:.2f} {lb[1]:.2f} Z"
    )
    svg.path_highlight(lune_d, "lune", fill="#d97706", fill_opacity=0.24)
    svg.polygon([c0, la, lb], "triABC", fill="#0284c7", fill_opacity=0.16)
    svg.seg(c0, la, "triABC", width=1.9)
    svg.seg(c0, lb, "triABC", width=1.9)
    svg.seg(la, lb, "triABC", width=1.9)
    svg.arc(c0, r_quad, 0.0, 90.0, "arcQuad", stroke="#0284c7", width=1.9)
    svg.arc(mid_ab, r_hyp, -45.0, 135.0, "arcHyp", stroke="#d97706", width=2.1)
    svg.point(c0, "triABC")
    svg.point(la, "lune")
    svg.point(lb, "lune")
    svg.label((195.0, 182.0), "Lune", "lune", size=13, italic=False)
    svg.label((135.0, 265.0), "1/2 R^2", "triABC", size=12, italic=False)
    svg.caption(165.0, 34.0, "App. Prop. II: Lune = Triangle")
    svg.caption(165.0, 396.0, "[Lune] = [Delta] = 1/2 R^2")

    # Panel 2 (x: 340..630): Prop. VII Cylindrical Ungula = 2/3 Circumscribed Prism
    uc = (485.0, 290.0)
    rx_u, ry_u, h_u = 105.0, 38.0, 145.0
    u_left = (uc[0] - rx_u, uc[1])
    u_right = (uc[0] + rx_u, uc[1])
    u_front = (uc[0], uc[1] + ry_u)
    u_top_front = (uc[0], uc[1] + ry_u - h_u)
    p_top_l = (uc[0] - rx_u, uc[1] + ry_u - h_u)
    p_top_r = (uc[0] + rx_u, uc[1] + ry_u - h_u)
    p_bot_l = (uc[0] - rx_u, uc[1] + ry_u)
    p_bot_r = (uc[0] + rx_u, uc[1] + ry_u)

    # Representative right-triangle Cavalieri slice at x_s = +0.42 R
    th = 0.42
    sx_b = uc[0] + rx_u * th
    sy_front = uc[1] + ry_u * math.sqrt(1.0 - th * th)
    sh_slice = h_u * math.sqrt(1.0 - th * th)
    s_base_back = (sx_b, uc[1])
    s_base_front = (sx_b, sy_front)
    s_apex = (sx_b, sy_front - sh_slice)

    svg.polygon([s_base_back, s_base_front, s_apex], "sliceTri", fill="#16a34a", fill_opacity=0.25)
    svg.seg(u_left, p_bot_l, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(u_right, p_bot_r, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(p_bot_l, p_bot_r, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(p_bot_l, p_top_l, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(p_bot_r, p_top_r, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(p_top_l, p_top_r, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(u_left, p_top_l, "prism", stroke="#94a3b8", width=1.2, dash="4 3")
    svg.seg(u_right, p_top_r, "prism", stroke="#94a3b8", width=1.2, dash="4 3")

    svg.seg(u_left, u_right, "ungula", width=2.0)
    svg.seg(u_front, u_top_front, "ungula", stroke="#d97706", width=2.1)
    svg.seg(u_left, u_top_front, "ungula", stroke="#d97706", width=1.9)
    svg.seg(u_right, u_top_front, "ungula", stroke="#d97706", width=1.9)
    svg.elements.append(
        f'    <path class="geom-arc" d="M {u_left[0]:.2f} {u_left[1]:.2f} '
        f'A {rx_u:.2f} {ry_u:.2f} 0 0 0 {u_right[0]:.2f} {u_right[1]:.2f}" '
        'fill="none" stroke="currentColor" stroke-width="2.0" data-ref="ungula"/>'
    )
    svg.seg(s_base_back, s_base_front, "sliceTri", stroke="#16a34a", width=1.8)
    svg.seg(s_base_front, s_apex, "sliceTri", stroke="#16a34a", width=1.8)
    svg.seg(s_apex, s_base_back, "sliceTri", stroke="#16a34a", width=1.8)

    svg.caption(485.0, 34.0, "App. Prop. VII: Cylindrical Ungula")
    svg.caption(485.0, 396.0, "Vol(Ungula) = 2/3 R^2 H = 2/3 Prism")

    # Panel 3 (x: 660..930): Prop. XIII Hemisphere 5:3 CG + Closing Indivisibles Slant Paradox
    hc = (795.0, 295.0)
    r_h = 110.0
    v_top = (795.0, 295.0 - r_h)
    cg_h = (795.0, 295.0 - (3.0 / 8.0) * r_h)  # 5:3 from vertex to base!

    svg.arc(hc, r_h, 0.0, 180.0, "hemi", stroke="#0284c7", width=2.1)
    svg.seg((hc[0] - r_h, hc[1]), (hc[0] + r_h, hc[1]), "hemi", width=2.0)
    svg.seg(v_top, hc, "axisVO", stroke="#64748b", width=1.6, dash="4 3")

    # Naive horizontal parallel chord slice vs true slant arc element ds = dz / cos(alpha)
    y1_s = 295.0 - 0.62 * r_h
    y2_s = 295.0 - 0.76 * r_h
    dx1 = math.sqrt(r_h * r_h - (295.0 - y1_s) ** 2)
    dx2 = math.sqrt(r_h * r_h - (295.0 - y2_s) ** 2)
    svg.seg((hc[0] - dx1, y1_s), (hc[0] + dx1, y1_s), "chordSlice", stroke="#dc2626", width=1.6, dash="4 3")
    svg.seg((hc[0] - dx2, y2_s), (hc[0] + dx2, y2_s), "chordSlice", stroke="#dc2626", width=1.6, dash="4 3")
    svg.seg((hc[0] + dx1, y1_s), (hc[0] + dx2, y2_s), "slantArc", stroke="#16a34a", width=3.2)

    svg.point(v_top, "axisVO")
    svg.point(hc, "axisVO")
    svg.point(cg_h, "cgH", r=4.6, fill="#d97706")
    svg.label(v_top, "V", "axisVO", dy=-14.0, size=13)
    svg.label(hc, "O", "axisVO", dy=15.0, size=13)
    svg.label(cg_h, "G (5:3)", "cgH", dx=34.0, size=12, italic=False)
    svg.label((hc[0] + dx1 + 26.0, (y1_s + y2_s) / 2.0), "ds != dz", "slantArc", size=12, italic=False)

    svg.caption(795.0, 34.0, "Prop. XIII (5:3 CG) & Indivisibles Paradox")
    svg.caption(795.0, 396.0, "Curved Surface Requires Slant Frustum ds, Not dz")
    return svg.render()


def generate_all_figures(output_dir: Path = OUT_DIR) -> list[Path]:
    """Generate all 8 ``.euclid-graphic`` SVG figures into ``output_dir``.

    Args:
        output_dir: Destination directory for ``.svg`` files.

    Returns:
        Ordered list of written SVG paths.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    specs: tuple[tuple[str, str], ...] = (
        ("fig01_statica_lever_elements.svg", build_fig01_statica_lever_elements()),
        ("fig02_ceva_interior_exterior.svg", build_fig02_ceva_interior_exterior()),
        ("fig03_menelaus_harmonic_quadrangle.svg", build_fig03_menelaus_harmonic_quadrangle()),
        ("fig04_isotomic_gergonne_nagel.svg", build_fig04_isotomic_gergonne_nagel()),
        ("fig05_spread_ceva_heronian.svg", build_fig05_spread_ceva_heronian()),
        ("fig06_pentagon_multilateral_ceva.svg", build_fig06_pentagon_multilateral_ceva()),
        ("fig07_tetrahedron_seven_lines.svg", build_fig07_tetrahedron_seven_lines()),
        ("fig08_appendix_ungula_indivisibles.svg", build_fig08_appendix_ungula_indivisibles()),
    )
    written: list[Path] = []
    for filename, content in specs:
        dest = output_dir / filename
        dest.write_text(content, encoding="utf-8")
        written.append(dest)
    return written


def main() -> None:
    """Entry point writing all 8 SVG plates to ``docsrc/_static/figures/``."""
    paths = generate_all_figures()
    for p in paths:
        print(f"Wrote {p.relative_to(OUT_DIR.parents[2])}")


if __name__ == "__main__":
    main()
