.. _unit-3-liber-secundus-polygons-solids-en:

Unit III · 3D Tetrahedra, Circumscribed Conics, Isotomic Conjugates & Odd Polygons (pp. 36–72)
==============================================================================================

*Original GEOMETOR English translation from Giovanni Ceva's De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`, *Liber Primus*, Props. XXIII–XXVI, pp. 36–43, & *Liber Secundus*, Lemma I & Props. I–XIV, pp. 45–72; `Tab. 3–7, Figs. 28–61`).

1. *Liber Primus*, Props. XXIII–XXVI — The Seven-Line Tetrahedron Equilibrium (pp. 36–43)
-----------------------------------------------------------------------------------------

Crowning *Liber Primus* (`Tab. 3, Figs. 28–31`), :person:`Giovanni Ceva <ceva>` ascends from the plane into three-dimensional solid geometry. Suppose four arbitrary non-zero weights $(m_A, m_B, m_C, m_D)$ are placed at the four vertices :g:`A`, :g:`B`, :g:`C`, :g:`D` of a solid tetrahedron :g:`ABCD <tetABCD>`. By associative static grouping, the global spatial center of gravity :g:`O` can be reached in **seven distinct ways**:

1. **Four Spatial Vertex-to-Face Cevians**: First combine any three vertices on their triangular face—yielding the four static face centers of gravity :g:`G_A` on $\triangle BCD$, :g:`G_B` on $\triangle ACD$, :g:`G_C` on $\triangle ABD$, and :g:`G_D` on $\triangle ABC$—and then join each face center to the remaining opposite vertex (:g:`AG_A`, :g:`BG_B <AG_B>`, :g:`CG_C <AG_C>`, :g:`DG_D <AG_D>`). Every one of these four spatial rays divides at :g:`O` in exact ratio $\overline{VO} : \overline{OG_V} = (m_{\text{tot}} - m_V) : m_V$ (for equal weights $1:1:1:1$, the classic $3 : 1$ tetrahedral centroid ratio of :person:`Commandino <commandino>`, :cite:`1565 <commandino:1565:centro>`).
2. **Three Skew-Edge Bimedians**: Alternatively, pair the four vertices into two opposite skew edges—$(AB, CD)$, $(AC, BD)$, or $(AD, BC)$—balancing each edge at its lever fulcrum (:g:`E_AB` with :g:`E_CD`, :g:`E_AC` with :g:`E_BD`, and :g:`E_AD` with :g:`E_BC`). Then the three straight segments (:g:`B_AB_CD`, :g:`B_AC_BD`, :g:`B_AD_BC`) joining opposite skew-edge fulcrums **also pass through the exact same point** :g:`O`!

.. picture:: /_static/figures/fig07_tetrahedron_seven_lines.svg
   :alt: Ceva Liber Primus Prop XXIII 3D Tetrahedron Seven-Line Static Equilibrium at Center O

Marveling at this simultaneous spatial intersection of **seven** lines in three-space, Ceva exclaims that all seven rays meet at :g:`O` *"mira quadam concordia"*—with a :term:`wondrous concord <concordia-septem-linearum>`! In **Propositions XXIV–XXVI**, Ceva extends the same barycentric decomposition to quadrangular and polygonal pyramids.

2. *Liber Secundus*, Lemma I — Borelli–Serenus Cylindrical Ellipse Projection (pp. 45–47)
-----------------------------------------------------------------------------------------

Opening *Liber Secundus* (`Tab. 4, Figs. 32–35`), Ceva proves a master projective-affine lemma for polygons circumscribed about circles and ellipses:

* **Circle Case**: Let any polygon of $n$ sides (whether $n$ be odd or even) be circumscribed around a circle :g:`circleC`. Since the two tangents drawn from each exterior vertex $V_k$ to the circle have equal lengths $t_k$ (:just:`III.36`), the contact points $T_0, T_1, \dots, T_{n-1}$ divide the consecutive sides into segments $(t_0, t_1), (t_1, t_2), \dots, (t_{n-1}, t_0)$ whose cyclic compound ratio is identically $1$:

  $$\frac{t_0}{t_1} \cdot \frac{t_1}{t_2} \cdots \frac{t_{n-1}}{t_0} = 1.$$

