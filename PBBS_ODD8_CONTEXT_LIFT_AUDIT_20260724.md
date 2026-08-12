# Odd-graph alternating-eight normal form, suspension, and the `KG(9,4)` route

Date: 2026-07-24

## Verdict

The certified 45-switch route in `KG(9,4)` contains one genuinely scalable
local object, but not a scalable balanced route by itself.

The positive result is exact: every simple alternating eight-cycle in every
odd graph has one universal four-label normal form.  Consequently its edge
trade has a direct parity-context suspension from `KG(2a+1,a)` to
`KG(2m+1,m)` for every `m>=a`.  This gives an all-dimensional local
connector and, when it meets four distinct point-regular components, an
automatic balanced four-way merger.

The negative result is equally exact: the same parity-context construction
cannot suspend a whole point-regular component.  Along a component the
context is forced to alternate with its complement.  Odd components do not
close, while even components have the wrong point degrees.  In the actual
45-switch certificate, 42 moves depend on cancellation between nonzero
centered vectors of long cut segments.  Only three moves have four
individually centered segments.  Thus the finite route cannot be lifted by
attaching fixed contexts to its 126 vertices.

The remaining scalable gate is now precise: realize the universal local
connector on target-dimensional components while controlling the centered
vectors of the four cut segments.  The local Kneser geometry is no longer an
obstruction; the nonlocal arc-balancing problem is.

No claim about the Wreath Conjecture or the coefficient-one OR bound is made.

## 1. Universal normal form for an odd-graph eight-cycle

For `m>=2`, put

\[
 O_m=KG(2m+1,m),
\]

and let

\[
 V_0,V_1,\ldots,V_7,V_0
\]

be a simple eight-cycle.  For its edge `V_i V_{i+1}`, let `lambda_i` be the
unique omitted coordinate:

\[
 \{\lambda_i\}=[2m+1]\setminus(V_i\cup V_{i+1}).
 \tag{1.1}
\]

### Theorem 1 (four-label normal form)

Up to a dihedral change of the cycle origin and a relabeling of four
coordinates, the edge-label word is

\[
 \boxed{a,b,c,a,d,c,b,d.}
 \tag{1.2}
\]

There is a partition

\[
 [2m+1]=X\mathbin{\dot\cup}Y
 \mathbin{\dot\cup}\{a,b,c,d\},
 \qquad |X|=m-1,\quad |Y|=m-2,
 \tag{1.3}
\]

for which the vertices are

\[
\begin{array}{c|c}
i&V_i\\ \hline
0&X\cup\{b\}\\
1&Y\cup\{c,d\}\\
2&X\cup\{a\}\\
3&Y\cup\{b,d\}\\
4&X\cup\{c\}\\
5&Y\cup\{a,b\}\\
6&X\cup\{d\}\\
7&Y\cup\{a,c\}.
\end{array}
\tag{1.4}
\]

Conversely, (1.3)--(1.4) always define a simple eight-cycle with label word
(1.2).

### Proof

Fix a coordinate `x`, and let `t_x` be the number of edges labeled `x`.
Across an edge not labeled `x`, membership of `x` toggles; on an edge labeled
`x`, both endpoints omit it.  Returning to the initial vertex shows that
`t_x` is even.

Consecutive edge labels are distinct.  Indeed, the standard odd-graph
recurrence is

\[
 V_{i+2}=(V_i\cup\{\lambda_i\})\setminus\{\lambda_{i+1}\}.
 \tag{1.5}
\]

If `lambda_i=lambda_{i+1}`, then `V_{i+2}=V_i`, contrary to simplicity.

Suppose two consecutive cyclic occurrences of `x` as an edge label are at
edge positions `i` and `j`.  Immediately after edge `i`, membership is zero.
The `j-i-1` intervening non-`x` edges toggle membership, and membership must
again be zero at the first endpoint of edge `j`.  Thus the cyclic gap `j-i`
is odd.  It is not one, by the preceding paragraph, so every such gap is at
least three.  Four occurrences would require four odd gaps of total at least
twelve, impossible on eight edges.  Hence every used label occurs exactly
twice.

