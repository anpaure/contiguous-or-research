# Guarded octagon doublets are exactly OR-transparent, but do not lift the CBC circuit

Date: 2026-08-01  
Status: exact source-word theorem and exact scope separation.  The native
single-copy lift is impossible.  A two-copy stabilization gives a closed
width-graded OR-language transposition in every exterior context, but it is
null on the coherent-birail circuit state and its minimal screens are not
resident.  Hence it is not a physical CBC lift.

## 0. Verdict

Let `Y^0,Y^1` be either the maximal or sharp source inverses of the resident
quaternary octagon after the two exterior split hosts have been expanded.
The exact source-deck audits give, for the sharp inverse and every `d>=2`,

\[
 |\operatorname{Deck}(Y^0)-\operatorname{Deck}(Y^1)|=4d+1,
 \qquad
 |\operatorname{Deck}(Y^1)-\operatorname{Deck}(Y^0)|=6d-3.       \tag{0.1}
\]

Moreover `3d-3` masks in either directed difference are outside the complete
arbitrary-block-refinement closure of the opposite source.  Thus **no number
of splits or stutters of current letters** makes one native phase
source-signature conjugate to the other.

There is nevertheless a precise stabilized positive statement.  Put

\[
                 L=\{a_0,a_1\},\qquad R=\{a_1,a_2\},
 \qquad G^\epsilon=L\,Y^\epsilon\,R.                    \tag{0.2}
\]

Then the prefix and suffix ORs of `G^0,G^1` agree **pointwise by relative
length**.  Consequently

\[
                       G^0G^1\longleftrightarrow G^1G^0          \tag{0.3}
\]

preserves the complete interval-OR multiset separately at every width, and
does so in every fixed exterior context.

This exactly neutralizes the two-sided exterior grid missed by the `B+2`
two-stutter calculation.  It still does not prove CBC(C): both sides of
(0.3) contain one copy of each octagon phase, so the abstract `C6/C8` state
does not change, and the two OR screens create short active-coordinate runs.
The construction is a closed null move, not the needed physical Markov
generator.

## 1. Width-graded source signatures

For a word `W=(W_1,...,W_n)`, write

\[
 \operatorname{Pre}_i(W)=\bigcup_{j=1}^iW_j,
 \qquad
 \operatorname{Suf}_i(W)=\bigcup_{j=n-i+1}^nW_j,                 \tag{1.1}
\]

and let `Deck_q(W)` be the multiset of OR values of all length-`q`
intervals.  Define the graded signature

\[
 \Sigma(W)=\bigl((\operatorname{Pre}_i(W))_i,
                  (\operatorname{Suf}_i(W))_i,
                  (\operatorname{Deck}_q(W))_q\bigr).           \tag{1.2}
\]

Pointwise prefix/suffix information is stronger than equality of their
ungraded supports.  It is exactly what is required to transport widths and
deadline addresses through a block interchange.

### Lemma 1.1 (graded block transposition)

Let `A,B` have the same length and suppose

\[
 \operatorname{Pre}_i(A)=\operatorname{Pre}_i(B),\qquad
 \operatorname{Suf}_i(A)=\operatorname{Suf}_i(B)                 \tag{1.3}
\]

for every `i`.  Then

\[
                 \Sigma(AB)=\Sigma(BA).                         \tag{1.4}
\]

More strongly, for arbitrary fixed exterior words `X,Z`,

\[
          \operatorname{Deck}_q(XABZ)=\operatorname{Deck}_q(XBAZ)
          \qquad\text{for every }q.                              \tag{1.5}
\]

#### Proof

Intervals lying in one complete block are transported with that labelled
block.  An interval crossing the unique internal seam and using `i` letters
from its left block and `j` from its right block has value

\[
                       \operatorname{Suf}_i(A)
                        \cup\operatorname{Pre}_j(B).
\]

After the transposition the corresponding interval has value
`Suf_i(B) union Pre_j(A)`, equal by (1.3), and has the same width `i+j`.
This is a width-preserving occurrence bijection.  Prefixes and suffixes are
handled by the same equations; a context-crossing interval which contains
both complete blocks sees their common total union.  This proves
(1.4)--(1.5).  \(\square\)

## 2. The octagon screens

The source-deck classification gives the exact directed differences

\[
\begin{array}{c|cc}
 &Y^0-Y^1&Y^1-Y^0\\ \hline
 \operatorname{Pre}&\{\{a_0\}\}&\{\{a_1\}\}\\
 \operatorname{Suf}&\{\{a_1\}\}&\{\{a_2\}\}.
\end{array}                                                   \tag{2.1}
\]

The tensor formulas give the stronger addresswise statement: every prefix
OR discrepancy is screened by adjoining `L={a0,a1}`, and every suffix OR
discrepancy is screened by adjoining `R={a1,a2}`.  Thus, for every relative
address `i`,

\[
 \operatorname{Pre}_i(G^0)=\operatorname{Pre}_i(G^1),\qquad
 \operatorname{Suf}_i(G^0)=\operatorname{Suf}_i(G^1).           \tag{2.2}
\]

The two guarded internal decks are still unequal by (0.1): a context or
endpoint screen cannot alter an interval lying wholly inside the packet.
Applying Lemma 1.1 to the pair `(G^0,G^1)` proves (0.3), including exact
width multiplicities and arbitrary exterior contexts.

