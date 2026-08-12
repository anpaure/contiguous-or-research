# Staged literal-q1 optimization inside the exact K=16 residence model

## Purpose

The unrestricted hard model asks for a residence-clean spanning 2-factor of
`J(16,8)` covering all `11,440` lower and all `11,440` upper q1 colours at
once.  Its first 16 GiB run ended only in `RESOURCE_LIMIT`; the audited 32 GiB
retry is a separate live lane.  This note defines a smaller-catalogue staged
route which starts from the known resident factor

```text
lower holes = 492, upper holes = 698, residence violations = 0
```

and emits a complete oriented/history-consistent hint for the hard model.

Implementation:

```text
scratch/solve_k16_q1_augmented_catalogue_residence_cegar_20260729.py
```

## Exact soft-coverage formulation

For every optimized colour `c`, introduce a Boolean `z_c` and the clause

```text
z_c -> OR(selected provider edges of c).
```

Every `z_c` has positive objective weight.  Therefore, for every fixed factor,
the best extension sets `z_c=1` for exactly its literally covered colours.
Consequently

```text
max sum_c z_c
```

has exactly the same optimum as maximizing literal q1 coverage.  The encoding
is one-way only to save memory; it is not a relaxation of the optimum.  A
nonoptimal incumbent may leave an available colour unclaimed, so every output
records both modeled and literal-replay coverage.  It asserts

```text
modeled coverage <= replay coverage,
```

and asserts equality when optimality is proved.

The initial `MaxEquality` implementation was abandoned: even on the restricted
25,349-edge Q/R catalogue it hit a 5 GiB address-space guard at 4.58 GiB RSS.
That is recorded only as `RESOURCE_LIMIT`.  The witness-clause version solved
the same 30-second regression with peak RSS 2.36 GiB.

### Exact lexicographic tie-break

Optionally minimize symmetric difference to either the resident or q1 factor
after maximizing coverage.  Two 12,870-edge factors differ in at most 25,740
edges, so the single integer objective

```text
25,741 * covered_colours - symmetric_difference
```

is exactly lexicographic: gaining one colour dominates the entire possible
tie-break range.

The fixed-factor tie-break is not invariant under `S_16`, so it cannot be
combined with the full-Johnson symmetry break.  Pure coverage is invariant and
can be combined with it safely.

## Artifact-to-hint interface

A successful soft stage serializes:

* all 12,870 selected physical edges;
* all 12,870 oriented arcs;
* the previous-three insertion labels and outgoing deletion at every vertex;
* component count and length histogram; and
* a literal replay proving zero residence violations.

The next stage consumes it with

```text
--static-hint artifact --static-hint-artifact PREVIOUS.json
```

The loader independently checks Johnson adjacency, degree two, q1 audit, and
residence before adding any hint.  With the full-Johnson symmetry break, the
factor is first canonically relabelled, preserving all loads and run lengths.

The restricted end-to-end regression is frozen in

```text
scratch/k16_static_directed_softboth_restricted_regression4_20260729.json
```

It returned the initial resident factor as a valid 30-second incumbent:

```text
modeled/replayed lower coverage = 10,948
modeled/replayed upper coverage = 10,742
unclaimed replayed colours       = 0
oriented arcs/history rows       = 12,870 / 12,870
history violations               = 0
status                           = SOFT_FEASIBLE_NOT_PROVEN
```

The objective accounting was exact.  This run did not improve the resident in
30 seconds and is not evidence that the restricted optimum equals the seed.
An independent solver-free replay of the selected edges, oriented arcs,
history rows, q1 loads, lexicographic coefficient, symmetric difference, and
integer objective is frozen in

```text
scratch/audit_k16_static_q1_stage_objective_20260729.py
scratch/k16_static_directed_softboth_restricted_regression4_20260729.audit.json
```

It passes, with coefficient margin exactly one over the maximum possible
factor distance.

An independently rebuilt hard consumer accepted that staged artifact and
created a complete consistent hint.  The hard-lower/soft-upper model also
builds successfully; frozen build:

```text
scratch/k16_static_directed_staged_hint_consumer4_build_20260729.json
scratch/k16_static_directed_hardlower_softupper_build_20260729.json
```

It has 151,837 variables and 189,799 constraints on the restricted catalogue.

## Search ladder

The intended ladder never labels a timeout as infeasibility.

1. **Restricted combined coverage.**  On `Q union R`, use residence hard,
   q1 hard mode `none`, soft objective `both`, resident tie-break.  This is a
   25,349-edge, approximately 2.4 GiB search rather than the full 411,840-edge
   model.
2. **Catalogue expansion.**  Re-run the same stage over the radius-1, radius-2,
   and radius-3 packet/provider catalogues, always consuming the best previous
   artifact as a static hint.  Advance an artifact only after literal replay.
3. **Palette focus.**  Run independent `soft lower` and `soft upper` objectives
   from the best combined incumbent.  A zero-hole palette becomes hard in the
   next stage.
4. **One-hard/one-soft.**  If lower reaches zero, use `--q1-mode lower
   --soft-q1-objective upper`; dually for upper.  This preserves the completed
   palette while maximizing the other.
5. **Hard both-q1.**  Feed the best staged artifact to the unrestricted static
   feasibility model.  With no fixed-factor tie-break, the sound S_16 symmetry
   break is again available.

Representative stage options are:

```text
--static-directed-residence
--static-hint artifact --static-hint-artifact PREVIOUS.json
--q1-mode none --soft-q1-objective both --soft-q1-tiebreak resident
```

then, after one palette closes,

```text
--q1-mode lower --soft-q1-objective upper --soft-q1-tiebreak resident
```

and finally

```text
--q1-mode both --feasibility-only
--full-johnson-symmetry-break
```

## Backend and resource safeguards

OR-Tools 9.15 aborts internally when `repair_hint` is combined with the partial
oriented hint and a maximize objective (`heuristics.fixed_search` check
failure).  The CLI rejects that combination.  Normal partial hints work and
were regression-tested.

Every heavy stage remains H100-CPU-only, at most four workers, with both an OS
address-space limit and an OR-Tools memory parameter.  A killed process or
`std::bad_alloc` is `RESOURCE_LIMIT`; timeout is `UNKNOWN`; neither is UNSAT.
