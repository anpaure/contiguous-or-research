# `k=16`: current exact frontier after the even quotient reduction

Date: 2026-07-29  
Status: exact reductions and finite certificates; no length-`12873` word is
claimed.

## 1. Target

For `k=16`,

\[
 r=8,\qquad W=\binom{16}{8}=12870,\qquad d(16)=3,
 \qquad B(16)=12873.
\]

The all-`k` deadline argument proves `nu(16)>=12873`.  Equality remains the
first open finite case.

### Strongest unconditional near-carrier: 123 holes, with one exact orbit descent

An explicit asymmetric two-rail factor is now frozen.  Put the audited
all-depth, positive-resident rank-eight `k=15` factor on the shore omitting a
new coordinate `z`.  On the `z` shore put the complements of the audited
zero-resident, double-q1 rank-eight factor.  Physical replay gives a spanning
factor of `J(16,8)` with

```text
12,870 distinct middle owners,
28 cyclic components,
minimum positive run 4 and zero positive-residence violations,
zero lower-q1 and upper-q1 holes,
all fixed shadows complete except 45 lower-q2 and 78 upper-q3 masks,
all arbitrary-width upper ranks complete except the same 78 rank-11 masks.
```

Thus the minimum carrier problem is no longer factor existence: this
explicit object is only `123` literal shadow masks from the canonical carrier
gate.  It is not yet compiler-ready, and the `123` holes cannot be silently
charged to the final word.

```text
scratch/build_audit_k16_asymmetric_two_rail_factor_20260729.py
SHA-256 de0c7faf3f67d01f9159936b4ae07f79798c7df161915890c3ed1d91d85246c6

scratch/k16_asymmetric_two_rail_factor_20260729.json
SHA-256 4f5368d063bcfddfe5c2be6d7f68d5ebc38327ee3c4f40d6b00d9d05c1ace139

scratch/k16_asymmetric_two_rail_factor_20260729.audit.json
SHA-256 d7aa0e13f0e30d0d814187d6892662cc4234d7f81e901c70bac4559fe3377e23
```

The first exact compound repair has now been found and physically replayed.
Among `211,067` positive-residence-compatible directed seams, all `2,023`
reciprocal two-edge switches fail to make a positive shadow gain while
preserving both q1 shores and the lower-q2/upper-q3 ledgers.  Directed
three-cycles behave differently: exactly `15` are simultaneously q1-safe,
deep-safe, and gainful.  They are pairwise cut-disjoint, lie in one source
component, have mutual cyclic cut gap at least seven, and form one complete
`Z_15` orbit.

Applying all fifteen cycles at once repairs the upper-q3 orbit represented by
`39911`.  Literal replay gives

```text
double q1 and positive residence unchanged,
lower-q2 holes unchanged at 45,
upper-q3 holes reduced 78 -> 63,
arbitrary-width rank-11 holes reduced 78 -> 63,
no arbitrary-width rank-12 holes.
```

The move creates fifteen *fixed-width* upper-q4 holes, but all fifteen masks
remain covered by intervals of other widths.  Thus the strict fixed-window
hole count stays `123`, whereas the objective-relevant lower-fixed plus
arbitrary-upper deficit falls to `45+63=108`.  Re-running the exact short
cycle census on the repaired carrier finds no further positive q1/deep-safe
cycle of length two through seven.  The length-five census contains `29,521`
provider-containing cycles (`988` preserve the deep ledger, none preserves
q1); length six contains `404,759` (`4,975` preserve the deep ledger, none
preserves q1); an exact q1-pruned length-seven traversal visits 236 million
DFS nodes and finds no q1-safe cycle at all.  Moreover, among all `1,263`
authenticated deep-safe gainful
cycles of lengths three through five, no nonempty subset preserves q1 even
after dropping cut separation and all deep-shadow constraints.  A solver-free
unit-load peeling certificate deletes `1,235` candidates in its first round
and the remaining `28` in its second; an independent 1,263-variable CP-SAT
optimization has optimum zero.

The first further descent occurs at length eight.  The exact q1-safe census
finds precisely fifteen deep-safe unit-gain cycles.  They are one complete
`Z_15` orbit and use 120 pairwise-distinct cuts, so their successor
permutations commute.  Applying the whole orbit and independently replaying
the physical factor preserves both q1 palettes and positive residence, leaves
the lower-q2 deficit at `45`, and reduces arbitrary upper rank-11 holes
`63 -> 48`.  The current objective-relevant deficit is therefore

```text
45 + 48 = 93.
```

The fifteen fixed-width q4 holes remain covered by other interval widths and
there are no arbitrary rank-12 holes.  This is a genuine nonlocal repair, not
a completion.  The successor census has now been rerun exactly through
length nine.  There is no q1-safe positive cycle at lengths three through
seven; all 45 q1-safe length-eight cycles fail the lower-q2/upper-q3 ledger;
and length nine has thirty scoped-safe unit-gain cycles in two `Z_15` orbits.
Their compatibility graph has exact independence number seven.  Complete
physical replay nevertheless shows that every representative repairs one
rank-11 hole while creating two rank-10 holes and one lower-q3 hole, for net
objective change `+2`.  Hence the `93`-hole carrier has no all-depth-safe
single port-cycle repair through length nine.  Length at least ten, or a
compound allowing temporary defects and later cancellation, is necessary in
this source-relative move class.  A capped length-ten run completely exhausts
1,777/5,425 provider anchors (32.8%) with no scoped-safe cycle in that region,
but leaves 3,648 anchors unsearched; it is a partial census, explicitly not a
length-ten no-go.  The global separated port-permutation master now supersedes
further one-length-at-a-time escalation.

The exact provider graph of that master gives a stronger service floor than
the raw `ceil(93/2)=47` count. Among 211,604 seams, 193 hit two missing
targets, inducing 119 distinct target pairs. Eighteen of the 93 defect
vertices are isolated in this double-provider graph, so at most 37 two-hit
services can be target-disjoint. A frozen 37-edge matching plus 19 singleton
providers proves that the provider-only minimum is exactly

```text
93 - 37 = 56 seams.
```

Port closure raises this substantially.  The current direct certificate puts
positive integer weights in `{1,2,4}` on all 93 defects, of total 207, and a
seven-level integer potential on the 12,870 ports.  Every one of the 211,604
seams satisfies

```text
weight(hits(e)) <= 2 + potential(head(e)) - potential(tail(e)).
```

Endpoint balance telescopes the potential, proving the unconditional exact
fractional bound `2*cut_count>=207`, hence at least 104 cuts.  An independently
replayed denominator-four primal circulation of value `207/2` proves this LP
bound tight.

At equality 104 there are exactly two integer ledgers: exact-once target
service with total dual slack one, or one repeated weight-one target with
total slack zero.  Deterministically emitted no-port-capacity CNFs and
independently checked compact DRAT proofs exclude both.  Therefore every
binary endpoint-balanced repair in this source-relative catalogue uses at
least

```text
105 cuts.
```

The canonical theorem is
`MATH_THEOREM_K16_DIRECT_DUAL_AND_EQUALITY_FLOOR105_20260730.md`
(SHA-256 `c10b3bd2c7844f34cee262f254bdb11627e7211bf51e7b708b68d5d8bd7d2017`),
with the 47-artifact inventory
`scratch/k16_floor105_proof_bundle_20260730.manifest.json`
(SHA-256 `05aacd9f090cc5e09905bdd694bc195eacf2b01dec945fe67ff804e186509b37`).
It omits physical port capacity and therefore applies a fortiori to the exact
separated-port master, but it remains source-relative and is not a lower
bound on arbitrary K16 carriers.

The master has been rebuilt and regression-tested with `cut_count>=105`:
224,475 variables and 112,484 constraints.  The first aggregate reduced
count-105 balance/service/capacity model retained 179,113 cycle-eligible arcs
and returned `UNKNOWN` after 300 seconds.  This is not a verdict.  The exact
identity `repeat weight + dual slack = 3` gives six smaller branch models;
those are the current constructive frontier.  No full physical count-105
master has been launched without a reduced witness.

```text
scratch/solve_k16_len8_physical_93_multicut_cegar_20260730.py
SHA-256 1f6bdb8f1addce0ced7442d13b04e7beb574ed4d1b7857966cee230186cf3308

scratch/k16_separated_port_master_floor105_build_20260730.audit.json
SHA-256 38039a504a4d5b9fc598f276e8ab0e4e0bf89048220e6eb2aa022bb8c5d69e24

scratch/k16_separated_port_master_floor105_regression_20260730.audit.json
SHA-256 926ce0e049877a5d5ba25e8b9ce9bc590548717e5e0c1a4d81319710da1aad01

scratch/k16_floor105_reduced_capacity_20260730.audit.json
SHA-256 fec7b3ee864d8a698785b47510d30a0f1eef4636c103bdc0da305eaed6cbec0c
```

```text
scratch/audit_k16_asymmetric_reciprocal_2switches_20260729.py
scratch/k16_asymmetric_short_rethread_cycles_20260729.audit.json
scratch/materialize_k16_asymmetric_triangle_orbit_repair_20260729.py
scratch/k16_asymmetric_triangle_orbit_repair_20260729.json
scratch/k16_asymmetric_triangle_orbit_repair_20260729.audit.json
scratch/k16_asymmetric_short_rethread_cycles_round1_len5_20260729.audit.json
scratch/k16_asymmetric_short_rethread_cycles_round1_len6_20260730.audit.json
MATH_K16_COMPOUND_SHORT_CYCLE_Q1_NO_GO_20260730.md
MATH_THEOREM_K16_ASYMMETRIC_LENGTH8_ORBIT_REPAIR_20260730.md
scratch/materialize_k16_asymmetric_len8_orbit_repair_20260730.py
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json
```

### New unrestricted-factor reduction (sufficient, not WLOG)

