# K16 directed-3opt Hall-witness no-go (2026-07-30)

## Result

One explicit Hall witness eliminates **all 61,464 complete retained states**
in the upper-targeted directed-3opt catalogue descended from atom 12.

The witness was extracted from atom 43389.  Its target side has 3,412
vertices and its physical short-cell neighbourhood has 3,320 vertices, so its
Hall deficiency is 92.  An independent native reconstruction agrees exactly
with the earlier Python audit:

- lower targets: 26,332;
- physical cells: 27,774;
- incidences: 367,491;
- maximum matching: 26,240;
- total Hall deficiency: 92;
- alternating witness: `3412 - 3320 = 92`.

For each retained atom, the census rebuilt the maximal erosion envelope and
the exact neighbourhood of the same 3,412-target witness.  No atom reached
3,412 neighbours.  The histogram of the resulting rigorous deficiencies was:

| deficiency | count |
|---:|---:|
| 89 | 6 |
| 90 | 35 |
| 91 | 10,841 |
| 92 | 39,142 |
| 93 | 11,193 |
| 94 | 183 |
| 95 | 50 |
| 96 | 9 |
| 97 | 5 |

All 61,464 states retain the same zero-based flat positions
`2031,12869,12871`.  Thus the result is not caused by comparing incompatible
dense cell numberings; physical cells were compared by `(start,length)`.

The six states attaining the best fixed-witness lower bound 89 were then run
through exact maximum matching.  Their actual deficiencies are respectively:

| atom | actual Hall deficiency |
|---:|---:|
| 9 | 96 |
| 10,854 | 95 |
| 10,855 | 96 |
| 32,417 | 98 |
| 43,544 | 96 |
| 44,019 | 96 |

So even the apparent fixed-witness minimizers are worse than atom 43389 under
the full Hall objective.

## Exact scope

This is a move-class theorem, not a global impossibility theorem.  It covers
the complete files `atom_0.targets` through `atom_61463.targets` in
`upper1_3opt_12/atoms2`.  The terminal file `atom_61464.targets` is excluded:
the interrupted generator wrote only 5,597 of the required 12,873 targets.

Every retained state was recorded by the catalogue as capacity 27,774, one
individual lower host, and zero upper holes.  The result does **not** exclude:

- an optimal K16 word of length 12,873;
- a different carrier or multi-parent braid;
- a move that relocates a flat;
- a move that creates at least 89 genuinely new neighbour cells for the
  deficient target set.

It does exclude ordinary upper-targeted long-segment directed 3-opt as a way
to finish this basin.

## Reproducibility

The compact audit package is at
`scratch/k16_directed_3opt_hall_witness_nogo_20260730/`.

Key SHA-256 hashes:

- native Hall witness: `616d1e5200215b84a2e3f6cba7ce2bf2dc714f1cac31ea258763942d230a270a`;
- independent Python audit: `b8458ef7915fbb6ad2ec45345a1e5f0f22686a9dcad3710ea6ddf0a1a67f625f`;
- full fixed-witness census: `4a425a95fd60f68d770a6a7c09150e53d563f8ab56878b77021fbf48a0163754`;
- exact full-Hall results on the six minimizers:
  `491eda723229d70c55c6b4729ab4217488e35b5cb72d482591aa2fdc309c86ee`.

Auditor sources:

- `scratch/audit_k16_generalized_hall_20260730.cpp`;
- `scratch/census_k16_hall_witness_20260730.cpp`;
- `scratch/census_k16_full_hall_20260730.cpp`.
