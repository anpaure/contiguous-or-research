# Shortest honest all-k chain and the exact missing theorem

Date: 2026-07-31  
Status: exact implication and scope synthesis; no all-k existence claim

## 0. Verdict

There are two different statements which must not be conflated.

1.  The **central Catalan gate** is the Catalan Linear Matching Theorem:
    the diamond graph has a perfect matching whose Johnson lift is a
    spanning \(\operatorname{Cat}_m\)-path forest.  Its logically weakest
    normal form is the direct ordered four-transversal.  A decorated
    middle-levels cycle is only a sufficient subclass and carries extra
    gap--Hall, trace, socket and voltage constraints.
2.  The **full word theorem** needs more than the central gate.  It needs
    residence, every deeper upper shadow, and an integral lower compiler in
    one chronology.  The exact single missing all-k statement is therefore
    the Regenerative Shadow--Braid Existence Theorem below, not Catalan
    Linear Matching by itself.

There is now an exact intermediate target.  Zero-defect RSB is needed for
`nu(k)=B(k)`, but `nu(k)<=B(k)+O(1)` only needs one compatible infinite odd
sidecar spine with uniformly bounded odd/even terminal repair charge.
Terminal holes are paid once and are not exported.  A carried potential
`Phi` with `Phi'<=rho Phi+beta`, `rho<1`, gives an explicit additive
constant.  This bounded-defect implication is proved in
`MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md`;
existence of such a spine remains open.

The weakening includes the central row: boundedly many missing middle masks
may be appended at terminal cost.  Thus the exact Catalan Linear Matching
Theorem remains the clean central target for equality, while a uniformly
bounded-defect ordered four-transversal/owner state is sufficient for the
additive-constant conjecture, provided that defect is also regenerated on
the auxiliary spine.

The repair theorem cannot be reduced further to bounded-radius local
descent.  Exact two-toggle examples have deficiency profile `1,2,2,0`, and
for every fixed radius there are states from which every nonempty move of at
most that radius is uphill although the full compound is exact.  Therefore
the correct positive object is a bank of **closed compound packets** with
either a serializable unit-debt max-flow, a guarded Rado/gammoid rank
certificate, or the exact global guarded cost-to-go.  Raw atomic deficiency
is not a Lyapunov function.

The best division of labour is consequently:

* target the direct ordered four-transversal when proving the central
  Catalan existence theorem;
* use the alternating-SDR/transparent-gluing formulation as a constructive
  recursive certificate generator, because it has finite local transfer
  rules;
* never infer that success in that narrower trace fibre is necessary for
  an arbitrary ordered four-transversal or for an optimal word.

There is now a further exact quantifier simplification inside the trace
lane.  Any two spanning 2-factors differ by edge-disjoint alternating
circuits.  Hence one may first use arbitrary Middle Levels/ECO gluing to
obtain any spanning 2-factor, forget all decoration/owner/router data used
by that construction, and only then rethread to an accepting decorated
2-factor.  Such a repair packet exists if and only if an accepting
componentwise decorated 2-factor exists at all.

There is an even weaker and now demonstrably necessary forest-first route.
Given any spanning physical linear-forest support `R`, the central Catalan
selection exists on `R` if and only if the occurrence graph between its
lower and upper colours has a perfect matching.  This is ordinary Hall/Rado;
the physical degree and acyclicity rows have already been paid by the
support.  At `m=3`, every one of the 6,272 spanning two-factors in the
frozen GMM/complement union is Hall-deficient, while exactly 28 Hamilton-
path supports in the same union pass Hall.  Thus neither Hamiltonicity nor
completion of the unused edges to a 2-factor belongs in the minimal central
theorem.  The direct ordered-diamond four-graph has outer degree
`m(m+1)`, middle-role degree `m^2`, and maximum codegree `m`; its exact
outer slack and normalized codegree are both `Theta(1/m)`.  Generic sparse
matching is therefore only an approximate input.  The missing direct step
is exact outer absorption together with directed-cycle elimination, or the
equivalent forest-support Hall theorem.

The local atom for that absorption step is now explicit.  For every lower
set `L` and upper set `U`, an alternating inclusion path has an off matching
covering exactly its internal outer vertices and an on matching covering the
same vertices together with `L,U`; both states lift to pairwise
middle-disjoint Johnson edges.  For `|L-U|>=3` this has been strengthened:
**any** prescribed first diamond above `L` and **any** prescribed last
diamond below `U` extend to such an absorber of support length at most
`2m+1`.  Thus the two boundary resource pairs are completely independent.
The fixed-filler subfamily really did have a rare common-boundary event of
probability `O(1/m)` at density `Theta(1/m)`; the independent-boundary
construction removes it rather than merely hiding it in a factorial first
moment.

Raw capacity is also no longer open.  A greedy resource deletion argument
packs at least `Cat_m` direct absorbers disjoint in all four resource
classes for every `m>=4`.  What remains is genuinely global: select a
robust endpoint template, realize all its required corridors mutually
resource-disjoint, correlate the bulk leave with its flexible bank, and
eliminate directed cycles.  A promising intermediate scale is survival
`p=m^(-1/3)`: the residual degree is `Theta(m)=Theta(log N)`, residual
pair-codegree is `Theta(m^(1/3))`, and the independent-boundary corridors
have superpolynomial schedule room.  However, those local parameters are
now known not to imply the needed residual theorem.  A probabilistically
sparsified four-partite space barrier has all degrees
`(1+o(1))Theta(log N)`, maximum pair-codegree two, and a perfect outer
projection, yet has no outer-perfect four-resource matching because one
middle label class is smaller than its forced outer preimage by one.  The
missing hypothesis must include robust four-resource fractional/capacity
expansion and a local transferral lattice; ordinary outer Hall is
insufficient.

There is a structured replacement for an arbitrary logarithmic residual.
Fix a balanced `a`-set on `2a` collar coordinates.  The induced central
subcube is literally the full ordered-diamond problem at parameter `m-a`;
for `a=(1/6+o(1))log_2 m` it has density `Theta(m^(-1/3))` and inherits the
exact uniform fractional point.  Removing it damages the ambient uniform
solution only in a radius-two trace collar: first-collar outer vertices have
deficit `2/(m+1)`, second-collar vertices have deficit `2/[m(m+1)]`, and all
other outer rows remain exact.  Thus the residual space barrier can be
removed deterministically at the cost of one explicit polynomial-size
collar braid.

The outer half of that braid is already integral.  A product SCD can be
chosen with the fixed balanced collar set as a singleton chain.  The
ambient SCD then contains the whole child subcube as a literal sub-SCD;
after deleting the child flags, its remaining central flags perfectly match
all nonchild lower and upper resources and use distinct nonchild on-chain
middle owners.  For this supplied state only opposite-middle injection and
physical acyclicity remain.  The canonical product still has large
opposite-corner fibres, so this is a three-resource completion theorem, not
Catalan Linear Matching.  The current direct target is therefore the exact
radius-two collar rethread which repairs those opposite corners while
leaving the recursive child frozen.

