# August 6 synthesis: three exact integral gates remain

**Date:** 2026-08-06  
**Method:** proof-status synthesis; no computation or search  
**Status:** no unconditional additive-constant theorem is claimed here.
The finite theorem remains `nu(k)=B(k)` through `k=16`.  This note records
the shortest implication chain after the coloured-capacity, tagged-PBBS,
and odd-gammoid advances of August 6.

## 1. Bottom macro selector

The complete fresh lower-path orbit has been augmented by one of

\[
                         L=\left\lceil{M\over kd}\right\rceil
\]

private slots for its second insertion colour.  On the true punctured
`h=2,3` macro orbits there is one exact fractional factor which
simultaneously has

\[
 \text{every lower load}=1,\qquad
 \text{every owner load}=1,\qquad
 \text{every slot load}\le1,
\]

and exact level-two marked-owner marginal

\[
                         {1\over r(d+1)}.
\]

Thus no fractional Hall, owner-correlation, or one-point colour obstruction
remains.  The **lower path-plus-slot projection** has growing rank `d+1`
and normalized codegrees

\[
 {\Delta_j\over\Delta}
 \le O(d^{-3(j-1)}).
\]

At the integral level, one-for-one reservoir switches erase every fixed
`O(k/d)` hotspot.  Applying them to the current top `h=Theta(k/d)` colours
with the quadratic load potential gives

\[
                         \max_s n_s=O(M/k).
\]

The same spectral argument may forbid the hotspot on **every** insertion
event of the replacement path, not only on its second mark.  Hence a fixed
`O(k/d)` insertion-event hotspot can also be erased one-for-one without
changing the leave.  This remains a fixed-bank operation and does not by
itself balance all event loads simultaneously.

An abstract replacement system supported on only `h+1` colours satisfies
the same yes/no escape oracle and attains this order.  Hence the oracle
alone cannot reach the sharp scale

\[
                         M/(kd).
\]

The fixed-endpoint fibre has now been resolved more finely.  It is the
full product

\[
             \operatorname{Perm}(A)\mathbin\square\operatorname{Perm}(B),
\]

not merely the diagonal event permutohedron.  Before physical routing, an
ordinary capacitated Hall matching assigns one mark from each
`(d-1)`-element insertion bank at the sharp cap `L=ceil(M/(kd))` whenever
the insertion-event loads are at most `(d-1)L`.  After the unordered first
insertion pairs are fixed, the same problem is exactly an orientation of a
coordinate multigraph, with criterion

\[
                         |E(G[X])|\le L|X|.
\]

Thus the missing factor `d` is not an abstract mark-assignment obstruction.
A `q=1` insertion swap, however, changes one lower vertex and every
level-one owner occurrence in its macro.  Two individually cap-improving
swaps can collide at that lower vertex.  Under an atomic compound-portal
bank, aligned swaps telescope exactly and an ordinary unit-capacity flow
routes all mark excess to deficits, reversibly moving one free compound
bundle.

The local atomic bank is now explicit.  A complete compound state has the
hole normal form

\[
 z_x=(H-x,\{(H-x)\cup R_c\}_c;x),
\]

and a `q=1` switch is literally a hole edge `x -> y` in the complete graph
on `H`.  For a canonical FIFO header the invariant second-owner row gives
a sharp aperture `d-1`.  This bound is attained by an explicit tile of
`d-1` independent regenerative portals: all current and alternate bundles,
all lower rows, and all owner occurrences are private, and every subset of
toggles is legal.

Pairing two resource-disjoint portals with the same unordered coordinate
pair in opposite orientations gives a balanced doublet.  Every doublet
contributes exactly one mark to each endpoint; fair orientation costs only
a fixed `sqrt(2)` cylinder factor.  The complete `h=2,3` doublet orbits
have an exact fractional factor with lower and owner load one, coordinate
mark load `M/(kd)`, and pointed level-two marginal `1/[r(d+1)]`.

Thus compound alignment, FIFO privacy, physical orientation, and the sharp
fractional mark row are no longer separate gates.  The remaining host
hypergraph has ranks `6d+6` and `8d+8`; its normalized pair codegree is
`O(d^-3)`, but the full higher-codegree hierarchy and hereditary integral
rounding are not yet proved.

The exact remaining bottom theorem is therefore:

