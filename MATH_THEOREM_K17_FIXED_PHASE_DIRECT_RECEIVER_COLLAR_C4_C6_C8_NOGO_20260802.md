# K17 fixed-phase direct receiver-collar `C4/C6/C8` obstruction

**Date:** 2026-08-02  
**Status:** exact finite no-go on the frozen transported phase tables and
potential-H mode atlas.  This is not a no-go for regenerated sources,
general compound circuits, root recoupling, or longer suffix circuits.

## 1. Frozen socket oracle

The calculation fixes the round-47 transported owner phases and the
phase-independent origin table:

```text
origin res1972
  db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
s7 phase 0
  ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
s7 phase 1
  736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
potential-H edge map
  d39b58f679f4d9219b72209b06ea71387db64cdecac649a4f390c9f7ed13da25
```

For every changed short row, the oracle ranges over all `2,129,483`
carrier-legal dynamic H modes, the `17` fixed-soft modes, all nine relaxed
short families, compatible predecessor/successor mode pairs, and the exact
nonempty five-cell coordinate DP.  A collar can pass the gate below only if
every changed role has a socket separately in both fixed phases.  This is a
necessary rowwise gate; it does not assume that independently chosen row
witnesses form one common global state.

## 2. Complete direct `C4` class: `0/304`

The complete strict two-row receiver exchange is

\[
 (S,R)+(L,Q)\longmapsto(L,R)+(S,Q),
 \qquad |S|=7,\quad |L|\leq6.
\]

On the 162 rank-seven roles stuck in the maximally relaxed fixed-root SCC
graph, the exact structural catalogue contains `304` exchanges and covers
`150` roles; twelve roles are structurally unsupported.  Exactly

```text
0 / 304
```

have both crossed roles socketable in both transported phases.  Hence no
direct two-row receiver collar in this exact target/root/mode class passes
even the separable rowwise socket necessity.

```text
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_receiver_bank_c4_structural_20260802.cpp
    654bd6658fb49d357961cc68d7c51ee0c1a5846849cb46b98ba37d1f1e755f20
  candidates.tsv
    c0c471e47f7a038c8ec87f65fc26752872ea93c5bc16b5886ab88ffca439f7b1
  audit.json
    2c5863c2d05c669596aa5cff587be7eb2c13f538d041c15da0cf255a65c980d4
  audit_a_k17_receiver_bank_c4_common_phase_socket_20260802.cpp
    d544c74f5f3bd89c744920f47c89590c9a46fd95ffc46b5029b96b4d95e92ca5
  socket_catalogue.audit.json
    1f3aee9947fa6cb51fc67da2338dd7ddd5f0b92483cc17eec583f046799352dd
  SOCKET_MANIFEST.sha256
    9b0943dc0ab20f232eed7c5afd72b0f5366f96e213b7f3bd5b5e683c0a1c8fd1
```

The manifest binds exactly 304 candidate-keyed result/error pairs.  Every
candidate fails with the same explicit verdict that the two crossed roles
are not both common-phase socketable.

## 3. Complete minimal receiver `C6` class: `0/208`

The twelve C4-uncovered anchors have exactly `208` directed three-row
receiver cycles on the `7,395` short rows, each containing at least one
nonreceiver-root role.  This is the exact minimal support-three class for
these anchors.

Of the 208 cycles, 204 contain an original-F row.  They project to 72
distinct rank-seven-on-F changed roles, and exact pricing gives

```text
common-phase rank-seven-on-F roles = 0 / 72.
```

The remaining four cycles are entirely original-P2:

```text
(23340,23365,10123)
(23340,23365,10837)
(23955,23980,10375)
(23955,23980,16810).
```

Every one has at least one changed row with zero hyperarcs in both phases.
Therefore none of the 208 exact minimal receiver C6s passes the rowwise
socket gate.

