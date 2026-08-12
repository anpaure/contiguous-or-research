# Mathematical attack D: sparse Boolean-\(E_2\) stability

Date: 2026-07-24

## 1. Verdict

The Sparse Boolean-\(E_2\) stability problem is true. In fact the density
range is larger than the requested interval \((0,1/16)\).

Put

\[
\theta_*=\frac{3-\sqrt6}{6}
=\frac12-\frac1{\sqrt6}
=0.091751\ldots .
\]

For every fixed central-window constant \(A_0<\infty\) and every compact
interval \(I\subset(0,\theta_*)\), there is
\(\varepsilon_I>0\) such that, uniformly for

\[
n=2m+1,\qquad |r-n/2|\le A_0\sqrt n,
\]

every Boolean family
\(\mathcal B\subseteq\binom{[n]}r\) of density
\(\theta\in I\) satisfies

\[
\boxed{
\left\|
P_{E_1\oplus E_{\ge3}}
\bigl(\mathbf1_{\mathcal B}-\theta\mathbf1\bigr)
\right\|_2^2
\ge
\varepsilon_I\binom nr .
}
\tag{1.1}
\]

Thus the requested theorem for compact
\(I\subset(0,1/16)\) holds.

The proof is not a direct robustification of the facet-star cascade.
Instead it uses Booleanity through the third moment. The uniform asymptotic
standardized skew of a Johnson \(E_2\) function is at most \(2\sqrt2\).
The standardized skew of a centered Boolean indicator of density
\(\theta<\theta_*\) is strictly larger.

When inserted into the corrected component-noise ledger, (1.1) proves
that, at every same-window global minimizer,

\[
\boxed{
R_H-4(n-1)B_H=\Omega_A(nW\sqrt m)
}
\tag{1.2}
\]

for every fixed nonzero window \(H=\lceil A\sqrt m\rceil\).
Consequently the corrected proposed gate

\[
R_H\le4(n-1)B_H+o(nW)
\]

is impossible on every such window.

This refutes that sufficient component-noise gate. It does not refute MWB,
SYNC, or the contiguous-OR conjecture.

## 2. Normalization and Johnson notation

Work in the nondegenerate slice range \(2\le r\le n-2\), which contains
every central rank used below, and write

\[
\Omega_{n,r}=\binom{[n]}r,\qquad N=\binom nr,
\]

and use normalized expectation and norm

\[
\mathbb E\phi=\frac1N\sum_{S\in\Omega_{n,r}}\phi(S),
\qquad
\|\phi\|_{2,\mathrm{prob}}^2=\mathbb E\phi^2.
\]

The unnormalized squared norm is \(N\) times this quantity.

Let

\[
L^2(\Omega_{n,r})=E_0\oplus E_1\oplus\cdots\oplus
E_{\min(r,n-r)}
\]

be the Johnson harmonic decomposition. For a Boolean family
\(\mathcal B\), put

\[
g=\mathbf1_{\mathcal B}-\theta,\qquad
\theta=\frac{|\mathcal B|}{N}.
\]

Then \(g\perp E_0\), and

\[
\mathbb Eg^2=\theta(1-\theta).
\]

The desired normalized quantity is

\[
\delta
=
\left\|P_{E_1\oplus E_{\ge3}}g\right\|_{2,\mathrm{prob}}^2.
\tag{2.1}
\]

## 3. Harmonic-matrix representation of \(E_2\)

### Lemma 3.1

Every \(h\in E_2\) has a unique representation

\[
\boxed{
h(S)=\sum_{1\le i<j\le n}a_{ij}\mathbf1_{\{i,j\}\subseteq S},
}
\tag{3.1}
\]

where \(A=(a_{ij})\) is symmetric, has zero diagonal, and satisfies

\[
\boxed{A\mathbf1=0.}
\tag{3.2}
\]

### Proof

Let \(\mathcal A\) be the space of symmetric zero-diagonal matrices
satisfying (3.2). The \(n\) row-sum equations have full rank on the edge
space of the complete graph, so

\[
\dim\mathcal A=\binom n2-n=\dim E_2.
\]

If \(h\) is given by (3.1), then

\[
\sum_{i<j}a_{ij}=0.
\]

