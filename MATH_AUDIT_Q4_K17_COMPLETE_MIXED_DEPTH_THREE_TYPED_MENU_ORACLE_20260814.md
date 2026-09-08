# Independent audit: complete q4 k17 mixed depth-three typed-menu oracle

**Date:** 2026-08-14

**Verdict:** **PASS**.  The PPS, PSS, and SSS formulas and layered cuts are
lossless for indexed configurations, including coincident row supports.
Every incoming self index remains in the group of the outgoing self it
replaces.  Together with the frozen three-pair oracle, the three types
partition all legal depth-three exchanges in the fixed reflection face.
No finite q4 pool is searched here.

## 1. Audited theorem

```text
MATH_REDUCTION_Q4_K17_COMPLETE_MIXED_DEPTH_THREE_TYPED_MENU_ORACLE_20260814.md
sha256 bb6be6d76220aaa700fb5669f0344fd340edfa58c1647a4168167f0e56a3c265
```

The common score follows by exact square expansion.  It depends only on
the indexed incidence vectors, so unequal configuration sizes and repeated
supports cause no correction.  Every omitted interaction in a face,
singleton, or prefix cut is an incoming overlap and is nonnegative.
Consequently each strict cut is necessary for a negative completion.

In PPS, the pair minimum uses two distinct pair indices, the singleton
exclusion removes the current pair index, and the self replacement is
drawn only from its one removed group.  In PSS and SSS the self menus are
labelled by distinct removed groups; they are not permuted or merged.
The final candidate restores every overlap with the retained prefix before
its sign is tested.  Thus every negative legal triple survives, and every
accepted leaf is evaluated exactly.

The outgoing-face counts replay symbolically:

```text
PPS  C(54,2)*35 = 50,085
PSS  54*C(35,2) = 32,130
SSS  C(35,3)     =  6,545
total              88,760.
```

An empty required self menu or undersized pair bank has no legal leaf and
is correctly discarded.

## 2. Independent H100 replay

```text
scratch/verify_q4_k17_complete_mixed_depth_three_typed_menu_oracle_20260814.py
sha256 7c1f6a2a5926ea2426498c1fc542dc5814ed0f41cc2a52264cb9a416f9c3bf4e

scratch/verify_q4_k17_complete_mixed_depth_three_typed_menu_oracle_20260814.h100.out
sha256 4bd07f745a0f85d0c41dd18238068e76b9dfc3225609a9514df4cdcbf50d7cec
status PASS
```

The verifier checks all 448 scalar three-out/three-in membership cases.
On random typed banks it compares 11,520 direct legal triples with the
closed score and finds exactly 2,973 PPS, 1,758 PSS, and 59 SSS negative
triples through the layered scans.  A disjoint exact-cover suite checks
2,144 further direct triples and supplies 24, 24, and 4 nonvacuous dead
faces, respectively.

## 3. Scope boundary

The theorem is a complete algebraic oracle for a frozen finite bank and
fixed self-group system.  It does not prove a negative exchange exists,
search the E54 pool, admit a self replacement from a different group, or
rule out missing columns, neutral paths, changing the fixed matching, or
exchanges of depth at least four.

All computation, replay, and hashing ran on H100.
