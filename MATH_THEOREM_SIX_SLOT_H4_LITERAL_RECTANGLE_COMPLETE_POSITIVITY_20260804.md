# Six-slot `h=4`: complete positivity of the literal correlated rectangle

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It proves the
literal correlated rectangle gate strictly positive on its complete
residual domain.  Combined with the already-proved initial period
interval and the exact literal reduction, this closes the complete
six-slot inert `h=4` branch.  No search or sampled computation is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 \delta_*={43849\over643260},
 \qquad
 \tau_0=A+\delta_*,
\tag{0.1}
\]

and

\[
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0).
\tag{0.2}
\]

The exact correlated rectangle is

\[
\boxed{
\begin{aligned}
 \mathfrak R(\delta,P,u)={}&C(\tau)+F_\tau(P)+F_\tau(P+u)\\
 &+\min\{C(\tau),F_\tau(u)\}-\Gamma(\delta),
 \qquad \tau=A+\delta,
\end{aligned}}
\tag{0.3}
\]

on

\[
 \delta_*\le\delta\le A/2,
 \qquad
 {2\tau\over3}\le P\le A,
 \qquad
 0\le u\le\min\{A-P,P/4\}.
\tag{0.4}
\]

The closed active side `F((A-delta)/2)>=57/1400`, including its switch,
already satisfies

\[
                         \mathfrak R>{3653\over700000}.
\tag{0.5}
\]

We prove the inactive side.  There

\[
                         \Gamma(\delta)={1\over20000}.
\tag{0.6}
\]

## 1. Two uniform train banks

The inactive-`u=0` theorem proves

