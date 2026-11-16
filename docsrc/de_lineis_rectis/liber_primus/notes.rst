:layout: book
:order: 2
:canonical_id: liber_primus
:breadcrumb_title: Liber Primus (Notes)
:folio: 0018
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _unit-2-liber-primus-ceva-menelaus-notes:
.. _liber-primus-notes:

Liber Primus · Historical & Mathematical Commentary
===================================================

1. Caravaggio Jr., Commandino & the Theory of Compound Ratios
-------------------------------------------------------------

In *Proposition VI*, Ceva includes the synthetic parallel-line demonstration of :person:`Pietro Paolo Caravaggio Jr. <caravaggio>`, proving that the concurrency criterion holds purely by Euclidean geometry (:just:`VI.4`) without mechanics. In *Lemma IV* and *Proposition VII*, Ceva grounds the calculation in the theory of :term:`compound ratios <ratio-composita>` established by :person:`Federico Commandino <commandino>` and :person:`Christoph Clavius <clavius>` (:cite:`1589 <clavius:1589:euclides>`), showing that multiplying proportions along the perimeter constitutes a rigorous operation on Euclidean magnitudes.

2. Projective Harmonic Conjugation & Straightedge Construction
--------------------------------------------------------------

By juxtaposing Ceva's concurrency (*Prop. VII*) with Menelaus's transversal (*Prop. VIII*), Ceva arrives at **projective harmonic division**:

$$\frac{\overline{BD}}{\overline{DC}} = -\frac{\overline{BD'}}{\overline{D'C}} \qquad \Longleftrightarrow \qquad (B, C; D, D') = -1.$$

In modern projective geometry, this means the cevian triangle and base transversal form a **complete quadrangle** whose diagonal points isolate harmonic conjugates. Ceva showed that harmonic conjugates can be constructed using an unmarked straightedge alone, anticipating :person:`Girard Desargues <desargues>` and nineteenth-century projective synthetic geometry (:person:`von Staudt <staudt>`).

3. From ``F - A`` to Möbius's *Barycentrischer Calcul* (1827)
-------------------------------------------------------------

On printed page 5 (*Elementum III Scholium*), Ceva's introduction of subtractive weights *"more analytico, seu algebrico"* as $F - A$ (:term:`pondus negativum <pondus-negativum>`) represents a conceptual breakthrough. By allowing weights to take negative signs, Ceva extended statics across the entire plane, establishing homogeneous barycentric coordinates $(u : v : w) \in \mathbb{P}^2(\mathbb{Q})$ nearly 150 years before :person:`August Ferdinand Möbius <moebius>` published *Der barycentrische Calcul* (:cite:`1827 <moebius:1827:barycentr>`).

4. Commandino's 3:1 Centroid & the 7-Line Spatial Equilibrium
-------------------------------------------------------------

In *Proposition XXIII*, Ceva extends statics into solid geometry. In 1565, :person:`Federico Commandino <commandino>` proved in *De centro gravitatis solidorum* (:cite:`1565 <commandino:1565:centro>`) that the centroid of a tetrahedron divides each median joining a vertex to the opposite face's centroid in the ratio $3 : 1$. Ceva generalizes Commandino's theorem to **arbitrary non-equal masses** $(m_A, m_B, m_C, m_D)$, demonstrating that all 4 vertex-to-face cevians and all 3 skew-edge bimedians intersect at the unique center of gravity $O$ *"mira quadam concordia"*—a 7-line spatial concurrency theorem.

5. Exact Symbolic Realization in ``geometor.ceva``
--------------------------------------------------

In :func:`geometor.ceva.static_barycentrics.solve_static_barycentrics`, vertex weights $(u, v, w)$ of any non-degenerate signs over $\mathbb{Z}$, $\mathbb{Q}$, or symbolic polynomial rings yield exact coordinates without floating-point approximations. In :func:`geometor.ceva.polygon_tetrahedron.solve_tetrahedron_static_equilibrium`, 3D tetrahedral equilibrium across all 7 lines is verified symbolically, confirming the vanishing concurrency residuals on non-coplanar vertices.
