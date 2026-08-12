# K17 compact Horn v3 independent stream replay

Date: 2026-08-02  
Status: independent fail-closed replay **GO**.  No solver was launched.  This
audit validates the exact serialized CNF and variable map; it does not assert
quotient connectivity, nonzero voltage, deeper upper coverage, a source
factor, or a compiler.

## 1. Frozen inputs and outputs

```text
round-one base CNF
  SHA c6638107ba4d1241403f914b5893614d9660a48cde7e43bef495b5fe28ebed52
catalogue map
  SHA 7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
marker58 witness
  SHA 88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
canonical union562 blocker bank
  SHA fc92330a6ab40e2edffacbfaba85d9c8bf21b1b1347c3c80f2eabb0af0a79952

compact Horn v3 CNF
  SHA cff3acda560916bdb846fb2f7026c0e4c514de54da4672f48d18f24ce02c103c
compact Horn v3 map
  SHA b623e15e60006dcf1ad4cbd817f7d595b691e9d622359a7886620e5f632ead38
```

The output header is exactly

```text
p cnf 314651 1833776
```

## 2. Independent reconstruction

The V2 auditor does not call the builder.  Starting from the authenticated
catalogue and marker witness, it independently reconstructs:

1. the 232 fixed marker edges and all 35,713 option rows;
2. the sorted 1,430 rank-nine owner representatives;
3. the exact forward/reverse dart variables, voltages, deletion labels and
   target-frame insertion labels;
4. the three `B,R1,R2` variables for every one of the 12,870 owner-coordinate
   states;
5. every line of the 110,484-row output map;
6. every CNF clause in serialized order.

It compares the first 439,463 output clauses literally against the base CNF,
then independently emits and compares the following exact sections:

| section | clauses |
|---|---:|
| edge/dart channel | 143,292 |
| owner outgoing/incoming ALO | 2,860 |
| endpoint `B` witnesses | 71,874 |
| `B -> R1`, `R1 -> R2` Horn transport | 1,149,984 |
| `B/R1`, `B/R2` conflicts | 25,740 |
| exact core total | 1,393,750 |
| lexicographically sorted redundant blockers | 562 |
| reversal-WLOG unit | 1 |

The final unit is exactly variable `204168`.  The replay consumes the complete
CNF with no missing or trailing token.

The independent source is

```text
scratch/audit_k17_compact_horn_v3_stream_replay_20260802.cpp
SHA 381e321d1979dd68f5f1d277ca486d6bee144684feacd931cdb0d1075ba58266
```

The structured audit is

```text
scratch/k17_compact_horn_v3_stream_replay_20260802.audit.json
SHA fff169578e0a1cf8c0a05f07013f85272914acab8143d012a089e87bb89766bb
```

Retained H100 root:

```text
/home/amodo/or15/work/qa_k17_compact_horn_v3_stream_replay_20260802_quotientaudit
```

## 3. Semantic controls

The stream auditor includes a positive synthetic run test.  The independent
Horn closure rejects positive run lengths two and three and accepts lengths
four through eight, exactly matching the intended residence-floor-four
semantics.  Length one remains excluded by the lower-facet identity, outside
the Horn reach rows themselves.

As a literal negative control, the independent orientation/reach audit was
rebuilt under the V2 root and replayed on the authenticated floor3502 factor.
It obtains exactly

```text
length-two run orbits   114
length-three run orbits  92
```

matching the independent physical counts `1938/17` and `1564/17`.  Its output
SHA is

```text
dc05c8b0ce7e02dac30e3bbe2c5a77d8fc62869a4a880add561947f81c429d52
```

No builder correction surfaced.  The artifact is eligible for a solver run
with respect to exact construction/replay only; decoding must still fail
closed on connectivity, voltage, literal residence, deeper upper ranks, and
all downstream source/compiler gates.
