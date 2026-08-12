# The `k=17` occurrence-labelled two-path connector theorem

Date: 2026-07-31  
Status: exact theorem and fixed-residual reduction.  With the lower palette
split free, the abstract doubly-rainbow two-path connector is constructive
and unconditional once a Hamilton cycle of `M_17` is fixed.  For a completed
tail with an arbitrary rank-eight palette, the residual prefix first has an
exact Hoffman factor test, followed by a genuinely graphic and
occurrence-labelled grouped-tile gate.  For arbitrary physical endpoint
occurrences, the final two-owner connector is an exact complementary-pair
matching on four ports.  No occurrence-factorable prefix or tail is claimed.

## 1. Setup

Put

\[
 {\cal X}=\binom{[17]}8,\qquad {\cal Y}=\binom{[17]}9,
 \qquad N=|{\cal X}|=|{\cal Y}|=24310.
\]

The middle-levels graph `M_17` is the bipartite inclusion graph on
`X union Y`.  A lower-ended alternating path has the form

\[
 x_0,H_0,x_1,H_1,\ldots,H_{s-2},x_{s-1},              \tag{1.1}
\]

with `x_i in X`, `H_i in Y`, and `x_i,x_{i+1} subset H_i`.
It is doubly rainbow when its lower and upper vertices are each distinct.

The corrected two-zone ledger asks for two such paths with shore sizes

\[
 (7400,7399),\qquad(16910,16909),                     \tag{1.2}
\]

together with the two omitted upper vertices.

## 2. Abstract connector is automatic

### Theorem 2.1 (Hamilton-cycle cut construction)

Let

\[
 x_0,H_0,x_1,H_1,\ldots,x_{N-1},H_{N-1},x_0          \tag{2.1}
\]

be any Hamilton cycle of `M_17`, with indices read modulo `N`.  Delete
`H_0` and `H_7400` and their four incident cycle edges.  The remainder is
the disjoint union of two lower-ended alternating paths having respectively

\[
 7400\text{ lower and }7399\text{ upper vertices},
\]

and

\[
 16910\text{ lower and }16909\text{ upper vertices}. \tag{2.2}
\]

The two deleted upper vertices reconnect the four path endpoints crosswise
and recover the original Hamilton cycle.  Thus an abstract rank-eight and
rank-nine palette split of the required cardinalities, including its endpoint
connector, always exists when the lower split may be chosen from the cycle.

#### Proof

The first open arc is

\[
 x_1,H_1,x_2,\ldots,H_{7399},x_{7400},
\]

and therefore has `7400` lower and `7399` upper vertices.  The complementary
arc has the remaining `N-7400=16910` lower and `16909` upper vertices.
The vertex `H_0` joins `x_0` to `x_1`, one endpoint from each arc, while
`H_7400` joins `x_7400` to `x_7401`, again one endpoint from each arc.
Restoring these two vertices and their four edges gives (2.1).  \(\square\)

For `M_17`, existence of the cycle in (2.1) follows from the middle-levels
Hamilton-cycle theorem.  The construction above is linear-time once the
cycle is listed.  It neither uses nor proves the physical low-block and tail
factorizations.  In particular, it does not show that the short arc contains
the `2328` certified internal block-union colours, let alone that those
colours occur at the required block positions.

## 3. Exact occurrence-labelled endpoint gate

The two literal seam occurrences do not automatically provide the abstract
connector from Theorem 2.1.  Indeed, write the end of the prefix as
`...,q_7399,q_7400` and the beginning of the tail as `t_0,t_1,t_2,...`.
The endpoint lower colours and the two seam-owner colours are

\[
 C_{7399}=q_{7399}\cup q_{7400},\qquad
 V_0=t_0\cup t_1\cup t_2,                            \tag{3.0a}
\]

\[
 S_0=q_{7399}\cup q_{7400}\cup t_0,qquad
 S_1=q_{7400}\cup t_0\cup t_1.                      \tag{3.0b}
\]

