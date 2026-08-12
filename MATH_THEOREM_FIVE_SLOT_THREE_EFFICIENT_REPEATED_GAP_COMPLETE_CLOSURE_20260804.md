# Complete closure of the two five-slot repeated-gap trains

**Date:** 2026-08-04  
**Status:** **RETRACTED — DO NOT CITE.**  Equation (1.4) reverses the
no-interior-minimum implication.  The correct statement for
\(0\le u\le v\le A/2\) is
\[
 F_A(u)\ge\min\{C(A),F_A(v)\},
\]
not the displayed reverse inequality.  Consequently (3.7) and both
inequalities in (4.7) are unsupported, so neither repeated-gap gate is
closed by this note.  The endpoint-descent lemma and the
\(F_A<64/1000\) estimate remain valid in isolation.

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
 \qquad C(P)=F_P(0),
\tag{0.1}
\]

and

\[
 \mathcal L_3(P;u,v)=F_P(0)+F_P(u)+F_P(v).
\tag{0.2}
\]

The two gates to be closed are

\[
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta)
\tag{0.3}
\]

on

\[
 0\le a\le\beta,
 \qquad 2a+2\beta<A<2a+3\beta,
\tag{0.4}
\]

and

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\tag{0.5}
\]

on

\[
 0<a<{A\over4},
 \qquad \max\{3a,A-2a\}<p<A-a.
\tag{0.6}
\]

Their cyclic gap words are respectively `(a,beta,beta)` and
`(a,a,p-2a)`: the singleton gap is no larger than the repeated gap in
the first gate and no smaller than it in the second.

## 1. A half-period train bound

We use the already proved and audited estimates from
`MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md`

\[
 C(A)>{43\over1000},
 \qquad
 F_A(v)<{61\over1000}\quad(0\le v\le2A/5),
\tag{1.1}
\]

and

\[
 F_A(v)>{1\over25}\quad(0\le v\le A/4).
\tag{1.2}
\]

We also use the exact reflected-train estimate proved there

\[
 F_A(A-v)>-F_A(v)-\varepsilon,
 \qquad
 \varepsilon:=4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000},
\tag{1.3}
\]

and its proved critical-point property: every interior critical point of
`F_A` on `[0,A/2]` is a strict local maximum.  Consequently,

\[
 F_A(v)\ge\min\{C(A),F_A(u)\}
 \qquad(0\le u\le v\le A/2).
\tag{1.4}
\]

The only extra analytic estimate needed here is the following mild
extension of (1.1).

### Lemma 1.1

For every `0<=v<=A/2`,

\[
                         \boxed{F_A(v)<{64\over1000}.}
\tag{1.5}
\]

#### Proof

Normalize `v=At`, put `alpha=pi/4`, and let

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-\alpha(t-j)^2}.
\]

The exact half-train completion is

\[
 F_A(At)=1-\Theta(t)+e^{-\alpha t^2}
             +\sum_{j\ge2}e^{-\alpha(j-t)^2}.
\tag{1.6}
\]

Poisson summation gives `Theta(t)>=2-epsilon`.  The rational analysis in
the proof of (1.1) shows, in fact on every interval containing its unique
maximizer `t_* in (1/10,3/25)`, that

\[
 e^{-\alpha t^2}+e^{-\alpha(2-t)^2}<{211\over200}.
\tag{1.7}
\]

Thus (1.7) holds on `[0,1/2]`.

For `0<=t<=1/2`, the first term of the remaining tail is at most

\[
 e^{-25\pi/16}<{1\over125}.
\tag{1.8}
\]

Indeed `pi>157/50`, `e^4>54`, and

\[
 e^{29/32}>
 1+{29\over32}+{1\over2}\left({29\over32}\right)^2
  +{1\over6}\left({29\over32}\right)^3
 ={479909\over196608},
\]

whose product with `54` is larger than `125`.

Successive terms of this tail have ratio at most `e^{-3pi/2}<1/100`.
For the last inequality, `3pi/2>471/100`, while

\[
 e^{471/100}>54
 \left(1+{71\over100}+{1\over2}{71^2\over100^2}\right)>100.
\]

Therefore

\[
 \sum_{j\ge3}e^{-\alpha(j-t)^2}
 <{{1/125}\over1-1/100}={4\over495}<{1\over120}.
\tag{1.9}
\]

Equations (1.6)--(1.9) yield

\[
 F_A(At)<{11\over200}+{1\over120}+{1\over20000}
 ={3803\over60000}<{64\over1000}.
\]

This proves the lemma. \(\square\)

## 2. Composite-endpoint descent

The common combinatorial reason the two gates close is that each has
exactly five clock points below `A`, while its sixth point is above `A`.

### Lemma 2.1 (five-point endpoint descent)

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

