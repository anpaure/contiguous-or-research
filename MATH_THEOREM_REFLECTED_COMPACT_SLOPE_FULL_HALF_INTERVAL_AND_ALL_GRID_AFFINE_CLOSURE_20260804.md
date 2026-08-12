# Full reflected compact-slope inequality and all-grid affine closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It extends the
reflected compact-slope inequality from `u<=1/3` to every `u<1/2` and uses
the extension to prove the complete affine setup-cost family positive in
every grid size.  It does not prove positivity of arbitrary Bellman tables
or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},
 \qquad c={\pi\over4},
 \qquad h(x)=xe^{-cx^2},
\tag{0.1}
\]

and let `K` be the Rayleigh signed-tail kernel.  On the compact branch,

\[
                         K'(Au)=2A D(u),
 \qquad
 D(u)=h(1+u)-h(1-u).
\tag{0.2}
\]

## 1. The missing reflected half interval

### Theorem 1.1

For every

\[
                         0\le u<{1\over2},
\]

one has

\[
 \boxed{
 D(1-u)>D(u),
 \qquad
 K'(A(1-u))>K'(Au).}
\tag{1.1}
\]

The equality at `u=1/2` is exact.  Thus `1/2` is the first and only
crossing on the closed half interval.

#### Proof

The authenticated reflected-slope theorem proves (1.1) on
`0<=u<=1/3`.  It remains to take

\[
                         {1\over3}<u<{1\over2},
 \qquad \delta=1-2u>0.
\tag{1.2}
\]

Use the exact decomposition from that theorem:

\[
 S(u)=-R(u)+T(u),
 \qquad
 R(u)=D(1-u)-D(u),
\tag{1.3}
\]

where

\[
 S(u)=\sum_{n\in\mathbb Z}(n+u)e^{-\pi(n+u)^2/4}
 =16\sum_{m\ge1}m e^{-4\pi m^2}\sin(2\pi mu),
\tag{1.4}
\]

and

\[
 T(u)=\sum_{k\ge2}\bigl(h(k+u)-h(k+1-u)\bigr).
\tag{1.5}
\]

Every summand in (1.5) is positive because `h` decreases on
`[2,infinity)`.  In the first one, the integration interval

\[
                         [2+u,3-u]
\]

has length `delta` and lies in `[7/3,8/3]`.  On this interval `h''>0`, so
`-h'` decreases.  Therefore

\[
                         T(u)\ge-\delta h'(8/3).
\tag{1.6}
\]

The endpoint derivative is

\[
 -h'(8/3)
 =e^{-16\pi/9}\left({32\pi\over9}-1\right)>{1\over40}.
\tag{1.7}
\]

Here is a rational proof.  The bounds `3<pi<22/7` give

\[
 {32\pi\over9}-1>{29\over3},
 \qquad
 {16\pi\over9}<{352\over63}<{28\over5}.
\]

The elementary estimates

\[
 e<{11\over4},
 \qquad e^{1/5}<{5\over4}
\]

give

\[
 e^{28/5}=e^5e^{3/5}
 <\left({11\over4}\right)^5\left({5\over4}\right)^3
 <{1160\over3}.
\]

Thus `e^(-16pi/9)>3/1160`, and (1.7) follows because
`(29/3)(3/1160)=1/40`.  The estimate `e<11/4` follows, for example, by
bounding the exponential tail from degree four geometrically; the second
estimate follows termwise from `e^x<1/(1-x)` for `0<x<1`.

It remains to bound the theta correction in units of `delta`.  Since

\[
 \sin(2\pi mu)=(-1)^{m+1}\sin(\pi m\delta),
\]

one has

\[
 |S(u)|\le16\pi\delta
          \sum_{m\ge1}m^2e^{-4\pi m^2}.
\tag{1.8}
\]

The positive Taylor sum gives `e>8/3`, whence

\[
 e^{12}>\left({8\over3}\right)^{12}>100000.
\]

Put `r=e^(-12)<1/100000`.  Since `pi>3`,

\[
 \sum_{m\ge1}m^2e^{-4\pi m^2}
 <\sum_{m\ge1}m^2r^m
 ={r(1+r)\over(1-r)^3}
 <{1\over90000}.
\tag{1.9}
\]

Using `16pi<352/7<51`, equations (1.8)--(1.9) give

\[
                         |S(u)|<{\delta\over1000}.
\tag{1.10}
\]

Finally, (1.3), (1.6), (1.7), and (1.10) imply

\[
 R(u)=T(u)-S(u)
 >\delta\left({1\over40}-{1\over1000}\right)>0.
\]

This proves (1.1) on the missing interval.  At `u=1/2`, the two arguments
coincide, so equality is literal. \(\square\)

