# Exact global rainbow-factor fiber engine for `k=15`

Date: 2026-07-29

Status: exact move theorem, independently audited implementation, a new
strictly improved resident connected carrier, and an analytic zero-hole
PBBS point in the full loop-allowing ambient fiber.  This does **not** prove
`nu(15)=6438`; the best rigorous bound remains

\[
6438\leq\nu(15)\leq6458.
\]

## 1. The implementable fiber

Let `L` be a rotation orbit of rank-seven masks and let `V` be a rotation
orbit of rank-eight masks.  An incidence is a physical extension

\[
L\longrightarrow L+a=V.
\]

There are 429 orbits on each shore and eight incidences at every vertex.
Selecting two incidences at every `L` and two at every `V` is exactly the
strict-equivariant quotient form of

1. one carrier edge for every rank-seven intersection colour; and
2. degree two at every rank-eight middle vertex.

Thus the global fiber in Theorem 3.1 of
`MATH_THEOREM_Q1_RAINBOW_CYCLE_AFFINE_NO_GO_AND_GLOBAL_FACTOR_FIBER_20260729.md`
is the 2-factor fiber of an 8-regular bipartite incidence multigraph.  A pair
of parallel incidences at one lower vertex is a quotient loop and has the
correct weight two at its rank-eight endpoint.

### Exact move theorem

The symmetric difference of two such bipartite 2-factors is balanced at
every vertex and therefore decomposes into alternating even cycles.  Toggling
any union of these cycles preserves both fiber equations identically.

Every bipartite 2-factor decomposes into two perfect matchings `M0+M1`.
Fix `M0` and choose any perfect matching `P` in the incidence graph with the
`M0` edges removed.  Then `M0+P` is another exact point of the fiber, and

\[
P\mathbin\triangle M1
\]

decomposes into independently toggleable alternating cycles.  This is the
implemented global move.  It changes hundreds of lower choices when useful,
while never losing middle ownership or the exact lower-`q1` rainbow.

This move system is complete: for any two fiber points, their symmetric
difference admits the same alternating-cycle decomposition.  No bounded
support claim is used.

## 2. Exact evaluator

For every proposed state the C++ engine expands all 429 selected edge orbits
to the 6,435 physical Johnson edges.  It then checks, from scratch:

* two selected incidences at every quotient vertex;
* physical degree two at every rank-eight mask;
* physical component count and sizes;
* every cyclic coordinate-run length and the depth-three residence condition;
* upper-`q1` loads from edge unions;
* lower-`q2` loads from the intersection of the two turns at each middle
  vertex; and
* upper-`q2` loads from the union of the same three middle vertices.

The lower-`q2` and upper-`q2` turn colours are independent of component
orientation, so no arbitrary orientation enters their evaluation.

The independent Python auditor reconstructs the physical factor through the
repository's stable `QuotientCatalogue`, recomputes all three shadow counts,
and compares them to the engine's claims.  A connected resident non-loop
candidate is emitted in `graded-quotient-carrier-v1` format, directly usable
by

```text
python3 scratch/graded_quotient_pipeline.py compile CARRIER \
  --word WORD --audit AUDIT
```

The compiler still performs its own carrier/shadow/Hall checks.  Candidate
export is not a claim of compiler SAT.

## 3. Calibration and first new candidate

The authoritative strict seed calibrates exactly as

```text
components=1, residence_bad=0, minimum_run=4,
upper-q1 physical/orbit holes = 995/67,
lower-q2 physical/orbit holes = 685/47,
upper-q2 physical/orbit holes = 405/27.
```

A deterministic five-second local run (`seed=991`, 2,000 matching proposals)
found and independently replayed

```text
components=1, residence_bad=0, minimum_run=4,
upper-q1 physical/orbit holes = 890/60,
lower-q2 physical/orbit holes = 595/41,
upper-q2 physical/orbit holes = 405/27.
```

The combined physical `q1/q2` deficit drops from 2,085 to 1,890 while
connectivity and residence remain exact.  The stable quotient replay reports
nonzero spiral voltage 8.  This is a genuine state outside the previously
audited small-support closure.

A second exact stage started from a resident eight-component factor with much
lower shadow load, increased the component penalty, and merged it back to one
physical cycle.  The independently replayed connected result is

```text
components=1, residence_bad=0, minimum_run=4,
upper-q1 physical/orbit holes = 510/34,
lower-q2 physical/orbit holes = 380/26,
upper-q2 physical/orbit holes = 318/22.
```

