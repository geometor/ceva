r"""Comprehensive test suite for ``geometor.ceva`` symbolic kernel, SVGs, and Book Codex."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
from geometor.model import Model, cross_ratio, is_harmonic, zero_test

from geometor.ceva import (
    CANONICAL_CENTERS,
    HERONIAN_VERTICES,
    RATIONAL_PENTAGON,
    RATIONAL_TETRAHEDRON,
    __version__,
    construct_ceva_concurrency,
    construct_cevian_menelaus_harmonic,
    construct_isotomic_conjugate,
    construct_pentagon_ceva,
    directed_ratio_collinear,
    evaluate_canonical_centers,
    prove_ceva_barycentric_identity,
    prove_circumscribed_polygon_lemma,
    solve_static_barycentrics,
    solve_tetrahedron_static_equilibrium,
    verify_appendix_invariants,
    verify_odd_polygon_ceva,
    verify_skew_quadrilateral_ceva,
    verify_spread_ceva,
)
from geometor.ceva.__main__ import main as cli_main

REPO_ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = REPO_ROOT / "docsrc" / "_static" / "figures"
CODEX_DIR = REPO_ROOT / "docsrc" / "de_lineis_rectis"

EXPECTED_SVGS: tuple[str, ...] = (
    "fig01_statica_lever_elements.svg",
    "fig02_ceva_interior_exterior.svg",
    "fig03_menelaus_harmonic_quadrangle.svg",
    "fig04_isotomic_gergonne_nagel.svg",
    "fig05_spread_ceva_heronian.svg",
    "fig06_pentagon_multilateral_ceva.svg",
    "fig07_tetrahedron_seven_lines.svg",
    "fig08_appendix_ungula_indivisibles.svg",
)

EXPECTED_UNITS: tuple[str, ...] = (
    "unit-1-statica-foundations",
    "unit-2-liber-primus-ceva-menelaus",
    "unit-3-liber-secundus-polygons-solids",
    "unit-4-appendix-geometrica",
)


def _assert_no_floats_in_model(model: Model) -> None:
    """Assert that a ``geometor.model.Model`` contains zero ``sp.Float`` atoms."""
    assert model.auto_intersect is False
    for elem in model:
        if isinstance(elem, sp.Basic):
            assert not elem.has(sp.Float), f"sp.Float detected in Model element: {elem!r}"


def test_version_and_cli(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify package version and Rich CLI summary output."""
    assert __version__ == "0.1.0"
    cli_main()
    captured = capsys.readouterr().out
    assert "GEOMETOR" in captured
    assert "Spread Ceva Product" in captured


def test_static_barycentrics_canonical_centers() -> None:
    """Verify exact rational coordinates and zero residuals for all canonical centers."""
    centers = evaluate_canonical_centers()
    assert set(centers.keys()) == set(CANONICAL_CENTERS.keys())

    expected_coords = {
        "X(1)": (sp.Integer(6), sp.Integer(4)),
        "X(2)": (sp.Rational(19, 3), sp.Integer(4)),
        "X(4)": (sp.Integer(5), sp.Rational(15, 4)),
        "X(6)": (sp.Rational(1673, 295), sp.Rational(1176, 295)),
        "X(7)": (sp.Rational(414, 73), sp.Rational(288, 73)),
        "X(8)": (sp.Integer(7), sp.Integer(4)),
        "J_A": (sp.Integer(8), sp.Integer(-12)),
    }

    for code, res in centers.items():
        ex, ey = expected_coords[code]
        assert res.center.x == ex
        assert res.center.y == ey
        assert res.ceva_product == 1
        assert all(zero_test(r) for r in res.lever_residuals)
        assert all(zero_test(r) for r in res.area_ratio_residuals)
        assert not res.center.has(sp.Float)

    assert centers["X(1)"].is_interior is True
    assert centers["J_A"].is_interior is False

    # Verify Nagel-line relation X(8) - X(2) == 2 * (X(2) - X(1))
    assert centers["X(8)"].center.x - centers["X(2)"].center.x == 2 * (
        centers["X(2)"].center.x - centers["X(1)"].center.x
    )


