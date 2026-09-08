# Exact standard four-cut no-go around the best RF-halo carrier

## Scope

This audit closes the **standard four-cut / 4-opt** neighborhood of the
authenticated cross-reflection carrier

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
```

whose exact lower Hall deficiency is three and whose five upper holes are
the two chains

```text
4e79 < 6f79,       ca79 < ea79 < eb79.
```

Four cuts split the movable interval into three nonempty internal blocks.
Keeping the outer prefix and suffix fixed gives `3! * 2^3 = 48` signed block
permutations.  Removing patterns that restore an old cut edge (and hence are
already moves of order at most three) leaves exactly 25
provenance-irreducible standard 4-opt patterns.

The two designated missing upper masks were pinned to distinct new seams.
The exact pin census was:

| free cuts after pinning | partial descriptors | materialized assignments |
|---:|---:|---:|
| 0 | 26,614 | 26,614 |
| 1 | 764 | 2,248,680 |
| 2 | 0 | 0 |

Thus this instance has no deferred two-free-cut face: the run is exhaustive
for every standard four-cut move that installs the two pinned upper masks.

## Result

After exact deduplication there are 28,429 candidate representations.  The
fast exact filters leave 22,439 candidates satisfying the duplicate-tail and
scalar-capacity constraints.  **None** has nonempty maximal envelopes with
exact middle-row reconstruction:

```text
candidate representations: 28,429
G0 + scalar capacity:        22,439
exact maximal envelopes:          0
upper complete:                   0
```

Therefore no standard signed 4-opt move in the stated pinned neighborhood
can repair the carrier.  The failure occurs before the upper-spectrum or
lower-Hall tests: it is an exact residence/envelope obstruction.

This is a scoped no-go only.  It does **not** cover nonstandard collars,
cell substitutions, segment duplications/deletions, compound motif braids,
or moves with five or more cuts.  Those are now the relevant neighborhoods.

## Reproducibility

Input:

```text
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/rank1_j3959.targets
SHA-256 edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```

Enumerator source:

```text
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/search.cpp
SHA-256 d35f5ae07ff0e47f74d15b0e02afb063b8ee6590a5da35987b78669e7de5f5ab
```

Exact result JSON:

```text
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/o4.full.json
SHA-256 b5d71ba23844076568bc685f23219959fc1bee7008b950a72b7e687ff60dbc4d
```

The authenticated H100 executable had SHA-256
`a9b4a56e801434254a38953beb382d3cbac8f8300a83e7cc6110c2aa3d0c721d`.
It was compiled for holes `4e79,ca79`, first flat `6433`, scalar capacity
`32176`, and upper-superset acceptance; hence pre-existing upper holes were
allowed and only the two pinned chains were forced at the seam-generation
stage.

