# Router resilience is closed under private tree sums

Date: 2026-07-31  
Status: exact abstract composition theorem on the prepared fixed-router
face; exact minimal nonlocal obstruction; no all-`m` coherent-catalogue
supply claim

## 0. Verdict

The router-resilience condition

\[
                         c(K_Y)\le |Y|+1                         \tag{0.1}
\]

has a genuinely recursive sufficient form.  Router-resilient blocks may be
joined along a tree provided every inter-block merge owns a private
source-to-sink occurrence channel.  The proof is an exact additive damage
identity: internal component damage plus failed tree adhesions is the whole
damage.

This is the natural router theorem for node-private plane-tree gluing.  It
also identifies the load-bearing meaning of *private*: private gap colours
or disjoint coherent-hex colour triples do not imply private occurrence
channels.  The former solve the decoration matching; the latter solve the
linkage gammoid.

The privacy cannot be replaced by edgewise or single-router tests.  Three
tree edges whose sources form the circuit `U_{2,3}` give a minimum
two-router synergy obstruction: every proper gluing subtree is routable and
every singleton deletion passes, but the full component tree fails (0.1).

## 1. Routed component systems

A routed component system consists of a component multigraph `K`, a fixed
vertex-capacitated directed network `N` with sink bank `Z`, and one source
`s_t` for every labelled component edge `c_t`.  For a router deletion set
`Y`, put

\[
 T_Y=\{t:s_t\leadsto Z\text{ in }N-Y\},\qquad
 K_Y=(V(K),\{c_t:t\in T_Y\}).                       \tag{1.1}
\]

Isolated component vertices count in `c(K_Y)`.  Source splitting permits
`Y` to be restricted to the internal capacity-one router vertices; the
same statements hold if sources and sinks are included among the split
capacity vertices.

Adding component labels, adding alternate routes, or adding sinks can only
add edges to every `K_Y`, hence can only decrease `c(K_Y)`.  It is therefore
enough to exhibit a router-resilient surviving backbone.

## 2. Exact additive damage identity

Let `J` be a tree on block indices `1,...,h`.  Block `i` has a component
vertex set `V_i`, a router bank `R_i`, and a surviving graph
`K_i(Y_i)` for `Y_i subseteq R_i`.  The sets `V_i` and `R_i` are pairwise
disjoint.  For every tree edge `a=ij`, add one component bridge `b_a` from a
vertex of `V_i` to a vertex of `V_j`.

Suppose the bridge has a fixed directed path `P_a` from its source to a
dedicated sink.  The paths `P_a` are pairwise vertex-disjoint and avoid all
block router banks.  Let

\[
 D(Y)=\{a\in E(J):Y\cap V(P_a)\ne\varnothing\}.     \tag{2.1}
\]

Let `H_Y` be the union of the block survivors and the bridge edges
`b_a` for `a notin D(Y)`.

### Lemma 2.1 (additive damage)

Writing `c_i(Y_i)=c(K_i(Y_i))`,

\[
 c(H_Y)-1
   =\sum_{i=1}^h\bigl(c_i(Y_i)-1\bigr)+|D(Y)|.       \tag{2.2}
\]

#### Proof

Before the bridges are added there are `sum_i c_i(Y_i)` components.  The
surviving bridge indices form the forest `J-D(Y)`, with
`h-1-|D(Y)|` edges.  Every such bridge joins two different current
components: a pre-existing connection between its endpoint blocks would
project to a cycle of `J-D(Y)`.  Thus every surviving bridge lowers the
component count by exactly one, giving

\[
 c(H_Y)=\sum_i c_i(Y_i)-\bigl(h-1-|D(Y)|\bigr),
\]

which is (2.2). \(\square\)

### Theorem 2.2 (private tree-sum closure)

If every block is router-resilient,

\[
                         c_i(Y_i)\le |Y_i|+1,        \tag{2.3}
\]

then the union system is router-resilient.  The conclusion remains true
after arbitrary extra component labels or alternate routes are added.

#### Proof

Pairwise path disjointness injects every member of `D(Y)` into a distinct
deleted path vertex, so

\[
                         |D(Y)|\le
   \left|Y\cap\bigcup_a V(P_a)\right|.              \tag{2.4}
\]

Using (2.2)--(2.4),

\[
 c(H_Y)-1
 \le \sum_i |Y_i|+|D(Y)|
 \le |Y|.
\]

The actual surviving graph `K_Y` contains `H_Y`, so
`c(K_Y)<=c(H_Y)<=|Y|+1`. \(\square\)

### Corollary 2.3 (wedge, leaf and ear closure)

1. The graph `1`-sum of two router-resilient systems at one shared factor
   component is router-resilient when their router interiors and sink banks
   are disjoint.  Indeed `c=c_1+c_2-1`.
2. A disjoint system may be attached to an old one by one privately routed
   bridge, and the result remains resilient.
3. More generally, add new factor vertices by a rooted forest in which each
   new tree edge has a private channel.  The result remains resilient.
4. For a two-anchor ear, use any rooted spanning subforest of the ear as the
   private backbone.  The omitted closing edge is an extra edge and can only
   improve resilience.

Thus a rooted plane-tree recursion is automatic on the router row when the
glue at every nonroot node owns a channel in a node-private annulus.  Mere
subtree containment is weaker: ancestor and descendant channels may still
share a bottleneck.