Consequently \(\mathbb Eh=0\). For every coordinate \(k\),
\(\mathbb[h\,\mathbf1_{\{k\in S\}}]=0\): the edges containing \(k\)
sum to zero by (3.2), and the remaining edges have total sum zero as well.
Thus the image of \(\mathcal A\) is orthogonal to \(E_0\oplus E_1\).

The exact positive norm formula in Lemma 4.1 below proves injectivity.
Dimension equality then proves that the image is exactly \(E_2\).
\(\square\)

For \(t\ge0\), write

\[
\pi_t=\frac{(r)_t}{(n)_t}.
\]

For a harmonic matrix \(A\), put

\[
S_2=\sum_{i<j}a_{ij}^2,\qquad
C_3=\sum_{i<j}a_{ij}^3,\qquad
T_3=\operatorname{tr}(A^3).
\tag{3.3}
\]

## 4. Exact second and third moments on the slice

### Lemma 4.1

Assume \(n\ge6\). For \(h\in E_2\) represented by \(A\),

\[
\boxed{
\mathbb Eh^2=\alpha_{n,r}S_2,
}
\tag{4.1}
\]

where

\[
\alpha_{n,r}
=\pi_2-2\pi_3+\pi_4
=\frac{(r)_2(n-r)_2}{(n)_4}.
\tag{4.2}
\]

Moreover,

\[
\boxed{
\mathbb Eh^3=a_{n,r}C_3+b_{n,r}T_3,
}
\tag{4.3}
\]

where

\[
a_{n,r}
=\pi_2-6\pi_3+13\pi_4-12\pi_5+4\pi_6,
\tag{4.4}
\]

and

\[
b_{n,r}
=\pi_3-3\pi_4+3\pi_5-\pi_6
=\frac{(r)_3(n-r)_3}{(n)_6}.
\tag{4.5}
\]

### Proof

Let \(X_1,\ldots,X_n\) be independent Bernoulli-\(x\) variables. Because
\(A\mathbf1=0\),

\[
\sum_{i<j}a_{ij}X_iX_j
=
\sum_{i<j}a_{ij}(X_i-x)(X_j-x).
\tag{4.6}
\]

In the second moment of the right side, every term vanishes unless the two
edges coincide. Hence

\[
\mathbb E_x h^2
=
S_2x^2(1-x)^2
=S_2(x^2-2x^3+x^4).
\tag{4.7}
\]

For the third moment, a product of three centered edge monomials survives
only in two cases.

First, all three edges coincide. Since

\[
\mathbb E(X_i-x)^3=x(1-x)(1-2x),
\]

these terms contribute

\[
C_3x^2(1-x)^2(1-2x)^2.
\]

Second, the three edges form a triangle. The six orderings of every
triangle are exactly the terms in \(\operatorname{tr}(A^3)\), and their
contribution is

\[
T_3x^3(1-x)^3.
\]

Therefore

\[
\mathbb E_xh^3
=
C_3x^2(1-x)^2(1-2x)^2
+T_3x^3(1-x)^3.
\tag{4.8}
\]

For any polynomial in the Boolean coordinates, its independent
Bernoulli-\(x\) expectation is obtained by assigning \(x^t\) to a monomial
using \(t\) distinct coordinates. Its uniform-slice expectation is obtained
from the same expansion by replacing \(x^t\) by
\(\pi_t=(r)_t/(n)_t\). Applying this coefficient substitution to
(4.7) and (4.8) gives (4.1)--(4.5).

The factorization in (4.2) is immediate algebra. \(\square\)

There is also the useful exact identity

\[
a_{n,r}
=
\alpha_{n,r}
\frac{(n-2r)^2-(n-4)}{(n-4)(n-5)}.
\tag{4.9}
\]

It follows either from (4.4), or by conditioning the without-replacement
expectation

\[
\mathbb E\!\left[
X_1X_2(1-X_3)(1-X_4)(1-2X_5)(1-2X_6)
\right].
\]

## 5. Uniform asymptotic \(E_2\) skew bound

### Theorem 5.1

Fix \(A_0<\infty\). Uniformly for

\[
|r-n/2|\le A_0\sqrt n
\]

and every \(h\in E_2\),

\[
\boxed{
|\mathbb Eh^3|
\le
\left(2\sqrt2+O_{A_0}(n^{-1})\right)
(\mathbb Eh^2)^{3/2}.
}
\tag{5.1}
\]

