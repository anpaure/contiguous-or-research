# Complete closure of the five-slot long-singleton gate by one `q=1,2` tangent

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the
remaining long-singleton pure lattice positive on its complete domain.  In
particular it closes the previously unresolved range
`A/8<a<A/4`.  The proof uses no numerical search or interval enumeration:
the complete first two derivative blocks are jointly convex, and one
rational tangent certificate is positive on the whole ambient rectangle.

Put

\[
 A={\sqrt\pi\over2},\qquad c={\pi\over4},\qquad
 h(x)=xe^{-cx^2}.
\tag{0.1}
\]

The long-singleton train is

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\tag{0.2}
\]

on

\[
 0<a<{A\over4},\qquad
 \max\{3a,A-2a\}<p<A-a.
\tag{0.3}
\]

The audited `q=1,2` derivative reduction introduces

\[
 r=1-{p\over A},\qquad s=r-{a\over A},
\tag{0.4}
\]

for which

\[
 0<r<{2\over5},\qquad 0<s<{r\over2},
 \qquad s\ge {4r-1\over3},
\tag{0.5}
\]

and proves

\[
 {1\over2A}{\partial\over\partial p}\mathcal P(p,a)>B(r,s),
\tag{0.6}
\]

where

\[
\begin{aligned}
 B(r,s)={}&h(2-r)-h(r)+h(2-s)-h(s)+h(2+r-2s)\\
 &+2h(3-2r)+2h(3-r-s)+2h(3-2s).
\end{aligned}
\tag{0.7}
\]

We prove that `B` is uniformly positive on the larger rectangle

\[
                  0\le r\le {2\over5},\qquad
                  0\le s\le {1\over5}.
\tag{0.8}
\]

## 1. Joint convexity

One has

\[
 h''(x)=2cx(2cx^2-3)e^{-cx^2}.
\tag{1.1}
\]

Thus `h` is concave on
`[0,sqrt(6/pi)]` and convex on
`[sqrt(6/pi),infinity)`.

On (0.8), the two negative terms satisfy

\[
 0\le r\le {2\over5},\qquad 0\le s\le {1\over5}
       <\sqrt{6/\pi},
\]

so `-h(r)` and `-h(s)` are convex.  Every argument of a positive
term in (0.7) is at least `8/5`.  Since

\[
 {8\over5}>\sqrt{6/\pi}
\]

(use `pi>3`), `h` is convex at all those arguments.  The composition of
a convex one-variable function with an affine form is convex.  Therefore:

### Lemma 1.1

The function `(r,s) -> B(r,s)` is jointly convex on (0.8).

## 2. One rational tangent certificate

Take

\[
                  r_0={12\over35},\qquad s_0={1\over7}.
\tag{2.1}
\]

The eight arguments occurring in `B`, `B_r`, and `B_s` at this point are

\[
 {58\over35},\ {12\over35},\ {13\over7},\ {1\over7},\
 {72\over35},\ {81\over35},\ {88\over35},\ {19\over7}.
\tag{2.2}
\]

The following rational bounds are an exact finite Taylor certificate.
All entries have denominator `10000`; an open interval `(l,u)` denotes
strict lower and upper numerators.

\[
\begin{array}{c|cc}
 x&10^4h(x)&10^4h'(x)\\ \hline
58/35 &(1917,1918)&(-3834,-3833)\\
12/35 &(3126,3127)&(7434,7435)\\
13/7  &(1237,1238)&(-2944,-2942)\\
1/7   &(1405,1406)&(9525,9526)\\
72/35 &(740,742)&(-2035,-2034)\\
81/35 &(344,345)&(-1105,-1104)\\
88/35 &(175,176)&(-624,-623)\\
19/7  &(83,84)&(-325,-324)
\end{array}
\tag{2.3}
\]

For completeness, these bounds require no decimal approximation.  Use

\[
 {333\over106}<\pi<{355\over113}
\tag{2.4}
\]

and, for rational `u>=0`,

\[
 S_N(u)<e^u<
 S_N(u)+{u^{N+1}\over(N+1)!}
             {1\over1-u/(N+2)},
 \qquad S_N(u)=\sum_{j=0}^N{u^j\over j!},
\tag{2.5}
\]

