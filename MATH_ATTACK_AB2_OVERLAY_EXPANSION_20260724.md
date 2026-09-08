# Second-wave AB: ownership-overlay expansion, anti-fragmentation, and the signed noise obstruction

Date: 2026-07-24

Status: theorem-level second-wave report.  Everything labelled **Theorem**, **Lemma**,
**Proposition**, or **Corollary** below is proved in this note, apart from two explicitly
identified audited inputs: the Johnson-slice spectrum and the first-wave transposition
component-equivariance theorem.  Every route statement labelled **Open gate** is unproved.
No finite search, numerical experiment, or external source is used.

## 0. Executive verdict

There is genuine ownership-overlay expansion, but it points in the wrong direction for
the occurrence-pair heat gap.

Let

\[
 n=2m+1,\qquad
 \Omega=\binom{[n]}m,\qquad
 W=|\Omega|,\qquad
 B=\frac Wn=\operatorname{Cat}_m.
\]

For every exact wreath factor \(F\), the following statements are proved.

1. **A well-chosen direct permutation is almost transverse.**  If

   \[
   a_{CD}^{\sigma}
   =|\mathcal W_m(C)\cap\sigma\mathcal W_m(D)|
   \]

   and

   \[
   P_\sigma=\sum_{C,D\in F}\binom{a_{CD}^{\sigma}}2,
   \]

   then some coordinate permutation \(\sigma\), expressible using at most \(n-1\)
   transpositions, satisfies

   \[
   P_\sigma\le 2W S_m,
   \qquad
   S_m:=\sum_{d=1}^m
      \frac1{\binom md\binom{m+1}d}
      =\frac1m+O(m^{-3}).
   \]

   Its direct overlay has at most

   \[
   \boxed{
   k_\sigma\le \frac Bn(1+4S_m)
   =\left(1+O(m^{-1})\right)\frac Bn
   }
   \]

   components.  All but \(O(B/n)\) owners lie in components larger than \(n/2\).
   Thus natural partition expansion produces **large components**, not the size-two
   fragmentation that kills duplicate concentration.

2. **The family of transposition overlays has an exact cut-isoperimetric bound.**
   If \(A\subseteq F\), \(|A|=a\), and \(\partial_\tau A\) is the cut multiplicity
   in the transposition owner graph, then

   \[
   \boxed{
   \sum_\tau\partial_\tau A
   \ge 2n(n-1)a\left(1-\frac aB\right),
   \qquad
   \max_\tau\partial_\tau A
   \ge4a\left(1-\frac aB\right).
   }
   \]

   The quantifier is \(\forall A\,\exists\tau\), not
   \(\exists\tau\,\forall A\).  It proves strong turnover between different
   transposition partitions; it does not prove that one overlay is a Cheeger expander.

3. **A spanning-tree family maximally coalesces the layered overlay.**  The join of
   the transposition-component partitions associated with the \(n-1\) edges of any
   coordinate spanning tree is one block for every exact factor.  The corresponding
   length-\((n-1)\) layered endpoint cube contains only \(F\) and its relabelling.
   Hence maximal layered expansion has exactly zero fair heat.

4. **Arbitrary direct components satisfy a two-sided leakage theorem.**  For a direct
   component \(K\) of side size \(s\), at depth \(q\), let \(x_K(S),y_K(S)\) be
   the left and right occurrence counts of a target \(S\).  Then

   \[
   \boxed{
   |y_K(S)-x_K(S)|
   \le
   \left\lfloor
   \frac{q(s-\min(x_K(S),y_K(S)))}{q+1}
   \right\rfloor.
   }
   \]

   In particular, singleton components are completely inert, size-two components
   have effect at most one at every depth, and at depth one the same is true through
   size three.  This does not require direct component equivariance.

5. **The exact heat datum is signed and target-coloured.**  Put

   \[
   d_K(S)=y_K(S)-x_K(S),\qquad z_S=\sum_Kd_K(S),
   \]

   \[
   B_S=\binom{|z_S|}{2},\qquad
   M_S=\frac{\sum_K|d_K(S)|-|z_S|}{2},\qquad
   R_S=\sum_K\binom{|d_K(S)|}{2}.
   \]

   The direct fair contribution of \(S\) is exactly

   \[
   \boxed{
   D_S=\frac12\left(z_S^2-\sum_Kd_K(S)^2\right)
      =B_S-M_S-R_S.
   }
   \]

   Small components control \(R_S\).  They do not control \(M_S\), the residual
   opposite-sign mixing.  Connected overlays have \(R_S=B_S\) and zero heat;
   maximally fragmented singleton overlays also have zero heat.  Ordinary component
   expansion and ordinary fragmentation therefore both fail as monotone principles.

6. **The corrected global component-noise gate contains three independent slacks.**
   For transpositions,

   \[
   R_H-D_H
   =4\sum_\tau(\mathfrak M_\tau+\mathfrak R_\tau-\mathfrak B_\tau).
   \]

   At a global minimizer,

   \[
   \boxed{
   \begin{aligned}
   R_H-4(n-1)B_H^{\rm floor}
   ={}&4\sum_\tau(\mathfrak M_\tau+\mathfrak R_\tau-\mathfrak B_\tau)\\
     &+\bigl[D_H-4(n-1)(B_H^{\rm floor}+\Phi_H)\bigr]\\
     &+4(n-1)\Phi_H.
   \end{aligned}}
   \]

   Overlay geometry addresses only the first line.  The second line is higher-Johnson
   spectral excess, and the third is the desired floor energy itself.  Consequently
   the corrected noise upper gate cannot follow from connectivity, component count,
   collision expansion, or zero point margins alone.

The surviving route is not an unsigned expansion lemma.  It is a signed colour
alignment theorem: for one common direct overlay, residual copies of every target at
every controlled depth must be unit-sized and globally oriented, up to the exact
Catalan residue.  That statement remains open.

---

## 1. Exact-factor and energy notation

A wreath row \(C\) is a cyclic order on \([n]\).  For \(1\le r\le m\),
\(\mathcal W_r(C)\) denotes its \(n\) cyclic intervals of size \(r\).
An exact factor \(F\) is a family of \(B=W/n\) wreath rows for which

\[
 \Omega=\bigsqcup_{C\in F}\mathcal W_m(C).
\tag{1.1}
\]

Fix a depth \(q\), put \(r=m-q\), and define

\[
 \mu_q^F(S)=|\{C\in F:S\in\mathcal W_r(C)\}|,
 \qquad S\in\binom{[n]}r.
\tag{1.2}
\]

Let

\[
 N_q=\binom nr,\qquad
 \frac W{N_q}=c_q+\theta_q,quad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,quad
 0\le\theta_q<1.
\tag{1.3}
\]

The rank-\(q\) floor energy and the fixed-window energy are

\[
 Q_q(F)=\sum_S(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1),
\tag{1.4}
\]

\[
 \mathcal Q_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q}.
\tag{1.5}
\]

If \(f_q=\mu_q^F-(W/N_q)\mathbf1\), then

\[
 Q_q(F)=\|f_q\|_2^2-V_q^{\min},
 \qquad
 V_q^{\min}=N_q\theta_q(1-\theta_q).
\tag{1.6}
\]

We use

\[
 B_H^{\rm floor}=\sum_{q\le H}\frac{V_q^{\min}}{c_q},
 \qquad
 \Phi_H(F)=\mathcal Q_H(F).
\tag{1.7}
\]

For the Gaussian window, \(H=H_A=\lceil A\sqrt m\rceil\), where \(A\) is fixed.
In this range \(1\le c_q\le C_A\) for a constant depending only on \(A\).  Indeed,

\[
 \frac W{N_q}
 =\frac{(m-q)!(m+1+q)!}{m!(m+1)!}
 =\prod_{j=1}^q\frac{m+1+j}{m-q+j},
\tag{1.8}
\]

and the logarithm of the product is \(O(q^2/m)=O_A(1)\).

All harmonic statements below are understood for sufficiently large \(m\), so that
\(H_A\le m-2\) and every controlled rank satisfies \(2\le r=m-q\le n-2\).
Rank one, when it occurs in a finite boundary case, has identically zero centered
load because exact factors have fixed singleton margins and must be treated
separately; it contributes nothing to the asymptotic gate.

Every row is point-regular: across \(\mathcal W_r(C)\), each coordinate occurs
exactly \(r\) times.  Consequently every component difference considered below has
zero total and zero point margins.

---

## 2. Direct overlaps are intersections of two equal-block partitions

Fix \(\sigma\in S_n\).  The direct overlay of \(F\) and \(\sigma F\) is the
bipartite multigraph whose left vertices are rows \(C\in F\), whose right vertices
are rows \(\sigma D\in\sigma F\), and whose middle-root edges are the sets
\(X\in\Omega\).  Thus

\[
 a_{CD}^{\sigma}
 :=|\mathcal W_m(C)\cap\mathcal W_m(\sigma D)|.
\tag{2.1}
\]

The matrix \(A^\sigma=(a_{CD}^{\sigma})\) is nonnegative integral, and every row
and every column sums to \(n\).

Let \(\Pi_F\) be the partition of \(\Omega\) into the root blocks
\(\mathcal W_m(C)\), \(C\in F\).  Let \(U_F\subseteq\mathbb R^\Omega\) be the
space of functions constant on each block of \(\Pi_F\).  We use \(\vee\) for the
coarsest partition coarser than both inputs, equivalently the equivalence relation
generated by both block relations.

### Theorem 2.1 (partition-intersection theorem)

If \(k_\sigma\) is the number of direct-overlay components, then

