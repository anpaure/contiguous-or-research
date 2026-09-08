# Ordered fixed-decoration transparent gluing after router repair

Date: 2026-07-31  
Status: exact dimension-uniform conditional theorem on the prepared
private/aligned graphic--gammoid face; no all-`m` catalogue,
run-redistribution, or compiler existence theorem

## 0. Verdict

Suppose a debt-carrying repair packet has terminated in one fixed decorated
factor with `q` components.  Freeze one complete correlated signature for
each later collar.  On the prefix-closed face where

1. the same occurrence-labelled decoration survives every permitted cube
   edge;
2. collar component effects are the edges of one graphic matroid;
3. occurrence-gap updates are globally private, or their only effective
   edges are aligned with those component edges;
4. occurrence transfers are sources in one fixed unpaired-sink gammoid; and
5. the directed boundary-reachability test is redundant on every
   component-forest prefix,

there is an ordered component-spanning transparent list if and only if

\[
 \boxed{
 r_C(X)+r_L(T\setminus X)\ge q-1
 \quad\text{for every }X\subseteq T.}                \tag{0.1}
\]

Here `M_C` is the component graphic matroid and `M_L` is the fixed-network
gammoid.  Edmonds supplies a common basis of size `q-1`.  In fact, every
ordering of every such basis is valid: every prefix merges two actual factor
components, preserves the same decoration, has a leaf-peelable occurrence-
gap forest, retains a sublinkage of one simultaneous linkage, and stays
directed-acyclic.

The fifth hypothesis cannot be suppressed.  Exact determinant contraction
adds an arc `T_t -> H_t` only when the current retained graph has no path
`H_t -> T_t`.  Two individually safe reciprocal arcs already give a
two-label catalogue satisfying every row of (0.1) but admitting no complete
order.

Thus the theorem closes the **ordering implication after repair**.  It does
not prove that the required repaired catalogue exists in every dimension.

## 1. Prepared prefix-closed collar face

Let `F_empty` be a factor whose set of connected components is `Q`, with
`|Q|=q`.  Let `T` be a finite set of collar labels.  The following
hypotheses define the theorem's face.

### H0. One complete correlated signature per label

For each `t` in `T`, freeze its physical ports, old and new local incidences,
selected occurrence identifiers, component edge, occurrence-gap update,
linkage source, and directed boundary effect.  Distinct labels may share
only declared public boundary objects; their private interiors are
disjoint.

For every component-independent set `U` defined below, these frozen toggles
have a literal order-independent superposition `F_U`.  Every pending collar
port remains live.  Future operations neither reopen a sealed fragment nor
delete an undeclared hidden edge.  Thus subset state, rather than prefix
word, is sufficient.

This is a correlation hypothesis.  If one label still has alternative
decorations, roots, terminal pairs, or linkage modes, expanding those modes
creates an at-most-one-per-label partition row in addition to `M_C` and
`M_L`.  Ordinary two-matroid intersection is then not exact unless the
alternatives are first resolved by a separate bounded-state computation or
have one deterministic common effect.

### H1. One fixed decoration on the full permitted Boolean interval

Fix one occurrence-labelled decoration

\[
                         D=(D_A,D_B)                 \tag{1.1}
\]

of `F_empty`.  It has the two complete turn palettes, alternating selected
shore types on every factor component, and its selected occurrence matching
is perfect.

For every component-forest state `U` and every `t` not in `U` for which
`U+t` is again a component forest, evaluate the collar on the **current**
state `F_U`.  Require both exact transparent-transfer rows:

* separately on the two shores, the selected local turn-colour multisets
  before and after the toggle agree; and
* on every retained fragment, store the first and last selected shore type
  in \(\{A,B,\bot\}\).  After reconnection, consecutive nonempty fragments meet
  in opposite types.

Occurrence identifiers are stable across the whole cube.  In particular,
the condition is not merely “`D` works at the root and after each
singleton.”  It holds on every subset of every possible common basis.

The transparent-transfer theorem then proves inductively that the same `D`
decorates every `F_U`.  No palette or occurrence-matching debt is carried by
these collars.  A `C8`/`C10` repair packet whose intermediate states are not
decorated belongs before this face and is contracted only after its terminal
debt is zero.

### H2. Exact component-graphic superposition

Each label has a nonloop edge

\[
                         c_t=u_tv_t                 \tag{1.2}
\]

