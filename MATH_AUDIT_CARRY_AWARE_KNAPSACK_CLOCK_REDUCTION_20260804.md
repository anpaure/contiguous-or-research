# Independent-style audit: carry-aware knapsack clock reduction

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_CARRY_AWARE_KNAPSACK_CLOCK_REDUCTION_20260804.md`  
**Verdict:** **PASS**, with the Bellman inequality (5.7) explicitly left
open.

## 1. Minimal extension

Internal superadditivity implies that every partition of `t<=1` has value
at most `b(t)`.  Concatenation of feasible lists proves that `mathsf S b`
is superadditive, and enlarging the capacity proves monotonicity.  Any
global extension dominates the value of every feasible list, hence
dominates `mathsf S b`.  These facts verify Theorem 1.1.

If two parts have sum at most one, merging them preserves feasibility and
does not lower value.  After all such mergers, at most one part is at most
one half.  Therefore a partition of capacity `t` has fewer than `2t+1`
parts, establishing the finite-arity statement.

## 2. Sign in the variational reduction

For `t>=1`, the partition consisting of `floor(t)` copies of one gives

\[
 (\mathsf Sb)(t)\ge\lfloor t\rfloor b(1)\ge A.
\]

On `[A,infinity)`,

\[
 K(x)=-e^{-(A+x)^2}
\]

is increasing.  Since every extension satisfies `a>=mathsf S b`, replacing
`a` by the least extension makes the tail integral smaller, not larger.
The first-period profile is fixed.  Hence (2.2) is an exact infimum, not
merely a lower envelope.

Time rescaling multiplies the integral by a positive factor and preserves
superadditivity.  Every nonzero finite superadditive clock eventually
reaches `A`, because `a(nh)>=n a(h)`.  This validates the normalization
`b(1)>=A`.

For a clock which jumps to infinity, ordinary truncation would indeed be
invalid because `min(a,T)` need not remain superadditive.  The theorem does
not use it.  If finite values before blow-up are unbounded, normalization
occurs before the blow-up.  If they are bounded, changing only the blow-up
endpoint to a sufficiently large `T` preserves every internal inequality;
the resulting tail is bounded by the summable Gaussian series associated
with `floor(t)T` and tends to zero.  This validates the limiting argument.

## 3. Carry formulas

Both partitions displayed before (3.1) have total capacity `q+r`, so their
values are legitimate lower bounds on `mathsf S b(q+r)`.  All such values
are at least `A` for `q>=1`; inserting their maximum into the increasing
tail kernel gives the direction in (3.2).

For the half-step profile, every unit of value `A` consumes at least one
half unit of time, while half-unit pieces attain this rate.  Therefore its
closure is `A floor(2t)`.  The functional is half the arithmetic-clock sum,
which is strictly positive by the already proved all-ceiling theorem.  The
old negative endpoint pair fixed the incompatible value `b(1)=A`; true
superadditivity forces `b(1)>=2A`.

## 4. Grid and Bellman recurrence

For `x+y<=1`,

\[
 \lfloor nx\rfloor+\lfloor ny\rfloor
 \le\lfloor n(x+y)\rfloor.
\]

Monotonicity and superadditivity of `b` therefore make `b_n` internally
superadditive.  A grid-cell value `c_j` can be obtained with minimum
capacity `j/n`; consequently the closure at capacity `t` is precisely the
integer unbounded-knapsack value at capacity `floor(nt)`.  This verifies
(5.4)--(5.6).  The series converges because

\[
 V_m\ge\lfloor m/n\rfloor c_n
\]

and the negative Gaussian tail is summable.

## 5. Counterexample preservation

The lower grid profiles satisfy `b_n<=b`, hence their closures satisfy
`mathsf S b_n<=mathsf S b`.  Tail monotonicity gives the perhaps
counterintuitive but essential inequality

\[
 \int_1^\infty K(\mathsf S b_n)
 \le\int_1^\infty K(\mathsf S b).
\]

On the compact first period, a monotone function has only countably many
discontinuities, so dominated convergence gives convergence of the first
integrals.  Thus a negative compact profile forces a negative finite grid
profile for all sufficiently fine grids.  This proves the nontrivial
direction of Theorem 5.1 without requiring convergence of the knapsack
closures themselves.

## 6. Denomination-insertion obstruction

The denomination-insertion calculation follows directly from the exact
ceiling identity.  Its positive correction term is smaller than `3/70` by
the displayed geometric Gaussian bound, whereas
`1/2-exp(-pi/4)>3/70`; hence the Bellman margin strictly decreases.  The
replacement proof for a generator with `c<=V_j` is exact, so dominated
insertions are correctly separated from the undominated obstruction.

## 7. Two-slot theorem

For `n=2`, internal superadditivity is exactly `T>=2y`; this gives the two
residue classes in (7.2).  At fixed `y`, increasing `T` moves only tail
arguments to the right, so the Bellman sum increases.

When `T=2y`, the two classes are the arithmetic lattice of step `y`.  In
the remaining range `y<=A/2`, differentiation of the uniformly convergent
Gaussian series is legitimate.  At a critical point, the first-derivative
identity supplies the exact weights needed to compare logarithmic
derivatives.  Since `lambda(z)=1/z-2z` decreases and

\[
 \lambda(A+y)+\lambda(A-y)
 =2A\left((A^2-y^2)^{-1}-2\right)<0,
\]

every critical point is a strict maximum.  Therefore an endpoint minimizes
the shift, and both endpoints reduce to proved ceiling clocks.  This
validates strict positivity without a numerical estimate.

## 8. Scope boundary

The theorem does **not** establish the Bellman inequality (5.7).  It also
does not establish:

* existence of an exact Rayleigh coagulation;
* an integral chain fragmentation;
* a resident central factor;
* upper occurrence selection or a common-cap router;
* `nu(k)<=B(k)+O(1)`.

Its exact gain is to replace the unsound independent-residue relaxation by
a carry-faithful finite dynamic program.  A remaining separator, if one
exists, is necessarily a finite mixed-denomination Bellman table.
