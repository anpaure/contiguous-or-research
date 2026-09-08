# Turn-defect transport: Hall flow, topology relays, and terminal linkage

Date: 2026-07-31  
Status: exact conditional controlled-debt packet-selection theorem; exact
`m=5` instantiation; exact K17 one-step calibrations; sharp independence
counterexamples; no all-`m` macro-supply theorem

## 0. Verdict

The three-`C10` repair at `m=5` is not inherently a period-three argument.
Its reusable structure is:

1. on each turn shore, one surplus occurrence token is transported to each
   missing colour;
2. a physical macro pairs one lower transport job with one upper transport
   job;
3. selected macros must be physically vertex-disjoint;
4. topology supplies a prerequisite/relay order; and
5. the augmented occurrence matching may remain deficient at every proper
   prefix, provided one terminal vertex-disjoint linkage discharges the
   common-core debt after the full packet.

On the private Cartesian face this has an exact Hall/flow theorem.  First
solve one capacitated Hall problem on each shore.  Then solve a perfect
matching between the selected lower and upper transport jobs.  If physical
conflicts are contained in the line graph of that compatibility graph, the
matching is automatically vertex-disjoint.  An acyclic relay certificate
orders it, and one terminal gammoid max-flow certifies the final alternating
SDR.  No intermediate SDR is required.

This formulation applies unchanged to free missing orbits.  A translation-
equivariant bank on a free orbit gives a balanced bipartite Cayley graph;
every nonempty allowed-shift set satisfies Hall, and one fixed shift already
gives a perfect transport matching.  Stabilizer-three is only the first
finite instance where topology needs a relay.

Here **bounded** means bounded support/port adhesion for each circuit and
bounded live boundary/linkage debt at a recursive interface.  The number of
circuits in a packet may grow with the defect set.  No theorem below assumes
a dimension-independent packet cardinality.

Without the private/line-conflict and relay hypotheses, no Hall theorem is
possible.  Arbitrary four-way macro compatibility contains `3DM`; two
macros can pass every marginal Hall test but share a physical vertex; and a
two-macro prerequisite cycle has no legal first move.  Palette repair also
does not imply terminal linkage.  These are four independent rows.

## 1. Loads, holes, and occurrence tokens

Fix one shore `epsilon in {-,+}` with colour alphabet `C_epsilon` and turn
load

\[
 n_\epsilon:C_\epsilon\longrightarrow\mathbb Z_{\ge0}.
\tag{1.1}
\]

Its holes and surplus occurrence tokens are

\[
 H_\epsilon=\{c:n_\epsilon(c)=0\},
\qquad
 R_\epsilon=\{(c,j):1\le j\le n_\epsilon(c)-1\}.
\tag{1.2}
\]

The occurrence label `j` is physical: two repeated occurrences of one colour
are distinct capacity-one donor tokens.  Aggregating them gives donor
capacity

\[
 s_\epsilon(c)=(n_\epsilon(c)-1)^+.
\tag{1.3}
\]

### Lemma 1.1 (one-hole transport decomposition)

Let an exact factor switch change the load by an integral vector `delta`
with total sum zero.  Suppose `delta(h)=1` for exactly one old hole `h`, no
other old hole has positive `delta`, the switch creates no new hole, and it
leaves every previously covered colour covered.  Then its
occurrence-level changes decompose into directed unit paths and cycles on
colour occurrences with exactly one path ending at `h` and starting at a
token of `R_epsilon`.  All other paths and cycles merely relocate surplus
tokens among covered classes.

#### Proof

Split every negative coordinate of `delta` into labelled departing units and
every positive coordinate into labelled arriving units.  Equality of the
total sums gives a bijection between the two banks.  Pair the units and
regard each pair as a directed one-step transport; if the physical switch
supplies an occurrence correspondence, use it.  Exactly one arrival ends at
`h`.  Every departure from an old colour is a surplus token: if
`delta(c)=-a`, terminal coverage gives `n(c)>=a+1`.  Hence the transport into
`h` starts at a token of `R_epsilon`.  All remaining transports have covered
targets and surplus sources; after identifying intermediate surplus labels,
they decompose into paths between surplus occurrences and directed cycles.
\(\square\)

Thus a `C10` may change three turn counters down and three up while carrying
only one **defect unit**: the collateral changes are a circulation in the
repeated part.

## 2. The two shore-flow problems

For each shore let

\[
 G_\epsilon=(R_\epsilon,H_\epsilon;A_\epsilon)
\tag{2.1}
\]

be the allowed unit-transport graph.  An edge
`rho h` is an occurrence-labelled job saying that some bounded macro can
transport donor token `rho` to hole `h`, with a supplied collateral reserve
certificate.  In the unit model that macro has `delta(h)=1` and does not
service another initially missing colour on the same shore.  Macros that
service several holes belong to a hypergraph model and are outside Theorem
2.1.

### Theorem 2.1 (capacitated shore Hall)

There is an integral set of jobs which fills every hole exactly once and
uses every donor occurrence at most once if and only if

\[
 |X|\le |N_\epsilon(X)|
 \quad\text{for every }X\subseteq H_\epsilon.
\tag{2.2}
\]