\[
 \boxed{
 k_\sigma
 =|\Pi_F\vee\sigma\Pi_F|
 =\dim(U_F\cap\sigma U_F).
 }
\tag{2.2}
\]

Every component has the same number \(s_K\) of left and right rows.

#### Proof

A function lies in \(U_F\cap\sigma U_F\) exactly when it is constant on every
left root block and every right root block.  Hence it is constant along every
alternating path in the overlay, and therefore on every overlay component.
Conversely, a component indicator is constant on every left and right block.
The component indicators are linearly independent and span the intersection.

The overlay is \(n\)-regular on both sides.  If a component has \(s_L\) left and
\(s_R\) right vertices, counting its edges from both sides gives
\(ns_L=ns_R\), so \(s_L=s_R\).  \(\square\)

Normalize every block indicator by \(n^{-1/2}\).  The cross-Gram matrix of the
two orthonormal block bases is

\[
 M_\sigma=\frac1nA^\sigma.
\tag{2.3}
\]

The singular value \(1\) has multiplicity exactly \(k_\sigma\).  This is also
immediate componentwise: on each connected regular component the normalized
constant vector is a unit singular vector, while equality in the contraction
\(\|M_\sigma v\|\le\|v\|\) forces constancy along all incident edges.

Define the parallel-pair collision mass

\[
 P_\sigma=\sum_{C,D\in F}\binom{a_{CD}^{\sigma}}2.
\tag{2.4}
\]

Since \(\sum_{C,D}a_{CD}^{\sigma}=nB\),

\[
 \|M_\sigma\|_F^2
 =\frac{nB+2P_\sigma}{n^2}.
\tag{2.5}
\]

### Corollary 2.2 (global collision isoperimetry)

For every direct overlay,

\[
 \boxed{
 k_\sigma\le\frac Bn+\frac{2P_\sigma}{n^2}.
 }
\tag{2.6}
\]

#### Proof

Each of the \(k_\sigma\) unit singular values contributes one to the squared
Frobenius norm in (2.5).  Equivalently, a component of side size \(s\) has an
\(s\times s\) matrix block of total mass \(ns\), so Cauchy gives squared
Frobenius mass at least \((ns)^2/s^2=n^2\).  Sum over components.  \(\square\)

### Lemma 2.3 (sharp local collision lower bound)

Let \(K\) have \(s\) owners on each side, and write

\[
 n=\ell s+r_0,\qquad 0\le r_0<s.
\tag{2.7}
\]

Its collision contribution satisfies

\[
 \boxed{
 P_K\ge
 s\left[(s-r_0)\binom\ell2+r_0\binom{\ell+1}2\right].
 }
\tag{2.8}
\]

In particular,

\[
 P_K\ge s(n-s),
\tag{2.9}
\]

and, when \(s<n\),

\[
 P_K\ge\frac{n(n-s)}2.
\tag{2.10}
\]

For \(s=2\), the exact lower bound is

\[
 \boxed{P_K\ge2m^2.}
\tag{2.11}
\]

#### Proof

There are \(s^2\) nonnegative integral matrix entries with sum \(ns\).
Discrete convexity of \(z\mapsto\binom z2\) makes the sum smallest when the
entries differ by at most one.  There are \(r_0s\) entries equal to \(\ell+1\)
and \((s-r_0)s\) equal to \(\ell\), which gives (2.8).

For (2.9), use \(\binom z2\ge z-1\) on each nonzero entry; at most \(s^2\)
entries are nonzero, so \(P_K\ge ns-s^2\).  For (2.10),

\[
 2P_K=\sum a_{CD}^2-ns\ge n^2-ns.
\]

For \(s=2\), \(n=2m+1=2m+1\) in (2.8), so

\[
 P_K\ge2\left[\binom m2+\binom{m+1}2\right]=2m^2.
\]

\(\square\)

### Proposition 2.4 (internal vertex expansion paid by collisions)

Inside one direct component, let \(A\) be a set of \(a\) left owners, let
\(N(A)\) contain \(b\) right owners, and let

\[
 P(A)=\sum_{C\in A,\,D\in N(A)}\binom{a_{CD}^{\sigma}}2.
\]

Then

\[
 \boxed{
 b\ge
 \max\left\{
 a,
 n-\frac{P(A)}a,
 \frac{n^2a}{na+2P(A)}
 \right\}.
 }
\tag{2.12}
\]

In particular, if the relevant overlap cells are simple, \(P(A)=0\), then
\(b\ge\max(a,n)\).

#### Proof

The \(na\) incident root edges all end in \(N(A)\).  Since every right owner has
total degree \(n\), Hall's counting inequality gives \(na\le nb\), hence \(b\ge a\).

At most \(ab\) matrix entries are positive, and
\(\binom z2\ge z-1\) on a positive entry.  Therefore

\[
 P(A)\ge na-ab=a(n-b),
\]

which gives the second bound.  Finally, Cauchy on the \(ab\) cells gives

\[
 na+2P(A)=\sum a_{CD}^2\ge\frac{(na)^2}{ab}
 =\frac{n^2a}{b},
\]

which gives the third.  \(\square\)

### Corollary 2.5 (both component-count extremes are heat-inert)

If \(k_\sigma=1\), the endpoint component cube contains only \(F\) and
\(\sigma F\); its fair heat is zero at every depth.

If \(k_\sigma=B\), then \(\Pi_F=\sigma\Pi_F\).  Every component is singleton,
and its two lower-rank histograms agree at every depth; again every component
effect and the fair heat are zero.

The second assertion follows from the arbitrary-permutation leakage theorem in
Section 7.  Thus neither increasing nor decreasing component count is monotone
toward heat.

### Example 2.6 (genuine maximal fragmentation and failure of direct equivariance)

Take \(m=2\), \(n=5\), and identify the coordinates with \(\mathbb Z_5\).  Let

\[
 C=(0,1,2,3,4),\qquad D=(0,2,4,1,3).
\]

Their length-two interval sets are respectively the step-one and step-two edges,
which partition \(K_5\).  Hence \(F=\{C,D\}\) is exact.  The nonidentity
permutation

\[
 \sigma:x\mapsto2x\pmod5=(0)(1\ 2\ 4\ 3)
\]

interchanges \(C\) and \(D\), so \(\sigma F=F\).  The direct overlay consists
of two singleton components, each with five parallel root edges, and all lower-rank
effects vanish.

This is also a genuine failure of direct component equivariance for a general
permutation.  The component with physical root block \(\mathcal W_m(C)\) has
left side \(\{C\}\) and right side \(\{\sigma D\}=\{C\}\), whereas
\(\sigma\{C\}=\{D\}\) lies in the other component.  Thus
\(R_K=\sigma L_K\) is not a general direct-overlay fact.  The example is already
balanced, so it does not refute a high-energy threshold alternative.

---

## 3. Uniform-permutation collision averaging

The preceding inequalities become useful because the direct collision mass has an
exact factor-independent average.

For two rank-\(m\) sets, write their Johnson distance as

\[
 d=m-|X\cap Y|\in\{1,\ldots,m\}.
\]

### Lemma 3.1 (pair counts)

Every wreath row contains exactly \(n\) unordered pairs of distinct middle windows
at each Johnson distance \(d=1,\ldots,m\).  The full middle layer contains

\[
 \frac W2\binom md\binom{m+1}d
\tag{3.1}
\]

unordered pairs at distance \(d\).

#### Proof

Two cyclic length-\(m\) windows whose starting points have shorter cyclic distance
\(d\) intersect in \(m-d\) points.  An odd \(n\)-cycle has exactly \(n\)
unordered pairs of starting points at each shorter distance \(d=1,\ldots,m\).

For the ambient count, choose the first set \(X\), delete \(d\) of its \(m\)
points, add \(d\) of the \(m+1\) complementary points, and divide the ordered
count by two.  \(\square\)

Put

\[
 S_m=\sum_{d=1}^m
 \frac1{\binom md\binom{m+1}d}.
\tag{3.2}
\]

### Theorem 3.2 (exact uniform-permutation collision average)

For uniform \(\sigma\in S_n\),

\[
 \boxed{\mathbb E_\sigma P_\sigma=2WS_m.}
\tag{3.3}
\]

#### Proof

Fix \(C,D\in F\).  A fixed unordered distance-\(d\) pair in
\(\mathcal W_m(C)\) is carried by uniform \(\sigma^{-1}\) uniformly over the
ambient orbit (3.1).  Exactly \(n\) members of that orbit are pairs in
\(\mathcal W_m(D)\).  Therefore

\[
 \mathbb E_\sigma\binom{a_{CD}^\sigma}2
 =\sum_{d=1}^m
 n\cdot
 \frac{n}{(W/2)\binom md\binom{m+1}d}
 =\frac{2n^2}{W}S_m.
\tag{3.4}
\]

There are \(B^2\) owner pairs and \(W=nB\), so summing (3.4) gives
\(2n^2B^2S_m/W=2WS_m\).  \(\square\)

### Lemma 3.3 (audited bounds on \(S_m\))

For \(m\ge4\),

\[
 \boxed{
 \frac1m\le S_m<\frac1m+\frac6{m^3}.
 }
\tag{3.5}
\]

#### Proof

The endpoint terms are

\[
 \frac1{m(m+1)}+\frac1{m+1}=\frac1m,
\tag{3.6}
\]

so the lower bound is immediate.

Let

\[
 u_d=\frac1{\binom md\binom{m+1}d}.
\]

The ratio

\[
 \frac{u_{d+1}}{u_d}
 =\frac{(d+1)^2}{(m-d)(m+1-d)}
\tag{3.7}
\]

