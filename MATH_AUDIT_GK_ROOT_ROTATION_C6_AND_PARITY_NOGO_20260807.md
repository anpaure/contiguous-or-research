# Audit: GK root-rotation C6 and parity obstruction

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_GK_ROOT_ROTATION_C6_AND_PARITY_NOGO_20260807.md`  
**Verdict:** **GO, with the no-go scoped to disjoint paired-root circuits.**

## Checks

1. The words `L=1A1B0C0D` and `R=1A0B1C0D` are Dyck whenever
   `A,B,C,D` are Dyck.  Setting the four displayed bits to zero gives the
   common rank-`(m-2)` word `a`.
2. Substitution gives
   `B_{x,L}=X_R`, `B_{y,L}=Z`, `B_{x,R}=Z`, and `B_{y,R}=X_L`.
   Applying the fixed GK successor to `X_L,X_R,Z` gives the three displayed
   upper vertices.  The union of the two endpoint switches is exactly one
   alternating six-cycle, not two private four-edge paths.
3. The suppressed triangle has common intersection `a` and three distinct
   union colours.  The `Z` word has unmatched-symbol pattern `0001`, while
   every fixed root facet `X_U` has unmatched-symbol pattern `00`; hence
   `Z` cannot collide with the fixed `X` bank.  Its unique unmatched one
   recovers `a`, proving injectivity of `a -> Z`.
4. Moving the displayed one across the balanced block `B` and one zero
   changes inversion number by `|B|+1`, which is odd.  The root-rotation
   graph is therefore bipartite.
5. The first-return inversion recurrence gives `d_{2s}=0` and
   `d_{2s+1}=-Cat_s`.  Hence any matching leaves at least `Cat_s` vertices
   on semilength `2s+1`.

## Scope

The parity theorem rules out only a bank formed from mutually disjoint
paired-root `C_6` circuits.  It does not rule out overlapping circuits whose
symmetric difference is degree two, higher alternating circuits, or a
second matching/omission phase that changes the parity balance.
