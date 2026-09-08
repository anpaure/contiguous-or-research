# k=15 phase-quotient residence handoff (2026-07-28)

This lane replaces the two rigid phase-aligned rectangle templates by the
complete `Z_15`-invariant Johnson-edge catalogue on the same 5,295 vertices
(physical cycle 1 plus the vertex set of physical cycle 12).

## Exact finite model

- 353 vertex orbits and 353 lower-colour orbits.
- 7,609 candidate edge orbits.
- Exactly one selected edge orbit per original lower-colour orbit.
- Quotient degree at most two.  Since exactly 353 edges are selected, the
  total-degree identity forces degree exactly two at all 353 quotient vertices.
- Every critical upper-q1 target is covered.
- All coordinate runs of length one and two are forbidden eagerly.  Length
  three is cut lazily, one quotient-distinct clause per witnessed motif.

The preserved current CNF is:

`scratch/k15_phasequotient_eager2_res_noconn.cnf`

- DIMACS: `p cnf 52150 1801026`
- SHA-256:
  `2940a2121aa6e9d000d680832af09b615304e6209546daae84805f6ccd274fee`
- It contains the eager 1,623,285 short-run clauses and all lazy length-three
  clauses learned through decoded round 2.  The next cloud solve is round 3.

Resume with:

```bash
python3 scratch/resume_k15_phasequotient_residence_cnf.py \
  scratch/k15_phasequotient_eager2_res_noconn.cnf \
  --prefix scratch/k15_phasequotient_cloud \
  --start-round 3 --seconds 1800 --rounds 100
```

The resume driver preserves every solver model, decodes the concrete factor,
runs the independent whole-carrier audit, appends all new quotient-distinct
length-three clauses, and writes a JSON round summary.  Thus migration between
machines does not lose the exact mathematical state (although Kissat's learned
internal clauses are not portable).

## Audited trajectory before local solving was stopped

| round | replacement components | replacement residence-3 defects | upper holes q1/q2/q3 |
|---:|---|---:|---|
| 0 | `45,45,105,200,200,200,1500,1500,1500` | 885 | `0 / 258 / 60` |
| 1 | `45,5250` | 855 | `0 / 213 / 60` |
| 2 | `5,5,5,50,50,50,270,4860` | 765 | `0 / 210 / 75` |

All three factors have the exact 5,295-colour lower-q1 palette and zero
upper-q1 holes.  Every remaining replacement residence defect has run length
exactly three; runs one and two are impossible by construction.  The original
physical cycle 14 contributes a separate 15 residence defects, so whole-carrier
counts are the displayed replacement count plus 15.

Round artifacts are named
`scratch/k15_phasequotient_eager2_res_noconn.round{0,1,2}.{kissat.out,factor.json,audit.json}`.
The saved solver-output hashes are:

- round 0: `d7cb84f805381e143ef10d71ea8b7e073422dba7efa0a3038dec48c355d969a3`
- round 1: `a155daf8121328fdf80e19f9a7767aaea51f5693926993b2125088366b917c3b`
- round 2: `81f0c151a09ee56e06c3e7f0dcd85dcdd20d6b826e92a853fa03c726487c6d85`

## What this proves and does not prove

It proves that exact lower-q1 plus exact upper-q1 and the complete exclusion of
residence runs one and two are jointly feasible in the invariant catalogue.
It does **not** yet prove full depth-three residence, upper q2/q3, or a usable
connected/cut-safe carrier.

Independently, the q1+q2 quotient model is SAT and misses only one 15-orbit at
upper q3, but its residence count is 1,500.  The combined target is therefore:

1. full residence (zero length-three motifs),
2. upper q1/q2/q3 coverage,
3. component/cut safety for the final compiler.

The local rectangle sublane is closed: its only exact global choices are the
uniform 444 template (resident but five components) and uniform 5049 template
(connected but 15 residence defects and 16 upper-q1 holes).  Any binary mixture
would require `j -> j+11` or `j -> j+13` to remain a permutation; the implication
`x_j <= x_{j+2}` around `Z_15` forces all choices equal.  The complete five-orbit
endpoint model is also UNSAT after imposing exact q1 and a component cut.

## 2026-07-28 combined upper-q3 / residence / connectivity update

The q1+q2 model has now been extended by exact lazy q3 separation.  A cloud
model enforcing the single q3 orbit 6139 was decoded independently and has
only two remaining q3 hole orbits, 4031 and 8111.  Thus the current exact q3
core needs only the three observed orbit constraints

```text
4031, 6139, 8111.
```

That decoded factor has 18 physical components, 97 quotient-distinct
depth-three residence blockers, and four quotient-distinct physical subtour
cuts.  These are preserved in:

```text
scratch/cf15_q3_seed17000.factor.json
scratch/cf15_q3_seed17000.residence.json
scratch/cf15_q3_seed17000.connectivity.json
```

`search_k15_phasequotient_upperq2.py` now imports both negative residence cuts
and positive physical subtour cuts, and emits the next exact cut families from
every decoded model.  `run_k15_upperq3_lazy.py --connected` jointly separates
q3 holes, residence defects, and physical components until all three vanish.
The smallest staged combined CNF has

```text
p cnf 617719 2252678
```

and is preserved at
`h100:/dev/shm/k15_sat/cf15_combined/combined_r1.cnf`.  It includes exact q1,
q2, the three q3 orbits above, eager length-one residence, the 97 exact seed
residence blockers, and the four exact seed subtour cuts.  The full cloud
command and final safe-opening audit are recorded in
`scratch/CF15_COMBINED_CLOUD_HANDOFF_20260728.md`.

There is also an exact static depth-three residence encoding using 2,824
endpoint auxiliaries.  For a coordinate x in a middle vertex v, the auxiliary
marks that exactly one selected edge at v crosses the x-boundary.  After
forbidding two crossings, a short x-run is exactly one of:

1. one vertex with two crossing edges;
2. one internal edge with both endpoints marked;
3. two internal edges with both outer endpoints marked.

This gives an exact q1+q2 fallback of 306,832 variables and 2,983,133 clauses
via `--compact-residence-depth3`.  It is stronger than the old eager-depth-two
CNF, while the lazy combined command remains the smaller primary search.

The first combined lazy CNF is SAT (seed 22007).  It preserves exact upper q1
and q2, and misses only the two new upper-q3 orbits 7677 and 8125.  Its physical
component sizes are `45,130,130,130,4860`; its replacement residence histogram
is 675 runs of length two and 585 of length three.  Adding the 84 new residence
blockers and three new subtour cuts gives round 2:

