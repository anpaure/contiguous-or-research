# Hostile audit: canonical two-step GK primitive fibers

**Date:** 2026-08-14
**Verdict:** PASS at the frozen source hash below
**Scope:** independent conceptual audit; no reliance on the finite replay

## Audited source

`MATH_THEOREM_CANONICAL_TWO_STEP_GK_SELECTOR_EXACT_PRIMITIVE_FIBERS_AND_HALF_HEAD_DEFECT_20260814.md`

H100 SHA-256:

`07b0d67d29c9b9827072db5287f33b394df40c051420e2fccf96b3d39b651aad`

## Findings

1. The map `U -> L(U)` is exactly two consecutive downward steps in the
   linear Greene--Kleitman chain, so its lower injectivity follows from the
   symmetric-chain partition.  After the first step, `p` is the last free
   zero and `q` the first free one; hence `q>p` and the canonical option is
   leaf-right.
2. The central-factor convention is correct.  With `a>0`, `D_a` is the
   balanced gap between the last free zero and first free one.  With `a=0`,
   it is `D_0`, the balanced prefix before the unique first free one.
3. The inverse-fiber statement is exact.  Flipping the closing zero of a
   top-level primitive factor of `D_a` exposes precisely its opening and
   that flipped coordinate as the first two free ones.  Conversely, for an
   inverse `U`, the pair formed by `p(U)` and the changed zero `q(U)` lies in
   `D_a` and has no intervening free symbol, so it is exactly one top-level
   primitive factor.  The constructions are inverse.
4. For fixed `a`, there are exactly `2a+1` arbitrary noncentral Dyck gaps;
   the central gap with `k` primitive components contributes `(xC)^k`.
   Therefore the generating function reduction

   \[
   \sum_{a\ge0}[x^{m-a}](xC)^kC^{2a+1}
   =[x^{m-k}]\frac{C^{k+1}}{1-xC^2}
   =[x^{m-k}]\frac{C^{k+1}}{2-C}
   \]

   is correct.
5. The Lagrange identity

   \[
   [x^r]\frac{C(x)^s}{2-C(x)}={2r+s-1\choose r}
   \qquad(r\ge0,\ s\ge1)
   \]

   is valid, and substituting `r=m-k`, `s=k+1` gives
   `{2m-k choose m-k}`.  The subsequent hockey-stick sum, Pascal difference,
   and ratio `(m-1)/(2m+1)` are all correct.
6. The scope is now accurate: the canonical collision ledger is not itself
   a Hall proof for the complete leaf host, while the separate leaf-right
   head-projection obstruction at `m=7` forces chart-zero resets.  The note
   does not claim the impossible pure leaf-right all-parameter theorem.

No mathematical defect or overclaim remains at the audited source hash.
