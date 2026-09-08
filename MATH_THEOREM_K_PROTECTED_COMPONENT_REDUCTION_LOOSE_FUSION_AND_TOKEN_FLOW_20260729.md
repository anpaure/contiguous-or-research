# Protected PBBS component reduction: loose fusion, sparse cuts, and target-token flow

Date: 2026-07-29

Status: unconditional sufficient reduction theorems.  They give two weaker
certificates for producing an at-most-two-component protected endpoint and
identify exact failure witnesses for those certificates.  Such witnesses do
not obstruct arbitrary component trades, unprotected middle permutations, or
the general upper-complete-`T` plus `COMP_d(T)` route.  No uniform PBBS
theorem is proved.

## 1. Protected factors and connectors

Fix odd `k=2m+1`, middle rank `r=m+1`, and residence depth `d=d(k)`.
Use the rank-`r-1`/rank-`r` inclusion graph.  A q1-exact factor is a spanning
2-factor of this bipartite graph, equivalently a Johnson 2-factor on all
rank-`r` owners with every lower-q1 colour once.

Call a factor **protected** when

1. every cyclic positive coordinate run has length at least `d+1`; and
2. every lower and upper fixed-window deck is complete at all possible
   depths.

The second condition implies arbitrary-width upper completeness and is
stronger than the final compiler requires.  The canonical PBBS chronology
supplies the all-depth shadow tower, but it is not thereby resident or
protected.  The audited finite modified endpoints at `k=11,13,15` are
examples lying in this protected face.

An alternating `C_6` has three selected and three unselected incidence
edges.  It is **transversal** when its three selected edges lie on three
distinct physical factor components.  Toggling it merges those three
components into one and changes no other component.

A **strong protected connector** is a transversal alternating `C_6` supplied
with a physical collar certificate proving that its toggle preserves
residence and every protected deck.  A family of connectors is called
**component-faithfully compatible** when its connectors are distinct, no
selected factor edge is used twice, the toggles commute, every partial toggle
is protected, and before each toggle its three selected edges still lie in
the three current components descended from its three original component
vertices.  Pairwise disjoint physical supports are a sufficient way to keep
the negative edges available; the final component-faithfulness clause is
stated explicitly because trace commutation alone does not imply it.  Put a
conflict edge between two connectors whenever they are not certified
component-faithfully compatible.  We require the certification convention to
have the hereditary property

\[
 \text{every independent set is component-faithfully compatible}. \tag{1.1}
\]

Disjoint fixed-window collars are one sufficient implementation of (1.1),
but (1.1) is the theorem's actual hypothesis.  Let `Delta` be the maximum
conflict degree.

### Lemma 1.1 (raw PBBS-star conflict constant)

In the natural PBBS legal-star atlas, declare two star hexagons to conflict
when their centre triples intersect.  For `m>=2` (recall `r=m+1`),

\[
 \Delta_{\rm raw}\le 3(m-1)=3r-6.                       \tag{1.2}
\]

#### Proof

The audited legal-star classification uses PBBS rank `m` and gives a linear
centre 3-graph with at most `m` atlas stars through any centre.  A fixed star
`h` can therefore conflict through each of its three centres with at most
`m-1` other stars.  The union bound gives `3(m-1)`.  The alternating-C6 lift
is injective on a centre and its fixed-matching lower endpoint, so disjoint
centre triples have disjoint raw physical supports.  QED.

For `m=1,2` the legal-star atlas is empty, so its raw conflict degree is zero.

The imported local facts are Lemma 5.1 and the legal-star classification in
`MATH_THEOREM_PBBS_PAIRED_C6_COMPLETE_CLASSIFICATION_20260726.md` and the
physical-survival audit in
`MATH_AUDIT_PBBS_C6_C8_CONNECTOR_PACKAGE_20260726.md`.

This is only a raw-overlap bound.  It becomes a bound for the strong
protected conflict graph only after a full-signature/collar heredity theorem
proves that raw-disjoint hexagons compose safely.  No such uniform theorem is
currently audited, so (1.2) cannot simply be inserted for `Delta` in
Theorem 2.1.

The connector multihypergraph `H(F)` has the physical components of `F` as
vertices and one 3-edge for every strong protected connector.  Parallel
hyperedges are retained because they may use different nonconflicting ports.

## 2. Loose-fusion expansion theorem

For a component set `S`, let

\[
 \partial_{1,2}(S)=
 \{Z:|V(Z)\cap S|=1,\ |V(Z)\setminus S|=2\}.             \tag{2.1}
\]

These are exactly the connectors that attach two previously untouched
components to one already fused component.

### Theorem 2.1 (protected loose fusion)

Let a protected factor have `c>=3` components.  Suppose:

1. `H(F)` contains at least one connector; and
2. for every odd \(S\subseteq V(H)\) with

\[
 3\le |S|\le
 \begin{cases}
 c-2,&c\text{ odd},\\
 c-3,&c\text{ even},
 \end{cases}                                             \tag{2.2}
\]

one has

\[
 |\partial_{1,2}(S)|>
 \Delta\frac{|S|-1}{2}.                                  \tag{2.3}
\]

Then a component-faithfully compatible sequence of strong protected connectors reduces the
factor to one component when `c` is odd and to two components when `c` is
even.  Every intermediate factor remains protected.

#### Proof

Choose any first connector.  It fuses its three component vertices, so the
current fused set `S` has size three and the selected loose tree has one
connector.  Inductively, suppose `S` has odd size and the chosen family has

\[
 j=(|S|-1)/2                                               \tag{2.4}
\]

connectors.  At most `j Delta` members of
\(\partial_{1,2}(S)\) conflict with a chosen connector.  By (2.3), some outward
connector is component-faithfully compatible with the whole chosen family.  It meets the already
fused component in one original component and two untouched components, so
its toggle merges those three current components.  The fused set grows from
`|S|` to `|S|+2`, and (2.4) remains true.

If `c` is odd, continue until `|S|=c`; if `c` is even, continue until
`|S|=c-1`, leaving one untouched component.  Compatibility and (1.1) keep
every partial factor protected.  QED.

For `c=3,4`, the expansion range is empty and one connector already gives
the stated conclusion.

### Corollary 2.2 (failure certificate for greedy strong-C6 loose fusion)

Failure of the hypotheses of Theorem 2.1 has one of two exact witnesses:

* there is no protected transversal `C_6`; or
* there is an odd component set `S` in the range (2.2) with

\[
 |\partial_{1,2}(S)|\le
 \Delta\frac{|S|-1}{2}.                                  \tag{2.5}
\]

These are obstructions only to this greedy strong-connector criterion.  They
do not show that the factor cannot be reduced by a nontransversal circuit, a
larger packet, an unsafe-intermediate simultaneous trade, or replacement by
another upper-complete middle permutation.  To establish or refute `LFE(m)`
specifically, one must prove the cut expansion bound or exhibit such a sparse
cut.

## 3. Why packets may be needed within protected-prefix descent

All-depth protection consists of integer lower bounds on occurrence loads.
A primitive circuit may consume the last witness of one target while a
second circuit creates a replacement.  Requiring every primitive circuit to
be safe separately discards such exchanges.

Let `Z` index all protected fixed-window target/depth/shore resources.  For a
factor `F`, write \(\lambda_F(z)\ge1\) for its occurrence load.  Let
`C_1,...,C_s` be alternating circuits.  Call them a **trace-commuting packet**
when every subset is a legal factor toggle and there are integer vectors
\(\Delta_i\) such that for every subset `I`,

\[
 \lambda_{F\triangle\bigtriangleup_{i\in I}C_i}(z)
 =\lambda_F(z)+\sum_{i\in I}\Delta_i(z).                 \tag{3.1}
\]

Assume separately that every subset toggle is residence-safe.  Collar
disjointness is again a sufficient, not necessary, way to obtain these two
properties.

For each resource `z`, make

\[
 s_z=\lambda_F(z)-1                                      \tag{3.2}
\]

initial slack tokens.  Circuit `i` creates
\(\max(\Delta_i(z),0)\) supply tokens and demands
\(\max(-\Delta_i(z),0)\) tokens of type `z`.

A **repair matching** injectively matches every demand token either to an
initial token of the same type or to a supply token of the same type.  If a
demand of circuit `i` is matched to a supply of circuit `j`, draw the
precedence arc `j -> i`.

### Theorem 3.1 (exact acyclic target-token ordering)

For a trace-commuting, residence-hereditary packet, its circuits can be
ordered so that every prefix factor is protected if and only if it has an
acyclic repair matching.  If the full packet has fewer components than `F`,
at least one step in any such protected order strictly decreases the
component count.

#### Proof

Take a topological order of the precedence digraph.  In any prefix, every
demand token already used is matched either to initial slack or to a supply
whose producer precedes its consumer and hence also lies in the prefix.
Injectivity gives, for every resource `z`,

\[
 \sum_{i\text{ in prefix}}\max(-\Delta_i(z),0)
 \le s_z+
 \sum_{i\text{ in prefix}}\max(\Delta_i(z),0).           \tag{3.3}
\]

By (3.1), the prefix load remains at least one.  Residence-heredity supplies
the other protected condition.  Component counts telescope along the order;
if the final count is smaller, some individual step has negative component
change.

