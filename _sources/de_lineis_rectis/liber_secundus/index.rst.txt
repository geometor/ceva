:layout: book
:order: 3
:canonical_id: liber_secundus
:breadcrumb_title: Liber Secundus
:folio: 0062
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _unit-3-liber-secundus-polygons-solids:
.. _unit-3-liber-secundus-polygons-solids-en:
.. _liber-secundus:
.. _liber-secundus-en:

Liber Secundus · Circumscribed Conics, Isotomic Conjugates & Odd Polygons (pp. 45–72)
===============================================================================================

.. rubric:: *Original GEOMETOR English translation from Giovanni Ceva's De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`, *Liber Secundus*, Lemma I & Props. I–XIV, pp. 45–72; Scans 0062–0089; `Tab. 4–7, Figs. 32–61`).

.. folio:: 0062
   :page: 45

1. Lemma I — Borelli–Serenus Cylindrical Ellipse Projection (pp. 45–47)
-----------------------------------------------------------------------

Opening *Liber Secundus* (`Tab. 4, Figs. 32–35`), Ceva proves a master projective-affine lemma for polygons circumscribed about circles and ellipses:

* **Circle Case**: Let any polygon of $n$ sides (whether $n$ be odd or even) be circumscribed around a circle :g:`circleC`. Since the two tangents drawn from each exterior vertex $V_k$ to the circle have equal lengths $t_k$ (:just:`III.36`), the contact points $T_0, T_1, \dots, T_{n-1}$ divide the consecutive sides into segments $(t_0, t_1), (t_1, t_2), \dots, (t_{n-1}, t_0)$ whose cyclic compound ratio is identically $1$:

  $$\frac{t_0}{t_1} \cdot \frac{t_1}{t_2} \cdots \frac{t_{n-1}}{t_0} = 1.$$

* **Ellipse Case via Cylindrical Section**: Now erect a right or oblique circular cylinder upon :g:`circleC` and cut it by an oblique plane (:g:`projCyl`), producing an arbitrary Apollonian ellipse :g:`ellipseE`, as demonstrated by :person:`Serenus of Antinoöpolis <serenus>` (:cite:`1566 <serenus:cylindri>`) and :person:`Giovanni Alfonso Borelli <borelli>` (:cite:`1661 <borelli:1661:apollonius>`). Because parallel generator lines along the cylinder map every tangent side $V_k V_{k+1}$ to a tangent side $V'_k V'_{k+1}$ of the ellipse and preserve the ratio of collinear segments (:just:`VI.2`), **any $n$-gon circumscribed about an ellipse also has its sides divided at the contact points in cyclic compound ratio $1$** (:term:`sectio cylindrica <sectio-cylindrica>`)!

2. Prop. I & *Corollarium* — Contact Point $X(7)$ & Isotomic Conjugate $X(8)$ (pp. 47–50)
------------------------------------------------------------------------------------------

Applying *Lemma* I to a triangle :g:`ABC` circumscribed around an inscribed circle :g:`incircle` (or any inscribed ellipse), **Proposition I** (pp. 47–49, `Tab. 4, Figs. 36–37`) establishes immediately by *Liber Primus, Prop.* VII that the three cevians :g:`AD`, :g:`BE`, :g:`CF` drawn to the points of contact concur at a single point :g:`X(7) <X7>`—published by Ceva in **1678**, 140 years before :person:`Joseph Diez Gergonne <gergonne>` (:term:`punctum contactus <punctum-contactus>`)!

Immediately afterward, in **Proposition I *Corollarium***, Ceva discovers **isotomic conjugation** (:term:`coniugatum isotomicum <coniugatum-isotomicum>`): if on each side of triangle :g:`ABC` we transfer the contact distances to the opposite ends—choosing :g:`D* <D_iso>`, :g:`E* <E_iso>`, :g:`F* <F_iso>` so that $BD^* = DC$ (:g:`BD_eq`), $CE^* = EA$ (:g:`CE_eq`), and $AF^* = FB$ (:g:`AF_eq`)—then each side ratio is inverted to its reciprocal, so their compound product remains $1^{-1} = 1$, and the three reflected cevians :g:`AD* <AD_iso>`, :g:`BE* <BE_iso>`, :g:`CF* <CF_iso>` concur at the reciprocal center :g:`X(8) <X8>` (rediscovered by :person:`Christian Heinrich von Nagel <nagel>` in 1836)!

.. picture:: /_static/figures/fig04_isotomic_gergonne_nagel.svg
   :alt: Ceva Liber Secundus Prop I Gergonne Contact Point X7 and Isotomic Nagel Point X8

3. Props. II–XIV — Multilateral Odd $(2m + 1)$-gon Concurrency (pp. 50–72)
---------------------------------------------------------------------------

In **Propositions II–XIV** (`Tab. 4–7, Figs. 38–61`), Ceva generalizes cevian concurrency and conic tangency from triangles to **multilateral polygons of odd side count** $n = 2m + 1$ (pentagons :g:`pentagon`, heptagons, enneagons). Whenever rays (:g:`cev0`, :g:`cev1`, :g:`cev2`, :g:`cev3`, :g:`cev4`) from the $2m + 1$ vertices (:g:`V0`..:g:`V4`) pass through a common concurrency center :g:`P` to meet their opposite sides at (:g:`Q0`..:g:`Q4`), static weight transfer across the vertex-to-opposite-side bipartite cycle proves that the cyclic product of the $2m + 1$ opposite-side division ratios equals $+1$:

$$\prod_{i=0}^{2m} \frac{\overline{V_{i+m} Q_i}}{\overline{Q_i V_{i+m+1}}} = 1.$$

.. picture:: /_static/figures/fig06_pentagon_multilateral_ceva.svg
   :alt: Ceva Liber Secundus Odd Pentagon Concurrency and Lemma I Cylindrical Ellipse Projection

.. toctree::
   :hidden:

   la
   summary
   notes