The two-coordinate version is now sharper.  Orient the recursive child
Catalan forest and, for every removed child edge, reuse its old tail and
head as the two cross-sector ports.  This preserves every central-trace
physical degree exactly, so the former middle-port collision row vanishes.
The two diagonal incidence rows are also automatic.  A strengthened
Kruskal--Katona chord proves that the dual two-step transversal matroid has
rank density at least

```text
Cat_(n+1)/binom(2n,n-1)
```

on every relevant subset.  Pulling the upper and lower dual matroids back
through the child tail/head injections makes Edmonds' common-basis
inequality hold term by term.  Hence every child forest has a synchronized
`Cat_(n+1)` deletion bank, and even a distribution on such banks with
uniform edge marginals.  Literal integral lifts pass at child parameters
`n=3,4`, producing the full parameter-`4,5` Catalan forests.

What remains in this recursion is now purely physical: realize the two
guaranteed diagonal bases as punctured side forests with seam-anchor degree
at most one, and make their contracted attachment multigraph acyclic.
The side component ledger is exact.  If the degree caps hold, each side
component contains zero, one or two anchors and

```text
     (# double-anchor components)-(# empty components)=Cat_n.
```

Thus scalar capacity, separate Hall and synchronized common-basis
integrality are no longer gates.  The missing central theorem is a
forest-compatible realization/interlacing theorem.

The **asymptotic** version of that physical row is now unconditional for
every preselected common basis.  For fixed `Q`, its four-uniform
capacity-slot hypergraph has maximum degree `D=Theta(n^2)`, codegree
`O(n)`, and edge count `(1-O(1/n))PD`.  Delcourt--Postle's conflict-free
coloring corollary applies despite the host's irregularity; forbidding
projected cycles through a fixed length and then diagonalizing the length
gives a physical linear forest with `P-o(P)` atoms on each shore.  The
existing attachment pruning retains all seams and costs another
`2 Cat_(n+1)=o(P)` atoms.  Hence common-basis quasirandomness is no longer a
bridge.  What remains is exact zero-defect physicalization and its joint
residence/shadow/common-cap regeneration, not asymptotic incidence supply.

The quantifier cannot be strengthened to exact physicalization for every
common basis.  For fixed `Q`, fractional outer-perfect physicalization has
an exact weighted-cut deficiency `rho(Q)`, obtained by dualizing artificial
owner capacities.  The authenticated bad parameter-three common basis has
`rho(Q)=1`, with matching primal and dual certificates.  Thus even the
fractional exact row can fail before integrality or graphic acyclicity.  The
correct recursion is bank-flexible: jointly choose the path-dependent
endpoint bank and a compatible common basis with `rho(Q)=0`, and only then
round/cover down.  Generic bounded-colour splitting cannot replace this
choice: affine linear four-partite hosts with codegree one have globally
unique factorizations for every retained palette of two, three or four
perfect colours.  Any positive colouring proof must therefore use the full
many-colour Boolean geometry or a separately constructed balanced absorber.
Before `Q` is rounded, this first row is now exact rather than qualitative:
Farkas duality writes both physical-shore conditions as families of modular
linear inequalities in the puncture vector `q`.  Intersecting them with the
strict common-base polytope has a polynomial separation oracle.  The open
step is integral/graphic rounding of this explicitly separated joint
polytope (or absorption around it), not discovery of another marginal
condition.

The first literal straddling row now clarifies what such rounding can and
cannot mean.  Complementing an upper physical row of cost
`z_(U_e)-a_(t_e)` gives lower cost
`z_(complement L_e)-a_(complement h_e)`, with no sign/permutation relation
unless the oriented parent has an additional complement-reversing
automorphism.  In the authenticated `n=3` parent the displayed positive
upper row becomes a redundant lower row, so physical rows do not pair
one-by-one under complement.  Yet the complete two-shore system has a
53-multiplier exact dual proving `sum_(i<14)p_i<=0`; its fractional
projection is the singleton integral bank `p_14=1`, and that bank has a
literal two-shore attachment-forest witness.  Thus aggregate donor coupling
can restore integrality even when rowwise face alignment and rowwise
complement pairing both fail.

On the strict direct-recursion face, the SBE load itself now has a smaller
exact normal form.  Uniform weight `1/(n+2)` on every occurrence saturates
all outer vertices.  The remaining middle debt is

```text
 internal       -2/[n(n+2)]
 unchosen end   -1/n
 chosen end      3/(n+2)
 isolated        2/(n+2).
```

A child path of length `ell` consequently has total debt
`2(n-ell)/[n(n+2)]`, independent of its orientation; reversal changes only
one endpoint dipole of strength `C/N`.  Since the average component length
is exactly `n`, these debts balance globally.  Strict balanced expansion is
equivalent to routing this explicit demand by row-sum-zero occurrence
adjustments of negative capacity `1/(n+2)`.  This does not prove
preservation, but it replaces the raw exponential Hall family by a bounded
transshipment invariant whose sources and sinks are completely known.

Retaining the **whole** conflict-free colouring gives one further exact
global structure, but not the hoped-for local absorber.  If `M_c` are its
colour classes and `R_c` their four-resource supports, then

```text
sum_c (P-|M_c|) = qP-|E(G_Q)|,
sum_(c<d) |R_c triangle R_d| = sum_v d(v)(q-d(v)).
```

The fixed-`Q` degree ledger therefore yields two `P-o(P)` colour classes
whose supports differ on only `o(P)` resources; after the usual long-cycle
deletions they are two such linear forests.  Their difference is a
canonical few-terminal exchange network: shared resources join opposite
colour atoms, support-symmetric-difference resources are terminals, every
atom has total degree four, and all but `o(P)` atoms lie in the four-valent
core.  Terminal-free connected components are exact count-neutral
four-resource trades, and every support-preserving two-colour switch is a
union of such components.  This is a genuine distributed global reservoir.
It is not a serializable ear theorem: one component can have `Theta(P)`
atoms and all terminals can lie in one component.  An infinite linear
four-partite example with codegree one has connected four-regular exchange
graphs for every colour pair, and a literal fixed-`Q`, `n=3` fixture has two
outer `C6` phases locked together by cross-slot dependencies.  Thus exact
cover-down now needs a multi-colour protected four-core splitting theorem
using additional Boolean/Johnson geometry; bounded bichromatic `C6/C8`
absorbers do not follow from Delcourt--Postle alone.

