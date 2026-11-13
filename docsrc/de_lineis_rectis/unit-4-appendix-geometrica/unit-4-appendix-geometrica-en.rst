.. _unit-4-appendix-geometrica-en:

Unit IV · Appendix Geometrica: Area Ratios, Ungula, Centroids & Indivisibles (pp. 73–104)
=========================================================================================

*Original GEOMETOR English translation from Giovanni Ceva's De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`, *Appendix Geometrica*, pp. 73–104; `Tab. 8–10, Figs. 62–85`).

1. Pure Synthetic Area-Ratio Proofs Free of Mechanics
-----------------------------------------------------

Opening the *Appendix Geometrica* (pp. 73–76, `Tab. 8, Figs. 62–64`), :person:`Giovanni Ceva <ceva>` fulfills a promise to strict classical geometers: every concurrency and proportion proved via static weights in *Libri I–II* can be demonstrated **purely synthetically without mechanics** by substituting **sub-triangle areas** for weights!

Indeed, if cevian $AD$ passes through an interior (or signed exterior) point $P$ of $\triangle ABC$ and meets side $BC$ at $D$, then by :person:`Euclid <euclid>` (:just:`VI.1` — triangles on bases $BD, DC$ sharing the same vertex have areas proportional to those bases):

$$\frac{[\triangle ABD]}{[\triangle ACD]} = \frac{\overline{BD}}{\overline{DC}}, \qquad \frac{[\triangle PBD]}{[\triangle PCD]} = \frac{\overline{BD}}{\overline{DC}}.$$

Subtracting numerator from numerator and denominator from denominator (:just:`V.19`) immediately yields the **fundamental barycentric area identity**:

$$\frac{[\triangle PAB]}{[\triangle PAC]} = \frac{\overline{BD}}{\overline{DC}}, \qquad \frac{[\triangle PBC]}{[\triangle PAB]} = \frac{\overline{CE}}{\overline{EA}}, \qquad \frac{[\triangle PAC]}{[\triangle PBC]} = \frac{\overline{AF}}{\overline{FB}}.$$

Multiplying these three ratios telescopes the three sub-triangle areas identically to $1$:

$$\frac{\overline{AF}}{\overline{FB}} \cdot \frac{\overline{BD}}{\overline{DC}} \cdot \frac{\overline{CE}}{\overline{EA}} = \frac{[\triangle PAC]}{[\triangle PBC]} \cdot \frac{[\triangle PAB]}{[\triangle PAC]} \cdot \frac{[\triangle PBC]}{[\triangle PAB]} = 1.$$

Thus Ceva's static vertex weights $(u : v : w)$ are canonically isomorphic to the signed oriented sub-triangle areas $([\triangle PBC] : [\triangle PCA] : [\triangle PAB])$!

2. Lune Quadrature (*Prop.* II) & Cylindrical *Ungula* Cubature (*Prop.* VII)
-----------------------------------------------------------------------------

Continuing through curvilineal and solid geometry (`Tab. 8–9`), Ceva establishes a suite of classical and Galilean quadratures and cubatures:

* **Proposition II — Hippocratean Lune Quadrature**: Over an isosceles right triangle :g:`triABC` of legs $R$ and hypotenuse $R\sqrt{2}$, the crescent :g:`lune` bounded between the semicircle :g:`arcHyp` on the hypotenuse (radius $R/\sqrt{2}$, area $\frac{1}{4}\pi R^2$) and the quadrant arc :g:`arcQuad` from the right-angle vertex (sector area $\frac{1}{4}\pi R^2$) equals the rectilinear right triangle :g:`triABC` itself:

  $$[\text{Lune}] = \frac{1}{4}\pi R^2 - \left(\frac{1}{4}\pi R^2 - \frac{1}{2}R^2\right) = \frac{1}{2}R^2 = [\triangle ABC],$$

  following :person:`Hippocrates of Chios <hippocrates>` via :just:`XII.2` without any transcendental remainder.