in a multigraph `K_C` on `Q`.  Let `M_C` be the pullback of the graphic
matroid of `K_C` to the labels `T`.

For every \(U\in I(M_C)\), the actual components of `F_U` are exactly the
blocks obtained by joining the original components along the edges
\(\{c_t:t\in U\}\).  Consequently, if `U+t` is independent, applying `t`
merges exactly the two current blocks containing `u_t,v_t` and splits or
changes no other block.  This is **component faithfulness**, stronger than
assigning a terminal component label to a move.

### H3. Exact private/aligned occurrence-gap superposition

Let `Gamma_U` be the occurrence-labelled gap--colour graph induced by `D`
on `F_U`.  Its perfect matching is the matching transported by `D`.
Forest is meant in the occurrence-labelled multigraph sense: a loop or two
parallel quotient edges is already a cycle.
The gap row is redundant on `I(M_C)` under either of the following exact
preparations.

**Globally rooted-private cube.**  There is a fixed forest `Gamma^circ` and,
for every label `t`, a globally private vertex bank `P_t`, one possible
fixed-core root `r_t`, and two rooted forests `B_t^0,B_t^1` on
\(P_t\cup\{r_t\}\) such that

\[
 \Gamma_U=\Gamma^\circ
       \cup\!\bigcup_{t\notin U}B_t^0
       \cup\!\bigcup_{t\in U}B_t^1.                \tag{1.3}
\]

The banks `P_t` are pairwise disjoint, and each alternative meets the
entire nonprivate and other-label graph only at `r_t`.  Empty alternatives
and roots are allowed.  The matching transported by `D` is a perfect
matching of every graph in (1.3).

**One-effective-edge aligned cube.**  After the exact old-edge deletion and
retained-forest contraction of the leaf-transfer theorem, every nonprivate
effect of `t` is one edge `g_t`.  There is an injective map of component
anchors such that

\[
        c_t=uv\quad\Longrightarrow\quad
        g_t=\iota(u)\iota(v),                       \tag{1.4}
\]

and every remaining piece is a globally rooted-private forest as above.
The fixed contracted core contains no extra path that identifies two
distinct `iota`-blocks.  Hence a component forest has a loopless, acyclic
gap attachment quotient.

In either case `Gamma_U` is a forest for every \(U\in I(M_C)\).  Global
privacy matters: two bundles can each be trees and nevertheless form the
cycle `u-g_1-v-g_2-u` if both meet the core at two vertices.

### H4. One fixed unpaired-sink linkage gammoid

Freeze a vertex-capacitated directed network `N`, a sink bank `Z`, and one
source `s_t` for each label.  Define

\[
 I(M_L)=\{U\subseteq T:\{s_t:t\in U\}
   \text{ link vertex-disjointly to distinct sinks in }Z\}. \tag{1.5}
\]

This is a gammoid.  A linkage in `N` is, by preparation, an exact occurrence
transfer and has no unrecorded effect on `D`, components, gaps, or directed
boundary reachability.  The network and sinks do not depend on the selected
set or its order.

Named source--sink pairing is stronger than (1.5), and two inseparable
sources for one label are a grouped pullback rather than this gammoid face.
Those cases require their pairing-resolved boundary relation.

### H5. Boundary reachability is redundant on common-independent sets

After contracting each internally acyclic collar, its only effective
cross-boundary directed edge is

\[
                         a_t:T_t\longrightarrow H_t. \tag{1.6}
\]

The retained directed state has the same subset superposition as `F_U`.
The root retained support is acyclic.  For every pair `(U,t)` for which
`U+t` is independent in both `M_C` and `M_L`, first include the label's
fixed passive internal relation and require that this passive insertion is
itself acyclic.  Let
\(\rho_U^{[t]}\) be the resulting transitive boundary reachability relation.
Then require

\[
 (H_t,T_t)\notin\rho_U^{[t]}                       \tag{1.7}
\]

for every such pair.  Thus the directed row is prefix-closed but contributes
no third selection constraint on the common-independent family.

Two useful structural certificates for (1.7) are:

1. **one global topological potential:** every retained and collar arc
   strictly increases the same potential;
2. **reachability--component alignment:** whenever a prefix contains a path
   `H_t -> T_t` after the pending passive relation is included, its
   projection contains a component-edge path between `u_t` and `v_t`.
   Then \(U+t\in I(M_C)\) forbids such a path.

