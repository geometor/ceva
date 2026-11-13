:navigation: header
:order: 20

Symbolic Demonstrations
=======================

Executable pure-symbolic Python demonstrations (`Model(..., auto_intersect=False)`) verifying every static lever equilibrium, signed barycentric coordinate, isotomic conjugate, projective harmonic range, Rational Trigonometry spread law, multilateral odd-polygon product, 3D seven-line tetrahedral concurrency, and *Appendix Geometrica* quadrature/cubature in ``geometor.ceva`` with **zero floating-point coordinates**.

.. contents:: On this page
   :local:
   :depth: 2

1. Static Barycentrics, Negative Weights (`F - A`), Isotomic Conjugates & Spread Ceva
-------------------------------------------------------------------------------------

Proves Ceva's Theorem and sub-triangle area proportions universally over indeterminate coordinates, evaluates canonical centers $X(1), X(2), X(4), X(6), X(7), X(8)$ and the exterior $A$-excenter $J_A$ over $\mathbb{Q}^2$ on the Heronian $(13, 14, 15)$ triangle, constructs ``@proposition`` models for interior/exterior concurrency, isotomic conjugation ($X(7) \leftrightarrow X(8)$), and the Menelaus harmonic conjugate $(B, C; D, D') = -1$, and verifies **Spread Ceva's Theorem** without square roots.

.. literalinclude:: ../../demos/static_barycentrics.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/static_barycentrics.py

2. Multilateral Odd Polygons, Circumscribed Conics, 3D Tetrahedra & Appendix Geometrica
---------------------------------------------------------------------------------------

Constructs concurrent cevians on a convex rational pentagon, proves *Liber Secundus, Lemma I* symbolically for polygons circumscribed around circles and Borelli–Serenus projected ellipses, verifies Ceva's 3D skew-quadrilateral corollary (*Elementum* V *Coroll.*) and 7-line tetrahedral equilibrium (*Liber Primus, Prop.* XXIII), and confirms Hippocratean lune quadrature, cylindrical *ungula* $\frac{2}{3}$ prism cubature, and hemisphere ($5:3$) / paraboloid ($2:1$) centroids.

.. literalinclude:: ../../demos/polygon_tetrahedron.py
   :language: python
   :linenos:

Run locally:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/polygon_tetrahedron.py