### Proof

The elementary coefficient bounds are

\[
|C_3|\le S_2^{3/2},
\tag{5.2}
\]

and, since \(A\) is real symmetric,

\[
|T_3|
\le
\bigl(\operatorname{tr}(A^2)\bigr)^{3/2}
=(2S_2)^{3/2}.
\tag{5.3}
\]

Put \(p=r/n\). For each fixed \(t\),

\[
\pi_t=p^t+O_t(n^{-1}).
\]

In the stated window \(p=1/2+O_{A_0}(n^{-1/2})\). Hence

\[
\alpha_{n,r}
=p^2(1-p)^2+O(n^{-1})
=\frac1{16}+O_{A_0}(n^{-1}),
\tag{5.4}
\]

\[
b_{n,r}
=p^3(1-p)^3+O(n^{-1})
=\frac1{64}+O_{A_0}(n^{-1}),
\tag{5.5}
\]

while

\[
\begin{aligned}
a_{n,r}
&=
p^2-6p^3+13p^4-12p^5+4p^6+O(n^{-1})\\
&=
p^2(1-p)^2(1-2p)^2+O(n^{-1})
=O_{A_0}(n^{-1}).
\end{aligned}
\tag{5.6}
\]

Combining (4.1), (4.3), and (5.2)--(5.6),

\[
\frac{|\mathbb Eh^3|}{(\mathbb Eh^2)^{3/2}}
\le
\frac{|a_{n,r}|+2\sqrt2\,|b_{n,r}|}
{\alpha_{n,r}^{3/2}}
=2\sqrt2+O_{A_0}(n^{-1}).
\]

\(\square\)

The constant \(2\sqrt2\) is the natural second-chaos skew constant. The
proof treats arbitrary coefficient concentration; no small-influence,
junta, or invariance hypothesis is used.

## 6. Uniform fourth moment of \(E_2\)

The cubic comparison with a Boolean function requires a separate
fourth-moment estimate.

### Lemma 6.1

There is an absolute constant \(K<\infty\) such that, whenever \(n\ge8\)
and

\[
r,n-r\ge n/3,
\]

every \(h\in E_2\) satisfies

\[
\boxed{
\mathbb Eh^4\le K(\mathbb Eh^2)^2.
}
\tag{6.1}
\]

### Proof

Using symmetry and the zero diagonal, first write

\[
h=\frac12\sum_{i,j}a_{ij}\mathbf1_{\{i,j\}\subseteq S}.
\]

Expand \(h^4\) into ordered quadruples of these ordered edge slots. Group
the terms by the equality pattern of their at most eight endpoints. Up to
the fixed factor \(2^{-4}\), every pattern is an injective weighted graph
sum

\[
\operatorname{inj}(G,A)
=
\sum_{\phi:V(G)\hookrightarrow[n]}
\prod_{uv\in E(G)}a_{\phi(u)\phi(v)}
\]

for a fixed four-edge multigraph \(G\), multiplied by the inclusion
probability \(\pi_{|V(G)|}\le1\).

Möbius inversion on the partition lattice of \(V(G)\) expresses every
injective sum as a fixed finite linear combination of unrestricted
homomorphism sums of quotient multigraphs.

If a quotient has a loop, its contribution vanishes because \(a_{ii}=0\).
If it has a degree-one vertex, sum first over the image of that vertex;
the contribution vanishes because \(A\mathbf1=0\).

Every surviving quotient therefore has minimum degree at least two. Since
it has four edges, it has at most four nonisolated vertices. Its nonzero
components are among:

- four parallel edges;
- two doubled edges sharing one vertex;
- a triangle with one doubled edge;
- a four-cycle;
- two disjoint doubled edges.

Put

\[
D=\sum_{i,j}a_{ij}^2=2S_2.
\]

The corresponding unrestricted sums are bounded respectively by

\[
\sum_{i,j}|a_{ij}|^4,\qquad
\sum_i\left(\sum_j a_{ij}^2\right)^2,
\]

\[
\left|\sum_{i,j,k}a_{ij}^2a_{jk}a_{ki}\right|,
\qquad
|\operatorname{tr}(A^4)|,
\qquad
D^2.
\]

Each is at most \(D^2\). For the doubled triangle, for example,

