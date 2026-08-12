# PBBS self-owned rebundling: exact path sewing, centered-cost bounds, and the odd-hexagon obstruction

Date: 2026-07-26

Input: the audited PBBS `q=1` theorem.  This note does not reprove any PBBS
shadow statement.

## 0. Verdict

Let

\[
 n=2m+1,qquad
 W=\binom nm,qquad
 B=\frac Wn=\operatorname {Cat}_m,                           \tag{0.1}
\]

and let `F=F_{PBBS}` be the canonical PBBS spanning `2`-factor of
`KG(n,m)`.  Every component of `F` is point-regular and has length
`\ell n`.

The desired statement is an exact `C_n`-factor `G` satisfying

\[
                         |E(F)\setminus E(G)|=O(B).           \tag{0.2}
\]

This would preserve all but `O(B)=O(W/m)` centered Johnson edges and lower
colour occurrences.  The union colours remain perfect for every Kneser
factor, independently of the rebundling.

The present attack proves the following.

1. **Exact sewing theorem.**  Condition (0.2) is equivalent to cutting
   `O(B)` PBBS edges and packetizing the residual PBBS paths into
   `n`-vertex endpoint-compatible Kneser cycles.  Every such packet is
   automatically a wreath.  The changed centered owners are exactly the
   vertices incident with the cut edges.
2. **Sharp cost window.**  If `b_1(F)` is the number of PBBS components
   already of length `n`, then every exact wreath factor `G` obeys

   \[
       B-b_1(F)le |E(F)\setminus E(G)|le d_{\rm cent}le
       2|E(F)\setminus E(G)|,                                \tag{0.3}
   \]

   where `d_cent` is the number of changed centered edges, equivalently
   changed centered lower-colour occurrences.  Thus Catalan-scale sewing is
   best possible in order whenever `b_1(F)=o(B)`; that last asymptotic for
   PBBS is not proved here.
3. **Odd-graph hexagon classification.**  Every simple `C_6` in
   `KG(2m+1,m)` is `K_{3,3}` minus one perfect matching.  Its alternating
   switch replaces one of the remaining perfect matchings by the other.
4. **Exact balance gate.**  A hexagon using one old edge from each of three
   point-regular components is an automatically balanced pure merge.  A
   hexagon which splits one component into two or three point-regular
   components must isolate a residual cyclic path of zero centered
   signature.
5. **Physical obstruction.**  A signature-primitive long PBBS component
   cannot be split directly by any alternating hexagon.  The canonical
   `KG(9,4)` PBBS factor contains an explicit signature-primitive
   `27`-cycle, given in Section 6.  Therefore a direct local hexagon-peeling
   theorem is false even in the first defective odd-graph dimension.

There is consequently no unconditional proof of (0.2) in this note.  The
exact surviving gate is the endpoint-compatible path packetization of
Section 2, or equivalently an `O(B)` merge--reorder--split route satisfying
the signature equations at every split.  General zero-owner-signature
hexagons from the even-ground auxiliary matching problem do not close this
gate: they live in a different Kneser graph and do not preserve the physical
centered PBBS edges when transplanted.

## 1. Centered-edge preservation is exactly vertex support

For any spanning Kneser `2`-factor `H` and center `X`, let

\[
 e_X(H)=\{Y_H(X),Z_H(X)\}                                    \tag{1.1}
\]

be the Johnson edge joining the two `H`-neighbours of `X`.  Its colours are

\[
 e_X(H)^\cup=X^c,
 \qquad
 e_X(H)^\cap=Y_H(X)\cap Z_H(X).                              \tag{1.2}
\]

Let `F,G` be spanning Kneser `2`-factors and put

\[
 R=E(F)\setminus E(G),qquad t=|R|.                          \tag{1.3}
\]

Since both factors are `2`-regular,

\[
                         |E(G)\setminus E(F)|=t.             \tag{1.4}
\]

### Proposition 1.1 (center support identity)

The set of centers whose Johnson edge changes is exactly

\[
                 D(F,G)=\{X:X\text{ is incident with an edge of }R\}. \tag{1.5}
\]

