# Second-wave Q: the corrected component-noise gate is false

## 1. Verdict

The corrected global component-noise gate

\[
R_H(F)\le 4(n-1)B_H+o_A(nW)
\tag{CN}
\]

is false, even when \(F\) is required to be a global minimizer of the same
fixed Gaussian-window floor objective.

More precisely, the following stronger opposite estimate holds.

### Main theorem

Fix \(A>0\), put

\[
n=2m+1,\qquad W=\binom nm,\qquad
H=\lceil A\sqrt m\rceil,
\]

and let \(F\) be any global minimizer, over exact middle wreath factors, of

\[
Q_H(F)=\sum_{q=1}^{H}\frac{Q_q(F)}{c_q},
\qquad
Q_q(F)=\|f_q\|_2^2-V_q^{\min}.
\]

The exact-factor fibre is finite and, by the frozen existence theorem,
nonempty, so such a minimizer exists. The threshold \(m_0(A)\) below is
understood to be large enough that \(H\le m-2\).

There are constants \(c_A>0\) and \(m_0(A)\) such that, for every
\(m\ge m_0(A)\),

\[
\boxed{
R_H(F)-4(n-1)B_H\ge c_A\,nW\sqrt m.}
\tag{1.1}
\]

Thus the proposed excess is not \(o_A(nW)\). It is at least a positive
\(A\)-dependent fraction of the natural \(nW\sqrt m\) Gaussian-window
scale.

The decisive new input is a robust Boolean-\(E_2\) theorem on central
Johnson slices. Its proof is self-contained: it uses an exact row-zero
quadratic representation, exact second and third moments, and a
dimension-free fourth-moment bound obtained from four-edge multigraphs.

This refutes only the component-noise sufficient route. It does not refute
MWB, \(LM_A\), RFEN, \(SCOV_A\), labelled synchronization, or the
contiguous-OR width conjecture.

## 2. Exact gate ledger

All sums indexed by \(q\le H\) below mean \(1\le q\le H\).

At depth \(q\), write

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\qquad c_q=\lfloor\lambda_q\rfloor,
\qquad 0\le\theta_q<1,
\]

\[
f_q=\mu_q-\lambda_q\mathbf1,
\qquad
V_q^{\min}=N_q\theta_q(1-\theta_q),
\]

and

\[
Q_q=\|f_q\|_2^2-V_q^{\min}\ge0.
\]

Because \(\sum_S(\mu_q(S)-c_q)=N_q\theta_q\), this variance excess has
the exact integral form

\[
Q_q
=\sum_{S\in\binom{[n]}{r_q}}
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{2.0}
\]

Use unnormalized counting norms on each rank layer and put

\[
B_H=\sum_{q\le H}\frac{V_q^{\min}}{c_q},
\qquad
S_H=\sum_{q\le H}\frac{\|f_q\|_2^2}{c_q}
=B_H+Q_H.
\]

Thus \(Q_H=\sum_{q\le H}Q_q/c_q\), in agreement with the objective in
the main theorem.

For an unordered coordinate transposition \(\tau\), let
\(\mathcal C_\tau(F)\) be the ownership-overlay components. If
\(u_{q,C}\) and \(w_{q,C}\) are the two side histograms, set

\[
d_{\tau,q,C}=w_{q,C}-u_{q,C},
\]

\[
N_{\tau,H}
=\sum_{C\in\mathcal C_\tau(F)}
 \sum_{q\le H}\frac{\|d_{\tau,q,C}\|_2^2}{c_q},
\]

\[
A_{\tau,H}
=\sum_{q\le H}
 \frac{\|\tau\mu_q-\mu_q\|_2^2}{c_q}.
\]

Finally,

\[
R_H=\sum_\tau N_{\tau,H},
\qquad
D_H=\sum_\tau A_{\tau,H}.
\]

Every component difference has zero total and zero point margins. Hence it
has no Johnson degrees zero or one. The same is true of every full centered
load \(f_q\).

Fair component switching and global minimality give

\[
N_{\tau,H}\ge A_{\tau,H}
\qquad\text{for every }\tau.
\tag{2.1}
\]

For unordered transpositions, the Johnson spectrum gives

\[
D_H-4(n-1)S_H
=2\sum_{q\le H}\frac1{c_q}
 \sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
\tag{2.2}
\]

Consequently the already audited three-slack identity is

\[
\boxed{
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)S_H\bigr)\\
&+4(n-1)Q_H.
\end{aligned}}
\tag{2.3}
\]

At a global minimizer all three terms on the right are nonnegative.
Equation (1.1) will follow by proving that the last two terms alone are
large on a positive proportion of the Gaussian depths.

## 3. Exact abstract stress tests

Before using exact ownership, it is useful to record that all three slacks
in (2.3) are algebraically independent under integrality, nonnegativity,
equivariance, and zero point margins.

Sections 3.2--3.3 use the unweighted one-rank ledger.
Multiplying every one-rank quadratic quantity by the same positive weight
\(1/c\) preserves which slacks vanish. In particular, the ratio in (3.5)
is only an unweighted algebraic stress test, not a true-factor gate-scale
claim. Section 3.4 returns to the weighted normalization of Section 2.

