# Self-audit: hook-C6 adjacency uniqueness

**Date:** 2026-08-05  
**Object:**
`MATH_THEOREM_PBBS_HOOK_C6_ADJACENCY_UNIQUENESS_20260805.md`  
**Method:** independent profile, rank, and scope audit; no search

## 1. Profile subtraction

The hook and promoted-hook peak profiles are

\[
                         (b+1,1^{h-1}),
        \qquad           (b,1^h).
\]

Their common size-`(m-1)` predecessor is `(b,1^(h-1))`: subtracting from
the hook must occur in row one, and subtracting from the promoted hook must
occur in row `h+1`.  There is no second row choice yielding the same
partition.  The sibling formula therefore gives block heights `0,0,h`.

## 2. Empty-block implication

A nonempty Dyck word contains an up-step and has height at least one.
Thus both height-zero blocks are literally empty, not merely action-empty.
The three children of `000D` are exactly `D10,10D,1D0`; their actions have
the required sizes.

## 3. Angle implication

One peak deletion of a base hook leaves a mountain with `2h-1` insertion
gaps.  Prepending/appending one primitive peak increments the first/last
gap.  These are adjacent on the cyclic gap order.  Hence the transfer is
one edge in the cyclic earthmover metric.

The metric statement is made only for chains whose hook-to-hook stages all
remain on this repeated-hook face.  A promoted-parent excursion changes
the vacancy-circle length and is explicitly excluded from the no-go.

## 4. Dependency and verdict

The proof uses only the already-proved deficit-three sibling-profile
identity and the literal hook peak-deletion coordinates.  It does not use
the unproved global matching or halo-packing statements.

**Verdict: PASS.**

