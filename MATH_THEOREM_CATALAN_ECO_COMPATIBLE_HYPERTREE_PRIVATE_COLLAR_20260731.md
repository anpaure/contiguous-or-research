# Compatible ECO hypertrees and the rank-balanced private collar

Date: 2026-07-31  
Status: exact topology and prepared-selection theorems; exact sharp abstract
obstructions to two-section connectivity and edgewise SDR; no all-`n`
compatible ECO hypertree, decoration, router, residence, or compiler theorem

## 0. Rebased verdict

The coherent-ECO supply theorem removes the raw component-connectivity
obstruction: every standard MMM pull is shadowed by a coherent ECO hexagon,
so the unfiltered component two-section is connected in every dimension.
That does **not** yet give a simultaneous gluing family.

For a set `S` of physically compatible atoms, let `H_t` be the set of old
factor components touched by atom `t`, and form the bipartite incidence graph

\[
 \mathcal I(S)\qquad\text{on}\qquad V_{\rm comp}\sqcup S,
 \qquad v\sim t\Longleftrightarrow v\in H_t.                      \tag{0.1}
\]

On the prefix-faithful merge face, `S` is a strict simultaneous component
hypertree exactly when `I(S)` is a tree.  Equivalently,

\[
 \bigcup_{t\in S}H_t=V_{\rm comp},\qquad
 \mathcal I(S)\text{ is connected},\qquad
 \sum_{t\in S}(|H_t|-1)=|V_{\rm comp}|-1.                        \tag{0.2}
\]

The correct fixed-pull-tree version assigns each selected atom the whole
subtree induced by `H_t` and partitions the pull-tree edges by these
subtrees.  Assigning one distinct atom to each pull edge is exact only on
the binary face `|H_t|=2`.  On that face, and only after physical conflicts
have genuinely been prepared into partition blocks, the problem is ordinary
graphic-matroid/partition-matroid intersection, or equivalently a fixed-tree
SDR.

Two exact small obstructions locate the boundary.

* The hypergraph `{123,124}` has connected two-section but no spanning
  incidence hypertree.
* On the pull path `12,23`, two distinct atoms both supported on `123` give
  an edgewise SDR, yet their incidence graph is `K_(3,2)` and the second
  atom cannot be certified as another strict merge after the first.

There is a second new cost.  An atom of component gain

\[
                            r_t=|H_t|-1                            \tag{0.3}
\]

causes `r_t` units of component damage when it dies in an incidence tree.
A binary private path pays for a binary atom, but a ternary ECO atom needs a
private failure cut of size at least two, or an exact decomposition into two
independently protected effective bridges.  One node-private route is not a
rank-two router certificate.

Thus the all-`n` target after coherent ECO supply is:

> choose one physically compatible incidence hypertree whose same atoms are
> owner-aligned matching splices and whose router failure capacities dominate
> their component gains.

This is the simultaneous **private coherent ECO collar** gate.

## 1. Physical ECO atoms and strict component gain

Let `F` be a two-factor with component set `V`.  A physical atom `t` is an
alternating incidence hexagon.  Its three old factor edges are pairwise
vertex-disjoint.  Let \(H_t\subseteq V\) be the set of factor components
containing those old edges.

Two atoms are **physically compatible** when their six-vertex port sets are
disjoint and their frozen signatures superpose on the prepared Boolean
cube.  Port disjointness makes their symmetric-difference operations
commute, but the prefix-faithful component, decoration, gap and boundary
rows are still explicit hypotheses.

Call `t` a **strict hypermerge** on `H_t` when the following prefix statement
holds: whenever the current factor components containing the members of
`H_t` are pairwise distinct, toggling `t` replaces exactly those
`|H_t|` components by one component and changes no other component.