### 3.1 A pure \(E_2\) atom

Assume \(n\ge5\) and \(2\le r\le n-2\), and put
\(N=\binom nr\).
Fix distinct coordinates \(a,b,c,d\). On \(\binom{[n]}r\), define

\[
g_{ab,cd}(S)
=
(\mathbf1_{a\in S}-\mathbf1_{b\in S})
(\mathbf1_{c\in S}-\mathbf1_{d\in S}).
\tag{3.1}
\]

Then

\[
g_{ab,cd}\in\{-1,0,1\},
\]

\[
\sum_Sg_{ab,cd}(S)=0,
\qquad
\sum_{S\ni x}g_{ab,cd}(S)=0
\quad(x\in[n]),
\tag{3.2}
\]

and

\[
\boxed{
\|g_{ab,cd}\|_2^2
=4\binom{n-4}{r-2}.}
\tag{3.3}
\]

Indeed, swapping \(a,b\), or swapping \(c,d\), reverses the sign and
preserves every relevant counting class. The function is a quadratic
polynomial in the coordinate indicators. Since (3.2) removes its
\(E_0\) and \(E_1\) parts, it lies purely in \(E_2\).

### 3.2 A first-slack-only formal model

Take a prime \(n\ge5\), fix \(\tau=(a\,b)\), and let

\[
L=\binom{n-2}{2}.
\]

For every pair \(e=\{c,d\}\) disjoint from \(\{a,b\}\), prescribe two formal
components with side histograms

\[
u_e^\pm=\mathbf1\pm g_{ab,cd},
\qquad
w_e^\pm=\tau u_e^\pm=\mathbf1\mp g_{ab,cd}.
\tag{3.4}
\]

All side histograms are nonnegative and integral, have equal total mass,
and have equal uniform point margins. Their left-side sum is the constant
parent

\[
\mu=2L\mathbf1.
\]

Thus this parent has \(B=Q=D=0\) and is an absolute quadratic minimum.
Nevertheless,

\[
N_\tau=8L\|g_{ab,cd}\|_2^2.
\]

Prescribing the same construction for every transposition gives

\[
R=8\binom n2L\|g_{ab,cd}\|_2^2.
\]