The second is the weaker certificate relevant to component merging.  If a
collar has several effective boundary arcs, it must carry and compose its
full atomic boundary relation.  Splitting it into single arcs is valid only
when every intermediate correlated signature is itself a permitted state.

## 2. Static rank theorem

### Lemma 2.1 (Edmonds common-basis criterion)

There is a set `S` of size `q-1` independent in both `M_C` and `M_L` if and
only if (0.1) holds.

#### Proof

Edmonds' matroid-intersection theorem gives

\[
 \max\{|S|:S\in I(M_C)\cap I(M_L)\}
 =\min_{X\subseteq T}
       \bigl(r_C(X)+r_L(T\setminus X)\bigr).        \tag{2.1}
\]

The component rank is at most `q-1`.  Hence the right side is at least
`q-1` exactly when a common independent set of that size exists.  The cut
`X=T` then forces `r_C(T)=q-1`; a size-`q-1` component forest on `q`
vertices is a spanning tree.  \(\square\)

Choose once and for all a simultaneous linkage

\[
             {\cal P}_S=\{P_t:s_t\leadsto z_t:t\in S\}       \tag{2.2}
\]

to distinct sinks.  Every prefix uses a subfamily of this same linkage.
No nested maximum matching or new route choice is required.

## 3. Ordered transparent gluing theorem

### Theorem 3.1

Under H0--H5, the following are equivalent.

1. There is an ordered list of `q-1` collars whose final occurrence
   transfers are simultaneously feasible, and every prefix is a fixed-`D`
   transparent component merge with a leaf-peelable gap graph and acyclic
   retained directed support.
2. `M_C` and `M_L` have a common independent set of size `q-1`.
3. The rank inequalities (0.1) hold for all \(X\subseteq T\).

Moreover, **every ordering of every common set in item 2 is valid**.  One
may therefore root its spanning tree, repeatedly peel a leaf edge, and use
either the resulting order or its reverse as a deterministic gluing list.

#### Proof

Items 2 and 3 are equivalent by Lemma 2.1.  Let `S` be a common set of size
`q-1`, and enumerate it arbitrarily as
\(t_1,\ldots,t_{q-1}\).  Put \(U_i=\{t_1,\ldots,t_i\}\).

Every subset of a tree is a forest.  If the endpoints of \(c_{t_i}\) were
already joined by \(c(U_{i-1})\), that prefix path together with \(c_{t_i}\)
would be a cycle in `S`.  H2 therefore makes the physical toggle merge
exactly two current factor components, so their number is `q-i`.

H1 applies the exact local palette-multiset and retained-fragment boundary
tests on the current cube edge.  Hence the same occurrence-labelled `D`
decorates \(F_{U_i}\); in particular its selected occurrence matching stays
perfect.

By H3, \(\Gamma_{U_i}\) is a forest.  A finite forest with a perfect matching
has a forced matching edge at every leaf; deleting that leaf and its mate
recursively recovers the whole matching.  Thus the gap graph is
leaf-peelable at every prefix.

The linkage (2.2) restricted to \(U_i\) remains vertex-disjoint and ends at
distinct sinks.  Finally, H5 gives the exact no-\(H_{t_i}\)-to-\(T_{t_i}\)
test, so adding the collar arc cannot close a directed cycle.  All five
invariants therefore hold by induction.  The last state is connected.

Conversely, an accepted `q-1`-step list merges the initial `q` components at
every step, so H2 makes its component edges a spanning tree.  Its final
simultaneous occurrence transfer is a linkage in the fixed network, hence
its label set is independent in `M_L`.  It is the common set of item 2.
\(\square\)

This theorem is dimension-uniform.  If repaired entrances and catalogues
satisfying H0--H5 and (0.1) are constructed for every `m`, their router
prefixes followed by these lists give connected fixed-decoration,
leaf-peelable states in every `m`.  The theorem does not construct those
entrances or catalogues.

## 4. Exact reachability composition and the first obstruction

Let \(\rho\) be the strict transitive reachability relation on the current live
boundary, and let \(\rho^*\) be its reflexive closure.  For one pending arc
`T_t -> H_t`, legality is exactly

\[
                         (H_t,T_t)\notin\rho.        \tag{4.1}
\]

After a legal insertion,

\[
 \rho'=\rho\ \cup
 \{(x,y):x\mathrel{\rho^*}T_t
          \text{ and }H_t\mathrel{\rho^*}y\}.       \tag{4.2}
\]

