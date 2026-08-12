# Audit: four-slot Apéry normal form and threshold-face positivity

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_20260804.md`  
**Verdict:** **PASS** for every asserted theorem.  The boundary inequality
`J(alpha)>0` is explicitly a remaining gate and is not counted as proved.
The audited theorem now states the inherited first-crossing hypothesis
`T>=A` and the nonnegative-table convention explicitly, and defines
`C(alpha)` at its scalar-gate use.

## 1. Reduced-walk census

The simple paths in `Z/4Z`, recorded by counts of steps `1,2,3`, are

\[
\begin{array}{c|l}
1&(1,0,0),(0,1,1),(1,2,0),(0,0,3)\\
2&(0,1,0),(2,0,0),(0,0,2),(1,1,1)\\
3&(0,0,1),(1,1,0),(3,0,0),(0,2,1).
\end{array}
\]

The inequalities

\[
 d_2\ge2d_1,quad d_3\ge d_1+d_2,quad
 d_1+d_3\le0,quad d_2\le0
\]

remove exactly the dominated entries claimed in the theorem.  This gives

\[
 \beta_1=\max(d_1,d_2+d_3,3d_3),quad
 \beta_2=\max(d_2,2d_3),quad
 \beta_3=d_3.
\]

No simple path is missing.

## 2. Finite-capacity replay

Direct partitioning gives

\[
\begin{array}{c|ccccc}
m&5&6&7&8&9\\ \hline
V_m&T+\max(x,y+z-T)&T+\max(y,2z-T)&T+z&2T&2T+s_1.
\end{array}
\]

The witness `3+3+3` first becomes available at capacity nine; this is why
the correction `K(T+b_1)-K(T+s_1)` is necessary.  The functional formula
contains it with the correct sign.  Residue two stabilizes at capacity
six, and residue three has no transient.

## 3. Exact rational exponential certificate

Use

\[
                         {333\over106}<\pi<{355\over113}.
\]

For rational `r>0`, every displayed exponential comparison was checked by
one of the following exact implications:

* to prove `e^{-c pi}<r`, use
  `sum_(j=0)^N (c(333/106))^j/j! > 1/r`;
* to prove `e^{-c pi}>r`, use the upper remainder

\[
 \sum_{j=0}^N{x^j\over j!}
 +{x^{N+1}\over(N+1)!}\,{1\over1-x/(N+2)},
 \qquad x=c{355\over113},                           \tag{3.1}
\]

and check that it is `<1/r`.

The following degrees suffice; all comparisons are between integers
after cross-multiplication.

\[
\begin{array}{c|c|c|c}
\text{claim}&c&r&N\\ \hline
e^{-\pi}<7/160&1&7/160&8\\
e^{-\pi}>1/24&1&1/24&4\\
e^{-9\pi/64}<129/200&9/64&129/200&3\\
e^{-25\pi/64}<47/160&25/64&47/160&5\\
e^{-81\pi/64}<19/1000&81/64&19/1000&9\\
e^{-9\pi/64}>641/1000&9/64&641/1000&1\\
e^{-25\pi/64}>7/24&25/64&7/24&2\\
e^{-81\pi/64}>37/2000&81/64&37/2000&6.
\end{array}                                                     \tag{3.2}
\]

For the two tail estimates, the first-term bounds

\[
 e^{-9\pi/4}<1/900,qquad e^{-169\pi/64}<1/3000
\]

use degrees nine and ten.  The respective successive ratios are below
`1/100`, using `e^{-7pi/4}<1/100` and
`e^{-15pi/8}<1/100`.  Therefore the tails are below `1/800` and
`1/1000`, respectively.

These checks give, exactly,

\[
 C(A)>{57\over1400}>{1\over25},qquad
 {1\over25}<F(A/4)<{1\over20}.
\]

## 4. Monotonicity interval replay

With `h(t)=t exp(-(pi/4)t^2)`, on the first half interval one has

\[
 h(5/8)>9/20,qquad
 h(5/4)+h(9/4)+{2\over\pi}e^{-81\pi/64}
 <{449719\over1065600}<{17\over40}.
\]

On the second half interval,

\[
 h(1/2)>2/5,qquad
 h(11/8)+h(19/8)+{2\over\pi}e^{-361\pi/256}
 <{619739\over1776000}<{7\over20}.
\]

Here the additional exact bounds are

\[
 e^{-25\pi/256}>18/25,quad e^{-\pi/16}>4/5,quad
 e^{-121\pi/256}<91/400,quad
 e^{-361\pi/256}<3/250,quad {2\over\pi}<{212\over333}.
\]

Thus `F` really is decreasing on `[A/4,A/2]`; the reflection estimate is
then in the direction used by the theorem.

## 5. Final margin

At `T=A`, both compact transient corrections are nonnegative.  The five
retained contributions have the strict lower bounds

\[
 {1\over25},quad {1\over25},quad 0,quad
 -{1001\over20000},quad -{101\over4000}.
\]

Their sum is

\[
                         {94\over20000}={47\over10000}>0.
\]

This checks the arithmetic of the claimed threshold-face margin.

## 6. Scope

The audit does not promote the final ceiling bridge

\[
 C(\alpha)+K(4\alpha)-K(5\alpha)>0,
 \qquad A/4\le\alpha\le A/3.
\]

That is the sole unproved row left by this note inside the
four-slot-efficient branch.  The three-efficient branch and the all-slot
Bellman inequality remain separate.
