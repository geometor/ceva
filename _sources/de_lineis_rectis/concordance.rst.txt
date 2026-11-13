.. _ceva-concordance:

Cross-Corpus Geometric Concordance
==================================

Bidirectional concordance mapping propositions and static constructions in :person:`Giovanni Ceva's <ceva>` *De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan, 1678 <ceva:1678:dlr>`) to sister repositories across the **GEOMETOR** canon and exact symbolic verifiers in ``geometor.ceva``.

.. list-table:: Ceva 1678 Cross-Corpus Concordance
   :header-rows: 1
   :widths: 22 30 22 26

   * - Ceva 1678 Locus
     - Geometric / Static Proposition
     - Sister GEOMETOR Canon
     - Symbolic Verifier (``geometor.ceva``)
   * - *Lib. I*, *Axiomata* I–II & *Lemmata* I–II (pp. 1–2; `Tab. 1, Figs. 1–3`)
     - Uniqueness of :term:`centrum gravitatis <centrum-gravitatis>` & Archimedes' Lever Law ($u \cdot \overline{AF} = v \cdot \overline{FB}$)
     - ``archimedes`` *Equipond.* I.4–7; ``euclid`` V–VI
     - ``static_barycentrics.solve_static_barycentrics``
   * - *Lib. I*, *Elementum* I & *Prop.* VIII (pp. 2–3, 10–12; `Tab. 1, Figs. 4, 12`)
     - Static proof of :person:`Menelaus's <menelaus>` Transversal Theorem & :term:`harmonic range <sectio-harmonica>` $(B, C; D, D') = -1$
     - ``menelaus`` III.1; ``ptolemy`` I.13; ``pappus`` VII
     - ``static_barycentrics.construct_cevian_menelaus_harmonic``
   * - *Lib. I*, *Elementum* II & *Prop.* VII (pp. 3–4, 8–10; `Tab. 1, Figs. 5, 11`)
     - Interior cevian concurrency $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$ at $P = \frac{uA+vB+wC}{u+v+w}$
     - ``etc`` $X(1), X(2), X(4), X(6)$; ``altshiller-court``
     - ``static_barycentrics.construct_ceva_concurrency``
   * - *Lib. I*, *Elementum* III & p. 5 *Scholium* (`Tab. 1, Fig. 6`)
     - Analytic negative weight :term:`F - A <pondus-negativum>` for exterior concurrency (excenter $J_A$)
     - ``etc`` excenters; :person:`Möbius <moebius>` (1827)
     - ``static_barycentrics.evaluate_canonical_centers``
   * - *Lib. I*, *Elementa* IV–V *Coroll.* (pp. 5–7; `Tab. 1, Figs. 7–8`)
     - Planar & :term:`3D skew quadrilateral <quadrilaterum-non-planum>` (*"non in eodem plano"*) fulcrum coplanarity & concurrency
     - ``elements`` XI; ``pappus``
     - ``polygon_tetrahedron.verify_skew_quadrilateral_ceva``
   * - *Lib. I*, *Prop.* VI (pp. 7–8; `Tab. 1, Fig. 10`)
     - Pure Euclidean parallel-line proof credited to :person:`Pietro Paolo Caravaggio Jr. <caravaggio>`
     - ``euclid`` / ``elements`` I.29, VI.2, VI.4
     - ``static_barycentrics.prove_ceva_barycentric_identity``
   * - *Lib. I*, *Props.* IX–XXII (pp. 12–35) & Rational Trigonometry
     - Medians $X(2)$, altitudes $X(4)$, bisectors $X(1)$, symmedians $X(6)$, & radical-free :term:`Spread Ceva <spread-ceva>`
     - ``etc``; ``wildberger`` *Divine Proportions*
     - ``static_barycentrics.verify_spread_ceva``
   * - *Lib. I*, *Props.* XXIII–XXVI (pp. 36–43; `Tab. 3, Figs. 28–31`)
     - :term:`3D Tetrahedron 7-Line Equilibrium <concordia-septem-linearum>` (*"mira quadam concordia"* at $O$)
     - ``archimedes``; ``elements`` XII
     - ``polygon_tetrahedron.solve_tetrahedron_static_equilibrium``
   * - *Lib. II*, *Lemma* I & *Prop.* I + *Coroll.* (pp. 45–50; `Tab. 4, Figs. 32–37`)
     - :term:`Cylindrical ellipse projection <sectio-cylindrica>`, :term:`Gergonne X(7) <punctum-contactus>` & :term:`Isotomic Nagel X(8) <coniugatum-isotomicum>`
     - ``apollonius``; ``etc`` $X(7), X(8)$; ``casey``
     - ``static_barycentrics.construct_isotomic_conjugate``
   * - *Lib. II*, *Props.* II–XIV (pp. 50–72; `Tab. 4–7, Figs. 38–61`)
     - Odd $(2m + 1)$-gon multilateral Ceva concurrency ($\prod_{i=0}^{2m} r_i = 1$)
     - ``pappus``; ``altshiller-court``
     - ``polygon_tetrahedron.construct_pentagon_ceva``
   * - *Appendix Geometrica*, *Props.* I–XVI & Closing Scholium (pp. 73–104; `Tab. 8–10`)
     - Synthetic area ratios ($[\triangle PAB]/[\triangle PAC] = BD/DC$), Lune, :term:`Ungula <ungula-cylindrica>` $= \frac{2}{3}$ prism, $5:3$ & $2:1$ centroids, & :term:`Indivisibles Caution <indivisibilia-cautio>`
     - ``euclid`` VI.1, XII.2; ``archimedes``; ``hoenen``
     - ``polygon_tetrahedron.verify_appendix_invariants``