Conversely, suppose a protected prefix order is given.  Fix a resource `z`
and scan the circuits in that order.  When a circuit demands `h` tokens, the
protected-prefix inequality says that at least `h` unused initial-slack or
earlier-supply tokens remain; match the demands to any such tokens.  When
a circuit supplies tokens, add them to the available pool.  Repeat
independently for every resource.  Every resulting precedence arc points
forward in the displayed circuit order, so the matching is acyclic.  QED.

### Corollary 3.2 (failure of the acyclic repair certificate forces a dependency cycle)

For a fixed trace-commuting, residence-hereditary packet, absence of every
protected prefix ordering is equivalent to every repair matching containing
a directed cycle.  A
smallest model example has two circuits and two unit-load resources:

\[
 \Delta_1=(-1,+1),\qquad \Delta_2=(+1,-1).               \tag{3.4}
\]

The total trade is load-neutral, but either first circuit kills one private
witness.  More generally, if every first move is unsafe while the full
additive packet is protected, every repair matching contains a directed
dependency cycle.  This obstructs only the acyclic token-ordering certificate
for that packet; it does not obstruct a different packet, a simultaneous
non-prefix toggle, nonadditive witness effects, or an arbitrary
upper-complete `T`.

There is no hidden nonexistence of a repair matching here.  If the full
packet is protected, then for every resource the total demand is at most its
initial slack plus total supply, so a typewise repair matching exists.  The
obstruction asserted above is precisely that every such matching has a
directed cycle.

## 4. Weaker sufficient invariants for the protected at-most-two-component wrapper

There is an exact formulation which includes neutral legality routers.  Fix
any declared literal switch library, and form a graph `G_P` whose vertices
are protected q1-exact factors and whose edges are switches whose two
endpoints are protected.  Let `c(F)` be the component count, and let
`G_P[c]` be the subgraph induced by the vertices of component count `c`.
Its connected components are the **neutral orbits** at level `c`.

### Theorem 4.1 (neutral-orbit positive-cut criterion)

Every vertex of `G_P` has a path to a factor with at most two components
along which the component count never increases if and only if every neutral
orbit `O` at every level `c>2` has an incident safe switch to a vertex of
strictly smaller component count.

After contracting neutral orbits and directing every strict-decrease edge
downward, one specified source has some successful nonincreasing route if and
only if its quotient vertex has a directed path to a level-at-most-two
vertex.  Requiring every nonincreasing-reachable state from that source to
remain completable is the stronger condition that every reachable neutral
orbit above level two have a lower boundary.

#### Proof

If `O` has a lower boundary edge, route inside `O` to its endpoint and take
that edge.  The component count strictly decreases.  Induction on the
nonnegative integer `c` reaches level at most two.  Conversely, if a neutral
orbit `O` has no lower boundary edge, a nonincreasing path starting in `O`
can only take neutral edges, all of which stay inside `O`; it is trapped.
For one source, contracting neutral moves gives exactly the stated directed
reachability problem.  A dead branch need not obstruct a different successful
branch, which is why quantifying over every reachable orbit is the stronger
robust condition.  QED.

This is the sharp statement for a fixed router/splitter library.  A no-go in
that architecture is a protected neutral orbit above level two with no
negative boundary, not merely a state with no immediately improving move.
If arbitrary sign-compatible global packets are admitted as single moves,
the endpoint question weakens further to whether the relevant protected
factor fibre contains any factor with at most two components.  The raw
inclusion-graph Markov basis proves algebraic connectivity, but not this
decorated protected minimum.

More precisely, for the protected face \(\mathscr P_{m,d}\) of the companion
report, endpoint-form UPMBC's component clause is exactly

\[
 \min_{G\in\mathscr P_{m,d}}c(G)\le2,                  \tag{4.1}
\]

with empty minimum equal to infinity.  Every route theorem in this note is a
sufficient certificate for this endpoint inequality from a supplied
protected seed; none is part of the inequality itself.

### Proposition 4.2 (ribbon gain and the minimal abstract packet lock)

For a matching packet `pi` on `s` marked ports, let `rho` be the old-fragment
return permutation, put

\[
 k=c(\pi),\qquad t=c(\rho),\qquad
 o=\#\operatorname{Orb}\langle\pi,\rho\rangle,
 \qquad b=s-k-t+o.
\]

There is a nonnegative integer ribbon genus sum `g` for which the exact
component fusion gain is

\[
 \Gamma=t-o-b+2g.                                      \tag{4.2}
\]

For one connected circuit, `k=o=1`, so

\[
 \Gamma=2t-s-1+2g.                                     \tag{4.3}
\]

#### Proof

Make the bipartite ribbon graph whose black vertices are the cycles of `pi`,
whose white vertices are the cycles of `rho`, and whose `s` edges are the
marked ports with cyclic orders induced by the two permutations.  It has `o`
components, cycle rank `b`, and boundary permutation `pi rho`.  Capping the
boundary components and applying Euler's formula gives