Its combined deficit is 1,208, a 42.1% reduction from the strict seed's 2,085.
This also demonstrates that the component count is not frozen by the global
fiber moves: a low-shadow multi-factor can be reconnected while keeping exact
residence.

### Exact collision-floor objective

There are 429 quotient labels in 335 upper-`q1` bins and likewise 429 labels
in 335 lower-`q2` bins.  If `P+` and `P-` are their pair-collision counts,
then 94 is the integrality floor for either deck and

\[
\Xi=P_++P_--188\ge0.
\]

In the present live rank-exact face, `Xi=0` forces both quotient decks to be
complete and floor-balanced.  Moreover `Xi` dominates the sum of their hole counts, so it is
a smoother exact primary objective than the terminal physical-hole count.
The engine now supports `--collision-primary --collision-weight C`, and the
independent physical-lift auditor recomputes all three collision numbers.

The strict seed has `(P+,P-,Xi)=(206,159,177)`.  The first connected phase-2
carrier has `(151,139,102)`.  A short collision-primary calibration from the
low-shadow factor reached `Xi=91` while retaining exact residence; the H100
CPU portfolio is continuing this phase.

The first collision-primary portfolio subsequently reached a resident
three-component point with `Xi=55`, then an exact matching move reconnected it.
The independently audited connected carrier has

```text
(P+,P-,Xi) = (130,115,57),
upper-q1 holes = 360 physical / 24 quotient,
lower-q2 holes = 225 physical / 15 quotient,
upper-q2 holes = 288 physical / 20 quotient,
minimum run = 4, physical components = 1.
```

The stable full carrier audit gives nonzero voltage 4, 13 lower-`q3` orbit
holes, and 49 all-upper orbit holes (ranks 9/10/11: 24/20/5), compared with
11 and 95 for the original strict seed.  Thus the global moves improve the
actual all-upper gate as well as their explicit `q1/q2` objective, while the
lower-`q3` gate remains essentially flat.

Retained artifacts:

* `scratch/k15_global_rainbow_factor_collision_merge405_best_20260729.json`
  (`sha256 e7e205bb322411351a6f169ee75eb454c040e43a6edc1d5962df210a8c1de238`)
* `scratch/k15_global_rainbow_factor_collision_merge405_best_20260729.audit.json`
  (`sha256 b39a83b06f355a7cdcfb0479938ec0b50c51253ea49330de017b3fe8ee2da169`)
* `scratch/k15_global_rainbow_factor_collision_merge405_best_20260729.carrier.json`
  (`sha256 6ef4042a329278699156ca0c4a7874bb5ed878a0d41096f28f61e7576aa7b512`)

A later reconnection pass improved the connected collision score to

```text
(P+,P-,Xi) = (127,108,47),
upper-q1 holes = 390 physical / 26 quotient,
lower-q2 holes = 165 physical / 11 quotient,
upper-q2 holes = 318 physical / 22 quotient,
minimum run = 4, physical components = 1, voltage = 11.
```

Its lower-`q3` and all-upper orbit-hole counts are 12 and 56.  Artifacts:

* `scratch/k15_global_rainbow_factor_collision_merge408_best_20260729.json`
  (`sha256 4d7cd2d109e1c0d341c23c5f3438bb482cbff999e41f69dbe85b48bb0ee07181`)
* `scratch/k15_global_rainbow_factor_collision_merge408_best_20260729.audit.json`
  (`sha256 9162cc79caab3d7c88a18328b63f2ac1bca8673824d1eb3441fde7f4a0dc9cd5`)
* `scratch/k15_global_rainbow_factor_collision_merge408_best_20260729.carrier.json`
  (`sha256 fe47e2e31641be8b1b5d7abd6030340a75a2e5444cf093fc0ea71483ceeb27ff`)

Holding `Xi=47`, a connected continuation improved the terminal physical
counts to upper-`q1`/lower-`q2`/upper-`q2` = `360/180/303`, with quotient
holes `24/12/21`, voltage 2, lower-`q3` holes 12, and all-upper holes 53.
This is the current strongest connected carrier by the engine's lexicographic
collision/terminal score:

* `scratch/k15_global_rainbow_factor_collision_connected409_best_20260729.json`
  (`sha256 bef085c91dd68db6e7322387a4ad14997a14fbda6d393dc1fd9f4ca9c3887a9c`)