Take transitive closure before forgetting any port which ceases to be live.
Formula (4.2) is exact because an acyclic new path uses the new arc at most
once.  With a passive internal relation, first replace `rho` by its
transitive closure with that relation.

### Proposition 4.1 (Edmonds cuts do not imply shellability)

Among root-safe instances satisfying (0.1), two labels are sufficient and
necessary for a failure caused solely by ordering.

#### Proof

Take `q=3` and two labels `a,b` whose component edges are the two edges of a
three-vertex path.  Make the gap atoms globally private and take
\(M_L=U_{2,2}\).  Then \(M_C=U_{2,2}\), and for every
\(X\subseteq\{a,b\}\)

\[
        r_C(X)+r_L(\{a,b\}\setminus X)=2=q-1.       \tag{4.3}
\]

Let the initial directed boundary have two isolated ports `x,y`.  Label `a`
inserts `x->y`, and label `b` inserts `y->x`.  Each is legal at the root.
Whichever is installed second sees the reverse path created by the first
and closes a directed two-cycle.  Thus the unique common basis is not
shellable.  With one root-safe label there is no second insertion, so this
is minimal in that class. \(\square\)

In the unrestricted face, the exact selection statement is therefore

\[
 \text{there exists a size-`q-1` common independent set which admits an
 ordering satisfying (4.1) at every prefix}.        \tag{4.4}
\]

That is a state-router or greedoid-type row, not one more Edmonds rank
partition.  Predecessor-rooted collars reduce to Theorem 3.1 only when every
selected basis is predecessor-closed and its dependency digraph is
automatically acyclic.

## 5. Lean inductive collar state

There is no absolute “weakest state” without fixing the permitted future
operations.  For bounded-boundary composition by occurrence-labelled
transparent collars, gap-forest updates, linkage transfer, and directed
edge insertions, a proof-sufficient correlated state is

\[
 \boxed{
 \Sigma=(\delta_\partial,\theta_\partial,\pi_C,
          \pi_\Gamma,\mu_\Gamma,\Lambda_\partial,\rho_\partial).}       \tag{5.1}
\]

The coordinates are:

* `delta_partial`: stable selected occurrence identifiers, shores, and
  current local turn-colour ownership at exposed ports;
* `theta_partial`: the first and last selected shore type in
  \(\{A,B,\bot\}\) on every retained fragment;
* `pi_C`: connectivity of live factor-component anchors;
* `pi_Gamma`: occurrence-labelled connectivity of the exposed gap forest;
* `mu_Gamma`: the exact exposed partial matching/mate relation, including
  which boundary occurrence is matched to which retained mate (equivalently,
  fixed mates together with the residual unmatched colour bank);
* `Lambda_partial`: the exact feasible relation of exposed disjoint
  linkages, including named pairings if the continuation asks for them; and
* `rho_partial`: the full directed reachability relation on live physical
  ports.

These coordinates must be carried as one correlated relation if their
physical resources overlap.  Independent feasible projections are not an
exact interface in that case.

The selected prefix `U` is retained as finite control state.  On the
prepared face H0--H5, the remaining state compresses: `D` and its boundary
trace have deterministic subset updates; the private/aligned gap state is a
deterministic image of `U` and `pi_C`; and the fixed unpaired network reduces
`Lambda_partial` to the chosen source subset and one gammoid oracle.  The
only genuinely dynamic relations left are the component partition and
boundary reachability, with H5 making the latter selection-redundant.

Call two states completion-equivalent when every compatible continuation
built from the declared primitive boundary operations accepts both or
neither.  Relative to the **universal** family of such future pair queries,
each displayed field is necessary in the following separator sense.  This
is not a claim of joint or bitwise minimality:

1. palette ownership and fragment endpoint types are separately necessary
   by the fixed-decoration transparent criterion;
2. states differing on whether component anchors `u,v` are joined are
   separated by appending the edge `uv`;
3. states differing on whether gap ports `u,v` are joined are separated by
   appending one gap edge;
4. states with the same gap partition but different exposed partial mates
   in `mu_Gamma` are separated by attaching a private leaf through an
   occurrence which is free in one state and already committed in the
   other;
5. states differing on `u -> v` reachability are separated by appending
   `v->u`;
6. a scalar linkage deficiency or independent terminal-reachability bits
   cannot distinguish named pairings or simultaneous routes sharing a
   bottleneck; and
