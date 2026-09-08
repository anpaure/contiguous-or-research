# Q1 audit: the second protected radius-1 exchange reaches K17 supplier deficiency 94

**Date:** 2026-08-02  
**Status:** exact finite positive theorem on the authoritative `b268` parent;
not a common occurrence state, chronology, or K17 word.

Starting from the independently frozen deficiency-95 selection in
[MATH_AUDIT_Q1_K17_B268_LLR_RADIUS11_DEF95_20260802.md](MATH_AUDIT_Q1_K17_B268_LLR_RADIUS11_DEF95_20260802.md),
an exact one-drop/one-add Benders face removes protected common edge `311` and
adds edge `89202`.  It retains `438` row-disjoint transfers.

The resulting table has hashes

```text
selected  7a1399bbbc876d007226835b457dc83a585249d751be2829fa342cc0aedc4e2e
table     2372971ac55737a5df73d3f6f2e2548a6da8d1e7500eda26412f41d32e8658f9
```

An independent supplier replay constructs `74,135` edges and returns

```text
matching       16804 / 16898
deficiency     94
zero heads     79
DM shore       108 / 14
graph FNV64    3d029717e0810c00
audit SHA      13df95c63fa50c3838030e69a0204478d8759120618ca6142da4e8a28cf7e00f
```

The full short-DNF replay is

```text
native phase 0       3099
transported phase 1  2254
both                 1840
either               3513
```

Thus this table improves every one of those four coordinates by one relative
to the deficiency-95 table while also increasing supplier rank by one.  It
strictly dominates that predecessor on the audited five-coordinate metric.

Direct comparison with the literal `b268` parent checks all `7,213`
authenticated private-ticket rows and finds zero changed values.  The two DNF
hashes are

```text
native phase 0       1bd71898e4bf8f8ae51de902f6f5669f313f05b20a6897c046a7cdefab2301e0
transported phase 1  976fb7a7f20fd268db9b5dd07c18b8cfa11871983e029d0e142e3622aabc81fb
```

The frozen package is

```text
scratch/q1_k17_b268_llr_radius_def94_20260802/
```

Phase 0 is literal on `b268`; phase 1 is still only a root-aligned transported
owner marginal.  Residual outer rematching, a shared occurrence-labelled
state, opening transport, chronology, residence, arbitrary upper shadows,
common cap, compiler, and a K17 word remain unproved.  The next exact finite
target is supplier deficiency `93` under another bounded exchange.