When the three old edges lie in three distinct factor components, the atom
is automatically a strict ternary hypermerge.  Removing one edge from each
cycle makes three paths, and the three new hexagon edges concatenate those
paths into one cycle.  If only two old components occur, one component
contributes two removed edges; binary merge faithfulness then depends on the
literal path pairing and must be audited on the whole prepared prefix cube.
An atom with `|H_t|=1` is a rethread or split candidate, not a hypermerge
edge merely because it is coherent.

## 2. Exact incidence-hypertree theorem

### Theorem 2.1 (strict simultaneous hypermerge topology)

Let `S` be a physically compatible set of strict hypermerges.  Assume their
component signatures are prefix-faithful.  The following are equivalent.

1. In some order, every atom `t` sees the current components indexed by
   `H_t` pairwise distinct, merges all of them, and the final factor is
   connected.
2. The same holds in every order.
3. The incidence graph `I(S)` is a tree.
4. Equation (0.2) holds.

#### Proof

Assume `I(S)` is a tree and expose the atoms in any order.  If two vertices
`u,v in H_t` had already been joined by earlier atoms, the earlier incidence
edges would contain a path from `u` to `v` avoiding the atom vertex `t`.
Adding the two incidence edges `u-t,t-v` would create a cycle in `I(S)`, a
contradiction.  Thus the members of `H_t` lie in pairwise distinct current
components.  Strict hypermerge faithfulness reduces their number by
`|H_t|-1`.  At the end, incidence connectivity makes the factor connected.
This proves Items 3 implies 2 implies 1.

Conversely, an order as in Item 1 reduces the component count by
`|H_t|-1` at atom `t`.  Since it starts with `|V|` components and ends with
one,

\[
                       \sum_{t\in S}(|H_t|-1)=|V|-1.                \tag{2.1}
\]

The final component can join two original components only through a chain
of selected atoms, so `I(S)` is connected.  It has

\[
 |V|+|S|\text{ vertices},\qquad
 \sum_t|H_t|=|V|+|S|-1\text{ edges}.
\]

A connected graph with one fewer edge than vertices is a tree.  This proves
Item 1 implies 3.  Finally, connectivity plus the edge count in (0.2) is
equivalent to being a tree, proving Items 3 and 4 equivalent.  \(\square\)

The theorem deliberately distinguishes a hypermerge from a binary merge.
For a ternary atom, one physical toggle pays two units of component rank.

### Corollary 2.2 (hyperleaf order)

Root `I(S)` at any component vertex.  Every atom vertex then has one parent
component and `|H_t|-1` child component branches.  Processing atom vertices
away from the root is a constructive hyperleaf-extension order; reversing
the order is a literal incidence-leaf peeling.  A ternary atom may attach
two child branches at once.

If each atom also has an exact private matching splice and its nonprivate
gap attachment is an injective copy of any tree on `H_t`, then the union gap
attachment is a forest.  If all forced edges lie in the transported unique
matching, forced-port Hall is automatic by owner alignment.

#### Proof

Replace every atom vertex of the incidence tree by its aligned component
tree on `H_t`.  This is a sequence of contractions/expansions of a tree and
therefore remains a tree.  Rooted private gap trees may then be peeled away.
The exact matching-splice and owner conclusions are Lemma 1.1 of
`MATH_THEOREM_CATALAN_PRIVATE_COHERENT_COLLAR_LEAF_EXTENSION_20260731.md`.
\(\square\)

## 3. A fixed pull-tree and the exact-cover formulation

Fix a standard MMM pull-tree `R` on `V`.  A hypermerge atom `t` is
**`R`-supported** when the induced graph `R[H_t]` is connected.  Put

\[
                         Q_t=E(R[H_t]).                            \tag{3.1}
\]

Then `|Q_t|=|H_t|-1`.  An `R`-supported family is an **exact pull cover**
when

\[
                  \{Q_t:t\in S\}\text{ partitions }E(R).         \tag{3.2}
\]

### Theorem 3.1 (fixed-tree hyper-SDR)

