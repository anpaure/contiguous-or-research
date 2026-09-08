# The first Rayleigh residual job density is strictly decreasing

**Date:** 2026-08-05  
**Method:** pure mathematics; elementary rational Gaussian bounds only;
no search or solver  
**Status:** unconditional.  After the first equal-level subtraction and
overlap cancellation, the residual job density `f_2(t)=u'(t)` is strictly
decreasing on its complete support `(b,infinity)`.  Together with the
separate endpoint-decrease theorem for the socket density, this shows that
the remaining Wang--Wang obstruction lies entirely on the unsplit socket
role.

## 1. Setup

Let `K` be the Rayleigh signed-tail kernel, with zero `b` and minimum `c`.
At equal level `u`, write

\[
 \ell=\ell(u)<c<r=r(u),
 \qquad t=r-\ell,
\]

and

\[
 a=K'(r)>0,
 \qquad q=-K'(\ell)>0.
\]

The transformed density and its derivative are

\[
 u'(t)={aq\over a+q},                             \tag{1.1}
\]

\[
 u''(t)={q^3K''(r)+a^3K''(\ell)\over(a+q)^3}.     \tag{1.2}
\]

The residual job support begins at `t=b`.  Put

\[
 e=\ell(u(b)),\qquad R=r(u(b))=e+b.
\]

The rational endpoint certificate gives

\[
 b>0.469,qquad e>0.565,qquad R>1.034,qquad A>0.8862. \tag{1.3}
\]

It also gives

\[
 -K'(e)>0.218>{1\over5}.                          \tag{1.4}
\]

## 2. Uniform branch bounds beyond `t=b`

As `t` increases from `b`, the right endpoint `r` increases from `R` and
the left endpoint `ell` decreases from `e` toward `b`.

On `[b,e]`,

\[
 K''(x)=Q'(A-x)+Q'(A+x)>0,
 \qquad Q(x)=2xe^{-x^2}.                          \tag{2.1}
\]

Indeed, throughout the rational rectangle supplied by (1.3), the first
term exceeds `1.06` and the magnitude of the second is below `0.87`.
Therefore `-K'` decreases with its argument on `[b,e]`, and

\[
 q=-K'(\ell)\ge-K'(e)>{1\over5}.                 \tag{2.2}
\]

On the right branch put `w=A+r`.  Equation (1.3) gives

\[
 w>A+R>1.9202.                                    \tag{2.3}
\]

Since `Q` is decreasing above `1/sqrt2`, the same rational exponential
enclosure gives

\[
 a=Q(w)<{1\over10}.                               \tag{2.4}
\]

Moreover

\[
 K''(r)=Q'(w)=-a\left(2w-{1\over w}\right),       \tag{2.5}
\]

and (2.3) implies

\[
 2w-{1\over w}>3.                                \tag{2.6}
\]

Finally, the global curvature theorem gives

\[
 K''(\ell)<{8\over5}.                             \tag{2.7}
\]

## 3. Strict decrease

Substitute (2.5) into the numerator of (1.2):

\[
\begin{aligned}
 q^3K''(r)+a^3K''(\ell)
 &=a\left[-q^3\left(2w-{1\over w}\right)
             +a^2K''(\ell)\right].
\end{aligned}                                     \tag{3.1}
\]

Equations (2.2), (2.4), (2.6), and (2.7) give

\[
 q^3\left(2w-{1\over w}\right)>{3\over125},
\]

whereas

\[
 a^2K''(\ell)<{1\over100}{8\over5}={2\over125}.
\]

Thus the bracket in (3.1) is strictly negative.  Since `a>0` and the
denominator in (1.2) is positive,

\[
 \boxed{u''(t)<0\qquad(t>b).}                     \tag{3.2}
\]

### Theorem 3.1

The first transformed, overlap-cancelled residual job density

\[
 f_2(t)=u'(t){\bf1}_{(b,\infty)}(t)
\]

is strictly decreasing on `(b,infinity)`.

## 4. Consequence and scope

Reflecting `f_2` produces an increasing density, exactly the job-side
orientation required by the same-direction monotone joint-mixability
theorem.  The whole normalized socket law nevertheless cannot be used as
the repeated role, because its density decreases near `b`.  Therefore any
Wang--Wang completion must decompose the socket law into monotone roles or
uniform layers; no further job-side monotonicity theorem is missing.

The result does not itself provide the required job split by arity, support,
and mean.

## 5. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.
2. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_SOCKET_ENDPOINT_DECREASE_NOGO_20260805.md`,
   SHA at use
   `78e017354f77b21e6ba0c53301027e25cec3ffd020872727cbe9aab8802469c7`.
3. `MATH_THEOREM_RAYLEIGH_CANONICAL_DISTANCE_SPLIT_LOCAL_CAPACITY_NOGO_20260805.md`,
   SHA at use
   `6e303bcf078f051f5645f6138b7983ac7dd00cb50ccbd47a23f4749af1ad4595`.
