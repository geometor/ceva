.. _unit-2-liber-primus-ceva-menelaus-en:

Unit II · Liber Primus Props. VI–XXII: Ceva, Menelaus & Spread Ceva (pp. 7–35)
==============================================================================

*Original GEOMETOR English translation from Giovanni Ceva's De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`, *Liber Primus*, Props. VI–XXII, pp. 7–35; `Tab. 1–3, Figs. 9–27`).

1. Proposition VI — Caravaggio Jr.'s Pure Euclidean Proof (`Tab. 1, Fig. 10`)
-----------------------------------------------------------------------------

Lest strict Euclidean purists object to importing mechanical weights into pure geometry, :person:`Giovanni Ceva <ceva>` pauses at **Proposition VI** (pp. 7–8) to record an elegant synthetic demonstration communicated by his young Milanese colleague :person:`Pietro Paolo Caravaggio Jr. <caravaggio>` (*"Petrus Paulus Carauaggius Petri Pauli filius præceptoris sui"*, son of Ceva's Milanese teacher Pietro Paolo Caravaggio Sr.):

Through vertex :g:`A` of triangle :g:`ABC`, draw a straight line parallel to base $BC$, meeting the extended cevians $CF$ and $BE$ at $K$ and $L$ (as illustrated in the left panel of Figure 2 in Unit I). By :person:`Euclid's <euclid>` similar triangles (:just:`VI.4`):

1. From $\triangle AKF \sim \triangle BCF$ and $\triangle ALE \sim \triangle CBE$:

   $$\frac{\overline{AF}}{\overline{FB}} = \frac{\overline{AK}}{\overline{BC}}, \qquad \frac{\overline{CE}}{\overline{EA}} = \frac{\overline{BC}}{\overline{AL}}.$$

2. Since :g:`AD` passes through the concurrency point :g:`P` of $BE$ and $CF$, the central ray from $P$ projects $KL$ onto $BC$: $\triangle AKP \sim \triangle DCP$ and $\triangle ALP \sim \triangle DBP$, yielding:

   $$\frac{\overline{BD}}{\overline{DC}} = \frac{\overline{AL}}{\overline{AK}}.$$

Multiplying the three proportions cancels $\overline{AK}$, $\overline{BC}$, and $\overline{AL}$ pairwise, proving $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$ by pure Book VI geometry!

2. Propositions VII–VIII & Lemma IV — Compound Ratios, Menelaus & Harmonic Ranges
---------------------------------------------------------------------------------

In **Lemma IV** and **Propositions VII–VIII** (pp. 8–12, `Tab. 1, Figs. 11–12`), Ceva cites :person:`Federico Commandino <commandino>` and :person:`Christoph Clavius <clavius>` (:cite:`1589 <clavius:1589:euclides>`) on the algebra of :term:`compound ratios <ratio-composita>` (*ratio ex rationibus composita*) to state both **Ceva's Theorem** and its converse, side-by-side with a two-lever static demonstration of :person:`Menelaus's <menelaus>` **Transversal Theorem** (:cite:`Sphaerica III.1 <menelaus:sphaerica>`):

* **Proposition VII (Ceva's Concurrency & Converse)**: In triangle :g:`ABC`, three :term:`cevians <ceviana>` :g:`AD`, :g:`BE`, :g:`CF` concur at a finite (or ideal parallel) point :g:`P` if and only if the ratio compounded of $(AF : FB)$, $(BD : DC)$, and $(CE : EA)$ is the ratio of equality ($1 : 1$). For if $AD$ and $BE$ meet at $P$, and $CP$ meets $AB$ at $F^*$, then $(AF^* / F^*B) \cdot (BD / DC) \cdot (CE / EA) = 1 = (AF / FB) \cdot (BD / DC) \cdot (CE / EA)$, whence $AF^* / F^*B = AF / FB$ and $F^* = F$ (:just:`V.9`).
* **Proposition VIII (Menelaus's Transversal & Projective Harmonic Division)**: Let the straight transversal :g:`EF` joining two cevian feet :g:`E` and :g:`F` be produced until it cuts the extended base :g:`lineBC` externally at :g:`D' <D_prime>`. Viewing $\triangle ABC$ cut by transversal :g:`EF`, static moments equate the unsigned ratio product to $1$, or with signed orientation:

  $$\frac{\overline{AF}}{\overline{FB}} \cdot \frac{\overline{BD'}}{\overline{D'C}} \cdot \frac{\overline{CE}}{\overline{EA}} = -1.$$

.. picture:: /_static/figures/fig03_menelaus_harmonic_quadrangle.svg
   :alt: Ceva Props VII and VIII Concurrent Cevians and Menelaus Transversal Harmonic Range

Dividing Ceva's equation by Menelaus's equation immediately yields **projective harmonic division** (:term:`sectio harmonica <sectio-harmonica>`):

$$\frac{\overline{BD}}{\overline{DC}} = -\frac{\overline{BD'}}{\overline{D'C}} \qquad \Longleftrightarrow \qquad (B, C; D, D') = -1.$$

Thus every concurrent cevian triad $(AD, BE, CF)$ automatically constructs the projective harmonic conjugate :g:`D' <D_prime>` of :g:`D` with respect to :g:`B` and :g:`C` using a **straightedge alone**!

3. Propositions IX–XXII — Canonical Triangle Centers & Spread Ceva
------------------------------------------------------------------

Across **Propositions IX–XXII** (pp. 12–35, `Tab. 1–3, Figs. 13–27`), Ceva systematically harvests corollaries for parallel transversals, medians, perpendicular altitudes, angle bisectors, and proportional chord configurations. Evaluated over $\mathbb{Q}$ on the canonical Heronian $(13, 14, 15)$ triangle with vertices :g:`A` $= (5, 12)$, :g:`B` $= (0, 0)$, and :g:`C` $= (14, 0)$ ($\text{Area} = 84$, inradius $r = 4$), every classical center (:person:`Kimberling <kimberling>` *ETC*) possesses exact integer static weights $(u : v : w)$ and rational coordinates:

* **Incenter** :g:`X(1) <X1>` (*angle bisectors*, $u:v:w = a:b:c = 14:15:13$) at $(6, 4)$;
* **Centroid** :g:`X(2) <X2>` (*medians*, $1:1:1$) at $\left(\frac{19}{3}, 4\right)$;
* **Orthocenter** :g:`X(4) <X4>` (*altitudes*, $70:99:55$) at $\left(5, \frac{15}{4}\right)$;
* **Symmedian Point** :g:`X(6) <X6>` ($a^2:b^2:c^2 = 196:225:169$) at $\left(\frac{1673}{295}, \frac{1176}{295}\right)$;
* **Gergonne Contact Point** :g:`X(7) <X7>` (*Lib. II Prop. I*, $\frac{1}{s-a}:\frac{1}{s-b}:\frac{1}{s-c} = 24:28:21$) at $\left(\frac{414}{73}, \frac{288}{73}\right)$;
* **Nagel Point** :g:`X(8) <X8>` (*isotomic conjugate*, $s-a:s-b:s-c = 7:6:8$) at $(7, 4)$—lying with :g:`X(1) <X1>` $= (6, 4)$ and :g:`X(2) <X2>` $= \left(\frac{19}{3}, 4\right)$ along the horizontal Nagel line $y = 4$, while the exterior **$A$-Excenter** ``J_A`` ($-14:15:13$) lies at $(8, -12)$.

.. picture:: /_static/figures/fig05_spread_ceva_heronian.svg
   :alt: Canonical Rational Triangle Centers and Spread Ceva Theorem on Heronian 13-14-15 Triangle

Furthermore, in Rational Trigonometry (:cite:`Wildberger 2005 <wildberger:2005:divine>`), squaring the trigonometric form of Ceva's Theorem replaces transcendental sines with exact rational **vertex spreads** (:g:`sA`, :g:`sB`, :g:`sC`) and **quadrances** (:term:`Spread Ceva <spread-ceva>`):

$$\frac{s(\angle BAD)}{s(\angle DAC)} \cdot \frac{s(\angle CBE)}{s(\angle EBA)} \cdot \frac{s(\angle ACF)}{s(\angle FCB)} = 1, \qquad \frac{Q(AF)}{Q(FB)} \cdot \frac{Q(BD)}{Q(DC)} \cdot \frac{Q(CE)}{Q(EA)} = 1.$$