shows that \((u_d)\) decreases and then increases.  Hence the maximum on
\(2\le d\le m-2\) is at an endpoint.  Moreover

\[
 u_2=\frac4{m^2(m^2-1)},
 \qquad
 \frac{u_{m-2}}{u_2}=\frac3{m-1}\le1.
\tag{3.8}
\]

Finally

\[
 u_{m-1}=\frac2{m^2(m+1)}.
\tag{3.9}
\]

Thus

\[
 \sum_{d=2}^{m-1}u_d
 \le \frac2{m^2(m+1)}
 +(m-3)\frac4{m^2(m^2-1)}
 <\frac6{m^3}.
\]

\(\square\)

### Theorem 3.4 (a short direct anti-fragmenting permutation)

For every exact factor and \(m\ge4\), there exists \(\sigma\in S_n\) such that

\[
 \boxed{P_\sigma\le2WS_m}
\tag{3.10}
\]

and

\[
 \boxed{
 k_\sigma
 \le\frac Bn(1+4S_m)
 =\left(1+O(m^{-1})\right)\frac Bn.
 }
\tag{3.11}
\]

The permutation \(\sigma\) is a product of at most \(n-1\) transpositions.

Furthermore,

\[
 \boxed{
 \sum_{K:s_K\le n/2}s_K
 \le4BS_m=(8+o(1))\frac Bn,
 }
\tag{3.12}
\]

and the number \(N_2(\sigma)\) of size-two components satisfies

\[
 \boxed{
 N_2(\sigma)\le\frac{WS_m}{m^2}=O(B/m^2).
 }
\tag{3.13}
\]

#### Proof

Choose \(\sigma\) no worse than the average in Theorem 3.2.  Substitute
\(P_\sigma\le2WS_m=2nBS_m\) into (2.6):

\[
 k_\sigma
 \le\frac Bn+\frac{4nBS_m}{n^2}
 =\frac Bn(1+4S_m).
\]

Every permutation with \(c\) coordinate cycles is a product of \(n-c\le n-1\)
transpositions.

For \(s_K\le n/2\), (2.9) gives
\(P_K\ge s_K(n-s_K)\ge ns_K/2\).  Summing gives

\[
 \sum_{s_K\le n/2}s_K\le\frac{2P_\sigma}{n}\le4BS_m.
\]

Finally each size-two component costs at least \(2m^2\) by (2.11), so

\[
 N_2(\sigma)\le\frac{P_\sigma}{2m^2}
 \le\frac{WS_m}{m^2}.
\]

\(\square\)

The matrix can be made \(0\)-\(1\) by deleting at most \(P_\sigma\) excess
parallel edges, because \((a-1)_+\le\binom a2\).  This is only a geometric
diagnostic; deleting middle roots is not a legal factor operation.

### Corollary 3.5 (collision expansion is anti-fragmentation)

The chosen direct overlap places all but \(O(B/n)\) owners in components larger
than \(n/2\), whereas the size-only certificate for suppressing lower-rank residual
concentration in Section 8 requires all but \(O_A(B/n^2)\) owners to lie in
components of size at most two.  Thus the most natural well-chosen-\(\sigma\)
partition expansion theorem and the needed duplicate-fragmentation theorem point
in quantitatively opposite directions.

### Proposition 3.6 (one prescribed cut can expand with low collision)

Let \(A\subseteq F\), \(|A|=a\le B/2\), and put

\[
 U_A=\bigsqcup_{C\in A}\mathcal W_m(C).
\]

Define the one-sided matched cut

\[
 \partial_\sigma A
 =|U_A\setminus\sigma U_A|.
\tag{3.14}
\]

There exists \(\sigma\in S_n\) such that

\[
 \boxed{
 \partial_\sigma A
 \ge\frac n2a\left(1-\frac aB\right)
 \ge\frac{na}{4},
 \qquad
 P_\sigma\le8WS_m.
 }
\tag{3.15}
\]

#### Proof

Uniform transitivity on \(\Omega\) gives

\[
 \mathbb E_\sigma\partial_\sigma A
 =na\left(1-\frac aB\right)=:\mu.
\tag{3.16}
\]

The cut is bounded by \(na\), and \(\mu\ge na/2\).  If
\(p=\Pr(\partial_\sigma A\ge\mu/2)\), then

\[
 \mu\le(1-p)\frac\mu2+pna,
\]

so \(p\ge\mu/(2na-\mu)\ge1/3\).  Markov and (3.3) give
\(\Pr(P_\sigma\le8WS_m)\ge3/4\).  The two events have positive intersection.
\(\square\)

The crucial scope is

\[
 \forall A\ \exists\sigma,
\tag{3.17}
\]

not a single-\(\sigma\) Cheeger statement.

---

## 4. Exact transposition-family cut isoperimetry

We now obtain a sharper prescribed-cut theorem when \(\sigma\) is restricted to
one transposition, by using the point-regularity of root unions.

For an unordered coordinate transposition \(\tau\), let \(\Gamma_\tau(F)\) be
the audited owner-orbit multigraph: a nonfixed root orbit \(\{X,\tau X\}\) gives
one edge between the owners of \(X\) and \(\tau X\).  For \(A\subseteq F\), let
\(\partial_\tau A\) be its cut multiplicity in this graph.

### Lemma 4.1 (root-boundary identity)

\[
 \boxed{
 \partial_\tau A
 =|U_A\setminus\tau U_A|
 =\frac12|U_A\triangle\tau U_A|.
 }
\tag{4.1}
\]

Moreover,

\[
 \sum_\tau\partial_\tau A
 =|\partial_J U_A|,
\tag{4.2}
\]

where the right side is the edge boundary of \(U_A\) in the Johnson graph
\(J(n,m)\).

#### Proof

A nonfixed \(\tau\)-orbit crosses \(U_A\) exactly when one of its two members is
in \(U_A\) and the other is not.  This proves (4.1).  Every Johnson edge
\(\{X,Y\}\), \(|X\triangle Y|=2\), is generated by the unique transposition
which exchanges the point in \(X\setminus Y\) with the point in \(Y\setminus X\).
Thus summing over transpositions counts every Johnson boundary edge once.  \(\square\)

The following spectral identity is an audited input used elsewhere in the project.
On Johnson harmonic degree \(j\), the Laplacian eigenvalue is

\[
 \lambda_j=j(n-j+1).
\tag{4.3}
\]

In particular, on the subspace with zero total and zero point margins, the least
eigenvalue is \(\lambda_2=2(n-1)\).  This input is proved representation-theoretically
in the earlier harmonic reports; it is not an unproved lemma of this lane.

### Theorem 4.2 (sharp familywise owner-cut expansion)

For \(m\ge2\), every exact factor, and every owner subset \(A\subseteq F\),
\(|A|=a\),

\[
 \boxed{
 \sum_\tau\partial_\tau A
 \ge2n(n-1)a\left(1-\frac aB\right).
 }
\tag{4.4}
\]

Consequently,

\[
 \boxed{
 \max_\tau\partial_\tau A
 \ge4a\left(1-\frac aB\right).
 }
\tag{4.5}
\]

If \(a\le B/2\), some transposition crosses the cut in at least \(2a\)
owner-orbit edges.

#### Proof

Put \(\alpha=a/B\) and

\[
 g_A=\mathbf1_{U_A}-\alpha\mathbf1_\Omega.
\]

We have \(|U_A|=na\).  Each coordinate lies in exactly \(ma\) roots of
\(U_A\), because every selected wreath row contributes \(m\) middle intervals
through that coordinate.  The full middle layer contains \(mW/n=mB\) sets through
each coordinate, and \(\alpha mB=ma\).  Thus \(g_A\) has zero total and zero point
margins.  By (4.3),

\[
 |\partial_J U_A|
 =\langle g_A,L_Jg_A\rangle
 \ge2(n-1)\|g_A\|_2^2.
\]

Also

\[
 \|g_A\|_2^2
 =na\left(1-\frac aB\right).
\]

Use (4.2) to obtain (4.4), and divide by
\(\binom n2=n(n-1)/2\) to obtain (4.5).  \(\square\)

### Corollary 4.3 (partition turnover)

Let \(\mathcal P=\{K_i\}\) be any partition of the owners, with
\(|K_i|=s_i\).  Let \(E_\tau(\mathcal P)\) count the \(\tau\)-owner edges whose
endpoints lie in different blocks of \(\mathcal P\).  Then

\[
 \boxed{
 \sum_\tau E_\tau(\mathcal P)
 \ge n(n-1)\left(B-\frac1B\sum_i s_i^2\right).
 }
\tag{4.6}
\]

Hence some \(\tau\) satisfies

\[
 \boxed{
 E_\tau(\mathcal P)
 \ge2\left(B-\frac1B\sum_i s_i^2\right).
 }
\tag{4.7}
\]

If \(\mathcal P\) is the component partition of a transposition \(\tau_0\), then
\(E_{\tau_0}(\mathcal P)=0\), and some \(\rho\ne\tau_0\) satisfies

\[
 \boxed{
 E_\rho(\mathcal P)
 \ge
 \frac{2n(n-1)}{n(n-1)-2}
 \left(B-\frac1B\sum_i s_i^2\right).
 }
\tag{4.8}
\]

#### Proof

Each crossing edge is counted in the boundaries of both blocks, so

\[
 E_\tau(\mathcal P)=\frac12\sum_i\partial_\tau K_i.
\]

Sum Theorem 4.2 over \(i\) to get (4.6), then average over all transpositions.
For (4.8), omit the zero term \(\tau_0\) and divide by
\(\binom n2-1=(n(n-1)-2)/2\).  \(\square\)

