# Integrated exact search for `k=11`, nonzero length `465`

## 1. Outcome of this integration pass

The best recoverable fixed-delay object is genuinely very close to a complete
solution, but the remaining defect is not a one-move defect.

The current central row is

```text
k11_lower956_upper549.txt
```

and its exact factor is

```text
k11_upper549_natural_array.txt
```

The factor has length `465` and covers `2034/2047` nonzero masks.  Its only
missing masks are

```text
251 493 607 941 956 958 1267 1468 1694 1763 1884 1946 1990
```

Here `958` has rank eight; the other twelve masks have rank seven.  Every mask
of ranks `1,...,6` and `9,...,11` is already covered.

A twelve-entry append that uses the old/new seam gives the independently
verified 477-entry nonzero word `k11_completed_477.txt`.  Hence the current
global upper bound is `nu(11)<=477` (`N(11)<=478`).  The exact search below
still targets length 465; this completion does not settle optimality.  The
append is optimal only for this fixed 465-entry prefix, because its twelve
missing rank-seven masks require twelve distinct new right endpoints.

All invariant-preserving reversal and three-edge-relocation neighborhoods used
so far have been exhausted without improving the upper score.  More
importantly, an audit exposed and corrected an invalid endpoint/first-edge
normalization in the first distance models.  The corrected no-canonical
distance-at-most-19 formula is UNSAT and now has an independently regenerated,
independently checked DRAT certificate.  Thus every degree-two central repair
having distinct rank-five colours, every rank-seven colour, and endpoint
access to the omitted rank-five colour must replace at least **twenty** of
the seed's 461 real Johnson edges.  This is stronger than a Hamilton-path
statement because disconnected cycle covers were allowed.

This is still a promising search target.  Full ordered models and
target-closure searches continue remotely.  No solution or global
impossibility result is claimed: the certificate is a radius-19 central-colour
exclusion around one seed, not an unrestricted length-465 refutation.

## 2. Problem and lower bound

Let `nu(k)` be the minimum length required to realize every nonempty mask.
For `k=11`,

```text
binom(11,5)=binom(11,6)=462,
B(11)=462+3=465.
```

Therefore a verified length-465 nonzero array would immediately prove

```text
nu(11)=465,
N(11)=466
```

for the original problem including zero.

The fixed central-row ansatz is

```text
T_i=A_i OR A_(i+1) OR A_(i+2) OR A_(i+3),
1 <= i <= 462.
```

It is a sufficient route to equality, not a necessary normal form.  Its
arithmetic defect is `sigma=369`, so failure or UNSAT of this ansatz would not
prove `nu(11)>465`.

## 3. Independently checked strongest checkpoint

For `k11_lower956_upper549.txt`:

```text
central rank 6: 462/462
rank-5 adjacent intersections: 461/462, missing 31
rank-4 triple intersections: 330/330
rank-3 quadruple intersections: 165/165
coordinate run deficit for delay 3: 0
rank-7 adjacent unions: 318/330
rank-8 triple unions: 164/165
ranks 9,10,11: complete
```

The omitted rank-five mask `31` is available through the truncated factor
window at the endpoint.  The central row is a permutation of all rank-six
masks and every consecutive pair is a Johnson edge.

For `k11_upper549_natural_array.txt`, exhaustive interval enumeration gives

```text
length=465 covered=2034 required=2047
rank 1:  11 at length 1
rank 2:  55 at length 1
rank 3: 165 at length 1
rank 4: 330 at length 2
rank 5:   1 at length 2, 461 at length 3
rank 6: 462 at length 4
rank 7: 318 at length 5
rank 8: 164 at length 6
rank 9:  55 at length 7
rank 10: 11 at length 8
rank 11:  1 at length 9
```

Every array entry has rank at most three.  Across 465 positions the entry-rank
distribution is

```text
rank 1: 75 occurrences, 11 distinct
rank 2: 215 occurrences, 55 distinct
rank 3: 175 occurrences, 165 distinct.
```

The central derivative `D^3 A` contains all 462 rank-six masks exactly once.
The factor is a sparse shrinking of the maximal intersection envelopes; only
173 of its 465 entries equal their maximal envelope.

SHA-256:

```text
f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477  k11_lower956_upper549.txt
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd  k11_upper549_natural_array.txt
```

The remote artifact audit found no stronger length-465 partial factor.  The
newer `k11_pair_repaired.txt` has substantially worse shadow scores.  Reductions of
the exact k=12 array give universal k=11 arrays of length at least 583, and do
not improve the verified upper bound 477.

## 4. Exact fixed-row constraints

The fixed-row search should use the following gates in this order.

### 4.1 Johnson path and the two edge colours

Each selected Johnson edge has a unique representation

```text
(C,U),  |C|=5, |U|=7, C subset U,
```

and joins the two rank-six sets strictly between `C` and `U`.  Thus its lower
colour is its endpoint intersection `C`, and its upper colour is its endpoint
union `U`.

There are

```text
462 rank-five colours, each incident with 15 Johnson edges;
330 rank-seven colours, each incident with 21 Johnson edges;
6930 Johnson edges in J(11,6).
```

After WLOG symmetry normalization, colour `31` is omitted, the path begins
`63,119`, and every other rank-five colour occurs exactly once.  Every
rank-seven colour must occur at least once.  The selected graph plus the dummy
endpoint vertex must be one Hamilton cycle, equivalently a Hamilton path on
the 462 real vertices.