For the sharp inverse, `|Y^epsilon|=9d+27` after the already-authenticated
exterior splits, so

\[
                 |G^\epsilon|=9d+29,qquad
                 |G^0G^1|=18d+58.                              \tag{2.3}
\]

The maximal-source statement has the same lengths and proof.

## 3. Why the `B+2` exterior-grid counterexample does not hit (0.3)

Identical two-stutter collars preserve only the local seam grid through the
owner band.  At larger widths an old block rotation exposes

\[
                    U\cup S_u\cup R_v,                           \tag{3.1}
\]

and the authenticated counterexample loses `(s-1)(t-1)` distinct values.
The missing hypothesis there is exactly (1.3): the old and new exterior
prefix/suffix chains differ.

In (0.3), the left and right exterior chains agree at every relative
address.  Hence every term of (3.1) transports termwise.  The doublet is
therefore an exact solution of the **upper-ticket equation**, but only after
stabilizing by a complete copy of the opposite phase.

This proves the sharp distinction:

\[
 \boxed{\text{identical collars are insufficient; identical graded block
 signatures are sufficient.}}                                  \tag{3.2}
\]

## 4. Native single-copy no-go and planted-host bounds

For the sharp packet, the exact native endpoint-ray cover numbers of the two
directed source-deck differences are `8` and `9`.  More strongly, arbitrary
refinement of all current letters still leaves `3d-3` unreachable masks in
each direction.  Therefore:

1. no current-letter split/stutter construction, of any cardinality, gives
   a native single-copy signature-conjugate lift;
2. if one new host is charged per physical ray, exactly eight/nine rays are
   necessary and sufficient at the unguarded set-geometry level;
3. if a binary planted host may realize two compatible rays, the ray count
   gives only the lower bound `ceil(9/2)=5` hosts; and
4. no five-host theorem follows without the pairing, common-union, owner,
   residence, deadline and common-cap equations.

Thus the exact minimum in the current word is infinity, while the newly
planted-host problem lies between five and nine hosts before physical
legality is imposed.  The latter is an honest open gate, not a consequence
of Dilworth width.

## 5. Exact CBC boundary

The doublet transposition is closed as an OR-language operation: it is an
involution, and disjoint doublets commute.  In whole-block terminology it
has degree two independently of `d`.

It fails the corrected CBC hypotheses in three separate ways.

### 5.1 It is a stabilization, not the circuit

Both states in (0.3) contain the multiset `{G^0,G^1}`.  Projecting to the
two alternating states of the `C6` fibre therefore gives the same stabilized
count on both sides.  The indispensable cubic changes one alternating table
to the other; (0.3) merely changes the order of a table plus its inverse.
It has zero net coherent-birail action.

### 5.2 The OR screens are not residence screens

At the left screen the leading run lengths of `a0,a1` in the two phases are
`(2,1)` in opposite order.  At the right screen the corresponding trailing
run lengths of `a1,a2` are `(2,1)` in opposite order.  For `d>=2` these are
shorter than the required `d+1`.  The screen positions therefore cannot be
inserted as internal source letters of a resident CBC class.

A resident screen needs a rail of length at least `d+1`, or an actual
ambient boundary at which the run is clipped.  The former is `Theta(d)`
physical support and the latter is not serially closed under arbitrary
reordering.

### 5.3 Deck equality is not a common-cap matching

The width-graded bijection preserves OR occurrences, but CBC also asks that
the relevant occurrences remain legal in one common cap and that the
terminal lower matching/topology rows survive.  Those labels are not encoded
by `Sigma(W)`.  In particular, stabilization doubles the local owner and
compiler resource rather than preserving the original fixed-margin fibre.

Consequently the proved implication is

\[
 \text{guarded doublet}\Longrightarrow
 \text{closed full-upper OR null move},                         \tag{5.1}
\]

not

\[
 \text{guarded doublet}\Longrightarrow
 \text{closed physical }C_6/C_8\text{ Markov lift}.             \tag{5.2}
\]

## 6. Smallest honest remaining theorem

An unstabilized CBC lift must supply, for each applicable `C4/C6` circuit,
two actual source states which

1. project to the two different circuit endpoints;
2. have identical graded prefix, suffix and internal interval signatures,
   or carry a literal protected-occurrence bijection for their residue;
3. have identical clipped residence and endpoint-envelope signatures;
4. preserve owner/topology/common-cap rows; and
5. regenerate the same planted host bank after the move.

The exact `8/9` ray theorem reduces item 2 to a constant physical interface,
but current-letter splitting is ruled out.  The needed construction must be
a newly planted two-sided host bank.  The `B+2` stutters can be part of its
short-band collar, but the full exterior-grid equality of item 2 must be
proved separately.

## 7. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_octagon_guarded_signature_doublet_20260801.py --write
```

The replay checks `2<=d<=24`, for both maximal and sharp source inverses:

* native and guarded single-phase internal deck inequality;
* pointwise guarded prefix/suffix equality;
* exact width-graded doublet deck equality;
* arbitrary tagged-context equality; and
* the short boundary-run obstruction.

It does not assert owner, common-cap or compiler legality.
