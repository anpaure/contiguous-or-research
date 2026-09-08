# Repair-first ECO tree tilings, owner alignment, and private routing

Date: 2026-07-31  
Status: exact conditional all-dimension composition theorem, exact path
integrality theorem, and sharp abstract branching/router obstructions; no
all-dimension repaired carrier or compatible ECO selection is claimed

## 0. Verdict and quantifier order

Use the paper parameter `n`.  The canonical MMM factor has a component set
\(\mathcal V\) indexed by the plane trees with \(n\) edges.  The all-dimension
ECO supply theorem gives, for every Dyck parent \(D=1u0v\), a coherent
central-\(000\) incidence hexagon.  In one fixed coordinate rotation:

* the ECO component two-section is connected;
* the physical-port collision graph and the two forced-owner-colour
  collision graphs are the same directed path forest

  \[
             1p100v\longrightarrow 1p010v;                  \tag{0.1}
  \]

* hence one independent set removes all three kinds of local repetition.

None of these statements creates a joint decoration.  The exact raw
project-\(m=5\) census proves that all 648 minimal canonical ECO
Hamiltonizations are already port-disjoint and forced-face-disjoint, yet
every endpoint misses the same three upper and three lower period-three
turn colours.  Thus there is not even an upper transversal.

The obstruction is genuinely repaired, not merely avoided, at that first
dimension.  The frozen synchronized three-\(C10\) preparation at project
\(m=5\) has a two-component endpoint with complete \(84+84\) occurrence
palettes and one unique gap-forest matching.  Four of its five
fixed-rotation ECO atoms are all-six marked and pointwise owner-aligned;
each is a literal one-atom Hamilton merge preserving the same decoration.
This finite certificate is the positive base for (0.2), not an all-\(n\)
induction.

The load-bearing order is therefore

\[
 \boxed{
 \text{controlled repair/rethread}
 \longrightarrow \text{collision-free ECO tree tiling}
 \longrightarrow \text{owner-aligned residual Hall}
 \longrightarrow \text{private/laminar occurrence routing}.}       \tag{0.2}
\]

This note proves three reusable statements for that order.

1.  An ECO incidence hypertree is equivalent to a tiling of the edges of
    an ordinary component tree by the connected supports of its atoms.
    Binary atoms are one-edge tiles and genuine ternary atoms are
    two-adjacent-edge tiles.
2.  When the component tree is a path, the unconflicted tile-selection LP
    is exactly a unit-flow polytope and is integral.  At the first branching
    star the analogous matrix already has determinant two and a unique
    half-integral, nonintegral cover.
3.  On a repaired state, a component-faithful common cube of owner-aligned
    tiles with one fixed simultaneous private occurrence realization gives
    a literal component-spanning fixed-decoration execution.  Deletion
    resilience is a separate weighted statement: an atom meeting \(r\)
    component blocks must have private kill cost at least \(r-1\) on the
    bare selected-hypertree backbone.

The first two statements isolate the smallest exact integral correlation
which remains after coherent abundance.  The third composes it with the
already proved owner and router theorems without conflating fixed execution
with adversarial deletion resilience.

## 1. Prepared factors and literal ECO data