The theorem proves strong recomputed turnover.  It does not say that the new
\(\rho\)-components are small: an edge crossing the old partition causes its join
with the new partition to **merge** old cells.

---

## 5. Generator joins: a universal coalescence theorem

The preceding turnover has an exact endpoint when several transposition partitions
are joined.

For a transposition \(\tau\), let \(\mathcal P_\tau\) denote the component
partition of the owner set \(F\) in \(\Gamma_\tau(F)\).  The first-wave audited
component-equivariance theorem says that, for every cell \(K\in\mathcal P_\tau\),

\[
 U_K:=\bigsqcup_{C\in K}\mathcal W_m(C)
\quad\text{satisfies}\quad
 \tau U_K=U_K.
\tag{5.1}
\]

This is the second explicit audited input used in this report.  Its proof uses the
existence of a \(\tau\)-fixed middle interval in every wreath and regularity of each
bipartite component.

Let \(T\) be a set of coordinate transpositions and put

\[
 \mathcal P_T=\bigvee_{\tau\in T}\mathcal P_\tau,
 \qquad G_T=\langle T\rangle.
\tag{5.2}
\]

### Theorem 5.1 (group-orbit bound for the joined overlay)

For every block \(K\in\mathcal P_T\), the root union \(U_K\) is invariant under
\(G_T\).  Consequently,

\[
 \boxed{
 |\mathcal P_T|
 \le \#\{G_T\text{-orbits on }\Omega\}.
 }
\tag{5.3}
\]

If the coordinate graph with edge set \(T\) has connected components
\(V_1,\ldots,V_c\), then

\[
 G_T=\prod_{j=1}^c S_{V_j},
\tag{5.4}
\]

and

\[
 \boxed{
 |\mathcal P_T|
 \le
 \#\left\{(r_1,\ldots,r_c):
 0\le r_j\le|V_j|,\ \sum_{j=1}^c r_j=m
 \right\}.
 }
\tag{5.5}
\]

Equivalently, the right side is

\[
 [z^m]\prod_{j=1}^c(1+z+\cdots+z^{|V_j|}).
\tag{5.6}
\]

#### Proof

A block of the join is a union of cells of \(\mathcal P_\tau\) for every
\(\tau\in T\).  Its root union is therefore a union of \(\tau\)-invariant root
unions and is itself \(\tau\)-invariant.  It is invariant under the generated group.
Distinct join blocks give disjoint nonempty invariant root unions, so each contains
at least one distinct \(G_T\)-orbit.  This proves (5.3).

Transpositions on the edges of a connected graph generate the full symmetric group
on that vertex set.  This proves (5.4).  The orbits of the product group on rank-\(m\)
sets are classified exactly by the intersection-size vector
\((|X\cap V_1|,\ldots,|X\cap V_c|)\), proving (5.5).  \(\square\)

### Corollary 5.2 (spanning-tree collapse)

If \(T\) is the \(n-1\) edges of any coordinate spanning tree, then

\[
 \boxed{\mathcal P_T=\{F\}.}
\tag{5.7}
\]

#### Proof

Here \(G_T=S_n\), which is transitive on \(\Omega\).  Equation (5.3) gives at most
one nonempty join block.  \(\square\)

### Corollary 5.3 (universal length-\((n-1)\) layered collapse)

There is a fixed word of \(n-1\) coordinate transpositions whose layered endpoint
bundle partition is one block for every exact factor.

#### Proof

Prescribe spanning-tree transpositions \(\rho_1,\ldots,\rho_{n-1}\).  Starting with
\(\sigma_0=1\), define recursively

\[
 \tau_i=\sigma_{i-1}\rho_i\sigma_{i-1}^{-1},
 \qquad
 \sigma_i=\tau_i\sigma_{i-1}.
\tag{5.8}
\]

Every \(\tau_i\) is a transposition, and

\[
 \rho_i=\sigma_{i-1}^{-1}\tau_i\sigma_{i-1}.
\]

The audited layered-word theorem identifies the endpoint bundle partition with

\[
 \mathcal P_{\rho_1}\vee\cdots\vee\mathcal P_{\rho_{n-1}},
\]

which is one block by Corollary 5.2.  \(\square\)

The endpoint cube in Corollary 5.3 has only its two whole-factor choices, \(F\) and
\(\sigma_{n-1}F\).  Therefore, at every depth,

\[
 V_{\sigma_{n-1}}=A_{\sigma_{n-1}},
\tag{5.9}
\]

and its fair heat gap is exactly zero.  This is a universal theorem of maximal
layered expansion and simultaneously a universal no-go for extracting heat from
that expansion.

The scope is important: it does **not** prove that the direct overlay of
\(F\) and \(\sigma_{n-1}F\) is connected.  Direct components can refine the single
layered bundle because direct equivariance fails for general permutations.

---

## 6. No single permutation has a universal signed spectral gap

The familywise transposition bound in Section 4 has an adaptive quantifier.  No one
coordinate permutation has a positive operator gap on the entire admissible signed
discrepancy space.  The following elementary theorem strengthens the earlier
four-untouched-coordinate obstruction and applies to every permutation.

Fix a rank \(r\) with \(2\le r\le n-2\).  For symmetric edge weights
\(a_{ij}=a_{ji}\), define

\[
 v_a(S)=\sum_{\{i,j\}\subseteq S}a_{ij},
 \qquad S\in\binom{[n]}r.
\tag{6.1}
\]

### Theorem 6.1 (an invariant degree-two tangent for every \(\sigma\))

For every \(n=2m+1\ge5\), every \(\sigma\in S_n\), and every
\(2\le r\le n-2\), there is a nonzero integral vector \(v\) on rank \(r\) such that

\[
 \boxed{
 \sigma v=v,\qquad
 \sum_Sv(S)=0,
 \qquad
 \sum_{S\ni i}v(S)=0\quad(i\in[n]).
 }
\tag{6.2}
\]

In fact \(v\) may be chosen in pure Johnson degree two.

#### Proof

Let the coordinate cycles of \(\sigma\) have lengths
\(\ell_1,\ldots,\ell_c\).  Let \(e\) be the number of \(\langle\sigma\rangle\)-orbits
on unordered coordinate pairs.  Pairs within cycle \(i\) have
\(\lfloor\ell_i/2\rfloor\) orbits, and pairs between cycles \(i,j\) have
\(\gcd(\ell_i,\ell_j)\) orbits.  Hence

\[
 e=\sum_i\left\lfloor\frac{\ell_i}{2}\right\rfloor
   +\sum_{i<j}\gcd(\ell_i,\ell_j).
\tag{6.3}
\]

We claim \(e\ge c+1\).  If \(c=1\), then \(e=m\ge2\).  If \(c=2\), either both
cycles are nontrivial, giving two internal orbits and one cross orbit, or one is fixed
and the other has length at least four, again giving at least three orbits.  If
\(c=3\), the three cross pairs give three orbits and, since \(n\ge5\), some cycle is
nontrivial and gives a fourth.  If \(c\ge4\), the cross pairs alone give
\(\binom c2\ge c+1\).

The space of \(\sigma\)-invariant edge weightings has dimension \(e\).  The map
which sends an edge weighting to its vector of vertex row sums has image in the
\(c\)-dimensional space of \(\sigma\)-invariant vertex vectors.  Since \(e>c\),
there is a nonzero invariant rational edge weighting with

\[
 \sum_{j\ne i}a_{ij}=0\qquad(i\in[n]).
\tag{6.4}
\]

Clear denominators to make it integral.  Its total edge sum is zero.

The vector \(v_a\) is \(\sigma\)-invariant.  Its total is

\[
 \sum_Sv_a(S)=\binom{n-2}{r-2}\sum_{i<j}a_{ij}=0.
\]

For a fixed coordinate \(x\),

\[
 \sum_{S\ni x}v_a(S)
 =\binom{n-2}{r-2}\sum_{j\ne x}a_{xj}
 +\binom{n-3}{r-3}
   \sum_{\substack{i<j\\i,j\ne x}}a_{ij}=0,
\tag{6.5}
\]

with the second term interpreted as zero when \(r=2\).  Both edge sums vanish by
(6.4) and the zero total edge sum.

It remains to prove \(v_a\ne0\).  Suppose \(v_a(S)=0\) on every rank-\(r\) set.
For distinct \(i,j\) and every \((r-1)\)-set
\(T\subseteq[n]\setminus\{i,j\}\),

\[
 0=v_a(T\cup\{i\})-v_a(T\cup\{j\})
 =\sum_{k\in T}(a_{ik}-a_{jk}).
\tag{6.6}
\]

Because \(1\le r-1\le n-3\), comparing two such sets which differ in one element
shows that all numbers \(a_{ik}-a_{jk}\), \(k\notin\{i,j\}\), are equal; their
sum on an \((r-1)\)-set is zero, so all are zero.  Thus, for fixed \(k\), all
incident weights \(a_{ik}\) are equal.  Symmetry then makes every edge weight one
common constant, and (6.4) makes that constant zero, contradicting the choice of
\(a\).  Hence \(v_a\ne0\).

Finally, functions of the form (6.1) span Johnson degrees \(0,1,2\); the zero total
and zero point margins remove degrees zero and one.  Thus \(v_a\) is pure degree two.
\(\square\)

### Consequence 6.2 (scope of the obstruction)

There is no constant \(\gamma>0\) such that one fixed permutation satisfies

\[
 \|v-\sigma v\|_2^2\ge\gamma\|v\|_2^2
\]

