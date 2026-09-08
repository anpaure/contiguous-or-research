# Native MSW common-history fusion reduces to a same-forced-rail graph, with an exact multiport criterion

**Date:** 2026-08-13  
**Status:** unconditional local theorem and exact global reduction.  The
same-forced transposition graph is computationally connected in the ranges
listed below, but its all-dimensional connectivity and a port-separated
spanning tree remain open.

## 0. Outcome

Put

\[
 n=2m+1,\qquad R=m+1,\qquad s=R-d=m+1-d.             \tag{0.1}
\]

For a canonical tight MSW row with cyclic coordinate order
`w=(w_i)_(i in Z_n)`, define, at a cut `a`,

\[
 P_j(w,a)=\{w_{a+j},\ldots,w_{a+j+s-1}\},\qquad
 F_j(w,a)=\{w_{a+j},w_{a+j+s-1}\}                  \tag{0.2}
\]

for `0<=j<d`.  The exact resident-history criterion says that two rows
admit a common literal length-`d` source history precisely when, after
choosing orientations and cuts,

\[
 F_j(w,a)\cup F_j(v,b)
   \subseteq P_j(w,a)\cap P_j(v,b)\quad(0\le j<d).  \tag{0.3}
\]

There is a much simpler sufficient relation:

\[
                    F_j(w,a)=F_j(v,b)\quad(0\le j<d). \tag{0.4}
\]

It is the equality of two cyclic boundary rails of length `d`, separated
by `s-1` positions in the tight words.  Under (0.4), use those common
two-element sets as the literal history letters.  No cross-containment
check remains.

The graph on Dyck roots whose edges are root transpositions satisfying
(0.4) is the **same-forced transposition graph**.  A spanning tree in this
graph, together with separated ports at every row, serializes every tight
MSW source circuit into one source Euler circuit.  It preserves the
complete occurrence-labelled source subword deck through width `d+1`, and
therefore every owner and every strict-lower compiler cell, at zero added
positions.

The necessary simultaneous-port statement is not pairwise automatic.  It
is supplied by the multi-block lemma below.

## 1. The exact word-coordinate criterion

Let the owner cycle on `w` be the cyclic rank-`R` interval trace.  Its
maximal depth-`d` antecedent letter at position `a+j` is the rank-`s`
interval `P_j(w,a)`.  Its exact forced set consists of the coordinate
deleted after that interval and the coordinate inserted `d+1` owner steps
earlier.  In tight cyclic interval coordinates these are exactly its two
endpoints, namely `F_j(w,a)` in (0.2).

Thus Theorem 5.1 of
`MATH_THEOREM_RESIDENT_JOHNSON_FORCED_PAIRS_AND_COMMON_HISTORY_CRITERION_20260805.md`
specializes literally to (0.3).

### Lemma 1.1 (same-forced rails)

If (0.4) holds, the two rows admit antecedents with the common history

\[
                         H_j=F_j(w,a)=F_j(v,b).       \tag{1.1}
\]

Equivalently, after possibly reversing either tight order, the unordered
endpoint pairs of the two length-`s` sliding intervals agree for `d`
successive starts.  A stronger ordered certificate is either

\[
\begin{aligned}
 w_{a+j}&=v_{b+j},&
 w_{a+s-1+j}&=v_{b+s-1+j},
\end{aligned}                                      \tag{1.2}
\]

for every `j`, or the same identities with the two rails crossed.

#### Proof

The common set (1.1) contains both forced sets.  Each forced set lies in
its own maximal interval, so (1.1) lies in both maximal intervals.  This is
(0.3), and the common-history criterion applies.  Identities (1.2) imply
the unordered equality (0.4).  \(\square\)

## 2. Several histories on one row

The one-block freedom theorem changes one cyclic block of at most `d`
source letters.  A root of degree greater than one in a fusion tree needs
several such changes simultaneously.  Pairwise compatibility does not by
itself justify that operation.

Let `B` be a union of disjoint cyclic intervals of source positions.  At
every `j in B`, choose a nonempty letter `H_j` satisfying

\[
                         F_j\subseteq H_j\subseteq P_j. \tag{2.1}
\]

Retain the maximal letter `P_j` outside `B`.

### Theorem 2.1 (multi-block freedom)

If every cyclic connected component of `B` has length at most `d`, then
the modified word is still a depth-`d` antecedent of the original owner
cycle.

In particular, any collection of length-`d` port blocks separated by at
least one untouched source position may be installed simultaneously.

#### Proof

Fix one coordinate and unwrap one of its positive owner runs.  Its maximal
source carrier is an interval `E`.  Every endpoint of `E` remains selected:
if it belongs to `B`, it belongs to the forced set at that position and is
retained by (2.1); otherwise the maximal letter is unchanged.

Consider consecutive retained carrier positions.  If they were not
consecutive in the maximal support, the omitted positions between them lie
in one cyclic connected component of `B`; two different components are
separated by an untouched maximal carrier position.  Hence at most `d`
positions are omitted between consecutive retained positions, so their
gap is at most `d+1`.  The bounded-gap support characterization then says
that every owner window containing the coordinate is still hit.  The same
cyclic argument treats a coordinate constant on the owner cycle.  Applying
this coordinatewise proves the antecedent equations.  \(\square\)

### Corollary 2.2 (port capacity)

One tight row of length `n` supports at most

\[
                         \left\lfloor{n\over d+1}\right\rfloor \tag{2.2}
\]

pairwise separated length-`d` ports.  Conversely, any selected ports with
cyclic start gaps at least `d+1` satisfy Theorem 2.1.

## 3. The exact global graph target

Let `G_sf(m,d)` have the `Cat_m` Dyck roots as vertices.  Join two roots
when:

