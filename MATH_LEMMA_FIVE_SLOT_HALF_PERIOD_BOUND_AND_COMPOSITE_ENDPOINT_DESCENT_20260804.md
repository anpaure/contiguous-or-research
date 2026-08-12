# A half-period train bound and composite-endpoint descent

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical lemmas.  These are the two
valid pieces isolated from the retracted repeated-gap closure attempt.
They do not sign either remaining repeated-gap gate.

Put

\[
 A={\sqrt\pi\over2}
\]

and let

\[
 K(t)=
 \begin{cases}
 1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
 -e^{-(A+t)^2},&t>A.
 \end{cases}
\]

For `P>0`, write

\[
 F_P(v)=\sum_{q\ge0}K(qP+v),
 \qquad C(P)=F_P(0).
\tag{0.1}
\]

## 1. A uniform half-period upper bound

### Lemma 1.1

For every `0<=v<=A/2`,

\[
                         \boxed{F_A(v)<{64\over1000}.}
\tag{1.1}
\]

#### Proof

Normalize `v=At`, put `alpha=pi/4`, and let

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-\alpha(t-j)^2},
 \qquad
 \varepsilon=4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000}.
\]

The exact half-train completion is

\[
 F_A(At)=1-\Theta(t)+e^{-\alpha t^2}
             +\sum_{j\ge2}e^{-\alpha(j-t)^2}.
\tag{1.2}
\]

Poisson summation gives `Theta(t)>=2-epsilon`.  Put

\[
 H(t)=e^{-\alpha t^2}+e^{-\alpha(2-t)^2}.
\]

The exact derivative analysis in
`MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md`
shows that `H` has a unique maximum `t_*` on `[0,1/2]`, with

\[
 {1\over10}<t_*<{3\over25},
\]

and its rational bounds give

\[
 H(t)\le H(t_*)
 <e^{-\pi/400}+e^{-2209\pi/2500}
 <{397\over400}+{1\over16}
 ={211\over200}.
\tag{1.3}
\]

For `0<=t<=1/2`, the first term of the remaining tail is at most

\[
 e^{-25\pi/16}<{1\over125}.
\tag{1.4}
\]

Indeed `pi>157/50`, `e^4>54`, and

\[
 e^{29/32}>
 1+{29\over32}+{1\over2}\left({29\over32}\right)^2
  +{1\over6}\left({29\over32}\right)^3
 ={479909\over196608},
\]

whose product with `54` is larger than `125`.

Successive terms have ratio at most `e^{-3pi/2}<1/100`.  For the last
inequality, `3pi/2>471/100`, while

\[
 e^{471/100}>54
 \left(1+{71\over100}+{1\over2}{71^2\over100^2}\right)>100.
\]

Therefore

\[
 \sum_{j\ge3}e^{-\alpha(j-t)^2}
 <{{1/125}\over1-1/100}={4\over495}<{1\over120}.
\tag{1.5}
\]

Equations (1.2)--(1.5) yield

\[
 F_A(At)<{11\over200}+{1\over120}+{1\over20000}
 ={3803\over60000}<{64\over1000}.
\]

This proves the lemma. \(\square\)

## 2. Composite-endpoint descent

### Lemma 2.1

Let `V` be a superadditive clock and suppose

\[
 V_0,\ldots,V_4<A<V_5=:E.
\tag{2.1}
\]

Then

\[
 \boxed{
 \sum_{m\ge0}K(V_m)
 \ge\sum_{i=0}^{4}F_E(V_i)
 \ge\sum_{i=0}^{4}F_A(V_i).
 }
\tag{2.2}
\]

#### Proof

Superadditivity gives

\[
 V_{5q+i}\ge qE+V_i
 \qquad(q\ge0,\ 0\le i<5).
\]

For `q=0` equality holds.  For `q>=1`, both sides lie above `A`, where
`K` is increasing.  Summing over `q,i` proves the first inequality.

For the second inequality, the `q=0` summands of `F_E(V_i)` and
`F_A(V_i)` agree.  For `q>=1`,

\[
 qE+V_i\ge qA+V_i\ge A,
\]

and tail monotonicity gives

\[
 K(qE+V_i)\ge K(qA+V_i).
\]

Summing proves (2.2). \(\square\)

## 3. Exact scope

For the short-singleton repeated-gap train, Lemma 2.1 gives

\[
 \mathcal R(a,\beta)
 \ge C(A)+F_A(a)+F_A(a+\beta)
       +F_A(a+2\beta)+F_A(2a+2\beta).
\]

For the long-singleton train, it gives

\[
 \mathcal P(p,a)
 \ge C(A)+F_A(a)+F_A(2a)+F_A(p)+F_A(p+a).
\]

These lower bounds are valid and useful, but the no-interior-minimum
property of `F_A` does not order either endpoint difference in the
direction needed to sign these expressions.  No positivity conclusion
for `mathcal R` or `mathcal P` is claimed here.