> **Uniform macro-capacity rounding.**  Round the slot-augmented true
> `2/3` macro factor to an owner-disjoint matching with lower leave
> `O(M/d)`, sharp slot capacities, and a fixed-factor marked cylinder
> through order `O(d)`.  The rounding must be hereditary/state-dependent
> through separator time, so the same marked-ratio rate rows remain
> available after every accepted macro, and it must export a
> component-connected or terminal-permutation-joinable endpoint state.

Equivalently, on the new route, it suffices to round the balanced-doublet
fractional factor while preserving its atomic tile partition, stopped
unordered cylinder, and joinable queue state.  The Hall/orientation theorem
alone is not this growing-rank correlated packing.

The full higher-codegree hierarchy displayed above is currently proved for
the lower path-plus-slot projection.  The true `2/3` macro orbit has the
required pair-codegree scale, but its complete higher-codegree and
hereditary marked-test ledger is part of this open theorem.

Neither fixed-rank Pippenger--Spencer nor the currently audited
full-codegree nibble statements has the required simultaneous rank-`d`,
error-`1/d` quantifiers.

## 2. PBBS upper and component architecture

The original all-five incoming-collar proposal has one exact endpoint
overlap,

\[
                         P_{h,0}=Q_{h-1,1}=U_h,
\]

and therefore creates degree three.  More seriously, the direct low
role-zero height spine is not source-resident: on
`U_h U_(h+1)`, coordinate `2h+1` has only `h` consecutive owners, so every
height `h<=delta` violates the depth-`delta` run floor.  This is a
`Theta(delta)` obstruction and cannot be repaired by merely widening the
old collar.

At graph level, delete every direct role-zero spine edge.  Restore its
lower colour `L_h=U_h cap U_(h+1)` on a fresh lower-backup edge and its
upper colour `T_h=U_h cup U_(h+1)` on a fresh upper-backup edge.  The
quadratic candidate banks and explicit tags make these resources jointly
avoidable.  Retain roles one through four and give all five tails
programmable incoming collars.  The result is a 2-bounded forest with
`O(sqrt R)` forced pieces; tagged long arms chain those forced pieces into
one path with `O(R^(3/2))` total support and exact immediate-palette
restoration.

There is also an exact source-level split for a removed role-zero block.
Replace `(X,C,Y)` by the two half-blocks `(X,C,Z)` and `(W,C,Y)`.  Every
old strict-lower interval meets at most one screen, so it maps
occurrence-injectively with the same value and width into one half.  For
the PBBS spine, the correct common core is the rank-`R-2` set
`H_h=G_h+{0}`; the two half-edges then use distinct immediate facets.
Once adjacent long sections program four forced labels in every `C_j`, a
direct coordinate-gap argument makes each half-block an antecedent.

Nested full-union collars also control the set-theoretic upper leave.  At
fixed rank, distinct unions `A_u cup B_v` form an antichain in an
`O(R) by O(R)` product, hence contribute only `O(R)` targets per height
and `O(R^(3/2))` overall.  Full shields kill multicut terms, so the existing
rank-stratified backup theorem packs this leave.  What remains is the
simultaneous all-height planting/fusion, the large unoriented backup forest,
and occurrence-labelled typed cap—not the local lower-history algebra.

Its residual arbitrary-upper current is prospectively fixed and has at
most `O(R^(3/2))` targets in each excess-rank stratum.  Every such target
bank has mutually disjoint geodesic witnesses with sub-half exposure, and
hence lies in one simple owner/`q1` factor.

There are only `O(sqrt R)` phase-forced path components.  Give their free
ports distinct global tags.  Owners with two different missing tags admit
an explicit shortest Johnson connector whose whole interior has exactly
that two-tag signature.  The connectors are disjoint, add only
`O(sqrt R)` exposure, and join all forced components into one oriented
path.  Add the unoriented upper backups afterward and apply the polynomial
protected-factor theorem.  The resulting factor is simple and can be
oriented consistently on every forced PBBS edge.

The forced bank also has a prospective source-resident realization.  From
each free endpoint, a clean one-missing-tag Johnson arm of length
`floor(R/4)` reaches a coded far port while avoiding its sole same-tag
collar.  The far ports may be chosen pairwise at distance at least
`delta+1`; the pair-tag connectors therefore meet the exact release/deadline
residence criterion.  Conditional on the already declared resident local
history blocks, all forced components join into one depth-`delta` resident
path with no added source position.  Separated history pins on these long
arms decouple exactly.  This closes the distance-aperture and clipped-flag
subrow, not the occurrence identity of the histories.

