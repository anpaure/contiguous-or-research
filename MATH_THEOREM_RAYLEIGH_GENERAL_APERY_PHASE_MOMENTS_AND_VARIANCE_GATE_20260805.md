# General Apéry phase moments and one finite cyclic-variance gate

**Date:** 2026-08-05  
**Method:** pure mathematics; exact queue moments and Fourier--Parseval
reduction; no computation, search, or solver  
**Status:** unconditional reduction.  For every formal Apéry clock, the
mean and variance of its complete periodic counting discrepancy are exact
functions of the first two moments of the normalized residue defect.  The
all-period Rayleigh transform theorem then reduces formal positivity to
one finite inequality for a cyclic subadditive metric.  That metric
inequality is verified on the arithmetic, endpoint, mechanical, and all
period-five extreme families, but is not proved here for every cyclic
metric.  Finite shoulders remain separate.

**Subsequent closure (2026-08-05):** the finite inequality isolated here is
now proved for every period in
`MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md`,
with an independent GO audit.  Accordingly the complete formal periodic
Rayleigh phase is closed; only the explicitly separate finite-shoulder
problem remains on this analytic branch.

## 1. Normalized defects and phase intervals

Let a formal Apéry clock have true residue period `g`, endpoint period

\[
 P=g\lambda\le\zeta,
\]

and residue shifts

\[
 s_r=r\lambda-d_r
 \qquad(0\le r<g).
\]

Normalize the defect by

\[
 e_r={d_r\over\lambda},
 \qquad e_0=e_g=0,
\tag{1.1}
\]

and put

\[
 a_r={s_r\over\lambda}=r-e_r,
 \qquad a_g=g.
\tag{1.2}
\]

The physical shift table is nondecreasing, so

\[
 a_{r+1}-a_r=1+e_r-e_{r+1}\ge0.
\tag{1.3}
\]

The normalized defects obey

\[
 e_{r+t}\le e_r+e_t
\]

cyclically, and physical nonnegativity gives

\[
 0\le e_r\le r.
\tag{1.4}
\]

Let `H(x)` count the formal clock points below `x`, and define its
equal-work discrepancy

\[
 D(x)=H(x)-{x\over\lambda}.
\tag{1.5}
\]

Then `D` is `P`-periodic.  On the normalized phase interval

\[
 a_r<y<a_{r+1},
 \qquad y={x\over\lambda},
\]

one has

\[
 \boxed{D(\lambda y)=r+1-y.}
\tag{1.6}
\]

Thus this branch descends from height `1+e_r` to height `e_(r+1)`.
Zero-length branches caused by repeated phases contribute nothing, so the
formula remains exact without a distinctness assumption.

## 2. Exact first and second moments

Write

\[
 \overline e={1\over g}\sum_{r=0}^{g-1}e_r,
 \qquad
 \operatorname {Var}(e)
 ={1\over g}\sum_{r=0}^{g-1}(e_r-\overline e)^2.
\tag{2.1}
\]

### Theorem 2.1 (Apéry phase moment identity)

For a uniformly sampled point of one period,

\[
 \boxed{
 \mathbb ED={1\over2}+\overline e,}
\tag{2.2}
\]

and

\[
 \boxed{
 \operatorname {Var}(D)
 ={1\over12}+\operatorname {Var}(e).}
\tag{2.3}
\]

#### Proof

Integrating (1.6) over every branch gives

\[
\begin{aligned}
 \mathbb ED
 &={1\over2g}\sum_{r=0}^{g-1}
 \bigl((1+e_r)^2-e_{r+1}^2\bigr)\\
 &={1\over2}+\overline e,
\end{aligned}
\]

because the cyclic square terms telescope.  Similarly,

\[
\begin{aligned}
 \mathbb ED^2
 &={1\over3g}\sum_{r=0}^{g-1}
 \bigl((1+e_r)^3-e_{r+1}^3\bigr)\\
 &={1\over3}+\overline e+overline{e^2}.
\end{aligned}
\]

Subtracting `(1/2+bar e)^2` gives (2.3). \(\square\)

This identity explains the exact `1/12` arithmetic floor variance and
isolates every nonarithmetic contribution as the ordinary residue-defect
variance.

## 3. Fourier lower bound for the complete formal phase

Tail integration and equal work give

\[
 \Phi(U)=\int_0^\infty D(x)q(x)dx,
 \qquad q=-K'.
\tag{3.1}
\]

Let

\[
 B={5324\over875}.
\]

For every nonzero Fourier frequency of period `P`, the all-period theorem
gives

\[
 \left|\widehat q\left({2\pi n\over P}\right)\right|
 <{BP^2\over4\pi^2n^2}.
\tag{3.2}
\]

Parseval and Cauchy--Schwarz, exactly as in the sparse Beatty proof, yield

\[
 |\text{nonzero modes}|
 <{BP^2\over2\sqrt{90}}
 \sqrt{{\operatorname {Var}(D)\over2}}.
\tag{3.3}
\]

