# Rayleigh arithmetic combs are exactly centered fractional-phase means

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation or search  
**Status:** unconditional all-mesh theorem.  For an arbitrary mesh, the
Rayleigh arithmetic-comb functional is the mean fractional part of a
centered Rayleigh variable minus its upper-tail mass.  Three integrations
by parts give a uniform Fourier bound for meshes no larger than the mean;
a direct Gaussian-tail estimate handles larger meshes.  Consequently every
Rayleigh arithmetic comb has strictly positive value.

## 1. Setup

Let `R` have Rayleigh density

\[
                         2r e^{-r^2}\,dr,
 \qquad r>0,                                     \tag{1.1}
\]

and put

\[
 A=\mathbb ER={\sqrt\pi\over2},
 \qquad p=\Pr(R>A)=e^{-A^2}=e^{-\pi/4}.          \tag{1.2}
\]

Define

\[
 X=(A-R)_+,
 \qquad Y=(R-A)_+.
\]

The Rayleigh signed-tail kernel is

\[
                         K(t)=\Pr(X>t)-\Pr(Y>t). \tag{1.3}
\]

For `h>0`, define its arithmetic-comb value

\[
                         C(h)=\sum_{n\ge0}K(nh). \tag{1.4}
\]

Write Euclidean division of the mean by the mesh as

\[
                         A=qh+\delta,
 \qquad q=\lfloor A/h\rfloor,
 \qquad0\le\delta<h.                             \tag{1.5}
\]

## 2. Centered phase identity

### Theorem 2.1

For every `h>0`,

\[
 \boxed{
 C(h)=\mathbb E\left\{ {R-\delta\over h}\right\}-p,
 }
\tag{2.1}
\]

where `{x}=x-floor(x) in[0,1)` is the ordinary fractional part, including
for negative `x`.

Equivalently,