Thus `C_7399 subset S_0` is forced.  No incidence of `S_0` with `V_0`,
no incidence of `S_1` with either displayed endpoint, and no incidence with
the two remote endpoints is forced by the chronological formulas.  Such
incidences can occur only through additional set containments and compatible
literal boundary states.  Consequently the statement that the two palettes
form two abstract middle-levels paths is strictly weaker than a physical
two-path connector theorem.

Fix two lower-ended physical path traces `P,T`.  Their four oriented endpoint
occurrences are

\[
 E_P=\{p_0,p_1\},\qquad E_T=\{t_0,t_1\}.             \tag{3.1}
\]

An endpoint occurrence records its rank-eight colour and all literal boundary
data needed for seam replay; two occurrences with the same rank-eight set but
different boundary data are different ports.  Let `A,B` be the two unused
rank-nine colours.

For `H in {A,B}`, define

\[
 K_H\subseteq E_P\mathbin{\times}E_T                 \tag{3.2}
\]

by `(p_i,t_j) in K_H` exactly when joining those two *occurrences* through
`H` is a legal literal local splice: both endpoint rank-eight colours are
facets of `H`, the required overlap/boundary occurrence agrees, and replay
preserves every frozen row outside the seam.  Thus (3.2), rather than bare
set containment, is the fail-closed physical connector relation.

Write

\[
 \overline{(p_i,t_j)}=(p_{1-i},t_{1-j}).              \tag{3.3}
\]

### Theorem 3.1 (two-owner connector criterion)

The two paths extend to one occurrence-labelled doubly-rainbow Hamilton cycle
using `A` and `B` if and only if

\[
 \boxed{\quad
 \text{there is }e\in K_A\text{ with }\bar e\in K_B.
 \quad}                                               \tag{3.4}
\]

Equivalently, the three-uniform hypergraph with vertices
`{A,B} union E_P union E_T` and hyperedges

\[
 \{H,p_i,t_j\}\quad ((p_i,t_j)\in K_H)               \tag{3.5}
\]

has a two-edge perfect matching.

#### Proof

In a Hamilton cycle, each omitted upper vertex has degree two and must join
one endpoint of `P` to one endpoint of `T`; joining the two endpoints of one
old path would close that path separately.  Every one of the four endpoint
occurrences must be used once.  Hence the edge used by `B` is exactly the
complement (3.3) of the edge used by `A`, proving necessity.  Conversely,
an allowed complementary pair uses every endpoint once, joins the two old
paths twice crosswise, and therefore forms one cycle.  The definition of
`K_H` supplies literal legality and preserves both palettes.  \(\square\)

For completeness, let `I_H` be the set of endpoint occurrences that admit a
legal one-sided incidence with `H`.  There is a spanning alternating
Hamilton **path** through the two old paths and both unused upper vertices if
and only if, after possibly interchanging `A,B`, there are

\[
 (p_i,t_j)\in K_A
 \quad\hbox{and}\quad
 e\in\{p_{1-i},t_{1-j}\}\cap I_B.                  \tag{3.5a}
\]

Indeed, the component graph on `P,T,A,B` must be a three-edge spanning path
in `K_{2,2}`.  Its degree-two upper component supplies the cross pair in
(3.5a), and its degree-one upper component supplies the one-sided incidence.
Conversely those three incidences join all four components without a cycle.
In particular, any cycle supplied by Theorem 3.1 can be opened by deleting
one of its connector incidences.

### Corollary 3.2 (Cartesian ports and two ordinary Hall tests)

Suppose seam legality factorizes endpointwise:

\[
 K_H=N_P(H)\mathbin{\times}N_T(H),                   \tag{3.6}
\]

where `N_P(H) subseteq E_P` and `N_T(H) subseteq E_T`.  Then (3.4) holds if
and only if each of the two `2 by 2` endpoint-incidence graphs

\[
 E_P\longleftrightarrow\{A,B\},\qquad
 E_T\longleftrightarrow\{A,B\}                      \tag{3.7}
\]