The strict all-period coefficient inequality

\[
 BP^2<12\sqrt{15}M
\tag{3.4}
\]

turns (3.3) into

\[
 \boxed{
 |\text{nonzero modes}|
 <M\sqrt{3\operatorname {Var}(D)}
 =M\sqrt{{1\over4}+3\operatorname {Var}(e)}.}
\tag{3.5}
\]

The zeroth mode is

\[
 M\left({1\over2}+\overline e\right).
\tag{3.6}
\]

Therefore the complete formal phase has the unconditional lower bound

\[
 \boxed{
 \Phi(U)
 >M\left(
 {1\over2}+\overline e
 -\sqrt{{1\over4}+3\operatorname {Var}(e)}
 \right).}
\tag{3.7}
\]

## 4. The finite cyclic-variance gate

### Corollary 4.1

Every formal Apéry clock whose normalized cyclic defect satisfies

\[
 \boxed{
 \operatorname {Var}(e)
 \le {\overline e(\overline e+1)\over3}}
\tag{4.1}
\]

has strictly positive Rayleigh phase functional.

#### Proof

Equation (4.1) is exactly

\[
 {1\over4}+3\operatorname {Var}(e)
 \le\left({1\over2}+\overline e\right)^2.
\]

All quantities are nonnegative.  Apply (3.7); the strict coefficient
inequality (3.4) retains strict positivity even in the equality case.
\(\square\)

Thus complete formal Apéry positivity follows from one finite statement:

> **Cyclic Apéry variance conjecture.**  Every nonnegative cyclically
> subadditive profile `e` with `e_0=0` and `e_r<=r` satisfies (4.1).

The `+1` in (4.1) is the normalization supplied by the unit-step physical
bound.  It is sharp on both boundary clocks.

## 5. Exact equality calibrations

### Arithmetic clock

Here `e_r=0`, so both sides of (4.1) vanish.  The phase discrepancy is the
unit sawtooth, with mean `1/2` and variance `1/12`.

### Endpoint-only directed-cycle clock

Here

\[
 e_r=r\qquad(0\le r<g).
\]

Thus

\[
 \overline e={g-1\over2},
 \qquad
 \operatorname {Var}(e)={g^2-1\over12}
 ={\overline e(\overline e+1)\over3}.
\]

So (4.1) is exact, not a loose sufficient estimate.

### Mechanical and period-five extreme clocks

For a mechanical clock `U_m=eta floor(mh/g)`, put `L=g/h` and `t=1/h`.
The same cell calculation as in the Beatty theorem gives the full
discrepancy law

\[
 A_h+L V,
\]

so its squared mean-minus-variance comparison is

\[
 (1+L-t)^2-(1+L^2-t^2)=2(L-t)(1-t)\ge0.
\]

Thus (4.1) holds for every mechanical clock.  Direct substitution also
verifies it for the two nonmechanical period-five extreme rays
`(0,1,1,0,2)` and `(0,2,1,1,2)`.  Their stronger phase decompositions are
already proved separately.

## 6. A useful pair-difference reduction

Cyclic subadditivity implies, for every fixed residue `t`,

\[
 -e_{-t}\le e_{r+t}-e_r\le e_t.
\tag{6.1}
\]

The average over `r` of the middle difference is zero.  The elementary
zero-mean bounded-interval variance bound therefore gives

\[
 {1\over g}\sum_r(e_{r+t}-e_r)^2
 \le e_t e_{-t}.
\tag{6.2}
\]

Averaging over `t` and using

\[
 {1\over g^2}\sum_{r,t}(e_{r+t}-e_r)^2
 =2\operatorname {Var}(e)
\]

gives

\[
 \boxed{
 \operatorname {Var}(e)
 \le {1\over2g}\sum_{t=0}^{g-1}e_t e_{-t}.}
\tag{6.3}
\]

Consequently the product inequality

\[
 \sum_t e_t e_{-t}
 \le {2g\over3}\overline e(\overline e+1)
\tag{6.4}
\]

would imply the full variance conjecture.  Equality holds in (6.2)--(6.4)
for the directed-cycle profile `e_r=r`.  Equation (6.4) is a second,
often more combinatorial, form of the surviving finite gate.

## 7. Exact boundary

The theorem removes all analytic Fourier and queue-shape ambiguity from
the formal-clock problem: only (4.1), or the stronger product estimate
(6.4), remains.  It does not prove either inequality for every cyclic
subadditive profile.

Even a proof of formal phase positivity would still leave the finite
availability shoulder.  Its queue is nonperiodic and does not enter the
telescoping moment identity (2.2)--(2.3) without an additional conductor
or regeneration estimate.

## 8. Dependencies

1. `MATH_THEOREM_RAYLEIGH_APERY_DEFECT_QUEUE_AND_ZEROTH_MODE_RESERVE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_ALL_APERY_PERIOD_FOURIER_POSITIVITY_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_ALL_MECHANICAL_APERY_ROTORS_POSITIVE_20260805.md`.