Boolean geometry nevertheless supplies an explicit absorber once it is
planted rather than inferred from an arbitrary pair of colours.  The
suspended transparent incidence hex is a literal fixed-four
`2 -> 3` gain-one packet: its full old and new phases use the same three
lower colours, three upper colours and six physical slots, and both project
to three-edge forests.  Every formal target has `2n(n-2)` embeddings.  A
full symmetric-orbit packing contains more than `P/54` pairwise-private
packets, and the uniform common-basis marginal distribution preserves
`1-O(1/n)` of any prepacked bank.  Thus absorber **supply** is linear and no
longer the gate.  The remaining correlation is to plant an `o(P)` off-state
subbank and construct the near-forest so its leave is exactly the designated
packet boundary while retaining the graphic/root/common-cap rows.  Sparse
induced `2ell`-cycle switches (`ell>=5`) add variable-length count-neutral
rerouters whose two physical phases are both linear forests; these may align
the leave but do not provide gain.  Together they replace the vague request
for generic local circuits by a concrete two-move catalogue: gain-one hexes
plus sparse-cycle kernel rerouting.

The Joos--Mubayi--Smith tripartite completion theorem does not combine these
two ingredients automatically.  In the natural fixed-four encoding one has
`(p,q,r)=(1,3,3)`, but uniformly for every fixed common basis

```text
d = Theta(n^2),  |P union Q| = exp(Theta(n)),
Delta_2(H_1) >= 2n-O(1).
```

Its size condition therefore requires `epsilon>=2^(-1/3)-o(1)`, while its
codegree condition requires `epsilon<=1/2+o(1)`.  The `>P/54` hex bank is a
global packet count, whereas the completion row requires at least
`d^epsilon` locally spread choices at every designated target.  Fixed
conflict arity would in any event forbid only bounded cycles.  Thus JMS does
not turn the arbitrary-`Q` near forest into an exact forest; a genuinely
small resource-disjoint block decomposition could still create a future
local application.

The topology part has a useful abstract decoupling, but not the initially
claimed physical one.  A side forest with no anchor-free component has
exactly `Cat_n` double-anchor paths and all remaining anchors one per
component.  The child segments induce only a partial matching between the
two seam shores.  Given any abstract Catalan-size pairing on the first
shore, a greedy component-merging argument chooses an abstract pairing on
the second shore whose union with the child relation is acyclic, using only
`Cat_(n+1)>2 Cat_n`.  Physical pairings, however, obey

```text
sum d_J(anchor pair) <= binom(2n,n-2),
```

and maximum-distance requests violate this budget in every `n>=3`.
Therefore the universal prescribed-pair shore theorem is false.  The exact
gate is joint and existential: choose the common basis, both physical side
forests and their induced pairings so that the two pairing families meet
the graphic completion class of the central partial matching.  A strict
edgewise child-lift realizes this joint system in an actual recursive chain
through child `n=5`; proving its propagation is the lead central route.

Two apparently simpler finishes are now quantitatively closed.  On a
uniform random perfect matching of the outer diamond graph, the canonical
three-edge overload events have conflict degree `3m^6+O(m^5)`; even the
optimistic probability `d^(-3)` gives `pD->24`, and an exact `m=3` audit
shows endpoint-disjoint events do not furnish the hoped-for lopsided
dependency graph.  Conditional on cap two, canonical whole-cycle shifts
are also incomplete: 73.52 percent of the cyclic `m=3` states are locked
against both shifts.  The collar theorem must therefore use correlated
factorization or compound circuits, not a routine LLL followed by one
cycle switch.

Hamiltonicity is itself unnecessary.  Global bijectivity of the two turn
palettes and componentwise alternation of selected shore types already
produce a perfect diamond matching.  Its lift is a spanning `Cat_m`-path
forest provided every marked component contains at least one unmarked
occurrence and is off the ordinary binary cycle face.  A wholly marked
component instead contributes two rail cycles; a wholly unmarked component
uses either residual cross-matching phase.  Thus the corrected Decorated
Middle Levels 2-Factor Theorem is
the weakest current trace target.  A decorated Hamilton cycle and a
transparent gluing tree are successively stronger constructive states, not
necessary interfaces for central existence.

The exact factor-level relational induction is now explicit.  For each
factor component (C), let (P_C) sum the monomials of all locally
forest-safe marked configurations, with constant coefficient two for its two
unmarked cross phases.  Then (P_F=prod_C P_C) supports an accepting
decoration exactly when the squarefree monomial containing every upper and
lower colour has positive coefficient.  Equivalently, node relations carry
disjoint consumed colour-set pairs and compose by disjoint-union join; the
root accepts at the full two palettes.  This is exact but may be exponential.
The remaining all-(m) statement is positivity of that coefficient for one
explicit recursively generated factor family, not component merging.

The first nontrivial trace base is now positive.  The explicit `ML(7)`
gap--Hall counterexample is repaired by one ordinary incidence-hex toggle,
and the repaired cycle has a spanning `Cat_4=14`-path lift.  What transfers
is not two separate turn rainbows: it is one **joint alternating SDR**.  A
single hex preserves a fixed decoration exactly when its selected local
turn-colour multisets agree on each shore and the retained-fragment boundary
mark types alternate after reconnection.  Thus a recursive construction must
choose a transparent gluing tree together with the SDR; an arbitrary frozen
SDR and an arbitrary published Middle-Levels gluing tree are each too weak.
Equivalently, in the weaker post-glue order, this same toggle is the smallest
literal example of rethreading a nondecorable Hamilton cycle to a decorable
one.  The six common-forest decorations in the local census show that the
strong transparent route is nonempty, while the terminal-only route needs no
common decoration across the toggle.

The correct recursive relaxation is now exact as well.  Instead of one
frozen SDR, carry the relation of all feasible augmented-matching boundary
degrees, occurrence mark states and finite trace-run summaries.  Natural
join followed by existential projection composes this relation exactly.  In
the Hamilton-restricted version, an empty-boundary accepting root is
equivalent to the terminal decorated-Hamilton condition.  For the weaker
2-factor target, the relation additionally retains the component partition
of open trace fragments and accepts at the root exactly when every terminal
component passes its own corrected trace test.  A scalar label “this glue is
transparent for some
decoration” does not compose: two vertex-disjoint `ML(7)` hexagons have
nonempty pairwise common-decoration sets but empty three-way intersection.
Thus the remaining recursive question is nonemptiness of the correlated
root relation, preferably through a bounded-adhesion or palette-private
decomposition.

