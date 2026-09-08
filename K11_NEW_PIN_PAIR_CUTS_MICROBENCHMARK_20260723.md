# Microbenchmark of the companion-pin and global-pair cuts

## Scope

This is a bounded Kissat search-dynamics benchmark.  Every run stopped with
`s UNKNOWN`; it is neither SAT nor UNSAT evidence.

The frozen production source was

```text
2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
  k11_forest_sat.cpp
```

and both optional modules had already passed independent theorem-to-CNF
audits.  The host was `root@157.157.221.29:27423`.  Every trial ran
sequentially on CPU 31 at nice level 15 with Kissat 4.0.4.  The protocol was

```text
kissat --seed=SEED --conflicts=CAP --statistics FORMULA.cnf
```

All raw logs and build inventories are archived under
`scratch/k11_newcuts_microbenchmark_20260723/`.

## Frozen formulas

| formula | variables | clauses | DIMACS SHA-256 |
|---|---:|---:|---|
| Type II, reverse pin | 3,676,391 | 20,175,839 | `ba18785f181d5628889247a5ea8a93b9601821af9826a1fe4079c3bbe53695fd` |
| Type II, reverse + companion | 3,686,611 | 20,247,467 | `3f4676e3522e344f6934174b725865630ee05189cd19ae912f0666c65f44e2fb` |
| Type I, facet + ridge | 3,669,795 | 20,162,593 | `945bfb2aaaf6f32bfbcfe8b68f261e196f1a67c949865eb4044b99193cd8e646` |
| Type I, facet + ridge + global pair | 3,671,659 | 20,175,646 | `c46f35c3d3aa15827bead565195d8cb67ebe2a31bb56bca1abd4026be47df0b0` |

The Type-I control hash is byte-identical to the earlier repaired-rank-five
benchmark control.  Thus the later source changes did not alter its guard-off
formula.

## Type-I global pair profile

Seeds were 357 and 359.

| cap | seed | global pair | conflicts | decisions | propagations | CPU seconds | peak RSS MiB |
|---:|---:|:---:|---:|---:|---:|---:|---:|
| 1,000 | 357 | off | 1,003 | 61,561 | 21,999,309 | 18.01 | 1,610 |
| 1,000 | 357 | on  | 1,000 | 24,258 | 17,886,868 | 17.27 | 1,618 |
| 1,000 | 359 | off | 1,003 | 24,962 | 17,030,685 | 17.60 | 1,610 |
| 1,000 | 359 | on  | 1,001 | 27,542 | 16,136,387 | 17.19 | 1,611 |
| 5,000 | 357 | off | 5,000 | 1,158,785 | 95,009,621 | 48.67 | 1,813 |
| 5,000 | 357 | on  | 5,001 | 53,591 | 146,867,998 | 44.94 | 1,776 |
| 5,000 | 359 | off | 5,002 | 815,004 | 360,571,358 | 57.21 | 1,815 |
| 5,000 | 359 | on  | 5,000 | 1,014,482 | 72,325,698 | 48.66 | 1,810 |

At 1,000 conflicts, the two-seed mean changes were

```text
decisions:    -40.1%
propagations: -12.8%
CPU time:      -3.2%
peak RSS:      +0.3%
```

At 5,000 conflicts they were

```text
decisions:    -45.9%
propagations: -51.9%
CPU time:     -11.6%
peak RSS:      -1.2%
```

CPU time improved for both seeds at both caps.  The individual 5,000-cap CPU
changes were `-7.7%` and `-14.9%`.  Decisions remained seed-sensitive, but
the propagation and timing evidence supports replacing the ridge-only live
slot by a ridge-plus-global-pair slot while preserving the facet-only slot as
formulation diversity.

## Type-II companion pin load

Seeds were 347 and 349.

| cap | seed | companion | conflicts | decisions | propagations | CPU seconds | peak RSS MiB |
|---:|---:|:---:|---:|---:|---:|---:|---:|
| 1,000 | 347 | off | 1,000 | 37,765 | 73,174,269 | 19.01 | 1,593 |
| 1,000 | 347 | on  | 1,000 | 43,494 | 42,332,010 | 18.11 | 1,601 |
| 1,000 | 349 | off | 1,000 | 65,082 | 83,561,669 | 20.08 | 1,593 |
| 1,000 | 349 | on  | 1,000 | 16,032 | 23,373,848 | 17.98 | 1,601 |
| 5,000 | 347 | off | 5,000 | 163,675 | 150,251,655 | 45.09 | 1,767 |
| 5,000 | 347 | on  | 5,000 | 1,055,650 | 217,595,899 | 59.23 | 1,775 |
| 5,000 | 349 | off | 5,002 | 576,763 | 157,178,902 | 51.94 | 1,779 |
| 5,000 | 349 | on  | 5,000 | 849,341 | 185,928,581 | 53.14 | 1,773 |

At 1,000 conflicts, the two-seed mean changes were favorable:

```text
decisions:    -42.1%
propagations: -58.1%
CPU time:      -7.7%
peak RSS:      +0.5%
```

At 5,000 conflicts, however, they reversed:

```text
decisions:    +157.3%
propagations:  +31.3%
CPU time:      +15.8%
peak RSS:       +0.1%
```

Both 5,000-cap CPU comparisons were unfavorable (`+31.4%`, `+2.3%`).  The
companion inequalities are exact and expose substantial early propagation,
but this sample does not justify replacing either current Type-II live slot.

## Deployment verdict

* Deploy one Type-I global-pair search in place of the ridge-only control.
* Keep the facet-only Type-I search for diversity.
* Retain the Type-II companion module as audited optional theory, but do not
  replace the current pin-localized or reverse-pin searches on this evidence.

No mathematical bound changes from these UNKNOWN microbenchmarks.
