# Self-audit: Rayleigh bounded-arity equal-split support no-go

**Date:** 2026-08-05  
**Method:** proof replay; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_BOUNDED_ARITY_EQUAL_SPLIT_SUPPORT_NOGO_20260805.md`  
**Verdict:** **GO.**

1. A job `x>=B` split into at most `M` equal pieces produces only sizes
   `x/n>=B/M`; mixtures preserve this support inclusion.
2. In the first transformed residual, `f_2` vanishes on `(0,b]`, while the
   strict one-well inequality makes `g_2` positive at every point of
   `(0,b)`.
3. For the displayed two/three recursion and `0<y<b/3`, both arguments
   `2y,3y` lie outside the job support, so its right side is identically
   zero and its left side strictly positive.
4. The proof uses equality of pieces essentially.  It makes no claim about
   unequal two/three packets, in which one piece can tend to zero, or about
   equal splitting with unbounded arity.

No endpoint atom, Jacobian, or count identity enters the obstruction.
