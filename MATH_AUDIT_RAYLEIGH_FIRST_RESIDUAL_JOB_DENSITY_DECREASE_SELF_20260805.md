# Self-audit: first Rayleigh residual job-density decrease

**Date:** 2026-08-05  
**Method:** proof replay; no search or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_JOB_DENSITY_DECREASE_20260805.md`  
**Verdict:** **GO.**

1. The formula
   `u''=(q^3 K''(r)+a^3 K''(ell))/(a+q)^3` has already been independently
   checked from the inverse-branch Jacobians.
2. For `t>=b`, `ell` stays in `[b,e]`, where the displayed `Q'` bounds make
   `K''>0`; hence `q=-K'(ell)>=-K'(e)>1/5`.
3. Also `r>=R`, so `w=A+r>1.9202`.  The Rayleigh tail `Q(w)` is decreasing
   there and the exact exponential bracket gives `a<1/10`.
4. The identity `Q'(w)=-Q(w)(2w-1/w)` is exact.  Its multiplier exceeds
   three, while the global bound `K''(ell)<8/5` holds regardless of the
   sign of the latter curvature.
5. Therefore the negative contribution in the numerator is larger than
   `3/125`, while the possible positive contribution is smaller than
   `2/125`; the numerator is strictly negative for every `t>b`.

The theorem proves monotonicity only for the transformed job density on its
post-cancellation support.  It does not supply a monotone decomposition of
the socket density or an arity/mean split.
