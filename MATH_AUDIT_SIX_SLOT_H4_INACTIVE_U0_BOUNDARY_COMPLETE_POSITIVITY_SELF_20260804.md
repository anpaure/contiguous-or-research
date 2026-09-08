# Self-audit: inactive `u=0` rectangle boundary

**Date:** 2026-08-04  
**Target:**
`MATH_THEOREM_SIX_SLOT_H4_INACTIVE_U0_BOUNDARY_COMPLETE_POSITIVITY_20260804.md`  
**Target SHA-256:**
`ba327b06397a9190de23c62c6a0ca0f985bbb75bff12188540518550e03ecd8f`  
**Verdict:** **SELF-AUDIT GO.**  The period reduction, both compact
ranges, both shifted-tail ranges, and the final margin replay exactly.
This is not an independent audit.

## 1. Period reduction and base constants

For fixed `P`, both `C(tau)` and `F_tau(P)` have strictly positive period
derivative, so reduction to `tau_0=A+delta_*` is valid.  Feasibility is
preserved because `P>=2tau/3>=2tau_0/3`.

The rational preliminaries replay as

\[
 A>{4431\over5000},
 \qquad
 \delta_*>{1363\over20000},
 \qquad
 1-2e^{-\pi/4}>{881\over10000}.
\]

The first ceiling argument satisfies

\[
 2A+\delta_*>{36811\over20000},
 \qquad
 \left({36811\over20000}\right)^2>{271\over80}.
\]

The degree-twelve positive Taylor sum at `271/80` exceeds `5000/169`,
so the first tail is `<169/5000`.  The second argument exceeds
`27949/10000`, whose square is `>39/5`.  From the second term onward the
ratio is `<1/200`, giving remainder `<1/2000`.  Thus

\[
 \mathcal T_0<{169\over5000}+{1\over2000}
 ={343\over10000}.
\]

## 2. Compact lower range

The admissible normalized shift satisfies `t>7/10`.  On this interval

\[
 {d\over dt}\log\left({1+t\over1-t}e^{-\pi t}\right)>0.
\]

At `17/20`, the ratio is `<1`, so `K` decreases up to that endpoint.
The endpoint prices are

\[
 1-e^{-9\pi/1600}>{87\over5000},
 \qquad
 e^{-1369\pi/1600}<{171\over2500}.
\]

Therefore

\[
 K(17A/20)>{87-342\over5000}=-{51\over1000}.
\]

All inequality directions are correct: the first price uses
`1-e^{-x}>x-x^2/2`, and the second uses a positive Taylor lower bound for
the reciprocal exponential.

## 3. Compact upper range

With `s=1-t`, an interior critical point satisfies

\[
 (2-s)e^{-\pi(2-s)^2/4}=s e^{-\pi s^2/4}.
\]

The quotient is strictly decreasing on `(0,3/20]`, and its value at
`3/25` is `<1`; hence every critical point has `s<3/25`.  At such a point

\[
 K=1-{2\over2-s}e^{-\pi s^2/4}.
\]

The subtracted expression increases through `3/25`.  The endpoint bound

\[
 e^{-9\pi/2500}<{12361\over12500}
\]

therefore gives the exact identity

\[
 {50\over47}{12361\over12500}={263\over250}.
\]

Thus every interior critical value is `>-13/250`; the two endpoints are
stronger.  This validates the complete upper compact range.

## 4. Shifted tails

In the lower range, the first argument exceeds `148607/60000`, whose
square is `>613/100`.  The first exponential is `<1/450`, and every
successive ratio is `<1/100`.  Hence

\[
 \mathcal T_P<{2\over891}<{9\over4000}.
\]

For `P>=17A/20`, the first argument exceeds `129691/50000`, whose square
is `>6727/1000`.  The first exponential is `<1/810`, giving

\[
 \mathcal T_P<{1/810\over1-1/100}<{1\over800}.
\]

The common ratio price uses the exact gap floor `19\pi/12`.

## 5. Final ledger

Both ranges give the same exact surplus.  Lower range:

\[
 {881\over10000}-{343\over10000}
 -{51\over1000}-{9\over4000}
 ={11\over20000}.
\]

Upper range:

\[
 {881\over10000}-{343\over10000}
 -{13\over250}-{1\over800}
 ={11\over20000}.
\]

On inactive `Gamma`, the charge is exactly `1/20000`, so

\[
 \mathfrak R(\delta,P,0)
 >2{11\over20000}-{1\over20000}
 ={21\over20000}>0.
\]

The `P=A` face is included because the domain forces `u=0` there.

## 6. Scope

The audit supports only the complete `u=0` face (inactive here, active by
the predecessor).  No conclusion is drawn for the other inactive
boundaries.