For the second, the `q=0` summands of `F_E(V_i)` and `F_A(V_i)` agree.
For `q>=1`, one has `qE+V_i>=qA+V_i>=A`, so tail monotonicity again gives

\[
 K(qE+V_i)\ge K(qA+V_i).
\]

Summing proves (2.2). \(\square\)

For the clocks in (0.3) and (0.5), superadditivity follows either from
their unbounded-knapsack interpretation or directly from their exact
three-residue normal forms.

## 3. The short-singleton orientation

### Theorem 3.1

On the domain (0.4),

\[
                         \boxed{\mathcal R(a,\beta)>{9\over10000}.}
\tag{3.1}
\]

#### Proof

Put

\[
 y=a+\beta,
 \qquad p=a+2\beta=2y-a.
\]

The corresponding clock starts

\[
 V_0,\ldots,V_5=0,a,y,p,2y,3y-a.
\tag{3.2}
\]

Condition (0.4) says exactly that the first five values are below `A`
and the sixth is above `A`.  Lemma 2.1 therefore gives

\[
 \mathcal R(a,\beta)
 \ge C(A)+F_A(a)+F_A(y)+F_A(p)+F_A(2y).
\tag{3.3}
\]

Define

\[
 v=A-2y,
 \qquad u=A-p=v+a.
\tag{3.4}
\]

The domain gives

\[
 {A\over3}<y<{A\over2},
 \qquad 0\le a\le {y\over2}<{A\over4},
 \qquad 0<v<{A\over3},
 \qquad 0<u<y<{A\over2}.
\tag{3.5}
\]

The last strict inequality is equivalent to
`a<3y-A`, which is the strict right inequality in (0.4).

Reflection (1.3) gives

\[
 F_A(p)>-F_A(u)-\varepsilon,
 \qquad
 F_A(2y)>-F_A(v)-\varepsilon.
\tag{3.6}
\]

By (1.4), (1.1), and Lemma 1.1,

\[
 F_A(y)-F_A(u)>C(A)-{64\over1000}.
\tag{3.7}
\]

Also (1.2), (1.1), and (3.5) give

\[
 F_A(a)-F_A(v)>{40\over1000}-{61\over1000}.
\tag{3.8}
\]

Substitute (3.6)--(3.8) in (3.3):

\[
\begin{aligned}
 \mathcal R(a,\beta)
 &>2{43\over1000}+{40\over1000}
     -{64\over1000}-{61\over1000}
     -{2\over20000}\\
 &= {9\over10000}>0.
\end{aligned}
\]

This proves the theorem. \(\square\)

## 4. The long-singleton orientation

### Theorem 4.1

On the domain (0.6),

\[
                         \boxed{\mathcal P(p,a)>{9\over10000}.}
\tag{4.1}
\]

#### Proof

The exact clock begins

\[
 V_0,\ldots,V_5=0,a,2a,p,p+a,p+2a.
\tag{4.2}
\]

Condition (0.6) says that the first five values are below `A` and the
sixth is above `A`.  Lemma 2.1 gives

\[
 \mathcal P(p,a)
 \ge C(A)+F_A(a)+F_A(2a)+F_A(p)+F_A(p+a).
\tag{4.3}
\]

Put

\[
 u=A-p,
 \qquad v=A-p-a=u-a.
\tag{4.4}
\]

The exact domain gives

\[
 0<v<a<u<2a<{A\over2}.
\tag{4.5}
\]

Reflection yields

\[
 F_A(p)>-F_A(u)-\varepsilon,
 \qquad
 F_A(p+a)>-F_A(v)-\varepsilon.
\tag{4.6}
\]

Twice applying the no-interior-minimum inequality (1.4), then Lemma 1.1,
gives

\[
 F_A(2a)-F_A(u)>C(A)-{64\over1000},
\qquad
 F_A(a)-F_A(v)>C(A)-{64\over1000}.
\tag{4.7}
\]

Substitution in (4.3) gives

\[
\begin{aligned}
 \mathcal P(p,a)
 &>3{43\over1000}-2{64\over1000}-{2\over20000}\\
 &= {9\over10000}>0.
\end{aligned}
\]

This proves the theorem. \(\square\)

## 5. Consequence for the five-slot Bellman problem

The audited reduction
`MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md`
leaves only `mathcal R` and the retained-pulse gate `mathcal H`.  The
audited concavity reduction
`MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md`
shows that positivity of `mathcal P` implies positivity of `mathcal H`.
Theorems 3.1 and 4.1 therefore close the entire size-three-efficient
five-slot branch.

The proof is unified at the structural level: in both orientations the
sixth clock point supplies a composite endpoint, endpoint descent moves
the five residue trains to period `A`, and the two late compact points
reflect onto the early half-period bank.  No period derivative or numeric
search is required.

This note does not address the size-four-efficient inert faces, which are
the only remaining faces in the complete five-slot Bellman analysis.
