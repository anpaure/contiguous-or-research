# Private coherent collars: exact leaf splicing and rooted supply

Date: 2026-07-31  
Status: exact dimension-uniform preservation theorem on the prepared binary
child-private/aligned face; exact minimum reduced-row correlation
obstruction; no all-`m` supply, ECO-hypertree, residence, voltage, or
compiler theorem

## 0. Verdict

After the two private closure theorems, the central recursive object has a
literal local certificate.

* On a leaf-peelable gap forest, a forced lower port is legal exactly when
  its occurrence edge is in the unique gap--colour matching.  A private
  matching splice preserves this statement without solving another Hall
  problem.
* On the occurrence-router side, a new component block may be attached by
  one child-private path.  The additive tree-damage identity then preserves
  router resilience.
* These are orthogonal resources.  They compose only when the **same
  coherent merge label** carries both certificates.

For a prepared family in which every nonroot child owns its matching-splice
bank and its occurrence-route bank, retain a directed parent--child label
only when it is simultaneously

1. a component-faithful coherent merge;
2. a forest-safe matching splice whose forced ports lie in the transported
   matching;
3. an aligned private gap attachment;
4. a node-private routed bridge; and
5. prefix-safe for directed boundary reachability and every separately
   carried physical collar row.

Call the resulting directed multigraph `A_*`.  There is a spanning private
coherent collar rooted at `r` if and only if `A_*` has an out-arborescence
rooted at `r`, equivalently

\[
 \boxed{\delta^-_{A_*}(X)\ne\varnothing
   \quad\text{for every }\varnothing\ne X\subseteq V-\{r\}.}       \tag{0.1}
\]

This is an exact all-dimension induction theorem **inside the prepared
binary private face**.  It converts that face's remaining central gate into
joint coherent leaf supply.  The coherent-ECO supply theorem introduces
ternary hypermerge atoms as well; their exact incidence-hypertree and
rank-balanced-router extension is developed separately in
`MATH_THEOREM_CATALAN_ECO_COMPATIBLE_HYPERTREE_PRIVATE_COLLAR_20260731.md`.
Neither note proves that the required selected family exists in every
dimension.

The correlation is load-bearing.  A three-component, three-label fixture
below has an owner-aligned spanning tree and a node-private routed spanning
tree, every label is individually routed, but no one tree has both
properties.  Three components are minimum under those nondegeneracy
hypotheses.

## 1. Exact matching splice at one leaf

Let `Gamma` be a finite bipartite forest with perfect matching `M`, and let
\(F\subseteq M\) be the already forced lower-port edges.  Let

\[
                       D\subseteq M-F                              \tag{1.1}
\]

be a bank of owner sockets released by one prospective leaf packet.  Put
`Gamma^circ=Gamma-D`.  Its exposed old vertices are `X=V(D)`.

Let `P` be a new private vertex bank, disjoint from `Gamma`, let `R` be a
set of retained old root vertices disjoint from `X`, and let `B` be a
bipartite edge set on `P union X union R`, disjoint from the retained old
edge set.  Define

\[
                   \Gamma'=\Gamma^\circ\cup B.                     \tag{1.2}
\]

Contract every tree component of `Gamma^circ`, retain the vertices in `P`,
and retain every edge of `B`, including loops and multiplicities.  Denote
the resulting attachment multigraph by `A(B)`.

### Lemma 1.1 (exact private matching-splice criterion)

Suppose \(N\subseteq B\) is a matching which saturates every vertex of
`P union X` and is incident with no vertex of `R`.  Then

\[
                         M'=(M-D)\sqcup N                          \tag{1.3}
\]

is a perfect matching of `Gamma'`, and

\[
             \Gamma'\text{ is a forest}
       \quad\Longleftrightarrow\quad A(B)\text{ is a forest}.       \tag{1.4}
\]

When these equivalent conditions hold, `M'` is the unique perfect matching
of `Gamma'`.  For a new forced set `F_new`, all old and new forced ports
extend if and only if

\[
                         F\cup F_{\rm new}\subseteq M'.             \tag{1.5}
\]

Conversely, suppose `Gamma'` is a forest with a perfect matching which
restricts to `M-D` away from `P union X`.  Its restriction to the splice is
a matching `N` as above, and (1.4)--(1.5) are necessary.

#### Proof

Every old vertex outside `X`, including every retained root in `R`, is
covered once by `M-D`; every vertex in `P union X` is covered once by `N`;
and the two matchings have disjoint vertex supports.  This proves (1.3).