## 3. A laminar tree-contiguous certificate

There is a broader sufficient form which permits a deleted resource to kill
many parallel labels, provided it creates only one laminar topological cut.

For every router vertex `v`, choose a component set `A_v subseteq V(K)`.
Assume the family `{A_v}` is laminar.  For `Y`, let `P_Y` be the partition
of `V(K)` into the nonempty atoms of membership in the sets
`{A_v:v in Y}`.  Suppose that

\[
                 K_Y[B]\text{ is connected for every }B\in P_Y.      \tag{3.1}
\]

### Proposition 3.1 (laminar-cut resilience)

Under (3.1), `K` is router-resilient.

#### Proof

Adding one set to a laminar family splits at most one existing atom, so
`|P_Y|<=|Y|+1`.  Every connected component of `K_Y` is a union of atoms by
(3.1); edges between atoms can only merge them.  Hence

\[
                         c(K_Y)\le |P_Y|\le |Y|+1.
\]

\(\square\)

A convenient local specialization fixes a rooted backbone tree `R` and
assigns every router resource to at most one parent--child edge.  Require
that every backbone edge absent after deleting `Y` is charged to a deleted
resource assigned to that edge.  Then `K_Y` contains `R` minus at most
`|Y|` edges.  This is the precise global form of the slogan “one deleted
private router exposes at most one additional component.”

## 4. Joint coherent-hex sufficient face

The router theorem can be combined with the forced-port theorem without
confusing their resources.  Let `S` be a coherent component-spanning tree.
Fix an upper transversal and a base gap--lower-colour perfect matching `M`.
For every `t in S`, suppose there are:

1. a three-gap block `G_t` and three-colour block `C_t`, with the blocks
   pairwise disjoint over `t`;
2. `M(G_t)=C_t` and a forced-port bijection
   `F_t:G_t -> C_t`; and
3. independently, an occurrence-router bank `R_t` containing the transfer
   source and a path to a dedicated sink, with the banks and paths pairwise
   vertex-disjoint.

Assume also that the forced upper ports are distinct and belong to the fixed
upper transversal.

### Corollary 4.1 (private matching blocks plus private channels)

The selected coherent tree passes both residual forced-port Hall and router
resilience.

#### Proof

Replace `M|G_t` by `F_t` independently in every disjoint block.  The result
is again a perfect gap--colour matching and contains every forced lower
port.  Thus one joint decoration selects all six ports of every coherent
label.  The occurrence paths satisfy Theorem 2.2 (or the fixed-tree private
channel criterion), so the selected component tree is router-resilient.
Coherence supplies fixed-decoration transparency. \(\square\)

If the gap graph is leaf-peelable, its perfect matching is unique.  In that
case the block condition sharpens to the pointwise owner alignment
`F_t subseteq M`.  The known private triples are evidence for the
gap/colour blocks.  They are not evidence for the occurrence banks: colour
vertices forget occurrence identifiers, and augmenting routes can share a
physical bottleneck even when all displayed colours are distinct.

## 5. Sharp nonlocal obstructions

### Proposition 5.1 (shared-router failure on a component tree)

Let `K` be the path `1-2-3`.  Route both edge sources only through one
capacity-one router vertex `v`, then to distinct sinks.  Each edge is
individually routable and `K` is a tree, but for `Y={v}` both edges die, so

\[
                         c(K_Y)=3>|Y|+1=2.           \tag{5.1}
\]

Thus a component tree plus local coherence is not a router theorem.

### Proposition 5.2 (the `U_{2,3}` synergy obstruction)

Let `K` be the path `1-2-3-4`, with edge labels `t_1,t_2,t_3`.  In the
router network use two capacity-one vertices `x,y` and distinct sinks, with

* `s_1` routable only through `x`;
* `s_2` routable only through `y`; and
* `s_3` routable through either `x` or `y`.

Every two of the three sources link vertex-disjointly to distinct sinks, but
all three do not.  They form the three-element gammoid circuit `U_{2,3}`.
Moreover,

\[
 c(K_{\{x\}})=c(K_{\{y\}})=2,
 \qquad
 c(K_{\{x,y\}})=4>3.                               \tag{5.2}
\]

Hence every proper gluing subtree is routable and every singleton router
deletion satisfies (0.1), while the full tree fails it.  Four component
vertices are minimum for a two-router violation, since for at most three
vertices one always has `c(K_Y)<=3=|Y|+1` when `|Y|=2`.

This is the smallest reason a recursive proof cannot retain only an
edgewise “good glue” bit.  It must carry either node-private channels, the
laminar global charging certificate of Section 3, or the full
pairing-resolved boundary-linkage state.

## 6. Exact scope

Theorems 2.2 and 3.1 solve only the router-resilience coordinate after a
prepared coherent merge tree or catalogue is supplied.  Corollary 4.1 also
solves the forced-port matching on its explicit block-private face.  None of
the statements constructs in every dimension:

* enough coherent **merge** hexagons;
* the required common upper transversal and private blocks;
* node-private occurrence channels;
* residence and deeper-shadow redistribution;
* a physical socket cycle with primitive voltage; or
* the lower compiler.

The standard plane-tree gluing tree supplies the right component topology,
but its published labels do not automatically supply either occurrence
privacy or the common decoration.  Those are the remaining constructive
inputs.