def test_universal_symbolic_barycentric_identity() -> None:
    """Verify universal polynomial proof of Ceva's Theorem and sub-triangle area ratios."""
    residuals = prove_ceva_barycentric_identity()
    assert len(residuals) == 7
    for key, val in residuals.items():
        assert val == 0, f"Non-zero residual for {key}: {val}"


def test_static_barycentrics_validation_errors() -> None:
    """Verify strict rejection of floats, zero weights, collinear vertices, and parallel sums."""
    with pytest.raises(ValueError, match="Floating-point"):
        solve_static_barycentrics(1.5, 2, 3, HERONIAN_VERTICES)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="non-zero"):
        solve_static_barycentrics(0, 2, 3, HERONIAN_VERTICES)
    with pytest.raises(ValueError, match="Degenerate weight sum"):
        solve_static_barycentrics(2, 3, -3, HERONIAN_VERTICES)
    with pytest.raises(ValueError, match="collinear"):
        solve_static_barycentrics(1, 2, 3, ((0, 0), (2, 2), (5, 5)))
    with pytest.raises(ValueError, match="not collinear"):
        a_pt, b_pt, c_pt = solve_static_barycentrics(1, 1, 1).vertices
        directed_ratio_collinear(a_pt, b_pt, c_pt)


def test_constructive_proposition_models_and_zero_floats() -> None:
    """Verify interior, exterior, isotomic, harmonic, and pentagonal Model constructions."""
    m_int = construct_ceva_concurrency(24, 28, 21)
    m_ext = construct_ceva_concurrency(-14, 15, 13)
    m_iso = construct_isotomic_conjugate(24, 28, 21)
    m_har = construct_cevian_menelaus_harmonic(24, 28, 21)
    m_pent = construct_pentagon_ceva(RATIONAL_PENTAGON, (4, 4))

    for model in (m_int, m_ext, m_iso, m_har, m_pent):
        _assert_no_floats_in_model(model)

    p_iso = m_iso.get_element_by_ID("P_iso")
    assert (p_iso.x, p_iso.y) == (sp.Integer(7), sp.Integer(4))

    b_pt = m_har.get_element_by_ID("B")
    c_pt = m_har.get_element_by_ID("C")
    d_pt = m_har.get_element_by_ID("D")
    dp_pt = m_har.get_element_by_ID("D_prime")
    assert cross_ratio(b_pt, c_pt, d_pt, dp_pt) == -1
    assert is_harmonic(b_pt, c_pt, d_pt, dp_pt) is True


def test_spread_ceva_rational_trigonometry() -> None:
    """Verify Spread Ceva's Theorem over Q without square roots."""
    res = verify_spread_ceva(14, 15, 13, HERONIAN_VERTICES)
    assert res.spread_product == 1
    assert res.quadrance_product == 1
    for s_val in (
        res.spread_bad,
        res.spread_dac,
        res.spread_cbe,
        res.spread_eba,
        res.spread_acf,
        res.spread_fcb,
    ):
        assert isinstance(s_val, sp.Rational)
        assert not s_val.has(sp.Pow)


