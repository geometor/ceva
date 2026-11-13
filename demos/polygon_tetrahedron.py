#!/usr/bin/env python3
"""Exact symbolic demonstration of multilateral polygons, 3D tetrahedra, and Appendix Geometrica."""

from __future__ import annotations

from rich.console import Console

from geometor.ceva import (
    construct_pentagon_ceva,
    prove_circumscribed_polygon_lemma,
    solve_tetrahedron_static_equilibrium,
    verify_appendix_invariants,
    verify_odd_polygon_ceva,
    verify_skew_quadrilateral_ceva,
)


def run_demo() -> None:
    """Execute exact symbolic verifications for Liber Secundus, 3D statics, and Appendix."""
    console = Console()

    console.print(
        "[bold amber1]1. Liber Secundus: Odd Multilateral Polygon Ceva & Circumscribed Conic Lemma I[/bold amber1]"
    )
    pent = verify_odd_polygon_ceva()
    pent_model = construct_pentagon_ceva()
    conic_lemma = prove_circumscribed_polygon_lemma(5)
    console.print(f"  • Rational Pentagon side ratios: {pent.side_ratios}")
    console.print(
        f"  • Cyclic opposite-side product = [green]{pent.cyclic_product}[/green] "
        f"(Model elements: {len(pent_model)})"
    )
    console.print(f"  • Borelli–Serenus Circumscribed Ellipse residuals: {conic_lemma}")

    console.print(
        "\n[bold amber1]2. Liber Primus Elem. V Coroll. & Prop. XXIII: 3D Skew Quad & 7-Line Tetrahedron[/bold amber1]"
    )
    skew = verify_skew_quadrilateral_ceva()
    tet = solve_tetrahedron_static_equilibrium()
    console.print(
        f"  • 3D Skew Quadrilateral: 6·Vol = {skew.tetrahedron_det6}, "
        f"coplanarity det = [green]{skew.fulcrum_coplanarity_det}[/green], "
        f"cyclic product = [green]{skew.cyclic_ratio_product}[/green]"
    )
    console.print(
        f"  • 3D Tetrahedron Center O = [green]{tuple(tet.center_of_gravity)}[/green]"
    )
    console.print(f"  • 4 Vertex-to-Face-CG ratios VO/OG: {tet.vertex_cevian_ratios}")
    console.print(f"  • 3 Skew-Edge Bimedian ratios: {tet.bimedian_ratios}")

    console.print(
        "\n[bold amber1]3. Appendix Geometrica: Lune Quadrature, Ungula Cubature & Centroids[/bold amber1]"
    )
    app = verify_appendix_invariants()
    for k, val in app.items():
        console.print(f"  • {k}: [green]{val}[/green]")


if __name__ == "__main__":
    run_demo()
