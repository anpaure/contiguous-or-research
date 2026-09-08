# K17 all-P2 receiver C8 no-go and the first unexcluded C10 gate

**Date:** 2026-08-02  
**Lane:** A, receiver-bank chain-slot packets  
**Status:** exact finite theorem on the frozen original-P2, length-two,
two-phase common-state face.  It proves a five-changed-role lower bound only
for packets confined to original P2 rows.  Mixed-F packets, changed long
roles, chain-length changes, richer state grammars, and indirect repairs in a
regenerated ambient table are outside the theorem.

## 1. Verdict

Let `K` be the twelve rank-seven P2 roles left uncovered by every exact
receiver-changing C4:

```text
23021 23042 23046 23070 23336 23340
23471 23850 23955 23987 24051 24055.
```

Restrict all changed rows to the frozen bank of 3,899 original P2 rows.
Every changed row remains length two, so the complete bank of long endpoint
modes used by the relaxed-nine five-cell oracle is pointwise unchanged.

The exact conclusions are:

1. support two is structurally impossible for every role in `K`;
2. the only support-three all-P2 receiver cycles are the four cycles already
   audited, and all four fail the exact two-phase socket row;
3. the complete support-four all-P2 catalogue has 58 directed C8s, and all
   58 fail the same socket row.

Consequently any original-P2-only, target/root/row-length-preserving packet
which moves the rank-seven target of a role in `K` and makes every changed
role socketable in both transported phases has changed support at least five.
The first unexcluded single-cycle matching primitive is therefore a directed
C10 on five P2 roles.

This is a lower bound, not a positive C10 or a full physical collar.  A
two-ended internal linear collar still needs exterior guards unless its
boundary is clipped or encoded by a different grammar.

## 2. Cycle decomposition

Write an original P2 row as `(A_v,R_v)`, with its lower target `A_v`, its
rank-eight root `R_v`, and its owner fixed at the physical row.  Any exact
reassignment of a finite set `X` of P2 lower targets among the same roots is
a permutation `pi` of `X` satisfying

\[
                         A_{\pi(v)}\subsetneq R_v
                         \qquad(v\in X).             \tag{2.1}
\]

The symmetric difference from the diagonal matching decomposes uniquely
into directed permutation cycles.  A cycle on `t` physical rows is the
alternating matching circuit of length `2t`.

For an anchor in `K`, a two-cycle is absent by the complete C4 audit.  Thus a
nonidentity packet on at most four changed rows has only the following
possibilities for the component containing the anchor:

* one directed three-cycle, with no room for another nontrivial component;
* one directed four-cycle; or
* a two-cycle, which does not exist.

A three-cycle plus a disjoint nontrivial cycle has support at least `3+2=5`,
and two disjoint two-cycles again require an anchor two-cycle.  Therefore the
complete support-at-most-four all-P2 face is exhausted by the previously
audited C6s and the C8s below.

The long endpoint-mode bank is unchanged because every moved row remains
length two.  Hence adding a disjoint P2 circuit cannot regenerate a zero
five-cell DNF for a rebuilt role: the role key and every possible long
predecessor/successor mode used by its oracle remain the same.  This is what
makes the cycle decomposition a physical necessary condition rather than
only a target/root projection.

## 3. Exact support-three calibration

The four all-P2 C6s are

```text
(23340,23365,10123)
(23340,23365,10837)
(23955,23980,10375)
(23955,23980,16810).
```

Their exact phase-0/phase-1 hyperarc counts by rebuilt row are

```text
(0/0,       0/0, 3400/3400)
(0/0,       0/0,  621/1179)
(2872/2872, 0/0, 1200/993)
(3697/3697, 0/0, 3777/4242).
```

Thus every cycle contains a rebuilt role whose complete DNF is empty in both
phases.  The selected warm47 supplier matching survives the first three;
the fourth destroys exactly the selected edge

```text
16810 -> 3407 : 50 -> 0.
```

All four avoid every occurrence used by the 1,748 selected private H tickets
and by their protected outer matching.  Those supplier and private
certificates live on separately authenticated parent projections; they are
not asserted to be one unified selected-state parent.  The empty DNF is
already decisive before that join.

## 4. Complete support-four catalogue

A directed four-cycle on distinct P2 rows `(i,j,k,l)` is