for every zero-total, zero-point-margin vector on a controlled rank.  This is a
signed tangent-space obstruction.  It does not realize \(v\) as the discrepancy of
an exact factor, and it does not rule out choosing \(\sigma\) adaptively after seeing
one genuine high-energy factor.

There is no contradiction with sequential midpoint contraction: a vector fixed by
the endpoint product \(\sigma\) need not be fixed by each transposition projection
in the word.

---

## 7. Two-sided leakage for arbitrary direct components

We now pass from middle-root geometry to the lower-rank target colours which control
heat.  This is the main cross-rank theorem of the second wave.

Let \(K\) be a component of the direct overlay of two exact factors \(F^0,F^1\).
The intended case is \(F^1=\sigma F^0\), but no relabelling relation is needed.
Let \(K^0,K^1\) be its two row sides and

\[
 s=|K^0|=|K^1|.
\]

The common set of root edges in the component is

\[
 U_K
 =\bigsqcup_{C\in K^0}\mathcal W_m(C)
 =\bigsqcup_{D\in K^1}\mathcal W_m(D),
 \qquad |U_K|=ns.
\tag{7.1}
\]

Fix \(q\in\{1,\ldots,m-1\}\), put \(r=m-q\), and fix an \(r\)-set \(S\).
Define

\[
 x_K(S)=|\{C\in K^0:S\in\mathcal W_r(C)\}|,
\tag{7.2}
\]

\[
 y_K(S)=|\{D\in K^1:S\in\mathcal W_r(D)\}|.
\tag{7.3}
\]

For one row \(C\), let

\[
 h_C(S)=|\{X\in\mathcal W_m(C):S\subseteq X\}|.
\tag{7.4}
\]

### Lemma 7.1 (cyclic containment)

\[
 \boxed{h_C(S)\le q+1,}
\tag{7.5}
\]

with equality if and only if \(S\in\mathcal W_r(C)\).

#### Proof

If no middle interval contains \(S\), the claim is immediate.  Otherwise lift one
containing middle interval to positions \(0,\ldots,m-1\), and let \(a,b\) be the
extreme occupied positions of \(S\).  A middle interval containing \(S\) has its
start in an interval of \(m-(b-a)\) possible positions.  Since \(|S|=r\),
\(b-a\ge r-1\), so

\[
 h_C(S)\le m-(r-1)=q+1.
\]

Equality holds exactly when \(b-a=r-1\), which says that \(S\) fills the consecutive
positions between its extremes.  \(\square\)

Define the two side leakages

\[
 e_K^0(S)
 =\sum_{C\in K^0}
 \left[h_C(S)-(q+1)\mathbf1_{\{S\in\mathcal W_r(C)\}}\right],
\tag{7.6}
\]

and analogously \(e_K^1(S)\) on \(K^1\).

### Theorem 7.2 (arbitrary-direct-overlay leakage identity)

For every direct component,

\[
 \boxed{
 0\le e_K^0(S)\le q(s-x_K(S)),
 \qquad
 0\le e_K^1(S)\le q(s-y_K(S)),
 }
\tag{7.7}
\]

and

\[
 \boxed{
 (q+1)(y_K(S)-x_K(S))
 =e_K^0(S)-e_K^1(S).
 }
\tag{7.8}
\]

Moreover,

\[
 \boxed{
 \sum_S e_K^0(S)=\sum_Se_K^1(S)
 =ns\left[\binom mq-(q+1)\right].
 }
\tag{7.9}
\]

#### Proof

By Lemma 7.1, a genuine cyclic occurrence contributes zero leakage, while a
nongenuine row contributes an integer between zero and \(q\).  This proves (7.7).

Both sides in (7.1) count the same quantity

\[
 H_K(S)=|\{X\in U_K:S\subseteq X\}|.
\]

Expanding it on the two sides gives

\[
 H_K(S)=(q+1)x_K(S)+e_K^0(S)
       =(q+1)y_K(S)+e_K^1(S),
\]

which proves (7.8).

For (7.9), sum \(H_K(S)\) over all rank-\(r\) targets.  Every one of the \(ns\)
middle roots contains \(\binom mq\) such targets.  Each side has \(ns\) genuine
rank-\(r\) occurrences, each subtracted with weight \(q+1\).  \(\square\)

### Corollary 7.3 (direct fragmentation bound)

\[
 \boxed{
 |y_K(S)-x_K(S)|
 \le
 \left\lfloor
 \frac{q(s-\min(x_K(S),y_K(S)))}{q+1}
 \right\rfloor.
 }
\tag{7.10}
\]

Consequently:

* a singleton component has \(x_K(S)=y_K(S)\) for every target and depth;
* a size-two component has \(|y_K(S)-x_K(S)|\le1\) at every depth;
* at \(q=1\), every component of size at most three has effect at most one.

#### Proof

Suppose \(x_K\ge y_K\).  From (7.8) and (7.7),

\[
 (q+1)(x_K-y_K)=e_K^1-e_K^0
 \le e_K^1\le q(s-y_K).
\]

The opposite case is symmetric.  Take the integer floor.  The three consequences
follow from

\[
 \left\lfloor\frac q{q+1}\right\rfloor=0,
 \qquad
 \left\lfloor\frac{2q}{q+1}\right\rfloor=1,
 \qquad
 \left\lfloor\frac32\right\rfloor=1.
\]

\(\square\)

Every component effect

\[
 d_K(S):=y_K(S)-x_K(S)
\tag{7.11}
\]

has zero total and zero point margins.  Indeed, each side has \(ns\) rank-\(r\)
occurrences and point margin \(rs\) at every coordinate.

The conceptual point is exact: a component packet is already annihilated at the
middle rank because its two sides own the same \(U_K\).  Its entire lower-rank image
is the leakage difference in (7.8).  Middle-overlay expansion acts at a rank where
the packet is zero; a successful theorem must control the target-coloured leakage
image.

---

## 8. Targetwise duplicate separation and exact direct heat

Continue with an arbitrary direct overlay.  For a fixed target \(S\), abbreviate

\[
 x_K=x_K(S),\qquad y_K=y_K(S),\qquad d_K=y_K-x_K,
 \qquad z=\sum_Kd_K.
\tag{8.1}
\]

The endpoint target loads differ by \(z\).

Define separated same-target pairs on the two sides and separated cross-side pairs:

\[
 P_S^0=\sum_{K<J}x_Kx_J,
 \qquad
 P_S^1=\sum_{K<J}y_Ky_J,
\tag{8.2}
\]

\[
 C_S^{01}=\sum_{K\ne J}x_Ky_J.
\tag{8.3}
\]

### Theorem 8.1 (general occurrence-pair identity)

\[
 \boxed{
 D_S:=P_S^0+P_S^1-C_S^{01}
 =\frac12\left(z^2-\sum_Kd_K^2\right).
 }
\tag{8.4}
\]

#### Proof

Using \(x=\sum_Kx_K\), \(y=\sum_Ky_K\),

\[
 P_S^0=\frac12\left(x^2-\sum_Kx_K^2\right),
 \quad
 P_S^1=\frac12\left(y^2-\sum_Ky_K^2\right),
\]

and

\[
 C_S^{01}=xy-\sum_Kx_Ky_K.
\]

Subtract and use \(z=y-x\), \(d_K=y_K-x_K\).  \(\square\)

Define

\[
 B_S=\binom{|z|}{2},
 \qquad
 M_S=\frac{\sum_K|d_K|-|z|}{2},
 \qquad
 R_S=\sum_K\binom{|d_K|}{2}.
\tag{8.5}
\]

Here \(M_S\) is exactly the co-location deficit of common left/right mass:

\[
 \boxed{
 M_S
 =\min\left(\sum_Kx_K,\sum_Ky_K\right)
  -\sum_K\min(x_K,y_K).
 }
\tag{8.6}
\]

After cancelling common mass inside each component, \(R_S\) counts residual
same-side pairs still trapped inside one component.

### Theorem 8.2 (exact residual decomposition)

\[
 \boxed{D_S=B_S-M_S-R_S.}
\tag{8.7}
\]

#### Proof

Let \(a=\sum_K|d_K|\) and \(t=|z|\).  Then

\[
 2M_S=a-t,
 \qquad
 2R_S=\sum_Kd_K^2-a,
 \qquad
 2B_S=t^2-t.
\]

Therefore

\[
 2(B_S-M_S-R_S)=t^2-\sum_Kd_K^2=2D_S.
\]

\(\square\)

Combining (7.8) and (8.4), with

\[
 g_K(S)=e_K^0(S)-e_K^1(S)=(q+1)d_K(S),
\tag{8.8}
\]

gives the exact signed leakage-correlation formula

\[
 \boxed{
 D_S=rac1{2(q+1)^2}
 \left[
 \left(\sum_Kg_K(S)\right)^2-
 \sum_Kg_K(S)^2
 \right].
 }
\tag{8.9}
\]

This is the decisive replacement for unsigned overlay expansion.

### Proposition 8.3 (fair direct-endpoint formula and parity audit)

Choose one complete side of every direct component independently and fairly.  Every
outcome is an integral exact factor.  Put

\[
 A_{\sigma,q}=\|\mu_q^{\sigma F}-\mu_q^F\|_2^2,
 \qquad
 V_{\sigma,q}=\sum_K\|d_{K,q}\|_2^2.
\tag{8.10}
\]

Then

\[
 \boxed{
 A_{\sigma,q}-V_{\sigma,q}=2\sum_SD_S,
 }
\tag{8.11}
\]

and

