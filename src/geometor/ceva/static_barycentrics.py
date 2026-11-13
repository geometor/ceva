r"""Exact static-barycentric solver and constructive proofs for Ceva's Theorem (1678).

Models Giovanni Ceva's *De lineis rectis se invicem secantibus statica constructio*
(Milan, 1678) in 100% exact symbolic algebra over :math:`\mathbb{Q}` and symbolic
rings using :mod:`sympy` and :mod:`geometor.model`:

- **Static-Mass Solver** (:func:`solve_static_barycentrics`): Assigns exact homogeneous
  weights :math:`(u : v : w)` to vertices :math:`(A, B, C)` (*Liber Primus*, *Elementa*
  I–III & *Scholium* p. 5 on negative weights :math:`F - A`), computes the three
  Archimedean lever fulcrums :math:`D \in BC`, :math:`E \in CA`, :math:`F \in AB`,
  the static center of gravity :math:`P`, signed segment ratios, signed sub-triangle
  area ratios (*Appendix Geometrica*), and verifies :math:`\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1`.
- **Canonical Rational Triangle Centers** (:data:`CANONICAL_CENTERS`,
  :func:`evaluate_canonical_centers`): Evaluates :math:`X(1), X(2), X(4), X(6), X(7), X(8)`
  and the exterior :math:`A`-excenter :math:`J_A` on the Heronian :math:`(13, 14, 15)`
  triangle :math:`A=(5, 12), B=(0, 0), C=(14, 0)` where every coordinate lies in :math:`\mathbb{Q}`.
- **Constructive ``@proposition`` Proofs**:

  - :func:`construct_ceva_concurrency`: Targeted ``geometor.model`` construction of
    interior and exterior cevian concurrency (*Liber Primus*, *Elementa* II–III & *Prop.* VI).
  - :func:`construct_isotomic_conjugate`: Midpoint-reflection construction of the
    isotomic conjugate :math:`(u^{-1} : v^{-1} : w^{-1})` pairing Ceva's contact point
    :math:`X(7)` (*Liber Secundus*, *Prop.* I) with the Nagel point :math:`X(8)`.
  - :func:`construct_cevian_menelaus_harmonic`: Dual Menelaus transversal :math:`EF \cap BC = D'`
    (*Liber Primus*, *Elementum* I & *Prop.* VIII) proving harmonic division
    :math:`(B, C; D, D') = -1`.
  - :func:`verify_spread_ceva`: Rational Trigonometry **Spread Ceva's Theorem**
    verified via exact rational spreads and quadrances with zero square roots.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    clean_expr,
    cross_ratio,
    is_harmonic,
    proposition,
    quadrance,
    vertex_spread,
    zero_test,
)
from geometor.model.invariants import signed_area2

SymScalar = int | sp.Expr

__all__ = [
    "CANONICAL_CENTERS",
    "HERONIAN_VERTICES",
    "SpreadCevaResult",
    "StaticBarycentricResult",
    "SymScalar",
    "construct_ceva_concurrency",
    "construct_cevian_menelaus_harmonic",
    "construct_isotomic_conjugate",
    "directed_ratio_collinear",
    "evaluate_canonical_centers",
    "prove_ceva_barycentric_identity",
    "solve_static_barycentrics",
    "verify_spread_ceva",
]

HERONIAN_VERTICES: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = (
    (5, 12),
    (0, 0),
    (14, 0),
)
"""Canonical Heronian (13, 14, 15) triangle A=(5,12), B=(0,0), C=(14,0) with Area = 84."""


@dataclass(frozen=True)
class StaticBarycentricResult:
    """Exact symbolic solution of Ceva's three-weight static equilibrium on triangle ABC."""

    name: str
    weights: tuple[sp.Expr, sp.Expr, sp.Expr]
    vertices: tuple[spg.Point2D, spg.Point2D, spg.Point2D]
    foot_d: spg.Point2D
    foot_e: spg.Point2D
    foot_f: spg.Point2D
    center: spg.Point2D
    ratio_af_fb: sp.Expr
    ratio_bd_dc: sp.Expr
    ratio_ce_ea: sp.Expr
    ceva_product: sp.Expr
    area_pbc: sp.Expr
    area_pca: sp.Expr
    area_pab: sp.Expr
    lever_residuals: tuple[sp.Expr, sp.Expr, sp.Expr]
    area_ratio_residuals: tuple[sp.Expr, sp.Expr, sp.Expr]
    is_interior: bool