\[
\left|\sum_{i,j,k}a_{ij}^2a_{jk}a_{ki}\right|
=
|\langle A\circ A,A^2\rangle|
\le
\|A\circ A\|_F\|A^2\|_F
\le D^2.
\]

For the four-cycle,

\[
\operatorname{tr}(A^4)\le(\operatorname{tr}(A^2))^2=D^2.
\]

There are only finitely many endpoint-equality patterns and finitely many
partition-lattice coefficients. Consequently

\[
\mathbb Eh^4\le K_0S_2^2
\]

for an absolute \(K_0\). In the stated central range,
\(\alpha_{n,r}\) in (4.2) is bounded below by an absolute positive
constant. Equation (4.1) therefore gives (6.1). \(\square\)

No external slice hypercontractivity theorem is required.

## 7. Booleanity forces a uniform gap

### Theorem 7.1

Fix \(A_0<\infty\) and a compact interval

\[
I\subset(0,\theta_*).
\]

There are \(\varepsilon_I>0\) and
\(n_0=n_0(A_0,I)\) such that (1.1) holds whenever
\(n\ge n_0\) and \(|r-n/2|\le A_0\sqrt n\).

### Proof

Use normalized expectation. Put

\[
g=\mathbf1_{\mathcal B}-\theta,\qquad
h=P_{E_2}g,\qquad
u=g-h.
\]

Then

\[
u=P_{E_1\oplus E_{\ge3}}g,
\qquad
\delta=\mathbb Eu^2,
\tag{7.1}
\]

and orthogonality gives

\[
\mathbb Eh^2
=
\theta(1-\theta)-\delta.
\tag{7.2}
\]

Write

\[
V=\theta(1-\theta).
\]

Since \(g\) takes the two values \(1-\theta\) and \(-\theta\),

\[
\boxed{\mathbb Eg^3=V(1-2\theta).}
\tag{7.3}
\]

Also,

\[
g^3-h^3=u(g^2+gh+h^2).
\]

By Cauchy--Schwarz, \(|g|\le1\), and Lemma 6.1,

\[
\begin{aligned}
|\mathbb Eg^3-\mathbb Eh^3|
&\le
\sqrt\delta\,
\left(
\|g^2\|_2+\|gh\|_2+\|h^2\|_2
\right)\\
&\le
\sqrt\delta\,
\left(
\sqrt V+\sqrt{V-\delta}
+\sqrt K\,(V-\delta)
\right)\\
&\le C_0\sqrt\delta,
\end{aligned}
\tag{7.4}
\]

where one may take

\[
C_0=1+\frac{\sqrt K}{4}.
\]

Theorem 5.1 and (7.2)--(7.4) imply

\[
V(1-2\theta)
\le
\left(2\sqrt2+o(1)\right)V^{3/2}
+C_0\sqrt\delta.
\tag{7.5}
\]

Define

\[
\Psi(\theta)
=
V\left[
(1-2\theta)-2\sqrt{2V}
\right].
\tag{7.6}
\]

The bracket is positive precisely when

\[
(1-2\theta)^2>8\theta(1-\theta).
\]

The lower root of the corresponding quadratic

\[
12\theta^2-12\theta+1=0
\]

is

\[
\theta_*=\frac{3-\sqrt6}{6}.
\]

Since \(I\subset(0,\theta_*)\) is compact,

\[
d_I:=\min_{\theta\in I}\Psi(\theta)>0.
\]

For all sufficiently large \(n\), the finite-\(n\) error term in (7.5)
is at most \(d_I/2\). Hence

\[
C_0\sqrt\delta\ge\frac{d_I}{2},
\]

and therefore

\[
\boxed{
\delta\ge\frac{d_I^2}{4C_0^2}
=:\varepsilon_I>0.
}
\tag{7.7}
\]

Multiplying by \(N\) gives (1.1). \(\square\)

By replacing \(\mathcal B\) with its complement, the symmetric upper-density
range \(1-\theta_*<\theta<1\) follows as well.

## 8. Why the facet-star cascade alone loses stability

The exact exclusion in the component-noise note proceeds by facet stars,
integer cross-degrees, and a second up/down cascade. That proof is effective
at zero error but does not directly yield a uniform \(L^2\) gap.

Let \(D\) and \(U\) be the normalized down and up operators between ranks
\(r\) and \(r-1\). On rank \(r\),

