r"""Multilateral polygons, circumscribed conics, 3D tetrahedra, and Appendix theorems (1678).

Formalizes *Liber Primus* (Props. V *Coroll.*, XXII–XXVI), *Liber Secundus* (*Lemma* I,
Props. I–XIV), and *Appendix Geometrica* (Props. I–XVI) of Giovanni Ceva's
*De lineis rectis se invicem secantibus statica constructio* (Milan, 1678) in 100%
exact symbolic algebra:

- **Odd Multilateral Polygon Ceva Concurrency** (:func:`verify_odd_polygon_ceva`,
  :func:`construct_pentagon_ceva`): Verifies over :math:`\mathbb{Q}` that rays joining
  the :math:`2m + 1` vertices of an odd polygon through a common point :math:`P` divide
  the opposite sides in cyclic directed product :math:`+1`.
- **Circumscribed Conic Contact Ratio (*Liber Secundus, Lemma I*)**
  (:func:`prove_circumscribed_polygon_lemma`): Proves symbolically that any :math:`n`-gon
  circumscribed around a circle or ellipse (via Ceva's Borelli–Serenus cylindrical /
  affine projection) divides its sides at the contact points in cyclic product :math:`1`.
- **3D Tetrahedron 7-Line Static Equilibrium (*Liber Primus, Prop. XXIII*)**
  (:func:`solve_tetrahedron_static_equilibrium`): Computes the 6 edge fulcrums, 4 face
  centers of gravity, and unique 3D center of gravity :math:`O` for four spatial weights
  :math:`(m_A, m_B, m_C, m_D)`, proving that all 4 vertex-to-face-barycenter cevians and
  all 3 opposite-edge fulcrum joins concur at :math:`O` (*"mira quadam concordia"*).
- **3D Skew Quadrilateral Concurrency (*Liber Primus, Elementum V Corollarium*)**
  (:func:`verify_skew_quadrilateral_ceva`): Proves coplanarity and intersection of
  opposite-side fulcrum joins on a non-planar 3D quadrilateral.
- **Appendix Geometrica Quadratures, Cubatures & Centers of Gravity**
  (:func:`verify_appendix_invariants`): Symbolic verification of Hippocratean lune
  quadrature (*Prop.* II), cylindrical hoof :math:`\frac{2}{3}` prism cubature (*Prop.* VII),
  hemisphere :math:`5:3` centroid (*Prop.* XIII), and paraboloid :math:`2:1` centroid (*Prop.* XIV).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr, proposition, zero_test
from geometor.model.invariants import signed_area2

from geometor.ceva.static_barycentrics import SymScalar, directed_ratio_collinear

__all__ = [
    "OddPolygonCevaResult",
    "RATIONAL_PENTAGON",
    "RATIONAL_TETRAHEDRON",
    "SkewQuadrilateralResult",
    "TetrahedronStaticResult",
    "construct_pentagon_ceva",
    "prove_circumscribed_polygon_lemma",
    "solve_tetrahedron_static_equilibrium",
    "verify_appendix_invariants",
    "verify_odd_polygon_ceva",
    "verify_skew_quadrilateral_ceva",
]

RATIONAL_PENTAGON: tuple[tuple[int, int], ...] = (
    (0, 0),
    (8, 0),
    (11, 6),
    (5, 11),
    (-2, 6),
)
"""Strictly convex rational pentagon in Q^2 for odd-polygon Ceva demonstrations."""

RATIONAL_TETRAHEDRON: tuple[
    tuple[int, int, int],
    tuple[int, int, int],
    tuple[int, int, int],
    tuple[int, int, int],
] = (
    (0, 0, 0),
    (12, 0, 0),
    (3, 10, 0),
    (4, 3, 9),
)
"""Asymmetric non-degenerate rational tetrahedron in Z^3 (6 * Volume = 1080)."""


@dataclass(frozen=True)
class OddPolygonCevaResult:
    """Exact verification record for Ceva's Theorem on an odd (2m + 1)-gon."""

    n_sides: int
    vertices: tuple[spg.Point2D, ...]
    center: spg.Point2D
    feet: tuple[spg.Point2D, ...]
    side_ratios: tuple[sp.Expr, ...]
    cyclic_product: sp.Expr


