"""GEOMETOR Ceva: Static barycentrics, cevian concurrency, and Digital Scriptorium Codex.

Provides 100% exact symbolic ``SymPy`` and ``geometor.model`` constructions and proofs for
Giovanni Ceva's *De lineis rectis se invicem secantibus statica constructio* (Milan, 1678).
"""

from __future__ import annotations

from geometor.ceva.polygon_tetrahedron import (
    RATIONAL_PENTAGON,
    RATIONAL_TETRAHEDRON,
    OddPolygonCevaResult,
    SkewQuadrilateralResult,
    TetrahedronStaticResult,
    construct_pentagon_ceva,
    prove_circumscribed_polygon_lemma,
    solve_tetrahedron_static_equilibrium,
    verify_appendix_invariants,
    verify_odd_polygon_ceva,
    verify_skew_quadrilateral_ceva,
)
from geometor.ceva.static_barycentrics import (
    CANONICAL_CENTERS,
    HERONIAN_VERTICES,
    SpreadCevaResult,
    StaticBarycentricResult,
    construct_ceva_concurrency,
    construct_cevian_menelaus_harmonic,
    construct_isotomic_conjugate,
    directed_ratio_collinear,
    evaluate_canonical_centers,
    prove_ceva_barycentric_identity,
    solve_static_barycentrics,
    verify_spread_ceva,
)

__version__ = "0.1.0"

__all__ = [
    "CANONICAL_CENTERS",
    "HERONIAN_VERTICES",
    "OddPolygonCevaResult",
    "RATIONAL_PENTAGON",
    "RATIONAL_TETRAHEDRON",
    "SkewQuadrilateralResult",
    "SpreadCevaResult",
    "StaticBarycentricResult",
    "TetrahedronStaticResult",
    "__version__",
    "construct_ceva_concurrency",
    "construct_cevian_menelaus_harmonic",
    "construct_isotomic_conjugate",
    "construct_pentagon_ceva",
    "directed_ratio_collinear",
    "evaluate_canonical_centers",
    "prove_ceva_barycentric_identity",
    "prove_circumscribed_polygon_lemma",
    "solve_static_barycentrics",
    "solve_tetrahedron_static_equilibrium",
    "verify_appendix_invariants",
    "verify_odd_polygon_ceva",
    "verify_skew_quadrilateral_ceva",
    "verify_spread_ceva",
]