```text
h100:/dev/shm/k15_sat/cf15_combined/combined_r2.cnf
p cnf 790969 2945767
SHA-256 08fdf4b72f9e1e102a0ebf419d4a7682371c597aea2b21a68118baf55dc1de2c
```

The five q3 keys are now `4031,6139,7677,8111,8125`; the exact cumulative
cut ledger has 181 residence clauses and seven physical subtour clauses.

## 2026-07-28 full-physical exact-residence / connectivity frontier

The quotient-only frontier above has now been superseded by an exact physical
catalogue on all 6,435 middle vertices.  The restricted catalogue has 70,605
Johnson edges.  Its static depth-three residence encoding has 795,770
variables and 18,486,851 clauses.  A first SAT model was independently
decoded as

```text
32 components = 21 cycles + 11 paths
residence defects = 0
upper holes q=1,...,7 = 0
lower q1 repeats = 0
lower holes = 11
```

The audited carrier is

```text
scratch/k15_dense40_exactres_seed550001_audit.audit.paths.json
```

Opening all cycles while retaining every upper witness is exact UNSAT.  This
is not a residence obstruction: the opening loses only 19 witnesses at
q=1,2,3, but their endpoint geometry cannot be repaired by a fixed ordering.
The correct operation is to change the selected physical edges.

Two exact operations are now available.

1. `append_k15_joint_cycle_blockers.py` appends either an exact selected-cycle
   blocker or a positive component-cut clause.  Repeated exact blockers have
   produced a sequence of residence-zero, upper-exact carriers whose cycle
   count fell from 21 to 3 by round 23 while preserving a simple lower
   palette.  Current files use the prefix
   `scratch/k15_dense40_exactgrad2`.
2. `search_k15_cycle_path_onepivot.py` deletes one cycle edge and adds one
   Johnson seam to a path endpoint.  The move is accepted only if all upper
   shadows q=1,...,7, depth-three residence, and the simple lower palette are
   preserved exactly.  Applied to exactgrad round 18 it reduced eight cycles
   to two with no SAT call:

```text
scratch/k15_exactgrad_r18_onepivot.json
20 components = 2 cycles + 18 paths
residence = 0; upper holes q1..q7 = 0; lower repeats = 0
```

At round 23 the same pivot leaves a single 30-cycle:

```text
scratch/k15_exactgrad_r23_onepivot.json
24 components = 1 cycle + 23 paths
```

That final cycle has no individually shadow-safe cut and no direct
residence-safe endpoint seam.  It must be removed by the continuing exact
edge reroute, not by pretending that general compiler slack can pay for lost
rank-seven colours.  The rank-seven row has only one spare cell, so the final
target remains one path with a simple lower palette.

For broader escape, `--full-johnson-catalogue` now enables all 180,180 edges
of `J(15,8)`.  With `max_paths=1` the base has 1,261,259 variables and
4,766,940 clauses.  The optimized exact residence encoding has 3,783,779
variables and 14,882,760 clauses.  Native-negative signs depend on the seed
factor: the authoritative base uses
`scratch/k15_uniform444_h8_exact.factor.json`; models appended with the older
phase-quotient factor are invalid and have been quarantined.

No length-6,438 OR certificate is claimed yet.  Completion still requires:

1. a connected one-path carrier (cycles zero and lower holes one),
2. exact all-rank lower Hall PASS,
3. compilation of the length-6,438 word, and
4. exhaustive verification of all 32,767 nonzero masks.

## 2026-07-28 endpoint-rotation descent: exact nine-path frontier

The cycle gate is now closed.  Two independent lanes produced cycle-free
carriers, and the stronger full-Johnson artifact has 21 paths with every hard
local invariant exact:

```text
scratch/k15_r21round1_branch6_audit.audit.paths.json
6435 distinct rank-8 vertices; 21 paths; 0 cycles
residence defects = 0
upper holes q=1,...,7 = 0
lower q1 repeats = 0; lower holes = 21
```

The fixed endpoints of this carrier have no admissible direct transition,
even if lower-colour simplicity is dropped.  This is an endpoint-geometry
obstruction, not a remaining cycle or shadow obstruction.

`scratch/search_k15_endpoint_rotation_descent.py` implements an exact
Posa-style repair.  It cuts one internal edge of path B and attaches an
endpoint of path A to one side of the cut.  The other side remains a path, so
the operation changes one endpoint without changing the path count.  Every
candidate is accepted only after exact checks of

1. all 6,435 middle vertices exactly once and Johnson adjacency,
2. depth-three residence,
3. a globally simple rank-seven edge palette, and
4. zero upper holes at every depth 1,...,7.

Whenever a rotation exposes an admissible endpoint join, the join reduces the
path count by one and is audited again.  This descent has certified

```text
21 paths -> 10 paths -> 9 paths.
```

The authoritative current carrier is

```text
scratch/k15_rotation_best9.json
independent audit: scratch/k15_rotation_best9.independent.json
audit SHA-256: 181d3fed484b8229eacb0bbd5f3d3adb457e60bc06093954d02037cd85e1428b
path lengths: 13,27,32,206,406,533,1179,2003,2036
lower holes q1,q2,q3: 9,32,10
upper holes q1,...,q7: all 0
residence defects: 0
```

A second inequivalent exact nine-path carrier is retained as
`scratch/k15_rotation_best9b.json` (independent audit SHA-256
`582851d4e17724f760392a7377906f4e8bf1d51bdbe72280e0441cd36dca7f33`).
The exact full-Johnson SAT lane is simultaneously descending the endpoint cap
from nine to eight and solving the direct one-path model with sound component
cuts and exhaustive final-missing-colour branches.

This is substantial but not yet the k=15 certificate.  The remaining formal
gates are unchanged: nine paths to one, then exact lower Hall, word extraction,
and the exhaustive 32,767-mask verifier.

## 2026-07-28 exact seven-path frontier and direct connectivity encoding

The endpoint-rotation descent continued without relaxing any invariant:

```text
21 paths -> 10 -> 9 -> 8 -> 7 paths.
```

The authoritative seven-path carrier is

```text
scratch/k15_rotation_best7_candidate.json
independent audits:
  scratch/k15_rotation_best7_candidate.independent.json
  scratch/k15_rotation_best7.independent.json
audit SHA-256: 389487e9c7481cb288d069083c41be822cb8b2d419b08963269d58654df2cf83
path lengths: 38,168,302,441,605,2192,2689
residence defects: 0
upper holes q=1,...,7: all 0
lower q1 repeats: 0; lower q1 holes: 7
lower holes q2,q3,q4: 49,13,2; q>=5: 0
```

