:navigation: footer
:order: 10

.. _ceva-about:

About GEOMETOR Ceva
===================

Historical, philological, and symbolic-modeling provenance for ``geometor-ceva`` in the **GEOMETOR Digital Scriptorium**.

Public-Domain Textual Provenance & Copyright Audit
--------------------------------------------------

All primary Latin texts in this repository are transcribed directly from the 100% Public Domain 1678 Milan quarto *editio princeps*:

* **Giovanni Ceva (1678)**: *De lineis rectis se invicem secantibus statica constructio. Ad Serenissimum Ferdinandum Carolum Ducem Mantuae, Montisferrati, Guastallae, &c. Auctore Ioanne Ceva Mediolanensi. Mediolani: Ex Typographia Ludovici Montiae, MDCLXXVIII. Superiorum Permissu.* (Biblioteca Nazionale Centrale di Firenze exemplar `ita-bnc-mag-00001346-001`; `[16] + 104` printed pages and `10` folding copperplates containing `Figs. 1–85`, with `Printed page N = PDF scan page N + 17`).

Every English translation (`-en`), executive summary (`-summary`), interactive SVG diagram, and historical-mathematical commentary (`-notes`) in this codex is **100% originally translated and authored for GEOMETOR** directly from Ceva's 1678 Latin. No modern copyrighted translations or sourcebook excerpts were consulted or reproduced.

Typographic Conventions of the 1678 Milan Imprint
-------------------------------------------------

In his prefatory *Typographus Lectori* note, Milanese printer :person:`Ludovico Monza <monza>` informs the reader that his shop lacked sufficient cast sorts of the Greek cross `+` and therefore employed the typographic dagger/obelus ``†`` to denote algebraic addition of weights (e.g., ``A † F`` for $A + F$ concentrated at an interior fulcrum), paired with the analytic minus sign ``-`` (``F - A`` for $F - A$, *Liber Primus* p. 5 *Scholium*) when balancing an exterior fulcrum. Our Latin track preserves Ceva's authentic notation alongside clear editorial explanation.

Position in the GEOMETOR Canon
------------------------------

``geometor-ceva`` bridges classical Greek synthetic geometry and modern projective, barycentric, and rational-trigonometric architecture across the GEOMETOR workspace:

* **Archimedean Statics to Barycentric Coordinates**: Connects ``geometor/archimedes`` (*Equiponderants* I.6–7) directly to homogeneous barycentric coordinates in ``geometor/etc`` ($X(1), X(2), X(4), X(6), X(7), X(8)$) and :person:`Möbius's <moebius>` *Der barycentrische Calcul* (1827).
* **Projective Dualism & Harmonic Ranges**: Unites Ceva's concurrency theorem with ``geometor/menelaus`` and ``geometor/pappus`` through the harmonic cross-ratio $(B, C; D, D') = -1$ verified via ``geometor.model.is_harmonic``.
* **Radical-Free Rational Trigonometry**: Extends Ceva's theorem to ``geometor/wildberger`` via **Spread Ceva's Theorem**, verified over $\mathbb{Q}$ on the Heronian $(13, 14, 15)$ triangle without a single square root.
