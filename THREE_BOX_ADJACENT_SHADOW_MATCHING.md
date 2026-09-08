# The adjacent-shadow graph is frozen

## 1. Outcome

Put

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                  |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1.
\]

The layers immediately below and above it are

\[
 L_a=\{w\in[-a,a]^3:\sum w_i=-1\},\qquad
 U_a=\{u\in[-a,a]^3:\sum u_i=1\}.
\]

Both have size `M_a-1`.  A Johnson edge in `H_a` has one meet in
`L_a` and one join in `U_a`.  It is therefore natural to ask for `M_a-1`
middle edges whose meets and joins are both rainbow.

There is no freedom in that first shadow layer.

> **Frozen adjacent-shadow theorem.**  The bipartite graph which pairs a
> lower color with an upper color when they are the meet and join of one
> middle Johnson edge has a unique perfect matching.  Its corresponding
> middle edges are exactly
> \[
>                         R_1\sqcup R_2\sqcup\cdots\sqcup R_a,
> \]
> the disjoint concentric hexagonal ring cycles.

Thus every exactly two-sided-rainbow collection of `M_a-1` middle edges is
the concentric collection.  In particular, changing the middle Hamilton
path while retaining exactly one occurrence of every lower and upper edge
color is not a live degree of freedom.

The theorem also gives an exact linearization ledger.  If the forced ring
cycles occur as `b_s` maximal forced-edge trail blocks on radius `s` in the
final row, then a middle row containing those rainbow adjacencies and the
center has length at least

\[
                         M_a+\sum_{s=1}^a b_s.                 \tag{1.1}
\]

This is attained by concatenating normalized arc vertex words and the
center.  If two formally declared arcs of one ring are adjacent in compatible
orientation, they form one maximal block and must first be merged.  The
closed concentric spiral is the case `b_s=1`, and hence is the shortest
linear row built from a common exact lower/upper rainbow:

\[
                              M_a+a.                           \tag{1.2}
\]

This does **not** prove that an arbitrary near-width OR word must use this
common rainbow.  With `O(a)` extra adjacent edges, the lower and upper
colors may be covered by a nonmatching edge cover.  The result precisely
classifies the zero-defect adjacent-shadow skeleton.

## 2. The lower--upper color graph

Let `e_1,e_2,e_3` be the three coordinate unit vectors.  Define a bipartite
graph `Gamma_a` on `L_a \sqcup U_a` by

\[
 w\sim u
 \quad\Longleftrightarrow\quad
 u-w=e_i+e_j\text{ for two distinct }i,j.                     \tag{2.1}
\]

There is no multiplicity hidden in (2.1): the unordered pair `{i,j}` is
uniquely determined by `u-w`.

### Lemma 1 (color-edge bijection)

Edges of `Gamma_a` are in bijection with Johnson edges of `H_a`.  Under the
bijection, `(w,u)` corresponds to

\[
                         \{w+e_i,w+e_j\},                     \tag{2.2}
\]

and these two middle points have coordinatewise meet `w` and join `u`.

### Proof

If (2.1) holds, the interval from `w` to `u` contains exactly the two
rank-zero points `w+e_i` and `w+e_j`.  They differ by `e_i-e_j`, so they are
adjacent in the triangular lattice `H_a`; the coordinate bounds in the
definition of `Gamma_a` ensure that both lie in the box.

Conversely, orient a Johnson edge as

\[
                         v'=v-e_i+e_j,\qquad i\ne j.
\]

Its meet and join are respectively

\[
                         w=v-e_i,\qquad u=v+e_j,
\]

and `u-w=e_i+e_j`.  These operations are inverse. \(\square\)

It follows immediately that a set of `M_a-1` Johnson edges has all lower
meets and all upper joins exactly once if and only if its color edges form a
perfect matching of `Gamma_a`.

## 3. Degree-one peeling

Two elementary boundary observations drive the proof.

### Lemma 2 (forced color at a positive or negative wall)

1. If `w in L_a` has `w_k=a`, then `w` has degree one in `Gamma_a`.
2. If `u in U_a` has `u_k=-a`, then `u` has degree one in `Gamma_a`.