For the additive-constant target, a lower-tight two-level cycle now has an
exact scalar central cost: if its upper turn collision excess is `delta`,
deletion gives central defect `max(1,delta)`.  XOR forces `delta>=2` in the
Mersenne dimensions `m=2^a-1`, and this is sharp at `m=3`.  More
importantly, the concrete binary `SatCycle::sat_2` recursion has
`Omega(Cat_m)` defect.  Any stateless sectorwise binary recursion changing
at most eight turn occurrences per splice has the same asymptotic failure;
nine is merely the first ledger-feasible width.  The positive `m=5`
three-`C10` repair acts on exactly nine signed palette entries per shore,
which makes it the first finite model for a stateful reset, but it does not
yet reset residence, deeper-provider and common-cap debt jointly.

This threshold is attained by a stronger literal cube.  One `C10` and its
first two rotations have pairwise disjoint supports; all eight subset states
are Hamiltonian and, with `s` switches selected, have exact defect triple
`(3-s,3-s,3-s)` for lower holes, upper holes and augmented matching
deficiency.  The invariant is matching-floor tightness: after isolated
palette holes are deleted, the augmented core has a perfect matching.  The
cube pads to every `m>=5`, but only for a private three-partition block of
holes with a common `(m-5)`-core.  Thus the live induction must normalize
its debt into such guarded blocks; padding does not provide arbitrary
packet supply.

The minimal balanced physical actuator is exact as well.  No nontrivial
two-column degree-balanced packet exists; every support-two three-column
packet is an alternating hexagon.  On the regenerated `K17` checkpoint a
complete census finds `13,871` one-path hex packets, including `165` that
improve rank-ten coverage while preserving the current residence and
capacity proxy floors.  An exact compound search selects `66` hexes and
independently replays every accepted prefix, reducing replay `748->735`,
strict `D2/D3` `503->502`, and upper holes
`1585/824/116/0 -> 1511/766/107/0`.  The accepted set contains `506`
two-packet subsets which are infeasible by themselves: compatibility is
nonhereditary, so a conflict graph, matroid or ordinary Rado packing is the
wrong global abstraction.  The correct object is a signed circulation with
topology and service constraints.  The fixed bank still leaves `1116`
rank-ten holes of service degree zero, requiring a regenerated base or
support-four/longer circuits.

The current `K17` construction supplies the first finite evidence that the
required state really has a base--fibre form rather than additive scalar
repairs.  Occurrence changes alter the macro endpoint demand; one must then
resolve an integral residual b-flow before applying degree-kernel circuits.
On the exact regenerated base, occurrence and kernel layers reduce replay
mismatches `3568 -> 748`; the guarded hex compound then reaches `735` while
preserving one-cycle/lower-q1 exactness and nonempty envelopes.  This is a
nontrivial multi-layer contraction witness, not an accepting RSB state or a
new `K17` bound.

## 1. Exact flat-carrier implication

For a linear word of sets \(X=(X_1,\ldots,X_s)\) define

\[
       (DX)_i=X_i\cup X_{i+1}.
\]

Then, by associativity and idempotence of union,

\[
       (D^qX)_i=X_i\cup\cdots\cup X_{i+q}.
\tag{1.1}
\]

Fix \(k\), put

\[
 r=\lceil k/2\rceil,\qquad W={k\choose r},\qquad
 d=d(k),\qquad L=W+d.
\]

### Theorem 1.1 (exact carrier--compiler criterion)

Suppose a length-\(L\) nonempty word \(A\) satisfies:

1. \(T=D^dA\) is a permutation of \(\binom{[k]}r\);
2. every nonempty set of rank below \(r\) occurs in one of
   \(D^0A,\ldots,D^{d-1}A\); and
3. every set of rank above \(r\) occurs in some \(D^qT\).

Then \(A\) is universal and \(\nu(k)\le W+d=B(k)\).

Conversely, these three conditions are necessary for a universal word
inside the flat-carrier class \(D^dA=\binom{[k]}r\).

#### Proof

Condition 1 covers the middle rank.  Condition 2 covers every shorter
target.  By (1.1),

\[
        D^qT=D^{q+d}A,
\]

so condition 3 covers every longer target by literal intervals of \(A\).
This covers every nonempty subset.  The converse is just the same partition
of interval lengths, restricted to the stated flat-carrier class.
\(\square\)

Together with the proved deadline inequality \(\nu(k)\ge B(k)\),
Theorem 1.1 shows that one certificate satisfying 1--3 proves equality.

## 2. Residence and the lower compiler

For each coordinate \(x\), write its indicator along \(T\).  The equation
\(D^dA=T\) is feasible coordinatewise exactly when every internal
one-run has length at least \(d+1\), with the corresponding one-sided
boundary conditions.  Equivalently the maximal legal cell at position
\(j\) is the erosion envelope

\[
        E_j=\bigcap_{i\le j\le i+d}T_i.
\tag{2.1}
\]

After the carrier is fixed, assigning the lower targets to the physical
short cells inside these envelopes is an exact system-of-distinct-
representatives problem.  Thus residence is the coordinatewise feasibility
gate and Hall is the integral correlation gate.  Neither follows from
middle-layer ownership alone.

## 3. What Catalan Linear Matching does and does not buy

On \(2m\) coordinates, a Catalan linear matching is equivalently an
ordered four-transversal

\[
 L\longmapsto
 (U_L=L+\{a_L,b_L\},\ T_L=L+a_L,\ H_L=L+b_L)
\]

with all three displayed maps injective and the directed graph
\(T_L\to H_L\) acyclic.  This produces exactly
\(\operatorname{Cat}_m\) paths and solves the two immediate turn
palettes.

It does **not** by itself provide:

* a linear chronology of those paths with safe seams;
* the run/residence inequalities needed for \(D^dA=T\);
* the shadows \(D^qT\) for \(q\ge2\); or
* the lower-target SDR inside (2.1).

The middle-levels trace specialization adds a common cycle on which the
four-transversal can be represented.  In return it must solve the exact
gap--Hall matching, the binary forest face, endpoint-labelled socket
closure and primitive voltage.  The new leaf-peelable/transparent-hex
theorems make these states finite and composable, but do not make them
automatic.

### Shortest exact trace-recursion state

At an accepting macro boundary the shortest currently proved trace state is

\[
                 \mathfrak S=(F,D_A,D_B,\Gamma,\chi),
\]

where \(F\) is the middle-levels factor, \((D_A,D_B)\) is one **joint**
alternating decoration realizing both turn palettes exactly, \(\Gamma\) is
its occurrence-labelled gap-colour forest with its unique leaf-peeling
matching, and \(\chi\) is either a protected trace breaker or the exact
“outside the cycle face” bit.  For a proposed incidence hexagon the complete
local signature is the two selected turn-colour multisets, the first/last
selected shore types on the retained fragments, and the component partition
of the old gap forest after its changed edges are deleted.  The same
decoration transfers exactly when the palette multisets agree, the fragment
boundaries alternate, and the new gap attachments are loopless and acyclic.
For recursive physical composition append either the full occurrence-
labelled socket path-cover relation or, only after node-private tree-
contiguity is proved, its endpoint-triple/gain compression.  Separate lower
and upper surjectivity is not a substitute for this joint state.

