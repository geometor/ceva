.. _unit-1-statica-foundations-notes:

Unit I · Historical & Mathematical Commentary
=============================================

1. Al-Mu'taman ibn Hūd (11th Century) vs. Ceva's Static Revolution (1678)
-------------------------------------------------------------------------

For three centuries :person:`Giovanni Ceva <ceva>` was universally regarded as the sole discoverer of the concurrency criterion $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$. In 1985, historian Jan P. Hogendijk (:cite:`1995 <hogendijk:1995:mutaman>`) discovered that :person:`Yusuf al-Mu'taman ibn Hud <mutaman>` (d. 1085), Hudid King of Zaragoza, had already proved the theorem synthetically in his Arabic *Kitāb al-Istikmāl* (*Book of Perfection*) by iterated applications of :person:`Menelaus's <menelaus>` transversal theorem.

Because *Kitāb al-Istikmāl* was never translated into medieval Latin, Ceva's 1678 discovery in Milan was completely independent—and methodologically far more radical. Where al-Mu'taman worked inside classical Greek proportion theory, Ceva invented **barycentric statics**: assigning algebraic masses $(u : v : w)$ to points so that incidence theorems reduce to associative vector addition over $\mathbb{Q}$.

2. From ``A † F`` and ``F - A`` (1678) to Möbius's *Barycentrischer Calcul* (1827)
----------------------------------------------------------------------------------

Two features of Ceva's opening pages mark a watershed between Renaissance Archimedeanism (:person:`Commandino <commandino>`, :person:`Valerio <valerio>`) and modern projective-affine algebra:

* **Typography in Transition (`A † F` and `F - A`)**: In Lombardy in 1678, :person:`Ludovico Monza's <monza>` press used the obelus ``†`` for addition alongside ``-`` for subtraction. Ceva's willingness on page 5 to treat a physical weight *"more analytico, seu algebrico"* as $F - A$ liberated static moments from the Greek requirement of strictly positive magnitudes. Physically, a negative weight acts as an upward buoyant pull (or pulley tension); algebraically, it yields homogeneous coordinates $(u : v : w) \in \mathbb{P}^2(\mathbb{Q})$ across the entire projective plane, directly anticipating :person:`August Ferdinand Möbius <moebius>` (:cite:`1827 <moebius:1827:barycentr>`).
* **Exact Symbolic Realization in ``geometor.ceva``**: In :func:`geometor.ceva.static_barycentrics.solve_static_barycentrics`, weights $(u, v, w)$ of any non-degenerate signs over $\mathbb{Z}$, $\mathbb{Q}$, or symbolic polynomial rings produce exact ``Point2D`` coordinates without a single floating-point operation or square root, while :func:`geometor.ceva.polygon_tetrahedron.verify_skew_quadrilateral_ceva` confirms the vanishing $3\times 3$ coplanarity determinant of *Elementum* V *Corollarium* on non-planar 3D vertices.
