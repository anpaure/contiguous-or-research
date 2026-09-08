# Independent audit: K17 joint residence 1921 / deeper upper 1694

Date: 2026-08-02

## Verdict

The checkpoint
`/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/checkpoint_joint_res1921_deep1694/`
is independently promoted as the authoritative K17 joint carrier endpoint.

Checkpoint manifest SHA-256 is `abb3715e7f70dcfbb8917b061e8e8d591e542712091af944fb332c7a55639304`; model SHA-256 is `353a9e97239666e88f93b3fbf89fdee95240ef1a5099af408b28692f930a6f15`. Its copied parent manifest has SHA-256 `097ec68ba65380d442dcfe4018b673db3854729213847e12f4482707d99fc2ba`, exactly binding the promoted 1923/1702 checkpoint.

The audit is path-independent. It uses the 16,261-row guard bank stored inside the checkpoint and bound by that manifest at SHA-256 `e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc`. The previously mutated shared guard alias is not read or credited.

This is an endpoint/carrier promotion only. It is not a source, lower compiler, universal word, global-optimality proof, or proof that the remaining residence/deeper-upper defects vanish.

## Endpoint replay

Fresh incidence/map parsing verifies:

- 48,620 selected incidence edges;
- lower-root degrees ordinary 2, exceptional M 1, exceptional D 3;
- every owner degree 2;
- normalized boundary present;
- all 16,261 immutable guards satisfied;
- one augmented connected component;
- all 19,412 ordinary non-D rank-10 colours;
- all 19,448 targets in each licensed opening;
- provider histogram `[0,15108,3789,480,34,1]`;
- opening-0 short histogram `[1218,703]`, total 1,921;
- opening-1 short histogram `[1219,702]`, total 1,921;
- both rank-10-through-17 missing vectors `[0,1457,235,2,0,0,0,0]`, total 1,694.

The primary assignment was independently extended to all 1,093,878 variables. All 7,164,257 clauses and 22,659,207 literals of the frozen round-5 CNF replay satisfied.

## Upper containment

Literal missing-list comparison was rerun independently in both openings. Each parent list has histogram `[0,1463,237,2,0,0,0,0]`; each child list has `[0,1457,235,2,0,0,0,0]`. Lexically normalized set comparison gives exactly eight gains and zero losses in each opening. Parent and child missing-list hashes are respectively `ba721a7d...` and `c75a989c...`, with identical hashes across the two orientations.

## Exact three-circuit interface

The exact parent-to-target assignment diff uniquely selects all three rows of batch SHA-256 `e30c607c6f9756bfba64d6d6229f19a8bd59d59420763de6accfb21d7c5d55f7`:

| row | family | core | cyclic labels | roots |
|---:|:---:|---:|:---|:---|
| 0 | C6 | 28,842 | `0,6,16` | `28843,28906,94378` |
| 1 | star C8 | 41,329 | `3,10,14,12` | `41337,42353,45425,57713` |
| 2 | C6 | 53,810 | `0,6,10` | `53811,53874,54834` |

The circuits are independently root-applicable, root-disjoint, and edge-disjoint. All seven nonempty subsets pass exact degree, boundary, guard, q1, connectivity, both-opening and upper-containment checks. All six permutations have physical prefixes; no precedence constraint is needed. Canonical order `0,1,2` reconstructs the target byte-for-byte and yields:

| state | residence | deeper upper | cumulative gains/opening |
|:---|---:|---:|---:|
| parent | 1,923 | 1,702 | 0 |
| row 0 | 1,922 | 1,699 | 3 |
| rows 0,1 | 1,922 | 1,696 | 6 |
| rows 0,1,2 | 1,921 | 1,694 | 8 |

With `Phi = 2R + H`, the parent has 5,548, the target has 5,536, and `Delta Phi = -12`.

## Promotion boundary

The credited authoritative objective is Phi 5,536. Provisional Phi-5,533 candidates remain explicitly uncredited until they have a frozen checkpoint manifest and pass this same path-independent immutable-guard replay.

## Evidence

The root independent bundle is `scratch/audit_k17_joint_res1921_deep1694_20260802/root/`, with endpoint, exhaustive circuit, physical-prefix, containment-list, source, full-CNF, and input-hash evidence. Its persistent H100 root is `/home/amodo/or15/work/audit_k17_joint_res1921_deep1694_root_20260802/`.

A separately implemented independent bundle is at `scratch/audit_k17_joint_res1921_deep1694_20260802/defect_agent/`; its 33-entry manifest SHA-256 is `bd9c4886676b0f3ee95f5af32cdaec79665381d9936a7ab0f3f34f32b6e0787c` and verifies locally and remotely.

The 1923/1702 checkpoint and its corrected compound order remain preserved as direct ancestry; all earlier audits remain historical controls.