The common-core linkage theorem makes the bounded-switch part genuinely
finite-width.  An alternating \(2t\)-circuit changes at most \(t\) physical,
\(t\) upper-turn and \(t\) lower-turn augmented edges.  If the old
augmented deficiency is \(e\), restricting an old maximum matching to the
common graph leaves deficiency at most \(e+3t\).  Thus a bounded gluing
polygon needs at most \(e+3t\) simultaneous augmenting paths (at most
\(3t\) from a decorated parent).  Their width is bounded, although the
paths may still travel globally; this is a finite boundary state, not a
local-existence proof.

Hence the direct ordered four-transversal is the better theorem target;
the decorated trace is the better current recursive proof language.

There is now a sharp complexity boundary for the recursive catalogue.  Once
palettes are globally prepared and private old sockets are contracted, the
component-tree, effective gap-edge, and fixed-sink linkage rows are two
graphic matroids and one gammoid on the same labels.  Their unrestricted
three-row intersection already contains perfect three-dimensional matching.
On the private/aligned face, however, the gap row is automatic or identified
with the component row, leaving ordinary graphic--gammoid intersection.  If
there are \(q\) factor components, an accepted spanning tree then exists
exactly when

\[
 r_{\rm comp}(X)+r_{\rm link}(T\setminus X)\ge q-1
 \qquad\text{for every }X\subseteq T.
\tag{3.1}
\]

This is why private/aligned palette repairs are not merely convenient: they
move the recursion from a genuine three-way integral correlation problem to
an exact two-matroid min--max theorem.

The rank family (3.1) now has an exact connectivity form.  Let \(K\) be the
component-edge multigraph and \(N\) the fixed linkage router.  For a router
vertex set \(Y\), retain the collar edge \(c_t\) exactly when its source
still reaches the sink bank in \(N-Y\), and call the surviving graph \(K_Y\).
Then (3.1) is equivalent to

\[
                    c(K_Y)\le |Y|+1
                    \qquad(Y\subseteq V(N)).          \tag{3.2}
\]

Thus the post-repair selection problem is router-resilient connectivity:
deleting \(y\) routing resources may create at most \(y\) additional
component pieces.

On the all-six-marked face, local transparency simplifies further.  An
incidence hexagon is transparent exactly when its three lower ports have one
common external insertion label and its three upper ports have one common
external deletion label.  The corresponding owner palettes are two forced
three-cube faces.  A selected coherent-hex tree has a common joint decoration
exactly when its forced port colours extend to an upper-turn transversal and
one residual gap--colour perfect matching.  Consequently the prepared
transparent-gluing gate has three constructive rows only: coherent
component-edge supply, forced-port gap Hall, and (3.2).  The repaired `m=4`
cycle supplies transparent Hamilton rethreads but no component-merging one
in its immediate hex neighbourhood; item2171's separate standard-factor
fixture supplies the positive component merge.  These certificates must not
be conflated.

Two of those three rows now have exact recursive closures.  If the chosen
upper transversal has a gap--colour graph which is a forest with perfect
matching \(M\), forced-port Hall is equivalent to the pointwise owner test

\[
                 \operatorname{owner}_M(g(j))=\ell_j
                 \quad\hbox{at every forced lower port}.              \tag{3.3}
\]

If router-resilient blocks are joined along a tree and every tree adhesion
owns a pairwise-disjoint occurrence path to a dedicated sink, then

\[
c(K_Y)-1
=\sum_i\bigl(c((K_i)_{Y_i})-1\bigr)+|D(Y)|\le |Y|,                  \tag{3.4}
\]

where \(D(Y)\) is the set of killed tree adhesions, so router resilience is
automatic.  A laminar cut family is a weaker
alternative.  Gap/colour privacy and occurrence-route privacy are distinct:
the first cannot be used as evidence for the second.

Coherent component abundance is also no longer open, but compatibility is.
The standard MMM gluing label \(110u0v\leftrightarrow101u0v\) is all-six
coherent only for \(u=\varnothing\), so the canonical standard
arborescence is not the answer.  Nevertheless every Dyck parent
\(D=1u0v\) supplies the explicit coherent ECO hexagon with support word
\(1u000v0\).  Its three old factor edges are the three consecutive leaf
insertions into \(D\), and every standard MMM component adjacency is
co-contained in one such coherent hyperedge.  Hence the two-section of the
coherent ECO component hypergraph is connected in every dimension.
In one fixed rotation, the upper and lower forced-owner collision graphs
are even the same explicit path forest
\(1p100v\to1p010v\), with \(\operatorname{Cat}_{n-2}\) edges.  One
independent-set choice therefore removes local owner repetition on both
shores simultaneously.  The same path forest is also the complete physical
six-port overlap graph.  Orienting its edges assigns every shared old factor
edge to one endpoint and leaves pairwise-disjoint atom banks, with at most
two old edges removed from any atom.  This still does not produce a global
transversal or source-to-sink routes.

The terminal half of this collision choice is substantially better
behaved.  Keeping only parents whose first child forest is empty or does
not end in a leaf, the first two ECO roles give the safe-pull graph
`[1u100v]--[1u010v]`.  This graph is connected for every `n`.  Every unsafe
pull is conjugate to a safe pull by one or two preparatory safe pulls, giving
a deterministic replacement of length three or five while fixing all
outside cyclic orders.  Replacing the edges of the connected unrestricted
MMM leaf-pull graph proves the result.  The no-search audit checks every
blocked labelled case through `n=12`.  This closes collision-free component
two-section supply, but not simultaneous toggle compatibility; under the
weaker decorated-2-factor target it is also optional for central existence.

An ECO atom touching \(c\) old factor components has component rank
\(c-1\).  In particular, a three-component atom must export two independent
unit channels; representing the whole toggle by one source is rank-deficient.
After unit expansion, router resilience follows from one exact local lemma:
inside every owned atom bank, after its at-most-two shared edges are assigned
away, route those \(c-1\) sources disjointly to distinct sinks.  ECO genealogy
alone does not prove the lemma, because the same component/support data can
be realized with either dedicated routes or a shared unit bottleneck.
The missing datum is now exact: for each of the at most four ownership
states \(Q\), export the directed vertex-capacitated occurrence network,
distinct source set, sink bank, child exclusions and the semantic map to the
component-unit edges.  The state passes precisely when the vertex-split max
flow is \(\rho(Z)\) for every \(Q\).  The repaired project-\(m=5\)
singleton already exports and passes this oracle through its compiled arc;
the open statement is uniform production of the export.

The topology row is exact as well.  For an atom \(t\) touching component set
\(H_t\), put \(w_t=|H_t|-1\).  A selected strict family is a simultaneous
component hypertree exactly when