Thus cycles and upper-shadow coverage are completely solved; only endpoint
geometry remains in the carrier stage.  Exact random rotations and beam
search are trying to expose the next missing-colour seam.  The strongest
beam frontier has a missing-colour endpoint pair with exactly one residence
defect, but an exhaustive collar 2-opt found no lower-palette-feasible repair
at that radius.  In the local two-cut neighbourhood, five of seven
final-missing-colour branches are exact UNSAT and two remain live.

A second exact lane now enforces connectivity in one SAT instance.  Orient
the selected degree-at-most-two graph, assign each vertex a 13-bit rank, and
require every directed selected edge to increment rank modulo 8192.  Since a
selected cycle has length at most 6435, it cannot close modulo 8192.  Requiring
exactly one indegree-zero source then forces a single spanning path.  The
full-Johnson instance has

```text
4,401,538 variables; 25,905,912 clauses; 180,180 physical edges.
```

It is phased around all 6,428 edges of the seven-path carrier, with no skipped
edge.  Restricted-catalogue and full-Johnson portfolios are running on the
remote CPU host; no SAT/UNSAT verdict is recorded yet.

The practical stopping target for the endpoint descent is two paths, not
necessarily one: five exact joins would leave one boundary seam for the
depth-three compiler's single rank-seven spare cell.  That boundary case must
still pass the exact Hall audit; it is not being counted as solved in advance.
After a one-path carrier, or a validated two-path boundary carrier, the
remaining gates are exact all-rank Hall, compilation of a length-6438 word,
and exhaustive verification of all 32,767 nonzero masks.

## 2026-07-28 exact six-path breakthrough

Four independent endpoint-rotation walks crossed the previous seven-path
frontier.  Three stable copies were independently audited by the root
pipeline; all are exact middle partitions, Johnson paths, depth-three
resident, upper-complete through q=7, and simple in the rank-seven palette:

```text
scratch/p7f_941_p6_candidate.json
  SHA-256 dfb596d36bb5efa3aaf7d0ec6a9d4af382d7ffdc323dc5fcb9baeaa201fc9652
  lengths 10,40,586,600,814,4385
  lower holes q1,q2,q3,q4 = 6,46,11,1

scratch/p7f_943_p6_candidate.json
  SHA-256 dc529d60e7da100ebd093e78303a97946558406c92180acaa33f61243b608181
  lengths 179,257,356,841,1685,3117
  lower holes q1,q2,q3,q4 = 6,51,12,2

scratch/p7f_944_p6_candidate.json
  SHA-256 9a47b06037366b8d96a9e301e0beebf996383faac1c916034ef087116c479f42
  lengths 23,592,672,930,1294,2924
  lower holes q1,q2,q3,q4 = 6,49,16,3
```

All have zero lower holes from q=5 onward and zero upper holes at every
q=1,...,7.  The balanced 943 copy is the current exact-SAT phase seed; all
6,429 selected edges are represented in the full-Johnson connectivity
encoding, leaving five joins/sources and no motif defect.  Exact rotation
walks and beams continue from all three inequivalent copies toward p5.

The 944 walk then immediately produced an exact five-path carrier:

```text
scratch/k15_rotation_best5_candidate.json
root independent audit: scratch/k15_rotation_best5.root_audit.json
SHA-256 d6217814ee9210fa92dfe290bdecabcd89fc91150ef6299f805e5cb63435fe93
path lengths: 519,643,781,884,3608
residence defects: 0
upper holes q=1,...,7: all 0
lower q1 repeats: 0
lower holes q1,q2,q3,q4 = 5,60,19,1; q>=5 = 0
```

This is three exact joins from the compiler-usable two-path boundary case,
or four from a single spanning path.  The producing walk remains live, and
the p4 SAT and direct cap-two/connectivity lanes are being rephased around
this stronger certificate.

The same descent then crossed to four paths:

```text
scratch/k15_rotation_best4_candidate.json
root independent audit: scratch/k15_rotation_best4.root_audit.json
SHA-256 b7754e476445c77c4bf392ce5b96094ef4439d5be77788608f327a72ee6d3675
path lengths: 666,1351,2151,2267
residence defects: 0
upper holes q=1,...,7: all 0
lower q1 repeats: 0
lower holes q1,q2,q3,q4 = 4,62,20,1; q>=5 = 0
```

Only two joins now separate the exact carrier from the two-path boundary
test.  `scratch/test_k15_two_path_boundary.py` exhausts all eight orders and
orientations of the first p2 carrier and accepts only an exact D^3 erosion,
zero residence defects, and complete upper shadows; any accepted chronology
then goes directly to the all-rank Hall audit.

One of the p4 walks has now made the next exact decrement:

```text
scratch/k15_rotation_best3_candidate.json
root independent audit: scratch/k15_rotation_best3.root_audit.json
SHA-256 436bde16bc34c156890ec649962704540591a75ebc25cebf89b3642f119db762
path lengths: 992,2515,2928
residence defects: 0
upper holes q=1,...,7: all 0
lower q1 repeats: 0
lower holes q1,q2,q3,q4 = 3,62,16,1; q>=5 = 0
```

The exact carrier is therefore one join from the two-path boundary test and
two from a single path.  Dedicated p3 rotations/beams and the direct cap-two
SAT model are now the primary carrier lanes.

## 2026-07-28 two-path boundary solved; Hall deficiency localized

The endpoint descent has reached two inequivalent exact p2 carriers:

```text
scratch/k15_rotation_best2_candidate.json
  SHA-256 a8e78fe813bc25c46a083d17b961c4631cdf9ccb03344b92cb0805839f2b0a8c
  lengths 111,6324; lower holes q1,q2,q3,q4 = 2,57,20,2

scratch/k15_rotation_best2b_candidate.json
  SHA-256 2b6348985399fc80c5a4c76978917fb8061fb6b0fd6ab93f57011ebba0597e85
  lengths 2756,3679; lower holes q1,q2,q3,q4 = 2,63,19,2
```

Both independently pass all middle, Johnson, residence, palette, and upper
audits.  Their fixed endpoints do not compile, but exact endpoint rotations
on the balanced copy produced multiple boundary chronologies with

```text
residence defects = 0
D^3(E^3(T)) = T exactly
upper holes q=1,...,7 = 0.
```

Thus the structural boundary gate is closed.  The first exact all-rank Hall
batch did not yet close the compiler: 21 independent boundary chronologies
had deficiencies 71,...,77, and a chronology from the unbalanced p2 carrier
improved the best to 69.  The unmatched targets are concentrated at ranks 7
and 6.  Empirically the Hall deficiency tracks missing lower-q2 targets almost
one for one (the first def=69 state had 57 lower-q2 holes), identifying the active
quantitative gate.

