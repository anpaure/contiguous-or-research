# Hostile audit: reflection owner search lattice and residual gate

**Date:** 2026-08-14
**Verdict:** PASS for the exact Benders/defect-cover reductions, modular
ranks, and stated capped E116 evidence.  No owner factor or infeasibility
claim is made.

## Frozen source

```text
MATH_REDUCTION_Q4_K17_REFLECTION_OWNER_SEARCH_LATTICE_AND_RESIDUAL_GATE_20260814.md
SHA-256 f74a14f67f3ee0b256b841ab1e06e5632252bb4a509317c15259d616d3c3d81a
```

## Exact checks

Fixing 35 pairwise-disjoint self footprints covers 140 nonfixed bracelet
rows, so 54 disjoint ten-row pair configurations cover exactly the
remaining 540.  Both implications of the residual exact-cover interface
are literal.

For an incumbent with loads in `{0,1,2}`, every exact target deletes a
vertex cover of the doubled-row defect graph.  The retained outside is
simple, and incidence conservation gives
`|F_R|=4*s_R+10*p_R`.  Target-only configurations exactly patch `F_R`
with the same destroyed self-group and pair profile.  Conversely, any such
patch gives an exact target.  At a zero row or zero group, branching over a
replacement configuration and adding all retained blockers is exhaustive;
using only one greedy blocker branch is correctly labelled heuristic.

The mod-two nullspace claims follow from the displayed column incidences.
On the full 750-row master, the all-row and fixed-70 indicators are
independent null vectors; rank 748 proves completeness.  On the 715-row
fixed-matching face, the nonfixed-680 indicator is null and rank 714 proves
uniqueness.  The 540-row residual has only its forced even-column relation.
Full mod-three ranks in all three systems give full rational row rank via a
nonzero maximal integer minor.  The replayed targets are consistent.

The E116 load histogram, structural-zero cover data, and UNKNOWN outcomes
match the bound H100 artifacts.  They are explicitly scoped to one
incumbent and finite caps.  The still-live residual Kissat process is not
part of this frozen verdict, and no E86 data from the independent Benders
lane are imported.

All replay and hashing ran through SSH on H100.  The local Mac was used
only for reading, editing, transfer, and Git.