There is a clean no-cross route which is strictly broader than the fixed
`(c,t)` catalogue but is still only a sufficient subclass.  Partition the
rank-eight deck by a new coordinate `z`.  If

* `A` is a positive-depth-four, double-`q1` factor of `J(15,8)`, and
* `B` is a positive-depth-four, double-`q1` factor of `J(15,7)`, with every
  component of length at least four,

then

\[
                         A\ \sqcup\ (B+z)
\]

is a spanning positive-resident, double-`q1` factor of `J(16,8)`.  The
audited `k=15` source already supplies `A`.

Moreover its turn derivative

\[
 X_i=T_i\cap T_{i+1}
\]

already supplies a double-`q1` factor `B_0` of `J(15,7)`: upper colours are
the `T_i` exactly once, and lower colours are the depth-two intersections of
`T`.  Its only residence defects are 1,425 runs of length three.  Their exact
closed-collar transversal is 900 physical edges, or 60 edge orbits on
`Z_426`.  Thus the weakest source-relative theorem sufficient for this
unrestricted carrier is a q1-preserving global rethread of `B_0` eliminating
those runs.  No zero-run condition or complement symmetry is required.

The exact smallest sufficient trade statement is now a rainbow endpoint
matching.  Cut a collar transversal `H`, require all retained paths to have
at least four vertices, and perfectly match their endpoints by
residence-compatible Johnson edges.  The new union colours must be exactly
the cut upper colours, and their intersections must restore every lost lower
colour.  At the minimum equivariant cut size 60, at least 12 globally unique
lower-colour orbits (180 physical colours) are necessarily cut and must be
restored.  The exact frontier for cut sizes `60..90` is frozen in the theorem
note and its deterministic audit.

The exact fixed-cut selector has now been implemented and independently
replayed.  For the saved minimum `60`-orbit transversal it has only `4,529`
CNF variables and `10,516` clauses, but is already infeasible before any
residence clauses: that particular cut set admits no degree-preserving,
lower-q1-restoring rethread.  Allowing the old edge inside each of the 31
saved DP witness banks of sizes `60..90` gives a SAT static factor followed
by `57..72` universal bad-path clauses and then UNSAT in every case.  This
rules out exactly those 31 banks, not all collar transversals.

```text
MATH_K15_FRR_FIXED_H_SELECTOR_CNF_AUDIT_20260729.md
scratch/k15_frr_h60_exact_result_20260729.json
scratch/k15_frr_frontier_witness_bank_scan_20260729.json
```

The joint cut-and-replacement model was superseded by a stronger static
endpoint theorem.  Once cut gaps are at least four, all capped inward traces
are source-fixed for *every* cut budget, leaving `426` cut bits and `2,000`
prevalidated residence-compatible seam bits.  The collar/spacing DP proves
that at least `60` cut orbits are needed.  Dropping the collars and every
lower-colour row, the exact endpoint/upper-rainbow system supports at most
`41` cut orbits.  A size-41 witness is independently replayed, while the
assertion `>=42` has a checked DRAT refutation (`drat-trim: s VERIFIED`).
An independent CNF implementation reproduces both bounds with Kissat and
CaDiCaL.  Hence

\[
                  60\le |H|\le41
\]

would be necessary: no `Z_15`-equivariant Theorem-4B.1 rethread of this fixed
source exists at any budget, before lower-shadow restoration.  The earlier
joint-H CEGAR ended `UNKNOWN_TIMEOUT` and is recorded only as superseded,
never as UNSAT.  Nonequivariant FRR and unrelated RTR factors remain open.

```text
MATH_THEOREM_K15_FRR_STATIC_ENDPOINT_EXACT_COVER_20260729.md
MATH_NOGO_K15_FRR_EQUIVARIANT_60_VS_41_20260729.md
scratch/frr_static_b60_20260729/k15_frr_static_endpoint_stage_20260729.json
SHA-256 b842f9721004f297729a255aa21441d1075b14c6a192d4486b0b5ac915d70029
```

A stronger symmetric alternative is a bi-resident, double-`q1` factor `G`
of `J(15,7)`; complement doubling `G` gives both even shores.  Both
reductions, the boundary/excess identity, and the exact one-map
turn-selector formulation are proved in

```text
MATH_THEOREM_K16_BIRESIDENT_COMPLEMENT_DOUBLE_AND_TURN_SELECTOR_20260729.md
```

Neither reduction is WLOG for an arbitrary factor of `J(16,8)`: cross-shore
edges and two unrelated rail factors remain possible.

## 2. The even equivariant normal form is proved

Writing `z` for the distinguished coordinate and rotating the other fifteen,
every unit-voltage equivariant cyclic carrier is encoded by

\[
 c\in\{0,1\}^{12870},\qquad t\in\{0,1\}^{858}.
\]

The class-sum, generalized start/end transversality, two middle necklace
bijections, and residence laws in

```text
MATH_EVEN_EQUIVARIANT_CT_NORMAL_FORM_20260729.md
```

have been independently exhaustively checked in the complete `k=4,6`
state spaces.  This is an exact sufficient subclass, not a claim that every
optimal even word is equivariant.  The known `k=14` optimum is not in it.

At `k=16`, the exceptional size-five necklace orbits at old ranks six and
nine sharpen the top-run count from the raw `95` to

\[
                         h\le 94.
\]

### Compact exact encoding of the same equivariant catalogue

The original eager `(c,t)` model expands every target against every start,
phase, and width.  Static counting shows that its upper catalogue alone
would create about 123 million selector variables and billions of generated
rows; the reported 33.5 GB middle build was therefore not the eventual model
size.

There is an exactly equivalent projection for the same width catalogue.
For each physical quotient window `S`, introduce only its canonical rotation
identifier

\[
 \operatorname{cid}(S)=\min_{s\in\mathbb Z_{15}}
       \operatorname{code}(\rho^sS).
\]

Middle ownership is one `AllDifferent` over the 858 middle identifiers;
freeness and the equal layer counts turn this injection into the two required
bijections.  Each `q1`, `q2`, or upper target then has one witness-index
variable and one `Element` equality into the list of actual window IDs.
This is equivalent in both directions to the old phase-selector model: a
selector supplies the witness index, while equality of canonical IDs recovers
some valid phase.

The estimated `k=16` model falls from roughly 151 million selector variables
to about 162,000 variables, with about 10.2 million native `Element`
references.  A positive output remains only a carrier certificate and must
still pass cut, compiler, and literal verification.  A negative output is
only for the encoded width catalogue `(2,3,4,6,9,13)` unless a separate
width-completeness theorem is supplied.  Full audit and equivalence proof:

```text
AUDIT_CLAUDE_EVEN_EAGER_K8_K10_COMPACT_ENCODING_20260729.md
```

The self-contained replacement is now implemented in
`scratch/search_even_eager_canonical_id_20260729.py`.  It solved `k=8` from
scratch in 0.20 seconds and passed the independent physical carrier audit.
At `k=16` it builds a valid 161,793-variable / 823,314-constraint model in
9.75 seconds with 1.52 GB peak RSS and no swap.  Thus the memory obstruction
of the old eager encoding is removed in practice.  This compactness is not
yet a search-time theorem: the unrestricted `k=10` validation solve remained
`UNKNOWN` at 300 seconds despite its much smaller model.

The old eager `h=1` two-rail implementation has now been retired by an exact
size audit, not by a mathematical UNSAT result.  After allocating 3,439,436
`q2` selectors it still had to allocate 61,565,361 upper selectors
(29,490,890 already at rank nine), each with several generated implications.
It reached 138 GB RSS before finishing the first upper rank and was terminated
to prevent a second host OOM.  Consequently the two-rail *slice remains open*;
only that selector-expanded implementation is closed.  Any further test must
use the compact canonical-ID encoding or another projected model.

The first frozen compact solve entered CP-SAT at about 3.7 GiB RSS but hit the
hard 12 GiB address-space cap (`std::bad_alloc`) without disturbing the host.
A second run is live under a hard 32 GiB cap and four workers.  Both use the
same 161,793-variable / 823,330-constraint audited model.  This carries no
mathematical status until it returns `CARRIER_PASS_CATALOGUE_CYCLIC` or a
catalogue-scoped UNSAT result.

An exact CNF projection is also available.  Independently phase each physical
window and route the required orbit representatives to fixed outputs through
four arbitrary-size Waksman partial-permutation networks.  This is equivalent
to canonical-ID coverage but removes native `MinEquality`, `AllDifferent`,
and `Element` products.  At `K=16` the exact CNF has 3,984,274 variables,
15,455,173 clauses, and 44,812,655 literal references.  The `K=8` instance
solved SAT and passed an independent physical audit.  A single-core K16
Kissat portfolio is live under a hard 16 GiB cap; its 379 MiB CNF was generated
streamingly on H100.  Scope remains the same explicit width catalogue:

```text
MATH_K16_EXACT_BENES_KISSAT_ENCODING_20260729.md
scratch/search_even_eager_benes_cnf_20260729.cpp
scratch/decode_even_benes_kissat_20260729.py
```

### The marginal two-rail skeletons exist, but fixed-path gauging is refuted

The later two-rail decomposition correctly reduces a restricted even carrier
to an `A` quotient path and a `B` quotient path plus physical phase gauges.
Two marginal path problems are easy at `k=16`: an independently sound model
finds a 429-vertex `A` path covering all 335 required labels and a 429-vertex
`B` path using 428 distinct labels.  This validates marginal abundance only.
The original path generators credited each chosen quotient arc with every
possible phase label and were therefore loose; their printed coverage counts
were not physical certificates.

For the independently exact pair, all 32 relative affine
multiplier/reversal placements fail the exact seam-and-residence gauge model.
More strongly, each fixed rail chronology is itself open-residence
infeasible in both directions even after deleting the partner rail, both
seams, voltage closure, every palette row, and the right-endpoint residence
conditions, while exempting the first three transitions from early-deletion
clauses.  Thus this pair does not fail because of bad seam alignment: its
chronologies intrinsically cannot be phased with the required residence.