`scratch/fast_k15_compiler_hall.py` is an exact reverse-enumeration Hall
scorer.  It reproduces the generic audit but runs in about 0.23 seconds, so
Hall-aware endpoint descent is now practical.  An exact Hall beam has since
improved the independently reproduced deficiency to 65 (11 zero-candidate
targets): `scratch/k15_p2_hallbeam_best65.json`, independently audited SHA-256
`ae96be347e71da7f2e4a9651c4dee04466b90dfcd3c248b72649b5cc9e1075f5`.
Its outer endpoint contains one of the two missing rank-seven faces, and the
rank-seven zero count correspondingly drops from two to one, exactly
confirming the endpoint-cell diagnosis.  Separate endpoint geometry is
targeting the second missing rank-seven
faces at the outer compiler cells.  In parallel,
`scratch/search_k15_lowerq_endpoint_descent.py` rewinds to the best p6 carrier
and protects lower q2/q3 during the remaining joins.  Its authoritative
checkpoint is now

```text
scratch/k15_lowerq_p6_h28.json
independent audit: scratch/k15_lowerq_p6_h28.audit.json
SHA-256 95471d900decb83f207b268b5d9ca68b442a34bb9fbc01202c3e23b675e15ce3
6 paths; lower holes q1,q2,q3,q4 = 6,26,5,1
residence defects 0; upper q1,...,q7 all complete
```

Thus the protected route has reduced q2 holes from 46 to 26 and q3 holes
from 11 to 5 while preserving every hard carrier invariant.  Capped beams
are descending this stronger state toward p2 while the p6 coverage walk
continues lowering the holes.

The Hall obstruction now has an exact layer interpretation.  On the def=69
p2 chronology, rank 7 alone misses the two simple-lower holes.  After rank-7
cells are reserved, ranks at most 6 miss 68 targets, all at rank 6; rank 6
alone misses 56, while competition from ranks at most 5 costs the remaining
12.  The row-1 rank-6 envelopes are precisely the lower-q2 colours and the
row-0 rank-5 envelopes are the lower-q3 colours.  Consequently the clean
sufficient target is:

```text
lower q2 holes = 0
lower q3 holes = 0
the two q1 holes match into the two outer endpoint compiler cells.
```

This explains both search objectives and turns the Hall gate into explicit
carrier statistics rather than a black-box matching score.

Connectivity is no longer a gate.  The selected best-deficiency boundary seam
is itself the residence-safe Johnson edge `29876 -> 29874`.  It was excluded
from the earlier path search only because its rank-seven colour `29872` was
already used once.  Palette simplicity is not a compiler requirement, so
joining across that edge gives the exact one-path chronology

```text
scratch/k15_p1_usedcolour_from_def65.json
SHA-256 ffd1af22869dcfe1d23d142dd06c25139e3e3c3dff7e54f81deea2dae1c329f9
1 path on all 6435 middle vertices; all edges Johnson
residence defects 0; D^3(E^3(T)) = T; upper q1,...,q7 complete
lower q1 holes 2, repeats 1; lower q2/q3 holes 56/20
exact Hall deficiency 65
```

The repeated lower colour is intentional and is already accounted for by the
authoritative Hall instance.  Direct-p1 SAT portfolios whose only purpose was
palette-simple connectivity were therefore retired, freeing the remote CPU
for Hall and lower-shadow search.

The protected carrier descent has now made its first path decrement without
spending the improved lower coverage:

```text
scratch/k15_lowerq_p5_q23_candidate.json
independent audit: scratch/k15_lowerq_p5_q23_candidate.independent.json
SHA-256 973cc465e1872bab51d830abcc1966747389c2e356fe5e8739be4cd5dfc6bb59
5 paths of lengths 18,433,1174,1988,2822
lower holes q1,q2,q3,q4 = 5,23,6,1
residence defects 0; upper q1,...,q7 all complete
```

Thus the q2 reduction survives p6 -> p5 exactly.  Dedicated capped Pareto
beams continue p5 -> p4; any decrement is independently audited before being
promoted.

The next decrement has also landed; a subsequent exact rotation recovered the
one q2 colour initially spent, so both joins from p6 now preserve q2=23:

```text
scratch/k15_lowerq_p4_q21q3_5_frontier.json
independent audit: scratch/k15_lowerq_p4_q21q3_5_frontier.independent.json
SHA-256 cee22b6e74ec1b765b3a65d0c9bfe231af0d1db156acfe412b38c350b09f8aec
4 paths of lengths 170,674,828,4763
lower holes q1,q2,q3,q4 = 4,21,5,1
residence defects 0; upper q1,...,q7 all complete
```

Protected p4 -> p3 beams are active.  Palette simplicity remains a convenient
move-generator invariant, not a compiler requirement: at p2 a residence-safe
used-colour join is allowed whenever the authoritative Hall/compile audit
passes.

The q2/q3 Pareto beam has since improved the same exact p6 lane once more:

```text
scratch/k15_lowerq_best24q3_5_p6.json
independent audit: scratch/k15_lowerq_best24q3_5_p6.independent.json
SHA-256 83034e28ccf15c5d3e7949c68c341c1f152b18335d619693736f3b957f0a4ff8
6 paths; lower holes q1,q2,q3,q4 = 6,24,5,1
residence defects 0; upper q1,...,q7 all complete
```

This is the strongest independently audited q2 checkpoint at the time of
writing with q3=5.  A second independently audited Pareto point has q2/q3
`23/6`: `scratch/k15_lowerq_best23_p6.json`, SHA-256
`92ecfdecb0ebf11153bc7900751ae2d4dbc34d1c4327d790bd15f8535866bab9`.
Thus the strongest q2 reduction is 46 -> 23.  `scratch/search_k15_lowerq_beam.py` now keeps a Pareto
beam in `(q2 holes,q3 holes,endpoint geometry)` rather than spending q3 on a
q2-only descent.  `scratch/search_k15_p2_outer_hall_beam.py` separately uses the
exact long-range Hall gradient: a maximum matching of the two missing q1
faces into the two outer compiler endpoints, followed by the fast exact Hall
score only on boundary-ready states.

Connectivity is now closed independently of palette simplicity.  Orienting
the two paths of the def=65 carrier in reverse order at both ends gives the
residence-safe Johnson join `29876 -> 29874`; its colour `29872` already has
load one.  The authoritative one-path artifact is