In colour-aggregated form this is

\[
 |X|\le\sum_{c\in N_\epsilon(X)}s_\epsilon(c).
\tag{2.3}
\]

#### Proof

Join a source to every donor occurrence with capacity one, use the edges of
`G_epsilon`, and join each hole to a sink with capacity one.  A flow of value
`|H_epsilon|` is integral.  The max-flow/min-cut inequalities are exactly
(2.2); merging parallel donor occurrences gives (2.3).  \(\square\)

Write `J_-` and `J_+` for two saturating integral job sets.  A macro must
realize one job from each shore, so in the unit/unit model a complete repair
requires

\[
 |H_-|=|H_+|=:d.
\tag{2.4}
\]

If the two numbers differ, one must add explicitly certified one-shore or
dummy-neutral macros; equality cannot be assumed away.

## 3. Pairing the shores and enforcing physical disjointness

For fixed `J_-`,`J_+`, form the macro compatibility graph

\[
 K(J_-,J_+)=(J_-,J_+;E_K).
\tag{3.1}
\]

An edge `e=ab` carries one literal bounded macro `mu_e` realizing lower job
`a` and upper job `b`, its full signed counter vectors, its physical vertex
support `V_e`, and its topology/linkage signature.

### Definition 3.1 (line-conflict catalogue)

The catalogue is line-conflict when

\[
 V_e\cap V_f\ne\varnothing
 \quad\Longrightarrow\quad
 e\text{ and }f\text{ share an endpoint in }K.
\tag{3.2}
\]

This is precisely the private-aligned condition needed at the macro layer:
conflict edges are contained in the line graph of `K`.

### Lemma 3.2 (compatibility Hall)

Under (2.4), a set of `d` pairwise physically vertex-disjoint macros
realizing all jobs exists if

\[
 |N_K(X)|\ge |X|\quad\text{for every }X\subseteq J_-.
\tag{3.3}
\]

Within a line-conflict catalogue, (3.3) is also necessary for a packet using
the fixed job sets.

#### Proof

Hall's theorem gives a perfect matching `M` in `K`.  Distinct edges of `M`
share neither a lower nor an upper endpoint.  Condition (3.2) therefore
implies their physical supports are disjoint.  Conversely, any packet using
every fixed job once is a perfect matching in `K`, so Hall is necessary.
\(\square\)

The shore flows and compatibility matching are separately integral.  The
choice of shore flows need not be easy in a general non-Cartesian catalogue:
the exact statement is that there exist saturating `J_-`,`J_+` for which
(3.3) holds.  Two useful polynomial sufficient faces are:

1. the shore job sets are prescribed and satisfy (3.3); or
2. every saturating lower job is compatible with every saturating upper job,
   so `K` is complete and the shore flows may be chosen independently.

## 4. Relay order and the full turn ledger

Static Hall does not know whether a selected circuit is alternating at the
time it is applied.  Give every macro `e` a prerequisite set

\[
 P(e)\subseteq M\setminus\{e\}.
\tag{4.1}
\]

The directed relay graph has arcs `f -> e` for `f in P(e)`.

### Definition 4.1 (relay-valid packet)

A selected matching `M` is relay-valid if its prerequisite graph is acyclic
and one (equivalently, a declared) topological order

\[
 e_1,\ldots,e_d
\tag{4.2}
\]

has both of the following exact properties.

1. `mu_{e_i}` is alternating in the current factor, its physical topology
   transition is legal, and the declared final topology accepts.
2. For both shores and every prefix `p`,
   \[
     n_\epsilon(c)+\sum_{i\le p}\delta_{e_i}^\epsilon(c)\ge1
   \tag{4.3}
   \]
   for every colour covered initially or at an earlier prefix; unserved old
   holes are exempt until their service step.

Condition (4.3) is the exact collateral reserve ledger promised in Section
2.  It prevents a macro from filling one hole by creating another.

### Lemma 4.2 (ordered installation)

A relay-valid perfect matching installs as a physically legal packet, fills
every lower and upper hole exactly once, and creates no new turn hole.

#### Proof

Acyclicity supplies the topological order.  Definition 4.1(1) makes every
factor switch legal and gives the terminal topology.  The shore matchings
service every hole once.  The prefix inequalities preserve all old and
already repaired colours, so the terminal palettes are complete.  Physical
supports are disjoint by Lemma 3.2.  \(\square\)

A convenient robust sufficient form partitions the macros into relay layers
`M_0,...,M_s`: supports in each layer commute, and every macro of layer `i`
is certified legal after all earlier layers.  Then concatenating the layers
gives (4.2).

### 4.1 Exact subset-state routing

### Theorem 4.3 (exact subset-state router)

Let `E` be any fixed set of pairwise vertex-disjoint alternating macros.
Delete all their old factor edges and pair the two ends of every resulting
path atom by traversal; call this fixed atom pairing `P`.  For `S\subseteq E`,
let `M_S` use the new port matching for macros in `S` and the old port
matching for macros outside `S`.  Then

\[
 \#\operatorname{comp}(F_S)=\#\operatorname{cycles}(P\cup M_S).
\tag{4.4}
\]