If \(W'=2LN\) is the formal total mass, then along central ranks
\(r/n\to1/2\),

\[
\frac{R}{nW'}
=2(n-1)\frac{\|g_{ab,cd}\|_2^2}{N}
\sim\frac n2.
\tag{3.5}
\]

The entire gate excess is \(R-D\). This is a formal component system, not an
exact wreath factor.

### 3.3 A last-slack-only formal model

Continue to assume that \(n\) is prime.
Put

\[
\mu=\mathbf1+g_{ab,cd}
\]

and take its \(S_n\)-orbit as a formal state space. For every transposition,
declare one connected component with the two side histograms
\(\mu,\tau\mu\). Every orbit state has the same energy and is therefore a
global minimizer in this formal fibre. Here

\[
B=0,\qquad Q=\|g_{ab,cd}\|_2^2,
\]

\[
R=D=4(n-1)\|g_{ab,cd}\|_2^2.
\]

The switching and spectral slacks vanish, and the whole excess is the final
term \(4(n-1)Q\).

### 3.4 A floor-balanced spectral-slack model at the actual normalization

Again let \(n=2m+1\) be prime. Fix \(2\le r\le n-2\), and put

\[
N=\binom nr,\qquad W=\binom nm,\qquad
c=\left\lfloor\frac WN\right\rfloor,\qquad W=cN+t,
\qquad 0\le t<N.
\]

Primality and \(0<r<n\) give

\[
N=\frac nr\binom{n-1}{r-1}.
\]

Since \(\gcd(n,r)=1\), the equivalent identity
\(rN=n\binom{n-1}{r-1}\) gives \(n\mid N\). Also

\[
\frac Wn=\frac1{m+1}\binom{2m}{m}
\]

is the \(m\)-th Catalan number, so \(n\mid W\). Hence \(n\mid t\).
A fixed coordinate \(n\)-cycle partitions the rank layer into

\[
L=N/n
\]

orbits of size \(n\). Each orbit is a \(1\)-design: every coordinate occurs
in exactly \(r\) of its sets. Indeed, a nonidentity element of the cyclic
group generates the whole group because \(n\) is prime, while no nonempty
proper \(r\)-set is invariant under the full coordinate cycle. Thus the
action is free; transitivity on coordinates then makes all point counts
equal, and their sum is \(nr\).

Choose \(k=t/n\) complete orbits and let \(\mathcal B\) be their union. Then

\[
\theta=\frac tN=\frac kL.
\]

Moreover,

\[
\mu=c\mathbf1+\mathbf1_{\mathcal B}
\tag{3.6}
\]

is exactly floor-balanced, has total mass \(W\), and has point margin
\(rW/n\). Its centered vector

\[
f=\mathbf1_{\mathcal B}-\frac{k}{L}\mathbf1
\]

has

\[
\|f\|_2^2=V^{\min}=N\theta(1-\theta),
\qquad Q=0,
\]

and no \(E_1\) part.

Choose the \(k\) orbits uniformly. If \(z_\ell\) is the indicator that the
\(\ell\)-th orbit was chosen, then

\[
\operatorname{Var}(z_\ell)=\theta(1-\theta),
\qquad
\operatorname{Cov}(z_\ell,z_{\ell'})
=-\frac{\theta(1-\theta)}{L-1}
\quad(\ell\ne\ell').
\]

In the orthonormal orbit basis
\(n^{-1/2}\mathbf1_{\mathcal O_\ell}\), the coefficients of \(f\) are
\(\sqrt n(z_\ell-\theta)\). Hence, on the mean-zero orbit-constant
subspace, the covariance is the scalar

\[
\frac{V^{\min}}{L-1}I.
\]

Therefore

\[
\mathbb E\|P_{E_2}f\|_2^2
\le
\frac{V^{\min}}{L-1}\dim E_2
=
\frac{V^{\min}}{L-1}\frac{n(n-3)}2.
\tag{3.7}
\]

At a Gaussian rank \(r=m-q\) with \(q=O(\sqrt m)\), the exact binomial
ratio used again in Section 9 gives \(N=\Theta(W)\). Since \(W\) is a
largest binomial coefficient and \(\sum_r\binom nr=2^n\),
\(W\ge2^n/(n+1)\). Hence \(L=N/n\) is exponential in \(n\), while
\(\dim E_2=O(n^2)\). It follows from (3.7) that some orbit union has

\[
\|P_{\ge3}f\|_2^2=(1-o(1))V^{\min}.
\]

On its formal \(S_n\)-orbit fibre, declare one component for every
transposition. In the weighted one-rank normalization, each transposition
has \(N_\tau=A_\tau=\|\tau\mu-\mu\|_2^2/c\). Hence
\(R=D\), \(B=V^{\min}/c\), and \(Q=0\). Thus

\[
R-4(n-1)B
\ge
\frac{2(n-4)}c\|P_{\ge3}f\|_2^2
=\Omega(nW)
\tag{3.8}
\]

at fixed Gaussian ranks \(r=m-q\), \(q=O(\sqrt m)\), whenever
\(\theta\) stays away from zero and one; here \(c=O(1)\) and
\(N=\Theta(W)\).

Thus the middle spectral slack can also be large by itself. These three
models show that no argument using only the linear margin and component
axioms can prove the gate. None of them is an exact middle ownership
factor. The refutation below is stronger: it applies to genuine exact
factors.

## 4. Quadratic representation of \(E_2\)

Let \(X\) be uniform on \(\binom{[n]}r\), and use normalized expectation in
Sections 4--7. Assume throughout these sections that
\(n\ge6\) and \(2\le r\le n-2\).

Let \(\mathcal A\) be the space of symmetric matrices \(A=(a_{ij})\) such
that

\[
a_{ii}=0,
\qquad
\sum_{j\ne i}a_{ij}=0
\quad(i\in[n]).
\tag{4.1}
\]

Define

\[
h_A(X)=\sum_{\{i,j\}\subseteq X}a_{ij}.
\tag{4.2}
\]

### Proposition 4.1

The map \(A\mapsto h_A\) is an isomorphism from \(\mathcal A\) onto the
Johnson harmonic space \(E_2\).

### Proof

The row-sum map on symmetric zero-diagonal matrices has rank \(n\). Indeed,
a vector orthogonal to all its edge columns would satisfy
\(y_i+y_j=0\) for every \(i\ne j\), which forces \(y=0\) when \(n\ge3\).
Therefore

\[
\dim\mathcal A=\binom n2-n=\dim E_2.
\]

Equation (4.1) gives

\[
\sum_{i<j}a_{ij}=0.
\]

It also gives

\[
\begin{aligned}
\mathbb E[h_A(X)\mathbf1_{x\in X}]
={}&
\rho_2\sum_{j\ne x}a_{xj}\\
&+\rho_3\sum_{\substack{i<j\\i,j\ne x}}a_{ij}
=0
\end{aligned}
\qquad(x\in[n]).
\]

Here \(\rho_s=(r)_s/(n)_s\), as in the next section.

Thus \(h_A\) is orthogonal to \(E_0\oplus E_1\), so its image lies in
\(\bigoplus_{j\ge2}E_j\). Since it is a quadratic function, it lies in
\(E_2\).

The positive second-moment formula in Proposition 5.1 below proves
injectivity. Equality of dimensions finishes the proof. \(\square\)

## 5. Exact second and third moments

Put

\[
\rho_s=\frac{(r)_s}{(n)_s},
\qquad
L=\sum_{i<j}a_{ij}^2,
\]

\[
U=\sum_{i<j}a_{ij}^3,
\qquad
T=\sum_{i<j<k}a_{ij}a_{ik}a_{jk}.
\]

### Proposition 5.1

For \(h=h_A\in E_2\),

\[
\boxed{
\mathbb Eh^2=v_{n,r}L,}
\tag{5.1}
\]

where

\[
v_{n,r}
=\rho_2-2\rho_3+\rho_4
=
\frac{r(r-1)(n-r)(n-r-1)}
{n(n-1)(n-2)(n-3)}.
\tag{5.2}
\]

Moreover,

\[
\boxed{
\mathbb Eh^3=\alpha_{n,r}U+6\beta_{n,r}T,}
\tag{5.3}
\]

where

\[
\alpha_{n,r}
=\rho_2-6\rho_3+13\rho_4-12\rho_5+4\rho_6,
\tag{5.4}
\]

\[
\beta_{n,r}
=\rho_3-3\rho_4+3\rho_5-\rho_6.
\tag{5.5}
\]

### Proof of the second moment

In the expansion of \(h^2\), an equal edge has union size two, two distinct
adjacent edges have union size three, and two disjoint edges have union size
four.

The row-zero identities give

\[
\sum_{\substack{e<f\\e\cap f\ne\varnothing}}a_ea_f=-L.
\]

Since the total edge sum is zero,

\[
\sum_{\substack{e<f\\e\cap f=\varnothing}}a_ea_f=\frac L2.
\]

Substitution gives

\[
\mathbb Eh^2
=\rho_2L+2\rho_3(-L)+2\rho_4(L/2),
\]

which is (5.1). Direct simplification gives (5.2). \(\square\)

### Proof of the third moment

For three distinct edges, let the product sums be grouped by their union
multigraph. The exact identities are

\[
\begin{array}{c|c}
\text{three-edge graph}&\text{product sum}\\ \hline
\text{triangle}&T\\
\text{three-star}&2U/3\\
\text{four-vertex path}&U-3T\\
\text{adjacent pair plus a disjoint edge}&3T-2U\\
\text{three-edge matching}&2U/3-T.
\end{array}
\tag{5.6}
\]

Here is a derivation.

For one zero-sum matrix row, Newton's identity gives

\[
\sum_{j<k<\ell}a_{ij}a_{ik}a_{i\ell}
=\frac13\sum_j a_{ij}^3.
\]

Summing over centers proves the three-star row of (5.6).

If \(P\) denotes the four-vertex path sum, summing over oriented paths gives

\[
2P=2U-\operatorname{tr}(A^3)=2U-6T,
\]

which proves the path row.

For a fixed three-vertex set with edge weights \(x,y,z\), choosing two
adjacent edges and then an edge disjoint from those three vertices gives

\[
(xy+xz+yz)(x+y+z).
\]

Indeed, summing the three row-zero equations shows that the total weight of
edges crossing from the three vertices to their complement is
\(-2(x+y+z)\). Since the total weight of all edges is zero, the total weight
of edges wholly outside those vertices is therefore \(x+y+z\). After
summation, the
squared-edge terms total \(-2U\), while the triangle terms total \(3T\).
This proves the adjacent-plus-disjoint row.

Finally, the third elementary symmetric sum of the complete edge-weight
list is \(U/3\), because the total edge weight is zero. Subtracting the
other four graph types gives the matching row.

The terms with one edge repeated twice contribute

\[
3(-2\rho_3+\rho_4)U.
\]

Indeed, for a fixed edge \(e\), the sum of the other adjacent edge weights
is \(-2a_e\), while the sum of the edge weights disjoint from \(e\) is
\(a_e\).

Adding the three-equal-edge term \(\rho_2U\) and the five distinct-edge
types in (5.6) gives exactly (5.3)--(5.5). \(\square\)

#### Independent audit of the moment formulas

There is a second derivation which does not use the five graph-sum
identities. Let \(X_1,\ldots,X_n\) be independent Bernoulli-\(x\) variables
and put \(Y_i=X_i-x\). The row-zero identities give the polynomial identity

\[
\sum_{i<j}a_{ij}X_iX_j
=\sum_{i<j}a_{ij}Y_iY_j.
\]

In the product-measure second moment, every edge pair except a repeated
edge has a degree-one endpoint and hence zero expectation. In the third
moment, the only surviving edge multisets are a triply repeated edge and a
triangle. Consequently

\[
\mathbb E_xh^2
=L\bigl(x^2-2x^3+x^4\bigr),
\]

and

\[
\mathbb E_xh^3
=U\bigl(x^2-6x^3+13x^4-12x^5+4x^6\bigr)
+6T\bigl(x^3-3x^4+3x^5-x^6\bigr).
\]

For each fixed edge tuple, product measure assigns the factor \(x^s\),
where \(s\) is the number of distinct endpoints, while the uniform
\(r\)-slice assigns \(\rho_s\). Replacing every \(x^s\) in the two preceding
polynomial identities by \(\rho_s\) therefore recovers (5.1)--(5.5)
exactly. This independently
checks the decisive cubic coefficients and every endpoint multiplicity.

### Corollary 5.2: an exact skewness bound

One has

\[
|U|\le L^{3/2}.
\]

Also

\[
6T=\operatorname{tr}(A^3),
\qquad
\operatorname{tr}(A^2)=2L.
\]

Schatten Hölder therefore gives

\[
|6T|\le(2L)^{3/2}=2\sqrt2\,L^{3/2}.
\]

Consequently, if \(h\ne0\),

\[
\boxed{
\frac{|\mathbb Eh^3|}{(\mathbb Eh^2)^{3/2}}
\le
C_{n,r}:=
\frac{|\alpha_{n,r}|+2\sqrt2|\beta_{n,r}|}
{v_{n,r}^{3/2}}.}
\tag{5.7}
\]

Uniformly for \(n=2m+1\) and \(|r-m|\le C\sqrt m\),

\[
v_{n,r}\longrightarrow\frac1{16},
\qquad
\alpha_{n,r}\longrightarrow0,
\qquad
\beta_{n,r}\longrightarrow\frac1{64}.
\]

Thus

\[
\boxed{C_{n,r}\longrightarrow2\sqrt2}
\tag{5.8}
\]

uniformly in every fixed Gaussian rank window.

## 6. A dimension-free fourth-moment bound

The third-moment argument needs a uniform way to transfer moments from a
Boolean function to its \(E_2\) projection.

### Proposition 6.1

There is an absolute constant \(K<\infty\) such that, whenever

\[
n\ge6,\qquad \frac n3\le r\le\frac{2n}3,
\]

every \(h\in E_2\) satisfies

\[
\boxed{\|h\|_4\le K\|h\|_2}
\tag{6.1}
\]

in normalized slice measure.

One may take the deliberately crude value

\[
K=18\cdot2^{32}.
\]

### Proof

Write \(h=h_A\) as in Proposition 4.1. From (5.2),

\[
v_{n,r}\ge\frac1{324},
\tag{6.2}
\]

because each of \(r,r-1,n-r,n-r-1\) is at least the corresponding crude
fraction \(n/3,n/6,n/3,n/6\).

Expand

\[
h=\frac12\sum_{i\ne j}a_{ij}X_iX_j
\]

to the fourth power. Group the eight endpoint slots by their equality
partition. There are at most \(8^8\) partitions. Every nonzero term is a
factor \(p_s\in[0,1]\), the probability that a fixed \(s\)-set lies in the
random slice member, times an injective labeling sum of a loopless
four-edge multigraph. (If \(s>n\), the injective sum is empty.)

For such a multigraph \(G\), use partition-lattice Möbius inversion:

\[
\operatorname{inj}(G,A)
=\sum_{\pi}\mu(\pi)\operatorname{hom}(G/\pi,A).
\tag{6.3}
\]

The number and absolute sizes of all coefficients in (6.3) are bounded by
a universal constant because \(G\) has at most eight vertices. There are at
most \(8^8\) initial endpoint partitions and, for each of them, at most
\(8^8\) quotient partitions. Every partition-lattice Möbius coefficient has
absolute value at most \(8!\). Thus the total coefficient mass is at most

\[
8^8\cdot8^8\cdot8!<2^{64}.
\]

A quotient containing a loop contributes zero because \(a_{ii}=0\).
An unrestricted homomorphism sum of a graph with a degree-one vertex also
vanishes: sum the leaf label and use the row-zero identity (4.1).
Therefore every surviving quotient is loopless, has four edge occurrences,
has minimum multidegree at least two, and has at most four vertices.

Up to isolated-free isomorphism, the only possibilities are

1. four parallel edges;
2. two disjoint doubled edges;
3. two doubled edges sharing one vertex;
4. a triangle with one doubled edge;
5. a four-cycle.

Let

\[
F_A=\sum_{i,j}a_{ij}^2=2L.
\]

For the five types, respectively, absolute homomorphism sums are bounded by

\[
\sum_{i,j}|a_{ij}|^4\le F_A^2,
\]

\[
\left(\sum_{i,j}a_{ij}^2\right)^2=F_A^2,
\]

\[
\sum_i\left(\sum_j a_{ij}^2\right)^2\le F_A^2,
\]

\[
\sum_{i,j,k}|a_{ij}|^2|a_{ik}a_{jk}|
\le F_A^2,
\]

and, on writing \(B_A=(|a_{ij}|)\) for the entrywise absolute-value
matrix,

\[
\operatorname{tr}(B_A^4)
\le\bigl(\operatorname{tr}B_A^2\bigr)^2
=F_A^2.
\]

The fourth inequality is Cauchy--Schwarz applied to
\(|a_{ij}a_{ik}|\) and \(|a_{ij}a_{jk}|\).

Since \(F_A^2=4L^2\), the coefficient count and the five bounds give

\[
\mathbb Eh^4<2^{66}L^2.
\]

In particular, the deliberately looser bound

\[
\mathbb Eh^4\le2^{128}L^2.
\tag{6.4}
\]

By (6.2),

\[
\sqrt L\le18\|h\|_2.
\]

Taking fourth roots in (6.4) proves (6.1) with the displayed \(K\).
\(\square\)

No external hypercontractivity or classification theorem is used here.

## 7. Robust Boolean-\(E_2\) stability

Define

\[
\theta_*=\frac{3-\sqrt6}{6}=0.091751\ldots .
\tag{7.1}
\]

### Theorem 7.1

Fix a compact interval

\[
I\subset(0,\theta_*)
\]

and a constant \(C<\infty\). There are

\[
\varepsilon_{I,C}>0,\qquad m_0(I,C)
\]

such that, whenever

\[
n=2m+1,\qquad m\ge m_0(I,C),\qquad |r-m|\le C\sqrt m,
\]

every family

\[
\mathcal B\subseteq\binom{[n]}r
\]

of density \(\theta\in I\) satisfies

\[
\boxed{
\left\|
P_{E_1\oplus E_{\ge3}}
(\mathbf1_{\mathcal B}-\theta\mathbf1)
\right\|_2^2
\ge
\varepsilon_{I,C}\binom nr.}
\tag{7.2}
\]

The norm in (7.2) is the unnormalized counting norm. Equivalently, the
corresponding squared norm in normalized slice measure is at least
\(\varepsilon_{I,C}\).

In particular, this proves the previously open robust statement on every
compact subinterval of \((0,1/16)\).

### Proof

Use normalized expectation on the rank layer and put

\[
f=\mathbf1_{\mathcal B}-\theta,
\qquad
h=P_{E_2}f,
\qquad
e=f-h.
\]

Then

\[
\delta:=\mathbb Ee^2
=
\binom nr^{-1}
\left\|P_{E_1\oplus E_{\ge3}}f\right\|_2^2,
\]

\[
\sigma^2:=\mathbb Ef^2=\theta(1-\theta),
\]

and

\[
\mathbb Ef^3=\theta(1-\theta)(1-2\theta).
\tag{7.3}
\]

By Proposition 6.1 and \(\|h\|_2\le\|f\|_2\le1/2\),

\[
\begin{aligned}
|\mathbb Ef^3-\mathbb Eh^3|
&=
|\mathbb E[e(f^2+fh+h^2)]|\\
&\le
\sqrt\delta
\left(1+\frac{K^2}{4}\right).
\end{aligned}
\tag{7.4}
\]

Here \(|f|\le1\) gives \(\|f^2\|_2\le\|f\|_2\le1/2\), while
\(\|fh\|_2\le\|f\|_\infty\|h\|_2\le1/2\), and Proposition 6.1 gives
\(\|h^2\|_2=\|h\|_4^2\le K^2\|h\|_2^2\le K^2/4\).

Put

\[
G_I=\inf_{\theta\in I}
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}},
\qquad
\Gamma=\frac{2\sqrt2+G_I}{2}.
\]

Then

\[
2\sqrt2<\Gamma<
\inf_{\theta\in I}
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}}.
\tag{7.5}
\]

These inequalities hold because

\[
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}}>2\sqrt2
\quad\Longleftrightarrow\quad
\theta<\frac{3-\sqrt6}{6}.
\]

