# Lower-target preservation after the actual 475- and 849-owner fusions

Date: 2026-09-08.

Status: exact finite verification of the fixed completed surgeries. The lower-bank interface survives both fusions. This remains a collection of cyclic sources plus the fixed linear prefix; it is not an optimal linear word or a simultaneous common-cap assignment.

## 1. Result

The two actual fusions preserve their affected components' rank-seven pair-union support and rank-six letter support exactly:

    mountain_135 + old_2(187) + old_8(153) -> giant_475,
    giant_475 + old_6(187) + old_7(187) -> giant_849.

For each move all four local support-difference lists are empty: rank-seven pair targets lost, rank-seven pair targets gained, rank-six letters lost, and rank-six letters gained. Thus these two lower-row preservation statements require no witnesses in other components. This is support equality, not a claim that the occurrence multiplicities are unchanged.

The global fixed-bank census is:

| Stage | Good cycles | Good source positions | Rank-seven good pair targets | Prefix targets added | Combined rank-seven targets | Rank-six good letter targets |
|---|---:|---:|---:|---:|---:|---:|
| After mountain, before 475 | 140 | 24,004 | 19,346 | 102 | 19,448 | 12,376 |
| After 475 | 138 | 24,004 | 19,346 | 102 | 19,448 | 12,376 |
| After 849 | 136 | 24,004 | 19,346 | 102 | 19,448 | 12,376 |

All good source letters have rank six, and every good adjacent pair union has rank seven, at all three stages. The unchanged 308-letter prefix has 191 distinct rank-seven letters; 102 are outside each stage's good pair palette. Both the combined rank-seven missing list and the rank-six letter missing list are empty at every stage.

There are consequently no missing rank-seven targets to test for legal one-letter cap hosts. This is a vacuous hole-repair check, not a new host-supply theorem. The older individual rank-at-most-six host statistics have not been recomputed or asserted invariant under these surgeries.

## 2. Why this needed a separate check

On a good upper-owner cycle T with positive coordinate runs of length at least four, the maximal depth-three cyclic antecedent is

    E_i = T_i intersect T_(i-1) intersect T_(i-2) intersect T_(i-3).

Its pair row is

    E_i union E_(i+1)
      = T_(i-2) intersect T_(i-1) intersect T_i.

Thus this lower rank-seven row is a triple intersection of upper owners, equivalently the complement of a triple union of lower owners. A theorem preserving lower-owner triple intersections, or only rank-eight adjacent facets, does not by itself prove this pair-row preservation. The separate finite check uses the actual new cycles and their literal maximal antecedents.

The fourfold-intersection letters also require their own support check. A residence bound proves legal replay but does not automatically prove that these letters still contain every rank-six target previously supplied by the changed components.

## 3. Exact verification method

The starting data are the actual post-mountain component bodies in `k17_second_clean_c6_topology_20260908.json`. The six original bad components are excluded and replaced by the active all-ports Johnson prefix, not used as intact cyclic backups. The prefix is the unchanged path

    116/33, 118/32, 122/31, 129/30, 138/29, 115/0,

in forward orientations, from `badsix_allports_johnson_306_owner_path.word` and `badsix_allports_johnson_308_depth2_source.word`.

For each good cycle the verifier forms its maximal antecedent and verifies at every cyclic position

    E_i union E_(i+1) = T_(i-2) intersect T_(i-1) intersect T_i,
    E_i union E_(i+1) union E_(i+2) = T_(i-1) intersect T_i,
    E_i union E_(i+1) union E_(i+2) union E_(i+3) = T_i.

It builds exact occurrence counters for letters and pair unions. For the 475 replacement it subtracts just the three affected components' counters and adds the literal new cycle's counters. It checks that the resulting component dictionary is exactly the pre-849 dictionary retained in the 221-parent catalogue. For the 849 replacement it again updates only the three changed components. Every updated counter remains nonnegative, and the good position total remains 24,004.

The independently formed antecedents of the two new cycles are compared entry by entry with `merged_475_depth3_source_cycle.word` and `merged_849_depth3_source_cycle.word`. The prefix's complete three-letter replay is checked against its 306 owners.

The support census exhausts all rank-six and rank-seven subsets of [17]. The local difference lists compare the affected old support directly with the new component support, and not merely their cardinalities.

No random search, new surgery search, matching, or cap solver is performed. All mathematical execution took place on h100, with a 90-second CPU limit, a 110-second wall alarm, and a 1-GiB address-space limit. The single fixed-stage audit passed.

## 4. Host and construction boundary

For a hypothetical missing rank-seven target S, the script implements the exact individual host test

    union over existing neighbors j of (E_i minus E_j)
        subseteq S subseteq E_i.

This is equivalent to preserving both neighboring original pair unions after replacing only E_i by S. No target reaches this test here, because the rank-seven missing lists are empty.

All rank-six targets currently appear as letters, so a future pair-preserving cap assignment must explicitly retain or reassign them. The 102 exceptional rank-seven prefix targets likewise require protected one-letter witnesses. Pair-union preservation by itself protects neither family of one-letter witnesses.

Further cycle fusions and the eventual linear opening need their own lower-row and host checks. The current stage still has 136 good cycles, the fixed shallow prefix, independent rank-eight repair and upper-support requirements, and an unsolved simultaneous lower compiler. The results here do not prove nu(17)=24,313 or an all-dimension equality theorem.

## 5. Artifacts

Local verifier:

    scratch/audit_k17_lower_bank_after_c6_fusions_20260908.py

Local exact output:

    scratch/k17_lower_bank_after_c6_fusions_20260908.json

Executed remote verifier and output:

    /home/amodo/exact-b-k17-second-c6-20260908/lower_bank_after_fusions.py
    /home/amodo/exact-b-k17-second-c6-20260908/lower_bank_after_fusions.json

The output records the three complete summaries, empty missing lists, both exact changed-component support differences, source-replay checks, and the explicit pre-opening scope. The terminal status was

    PASS exact fixed-stage lower-bank audit; no solver or additional surgery search.

Related earlier interface:

    scratch/K17_PBBS_GOOD_CYCLE_LOWER_BANK_AND_HOST_INTERFACE_20260908.md

Related completed fusion records and inputs:

    scratch/K17_SECOND_CLEAN_C6_TRUE_FUSION_475_20260908.md
    scratch/k17_second_clean_c6_topology_20260908.json
    scratch/k17_second_clean_c6_audit_20260908.json
    scratch/k17_six_plus_one_parent_catalogue_20260908.json
    scratch/k17_six_plus_one_selected_849_audit_20260908.json
