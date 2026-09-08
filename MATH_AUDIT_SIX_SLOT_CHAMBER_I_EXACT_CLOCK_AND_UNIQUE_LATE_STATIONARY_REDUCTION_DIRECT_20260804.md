# Direct symbolic audit: six-slot chamber-I exact-clock and unique-stationary reduction

**Date:** 2026-08-04  
**Verdict:** **GO as a reduction.**  The actual chamber-I clock, the two
inert-generator identities, the period-`2p` lower clock, the compact
third-derivative sign, the endpoint/stationary minimizer classification,
and the degenerate `a=b=0` boundary all check symbolically.  This audit is
a direct author-side audit, not an independent audit and not a positivity
certificate for the three residual exits.

## 1. Exact binding

Primary theorem:

`MATH_THEOREM_SIX_SLOT_CHAMBER_I_EXACT_CLOCK_AND_UNIQUE_LATE_STATIONARY_REDUCTION_20260804.md`

SHA-256:

`0724658e0a0ea749e7dd2cc417377eda6fced2a47d6d8f8a27fe96ea6ec3b47d`

The dependency hashes printed in its Section 7 agree with the current
workspace bytes.

## 2. Table and recurrence audit

With `x=b-a`, the exact table is

\[
                         (0,x,b,p,p+a,p+b,2p).
\]

The chamber inequalities give

\[
 0\le x\le a,\qquad b\le2a,\qquad p\ge3a.
\]

Every nontrivial internal superadditivity row reduces to one of

\[
 b\ge2x,qquad p\ge2b-a,qquad p\ge a+b,
\]

or to `a>=x`.  The first is `b<=2a`; the other two follow from
`p>=3a` and `b<=2a`.  The exact decompositions

\[
 c_5=c_2+c_3,
 \qquad
 c_6=2c_3
\]

prove that sizes five and six are inert, not merely density ties.

The first six values are literal table values.  Size three has maximum
density because

\[
 {x\over1}\le {p\over3},
 \quad {b\over2}\le {p\over3},
 \quad {p+a\over4}\le {p\over3},
 \quad {p+b\over5}\le {p\over3},
 \quad {2p\over6}={p\over3}.
\]

The first four inequalities follow respectively from `x<=a<=p/3`,
`3b<=6a<=2p`, `3a<=p`, and `3b<=6a<=2p`.
The residue-one shift is `a`; the residue-two shift is `2a`.  Their first
availability failures are exactly

\[
 a\mapsto x,
 \qquad
 2a\mapsto b,
 \qquad
 p+2a\mapsto p+b,
\]

at capacities one, two, and five.  This reproduces every term of the
displayed `G_I` and verifies the exact-clock claim.

## 3. Period-retaining descent audit

Concatenating `q` optimal capacity-six configurations with an optimal
capacity-`i` configuration gives

\[
 V_{6q+i}\ge qV_6+V_i=2pq+W_i.
\]

For `q>=1`, both arguments are at least `2p>=A`; hence monotonicity of
`K` on its Gaussian tail points in the claimed lower-bound direction.
The six consecutive gaps of the lower clock are

\[
 x, a, p-b, a, x, p-b,
\]

and `p-b>=a` follows from `p>=3a`, `b<=2a`.  No replacement of `2p`
by `A` occurs.

## 4. Third-derivative audit

On the compact branch, with `u=x/A`,

\[
 K'(Au)=2A\{h(1+u)-h(1-u)\},
\]

so

\[
 K'''(Au)={2\over A}\{h''(1+u)-h''(1-u)\}.
\]

For `0<u<=1/2`, the cited compact lemma proves this bracket positive.
For `1/2<=u<1`, one has

\[
 1+u\ge3/2>\sqrt{6/\pi},
 \qquad
 0<1-u\le1/2<\sqrt{6/\pi},
\]

and the explicit sign formula for `h''` makes the first term positive and
the second negative.  Thus `K'''>0` on `(0,A)` exactly as claimed.

For `a>0`, feasibility gives

\[
 4a\le p+a\le p+b<A,
\]

so `2a<A/2`.  Therefore all three arguments of

\[
 J(b)=K(b-a)+K(b)+K(p+b)
\]

stay on the compact branch throughout the open fibre, and `J'''>0` is
legitimate without a hidden threshold jump.

## 5. Stationary classification audit

Since `J'` is strictly convex, it has at most two zeros.  An interior
minimum of `G_I` must have

\[
 J'=0,qquad J''\ge0.
\]

Among at most two zeros of a strictly convex differentiable function,
only the larger can have nonnegative derivative; in the one-root case the
same test keeps only a possible minimum or tangency.  Hence the stationary
set in the theorem has cardinality at most one.  Compactness of the closed
fibre then gives the exact endpoint-plus-stationary minimum formula.

The positive zero `theta` of

\[
 2\operatorname{arctanh}u=\pi u
\]

is unique after the root at zero because the left-minus-right function
has strictly increasing derivative, begins with negative derivative, and
tends to infinity.  Its value at `1/2` is negative, so `theta>1/2`.
Both low arguments of `J'` are below `A/2`; hence a zero of `J'` requires
the high argument `p+b` to exceed `A theta`.  This verifies the late-strip
restriction.

## 6. Degenerate-boundary audit

If `a=0`, then `a<=b<=2a` forces `b=0`, hence `x=0`.  Every finite pulse
vanishes and

\[
 \mathcal G_{\rm I}(p,0,0)
 =3\sum_{q\ge0}K(qp)=3C(p)>0.
\]

This uses the all-ceiling theorem at the arbitrary positive step `p`, not
the weak threshold-period theta bound.  Thus the reduction does not inherit
the latter bound's negative limiting artefact.

## 7. Exact scope

The theorem proves no sign for:

1. `E_0(p,a)`;
2. `L_3(p;a,2a)` on `p+2a<=A`;
3. the possible unique late stationary gate.

It therefore does not close chamber I or six-slot positivity.  Its valid
advance is the exact replacement of an unsigned three-dimensional
theta-relaxed gate by two explicit boundary gates and at most one
late-stationary gate of the actual clock, with the full degenerate boundary
already positive.

