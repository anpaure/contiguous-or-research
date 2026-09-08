# MSW cut rigidity and the exact obstruction to core-safe Dyck Gray edges

**Date:** 2026-08-05  
**Method:** pure mathematics; no finite computation, enumeration, or solver  
**Status:** unconditional rigidity theorem and sharp edgewise obstruction.
The existence of a specially chosen alternating core-safe Hamilton path in
the Dyck transposition graph remains open.

## 0. Outcome

The alternating core-safe Dyck Gray-code programme cannot obtain extra
freedom by cyclically cutting or rerooting the canonical MSW wreaths.

For `x in D_r`, let

\[
 C(x)=P(x)+e_x,
 \qquad e_x=\{x,\bar x\},
\]

be the canonical MSW cycle in `G_r^+`.  The closure `e_x` is the unique
edge of `C(x)` outside the bipartite incidence graph `G_r`.

The only edge which can be removed from `C(x)` so that the remainder is an
incidence path with two rank-`r` endpoints is `e_x`.  Therefore the only
admissible fixed-half paths are

\[
 P(x)\quad\text{and its reversal}.
\]

In particular, the forward and reverse forbidden core sets are invariants
of the protected MNW half-projection.  A cyclic change of the written start
of the wreath does not change either set, and cutting any incidence edge
destroys the required half-projection.

There is also a sharp local obstruction.  If a Dyck transposition edge is

\[
 y=x-\{a\}+\{b\},
 \qquad x_a=1,\quad x_b=0,
\]

then it can enter the component of `x`

* in forward sign exactly when `a` survives the first `h` forward MSW
  departures;
* in reverse sign exactly when `b` survives the first `h` reverse MSW
  departures.

Some Dyck transposition edges fail both conditions.  For every `r>=2` and
every `h>=1`, the edge

\[
 1^r0^r
 \longleftrightarrow
 10\,1^{r-2}0^{r-2}\,10
\]

is unsafe in both signs.  Hence neither alternating parity nor wreath
rerooting can make an arbitrary transposition Gray code core-safe.  A
positive proof must construct a Hamilton path which avoids all such doubly
forbidden edges and satisfies the remaining forced-parity constraints.

## 1. The canonical wreath

Write

\[
 P(x)=(X_0,Y_0,X_1,Y_1,\ldots,Y_{r-1},X_r),
 \qquad X_0=x,\qquad X_r=\bar x,
\]

where the `X_i` have rank `r` and the `Y_i` have rank `r+1`.  Every edge
of `P(x)` belongs to `G_r`, while

\[
 e_x=X_rX_0=\{\bar x,x\}
\]

is a complement edge inside the rank-`r` shore.  Thus

\[
 E(C(x))\setminus E(G_r)=\{e_x\}.                 \tag{1.1}
\]

The MNW Hamiltonization preserves `e_x` and changes only incidence edges.
In the alternative middle-levels lift, removing `e_x` is what exposes the
two endpoints to the vertical matching edges and leaves `P(x)` as the fixed
opposite-half path.

## 2. Cut-rigidity theorem

### Theorem 2.1 (unique admissible cyclic cut)

Let `e` be an edge of `C(x)`.  The graph `C(x)-e` is a path spanning
`V(C(x))`, contained in `G_r`, and having both endpoints in the rank-`r`
shore if and only if

\[
 e=e_x.
\]

Consequently, among all cyclic cuts of the canonical wreath, the only
cut whose suppression is an `r`-edge complementary Johnson geodesic with
all `r` upper colours is the original closure cut.

#### Proof

If `e=e_x`, the remaining path is exactly `P(x)`, so the claim holds.

If `e!=e_x`, then `e` is an incidence edge of `G_r`.  Its endpoints lie on
opposite shores.  Hence `C(x)-e` has one endpoint of rank `r` and one of
rank `r+1`, not two rank-`r` endpoints.  Moreover it still contains the
closure edge `e_x`, which is not an edge of `G_r`.  Thus the remaining path
is not contained in the incidence graph and cannot suppress to a Johnson
path whose every edge is represented by an intervening rank-`(r+1)`
vertex.  This proves uniqueness. `square`

### Corollary 2.2 (no rerooting freedom in the fixed half)

Suppose the MNW closure matching and the exact fixed half-projection
`F_z(H)=P_r` are retained.  For each component `x`, its protected stem can
start only at `x` or at `bar(x)`.  These are precisely the forward and
reverse orientations already encoded by the signed endpoint graph.

Changing the written cyclic origin of `C(x)` while leaving the deleted edge
equal to `e_x` is only a notational rotation: after deletion, the path still
starts at one endpoint of `e_x`.  Changing the deleted edge invalidates
Theorem 2.1.

#### Proof

In the middle-levels lift, the two vertical edges attach at the endpoints
of the fixed incidence path.  Contracting that path and its vertical edges
must recover the retained closure edge `e_x`.  Therefore those endpoints
are `x` and `bar(x)`.  The two traversal directions give the two stated
orientations and no others. `square`

### Remark 2.3 (coordinate rotations do not help)

A single global permutation of the `2r` coordinates is a graph
automorphism.  It relabels the departure sets and every Gray transposition
simultaneously, so core safety is invariant.  Applying unrelated coordinate
permutations to different wreaths is not one automorphism and does not
preserve the MSW vertex partition or the MNW flipping-cycle interfaces.
It therefore supplies no legitimate per-component cut freedom.

## 3. Exact edgewise sign criterion

Let the MSW bit-flip sequence be

\[
 \pi(x)=(\pi_1,\ldots,\pi_{2r}).
\]

Its forward departure coordinates are

