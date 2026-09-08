# An elementary clock bound for a possible ten-axis improvement

Date: 2026-09-07. The moment bound below is proved. The ten-axis full
template mentioned in its application has **not** been constructed here.

## 1. A quantitative concavity bound

Let `X>=0` have finite third moment, with mean `mu>0`, variance `v>0`,
and third centered moment `kappa`. Then

\[
\boxed{\mathbb E\sqrt X\le\sqrt\mu-
 \frac{v^2}{4\sqrt\mu(2\mu v+\kappa)}.}             \tag{1}
\]

The denominator is positive because
`2 mu v+kappa=E[(X-mu)^2(X+mu)]>0`.
First,

\[
\sqrt\mu-\mathbb E\sqrt X
=\frac1{2\sqrt\mu}\mathbb E(\sqrt X-\sqrt\mu)^2.
\]

Cauchy--Schwarz applied to
`|X-mu|/(sqrt(X)+sqrt(mu))` and
`|X-mu|(sqrt(X)+sqrt(mu))` gives

\[
\mathbb E(\sqrt X-\sqrt\mu)^2\ge
\frac{v^2}{\mathbb E[(X-\mu)^2(\sqrt X+\sqrt\mu)^2]}.
\]

Since `(sqrt(X)+sqrt(mu))^2<=2(X+mu)`, the denominator on the right is
at most `2(2 mu v+kappa)`. This proves (1).

## 2. Application to the accumulator clock

Let `tau` be the exit time from the unit ball of standard three-dimensional
Brownian motion, started at the origin. The radial boundary-value equation
`u''/2+u'/r=s u`, `u(1)=1`, gives

\[
\mathbb E e^{-s\tau}=\frac{\sqrt{2s}}{\sinh\sqrt{2s}}.
\]

Indeed its bounded regular solution is
`sinh(r sqrt(2s))/(r sinh(sqrt(2s)))`; applying the stopped bounded-solution
martingale and then evaluating at zero proves the formula. Moments are
finite: at every integer time, regardless of the current point inside the
ball, a fixed positive-probability Gaussian increment of length greater
than two forces exit within the next unit of time. The Markov property
therefore gives a geometric bound on `Pr(tau>n)`.

Expanding the transform at zero yields

\[
\mathbb E\tau=\frac13,\qquad
\mathbb E\tau^2=\frac7{45},\qquad
\mathbb E\tau^3=\frac{31}{315},
\]

and hence `Var(tau)=2/45` and the third centered moment `16/945`.
For the sum `S_r` of `r` independent copies, the corresponding quantities
are `mu=r/3`, `v=2r/45`, `kappa=16r/945`. Inserting them into (1) gives

\[
\boxed{\beta_r:=\sqrt{\pi/8}\,\mathbb E\sqrt{S_r}
\le\sqrt{\frac{\pi r}{24}}
 \left(1-\frac7{20(7r+4)}\right).}                  \tag{2}
\]

This is a rigorous upper bound, not a numerical quadrature estimate or an
assertion of equality. It improves the elementary Jensen bound by a
relative term of order `1/r`.

## 3. What a forty-two-row template would imply

A full balanced prefix rectangle on ten binary coordinates consists of
all unions of a prefix of one ordered five-set and a prefix of its ordered
complement. It has six targets at rank five and five at each adjacent rank.
Therefore a covering family needs at least `binom(10,5)/6=42` rows.

If 42 such rows cover **all** 1024 binary targets, their flat charge is
`M=42(6+6)=504`. The established literal q-ary amplification and accumulator
compiler then gives the conditional implication

\[
\nu(k)\le\left(\frac{504}{2^9}\beta_{11}+o(1)\right)W(k).
\]

The compiler dependency is the theorem in
`QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md`, with
`q=2,d=10`; this note does not replace its full construction proof.
By (2),

\[
\frac{504}{512}\beta_{11}
\le \frac{63}{64}\frac{1613}{1620}\sqrt{\frac{11\pi}{24}}
<1.17635.                                           \tag{3}
\]

The last comparison has a simple rational certificate. The positive
integral `integral_0^1 x^4(1-x)^4/(1+x^2) dx=22/7-pi` proves `pi<22/7`.
All factors in (3) are positive, so squaring reduces the comparison to:

```python
from fractions import Fraction as F
upper_square = (F(63, 64)*F(1613, 1620))**2 * F(121, 84)
assert upper_square < F(117635, 100000)**2
```

Thus this finite target would strictly improve the current coefficient
`1.1807038038...`. It would still be a constant-factor improvement, not the
full coefficient-one theorem. No such 42-row cover is certified by this
moment calculation or by a fractional template.
