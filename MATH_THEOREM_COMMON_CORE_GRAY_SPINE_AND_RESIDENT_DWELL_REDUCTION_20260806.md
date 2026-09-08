# Common-core Gray spine and the resident dwell reduction

**Date:** 2026-08-06  
**Method:** an exact Boolean-to-Johnson embedding and cyclic interval
detours; no computation or search  
**Status:** unconditional spine/dwell theorem and a sharp port reduction.
It supplies a one-component ordering language for the exponentially large
common-core target bank.  It does not yet prove that all opened detours can
be assigned pairwise distinct physical owners and both immediate palettes
while retaining the pre-existing protected reservoir.

## 1. Exact Boolean-to-Johnson spine

Let

\[
 K=\{k_1,\ldots,k_{m-1}\},\qquad |E|=m,
 \qquad K\cap E=\varnothing .
\]

For every nonempty `T subseteq E`, put `q=|T|` and define

\[
 D_q=\{k_1,\ldots,k_{q-1}\},\qquad
 U(T)=(K\setminus D_q)\cup T.                    \tag{1.1}
\]

Then `|U(T)|=m`.

### Theorem 1.1 (common-core Gray spine)

The map `T mapsto U(T)` is injective.  If `T'` is obtained from `T` by
toggling one external coordinate, then `U(T)` and `U(T')` are adjacent in
the rank-`m` Johnson graph on `K union E`.

More explicitly, if `T'=T union {e}` and `q=|T|`, then

