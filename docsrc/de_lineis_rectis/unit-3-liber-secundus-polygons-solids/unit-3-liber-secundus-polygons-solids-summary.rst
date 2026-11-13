.. _unit-3-liber-secundus-polygons-solids-summary:

Unit III · Executive Geometric Summary
======================================

Core Results of *Liber Primus* XXIII–XXVI & *Liber Secundus* (1678, pp. 36–72)
------------------------------------------------------------------------------

1. **Seven-Line 3D Tetrahedral Equilibrium (*Lib. I, Prop. XXIII*)**: Given non-coplanar vertices $A, B, C, D \in \mathbb{Q}^3$ with non-zero masses $(m_A, m_B, m_C, m_D)$ and $M = m_A + m_B + m_C + m_D \neq 0$, the unique spatial center of gravity $O = \frac{1}{M}(m_A A + m_B B + m_C C + m_D D)$ lies simultaneously on **all 7** static lines (:func:`~geometor.ceva.polygon_tetrahedron.solve_tetrahedron_static_equilibrium`):

   - **4 Vertex-to-Face Cevians** $V G_V$, divided at $O$ in ratio $\frac{\overline{VO}}{\overline{OG_V}} = \frac{M - m_V}{m_V}$;
   - **3 Opposite-Edge Bimedians** $E_{ij} E_{kl}$, divided at $O$ in ratio $\frac{\overline{E_{ij} O}}{\overline{O E_{kl}}} = \frac{m_k + m_l}{m_i + m_j}$.

2. **Affine Invariance of Circumscribed Conic Tangency (*Lib. II, Lemma I*)**: Under any invertible affine transformation $X' = M X + b$ (realized geometrically by :person:`Serenus <serenus>` and :person:`Borelli <borelli>` via oblique cylindrical section), a circle maps to a general ellipse, tangent lines map to tangent lines, and every collinear contact division ratio $\lambda_k = \overline{V_k T_k} / \overline{T_k V_{k+1}}$ is strictly preserved, keeping $\prod_{k=0}^{n-1} \lambda_k = 1$ (:func:`~geometor.ceva.polygon_tetrahedron.prove_circumscribed_polygon_lemma`).
3. **Gergonne $X(7)$ & Isotomic Conjugate $X(8)$ (*Lib. II, Prop. I & Corollarium*)**: Reflecting the contact feet $(D, E, F)$ of $P = (u : v : w)$ across the side midpoints produces $D^* = B + C - D$, $E^* = C + A - E$, $F^* = A + B - F$, inverting every side ratio and mapping $(u : v : w) \mapsto (u^{-1} : v^{-1} : w^{-1})$. For the incircle, $X(7) = \left(\frac{1}{s-a} : \frac{1}{s-b} : \frac{1}{s-c}\right) \mapsto X(8) = (s - a : s - b : s - c)$ (:func:`~geometor.ceva.static_barycentrics.construct_isotomic_conjugate`).
4. **Odd $(2m + 1)$-gon Multilateral Ceva Concurrency**: On our convex rational pentagon $V_0=(0,0), V_1=(8,0), V_2=(11,6), V_3=(5,11), V_4=(-2,6)$ with $P=(4,4)$, :func:`~geometor.ceva.polygon_tetrahedron.verify_odd_polygon_ceva` yields exact side ratios $\left(\frac{5}{6}, 2, \frac{13}{10}, \frac{3}{4}, \frac{8}{13}\right)$ whose product is identically $1$.