@dataclass(frozen=True)
class SpreadCevaResult:
    """Exact Rational Trigonometry invariants for Spread Ceva's Theorem."""

    spread_bad: sp.Expr
    spread_dac: sp.Expr
    spread_cbe: sp.Expr
    spread_eba: sp.Expr
    spread_acf: sp.Expr
    spread_fcb: sp.Expr
    spread_product: sp.Expr
    quadrance_product: sp.Expr


CANONICAL_CENTERS: dict[str, tuple[str, tuple[int, int, int]]] = {
    "X(1)": ("Incenter (angle bisectors, u:v:w = a:b:c)", (14, 15, 13)),
    "X(2)": ("Centroid (medians, Lib. II Prop. III, u:v:w = 1:1:1)", (1, 1, 1)),
    "X(4)": ("Orthocenter (altitudes, u:v:w = 1/S_A : 1/S_B : 1/S_C)", (70, 99, 55)),
    "X(6)": ("Symmedian point (symmedians, u:v:w = a^2:b^2:c^2)", (196, 225, 169)),
    "X(7)": (
        "Gergonne contact point (Ceva 1678 Lib. II Prop. I, 1/(s-a):1/(s-b):1/(s-c))",
        (24, 28, 21),
    ),
    "X(8)": ("Nagel point (isotomic conjugate of X(7), s-a:s-b:s-c)", (7, 6, 8)),
    "J_A": (
        "A-Excenter (exterior negative weight Lib. I Elem. III, -a:b:c)",
        (-14, 15, 13),
    ),
}
"""Exact integer homogeneous barycentric weights on the (13, 14, 15) Heronian triangle."""


def _sympify_point2d(pt: spg.Point2D | tuple[SymScalar, SymScalar]) -> spg.Point2D:
    """Convert a point or coordinate pair into an exact SymPy ``Point2D`` without floats."""
    if isinstance(pt, spg.Point2D):
        coords = (sp.sympify(pt.x), sp.sympify(pt.y))
    else:
        coords = (sp.sympify(pt[0]), sp.sympify(pt[1]))
    for c in coords:
        if c.has(sp.Float):
            raise ValueError(f"Floating-point coordinate forbidden in geometor.ceva: {c!r}")
    return spg.Point2D(clean_expr(coords[0]), clean_expr(coords[1]), evaluate=False)


def directed_ratio_collinear(
    p_start: spg.Point2D,
    p_div: spg.Point2D,
    p_end: spg.Point2D,
) -> sp.Expr:
    """Compute the exact directed segment ratio ``(p_start -> p_div) / (p_div -> p_end)``.

    Projects collinear displacements onto ``p_end - p_start`` so no square roots are
    introduced. Positive when ``p_div`` lies strictly between ``p_start`` and ``p_end``,
    and negative when ``p_div`` divides ``p_start p_end`` externally.

    Args:
        p_start: First endpoint of the directed base segment.
        p_div: Collinear division point (lever fulcrum).
        p_end: Second endpoint of the directed base segment.

    Returns:
        Exact simplified SymPy expression for the signed ratio.

    Raises:
        ValueError: If the three points are not collinear or ``p_div == p_end``.
    """
    dx = clean_expr(p_end.x - p_start.x)
    dy = clean_expr(p_end.y - p_start.y)
    if zero_test(dx) and zero_test(dy):
        raise ValueError("Base segment endpoints coincide in directed_ratio_collinear.")

    col_det = clean_expr(dx * (p_div.y - p_start.y) - dy * (p_div.x - p_start.x))
    if not zero_test(col_det):
        raise ValueError(f"Point {p_div} is not collinear with {p_start} and {p_end}.")

    num = clean_expr((p_div.x - p_start.x) * dx + (p_div.y - p_start.y) * dy)
    den = clean_expr((p_end.x - p_div.x) * dx + (p_end.y - p_div.y) * dy)
    if zero_test(den):
        raise ValueError("Division point coincides with second endpoint (infinite ratio).")
    return clean_expr(sp.simplify(num / den))


