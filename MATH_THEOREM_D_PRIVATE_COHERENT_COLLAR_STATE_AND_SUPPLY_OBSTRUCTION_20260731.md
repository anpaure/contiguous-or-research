# Private coherent collars: the closed recursive state and its first supply obstructions

Date: 2026-07-31  
Status: exact conditional preservation theorem on a fixed component tree;
exact minimal abstract owner-drift and router-sharing obstructions; exact
all-dimension raw coherent ECO component supply; no all-`m` compatible
private hypertree theorem

## 0. Verdict

The leaf-forest owner theorem and the private-router tree theorem compose
without another Hall or min-cut calculation, but only after one carries the
following **joint private coherent collar** state.

* The gap/colour coordinate is one fixed upper transversal, one
  occurrence-labelled decoration, and private old/new matched-forest blocks
  having the same full occurrence-labelled boundary matching transfer.
* The occurrence-router coordinate is one fixed private source--sink path
  for every component-tree edge.
* The physical coordinate is a component-faithful coherent all-six toggle
  with a fixed common exterior on the whole declared product cube.

Under these hypotheses every component-tree order preserves the state.  In
particular, owner alignment is checked once, before the first merge, and
router resilience follows from the additive damage identity.

The matching and routing privacies are orthogonal.  Matching-private colour
triples do not make occurrence paths disjoint, and disjoint occurrence paths
do not put forced lower ports on their unique matching owners.  The remaining
constructive problem is therefore **joint supply** of physical collars which
have both signatures at once.  Separate marginal catalogues do not combine.

Raw coherent abundance itself is no longer the gate.  The canonical MMM
labels are coherent only in the degree-two-parent case, so their standard
arborescence is unusable.  However, the explicit coherent ECO hexagon of
every Dyck parent shadows every standard MMM pull adjacency, and the
two-section of the resulting component hypergraph is connected in every
dimension.  The live problem is to extract from this connected raw supply a
simultaneously compatible ECO hypertree carrying the two private signatures
and the common matching-seam state.

There is also one dynamic condition which cannot be omitted: the private
matched-forest decomposition, including the common exported boundary
matching signature, must hold on the whole cube.  Otherwise a preceding
toggle can change the unique owner of a later forced port.  The smallest
two-boundary obstruction has two gaps and two colours.

## 1. The recursive state

Let `Q` be the components of a prepared alternating factor and let `J` be a
tree on `Q`.  Its edge set is denoted by `T`; edge `t` is intended to be one
component merge.

Fix one upper occurrence transversal `I`.  For every state below, the
selected lower occurrences together with `I` form the same
occurrence-labelled decoration `D` transported through the toggles.

### 1.1 Matching-private banks

Fix a core gap--lower-colour forest `Gamma^circ` with an
occurrence-labelled matching `M^circ`.
For every `t in T`, choose a private vertex set `V_t`, a root `r_t`, and two
rooted forest alternatives

\[
                 (B_t^0,M_t^0),\qquad (B_t^1,M_t^1).             \tag{1.1}
\]

Require the following.

1. The sets `V_t` are pairwise disjoint, the roots `r_t` are distinct,
   `V(B_t^epsilon)=V_t union {r_t}`, and `B_t^epsilon` meets the core and
   every other bank only at `r_t`.
2. `M_t^0` and `M_t^1` match every vertex of `V_t` and export the same full
   occurrence-labelled boundary matching transfer.  In the literal
   one-root projection, either both cover `r_t`, or both leave it to
   `M^circ`.  The core covers `r_t` exactly in the latter case and does not
   cover it in the former case.  The matching `M^circ` saturates every
   other core vertex.
   Occurrence labels are part of this record: `M_t^0` and `M_t^1` are the
   gap incidences of the same fixed selected lower occurrences in the two
   alternatives, not merely abstract matchings of equal size.
3. The three forced lower-port edges `F_t` of collar `t` are edges of
   `M_t^0`.  They have distinct gap and colour endpoints.  Its three forced
   upper ports belong to `I`.

For `U subseteq T`, define

