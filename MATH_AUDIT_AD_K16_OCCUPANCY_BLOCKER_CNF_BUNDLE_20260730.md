# K16 interval-occupancy/blocker CNF bundle

Date: 2026-07-30  
Lane: AD  
Status: exact proof-pinned instances generated; no SAT or UNSAT solve

## 1. Mathematical and code pins

~~~text
MATH_THEOREM_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 2f52bc0bbcbc61d7ac0d22113bceb951d46610c0c526c0482160da6785f5a156

MATH_THEOREM_AD_K16_INTERVAL_OCCUPANCY_BLOCKER_COMPRESSION_20260730.md
SHA-256 7ffa70336bec21ea2ecd9c6af5625e5dedb30ab6fd152c5d8dd5746e54390509

scratch/build_ad_k16_12873_occupancy_blocker_cnf_20260730.py
SHA-256 203e2a914cfcd550045916faafaa6d44236b3e1af90d0a8e478624c33fa59faf

scratch/decode_verify_ad_k16_12873_occupancy_blocker_cnf_20260730.py
SHA-256 d8aa9dd1d11a931ccff885c3afcb2de2fedd2797c84eb4f77cca8ce16cf72f89
~~~

The emitter also byte-pins the authenticated length-12,874 answer, the
three-profile core source and JSON, and both theorem notes. It restores the
integer keys of the one serialized Counter before replaying the core payload.

The decoder requires a complete SAT assignment. Independently of the mutable
map, it byte-pins and replays the core audit, reconstructs the canonical
profile/deletion/blocks/positions, 57-target family, representative source
hash, complete variable partitions, exhaustive chart/base/required-bit
ledger, every count, and the entire ordered CNF clause sequence. It then
checks the assignment, reconstructs the unique occupied interval and block
for every target, intersects all active targets at every used cell, verifies
every actual maximal-context chart, materializes the 17 nonzero values, and
replays all 65,535 targets literally. Blocker bits are not decoded as word
bits. The emitter rejects aliased CNF/map outputs, and the decoder rejects
aliased candidate/audit outputs.

These changes close Findings 7.1--7.2 of

~~~text
MATH_AUDIT_AD_K16_INTERVAL_OCCUPANCY_BLOCKER_V2_20260730.md
SHA-256 24dd564ec1d4e87842e3fb31bc3357db43d4bf59de8ffa2239960f4e2eea3ea9
~~~

All four v3 map/CNF pairs pass the independent reconstruction through the
last provenance check; with an empty solver transcript, each then fails at
the intended SAT-status gate. Alias regressions fail before reading any
input artifact. The v3 CNF bytes are identical to v2, so an already running
solver on one of those exact CNF hashes remains logically usable with the
corresponding reconstructed v3 map.

## 2. Exact encoding audit

There are:

* \(57\cdot17=969\) target-position occupancy variables;
* \(57\cdot3=171\) target-block variables;
* \(17\cdot16=272\) blocker variables; and
* 1,412 variables in total.

The constraints are exactly:

1. one nonempty occupancy support per target;
2. occupancy-to-block implications and targetwise block AMO;
3. AMO on every pair of nonadjacent 0-to-1 run starts, giving one run;
4. occupancy-to-blocker implications for every omitted coordinate;
5. one common-coordinate row per cell; and
6. maximal-context durable rows triggered by the exact endpoint/neighbor
   signature of each possible interval.

The run-start clauses include every singleton, full-block, and one-sided
boundary support. Adjacent starts need no row because their definitions
already require their shared occupancy bit to be both zero and one.

The initial draft arithmetic for profile (5,9,3) was deliberately caught by
the emitter's independent total assertion and corrected before these frozen
files were emitted. Its unanchored total is 39,520, not 40,529. No formula
semantics changed in that correction.

## 3. Complete singleton-anchor instances

For target \(H=\mathtt{0x8000}\), pairwise AMO on its 17 occupancy variables,
together with its existing target ALO, forces one singleton witness. This is
WLOG and adds 136 clauses. The three complete profile instances are:

| profile | variables | clauses | CNF SHA-256 | map SHA-256 | payload SHA-256 |
|---|---:|---:|---|---|---|
| (4,9,4) | 1,412 | 39,196 | 975dcd4c5a44bf7947bfd3a390ed07ec9d7962877ee383a5c8aa98525c963099 | 546d200ddbbc3fb85725d9b8e4e561aaf0cf80e285f5f59b4fea781103ba602d | 93f11755eb2f90517725d1becf9eda879e0587e9e4c7ee45458fe67882d98916 |
| (5,8,4) | 1,412 | 37,118 | 1d6ae2c044d1a1c6aaaa1c4b7331d6e3c916c80e04702bb304dcdc21404d2b89 | f3aa5dcec3a056b13643c8c8a9233b330c773eed8e04ae298e69f34bea013c02 | 348ce42dc1dbe2a8f4427e380ead835d197b667a43f60783c0c35d29cbc96760 |
| (5,9,3) | 1,412 | 39,656 | 8aed0629470afc57738ab0093adb5ea899be90a9a6913fc94fb5a813e8827159 | 49e9b38813f8e7fa5d30dde734c831a612c04f7f5b50697202be745677b59de2 | da221e7cc0e7d4d5215a3bb6695a774fe57e0b5917de9800ba3e58f100010003 |

The files are

~~~text
scratch/occupancy_blocker_v3_4_9_4_anchorany.{cnf,map.json}
scratch/occupancy_blocker_v3_5_8_4_anchorany.{cnf,map.json}
scratch/occupancy_blocker_v3_5_9_3_anchorany.{cnf,map.json}
~~~

Every map payload replays exactly, every CNF byte hash matches its map, and
every file has exactly one header plus its declared number of clause lines.

## 4. Fixed-anchor regression

The exact (4,9,4) singleton branch at absolute shortened-word position 6436
uses 17 unit clauses: its occupancy is true there and false at the other 16
editable positions.

~~~text
scratch/occupancy_blocker_v3_4_9_4_anchor6436.cnf
SHA-256 ffc9ea2f38dca7c34a46d020efd9060d8e67ff3c4891c4523269cfc6af1f15fb

scratch/occupancy_blocker_v3_4_9_4_anchor6436.map.json
SHA-256 c801576eb99c5e4142af328bb01b1247a55af563b6a3ff470bcc4b3d379079d3
payload SHA-256 73d25ec91fe6329d7b59ba77b886f1fd87943bef337f10ace190fc2b1f767fed
~~~

It has 1,412 variables and 39,077 clauses. This is one restricted anchor
branch, not a complete profile model.

## 5. Proof scope

SAT plus the frozen decoder and full replay proves a literal length-12,873
word. Proof-checked UNSAT of one of the three anchor-any instances closes
its entire fixed-gap shortening profile. A timeout or resource exit is
UNKNOWN. No solver has been launched for these instances.

None of these models covers a changed fixed gap, a moved separator, a
cross-gap braid, or an arbitrary word outside the three shortened profiles.