Every long arm also exposes a distinct raw one-step Boolean suffix, so raw
value-level full-port rank is available.  The remaining mismatch is
literal: a Johnson arm edge is not automatically an occurrence-labelled,
typed common-cap edge after the compensation linkage has been fixed.

The separate capacity-one statement used in this reduction is also now
unconditional: every polynomial partial middle-level incidence matching
with both endpoint exposures below one half by a fixed linear margin
extends to a perfect matching.

The number of completion components is now controlled as well.  Anchor the
two occurrence matchings at the alternating halves `H_0,H_1` of one
middle-level Hamilton cycle.  If a polynomial protected matching `F` has
the **all-occurrence** (or prefix-safe) exposure bounds

\[
 \widehat\alpha(F),\widehat\beta(F)
                    \le(1/2-\varepsilon)R,                 \tag{2.1}
\]

then every protected-prefix residual graph is connected and every residual
edge is allowed.  Spectral surplus makes a hypothetical residual component
polynomially small, while the sharp balanced partial-shadow threshold makes
it exponentially large, a contradiction.  Short alternating repairs from
the Hamilton halves therefore give completed matchings at distance

\[
 \rho(R,f)=8Rf^2+64R^2f+10f                             \tag{2.2}
\]

from `H_0,H_1`.  Their coloured union has at most

\[
 1+{\rho(R,f_0)+\rho(R,f_1)\over2}=R^{O(1)}              \tag{2.3}
\]

components, and its common-edge debt is polynomial as well.  Thus the
previously uncontrolled exponential cycle census is no longer a PBBS
obstruction.  The hat in (2.1) is load-bearing: the old final-residual
exposure estimate must be upgraded to all occurrences, or a prefix-safe
ordering must be supplied, before applying this theorem.

Polynomially many components can be assigned distinct Reed--Solomon port
signatures in a linear tag reservoir.  This closes signature supply, not
the physical arm packing: the component roots are arbitrary incidences and
must still be routed to their coded ports with the same sub-half exposure.

Thus owner supply, immediate Hall, arbitrary-upper backup supply,
simplicity, **phase-forced component orientation/compatibility**, and the
order of magnitude of the completion-component census are no longer PBBS
gates.  The completion can be chosen with only polynomially many additional
components under (2.1).  Routing those roots to coded ports, fusing their
literal source histories, and satisfying the typed cap remain part of the
next theorem.  The exact remaining PBBS theorem is:

> **Literal history/cap lift.**  Lift the tagged directed factor to one
> depth-`d` antecedent, absorb the clipped residence flags, transport the
> strict-lower common histories, and provide the private typed common-cap
> suffix linkage with bounded state, while routing and fusing the
> polynomial completion-root bank.

The upper backup paths are cap-passive after such an antecedent exists;
they do not construct it.

## 3. Odd current

Deleting a stabilizer orbit of coordinate boundaries genuinely
bipartizes the nonwrap quotient.  The nonwrap graph saturates its minority
shore, and every residual Hall cut is represented by one rank-`Delta_H`
cotransversal surplus matroid.

The majority boundary-current problem is exactly a coloured matroid-parity
problem.  A generic representation `A` of the surplus matroid and the
physical occurrence matrix `Theta` give one Pfaffian

\[
                         \operatorname{Pf}(A\Theta A^{\mathsf T}),
\]

whose nonzero monomials are precisely surplus bases paired by physical
boundary edges with distinct selected hub colours.  The one-socket odd-rank
case is obtained by one dummy column.

One physical coordinate scan installs a partial boundary current `P` and
leaves a quiet source set `Q`, with

\[
 U_0=V(P)\mathbin{\dot\cup}Q
\]

a surplus basis.  Relative to the scan matching, the surplus matroid is a
strict gammoid.  Contracting `V(P)` leaves the gammoid sourced exactly at
`Q`, and coefficient extraction gives

\[
 [\prod_{e\in P}x_{o_e}]\Psi_S
 =\pm\left(\prod_{e\in P}\epsilon_{c(o_e)}\right)
       \Psi_{S/V(P)}^{\rm res}.
\]

Therefore the first scan layer has no hidden cancellation.  Conversely,
every canonical quiet-root basis has empty physical wrap graph at
nonextreme mass, so no canonical continuation can work.