* `scratch/k15_global_rainbow_factor_collision_connected409_best_20260729.audit.json`
  (`sha256 617f9adc987dc1d106b364af571b7890f29313e8204bcab4df1f686d9d69f825`)
* `scratch/k15_global_rainbow_factor_collision_connected409_best_20260729.carrier.json`
  (`sha256 8997633a1998e82ff05754a83c15d096cbbc2f001fa381b06c792f55f90b439d`)

The converse needs a qualification: complete decks can still have `Xi>0` if
some bin has load at least three.  The fixed-matching SAT factors below are
explicit examples, with both decks complete but `Xi=18` and `Xi=28`.
Therefore the unconditional statement is

```text
Xi = 0  =>  both decks complete and floor-balanced,
Xi >= total quotient holes,
```

while “complete implies `Xi=0`” is valid only on a cap-two/floor-balanced
face.  The engine uses `Xi` as a smooth stronger objective, not as an
unqualified equivalence.

The exact identity behind the qualification is useful.  For `B=429` labels
in `n=335` bins, let `h` be the number of empty bins and `l_A` the positive
loads.  Then

\[
 P-(B-n)
 =h+\sum_{A:l_A>0}{l_A-1\choose2}.                 \tag{1}
\]

Indeed `B-(n-h)=94+h` is the total excess above one on occupied bins, and
`binom(l,2)-(l-1)=binom(l-1,2)`.  Summing (1) for the two decks gives

\[
 \boxed{\Xi=h_++h_-+
   \sum_A{l_A^+-1\choose2}+
   \sum_A{l_A^--1\choose2}.}                       \tag{2}
\]

Thus `Xi` is not merely a bound: it is exactly “holes plus triple-and-higher
collision excess.”  This is why it gives a smoother descent while preserving
the correct zero set of complete cap-two decks.

## 3.1 Fixed-matching exact macro and residence CEGAR

After fixing `M0`, a candidate edge of the second perfect matching has two
local labels: its upper-`q1` colour at the lower shore and its lower-`q2` turn
colour at the middle shore.  Requiring a perfect matching that covers every
orbit of both labels gives an exact CNF with approximately 3,000 variables
and 19,500 clauses.

Kissat found SAT points from both the strict seed and the connected phase-2
carrier.  Both have zero upper-`q1` and zero lower-`q2` holes.  Their remaining
geometry is poor:

| parent | SAT components | residence violations | `Xi` |
|---|---:|---:|---:|
| strict seed | 20 | 1,425 | 18 |
| connected phase 2 | 11 | 1,110 | 28 |

The matching differences have only ten alternating components of supports
`1,2,3,3,4,12,18,77,114,137`, and five components of supports
`3,19,58,105,180`, respectively.  Exhausting all `2^10+2^5=1056` hybrids
found exactly one resident point in each cube: the original parent.  Thus
these particular exact-deck endpoints cannot be interpolated back to
residence by choosing a subset of their matching cycles.

A sound residence CEGAR now addresses this directly.  A short positive run
of length at most three is fixed by the selected matching variables on the
transition immediately before it and on every transition leaving one of its
vertices.  Their joint negation is a clause of width at most four.  Exact
degree two makes the clause sound: retaining all those edge orbits retains
the same bounded bad path regardless of the rest of the matching.  The CEGAR
adds all fresh motif clauses and resolves the exact double-shadow matching.
It is running on the H100 CPU.

Additional artifacts:

* `scratch/k15_fixed_matching_double_shadow_sat_20260729.py`
* `scratch/k15_fixed_matching_residence_cegar_20260729.py`

Artifacts:

* `scratch/search_k15_global_rainbow_factor_fiber_20260729.cpp`
* `scratch/export_k15_global_rainbow_factor_fixture_20260729.py`
* `scratch/k15_global_rainbow_factor_seed_20260729.txt`
* `scratch/audit_k15_global_rainbow_factor_candidate_20260729.py`
* `scratch/k15_global_rainbow_factor_seed991_best_20260729.json`
  (`sha256 f75d962a39afc4eeab675cac220336e4e2a57c5a9a5b532cca95c70c9dba10a3`)
* `scratch/k15_global_rainbow_factor_seed991_best_20260729.audit.json`
  (`sha256 f4694ed4914911446255ba161822fdd5e7d7c5722667e109f277922348e3357c`)
* `scratch/k15_global_rainbow_factor_seed991_best_20260729.carrier.json`
  (`sha256 a943f5c0e8a50157a753e594567357d41917805f24bc4fb25ae443d4355aea60`)
