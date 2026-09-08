# Five-slot three-efficient clocks: delayed-`b` concavity and the pure lattice gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves that the
last three-pulse delayed gate is strictly concave in its endpoint increment
`b`; hence its minimum is attained either at the already-closed threshold
endpoint or at the pulse-free pure three-coset lattice.  It retains the
adverse pulse `K(p+b)-K(p+2a)`.  Positivity of the remaining two-variable
pure lattice is not proved here.

Put

\[
 A={\sqrt\pi\over2},\qquad c={\pi\over4},
\]

and let `K` be the Rayleigh signed-tail kernel.  The preceding audited
five-slot reduction leaves the gate

\[
\begin{aligned}
 \mathcal H(p,a,b)={}&\mathcal L_3(p;a,2a)\\
 &+K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(p+b)-K(p+2a),
\end{aligned}
\tag{0.1}
\]

on the exact domain

\[
 p<A,qquad p\ge3a,qquad a<A-p<b\le2a.
\tag{0.2}
\]

Only the three displayed positive-`b` terms vary with `b`.  Define

\[
                         J_{p,a}(b)=K(b-a)+K(b)+K(p+b).
\tag{0.3}
\]

## 1. A compact second-derivative lemma

Normalize

\[
 \alpha={a\over A},\qquad t={p\over A},
 \qquad v={b\over A},
\]

and put

\[
 h(s)=s e^{-cs^2},
 \qquad G(u)=h'(1+u)+h'(1-u).
\tag{1.1}
\]

For `0<=u<=1`, direct differentiation gives

\[
 {d^2\over du^2}K(Au)=2cG(u),
\tag{1.2}
\]

while for `u>=1`,

\[
 {d^2\over du^2}K(Au)=2c h'(1+u).
\tag{1.3}
\]

### Lemma 1.1

The function `G` is strictly increasing on `[0,1/2]`, and

\[
                         \boxed{G(1/4)+G(1/2)<-{1\over200}.}
\tag{1.4}
\]

#### Proof

The relevant derivatives are

\[
 h''(s)=2cs(2cs^2-3)e^{-cs^2},
\tag{1.5}
\]

and