\[
 \Gamma_U=\Gamma^\circ\cup
       \bigcup_{t\notin U}B_t^0\cup
       \bigcup_{t\in U}B_t^1,
 \qquad
 M_U=M^\circ\cup
       \bigcup_{t\notin U}M_t^0\cup
       \bigcup_{t\in U}M_t^1.                    \tag{1.2}
\]

The full occurrence-labelled transfer in Item 2 is the **matching seam
state**.  Root coverage is only its one-root projection, not a sufficient
general boundary summary.  Literal one-root attachment is a convenient
sufficient syntax; the more general H3 one-effective-edge-aligned cube may
replace it without changing the theorem.

### 1.2 Coherent physical signatures

For every `t`, freeze one all-six incidence hexagon and all its occurrence
identifiers.  Require:

* its three lower external add labels are equal and its three upper external
  delete labels are equal;
* its effective component edge is exactly the edge `t` of `J`;
* the physical supports of distinct collars are disjoint except for declared
  inert boundary objects; and
* on every subset state `U` not containing `t`, the same six ports and the
  same external labels remain present, and toggling `t` changes the physical
  component partition exactly by adding the edge `t`.

The last two bullets are the literal product-cube and component-faithfulness
assumptions.  Root-only coherence is not enough.

### 1.3 Route-private banks

For every `t`, freeze a directed occurrence path

\[
                         Q_t:s_t\leadsto z_t                 \tag{1.3}
\]

to a dedicated sink.  The paths `Q_t` are pairwise vertex-disjoint and are
unchanged on the physical product cube.  Internal child-router banks, if
present, are disjoint from all `Q_t`.

No identification is made between the vertices of `V_t` and the vertices of
`Q_t`.  The former certify gap/colour ownership; the latter carry literal
occurrence capacity.  If a physical construction lets the two systems
overlap, that overlap must be certified separately rather than inferred
from colour equality.

## 2. Exact preservation theorem

### Theorem 2.1 (private coherent collar recursion)

Assume the state of Section 1 and the remaining fixed-decoration trace and
directed-reachability guards of the prepared H0--H5 face.  Then, for every
`U subseteq T`, the following assertions hold.

1. The physical components are the components of the forest `J[U]`, hence
   their number is `|Q|-|U|`.
2. `Gamma_U` is a forest and `M_U` is its unique perfect matching.
3. The same decoration `D` decorates the physical state.  For every pending
   collar `t notin U`, its forced lower edges satisfy
   `F_t subseteq M_U`, and all six of its ports are selected by `D`.
4. Every pending collar is a fixed-`D` transparent merge.
5. For a router deletion set `Y`, let the certified private backbone
   `J^Q[U]_Y` retain an edge `t in U` exactly when `Q_t` avoids `Y`.  Then

   \[
      c(J^Q[U]_Y)-c(J[U])
       =|\{t\in U:V(Q_t)\cap Y\ne\varnothing\}|
       \le |Y|.                                      \tag{2.1}
   \]

Consequently every ordering of `T` is an accepted coherent merge order.  The
actual surviving catalogue contains the certified backbone (a source may
have additional routes).  At the final state, therefore,

\[
                 c(K_Y)\le c(J^Q[T]_Y)\le |Y|+1,     \tag{2.2}
\]

so forced-port Hall and router resilience are both already closed.

#### Proof

A one-point union of forests is a forest.  Thus (1.2) is a forest for every
`U`.  The equal boundary matching signatures imply that the displayed
`M_U` covers each root exactly once and every private vertex exactly once;
it is a perfect matching.  A forest has at most one perfect matching, so it
is unique.

If `t notin U`, the whole `t` bank is still in alternative zero.  Other
bank replacements are disjoint from it, hence

\[
                         F_t\subseteq M_t^0\subseteq M_U.     \tag{2.3}
\]

The leaf-forest forced-port theorem now says precisely that the pending
forced lower ports are owned by their gaps.  Their upper ports lie in `I`,
so they are all selected by `D`.  Coherence gives the two shore-palette
equalities, and the all-six boundary alternation is automatic.  The product
cube assumption keeps the common exterior and occurrence identifiers fixed.
Therefore toggling `t` transports the same `D` and replaces only
`B_t^0` by `B_t^1`.

