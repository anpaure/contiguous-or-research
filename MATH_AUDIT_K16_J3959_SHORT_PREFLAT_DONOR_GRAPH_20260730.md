# K16 j3959 short pre-flat donor compatibility graph

Date: 2026-07-30

Status: **exact scoped no-three-gap-cover; independently replayed**.

The authenticated buffered `j=3959` compound chronology has an exact
post-flat service path and exactly twelve replay defects at the three
pre-flat joins `R0|R1`, `R1|R2`, and `R2|R3`.  This audit asks whether those
three joins can be repaired by moving three short, intact donor blocks out of
the protected depth-three interior of `R3`.

The domain contains every oriented contiguous source block of length one,
two, or three whose removal leaves its source seam exactly depth-three
resident.  Each surviving source block is tested independently at all three
defective joins using the exact four-row erosion/replay equations.  The five
fixed upper-service tokens and the complete post-flat order are untouched.

The exact counts are

```text
oriented source blocks                  8,989
source-seam exact                         996
  length 1                                638
  length 2                                280
  length 3                                 78

destination compatibility edges            1
  gap R0|R1                                 0
  gap R1|R2                                 0
  gap R2|R3                                 1
```

The unique edge moves the singleton block `4f31` from source index 6395 to
the third gap.  Since the first two gap vertices have degree zero, the
occurrence-disjoint three-gap matching/path-cover is empty.

This is not a global K16 no-go.  It does not cover a donor touching a
fragment or flat boundary, length at least four, noncontiguous packets,
multiple donor removals whose source defects cancel jointly, or a different
compound chronology.  The stronger same-parent length-at-most-64 theorem
subsumes the mathematical scope; the present audit is an independent native
and Python replay of its smallest boundary-signature face.

Authenticated artifacts:

```text
scratch/search_k16_j3959_preflat_three_gap_donor_cover_20260730.cpp
  SHA256 93846a0015e74ca944c800c1976ac1a9d81f6b00cb1cefc83f9bcdd3318e2cbb

scratch/k16_j3959_preflat_three_gap_donor_cover_20260730/graph.tsv
  SHA256 54311be5ce0973ad3a0ec19e8c13e09a8d6bd42a6bbba258265f0173063186aa

scratch/audit_k16_j3959_preflat_three_gap_donor_cover_20260730.py
  SHA256 3ccf72c9f4beb1ce32376475585bb42c92cf5d44598e6ad1869cc375e4149026

scratch/k16_j3959_preflat_three_gap_donor_cover_20260730/audit.json
  SHA256 d4ede22ff9de6ed1e4d2b5b9172ebfde75fd6aab0e0d7f8b0e35126ff80c7929
  payload 1fcd203757d2119423ea4868991ccb44440faaf284d9c9bc522788eebc31d4ae
```
