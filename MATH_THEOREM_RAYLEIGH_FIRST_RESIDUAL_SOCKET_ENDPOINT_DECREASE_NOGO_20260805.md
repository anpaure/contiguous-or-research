# The first Rayleigh residual socket density decreases at its endpoint

**Date:** 2026-08-05  
**Method:** pure mathematics; elementary rational Gaussian bounds only;
no search or solver  
**Status:** unconditional scoped no-go.  The socket density left after the
first equal-level subtraction and overlap cancellation has negative left
derivative at the end of its support.  Hence it is not nondecreasing, so a
Wang--Wang construction which uses this whole normalized socket law as an
increasing-density role cannot apply.  The result does not obstruct
subdivision into monotone layers or a different joint-mixability packet.

## 1. Setup and derivative formula

Use the Rayleigh kernel

\[
 K(t)=
 \begin{cases}
 1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
 -e^{-(A+t)^2},&t>A,
 \end{cases}
 \qquad A={\sqrt\pi\over2}.
\]

Let `b` be its first zero and `c` its minimum.  For equal-level endpoints

\[
 K(\ell(u))=K(r(u))=u,
 \qquad \ell(u)<c<r(u),
\]

put `z(u)=r(u)-ell(u)` and `u(t)=z^{-1}(t)`.  After the first subtraction
and cancellation of the one-piece overlap, the residual socket density is

\[
 g_2(t)=-K'(t)-u'(t),\qquad 0<t<b.                \tag{1.1}
\]

At a fixed equal-level pair write

\[
 a=K'(r)>0,\qquad q=-K'(\ell)>0.
\]

The primary-subtraction theorem gives

\[
 u'(t)={aq\over a+q}.                              \tag{1.2}
\]

Differentiating with respect to the common level and then using (1.2)
gives the exact second-derivative identity

\[
 \boxed{
 u''(t)=
 {q^3K''(r)+a^3K''(\ell)\over(a+q)^3}.}           \tag{1.3}
\]

Indeed,

\[
 {dr\over du}={1\over a},\qquad
 {d\ell\over du}=-{1\over q},
\]

so

\[
 {da\over du}={K''(r)\over a},\qquad
 {dq\over du}={K''(\ell)\over q};
\]

substitution in the derivative of `aq/(a+q)` proves (1.3).

## 2. A coarse exact endpoint certificate

Let

\[
 e=\ell(u(b)),\qquad R=r(u(b))=e+b.
\]

The exact rational Gaussian brackets in the two-to-three count theorem
give

\[
 0.46<b<0.48,
 \qquad
 0.55<e<0.60,
 \qquad
 1.01<R<1.08.                                    \tag{2.1}
\]

We record the few derivative bounds needed below.  They use only

\[
 {4431\over5000}<A<{8863\over10000}               \tag{2.2}
\]

and the rational exponential enclosure

\[
 \sum_{j=0}^{20}{x^j\over j!}<e^x<
 \sum_{j=0}^{20}{x^j\over j!}
 +{x^{21}\over21!}{1\over1-x/22}
 \qquad(0\le x<22).                               \tag{2.3}
\]

Writing

\[
 Q(x)=2xe^{-x^2},\qquad Q'(x)=2(1-2x^2)e^{-x^2},
\]

one has

\[
 K''(t)=Q'(A-t)+Q'(A+t)\quad(t<A),
 \qquad
 K''(t)=Q'(A+t)\quad(t>A).
\]

Substitution of the rational rectangles in (2.1)--(2.2) into (2.3)
gives

\[
\boxed{
 K''(b)>0.19,
 \qquad K''(e)>0,
 \qquad -K''(R)<0.35.}                            \tag{2.4}
\]

The same enclosure gives

\[
 \boxed{a>0.075,\qquad q<0.28.}                  \tag{2.5}
\]

For orientation, none of these bounds is tight.  A fully elementary way
to see the margins in (2.4)--(2.5) is as follows.

* For `b in (0.46,0.48)`, the positive term `Q'(A-b)` exceeds `1.06`,
  while the magnitude of the negative term `Q'(A+b)` is below `0.87`.
* For `e in (0.55,0.60)`, the corresponding two bounds are `1.38` and
  `0.80`, proving `K''(e)>0`.
* Since `A+R in (1.8962,1.9663)`, the function `-Q'` is below `0.35` on
  that interval, while
  `a=2(A+R)e^{-(A+R)^2}>2(1.8962)(0.02)>0.075`.
* Finally

  \[
  q=2\bigl((A-e)e^{-(A-e)^2}
           -(A+e)e^{-(A+e)^2}\bigr)<0.28.
  \]

Every displayed decimal is a terminating rational; (2.3) turns these
checks into finite rational inequalities.

## 3. Strict endpoint decrease

### Theorem 3.1

The residual socket density has

\[
 \boxed{g_2'(b-)<0.}                               \tag{3.1}
\]

### Proof

At `t=b`, equation (1.3) and `K''(e)>0` imply

\[
 -u''(b)
 <\bigl(-K''(R)\bigr)
   \left({q\over a+q}\right)^3.                   \tag{3.2}
\]

By (2.5),

\[
 {a\over q}>{0.075\over0.28}={15\over56},
 \qquad
 {q\over a+q}<{56\over71}.
\]

Hence (2.4) gives

\[
 -u''(b)
 <0.35\left({56\over71}\right)^3
 <0.172.                                           \tag{3.3}
\]

Differentiating (1.1) from the left and using (2.4), (3.3),

\[
 g_2'(b-)=-K''(b)-u''(b)
 <-0.19+0.172<0.
\]

This proves (3.1). `square`

## 4. Exact scope

The density `g_2` starts from zero at the origin and is positive in the
interior, but Theorem 3.1 shows that it decreases in a left neighborhood
of `b`.  Therefore it is not nondecreasing on `(0,b)`.

This rules out the direct proposal in which the **whole** normalized
residual socket law is repeated as an increasing-density Wang--Wang role
against a decreasing job law.  It does not rule out:

1. decomposing `g_2` into several monotone role densities;
2. using the canonical uniform-interval layer decomposition;
3. assigning different role laws to different job bands; or
4. any coagulation outside the monotone-density theorem.

The surviving joint-mixability problem is therefore a role-decomposition
or layer-transport problem, not monotonicity of the unsplit socket density.

## 5. Frozen dependency

`MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
SHA at use
`1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.

