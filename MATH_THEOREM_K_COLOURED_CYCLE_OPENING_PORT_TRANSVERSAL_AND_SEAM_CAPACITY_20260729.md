# Exact coloured cycle opening, port transversals, and the physical seam-capacity obstruction

## Status and scope

This note isolates the exact combinatorics of opening a lower-rainbow
Johnson `2`-factor and joining its cycle components into one spanning path.
It proves three facts.

1. An ordinary two-edge switch between two vertex-disjoint cycles cannot
   preserve the two deleted lower colours.  Thus twelve independent
   palette-neutral `2`-switches are not a viable interpretation of the
   thirteen-cycle endpoint.
2. The correct one-cut-per-cycle construction is an exact coloured port
   transversal.  For fixed ports it is a common size-`c-1` independent set
   of a graphic matroid and three partition matroids; in the useful
   child-pays normal form it is exactly a matching with subtour cuts, or a
   directed Hamilton path in the child-star compatibility graph.
3. Irrespective of port compatibility, twelve physical seams create only
   `24` new depth-two windows and `36` new depth-three windows.  Consequently
   they cannot complete the remaining shadows of the retained `seed0`
   factor: at least `84` upper-`q2`, `42` lower-`q3`, and `9` upper-`q3`
   physical holes remain before cut losses are charged.

The first two statements are abstract and exact.  The final numerical
statement uses only the independently audited physical hole masses of
`seed0`.  Nothing here asserts residence-safe port existence, compiler
feasibility, or a contiguous-OR word.

## 1. Johnson colours and cut states

Let

\[
 G=J(n,r),\qquad V(G)=\binom{[n]}r.
\]

For a Johnson edge `AB`, define its lower colour

\[
 \kappa_-(AB)=A\cap B\in\binom{[n]}{r-1}.             \tag{1.1}
\]

Thus an edge of colour `S` has the unique form

\[
 \{S+a,S+b\},\qquad a,b\notin S,quad a\ne b.        \tag{1.2}
\]

Let `F` be a spanning `2`-factor with vertex-disjoint cycle components

\[
 C_1,\ldots,C_c,
\]

and suppose that `kappa_-` is injective on `E(F)`.  On the odd ground
`n=2r-1`, the number of factor edges and the number of lower colours are
both `binom(n,r)`, so injectivity is equivalent to use of every lower colour
exactly once.

A **cut state** on `C_i` consists of an edge `e_i=u_iv_i` and one of the
two orientations of `C_i-e_i`.  Write the resulting oriented path as

\[
 P(s_i)=(a_i,\ldots,b_i)                              \tag{1.3}
\]

and put

\[
 \lambda_i=\kappa_-(e_i).                             \tag{1.4}
\]

The vertices `a_i,b_i` are respectively the initial and terminal ports.
Both contain `lambda_i`.  Reversing the state exchanges `a_i,b_i` and does
not change `lambda_i`.

Because `F` is lower-rainbow, cut edges on distinct components have
distinct colours.

## 2. Ordinary palette-neutral two-switches are impossible

### Theorem 2.1 (lower-colour two-switch rigidity)

Let `e_S` and `e_T` be edges in two vertex-disjoint cycles of a
lower-rainbow Johnson factor, with lower colours `S` and `T`.  Delete these
two edges.  No nontrivial perfect matching of their four endpoints by two
Johnson edges has lower-colour multiset `{S,T}`.

In particular, an ordinary graph `2`-switch cannot merge two disjoint
factor cycles while preserving the complete lower palette.

#### Proof

Write

\[
 e_S=\{x_0,x_1\},\qquad e_T=\{y_0,y_1\}.
\]

The four endpoints are distinct because the cycles are vertex-disjoint.
Also `S ne T`, since the old factor is lower-rainbow.

Any nontrivial perfect matching is a cross matching.  After renaming the
`y` endpoints and interchanging `S,T` if necessary, suppose that one new
edge is `x_0y_0` of colour `S` and the other is `x_1y_1` of colour `T`.
The first assertion gives `S subset y_0`; because `y_0` is an endpoint of
`e_T`, it also contains `T`.  Similarly, the second assertion gives
`T subset x_1`, while `x_1` already contains `S`.  Hence both `y_0` and
`x_1` contain `S union T`.

Two distinct `(r-1)`-sets have union of size at least `r`.  Since that
union is contained in an `r`-set, it has size exactly `r`, and therefore

