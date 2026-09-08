# Binary-10 involution gate: model and scope

Status: no 42-row full-cube cover has yet been verified. Two selected cores
(indices 2 and 29 below) now have exactly verified rational fractional
completion certificates. Other LP outcomes remain numerical reports.
The earlier 30-second local integer run
returned `UNKNOWN`. All subsequent heavy computation is restricted to
explicit `ssh h100`, as required by `COMPUTE_POLICY_20260907.md`.

## Literal finite object

A row is two ordered, disjoint five-tuples partitioning coordinates `0,...,9`.
Its targets are the 36 unions of one prefix of each tuple, including empty
prefixes. It contains exactly 5, 6, 5 targets of ranks 4, 5, 6. Thus a 42-row
cover of all 1024 targets must partition each of these three ranks exactly.
In particular, the 42 unordered shore splits must be distinct: every row
contains both whole shores among its rank-5 targets.

The finite gate is constructive and independently checkable. A feasible LP,
a solver objective, or a timeout does not establish it. Its implication for
the asymptotic constant is recorded separately in
`EXIT_CLOCK_MOMENT_BOUND_AND_TEN_AXIS_THRESHOLD_20260907.md`.

## Symmetry reductions

The action cycling coordinates `0,...,6` and fixing `7,8,9` cannot support an
optimal invariant cover. Any row covering the fixed triple `{7,8,9}` also
contains its two distinct immediate prefix extensions by moving coordinates.
These rank-4 targets lie in the same cyclic orbit. Developing the row repeats
a tight target. Hence this symmetry is rejected analytically, not by timeout.

Instead use the involution `i <-> i+5`. There are 528 target orbits, including
110, 126, 110 orbits at the tight ranks. A fixed row has the form

```
(x_1,...,x_5) | (tau(x_1),...,tau(x_5)),
```

where the five labels represent the five swapped pairs. Up to exchanging
shores there are `5! * 2^4 = 1920` fixed rows.

Every invariant 42-row cover must use exactly ten fixed rows and sixteen
nonfixed row orbits. Indeed, the twenty fixed tight targets are the ten unions
of two coordinate-pairs and the ten unions of three pairs. A fixed row covers
one of each. A nonfixed row orbit containing a fixed tight target repeats it
and is forbidden. The fixed incidences therefore form a perfect matching
between the two- and three-subsets of the five pair labels, using containment.

A nonfixed admissible row orbit cannot have a transversal shore split (one
coordinate from each pair), since its two whole shores are involution partners
already appearing in the same seed row. The ten fixed rows use ten of the
sixteen transversal shore splits. Nonfixed rows use the 55 involution pairs of
nontransversal shore splits.

Do not additionally impose closure under set complementation. Complementing
a row reverses both shore orders but preserves its whole-shore middle targets.
For five-element shores the complementary row is distinct, so including both
would repeat middle targets. This differs from coordinate involution symmetry.

## Reproducible catalogue and restricted core

Sources:

- `binary10_involution_catalogue_20260907.cpp`: exhaustive permutation-orbit
  catalogue, rejecting any orbit that repeats a tight target.
- `binary10_involution_scd_core_20260907.py`: deterministic ten-fixed-row core.
- `binary10_involution_completion_20260907.py`: complete residual LP and optional
  integer exact-cover test, followed by literal coverage verification.

The complete catalogue has 908160 canonical row orbits: 1920 invariant rows
and 906240 nonfixed row orbits before tight-collision filtering. The valid pool
contains all 1920 invariant rows and 501120 nonfixed orbits.

The prescribed ten-row core covers 312 distinct targets, including 160 distinct
tight targets and all twenty fixed tight targets. Exactly 36196 nonfixed row
orbits avoid its tight targets. None have identical residual support. They
must cover 356 remaining target orbits, of which 256 are tight.

The residual LP imposes equality one on every tight orbit and lower bound one
on every other orbit. Each remaining column has weight two. Every feasible
solution would have objective 32, because the tight equalities force that
objective. Both initial LP runs returned numerical fractional solutions; the
remote run had 269 positive columns. Without exact rational verification,
these are numerical evidence of fractional extendability, not a proved
fractional construction and certainly not an integral construction.

The integer model retains all these target constraints and requires total
weight 32. Any successful solver output is expanded into 42 literal rows,
then independently checked to cover every integer mask `0,...,1023` with
exactly one occurrence of each rank-4, rank-5, and rank-6 target. Only that
post-check prints `VERIFIED_FULL_COVER`.

The first remote 900-second integer run used PID 3302359 in
`/home/amodo/or-research-20260907-QiqXT3/`. The recorded stdout reached the
fractional LP result above. Subsequent remote process checks found no remaining
solver, but the original SSH session remained open without a final integer
status. Its result is therefore **unretrieved**, not certified `UNKNOWN`,
`INFEASIBLE`, or feasible. There was no durable remote run log in that attempt.
No literal witness has been retrieved from it. Future runs should save remote
stdout and exit status and disable unnecessary SSH forwarding.