### Proof

An edge from `w` adds one to two distinct coordinates.  If one of those
were coordinate `k`, it would leave the box.  Hence it must add to the two
other coordinates, which determines `u` uniquely.  They are both below
`a`: a second coordinate equal to `a` would force the third below `-a`
because `sum w_i=-1`.  Thus the unique candidate is valid.

The upper statement is the reversed argument.  A predecessor subtracts one
from two distinct coordinates and cannot subtract from coordinate `k`; the
other two coordinates are strictly above `-a`, so the unique predecessor is
valid. \(\square\)

Write the outer ring `R_a`, starting at `(a,-a,0)`, in its six directed
sides

\[
\begin{array}{c|c|c}
\text{side}&\text{step}&\text{forced endpoint color}\\ \hline
0&(0,1,-1)&\text{meet has }x=a\\
1&(-1,1,0)&\text{join has }z=-a\\
2&(-1,0,1)&\text{meet has }y=a\\
3&(0,-1,1)&\text{join has }x=-a\\
4&(1,-1,0)&\text{meet has }z=a\\
5&(1,0,-1)&\text{join has }y=-a.
\end{array}                                                   \tag{3.1}
\]

Every one of the `6a` outer-ring edges is therefore forced into every
perfect matching by Lemma 2.

For completeness, if `0<=t<a`, their meet and join colors, side by side,
are

\[
\begin{array}{c|c|c}
0&(a,-a+t,-t-1)&(a,-a+t+1,-t)\\
1&(a-t-1,t,-a)&(a-t,t+1,-a)\\
2&(-t-1,a,-a+t)&(-t,a,-a+t+1)\\
3&(-a,a-t-1,t)&(-a,a-t,t+1)\\
4&(-a+t,-t-1,a)&(-a+t+1,-t,a)\\
5&(t,-a,a-t-1)&(t+1,-a,a-t).
\end{array}                                                   \tag{3.2}
\]

These six lists are pairwise disjoint on each color side, including at
corners.  A count check is also useful: the adjacent-layer size is

\[
                         |L_a|=|U_a|=M_a-1,
\]

and hence the number of points in either adjacent layer which meet a wall
`|coordinate|=a` is

\[
 (M_a-1)-(M_{a-1}-1)=M_a-M_{a-1}=6a.                          \tag{3.3}
\]

The `6a` distinct colors in (3.2) all meet such a wall, so they exhaust the
boundary colors on both sides.

### Theorem 3 (unique perfect matching)

`Gamma_a` has a unique perfect matching.  Under Lemma 1 it is the union of
the ordinary edge sets of `R_1,...,R_a`.

### Proof

Induct on `a`.  For `a=0`, both adjacent layers are empty and the empty
matching is unique.

For `a>=1`, Lemma 2 and (3.1) force all `6a` outer-ring edges.  By (3.3),
their endpoints are exactly all lower and upper colors touching the outer
walls.  Delete those endpoints.  The remaining lower and upper vertices
are precisely

\[
 L_{a-1}=\{w\in[-a+1,a-1]^3:\sum w_i=-1\},
\]

and the analogous `U_(a-1)`.  Equation (2.1) is unchanged on these
vertices, so the remaining induced graph is exactly `Gamma_(a-1)`.
The induction hypothesis forces `R_1 \sqcup \cdots \sqcup R_(a-1)`.  Restoring
the outer forced edges proves both existence and uniqueness. \(\square\)

This proof also rules out an easy source of confusion.  Comparable pairs
with `u-w=2e_i` are not graph edges: their interval has only one middle
point, so they cannot be the meet and join of an adjacent **pair**.  The
three distinct-coordinate choices in (2.1) are exhaustive.

## 4. Trail and arc normal forms

The following general ledger explains the `+a` in the closed spiral.

Let `mu` be any perfect matching in a lower--upper color graph of the form
above, and let `G_mu` be the graph on the middle layer obtained through
Lemma 1.  Let `z(G_mu)` be its number of isolated middle vertices.  For a
nontrivial connected component `C`, write `o(C)` for the number of its
odd-degree vertices and put

