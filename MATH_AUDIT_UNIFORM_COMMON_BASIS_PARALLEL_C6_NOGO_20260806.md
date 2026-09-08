# Audit of the parallel-\(C_6\) common-basis no-go

**Date:** 2026-08-06  
**Primary note:**  
MATH_THEOREM_UNIFORM_COMMON_BASIS_NEGATIVE_DEPENDENCE_AND_STAR_HALO_NOGO_20260806.md  
**Verdict:** PASS as an abstract two-matroid obstruction; Boolean-specific
scope retained.

## 1. Degree and base classification

At each left or right vertex the parallel-\(C_6\) gadget has \(a\) atoms
from one alternating bundle and \(b\) from the other, so its degree is
\(a+b=r\).

The underlying simple graph is one six-cycle.  A perfect matching must
choose either all three \(A\)-bundles or all three \(B\)-bundles.  Parallel
labels create independent copy choices but no third support pattern.

The common bases of the two endpoint partition matroids are exactly these
perfect matchings.

## 2. Uniform marginal replay

The prescribed distribution gives an \(A\)-atom probability

\[
 \frac ar\frac1a=\frac1r
\]

and a \(B\)-atom probability

\[
 \frac br\frac1b=\frac1r.
\]

There are \(3r\) atoms and every base has size three, so the global density
is also \(3/(3r)=1/r\).

For any distribution with these marginals, the \(A\)-orientation
probability is forced to be \(a/r\).  The sum of all \(a^2\) pair
probabilities across bundles \(A_0,A_1\) is therefore \(a/r\).  Pairwise
negative correlation would bound this sum by \(a^2/r^2\), which is smaller
because \(0<a<r\).  The negative-dependence contradiction is exact and
does not depend on the particular displayed distribution.

Strongly-Rayleigh measures are pairwise negatively correlated, so the
strongly-Rayleigh corollary is valid.

## 3. Cylinder and swap checks

The designated atoms

\[
 A_0^1=x_0y_0,\qquad B_1^1=x_1y_2
\]

have four distinct endpoints.  They are therefore independent in both
partition matroids.  They belong to opposite support orientations, so no
common base contains both.

For a one-element exchange from an \(A\)-base toward a \(B\)-base, the left
partition forces replacement of \(A_i\) by \(B_i\).  This repeats right
vertex \(y_{i+1}\) and leaves \(y_i\) uncovered.  Hence there is no
orientation-changing common symmetric exchange.  A three-edge move is
necessary.

## 4. Star-halo count

The four endpoints of the designated pair meet:

\[
 A_0,A_1,A_2,B_0,B_1,B_2.
\]

Thus they meet every one of the \(3r\) occurrence atoms.  Removing the two
designated atoms leaves exactly \(3r-2\) halo atoms.

Every perfect matching selects three atoms of one orientation and contains
at most one designated atom.  It therefore selects at least two halo atoms.
The \(d\)-fold direct sum gives

\[
 |D|=d(3r-2),\qquad |B\cap D|\ge2d.
\]

Uniform marginals give

\[
 \mathbb E|B\cap D|=|D|/r=3d-2d/r.
\]

All scaling claims in the primary note follow.

Since the four protected endpoints meet every bundle, \(E-D=I\) in the
direct sum.  Thus the maximum common-independent size outside \(D\) is
\(2d\), versus common rank \(3d\), proving the claimed generic
\(\Omega(d)\) deficiency.  The general upper bound follows by choosing a
base with at most the average \(p|D|\) collisions and deleting them.

## 5. Scope

The gadget uses labelled parallel occurrence atoms.  This is legitimate
for an abstract intersection of two partition matroids and is especially
natural for occurrence-labelled common-basis systems.  The note does not
assert that the strict Boolean SBE matroids contain this gadget as a minor.

Accordingly it proves:

* no generic upgrade from uniform common-base marginals to strong Rayleigh;
* no generic common-base swap-rounding theorem;
* no generic conditioning theorem for a clean common-independent bank;
* no generic \(O(1)\) star-halo collision theorem.

It does not prove:

* that the audited sharp-pivot bank is incompatible with the Boolean
  common-basis face;
* that a Boolean-specific protected minor cannot exist;
* that a prospective packet/common-basis co-selection cannot work; or
* any lower bound on \(\nu(k)\).

The next valid target is therefore Boolean-specific protected extension or
prospective co-selection, not a stronger probabilistic interpretation of
the already known uniform marginal point.
