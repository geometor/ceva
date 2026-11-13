# GEOMETOR · Ceva (`geometor-ceva`)

Four-Unit Bilingual Book Codex (`:layout: book`) and 100% exact symbolic `SymPy` + `geometor.model` constructive engine for **Giovanni Ceva (1647–1734)**, *De lineis rectis se invicem secantibus statica constructio* (Milan: Ludovico Monza, 1678; BNCF Florence `ita-bnc-mag-00001346-001`, `Printed page N = PDF page N + 17`).

## Key Modules & Layout

- `src/geometor/ceva/static_barycentrics.py`: Exact signed static-barycentric solver (`solve_static_barycentrics`), canonical rational triangle centers on Heronian $\triangle(13, 14, 15)$ (`X(1), X(2), X(4), X(6), X(7), X(8), J_A`), universal symbolic prover, `@proposition` constructions for interior/exterior concurrency (`F - A`), isotomic conjugation (`X(7) <-> X(8)`), Menelaus harmonic division `(B, C; D, D') = -1`, and radical-free `verify_spread_ceva`.
- `src/geometor/ceva/polygon_tetrahedron.py`: Odd `(2m + 1)`-gon Ceva verifier & `@proposition("Ceva.LibII.Pentagon")`, Borelli–Serenus circumscribed circle/ellipse contact-ratio prover (*Liber Secundus, Lemma I*), 3D skew-quadrilateral (*Elementum V Coroll.*) & 7-line tetrahedral equilibrium solvers (*Liber Primus, Prop. XXIII*), and *Appendix Geometrica* quadrature/cubature/centroid verifiers.
- `src/geometor/ceva/sphinx_ext.py`: Offline-safe local `intersphinx_mapping` across sister GEOMETOR repositories.
- `scripts/build_figures.py`: Generates all **8** theme-adaptive `.euclid-graphic` SVG plates into `docsrc/_static/figures/`.
- `docsrc/de_lineis_rectis/`: 4-unit, 4-track (`-en.rst`, `-la.rst`, `-summary.rst`, `-notes.rst`) Book Codex with zero embedded `py_file` directives inside historical tracks (executable demos reside in `demos/` and `docsrc/demos/index.rst`).

## Architectural Invariants

1. **100% Exact Symbolic Coordinates**: Never inject `float` or `sp.Float` into `Model`; always construct with `Model(..., auto_intersect=False)` and explicit `model.intersect(...)`.
2. **Strict `.. picture::` Options**: Pass only `:alt:` on `.. picture::` (never `:width:`, `:align:`, or indented caption lines).
3. **100% Public-Domain Latin & Original English**: Transcribed from the 1678 Milan *editio princeps* with 100% original GEOMETOR English translation; keep `resources/{persons,citations,glossary}.json` and `resources/de_lineis_rectis/{persons,citations,glossary}.json` byte-identical.
4. **Clean Git Tree**: Never commit `.pdf` files, PNG/JPG scans, `docs/`, or `docsrc/modules/api/`.

## Offline Sandbox Verification Commands

```bash
/home/phi/.local/bin/ruff check src scripts demos tests
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v
/home/phi/PROJECTS/geometor/.venv/bin/python scripts/build_figures.py
/home/phi/.local/bin/publish build
```