def solve_static_barycentrics(
    u: SymScalar,
    v: SymScalar,
    w: SymScalar,
    vertices: tuple[tuple[SymScalar, SymScalar] | spg.Point2D, ...] = HERONIAN_VERTICES,
    *,
    name: str = "P",
) -> StaticBarycentricResult:
    r"""Solve Ceva's static equilibrium for homogeneous vertex weights ``(u, v, w)``.

    Places weights ``u`` at ``A``, ``v`` at ``B``, and ``w`` at ``C``. By Archimedes'
    Law of the Lever (*Liber Primus*, *Lemma* I):

    - :math:`D = \frac{v B + w C}{v + w}` balances :math:`B` and :math:`C` with
      :math:`v \cdot \overline{BD} = w \cdot \overline{DC}`,
    - :math:`E = \frac{w C + u A}{w + u}` balances :math:`C` and :math:`A` with
      :math:`w \cdot \overline{CE} = u \cdot \overline{EA}`,
    - :math:`F = \frac{u A + v B}{u + v}` balances :math:`A` and :math:`B` with
      :math:`u \cdot \overline{AF} = v \cdot \overline{FB}`,

    and all three cevians :math:`AD, BE, CF` concur at the static center of gravity
    :math:`P = \frac{u A + v B + w C}{u + v + w}`.

    Args:
        u: Exact weight at vertex ``A`` (integer, rational, or SymPy expression).
        v: Exact weight at vertex ``B``.
        w: Exact weight at vertex ``C``.
        vertices: Three non-collinear vertices ``(A, B, C)``.
        name: Label for the concurrency center.

    Returns:
        Populated :class:`StaticBarycentricResult` with verified lever and area invariants.

    Raises:
        ValueError: If any pairwise or total weight sum vanishes (parallel cevian / point at infinity)
            or if ``vertices`` are collinear or contain ``Float`` values.
    """
    u_ex, v_ex, w_ex = (clean_expr(sp.sympify(val)) for val in (u, v, w))
    for val in (u_ex, v_ex, w_ex):
        if val.has(sp.Float):
            raise ValueError(f"Floating-point weight forbidden: {val!r}")
        if zero_test(val):
            raise ValueError("All three vertex weights must be non-zero for proper cevians.")

    if len(vertices) != 3:
        raise ValueError("vertices must contain exactly three points (A, B, C).")
    a_pt, b_pt, c_pt = (_sympify_point2d(pt) for pt in vertices)
    if zero_test(signed_area2(a_pt, b_pt, c_pt)):
        raise ValueError("Triangle vertices A, B, C are collinear.")

    vw = clean_expr(v_ex + w_ex)
    wu = clean_expr(w_ex + u_ex)
    uv = clean_expr(u_ex + v_ex)
    total = clean_expr(u_ex + v_ex + w_ex)
    for denom, label in ((vw, "v + w"), (wu, "w + u"), (uv, "u + v"), (total, "u + v + w")):
        if zero_test(denom):
            raise ValueError(f"Degenerate weight sum ({label} == 0) places fulcrum at infinity.")

    d_pt = spg.Point2D(
        clean_expr(sp.simplify((v_ex * b_pt.x + w_ex * c_pt.x) / vw)),
        clean_expr(sp.simplify((v_ex * b_pt.y + w_ex * c_pt.y) / vw)),
        evaluate=False,
    )
    e_pt = spg.Point2D(
        clean_expr(sp.simplify((w_ex * c_pt.x + u_ex * a_pt.x) / wu)),
        clean_expr(sp.simplify((w_ex * c_pt.y + u_ex * a_pt.y) / wu)),
        evaluate=False,
    )
    f_pt = spg.Point2D(
        clean_expr(sp.simplify((u_ex * a_pt.x + v_ex * b_pt.x) / uv)),
        clean_expr(sp.simplify((u_ex * a_pt.y + v_ex * b_pt.y) / uv)),
        evaluate=False,
    )
    p_pt = spg.Point2D(
        clean_expr(sp.simplify((u_ex * a_pt.x + v_ex * b_pt.x + w_ex * c_pt.x) / total)),
        clean_expr(sp.simplify((u_ex * a_pt.y + v_ex * b_pt.y + w_ex * c_pt.y) / total)),
        evaluate=False,
    )

    r_af_fb = directed_ratio_collinear(a_pt, f_pt, b_pt)
    r_bd_dc = directed_ratio_collinear(b_pt, d_pt, c_pt)
    r_ce_ea = directed_ratio_collinear(c_pt, e_pt, a_pt)
    product = clean_expr(sp.simplify(r_af_fb * r_bd_dc * r_ce_ea))

    area_pbc = clean_expr(sp.simplify(signed_area2(p_pt, b_pt, c_pt) / 2))
    area_pca = clean_expr(sp.simplify(signed_area2(p_pt, c_pt, a_pt) / 2))
    area_pab = clean_expr(sp.simplify(signed_area2(p_pt, a_pt, b_pt) / 2))

    # Archimedean lever balance residuals: m_A * AF - m_B * FB == 0, etc.
    lev_ab = clean_expr(sp.simplify(r_af_fb - v_ex / u_ex))
    lev_bc = clean_expr(sp.simplify(r_bd_dc - w_ex / v_ex))
    lev_ca = clean_expr(sp.simplify(r_ce_ea - u_ex / w_ex))

    # Pure synthetic area-ratio equivalence (Appendix Geometrica): [PAB]/[PCA] == BD/DC
    area_res_bc = clean_expr(sp.simplify(area_pab / area_pca - r_bd_dc))
    area_res_ca = clean_expr(sp.simplify(area_pbc / area_pab - r_ce_ea))
    area_res_ab = clean_expr(sp.simplify(area_pca / area_pbc - r_af_fb))

    is_interior = all(val.is_positive is True for val in (r_af_fb, r_bd_dc, r_ce_ea))

    return StaticBarycentricResult(
        name=name,
        weights=(u_ex, v_ex, w_ex),
        vertices=(a_pt, b_pt, c_pt),
        foot_d=d_pt,
        foot_e=e_pt,
        foot_f=f_pt,
        center=p_pt,
        ratio_af_fb=r_af_fb,
        ratio_bd_dc=r_bd_dc,
        ratio_ce_ea=r_ce_ea,
        ceva_product=product,
        area_pbc=area_pbc,
        area_pca=area_pca,
        area_pab=area_pab,
        lever_residuals=(lev_ab, lev_bc, lev_ca),
        area_ratio_residuals=(area_res_bc, area_res_ca, area_res_ab),
        is_interior=is_interior,
    )