The eight edge positions are therefore paired into four pairs.  Both cyclic
gaps in one pair are odd and at least three, so they are three and five.  In
other words, positions are paired at distance three in `Z_8`.  The
distance-three graph on `Z_8` is an eight-cycle and has two perfect
matchings, which are dihedrally equivalent.  One is

\[
 \{0,3\},\{1,6\},\{2,5\},\{4,7\},
\]

giving (1.2).

Every coordinate outside `{a,b,c,d}` is never an edge label and therefore
alternates membership at every step.  Let `X` contain those present at even
vertices and `Y` those present at odd vertices.  Propagating the four label
memberships around (1.2) gives (1.4).  The size equations at `V_0` and `V_1`
give `|X|=m-1` and `|Y|=m-2`.  Direct unions in (1.4) prove the converse.
QED

An important consequence is that the local label type seen in the finite
certificate is forced by odd-graph geometry; it is not a special discovery
of the search.

### Corollary 1.1 (directed-four-cycle reversal)

Put `A={a,b,c,d}`.  For a directed four-cycle `sigma` on `A`, define the
four-edge matching

\[
 M_\sigma=
 \left\{
 \left\{
 X\cup\{u\},
 Y\cup\bigl(A\setminus\{u,\sigma(u)\}\bigr)
 \right\}:u\in A
 \right\}.
 \tag{1.6}
\]

The omitted label of the edge indexed by `u` is `sigma(u)`.  Every simple
eight-cycle in `O_m` is, uniquely up to reversing `sigma`,

\[
 \boxed{M_\sigma\mathbin\triangle M_{\sigma^{-1}}.}
 \tag{1.7}
\]

Thus an alternating-eight switch is exactly the reversal of a directed
four-cycle on four omitted labels, with the two inactive cores held fixed.
There are three such undirected trades for every partition (1.3).  In
particular, the total number of unrooted simple eight-cycles in `O_m` is

\[
 \boxed{
 3\binom{2m+1}{4}\binom{2m-3}{m-1}.
 }
 \tag{1.8}
\]

To verify (1.6), note that its two endpoint sets are disjoint and their union
omits exactly `sigma(u)`.  A directed four-cycle and its inverse give two
disjoint perfect matchings whose union is connected.  Conversely, Theorem 1
recovers `A`, the unequal-size contexts `X,Y`, and the inverse pair of
directed cycles.  This also proves the count (1.8).

Both matchings in (1.7) contain exactly one edge of each label in `A`.
Therefore every alternating-eight switch preserves the global multiset of
omitted edge labels, not merely the middle-vertex set.  What changes is the
distribution of those labels among the reconnected components.

## 2. Exact local context suspension

### Theorem 2 (parity-context suspension)

Let `a<=m`.  Every simple eight-cycle in `O_a` lifts to a simple
eight-cycle in `O_m`, preserving the alternating designation of any four
opposite edges as old factor edges.

More explicitly, write its normal form using contexts `X_0,Y_0`, where

\[
 |X_0|=a-1,\qquad |Y_0|=a-2.
\]

Take disjoint new sets `C,D`, each of size `m-a`, and replace

\[
 X_0\longmapsto X_0\cup C,
 \qquad
 Y_0\longmapsto Y_0\cup D
 \tag{2.1}
\]

in (1.4).  The result is the required lifted cycle.

### Proof

Every lifted vertex has size `m`.  Consecutive vertices use opposite
contexts, so their added parts are disjoint.  Their base parts already have
union equal to the old `(2a+1)`-set minus one of `a,b,c,d`.  The added parts
have union \(C\cup D\).  Hence the complement of every consecutive union in
the new `(2m+1)`-set is the same singleton edge label as before.  Simplicity
and the old/new alternation are preserved.  QED

For the certified `KG(9,4)` moves this simply adds `m-4` coordinates to each
of the two inactive parity contexts.  Thus every one of the 45 local edge
trades exists, in isolation, in every `O_m` for `m>=4`.

