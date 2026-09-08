# Independent audit: Rayleigh ceiling domination and the finite MIR-cone no-go

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md`

**Verdict:** PASS.  The all-`a` ceiling inequality is strict.  The
five-capacity table is a valid monotone-subadditive covering closure and the
displayed functional separates it from the conic hull of all increasing
concave prices and all unshifted ceiling rays.  The theorem does not claim
that the full smooth configuration dual is closed.

The physical covering scope has one qualification now made explicit in the
theorem.  For `0<a<A`, `f_a` is the covering closure of its socket
restriction.  At `a=A` this holds away from positive multiples of `A`, a
zero-measure endpoint convention.  For `a>A`, the restriction is constant
one and closes to the `a=A` minimum-piece price up to that convention; the
proved `f_a` inequality remains analytically true but is not an additional
physical one-denomination price.

## 1. Cost identities and endpoint convention

For `x>0`, almost everywhere,

\[
\left\lceil{x\over a}\right\rceil
=\sum_{n\ge0}{\bf1}_{x>na}.
\]

The job tail above `q` is `exp(-(A+q)^2)`.  The socket tail above `q<A` is
`1-exp(-(A-q)^2)`.  Tonelli therefore gives exactly the two sums `J(a)` and
`S(a)` in the theorem.  If `A/a` is integral, the strict inequality
`na<A` correctly omits the zero-measure endpoint contribution.

## 2. Fourier sign and decay

Writing `sigma=socket-job`, first-moment equality removes the linear part of
the ceiling.  The sawtooth Fourier series has positive sine sign:

\[
1-\{u\}={1\over2}+{1\over\pi}\sum_{m\ge1}{\sin(2\pi m u)\over m}.
\]

After both changes of variables, the sine transform is

\[
I(t)=\int_0^\infty2ze^{-z^2}\sin(t(A-z))\,dz.
\]

This confirms that the socket and job contributions have not been reversed.
For `p(z)=2ze^{-z^2}`, both endpoint values of `p` vanish.  Two integrations
by parts give

\[
\left|\int_0^\infty p(z)e^{-itz}\,dz\right|
\le {|p'(0)|+\int_0^\infty|p''(z)|\,dz\over t^2}.
\]

Now `p'(0)=2`; `p'` has unique interior minimum
`-4e^{-3/2}` and tends to zero.  Hence

\[
\int|p''|=2+8e^{-3/2},
\]

and the total constant is `4+8e^{-3/2}`.  This validates the `m^{-3}`
summability after the additional Fourier coefficient `1/m`, so Abel or
Fejer regularization passes to the displayed absolutely convergent series.

For `a<=4A/5`, substituting `A^2=pi/4` gives

\[
{Ca^2\zeta(3)\over4\pi^3}
\le {C\zeta(3)\over25\pi^2}<1/30.
\]

The coarse bounds used are all in the safe direction:
`C<6`, `zeta(3)<5/4`, and `pi^2>9`.

## 3. Rational tail audit

The degree-four Taylor polynomial at `157/200` exceeds `35/16`; explicitly
its excess is

\[
{26335867\over12800000000}>0.
\]

Thus `e^{-pi/4}<16/35` and `M>3/35`.

The degree-six Taylor polynomial at `12717/5000` exceeds `25/2` by

\[
{33139247666202631033441
 \over1250000000000000000000000}>0,
\]

and the degree-six Taylor polynomial at `1727/625` exceeds `15` by

\[
{20891492376545616889\over42915344238281250000}>0.
\]

Together with `pi>157/50`, these prove

\[
{e^{-81\pi/100}\over1-e^{-22\pi/25}}
<{2/25\over1-1/15}={3\over35}.
\]

For `4A/5<=a<A`, the socket sum has exactly two terms; for `a>=A`, it has
exactly one.  In both ranges the remaining right Gaussian tail is decreasing
in `a`, so the case split covers every positive `a` without a gap.

## 4. Finite covering-price audit

For prices `(1,2,2,2,3)` on capacities `1,...,5`, direct coverings attain
those five values.  No cheaper cover exists:

* size one costs at least one;
* size two costs at least two;
* sizes three and four have one-socket cost two, the smallest possible
  nonunit cost;
* size five costs at least three: a single size-five socket costs three,
  while any cover using a size-three or size-four socket needs another
  positive socket, and covers using only sizes one and two cost at least
  three.

Thus the table really is its finite covering closure.  Its subadditivity on
sums at most five follows directly from the only sharp nontrivial row
`f(5)=f(1)+f(4)=3`; all other decompositions have at least as much cost.

For increasing concave prices, the separator is

\[
(\Delta_1-\Delta_2)+\Delta_3+(\Delta_4-\Delta_5)\ge0.
\]

For arbitrary `b>0`, the two universal ceiling inequalities

\[
\lceil5b\rceil\le\lceil4b\rceil+\lceil b\rceil,
\qquad
\lceil4b\rceil\ge2\lceil2b\rceil-1
\]

give the same separator sign.  The test table has value `-1`.  The conic
non-generation conclusion is therefore exact and does not depend on a
finite enumeration of ceiling patterns.

## 5. Scope

What is proved is

\[
\int f_a\,d\mu<\int f_a\,d\nu\qquad(a>0)
\]

for every unshifted ceiling ray, plus a finite cone-separation theorem.
This does not prove the inequality for every nondecreasing-subadditive
price, give a whole-job configuration mixture, establish integral rounding,
or solve literal cross-SCD containment Hall.
