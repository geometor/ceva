#!/usr/bin/env python3
"""Generate 22 calibrated 5-layer .euclid-graphic SVG vectorizations paired to Ceva (1678) plates.

Each SVG is placed directly alongside its cropped archival bitmap ``<NNNN>.g<k>.png``
inside the corresponding Book Codex leaf folder and strictly obeys:
- ``class="euclid-graphic"`` with ``<defs>`` tick markers ``#geom-tick-1..3``
- 5 canonical ``<g>`` layers in exact order: ``elements``, ``graphics``, ``highlights``, ``points``, ``labels``
- 3-vertex midpoint ``<path d="M x1 y1 L mx my L x2 y2">`` segments
- Theme-adaptive CSS variables (``--geom-primary``, ``--geom-secondary``, ``--geom-highlight``, etc.)
- Exact 1678 Ceva vertex letters wired via ``data-ref`` attributes for ``:g:`` / ``:eq:`` hover interaction.
"""

from __future__ import annotations

import html
import math
from pathlib import Path
from typing import Sequence

CODEX_DIR = Path(__file__).resolve().parents[1] / "docsrc" / "de_lineis_rectis"

Point2F = tuple[float, float]

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


def lerp(a: Point2F, b: Point2F, t: float) -> Point2F:
    """Linearly interpolate between two 2D points."""
    return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))


