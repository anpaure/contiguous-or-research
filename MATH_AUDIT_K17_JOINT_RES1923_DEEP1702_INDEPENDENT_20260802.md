# Independent audit: K17 joint residence 1923 / deeper upper 1702

Date: 2026-08-02

## Verdict

The frozen checkpoint at
`/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/checkpoint_joint_res1923_deep1702/`
is independently promoted as the authoritative K17 joint carrier endpoint, with one mandatory correction to its compound-move interface.

The static endpoint, the complete round-5 DIMACS replay, and a corrected physical circuit order all pass. The table's declared row order `0,1,2,3` is not a valid physical composition: its third prefix (mask 7) disconnects the factor. Exhaustive subset/order replay finds 12 valid orders; `0,1,3,2` is the frozen canonical replay used here.

This is an endpoint/carrier promotion only. It is not a source, lower compiler, universal word, global-optimality proof, or proof that the remaining residence/deeper-upper defects vanish.

## Frozen checkpoint and ancestry

- model SHA-256: `7a80fe02517039df87bcf7f88860b1bbf201482952c1317bfbcd6aeb9d435a2c`
- checkpoint manifest SHA-256: `097ec68ba65380d442dcfe4018b673db3854729213847e12f4482707d99fc2ba`
- producer independent report SHA-256: `40ccf578cfe9cdac77f4e25806966784f65f5b9a3116b56d1953c6b4d717ffbd`
- producer containment report SHA-256: `74fd86d4d9235c0900427219bcce8f0a5568e9e5cdefece6157a934617760092`
- containment table SHA-256: `5f5d0cc71dd42599489bedcea7277ae38a90e69d0b56aa50df9123784aa06d7b`
- four-row batch SHA-256: `ced90034bca1cc94eec14a99deef850f34ecbb2439942a257656fc1da005ada0`
- copied parent manifest SHA-256: `44171fe48b108a2ec3b9bd10ea18daba52ba76b9b269168a3502c0ca6e6ab113`

The copied parent manifest is byte-identical to the frozen 1926/1712 checkpoint manifest and binds parent model SHA-256 `978386dff296a61195781aa23d0b4c85f0c671eb0ac59355a61aaa5e4851fbc3`. Thus 1930/1721 and all earlier checkpoints remain ancestry rather than competing promotion roots.

## Independent endpoint replay

Fresh parsing from the incidence/global maps and the immutable 16,261-row guard bank verifies:

- selected incidence edges: 48,620;
- lower-root degrees: ordinary 2, exceptional M 1, exceptional D 3;
- every owner degree: 2;
- normalized boundary: present;
- frozen guards: all 16,261 satisfied;
- augmented topology: one component;
- ordinary non-D rank-10 colours: 19,412 / 19,412;
- both licensed openings: 19,448 / 19,448;
- provider histogram: `[0,15106,3793,478,34,1]`;
- opening-0 short histogram: `[1218,705]`, total 1,923;
- opening-1 short histogram: `[1219,704]`, total 1,923;
- both rank-10-through-17 missing vectors: `[0,1463,237,2,0,0,0,0]`, total 1,702.

The primary assignment was independently extended to all 1,093,878 variables. Streaming replay satisfies every one of 7,164,257 clauses and all 22,659,207 literals in the frozen round-5 CNF.

## Exact compound interface

The exact parent-to-target assignment diff is the union of all four batch rows: two octahedral C8 circuits followed by two C6 circuits. Geometry is inferred from incidence endpoints rather than trusted from table labels.

| row | family | core | cyclic labels | root count |
|---:|:---:|---:|:---|---:|
| 0 | octahedral C8 | 49,734 | `4,7,5,12` | 4 |
| 1 | octahedral C8 | 1,205 | `1,14,8,16` | 4 |
| 2 | C6 | 68,485 | `1,3,6` | 3 |
| 3 | C6 | 55,436 | `4,9,13` | 3 |

All four circuits are root-disjoint, edge-disjoint, independently applicable at the parent, and their union reconstructs the target byte-for-byte.

All 15 nonempty subsets and all 24 permutations were replayed. Exactly three subsets are nonphysical:

| mask | rows | failure | component sizes |
|---:|:---|:---|:---|
| 5 | `0,2` | disconnected | `35,882 + 12,738` |
| 7 | `0,1,2` | disconnected | `35,882 + 12,738` |
| 13 | `0,2,3` | disconnected | `32,798 + 15,822` |

Therefore the minimal exact interface is:

> Rows 0 and 2 may not coexist in a proper prefix. Equivalently, the later of rows 0 and 2 must be the final move.

This rule admits exactly 12 of 24 orders. The producer order `0,1,2,3` violates it at prefix mask 7. The canonical repaired order `0,1,3,2` has every prefix physical and yields these objective states:

| state | residence | deeper upper | both-opening q1 |
|:---|---:|---:|:---:|
| parent | 1,926 | 1,712 | full |
| row 0 | 1,925 | 1,709 | full |
| rows 0,1 | 1,925 | 1,704 | full |
| rows 0,1,3 | 1,924 | 1,703 | full |
| rows 0,1,3,2 | 1,923 | 1,702 | full |

Every repaired prefix also retains exact degrees, normalized boundary, all guards, one connected component, and both openings. The terminal containment comparison has zero losses and ten gains in each opening. With `Phi = 2R + H`, the parent has 5,564, the target 5,548, and `Delta Phi = -16`.

## Shared-input race and fail-closed repair

During this audit, the mutable shared path
`.../exact_q1_stage/cumulative4.cuts.cnfpart`
was overwritten after the first passing runs: its expected SHA-256 `e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc` and 16,261 rows became SHA-256 `7ec90c9359444fd2f7b3d1301c724e9e2693781476d4c3a9724468989a2ac72f` with six rows. Fresh auditors correctly rejected the six-row file by clause census.

The exact immutable 16,261-row bank was copied into the unique audit root as `frozen.cumulative4.cuts.cnfpart`; the endpoint, corrected prefixes, all subsets, and all orders were rerun against that copy and passed with identical reports. The mutated shared path is excluded from the frozen audit.

The other authoritative inputs remained stable:

- incidence map: `80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a`;
- global map: `d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63`;
- round-5 CNF: `e9b15f2d46640162e28feaae66e50f8e4e939ae6a433bb0e7ff1bf2c2b472011`.

## Evidence

The local frozen bundle is `scratch/audit_k17_joint_res1923_deep1702_20260802/root/`. Principal files are:

- `frozen_circuits.audit.json`: exhaustive subset/order audit;
- `frozen_circuits.subsets.tsv`: exact subset topology and metrics;
- `frozen_circuits.orders.tsv`: all 24 permutations;
- `frozen_valid0132.stage_summary.tsv`: repaired physical-prefix replay;
- `target1923.fullcnf.audit.json`: complete DIMACS replay;
- `COMPOSITION_INTERFACE.audit.json`: solver-facing minimal interface;
- `INPUTS.sha256`: checkpoint, ancestry, maps, guard bank, and CNF bindings.

The persistent H100 audit root is
`/home/amodo/or15/work/audit_k17_joint_res1923_deep1702_root_20260802/`.

Historical independent results remain preserved, including the 1930/1721 bundle at `scratch/audit_k17_joint_res1930_deep1721_20260802/defect_agent/`, the 1926/1712 second audit at `scratch/audit_k17_joint1926_packet_second_20260802/`, the exact depth-3 owner-payload audit, and the res1994 defect/compound catalogues.