* `scratch/k15_global_rainbow_factor_phase2_301_best_20260729.json`
  (`sha256 d2ea86cb2a9b016238b26779a19b765e8c8d09b022b0f743dbdacf17c89e7446`)
* `scratch/k15_global_rainbow_factor_phase2_301_best_20260729.audit.json`
  (`sha256 05ae4725f04116126840744e45dc473f67e84620617ac1e13748f99e92872629`)
* `scratch/k15_global_rainbow_factor_phase2_301_best_20260729.carrier.json`
  (`sha256 8868f6a4df0628d5a0fe3aaabb8b9449a198326daac41085a768110a77d0bb0a`)

## 4. Commands and soundness boundary

Calibration:

```text
c++ -O3 -DNDEBUG -std=c++20 \
  scratch/search_k15_global_rainbow_factor_fiber_20260729.cpp \
  -o /tmp/search_k15_global_rainbow_factor
/tmp/search_k15_global_rainbow_factor --calibrate-only
```

Independent replay:

```text
python3 scratch/audit_k15_global_rainbow_factor_candidate_20260729.py \
  scratch/k15_global_rainbow_factor_seed991_best_20260729.json \
  --audit /tmp/audit.json --carrier-output /tmp/carrier.json
```

Heavy search is running only on the H100 pod's CPU under
`/home/amodo/or15/global_rainbow_factor_20260729`; the GPU is unused.

The default search face excludes the 14 quotient-loop pairs so that every
retained candidate has an immediate stable compiler representation.  The C++
engine can audit the full loop-containing fiber with `--allow-quotient-loops`,
but the current Python/compiler adapter deliberately rejects such candidates
until a weighted-loop serialization is independently implemented.  Therefore
the engine is exact on the searched non-loop face, and its move theorem is
exact on the full multigraph fiber; it does not claim that the default face is
connected.

Finally, neither the C++ evaluator nor the independent audit proves lower
compiler Hall, lower `q3`, or all deeper upper shadows.  Those remain guarded
downstream gates.  A final solution requires an independently verified
length-6,438 word, not merely a low shadow score.

## 5. Relation to the binary-trace `c`-space lane

There is no contradiction with Claude's strict voltage-spiral reduction.
Every connected resident candidate retained here is equivariant and has
coprime nonzero voltage (the current best has voltage 4), so it is precisely a
single binary trace with transversal run starts and ends in that formulation.
The factor engine is a different coordinate system and a global move set on
the same strict objects: it preserves middle ownership and lower `q1` before
reconstructing the trace.

The exact double-shadow SAT endpoints are different.  They are generally
multi-component and have hundreds of short residence runs, so they do **not**
claim a valid one-trace `c`-space solution.  They prove that the two shadow
decks are jointly feasible in the ambient exact factor fiber once the global
trace/residence constraint is omitted.  The residence-motif CEGAR is exactly
the bridge back: its width-at-most-four clauses are the factor-coordinate
form of forbidding the corresponding short age motifs in `c`-space.

Thus the two lanes localize the same remaining obstruction rather than giving
conflicting evidence.  Claude's current search has no new `PASS`; the global
factor results show that shadow feasibility itself is not the missing theorem,
while trace-compatible shadow feasibility still is.

## 6. PBBS closes raw shadow feasibility analytically

Let `f` be the canonical PBBS permutation on rank-seven masks.  The two
perfect incidence matchings

```text
M+(A) = complement(f(A)),
M-(A) = complement(f^(-1)(A))
```

belong to the full ambient fiber.  At a lower owner `A`, their upper pair
has union `theta(A)^c`; at the upper owner `A^c`, their two lower neighbours
intersect in `theta(A)`, where

```text
theta(A) = f^(-1)(A) intersect f(A).
```

The audited PBBS first-shadow theorem makes both palettes hole-free.  Their
common quotient load histogram is exactly

```text
load 1: 244 target orbits
load 2:  88 target orbits
load 3:   3 target orbits
```

The factor has 59 quotient components (73 physical components) and uses two
of the fourteen quotient-loop pairs.  It is therefore outside the default
loop-free resident connected face, but it is an exact point of the full
fiber.  More strongly, the audited PBBS path theorem gives correct-window
support at every lower and upper depth of this factor.

Accordingly, the engine's remaining mathematical target is not ambient
shadow feasibility.  It is the intersection of zero-hole/all-depth support
with the loop-free, connected, coprime-voltage, resident, safely openable,
compiler-compatible face.  The complete proof is in
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`.
