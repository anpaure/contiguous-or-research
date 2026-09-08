# Independent height-moment certificate at dimensions137/138

2026-09-09. **PASS:** the standalone exact checker and its complete
priority-free replay independently prove

    nu(137)<1.00001W(137),   nu(138)<1.00001W(138).

This verifies one odd case and its established even lift. It does not
verify the claimed uniform threshold137, the other3,355 cases in the
unprovided band, or the construction-specific predecessor failure.
The retained finite construction, fibre and period theorems are the
mathematical inputs; no enormous word was materialized.

## Exact finite arithmetic

For r=68 the complete retained prefix frontier gives

    Cat_68 = 86218923998960285726185640663701108500
    U      = 860872256709126171307785011672491

and the exact positive comparison

    Cat_68-100000U = 131698328047668595407139496452008500 > 0.

Its outward enclosure is

    U/Cat_68 < 0.000009984725125072396316850761 < 0.00001.

The actual integer width and resulting construction-length upper bound are

    W(137) = 11811992587857559144487432770927051864500,
    N      <=11812110527356728294772901937473650995767.

The generator used162 refinements and2,571 nodes. All2,409 final leaves
were retained, including2,388 unfinished leaves. The maximum processed
depth was three. The replay independently regenerated every complete
split, recomputed period denominators and integrated height charges,
and freshly summed both Catalan mass and integer U. No symmetry class,
next-size child, or residual mass was discarded.

## Independently checked structure

* 5,050 exact conditional K,H cells through a=100.
* All23,713 nonempty Dyck roots through semilength10, including every
  pruning-class count, height total and one-step height drop.
* All125,475 middle bridges through semilength9, with both reflection
  counts and every rooted rotation multiplicity.
* 5,050 exact geometric-tail comparisons and338,350 conditional-height
  tail comparisons.
* 2,575 directly enumerated ordered composition rows in36 slot/mass cases.
* 288 small prefix states and184 integrated-period correction identities;
  complete period/height histograms and unrounded native charges match
  the earlier independently verified census for r=1,...,9.

The illustrative conditional mean is certified by

    16.428245020843044252579122292728
      <= H(100,50)/K(100,50)
      < 16.428245020843044252579122292729.

## Review, execution and artifacts

The [independent pre-execution source audit](MOMENT_PREFIX_STRUCTURE_AND_R68_CHECKER_PREEXECUTION_CODE_AUDIT_20260909.md)
and root's full source review passed before the sole h100 execution.
The [height/reflection proof audit](PBBS_MOMENT_PREFIX_HEIGHT_RECURRENCE_AND_REFLECTION_SUBFAMILY_AUDIT_20260909.md)
and [integrated-period proof audit](MOMENT_PREFIX_INTEGRATED_PERIOD_SPARSE_RESERVE_AND_THRESHOLD_INDEPENDENT_AUDIT_20260909.md)
separately establish the mathematical interfaces.

The run used1.53143053 CPU seconds and1.532426885329187 wall seconds
under60CPU/90wall/1GiB hard limits. No retry, alternative priority,
additional dimension or band enumeration occurred.

* [Standalone checker](verify_moment_prefix_structure_and_r68_20260909.py).
* [Complete report](moment_prefix_structural_and_r68_20260909/moment_prefix_complete_certificate.json).
* [Structural report](moment_prefix_structural_and_r68_20260909/structural_certificate.json).
* [Exact table](moment_prefix_structural_and_r68_20260909/exact_height_table_through100.jsonl).
* [r68 summary](moment_prefix_structural_and_r68_20260909/r68_frontier/summary.json),
  [complete split log](moment_prefix_structural_and_r68_20260909/r68_frontier/splits.jsonl),
  [all final leaves](moment_prefix_structural_and_r68_20260909/r68_frontier/final_leaves.jsonl).
* [Execution provenance and all artifact hashes](moment_prefix_structural_and_r68_20260909/execution_provenance.json).
* [Detailed implementation and replay specification](MOMENT_PREFIX_STRUCTURAL_AND_SINGLE_R68_CHECK_SPECIFICATION_20260909.md).

Source SHA-256:
`6f1f556319147121250420d4715a21e0a7cbf3a679392b3b7b8b210a11c17132`.

Complete report SHA-256:
`4a72d1ed42e689b59eff6e7b80bf082e5cc7044b436731a18313834794df16d4`.

The complete local artifact directory is
`scratch/moment_prefix_structural_and_r68_20260909/`. Its remote source is
`h100:/home/amodo/exact-b-moment-prefix-structural-and-r68-20260909/`.
All artifacts have been copied locally. The existing exact17/18 literal
results and the all-dimensional exact-equality objective are unchanged.
