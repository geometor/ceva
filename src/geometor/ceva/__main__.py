"""Rich CLI summary for ``geometor.ceva`` (``ceva`` console entry point)."""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from geometor.ceva import (
    CANONICAL_CENTERS,
    __version__,
    evaluate_canonical_centers,
    solve_tetrahedron_static_equilibrium,
    verify_appendix_invariants,
    verify_odd_polygon_ceva,
    verify_spread_ceva,
)


def main() -> None:
    """Print an exact symbolic summary of Ceva's 1678 theorems over Q."""
    console = Console()
    console.print(
        f"[bold amber1]GEOMETOR • Ceva[/bold amber1] v{__version__} — "
        "[italic]De lineis rectis se invicem secantibus statica constructio[/italic] (Milan, 1678)"
    )

    table = Table(
        title="Canonical Triangle Centers on Heronian Δ(13, 14, 15): A=(5,12), B=(0,0), C=(14,0)",
        show_lines=False,
    )
    table.add_column("Center", style="bold cyan")
    table.add_column("Weights (u : v : w)", style="magenta")
    table.add_column("Exact P in Q^2", style="green")
    table.add_column("AF/FB · BD/DC · CE/EA", style="yellow")
    table.add_column("Regime")

    centers = evaluate_canonical_centers()
    for code, res in centers.items():
        _desc, (u_val, v_val, w_val) = CANONICAL_CENTERS[code]
        regime = "Interior" if res.is_interior else "Exterior (F - A)"
        ratio_str = (
            f"({res.ratio_af_fb}) · ({res.ratio_bd_dc}) · ({res.ratio_ce_ea}) "
            f"= {res.ceva_product}"
        )
        table.add_row(
            code,
            f"{u_val} : {v_val} : {w_val}",
            f"({res.center.x}, {res.center.y})",
            ratio_str,
            regime,
        )
    console.print(table)

    spread_res = verify_spread_ceva()
    pent_res = verify_odd_polygon_ceva()
    tet_res = solve_tetrahedron_static_equilibrium()
    app_res = verify_appendix_invariants()

    console.print(
        f"• [bold]Spread Ceva Product[/bold] (X(1) on Δ(13,14,15)): "
        f"s_prod = [green]{spread_res.spread_product}[/green], "
        f"Q_prod = [green]{spread_res.quadrance_product}[/green]"
    )
    console.print(
        f"• [bold]Pentagonal Ceva Product[/bold] (Lib. II odd 5-gon): "
        f"cyclic product = [green]{pent_res.cyclic_product}[/green]"
    )
    o_coords = tuple(tet_res.center_of_gravity)
    console.print(
        f"• [bold]3D Tetrahedron 7-Line Equilibrium[/bold] (Lib. I Prop. XXIII): "
        f"O = [green]{o_coords}[/green] (all 7 spatial lines concurrent)"
    )
    console.print(
        f"• [bold]Appendix Geometrica[/bold]: "
        f"Lune - Δ = [green]{app_res['lune_minus_triangle_residual']}[/green], "
        f"Ungula/Prism = [green]{app_res['ungula_to_prism_ratio']}[/green], "
        f"Hemisphere CG = [green]{app_res['hemisphere_vertex_to_base_ratio']}[/green], "
        f"Paraboloid CG = [green]{app_res['paraboloid_vertex_to_base_ratio']}[/green]"
    )


if __name__ == "__main__":
    main()
