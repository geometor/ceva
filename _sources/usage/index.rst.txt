:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Interactive Features & Reader's Guide to Giovanni Ceva's *De Lineis Rectis*

Welcome to the **GEOMETOR Digital Scriptorium** edition of :person:`Giovanni Ceva's <ceva>` foundational treatise, *De lineis rectis se invicem secantibus statica constructio* (Milan: Ludovico Monza, 1678). This edition unites Archimedean statics, classical Euclidean deduction, and modern barycentric and projective geometry in an interactive bilingual codex with exact symbolic verifications.

Interactive Reader Features
---------------------------

1. Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every unit in the :doc:`Book Codex </de_lineis_rectis/index>` is published as a 4-track bilingual edition accessible via the companion track switcher bar:

* **English**: Authoritative English translation prepared directly from Ceva's Neo-Latin for GEOMETOR, paired with calibrated interactive ``.euclid-graphic`` SVGs.
* **Latin**: Diplomatic transcription of the 1678 Milan *editio princeps*, preserving historical typography such as the printer's obelus/dagger ``†`` for static weight composition (:term:`A † F <obelus-additio>`) and minus signs for exterior lever fulcrums (:term:`F - A <pondus-negativum>`).
* **Summary**: Executive summaries condensing each proposition, cevian ratio product, and barycentric invariant.
* **Notes**: Scholarly commentary detailing Archimedean mechanical foundations, projective harmonic conjugates $(B, C; D, D') = -1$, and connections to Euclid, Menelaus, and modern triangle geometry.

2. Primary-Source Folio Milestones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Marginal folio links (e.g., ``[p. 1]``, ``[p. 5]``, ``[p. 26]``) record the exact page boundaries of the 1678 Milan imprint (`Printed page N = PDF scan page N + 17`). Clicking these marginal links or the header **Folio** badge opens the archival scans from the Biblioteca Nazionale Centrale di Firenze (exemplar ``ita-bnc-mag-00001346-001``), allowing direct verification of Ceva's text and original folding plates (Tab. 1–10).

3. Interactive Diagrams & Deductive Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every figure across the four units is rendered natively as an interactive SVG:

* **Barycentric & Static Highlighting**: Hovering over or clicking geometric entities pulses corresponding segments, points, and weight distributions in the diagram.
* **Exact Symbolic Verification**: All constructions are computed in :mod:`geometor.ceva` using exact rational arithmetic over $\mathbb{Q}$ (such as the canonical Heronian triangle $(13, 14, 15)$ with vertices $A = (5, 12), B = (0, 0), C = (14, 0)$), ensuring zero floating-point approximation error.

4. Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The search box in the sidebar indexes all four reading tracks and apparatus documents. Search results append ``?highlight=`` parameters to document URLs, highlighting matching terms directly inside propositions, proofs, and historical notes.

5. Categories, Tags, Document Types & Collection Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sidebar provides structured faceted navigation:

* **Categories & Tags**: Explore by mathematical domain (*statics*, *levers*, *ceva-theorem*, *menelaus*, *harmonic-division*, *tetrahedron*, *quadrature*).
* **Document Types**: Filter pages by content type (*treatise*, *unit*, *demos*, *biography*, *log*).
* **Collection Views**: Collection index pages offer view toggles between **Cards**, **Banners**, and **List** modes.

6. People, Bibliography & Glossary Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Prosopographical Hover Cards**: Links marked with ``:person:`` (e.g., :person:`Giovanni Ceva <ceva>`, :person:`Tommaso Ceva <tommaso-ceva>`, :person:`Archimedes <archimedes>`, :person:`Pietro Paolo Caravaggio Jr. <caravaggio>`) provide instant biographical summaries and direct links to the :doc:`People </de_lineis_rectis/persons>` register.
* **Bibliographic Citations**: Citations formatted with ``:cite:`` link directly to the :doc:`Bibliography </de_lineis_rectis/bibliography>`.
* **Glossary Tooltips**: Technical terms linked with ``:term:`` provide instant definitions of Neo-Latin and projective vocabulary.
* **Light / Dark Theme**: Toggle visual themes using the control in the top navigation bar.

----

Command-Line & Python API
-------------------------

Command-Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``geometor.ceva`` CLI produces an exact symbolic ledger of canonical triangle centers, Spread Ceva invariants, odd-polygon products, and tetrahedral equilibria:

.. code-block:: bash

   # Display the full symbolic verification summary table
   python3 -m geometor.ceva

Python API
~~~~~~~~~~

Run exact static barycentric computations and verify geometric theorems:

.. code-block:: python

   from geometor.ceva import (
       CANONICAL_CENTERS,
       evaluate_canonical_centers,
       solve_tetrahedron_static_equilibrium,
       verify_odd_polygon_ceva,
       verify_spread_ceva,
   )

   # Evaluate canonical triangle centers on the Heronian (13, 14, 15) triangle
   centers = evaluate_canonical_centers()
   for code, res in centers.items():
       print(f"Center {code}: P={res.center}, Ceva Product={res.ceva_product}, Interior={res.is_interior}")

   # Verify radical-free Spread Ceva's Theorem
   spread_res = verify_spread_ceva()
   print("Spread Ceva verified:", spread_res.verified)

   # Solve 3D 7-line tetrahedral static equilibrium
   tet = solve_tetrahedron_static_equilibrium()
   print("Tetrahedral equilibrium center O:", tet.center_o)
