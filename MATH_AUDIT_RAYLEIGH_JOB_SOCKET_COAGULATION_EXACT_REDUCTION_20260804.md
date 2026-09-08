# Independent-style audit: Rayleigh job/socket coagulation reduction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_RAYLEIGH_JOB_SOCKET_COAGULATION_EXACT_REDUCTION_20260804.md`  
**Verdict:** **PASS**, with the existence of the coagulation kernel explicitly
left open.

## 1. Measure and workload identities

With `A=sqrt(pi)/2`, substitution `z=A+x` gives

\[
 \int_0^\infty2(A+x)e^{-(A+x)^2}\,dx=e^{-A^2}.
\]

Substitution `z=A-y` gives

\[
 \int_0^A2(A-y)e^{-(A-y)^2}\,dy=1-e^{-A^2}.
\]

Integration by parts gives

\[
 \int_0^\infty x\,\mu(dx)=\int_A^\infty e^{-z^2}\,dz
\]

and

\[
 \int_0^Ay\,\nu(dy)=A-\int_0^Ae^{-z^2}\,dz.
\]

These are equal exactly because
`A=int_0^infinity exp(-z^2) dz`.  Thus the zero-slack premise used in the
main theorem is exact.

## 2. Zero trimming

For a configuration with assigned amounts `z_i<=y_i`, the unused amount is
`sum_i(y_i-z_i)>=0`.  Its integral against a kernel with the declared two
marginals is

\[
 \int y\,d\nu-\int x\,d\mu=0.
\]

A nonnegative measurable function with integral zero vanishes almost
everywhere.  Hence `z_i=y_i` for every piece in almost every finite
configuration.  This validates the passage from the trimmed fragmentation
model to exact finite coagulation.

The aggregate piece count is

\[
 \int n\,d\rho=\nu(0,A)<\infty,
\]

so infinite groups have zero measure.  No hidden finite-cardinality
assumption is needed.

## 3. Uniform coordinate and centered-Rayleigh interpretation

For `y<A`, set `u=exp(-(A-y)^2)`.  Then

\[
 du=2(A-y)e^{-(A-y)^2}\,dy.
\]

On the job side `y=-x`, orientation reverses, and

\[
 \mu(dx)=-du,
 \qquad x=\sqrt{-\log u}-A,
 \qquad 0<u<e^{-A^2}.
\]

On the socket side

\[
 \nu(dy)=du,
 \qquad y=A-\sqrt{-\log u},
 \qquad e^{-A^2}<u<1.
\]

Thus the uniform-coordinate statement has the correct orientation and
normalization.

Equivalently, let `Z` have Rayleigh density `2z exp(-z^2)` on `z>0`.
Every exact socket group `w_1,...,w_n<A` paired with one job coordinate
`z>A` obeys

\[
 (z-A)=\sum_{i=1}^n(A-w_i)
 \quad\Longleftrightarrow\quad
 z+\sum_{i=1}^n w_i=(n+1)A.                         \tag{3.1}
\]

Therefore the open coagulation theorem is also exactly a decomposition of
the Rayleigh law into finite equal-weight blocks of arithmetic mean `A`,
each block containing one above-mean point and all remaining points below
the mean.  This is an equivalent reformulation, not an existence proof.

## 4. Fragment tails

Since every piece is `<A`, a job of size `x` needs at least `ceil(x/A)`
pieces.  Therefore

\[
 \rho\{N\ge n\}
 \ge\mu((n-1)A,\infty)
 =e^{-(A+(n-1)A)^2}=e^{-\pi n^2/4}.
\]

The difference of successive tails gives the displayed exact minimum-class
intensity.  Summing the tails gives the minimum count series.

For the strict count slack, the bound

\[
 n^2\ge4(n-1)\quad(n\ge2)
\]

implies

\[
 \sum_{n\ge1}q^{n^2}
 \le q+{q^4\over1-q^4},\qquad q=e^{-\pi/4}.
\]

The rational estimate in the theorem makes the latter strictly smaller
than `1-q`.  Hence the sign of `Delta_#` is correct.  Finally, the group
count and excess count identities follow directly by subtracting the two
total masses.

## 5. Scope audit

The note does **not** claim any of the following:

* existence of the exact coagulation measure;
* sufficiency of the displayed price inequalities without a cone-closedness
  proof;
* discrete or literal SCD rounding;
* containment Hall for a fixed pair of SCDs;
* an all-dimensional OR-word upper bound.

The reduction is therefore proof-safe.  Its precise unresolved row is the
equal-mean finite-block decomposition (3.1), or a separating exact
configuration price.