\[
\begin{aligned}
 (A_i,R_i)&\mapsto(A_l,R_i),\\
 (A_j,R_j)&\mapsto(A_i,R_j),\\
 (A_k,R_k)&\mapsto(A_j,R_k),\\
 (A_l,R_l)&\mapsto(A_k,R_l),
\end{aligned}                                        \tag{4.1}
\]

with the four strict containments forced by (2.1).  Exhaustive indexed
enumeration over all 3,899 original P2 rows gives the following exact counts:

| anchor | C8s |
|---:|---:|
| 23021 | 8 |
| 23042 | 15 |
| 23046 | 0 |
| 23070 | 4 |
| 23336 | 0 |
| 23340 | 16 |
| 23471 | 0 |
| 23850 | 6 |
| 23955 | 9 |
| 23987 | 0 |
| 24051 | 0 |
| 24055 | 0 |
| **total** | **58** |

For every C8, the audit materializes all four crossed role keys and reruns
the complete endpoint/state/socket oracle in phase zero and phase one.  A
cycle is accepted only if every rebuilt role has at least one exact five-cell
hyperarc in both phases.  The result is

\[
                  58\text{ structural C8s},\qquad
                   0\text{ accepted C8s}.             \tag{4.2}
\]

The frozen ledger records all eight per-cycle quantities (four roles times
two phases), rather than only an aggregate Boolean verdict.

## 5. Exact scope of the C10 gate

Combining Sections 2--4 proves

\[
 \boxed{\text{all-P2 common-state receiver support}\ge5}       \tag{5.1}
\]

for moving the rank-seven target of any anchor in `K` on the frozen table.
The first unexcluded connected matching circuit is a C10.  This does not say
that a C10 exists with all DNFs nonempty, that its occurrence witnesses are
simultaneously resource-disjoint, or that it preserves the selected supplier
matching.

Nor does (5.1) apply to a support-four circuit recruiting F rows or long H
rows.  Such a packet can change the outer receiver matching or the long mode
bank and must be replayed in the joint chain/slot/owner master.  Likewise,
the fixed-root SCC theorem permits indirect repair of an unchanged role when
other long modes are regenerated; no such global impossibility is claimed.

For a standard internal two-ended all-P2 collar, five changed roles plus two
retained exterior guards give a seven-role lower bound.  A global boundary,
a cyclic serialization, or a nonstandard grammar may alter that guard count;
only the changed-support bound (5.1) is unconditional within the declared
all-P2 face.

## 6. Frozen evidence

```text
scratch/a_five_role_joint_packet_20260802/
  enumerate_allp2_receiver_c8.cpp
    c61f61ef73bc790f623e1fd02290951849cbd6d1e23da815a1298a7cf8c1d865
  allp2_receiver_c8.json
    5592760b44cf1a627c197a9f87806c1042194756db1173094d58e5c1b22aebfe
  allp2_receiver_c8.tsv
    35e39f0fbfa5e23b7c18ba8839b4890e330126182c4a9eec7c7347655c8afecb
  price_allp2_receiver_c8_sockets.cpp
    f142018eaedb5f565733878fe3f5e2edc7e38c36472048d0a74b02ad50243ba8
  allp2_c8_sockets.tsv
    7525b4e6fb356807394dff750fd02e6aec76d0aefae0412ee6b911cf6ced24b7
  verify_allp2_receiver_c8_gate_20260802.py
    f0fffe8e096f336db921d422ae6a7bbefa8c34e6a7e3661ddbcb5fc680f1b5fb
  allp2_c8_independent.audit.json
    e00ca4a0a1805972822d1ccb63a4f3c73911c6a73eab25d733aac674db4bf0df
```

The structural enumeration and socket pricing were compiled with `-O3` and
run under the unique persistent H100 root

```text
/home/amodo/or15/work/a_five_role_joint_packet_20260802
```

The exact four-C6 ledger and its independent verifier are frozen at

```text
scratch/a_k17_receiver_bank_c4_20260802/
  all_p2_receiver_c6_exact_no_go.audit.tsv
    2cf60a02278e25e9b06a9615cac5ef56303746afd68594acb60eed956989c10b
  verify_a_k17_receiver_bank_c4_c6_calibration_20260802.py
    1193c9b332d44f9e3243e536e33075ac1359a4db7b8c33f918a4b761fbd130ad
```

Scope exclusions: mixed-F support four, any changed long role, chain-length
changes, richer source/state grammars, simultaneous occurrence packing,
chronology, residence, upper shadows, source/common-cap/compiler closure, and
a word.
