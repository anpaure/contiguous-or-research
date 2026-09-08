# Audit: AD `k=17` all-opening Benders v5 executable replay

Date: 2026-08-02

## 1. Verdict

PASS for the claimed executable scope.

The v5 implementation authenticates the marker58 factor interface,
enumerates all 48,620 directed openings, emits incumbent-guarded selector
cuts, materializes exact upper and Hall/DM data on requested roots, and
publishes a SAT common-cap word only after total-model and dual exhaustive
verification.  The final2397 and clean1581 `k=17` controls are definitive
source-negative calibrations.  The upper/DM and SAT common-cap branches are
executed by independent `k=13` and authenticated `k=15` controls.  The
fail-closed `UNSAT_PROOF` mapping is source-audited but was not dynamically
reached by a source-ready `k=17` root.

No authenticated source-ready resident `k=17` model was available.  No
`k=17` word was emitted.  A pathname-only `UNSAT_PROOF` is nonterminal and
never contributes to a cut or global no-good.

## 2. Frozen predecessor boundary

The v4 theorem and replay audit were not edited:

```text
c00afc94cd3ebae75d41b3dccd6fc2563f8a77345b5ff3df1154ae714cfd786e  MATH_THEOREM_AD_ALL_OPENING_PRIMARY_BENDERS_AND_DM_INTERFACE_20260802.md
4a450ea7a3885f592ea6764ede6afd03d2bc7585dc5be0342e866cd00b3b821c  MATH_AUDIT_AD_K17_ALL_OPENING_PRIMARY_BENDERS_REPLAY_20260802.md
63e43380a14c970249ee73890e3b620a6cf0af5dfd71247d8f6954a53059d4e7  build_ad_k17_opening_benders_primary_interface_20260802.cpp
3d25b015cb5f2a97ec0c6ceb9f1011478dc31b710f65ed5a45efc67e608ddbdd  verify_ad_k17_opening_benders_primary_interface_20260802.cpp
```

V4 proves source/provenance and the guarded-cut interface.  This audit does
not retroactively describe v4 as an executed deep oracle.

## 3. Execution environment and build

All heavy compilation and replay ran on the H100 host CPU only:

```text
host: arboghast
root: /home/amodo/or15/work/ad_v5r_root_019fc04bf4d7_20260802
flags: -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic
GPU: unused
```

The five final warning logs are empty.  Final binary hashes are:

```text
af281040cb1b863a95c5e4e5c5aa20ced7a34aeaa5bedba824ee3b39ccc64656  ad_v5
4a0885951952a2b37ac35f8aacd8416d019464544a8b66eeb7e481c127cb4003  verify_k17
8f55659540eb07bfd3fa5d2f6b02014fddbe86c6fdef9eefa52d1b2bacf670ab  verify_cycle
3621dd8c58992d72af756805d25f52734f2d92b987008eec073d9a92da72408d  verify_sat
e8997a553b8c567677fae1bdb27a6e02041bb27199228bac67338755c80016ed  verify_word
```

Principal source hashes are:

```text
e85b9aa0b54a0856aa7d8171a1f535528ac988c0de4bed94594e5c610469ed9a  build_ad_k17_all_opening_benders_v5_20260802.cpp
1ff83d792a02d134698bbff7335d655fcbaac81f10096e2e90053c88e9c651d4  verify_ad_k17_all_opening_benders_v5_20260802.cpp
8f662a22c90d006833f2c98e1c7e7eeac9843255dd938097b0410c85647627b9  verify_ad_benders_v5_cycle_hall_control_20260802.cpp
7372d11f99e04a554b3c3838f0f87f4f2d62c1e136e727f3e7c2a819dfe0ccae  verify_ad_benders_v5_commoncap_sat_control_20260802.cpp
0bde69820a62277cf381bb1c076cba187e4cf0d5bb00def860caa88cdc73cc64  verify_ad_commoncap_unsat_receipt_v5_20260802.sh
```

## 4. Authenticated inputs

The package binds the following principal inputs:

```text
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3  final2397.map.tsv
88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403  final2397.witness.tsv
9aa9c8137b4b90508aa255536a6f683bfa448b60de497b498f7119e432eb24ec  final2397.model
eba52226952cda38d74e98fc7463f54640b0b59736ff88fc2949c8f0c02de1eb  final2397.factor.tsv
178a91fc4979f359448704085a6ae92f41caff9bf8cb23ab5713a4475af98cfe  clean1581.model
14903257c9dd4082ef571a82aefea753a5cda958807d90958f5e43454d2c9497  clean1581.factor.tsv
c23709d973f2652ce98843f4cd1ae1deb31f9312743e0c802f835554bca4aa98  k13 cycle
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b  k15.word
2812a4f32ef098408006fb3e9f035cb3d350397d1781a03ebe11828aa123209e  k15.owners.tsv
09c859b4c3a5c3b136afde4d00d9011a80959cb61418a6ffe8f3973b8873f866  k15.commoncap.cnf
ffb20c9bc36bc603d665a9e0161432eeac7a63bb6cc5c51276905078fa1f7db2  k15.control.model
017f05fa1b4a642688c246064d303d70d267683aca21befafd78bf1decd8dea3  k15.maximal.verified.word
```

