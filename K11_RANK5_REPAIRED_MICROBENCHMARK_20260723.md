# Corrected rank-five portfolio microbenchmark — 2026-07-23

## Scope and evidentiary status

This is a bounded search-dynamics benchmark of the repaired `k=11,n=465`
formulas.  It is not SAT or UNSAT evidence.  Every run stopped with
`s UNKNOWN` at its requested conflict cap.

The benchmark compares two independently useful pairs:

1. Type I with the corrected rank-five singleton equations and the facet
   load theorem, versus the same formula with the ridge load theorem added;
2. Type II with the corrected rank-five singleton equations, versus the same
   formula with the two-component pin-localization module added.

The four live corrected candidate searches, solver PIDs

```text
153935, 153940, 153943, 153944
```

were not signalled, moved, stopped, or otherwise modified by the benchmark.
At the post-run hash snapshot they remained live on CPUs `9,12,4,5`,
respectively.  All
formula generation and solver trials were sequential, pinned to CPU 6, and
run at nice level 15.  CPU 6 was not used by any of the four live `k=11`
solvers.  It was a sibling of another non-`k=11` workload, so the absolute
timings should be treated as local measurements; the paired comparisons use
the same CPU and background environment.

## Frozen provenance

Host and directory:

```text
root@157.157.221.29:27423
/root/k11_onion_20260723
```

Binary hashes:

```text
17bed4d6957eef3346850c3cebf883f0d503ec037ad8e1f6ac30491f63be1f09  k11_forest_sat_rank5repair
0a0f9ef8e8f73235f37dea6bc294905ac470c41def0f1f605b4128fa0c0509c4  kissat 4.0.4
```

The generator is the independently audited corrected binary from
`K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md` and
`K11_RANK5_REPAIR_DOWNSTREAM_AUDIT.md`.

All four formulas enabled the common audited stack:

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS=1
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_SINGLETON_POOL_CUT=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_LOCAL_DENSITY_PB=1
K11_FOREST_CONTAINMENT_CAPS=1
K11_FOREST_SUBCUBE_DEFICIENCY=1
K11_FOREST_NAMED_CELL_HALL=1
K11_FOREST_RANK7_TRUNCATED_WIDTH=1
K11_FOREST_RESIDUAL_COORD_LEX=1
```

Type I additionally enabled

```text
K11_FOREST_RANK6_BRANCH=1
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_TYPE1_PREFIX_CHAIN=1
K11_FOREST_TYPE1_FACET_PIN_LOAD=1
```

and varied only

```text
K11_FOREST_TYPE1_RIDGE_PIN_LOAD=0/1.
```

Type II enabled

```text
K11_FOREST_RANK6_BRANCH=0
K11_FOREST_RANK_FILTRATION_TYPE2=1
```

and varied only

```text
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=0/1.
```

The exact inventories and DIMACS hashes were:

| formula | variables | clauses | DIMACS SHA-256 |
|---|---:|---:|---|
| Type I, facet only | 3,649,035 | 20,038,123 | `44887f5d1350ce52ee567c53a54c6f47b06718b1ed83d7c9639d0a64f9adb96f` |
| Type I, facet + ridge | 3,669,795 | 20,162,593 | `945bfb2aaaf6f32bfbcfe8b68f261e196f1a67c949865eb4044b99193cd8e646` |
| Type II, base | 3,648,842 | 20,021,985 | `b413962b5f12de8a4ea210feef9bae6b499c62a91cd4ab5e7c145f1cf4ff243d` |
| Type II, pin localization | 3,660,446 | 20,079,690 | `d1c08f48d3310f12ffadda54bbe2023a643e444afb9ede5507f5b9e70fb493ec` |

Thus the ridge theorem costs exactly `20,760` variables and `124,470`
clauses, while pin localization costs `11,604` variables and `57,705`
clauses.

## Solver protocol

Kissat 4.0.4 was run sequentially with two seeds and conflict caps 1,000 and
5,000.  The Type-I seeds were `311,313`; the Type-II seeds were `317,319`.
Each command had the form

```bash
taskset -c 6 nice -n 15 /usr/local/bin/kissat \
  --seed=SEED --conflicts=CAP --statistics FORMULA.cnf