### 4.2 First deeper shadows

At each internal rank-six vertex, the two incident selected edges determine
simultaneously

```text
the intersection of three consecutive central vertices (rank 4),
the union of three consecutive central vertices (rank 8).
```

Pair-of-incident-edge variables therefore enforce all 330 rank-four and all
165 rank-eight targets with one shared local encoding.  Four-vertex path
variables similarly enforce all 165 rank-three and all 55 rank-nine targets.
Ranks 10 and 11 are checked lazily; they are already highly redundant in the
seed.

The rank-four/rank-eight pair gate now uses an exact grouped encoding rather
than one variable for every explicit pair of incident edges.  At a possible
rank-eight centre `T`, the twelve relevant incident edges split into two
six-edge groups according to which of the two missing target bits is added;
the triple union is the target exactly when one selected edge comes from each
group.  The rank-four intersection gate is the dual five-by-five statement.
Three variables per centre encode the two group ORs and their conjunction.
For target `958` this reduces `1008` witness variables and `3025` clauses to
`84` variables and `477` clauses.  If all rank-four and rank-eight gates are
materialized, it saves `166320` variables and `420420` clauses.  This is a
logical equivalence, not a relaxation; the proof and independent checker are
in `K11_COMPACT_PAIR_SHADOWS.md` and its audit.

The rank-three/rank-nine four-path gate now has an even smaller exact
projected encoding.  Fixing the middle Johnson edge leaves two excess or
missing coordinates and exactly two ways to assign them to the two outer
edges.  One existential flag per assignment needs only three implications:
the middle edge is selected and a suitable outer edge is selected at each
endpoint.  The target clause ORs these flags; reverse Tseitin implications
are unnecessary after existential projection.  A rank-three target falls
from `21000` explicit witnesses and `84001` clauses to `840` flags and `2521`
clauses; a rank-nine target falls from `54432/217729` to `1512/4537`.  If both
layers are materialized, the replacement uses `221760` variables and
`665500` clauses, versus `5765760` variables and `23063260` clauses in the
old shared up-front four-path block.  The exact proof, sparse-graph argument,
independent audit, and exhaustive checker are in
`K11_COMPACT_FOUR_SHADOWS.md` and `K11_COMPACT_FOUR_SHADOWS_AUDIT.md`.  Enable it with
`RECOMBINE_COMPACT_FOUR_SHADOWS=1`; lazy rank-three/rank-nine cuts use the
same gate on demand.

### 4.3 Exact factorability

A central row factors as `T=D^3 A` if and only if every internal 1-run in each
coordinate incidence word of `T` has length at least four.  Runs touching an
endpoint may be shorter.  Lazy blocking of an observed bad run needs only the
two to four selected path edges surrounding that run.

### 4.4 Exact lower pinning

For a fixed path define

```text
E_j = intersection of all T_i whose central four-window contains j.
```

Every factor has `A_j subset E_j`.  If a lower target `S` is assigned to a
short physical interval `J_S`, define for each bit `b`

```text
Z_b = {j : b in E_j} minus union{J_S : b not in S}.
```

The assignments and the central row are simultaneously realizable exactly
when

```text
J_S intersects Z_b       for every b in S,
[i,i+3] intersects Z_b   for every b in T_i.
```

This pin-survival test is stronger than envelope containment or an ordinary
Hall matching.  A candidate path must be passed through it before it is called
labelable.

The natural grading used by the current successful factor has exact selector
counts

```text
ranks 1--3, singleton slots:  (11+55+165)*465 = 107415
rank 4, adjacent-pair slots:  330*464         = 153120
rank 5, triple slots:         462*463         = 213906
total selectors:                                474441
factor bit variables:                             5115
total variables:                                479556.
```

This is the cheapest first label gate.  If it is UNSAT, the complete flexible
short-interval label model must still be tried; for this instance it has
`1,062,204` variables and `16,560,867` clauses.  Natural grading is a
sufficient ansatz, not a theorem about every factor.

## 5. The twelve-colour repair calculation

The score-549 path misses twelve rank-seven colours.  A selected edge for a
rank-five colour `C` can be changed to upper colour `U` exactly when `C subset
U`.  If its old upper colour occurs more than once, this reassignment does not
destroy existing rank-seven coverage.

`k11_rank7_repair_flow.cpp` solves this capacitated matching problem.  It finds
a safe assignment for all twelve missing colours:

| missing `U` | donor lower colour `C` | displaced upper colour | old multiplicity |
|---:|---:|---:|---:|
| 251 | 59 | 379 | 2 |
| 493 | 109 | 877 | 2 |
| 607 | 79 | 127 | 2 |
| 941 | 173 | 1199 | 2 |
| 956 | 188 | 508 | 3 |
| 1267 | 115 | 631 | 2 |
| 1468 | 316 | 319 | 2 |
| 1694 | 654 | 702 | 2 |
| 1763 | 227 | 499 | 2 |
| 1884 | 604 | 892 | 2 |
| 1946 | 666 | 734 | 2 |
| 1990 | 454 | 974 | 3 |

This proves that the upper-colour incidence layer alone has repair distance
exactly twelve.  It does **not** preserve degrees, connectivity, lower deeper
shadows, or factorability.  The assignment is now supplied to the exact
solver as a phase hint through

```text
RECOMBINE_PHASE_REPAIRS=k11_rank7_flow_phase.txt
```

and never changes the feasible set.

## 6. Proof-certified distance at least seventeen