has a perfect matching.  Thus in the Cartesian case the connector gate is
exactly two ordinary Hall conditions.

#### Proof

A connector cycle assigns the two endpoints of each old path bijectively to
`A,B`, proving necessity.  Conversely choose a perfect matching in each
graph (3.7).  For each `H`, its two matched endpoints, one from each path,
form an allowed pair by (3.6), and the two resulting pairs are complementary.
\(\square\)

Bare middle-levels incidence is Cartesian, so Theorem 2.1 is a special case.
Literal occurrence constraints need not be Cartesian.

If the two unused owners are not fixed in advance and only bare incidence is
required, the test becomes still smaller.  Write `X_e` for the lower colour
of endpoint `e`.  A connector cycle exists if and only if one of the two
bijections `pi:{0,1}->{0,1}` satisfies

\[
 |X_{p_i}\cup X_{t_{\pi(i)}}|=9\quad(i=0,1),         \tag{3.7a}
\]

and the two displayed unions are distinct unused upper colours.  This is
because two distinct rank-eight sets have a common rank-nine neighbour
exactly when their union has rank nine, and that neighbour is then unique.
For a fixed complementary owner palette, the two unions in (3.7a) must be
exactly that palette.

### Proposition 3.3 (minimal parity obstruction)

Identify a cross pair `(p_i,t_j)` with `(i,j) in {0,1}^2`.  Complementation
preserves the parity `i+j mod 2`.  Therefore a connector requires the two
owners to support complementary pairs in the same parity class.

This condition is genuinely pair-level.  For example,

\[
 K_A=\{(0,0),(1,1)\},\qquad
 K_B=\{(0,1),(1,0)\}                                 \tag{3.8}
\]

supports every endpoint under each owner separately, but (3.4) fails.
Thus marginal endpoint support, and even ownerwise support of all four
endpoints, does not imply a physical connector.  Formula (3.8) is the
smallest occurrence-coupled parity obstruction.

## 4. Local occurrence-labelled Johnson edges

There is also a useful exact description of the internal occurrence lists.
Let a physical central occurrence carry a set `a`, and let `H in Y` be its
desired rank-nine owner.  Any adjacent rank-eight colours through this
occurrence have the form

\[
 X=H-\{u\},\qquad Y=H-\{v\},\qquad u\ne v,           \tag{4.1}
\]

and necessarily

\[
 a\subseteq X\cap Y=H-\{u,v\}.                       \tag{4.2}
\]

Consequently the support-only candidate bank is

\[
 {\cal E}_{a,H}=
 \bigl\{\{H-u,H-v\}:u\ne v,\ u,v\in H-a\bigr\}.    \tag{4.3}
\]

When `a subseteq H` and `|a|=s`, this bank has

\[
 |{\cal E}_{a,H}|=\binom{9-s}{2}.                   \tag{4.4}
\]

In particular, a rank-seven separator forces a unique Johnson edge once
its upper owner `H` is assigned.  A fixed literal block can only shrink
(4.3), because its two outer occurrences must also realize the prescribed
rank-eight unions.

This exposes the first exact occurrence obstruction: after assigning upper
owners to the `2536` rank-seven separators, their `2536` forced Johnson
edges must be distinct, have degree at most two, and form a forest inside
the desired prefix path.  Any forced cycle is already a graphic-Rado
certificate of failure.

There is a sharp ordinary-Hall projection before the graphic test.  Fix the
candidate prefix lower palette \({\cal R}_8\) and, for each selected
rank-seven separator `B`, put

\[
 D_B=\{x\in[17]-B:B+x\in{\cal R}_8\},               \tag{4.5}
\]

\[
 \Omega_B=\{B+\{u,v\}:u,v\in D_B,\ u\ne v\}.        \tag{4.6}
\]

The set `Omega_B` is exactly the list of upper owners for which the forced
separator edge has both endpoints in the prefix palette.  Hence distinct
upper owners can be assigned to all separators if and only if

