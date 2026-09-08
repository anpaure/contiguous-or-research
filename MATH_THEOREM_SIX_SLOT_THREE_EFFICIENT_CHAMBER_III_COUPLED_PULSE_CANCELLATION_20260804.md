# Six-slot `h=3`, chamber III: the two adverse pulses cancel jointly

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves that the
sum of the two adverse finite comparisons in chamber III is nonnegative.
Consequently the whole chamber reduces to one pulse-free prethreshold
repeated-gap train.  It does **not** sign that residual train, close the
other two `h=3` chambers, prove complete six-slot positivity, or make an
all-grid assertion.

Put

\[
                         A={\sqrt\pi\over2},
\]

and let

\[
 K(x)=
 \begin{cases}
  1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
  -e^{-(A+x)^2},&x>A
 \end{cases}
\tag{0.1}
\]

be the Rayleigh signed-tail kernel.  For `P>0`, write

\[
 \mathcal L_3(P;u,v)
 =\sum_{q\ge0}\{K(qP)+K(qP+u)+K(qP+v)\}.
\tag{0.2}
\]

The authenticated chamber-III gate is

\[
\begin{aligned}
 \mathcal G_{\rm III}(p,a,b)={}&
 \mathcal L_3(p;2b-p,b)\\
 &+K(p+a)-K(2b)\\
 &+K(2p+a)-K(p+2b),
\end{aligned}
\tag{0.3}
\]

on

\[
 {A\over2}\le p<A,
 \qquad 0\le a\le {p\over3},
 \qquad {p+a\over2}\le b\le {2p\over3},
 \qquad b<A-p.
\tag{0.4}
\]

## 1. Repeated-gap coordinates

Set

\[
                         c=2b-p,
 \qquad \beta=p-b={p-c\over2}.
\tag{1.1}
\]

Then

\[
 p=c+2\beta,
 \qquad b=c+\beta,
\tag{1.2}
\]

and (0.4) gives

\[
 0\le a\le c\le {p\over3},
 \qquad 2c+3\beta=p+b<A.
\tag{1.3}
\]

In particular,

\[
                         {A\over2}\le p<{2A\over3},
 \qquad c<2A-3p.
\tag{1.4}
\]

The three-coset train in (0.3) has cyclic gaps exactly

\[
                         (c,\beta,\beta).
\tag{1.5}
\]

Both finite comparisons have the same displacement `c-a`.  Indeed,

\[
 2b=p+c,
 \qquad p+2b=2p+c,
\]

so their sum is

\[
 \{K(p+a)+K(2p+a)\}
 -\{K(p+c)+K(2p+c)\}.
\tag{1.6}
\]

The point of the theorem is that (1.6) must be priced as one object; its
two summands separately have opposite compact/tail behavior.

## 2. A compact-plus-tail slope inequality

Define

\[
                         h(s)=s e^{-\pi s^2/4}.
\tag{2.1}
\]

### Lemma 2.1

For every

\[
                         {1\over5}\le r\le {1\over2},
\]

one has

\[
                         \boxed{h(r)>h(2-r)+h(5/2-r).}
\tag{2.2}
\]

#### Proof

Put

\[
                         f(r)=h(r)-h(2-r)-h(5/2-r).
\tag{2.3}
\]

Direct differentiation gives

\[
 h''(s)={\pi\over2}s
        \left({\pi s^2\over2}-3\right)e^{-\pi s^2/4}.
\tag{2.4}
\]

On `1/5<=r<=1/2`, one has `h''(r)<0`.  The other two arguments
are at least `3/2`; since `pi>3>8/3`, they are larger than
`sqrt(6/pi)` and their second derivatives are positive.  Hence

\[
                         f''(r)<0.
\tag{2.5}
\]

Thus the minimum of `f` on this interval is attained at an endpoint.
We certify both endpoints using only positive exponential series.

At `r=1/2`, multiplication by `2e^(pi/16)` gives

\[
 2e^{\pi/16}f(1/2)
 =1-3e^{-\pi/2}-4e^{-15\pi/16}.
\tag{2.6}
\]

The inequalities `pi>3` and

\[
 \sum_{j=0}^{5}{(3/2)^j\over j!}
 ={17133\over3840}>{40\over9}
\]

give `e^(pi/2)>40/9`.  Also

\[
 e^2>{331\over45},
 \qquad
 e^{13/16}>1+{13\over16}+{169\over512}
                   +{2197\over24576}
 ={54853\over24576},
\]

and the product of the two displayed rational lower bounds is greater
than `16`.  Therefore `e^(15pi/16)>e^(45/16)>16`.  It follows that

\[
 3e^{-\pi/2}+4e^{-15\pi/16}
 <{27\over40}+{1\over4}={37\over40}<1.
\tag{2.7}
\]

Hence `f(1/2)>0`.

At `r=1/5`, multiplication by `5e^(pi/100)` gives