@dataclass(frozen=True)
class TetrahedronStaticResult:
    """Exact 3D static equilibrium of 4 weights on a tetrahedron (Lib. I Prop. XXIII)."""

    weights: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    vertices: tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]
    edge_fulcrums: dict[str, sp.Matrix]
    face_centers: dict[str, sp.Matrix]
    center_of_gravity: sp.Matrix
    vertex_cevian_ratios: dict[str, sp.Expr]
    bimedian_ratios: dict[str, sp.Expr]
    concurrency_residuals_zero: bool


@dataclass(frozen=True)
class SkewQuadrilateralResult:
    """Exact 3D skew-quadrilateral static concurrency (Lib. I Elem. V Corollarium)."""

    weights: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    vertices: tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]
    side_fulcrums: tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]
    center: sp.Matrix
    cyclic_ratio_product: sp.Expr
    tetrahedron_det6: sp.Expr
    fulcrum_coplanarity_det: sp.Expr


def _pt2d(val: spg.Point2D | tuple[SymScalar, SymScalar]) -> spg.Point2D:
    """Convert coordinate pair into exact ``Point2D`` rejecting ``sp.Float``."""
    x_val, y_val = (val.x, val.y) if isinstance(val, spg.Point2D) else (val[0], val[1])
    sx, sy = clean_expr(sp.sympify(x_val)), clean_expr(sp.sympify(y_val))
    if sx.has(sp.Float) or sy.has(sp.Float):
        raise ValueError(f"Float coordinate forbidden in geometor.ceva: ({sx!r}, {sy!r})")
    return spg.Point2D(sx, sy, evaluate=False)


def _vec3(val: tuple[SymScalar, SymScalar, SymScalar] | sp.Matrix) -> sp.Matrix:
    """Convert 3-tuple into exact 3x1 SymPy column vector rejecting ``sp.Float``."""
    coords = list(val) if isinstance(val, sp.Matrix) else [val[0], val[1], val[2]]
    if len(coords) != 3:
        raise ValueError(f"Expected 3D point, got {coords!r}")
    sym_coords = [clean_expr(sp.sympify(c)) for c in coords]
    for c in sym_coords:
        if c.has(sp.Float):
            raise ValueError(f"Float coordinate forbidden in 3D point: {c!r}")
    return sp.Matrix(sym_coords)


def _directed_ratio_3d(a_vec: sp.Matrix, p_vec: sp.Matrix, b_vec: sp.Matrix) -> sp.Expr:
    """Compute exact directed ratio ``(A -> P) / (P -> B)`` for collinear 3D points."""
    ab = b_vec - a_vec
    ap = p_vec - a_vec
    pb = b_vec - p_vec
    cross_vec = ab.cross(ap)
    if not all(zero_test(c) for c in cross_vec):
        raise ValueError("3D points A, P, B are not collinear.")
    denom = clean_expr(pb.dot(ab))
    if zero_test(denom):
        raise ValueError("Division point P coincides with endpoint B.")
    return clean_expr(sp.simplify(ap.dot(ab) / denom))


