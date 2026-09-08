# Thread D: exact r99 cut-only double-repair capacity payload

**Date:** 2026-07-29  
**Status:** exact model and fail-closed replay interface; no new solve launched.

## The necessary relaxation

Let `F` be the frozen 858-edge source factor and let `x_e` indicate a
radius-99 source cut.  The cut is constrained to the retain-22511 or
delete-22511 branch and must hit all 147 current residence motifs.  For every
loopless off-source seam `a` whose lower and upper q1 colours have respective
unique source providers `e_L(a),e_U(a)`, introduce `y_a` and impose

\[
y_a\le x_{e_L(a)},\qquad y_a\le x_{e_U(a)}.
\]

Selected `y` seams are separately a matching in their lower colours and in
their upper colours.  At every quotient node `v` they also obey

\[
 \sum_{a\ni v}y_a\le \sum_{e\in F:e\ni v}x_e.
\]

Every exact degree-balanced both-q1 radius-99 completion induces a feasible
point.  Hence an optimum below 14 in the retain branch, or below 12 in the
delete branch, would exclude that branch.  The converse is false.

The literal model has:

- 858 source-cut bits and 20,787 `y` bits;
- one radius row, one branch lock, and 147 motif rows;
- 41,561 deduplicated provider-activation rows;
- 675 lower-colour and 673 upper-colour matching rows;
- 858 endpoint-capacity rows;
- 21,645 variables and 43,916 constraints in total; and
- the pure objective `maximize sum(y)`.

It deliberately omits the legacy dynamic-demand row and does not optimize a
slack surrogate.

## Exact positive audit of this relaxation

The frozen Pareto row-halo certificate already contains a literal feasible
`y` packing of size 21 in each branch.  The new builder replays those cut and
seam IDs before accepting them as hints.  Therefore

\[
\operatorname{OPT}_{\rm retain}\ge21>14,
\qquad
\operatorname{OPT}_{\rm delete}\ge21>12.
\]

Thus this relaxation cannot itself prove r99 q1 infeasibility.  Its optimized
cut can only be a targeted hint for the residual exact seam/degree/q1 model.

The two already-running legacy jobs subsequently terminated with FEASIBLE
incumbents of size 61 in both branches (neither run proved optimal).  Their
result files were copied and independently replayed:

| branch | result SHA-256 | `(lost lower,lost upper)` | cut-dependent demand | `|y|` |
|---|---|---:|---:|---:|
| retain | `cc6d4efebcb1e4d33a6a49205a7caa46215afc61d87940839d8dae895e306c49` | `(76,86)` | 63 | 61 |
| delete | `fe9d5bad18df34c3a47cd62d8f22c668c600888a2050d6bf5b0dfa2d4e6a1cb5` | `(78,84)` | 63 | 61 |

The legacy delete payload is not canonically round-trip hashable: its writer
hashed integer-keyed histograms before JSON converted those keys to strings.
A naive parse/reserialize digest therefore differs.  The replay reconstructs
the typed histogram keys and exactly recovers the stored writer digest, so
this is a legacy schema defect rather than evidence of post-write mutation.

Both literal replays pass all cut, motif, provider, colour-matching, and
endpoint-capacity checks.  However, each displayed `y` family falls two short
of its cut-dependent inclusion--exclusion demand.  Thus the displayed
cut/`y` pairs are not full-completion witnesses.  Because neither run proved
optimal, the cuts themselves may still admit two further double repairs; they
remain diagnostic candidates, while the canonical minimum-loss size-21 hints
are better aligned with residual completion.  Literal replay of the two
61-seam families gives the rigorous lower bound 61 for each relaxation
optimum.

## Reproducible payloads

The builder is

```text
scratch/threadD_build_k16_r99_cutonly_double_capacity_20260729.py
```

It fail-closes on the source, cut-space, Pareto-row-halo, catalogue digest,
and catalogue-module hashes.  Build output records the driver and module
hashes, OR-Tools version, exact argv and shell command, host, solver
parameters, pre-solve proto hash, incumbent, best bound, and a literal replay
of every emitted cut/`y` witness.  `--build-only` exports the proto without
starting CP-SAT; incumbent and bound are then explicitly null.

The independent result replay is

```text
scratch/audit_threadD_k16_r99_cutonly_double_capacity_result_20260729.py
```

It accepts the new schema and both retained legacy result schemas.  In
particular, a legacy FEASIBLE result may omit a proto, but it is accepted only
after reconstructing the frozen 20,787-seam domain and literally checking
radius, branch, all motif hits, both provider implications, both colour
matchings, endpoint capacities, and the reported objective.  Missing proto
provenance is reported rather than silently inferred.

No additional CP-SAT run was launched while the H100 allocation was
saturated; the two reported jobs were the already-running legacy jobs.  A
build-only proto is not a solver certificate, and `FEASIBLE` is not an upper
bound on this maximization problem.

The hardened builder's proto export is deferred because no new H100 build
slot was assigned and local OR-Tools is unavailable.  The source fail-closes
on the expected 21,645-variable/43,916-row census; no proto hash is claimed in
this iteration.

The retained legacy outputs and replays are under
`scratch/threadD_k16_r99_cutonly_double_capacity_20260729/`.  They have no
serialized proto and no best-bound field; the replay records both omissions
explicitly.

One provenance subtlety is now audited.  A naive parse/re-serialize hash of
the delete JSON gives `eb8eff34...`, not its stored payload digest
`4d411df3...`.  This is not post-write mutation: the legacy writer hashed
Python dictionaries while the local-cost histogram keys were integers, then
JSON converted those keys to strings.  Restoring exactly those known typed
histogram keys reproduces `4d411df3...` byte-for-byte.  The retain payload
reproduces its stored `82e77980...` digest both ways because its realized key
ordering does not expose the distinction.  The replay files record both the
round-trip and exact legacy-writer checks.