```

The reported `process-time` includes parsing and solving.  It is the timing
column below.  All sixteen logs are archived under
`scratch/k11_rank5_repaired_microbenchmark_20260723/`.

## Type-I results: facet versus facet plus ridge

| cap | seed | ridge | conflicts | decisions | propagations | CPU seconds | peak RSS |
|---:|---:|:---:|---:|---:|---:|---:|---:|
| 1,000 | 311 | off | 1,000 | 48,038 | 78,694,164 | 17.49 | 1,600 MB |
| 1,000 | 311 | on  | 1,000 | 28,660 | 16,149,471 | 15.26 | 1,610 MB |
| 1,000 | 313 | off | 1,000 | 32,266 | 15,885,193 | 15.50 | 1,596 MB |
| 1,000 | 313 | on  | 1,000 | 26,614 | 15,037,988 | 15.20 | 1,610 MB |
| 5,000 | 311 | off | 5,002 | 71,192 | 208,261,957 | 43.14 | 1,784 MB |
| 5,000 | 311 | on  | 5,000 | 80,465 | 215,766,730 | 49.32 | 1,807 MB |
| 5,000 | 313 | off | 5,000 | 76,906 | 71,592,136 | 44.44 | 1,786 MB |
| 5,000 | 313 | on  | 5,000 | 217,856 | 117,055,971 | 42.54 | 1,807 MB |

At 1,000 conflicts, the two-seed means change under the ridge module by

```text
decisions:    -31.2%
propagations: -67.0%
CPU time:      -7.7%
peak RSS:      +0.7%
```

The CPU changes are favorable for both seeds: `-12.8%` and `-1.9%`.

At 5,000 conflicts, however, the two-seed means change by

```text
decisions:    +101.4%
propagations:  +18.9%
CPU time:       +4.9%
peak RSS:       +1.3%
```

The individual 5,000-conflict CPU changes are `+14.3%` at seed 311 and
`-4.3%` at seed 313.  The seed-313 decision count rises by `183.3%` despite
the small CPU reduction.

The ridge theorem therefore has a real early-propagation effect, but the
effect does not persist monotonically to 5,000 conflicts.  The present
sample does not justify making both Type-I portfolio members ridge-enabled.
One facet-only Type-I seed should be retained as formulation diversity while
the other keeps the stronger facet-plus-ridge formula.

## Type-II results: base versus pin localization

| cap | seed | pin localization | conflicts | decisions | propagations | CPU seconds | peak RSS |
|---:|---:|:---:|---:|---:|---:|---:|---:|
| 1,000 | 317 | off | 1,000 | 58,693 | 72,640,687 | 18.02 | 1,576 MB |
| 1,000 | 317 | on  | 1,000 | 35,938 | 63,447,166 | 16.89 | 1,582 MB |
| 1,000 | 319 | off | 1,000 | 47,186 | 42,514,058 | 17.54 | 1,576 MB |
| 1,000 | 319 | on  | 1,000 | 60,253 | 68,801,616 | 18.04 | 1,582 MB |
| 5,000 | 317 | off | 5,000 | 797,748 | 169,953,038 | 55.57 | 1,747 MB |
| 5,000 | 317 | on  | 5,000 | 511,348 | 129,914,370 | 46.33 | 1,747 MB |
| 5,000 | 319 | off | 5,001 | 302,527 | 312,985,839 | 54.10 | 1,744 MB |
| 5,000 | 319 | on  | 5,000 | 365,414 | 279,315,115 | 48.94 | 1,756 MB |

At 1,000 conflicts, the two-seed means change under pin localization by

```text
decisions:     -9.2%
propagations: +14.8%
CPU time:      -1.8%
peak RSS:      +0.4%
```

The seedwise CPU changes are mixed: `-6.3%` and `+2.9%`.

At 5,000 conflicts, the two-seed means change by

```text
decisions:    -20.3%
propagations: -15.3%
CPU time:     -13.1%
peak RSS:      +0.3%
```

Both 5,000-conflict CPU comparisons are favorable, by `-16.6%` and `-9.5%`.
Decisions are still seed-sensitive (`-35.9%` and `+20.8%`), but the longer
bounded sample supports retaining pin localization in the live Type-II
portfolio.

## Verdict

The repaired theory modules materially change the search, but neither gives
a uniform monotone speedup on every metric and seed.

* **Type I:** ridge load is strong at 1,000 conflicts but mixed at 5,000.
  Keep one facet-plus-ridge seed and one facet-only seed rather than spending
  both Type-I slots on the ridge formulation.
* **Type II:** pin localization gives a reproducible 5,000-conflict CPU
  improvement in both seeds, with nearly neutral memory.  Keeping both live
  Type-II seeds pin-enabled is reasonable; a base control is less urgent.

These statements concern bounded search dynamics only.  They do not show
that either formula is satisfiable or unsatisfiable, do not estimate total
solution time, and do not alter the mathematical bounds

```text
465 <= nu(11) <= 477.
```

The temporary DIMACS files and remote raw logs were removed from `/dev/shm`
after their hashes and the local raw-log archive were secured.  No live
candidate file or live solver log was removed.

After that post-run snapshot, the portfolio coordinator intentionally
retired PID `153944` and its wrapper, having independently checked that its
candidate was absent and it had no terminal marker.  That planned portfolio
replacement was separate from this benchmark; it is not a solver outcome or
evidence about satisfiability.
