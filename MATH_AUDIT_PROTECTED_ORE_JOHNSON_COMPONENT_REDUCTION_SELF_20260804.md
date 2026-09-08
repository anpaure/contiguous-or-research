# Self-audit: protected Ore Johnson-component reduction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_PROTECTED_ORE_JOHNSON_COMPONENT_REDUCTION_20260804.md`

## Verdict

Self-audit **GO**, pending an independent audit before the theorem is used
as a frozen dependency.

## Checks

1. For one rank-`m` owner, every pair of its rank-`m-1` facets has
   intersection rank `m-2`; hence all selected facets of one owner lie in
   one component of the induced Johnson graph.
2. The upper shadows of distinct components are therefore disjoint.
3. On an owner in one component shadow, both `a_U` and the protected
   complement count `p_U` agree for the whole cut and the component cut;
   no facet from another component is incident with that owner.
4. The local formulas for `sigma`, `lambda`, shadow surplus, and `b` thus
   add exactly, proving the connected-cut equivalence.
5. The frozen equality classification has pairwise support intersections
   at most `m-3`, so its summands are precisely separate Johnson
   components.  A connected equality cut has one support.
6. `J(2m-1,m-1)` has degree `(m-1)m`.
7. A canonical spanning-tree depth-first traversal has length `2(t-1)`
   and visited set exactly the connected family.  Counting all walks gives
   the claimed deliberately coarse entropy bound.
8. The near-shadow cardinality estimate is quoted with its exact final
   SHA and is not strengthened silently.

## Scope guard

The theorem reduces all protected Ore checks to connected lower cuts.  It
does not claim that complements of connected cuts are connected, does not
close the positive-clique-defect family, and does not prove factor
extension for the common-core reservoir.
