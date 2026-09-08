# Self-audit: optional-core coordinate span and local-cube cover

**Date:** 2026-08-04  
**Artifact:**
`MATH_COROLLARY_OPTIONAL_CORE_COORDINATE_SPAN_AND_LOCAL_CUBE_COVER_20260804.md`  
**Verdict:** **GO**.  The result is an elementary fixed-rank counting
corollary of the sharp optional-core cardinality bound.

## 1. Span check

Every member of a common-rank family `B` has the form

\[
                         C(B)\cup Z,
 \qquad Z\in{U(B)-C(B)\choose t}                     \tag{1.1}
\]

for the same `t`.  Therefore

\[
 |B|\le {h(B)\choose t}
      \le {h(B)\choose\lfloor h(B)/2\rfloor}.        \tag{1.2}
\]

The central binomial coefficients strictly increase with the dimension.
At dimension `2D-1` their value is exactly
`binom(2D-1,D-1)`.  The strict optional-core lower bound is one larger, so
dimension `2D-1` is impossible and `h(B)>=2D` is exact.

## 2. Cover check

The intersections of `B` with the covering intervals need not be disjoint.
That only makes the union bound

\[
 |B|\le\sum_i|B\cap[X_i,Y_i]|
      \le t{h\choose\lfloor h/2\rfloor}              \tag{2.1}
\]

weaker and therefore safe.  Dividing by the per-interval maximum gives the
displayed ceiling bound.

For `h=D+C`, Stirling's formula gives logarithm base two

\[
 (2D-1)-{1\over2}\log_2D
 -(D+C)+{1\over2}\log_2(D+C)+O(1)
 =D-C+O(1),                                          \tag{2.2}
\]

so the stated exponential cover count is correct.

## 3. Optional substitution and scope

With `D=d-3`, the sharp theorem gives

\[
 |B^-|\ge {2D-1\choose D-1}+1.
\]

Hence the free-coordinate span is at least

\[
                         2D=2d-6.
\]

No claim is made that the current reservoir confines the core to fewer
coordinates or to a bounded interval cover.  The corollary is therefore a
necessary localization barrier, not a global core-elimination theorem.