def verify_odd_polygon_ceva(
    vertices: tuple[tuple[SymScalar, SymScalar] | spg.Point2D, ...] = RATIONAL_PENTAGON,
    center: tuple[SymScalar, SymScalar] | spg.Point2D = (4, 4),
) -> OddPolygonCevaResult:
    r"""Verify Ceva's cyclic ratio product ``= 1`` for any odd ``(2m + 1)``-gon.

    For each vertex :math:`V_i` (:math:`0 \le i < 2m + 1`), projects the ray :math:`V_i P`
    onto the opposite side line :math:`V_{i+m} V_{i+m+1}` (indices modulo :math:`2m + 1`)
    at :math:`Q_i` and verifies:

    .. math::

       \prod_{i=0}^{2m} \frac{\overline{V_{i+m} Q_i}}{\overline{Q_i V_{i+m+1}}} = 1.

    Args:
        vertices: Sequence of ``2m + 1`` planar vertices (``n >= 3`` odd).
        center: Concurrency point ``P`` not lying on any side line or parallel ray.

    Returns:
        Verified :class:`OddPolygonCevaResult` with exact rational/symbolic ratios.
    """
    n_sides = len(vertices)
    if n_sides < 3 or n_sides % 2 == 0:
        raise ValueError(f"Odd-polygon Ceva requires odd n >= 3, got n={n_sides}.")
    m_half = (n_sides - 1) // 2

    pts = tuple(_pt2d(v) for v in vertices)
    p_pt = _pt2d(center)

    feet: list[spg.Point2D] = []
    ratios: list[sp.Expr] = []

    for i in range(n_sides):
        vi = pts[i]
        s0 = pts[(i + m_half) % n_sides]
        s1 = pts[(i + m_half + 1) % n_sides]

        d0 = signed_area2(p_pt, vi, s0)
        d1 = signed_area2(p_pt, vi, s1)
        denom = clean_expr(d0 - d1)
        if zero_test(denom):
            raise ValueError(
                f"Ray V_{i} P is parallel to opposite side V_{i + m_half} V_{i + m_half + 1}."
            )
        t_param = clean_expr(sp.simplify(d0 / denom))
        qx = clean_expr(sp.simplify(s0.x + t_param * (s1.x - s0.x)))
        qy = clean_expr(sp.simplify(s0.y + t_param * (s1.y - s0.y)))
        q_pt = spg.Point2D(qx, qy, evaluate=False)
        feet.append(q_pt)
        ratios.append(directed_ratio_collinear(s0, q_pt, s1))

    prod = sp.Integer(1)
    for r_val in ratios:
        prod = clean_expr(sp.simplify(prod * r_val))
    if not zero_test(prod - 1):
        raise AssertionError(f"Odd-polygon Ceva product != 1: {prod}")

    return OddPolygonCevaResult(
        n_sides=n_sides,
        vertices=pts,
        center=p_pt,
        feet=tuple(feet),
        side_ratios=tuple(ratios),
        cyclic_product=prod,
    )


@proposition(
    "Ceva.LibII.Pentagon",
    kind="theorem",
    title="Pentagonal Ceva Concurrency (Liber Secundus Multilateral Generalization)",
)
def construct_pentagon_ceva(
    vertices: tuple[tuple[int, int], ...] = RATIONAL_PENTAGON,
    center: tuple[int, int] = (4, 4),
) -> Model:
    """Construct concurrent cevians of a rational pentagon in :class:`~geometor.model.Model`.

    Args:
        vertices: Five rational vertices ``V0..V4``.
        center: Rational concurrency center ``P``.

    Returns:
        Verified :class:`~geometor.model.Model` with ``auto_intersect=False`` and zero floats.
    """
    if len(vertices) != 5:
        raise ValueError("construct_pentagon_ceva expects exactly 5 vertices.")

    model = Model("pentagon_ceva", auto_intersect=False)
    v_pts = [
        model.set_point(vx, vy, classes=["given"], ID=f"V{idx}")
        for idx, (vx, vy) in enumerate(vertices)
    ]
    model.construct_polygon(v_pts, classes=["given"], ID="pentagon")
    p_pt = model.set_point(center[0], center[1], classes=["given", "center"], ID="P")

    side_lines = [
        model.construct_line(
            v_pts[i],
            v_pts[(i + 1) % 5],
            classes=["given"],
            guide=True,
            ID=f"side{i}",
        )
        for i in range(5)
    ]

    q_pts: list[spg.Point2D] = []
    cevians: list[spg.Line2D] = []
    for i in range(5):
        opp_idx = (i + 2) % 5
        ray_line = model.construct_line(
            v_pts[i], p_pt, classes=["cevian"], ID=f"cev{i}", by="Post.1"
        )
        cevians.append(ray_line)
        q_hit = model.intersect(
            ray_line,
            side_lines[opp_idx],
            ID=f"Q{i}",
            classes=["foot"],
            by="Pentagon Opposite Side Intersection",
        )
        q_pts.append(q_hit)
        model.assert_collinear(v_pts[i], p_pt, q_hit, by="Constructed Ray")

    prod = sp.Integer(1)
    for i in range(5):
        s0 = v_pts[(i + 2) % 5]
        s1 = v_pts[(i + 3) % 5]
        prod = clean_expr(sp.simplify(prod * directed_ratio_collinear(s0, q_pts[i], s1)))
    if not zero_test(prod - 1):
        raise AssertionError(f"Constructed pentagon Ceva product != 1: {prod}")

    model.conclude(p_pt, *q_pts, *cevians, kind="qed", by="Multilateral Ceva Product = 1")
    return model