Contracting a forest is graphic-matroid contraction.  Thus adding `B` to
`Gamma^circ` creates a cycle exactly when the image of `B` contains a
cycle, where a loop and a parallel pair are cycles of lengths one and two.
This proves (1.4).  A forest has at most one perfect matching, so `M'` is
unique.  The forced-port owner-alignment theorem now says precisely that a
forced set extends if and only if it is contained in that unique matching,
which is (1.5).  The converse follows by restricting the asserted perfect
matching to the vertices exposed by deleting `D`, and by the same graphic
contraction.  \(\square\)

Two useful special cases are worth separating.

* If `D` is empty, `R={r}`, and `B` meets the old graph only in `r`, which
  is left unmatched by `N`, this is a root-neutral forest graft.
* If `D={xy}` and a private tree replaces the matched socket `xy`, its new
  matching must saturate `x,y` and all new vertices.  This is the exact
  matched-edge substitution used by a private socket collar.

Thus a collar may replace a matched socket; it need not be a literal
one-vertex graft.  What must be preserved is the exposed matching signature,
not a vague statement that the new colours are private.

### Corollary 1.2 (aligned private leaf packet)

Suppose the attachment multigraph of a packet consists of

* one effective edge between two previously distinct contracted gap
  components; and
* rooted private trees meeting that effective edge or the retained core in
  at most one vertex each.

Then its attachment is a forest.  If its matching splice satisfies (1.3)
and its forced edges satisfy (1.5), the post-packet gap graph is
leaf-peelable and every forced port is literally owner-aligned.

For several packets, suppose their private vertices and released socket
banks are disjoint and their effective gap edges are the injective image of
their factor-component edges.  Every factor-component forest then induces
a gap attachment forest.  The matching splices commute, and owner alignment
is checked packet by packet.

#### Proof

Peel the rooted private trees.  What remains is the displayed effective
edge.  For several packets, peeling all private trees leaves an injective
copy of the selected factor-component forest, so no gap cycle remains.
Disjoint matching supports make the union of (1.3) a perfect matching.
Lemma 1.1 gives the conclusions.  \(\square\)

This is the exact sense in which colour/gap privacy is recursive.  It says
nothing about the physical occurrence router.

## 2. The private coherent leaf interface

Let the prepared factor be partitioned into blocks indexed by a finite set
`V`, with distinguished root `r`.  A block may already contain an accepted
internal component tree.  It carries:

* one fixed occurrence-labelled decoration `D`;
* a leaf-peelable gap forest and its unique matching;
* an internally router-resilient component catalogue in a router bank
  `R_v`; and
* the exact boundary state required by the ordered fixed-decoration
  theorem.

The banks `R_v` are pairwise disjoint.  For every candidate directed label
`t:u -> v`, with `v != r`, require the following data.

### L0. Exclusive child ownership

All mutable physical, gap, matching and router resources of the label lie
in a bank owned by its head `v`, apart from its declared parent anchors in
`u`.  Banks belonging to different heads are disjoint.  Alternative labels
with the same head are mutually exclusive; one selected arborescence uses
at most one of them.

This is the correlation/superposition hypothesis.  It is stronger than
pairwise colour disjointness.

### L1. Coherent component merge

The label is a literal component-faithful binary `MERGE`.  Its all-six
ports have one common external lower add label and one common external upper
delete label, and the fixed decoration passes the transparent boundary-mark
test.  Its effective component edge is `uv`.

### L2. Exact aligned matching splice

Relative to the child's prepared socket bank, the label has data
`(D_t,R_t^gap,B_t,N_t,F_t)` satisfying Lemma 1.1.  Its attachment multigraph is a
private rooted forest with one effective nonprivate edge aligned with
`uv`, and every forced lower port of the label belongs to the transported
matching.

On the leaf-forest face this last clause is exactly literal owner alignment,
not a surrogate Hall inequality.  Off the forest face it would have to be
replaced by an explicit vertex-disjoint alternating-cycle packing.

### L3. Node-private occurrence route

The label source has a fixed path `P_t` to a dedicated sink.  For labels
with different heads, these paths are vertex-disjoint and avoid every
internal block router bank `R_w`.  Colour vertices and gap vertices are not
identified with router vertices: this is an independent privacy clause.

### L4. Prefix reachability

After inserting the label's passive internal boundary relation, let `rho`
be the current strict transitive boundary reachability.  If the effective
arc is `T_t -> H_t`, the exact one-step condition is

\[
                         (H_t,T_t)\notin\rho.                        \tag{2.1}
\]

The family must make this condition prefix-closed.  It is enough that all
retained and new arcs increase one global potential, or that reverse
reachability projects to a path between the endpoints `u,v`; a
component-forest prefix then forbids it.

