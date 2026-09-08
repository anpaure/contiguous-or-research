# Moving-core pull clocks: an all-odd depth-one Hamilton rail and the exact depth-two boundary

**Date:** 2026-08-02
**Status:** unconditional infinite-family construction and exact depth-two
interface.  The construction is owner-exact and top-target-exact on the
literal rail.  After extending one parity matching to a symmetric-chain
decomposition, it also carries an exact static lower-target chain payload.
Only the depth-one target row is asserted to be serialized by the literal
rail.  No upper-shadow, residence beyond the stated depth, exterior-opening,
or common-cap/compiler claim is made.

## 0. Result

Put

\[
             k=2r-1,\qquad
             W={2r-1\choose r}={2r-1\choose r-1},
             \qquad r\ge2.                                      \tag{0.1}
\]

For every such `r` there is a static table with

1. every rank-`r` owner exactly once;
2. every rank-`(r-1)` target exactly once;
3. one literal predecessor Hamilton cycle; and
4. stationary pull-clock type `(r-1,1)` at every occurrence.

Thus the simplest stationary pull-clock vertex has an exact one-copy
integral realization in every odd dimension.  The essential move is to let
the `(r-2)`-core change from owner to owner; freezing the symmetric
pull-clock core is unnecessary and would miss this construction.

Moreover one can choose the owner matching to extend to a full SCD of
`B_(2r-1)`.  The SCD supplies, simultaneously, every nonempty lower Boolean
target exactly once as a static chain payload.  This does not turn those deeper
payload entries into source-window suffixes; that stronger serialization
starts at depth two and has a sharp extra condition.

For a cyclic lower-middle sequence `q_i`, the depth-two all-high lift exists
exactly when no coordinate has a one-position positive run.  Equivalently,

\[
 (q_{i-1}\cap q_i)\cup(q_i\cap q_{i+1})=q_i
 \quad\text{for every }i.                                     \tag{0.2}
\]

On this face the depth-two block at the overlap is forced to be
`q_i cap q_(i+1)`.  Hence exact rank-`(r-2)` target coverage is equivalent
to surjectivity of the adjacent-intersection palette.  This is the first
nonautomatic recursive row.

## 1. The depth-one moving-core table

Let

\[
 q_0,T_0,q_1,T_1,\ldots,q_{W-1},T_{W-1},q_0             \tag{1.1}
\]

be a Hamilton cycle of the Middle Levels graph on ranks `r-1` and `r` of
`B_(2r-1)`.  Thus

\[
 |q_i|=r-1,\quad |T_i|=r,\quad
 q_i\subset T_i\supset q_{i+1},                         \tag{1.2}
\]

and all `q_i` and all `T_i` are distinct.  Indices are cyclic.

Make role `i` have owner `T_i` and one-letter head

\[
                         h_i=(q_{i+1}).                  \tag{1.3}
\]

In the notation of the Boolean rail theorem,

\[
 U_i=q_{i+1},\qquad
 P_i=T_i\setminus q_{i+1}=q_i\setminus q_{i+1}.         \tag{1.4}
\]

Both rail words are the unique empty word at depth one.

### Theorem 1.1 (all-odd Hamilton rail)

For every `r>=2`, the table (1.3) is owner-exact and rank-`(r-1)`
target-exact, and its cloned predecessor graph contains the directed
Hamilton cycle

\[
                       0\to1\to\cdots\to W-1\to0.       \tag{1.5}
\]

Consequently it has a balanced connected literal trace selector with zero
lower-side sidecar.

#### Proof

Owner and target exactness follow immediately from the Hamilton cycle
(1.1).

The head token of role `i-1` is `q_i`.  By (1.2),

\[
 P_i=q_i\setminus q_{i+1}\subseteq q_i\subseteq T_i.    \tag{1.6}
\]

The depth-one rail equality is vacuous, so Lemma 1.1 of the Boolean rail
theorem says exactly that `i-1` can precede `i`.  These `W` literal arcs
give (1.5), using every head token and every role once.  Reading the cycle
spells the cyclic source word

\[
                         q_0,q_1,\ldots,q_{W-1}.         \tag{1.7}
\]

Its consecutive two-letter unions are the owners `T_i`, each once.  The
one-letter heads are the targets `q_i`, each once.  This is a literal
balanced connected selector. \(\square\)

### Corollary 1.2 (integral all-high pull-clock vertex)

Every owner window in (1.7) has novelty-age sizes `(r-1,1)`: one of its
two facets is the current rank-`(r-1)` source letter and the other contributes
the unique missing point.  Thus Theorem 1.1 is a one-copy integral
realization of the depth-one all-high stationary pull-clock type.

The stationary fractional construction usually symmetrizes a fixed core.
Here the core

\[
                         q_i\cap q_{i+1}                 \tag{1.8}
\]

is allowed to move with `i`.  That basis change is precisely what permits
one-copy owner exactness.

