:layout: book
:order: 2
:canonical_id: liber_primus
:breadcrumb_title: Book I
:folio: 0018
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _unit-2-liber-primus-ceva-menelaus:
.. _unit-2-liber-primus-ceva-menelaus-en:
.. _liber-primus:
.. _liber-primus-en:

Book I · Axioms, Ceva, Menelaus & 3D Statics (pp. 1–44)
=======================================================

.. rubric:: *Original GEOMETOR English translation from Giovanni Ceva's De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`, *Liber Primus*, pp. 1–44; Scans 0018–0061; `Tab. 1–3, Figs. 1–31`).

.. folio:: 0018
   :page: 1

1. Axiomata, Petitio & Archimedean Lemmata (pp. 1–2)
----------------------------------------------------

Ceva erects his static calculus upon two self-evident **Axioms**, one **Postulate (*Petitio*)**, and two **Archimedean Lemmas** (:cite:`Equiponderants I.6–7 <archimedes:equipond>`):

* **Axioma I**: Every system of heavy bodies possesses a single, unique :term:`center of gravity <centrum-gravitatis>` (*centrum gravitatis unicum*).
* **Axioma II**: The common center of gravity of two weights lies upon the straight segment joining their individual centers, and the combined weight acts at that fulcrum exactly as if both masses were concentrated there (`A † B`).
* **Petitio (Postulate)**: One may freely place arbitrary positive—or analytically signed—weights at any given geometric vertices so as to bring a given dividing point into static equilibrium.
* **Lemmata I & II** (`Tab. 1, Figs. 1–3`): Along a straight lever :g:`AB`, weights :g:`mA` ($u$) suspended at :g:`A` and :g:`mB` ($v$) suspended at :g:`B` balance around fulcrum :g:`F` if and only if their magnitudes stand inversely as their lever arms (:term:`momentum ponderis <momentum-ponderis>`):

  $$u : v = \overline{BF} : \overline{FA} \qquad \Longleftrightarrow \qquad \frac{\overline{AF}}{\overline{FB}} = \frac{v}{u}.$$

.. picture:: /_static/figures/fig01_statica_lever_elements.svg
   :alt: Archimedes Law of the Lever and Ceva Elementum II Three-Weight Triangle Equilibrium

2. *Elementa I–III* & the p. 5 *Scholium* on Negative Weights ``F - A`` (pp. 2–5)
---------------------------------------------------------------------------------

With effortless economy, Ceva derives three foundational configurations:

1. ***Elementum I* — Static Menelaus Sector (`Tab. 1, Fig. 4`)**: When two transversals cut across the sides of an angle (the planar sector of :person:`Menelaus <menelaus>` and :person:`Ptolemy <ptolemy>`), placing two weights at the base and grouping them in two ways immediately equates the common fulcrum on the intersection ray.
2. ***Elementum II* — Interior Cevian Concurrency (`Tab. 1, Fig. 5`)**: On triangle :g:`ABC`, let cevians :g:`AD` and :g:`BE` meet inside the triangle at :g:`P`. Place weights $u$ at :g:`A`, $v$ at :g:`B`, and $w$ at :g:`C` chosen so that $v : w = \overline{DC} : \overline{BD}$ (making :g:`D` the fulcrum of $B$ and $C$ with combined load ``v † w``) and $w : u = \overline{EA} : \overline{CE}$ (making :g:`E` the fulcrum of $C$ and $A$ with load ``w † u``). By *Axioma I*, the global center of gravity of all three masses (`u † v † w`) must lie simultaneously on :g:`AD` and on :g:`BE`—hence **at their unique intersection** :g:`P`! Grouping $A$ and $B$ first at their fulcrum :g:`F` on $AB$ ($\overline{AF} : \overline{FB} = v : u$), the line :g:`CF` joining $C$ to fulcrum :g:`F` must *also* pass through the global center :g:`P`. Thus all three cevians :g:`AD`, :g:`BE`, :g:`CF` concur at :g:`P`, and multiplying the three lever ratios eliminates the weights identically:

   $$\frac{\overline{AF}}{\overline{FB}} \cdot \frac{\overline{BD}}{\overline{DC}} \cdot \frac{\overline{CE}}{\overline{EA}} = \frac{v}{u} \cdot \frac{w}{v} \cdot \frac{u}{w} = 1.$$

3. ***Elementum III* & p. 5 *Scholium* — Analytic Negative Weights (`Tab. 1, Fig. 6`)**: What if the concurrency point :g:`J_A` lies **outside** triangle :g:`ABC`, so that one cevian :g:`AD` cuts side $BC$ internally at :g:`D` while :g:`BE` and :g:`CF` cut sides $CA$ and $AB$ **externally** at :g:`E' <E_ext>` and :g:`F' <F_ext>`? In a historic conceptual breakthrough on printed page 5, Ceva introduces :term:`algebraic negative weights <pondus-negativum>`:

   *"And this weight $L$, in the analytic or algebraic manner, we shall write thus: $F - A$, that is, $F$ minus $A$."*

