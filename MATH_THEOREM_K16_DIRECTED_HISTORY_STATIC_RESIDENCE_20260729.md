# Exact directed-history encoding for the unrestricted K=16 factor gate

## Scope

The target in this note is an arbitrary spanning simple 2-factor of
`J(16,8)` which

1. covers every rank-7 intersection colour;
2. covers every rank-9 union colour; and
3. has every nonconstant coordinate-1 run of cyclic length at least four.

This is the current PBBS carrier gate only.  A passing factor would still
need the deeper-shadow and lower-compiler audits before it became a word of
length `12873`.

The implementation is

```text
scratch/solve_k16_q1_augmented_catalogue_residence_cegar_20260729.py
```

under `--static-directed-residence`.  It removes motif CEGAR entirely.

## Directed-history theorem

Orient every component of a selected 2-factor.  Write

```text
add(u,v)  = the unique coordinate in v\u,
drop(u,v) = the unique coordinate in u\v.
```

At a vertex `v`, let `h_j(v)` be the coordinate inserted on the transition
which occurred `j` steps before reaching `v`, for `j=1,2,3`.  If `p(v)` is
the directed predecessor, then

```text
h1(v) = add(p(v),v),
h2(v) = h1(p(v)),
h3(v) = h2(p(v)).
```

**Theorem.**  Every coordinate-1 run has length at least four if and only if

```text
drop(v,s(v)) != h1(v), h2(v), h3(v)
```

at every vertex `v`.

**Proof.**  A coordinate run ending on the transition `v -> s(v)` has length
`j <= 3` precisely when that coordinate was most recently inserted `j`
transitions ago.  This gives one of the three displayed equalities.  In the
other direction, equality with one of the last three insertion labels says
that the coordinate was inserted at most three transitions ago.  It cannot
be inserted again while present, so its current run has length at most three.
Coordinates constant on a component are never inserted or deleted and are
correctly unconstrained.  The argument is cyclic and also covers components
of lengths three and four.  QED.

The same coordinate can occur twice among the three historical labels when
two short runs are separated by a short gap.  This creates only a redundant
inequality: the most recent occurrence is the current run's start.  The
solver-free regression audit accounts for this explicitly.

## CP-SAT formulation

For each physical Johnson edge `{u,v}` the model has two directed literals
`u->v` and `v->u`, whose sum equals the undirected selection literal.  One
incoming and one outgoing arc at every vertex orients every component and
precludes directed 2-cycles because an undirected edge can receive only one
orientation.

For every vertex the predecessor is a 64-way integer choice.  Two `Element`
constraints propagate `h2` and `h3`; three disequalities impose the theorem.
Thus the full unrestricted model has

```text
catalogue edges                 411,840
directed arc Booleans           823,680
history/predecessor integers     64,350
total model variables         1,299,870
total high-level constraints    576,292
motif CEGAR rows                      0
```

The build took `15.95 s` and peaked at `1,489,652 KiB` on `arboghast` under a
16 GiB address-space guard.  Frozen build artifact:

```text
/dev/shm/k16_fl3/scratch/k16_full_johnson_static_directed_build_20260729.json
```

The first long full solve hit `std::bad_alloc` after about 3:05 under a 16 GiB
address-space guard (peak RSS about 13.98 GiB).  It is recorded only as
`RESOURCE_LIMIT`, never as UNSAT.  The identical audited model is currently
running as `k16_fulljohnson_static_directed_32g_20260729` with a 32 GiB OS
guard, 28 GiB OR-Tools limit, two workers, and 1800 seconds.  It has not yet
returned a verdict.  Therefore this note claims neither SAT nor UNSAT.

A one-second, one-worker solver smoke test (19.32 seconds including model
construction) accepted the complete canonicalized hint and returned
`UNKNOWN`, not `MODEL_INVALID` and not `RESOURCE_LIMIT`, with peak RSS
2,533,872 KiB under a 12 GiB address-space guard.  Frozen provenance:

```text
scratch/k16_full_johnson_static_directed_smoke_20260729.json
scratch/k16_full_johnson_static_directed_smoke_20260729.resource.txt
```

## Sound symmetry breaking

For the full Johnson catalogue only, S_16 transitivity lets us fix the
oriented edge

```text
255 -> 383.
```

The stabilizer of this ordered edge has exactly three orbits on its possible
predecessor.  Representatives are

```text
639, 447, 703.
```

Requiring the predecessor to be one of these three retains an isomorphic copy
of every solution.  A resident factor hint is relabelled by an explicit
ground-set permutation so that both symmetry rows and its complete directed
history are consistent.

The older `--initial-hint` interface remains backward-compatible for dynamic
CEGAR.  In static mode it is promoted to the stronger history-consistent
hint.  Supplying a conflicting `--initial-hint` and `--static-hint` is rejected
before model construction.

## Independent regression evidence

The solver-free audit

```text
scratch/audit_k16_directed_history_residence_encoding_20260729.py
scratch/k16_directed_history_residence_encoding_regression_20260729.audit.json
```

checks:

* all 126 directed simple Johnson cycles on subsets of the six vertices of
  `J(4,2)` (394 canonical ordered candidates before adjacency filtering);
* the authoritative K=16 both-q1 factor, reproducing exactly
  `132/904/1186` runs of lengths `1/2/3`, total `2222`;
* the authoritative K=16 resident factor, reproducing zero violations; and
* the canonical symmetry relabelling, with predecessor `703` and unchanged
  residence audit.

It passes all checks.

As a plumbing regression, the restricted 25,349-edge Q/R catalogue was built
with 140,397 variables and 189,799 constraints, then proved `INFEASIBLE` in
6.71 seconds with peak RSS 841,808 KiB under a 4 GiB hard guard.  This agrees
with the independently known exact-overlay no-go; it is not used as evidence
about the unrestricted full-Johnson model.

The matching positive regression disables q1 coverage and supplies the known
resident factor through the backward-compatible `--initial-hint resident`.
Static mode promoted it to the complete directed-history hint and returned
the literal two-component resident factor with zero residence violations:

```text
scratch/k16_static_directed_resident_positive_regression_20260729.json
scratch/k16_static_directed_resident_positive_regression_20260729.resource.txt
```

It returned `PASS/OPTIMAL` in 24.06 solver seconds (27.17 seconds total), peak
RSS 1,767,916 KiB under a 4 GiB hard guard.  Its 492 lower and 698 upper q1
holes are expected because this regression deliberately used `--q1-mode none`.

## Capped full command

The intended comparison run is CPU-only and must be launched on `h100` with
at most four workers and a hard address-space/time guard, for example:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
timeout 2400 prlimit --as=12884901888 -- \
python3 scratch/solve_k16_q1_augmented_catalogue_residence_cegar_20260729.py \
  ...authoritative inputs... \
  --trade-report scratch/k16_failedlit0_core_q1_provider_star6_catalogue_20260729.json \
  --static-directed-residence --full-johnson-symmetry-break \
  --static-hint resident --feasibility-only \
  --workers 4 --max-memory-mb 11264 --time-limit 1800
```

`UNKNOWN` and `RESOURCE_LIMIT` remain inconclusive.  Only a literal replayed
`PASS` is a construction; only solver `INFEASIBLE` for this exact static model
is a no-go for the cyclic bi-q1 resident 2-factor architecture.