def prove_circumscribed_polygon_lemma(n_sides: int = 5) -> dict[str, sp.Expr]:
    r"""Prove Ceva's *Liber Secundus, Lemma I* for polygons circumscribed about circles & ellipses.

    In *Liber Secundus, Lemma I* (`tab. 4. figs. 32–35`), Ceva proves that if an :math:`n`-gon
    is circumscribed around a circle—or, by cylindrical projection citing Borelli and Serenus,
    around any ellipse—the contact points :math:`T_0, \dots, T_{n-1}` divide the sides in cyclic
    product :math:`1`. This function verifies:

    1. Equal tangent lengths :math:`t_k` from each vertex :math:`V_k` to a circle give
       :math:`\prod_{k=0}^{n-1} \frac{t_k}{t_{k+1}} = 1`.
    2. Applying a general symbolic invertible affine map :math:`X' = M X + b` (the planar
       realization of Serenus/Borelli cylindrical section mapping the circle to an arbitrary
       ellipse) preserves every collinear contact ratio :math:`\frac{V'_k T'_k}{T'_k V'_{k+1}}`
       and maintains :math:`\prod_{k=0}^{n-1} \frac{V'_k T'_k}{T'_k V'_{k+1}} = 1`.

    Args:
        n_sides: Number of polygon sides (``n_sides >= 3``, odd or even).

    Returns:
        Dictionary of simplified symbolic residuals (all identically ``0``).
    """
    if n_sides < 3:
        raise ValueError("n_sides must be >= 3.")
    tangents = sp.symbols(f"t_0:{n_sides}", positive=True)
    circle_prod = sp.Integer(1)
    for k in range(n_sides):
        circle_prod = sp.simplify(circle_prod * (tangents[k] / tangents[(k + 1) % n_sides]))

    vx0, vy0, vx1, vy1 = sp.symbols("x_0 y_0 x_1 y_1", real=True)
    lam = sp.Symbol("lambda", positive=True)
    m11, m12, m21, m22, bx, by = sp.symbols("m_11 m_12 m_21 m_22 b_x b_y", real=True)
    m_mat = sp.Matrix([[m11, m12], [m21, m22]])
    b_vec = sp.Matrix([bx, by])

    v0 = sp.Matrix([vx0, vy0])
    v1 = sp.Matrix([vx1, vy1])
    t_pt = (v0 + lam * v1) / (1 + lam)

    v0_p = m_mat * v0 + b_vec
    v1_p = m_mat * v1 + b_vec
    t_pt_p = m_mat * t_pt + b_vec
    affine_diff = sp.simplify((t_pt_p - v0_p) - lam * (v1_p - t_pt_p))

    return {
        "circle_cyclic_product_minus_one": sp.simplify(circle_prod - 1),
        "ellipse_affine_x_residual": affine_diff[0],
        "ellipse_affine_y_residual": affine_diff[1],
    }


