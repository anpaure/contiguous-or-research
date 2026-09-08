# A clean PBBS C6 has an exact common-history lift through every lower depth

**Date:** 2026-08-05  
**Method:** exact reindexing of the cyclic common-history hinge ring, followed
by literal interval classification; no computation or search  
**Status:** unconditional local theorem.  Every clean Boolean-diamond C6 is
the inverse three-hinge rethread of the common-history construction.  After
one prospective depth-`d` decoration, the complete strict-lower occurrence
deck, every lower derivative row (including q3 and all deeper rows), and
every occurrence-labelled strict-lower compiler matching transport exactly
under arbitrarily many serial decorated switches.  Positive residence and
source length are also exact.  Arbitrary upper transparency is false in
general: the first context-dependent failure can occur at width `d+3` and
rank `r+2`.

## 1. Clean-C6 normal form

Let `K` have size `r-2`, and choose pairwise distinct labels

\[
 a_0,a_1,a_2,c\notin K.
\]

Read subscripts modulo three and put

\[
 R_i=K+a_i,\qquad
 P_i=K+a_i+a_{i+1},\qquad
 Q_i=K+a_i+c.                                      \tag{1.1}
\]

The old and new clean-C6 shores are

\[
 E_i=P_iQ_i,\qquad E_i'=P_iQ_{i+1}.                \tag{1.2}
\]

Their owner and immediate-palette currents vanish.  In the selected PBBS
application, q2 transparency is supplied independently by the authenticated
common-deletion condition: the unchanged companion rows at the three
`P_i` delete one common coordinate `p in K`.  The present theorem does not
need that coordinate for its source lift; it is compatible with it.

Fix a source deadline `d` satisfying

\[
                         1\le d\le r-2.             \tag{1.3}
\]

Choose any ordered partition into nonempty source letters

\[
 K=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
 \qquad {\cal C}=(C_1,\ldots,C_d).                 \tag{1.4}
\]

## 2. Exact identification with the three-hinge ring

Set

\[
 X_i=\{c,a_i\},\qquad Y_i=\{a_{i-1},a_i\}.         \tag{2.1}
\]

Define the two source-fragment families

\[
 W_i=(X_i,{\cal C},Y_i),\qquad
 \widehat W_i=(X_i,{\cal C},Y_{i+1}).              \tag{2.2}
\]

The two length-`d+1` owner windows in `W_i` are

\[
 K+c+a_i=Q_i,qquad K+a_{i-1}+a_i=P_{i-1},         \tag{2.3}
\]

while those in `widehat W_i` are

\[
                         Q_i,\qquad P_i.            \tag{2.4}
\]

Consequently