* **Ellipse Case via Cylindrical Section**: Now erect a right or oblique circular cylinder upon :g:`circleC` and cut it by an oblique plane (:g:`projCyl`), producing an arbitrary Apollonian ellipse :g:`ellipseE`, as demonstrated by :person:`Serenus of Antinoöpolis <serenus>` (:cite:`1566 <serenus:cylindri>`) and :person:`Giovanni Alfonso Borelli <borelli>` (:cite:`1661 <borelli:1661:apollonius>`). Because parallel generator lines along the cylinder map every tangent side $V_k V_{k+1}$ to a tangent side $V'_k V'_{k+1}$ of the ellipse and preserve the ratio of collinear segments (:just:`VI.2`), **any $n$-gon circumscribed about an ellipse also has its sides divided at the contact points in cyclic compound ratio $1$** (:term:`sectio cylindrica <sectio-cylindrica>`)!

3. *Liber Secundus*, Prop. I & *Corollarium* — Contact Point $X(7)$ & Isotomic Conjugate $X(8)$
-----------------------------------------------------------------------------------------------

Applying *Lemma* I to a triangle :g:`ABC` circumscribed around an inscribed circle :g:`incircle` (or any inscribed ellipse), **Proposition I** (pp. 47–49, `Tab. 4, Figs. 36–37`) establishes immediately by *Liber Primus, Prop.* VII that the three cevians :g:`AD`, :g:`BE`, :g:`CF` drawn to the points of contact concur at a single point :g:`X(7) <X7>`—published by Ceva in **1678**, 140 years before :person:`Joseph Diez Gergonne <gergonne>` (:term:`punctum contactus <punctum-contactus>`)!

Immediately afterward, in **Proposition I *Corollarium***, Ceva discovers **isotomic conjugation** (:term:`coniugatum isotomicum <coniugatum-isotomicum>`): if on each side of triangle :g:`ABC` we transfer the contact distances to the opposite ends—choosing :g:`D* <D_iso>`, :g:`E* <E_iso>`, :g:`F* <F_iso>` so that $BD^* = DC$ (:g:`BD_eq`), $CE^* = EA$ (:g:`CE_eq`), and $AF^* = FB$ (:g:`AF_eq`)—then each side ratio is inverted to its reciprocal, so their compound product remains $1^{-1} = 1$, and the three reflected cevians :g:`AD* <AD_iso>`, :g:`BE* <BE_iso>`, :g:`CF* <CF_iso>` concur at the reciprocal center :g:`X(8) <X8>` (rediscovered by :person:`Christian Heinrich von Nagel <nagel>` in 1836)!

.. picture:: /_static/figures/fig04_isotomic_gergonne_nagel.svg
   :alt: Ceva Liber Secundus Prop I Gergonne Contact Point X7 and Isotomic Nagel Point X8

4. *Liber Secundus*, Props. II–XIV — Multilateral Odd $(2m + 1)$-gon Concurrency (pp. 50–72)
--------------------------------------------------------------------------------------------

In **Propositions II–XIV** (`Tab. 4–7, Figs. 38–61`), Ceva generalizes cevian concurrency and conic tangency from triangles to **multilateral polygons of odd side count** $n = 2m + 1$ (pentagons :g:`pentagon`, heptagons, enneagons). Whenever rays (:g:`cev0`, :g:`cev1`, :g:`cev2`, :g:`cev3`, :g:`cev4`) from the $2m + 1$ vertices (:g:`V0`..:g:`V4`) pass through a common concurrency center :g:`P` to meet their opposite sides at (:g:`Q0`..:g:`Q4`), static weight transfer across the vertex-to-opposite-side bipartite cycle proves that the cyclic product of the $2m + 1$ opposite-side division ratios equals $+1$:

$$\prod_{i=0}^{2m} \frac{\overline{V_{i+m} Q_i}}{\overline{Q_i V_{i+m+1}}} = 1.$$

.. picture:: /_static/figures/fig06_pentagon_multilateral_ceva.svg
   :alt: Ceva Liber Secundus Odd Pentagon Concurrency and Lemma I Cylindrical Ellipse Projection