def solve_tetrahedron_static_equilibrium(
    weights: tuple[SymScalar, SymScalar, SymScalar, SymScalar] = (2, 3, 5, 8),
    vertices: tuple[
        tuple[SymScalar, SymScalar, SymScalar],
        tuple[SymScalar, SymScalar, SymScalar],
        tuple[SymScalar, SymScalar, SymScalar],
        tuple[SymScalar, SymScalar, SymScalar],
    ] = RATIONAL_TETRAHEDRON,
) -> TetrahedronStaticResult:
    r"""Solve Ceva's 3D tetrahedron 7-line static concurrency (*Liber Primus, Prop. XXIII*).

    Places exact weights :math:`(m_A, m_B, m_C, m_D)` at the four vertices :math:`(A, B, C, D)`
    of a 3D tetrahedron (`tab. 3. fig. 28`) and verifies that:

    1. The **4 spatial cevians** :math:`A G_A, B G_B, C G_C, D G_D` joining each vertex to
       the static center of gravity of its opposite triangular face concur at :math:`O`.
    2. The **3 spatial bimedians** :math:`E_{AB} E_{CD}, E_{AC} E_{BD}, E_{AD} E_{BC}` joining
       the lever fulcrums of opposite skew edges ALSO concur at the exact same point :math:`O`
       (*"mira quadam concordia"*).

    Args:
        weights: Four exact non-zero vertex weights ``(m_A, m_B, m_C, m_D)``.
        vertices: Four non-coplanar 3D vertices ``(A, B, C, D)``.

    Returns:
        Verified :class:`TetrahedronStaticResult` over :math:`\mathbb{Q}` (or symbolic ring).
    """
    ma, mb, mc, md = (clean_expr(sp.sympify(w)) for w in weights)
    for w_val in (ma, mb, mc, md):
        if w_val.has(sp.Float):
            raise ValueError(f"Float weight forbidden in 3D static equilibrium: {w_val!r}")
        if zero_test(w_val):
            raise ValueError("All four tetrahedron weights must be non-zero.")

    va, vb, vc, vd = (_vec3(v) for v in vertices)
    det6 = clean_expr(sp.Matrix.hstack(vb - va, vc - va, vd - va).det())
    if zero_test(det6):
        raise ValueError("Tetrahedron vertices A, B, C, D are coplanar (degenerate).")

    m_tot = clean_expr(ma + mb + mc + md)
    if zero_test(m_tot):
        raise ValueError("Total tetrahedron mass m_A + m_B + m_C + m_D vanishes.")

    named_v = {"A": (ma, va), "B": (mb, vb), "C": (mc, vc), "D": (md, vd)}
    edge_pairs = (("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D"))
    edge_fulcrums: dict[str, sp.Matrix] = {}
    for k1, k2 in edge_pairs:
        w1, p1 = named_v[k1]
        w2, p2 = named_v[k2]
        w12 = clean_expr(w1 + w2)
        if zero_test(w12):
            raise ValueError(f"Pairwise edge weight sum m_{k1} + m_{k2} vanishes.")
        edge_fulcrums[f"{k1}{k2}"] = sp.Matrix(
            [clean_expr(sp.simplify((w1 * p1[i] + w2 * p2[i]) / w12)) for i in range(3)]
        )

    face_specs = (
        ("A", ("B", "C", "D")),
        ("B", ("A", "C", "D")),
        ("C", ("A", "B", "D")),
        ("D", ("A", "B", "C")),
    )
    face_centers: dict[str, sp.Matrix] = {}
    for opp_key, (f1, f2, f3) in face_specs:
        w1, p1 = named_v[f1]
        w2, p2 = named_v[f2]
        w3, p3 = named_v[f3]
        wf = clean_expr(w1 + w2 + w3)
        if zero_test(wf):
            raise ValueError(f"Face weight sum opposite {opp_key} vanishes.")
        face_centers[opp_key] = sp.Matrix(
            [
                clean_expr(sp.simplify((w1 * p1[i] + w2 * p2[i] + w3 * p3[i]) / wf))
                for i in range(3)
            ]
        )

    center_o = sp.Matrix(
        [
            clean_expr(
                sp.simplify((ma * va[i] + mb * vb[i] + mc * vc[i] + md * vd[i]) / m_tot)
            )
            for i in range(3)
        ]
    )

    vertex_cevian_ratios: dict[str, sp.Expr] = {}
    all_zero = True
    for key, (w_key, p_key) in named_v.items():
        g_opp = face_centers[key]
        ratio_vo_og = _directed_ratio_3d(p_key, center_o, g_opp)
        expected = clean_expr(sp.simplify((m_tot - w_key) / w_key))
        if not zero_test(ratio_vo_og - expected):
            all_zero = False
        vertex_cevian_ratios[key] = ratio_vo_og

    bimedian_specs = (("AB", "CD"), ("AC", "BD"), ("AD", "BC"))
    bimedian_ratios: dict[str, sp.Expr] = {}
    for e1, e2 in bimedian_specs:
        f1_pt = edge_fulcrums[e1]
        f2_pt = edge_fulcrums[e2]
        ratio_b = _directed_ratio_3d(f1_pt, center_o, f2_pt)
        w_e1 = named_v[e1[0]][0] + named_v[e1[1]][0]
        w_e2 = named_v[e2[0]][0] + named_v[e2[1]][0]
        expected_b = clean_expr(sp.simplify(w_e2 / w_e1))
        if not zero_test(ratio_b - expected_b):
            all_zero = False
        bimedian_ratios[f"{e1}-{e2}"] = ratio_b

    if not all_zero:
        raise AssertionError("3D tetrahedron 7-line static concurrency check failed.")

    return TetrahedronStaticResult(
        weights=(ma, mb, mc, md),
        vertices=(va, vb, vc, vd),
        edge_fulcrums=edge_fulcrums,
        face_centers=face_centers,
        center_of_gravity=center_o,
        vertex_cevian_ratios=vertex_cevian_ratios,
        bimedian_ratios=bimedian_ratios,
        concurrency_residuals_zero=all_zero,
    )