## 3. Exact obstruction to suspending balanced components

The local theorem does not suspend the factor components which carry the
eight switch vertices.

### Proposition 3 (fixed-context component obstruction)

Let `a<m`.  Let

\[
 C=(V_0,V_1,\ldots,V_{ell-1},V_0)
\]

be a Kneser cycle in `O_a`.  Add a context universe `Z` of size `2(m-a)` and
try to lift each vertex to

\[
 \widehat V_i=V_i\cup Q_i,
 \qquad Q_i\subseteq Z,\quad |Q_i|=m-a,
 \tag{3.1}
\]

while retaining all cycle edges.  Then:

1. `Q_{i+1}=Z\setminus Q_i` on every edge;
2. if `ell` is odd, the lifted cycle cannot close; and
3. if `ell` is even, the lifted cycle is never point-regular in `O_m`.

### Proof

Adjacent base vertices are disjoint.  Their two context sets have equal size
`m-a` inside a universe of size `2(m-a)`.  Lifted adjacency forces them to be
disjoint, hence complementary.  This proves (1), and alternation proves (2).

When `ell` is even, every coordinate of `Q_0` occurs in exactly `ell/2`
lifted vertices.  Point regularity in `O_m` would instead require every
coordinate to occur

\[
 \frac{m\,ell}{2m+1}
\]

times.  The equality `ell/2=m ell/(2m+1)` is impossible for `ell>0`.
This proves (3).  QED

So the parity-context lift is an exact local-trade lift and an exact global
balance obstruction at the same time.  In particular the 126-vertex
`KG(9,4)` route cannot be promoted to larger odd graphs by attaching fixed
contexts to its vertices.

There is also a dimension-free divisibility obstruction.  In `O_m`, a
point-regular family of `ell` middle sets has each point in
`m ell/(2m+1)` sets.  Since `gcd(m,2m+1)=1`,

\[
 \boxed{2m+1\mid ell.}
 \tag{3.2}
\]

Thus a target-dimensional centered segment must itself have length divisible
by the target wreath length; a fixed 9-based segment cannot remain centered
as `m` grows.

## 4. Scalable centered-segment routing

For a path segment `P` of middle sets in `O_m`, use the integral centered
vector

\[
 \zeta_m(P)
 =(2m+1)\sum_{A\in P}{\bf1}_A
 -m|P|{\bf1}.
 \tag{4.1}
\]

It vanishes exactly when `P` is point-regular.  Additivity gives the exact
switch criterion.

### Lemma 4 (four-segment routing)

Delete the four factor edges of an alternating eight-cycle from a
componentwise point-regular 2-factor.  Let `P_1,...,P_4` be the resulting
path segments.  A new component formed from the segment index set `J` is
point-regular if and only if

\[
 \boxed{\sum_{j\in J}\zeta_m(P_j)=0.}
 \tag{4.2}
\]

In particular, if every `zeta_m(P_j)=0`, then every reconnection produced by
the alternating-eight toggle is componentwise point-regular.

The union of the touched old components is point-regular, so

\[
 \sum_{j=1}^4\zeta_m(P_j)=0.
 \tag{4.3}
\]

Consequently exactly three of the four segment vectors can never vanish.

### Proof

The new edges change no vertex incidence.  Incidence and length of a new
component are the sums over its constituent segments, and (4.2) follows
from (4.1).  Equation (4.3) follows by summing the zero centered vectors of
the touched old components.  QED

The centered condition has a useful exact translation into omitted-edge
labels.

### Lemma 4.1 (endpoint-corrected label census)

Let

\[
 P=(A_0,A_1,\ldots,A_{L-1})
\]

be a path in `O_m`.  Let `t_x(P)` be the number of its `L-1` internal edges
whose omitted label is `x`, and let

\[
 e_x={\bf1}_{x\in A_0}+{\bf1}_{x\in A_{L-1}}.
\]

Then, coordinatewise,

\[
 \boxed{
 2\,\iota_x(P)=L-1-t_x(P)+e_x.
 }
 \tag{4.4}
\]