The first full-graph distance runs were invalid as global distance claims:
they retained a canonical omitted-colour, endpoint, and first-edge
normalization.  That normalization is WLOG for unrestricted existence but not
relative to distance from one fixed seed.  The source now requires
`near_limit<0` before activating it.

The corrected model uses the complete 6930-edge graph and leaves the omitted
rank-five colour, both endpoints, orientation, first edge, and bit labels
free.  At distance at most 16, the exact extra-upper-colour support encoding
has

```text
45984 variables and 163030 clauses.
```

Kissat returned

```text
UNSAT
```

and `drat-trim` independently returned `s VERIFIED`.  The formula requires
only:

```text
degree two at every real vertex and at the dummy;
461 distinct rank-five intersection colours;
all rank-seven colours at least once;
endpoint access to whichever rank-five colour is omitted;
at most seventeen dropped seed real edges.
```

Every real vertex and the dummy have degree exactly two, but connectivity is
not required.  Hence even a disconnected cycle cover cannot satisfy these
colour conditions within seventeen changes.  Any qualifying Hamilton path
must drop at least eighteen seed edges, or have real-edge symmetric difference
at least 36.

The frozen source regenerated the archived formula byte-for-byte on a second
RunPod, and the proof was independently rechecked there.  Full artifacts and
scope audits are in `scratch/certificates/k11_distance16/`,
`scratch/certificates/k11_distance17/`, `K11_DISTANCE15_AUDIT.md`,
`K11_DISTANCE16_AUDIT.md`, and `K11_DISTANCE17_AUDIT.md`.

A compact exact support decomposition explains the strong propagation.  The
twelve missing rank-seven colours require twelve new edges.  At distance at
most `12+q`, at most `q` further new edges exist, so their upper colours have
support at most `q`.  Selector variables encode that support directly while
the ordinary distance counter retains exact multiplicities.  For distance 17
the cap is five.  Equivalently, every fixed support case exposes only

```text
the 461 seed edges and all edges whose upper colour is one of the twelve
missing colours or one of at most five extra colours.
```

The selector formulation represents all support cases in one proof-producing
CNF; it is redundant with, and does not restrict beyond, the distance bound.

The next shell is now certified as well.  The corrected no-canonical
distance-at-most-19 relaxation has 48,357 variables and 167,764 clauses.
Its independently regenerated CNF is byte-identical to the producer formula,
and `drat-trim` reports `s VERIFIED` with exit code zero against the
4,723,026,902-byte proof.  Thus even a disconnected qualifying degree-two
cover must drop at least twenty seed edges; every qualifying Hamilton path has
real-edge symmetric difference at least 40.  Exact hashes and scope are in
`K11_DISTANCE19_CERTIFICATE_PROMOTION.md` and `K11_DISTANCE19_AUDIT.md`.

### Exact canonical-prefix decomposition

After fixing the omitted colour, first endpoint, and first real edge, the
factorable ordered search has four second-edge orbits and then 15 total
third-edge orbits.  Fixing one more transition leaves exactly 15 legal labelled
choices in every third-edge branch: the coordinates introduced on the first
three transitions are unavailable for removal by the delay-three cooldown.
The residual prefix stabilizers reduce the resulting 225 labelled choices to
60 exhaustive fourth-edge branches.  The exact table and two independent
derivations are in `K11_FOURTH_EDGE_ORBITS.md` and its audit.

For every nonomitted lower colour forced by this prefix, the six containing
rank-six vertices satisfy the exact flag moment

```text
selected real cut edges + selected dummy endpoint incidences = 10.
```

`RECOMBINE_PREFIX_MOMENTS=1` adds these cheap redundant counters; it composes
with the omitted-colour exact-12 moment.  The orbit options are guarded by an
actual factorability check: pure base/shadow modes are intentionally rejected,
because the cooldown classification would not be exhaustive for those larger
relaxations.

There is an upper-colour analogue.  For every distinct forced rank-seven
prefix colour `U`, summing degrees on its seven rank-six subsets gives

```text
2 * selected internal-U edges
  + selected real cut edges
  + selected dummy endpoint incidences = 14.
```

`RECOMBINE_PREFIX_UPPER_MOMENTS=1` encodes this exact weighted equality over
217 literal occurrences.  It is independent of the lower moments and has been
checked against the canonicalized score-549 seed.  A fifth-edge orbit census
would split the 60 jobs into 464 branches; it is documented but deliberately
not used because these global moments offer substantially more propagation per
portfolio process.

## 7. Searches currently running

The following searches were launched on the remote Pod; none runs on the Mac.

### Exhaustive canonical fourth-edge queue

All 60 certified `(second,third,fourth)` orbit triples are covered by a
deterministic 15-parent queue.  Every child uses the complete ordered Johnson
graph, exact lazy delay-three factorability, seed distance at least 19, target
958, the omitted-colour exact-12 moment, all forced lower-prefix exact-10
moments, every deduplicated upper-prefix exact-14 weighted moment, and both
compact pair- and four-shadow gates.  Initial formula sizes are now `95,754`,
`101,739`, or `107,724` variables,
depending on the number of prefix moments.  Before the compact rank-eight
gate, the corresponding smallest branch had `96,678` variables.  The exact branch/seed
mapping is frozen in `scratch/k11_fourth_queue/BRANCH_MANIFEST.tsv`.