The two-rail class itself remains open.  What is closed is the pipeline

```text
find marginal quotient paths -> assign phases afterward.
```

Any sound successor must choose quotient arcs and phases jointly, with the
three-step residence state carried during path generation.

This joint choice now has an exact phase-free normal form.  A directed
quotient transition option records its relative rotation `delta` and its
deleted/inserted labels.  For each quotient owner `u`, three history values
`h_1(u),h_2(u),h_3(u)` store the last three inserted old coordinates in the
canonical frame.  A selected option `e=(u,v;a,b,delta)` enforces

```text
a != h_j(u)                                      (j=1,2,3),
h_1(v)=b-delta,
h_j(v)=h_(j-1)(u)-delta                          (j=2,3),
```

with the top-coordinate sentinel propagated in the evident way.  These rows
are necessary and sufficient for positive residence; no separate physical
phase variables are required.  At `K=16` the exact one-A-block/one-B-block
model has 858 quotient owners, 54,856 selectable transition options, 2,574
domain-16 history integers, and 1,528 q1 orbit rows, plus ordinary circuit
and voltage constraints.  It replays the known equivariant `K=10` optimum
exactly.  This is the sound successor to paths-first/gauges-later; satisfiability
at `K=16` and deeper shadows remain open.

```text
AUDIT_CLAUDE_TWO_RAIL_ENCODING_20260730.md
AUDIT_CLAUDE_TWO_RAIL_K10_K16_SKELETONS_20260730.md
MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md
scratch/audit_claude_exact_covering_rail_path_20260729.py
scratch/audit_k16_rail_path_phase_residence_20260730.py
scratch/audit_joint_rail_quotient_history_model_20260730.py
scratch/claude_exact_arail_n15_20260730.audit.json
scratch/claude_exact_brail_n15_20260730.audit.json
scratch/claude_open_a_rail_residence_rev0_20260730.audit.json
scratch/claude_open_a_rail_residence_rev1_20260730.audit.json
scratch/claude_open_b_rail_residence_rev0_20260730.audit.json
scratch/claude_open_b_rail_residence_rev1_20260730.audit.json
```

### Fixed-parent braided-complement route is refuted

The cheap odd-to-even proposal “take an odd carrier and its complemented
copy, then choose a small seam schedule” has been audited exactly.  The cross
edge test `X union Y = [15]` is correct, but it enforces only Johnson
adjacency; residence and both q1 palettes remain independent constraints.

For the known optimal `k=15` factor, parent positions 796--800 have
coordinate-zero trace `1,0,0,0,1`.  The complemented rail therefore contains
the forbidden child run `0,1,1,1,0`, so one of its four internal edges must be
cut.  Each of those four edges is the unique global provider of a different
top lower-q1 colour, and neither an AA nor a cross edge can provide a
top-containing intersection.  Residence requires a cut while q1 completeness
forbids every possible cut.  Hence no arbitrary legal complement seam
schedule can lift this fixed parent.

The exact fixed-parent model passes and compiles at `K=8`, but is infeasible
already at q1 plus residence for the intended `k=9 -> K=10` and known
`k=11 -> K=12` parents.  Independently rethreading the two rails remains open,
but that is the full bilayer problem rather than a small seam CSP:

```text
MATH_AUDIT_BRAIDED_COMPLEMENT_RECIPE_20260729.md
scratch/audit_braided_complement_fixed_parent_20260729.py
```

## 3. The exact quotient edge model

The middle layer modulo `C_15` has `429` A vertices and `429` B vertices.
Its labelled Johnson quotient has

\[
 12012\ AA+3432\ AB+12012\ BB=27456
\]

edge orbits.  A rotation-invariant factor is given by 858 weighted degree-two
rows.  Complete lower and upper immediate shadows are exactly 1,528 colour
cover rows (764 on either side).

The centred PBBS factor on the B shore plus its complementary A factor is a
deterministic solution of this static core.  Hence simultaneous two-sided
`q1` coverage is not conjectural.

A free exact solve also produced a mixed factor with edge counts

\[
 (AA,AB,BB)=(377,104,377),
\]

ten quotient components, thirty physical components, and zero lower/upper
`q1` holes.  It is not resident and misses deeper shadows.

## 4. Connectivity is a higher-trade gate

Three individually colour-safe 2-switches merge the three nontrivial
quotient cycles of that factor, leaving one 852-vertex cycle and six quotient
loops.  No remaining loop has an individually double-`q1`-safe insertion.

The exact six-loop joint insertion ILP has only 149 rows and is infeasible
with both colour palettes.  Its soft optimum gives one physical Hamilton
cycle but leaves three lower and five upper quotient colours uncovered.
Thus the factor is topologically within six insertions of Hamiltonicity, but
ordinary 2-switches cannot finish it without a small shadow defect.  Larger
alternating trades or a fresh global factor are necessary.

One subsequent internal 2-opt on that Hamilton cycle,

```text
remove 25126,23360; add 25046,23361
```

preserves the single physical `12870`-cycle and improves the quotient defect
to two lower and five upper necklace colours.  This is only a quotient-level
diagnostic: two missing lower orbits expand to twenty literal rank-seven
colours, so they exceed the two literal boundary cells of a depth-three
compiler.  The carrier is also far from complete because it has 92 lower-q2
holes, 131 arbitrary-upper orbit holes, and 3,465 short coordinate runs.

This `2+5` factor was then used as the centre of an exact edge-orbit radius
search.  With a diagnostic cap of at most two missing lower-`q1` quotient
orbits (not the two-literal-cell compiler allowance),
radii five through ten are rigorously infeasible.  Radius thirteen is
feasible: thirteen selected edge orbits are replaced, giving one quotient
cycle with exactly two lower *orbit* holes and no upper-`q1` holes.  Its first lift
had voltage of gcd three and hence three physical 4,290-cycles.  A single
parallel-orbit replacement

```text
remove 13230; add 13232
```

keeps the same quotient endpoints and both `q1` profiles, but changes the
voltage to a unit of `Z_15`.  The resulting literal certificate

```text
scratch/k16_connected_q1_lower2_hamilton_20260729.json
```

has one physical Hamilton cycle of length 12,870, exactly two lower-`q1`
orbit holes (twenty literal holes), zero upper-`q1` holes, 89 `q2` orbit
holes, 129 arbitrary-upper orbit
holes, and 3,420 short coordinate runs (375 of length one, 1,635 of length
two, and 1,410 of length three).  This closes middle ownership,
physical connectivity and the upper immediate shadow, but not the literal
lower immediate-shadow compiler gate; it also does not close residence or the
deeper shadows.

The fixed quotient cycle has only 43 adjacencies admitting more than one
parallel edge orbit (50 alternative orbits in total).  An exact motif audit
shows that 3,000 of the 3,420 short runs use no such adjacency in their
entering, internal, or exiting edge window.  Changing a parallel orbit can
only rotate all coordinates together away from that window, so each of those
motifs persists under every phase/voltage reassignment on the fixed quotient
cycle.  Therefore a phase-only repair is impossible: residence requires a
genuine change of quotient topology, not another voltage choice.

The reproducible scripts are

```text
scratch/merge_k16_quotient_doubleq1_factor_20260729.py
scratch/solve_k16_quotient_loop_absorption_20260729.py
scratch/repair_k16_connected_qfactor_radius_20260729.py
scratch/promote_k16_qfactor_parallel_voltage_repair_20260729.py
```

## 5. Residence is local and exactly encodable

For any connected loopless quotient factor, let `b_v` be the selected cross
degree at vertex `v`.  The following constraints are exactly the statement
that both the top trace and its complement have no run of length one, two, or
three:

1. `b_v<=1` at every vertex;
2. for every selected same-shore edge `uv`, not all of
   `x_uv,b_u,b_v` equal one;
3. for every selected same-shore two-path `u-v-w`, not all of
   `x_uv,x_vw,b_u,b_w` equal one.

A compact directed-reach encoding uses 48k auxiliaries rather than a million
explicit motif clauses.  It has been exhaustively checked on every binary
cycle of lengths 3 through 12.

Feasibility is witnessed already at factor level: a particular complementary
PBBS square switch yields exact two-sided `q1`, cross count two, and minimum
top-one and top-zero run length fifteen.  It still has 117 quotient components
and 1,050 old-coordinate short runs.  Thus top residence is solved locally;
old-coordinate residence and connectivity remain coupled.

An exact repair solve around the earlier mixed factor subsequently produced a
top-biresident, double-`q1` factor with two quotient components.  Exhaustive
two-edge splicing found 22 unit-voltage completions.  The first literal trade

```text
remove 22568,25126; add 22572,24966
```