In particular, if `L=r(2m+1)`, then `P` is centered if and only if

\[
 \boxed{t_x(P)=r-1+e_x\quad\text{for every }x.}
 \tag{4.5}
\]

If the two path endpoints are Kneser-adjacent with omitted label `y`, this
is equivalent to saying that, after adding the closing edge, every ground
coordinate occurs exactly `r` times as an edge label.

In particular, for any odd-graph cycle of length `L`, if `t_x` now counts
all cyclic edge labels, then

\[
 2\,\iota_x=L-t_x.
 \tag{4.6}
\]

Hence the cycle is point-regular if and only if `2m+1` divides `L` and every
edge label occurs exactly `L/(2m+1)` times.

### Proof

For one coordinate `x`, an internal edge contributes one to the sum of the
memberships of its two endpoints unless that edge is labeled `x`, in which
case it contributes zero.  Summing over the internal edges gives

\[
 \sum_{i=0}^{L-2}
 \left({\bf1}_{x\in A_i}+{\bf1}_{x\in A_{i+1}}\right)
 =L-1-t_x(P).
\]

The left side is `2 iota_x(P)-e_x`, proving (4.4).  Substitute
`L=r(2m+1)` and `iota_x(P)=rm` to get (4.5).  For a closing Kneser edge,
`e_x=1` except at its omitted label `y`, where `e_y=0`; the last assertion
follows.  QED

Thus a target-dimensional zero-centered arc is exactly an almost-uniform
block of the omitted-label word, with the two endpoint corrections shown in
(4.5).  This turns the open zero-arc supply problem into a concrete
discrepancy problem on edge labels.

PBBS homomesy alone does not provide such arcs.  In the initial `O_4`
factor, the level-three orbit

```text
1246 3578 1469 2357 4689 1257 3468 1579 2368
4579 1268 3479 1568 2379 1458 2679 1348 2569
1378 2459 1367 2489 1356 2478 1359 2467 3589
```

has no centered cyclic arc of length nine.  The other level-three orbit has
nine centered length-nine arcs, but none has Kneser-adjacent endpoints.  By
contrast, the level-five orbit has nine centered and closable length-nine
arcs.  These statements are exhaustively checked by the analysis script.
Thus even on the critical diagonal, orbitwise point regularity gives neither
a balanced minimum arc nor its closability uniformly.

### Corollary 5 (balanced four-way merger)

Suppose the four old edges in the normal form (1.4) lie in four distinct
point-regular factor components.  Toggling the eight-cycle merges those four
components into one point-regular component.

Indeed, cutting one edge from each component produces four whole-component
paths, hence four zero-centered segments.  The four new edges join them in
one cyclic order.

This is a genuinely all-dimensional merge primitive.  Its unresolved input
is a supply theorem: one must find normal-form connector edges in the desired
four components.  The inverse split is balanced when the four arcs cut from
one component are individually centered.  By (3.2), those arcs necessarily
have lengths divisible by `2m+1`.

## 5. Exact anatomy of the 45-switch certificate

The analysis script

```text
python3 scratch/analyze_pbbs_odd9_switch_motifs.py
```

parses `PBBS_BALANCED_SWITCH_9_4_CERTIFICATE.txt`, cuts each pre-switch
factor at the four removed edges, computes all four vectors (4.1), recovers
the post-switch segment grouping, checks (4.2), verifies the local normal
form, and audits the parity-context suspension in `O_5` and `O_6`.

All 45 moves have the single dihedral label type

\[
 (0,1,2,0,3,2,1,3),
 \tag{5.1}
\]

which is (1.2).  The number of individually zero-centered segments is

\[
\begin{array}{c|rrrr}
\#\{j:\zeta_4(P_j)=0\}&0&1&2&4\\ \hline
\text{number of moves}&14&15&13&3.
\end{array}
\tag{5.2}
\]

Here a cut partition such as `(1,1,2)` records the numbers of removed edges
in the touched old components, and a new grouping such as `(1,3)` records
the numbers of cut segments in the new components.  The full routing census
is