The queues were safely archived and restarted after the compact four-shadow
gate landed.  No interrupted child had returned a candidate, `UNSAT`, or an
ordinary exit status.  All fifteen live processes expose both compact flags
and the five-million-variable reserve; the rank-three/rank-nine savings occur
when the exact lazy loop discovers a missing depth-three shadow.

The lazy user-variable reserve is five million.  A first launch used 1.5
million and five `u=0` children aborted with CaDiCaL status 134 when newly
learned rank-3/rank-9 witnesses crossed variable 1,500,000.  Those executions
were correctly classified as infrastructure failures, never as UNSAT; their
logs were archived and every queue restarted from an unsearched child.  The
wrapper now treats status 134 as retry-required and all live environments were
checked to contain the five-million reserve.

This queue is exhaustive only for the factorable fixed-row ansatz after the
proved WLOG canonicalization.  A proof-producing distance-at-most-19 relaxation
and an independent distance-19 solve run separately and are not interrupted by
the branch portfolio.  No path candidate has yet been emitted.

### Larger corrected distance shells, complete Johnson graph

```text
./recombine_paths_integrated ... allinc17
./recombine_paths_integrated ... allinc18
./recombine_paths_integrated ... allinc19
```

These models suppress all bit-symmetry normalization tied to a particular
endpoint and use exact extra-colour support caps five, six, and seven.

An independent seed uses the twelve-colour max-flow repair as SAT phases.
When a base solver finds a model, the executable adds exact lazy cuts for
connectivity, short coordinate runs, and every missing deeper shadow.

### Target-closure ordered hybrid

```text
./recombine_paths_integrated ... targetordhybrid
```

This restricted but much more strongly propagated search has

```text
4639 candidate real edges
138358 variables after ordered connectivity and pair-shadow gates.
```

It exposes all alternatives for missing or singleton rank-seven colours and
for the missing rank-eight colour.  It is exact inside that target closure,
not globally exact over all fixed rows.

### Full ordered hybrid portfolio

The unrestricted ordered model should be run with several seeds.  It uses a
binary position label for every rank-six vertex, so disconnected subtours are
impossible in the first SAT call.  The correct order of gates is

```text
rank-5 rainbow + rank-7 complete
-> Hamilton order
-> rank-4 and rank-8 incident-edge pairs
-> delay-three run cuts
-> lazy rank-3 and rank-9 paths
-> natural pin labeling
-> flexible pin labeling
-> independent interval-OR verification.
```

The first SAT model surviving all central gates should be factored
immediately.  Continuing to optimize shadow scores without a pin test risks
moving into an unlabelable component, as happened during the k=12 work.

## 8. Unrestricted mathematical constraints, if the fixed row fails

An UNSAT result for every fixed row would not settle length 465.  The exact
unrestricted fallback is substantially smaller than raw array SAT once the
proved central structure is used.

### 8.1 Monotone band

Choose one witness for every rank-six mask and sort by left endpoint.  Then

```text
I_i=[i+alpha_i,i+beta_i],
0 <= alpha_1 <= ... <= alpha_462 <= 3,
0 <= beta_1  <= ... <= beta_462  <= 3,
alpha_i <= beta_i.
```

There are ten possible band states and at most seven constant-state regimes.
At least 93 selected rank-six witnesses have length four.  This is the proper
unrestricted replacement for assuming all 462 witnesses are the four-windows
`[i,i+3]`.

### 8.2 New fan-capped pruning of the band states

Put `w_i=beta_i-alpha_i` and let `x_j` be the number of selected rank-six
witnesses with width `j`, `0<=j<=3`.  Applying the fan-capped avoidance theorem
to lower rank slabs gives the valid inequalities

```text
x_0 <= 3,
2*x_0+x_1 <= 138,
sum_i w_i >= 1008,
x_3 >= 93.
```

The first inequality uses the rank-five antichain.  The second uses ranks four
and five, whose chain height is two.  The third uses the complete nonzero
lower ideal of ranks one through five, whose chain height is five.  The last
is the independent short-interval-pool bound.  These constraints are cheap
pseudo-Boolean filters on the at-most-seven regime sequence.  Fan-capped
avoidance does not directly repair the fixed row, where every `w_i=3`; its
value here is pruning the unrestricted fallback.

### 8.3 Necessary two-coloured central forest

Choose witnesses for every rank-five and rank-six mask.  Join an included pair
by an `L` edge when the intervals share a left endpoint and by an `R` edge when
they share a right endpoint.  The proved theorem forces:

```text
each colour class is a matching;
no pair receives both colours;
the union is a spanning linear forest;
|L| >= 459 and |R| >= 459;
at most 6 path components;
at least 456 degree-two masks in each central layer.
```

It further forces at least `324/330` rank-four masks as intersections of
selected rank-five masks and at least `324/330` rank-seven masks as unions of
selected rank-six masks.  At least 93 rank-six witnesses have length four,
and at least 87 of those are internal vertices of this forest.

Thus the unrestricted central search is not an `11*465` free-bit problem.  It
is a six-component alternating forest in the rank-five/rank-six inclusion
graph, an at-most-seven-regime endpoint schedule, and eleven independent
interval-stabbing systems.  This structure is now implemented in the exact
forest/band solver below; it runs in parallel with, rather than waiting for,
the smaller fixed-row program.

### 8.4 Literal filtering constraints

Because `nu(10)=254`, every coordinate is absent from at least 254 array
entries.  More generally, for every `q`-set `Q`, at least `nu(11-q)` entries
avoid all coordinates in `Q`.  The averaged pseudo-Boolean constraints are

