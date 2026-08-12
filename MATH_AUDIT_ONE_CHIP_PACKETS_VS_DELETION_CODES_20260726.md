# Audit: one-chip packets versus constant-weight deletion codes

Date: 2026-07-26

## 0. Verdict

The internal one-chip construction in
`MATH_THEOREM_ALL_FORM_ONE_CHIP_VOLTAGE_PACKETS_20260726.md` is sound:
the successor identity, packet length, voltage, vertex degree, phase
resolution, and periodic-parent estimate all check.

The coding-theory interpretation needs two corrections.

1. The packet problem is a **cyclic zero-insertion packing** (equivalently,
   an upward-star packing in a quotient of a discrete simplex).  It is not
   the ordinary rooted constant-weight single-deletion problem to which the
   modified VT coloring is applied.
2. In fact no packet matching covers more than
   \((1/2+o(1))T\) odd form classes.  The phase matching in the packet
   note is asymptotically optimal.  Thus both the perfect and near-perfect
   one-chip packet branches are impossible.

In particular, the modified VT construction of Cullina--Kulkarni--Kiyavash
does **not** imply a near-perfect matching after cyclic quotienting.  The
correct asymptotic answer for this packet catalogue is one half, not one.

Primary source checked:
[Cullina--Kulkarni--Kiyavash, arXiv:1211.4056](https://arxiv.org/abs/1211.4056).

## 1. Audit of the packet theorem

Put (n=2m+1).  If (z=(z_1,\ldots,z_m)) is a positive
composition of (2m), then

\[
 \iota(z)=(z_1,\ldots,z_{m-1},z_m+1),
 \qquad
 \Phi(\iota(z))=\iota(Rz).
\]

Thus a parent of least rotation period (r\mid m) produces (r) distinct
odd form classes.  The voltage is the sum of one period of (z), namely
(2r), and

\[
 \gcd(2m+1,2r)=1
\]

because (r\mid m) and (2m+1) is odd.  Hence the physical lift is one
component of length ((2m+1)r).

For

\[
 \kappa(d)=\sum_{i=1}^m i d_i\pmod m,
\]

direct calculation gives

\[
 \kappa(Rd)-\kappa(d)\equiv-1,
 \qquad
 \kappa(\Phi(d))=\kappa(d).
\]

This proves distinctness of the child form classes and the phase matching.
The degree formula

\[
 \deg(F)=s(F):=\#\{i:d_i\ge2\}
\]

then follows by lowering each active coordinate.  Writing (d_i=1+y_i)
gives the exact Narayana distribution

\[
 V_s={1\over m}\binom ms\binom m{s-1},
 \qquad
 \sum_s sV_s={m+1\over2}T.
\]

Finally, a proper period (r<m) satisfies (r\le m/2), so the number of
periodic parents is at most (2^{m+o(m)}=e^{-\Omega(m)}T).  These parts of
the note require no correction.

## 2. The exact channel represented by the packet hypergraph

Subtract one from every positive gap.  A rooted even parent becomes

\[
 x=(x_1,\ldots,x_m)\in\Delta_m(m)
 :=\{x\in\mathbb Z_{\ge0}^m:\sum_i x_i=m\},
\]

and a rooted odd child becomes (u\in\Delta_m(m+1)).  The rooted
zero-insertion sphere of (x) is the upward star

\[
 U(x)=\{x+e_i:1\le i\le m\}.
\tag{2.1}
\]

Coordinate rotation acts on both simplex levels.  A packet is precisely
the quotient of (2.1) by this action.  Consequently two parent necklaces
conflict exactly when some rotations of their rooted gap words have a
common upward child.

This differs from the standard graph (L_{1,N,k}): its vertices are
*rooted linear binary strings* and adjacency means that the ordinary
single-deletion sets meet.  Even if one restricts to deletion of a zero,
passing to necklaces strengthens the conflict relation:

\[
 [x]\sim[y]
 \quad\Longleftrightarrow\quad
 D_0(R^a x)\cap D_0(R^b y)\ne\varnothing
 \text{ for some }a,b.
\tag{2.2}
\]

A code for one chosen pair of representatives does not imply (2.2)-
independence.

The safe terminology is therefore:

> a matching of packets is a cyclic constant-weight zero-insertion code;
> a near-perfect matching is an asymptotically perfect packing of the odd
> insertion-output layer.

Deletion correction and insertion correction have the same pairwise
conflict relation in the rooted model, but **perfect deletion covering**
and **perfect insertion covering** are different assertions because their
ambient output layers differ.

## 3. Why modified VT does not descend to necklaces

For rooted words of length (N=2m) and weight (m), the modified VT
coloring in arXiv:1211.4056 is

\[
 f(x)=\sum_{j=1}^{2m}j x_j\pmod{m+1}.
\tag{3.1}
\]

It is an optimal proper coloring of the ordinary constant-weight
single-deletion graph.  It is not rotation invariant.  For left rotation
(R),

\[
 f(Rx)-f(x)=2m x_1-m\equiv1-2x_1\pmod{m+1}.
\tag{3.2}
\]

Thus a color class does not define a code on necklaces.  Canonicalizing
one representative does not fix the problem, since a conflict can use
different rotations.

There is already a four-bit counterexample.  With (m=2),

\[
 x=1100,qquad y=0101
\]

both have modified VT color (0\pmod3).  But the rotation (Ry=1010)
and (x) both zero-delete to (110).  Hence the two necklaces conflict
in the packet hypergraph.

The phase κ in the packet note is the correct cyclic analogue.  In
simplex coordinates it is

\[
 \kappa(x)=\sum_{i=1}^m i x_i\pmod m.
\]

It is rotation invariant because ∑x_i=m.  If two parents of a child
(u) are (u-e_i) and (u-e_j), then their colors differ by
(j-i\not\equiv0\pmod m).  Hence κ is a proper (m)-coloring of the
cyclic conflict graph.  A child with every coordinate positive has all
(m) possible parents, giving an (m)-clique, so this coloring is
chromatically optimal.

This exactly explains the half-cover in the packet note: an optimal
coloring supplies explicit independent sets, but does not force a maximum
independent set or a near-perfect upper-star packing.  The cited paper
itself emphasizes the general distinction between optimal coloring and
maximum independent sets.

## 4. Exact perfect packet matchings do not exist for (m\ge3)

### Theorem 4.1

For every (m\ge3), the packet hypergraph \(\mathcal H_m\) has no perfect
matching.

### Proof

Suppose a quotient-perfect matching exists.  Lift every selected parent
necklace to all of its distinct coordinate rotations.  The odd level has
free coordinate-rotation action because

\[
 \gcd(m,m+1)=1.
\]

The quotient packet partition therefore lifts to a partition of
(\Delta_m(m+1)) by the rooted upward stars (U(x)).

Let (C\subseteq\Delta_m(m)) be the lifted parent set and put

\[
 F(X_1,\ldots,X_m)=\sum_{x\in C}X^x.
\]

The coefficient of (X^u) in
((X_1+\cdots+X_m)F) is exactly the number of selected parents
(u-e_i) of (u).  A star partition would therefore imply the polynomial
identity

\[
 (X_1+\cdots+X_m)F
 =h_{m+1}(X_1,\ldots,X_m),
\tag{4.1}
\]

where (h_{m+1}) is the complete homogeneous polynomial of degree
(m+1).

For odd (m\ge3), specialize

\[
 (X_1,X_2,X_3,\ldots)=(1,-1,0,\ldots).
\]

The left side of (4.1) vanishes, whereas

\[
 h_{m+1}(1,-1)=\sum_{j=0}^{m+1}(-1)^j=1
\]

because (m+1) is even.

For even (m\ge4), put (d=m+1) and specialize

\[
 (X_1,X_2,X_3,X_4,\ldots)=(1,1,-2,0,\ldots).
\]

Again the linear factor vanishes, while

\[
 \begin{aligned}
 h_d(1,1,-2)
 &=\sum_{c=0}^d(d-c+1)(-2)^c\\
 &={3d+5-2^{d+2}\over9}\ne0,
 \end{aligned}
\]

the last inequality holding for odd (d\ge5).  Thus (h_{m+1}) is not
divisible by (X_1+\cdots+X_m), contradicting (4.1).  □

For (m=2), the obstruction disappears:

\[
 h_3(X_1,X_2)=(X_1+X_2)(X_1^2+X_2^2),
\]

consistent with the two-child packet that gives the small perfect example.

The polynomial argument is an exact no-go.  The next section gives the
stronger asymptotic no-go.

## 5. Dual-shadow capacity: one half is asymptotically optimal

For a rooted parent \(x\in\Delta_m(m)\), define its downward shadow

\[
 D(x)=\{x-e_i:x_i>0\}\subseteq\Delta_m(m-1).
\tag{5.1}
\]

### Lemma 5.1 (upward conflict equals downward conflict)

For two distinct parent rotation classes \([x]\) and \([y]\), their
upward packet stars meet if and only if their quotient downward shadows
meet.

#### Proof

After choosing suitable rotations, a common downward child has the form

\[
 x=v+e_i,\qquad y=v+e_j,\qquad i\ne j.
\]

Then \(v+e_i+e_j\) is a common upward child.  Conversely, if

\[
 x+e_i=y+e_j=u
\]

with distinct parents, then \(i\ne j\), both \(u_i,u_j\) are positive,
and \(u-e_i-e_j\) is a common downward child.  This argument commutes
with coordinate rotation.  \(\square\)

Thus every packet matching also packs pairwise-disjoint downward shadows.
The lower action is free because \(\gcd(m,m-1)=1\), and hence the total
number of quotient lower targets is exactly

\[
 B_-={1\over m}\binom{2m-2}{m-1}
 ={m+1\over2(2m-1)}T
 =\left({1\over4}+o(1)\right)T.
\tag{5.2}
\]

### Lemma 5.2 (aperiodic downward-shadow size)

If \(x\in\Delta_m(m)\) has least coordinate-rotation period \(m\), then

\[
 |D(x)/\langle R\rangle|=s(x):=|\{i:x_i>0\}|.
\tag{5.3}
\]

#### Proof

Suppose \([x-e_i]=[x-e_j]\) for two active, distinct coordinates.  Then
for some coordinate rotation \(P=R^t\),

\[
 P(x-e_i)=x-e_j,
 \qquad
 Px-x=e_{Pi}-e_j.
\tag{5.4}
\]

Let \(g=\gcd(m,t)\); every \(P\)-cycle has length
\(\ell=m/g\).  Summing (5.4) on a \(P\)-cycle first shows that
\(Pi\) and \(j\) lie on the same cycle.  If \(Pi\ne j\), then on this
cycle the coordinates of \(x\) are constant except for a unit jump across
a nonempty proper arc.  Its coordinate sum is therefore nonzero modulo
\(\ell\).  All other cycle sums are divisible by \(\ell\), contradicting

\[
 \sum_i x_i=m=g\ell.
\]

Hence \(Pi=j\), so (5.4) gives \(Px=x\).  A nonidentity \(P\) would make
\(x\) periodic, while the identity would force \(i=j\).  Both are
impossible.  \(\square\)

### Lemma 5.3 (almost every parent has half-full support)

For rooted parents, the number having exactly \(s\) positive coordinates
is

\[
 A_s=\binom ms\binom{m-1}{s-1}.
\tag{5.5}
\]

There is a sequence \(\delta_m\to0\) such that the number of aperiodic
parent rotation classes with

\[
 s<(1/2-\delta_m)m
\]

is \(o(T/m)\).

#### Proof

Formula (5.5) follows by choosing the support and then a positive
composition of \(m\) on that support.  Moreover

\[
 A_s={s\over m}\binom ms^2\le\binom ms^2.
\]

The binomial Chernoff bound therefore gives

\[
 \sum_{s\le(1/2-\delta)m}A_s
 \le\left(\sum_{s\le(1/2-\delta)m}\binom ms\right)^2
 \le4^m\exp(-4\delta^2m).
\]

Taking, for example,

\[
 \delta_m=\sqrt{2\log m/m},
\]

the right side is at most \(4^m m^{-8}=o(T)\), since
\(T=\Theta(4^m/m^{3/2})\).  Division by the full aperiodic orbit size
\(m\) gives \(o(T/m)\) aperiodic classes.  Periodic parents are already
\(e^{-\Omega(m)}T\).  \(\square\)

### Theorem 5.4 (sharp half-capacity)

Let \(\nu_w(\mathcal H_m)\) be the maximum number of odd form vertices
covered by a packet matching.  Then

\[
 \boxed{\nu_w(\mathcal H_m)=\left({1\over2}+o(1)\right)T.}
\tag{5.6}
\]

#### Proof

Let \(\mathcal M\) be a packet matching.  Discard its periodic parents and
the aperiodic parents from the low-support exceptional set in Lemma 5.3.
Together their upward packets cover only \(o(T)\) vertices.

If \(k\) parents remain, Lemmas 5.1--5.3 and (5.2) give

\[
 k(1/2-\delta_m)m\le B_-.
\]

Every remaining aperiodic packet has exactly \(m\) upper vertices, so

\[
 km\le {B_-\over1/2-\delta_m}
 =\left({1\over2}+o(1)\right)T.
\]

This proves the upper bound.  Proposition 3.2 of the packet note gives a
phase matching covering at least

\[
 {m+1\over2m}T=\left({1\over2}+o(1)\right)T,
\]

which proves the matching lower bound.  \(\square\)

## 6. Consequences for the coefficient-one program

The all-form one-chip catalogue is now completely resolved at the middle
matching level:

* its voltage, owner legality, and all-form incidence are valid;
* its best possible matching covers asymptotically one half of the form
  vertices; and
* it cannot supply the \(T-o(T)\) owner coverage needed for a
  coefficient-one construction.

The lower-prefix inequalities are therefore moot for this catalogue as a
bulk mechanism.  One-chip packets can still be used as a half-cover or a
reserve/absorber, but a different, larger trade family is required for the
remaining positive-density owner mass.

## 7. Disposition

* Keep Theorems 2.1, 3.1, and 3.2 and promote the half-cover component
  bound to an asymptotically sharp theorem.
* Rename the code gate to avoid conflating deletion packing with insertion
  covering.
* Replace both “perfect packet decomposition open” and “near-perfect packet
  matching open” by Theorem 5.4.
* Do not cite modified VT weight partitioning as a near-perfect matching
  theorem after cyclic quotienting.  Its checksum does not descend, and
  the correct cyclic packet capacity is only one half.