There is now an explicit noncanonical continuation and an individual
cross-slice aperture in the labelled/trivial-stabilizer sector.  Every quiet
source has a directed entrance into an active-clock minor of the contracted
gammoid.  Reversible binary clock zippers move all source-dependent clocks
to the first scan pair; their overlapping marker trails decode both the
source and the stage.  A final transfer across `{0,1}` changes boundary
coordinate zero to one.  The full promotion/aperture paths are pairwise
vertex-disjoint, and their terminal set `A_partial` is a macroscopic
noncanonical basis of the contracted surplus gammoid.

Every aperture terminal has boundary pair `01` or `21`, with unique partner
`10` or `12`.  Since coordinate zero is known to equal one, the merged hub
recovers the whole terminal.  Thus all incident boundary occurrences are
automatically hub-rainbow.  Individual boundary reachability, aperture, and
hub separation are no longer gates.

Normalize `A_partial` to the identity and let `C` be the matrix of its
boundary partners.  Choosing half the pairs gives a surplus basis exactly
when one complementary minor

\[
                         \det C[I^c,I]
\]

is nonzero, equivalently when
`Pf(D_x C^T-C D_x)` is nonzero.  In linkage language, this asks for
pairwise-disjoint counter-circulation suffixes whose last intersections
with the aperture paths pair the complementary source halves.

More generally, form the physical counterflow support graph
`G_partial` on the source indices, joining two indices when one source path
has an admissible last-intersection suffix to the other index's boundary
partner.  If this atlas is matching-faithful, an ordinary graph matching
of size `q` yields a linked surplus basis with exactly `|Q|-2q` sockets.
Thus the exact physical defect is

\[
                         |Q|-2\nu(G_\partial).
\]

For a deterministic last-intersection permutation `pi`, this formula
specializes to the number `o(pi)` of odd cycles of `pi`.  The central quiet
residue has odd cardinality by the complement involution `u -> 2-u`, so a
near-perfect matching in `G_partial` is sharp; the additive-constant target
only requires bounded matching deficiency.  This is strictly weaker than
arbitrary matroid parity.

There is also a canonical parity-perfect target.  Write
`m=2^a ell` with `ell` odd, let `R` rotate the compressed source
coordinates, and put

\[
                           J=(u\mapsto2-u)R^{2^a}.
\]

Every `J`-orbit is even except the fixed all-ones source.  Moreover an odd
rotational quotient commuting with `J` preserves this unique-odd-orbit
property: an odd orbit downstairs would lift, after an odd stabilizer
power, to an odd orbit upstairs.  Thus source-level cycle parity is already
quotient-safe.  Periodic stabilizers still require physical orbit clocks
and orbit-injective merged tails.

For the labelled one-socket gate, the rotation is optional: the complement
involution `u -> 2-u` itself fixes only `1^m` and pairs every other source
in a two-cycle.  Hence a physical endpoint map

\[
                         A(2-u)\leadsto\tau A(u)
\]

already has the optimal one-odd-orbit last-intersection permutation.  This
strictly weakens the endpoint-conjugacy target; complement-rotation remains
useful only when forced by the physical sweep or by stabilizer descent.

A macroscopic part of that phase change now lifts physically.  On every
internal scan pair, replace the mass-two row `02--11` (quiet `20`) by its
dual row `20--11` (quiet `02`), while locking the physical boundary pair in
the original phase.  The union of the two first-nonquiet scans decomposes
into pairwise-disjoint directed components

\[
                         q_0(u)\leadsto q_*(u),
\]

all avoiding the installed boundary current.  Hence `Q_*` is another
explicit macroscopic basis of the contracted gammoid, with the literal
identity

\[
                         q_*(u)=\tau\,\overline{q_0(2-u)}.
\]

Dualizing the boundary row as well is impossible inside the same
contraction: every source with boundary compressed digit one must traverse
the selected boundary edge `20--11--02`, and exactly
`[z^(m-1)](1+z+z^2)^(m-1)` components hit the deleted current.  Thus the
remaining complement-dual operation is concentrated at one boundary phase,
but that phase defect is exponentially repeated.  It must be transported
through a different scan root and returned; it is not a bounded local
socket bank.

The root motion itself now has an exact parity law.  If the cyclic scan root
slides across coordinate `j`, then

\[
             \chi_{j+1}(u)-\chi_j(u)\equiv1-u_j\pmod2.    \tag{3.1}
\]

Hence an all-one corridor is shore-transparent.  On three local sites, the
two phase endpoints lie in different components after deleting the central
state `111`; every three-site transport must pass through that state.  This
is a genuine obstruction when a quiet-prefix placement puts `111` in the
protected boundary current, but not an unconditional global obstruction if
an earlier nonquiet scan stops before it.