Because `J` is a tree, adding an unused edge to `J[U]` joins two different
current blocks.  Component faithfulness makes the physical operation one
merge.  Induction proves Items 1--4 in any order.

Finally, `J[U]` is a forest, so deleting `d` of its edges raises its
component count by exactly `d`.  An edge is lost only when its private path
meets `Y`.  Pairwise path disjointness injects lost edges into vertices of
`Y`, proving (2.1).  For `U=T`, `c(J)=1`; the actual survivor graph contains
this private-path survivor, so (2.2) follows.  \(\square\)

### Corollary 2.2 (ordered recursive construction)

The same conclusion holds for a rooted block tree.  Each child may already
carry a state satisfying Theorem 2.1 in a disjoint internal router and gap
bank.  Join the child blocks by a tree of new collars satisfying Section 1
relative to the union state.  Internal damage and bridge damage add on the
certified tree-sum backbone:

\[
 c(\widehat K_Y)-1
 =\sum_i(c((K_i)_{Y_i})-1)
   +\#\{\hbox{new private bridge paths hit by }Y\}.              \tag{2.4}
\]

The actual catalogue may contain extra surviving labels, in which case only

\[
 c(K_Y)-1\le c(\widehat K_Y)-1                                  \tag{2.5}
\]

is asserted; extra edges may merge components but cannot increase their
number.

Thus any bottom-up order, and in fact any order permitted by the physical
product cube, preserves the joint collar state.  This is a preservation
lemma, not a source of new parent collars.

## 3. The first dynamic obstruction: owner drift

Root owner alignment does not by itself give Theorem 2.1.  The old/new
blocks must form the private one-root product of Section 1 (or pass the full
H3 cube), including the same matching seam state.

Take two gaps `g_1,g_2` and two colours `c_1,c_2`.  Let

\[
 \Gamma_0=\{g_1c_1,g_2c_2\},\qquad
 \Gamma_1=\{g_1c_2,g_2c_1\}.                       \tag{3.1}
\]

Both graphs are forests and each has a unique perfect matching.  In the
root state the prospective later port `g_2c_2` is owner-aligned.  After the
first replacement its gap owner is `c_1`, and `g_2c_2` is not even present.
Hence there is no single transported decoration selecting that later port
on both states.

This exchange uses two boundary vertices of the later owner block; it is
therefore excluded by the disjoint one-root banks in Section 1.  Its role is
to show why endpoint leaf-forest checks and root ownership cannot replace
that collective private-product hypothesis.  A genuinely private one-root
bank still needs the common root-coverage bit so that the displayed global
matching covers the attachment exactly once in both alternatives.

This is the smallest possible owner-drift witness: one gap and one colour
have only one matching.  It shows that the following weaker induction is
false:

> every endpoint gap graph is leaf-peelable, and every collar is
> owner-aligned when first listed at the root.

The private one-root decomposition with its common boundary matching
signature, or the full fixed-`D` H3 cube, rules out (3.1).  This obstruction
is in the abstract occurrence-gap state; no claim is made here that (3.1)
alone is a physical incidence-hex realization.

## 4. Orthogonal route obstruction

Owner alignment does not control route damage.  On the component path
`1-2-3`, let both coherent owner-aligned collar sources traverse the same
unit router vertex `v`.  Every forced colour and gap can be private, but
deleting `v` kills both tree edges and leaves three components:

\[
                         3>|\{v\}|+1=2.              \tag{4.1}
\]

Conversely, pairwise-disjoint occurrence paths say nothing about whether a
forced edge lies in the unique matching.  Thus neither privacy coordinate
may be dropped or used as a proxy for the other.

## 5. Exact remaining supply obstruction

For a desired scaffold edge `e`, let `H_e` be its literal coherent merge
options.  A candidate `h` has two independent resource signatures:

\[
 B(h)=\{\hbox{forced gap/colour owner edges and private bank}\},
 \qquad
 R(h)=\{\hbox{vertices of its occurrence route}\}.              \tag{5.1}
\]

After coherence and component-faithfulness have been checked, construction
of the state in Section 1 is exactly selection of one `h_e in H_e` for each
tree edge so that

