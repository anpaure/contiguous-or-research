# Integral resolution of quartet faces, and the cycle-window gap

## 0. Verdict

At the level of abstract cube faces, the integral resolution problem has an
exact positive answer which is much stronger than a catalog theorem:

> **Every deterministic quartet wreath partition covers every lower and
> upper Boolean target as a face of one of its cells.**

Therefore, given any nonempty catalog--in particular a catalog of
`R=Theta(m2^H)` members--choose one complete member.  Assign each middle
vertex to its unique cell in that member.  The cells remain disjoint, cover
the middle layer exactly, and have zero lower or upper **face** deficit at
every depth `q<=m`.  No per-source mixing and no sector repair are needed.

This does not solve the OR problem.  A cell of dimension `d` has

\[
 \binom dq2^{d-q}                                    \tag{0.1}
\]

lower `q`-faces, but a cyclic ordering of its `2^d` vertices has only
`2^d` starting windows.  It can expose at most the fraction

\[
 {2^q\over\binom dq}                                \tag{0.2}
\]

of those faces as consecutive geodesic windows.  At `d=Theta(m)` and
`q=Theta(sqrt(m))`, this fraction is
`exp(-Theta(sqrt(m) log m))`.

The catalog incidence theorem is therefore an availability theorem for
faces, not an integral routing theorem for windows.  The actual unresolved
step is to choose whole cells, cycles, and direction orders so that the
small trace (0.2) is globally injective on almost all targets.

## 1. Local face extension is frame-independent

Let a quartet `Q` carry any one of its three perfect matchings `P`.  The
rank-`t` matching resolution partitions the local `t`-subsets into physical
pair-flip cubes.

### Lemma 1 (lower local extension)

Let `S subset Q` have rank `s`.  If

\[
 s\le t\le2,                                        \tag{1.1}
\]

then `S` is the intersection of a `(t-s)`-face in the rank-`t` resolution,
for every choice of `P`.

### Proof

At most `s` of the two matching edges meet `S`, so at least `2-s` matching
edges are empty.  Choose `t-s` of those empty edges, change them to split
edges by selecting one endpoint, and call the resulting rank-`t` vertex
`X`.  In the cell containing `X`, vary precisely those new free edges and
fix every other free edge at its `S` endpoint.  The intersection of that
face is `S`.  QED.

### Lemma 2 (upper local extension)

Let `T subset Q` have rank `s`.  If

\[
 2\le t\le s,                                        \tag{1.2}
\]

then `T` is the union of an `(s-t)`-face in the rank-`t` resolution, for
every choice of `P`.

### Proof

A rank-`s` subset of a quartet contains at least `s-2` complete matching
edges.  Choose `s-t` of them, change each from full to split by deleting one
endpoint, and vary those directions in the cell of the resulting
rank-`t` vertex.  Their face union restores `T`.  QED.

For the leftover pair in odd `m`, the identical statements hold with
central local rank one in place of two.

## 2. Every wreath partition resolves every target

Partition `[2m]` into quartets `Q_1,...,Q_g`, with a leftover pair when
`m` is odd.  Write

\[
 b_j=2\quad(Q_j\text{ a quartet}),
 \qquad b_0=1\quad(\text{leftover pair}),            \tag{2.1}
\]

so that `sum b_j=m`.

A deterministic wreath frame function may choose a different local
matching in every block for every admissible middle rank vector `t`.  No
compatibility between different sectors is assumed.

### Theorem 3 (exact integral face resolver)

For every such frame function and every `0<=q<=m`:

1. every set `S` of rank `m-q` is the intersection of a physical `q`-face
   in one cell of the wreath partition; and
2. every set `T` of rank `m+q` is the union of a physical `q`-face in one
   cell of the wreath partition.

### Proof: lower side

Put `s_j=|S intersection Q_j|`, including the leftover block if present.
Then

\[
 \sum_j(b_j-s_j)=q.                                 \tag{2.2}
\]

The sum of the positive terms in (2.2) is at least `q`.  Choose integers

\[
 0\le r_j\le(b_j-s_j)_+,
 \qquad\sum_jr_j=q,                                 \tag{2.3}
\]

and set `t_j=s_j+r_j`.  This is an admissible middle rank vector because
`sum t_j=m`.

Now inspect the frame chosen by the wreath function in this very sector
`t`.  Whenever `r_j>0`, we have `s_j<=t_j<=b_j`; Lemma 1, or its leftover
pair version, supplies a local `r_j`-face with intersection
`S intersection Q_j`.  When `r_j=0`, use the local vertex itself.  The
Cartesian product is a physical `q`-face in a cell of sector `t`, and its
intersection is `S`.

Crucially, `t` was selected before looking at the frame.  Lemma 1 works for
all three frames, so there is no circular fixed-point requirement.

### Proof: upper side

For `s_j=|T intersection Q_j|`,

\[
 \sum_j(s_j-b_j)=q.                                 \tag{2.4}
\]

Choose

\[
 0\le r_j\le(s_j-b_j)_+,
 \qquad\sum_jr_j=q,                                 \tag{2.5}
\]