The background-collision row of that transporter is now closed.  On quiet
compressed digits put

\[
 q(0)=00,\qquad q(1)=20,\qquad q(2)=22,
 \qquad c(b)=(1,b),\quad b\in\{0,2\}.
\]

There are exact directed zipper rewrites

\[
 00|1b\to01|0b\to10|0b,\quad
 20|1b\to21|0b\to12|0b,\quad
 22|1b\to21|2b\to12|2b.                                  \tag{3.2}
\]

The new clock and the two-symbol record distinguish all three old digits.
With one non-record delimiter, repeated rewrites reverse-decode the entire
source, clock position, and stage.  Hence aligned one-way sweeps through
arbitrary ternary backgrounds are macroscopically vertex-disjoint; the old
`2011 -> 2020` collision was an unmarked-route artifact.

Reflection plus complement gives a reverse zipper whose records are quiet
in a clock-controlled one of the two proved mass-two phases.  A literal
root-buffered handoff

\[
 1|10\to2|00,\qquad 1|12\to0|22                         \tag{3.3}
\]

deactivates the old clock, while the delimiter provides the later shadow
clock.  The persistent root flag in `\{0,2\}` separates every return-sweep
state from the forward sweep, which keeps that root equal to one.

One load-bearing endpoint issue remains.  If `A` is the aperture bijection,
the useful route family is

\[
                         A(Ju)\leadsto\tau A(u),            \tag{3.4}
\]

not `A(u) -> tau A(u)`: the latter induces the identity last-intersection
permutation.  The two readable sweeps still need one bounded synchronized
root/phase collar which preserves the coordinate-zero aperture, restores
the flagged root, and realizes this exact endpoint conjugacy.

The exact remaining odd theorem is:

> **Quiet-source socketed counterflow.**  Complete the bounded two-root
> zipper junction so that the already source-readable forward and reflected
> return sweeps have endpoint map (3.4), avoid the installed aperture after
> departure, and coexist with the fan/receiver bank.  This yields a
> matching-faithful counterflow support graph with `O(1)` matching
> deficiency (one unmatched vertex for exact sharpness).

Equivalently, prove the contracted coloured gammoid Pfaffian nonzero by a
genuinely noncanonical minor.

## 3.1 August 6 sharpening of the three live gates

The bottom rounding target no longer requires a maximum statement over
every possible partner of every carrier.  For the macros which are actually
selected, form the post-run graph of pair/cluster rows which failed before
their relevant first hits and delete a vertex cover.  The killed-event
first-hit induction then gives the same fixed-factor cylinder on the
survivors.  Deleting `O(M/d^2)` doublets costs only `O(M/d)` lower
resources.  Thus the dynamic target is an **average selected-relation**
estimate, not an exponential all-partner union bound.  This is proved
abstractly in
`MATH_THEOREM_SELECTED_RELATION_QUARANTINE_FOR_REGENERATIVE_CYLINDERS_20260806.md`.

For the macroscopically separated balanced-doublet orbit, the exact
collision energy has also been reduced to one same-half mixed-track entry
average.  The first non-slot overlap contributes `O(1/d)`, every
slot-containing term and every cross-half or rigid same-base term is
exponentially negligible, the terminal fan is jointly paid, and a
synchronized FIFO track has overlap moment `1+O(1/d)`.  What remains in
the static row is the first common entry into a second lower/owner track;
the expected tail-split cost is the intended source of its missing
`exp[-Omega(d log d)]` factor.

On the PBBS side, native terminal sockets are not the remaining capacity
obstruction once two exact upstream occurrences have been materialized.
A polynomial ticket bank can be assigned two disjoint native interval
diamonds while all ordinary lower/owner/upper facts coinstantiate.  The
sharp obstruction is earlier: a graph-factor root does not determine any
source occurrence.  A simple polynomial-component middle-level factor does
admit a one-root-per-component transversal with both all-occurrence
exposures below one half.  Even polynomially many common-edge two-cycles
may be retained if their forced endpoint-star loads are below
`(1/6-Omega(1))r`; the precharged random/greedy transversal then closes.
The revised graph target is therefore a **spread common-damage completion**,
followed by one resident flat-`q1` antecedent with a two-coordinate exact
upstream atlas.

