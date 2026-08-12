# Uniform common-basis marginals do not imply negative dependence or constant star-halo loss

**Date:** 2026-08-06  
**Method:** an explicit parallel-\(C_6\) intersection of two partition
matroids  
**Status:** unconditional abstract no-go theorem at the exact
\(p=\Theta(1/r)\), \(|D|=\Theta(rd)\) scale of the protected Catalan host.
It does not refute a Boolean-specific protected common-basis theorem.

## 0. Outcome

The synchronized common-basis theorem supplies a distribution with uniform
one-element marginals

\[
                         \Pr(e\in B)=p=\Theta(1/r).
\tag{0.1}
\]

This fact cannot, in general, be upgraded to any of the following:

1. a pairwise negatively correlated or strongly-Rayleigh distribution with
   the same marginals;
2. a one-element common-base swap process suitable for ordinary swap
   rounding;
3. positive cylinder mass for every clean prescribed common-independent
   set;
4. a common base meeting a \(\Theta(rd)\) endpoint-star halo in only
   \(O(1)\) elements.

All four failures already occur for the common bases of two partition
matroids.  For every \(r\ge2\) and every \(d\ge1\), there is such an
instance with a uniform-marginal common-base distribution of marginal
\(1/r\), a prescribed common-independent matching \(I\) of size \(2d\),
and a star halo \(D\) of size

\[
                         |D|=d(3r-2)
\tag{0.2}
\]

such that

\[
                         I\not\subseteq B
                         \quad\hbox{and}\quad
                         |B\cap D|\ge2d
\tag{0.3}
\]

for every common base \(B\).

Thus neither negative dependence nor swap rounding can turn the existing
uniform marginals into the \(O(1)\)-collision protected Catalan certificate.
A successful proof must use additional Boolean incidence structure,
contract a jointly extendable protected bank, or select the sharp-pivot
packets and the common basis prospectively.

## 1. One parallel-\(C_6\) gadget

Fix positive integers \(a,b\) with

\[
                         a+b=r.
\tag{1.1}
\]

Let the left vertices be \(x_0,x_1,x_2\), the right vertices be
\(y_0,y_1,y_2\), with indices modulo three.  Use two alternating edge
orbits:

\[
\begin{aligned}
 A_i&=x_i y_i,\\
 B_i&=x_i y_{i+1}.
\end{aligned}
\tag{1.2}
\]

Replace every \(A_i\) by \(a\) labelled parallel occurrence atoms
\(A_i^1,\ldots,A_i^a\), and every \(B_i\) by \(b\) labelled parallel
occurrence atoms \(B_i^1,\ldots,B_i^b\).

Let \(\mathcal M_L\) be the partition matroid that permits at most one atom
at each left vertex, and let \(\mathcal M_R\) be the analogous partition
matroid on right vertices.  Their common bases are precisely the perfect
matchings of this occurrence-labelled bipartite multigraph.

### Lemma 1.1

Every common base has exactly one of the two forms

\[
 \{A_0^{u_0},A_1^{u_1},A_2^{u_2}\}
\quad\hbox{or}\quad
 \{B_0^{v_0},B_1^{v_1},B_2^{v_2}\}.
\tag{1.3}
\]

### Proof

After parallel copies are forgotten, the support graph is a six-cycle.
It has exactly its two alternating perfect matchings.  Restoring labels
allows an arbitrary copy choice in each of the three selected bundles and
no other possibility.  \(\square\)

## 2. Exact uniform marginals

Define a common-base distribution as follows:

* choose the \(A\)-orientation with probability \(a/r\), then independently
  choose one of the \(a\) copies in each \(A_i\) bundle;
* choose the \(B\)-orientation with probability \(b/r\), then independently
  choose one of the \(b\) copies in each \(B_i\) bundle.

### Lemma 2.1

Every occurrence atom has marginal exactly \(1/r\).

### Proof

For an \(A\)-atom,

\[
 \Pr(A_i^u\in B)=\frac ar\frac1a=\frac1r.
\]

The \(B\)-calculation is identical.  \(\square\)

Thus the common point

\[
                         (1/r,\ldots,1/r)
\tag{2.1}
\]

lies in the common-base polytope exactly as in the synchronized
common-basis theorem.

## 3. No negatively correlated uniform-marginal distribution exists

The preceding distribution is not merely an unfortunate convex
decomposition.  No distribution on all common bases of the gadget can
have both the marginals \(1/r\) and pairwise negative correlation.

