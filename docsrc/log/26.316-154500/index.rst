:date: 26.316-154500
:author: phi ARCHITECT
:type: log
:categories: codex, symbolic-geometry, translation
:tags: ceva, barycentrics, menelaus, isotomic-conjugate, tetrahedron, indivisibles

=================================================================================================
Initial Bilingual Book Codex & Symbolic Engine of Ceva's De Lineis Rectis Statica Constructio
=================================================================================================

Established ``geometor-ceva`` (``v0.1.0``), uniting a four-unit, four-track bilingual Neo-Latin/English **Digital Scriptorium Book Codex** with 100% exact ``SymPy`` and ``geometor.model`` symbolic verifications for Giovanni Ceva's *De lineis rectis se invicem secantibus statica constructio* (Milan: Ludovico Monza, 1678).

Highlights
----------

- **Four-Unit 4-Track Bilingual Codex** (``docsrc/de_lineis_rectis/``): Folio-verified transcription and original English translation of the 1678 Milan first edition across *Liber Primus* (static foundations, negative algebraic weights ``F - A``, Caravaggio Jr.'s Prop. VI, Ceva & Menelaus concurrencies, 3D skew quadrilateral, and 7-line tetrahedral equilibrium), *Liber Secundus* (Borelli–Serenus cylindrical ellipse projection, Gergonne $X(7)$ & isotomic Nagel $X(8)$, and odd multilateral polygons), and *Appendix Geometrica* (synthetic area ratios, Hippocratean lune, cylindrical *ungula* $= \frac{2}{3}$ prism, hemisphere $5:3$ & paraboloid $2:1$ centroids, and Ceva's closing caution on Cavalieri's indivisibles), illustrated by **8** interactive ``.euclid-graphic`` SVG plates.
- **100% Exact Symbolic Kernel** (``src/geometor/ceva/``): Implemented ``solve_static_barycentrics``, canonical rational center evaluation on the Heronian $(13, 14, 15)$ triangle, ``@proposition`` models for interior/exterior concurrency, isotomic conjugation, harmonic division $(B, C; D, D') = -1$, **Spread Ceva's Theorem**, pentagonal concurrency, and 3D 7-line tetrahedral static equilibrium with zero floating-point coordinates.