Consequently

\[
                              t\le |D(F,G)|\le2t.            \tag{1.6}
\]

At every center outside `D(F,G)`, both the centered edge and its lower
colour are retained.  At every center, including those in `D(F,G)`, the
union colour remains `X^c`.

#### Proof

If no removed edge is incident with `X`, both `F`-edges at `X` remain in
`G`.  Degree two then forces the same unordered neighbour pair.  Conversely,
an incident removed edge deletes one of the old neighbours, so the centered
edge changes.

The graph `(V,R)` has maximum degree two.  Every one of its nonempty path
or cycle components has at least as many vertices as edges, giving the
lower bound in (1.6); the upper bound is the endpoint count.

For fixed union `X^c`, a lower colour determines the Johnson edge uniquely:
if the lower colour is `S`, the endpoints are the two `m`-sets between
`S` and `X^c`.  Hence a changed centered edge is also a changed lower-colour
occurrence.  Formula (1.2) proves the union assertion. `\square`

Thus an `O(B)` Kneser-edge rebundling pays exactly the required
`O(W/m)` centered cost, with no hidden multiplication by `m`.

## 2. Exact path-packet sewing theorem

Cut a set `R\subseteq E(F)` of PBBS edges.  Every cut PBBS cycle becomes
as many vertex-disjoint paths as it has cut edges; an uncut component
remains a cycle.  Call the resulting paths **old intervals**.

A **wreath packet** consists of old intervals

\[
 P_1=(a_1,\ldots,b_1),\ldots,P_q=(a_q,\ldots,b_q)           \tag{2.1}
\]

with total `n` distinct vertices, together with orientations and a cyclic
ordering for which

\[
                              b_i\cap a_{i+1}=\varnothing    \tag{2.2}
\]

for every cyclic `i`.  The edges `b_i a_{i+1}` are its seams.  An uncut
PBBS `n`-cycle is allowed as a packet with no new seam.

### Theorem 2.1 (self-owned path sewing)

Let `F` be the PBBS factor.  The following are equivalent for an integer
`t`.

1. There is an exact `C_n`-factor `G` of `KG(n,m)` with

   \[
                              |E(F)\setminus E(G)|=t.        \tag{2.3}
   \]

2. There is a `t`-edge cut set `R\subseteq E(F)` such that all residual
   old intervals and all uncut PBBS `n`-cycles partition into wreath
   packets, using exactly `t` seams in total, and no seam belongs to `F`.

Under either condition, the final factor retains at least `W-2t` centered
edges and lower-colour occurrences, and retains the perfect union ledger
exactly.

#### Proof

Assume item 2.  Retain every uncut PBBS edge and add the packet seams.
Each packet is a simple Kneser cycle of length `n`.  Every `C_n` in
`KG(2m+1,m)` is a wreath: if `z_i` is the unique omitted label of its
`i`-th edge, cycle parity forces every coordinate to occur exactly once
among the `z_i`, and the recurrence

\[
                              A_{i+1}=A_i^c\setminus\{z_i\}  \tag{2.4}
\]

reconstructs the cyclic-window form.  The packets partition all vertices,
so they give an exact wreath factor `G`.  The number of removed and added
edges is `t`.

Conversely, let `G` satisfy item 1.  The common graph `F\cap G` has maximum
degree two and consists of paths together with components on which the two
factors agree completely.  Intersect each `G`-cycle with `F\cap G`.
This partitions that `G`-cycle into old intervals joined by edges of
`G\setminus F`; hence it is a wreath packet.  There are exactly `t` such
new seams by (1.4).  A common whole component must already have length `n`,
because it is a component of the exact factor `G`.  This is item 2.

The centered assertions follow from Proposition 1.1. `\square`

The theorem is a literal necessary-and-sufficient sewing interface.  Its
open content is not point regularity after the fact: endpoint compatibility
(2.2) and a global packing of the old intervals into `n`-vertex packets
must be achieved simultaneously.

## 3. The unavoidable Catalan-scale cost

Let `b_1(F)` be the number of PBBS components of length exactly `n`.