gives one quotient cycle of voltage 11 and hence one physical Hamilton cycle.
Its independently replayed certificate is

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
scratch/k16_qfactor_q1_topresident_hamilton_20260729.audit.json
```

It covers all 764 lower and all 764 upper `q1` orbit colours, and both the top
one-runs and top zero-runs have minimum four.  The remaining fifteen old
coordinates still have 3,390 short runs; the carrier has 88 `q2` orbit holes
and 122 arbitrary-upper orbit holes.  Thus topology, immediate shadows, and
the distinguished-coordinate residence law are simultaneously solved.  The
remaining residence obstruction is entirely on the rotating old coordinates.

For this scaffold, the 3,390 physical old-coordinate violations collapse by
`C_15` symmetry to exactly 226 distinct forcing motifs: 22 selected-edge sets
of size two, 108 of size three, and 96 of size four.  The exact transversal
problem on these motifs has optimum 147.  Consequently every resident factor
obtained from this scaffold must remove at least 147 of its 858 selected edge
orbits before accounting for any newly created motifs.  This certifies that
residence is a global rethread, not a local clean-up.  Reproduce with

```text
scratch/k16_residence_motif_hitting_set_20260729.py
scratch/k16_residence_motif_hitting_set_20260729.json
scratch/audit_k16_residence_motif_structure_20260729.py
scratch/k16_qfactor_q1_topresident_hamilton_residence_motifs_20260729.audit.json
```

The lower bound does not depend on trusting an opaque optimizer.  Every motif
is a cyclic interval in the 858-edge quotient Hamilton cycle, and 300 cycle
edges lie in no motif, so cutting there gives an ordinary interval
hypergraph.  Earliest-finish greedy produces 147 pairwise edge-disjoint
motifs (20 of size two, 72 of size three, and 55 of size four) and the usual
greedy interval stabbing algorithm produces 147 edges.  Hence packing and
transversal numbers are both 147.  The hypergraph has 112 intersection
components, each with at most seven motifs and fourteen edges.

The coupling to the immediate shadows is equally sharp.  No deletion set can
hit all 226 motifs while retaining at least one *current* provider of every
lower and upper `q1` colour.  If palette losses are allowed and minimized
lexicographically before deletion count, the exact optimum deletes 148 edges
and destroys 180 currently supplied colours (88 lower and 92 upper).  New
edges must therefore reconstruct at least 180 immediate-shadow classes while
rethreading residence; the two tasks cannot be solved sequentially.  The
certificates are

```text
scratch/solve_k16_residence_motif_palette_safe_hitting_20260729.py
scratch/k16_residence_motif_palette_safe_hitting_20260729.json
scratch/k16_residence_motif_minholes_hitting_20260729.json
```

## 6. Why the direct `k=15` complement lift fails

For the exact `k=15` answer, let `T=D^3A`.  A direct audit gives

```text
positive runs shorter than 4:       6
zero runs shorter than 4:        2016
```

The B shore `z+complement(T)` inherits the 2,016 zero-run defects as positive
residence defects.  Hence the optimal odd carrier cannot simply be duplicated
and complemented; a genuine rethread is required.  Reproduce with

```text
scratch/audit_k15_carrier_biresidence_20260729.py
```

## 7. PBBS trade-and-braid lane

An exact 27-trade B factor preserves lower `q1` and reduces the B topology to
21 components with one delete-inaccessible component.  A first full-closure
cut solve opened all 21 components with 552 cuts, but lost 16 lower colours;
15 of those had no possible B-B restoration seam among the exposed endpoints.
Consequently both the all-cross and the unrestricted AA/AB/BB macro models
were immediately infeasible on that cut certificate.

This is a scoped no-go for that cut objective, not for the PBBS lane.  A
strengthened cut solve found 567 cuts losing seventeen lower colours, all
seventeen simultaneously B-B-restorable, with sixty length-three segments.
The unrestricted 739k-seam macro then timed out without an incumbent.  The
smaller no-AA model gives a sharper structural obstruction: lower `q1` alone
is feasible with 47 B-B seams, but upper `q1` is infeasible because 62 lost
B-upper colours have neither an exposed B-B union seam nor a safely cuttable
A incidence.  The next cut model must therefore enforce *upper* accessibility
at cut-selection time, just as the previous model enforced lower
restorability.

## 8. Exact remaining gates

A length-`12873` proof now needs one of the following equivalent advances:

1. improve the q1-perfect, top-biresident physical Hamilton factor to full
   old-coordinate residence and the remaining deeper shadows;
2. an integrated PBBS cut/rung/B-B braid satisfying both `q1` palettes and
   seam residence; or
3. a larger alternating trade repairing the `3+5` colour deficit of the
   current connected quotient Hamilton factor while simultaneously reducing
   its short-run motifs.

Any candidate must then pass exact `COMP_3` with a literal `{z}` source and an
exhaustive check of all `2^16-1` nonempty targets.  Carrier coverage alone is
not a word certificate.

## 9. Palette-weighted iterative residence descent

The fixed-cross radius-147 face is exactly infeasible: no factor at that
radius can keep all eighty scaffold AB edge orbits while restoring degree two
and both `q1` palettes.  Allowing the cross pattern to change removes that
obstruction.  The unrestricted exact model found

```text
removed: 76 AA, 8 AB, 63 BB
selected cross edges: 86
quotient components: 3
physical components: 5
top/complement-top residence: PASS
lower/upper q1: 764/764
old-coordinate short runs: 2205
```

The durable factor is

```text
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
```

with file SHA-256
`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`.
This is the first factor on the far side of the certified 147-motif barrier.
It is not resident and is not a word certificate.

Its 2,205 physical violations collapse to 147 quotient motif orbits.  Their
overlap graph has 85 components, none larger than nine motifs.  Exact
componentwise enumeration gives

\[
\nu(\mathcal M)=\tau(\mathcal M)=97.
\]

The ordinary minimum is nevertheless incompatible with upper `q1`.  Motifs

```text
{22511,22520}
{22511,22692,25634}
```

have ordinary transversal `{22511}`, but edge 22511 is the unique selected
provider of upper colour `(1,1907)` and no off-source provider has both
endpoints in the full motif-boundary domain.  A transversal safe for this
locked colour must retain 22511 and use 22520 together with one of 22692 or
25634.  Consequently

\[
\tau_{\rm static\ palette}=98.
\]

This is certified solver-free by

```text
scratch/audit_k16_motif_overlap_minmax_20260729.py
scratch/k16_dynamic_cross_r147_round0_motif_overlap_minmax_20260729.audit.json
```

The 147 motifs split into 85 independent overlap components.  Enumerating
every locally minimum locked-colour-safe transversal yields only 262 options in
total, at most eight in any component.  Choosing one option per component is
an exact normal form for every radius-98 palette-safe cut set.

The complete 262-option model, with every loopless replacement seam on the
full motif boundary, degree two, both `q1` palettes, and dynamic
top/complement-top residence, is **infeasible**.  The diagnostic ladder is:

```text
degree only                  OPTIMAL
degree + lower q1            OPTIMAL
degree + upper q1            OPTIMAL
degree + both q1             INFEASIBLE
degree + both q1 + top       INFEASIBLE
```

Thus top residence is not the radius-98 blocker; the two immediate-shadow
palettes are jointly incompatible at that radius.  Any loopless hard-gate
rethread from this center has radius at least 99.

The tempting radius-99 normal form “one locked-colour-safe minimum option in every
component, plus one extra source cut” is **false**.  In 33 components there
are inclusion-minimal excess-one transversals containing no locally minimum
option.  Moreover, cutting the locked provider 22511 becomes possible once
an outside endpoint is exposed, and this is a distinct branch rather than a
locked-colour-safe minimum extension.  This adjective concerns the one
unreplaceable colour only; the other immediate-shadow rows remain dynamic
constraints of the seam model.

The exact cut space has the following two branches.

```text
branch                         local base   excess budget   compact cores
retain 22511                        98             1             566
delete and replace 22511            97             2             973
```

In the retain branch the exact local option counts at excess 0 and 1 are 262
and 958; 304 inclusion-minimal excess-one cores are absent from the old
minimum-option form.  In the delete branch the exact local option counts at
excess 0, 1, and 2 are 261, 960, and 3442.  A scope-complete extended model
therefore uses all 858 source-cut bits, one audited compact core per overlap
component, exactly 99 cuts, and all 26,570 loopless off-source seams.  The two
branches contain approximately `2.63e40` and `5.28e42` distinct source cut
sets respectively.  The solver-free scope certificates are

```text
scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json
scratch/k16_r99_two_branch_core_scope_independent_20260729.audit.json
```

There is also a sharp solver-free two-palette capacity bound.  Exhaustive
component convolution shows that every retain-branch cut destroys at least
113 unique q1 providers in total, while every delete-branch cut destroys at
least 111.  Since 99 replacement seams can cover at most 99 single-palette
losses without pairing, a feasible completion needs at least fourteen or
twelve seams, respectively, that simultaneously repair a missing lower and a
missing upper colour.  The full Pareto frontiers and replay are in

```text
scratch/audit_k16_r99_unique_provider_pareto_20260729.py
```

This loss count has an exact endpoint-capacitated matching consequence.  For
a proposed cut \(C\), choose one added provider for each lost unique lower
colour and one for each lost unique upper colour.  The two representative
sets lie in the same 99-edge addition, so their intersection has size at
least

\[
L(C)+U(C)-99.
\]

Those intersection seams must be colour-disjoint in each palette and their
incidence at every quotient node is bounded by the cut incidence there.  This
gives a 21,645-variable cut-only necessary relaxation over the 20,787
double-colour seam candidates.  The theorem and exact model census are
audited in

```text
scratch/k16_r99_cut_double_capacity_relaxation_20260729.audit.json
scratch/solve_k16_r99_cut_double_capacity_relaxation_20260729.py
```

The relaxation is not itself an obstruction: canonical retain/delete hints
have demand 14/12 and matching capacity 22.  Its purpose is to optimize a cut
with maximum double-repair slack and feed that cut to the full q1 completion
model.

The exact dynamic optimizer subsequently found much stronger feasible cuts:
retain has `L/U=62/61`, demand 24, matching 49, and slack `+25`; delete has
`L/U=61/60`, demand 22, matching 46, and slack `+24`.  Yet fixing either cut
and solving the complete 99-seam degree-plus-two-palette subproblem is
**INFEASIBLE in presolve**.  Thus even generous endpoint-capacitated
double-repair supply is not sufficient.  These two failures are now the seed
cores for an exact Benders decomposition: cut master, fixed-cut seam
subproblem, guarded UNSAT core, repeat.

In fact their immediate failure already has a solver-free cut-only
explanation.  For each source-unique q1 colour with no parallel replacement,
any replacement uses an alternate quotient node; degree balance forces at
least one source cut incident to that alternate-node set.  This gives 1,328
exact portal inequalities.  The retain high-slack cut violates seven of them
and the delete cut violates six, so neither was a valid seam-completion hint.
The complete portal family is audited in

```text
scratch/ad_k16_r99_unique_colour_portal_rows_20260729.audit.json
```

First-order portal closure is not enough: explicit cuts in both branches hit
all 147 motifs and satisfy all 1,328 implications.  Distinct lost colours in
one palette, however, require distinct added seams.  If `T` is a set of
source-unique colours and `P` is the union of their fixed alternate-provider
portal sets, exact degree restoration gives the stronger Hall inequality

\[
 \sum_{h\in E_0}|\partial h\cap P|x_h
       \;\ge\;\sum_{c\in T}x_{e(c)}.                 \tag{9.1}
\]

The two explicit first-order-feasible cuts violate (9.1): on the lower
palette both have demand/capacity `5/3`, and on the upper palette they have
`8/4`.  This strictness is reconstructed without an optimizer in

```text
scratch/audit_k16_r99_portal_hall_strictness_20260729.py
scratch/k16_r99_portal_hall_strictness_20260729.audit.json
```

Moreover, the strongest violated member of this fixed-portal family has a
polynomial separator.  Give each colour node profit `x[e(c)]`, each portal
node cost equal to its source-cut incidence, and force a selected colour to
select every node in its portal set.  Maximum-weight closure, equivalently
one source/colour/portal/sink min-cut, maximizes the violation of (9.1), also
for fractional master solutions.  Thus the radius-99 Benders master can
separate the whole second-level family instead of accumulating hand-picked
subsets.

Separate-palette closure still does not finish the master: after 33 learned
retain rows and 16 delete rows, both branches contain explicit cuts satisfying
every motif, all first-order portals, and the entire same-palette Hall family.
The next exact level couples lower colour, upper colour, and endpoint capacity
of each possible double-repair seam.  An integral cover of these 20,787
four-feature hyperedges yields the valid dual Benders inequality

\[
  \operatorname{cover\_cost}(x)\ge L(x)+U(x)-99.       \tag{9.2}
\]

For the same-palette-feasible candidates, retain has cover cost 30 against
demand 44 (deficit 14), while delete has 39 against 42 (deficit 3).  Every
hyperedge and all nonzero signed coefficients replay solver-free in

```text
scratch/k16_r99_joint_double_hypergraph_cover_20260729.audit.json
```

This rejects the two current candidates, not either complete branch.  It
identifies joint lower/upper/endpoint compatibility—not marginal provider
counts—as the next separation layer.

For the implemented `(x,y)` master this family is a projected certificate,
not a new integer-feasibility gate: summing the colour and endpoint capacity
rows indexed by any cover gives `cover_cost(x)>=|y|>=L+U-99`.  The production
master therefore installs no joint-cover projection row and runs no redundant
per-candidate cover ILP.  The artifact verifies explicit covers, not minimum
covers; four-partite minimum cover is not the same-palette
max-closure/min-cut problem.

The first delete-branch cut to pass that joint capacity test (`6c98`) was
then frozen and solved exactly for all 198 quotient endpoint degrees and all
764 lower plus 764 upper `q1` rotation-colour rows.  The selector-free CNF
has 9,938 variables and 19,816 clauses.  Independent CaDiCaL 1.9.5 replay on
the H100 CPU returned **UNSAT** in 0.011 seconds (26 MiB maximum RSS):

```text
scratch/k16_r99_joint_matching_delete_20260729.audit.json
scratch/k16_r99_fixed_delete_6c98_degree_q1_20260729.build.json
scratch/k16_r99_fixed_delete_6c98_degree_q1_20260729.cnf
scratch/k16_r99_fixed_delete_6c98_degree_q1_20260729.solve.json
```

Thus joint capacity is necessary but not sufficient.  The exact conflict
from this frozen add problem is the next sound Benders row; this result does
not close the full delete branch.

That conflict has now been reduced to a solver-free four-colour Hall cut.
The deletion-minimal q1 core consists only of upper colours

```text
(1,1883)  (1,1907)  (1,3255)  (1,5939).
```

Their 140 off-source provider seams form four `K9` blocks with the unique
source edge removed.  A minimum 26-node endpoint cover `P` meets all 140,
but exact degree restoration gives `P` only three units of endpoint
capacity.  Hence the globally valid projected Benders inequality is

\[
 \sum_h |\operatorname{ends}(h)\cap P|x_h
 \;\ge\;x_{4742}+x_{22511}+x_{23229}+x_{24034}.
\]

At `6c98` its two sides are 3 and 4.  The row remains valid for fractional
cut/add recourse and in both retain/delete branches.  It excludes at least
713 distinct delete-branch radius-99 cuts that hit all 147 source motifs,
not merely the discovery assignment.  The 52-coefficient master row and all
140 provider incidences replay independently in

```text
MATH_THEOREM_L_K16_R99_6C98_ENDPOINT_COVER_BENDERS_20260729.md
scratch/k16_r99_fixed_delete_6c98_q1_core_20260729.json
scratch/k16_r99_6c98_fourcolour_endpoint_cover_cut_20260729.audit.json
scratch/k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.audit.json
```

This is an arbitrary endpoint-cover Hall row, strictly beyond the canonical
portal-union closure; it is installed as an eager same-palette row rather
than mislabelled as a joint-hypergraph-cover row.  The full delete branch
remains open.

An exhaustive one-swap replay makes that family statement quantitative.
Among 74,382 branch-preserving swaps, 65 violate this row while satisfying
all static master rows; 11 of those also retain the explicit 35-edge joint
matching witness and hence satisfy the full previously seeded delete master.
The solver-free replay is

```text
MATH_AUDIT_K16_R99_UPPER4_HALL_BENDERS_FAMILY_20260729.md
scratch/k16_r99_upper4_benders_one_swap_family_20260729.audit.json
```

The guarded master has been rerun with this row under a hard 2 GiB cap
(single-thread CaDiCaL, under 91 MiB observed RSS per branch).  The next delete
candidate has a lower-Hall deficit one and joint-cover deficit three; the next
retain candidate has an upper-Hall deficit one and joint-cover deficit eleven.
They were separated and added to the masters, giving 17 Hall plus 3 joint rows
on delete and 34 Hall plus 2 joint rows on retain.  Neither branch has yet
returned a joint-feasible replacement cut:

```text
scratch/k16_r99_joint_guarded_upper4_delete_20260729.json
scratch/k16_r99_joint_guarded_upper4_retain_20260729.json
```

After 43 cumulative guarded rounds per branch, neither master has yet passed
both marginal Hall and joint cover.  Delete has 70 Hall plus 45 joint rows;
its best Hall-feasible joint deficit is four.  Retain has 86 Hall plus 44
joint rows; round 39 was Hall-feasible and missed joint cover by exactly one
(`40<41`).  Peak RSS stayed below one GiB.  This shows the separation loop is
approaching the boundary but is not yet an existence certificate:

```text
scratch/k16_r99_joint_guarded_upper4_delete_r43_20260729.json
scratch/k16_r99_joint_guarded_upper4_retain_r43_20260729.json
```

Those guarded artifacts are historical cut-discovery runs.  In the corrected
production normal form their joint-cover rows are omitted because the lifted
matching layer already implies them.  The master instead installs the
four-colour arbitrary endpoint-cover row above, giving 21,645 variables and
3,691/3,692 retain/delete constraints.  The next recourse tier is the
branch-free four-colour degree oracle (863 native constraints), followed only
if needed by the complete branch-free both-q1 oracle (27,428 variables and
2,387 constraints).  The latter contains no branch/master rows, so every
replayed positive assumption core is valid in both masters.  No new H100 run
is claimed under the active resource freeze.

As a complementary exact diagnostic, one canonical motif-hitting cut was
constructed at every point of the two Pareto frontiers (14 retain witnesses
and 15 delete witnesses).  Fixing each cut and solving only for 99 balanced
replacement seams with both q1 palettes gives **INFEASIBLE for all 29**, almost
always in presolve.  This rejects those canonical representatives, not every
cut with the same loss pair; it demonstrates that provider counts alone do
not determine feasibility.  The reproducible bank and sweep are

```text
scratch/k16_r99_pareto_cut_witnesses_20260729.audit.json
scratch/k16_r99_fixed_pareto_sweep_20260729.audit.json
```

Two independent exact degree-plus-two-palette portfolios have now run.  The
core-witness encoding returned `UNKNOWN` in both branches after 600 seconds;
the selector-free raw-plus-Pareto encoding returned `UNKNOWN` in both branches
after 1,800 seconds.  None found an incumbent and none proved infeasibility.
Thus radius 99 remains open.  A feasible incumbent would only be a q1-stage
checkpoint: newly created positive residence motifs must still be separated
by CEGAR before the factor is called resident.  Infeasibility of both
branches, if eventually proved, would certify radius at least 100 for every
resident rethread about this center.  The next frozen fallback uses a
projection-bijective exact graded option encoding, seeded by the cut-only
double-repair optimizer.

## 10. Fully resident PBBS endpoint

The oriented-port PBBS model now chooses cuts and seam orientations jointly,
rather than trying to repair a fixed cut set.  Its first spanning physical
2-factor had seven components and **zero residence violations in all sixteen
coordinates**.  A ten-minute warm continuation retained exact residence,
reduced the factor to two components of lengths 4435 and 8435, and improved
the immediate-shadow deficit to

```text
lower q1 holes: 492
upper q1 holes: 698
```

A second warm continuation improved the palette total again, to 443 lower
and 646 upper holes (1,089 total), though topology moved back to four
components.  Thus resume 1 remains the best topology endpoint and resume 2
the best palette endpoint.

The independently audited artifacts are

```text
scratch/k16_pbbs_oriented_noaa_softq1_20260729.json
scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
scratch/k16_pbbs_oriented_noaa_softq1_resume2_20260729.json
```

This is complementary to the quotient endpoint above: one factor is
q1-perfect but nonresident, while the other is fully resident but
palette-defective.  Their physical edge symmetric difference therefore
defines an exact alternating-circulation lattice.  For the *first* resident
endpoint, the complete circulation model (vertex balance, all 22,880 literal
q1 rows, and all 2,205 initial short-motif closures) is infeasible.  This is
an endpoint-specific no-go, not by itself a no-go for PBBS.
No claim is made until a factor passes both palettes, residence, topology,
`COMP_3`, and exhaustive word coverage.

The exact overlay tests have now been repeated for the original resident
endpoint and both warm continuations; all three are infeasible.  They share
one explicit static Hall lock: physical motif 1993 (coordinate 9, run length
2) has closure edges

```text
(45358,45614), (45614,47630), (47246,47630).
```

Every closure edge removable in each overlay is a unique provider of a lower
or upper q1 colour, and the resident-only side supplies no replacement of
that colour.  Thus no balanced union of alternating circuits inside any of
these three pairwise overlays can hit the motif while preserving q1.  The
reproducible audit is

```text
scratch/audit_k16_overlay_static_hall_obstructions_20260729.py
scratch/k16_overlay_three_endpoints_static_hall_obstruction_20260729.json
```

This links the two live lanes: a q1-preserving pretrade of the common source
that moves this locked motif, a full radius-99 residence rethread, or a larger
multi-factor/AA-enabled move is required before the PBBS overlay can help.

The first alternative is now realized locally.  Three chained quotient
2-trades give a radius-five q1-neutral preconditioner

```text
remove: 2678, 4423, 18185, 24034, 24140
add:    2693, 4421, 18183, 24038, 26703
```

that preserves degree two and both 764-colour q1 palettes.  It moves motif
1993; against the two-component resume-1 resident endpoint the complete
static Hall-obstruction audit is now empty.  The preconditioned q1 factor has
five physical components and 2,250 short motifs, so it is not itself resident
or final.  Its role is to open a genuine alternating-circulation portal that
the original endpoint lacked.  The audited artifact is

```text
scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json
```

The exact portal-versus-resume-1 circulation model is nevertheless
**infeasible in presolve**.  Thus eliminating every single-motif static lock
is necessary but not sufficient: the remaining obstruction is a grouped
Hall deficiency coupling several motif closures through degree and q1 rows.
This closes the radius-five pairwise overlay, while supplying a much sharper
dual target for the next portal or AA-enabled descent.

Unit propagation reduces that grouped obstruction to six rows.  Motif 15 has
closure

```text
b1=(50531,51042), common=(50531,52547), b3=(52547,56642).
```

Unique upper colour 51043 has no resident-only provider, so `b1` cannot be
cut and the motif forces `b3` to be cut.  The upper-56643 row then forces its
sole resident replacement `r=(55619,56579)`.  At vertex 55619 the two blue incident edges
`(55491,55619)` and `(55619,63747)` are themselves protected by unique uppers
55747 and 63811 with no resident-only providers.  Degree balance therefore
forbids `r`, a contradiction.  The next pretrade need only break this explicit
motif-plus-four-colours-plus-one-vertex core while keeping the earlier portal
open; blind global overlay searches are no longer justified.

An explicit physical alternating six-cycle does break this core while
preserving both q1 colour multisets exactly:

```text
delete: (50475,50979), (50531,51042), (50538,50986)
add:    (50475,50986), (50531,50979), (50538,51042)
```

It keeps motif 1993 unlocked and leaves zero single-motif static blockers,
but replaces three old residence motifs by three fresh ones; the total stays
2,250.  Thus raw motif count is not a descent potential.  Full unit
propagation of motif, degree, and both q1 rows instead peels 27 disjoint
interaction cores involving 40 motif rows (7 length-one, 25 length-two, 8
length-three) across fourteen coordinates; 39 lie in the giant overlay
component.  The current portal beam minimizes this interaction-core count,
not the number of individually locked motifs.

This proof-directed potential now has a complete greedy, solver-free descent
of the *known local* obstruction while preserving both `q1` palettes exactly
and keeping zero static blockers:

```text
27/501 -> 21/390 -> 18/301 -> 16/249 -> 14/226 -> 12/213
       -> 11/166 -> 9/150 -> 8/110 -> 7/86 -> 6/64 -> 5/49
       -> 4/42 -> 3/18 -> 2/12 -> 1/7 -> 0/0.
