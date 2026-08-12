# K16 WIDTH45: exact safe-tight-cycle exclusion of C=103 branch C

Date: 2026-07-30  
Status: **exact source-relative theorem; branch C is excluded**

At `C=103`, branch C has scale-four slack zero and one additional service
occurrence on a price-four target.  Every selected seam is therefore tight.
A balanced capacity-one binary support is a vertex-disjoint union of directed
simple cycles, and global Sep5 passes to each cycle.

The complete integral admitted graph has 7,742 tight seams.  An independent
Python DFS, using canonical least-vertex roots and the physical cyclic Sep5
positions, exhausts every tight directed simple cycle of length at most 103.
It terminates with

```text
complete Sep5-safe tight simple cycles       56
branch-C-compatible cycles                   52
mandatory targets with any compatible provider 60
mandatory targets with no compatible provider  33
```

A cycle is branch-C-compatible precisely when it is target-simple, or has
exactly one price-four target at load two and no other repeat.  Since 33
mandatory targets have no provider in the complete compatible cycle bank, no
union of such cycles can satisfy branch C.  This proves branch-C infeasibility
without invoking the earlier GF(2) lock or a solver.

The native O3 census and independent Python census agree exactly on all 56
ordered seam cycles.  The corresponding restricted master also dies in
presolve, but that solver result is not needed for the theorem.

Artifacts:

```text
scratch/audit_r_k16_width45_c103_branchC_safe_tight_cycles_20260730.py
  SHA-256 462b10b7a892b42dcc6e93b74c2ae889223c067e943f84e15db9bde876a9c5a4

scratch/k16_width45_c103_branchC_safe_tight_cycle_exhaustion_20260730.audit.json
  SHA-256 6f4d673387dcfcdec2cdcbc5f218e27eecd64f8d369f1edcf96d6b1e0edbee9c
  payload f59c17c8c65adb5f9ef09fd60f3de7e34a295496a8d428b95194d7140da19576

scratch/k16_width45_c103_branchB_safe_cycle_relaxed_pool_20260730.json
  SHA-256 fcacacafede479c0ebfd361ad5a9a7daf3313c93006bde2e943389a46cf0fe8e
```

Scope: the frozen K16 WIDTH45/global-Sep5 source-relative seam model only.
This does not exclude another carrier, reverse seams or unrestricted
rethreading.  Together with the branch-B safe-cycle theorem, it leaves exactly
one C=103 face: exact-once service of all 93 targets with total slack four
(branch A).
