# Second independent audit: five-slot endpoint-efficient threshold closure

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_FIVE_SLOT_ENDPOINT_EFFICIENT_THRESHOLD_CLOSURE_20260804.md`  
**Audited source SHA-256:**
`db22119a59eae766e51c9461111f207342280309a3144fe43d0caf214c704027`  
**Method:** independent symbolic replay of the endpoint normalization,
train derivative, concavity argument, rational exponential substitutions,
Gaussian tail bounds, and literal endpoint-period comparison.  No search,
solver, or numerical sign test was used.  
**Verdict:** **PASS; no source repair required.**

## 1. Least-maximizer normalization

After first-crossing deletion and endpoint saturation,

\[
 c_5'=\max\{A,P_5\}.
\]

If `c_5'>A`, then `c_5'=P_5`.  An attaining lower-denomination
partition writes

\[
 {c_5'\over5}
 =\sum_i{j_i\over5}{c_{j_i}\over j_i}.
\]

Some `j_i<5` therefore has density at least `c_5'/5`.  Under assignment
to the least maximum-density index, such a table belongs to a branch below
five.  Hence a genuine `h=5` table has exactly

\[
                         c_5=A.
\]

This is a branch assignment, not an invalid deletion of an inert endpoint
from first-crossing form.

## 2. Train identity and derivative

With `a=pi/4`, `E(x)=exp(-a*x^2)`, and `v=At`, the compact `q=0` term
and the Gaussian tail give exactly

\[
 F_A(At)=1-E(1-t)-\sum_{n\ge0}E(1+t+n).
\]

For `h(x)=xE(x)`, termwise differentiation is justified by uniform
Gaussian convergence and gives

\[
 {d\over dt}F_A(At)
 =2a\left(\sum_{n\ge0}h(1+t+n)-h(1-t)\right).
\]

There is no missing boundary term: at `t=1` the compact and tail branches
of `K` have the same value and first derivative.

## 3. Decrease on `[A/2,4A/5]`

Put `u=1-t`, so `1/5<=u<=1/2`.  Since the sampled tail starts at
`2-u>=3/2` and `h` decreases there,

\[
 \sum_{n\ge0}h(2-u+n)
 \le h(2-u)+h(3-u)
    +{e^{-a(3-u)^2}\over2a}.
\]

Thus it suffices to prove positivity of

\[
 J(u)=h(u)-h(2-u)-h(3-u)
      -{e^{-a(3-u)^2}\over2a}.
\]

Direct differentiation gives

\[
 J''(u)=h''(u)-h''(2-u)-h''(3-u)+h'(3-u),
\]

where

\[
 h''(x)=2ax(2ax^2-3)e^{-ax^2}.
\]

On `1/5<=u<=1/2`, `h''(u)<0`, both
`h''(2-u)` and `h''(3-u)` are positive, and `h'(3-u)<0`.
Therefore `J''(u)<0`.  A concave function has its minimum at an endpoint.

The endpoint substitutions are exactly

\[
\begin{aligned}
J(1/5)={}&{1\over5}e^{-\pi/100}
-{9\over5}e^{-81\pi/100}
-\left({14\over5}+{2\over\pi}\right)e^{-49\pi/25},\\
J(1/2)={}&{1\over2}e^{-\pi/16}
-{3\over2}e^{-9\pi/16}
-\left({5\over2}+{2\over\pi}\right)e^{-25\pi/16}.
\end{aligned}
\]

For `x>=0`, Taylor's remainder gives

\[
 Q_9(x)<e^{-x}<{1\over P_8(x)}
\]

at positive `x`.  Using `157/50<pi<22/7`, every occurrence of `Q_9`
in `J_L,J_R` bounds a positive term downward, every reciprocal `P_8`
bounds a subtracted exponential upward, and `100/157` bounds the adverse
coefficient `2/pi` upward.  The four exponent substitutions are

\[
 {\pi\over100}<{11\over350},\quad
 {81\pi\over100}>{12717\over5000},\quad
 {49\pi\over25}>{7693\over1250},
\]

and

\[
 {\pi\over16}<{11\over56},\quad
 {9\pi\over16}>{1413\over800},\quad
 {25\pi\over16}>{157\over32}.
\]

Expanding the finite rational polynomials and clearing their positive
denominators verifies

\[
 J(1/5)>J_L>{1\over25},
 \qquad
 J(1/2)>J_R>{1\over10}.
\]

Hence `J>0`, the derivative of `F_A(At)` is negative, and `F_A` is
strictly decreasing on `[A/2,4A/5]`.

## 4. Endpoint bounds and exact tail origins

For `z>0`, monotonicity of the Gaussian gives

\[
 \sum_{m\ge0}E(z+m)
 \le E(z)+\int_z^\infty E(x)\,dx
 \le E(z)\left(1+{1\over2az}\right).
\]

At `t=3/5`, the terms before the residual tail have arguments

\[
 2/5,\quad8/5,\quad13/5,
\]

and the residual tail begins at `18/5`.  Therefore

\[
\begin{aligned}
F_A(3A/5)\ge{}&1-e^{-\pi/25}-e^{-16\pi/25}
-e^{-169\pi/100}\\
&-\left(1+{5\over9\pi}\right)e^{-81\pi/25}.
\end{aligned}
\]

The exponent and coefficient replacements in `B_3` are respectively

\[
 {157\over1250},\ {1256\over625},\ {26533\over5000},\
 {12717\over1250},\quad 1+{250\over1413},
\]

all in the sign-safe direction.  Exact rational clearing gives

\[
                         F_A(3A/5)>B_3>-{1\over40}.
\]

At `t=4/5`, the corresponding arguments are

\[
 1/5,\quad9/5,\quad14/5,
\]

and the residual tail begins at `19/5`.  This gives

\[
\begin{aligned}
F_A(4A/5)\ge{}&1-e^{-\pi/100}-e^{-81\pi/100}
-e^{-49\pi/25}\\
&-\left(1+{10\over19\pi}\right)e^{-361\pi/100}.
\end{aligned}
\]

The `B_4` substitutions

\[
 {157\over5000},\ {12717\over5000},\ {7693\over1250},\
 {56677\over5000},\quad1+{500\over2983}
\]

again all point downward.  Exact rational clearing gives

\[
                         F_A(4A/5)>B_4>-{21\over400}.
\]

Together with positivity on `[0,A/2]` and strict decrease afterward,
these prove the two advertised uniform train bounds.

## 5. Literal endpoint-period margin

For a genuine endpoint-efficient table, maximum density and `c_5=A`
give

\[
                         0\le c_i\le{iA\over5}
 \qquad(1\le i\le4).
\]

For capacity `5q+r`, concatenate `q` literal endpoint generators with the
size-`r` generator.  Then

\[
 V_{5q+r}\ge qA+c_r.
\]

At `q=0`, internal superadditivity gives equality.  At `q>=1`, both sides
lie in the increasing tail of `K`.  Hence

\[
 \Phi\ge C(A)+\sum_{r=1}^{4}F_A(c_r).
\]

Applying the bounds at `A/5,2A/5,3A/5,4A/5` gives, term for term,

\[
 \Phi>{1\over25}+{1\over25}+0-{1\over40}-{21\over400}
 ={1\over400}>0.
\]

This comparison uses the actual Bellman clock and therefore does not omit
any finite availability correction from the sixteen endpoint Apéry paths.

## 6. Audit scope

The source theorem is correct as written.  It closes exactly the genuine
least-maximizer `h=5` branch after saturation.  It makes no assertion about
the size-three or size-four branches, a general all-slot Bellman theorem,
or an OR-word upper bound.