\[
 k+t+c(\pi\rho)=s+2o-2g.
\]

The cut--join identity says
`Gamma=t-c(pi rho)`; substitution gives (4.2), and the connected-circuit
specialization gives (4.3).  QED.

The direct pointwise connected-circuit conjecture is false for generic
abstract quota-protected matching fibres, so it cannot follow from factor
algebra and additive deck inequalities alone.  On six ports take

\[
 M_0=\mathrm{id},\qquad P=(01)(23)(45),\qquad
 \pi_E=(024),\qquad \pi_O=(135).
\]

Give the four shores the two-colour load vectors

\[
 P:(3,3),\quad P\pi_E:(0,6),\quad P\pi_O:(6,0),\quad
 P\pi_E\pi_O:(3,3).
\]

With positivity threshold one, only the two endpoints are protected.  The
initial factor has three components, neither connected `C_6` is a protected
first move, and their simultaneous two-C6 packet reaches one component.
This is also the two-resource cyclic repair lock of (3.4): no acyclic prefix
certificate exists although the simultaneous endpoint is protected.

The ribbon proof and the minimality/nonloop audit are independently given in
`MATH_THEOREM_L_PBBS_PROTECTED_RIBBON_POSITIVE_CUT_AND_PACKET_LOCK_20260729.md`.
The example does not instantiate the residence/all-depth PBBS protected face;
it is an abstract matching-fibre obstruction.  It refutes a universal
algebraic pointwise exchange lemma but does not refute endpoint-form UPMBC or
a PBBS-specific circuit-extraction theorem.

The direct conjecture

> every protected factor with more than two components has one protected
> component-decreasing alternating circuit

may be replaced by either of the following weaker assertions.

* **Loose-fusion expansion `LFE(m)`:** the strong protected `C_6` connector
  system satisfies Theorem 2.1 at every protected state above two components
  reachable from a declared protected seed.
* **Acyclic packet flow `APF(m)`:** every protected state above two
  components reachable from that seed has a trace-commuting,
  residence-hereditary packet with lower final component count and an acyclic
  repair matching.

Given such a protected seed, either assertion can be iterated to produce a
protected factor with at most two components.  Neither assertion constructs
the seed: the canonical PBBS two-matching factor is all-depth and q1-exact,
but is not uniformly known to be `d`-resident.  Combined with a protected
seed, the upper-safe opening, and the exact full compiler in
`MATH_THEOREM_K_ALL_ODD_PBBS_MARKOV_BOUNDARY_COMPILER_REDUCTION_20260729.md`,
it discharges the component-reduction clause of `UPMBC(m)`.

Neither assertion is necessary for coefficient one.  Their failure can
coexist with a different protected endpoint, a nonhereditary simultaneous
trade, a multi-component opening, or a direct upper-complete permutation `T`
satisfying `COMP_d(T)`.

The invariants are genuinely weaker in different directions.  `LFE` permits
the useful connector to depend on the growing fused component and requires
only a sparse-cut expansion estimate.  `APF` permits every primitive circuit
except the initially funded source circuits to be individually shadow-unsafe,
provided later witness repairs have an acyclic funding order.  An acyclic
funding digraph necessarily has a source circuit funded from initial slack.

## 5. Calibration and exact remaining boundary

At `k=11` and `k=13`, the audited protected endpoint already has one and two
components, respectively, so component reduction is vacuous.  At `k=15`,
the protected fixed-matching chain has component counts

\[
 9\longrightarrow4\longrightarrow3\longrightarrow2       \tag{5.1}
\]

under support `4,6,4` alternating exchanges.  This proves protected descent
for that endpoint, but the exchanges are not all transversal `C_6`
connectors and the finite chain does not prove `LFE(m)` or `APF(m)`.

No PBBS theorem currently proves `LFE(m)` or `APF(m)` uniformly.  Within
these two sufficient component-reduction architectures, the next targets
are:

1. construct or otherwise certify a protected seed in the PBBS q1 fibre;
2. derive (2.3) from its Catalan component hierarchy and a bounded physical
   conflict degree;
3. construct an `APF` token matching from its PBBS witness atlas; or
4. delimit these two descent criteria's failure precisely.

A sparse odd cut refutes the `LFE` hypothesis only at the stated factor.  To
refute `APF` at that factor, one must prove that **every** admissible
trace-commuting, residence-hereditary component-decreasing packet lacks an
acyclic repair matching; exhibiting one cyclic packet is insufficient.
Neither negative conclusion would obstruct the general upper-complete-`T`
plus `COMP_d(T)` route.  Finite `k=11,13,15` success is calibration only and
is not used as a uniform proof.