```text
sum_i binom(11-|A_i|,q) >= binom(11,q)*nu(11-q).
```

These are independent of rank slack and should be included in any direct or
forest-based unrestricted SAT model.

### 8.5 Implemented globally exact forest/band solver

`k11_forest_sat.cpp` replaces the raw interval variables for all rank-five and
rank-six targets by two monotone 462-slot band schedules.  Each slot chooses
one of the ten endpoint states `(alpha,beta)`, its eleven bits are constrained
to equal the OR of that physical interval, and 462-by-462 target flags force
the slot values to permute the corresponding Boolean layer.  Shared left and
right endpoints materialize the two inclusion matchings as redundant
propagation clauses.  All other ranks retain the audited direct interval
encoding, so no fixed-row, Hamilton, Johnson-adjacency, or chosen-component
assumption is introduced.

The independently reproduced inventory is

```text
variables = 4,892,622
clauses   = 15,524,818
```

versus `9,815,220` actual variables and `26,452,166` clauses in the older
unrestricted direct model after endpoint-injection auxiliaries.  The
formula is SAT if and only if a universal nonzero length-465 array exists.
`K11_FOREST_SAT_DESIGN.md` and `K11_FOREST_SAT_AUDIT.md` contain the exact
soundness/completeness proof and inventory.  Two low-priority seeds are live
on the remote Pod, in addition to two independently audited direct-formula
seeds; any SAT output is still required to pass both project verifiers.

### 8.5 First globally WLOG forest/band generator

`k11_forest_sat.cpp` now implements the minimal exact unrestricted fallback.
It replaces the raw rank-five and rank-six target witnesses by two sorted
462-slot monotone schedules

```text
I_i^s=[i+alpha_i^s,i+beta_i^s],
0<=alpha_i^s<=beta_i^s<=3,
alpha^s and beta^s nondecreasing.
```

Small conditional OR clauses label each slot, and 426,888 slot-mask indicators
make each central row a permutation of its Boolean layer.  Shared left and
right endpoint states explicitly expose the two inclusion matchings and their
strict nesting directions, hence the at-most-six-component alternating
forest.  Rank-five width four is forbidden by exact rank-six witness pruning.

All noncentral ranks retain the audited direct exact witness encoding.  This
makes the first version easy to prove sound and complete while reducing the
primary formula from 8,098,440 to about 4.9 million variables (roughly 39%).
It is unrestricted: every hypothetical length-465 solution maps to one of its
two monotone schedules.  The full proof, clause inventory, and next exact
compressions are in `K11_FOREST_SAT_DESIGN.md`.

### 8.6 Exact adjacent-shadow compression

Ranks four and seven need not retain their full direct witness blocks.  For
rank four, independently choose one witness for every target and compare its
left and right endpoint sets with those of the selected rank-five family.
Each same-side endpoint intersection has size at least

```text
330+462-465=327.
```

Therefore at least `327+327-330=324` rank-four targets have both flags, and at
most six are exceptions.  A doubly flagged rank-four witness is strictly
inside two rank-five witnesses and hence has length at most two.  It can be
selected from the shared strip of exactly

```text
465 singleton intervals + 464 adjacent pairs = 929 candidates.
```

The dual endpoint argument gives at least 324 doubly flagged rank-seven
targets.  Their selected rank-six proper prefix and suffix are distinct
six-subsets of the target, so their union is the whole seven-set.  Six generic
exact witness slots per layer represent the possible exceptions without
guessing which six masks they are.

This theorem is implemented under

```text
K11_FOREST_ADJACENT_SHADOWS=1
```

and is globally WLOG.  It preserves both independent monotone central
schedules and introduces no fixed derivative row, Hamilton path, Johnson
adjacency, or chosen exception set.  Its independently checked inventory is

```text
variables = 3,148,302
clauses   = 14,546,194
```

instead of `4,892,622/15,524,818`, saving `1,744,320` variables and `978,624`
clauses.  The exact proof, implementation inventory, and independent frozen-
source audits are in `K11_FOREST_ADJACENT_SHADOW_REDUCTION.md`,
`K11_FOREST_ADJACENT_SHADOW_REDUCTION_AUDIT.md`, and
`K11_FOREST_ADJACENT_SHADOW_REDUCTION_INDEPENDENT_AUDIT.md`.

### 8.7 Exact rank-six band cuts and combined formula

The optional guard

```text
K11_FOREST_BAND_CUTS=1
```

encodes the four proved necessary inequalities for the selected **rank-six**
schedule:

```text
x0 <= 3
2*x0+x1 <= 138
sum(width_i) >= 1008
x3 >= 93
```

They come respectively from the rank-five antichain, the rank-four/five
height-two slab, the full ranks-one-through-five ideal, and the independent
short-interval-pool count.  They must not be copied onto the independently
chosen rank-five schedule.

Because `x3>=93`, state `03` occurs.  Coordinatewise monotonicity then excludes
the three states incomparable with it, leaving the exact chain

```text
00, 01, 02, 03, 13, 23, 33.
```

If `b1,...,b6` are its six transition positions, the four inequalities are
equivalent to

```text
b1+459             <= b6
b1+b2+786          <= b5+b6
b1+b2+b3+1008      <= b4+b5+b6
b3+93              <= b4.
```

