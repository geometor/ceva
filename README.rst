=============
geometor-ceva
=============

Scholarly **Four-Track Bilingual Book Codex** (`English`, `Latin`, `Summary`, `Notes`) and **100% Exact Symbolic Geometry Engine** for **Giovanni Ceva's (1647–1734)** landmark treatise *De lineis rectis se invicem secantibus statica constructio* (*Mediolani: Ex Typographia Ludovici Montiae, 1678*) in the **GEOMETOR** Digital Scriptorium:

1. ***Liber Primus* — Static Foundations, Signed Weights (`F - A`), Ceva, Menelaus & 3D Equilibrium (pp. 1–43)**: Replaces auxiliary Euclidean circles and parallels with :person:`Archimedes'` Law of the Lever ($u \cdot \overline{AF} = v \cdot \overline{FB}$), proves **Ceva's Concurrency Theorem** $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$ (*Elementum* II, *Prop.* VII) and **Menelaus's Transversal Theorem** (*Elementum* I, *Prop.* VIII), introduces **algebraic negative weights** (`F - A`, *Elementum* III & p. 5 *Scholium*) 149 years before Möbius (1827), preserves **Pietro Paolo Caravaggio Jr.'s** pure Euclidean parallel-line proof (*Prop.* VI), and proves **3D skew-quadrilateral** (*Elementum* V *Coroll.*) and **tetrahedral 7-line concurrency** (*Prop.* XXIII, *"mira quadam concordia"*).
2. ***Liber Secundus* — Circumscribed Conics, Gergonne $X(7)$, Isotomic Conjugates & Odd Polygons (pp. 45–72)**: Applies Borelli–Serenus cylindrical projection (*Lemma* I) from circles to arbitrary ellipses, proves the concurrency of incircle/inellipse contact cevians (*Prop.* I, $X(7)$) and its **isotomic conjugate** (*Prop.* I *Corollarium*, $X(8)$), and generalizes cevian concurrency to **odd $(2m + 1)$-gons**.
3. ***Appendix Geometrica* — Synthetic Area Ratios, Cylindrical *Ungula*, Centroids & Indivisibles Caution (pp. 73–104)**: Demonstrates ratio concurrency purely by Euclidean sub-triangle areas ($[\triangle PAB]/[\triangle PAC] = BD/DC$), squares Hippocratean lunes (*Prop.* II), cubes the cylindrical *ungula* as $\frac{2}{3}$ of its circumscribed prism (*Prop.* VII), establishes the $5 : 3$ hemisphere centroid (*Prop.* XIII, praising Luca Valerio) and $2 : 1$ paraboloid centroid (*Prop.* XIV, citing Torricelli), and warns against naive parallel **indivisibles** on curved surfaces without conical-frustum slant correction.

Architecture
------------

* ``src/geometor/ceva/`` — Pure exact symbolic ``SymPy`` + ``geometor.model`` modules (``auto_intersect=False``, ``@proposition`` proofs, Rational Trigonometry quadrance & spread invariants, zero floating-point coordinates):

  * ``static_barycentrics.py`` — Exact signed static-barycentric solver ``solve_static_barycentrics``, Heronian $(13, 14, 15)$ rational center evaluator ($X(1), X(2), X(4), X(6), X(7), X(8), J_A$), universal polynomial identity prover, ``@proposition`` models for interior/exterior concurrency, isotomic conjugation, and harmonic division $(B, C; D, D') = -1$, and ``verify_spread_ceva``.
  * ``polygon_tetrahedron.py`` — Odd $(2m + 1)$-gon Ceva verifier and ``@proposition("Ceva.LibII.Pentagon")`` constructor, symbolic Borelli–Serenus circumscribed ellipse prover, 3D skew-quadrilateral and 7-line tetrahedral static equilibrium solvers, and *Appendix Geometrica* quadrature/cubature/centroid verifiers.

* ``docsrc/de_lineis_rectis/`` — Four-unit, four-track ``:layout: book`` codex (``-en.rst``, ``-la.rst``, ``-summary.rst``, ``-notes.rst``) wired to **8** interactive ``.euclid-graphic`` SVG figures in ``docsrc/_static/figures/`` and scholarly apparatus registries in ``resources/`` (26 persons, 18 citations, 16 glossary entries, 11 cross-corpus concordances).

Provenance & Licensing
----------------------

All Neo-Latin source texts derive strictly from the Public Domain 1678 Milan *editio princeps* (BNCF Florence exemplar ``ita-bnc-mag-00001346-001``). Every English translation, executive summary, SVG figure, and commentary note is **100% originally authored for GEOMETOR** without consulting or reproducing copyrighted translations.

Verification & Build
--------------------

.. code-block:: bash

   /home/phi/.local/bin/ruff check src scripts demos tests
   /home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v
   /home/phi/PROJECTS/geometor/.venv/bin/python scripts/build_figures.py
   /home/phi/.local/bin/publish build
