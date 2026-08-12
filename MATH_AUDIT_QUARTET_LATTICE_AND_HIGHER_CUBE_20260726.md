# Audit of quartet-lattice saturation and the higher placeholder cube

Date: 2026-07-26

Sources audited:

* `MATH_THEOREM_QUARTET_RECTANGLE_LATTICE_SATURATION_AND_TEMPLATE_GATE_20260726.md`;
* `MATH_THEOREM_PROMOTION_ALL_DEPTH_HIGHER_CUBE_EXCHANGE_20260726.md`.

## 0. Verdict

The integral rectangle-saturation theorem is correct over the full range
\(2\le k\le N-2\).  Its annihilator calculation remains valid in every
characteristic, including primes dividing \(k\), and the maximal-minor
argument really proves saturation rather than merely rational equality.

The higher-cube column cancellation is also exact over the integers and
therefore in every characteristic.  Two scope corrections were needed in
its statement:

1. in general one needs
   \(2\le d\le\min\{M,N-M\}\), not only \(d\le N-M\), because the
   common core has size \(M-d\); and
2. phase deletion or stopping tags must use one common positional
   schedule at every cube corner and for both placeholder permutations.
   Equal tag counts with corner-dependent placements are not enough.

These corrections have been patched into the higher-cube source.  In the
critical regime \(N=2m,M=m+H\), the first correction changes nothing:
\(N-M=m-H<M\), so the advertised range \(2\le d\le m-H\) is correct.

## 1. Audit of the arbitrary-field annihilator

Suppose \(f:\binom\Omega k\to\mathbb F\) annihilates every rectangle.
For distinct \(x,y\), define

\[
 d_{xy}=f(B+y)-f(B+x),qquad
 B\in\binom{\Omega\setminus\{x,y\}}{k-1}.
\]

The Johnson graph on these \(B\)'s is connected because
\(1\le k-1\le N-3\).  Along an edge \(B=C+p,B'=C+q\), context
independence is exactly the rectangle on the four distinct labels
\(p,q,x,y\).  This argument uses no division and therefore survives
characteristic two.

For three distinct \(x,y,z\), a common \((k-1)\)-set disjoint from all
three exists even at the endpoint \(k=N-2\).  Telescoping gives

\[
 d_{xy}+d_{yz}=d_{xz}.
\]

Thus \(d_{xy}=\alpha_y-\alpha_x\), and connectedness of \(J(N,k)\)
gives

\[
 f(U)=c+\sum_{x\in U}\alpha_x.
\]

Conversely every such affine function annihilates a rectangle.  The
parameter kernel consists exactly of

\[
 \alpha_x=t\quad(x\in\Omega),\qquad c=-kt.
\]

This remains one-dimensional when the field characteristic divides
\(k\): then the condition simply reads \(c=0\), with \(t\) still free.
Hence the annihilator dimension is exactly \(N\) over every field, and
the rectangle rank is \(\binom Nk-N\) over every field.

## 2. Audit of integral saturation

Let \(R\) be an integer matrix listing the rectangle rows, and put
\(r=\binom Nk-N\).  The arbitrary-field result says

\[
 \operatorname{rank}_{\mathbb F_p}R=r
\]

for every prime \(p\), equal to its rational rank.  Therefore, for every
prime, some maximal \(r\)-minor is nonzero modulo \(p\).  No prime divides
the gcd of all maximal minors, so that gcd is one.  Smith normal form then
shows that the rectangle row lattice is saturated in its rational span.

Every rectangle has zero element margin.  The element-incidence matrix
\(A\) has rational row rank \(N\), so \(\ker_{\mathbb Z}A\) has the same
rank \(r\).  It is saturated because its quotient is
\(\operatorname{im}A\), a subgroup of a free abelian group.  Two
saturated sublattices of \(\mathbb Z^{\binom\Omega k}\) with the same
rational span both equal the intersection of that span with the ambient
integer lattice.  Therefore

\[
 \mathcal R=\ker_{\mathbb Z}A.
\]

No rational, modular, or torsion qualifier is missing.  This is a lattice
statement only: it does not give a nonnegative Markov basis or manufacture
the four compatible positional templates.

## 3. Audit of the higher-cube identity

Fix a positional interval.  Let \(K\subseteq[d]\) be the set of
placeholder *positions* it contains.  Under a placeholder permutation
\(\rho\), the labels visible in those positions form
\(J_\rho=\rho(K)\) (up to the harmless inverse convention).  The
ordinary-label subset \(B\subseteq C\) is independent of \(\rho\), and
at corner \(\epsilon\) the interval set is

\[
 B\cup\{a_{j,\epsilon_j}:j\in J_\rho\}.
\]

If \(J_\rho\ne[d]\), choose a missing coordinate \(h\).  The basis
vector is independent of \(\epsilon_h\), so pairing the two values of
\(\epsilon_h\) cancels the alternating cube sum.  If
\(J_\rho=[d]\), the interval contains all placeholder positions; its set
is

\[
 B\cup\{a_{1,\epsilon_1},\ldots,a_{d,\epsilon_d}\},
\]

independent of \(\rho\).  Since a permutation preserves the fixed set of
placeholder positions,

\[
 J_\sigma=[d]\iff J_\tau=[d].
\]

Thus the two alternating sums either both vanish or agree term by term.
This proves the claimed difference identity in the free abelian group on
actual interval sets, so it is stronger than a real-vector or
characteristic-specific identity.

At interval length zero, both variants give the empty set; at length
\(M\), both give the whole top \(U_\epsilon\).  Hence the identity extends
trivially to both boundary lengths, including the promotion top rank.

## 4. Exact exchange quantifiers

Let the old family contain the \(\sigma\)-frame at even corners and the
\(\tau\)-frame at odd corners, and let the new family reverse these
choices.  New minus old is the negative of the alternating identity, so
all interval loads are preserved.

Because the identity holds separately for every positional phase and
every interval length, it remains true after multiplying a column by an
arbitrary real coefficient \(w_{s,\ell}\) common to all corners and both
frame variants.  In particular it survives:

* a common retained-phase set;
* one common phase-to-depth stopping schedule;
* common deletion of specified phases; and
* any common real weighting of phase/length columns.

It does **not** imply cancellation for weights
\(w_{\epsilon,\rho,s,\ell}\) depending on the corner or frame variant.
Thus merely giving the corners the same tag histogram, but placing those
tags at different phases, is outside the theorem.

For promotion masks represented as direct intervals, the conclusion is
literal.  If a root convention represents a mask by the global complement
of a positional interval, global complementation is a fixed permutation
of the target basis and preserves the same identity.

## 5. Exact surviving scope

The two audited notes jointly prove:

1. every integral top-count redistribution preserving all element margins
   is an integral sum of abstract quartet rectangles;
2. whenever all \(2^d\) compatible positional cube corners are physically
   present, swapping two placeholder permutations in checkerboard parity
   is an exact legal frame exchange;
3. that exchange preserves every promotion depth simultaneously under one
   common positional stopping schedule; and
4. in the critical regime, cubes exist abstractly at every possible top
   distance \(2\le d\le m-H\).

Neither theorem proves that a given nonnegative frame table contains the
required templates, that the lattice decomposition can be ordered without
negative multiplicities, or that enough complete cubes occur to connect
the desired common-permutation fibre.  The remaining gate is physical
template abundance plus nonnegative connectivity, not another abelian
top-incidence invariant.
