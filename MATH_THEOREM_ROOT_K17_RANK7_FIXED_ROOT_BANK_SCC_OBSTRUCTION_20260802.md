# K17 rank-seven fixed-root-bank SCC obstruction

Date: 2026-08-02

## Verdict

No suffix rethread confined to the current rank-seven receiver-root bank can
**move every one** of the 623 frozen rank-seven P2 socket-zero target labels.
This remains true even after all rank-seven slots are allowed to participate
and every lower-bottom containment constraint is deleted.  In that generous
relaxation, 162 of the 623 bad P2 labels are singleton strongly connected
components of the exact assignment digraph.  Socket, state, supplier, and
protected-resource tests can only delete assignment arcs, so they cannot make
one of those labels movable.

Therefore any architecture that repairs each defect by moving its own
rank-seven label must change which rank-eight roots receive rank-seven
targets, equivalently recouple the full three-level chain partition.  This
does **not** yet prove root recoupling necessary for every possible socket
repair: moving other H middles can create new endpoint modes for a P2 role
whose own target label stays fixed.

## Assignment digraph

The authenticated table uses every rank-seven target exactly once in 19,448
rank-seven slots:

- 785 fixed P2 rank-seven bottoms;
- 1,748 shortened-H rank-seven bottoms; and
- 16,915 long-H rank-seven middles.

Each slot has a fixed rank-eight root.  Contract the current target-to-root
assignment.  For slots `u,v`, put an arc `u -> v` when the rank-seven label
currently at `u` is strictly contained in the fixed root at `v`.  In the
literal fixed-bottom face, also require the unchanged lower bottom at a long
H destination `v` to lie below the incoming rank-seven label.

A root-preserving reassignment is a permutation supported by these arcs.  It
decomposes into directed cycles.  Hence a slot can change its label only if it
lies in a nontrivial strongly connected component.  This is an exact
necessity, independent of how long the circuit is.

## Exact ladder

The independently replayed SCC counts are:

| face | vertices | arcs | SCCs | largest SCC | bad movable | bad stuck |
|---|---:|---:|---:|---:|---:|---:|
| current long H + rank-7 P2, fixed bottoms | 17,700 | 29,109 | 12,536 | 4,077 | 194 | 429 |
| all rank-7 slots, fixed bottoms | 19,448 | 44,407 | 7,728 | 10,683 | 220 | 403 |
| all rank-7 slots, bottom constraints deleted | 19,448 | 136,136 | 421 | 18,953 | 461 | 162 |

The last row is a strict overapproximation of every fixed-root-bank physical
target reassignment.  Its 162 singleton bad roles prove the claimed
**target-movement** no-go.  The positive P2--H--H C6 remains useful—it shows
local rank-seven movement and can repair part of the bank—but no packing that
requires every bad target itself to move can finish the entire rank-seven
task on the frozen root bank.  Indirect DNF repair of an unchanged role is
outside this SCC statement.

## Required next object for the target-movement route

The exact next outer object for that route is the global three-level chain
flow on

\[
  21,777\text{ targets of ranks }1\ldots6,
  \quad19,448\text{ rank-seven targets},
  \quad24,310\text{ rank-eight roots}.
\]

It may choose anew which 19,448 roots receive a rank-seven predecessor and
which 16,915 of those rank-seven slots receive a lower predecessor.  The
frozen P2 squares and suffix C6s are fundamental circuits of restricted faces
of this larger integral chain-recoupling system.

This theorem does not prove that the global recoupling has a socket-complete
solution.  It proves that such a root-bank change is necessary for the
move-each-defect architecture.  A fixed-root construction remains logically
possible only through regenerated endpoint/state DNFs that repair some of
the 162 immovable roles indirectly.

## Evidence

Audit source:

- `scratch/audit_root_k17_rank7_fixed_root_bank_scc_obstruction_20260802.cpp`, SHA-256 `e85553287c401e53dfa06a4b75441323f7aed556c879fb3a9694a189738e4411`;
- `scratch/k17_fixed_p2_role_moving_escape_20260802/rank7_fixed_root_bank_scc.audit.json`, SHA-256 `df4b4b18a356a5c65a7f6ffdf5228d90367944ba1a117bd02b0e4888e9f534e4`.

The original count-identical O3 replay is frozen at
`/home/amodo/or15/work/root_k17_rank7_fixed_root_bank_scc_obstruction_20260802/`;
its old conclusion string predates the scope correction above and is not
load-bearing.  A separately written audit of the maximally relaxed row
reproduces `19448/136136/421/18953/461/162` under

```text
scratch/audit_k17_rank7_fixed_root_assignment_scc_20260802.cpp
  14cd04785aefcc1dd524f272b11c861d8a942c2717cc58e3595b62e1bfe6fcd2
scratch/k17_rank7_p2_hh_c6_audit_20260802/fixed_root_scc.audit.json
  65904e7e33fe1f6df3004077fea1800ac2f9ec05aee1253467b99cf2c2608b85
```

Inputs are the two complete fixed-P2 global-union metric files and the two
authenticated `s7` phase tables.  The phase tables have identical target
chains and roots; only their owners differ.  The audit checks all input
censuses, constructs every containment arc directly from masks, computes SCCs
twice, and asserts the exact ladder above.

Scope exclusions: a changed rank-eight receiver bank, an enlarged
three-level chain flow, common-phase socket pricing, protected/private-bank
reconstruction, supplier Hall, long-state flow, chronology, residence,
upper/source/compiler closure, and a word.