Declare `S` safe when this literal port transition has the allowed topology,
the required protected-support state, and every prefix condition that the
application is required to retain.  There is a legal one-at-a-time ordering
of all macros if and only if the safe subset cube contains a maximal chain

\[
 \varnothing=S_0\subset S_1\subset\cdots\subset S_{|E|}=E,
 \qquad |S_i\setminus S_{i-1}|=1,
\tag{4.5}
\]

whose added macro is alternating and legal at every step.  Equivalently,

\[
 R(\varnothing)=1,\qquad
 R(S)={\bf1}_{\rm safe}(S)
 \bigvee_{e\in S}
 \bigl(R(S\setminus\{e\})\wedge
       \operatorname{legal}(S\setminus\{e\},e)\bigr).
\tag{4.6}
\]

If matching debt is permitted until packet end, it is absent from the
prefix safety state and is tested once by Theorem 5.1.  If a recursive
interface demands prefix linkages, the full pairing-resolved boundary
linkage relation, not its rank, must be included in `safe(S)`.

#### Proof

All switches are support-disjoint, so deleting all old switch edges leaves
the same path atoms for every subset.  A factor component is exactly an
alternating cycle of an atom edge from `P` and a seam edge from `M_S`, proving
(4.4).  Any executable order records the maximal chain of its installed
subsets.  Conversely, every step of a chain counted by (4.6) is, by
definition, a legal current-factor switch with the required retained state.
Induction along the chain installs the packet.  \(\square\)

Static Hall does not imply (4.5).  Two vertex-disjoint macros can each split
a Hamilton cycle while their joint toggle is Hamiltonian; then the terminal
subset is safe but neither singleton is.  This two-macro fixture is the
smallest topology-relay obstruction.

Under the additional **context-independent Markov** hypothesis, macros may
instead be arcs of a directed relay multigraph.  An order using every arc
once from `r_0` to `r_f` exists exactly when the Euler degree balances hold,

\[
 \deg^+(v)-\deg^-(v)
 =\mathbf 1_{v=r_0}-\mathbf 1_{v=r_f},
\tag{4.7}
\]

and, after adjoining the return arc `r_f -> r_0`, the underlying undirected
support on nonzero-degree vertices is connected.  This is a useful flow
projection, but it is not valid for context-dependent relays; those require
(4.6).

### 4.2 Transparent glues are not repair macros

Fix a genuine factor-alternating incidence hexagon and one decoration `D`.
Its toggle is transparent for this same `D` exactly when:

1. the selected local turn-colour multisets agree before and after,
   separately on the two shores; and
2. after deleting the old matching, discard every retained fragment with an
   empty selected subsequence; the boundary mark types of the remaining
   fragments alternate across the new seams.

Such a move carries the same selected occurrence matching and has no new
matching debt relative to `D`.  These are the moves that may enter a later
prepared private gluing catalogue.

A transport macro is different.  It changes a turn-defect unit and may have
no decoration at a proper prefix.  Requiring it to be transparent would
forbid the repair it is meant to perform.  Its obligation is instead the
turn ledger (4.3), topology shelling, and the one packet-end linkage of
Section 5.

The frozen `ML(7)` calibration shows both behaviours.  One ordinary standard
incidence-hex toggle repairs the first gap-Hall counterexample by permitting
a new joint decoration; it is not asserted transparent for the failed frozen
decoration.  Around the repaired cycle there are `31`
alternating hexagons, `16` Hamilton outputs, `10` decorable outputs, and only
`6` toggles with a decoration common to both sides.  Hence neither an
arbitrary frozen SDR nor an arbitrary published gluing tree is a valid
router.  The recursion must first construct the joint alternating SDR, then
use only its transparent face for private gluing; repair packets sit outside
that face until their terminal linkage closes.

## 5. Terminal common-core linkage, with no prefix requirement

Let `A_0` be the initial augmented occurrence graph and `A_M` the graph after
the whole relay-valid packet.  Let `F` be any guarded selected-edge bank
forced at both endpoints.  Delete the vertices saturated by `F`; all graphs
below mean the residual graphs.  Put

\[
 C_M=A_0\cap A_M
\tag{5.1}
\]

on the common occurrence-labelled vertex set.  Let `P` be a maximum matching
of `C_M`, of size `N-r`.  Orient unmatched final edges left-to-right and
matched common edges right-to-left, with the standard vertex splitting for
unit capacities.  Let `S` and `Z` be the exposed left and right vertices.

### Theorem 5.1 (packet-end linkage criterion)

The terminal augmented graph `A_M` has a perfect matching extending `F` if
and only if the oriented final residual network contains `r`
vertex-disjoint directed paths linking all vertices of `S` to distinct
vertices of `Z`.  Equivalently, after adjoining a capacity-one supersource
to `S` and a capacity-one supersink from `Z`, every source--sink cut has
capacity at least `r`.

No matching or linkage condition is required at a proper packet prefix.

#### Proof

This is the Berge augmenting-path theorem after contracting the forced
matching `F`, in the common-core orientation.
The symmetric difference of `P` and a final perfect matching consists of
`r` vertex-disjoint augmenting paths plus alternating cycles.  Conversely,
toggling `P` along `r` such paths increases its size from `N-r` to `N`.
Menger's theorem gives the separator formulation.  \(\square\)

