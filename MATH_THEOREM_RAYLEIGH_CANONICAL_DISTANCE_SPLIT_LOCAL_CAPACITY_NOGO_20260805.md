# Rayleigh canonical distance-to-minimum split exceeds local socket capacity

**Date:** 2026-08-05  
**Method:** pure mathematics; elementary rational Gaussian enclosures only;
no search or solver  
**Status:** unconditional scoped no-go.  Splitting each first-transformed
job at the old kernel minimum gives an exact two-piece algebraic
decomposition, but using that split on the full two-piece-eligible initial
job band is not a submeasure of the physical residual socket bank.  A
thinned or shifted-pivot version is not excluded.

## 1. The canonical split and its occurrence densities

Use the Rayleigh kernel `K`, its minimum `c`, and equal-level inverse
branches

\[
 K(\ell(u))=K(r(u))=u,
 \qquad \ell(u)<c<r(u).
\]

The transformed job is

\[
 t=z(u)=r(u)-\ell(u).
\]

Its canonical distance-to-minimum split is

\[
 y_-(u)=c-\ell(u),
 \qquad
 y_+(u)=r(u)-c,
 \qquad
 y_-(u)+y_+(u)=t.                                \tag{1.1}
\]

Put

\[
 a(u)=K'(r(u))>0,
 \qquad q(u)=-K'(\ell(u))>0.
\]

Since `d ell/du=-1/q` and `dr/du=1/a`, the pushforward of level measure
`du` under the two pieces has densities

\[
 \rho_-(y)=-K'(c-y),
 \qquad
 \rho_+(y)=K'(c+y),                              \tag{1.2}
\]

on their respective image intervals.  Thus (1.1) is a literal two-piece
kernel whenever both distances are below the socket ceiling `b`.

Let `u_b=z^{-1}(b)`, and write

\[
 e=\ell(u_b),\qquad R=r(u_b)=e+b.
\]

The first residual jobs are those with `u>u_b`.  At their lower endpoint,

\[
 y_-^0=c-e,
 \qquad y_+^0=R-c.                               \tag{1.3}
\]

## 2. Exact rational separation at the first left piece

The exponential-tail enclosure

\[
 \sum_{j=0}^{20}{x^j\over j!}<e^x<
 \sum_{j=0}^{20}{x^j\over j!}
 +{x^{21}\over21!}{1\over1-x/22}
\]

together with `4431/5000<A<8863/10000` gives the following terminating-
rational brackets:

\[
 0.469<b<0.472,
 \qquad 0.781<c<0.783,
 \qquad 0.565<e<0.575.                           \tag{2.1}
\]

For orientation, the first two intervals follow from the signs of `K` at
`0.469,0.472` and of `K'` at `0.781,0.783`.  For the last interval, the
same-level comparisons

\[
 K(0.565)>K(1.037),
 \qquad
 K(0.575)<K(1.044)
\]

combine with the bounds on `b` and monotonicity of the right inverse
branch exactly as in the earlier separation-level certificate.

It follows that

\[
 0.206<y_-^0<0.218.                              \tag{2.2}
\]

Direct substitution of the rectangles in (2.1)--(2.2) into the same
rational exponential enclosure gives

\[
 \boxed{-K'(e)>0.218,}
 \qquad
 \boxed{-K'(y_-^0)<0.205.}                       \tag{2.3}

The margins are coarse: on `(0,A)`,

\[
 -K'(x)=2(A-x)e^{-(A-x)^2}
        -2(A+x)e^{-(A+x)^2},
\]

so (2.3) is again only a finite list of rational comparisons.

## 3. Local capacity failure

After overlap cancellation, the available socket density is

\[
 g_2(y)=-K'(y)-u'(y),\qquad 0<y<b,
\]

with `u'(y)>0`.  Therefore (2.3) gives

\[
 g_2(y_-^0)<-K'(y_-^0)<0.205<0.218<-K'(e)
             =\rho_-(y_-^0).                    \tag{3.1}
\]

Also `y_+^0>0.251` by (2.1), so no right-piece occurrence contributes at
`y_-^0`; (3.1) is already a one-branch overload.  All functions involved
are continuous at these interior points.  Hence the overload persists on
a positive-length neighborhood of `y_-^0`.

### Theorem 3.1

The canonical split (1.1), applied with unit weight to the full initial
band of first-residual jobs for which `y_+(u)<b`, does not have aggregate
socket marginal dominated by `g_2(y)dy`.

### Proof

Its left-piece marginal has density `rho_-`.  Equation (3.1) says this
density alone strictly exceeds the complete available socket density on a
non-null interval.  Adding the right-piece marginal cannot restore
domination. `square`

## 4. Exact scope

The theorem does not say that the distance split is useless.  Any compact
subband can be thinned by a sufficiently small positive factor, because
its demand densities are continuous and the physical density is positive
on the relevant interior support.  What fails is the hoped-for coefficient-
one subtraction of the whole pair-eligible band.

Nor does the theorem exclude replacing `c` by a job-dependent pivot
`p(u)` and using pieces `p(u)-ell(u)` and `r(u)-p(u)`.  That extra pivot
degree of freedom is exactly what can spread the overloaded left-piece
density across the socket bank.  The surviving two-piece problem is
therefore a pivot-transport problem, not the canonical fixed-pivot split.

## 5. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`,
   SHA at use
   `b63058f76b1ebb4904b4b939b10f981332d7de36bba90a39d8b1a35424787ac6`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.
3. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
   SHA at use
   `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.
