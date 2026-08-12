# Audit: labelled even capacity-two edge extendability

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_LABELLED_EVEN_CAPACITY_TWO_EDGE_EXTENDABILITY_AND_STRICT_HALL_20260805.md`  
**Method:** local-path and first-active-pair replay; no computation  
**Verdict:** PASS on the labelled sector.  No quotient descent is inferred.

## 1. Prescribed-edge scan

Every coordinate edge of an even cycle belongs to an alternating perfect
matching of coordinate positions.  On the selected coordinate pair, the
fixed-mass allocation graph has orders `1,2,3,2,1`.  Its unique edge is
forced at masses one and three; at mass two, choosing the unmatched end of
the three-vertex path opposite the prescribed edge makes that edge part of
the local matching.

Placing this coordinate pair first ensures both endpoints of the prescribed
global edge activate it.  Earlier coordinates do not exist, and swapping
the local pair leaves it nonquiet, so the first-active scan reverses.  An
all-quiet state would have even mass in every coordinate pair, contradicting
odd total mass.  Hence the scan is a perfect matching containing the edge.

## 2. Strict Hall

If a proper nonempty shore set `U` were tight, connectivity forces an edge
from `N(U)` to the opposite-shore complement.  No perfect matching can use
that edge because `U` would then have fewer than `|U|` remaining neighbours.
Edge extendability contradicts this, giving one unit of strict slack.

The strict unit does not address the empty shore set, where endpoint-list
packing is tested directly, and it does not pay two simultaneous
bicircular-surplus units.

## 3. Quotient warning

The scan chooses a literal coordinate root and generally breaks an odd
rotational stabilizer.  Literal edge extendability therefore does not
imply quotient-edge extendability or strict quotient Hall.  The theorem's
scope statement is exact.

Under a semiregular action, however, every lifted shore set and its
neighbourhood have sizes multiplied by `|H|`.  The positive labelled slack
is a multiple of `|H|`, so it descends as at least one quotient unit.  A
rotation of order `d` fixes a token state only when `d` divides its total
mass.  Hence `gcd(R,|H|)=1` is a valid sufficient condition for
semiregularity.  This verifies the theorem's arithmetic quotient
corollary while leaving nonsemiregular periodic sectors open.