with `N=24`.  Every exponent `pi*x^2/4` in (2.2) is less than six, so
the last denominator in (2.5) is positive.  Apply (2.5) at the two
rational endpoints supplied by (2.4), invert, and multiply by `x` or by
`1-pi*x^2/2`.  Clearing positive denominators gives exactly (2.3).

The value bound follows immediately.  The positive terms in (0.7) have
total lower numerator

\[
 1917+1237+740+2(344)+2(175)+2(83)=5098,
\]

while the two adverse terms have total upper numerator

\[
                         3127+1406=4533.
\]

Hence

\[
              B(r_0,s_0)>{565\over10000}>{1\over20}.
\tag{2.6}
\]

Differentiating (0.7),

\[
\begin{aligned}
 B_r={}&-h'(2-r)-h'(r)+h'(2+r-2s)\\
      &-4h'(3-2r)-2h'(3-r-s),\\
 B_s={}&-h'(2-s)-h'(s)-2h'(2+r-2s)\\
      &-2h'(3-r-s)-4h'(3-2s).
\end{aligned}
\tag{2.7}
\]

Substitution of the derivative intervals in (2.3) gives, in numerator
units of `10^-4`,

\[
\begin{aligned}
 25
 &<10^4B_r(r_0,s_0)<34,\\
 26
 &<10^4B_s(r_0,s_0)<37.
\end{aligned}
\tag{2.8}
\]

For example the lower and upper numerators for the first line are

\[
 3833-7435-2035+4416+1246=25,
\]

and

\[
 3834-7434-2034+4420+1248=34;
\]

the second line is obtained from

\[
 2942-9526+4068+1246+1296=26
\]

and

\[
 2944-9525+4070+1248+1300=37.
\]

In particular,

\[
0<B_r(r_0,s_0)<{1\over100},
 \qquad
0<B_s(r_0,s_0)<{1\over100}.
\tag{2.9}
\]

## 3. Uniform positivity of the derivative block

By joint convexity, the tangent plane at `(r_0,s_0)` is a global lower
support:

\[
 B(r,s)\ge B(r_0,s_0)
 +B_r(r_0,s_0)(r-r_0)+B_s(r_0,s_0)(s-s_0).
\tag{3.1}
\]

On (0.8), `r,s>=0`.  The two tangent slopes are positive, so (2.6) and
(2.9) yield

\[
\begin{aligned}
 B(r,s)
 &>{1\over20}-{1\over100}
       \left({12\over35}+{1\over7}\right)\\
 &= {79\over1750}>0.
\end{aligned}
\tag{3.2}
\]

This proves a margin on a rectangle strictly larger than the true
parameter domain.

### Theorem 3.1

For every `(r,s)` satisfying (0.5),

\[
                         \boxed{B(r,s)>{79\over1750}.}
\tag{3.3}
\]

Consequently, throughout (0.3),

\[
             {\partial\over\partial p}\mathcal P(p,a)>0.
\tag{3.4}
\]

## 4. Closure of the long-singleton gate

For fixed `a`, the lower-period boundary in (0.3) is

\[
 p_-(a)=\max\{3a,A-2a\}.
\tag{4.1}
\]

Both pieces are already proved positive in the audited delayed-`b`
reduction:

* if `a>=A/5`, then `p_-(a)=3a` and
  `mathcal P(3a,a)=C(a)>0`;
* if `a<=A/5`, then `p_-(a)=A-2a`, the capacity-five endpoint is `A`,
  and the threshold-endpoint theorem gives positivity.

Equation (3.4) now transports that positivity through the whole open
period interval.

### Corollary 4.1

On the complete domain (0.3),

\[
                         \boxed{\mathcal P(p,a)>0.}
\tag{4.2}
\]

In particular the formerly open range `A/8<a<A/4` is closed.  Combined
with the audited delayed-`b` concavity theorem, this also closes the
retained three-pulse gate `mathcal H`.  Complete size-three-efficient
positivity then additionally requires the separate short-singleton gate.

## 5. Scope

This theorem is only the long-singleton analytic closure.  It does not
by itself prove the short-singleton repeated-gap gate, the complete
five-slot Bellman theorem, the all-grid Bellman inequality, or an
`O(1)` OR-word upper bound.