\[
 y_0=S\cup T=x_1.
\]

This contradicts distinctness of the four endpoints.  The other cross
matching is identical after relabelling.  \(\square\)

### Consequence 2.2 (architecture boundary)

No sequence whose every step is an ordinary palette-neutral two-edge
fusion can even perform its first inter-component merge.  This does not
exclude:

* a compound trade changing at least three old edges;
* temporary lower-colour debt repaired by a later trade;
* cutting all cycles and producing a spanning path with one deliberately
  absent lower colour.

The last alternative is the exact twelve-seam architecture considered
below.

## 3. Exact all-at-once path splice

Fix one cut state `s_i` on each component.  A connector from `C_i` to
`C_j` is the Johnson edge

\[
 f_{ij}=b_i a_j,                                      \tag{3.1}
\]

when this edge exists.

### Definition 3.1 (child-pays connector)

The connector `i -> j` is **child-pays** if

\[
 \kappa_-(b_i a_j)=\lambda_j.                         \tag{3.2}
\]

Equivalently,

\[
 \lambda_j\subset b_i.                               \tag{3.3}
\]

Indeed `a_j=lambda_j+x` for one coordinate `x`, and the distinct middle
owner `b_i` forms an edge of intersection `lambda_j` with `a_j` exactly
when `b_i=lambda_j+y` for `y ne x`.  Thus the compatibility test is a
literal owner-star containment test.

Let `D(s_1,...,s_c)` be the directed graph on `[c]` whose arcs are the
child-pays connectors.

### Theorem 3.2 (child-pays port-transversal theorem)

Fix a component `r_0` as root.  The following are equivalent.

1. The chosen oriented component paths can be concatenated, starting with
   `P(s_(r_0))`, into one spanning path using `c-1` child-pays connectors.
2. `D(s_1,...,s_c)` contains a directed Hamilton path starting at `r_0`.
3. There are zero-one values `x_ij` on the arcs of `D` satisfying

   \[
   \begin{aligned}
    &\sum_i x_{ij}=1 &&(j\ne r_0),\\
    &\sum_i x_{i r_0}=0,\\
    &\sum_j x_{ij}\le1 &&(i\in[c]),                  \tag{3.4}\\
    &\sum_{i,j\in Q}x_{ij}\le |Q|-1
       &&(\varnothing\ne Q\subseteq[c]\setminus\{r_0\}).
   \end{aligned}
   \]

Whenever these conditions hold, the new path has lower-colour multiset

\[
 \kappa_-(E(F))\setminus\{\lambda_{r_0}\}.           \tag{3.5}
\]

Thus it is exactly lower-rainbow and misses only the root cut colour.

#### Proof

The equivalence of 1 and 2 is the definition of concatenation through the
terminal and initial ports.  A Hamilton path gives (3.4).

Conversely, the first two lines of (3.4) give indegree one at every
nonroot and indegree zero at the root; the third gives outdegree at most
one.  The last line excludes a directed cycle on nonroot vertices.  Every
component not containing the root would contain a directed cycle, because
all of its vertices have indegree one.  Hence the selected arcs are
connected.  There are `c-1` of them, and the indegree/outdegree bounds force
the connected graph to be one consistently oriented spanning path.

Cutting the cycles removes the pairwise distinct colours
`lambda_1,...,lambda_c`.  Each nonroot component has one incoming connector,
and by (3.2) that connector restores exactly its own cut colour.  The root
has no incoming connector, proving (3.5).  \(\square\)

### Remark 3.3 (matching versus topology)

If the subtour inequalities are omitted, (3.4) is a bipartite matching
which saturates all nonroot heads.  Its feasibility has the ordinary Hall
criterion

\[
 |N^-(Q)|\ge |Q|\qquad
 (Q\subseteq[c]\setminus\{r_0\}).                    \tag{3.6}
\]

Such a matching may be the disjoint union of a root-to-terminal path and
one or more directed cycles.  Hence Hall is necessary and sufficient for a
path cover of the ports, but not for the required spanning path.  The
subtour inequalities are the exact missing topological condition.  If the
outdegree bounds are dropped instead, the cut form of the last line is the
usual rooted-arborescence condition; branching cannot be realized with one
terminal port per opened cycle.

## 4. The general palette-recycling criterion

Child-pays is a useful sufficient normal form, but global palette recovery
need not assign a seam colour to its head component.  For fixed cut states,
let `A` be the set of all legal directed connectors `b_i a_j` whose lower
colour belongs to