\[
 \{\text{hinges of }\widehat W_i\}_i=\{E_i\}_i,
 \qquad
 \{\text{hinges of }W_i\}_i=\{E_i'\}_i.          \tag{2.5}
\]

Indeed, the second equality is the reindexing
`Q_i P_(i-1)=P_(i-1)Q_i=E'_(i-1)`.  Thus the clean switch
`E -> E'` is exactly the **inverse** cyclic head rethread
`widehat W -> W` of the frozen common-history hinge-ring theorem, with

\[
 B=K,\qquad b=c,\qquad \text{number of hinges}=3.  \tag{2.6}
\]

All conclusions of that theorem are symmetric under reversing the move.

## 3. Complete lower-depth transparency

Allow arbitrary literal left and right contexts.  Move the complete right
pair (screen plus context) with the head, exactly as in the hinge-ring
comparison.  Then there is an occurrence-preserving bijection between the
old and new interval-OR cells of rank strictly below `r`.

### Theorem 3.1 (all strict-lower occurrences)

The decorated clean C6 preserves the occurrence-labelled multiset of every
strict-lower interval-OR value, at every source width.  In particular it
preserves the complete deck at every width `1,...,d`.

#### Proof

An interval meeting both screens `X_i` and `Y_i` contains every source
letter in `cal C`, hence contains

\[
 K\cup X_i=Q_i,
\]

which has rank `r`.  Therefore a strict-lower interval meets at most one
screen.  Intervals on the left are fixed role by role.  Intervals on the
right move with the complete pair `(Y_i,right context)` and are cyclically
permuted.  Intervals wholly inside `cal C` or a context are fixed or
permuted.  These literal maps are mutually inverse and preserve address,
width, OR value, and multiplicity.  This is the inverse direction of the
common-history hinge-ring bijection.  \(\square\)

Let `D` denote the consecutive-union derivative.  In a depth-`d`
antecedent, owners are `D^d A`; the successive lower rows are

\[
 D^{d-1}A,D^{d-2}A,\ldots,A,                       \tag{3.1}
\]

whose cells are source intervals of widths `d,d-1,...,1`.  Hence:

### Corollary 3.2 (q3 and every deeper lower row)

Every lower derivative row is transparent.  In particular q3 is exact
whenever it exists, and no signed lower sidecar accumulates at any deeper
level.

This conclusion is stronger than equality of target supports: it preserves
the full occurrence multiset.

### Corollary 3.3 (serial telescoping)

Any finite serial sequence of prospectively decorated clean C6 moves has
zero total signed derivative on the complete strict-lower occurrence deck.

#### Proof

Each move supplies a literal occurrence bijection.  Compose the bijections.
No disjointness or commutativity is required once every intermediate move is
literally planted and its complete right pair is moved as specified.
\(\square\)

The word "prospectively" is essential.  An arbitrary PBBS C6 in a frozen
owner factor is not thereby guaranteed to expose the source letters
`(X_i,C_1,...,C_d,Y_i)` in one already fixed antecedent.  The theorem gives
the exact whole-packet decoration that a protected planting theorem must
install.

## 4. Compiler and residence consequences

### Theorem 4.1 (strict-lower compiler transport)

Let a strict-lower compiler use distinct occurrence-labelled interval cells
and let validity of an edge mean that the cell OR equals (or contains, under
the stated compiler convention) its assigned lower target.  Transport every
selected cell through the bijection of Theorem 3.1.  Then all target
assignments remain valid and distinct.  Thus the compiler deletion number
is exactly unchanged; in particular a zero-defect compiler stays zero
defect after any serial sequence.

This includes all compiler information encoded solely by the literal cell,
its width, value, and the transported context.  It does **not** automatically
include an external maximal-common-cap network with additional phase flags,
typed sink identities, shared route capacities, or state-dependent
structural zeros.  Such a cap transports only after those extra data are
proved equivariant under the same occurrence bijection.

### Theorem 4.2 (positive residence and charge)

On a cyclic source word, every occurrence of a coordinate belongs to
`d+1` consecutive owner windows.  Thus each occurrence creates a positive
owner run of length at least `d+1`; overlaps only merge runs into longer
ones.  The old and new packet families use the same source-letter multiset,
with heads merely permuted, and therefore add no source position.

For a linear word, every relevant fragment must lie at least `d` source
positions from an endpoint or use the standard clipped endpoint collar.
Minimum **zero-run/gap** residence is a separate exterior condition and is
not proved here.

## 5. The exact first upper boundary

The internal fragment deck is exact through width `d+2`:

1. widths at most `d` follow from Theorem 3.1;
2. width `d+1` is the owner bank; and
3. width `d+2` is the immediate-upper bank, cyclically permuted.

The first context-dependent width is `d+3`, and exact upper transparency is
already false there.

### Theorem 5.1 (sharp private-prefix upper counterexample)

Adjoin three fresh labels `p_0,p_1,p_2`, each occurring only in a singleton
left-context letter immediately before the corresponding hinge fragment.
In the `W` orientation, the full width-`d+3` interval in role `i` has value

\[
 T_i=K\cup\{c,a_{i-1},a_i,p_i\}.                  \tag{5.1}
\]

After the head rethread, the only full width-`d+3` interval containing
`p_i` in that role has value

\[
 \widehat T_i=K\cup\{c,a_i,a_{i+1},p_i\}.         \tag{5.2}
\]

The value `T_i` is absent from the new displayed local family.

#### Proof

The private label `p_i` occurs in no other role, so any new local interval
with value `T_i` must lie in role `i` and contain that left singleton.
But the rethreaded role contains active labels `a_i,a_(i+1)` and contains no
`a_(i-1)`.  Hence no such interval has value (5.1).  The old full interval
does.  Its rank is `|K|+4=r+2`.  \(\square\)

By reversing the comparison, the same counterexample applies in the PBBS
orientation `E -> E'`.  Thus width `d+3` and rank `r+2` are the first place
where an exterior upper casualty can occur.  The failure is not at q3 or
at any deeper lower row.

More generally, every potentially lost old upper value contains one old
rank-`r+1` hinge union

\[
 U_i=K\cup\{c,a_{i-1},a_i\}.                       \tag{5.3}
\]

Therefore one packet's damage universe is contained in the three Boolean
cones above the `U_i`, of total size at most

\[
                         3\,2^{k-r-1}.              \tag{5.4}
\]

This is localization, not a bounded sidecar.  A serial collection of C6s
has no context-free cancellation theorem for these upper cones.  It needs
a protected alternative-witness bank or a correlated exterior permutation.

### Corollary 5.2 (no purely local all-upper circuit theorem)

No theorem based only on the clean-C6 owner/q1/q2 identities and the common
history can assert arbitrary-exterior all-upper transparency: Theorem 5.1
is a literal counterexample.  Replacing C6 by another finite head-permutation
circuit does not remove this issue if the permutation is nonidentity and
contexts are arbitrary; private context labels expose the changed pairing.
The missing ingredient is therefore an exterior guard, not merely a larger
unadorned Boolean circuit.

## 6. Consequence for the current PBBS programme

For every selected common-pivot PBBS connector in the current hook/profile
atlas, the local higher-depth state is now:

| gate | status after common-history decoration |
|---|---|
| owner, lower q1, upper q1 | exact |
| selected q2 | exact by the PBBS common-pivot theorem |
| q3 and every deeper lower row | exact occurrence multiset |
| strict-lower compiler matching | exact transport, zero deletion |
| positive depth-`d` residence | exact cyclically / with endpoint collar |
| source length | zero charge |
| zero-gap residence | open exterior guard |
| arbitrary-width upper deck | false locally from width `d+3`; protected witnesses required |
| typed/shared maximal common cap | conditional on equivariance of its extra state and routes |

Thus the first new obstruction after q1/q2 is **not q3**.  It is the
rank-`r+2` long upper/exterior row (together with non-functorial cap and
zero-gap guards).

## 7. Dependencies and scope

The proof specializes, with the explicit reindexing (2.3)--(2.6),

`MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md`

and its final cross-audit.  The PBBS q2 statement is imported only from

`MATH_THEOREM_CLEAN_C6_Q2_NEUTRAL_COMMON_DELETION_CLASSIFICATION_20260805.md`.

No PBBS source planting, global loose forest, upper witness bank, zero-gap
residence theorem, typed common-cap router, or all-`k` universal word is
claimed.