\[
 \left|\bigcup_{B\in{\cal S}}\Omega_B\right|
       \ge |{\cal S}|                                \tag{4.7}
\]

for every separator subfamily \({\cal S}\).  This is ordinary Hall, and is
therefore necessary and sufficient for the owner-assignment projection.
It immediately includes the local cut `|D_B|>=2`.  It does not impose
degree two or acyclicity on the resulting forced edges.

For the unrestricted lower palette, every `D_B` has size ten.  The full
rank-seven/rank-nine inclusion graph has left degree `45` and right degree
`36`, so edge counting gives

\[
 45|{\cal S}|\le36|N({\cal S})|,
\]

and (4.7) holds with slack.  Thus any separator-owner Hall obstruction is
created by the selected `7400`-vertex prefix palette or by occurrence
restrictions, not by the full Boolean inclusion graph.

### Theorem 4.1 (resource-disjoint separator-diamond reserve)

Let \({\cal I}\subseteq{\cal X}\) be any set of `2328` already reserved
rank-eight colours; in particular, it may be the certified internal-block
union set.  There exist `2536` Johnson edges

\[
 e_j=X_jY_j\quad(1\le j\le2536)                      \tag{4.8}
\]

such that

1. all `5072` endpoints `X_j,Y_j` are distinct and avoid \({\cal I}\);
2. all rank-seven intersections \(X_j\cap Y_j\) are distinct; and
3. all rank-nine unions \(X_j\cup Y_j\) are distinct.

Moreover, a greedy algorithm finds such a bank from the complete Johnson
edge list.

#### Proof

The Johnson graph `J(17,8)` has `24310` vertices and degree
`8*9=72`, hence

\[
 |E(J(17,8))|=\frac{24310\cdot72}{2}=875160.         \tag{4.9}
\]

Deleting every edge incident with \({\cal I}\) removes at most

\[
 2328\cdot72=167616

\]

edges, leaving at least `707544`.

Join two surviving Johnson edges in a conflict graph when they share a
rank-eight endpoint, their rank-seven intersections agree, or their
rank-nine unions agree.  A fixed Johnson edge conflicts with at most

\[
 2(72-1)+(45-1)+(36-1)=221                          \tag{4.10}
\]

others: `71` through each endpoint, `44` through its intersection, and `35`
through its union.  Greedy independent-set selection therefore returns at
least