1. their binary roots differ by one `1/0` transposition; and
2. some orientations and cuts of their tight MSW orders satisfy (0.4).

A proof sufficient for global source fusion is now:

> **Separated-port spanning-tree theorem.**  For all sufficiently large
> target parameters, `G_sf(m,d)` has a spanning tree `T` and an assignment
> of one witnessing length-`d` port at each incidence `(root,edge)` such
> that ports assigned to one root are cyclically separated by an untouched
> position.

By Theorem 2.1, install all histories incident with one row simultaneously.
Every tree edge is then a common de Bruijn vertex between its two row
circuits.  Splicing along the tree gives one Euler circuit.  The common-
vertex short-deck theorem preserves every literal subword occurrence of
length at most `d+1`.

Ordinary connectivity of `G_sf(m,d)` is not enough: an arbitrary spanning
tree can have too many incident ports at a row or overlapping port blocks.
A Hamilton path would give degree at most two, but even then the two ports
must be distinct and separated unless their requested history letters
coincide consistently on the overlap.

## 4. Exact finite census on H100

The verifier is
`scratch/audit_msw_common_history_graph.cpp`.  It reconstructs every
canonical tight order, every orientation and cut, and applies (0.3) and
(0.4) exactly.  Heavy runs were executed only on `h100`.

For the same-forced transposition graph:

\[
\begin{array}{c|c|c|c|c|c}
m&d&|V|&|E|&\delta&\Delta\\ \hline
8&3&1430&5405&2&24\\
9&3&4862&38339&6&48\\
10&3&16796&221021&10&76
\end{array}                                         \tag{4.1}
\]

Every graph in (4.1) is connected and all vertices are active.  The
stronger ordered-rail subgraph (1.2) is also connected, with respectively
`5382`, `38277`, and `220895` edges and the same displayed minimum and
maximum degrees.

There is a useful threshold diagnostic at `m=10=3d+1`.  Every nonmaximum-
area Dyck root has at least one area-increasing same-forced transposition.
Choosing such parents greedily toward the mountain gives an arborescence
with at most three children per root.  At `m=8,9`, respectively `20,1`
nonmaximum roots have no increasing same-forced neighbour.  This suggests
an eventual monotone proof, but the greedy tree has not yet been assigned
separated witness ports, and the observation through one value of `d` is
not a theorem.

The full compatibility transposition graph is connected at

\[
 (m,d)=(8,3),(9,3),(10,3),(11,4),(12,4),             \tag{4.2}
\]

with edge counts `7494,56236,328821,722641,4265503`.
These are finite facts, not an all-dimensional proof.

Two tempting smaller graph claims are false in this range:

1. equality of the complete maximal histories has zero transposition
   edges at `m=8,9,10`;
2. requiring an adjacent binary transposition disconnects the same-forced
   graph (at `m=10,d=3` it has `52` components).

Thus an all-dimensional proof must permit nonadjacent root transpositions
and exploit the endpoint-rail identity, not equality of maximal letters.

### 4.1 Four local promotion patterns

Orient root transpositions toward larger Dyck area, so a zero at `p` moves
rightward to a one at `q`.  At `m=10,d=3`, selecting a shortest available
area-increasing same-forced move at every nonmountain root yields only

\[
              01\to10,\qquad001\to100,\qquad
              011\to110,\qquad0011\to1010.           \tag{4.3}
\]

There are `16665` adjacent moves and respectively `35,43,52` moves of the
three longer types.  The four types are exactly a valley rotation, with an
optional neighbouring zero, one, or both absorbed into the transposition.
This is a finite classification of the chosen census moves, not yet a
symbolic exhaustiveness theorem.

The exact MSW recursion

\[
 \rho(1u0v)=\bigl(c,c-\rho(\mu u),1,c+\rho(v)\bigr) \tag{4.4}
\]

turns a contextual leaf rotation into one of the two block permutations
recorded in equations (4.17)--(4.18) of
`MATH_THEOREM_MSW_FIXED_SLOT_COMPENSATION_CUBE_20260727.md`.  A prospective
proof of connectivity should split the complement of the local block into
the three recursive context regions.  Their total semilength is `m-O(1)`;
if `m>=3d+1`, one region has length at least `d`.  The missing lemma is that
such a region supplies the common ordered endpoint rail (1.2) for one of
the four rotations (4.3).  Proving that implication would give a canonical
area-increasing parent at every nonmountain root and hence connectivity.
The H100 facts support this lemma at `m=10,d=3`, but do not prove it.

## 5. Why the published MNW hypertree is not an automatic shortcut

The published MNW conflict-free spanning hypertree concerns the
rotational/lexical middle-levels path factor.  The present vertices are the
canonical tight MSW minimum wreaths.  The standard pull has old-edge
distribution `2+1` between two rotational-factor components and is not a
three-native-wreath trade.  Therefore its connectivity does not identify
the native graph `G_sf(m,d)`.

Moreover, MNW conflict-freeness says that the marked canonical path edges
selected by different flipping cycles are distinct.  It does not say that
the corresponding length-`d` source blocks in a tight antecedent have an
untouched position between them.  Hence it does not imply Theorem 2.1's
simultaneous-port hypothesis even if a future provenance conjugacy is
found.

## 6. Frozen boundary

The common-history route strictly dominates the bare `q`-safe seam route
for the middle/lower/source problem: once a separated-port spanning tree
is found, every source interval through owner width is preserved literally,
not merely resident.

The exact remaining native theorem is nevertheless two-part:

\[
 \boxed{\text{prove same-forced transposition connectivity and choose a
 separated-port spanning tree.}}                    \tag{6.1}
\]

Neither part follows from the finite census.  The long upper deck, whose
intervals have width at least `d+2`, remains a later opening/current gate.