\[
UD
=
I-\frac{L_J}{r(n-r+1)}.
\tag{8.1}
\]

Its \(E_2\) eigenvalue is

\[
\rho_2
=
1-\frac{2(n-1)}{r(n-r+1)}.
\tag{8.2}
\]

If \(g=p+h\), with \(p\in E_2\) and
\(\|h\|_2^2=\delta\), then

\[
\|(UD-\rho_2)g\|_2=O(\sqrt\delta).
\tag{8.3}
\]

However, converting a normalized error \(t\) in (8.3) into the unnormalized
sum of facet-star deficits multiplies it by

\[
r(n-r+1)=\Theta(m^2).
\]

One nonfull facet contributes a deficit of order
\(n-r+1=\Theta(m)\). Thus the inferred number of nonfull facets has
uncertainty of order

\[
O(r\,t).
\]

Thus a pointwise normalized error \(t\) produces \(O(rt)\) uncertainty in
the inferred number of nonfull facets. An \(L^2\) error \(\delta\) gives
only an RMS normalized error of order \(\sqrt\delta\), and hence this
calculation permits RMS uncertainty \(O(r\sqrt\delta)\), which need not be
\(o(1)\). The exact step “there are four nonfull facets” cannot be
stabilized at a fixed positive \(L^2\) scale by this local calculation
alone.

The cubic-moment proof avoids this factor \(r\): it averages the harmonic
constraint globally before applying Booleanity.

## 9. Rounding an integer load to a Boolean bonus family

The gate application requires passing from an integer load vector to a
balanced adjacent-integer Boolean vector.

All vector norms in Sections 9 and 10 are unnormalized counting norms.

### Lemma 9.1

Let \(\mu\in\mathbb Z_{\ge0}^N\) have total

\[
\sum_S\mu(S)=W=N(c+\theta),
\qquad c\in\mathbb Z_{\ge0},\quad0\le\theta<1.
\]

Put

\[
f=\mu-(c+\theta)\mathbf1
\]

and

\[
\mathcal E
=
\|f\|_2^2-N\theta(1-\theta)
=
\sum_S(\mu(S)-c)(\mu(S)-c-1).
\tag{9.1}
\]

Here \(\mathcal E\) is the full quadratic floor excess. The corresponding
pair-collision, or half-energy, excess is \(\mathcal E/2\). This convention
is kept throughout Section 10.

Then there is a family \(\mathcal B\subseteq[N]\) of size
\(\theta N\) such that

\[
\boxed{
\left\|
\mu-\bigl(c\mathbf1+\mathbf1_{\mathcal B}\bigr)
\right\|_2^2
\le
2\mathcal E+2\sqrt{N\mathcal E}.
}
\tag{9.2}
\]

### Proof

Define \(b(S)\in\{c,c+1\}\) pointwise by taking \(c\) when
\(\mu(S)\le c\) and \(c+1\) when \(\mu(S)\ge c+1\). Pointwise,

\[
(\mu(S)-b(S))^2
\le
(\mu(S)-c)(\mu(S)-c-1),
\]

so

\[
\|\mu-b\|_2^2\le\mathcal E.
\]

Let

\[
\Delta=\left|\sum_Sb(S)-W\right|.
\]

By Cauchy--Schwarz,

\[
\Delta
\le\sqrt N\,\|b-\mu\|_2
\le\sqrt{N\mathcal E}.
\]

Flip exactly \(\Delta\) entries of \(b\) between \(c\) and \(c+1\) in
the required direction, obtaining a vector

\[
b'=c\mathbf1+\mathbf1_{\mathcal B}
\]

of total \(W\). Since \(\|b-b'\|_2^2=\Delta\),

\[
\|\mu-b'\|_2^2
\le2\|\mu-b\|_2^2+2\|b-b'\|_2^2
\le2\mathcal E+2\sqrt{N\mathcal E}.
\]

\(\square\)

## 10. Consequence for the corrected component-noise gate

Now return to exact wreath histograms. Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
N_q=\binom n{m-q},
\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q.
\]

Let

\[
f_q=\mu_q-\lambda_q\mathbf1.
\]

Exact wreath point margins imply

\[
f_q^{(0)}=f_q^{(1)}=0.
\tag{10.1}
\]

Define the rank floor excess

