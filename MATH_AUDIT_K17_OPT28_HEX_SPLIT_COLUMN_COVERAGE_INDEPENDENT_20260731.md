# Independent audit of the K17 OPTIMAL28 split-hex column extension

Date: 2026-07-31  
Status: exact catalogue/coverage replay; no compatible packing or K17 word is claimed

## Verdict

The current split-hex catalogue passes an independent literal replay.

* The lower-rainbow factor has `48,620` selected rank-eight/rank-nine
  incidences on `24,310` owners and `24,310` lower colours.
* The fixed complementary macro interiors contain exactly `724` strict bad
  runs in `257` components: `320` of owner length two and `404` of owner
  length three.
* Exhaustive independent enumeration gives `44,917` alternating incidence
  hexagons, `27,933` whose three changed owners avoid the marked packet, and
  `5,433` which also remove an incidence supporting at least one old bad row.
* All `5,433` exported records agree literally with the independent
  enumeration, including the six incidences, three source-edge rethreads,
  hit rows, and hit components.  Their canonical column payload is
  `3807e024ab8dbd711b49671b7af88ed1fe77bc73ec2360599497e5a3249d0aac`.
* Every one of the `724` rows has active supply.  Row degree is `2..34`; one
  column hits at most five rows.  The hit profile is
  `1^2947 2^2115 3^263 4^103 5^5`.
* All `257` bad components are touched.  In particular, all `106` components
  in the relaxed scalar-floor witness have column degree `5..225`.

This proves local supply, not repair.  A hit only certifies that a necessary
support incidence changes.  Selected columns may conflict, create fresh
short runs, disconnect the factor, lose upper witnesses, or fail common-cap
recourse.

## Fail-closed separation from residual pure-U circuits

Let `I` be the union of the selected incidences supporting the `724` strict
component-interior rows.  Every incidence in `I` is incident with a tagged
`A/X/Y` macro owner.  A residual pure-`U` circuit changes only incidences of
untagged old-only rank-nine owners.  Therefore

\[
       \operatorname{supp}(\text{pure-}U\text{ circuit})\cap I=\varnothing.
\]

This holds for a residual circuit of any length, not only a `C6`: residual
port circuits cannot touch even one of the `724` interior support rows.

The upper obstruction is independently unchanged.  Allowing all `4,872`
residual pure-`U` owners to choose arbitrary capacity-positive port pairs
still leaves exactly `218` rank-ten targets with zero support, payload
`cda1d49d62b377782acbc82764bfd19fb0aee65121bbe91189d3833d7d6a29de`.
Thus pure-`U` pairing/circuits alone can repair neither the component-interior
floor nor these `218` upper targets.

Every active split hex genuinely leaves that fibre: its owner-vertex profile
by number of pure-`U` owners is `0^3896 1^1537`; it is never three.  Equivalently,
each active column changes incidences of two or three tagged macro owners.
There are `7,216` all-pure-`U` alternating hexagons in the authoritative
OPTIMAL28 factor (`6,535` avoid marked owners), and none is active on an
immutable row.  The older `7,225` residual-`C6` count belongs to a different,
parent-induced carrier and must not be substituted here.

## Direct upper-q1 reach of the active columns

For each active column and each of its three source colours, the independent
audit replaces

\[
  w^{\rm fixed}\cup w^- \quad\text{by}\quad
  w^{\rm fixed}\cup w^+ .
\]

Against the independently reconstructed `218` zero-support targets:

* `355` active columns create at least one target: `346` create one and `9`
  create two;
* their union contains `154` targets, with target column degree `1..8`;
* `64` targets have no direct baseline-to-single-active-column gain;
* the `355` joint columns touch `289` old bad rows in `113` components;
* restricting to columns that lose no currently unique rank-ten colour leaves
  direct coverage of `98` targets.

The opened-target payload is
`737e701b53899e008d5f15161ebe8d81b1de4863540612b27cdc837beb54dbf9`;
the `64`-target residual payload is
`9671c65734465f4f173d3c1919a3d2c90cc345059667bcf7b1e5bda88cf4b86a`.