```

The second trade is

```text
delete: (39532,55852), (39544,40552), (39596,39656)
add:    (39532,40552), (39544,39656), (39596,55852).
```

It is recorded in

```text
scratch/k16_resume1_core21_hitting_portal24_20260729.json
```

with SHA-256
`bf0b3e46913ee69783c045298bf2bf48034861902e6a029d3c374d8981f79942`.
The final radius-four trade is

```text
delete: (34233,34281), (37305,37337), (38345,42441), (41401,42409)
add:    (34233,42409), (34281,42441), (37305,41401), (37337,38345).
```

The materialized endpoint is

```text
scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_20260729.json
physical-edge digest:
432839c8e7c28cf6862b7d69a97ad6126968c73c4453bcaf600931fcfe3fd749
```

The endpoint file SHA-256 is
`6f614ae41d1264121acc7cfb1b3303f3bb93532d57aeac1d0153e3f344a73f53`;
the complete sixteen-step ledger is
`scratch/k16_resume1_zero_full_unit_core_descent_ledger_20260729.json`
(SHA-256
`9ae67fa10c220e5216d837f0a922b3716ed7820d89862db4b73f84de40826698`).

It has four components, zero lower/upper `q1` holes, 2,250 short residence
runs, and score `(0,0,0,2250,4)`.  This is the first endpoint for which full
unit propagation finds neither an interaction core nor a static blocker.
It is **not yet a feasible overlay certificate**: absence of these local
cores is only a necessary condition.  The unrestricted red/blue circulation
with dynamic residence CEGAR must still return a positive literal factor.
The result nevertheless establishes that the grouped-Hall core count is a
powerful descent potential beyond the first move, unlike raw motif count.

The exact full overlay model has already been built against this endpoint:
24,959 variables, 37,997 constraints, 12,479 variables on each shore, 2,250
initial motif cuts, and no fixed-common unrepairable motif.  Its frozen model
SHA-256 is
`c2a5cf5e56dfbc6cebe021a92fa46c8999ec6206a9649d8d37e3c8466217e1ec`.
After partial H100 recovery the exact degree-plus-both-`q1`-plus-all-initial-
motifs model returned **INFEASIBLE in its first solve**, before any dynamic
CEGAR round.  The complete result is

```text
scratch/k16_zero_full_unit_core_overlay_solve_20260729.json
SHA-256 6995f5d2d6e2b10385cd2d342b39fc93d10b3455437b27f26048890dbdb4902b
```

Therefore zero peeled unit cores is not sufficient: this endpoint contains a
genuinely higher-order overlay obstruction.  The next exact task is to guard
the 2,250 motif rows by assumptions, extract and minimize a sufficient UNSAT
core, and identify its Hall/packet structure—or change the resident endpoint.

That higher-order obstruction is now explicit.  A nine-row real-linear
certificate for the first endpoint combines one newly created length-two
motif with four lower/degree rows and four upper/degree rows; its weighted sum
is literally `0 <= -1`.  It is inclusion-minimal within those nine rows:

```text
scratch/k16_zero_unit_nine_row_packet_obstruction_20260729.audit.json
```

The radius-four catalogue actually contains three score-`(0,0,0,*,4)`
endpoints.  The other two avoid that newly created lock, but exhaustive
solver-free failed-literal propagation refutes both: each has 93 variables
whose two Boolean branches contradict the exact degree, both-`q1`, and motif
rows.  More sharply, all three share the *same single inherited motif* with
physical closure

```text
{(62050,64034),(62514,63538),(63538,64034)}
coordinate 11, length 2.
```

That motif plus eight fixed palette/degree rows has an inclusion-minimal
real-linear certificate: four rows sum to `x <= 0`, the other five to
`-2x <= -1`, and twice the first packet plus the second is `0 <= -1`.
The same named nine rows replay against all three endpoints:

```text
scratch/k16_three_zero_unit_candidates_common_affine_core_20260729.audit.json
MATH_THEOREM_K16_DOUBLE_FAN_AFFINE_HALL_OBSTRUCTION_20260729.md
```

The complete packet replay is stronger.  Candidates 1 and 2 have fourteen
distinct inherited motifs which are each individually impossible against the
hard degree-plus-both-q1 rows.  Candidate 0 has thirteen of those transported
locks plus its independent motif-82 lock.  A motif-disjoint serial packet on
the coordinate-8 and coordinate-14 occurrences forces one additional hole.
Hence, for the three fixed overlays,

\[
                         \Delta_R(Q_i)\ge15\qquad(i=0,1,2).
\]

This is the exact circuit-packing lower bound on inherited deficiency, not a
failed-literal count:

```text
scratch/k16_three_zero_endpoints_singleton_packet_packing_20260729.audit.json
MATH_AUDIT_K_K16_SINGLETON_PACKET_PACKING_AND_SMALL_TRADE_SCOPE_20260729.md
```

Thus the correct next local potential is the full failed-literal/affine-core
bank, not peeled unit-core count.  Future exact-`q1` trades must hit this
closure or change one of its eight palette/degree support rows.  Candidate 0
also contains the separate newly created motif-82 affine lock above.

That potential now gives a strict descent chain.  Targeted q1-cover-preserving packets
preserve both immediate-shadow palettes while full solver-free failed-literal
replay decreases the obstruction bank

\[
93\to86\to81\to78\to76\to73\to69\to56\to48\to39\to34\to30\to27\to19\to15\to12\to9\to7\to5\to3.
\]

The current endpoint has 2,222 short motifs, three components, zero unit
cores/static blockers, and zero lower or upper `q1` holes:

```text
scratch/k16_q1_endpoint_resume1_failedlit3_20260729.json
SHA-256 430fa828587fd793a908cb5c379be6c5686dc5bb473657fe2b5af10ca037481a
scratch/k16_failedlit3_fullbank_20260729.audit.json
SHA-256 e292d250dbfca0331fb74b12d8cc7e69770ea101c8a9f9b890289e5d1db2bd94
scratch/k16_candidate1_affine_to_failedlit81_chain_20260729.audit.json
SHA-256 6a1442ccb502d1d57aacce4031f292a7e99f16ef3f96208eb5fa3245e54d26c5
scratch/k16_failedlit81_to73_chain_20260729.audit.json
SHA-256 d0e68f183828697216ba4627afdc42ca579f0f630c27a59ef695175d78182241
```

A complementary, fully explicit three-C6 path targets the two inherited
serial motifs and the common packet support.  It preserves both q1 supports
and gives `93->87->84->82`; its final state has three components and 2,253
short motifs.  This is detector descent, not a proved decrease of
`Delta_R`:

```text
scratch/k16_candidate1_abc_failed_literal_descent_20260729.audit.json
```

The endpoint is still certified infeasible: 3 exact double-failure
contradictions remain.  The result proves that the higher-order bank is
movable by exact packet trades and supplies a concrete iterative lane, but
not yet a resident/all-depth factor.

At the intermediate `fl73` snapshot the failed proofs were not uniformly
supported.  Counting each physical blue edge at most once per failed
variable, five edges occurred in 16 of the 73 two-branch proofs:

```text
(34546,42736)  (41203,57523)  (41395,41401)
(42736,44752)  (57523,58515)
```

Four more occur in 14 proofs:

```text
(41811,45395)  (44307,46355)  (45395,46355)  (51562,57706)
```

This does not make the potential monotone—trades can create new proofs—but it
gives a second, global packet target complementary to chasing only the
smallest surviving proof.

### Strict-token core chase: exact two-cycle trap

The full circulation after the first strict-token (C_6) is no longer open:
it is solver-free infeasible.  Its translated core has motif closure

```text
(37531,37785), (37531,41627), (41627,41657)
```

and a conditional lower-colour replacement `(33467,49819)`.  The two selected
source edges at socket `49819`, namely `(49819,53787)` and `(49819,49881)`,
are protected by unique q1 rows, so degree balance forbids that replacement.
The other two motif edges are also protected, and the closure cannot be hit.

A second exact strict-token (C_6) deletes

```text
(41147,57499), (41627,41657), (57529,58009)
```

and adds

```text
(41147,41627), (41657,58009), (57499,57529).
```

Both shores have lower token multiset `{41115,41625,57497}` and upper token
multiset `{41659,57531,58041}`.  It breaks that motif, preserves every q1
load exactly, and yields another four-component q1-perfect factor.  Its full
overlay is again solver-free infeasible: the new motif closure is

```text
(37051,41147), (37531,41627), (41147,41627)
```

and it is tied to the same locked socket `49819`.

The current core has no strict-token alternating (C_4) through any of its
five blue edges (53 raw squares total).  Among all 2,034 alternating (C_6)
candidates through those five edges, exactly one preserves both token
multisets: it is the inverse of the second (C_6), returning to the previous
factor.  Thus direct radius-at-most-three strict-token core chasing is trapped
in a two-cycle.  The first unclosed local move is a non-inverse strict-token
(C_8), a controlled non-strict q1-slack move, or a simultaneous change of
the resident endpoint which releases the socket.  The radius-four search was
not launched after the H100 resource moratorium.

Full theorem and replay:

```text
MATH_THEOREM_H_K16_STRICT_TOKEN_C6_PORTAL_CHAIN_AND_TRAP_20260729.md
scratch/audit_k16_strict_token_c6_chain_trap_20260729.py
scratch/k16_strict_token_c6_chain_trap_20260729.audit.json
```

## Detector zero reached; exact overlay exposes one higher-order lock

Targeted both-q1-preserving packets continued the certified failed-literal
descent

\[
93\to86\to81\to78\to76\to73\to69\to56\to48\to39\to34\to30
\to27\to19\to15\to12\to9\to7\to5\to3\to2\to0.
\]

At the FL2 endpoint, each of the two remaining contradictions could be
removed individually by a radius-two/three packet.  The two best packets are
compatible.  Their composition has both physical q1 palettes complete, zero
unit cores, zero static blockers, and zero double failures among all `954`
full-bank probes:

```text
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
SHA-256 17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8