\[
\begin{array}{c|c|c|r}
\text{old cut partition}&\text{new grouping}&\text{zero segments}&\text{count}\\ \hline
(1,1,2)&(1,3)&4&2\\
(1,1,2)&(4)&2&1\\
(1,3)&(1,3)&2&6\\
(1,3)&(4)&1&7\\
(1,3)&(4)&2&1\\
(4)&(1,1,1,1)&4&1\\
(4)&(1,1,2)&2&4\\
(4)&(1,3)&1&8\\
(4)&(1,3)&2&1\\
(4)&(4)&0&14.
\end{array}
\tag{5.3}
\]

This reproduces the independently known decomposition into 11 merges, 20
component-preserving reorderings, and 14 splits.

Only steps 28, 32, and 37 are fully zero-centered.  Their segment data are

\[
\begin{array}{c|c|c|c}
\text{step}&\text{lengths}&\text{old cuts}&\text{new grouping}\\ \hline
28&(9,9,9,63)&(1,1,2)&(1,3)\\
32&(9,9,9,63)&(1,1,2)&(1,3)\\
37&(9,9,9,45)&(4)&(1,1,1,1).
\end{array}
\tag{5.4}
\]

All lengths in (5.4) are multiples of nine, as forced by (3.2).  Step 37
is a four-way balanced split; its reverse is the scalable four-way merger of
Corollary 5.  Steps 28 and 32 are catalyst moves: two whole balanced
components and two balanced arcs of a long component are rerouted into one
singleton segment component and one three-segment component.

When segment-length multiset, zero count, and new grouping are retained,
the 45 moves occupy 43 distinct structural types.  More importantly, 42
moves use nonzero vector cancellations.  The route is therefore not a
repetition of a bounded, independently balanced local patch.  Its success
depends on the evolving long-component arc geometry.

The connector supports are nearly as diverse.  A support is the recovered
triple `(A,X,Y)` in (1.3).  The 45 moves use 43 distinct supports: 41 occur
once and two occur twice.  Thus the route is not repeatedly flipping the
three orientations of one small collection of fixed core cells; it keeps
moving the local connector through the coordinate geometry.

## 6. Consequence for the asymptotic program

The finite certificate proves that odd-graph merge--reorder--split is
possible and identifies a universal local connector.  The context theorem
shows that connector availability is compatible with every dimension.  But
Proposition 3 rules out the simplest induction in which one merely appends
two fixed context blocks and replays the 45 switches.

An all-dimensional theorem must instead do one of the following inside the
target graph itself:

1. find many four-way connectors between point-regular components, then
   create target-dimensional zero-centered arcs of lengths divisible by
   `2m+1`; or
2. route nonzero segment vectors so that the exact group sums (4.2) vanish.

This is a sharper target than an unspecified switching theorem.  It
separates the fully solved local edge geometry from the still-open nonlocal
centered-arc supply problem.

## 7. Reproducibility and status

The original certificate is preserved unchanged:

* `PBBS_BALANCED_SWITCH_9_4_CERTIFICATE.txt`;
* `scratch/verify_pbbs_odd9_balanced_switch_certificate.py`.

The new analysis is read-only with respect to the certificate:

* `scratch/analyze_pbbs_odd9_switch_motifs.py`.

### Proved

1. The universal four-label normal form (1.2)--(1.4).
2. The all-dimensional local parity-context suspension theorem.
3. The fixed-context obstruction for whole balanced components.
4. The exact centered-segment routing and four-way merger lemmas.
5. The complete segment/vector census (5.2)--(5.4) of the certified route.

### Still open

1. An asymptotic supply of normal-form connectors between prescribed
   balanced components.
2. A target-dimensional supply of zero-centered arcs, or an alternative
   theorem routing nonzero centered vectors.
3. A balanced all-dimensional conversion from the PBBS factor to a wreath
   factor.

Accordingly this note does not prove the Wreath Conjecture or improve the
global OR coefficient by itself.