7. occurrence labels cannot be quotiented to anonymous endpoint pairs,
   because parallel occurrence gaps may form a literal two-cycle.

For one fixed finite catalogue, the exact Myhill--Nerode quotient of these
relations may be smaller: only future distinctions which the catalogue can
query need be retained.  Thus (5.1) is a universally exact lean relational
interface, not a claim that every instance needs every bit of every full
relation.

For a bottom-up open gap node, `mu_Gamma` is essential.  If future moves may
delete hidden retained edges, one must additionally carry the full exposed
forest or its exact deletion-response table.  If physical linearity is part
of the target, append the exact binary-trace cycle-face bit (or a protected
literal run).  Socket pairing and voltage, deeper shadows, residence, and
compiler envelopes are downstream coordinates, not consequences of (5.1).

## 6. Relation to the all-`k` repair-and-glue programme

The correct recursive order is now exact:

1. an ordered controlled-debt packet of bounded-port circuits carries the
   full correlated boundary state and may be undecorated at intermediate
   prefixes;
2. only after its debt is zero does one freeze `D` and the prepared collar
   ground;
3. the Edmonds rows (0.1), together with H0--H5, select and order the
   transparent component-spanning list; and
4. residence-compatible run redistribution, all-depth connector chronology,
   and the common-cap compiler remain separate.

Item 2184's Pascal determinant split explains why step 1 cannot be replaced
by two scalar full-parent copies: exact contraction must remember both
acyclicity and `H->T` reachability.  Item 2187R proves that a cyclic Catalan
linear matching has average run length exactly `m`, so residence has
aggregate margin rather than an intrinsic central capacity obstruction.
Item 2188 then supplies a genuine `m=5` interior rethread with exact immediate
palettes and internal minimum run three.  Its 21 deeper-target debts and
unjoined endpoint runs show the remaining finite interface precisely:
choose an all-depth, residence-compatible connector chronology, then pass the
compiler.  No new finite `m=5` claim is made here.

Accordingly, Theorem 3.1 is the requested postrepair recursive gluing
theorem, not a proof of `nu(k)=B(k)` for new `k`.

## 7. Authoritative inputs

The proof uses the following frozen results, without strengthening their
scope:

* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`,
  SHA-256
  `3c5007b3759e94a635593eaf83980dd93819c7f3d9bf8e280ab50fa46678b6e2`,
  for fixed-decoration transparency and the exact leaf-transfer test;
* `MATH_THEOREM_CATALAN_JOINT_GRAPHIC_GAMMOID_GLUING_FACE_20260731.md`,
  SHA-256
  `b0595b2dd109f92ef17fbd5ee43d29554ea3bb09c542df8fdc689b3195e3e82e`,
  for the private/aligned two-matroid face and Edmonds reduction;
* `MATH_THEOREM_CATALAN_PASCAL_SECTOR_DETERMINANT_AND_TWO_COPY_NOGO_20260731.md`,
  SHA-256
  `a4c89a962b59eac35556e7c4c1fab42bf24757ec86029e4d691bfd43a9380659`,
  for the exact no-`H->T` contraction row; and
* `MATH_SYNTHESIS_SHORTEST_ALLK_CHAIN_AND_EXACT_MISSING_THEOREM_20260731.md`,
  SHA-256
  `41825e4e960a461ebea067913bec3cd57a28c09269b55f548ff4ed12353e4356`,
  for the controlled-debt/router and residence scope boundary.
* `MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md`,
  SHA-256
  `e1e0ddae1289a91d6912e07e0b1e1ca7f2728eb1640e7f3c6e08b18d48e96d48`,
  for the all-`m` seam-run ledger; and
* `MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md`,
  SHA-256
  `5e0aa50a965cee30ea9848fbe1f90d9b71b36b3d6e3b3ed7df21c6d57f32f5a2`,
  for the independently replayed finite `m=5` residence rebase.

The finite obstruction in Proposition 4.1 is replayed by
`scratch/audit_catalan_ordered_transparent_reachability_counterexample_20260731.py`,
SHA-256
`4fedea9090813b098486b1be90b73a5e6b9cb65bdff696ae629997cc0dd08724`.
Its canonical payload SHA-256 is
`103d19c3520e76edae5565037a18ac6e2c44ed94e6589ce397b20b6217a2dc8f`.