\[
 \left\lceil\frac{707544}{222}\right\rceil=3188     \tag{4.11}

pairwise resource-disjoint edges.  Keep any `2536`.  \(\square\)

Taking the `5072` endpoints in (4.8) together with \({\cal I}\) gives
exactly `7400` distinct rank-eight colours, while (2)--(3) give distinct
separator and central owner colours.  This is only a palette reserve.  It
does not assign the two endpoints of each diamond to the two low-block port
occurrences adjacent to that separator, and it does not order the resulting
block transitions.  Those occurrence correlations are the next gate.

## 5. Exact Rado relaxation after owner assignment

Let `Q` be a set of physical turn occurrences and let

\[
 \sigma:Q\longrightarrow{\cal Y}'                   \tag{5.1}
\]

be a bijection onto the selected upper palette.  For each `q in Q`, let
`F_q` be its full literal candidate edge set, a subset of
`E_{a(q),sigma(q)}` from (4.3), on the selected lower rank-eight vertices.

### Theorem 5.1 (occurrence-conditioned graphic Rado criterion)

There is a palette-rainbow occurrence-labelled forest choosing one edge
from every `F_q` if and only if, for every `S subseteq Q`,

\[
 r_{\rm gr}\left(\bigcup_{q\in S}F_q\right)\ge |S|. \tag{5.2}
\]

#### Proof

This is Rado's independent-transversal theorem applied to the graphic
matroid on the lower Johnson-edge ground set.  \(\square\)

For a prefix with `7400` lower vertices and `7399` turns, a transversal in
(5.2) is a spanning tree.  It is a Hamilton path exactly when every lower
vertex has degree at most two.  For the global two-path split, `24308`
independent edges on `24310` lower vertices give a two-component forest;
requiring every degree to lie in `{1,2}` makes the two components paths.
Thus (5.2) is an exact acyclicity test, not a replacement for the degree-two
or literal block-order constraints.

Without occurrence restrictions, the Rado inequalities never obstruct the
two-path split.  Indeed, for a family `A` of proper upper vertices, each
connected component `A_i` of the corresponding clique-union satisfies

\[
 |\partial A_i|\ge |A_i|+1.                          \tag{5.3}
\]

The weak inequality follows by edge counting in the `9`-regular
middle-levels graph.  Equality would make the bipartite vertex set formed by
`A_i` and its lower shadow a union of components of `M_17`; connectedness
would force `A_i` to be the whole upper shore, which is
impossible after two upper vertices are omitted.  Summing (5.3) gives
graphic rank at least `|A|`.

## 6. Exact grouped-tile model for the certified prefix inventory

The coloured inventory admits a compact occurrence-exact hypergraph model.
Give every low block two distinct left/right *halfports*.  A two-letter block
labels them by its two physical letters; a singleton's two halfports carry
the same one-letter occurrence but represent its two possible incidences.
Let `A(p)` be the low mask on halfport `p`, and let \({\cal I}\)
be the `2328` fixed internal block-union colours.
Fix also a desired prefix lower palette \({\cal R}_8\supseteq{\cal I}\) of
size `7400` and a desired internal prefix upper palette
\({\cal R}_9^\circ\) of size `7399`.

### Proposition 6.0 (bare orientation and block order are unconditional)

Choose either orientation of every two-letter block, arbitrarily, and keep
the unique state of each singleton.  The induced local-compatibility
digraph on these `2537` selected states has minimum in- and outdegree at
least `1321`, and hence has a directed Hamilton cycle.

#### Proof

The audited `4865`-state digraph has minimum semidegree `3649`.  A state of
a two-letter block has `4863` possible states outside its own block, so at
most `4863-3649=1214` of them are nonneighbours in either direction.  A
singleton has at most `4864-3649=1215` such nonneighbours.  Any selected
transversal contains `2536` other block states, hence its minimum semidegree
is at least

\[
                         2536-1215=1321>2537/2.
\]

The directed Hamilton-cycle theorem of Ghouila--Houri now applies.
\(\square\)

Opening one arc gives a block order.  This proposition certifies only that
every retained arc has at least one locally legal separator-centred triple.
It does not choose distinct separators or pair/owner colours and does not
certify either low-centred edge adjacent to a fixed internal block colour.

A separator tile is a tuple

\[
 \tau=(p,B,p';X,Y,H)                                \tag{6.1}
\]

with halfports on different blocks, with `B` a rank-seven mask, and

\[
 X=A(p)\cup B,\qquad Y=B\cup A(p'),qquad
 |X|=|Y|=8,qquad H=X\cup Y,\quad |H|=9.             \tag{6.2}
\]

The tile consumes its two halfports, separator colour `B`, the two
rank-eight colours `X,Y`, and the central rank-nine colour `H`.

Choose `2536` tiles subject to:

1. every halfport is used at most once and exactly two of the `5074`
   halfports are unused;
2. the `B` resources, the `5072` resources `X,Y`, and the `H` resources are
   separately distinct, with every `X,Y` in
   \({\cal R}_8- {\cal I}\);
3. the bipartite incidence graph on the `2537` block nodes and the `2536`
   chosen separator nodes is connected, where each tile gives the two edges
   from its separator to its endpoint blocks; and
4. all central tile colours and all rank-nine colours induced at block nodes
   are pairwise distinct members of \({\cal R}_9^\circ\).

The induced block colours in item 4 are literal.  At a two-letter block with
internal colour `I`, an incident separator colour `X` contributes owner
\(I\cup X\).  At an internal singleton block, its two incident separator
colours `X,Y` contribute owner \(X\cup Y\).  Endpoint blocks contribute only
the owners on their used sides.

### Theorem 6.1 (grouped-tile equivalence)

The selected tiles expand to an occurrence-labelled prefix path with exactly
the certified low blocks, `2536` distinct rank-seven separators, `7400`
distinct rank-eight colours, and `7399` distinct rank-nine owners if and only
if conditions 1--4 hold and every derived owner in item 4 has rank nine.

#### Proof

There are `2537+2536=5073` block/separator nodes and every tile supplies two
incidence edges, so the selected incidence graph has `5072` edges.  Halfport
capacity gives block degree at most two, and every separator has degree two.
Under condition 3 the graph is therefore a tree of maximum degree two, hence
one alternating path; its two unused halfports are its endpoints.  Expanding a
tile gives the literal three-letter segment in (6.2), while expanding a
two-letter or singleton block gives exactly the owner rules in item 4.
The lower path has `5072+2328=7400` vertices.  If exactly `r` of its two
endpoint blocks are two-letter blocks, the two-letter blocks contribute
`2*2328-r` noncentral owners and the singleton blocks contribute
`209-(2-r)=207+r`; hence there are always `4863` noncentral owners and
`4863+2536=7399` owners in total.  Conditions 1--2 give the required low,
separator, and rank-eight palettes; condition 4 and the rank-nine requirement
give the upper palette.  This proves sufficiency.  Contracting every
separator and low block in any valid prefix recovers the same tiles and all
four conditions, proving necessity.
\(\square\)

This model displays the exact correlation left after Theorem 4.1.  Tile
selection is a grouped resource matching, its topology is graphic, and its
noncentral owner labels are quadratic at the block nodes.  Separate Hall for
ports, separate Hall for owner colours, and the near-completeness of the bare
block graph do not imply their simultaneous satisfaction.

## 7. Fixed-residual factor theorem for the shifted `s=1` tail

The adjacent-cut tail must now be completed before the prefix palette is
known.  Let its rank-eight palette be an arbitrary set

\[
 {\cal T}_8\subseteq{\cal X},\qquad |{\cal T}_8|=16910,
\]

and put

\[
 {\cal L}={\cal X}\setminus{\cal T}_8,\qquad |{\cal L}|=7400. \tag{7.1}
\]

Likewise, after the tail rank-nine palette and the two proposed seam owners
have been fixed, let \({\cal R}\subseteq{\cal Y}\) be the remaining
`7399` internal prefix owners.  Form the residual inclusion graph

\[
 G=M_{17}[{\cal L},{\cal R}].
\]

This definition is deliberately palette-parametric.  In particular, the
fixed coloured inventory from Section 6 is usable only if its `2328`
internal colours lie in \({\cal L}\); otherwise the inventory must be
reselected inside the residual palette.

### Theorem 7.1 (exact Hoffman factor cut)

The graph \(G\) has a spanning subgraph \(F\) satisfying

\[
 d_F(H)=2\quad(H\in{\cal R}),\qquad
 1\le d_F(U)\le2\quad(U\in{\cal L})                 \tag{7.2}
\]

if and only if, for every \(X\subseteq{\cal L}\) and
\(Y\subseteq{\cal R}\),

\[
 |X|\le2|Y|+e_G(X,{\cal R}\setminus Y),             \tag{7.3}
\]

and

\[
 2|Y|\le2|X|+e_G({\cal L}\setminus X,Y).            \tag{7.4}
\]

Every such \(F\) has exactly two degree-one vertices on the lower shore and
is the disjoint union of one lower-ended alternating path and zero or more
alternating cycles.  It is the required abstract prefix path exactly when
it is acyclic, equivalently connected.

#### Proof

Apply the bipartite \((g,f)\)-factor theorem to lower/upper degree intervals
\([2,2]\) on \({\cal R}\) and \([1,2]\) on \({\cal L}\).
Its two families of cut inequalities are precisely (7.3)--(7.4);
equivalently they are the Hoffman circulation cuts in the network

\[
 s\longrightarrow{\cal R}\longrightarrow{\cal L}\longrightarrow t
\]

with degree interval `[2,2]` on the first layer, edge capacity `[0,1]` on
the incidence layer, degree interval `[1,2]` on the last layer, and the
standard return arc.  The selected
degree sum is

\[
 \sum_{H\in{\cal R}}d_F(H)=2\cdot7399=14798,
\]

whereas \(2|{\cal L}|=14800\), so exactly two lower vertices have degree
one.  All remaining vertices have degree two, proving the component
description.  Such a graph is one spanning path exactly when it has no
cycle.  \(\square\)

For prescribed lower endpoints \(Z\in\binom{{\cal L}}2\), the exact
fixed-degree cut reduces to

\[
 2|X|-|X\cap Z|
   \le2|Y|+e_G(X,{\cal R}\setminus Y)
       \quad(X\subseteq{\cal L},\ Y\subseteq{\cal R}). \tag{7.5}
\]

The complementary instance of (7.5) supplies the reverse cut.  Thus
(7.5) is necessary and sufficient for a path-plus-cycles factor with
endpoints \(Z\).

Theorem 7.1 is polynomially checkable by max flow and returns a literal
violated pair \((X,Y)\) when the shifted tail palette is incompatible even
at the unlabelled level.  It does not hide topology: after (7.3)--(7.4)
pass, the exact Hamilton-path strengthening is

\[
 \sum_{e\in E(W)}z_e\le |W|-1
   \quad(\varnothing\ne W\subsetneq V(G)),           \tag{7.6}
\]

together with (7.2).  Since every feasible factor has
\(|V(G)|-1\) edges, (7.6) is equivalent to connectedness.

### Corollary 7.2 (first fail-closed residual tests)

For the fixed certified inventory and fixed residual palettes, all of the
following are necessary:

1. every certified internal colour belongs to \({\cal L}\);
2. every \(H\in{\cal R}\) has at least two lower facets in \({\cal L}\);
3. (7.3)--(7.4) hold;
4. there is a bijective occurrence-owner assignment for which the
   graphic-Rado inequalities (5.2) hold; for a proposed fixed assignment,
   failure excludes that assignment but not every other assignment; and
5. for every proposed separator \(B\), the list \(D_B\) in (4.5) has size at
   least two, while the residual owner lists
   \(\Omega_B^{\cal R}:=\Omega_B\cap{\cal R}\) satisfy (4.7) with
   \(\Omega_B^{\cal R}\) in place of \(\Omega_B\).  After block-local owners
   have been fixed, they too must be deleted from these lists.

Any failed row is an exact tail-prefix incompatibility certificate.  Passing
all five remains weaker than the grouped-tile system of Section 6 because
the owner assignment, degree-two row and macro topology must be common.

The unrestricted reserve of Theorem 4.1 and the block-local calibration
below range over the full Boolean levels.  They must not be imported into
an arbitrary `s=1` residual palette without rerunning these tests.

## 8. Full-universe block-local calibration

The occurrence restrictions of the certified inventory are nevertheless
jointly consistent before the tail palette is frozen.  For a two-letter
block \(b=(A,D)\), put \(I_b=A\cup D\).  A port occurrence \(A\) admits the
arm

\[
 I_b-H-U,\qquad
 H=I_b\cup\{y\},\quad U=H\setminus\{x\},\quad
 y\notin I_b,\quad x\in I_b\setminus A.             \tag{8.1}
\]

Then \(A\subseteq I_b\cap U\), so (8.1) carries the correct literal
occurrence.

### Theorem 8.1 (certified block-local macro bank)

For the frozen coloured inventory there are:

* `4656` arms (8.1), one for every halfport of every two-letter block, with
  all upper owners distinct, all cross lower endpoints distinct, and no
  cross endpoint equal to any of the `2328` internal colours; and
* `209` pairwise resource-disjoint singleton macros \(U-H-V\) with the
  singleton occurrence contained in \(U\cap V\), whose `418` lower endpoints
  and `209` upper owners avoid every resource in the core bank.

#### Proof

First match the two copies of every \(I_b\) to distinct rank-nine supersets
\(H\).  For this concrete matching, each halfport has the lower menu

\[
 D_{b,A}(H)=
 \{H\setminus\{x\}:x\in I_b\setminus A\}
   \setminus\{I_{b'}:b'\text{ a two-letter block}\}. \tag{8.2}
\]

The deterministic auditor finds matching rank `4656` in both stages and
then checks every containment, rank, union and resource identity literally.
Starting with that bank, it processes the `56` rank-four, `136` rank-two and
`17` rank-one singletons in this order and greedily chooses a fresh
Johnson edge whose rank-seven intersection contains the singleton.  All
`209` choices succeed and are replayed literally.  \(\square\)

Before opening endpoints, this bank has

\[
 2328+4656+2\cdot209=7402
\]

lower vertices and

\[
 4656+209=4865
\]

block-local upper edges.  Deleting one core arm at each of two distinct
terminal two-letter blocks leaves exactly `7400` lower vertices and `4863`
block-local upper edges.  The remaining `5072` exposed halfports must then
be paired by `2536` doubly-rainbow separator edges.  Adding them gives the
required `7399` upper owners.

This is a genuine simultaneous local certificate, but it is not a prefix:
the `2536`-edge coloured socket matching, the graphic subtour row, the
shifted tail palettes, and the literal seam are not supplied.  Its purpose
is to show that the first obstruction for the certified inventory is now
the separator/socket correlation, not a block-local occurrence conflict.

## 9. Exact surviving hypothesis

With a freely chosen lower split, the abstract endpoint connector and the
unlabelled palette split are closed by Theorem 2.1.  The shifted `s=1` tail
does not give a free split: after its palette is completed, the prefix must
first pass Theorem 7.1 and then the grouped-tile gate.  The literal
chronological seam is also not closed: (3.0) supplies only one automatic
endpoint incidence.  The certified coloured inventory does not yet supply
an occurrence-labelled Hamilton cycle.

> Complete the `s=1` tail palette; put its exact complement into (7.1);
> solve the grouped-tile system of Section 6 inside those residual palettes;
> and require the two literal seam-owner occurrences to pass the
> complementary-pair connector test (3.4).

Equivalently for the internal two-path factor, after fixing the owner
assignment prove (5.2), the Hoffman/degree rows, the graphic row, and the
block/tail factorization simultaneously; the physical completion still
additionally requires the seam test (3.4).  The near-complete bare block
graph addresses only local port adjacency and implies none of these common
rows.

## 10. Reproducibility and scope ledger

The fixed coloured inventory and its local graph are authenticated in
`MATH_AUDIT_K17_PREFIX_COLORED_INVENTORY_AND_MIDDLE_LEVELS_SPLIT_20260731.md`.
The deterministic block-local reconstruction is

```text
scratch/audit_r_k17_internal_ear_relaxations_20260731.py
scratch/r_k17_internal_ear_relaxations_20260731.audit.json
```

and reports matching ranks `4656/4656`, singleton rank `209`, core-ear
digest
`a36c02fa5ff66046bc17d95f7fc1c00b625ff2004e760df8e43a4694fd05e8c6`
and singleton digest
`98a6011b5f85fe68f45e22c36f0ad9e1a9e28f342b2f93fa7f9908b4736eb04b`.
The tiny independent Hoffman audit

```text
scratch/audit_r_k17_fixed_residual_factor_cuts_20260731.py
scratch/r_k17_fixed_residual_factor_cuts_20260731.audit.json
```

exhausts all `68` hosts at `n=2,3` and all `196` prescribed-endpoint
instances; its canonical payload is
`1ccf9e596fb2fa1dc3a0b6141e0ea5a50af03bf53ea1dddf5aec88ef9093ab59`.

No residence, rank-ten-and-higher shadow, compiler, or length-`24313` claim
is made here.