and put `t_j=s_j-r_j`.  Then `sum t_j=m`, and every changed block satisfies
`b_j<=t_j<=s_j`.  Lemma 2 in the frame assigned to sector `t` gives local
faces whose product has union `T`.  QED.

### Corollary 4 (catalog integration is trivial for faces)

Let `Pi_1,...,Pi_R` be any nonempty catalog of complete quartet wreath
partitions.  Choose one index `a` and assign every middle source `X` to its
unique cell in `Pi_a`.  Then:

* the selected cells are pairwise disjoint;
* they cover every middle vertex exactly once; and
* every lower and upper target at every depth is a face of a selected cell.

Thus the abstract face deficit is exactly zero, not merely `o(W)`.  The
hypothesis that the catalog covers every **nested source--target pair** is
strictly stronger than needed for targetwise face coverage.

The same conclusion holds after arbitrary sector switching: choose any
available frame vector independently in each disjoint rank-vector sector.
The result is another wreath partition, and Theorem 3 applies unchanged.

## 3. Face multiplicity versus window capacity

Consider one physical `d`-cube cell.  A lower `q`-face is determined by:

* the `q` free directions whose two endpoints disappear from the
  intersection; and
* one fixed orientation on each of the other `d-q` directions.

Hence the number of distinct lower targets internal to the cell is exactly

\[
 F_q(d)=\binom dq2^{d-q}.                            \tag{3.1}
\]

The upper count is identical.

Now give the `2^d` cell vertices a cycle factor whose transitions are cube
edges.  At depth `q` there are only `2^d` cyclic starting positions in
total.  Any length-`q` transition window
whose intersection loses exactly `q` coordinates must use `q` distinct
directions without restoring a deleted coordinate; it is a geodesic
window.  Such a window exposes at most one lower face and one upper face.

### Proposition 5 (local trace bound)

Any cyclic cell order exposes at most `2^d` distinct lower depth-`q`
targets and at most `2^d` distinct upper targets.  Relative to all physical
faces, its coverage fraction is at most

\[
 \min\left(1,{2^q\over\binom dq}\right).            \tag{3.2}
\]

For `q<=d/2`,

\[
 {2^q\over\binom dq}\le\left({2q\over d}\right)^q. \tag{3.3}
\]

This is a capacity comparison, not by itself a global omission theorem:
one target can occur as a face in many different cells.

## 4. A sharp separation already exists

Take a constant wreath frame.  It is the ordinary partition associated
with one global coordinate matching.  Theorem 3 says it has **zero**
abstract face deficit on both sides at every depth.

Nevertheless the fixed-pair type argument recorded in
`PIVOT_SHADOW_CAPACITY.md`, specialized to zero nonnative pivots, proves
that any sufficiently long geodesic factor confined to this fixed matching
system misses

\[
 \Omega(W)                                           \tag{4.1}
\]

lower targets and `Omega(W)` upper targets at one depth
`q=floor(c sqrt(m))`, regardless of its direction orders.

Therefore

\[
 \text{complete integral face resolution}
 \quad\not\Longrightarrow\quad
 \text{consecutive-window shadow coverage}.         \tag{4.2}
\]

This is not merely a missing proof technique: the implication is false for
an explicit subfamily of wreath partitions.

Sector-dependent frames evade the hypotheses of that fixed-type capacity
theorem, so (4.1) cannot be transferred to every wreath partition.  The
window problem for genuinely diffused sector frames remains open.

## 5. Why pairwise catalog coverage does not select cells

Suppose two partitions `Pcal,Qcal` of the middle layer are offered and one
tries to choose whole cells from both while retaining an exact partition.
Form their bipartite overlap graph.  If `x_C,y_D` indicate whether cells
`C in Pcal`, `D in Qcal` are selected, every nonempty overlap imposes

\[
 x_C+y_D=1.                                         \tag{5.1}
\]

Along a connected component, all `Pcal` variables are equal and all
`Qcal` variables are their complement.  Thus each overlap component must
choose one complete side.  An assignment made independently for every
source is not legitimate.

With three or more systems the selection problem becomes a genuine exact
cover/absorber problem; pairwise nested-face coverage supplies no theorem
solving it.  Wreath sector switching is legal only because the sectors are
already disjoint components.  Even after a legal cell selection, one must
still solve the much stronger cycle trace problem of Section 3.

## 6. Correct remaining target

The `Theta(m2^H)` catalog from the joint-incidence theorem is unnecessary
for abstract targetwise faces and insufficient by itself for consecutive
windows.  Its useful role is only as a reservoir of alternative local
traces.

A positive theorem now needs to select, simultaneously:

1. one exact middle-cell resolution, possibly by multi-system absorbers;
2. a cycle/path factor inside every retained cell;
3. one consecutive depth-`q` window for almost every lower and upper target
   through `H`; and
4. cross-cell injectivity with only `o(W)` seams and repairs.

The face resolver proved here discharges none of items 2--4.  It does show
that future work should stop treating raw face existence as the missing
resource: the resource is already complete.  The bottleneck is integral
ordered routing through an exponentially sparse trace of those faces.
