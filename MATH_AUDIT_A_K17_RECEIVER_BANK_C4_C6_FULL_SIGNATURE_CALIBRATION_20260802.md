# K17 receiver-bank `C4/C6` calibration and the exact support-at-most-three common-state no-go

**Date:** 2026-08-02  
**Lane:** A, joint chain-slot/private-socket escape  
**Status:** exact structural and exact relaxed-nine common-state audit on the
frozen round-47 target table.  This note distinguishes the positive
fixed-receiver `P2--H--H C6` from a genuine receiver-set change and closes the
complete support-two/support-three directed length-two circuit face for the
12 residual SCC-stuck roles.  It is not a global K17 impossibility theorem.

## 1. Verdict

There are three different circuit projections.

1. The authenticated `P2` prefix `C4` on rows `565,649` is a support-two
   target/root exchange and gives an exact one-unit reduction of the old P2
   common-phase zero count.  Both rows remain rank-six-bottom P2 roles.  It
   does not change the rank-seven receiver bank.
2. The authenticated `P2--H--H C6` on rows
   `16269,16267,16271` is the support-minimal rank-seven reassignment inside
   the **unchanged** receiver bank.  It preserves the target partition,
   roots, owners, row lengths, the frozen supplier certificate and protected
   private bank in their audited scopes.  It is not an escape for the 162
   singleton SCC roles, because its three receiver roots were receivers both
   before and after the move.
3. A genuine receiver-bank change first has the two-row form

   \[
      (S,R)+(L,Q)\longmapsto(L,R)+(S,Q),              \tag{1.1}
   \]

   where `|S|=7`, `|L|<7`, and
   (S\subsetneq Q, L\subsetneq R).  Thus the rank-seven receiver changes
   from `R` to `Q`.

On the exact frozen table, (1.1) has 304 structural occurrences covering 150
of the 162 fixed-root SCC-stuck roles.  The other 12 have no such support-two
move.  Nevertheless **none of the 304 occurrences is a complete
common-phase socket move**: the new rank-seven-on-nonreceiver role has zero
exact relaxed-nine five-cell hyperarcs in each phase for every occurrence.

For the residual 12 roles, the complete support-three directed-cycle
catalogue has 208 entries.  It splits as

```text
all-original-P2       4
one original F       60
two original F      144
```

The 204 cycles using an original F row contain one of 72 distinct
rank-seven-on-F roles.  All 72 have zero exact hyperarcs in phase 0 and zero
in phase 1.  Each of the four all-P2 cycles also has at least one new role
with zero hyperarcs in both phases.  Therefore:

> No directed target/root matching circuit of support at most three in the
> frozen 7,395-row length-two face both changes the receiver bank for one of
> the 162 SCC-stuck roles and makes every changed role common-phase
> socketable under the complete relaxed-nine five-cell oracle.

This is the sharp scoped obstruction requested here.  The next matching
primitive is a directed support-four `C8`; alternatively one must change
chain length, the endpoint/state grammar, or the physical owner/guard host.
A standard two-ended reciprocal private collar still needs its own linear
guard support and is not supplied by target/root circuit existence.

## 2. The two positive calibrations

### 2.1 Prefix `C4`

The positive square is

```text
old  (4423,4943) + (4427,5455)
new  (4427,4943) + (4423,5455).
```

All four containments are strict.  The target multiset, roots, owners and row
lengths are unchanged.  Exact two-phase pricing gives, for the two crossed
roles, respectively,

```text
phase 0: 1829, 7377 hyperarcs
phase 1: 1829, 1682 hyperarcs.
```

The old row 565 was zero in both phases, while the old row 649 was positive
in both; hence the exact union-zero count drops by one.  The raw-warm47
supplier matching stays `16898/16898`, all 1,748 protected H tickets remain
untouched, and the complete protected outer matching stays
`16898 H + 1748 F`.

This proves that support two is enough for a lower-rank prefix role move.  It
does not move a rank-seven target between receiver and nonreceiver roots.

### 2.2 Fixed-bank `P2--H--H C6`

For rank-seven targets `S0,S1,S2`, rank-eight roots `R0,R1,R2`, and fixed H
bottoms `B1,B2`, the literal identity is

\[
\begin{aligned}
 &(S_0,R_0)+(B_1,S_1,R_1)+(B_2,S_2,R_2)\\
 &\qquad\longmapsto
 (S_1,R_0)+(B_1,S_2,R_1)+(B_2,S_0,R_2),              \tag{2.1}
\end{aligned}
\]

with

\[
 S_1\subsetneq R_0,quad S_2\subsetneq R_1,quad
 S_0\subsetneq R_2,quad B_1\subsetneq S_2,quad
 B_2\subsetneq S_0.                                  \tag{2.2}
\]

