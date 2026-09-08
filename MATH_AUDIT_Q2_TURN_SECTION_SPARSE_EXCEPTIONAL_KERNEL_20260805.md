# Independent audit: the q2 turn-section sparse exceptional kernel

**Date:** 2026-08-05  
**Method:** pure mathematics; independent line-by-line counting and
occurrence-CSP audit; no computation or search  
**Audited source:**
`MATH_THEOREM_Q2_TURN_SECTION_SPARSE_EXCEPTIONAL_KERNEL_20260805.md`  
**Verdict:** **GO**, with one terminology clarification and no mathematical
correction.

## 1. Parameter and repeated-occurrence ledger

Put

\[
 P={2r-1\choose r-1},\qquad Q={2r-1\choose r-2},\qquad
 \kappa=P-Q.
\]

The identities

\[
 \frac QP=\frac{r-1}{r+1},\qquad
 \kappa=\frac{2P}{r+1}=\operatorname {Cat}_r
\]

are exact.  If `m(Y)` is the occurrence multiplicity of a turn label, turn
surjectivity gives

\[
 \sum_Y(m(Y)-1)=P-Q=\kappa.
\]

Consequently the repeated-label family `R` has order at most `kappa`, and
the union `H` of all occurrences of repeated labels has

\[
 |H|=|\mathcal R|+\kappa\le 2\kappa.
\]

This verifies Lemma 2.1 exactly.

## 2. Exceptional q2 colours

If a q2 colour has no witness with two globally unique endpoint labels,
then every one of its witnesses touches an occurrence in `H`.  A set of
`h=|H|` positions in a cyclic word is incident with at most `2h` adjacent
indices.  Therefore

\[
 \#\{\hbox{exceptional colours}\}\le 2h\le4\kappa,
\]

and the **total number of their occurrence-labelled witness terms** is also
at most `2h<=4 kappa`.  This verifies both assertions of Lemma 2.2.  Sharing
a globally unique occurrence between two clean witnesses causes no conflict:
the section selects that unique occurrence once, and both adjacent witnesses
remain present.

## 3. Positive two-local CSP equivalence

A retained q2 witness has unequal endpoint labels.  For each repeated
endpoint it imposes one equality choosing its literal occurrence, so its
term has zero, one, or two equalities.  Pairwise consistency of such
equalities is global consistency, because all literals simply assign values
to the variables `a_Y`.

* A q2-complete section restricts to a satisfying assignment on the repeated
  labels and makes one witness term true in every exceptional class.
* Conversely, a satisfying assignment selects one occurrence of every
  repeated label; selecting the unique occurrence of every other label then
  keeps every true exceptional witness and every clean witness.

Thus Theorem 3.1 is an exact equivalence.  Its four size bounds follow from
Sections 1--2 above.

## 4. Nonsingleton-class count and propagation

Let

\[
 M={2r-1\choose r-3}
\]

and let `A<=P` be the number of retained unequal adjacent indices.  Under
q2 surjectivity,

\[
 \sum_D(|E_D|-1)=A-M\le P-M.
\]

Direct cancellation gives

\[
 P-M=\frac{6rP}{(r+1)(r+2)}
     =\frac{3r}{r+2}\,\kappa<3\kappa.
\]

Every nonsingleton original class contributes at least one to the left-hand
sum, so fewer than `3 kappa` classes are initially nonunit.  Satisfying and
deleting consistent unit classes leaves only members of that original
nonunit family; subsequent propagation cannot create a new constraint
class.  Hence the residual class count remains below `3 kappa`.

The only clarification is linguistic.  After the first substitution round,
"repeat singleton propagation" means:

> propagate any surviving constraint which has exactly one surviving
> witness term,

not that its original occurrence set `E_D` has suddenly changed cardinality.
This is the standard unit-propagation meaning and is exactly what the proof
uses.

## 5. Scope

The audit confirms only the conditional kernel theorem.  It retains both
premises:

1. the turn word is surjective on rank-`(r-2)` labels; and
2. its unequal-adjacency q2 row is surjective on rank-`(r-3)` colours.

It does not prove feasibility of the residual positive CSP.  In particular,
two singleton q2 classes may force two different occurrences of one repeated
turn label.  That is a genuine occurrence-correlation obstruction and is
not removed by the Catalan-scale counting bounds.