def verify_skew_quadrilateral_ceva(
    weights: tuple[SymScalar, SymScalar, SymScalar, SymScalar] = (2, 3, 5, 7),
    vertices: tuple[
        tuple[SymScalar, SymScalar, SymScalar],
        tuple[SymScalar, SymScalar, SymScalar],
        tuple[SymScalar, SymScalar, SymScalar],
        tuple[SymScalar, SymScalar, SymScalar],
    ] = RATIONAL_TETRAHEDRON,
) -> SkewQuadrilateralResult:
    r"""Verify Ceva's *Liber Primus, Elementum V Corollarium* on a 3D skew quadrilateral.

    Along the cyclic skew quadrilateral ``A -> B -> C -> D -> A`` in :math:`\mathbb{R}^3`,
    the four side fulcrums :math:`E_{AB}, E_{BC}, E_{CD}, E_{DA}` divide the skew sides in
    cyclic ratio product ``1``, lie in a single plane, and have opposite joins
    :math:`E_{AB} E_{CD}` and :math:`E_{BC} E_{DA}` intersecting at :math:`O`.

    Args:
        weights: Four exact non-zero weights ``(m_A, m_B, m_C, m_D)``.
        vertices: Four non-coplanar 3D vertices ``(A, B, C, D)``.

    Returns:
        Verified :class:`SkewQuadrilateralResult`.
    """
    ma, mb, mc, md = (clean_expr(sp.sympify(w)) for w in weights)
    va, vb, vc, vd = (_vec3(v) for v in vertices)
    det6 = clean_expr(sp.Matrix.hstack(vb - va, vc - va, vd - va).det())
    if zero_test(det6):
        raise ValueError("Vertices A, B, C, D are coplanar; expected 3D skew quadrilateral.")

    e_ab = (ma * va + mb * vb) / (ma + mb)
    e_bc = (mb * vb + mc * vc) / (mb + mc)
    e_cd = (mc * vc + md * vd) / (mc + md)
    e_da = (md * vd + ma * va) / (md + ma)
    center_o = (ma * va + mb * vb + mc * vc + md * vd) / (ma + mb + mc + md)

    r1 = _directed_ratio_3d(va, e_ab, vb)
    r2 = _directed_ratio_3d(vb, e_bc, vc)
    r3 = _directed_ratio_3d(vc, e_cd, vd)
    r4 = _directed_ratio_3d(vd, e_da, va)
    prod = clean_expr(sp.simplify(r1 * r2 * r3 * r4))

    copl_det = clean_expr(
        sp.simplify(sp.Matrix.hstack(e_bc - e_ab, e_cd - e_ab, e_da - e_ab).det())
    )
    _directed_ratio_3d(e_ab, center_o, e_cd)
    _directed_ratio_3d(e_bc, center_o, e_da)

    if not zero_test(prod - 1) or not zero_test(copl_det):
        raise AssertionError("Skew quadrilateral Ceva concurrency verification failed.")

    return SkewQuadrilateralResult(
        weights=(ma, mb, mc, md),
        vertices=(va, vb, vc, vd),
        side_fulcrums=(e_ab, e_bc, e_cd, e_da),
        center=center_o,
        cyclic_ratio_product=prod,
        tetrahedron_det6=det6,
        fulcrum_coplanarity_det=copl_det,
    )


