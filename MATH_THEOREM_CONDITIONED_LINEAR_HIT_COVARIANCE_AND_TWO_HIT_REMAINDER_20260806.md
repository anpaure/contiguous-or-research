# Conditioned linear-hit covariance and the exact two-hit remainder

**Date:** 2026-08-06  
**Method:** conditional variance, exact linearization of a row-hit event,
fixed-count covariance projection, and the elementary factorial inequality
\((n-1)^2\le 2\binom n2\); no computation or search  
**Status:** unconditional reduction for the centered survivor carré. It
strictly sharpens the positive PINC4 coarea bound: all constant
fixed-count blocker modes cancel exactly, and the nonlinear remainder is
already a first-two-hit term. The stopped centered second-incidence
covariance is not bounded here.

This note continues
MATH_THEOREM_CONDITIONED_SURVIVOR_COAREA_AND_SECOND_INCIDENCE_CODEGREE_GATE_20260806.md.
All quantities below are at one fixed stopped state.

## 1. The row-hit variable

Retain

\[
 z_A(x)={\bf1}_{\{x\in U_A^\circ\cap T\}},
 \qquad
 \theta_A^G=t_A{\bf1}_{\{G\cap S_A=\varnothing\}},
 \qquad 0<t_A\le C_t.
\tag{1.1}
\]

For a live output \(x\), write

\[
 L_x=\{G:x\notin G\},
 \qquad
 n_A^x(G)=|G\cap(S_A-\{x\})|.
\tag{1.2}
\]

On \(L_x\), the row is killed exactly when \(n_A^x(G)>0\). Put

\[
 w_A^x=\mu_Az_A(x)t_A,
 \qquad
 F_x(G)=\sum_Aw_A^x{\bf1}_{\{n_A^x(G)>0\}}.
\tag{1.3}
\]

### Lemma 1.1 (the survivor carré is a conditional row-hit variance)

For \(G\in L_x\),

\[
 \sum_A\mu_Az_A(x)\widetilde\theta_A^{G,x}
 =-\bigl(F_x(G)-\mathbb E_i(F_x\mid L_x)\bigr).
\tag{1.4}
\]

Consequently, under the live-reference lower bound

\[
                         c_x'\ge c_rc_x,
\tag{1.5}
\]

one has

\[
 \boxed{
 \mathcal C_i\le {1\over c_r}
 \sum_x{1\over c_x}
 \mathbb E_i\!\left[
   {\bf1}_{L_x}
   \bigl(F_x-\mathbb E_i(F_x\mid L_x)\bigr)^2
 \right].}
\tag{1.6}
\]

#### Proof

On \(L_x\),

\[
 \theta_A^G=t_A(1-{\bf1}_{\{n_A^x(G)>0\}}).
\]

Subtract its conditional mean, multiply by \(\mu_Az_A(x)\), and sum.
This gives (1.4). Insert it in the definition of \(\mathcal C_i\) and
use (1.5). \(\square\)

## 2. Exact linearization and a factorial remainder

For every integer \(n\ge0\), define

\[
                         r(n)=n-{\bf1}_{\{n>0\}}.
\tag{2.1}
\]

Then

\[
 {\bf1}_{\{n>0\}}=n-r(n),
 \qquad
 0\le r(n),
 \qquad
 \boxed{r(n)^2\le2{n\choose2}.}
\tag{2.2}
\]

The last inequality is equality at \(n=2\); for \(n\ge2\), it is
\((n-1)^2\le n(n-1)\).

Define the literal linear-incidence coefficients

\[
 \lambda_{x,y}=\sum_Aw_A^x\chi_A(y)
               =\sum_A\mu_Az_A(x)t_A\chi_A(y),
 \qquad y\ne x.
\tag{2.3}
\]

Put