\[
 5e^{\pi/100}f(1/5)
 =1-9e^{-4\pi/5}-{23\over2}e^{-21\pi/16}.
\tag{2.8}
\]

Use the classical lower bound `pi>157/50`.  The positive series give

\[
 e^{4\pi/5}>e^{314/125}
 =e^2e^{64/125}
 >{331\over45}{25673\over15625}>12.
\tag{2.9}
\]

Likewise `pi>3`, together with

\[
 e^3>\sum_{j=0}^{8}{3^j\over j!}
 ={806769\over40320}>20
\]

and

\[
 e^{15/16}>1+{15\over16}+{225\over512}
                    +{3375\over24576}
 ={61791\over24576}>{12\over5},
\]

gives

\[
                         e^{21\pi/16}>e^{63/16}>48.
\tag{2.10}
\]

Consequently

\[
 9e^{-4\pi/5}+{23\over2}e^{-21\pi/16}
 <{3\over4}+{23\over96}={95\over96}<1.
\tag{2.11}
\]

Thus `f(1/5)>0`.  Strict concavity and the two endpoint inequalities
prove (2.2). \(\square\)

### Lemma 2.2 (coupled pulse monotonicity)

Under (1.3)--(1.4), the function

\[
                         Q(z)=K(p+z)+K(2p+z)
\tag{2.12}
\]

is strictly decreasing for `0<=z<=c`.

#### Proof

Normalize

\[
                         t={p\over A},
 \qquad \zeta={z\over A},
 \qquad r=1-t-\zeta.
\tag{2.13}
\]

The domain gives

\[
 {1\over2}\le t<{2\over3},
 \qquad
 0\le\zeta\le\min\{t/3,2-3t\}.
\tag{2.14}
\]

Therefore

\[
 r\ge\max\{1-4t/3,2t-1\}\ge{1\over5},
 \qquad r\le1-t\le{1\over2}.
\tag{2.15}
\]

The last lower bound is sharp at `t=3/5`, where the two affine lower
bounds meet.

The compact and tail derivative formulas from (0.1) give

\[
 {Q'(z)\over2A}
 =h(2-r)-h(r)+h(2+t-r).
\tag{2.16}
\]

Since `2+t-r>=2` and `h` is strictly decreasing on `[2,infinity)`,
while `t>=1/2`,

\[
 h(2+t-r)\le h(5/2-r).
\tag{2.17}
\]

Lemma 2.1 now gives `Q'(z)<0`. \(\square\)

## 3. Complete cancellation and the residual gate

### Theorem 3.1

On the full chamber-III domain (0.4),

\[
\boxed{
 \mathcal G_{\rm III}(p,a,b)
 \ge \mathcal L_3(p;2b-p,b).
}
\tag{3.1}
\]

Equivalently, in the coordinates (1.1),

\[
\boxed{
 \mathcal G_{\rm III}(c+2\beta,a,c+\beta)
 \ge \mathcal L_3(c+2\beta;c,c+\beta).
}
\tag{3.2}
\]

The inequality is strict unless `a=c`.

#### Proof

By (1.6), the sum of the two finite comparisons is `Q(a)-Q(c)`.
Since `0<=a<=c`, Lemma 2.2 gives

\[
                         Q(a)-Q(c)\ge0,
\tag{3.3}
\]

with equality exactly when `a=c`.  Substitute (3.3) into (0.3).
\(\square\)

### Corollary 3.2 (smallest residual from this pricing)

It is sufficient to prove

\[
\boxed{
 \mathcal R_{<}(c,\beta)
 :=\mathcal L_3(c+2\beta;c,c+\beta)>0
}
\tag{3.4}
\]

on

\[
 c\ge0,
 \qquad c\le\beta,
 \qquad {A\over2}\le c+2\beta,
 \qquad 2c+3\beta<A.
\tag{3.5}
\]

This is a pulse-free repeated-gap train with gaps `(c,beta,beta)`.  The
last inequality in (3.5) is the **prethreshold** orientation: it is the
opposite of the already-closed short-singleton gate
`A<2c+3beta`.  No positivity theorem for (3.4)--(3.5) is asserted here.

Thus chamber III has no independent finite-pulse obstruction.  Its only
remaining scalar obstruction is the prethreshold repeated-gap train
(3.4).

## 4. Frozen dependency and scope

| role | file | SHA-256 |
|---|---|---|
| exact chamber-III gate and domain | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_20260804.md` | `a3a79b92148b1b4b415c7795473b70f50bd6d0b84f20f6899a3275f62af9b0dd` |

The kernel formula, derivative calculation, concavity argument, and
rational endpoint certificates are included in this note.  No numerical
search, remote computation, or external analytic theorem is used beyond
the displayed classical rational bounds for `pi`.

This theorem does not sign (3.4), does not close chambers I or II, does
not prove the complete six-slot Bellman inequality, and does not
generalize to arbitrary slot number.