\[
\mathcal E_q
=
\|f_q\|_2^2-N_q\theta_q(1-\theta_q),
\tag{10.2}
\]

and the high-harmonic mass

\[
\mathcal H_q
=
\sum_{j\ge3}\|f_q^{(j)}\|_2^2.
\tag{10.3}
\]

For this section write

\[
B_H=\sum_{q=1}^H\frac{N_q\theta_q(1-\theta_q)}{c_q},
\qquad
E_H=\sum_{q=1}^H\frac{\mathcal E_q}{c_q}.
\tag{10.3a}
\]

If \(d_{q,S}=\mu_q(S)-c_q\), put

\[
O_q=\max\left\{
\sum_S(-d_{q,S})_+,\,
\sum_S(d_{q,S}-1)_+
\right\},
\qquad
P_H=\sum_{q=1}^H\frac{O_q}{c_q}.
\tag{10.3b}
\]

Finally, for an unordered transposition \(\tau\), let \(u_{q,C}\) and
\(w_{q,C}\) be the two complete-side depth-\(q\) histograms in an overlap
component \(C\) of the factor and its \(\tau\)-relabeling, and set

\[
R_H=
\sum_\tau\sum_C\sum_{q=1}^H
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\tag{10.3c}
\]

The “same-window global minimizer” below means a factor minimizing
\(B_H+E_H=\sum_{q=1}^H\|f_q\|_2^2/c_q\).

Fix \(A>0\) and put \(H=\lceil A\sqrt m\rceil\). Choose constants

\[
0<u<v<\min\{A,\sqrt{\log(17/16)}\}.
\]

For all depths satisfying

\[
u\sqrt m\le q\le v\sqrt m,
\tag{10.4}
\]

one has, uniformly,

\[
\lambda_q=e^{q^2/m+o(1)},\qquad c_q=1,
\]

and the fractional parts \(\theta_q\) lie in a fixed compact interval

\[
I\subset(0,1/16)
\]

after shrinking \([u,v]\) slightly if necessary. Also

\[
N_q=\Theta_{u,v}(W).
\tag{10.5}
\]

Apply Lemma 9.1 at such a depth and write

\[
b_q-\lambda_q\mathbf1
=
\mathbf1_{\mathcal B_q}-\theta_q\mathbf1.
\]

By Theorem 7.1,

\[
\varepsilon_I N_q
\le
\left\|
P_{E_1\oplus E_{\ge3}}
(b_q-\lambda_q\mathbf1)
\right\|_2^2.
\tag{10.6}
\]

On the other hand, (10.1), orthogonal projection, and Lemma 9.1 give

\[
\begin{aligned}
\left\|
P_{E_1\oplus E_{\ge3}}
(b_q-\lambda_q\mathbf1)
\right\|_2
&\le
\sqrt{\mathcal H_q}
+\sqrt{2\mathcal E_q+2\sqrt{N_q\mathcal E_q}}.
\end{aligned}
\]

Therefore

\[
\varepsilon_I N_q
\le
2\mathcal H_q
+4\mathcal E_q
+4\sqrt{N_q\mathcal E_q}.
\tag{10.7}
\]

Assume \(0<\varepsilon_I\le1\). Equation (10.7) implies the following
rankwise dichotomy:

\[
\boxed{
\mathcal H_q\ge\frac{\varepsilon_I}{4}N_q
\quad\text{or}\quad
\mathcal E_q\ge\frac{\varepsilon_I^2}{256}N_q.
}
\tag{10.8}
\]

Indeed, if the first alternative fails and
\(\sqrt{\mathcal E_q/N_q}<\varepsilon_I/16\), then the right side of
(10.7) is strictly smaller than \(\varepsilon_I N_q\).

At a global minimizer of the same \(H\)-window objective, the exact
three-slack ledger and the sharp point-margin coefficient give

\[
\begin{aligned}
R_H-4(n-1)B_H
\ge{}&
4(n-1)\sum_{q=1}^H\frac{\mathcal E_q}{c_q}\\
&+
2\sum_{q=1}^H\frac1{c_q}
\sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
\end{aligned}
\tag{10.9}
\]

For \(j\ge3\) and \(j\le r_q\le m\),

\[
(j-2)(n-j-1)\ge n-4.
\tag{10.10}
\]