## 2. Simultaneous SCD target payload

Choose from (1.1) the parity matching

\[
                         M=\{q_{i+1}T_i:i\in\mathbb Z_W\}.       \tag{2.1}
\]

The central-matching extension theorem says that every perfect matching
between the two middle ranks of `B_(2r-1)` extends to a saturated SCD.
Apply it to `M`.

### Theorem 2.1 (static all-lower payload with the same owners)

There is an SCD `D` whose chain containing `q_(i+1)` continues upward to
the owner `T_i`.  Attach the downward part of that chain as a static
target-chain payload to role `i`.  Across all roles, every nonempty Boolean
target of ranks `1,...,r-1` occurs exactly once in these payloads, while the
literal depth-one Hamilton rail (1.5) is unchanged.

#### Proof

Extend `M` to an SCD.  Each SCD chain crosses both middle ranks, and its
central edge is exactly one edge `q_(i+1)T_i` of `M`.  Since the SCD
partitions the Boolean lattice, its downward chain members partition every
lower rank.  Assigning the chain with central edge `q_(i+1)T_i` to role `i`
therefore gives every owner and every nonempty lower target exactly once.
The head word (1.3) and the selected predecessor arcs (1.5) are untouched.
\(\square\)

### Scope warning

Theorem 2.1 is a **static** payload theorem.  A rank below `r-1` need not be
the union of a suffix of the physical depth-one word (1.7).  Therefore it
does not close the depth-`d` triangular source row for `d>=2`.  It does show
that the target-chain marginal, owner matching, and depth-one chronology can
be chosen together; the first remaining correlation is literal age shift.

## 3. Exact depth-two lift

Assume in this section that `r>=3`, so depth two is below the owner rank
and every overlap block is nonempty.

Keep the lower-middle Hamilton order `q_i`.  Because consecutive lower
vertices share the upper vertex `T_i`, they are Johnson adjacent.  Put

\[
                         B_i=q_i\cap q_{i+1},qquad |B_i|=r-2.  \tag{3.1}
\]

Consider the proposed two-letter heads

\[
                         h_i=(B_i,B_{i+1}).              \tag{3.2}
\]

Their union is the desired first lower target `q_(i+1)` precisely when

\[
                         B_i\cup B_{i+1}=q_{i+1}.        \tag{3.3}
\]

### Theorem 3.1 (depth-two run/intersection equivalence)

The following are equivalent.

1. The Middle Levels carrier (1.1) has an all-high depth-two literal lift
   whose rank-`(r-2)` overlap blocks have the required rank.
2. The forced blocks (3.1) satisfy
   `B_(i-1) union B_i=q_i` for every `i`.
3. No coordinate has a positive run of length one in the cyclic incidence
   word of the `q_i`.
4. Consecutive adjacent-intersection colours are unequal:
   `B_(i-1) != B_i` for every `i`.

When these conditions hold, the heads (3.2) and the leading blocks
`B_(i-1)` spell the literal Hamilton chronology

\[
 \cdots,B_{i-1},B_i,B_{i+1},\cdots,                    \tag{3.4}
\]

whose consecutive two-block unions are all `q_i` and whose consecutive
three-block unions are all `T_i`.

#### Proof

Suppose first that a rank-correct depth-two lift exists, and write its
overlap block between the `q_i` and `q_(i+1)` heads as `C_i`.  Then

\[
 C_i\subseteq q_i\cap q_{i+1}=B_i.                    \tag{3.5}
\]

Both sets have rank `r-2`, so `C_i=B_i`.  Hence the lift is possible only
if the two blocks around `q_i` cover it, which is statement 2.  Conversely,
statement 2 gives, simultaneously for every cyclic index `i`,

\[
 B_{i-1}\cup B_i=q_i,
 \qquad B_i\cup B_{i+1}=q_{i+1}.                       \tag{3.6a}
\]

Taking their union gives the exact three-window identity

\[
 B_{i-1}\cup B_i\cup B_{i+1}
   =q_i\cup q_{i+1}=T_i,                               \tag{3.6b}
\]

for every `i`.  Thus all two-windows are the lower targets and all
three-windows are the owners, proving that (3.4) is a literal depth-two
lift on the whole cycle.

Write

\[
 q_i=q_{i-1}-\{a\}+\{b\},\qquad
 q_{i+1}=q_i-\{c\}+\{e\}.                             \tag{3.7}
\]

Every element of `q_i` other than the newly arrived `b` lies in `q_(i-1)`,
and every element other than the departing `c` lies in `q_(i+1)`.  Therefore

\[
 (q_{i-1}\cap q_i)\cup(q_i\cap q_{i+1})=q_i           \tag{3.8}
\]

unless `b=c`.  The equality `b=c` says exactly that coordinate `b` is
present only at `q_i`, i.e. it has a one-position positive run.  This proves
2 iff 3.