The two `k=17` models are `sparse-control` calibrations.  They authenticate
the complete determinant-primary assignment and factor binding, but do not
claim complete combined-master CNF replay.

## 5. Branch matrix

| Branch | Executed fixture | Principal result | Independent result |
|---|---|---|---|
| all-opening source and selector guards | final2397, clean1581 | PASS | PASS |
| all-opening upper classifier | `k=13` cycle | PASS, all 3,432 counts | PASS |
| exact P/U/M Hall and DM schema | `k=13`, root `127 -> 4191` | 3,984/4,095, deficiency 111 | exact shore/q replay PASS |
| generic positive compiler | authenticated `k=15` word | 16,383/16,383; word emitted | 32,767/32,767 PASS |
| common-cap SAT publication | authenticated `k=15` path/model | 621,905 clauses; dual scans PASS | exact CNF/provider/derivative/dual replay PASS |
| common-cap UNSAT token | no source-ready `k=17` root and no authoritative proof interface | not dynamically reached | forced UNKNOWN by audited code path |
| resident `k=17` publication | no eligible input | not run | no claim |

## 6. `k=13` upper/Hall/DM replay

The fixture contains 1,716 owners and 3,432 directed openings.  Every
opening passes source.  V5 records 108,108 owner/upper-target incidences; an
independent implementation reconstructs every opening's upper count.  There
are 1,976 upper-failing directed openings, with at most three missing upper
targets.

At the selected root `127 -> 4191`:

```text
upper holes:                 0
strict-lower targets:        4,095
short cells:                 5,154
candidate incidences:        20,156
maximum matching:            3,984
deficiency:                  111
canonical Hall shore:        453 / 342
DM q cells outside N(A):     4,812
```

The independent verifier reconstructs the physical chronology, exact source,
all nonwrapping unions, every P/U/M candidate, the Hall neighborhood and
matching, and the exported DM target/q/row schema.  It checks that the q-cell
bank is exactly the complement of `N(A)`.

Frozen audit hashes are:

```text
56d60c1b1297fa0064d2a2a31187a988eac55e972962412c482c2da73ee841c0  freeze_k13.audit.json
3613a56207c76096d48ce330a2c87dab5a4617afbdc276eb2769f44d7a17893d  freeze_k13.root_127_4191.audit.json
eb2e300bcb8523133153c3ba679f2335a80bbe51bc9a1e56fd66829cfa774835  freeze_k13.independent.audit.json
```

This fixture deliberately excludes determinant-primary binding and
common-cap simultaneity.

## 7. Authenticated `k=15` positive and SAT replay

The generic positive control reports:

```text
PASS_UNIVERSAL_REPLAY_WORD_EMITTED ... matching=16383 word=1
PASS covered=32767/32767 length=6438
```

Its regenerated CNF, total model, owners, and emitted word are byte-identical
to the authenticated controls.  Audit hashes are:

```text
e88870c0dc8729e80eb6095260416159ec3c9d0f7958e082bffcd83947f5e0e6  freeze_k15_generic.audit.json
9af3c323b4a53334425a1a7bea4fe111beafdeaa72c81cc01af7e89e38f2bf8c  freeze_k15_generic.independent.audit.json
```

The explicit `path-control` SAT replay records:

```text
owners/source letters:       6,435 / 6,438
upper holes:                 0
strict-lower targets:        16,383
short cells:                 19,311
candidate/providers:         137,238
matching:                    16,383 / 16,383
CNF variables/clauses:       169,440 / 621,905
covered, start scan:         32,767
covered, frontier scan:      32,767
start intervals/frontiers:   122,031 / 70,741
```

The primary path-control binds inputs before and after replay and installs
the output word only after all checks.  The independent verifier regenerates
the exact CNF byte-for-byte, replays all clauses and provider semantics,
rebuilds the derivative, and repeats both exhaustive scans.

```text
e2ae776f3a35626c1f3c9225ea5b47edac95a71f61e3ae67965f57b9218a9dac  freeze_k15_sat.audit.json
e9d243143e2a289f96875a487fb23fd601a4405a977af4b0f56288907bf8337e  freeze_k15_sat.deep.audit.json
f70a5de9d664feb1b214680329427df44aa2da0dc4571f87de03af40b700a378  freeze_k15_sat.independent.audit.json
```

Two publication controls also pass by rejecting the operation: an existing
word cannot be overwritten, and an output pathname cannot canonically alias
an authenticated input pathname.  The previously emitted word hash remains
unchanged.  Distinct hard-link names are not inode-compared by this gate.

## 8. `k=17` all-opening replay and guards