By (5.8), for all sufficiently large \(m\),

\[
|\mathbb Eh^3|
\le\Gamma(\mathbb Eh^2)^{3/2}
\le\Gamma\sigma^3.
\tag{7.6}
\]

Combining (7.3)--(7.6) yields

\[
\left(1+\frac{K^2}{4}\right)\sqrt\delta
\ge
\theta(1-\theta)
\left[
1-2\theta-\Gamma\sqrt{\theta(1-\theta)}
\right].
\tag{7.7}
\]

Put

\[
M_{I,\Gamma}
=\min_{\theta\in I}
\theta(1-\theta)
\left[1-2\theta-\Gamma\sqrt{\theta(1-\theta)}\right]>0.
\]

Thus one may take

\[
\varepsilon_{I,C}
=\left(
\frac{M_{I,\Gamma}}{1+K^2/4}
\right)^2,
\]

after choosing \(m_0(I,C)\) large enough that (7.6) holds uniformly.
This proves (7.2). \(\square\)

By complementation, the corresponding robust conclusion also holds on
compact subintervals of \((1-\theta_*,1)\).

## 8. Rounding an integer load to a Boolean bonus family

The following elementary lemma transfers Theorem 7.1 to exact-factor loads.

### Lemma 8.1

Suppose \(c\in\mathbb Z_{\ge0}\), \(0\le\theta<1\),
\(\lambda=c+\theta\), and
\(\mu\in\mathbb Z_{\ge0}^{N}\) has total mass \(N\lambda\). Put