\[
 \boxed{
 C(h)\ge0
 \quad\Longleftrightarrow\quad
 \mathbb E\left\{ {R-(A\bmod h)\over h}\right\}
 \ge e^{-\pi/4}.}
\tag{2.2}

### Proof

The tail-sum formula and (1.3) give

\[
 C(h)=\mathbb E\left\lceil{X\over h}\right\rceil
      -\mathbb E\left\lceil{Y\over h}\right\rceil.
\tag{2.3}
\]

Rayleigh's law is continuous, so lattice-boundary events have probability
zero.  Put

\[
                         Z={R-\delta\over h}.
\]

If `R<A`, then

\[
 \left\lceil{A-R\over h}\right\rceil
 =\lceil q-Z\rceil=q-\lfloor Z\rfloor.           \tag{2.4}
\]

If `R>A`, then

\[
 -\left\lceil{R-A\over h}\right\rceil
 =q-\lfloor Z\rfloor-1.                         \tag{2.5}
\]

Thus the random signed ceiling count in (2.3) is

\[
 q-\lfloor Z\rfloor-\mathbf1_{\{R>A\}}.         \tag{2.6}
\]

But `ER=A=qh+delta`, and hence `EZ=q`.  Taking expectations in (2.6)
therefore gives

\[
 C(h)=\mathbb E(Z-\lfloor Z\rfloor)-\Pr(R>A),
\]

which is (2.1). `square`

## 3. Equivalent shifted half-Gaussian sum

The same identity has a useful explicit analytic form.

### Corollary 3.1

For `q,delta` as in (1.5),

\[
 \boxed{
 C(h)=q+1-p-
       \sum_{m=0}^{\infty}e^{-(\delta+mh)^2}.}
\tag{3.1}
\]

Consequently all-mesh comb positivity is exactly the shifted lattice
bound

\[
 \boxed{
 \sum_{m=0}^{\infty}e^{-(\delta+mh)^2}
 \le q+1-p,
 \qquad A=qh+\delta,quad0\le\delta<h.}
\tag{3.2}

### Proof

For `0<=n<=q`, use the inner formula for `K(nh)`; for `n>q`, use the
Gaussian tail formula.  Reversing the first finite Gaussian sum gives

\[
\begin{aligned}
 C(h)
 &=q+1-sum_{m=0}^{q}e^{-(\delta+mh)^2}
       -\sum_{m=q}^{\infty}e^{-(\delta+mh)^2}\\
 &=q+1-p-sum_{m=0}^{\infty}e^{-(\delta+mh)^2},
\end{aligned}
\]

because the doubly counted joining term is
`e^{-(delta+qh)^2}=e^{-A^2}=p`. `square`

Formula (2.1) explains why the small-mesh limit is `1/2-p=K(0)/2`, not
a dimension-free positive constant: the centered Rayleigh phase becomes
asymptotically uniform.

## 4. A uniform centered-phase estimate for `h<=A`

Let

\[
                         \varphi(r)=2r e^{-r^2}
\tag{4.1}
\]

be the Rayleigh density and

\[
                         \widehat\varphi(t)
 =\int_0^\infty e^{itr}\varphi(r)\,dr            \tag{4.2}
\]

its characteristic function.

### Lemma 4.1 (quadratic-cubic Fourier decay)

For every `t>0`,

\[
 \boxed{
 |\widehat\varphi(t)|
 \le {2\over t^2}+{20\over t^3}.}
\tag{4.3}

### Proof

Direct differentiation gives

\[
\begin{aligned}
 \varphi'(r)&=2(1-2r^2)e^{-r^2},\\
 \varphi''(r)&=4r(2r^2-3)e^{-r^2},\\
 \varphi'''(r)&=(-16r^4+48r^2-12)e^{-r^2}.
\end{aligned}                                    \tag{4.4}
\]

The two positive zeros of `varphi'''` have squared locations

\[
 s_-={3-\sqrt6\over2},
 \qquad
 s_+={3+\sqrt6\over2}.                           \tag{4.5}
\]

Thus `varphi''` starts at zero, decreases to one negative minimum, rises
through zero to one positive maximum, and then decreases to zero.  The two
extremal magnitudes are

\[
 M=4\sqrt{6s_-}\,e^{-s_-},
 \qquad
 P=4\sqrt{6s_+}\,e^{-s_+}.                      \tag{4.6}
\]

Since `sqrt(6)>7/3`, one has `6s_-<2`, so

\[
                         M<4\sqrt2<6.            \tag{4.7}
\]

Also `6s_+<17` and `s_+>5/2`.  The elementary exponential series gives
`e^(5/2)>9`, and hence

\[
                         P<{17\over9}<2.         \tag{4.8}
\]

It follows from the three monotonicity pieces of `varphi''` that

\[
 \|\varphi'''\|_1
 =\operatorname {Var}(\varphi'')
 =2(M+P)<16<20.                                  \tag{4.9}
\]

Integrate (4.2) by parts three times.  The endpoint data are

\[
 \varphi(0)=0,
 \qquad \varphi'(0)=2,
 \qquad \varphi''(0)=0,
\]

and all three functions vanish at infinity.  Therefore

\[
 \widehat\varphi(t)
 ={2\over(it)^2}-{1\over(it)^3}
   \int_0^\infty e^{itr}\varphi'''(r)\,dr.
\tag{4.10}
\]

Equations (4.9)--(4.10) prove (4.3). `square`

### Theorem 4.2 (small- and medium-mesh phase bound)

For every `0<h<=A` and every real shift `delta`,

\[
 \left|
 \mathbb E\left\{{R-\delta\over h}\right\}
 -{1\over2}
 \right|
 <{35\over864}.                                  \tag{4.11}
\]

In particular, when `delta=A mod h`,

\[
 \mathbb E\left\{{R-\delta\over h}\right\}>p
\quad\text{and}\quad C(h)>0.                    \tag{4.12}

### Proof

The fractional-part sawtooth has Fourier series

\[
 \{x\}-{1\over2}
 =-{1\over\pi}\sum_{m\ge1}{\sin(2\pi mx)\over m}
\tag{4.13}
\]

away from the integers.  Rayleigh's law is continuous.  One may first use
the bounded Fejer sums in (4.13) and then pass to the limit.  Lemma 4.1
makes the resulting expected series absolutely convergent.  With
`t_m=2pi m/h`, the phase factor caused by `delta` has modulus one, so

\[
\begin{aligned}
 \left|E\left\{{R-\delta\over h}\right\}-{1\over2}\right|
 &\le {1\over\pi}\sum_{m\ge1}
       {|\widehat\varphi(t_m)|\over m}\\
 &\le {h^2\over2\pi^3}\sum_{m\ge1}{1\over m^3}
      +{20h^3\over8\pi^4}\sum_{m\ge1}{1\over m^4}.          \tag{4.14}
\end{aligned}
\]

Use `h<=A`, `A^2=pi/4`, `zeta(3)<5/4`, and `zeta(4)<10/9`.
The elementary bounds `pi^2>9` and `sqrt(pi)>5/3` give

\[
 {A^2\zeta(3)\over2\pi^3}
 <{5\over288},
\tag{4.15}
\]

and

\[
 {20A^3\zeta(4)\over8\pi^4}
 <{5\over216}.                                   \tag{4.16}
\]

(For example, the displayed zeta bounds follow by isolating the first two
terms and bounding the remaining decreasing tails by integrals.)  Hence

\[
 \left|E\left\{{R-\delta\over h}\right\}-{1\over2}\right|
 <{5\over288}+{5\over216}
 ={35\over864}.                                  \tag{4.17}
\]

The authenticated Rayleigh bound `K(0)>0.088` says

\[
 p={1-K(0)\over2}<{57\over125}.                  \tag{4.18}
\]

Finally

\[
 {1\over2}-{35\over864}={397\over864}
 >{57\over125}>p.                               \tag{4.19}
\]

This proves (4.11)--(4.12), using Theorem 2.1 in the last implication.
`square`

## 5. Meshes larger than the mean

### Theorem 5.1

If `h>A`, then

\[
                         \boxed{C(h)>0.}         \tag{5.1}
\]

### Proof

Here `q=0`, and the direct kernel formula gives

\[
 C(h)=K(0)-\sum_{n\ge1}e^{-(A+nh)^2}.            \tag{5.2}
\]

Since `h>A`,

\[
 \sum_{n\ge1}e^{-(A+nh)^2}
 <\sum_{m\ge2}p^{m^2}.                          \tag{5.3}
\]

For `m>=2`, one has `m^2>=4+5(m-2)`, and therefore

\[
 \sum_{m\ge2}p^{m^2}
 \le {p^4\over1-p^5}.                           \tag{5.4}
\]

The authenticated rational Rayleigh bound `K(0)>0.088` gives
`p<0.456`.  Hence

\[
 {p^4\over1-p^5}<0.045<K(0).                    \tag{5.5}
\]

Equations (5.2)--(5.5) prove (5.1). `square`

Combining Theorems 4.2 and 5.1 gives the complete arithmetic face.

### Corollary 5.2 (all arithmetic combs are strictly positive)

For every `h>0`,

\[
 \boxed{
 C(h)>{377\over108000}>0.}                      \tag{5.6}
\]

### Proof

For `h<=A`, equations (4.17)--(4.19) and Theorem 2.1 give

\[
 C(h)>{397\over864}-{57\over125}
 ={377\over108000}.                             \tag{5.7}
\]

For `h>A`, the proof of Theorem 5.1 gives the much stronger lower bound
`C(h)>0.088-0.045=0.043`. `square`

At the reciprocal meshes `h=A/q`, the existing Poisson-summation identity
also gives the sharper formula

\[
 C(A/q)={1\over2}-p
 -2q\sum_{m\ge1}e^{-4\pi q^2m^2}>0.             \tag{5.8}
\]

## 6. Exact consequence and frontier

The previous comb analysis used Euler--Maclaurin asymptotics and a special
reciprocal-mesh theta identity.  Theorem 2.1 replaces the arbitrary-mesh
question by a single probabilistic statement:

> **Centered Rayleigh phase inequality.**  If `A=ER` and
> `delta=A mod h`, then
> \[
>       E\{(R-delta)/h\}\ge P(R>A).
> \]

Theorem 4.2 proves this centered phase inequality with a uniform strict
margin.  Therefore **every** arithmetic clock passes, not merely reciprocal
meshes or sufficiently small meshes.  Corollary 5.2 additionally gives a
dimension-free lower bound on the unscaled comb functional `C(h)`.  This
does not contradict the vanishing normalized margin `hC(h)` as `h` tends
to zero.

This remains strictly narrower than the full all-price theorem.  A formal
Apéry clock may have different negative displacements on its residue
classes, and its finite availability shoulder need not be an arithmetic
comb.  The result removes the entire one-period arithmetic face from the
frontier; it does not control those nonarithmetic residue displacements.

## 7. Dependencies

1. `MATH_THEOREM_RAYLEIGH_DEVIATION_LORENZ_AND_RESIDUAL_INTERVAL_CORE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`
   (for the authenticated rational bound `K(0)>0.088`).