def evaluate_canonical_centers() -> dict[str, StaticBarycentricResult]:
    r"""Evaluate all canonical centers in :data:`CANONICAL_CENTERS` over :math:`\mathbb{Q}`.

    Returns:
        Mapping from center key (``X(1)``, ``X(2)``, ``X(4)``, ``X(6)``, ``X(7)``,
        ``X(8)``, ``J_A``) to its exact :class:`StaticBarycentricResult`.
    """
    results: dict[str, StaticBarycentricResult] = {}
    for code, (_desc, (u_val, v_val, w_val)) in CANONICAL_CENTERS.items():
        results[code] = solve_static_barycentrics(
            u_val,
            v_val,
            w_val,
            HERONIAN_VERTICES,
            name=code,
        )
    return results


def prove_ceva_barycentric_identity() -> dict[str, sp.Expr]:
    r"""Prove Ceva's Theorem and sub-triangle area proportions universally over symbolic coordinates.

    Uses indeterminate vertex coordinates :math:`A=(x_A, y_A), B=(x_B, y_B), C=(x_C, y_C)`
    and symbolic weights :math:`(u, v, w)` to verify that:

    1. :math:`P = \frac{u A + v B + w C}{u + v + w}` is collinear with :math:`(A, D)`,
       :math:`(B, E)`, and :math:`(C, F)`.
    2. :math:`\frac{\overline{AF}}{\overline{FB}} \cdot \frac{\overline{BD}}{\overline{DC}} \cdot \frac{\overline{CE}}{\overline{EA}} - 1 = 0`.
    3. :math:`[\triangle PBC] : [\triangle PCA] : [\triangle PAB] = u : v : w`.

    Returns:
        Dictionary of simplified symbolic residuals (every residual identically ``0``).
    """
    xa, ya, xb, yb, xc, yc = sp.symbols("x_A y_A x_B y_B x_C y_C", real=True)
    u_s, v_s, w_s = sp.symbols("u v w", real=True, nonzero=True)
    res = solve_static_barycentrics(
        u_s,
        v_s,
        w_s,
        ((xa, ya), (xb, yb), (xc, yc)),
        name="P_sym",
    )
    a_pt, b_pt, c_pt = res.vertices
    col_adp = sp.simplify(signed_area2(a_pt, res.foot_d, res.center))
    col_bep = sp.simplify(signed_area2(b_pt, res.foot_e, res.center))
    col_cfp = sp.simplify(signed_area2(c_pt, res.foot_f, res.center))
    area_tot = sp.simplify(signed_area2(a_pt, b_pt, c_pt) / 2)
    bary_area_u = sp.simplify(res.area_pbc / area_tot - u_s / (u_s + v_s + w_s))
    bary_area_v = sp.simplify(res.area_pca / area_tot - v_s / (u_s + v_s + w_s))
    bary_area_w = sp.simplify(res.area_pab / area_tot - w_s / (u_s + v_s + w_s))
    return {
        "ceva_product_minus_one": sp.simplify(res.ceva_product - 1),
        "collinear_ADP": col_adp,
        "collinear_BEP": col_bep,
        "collinear_CFP": col_cfp,
        "barycentric_area_u": bary_area_u,
        "barycentric_area_v": bary_area_v,
        "barycentric_area_w": bary_area_w,
    }