```text
scratch/a_k17_joint_chain_slot_receiver_c4_20260802/
  receiver_c6_cycles.tsv
    32bfe2225282791cd050a2ed424b50576c61c3f927cc27cf327034d7aa07f1ce
  receiver_c6.audit.json
    51f8c537c88da4cd55bd7cb88ac207019f77c89c168ca8a39da460e3dc7f4ade
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_rank7_on_f_common_phase_socket_20260802.cpp
    cb33262df430c3f622aeb5356ad862745546e62741e6423936d5f0317c3e1f66
  rank7_on_f_pairs.txt
    3da3fe6128547d470b3100146254b1f20c3d664298f763dd914b9e3822563bcc
  rank7_on_f_socket.audit.json
    fe50282c80ad372f234bf09660792073f5ae80f50161e00291c60696405e734a
  RANK7_ON_F_MANIFEST.sha256
    17c61b4d92c33bd1eb31a2f4635db0006dca2990a579132bdfe49f1f8daf7488
scratch/a_five_role_joint_packet_20260802/
  aligned_c6_sockets.tsv
    975d99d84d925331ceec1378b0d1662f3e93ec54de29a9de71e554b203e86978
```

### Supplier and private-bank classification of the four all-P2 C6s

The warm47 `16,898`-edge supplier matching survives the first three
all-P2 cycles.  The fourth destroys exactly supplier edge
`16810->3407`, whose legal mask changes from `50` to `0`.  All four cycles
avoid every footprint in the protected 1,748-ticket bank and every endpoint
of the complete `16,898 H + 1,748 F` outer matching.

```text
scratch/a_five_role_joint_packet_20260802/
  four_p2_c6_supplier_private.tsv
    1763d40a491f82829cb8644f13fe06ce1b74487d5e2b29bb2f9f448d057fe081
  MANIFEST.four_p2_c6_supplier.sha256
    eb4e0eeba6e8140359100cca0e82e1b94fae85758824fd8ba9313e65c330ea0a
```

The supplier replay is on warm47, whereas the ticket/outer avoidance test
uses the separately authenticated protected table.  This is an exact
classification, not a same-table simultaneous certificate.

## 4. Follow-on all-P2 receiver `C8`: `0/58`

The completed simple directed all-P2 C8 census has `58` cycles.  Their
anchor counts are

```text
23021:8, 23042:15, 23070:4, 23340:16, 23850:6, 23955:9,
and 0 at the other six C4-uncovered anchors.
```

No cycle passes the common-phase rowwise socket gate.  Every cycle has at
least one row with zero sockets in both phases; the number of such rows per
cycle has histogram

```text
1 -> 11,  2 -> 34,  3 -> 12,  4 -> 1.
```

```text
scratch/a_five_role_joint_packet_20260802/
  enumerate_allp2_receiver_c8.cpp
    c61f61ef73bc790f623e1fd02290951849cbd6d1e23da815a1298a7cf8c1d865
  allp2_receiver_c8.tsv
    35e39f0fbfa5e23b7c18ba8839b4890e330126182c4a9eec7c7347655c8afecb
  allp2_receiver_c8.json
    5592760b44cf1a627c197a9f87806c1042194756db1173094d58e5c1b22aebfe
  MANIFEST.allp2_c8.sha256
    6061efce1fed77ce0bb815468eb64c65a12a6a236e9a369529644115886f543a
  price_allp2_receiver_c8_sockets.cpp
    f142018eaedb5f565733878fe3f5e2edc7e38c36472048d0a74b02ad50243ba8
  allp2_c8_sockets.tsv
    7525b4e6fb356807394dff750fd02e6aec76d0aefae0412ee6b911cf6ced24b7
  MANIFEST.allp2_c8_socket.sha256
    2f6248bfa0e996f918f91f2a507bd3b61f30071d787ec0f3de820e61afbf0567
```

Both remote manifests replay with every entry `OK`.  The process formerly
seen as PID `1920607` is absent.  There is no surviving launcher, PID
ledger, resource log, or shell exit record, but the producer emitted its
PASS JSON, complete 58-row catalogue, empty error file, and a
checksum-consistent manifest.  Thus the enumeration itself completed; its
wrapper exit status is not independently frozen.  Relaunching would only
duplicate a byte-verified completed producer and was not done.

## 5. Exact scope

The theorem kills

1. every direct two-row C4 receiver collar;
2. every exact minimal three-row receiver C6 collar; and
3. the enumerated simple directed all-P2 C8 family,

on the fixed transported phases and frozen potential-H source atlas.

It does **not** exclude other compound C8 topologies, F/H-containing C8s,
longer suffix circuits, simultaneous multicycle packing, root-bank
recoupling, changed roots or owners, regenerated source modes/atlases, or
downstream state sharing, guard, chronology, topology, residence, upper,
source, compiler, and word constructions.  In particular, a later table
edit may create a socket mode absent from this frozen atlas.