\[
 \sum_{t:H_t\subseteq A}w_t\le |A|-1\quad(\varnothing\ne A\subseteq V),
 \qquad \sum_tw_t=|V|-1.                              \tag{3.5a}
\]

Equivalently, its component--atom incidence graph is a tree, which supplies
a hyperleaf order.  Two-section connectivity and one-atom-per-pull-edge SDR
are both insufficient because a ternary atom is one indivisible rank-two
bundle.

There is an exact ordinary-tree form.  Choose a tree \(A\) on the old
components; an atom \(t\) is a tile only when \(A[H_t]\) is connected, and
the tiles must partition \(E(A)\).  On a path \(A\), interval tiles are
source--sink arcs, so the fixed-filter relaxation is an integral unit-flow
polytope.  The reduction is not without loss: on the first branching tree
\(K_{1,3}\), the three pair-of-arm ternary tiles have determinant two and
only the fractional cover \((1/2,1/2,1/2)\).  Thus a path/leaf-block
construction could remove a genuine integral obstruction which raw
connectedness cannot.

For the stronger **repair-first transparent-gluing route**, the exact
selection problem is therefore no longer “find coherent edges.”  It is:

> choose from the connected ECO supply a simultaneously executable
> component-spanning hypertree whose forced ports satisfy (3.3) in one
> joint decoration and whose occurrence sources satisfy the private or
> laminar router certificate (3.4).

Static hypergraph connectivity alone proves none of these correlated rows
in that stronger route.
Indeed the raw canonical project-\(m=5\) factor is the first exact
counterexample: all 648 minimal topology-safe two-ECO Hamilton sequences
already have disjoint forced faces on both shores, but miss the same three
upper and three lower period-three colours, so none even admits an upper
transversal.  The known synchronized three-switch repair is positive.
Consequently, if the repaired decoration must survive every subsequent
glue, the constructive order is load-bearing:

\[
 \boxed{\text{controlled-debt repair/rethread first; then select the
 private owner-aligned ECO hypertree jointly}.}                    \tag{3.5}
\]

This stronger order is not merely aspirational.  At project \(m=5\), the synchronized
three-\(C_{10}\) repair leaves two components and one transported
leaf-peelable decoration.  All five fixed-rotation ECO atoms survive the
repair and Hamiltonize; four are all-six marked and pointwise owner-aligned
in the same unique matching.  One isolated standard atom recovers the known
endpoint, while a nonstandard atom gives a new Hamilton endpoint outside the
standard two-glue cube.  Both preserve the accepting decoration literally.
Thus the first obstructed base validates repair-then-ECO exactly.  What is
open is its uniform export, not the finite compatibility mechanism.

For the **minimal trace route**, all owner-alignment, router and component-
merging rows above disappear.  By the 2-factor difference theorem, a finite
packet of alternating circuits carries any starting spanning 2-factor
through 2-factors to a terminal factor \(F_*\) exactly when such an accepting
\(F_*\) exists.  The weakest trace target is therefore:

> **Decorated Middle Levels 2-Factor Theorem.**  For every \(m\ge2\),
> \({\rm ML}(2m-1)\) has a spanning 2-factor with globally bijective upper
> and lower turn representatives, componentwise alternating selected shore
> types, such that every marked component contains an unmarked occurrence
> and is off the binary cycle face.

The componentwise decorated-cycle construction then gives the perfect
diamond matching and a spanning `Cat_m`-path forest directly.  Hamilton,
leaf-peelable and transparent-gluing versions are progressively stronger
useful induction targets.  The repaired `ML(7)` hexagon remains the first
literal Hamilton repair example, and its six common-forest toggles certify
that the strongest local route is nonempty.

## 4. Exact single missing all-k theorem

### Regenerative Shadow--Braid Existence Theorem (RSB)

For every \(k\) there is a certificate \((A,T,\mathcal P)\) such that:

1. \(|A|=B(k)\) and \(T=D^{d(k)}A\) enumerates every middle-rank
   set exactly once;
2. every coordinate run of \(T\) satisfies the exact depth-\(d(k)\)
   residence condition;
3. every upper target occurs in a consecutive union of \(T\);
4. the erosion-envelope incidence system has an SDR covering every lower
   target in the short derivative rows; and
5. \(\mathcal P\) is a finite protected-port state from which the Pascal
   odd-to-even and odd-to-odd braids construct certificates satisfying
   1--4 in the next dimensions.

The protected state in item 5 may be instantiated by the current exact
rows: a leaf-peelable joint alternating SDR, a leaf-transparent bulk-shell
gluing tree, a trace breaker, endpoint-labelled sockets with primitive
voltage, and compiler-compatible private guards.  Another construction may
use a weaker state; those particular trace constraints are sufficient, not
logically necessary.

Here “finite” means finite on each declared boundary, not a
dimension-independent anonymous alphabet.  The literal socket-permutation
realization gives (n!) pairwise completion-distinguishable routing states
on (n) live components.  Therefore a recursive proof must either carry the
full occurrence-labelled socket path-cover relation, or prove a locality
statement such as tree-contiguity, under which every proper subtree carries
one socket chain and an endpoint triple suffices.  The positive (m=4)
private-path fixture is evidence for this local face, not an all-(m)
locality theorem.

The most direct standard-tree strengthening is already false.  At (m=5),
both Hamilton cycles in the complete standard MMM gluing-label family miss
the same period-three orbit of three lower turn colours (and three upper
colours), although one of the two trees has disjoint all-six locally
transparent private triples at both glues.  Therefore the recursion must
include a palette-repair switch, a nonstandard gluing family, or a different
base factor before the private/local socket face can be used.  Local
transparency alone cannot manufacture globally absent colours.

That first failure is nevertheless repairable without abandoning the
private recursion.  Three pairwise vertex-disjoint (C_{10}) switches give
the exact deficit staircase

\[
 (3,3,3)\to(2,2,2)\to(1,1,1)\to(0,0,0),
\tag{4.1a}
\]

for the lower palette, upper palette, and joint alternating-SDR deficiency.
The resulting (m=5) decoration is leaf-peelable and trace-linear on the
entire two-standard-glue cube, and both private attachment paths survive.
Its common-core deficiency (13) is certified by (13) vertex-disjoint
augmenting paths.  Hence the corrected recursive central target is not an
arbitrary palette repair but a **controlled-debt packet of bounded-port
circuits followed by private/aligned gluing**.  Its number of circuits need
not be bounded independently of (m); what is finite at each step is the
live boundary and linkage debt.  Uniform existence remains open.