\[
M=\theta N=N\lambda-cN\in\{0,1,\ldots,N-1\}.
\]

Also put

\[
Q=\sum_{i=1}^{N}(\mu_i-c)(\mu_i-c-1).
\]

There is a vector

\[
b'=c\mathbf1+\mathbf1_{\mathcal B},
\qquad |\mathcal B|=M=\theta N,
\]

such that

\[
\boxed{
\|\mu-b'\|_2^2
\le2Q+2\sqrt{NQ}.}
\tag{8.1}
\]

### Proof

Clamp each coordinate of \(\mu\) to the nearer member of
\(\{c,c+1\}\), obtaining \(b\). Pointwise,

\[
|\mu_i-b_i|^2
\le(\mu_i-c)(\mu_i-c-1),
\]

so

\[
\|\mu-b\|_2^2\le Q.
\]

The mass discrepancy satisfies

\[
\Delta=\left|\sum_i b_i-N\lambda\right|
\le\sqrt N\,\|b-\mu\|_2
\le\sqrt{NQ}.
\]

Flip exactly \(\Delta\) entries of \(b\) in the required direction. There
are enough entries because the target number of high coordinates is
\(\theta N\). The resulting vector \(b'\) has the required mass, and

\[
\|b-b'\|_2^2=\Delta.
\]

The squared triangle inequality gives (8.1). \(\square\)

For an exact-factor load, both

\[
f=\mu-\lambda\mathbf1
\]

and

\[
g=\mathbf1_{\mathcal B}-\theta\mathbf1
\]

have mean zero. Exact point margins give

\[
P_{E_1}f=0.
\tag{8.2}
\]

If

\[
H^{\mathrm{hi}}=\sum_{j\ge3}\|f^{(j)}\|_2^2,
\]

then (8.1), orthogonal projection, and (8.2) give

\[
\boxed{
\left\|P_{E_1\oplus E_{\ge3}}g\right\|_2^2
\le
2H^{\mathrm{hi}}+4Q+4\sqrt{NQ}.}
\tag{8.3}
\]

Indeed, \(g=f-(\mu-b')\), so project and use
\(\|x+y\|^2\le2\|x\|^2+2\|y\|^2\).

## 9. Refutation of the corrected gate

We now prove the main theorem.

Fix \(A>0\), and set

\[
\eta=\sqrt{\log(17/16)},
\qquad
v=\frac12\min\{A,\eta\},
\qquad
u=\frac v2.
\]

Then \(0<u<v<A\) and

\[
e^{v^2}-1<\frac1{16}.
\tag{9.1}
\]

Indeed, \(v\le\eta/2<\eta\) and \(e^{\eta^2}=17/16\).

Moreover, the exact binomial ratio is

\[
\lambda_q
=\prod_{s=0}^{q-1}\frac{m+2+s}{m-s}.
\]

For \(q\le A\sqrt m\), Taylor's formula, uniformly in \(s<q\), gives

\[
\begin{aligned}
\log\lambda_q
&=\sum_{s=0}^{q-1}
\left[
\log\left(1+\frac{s+2}{m}\right)
-\log\left(1-\frac{s}{m}\right)
\right]\\
&=\sum_{s=0}^{q-1}\frac{2s+2}{m}
+O\left(\frac{q^3+q}{m^2}\right)\\
&=\frac{q(q+1)}m+O_A(m^{-1/2}).
\end{aligned}
\]

Thus we have the uniform Gaussian-window asymptotic:

\[
\lambda_q
=\frac W{N_q}
=\exp\left(\frac{q(q+1)}m+O_A(m^{-1/2})\right)
\tag{9.2}
\]

The explicit compact interval

\[
I_A=
\left[
\frac{e^{u^2}-1}{2},
\frac{e^{v^2}-1+1/16}{2}
\right]
\subset(0,1/16)
\]

has the property that, for all sufficiently large \(m\) and all integers

\[
u\sqrt m\le q\le v\sqrt m,
\tag{9.3}
\]

\[
c_q=1,\qquad \theta_q\in I_A,\qquad N_q\ge W/2.
\tag{9.4}
\]

For all sufficiently large \(m\), there are at least

\[
c'_A\sqrt m,
\qquad
c'_A=\frac{v-u}{2},
\]

such depths.

Let \(F\) be a global minimizer of the full \(H\)-window objective. At one
selected depth, put

\[
H_q^{\mathrm{hi}}=\sum_{j\ge3}\|f_q^{(j)}\|_2^2.
\]

Apply Lemma 8.1 and Theorem 7.1. For

\[
\varepsilon_A:=\varepsilon_{I_A,v}>0,
\]

equation (8.3) gives

\[
\varepsilon_A N_q
\le
2H_q^{\mathrm{hi}}+4Q_q+4\sqrt{N_qQ_q}.
\tag{9.5}
\]

Let

\[
t_q=\frac{H_q^{\mathrm{hi}}+Q_q}{N_q}.
\]

If \(t_q\le1\), the right side of (9.5) is at most

\[
N_q(4t_q+4\sqrt{t_q})
\le8N_q\sqrt{t_q}.
\]

If \(t_q>1\), the following conclusion is automatic. Thus, with

\[
\delta_A
=\min\left\{1,\left(\frac{\varepsilon_A}{8}\right)^2\right\}>0,
\]

every selected depth obeys

\[
\boxed{
H_q^{\mathrm{hi}}+Q_q\ge\delta_A N_q.}
\tag{9.6}
\]

At a global minimizer, drop the nonnegative switching-cube slack from
(2.3). On the selected depths \(c_q=1\), so

\[
R_H-4(n-1)B_H
\ge
\sum_{\text{selected }q}
\left(
4(n-1)Q_q
+2\sum_{j\ge3}
(j-2)(n-j-1)\|f_q^{(j)}\|_2^2
\right).
\tag{9.7}
\]

For \(3\le j\le r_q\le m\),

\[
(j-2)(n-j-1)\ge n-4.
\tag{9.8}
\]

To check the endpoint, the left side equals \(n-4\) at \(j=3\), and its
increment when \(j\) is increased by one is \(n-2j>0\) throughout
\(j\le m=(n-1)/2\).

Also \(4(n-1)\ge2(n-4)\). Hence (9.6)--(9.8) imply that every selected
depth contributes at least

\[
2(n-4)\delta_A N_q
\ge(n-4)\delta_A W.
\]

For \(n\ge6\), \(n-4\ge n/3\). Summing over the selected depths therefore
proves

\[
R_H(F)-4(n-1)B_H
\ge c_A nW\sqrt m,
\qquad
c_A=\frac{\delta_A(v-u)}6>0.
\]

Take \(m_0(A)\) to be the maximum of the thresholds needed for
Theorem 7.1, (9.2)--(9.4), the depth count, \(n\ge6\), and
\(H\le m-2\). This is (1.1). \(\square\)

## 10. Sharpness and scope audit

### 10.1 The skewness constant is genuine

Assume \(m\ge2\).
Split \([n]\) into blocks \(P,Q\) of sizes \(m,m+1\). Define a symmetric
zero-diagonal row-zero matrix by assigning weights

\[
a_{ij}=
\begin{cases}
\dfrac{m+1}{m-1},&i,j\in P,\\
1,&i,j\in Q,\\
-1,&i\in P,\ j\in Q.
\end{cases}
\tag{10.1}
\]

Its eigenvalues are

\[
n,\qquad
-\frac{m+1}{m-1}\ \text{with multiplicity }m-1,
\qquad
-1\ \text{with multiplicity }m,
\qquad
0.
\]

Therefore

\[
\frac{\operatorname{tr}(A^3)}
{(\operatorname{tr}(A^2))^{3/2}}
\longrightarrow1.
\]

The associated central-slice \(E_2\) function has standardized third moment
tending to \(2\sqrt2\). Thus the constant in (5.8) is sharp for abstract
zero-margin \(E_2\) profiles. This example is a quadratic block-count
profile, not a Boolean indicator.

### 10.2 What has and has not been proved

The proof establishes:

1. **PROVED:** the exact second- and third-moment formulas (5.1)--(5.5);
2. **PROVED:** a dimension-free central-slice \(L^4/L^2\) bound for \(E_2\);
3. **PROVED:** robust Boolean-\(E_2\) separation on every compact subset of
   \[
   \left(0,\frac{3-\sqrt6}{6}\right),
   \]
   in particular on every compact subset of \((0,1/16)\);
4. **PROVED:** the exact load-rounding and projection transfer (8.1)--(8.3);
5. **REFUTED:** the corrected global component-noise gate at global
   Gaussian-window minimizers, with the quantitative lower gap (1.1).

The proof does not establish:

1. failure of low floor energy or weighted overload;
2. failure of MWB or the contiguous-OR conjecture;
3. any obstruction to a direct literal OR word;
4. any implication concerning labelled common-owner synchronization;
5. any exact-factor realization of the abstract models in Section 3.

The reason the gate fails is now exact. Near its baseline it demands both
small floor excess and negligible Johnson degrees at least three. Sparse
Boolean bonus families with nearly zero \(E_1\) mass cannot satisfy both.
The component-noise criterion therefore packages an impossible spectral
near-equality on a positive portion of every Gaussian window.

### 10.3 Dependency and internal-audit ledger

The proof uses three previously proved exact-factor inputs: existence of
the middle wreath factors, legality of fair complete-component switching,
and the unordered-transposition Johnson identity (2.2). The only place
global minimality is used is (2.1), which makes \(R_H-D_H\ge0\). No
labelled common-owner synchronization statement is used.

All new claims needed for the refutation are proved here. In particular:

1. the cubic Johnson-slice formula has two independent derivations, the
   graph-sum derivation and the Bernoulli-polynomial audit following it;
2. the fourth-moment proof explicitly accounts for every equality
   partition, every Möbius coefficient, and all five surviving four-edge
   quotient types;
3. the Boolean stability theorem includes \(E_1\), so the rounded bonus
   family need not inherit exact point margins;
4. exact point margins are used only for the original load, through
   \(P_{E_1}f=0\);
5. the selected density interval is compactly contained in \((0,1/16)\),
   so neither endpoint is approached;
6. the abstract Section 3 systems are stress tests only and are never
   substituted for an exact factor.

There is no unproved lemma in the new Boolean-\(E_2\), rounding, or
Gaussian-window part of the argument.