```text
scratch/k15_p1_usedcolour_from_def65.json
SHA-256 ffd1af22869dcfe1d23d142dd06c25139e3e3c3dff7e54f81deea2dae1c329f9
exact Hall: scratch/k15_p1_usedcolour_from_def65.hall.json
```

It visits all 6435 middle vertices once, has residence zero and complete upper
shadows.  Lower q1 has two holes and one intentional repeat, which the
compiler permits.  The exact Hall score remains deficiency 65; Hall/lower-q
coverage, not connectivity, is now the sole finite gate.

A one-path Posa/Hall beam has already improved this connected lane to exact
deficiency 59:

```text
scratch/k15_p1_hallbeam_best59.json
SHA-256 ae942b4a1d28042998be350ab59ed72fe77fa50d30867b30166713f5db2a4f1f
lower q1 holes/repeats = 2/1; lower q2/q3 holes = 56/18
outer endpoint matching = 2/2; zero-candidate ranks 7/6 = 0/9
Hall unmatched ranks 7/6 = 50/9
```

The independent fast Hall audit reproduces deficiency 59.  Both exceptional
outer compiler cells now contain the two missing rank-7 faces, so the endpoint
gate is completely closed and every remaining zero-candidate target has rank
6.  This confirms that
the relaxed connected search space has genuine Hall descent directions; the
protected p4 lane remains the much stronger lower-q starting point.

For the outer-complete p1 state, the nine zero-candidate rank-6 masks are

```text
5286 8869 9042 10794 17738 18602 18986 21588 22176
```

The protected p4 q2=21 state already covers five of them; only
`8869,10794,17738,21588` are absent.  `search_k15_lowerq_beam.py` therefore
supports `--critical-mask` and puts this exact four-mask deficiency ahead of
the aggregate q2/q3 score.  Critical-aware p4 -> p3 beams preserve the five
already-paid Hall targets while attacking the remaining four directly.

The relaxed-palette lane has now merged connectivity with the protected lower
coverage.  Starting from the exact relaxed p2 q2=20 carrier, endpoint rotations
and one residence-safe join produced

```text
scratch/k15_relaxed_p1_q22_candidate.json
SHA-256 06815fbd4a129effc7fab586dd89116e762a96c6fc3e8042c36b82a64c387b2e
one path through all 6435 middle vertices
lower holes q1,q2,q3,q4 = 4,22,6,1; q1 repeats = 3
residence defects 0; upper q1,...,q7 all complete
exact Hall deficiency 37; zero candidates rank 7/6 = 4/7
```

The generic carrier auditor reports FAIL solely because of the intentional
q1 repeats.  `fast_k15_compiler_hall.py` now accepts a singleton
`middle_components` payload and independently reproduces deficiency 37.  This
cuts the finite Hall gap from 59 to 37 in one step.  The immediate target is
therefore p1 palette/endpoint repair (q1 holes/repeats `4/3 -> 2/1`) while
preserving q2 near 22, followed by the four critical rank-6 masks.

The protected simple-palette lane has now made the next exact decrement:

```text
scratch/k15_lowerq_p3_q24q3_5.json
SHA-256 0a092f390e40386beed0854dc617f5ca74399c9d7bb91e09483688ddb91819bb
3 paths of lengths 1422,1986,3027
lower holes q1,q2,q3,q4 = 3,24,5,1; q1 repeats = 0
residence defects 0; upper q1,...,q7 all complete
```

This is important for the final rank-seven Hall gate.  A length-6435 one-path
carrier can pass Hall only with at most two q1 holes: the compiler has exactly
two exceptional outer cells capable of paying missing rank-seven targets.
The relaxed p1 Hall descent is therefore bridge-only until its palette returns
to holes/repeats `2/1`.  By contrast the new p3 carrier is still simple.  Two
further joins through currently missing colours would give p1 holes/repeats
`1/0`, closing the rank-seven prerequisite with room.  Wide p3 -> p2 simple
beams are now the primary clean lane.

The relaxed Hall/DM lane has independently reached deficiency 34, but only by
temporarily increasing q1 holes/repeats to `6/5`; its zero-candidate set is
still four rank-seven plus seven rank-six masks.  This confirms that scalar
Hall descent alone is not the endgame.  `search_k15_palette_2opt_walk.py`
therefore performs exact two-opt bridge walks targeted at restoring the q1
palette while preserving residence and, in the strict lane, every upper
shadow.  A bounded-upper-hole variant is also available for testing whether
upper completeness is the local barrier to palette repair.

The clean lane is now one component closer again.  The strongest frozen p3
and its first p2 decrement are:

```text
scratch/k15_simple_p3_q21.json
SHA-256 8decd062f1d4319c486d7c61f995dc60882044355b58dc6c7f2d29b08743e341
p3 lengths 180,1769,4486; q1 holes/repeats 3/0
q2/q3/q4 holes 21/5/1; residence 0; all upper shadows complete

scratch/k15_clean_p2_q24.json
SHA-256 f7cf0efa9d84b97b7f2731d6c4db4006e35f93ec84a392231bce5b7f307cf865
p2 lengths 343,6092; q1 holes/repeats 3/1
q2/q3/q4 holes 24/5/1; residence 0; all upper shadows complete
```

The p2 carrier is the nearest structural state so far: a final join through
one of its three missing q1 colours lands exactly at the necessary terminal
palette `holes/repeats = 2/1`.  Its endpoint potential already has a missing
colour at radius two.  Dedicated p2 endpoint beams and walks are active.
Because the strict palette exposes only four initial rotations, the search
now separates bridge and terminal budgets: rotations may temporarily use up
to `rep/hole = 2/4`, `3/5`, or `4/6`, while a decrementing join is accepted
only at terminal `1/2`.  This expands the first rotation layer from four to
23 exact moves without weakening the final rank-seven Hall condition.

Several small simultaneous-splice classes have also been exhausted exactly:

* low-q p1 has no palette-improving 2-opt, 3-opt, or separated alternating
  4-opt (the 3-opt scan checked 12,893,731 sparse triples / 693,217 routed
  moves; the 4-opt scan checked 110,556 unique exchanges);
* p3 has no one-cut/four-segment Johnson routing among all 6,432 cuts and 192
  oriented segment orders;
* the frozen p2 has no terminal-valid direct one-cut/three-segment splice,
  nor a two-cut splice forced through one of its seven currently cross-path
  missing-colour edges.

These are local-search barriers, not impossibility results.  They establish
that the final clean join needs a nontrivial endpoint-rotation bridge or a
higher-order simultaneous exchange; they prevent further compute from being
wasted on the already-exhausted 2/3/4-opt neighbourhoods.

The exact Hall front has since advanced once more:

