# An endpoint-critical finite Apéry shoulder can be negative

**Date:** 2026-08-07  
**Status:** unconditional pure mathematics.  This is an exact rational
counterexample to the proposed separate sign of the finite-availability
shoulder.  It does not contradict positivity of the complete Bellman
functional: the latter also contains the strictly positive cyclic theta
reserve.

## 1. The table

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},\qquad
 \alpha={1\over20000},\qquad n=20.
\tag{1.1}
\]

Define

\[
 v_0=0,
 \qquad
 v_j={j\over20}-\alpha j\quad(1\le j\le18),
 \qquad
 v_{19}={19\over20}-6\alpha,
 \qquad
 v_{20}=1.
\tag{1.2}
\]

Thus its endpoint costs are

\[
 e_j={j\over20}-v_j=
 \begin{cases}
  \alpha j,&1\le j\le18,\\
  6\alpha,&j=19,\\
  0,&j=20.
 \end{cases}
\tag{1.3}
\]

### Lemma 1.1 (strict endpoint-critical feasibility)

The table (1.2) is strictly increasing and internally superadditive, and

\[
 {v_j\over j}<{1\over20}={v_{20}\over20}
 \qquad(1\le j<20).
\tag{1.4}
\]

Hence \(20\) is its unique maximum-density denomination.

#### Proof

Write \(c=1/20-\alpha>0\).  The entries through \(18\) are \(v_j=cj\).
They are strictly increasing.  Moreover

\[
 v_{19}-v_{18}={1\over20}+12\alpha>0,
 \qquad
 v_{20}-v_{19}={1\over20}+6\alpha>0.
\tag{1.5}
\]

If \(i+j\le18\), internal superadditivity is equality.  If \(i+j=19\),
then

\[
 v_{19}-(v_i+v_j)=13\alpha>0.
\tag{1.6}
\]

If \(i+j=20\), the pair \(1+19\) has value \(1-7\alpha<1\), while every
pair with both indices at most \(18\) has value \(1-20\alpha<1\).
These are all cases.  Finally the densities below \(20\) are respectively
\(1/20-\alpha\) and \(1/20-6\alpha/19\), proving (1.4).  \(\square\)

## 2. Exact cyclic and physical min-plus costs

Let

\[
 \delta(m)=
 \min_{\sum_{j=1}^{20}jx_j=m}\sum_{j=1}^{20}e_jx_j
\tag{2.1}
\]

be the physical partition cost.  For \(0\le r<20\), let \(d_r\) be the
least cost of a walk using only the proper denominations \(1,\ldots,19\)
whose total capacity is congruent to \(r\pmod {20}\).

### Lemma 2.1 (one unavailable cyclic shortcut)

One has

\[
 \boxed{d_r=\alpha\min\{r,6(20-r)\}.}
\tag{2.2}
\]

Equivalently,

\[
 d_r=\alpha r\quad(0\le r\le17),
 \qquad d_{18}=12\alpha,
 \qquad d_{19}=6\alpha.
\tag{2.3}
\]

Furthermore

\[
 \boxed{
 \delta(m)=d_{m\bmod20}\quad(m\ne18),
 \qquad
 \delta(18)=18\alpha.}
\tag{2.4}
\]

#### Proof

In a proper-denomination walk, let \(k\) be the number of \(19\)-steps
and let \(t\) be the total capacity supplied by steps of sizes at most
\(18\).  Its cost is exactly

\[
 \alpha(t+6k),
\tag{2.5}
\]

and its residue is \(t-k\pmod {20}\).  Conversely every \(t\ge0\) is
available, using \(t\) copies of denomination \(1\).  If
\(t-k=r+20z\), then

\[
 t+6k=r+20z+7k.
\tag{2.6}
\]

For \(z\ge0\), this is at least \(r\).  For \(z\le-1\), writing
\(h=-z\ge1\) gives \(k-t=20h-r\), and hence

\[
 t+6k\ge6(20-r).
\tag{2.7}
\]

Both bounds are attained: use \(t=r,k=0\), or \(t=0,k=20-r\).
This proves (2.2), and the comparison \(r\le6(20-r)\) is equivalent to
\(7r\le120\), giving (2.3).

For physical capacity \(20q+r\), the direct witness \(t=r,k=0\), with
\(q\) endpoint parts, realizes \(d_r\) for every \(r\le17\).  A single
\(19\)-part realizes \(d_{19}\) in every row.  Two \(19\)-parts have total
capacity \(38\), so they realize \(d_{18}\) in every row \(q\ge1\).
At \(m=18\), however, neither a \(19\)-part nor a \(20\)-part is
available.  Every partition then uses only the linear-cost parts and has
cost \(18\alpha\).  Since every physical cost is at least its cyclic
relaxation, these witnesses prove (2.4).  \(\square\)

## 3. The shoulder is one strictly negative term

Let