### L5. Separately carried physical collar

Any residence, bounded deep-shadow service, protected trace,
gain--Brauer/socket, voltage, or compiler condition demanded at this stage
is evaluated on the same literal label and its exact collar state.  These
rows may be used to filter labels only when their transition is
prefix-closed under L0.  None follows from L1--L4.

A label satisfying L0--L4, and L5 when L5 is in scope, is a **private
coherent leaf arc**.  Let `A_*` be the directed multigraph of these arcs.

## 3. Exact leaf-extension theorem

### Theorem 3.1 (one-leaf preservation)

Let \(W\subseteq V\) carry an accepted private coherent collar rooted at `r`,
and let \(v\notin W\).  Under L0, the block `v` can be adjoined as a leaf
without reopening any old certificate if and only if there are \(u\in W\)
and a private coherent leaf arc `t:u -> v`.

After the extension:

1. the component edges remain a tree;
2. the gap graph is a forest with a unique perfect matching;
3. every old and new forced port is owner-aligned;
4. router resilience holds;
5. directed boundary support stays acyclic; and
6. every physical row explicitly included in L5 is preserved.

#### Proof

The new component edge joins the old component tree to the disjoint block
`v`, proving Item 1.  L2 and Lemma 1.1 give Items 2 and 3; L0 ensures that
the splice neither releases an old forced edge nor overlaps an earlier
splice.

For Item 4, regard the old collar and block `v` as two router-resilient
blocks.  The path `P_t` is disjoint from both router banks.  The private
tree-sum theorem gives

\[
                         c(K_Y)\le |Y|+1
\]

for every deletion set `Y`.  Equivalently, internal component damage and
failure of the one new bridge charge to disjoint parts of `Y`.

Condition (2.1), followed by exact transitive-closure update, gives Item 5.
L5 gives Item 6.  Conversely, within the declared L0--L5 class, an accepted
leaf extension has one component merge `u-v`; Lemma 1.1 forces its matching
splice and owner membership, its declared private route is L3, and
acyclicity forces (2.1).  Hence its label is an arc of `A_*`.  \(\square\)

The converse is scoped to the private leaf grammar.  A nonprivate system
may be resilient through alternate routes or alternating-cycle exchange
without possessing a literal private arc.

### Theorem 3.2 (rooted private coherent collar)

Under L0--L5, the following are equivalent.

1. There is a spanning private coherent collar rooted at `r`, constructed
   by leaf extensions.
2. `A_*` contains a spanning out-arborescence rooted at `r`.
3. The cut condition (0.1) holds.
4. Every vertex of `A_*` is reachable from `r`.

For any chosen arborescence, a parent-before-child order constructs the
collar and the reverse order is a literal leaf-peeling certificate.  Once
the full item-2189 Boolean-cube hypotheses are available, every ordering of
the same undirected component tree is executable; the present induction
needs only the displayed parent-before-child order.

#### Proof

The equivalence of Items 2--4 is the elementary rooted branching theorem.
If every vertex is reachable from `r`, choose for each nonroot vertex the
last arc on one shortest `r`-to-vertex path.  Distances strictly increase
along the chosen arcs, so they form an out-arborescence.  Conversely, an
out-arborescence enters every nonempty set not containing its root, proving
(0.1), and plainly reaches every vertex.

Given an arborescence, order its vertices by nondecreasing distance from
the root and repeatedly apply Theorem 3.1.  L0 makes all different-child
splices commute.  On the gap side, the effective attachment edges are an
injective copy of the component arborescence, so Corollary 1.2 applies.  On
the router side, the bridge paths are pairwise disjoint, so the additive
tree-damage theorem applies to the whole tree.  This proves Item 1.

Any collar constructed in the private leaf grammar has one selected
incoming label for every nonroot block and no component cycle.  Orienting
the selected tree away from `r` gives an out-arborescence contained in
`A_*`, proving Item 1 implies Item 2.  \(\square\)

### Corollary 3.3 (predetermined recursive parent map)

If an inductive construction prescribes a parent `p(v)` for every nonroot
block, the whole gate reduces to

\[
 \boxed{
   \text{for every }v\ne r\text{, at least one label }
   p(v)\longrightarrow v\text{ satisfies L0--L5}.}                 \tag{3.1}
\]

There is no further forced-port Hall or router-resilience computation.
The point is not that the two rows are identical; it is that their separate
private certificates are carried by the same chosen label.

## 4. Minimum nondegenerate correlation obstruction