\[
 B(h_e)\cap B(h_f)=\varnothing,\qquad
 R(h_e)\cap R(h_f)=\varnothing                         \tag{5.2}
\]

for distinct edges, together with the common matching-seam and product-cube
guards.  This is a correlated two-resource packing problem.  It is not
another forced-port Hall problem and not another router min-cut problem.

The minimum marginal-versus-joint obstruction has two scaffold tasks.  Let
the first task have only signature `(A,x)` and the second have alternatives
`(A,y)` and `(B,x)`, where `A,B` are disjoint matching banks and `x,y` are
disjoint route banks.  Matching privacy alone chooses `(A,x),(B,x)`;
route privacy alone chooses `(A,x),(A,y)`; no joint pair exists.  The absent
rectangle corner `(B,y)` is exactly the missing physical collar.

There is also a scalar necessary condition.  If selected all-six collars
have disjoint physical ports and the decoration has `P` selected occurrences
on each shore, a tree on `q` components consumes three fresh ports per shore
per edge, so

\[
                              3(q-1)\le P.             \tag{5.3}
\]

This bound is not the obstruction for the standard Catalan plane-tree count
from `m>=4`, but it is an exact no-go for denser component factors on the
strict private face.

Therefore the smallest noncircular recursive target is not “prove Hall and
router again.”  It is one of the following literal supply statements.

1. **Parent-total collar grammar:** every admissible pair of child terminal
   modes has a coherent component-faithful parent collar with a fresh owner
   bank, a fresh occurrence route, and the same exported matching seam
   state.
2. **Rectangle closure:** the physical collar catalogue factors sufficiently
   between matching-bank choices and route-bank choices to fill every needed
   corner such as `(B,y)`.
3. **Bounded-pressure selection:** candidate lists are large enough, and
   their two-resource conflict graph sparse enough, to select a spanning
   tree while preserving one fixed decoration and product cube.

Any one of these supplies the hypotheses of Theorem 2.1.  None follows from
coherence, owner alignment, or router privacy separately.

## 6. ECO supply is connected before the private filters

Use the paper parameter `n`, so the canonical MMM factor components are the
plane trees with `n` edges.  A standard MMM pull label

\[
                         110u0v\longleftrightarrow101u0v          \tag{6.1}
\]

is all-six coherent exactly when `u` is empty.  Thus restricting the
canonical arborescence to its coherent labels is false: from `n=5` onward
that graph is disconnected.

The replacement is the coherent ECO atom.  For every Dyck parent
`D=1u0v` of semilength `n-1`, insert the three-corner window

\[
                              h(D)=1u000v0.                       \tag{6.2}
\]

The three zero positions give one alternating incidence hexagon.  In the
canonical coordinate gauge its external labels are

\[
                              (d,e)=(2n,0),                       \tag{6.3}
\]

and rotations give `(j-1,j)`.  Hence every atom is coherent.  Deleting the
new leaf shows that every standard MMM pull adjacency is co-contained in
one ECO hyperedge.  Since the standard MMM auxiliary graph is connected,
the two-section of the coherent ECO component hypergraph is connected for
every `n`.

For `n>=3` there is also an exact fixed-rotation collision simplification.
On the
`Cat_(n-1)` atoms with `(d,e)=(2n,0)`, each displayed forced owner colour
and each physical port occurs in at most two atoms.  The physical-port and
the two shore owner-colour collision graphs are the same directed path
forest.  Its edges are

\[
  1p\,10\,0v\longrightarrow 1p\,0\,10v,             \tag{6.4}
\]

and there are exactly `Cat_(n-2)` of them.  Hence one independent set in
this path forest makes the selected six-port sets disjoint and removes every
repeated displayed owner colour on both shores simultaneously.  This is a
useful common prefilter, not literal owner alignment: it neither proves that
the selected occurrence edge lies in the unique gap matching nor controls
occurrence-route bottlenecks.  The cases `n<=2` are collision-free or
trivial and are handled directly; the `Cat_(n-2)` edge formula is not
asserted there.

This static theorem removes only the **raw coherent-supply** obstruction.
It does not provide a legal family of toggles.  One ECO hyperedge may touch
three factor components; distinct atoms may share old factor edges or
ports; and owner masking or route privacy may delete every atom crossing a
given component cut.