\[
 \boxed{
 \mathbb E Q_q(F_\varepsilon)
 =Q_q(F)-\frac14(A_{\sigma,q}-V_{\sigma,q})
 =Q_q(F)-\frac12\sum_SD_S.
 }
\tag{8.12}
\]

For the integer parity correction, put

\[
 \epsilon_S=|z_S|\bmod2,
 \qquad F_S=\left\lfloor\frac{|z_S|}{2}\right\rfloor.
\]

The target contributions to ideal coherent gain and corrected component noise are

\[
 \boxed{
 G_S=\frac{z_S^2-\epsilon_S}{4}
 =\frac12(B_S+F_S),
 }
\tag{8.13}
\]

\[
 \boxed{
 C_S=\frac{\sum_Kd_K(S)^2-\epsilon_S}{4}
 =\frac12(M_S+R_S+F_S).
 }
\tag{8.14}
\]

Thus the parity-restoration term cancels exactly:

\[
 G_S-C_S=\frac12(B_S-M_S-R_S).
\tag{8.15}
\]

#### Proof

The child load has mean \((\mu_q^F+\mu_q^{\sigma F})/2\) and component variance
\(V_{\sigma,q}/4\).  Relabelling preserves the endpoint squared norm, so midpoint
averaging lowers it by \(A_{\sigma,q}/4\).  This proves (8.12).  Equation (8.11)
is (8.4) summed over targets.

Equations (8.13)--(8.14) follow by checking the two parities of \(|z_S|\), using

\[
 M_S+R_S=\frac{\sum_Kd_K^2-|z_S|}{2}.
\]

\(\square\)

For the window, define half-summed quantities

\[
 \mathbf B_\sigma
 =\frac12\sum_{q\le H}\frac1{c_q}\sum_SB_S,
\tag{8.16}
\]

and similarly \(\mathbf M_\sigma,\mathbf R_\sigma\).  Then

\[
 \boxed{
 \mathcal Q_H(F)-\mathbb E\mathcal Q_H(F_\varepsilon)
 =\mathbf B_\sigma-\mathbf M_\sigma-\mathbf R_\sigma.
 }
\tag{8.17}
\]

For a transposition, the two oriented targets in every moved pair have identical
values of \(B,M,R\).  The half-sum therefore recovers exactly the first-wave
unordered-pair normalization.

### Theorem 8.4 (sharp targetwise component-count isoperimetry)

Suppose the direct overlay has \(k\) components and write

\[
 |z_S|=ak+r_0,
 \qquad0\le r_0<k.
\tag{8.18}
\]

Then

\[
 \boxed{
 M_S+R_S
 \ge k\binom a2+r_0a.
 }
\tag{8.19}
\]

Equality holds exactly when, after orienting by the sign of \(z_S\), the integers
\(d_K(S)\) are nonnegative and differ by at most one.  When \(z_S=0\), this means
that every \(d_K(S)\) is zero.

In particular:

* a connected overlay has \(M_S=0\), \(R_S=B_S\), and \(D_S=0\);
* zero target loss requires at least \(|z_S|\) components and aligned unit residuals;
* if \(z_S=0\), then \(D_S=-\frac12\sum_Kd_K(S)^2\le0\), with equality only
  when every component effect vanishes at \(S\).

#### Proof

Since

\[
 M_S+R_S=\frac{\sum_Kd_K^2-|z_S|}{2},
\]

we minimize the sum of squares of \(k\) integers with fixed sum \(z_S\).
Discrete convexity makes them have one sign and differ by at most one.  There are
\(r_0\) values \(a+1\) and \(k-r_0\) values \(a\), giving

\[
 \frac{r_0(a+1)^2+(k-r_0)a^2-(ak+r_0)}2
 =k\binom a2+r_0a.
\]

The equality characterization and consequences follow.  \(\square\)

### Proposition 8.5 (what a component-size cap actually gives)

Put

\[
 b_q(s)=\left\lfloor\frac{qs}{q+1}\right\rfloor.
\tag{8.20}
\]

For every target,

\[
 \boxed{
 R_S
 \le\frac12\sum_K
 \bigl(b_q(s_K)-1\bigr)_+|d_K(S)|.
 }
\tag{8.21}
\]

Define the size profile

\[
 \Xi_{\sigma,H}
 =\sum_{q\le H}\frac1{c_q}
   \sum_Ks_K\bigl(b_q(s_K)-1\bigr)_+.
\tag{8.22}
\]

Then

\[
 \boxed{
 \mathbf R_\sigma\le\frac n2\Xi_{\sigma,H}.
 }
\tag{8.23}
\]

#### Proof

Corollary 7.3 gives \(|d_K(S)|\le b_q(s_K)\).  For an integer
\(0\le t\le b\),

\[
 \binom t2\le\frac{(b-1)t}{2}.
\]

This proves (8.21).  For each component and depth,

\[
 \sum_S|d_K(S)|\le\sum_S(x_K(S)+y_K(S))=2ns_K.
\]

Sum (8.21), include the factor \(1/2\) in the definition of
\(\mathbf R_\sigma\), and obtain (8.23).  \(\square\)

To pay \(\mathbf R_\sigma\) entirely from the scale-correct one-step residue

\[
 O_A\left(\frac{H_AB}{n}\right),
\]

the size-only estimate (8.23) requires

\[
 \boxed{
 \Xi_{\sigma,H_A}=O_A\left(\frac{H_AB}{n^2}\right).
 }
\tag{8.24}
\]

This certificate is extraordinarily rigid.  For every \(q\ge2\) and every
\(s\ge3\), \(b_q(s)-1\ge1\).  Since \(c_q\le C_A\), summing over
\(2\le q\le H_A\) shows, for all sufficiently large \(m\), that (8.24) forces
all but

\[
 \boxed{O_A(B/n^2)}
\tag{8.25}
\]

owners into components of size at most two.  This is a sufficient certificate, not
a necessary condition: a large component can still have \(|d_K(S)|\le1\) for all
controlled targets.

For a one-sided hole-to-duplicate target, say \(\sum_Kx_K=0\) and
\(\sum_Ky_K=t\), all \(d_K\ge0\), so \(M_S=0\) and

\[
 D_S=\binom t2-\sum_K\binom{y_K}2
 =\sum_{K<J}y_Ky_J.
\tag{8.26}
\]

This is the clean regime in which fragmentation literally equals duplicate
separation.  Balanced and adjacent-load targets are the obstruction: they have no
\(B_S\)-budget with which to pay opposite-sign mixing.

---

## 9. Why unsigned expansion cannot force the heat sign

The residual identity yields several exact no-go theorems.  They are stronger than
the observation that connectivity can be bad.

### Proposition 9.1 (merging has a signed, nonmonotone effect)

If two components \(U,V\) are merged, then at a fixed target

\[
 \boxed{
 (M_S+R_S)_{\rm merged}-(M_S+R_S)_{\rm old}
 =d_U(S)d_V(S).
 }
\tag{9.1}
\]

Equivalently,

\[
 D_S^{\rm merged}-D_S^{\rm old}=-d_U(S)d_V(S).
\tag{9.2}
\]

In the weighted vector notation, merging endpoint bundles \(U,V\) changes the fair
gap by

\[
 \boxed{-\frac12\langle\Delta_U,\Delta_V\rangle_H.}
\tag{9.3}
\]

#### Proof

Use

\[
 M_S+R_S=\frac{\sum_Kd_K(S)^2-|z_S|}{2}.
\]

Replacing \(d_U,d_V\) by \(d_U+d_V\) changes the numerator by
\(2d_Ud_V\).  Equation (9.3) is the same calculation after summing targets and
depths, with the factor \(1/2\) from the direct fair formula.  \(\square\)

Same-sign merging traps duplicate residuals and hurts.  Opposite-sign merging
performs internal cancellation and helps.  Layered joins therefore have no unsigned
monotonicity.

### Theorem 9.2 (exact transposition-cube orientation no-go)

Fix a transposition \(\tau\) and its components, and let
\(\Delta_1,\ldots,\Delta_k\) be their effects in the weighted fixed-window Hilbert
space.  Every orientation

\[
 \varepsilon\in\{\pm1\}^k
\]

is a genuine integral exact factor in the same component cube.  At that vertex, the
fair decrease offered by the \(\tau\)-cube is

\[
 \boxed{
 h(\varepsilon)
 =\frac14\left(
 \left\|\sum_K\varepsilon_K\Delta_K\right\|_H^2
 -\sum_K\|\Delta_K\|_H^2
 \right)
 =\frac12\sum_{K<J}\varepsilon_K\varepsilon_J
   \langle\Delta_K,\Delta_J\rangle_H.
 }
\tag{9.4}
\]

Moreover,

\[
 \boxed{\mathbb E_\varepsilon h(\varepsilon)=0.}
\tag{9.5}
\]

If some off-diagonal Gram entry is nonzero, \(h\) takes both positive and negative
values on genuine cube vertices.  If all off-diagonal entries vanish, \(h\equiv0\).

#### Proof

The first-wave component-equivariance theorem identifies \(\tau F_\varepsilon\)
with the complementary orientation.  Thus the endpoint displacement at orientation
\(\varepsilon\) is \(\sum_K\varepsilon_K\Delta_K\), while the independent component
variance is \(\sum_K\|\Delta_K\|^2\).  The fair formula gives (9.4).

Every nonconstant Walsh monomial \(\varepsilon_K\varepsilon_J\) has mean zero, which
proves (9.5).  A nonzero real function with mean zero cannot be everywhere
nonnegative or everywhere nonpositive.  \(\square\)

All side-swap-invariant data are unchanged across this cube, including:

* component count and component sizes;
* internal owner-edge expansion, cycle rank, and collision multiplicities;
* every targetwise magnitude \(|d_K(S)|\);
* every absolute leakage magnitude \(|g_K(S)|\);
* the condition \(R_S=0\) for every target.

Therefore no condition using only those unsigned data can force positive fair heat
at every factor having that geometry.  The minimal missing datum is the signed Gram
graph

\[
 w_{KJ}=\langle\Delta_K,\Delta_J\rangle_H.
\tag{9.6}
\]

For a selected component cut \(I\), the exact energy change is

\[
 \boxed{
 \mathcal Q_H(F_I)-\mathcal Q_H(F)
 =-\left\langle
 \sum_{K\in I}\Delta_K,
 \sum_{J\notin I}\Delta_J
 \right\rangle_H.
 }
\tag{9.7}
\]

To audit (9.7), write \(u=\sum_{K\in I}\Delta_K\) and
\(v=\sum_{J\notin I}\Delta_J\).  Relabelling sends the \(I\)-child to the
complementary child, so their energy changes are equal; switching every component
also preserves energy.  Adding the two equal changes gives \(-2\langle u,v\rangle\),
and hence either one equals \(-\langle u,v\rangle\).

Thus a beneficial correlated cut exists exactly when the signed Gram graph has a
positive-weight cut.  This is the route-minimal positive-cut problem; it is strictly
weaker than requiring the fair total correlation to be positive.

The elementary sharpness patterns are

\[
 (d_1,d_2)=(1,1)\Longrightarrow D=1,
 \qquad
 (1,-1)\Longrightarrow D=-1.
\tag{9.8}
\]

They have identical unsigned fragmentation.  These two-entry patterns are algebraic
sharpness witnesses, not asserted whole-factor realizations.

### Corollary 9.3 (global-minimizer obstruction)

Let \(F_*\) minimize \(\mathcal Q_H\) over all exact factors.  For every coordinate
permutation \(\sigma\), every direct-component child is exact, so

\[
 \boxed{
 A_{\sigma,H}-V_{\sigma,H}\le0,
 \qquad
 \mathbf B_\sigma-\mathbf M_\sigma-\mathbf R_\sigma\le0.
 }
\tag{9.9}
\]

Hence no unconditional theorem can say that some well-chosen direct permutation has
strictly positive fair heat for every exact factor.  This does not refute a
thresholded floor alternative: the global minimizer might already satisfy
\(\mathcal Q_H=O_A(H_AB)\).

---

## 10. The exact signed direct-overlay gate

The preceding negative results isolate a precise positive theorem which would be
sufficient.  It is not proved here.

Put

\[
 E_A=\frac{H_AB}{n}.
\tag{10.1}
\]

### Open gate 10.1 (direct signed colour gate; unproved)

For every fixed \(A\), there should exist constants
\(\kappa_A,\delta_A>0\), \(C_A^E,C_A^F<\infty\), and \(m_0(A)\) such that,
for every \(m\ge m_0(A)\) and every exact factor \(F\), there is one coordinate
permutation \(\sigma=\sigma(F)\) for which, simultaneously,

\[
 \boxed{
 \mathbf B_\sigma
 \ge\frac{\kappa_A}{n}\mathcal Q_{H_A}(F)-C_A^E E_A,
 }
\tag{10.2}
\]

and

\[
 \boxed{
 \mathbf M_\sigma+\mathbf R_\sigma
 \le(1-\delta_A)\mathbf B_\sigma+C_A^F E_A.
 }
\tag{10.3}
\]

The same \(\sigma\) is required in both inequalities.

### Theorem 10.2 (conditional exact-factor implication)

If Open gate 10.1 holds, then some integral exact child \(G\) satisfies

\[
 \boxed{
 \mathcal Q_{H_A}(G)
 \le
 \left(1-\frac{\delta_A\kappa_A}{n}\right)
 \mathcal Q_{H_A}(F)
 +(\delta_AC_A^E+C_A^F)\frac{H_AB}{n}.
 }
\tag{10.4}
\]

At a global minimizer,

\[
 \boxed{
 \mathcal Q_{H_A}(F_*)
 \le
 \frac{\delta_AC_A^E+C_A^F}{\delta_A\kappa_A}
 H_AB.
 }
\tag{10.5}
\]

Consequently the fixed-window overload is \(o(W)\), and the audited diagonalization
then gives MWB.

#### Proof

Equations (8.17), (10.2), and (10.3) give the expected decrease

\[
 \mathbf B_\sigma-\mathbf M_\sigma-\mathbf R_\sigma
 \ge
 \frac{\delta_A\kappa_A}{n}\mathcal Q_{H_A}(F)
 -(\delta_AC_A^E+C_A^F)E_A.
\]

Some integral child is no worse than the expectation, which proves (10.4).  At a
global minimizer the left side cannot be positive; rearranging gives (10.5).

For every rank, the floor energy is at least twice the overload.  Also

\[
 H_AB=H_A\frac Wn=O_A(W/\sqrt m)=o(W).
\]

The fixed-window overload and MWB implications are the previously audited
diagonalization route.  \(\square\)

For one fixed \(\sigma\), the exact necessary-and-sufficient fair inequality at
the contraction scale is simply

\[
 \boxed{
 \mathbf M_\sigma+\mathbf R_\sigma
 \le\mathbf B_\sigma
 -\frac{\eta_A}{n}\mathcal Q_{H_A}(F)+C_AE_A.
 }
\tag{10.6}
\]

Equation (10.6), not ordinary Cheeger expansion, is the minimal fair direct-overlay
gate.  A strong targetwise sufficient condition is:

\[
 d_K(S)\in\{0,1\}\text{ for all }K
\quad\text{or}\quad
 d_K(S)\in\{0,-1\}\text{ for all }K,
\tag{10.7}
\]

according to the sign of \(z_S\).  Then \(M_S=R_S=0\) and \(D_S=B_S\).
The challenge is to realize this common orientation simultaneously over all targets
and all depths inside one exact overlay.

---

## 11. Exact bridge to the corrected global component-noise gate

The global component-noise proposal uses only transpositions, counted once each.
For a transposition \(\tau\), let \(K\) run over its equivariant components and set

\[
 N_{\tau,H}=\sum_K\sum_{q\le H}
 \frac{\|\Delta_{\tau,K,q}\|_2^2}{c_q},
\tag{11.1}
\]

\[
 A_{\tau,H}=\sum_{q\le H}
 \frac{\|\tau\mu_q-\mu_q\|_2^2}{c_q}.
\tag{11.2}
\]

Put

\[
 R_H=\sum_\tau N_{\tau,H},
 \qquad D_H=\sum_\tau A_{\tau,H}.
\tag{11.3}
\]

For an unordered moved target pair \(p=\{S,\tau S\}\), orient it once and write

\[
 d_{K,p}=x_K(S)-x_K(\tau S),
 \qquad z_p=\sum_Kd_{K,p}.
\tag{11.4}
\]

Define \(B_p,M_p,R_p\) as in (8.5), and their weighted sums

\[
 \mathfrak B_\tau=\sum_{q,p}\frac{B_p}{c_q},
 \qquad
 \mathfrak M_\tau=\sum_{q,p}\frac{M_p}{c_q},
 \qquad
 \mathfrak R_\tau=\sum_{q,p}\frac{R_p}{c_q}.
\tag{11.5}
\]

### Proposition 11.1 (the first global slack is signed leakage misalignment)

\[
 \boxed{
 A_{\tau,H}-N_{\tau,H}
 =4(\mathfrak B_\tau-\mathfrak M_\tau-\mathfrak R_\tau).
 }
\tag{11.6}
\]

Consequently,

\[
 \boxed{
 R_H-D_H
 =4\sum_\tau
 (\mathfrak M_\tau+\mathfrak R_\tau-\mathfrak B_\tau).
 }
\tag{11.7}
\]

At a global minimizer, every summand on the right of (11.7) is nonnegative.

#### Proof

Component equivariance gives

\[
 \|\Delta_{K,q}\|_2^2=2\sum_pd_{K,p}^2,
 \qquad
 \|\tau\mu_q-\mu_q\|_2^2=2\sum_pz_p^2.
\]

Thus

\[
 A_{\tau,H}-N_{\tau,H}
 =2\sum_{q,p}\frac{z_p^2-\sum_Kd_{K,p}^2}{c_q}
 =4\sum_{q,p}\frac{B_p-M_p-R_p}{c_q}.
\]

At a global minimizer, fair switching inside this one \(\tau\)-cube cannot lower
the energy, so \(N_{\tau,H}\ge A_{\tau,H}\).  \(\square\)

Decompose \(f_q\) into Johnson harmonics.  Since total and point margins vanish,
only degrees \(j\ge2\) occur.  The audited spectrum gives

\[
 \boxed{
 D_H-4(n-1)(B_H^{\rm floor}+\Phi_H)
 =2\sum_{q\le H}\frac1{c_q}
   \sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
 }
\tag{11.8}
\]

### Theorem 11.2 (corrected three-slack identity in target-colour form)

At every global minimizer,

\[
 \boxed{
 \begin{aligned}
 R_H-4(n-1)B_H^{\rm floor}
 ={}&4\sum_\tau
 (\mathfrak M_\tau+\mathfrak R_\tau-\mathfrak B_\tau)\\
 &+2\sum_{q\le H}\frac1{c_q}
   \sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2\\
 &+4(n-1)\Phi_H.
 \end{aligned}
 }
\tag{11.9}
\]

All three displayed terms on the right are nonnegative.

#### Proof

Insert (11.7) and (11.8) into the tautological decomposition