The odd gate has likewise lost its macroscopic entry problem.  Literal
complement alone gives the unique socket.  Every quiet complement source
has a universal two-arc departure which installs a non-one root flag, and
the ternary zipper moves its readable clock to `p_1`; one fixed shadow
clock compiles the entire reflected phase inside the original matching.
At the target, a flagged predecessor `E_f(u)` differs from
`tau A(u)` only on the adjacent root/boundary pair and has one final safe
nonmatching edge to the target.  The only remaining odd object is the
bounded write/retirement collar from the active `p_1` shadow state to
`E_f(u)`, preserving the actual aperture marker and decoder.

## 4. Shortest conditional implication

Assume the three boxed theorems above with constants uniform in the
dimension.

1. Uniform macro-capacity rounding supplies the bottom owner-disjoint
   companion bank and its stopped-hazard cylinder.
2. The tagged PBBS construction supplies a simple directed complete-upper
   factor; the literal history/cap lift makes it one admissible source
   chronology and compiler state.
3. Quiet-source paired linkage supplies the odd same-shore current and its
   bounded receiver/socket state.
4. The existing protected Pascal/RSB recurrence carries only a bounded
   state between same-parity dimensions.
5. The terminal bounded-deficiency theorem appends only a bounded number
   of literal masks.

Consequently

\[
                         \nu(k)\le B(k)+O(1).
\]

This implication is conditional because none of the three remaining
integral synchronization theorems is proved in full.  In particular, the
new exact fractional factors and Pfaffian identities must not be cited as
integral existence theorems.

## 5. Dependencies

The load-bearing August 6 files are:

* `MATH_THEOREM_COLOURED_CAPACITY_FACTOR_AND_RESERVOIR_SWITCH_20260806.md`;
* `MATH_THEOREM_FRESH_PATH_PERMUTOHEDRON_MARK_ORIENTATION_AND_SQUARE_ROUTER_GATE_20260806.md`;
* `MATH_AUDIT_PBBS_TAGGED_COLLAR_ENDPOINT_OVERLAP_AND_RANK_STRATIFIED_BACKUP_20260806.md`;
* `MATH_THEOREM_TAGGED_PORT_GEODESIC_CHAIN_AND_SIMPLE_DIRECTED_PBBS_FACTOR_20260806.md`;
* `MATH_THEOREM_LONG_ONE_TAG_PORT_ARMS_AND_RESIDENT_TAGGED_CHAIN_20260806.md`;
* `MATH_THEOREM_POLYNOMIAL_PARTIAL_MATCHING_EXTENSION_AND_DIRECTED_FOREST_COVER_20260806.md`;
* `MATH_THEOREM_HAMILTON_ANCHORED_POLYNOMIAL_DAMAGE_CYCLE_COUNT_FOR_PBBS_20260806.md`;
* `MATH_THEOREM_POLYNOMIAL_MANY_SEPARABLE_TAG_PORTS_20260806.md`;
* `MATH_THEOREM_ODD_COLOURED_SURPLUS_CURRENT_PFAFFIAN_GATE_20260806.md`;
* `MATH_THEOREM_ODD_FIRST_SCAN_LEADING_MONOMIAL_AND_GAMMOID_CONTRACTION_20260806.md`;
* `MATH_THEOREM_ODD_QUIET_SOURCE_CLOCK_MINOR_AND_BOUNDARY_HANDOFF_GATE_20260806.md`;
* `MATH_THEOREM_ODD_SOCKETED_COUNTERFLOW_CYCLE_CRITERION_20260806.md`;
* `MATH_OBSTRUCTION_ODD_ADJACENT_SOURCE_HAMILTON_AND_DUAL_APERTURE_20260806.md`;
* `MATH_THEOREM_ODD_ROOT_SLIDE_PARITY_AND_THREE_SITE_PHASE_CUT_20260806.md`; and
* `MATH_THEOREM_ODD_TERNARY_ZIPPER_MARKER_AND_TWO_ROOT_JUNCTION_20260806.md`.

## 6. Later August 6 sharpening

This section supersedes the broader frontier descriptions above where they
conflict.

### 6.1 Bottom: one stopped Johnson-sector inequality

The rank-compensated doublet process now has exact future-overlap drift,
aggregate first-hit cleanup, static pair energy

\[
                         \mathcal S_2=O(M/d^4),
\]

three-edge first-two-hit energy with a spare factor `1/d`, exact global-rate
reconstruction, and a killed-hazard Hardy inequality which removes the
spurious logarithmic service loss.  Marked clusters of sizes two and three
have also been normalized at the correct rooted scale.