Every physically compatible exact pull cover is an incidence hypertree.
Conversely, every incidence hypertree supports *some* component tree
obtained by replacing each atom vertex with an arbitrary tree on `H_t`, but
it need not support a prescribed MMM pull-tree.

#### Proof

Under (3.2), the union of the connected subtrees `R[H_t]` is `R`, so the
incidence graph is connected.  Moreover

\[
 \sum_t(|H_t|-1)=\sum_t|Q_t|=|E(R)|=|V|-1.
\]

Theorem 2.1 applies.  Conversely, replace every atom vertex in the incidence
tree by a star, or any tree, on its neighbours.  These local replacements
preserve connectedness and the total edge count `|V|-1`, hence give a
component tree.  No reason forces that tree to equal a previously chosen
`R`.  \(\square\)

For a prepared finite catalogue, (3.2) is the exact integral system

\[
              \sum_{t:e\in Q_t}x_t=1\quad(e\in E(R)),qquad
              x_t\in\{0,1\},                                      \tag{3.3}
\]

together with the physical compatibility rows and the private coherent
collar filters.  A ternary atom contributes one all-or-none column with two
ones.  Splitting that column into two independently selectable labels would
split one physical toggle and is unsound.

### Theorem 3.2 (ordinary graphic--partition face)

Restrict to the binary face `|H_t|=2`, so every `Q_t` is one pull-tree edge.
Suppose, additionally, that physical compatibility has been prepared as a
partition matroid `M_P` on the label representations: at most one
representation may be selected from each physical resource block, and
labels in distinct blocks are truly compatible.

Let `M_G` be the parallel extension of the graphic matroid of `R`: every
representation of pull edge `e` is parallel to `e`.  Then a compatible
fixed-pull-tree SDR exists if and only if

\[
       r_G(X)+r_P(\Omega-X)\ge |V|-1
                  \quad\text{for every }X\subseteq\Omega.          \tag{3.4}
\]

Equivalently, if `B(J)` is the set of physical resource blocks containing a
representation of at least one edge in \(J\subseteq E(R)\), then

\[
                            |B(J)|\ge |J|
                    \qquad(J\subseteq E(R)).                       \tag{3.5}
\]

#### Proof

Edmonds' matroid-intersection theorem gives (3.4).  A common independent set
of size `|V|-1` projects to a graphic basis of the tree `R`.  Since every
edge of a tree is a coloop in its own graphic matroid, the set contains
exactly one representation of every pull edge.  Partition independence
makes their physical blocks distinct.  Conversely, such an SDR is a common
basis.  Hall's theorem on the bipartite graph from pull edges to physical
blocks gives (3.5).  \(\square\)

The hypotheses identify the polynomial integral face; they are not true of
the unfiltered ECO catalogue for free.

1. For ternary atoms, the all-or-none columns in (3.3) are grouped graphic
   bundles rather than elements of `M_G`.
2. Literal port-disjointness of arbitrary atoms is a set-packing system,
   not generally a partition matroid.  For example, atoms with port sets
   `{p,q}`, `{p}`, `{q}` have independent sets `{first}` and
   `{second,third}` and violate matroid exchange.

Child-owned preallocation repairs Item 2: alternatives for one child form
one partition block and banks of different children are disjoint.  It does
not split a ternary atom's rank-two component effect.

## 4. Why two-section connectivity and edgewise SDR are insufficient

### Proposition 4.1 (minimum two-section obstruction)

On four component vertices take only the two supports

\[
                           H_a=\{1,2,3\},\qquad
                           H_b=\{1,2,4\}.                          \tag{4.1}
\]

Their component two-section is connected.  Any spanning family must select
both atoms, but its incidence graph contains the four-cycle

\[
                         1-a-2-b-1.                               \tag{4.2}
\]