### Theorem 3.1 (edge and centered lower bounds)

For every exact wreath factor `G`,

\[
 \boxed{
 B-b_1(F)le |E(F)\setminus E(G)|le |D(F,G)|.
 }                                                           \tag{3.1}
\]

#### Proof

Put `t=|E(F)\setminus E(G)|`.  After the `t` old edges are removed, an
initial component cut `k>=1` times produces exactly `k` old intervals.  An
uncut initial component persists as a whole component after the new edges
are added, so it can be uncut only if it already has length `n`.  Therefore
the retained old graph has at most

\[
                              b_1(F)+t                       \tag{3.2}
\]

components.  Adding edges cannot increase component count.  The final
factor has exactly `B` components, so `B\le b_1(F)+t`.  Proposition 1.1
gives `t\le|D(F,G)|`. `\square`

Combining Theorems 2.1 and 3.1 gives the calibrated target

\[
 B-b_1(F)\le t=O(B).                                        \tag{3.3}
\]

An `o(B)` sewing is impossible if `b_1(F)=o(B)`.  No asymptotic estimate
of that strength for the PBBS short-orbit count is assumed here.  The
lower bound therefore calibrates the route but does not disprove (0.2).

## 4. Normal form of an odd-graph hexagon

The six-coordinate zero-signature hexagon in the even-ground auxiliary
matching problem is not itself a cycle in `KG(2m+1,m)`.  The physical
odd-graph hexagon has a different, three-residual-coordinate normal form.

### Theorem 4.1 (classification of `C_6` in the odd graph)

Every simple six-cycle in `KG(2m+1,m)`, for `m>=3`, has a unique
description, up to exchanging the two cores and permuting three labels,
as

\[
 K+a, L+b, K+c, L+a, K+b, L+c, K+a,                  \tag{4.1}
\]

where

\[
 [n]=K\mathbin{\dot\cup}L\mathbin{\dot\cup}\{a,b,c\},
 \qquad |K|=|L|=m-1.                                       \tag{4.2}
\]

Equivalently, its six vertices induce `K_{3,3}` minus the three forbidden
same-label edges `(K+x)(L+x)`.

#### Proof

Let the cyclic vertices be `A_0,...,A_5`, and label each edge by its unique
omitted coordinate

\[
                              g_i=[n]\setminus(A_i\cup A_{i+1}). \tag{4.3}
\]

For a coordinate `x`, membership toggles on every edge not labelled `x`
and stays zero on an `x`-edge.  Closure of a six-cycle implies that the
number of `x` labels is even.  Equal adjacent labels would give
`A_i=A_{i+2}`, contradicting simplicity.  A label can therefore occur at
most three times, and its positive multiplicity is exactly two.  Since
there are six edges, precisely three labels `a,b,c` occur twice.

Every other coordinate toggles on all six edges and hence belongs either
to all even vertices or to all odd vertices.  Call these two disjoint cores
`K,L`.  Successive occurrences of one gap label have odd cyclic distance;
with two occurrences and no adjacency their distance is three.  The label
therefore belongs to exactly one even and one odd vertex.  Each parity
class consists of `K`, respectively `L`, plus the three residual labels
one at a time.  Disjointness forbids equal labels across a cycle edge,
giving exactly (4.1). `\square`

The two alternating perfect matchings of (4.1) are

\[
\begin{aligned}
 M^-&=\{(K+a,L+b),(K+b,L+c),(K+c,L+a)\},\\
 M^+&=\{(K+a,L+c),(K+c,L+b),(K+b,L+a)\}.
\end{aligned}                                                \tag{4.4}
\]

An `F`-alternating hexagon switch replaces `M^-` by `M^+`, or conversely.
It changes three Kneser edges and at most six centered lower-colour
occurrences.  Unlike the auxiliary even-ground hexagon, it does not have
zero physical centered signature automatically.

## 5. Exact signature criterion for a hexagon switch

For an ordered path or vertex family `P`, define its integral centered
signature

\[
 \zeta(P)=n\sum_{A\in P}{\bf1}_A-m|P|\mathbf1\in\mathbb Z^n. \tag{5.1}
\]

