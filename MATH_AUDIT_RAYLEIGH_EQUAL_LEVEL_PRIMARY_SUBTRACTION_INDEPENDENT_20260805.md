# Independent audit: Rayleigh equal-level primary subtraction

**Date:** 2026-08-05  
**Method:** pure mathematical reconstruction; no computation, search, or
solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`  
**Verdict:** **GO with no theorem correction.**  The branch orientation,
pushforward measures, harmonic-mean density, workload identity, count
slack, and lifting map are valid.  The transformed pair remains unsolved.
In particular, an integrated prefix inequality for that pair would not be
equivalent to its pointwise density inequality; only the latter implies the
former without an additional monotonicity argument.

## 1. Shape of the signed-tail kernel

On `(0,A)`,

\[
 K'(t)=j(t)-s(t),
\]

and beyond `A`, `K'(t)=j(t)>0`.  The unique density crossing `c` therefore
makes `K` strictly decreasing on `(0,c)` and strictly increasing on
`(c,infinity)`.  Since

\[
 K(0)=1-2e^{-\pi/4}>0,
 \qquad K(A)=-e^{-\pi}<0,
\]

there is one zero `y_* in (0,c)`.  Thus the inverse branches in the theorem
have exactly the stated domains and orientations.

For `u in (m,0)`,

\[
 \ell'(u)=1/K'(\ell(u))<0,
 \qquad r'(u)=1/K'(r(u))>0.
\]

Hence

\[
 z'(u)=1/K'(r(u))-1/K'(\ell(u))>0.
\]

The endpoint limits are `z(m+)=0` and `z(0-)=infinity`, so `z` is indeed a
bijection from `(m,0)` to `(0,infinity)`.

## 2. Exact pushforwards

On the right branch, `du=K'(x)dx`, which is precisely the separated job
density.  On the left branch, increasing `u` moves `ell(u)` from `c` down
to `y_*`; the absolute Jacobian is `-K'(y)dy`.  Therefore

\[
 r_\#du=\mu_{\rm res},
 \qquad
 \ell_\#du=\nu_{\rm res}|_{(y_*,c)}.
\]

No orientation sign is missing.

Writing

\[
 a=K'(r)>0,\qquad b=-K'(\ell)>0,
\]

gives

\[
 {dz\over du}={1\over a}+{1\over b},
 \qquad
 {d\widetilde\mu\over dz}={ab\over a+b}.
\]

This verifies the harmonic-mean formula.

## 3. Mass and work

The transformed job mass is the length of `(m,0)`, namely `-m`.  The
unused socket mass is

\[
 \int_0^{y_*}-K'(y)dy=K(0)-K(y_*)=K_0.
\]

The original separated pair has equal first moments.  Removing the paired
occurrences `r(u)` and `ell(u)` on the same `du` base leaves exactly

\[
 \int_m^0(r(u)-\ell(u))du
 =\int_0^{y_*}y(-K'(y))dy.
\]

Thus the transformed workload ledger is exact.

For the count slack, the crossing relation gives

\[
 m=1-{2\over1+\theta}
       e^{-A^2(1-\theta)^2}.
\]

The theorem's elementary bounds imply `theta>17/20` and
`p<17/37`.  Since the exponential factor is below one,

\[
 p+{e^{-A^2(1-\theta)^2}\over1+\theta}
 <{17\over37}+{20\over37}=1,
\]

which is exactly `K_0>-m`.  The inequality directions are correct.

## 4. Lifting

Given a transformed job `w`, the inverse `u=z^{-1}(w)` is measurable and
unique.  Appending the socket `ell(u)` changes its sum to

\[
 w+\ell(u)=r(u).
\]

The appended socket marginal is the used left-branch bank; the old
transformed socket marginal is the unused initial bank.  Their sum is all
of `nu_res`, and the new job marginal is all of `mu_res`.  Adding back the
common one-piece density restores `(mu,nu)`.  Finiteness is preserved by
adding one piece.  The lifting theorem is exact.

## 5. Transformed signed-tail recurrence

Let `b=y_*`.  For `t<b`, the unused-socket tail is

\[
 \int_t^b-K'(y)dy=K(t),
\]

while the transformed-job tail is `-u(t)`.  Their signed difference is
therefore `K(t)+u(t)`.  Above `b` there are no sockets and the signed tail
is `u(t)`.  Hence

\[
 \widetilde K(t)=
 \begin{cases}
 K(t)+u(t),&t<b,\\
 u(t),&t\ge b.
 \end{cases}
\]

The endpoint values `widetilde K(0)=K_0+m` and
`widetilde K(infinity)=0` follow from `u(0)=m` and `u(infinity)=0`.
Its integral is the transformed socket work minus transformed job work,
which is zero.  Thus Proposition 2.3 is correct.

## 6. Boundary for the proposed next inequality

For `0<t<y_*`, let `u(t)=z^{-1}(t)`.  The transformed prefix difference is

\[
 D(t)=\widetilde\nu(0,t]-\widetilde\mu(0,t]
     =K_0+m-K(t)-u(t).                              \tag{5.1}
\]

Its derivative is

\[
 D'(t)=-K'(t)-{a(u(t))b(u(t))\over a(u(t))+b(u(t))}.
\tag{5.2}
\]

Thus the pointwise domination

\[
 -K'(t)\ge {ab\over a+b}                           \tag{5.3}
\]

would imply the integrated four-point inequality `D(t)>=0`.  Conversely,
`D(t)>=0` for every `t` does not by itself imply (5.3); a nonnegative
function may have a negative derivative.  Any future note should call
(5.1) the integrated prefix condition and (5.3) the stronger local
condition, rather than label them equivalent without an additional shape
theorem.

Neither condition was proved in the audited primary-subtraction source.
It is proved in the later independently audited one-well regeneration
theorem.  This chronology is scope-consistent: the primary source is an
exact reduction, while the later theorem supplies the additional
Rayleigh-specific slope bounds.