It is not an incidence hypertree: the selected gain is
`2+2=4>|V|-1=3`.  Whichever atom is toggled first merges three components;
the second then sees `1,2` already in the same component and is not a strict
three-way merge.  Four component vertices are minimum for a connected
two-section with no spanning incidence tree: on at most three vertices, a
minimal connected support family either contains the whole vertex set in
one atom or reduces to an ordinary graph tree.

This is an exact component-support obstruction.  A particular second atom
might still be a useful rethread or binary merge after the first, but that
requires its full prefix signature and is not certified by two-section
connectivity.

### Proposition 4.2 (fixed pull-edge SDR obstruction)

Let the fixed pull-tree be the path `12,23`.  Take two distinct, physically
compatible atoms `a,b`, both with support `{1,2,3}`.  Assign `a` to pull edge
`12` and `b` to pull edge `23`.  This is a system of distinct physical atom
representatives for the two pull edges, and every pull edge is shadowed.

Nevertheless the incidence graph is `K_(3,2)`, so it has cycles and total
gain four instead of two.  The first atom already joins all components; the
second is not another strict merge.  The fixed-edge SDR has counted the
same rank-two support twice.  The exact pull-cover formulation instead uses
one ternary atom with `Q_t={12,23}`.

Thus the coherent-ECO leaf-deletion shadow theorem supplies candidates for
every pull edge, but an edgewise SDR is a correct selection theorem only
after restricting to binary atoms.  In the full ECO family the units are
hyperedge bundles.

## 5. Rank-balanced router closure for a hypertree

The private tree-damage identity has a weighted hypergraph form.  Let the
component blocks indexed by `V` have pairwise disjoint internal router banks
and satisfy

\[
                         c(K_v(Y_v))\le |Y_v|+1.                    \tag{5.1}
\]

Let `S` be an incidence hypertree.  Put `r_t=|H_t|-1`.  For each atom `t`,
let `R_t` be a private router bank, disjoint from every other atom and block
bank.  Assume every deletable vertex capable of separating this atom lies in
`R_t`, its sink bank is dedicated, the atom is live unless its private
source-to-sink system is separated, and every separating set in `R_t` has
size at least `r_t`.  Here `c(K_Y)` counts the components of the surviving
component hypergraph, equivalently of its two-section.

### Theorem 5.1 (rank-balanced private hyper-tree sum)

Under these hypotheses, the surviving hypermerge catalogue satisfies

\[
                         c(K_Y)\le |Y|+1                            \tag{5.2}
\]

for every router deletion `Y`.

#### Proof

Let `D(Y)` be the dead atoms.  A live subfamily of an incidence tree is an
incidence forest.  Starting from the internal block survivors and inserting
the live atoms gives the exact damage identity

\[
 c(K_Y)-1
   =\sum_{v\in V}\bigl(c(K_v(Y_v))-1\bigr)
      +\sum_{t\in D(Y)}r_t.                         \tag{5.3}
\]

Indeed, a live atom joins `|H_t|` pieces in distinct incidence-tree branches
and lowers the count by `r_t`; deleting it from the full incidence tree
creates exactly `r_t` additional branches.

By (5.1), the first sum is at most \(\sum_v|Y_v|\).  Killing atom `t` costs at
least `r_t` vertices of its private bank.  The atom banks are disjoint, so

\[
                      \sum_{t\in D(Y)}r_t
                       \le\left|Y\cap\bigcup_tR_t\right|.           \tag{5.4}
\]

Substitution in (5.3) gives (5.2).  \(\square\)

For a binary atom `r_t=1`, one private path is enough: a deletion killing
that path pays the one unit of component damage.  For a ternary atom
`r_t=2`, one path is not enough.  If its only route contains a vertex `z`,
deleting `z` kills the atom and splits its three incident branches, giving

\[
                         c(K_{\{z\}})=3>2.                           \tag{5.5}

\]

