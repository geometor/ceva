#!/usr/bin/env python3
"""Exact symbolic demonstration of Ceva's static barycentrics, isotomic conjugates, and Spread Ceva."""

from __future__ import annotations

import sympy as sp
from geometor.model import cross_ratio, is_harmonic
from rich.console import Console
from rich.table import Table

from geometor.ceva import (
    CANONICAL_CENTERS,
    construct_ceva_concurrency,
    construct_cevian_menelaus_harmonic,
    construct_isotomic_conjugate,
    evaluate_canonical_centers,
    prove_ceva_barycentric_identity,
    verify_spread_ceva,
)


def run_demo() -> None:
    """Execute exact symbolic proofs for Liber Primus and canonical triangle centers."""
    console = Console()
    console.print(
        "[bold amber1]1. Universal Symbolic Proof of Ceva's Barycentric & Area Identities[/bold amber1]"
    )
    residuals = prove_ceva_barycentric_identity()
    for key, expr in residuals.items():
        assert expr == 0, f"Non-zero symbolic residual {key}: {expr}"
        console.print(f"  • {key}: [green]{expr}[/green]")

    console.print(
        "\n[bold amber1]2. Canonical Rational Centers on Heronian Δ(13, 14, 15)[/bold amber1]"
    )
    tbl = Table(show_lines=False)
    tbl.add_column("Center", style="bold cyan")
    tbl.add_column("Weights (u:v:w)", style="magenta")
    tbl.add_column("Exact P in Q^2", style="green")
    tbl.add_column("Signed Ratios (AF/FB, BD/DC, CE/EA)", style="yellow")
    tbl.add_column("Product")

    for code, res in evaluate_canonical_centers().items():
        _desc, (u_val, v_val, w_val) = CANONICAL_CENTERS[code]
        tbl.add_row(
            code,
            f"{u_val}:{v_val}:{w_val}",
            f"({res.center.x}, {res.center.y})",
            f"({res.ratio_af_fb}, {res.ratio_bd_dc}, {res.ratio_ce_ea})",
            str(res.ceva_product),
        )
    console.print(tbl)

    console.print(
        "\n[bold amber1]3. Constructive @proposition Models (Interior, Exterior F-A, Isotomic, Harmonic)[/bold amber1]"
    )
    m_int = construct_ceva_concurrency(24, 28, 21)
    m_ext = construct_ceva_concurrency(-14, 15, 13)
    m_iso = construct_isotomic_conjugate(24, 28, 21)
    m_har = construct_cevian_menelaus_harmonic(24, 28, 21)

    b_pt = m_har.get_element_by_ID("B")
    c_pt = m_har.get_element_by_ID("C")
    d_pt = m_har.get_element_by_ID("D")
    dp_pt = m_har.get_element_by_ID("D_prime")
    cr_val = cross_ratio(b_pt, c_pt, d_pt, dp_pt)
    assert is_harmonic(b_pt, c_pt, d_pt, dp_pt)

    console.print(f"  • Interior Gergonne X(7) Model elements: [green]{len(m_int)}[/green]")
    console.print(f"  • Exterior Excenter J_A (-14:15:13) elements: [green]{len(m_ext)}[/green]")
    console.print(f"  • Isotomic X(7) <-> X(8) Model elements: [green]{len(m_iso)}[/green]")
    console.print(
        f"  • Cevian–Menelaus Cross-Ratio (B, C; D, D'): [green]{sp.simplify(cr_val)}[/green]"
    )

    console.print(
        "\n[bold amber1]4. Rational Trigonometry Spread Ceva Theorem (Zero Radicals)[/bold amber1]"
    )
    spread = verify_spread_ceva()
    console.print(
        f"  • s(BAD)={spread.spread_bad}, s(DAC)={spread.spread_dac} | "
        f"s(CBE)={spread.spread_cbe}, s(EBA)={spread.spread_eba} | "
        f"s(ACF)={spread.spread_acf}, s(FCB)={spread.spread_fcb}"
    )
    console.print(
        f"  • Spread Product = [green]{spread.spread_product}[/green], "
        f"Quadrance Product = [green]{spread.quadrance_product}[/green]"
    )


if __name__ == "__main__":
    run_demo()
