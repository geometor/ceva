.. _unit-4-appendix-geometrica-summary:

Unit IV · Executive Geometric Summary
=====================================

Core Results of *Appendix Geometrica* (1678, pp. 73–104)
--------------------------------------------------------

1. **Barycentric Weights = Oriented Sub-Triangle Areas**: Eliminating physical mechanics via :just:`VI.1` and :just:`V.19`, Ceva proves that for any concurrency point $P = (u : v : w)$,

   $$[\triangle PBC] : [\triangle PCA] : [\triangle PAB] = u : v : w, \qquad \frac{[\triangle PAB]}{[\triangle PAC]} = \frac{\overline{BD}}{\overline{DC}},$$

   verified both symbolically over $\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u, v, w]$ (:func:`~geometor.ceva.static_barycentrics.prove_ceva_barycentric_identity`) and rationally for every canonical center (:func:`~geometor.ceva.static_barycentrics.solve_static_barycentrics`).
2. **Exact Quadratures, Cubatures & Solid Centroids** (:func:`~geometor.ceva.polygon_tetrahedron.verify_appendix_invariants`):

.. list-table:: Verified *Appendix Geometrica* Invariants (``geometor.ceva.polygon_tetrahedron``)
   :header-rows: 1
   :widths: 22 30 24 24

   * - 1678 Locus
     - Geometric Object
     - Exact Symbolic Value
     - Classical / Modern Link
   * - *Appendix Prop.* II
     - Hippocratean Lune on isosceles right $\triangle$
     - $[\text{Lune}] = \frac{1}{2} R^2 = [\triangle ABC]$
     - Hippocrates of Chios / Euclid XII.2
   * - *Appendix Prop.* VII
     - Cylindrical Hoof (*Ungula*) in prism $R^2 H$
     - $\text{Vol} = \frac{2}{3} R^2 H = \frac{2}{3}\,\text{Prism}$
     - Archimedes *The Method* (rediscovered 1906!)
   * - *Appendix Prop.* XIII
     - Solid Hemisphere centroid along axis $VO$
     - $\bar{z}_{\text{vertex}} : \bar{z}_{\text{base}} = 5 : 3$
     - Luca Valerio (*De centro gravitatis*, 1604)
   * - *Appendix Prop.* XIV
     - Parabolic Conoid centroid along axis
     - $\bar{z}_{\text{vertex}} : \bar{z}_{\text{base}} = 2 : 1$
     - Archimedes / Commandino (1565) / Torricelli (1644)

3. **Ceva's Closing Caution on Indivisibles**: Summing parallel circles $2\pi r(z)\,dz$ along an axis omits the Jacobian slant factor $\sec\alpha = \sqrt{1 + (dr/dz)^2}$ of inscribed Archimedean conical frusta—explaining why naive surface indivisibles yield $\frac{\pi^2}{2}R^2$ instead of $2\pi R^2$ on a hemisphere.