## 2. The arbitrary-grid affine clock

Fix an integer `n>=3` and put

\[
                         h=n-1.
\]

For

\[
                         0<\beta<{A\over n-2},
\]

the affine setup-cost family is

\[
 c_j=\alpha j-\beta\quad(1\le j<n),
 \qquad c_n=A,
 \qquad \alpha={A+2\beta\over n}.
\tag{2.1}
\]

Its exact Bellman clock is

\[
                         V_m=\alpha m-\beta
                                  \left\lceil{m\over h}\right\rceil.
\tag{2.2}
\]

Put

\[
 x=c_1,
 \qquad t={x\over A},
 \qquad a={\alpha\over A},
 \qquad p={c_h\over A}.
\tag{2.3}
\]

Solving the endpoint and first-gap equations gives

\[
 a={1-2t\over h-1},
 \qquad p=1-t,
 \qquad 0<t<{1\over h+1}={1\over n}.
\tag{2.4}
\]

For `m=qh+r`, `0<=r<h`, the exact normalized clock is

\[
 {V_{qh+r}\over A}=qp+s_r,
\tag{2.5}
\]

where

\[
 s_0=0,
 \qquad
 s_r=t+(r-1)a\quad(1\le r<h).
\tag{2.6}
\]

Thus one period has cyclic gaps

\[
                         (t,a,a,\ldots,a).
\tag{2.7}
\]

## 3. Complete derivative pairing

Let

\[
 \Phi_n(t)=\sum_{q\ge0}\sum_{r=0}^{h-1}
               K\bigl(A(qp+s_r)\bigr).
\tag{3.1}
\]

Termwise differentiation is justified uniformly on every closed
subinterval of `0<t<=1/n` by a Gaussian summable majorant.  The normalized
slopes are

\[
 {d\over dt}(qp+s_0)=-q,
\]

and, writing `j=r-1`,

\[
 {d\over dt}(qp+s_r)
 =-q+\ell_j,
 \qquad
 \ell_j=1-{2j\over h-1}
 \quad(0\le j\le h-2).
\tag{3.2}
\]

The derivative terms partition exactly as follows.

1. The compact term at shift `t`, whose slope is one, pairs with the
   first-period bare term at `p=1-t`, whose slope is minus one.  Theorem
   1.1 makes this pair strictly negative.
2. For every `1<=j<h-1-j<=h-2`, the two compact shifts

   \[
    u=t+ja,
    \qquad
    1-u=t+(h-1-j)a
   \]

   have opposite slopes `ell_j` and `-ell_j`, with `ell_j>0` and
   `u<1/2`.  Theorem 1.1 makes every such pair strictly negative.
3. When `h-1` is even, the central compact shift is `1/2` and has slope
   zero.  The bare zero term is stationary as well.  The first-period
   shift `p+t=1` also has slope zero.
4. Every unpaired first-period shifted term has argument

   \[
                         p+s_r=1+(r-1)a>1
   \]

   and slope `-2(r-1)/(h-1)<0` for `r>=2`.
5. Every term with `q>=2` has argument greater than one and strictly
   negative slope.

On the Gaussian tail `K'>0`.  Hence every nonstationary contribution is
strictly negative, and

\[
                         \boxed{\Phi_n'(t)<0
                         \quad(0<t\le1/n).}
\tag{3.3}
\]

## 4. Uniform endpoint and conclusion

At `t=1/n`, equation (2.4) gives

\[
                         a={1\over n},
 \qquad p={n-1\over n},
 \qquad s_r={r\over n}.
\]

As `(q,r)` ranges over `q>=0`, `0<=r<n-1`, the integer
`q(n-1)+r` ranges over every nonnegative integer exactly once.  Therefore

\[
                         \Phi_n(1/n)=C(A/n)>0
\tag{4.1}
\]

by strict reciprocal-ceiling positivity.  Since `Phi_n` decreases with
`t`,

\[
                         \boxed{\Phi_n(t)>\Phi_n(1/n)>0
                         \quad(0<t<1/n).}
\tag{4.2}
\]

### Corollary 4.1

Every member of the affine setup-cost no-descent family is strictly
positive for every grid size `n>=3`.  The balanced point is not special;
the full allowed `beta` interval is closed.

This conclusion concerns only the one-parameter affine family.  It does
not close any complete efficiency branch for arbitrary Bellman tables,
the all-grid Bellman inequality, or `nu(k)<=B(k)+O(1)`.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| previous reflected-slope interval `u<=1/3` and its Poisson decomposition | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_20260804.md` | `6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7` |
| exact affine setup-cost clock | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| strict reciprocal-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