If a recursive state requires one common core through every intermediate
factor, replace (5.1) by `intersection_j A_j`.  For endpoint-only packet
acceptance, `A_0 intersection A_M` is exact and does not impose a hidden
prefix decoration requirement.

Physical vertex-disjointness of macros does not make their linkage gains
additive.  Here is a minimum endpoint-disjoint example.  Take

\[
 L=\{b,s_1,s_2\},\qquad R=\{a,t_1,t_2\},
\tag{5.2a}
\]

and let the common core have exactly the edges `ba,bt_1`.  Its maximum
matching `P={ba}` has rank one.  Macro `e_1` adds `s_1a`; macro `e_2` adds
`s_2t_1`.  The two added edges have disjoint endpoint sets.  Alone, `e_1`
has the augmenting path

\[
 s_1-a-b-t_1,
\tag{5.2b}
\]

and alone `e_2` has the direct augmenting path `s_2-t_1`.  Together both
augmentations require the same exposed sink `t_1`; the maximum matching rank
is still two, not three (indeed `t_2` is isolated).  Thus the joint linkage
gain is one, not two.
Thus a packet needs the global terminal flow.  Additivity is valid under the
stronger direct-sum hypothesis that exposed banks and all possible routes
lie in pairwise vertex-disjoint directed modules with distinct sink banks.

If the initial augmented deficiency is `d_0` and the selected disjoint
circuits have half-lengths `t_e`, item 2169 gives the useful a priori bound

\[
 r\le d_0+3\sum_{e\in M}t_e.
\tag{5.3}
\]

For `d` `C10` macros this is `r <= d_0+15d`.  The bound controls terminal
state width; it does not produce the paths.

## 6. The exact ordered transport theorem

### Theorem 6.1 (Hall--relay--linkage packet theorem)

Assume the unit/unit model (2.4) and a supplied bounded macro catalogue.
There is an ordered, physically vertex-disjoint packet which fills every
turn hole on both shores, ends in the declared topology, and has a perfect
augmented occurrence matching if the following objects exist:

1. shore-saturating integral job sets `J_-`,`J_+`, equivalently the Hall
   flows of Theorem 2.1;
2. a perfect matching `M` in `K(J_-,J_+)` whose chosen literal macro
   supports are pairwise disjoint; a line-conflict catalogue together with
   (3.3) is one checkable sufficient certificate for this clause;
3. a relay-valid order of `M`; and
4. a terminal linkage of size `r` from Theorem 5.1.

Within the occurrence-labelled unit/unit model, for a supplied catalogue
whose feasible packets are required to be matchings in `K`, the four clauses
are also necessary.  Line-conflict is a sufficient structural property of
the catalogue, not a necessary property of an individual successful packet.

#### Proof

Sufficiency is the support-disjoint matching, Lemma 4.2 and Theorem 5.1 in
that order; Lemma 3.2 supplies the matching on the line-conflict face.  For
necessity, decompose each successful macro's unit turn change by Lemma
1.1 and retain its serviced donor--hole job on each shore.  Since every hole
is filled once and physical donor occurrences are not reused, these jobs are
saturating integral shore flows.  Pairing the two jobs performed by each
macro gives a perfect matching in `K`.  The actual application order is a
relay-valid order, and the final perfect augmented matching gives the
terminal linkage by symmetric difference with a maximum common matching.
\(\square\)

### Corollary 6.2 (robust Cartesian face)

Suppose both shore Hall inequalities hold, the macro lift is complete
Cartesian and line-conflict, one fixed relay layering is valid for every
perfect compatibility matching, and every such matching activates a fixed
private terminal linkage.  Then the Hall inequalities alone construct a
successful packet by two max flows and one bipartite matching.

This is the direct analogue of the prepared private/aligned
graphic--gammoid face.  It is intentionally stronger than the general macro
problem.

### Corollary 6.3 (repair first, transparent private gluing second)

Suppose a relay-valid transport packet satisfies Theorem 6.1 and terminates
at a factor `F*` with one guarded decoration `D*`.  Suppose, on `F*`, a
later collar bank is transparent for this same `D*` by the two local tests of
Section 4.1 and satisfies the prepared private/aligned graphic--gammoid rank
criterion

\[
 r_{\rm gr}(X)+r_{\rm link}(T\setminus X)\ge q-1
 \quad(X\subseteq T).
\tag{6.1}
\]

Then one may concatenate the ordered repair packet with a selected private
gluing tree.  The packet changes the decoration and pays its matching debt;
the later transparent moves carry `D*` without reopening that debt.

Conversely, a move transparent for a fixed `D` cannot itself repair a
selected turn-colour defect: its selected local turn-colour multiset is
unchanged on each shore.  Therefore a recursion which needs palette repair
must either complete a macro packet before entering the transparent face, or
carry the full bounded linkage signature through the interleaving.  Pairwise
transparent glues for unrelated decorations do not suffice.

#### Proof