It is additive, and a cycle or packet is point-regular exactly when its
signature is zero.

Delete the three old edges of an alternating hexagon from a factor `F`
whose components are point-regular.  Exactly three residual paths
`P_1,P_2,P_3` result, counted with multiplicity across the old components.
Let `r` and `s` be the numbers of touched old and new components.

### Theorem 5.1 (lossless hexagon balance table)

The old/new path-incidence bipartite multigraph is connected and has three
edges, so

\[
                              r+s\le4.                        \tag{5.2}
\]

Every new component is point-regular if and only if the signatures of its
constituent residual paths sum to zero.  In particular:

1. `r=3,s=1`: the switch is a pure three-component merge and is balanced
   automatically;
2. `r=1,s=2`: the switch is balanced exactly when the singleton residual
   path on one side of the new partition has signature zero;
3. `r=1,s=3`: the switch is balanced exactly when all three residual paths
   have signature zero; and
4. `r=1,s=1`: component-preserving reordering is balanced automatically.

For `r=2`, a one-output merge is automatic, while a two-output exchange is
balanced precisely when either one new path block, equivalently both, has
zero total signature.

#### Proof

Assign each residual path to its old and new component.  Traversing the
connected alternating hexagon gives a connected walk through the line graph
of the incidence multigraph, proving connectedness and (5.2).

New edges carry no vertices.  Thus a new component made from a path block
`J` has signature `\sum_{j\in J}\zeta(P_j)`.  This proves the criterion.
The old point-regular components give the corresponding old-block sums zero,
and the sum of all three path signatures is zero.  The listed cases now
follow by enumerating partitions of three paths. `\square`

### Corollary 5.2 (signature-primitive obstruction)

Call a point-regular cycle **signature-primitive** when it has no nonempty
proper contiguous cyclic path `P` with `\zeta(P)=0`.  No balanced
alternating hexagon supported entirely on a signature-primitive component
can increase the number of components.

#### Proof

A component-increasing switch has `r=1` and `s=2` or `3`.  Theorem 5.1
then forces at least one of the three residual contiguous paths to have
zero signature, contrary to primitivity. `\square`

More quantitatively, if the initial PBBS factor contains `p` long
signature-primitive components, then in any componentwise-point-regular
hexagon-only route to wreaths, the first switch touching each such component
cannot be a direct self-split.  Since one hexagon touches at most three
initial components, at least `\lceil p/3\rceil` preparatory merge, exchange,
or component-preserving events are necessary.  This is a route-specific
lower bound, not a prohibition on `O(B)` global sewing.

## 6. A literal primitive PBBS component in `KG(9,4)`

The following is one canonical PBBS orbit, written cyclically:

\[
\begin{split}
&1246,3578,1469,2357,4689,1257,3468,1579,2368,\\
&4579,1268,3479,1568,2379,1458,2679,1348,2569,\\
&1378,2459,1367,2489,1356,2478,1359,2467,3589.
\end{split}                                                   \tag{6.1}
\]

Its omitted-label word is

\[
 9,2,8,1,3,9,2,4,1,3,5,2,4,6,3,5,7,4,6,8,5,7,9,6,8,1,7.   \tag{6.2}
\]

Equation

\[
                              A_{i+1}=A_i^c\setminus\{g_i\} \tag{6.3}
\]

verifies every Kneser edge; direct cyclic `10` matching verifies that
`g_i` is the PBBS unmatched zero at `A_i`.  Each coordinate occurs twelve
times in (6.1), so the `27`-cycle is point-regular.

If a path in this cycle has zero signature, its length is divisible by
`9`, because `\gcd(9,4)=1`.  It is therefore enough to test the `27`
cyclic intervals of length nine; an interval of length eighteen is centered
exactly when its complementary length-nine interval is centered.

For the length-nine intervals starting at positions `0,...,26`, the
coordinates occurring above and below their required degree four are,
respectively,

