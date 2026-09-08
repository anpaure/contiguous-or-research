# PBBS degree-three collar separation and the failure of sibling upper cancellation

**Date:** 2026-08-05  
**Method:** cyclic interval packing and the clean-C6 private-prefix test; no
search  
**Status:** unconditional for the aligned depth-`d` source lift described
below.  At a subcubic node, an optional third packet can be separated from
the forced consecutive sibling pair once `2m+1>2d+8`.  Pairing the two
sibling packets does not, by itself, cancel their first arbitrary-upper
damage.

## 1. The protected source collar of one packet

Index a cyclic source word by `Z_L`.  A depth-`d` common-history packet
whose changed owner edge starts at time `t` uses the source fragment

\[
                 A_t,A_{t+1},\ldots,A_{t+d+1}.       \tag{1.1}
\]

To include both adjacent owner turns used by the directed q2 identity,
protect the conservative collar

\[
 {cal C}_d(t)=\{t-1,t,\ldots,t+d+2\}\subseteq\mathbb Z_L. \tag{1.2}
\]

Thus disjoint protected collars imply disjoint literal histories, changed
owner edges, and q2 halos.  The collar is deliberately one position larger
on each side than the source fragment; no claim of optimality is needed.

Suppose the forced cool-lex sibling pair uses consecutive changed edges at
times `t,t+1`.  Its combined protected collar is

\[
 {cal F}_d(t)={\cal C}_d(t)\cup{cal C}_d(t+1)
              =\{t-1,\ldots,t+d+3\}.                \tag{1.3}
\]

### Lemma 1.1 (exact bad-anchor interval)

Assume `L>2d+8`.  An optional packet starting at `s` has
`C_d(s) cap F_d(t) != emptyset` if and only if

\[
                    s\in\{t-d-3,\ldots,t+d+4\}.     \tag{1.4}
\]

There are exactly `2d+8` bad anchor positions.

#### Proof

Lift the two cyclic intervals to integers without wrap.  The intervals

\[
 [s-1,s+d+2],\qquad [t-1,t+d+3]
\]

meet exactly when

\[
 s-1\le t+d+3\quad\hbox{and}\quad s+d+2\ge t-1.
\]

These inequalities are equivalent to (1.4), whose inclusive cardinality
is `2d+8`.  `square`

Without the inequality on `L`, (1.4), interpreted cyclically, is still the
exact finite conflict set; it may simply fill the whole cycle.

## 2. PBBS phase rotation removes the third incidence

Let the ground size be

\[
                            n=2m+1.                \tag{2.1}
\]

The PBBS ground rotations of a clean hook-angle C6 preserve its component
triple, its orientation, and all q1/q2 identities.  On each shore, the `n`
rotates of its selected old factor edge are distinct.  Indeed, a
nonidentity ground rotation cannot fix a rank-`m` endpoint because
`gcd(m,2m+1)=1`; and an odd-order rotation cannot interchange the two
endpoints of an edge.

### Theorem 2.1 (degree-three separation)

Assume that:

1. two forced sibling packets occupy consecutive edges on their common
   child shore;
2. an optional third incident packet has its other two shores fresh, as in
   a loose-tree placement; and
3. source histories are lifted in the aligned form (1.1).

If

\[
                           2m+1>2d+8,               \tag{2.2}
\]

then one ground rotation of the optional packet has protected collar
disjoint from the forced pair on the reused shore.  Consequently the three
local incidences admit simultaneous depth-`d` source histories and
pairwise-disjoint q2 halos, except for the already authenticated directed
head-to-tail overlap inside the forced sibling pair.

#### Proof

By Lemma 1.1 the forced pair forbids only `2d+8` anchor edges on the reused
factor cycle.  Ground rotation gives `2m+1` distinct candidate anchor
edges.  Under (2.2), at least one candidate lies outside the forbidden
set.  Its conservative collar is disjoint from the forced collar, while
its other two shores are fresh by hypothesis.

