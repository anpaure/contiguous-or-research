# Independent audit: order-free two-corridor Hamilton contraction

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_ROOT_ORDER_FREE_TWO_CORRIDOR_HAMILTON_CONTRACTION_20260802.md`  
**Audited theorem SHA:**
`7231f74bf433c75d81e117d21861e9763862ccba62ca3ee6accbd6c13c6ea9e6`  
**Verdict:** `PASS_SCOPE_SAFE`

## Checks

1. **State fibres.**  The theorem uses partition-Hamiltonicity: exactly one
   accepted state is selected from each physical-fragment fibre.  It invokes
   ordinary Hamiltonicity only after a globally compatible state has already
   been fixed for every fragment.  Thus it does not mistake multiple state
   copies for multiple physical fragments.
2. **Global capacities.**  Shared capacities are required to live in a
   genuinely global/cumulative state expansion.  Independent local arc
   filtering is explicitly declared insufficient.
3. **Pump contraction.**  Contracting
   `A_b -> F -> P_3 -> E -> D_c` removes every internal `P_3` fragment from
   the residual bank.  The marked arc carries the complete internal owner,
   arc, history, private-resource, and voltage ledger, preventing reuse or
   double counting.
4. **Topology.**  With the four Boolean-hex endpoints distinct, deleting the
   prescribed arcs from a partition-Hamilton cycle leaves exactly the two
   vertex-disjoint spanning corridors
   `D_c -> C_bc` and `B_bc -> A_b`.  The crossed endpoint pairing would close
   two cycles and therefore cannot come from one Hamilton cycle.
5. **Directional forced-arc contraction.**  For `u -> v`, the contracted
   state retains only entrances to `u` and exits from `v`; expansion uniquely
   restores the forced arc.  Distinct endpoint histories and resource states
   remain distinct marked states.

## Scope

The note is an exact graph-theoretic reduction, not a Hamiltonicity theorem.
It does not prove robust expansion, existence of the accepted
partition-Hamilton cycle, zero background charge, deeper upper coverage,
source factorization, the lower compiler, or regeneration.  No correction to
the audited theorem is required.

