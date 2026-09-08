# K16 pass33 dependency-disjoint compatibility-cycle census

Date: 2026-07-31  
Status: **PASS_SCOPED; three exact/all-upper cycles exist, but all fully
rematch worse than Hall 24.  No global K16 claim.**

## Frozen scope

The parent is the exact/all-upper Hall-24 carrier

```text
scratch/defect_transport_sparse_bad2_20260730/shorebfs_out/pass_33.targets
SHA-256 2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec
```

Every cycle makes the forced halo transport

```text
6b29 : occurrence 3846 -> physical row 4653.
```

All further occurrence positions are mutually farther than six rows.  Thus
their middle dependencies are disjoint and each arc may be certified by its
single-row compatibility.  Sources within distance six of the three flat
sites or the independent `8000` provider at physical row 12720 are excluded.
The path has at most seven intermediate compatibility arcs; the displaced
old row `69a9@4653` closes the occurrence cycle.

The frozen search source and result table are

```text
scratch/search_k16_pass33_compatibility_cycles_20260731.cpp
SHA-256 c56882d85371e104a7643b585c9dc7c9f2df2926fd831dce6c0b1e35c81c41cb

scratch/k16_pass33_compatibility_cycles_20260731/depth7_match_fast.tsv
SHA-256 ca25a947847baf3a8ecab733e68cfcae3557143163d6c9f6b1f867c64532c57b
```

## Literal census

An independent C++ replay reconstructed every row from its labelled arc
cycle and checked:

1. occurrence bijection;
2. exact middle reconstruction;
3. unrestricted upper holes;
4. physical incidences `6a29--(4654,4655,4656)`,
   `4a29--(4655,4656)`, and the retained `8000` provider;
5. losses from the frozen 26,308-edge pass33 matching.

The result is

```text
closed cycles                    2732
middle-exact                     2732
physical halo + 8000             2732
arbitrary-upper complete            3
minimum frozen matching losses     24
```

The complete upper-hole-count histogram begins

```text
0:3, 1:6, 2:41, 3:94, 4:170, 5:274, 6:340, 7:370, 8:388, ...
```

## The three all-upper cycles

Each was reconstructed independently with transported occurrence labels and
then subjected to the complete generalized Hall matching, not merely the
frozen-edge-loss proxy.

| table row (0-based) | artifact | frozen matching losses | full Hall deficiency | decomposition `Z+S` |
|---:|---|---:|---:|---:|
| 422 | `remote_pass/candidate_34.targets` | 44 | 30 | `15+15` |
| 461 | `remote_pass/candidate_45.targets` | 43 | 34 | `16+18` |
| 463 | `remote_pass/candidate_46.targets` | 44 | 31 | `16+15` |

Their exact SHA-256 values are respectively

```text
0b43cc742ef28d822f86690ea2b13d8596dc7144a84c1d9ebbe7adcde2567027
67e606307fd951f37a52878befd5917a18eb03d4c5f5a6c4d61206353ec09fbc
8e94ae0ad9b86b91e9122dcbd37b350ef7558c116f12bc50ec37efe7df672e5b
```

Thus upper closure and the physical halo can coexist in this family, but
the required global lower matching does not survive: all three are strictly
worse than the Hall-24 parent.

## The minimum-loss cycle

There is exactly one row with only 24 frozen matching-edge losses, table row
2708.  Its cycle is

```text
3846->4653,6263->3846,6252->6263,3373->6252,4653->3373
```

and its unrestricted upper holes are exactly

```text
2bab 2fac 6b39.
```

For calibration, a complete Hall rematch of this non-upper-complete word has
deficiency 32 (`15+17`).  That diagnostic is not a production result; the
three upper holes already reject it.

## Conclusion and exclusions

The common-`0200` halo is occurrence-integral: 2,732 exact compatibility
cycles realize it, and three are also arbitrary-upper complete.  What fails
is lower-provider preservation.  The depth-seven, dependency-disjoint
restriction turns the desired gains at the halo into 43--44 frozen matching
losses in every all-upper realization found.

This closes only the stated pass33 disjoint-cycle family.  It does not cover
dependency-overlapping cycles, longer paths, a different Hall-24 parent,
provider migration, joint matching-aware arc selection, or a different
carrier.

## Audit artifacts

```text
scratch/audit_k16_pass33_compatibility_cycles_independent_20260731.cpp
scratch/k16_pass33_compatibility_cycles_20260731/independent_audit.stdout
scratch/audit_k16_pass33_compatibility_cycles_full_20260731.py
scratch/k16_pass33_compatibility_cycles_20260731.audit.json
```

Full audit payload SHA-256:
`98b4d83884cd495cdfec8510da8514303458b6436a55fa7d4168322cf2f1bbfe`.
