# Final 1513-stage lower-bank audit

Date: 2026-09-08.

Status: exact bounded incremental verification, PASS. The two latest completed good-cycle fusions preserve the rank-seven pair and rank-six letter occurrence counters exactly. All mathematical execution was on h100. No host matching or further finite search was performed.

## 1. Exact result

The actual replacements are

    giant_849 + old_4(187) + old_5(187) -> giant_1223,
    giant_1223 + mountain_103 + old_3(187) -> giant_1513.

For each replacement the old affected components and the resulting cycle have identical rank-seven adjacent-pair-union counters and identical rank-six letter counters in their maximal depth-three sources. Every local target lost/gained list is empty and every signed occurrence-difference dictionary is empty. This is stronger than support equality and requires no outside backup for either lower row.

The global fixed bank has the following exact values:

| Stage | Good cycles | Good source positions | Rank-seven pair targets | Original protected prefix targets | Combined rank-seven targets | Rank-six letter targets |
|---|---:|---:|---:|---:|---:|---:|
| 849 | 136 | 24,004 | 19,346 | 102 | 19,448 | 12,376 |
| 1223 | 134 | 24,004 | 19,346 | 102 | 19,448 | 12,376 |
| 1513 | 132 | 24,004 | 19,346 | 102 | 19,448 | 12,376 |

Every good source letter has rank six. Every good adjacent pair union has rank seven. At every stage all rank-seven targets are covered by good pairs together with exactly the original 102 exceptional prefix masks from the first lower-bank census. The additional prefix target set was compared as a set with that original retained list, not merely by cardinality. It is unchanged. All 12,376 rank-six targets remain present as good-cycle letters.

Thus the completed 1513-cycle stage retains the lower-bank interface previously verified through 849. This closes the pending rank-seven/rank-six finite audit in `K17_NINE_COMPONENT_1513_FUSION_AND_PARENT_FAMILY_SATURATION_20260908.md`.

## 2. Inputs and exact verification

The baseline is the actual post-849 `current_lower_cycles` dictionary in `continuation_from_849_catalogue.json`. The six original bad components are excluded. The same actual 306-owner path and 308-letter source replace them throughout. The prefix owner sequence is checked equal to the one stored in all three continuation catalogues, and every three-letter prefix replay is checked.

For each good upper-owner cycle T, the independently formed source is

    E_i = T_i intersect T_(i-1) intersect T_(i-2) intersect T_(i-3).

At every position the verifier checks the exact pair, triple, and four-letter identities

    E_i union E_(i+1) = T_(i-2) intersect T_(i-1) intersect T_i,
    E_i union E_(i+1) union E_(i+2) = T_(i-1) intersect T_i,
    E_i union E_(i+1) union E_(i+2) union E_(i+3) = T_i.

It initially builds the baseline letter and pair occurrence counters. For each new surgery it subtracts only the three affected components' counters, constructs the one new component, and adds its counters. All updated counts remain nonnegative and the total remains 24,004. The resulting whole component dictionary is checked equal to the next actual continuation catalogue.

The independently constructed 1223- and 1513-owner sequences and their antecedents are compared entry by entry with both corresponding literal owner and source files. The rank-six and rank-seven global target checks exhaust their complete Boolean layers. The new counters are also compared directly with the old affected counters, yielding exact local multiplicity equality for both surgeries.

The original protected prefix masks are read from the first canonical-bank JSON, `good_cycle_lower_bank.json`. Their number is 102, each is still a rank-seven prefix letter, and their union with the current good pair support is the entire rank-seven layer at each stage.

The run used limits of 90 CPU seconds, a 110-second wall alarm, and 1 GiB of address space. This was one fixed two-step incremental audit; no new candidate was selected and no construction solver was run.

## 3. What is and is not transported

The rank-seven good pair witnesses are protected by any future operation that actually preserves their pair unions. The exceptional prefix targets have one-letter witnesses and still need explicit protection against later common caps. All rank-six targets likewise currently have one-letter witnesses and must be retained or reassigned during the lower-target compiler.

This audit does not transport the original individual-host multiplicities or prove a simultaneous cap assignment. Its positive counter result also does not certify arbitrary future cuts, joins, or common caps.

The current bank remains 132 cyclic good sources plus the fixed linear shallow prefix. The cyclic closures are present, and no optimal linear opening is supplied here. The independent rank-eight defects and the unsolved global construction requirements remain. No new value of nu(17) or proof of nu(k)=B(k) is claimed.

The requested finite checks stop at this completed audit.

## 4. Retained artifacts

Local script:

    scratch/audit_k17_lower_bank_849_to_1513_20260908.py

Local exact JSON:

    scratch/k17_lower_bank_849_to_1513_20260908.json

The JSON contains all three summaries, the unchanged original 102-mask list, both exact component-delta records, empty lower missing lists, and source/catalogue equality checks.

Actual continuation inputs and literal cycles:

    scratch/k17_1513_sector_fusion_20260908/

Executed remote script and output:

    /home/amodo/exact-b-k17-second-c6-20260908/lower_bank_849_to_1513.py
    /home/amodo/exact-b-k17-second-c6-20260908/lower_bank_849_to_1513.json

The terminal status was

    PASS fixed incremental849-to1513 lower support audit; finite checks stop here.

Earlier lower-bank record:

    scratch/K17_LOWER_BANK_AFTER_475_AND_849_FUSIONS_20260908.md