scratch/k16_failedlit0_fullbank_20260729.audit.json
SHA-256 703d44d0e949094a6bc37ed0a44b1a3caca2af74fda24cf0908c84a98246976d
```

This closes the first-order detector, not the physical problem.  The exact
degree-plus-both-q1-plus-all-initial-motifs overlay returned `INFEASIBLE` at
round zero in `1.59` seconds.  It has `12,479` red and `12,479` blue variables,
`391` fixed common edges, and `2,222` distinct motif rows:

```text
scratch/k16_failedlit0_exact_overlay_20260729.json
SHA-256 4fd0b2d2a15326b9ecfa5c1b939f835814ca2d5303268268ad1ea639e33fdcf2
```

Guarding every q1 and motif row yields a deletion-minimal `22`-assumption
core with no unknown replay: `8` lower-q1 rows, `13` upper-q1 rows, and one
length-two motif.  The sole motif is coordinate `2`, start `8107`, with
closure

```text
(57902,57998), (57902,61994), (57998,58250).
```

All `21` palette rows have base load one.  The core is

```text
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json
SHA-256 2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238
```

The solver-free mixed-Hall/Farkas explanation is now complete.  The 21 rows
and nine sockets force all three closure-deletion variables to zero already
over the nonnegative reals.  For a new Johnson edge `e`, the exact branch
certificate drift is

```text
kappa_j(e) = number of its endpoints in branch sockets
             - number of guarded branch colours it supplies.
