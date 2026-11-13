.. _unit-3-liber-secundus-polygons-solids-notes:

Unit III · Historical & Mathematical Commentary
===============================================

1. Ceva's Priority for the Gergonne Point $X(7)$ and Isotomic Conjugation (1678)
--------------------------------------------------------------------------------

Standard nineteenth- and twentieth-century textbooks routinely attribute the concurrency of incircle-contact cevians $X(7)$ to :person:`Joseph Diez Gergonne <gergonne>` (*Annales de Mathématiques*, 1818) and the isotomic excircle-contact point $X(8)$ to :person:`Christian Heinrich von Nagel <nagel>` (1836). Yet inspection of `Tab. 4, Figs. 36–37` (printed pp. 47–50 of the 1678 Milan quarto) shows that :person:`Giovanni Ceva <ceva>` proved **both** results in full generality—not merely for circles, but for **arbitrary inscribed ellipses**—together with the general midpoint-reflection theorem for isotomic conjugates!

2. Why Multilateral Vertex-to-Opposite-Side Ceva Requires Odd $n = 2m + 1$
--------------------------------------------------------------------------

Why does *Liber Secundus* separate **odd** polygons ($n = 2m + 1$: triangles, pentagons, heptagons) from even polygons ($n = 2m$: quadrilaterals, hexagons)?

* In an **odd $(2m+1)$-gon**, each vertex $V_i$ stands directly opposite a unique **side** $e_{i+m} = V_{i+m} V_{i+m+1}$. As $i$ runs through $\mathbb{Z} / (2m+1)\mathbb{Z}$, the map $i \mapsto i + m$ is a bijection from vertices to sides. Moreover, using signed areas relative to concurrency point $P$:

  $$\frac{\overline{V_{i+m} Q_i}}{\overline{Q_i V_{i+m+1}}} = \frac{[\triangle P V_i V_{i+m}]}{[\triangle P V_{i+m+1} V_i]} = -\frac{[\triangle P V_i V_{i+m}]}{[\triangle P V_i V_{i+m+1}]}.$$

  Because $n = 2m + 1$ is odd, the vertex-step $m$ and $(m + 1)$ have $\gcd(m, 2m+1) = 1$, and orienting the rays from $V_i$ *through* $P$ to the opposite side gives $[\triangle P V_i V_{i+m}]$ and $[\triangle P V_{i+m+1} V_i]$ with the **same** positive sign when $P$ lies inside the convex $(2m+1)$-gon, telescoping the ratio of altitudes/sine products around the cycle cleanly to $+1$!
* By contrast, in an **even $2m$-gon**, vertices stand opposite *vertices* (diagonals), whereas *Lemma* I (`Tab. 4, Figs. 33, 35`) governs tangent contact points on all $2m$ sides simultaneously (an anticipation of Brianchon's theorem for circumscribed hexagons).