### Theorem 3.1

Let \(\mu\) be any distribution on the common bases satisfying

\[
                         \Pr_\mu(e\in B)=1/r
\tag{3.1}
\]

for every occurrence atom.  Then some pair of distinct atoms \(e,f\)
satisfies

\[
                         \Pr_\mu(e,f\in B)>
                         \Pr_\mu(e\in B)\Pr_\mu(f\in B).
\tag{3.2}
\]

Consequently no such distribution is strongly Rayleigh.

### Proof

Summing (3.1) over the \(a\) copies of the bundle \(A_0\) gives

\[
                         \Pr_\mu(B\hbox{ has }A
                         \hbox{ orientation})=a/r.
\tag{3.3}
\]

Whenever the \(A\)-orientation is chosen, exactly one atom from \(A_0\)
and one from \(A_1\) are selected.  Therefore

\[
 \sum_{u=1}^a\sum_{v=1}^a
 \Pr_\mu(A_0^u,A_1^v\in B)=a/r.
\tag{3.4}
\]

If every pair in (3.4) were negatively correlated, each summand would be
at most \(1/r^2\), so the left side would be at most \(a^2/r^2\).
But

\[
                         \frac ar>\frac{a^2}{r^2}
\]

because \(a<r\).  This contradiction proves (3.2).  Strongly-Rayleigh
measures are pairwise negatively correlated, so none can have the stated
marginals on this support.  \(\square\)

Negative dependence is therefore not a formal consequence of a uniform
point in two matroid base polytopes.

## 4. Ordinary swap rounding cannot stay in the common-base family

Let \(B_A\) and \(B_B\) be common bases of the two orientations in (1.3).

### Proposition 4.1

There is no one-element symmetric exchange

\[
 B_A-e+f
\tag{4.1}
\]

which is a common base and has \(f\in B_B\).

### Proof

The left partition forces \(f\) to use the same left vertex as \(e\).
Thus replacing \(A_i\) requires an atom from \(B_i\).  But \(B_i\) meets
\(y_{i+1}\), whose \(A_{i+1}\)-atom is still present, and leaves \(y_i\)
unmatched.  Hence the right partition fails.  \(\square\)

Changing orientation requires the indispensable cubic exchange of all
three bundles.  The one-element common-base exchange graph has distinct
orientation components.  Standard matroid swap rounding relies on
one-element symmetric basis exchange inside one matroid base family and
therefore has no direct common-base implementation here.

## 5. A clean cylinder has probability zero

Choose the two occurrence atoms

\[
                         \alpha=A_0^1=x_0y_0,
\qquad
                         \beta=B_1^1=x_1y_2.
\tag{5.1}
\]

They have disjoint left and right endpoints.  Therefore

\[
                         I_1=\{\alpha,\beta\}
\tag{5.2}
\]

is independent in both partition matroids.

### Proposition 5.1

Every uniform-marginal distribution above satisfies

\[
 \Pr(\alpha\in B)=\Pr(\beta\in B)=1/r,
\qquad
 \Pr(\alpha,\beta\in B)=0.
\tag{5.3}
\]

In particular \(I_1\) is a clean common-independent set which does not
extend to a common base.

### Proof

The marginal statement is (3.1).  By Lemma 1.1 a common base uses one
orientation globally.  The two prescribed atoms have opposite
orientations, so no common base contains both.  \(\square\)

Thus conditioning the synchronized distribution on a prescribed clean
packet bank can be an empty event even when every prescribed atom has the
correct positive marginal and the prescribed set is independent in each
matroid separately.

## 6. The \(d\)-gadget star-halo obstruction

Take the direct sum of \(d\) disjoint copies of the gadget.  The two
matroids are the corresponding direct sums.  Use the product of the
distributions in Section 2.  Every ground atom still has marginal \(1/r\).

Let

\[
                         I=\bigcup_{g=1}^d I_1^{(g)}.
\tag{6.1}
\]

The \(2d\) designated atoms have pairwise disjoint endpoints, so \(I\) is a
matching and is independent in both matroids.

For one gadget, let \(D_g\) be every occurrence atom incident with an
endpoint of \(I_1^{(g)}\), except the two designated atoms themselves.
The four designated endpoints meet all six bundles of the underlying
six-cycle.  Hence

\[
                         |D_g|=3r-2.
\tag{6.2}
\]

Put

\[
                         D=\bigcup_{g=1}^dD_g.
\tag{6.3}
\]