Fix the state of Section 1 and let `E_raw(I,M)` consist of ECO atoms which,
individually,

1. have six literal ports with coherent external labels and an individually
   legal physical signature;
2. have all upper ports in `I` and all occurrence-labelled lower forced
   edges in the appropriate private matching bank;
3. have a literal binary component-merge effect; and
4. have at least one candidate occurrence route to the sink bank.

Support compatibility, the common matching-boundary transfer, H0--H5 cube
closure, pairwise node privacy, and laminar damage charging are deliberately
not unary fields of `E_raw`.  They are properties of one selected family.

### Corollary 6.1 (exact binary ECO private-tree reduction)

Let `S subseteq E_raw(I,M)` be one family whose physical supports are jointly
compatible, whose old/new banks export one common matching seam state, and
whose every component-forest subset satisfies the prepared H0--H5 cube.
Assume its component effects form a spanning tree and either

* its chosen source-to-dedicated-sink paths are pairwise node-disjoint; or
* one explicit laminar damage-charging certificate applies to the whole
  family.

Then forced-port Hall and router resilience require no further search.  The
common matching banks and the selected family-level route certificate prove
them, and the ordered fixed-decoration theorem executes every permitted
tree order.

A genuinely ternary ECO toggle which lowers component count by two is not
covered by pretending it is one graphic edge: one deleted router resource
could then restore two components.  Such an atom needs an explicit
rank-two decomposition with two privately charged route units, or a new
rank-weighted hypertree theorem.  The following exact unit expansion now
supplies the correct interface; static ECO co-containment alone does not.

### Corollary 6.2 (unit-expanded ECO router closure)

Let the selected ECO family be contained in one fixed coordinate rotation,
be jointly physically compatible on the prepared H0--H5 cube, and satisfy
the common owner/matching state.  For one selected atom `Z`, let `C(Z)` be
the distinct old factor
components met by its three old matching edges and put

\[
                         \rho(Z)=|C(Z)|-1.                         \tag{6.5}
\]

Choose a tree `R_Z` on `C(Z)`.  Require every edge of `R_Z` to be a
component-faithful ground element whose availability is controlled by its
own channel.  Equivalently, a retained grouped-rank state may be used, but
it must prove that deleting any `h` of the atom's channel resources lowers
its surviving component rank by at most `h`, for every partial channel set.
Suppose the union of all `R_Z` is a tree on the factor components.  Orient
every edge of the common
physical-support conflict path forest (6.4) to one incident atom and assign
their shared old factor edge to that atom as a routing resource.  The
residual **routing banks** are pairwise disjoint, and each atom loses route
vertices from at most two shared old edges.  This ownership operation does
not by itself make overlapping physical toggles compatible; that was the
opening hypothesis.

If, after either ownership choice at each of those at-most-two edges, every
selected atom realizes `rho(Z)` vertex-disjoint source-to-distinct-sink
occurrence paths inside its residual bank, and paths belonging to distinct
atoms are disjoint and avoid child router banks, then the unit-expanded tree
is router-resilient:

\[
                              c(R_Y)\le |Y|+1.                     \tag{6.6}
\]

Indeed, the selected paths give one private route per unit edge of the tree,
and the independent-survival hypothesis makes a deletion kill at most one
unit edge per deleted vertex.  This
closes the router coordinate only.  The same atom family must still pass the
owner/matching-seam and physical prefix-cube conditions above.

The first rank-two atom occurs at paper `n=5`; a single source copied twice
has gammoid rank one and is invalid.  The exact remaining routing statement
is therefore the **ECO local-channel lemma**: build these `rho(Z)` channels
inside each owned atom bank after its at-most-two genealogy-shared edges are
assigned away.  Failure is local to one atom plus its two ownership bits.
For a family mixing coordinate rotations, the full cross-rotation support
conflict graph must be recomputed; neither path degree at most two nor the
two-bit local reduction is asserted.