\[
 \begin{aligned}
 L_x^{\rm lin}(G)&=\sum_{y\ne x}\lambda_{x,y}{\bf1}_{\{y\in G\}},\\
 R_x^{\ge2}(G)&=\sum_Aw_A^xr(n_A^x(G)).
 \end{aligned}
\tag{2.4}
\]

Then, pointwise on \(L_x\),

\[
                         F_x=L_x^{\rm lin}-R_x^{\ge2}.
\tag{2.5}
\]

Moreover, with

\[
                         g_x^{(t)}=\sum_Aw_A^x\le C_tg_x,
\tag{2.6}
\]

Cauchy--Schwarz and (2.2) give the exact first-two-hit bound

\[
 \boxed{
 (R_x^{\ge2}(G))^2
 \le2g_x^{(t)}
       \sum_Aw_A^x{n_A^x(G)\choose2}.}
\tag{2.7}
\]

Thus the nonlinear error does not require a four-hit estimate. It starts
at two literal hits and has precisely the factorial weight used in the
existing FE3 expansion.

## 3. The exact conditioned covariance matrix

Write

\[
 \begin{aligned}
 X_x&=\sum_{G:x\notin G}a_G=X-Y_x,\\
 Y_{y\mid\bar x}&=\sum_{G:x\notin G,\ y\in G}a_G,\\
 Y_{y,z\mid\bar x}&=\sum_{G:x\notin G,\ \{y,z\}\subseteq G}a_G,
 \end{aligned}
\tag{3.1}
\]

with \(Y_{y,y\mid\bar x}=Y_{y\mid\bar x}\). Define

\[
 K_x(y,z)=Y_{y,z\mid\bar x}
 -{Y_{y\mid\bar x}Y_{z\mid\bar x}\over X_x}.
\tag{3.2}
\]

This is \(X_x\) times the covariance matrix of the accepted-edge
incidence vector under the law conditioned on \(L_x\), and is therefore
positive semidefinite.

### Theorem 3.1 (centered coarea identity)

One has

\[
 \boxed{
 \mathbb E_i\!\left[{\bf1}_{L_x}
   \bigl(L_x^{\rm lin}-\mathbb E_i(L_x^{\rm lin}\mid L_x)\bigr)^2
 \right]
 ={1\over X}\sum_{y,z\ne x}
       K_x(y,z)\lambda_{x,y}\lambda_{x,z}.}
\tag{3.3}
\]

Consequently,

\[
 \boxed{
 \begin{aligned}
 \mathcal C_i\le{}&{2\over c_rX}
   \sum_x{1\over c_x}
      \sum_{y,z\ne x}K_x(y,z)\lambda_{x,y}\lambda_{x,z}\\
 &+{4\over c_rX}
   \sum_Ga_G\sum_{x:G\in L_x}{g_x^{(t)}\over c_x}
      \sum_Aw_A^x{n_A^x(G)\choose2}.
 \end{aligned}}
\tag{3.4}
\]

#### Proof

Expand the conditional variance of
\(L_x^{\rm lin}=\sum_y\lambda_{x,y}{\bf1}_{\{y\in G\}}\). The second
moment contributes \(X^{-1}Y_{y,z\mid\bar x}\), while

\[
 \Pr_i(L_x)
 \mathbb E_i(L_x^{\rm lin}\mid L_x)^2
 ={1\over XX_x}
   \left(\sum_yY_{y\mid\bar x}\lambda_{x,y}\right)^2.
\]

This proves (3.3). From (2.5),

\[
 \operatorname {Var}(F_x\mid L_x)
 \le2\operatorname {Var}(L_x^{\rm lin}\mid L_x)
    +2\operatorname {Var}(R_x^{\ge2}\mid L_x).
\]

Bound the last variance by its conditional second moment, use (2.7),
and insert the result in (1.6). \(\square\)

## 4. Fixed-count modes vanish identically

