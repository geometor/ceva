.. _unit-2-liber-primus-ceva-menelaus-notes:

Unit II · Historical & Mathematical Commentary
==============================================

1. Why Ceva Credited Pietro Paolo Caravaggio Jr. in Proposition VI
------------------------------------------------------------------

In seventeenth-century Milan, mathematics flourished around the Palatine Schools (*Scuole Palatine*) and the Jesuit Brera College (where Giovanni's brother :person:`Tommaso Ceva <tommaso-ceva>` taught). Pietro Paolo Caravaggio Sr. (1617–1688) held the chair of mathematics at the Palatine Schools, and his teenage prodigy son :person:`Pietro Paolo Caravaggio Jr. <caravaggio>` (1658–1723) later succeeded him. By explicitly naming Caravaggio Jr. for the Euclidean parallel-line proof of *Proposition* VI (`Tab. 1, Fig. 10`), Ceva accomplished a double rhetorical aim: honoring his Milanese teacher's family while proving beyond cavil that every theorem discovered via *Statica Constructio* possesses a rigorous, weight-free Euclidean counterpart.

2. Collinearity of $X(1), X(2), X(8)$ on the Nagel Line ($y = 4$)
-----------------------------------------------------------------

Notice a delightful arithmetic gem revealed by our exact Heronian $\triangle(13, 14, 15)$ table in ``geometor.ceva``:

* $X(1) = (6, 4)$,
* $X(2) = \left(\frac{19}{3}, 4\right)$,
* $X(8) = (7, 4)$.

All three points share the exact integer ordinate $y = 4$ (equal to the inradius $r = \frac{\Delta}{s} = \frac{84}{21} = 4$, since base $BC$ lies along $y = 0$ and $\frac{a \cdot 12}{a + b + c} = \frac{14 \cdot 12}{42} = 4$), and satisfy the universal **Nagel-line proportion**:

$$X(8) - X(2) = \left(\frac{2}{3}, 0\right) = 2\left(\frac{1}{3}, 0\right) = 2\bigl(X(2) - X(1)\bigr).$$

3. Complete Quadrangle & Projective Invariance of Ceva–Menelaus
---------------------------------------------------------------

Viewed in $\mathbb{P}^2$, the four points $(A, B, C, P)$ form a **complete quadrangle** whose three diagonal points are $(D, E, F)$ (with $D = AP \cap BC$, $E = BP \cap CA$, $F = CP \cap AB$). By :person:`Pappus <pappus>` Book VII (:cite:`1588 <pappus:synagoge>`), the diagonal line $EF$ cuts $BC$ at the fourth harmonic point $D'$ of $(B, C; D)$. Thus Ceva's *Proposition* VII and *Proposition* VIII already encapsulate the fundamental harmonic theorem of synthetic projective geometry later systematized by :person:`Lazare Carnot <carnot>` (1806) and :person:`Joseph Diez Gergonne <gergonne>`.