The word “packet” is essential.  The three intermediate (m=5) cycles are
Hamiltonian but are not decorated, so the three switches cannot be treated
as independent accepting recursion steps.  The recursive state must allow
temporary matching debt and discharge the complete augmenting linkage at
the macro boundary.  Moreover, bounded path count does not bound augmenting-
path length: for deeper shadows and compiler rows the affected support is
the actual representative symmetric difference, not merely the fifteen
carrier edges toggled by the three (C_{10})'s.

An independent long-switch replay strengthens the *final-state* side of this
base.  In its scoped frontier there are 585 palette-perfect Hamilton outputs,
452 with a perfect augmented matching, and one displayed three-`C10` witness
whose diamond lift is a 42-path forest closed by 42 colour-injective
connectors into one Hamilton cycle; cutting it gives an `h=1` right-comb
schedule.  This proves that palette repair, alternating SDR, leaf-peelability
and final physical closure can coexist at `m=5`.  It does not yet protect the
closure through the two-glue cube, supply nontrivial voltage, or preserve
strict residence, deeper shadows and the lower compiler.

A downstream replay of the *other*, synchronized repair witness sharpens
this separation further.  Its 42-path lift plus a colour-injective closure
covers the complete upper-union/lower-intersection flag tower through every depth at
`m=5`, and 46 cuts preserve that support.  Nevertheless every
whole-path opening fails residence: the fixed interiors contain 31 bounded
coordinate one-runs of length two, whereas `d=2` requires length at least
three.  Path permutation, reversal and endpoint socket choice cannot remove
them.  Thus at this first repaired base the remaining compiler obstruction
is not shadow coverage or final topology but an **interior rethread** which
changes the path bodies while preserving the accepted decoration and flag
tower.

That interior obstruction is now solved at the central `m=5` level.  A
second exact rank-4/rank-6 diamond matching, obtained by mixed alternating
`C4/C6` exchanges and replayed directly from its 210 matched pairs, lifts to
a spanning 42-path forest with both immediate palettes exact and no internal
positive run below length three.  It changes 119 matching partners, so it is
genuinely outside the intact-path face.  Its unjoined fragments still owe 21
deeper targets and a residence-compatible endpoint chronology; those rows
must now be solved jointly.

The accompanying all-`m` seam identity explains why this should be a
redistribution theorem rather than a capacity theorem.  Every coordinate
has exactly `Cat_m` runs in a Catalan linear matching, and each Johnson seam
merges exactly `m-1` runs.  A cyclic joining therefore has average run length
exactly `m`, compared with required length `d+1=Theta(sqrt(m))`.

The exact central recursive statement suggested by the two bases is the
following.

### Uniform repaired transparent macro lemma

For every `m >= 2`, one recursively supplied `ML(2m-1)` factor with
declared child collars admits:

1. a collar-disjoint ordered packet of bounded-port alternating circuits,
   whose cardinality may grow with the defect structure;
2. one selected occurrence decoration `D` at the packet endpoint; and
3. an ordered component-spanning list of incidence hexagons.

The packet endpoint must have exact lower and upper turn palettes and a
perfect augmented-trace matching selecting `D`, while retaining every
declared port.  Intermediate packet states may carry palette and matching
debt, but an explicit common-core augmenting linkage discharges it at the
macro boundary.  Every subsequent hexagon must preserve that same `D` by
the two local palette-multiset equalities and the retained-fragment boundary-
alternation test, preserve leaf-peelability by the contracted attachment-
forest test, and the ordered list must merge all components.  The final
trace retains a protected breaker and either a node-private tree-contiguous
socket schedule or the full occurrence-labelled socket relation.

Only the packet endpoint and subsequent transparent states are accepting.
Transparency is a relation between the current factor, one fixed joint
decoration and the remaining ordered gluing list—not a unary state property.
This lemma gives the central Catalan linear-forest state for every `m`, but
does not supply primitive voltage, strict residence, deeper shadows or the
lower compiler; RSB remains the theorem sufficient for the full formula.

### Corollary 4.1

RSB for every \(k\) implies

\[
                         \nu(k)=B(k)\qquad(k\ge1).
\]

#### Proof

Apply Theorem 1.1 to the certificate supplied by RSB, then combine the
resulting upper bound with the proved deadline lower bound.
\(\square\)

## 5. The shortest honest research frontier

The present proof tree therefore has two nested open statements.

* **Central statement:** prove the Catalan Linear Matching Theorem, most
  cleanly in direct ordered-four-transversal form.  The known uniform LP
  meets every matching, cap-two and graphic row, but explicit odd-resource
  cuts show that integral correlation is real.  Even the complete
  resource-conflict stable-set closure is insufficient at (m=2): the first
  missing inequalities must mix assignment completion with graphic
  acyclicity.  A positive direct proof therefore needs either such a mixed
  extended formulation or a symmetry-broken catalogue with a common
  middle-owner-dependent potential.  In the trace subclass, the weakest
  exact target is now the Decorated Middle Levels 2-Factor Theorem: one
  accepting componentwise decorated spanning factor in every dimension.
  Alternating-circuit decomposition removes repair realization as a
  separate gate, while the factor-to-diamond theorem removes Hamiltonicity
  and component merging.
  The prepared private/aligned machinery instead proves a stronger recursive
  route: a fixed joint SDR transported through a transparent leaf-peelable
  gluing tree.  Its owner and occurrence-router conditions remain exact for
  that route, but must no longer be advertised as necessary for central
  existence.  The newest minimal constructive interface is forest-first:
  find a spanning linear-forest support in a lower-tight/upper-tight edge
  catalogue and then apply ordinary Hall to its colour-occurrence graph.
  This succeeds on 28 `m=3` Hamilton-path supports even though every
  cycle-preserving hybrid fails, so future fusion arguments should optimize
  support plus Hall and deliberately ignore the unused edges.
  The strongest current inductive interface is the exact two-coordinate
  collar.  Inherited child endpoints settle the central middle bank;
  Kruskal--Katona plus matroid intersection settles the synchronized
  diagonal incidence bank for every child.  Its sole remaining row is to
  realize those bases as two anchor-capped side forests whose contracted
  seam graph is acyclic.  This is positive literally for child parameters
  `3,4`, and a stricter edgewise child-lift has now been chained through
  child `n=6`, producing one literal chain with ambient Catalan component
  counts `14,42,132,429`.  The new row required eleven genuine cycle cuts,
  so the graphic condition remains active.  A uniform *joint* edgewise-side realization theorem would
  therefore prove the central Catalan statement by induction without a
  decorated Hamilton-cycle theorem.  Arbitrary prescribed anchor pairing is
  impossible by the Johnson-distance budget and is no longer a target.
  One coupling previously attributed to this recursion is now removed:
  the isolated translated `c`-rail need not copy the structural child used
  for `Q`, the two side SDRs, the punctured `z`-rail and the seams.  Any
  Catalan forest at the same parameter supplies exactly the same translated
  lower/upper palette banks and is physically disjoint from the other three
  sectors.  Thus the collar is a two-parent construction: strict incidence
  and guarded filler chronology may be selected independently.  This does
  not supply the guarded filler, but it means copied-child residence debt is
  an artefact of the one-parent witness rather than an invariant of DERF.
  Conversely, the new child-`n=6` row refutes another tempting propagation
  invariant: its two side forests have `12` and `16` anchor-free
  components.  The exact charge law survives, but a rooted/no-empty shore
  does not propagate automatically and must be imposed or replaced by a
  controlled-empty routing state.
  The strict common-basis row nevertheless has a new exact candidate
  propagation invariant.  Weight endpoint-image middle vertices by `R/N`
  and unused path terminals by one.  Weighted Hall expansion of every
  outer family is equivalent to the uniform vector `C/N` lying in the
  strict dual base polytope; when it holds on both shores, matroid
  intersection gives common bases with exact uniform marginals.  One
  min-cut separates the condition.  Its exact scaled violations on the
  chained parents `n=3,4,5,6,7` are `(11,4),(14,0),(0,0),(0,0),(0,0)`.
  Thus common-basis DERF is now narrowed to preservation of one explicit
  balanced-expansion invariant after parameter five, not arbitrary
  two-matroid rank control.
  The orientation coordinate of that invariant is now exact.  For one
  strict occurrence graph, if `Z` chooses one terminal endpoint per child
  path, SBE is equivalent to

  ```text
  C |Z intersect A|
    >= N |{o : N(o) subseteq A}| - R |A|    for every A subseteq X.
  ```

  The right side is fully supermodular, and the opposite shore uses the
  complementary endpoint choice on every nontrivial path.  Hence balanced
  DERF orientation is one coupled binary supermodular-cover system with a
  polynomial fractional separation oracle.  It is not automatically
  block-integral.  Scaling `y=Cz` produces the natural
  supermodular-lower/submodular-upper split-capacity system and partition
  equations `y_u+y_v=C`; ordinary integral submodular flow allows every
  integer `0<=y_x<=C`, while coherent path orientation needs
  `y_x in {0,C}`.  At `n=3`, `C=14` and the integer split `y_x=7` passes both
  raw shores although no coherent orientation exists.  Normalizing before
  rounding restores the block choice only by introducing `ceil(g/C)`, whose
  crossing-supermodularity failure is authenticated.  The remaining
  preservation step is therefore a **block-submodular donor theorem** or an
  explicit recursive block choice, not ordinary integral submodular flow
  and not another search over arbitrary path directions.
