# K17 `45a0fd -> 89c9e9` final serial packet/common replay

Date: 2026-08-01  
Lane: A / independent serial-winner audit  
Status: **PASS, exact literal replay**

The two authenticated rooted flag tables are

```text
baseline  45a0fd760309fdb85382c410e61b543ea7a0cb5c49199b43bd43f6689159888d
final     89c9e92e23e1b38f067d32f6e46f8c44d2e51ee27c89b3eeda686cc50988b78a.
```

An independent O3 replay on H100 CPU verifies the complete static
type/lower-resource ledger, reconstructs all literal loop-free physical
transitions and attachment-state arcs, and reruns both packet and common
Hopcroft--Karp/Hall audits.  It consumes neither the selector catalogue nor
its score delta.

| graph | baseline | final |
|---|---:|---:|
| packet matching | 1173 | 1173 |
| packet Hall shore | `561 -> 304` | `565 -> 308` |
| packet deficiency | 257 | 257 |
| packet zero out/in | `44 / 212` | `43 / 212` |
| common matching | 1146 | 1147 |
| common Hall shore | `301 -> 17` | `300 -> 17` |
| common deficiency | 284 | 283 |

Thus the final serial circuit gains one exact common-matching unit while
leaving packet matching and packet deficiency unchanged.  It also changes
the canonical packet Hall shore; the unchanged cardinal deficiency must not
be read as an unchanged packet obstruction.

The independent replay produced byte-for-byte the already persisted audit:

```text
scratch/threadA_k17_45a0_dm_support3_commutator_20260801/
  packet_common.independent.audit.json
SHA256 6760c73f537e9f5e714114ba0ed8d7e24560d055c2ad8e389d09d183bb04bb4a.
```

The frozen replay sources in the same directory are

```text
audit_threadA_k17_89c9_packet_and_common_replay_20260801.cpp
  1bce915b97e1fb957bf9ce1779253d9d7f86676bb95ac555b0cdce096cc6690a
verify_k17_disjoint_support2_selector_20260801.cpp
  0d0f68bc3524579b940f8797a7dacc2dd531d7417f132c92ffbf09ee906e7d23.
```

The independently compiled O3 executable had SHA256

```text
58477fd07e46dcb6535d433e7f472db3beb6c96a285527bd42933b9642111885.
```

This audit establishes only the rooted-static ledger, packet transition
matching, and common both-live matching/Hall shores.  It does not construct
a full common state transversal and makes no chronology, topology, upper
shadow, residence, voltage, opening, or compiler claim.
