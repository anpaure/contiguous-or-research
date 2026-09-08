# A propagating concave-branch cone for anchored rearrangement

**Date:** 2026-08-05  
**Method:** pure analysis; no search or solver  
**Status:** unconditional abstract theorem.  It identifies the exact scalar
aperture not supplied by branch concavity or zero total mass.  The first
Rayleigh iterate does not literally belong to the cone, so this theorem is
not by itself an induction for the Rayleigh kernel.

## 1. The cone

Let `H` be continuous and integrable on `[0,infinity)`, with zero integral.
Assume there are `0<a<b` such that

1. `H>0` on `[0,a)`, `H(a)=0`, and `H<0` on `(a,infinity)`;
2. `H` is concave on `[0,b]`;
3. `H` is increasing and concave on `[b,infinity)`, with `H(t)->0`;
4. `b` is the unique minimum.

Write

\[
 P=H(0),\qquad q=-H(b),
\]

and let `C_H` be the anchored negative-component profile.

The two concave pieces are allowed to meet in an upward cusp at `b`.

## 2. Convexity of the rearranged negative profile

For `0<s<q`, let `L(s) in (a,b)` and `R(s)>b` satisfy

\[
 H(L(s))=H(R(s))=-s.
\]

Put

\[
 g(s)=-H'(L(s)),\qquad f(s)=H'(R(s)).
\]

The component length is `Z(s)=R(s)-L(s)`.  If `t=Z(s)`, inverse
differentiation gives

\[
 -C_H'(t)={g(s)f(s)\over g(s)+f(s)}.             \tag{2.1}
\]

As `t` increases, `s` decreases, `L(s)` moves left and `R(s)` moves
right.  Concavity on the left says `-H'` is nondecreasing with its spatial
argument, so `g(s)` decreases as `L` moves left.  Concavity on the right
says `H'` is nonincreasing, so `f(s)` decreases as `R` moves right.

The parallel-sum map `(x,y)->xy/(x+y)` is increasing in both variables.
Therefore `-C_H'(t)` is nonincreasing.  Equivalently,

\[
 \boxed{C_H\text{ is decreasing and convex}.}   \tag{2.2}
\]

The same conclusion holds in the nonsmooth case by approximation, or
directly from monotonicity of one-sided slopes.

## 3. Cone propagation

### Theorem 3.1

If, in addition,

\[
 \boxed{P>q,}                                    \tag{3.1}
\]

then `G=RH=H_+-C_H` has exactly one zero, has its unique minimum at the
old zero `a`, and is concave on each side of that minimum.

More explicitly, there is one `a_G in (0,a)` such that

\[
 G>0\text{ on }[0,a_G),
 \qquad
 G<0\text{ on }(a_G,infinity),                  \tag{3.2}
\]

while

\[
 G(0)=P-q,
 \qquad
 -G(a)=C_H(a).                                   \tag{3.3}
\]

### Proof

On `[0,a]`,

\[
 G=H-C_H.
\]

The first term is concave and, by (2.2), the second term with its minus
sign is concave.  Thus `G` is concave on `[0,a]`.  Its endpoint values are

\[
 G(0)=P-q>0,
 \qquad
 G(a)=-C_H(a)<0.
\]

A concave function's nonnegative superlevel set is an interval.  Since it
contains zero but not `a`, there is exactly one crossing.

On `[a,infinity)`, `G=-C_H`; it is increasing and concave by (2.2), and
tends to zero from below.  A concave function on `[0,a]` attains its
minimum at an endpoint.  Since `G(a)<G(0)`, the unique minimum is at `a`.
This proves every assertion. `square`

Thus branch concavity is a genuine regenerative shape cone.  It turns the
infinite-dimensional sign-order question into a scalar aperture question.

## 4. Exact scalar required for another step

The output's positive origin height and negative depth are, by (3.3),

\[
 P_G=P-q,
 \qquad
 q_G=C_H(a).                                     \tag{4.1}
\]

To apply Theorem 3.1 again, the necessary and sufficient scalar row is