\[
 \Lambda=\{\lambda_1,\ldots,\lambda_c\}.              \tag{4.1}
\]

On the connector ground set define four matroids:

* `M_G`, the graphic matroid of the underlying component multigraph;
* `M_out`, the partition matroid allowing at most one connector with each
  tail component;
* `M_in`, the partition matroid allowing at most one connector with each
  head component;
* `M_col`, the partition matroid allowing at most one connector of each
  lower colour.

### Theorem 4.1 (four-matroid port criterion)

For the fixed cut states, a one-cut-per-cycle spanning path whose connector
colours recycle all but one member of `Lambda` exists if and only if `A`
contains a common independent set of `M_G,M_out,M_in,M_col` of size `c-1`.

#### Proof

Any such spanning path is acyclic, uses every tail and head at most once,
and uses `c-1` distinct colours from the `c`-set `Lambda`; hence its arcs
form the stated common independent set.

Conversely, a size-`c-1` independent set of `M_G` is a forest with `c-1`
edges on the `c` component vertices, hence a spanning tree.  Independence
in `M_out` and `M_in` makes every vertex have undirected degree at most two;
at an internal vertex one edge enters and one leaves.  The tree is therefore
a consistently oriented Hamilton path.  Independence in `M_col`, together
with restriction to colours in `Lambda`, says that its `c-1` connectors use
exactly `c-1` cut colours.  Cutting removed all `c` cut colours, so precisely
one remains absent.  \(\square\)

### Remark 4.2 (why there is no single Hall test)

Theorem 4.1 is a common-independent-set criterion for one graphic and three
partition matroids, not ordinary two-matroid intersection.  Even before
connectivity, arbitrary-colour seams give a three-dimensional matching
problem on tail, head, and colour.

The four triples

\[
 (a,1,R),\ (a,2,B),\ (b,1,B),\ (b,2,R)                \tag{4.2}
\]

are the smallest parity rectangle: every two-coordinate projection has a
perfect matching and all separate Hall tests pass, but each tail-head
perfect matching is monochromatic.  Thus no rainbow perfect matching
exists.  Palette, endpoint, and topology constraints cannot in general be
audited independently.

### Remark 4.3 (variable port states)

Theorem 4.1 is applied after choosing one oriented cut state on each cycle.
With variable ports, the exact condition is

\[
 \exists(s_1,\ldots,s_c)\quad
 \exists A'\subseteq A(s_1,\ldots,s_c)
\]

with `A'` as in Theorem 4.1.  Incoming and outgoing connectors at a given
component must use the same selected cut state.  That port-consistency
condition is not captured by independently choosing an incoming and an
outgoing endpoint; omitting it is a genuine relaxation.

Residence, terminal pins, and protected shadow collars may be imposed by
deleting ineligible states and connector arcs before applying the theorem.
Global shadow coverage still needs the load ledger below.

## 5. Exact cut/seam shadow ledger

For a sequence of middle owners define the depth-`q` lower and upper traces

\[
 \Phi_q^-(T_0,\ldots,T_q)=\bigcap_{h=0}^qT_h,
 \qquad
 \Phi_q^+(T_0,\ldots,T_q)=\bigcup_{h=0}^qT_h.         \tag{5.1}
\]

Fix cut states and a spanning-path connector set.  For a physical target
`Z`, let

* `L_q^pm(Z)` be its old cyclic trace load;
* `D_q^pm(s_i,Z)` count old windows with trace `Z` crossing the cut edge of
  state `s_i`;
* `G_q^pm(f,Z)` count new windows with trace `Z` crossing connector `f`.

Suppose every opened component path has at least `q` vertices, so a
`q`-edge window crosses at most one new seam.  Then the new linear-path load
is exactly

\[
 L_q^{\pm\prime}(Z)
 =L_q^\pm(Z)-\sum_{i=1}^cD_q^\pm(s_i,Z)
              +\sum_{f}G_q^\pm(f,Z).                 \tag{5.2}
\]

#### Proof

Every new window is either wholly inside one retained component segment or
crosses exactly one seam.  The first class is precisely the old cyclic
windows not crossing a chosen cut.  The second class is counted by the last
sum.  These classes are disjoint and exhaustive.  \(\square\)

Thus exact preservation or completion of a target deck is the family of
integer inequalities