Theorem 6.1 produces the decorated entrance state `(F*,D*)`.  Fixed-`D*`
transparency preserves both selected palettes and boundary alternation.  On
the prepared private/aligned face, (6.1) is the exact
graphic--gammoid-intersection criterion for selecting a component spanning
tree with the required linkage.  Concatenation proves the positive claim.
For the converse, equality of the two local selected turn-colour multisets
on each shore is exactly the first transparency condition, so no missing
selected colour can be gained.  The final sentence follows because the
common decoration is the shared ground state of both the palette and
boundary tests.  \(\square\)

### Theorem 6.4 (exact controlled-debt packet criterion)

Let every augmented occurrence graph in the state system have two shores of
order `N`.  At a packet state `S`, let `h_-(S),h_+(S)` be the numbers of
declared zero-occurrence turn classes; these are isolated vertices on their
respective augmented shores.  Put

\[
 b(S)=\max\{h_-(S),h_+(S)\},\qquad
 \xi(S)=N-\nu(A_S)-b(S).
\tag{6.2}
\]

The nonnegative integer `xi(S)` is the **correlation debt** beyond the forced
palette-hole floor.  For a legal transition or declared macro block
`S -> S'`, contract the forced guarded bank common to its endpoints, take a
maximum matching of the residual common graph, and let `lambda(S,S')` be the
number of vertex-disjoint augmenting paths in a supplied linkage to a
declared maximum matching of `A_{S'}`.  Thus `lambda` is the target matching
rank minus the residual common-core rank.  Let `theta(S)` be the exact
port-pairing, protected-support, and reachability signature required by the
topology interface.  Its boundary \(\partial\theta(S)\) is, by definition, the
named set of live port/terminal vertices on which those relations are stored;
\(|\partial\theta(S)|\) counts vertices, not relations or states.

Fix widths `w,ell,a`.  A packet is `(w,ell,a)`-controlled when every literal
prefix state, including the empty initial prefix, satisfies

\[
 \xi(S)\le w,\qquad |\partial\theta(S)|\le a,
\tag{6.3}
\]

every nonterminal transition `S -> S'` satisfies
`lambda(S,S')<=ell`, and its terminal state has `b=xi=0`.  The packet size
itself is unrestricted.

For a supplied occurrence-labelled unit-macro catalogue, such an ordered
packet exists **if and only if** there are:

1. shore-saturating transport jobs and a support-disjoint compatible macro
   selection as in Theorem 6.1;
2. a maximal legal chain in the exact subset-state router of Theorem 4.3
   whose full signed palette ledger never creates an undeclared hole;
3. the bounds (6.3) at every state and transition, with the full boundary
   linkage relation stored whenever transitions are composed; and
4. an accepting terminal topology with `b=xi=0`.

If matching debt is allowed only inside a declared block, its proper states
need not be accepting, but they remain measured literal prefixes satisfying
(6.3) and the transition bound.  One Theorem 5.1 linkage closes the block.
Equivalently, a contracted atomic-block arc must export the maxima of `xi`,
boundary adhesion, and transition linkage over its fail-closed interior.
Every internal circuit must still be literally alternating/legal, and its
signed palette ledger, protected support, and any topology/residence row
required by the application must be certified.
For a packet whose cardinality grows, uniform bounded-state recursion
requires a decomposition into blocks with common bounds `w,ell,a`; taking
the intersection of the first and last graphs of the whole growing packet
need not have bounded linkage width.

#### Proof

Necessity follows by reading the serviced occurrence jobs, literal supports,
prefix states, maximum-matching deficiencies, boundary signatures, and
matching symmetric differences from an installed packet.  For sufficiency,
follow the maximal chain.  The signed ledger preserves the declared palette
state and the exact port signature makes each topology transition legal.
At every block boundary, toggle the stored maximum matching along the
supplied vertex-disjoint linkage and along any stored rank-neutral
alternating cycles/even paths in the symmetric difference; this realizes the
next declared matching with at most `ell` augmenting linkage paths and leaves
at most `w` correlation exposures.  If downstream matching identity is
irrelevant, one may instead declare the path-toggle output itself.  Induction
reaches the terminal state, where `b=xi=0` makes the declared matching
perfect.  The argument never uses the number of completed blocks.  \(\square\)

The scalar inequalities in (6.3) are not themselves a state compression:
the pairing-resolved linkage and reachability relation in `theta` is
essential.  Theorem 6.4 says exactly what a bounded-state construction must
supply; it does not assert that PBBS provides such signatures uniformly.

### Theorem 6.5 (state-expanded criterion, allowing neutral/overlapping circuits)

Assume monotone bounded service and let `Sigma` be a **Markov-sufficient exact
boundary state**: two partial factors with the same state have the same
legal bounded-port macro continuations, the same signed turn update for each
continuation, and the same next port/linkage/reachability state.  In addition,
`sigma` determines the current `xi`, its named boundary and adhesion, and the
common-core linkage width of every labelled continuation (or stores the exact
occurrence relation from which these are computed).  The state must retain
the full pairing-resolved linkage relation; ranks alone are not
Markov-sufficient.

Form the layered directed graph whose vertices are

\[
 (H_-,H_+,U,\sigma),\qquad \sigma\in\Sigma,
\tag{6.4}
\]

