:layout: book
:order: 2
:canonical_id: liber_primus
:breadcrumb_title: Liber Primus (Summary)
:folio: 0018
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _unit-2-liber-primus-ceva-menelaus-summary:
.. _liber-primus-summary:

Liber Primus · Executive Geometric Summary
==========================================

Core Theses & Theorems of *Liber Primus* (1678, pp. 1–44)
---------------------------------------------------------

1. **The Static Calculus of Intersecting Lines**: Placing non-zero point masses $(u, v, w)$ at triangle vertices $(A, B, C)$ transforms geometric concurrency into associative barycentric grouping. By Archimedes' Law of the Lever ($u \cdot \overline{AF} = v \cdot \overline{FB}$), composite fulcrums determine concurrent cevian lines at the global center of gravity $P = \frac{uA + vB + wC}{u + v + w}$.
2. **Signed / Negative Weights (1678 $\to$ 1827)**: In *Elementum* III & p. 5 *Scholium*, Ceva extends the physical lever to exterior concurrency by writing subtractive weights *"more analytico, seu algebrico"* as $F - A$ (:term:`pondus negativum <pondus-negativum>`), directly anticipating :person:`August Ferdinand Möbius <moebius>` (1827).
3. **3D Non-Planar Skew Quadrilateral Coplanarity**: In *Elementum* V *Corollarium* (pp. 6–7), four spatial fulcrums along a non-planar 3D quadrilateral remain strictly coplanar because opposite-edge lever joins intersect at the spatial center of gravity $O$.
4. **Ceva's Theorem & Menelaus's Transversal**: *Proposition VII* establishes that cevians $AD, BE, CF$ concur if and only if $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$. Dividing Ceva's relation by *Proposition VIII* (Menelaus's transversal $\frac{AF}{FB}\cdot\frac{BD'}{D'C}\cdot\frac{CE}{EA} = -1$) produces the projective harmonic range $(B, C; D, D') = -1$ constructible by straightedge alone.
5. **Canonical Centers & Spread Ceva**: Every classical Kimberling center possesses exact rational coordinates over $\mathbb{Q}$ on Heronian triangles ($X_1, X_2, X_4, X_6, X_7, X_8, J_A$). In Rational Trigonometry, Spread Ceva replaces transcendental sines with exact rational vertex spreads and quadrances: $\prod \frac{s(\angle BAD)}{s(\angle DAC)} = 1$.
6. **Seven-Line 3D Tetrahedral Equilibrium (*Prop. XXIII*)**: Given non-coplanar vertices $A, B, C, D$ with weights $(m_A, m_B, m_C, m_D)$, the unique spatial center of gravity $O$ lies simultaneously on **all 7** lines: 4 vertex-to-face cevians ($V G_V$, divided in ratio $\frac{M - m_V}{m_V}$) and 3 skew-edge bimedians ($E_{ij} E_{kl}$, divided in ratio $\frac{m_k + m_l}{m_i + m_j}$).

.. list-table:: Static Regimes in *Liber Primus* (``geometor.ceva``)
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
   * - *Prop.* XXIII (`Tab. 3, Fig. 28`)
     - $(m_A, m_B, m_C, m_D)$ in $\mathbb{R}^3$
     - 4 cevians + 3 bimedians
     - 7-line spatial concurrency *"mira quadam concordia"* at $O$
