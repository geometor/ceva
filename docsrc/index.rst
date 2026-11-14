:title: GEOMETOR • ceva

GEOMETOR • ceva
================

.. rubric:: Giovanni Ceva's *De Lineis Rectis* (Milan, 1678) — Static Barycentrics, Cevian Concurrency & Digital Codex

.. epigraph::

   *Substitutisque linearum vice ponderibus... nulla adhibita circulorum, linearumque præuia constructione, quæ ad linearum se se intersecantium symptomata spectant, solis ponderibus staticè enodare. Hinc staticam constructionem libuit appellare.*

   *Having substituted weights in place of straight lines... with no prior construction of circles and auxiliary lines employed, I resolved statically—by weights alone—the properties pertaining to mutually intersecting straight lines. Hence I was pleased to call it a Static Construction.*

   — :person:`Giovanni Ceva <ceva>`, *De lineis rectis se invicem secantibus statica constructio*, Prooemium (:cite:`Milan, 1678 <ceva:1678:dlr>`)

Overview
--------

**GEOMETOR Ceva** (``geometor-ceva``) unites a **4-Track Bilingual Digital Scriptorium Book Codex** (`English`, `Latin`, `Summary`, `Notes`) with **100% exact symbolic SymPy / ``geometor.model`` constructions and proofs** for :person:`Giovanni Ceva's <ceva>` (1647–1734) landmark quarto treatise *De lineis rectis se invicem secantibus statica constructio* (:cite:`Milan: Ludovico Monza, 1678 <ceva:1678:dlr>`):

1. ***Liber Primus* — Static Foundations, Negative Weights (`F - A`), Ceva & Menelaus**: Dedicating the work to :person:`Ferdinando Carlo Gonzaga <gonzaga>` and honoring his Pisan mentor :person:`Donato Rossetti <rossetti>`, Ceva replaces auxiliary Euclidean lines with :person:`Archimedes' <archimedes>` Law of the Lever ($u \cdot \overline{AF} = v \cdot \overline{FB}$). He proves **Menelaus's Transversal Theorem** (*Elementum* I, *Prop.* VIII), **Ceva's Concurrency Theorem** $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1$ (*Elementum* II, *Prop.* VII), introduces **algebraic negative weights** (*"pondus... more analytico, seu algebrico ita scribemus $F - A$"*, *Elementum* III & p. 5 *Scholium*) 149 years before :person:`Möbius <moebius>`, preserves :person:`Pietro Paolo Caravaggio Jr.'s <caravaggio>` pure Euclidean parallel-line proof (*Prop.* VI), and establishes **3D skew-quadrilateral** (*Elementum* V *Coroll.*) and **tetrahedral 7-line concurrency** (*Prop.* XXIII, *"mira quadam concordia"*).
2. ***Liber Secundus* — Circumscribed Conics, Isotomic Conjugates & Odd Polygons**: Using :person:`Serenus <serenus>` and :person:`Borelli's <borelli>` cylindrical projection (*Lemma* I), Ceva proves contact-ratio invariance on circles and ellipses, discovers the concurrency of incircle/inellipse contact cevians (*Prop.* I, anticipating :person:`Gergonne <gergonne>` $X(7)$) and its **isotomic conjugate** (*Prop.* I *Corollarium*, anticipating :person:`Nagel <nagel>` $X(8)$), and generalizes cevian concurrency to arbitrary **odd $(2m + 1)$-gons**.
3. ***Appendix Geometrica* — Pure Area Ratios, Ungula Cubature & Indivisibles Caution**: Dispensing with mechanics altogether, Ceva re-grounds ratio geometry in pure Euclidean triangle areas ($[\triangle PAB] / [\triangle PAC] = BD / DC$), squares Hippocratean lunes (*Prop.* II), cubes the cylindrical *ungula* as $\frac{2}{3}$ of its circumscribed prism (*Prop.* VII), establishes the $5 : 3$ hemisphere centroid (*Prop.* XIII, praising :person:`Luca Valerio <valerio>`) and $2 : 1$ paraboloid centroid (*Prop.* XIV, citing :person:`Evangelista Torricelli <torricelli>`), and closes with his celebrated **caution on Cavalieri's indivisibles** on curved surfaces.

----

Book Codex & Repository Architecture
------------------------------------

* :doc:`Book Codex: On Straight Lines Mutually Intersecting (De Lineis Rectis, 1678) <de_lineis_rectis/index>`: Four multi-track units pairing original GEOMETOR English translations with folio-verified 1678 Neo-Latin primary texts, executive geometric summaries, scholarly commentary, interactive ``.euclid-graphic`` SVG plates, and linked scholarly apparatus (:doc:`People </de_lineis_rectis/persons>`, :doc:`Bibliography </de_lineis_rectis/bibliography>`, :doc:`Concordance <de_lineis_rectis/concordance>`, :doc:`Glossary <de_lineis_rectis/glossary>`).
* :doc:`Using This Edition (Reader's Guide & CLI) <usage/index>`: Interactive reading tracks, BNCF Florence primary folios, SVG diagram links, full-text search, and command-line usage.
* :doc:`Exact Symbolic Demonstrations <demos/index>`: Pure-symbolic Python scripts (`Model(..., auto_intersect=False)`) free of floating-point coordinates, verifying canonical centers $X(1), X(2), X(4), X(6), X(7), X(8), J_A$ over $\mathbb{Q}$, harmonic ranges $(B, C; D, D') = -1$, **Spread Ceva's Theorem**, pentagonal concurrency, 3D 7-line tetrahedral equilibrium, and *Appendix* integrals.
* :doc:`Python Package Reference <modules/index>`: Documented symbolic modules in ``geometor.ceva`` (`static_barycentrics`, `polygon_tetrahedron`, `sphinx_ext`, `__main__`).
* :doc:`Curation Log <log/index>`: Chronological transcription, translation, and verification records.
* :doc:`About This Edition <about/index>`: Provenance, historical context, and editorial conventions.

.. toctree::
   :maxdepth: 2
   :hidden:

   de_lineis_rectis/index
   de_lineis_rectis/persons
   de_lineis_rectis/bibliography
   about/index
   usage/index
   demos/index
   log/index
   modules/index