\[
 \operatorname{tr}(G_\mu)
   =\sum_{C:E(C)\ne\varnothing}\max\{1,o(C)/2\}.               \tag{4.1}
\]

### Lemma 4 (trail-row ledger)

There is a middle row containing every middle vertex and every matched
edge as a consecutive pair, of length

\[
             |E(G_\mu)|+\operatorname{tr}(G_\mu)+z(G_\mu).    \tag{4.2}
\]

No row which uses every matched edge exactly once can be shorter.

### Proof

The minimum number of trails partitioning the edges of a connected graph is
`max(1,o(C)/2)`: pair its odd vertices after adjoining that many dummy
edges and take an Euler tour; conversely each open trail accounts for at
most two odd ends, while an Eulerian nonempty component still needs one
closed trail.

Write each trail by its vertex sequence.  A trail with `e` edges uses
`e+1` row positions.  Concatenate all such words and append every isolated
middle vertex once.  This proves (4.2).  The same parity argument proves
minimality for an exact edge traversal. \(\square\)

For the unique matching in Theorem 3, `G_mu` consists of the `a` cycles
`R_s` and the isolated center.  Thus

\[
 |E|=M_a-1,\qquad \operatorname{tr}=a,\qquad z=1,
\]

and (4.2) is `M_a+a`.

There is a more flexible equivalent description.  Split `R_s` into nonempty
edge-disjoint trail arcs, where the arcs together contain every ring edge
exactly once; a sole arc is the closed ring and multiple arcs are proper
paths.  Interleave their vertex words, merge adjacent compatible pieces of
the same ring, and let `b_s` be the resulting number of maximal forced-edge
trail blocks.  The
`M_a-1` forced edges require `M_a-1` adjacencies, each arc costs one initial
vertex, and the center costs one more position.  Therefore the exact length
is

\[
              (M_a-1)+\sum_s b_s+1=M_a+\sum_s b_s,             \tag{4.3}
\]

which proves (1.1).  In particular, a row of length `M_a+O(a)` using a
common exact rainbow can split the forced cycles into only `O(a)` arcs in
total: only constantly many arcs per radius on average.

The principal escape route is to use a few more color edges, so that the
lower and upper projections are surjective but no longer form one perfect
matching.  Uniqueness still gives a useful defect normal form.

### Lemma 5 (near-rainbow defect localization)

Let a bipartite graph have `n` vertices on each side and a unique perfect
matching `mu`.  If `F` is an edge cover of all `2n` vertices with

\[
                              |F|\le n+s,
\]

then there is a matching `P` contained in `F`, of size at least `n-s`, such
that:

1. `mu` symmetric-difference `P` is a union of at most `s` alternating paths and no
   alternating cycles; and
2. at most `2s` edges of `F` lie outside `P`.

Consequently every edge of `mu` omitted by `P` lies on one of at most `s`
alternating defect paths.

### Proof

For a graph without isolated vertices, the minimum edge-cover size is
`2n-nu`, where `nu` is its maximum matching size.  Apply this to the
subgraph with edge set `F`.  Since `F` itself is an edge cover,

\[
                         |P|=\nu(F)\ge2n-|F|\ge n-s.           \tag{4.4}
\]

The symmetric difference of two matchings is a disjoint union of alternating
paths and cycles.  An alternating cycle between `P` and `mu` would allow us
to toggle `mu` on that cycle and obtain a second perfect matching, contrary
to uniqueness.  Every path endpoint is unmatched by `P`, because `mu` is
perfect.  There are `2(n-|P|)` such endpoints, hence at most
`n-|P|<=s` paths.  Finally,

\[
                  |F\setminus P|\le(n+s)-(n-s)=2s.             \tag{4.5}
\]

This proves both assertions. \(\square\)

Applied to `Gamma_a`, Lemma 5 says that an `O(a)`-defect adjacent-shadow
cover is not arbitrary: after discarding only `O(a)` extra color edges, all
departures from the frozen rings lie on only `O(a)` alternating corridors.
Those corridors may be long, so the lemma does not collapse the problem
back to the exact matching case.

## 5. Consequence of the anti-mixing theorem