Separate owner-aligned and routed spanning trees do not imply Theorem 3.2.
The following reduced-row fixture retains literal gap occurrences and
capacity-one router vertices.

Take component vertices `0,1,2` and coherent labels

\[
               a=01,\qquad b=12,\qquad c=02.                      \tag{4.1}
\]

Let the gap forest have matched edges

\[
                  M=\{g_i c_i:0\le i<8\}                         \tag{4.2}
\]

and one additional edge `g_0 c_3`.  This is a forest and `M` is its unique
perfect matching.  Give the labels the forced lower triples

\[
\begin{aligned}
 F_a&=\{g_0c_3,g_6c_6,g_7c_7\},\\
 F_b&=\{g_0c_0,g_1c_1,g_2c_2\},\\
 F_c&=\{g_3c_3,g_4c_4,g_5c_5\}.
\end{aligned}                                                       \tag{4.3}
\]

Thus `b,c` are owner-aligned, their triples are mutually gap- and
colour-private, and `{b,c}` is an owner-aligned component-spanning tree.
Label `a` is not owner-aligned.

In the occurrence router, let the fixed paths of `a,b,c` use respectively

\[
                             \{x\},\quad\{y\},\quad\{y\}.          \tag{4.4}
\]

Every label is individually routed.  The trees `{a,b}` and `{a,c}` have
pairwise vertex-disjoint occurrence paths and are router-resilient.  The
only owner-aligned tree `{b,c}` loses both edges when `y` is deleted, so

\[
                         c(K_{\{y\}})=3>2=|\{y\}|+1.               \tag{4.5}
\]

Hence no common private coherent tree exists.

This fixture is minimum among simple component graphs under the conditions
that every catalogue label is individually routed and both projected
spanning-tree families are nonempty.  With at most two components, an
owner-aligned spanning tree consists of one owner-aligned label; because
that label is individually routed, its singleton route is automatically
private and gives a common tree.  The displayed three-component fixture
therefore attains the minimum.  If labels with no occurrence route are
allowed, the vacuous two-component obstruction with two parallel labels is
possible and carries no structural information.

The example is an exact reduced-row collar fixture, not a literal
middle-levels hexagon census.  It isolates the remaining obstruction:
owner-aligned leaf supply and node-private route supply must intersect on
one coherent branching, rather than merely exist in two projections.

## 5. Consequences and remaining all-`m` gate

The two privacy notions have different objects and different failure
modes.

* **Gap/colour privacy** is a graphic/matching-splice statement.  It prevents
  attachment cycles and, on a forest, freezes every forced port to its
  literal owner edge.
* **Occurrence-route privacy** is a physical linkage statement.  It bounds
  component damage under router deletions.  Distinct colours may still be
  occurrences sharing one bottleneck.

The exact recursive supply target is therefore a family of child-owned
coherent labels for which the jointly filtered graph `A_*` satisfies
(0.1), preferably the stronger predetermined-parent condition (3.1).
Off the leaf-forest face, owner membership must be replaced by compatible
alternating-cycle packing.  Off the node-private router face, the complete
router-resilience or graphic--gammoid row returns.

Nothing here makes the repaired ML(7) Hamilton rethreads into merge arcs.
The component edge in L1 must be a literal merge; item 2171 remains the
separate positive `m=4` merge base.  Likewise, this theorem does not create
the residence-compatible interior actuator missing from the fixed `m=5`
42-path endpoint face.  Residence, deep shadows, the two global path
endpoints, socket/voltage closure and the common-cap compiler remain exact
L5 filters or downstream gates.

## 6. Deterministic audit and dependencies

The lightweight audit
`scratch/audit_catalan_private_coherent_collar_leaf_extension_20260731.py`
checks the forest and unique matching in (4.2), all forced triples, every
component spanning tree, every router deletion, the two separate positive
tree families, and the empty joint family.  It uses no solver and makes no
physical all-`m` claim.

The exact inputs rebased here are:

* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`;
* `MATH_THEOREM_CATALAN_LEAF_PEELABLE_TRANSPARENT_GLUING_STATE_20260731.md`;
* `MATH_THEOREM_CATALAN_ORDERED_FIXED_D_TRANSPARENT_GLUING_AFTER_ROUTER_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORATION_FILTERED_COHERENT_CATALOGUE_20260731.md`;
* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
  and
* handoff items 2192--2195.

The preparation assumptions are load-bearing: occurrence identities are
stable, socket alternatives owned by different children superpose, the gap
effective edge is aligned with the component edge, and boundary
reachability is prefix-safe.  Without them, a local leaf menu is not a
closed inductive state.
