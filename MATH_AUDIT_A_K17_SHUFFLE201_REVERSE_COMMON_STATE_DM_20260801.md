# Exact common-state DM obstruction for the frozen `shuffle201_reverse` table

**Date:** 2026-08-01  
**Status:** independently replayed exact finite theorem. This is a no-go for
one frozen rooted flag table, not for the shuffle201 basin or K17 generally.

## 1. Input and question

The fixed table is

```text
scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.candidate.tsv
SHA256 e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd
```

For every rank-8 root packet and every one of its nine rank-9 owner
attachments, rebuild the complete phase-labelled changing-owner state graph.
Call an attachment **common-live** when it has at least one literal incoming
and at least one literal outgoing transition. Form the bipartite graph
`G=(R,O;E)`, where a root `r` is adjacent to owner orbit `o` precisely when
their unique incidence state is common-live. A perfect matching in `G` is
necessary for one common choice of a root state and owner orbit at every row.
It is still weaker than an induced transition cycle cover.

## 2. Exact reconstruction theorem

The independent O3 C++ replay verifies the full static lower flag tower and
reconstructs

```text
attachment states                         12,870
phase-labelled packet turns                1,855
labelled state arcs                        14,840
zero-out states                             2,803
zero-in states                             11,140
common-live root-owner states               1,290
roots with no common-live incidence           661
owners with no common-live incidence          526
```

The common-live graph has exact maximum matching size 718. Indeed, the
emitted matching contains 718 literal common-live incidences. Conversely,
the alternating shore of the unmatched roots gives an explicit set `S` with

```text
|S| = 770,  |N(S)| = 58,  |S|-|N(S)| = 712.                    (2.1)
```

Thus Hall gives `matching(G) <= 1430-712 = 718`, proving equality. The
literal ID hashes agree byte-for-byte with the independent Python
reconstruction:

```text
matching root-owner pair hash
2ff089bbd6ee72a77bcea15dab162118077563128f457375f98ecb08fe14d496

Hall tail-root ID hash
980087d9fa6dbd3fc87a8c5ba90179a31aa727f71db5aaffdbbde6395dcd4773

Hall head-owner ID hash
87a3c7dfbcb139dfe64c5f6994f063599247ae18c3f9e1a74820288ac36e25dd
```

Consequently the frozen table admits no common root/owner state transversal,
and therefore no induced transition cycle cover or Hamilton chronology,
before any upper condition is imposed.

## 3. Exact DM and component profile

For the emitted maximum matching, orient every nonmatching edge from roots to
owners and every matching edge from owners to roots. The canonical
Dulmage--Mendelsohn vertex partition is

```text
                 roots    owners
PLUS               770        58
MINUS              226       938
CORE               434       434
```

The PLUS imbalance is exactly the Hall deficiency 712, and the MINUS
imbalance is its dual. Contracting the 718 matching edges leaves 2,142 DM
atoms. The resulting alternating digraph is acyclic: its 2,142 strongly
connected components are exactly

```text
712 PLUS unmatched-root atoms,
 58 PLUS matched-pair atoms,
226 MINUS matched-pair atoms,
712 MINUS unmatched-owner atoms,
434 CORE matched-pair atoms.
```

Equivalently, the SCC left-minus-right histogram is

```text
-1:712, 0:718, +1:712.
```

The undirected common-live graph has 1,572 weak components. Of these, 1,187
are isolated vertices. Its exact component-size histogram is

```text
1:1187, 2:191, 3:72, 4:40, 5:18, 6:17, 7:6, 8:7, 9:4,
10:5, 11:2, 12:5, 13:2, 14:1, 15:4, 16:2, 18:1, 19:1,
21:1, 24:1, 28:1, 33:1, 34:1, 46:1, 102:1.
```

The full weak-component file also records, component by component, root and
owner counts, edge and matching counts, DM-region counts, and the nine root
type counts. There is no quotient transition-component profile to report:
the prerequisite common state transversal already fails by (2.1).

## 4. Frozen proof artifacts

```text
O3 C++ independent auditor
scratch/audit_threadA_k17_shuffle201_common_state_dm_20260801.cpp
SHA256 17ad6d1c1c6b2e864fa3dc41b2c900600dc76d29e3926c32017f3fe067f11efa

summary audit
scratch/shuffle201_reverse.common_state.audit.json
SHA256 f33a5d43775802866fc406ceaf31bad68c67d2515b30ac377b94660c25536bc9

literal maximum matching
scratch/shuffle201_reverse.common_state.maximum_matching.tsv
SHA256 27094725bce2cbd8df70b25bf311cc2eea18c2ade40dfdc71c473087e8256031

literal Hall shore
scratch/shuffle201_reverse.common_state.hall_cut.tsv
SHA256 5d8f2a851e7254478cd1ded1e59fbe22d93a9d404aa9da39a13ee318b5b3085b

weak-component profiles
scratch/shuffle201_reverse.common_state.weak_components.tsv
SHA256 e8b7584d7cb5537c14f2aa08be2c7d7875d1de2038762ba1c887aaffb205b434

contracted DM components
scratch/shuffle201_reverse.common_state.dm_scc.tsv
SHA256 bc27aa389d4837e403c859de97e3bdd8a4992dcad27b2ba6b4af3f6dc634239e

independent Python replay
scratch/threadA_k17_shuffle201_common_state_python_replay_20260801.audit.json
SHA256 3ae325d494eb8ecaa2c068a8a0fd1af280882be3604f6078af283cd57a979dac
```

The H100 run used only CPU, `-O3`, a 4 GiB address-space cap, a 300-second CPU
cap, and the unique directory

```text
/home/amodo/or15/work/threadA_k17_shuffle201_common_state_20260801
```

## 5. Scope boundary

This obstruction is stronger than a packet-support deficiency: it already
requires a single attachment to serve root identity, owner identity, and both
directions of the literal age recurrence. It is nevertheless table-local.
Changing the selected support-two circuits, allowing higher-support GKS
containment switches, or changing the rooted flag table changes `G` and can
escape the cut. No upper-shadow, voltage, opening, or compiler row is used.

