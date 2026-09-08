# Rayleigh ceiling-price domination and a finite MIR-cone no-go

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.

For the Gaussian job/socket measures arising from chain-dependent SCD
fragmentation, every ceiling price

\[
f_a(x)=\left\lceil{x\over a}\right\rceil ,\qquad a>0,
\]

passes the corresponding continuum job--socket inequality, strictly.  In
the primitive physical range described below, this proves that no pure
minimum-number-of-pieces (MIR) price separates the Rayleigh limit.  However,
increasing concave prices together with all ceiling rays do **not** generate
the finite nondecreasing-subadditive covering-price cone: a five-capacity
counterexample and an exact separating inequality are given below.

This closes one natural nonconcave family but does not close the full smooth
configuration dual.

For the physical covering interpretation, `0<a<=A` is the primitive range.
For `a<A`, `f_a` is exactly the covering closure of its restriction to the
socket interval `(0,A)`: ceiling subadditivity gives the lower bound, and
splitting `x` into `ceil(x/a)` positive parts gives equality.  At `a=A`
the same statement holds away from the zero-measure set of positive
multiples of `A`, which is all that the continuum integral uses.  If
`a>A`, the socket restriction is the constant price one and its physical
covering closure is the `a=A` minimum-piece price, up to the same endpoint
convention, not `f_a`; Theorem 2.1 for `a>A` is a stronger analytic
inequality but not a new physical MIR ray.

## 1. The two exact costs

Put

\[
A={\sqrt\pi\over2},
\]

and let the job and socket measures have densities

\[
j(x)=2(A+x)e^{-(A+x)^2}\quad(x>0),
\]

and

\[
s(y)=2(A-y)e^{-(A-y)^2}\quad(0<y<A).
\]

Their first moments agree.  Their masses differ by

\[
M:=\int s-\int j=1-2e^{-A^2}=1-2e^{-\pi/4}>0.       \tag{1.1}
\]

For `a>0`, the layer-cake identity for the ceiling gives

\[
\begin{aligned}
J(a)&:=\int_0^\infty f_a(x)j(x)\,dx
     =\sum_{n\ge0}e^{-(A+na)^2},\\
S(a)&:=\int_0^A f_a(y)s(y)\,dy
     =\sum_{0\le na<A}\left(1-e^{-(A-na)^2}\right).
                                                        \tag{1.2}
\end{aligned}
\]

The strict endpoint convention in the second sum is immaterial to the
integral and is the correct finite expression for the displayed ceiling.

## 2. Fourier control of the rounding term

### Theorem 2.1 (all ceiling rays pass)

For every `a>0`,

\[
\boxed{J(a)<S(a).}                                  \tag{2.1}
\]

#### Proof for `0<a<=4A/5`

Let `sigma` be socket measure minus job measure.  Since its first moment is
zero,

\[
S(a)-J(a)=\int\left(\left\lceil{x\over a}\right\rceil-{x\over a}\right)
             d\sigma(x).                            \tag{2.2}
\]

Away from integer multiples of `a`,

\[
\left\lceil{x\over a}\right\rceil-{x\over a}
={1\over2}+{1\over\pi}\sum_{m\ge1}{\sin(2\pi m x/a)\over m}. \tag{2.3}
\]

The measures are absolutely continuous, so the values at the jumps do not
matter.  Define

\[
I(t):=\int\sin(tx)\,d\sigma(x).                     \tag{2.4}
\]

After substituting `z=A-y` on the socket side and `z=A+x` on the job side,

\[
I(t)=\int_0^\infty p(z)\sin(t(A-z))\,dz,
\qquad p(z)=2ze^{-z^2}.                              \tag{2.5}
\]

For

\[
F(t)=\int_0^\infty p(z)e^{-itz}\,dz,
\]

two integrations by parts give