\[
\begin{split}
&(6/9),(57/12),(6/3),(7/1),(68/23),(7/4),(8/2),(79/34),(8/5),\\
&(9/3),(18/45),(9/6),(1/4),(29/56),(1/7),(2/5),(13/67),(2/8),\\
&(3/6),(24/78),(3/9),(4/7),(35/89),(4/1),(5/8),(46/19),(5/2).
\end{split}                                                   \tag{6.4}
\]

For example `(57/12)` means that coordinates `5,7` have degree five and
coordinates `1,2` have degree three; all unlisted coordinates have degree
four.  Every entry in (6.4) is nonempty on both sides.  Hence the PBBS
cycle (6.1) is signature-primitive.

### Corollary 6.1

The component (6.1) cannot be split directly into smaller point-regular
components by any alternating Kneser hexagon.

This is a physical PBBS counterexample to a universal direct-hexagon peel.
It does not obstruct a merge--reorder--split route: the existing finite
`KG(9,4)` certificate succeeds precisely by temporarily mixing and
reordering components before the final splits.

## 7. A conditional `O(B)` hexagon sewing theorem

The preceding obstruction identifies the extra input needed by a positive
route.

### Theorem 7.1 (certificate-to-sewing implication)

Suppose there is a sequence of `h` factor-alternating odd-graph hexagons
starting at `F_{PBBS}` such that:

1. after every switch, every factor component is point-regular;
2. the final factor has exactly `B` components; and
3. `h\le C B` for an absolute constant `C`.

Then the final factor is an exact wreath factor and differs from PBBS at
at most `3CB` Kneser edges and at most `6CB` centered lower-colour
occurrences.

#### Proof

Every hexagon toggles three old and three new factor edges, so the final
edge distance from PBBS is at most `3h`.  Proposition 1.1 gives centered
distance at most `6h`.

Point regularity forces every nonempty component length to be divisible by
`n`, since `\gcd(n,m)=1`.  The final `B` positive multiples of `n` sum to
`W=Bn`, so every component has length exactly `n`.  Every odd-graph
`C_n` is a wreath by the omitted-label reconstruction used in Theorem 2.1.
`\square`

The theorem also holds with general bounded alternating cycles, replacing
the constants `3,6` by the numbers of removed edges and touched endpoints.
Its unresolved hypothesis is availability: pure-merge hexagons are
automatically balanced, but signature-primitive components require
nonmonotone merging or reordering before any hexagonal split.

## 8. Quantitative obstruction for bounded-switch routes

Let a route use alternating cycles which remove at most `q` current factor
edges per step.  Deleting those edges produces at most `q` residual paths,
so one switch can increase component count by at most `q-1`.  Starting with
`c(F)` PBBS components and ending with `B` wreaths therefore requires

\[
                              h\ge\frac{B-c(F)}{q-1}.         \tag{8.1}
\]

For hexagons, `q=3`:

\[
                              h\ge\frac{B-c(F)}2.            \tag{8.2}
\]

Together with Theorem 3.1, this shows that any bounded-local-template route
must be applied at Catalan scale whenever PBBS has `B-o(B)` component
excess.  It does not rule out the requested `O(B)` construction; it rules
out a sparse `o(B)` absorber and explains why isolated zero-signature
hexagons are insufficient.

## 9. Exact remaining theorem

The audited `q=1` shadow is not the bottleneck.  The exact missing statement
is one of the following equivalent positive forms.

1. **Static path packets:** find the packetization of Theorem 2.1 with
   `t=O(B)`.
2. **Dynamic switches:** find an `O(B)` sequence of balanced alternating
   Kneser switches ending with `B` point-regular components.

The odd-hexagon normal form proves that zero-signature split directions
exist, and pure three-component merges need no signature condition.  The
primitive PBBS component (6.1) proves that direct self-peeling is false.
What remains is a quantitative availability/routing theorem showing that
merges and component-preserving reorderings create enough zero-signature
cuts before more than `O(B)` edges have been changed.

No theorem currently supplies that availability.  Consequently an exact
self-owned rebundling at `O(W/m)` cost remains open, but its topology,
balance equations, optimal scale, and the failure of the direct-hexagon
strategy are now exact.
