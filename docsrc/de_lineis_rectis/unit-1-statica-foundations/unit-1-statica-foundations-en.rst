.. _unit-1-statica-foundations-en:

Unit I · Dedication, Prooemium & Static Foundations (1678, pp. 1–7)
===================================================================

*Original GEOMETOR English translation from Giovanni Ceva's De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`, Frontmatter & *Liber Primus*, pp. 1–7; `Tab. 1, Figs. 1–8`).

1. Dedication to Ferdinando Carlo Gonzaga & Printer's Note on ``†``
-------------------------------------------------------------------

*"I should tremble, Most Serene Duke, to prefix such resplendent titles to this slender little book..."* Addressing :person:`Ferdinando Carlo Gonzaga <gonzaga>`, Duke of Mantua, Montferrat, and Guastalla, :person:`Giovanni Ceva <ceva>` declares that **Geometry—the Queen of all sciences (*scientiarum omnium Regina*)—loses all vigor and life whenever deprived of the sheltering shade of princely patrons (*Mæcenatum umbra*)**. Just as the House of Gonzaga fostered arts and letters across Lombardy, Ceva offers these geometric-mechanical meditations as the first fruits of his studies.

Immediately preceding *Liber Primus* (`PDF p. 17`), Milanese printer :person:`Ludovico Monza <monza>` inserts an essential typographic notice (*Typographus Lectori*): whenever two static weights are compounded into a single fulcrum load, the press prints the :term:`obelus or dagger † <obelus-additio>` in place of the plus sign—writing ``A † F`` for *A plus F* ($A + F$)—paired with the analytic minus sign ``-`` in ``F - A`` (*F minus A*, $F - A$) whenever a weight acts subtractively.

2. Prooemium — Cured by Cavalieri, Enamored of Static Construction
------------------------------------------------------------------

In his *Prooemium ad Lectorem*, Ceva recounts his youthful wonder upon reading :person:`Euclid <euclid>`, :person:`Archimedes <archimedes>`, :person:`Apollonius <apollonius>`, and :person:`Pappus <pappus>`. Like many ardent beginners, he confesses he once wasted stubborn hours attempting the quadrature of the circle—until a deeper study of *"the indivisibles of Cavalieri"* (:person:`Bonaventura Cavalieri <cavalieri>`, :cite:`1635 <cavalieri:1635:indivis>`) cured him of that vain obstinacy by revealing the true nature of curvilinear ratios.

Turning to configurations of mutually intersecting straight lines in triangles, polygons, and solids, Ceva discovered an unexpected royal road:

   *"Having substituted weights in place of straight lines... with no prior construction of circles and auxiliary lines employed, I was able to untie statically—by weights alone—all the properties pertaining to mutually intersecting straight lines. Hence I was pleased to call this method a :term:`Static Construction <statica-constructio>`."*

Before opening the demonstrations, Ceva pays affectionate tribute to his revered teacher at the University of Pisa, :person:`Donato Rossetti <rossetti>`, Canon of Livorno, mourning Rossetti's departure from Tuscany to the court of Turin while crediting his Pisan lectures for kindling this synthesis of mechanics and pure geometry.

3. *Liber Primus* — Axiomata, Petitio & Archimedean Lemmata (pp. 1–2)
---------------------------------------------------------------------

Ceva erects his static calculus upon two self-evident **Axioms**, one **Postulate (*Petitio*)**, and two **Archimedean Lemmas** (:cite:`Equiponderants I.6–7 <archimedes:equipond>`):

* **Axioma I**: Every system of heavy bodies possesses a single, unique :term:`center of gravity <centrum-gravitatis>` (*centrum gravitatis unicum*).
* **Axioma II**: The common center of gravity of two weights lies upon the straight segment joining their individual centers, and the combined weight acts at that fulcrum exactly as if both masses were concentrated there (`A † B`).
* **Petitio (Postulate)**: One may freely place arbitrary positive—or analytically signed—weights at any given geometric vertices so as to bring a given dividing point into static equilibrium.
* **Lemmata I & II** (`Tab. 1, Figs. 1–3`): Along a straight lever :g:`AB`, weights :g:`mA` ($u$) suspended at :g:`A` and :g:`mB` ($v$) suspended at :g:`B` balance around fulcrum :g:`F` if and only if their magnitudes stand inversely as their lever arms (:term:`momentum ponderis <momentum-ponderis>`):

  $$u : v = \overline{BF} : \overline{FA} \qquad \Longleftrightarrow \qquad \frac{\overline{AF}}{\overline{FB}} = \frac{v}{u}.$$

.. picture:: /_static/figures/fig01_statica_lever_elements.svg
   :alt: Archimedes Law of the Lever and Ceva Elementum II Three-Weight Triangle Equilibrium

4. *Elementa I–III* & the p. 5 *Scholium* on Negative Weights ``F - A`` (pp. 2–5)
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

5. *Elementa IV–V* & the 3D Skew Quadrilateral *Corollarium* (pp. 5–7)
----------------------------------------------------------------------

Extending four weights $(m_A, m_B, m_C, m_D)$ around a four-sided cycle $ABCD$ (*Elementa IV–V*, `Tab. 1, Figs. 7–8`), Ceva proves that if consecutive sides are divided in cyclic ratio product $1$, the lines joining opposite fulcrums intersect at the global center of gravity $O$. In a remarkable spatial *Corollarium* (pp. 6–7), Ceva observes that **even when the quadrilateral does not lie in a single plane** (:term:`skew quadrilateral <quadrilaterum-non-planum>`, *"licet prædictum sic sectum quadrilaterum non in eodem plano iaceat"*), the four spatial fulcrums remain strictly **coplanar** because the two opposite-edge lever joins both pass through the unique 3D center of gravity $O$!
