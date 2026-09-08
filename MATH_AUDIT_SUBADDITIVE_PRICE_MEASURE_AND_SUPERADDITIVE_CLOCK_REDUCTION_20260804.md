# Independent-style audit: anchored-window and inverse-clock reduction

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_SUBADDITIVE_PRICE_MEASURE_AND_SUPERADDITIVE_CLOCK_REDUCTION_20260804.md`

**Verdict:** PASS with the stated scope.  The theorem gives exact
representations and a valid residue lower envelope.  It does not prove the
universal Gaussian inequality.

## 1. Sign convention

The signed measure is socket minus job.  Its tail is

\[
 K(x)=\mu((x,\infty))-\nu((x,\infty)).
\]

For `0<=x<=A`, the two tails are respectively

\[
 1-e^{-(A-x)^2},\qquad e^{-(A+x)^2},
\]

and for `x>A` only the job tail remains.  This confirms (0.1) and the sign
in (1.3), (2.4), and (2.5).

The physical socket support is `(0,A)`, but enlarging the test class to all
monotone subadditive functions is exact at the universal-quantifier level.
For any such `f`, its `(0,A)`-generated covering closure `hat(f)_A` agrees
with `f` on socket capacities and dominates it on every job size.  Hence

\[
 \text{all physical closures pass}
 \Longrightarrow
 \text{all monotone subadditive }f\text{ pass},
\]

while the converse is immediate.  This fills the support step needed before
the clock equivalence; it does not assert that each individual clock price
is already self-generated from `(0,A)`.

## 2. Stieltjes and layer-cake forms

For `rho=df`, including the atom `rho({0})=f(0+)`,

\[
 \rho((x,x+t])=f(x+t)-f(x),\qquad
 \rho([0,t])=f(t)-f(0)=f(t)
 \quad(x>0).
\]

Thus anchored-window domination is exactly subadditivity, not merely a
necessary condition.  Including zero on the right is essential for ceiling
prices, which have a positive initial jump.

The Stieltjes identity uses `f(z)=int 1_(x<z) d rho(x)`.  The inverse-clock
identity instead uses the ordinary layer-cake formula

\[
 f(z)=\int_0^\infty {\bf1}_{f(z)>u}\,du.
\]

Both reduce to the same signed tail `K`.  Monotone functions have only
countably many discontinuities, and the Gaussian measures are continuous,
so endpoint conventions cause no missing atoms.

## 3. Clock equivalence

If `x<a_f(u)` and `y<a_f(v)`, approximation from below plus
subadditivity gives `x+y<=a_f(u+v)`.  Conversely, approximation from above
in the generalized inverse and superadditivity give

\[
 f_a(x+y)\le f_a(x)+f_a(y).
\]

Allowing `a=infinity` handles bounded prices; `K(infinity)=0` is the
correct tail convention.  The integer jump formula is the atomic special
case of layer cake.

## 4. Residue envelope

From superadditivity,

\[
 a(qh+r)\ge q a(h)+a(r)=qT+a(r).
\]

When `T>=A` and `q>=1`, both sides lie in the region where
`K(x)=-exp(-(A+x)^2)` is increasing.  Hence replacing the true clock by the
right side gives a lower, not upper, bound.  Summing the Gaussian tail gives
exactly (3.2).  No monotonicity assertion about `K` on `(0,A)` is used for
the `q=0` term.

The residue pair condition has the correct direction:

\[
 a(r)+a(h-r)\le a(h)=T.
\]

## 5. Theta obstruction

At `T=A`, the two endpoint residues give

\[
 G_A(0)+G_A(A)=1-2\sum_{n>=1}e^{-n^2\pi/4}.
\]

Poisson/Jacobi transformation says

\[
 \sum_{n\in\mathbb Z}e^{-\pi n^2/4}
 =2\sum_{m\in\mathbb Z}e^{-4\pi m^2}.
\]

Therefore the displayed expression is
`-4 sum_(m>=1)e^(-4 pi m^2)`, strictly negative.  This disproves only the
pointwise pair relaxation; it is not a counterexample clock and is not
claimed to be one.

## 6. Scope boundary

The exact open statement after this theorem is positivity on the complete
anchored-window cone, equivalently on complete superadditive clocks.  The
following do not follow:

* a decomposition into concave prices and ceiling rays;
* positivity from the pair condition alone;
* an integral whole-job fragmentation;
* a literal cross-SCD containment matching;
* `nu(k)<=B(k)+O(1)`.

The reduction is proof-safe and strictly analytic.