\[
 \boxed{P-q>C_H(a).}                             \tag{4.2}
\]

Equivalently,

\[
 \boxed{P>q+q_G.}                                \tag{4.3}
\]

Consequently a complete induction in this cone consists of only two rows:

1. the concave-branch shape, which Theorem 3.1 regenerates;
2. the aperture inequalities `P_n>q_n+q_{n+1}`.

The second row is not a consequence of zero area, integrable tails, or
branch concavity.

## 5. Exact obstruction to deleting the scalar row

There is an exact continuous counterexample inside the cone.  Put

\[
 b={19\over16},\qquad \lambda={96\over103},
\]

and define

\[
 H(t)=
 \begin{cases}
  1,&0\le t\le3/4,\\
  1-4(t-3/4),&3/4\le t\le b,\\
  -{3\over4}e^{-\lambda(t-b)},&t\ge b.
 \end{cases}                                    \tag{5.1}
\]

It is continuous, its unique zero is `a=1`, and its unique minimum is
`H(b)=-3/4`.  On `[0,b]` its slope drops from zero to `-4`, so that branch
is concave.  The right exponential branch is increasing and strictly
concave.

Its positive area is

\[
 {3\over4}+{1\over2}{1\over4}={7\over8}.
\]

Its negative left-triangle area and right-tail area are

\[
 {1\over2}{3\over16}{3\over4}={9\over128},
 \qquad
 {3/4\over\lambda}={103\over128},
\]

whose sum is also `7/8`.  Thus `int H=0` exactly.

At negative depth `s in (0,3/4)`, the component endpoints are

\[
 L(s)=1+{s\over4},
 \qquad
 R(s)=b+{103\over96}\log {3/4\over s}.
\]

Hence

\[
 Z(s)={3\over16}-{s\over4}
      +{103\over96}\log {3/4\over s}.           \tag{5.2}
\]

At `s=1/4`, using `log 3>1`,

\[
 Z(1/4)={1\over8}+{103\over96}\log3>1=a.
\]

Since `Z` decreases, this says

\[
 C_H(a)>{1\over4}=P-q.                           \tag{5.3}
\]

So the first rearrangement has positive origin, but its origin is already
too shallow for a second cone step, despite continuity, exact zero area,
strict tails, and branch concavity.

This is the scalar form of the subtractive-Euclidean rectangular orbit
obstruction.

## 6. Rayleigh placement relative to the cone

Let `H=RK` be the first Rayleigh iterate and

\[
 g_2=-H'
\]

on its decreasing branch.  The authenticated endpoint theorem gives

\[
 g_2'(b-)<0.
\]

Hence

\[
 H''(b-)=-g_2'(b-)>0.                            \tag{6.1}
\]

The first Rayleigh iterate is therefore **not** concave on its complete
left branch and does not directly enter the cone.

The newly proved second-iterate one-crossing theorem does show the correct
sign order for `R^2K`.  To place `R^2K` inside this cone it would suffice
to prove the two narrower differential statements

\[
 H''\le0\text{ on the positive support of }H,
 \qquad
 C_H''\ge0.                                      \tag{6.2}
\]

Indeed `R^2K=H-C_H` before the old zero and equals `-C_H` afterward.
Those two inequalities would make both branches concave.  They are not
proved here.

Even after (6.2), induction still requires the scalar aperture

\[
 (R^2K)(0)>-\min R^2K,                           \tag{6.3}
\]

and its analogues at every later step.  Zero area and Gaussian tails do
not supply (6.3) automatically, as Section 5 demonstrates.

## 7. Conclusion

There is a clean propagating analytic cone, but it does not remove the
essential scalar obstruction:

\[
 \boxed{
 \text{branch concavity regenerates; origin-versus-depth aperture does not.}}
\]

For the Rayleigh orbit, the most focused next targets are therefore:

1. prove (6.2) for the second iterate;
2. prove a quantitative aperture recurrence, or instead prove the signed
   first-moment barrier directly.
