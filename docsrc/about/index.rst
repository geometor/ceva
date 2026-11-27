:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _ceva-about:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor-ceva`` establishes the authoritative Digital Scriptorium critical edition and exact symbolic engine for **Giovanni Ceva's** (1647–1734) landmark quarto treatise, :cite:`*De lineis rectis se invicem secantibus statica constructio* (Milan, 1678) <ceva:1678:dlr>`. Dedicated to Ferdinando Carlo Gonzaga, Duke of Mantua, this revolutionary work introduced the static barycentric method to mathematics—resolving the concurrency and collinearity properties of intersecting straight lines by substituting fictitious gravitational weights in place of lines and invoking Archimedes' Law of the Lever (:math:`u \cdot \overline{AF} = v \cdot \overline{FB}`), while introducing algebraic negative weights (:math:`F - A`) nearly a century and a half before August Ferdinand Möbius.

The edition reconstructs the complete 1678 treatise across four synchronized units: *Liber Primus* (establishing Menelaus's transversal theorem, Ceva's concurrency theorem :math:`\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1`, Caravaggio's Euclidean parallel-line proof, 3D skew quadrilaterals, and 7-line tetrahedral concurrency), *Liber Secundus* (conic contact-ratio invariance, the contact cevian concurrency anticipating Gergonne :math:`X(7)` and its isotomic conjugate anticipating Nagel :math:`X(8)`, and generalization to arbitrary odd :math:`(2m + 1)`-gons), and the *Appendix Geometrica* (pure geometric area-ratio foundations, cubature of the cylindrical *ungula*, hemisphere and paraboloid centroids, and Ceva's famous foundational critique of Cavalieri's method of indivisibles).

Within the **GEOMETOR** canon, ``geometor-ceva`` forms the primary bridge uniting classical Archimedean statics (``geometor/archimedes``) with classical Greek transversal lemmas (``geometor/menelaus``, ``geometor/pappus``), homogeneous barycentric coordinates in ``geometor/etc``, and modern radical-free Rational Trigonometry (``geometor/wildberger``), establishing the computational foundation for cevian concurrency and harmonic division across all geometries.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, founded by **phi ARCHITECT**, is dedicated to a three-fold synthesis of classical geometry, exact symbolic computation, and modern knowledge architecture:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and static OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. We elevate running prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs where every enunciation, proof step, and historical cross-reference is individually referenceable.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (via ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than lossy floating-point approximations. Every geometric theorem is treated as an exact algebraic truth verifiable through computational modeling.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

Public-Domain Textual Provenance & Copyright Audit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All primary Latin texts in this repository are transcribed directly from the 100% Public Domain 1678 Milan quarto *editio princeps*:

* **Giovanni Ceva (1678)**: *De lineis rectis se invicem secantibus statica constructio. Ad Serenissimum Ferdinandum Carolum Ducem Mantuae, Montisferrati, Guastallae, &c. Auctore Ioanne Ceva Mediolanensi. Mediolani: Ex Typographia Ludovici Montiae, MDCLXXVIII. Superiorum Permissu.* (Biblioteca Nazionale Centrale di Firenze exemplar `ita-bnc-mag-00001346-001`; `[16] + 104` printed pages and `10` folding copperplates containing `Figs. 1–85`, with `Printed page N = PDF scan page N + 17`).

Every English translation (`-en`), executive summary (`-summary`), interactive SVG diagram, and historical-mathematical commentary (`-notes`) in this codex is **100% originally translated and authored for GEOMETOR** directly from Ceva's 1678 Latin. No modern copyrighted translations or sourcebook excerpts were consulted or reproduced.

Typographic Conventions of the 1678 Milan Imprint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In his prefatory *Typographus Lectori* note, Milanese printer :person:`Ludovico Monza <monza>` informs the reader that his shop lacked sufficient cast sorts of the Greek cross `+` and therefore employed the typographic dagger/obelus ``†`` to denote algebraic addition of weights (e.g., ``A † F`` for :math:`A + F` concentrated at an interior fulcrum), paired with the analytic minus sign ``-`` (``F - A`` for :math:`F - A`, *Liber Primus* p. 5 *Scholium*) when balancing an exterior fulcrum. Our Latin track preserves Ceva's authentic notation alongside clear editorial explanation.

Position in the GEOMETOR Canon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``geometor-ceva`` bridges classical Greek synthetic geometry and modern projective, barycentric, and rational-trigonometric architecture across the GEOMETOR workspace:

* **Archimedean Statics to Barycentric Coordinates**: Connects ``geometor/archimedes`` (*Equiponderants* I.6–7) directly to homogeneous barycentric coordinates in ``geometor/etc`` (:math:`X(1), X(2), X(4), X(6), X(7), X(8)`) and :person:`Möbius's <moebius>` *Der barycentrische Calcul* (1827).
* **Projective Dualism & Harmonic Ranges**: Unites Ceva's concurrency theorem with ``geometor/menelaus`` and ``geometor/pappus`` through the harmonic cross-ratio :math:`(B, C; D, D') = -1` verified via ``geometor.model.is_harmonic``.
* **Radical-Free Rational Trigonometry**: Extends Ceva's theorem to ``geometor/wildberger`` via **Spread Ceva's Theorem**, verified over :math:`\mathbb{Q}` on the Heronian :math:`(13, 14, 15)` triangle without a single square root.

Scholarly Apparatus & References:

* :doc:`Reader's Guide and Usage </usage/index>`
* :doc:`De Lineis Rectis Codex </de_lineis_rectis/index>`
* :doc:`Exact Symbolic Demonstrations </demos/index>`
* :doc:`Biographical Register of Persons </de_lineis_rectis/people/index>`
* :doc:`Systematic Bibliography </de_lineis_rectis/bibliography>`