A sufficient private certificate in the atomic live/dead model is protected
vertex connectivity at least two from the atom source to its dedicated sink
bank, with the source and sink either undeletable or carrying capacity at
least two.  Then disabling the whole atomic hypermerge costs two router
deletions.  Another valid architecture replaces the atom's
component effect by two separately protected effective bridges, but that
requires a literal correlated physical decomposition; it cannot be inferred
from the one hexagon alone.

The theorem is a damage certificate.  If the downstream linkage model
requires named simultaneous source--sink pairs or all-or-none grouped
sources, those pairing equations remain part of the prepared atom signature.
One must not promote the weighted condition to an ordinary unpaired gammoid
without proving that representation.

### Corollary 5.2 (literal unitwise-survival certificate)

For each atom `t`, choose a tree `R_t` on `H_t`.  Suppose the union of these
unit trees is a component tree and the physical signature has a literal
unitwise decomposition: every one of the `r_t` unit edges is separately
executable and remains live when another unit of the same atom dies.  Give
each unit edge its own named source-to-distinct-sink occurrence path.  If all
unit paths, within and between atoms, are vertex-disjoint and avoid the
internal block banks, then router resilience holds.

#### Proof

There are exactly

\[
                        \sum_t r_t=|V|-1
\]

pairwise-disjoint paths, one for every edge of the unit-expanded component
tree.  A deletion set kills at most one such unit edge per deleted router
vertex.  Deleting at most `|Y|` edges of a tree leaves at most `|Y|+1`
components.  \(\square\)

For an indivisible ternary ECO atom, two distinct source elements of joint
linkage rank two do **not** imply the unitwise-survival hypothesis.  If
losing either source disables the all-or-none atom, one deletion removes
both rank units and (5.5) returns.  Such an atom must instead use the
rank-two atomic failure-cut hypothesis of Theorem 5.1, a weighted-laminar
analogue, or a separately proved physical unitwise decomposition.  Copying
one source twice has gammoid rank one in any event.

## 6. Joint private coherent ECO collar theorem

### Theorem 6.1 (prepared simultaneous ECO implication)

Let `S` be a set of coherent ECO atoms such that:

1. the atoms are physically compatible and prefix-faithful strict
   hypermerges;
2. `I(S)` is a tree;
3. each atom has an exact private matching splice, the effective gap bundles
   align with a tree on `H_t`, and every forced port is in the transported
   unique matching;
4. the matching/socket banks of distinct atoms are disjoint;
5. the occurrence router satisfies Theorem 5.1, independently of the
   colour/gap banks, and its named/grouped linkage equations are exact; when
   a literal independently surviving unit decomposition exists, Corollary
   5.2 supplies these rows;
6. the fixed decoration is transparent on the entire selected subset cube;
   and
7. boundary reachability and every in-scope residence, shadow, trace,
   socket/voltage and compiler transition are prefix-safe.

Then the atoms admit an ordered simultaneous private coherent hyperleaf
gluing.  Every prefix is component-acyclic, gap-leaf-peelable, owner-aligned,
fixed-decoration transparent and directed-boundary-acyclic, and retains the
restriction of the common private linkage/damage certificate.  The full
selected hypertree is router-resilient and the final factor is connected.

#### Proof

Theorem 2.1 and Corollary 2.2 give the component chronology.  Exact matching
splicing and owner alignment give the gap forest and forced decoration row.
Theorem 5.1 gives router resilience.  Conditions 6--7 are precisely the
remaining prepared prefix rows, so induction over the rooted incidence tree
finishes the proof.  \(\square\)

This theorem is the hypergraph analogue of the binary private coherent leaf
theorem.  It does not assert that the explicit ECO family contains such an
`S` for every `n`.

## 7. Collision masking, the raw `m=5` closure, and the live order

The authoritative supply facts now have the following exact interpretation.

* Standard MMM labels are coherent exactly when their word parameter `u` is
  empty; these binary labels are disconnected from `n=5` onward.
* ECO atoms shadow every standard pull and make the unfiltered two-section
  connected.
