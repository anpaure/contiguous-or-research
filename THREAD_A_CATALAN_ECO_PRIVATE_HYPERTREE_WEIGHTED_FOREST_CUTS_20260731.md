# Private ECO hypertrees: weighted forest cuts and one-anchor construction

Date: 2026-07-31  
Status: exact all-dimension topology and router theorems on the prepared
owner-aligned face; no all-`n` compatible ECO-hypertree construction

## 0. Verdict

The coherent-supply problem and the local two-shore collision problem are
closed, but the selectable topology and postrepair owner problem are not.
For every Dyck parent `D=1u0v`, the central-`000` ECO hexagon is all-six
coherent, and every standard MMM pull adjacency is co-contained in one ECO
hyperedge.  Hence the raw coherent ECO two-section is connected in every
dimension.  At one fixed rotation, the physical-port, lower-owner, and
upper-owner collision graphs are the **same path forest**.  Thus one
independent atom set clears all three local repetition systems at once.

A raw connected two-section does not yet give a private coherent collar.
Three additional facts are now exact.

1. A selected ECO family is an incidence hypertree exactly when it satisfies
   the weighted Berge-forest cuts (2.2) and total rank equality (2.3).
2. Incidence hypertrees are exactly the families admitting a
   **one-anchor expansion**: every new atom meets the already built
   component set in exactly one component and introduces all its other
   components.  A frontier condition gives a greedy catalogue certificate.
3. An atom meeting `r_t` distinct components has hypertree-backbone damage
   `w_t=r_t-1`.  Without alternate reconnecting atoms, a private router
   certificate must give it kill cost at least `w_t`; one private route is
   insufficient for an isolated ternary backbone atom.

This still does not create a global turn transversal.  On the raw canonical
project-`m=5` factor, all `648` topology-safe minimal ECO Hamiltonizations
are already port- and forced-face-disjoint, yet every endpoint misses the
same period-three triple on each shore.  Hence the correct order is

\[
 \boxed{\text{controlled repair/rethread}\to
 \text{collision-free ECO candidate}\to
 \text{same-candidate owner-Hall certification}\to
 \text{private/laminar occurrence routing}.}         \tag{0.1}
\]

After filtering the repaired endpoint to one occurrence-resolved
decoration, literal owner alignment, a prepared matching seam, physical
compatibility, and the weighted private router condition, the one-anchor
theorem gives an executable private coherent ECO hypertree.  Proving that a
repair endpoint has such a filtered expansion in every dimension remains
open.

The forest-cut family is not a matroid when binary and ternary atoms are
mixed.  Thus ordinary graphic matroid intersection is not a hidden solution
to this last selection gate.

## 1. Authoritative ECO input and typed atoms

Use the paper parameter `n`.  The canonical MMM factor has a component set
`V` indexed by plane trees with `n` edges.  The theorem
`MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md` supplies, for
every Dyck parent

\[
                         D=1u0v\in\mathcal D_{n-1},                 \tag{1.1}
\]

the support word `1u000v0` and the incidence hexagon on its three central
zero coordinates.  Its common external labels are `(d,e)=(2n,0)`, up to
rotation.  Every standard MMM pull adjacency is co-contained in the
component support of one such coherent atom.

For a physical ECO atom `t`, let

\[
                         S_t\subseteq V,qquad r_t=|S_t|,\qquad
                         w_t=r_t-1.                                \tag{1.2}
\]

Here `S_t` is the set of distinct old factor components containing the
three old matching edges of the hexagon.  Atoms with `r_t=1` have zero
merge rank and are not gluing atoms.  A binary atom has `r_t=2,w_t=1`; a
ternary atom has `r_t=3,w_t=2`.

Throughout Sections 2--6, selected gluing families contain only atoms with
`r_t>=2`.  Unary zero-rank atom leaves may be deleted without changing
component connectivity and are not part of a merge chronology.

Every statement below is about one **occurrence-resolved realization** of
an atom.  Its six port occurrences, actual gaps, exterior factor edges,
component support, and router source are one indivisible label.  An owner
witness for one phase and a router witness for another phase cannot be
combined.

