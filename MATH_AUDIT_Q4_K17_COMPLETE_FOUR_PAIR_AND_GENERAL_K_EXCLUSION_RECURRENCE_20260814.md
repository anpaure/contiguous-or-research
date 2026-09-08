# Independent audit: complete four-pair and general-k exclusion recurrence

**Date:** 2026-08-14

**Verdict:** **PASS**.  The quadratic score, distinct-candidate exclusion
minima, and canonical prefix search are exact.  For four reflected pairs,
the construction gives a complete lossless oracle over all 316,251
outgoing faces.  It does not assert that the surviving search is small or
give a verdict on any q4 finite pool.

## 1. Audited theorem

```text
MATH_REDUCTION_Q4_K17_COMPLETE_FOUR_PAIR_AND_GENERAL_K_EXCLUSION_RECURRENCE_20260814.md
sha256 c167af4918a10447fbea6e22de08884a30d780cc4e96235deae265a9de24b62d
```

For a fixed outgoing set `R`, direct square expansion gives the constant
`c_R`, candidate linear score `h_R`, and only pairwise incoming overlap
terms.  The prefix recurrence includes every overlap internal to the
prefix exactly once.

For a prefix `S`, the sum of the required number of smallest distinct
`h_R` scores outside `S` is a valid lower bound because every omitted
overlap is nonnegative.  Therefore a negative completion must pass the
strict prefix inequality.  The bound is necessary, not sufficient.  The
four-pair singleton, pair, and triple tests are precisely the depth-one,
depth-two, and depth-three instances of this statement.

The exclusion minima respect distinct incoming indices.  After sorting by
`(h_R,index)`, a prefix of size `j` can exclude at most `j` of the first
entries; hence the first `k` entries contain the required `k-j` admissible
scores.  The claimed constant-time computation for fixed depth is sound.

Canonical index growth cannot lose a negative exchange: its unique sorted
prefix at every depth passes the corresponding necessary cut, and the
full prefix is tested with the exact score.  Conversely, every accepted
leaf is a legal set of distinct unselected candidates.

## 2. Independent H100 replay

```text
scratch/verify_q4_k17_complete_four_pair_general_k_exclusion_recurrence_20260814.py
sha256 30b1a6b14ca6f2fb79991ff10d34d10faf3ad8c711d6e33c1d2e801a7923cb19

scratch/verify_q4_k17_complete_four_pair_general_k_exclusion_recurrence_20260814.h100.out
sha256 0634987da52617d92dc9df1bcd095265e2a87202e4ef4bf9df580fd3dfb2c5f5
status PASS
```

The replay checks all 2,304 scalar cases (`ell=0,...,8` and all 256
four-out/four-in membership patterns).  Synthetic finite banks then compare
the formula with 40,396 direct exchanges at depths one through four,
check 431,803 negative-prefix implications, and verify literal equality
between the layered search result and the complete negative set.  At
depth four it finds 24,050 negative exchanges.  A disjoint exact-cover
suite supplies fifteen nonvacuous face cuts and no negative exchange.

## 3. Scope boundary

The theorem is an exact algebraic oracle for equal-size replacement by
distinct reflected-pair columns.  It neither searches the current E54
pool nor covers mixed self/pair menus, changing the fixed matching,
missing columns, neutral paths, or a different exchange depth.  The
recurrence is lossless but may retain exponentially many prefixes.

All computation, replay, and hashing ran on H100.