.. picture:: /_static/figures/fig02_ceva_interior_exterior.svg
   :alt: Caravaggio Parallel-Line Euclidean Proof vs Ceva Exterior Negative Weight Concurrency

By assigning weight $-u$ at :g:`A` alongside $+v$ at :g:`B` and $+w$ at :g:`C`, two of the directed side ratios become negative while the third remains positive, preserving the exact signed product $(-)\cdot(+)\cdot(-) = +1$ and anticipating :person:`August Ferdinand Möbius's <moebius>` *Der barycentrische Calcul* (:cite:`1827 <moebius:1827:barycentr>`) by nearly a century and a half!

3. *Elementa IV–V* & the 3D Skew Quadrilateral *Corollarium* (pp. 5–7)
----------------------------------------------------------------------

Extending four weights $(m_A, m_B, m_C, m_D)$ around a four-sided cycle $ABCD$ (*Elementa IV–V*, `Tab. 1, Figs. 7–8`), Ceva proves that if consecutive sides are divided in cyclic ratio product $1$, the lines joining opposite fulcrums intersect at the global center of gravity $O$. In a remarkable spatial *Corollarium* (pp. 6–7), Ceva observes that **even when the quadrilateral does not lie in a single plane** (:term:`skew quadrilateral <quadrilaterum-non-planum>`, *"licet prædictum sic sectum quadrilaterum non in eodem plano iaceat"*), the four spatial fulcrums remain strictly **coplanar** because the two opposite-edge lever joins both pass through the unique 3D center of gravity $O$!

4. Proposition VI — Caravaggio Jr.'s Pure Euclidean Proof (`Tab. 1, Fig. 10`)
-----------------------------------------------------------------------------