### Theorem 6.1

For every common base \(B\),

\[
                         I\not\subseteq B,
\qquad
                         |B\cap D|\ge2d.
\tag{6.4}
\]

Moreover

\[
                         |D|=d(3r-2),
\qquad
                         \mathbb E|B\cap D|
                         =\frac{|D|}{r}
                         =3d-\frac{2d}{r}.
\tag{6.5}
\]

### Proof

In each gadget a common base chooses exactly three atoms of one
orientation.  It contains at most one of the two oppositely oriented
designated atoms.  The other two selected atoms, and possibly all three,
belong to \(D_g\).  Thus every gadget contributes at least two halo
collisions and cannot contain its prescribed pair.  Summing gives (6.4).

Equation (6.2) gives the cardinality in (6.5).  Uniform marginals and
linearity of expectation give its expectation.  \(\square\)

Taking \(d=\Theta(\sqrt r)\) reproduces exactly the protected-host scale:

\[
 |I|=\Theta(\sqrt r),\qquad
 |D|=\Theta(r^{3/2}),\qquad
 \min_B|B\cap D|=\Omega(\sqrt r).
\tag{6.6}
\]

No choice of distribution, negative dependence, or rounding algorithm can
produce \(O(1)\) collisions in this instance because the lower bound holds
for every common base.

### Corollary 6.2 (the best generic marginal bound is order \(d\))

Let any common-base family have a distribution with constant marginal
\(p\), and let \(D\) be fixed.  There is a common independent set
\(J\subseteq E-D\) with

\[
 |J|\ge C-\lfloor p|D|\rfloor,
\tag{6.7}
\]

where \(C\) is the common-base size.

At the endpoint-star scale

\[
 p=\Theta(1/r),\qquad |D|=\Theta(rd),
\]

this gives defect \(O(d)\).  In the direct-sum construction the only atoms
outside \(D\) are the \(2d\) members of \(I\), whereas the common-base rank
is \(3d\).  Hence every common independent set avoiding \(D\) has defect at
least \(d\), so the order \(d\) cannot be improved under the generic
hypotheses.

### Proof

Linearity of expectation gives a common base \(B\) with

\[
 |B\cap D|\le\lfloor p|D|\rfloor.
\]

Delete \(B\cap D\).  The remainder is independent in both matroids,
avoids \(D\), and has the size in (6.7).

In the direct-sum example \(E-D=I\) and \(|I|=2d\), while every common base
has size \(3d\).  Thus even the largest common independent set avoiding
\(D\) has deficiency \(d\).
\(\square\)

This corollary does not retain the prescribed set \(I\): Theorem 5.1 shows
that \(I\) may have no common-base extension at all.  It is therefore an
unconditioned \(O(d)\)-defect theorem, not a protected-host theorem.

## 7. Consequence for ordered connector rank

The protected Catalan target asks simultaneously for

1. \(O(1)\) endpoint-star collisions; and
2. ordered free-port connector deficiency \(O(1)\).

Theorem 6.1 already fails the first row before a connector graph is
defined.  Therefore no theorem whose hypotheses are only

\[
 \text{two matroids}
 +\text{ a common uniform point}
 +\text{ a clean }O(d)\text{ common-independent bank}
\tag{7.1}
\]

can imply the desired two-row conclusion.

Ordered connector rank is also adaptive: its port graph is defined only
after the common basis and its path components are selected.  It is not an
additive element cost to which one-point marginal averaging applies.
Negative association of the selected ground elements, even if available,
would give no lower bound on this post-selection graphic/ordered-Hall rank.

## 8. Correct positive target

The no-go is abstract.  It does not prove that the Boolean SBE common-base
family contains a parallel-\(C_6\) obstruction, nor that the prospective
sharp-pivot bank is incompatible.

It changes the next theorem in a load-bearing way.  One must prove a
Boolean-specific statement of one of the following forms:

1. **protected minor extension:** the complete prescribed packet bank is
   jointly extendable, and after contracting it the two strict matroids
   retain a common base with controlled port rank;
2. **prospective co-selection:** choose the packet labels from a common
   basis and connector state rather than fixing them first;
3. **higher-degree common exchange:** exhibit literal common
   \(C_6/C_8\)-type exchanges which remove all but \(O(1)\) star collisions
   while increasing or preserving ordered connector rank.

Uniform marginals alone, even supplemented by a hypothetical
strongly-Rayleigh upgrade, are insufficient at the required scale.