```text
scratch/k15_p1_hallbeam_best33.json
SHA-256 d29f993920b23b7d7e434be712cd8b1a30e8938c58542ed6d232f9eaa6d1c278
one path through all 6435 middle vertices
lower q1 holes/repeats = 5/4; lower q2/q3 holes = 23/6
outer endpoint matching = 1/2
exact Hall matching = 16350/16383, deficiency 33
zero-candidate targets = 6 at rank 6 and 4 at rank 7
```

Both the fast reverse enumerator and the generic all-rank Hall auditor reproduce
the deficiency.  The strict sequence of independently audited improvements is
`65 -> 64 -> 63 -> 62 -> 61 -> 59 -> 37 -> 36 -> 35 -> 34 -> 33`.
The high-repeat states are bridge states only: the exact rank-7 gate forces a
final one-path carrier back to at most two q1 holes.  An exhaustive audit of
every residence/upper-safe internal two-opt move from the def=33 carrier with
q1 holes at most eight found no neighbor of deficiency below 33, so the next
decrement requires at least a two-move bridge or a non-two-opt splice.

The clean lane has also improved substantially:

```text
scratch/k15_simple_p3_q21.json
SHA-256 8decd062f1d4319c486d7c61f995dc60882044355b58dc6c7f2d29b08743e341
3 paths of lengths 180,1769,4486
lower q1 holes/repeats = 3/0
lower q2/q3/q4 holes = 21/5/1
residence defects 0; upper q1,...,q7 all complete
```

This is currently the strongest structurally clean carrier.  Two joins through
missing q1 colours would produce a one-path carrier with q1 holes/repeats
`1/0`, eliminating the rank-7 obstruction rather than paying it at the two
outer cells.  Endpoint walks and Pareto beams have not yet found those two
joins.  A direct four-segment splice is the primary next search because it can
cross the sequential endpoint-rotation barrier in one operation.

The palette obstruction is now backed by finite local audits.  At repeats 3
there is a unique neutral exact two-opt move, which unlocks further neutral
Posa moves but has not reached repeats 2.  Exhaustive targeted three-opt on the
original repeats-3 carrier examined 12,893,731 unique triples (693,217
Johnson-valid raw reconnections) and found no state with q1 holes at most
three, even before the residence and upper constraints.  A targeted four-opt
audit over all three duplicate-colour cuts plus every fourth cut likewise found
no carrier with repeats at most one.  Thus palette repair also needs a longer
bridge, reinforcing the direct clean-splice lane.

The clean-splice lane has now closed the final palette/connectivity gate.  A
single used-colour seam first reduced the simple p3 carrier to the exact p2
checkpoint

```text
scratch/k15_mixed_p2_q24.json
SHA-256 f7cf0efa9d84b97b7f2731d6c4db4006e35f93ec84a392231bce5b7f307cf865
2 paths of lengths 343,6092
lower q1 holes/repeats = 3/1; lower q2/q3/q4 holes = 24/5/1
residence defects 0; upper q1,...,q7 all complete
```

An endpoint-first exact beam then found the forced missing-colour final seam:

```text
scratch/k15_clean_p1_q28.json
SHA-256 ba96c6f81098ed73f09f861d9e55283d9374e3426604e05eab0e0c2cd5dabffe
one path through all 6435 middle vertices
lower q1 holes/repeats = 2/1; lower q2/q3/q4 holes = 28/5/1
residence defects 0; upper q1,...,q7 all complete
```

The independent path-cover audit confirms every hard invariant (its overall
status is `FAIL` only because that generic auditor demands a simple q1 palette,
whereas the compiler explicitly permits the one repeat).  Thus connectivity,
residence, every upper shadow, and the exact compiler-payable q1 palette are
all simultaneously closed for k=15.

The first exact Hall audit of this clean p1 is deficiency 41, with 9
zero-candidate targets: 7 of rank 6 and the 2 missing rank-7 faces.  Its outer
endpoint geometry is not yet aligned with those two faces.  The authoritative
best Hall value therefore remains 33 on the bridge-palette p1, but that state
cannot finish until its palette returns.  Hall-aware Posa/DM beams are now
running directly from the clean p1, while p2 beams search for alternative
final seams with better q2 and outer geometry.

The local negative results are now exact through four internal two-opt moves
from the def=33 carrier.  In the palette corridor q1 holes
`8 -> 6 -> 5 -> 4`, the exhaustive state counts are 320, 203, 80, and 0;
no state has Hall deficiency below 33.  Direct p2 one-cut and targeted two-cut
simultaneous splice classes are also palette-invalid.  Further progress must
therefore use Posa/component rotations, a higher-order splice, or a different
clean p1 seam rather than another missed small two-opt.

The clean terminal lane subsequently improved its Hall score without weakening
any hard invariant:

```text
scratch/k15_targetpalette_p1_h37.json
SHA-256 2bc88d1d5b82f854f514311b908f8ccf925fa460670dd024da4e13a0c7c718cc
one path; lower q1 holes/repeats = 2/1; q2/q3 = 28/5
residence defects 0; every upper shadow complete
exact Hall deficiency 37; zero candidates rank 6/7 = 6/2
```

The current global Hall bridge is now stronger than the old deficiency-33
state:

```text
scratch/k15_outer2_p1_h31_bridge.json
SHA-256 f8f09df9617afe1ab441c61f11451a618b04180763f07d6a17e811e1d47ad9fd
independent Hall sidecar SHA-256
  2eed8202393483a0e3bee29816d23dc9b0c48357123d4b4186e87c84b7c95b3e
one path; lower q1 holes/repeats = 4/3; q2/q3 = 22/5
outer endpoint coverage = 2; residence defects 0; every upper shadow complete
exact Hall deficiency 31; zero candidates rank 6/7 = 5/2
```

It is still not a certificate because its exact all-rank Hall deficiency is
positive.  The q1 palette `2/1` is a clean sufficient normal form, but it is
not a theorem about every compiler: row-zero/one/two cells can also realize
rank-seven masks.  Consequently any Hall-zero state is terminal regardless
of its repeat count; palette-first beams are only one complementary lane.

The current exact Hall fronts are:

```text
scratch/k15_targetpalette_p1_h36.json
SHA-256 ce9548d7ddf777471feb06310144dbbb15a93800169ed92d89c20d02556e55ae
q1 holes/repeats 2/1; q2/q3 27/7; Hall 36; res0; all upper exact

scratch/k15_outer2_p1_h30_bridge.json
SHA-256 6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
q1 holes/repeats 4/3; q2/q3 21/5; outer2; Hall 30; res0; all upper exact

scratch/k15_outer2_palette_r2_h31.json
SHA-256 870bc3773461da7f665facddf22e188068dcfe6141b681673e5e848a87e8efc1
q1 holes/repeats 3/2; q2/q3 21/5; outer2; Hall 31; res0; all upper exact
```