## Constructive cores and completed all-60 screen

`BINARY10_ALL_FIXED_MATCHINGS_CORE_LEMMA_20260907.md` proves that every fixed
incidence matching admits a tight-disjoint invariant core, with no search.
It also proves the tournament sink obstruction and related local conditions.
These analytic results are distinct from the numerical LP outcomes below.

The matching generator uses a regular first-pair tournament and a canonical
valid last-label assignment. Its names `6`, `24`, and `30` refer to three
selected representatives of abstract matching types, **not** to exhaustive
joint matching/tournament/last-label symmetry classes. Once the tournament is
fixed, relative placement matters. Accordingly, all sixty labelled matchings
were screened with the literal canonical conventions.

The durable all-60 screen is
`/home/amodo/or-research-20260907-QiqXT3/run-all60-Kl6mO4/` on h100. It retains
all-rank residual constraints and produced:

| Numerical LP report | Number of cores |
| --- | ---: |
| Optimal, fractional primal returned | 7 |
| Infeasible | 32 |
| Unknown (status 4 / HiGHS model status 15) | 21 |

The seven numerical-feasibility indices are `2,7,12,29,35,46,50`. Index 2 has
incidence permutation cycle type `2+8`; the other six have five 2-cycles.
Index 29 is the unique matching invariant under cyclic permutation of the
five pair labels. These infeasibility reports have not been independently
converted to rational Farkas certificates; the unknown cases are not treated
as infeasible. All sixty process exit codes were zero. Source snapshots,
per-core logs, and `summary.json` preserve the exact scope.

The regular representative named `6` is index 7. Its durable integer run in
`run-regular6-FNdK8E/` returned `UNKNOWN` after 912.270342501 seconds, with a
900-second requested solver cap and shutdown overhead. It produced no witness.
The increasing-first-order version of that representative had an exact
catalogue omission certificate for masks 373 and 496; that is a statement
about that particular core, explained by the sink obstruction.

The next two bounded integer attempts use genuinely different cores, index 2
and index 29, each with sixteen workers and a 900-second cap. Their durable
directories are `run-index2-iUxh3U/` and `run-index29-ueYal1/` under the same
remote parent. Each saves `lp_primal.json` with the literal core and every
nonzero numerical primal column/value for later rational checking, plus
`output.log`, source snapshots, and an explicit `exit.status` on completion.
Only a retrieved `VERIFIED_FULL_COVER` followed by independent literal checking
would establish the finite gate.

### Exact fractional certificates for the two selected cores

The saved numerical supports for indices 2 and 29 were promoted to exact
rational certificates. Numerical QR selected square independent systems of
263 and 264 binding target equations; FLINT then solved those integer systems
over the rationals. The verifier subsequently checked every literal row and
all original constraints exactly: nonnegative weights, equality on every
tight orbit, lower bound one on every other required orbit, and physical
residual row charge exactly 32. Thus these two specific cores do have proved
fractional completions. The integral selection problem remains open.

The complete certificates are local artifacts
`binary10_exact_fractional_index2_20260907.json` and
`binary10_exact_fractional_index29_20260907.json`. They retain all literal rows
and rational weights (denominators up to 43 and 49 digits, respectively).
`binary10_verify_fractional_primal_20260907.py` directly verifies the stored
rationals using only exact integer/fraction arithmetic; reconstructing the
certificate from its numerical precursor additionally uses QR and FLINT.
This is a certificate for the fixed-core fractional problem, not a new
unrestricted fractional optimum or a 42-row integral word.

A negative result for this model would exclude only completion of this fixed
core. It would not exclude another invariant core, an unrestricted 42-row
cover, or the coefficient-one conjecture.

## Later exact diagnostics and integer status

For index 2, the complete integer model returned `INFEASIBLE` after
66.562660565 seconds. This remains a solver-reported exclusion of that literal
core: no independent proof trace or combinatorial impossibility certificate
has been extracted. In particular, the note does not claim an independently
proved fractional/integral separation solely from that report. Index 29's
bounded integer run returned `UNKNOWN` after 905.480965412 seconds, with
durable exit status zero and no retrieved integral witness.

The exact GF(2) diagnostic in `binary10_tight_parity_20260907.py` was run on all
literal admissible columns, not just the fractional supports. Index 2 has
27368 columns and index 29 has 29615; both tight-orbit matrices have rank 245
over GF(2), with 256 rows. The all-ones demand lies in the column span in each
case. Thus this particular tight-rank parity obstruction is absent. This
neither proves integral feasibility nor weakens the all-rank requirements.