\[
 L_q^\pm(Z)-\sum_iD_q^\pm(s_i,Z)+\sum_fG_q^\pm(f,Z)
 \ge1                                                       \tag{5.3}
\]

for every required physical target `Z`.  In particular, a seam advertised
as gaining a missing target is not automatically safe: its cut states may
simultaneously delete the last witness of a different target.

For a fixed connector set `A'` and a set `M` of initially missing targets,
put a bipartite edge `f--Z` when `G_q^pm(f,Z)>0`.  If one demands a distinct
seam designated for each target of `M`, such a designation exists exactly
when

\[
 |N(Q)|\ge |Q|\qquad(Q\subseteq M).                   \tag{5.4}
\]

This is an ordinary SDR after the port path has been selected.  Selecting
the path and the gains simultaneously is the common-base problem of
Theorem 4.1 with additional covering inequalities (5.3); it is not implied
by (5.4) on an unselected seam catalogue.

## 6. Universal physical seam-capacity bound

### Lemma 6.1 (exact number of new windows)

Assume every opened segment has at least `q` vertices.  Each connector lies
in exactly `q` new `q`-edge windows, namely

\[
 (A_{-a},\ldots,A_0,B_0,\ldots,B_{q-1-a}),
 \qquad a=0,1,\ldots,q-1,                             \tag{6.1}
\]

where `A_0B_0` is the connector.  No such window contains two connectors.
Consequently `c-1` seams create exactly

\[
 q(c-1)                                                \tag{6.2}
\]

new physical depth-`q` windows.

#### Proof

A `q`-edge window containing the connector has `a` old edges on its left
and `q-1-a` old edges on its right for a unique `a` in the stated range.
The segment-length assumption supplies all these windows.  Crossing two
connectors would require traversing an entire intervening segment and hence
more than `q` edges.  \(\square\)

### Corollary 6.2 (hole-capacity obstruction)

If the old factor has `M_q` missing physical targets at depth `q`, any
one-cut-per-cycle splice leaves at least

\[
 \max\{0,M_q-q(c-1)\}                                 \tag{6.3}
\]

of those targets missing.  This lower bound ignores new holes caused by
cutting, so it can only be strengthened by the full ledger (5.2).

#### Proof

An initially missing target can become covered only by a new seam-crossing
window.  Each new window has one trace value, and there are only (6.2) such
windows.  \(\square\)

## 7. Exact `seed0` implication

For the retained factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.engine.json
```

the thirteen physical cycles all have length at least `15`, so Lemma 6.1
applies at depths two and three.  The exact missing physical masses are:

* upper `q2` / rank ten: `108`, from orbit sizes
  `15,15,15,15,15,15,15,3`;
* lower `q3`: `78`, from orbit sizes `15,15,15,15,15,3`;
* upper `q3` / rank eleven: `45`, from three size-`15` orbits.

There are only twelve connectors.  Therefore every literal thirteen-cut,
twelve-seam spanning path has residual holes at least

\[
\begin{array}{c|c|c|c}
\text{deck}&M_q& q(c-1)&\text{unavoidable residual}\\ \hline
\text{upper }q2&108&24&84\\
\text{lower }q3&78&36&42\\
\text{upper }q3&45&36&9.
\end{array}                                           \tag{7.1}
\]

This is independent of the lower-palette port problem and remains true
even if every seam is residence-safe and every new window hits a different
old hole.

The tempting comparison

```text
12 seams versus 8+3 missing upper orbits
```

mixes quotient and physical units.  Once the equivariant factor is opened
at twelve physical seams, a new window witnesses one physical target, not
all fifteen translates in its orbit.  Hence the twelve-seam splice can be a
topological/compiler opening, but it cannot by itself be the advertised
all-depth shadow repair.

## 8. Sharp remaining alternatives

The proven obstruction leaves three logically distinct routes.

1. Find the missing physical shadow witnesses inside the fixed-matching
   factor fibre before opening cycles; then solve the port-transversal path
   problem while protecting those witnesses through (5.3).
2. Use a compound braid with substantially more than twelve changed
   adjacencies/windows, while arranging that its net component count still
   falls to one path and its lower palette is restored.
3. Relax the demand that every physical missing target be repaired by the
   seam stage, if the downstream compiler supplies a separately proved
   literal source for the residual targets.

What is closed is the direct claim that twelve ordinary seams simultaneously
merge the thirteen cycles and fill the current `seed0` depth-two/depth-three
physical holes.
