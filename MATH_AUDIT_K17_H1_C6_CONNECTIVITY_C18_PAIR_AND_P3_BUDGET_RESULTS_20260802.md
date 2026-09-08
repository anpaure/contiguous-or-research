# K17 authenticated outer-search checkpoint: C6 connectivity, C18 pairs, and P3 budgets

Date: 2026-08-02

This note freezes three completed, disjoint computational statements.  None
of them is a K17 word or a proof that `nu(17)=B(17)`.

## 1. Exact C6 component patching of the h=1 sample portfolio

The input family is the forty-eight SAT models `round01` through `round48`
from the exact h=1 degree-factor CEGAR lane.  For each model, the patcher
enumerates literal alternating incidence hexagons and accepts a toggle only
after a fresh exact component replay proves a strict component decrease.  It
preserves the complete h=1 degree ledger and the fixed `MB` incidence.  The
independent decoder then reconstructs both linear orientations and replays
positive residence and every upper interval union.

Every one of the 48 inputs reached one component.  Thus this portfolio gives
48 literal connected h=1 lollipops, rather than only disconnected degree
factors.  This is an empirical portfolio result, not a theorem that greedy C6
descent connects every factor.

The downstream scores remain far from the required gate:

| extremum | round | components | C6 toggles | short positive runs | upper holes | rank 10--13 holes |
|---|---:|---:|---:|---:|---:|---:|
| least residence debt | 40 | 30 -> 1 | 25 | 5,846 | 7,441 | 4,538 / 2,408 / 487 / 8 |
| least upper debt | 48 | 23 -> 1 | 20 | 6,009 | 7,292 | 4,446 / 2,396 / 435 / 15 |

Ranks 14 through 17 have no holes in both displayed rows.  No portfolio row
passes residence or the upper deck.

Authoritative H100 root:

`/home/amodo/or15/work/root_k17_h1_materialize_patch_20260802/out/portfolio`

Authenticated artifacts:

- `summary.tsv`, SHA-256
  `93ccf190a1bc01450354609c4dc21249bea150324ee860976a74dff6b1947539`;
- `r40.patch.json`, SHA-256
  `c53d900d626aa54a75372e5e87c26d6f854e55158a8ccd57a5c049a11667010d`;
- `r40.audit.json`, SHA-256
  `758b22a0971ef9c760a1b05bb540777f2cd905ef0566bef7f97870da87a64d45`;
- `r48.patch.json`, SHA-256
  `f4270bf2921533e888bb3182cc041d239107664f753b861460185b596d20af34`;
- `r48.audit.json`, SHA-256
  `1574675aaaec5a86f95c40832a57d2225df1e7182d1c7229c18f5f7f67042f47`.

Source hashes:

- `scratch/patch_k17_h1_components_by_c6_20260802.cpp`,
  `a18d663f711368b9f3cf0b8d2ffcad7ccbf7aadc4e0893266e75e4e51f16cde7`;
- `scratch/audit_k17_local_p0_lollipop_chronology_20260802.cpp`,
  `47134d11eeed315bca480fdecee2df7bb2061db43b6a0b4761b25690531aa69c`.

## 2. Complete fixed-base C18-pair census

The supplied quotient catalogue has 6,127 individually cap-safe C18
circuits.  The 32 shards partition every unordered pair, exactly

`binom(6127,2) = 18,767,001` pairs.

For each pair the scorer rejects shared quotient facets, replays the combined
rank-10 cap, computes the exact local positive-residence update, and, for any
strict improvement, replays retained-path topology and the full cyclic
rank-11 through rank-16 union deck.

The exact aggregate is:

| counter | value |
|---|---:|
| raw pairs | 18,767,001 |
| shared-facet blocked | 3,529,940 |
| combined-cap blocked | 991,066 |
| residence nonimproving | 14,245,986 |
| topology blocked | 9 |
| strict-residence connected | 0 |
| exact candidates | 0 |
| best residence debt | 1,241 (the unchanged baseline) |

Therefore no disjoint pair in this fixed-base, individually cap-safe C18
catalogue gives a strict positive-residence improvement while retaining a
connected chronology.  Pairs sharing a quotient facet, triples,
non-equivariant moves, source rows, and the compiler are outside this
negative result.

Authoritative H100 root:

`/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/c18_repair_res1241/pairs`

The aggregate audit SHA-256 is
`b4cc18b3f3a92b8d3c57d3dcf58c9f859d6d36167b4f744d6167cc77b4027bd8`.
The immutable catalogue and all 32 shard audits are indexed by
`SHA256SUMS` and `SHARD_AUDIT_SHA256SUMS` in that root.

Source hashes:

- `scratch/search_k17_c18_pair_strict_clean_20260802.cpp`,
  `aded34497cfb29826ab4ae7d9337c4037f5855a3208d14fa9d6702592a1c83c5`;
- `scratch/aggregate_k17_c18_pair_strict_clean_shards_20260802.cpp`,
  `037c4f1120b913c33900ad1b3a4850f6c27ea48b45f618f66f05a5ccee416398`.

## 3. P3 minimum-hit selector budget ladder

On the frozen `res1581 / union698` P3 selector instance, budgets 8 through
15 are verified trivial-input UNSAT.  Budget 16 reached the 1,800-second cap
with exit 124 and is **UNKNOWN**.  Its 854,589,440-byte partial DRAT is not an
UNSAT proof.

Authoritative H100 root:

`/home/amodo/or15/work/p3_k17_res1581_union698_minhs_selector_20260802`

Hashes:

- `budget_loop.tsv`,
  `eb515bf152f890c2337aa7d1c945a8758bf6087bc13815576cffa235c57842ea`;
- budget-8 normalized proof replay,
  `400ee69e8e56f713ddf65c1a01693fb3068ae7a39d43c45ff5eb42c79e0f3fca`;
- budget-15 normalized proof replay,
  `c62375716dbd07ad442f643983af64c4e741ee84a3b63ccaccf413f7796de18c`;
- budget-16 partial DRAT,
  `c62a56057423c3e6a511e81022d703c83fdb986302307ca0193ce66d4184fff3`.

## Consequence for the active programme

Bare h=1 connectivity is now concretely materialized and is no longer the
main engineering uncertainty.  Conversely, local C18 pair repair of the
best 1,241-run quotient basin is exhausted.  The active route must select
connectivity, residence, and upper excursions jointly, rather than connect a
bad factor first or compound two members of this C18 catalogue afterward.
The literal lower compiler remains downstream of that joint outer gate.