@proposition(
    "Ceva.LibI.PropVI",
    kind="theorem",
    title="Ceva's Theorem (Liber Primus, Elementa II–III & Prop. VI)",
)
def construct_ceva_concurrency(
    u: int | sp.Rational = 24,
    v: int | sp.Rational = 28,
    w: int | sp.Rational = 21,
    vertices: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = HERONIAN_VERTICES,
) -> Model:
    """Construct exact cevian concurrency in :class:`~geometor.model.Model` for weights ``(u, v, w)``.

    Supports both interior concurrency (all weights same sign, e.g. Gergonne ``(24, 28, 21)``)
    and exterior concurrency with negative static weights (*Elementum* III & p. 5 *Scholium*,
    e.g. ``(-14, 15, 13)``). Constructs ``P`` strictly as the intersection ``AD ∩ BE`` via
    ``model.intersect`` and deductively demonstrates ``P ∈ CF`` and Ceva's ratio product ``= 1``.

    Args:
        u: Exact rational weight at ``A``.
        v: Exact rational weight at ``B``.
        w: Exact rational weight at ``C``.
        vertices: Rational vertex coordinates ``(A, B, C)``.

    Returns:
        Verified :class:`~geometor.model.Model` with ``auto_intersect=False`` and zero floats.
    """
    sol = solve_static_barycentrics(u, v, w, vertices, name="P")
    model = Model("ceva_concurrency", auto_intersect=False)

    # 1. Given: Triangle ABC and static lever fulcrums D, E, F
    a_pt = model.set_point(sol.vertices[0].x, sol.vertices[0].y, classes=["given"], ID="A")
    b_pt = model.set_point(sol.vertices[1].x, sol.vertices[1].y, classes=["given"], ID="B")
    c_pt = model.set_point(sol.vertices[2].x, sol.vertices[2].y, classes=["given"], ID="C")
    model.construct_polygon([a_pt, b_pt, c_pt], classes=["given"], ID="triABC")

    line_bc = model.construct_line(b_pt, c_pt, classes=["given"], guide=True, ID="lineBC")
    line_ca = model.construct_line(c_pt, a_pt, classes=["given"], guide=True, ID="lineCA")
    line_ab = model.construct_line(a_pt, b_pt, classes=["given"], guide=True, ID="lineAB")

    d_pt = model.set_point(sol.foot_d.x, sol.foot_d.y, classes=["given"], ID="D")
    e_pt = model.set_point(sol.foot_e.x, sol.foot_e.y, classes=["given"], ID="E")
    f_pt = model.set_point(sol.foot_f.x, sol.foot_f.y, classes=["given"], ID="F")

    # 2. Construct: Cevians AD, BE, CF and intersect AD ∩ BE at P
    cev_ad = model.construct_line(a_pt, d_pt, classes=["cevian"], ID="AD", by="Post.1")
    cev_be = model.construct_line(b_pt, e_pt, classes=["cevian"], ID="BE", by="Post.1")
    cev_cf = model.construct_line(c_pt, f_pt, classes=["cevian"], ID="CF", by="Post.1")

    p_pt = model.intersect(cev_ad, cev_be, ID="P", classes=["center"], by="Lib.I.Elem.II")

    # 3. Demonstrate: Collinearity on sides, incidence of P on third cevian CF, and Ceva product = 1
    model.assert_incident(d_pt, line_bc, by="Lib.I.Lemma.I", label="D balances B and C on BC")
    model.assert_incident(e_pt, line_ca, by="Lib.I.Lemma.I", label="E balances C and A on CA")
    model.assert_incident(f_pt, line_ab, by="Lib.I.Lemma.I", label="F balances A and B on AB")
    model.assert_incident(
        p_pt,
        cev_cf,
        by="Ceva Lib.I.Prop.VI",
        label="Third cevian CF passes through P = AD ∩ BE",
    )
    model.assert_collinear(c_pt, f_pt, p_pt, by="Ceva Lib.I.Elem.II")

    if not zero_test(sol.ceva_product - 1):
        raise AssertionError(f"Ceva product != 1: {sol.ceva_product}")
    if not (zero_test(p_pt.x - sol.center.x) and zero_test(p_pt.y - sol.center.y)):
        raise AssertionError(f"Constructed P {p_pt} != static center {sol.center}")

    model.conclude(p_pt, cev_ad, cev_be, cev_cf, kind="qed", by="Ceva 1678 Lib.I.Prop.VII")
    return model