Finally, both `B_(i-1)` and `B_i` are distinct rank-`(r-2)` subsets of
`q_i` unless their omitted points agree.  They are equal exactly when the
new point `b` is also the departing point `c`.  Thus 3 iff 4. \(\square\)

### Corollary 3.2 (the first recursive target row)

On a depth-two lift, the rank-`(r-2)` source values are exactly

\[
                  \{q_i\cap q_{i+1}:i\in\mathbb Z_W\}. \tag{3.9}
\]

Consequently every rank-`(r-2)` target can be assigned once if and only if
the **support** of the map in (3.9) is all of
`binom([2r-1],r-2)`.  This is a surjectivity/marking condition, not a
bijection: one occurrence of each target is marked and extra occurrences
remain unmarked.

This condition is strictly stronger than the absence of singleton runs:
Theorem 3.1 gives only adjacent nonrepetition, whereas surjectivity is a
global palette condition.

## 4. Sharp local obstruction and recursive interface

Let `S` have rank `r-2`, and take three distinct points `a,b,c` outside
`S`.  The legal local Middle Levels segment

\[
 S+a,\quad S+a+b,\quad S+b,\quad S+b+c,\quad S+c       \tag{4.1}
\]

has a one-position run of `b` on the lower shore.  Both adjacent
intersection colours equal `S`.  Therefore no rank-correct depth-two block
lift can serialize this segment, even though both middle-level wedges are
perfectly legal and all five displayed vertices are distinct.

This is the exact boundary missed by a recursion that preserves only the
central incidence matching or only SCD target exactness.

There is also a sharp global first-boundary calibration.  The independent
audit
`MATH_AUDIT_K_PRIVATE_SOCKET_PASCAL_RECURSION_AND_K5_TWO_CYCLE_BOUNDARY_20260802.md`
proves that every balanced owner-exact all-high table at `(k,d)=(5,2)` is,
up to relabelling, the regular `Z_5` tournament and its forced transition
permutation is the disjoint union of the step-one and step-two directed
`C_5` cycles.  Thus the depth-one family of Theorem 1.1 does **not** promote
to depth two by the raw `3 -> 5` Pascal step.  An open port, a non-all-high
role, or a compound matching-closed absorber is already necessary there.

The strongest proof-safe same-parity interface supplied here is therefore:

> Choose a Middle Levels Hamilton cycle and one parity matching; extend the
> matching to an SCD; then require that the Hamilton lower order has no
> positive coordinate run shorter than the desired depth and that its
> consecutive-intersection decks contain the prescribed SCD targets.

At depth one the last requirement is vacuous, proving Theorems 1.1 and 2.1
for all odd dimensions.  At depth two it is exactly Theorem 3.1 plus the
surjectivity row (3.9).  For larger depth it becomes the intersection-deck
identity

\[
 q_i\cap q_{i+1}\cap\cdots\cap q_{i+j},qquad 1\le j<d, \tag{4.2}
\]

together with minimum positive run length `d`, as in the audited all-high
serialization theorem.

## 5. Separation from downstream gates

The proved construction closes only the following rows:

| row | depth one | depth two |
|---|---:|---:|
| owners exactly once | proved | conditional on Theorem 3.1 |
| lower q1 targets exactly once | proved | inherited from the carrier |
| one predecessor component | proved | conditional on Theorem 3.1 |
| static SCD lower payload | proved | proved but not automatically serialized |
| lower q2 targets | not present | exactly the surjectivity gate (3.9) |
| upper interval decks | not claimed | not claimed |
| required global residence | depth-one only | exactly the stated no-singleton condition |
| exterior opening | not claimed | not claimed |
| common-cap/compiler | not claimed | not claimed |

The construction therefore supplies a genuine infinite integral rail family
and an exact recursive boundary, but not the full `nu(k)=B(k)` induction.

## 6. Proof dependencies

The construction uses only the following previously audited results.

1. Middle Levels Hamiltonicity in every odd dimension.
2. The literal predecessor identity from
   `MATH_THEOREM_K_BOOLEAN_RAIL_INTERVAL_HALL_AND_COMPLETE_TRANSITION_EULER_FUSION_20260802.md`.
3. The arbitrary-central-matching SCD extension from
   `MATH_THEOREM_ANTICHAIN_TOP_SCD_HAMILTON_OWNER_LIFT_AND_LITERAL_AGE_GATE_20260802.md`.
4. The identification of `(r-1,1)` as the depth-one all-high rotor type in
   `MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`.
5. The first same-parity boundary audit in
   `MATH_AUDIT_K_PRIVATE_SOCKET_PASCAL_RECURSION_AND_K5_TWO_CYCLE_BOUNDARY_20260802.md`.

No generic degree-only rainbow theorem, matroid-extension assertion, or
rounding of the canonical rational pull-block histogram is used.
