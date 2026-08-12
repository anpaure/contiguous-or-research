# K17 `4f5fb7` packet-matching independent replay

Date: 2026-08-01  
Lane: A / finite support-three escape  
Status: **PASS, exact literal packet replay**

## 1. Statement

The exact rooted flag tables

```text
baseline  2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb
final     4f5fb7f2b0a5a29090925cddcdbfe124cd3930f0c36b88948f28d9cf41794acb
```

were decoded independently of the support-three selector and its cached
score.  The auditor verifies the complete static type/lower-resource ledger,
reconstructs every literal loop-free physical root transition, and runs a
fresh Hopcroft--Karp matching plus canonical alternating Hall audit.

The packet result is

| table | matching | Hall shore | deficiency | zero out/in | loop-free geometries |
|---|---:|---:|---:|---:|---:|
| `2e9194` | 1172 | `565 -> 307` | 258 | `42 / 215` | 2245 |
| `4f5fb7` | 1173 | `562 -> 305` | 257 | `43 / 214` | 2244 |

Thus the support-three commutator gains one exact packet-matching unit even
though the number of raw loop-free geometries decreases by one.  The final
packet Hall-tail/head identifier hashes are

```text
tail  3d9ff8ff10faf037859790802ae28e42fbd66d26ac992707d49b4deca6cf1f2f
head  2d5c9d9daf42adefe381f384f168827bcb146b1cb228e5d051aa34e6112fa474.
```

The final packet edge-set and selected maximum-matching hashes are

```text
edges     1d3b09366bea89309debdb8f5050b42e58852b6d4f4bc10474c4355eeb800d67
matching  a93f62adbed4c2cbd7c2a5ca300604d9ae383bac95c2f802fc41be13c4ea6b55.
```

The same clean replay independently corroborates common matching
`1141 -> 1142`, but that result is frozen by the separate common-DM verifier.

## 2. Frozen artifacts

The original compact replay wrapper requested for lineage is preserved
byte-for-byte at

```text
scratch/threadA_k17_2e919_dm_support3_commutator_20260801/
  audit_threadA_k17_4f5_packet_and_common_replay_20260801.v1.cpp
SHA256 048d18732b463243d5bb71f60a00e053924334df40cd0845ed297847318d0d11.
```

The enhanced wrapper authenticates both input hashes and emits the packet
edge, matching, and Hall-shore hashes:

```text
scratch/threadA_k17_2e919_dm_support3_commutator_20260801/
  audit_threadA_k17_4f5_packet_and_common_replay_20260801.enhanced.cpp
SHA256 ce5800b5eab4883d7b01f13e748ac0e4756563a16c96894fff36c506320d7a31

  verify_k17_disjoint_support2_selector_20260801.cpp
SHA256 0d0f68bc3524579b940f8797a7dacc2dd531d7417f132c92ffbf09ee906e7d23

  packet_common.independent.audit.json
SHA256 de061acb3c6d930aeeac3aa067a286cf86dd526030c0d585b29a1da24ecb2063.
```

The enhanced O3 executable was compiled and run on H100 CPU under a 2 GiB
address-space cap; its SHA256 was

```text
c80f2a9f0a0fc479f676b5aadd23266eb756dedddb8bb500c5fe4e11e5cf84cd.
```

## 3. Scope boundary

The exact conclusion is a packet/root-transition matching gain and its Hall
certificate.  It does not select one common attachment state per root and
owner, and it makes no chronology, component, voltage, upper-shadow,
residence, opening, or compiler claim.
