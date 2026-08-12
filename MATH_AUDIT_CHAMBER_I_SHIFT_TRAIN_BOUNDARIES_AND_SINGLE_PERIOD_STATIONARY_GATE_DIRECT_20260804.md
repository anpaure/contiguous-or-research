# Direct proof audit: Chamber-I shift boundaries and period-stationary collapse

**Date:** 2026-08-04  
**Verdict:** **GO as a reduction.**  The shift-train polygon, both lower
period boundary comparisons, the strict period-derivative convexity, and
the collapse to one period-stationary scalar are internally consistent.
This is an author-side direct audit, not an independent audit and not a
positivity certificate for the final scalar.

## 1. Shift-train domain and convexity

With `t=P/A`, `u=w/A`, the desired wedge is

\[
 1/2\le t\le3/4,\qquad t/3\le u\le2t/3.
\]

The cut `t+u=1` meets the lower rail only at `(3/4,1/4)` and the upper
rail at `(3/5,2/5)`.  The compact polygon therefore has precisely the
four vertices listed in (1.10), and the tail polygon the three vertices
in (1.11).

On the compact polygon every nonlinear summand is `D` of an affine form
or `h` of an affine form at argument at least `2`; on the tail polygon
the same is true with the crossing `D` replaced by `h` at argument at
least `2`.  Since `D''>0` and `h''>0` in those ranges, every Hessian is a
nonnegative scalar times an outer product.  Thus the infinite Gaussian
sum is convex after termwise limiting.

The rational bounds in (1.12) have comfortable margins.  Direct
substitution gives approximate locations only as a readability check,
not as proof:

\[
 -0.134,\quad-0.021,\quad-0.051,\quad-0.133,\quad-0.109.
\]

They agree with the strict rational upper bounds.  The Taylor remainder
sign in (1.14) is valid for every positive `z` by Taylor's theorem, and
the Gaussian ratio (1.15) makes the infinite-tail enclosure literal.

## 2. Boundary regrouping

At `p=A/2`, the exact chamber functional splits into the three braces in
(2.2).  The first replacement is favorable because
`0<=b-a<=a<=A/6`.  In the third brace only the first two occurrences are
replaced; every later occurrence lies above `A`, where increasing the
argument from `b` to `2a` increases `K`.  Hence the comparison with
`F_(A/2)(b)` is in the claimed direction.

The authenticated half-period theorem is valid on all of `[0,A/3]`, so
both comparisons `F(b)>=F(2a)` and the monotone decrease in `a` are
legal.  At `a=A/6`, the residues `0,A/6,A/3` modulo `A/2` enumerate the
complete arithmetic lattice.

At `p=3a`, feasibility gives `A/6<=a<A/4`.  The same tail comparison
starts no lower than `7a>A`, and Theorem 1.1 applies exactly on
`a<=b<=2a`.  The three residues `0,a,2a` modulo `3a` again enumerate the
complete arithmetic lattice.

## 3. Period derivative

Differentiating the exact clock first removes the finite
`K(p+2a)` occurrence and replaces it by `K(p+b)`, producing (4.1).
No availability pulse is omitted.  For `q>=2`, all arguments are at least
`2p>=A`; for `q=1`, all three retained arguments are at most `A`.

The compact `K'''` theorem and the explicit tail formula (4.2) make every
summand of `partial_p^3 G` strictly positive.  Therefore `partial_p G` is
strictly convex and has at most two zeros, only the later of which can
have nonnegative derivative.  This proves the singleton property of
`mathcal T_(a,b)` exactly as in the audited `b`-fibre argument.

At `p=A-b`, the retained fifth value is the threshold value `A`, so the
cited threshold theorem applies.  The two lower endpoints were proved in
Sections 2--3.  Thus every possible nonpositive minimum is the unique
period-stationary scalar, and (5.2) is an exact equivalence rather than
only a sufficient condition.

Finally, all `q>=2` derivative terms are positive.  If `p>=xi`, the
three compact `q=1` derivatives are nonnegative as well, excluding a
stationary point.  Combining `p_*<xi` with the previous interior
`b`-stationary theorem's `p_*+b>xi` gives (5.4).

For the curvature filter, `p>=3a` and `b<=2a` give `p>=3b/2`.
Together with `p+b<A` this yields `b<2A/5`.  The compact second
derivative is increasing, and the rational sign at `2A/5` is negative,
so both low entries in `Xi` are negative.  The high entry is positive on
the rising side beyond `xi`.  Hence `0<=Xi<K''(p+b)`.  The determinant
inequality for the `(p,b)` Hessian then gives `Omega>K''(p+b)`, and
literal subtraction leaves exactly `mathfrak C(p,a)` in (5.10).  No
tail term or multiplicity is dropped: the period second derivative has
weights `q^2`.

## 4. Scope

The audit establishes no sign for `mathfrak S(a,b)`.  It therefore does
not claim complete chamber-I, six-slot, all-grid, or OR-word positivity.
