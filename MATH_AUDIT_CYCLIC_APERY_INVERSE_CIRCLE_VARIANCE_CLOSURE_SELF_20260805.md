# Self-audit: inverse-circle closure of the cyclic Apéry variance gate

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md`  
**Method:** independent line-by-line algebraic replay; pure mathematics;
no computation, search, or solver  
**Verdict:** **PASS SELF-AUDIT.**  The inverse exists on the full integer
lift, is degree-one and subadditive, and its periodic defect is exactly the
complete phase discrepancy almost everywhere.  Connected-circle sumset
growth removes the finite Kneser loss and the continuous quantile argument
has the correct majorization direction.  Scaling gives the advertised
sharp coefficient `e(1)`.  The theorem closes only the complete formal
periodic variance gate, not the finite shoulder.

## 1. Normalization audit

Let `c=e(1)`.

* If `c=0`, then `e(r)<=r c=0`, so nonnegativity forces `e=0`.
* If `c>0`, `f=e/c` is nonnegative and cyclically subadditive,
  `f(1)=1`, and `f(r)<=r`.
* The normalized conclusion

  \[
  \operatorname {Var}(f)\le {\bar f(\bar f+1)\over3}
  \]

  rescales to

  \[
  \operatorname {Var}(e)
  \le {\mu(\mu+c)\over3}.
  \]

No unrecorded assumption that `c=1` in the original physical units is
used.

## 2. Integer-lift audit, including negative indices

For `n=qg+r`, `0<=r<g`, define

\[
 A(n)=n-e(r).
\]

This formula is valid for negative `q` as well.  It gives

\[
 A(n+g)=A(n)+g,
 \qquad A(n)\le n.
\]

For arbitrary integers `m,n`, the residues of `m+n` and
`bar m+bar n` agree, including the carry.  Hence

\[
 A(m+n)-A(m)-A(n)
 =e(\bar m)+e(\bar n)-e(\bar m+\bar n)\ge0.
\]

Thus superadditivity has no missing seam term.

For a nonseam step,

\[
 A(n+1)-A(n)=1+e(r)-e(r+1)\ge0.
\]

At the seam it is `1+e(g-1)`.  Therefore `A` is nondecreasing on all of
`Z`.  Since `A(n)=n+O(1)`, the generalized inverse

\[
 B(t)=\min\{n:A(n)\ge t\}
\]

is finite for every real `t`.

## 3. Generalized-inverse audit

Degree follows in both directions:

\[
 A(n)\ge t
 \iff A(n+g)\ge t+g,
\]

so `B(t+g)=B(t)+g`.

For subadditivity, the two defining inequalities

\[
 A(B(s))\ge s,
 \qquad A(B(t))\ge t
\]

and superadditivity of `A` give

\[
 A(B(s)+B(t))\ge s+t.
\]

Minimality gives `B(s+t)<=B(s)+B(t)`.  Also `A(n)<=n` implies that no
integer `n<t` can reach level `t`, hence `B(t)>=t`.

Therefore

\[
 u(t)=B(t)-t
\]

is nonnegative, `g`-periodic, and subadditive on the real lift and hence
on `R/gZ`.

## 4. Endpoint and cell audit

On `[0,g]`, put `a_r=A(r)=r-e_r`, with `e_g=e_0=0`.  Monotonicity gives

\[
 0=a_0\le\cdots\le a_g=g.
\]

If `a_r<t<a_(r+1)`, then every integer at most `r` has `A`-value below
`t`, while `A(r+1)>t`.  Thus `B(t)=r+1` and

\[
 u(t)=r+1-t.
\]

At an endpoint the left-inverse convention may choose a different branch,
but there are only finitely many endpoints.  Repeated phases create empty
open cells.  Neither affects Haar moments or sublevel-set measures after
arbitrary epsilon enlargement.

The first cell integral is

\[
 \int_{a_r}^{a_{r+1}}(r+1-t)dt
 ={(1+e_r)^2-e_{r+1}^2\over2}.
\]

The second is

\[
 \int_{a_r}^{a_{r+1}}(r+1-t)^2dt
 ={(1+e_r)^3-e_{r+1}^3\over3}.
\]

After cyclic telescoping and normalization by `g`, these give

\[
 \mathbb Eu={1\over2}+\mu,
 \qquad
 \mathbb Eu^2={1\over3}+\mu+\mathbb Ee^2,
\]

and therefore

\[
 \operatorname {Var}(u)
 ={1\over12}+\operatorname {Var}(e).
\]

The signs and the `1/12` correction are exact.

## 5. Connected-sumset audit

For `C_z={x:u(x)<=z}`, subadditivity gives

\[
 C_s+C_t\subseteq C_{s+t}.
\]

The compact connected circle has no proper closed subgroup of positive
Haar measure.  Compact-group Kneser therefore gives

\[
 m(E+F)\ge\min(1,m(E)+m(F)).
\]

The actual `C_z` are finite unions of intervals, so compact inner
approximation (or the standard measurable form) applies directly.  If
`q` is the increasing quantile of `u`, use levels `q(x)+epsilon` and
`q(y)+epsilon`; then let `epsilon` decrease to zero.  This proves

\[
 q(x+y)\le q(x)+q(y)
 \qquad(x+y\le1).
\]

The missing finite-group `-1/g` term is genuinely absent.  This is the
step that eliminates all composite-period stabilizer losses.

## 6. Quantile-majorization audit

Put `S(x)=int_0^x q`.  Integrating

\[
 q(x)\le q(y)+q(x-y)
\]

over `0<y<x` gives

\[
 xq(x)\le2S(x).
\]

Thus `S(x)/x^2` is nonincreasing.  Since `S(1)=m=Eu`,

\[
 S(x)\ge mx^2.
\]

The comparison `ell(x)=2mx` has the same total and prefix `mx^2`.
Therefore `q` is the less-spread vector and the square-moment direction is

\[
 \int q^2\le\int ell^2={4m^2\over3}.
\]

The integration-by-parts sign in the theorem confirms this directly:
`H=int_0^x(q-ell)>=0`, while `d(q+ell)>=0`, so

\[
 \int(q^2-ell^2)=-\int H\,d(q+ell)\le0.
\]

Consequently `Var(u)<=m^2/3`.

## 7. Final substitution and equality calibrations

Using `m=1/2+mu` and the variance identity,

\[
 {1\over12}+\operatorname {Var}(e)
 \le { (1/2+\mu)^2\over3}
 ={1\over12}+{\mu(\mu+1)\over3}.
\]

Cancellation proves the normalized theorem.

Two boundary checks agree exactly:

1. `e_r=0`: `A(n)=n`, `B(t)=ceil(t)`, and `u=ceil(t)-t` is the unit
   sawtooth with mean `1/2`, variance `1/12`.
2. `e_r=r` on `0<=r<g`: `A` is constant on each integer period,
   `B(t)=g` for almost every `0<t<g`, and `u(t)=g-t`; its continuous
   uniform law has variance equal to the square of its mean divided by
   three.

Both sides of the finite inequality are equal in both calibrations.

## 8. Scope audit

The theorem proves the cyclic variance gate for every finite residue
period and, with the already-proved strict Fourier coefficient estimate,
strict positivity of every **complete formal periodic** Apéry phase.

It does not make the finite availability queue periodic and proves no
finite-shoulder conductor or regeneration estimate.  No such claim is
made in the theorem.

