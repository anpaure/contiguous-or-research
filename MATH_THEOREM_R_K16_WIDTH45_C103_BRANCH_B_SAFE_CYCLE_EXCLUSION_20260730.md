# K16 WIDTH45: exact safe-cycle exclusion of the C=103 price-three/slack-one branch

Date: 2026-07-30  
Lane: R / native safe-cycle pricing  
Status: **exact source-relative theorem; branch B is excluded**

## 1. Statement and scope

On the frozen K16 length-eight source, use the authenticated 211,604-seam
WIDTH45/global-Sep5 interface and the symmetric scale-four certificate from

```text
MATH_THEOREM_R_K16_WIDTH45_SCALE4_DUAL_GF2_FLOOR103_20260730.md
```

At seam count `C=103`, the scale-four identity has three integral branches.
Branch B has target excess exactly one on a price-three target and total seam
slack exactly one.  There is no binary balanced global-Sep5 circulation in
branch B.

This is source-relative.  It does not exclude the no-repeat/slack-four branch
A, another carrier, reverse seams, or an unrestricted rethread.  It omits q1,
survivor, residence, compiler, connectedness and literal-word constraints.

## 2. Complete admitted graph

All seam slacks are nonnegative integers.  A branch-B binary circulation has
exactly one slack-one seam and every other selected seam is tight.  The unique
slack-one seam lies on a directed selected cycle, so it must admit a tight
directed return.  The authenticated complete integral admitted graph is
therefore

```text
7,742 tight seams + 43 slack-one seams with a tight return = 7,785 seams.
```

This pruning is complete for integral branch B.  It is not valid for the
fractional face, where a high-slack seam may carry small rational mass.

The exact exporter is

```text
scratch/export_r_k16_width45_branchB_cycle_graph_20260730.py
SHA-256 6dc441fa07fde9e4ff06032f6b1c44ff42710d895e519126eea09a3ed79f66b6
```

## 3. Safe-cycle exhaustion

A balanced capacity-one binary circulation is a vertex-disjoint union of
directed simple cycles.  Global Sep5 passes to each cycle.  Since branch B has
only one additional target occurrence globally, a cycle may repeat no target
unless it repeats exactly one price-three target exactly twice.

The O3 native generator

```text
scratch/r_k16_width45_safe_cycle_pricer_20260730.cpp
SHA-256 3637dea27c2ed59720873f926ad6017822f6a1fd13079e051c0b0073eadf0b07
```

enumerates tight simple cycles canonically by their least vertex and enumerates
each slack-one cycle as its unique slack seam followed by a tight return path.
During DFS it enforces cyclic Sep5 on physical source positions, simplicity,
length at most 103 and, in safe mode, the complete branch-B multiplicity rule
(target-simple, except for the one permitted price-three repeat).  It terminates
without a time or column cutoff.  On the H100 CPU it finds

```text
branch-B-compatible Sep5-safe: 22 tight cycles,  0 slack-one cycles;
target-relaxed Sep5-safe:      56 tight cycles, 43 slack-one cycles.
```

The target-relaxed run is necessary: branch B permits one special internal
price-three repeat, so target-simple enumeration alone would be insufficient.

An independent Python checker reparses the frozen raw binary and all three
authenticated JSON inputs.  It does not import or execute the native
generator.  For each of the 43 slack-one seams it exhausts every Sep5-safe
tight return path of length at most 102.  It explores 189,207 states, finds
exactly the same 43 slack-one cycles, and classifies them as

| number | repeated-target signature `(price,load)` |
|---:|---|
| 15 | `(3,2),(4,2)` |
| 15 | `(4,2)^4,(6,2)` |
| 13 | `(8,2)^2` |

Thus every slack-one cycle has at least one forbidden repeat in addition to,
or instead of, the sole permitted price-three repeat.  The number of
branch-B-compatible slack cycles is zero.

## 4. Proof

Assume a branch-B binary circulation exists.  Its selected graph has equal
in- and out-degree at every port and capacity at most one, hence decomposes
into directed simple cycles.  Total slack one implies exactly one selected
slack-one seam; let `Z` be its cycle.  All other seams of `Z` are tight, its
length is at most the total selected count 103, and global Sep5 makes `Z`
individually Sep5-safe.  The exhaustive census therefore contains `Z`.

Branch B services every target once except one price-three target twice.
Consequently the target multiplicities internal to `Z` may have no repeated
target, or exactly that single price-three target at load two.  The census
shows that none of the 43 possible cycles has this form, a contradiction.
Therefore branch B is infeasible.  QED.

## 5. Frozen artifacts

```text
scratch/audit_r_k16_width45_c103_branchB_safe_cycles_20260730.py
  SHA-256 caf1686e91f8b859a2132bab4fd31046883a73844a0c3e75cb7f87cba553289a

scratch/k16_width45_c103_branchB_safe_cycle_exhaustion_20260730.audit.json
  SHA-256 9e45987c6ed464fbb601df58da6f6ac0cb1655f42fdef7701493845d302698ad
  payload b141f36cdc804e10dfac1cdb947188bd3a2fdfb288816a77ecd7bf6e53596d43

scratch/k16_width45_c103_branchB_safe_cycle_pool_20260730.json
  SHA-256 c4501821acbf598a6628835bb84c2ec9ae6fe4e575f987dad7dcbf75942e6895

scratch/k16_width45_c103_branchB_safe_cycle_relaxed_pool_20260730.json
  SHA-256 fcacacafede479c0ebfd361ad5a9a7daf3313c93006bde2e943389a46cf0fe8e

scratch/k16_width45_c103_branchB_complete_safe_cycle_master_20260730.audit.json
  SHA-256 c322701b4e34db5b032d27e6d8c7718028ef572d65c65df8a4680b05e890f54f
```

The last artifact is deliberately marked as a restricted-pool solver result;
it is not the proof.  The theorem is supplied by the complete admitted-graph
reduction plus the two matching exhaustive cycle enumerations above.

## 6. Remaining C=103 face

The earlier GF(2) lock excludes the tight price-four branch C.  This new
theorem excludes branch B.  Therefore the only remaining C=103 numerical face
is branch A:

```text
all 93 targets serviced exactly once, total seam slack exactly four.
```

That is now the unique WIDTH45/global-Sep5 construction target at the proved
floor.
