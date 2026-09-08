# The endpoint-critical first physical row is an exact tropical cubic

**Date:** 2026-08-12
**Method:** pure mathematics; literal min-plus Bellman recursion and a
first-crossing collapse
**Status:** unconditional.  The first carry row is determined exactly by
the displayed endpoint table through a three-part min-plus convolution.
Equivalently, its inverse discrepancy is the tropical cubic convolution of
the head inverse discrepancy.  This is strictly stronger than the formerly
retained sublevel/sumset laws.  It reduces the two-block covariance to one
integer staircase profile and proves a late-phase saturation law for every
minimizer.  It does **not** prove the covariance is nonnegative.

## 1. Endpoint-critical Bellman data

Fix an integer \(n\ge2\).  Let

\[
 0=v_0\le v_1\le\cdots\le v_n=1
\tag{1.1}
\]

be internally superadditive,

\[
 v_{i+j}\ge v_i+v_j\qquad(i,j\ge0,\ i+j\le n),
\tag{1.2}
\]

and endpoint-critical,

\[
 v_j\le {j\over n}\qquad(0\le j\le n).
\tag{1.3}
\]

The strict form has \(v_j<j/n\) for \(0<j<n\), but none of the results
below needs strictness.  Let

\[
 L(m)=\max_{\substack{x_1,\ldots,x_n\in\mathbb Z_{\ge0}\\
                       \sum jx_j=m}}
             \sum_{j=1}^n v_jx_j
\tag{1.4}
\]

be the literal max-plus Bellman clock, and put

\[
 p_r=L(n+r)-1\qquad(0\le r\le n).
\tag{1.5}
\]

For \(m\le n\), repeated use of (1.2) gives

\[
 L(m)=v_m.
\tag{1.6}
\]

## 2. A first crossing uses at most three displayed parts

### Theorem 2.1 (three-part first-crossing normal form)

For every \(0\le r<n\),

\[
\boxed{
 p_r=\max\left\{
 v_r,
 \max_{\substack{a,b,c\in\{0,\ldots,n-1\}\\a+b+c=n+r}}
       \bigl(v_a+v_b+v_c-1\bigr)
 \right\}.}
\tag{2.1}
\]

Thus the complete first physical row is a tropical cubic in the literal
head values.  Binary first-wrap formulas are, in general, only a proper
subfamily of (2.1).

#### Proof

Consider a partition of \(n+r<2n\).

If it uses a part of size \(n\), it uses exactly one such part.  All
remaining parts have total size \(r<n\), and (1.2) collapses them to the
single displayed part \(r\) without decreasing reward.  This gives the
term \(1+v_r\).

Suppose it uses no size-\(n\) part.  Order its parts arbitrarily, and stop
immediately before the first part which makes the running total at least
\(n\).  Let \(a<n\) be the total before that part, let \(b<n\) be that
part, and let \(c\) be the remaining total.  Since \(a+b\ge n\) and the
whole total is \(n+r<2n\), one has \(0\le c<n\).  Repeated use of (1.2)
collapses the prefix to part \(a\) and the suffix to part \(c\), without
decreasing reward.  We have therefore obtained a three-part partition
with

\[
 a+b+c=n+r.
\]

Conversely every term displayed in (2.1) is a literal partition of
\(n+r\).  Hence no partition outside the displayed family can improve the
maximum.  Subtracting the endpoint reward one proves (2.1). \(\square\)

In reduced-cost coordinates

\[
 e_j={j\over n}-v_j,
 \qquad
 f_r={r\over n}-p_r,
\tag{2.2}
\]

the same identity is

\[
\boxed{
 f_r=\min\left\{
 e_r,
 \min_{\substack{a,b,c<n\\a+b+c=n+r}}
       (e_a+e_b+e_c)
 \right\}.}
\tag{2.3}
\]

This retains the literal finite-availability constraint: the three sizes
sum to \(n+r\), not merely to residue \(r\) modulo \(n\).

## 3. Exact inverse tropical cubic

For \(0\le x\le1\), define the left inverse of the displayed head by

\[
 C_0(x)=\min\{0\le j\le n:v_j\ge x\},
 \qquad U_0(x)=C_0(x)-nx.
\tag{3.1}
\]

For \(0\le z\le1\), define

\[
 C_1(z)=\min\{0\le r\le n:p_r\ge z\},
 \qquad U_1(z)=C_1(z)-nz.
\tag{3.2}
\]

Endpoint conventions at finitely many phase atoms do not affect any later
integral.

### Theorem 3.1 (exact inverse cubic law)

For \(0<z<1\),

