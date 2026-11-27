:navigation: header
:order: 14
:nav_title: Concordance

.. _ceva-concordance:

Cross-Corpus Geometric Concordance
==================================

Bidirectional concordance mapping every landmark proposition in :person:`Giovanni Ceva's <ceva>` *De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan, 1678 <ceva:1678:dlr>`, verified against BNCF Florence scans ``0001``–``0126``) to atomic Book Codex leaves, sister **GEOMETOR** repositories, and exact symbolic verifiers in ``geometor.ceva``.

.. list-table:: Ceva 1678 Folio-Verified Cross-Corpus Concordance
   :header-rows: 1
   :widths: 24 30 22 24

   * - Ceva 1678 Locus (Folio / Page)
     - Geometric / Static Proposition
     - Sister GEOMETOR Canon
     - Symbolic Verifier (``geometor.ceva``)
   * - :ref:`Lib. I, Axioms & Lemmas I–II <liber-primus-axiomata-lemmata>` (pp. 1–2; ``0018``–``0019``; `Tab. 1, Figs. 1–3`)
     - Uniqueness of :term:`centrum gravitatis <centrum-gravitatis>` & Archimedes' Lever Law (:math:`u \cdot \overline{AF} = v \cdot \overline{FB}`)
     - ``archimedes`` *Equipond.* I.6; ``euclid`` V–VI
     - ``static_barycentrics.solve_static_barycentrics``
   * - :ref:`Lib. I, Prop. I (Elem. I) <liber-primus-prop-01>` & :ref:`Prop. VI <liber-primus-prop-06>` (pp. 2–3, 7–10; ``0019``–``0027``; `Tab. 1, Figs. 4, 10`)
     - Static :person:`Menelaus <menelaus>` sector & :person:`Caravaggio Jr.'s <caravaggio>` pure parallel-line proof (p. 10)
     - ``menelaus`` III.1; ``ptolemy`` I.13; ``pappus`` VII
     - ``static_barycentrics.construct_cevian_menelaus_harmonic``
   * - :ref:`Lib. I, Prop. II (Elem. II) <liber-primus-prop-02>` & :ref:`Prop. X <liber-primus-prop-10>` (pp. 3–4, 15–17; ``0020``–``0034``; `Tab. 1, Fig. 5`)
     - **Ceva's Theorem** :math:`\frac{AD}{DE}\cdot\frac{EK}{KC}\cdot\frac{CB}{BA} = 1` & Caravaggio Jr.'s second proof (p. 15)
     - ``etc`` :math:`X(1), X(2), X(4), X(6)`; ``altshiller-court``
     - ``static_barycentrics.construct_ceva_concurrency``
   * - :ref:`Lib. I, Prop. III–IV <liber-primus-prop-03>` (pp. 4–5; ``0021``–``0022``; `Tab. 1, Figs. 6–7`)
     - Analytic negative weight :term:`F - A <pondus-negativum>` & addition sign :term:`✠ <obelus-additio>` (p. 5 Scholia)
     - ``etc`` excenters; :person:`Möbius <moebius>` (1827)
     - ``static_barycentrics.evaluate_canonical_centers``
   * - :ref:`Lib. I, Prop. V (Elem. V) <liber-primus-prop-05>` & :ref:`Prop. XXII <liber-primus-prop-22>` (pp. 6–7, 30–31; ``0023``–``0048``; `Tab. 1, Fig. 8`)
     - Planar & :term:`3D skew quadrilateral <quadrilaterum-non-planum>` (*"non in eodem plano"*) fulcrum coplanarity
     - ``elements`` XI; ``pappus``
     - ``polygon_tetrahedron.verify_skew_quadrilateral_ceva``
   * - :ref:`Lib. I, Prop. XXI <liber-primus-prop-21>` (p. 30; ``0047``; `Tab. 2, Fig. 24`)
     - Harmonic division along interior cevian :math:`KL : LA = 2G : (I+H)` & :term:`Spread Ceva <spread-ceva>`
     - ``wildberger`` *Divine Proportions*; ``pappus``
     - ``static_barycentrics.verify_spread_ceva``
   * - :ref:`Lib. I, Props. XXIII–XXVI <liber-primus-prop-23>` (pp. 31–34; ``0048``–``0051``; `Tab. 3, Figs. 28–31`)
     - :term:`3D Tetrahedron 7-Line Equilibrium <concordia-septem-linearum>` (*"mira quadam concordia"*), pyramids & frustum
     - ``archimedes``; ``elements`` XII; :person:`Commandino <commandino>`
     - ``polygon_tetrahedron.solve_tetrahedron_static_equilibrium``
   * - :ref:`Lib. II, Lemmas I–III <liber-secundus-lemmata-conica>` & :ref:`Prop. I <liber-secundus-prop-01>` (pp. 35–38; ``0052``–``0055``; `Tab. 4, Figs. 32–38`)
     - :term:`Cylindrical ellipse projection <sectio-cylindrica>`, Gergonne :math:`X(7)`, & **Converse of Ceva's Theorem** (p. 38)
     - ``apollonius``; ``serenus``; ``etc`` :math:`X(7), X(8)`
     - ``polygon_tetrahedron.prove_circumscribed_polygon_lemma``
   * - :ref:`Lib. II, Props. IX–XVI <liber-secundus-prop-09>` (pp. 44–52; ``0061``–``0069``; `Tab. 5–7, Figs. 44–61`)
     - Inscribed ellipses, 3-tangent parabola concurrency & cubic area law, Incenter `Tab. 7, Fig. 57`
     - ``apollonius`` III.41; ``euclid`` VI.3; ``etc`` :math:`X(1)`
     - ``static_barycentrics.construct_isotomic_conjugate``
   * - :ref:`Lib. II, Props. XIX–XXI <liber-secundus-prop-21>` (pp. 54–60; ``0071``–``0077``; `Tab. 8 & 10, Figs. 63–67, 85`)
     - Reciprocally inscribed triangles & single-station optical distance rangefinder (`Fig. 85`)
     - ``pappus``; ``altshiller-court``
     - ``polygon_tetrahedron.construct_pentagon_ceva``
   * - :ref:`Appendix, Props. I–XVI & Scholium <appendix-geometrica-prop-04>` (pp. 61–83; ``0078``–``0100``; `Tab. 8–10, Figs. 68–84`)
     - Hippocrates' Lunes, :term:`Ungula <ungula-cylindrica>` :math:`= \frac{2}{3}` prism, :math:`5:3` & :math:`2:1` centroids, Torricelli infinite solid, :term:`Indivisibles Caution <indivisibilia-cautio>` & p. 83 Printer's Note on ``✠``
     - ``euclid`` XII.2; ``archimedes``; ``hoenen``
     - ``polygon_tetrahedron.verify_appendix_invariants``
