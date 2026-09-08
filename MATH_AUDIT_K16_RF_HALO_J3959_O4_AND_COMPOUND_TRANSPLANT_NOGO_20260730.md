# Exact local no-go at the Hall-3 RF-halo carrier

This theorem freezes two exhaustive neighborhoods around the authenticated
`j=3959` cross-reflection carrier.  It explains why the remaining one-unit
gap is not removable by another ordinary cut-rejoin or by directly
co-locating the five named services.

## 1. Every standard four-cut move is dead

All 25 provenance-irreducible signed standard 4-opt patterns were enumerated
with the two designated upper holes pinned to distinct new seams.  The exact
pin domains were

```text
zero free cuts:       26,614
one free cut:      2,248,680 completions from 764 descriptors
two free cuts:             0
```

After exact deduplication, 28,429 candidate representations remained.  Of
these, 22,439 pass the exact duplicate-tail and scalar-capacity tests, but
**zero** have nonempty maximal envelopes with exact middle replay.

The full statement and reproducibility data are in
`MATH_AUDIT_K16_RF_HALO_J3959_STANDARD_O4_NOGO_20260730.md`.

## 2. Every direct all-service transplant is dead

The following service macro was then exhausted:

1. choose one of the 330 private-top masks `X` and move it into the
   first-flat `a879 / a86d` sandwich;
2. choose one of the 56 masks `Y` with `6879 | Y = 6f79` and move it after
   `6879`;
3. move `4a79,4e39,4d39` after the intact tail
   `eb60,ea61,ca71`, in all six internal orders.

After excluding nonunique source occurrences and anchor collisions, this is
exactly 109,848 distinct target-multiset-preserving chronologies.  All
109,848 retain the exact three-flat profile and sufficient scalar capacity.
**Zero** have exact maximal-envelope/middle reconstruction:

```text
generated                109,848
flat profile              109,848
scalar capacity           109,848
exact middle replay             0
upper complete                  0
```

The minimum structural defect is 12 bad replay rows with no empty envelope
cells, attained by 16 chronologies.  Thus even the best direct transplant is
three times farther from exact residence than the upper-service O5
rethreading recorded separately.

Thus the three lower services and the two upper chains cannot simply be
co-located by singleton/block transplantation.  At least one additional
buffer segment or a different witness is required to preserve residence.

## Exact scope

These are local theorems, not a K16 impossibility result.  They do not cover:

- buffered segment reconnections using one or more extra vertices;
- compound five-or-more-cut braids outside standard 4-opt;
- substitutions that change the target multiset;
- alternative witnesses for `2665`, `8000`, the `0665` star, or the upper
  chains;
- a different carrier basin.

The next search is therefore a buffered segment-level reconnection, with the
required services imposed as subpaths and one to three additional vertices
available to restore residence.

## Artifacts

Input carrier:

```text
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/rank1_j3959.targets
SHA-256 edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```

Standard O4:

```text
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/search.cpp
SHA-256 d35f5ae07ff0e47f74d15b0e02afb063b8ee6590a5da35987b78669e7de5f5ab
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/o4.full.json
SHA-256 b5d71ba23844076568bc685f23219959fc1bee7008b950a72b7e687ff60dbc4d
```

Compound all-order transplant:

```text
scratch/enumerate_k16_j3959_compound_service_braid_20260730.cpp
SHA-256 31e92886856195c5a598359ed68de962e1796639c16629c7243138d177919a69
scratch/k16_rf_halo_j3959_standard_o4_nogo_20260730/compound_all_orders.audit.json
```

The compound H100 executable had SHA-256
`54bee74438e3892a1f63b13c3703bc9a703b5ef2d711cfd0b6e05949873b9019`.
