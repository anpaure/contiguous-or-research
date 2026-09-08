# K16 Hall-23 protected facet four-cycle census

Date: 2026-07-31  
Status: **PASS_EXHAUSTIVE_NO_EXACT in the stated family; no global K16 claim**

## Input and objective

The fixed carrier is the materialized Hall-23 descendant

```text
scratch/k16_nested_hall24_third_equalblock_20260731/pass33_m32/hit_7.targets
SHA-256 57db213117877dc3a41f3426fdce98de4cf754119bc6374639ba635b16c1d252
```

It is middle-exact, has matching 26,309/26,332, and has the sole upper hole
`4e79`.  Its lost unique witness used physical rows 12713--12714, so the
return port is fixed at `U=12714`.

## Exhausted family

Choose:

1. a physical donor `v` carrying a rank-eight facet of `4e79`, excluding
   the incumbent left facet `4a79` and both frozen provider collars;
2. one relief row `r` in `{12715,12716,12717}`;
3. one distinct donor-neighbour row `p` with `|p-v|<=3`, again outside the
   provider collars.

The frozen collars are `[6604,6612)` and `[12718,12724)`.  Requiring the
facet movement `old[v] -> U` leaves the two genuine four-cycle orders

```text
old[v] -> U, old[r] -> v, old[p] -> r, old[U] -> p;
old[v] -> U, old[p] -> v, old[r] -> p, old[U] -> r.
```

The eight physical donor occurrences were

```text
4c79@3105 4e69@4347 4e39@4507 4e59@4606
0e79@6060 4e71@6320 4e71@6321 4679@12826.
```

## Result

Both a C++ whole-word replay and an independent Python local-dependency
replay give exactly:

| count | total | order 0 | order 1 |
|---|---:|---:|---:|
| raw cycles | 288 | 144 | 144 |
| correct three-flat schedule | 216 | 108 | 108 |
| exact middle ownership | **0** | **0** | **0** |
| upper-complete | 0 | 0 | 0 |

Thus no full Hall calculation is reached: every candidate fails exact middle
ownership first.  This closes only the protected radius-three four-cycle
family.  It does not exclude a fifth occurrence, a wider donor dependency
closure, a provider-collar migration, or a different carrier.

## Reproducibility

```text
scratch/search_k16_nested_hall23_protected_facet_4cycle_20260731.cpp
scratch/audit_k16_nested_hall23_protected_facet_4cycle_20260731.py
scratch/k16_nested_hall23_protected_facet_4cycle_20260731.audit.json
scratch/k16_nested_hall23_protected_facet_4cycle_20260731/pass33_alpha.tsv
scratch/k16_nested_hall23_protected_facet_4cycle_20260731/pass33_alpha.stderr
```

Audit payload SHA-256:
`acf1ea40a9a5bb3d19d21bcfa3bae9c8248782e194a42ed5a5f92453af35ae3f`.