\[
\boxed{
 n+C_1(z)=
 \min_{\substack{x_1,x_2,x_3\in[0,1]\\
                  x_1+x_2+x_3\ge1+z}}
       \bigl(C_0(x_1)+C_0(x_2)+C_0(x_3)\bigr).}
\tag{3.3}
\]

Equivalently,

\[
\boxed{
 U_1(z)=
 \min_{\substack{x_1,x_2,x_3\in[0,1]\\
                  x_1+x_2+x_3\ge1+z}}
 \left\{
   \sum_{i=1}^3U_0(x_i)
   +n\left(\sum_{i=1}^3x_i-1-z\right)
 \right\}.}
\tag{3.4}
\]

#### Proof

Let

\[
 C(t)=\min\{m\ge0:L(m)\ge t\}.
\]

Density (1.3) gives \(L(m)\le m/n\), so \(C(1+z)>n\).  The partition
consisting of one endpoint part and a head witness for \(z\) gives

\[
 C(1+z)\le n+C_0(z)\le2n.
\tag{3.5}
\]

For any triple \((x_1,x_2,x_3)\) in (3.3), use the three literal parts
of sizes \(C_0(x_i)\).  Their reward is at least \(1+z\).  Hence

\[
 C(1+z)\le \sum_iC_0(x_i).
\tag{3.6}
\]

Conversely, take a maximizing partition at the first hitting index
\(C(1+z)\).  If that index is below \(2n\), the first-crossing argument in
Theorem 2.1 collapses it without reward loss to at most three displayed
parts \(a_1,a_2,a_3\), whose rewards sum to at least \(1+z\).  If the
index is \(2n\), use the three-part certificate \((n,n,0)\).  Taking
\(x_i=v_{a_i}\) gives in either case

\[
 \sum_i C_0(x_i)\le\sum_i a_i=C(1+z).
\tag{3.7}
\]

Together (3.6)--(3.7) prove equality.  Finally

\[
 C(1+z)=n+C_1(z)
\]

by (1.5).  Substituting \(C_0(x)=nx+U_0(x)\) gives (3.4). \(\square\)

This supplies, for example, the pointwise bounds

\[
\boxed{
 U_1(z)\le
 \min\left\{
 U_0(z),
 2U_0\!\left({1+z\over2}\right),
 3U_0\!\left({1+z\over3}\right)
 \right\}.}
\tag{3.8}
\]

The first choice uses \((1,z,0)\), the second two equal parts and a zero
part, and the third three equal parts.  More generally (3.4) retains every
unequal three-part transport, which is essential in a sharp argument.

### Corollary 3.2 (one-dimensional integral saturation)

Every first-row hitting event has a literal certificate using at most three
head denominations.  No rational mixing, stabilized residue walk, or
conductor passage is needed.  In particular the scalar first-row
owner-to-carry signature lies in the degree-three integer semigroup of the
literal head signatures, not merely in its rational cone.

This is an actual lattice/integrality statement, but only for the scalar
Bellman chronology.  It does not identify named Boolean targets or provide
disjoint occurrence packets.

## 4. The covariance is now a one-profile functional

Put

\[
 a={\pi\over4},\qquad f(x)=e^{-ax^2},
\]

\[
 B(y)=f(1-y)+f(1+y),
 \qquad
 H_2(y)=\sum_{\ell\ge2}f(\ell+y).
\tag{4.1}
\]

The first-row covariance reduction gives

\[
 \mathcal Q(v)
 =\int_0^1\bigl(U_0(z)B'(z)+U_1(z)H_2'(z)\bigr)\,dz.
\tag{4.2}
\]

Define the tropical cubic operator \(\mathcal T_n\) by the right side of
(3.4).  Theorem 3.1 turns (4.2) into the exact one-profile identity

\[
\boxed{
 \mathcal Q(v)=
 \int_0^1
 \left[U_0(z)B'(z)+(\mathcal T_nU_0)(z)H_2'(z)\right]dz.}
\tag{4.3}
\]