\[
 U(T')=U(T)-\{k_q\}+\{e\}.                       \tag{1.2}
\]

The immediate lower and upper colours of this edge are

\[
 I(T,e)=(K\setminus D_{q+1})\cup T,              \tag{1.3}
\]

and

\[
 A(T,e)=(K\setminus D_q)\cup T\cup\{e\}.        \tag{1.4}
\]

#### Proof

The external trace of `U(T)` is exactly `T`, proving injectivity.  Formula
(1.2) is immediate from `D_(q+1)=D_q union {k_q}`.  Taking its intersection
and union with `U(T)` gives (1.3)--(1.4).  \(\square\)

Thus every simple Gray walk on nonempty external traces lifts literally to
a simple Johnson walk.  No matching, rounding, or chronology theorem is
used in this lift.

### Corollary 1.2 (immediate-palette multiplicity)

Along a simple Gray path, every lower colour (1.3) and every upper colour
(1.4) occurs at most twice.

#### Proof

The external trace of (1.3) is the smaller endpoint `T`.  A simple path has
at most two edges incident with a given vertex, so this value occurs at most
twice.  (At a local rank minimum both incident edges can indeed have the
same lower colour, so multiplicity one would be false.)

The external trace of (1.4) is the larger endpoint `T union {e}`.  A path
has at most two incident edges at one vertex, so that value has multiplicity
at most two.  \(\square\)

The upper multiplicity two is harmless for a protected skeleton: it is a
bounded exposure, not a claim of a globally rainbow upper palette.

## 2. A long dwell block inside every common-core target

Fix `T subseteq E` of size `2<=q<=m-1`, and put

\[
 h=m-q,\qquad 1\le h\le m-2.
\]

Give `K` its cyclic order and let

\[
 W_j=\{k_j,k_{j+1},\ldots,k_{j+h-1}\},
 \qquad j\in\mathbb Z/(m-1)\mathbb Z.             \tag{2.1}
\]

Define

\[
                         V_{T,j}=T\cup W_j.         \tag{2.2}
\]

### Theorem 2.1 (resident external dwell cycle)

The owners `(V_(T,j))` form a simple Johnson cycle of length `m-1` inside
`binom(K union T,m)`.  Their union is `K union T`; every external coordinate
of `T` occurs throughout the cycle; and every `K`-coordinate has one cyclic
positive run of length exactly `h` and one cyclic zero gap of length exactly
`q-1`.

In particular, opening this cycle gives a target witness of length `m-1`
whose external trace is held fixed for at least `d+1` owner positions for
all sufficiently large `m`.

#### Proof

Successive cyclic `h`-windows delete one `K`-coordinate and insert the next,
so consecutive owners are Johnson adjacent.  Distinct starting positions
give distinct windows because `1<=h<m-1`.  Their union is all of `K`, and
adjoining the fixed set `T` proves the target-union assertion.  A fixed
`K`-coordinate belongs to exactly `h` consecutive cyclic windows.  The
remaining `q-1=(m-1)-h` windows form its zero gap.  Finally `m-1>d` at the
deadline scale `d=O(sqrt(m))`.  \(\square\)

The internal `K` runs need not themselves be `d`-resident when `q` or `h`
is small.  This theorem is used as an **external-coordinate dwell block**;
the `K`-coordinate endpoint flags must be joined in the port theorem below.

## 3. Residence becomes a port-order problem

Let a Gray path be

\[
 T_1,T_2,\ldots,T_N,
\]

and replace every state of rank between two and `m-1` by one opened dwell
cycle from Theorem 2.1.  At a Gray edge which inserts `e`, choose the last
`K`-window of the old block and the first `K`-window of the new block so
that

\[
                         W'\subset W,
 \qquad |W-W'|=1.                                  \tag{3.1}
\]

At a deletion edge use the reverse containment.  Equation (3.1) makes the
two port owners Johnson adjacent.

### Theorem 3.1 (external residence from dwell)

Assume the opened dwell blocks admit endpoint choices satisfying (3.1) at
every Gray seam.  Then every nonconstant positive run and every nonconstant
zero gap of every external coordinate has length at least `d+1`, except
possibly at the two linear endpoints and at a singleton-trace block whose
two Gray neighbours both delete that singleton.

The latter event cannot occur at an internal singleton vertex of a simple
Gray path on nonempty subsets: every neighbour of `{e}` has the form
`{e,f}` and still contains `e`.  Thus only the two global endpoints remain.

#### Proof

Membership of an external coordinate is constant throughout each dwell
block.  Between two consecutive flips of that coordinate, the Gray path
contains at least one whole intervening vertex block.  Every nonsingleton
block has `m-1>d` owners by Theorem 2.1.  At a singleton `{e}`, both internal
neighbours contain `e`, so its one-owner block lies inside, rather than at
an endpoint of, the positive run.  The same argument applies to a zero gap.
Only the two ends of a linear Gray path have no block on one side.  \(\square\)

This removes the apparent need for a run-length-limited Gray code.  Ordinary
one-bit Gray order is sufficient once each trace carries a long physical
dwell.

## 4. The one-bit adjacency ports close explicitly

An opened cycle (2.2) has endpoint windows which are adjacent on the cyclic
`K`-window graph.  The adjacency part of the port problem has an exact
solution.

### Theorem 4.1 (phase-propagated Gray ports)

Let `T_1,...,T_N` be any one-bit Gray path, put

\[
 h_i=m-|T_i|,
\]

and choose signs `epsilon_i in {+1,-1}`.  Starting from any phase `a_1`,
open the cyclic dwell for `T_i` into the long path which starts at
`W_(a_i)^(h_i)`, visits every cyclic `h_i`-window once, and ends at the
adjacent window `W_(a_i+epsilon_i)^(h_i)`.  Put

\[
                         a_{i+1}=a_i+\epsilon_i
                         \pmod {m-1}.               \tag{4.1}
\]

Then the last owner of block `i` and the first owner of block `i+1` are
Johnson adjacent.  If the Gray path is cyclic and

\[
                         \sum_i\epsilon_i=0
                         \pmod {m-1},               \tag{4.2}
\]

the last-to-first seam is Johnson adjacent as well.

#### Proof

Suppose first that `T_(i+1)=T_i union {e}`.  Then
`h_(i+1)=h_i-1`.  At the common phase `a_(i+1)`, choose the shorter cyclic
window by deleting the appropriate endpoint of the old window.  Thus

\[
 W_{a_{i+1}}^{h_i-1}\subset W_{a_{i+1}}^{h_i}
\]

with difference one.  The external trace gains exactly `e`, so the two
owners differ by one Johnson swap.  For a deletion Gray edge use the reverse
containment.  Equation (4.1) handles every internal seam, and (4.2) gives
the same containment at the cyclic closing seam.  \(\square\)

Thus the **owner-adjacency** portion of the Gray-dwell port lemma is closed;
no matching is needed.  What remains at a seam is only the nested
residence flag: the endpoint of one opened cyclic dwell may split one short
prefix or suffix of a `K`-coordinate run, and the adjacent block must retain
that coordinate for the missing number of steps.

There is a particularly useful central band.  If

\[
                 d+2\le |T|\le m-d-1,              \tag{4.3}
\]

then the **cyclic** dwell block itself is biresident, because its `K` runs
have length `m-|T|>=d+1` and its `K` gaps have length `|T|-1>=d+1`; its
external coordinates occur throughout.  Hence only the run/gap which is
split by the chosen opening needs a seam extension.  The two tails outside
(4.3) contain only `2^{o(m)}` traces.

## 5. Exact residual residence/resource gate

The absence of an ordinary Hamilton Gray cycle on the whole consecutive
band is not an obstruction.  The published saturating-cycle theorem gives
the following exact substitute.

### Theorem 5.1 (square-Gray ordering of a consecutive band)

Let

\[
 \mathcal B=\{T\subseteq E:a\le |T|\le b\},
 \qquad 0\le a<b\le m,
\]

and assume every boundary vertex has a cube neighbour in the band (in
particular this holds when `0<a<b<m`).  There is a cyclic ordering of every
member of `mathcal B` exactly once in which consecutive traces have Hamming
distance one or two.

Under the spine map (1.1), consecutive owners in this order have Johnson
distance at most two.

#### Proof

Apply the Gregor--Micka--Mutze saturating-cycle theorem to the consecutive
cube levels `a,...,b`.  It gives a cycle containing every vertex of the
smaller bipartition class.  Let `C` be that class and let `D_0` be the
vertices of the other class already on the cycle.

Assign every omitted vertex `v` of the other class to an arbitrary neighbour
`c(v) in C` lying in the band.  At a cycle segment

\[
                         x,c,y
\]

list the omitted vertices assigned to `c` as `v_1,...,v_t` and replace the
segment by

\[
                         x,v_1,\ldots,v_t,c,y.       \tag{5.1}
\]

All `v_j` and `x` are distinct cube neighbours of `c`; hence consecutive
members of the inserted list have Hamming distance two, while `v_t,c` and
`c,y` have distance one.  The lists partition the omitted vertices, so the
result is the required cyclic ordering.

For two traces at Hamming distance one, Theorem 1.1 gives Johnson distance
one.  At Hamming distance two, either one external coordinate is exchanged
and the core prefix is unchanged, giving Johnson distance one, or two
external coordinates are inserted/deleted and the core prefix changes by
two, giving Johnson distance two.  \(\square\)

For the middle band `(4.3)`, Theorem 5.1 orders all but only
`2^{o(m)}` tail traces on one square-Gray cycle.  A distance-two seam needs
at most one intermediate owner abstractly.  A literal simple realization
must choose that intermediate outside the owner set already exhausted by
the dwell blocks; a noncyclic `K`-profile detour is the natural reserve.

For a one-bit trace order, Theorem 4.1 has eliminated owner adjacency.
The remaining statement is:

> **Gray-dwell residence/resource lemma.**  Choose the opening signs and,
> when necessary, bounded monotone `K`-window ears so that the split endpoint
> run/gap flags are extended for `d+1` steps, while all owner, lower-`q1`, and
> protected upper roles remain distinct.

If this lemma holds with pairwise distinct owner, lower-`q1`, and protected
upper resources, the exponentially large common-core reservoir can be
placed in one chronology.  Theorem 3.1 supplies external residence, while
the ordered nested-port bridge supplies the remaining `K`-coordinate
residence.

## 6. Scope

Proved here:

1. an exact injective Boolean-to-Johnson Gray spine;
2. lower- and upper-`q1` multiplicity at most two on it;
3. an explicit length-`m-1` dwell cycle witnessing every common-core target
   with `2<=|T|<=m-1`; and
4. automatic external-coordinate residence after dwell expansion; and
5. exact owner-adjacent propagation of all one-bit Gray seams; and
6. a one-component distance-at-most-two ordering of every trace in a
   consecutive central band.

Not proved here:

1. the simultaneous endpoint residence flags in the Gray-dwell
   residence/resource lemma;
2. collision-free noncyclic intermediate owners at the distance-two seams;
3. global resource-disjointness of all dwell blocks;
4. the full PBBS upper occurrence bank outside this common-core family;
5. terminal compiler/common-cap transport; or
6. `nu(k)<=B(k)+O(1)`.

The gain is a quantifier reduction: the `2^m` clipped paths need not be
Hamiltonized by an arbitrary connector matching.  They have a canonical
one-bit spine, and residence reduces to compatible openings of explicit
cyclic dwell blocks.