### Forced-colour crossover normal form

When two or more carrier paths have an edge union in which every exposed q1
colour has small multiplicity, every singleton-colour edge is forced in any
terminal path using all 6,433 exposed colours.  Contracting the forced
singleton graph leaves a small capacity-constrained connector problem:

* select at least one edge from every non-singleton colour group;
* select exactly `(# forced components - 1)` connectors;
* respect the remaining degree capacity at every middle vertex;
* impose connectivity with lazy subtour cuts, followed by lazy residence cuts.

This is an exact SAT primitive, implemented in
`scratch/search_k15_union_connector_sat.py`.  On the clean q28 / Hall33 union
it contracts 6,435 vertices to 89 nodes.  Exhaustive SAT found exactly four
residence-valid Hamilton selections, all with the same terminal palette,
outer coverage zero, and Hall deficiencies 41 or 42, then proved UNSAT:

```text
scratch/k15_union89_crossover.summary.json
SHA-256 e5edacf5cf59654a67b06ba796955edb6327b9838bb6665593b910f0283276d2
scratch/k15_union89_crossover.best.json
SHA-256 57ef253b181b833d2cfb4e0e13cc6c0a419e2c5228967b036f2aaa740b83de9d
```

Three further exact spaces are closed: terminal-Hall37 with the first outer2
bridge (16 contracted nodes), with the later outer2 bridge (49 nodes), and
with Hall33 (100 nodes).  They contain respectively 11, 11, and 30 valid
terminal paths; none has outer coverage two or Hall below 37.  Authoritative
summaries include

```text
scratch/k15_union16_clean_outer.summary.json
SHA-256 88de90846bd53d9a2d79be6d417ebbe05ff623af5f05b7397ab0e9f82a744ff1
scratch/k15_union49_clean_outer.summary.json
SHA-256 d5db256ba6bb94ca50258cc8b4330b8019fa35adae5e6ed3fce522bde10e0e42
scratch/k15_union100_h37_h33.summary.json
SHA-256 4ca4640e712891bf31d18d9448497b95f9b2f6d9522becfea5646dd94c2d9fab
```

This normal form is reusable: it turns a vague "cross two good paths" idea
into a finite proof-quality census, and prevents compute from being spent on
edge unions whose entire clean crossover space is already exhausted.

### Mixed-seam and full-component update

Positive lower-bound slack permits a central chronology whose consecutive
middle sets are not Johnson-adjacent.  The exact requirement is the
depth-three erosion identity, equivalently the minimum coordinate-run
condition.  A rank-six adjacent intersection is then a literal rank-six
compiler cell even when it is not a natural three-vertex q2 shadow.

From the Hall-31 bridge, three simultaneous upper-safe and residence-safe
rank-six seams produced a four-path mixed carrier

```text
scratch/k15_h31_fourroot_pathcover.json
SHA-256 bd77b8f7005222353346c0ed87440709826b928825d2e671f9898825db51e611
```

with residence zero, every upper shadow complete, and lower q1/q2/q3 holes
`10/24/5`.  One further endpoint rotation exposes a factorable assembly:

```text
scratch/k15_h31_rootmixed_p1_h35.json
SHA-256 6334e26c926d0ff861b6f708ec22926c64ebe77413ebc3ffcfb1752a931f6bf1
Hall 35; q1 holes/repeats 6/3; q2/q3 23/5; res0; all upper exact
```

This does not improve the scalar Hall record, but it is the first terminal
outside the Johnson-only edge unions.  Its exact union with Hall-31 is closed:
only the two source paths survive residence/upper separation.  Its union with
the clean Hall-36 carrier is being enumerated separately.

The mixed-seam insight scales beyond p3/p4.  A census of every saved resident,
upper-exact component carrier found a 46-path source with 216 safe directed
oriented seams.  Its fixed endpoint graph had four forced leaves and was
therefore Hamilton-path UNSAT.  An exact leaf-focused Posa census found a
single invariant-preserving rotation that makes the seam graph connected with
only one leaf (110 safe seams), and eight repaired candidates have at most two
leaves.  Exact orientation/order SAT is now running on those carriers.  This
is the first search that uses the full component-seam capacity rather than
forcing a Johnson Hamilton path first.

### Authoritative Hall-30 / global-segmentation update

The clean terminal lane and bridge lane have improved again:

```text
scratch/k15_terminal_palette_h31_outer1.json
SHA-256 b8f688867544cc62cdc86d1d6f2550bcd83e283f24cd6bfede3c2d639ab6219f
q1 holes/repeats 2/1; outer score 1; q2/q3 22/5; Hall 31

scratch/k15_outer2_p1_h30_bridge.json
SHA-256 6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
q1 holes/repeats 4/3; outer score 2; q2/q3 21/5; Hall 30
```

Both have residence zero and every upper shadow complete.  Hall 30 is the
current global record; no length-6438 word exists yet.

The exact three-component overlay between the Hall-30 path and the earlier
outer-2 Hall-37 path has eight hybrids.  Seven are Hamilton paths, with Hall
values `30,31,33,33,34,35,36`; one is disconnected.  This proves the hybrid
cube is a valid finite neighborhood but refutes Hall additivity and contains
no new record.  Reproducible artifacts:

```text
scratch/audit_k15_open_overlay_hybrids.py
SHA-256 8795dc0e15dfd477f895a2123faf18120406e12036aedd45e2d664f6f05cfcbc
scratch/k15_h30_h37_c3_hybrids.json
SHA-256 b091db161e9afd38d3e59f75006fe54466f55ced9a6c0856c5c43997ebcfbd8a
```

A stronger global neighborhood cuts the Hall-30 chronology itself into many
resident components.  Upper-safe 46/64/96-component segmentations have
connected seam graphs and no forced leaves.  The full 46-component space has
108 Hamilton chronologies and exact best Hall 30; the 64/96 searches remain
active.  The targeted cut specification

```text
scratch/k15_h30_fivezero_targetcuts.json
SHA-256 855be9da36ee3f1bd99538c03bda792699e536ed0adf80fc6a00deb0c66e05ae
```

