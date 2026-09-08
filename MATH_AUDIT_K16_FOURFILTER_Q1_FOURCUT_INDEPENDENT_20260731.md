# Independent audit of the K16 four-filter four-cut q1 face

## Result

GO.  An occurrence-index implementation independently reproduces the exact
four-cut census from the authenticated carrier

```
scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word
SHA-256 e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452.
```

The carrier misses exactly the two rank-nine adjacent-union colours
`a9ce,b8ce`.  In the class obtained by deleting exactly four old path edges
and adding exactly four Johnson edges while retaining the two original path
endpoints, there is no capacity-live repair.

## Completeness reduction

Any repaired path must add an `a9ce` facet edge and a `b8ce` facet edge.
Each rank-nine mask has nine rank-eight facets and therefore 36 unordered
facet edges.  For every one of the `36^2=1296` distinguished edge pairs, the
audit chooses an incident removed edge for each of its four occurrence
endpoints.  This produces exactly 18,432 raw endpoint assignments; 17,714
use four distinct cuts.

After subtracting the four forced endpoint deficits, exactly four deficits
remain.  Their three perfect pairings are exhaustive, giving
`17,714*3=53,142` pairing rows.  Exactly 321 rows have both extra edges in
the Johnson graph.  Deduplication by `(four cuts, four new edges)` leaves
316 configurations.

Literal adjacent-union multiplicity replay leaves four q1-complete
configurations.  Direct degree and traversal replay finds only two connected
Hamilton paths.  A separate maximal-envelope P/Q dynamic program gives:

| word SHA-256 | best selected area | area + 9 | upper holes |
|---|---:|---:|---|
| `6577822589e61fa14f10a808f50bf4b97d32118e9597b610637a2e681ac2adbb` | 25828 | 25837 | `7bce,a9fe,b8cf,b9ce,b9fe` |
| `0f6dd0fbfce9f86ec7c0852548ad0f194f4f97636a59918f7eaaff4c45c9c595` | 24459 | 24468 | `7bce,a9fe,b8cf,b9ce,b9fe` |

Both capacity bounds are below the required 26,332 lower masks.  The face is
therefore empty before fixed-schedule Hall or common-cap replay.

The audit is exact only for four removed/four added Johnson edges with the
fixed endpoints and unchanged rank-eight masks.  Five or more cuts, changed
values, other parents, and unrestricted K16 remain open.

## Artifacts

- `scratch/audit_j3959_outer_context_k16_fourfilter_q1_fourcut_independent_20260731.py`
  - SHA-256 `647ecdd807982253e52e0070667711f3523a72beb3e813d5c2e6d9f57eb7d0a8`
- `scratch/j3959_outer_context_k16_fourfilter_q1_fourcut_independent_20260731/audit.json`
  - SHA-256 `602d4535b63363b6086f2afa6bb78888ffe3e9b7be68b0ab27335203067b6f28`
  - payload SHA-256 `4350d0b68ce31bf0ecd8ac6d38d3da86b68b1739a6def40a47b5d643f8d2878f`
- production reference
  - `scratch/k16_fourfilter_q1_fourcut_20260731/census.audit.json`
  - SHA-256 `8625b481d53c77226dc9b8037271e8d25e4c9a6dd76bc65ad4bf7d2f3ec6e3ee`
  - payload SHA-256 `ffbbd7857dbc3d442472eb5daefe3e5798fe3ebfde630bc154af8afa9597bfa9`