The frozen matching theorem and the extreme-run anti-mixing theorem point in
the same direction.

* Exact adjacent two-sided shadows force the concentric ring **edge set**.
* Keeping whole rings contiguous is impossible for a factorable
  width-plus-perimeter band, by the earlier `3a^3` versus `4a^3` avoidance
  obstruction.
* Uniform or low-discrepancy mixing of the ring arcs is also impossible.  If
  the physical excess is `D=O(a)`, the extreme-run mesh must be
  `Omega(a^2)`.
* Formula (4.3) allows only `O(a)` total arcs.

Consequently, the exact-rainbow route, if it works at all, has a sharply
restricted remaining geometry:

> use only `O(a)` maximal forced-edge trail blocks in total, while arranging
> the selected middle-target order so that its extreme-run mesh has the
> required quadratic desert.

This rules out both previous extremes--one contiguous block per radius and
certifiably low-discrepancy radius mixing.  It does not prove that a bounded
number of macroscopic phases is sufficient or necessary, nor that the
deserts from nested subcubes align.  A six-sector or another phase-separated
shelling is one natural object to test mathematically.  It must still
satisfy the monotone-band factorability inequalities, provide the required
`4a^3+O(a^2)` lower avoidance capacity, and retain the longer upper union
shadows.  None of those last three properties follows merely from Theorem 3.

There is also a quantitative consequence stronger than saying that the
one-arc-per-ring spiral fails.

### Corollary 6 (a linear number of extra ring cuts is necessary)

Consider a family of exact-rainbow arc schedules as in (4.3), with
`sum_s b_s=O(a)`, used as the middle occurrences of a factorable monotone
band with physical excess `D=O(a)`.  If the resulting factor is to have
enough middle-avoiding intervals for the lower half, then

\[
                         \sum_{s=1}^a(b_s-1)=\Omega(a).        \tag{5.1}
\]

Thus the `+a+o(a)` occurrence regime is impossible.

### Proof

Suppose instead that the left side of (5.1) is `o(a)`.  Then only `o(a)`
rings are split.  The total number `R` of occurrences belonging to those
rings is `o(a^2)`: each ring has `O(a)` edges, and the total arc overhead is
`O(a)`.

Delete those `R` occurrences temporarily.  Every remaining radius is one
contiguous complete ring block.  As in the ring-by-ring obstruction, choose
two internal positive-extreme runs of length at most `a+1` on each such
block.  In the undeleted schedule, the distance to the next chosen run is
`O(a)+R=o(a^2)`.  Applying the exact band run inequality and charging a
fixed increment of either monotone endpoint-offset sequence only across
that distance gives

\[
 \sum_{i\notin\text{split rings}}(r_i-\ell_i)
       \le aM_a+o(a^3).
\]

The `R=o(a^2)` deleted occurrences each contribute at most `D=O(a)`, hence
another `o(a^3)`.  The exact avoidance ledger adds only
`O(D^2)=O(a^2)`.  Thus the total number of intervals avoiding every middle
witness is at most

\[
                         3a^3+o(a^3),
\]

whereas the lower half has `4a^3+O(a^2)` targets.  This contradiction proves
(5.1). \(\square\)

Combining Corollary 6 with anti-mixing leaves a narrow but nonempty regime:
linearly many extra ring cuts in total, only constantly many cuts per ring on
average, and an ordering with a quadratic extreme-run desert.  The theorem
does not force those cuts to occur on linearly many distinct rings.

## 6. Exact scope

The theorem concerns the first shadow layer of a prescribed middle order.
It proves:

1. uniqueness of a common perfect matching between lower and upper adjacent
   colors;
2. the forced concentric edge set;
3. the optimal `M_a+a` row length for an exact traversal of that matching;
   and
4. the `O(a)`-arc normal form for every near-width traversal of it.

It does not prove that every unrestricted OR word selects its rank-adjacent
witnesses from consecutive pairs of one central row.  It also does not
exclude a near-perfect nonmatching edge cover with `O(a)` duplicate colors,
or a variable-band construction whose adjacent masks arise through a more
general endpoint schedule.  Those are the precise escape routes.