\[
 h'''(s)=2ce^{-cs^2}
          \left(-4c^2s^4+12cs^2-3\right).
\tag{1.6}
\]

For `0<=u<=2/5`, both arguments `1-u,1+u` lie in
`[3/5,7/5]`.  If `q=cs^2`, then on this interval

\[
 {7\over25}<q<{11\over7}.
\]

The polynomial `-4q^2+12q-3` is concave and is positive at both displayed
rational endpoints:

\[
 -4(7/25)^2+12(7/25)-3={29\over625}>0,
\]

and

\[
 -4(11/7)^2+12(11/7)-3={293\over49}>0.
\]

Thus `h'''(s)>0` on `[3/5,7/5]`; hence `h''` is increasing there and

\[
 G'(u)=h''(1+u)-h''(1-u)>0.
\]

For `2/5<=u<=1/2`, one has `1+u>=7/5`, where `h''>0`, and
`1-u<=3/5`, where `h''<0`.  Therefore `G'(u)>0` on this interval as
well.

It remains to check (1.4).  Expanding the four terms gives

\[
 G(1/4)+G(1/2)
 =h'(1/2)+h'(3/4)+h'(5/4)+h'(3/2).
\tag{1.7}
\]

The positive terms satisfy, using `pi>157/50`,

\[
 h'(1/2)<1- {157\over400}={243\over400},
\]

and

\[
 h'(3/4)<1-{1413\over1600}={187\over1600}.
\tag{1.8}
\]

For the two negative terms, first

\[
 e^{-25\pi/64}>{13\over50}.
\tag{1.9}
\]

Indeed `25pi/64<275/224<5/4`, while

\[
 e<{87\over32},qquad
 e^{1/4}<1+{1\over4}
 +{{1\over32}\over1-{1\over12}}={113\over88},
\]

so `e^(5/4)<(87/32)(113/88)<50/13`.  Consequently

\[
 -h'(5/4)
 =e^{-25\pi/64}\left({25\pi\over32}-1\right)
 >{13\over50}{43\over32}={559\over1600}.
\tag{1.10}
\]

Similarly,

\[
                         e^{-9\pi/16}>{4\over25}.
\tag{1.11}
\]

To see this, `9pi/16<99/56<9/5`, and the positive exponential series,
with its tail taken from degree four, gives

\[
 e^{9/5}
 <{674\over125}+{2187\over3200}
 ={97207\over16000}<{25\over4}.
\]

Hence

\[
 -h'(3/2)
 =e^{-9\pi/16}\left({9\pi\over8}-1\right)
 >{4\over25}{19\over8}={19\over50}
 ={608\over1600}.
\tag{1.12}
\]

Combining (1.7)--(1.12),

\[
 G(1/4)+G(1/2)
 <{1159\over1600}-{1167\over1600}
 =-{1\over200}.
\]

This proves the lemma. \(\square\)

## 2. Strict concavity in `b`

### Theorem 2.1

For every fixed feasible pair `(p,a)`, the function

\[
                         b\longmapsto\mathcal H(p,a,b)
\]

is strictly concave on the closed interval

\[
                         A-p\le b\le2a.
\tag{2.1}
\]

#### Proof

Put `d=1-t`.  The domain (0.2) gives

\[
                         \alpha<d<v\le2\alpha,
 \qquad t\ge3\alpha.
\tag{2.2}
\]

It follows that

\[
 \alpha<{1\over4},qquad
 0<v<{1\over2},qquad
 0<v-\alpha\le{v\over2}\le{1\over4}.
\tag{2.3}
\]

Using (1.2)--(1.3), the second derivative of the `b`-dependent part,
apart from the positive scale factor `2c/A^2`, is

\[
 G(v-\alpha)+G(v)+h'(1+t+v).
\tag{2.4}
\]

By monotonicity of `G` and (2.3),

\[
 G(v-\alpha)+G(v)
 \le G(v/2)+G(v)
 \le G(1/4)+G(1/2)<-{1\over200}.
\tag{2.5}
\]

Also `t+v>=1`, so `1+t+v>=2` and `h'(1+t+v)<0`.
Thus (2.4) is strictly negative.  The other terms in (0.1) do not depend
on `b`, proving strict concavity. \(\square\)

### Corollary 2.2 (endpoint collapse)

For every point of (0.2),

\[
 \boxed{
 \mathcal H(p,a,b)
 \ge\min\left\{
   \mathcal H(p,a,A-p),
   \mathcal L_3(p;a,2a)
 \right\}.}
\tag{2.6}
\]

The adverse pulse is present throughout this comparison; it vanishes only
at the right endpoint `b=2a`.

#### Proof

A concave function on a compact interval attains its minimum at an
endpoint.  At `b=2a`, all three pulse differences in (0.1) vanish, leaving
`mathcal L_3(p;a,2a)`. \(\square\)

## 3. The threshold endpoint is already positive

Let

\[
                         d=A-p.
\]

At `b=d`, the extremal table realizing (0.1) is

\[
 (0,d-a,d,p,p+a,A).
\tag{3.1}
\]

The inequalities `a<d<2a` and `p>=3a` verify internal
superadditivity and size-three maximal efficiency directly.  Its endpoint
is the first threshold crossing.  Therefore the previously proved
threshold-endpoint theorem gives

\[
                         \boxed{
 \mathcal H(p,a,A-p)>{69\over10000}.}
\tag{3.2}
\]

For completeness, the only non-immediate checks are

\[
 p\ge2d-a,qquad p+a\ge2d,qquad 2p\ge3d,
\]

all of which follow from `p>=3a` and `d<2a`.

## 4. The sole residual pure lattice

Define

\[
                         \mathcal P(p,a)
 :=\mathcal L_3(p;a,2a).
\tag{4.1}
\]

Equations (2.6) and (3.2) show that

\[
 \boxed{
 \mathcal P(p,a)>0
 \quad\Longrightarrow\quad
 \mathcal H(p,a,b)>0.}
\tag{4.2}
\]

The exact residual domain is

\[
 \boxed{
 0<a<{A\over4},qquad
 p\ge3a,\qquad p>A-2a,\qquad p<A-a.}
\tag{4.3}
\]

All boundary pieces of (4.3) are already positive:

1. on the boundary `p=3a` (which is feasible for `a>A/5`), the three
   residue classes interlace and
   `mathcal P(3a,a)=C(a)>0`;
2. on the limiting boundary `p=A-2a` (active for `a<=A/5`), the
   capacity-five endpoint is exactly `A`, so (3.2) applies with `b=2a`;
3. at `p=A-a`, adjoining the inert size-four value `A=p+a` gives the
   same Bellman clock, and the complete four-slot theorem proves
   positivity.

The literal period derivative is

\[
 {\partial\over\partial p}\mathcal P(p,a)
 =\sum_{q\ge1}q\left(
 K'(qp)+K'(qp+a)+K'(qp+2a)
 \right).
\tag{4.4}
\]

Thus the original three-variable, three-pulse gate has been reduced to a
two-variable pulse-free theta train whose entire topological boundary is
positive.  What remains is exactly the exclusion of a negative interior
minimum of (4.1); no finite Apéry pulse or endpoint chamber remains.

## 5. Exact scope

This theorem proves the `b`-concavity and endpoint reduction
unconditionally.  It does **not** assert (4.2)'s premise.  Complete
positivity of the size-three-efficient five-slot branch is now equivalent,
on this last face, to positivity of the pure lattice (4.1)--(4.3).