Because \(H_2'<0\), every explicit admissible triple in (3.4) gives a
proof-safe lower bound on \(\mathcal Q\).  Thus the former two-profile
covariance target has been reduced to a signed transport inequality for
one integer subadditive staircase.  A proof using only the distributions
of \(U_0,U_1\) discards the exact minimum in (3.4) and is strictly weaker.

## 5. Late phases of a minimizing table are constraint-saturated

Let \(\theta\in(0,1)\) be the unique interior zero of \(B'\).  Equivalently,
\(A\theta\) is the unique compact minimum of the Rayleigh kernel.  Hence

\[
 B'(y)<0\qquad(\theta<y<1).
\tag{5.1}
\]

Let \(\mathcal P_n\) be the compact polytope of tables satisfying
(1.1)--(1.3), with weak endpoint criticality.  Define \(p\) by (2.1) and,
equivalently to (4.2), put

\[
 \mathcal Q(v)=n-\sum_{r=0}^{n-1}
       \bigl(B(v_r)+H_2(p_r)\bigr).
\tag{5.2a}
\]

The maximum in (2.1) is finite, so \(p\), and hence \(\mathcal Q\), is
continuous on \(\mathcal P_n\).  Therefore \(\mathcal Q\) has a minimizer
there.

### Theorem 5.1 (late-phase downward saturation)

Let \(v\) minimize \(\mathcal Q\) on \(\mathcal P_n\).  If
\(0<j<n\) and \(v_j>\theta\), then at least one of the following exact
relations holds:

\[
\boxed{
 v_j=v_{j-1}
 \quad\hbox{or}\quad
 v_j=v_i+v_{j-i}\text{ for some }1\le i<j.}
\tag{5.2}
\]

#### Proof

Suppose neither relation holds.  Then \(v_j\) may be decreased by a
sufficiently small \(\varepsilon>0\) while preserving monotonicity and
every inequality in which \(v_j\) is the left side.  Inequalities in which
\(v_j\) is on the right only become weaker; the density upper bound also
remains valid.  Thus the perturbed table remains in \(\mathcal P_n\).

The direct contribution \(-B(v_j)\) strictly decreases, because
\(B'(v_j)<0\).  Formula (2.1) shows that every \(p_r\) is coordinatewise
nondecreasing in every \(v_j\); hence decreasing \(v_j\) cannot increase
any \(p_r\).  Since \(H_2\) is strictly decreasing, every contribution
\(-H_2(p_r)\) is nonincreasing.  Therefore \(\mathcal Q\) strictly
decreases, contradicting minimality. \(\square\)

For a strictly increasing minimizing table, every phase above \(\theta\)
therefore has an integral additive decomposition into earlier phases.
Recursively expanding these equalities gives a rooted literal additive
tree.  With plateaux allowed, every maximal late plateau is pinned either
at its left boundary or by such an additive equality.  This is the exact
finite-support staircase to which any extremal covariance argument may be
restricted.

There is a complementary, slightly less rigid statement below the compact
minimum.

### Theorem 5.2 (early-phase upward saturation)

Let \(v\) minimize \(\mathcal Q\) on \(\mathcal P_n\).  If
\(0<j<n\) and \(v_j<\theta\), then at least one of the following holds:

1. \(v_j=v_{j+1}\);
2. \(v_j=j/n\);
3. \(v_{j+i}=v_j+v_i\) for some \(1\le i\le n-j\); or
4. the coordinate \(v_j\) occurs with positive multiplicity in one of the
   expressions attaining the finite maximum (2.1) for some \(p_r\).

#### Proof

If none holds, increase \(v_j\) by a sufficiently small positive
\(\varepsilon\).  Conditions 1--3 being absent give positive slack in
monotonicity, density, and every superadditivity inequality in which
\(v_j\) occurs on the right.  Inequalities in which it is the left side
are relaxed.  Because the family of expressions in (2.1) is finite and no
maximizer uses \(v_j\), condition 4 being absent gives a positive gap to
every expression which does; hence all \(p_r\) remain unchanged for small
enough \(\varepsilon\).

The function \(B\) is strictly increasing on \([0,\theta]\) (although its
right derivative vanishes at zero).  Hence the direct term \(-B(v_j)\)
strictly decreases, while the tail terms do not change.  This contradicts
minimality.
\(\square\)

Thus a minimizing table is finite-combinatorial on both sides of the
Rayleigh minimum: late phases lie on literal additive/plateau faces, while
an early phase lies on a monotonicity, density, outgoing-additivity, or
active tropical-cubic face.

## 6. What remains

The physical first-row covariance conjecture is now the following single
statement:

> For every integer inverse staircase \(U_0\) arising from
> \(\mathcal P_n\), the one-profile functional (4.3) is nonnegative.

The new information unavailable to a sublevel-only proof is the exact
tropical cubic (3.4), together with the two-sided saturation in Theorems
5.1--5.2.  A counterexample, if one exists, may be chosen as a compact
minimizer lying entirely on this finite arrangement of literal Bellman
faces; in particular its post-minimum region is an additive staircase.

Even a proof of (4.3) would close only the analytic whole-job scalar.  The
all-\(k\) OR-word theorem still requires occurrence-labelled packet
rounding, topology, and a common-cap router.  Corollary 3.2 supplies a
one-dimensional degree-three lattice fact relevant to that rounding, not
the missing multidimensional packet saturation theorem.