\[
 D_h^+(x)=\{\pi_2,\pi_4,\ldots,\pi_{2h}\},          \tag{3.1}
\]

all of which are `1`-positions of `x`.  Starting from `bar(x)` and reversing
the path, the first `h` departure coordinates are

\[
 D_h^-(x)=
 \{\pi_{2r-1},\pi_{2r-3},\ldots,
   \pi_{2r-(2h-1)}\},                                \tag{3.2}
\]

all of which are `0`-positions of `x` and hence `1`-positions of `bar(x)`.
The surviving core sets are their complements within the corresponding
endpoint supports.

### Theorem 3.1 (allowed signs of a Gray edge)

Let `x,y in D_r` differ by one transposition,

\[
 y=x-\{a\}+\{b\},
 \qquad x_a=1,\qquad x_b=0.                         \tag{3.3}
\]

For a stem of depth `h`:

1. the edge can enter `(x,+)` if and only if
   `a notin D_h^+(x)`;
2. the edge can enter `(x,-)` if and only if
   `b notin D_h^-(x)`.

Hence the set of permitted signs at the target `x` is

\[
 S_h(y,x)=
 \{+ : a\notin D_h^+(x)\}
 \cup
 \{- : b\notin D_h^-(x)\}.                          \tag{3.4}
\]

#### Proof

At the forward endpoint `x`, the free-repeat seam deletes the source
coordinate `a` from `x` and inserts `b`.  The literal collar requires the
deleted coordinate to remain in the stem core, which is exactly
`a notin D_h^+(x)`.

At the reverse endpoint `bar(x)`, the same transposition is complemented:
the coordinate deleted from `bar(x)` is `b`.  It remains in the reverse
stem core exactly when `b notin D_h^-(x)`. `square`

### Corollary 3.2 (sharp parity test for a fixed Gray order)

Let `x_1,...,x_C` be a transposition Gray order and orient its vertices with
alternating signs.  It is core-safe if and only if there is a choice of the
initial sign such that

\[
 \operatorname{sign}(x_i)\in S_h(x_{i-1},x_i)
 \qquad(2\le i\le C).                                \tag{3.5}
\]

Thus:

* an incoming edge with `S_h=emptyset` kills the order for both initial
  parities;
* an incoming edge with a singleton `S_h` forces the global parity;
* all singleton constraints must prescribe the same initial parity after
  accounting for the parity of their indices.

This criterion is exact; no cyclic rerooting of the MSW wreaths enlarges
any set `S_h`.

## 4. A uniform doubly forbidden edge

### Theorem 4.1

For every `r>=2`, put

\[
 x_r=1^r0^r,
 \qquad
 y_r=x_r-\{2\}+\{2r-1\}
     =10\,1^{r-2}0^{r-2}\,10.                       \tag{4.1}
\]

Then `x_r,y_r in D_r`, but for every `h>=1`,

\[
 S_h(y_r,x_r)=\varnothing.                           \tag{4.2}
\]

#### Proof

The displayed factorization of `y_r` is a concatenation of three Dyck
words,

\[
 10,\qquad 1^{r-2}0^{r-2},\qquad 10,
\]

with empty middle factor when `r=2`.  Hence `y_r` is Dyck.

For `x_r=1^r0^r`, the MSW recursion is

\[
 \pi(1u0)=
 (2r,\ 2r-\pi(\overleftarrow{\bar u}),\ 1),
 \qquad u=1^{r-1}0^{r-1}.
\]

Here `u` is fixed by reverse-complement.  Its first flip coordinate is
`2r-2` and its last flip coordinate is `1`.  Therefore

\[
 \pi_2(x_r)=2,
 \qquad
 \pi_{2r-1}(x_r)=2r-1.                              \tag{4.3}
\]

The exchanged `1`-coordinate `a=2` is the first forward departure, and the
exchanged `0`-coordinate `b=2r-1` is the first reverse departure.  Both are
forbidden for every `h>=1`.  Theorem 3.1 gives (4.2). `square`

### Consequence 4.2

No argument of the form

> take an arbitrary transposition Gray code, choose its initial alternating
> sign, and reroot each MSW wreath to repair unsafe edges

can work.  The edge (4.1) is intrinsically unsafe in both signs, and
Theorem 2.1 rules out rerooting as a repair.

This does **not** prove that every transposition Gray code contains (4.1),
nor does it refute the alternating core-safe Dyck Gray-code lemma.  It shows
that the lemma is an avoidance-and-parity theorem about a specially chosen
Hamilton path, rather than a formal corollary of the Proskurowski--Ruskey
Gray-code theorem.

## 5. Exact remaining target

Let `T_r` be the Dyck transposition graph.  Direct every incidence
`y--x` toward the signed target states permitted by (3.4).  The unresolved
statement is:

> Find a Hamilton path `x_1,...,x_C` of `T_r` and one initial alternating
> sign such that every incoming incidence obeys (3.5).

The classical Proskurowski--Ruskey theorem supplies a Hamilton path in
`T_r`, but it does not impose (3.5).  The MNW fixed-half theorem supplies
exactly two orientations per wreath, but by Theorem 2.1 supplies no further
cyclic-cut freedom.

Accordingly, the next positive route must either

1. audit and modify the recursive Proskurowski--Ruskey order so that it
   avoids all empty-sign edges and satisfies the forced-parity constraints;
2. prove a new Hamilton-path theorem directly in the signed safe graph; or
3. abandon the exact canonical MSW half-projection and rethread the path
   factor itself, paying for the resulting upper-colour and MNW-interface
   changes.

The cyclic-cut/rotation option is now closed.
