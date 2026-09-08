# Self-audit: Rayleigh canonical distance-split local-capacity no-go

**Date:** 2026-08-05  
**Method:** independent proof replay inside the producing lane; no search or
solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_CANONICAL_DISTANCE_SPLIT_LOCAL_CAPACITY_NOGO_20260805.md`  
**Verdict:** **GO.**

## Checks

1. With level measure `du`, the derivatives
   `d(c-ell)/du=1/q` and `d(r-c)/du=1/a` give occurrence densities `q`
   and `a`; no inverse Jacobian is missing.
2. The orientation of the two `e` comparisons is correct.  At `ell=.565`
   the candidate right endpoint at distance `b` has a lower `K`-value, so
   the true right endpoint lies farther away.  At `ell=.575` the reverse
   holds.  Since separation decreases with the left endpoint, this traps
   `e` between them.
3. The extrema in (2.3) occur at the expected rational rectangle corners:
   `-K'(e)` is minimized at the largest `e` and smallest `A`, whereas
   `-K'(y)` on `y in (.206,.218)` is maximized at the largest `y` and
   largest `A`.  The finite exponential enclosure leaves the stated strict
   gap `0.205<0.218`.
4. At `y_-^0`, the physical density is strictly smaller than `-K'(y_-^0)`
   because `u'>0`.  The canonical left-piece demand equals `-K'(e)`, so
   it exceeds capacity.  Continuity upgrades the endpoint comparison to a
   positive-measure interval.
5. The right-piece image starts above `0.251`, while `y_-^0<0.218`; no
   hidden coincident right demand is needed for the contradiction.

The conclusion is limited to coefficient-one use of the fixed pivot `c`.
Thinning, a moving pivot, and general unequal two-piece couplings remain
open.