### The common fixed-rotation collision forest

For the `Cat_(n-1)` atoms with `(d,e)=(2n,0)`, the exact ECO theorem proves
that the physical-port collision graph and the two forced-owner collision
graphs coincide.  Their directed edges are

\[
       1p\,10\,0v\longrightarrow1p\,0\,10v,          \tag{1.3}
\]

and form a path forest with `Cat_(n-2)` edges.  Consequently, for binary
selection variables `z_t`, the single family

\[
                         z_t+z_{t'}\le1              \tag{1.4}
\]

over edges of this path forest simultaneously prevents the displayed
physical-port collision and both forced-face repetitions.  The stable-set
polytope given by (1.4) and `0<=z_t<=1` is integral, but its intersection with the
weighted hypertree system below is not claimed integral.

This collision identity belongs to the raw canonical fixed-rotation port
family.  A preliminary rethread may change exterior factor edges or which
ECO ports remain live.  It may use (1.4) only if it exports those literal
port/owner signatures unchanged; otherwise its exact postrepair conflict
graph must be recomputed.

## 2. Exact weighted Berge-forest cuts

For a selected atom family `T`, form the bipartite incidence graph

\[
 B(V,T):\quad V\ \dot\cup\ T,\qquad vt\in E(B)
       \Longleftrightarrow v\in S_t.                              \tag{2.1}
\]

Every selected atom brings its complete star; individual incidences may not
be discarded.

### Theorem 2.1 (incidence-forest characterization)

The incidence graph `B(V,T)` is a forest if and only if, for every nonempty
`A subseteq V`,

\[
 \boxed{
   \sum_{\substack{t\in T\\S_t\subseteq A}} (|S_t|-1)
       \le |A|-1.}                                                   \tag{2.2}
\]

It is a spanning tree if and only if (2.2) holds and

\[
 \boxed{
                 \sum_{t\in T}(|S_t|-1)=|V|-1.}                    \tag{2.3}
\]

#### Proof

Assume first that `B(V,T)` is a forest.  Fix nonempty `A`, and let `T_A`
be the selected atoms whose complete supports lie in `A`.  The induced
incidence graph on `A dotcup T_A` is a forest.  If `T_A` is nonempty and
uses `a` component vertices in `A` and has `c>=1` nonempty components, then

\[
 \sum_{t\in T_A}|S_t|
       \le a+|T_A|-c\le |A|+|T_A|-1.
\]

Subtracting `|T_A|` proves (2.2).  The empty case is immediate.

Conversely, suppose the incidence graph has a cyclic connected component.
Let `T_0` be its atom vertices and let

\[
                         A_0=\bigcup_{t\in T_0}S_t.
\]

The component has at least as many edges as vertices, so

\[
 \sum_{t\in T_0}|S_t|\ge |A_0|+|T_0|,
 \qquad
 \sum_{t\in T_0}(|S_t|-1)\ge |A_0|,
\]

contradicting (2.2) for `A_0`.  Thus (2.2) is equivalent to incidence
acyclicity.

Finally, under (2.3) the incidence graph has

\[
 \sum_t|S_t|=\sum_t(|S_t|-1)+|T|
                =|V|+|T|-1                                      \tag{2.4}
\]

edges on `|V|+|T|` vertices.  A forest with one fewer edge than vertices
has exactly one component.  Hence it is a spanning tree.  The converse is
the same edge count.  QED.

Equations (2.2)--(2.3) are an exact integer description of the component
topology.  They do not assert integrality of their linear relaxation once
atom-selection variables and physical conflicts are added.

Equivalently, for binary atom variables, the exact topology-plus-local-
collision system is

\[
 \sum_{t:S_t\subseteq A}w_tz_t\le|A|-1
       \quad(\varnothing\ne A\subseteq V),\qquad
 \sum_tw_tz_t=|V|-1,                                \tag{2.5}
\]

together with (1.4).  Its integral solutions are precisely the
fixed-rotation collision-free spanning incidence hypertrees, before
component-faithfulness and the global decoration are tested.

### Proposition 2.2 (the mixed-rank system is not a matroid)

Let `V={1,2,3}` and take atoms

\[
             e=\{1,2,3\},\qquad f=\{1,2\},\qquad g=\{2,3\}.        \tag{2.6}
\]

Both `{e}` and `{f,g}` have forest incidence graphs.  The first family has
one atom and the second has two.  But neither `{e,f}` nor `{e,g}` is a
forest: the two corresponding atom stars share two component vertices and
create an incidence four-cycle.  Therefore the exchange axiom fails.

Thus the general mixed binary/ternary incidence-forest independence system
need not be a matroid and is not automatically an ordinary graphic matroid
intersection problem.  In the all-binary subfamily,
(2.2) is exactly the usual graphic-forest family.

## 3. One-anchor expansion

The weighted cuts have a simple constructive sufficient syntax.

Fix a root component `v_0`.  For an ordered atom list
`t_1,...,t_s`, put

\[
 R_0=\{v_0\},\qquad R_i=R_{i-1}\cup S_{t_i}.                       \tag{3.1}
\]

Call the list a **one-anchor expansion** when

\[
              |S_{t_i}\cap R_{i-1}|=1,qquad
              S_{t_i}\setminus R_{i-1}\ne\varnothing             \tag{3.2}
\]

for every `i`, and `R_s=V`.

### Theorem 3.1 (one-anchor characterization)

A selected positive-rank gluing family (so every `r_t>=2`) is a spanning
incidence hypertree if and only if, for any chosen root component `v_0`,
its atoms admit a one-anchor ordering.
In such an order atom `t_i` introduces exactly `w_(t_i)` new component
vertices into the incidence tree, and

\[
                         \sum_iw_{t_i}=|V|-1.                       \tag{3.3}
\]

#### Proof

At step `i`, add the atom node `t_i`, join it to the unique old anchor, and
join it to `w_(t_i)` new component vertices.  This attaches a star to the
existing incidence tree at one vertex, so no cycle is created and the
result remains connected.  Induction gives a spanning incidence tree.
The rank identity (3.3) follows either by counting the new component
vertices at each step or by Theorem 2.1.

Conversely, root the incidence tree at `v_0` and order its atom nodes by
nondecreasing distance from the root.  Every atom node has exactly one
component neighbour closer to the root.  All its other component neighbours
are its children and cannot have appeared through another earlier atom,
since that would give them two root paths.  Hence the resulting atom order
satisfies (3.2).  QED.

Consequently, on a static globally compatible private catalogue, the
frontier condition

\[
 \boxed{
 \text{for every }R\text{ with }v_0\in R\subsetneq V,
 \text{ some eligible }t\text{ has }|S_t\cap R|=1
 \text{ and }S_t\setminus R\ne\varnothing}                         \tag{3.4}
\]

is sufficient: greedily choose such an atom until all components have been
introduced.  Condition (3.4) is stronger than raw two-section connectivity,
which permits every crossing hyperedge to meet `R` in two or more already
present components.

Condition (3.4) is a sufficient **catalogue** frontier condition, not a
necessary cut for the existence of some hypertree; the exact selected-family
condition remains (2.2)--(2.3).

When atom compatibility is state-dependent, (3.4) must be imposed on the
actual terminal mode and remaining private banks.  It cannot be checked on
unresolved marginal signatures.

## 4. Owner alignment and matching-seam preservation

Fix one upper transversal `I` whose gap--lower-colour graph `Gamma_I` is a
forest with unique perfect matching `M`.  For an occurrence-resolved
coherent atom `t`, let `F_t` be its three forced lower gap--colour edges.
On this face forced-port Hall is exact owner alignment:

\[
                         F_t\subseteq M.                            \tag{4.1}
\]

If the same abstract matched gap--colour edge has several physical
occurrences, (4.1) permits choosing the forced occurrence, but does not by
itself certify the prepared H0--H5 state.  The chosen occurrence lift of
`(I,M)` must be the same literal decoration used by the collar and router.

For a product family, root owner alignment is also insufficient unless
every old/new private matching splice exports the same boundary matching
status.  Equivalently, after deleting its old socket bank, each collar must
replace it by a private forest with the same exposed matched/unmatched
boundary signature.  Under pairwise private splice banks this gives, for
every subset of selected atoms, a forest with its unique transported
matching.  Every pending forced port then remains an owner edge.

This is the exact matching-seam condition of
`MATH_THEOREM_D_PRIVATE_COHERENT_COLLAR_STATE_AND_SUPPLY_OBSTRUCTION_20260731.md`.
It is separate from component incidence acyclicity.

## 5. Rank-weighted router damage

Let `T` be an incidence hypertree.  For every atom `t`, put its occurrence
router in a private bank `R_t`, with the banks disjoint.  Under a router
deletion `Y`, call `t` dead if its complete atomic occurrence transfer has
no surviving route.

### Theorem 5.1 (exact weighted damage identity)

For the surviving hypertree backbone `H_Y`,

\[
 \boxed{
              c(H_Y)-1=\sum_{t\text{ dead}}w_t.}                   \tag{5.1}
\]

Consequently the backbone is router-resilient exactly when

\[
                 \sum_{t\text{ dead under }Y}w_t\le |Y|
                 \quad\text{for every }Y.                          \tag{5.2}
\]

#### Proof

Remove the dead atom nodes from the incidence tree.  An atom node has degree
`r_t`; its removal increases the number of component-containing tree pieces
by `r_t-1=w_t`.  Atom nodes lie on one shore of the incidence bipartition
and are never adjacent, so the increases add.  This proves (5.1), and (5.2)
is its substitution into `c(H_Y)<=|Y|+1`.  QED.

The equality is for the exhibited hypertree backbone.  Extra surviving
catalogue atoms can only join pieces, so the full survivor satisfies
`c(K_Y)<=c(H_Y)`.

### Corollary 5.2 (private kill-cost certificate)

Suppose

\[
 t\text{ dead under }Y\quad\Longrightarrow\quad
                 |Y\cap R_t|\ge w_t.                              \tag{5.3}
\]

Then (5.2) holds.

#### Proof

The private banks are disjoint, hence

\[
 \sum_{t\text{ dead}}w_t
 \le\sum_{t\text{ dead}}|Y\cap R_t|\le|Y|.
\]

QED.

For one source and a private sink bank, minimum source-to-sink cut at least
`w_t` is a sufficient certificate for (5.3), provided the cut convention
includes every deletable split copy of the source and sinks and the atom
remains executable whenever any one route survives.  Merely counting
internally disjoint routes while leaving a unit-deletable source outside the
count is not sufficient.  If the physical atom requires several named
transfers simultaneously, its literal atomic kill condition must be used
instead.

For a ternary atom, `w_t=2`.  If one router vertex kills it, then its
deletion leaves three pieces and

\[
                         3>1+1.                                   \tag{5.4}
\]

Thus a single node-private route, which is exact for a binary merge, cannot
pay for a ternary ECO hypermerge.  It needs private kill cost two, a literal
factorization into two independently survivable binary merges, or an
equivalent weighted laminar charge.

This necessity is for the exhibited hypertree backbone (or a catalogue in
which no alternate live atom reconnects its pieces).  A richer full
catalogue can satisfy router resilience through redundant surviving atoms;
then (5.3) remains sufficient but need not be necessary atom by atom.
The grouped hyperatom semantics and its prepared pairing equations are
essential: (5.1) is not an ordinary unit-edge graphic--gammoid model.

## 6. Private one-anchor ECO theorem after repair

### Theorem 6.1

Let a controlled repair/rethread terminate at a prepared factor `F'` and
export a static, occurrence-resolved ECO atom catalogue.  This export is an
assumption: an ECO atom alternating in the raw canonical factor need not
survive an arbitrary rethread.  Fix one occurrence-resolved prepared
decoration `D=(I,M)` of `F'`.  Suppose the exported catalogue has the
following properties.

1. Every retained atom is an all-six coherent hypermerge.  In the ECO
   orientation of Section 1 its transversal-side ports obey
   \(\{L_a,L_b,L_c\}\subseteq I\), and its opposite-side forced edges

   \[
      F_t=\{(g_{ab},H-e+b),(g_{bc},H-e+c),(g_{ca},H-e+a)\}
          \subseteq M.                                           \tag{6.1}
   \]

   Reverse every shore name together if the opposite occurrence convention
   is used.
   The catalogue satisfies **hypergraphic component faithfulness**: for
   every permitted atom subset `U`, the physical factor-component partition
   is exactly the partition induced by connectivity in `B(V,U)`.
2. The old/new gap alternatives have one common matching-seam signature,
   and their private attachments remain a forest on every permitted subset.
3. All physical supports and occurrence identifiers form one prepared
   product cube satisfying H0, H1, and H3--H5 of item 2189; its binary H2
   row is replaced by the hypergraphic component-faithfulness row in Item
   1.  Required residence, deep-shadow, socket/voltage, and compiler rows
   are included in that same state when they are in scope.
   The selected atoms obey (1.4) when the canonical collision signature was
   exported, or the exact recomputed postrepair conflict rows otherwise.
4. Every atom has a private router bank satisfying (5.3).
5. Relative to one root component, the eligible atoms satisfy the
   one-anchor frontier condition (3.4).

Then a greedy selection gives a spanning private coherent ECO hypertree.
Every selected port belongs to the same decoration, the factor becomes
connected, the gap forest and matching survive, and weighted router
resilience holds.  Under the stated full subset cube every ordering is
executable.  If the same hypotheses are verified only along the exact
greedy prefix chain, the conclusion is correspondingly only that this
greedy order is certified.

#### Proof

Theorem 3.1 constructs the incidence hypertree.  Owner alignment and the
matching-seam hypothesis keep the one decoration and residual matching on
every prepared prefix.  Coherence preserves both local palettes.
Hypergraphic component faithfulness makes each one-anchor atom merge its
`r_t` distinct current blocks.  Theorem 5.1 and Corollary 5.2 give router
resilience for the exhibited backbone.  The remaining
physical rows are assumptions of the same prepared state, so induction over
the greedy order completes the construction.  QED.

This is a dimension-uniform sufficient theorem.  The ECO supply theorem
on the raw canonical factor does not prove that the repair exports the
catalogue or that hypotheses 2--5 hold.

## 7. Sharp remaining obstructions

### 7.1 Rank-excess/Berge-cycle cut

On `V={1,2,3,4}`, take the two ternary supports

\[
                         \{1,2,3\},\qquad\{1,2,4\}.                \tag{7.1}
\]

Their two-section is connected, and both atoms are needed to reach vertices
`3,4`.  But for `A=V` the left side of (2.2) is `2+2=4>|A|-1=3`.
The incidence graph contains the four-cycle through component vertices
`1,2`.  Hence raw coherent two-section connectivity does not imply a
spanning incidence hypertree.

### 7.2 Decorated-private barren cut

Even when the raw ECO hypergraph crosses every component cut, owner masking,
occurrence resolution, matching-seam compatibility, or route capacity can
remove every usable atom across one cut.  A nontrivial component set with no
eligible crossing atom is a literal obstruction to (3.4) and to every
private coherent hypertree.

### 7.3 Phase anti-correlation

One abstract gap--colour owner edge may have two physical occurrences
`p,q`.  The coherent hex may require `p`, while the only private router
source occurs at `q`.  The owner projection and the route projection each
pass, but no occurrence-resolved atom passes both.  Thus the catalogue must
be intersected at the physical label level before applying any topology
cut.

### 7.4 Type separation

The six shared-decoration rows of the repaired `ML(7)` cycle are Hamilton
rethreads and have zero component rank.  Its splitting toggles have no
common decoration.  Neither supplies an ECO merge atom.  Item 2171 is the
separate positive binary `m=4` merge calibration.

### 7.5 The raw canonical `m=5` owner obstruction

The exact audit
`MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`
closes the unrepaired route.  The raw factor has three components and `45`
distinct ECO atoms.  All `648` legal ordered two-atom Hamiltonizations
have disjoint six-port sets and disjoint forced faces on both shores, so
they satisfy the stronger literal conclusion of collision-freedom.  (The
rows (1.4) themselves are only the single fixed-rotation encoding, whereas
this census uses all rotations.)  Nevertheless
every endpoint realizes only `81/84` turn colours on each shore and misses

\[
 \mathcal R^+=\{219,365,438\},\qquad
 \mathcal R^-=\{73,146,292\}.                       \tag{7.2}
\]

No upper transversal exists, so owner alignment cannot even be formed.
This is not a defect of the weighted topology cuts: it proves that the
controlled repair in (0.1) is logically prior to owner Hall.  It does not
exclude a repaired endpoint; the synchronized repaired `m=5` fixture is
positive on the leaf-owner face.

### 7.6 The repaired `m=5` endpoint realizes the order exactly

The subsequent exact finite theorem
`MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`
shows that the qualification in Section 7.5 is essential.  Apply the
synchronized three-`C10` repair first and delete the two old standard glues.
The resulting pre-glue factor has two components of orders `120,132`, a
forest gap graph, and one unique perfect matching.  All five fixed-rotation
ECO atoms survive the repair support and each merges those two components
into one Hamilton cycle.  Exactly the four atoms

\[
              110100,\qquad110010,\qquad101100,\qquad101010              \tag{7.3}
\]

are all-six marked and pointwise owner-aligned in that same matching.  The
atom `101100` is isolated in the fixed-rotation support-conflict graph; the
nonstandard atom `110100` gives a second one-atom witness outside the four
old standard-cube endpoints.  In either case the component--atom incidence
graph is a three-vertex tree, so Theorems 2.1 and 3.1 are realized literally.

This proves the finite implication

\[
  \text{controlled repair}\Longrightarrow
  \text{collision-free, owner-aligned ECO hypertree}              \tag{7.4}
\]

at the first raw-obstructed dimension.  It does **not** prove that an
arbitrary recursive repair exports such an atom bank, nor does it construct
the uniform occurrence channel needed for the all-`m` router theorem.  The
finite toggle itself is unconditional because its physical endpoint and
the unchanged decoration are replayed directly.

## 8. Exact remaining all-`n` gate

The coherent ECO theorem proves the raw unfiltered input and the common
local collision forest.  The minimal direct two-atom unrepaired canonical
ECO-hypertree route is refuted at `m=5`, while Section 7.6 proves that the
repair-first route succeeds there.  The all-`m` extension remains live.
A complete recursive construction must now produce a controlled repair
endpoint and then one same-decoration atom family satisfying

\[
 \begin{array}{ll}
 \text{local packing:}&\text{the exported path-forest rows (1.4), or the}\\
                     &\text{exact recomputed postrepair conflict rows;}\\
 \text{topology:}&\text{(2.2)--(2.3), or the one-anchor condition (3.4);}\\
 \text{matching:}&\text{literal owner alignment plus a stable matching seam;}\\
 \text{routing:}&\text{private kill cost }w_t=|S_t|-1;\\
 \text{physics:}&\text{H0,H1,H3--H5 plus hypergraphic faithfulness in}\\
               &\text{place of binary H2, with all carried}\\
                 &\text{residence/deep-shadow/socket/compiler guards.}
 \end{array}                                                       \tag{8.1}
\]

The first violated weighted forest cut is an exact topology obstruction;
the first owner/route-filtered frontier with no one-anchor atom is an exact
constructive obstruction.  No all-`n` proof of (8.1), and therefore no
exact-equality or coefficient-one conclusion, is claimed.

## 9. Dependencies

* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`;
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_COHERENT_COLLAR_LEAF_EXTENSION_20260731.md`;
* `MATH_THEOREM_D_PRIVATE_COHERENT_COLLAR_STATE_AND_SUPPLY_OBSTRUCTION_20260731.md`; and
* `MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md`.