The `64` count is a single-column screening statement, not a packet no-go.
Overlapping hexes can change both endpoints of a colour and create an upper
pair absent from every individual baseline delta.  Exact binary incidence
bounds and literal post-composition replay remain mandatory.  Across all
`27,933` marked-safe minimum hexes, including columns that do not hit a
current bad row, `217/218` targets have a direct one-hex gain; the lone
exception is target `63302`.  Across hexes that may touch marked owners all
`218` have a direct gain.

## Three distinct column universes

| universe | exact size | semantics | composability |
|---|---:|---|---|
| radius-one occurrence states | `1,430` alternatives; `438` preserve all 134 marked/optional components | change one retained rank-six parent-colour occurrence and rebuild the complete 1,430-macro atlas | whole states, not additive columns; best remaining tax is `718` |
| complement edge exchanges | `545,721` alternatives on `20,201` complement-interior colours | assign one rank-eight colour an alternative complement-owner pair | colour-preserving but not owner-degree neutral alone; `6,419` rows over `5,220` colours support the 218-target set |
| active split hexes | `5,433` of `27,933` marked-safe minimum hexes | couple three source-edge rethreads into one alternating six-incidence circulation | exactly owner- and colour-degree neutral individually; binary incidence conflicts and all physical replay still apply |

The radius-one occurrence census is therefore not the split-column
extension, and the `545,721` local pair choices are not individually legal
factor circuits.  The active hex catalogue is the smallest additive
palette-preserving rethread layer.

## Frozen provenance

Current producer theorem provenance is coherent after correction:

```text
scratch/audit_threadD_k17_opt28_hex_variant_catalogue_20260731.py
SHA-256 0a9daacc04c7754e70d674f862d66d03d13842fe6153bf520ac6fcfd2ad99cd0

scratch/threadD_k17_opt28_hex_variant_catalogue_20260731.audit.json
SHA-256 9ac6416078d73676ca63d483cf30540806ef14f588f77bf8301d0ca5b919a87e
payload ba0fce17bfe13d491cbb2cf229d3f070e75def80b50de854d89af226e5d24923

MATH_THEOREM_THREAD_D_K17_OPT28_MINIMAL_HEX_VARIANT_STATE_20260731.md
SHA-256 6d27374be992b57c6fc6b751af5ac9f39fd68fe9ab047a62bb5d8a7e38e3c49a
```

Independent replay:

```text
scratch/independent_audit_k17_opt28_hex_split_column_coverage_20260731.py
SHA-256 bf64c0dd90df691953dc13fb55e4e55d72c5d555ff4bef383c507602f9366b79

scratch/k17_opt28_hex_split_column_coverage_independent_20260731.audit.json
SHA-256 46f0a54941b75cacf17431bfd1d8169cb602120fd01f2bafc7cd523d387177f2
payload 3d1d357b33344fbcedcf9c40908833e52f0f66a576f0b0aea2e19879fed5a10b
```

Other frozen inputs used by the replay:

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json
SHA-256 4e3129d2604d3e41c226efa3bea71a203180538710dd97272cc734e23412441b
payload f1ab56555d744d2e527325c8617c2af1ee0f463ad13666f153d56efc588624db

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.result.json
SHA-256 b60341b5cee0de1884d3af6561d8247722bad879d7b5322ca21d94f60472e351
payload 2440ee4a506932c4e7903dc327a6c8445c5c3c7b310c0e748d4520566c14ffae

scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa

scratch/ad_k17_opt28_depth2_local_provider_state_20260731.audit.json
SHA-256 bcaa076f8844787093b4b5aad98db0186289f5cea66ebc83e45ce20f2eadbbc0
payload fe9bcb8ae361e02be1782d37ff89244bea3779f60b8ee055b568233684229418

scratch/k17_opt28_complement_occurrence_columns_20260731.census.json
SHA-256 7966aea624932fa51cc00d7b302f0722873293b26b3538f38a8639615985710b
payload 6745af3e59aec09dd0d788fbfeedbd1cf36b956e3968fc25fa3a5e9ed4a2267d
```