```

Among 699 absent relevant providers the helpful counts are 420/229/85.  A
complete two-new-edge C4 audit finds 11 guarded-core-safe portals and exactly
one portal preserving both full physical q1 palettes:

```text
del (57902,61994),(25135,29230)
add (25135,57902),(29230,61994).
```

It destroys motif 390 but creates one new coordinate-9 length-three motif;
the total remains 2,222, while `sum_(short M)(4-length(M))` drops by one.
Therefore the two-outside-edge C4 portal class is closed exactly; this is not
a global lower bound for longer alternating circuits.  The exact next target
is a second full-q1 portal on the transported
length-three defect, with annihilation or extension to length four; no
repeatability is claimed.  Full theorem:

```text
MATH_THEOREM_K_K16_FL0_MOTIF390_FARKAS_LOCK_AND_MINIMAL_CERTIFICATE_EXPANSION_20260729.md
```

There is also an exact finite-catalogue boundary.  Allowing an arbitrary
spanning 2-factor from `Q union R` plus every changed edge in the three
radius-two/three packet reports still returns first-round `INFEASIBLE`
(`25,530` candidate edges).  Hence merely recombining all currently known
small packets cannot finish residence; a radius-four/new edge or a different
parent is necessary.  Scope and artifacts are frozen in

```text
MATH_AUDIT_K16_FL2_AUGMENTED_CATALOGUE_NO_GO_20260729.md
scratch/solve_k16_q1_augmented_catalogue_residence_cegar_20260729.py
scratch/k16_fl2_augmented_allr23_cegar_20260729.json
```

## The higher-order lock is now solver-free; radius three is still insufficient

The `22`-row motif-390 obstruction above has a complete solver-free branch
proof.  Its three closure alternatives are the blue variables

```text
b11795 = (57902,57998)
b11796 = (57902,61994)
b11821 = (57998,58250).
```

The `b11796=1` and `b11821=1` branches collapse through explicit `13`-row
and `4`-row unit-propagation certificates.  For the remaining branch, an
integer Farkas identity formed from `17` q1 inequalities and `8` degree
equalities yields

```text
b11795 + (six nonnegative red-add variables) <= 0,
```

so `b11795=0`.  Motif 390 requires at least one of the three variables, a
contradiction.  The active affine socket uses `33` variables/edges on `40`
physical vertices.  The proof and independent replay are frozen in

```text
MATH_AUDIT_K16_FAILEDLIT0_GUARDED_MOTIF390_SOLVER_FREE_CORE_20260729.md
scratch/k16_failedlit0_motif390_branch_cores_20260729.audit.json
scratch/k16_failedlit0_b11795_affine_core_20260729.audit.json
```

Expanding the exact 2-factor model to every Johnson edge within three star
steps of the guarded q1-provider set gives `330,628` candidate edges, about
`80%` of all `411,840` edges of `J(16,8)`.  The model is still
first-round `INFEASIBLE` with all `2,222` necessary initial motif-closure
rows.  This is no longer a small-packet failure: any PBBS escape must cross a
larger global socket.  Frozen result:

```text
scratch/k16_failedlit0_corestar3_augmented_cegar_20260729.json
SHA-256 4ae0ab6a00b006cbbd87ce845e3ccfe03ac486306dd6c10e40970af0c5dc5108
```

A depth-four provider expansion contains `407,410` edges (`98.9%` of the
full Johnson graph); after union with the fixed inputs, the exact catalogue
has `407,675` edges.  Its first `300`-second solve returned `UNKNOWN`, using
about `5.8 GiB` under a `12 GiB` hard cap.  This is neither infeasibility nor
a proof.  An eight-worker retry hit the address-space guard (`std::bad_alloc`,
peak RSS about `8.46 GiB`) and is recorded only as `RESOURCE_LIMIT`; the
redundant objective-bearing retry was later stopped in favour of the complete
static and feasibility-only models below.

```text
scratch/k16_failedlit0_corestar4_augmented_cegar_20260729.json
SHA-256 97bc3abd8ad3995ceda87e3b9471d16f791eda02c2c3ed59bfdaed0a89527510
```

The star expansion becomes essentially and then literally unrestricted:

```text
depth 5: 411,836 / 411,840 Johnson edges
depth 6: 411,840 / 411,840 Johnson edges
```

The original finite-catalogue model minimized symmetric difference from the
q1 seed.  That objective is irrelevant for an unrestricted existence test
and can delay the first feasible factor, so the solver now has a
provenance-recorded `--feasibility-only` mode.  A full-`J(16,8)` feasibility
CEGAR lane with all degree, both-q1, and initial necessary motif rows hard
returned `UNKNOWN` in its first 1,800-second round under four workers and a
16-GiB guard.  An objective-bearing version returned the same `UNKNOWN`
status.  Peak RSS was about 4.1 and 6.8 GiB respectively, so these are
time-limited results, not memory failures and not proofs.

```text
scratch/k16_fulljohnson_feasibility_cegar_20260729.json
SHA-256 c1fb5dad47f7b22e743ce0b047a0318b0e0bc12a9c9018040229bc2fd81ad510