\[
 \boxed{
 H_\tau(w):=C(\tau)+F_\tau(w)>{11\over20000}}
\tag{1.1}

for every `tau>=tau_0` and every

\[
                         {2\tau\over3}\le w\le A.
\tag{1.2}
\]

Its proof also gives the following separate upper-shift floor.

### Lemma 1.1 (upper bank)

For every point satisfying (1.2),

\[
                         \boxed{F_\tau(w)>-{213\over4000}.}
\tag{1.3}
\]

#### Proof

Reduce the period to `tau_0`, as in the `u=0` theorem.  If
`w/A<=17/20`, its compact and period-tail bounds are

\[
 K(w)>-{51\over1000},
 \qquad
 \text{tail}<{9\over4000}.
\]

If `w/A>=17/20`, they are

\[
 K(w)>-{13\over250},
 \qquad
 \text{tail}<{1\over800}.
\]

Both ledgers give the same result:

\[
 -{51\over1000}-{9\over4000}
 =-{13\over250}-{1\over800}
 =-{213\over4000}.
\]

Increasing the period only raises the train.  This proves (1.3).
\(\square\)

We next establish the matching low bank.

### Lemma 1.2 (low bank)

For every `tau>=tau_0` and every `0<=u<=A/5`,

\[
                         \boxed{F_\tau(u)>{269\over5000}.}
\tag{1.4}
\]

#### Proof

The period-uniform critical-point theorem says that every interior
critical point of `F_tau` on `[0,A/2]` is a strict local maximum.
Therefore the minimum on `[0,A/5]` is attained at `0` or `A/5`.

At zero, the ceiling-tail ledger from the `u=0` theorem gives

\[
 F_\tau(0)=C(\tau)
 >{881\over10000}-{343\over10000}
 ={269\over5000}.
\tag{1.5}
\]

At `A/5`, the compact quarter estimate gives

\[
                         K(A/5)>{9\over125}.
\tag{1.6}
\]

The first period-tail argument satisfies

\[
 A+\tau+{A\over5}
 \ge {11A\over5}+\delta_*
 >{201779\over100000}.
\]

Its square exceeds `4071/1000`, whose exponential is greater than `57`.
Every successive squared-argument gap is at least `27\pi/20`, whose
exponential is greater than `60`.  Hence the complete tail is smaller
than

\[
 {1/57\over1-1/60}={20\over1121}<{9\over500}.
\tag{1.7}
\]

Equations (1.6)--(1.7) give

\[
 F_\tau(A/5)>{9\over125}-{9\over500}
 ={27\over500}>{269\over5000}.
\]

Both endpoints are strictly above `269/5000`, proving (1.4).
\(\square\)

## 2. The domain automatically couples the two banks

### Lemma 2.1

Every point of the rectangle domain satisfies

\[
 \boxed{
 0\le u\le{A\over5},
 \qquad
 {2\tau\over3}\le P\le P+u\le A.}
\tag{2.1}
\]

#### Proof

If `P<=4A/5`, then `u<=P/4<=A/5`.  If `P>=4A/5`, then
`u<=A-P<=A/5`.  The remaining inequalities are immediate from (0.4).
\(\square\)

Combining Lemmas 1.1, 1.2, and 2.1 gives the exact cross-bank margin

\[
\boxed{
 F_\tau(u)+F_\tau(P+u)
 >{269\over5000}-{213\over4000}
 ={11\over20000}.}
\tag{2.2}
\]

## 3. Complete inactive sign

### Theorem 3.1

On the complete inactive side,

\[
                         \boxed{\mathfrak R>{21\over20000}>0.}
\tag{3.1}
\]

#### Proof

There are only two low branches.

If the minimum in (0.3) is `C(tau)`, then both upper shifts lie in the
range of (1.1), so

\[
 \mathfrak R
 =H_\tau(P)+H_\tau(P+u)-{1\over20000}
 >{21\over20000}.
\tag{3.2}
\]

If the minimum is `F_tau(u)`, use (1.1) for `P` and (2.2):

\[
\begin{aligned}
 \mathfrak R
 &=H_\tau(P)+\{F_\tau(u)+F_\tau(P+u)\}
   -{1\over20000}\\
 &>{11\over20000}+{11\over20000}-{1\over20000}
 ={21\over20000}.
\end{aligned}
\tag{3.3}
\]

This proves (3.1). \(\square\)

### Corollary 3.2 (complete residual rectangle)

On the whole domain (0.4),

\[
                         \boxed{\mathfrak R>{21\over20000}>0.}
\tag{3.4}
\]

#### Proof

The inactive side is Theorem 3.1.  On the closed active side, (0.5) is
stronger because

\[
                         {3653\over700000}>{21\over20000}.
\]

The active theorem includes the switch, so the two cases cover the whole
domain. \(\square\)

## 4. Complete physical `h=4` consequence

The literal correlated reduction proves that every residual physical
inert `h=4` table satisfies

\[
                         \Phi>\mathfrak R.
\]

Corollary 3.2 therefore gives `Phi>0` throughout the residual interval
`delta>=delta_*`.  The corrected local-gate theorem already proves
physical positivity for `0<=delta<=delta_*`.

### Theorem 4.1

Every canonical six-slot size-four-efficient inert table has strictly
positive Bellman functional.  Equivalently, the complete six-slot inert
`h=4` branch is closed.

This conclusion concerns the frozen six-slot Bellman classification.  It
does not by itself prove arbitrary-grid Bellman positivity, the all-`n`
analytic theorem, or an OR-word upper bound.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| literal correlated reduction | `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| active-`Gamma` complete positivity | `MATH_THEOREM_SIX_SLOT_H4_ACTIVE_GAMMA_COMPLETE_POSITIVITY_AND_BOUNDARY_COLLAPSE_20260804.md` | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| inactive `u=0` theorem and train ledgers | `MATH_THEOREM_SIX_SLOT_H4_INACTIVE_U0_BOUNDARY_COMPLETE_POSITIVITY_20260804.md` | `ba327b06397a9190de23c62c6a0ca0f985bbb75bff12188540518550e03ecd8f` |
| quarter compact endpoint price | `MATH_THEOREM_SIX_SLOT_H4_INACTIVE_QUARTER_BOUNDARY_COMPLETE_POSITIVITY_20260804.md` | `60ebf810ad63bafd01fa19661780fad8a0fc1a52c2266f1a58995cc5fe635dc1` |
| corrected initial interval | `MATH_THEOREM_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.md` | `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af` |
| period-uniform critical-point theorem | `MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md` | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| compact Gaussian prices | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