\[
|I(t)|\le |F(t)|
 \le {|p'(0)|+\|p''\|_1\over t^2}.                 \tag{2.6}
\]

Here

\[
p'(z)=2(1-2z^2)e^{-z^2},\qquad
p''(z)=4z(2z^2-3)e^{-z^2}.                          \tag{2.7}
\]

The function `p'` decreases from `2` to
`-4e^{-3/2}` and then increases to zero.  Therefore

\[
|p'(0)|+\|p''\|_1
=4+8e^{-3/2}=:C<6.                                  \tag{2.8}
\]

In particular, the integrated Fourier series is absolutely convergent, and
(2.2)--(2.4) yield

\[
S(a)-J(a)
={M\over2}+{1\over\pi}\sum_{m\ge1}{I(2\pi m/a)\over m}. \tag{2.9}
\]

Consequently

\[
\left|S(a)-J(a)-{M\over2}\right|
\le {Ca^2\zeta(3)\over4\pi^3}.                     \tag{2.10}
\]

When `a<=4A/5`, using `A^2=pi/4`, `C<6`,
`zeta(3)<5/4`, and `pi^2>9`,

\[
{Ca^2\zeta(3)\over4\pi^3}
\le {C\zeta(3)\over25\pi^2}
< {1\over30}.                                      \tag{2.11}
\]

The elementary estimate in Lemma 2.2 below gives `M>3/35`, and hence

\[
S(a)-J(a)>{3\over70}-{1\over30}={1\over105}>0.     \tag{2.12}
\]

#### Proof for `a>=4A/5`

Write

\[
R(a):=\sum_{n\ge1}e^{-(A+na)^2}.                   \tag{2.13}
\]

This is decreasing in `a`.  Lemma 2.2 proves

\[
R(4A/5)<{3\over35}<M.                              \tag{2.14}
\]

If `4A/5<=a<A`, exactly the terms `n=0,1` occur on the socket side, so

\[
S(a)-J(a)
=M+\left(1-e^{-(A-a)^2}\right)-R(a)>M-R(a)>0.      \tag{2.15}
\]

If `a>=A`, only `n=0` occurs on the socket side, and

\[
S(a)-J(a)=M-R(a)>0.                                \tag{2.16}
\]

Together with (2.12), this proves (2.1).  \(\square\)

### Lemma 2.2 (rational Gaussian bounds)

The following strict inequalities hold:

\[
M>{3\over35},                                      \tag{2.17}
\]

and

\[
\sum_{n\ge1}e^{-A^2(1+4n/5)^2}<{3\over35}.        \tag{2.18}
\]

#### Proof

Use the classical elementary bound `pi>3.14=157/50`.  Since

\[
e^{157/200}>1+{157\over200}
+{1\over2}\left({157\over200}\right)^2
+{1\over6}\left({157\over200}\right)^3
+{1\over24}\left({157\over200}\right)^4
>{35\over16},                                      \tag{2.19}
\]

we have `e^{-pi/4}<16/35`, proving (2.17).

For the tail in (2.18), consecutive squared arguments differ by at least
`88/25`, so

\[
\sum_{n\ge1}e^{-A^2(1+4n/5)^2}
\le {e^{-81\pi/100}\over1-e^{-22\pi/25}}.          \tag{2.20}
\]

The degree-six exponential Taylor lower bounds, again with `pi>157/50`,
give

\[
e^{81\pi/100}>e^{12717/5000}>{25\over2},
\qquad
e^{22\pi/25}>e^{1727/625}>15.                      \tag{2.21}
\]

Hence the right side of (2.20) is strictly smaller than

\[
{2/25\over1-1/15}={3\over35}.                      \tag{2.22}
\]

This proves the lemma.  \(\square\)

## 3. Ceiling rays do not generate all finite covering prices

It would be tempting to combine Theorem 2.1 with the already proved
concave-price domination by claiming that all finite monotone-subadditive
covering prices are nonnegative sums of these two classes.  This is false.

Consider integer capacities `1,...,5` and the price table

\[
f(0)=0,qquad (f(1),f(2),f(3),f(4),f(5))=(1,2,2,2,3). \tag{3.1}
\]

This table is nondecreasing and subadditive on all sums at most five.  It is
also its own finite covering closure: a target of size `1,2,3,4,5` has
minimum covering costs respectively `1,2,2,2,3` under this same capacity
price table.

Define the linear functional

\[
\mathcal E(g):=2g(1)-2g(2)+2g(4)-g(5).             \tag{3.2}
\]

### Theorem 3.1 (five-capacity MIR-cone separator)

Every nonnegative nondecreasing concave price `g` with `g(0)=0` satisfies

\[
\mathcal E(g)\ge0.                                  \tag{3.3}
\]

Every ceiling ray

\[
c_b(k)=\lceil bk\rceil\qquad(b>0)                  \tag{3.4}
\]

satisfies

\[
\mathcal E(c_b)\ge0.                               \tag{3.5}
\]

But the covering price (3.1) satisfies

\[
\mathcal E(f)=-1.                                  \tag{3.6}
\]

Therefore `f` is not a nonnegative conic combination of increasing concave
prices and arbitrary ceiling rays.

#### Proof

For a concave `g`, put

\[
\Delta_i=g(i)-g(i-1).
\]

Then

\[
\Delta_1\ge\Delta_2\ge\cdots\ge\Delta_5\ge0,
\]

and direct expansion gives

\[
\mathcal E(g)
=(\Delta_1-\Delta_2)+\Delta_3+(\Delta_4-\Delta_5)
\ge0.                                               \tag{3.7}
\]

For a ceiling ray, write `c_k=ceil(bk)`.  Ceiling subadditivity gives

\[
c_5\le c_4+c_1.                                    \tag{3.8}
\]

Also

\[
c_4=\lceil2(2b)\rceil\ge2\lceil2b\rceil-1=2c_2-1. \tag{3.9}
\]

Since `c_1>=1`,

\[
\begin{aligned}
\mathcal E(c_b)
&\ge 2c_1-2c_2+c_4-c_1\\
&=c_1-2c_2+c_4\\
&\ge c_1-1\ge0.                                    \tag{3.10}
\end{aligned}
\]

Finally, substituting (3.1) into (3.2) gives `-1`.  Since (3.2) is
nonnegative on every generator and hence on their conic hull, the claimed
decomposition is impossible.  \(\square\)

## 4. Exact consequence for the smooth configuration programme

The continuum dual now has the following proof-safe status.

1. Every nonnegative increasing concave price passes by Rayleigh convex
   order.
2. Every physical one-denomination ceiling/MIR closure passes; Theorem 2.1
   also proves the analytic `f_a` inequality outside the primitive range.
3. These two families do not generate even the five-capacity finite
   monotone-subadditive covering cone.

Thus the minimum-piece obstruction is absent in the actual Rayleigh limit,
but this is not a proof of the whole configuration inequality.  Additional
nonconcave extreme prices, already present in dimension five, must either be
controlled directly or bypassed by an explicit configuration mixture.
