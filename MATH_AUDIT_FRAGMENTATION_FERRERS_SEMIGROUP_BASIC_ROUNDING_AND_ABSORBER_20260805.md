# Self-audit: Ferrers fragmentation, basic rounding, and the universal absorber

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`  
**Method:** independent line-by-line algebraic replay inside the same pure
mathematical lane; no computation, search, or solver  
**Verdict:** SELF-GO at the stated conditional scope.  No conclusion about
fractional feasibility or physical exposure of the absorber is made.

## 1. Ferrers conjugation

For pieces of lengths at most `D`, the conjugate vector

\[
                         z_q=\#\{\ell:\ell\ge q\}
\]

is an integer partition and

\[
                         \sum_qz_q=\sum_\ell\ell.
\]

Conversely `w_q=z_q-z_(q+1)` recovers `w_q` pieces of exact length `q`,
and telescoping gives `sum_q q w_q=sum_q z_q`.  Aggregate coordinate `q`
is exactly the number of pieces requiring a socket of capacity at least
`q`.  The sorted matching criterion therefore proves Theorem 1.1 in both
directions, including injectivity of socket use.

The warning about the naive real slice is correct: for `L=1,D=2`, its
constraints reduce to `z_1+z_2=1,z_1>=z_2>=0`, whose endpoint
`(1/2,1/2)` is fractional.

## 2. Extreme-point support count

There is one equality per job and at most `D` active socket inequalities.
On the positive support of an extreme point, more than `N+D` columns would
be linearly dependent while preserving every active row.  Since every
inactive inequality has positive slack, a sufficiently small perturbation
in both signs remains feasible.  Thus support size is at most `N+D`.

If `f_a` is the number of positive configurations of job `a`, then

\[
                         \sum_a(f_a-1)=s-N\le D.
\]

Every job with `f_a=1` has coefficient one, so those configurations are
literally integral.  Their resource use is a coordinatewise subvector of
the feasible fractional use.  This verifies Theorem 2.1.  Degeneracy can
only reduce support and causes no exception.

## 3. Absorber arithmetic

For one job, Euclidean division `L=qD+r` uses `q` maximal sockets when
`r=0`, and `q+1` maximal sockets when `r>0`; the last socket is simply
trimmed to load `r`.  Thus at most `ceil(L_max/D)` maximal sockets per job
are sufficient.  The absorber is disjoint from the original sockets, so it
does not matter which original socket types the fractional residual jobs
had used.  This verifies Lemma 3.1 and Theorem 3.2.

At `h=D`, the socket count is

\[
 D\lceil L_{\max}/D\rceil,
\]

which is (3.4).  Its capacity is

\[
 D^2\lceil L_{\max}/D\rceil,
\]

which is (3.5).  With `D=Theta(sqrt(k))` and
`L_max=O(k)`, these are respectively `O(k)` and `O(k^(3/2))`.

## 4. Scope audit

The proof does **not** establish any of the following:

1. the all-price fractional configuration inequalities for the binomial
   job/socket profile;
2. an integral packing into the unaugmented socket vector;
3. that the one-each triangular sockets dominate the absorber;
4. that one extra physical word position exposes the required exact-type,
   occurrence-disjoint sockets;
5. named Boolean containment, run serialization, upper coverage, or
   topology.

The first two theorem sections are exact for arbitrary finite integer data.
The absorber theorem is conditional on genuinely adjoining its socket
multiset.  The final section states rather than suppresses the missing
physical exposure bridge.  **SELF-GO.**