* In one fixed rotation, the physical-port conflict graph and both forced
  owner-colour collision graphs are the same directed path forest:

  \[
                 1p100v\longrightarrow 1p010v.                    \tag{7.1}
  \]

  It has exactly \(\operatorname{Cat}_{n-2}\) edges.  One independent-set
  choice therefore removes physical collisions and both local owner-colour
  collisions simultaneously.  This is local injectivity, not existence of
  a complete upper transversal or owner matching.
* Finite audits through `n=7` find physically disjoint Hamiltonizing ECO
  hypertrees.  This is valuable positive evidence for Items 1--2 of Theorem
  6.1, not an all-dimension proof and not evidence for Items 3--7.

The canonical project-`m=5` factor closes the raw minimal ECO recursion
negatively.  It has three components and 45 physical ECO atoms.  Exhaustion
of all 648 legal ordered two-atom reductions (324 endpoint Hamilton cycles)
shows that every accepted pair already has disjoint six-port supports and
disjoint forced three-colour faces, but every endpoint realizes only 81 of
84 turn colours on each shore, missing

\[
      \{219,365,438\}\quad\text{above},\qquad
      \{73,146,292\}\quad\text{below}.                           \tag{7.2}
\]

Hence no upper transversal exists, before a gap forest or literal owner
test can be formed.  Collision-independent incidence-hypertree selection
must therefore occur after palette preparation.  This does not exclude a
preliminary neutral packet or a repaired factor; the synchronized repaired
`m=5` state remains positive.

The exact constructive quantifier order is

\[
\boxed{
\begin{aligned}
 &\text{controlled zero-debt repair/rethread}\\
 &\longrightarrow\text{ collision-independent, component-faithful
 incidence hypertree}\\
 &\longrightarrow\text{ one leaf-peelable upper transversal and
 owner-aligned residual matching}\\
 &\longrightarrow\text{ rank-balanced private or certified laminar
 occurrence routing}.
\end{aligned}}                                                     \tag{7.3}
\]

Every arrow is evaluated on the endpoint produced by the preceding stage.
In particular, an owner mask from the raw canonical factor cannot be reused
after repair, and occurrence-route privacy remains orthogonal to gap/colour
privacy.

The smallest precise next catalogue is therefore not “one ECO atom per MMM
pull edge.”  It is one of the following.

1. A binary, child-preallocated ECO shadow catalogue satisfying the
   matroid/Hall rows (3.4)--(3.5); or
2. a genuine exact pull cover (3.2), with every indivisible ternary atom
   carrying an atomic failure cut of size two (or an exact weighted-laminar
   certificate), or else a literal two-unit independently surviving
   decomposition, together with one owner-aligned matching splice.

This keeps the repaired ML(7) Hamilton rethreads separate from component
merge atoms and keeps colour/gap privacy separate from physical occurrence
routing.  Static coherent supply and the unrepaired canonical minimal-ECO
route are both closed.  Repair-plus-ECO remains live; simultaneous
compatible private hypertree supply at the repaired endpoint is the
remaining central obstruction.

## 8. Deterministic audit and dependencies

The lightweight audit
`scratch/audit_catalan_eco_compatible_hypertree_private_collar_20260731.py`
checks the two incidence obstructions, the fixed-pull-edge SDR failure, the
nonmatroid physical-conflict exchange witness, and the rank-one versus
rank-two router damage rows.  These are abstract exact interface fixtures,
not literal middle-levels no-go instances.

The authoritative inputs are:

* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md`;
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`;
* `MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md`;
  and
* `MATH_THEOREM_CATALAN_PRIVATE_COHERENT_COLLAR_LEAF_EXTENSION_20260731.md`.

The strict hypermerge and prepared-subset hypotheses are load-bearing.  An
atom which is only a rethread, whose binary path pairing changes after an
earlier toggle, or whose route/source grouping is not rank-balanced lies
outside the theorem.