where `H_-,H_+` are the still-unserved occurrence-labelled defect jobs.  At
the initial vertex these banks enumerate every actual palette hole, and the
arc ledger forbids creation of an undeclared hole.  The coordinate `U` is an
exact used-resource/stage state equipped with a declared finite acyclic
progress order.  Put
an arc labelled by macro `e` when `e` is physically legal in state `sigma`,
services declared subsets \(T_e^-\subseteq H_-\),
\(T_e^+\subseteq H_+\) (both may be empty), obeys the full collateral
ledger, has `xi<=w` and transition linkage width at most `ell`, and produces
a state of boundary adhesion at most `a`.  Every arc must either service at
least one defect job or strictly advance `U`.  A bounded macro may service
several jobs inseparably, and a q1-neutral rethread is represented by an
empty-service progress arc.  Macros may overlap supports at different times;
legality is checked on the current state.

Retain only state vertices, including the literal initial vertex, satisfying
`xi<=w` and \(|\partial\theta|\le a\); retain only arcs with `lambda<=ell`.

Then an ordered `(w,ell,a)`-controlled packet exists if and only if this
state-expanded graph has a directed path from the literal initial state to

\[
 (\varnothing,\varnothing,U_{\rm accept},\sigma_{\rm accept})
\tag{6.5}
\]

with accepting topology and `xi=0`.

#### Proof

Every installed packet records such a path.  Conversely, read the arc labels
of a path in order.  Markov sufficiency makes every represented macro a legal
transition in the current literal class; the arc predicates enforce the
palette, debt, linkage, and boundary bounds.  The layer loses at least one
job or strictly advances the finite acyclic progress state at every step, so a
represented path is finite.  At (6.5), there is no palette floor and no
correlation debt, hence the stored maximum matching is perfect.  \(\square\)

Theorem 6.5 is an exact selection criterion, not a polynomial-time claim.
On the support-disjoint face, `sigma` is the safe subset/port state and it
specializes to Theorem 6.4.  Under private Cartesian compatibility, its
static job selection reduces further to the Hall flows of Theorem 6.1.  A
uniform recursion must prove that `Sigma` has bounded live adhesion; using
the entire factor as `sigma` makes the equivalence true but vacuous.

## 7. Free and stabilized orbit corollaries

Let a defect orbit have lower and upper classes

\[
 H_-^O=\{\ell_i:i\in\mathbb Z_q\},
 \qquad
 H_+^O=\{u_i:i\in\mathbb Z_q\}.
\tag{7.1}
\]

Here `q=k` for a free coordinate-rotation orbit and `q<k` for a stabilized
orbit.  Suppose the allowed service pairs are translation-invariant:

\[
 \ell_i u_{i+s}\quad(i\in\mathbb Z_q, s\in S).
\tag{7.2}
\]

### Corollary 7.1 (orbit Hall)

If `S` is nonempty, the graph (7.2) is balanced `|S|`-regular and satisfies
Hall.  In fact every fixed `s in S` gives the perfect matching

\[
 \{\ell_i u_{i+s}:i\in\mathbb Z_q\}.
\tag{7.3}
\]

If the macros on one such matching have saturating donor flows,
line-conflict supports, a relay-valid order and terminal linkage, they repair
the entire orbit.

#### Proof

Translation by a fixed `s` is a permutation of `Z_q`, proving (7.3).  Apply
Theorem 6.1.  \(\square\)

Thus free defect orbits at `m>=6` require no new symmetry principle.  They
require physical macros for at least one shift and the independent relay and
terminal-linkage rows.  Partial free-orbit defect sets, or unions sharing
donor capacity, revert to the general Hall inequalities (2.2)--(3.3).

For many orbits, take their disjoint union.  If donor tokens, physical
supports and terminal private routes are orbit-private, solve each orbit and
concatenate any topological ordering of the orbit relay DAG.  Cross-orbit
macros are allowed by Theorem 6.1 but destroy this product simplification.

## 8. The `m=5` packet as a three-step relay

For the repaired standard `m=5` candidate, the service matching is

\[
 73\longleftrightarrow365,\qquad
 146\longleftrightarrow219,\qquad
 292\longleftrightarrow438.
\tag{8.1}
\]

These are the three induced lower-hole/upper-hole pairings at a cyclic
offset; each literal macro also carries its occurrence-labelled donor jobs.
The three `C10` supports are pairwise vertex-disjoint and the full signed
ledgers are turn-monotone.

Topology is not three independent moves.  The first two macros are direct
filters; the third is a relay which is not Hamilton-safe alone but is safe
after the first two.  Hence one valid relay layering is

\[
 \{C_1,C_2\}\prec\{C_3\}.
\tag{8.2}
\]

More exactly, among the eight subsets the Hamilton-safe ones are

\[
 \varnothing,\quad\{C_1\},\quad\{C_2\},\quad
 \{C_1,C_2\},\quad\{C_1,C_2,C_3\}.
\tag{8.3}
\]

The component counts in selector order `000,001,...,111` are
`1,1,1,1,2,3,2,1`.  Thus Theorem 4.3 permits exactly the two orders
`C1,C2,C3` and `C2,C1,C3`.  After complementing the repaired upper class,
the defect-relay projection is the directed cycle

