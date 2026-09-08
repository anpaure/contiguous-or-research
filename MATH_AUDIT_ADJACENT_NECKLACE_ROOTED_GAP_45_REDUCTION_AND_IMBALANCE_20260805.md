# Audit: rooted gap 4/5 reduction and imbalance

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_ROOTED_GAP_45_REDUCTION_AND_IMBALANCE_20260805.md`
  
**Method:** inverse-rule and generating-function audit; no search  
**Verdict:** PASS after the Section 3 hub-fibre correction.

## 1. Involution check

The scan ignores only 4 and 5.  A split `g -> 3,g-3` creates the first
active symbol 3 at the same location; merging restores `g`.  A merge
`3,h -> h+3` creates the first active symbol at least 6 at the same
location; splitting restores the pair.  The protected root is unaffected,
including when `h` is the final gap.

Thus the residual is exactly a 4/5 internal prefix and an arbitrary final
gap at least three.

## 2. Binary path check

For fixed prefix length and number of fives, the final gap is forced by
the total.  Moving a cut between adjacent gaps transfers one unit, so the
only move preserving the 4/5 alphabet is `45 <-> 54`.  Coarsening the
pointed boundary produces a distinguished 9 and recovers the two
orientations after the split site and every other expansion are fixed.

The original stronger sentence that every path matching is automatically
hub-rainbow was false.  A hub with two 9-parts has independent expansions;
the two disjoint edges displayed in (3.3) share that hub.  The corrected
theorem claims only the forward pointed-edge-to-hub map and explicitly
retains hub-rainbow selection as an extra condition.

## 3. Imbalance check

Odd and even coordinate positions contribute factors `(1-z)` and
`(1+z)` respectively.  Pairing them gives `(1-z^2)^m`, with one extra
`(1-z)` when `n` is odd.  The coefficient formulas in the theorem follow.

At `n=4,t=2`, the magnitude is `binom(2,1)=2`, so no path matching can
have deficiency at most one.  This validates the stated no-go scope.

## 4. Scope

The root is marked data and is not silently forgotten.  The theorem also
does not claim that unique hubs alone make the blossom interiors available
after previous matching stages.  Both limitations are stated.