The forced pair itself has compatible minimal histories by the exact
two-consecutive-packet screen theorem: its outgoing and incoming two-set
screens are disjoint and its common rank-`(r-4)` body partitions into
`d-1` nonempty history letters.  Adding the separated optional history
therefore creates no source conflict.  Collar disjointness also separates
the optional q2 halo, and the sibling head-to-tail overlap is handled by
the directed-halo telescoping theorem.  `square`

Since `d=Theta(sqrt(m))`, (2.2) holds for all sufficiently large `m`.

### Corollary 2.2 (exact finite multi-shore criterion)

For an optional packet with rotation index `j in Z_n`, let `e_C(j)` be its
anchor edge on every reused component `C`.  Let `B_C` be the finite set of
anchor edges whose protected collars meet the already planted collars on
`C`.  Then a legal rotation exists if and only if

\[
 \mathbb Z_n\setminus
 \bigcup_C\{j:e_C(j)\in B_C\}\ne\varnothing.        \tag{2.3}
\]

Moreover,

\[
 \left|\{j:e_C(j)\in B_C\}\right|\le |B_C|,        \tag{2.4}
\]

because `j -> e_C(j)` is injective.  Hence the sufficient scalar test

\[
                         n>\sum_C |B_C|             \tag{2.5}
\]

handles any bounded collection of reused shores.  Equation (2.3), rather
than (2.5), is the exact criterion when the forbidden sets overlap in
rotation phase.

## 3. The first upper casualty does not cancel across a sibling pair

One common-history clean C6 is internally exact through width `d+2`.  On a
role with clean core `K`, active labels `c,a_(i-1),a_i`, and a private
singleton left prefix `p_i`, its old width-`d+3` value is

\[
 T_i=K\cup\{c,a_{i-1},a_i,p_i\},                  \tag{3.1}
\]

whereas the rethreaded role offers

\[
 \widehat T_i=K\cup\{c,a_i,a_{i+1},p_i\}.         \tag{3.2}
\]

The label `p_i` certifies that (3.1) is not recreated elsewhere in that
displayed role.

Two consecutive cool-lex sibling packets share exactly one child
component.  Each packet therefore still has a role on a shore not changed
by the other packet.

### Theorem 3.1 (no context-free sibling cancellation)

The compound switch of two consecutive sibling packets has no universal
width-`d+3` upper-cancellation identity.

#### Proof

Choose a nonshared role of the first packet and adjoin a fresh singleton
left prefix `p`, appearing in no other displayed role.  Equations
(3.1)--(3.2) give an old rank-`(r+2)` target `T` which is absent from the
first packet's rethreaded displayed family.  The second packet has no
changed fragment on this shore, and none of its displayed intervals
contains `p`.  It therefore contributes neither `T` nor an opposite signed
occurrence carrying the same private label.  Hence the signed local upper
damage of the first packet survives in the compound displayed family.
`square`

This does not assert that `T` is absent from a completed global word: an
independent protected witness may represent it elsewhere.  It proves the
precise negative needed here: sibling pairing alone cannot be the theorem
which supplies arbitrary-width upper transparency.

## 4. Consequence and remaining gate

The degree-three source-packing issue is asymptotically local: the forced
pair costs one interval of `2d+8` forbidden rotation phases, while PBBS
supplies `2m+1` phases.  Thus it is not a new Catalan-scale obstruction.

By contrast, the first upper boundary remains genuinely external.  Even
after all lower depths, q1, q2, positive residence, and the degree-three
source collars are coordinated, a protected alternative-witness reservoir
or a correlated exterior permutation is still required from width `d+3`
onward.  The existing three-ring clipped upper-cone reservoir supplies the
right local witness type, but a simultaneous global planting theorem for
the full packet tree is not proved here.

## 5. Scope

The rotation theorem assumes the standard aligned source lift and fresh
nonshared shores.  Corollary 2.2 is the proof-safe criterion when more
shores are reused.  The result does not prove zero-gap residence, a global
upper-reservoir packing, typed maximal-common-cap routing, or one final
Euler serialization.