The exact remaining gate is existence of either one such collectively
compatible binary subcatalogue or one compatible unit-expanded ECO
hypertree satisfying the local-channel lemma.  Relative to any fixed unit
expansion, connectivity is equivalently the absence of a
**decorated-private barren cut**.  Before the family and its unit expansion
have been chosen, a barren cut is only the first necessary obstruction: the
missing-rectangle example of Section 5 shows that higher-order resource
incompatibility can defeat every global choice even when every component cut
has an individually admissible raw atom.  Raw two-section connectivity rules
out only the unfiltered cut obstruction.  It gives no owner-alignment,
matching-seam, local channels, residence, or compiler certificate.

## 7. The first literal filtered obstruction occurs at project `m=5`

Raw ECO connectivity does not survive automatically to an owner-aligned
decoration.  On the unrepaired canonical factor at paper parameter `n=4`
(project `m=5`), there are three factor components and 45 physical ECO
atoms.  Exhaustive literal replay of every minimal topology-safe two-atom
sequence gives

\[
 648\text{ ordered sequences},\qquad324\text{ Hamilton endpoints}. \tag{7.1}
\]

Every accepted pair has disjoint six-port sets and disjoint forced
three-colour faces on both shores, so it already passes the literal
collision-free condition whose fixed-rotation graph is described by (6.4).
Nevertheless every endpoint realizes only
81 of the required 84 turn colours on each shore, with common missing sets

\[
 \mathcal R^+=\{219,365,438\},\qquad
 \mathcal R^-=\{73,146,292\}.                       \tag{7.2}
\]

Thus no upper transversal `I` exists at all.  Owner alignment, its gap
forest, and route privacy are downstream and cannot repair this raw
endpoint.  This is a literal obstruction, stronger than the abstract
missing rectangle, but sharply scoped: it closes only minimal ECO
Hamiltonization of the unrepaired canonical `m=5` factor.

Project `m<=4` is positive on this raw face.  The known synchronized `m=5`
repair is also consistent with the obstruction because it changes the
factor first and then exports a leaf-peelable decoration.  Hence the exact
order forced by (7.2) is

\[
 \boxed{\text{controlled repair/rethread} \longrightarrow
 \text{collision-free compatible ECO family}\ \longrightarrow
 \text{owner-aligned residual matching}\ \longrightarrow
 \text{private/laminar occurrence routing}.}                     \tag{7.3}
\]

The arrows are gates, not independent choices: the repaired endpoint fixes
the physical ECO catalogue; the ECO family and upper transversal must still
be chosen so that the literal forced occurrences are matching owners; and
the same selected atoms must receive the route certificate.  The common
path-forest independent set closes only the displayed owner-colour repeats,
not the third gate by itself.

The proof-carrying finite scope is frozen in
`MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`.
It does not exclude a neutral preparation packet, a longer sequence, a
different factor, a non-ECO coherent family, or the off-forest alternating-
cycle route.

## 8. Type separation in the finite fixtures

The six shared-decoration transparent rows of the repaired `ML(7)` cycle
are Hamilton-to-Hamilton rethreads.  They may prepare a better state, but
they are loops in the component graphic coordinate and supply no edge of
`J`.  Its fifteen split toggles have no common decoration and are outside
the private coherent merge state.

The `m=4` component merge from item 2171 is a separate positive merge
certificate.  It can seed Theorem 2.1 only after its decoration, gap bank,
component edge and occurrence route have been put in the same prepared
signature.  A rethread certificate and a merge certificate cannot be added
as if they were two edges of one catalogue.

The raw ECO supply theorem used in Section 6 is
`MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`.  Its finite
pairwise-disjoint hypertrees through `n=7` are calibration only; they do not
prove the common decoration or private-router rows required here.

## 9. Dependencies and exact audit scope

The closed preservation theorem uses:

* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`;
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORATION_FILTERED_COHERENT_CATALOGUE_20260731.md`;
* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
* `MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md`;
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`.

The frozen finite audits independently replay the ECO supply/path-forest
calibration, the raw canonical `m=5` obstruction, and the occurrence-support
conflict/rank ledger.  They do not search for the controlled preliminary
repair or prove the ECO local-channel lemma.  Theorems 2.1 and 6.1--6.2 are
conditional mathematical implications; no all-`m` compatible private ECO
hypertree or coefficient-one conclusion is claimed.