@proposition(
    "Ceva.LibII.PropI.Isotomic",
    kind="theorem",
    title="Isotomic Conjugate Concurrency (Gergonne X(7) <-> Nagel X(8))",
)
def construct_isotomic_conjugate(
    u: int | sp.Rational = 24,
    v: int | sp.Rational = 28,
    w: int | sp.Rational = 21,
    vertices: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = HERONIAN_VERTICES,
) -> Model:
    r"""Construct the isotomic conjugate :math:`P' = (u^{-1}:v^{-1}:w^{-1})` via side-midpoint reflection.

    Reflects each cevian foot :math:`D, E, F` of :math:`P = (u:v:w)` across the midpoints
    :math:`M_A, M_B, M_C` of :math:`BC, CA, AB` to obtain :math:`D^*, E^*, F^*` satisfying
    :math:`BD^* = DC`, :math:`CE^* = EA`, :math:`AF^* = FB`, and proves by Ceva's Converse
    (*Liber Secundus*, *Prop.* I *Corollarium*) that :math:`AD^*, BE^*, CF^*` concur at
    the isotomic conjugate :math:`P^*`. For :math:`(24:28:21)`, :math:`P = X(7)` (Gergonne)
    and :math:`P^* = X(8)` (Nagel).

    Args:
        u: Exact non-zero rational weight at ``A``.
        v: Exact non-zero rational weight at ``B``.
        w: Exact non-zero rational weight at ``C``.
        vertices: Rational vertex coordinates ``(A, B, C)``.

    Returns:
        Verified :class:`~geometor.model.Model` proving isotomic segment equalities and concurrency.
    """
    sol_p = solve_static_barycentrics(u, v, w, vertices, name="P")
    sol_iso = solve_static_barycentrics(
        sp.Rational(1) / sp.sympify(u),
        sp.Rational(1) / sp.sympify(v),
        sp.Rational(1) / sp.sympify(w),
        vertices,
        name="P_iso",
    )

    model = Model("ceva_isotomic_conjugate", auto_intersect=False)
    a_pt = model.set_point(sol_p.vertices[0].x, sol_p.vertices[0].y, classes=["given"], ID="A")
    b_pt = model.set_point(sol_p.vertices[1].x, sol_p.vertices[1].y, classes=["given"], ID="B")
    c_pt = model.set_point(sol_p.vertices[2].x, sol_p.vertices[2].y, classes=["given"], ID="C")
    model.construct_polygon([a_pt, b_pt, c_pt], classes=["given"], ID="triABC")

    d_pt = model.set_point(sol_p.foot_d.x, sol_p.foot_d.y, classes=["given"], ID="D")
    e_pt = model.set_point(sol_p.foot_e.x, sol_p.foot_e.y, classes=["given"], ID="E")
    f_pt = model.set_point(sol_p.foot_f.x, sol_p.foot_f.y, classes=["given"], ID="F")

    # Reflect each foot across the side midpoint: D* = B + C - D
    d_iso = model.set_point(
        b_pt.x + c_pt.x - d_pt.x,
        b_pt.y + c_pt.y - d_pt.y,
        classes=["isotomic"],
        ID="D_iso",
    )
    e_iso = model.set_point(
        c_pt.x + a_pt.x - e_pt.x,
        c_pt.y + a_pt.y - e_pt.y,
        classes=["isotomic"],
        ID="E_iso",
    )
    f_iso = model.set_point(
        a_pt.x + b_pt.x - f_pt.x,
        a_pt.y + b_pt.y - f_pt.y,
        classes=["isotomic"],
        ID="F_iso",
    )

    cev_ad = model.construct_line(a_pt, d_pt, classes=["cevian"], guide=True, ID="AD")
    cev_be = model.construct_line(b_pt, e_pt, classes=["cevian"], guide=True, ID="BE")
    cev_cf = model.construct_line(c_pt, f_pt, classes=["cevian"], guide=True, ID="CF")
    p_pt = model.intersect(cev_ad, cev_be, ID="P", classes=["center"])

    iso_ad = model.construct_line(a_pt, d_iso, classes=["isotomic"], ID="AD_iso")
    iso_be = model.construct_line(b_pt, e_iso, classes=["isotomic"], ID="BE_iso")
    iso_cf = model.construct_line(c_pt, f_iso, classes=["isotomic"], ID="CF_iso")
    p_iso = model.intersect(iso_ad, iso_be, ID="P_iso", classes=["isotomic_center"])

    # Demonstrate isotomic segment quadrance equalities and concurrency of third isotomic cevian
    model.assert_equal((b_pt, d_pt), (d_iso, c_pt), by="Isotomic Def", label="BD = D*C")
    model.assert_equal((c_pt, e_pt), (e_iso, a_pt), by="Isotomic Def", label="CE = E*A")
    model.assert_equal((a_pt, f_pt), (f_iso, b_pt), by="Isotomic Def", label="AF = F*B")
    model.assert_incident(p_pt, cev_cf, by="Ceva Lib.II.Prop.I")
    model.assert_incident(
        p_iso,
        iso_cf,
        by="Ceva Lib.II.Prop.I.Coroll",
        label="Reciprocal ratio product = 1 implies AD*, BE*, CF* concur at P*",
    )

    if not (zero_test(p_iso.x - sol_iso.center.x) and zero_test(p_iso.y - sol_iso.center.y)):
        raise AssertionError(f"Constructed P_iso {p_iso} != {sol_iso.center}")

    model.conclude(p_pt, p_iso, iso_ad, iso_be, iso_cf, kind="qed", by="Ceva Lib.II.Prop.I.Coroll")
    return model