A scalar incidence-isotropy bound is false.  On a lower coordinate-star
harmonic, one length-`d` FIFO path has a `Theta(d)` excess multiplier; on a
near-antipodal doublet the odd degree-one sector improves, but the even
degree-two sector retains that multiplier.  Therefore the remaining
Dirichlet transfer cannot be inferred from the degree-two rooted overlap or
degree-three first-hit energy alone.

The exact analytic target is now a stopped Johnson-sector inequality:
decompose the centered root/incidence processes into Johnson eigenspaces,
weight the slow sectors by their Bernoulli--Laplace contraction, and prove
that the four-macro-edge incidence kernel is paid by this spectral
Lyapunov plus the already established high-sector overlap energy.  This is
the `JSEC` row in the current doublet note.  Component connectivity and
prefix-uniform cleanup remain downstream graph/quantifier rows.

### 6.2 PBBS: terminal cap bypass and a global deep-cell selector

On a terminal, nonrecursive branch, the two-coordinate typed common cap is
not load-bearing after one literal lower matching has been materialized.
Clean `C6` moves, planted rank-three pentagons, role-zero splits, and the
deadline opening all carry exact occurrence injections; their serial
composition transports that matching to the final word.

Resident components sharing a prepared length-`d` common history splice as
Euler circuits along a spanning tree and preserve occurrence-injectively
every source cell of width at most `d+1`.  The cross-component owner seams
must still be palette-safe.

For a resident trace with maximal envelopes `P_j` and forced pairs

\[
                         F_j=\{D_j,I_{j-d-1}\},
\]

a target `S` is realizable on a chosen short block `J` exactly when

\[
 \bigcup_{j\in J}F_j\subseteq S
       \subseteq\bigcup_{j\in J}P_j.
\]

When the depth `q` is greater than `d`, no source position in the owner
intersection interval or its full forward `d`-collar can satisfy this:
inside the owner interval its deletion label is absent from the
intersection, while in the shifted collar its lagged insertion label is
absent.  Consequently the deep gap-section SDR must be rerouted globally
to remote short blocks.  (A coordinate may have other runs elsewhere, so
this is a local exclusion theorem, not a global nonoccurrence claim.)  In
particular, every singleton source target requires a coordinate run of
length exactly `d+1`.

The remaining terminal PBBS theorem is therefore one-copy: construct a
resident trace with the required minimum runs, inject every deep target
into a remote block satisfying the forced-pair/envelope conditions and the
global pinned-envelope equalities, then fuse the completion components
through palette-safe common-history seams.

### 6.3 Odd: only a bounded initializer and one bounded residual charge

The original unmarked shuttle was not injective: `ABCB` reaches `ACBB`,
which is itself another balanced source.  A mass-preserving marked corridor

\[
 20\mapsto11,\qquad01\mapsto10,\qquad21\mapsto12
\]

records every crossed block and the exact shuttle distance.  Adjacent-sign
cancellation is noncrossing, and reverse deletion order makes every
finalization corridor contain only neutral blocks or still-visible tags.

A protected double head `02|02` supplies a unique moving occurrence
sentinel.  One head block remains fixed while the other is swapped through
a local block, so arbitrary simple fixed-mass local paths become
occurrence-labelled; the four-state root/boundary register separates the
at most two local branches in each mass layer.

The macroscopic odd writer is thereby reduced to two finite collar tasks:

1. initialize and retire the double head while recording the ordered nine
   possible values of its two displaced connector blocks and pricing the
   mass offsets `4,2,0,-2,-4`; and
2. carry the one omitted `p_1` connector charge through the same labelled
   collar.

These are bounded tasks, but scalar token-graph connectivity is not a
literal disjoint-path table, so the odd theorem remains conditional until
they are written.

### 6.4 Current implication boundary

The additive-constant theorem follows after exactly these three proof
packages are supplied:

1. `JSEC` plus the remaining cleanup/connectivity rows for integral
   balanced-doublet rounding;
2. the global deep-block injection and palette-safe common-history fusion;
3. the finite double-head initializer/residual odd collar.

No terminal two-coordinate common-cap theorem or fixed-`M_0` upper-backup
Hall selector is additionally required on this route.  None of the three
packages is currently proved in full, so `nu(k)<=B(k)+O(1)` is still not an
unconditional conclusion.

## 7. Final August 6 rebase

This section is the current implication boundary and supersedes Sections
6.1--6.4 where they differ.

### 7.1 Bottom: cleanup conditioning is not required