Exact boundary selectors, binary extraction, ripple addition, and unsigned
comparators add `3,026` variables and `8,361` clauses.  The guard is
orthogonal to adjacent shadows.  All four independently reproduced formula
inventories are

| adjacent shadows | band cuts | variables | clauses |
|---:|---:|---:|---:|
| 0 | 0 | 4,892,622 | 15,524,818 |
| 0 | 1 | 4,895,648 | 15,533,179 |
| 1 | 0 | 3,148,302 | 14,546,194 |
| 1 | 1 | 3,151,328 | 14,554,555 |

Thus the smallest currently audited globally unrestricted formula is the last
row.  It remains satisfiable if and only if a universal nonzero 11-bit array
of length 465 exists.  This is an exact reduction statement, not a solver
result: the build-only reproductions prove neither SAT nor UNSAT.  Any SAT
model still needs both independent OR verifiers, and an UNSAT theorem still
needs an archived, independently checked proof trace.  See
`K11_FOREST_BAND_CUTS.md` and `K11_FOREST_BAND_CUTS_AUDIT.md`.

### 8.8 Exact rank-three shadow compression

The rank-three/rank-five endpoint sets meet in at least 162 positions at
each endpoint colour.  Hence at least 159 of the 165 rank-three targets are
crossed at both ends by proper rank-five extensions.  Since every selected
rank-five interval has physical length at most three, these 159 witnesses are
singletons or adjacent pairs.  Six exact generic slots cover the possible
exceptions.

The guarded `K11_FOREST_RANK3_SHADOWS=1` encoding reuses the 929 exact short
OR values from the adjacent-shadow guard.  With adjacent shadows and band
cuts it produces

```text
2,885,308 variables
14,360,485 clauses
298 direct targets.
```

The theorem, encoding, and inventory are independently audited in
`K11_FOREST_RANK3_SHADOW_REDUCTION_AUDIT.md` and
`K11_FOREST_RANK3_SHADOW_IMPLEMENTATION_AUDIT.md`.

### 8.9 Joint rank-five/rank-six band circuit

Writing `x_j` and `y_j` for the width profiles of the selected rank-six and
rank-five rows, respectively, every unrestricted optimum must satisfy

```text
x0 <= 1
y0+x0 <= 135
y1+2*y2 >= 549+4*x0
x0+x1 <= y0+3
y2 <= x3+3.
```

These rows combine omitted-endpoint sums, fan-capped lower mass, and
cross-layer endpoint nesting.  They leave only 563,562,210 of the prior
13,985,992,864 scalar profile pairs.  The exact guarded implementation
selects one of three complete rank-five monotone state chains and translates
the rows to unsigned boundary comparisons.  It adds 4,016 variables and
29,966 clauses.  With every current globally-WLOG guard enabled, the exact
unrestricted instance is

```text
2,889,324 variables
14,390,451 clauses.
```

Two seeds of this formula are live remotely.  This is still a candidate
search, not a SAT or UNSAT result.  See
`K11_FOREST_JOINT_SHORT_BAND_CUTS_AUDIT.md` and
`K11_FOREST_JOINT_BAND_IMPLEMENTATION_AUDIT.md`.

### 8.10 Multi-rank endpoint alignment

At either endpoint colour, inclusion-exclusion forces at least 324 common
rank-4/5/6 endpoints and at least 24 common rank-3/4/5/6 endpoints.  Strict
nesting under the width-three cap makes their central widths respectively

```text
rank5 in {1,2}, rank6 in {2,3};
rank5=2, rank6=3.
```

The exact guarded implementation defines all endpoint summaries and counted
conjunctions bidirectionally and uses four 465-input counters.  It adds
35,373 variables and 126,635 clauses.  With all currently audited guards the
production CaDiCaL build has

```text
2,924,697 variables
14,517,086 clauses.
```

The source and formula inventories are independently audited in
`K11_FOREST_ENDPOINT_ALIGNMENT_IMPLEMENTATION_AUDIT.md`.  No live search was
replaced by this binary before that audit completed.

### 8.11 Exact literal-rank-six branch portfolio

The unrestricted witness-band mathematics now proves that an optimal array
has at most one literal rank-six occurrence, that it lies at a word endpoint,
and that coordinate permutation plus reversal reduce it to the normal form

```text
either no rank-six entry occurs,
or A[0]=63 is the sole rank-six entry.
```

The guarded solver anchors the joint-band bit `e=x0` to `A[0]=63` and runs
the two exhaustive units `e=0` and `e=1`.  The boundary deletion count adds
the stronger branch-one row

```text
y2 >= x1+96.
```

After independent source audit, production build-only runs reproduced:

| branch | variables | clauses |
|---:|---:|---:|
| 0 | 2,924,697 | 14,732,380 |
| 1 | 2,924,938 | 14,734,039 |

Seeds 61 and 62 are live remotely on cores 36 and 38.  These runs are an
exact partition of the symmetry-reduced unrestricted existence problem, not
merely heuristic phase variants.  A SAT result still needs both independent
OR verifiers; two UNSAT results need checked proof traces and explicit
case-split packaging.  See `K11_FOREST_RANK6_BRANCH_DEPLOYMENT.md`.

### 8.12 Exact minimal-component specializations

The independently audited component theorem gives two much smaller exact
subcases of the unrestricted forest.  The optional solver mode
`K11_FOREST_MIN_COMPONENT` has two values:

```text
e0c1: no literal rank-six entry and one alternating central component;
e1c2: A[0]=63 isolated, plus one alternating 923-vertex component.
```