scratch/k16_fulljohnson_initialmotif_cegar_20260729.json
SHA-256 4bfcb6616fdeb6b40c7f5e1dd965d0b41c47922eb8e6cba4dd7e715ccf368187
```

A feasible round would be audited literally and every newly created short
run would become another sound cut.  Only `PASS` would produce a resident,
both-q1-complete factor.  It would still need the deeper-shadow and
lower-compiler audits before becoming a word.  `INFEASIBLE` at any round
would close this unrestricted factor subproblem, not disprove
`nu(16)=12873`; `UNKNOWN` remains inconclusive.

## The motif-390 core is exactly a rank-two mixed-Hall cut

The guarded `22`-row core now has a strictly stronger solver-free
explanation than the branch/affine proof above.  Give weight two to

```text
L47652,L61988,U47645,U47676,U47772,U62118,U64044,U65060,
```

weight one to the other thirteen guarded q1 colours, endpoint weight two at

```text
47644,47660,61990,64036,
```

and endpoint weight one at

```text
26718,59422,59942,59918,58126.
```

All 12,479 resident-only red seams satisfy the exact mixed column inequality

```text
lambda_lower + lambda_upper <= w_left + w_right.
```

Exactly twelve have nonzero price and all twelve are tight.  Expanding the
Hall row in the blue deletion variables cancels every coefficient except

```text
b11795+b11796+b11821 <= 0.
```

Motif 390 requires the same sum to be at least one.  Hence the core is
fractionally infeasible with integer margin one; no integrality, upper-bound,
or branch argument is needed.  The proof uses all 21 guarded q1 rows and only
nine endpoint sockets.  A permanent standard-library verifier replays every
one of the 12,479 red columns.

Two literal q1-perfect radius-two moves cross this precise certificate:

```text
delete (25662,27678),(25694,25722)
add    (25662,25722),(25694,27678)   [U27742 load 1 -> 2]

delete (57487,57615),(57550,57742)
add    (57487,57550),(57615,57742)   [L57614 load 1 -> 2].
```

Each preserves physical degree two and leaves both q1 palettes hole-free;
each removes one zero-provider anchor from the Hall proof.  They are exact
certificate escapes, not residence solutions.  Full theorem and replay:

```text
MATH_THEOREM_L_K16_FAILEDLIT0_MIXED_HALL_CORE_AND_ESCAPE_20260729.md
scratch/audit_k16_failedlit0_mixed_hall_farkas_20260729.py
scratch/k16_failedlit0_mixed_hall_farkas_20260729.audit.json.
```

The two certificate-breaking moves have now been materialized independently,
as has their four-edge composition.  All three remain literal spanning
2-factors with zero lower/upper q1 holes.  They do **not** reduce the global
residence burden: their short-run counts are `2224`, `2222`, and `2224`.
More importantly, rebuilding the complete fixed `R`/escaped-`Q` overlay and
solving it exactly returns first-round `INFEASIBLE` for each endpoint.  Thus
the mixed-Hall row was a real obstruction but not the only one; invalidating
one sparse dual certificate is insufficient.

```text
scratch/k16_failedlit0_mixed_hall_escape_materialization_20260729.audit.json

single U27742 escape overlay:       SHA-256 6e6a85ff2bbce6cd16d5a5902effec07eca8e17dfc214bbfb49c99a88b31ffcf
single L57614 escape overlay:       SHA-256 07c953f2aaabcd27629d1e6ece1a7e1a069b0f3867a2df463825e1dbf070fdb6
composed escape overlay:            SHA-256 101240249dcc0bf4cdc4c14e28474250a72b6845640cdd37382b1c9a470844da
```

A guarded-core extraction on the composed endpoint is running to identify
the successor mixed-Hall row rather than treating these three no-go results
as opaque solver statuses.

That extraction is now complete.  The composed endpoint has a new
deletion-minimal `19`-row core: `10` lower-q1 rows, `8` upper-q1 rows, and
one length-two motif.  Every one of the nineteen `18`-row deletion replays is
`OPTIMAL`; there are no `UNKNOWN` replays.  The successor motif is coordinate
`5`, start `7706`, with closure

```text
(64036,64040), (64036,65028), (64040,64264).
```

```text
scratch/k16_mixed_hall_escape_both_guarded_core_20260729.json
SHA-256 285063a11c1894f3420fe442a7c3d2f6cb16138ab8ff8fbd1b5980569ddad6a6
```

Thus the dual obstruction moves rather than disappears.  The two singleton
branches sharpen this further.  The `L57614` two-edge escape alone already
reaches a deletion-minimal `19`-row core with the same successor motif as the
four-edge composition, whereas the `U27742` escape leaves a larger `23`-row
core with two motifs.  Every deletion replay is `OPTIMAL`; none is
`UNKNOWN`.  Therefore the `L57614` branch dominates the composed branch for
the next dual iteration.

```text
scratch/k16_mixed_hall_escape_l57614_guarded_core_20260729.json
SHA-256 60c01989449f066e5daa943fda7282e637a5bfba3250d89b174918455692bf96

scratch/k16_mixed_hall_escape_u27742_guarded_core_20260729.json
SHA-256 996514c394b46c7ae6a81df49b1821a473a97efe79b3ee6552148a183f0d519b
```

Derivation of the `L57614` successor sparse mixed-Hall row and its smallest
q1-safe escape is assigned; no claim is made that this iterative certificate
chain terminates.

## Universal residence rows and the complete static model

The motif rows used above are not merely valid inside a Q/R overlay.  If a
short run of a source factor has bordered path

\[
v_0v_1,v_1v_2,\ldots,v_\ell v_{\ell+1},\qquad 1\le\ell\le3,
\]

then every residence-at-least-four spanning 2-factor on the entire Johnson
graph must omit at least one of those edges.  Otherwise degree two exhausts
every interior vertex and forces the same short run.  This solver-free lemma
justifies using all `2,222` Q0 rows in the unrestricted full-graph model.
The exact star census and proof are in

```text
MATH_AUDIT_K16_PBBS_STAR_DEPTH_AND_UNIVERSAL_RESIDENCE_CUTS_20260729.md
```

There is now also a complete non-CEGAR residence encoding.  Orient every
factor component.  At vertex `v`, track the coordinates inserted on the last
three incoming transitions.  A positive coordinate run has length at least
four exactly when the outgoing deletion coordinate differs from all three.
This gives the full `J(16,8)` model

```text
411,840 undirected edge variables
823,680 directed arc variables
64,350 history/predecessor integers
1,299,870 total variables
576,292 high-level constraints
```

with no motif rows.  Exhaustive `J(4,2)` regression and both authoritative
K16 factors replay exactly.  A sound `S_16` break fixes one oriented edge and
one of three predecessor orbits.  The first full static solve exhausted its
16-GiB address-space cap after 185 seconds (`std::bad_alloc`, peak RSS 13.98
GiB).  This is `RESOURCE_LIMIT`, not `UNSAT`.  An otherwise identical
two-worker solve is running with an OS-enforced 32-GiB cap and a 1,800-second
solver limit; there is no SAT/UNSAT verdict yet.

```text
MATH_THEOREM_K16_DIRECTED_HISTORY_STATIC_RESIDENCE_20260729.md
```

## Complement doubling reduces one sufficient K16 subclass to RTR(7,4)

Let `G` be a spanning 2-factor of `J(15,7)` covering every rank-six
intersection and every rank-eight union.  If all one-runs, zero-runs, and
components of `G` have length at least four, then placing `G` on the shore
containing the new coordinate and its set-complement on the other shore
produces a resident, both-q1-complete factor of `J(16,8)`.  This is exact for
the no-cross complement-doubled subclass, not WLOG for arbitrary K16 factors.

The odd factor is encoded by one turn-selector map

\[
p:\binom{[15]}8\to\binom{[15]}2,\qquad p(U)\subset U,
\]

with exact degree rows, lower-turn surjectivity, and the two-sided residence
law.  The missing statement is the finite **resident turn-rainbow lemma
`RTR(7,4)`**.  First-moment identities give forced mean one/zero run lengths
`7/8`, so there is no boundary-supply obstruction; the problem is arranging
the runs while preserving turn colours.

```text
MATH_THEOREM_K16_BIRESIDENT_COMPLEMENT_DOUBLE_AND_TURN_SELECTOR_20260729.md
```

A compact exact quotient/CNF attack on `RTR(7,4)` is being built separately
from the unrestricted K16 searches.
