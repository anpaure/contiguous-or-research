# The h=4 inert faces reduce to a one-dimensional compact Gaussian gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It exploits the
active-pair equation `max(x-u,y-v)=delta` to remove all shifted Gaussian
trains from the unresolved pair envelope.  What remains is one ceiling
train and an explicit compact two-point kernel difference.  The final
one-dimensional gate is not signed here.

Put

\[
A={\sqrt\pi\over2},
\qquad
F(t)=F_A(t)=\sum_{q\ge0}K(qA+t),
\qquad
C=C(A)=F(0),
\tag{0.1}
\]

and abbreviate

\[
F_q=F(A/4),
\qquad
m_0=\min\{C,F_q\},
\qquad
\eta_-=(C-F_q)_+,
\qquad
\eta_+=(F_q-C)_+.
\tag{0.2}

Thus `C-m_0=eta_-` and `F_q-m_0=eta_+`.

Consider either inert normalized endpoint face from the preceding theorem,
and write

\[
u=A-P,
\qquad v=A-z,
\qquad\delta=\tau-A.
\tag{0.3}

The exact constraints include

\[
0\le u\le A/5,
\qquad
0\le\delta\le A/4-5u/4,
\tag{0.4}
\]

\[
x-u\le\delta,
\qquad y-v\le\delta,
\qquad\max\{x-u,y-v\}=\delta,
\tag{0.5}

and

\[
v\ge A/4+3u/4,
\qquad
y\le(A-u)/2.
\tag{0.6}

The five-residue endpoint train is

\[
\mathscr B_{A+\delta}
=C(A+\delta)+F_{A+\delta}(x)+F_{A+\delta}(P)
+F_{A+\delta}(y)+F_{A+\delta}(z).
\tag{0.7}

## 1. The small-bank derivative costs less than one sixth

### Lemma 1.1

For `0<=t<=A/5`,

\[
                         F(t)\le C+{t\over6}.
\tag{1.1}

Moreover, for every `0<=x<=A/4`,

\[
                         F(x)\ge m_0.
\tag{1.2}

### Proof

Let `h(w)=w exp(-w^2)`.  Direct differentiation gives

\[
{1\over2}F'(t)
=h(A+t)-h(A-t)+\sum_{n\ge2}h(nA+t).
\tag{1.3}

For `t<=A/5`, one has `A-t>=4A/5>1/sqrt(2)`.  Hence `h` is decreasing
from `A-t` onward, so the first difference in (1.3) is nonpositive and
`h(nA+t)<=h(nA)`.  Consequently

\[
F'(t)\le L:=2\sum_{n\ge2}nA e^{-n^2A^2}.
\tag{1.4}

The exact Gaussian estimates

\[
A<8/9,
\qquad e^{-\pi}<7/160,
\qquad e^{-9\pi/4}<1/900,
\qquad e^{-7\pi/4}<1/100
\tag{1.5}

give

\[
L<{7\over45}+{1/150\over1-1/75}
={1081\over6660}<{1\over6}.
\tag{1.6}

Indeed, the first term is the `n=2` term; from `n=3` onward successive
weighted terms have ratio below `1/75`.  Integrating (1.4) from zero to
`t` proves (1.1).

Every interior critical point of `F` on `[0,A/4]` is a strict maximum.
Therefore its minimum on this interval is attained at `0` or `A/4`, which
is exactly (1.2). \(\square\)

### Corollary 1.2

The first reflected pair satisfies

\[
F_{A+\delta}(x)+F_{A+\delta}(P)
>-\eta_- -{u\over6}-\varepsilon,
\qquad \varepsilon={1\over20000}.
\tag{1.7}

### Proof

Increasing the period raises each fixed shifted train, while reflection at
`u=A-P` gives

\[
F_{A+\delta}(x)+F_{A+\delta}(P)
>F(x)-F(u)-\varepsilon.
\]

Now use `F(x)>=m_0` and `F(u)<=C+u/6`. \(\square\)

## 2. The second pair has only a compact kernel loss

For admissible `u,delta`, put

\[
v_0(u)=A/4+3u/4,
\qquad
v_1(u)=(A-u)/2,
\tag{2.1}

and define

\[
\Delta_K(u,\delta)
=\max_{v_0(u)\le w\le v_1(u)}
\left[
K(w)-K\bigl(\min\{w+\delta,v_1(u)\}\bigr)
\right].
\tag{2.2}

The interval is nonempty precisely because `u<=A/5`.  The kernel is
decreasing on `[A/4,A/2]`: writing `t=w/A`, its derivative has the sign of

\[
h(A+w)-h(A-w),
\]

and

\[
2\operatorname{arctanh}(t)<\pi t
\qquad(1/4\le t\le1/2)
\tag{2.3}

gives the required sign.

### Lemma 2.1

The second reflected pair satisfies

\[
F_{A+\delta}(y)+F_{A+\delta}(z)
>-\max\{\eta_+,\Delta_K(u,\delta)\}-\varepsilon.
\tag{2.4}

### Proof

If `z<=A/2`, both trains are positive and there is nothing to prove.
Suppose `z>A/2` and put `v=A-z`.  Then (0.6) gives

\[
v_0(u)\le v<A/2.
\]

Reflection and period monotonicity give

\[
F_{A+\delta}(y)+F_{A+\delta}(z)
>F(y)-F(v)-\varepsilon.
\tag{2.5}

If `y<A/4`, then `F(y)>=m_0`, while monotone decrease gives
`F(v)<=F_q`; the loss is at most `eta_+`.  If `A/4<=y<=v`, the same
monotone decrease makes (2.5) nonnegative before the reflection error.

It remains to take `y>v`.  Equations (0.5)--(0.6) give

\[
y\le\min\{v+\delta,v_1(u)\}.
\tag{2.6}

For `A/4<=v<y<=A/2`, the positive Gaussian tail in `F` implies

\[
F'(t)>K'(t).
\]

After integration,

\[
F(v)-F(y)<K(v)-K(y).
\tag{2.7}

Since `K` is decreasing, (2.6)--(2.7) bound the loss by
`Delta_K(u,delta)`.  This proves (2.4). \(\square\)

## 3. One-dimensional scalar gate

For `0<=delta<=A/4`, define

\[
U(\delta)={A-4\delta\over5},
\tag{3.1}

and

\[
\Xi(\delta)
=\max_{0\le u\le U(\delta)}
\left[
{u\over6}
+\max\{\eta_+,\Delta_K(u,\delta)\}
\right].
\tag{3.2}

### Theorem 3.1

Both inert h=4 faces are positive if

\[
\boxed{
C(A+\delta)
>\eta_-+\Xi(\delta)+{1\over10000}
\qquad(0\le\delta\le A/4).
}
\tag{3.3}

### Proof

Equation (0.4) is equivalent to `u<=U(delta)`.  Add the pair bounds
(1.7) and (2.4) to the ceiling train in (0.7).  The two reflection errors
sum to `1/10000`, and maximization over the only remaining physical
parameter `u` gives (3.3). \(\square\)

### Why this is smaller than the previous gate

The prior exact envelope `Gamma(delta)` minimized two complete shifted
train pairs over four coupled physical variables.  The new gate has:

1. one explicit ceiling train `C(A+delta)`;
2. two fixed quarter-shift constants `eta_-,eta_+`;
3. one compact Gaussian difference of the elementary kernel `K`;
4. one maximization over `u`, followed by the displayed one-dimensional
   variable `delta`.

All infinite shifted trains except the favorable ceiling train have been
removed.  The active-pair restriction enters through both
`y-v<=delta` in (2.6) and `u<=U(delta)` in (3.1).

## 4. Scope

Inequality (3.3) remains to be proved.  This theorem therefore does not
close the inert faces or the five-slot Bellman inequality.  It is a
strictly smaller proof-safe analytic target, with no numerical or finite
search premise.