Suppose first that the accepted-edge law is restricted to one literal
macro stratum \(\sigma\) in which every accepted edge has exactly
\(m_{T,\sigma}\) resources of each physical type \(T\). After conditioning
on \(L_x\), this count remains deterministic for every type, including
the type of \(x\): the condition says only that the particular resource
\(x\) is absent, not that one role of its type has been removed from
\(G\).

Let \(K_x^\sigma\) be the analogue of (3.2) in this stratum. For the
type-indicator vector \({\bf1}_T\),

\[
 \boxed{K_x^\sigma{\bf1}_T=0.}
\tag{4.1}
\]

Therefore, for arbitrary constants \(b_{x,T,\sigma}\),

\[
 \boxed{
 \lambda_x^*K_x^\sigma\lambda_x
 =\left(\lambda_x-
      \sum_Tb_{x,T,\sigma}{\bf1}_T\right)^*
 K_x^\sigma
 \left(\lambda_x-
      \sum_Tb_{x,T,\sigma}{\bf1}_T\right).}
\tag{4.2}
\]

#### Proof

For \(G\) in the stratum and conditioned on \(L_x\),
\(\langle{\bf1}_T,{\bf1}_G\rangle=m_{T,\sigma}\) is deterministic.
Its covariance with every incidence coordinate is zero, proving (4.1).
Equation (4.2) follows by polarization. \(\square\)

If the clock mixes finitely many macro strata (for example the two owner
multiplicities \(h=2,3\)), apply conditional variance decomposition:

\[
 \operatorname {Var}(L_x^{\rm lin}\mid L_x)
 =\mathbb E[\operatorname {Var}(L_x^{\rm lin}\mid L_x,\sigma)\mid L_x]
 +\operatorname {Var}(\mathbb E[L_x^{\rm lin}\mid L_x,\sigma]\mid L_x).
\tag{4.3}
\]

The first term has the exact projection (4.2). The second is a
finite-dimensional macro-mixture term and must remain in the already
named owner/type-mixture ledger; it is not a Johnson-sector covariance.

## 5. The sharpened remaining gate

The positive coarea PINC4 discards the negative product in (3.2) and
therefore charges fixed-count constant modes which in fact have zero
variance. The proof-safe replacement is the sum of only two terms:

1. the stratum-conditioned, type-centered covariance

   \[
   \operatorname {SCOV4}
   =\mathbb E\sum_{i<\tau}{1\over X_i}
     \sum_{x,\sigma}{1\over c_x}
       (\lambda_{x,i}^{\perp,\sigma})^*
       K_{x,i}^\sigma\lambda_{x,i}^{\perp,\sigma};
   \tag{5.1}
   \]

2. the factorial two-hit remainder in the second line of (3.4), plus the
   finite macro-mixture term in (4.3).

Here \(\lambda^{\perp,\sigma}\) denotes subtraction of arbitrary
typewise constants; the quadratic form is independent of which constants
are chosen. The second term of (3.4) has no hidden fourth-hit loss because
of (2.7). After expanding \(g_x^{(t)}/c_x\), its constant part has exactly
the FE3 first-two-hit coefficient. Its centered part is an actual-vector
incidence term and should be grouped with GDIR, not with a new positive
four-hit ledger.

Thus PINC4 is sufficient but no longer sharp. The true unclosed survivor
row is SCOV4 together with the centered part of the explicit two-hit
remainder. In particular, any attempted counterexample based on a
constant second-incidence profile is spurious: such a profile lies in the
exact nullspace (4.1).

## 6. Proof boundary

This note proves the cancellation and the factorial reduction, not the
cumulative estimate (5.1). A closure may now use either:

* a stopped covariance estimate for the type-centered second-incidence
  profile;
* complete-row blocker conjugation on that centered profile; or
* a coefficient-faithful service potential whose noise bracket is (5.1).

What is no longer needed is an uncentered positive bound on every
same-anchor or distinct-anchor pair. The fixed-count baseline vanishes
before any Johnson or rooted-overlap estimate is applied.