@proposition(
    "Ceva.LibI.PropVIII.Harmonic",
    kind="theorem",
    title="Cevian–Menelaus Harmonic Range (B, C; D, D') = -1",
)
def construct_cevian_menelaus_harmonic(
    u: int | sp.Rational = 24,
    v: int | sp.Rational = 28,
    w: int | sp.Rational = 21,
    vertices: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = HERONIAN_VERTICES,
) -> Model:
    """Construct the projective harmonic conjugate ``D' = EF ∩ BC`` of a cevian foot ``D``.

    Combines Ceva's interior concurrency (*Elementum* II, *Prop.* VII) with Ceva's static
    proof of Menelaus's Transversal Theorem (*Elementum* I, *Prop.* VIII): for any point
    ``P = (u:v:w)`` with ``v != w``, the line ``EF`` joining two cevian feet meets the
    third side ``BC`` at ``D'`` such that ``(B, C; D, D') = -1``.

    Args:
        u: Exact rational weight at ``A``.
        v: Exact rational weight at ``B`` (must differ from ``w`` so ``EF`` meets ``BC`` finitely).
        w: Exact rational weight at ``C``.
        vertices: Rational vertex coordinates ``(A, B, C)``.

    Returns:
        Verified :class:`~geometor.model.Model` whose collinear points ``(B, C, D, D')``
        satisfy ``is_harmonic(B, C, D, D') == True``.
    """
    if zero_test(sp.sympify(v) - sp.sympify(w)):
        raise ValueError("v and w must differ so transversal EF intersects BC at a finite point.")

    sol = solve_static_barycentrics(u, v, w, vertices, name="P")
    model = Model("cevian_menelaus_harmonic", auto_intersect=False)

    a_pt = model.set_point(sol.vertices[0].x, sol.vertices[0].y, classes=["given"], ID="A")
    b_pt = model.set_point(sol.vertices[1].x, sol.vertices[1].y, classes=["given"], ID="B")
    c_pt = model.set_point(sol.vertices[2].x, sol.vertices[2].y, classes=["given"], ID="C")
    model.construct_polygon([a_pt, b_pt, c_pt], classes=["given"], ID="triABC")

    line_bc = model.construct_line(b_pt, c_pt, classes=["given"], ID="lineBC")
    d_pt = model.set_point(sol.foot_d.x, sol.foot_d.y, classes=["given"], ID="D")
    e_pt = model.set_point(sol.foot_e.x, sol.foot_e.y, classes=["given"], ID="E")
    f_pt = model.set_point(sol.foot_f.x, sol.foot_f.y, classes=["given"], ID="F")

    cev_ad = model.construct_line(a_pt, d_pt, classes=["cevian"], ID="AD")
    cev_be = model.construct_line(b_pt, e_pt, classes=["cevian"], ID="BE")
    cev_cf = model.construct_line(c_pt, f_pt, classes=["cevian"], ID="CF")
    p_pt = model.intersect(cev_ad, cev_be, ID="P", classes=["center"])

    trans_ef = model.construct_line(e_pt, f_pt, classes=["transversal"], ID="EF")
    d_prime = model.intersect(
        trans_ef,
        line_bc,
        ID="D_prime",
        classes=["harmonic_conjugate"],
        by="Ceva Lib.I.Elem.I (Menelaus)",
    )

    model.assert_incident(p_pt, cev_cf, by="Ceva Lib.I.Prop.VII")
    model.assert_collinear(b_pt, c_pt, d_pt, d_prime, by="Line BC")

    # Verify Menelaus signed product = -1 and harmonic cross-ratio (B, C; D, D') = -1
    r_bdp_dpc = directed_ratio_collinear(b_pt, d_prime, c_pt)
    menelaus_prod = clean_expr(sp.simplify(sol.ratio_af_fb * r_bdp_dpc * sol.ratio_ce_ea))
    if not zero_test(menelaus_prod + 1):
        raise AssertionError(f"Menelaus signed product != -1: {menelaus_prod}")

    cr = cross_ratio(b_pt, c_pt, d_pt, d_prime)
    if not is_harmonic(b_pt, c_pt, d_pt, d_prime):
        raise AssertionError(f"Cross-ratio (B, C; D, D') = {cr} != -1")

    model.conclude(d_prime, trans_ef, p_pt, kind="qed", by="Harmonic Division (B,C;D,D')=-1")
    return model