* **Full statement:** prove RSB.  Inside the trace strategy, its next exact
  central subproblem may be attacked directly at the decorated-2-factor
  level, through a decorated Hamilton theorem, or recursively by the
  stronger uniform repaired transparent macro lemma above.  None supplies
  the downstream word rows.  The
  finite `m=5` rethread proves strict internal residence can coexist with the
  exact palettes, but endpoint joining and its 21 deep targets remain
  coupled.  The minimum-three residence row itself is no longer global: on
  any selected physical forest it is exactly the cubic clause forbidding a
  three-edge window whose first insertion equals its third deletion.  This
  clause system includes every block interior and seam and streams with only
  the previous two directed edges.  Therefore the remaining residence
  theorem is simultaneous feasibility of a finite local automaton with the
  strict matching/graphic rows and an output-depth-safe independent filler,
  not discovery of another run invariant.  Uniform run redistribution,
  primitive voltage and the lower compiler must still be preserved.
  The filler quantifier is itself jump-localized.  A finite symmetry bank
  under sealed filler copying cannot meet unbounded guards, because one seed
  chronology survives as an isolated induced ancestry.  But the deadline
  guard `d(2n)+1` is nondecreasing and jumps only `O(sqrt n)` times through
  parameter `n`; between jumps the current accepted forest is already a
  valid filler.  Hence the exact new subtarget is same-parameter guarded
  promotion only at deadline jumps.  At `n=5`, substituting a clean
  independent filler deletes all 44 copied-rail bad windows while preserving
  the exact 132-path support, experimentally separating this promotion row
  from the remaining 100 structural/seam clauses.
  There is now a stronger exact filler face which removes the guard schedule
  altogether.  An antipodal-geodesic Catalan forest has every component of
  length `n`, complementary endpoints, and one flip of every coordinate;
  it is therefore safe at every residence width.  Such forests now exist by
  independently replayed certificates at `n=3,4`.  After adjoining a
  distinguished point, they are exactly pointed exact wreath factors whose
  interior consecutive lower turns are rainbow.  More importantly, the
  `n=3 -> 4` certificate lies on a genuine recursive face: every parent path
  is extended whole by one `c <-> z` swap, while the remaining vertices form
  nine forced-monotone `00 -> 01 -> 11` geodesics.  In general the residual
  has three equal middle banks of order `N`, lower-resource orders
  `(N,N,P)`, upper-resource orders `(P,N,N)`, and exactly
  `H=N-P=3N/(n+2)` paths.  Perfect resource matching in this explicit
  three-sector residual is now the clean all-parameter filler theorem.  It
  is proved for the first recursive step, not yet in general; see
  `MATH_THEOREM_CATALAN_ANTIPODAL_FILLER_POINTED_WREATH_AND_THREE_SECTOR_RECURSION_20260731.md`.
* **Additive-constant statement:** prove bounded-defect sidecar RSB.  It is
  enough to regenerate a uniformly bounded auxiliary state and compile each
  odd/even terminal word with uniformly bounded repair charge; terminal
  repairs do not accumulate along the spine.  The ordinary closed top-bit
  splice cannot supply this because its even excess is `Theta(sqrt(k))`
  even from exact odd parents.  A cap/facet child recompilation or another
  reset transition is essential.
  The repair subtheorem must be stated for closed compound packets and
  literal-weighted leave.  Constant packet-count leave is insufficient when
  one unresolved residence packet represents `Theta(sqrt(k))` missing
  literal masks, and no fixed packet-radius descent theorem is possible.
  On the central row, a passive binary GMM recursion with at most eight
  changed turns per splice is now ruled out quantitatively.  The first live
  recursive target is a stateful nine-plus-entry palette reset coupled to
  physical linearization, residence, deep providers and the common guard;
  the `m=5` three-switch repair is the finite base, not yet the induction.

Thus it would be inaccurate to call “joint alternating SDR plus transparent
gluing tree” the sole missing theorem for \(\nu(k)=B(k)\).  It is a strong
recursive certificate for the central gate; a decorated Hamilton cycle is
weaker, and a componentwise decorated 2-factor is weaker again and already
sufficient.  Beyond any central solution, residence, deep shadows and the
lower compiler still have to be coupled in one chronology.  RSB remains the
shortest exact single theorem whose proof would finish the formula.