def intersect_lines(p1: Point2F, p2: Point2F, p3: Point2F, p4: Point2F) -> Point2F:
    """Return exact intersection of lines p1-p2 and p3-p4."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-9:
        return lerp(p1, p2, 0.5)
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)


class CalibratedSVG:
    """5-layer theme-adaptive .euclid-graphic SVG builder."""

    def __init__(self, width: int, height: int, aria_label: str) -> None:
        """Initialize an empty 5-layer SVG canvas."""
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
        stroke: str = "var(--geom-primary, currentColor)",
        width: float = 2.0,
        dash: str | None = None,
        ticks: int = 0,
    ) -> None:
        """Add a 3-vertex midpoint path segment to #elements."""
        x1, y1 = p1
        x2, y2 = p2
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        attrs = [
            f'd="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"',
            f'data-ref="{html.escape(ref, quote=True)}"',
            'class="geom-line"',
            'fill="none"',
            f'stroke="{stroke}"',
            f'stroke-width="{width:.2f}"',
            'stroke-linecap="round"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if ticks in (1, 2, 3):
            attrs.append(f'marker-mid="url(#geom-tick-{ticks})"')
        self.elements.append(f"    <path {' '.join(attrs)}/>")

    def poly(
        self,
        pts: Sequence[Point2F],
        ref: str,
        *,
        fill: str = "var(--geom-accent-fill, rgba(180,120,40,0.12))",
        stroke: str = "none",
        layer: str = "graphics",
    ) -> None:
        """Add a shaded polygon to #graphics or #highlights."""
        coords = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        el = (
            f'    <polygon points="{coords}" data-ref="{html.escape(ref, quote=True)}" '
            f'fill="{fill}" stroke="{stroke}"/>'
        )
        if layer == "highlights":
            self.highlights.append(el)
        else:
            self.graphics.append(el)

    def circle(
        self,
        center: Point2F,
        r: float,
        ref: str,
        *,
        stroke: str = "var(--geom-primary, currentColor)",
        width: float = 1.9,
        fill: str = "none",
        dash: str | None = None,
        layer: str = "elements",
    ) -> None:
        """Add a circle element to #elements or #graphics."""
        attrs = [
            f'cx="{center[0]:.2f}"',
            f'cy="{center[1]:.2f}"',
            f'r="{r:.2f}"',
            f'data-ref="{html.escape(ref, quote=True)}"',
            f'fill="{fill}"',
            f'stroke="{stroke}"',
            f'stroke-width="{width:.2f}"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        el = f"    <circle {' '.join(attrs)}/>"
        if layer == "graphics":
            self.graphics.append(el)
        else:
            self.elements.append(el)

    def ellipse(
        self,
        center: Point2F,
        rx: float,
        ry: float,
        ref: str,
        *,
        rot: float = 0.0,
        stroke: str = "var(--geom-primary, currentColor)",
        width: float = 1.9,
        fill: str = "none",
        dash: str | None = None,
        layer: str = "elements",
    ) -> None:
        """Add an ellipse element to #elements or #graphics."""
        attrs = [
            f'cx="{center[0]:.2f}"',
            f'cy="{center[1]:.2f}"',
            f'rx="{rx:.2f}"',
            f'ry="{ry:.2f}"',
            f'data-ref="{html.escape(ref, quote=True)}"',
            f'fill="{fill}"',
            f'stroke="{stroke}"',
            f'stroke-width="{width:.2f}"',
        ]
        if rot:
            attrs.append(f'transform="rotate({rot:.2f} {center[0]:.2f} {center[1]:.2f})"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        el = f"    <ellipse {' '.join(attrs)}/>"
        if layer == "graphics":
            self.graphics.append(el)
        else:
            self.elements.append(el)

    def path(
        self,
        d: str,
        ref: str,
        *,
        stroke: str = "var(--geom-primary, currentColor)",
        width: float = 1.9,
        fill: str = "none",
        dash: str | None = None,
        layer: str = "elements",
    ) -> None:
        """Add an SVG curve path to the requested layer."""
        attrs = [
            f'd="{d}"',
            f'data-ref="{html.escape(ref, quote=True)}"',
            f'fill="{fill}"',
            f'stroke="{stroke}"',
            f'stroke-width="{width:.2f}"',
            'stroke-linecap="round"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        el = f"    <path {' '.join(attrs)}/>"
        if layer == "graphics":
            self.graphics.append(el)
        elif layer == "highlights":
            self.highlights.append(el)
        else:
            self.elements.append(el)

    def pt(
        self,
        pos: Point2F,
        ref: str,
        label: str | None = None,
        *,
        dx: float = 10.0,
        dy: float = -8.0,
        r: float = 4.0,
        highlight: bool = False,
        anchor: str = "middle",
    ) -> None:
        """Add a geometric point marker and optional text label."""
        fill = "var(--geom-highlight, #d97706)" if highlight else "var(--geom-point-fill, #ffffff)"
        stroke = "var(--geom-highlight, #d97706)" if highlight else "var(--geom-primary, currentColor)"
        self.points.append(
            f'    <circle cx="{pos[0]:.2f}" cy="{pos[1]:.2f}" r="{r:.2f}" '
            f'data-ref="{html.escape(ref, quote=True)}" class="geom-point" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>'
        )
        if highlight:
            self.highlights.append(
                f'    <circle cx="{pos[0]:.2f}" cy="{pos[1]:.2f}" r="{r + 4.5:.2f}" '
                f'data-ref="{html.escape(ref, quote=True)}" fill="none" '
                f'stroke="var(--geom-highlight, #d97706)" stroke-width="1.2" opacity="0.55"/>'
            )
        if label is not None:
            self.text((pos[0] + dx, pos[1] + dy), label, ref, anchor=anchor, highlight=highlight)

    def text(
        self,
        pos: Point2F,
        content: str,
        ref: str,
        *,
        anchor: str = "middle",
        size: int = 16,
        italic: bool = True,
        highlight: bool = False,
        weight: str = "600",
    ) -> None:
        """Add an escaped serif text label to #labels."""
        fill = "var(--geom-highlight, #d97706)" if highlight else "var(--geom-text, currentColor)"
        style = "italic" if italic else "normal"
        self.labels.append(
            f'    <text x="{pos[0]:.2f}" y="{pos[1]:.2f}" data-ref="{html.escape(ref, quote=True)}" '
            f'text-anchor="{anchor}" font-family="Georgia, \'Times New Roman\', serif" '
            f'font-size="{size}" font-style="{style}" font-weight="{weight}" fill="{fill}">'
            f"{html.escape(content)}</text>"
        )

    def weight_badge(self, pos: Point2F, label: str, ref: str) -> None:
        """Add a dashed circular static-weight badge."""
        self.graphics.append(
            f'    <circle cx="{pos[0]:.2f}" cy="{pos[1]:.2f}" r="13.5" '
            f'data-ref="{html.escape(ref, quote=True)}" '
            f'fill="var(--geom-accent-fill, rgba(217,119,6,0.14))" '
            f'stroke="var(--geom-highlight, #d97706)" stroke-width="1.4" stroke-dasharray="3 2"/>'
        )
        self.text((pos[0], pos[1] + 5.0), label, ref, size=14, italic=False, highlight=True)

    def render(self) -> str:
        """Serialize the 5-layer .euclid-graphic SVG markup."""
        return "\n".join(
            [
                f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
                f'class="euclid-graphic" role="img" aria-label="{self.aria_label}">',
                DEFS_BLOCK,
                '  <g id="elements">',
                *self.elements,
                "  </g>",
                '  <g id="graphics">',
                *self.graphics,
                "  </g>",
                '  <g id="highlights" style="pointer-events: none;">',
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
        )


def write_svg(rel_path: str, svg: CalibratedSVG) -> None:
    """Write rendered SVG text to its codex leaf path."""
    out = CODEX_DIR / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg.render(), encoding="utf-8")


def build_all() -> int:
    """Generate all 22 calibrated 5-layer .euclid-graphic SVGs."""
    count = 0

    # 1. Tab. I Fig. 1-3: Axioms & Lever Law
    s = CalibratedSVG(520, 260, "Ceva 1678 Tabula I Figs. 1-3: Archimedean Lever Balance")
    A, B = (90.0, 125.0), (430.0, 125.0)
    F = lerp(A, B, 0.38)
    K = lerp(A, B, 0.65)
    s.seg(A, B, "AB", width=2.6)
    s.seg(A, F, "AF", stroke="var(--geom-highlight, #d97706)", width=2.8)
    s.seg(F, B, "FB", stroke="var(--geom-secondary, #475569)", width=2.4)
    s.poly([(F[0], F[1] + 4), (F[0] - 18, F[1] + 38), (F[0] + 18, F[1] + 38)], "F")
    s.seg((A[0], A[1]), (A[0], A[1] + 45), "A_cord", dash="4 3", width=1.4)
    s.seg((B[0], B[1]), (B[0], B[1] + 45), "B_cord", dash="4 3", width=1.4)
    s.weight_badge((A[0], A[1] + 62), "u", "mA")
    s.weight_badge((B[0], B[1] + 62), "v", "mB")
    s.pt(A, "A", "A", dx=0, dy=-16)
    s.pt(F, "F", "F", dx=0, dy=-16, highlight=True)
    s.pt(K, "K", "K", dx=0, dy=-16)
    s.pt(B, "B", "B", dx=0, dy=-16)
    s.text((260, 232), "A : B = BF : FA  (Axioma I-II, Lemma I-II)", "eq_lever", size=14, italic=False)
    write_svg("liber_primus/axiomata_lemmata/0103.g1.svg", s)
    count += 1

    # 2. Tab. I Fig. 4: Elementum I (Menelaus Sector)
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula I Fig. 4: Elementum I Menelaus Sector")
    A, E, C = (210.0, 58.0), (85.0, 290.0), (385.0, 290.0)
    D = lerp(A, E, 0.45)
    B = lerp(A, C, 0.56)
    F = intersect_lines(E, B, C, D)
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(C, D, "CD", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.weight_badge((165, 58), "G", "G")
    s.weight_badge((85, 325), "I", "I")
    s.weight_badge((385, 325), "H", "H")
    s.pt(A, "A", "A", dx=12, dy=-8)
    s.pt(E, "E", "E", dx=-16, dy=6)
    s.pt(C, "C", "C", dx=16, dy=6)
    s.pt(D, "D", "D", dx=-18, dy=-4)
    s.pt(B, "B", "B", dx=16, dy=-4)
    s.pt(F, "F", "F", dx=2, dy=20, highlight=True)
    write_svg("liber_primus/prop_01/0103.g4.svg", s)
    count += 1

    # 3. Tab. I Fig. 5: Elementum II (Interior Ceva)
    s = CalibratedSVG(460, 380, "Ceva 1678 Tabula I Fig. 5: Elementum II Interior Ceva Concurrency")
    A, E, C = (210.0, 56.0), (80.0, 300.0), (388.0, 295.0)
    D = lerp(A, E, 0.58)
    B = lerp(A, C, 0.44)
    F = intersect_lines(E, B, C, D)
    K = intersect_lines(A, F, E, C)
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.07))")
    s.seg(A, E, "AE", width=2.3)
    s.seg(A, C, "AC", width=2.3)
    s.seg(E, C, "EC", width=2.3)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, D, "CD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, K, "AK", stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.weight_badge((250, 54), "G", "G")
    s.weight_badge((80, 336), "I", "I")
    s.weight_badge((388, 332), "H", "H")
    s.pt(A, "A", "A", dx=-14, dy=-4)
    s.pt(E, "E", "E", dx=-16, dy=6)
    s.pt(C, "C", "C", dx=16, dy=6)
    s.pt(D, "D", "D", dx=-18, dy=-2)
    s.pt(B, "B", "B", dx=16, dy=-4)
    s.pt(K, "K", "K", dx=0, dy=22)
    s.pt(F, "F", "F", dx=14, dy=-10, highlight=True)
    write_svg("liber_primus/prop_02/0103.g5.svg", s)
    count += 1

    # 4. Tab. I Fig. 6: Elementum III (Exterior Ceva & Negative Weights)
    s = CalibratedSVG(460, 380, "Ceva 1678 Tabula I Fig. 6: Elementum III Negative Weights")
    E, A, C = (225.0, 56.0), (112.0, 305.0), (355.0, 305.0)
    F = lerp(E, A, 0.56)
    D = lerp(E, C, 0.48)
    B = lerp(A, C, 0.42)
    G = intersect_lines(E, B, F, D)
    s.poly([E, A, C], "EAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.07))")
    s.seg(E, A, "EA", width=2.3)
    s.seg(E, C, "EC", width=2.3)
    s.seg(A, C, "AC", width=2.3)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.seg(F, D, "FD", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.weight_badge((182, 56), "I", "I")
    s.weight_badge((268, 56), "K", "K")
    s.weight_badge((112, 342), "H", "H")
    s.weight_badge((355, 342), "F-A", "L")
    s.pt(E, "E", "E", dx=0, dy=-16)
    s.pt(A, "A", "A", dx=-16, dy=6)
    s.pt(C, "C", "C", dx=16, dy=6)
    s.pt(F, "F", "F", dx=-18, dy=0)
    s.pt(D, "D", "D", dx=18, dy=0)
    s.pt(B, "B", "B", dx=6, dy=20)
    s.pt(G, "G", "G", dx=14, dy=-10, highlight=True)
    write_svg("liber_primus/prop_03/0103.g6.svg", s)
    count += 1

    # 5. Tab. I Fig. 7: Elementum IV (Crossed Bowtie & Sign +)
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula I Fig. 7: Elementum IV Crossed Lines")
    A, C = (105.0, 75.0), (355.0, 75.0)
    E, F = (105.0, 290.0), (355.0, 290.0)
    D = intersect_lines(A, F, E, C)
    B = lerp(A, C, 0.5)
    G = lerp(E, F, 0.5)
    s.poly([A, C, D], "ACD", fill="var(--geom-accent-fill, rgba(180,120,40,0.08))")
    s.poly([E, F, D], "EFD", fill="var(--geom-accent-fill, rgba(180,120,40,0.08))")
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, F, "EF", width=2.2)
    s.seg(A, F, "AF", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.weight_badge((65, 75), "I", "I")
    s.weight_badge((395, 75), "H", "H")
    s.weight_badge((65, 290), "K", "K")
    s.weight_badge((395, 290), "L", "L")
    s.pt(A, "A", "A", dx=-12, dy=-12)
    s.pt(B, "B", "B", dx=0, dy=-14)
    s.pt(C, "C", "C", dx=12, dy=-12)
    s.pt(E, "E", "E", dx=-12, dy=18)
    s.pt(G, "G", "G", dx=0, dy=20)
    s.pt(F, "F", "F", dx=12, dy=18)
    s.pt(D, "D", "D", dx=16, dy=4, highlight=True)
    write_svg("liber_primus/prop_04/0103.g7.svg", s)
    count += 1

    # 6. Tab. I Fig. 8: Elementum V (Quadrilateral / Skew Corollarium)
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula I Fig. 8: Elementum V Quadrilateral")
    A, C, I_pt, H = (115.0, 88.0), (355.0, 68.0), (345.0, 286.0), (110.0, 295.0)
    B = lerp(A, C, 0.46)
    G = lerp(H, I_pt, 0.48)
    E = lerp(A, H, 0.50)
    D = lerp(C, I_pt, 0.52)
    F = intersect_lines(B, G, E, D)
    s.poly([A, C, I_pt, H], "ACIH", fill="var(--geom-accent-fill, rgba(180,120,40,0.07))")
    s.seg(A, C, "AC", width=2.3)
    s.seg(C, I_pt, "CI", width=2.3)
    s.seg(I_pt, H, "IH", width=2.3)
    s.seg(H, A, "HA", width=2.3)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.seg(E, D, "ED", stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.weight_badge((115, 48), "M", "M")
    s.weight_badge((392, 68), "L", "L")
    s.weight_badge((388, 286), "K", "K")
    s.weight_badge((110, 332), "N", "N")
    s.pt(A, "A", "A", dx=-16, dy=4)
    s.pt(B, "B", "B", dx=6, dy=-14)
    s.pt(C, "C", "C", dx=10, dy=-12)
    s.pt(D, "D", "D", dx=16, dy=4)
    s.pt(I_pt, "I", "I", dx=12, dy=16)
    s.pt(G, "G", "G", dx=4, dy=20)
    s.pt(H, "H", "H", dx=-16, dy=6)
    s.pt(E, "E", "E", dx=-16, dy=4)
    s.pt(F, "F", "F", dx=14, dy=-10, highlight=True)
    write_svg("liber_primus/prop_05/0103.g8.svg", s)
    count += 1

    # 7. Tab. I Fig. 10: Caravaggio Parallel-Line Proof
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula I Fig. 10: Caravaggio Jr. Geometric Proof")
    A, E, C = (210.0, 56.0), (88.0, 305.0), (382.0, 305.0)
    D = lerp(A, E, 0.54)
    B = lerp(A, C, 0.60)
    F = intersect_lines(E, B, C, D)
    G = (F[0] - (305.0 - F[1]) * (210.0 - 88.0) / (305.0 - 56.0) - 22.0, F[1])
    G = intersect_lines(A, E, (0.0, F[1]), (500.0, F[1]))
    H = intersect_lines(A, C, (0.0, F[1]), (500.0, F[1]))
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(E, B, "EB", stroke="var(--geom-secondary, #475569)", width=1.9)
    s.seg(C, D, "CD", stroke="var(--geom-secondary, #475569)", width=1.9)
    s.seg(G, H, "GH", stroke="var(--geom-highlight, #d97706)", width=2.4, dash="6 4")
    s.pt(A, "A", "A", dx=0, dy=-14)
    s.pt(E, "E", "E", dx=-16, dy=6)
    s.pt(C, "C", "C", dx=16, dy=6)
    s.pt(D, "D", "D", dx=-16, dy=-6)
    s.pt(B, "B", "B", dx=16, dy=-6)
    s.pt(G, "G", "G", dx=-16, dy=4)
    s.pt(H, "H", "H", dx=16, dy=4)
    s.pt(F, "F", "F", dx=0, dy=20, highlight=True)
    write_svg("liber_primus/prop_06/0103.g10.svg", s)
    count += 1

    # 8. Tab. II Fig. 24: Prop XXI Cevian Segment Ratio KL : LA
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula II Fig. 24: Proposition XXI Cevian Ratio")
    A, E, C = (165.0, 52.0), (88.0, 292.0), (376.0, 310.0)
    D = lerp(A, E, 0.72)
    B = lerp(A, C, 0.68)
    F = intersect_lines(E, B, C, D)
    K = intersect_lines(A, F, E, C)
    L = intersect_lines(A, K, D, B)
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.seg(A, E, "AE", width=2.2)
    s.seg(A, C, "AC", width=2.2)
    s.seg(E, C, "EC", width=2.2)
    s.seg(E, B, "EB", width=1.7)
    s.seg(C, D, "CD", width=1.7)
    s.seg(A, K, "AK", stroke="var(--geom-highlight, #d97706)", width=2.3)
    s.seg(D, B, "DB", stroke="var(--geom-highlight, #d97706)", width=2.2, dash="5 3")
    s.pt(A, "A", "A", dx=0, dy=-14)
    s.pt(E, "E", "E", dx=-16, dy=6)
    s.pt(C, "C", "C", dx=16, dy=6)
    s.pt(D, "D", "D", dx=-16, dy=-2)
    s.pt(B, "B", "B", dx=16, dy=-4)
    s.pt(K, "K", "K", dx=0, dy=20)
    s.pt(L, "L", "L", dx=14, dy=-8, highlight=True)
    s.pt(F, "F", "F", dx=14, dy=14, highlight=True)
    write_svg("liber_primus/prop_21/0105.g24.svg", s)
    count += 1

    # 9. Tab. III Fig. 28: Prop XXIII 3D Tetrahedron 7-Line Concurrency
    s = CalibratedSVG(480, 400, "Ceva 1678 Tabula III Fig. 28: Tetrahedron 7-Line Static Concurrency")
    E = (240.0, 52.0)
    A = (66.0, 346.0)
    C = (416.0, 336.0)
    G = (242.0, 210.0)
    # Weights R=2 at A, S=3 at E, T=5 at C, Q=4 at G
    def wavg(pairs: Sequence[tuple[Point2F, float]]) -> Point2F:
        tot = sum(w for _, w in pairs)
        return (sum(p[0] * w for p, w in pairs) / tot, sum(p[1] * w for p, w in pairs) / tot)
    wA, wE, wC, wG = 2.0, 3.0, 5.0, 4.0
    P = wavg([(A, wA), (E, wE)])
    D = wavg([(E, wE), (C, wC)])
    B = wavg([(A, wA), (C, wC)])
    N = wavg([(A, wA), (G, wG)])
    L = wavg([(C, wC), (G, wG)])
    I_pt = wavg([(E, wE), (G, wG)])
    H = wavg([(A, wA), (E, wE), (G, wG)])
    K = wavg([(E, wE), (C, wC), (G, wG)])
    M = wavg([(A, wA), (C, wC), (G, wG)])
    F = wavg([(A, wA), (E, wE), (C, wC)])
    O_pt = wavg([(A, wA), (E, wE), (C, wC), (G, wG)])
    s.poly([A, E, C], "AEC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    for p1, p2, ref in [(A, E, "AE"), (E, C, "EC"), (A, C, "AC")]:
        s.seg(p1, p2, ref, width=2.4)
    for p1, p2, ref in [(A, G, "AG"), (E, G, "EG"), (C, G, "CG")]:
        s.seg(p1, p2, ref, width=1.6, dash="5 3")
    # 4 vertex-to-face cevians + 3 bimedians concurring at O
    for p1, p2, ref in [(A, K, "AK"), (E, M, "EM"), (C, H, "CH"), (G, F, "GF")]:
        s.seg(p1, p2, ref, stroke="var(--geom-highlight, #d97706)", width=2.0)
    for p1, p2, ref in [(P, L, "PL"), (D, N, "DN"), (B, I_pt, "BI")]:
        s.seg(p1, p2, ref, stroke="var(--geom-secondary, #0284c7)", width=1.7, dash="4 2")
    for pt_v, ref, lbl, dx, dy in [
        (E, "E", "E (S)", 0, -14),
        (A, "A", "A (R)", -16, 16),
        (C, "C", "C (T)", 18, 16),
        (G, "G", "G (Q)", -20, -6),
        (P, "P", "P", -14, -4),
        (D, "D", "D", 14, -4),
        (B, "B", "B", 0, 18),
        (H, "H", "H", -14, 0),
        (K, "K", "K", 14, 0),
        (M, "M", "M", 0, 18),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    s.pt(O_pt, "O", "O", dx=14, dy=12, r=5.0, highlight=True)
    write_svg("liber_primus/prop_23/0107.g28.svg", s)
    count += 1

    # 10. Tab. IV Fig. 35: Liber II Lemma I Oblique Cylinder Projection
    s = CalibratedSVG(480, 360, "Ceva 1678 Tabula IV Fig. 35: Oblique Cylinder Ellipse Projection")
    # Base circle projected as ellipse centered at (240, 285), upper oblique ellipse centered at (240, 170)
    s.ellipse((240, 285), 115, 34, "HIK", width=2.1)
    s.ellipse((240, 165), 115, 42, "ABC", rot=22.0, stroke="var(--geom-highlight, #d97706)", width=2.3)
    s.seg((125, 285), (125, 118), "EH", width=2.0)
    s.seg((355, 285), (355, 208), "CK", width=2.0)
    s.seg((125, 118), (355, 208), "EC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg((125, 285), (355, 285), "HK", dash="4 3", width=1.5)
    s.seg((240, 285), (240, 165), "IL", dash="4 3", width=1.5)
    for pt_v, ref, lbl, dx, dy in [
        ((125, 118), "E", "E", -14, -4),
        ((355, 208), "C", "C", 14, 4),
        ((125, 285), "H", "H", -14, 14),
        ((240, 285), "I", "I", 0, 22),
        ((355, 285), "K", "K", 14, 14),
        ((180, 138), "A", "A", -10, -14),
        ((240, 165), "B", "B", 12, -12),
        ((290, 185), "D", "D", 14, -12),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    write_svg("liber_secundus/lemmata_conica/0109.g35.svg", s)
    count += 1

    # 11. Tab. IV Fig. 38: Liber II Prop. I Inscribed Ellipse & Converse of Ceva
    s = CalibratedSVG(460, 380, "Ceva 1678 Tabula IV Fig. 38: Inscribed Conic Concurrency and Converse of Ceva")
    G, A, C = (224.0, 48.0), (62.0, 322.0), (402.0, 298.0)
    # Steiner inellipse of triangle touches midpoints; use projective weights (1, 1.3, 1.1)
    # Tangent points on sides of triangle from affine map of circle inscribed in equilateral triangle
    # Barycentric map from equilateral triangle (inradius 0.5) to (G, A, C)
    def tri_map(x: float, y: float) -> Point2F:
        # Barycentrics of (x,y) wrt e1,e2,e3
        l1 = (2 * y + 1) / 3.0
        l2 = (1 - y - math.sqrt(3) * x) / 3.0
        l3 = (1 - y + math.sqrt(3) * x) / 3.0
        return (l1 * G[0] + l2 * A[0] + l3 * C[0], l1 * G[1] + l2 * A[1] + l3 * C[1])
    pts_el = [tri_map(0.5 * math.cos(2 * math.pi * i / 72), 0.5 * math.sin(2 * math.pi * i / 72)) for i in range(73)]
    d_el = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_el) + " Z"
    F = tri_map(-math.sqrt(3)/4, 0.25)  # midpoint of GA
    D = tri_map(math.sqrt(3)/4, 0.25)   # midpoint of GC
    B = tri_map(0.0, -0.5)              # midpoint of AC
    E = tri_map(0.0, 0.0)
    s.poly([G, A, C], "GAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.path(d_el, "conic", stroke="var(--geom-secondary, #0284c7)", width=2.2)
    s.seg(G, A, "GA", width=2.3)
    s.seg(G, C, "GC", width=2.3)
    s.seg(A, C, "AC", width=2.3)
    s.seg(G, B, "GB", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, D, "AD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, F, "CF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.pt(G, "G", "G", dx=0, dy=-14)
    s.pt(A, "A", "A", dx=-14, dy=14)
    s.pt(C, "C", "C", dx=14, dy=10)
    s.pt(F, "F", "F", dx=-16, dy=-4)
    s.pt(D, "D", "D", dx=16, dy=-4)
    s.pt(B, "B", "B", dx=4, dy=20)
    s.pt(E, "E", "E", dx=14, dy=14, highlight=True)
    write_svg("liber_secundus/prop_01/0109.g38.svg", s)
    count += 1

    # 12. Tab. V Fig. 41: Liber II Prop. V Nested Ceva Triangles
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula V Fig. 41: Iterated Nested Ceva Triangles")
    D, A, G = (210.0, 50.0), (80.0, 308.0), (390.0, 308.0)
    B = lerp(D, A, 0.45)
    E = lerp(D, G, 0.42)
    C = lerp(D, A, 0.62)
    F = lerp(D, G, 0.58)
    H = lerp(A, G, 0.44)
    I_pt = intersect_lines(D, H, B, G)
    K = intersect_lines(E, A, B, G)
    L = intersect_lines(D, H, C, G)
    s.poly([D, A, G], "DAG", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.seg(D, A, "DA", width=2.3)
    s.seg(D, G, "DG", width=2.3)
    s.seg(A, G, "AG", width=2.3)
    s.seg(D, H, "DH", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(B, G, "BG", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(A, E, "AE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(C, G, "CG", stroke="var(--geom-secondary, #0284c7)", width=1.6, dash="5 3")
    s.seg(A, F, "AF", stroke="var(--geom-secondary, #0284c7)", width=1.6, dash="5 3")
    for pt_v, ref, lbl, dx, dy in [
        (D, "D", "D", 0, -14),
        (A, "A", "A", -16, 6),
        (G, "G", "G", 16, 6),
        (B, "B", "B", -16, -2),
        (E, "E", "E", 16, -2),
        (C, "C", "C", -16, 6),
        (F, "F", "F", 16, 6),
        (H, "H", "H", 0, 20),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    s.pt(K, "K", "K", dx=12, dy=-10, highlight=True)
    s.pt(I_pt, "I", "I", dx=14, dy=14, highlight=True)
    write_svg("liber_secundus/prop_05/0111.g41.svg", s)
    count += 1

    # 13. Tab. V Fig. 44: Liber II Prop. IX Inscribing Ellipse Given Two Contact Points
    s = CalibratedSVG(480, 380, "Ceva 1678 Tabula V Fig. 44: Inscribing an Ellipse Given Two Contact Points")
    B, A, C = (252.0, 46.0), (88.0, 326.0), (418.0, 326.0)
    def tri_map_b(x: float, y: float) -> Point2F:
        l1 = (2 * y + 1) / 3.0
        l2 = (1 - y - math.sqrt(3) * x) / 3.0
        l3 = (1 - y + math.sqrt(3) * x) / 3.0
        return (l1 * B[0] + l2 * A[0] + l3 * C[0], l1 * B[1] + l2 * A[1] + l3 * C[1])
    pts_e = [tri_map_b(0.5 * math.cos(2 * math.pi * i / 72), 0.5 * math.sin(2 * math.pi * i / 72)) for i in range(73)]
    d_e = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_e) + " Z"
    F = tri_map_b(-math.sqrt(3)/4, 0.25)
    E = tri_map_b(math.sqrt(3)/4, 0.25)
    D = tri_map_b(0.0, -0.5)
    G = tri_map_b(0.0, 0.0)
    O_pt = (52.0, 204.0)
    s.poly([B, A, C], "BAC", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    s.path(d_e, "ellipse", stroke="var(--geom-secondary, #0284c7)", width=2.2)
    s.seg(B, A, "BA", width=2.3)
    s.seg(B, C, "BC", width=2.3)
    s.seg(A, C, "AC", width=2.3)
    s.seg(B, D, "BD", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, E, "AE", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(C, F, "CF", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(O_pt, F, "OF", dash="4 3", width=1.5)
    s.seg(O_pt, D, "OD", dash="4 3", width=1.5)
    for pt_v, ref, lbl, dx, dy in [
        (B, "B", "B", 0, -14),
        (A, "A", "A", -14, 14),
        (C, "C", "C", 14, 14),
        (F, "F", "F", -16, -6),
        (E, "E", "E", 16, -6),
        (D, "D", "D", 0, 20),
        (O_pt, "O", "O", -14, 0),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    s.pt(G, "G", "G", dx=14, dy=-10, highlight=True)
    write_svg("liber_secundus/prop_09/0111.g44.svg", s)
    count += 1

    # 14. Tab. VI Fig. 50: Liber II Props. X-XII Three Tangents to a Parabola
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula VI Fig. 50: Three Tangents to a Parabola")
    # Parabola y = 0.008 * (x - 160)^2 + 90 -> rotated/tilted clean arc with tangents at F, E, D
    def para(t: float) -> Point2F:
        return (110.0 + 180.0 * t, 285.0 - 210.0 * t + 140.0 * t * t)
    def para_tan(t: float) -> Point2F:
        return (180.0, -210.0 + 280.0 * t)
    def tan_pt(t: float, s_val: float) -> Point2F:
        p, v = para(t), para_tan(t)
        return (p[0] + s_val * v[0], p[1] + s_val * v[1])
    tF, tE, tD = 0.12, 0.58, 1.05
    F_pt, E_pt, D_pt = para(tF), para(tE), para(tD)
    A = intersect_lines(F_pt, tan_pt(tF, 1.0), E_pt, tan_pt(tE, 1.0))
    B = intersect_lines(F_pt, tan_pt(tF, 1.0), D_pt, tan_pt(tD, 1.0))
    C = intersect_lines(E_pt, tan_pt(tE, 1.0), D_pt, tan_pt(tD, 1.0))
    H = intersect_lines(A, D_pt, C, F_pt)
    pts_p = [para(i / 40.0) for i in range(-2, 48)]
    d_p = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_p)
    s.path(d_p, "parabola", stroke="var(--geom-secondary, #0284c7)", width=2.4)
    s.seg(F_pt, B, "FB", width=2.1)
    s.seg(B, D_pt, "BD", width=2.1)
    s.seg(A, C, "AC", width=2.1)
    s.seg(A, D_pt, "AD", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(C, F_pt, "CF", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, E_pt, "BE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    for pt_v, ref, lbl, dx, dy in [
        (A, "A", "A", -14, -8),
        (B, "B", "B", 0, -14),
        (C, "C", "C", 14, -8),
        (F_pt, "F", "F", -16, 4),
        (E_pt, "E", "E", 2, -16),
        (D_pt, "D", "D", 16, 6),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.6)
    s.pt(H, "H", "H", dx=0, dy=20, highlight=True)
    write_svg("liber_secundus/prop_10/0113.g50.svg", s)
    count += 1

    # 15. Tab. VII Fig. 57: Liber II Prop. XVI Concurrency of Angle Bisectors (Incenter)
    s = CalibratedSVG(460, 360, "Ceva 1678 Tabula VII Fig. 57: Angle Bisectors and Incenter")
    I_pt, A, E = (210.0, 54.0), (76.0, 306.0), (392.0, 306.0)
    def dist(p: Point2F, q: Point2F) -> float:
        return math.hypot(p[0] - q[0], p[1] - q[1])
    a_len = dist(A, E)
    e_len = dist(I_pt, A)
    i_len = dist(I_pt, E)
    perim = a_len + e_len + i_len
    inc = (
        (a_len * I_pt[0] + i_len * A[0] + e_len * E[0]) / perim,
        (a_len * I_pt[1] + i_len * A[1] + e_len * E[1]) / perim,
    )
    C = intersect_lines(I_pt, inc, A, E)
    G = intersect_lines(A, inc, I_pt, E)
    N = intersect_lines(E, inc, I_pt, A)
    area = 0.5 * abs((A[0] - I_pt[0]) * (E[1] - I_pt[1]) - (E[0] - I_pt[0]) * (A[1] - I_pt[1]))
    inrad = 2.0 * area / perim
    s.poly([I_pt, A, E], "IAE", fill="var(--geom-accent-fill, rgba(180,120,40,0.06))")
    s.circle(inc, inrad, "incircle", stroke="var(--geom-secondary, #0284c7)", width=1.8, dash="5 3")
    s.seg(I_pt, A, "IA", width=2.3)
    s.seg(I_pt, E, "IE", width=2.3)
    s.seg(A, E, "AE", width=2.3)
    s.seg(I_pt, C, "IC", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(A, G, "AG", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(E, N, "EN", stroke="var(--geom-highlight, #d97706)", width=2.0)
    for pt_v, ref, lbl, dx, dy in [
        (I_pt, "I", "I", 0, -14),
        (A, "A", "A", -16, 8),
        (E, "E", "E", 16, 8),
        (N, "N", "N", -16, -2),
        (G, "G", "G", 16, -2),
        (C, "C", "C", 0, 20),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.6)
    s.pt(inc, "F", "F", dx=12, dy=-12, highlight=True)
    write_svg("liber_secundus/prop_16/0115.g57.svg", s)
    count += 1

    # 16. Tab. X Fig. 85: Liber II Prop. XXI Scholium Optical Rangefinder
    s = CalibratedSVG(480, 360, "Ceva 1678 Tabula X Fig. 85: Single-Station Optical Distance Rangefinder")
    D, E = (340.0, 295.0), (110.0, 295.0)
    C, L = (340.0, 95.0), (110.0, 155.0)
    K = (110.0, 36.0)
    B = lerp(D, E, 0.28)
    M = lerp(D, K, 0.62)
    I_pt = intersect_lines(B, C, D, K)
    s.seg(D, E, "DE", width=2.6)
    s.seg(D, C, "DC", width=2.5)
    s.seg(E, L, "EL", width=2.5)
    s.seg(L, K, "LK", stroke="var(--geom-secondary, #0284c7)", width=1.8, dash="6 4")
    s.seg(B, C, "BC", stroke="var(--geom-highlight, #d97706)", width=2.0)
    s.seg(D, K, "DK", stroke="var(--geom-highlight, #d97706)", width=2.0)
    for pt_v, ref, lbl, dx, dy in [
        (D, "D", "D (Eye)", 18, 16),
        (E, "E", "E", -14, 16),
        (B, "B", "B", 0, 20),
        (C, "C", "C", 16, 0),
        (L, "L", "L", -16, 0),
        (M, "M", "M", 16, -4),
        (K, "K", "K (Target)", 18, 6),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.6)
    s.pt(I_pt, "I", "I", dx=-16, dy=-6, highlight=True)
    write_svg("liber_secundus/prop_21/0121.g85.svg", s)
    count += 1

    # 17. Tab. VIII Fig. 71: Appendix Prop. IV Hippocrates' Lune
    s = CalibratedSVG(440, 360, "Ceva 1678 Tabula VIII Fig. 71: Hippocrates Lune on Isosceles Right Triangle")
    A, C, B = (100.0, 200.0), (340.0, 200.0), (220.0, 80.0)
    # Semicircle on AC (center (220,200), r=120) and quadrant arc of radius 120*sqrt(2) centered at B passing through A,C
    r_semi = 120.0
    r_quad = r_semi * math.sqrt(2.0)
    # Lune D between lower semicircle ADC and lower quadrant arc from A to C centered at B
    d_lune = (
        f"M {A[0]:.2f} {A[1]:.2f} A {r_quad:.2f} {r_quad:.2f} 0 0 0 {C[0]:.2f} {C[1]:.2f} "
        f"A {r_semi:.2f} {r_semi:.2f} 0 0 1 {A[0]:.2f} {A[1]:.2f} Z"
    )
    s.path(d_lune, "D", fill="var(--geom-accent-fill, rgba(217,119,6,0.22))", stroke="none", layer="graphics")
    s.poly([A, B, C], "ABC", fill="var(--geom-secondary-fill, rgba(2,132,199,0.14))")
    s.circle((220.0, 200.0), r_semi, "circle_AC", width=2.0)
    s.path(f"M {A[0]:.2f} {A[1]:.2f} A {r_quad:.2f} {r_quad:.2f} 0 0 0 {C[0]:.2f} {C[1]:.2f}", "arc_ADC", stroke="var(--geom-highlight, #d97706)", width=2.3)
    s.seg(A, B, "AB", width=2.3)
    s.seg(B, C, "BC", width=2.3)
    s.seg(A, C, "AC", width=2.3)
    s.pt(A, "A", "A", dx=-16, dy=4)
    s.pt(C, "C", "C", dx=16, dy=4)
    s.pt(B, "B", "B", dx=0, dy=-14)
    s.text((220.0, 286.0), "Lune D = △ABC", "D_lbl", highlight=True, size=16)
    write_svg("appendix_geometrica/prop_04/0117.g71.svg", s)
    count += 1

    # 18. Tab. IX Fig. 74: Appendix Prop. VII Cylindrical Hoof / Ungula (2/3 of Prism)
    s = CalibratedSVG(460, 400, "Ceva 1678 Tabula IX Fig. 74: Cylindrical Ungula Two-Thirds of Circumscribed Prism")
    B, E, A = (230.0, 40.0), (230.0, 165.0), (230.0, 290.0)
    K, L = (82.0, 128.0), (378.0, 128.0)
    C, D = (82.0, 252.0), (378.0, 252.0)
    Q, P = (82.0, 366.0), (378.0, 366.0)
    F = lerp(B, E, 0.48)
    s.poly([B, K, Q, P, L], "prism_QBP", fill="var(--geom-accent-fill, rgba(180,120,40,0.05))")
    # Two semi-elliptical hooves BCA and BDA
    s.path("M 230 40 C 135 110, 78 190, 82 252 C 86 335, 160 330, 230 290", "BCA", stroke="var(--geom-highlight, #d97706)", width=2.4)
    s.path("M 230 40 C 325 110, 382 190, 378 252 C 374 335, 300 330, 230 290", "BDA", stroke="var(--geom-highlight, #d97706)", width=2.4)
    for p1, p2, ref in [
        (B, K, "BK"), (B, L, "BL"), (K, Q, "KQ"), (L, P, "LP"), (Q, P, "QP"),
        (A, Q, "AQ"), (A, P, "AP"), (B, A, "BA"), (C, E, "CE"), (E, D, "ED"),
        (K, E, "KE"), (E, L, "EL"),
    ]:
        s.seg(p1, p2, ref, width=1.9)
    s.seg(F, (82.0, 195.0), "FI", stroke="var(--geom-secondary, #0284c7)", width=1.6, dash="4 3")
    s.seg(F, (378.0, 195.0), "FM", stroke="var(--geom-secondary, #0284c7)", width=1.6, dash="4 3")
    for pt_v, ref, lbl, dx, dy in [
        (B, "B", "B", 0, -14), (E, "E", "E", 14, 14), (A, "A", "A", 0, -14),
        (K, "K", "K", -14, -4), (L, "L", "L", 14, -4), (C, "C", "C", -16, 4),
        (D, "D", "D", 16, 4), (Q, "Q", "Q", -14, 14), (P, "P", "P", 14, 14),
        (F, "F", "F", 12, -4),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    write_svg("appendix_geometrica/prop_07/0119.g74.svg", s)
    count += 1

    # 19. Tab. X Fig. 80: Appendix Prop. XIII Hemisphere 5:3 Center of Gravity
    s = CalibratedSVG(440, 360, "Ceva 1678 Tabula X Fig. 80: Center of Gravity of Hemisphere (BO : OF = 5 : 3)")
    F = (220.0, 90.0)
    B = (220.0, 250.0)
    R = 160.0
    A_pt, C_pt = (60.0, 90.0), (380.0, 90.0)
    E_pt, D_pt = (60.0, 250.0), (380.0, 250.0)
    O_pt = lerp(B, F, 5.0 / 8.0)
    L = lerp(B, F, 0.5)
    P = lerp(B, F, 0.25)
    s.poly([E_pt, D_pt, F], "cone_EFD", fill="var(--geom-accent-fill, rgba(217,119,6,0.12))")
    s.path(f"M {A_pt[0]:.2f} {A_pt[1]:.2f} A {R:.2f} {R:.2f} 0 0 0 {C_pt[0]:.2f} {C_pt[1]:.2f}", "hemi_ABC", stroke="var(--geom-secondary, #0284c7)", width=2.4)
    s.seg(A_pt, C_pt, "AC", width=2.2)
    s.seg(E_pt, D_pt, "ED", width=2.2)
    s.seg(A_pt, E_pt, "AE", width=2.0)
    s.seg(C_pt, D_pt, "CD", width=2.0)
    s.seg(F, E_pt, "FE", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, D_pt, "FD", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(F, B, "FB", width=2.2)
    s.seg((60.0, 170.0), (380.0, 170.0), "HG", dash="5 3", width=1.5)
    for pt_v, ref, lbl, dx, dy in [
        (A_pt, "A", "A", -14, -6), (C_pt, "C", "C", 14, -6),
        (E_pt, "E", "E", -14, 14), (D_pt, "D", "D", 14, 14),
        (F, "F", "F", 0, -14), (B, "B", "B", 0, 22),
        (L, "L", "L (1/2)", 34, 4), (P, "P", "P (1/4)", 34, 4),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    s.pt(O_pt, "O", "O (5:3)", dx=-42, dy=4, highlight=True)
    write_svg("appendix_geometrica/prop_13/0121.g80.svg", s)
    count += 1

    # 20. Tab. X Fig. 81: Appendix Prop. XIV Parabolic Conoid 2:1 Center of Gravity
    s = CalibratedSVG(460, 320, "Ceva 1678 Tabula X Fig. 81: Center of Gravity of Parabolic Conoid (BE : ED = 2 : 1)")
    B = (390.0, 160.0)
    D = (90.0, 160.0)
    C = (90.0, 62.0)
    A = (90.0, 258.0)
    E = lerp(B, D, 2.0 / 3.0)
    H = lerp(B, D, 0.55)
    # Parabola x = 390 - 300 * ((y - 160)/98)^2
    pts_par = [(390.0 - 300.0 * ((y - 160.0) / 98.0) ** 2, y) for y in [62.0 + i * 196.0 / 60.0 for i in range(61)]]
    d_par = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_par)
    s.poly([B, C, A], "tri_ABC", fill="var(--geom-accent-fill, rgba(217,119,6,0.12))")
    s.path(d_par, "paraboloid_ABC", stroke="var(--geom-secondary, #0284c7)", width=2.4)
    s.seg(C, A, "CA", width=2.3)
    s.seg(B, C, "BC", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, A, "BA", stroke="var(--geom-highlight, #d97706)", width=1.9)
    s.seg(B, D, "BD", width=2.1)
    y_slice = 98.0 * math.sqrt((390.0 - H[0]) / 300.0)
    s.seg((H[0], 160.0 - y_slice), (H[0], 160.0 + y_slice), "KF", dash="5 3", width=1.6)
    for pt_v, ref, lbl, dx, dy in [
        (B, "B", "B", 16, 4), (D, "D", "D", -16, 4),
        (C, "C", "C", -16, -6), (A, "A", "A", -16, 12),
        (H, "H", "H", 12, 16),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    s.pt(E, "E", "E (2:1)", dx=0, dy=-16, highlight=True)
    write_svg("appendix_geometrica/prop_14/0121.g81.svg", s)
    count += 1

    # 21. Tab. X Fig. 82: Appendix Prop. XV Infinitely Extended Hyperbolic Solid (Torricelli Trumpet)
    s = CalibratedSVG(460, 340, "Ceva 1678 Tabula X Fig. 82: Finite Volume of Infinitely Extended Hyperbolic Solid")
    cx, cy = 230.0, 170.0
    # 4 symmetric hyperbolic branches |x - cx| * |y - cy| = k (k = 1200)
    k = 1200.0
    for sx, sy, ref in [(1, -1, "hyp_NE"), (-1, -1, "hyp_NW"), (-1, 1, "hyp_SW"), (1, 1, "hyp_SE")]:
        pts_h = []
        for i in range(40):
            dx_v = 10.0 + i * 4.5
            dy_v = k / dx_v
            if dy_v <= 135.0:
                pts_h.append((cx + sx * dx_v, cy + sy * dy_v))
        d_h = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts_h)
        s.path(d_h, ref, stroke="var(--geom-secondary, #0284c7)", width=2.2)
    s.seg((40, cy), (420, cy), "EK", width=1.8, dash="6 4")
    s.seg((cx, 30), (cx, 310), "FC", width=1.8, dash="6 4")
    # Square on conjugate semi-axis (dx = dy = sqrt(k) = 34.64)
    r_sq = math.sqrt(k)
    s.poly(
        [(cx - r_sq, cy - r_sq), (cx + r_sq, cy - r_sq), (cx + r_sq, cy + r_sq), (cx - r_sq, cy + r_sq)],
        "MNH",
        fill="var(--geom-accent-fill, rgba(217,119,6,0.16))",
        stroke="var(--geom-highlight, #d97706)",
    )
    s.seg((cx - r_sq, cy + r_sq), (cx + r_sq, cy - r_sq), "HM", stroke="var(--geom-highlight, #d97706)", width=2.1)
    s.pt((cx, cy), "D", "D", dx=12, dy=14, highlight=True)
    s.pt((cx + r_sq, cy - r_sq), "M", "M", dx=12, dy=-8)
    s.pt((cx - r_sq, cy + r_sq), "H", "H", dx=-14, dy=14)
    s.pt((cx + r_sq, cy + r_sq), "N", "N", dx=14, dy=14)
    s.text((48, cy - 12), "E", "E")
    s.text((412, cy - 12), "K", "K")
    s.text((cx + 14, 42), "F", "F")
    s.text((cx + 14, 304), "C", "C")
    write_svg("appendix_geometrica/prop_15/0121.g82.svg", s)
    count += 1

    # 22. Tab. X Fig. 84: Appendix Closing Scholium — Sphere Indivisibles Counterexample
    s = CalibratedSVG(440, 360, "Ceva 1678 Tabula X Fig. 84: Sphere Surface Indivisibles Paradox")
    ctr = (220.0, 180.0)
    R = 128.0
    A, B = (ctr[0] - R, ctr[1]), (ctr[0] + R, ctr[1])
    C, D = (ctr[0], ctr[1] - R), (ctr[0], ctr[1] + R)
    ang = math.radians(48.0)
    E = (ctr[0] + R * math.cos(ang), ctr[1] - R * math.sin(ang))
    F = (ctr[0] + R * math.cos(ang), ctr[1] + R * math.sin(ang))
    ang2 = math.radians(32.0)
    G = (ctr[0] + R * math.cos(ang2), ctr[1] - R * math.sin(ang2))
    H = (ctr[0] + R * math.cos(ang2), ctr[1] + R * math.sin(ang2))
    I_pt = (E[0], ctr[1])
    s.circle(ctr, R, "sphere_ACBD", width=2.2)
    s.seg(A, B, "AB", width=2.1)
    s.seg(C, D, "CD", width=1.9)
    s.seg(E, F, "EF", stroke="var(--geom-highlight, #d97706)", width=2.2)
    s.seg(G, H, "GH", stroke="var(--geom-secondary, #0284c7)", width=1.8, dash="4 3")
    s.seg(A, E, "AE", stroke="var(--geom-secondary, #0284c7)", width=1.7)
    s.seg(E, B, "EB", stroke="var(--geom-highlight, #d97706)", width=2.1)
    for pt_v, ref, lbl, dx, dy in [
        (A, "A", "A", -16, 4), (B, "B", "B", 16, 4),
        (C, "C", "C", 0, -14), (D, "D", "D", 0, 20),
        (E, "E", "E", 12, -10), (F, "F", "F", 12, 16),
        (G, "G", "G", 14, -4), (H, "H", "H", 14, 12),
    ]:
        s.pt(pt_v, ref, lbl, dx=dx, dy=dy, r=3.5)
    s.pt(I_pt, "I", "I", dx=-12, dy=16, highlight=True)
    write_svg("appendix_geometrica/scholium_indivisibilia/0121.g84.svg", s)
    count += 1

    print(f"Generated {count} calibrated 5-layer .euclid-graphic SVGs in {CODEX_DIR}")
    return count


if __name__ == "__main__":
    build_all()
