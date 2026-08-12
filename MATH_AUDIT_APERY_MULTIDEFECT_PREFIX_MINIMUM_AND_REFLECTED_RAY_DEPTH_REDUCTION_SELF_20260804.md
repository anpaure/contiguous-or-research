# Self-audit: multidefect prefix minima and reflected-ray depth reduction

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md`  
**Target SHA-256:**
`843497f6d0a7a409165f20b0dbfab513e3b5a63d9e73a708c5f947665192945f`  
**Verdict:** **PASS / GO as a reduction and sufficient subchamber theorem.**

This is a proof self-audit, not an independent-authorship audit.  No
enumeration, solver, numerical search, Python, or H100 computation was used.

## 1. Cyclic block algebra

For a length-`t` cyclic gap block beginning after residue `r`, its value is

\[
 s_{r+t}-s_r
 \quad\hbox{or}\quad
 P+s_{r+t-h}-s_r.
\]

The two carry-aware superadditivity inequalities say exactly that this is at
least `s_t`.  Summing over all `h` starts counts each gap `t` times, yielding

\[
                         hs_t\le tP.
\]

The case `t=1` proves every gap is at least `s_1`.  No ordering of the
remaining gaps is assumed.

With `p=P/h` and `d_t=tp-s_t`, ordinary and carry superadditivity both reduce
to

\[
 d_{(r+t)\bmod h}\le d_r+d_t.
\]

The gap identity follows by subtraction, including the wrap after setting
`d_h=d_0=0`.  Thus the deficit parametrization is exact.

## 2. Endpoint-period comparison

At exact first carry, a legal size-`h+1` configuration has value
`P+s_1=A`.  For `0<=r<=h`, the old clock at capacity `(h+1)q+r` is at least

\[
 qA+c_r,
 \quad
 c_0=0,\quad c_r=s_r\ (1\le r<h),\quad c_h=P.
\]

For `q=0` equality holds.  For `q>=1`, both sides are at least `A`, where
the kernel is increasing.  Therefore termwise summation has the direction

\[
 \Phi(W)\ge C+\sum_{r=1}^{h-1}F(s_r)+F(P).
\]

This verifies the crucial lower-comparison direction.

## 3. Reflected-ray indexing

If `u` shifts are above `A/2`, they are exactly
`s_(h-u),...,s_(h-1)`.  Pair `s_(h-i)` with `s_(i+1)`.  Their indices sum
to `h+1`, so carry superadditivity gives

\[
 s_{i+1}+s_{h-i}\le P+s_1=A.
\]

Hence `X_i<=Y_i`.  Since `Y_i<1/2`, the paired early shift is genuinely
lower.  This also proves the early and late index sets are disjoint.

The first reflected point obeys

\[
 A-s_{h-1}=a+\gamma_h\ge2a,
\]

and successive reflected gaps are old cyclic gaps, each at least `a`.
Thus `Y_i>=(i+1)alpha` with no omitted endpoint.

Using `rho(A-w)=rho(w)`, every upper term is exactly

\[
 F(s_{h-i})=g(Y_i)-f(Y_i).
\]

Together with the early term `f(X_i)`, this proves the exact decomposition
(3.6).  All unpaired residues lie below the midpoint and contribute a
strictly positive compact train value.

## 4. Transport-depth estimate

For `D(t)=#\{i:X_i<=t<Y_i\}`,

\[
 \sum_i(f(X_i)-f(Y_i))=-\int f'(t)D(t)\,dt.
\]

The portion where `f'<=0` is favorable.  On the positive-slope portion,
`D<=H`; because `f` is one-mode, its total positive variation is at most
`sup f-f(0)`.  Therefore

\[
                         T\ge-H(\sup f-C).
\]

This argument does not require the transport intervals to be disjoint.  It
is precisely their maximum overlap depth that is priced.

## 5. Theta-ray estimate

There are `u+1` theta terms, giving the unconditional strict bound
`Theta>-(u+1)/20000`.

For the stronger branch, monotonicity and `Y_i>=(i+1)alpha` give

\[
 \Theta\ge\sum_{j=1}^{u+1}g(j\alpha).
\]

The last arithmetic point is below `1/2`.  Right-endpoint quadrature gives

\[
 \alpha\sum_{j=1}^{u+1}g(j\alpha)
 \ge\int_0^{(u+1)\alpha}g.
\]

Since `g` is increasing and has zero integral on `[0,1/2]`, every terminal
tail integral is nonnegative.  Consequently the last integral is bounded
below by minus the uncovered terminal length times `g(1/2)`.  Under
`(u+2)alpha>=1/2`, that length is at most `alpha`, so division introduces
no factor depending on `u`:

\[
                         \Theta\ge-g(1/2)>-1/20000.
\]

## 6. Constant arithmetic

The compact contribution satisfies

\[
 C-H(61/1000-C)
 =(H+1)C-H(61/1000)
 >{43-18H\over1000}.
\]

After the theta charge `tau/20000`, this is

\[
                         {860-360H-\tau\over20000}.
\]

Thus `360H+tau<=860` implies strict positivity.  Under terminal coverage,
`tau=1`; for `H=2` the numerator is `139`.  Without coverage, `tau=u+1`,
giving the stated cutoffs `u<=139` at depth two and `u<=499` at depth one.

Finally `u+1<h-u` gives `h>=2u+2`, hence the residual period bounds 282
and 1002.

## 7. Scope audit

The theorem does **not** prove a universal uncrossing to one defect.  It
proves instead that all exact-first-carry multidefect dependence in the
endpoint comparison is controlled by `(H,tau)`, and closes the region
`360H+tau<=860`.

It does not address threshold overshoot, later first carry, the original
clock's finite Apéry shoulder, endpoint-critical clocks, or any integral
OR-word construction.  Subject to that scope, the theorem is proof-safe.
