# Independent audit: Rayleigh fragmentation convex order and configuration cuts

**Date:** 2026-08-04  
**Audited theorem:**  
MATH_THEOREM_RAYLEIGH_FRAGMENTATION_CONVEX_ORDER_AND_CONFIGURATION_CUT_20260804.md

**Verdict:** PASS, with the theorem scoped exactly as written.  The
Rayleigh convex-order statement is unconditional.  The configuration-price
criterion is the exact fractional whole-job criterion with trimming.
The finite examples separate that criterion from scalar and threshold
relaxations.  They are abstract examples, not binomial-profile no-go
theorems.

## 1. Scaling normalization

For \(k=2r\) and \(b=r-z\sqrt r\),

\[
 { {2r\choose b}\over {2r\choose r}}\to e^{-z^2},
 \qquad
 {2r+1-2b\over2r+1-b}\sim {2z\over\sqrt r}.
\]

Therefore the two displayed limiting densities are

\[
 j(x)=2(A+x)e^{-(A+x)^2},\qquad
 s(y)=2(A-y)e^{-(A-y)^2}.
\]

Direct antiderivatives give

\[
 \int_0^\infty j=e^{-A^2},\qquad
 \int_0^A s=1-e^{-A^2}.
\]

Integration by parts gives

\[
 \int_0^\infty xj(x)\,dx=\int_A^\infty e^{-z^2}\,dz,
\]

and

\[
 \int_0^A ys(y)\,dy=A-\int_0^A e^{-z^2}\,dz.
\]

These agree precisely because \(A=\sqrt\pi/2\).  Thus the padded measures
really do have equal mass and first moment.

## 2. Convex-order direction

For

\[
 D(q)=\int\min(z,q)\,d(\nu-\widetilde\mu)(z),
\]

the derivative on \(0<q<A\) is

\[
 D'(q)=1-e^{-(A-q)^2}-e^{-(A+q)^2}.
\]

Writing

\[
 F(q)=2e^{-(A^2+q^2)}\cosh(2Aq)
\]

gives \(D'=1-F\), and

\[
 {d\over dq}\log F(q)=2(A\tanh(2Aq)-q).
\]

The inner function has strictly negative second derivative on the positive
axis, positive derivative at zero, and negative value at \(A\).  Hence
\(F\) is first increasing and then decreasing.  Since

\[
 F(0)=2e^{-\pi/4}<1,\qquad
 F(A)=1+e^{-\pi}>1,
\]

there is exactly one crossing of one on \((0,A)\).  Consequently \(D\)
first increases and then decreases there.  The endpoint identities

\[
 D(0)=0,\qquad
 D(A)=\int_A^\infty(x-A)\,d\mu(x)>0
\]

prove \(D\ge0\) on \([0,A]\).  Above \(A\), \(D'<0\) and \(D\) tends to
zero.  The convex-order direction in the theorem is therefore correct:
the socket measure is the less dispersed measure.

For a concave \(\phi\) with \(\phi(0)=0\), the two elementary concavity
inequalities at \(x/(x+y)\) and \(y/(x+y)\) add to
\(\phi(x+y)\le\phi(x)+\phi(y)\).  Thus the stated concave/subadditive
consequence has the correct direction.

## 3. Configuration polyhedron

For a capacity multiset \(p\), a positive integer load \(l\) can be
distributed over those sockets exactly when

\[
 |p|\le l\le\sum_u u p_u.
\]

Necessity is immediate.  For sufficiency, put one unit in every selected
socket and add the remaining units one at a time; the available additional
room is \(\sum_u(u-1)p_u\).  Hence the pattern set in the theorem is exact.

Let \(C\) be the convex set of aggregate usage vectors obtained after
choosing one pattern per job.  Feasibility is \(m\in C+\mathbb R_+^d\).
A separating functional bounded below on this upper-closed set must be
nonnegative.  Its minimum over \(C\) separates over jobs, giving exactly

\[
 \sum_l n_l\min_{p\in\mathcal Q_l}\theta\cdot p
 \le\theta\cdot m.
\]

The sign and quantifiers of Theorem 3.1 are correct.  No integrality of the
configuration matrix is used or claimed.

## 4. First finite separator

For capacities \(6,6,3,3,2\), price capacities 6, 3, 2 by 2, 1, 1.
Any pattern of total capacity at least ten having price at most three can
contain:

* no 6-socket, in which case its capacity is at most \(3+3+3=9\); or
* one 6-socket, in which case its remaining price is at most one and its
  capacity is at most \(6+3=9\).

Thus every 10-pattern costs at least four.  Two jobs cost at least eight,
whereas all sockets cost

\[
 2\cdot2+2\cdot1+1\cdot1=7.
\]

This validates the configuration-price certificate under the theorem's
trimming convention.  Separately, the declared exact fragment vector
\((6,6,3,3,2)\) has no subset of sum ten, while its partial sums are
majorized by \((10,10,0,0,0)\).  Hence the claimed Lorenz-versus-grouping
separation is genuine.

## 5. Uniform plus-one separator

The base capacities \(7,7,7,1\) have total 22, equal to two jobs of length
11.  Raising every capacity by one gives \(8,8,8,2\), total 26.

With prices \(\theta_8=2,\theta_2=1\), any pattern of price at most three
has either no 8-socket and capacity at most six, or one 8-socket and
capacity at most ten.  Therefore every 11-pattern costs at least four.
For \(m\) copies, demand costs at least \(8m\), while supply costs \(7m\).

The direct deficiency calculation is also valid.  If \(A,B,C\) jobs use
respectively at least two, exactly one, or zero 8-sockets, then

\[
 2A+B\le3m,\qquad 2B+6C\le m.
\]

Maximizing \(A+B+C\) under these inequalities gives at most \(7m/4\).
Thus the obstruction remains linear after a uniform one-unit increase.

The anonymous proposed fragments \(8,8,4,2\) have load 22 and fit into
\(8,8,8,2\), so the receiving threshold relaxation sees no problem.
The theorem correctly concludes only that scalar or uniform-plus-one
capacity is not a generic configuration-rounding principle.  It does not
assert that the smooth binomial/Rayleigh capacities have this obstruction.

## 6. Final scope

The theorem closes the Gaussian Lorenz gate and exposes the exact
nonconcave configuration gate.  It does not construct the required
chain-dependent SCD composition, prove all configuration-price inequalities
for the binomial profile, round the fractional configuration system
integrally, or address literal containment Hall.