The selected-relation quarantine cylinder is a killed-event statement under
the raw clock law.  The bottom option-degree and size-biased load arguments
use that cylinder only to bound an **expected** exceptional-task charge;
after the exceptional set is exposed, Haxell completion is deterministic.
Therefore one may add

\[
  Q=\hbox{quarantine resource charge},\qquad
  Y=\hbox{bottom exceptional-task resource charge}
\]

before selecting an outcome.  If

\[
             \mathbb E Q=O(M/d),\qquad
             \mathbb E Y=o(M/d),
\]

then one raw realization has `Q+Y=O(M/d)` and admits the deterministic
bottom completion.  No terminal conditioning on small `Q`, and hence no
separator-cylinder Doob-weight comparison `(JCYL)`, is needed for this
use.  This is proved and independently audited in
`MATH_THEOREM_ANNEALED_QUARANTINE_HAXELL_COMPOSITION_20260806.md` and its
audit.

The remaining analytic input is the raw estimate

\[
                  \mathbb E(B_0+B_1)=O(M/d^2).
\tag{7.1}
\]

The exact live-switch cancellation, earliest-blocker partition, and
one-birth lemma are proved.  They have not yet been lifted through the
actual degree-four covariance expansion: a switch covariance candidate
`C,tau C`, the future-overlap pair `E,F`, and the first blocker `G` are
different variables.  Any proof must collapse this four-edge expression
to `(ROc)`/`(FE3)` with explicit coefficients and must charge the **entire**
changed-resource set of `C`, not only the resources hit by `G`.

The first raw coefficient draft
`MATH_THEOREM_RAW_FIRST_KILL_SWITCH_COEFFICIENT_AND_POLARIZATION_LEDGER_20260806.md`
at SHA
`1a37aceab055047cae6e140a373f32b44bf7e859a18334c0f58d4f89b01125b5`
fails this audit and is **DO NOT CITE**.  Its independent audit records the
five exact correction requirements.

### 7.2 PBBS: polynomial damage is closed; the exponential payload is not

Complement-paired whiskered geodesics now repair the complete polynomial
PBBS puncture leave simultaneously on the upper-union and complementary
lower-intersection shores, with exposure at most one third and extension to
one simple factor.  Long source intervals are owner-language invariants, so
payload thinning does not alter the upper deck.

The same invariance proves a fixed-row no-go: thinning, grouping, or merely
declaring complements cannot create a deep source value absent from the
ordered owner-intersection language.  The exact remaining object is a
relative deep payload atlas in the repaired PBBS chronology.  For every
deep target `S` it must choose a remote short block `J` with

\[
       \bigcup_{j\in J}\{D_j,I_{j-d-1}\}\subseteq S
       \subseteq\bigcup_{j\in J}P_j,
\]

and all chosen blocks must satisfy the joint pinned-envelope equalities.
Every coordinate must first have one positive owner run of exact length
`d+1`, because that condition is equivalent to the existence of its
singleton source letter.

### 7.3 Odd: the unfinished packet replaces the reservoir

If `a_1` is the first connector and `a,b` are the two collar connectors,
the residual extreme bank has charge

\[
 -\bigl(\epsilon(a_1)+\epsilon(a)+\epsilon(b)\bigr).
\]

Adding `a_1` back shows that the unfinished packet has exactly the opposite
charge from the collar.  Hence collar and packet extremes partition into
opposite `A/C` pairs in every residual case `0,1,2,3`.  Explicit
four-coordinate paths take every such pair through a source-decodable
midpoint and on to its complement.  No anonymous scalar reservoir remains.

The only unresolved odd row is occurrence-labelled transport of the at
most four packet blocks to and from the fixed collar before the permanent
double head exists.  A promising refinement is a stationary marked-corridor
guard: once one `B` or earlier tag is changed to its disjoint `mu`-mark,
that fixed guard locates every strict local swap while the marked corridor
grows and later shrinks.  Noncrossing cancellation supplies such guards
except for a finite collection of adjacent/one-interior-block cases.  Those
finite cases still require literal paths and an independent audit.

### 7.4 Current three statements

The shortest current route to `nu(k)<=B(k)+O(1)` consists of:

1. a raw four-to-three first-kill incidence inequality proving (7.1), plus
   pointwise or annealed terminal component joining;
2. the PBBS-relative deep payload atlas and palette-safe fusion; and
3. the bounded odd midpoint-packet shuttle, including its finite guardless
   cases.

All three statements are strictly smaller than their predecessors.  None
is yet proved in full, so the additive-constant theorem remains open.