exposes endpoints whose pairwise intersections are the five persistent
rank-six zero targets.  Exact compiler-aware SAT now uses the same
carrier/mandatory rule as the final Hall audit rather than natural q2/q3
proxies.  On the first targeted 32/46-component sources, hard upper coverage
makes every exposed root arc globally unusable: the exact optimum is zero
selected root arcs and Hall remains 30.  Root `5397` has no individually
upper-safe cut pair; the other four do.  The live refinement therefore builds
an upper-exact four-root-biased segmentation and searches its actual compiler
cells.  This is a genuine compatibility constraint, not a score-tuning issue.

### Open-path overlay theorem and compiler-locality closure

For two spanning middle paths `P,Q`, colour the exclusive edges red and blue
and let `C_i` be the connected components of their symmetric difference.  A
component hybrid selects all red or all blue edges on each `C_i`, retaining
the common edges.  At every vertex in `C_i`, the hybrid degree is exactly its
degree in `P` or in `Q`, according to that component's choice.  Hence every
hybrid is spanning of maximum degree two.  With

```text
delta_i = |boundary(Q) intersect C_i| - |boundary(P) intersect C_i|,
```

the hybrid has `2 + sum_{i selected} delta_i` endpoints.  It is a Hamilton
path **iff** this sum is zero **and** the selected graph is connected.
Endpoint balance alone is insufficient: in the Hall-30/Hall-37 three-component
census, one balanced hybrid is a path plus a disjoint cycle.  Compiler Hall is
global and is not additive across the overlay components.  The exact eight-way
census and checksums are recorded immediately above.

The clean Hall-31/Hall-30 pair and its union with clean Hall-35 admit a still
stronger statewise no-go.  A depth-three compiler candidate cell is local:
an interior row-depth-`d` cell depends on `d+10` consecutive middle vertices;
every boundary cell is determined by an oriented 12-vertex endpoint prefix.
Exhaustive enumeration of every simple local path in each edge union gives:

```text
targets 10794, 17738, 21588:
  interior witness count = 0, 0, 0
  every endpoint prefix witnesses at most one target
```

Thus two endpoints can make at most two of the three targets nonzero.  Every
spanning chronology in either union has at least one zero compiler candidate,
so Hall deficiency zero is impossible regardless of connectivity, residence,
or upper-shadow compatibility.  This closes the requested generalized pair
and triple unions without relying on long SAT enumeration.

```text
scratch/prove_k15_union_zero_capacity.py
SHA-256 df267712c7ef889338b17f5f57a6c6650fb1a1519940e77436ab0b08451f8937
scratch/k15_union_clean31_h30_zero_capacity.json
SHA-256 f9a60a2d0ff72ce267b58a2d7f842eaef40f60e7c1cb4187fb82a63283727e86
scratch/k15_union_clean31_h30_clean35_zero_capacity.json
SHA-256 b2031de20053f4e5c030e47c3473a4f5186a4d07eb23e636162868a4c9f7818c
```

This locality test is now the correct pre-SAT filter: a new carrier should be
added to a crossover pool only if its edge motifs supply interior candidates
for all three persistent roots (or make two of them simultaneously available
at one endpoint).  Otherwise Hall zero is ruled out before chronology search.

### Exact Hall-witness separation

The Hall-30 graph has one canonical alternating DM witness with

```text
|A| = 1528, |N(A)| = 1498, deficiency = 30,
A rank histogram 4:9, 5:82, 6:413, 7:1024.
```

For well-separated resident components, the number of compiler cells adjacent
to any fixed target set `A` decomposes exactly into an intrinsic component
constant plus one weight for every selected seam.  Hence every Hall-zero
chronology satisfies a necessary weighted inequality

```text
intrinsic(A) + sum(selected seam weights for A) >= |A|.
```

`scratch/search_k15_segment_dm_order_sat.py --benders-rounds ...` now iterates
chronology SAT, exact Hall/DM witness extraction, and these weighted cuts.
The first calibration on a 32-component segmentation reproduced the source
gap exactly (`1528-1498=30`), added only 2,464 variables / 19,711 clauses, and
the next SAT call proved UNSAT in 0.098 seconds.  Thus that entire segmentation
contains no Hall-zero chronology; this is an exact family closure rather than
an enumerative failure.

An upper-exact 46-component resource construction now exposes local exact
actions for all seven Hall-zero targets:

```text
scratch/k15_h30_saferootzero46_s10711.json
SHA-256 1aefd186c8f8d1818f24230aa686bdebff8d0aa2c7b130289eb41d6be98cd99b
```

Four rank-six targets are supplied by prescribed seams; one endpoint supplies
rank-seven target `5801`, and the other supplies both rank-six `5397` and
rank-seven `13589`.  Local capacity is therefore no longer the obstruction.
However, hard-requiring all seven actions makes the 46-component path-order
CNF UNSAT, and the exact soft optimum can select only one zero action (Hall
32).  The remaining issue is global action/connectivity compatibility.  Finer
64/96-component action families and Benders separation are the live tests.

### Native portfolio and first Hall-cut closures

The Python hot kernels have native C++20 `-O3 -march=native` replacements:

```text
scratch/build_k15_h30_exactzero_fast.cpp
scratch/fast_k15_hall_dm.cpp
scratch/fast_k15_union_motifs.cpp
```

The segmentation engine is about 73x faster than its unified Python reference
and over 30,000x faster than the legacy natural-root lane.  Hall/DM is about
20x faster, and fixed-target distance batches about 31x faster.  All have
frozen Python regressions.  SAT orchestration remains Python because profiling
shows it is negligible beside Kissat on the hard Hall cuts.

The native builder generated 256 distinct, upper-exact, resident cut/action
topologies in seconds.  Every tested 32- and 46-component topology, and most
64-component topologies, violate the original Hall-30 DM inequality so
strongly that one Benders cut proves the entire chronology family UNSAT.  Some
96-component topologies pass the original cut, but the first new chronology
relocates the obstruction (observed Hall values 51--115) and the second Hall
cut becomes hard.  Adding a q1 corridor is therefore the current exact search,
not merely generating more zero-root actions.

For one rich 64-component topology, preserving all source q1 colours or losing
at most 1, 2, or 3 additional colours is exact UNSAT after the first Hall cut.
Any Hall-zero chronology in that topology must sacrifice at least four source
q1 colours.  This quantifies the lower-palette price of escaping the source DM
block.

The first dense carrier union to pass the compiler-locality prefilter was
Hall-30 plus `k15_p1_2opt_smoke.json`, with internal motif counts
`1850,254,143` for roots `10794,17738,21588`.  Nevertheless, hard-requiring all
three motifs together with degree, residence, and all upper shadows is exact
UNSAT before connectivity.  Individual motif abundance is therefore not the
remaining invariant; simultaneous orientation/degree/upper compatibility is.