\[
 \begin{aligned}
 R_H-4(n-1)B_H^{\rm floor}
 ={}&(R_H-D_H)\\
 &+[D_H-4(n-1)(B_H^{\rm floor}+\Phi_H)]\\
 &+4(n-1)\Phi_H.
 \end{aligned}
\]

Nonnegativity follows respectively from global minimality, the Johnson spectrum,
and the definition of floor energy.  \(\square\)

The corrected upper gate

\[
 R_H\le4(n-1)B_H^{\rm floor}+o(nW)
\tag{11.10}
\]

therefore demands all of the following:

\[
 \sum_\tau(\mathfrak M_\tau+\mathfrak R_\tau-\mathfrak B_\tau)=o(nW),
\tag{11.11}
\]

\[
 \sum_{q,j\ge3}\frac{(j-2)(n-j-1)}{c_q}
 \|f_q^{(j)}\|_2^2=o(nW),
\tag{11.12}
\]

and

\[
 \Phi_H=o(W).
\tag{11.13}
\]

Thus the gate already contains the desired quadratic conclusion plus two additional
near-equalities.  Connectivity of one transposition overlay merely makes that
transposition's contribution to (11.11) zero.  It does not control (11.12) or
(11.13).

There is also a scope separation which must not be blurred: Theorem 3.4 chooses one
arbitrary permutation \(\sigma\), whereas \(R_H\) in (11.3) sums the component
noise of **all transpositions**.  No comparison between the chosen direct
\(P_\sigma\) and this all-transposition quantity is proved.  Such a comparison would
itself be a new theorem.

---

## 12. Comparison with genuine size-two fragmentation

The first-wave MSW theorem, used here only as an imported comparison, supplies for
its distinguished transposition at least \(\operatorname{Cat}_{m-2}\) size-two
components.  Lemma 2.3 therefore forces its direct collision mass to satisfy

\[
 \boxed{
 P_\tau\ge2m^2\operatorname{Cat}_{m-2}
 \sim\frac18m^2B.
 }
\tag{12.1}
\]

By contrast, Theorem 3.4 gives a permutation with

\[
 P_\sigma\le(4+o(1))B.
\tag{12.2}
\]

Thus positive-density exact size-two fragmentation is paid for by a
\(\Theta(m^2)\) increase in root-level parallel collision.  The comparison makes
the anti-fragmentation conclusion concrete inside the exact-factor universe.

The MSW size-two cells force \(R_S=0\) for their local residuals at every depth.
They do not control the larger components or the global opposite-sign term \(M_S\).
Accordingly, neither the first-wave MSW theorem nor the second-wave collision theorem
proves the signed gate.

---

## 13. Independent audit of the decisive steps

The report was assembled from three independent proof attacks and then rederived
line by line.  The following are the decisive audit checks.

### Audit A: collision expectation and constants

For fixed \(C,D\), \(\binom{a_{CD}^\sigma}{2}\) counts unordered pairs which are
simultaneously in one left and one right block.  At distance \(d\), the source row
has \(n\) pairs and the probability that a uniform image pair lies in the target row
is

\[
 \frac{n}{(W/2)\binom md\binom{m+1}d}.
\]

This independently reproduces the factor \(2n^2/W\) in (3.4), and summing
\(B^2\) entries independently reproduces \(2WS_m\), with no missing ordered-pair
factor.

The endpoint terms \(d=1,m\) sum exactly to \(1/m\).  The ratio calculation
(3.7), not an asymptotic estimate, proves the stated strict \(6/m^3\) remainder for
every \(m\ge4\).

### Audit B: component-count constant

On every component, the intersection submatrix has total \(ns\) spread over
\(s^2\) entries.  Its squared Frobenius mass is at least \(n^2\), independent of
\(s\).  Since

\[
 \sum_{C,D}(a_{CD}^\sigma)^2=nB+2P_\sigma,
\]

the exact global constant is

\[
 k_\sigma n^2\le nB+2P_\sigma.
\]

With \(P_\sigma\le2nBS_m\), this is
\(k_\sigma\le(B/n)(1+4S_m)\).  This improves the weaker threshold-splitting bound
\((B/n)(1+2\sqrt{S_m})^2\); the latter is valid but not used in the final theorem.

### Audit C: arbitrary-\(\sigma\) scope

For a direct component, the root edge set \(U_K\) is common to its two sides.
It need not be \(\sigma\)-invariant, and in general

\[
 y_K(S)\ne x_K(\sigma^{-1}S).
\]

The proof of Theorem 7.2 uses only equality of the two root unions.  It never invokes
component equivariance.  Example 2.6 genuinely shows why the stronger assertion
would be false.

### Audit D: fair-heat factors

For each target,

\[
 A_{\sigma,q}-V_{\sigma,q}
 =z_S^2-\sum_Kd_K(S)^2=2D_S.
\]

Fair midpoint variance supplies the additional factor \(1/4\), so the decrease is
\(D_S/2\) for an arbitrary oriented target sum.  In a transposition orbit the two
targets duplicate this value, recovering the old unordered-pair decrease \(D_p\).
This audits every factor \(2\), \(1/2\), and \(1/4\) in Sections 8 and 11.

### Audit E: transposition-boundary constant

The centered root-union indicator has squared norm

\[
 na(1-a/B)
\]

and no Johnson degrees zero or one.  The \(j=2\) Laplacian eigenvalue is
\(2(n-1)\), so its Johnson boundary is at least
\(2n(n-1)a(1-a/B)\).  Because each Johnson edge belongs to one coordinate
transposition, no extra factor two appears in (4.4).  Equivalently,
\(\|g-\tau g\|^2=2\partial_\tau A\) and the all-transposition norm identity has
factor \(4(n-1)\); the same constant results.

### Audit F: layered versus direct overlays

Theorem 5.1 concerns a join of pulled-back transposition partitions.  Corollary 5.3
therefore proves connectivity only of the **layered endpoint bundle partition**.
It makes no claim about the direct overlay of the two endpoint factors.  This scope
restriction is essential and is stated at every use.

### Audit G: corrected global noise

The global \(R_H\) is unscaled component variance and is four times fair conditional
variance.  Transpositions are unordered and counted once.  With these conventions,

\[
 R_H-D_H=4\sum(\mathfrak M+\mathfrak R-\mathfrak B),
\]

and the Johnson baseline is \(4(n-1)\), not \(2n\).  These are the corrected
first-wave constants used in (11.9).

---

## 14. Final theorem status and genuine remainder

### Proved in this report

1. The direct-overlay partition-intersection and common-subspace theorem.
2. Sharp local collision lower bounds and the global component-count inequality.
3. The exact uniform-permutation collision average \(2WS_m\), including
   \(1/m\le S_m<1/m+6/m^3\).
4. Existence of a length-at-most-\((n-1)\) direct permutation with
   \((1+O(1/m))B/n\) components and only \(O(B/n)\) owners in components of
   size at most \(n/2\).
5. Prescribed-cut direct expansion with simultaneous low collision.
6. Sharp transposition-family owner-cut isoperimetry and partition turnover.
7. The group-orbit bound for joins and universal spanning-tree layered collapse.
8. A nonzero invariant pure-degree-two tangent for every single coordinate
   permutation.
9. Two-sided containment leakage and fragmentation for arbitrary direct overlays.
10. The general targetwise \(B-M-R\) identity, parity correction, and exact fair
    heat constants.
11. The size-profile certificate and its \(O_A(B/n^2)\) small-component rigidity.
12. The transposition-cube orientation no-go and the signed merge law.
13. The exact target-colour form of the corrected three-slack noise identity.

### Not proved, and not claimed

1. No theorem \(\forall F\,\exists\sigma\) asserting that the direct overlay is
   connected.
2. No single-\(\sigma\) all-cuts Cheeger theorem \(\exists\sigma\,\forall A\).
3. No implication from low root collision to favourable lower-rank leakage signs.
4. No implication from component sizes, connectivity, or cycle rank to control of
   \(M_S\).
5. No proof of Open gate 10.1 or of the weaker positive-cut/local-minimum theorem.
6. No adaptive sequential theorem after recomputing components at each step.
7. No exact-factor realization of the invariant signed degree-two vectors in
   Theorem 6.1.
8. No derivation of the corrected all-transposition noise gate from the one-permutation
   collision theorem.
9. No labelled common-owner synchronization theorem, and no implication to such a
   labelled statement.

### Exhausted conclusion

Ordinary ownership expansion has now been proved in three strong forms: transverse
direct partitions, Johnson cut expansion across transpositions, and full layered
coalescence under a spanning-tree word.  Each form either forces large components or
merges all components.  Neither behaviour supplies occurrence-pair heat.

The cross-rank leakage theorem shows why.  A middle component has no middle-rank
effect; its lower-rank effect is entirely the signed difference of its two noncyclic
containment leakages.  Duplicate separation measures the square of the **sum** of
these leakage gradients, whereas component noise measures the **sum of their
squares**.  Unsigned geometry cannot compare the two.  The exact missing statement
is therefore a target-coloured correlation theorem, at the scale

\[
 \frac1{4}
 \sum_{q,S}\frac{
 (\sum_Kg_K(S))^2-\sum_Kg_K(S)^2
 }{c_q(q+1)^2}
 \ge
 \frac{\eta_A}{n}\mathcal Q_{H_A}(F)
 -O_A\left(\frac{H_AB}{n}\right),
\tag{14.1}
\]

or the still weaker existence of a positive cut in the signed component Gram graph.
Both remain unproved.  No further unsigned expansion or component-count argument can
close this lane without adding precisely that signed, targetwise information.