def verify_appendix_invariants() -> dict[str, sp.Expr]:
    r"""Verify key quadrature, cubature, and centroid propositions in *Appendix Geometrica*.

    Symbolically confirms four signature results from Printed pp. 63–83:

    1. **Prop. II (Hippocratean Lune Quadrature)**: For an isosceles right triangle of legs
       :math:`R` and hypotenuse :math:`R\sqrt{2}`, the lune bounded by the semicircle on
       the hypotenuse (radius :math:`R/\sqrt{2}`) and the quadrant arc of radius :math:`R`
       has exact area :math:`\frac{1}{2} R^2 = [\triangle ABC]` (all :math:`\pi` terms cancel).
    2. **Prop. VII (Cylindrical Hoof / Ungula Cubature)**: A plane through a diameter of the
       base of a right circular cylinder (radius :math:`R`, altitude :math:`H`) cuts off a
       cylindrical hoof whose volume :math:`\frac{2}{3} R^2 H` equals exactly :math:`\frac{2}{3}`
       of the circumscribed triangular prism (volume :math:`R^2 H`).
    3. **Prop. XIII (Hemisphere Center of Gravity)**: Divides the axis from vertex to base
       in the exact ratio :math:`5 : 3` (:math:`\bar{z} = \frac{3}{8} R` from the base,
       :math:`\frac{5}{8} R` from the vertex).
    4. **Prop. XIV (Parabolic Conoid Center of Gravity)**: Divides the axis from vertex to
       base in the exact ratio :math:`2 : 1` (:math:`\bar{z} = \frac{2}{3} H` from the vertex).

    Returns:
        Dictionary of exact symbolic ratios and zero-residuals.
    """
    r_sym, h_sym, x_sym, z_sym = sp.symbols("R H x z", positive=True)

    # 1. Prop. II: Semicircle on hypotenuse (r = R / sqrt(2)) minus circular segment of quadrant R
    area_triangle = sp.Rational(1, 2) * r_sym**2
    area_semicircle_hyp = sp.Rational(1, 2) * sp.pi * (r_sym / sp.sqrt(2)) ** 2
    area_quadrant_seg = sp.Rational(1, 4) * sp.pi * r_sym**2 - area_triangle
    area_lune = sp.simplify(area_semicircle_hyp - area_quadrant_seg)
    lune_residual = sp.simplify(area_lune - area_triangle)

    # 2. Prop. VII: Cavalieri slice of cylindrical ungula vs circumscribed right-triangular prism
    y_sq = r_sym**2 - x_sym**2
    vol_ungula = sp.integrate(sp.Rational(1, 2) * (h_sym / r_sym) * y_sq, (x_sym, -r_sym, r_sym))
    vol_circumscribed_prism = r_sym**2 * h_sym
    ungula_to_prism_ratio = sp.simplify(vol_ungula / vol_circumscribed_prism)

    # 3. Prop. XIII: Hemisphere z in [0, R] with vertex at z = 0 and base at z = R
    hemisphere_vol = sp.integrate(sp.pi * (2 * r_sym * z_sym - z_sym**2), (z_sym, 0, r_sym))
    hemisphere_mom = sp.integrate(
        z_sym * sp.pi * (2 * r_sym * z_sym - z_sym**2), (z_sym, 0, r_sym)
    )
    z_bar_hemi = sp.simplify(hemisphere_mom / hemisphere_vol)
    hemi_axis_ratio = sp.simplify(z_bar_hemi / (r_sym - z_bar_hemi))

    # 4. Prop. XIV: Parabolic conoid z in [0, H] from vertex z = 0
    paraboloid_vol = sp.integrate(z_sym, (z_sym, 0, h_sym))
    paraboloid_mom = sp.integrate(z_sym * z_sym, (z_sym, 0, h_sym))
    z_bar_parab = sp.simplify(paraboloid_mom / paraboloid_vol)
    parab_axis_ratio = sp.simplify(z_bar_parab / (h_sym - z_bar_parab))

    return {
        "lune_minus_triangle_residual": lune_residual,
        "ungula_to_prism_ratio": ungula_to_prism_ratio,
        "hemisphere_vertex_to_base_ratio": hemi_axis_ratio,
        "paraboloid_vertex_to_base_ratio": parab_axis_ratio,
    }