Let \(F'\) be the endpoint of a controlled repair packet, and let
\(\mathcal V\) be its physical factor components.  Fix one occurrence-
labelled joint decoration \(\mathscr D=(I,M)\):

* \(I\) is the chosen upper-turn transversal;
* \(\Gamma_I\) is the occurrence-labelled cyclic-gap versus lower-colour
  multigraph; and
* \(M\) is a perfect matching of \(\Gamma_I\).

On the leaf-peelable face, \(\Gamma_I\) is a forest.  Parallel occurrence
edges count as a two-cycle, so a forest has at most one perfect matching.

An ECO atom is written

\[
 t=(H;a,b,c;d,e),                                      \tag{1.1}
\]

with six ports

\[
 \begin{array}{lll}
 L_a=H+a,&L_b=H+b,&L_c=H+c,\\
 U_{ab}=H+a+b,&U_{bc}=H+b+c,&U_{ca}=H+c+a.
 \end{array}                                           \tag{1.2}
\]

The canonical old and new local matchings are

\[
 \begin{aligned}
 E_0(t)&=\{L_aU_{ca},L_bU_{ab},L_cU_{bc}\},\\
 E_1(t)&=\{L_aU_{ab},L_bU_{bc},L_cU_{ca}\}.
 \end{aligned}                                         \tag{1.3}
\]

All three nonhexagon edges at the \(L\)-ports insert the common label
\(d\), and all three nonhexagon edges at the \(U\)-ports delete the common
label \(e\).  This is the all-six coherence condition.

The shore convention is important.  The selected **upper-turn**
occurrences are the physical \(L\)-vertices, whereas the forced
**lower-turn** occurrences lie at the physical \(U\)-vertices.  Thus an
atom is selected by the upper transversal only if

\[
                         L_a,L_b,L_c\in I.             \tag{1.4}
\]

Let \(g_{ab},g_{bc},g_{ca}\) be the literal \(I\)-gaps containing the
specified occurrences \(U_{ab},U_{bc},U_{ca}\).  The three forced
occurrence edges of \(\Gamma_I\) are

\[
 \begin{aligned}
 f_{ab}(t)&=(g_{ab},U_{ab};H-e+b),\\
 f_{bc}(t)&=(g_{bc},U_{bc};H-e+c),\\
 f_{ca}(t)&=(g_{ca},U_{ca};H-e+a),
 \end{aligned}                                         \tag{1.5}
\]

and put \(F_t=\{f_{ab}(t),f_{bc}(t),f_{ca}(t)\}\).
The occurrence label in (1.5) is retained even when two edges have the same
gap and colour.

By the leaf-forest owner theorem, the exact local owner predicate is

\[
 \boxed{\quad L_a,L_b,L_c\in I\quad\text{and}\quad F_t\subseteq M.\quad}
                                                               \tag{1.6}
\]

Off the forest face, \(F_t\subseteq M\) is replaced by the exact
vertex-disjoint alternating-cycle packing for the literal union of the
forced edges.  Merely making their colours distinct is not enough.

Let \(S_t\subseteq\mathcal V\) be the set of distinct components containing
the three old edges \(E_0(t)\), and write

\[
                            r_t=|S_t|.                 \tag{1.7}
\]

Only atoms with \(r_t\in\{2,3\}\) are used as merge tiles.  An \(r_t=1\)
atom is a neutral rethread or a split on the current face and belongs in
the preliminary repair packet, not in the later component tree.

## 2. The ordinary-tree tiling equivalence

Let \(A\) be an ordinary tree on vertex set \(\mathcal V\).  Call an atom
\(t\) **\(A\)-local** when the induced subtree \(A[S_t]\) is connected, and
put

\[
                         Q_t=E(A[S_t]).                \tag{2.1}
\]

Then \(|Q_t|=r_t-1\).  A family \(\mathcal T\) is an **\(A\)-tiling** when

\[
                  E(A)=\mathop{\dot\bigcup}_{t\in\mathcal T}Q_t.    \tag{2.2}
\]

Thus a binary atom tiles one edge of \(A\), while a ternary atom tiles the
two adjacent edges of the three-vertex subtree \(A[S_t]\).

For a family \(\mathcal T\), let \(B(\mathcal V,\mathcal T)\) be the
bipartite incidence graph with an edge \(vt\) iff \(v\in S_t\).

### Theorem 2.1 (tree-tiling equivalence)

The following are equivalent.

1.  \(B(\mathcal V,\mathcal T)\) is a spanning tree.
2.  There is an ordinary tree \(A\) on \(\mathcal V\) such that
    \(\mathcal T\) is an \(A\)-tiling.

Moreover, in direction 1 to 2 one may choose an arbitrary spanning tree on
each support \(S_t\); the union of those labelled local trees is \(A\).

#### Proof

Assume (2).  For every edge \(xy\in E(A)\), (2.2) supplies a unique atom
\(t\) with \(xy\in Q_t\), so \(x-t-y\) is a path in the incidence graph.
Since \(A\) is connected, the incidence graph is connected.  Its number of
incidence edges is

\[
 \sum_{t\in\mathcal T}r_t
   =\sum_t(|Q_t|+1)
   =|\mathcal V|-1+|\mathcal T|,                       \tag{2.3}
\]

which is one less than its \(|\mathcal V|+|\mathcal T|\) vertices.  Hence
it is a tree.

Conversely suppose the incidence graph is a tree.  For each atom \(t\),
choose any ordinary tree \(Q_t\) on the vertex set \(S_t\).  Replace the
atom node and its incident star by \(Q_t\).  Connectivity is preserved, and

\[
 \sum_t|Q_t|=\sum_t(r_t-1)=|\mathcal V|-1,             \tag{2.4}
\]

the last equality following from the edge count of the incidence tree.
The union is therefore a connected multigraph with \(|\mathcal V|-1\)
edges, hence an ordinary tree \(A\).  It has neither a repeated edge nor an
extra edge inside any \(S_t\), since either would make a cycle.  Equivalently,
two distinct supports cannot share two component vertices: such vertices
and the two atom nodes would already form a four-cycle in the incidence
tree.  Therefore
\(Q_t=A[S_t]\), the \(Q_t\)'s partition \(E(A)\), and (2) follows.
\(\square\)

This theorem is combinatorial.  It does not say that the physical ECO
toggles are simultaneously legal or that their literal component change
follows the incidence tree.  Those are the component-faithful cube rows in
Section 5.

### Corollary 2.2 (exact tiling master)

For a fixed component tree \(A\) and a prefiltered bank \(\mathcal B\) of
\(A\)-local atoms, the incidence-tree selection equations are exactly

\[
       \sum_{t\in\mathcal B:e\in Q_t}x_t=1
       \qquad(e\in E(A)),\qquad x_t\in\{0,1\}.          \tag{2.5}
\]

Local collision edges \(tt'\) add

\[
                              x_t+x_{t'}\le1.           \tag{2.6}
\]

Owner masks set \(x_t=0\) unless (1.6) holds.  Physical-cube and route
conflicts are separate rows; neither (2.5) nor (2.6) encodes them.

## 3. Exact path integrality and the first branching obstruction

Assume every atom has arity at most three.

### Theorem 3.1 (path tilings are unit flows)

If \(A\) is a path, the relaxation of (2.5) to \(x_t\ge0\) is integral.
More precisely, index the edges of \(A\) by \(1,\ldots,s\).  Every tile is
an interval \([a,b]\) of length one or two.  Map that tile to the directed
arc

\[
                              a-1\longrightarrow b                  \tag{3.1}
\]

of the acyclic graph on \(0,1,\ldots,s\).  Then (2.5) is exactly the
unit-flow polytope from \(0\) to \(s\).

#### Proof

Let

\[
                  c_i=\sum_{t:a_t\le i\le b_t}x_t.      \tag{3.2}
\]

The tiling equations say \(c_i=1\) for every \(i\).  At an internal node
\(j\), the identity

\[
     c_{j+1}-c_j
       =\sum_{t:a_t=j+1}x_t-\sum_{t:b_t=j}x_t           \tag{3.3}
\]

is precisely flow conservation.  At the two boundary nodes, \(c_1=1\)
and \(c_s=1\) say that the total source outflow and sink inflow are one.
Conversely these flow equations imply all the \(c_i\)'s equal one.

Every nonnegative unit flow in an acyclic directed graph is a convex
combination of directed source--sink paths.  Such a path is exactly a
partition of \(1,\ldots,s\) into the chosen length-one and length-two
tiles.  Hence every vertex of the relaxation is integral. \(\square\)

Deletion of atoms by owner, port, deep-shadow or private-route masks merely
deletes arcs and preserves this conclusion.  Adding arbitrary pairwise
conflict inequalities does not: the path theorem applies to a bank which
has already been made mutually compatible, or to conflicts separately
proved to be represented by the same flow network.

### Proposition 3.2 (the determinant-two three-arm obstruction)

The path conclusion is false at the first branching tree.  Let \(A\) be
the three-edge star with edges \(e_1,e_2,e_3\), and suppose the only tiles
are three ternary tiles

\[
       Q_{12}=\{e_1,e_2\},\quad
       Q_{23}=\{e_2,e_3\},\quad
       Q_{31}=\{e_3,e_1\}.                              \tag{3.4}
\]

Then the fractional tiling equations have the unique solution

\[
                         x_{12}=x_{23}=x_{31}=\tfrac12, \tag{3.5}
\]

but there is no integral tiling.

#### Proof

The coefficient matrix is

\[
       \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},           \tag{3.6}
\]

whose determinant is two.  Subtracting pairs of the three equations gives
(3.5).  Integrally, one tile leaves one arm uncovered and two tiles cover
one arm twice. \(\square\)

Equivalently, each candidate hyperedge consists of the centre and two
leaves.  Any one misses the third leaf, while any two have a Berge cycle
through their two common component vertices.  Thus connected component
two-section, cap-two degrees, and a feasible uniform fractional point do
not imply an integral incidence hypertree.  This is an abstract
component-support obstruction, not a claim that this exact three-arm
fixture occurs in the canonical ECO catalogue.

## 4. Using the common collision path forest

For the fixed-rotation canonical ECO bank, let \(\mathcal P\) be the path
forest (0.1).  On each nontrivial path choose one of its two alternating
parity classes, and retain that class; isolated atoms are always retained.
The result is independent in the physical-port and both forced-owner-
colour collision graphs.

The following gives a quantitative, deliberately binary, way in which the
path forest can supply a component tree after a repair.

### Proposition 4.1 (random phase binary-shadow criterion)

Fix an ordinary component tree \(A\).  For each \(e\in E(A)\), suppose
there are \(\mu_e\) certified binary ECO merge atoms with support equal to
the endpoints of \(e\), lying on \(\mu_e\) distinct paths of \(\mathcal P\).
Choose one such witness on each of those paths.  Assume every witness is a
literal binary merge on the eventual common cube; this is not inferred
from its support alone.

If

\[
                         \sum_{e\in E(A)}2^{-\mu_e}<1,              \tag{4.1}
\]

then there is a parity choice on the paths of \(\mathcal P\) which retains
at least one witness for every edge of \(A\).  Selecting one retained
witness per edge gives a collision-free abstract \(A\)-tiling.

#### Proof

Choose the two parities of every collision path independently and
uniformly.  For a fixed edge \(e\), its chosen witnesses lie on distinct
paths.  The probability that every one lies in the discarded parity is at
most \(2^{-\mu_e}\); it is zero if one path already offers witnesses of
both parities.  By the union bound, (4.1) gives positive probability that
no edge is uncovered.  Binary atoms cannot represent two different edges
of the simple tree \(A\), so choosing one retained atom per edge is an
\(A\)-tiling. \(\square\)

In particular, the uniform bound

\[
          \mu_e\ge \left\lceil\log_2(2|E(A)|)\right\rceil
          \quad\text{for every }e                         \tag{4.2}
\]

suffices.  Proposition 4.1 proves only collision-free static selection.
Owner alignment, component faithfulness, global cube compatibility and
routing are still required.  The all-dimension ECO supply theorem gives at
least one shadowing atom per standard tree edge, not the multiplicity or
binary-support hypothesis of (4.1).

## 5. Component-faithful private ECO collars

An \(A\)-tiling \(\mathcal T\) is called a **prepared private coherent
collar** on \((F',\mathscr D)\) when all of the following hold.

1. **One literal common cube.**  For every
   \(\mathcal U\subseteq\mathcal T\), the symmetric difference with the
   declared \(E_0(t)\triangle E_1(t)\) is a literal degree-two factor, is
   independent of toggle order, has no undeclared edge/resource conflict,
   and every pending atom remains available.
2. **Component faithfulness.**  In every subset state \(\mathcal U\), the
   physical component partition is exactly the component partition of the
   incidence subforest \(B(\mathcal V,\mathcal U)\).  Equivalently, a
   pending atom touching \(r_t\) incidence blocks merges those \(r_t\)
   physical blocks and splits none.
3. **Owner alignment.**  Every atom satisfies the literal occurrence test
   (1.6) in the same \((I,M)\).
4. **Protected state.**  The same gap-forest, trace, reachability,
   residence, deeper-shadow, socket/voltage and compiler guards required by
   the application survive every subset state.
5. **One simultaneous occurrence realization.**  Each atom has a named
   atomic occurrence transfer.  These transfers have pairwise internally
   vertex-disjoint private routes from distinct protected sources to
   distinct protected sinks, and there is one subset-closed simultaneous
   realization: restricting it to any \(\mathcal U\) executes exactly the
   atoms of \(\mathcal U\).

The protected source and sink terminals in item 5 are not deletable router
vertices.  “Private” includes every internal vertex on which the declared
atomic availability depends; an unrecorded shared bottleneck violates the
hypothesis.

### Theorem 5.1 (repair-first private ECO composition)

If \(\mathcal T\) is a prepared private coherent collar, toggling all atoms
of \(\mathcal T\) gives one physical component, preserves the joint
decoration \(\mathscr D\), and passes the forced-port Hall row.  Every order
of the atoms is executable on this prepared cube.

#### Proof

The tree-tiling theorem makes the abstract incidence graph a tree.  Suppose
a pending atom had two incident component vertices already joined by
earlier atoms.  The earlier incidence path between them together with the
two incidences through the pending atom would be a cycle.  Thus its
\(r_t\) incident vertices lie in distinct current incidence blocks.
Component faithfulness makes the literal toggle merge precisely those
blocks.  Induction in any order ends in one component.

For Hall, every selected upper-turn port lies in the same \(I\), and every
forced literal lower occurrence edge belongs to the same matching \(M\).
Hence the union of all forced ports is already part of \(\mathscr D\); no
new residual matching is required on the forest face.  Coherence transports
that fixed decoration across every atom.  Items 1, 4 and 5 execute the
literal operations and preserve the remaining state. \(\square\)

One private named route per atom is enough for this fixed simultaneous
execution, including a genuine ternary atom.  It is **not** enough for the
stronger adversarial-deletion router inequality, treated next.

## 6. Exact weighted deletion robustness

Fix the bare selected incidence-tree backbone \(\mathcal T\).  Give each
atom a full private internal failure bank \(R_t\), with the banks pairwise
disjoint.  Router deletion sets \(Y\) range only over internal, unprotected
vertices.  Availability of atom \(t\) after deletion depends only on
\(Y\cap R_t\).  Every relevant deletable router vertex belongs to exactly
one bank; vertices outside the banks, if retained in the ambient notation,
are declared irrelevant to all atomic availabilities.  Let
\(\mathcal D(Y)\) be the dead atoms and put

\[
                              w_t=r_t-1.                         \tag{6.1}
\]

### Lemma 6.1 (exact atomic damage)

After deleting the dead atom nodes from the incidence tree,

\[
                c_Y-1=\sum_{t\in\mathcal D(Y)}(r_t-1)
                     =\sum_{t\in\mathcal D(Y)}w_t.               \tag{6.2}
\]

#### Proof

Removing a degree-\(r_t\) atom node from a tree increases the number of
component-containing pieces by \(r_t-1\).  Atom nodes are pairwise
nonadjacent, so the increases add.  Component faithfulness identifies the
incidence pieces with the physical backbone pieces. \(\square\)

Let

\[
 \lambda_t=\min\{|Z|:Z\subseteq R_t\text{ and }Z\text{ kills }t\}. \tag{6.3}
\]

Set \(\lambda_t=\infty\) if no internal set kills \(t\).

If the atomic transfer is available whenever any one member of a private
source--sink route family survives, every killing set must hit every route.
Thus \(w_t\) internally vertex-disjoint protected-terminal routes certify
\(\lambda_t\ge w_t\).  Equality with an ordinary Menger cut requires the
stronger converse that killing all such routes kills the atom.  Either
interpretation is invalid if a source or sink can itself be deleted, or if
complete execution needs several simultaneous routes.

### Theorem 6.2 (private weighted-router criterion)

On the bare selected-hypertree backbone with the complete disjoint-bank
hypotheses above,

\[
             c_Y\le |Y|+1\quad\text{for every }Y                 \tag{6.4}
\]

holds if and only if

\[
                              \lambda_t\ge w_t
                 \qquad(t\in\mathcal T).                         \tag{6.5}
\]

#### Proof

If (6.5) holds, disjointness of the complete banks gives

\[
 \sum_{t\in\mathcal D(Y)}w_t
   \le\sum_{t\in\mathcal D(Y)}|Y\cap R_t|
   \le |Y|.
\]

Combine with (6.2).

Conversely, if \(\lambda_t<w_t\), choose a minimum killing set
\(Y\subseteq R_t\).  Completeness and disjointness of the banks leave every
other atom live, so (6.2) gives
\(c_Y-1=w_t>|Y|\), contradicting (6.4). \(\square\)

For a binary atom, \(w_t=1\) and one private route is enough.  A ternary
atom has \(w_t=2\); a single internal articulation kills it at cost one and
violates (6.4).  Two protected-terminal routes, a literal factorization
into two independently survivable binary merges, or a proved laminar
two-unit charge are sufficient mechanisms.  They are not exhaustive in a
larger catalogue: extra unselected atoms may reconnect the branches, and
shared global routing may satisfy (6.4) without decomposing into private
banks.  The necessity in Theorem 6.2 is scoped exactly to the bare selected
backbone.

## 7. Exact repair-transport signature

Suppose a preliminary packet carries \(F\) to \(F'\), and one wants to
transport a named ECO family rather than recompute it at \(F'\).  The
following data are sufficient and, component by component, exactly what
the proof of Theorem 5.1 reads.

For every atom preserve:

1. its six literal port occurrences;
2. the old local matching phase \(E_0(t)\), every external factor neighbour,
   and the common labels \((d,e)\);
3. the new local incidences \(E_1(t)\) and the direction of the toggle;
4. its component support \(S_t\), the tree tile \(Q_t\), and the physical
   component partition on every subset;
5. the selected \(I\)-occurrences at the \(L\)-ports, the literal gap
   identities at the \(U\)-ports, and the owner edges \(F_t\subseteq M\);
6. the common-cube conflict state and every protected gap, trace,
   reachability, residence, deeper-shadow, socket/voltage and compiler
   guard; and
7. the named atomic occurrence transfer, its complete private bank, and
   its protected source and sink.

### Proposition 7.1 (transport)

If the preliminary packet preserves items 1--7 for a prepared private ECO
collar, the same collar satisfies Theorem 5.1 on \(F'\).  If it also
preserves the complete banks and their kill numbers, Theorem 6.2 transfers.

#### Proof

Items 1--3 preserve the literal coherent atom.  Item 4 preserves the
tree-tiling and component-faithful cube arguments.  Item 5 preserves the
fixed-decoration Hall proof.  Items 6--7 preserve the remaining execution
and routing hypotheses.  These are exactly the hypotheses used in Sections
5--6. \(\square\)

Keeping only the six visible vertices is insufficient.  A remote rethread
may change their external neighbours, old matching phase, bracketing gaps,
component interleaving or route bottlenecks without changing the six masks.
In the general repair-first architecture the safer procedure is to finish
the repair, then recompute the atoms, owners and routes on its endpoint.

## 8. Finite evidence and the raw project-\(m=5\) obstruction

The frozen fixed-rotation ECO audit gives the following **static**
incidence-tree/final-Hamilton witnesses:

\[
\begin{array}{c|r|r|r|r}
n&|\mathcal V|&|\mathcal T|&\#\{r_t=2\}&\#\{r_t=3\}\\ \hline
3&2&1&1&0\\
4&3&2&2&0\\
5&6&3&1&2\\
6&14&8&3&5\\
7&34&19&5&14.
\end{array}                                                   \tag{8.1}
\]

The arities follow from

\[
 \#\{r_t=3\}=|\mathcal V|-1-|\mathcal T|,
 \qquad
 \#\{r_t=2\}=2|\mathcal T|-(|\mathcal V|-1).                  \tag{8.2}
\]

The audit's union-find acceptance proves incidence acyclicity/rank, its
port test proves physical vertex-disjointness, and its final replay proves
that the all-at-once symmetric difference is Hamilton.  It does **not**
replay every subset or order and therefore does not authenticate the full
component-faithful cube of Section 5.

The separate raw project-\(m=5\) theorem is decisive for quantifier order.
At paper parameter \(n=4\), all 648 ordered minimal ECO Hamiltonizations
(324 endpoints) have disjoint physical ports and disjoint forced owner
faces, but every endpoint has only 81 of 84 turn colours on each shore,
missing

\[
 \{219,365,438\}\quad\text{above},\qquad
 \{73,146,292\}\quad\text{below}.                              \tag{8.3}
\]

Thus neither collision independence nor a static topology witness creates
\(I\).  The owner predicate (1.6) cannot even be posed until the palette is
repaired.  Project \(m=4\) is positive, so this is the smallest raw
canonical minimal-ECO failure.  It does not obstruct the synchronized
repair-first route.

That surviving route is already exact at the same finite dimension.  The
synchronized three-\(C10\) endpoint has two components of sizes 120 and
132, a complete occurrence-labelled decoration, a forest gap graph with a
unique matching, and a trace forest.  All five fixed-rotation atoms survive
the repair support and individually Hamiltonize; precisely

\[
             D\in\{110100,110010,101100,101010\}                 \tag{8.4}
\]

are all-six marked and owner-aligned.  Toggling any of these four preserves
the accepting decoration.  Thus the central physical joining and owner-Hall
conclusion of Theorem 5.1 has an unconditional one-atom realization at
project \(m=5\); the finite certificate does not claim all of item 4's
downstream residence/deep/compiler guards.  The nonstandard witness
\(D=110100\) is outside the old two-standard-glue cube, so the result is not
just a relabelling of the earlier standard merge.  What remains conditional
is promotion to a uniform repair-exported hypertree and occurrence-channel
theorem.

## 9. Exact proved/open boundary

Proved here:

1. the ordinary-tree tiling equivalence for binary/ternary ECO supports;
2. the exact binary master (2.5) and its separation from collision, owner,
   physical and route rows;
3. unit-flow integrality for a path component tree;
4. the determinant-two three-arm obstruction at the first branch;
5. the random-phase collision-path binary-shadow criterion;
6. the repair-first private owner-aligned ECO composition theorem;
7. the exact weighted private-bank criterion for deletion resilience; and
8. the full repair-transport signature.

Imported, with exact scope:

1. fixed-rotation coherent ECO two-section connectivity and the common
   physical/owner collision path forest;
2. leaf-forest owner alignment;
3. private-tree Hall/router closure; and
4. the raw project-\(m=5\) palette counterexample.

Finite positive calibration:

1. the synchronized repaired project-\(m=5\) endpoint has four literal
   owner-aligned fixed-rotation ECO Hamilton merges preserving its unique
   decoration.

Still open:

1. an all-dimension controlled repair whose endpoint has complete palettes
   and the required deeper protected state;
2. after that repair, a collision-free, physical component-faithful ECO
   tree tiling;
3. one joint \((I,M)\) satisfying every literal owner edge (1.5);
4. a simultaneous private or correctly weighted/laminar occurrence
   realization for the same atoms;
5. residence and all-depth shadow preservation through the whole cube;
6. primitive-voltage/socket closure; and
7. the common-\(Q\) compiler.

The strongest present selection target is therefore not another coherent-
edge abundance theorem.  It is a repair endpoint on which the exact tiling
system (2.5), the owner predicate (1.6), component faithfulness and the
occurrence routes have one common integral solution.  On a component path,
the bare tiling row is already integral; on a branching tree, Proposition
3.2 shows why a genuinely correlated integral choice can remain.

## 10. Dependencies

* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`
* `MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`
* `MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md`
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`
* `MATH_THEOREM_CATALAN_ROUTER_TREE_SUM_AND_PRIVATE_OCCURRENCE_COMPOSITION_20260731.md`
* `MATH_THEOREM_K_COHERENT_EDGE_SUPPLY_FORCED_PORT_HALL_ROUTER_CATALOGUE_20260731.md`