def test_odd_polygons_conics_tetrahedron_and_appendix() -> None:
    """Verify multilateral odd polygons, circumscribed ellipse Lemma I, 3D statics, and Appendix."""
    pent = verify_odd_polygon_ceva(RATIONAL_PENTAGON, (4, 4))
    assert pent.n_sides == 5
    assert pent.cyclic_product == 1

    # Also test a convex rational heptagon (n = 7)
    heptagon = ((0, 0), (6, 0), (10, 3), (11, 8), (7, 12), (1, 11), (-2, 5))
    hept = verify_odd_polygon_ceva(heptagon, (4, 5))
    assert hept.n_sides == 7
    assert hept.cyclic_product == 1

    with pytest.raises(ValueError, match="odd n >= 3"):
        verify_odd_polygon_ceva(((0, 0), (4, 0), (4, 4), (0, 4)), (2, 1))

    lemma = prove_circumscribed_polygon_lemma(6)
    assert all(v == 0 for v in lemma.values())

    tet = solve_tetrahedron_static_equilibrium((2, 3, 5, 8), RATIONAL_TETRAHEDRON)
    assert tet.concurrency_residuals_zero is True
    assert len(tet.edge_fulcrums) == 6
    assert len(tet.face_centers) == 4
    assert len(tet.vertex_cevian_ratios) == 4
    assert len(tet.bimedian_ratios) == 3

    skew = verify_skew_quadrilateral_ceva((2, 3, 5, 7), RATIONAL_TETRAHEDRON)
    assert skew.cyclic_ratio_product == 1
    assert skew.fulcrum_coplanarity_det == 0
    assert skew.tetrahedron_det6 != 0

    app = verify_appendix_invariants()
    assert app["lune_minus_triangle_residual"] == 0
    assert app["ungula_to_prism_ratio"] == sp.Rational(2, 3)
    assert app["hemisphere_vertex_to_base_ratio"] == sp.Rational(5, 3)
    assert app["paraboloid_vertex_to_base_ratio"] == 2


def test_euclid_graphic_svgs_valid_xml() -> None:
    """Verify all 8 .euclid-graphic SVG plates exist and obey XML & layer contracts."""
    svg_ns = "{http://www.w3.org/2000/svg}"
    for fname in EXPECTED_SVGS:
        svg_path = FIGURES_DIR / fname
        assert svg_path.is_file(), f"Missing SVG figure: {svg_path}"
        root = ET.parse(svg_path).getroot()
        assert root.tag == f"{svg_ns}svg"
        assert "euclid-graphic" in root.attrib.get("class", "")
        layer_ids = [el.attrib.get("id") for el in root.findall(f"{svg_ns}g")]
        assert layer_ids == ["elements", "graphics", "highlights", "points", "labels"]
        refs = [el.attrib["data-ref"] for el in root.iter() if "data-ref" in el.attrib]
        assert len(refs) >= 5, f"Expected data-ref wiring in {fname}"


def test_codex_tracks_apparatus_and_picture_directives() -> None:
    """Verify all 16 codex track RSTs, byte-identical JSON registries, and strict .. picture:: options."""
    for unit in EXPECTED_UNITS:
        for suffix in ("en", "la", "summary", "notes"):
            track_file = CODEX_DIR / unit / f"{unit}-{suffix}.rst"
            assert track_file.is_file(), f"Missing codex track: {track_file}"
            text = track_file.read_text(encoding="utf-8")
            assert len(text.strip()) > 400
            assert ".. py_file::" not in text

    for json_name in ("persons.json", "citations.json", "glossary.json"):
        root_json = (REPO_ROOT / "resources" / json_name).read_text(encoding="utf-8")
        book_json = (REPO_ROOT / "resources" / "de_lineis_rectis" / json_name).read_text(
            encoding="utf-8"
        )
        assert root_json == book_json, f"Apparatus JSON mismatch for {json_name}"
        parsed = json.loads(root_json)
        assert len(parsed) >= 15

    # Ensure zero :width: or :align: options or indented captions under .. picture::
    for rst_path in (REPO_ROOT / "docsrc").rglob("*.rst"):
        if "modules/api" in rst_path.as_posix():
            continue
        lines = rst_path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            if line.strip().startswith(".. picture::"):
                j = idx + 1
                while j < len(lines) and (lines[j].startswith("   ") or not lines[j].strip()):
                    stripped = lines[j].strip()
                    if not stripped:
                        break
                    assert not stripped.startswith(":width:"), (
                        f"Forbidden :width: on .. picture:: in {rst_path}:{j + 1}"
                    )
                    assert not stripped.startswith(":align:"), (
                        f"Forbidden :align: on .. picture:: in {rst_path}:{j + 1}"
                    )
                    assert stripped.startswith(":"), (
                        f"Forbidden indented caption under .. picture:: in {rst_path}:{j + 1}"
                    )
                    j += 1