def verify_spread_ceva(
    u: int | sp.Rational = 14,
    v: int | sp.Rational = 15,
    w: int | sp.Rational = 13,
    vertices: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = HERONIAN_VERTICES,
) -> SpreadCevaResult:
    r"""Verify Rational Trigonometry **Spread Ceva's Theorem** with zero square roots.

    For concurrent cevians ``AD, BE, CF`` meeting at ``P = (u:v:w)``, computes the six
    exact vertex spreads ``s(BAD), s(DAC), s(CBE), s(EBA), s(ACF), s(FCB)`` and six segment
    quadrances over :math:`\mathbb{Q}` and verifies:

    .. math::

       \frac{s(\angle BAD)}{s(\angle DAC)} \cdot
       \frac{s(\angle CBE)}{s(\angle EBA)} \cdot
       \frac{s(\angle ACF)}{s(\angle FCB)} = 1,
       \qquad
       \frac{Q(AF)}{Q(FB)} \cdot \frac{Q(BD)}{Q(DC)} \cdot \frac{Q(CE)}{Q(EA)} = 1.

    Args:
        u: Exact rational weight at ``A``.
        v: Exact rational weight at ``B``.
        w: Exact rational weight at ``C``.
        vertices: Rational vertex coordinates ``(A, B, C)``.

    Returns:
        Verified :class:`SpreadCevaResult` over :math:`\mathbb{Q}`.
    """
    sol = solve_static_barycentrics(u, v, w, vertices, name="P_spread")
    a_pt, b_pt, c_pt = sol.vertices
    d_pt, e_pt, f_pt = sol.foot_d, sol.foot_e, sol.foot_f

    s_bad = vertex_spread(b_pt, a_pt, d_pt)
    s_dac = vertex_spread(d_pt, a_pt, c_pt)
    s_cbe = vertex_spread(c_pt, b_pt, e_pt)
    s_eba = vertex_spread(e_pt, b_pt, a_pt)
    s_acf = vertex_spread(a_pt, c_pt, f_pt)
    s_fcb = vertex_spread(f_pt, c_pt, b_pt)

    spread_prod = clean_expr(
        sp.simplify((s_bad / s_dac) * (s_cbe / s_eba) * (s_acf / s_fcb))
    )
    quad_prod = clean_expr(
        sp.simplify(
            (quadrance(a_pt, f_pt) / quadrance(f_pt, b_pt))
            * (quadrance(b_pt, d_pt) / quadrance(d_pt, c_pt))
            * (quadrance(c_pt, e_pt) / quadrance(e_pt, a_pt))
        )
    )
    if not zero_test(spread_prod - 1):
        raise AssertionError(f"Spread Ceva product != 1: {spread_prod}")
    if not zero_test(quad_prod - 1):
        raise AssertionError(f"Quadrance Ceva product != 1: {quad_prod}")

    return SpreadCevaResult(
        spread_bad=s_bad,
        spread_dac=s_dac,
        spread_cbe=s_cbe,
        spread_eba=s_eba,
        spread_acf=s_acf,
        spread_fcb=s_fcb,
        spread_product=spread_prod,
        quadrance_product=quad_prod,
    )