The Boolean rank-seven/rank-eight incidence graph has no `C4`: two distinct
rank-seven sets have at most one common rank-eight superset.  Hence three
physical rows, equivalently six matching edges in the symmetric difference,
are necessary and (2.1) is support-minimal for a nontrivial fixed-bank
rank-seven reassignment.

The authenticated instance is

```text
rows 16269,16267,16271
old  81416-81417 ; 73216-81409-81413 ; 81408-81412-81420
new  81409-81417 ; 73216-81412-81413 ; 81408-81416-81420.
```

Its new P2 role has 3,899 phase-0 and 3,584 phase-1 exact hyperarcs.  The move
preserves the 65,535-target deck, every root, owner and row length, all 1,748
private tickets, the complete outer matching and the raw-warm47
`16898/16898` supplier certificate.  It does **not** certify complete H
state/history/guard clones, one common selected state, or a reciprocal unary
ticket.  Most importantly, the receiver set `{R0,R1,R2}` is unchanged.

## 3. Genuine receiver-bank `C4`

Let the current rows be

\[
                    (S,R),\qquad(L,Q),               \tag{3.1}
\]

with `|S|=7`, `|R|=|Q|=8`, `|L|<7`.  Suppose

\[
                      S\subsetneq Q,qquad L\subsetneq R.     \tag{3.2}
\]

Then (1.1) is an exact two-row chain-slot circuit.  It preserves the complete
target partition, both physical roots and owners, and the row-length
histogram.  Before the move `R` receives a rank-seven target and `Q` does
not; after the move `Q` receives `S` and `R` does not.  A one-row move cannot
preserve both target and root use, so support two is set-level minimal.

The independent O3 audit uses the 162 singleton-SCC roles from the strongest
fixed-root relaxation and every current length-two row whose bottom has rank
below seven.  It proves

```text
candidate edges       304
covered stuck roles   150 / 162
maximum degree          5
zero roles             12
```

with zero chain IDs

```text
23021 23042 23046 23070 23336 23340
23471 23850 23955 23987 24051 24055.
```

The exact two-phase socket audit then reconstructs the global potential-mode
union once per candidate and prices both crossed roles.  Its result is

```text
first crossed role common-phase positive   143 / 304
rank7-on-nonreceiver role positive           0 / 304
both crossed roles positive                  0 / 304.
```

Thus the structural `C4` is a real receiver-bank actuator on the target/root
projection, but no occurrence in this frozen table is a literal common-state
actuator.

### Phase/private-model compatibility

The 304 structural edges are defined on the transported round-47 target
table.  An original singleton/F row there already carries a relocated lower
target.  The separately frozen private outer matching is bound to the
origin/res1972 model, so its lower assignment cannot be transported by row
name alone.  Exactly seven structural edges have the same F lower in the two
models.  Their exact DNF ledger is frozen separately.  Five of the seven make
the first crossed role positive in both phases, but all seven leave the new
rank-seven-on-F role with zero hyperarcs in both phases.  Hence even this
common-model subface has `0/7` complete receiver-bank C4s.

For the other 297 edges, private/supplier preservation was not tested and
must not be inferred.  The common-state zero already excludes them as full
packets on this endpoint grammar.

## 4. The exact support-three residual class

For three current length-two rows

\[
                (A_0,R_0),(A_1,R_1),(A_2,R_2),       \tag{4.1}
\]

a directed matching `C6` is

\[
 (A_0,R_0)+(A_1,R_1)+(A_2,R_2)
 \longmapsto
 (A_2,R_0)+(A_0,R_1)+(A_1,R_2),                     \tag{4.2}
\]

provided

\[
                     A_2\subsetneq R_0,quad
                     A_0\subsetneq R_1,quad
                     A_1\subsetneq R_2.              \tag{4.3}
\]

The complete indexed enumeration of (4.2) on all 7,395 current length-two
rows, anchored at the 12 support-two-uncovered rank-seven roles and requiring
at least one nonreceiver root, has exactly 208 cycles.  There are 72 distinct
roles in which the anchor rank-seven target is placed on an original F root.
Direct exact pricing gives

```text
phase-0-positive rank7-on-F roles   0 / 72
phase-1-positive rank7-on-F roles   0 / 72.
```

This kills all 204 F-using cycles before supplier/private rows.

The four all-original-P2 cycles are the only support-three candidates which
avoid that obstruction.  Their exact ledger is:

| rows | hyperarcs by new row, phase 0 / phase 1 | all roles common | supplier | private bank |
|---|---|---:|---:|---:|
| `23340,23365,10123` | `0/0, 0/0, 3400/3400` | no | pass | pass |
| `23340,23365,10837` | `0/0, 0/0, 621/1179` | no | pass | pass |
| `23955,23980,10375` | `2872/2872, 0/0, 1200/993` | no | pass | pass |
| `23955,23980,16810` | `3697/3697, 0/0, 3777/4242` | no | fail | pass |