\[
 L(m)={m\over20}-\delta(m),
 \qquad
 s_r={r\over20}-d_r,
 \qquad
 W(20q+r)=q+s_r.
\tag{3.1}
\]

By Lemma 2.1, \(L(m)=W(m)\) except at \(m=18\), where

\[
 L(18)={9\over10}-18\alpha={8991\over10000},
 \qquad
 W(18)={9\over10}-12\alpha={4497\over5000}.
\tag{3.2}
\]

Recall the compact branch of the Rayleigh signed-tail kernel:

\[
 \kappa(y):=K(Ay)
 =1-e^{-a(1-y)^2}-e^{-a(1+y)^2}
 \qquad(0\le y\le1).
\tag{3.3}
\]

### Lemma 3.1 (a rational interval on the increasing compact branch)

The function \(\kappa\) is strictly increasing on
\([899/1000,1]\).

#### Proof

Differentiation shows that \(\kappa'(y)>0\) exactly when

\[
 h(y):=\log{1+y\over1-y}-\pi y>0.
\tag{3.4}
\]

On the stated interval,

\[
 h'(y)={2\over1-y^2}-\pi>0,
\tag{3.5}
\]

because \(y^2>(899/1000)^2>4/11\), and hence
\(2/(1-y^2)>22/7>\pi\).  At \(x=899/1000\), the positive-term expansion

\[
 \log{1+x\over1-x}
 =2\sum_{k\ge0}{x^{2k+1}\over2k+1}
\tag{3.6}
\]

and direct rational arithmetic give

\[
 \left(2x,{2x^3\over3},{2x^5\over5},{2x^7\over7},
 {2x^9\over9},{2x^{11}\over11},{2x^{13}\over13}\right)
 >_{\rm sum}
 {1\over1000}(1798,484,234,135,85,56,38),
\tag{3.7}
\]

where \(>_{\rm sum}\) means componentwise \(\ge\), with at least one
strict inequality.  Consequently

\[
 2\sum_{k=0}^{6}{x^{2k+1}\over2k+1}
 >{283\over100}
 >{22\over7}{899\over1000}
 >\pi x.
\tag{3.8}
\]

Thus \(h(x)>0\), and (3.5) proves the claim.  \(\square\)

### Theorem 3.2 (negative endpoint-critical finite shoulder)

For the strict endpoint-critical table (1.2),

\[
 \boxed{
 \mathcal H
 :=\sum_{m\ge0}\bigl[K(AL(m))-K(AW(m))\bigr]
 <0.}
\tag{3.9}
\]

#### Proof

All summands vanish except \(m=18\).  Therefore

\[
 \mathcal H
 =\kappa\!\left({8991\over10000}\right)
  -\kappa\!\left({4497\over5000}\right).
\tag{3.10}
\]

Both arguments exceed \(899/1000\), and the second is strictly larger.
Lemma 3.1 makes (3.9) strictly negative.  \(\square\)

For orientation only, its numerical value is

\[
 \mathcal H=-5.5553955457\ldots\times10^{-6}.
\tag{3.11}
\]

## 4. Consequence for the endpoint proof architecture

The finite-availability shoulder has no universal nonnegative sign, even
under all of the following simultaneous restrictions:

1. the table is rational and strictly increasing;
2. it is internally superadditive;
3. the endpoint is the unique maximum-density denomination;
4. only one physical state differs from the formal Apéry clock.

Thus the positive cyclic theta reserve and the finite shoulder cannot be
signed separately.  Any proof of the complete endpoint-critical Bellman
inequality must spend part of the cyclic reserve against a quantitatively
controlled negative shoulder, or use a coupled identity which performs
that compensation automatically.

## 5. The complete functional in this example is rigorously positive

The counterexample is only to the separate shoulder sign.  Indeed, the
cyclic Apéry theta theorem gives the formal reserve

\[
 \mathcal R:=\sum_{m\ge0}K(AW(m))>{1\over2000}.
\tag{5.1}
\]

On the interval in (3.10), Lemma 3.1 gives \(\kappa'>0\), while (3.3)
gives the elementary global upper bound

\[
 \kappa'(y)
 <2a(1+y)e^{-a(1+y)^2}
 \le \max_{x\ge0}2ax e^{-ax^2}
 =\sqrt{{2a\over e}}<1.
\tag{5.2}
\]

The last strict inequality follows from \(2a=\pi/2<e\).  Since the two
arguments in (3.10) differ by \(6\alpha=3/10000\), the mean-value theorem
therefore yields

\[
 -{3\over10000}<\mathcal H<0.
\tag{5.3}
\]

Consequently the complete physical value satisfies the explicit strict
bound

\[
 \boxed{
 \sum_{m\ge0}K(AL(m))
 =\mathcal R+\mathcal H
 >{1\over2000}-{3\over10000}
 ={1\over5000}>0.}
\tag{5.4}
\]

Thus this exact table simultaneously disproves shoulder positivity and
passes the desired total Bellman inequality with certified room.