The first mode enforces the one-perfect-matching/unit-shift schedule.  The
second enforces

```text
P0,Q1,P1,...,Q461,P461,
Q(i+1)=P(i) union P(i+1),
```

the exact physical endpoint equations, length-two caps below rank five, and
the audited four-exception reduction.  Both modes are sound and complete for
their named component branches; neither covers all possible optima.

Independent formula inventories are:

| mode | variables | clauses | added clauses |
|---|---:|---:|---:|
| branch 0, absent | 2,924,697 | 14,732,380 | 0 |
| `e0c1` | 2,924,697 | 14,772,036 | 39,656 |
| branch 1, absent | 2,924,938 | 14,734,039 | 0 |
| `e1c2` | 2,924,938 | 14,811,758 | 77,719 |

No variables are added.  The absent-mode clause stream is exactly unchanged.
Production searches with seeds 71 and 72 are live remotely on cores 40 and
43.  Source SHA-256 is
`c16750771e78912f427d472d845cf952e30e4909eea97b474b6fccc0d9676017`;
the independent audit is `K11_MINCOMP_SOLVER_INDEPENDENT_AUDIT.md`, SHA-256
`8984ad8b9420ca8c388e54c215abe3b8250ae89116638feabf1ac8823b2c905d`.

### 8.13 Optional exact local-density cuts

The unrestricted density theorems are now encoded behind

```text
K11_FOREST_LOCAL_DENSITY_PB=1
```

as the exact pseudo-Boolean inequalities

```text
210 n1+84 n2+28 n3+7 n4+n5 >= 7392,
252 n1+126 n2+56 n3+21 n4+6 n5+n6 >= 12936.
```

The implementation derives exact one-hot entry ranks from the original array
bits, shares the rank circuit, uses nonmodular ripple addition, and finishes
with exact unsigned comparators.  It adds 59,036 variables and 280,226 clauses
to each production portfolio.  Enabled inventories are:

| mode | variables | clauses |
|---|---:|---:|
| branch 0 | 2,983,733 | 15,012,606 |
| `e0c1` | 2,983,733 | 15,052,262 |
| `e1c2` | 2,983,974 | 15,091,984 |

The disabled clause streams are literally identical to the frozen solver in
all three modes.  Standalone exhaustive gate tests and six production
build-only regressions pass.  This is a logically valid pruning module, not a
new SAT/UNSAT result.  See `K11_LOCAL_DENSITY_PB_ENCODING.md`; this original
density-only checkpoint had source SHA-256
`a66bf34be18ae09c3b22252fe96c7dd96f9f780495ce0acd1fa7868d3f015247`.

The two density-only minimal-component runs, seeds 81 and 82, were later
retired without a result when the six-set threshold was strengthened.  Their
logs and hashes were preserved.

### 8.14 Containment-multiplicity witness caps

If a physical interval has OR-rank `s`, the simultaneous selected-witness
argument gives the exact length cap

```text
c_s(n)=min_r [n-C(k,r) + (r<=s ? C(s,r) : 0)].
```

At `k=11,n=465`, ranks one through eleven have caps

```text
3,3,3,3,3,4,10,31,87,213,465.
```

The optional switch `K11_FOREST_CONTAINMENT_CAPS=1` applies these bounds to
the direct and exceptional witnesses.  It adds no variables and 107,368
binary clauses in the fully enabled adjacent-shadow formula.  With both the
density module and containment caps, the two minimal-component inventories
are:

| mode | variables | clauses |
|---|---:|---:|
| `e0c1` | 2,983,733 | 15,159,630 |
| `e1c2` | 2,983,974 | 15,199,352 |

Seeds 91 and 92 remain live on remote cores 40 and 43 using the original
six-set threshold.  Their source SHA-256 is
`78360d76011be1b6f600baf944e51e2949f059231595864233dd8dc8d0b3d7b8`.
The independent proof/encoding audit is
`CONTAINMENT_MULTIPLICITY_INDEPENDENT_AUDIT.md`, SHA-256
`0f3ab112fc712ec93ba937a2c42818f8119aa67640c4ca8c100a33cb74f4eefd`.

### 8.15 Nested local-density strengthening

Because the containment caps bound every physical interval, marked-run
packing inside each fixed six-set improves `p_U>=23` to `p_U>=28`.  The
six-set PB comparator is therefore strengthened, with no new gate or clause,
to

```text
252 n1+126 n2+56 n3+21 n4+6 n5+n6 >= 12936.
```

The exact cap-only local bounds for ambient subcube ranks one through ten are

```text
1,2,4,8,16,28,45,76,129,214.
```

The current solver source SHA-256 is
`c9b27476bfe62c1b0c75cda5f0dd713470a66db10fb2d697fd6cf6698b407049`.
Remote build-only verification reproduced the unchanged strongest formula
inventories.  Seeds 101 (`e0c1`, core 44) and 102 (`e1c2`, core 47) now run
the strengthened density cut together with containment caps.  The proof and
source audit is `CONTAINMENT_CAPS_SOLVERS_INDEPENDENT_AUDIT.md`, SHA-256
`e86622b80bf35b92092fa79df22c26d0e0c9ed00e25d4619143504563b2b5017`.

### 8.16 Corrected q19 mixed-delay prefix