Here “supplier pass” means every one of the 16,898 selected warm47 supplier
edges remains legal.  In the fourth row the unique recorded casualty is

```text
16810 -> 3407 : flag mask 50 -> 0.
```

“Private pass” means all 1,748 selected private tickets are footprint-disjoint
from the three changed P2 rows and the frozen outer matching remains
`16898 H + 1748 F`.  These private certificates are separate from the socket
oracle; they do not repair a zero socket role.

The phase owners used by the socket replay are frozen in the exact table.  In
the fourth candidate row 16810 has owner `84199` in phase 0 and `84211` in
phase 1; the displayed `3777/4242` counts use those different owners.  Every
other owner in the four-row table is identical between the two transported
phases.  Thus the no-go does not come from accidentally pricing against a
stale common owner.

## 5. What is and is not proved

Proved:

1. the exact distinction between fixed-bank rank-seven reassignment and a
   genuine receiver-set change;
2. structural support-two receiver-bank coverage `150/162`, with 12 exact
   zeros;
3. zero full common-state packets among all 304 support-two circuits;
4. the complete 208-cycle support-three residual catalogue;
5. zero sockets for all 72 distinct rank-seven-on-F roles used by its 204
   F-containing cycles;
6. exact per-role/per-phase no-go, supplier replay and private-footprint
   replay for all four all-P2 cycles; and
7. consequently, the support-at-most-three no-go stated in Section 1.

Not proved or excluded:

* a directed support-four `C8` or larger correlated chain-slot circuit;
* a chain-length-changing packet rather than the fixed 7,395-row face;
* a socket grammar richer than the complete one-short relaxed-nine five-cell
  oracle used here;
* indirect repair of an unchanged bad role through a regenerated ambient
  mode bank;
* simultaneous chronology, residence, upper/source/common-cap/compiler rows;
  or
* a K17 word or an all-dimensional theorem.

The standard two-ended reciprocal private-ticket collar also has a separate
five-chronological-role lower bound (`g0,e0,g1,e1,g2`) under the established
direct-adjacency obstruction.  That bound concerns literal guarded
serialization; it must not be confused with the support-two/support-three
target/root matching bounds proved here.

## 6. Frozen evidence

Structural receiver `C4`:

```text
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_receiver_bank_c4_structural_20260802.cpp
    654bd6658fb49d357961cc68d7c51ee0c1a5846849cb46b98ba37d1f1e755f20
  audit.json
    2c5863c2d05c669596aa5cff587be7eb2c13f538d041c15da0cf255a65c980d4
  candidates.tsv
    c0c471e47f7a038c8ec87f65fc26752872ea93c5bc16b5886ab88ffca439f7b1
```

Exact support-two socket catalogue:

```text
  audit_a_k17_receiver_bank_c4_common_phase_socket_20260802.cpp
    d544c74f5f3bd89c744920f47c89590c9a46fd95ffc46b5029b96b4d95e92ca5
  socket_catalogue.audit.json
    1f3aee9947fa6cb51fc67da2338dd7ddd5f0b92483cc17eec583f046799352dd
  aligned7_common_phase_socket.audit.tsv
    730c4247227c63b3f2f9f087f4228bbc98f453da4abc22ea907184bf3cc57d83
```

Support-three structural catalogue:

```text
scratch/a_k17_joint_chain_slot_receiver_c4_20260802/
  receiver_c6_cycles.tsv
    32bfe2225282791cd050a2ed424b50576c61c3f927cc27cf327034d7aa07f1ce
  receiver_c6.audit.json
    51f8c537c88da4cd55bd7cb88ac207019f77c89c168ca8a39da460e3dc7f4ade
```

Exact support-three state/resource audits:

```text
scratch/a_k17_receiver_bank_c4_20260802/
  audit_a_k17_receiver_bank_c6_common_phase_socket_20260802.cpp
    18c717f05976e82c6333408818cc5f6010dcca94eb55cb92c5179647d45c0af3
  audit_a_k17_rank7_on_f_common_phase_socket_20260802.cpp
    cb33262df430c3f622aeb5356ad862745546e62741e6423936d5f0317c3e1f66
  rank7_on_f_socket.audit.json
    fe50282c80ad372f234bf09660792073f5ae80f50161e00291c60696405e734a
  audit_a_k17_receiver_bank_c6_supplier_private_20260802.cpp
    e7759efba80e234fc1df1e15820d1929992e55e9fc7c3562308fe7684c079676
  all_p2_receiver_c6_exact_no_go.audit.tsv
    2cf60a02278e25e9b06a9615cac5ef56303746afd68594acb60eed956989c10b
```

The O3 campaign is retained at

```text
/home/amodo/or15/work/a_k17_receiver_bank_c4_20260802/
```

under explicit eight-worker caps for the finite socket catalogues.