\[
 73\longrightarrow146\longrightarrow292\longrightarrow73.
\tag{8.4}
\]

Its head-to-tail Euler order is `C1,C2,C3`; the other topology-safe order
shows that this Euler description is a useful projection, not the complete
contextual legality state.

The final common augmented graph has matching rank `197` on shores of order
`210`, so `r=13`.  Thirteen vertex-disjoint terminal augmenting paths
discharge the debt; no proper-prefix perfect matching is used.  The selected
packet therefore directly witnesses the conclusion of Theorem 6.1.  This
does not certify that the whole surrounding `C10` catalogue is line-conflict.

After the packet, the two standard glues lie on the prepared private face
with attachment paths

\[
 [82]-g-[84]-g-[88],\qquad
 [50]-g-[52]-g-[56].
\tag{8.5}
\]

This is the first exact packet followed by a prepared private **gap-owner**
gluing base.  The displayed private paths are not named physical endpoint
sockets, and the strict run/deeper-shadow/compiler interfaces are separate.
It does not prove the orbit hypotheses or terminal linkage uniformly.

The authoritative downstream replay sharpens this boundary.  A
colour-injective `42`-connector closure of the synchronized repaired forest
covers the complete upper/lower flag tower through every depth, and `46`
edge cuts preserve that support.  Nevertheless every intact-path opening
contains one of `31` internally bounded coordinate one-runs of length two.
For `d=2`, residence requires length at least three, and path permutation,
reversal, and endpoint/socket choice cannot change an internal run.  Hence an
interior rethread is mandatory for that fixed forest.

Item 2188 now supplies such a rethread at `m=5`: another exact diamond
matching has both q1 palettes, a `210`-edge/`42`-path forest, and no internal
positive run shorter than three.  Residence is therefore not an intrinsic
central-palette obstruction.  The new forest still has `21` deeper internal
target debts and unjoined endpoint runs.  Moreover its `119` changed matching
partners certify the endpoint matching, not a fail-closed ordered circuit
history through the controlled state of Theorem 6.5.  The remaining finite
gate is a residence-compatible, all-depth connector chronology followed by
the compiler.

### 8.1 Controlled-debt calibration at `m=5`

On shores of order `N=210`, the eight packet-subset augmented ranks in
selector order are

\[
 207,208,208,209,208,209,209,210.
\tag{8.6}
\]

Along either legal chain from (8.3), the forced hole floor is `3,2,1,0` and
the matching deficiency is also `3,2,1,0`.  Hence the live correlation debt
is identically

\[
 \xi=0.
\tag{8.7}
\]

Treating the three switches as one atomic block, the source/final common
core has rank `197` and its terminal linkage has width `ell=13`.  Thus this
literal finite packet calibrates `w=0` and `ell=13` at the palette/matching
level.  Its three circuits have `30` support vertices and its exact topology
is the eight-state subset automaton.  After any explicit finite named-boundary
convention it is `(0,13,a)`-controlled for the resulting finite `a`; no
particular numerical `a` is claimed here.  It proves the architecture at
`m=5`; it does not give a uniform bound on future packet interfaces.

### 8.2 Exact K17 bank test

For the frozen K17 common-exterior bank, `N=43758`.  The source has lower
hole floor `b=3826`, matching rank `39624`, and therefore

\[
 N-39624=4134=3826+308,
 \qquad \xi_{\rm source}=308.
\tag{8.8}
\]

The `C10` packet serial `3836` gains four missing lower colours, loses none,
preserves the upper multiset, and has source/common/candidate ranks

\[
 39624,\quad39622,\quad39628.
\tag{8.9}
\]

Its candidate floor is `3822`, its deficiency is `4130`, and its correlation
debt remains `308`; six common-core augmenting paths give `ell=6`.  Its
literal topology changes `11` components to `9`.  It is therefore a valid
one-step excess-nonincreasing bounded-service transition of Theorem 6.5 with
`w=308`, not a unit/unit Theorem 6.1 macro and not an accepting packet.

Serial `919` gains two lower colours without loss and has
source/common/candidate ranks

\[
 39624,\quad39623,\quad39627.
\tag{8.10}
\]

Its floor is `3824`, deficiency `4131`, correlation debt `307`, and linkage
width `ell=4`.  It is a strict correlation-debt descent transition.

The complete common-exterior `C8/C10` census (`4155` packets, `451`
positive-support rows) therefore verifies that the abstract state has
literal K17 transitions.  It does **not** verify a compound maximal chain
covering all `3826` holes, a dimension-uniform bound replacing `w=308`, an
accepting topology, residence, deeper shadows, or the compiler.  Indeed the
shell-tight inequality requires at least

\[
 \left\lceil\frac{308+s}{3}\right\rceil
\tag{8.11}
\]

new joint columns after servicing `s` holes.  This is evidence for a growing
packet with bounded local ports, not for a bounded number of switches.

