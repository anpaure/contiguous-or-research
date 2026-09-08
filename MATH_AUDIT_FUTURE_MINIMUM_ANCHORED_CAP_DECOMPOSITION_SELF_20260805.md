# Self-audit: future-minimum anchored/cap decomposition

**Date:** 2026-08-05  
**Method:** proof replay; no search or solver  
**Audited theorem:**
`MATH_THEOREM_FUTURE_MINIMUM_ANCHORED_CAP_DECOMPOSITION_20260805.md`  
**Verdict:** **GO.**

1. Shrinking the future interval `[y,B]` makes its minimum nondecreasing.
   Continuity follows from uniform continuity of `g` (equivalently, Berge's
   compact maximum/minimum theorem for this interval correspondence).
2. Any nondecreasing `v<=g` obeys `v(y)<=v(t)<=g(t)` for all `t>=y`, so
   `v<=h`; maximality is pointwise exact.
3. The cap `k=g-h` is nonnegative and vanishes at both endpoints.  Hence
   every positive superlevel component of `k` is internal, while every
   superlevel set of nondecreasing `h` is terminal and upper-anchored.
4. The notation `Lambda_g^split` is deliberately a chosen layer
   representation obtained by separately decomposing `h` and `k`; it is
   not claimed to equal the nonlinear canonical superlevel decomposition
   of `g` itself.  Their barycenters nevertheless add exactly to `g(y)dy`.
5. For Rayleigh, strict decrease at `b` makes `g_2(y)>g_2(b)` immediately
   to the left.  The future minimum there is at most `g_2(b)`, so the cap is
   genuinely nonzero on a positive interval.

No unimodality or finite number of critical points is assumed.  The output
has two typed density banks, although either bank may contain a continuum
of uniform layers.
