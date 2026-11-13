.. _unit-1-statica-foundations-summary:

Unit I · Executive Geometric Summary
====================================

Core Theses of the Frontmatter & *Liber Primus* Opening (1678, pp. 1–7)
-----------------------------------------------------------------------

1. **The Principle of *Statica Constructio***: Rather than introducing clever auxiliary parallels or circles *ad hoc* for each incidence theorem, :person:`Giovanni Ceva <ceva>` places exact non-zero point masses $(u, v, w)$ at the vertices $(A, B, C)$ of a geometric configuration. Because addition of weighted points is **commutative and associative** and the global :term:`center of gravity <centrum-gravitatis>` $P = \frac{uA + vB + wC}{u + v + w}$ is **unique** (*Axioma* I), grouping $(B, C)$ first at fulcrum $D$, $(C, A)$ at $E$, or $(A, B)$ at $F$ forces $AD$, $BE$, and $CF$ to concur at $P$.
2. **Signed / Negative Weights (1678 $\to$ 1827)**: On printed page 5 (*Elementum* III *Scholium*), Ceva extends Archimedes' physical lever to exterior concurrency by writing subtractive weights *"more analytico, seu algebrico"* as $F - A$ (:term:`pondus negativum <pondus-negativum>`). Whenever one vertex carries a negative sign (e.g., $(-u, +v, +w)$ with $u + v + w \neq 0$), exactly two side fulcrums fall externally on extended sides, producing two negative directed ratios and one positive ratio whose product remains $(-)(+)(-) = +1$.
3. **3D Non-Planar Skew Quadrilateral Coplanarity**: In *Elementum* V *Corollarium* (pp. 6–7), Ceva proves that four weights $(m_A, m_B, m_C, m_D)$ on a **non-planar 3D quadrilateral** determine four edge fulcrums $E_{AB}, E_{BC}, E_{CD}, E_{DA}$ in cyclic product $1$ whose opposite joins $E_{AB}E_{CD}$ and $E_{BC}E_{DA}$ intersect at the spatial center $O = \frac{m_A A + m_B B + m_C C + m_D D}{m_A + m_B + m_C + m_D}$, forcing all four spatial fulcrums to be coplanar.

.. list-table:: Static Regimes in *Liber Primus*, Elementa I–V (``geometor.ceva``)
   :header-rows: 1
   :widths: 22 24 26 28

   * - 1678 Locus
     - Vertex Weights
     - Directed Side Ratios
     - Geometric Regime
   * - *Elementum* II (`Tab. 1, Fig. 5`)
     - $(+u, +v, +w)$, same sign
     - $(+ , + , +)$, product $= +1$
     - Interior concurrency $P \in \operatorname{int}(\triangle ABC)$
   * - *Elementum* III & p. 5 *Scholium*
     - $(-u, +v, +w)$, $u \neq v, w$
     - $(- , + , -)$, product $= +1$
     - Exterior concurrency (e.g., excenter $J_A$)
   * - Limit $v + w = 0$
     - $(u, v, -v)$
     - Fulcrum $D \to \infty$
     - Cevian $AD \parallel BC$ (ideal projective point)
   * - *Elementum* V *Corollarium*
     - $(m_A, m_B, m_C, m_D)$ in $\mathbb{R}^3$
     - $r_1 r_2 r_3 r_4 = +1$, $\det = 0$
     - Coplanar fulcrums & intersecting joins on 3D skew cycle