In particular, any Theorem 6.5 path starting at this frozen source has
`w>=308`; the initial-state clause forbids hiding that debt.  A uniform
bounded-width recursion would need a separately certified bootstrap block
whose endpoint reduces `xi` to the uniform bound.  Matching acceptance may
be deferred inside that block, but its literal circuit legality, palette
ledger, protected topology, and other required physical rows may not.

## 9. Sharp independence obstructions

Every row of Theorem 6.1 is necessary even in tiny abstract catalogues.

1. **Shore Hall.**  One hole with no donor neighbour cannot be repaired,
   regardless of upper macros or topology.
2. **Compatibility Hall.**  Two lower jobs both adjacent only to one upper
   job pass their separate shore flows but have no macro perfect matching.
3. **Physical line conflict.**  Two disjoint compatibility edges may use one
   common physical vertex.  The compatibility perfect matching then is not
   installable.  A sharp `2 x 2` fixture has lower jobs `l_1,l_2`, upper jobs
   `u_1,u_2`, and capacity-one resources `p,q`: let the diagonal macros
   `x_11,x_22` both use `p`, and the off-diagonal macros `x_12,x_21` both use
   `q`.  The compatibility graph is `K_{2,2}` and the half-vector
   `x_ij=1/2` satisfies every job and resource row, but each of its two
   integral perfect matchings overloads one resource.  Allowing arbitrary
   such conflicts recovers hypergraph matching and contains `3DM`.
4. **Relay cycle.**  Two disjoint macros can each require the other to be
   installed first.  Every static Hall condition passes but no first move is
   legal.
5. **Terminal linkage.**  Let exposed sources be `a,b`, sinks `c,d`, and let
   all final directed paths end at `c`.  Turn transport and topology can be
   perfect while the terminal linkage rank is one rather than two.

These examples also show why “common-core debt is discharged at the end” is
a positive freedom, not permission to omit the final gammoid cut.

## 10. Exact remaining existence lemma

The transport theorem reduces the all-`m` task to the following concrete
supply statement.

> For every defect orbit of a recursively supplied factor, build saturated
> occurrence-level shore transport graphs, a line-conflict bounded macro
> lift satisfying compatibility Hall, an acyclic topology relay, and a
> terminal common-core linkage; make these banks private or compatibly
> layered across all orbits and later transparent glues.

This is broader than the stabilizer-three necklace conjecture and explicitly
includes free orbits.  It is not proved here.  General macro catalogues need
not lie on this tractable face, and Theorem 6.1 makes no claim that PBBS/MMM
automatically supplies it.

The Pascal determinant split rules out the scalar alternative “take two
complete parent states and splice them.”  Two full embedded parent solutions
force enough cross-rail edges to create a cycle.  Even one chosen contraction
arc `T -> H` is legal only when the residual selection is acyclic and has no
`H -> T` path.  Thus an induction must carry boundary-deficient rails and an
endpoint/reachability relation.  This is exactly the role of the safe port
state in Theorem 4.3 and the terminal linkage state in Theorem 5.1; it is not
optional bookkeeping.

The corrected uniform target is therefore:

1. an ordered controlled-debt packet of bounded-port circuits, allowing
   q1-neutral interior rethreads and possibly growing cardinality, ending in
   one exact internally resident decoration and discharging its common-core
   linkage;
2. an ordered fixed-decoration transparent, leaf-peelable connector/gluing
   list whose linear opening preserves residence and supplies every all-depth
   target; and
3. a literal compiler/common-cap module.

Theorem 6.5 models the abstract product state for these rows, but uniform
existence of its run/provider/reachability transitions and the compiler is
not proved.

## 11. Audit boundary

The Hall and terminal-linkage statements are standard integral max-flow and
Berge--Menger equivalences; their proofs above are independent of finite
search.  The `m=5` numerical instance is frozen in

```text
MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md
scratch/catalan_standard_m5_three_c10_private_repair_20260731.audit.json
```

and is independently replayed by

```text
scratch/audit_catalan_standard_m5_three_c10_private_repair_independent_20260731.py
scratch/audit_r_catalan_prepared_private_palette_gate_20260731.py
```

The latter independently checks the repaired two-glue prepared factorization
and literal binary-trace guards; those guards are not the failed `d=2`
coordinate-residence condition.  No claim in this note uses a K16/K17 SAT
result.
The fixed-decoration transparency criterion and the `ML(7)` counts are taken
only from

```text
MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md
```

and are used here to separate zero-debt transparent glues from defect-moving
macros with terminally discharged matching debt.

The K17 ranks and linkage widths in Section 8.2 come from the
implementation-independent proof-carrying replay

```text
scratch/threadD_k17_commonext_packets_3836_919_independent_20260731.audit.json
```

The lightweight independent synthesis check is

```text
scratch/audit_r_turn_defect_transport_controlled_debt_20260731.py
```

It rechecks the abstract resource/linkage counterexamples, the ML(7) counts,
the m5 safe cube and debt profile, and both K17 arithmetic rows.  No new
finite search is used.

The all-`m` run ledger and the independently replayed q1-neutral `m=5`
endpoint are frozen separately in

```text
MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md
scratch/catalan_m5_residence_rethread_c4c6_20260731.audit.json
```

Only the final rethreaded matching is used here; no ordered `C4/C6` history
is inferred from its generator provenance.
