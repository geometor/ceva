.. _unit-2-liber-primus-ceva-menelaus-summary:

Unit II · Executive Geometric Summary
=====================================

Core Results of *Liber Primus*, Props. VI–XXII (1678, pp. 7–35)
---------------------------------------------------------------

1. **Equivalence of Static & Synthetic Proofs (*Props.* VI–VII)**: :person:`Pietro Paolo Caravaggio Jr.'s <caravaggio>` parallel-line construction through vertex $A$ (*Prop.* VI) translates Ceva's static weight cancellation into three pairs of similar triangles (:just:`VI.4`), establishing both necessity and sufficiency (*reductio* / coincidence of the third foot $F^* = F$ by :just:`V.9`).
2. **Ceva–Menelaus Duality & Straightedge Harmonic Conjugation (*Prop.* VIII)**: Pairing concurrent cevians $AD, BE, CF$ ($\frac{AF}{FB}\frac{BD}{DC}\frac{CE}{EA} = +1$) with the transversal $EF$ cutting $BC$ at $D'$ ($\frac{AF}{FB}\frac{BD'}{D'C}\frac{CE}{EA} = -1$) yields $\frac{BD}{DC} + \frac{BD'}{D'C} = 0$, proving $(B, C; D, D') = -1$ (:func:`~geometor.ceva.static_barycentrics.construct_cevian_menelaus_harmonic`).
3. **Exact Rational Constellation on Heronian $\triangle(13, 14, 15)$**: Choosing $A=(5,12), B=(0,0), C=(14,0)$ ($a=14, b=15, c=13, s=21, \Delta=84, r=4$) places every classical center inside $\mathbb{Q}^2$ with zero radicals:

.. list-table:: Canonical Triangle Centers on $\triangle(13, 14, 15)$ (``geometor.ceva.static_barycentrics``)
   :header-rows: 1
   :widths: 12 24 22 22 20

   * - Center
     - Geometric Definition
     - Static Weights $u : v : w$
     - Exact Coordinates in $\mathbb{Q}^2$
     - Ceva Product
   * - ``X(1)``
     - Incenter (angle bisectors)
     - $14 : 15 : 13$
     - $(6, 4)$
     - $\frac{15}{14}\cdot\frac{13}{15}\cdot\frac{14}{13} = 1$
   * - ``X(2)``
     - Centroid (medians)
     - $1 : 1 : 1$
     - $\left(\frac{19}{3}, 4\right)$
     - $1 \cdot 1 \cdot 1 = 1$
   * - ``X(4)``
     - Orthocenter (altitudes)
     - $70 : 99 : 55$
     - $\left(5, \frac{15}{4}\right)$
     - $\frac{99}{70}\cdot\frac{55}{99}\cdot\frac{70}{55} = 1$
   * - ``X(6)``
     - Symmedian point ($a^2:b^2:c^2$)
     - $196 : 225 : 169$
     - $\left(\frac{1673}{295}, \frac{1176}{295}\right)$
     - $\frac{225}{196}\cdot\frac{169}{225}\cdot\frac{196}{169} = 1$
   * - ``X(7)``
     - Gergonne point (*Lib. II Prop. I*)
     - $24 : 28 : 21$
     - $\left(\frac{414}{73}, \frac{288}{73}\right)$
     - $\frac{7}{6}\cdot\frac{3}{4}\cdot\frac{8}{7} = 1$
   * - ``X(8)``
     - Nagel point (*isotomic*)
     - $7 : 6 : 8$
     - $(7, 4)$
     - $\frac{6}{7}\cdot\frac{8}{6}\cdot\frac{7}{8} = 1$
   * - ``J_A``
     - $A$-Excenter (*Elem. III* `F - A`)
     - $-14 : 15 : 13$
     - $(8, -12)$
     - $\left(-\frac{15}{14}\right)\left(\frac{13}{15}\right)\left(-\frac{14}{13}\right) = 1$

4. **Spread Ceva's Theorem**: On ``X(1)``, :func:`~geometor.ceva.static_barycentrics.verify_spread_ceva` computes the six exact vertex spreads over $\mathbb{Q}$ ($s(\angle BAD) = s(\angle DAC) = \frac{16}{65}$, $s(\angle CBE) = s(\angle EBA) = \frac{4}{13}$, $s(\angle ACF) = s(\angle FCB) = \frac{1}{5}$), confirming unit spread product and unit quadrance product with zero square roots.