Every one of the \(\Theta_{u,v}(\sqrt m)\) depths in (10.4) therefore
contributes at least

\[
\min\left\{
\frac{(n-4)\varepsilon_I}{2}N_q,\,
\frac{(n-1)\varepsilon_I^2}{64}N_q
\right\}
=\Omega_I(nW)
\]

to the right side of (10.9). Summing gives

\[
\boxed{
R_H-4(n-1)B_H
\ge
\kappa_A\,nW\sqrt m
}
\tag{10.11}
\]

for some \(\kappa_A>0\) and all sufficiently large \(m\).

This proves (1.2).

The coefficient \(4(n-1)\) is essential. Exact wreath histograms have zero
point margins, so their first possible Johnson harmonic is \(E_2\), whose
transposition coefficient is exactly \(4(n-1)\). The generic coefficient
\(2n\) is not the applicable baseline.

The previously audited implication

\[
P_H\le\frac{E_H}{2}
\le
\frac{R_H-4(n-1)B_H}{8(n-1)}
\tag{10.12}
\]

remains correct. The new result shows that its proposed near-baseline
hypothesis cannot hold: the numerator in (10.12) has order at least
\(nW\sqrt m\), rather than \(o(nW)\), on every fixed nontrivial Gaussian
window.

This does not imply that \(P_H\) or \(E_H\) must themselves be large:
the obstruction may be paid entirely by the \(j\ge3\) spectral slack.
It shows precisely that the component-noise near-equality route cannot
certify their smallness.

## 11. Adversarial audit

1. **Mean subtraction is essential.** The harmonic-matrix representation
   is applied to \(P_{E_2}(\mathbf1_{\mathcal B}-\theta)\), not to the raw
   indicator.

2. **The complete residual is controlled.** The theorem bounds
   \(E_1\oplus E_{\ge3}\), not only the high Johnson degrees. This is needed
   because the Boolean rounding of an exact-factor histogram need not retain
   zero point margins.

3. **The \(a_{n,r}C_3\) term is retained.** It vanishes only asymptotically.
   Formula (5.6) proves that it is \(O(n^{-1})\) throughout a fixed
   \(O(\sqrt n)\) central window.

4. **\(L^2\) closeness alone does not transfer cubic moments.** Lemma 6.1
   supplies the required uniform \(L^4\) control of the \(E_2\) projection.
   No \(L^p\) estimate on the residual is assumed.

5. **No influence hypothesis is used.** The matrix argument covers both
   concentrated and diffuse quadratic forms.

6. **Compactness away from zero is genuine.** The uniform
   \(\varepsilon_I\) tends to zero as the density interval approaches zero.
   No density-independent positive constant down to \(\theta=0\) is claimed.

7. **The proved density cutoff is method-specific.** The argument proves
   \(\theta<\theta_*=(3-\sqrt6)/6\) and the complementary upper range. It
   makes no assertion at or above that threshold.

8. **The facet-star exact theorem remains valid.** Section 8 explains only
   why its naive local-deficit perturbation loses a factor \(r\); the global
   third-moment argument supplies the missing stability by a different
   mechanism.

9. **The gate consequence uses a same-window global minimizer.** This is
   required for the nonnegative switching slack \(R_H-D_H\). The Boolean
   stability theorem itself applies to every family on the slice.

10. **The corrected baseline is used throughout.** The invalid generic
    \(2nB_H\) target is not used. The conclusion is that even the spectrally
    compatible \(4(n-1)B_H\) near-equality target is impossible.

## 12. Final status

The Sparse Boolean-\(E_2\) stability problem is resolved affirmatively,
with a stronger density range. The decisive invariant is the third moment:

\[
\text{Johnson }E_2\text{ skew}\le2\sqrt2+o(1),
\]

whereas

\[
\text{Boolean skew}
=
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}}
>2\sqrt2
\]

for \(0<\theta<(3-\sqrt6)/6\).

The uniform fourth-moment lemma converts this strict skew gap into the
macroscopic projection bound (1.1). The resulting rankwise dichotomy,
combined with exact zero point margins and the three-slack identity, forces
the global lower bound (10.11). Hence the corrected component-noise gate is
not merely difficult: on fixed Gaussian windows it is quantitatively false.

No unproved stability, inverse, or hypercontractive lemma is used.