The former thirteen-cell portal proposal is graph-theoretically impossible:
the twelve missing rank-seven masks induce six components in `J(11,7)`, but
one rank-eight portal can split their consecutive colour walk into at most two
blocks.  A seam-compatible factorable lift first appears with nineteen
rank-six triple windows.  The exact 22-entry prefix is

```text
489 425 424 300 780 788 836 1604 1602 1218 195
99 83 27 30 538 154 1176 408 4 32 514
```

Its first eighteen quadruple windows cover all twelve missing rank-seven
masks plus six connector colours, and its nineteenth is `958`.  The retained
factor state is `4|32|514`.  The certificate and proof are
`K11_PARTIAL_SWITCH_PREFIX_NEXT.md` and
`K11_PORTAL_EMBEDDING_MATH_NEXT.md`.

### 8.17 Exact full-array portal branches

`k11_forest_sat.cpp` now accepts

```text
K11_FOREST_PORTAL_BRANCH=q19_factor_prefix
K11_FOREST_PORTAL_BRANCH=q19_fixed_row
```

with exactly adjacent shadows, rank-three shadows, and optionally containment
caps enabled.  The first branch fixes the 22 array entries above.  The second
fixes only the mixed central schedule, its nineteen rank-six values, and the
`958` seam.  Their capped inventories are respectively

| branch | variables | clauses |
|---|---:|---:|
| q19 fixed row | 2,882,282 | 14,459,977 |
| q19 fixed factor prefix | 2,882,282 | 14,460,196 |

The independent implementation audit is
`K11_PORTAL_BRANCH_IMPLEMENTATION_AUDIT.md`, SHA-256
`863dda810cafd94ce3aaaeff38f0a64092ed43b331b0d6b123425a658ed99201`.
Both are exact branches of the full 465-entry universal-array formula.  A SAT
model settles `nu(11)=465`; branch UNSAT has no unrestricted implication.

The suffix-only recombination switches are not deployed: their current form
omits part of the exact boundary signature and part of the external coverage
ledger.  See `RECOMBINE_PORTAL_OPTIONS_PREDEPLOY_AUDIT.md`.

### 8.18 Prescribed middle-level cycle

The alternating path induced by the q19 prefix extends to a 924-vertex
Hamilton cycle in the rank-five/rank-six incidence graph.  Cutting it into
369- and 93-rank-six arcs accounts for all 462 rank-five colours exactly.
This closes the pure middle-level graph gate.

It does not close factorability.  Exhausting all 702 oriented admissible cuts
of this certificate finds no mixed-delay factorable row; the best cut has 98
bad coordinate runs and total deficit 111.  Future central-cycle searches
must impose run constraints during construction rather than append them after
Hamilton completion.  The certificate and audit are in
`ML11_PRESCRIBED_EXTENSION_NEXT.md`.

A bounded two-perfect-matching search preserving the forced path improved the
q19 mixed-run score from `239/154` to the independently verified `187/126`.
The new cycle is a valid
Hamilton certificate, but the score omits fixed-boundary pins, lower labels,
and upper shadows and is not an edit distance.  See
`ML11_PRESCRIBED_RUN_SEARCH_NEXT.md`.

### 8.19 Exact boundary-reservoir reduction

The audited left-anchored maximal-shadow theorem changes the factor stage.
For the canonical `369/93` single switch, all 1,011 nontrivial feasible
central meets are exact lower OR witnesses in the maximal factor, and every
factor of the same central row automatically retains every consecutive upper
union.  The remaining short cells are the explicit twelve-cell reservoir

```text
[1,1] [1,2] [2,2]
[370,372] [371,372] [372,372]
all six intervals in [463,465].
```

The maximal factor collapses these to at most eight values and therefore
must miss at least four lower masks.  Sparse pinning is not optional, but its
entire effect is confined to the eight physical positions

```text
[1,2] union [370,372] union [463,465].
```

After choosing twelve reservoir labels, only `O(k d^2)` local pin conditions
need be retested; upper-shadow witnesses require no separate protection as
long as the central row remains exact.  See
`SINGLE_SWITCH_MAXIMAL_SHADOW_THEOREM.md` and its independent audit.

## 9. What the general asymptotic mathematics contributes here

The complement-bridge, product-box, triangular-core, and fan-capped work does
not directly shorten the present 465-entry checkpoint.  Its useful finite
contributions are:

1. fan-capped avoidance gives the unrestricted band inequalities above;
2. the exact pinning theorem prevents false positives from envelope-only
   searches;
3. the global flag/forest theorem supplies the correct fallback if the fixed
   row is impossible;
4. the successful exact k=10 and k=12 patterns justify prioritizing the
   two-sided Johnson row plus sparse pins rather than raw decimal arrays.

The current finite search and the general mathematical program should
therefore continue in parallel.  A k=11 SAT witness would settle the first
open finite case.  It would not by itself supply the missing all-k recurrence;
conversely, the general three-/four-box work is unlikely to discover these
last fourteen Johnson-edge replacements for us.

## 10. Completion criterion

If any remote path survives every central gate:

1. generate both the natural and flexible factor-label CNFs;
2. translate a SAT model to exactly 465 nonzero entries;
3. check `D^3 A=T` directly;
4. enumerate all `465*466/2=108345` intervals;
5. independently verify by the distinct-suffix-OR recurrence;
6. preserve the path, factor model, array, logs, hashes, and solver version.

A passing array proves `nu(11)=465` immediately by the rank-slack lower bound.
No UNSAT result confined to the fixed-row ansatz proves a stronger lower bound
for the unrestricted problem.
