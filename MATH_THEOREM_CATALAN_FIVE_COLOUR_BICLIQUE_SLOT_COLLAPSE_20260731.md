# Boolean containment bicliques collapse onto one physical owner

Date: 2026-07-31  
Status: exact all-parameter obstruction.  It rules out the direct embedding
of the affine five-colour refactorization as a complete lower--upper block
inside the Catalan capacity-slot host.  It does not rule out sparse
five-colour packets, status migration, or larger non-biclique exchanges.

## 1. Statement

Let

\[
 \mathcal A\subseteq {[2n]\choose n},\qquad
 \mathcal B\subseteq {[2n]\choose {n+2}}
\]

contain at least two distinct members each, and suppose

\[
                         A\subset B
        \qquad(A\in\mathcal A,\ B\in\mathcal B).       \tag{1.1}
\]

Then there is one rank-`n+1` set `H` such that

\[
 A=H-\{a_A\},\qquad B=H+\{b_B\},                     \tag{1.2}
\]

for every `A,B`.  Consequently the two intermediate owners of the Boolean
diamond `(A,B)` are

\[
                  H,\qquad H-\{a_A\}+\{b_B\}.        \tag{1.3}
\]

In particular **every** atom above the complete containment biclique
`mathcal A x mathcal B` uses the same physical owner `H`.

In the punctured capacity-slot host, `H` has capacity at most two (one when
it is a seam anchor).  Hence any host matching contains at most two atoms
from this entire biclique.

## 2. Proof

Put

\[
              U=\bigcup_{A\in\mathcal A}A,
              \qquad I=\bigcap_{B\in\mathcal B}B.
\]

Condition (1.1) gives `U subseteq I`.  Since `mathcal A` contains two
distinct rank-`n` sets,

\[
                            |U|\ge n+1.               \tag{2.1}
\]

Since `mathcal B` contains two distinct rank-`n+2` sets,

\[
                            |I|\le n+1.               \tag{2.2}
\]

Thus `U=I=:H` and `|H|=n+1`.  Every rank-`n` member of `mathcal A` contained
in `H` is `H-{a_A}`, while every rank-`n+2` member of `mathcal B` containing
`H` is `H+{b_B}`.  Their difference is exactly `{a_A,b_B}`, so the two
rank-`n+1` intermediates are those in (1.3).  This proves the structural
claim.  The matching bound follows because every atom consumes one of the
one or two occurrence slots at `H`.  `square`

## 3. Consequence for the five-colour idea

The affine four-partite example in
`MATH_THEOREM_CATALAN_FIXED_Q_DUMMY_DUAL_AND_MULTICOLOUR_LOCKING_20260731.md`
first refactors at five colours.  Its 25 atoms form a transversal design:
the projections onto any two resource parts are complete `K_(5,5)` blocks.
Under an injective partwise identification of its five lower and five upper
resources with distinct Boolean rank-`n` and rank-`n+2` colours, the
projection is a literal `K_(5,5)` and invokes the theorem above.  All 25
candidate diamonds
then pass through one owner `H`, so no physical matching can contain more
than two of them.  The affine 25-atom refactorization therefore has **no
direct capacity-slot embedding**.

This separates two statements:

* five colours are the first point where generic four-partite factorization
  need not be locked;
* the first useful Boolean five-colour move cannot be the complete affine
  transversal design.

A viable packet must instead use a sparse lower--upper incidence pattern,
move the puncture/status bank while it switches, or combine several owner
fibres so that no rank-`n+1` owner exceeds capacity two.  Standard Boolean
incidence hexagons have a sparse six-edge pattern and are not excluded by
this theorem; their palette, slot, graphic, and downstream-cap compatibility
remain separate questions.

## 4. Scope audit

The proof uses only ranks and containment and is valid for every `n` for
which both families exist.  It makes no assertion about an arbitrary set of
25 diamonds whose lower--upper projection is not complete, and it does not
convert the abstract affine locking theorem into a Boolean impossibility.
It closes only the most direct `K_(5,5)` embedding.