Lest strict Euclidean purists object to importing mechanical weights into pure geometry, :person:`Giovanni Ceva <ceva>` pauses at **Proposition VI** (pp. 7–8) to record an elegant synthetic demonstration communicated by his young Milanese colleague :person:`Pietro Paolo Caravaggio Jr. <caravaggio>` (*"Petrus Paulus Carauaggius Petri Pauli filius præceptoris sui"*, son of Ceva's Milanese teacher Pietro Paolo Caravaggio Sr.):

Through vertex :g:`A` of triangle :g:`ABC`, draw a straight line parallel to base $BC$, meeting the extended cevians $CF$ and $BE$ at $K$ and $L$ (as illustrated in the left panel of Figure 2). By :person:`Euclid's <euclid>` similar triangles (:just:`VI.4`):

1. From $\triangle AKF \sim \triangle BCF$ and $\triangle ALE \sim \triangle CBE$:

   $$\frac{\overline{AF}}{\overline{FB}} = \frac{\overline{AK}}{\overline{BC}}, \qquad \frac{\overline{CE}}{\overline{EA}} = \frac{\overline{BC}}{\overline{AL}}.$$

2. Since :g:`AD` passes through the concurrency point :g:`P` of $BE$ and $CF$, the central ray from $P$ projects $KL$ onto $BC$: $\triangle AKP \sim \triangle DCP$ and $\triangle ALP \sim \triangle DBP$, yielding:

   $$\frac{\overline{BD}}{\overline{DC}} = \frac{\overline{AL}}{\overline{AK}}.$$

Multiplying the three proportions cancels $\overline{AK}$, $\overline{BC}$, and $\overline{AL}$ pairwise, proving $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$ by pure Book VI geometry!

5. Propositions VII–VIII & Lemma IV — Compound Ratios, Menelaus & Harmonic Ranges (pp. 8–12)
--------------------------------------------------------------------------------------------

In **Lemma IV** and **Propositions VII–VIII** (pp. 8–12, `Tab. 1, Figs. 11–12`), Ceva cites :person:`Federico Commandino <commandino>` and :person:`Christoph Clavius <clavius>` (:cite:`1589 <clavius:1589:euclides>`) on the algebra of :term:`compound ratios <ratio-composita>` (*ratio ex rationibus composita*) to state both **Ceva's Theorem** and its converse, side-by-side with a two-lever static demonstration of :person:`Menelaus's <menelaus>` **Transversal Theorem** (:cite:`Sphaerica III.1 <menelaus:sphaerica>`):

* **Proposition VII (Ceva's Concurrency & Converse)**: In triangle :g:`ABC`, three :term:`cevians <ceviana>` :g:`AD`, :g:`BE`, :g:`CF` concur at a finite (or ideal parallel) point :g:`P` if and only if the ratio compounded of $(AF : FB)$, $(BD : DC)$, and $(CE : EA)$ is the ratio of equality ($1 : 1$). For if $AD$ and $BE$ meet at $P$, and $CP$ meets $AB$ at $F^*$, then $(AF^* / F^*B) \cdot (BD / DC) \cdot (CE / EA) = 1 = (AF / FB) \cdot (BD / DC) \cdot (CE / EA)$, whence $AF^* / F^*B = AF / FB$ and $F^* = F$ (:just:`V.9`).
* **Proposition VIII (Menelaus's Transversal & Projective Harmonic Division)**: Let the straight transversal :g:`EF` joining two cevian feet :g:`E` and :g:`F` be produced until it cuts the extended base :g:`lineBC` externally at :g:`D' <D_prime>`. Viewing $\triangle ABC$ cut by transversal :g:`EF`, static moments equate the unsigned ratio product to $1$, or with signed orientation:

  $$\frac{\overline{AF}}{\overline{FB}} \cdot \frac{\overline{BD'}}{\overline{D'C}} \cdot \frac{\overline{CE}}{\overline{EA}} = -1.$$

.. picture:: /_static/figures/fig03_menelaus_harmonic_quadrangle.svg
   :alt: Ceva Props VII and VIII Concurrent Cevians and Menelaus Transversal Harmonic Range

Dividing Ceva's equation by Menelaus's equation immediately yields **projective harmonic division** (:term:`sectio harmonica <sectio-harmonica>`):

$$\frac{\overline{BD}}{\overline{DC}} = -\frac{\overline{BD'}}{\overline{D'C}} \qquad \Longleftrightarrow \qquad (B, C; D, D') = -1.$$

Thus every concurrent cevian triad $(AD, BE, CF)$ automatically constructs the projective harmonic conjugate :g:`D' <D_prime>` of :g:`D` with respect to :g:`B` and :g:`C` using a **straightedge alone**!

6. Propositions IX–XXII — Canonical Triangle Centers & Spread Ceva (pp. 12–35)
------------------------------------------------------------------------------

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

7. Propositions XXIII–XXVI — The Seven-Line Tetrahedron Equilibrium (pp. 36–43)
-------------------------------------------------------------------------------

Crowning *Liber Primus* (`Tab. 3, Figs. 28–31`), :person:`Giovanni Ceva <ceva>` ascends from the plane into three-dimensional solid geometry. Suppose four arbitrary non-zero weights $(m_A, m_B, m_C, m_D)$ are placed at the four vertices :g:`A`, :g:`B`, :g:`C`, :g:`D` of a solid tetrahedron :g:`ABCD <tetABCD>`. By associative static grouping, the global spatial center of gravity :g:`O` can be reached in **seven distinct ways**:

1. **Four Spatial Vertex-to-Face Cevians**: First combine any three vertices on their triangular face—yielding the four static face centers of gravity :g:`G_A` on $\triangle BCD$, :g:`G_B` on $\triangle ACD$, :g:`G_C` on $\triangle ABD$, and :g:`G_D` on $\triangle ABC$—and then join each face center to the remaining opposite vertex (:g:`AG_A`, :g:`BG_B <AG_B>`, :g:`CG_C <AG_C>`, :g:`DG_D <AG_D>`). Every one of these four spatial rays divides at :g:`O` in exact ratio $\overline{VO} : \overline{OG_V} = (m_{\text{tot}} - m_V) : m_V$ (for equal weights $1:1:1:1$, the classic $3 : 1$ tetrahedral centroid ratio of :person:`Commandino <commandino>`, :cite:`1565 <commandino:1565:centro>`).
2. **Three Skew-Edge Bimedians**: Alternatively, pair the four vertices into two opposite skew edges—$(AB, CD)$, $(AC, BD)$, or $(AD, BC)$—balancing each edge at its lever fulcrum (:g:`E_AB` with :g:`E_CD`, :g:`E_AC` with :g:`E_BD`, and :g:`E_AD` with :g:`E_BC`). Then the three straight segments (:g:`B_AB_CD`, :g:`B_AC_BD`, :g:`B_AD_BC`) joining opposite skew-edge fulcrums **also pass through the exact same point** :g:`O`!

.. picture:: /_static/figures/fig07_tetrahedron_seven_lines.svg
   :alt: Ceva Liber Primus Prop XXIII 3D Tetrahedron Seven-Line Static Equilibrium at Center O

Marveling at this simultaneous spatial intersection of **seven** lines in three-space, Ceva exclaims that all seven rays meet at :g:`O` *"mira quadam concordia"*—with a :term:`wondrous concord <concordia-septem-linearum>`! In **Propositions XXIV–XXVI**, Ceva extends the same barycentric decomposition to quadrangular and polygonal pyramids.

.. toctree::
   :hidden:

   la
   summary
   notes