* **Proposition VII — Cubature of the Cylindrical Hoof (*Ungula*)**: Let a right circular cylinder of base radius $R$ and altitude $H$ be cut obliquely by a plane passing through a diameter of the base (`Tab. 8–9`), detaching a :term:`cylindrical ungula <ungula-cylindrica>` :g:`ungula` inscribed inside a right-triangular :g:`prism` of base $2R \times R$ and height $H$ ($\text{Vol}_{\text{prism}} = R^2 H$). Slicing parallel to the cylinder's axis and perpendicular to the diameter produces similar right-triangular cross-sections :g:`sliceTri` of base $\sqrt{R^2 - x^2}$ and height $\frac{H}{R}\sqrt{R^2 - x^2}$, whose area $\frac{H}{2R}(R^2 - x^2)$ integrates (by :person:`Archimedes' <archimedes>` parabolic exhaustion) to:

  $$\operatorname{Vol}(\text{Ungula}) = \frac{2}{3} R^2 H = \frac{2}{3} \operatorname{Vol}(\text{Circumscribed Prism}).$$

.. picture:: /_static/figures/fig08_appendix_ungula_indivisibles.svg
   :alt: Ceva Appendix Geometrica Hippocratean Lune Cylindrical Ungula and Indivisibles Caution

3. Solid Centroids: Valerio's $5:3$ Hemisphere (*Prop.* XIII) & Torricelli's $2:1$ Conoid
-----------------------------------------------------------------------------------------

Turning to solid centers of gravity (`Tab. 9–10`), Ceva salutes two giants of the Italian school:

* **Proposition XIII — Center of Gravity of the Hemisphere ($5 : 3$)**: Along the symmetry axis :g:`axisVO` of a solid hemisphere :g:`hemi` from pole $V$ ($z = 0$) to base center $O$ ($z = R$), the center of gravity :g:`cgH` divides the axis in the exact ratio **$5 : 3$** ($\bar{z} = \frac{5}{8} R$ from the vertex, $\frac{3}{8} R$ above the equatorial base). Ceva hails :person:`Luca Valerio <valerio>` (:cite:`1604 <valerio:1604:centro>`) as *"subtilissimus nostri æui Archimedes"* (*"the most subtle Archimedes of our age"*).
* **Proposition XIV & Hyperbolic Solids — Tribute to Torricelli**: For a parabolic conoid of revolution of altitude $H$, the center of gravity divides the axis from vertex to base in the exact ratio **$2 : 1$** ($\bar{z} = \frac{2}{3} H$), while :person:`Evangelista Torricelli's <torricelli>` (:cite:`1644 <torricelli:1644:opera>`) acute infinite hyperbolic solid possesses a **finite** volume despite extending infinitely along its asymptote.

4. Closing Caution & Paradox on Cavalieri's Indivisibles (pp. 100–104)
----------------------------------------------------------------------

In the celebrated closing pages of the *Appendix Geometrica*, Ceva—who had praised :person:`Bonaventura Cavalieri <cavalieri>` in the *Prooemium*—issues a razor-sharp **methodological warning** (:term:`indivisibilia & slant frustum <indivisibilia-cautio>`):

Suppose one slices a hemisphere :g:`hemi` (or cone) by equidistant parallel planes (:g:`chordSlice`) of spacing $dz$ and naively equates the **curved surface area** to the sum of the parallel circular circumferences $2\pi r(z)\,dz$. For a hemisphere $r(z) = \sqrt{R^2 - u^2}$, that naive integral $\int_0^R 2\pi\sqrt{R^2 - u^2}\,du = \frac{\pi^2}{2} R^2$ **falsely disagrees** with Archimedes' true surface area $2\pi R^2$ (*On the Sphere and Cylinder* I.33)! Why? Because on a curved or oblique surface, an infinitesimal band between parallel planes is a **conical frustum** whose slant generator :g:`slantArc` has length $ds = \frac{du}{\cos\alpha} = \frac{R}{\sqrt{R^2 - u^2}}\,du$, so the true surface element is:

$$2\pi r(u)\,ds = 2\pi \sqrt{R^2 - u^2} \cdot \frac{R}{\sqrt{R^2 - u^2}}\,du = 2\pi R\,du \implies \int_0^R 2\pi R\,du = 2\pi R^2!$$

Without Archimedean frustum slant correction, Ceva concludes, **parallel indivisibles are treacherous on curved surfaces**, even where they succeed brilliantly for planar areas and solid volumes!