For final2397, the primary and independent runs report all 48,620 directed
openings exactly once.  Every opening is `SOURCE_FAIL`; minimum residual
short runs are 2,395.  The source core has two runs, eight bracket edges, and
six determinant primaries.

The concrete extension contains 48,620 selectors, a Sinz at-most-one bank,
the conditional at-least-one row, selector-to-guard links, and the full
35,713-primary assignment guard.  The audit's guard variable is 132,953.
It independently verifies that all local selectors are false off incumbent
and exactly one is selected on incumbent.  The final hashes are:

```text
c90e8c25fcd3389f45f1aa864b605207a85332942b927125e1818600fa73ea16  selector extension CNF
e98ae498cd221ff0009ec7b191dbf0a8508ac990ce86d5f348ce0c6a5150f529  guarded cuts CNF
c449e7804bcdc0b407219f3416f54942e606995dba051a1299de2c6d68563c37  freeze_final2397.audit.json
41295696b5e2366a0a2f63a2ed2321f9fde60640c6132cdbbf582e71d2c2ff60  freeze_final2397.independent.audit.json
```

For clean1581, every opening is also `SOURCE_FAIL`; minimum residual short
runs are 1,579 and the source core is two runs, six edges, five primaries.

```text
6d5563ece3187c169b94cb9d7439e5e37a25c5e9d2bb8683d5201d6d75295eb9  freeze_clean1581.audit.json
d7003fa993aa0582fb25fb211809ace7c9d72bf50fb3cb0dc83e518cd3d08c61  freeze_clean1581.independent.audit.json
```

Both primary terminal lines are:

```text
PASS_ALL_OPENINGS_TERMINAL_GLOBAL_NOGOOD source=48620 upper=0 hall=0 pending=0 word=0
```

This is a definitive all-opening source-negative result for each exact
factor, not a `k=17` residence or word result.

## 9. Fail-closed review

The audit checked the following publication boundaries:

- local cuts contain a root selector;
- root selectors imply the exact incumbent guard;
- the guard is equivalent to the complete signed primary assignment;
- the exact-1,198 selected-factor no-good is scoped to the marker58
  exact-cardinality face;
- a Hall row is described as strong only under exact `q` iff candidate links;
- `UNSAT_PROOF` is always mapped to `COMMONCAP_UNKNOWN`;
- any pending or unknown opening prevents the global no-good;
- a word is emitted only by the total SAT replay plus two exhaustive scans;
- no-replace and canonical-path-alias checks run before publication.

The shell receipt
`verify_ad_commoncap_unsat_receipt_v5_20260802.sh` has schema
`ad-commoncap-unsat-path-receipt-nonterminal-v1`.  It is diagnostic only and
the production executable never trusts it.

Because every authenticated `k=17` opening failed source, no production
replay reached a Hall-perfect root carrying `UNSAT_PROOF`.  Accordingly this
audit claims the implemented fail-closed mapping, not execution or
verification of an UNSAT certificate branch.

Independent post-patch review found no production soundness blocker.  A
future hardening may add directory-descriptor pinning and directory `fsync`;
that is durability hardening, not a change to the current no-replace semantic
gate.

## 10. Resident integration audit

This section records a final read-only observation of external H100 state.
The observed lineage and live-process state are not members of the 143-entry
v5 package and are not covered by its manifest.

No authenticated source-ready resident `k=17` model was found at freeze.
The newest authenticated factor lineage, `promoted_c18_pair0104`, has:

```text
factor SHA-256: d458d19839a143648aee72fac9cd9bfba88d1c22c72bd13656731790c39211b1
model SHA-256:  860b84d7f755dcd60738eeda1377a2c1f460d5264bcbdf2673b2bf969101b7c
short positive runs: 1,496
source gate: FAIL
deep upper: rank11 10,914/12,376; rank12 5,967/6,188
```

It is nonresident, source-failing, and upper-incomplete, so it is ineligible
for v5 resident integration.  The relevant compact-Horn combined-master
solver remained live with no SAT or UNSAT verdict at the final read-only
poll.  These are explicitly unfrozen external observations.  No residence
search was launched, modified, or stopped by this task.

## 11. Frozen package

The package is
`scratch/ad_k17_all_opening_benders_v5_20260802/`.  It contains the exact
sources, final H100 binaries, authenticated inputs, final `freeze_*` outputs,
zero-length compiler warning logs, and a replay runbook.  The manifest has
143 entries; its SHA-256 is:

```text
e118cf2d32b0a8422d2328e6b08ef7e3fb66bc7478cde4174f8b96e0022b5116  SHA256SUMS
```

The manifest passed on the H100 before transfer and passed again against the
local package after transfer.

## 12. Nonclaims

This audit does not claim:

- a full combined-master replay for the two sparse `k=17` calibrations;
- a resident or source-ready `k=17` factor;
- an authoritative common-cap UNSAT proof branch;
- that the prospective strong DM row is already linked into a persistent
  host master;
- cyclic closure for the authenticated `k=15` linear path;
- a `k=17` word or `nu(17)=B(17)`.
