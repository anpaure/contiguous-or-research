# A sharp hypercube local-fault obstruction to further generic path-cover contraction

**Date:** 2026-08-05  
**Method:** pure mathematics; no finite computation, enumeration, or solver  
**Status:** unconditional lower bound for infinitely many cube dimensions.
It shows that Hamilton decompositions and four-cycle switches cannot improve
the aligned-cube path count using only the per-vertex fault-ledger bounds.

## 0. Outcome

The aligned Catalan-cube theorem reduces the bi-core seam problem inside a
large cube `Q_m` to a directed local-fault model:

* every vertex has at most `h` target-forbidden coordinate directions;
* every vertex has at most `h` source-forbidden coordinate directions;
* an arc is usable only when it passes both endpoint tests.

Automorphism averaging gives a path cover with

\[
 O\!\left({h\over m}2^m\right)                     \tag{0.1}
\]

components.  This order cannot be improved from those two cardinality
bounds alone.

### Theorem

Let

\[
 m=2^q-1,
 \qquad 1\le h\le m+1.
\]

There are target-forbidden sets `A_v subseteq [m]`, `|A_v|<=h`, and empty
source-forbidden sets such that every directed path cover of `Q_m` using
only allowed arcs has at least

\[
 {h\over m+1}2^m                                    \tag{0.2}
\]

path components.

Thus (0.1) is sharp up to an absolute factor.  In particular, a Hamilton
decomposition of `Q_m`, additional edge-disjoint Hamilton cycles, or
unpriced four-cycle symmetric differences cannot by themselves reduce the
cover to `2^{O(h)}` or `O(1)` components.

## 1. Hamming-code construction

Let `C` be the binary Hamming code of length

\[
 m=2^q-1.
\]

It has size

\[
 |C|={2^m\over m+1},                                \tag{1.1}
\]

minimum distance three, and covering radius one.  Its `m+1` cosets
partition `Q_m`; every coset is itself a perfect one-error-correcting code.

Choose `h` distinct cosets and let `S` be their union.  Then

\[
 |S|={h\over m+1}2^m.                               \tag{1.2}
\]

### Lemma 1.1

Every vertex of `Q_m` has at most `h` neighbours in `S`.

#### Proof

Fix one chosen coset `C'`.  If `v in C'`, minimum distance three implies
that `v` has no neighbour in `C'`.  If `v notin C'`, perfection of `C'`
gives exactly one member of `C'` at distance one from `v`.  Summing over
the `h` chosen cosets gives at most one neighbour from each coset, hence at
most `h` altogether. `square`

## 2. The fault ledger

For every vertex `v`, define

\[
 A_v=\{j\in[m]:v\oplus e_j\in S\},                 \tag{2.1}
\]

and put its source-forbidden set equal to the empty set.  Lemma 1.1 gives

\[
 |A_v|\le h.                                        \tag{2.2}
\]

Declare an arc `u -> v=u xor e_j` unusable at its target exactly when
`j in A_v`.

### Lemma 2.1

Every `s in S` has allowed outdegree zero.

#### Proof

For every coordinate `j`, put `v=s xor e_j`.  Then

\[
 v\oplus e_j=s\in S,
\]

so `j in A_v` by (2.1).  Hence the arc `s -> v` fails at its target.  This
holds in all `m` coordinate directions. `square`

## 3. Path-cover lower bound

Every member of `S` can occur only as the terminal vertex of a directed
allowed path.  One path has at most one terminal vertex.  Consequently
every allowed directed path cover has at least `|S|` components.  Equation
(1.2) gives (0.2). `square`

## 4. Consequence for the MSW cube programme

The fault ledger above is an abstract ledger; it is not asserted to arise
from actual MSW departure sets.  Its role is exact and limited:

\[
 \boxed{
 \text{the inequalities }|A_v|,|B_v|\le h
 \text{ alone cannot imply a smaller-order path cover.}}
\]

Therefore a contraction beyond `Theta(h2^m/m)` must use additional
correlation specific to the MSW cores, for example:

1. a structural restriction on which neighbouring targets can forbid the
   same source;
2. an all-cut expansion theorem for the actual bi-core arc graph;
3. cross-cube exchanges whose endpoint faults telescope; or
4. a collar/trace absorber chosen jointly with the cube-cycle breaks.

A Hamilton decomposition supplies more switching edges, but the Hamming
code construction makes every one of those edges point outward from a
forced terminal through a target-forbidden direction.  No sequence of
four-cycle switches can change the need for one terminal per member of
`S` without invoking structure absent from the local ledger.
