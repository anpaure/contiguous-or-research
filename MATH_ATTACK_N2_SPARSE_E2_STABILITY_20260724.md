# Second-wave N: sparse Boolean \(E_2\) stability on the central slice

## 0. Outcome

This lane obtains the needed quantitative stability theorem and closes the
corrected component-noise question in the negative.

Let

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q}.
\]

For a Boolean family \(\mathcal B\) on a central Johnson slice, write

\[
g=\mathbf 1_{\mathcal B}-\theta\mathbf 1,
\qquad
\theta=\frac{|\mathcal B|}{|\Omega|}.
\]

The main single-rank theorem is

\[
\boxed{
\|P_2g\|_{2,\mathrm{prob}}^2
\le
256e^2\theta^2
\log^2\!\left(\frac{4\sqrt n}{\theta}\right)
}
\tag{0.1}
\]

uniformly on slices whose rank ratio lies in \([1/3,2/3]\). At the first
shadow \(\Omega=\binom{[2m+1]}{m-1}\), the constant \(256\) improves to
\(64\). Consequently, at density \(\theta=2/m\),

\[
\boxed{
\operatorname{dist}_{2,\mathrm{prob}}^2(g,E_2)
\ge
\frac2m-\frac4{m^2}
-\frac{256e^2}{m^2}
\log^2\!\bigl(2m\sqrt{2m+1}\bigr).
}
\tag{0.2}
\]

Thus

\[
\operatorname{dist}_{2,\mathrm{prob}}^2(g,E_2)
=\frac{2+o(1)}m,
\]

while \(\|g\|_2^2=(2/m)(1-2/m)\). Sparse Boolean centered indicators are
asymptotically almost orthogonal to \(E_2\), not close to it.

The single first-shadow estimate is only \(O(W/m)=o(W)\) in counting norm,
so by itself it cannot contradict an \(o(W)\) window allowance. The
decisive observation is that the same theorem applies uniformly to the
first

\[
K=\lfloor m^{1/3}\rfloor
\]

depths. Their exact floor-fraction variances sum to

\[
\left(\frac13+o(1)\right)W.
\]

An exact integer rounding lemma transfers any near-floor exact-factor
histogram to the required Boolean bonus family at squared cost no larger
than its floor-quadratic excess. Exact point homomesy removes degree one.
It follows that every exact factor satisfies

\[
\boxed{
\sum_{q\le K}
\left(
E_q+\sum_{j\ge3}\|P_jf_q\|_2^2
\right)
\ge
\left(\frac16-o(1)\right)W,
}
\tag{0.3}
\]

where \(E_q\) is the rank-\(q\) floor-quadratic excess and all norms in
(0.3) are unnormalized counting norms.

At a global minimizer, the corrected three-slack identity therefore gives

\[
\boxed{
R_H-4(n-1)B_H
\ge
\left(\frac13-o(1)\right)nW
}
\tag{0.4}
\]

for every fixed \(A>0\) and \(H=\lceil A\sqrt m\rceil\). In particular,

\[
R_H\le4(n-1)B_H+o(nW)
\]

is impossible. This refutes the corrected global component-noise gate as
an attainable sufficient route. It does not refute MWB: the component-noise
gate was already strictly stronger than low overload.

All constants in the sparse projection theorem, the integer rounding
bridge, the early-rank sum, and the implication to (0.4) were independently
audited.

## 1. Exact-factor and component-noise setup

Unless explicitly marked “prob”, every norm from this point onward is the
unnormalized counting norm on the relevant slice.

At depth \(q\), put

\[
r_q=m-q,\qquad
a_q=\frac{W}{N_q},\qquad
c_q=\lfloor a_q\rfloor,
\]

\[
\rho_q=W-c_qN_q,\qquad
\theta_q=\frac{\rho_q}{N_q}.
\]

Thus

\[
a_q=c_q+\theta_q.
\]

For an exact wreath factor, let \(\mu_q\) be its rank-\(r_q\) cyclic
interval histogram and define

\[
f_q=\mu_q-a_q\mathbf 1.
\]

Every coordinate belongs to exactly \(r_q\) intervals in each wreath.
Since the factor has \(W/n\) wreaths,

\[
\sum_{S\ni i}\mu_q(S)=\frac{r_qW}{n}
\qquad(i\in[n]).
\tag{1.1}
\]

The constant vector \(a_q\mathbf1\) has the same point margins:

\[
a_q\binom{n-1}{r_q-1}
=\frac{W}{N_q}\frac{r_qN_q}{n}
=\frac{r_qW}{n}.
\]

Therefore

\[
\boxed{P_0f_q=P_1f_q=0,}
\tag{1.2}
\]

so

\[
f_q\in\bigoplus_{j\ge2}E_j.
\]

This exact point-homomesy fact is indispensable below.

Define the rank floor-quadratic excess

\[
\boxed{
E_q
=\sum_S
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
}
\tag{1.3}
\]

Since \(\mu_q(S)-c_q\) is integral, every summand is nonnegative. Also

\[
E_q=\|f_q\|_2^2-N_q\theta_q(1-\theta_q).
\tag{1.4}
\]

For a height \(H\), write

\[
\mathcal E_H=\sum_{q\le H}\frac{E_q}{c_q},
\qquad
\mathcal H_H=\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}\|P_jf_q\|_2^2.
\tag{1.5}
\]

Also put

\[
B_H=\sum_{q\le H}\frac{N_q\theta_q(1-\theta_q)}{c_q}.
\]

For an unordered coordinate transposition \(\tau\), let
\(\mathcal C_\tau\) be the overlap components of the factor with its
\(\tau\)-image, and let \(u_{q,C},w_{q,C}\) be the two component
histograms. In the unscaled convention,

\[
R_H=\sum_\tau\sum_{C\in\mathcal C_\tau}
\sum_{q\le H}\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q},
\]

whereas the coherent transposition energy is

\[
D_H=\sum_\tau\sum_{q\le H}
\frac{\|f_q-\tau f_q\|_2^2}{c_q}.
\]

The corrected component-noise analysis gives, at a global minimizer, the
exact decomposition

\[
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+2\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}(j-2)(n-j-1)\|P_jf_q\|_2^2\\
&+4(n-1)\mathcal E_H.
\end{aligned}
\tag{1.6}
\]

All three terms on the right are nonnegative. Hence the proposed upper
gate

\[
R_H\le4(n-1)B_H+o(nW)
\tag{1.7}
\]

would imply both

\[
\mathcal E_H=o(W)
\tag{1.8}
\]

and

\[
\mathcal H_H=o(W).
\tag{1.9}
\]

The rest of the report proves that (1.8) and (1.9) cannot hold
simultaneously.

## 2. Spectral dictionary at the first shadow

All norms in this section are probability norms.

Let

\[
\Omega=\binom{[n]}k,\qquad
n=2m+1,\qquad k=m-1,
\]

and let \(A\) be the Johnson adjacency operator. Its degree is

\[
d=k(n-k)=(m-1)(m+2).
\]

The adjacency eigenvalue on \(E_j\) is

\[
\lambda_j=d-j(n-j+1),
\]

while the positive Laplacian eigenvalue is

\[
\mu_j=j(n-j+1).
\]

In particular,

\[
\mu_1=2m+1,\qquad
\mu_2=4m,\qquad
\mu_3=6m-3.
\tag{2.1}
\]

Let \(\mathcal B\subseteq\Omega\) have density \(\theta\), and put

\[
g=\mathbf1_{\mathcal B}-\theta\mathbf1
=\sum_{j=1}^{k}g_j.
\]

Define

\[
\varepsilon
=\operatorname{dist}_{2,\mathrm{prob}}^2(g,E_2)
=\|g_1\|_2^2+\sum_{j\ge3}\|g_j\|_2^2.
\tag{2.2}
\]

Since

\[
\|g\|_2^2=\theta(1-\theta),
\]

one has

\[
\varepsilon=\theta(1-\theta)-\|g_2\|_2^2.
\tag{2.3}
\]

The exact adjacency residual

\[
\Delta=(A-\lambda_2I)g
\tag{2.4}
\]

satisfies

\[
\boxed{
\|\Delta\|_2^2
=(2m-1)^2\|g_1\|_2^2
+\sum_{j=3}^{m-1}
\bigl(j(2m+2-j)-4m\bigr)^2\|g_j\|_2^2.
}
\tag{2.5}
\]

Thus, for \(m\ge4\),

\[
(2m-3)^2\varepsilon
\le\|\Delta\|_2^2.
\tag{2.6}
\]

For \(m\ge5\), the largest multiplier is

\[
(m-3)(m+1),
\]

so

\[
\|\Delta\|_2^2
\le(m-3)^2(m+1)^2\varepsilon.
\tag{2.7}
\]

If \(c(X)\) is the number of Johnson neighbours of \(X\) in the opposite
Boolean cell, then

\[
c(X)=
\begin{cases}
4m\theta+\Delta(X),&X\notin\mathcal B,\\[1mm]
4m(1-\theta)-\Delta(X),&X\in\mathcal B.
\end{cases}
\tag{2.8}
\]

At \(\theta=2/m\), the ideal cross-degrees are therefore

\[
8\quad\text{outside }\mathcal B,
\qquad
4m-8\quad\text{inside }\mathcal B.
\tag{2.9}
\]

Exact membership in \(E_2\) is exactly the equitable two-colouring
condition \(\Delta=0\). A signed Rayleigh defect is not enough for
stability, because the \(E_1\) and \(E_{\ge3}\) terms in
\(\langle g,(L-4mI)g\rangle\) have opposite signs. Squared spectral defect,
or separate harmonic control, is required.

For the one-swap Markov operator \(P=A/d\), (2.6) gives

\[
\|(P-\lambda_2/d)g\|_2^2
\ge
\left(\frac{2m-3}{(m-1)(m+2)}\right)^2\varepsilon.
\tag{2.10}
\]

Once the sparse stability theorem is proved, (2.10) will give the exact
one-swap scale \(m^{-3}\).

## 3. Uniform sparse Boolean \(E_2\) stability

All norms in this section are probability norms.
All logarithms are natural.

### Theorem 3.1 (uniform central-slice level-two bound)

Let

\[
\Omega=\binom{[n]}k,\qquad
\frac13\le\frac kn\le\frac23,
\qquad n\ge9.
\]

For every Boolean family \(\mathcal B\subseteq\Omega\) of density
\(0<\theta\le1\),

\[
\boxed{
\|P_2(\mathbf1_{\mathcal B}-\theta)\|_2^2
\le
256e^2\theta^2
\log^2\!\left(\frac{4\sqrt n}{\theta}\right).
}
\tag{3.1}
\]

Consequently,

\[
\boxed{
\operatorname{dist}_2^2(
\mathbf1_{\mathcal B}-\theta,E_2)
\ge
\theta(1-\theta)
-256e^2\theta^2
\log^2\!\left(\frac{4\sqrt n}{\theta}\right).
}
\tag{3.2}
\]

### Proof

Every \(h\in E_2\) has a unique harmonic quadratic representation

\[
h(S)=\sum_{\{i,j\}\subseteq S}a_{ij},
\tag{3.3}
\]

where

\[
a_{ij}=a_{ji},\qquad a_{ii}=0,\qquad
\sum_{j\ne i}a_{ij}=0
\quad(i\in[n]).
\tag{3.4}
\]

Put

\[
T=\sum_{i<j}a_{ij}^2.
\]

A direct same-edge/share-one-vertex/disjoint-edge expansion gives

\[
\boxed{
\|h\|_{2,\mathrm{slice}}^2
=\beta_{n,k}T,
\qquad
\beta_{n,k}
=\frac{(k)_2(n-k)_2}{(n)_4}.
}
\tag{3.5}
\]

Indeed, if \(B_1\) is the sum of \(a_ea_{e'}\) over pairs of edges sharing
one endpoint and \(B_0\) is the corresponding disjoint-edge sum, the
row-sum conditions give

\[
B_1=-T,\qquad B_0=\frac T2.
\]

Substitution of the three inclusion probabilities yields (3.5).

Now let \(X_i\) be independent Bernoulli variables of mean

\[
p=\frac kn,
\]

and set

\[
Z_i=\frac{X_i-p}{\sqrt{p(1-p)}}.
\]

Since \(p\in[1/3,2/3]\), every \(Z_i\) is mean zero, variance one, and
\(|Z_i|\le\sqrt2\). The row-sum conditions in (3.4) kill the constant and
linear product terms, leaving

\[
h(X)=p(1-p)\sum_{i<j}a_{ij}Z_iZ_j.
\tag{3.6}
\]

For independent mean-zero variables bounded by \(\sqrt2\), the elementary
linear moment bound is

\[
\left\|\sum_i c_iZ_i\right\|_s
\le2\sqrt s\left(\sum_i c_i^2\right)^{1/2}
\qquad(s\ge2).
\tag{3.7}
\]

It follows either from the bounded-variable moment generating function or
from symmetrization followed by the Rademacher moment estimate.

Let

\[
Q(Z)=\sum_{i<j}a_{ij}Z_iZ_j.
\]

Choose a uniform random bipartition \(I\sqcup I^c=[n]\), independently of
the \(Z_i\), and let

\[
Q_I=\sum_{i\in I,\ j\in I^c}a_{ij}Z_iZ_j.
\]

Every edge crosses with probability \(1/2\), so

\[
Q=2\mathbb E_IQ_I.
\]

For fixed \(I\), apply (3.7) first in the \(I^c\)-variables and then to
the coefficient linear forms in the \(I\)-variables. Minkowski in
\(L_{s/2}\) gives

\[
\|Q_I\|_s\le4s\sqrt T.
\]

Therefore

\[
\boxed{\|Q\|_s\le8s\sqrt T.}
\tag{3.8}
\]

Under the product measure,

\[
\|h\|_{2,\mathrm{prod}}^2=p^2(1-p)^2T.
\]

The exact ratio between the product and slice squared norms is

\[
\mathcal R_{n,k}
=
\frac{k(n-k)(n-1)(n-2)(n-3)}
{n^3(k-1)(n-k-1)}
<4.
\tag{3.9}
\]

Thus

\[
\|h\|_{s,\mathrm{prod}}
\le8s\|h\|_{2,\mathrm{prod}}
\le16s\|h\|_{2,\mathrm{slice}}.
\tag{3.10}
\]

Let

\[
\pi=\Pr\{\operatorname{Bin}(n,k/n)=k\}.
\]

Elementary factorial bounds give

\[
\boxed{\pi\ge\frac1{4\sqrt n}.}
\tag{3.11}
\]

For completeness, use the elementary Stirling--Wallis inequalities

\[
\sqrt{2\pi}\,t^{t+1/2}e^{-t}
\le t!
\le e\,t^{t+1/2}e^{-t}
\qquad(t\ge1).
\]

They give

\[
\begin{aligned}
\pi
&=\binom nk(k/n)^k(1-k/n)^{n-k}\\
&\ge
\frac{\sqrt{2\pi}}{e^2}
\sqrt{\frac{n}{k(n-k)}}\\
&\ge
\frac{2\sqrt{2\pi}}{e^2\sqrt n}
>\frac1{4\sqrt n}.
\end{aligned}
\]

The last coarse comparison follows from
\(\sqrt{2\pi}>2\) and \(e^2<9\), since \(4/9>1/4\).
Conditioning the product law on \(\sum_iX_i=k\) now yields

\[
\boxed{
\|h\|_{s,\mathrm{slice}}
\le16s\,\pi^{-1/s}\|h\|_{2,\mathrm{slice}}.
}
\tag{3.12}
\]

Take

\[
h=P_2\mathbf1_{\mathcal B}
=P_2(\mathbf1_{\mathcal B}-\theta).
\]

By orthogonal projection and Hölder,

\[
\|h\|_2^2
=\langle\mathbf1_{\mathcal B},h\rangle
\le\theta^{1-1/s}\|h\|_s.
\tag{3.13}
\]

Combining (3.12) and (3.13),

\[
\|h\|_2^2
\le
256s^2\pi^{-2/s}\theta^{2-2/s}.
\tag{3.14}
\]

Choose

\[
s=\log\!\left(\frac{4\sqrt n}{\theta}\right)>2.
\]

Since \(\pi^{-1}\le4\sqrt n\),

\[
(\pi\theta)^{-2/s}\le e^2.
\]

Equation (3.14) becomes (3.1), and (3.2) follows from
\(\|\mathbf1_{\mathcal B}-\theta\|_2^2=\theta(1-\theta)\).
\(\square\)

### Theorem 3.2 (sharper first-shadow constant)

For

\[
n=2m+1,\qquad k=m-1,\qquad m\ge4,
\]

the constant \(256\) in (3.1) improves to \(64\):

\[
\boxed{
\|P_2(\mathbf1_{\mathcal B}-\theta)\|_2^2
\le
64e^2\theta^2
\log^2\!\left(\frac{4\sqrt{2m+1}}{\theta}\right).
}
\tag{3.15}
\]

The only change in the proof is that the exact ratio in (3.9) is now

\[
\mathcal R_m
=
\frac{4m(m-1)^2(m+2)(2m-1)}
{(m-2)(m+1)(2m+1)^3}
<1.
\tag{3.16}
\]

The denominator minus the numerator in (3.16) is

\[
8m^4+2m^3-57m^2-5m-2>0
\qquad(m\ge3).
\]

Hence the factor \(2\) in (3.10) is absent, replacing \(16s\) by \(8s\)
and \(256\) by \(64\).

At \(\theta=2/m\), put

\[
L_m=\log\!\bigl(2m\sqrt{2m+1}\bigr).
\]

Then (3.15) gives

\[
\|P_2g\|_2^2
\le\frac{256e^2L_m^2}{m^2},
\tag{3.17}
\]

and therefore

\[
\boxed{
\operatorname{dist}_2^2(g,E_2)
\ge
\frac2m-\frac4{m^2}
-\frac{256e^2L_m^2}{m^2}.
}
\tag{3.18}
\]

Equivalently,

\[
\frac{\operatorname{dist}_2^2(g,E_2)}
{\|g\|_2^2}
\ge
1-\frac{128e^2L_m^2}{m(1-2/m)}.
\tag{3.19}
\]

Thus the relative distance tends to one.

Combining (2.10) and (3.18) gives the exact one-swap version:

\[
\boxed{
\begin{aligned}
\|(P-\lambda_2/d)g\|_2^2
\ge{}&
\left(\frac{2m-3}{(m-1)(m+2)}\right)^2\\
&\times
\left[
\frac2m-\frac4{m^2}
-\frac{256e^2L_m^2}{m^2}
\right]_+.
\end{aligned}
}
\tag{3.20}
\]

In particular,

\[
\|(P-\lambda_2/d)g\|_2^2
\ge\frac{8-o(1)}{m^3}.
\tag{3.21}
\]

The universal squared one-swap-defect lower scale supplied by sparse
stability at density \(2/m\) is therefore \(m^{-3}\).

## 4. Exact and robust facet consequences

The level-two theorem is asymptotically strongest, but the original
full-facet cascade also admits a fully quantitative finite-\(m\)
robustification.

Retain

\[
n=2m+1,\qquad r=m-1,\qquad k=m-2,
\qquad \theta=\frac2m.
\]

For \(T\in\binom{[n]}k\), define

\[
\kappa(T)
=\#\{S\in\mathcal B:T\subset S\}.
\]

The extension star over \(T\) has size

\[
s=n-k=m+3.
\]

### Theorem 4.1 (exact sparse \(E_2\) exclusion)

For every \(m\ge18\), no nontrivial family
\(\mathcal B\subseteq\binom{[2m+1]}{m-1}\) of density \(2/m\) has

\[
\mathbf1_{\mathcal B}-\frac2m\mathbf1\in E_2.
\]

### Proof

Exact \(E_2\) membership gives the cross-degrees in (2.9). If \(T\) is
not full, choose an outside extension \(S\supset T\). Every bonus extension
of \(T\) is a bonus Johnson neighbour of \(S\), so

\[
\kappa(T)\le8
\qquad\text{or}\qquad
\kappa(T)=m+3.
\tag{4.1}
\]

For \(S\in\mathcal B\), summing over its \((m-2)\)-facets gives

\[
\sum_{T\subset S}\kappa(T)=m^2-2m+5.
\tag{4.2}
\]

If all \(m-1\) facets were full, the sum would be

\[
(m-1)(m+3)=m^2+2m-3.
\]

Thus the total deficit from full size is \(4m-8\). Every nonfull facet
has deficit in \([m-5,m+3]\). For \(m\ge18\), three such deficits are too
small and five are too large. Therefore every \(S\in\mathcal B\) has
exactly four nonfull facets and \(m-5\) full facets.

Let \(\mathcal F\) be the family of full facets. If \(U\) is the up
operator from rank \(m-2\) to rank \(m-1\), then

\[
U\mathbf1_{\mathcal F}=(m-5)\mathbf1_{\mathcal B}.
\tag{4.3}
\]

The singular square of \(U\) on \(E_j\) is

\[
(m-1-j)(m+3-j)>0,
\]

so \(U\) is injective and intertwines harmonic degree. Hence the centered
indicator of \(\mathcal F\) also lies in \(E_2\).

Every full facet has exactly four nonfull neighbours through each of its
\(m+3\) extensions, so its Johnson boundary degree in \(\mathcal F\) is

\[
4(m+3).
\]

An \(E_0\oplus E_2\) Boolean family at rank \(m-2\) has boundary degree

\[
4m(1-\operatorname{dens}\mathcal F)<4m.
\]

This contradiction proves the theorem. \(\square\)

### Theorem 4.2 (robust full-facet cascade)

Let \(m\ge100\), let

\[
g=\mathbf1_{\mathcal B}-\frac2m\mathbf1,
\qquad
z=(L-4mI)g,
\qquad Z^2=\|z\|_{2,\mathrm{count}}^2.
\]

Then

\[
\boxed{
Z^2\ge\frac23\frac{|\mathcal B|}{m^2}.
}
\tag{4.4}
\]

Consequently,

\[
\boxed{
\operatorname{dist}_{2,\mathrm{count}}^2(g,E_2)
\ge
\frac{2|\mathcal B|}
{3m^2(m-3)^2(m+1)^2}
>
\frac{2|\mathcal B|}{3m^6}.
}
\tag{4.5}
\]

### Proof with audited constants

Let \(D\) be the down operator and \(U=D^*\). Since

\[
UD=(m-1)(m+3)I-L,
\]

one has

\[
\boxed{
(U\kappa)(S)
=(m^2-2m-3)\mathbf1_{\mathcal B}(S)+8-z(S).
}
\tag{4.6}
\]

Thus \(Z^2\) is exactly the squared discrepancy of the two cross-degree
equations in (2.9).

For every nonfull facet, summing over its outside extensions gives the
sharp penalty

\[
\boxed{
\sum_T(s-\kappa(T))(\kappa(T)-8)_+^2
\le Z^2.
}
\tag{4.7}
\]

There is no extra factor \(m+3\). For fixed \(S\notin\mathcal B\), its
neighbours are partitioned by its facets, and

\[
\sum_{T\subset S}(\kappa(T)-8)_+^2
\le
\left(\sum_{T\subset S}\kappa(T)-8\right)_+^2
=z(S)_-^2.
\]

Summing over outside \(S\) proves (4.7).

Let

\[
\mathcal H=\{T:9\le\kappa(T)\le m+2\},
\qquad
\mathcal F=\{T:\kappa(T)=m+3\}.
\]

Equation (4.7) implies

\[
\sum_{T\in\mathcal H}\kappa(T)
\le\frac{15}{m-12}Z^2.
\tag{4.8}
\]

Put

\[
u=U\mathbf1_{\mathcal F}-(m-5)\mathbf1_{\mathcal B}.
\]

The deficit identity from (4.6), split between low facets
\(\kappa\le8\) and the exceptional family \(\mathcal H\), gives

\[
\|u\|_2^2
\le
\left(
\frac{30(m-1)}{m-12}
+\frac{2}{(m-17)^2}
\right)Z^2
<34Z^2.
\tag{4.9}
\]

In particular,

\[
\left|
(m+3)|\mathcal F|-(m-5)|\mathcal B|
\right|
\le\sqrt{34|\mathcal B|}\,Z.
\tag{4.10}
\]

The minimum singular square of \(U\) is \(5\). Combining (4.9) with
the lower spectral gap in (2.6) shows that the non-\(E_0\oplus
E_2\) part of \(\mathbf1_{\mathcal F}\) has squared norm less than
\(9Z^2\). Hence its spectral boundary satisfies

\[
|\partial\mathcal F|
\le4m|\mathcal F|+9m^2Z^2.
\tag{4.11}
\]

Directly counting the four expected missing facets through each full
extension, with the error \(u\), gives

\[
|\partial\mathcal F|
\ge4(m+3)|\mathcal F|
-6m\sqrt{|\mathcal B|}\,Z.
\tag{4.12}
\]

Therefore

\[
12|\mathcal F|
\le6m\sqrt{|\mathcal B|}\,Z+9m^2Z^2.
\tag{4.13}
\]

Use (4.10), and set

\[
y=\frac{mZ}{\sqrt{|\mathcal B|}}.
\]

Equations (4.10) and (4.13) imply

\[
9y^2+
\left(
6+\frac{12\sqrt{34}}{m(m+3)}
\right)y
-\frac{12(m-5)}{m+3}
\ge0.
\tag{4.14}
\]

For \(m\ge100\), the left side of (4.14) is negative at
\(y=\sqrt{2/3}\): indeed,

\[
6+\frac{12\sqrt{34}}{m(m+3)}<6.007,
\qquad
\frac{12(m-5)}{m+3}\ge\frac{1140}{103}.
\]

Thus \(y^2>2/3\), which is (4.4). Finally, (2.7) gives (4.5).
\(\square\)

Theorem 4.2 is a finite-\(m\), facet-local certificate. The asymptotic
level-two estimate (3.18) is much stronger: it forces almost the entire
Boolean variance, not merely an \(m^{-6}\) fraction, outside \(E_2\).

## 5. Sharpness and structural examples

The order of the level-two upper bound is essentially sharp.
All norms in this section are probability norms.

Fix a \(t\)-set \(T\subseteq[n]\) and let

\[
\mathcal U_T=\{S\in\binom{[n]}k:T\subseteq S\}.
\]

Its density is

\[
\theta_t=\frac{(k)_t}{(n)_t}.
\]

A direct pair-covariance calculation gives

\[
\boxed{
\|P_2\mathbf1_{\mathcal U_T}\|_2^2
=
\theta_t^2
\frac{(t)_2(n-k)_2\,n(n-3)}
{2(n-t)_2(k)_2}.
}
\tag{5.1}
\]

For central \(k\) and \(t=o(\sqrt n)\), the factor after \(\theta_t^2\)
is

\[
\binom t2(1+o(1)).
\]

Taking \(t=\log_2m+O(1)\) gives density \(\Theta(1/m)\) and relative
\(E_2\) mass

\[
\Theta\!\left(\frac{\log^2m}{m}\right).
\]

Thus the \(\theta\log^2(1/\theta)\) relative scale in Theorem 3.1 cannot in
general be replaced by a smaller order.

Some natural quadratic families live near \(E_2\) only at constant density.
For example, the pair-XOR family

\[
\mathbf1_{\{1\in S\}}\oplus\mathbf1_{\{2\in S\}}
\]

has density

\[
\theta=\frac{2k(n-k)}{n(n-1)}
\]

and exact relative off-\(E_2\) mass

\[
\frac{(n-2k)^2}{n(n-2)(1-\theta)}.
\tag{5.2}
\]

It is pure \(E_2\) when \(n=2k\). On the present first-shadow slice the
quantity in (5.2) is

\[
\frac{9m}{(2m-1)(m^2+2)}=O(m^{-2}),
\]

but its density is asymptotic to \(1/2\), not \(2/m\). Sparse density,
not Booleanity by itself, is the source of the strong stability theorem.

No complete isomorphism classification of all near-extremizers is needed
for the component-noise application. The quantitative theorem already has
the correct sparse order.

## 6. Exact adjacent-integer Boolean rounding

The following lemma is the decisive bridge from exact-factor loads to
Boolean bonus indicators.
All norms in Sections 6--8 are unnormalized counting norms.

### Lemma 6.1 (top-remainder rounding)

Let \(\mu\in\mathbb Z_{\ge0}^{N}\) have total mass

\[
\sum_S\mu(S)=cN+\rho,
\qquad
0\le\rho<N.
\]

Put

\[
x(S)=\mu(S)-c
\]

and

\[
E=\sum_Sx(S)(x(S)-1).
\]

Choose \(\mathcal B\) to be the \(\rho\) coordinates having largest
values of \(x(S)\). Then

\[
\boxed{
\|\mu-(c\mathbf1+\mathbf1_{\mathcal B})\|_2^2
\le E.
}
\tag{6.1}
\]

### Proof

Since

\[
\sum_Sx(S)=\rho,
\]

one has

\[
\begin{aligned}
\|x-\mathbf1_{\mathcal B}\|_2^2
&=\sum_Sx(S)^2
-2\sum_{S\in\mathcal B}x(S)+\rho,\\
E&=\sum_Sx(S)^2-\rho.
\end{aligned}
\]

Therefore

\[
\|x-\mathbf1_{\mathcal B}\|_2^2-E
=2\sum_{S\notin\mathcal B}x(S).
\tag{6.2}
\]

The last sum is nonpositive. If it were positive, some unselected integer
\(x(S)\) would be at least one. Since \(\mathcal B\) contains the
\(\rho\) largest entries, every selected entry would then be at least one,
so

\[
\sum_{S\in\mathcal B}x(S)\ge\rho,
\]

forcing the outside sum to be nonpositive after all. Equation (6.1)
follows. \(\square\)

This exact constant \(1\) is stronger than a pointwise clamp-and-rebalance
bound. The error is controlled by the floor-quadratic excess \(E\), not by
the much larger remainder \(\rho\).

Apply the lemma at depth \(q\). Let \(\mathcal B_q\) have size \(\rho_q\)
and define

\[
b_q=\mathbf1_{\mathcal B_q}-\theta_q\mathbf1,
\]

\[
e_q=f_q-b_q
=\mu_q-(c_q\mathbf1+\mathbf1_{\mathcal B_q}).
\]

Then

\[
\boxed{\|e_q\|_2^2\le E_q.}
\tag{6.3}
\]

Because of the exact point-margin identity (1.2),

\[
P_{1\oplus\ge3}b_q
=P_{\ge3}f_q-P_{1\oplus\ge3}e_q.
\]

Thus

\[
\boxed{
\operatorname{dist}_2^2(b_q,E_2)
\le
2\sum_{j\ge3}\|P_jf_q\|_2^2+2E_q.
}
\tag{6.4}
\]

The varying harmonic spaces at different ranks cause no issue: (6.4) is
rankwise and can be summed in their orthogonal direct sum.

## 7. The first \(m^{1/3}\) floor fractions

Put

\[
K=\lfloor m^{1/3}\rfloor.
\]

Exactly,

\[
a_q=\frac{W}{N_q}
=\prod_{j=0}^{q-1}
\frac{m+j+2}{m-j}
=\prod_{j=0}^{q-1}
\left(1+\frac{2(j+1)}{m-j}\right).
\tag{7.1}
\]

Uniformly for \(q\le K\), Taylor expansion with the second-order
cancellation gives

\[
\log a_q
=\frac{q(q+1)}m
+O\!\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right)
=o(1).
\tag{7.2}
\]

Consequently, for every sufficiently large \(m\),

\[
\boxed{c_q=1\qquad(1\le q\le K),}
\tag{7.3}
\]

and

\[
\theta_q=a_q-1
=\frac{q(q+1)}m
+O\!\left(\frac{q^4}{m^2}+\frac{q^2}{m^2}\right).
\tag{7.4}
\]

In particular,

\[
\frac2m\le\theta_q=O(m^{-1/3})
\]

uniformly in this range.

Since

\[
\frac{\rho_q}{W}
=1-\frac1{a_q},
\]

equations (7.2)--(7.4) give

\[
\begin{aligned}
\sum_{q=1}^{K}\frac{\rho_q}{W}
&=
\frac1m\sum_{q=1}^{K}q(q+1)+O(m^{-1/3})\\
&=
\frac{K(K+1)(K+2)}{3m}+O(m^{-1/3})\\
&=\frac13+o(1).
\end{aligned}
\tag{7.5}
\]

Moreover,

\[
\sum_{q\le K}
N_q\theta_q^2=o(W),
\]

so

\[
\boxed{
\sum_{q\le K}
N_q\theta_q(1-\theta_q)
=\left(\frac13+o(1)\right)W.
}
\tag{7.6}
\]

At rank \(r_q=m-q\), the ratio \(r_q/n\) lies in \([1/3,2/3]\).
Theorem 3.1 applies uniformly. Since

\[
\sup_{q\le K}
\theta_q
\log^2\!\left(\frac{4\sqrt n}{\theta_q}\right)
=o(1),
\]

it gives

\[
\sum_{q\le K}\|P_2b_q\|_2^2=o(W).
\tag{7.7}
\]

Combining (7.6) and (7.7),

\[
\boxed{
\sum_{q\le K}
\operatorname{dist}_{2,\mathrm{count}}^2(b_q,E_2^{(q)})
=\left(\frac13+o(1)\right)W.
}
\tag{7.8}
\]

This is the required multirank amplification. The first shadow alone has
only \(O(W/m)\) Boolean variance, but the first \(m^{1/3}\) sparse ranks
together carry a positive fraction of \(W\).

## 8. Quantitative failure of the corrected component-noise gate

Apply (6.4) for \(q\le K\). Since \(c_q=1\) in this range,

\[
\begin{aligned}
\sum_{q\le K}
\operatorname{dist}_2^2(b_q,E_2^{(q)})
\le{}&
2\sum_{q\le K}E_q\\
&+
2\sum_{q\le K}\sum_{j\ge3}\|P_jf_q\|_2^2.
\end{aligned}
\tag{8.1}
\]

Comparison with (7.8) proves the unconditional exact-factor inequality

\[
\boxed{
\sum_{q\le K}
\left(
E_q+\sum_{j\ge3}\|P_jf_q\|_2^2
\right)
\ge
\left(\frac16-o(1)\right)W.
}
\tag{8.2}
\]

In particular, at least one of the two aggregate slacks is

\[
\left(\frac1{12}-o(1)\right)W.
\tag{8.3}
\]

Now let \(H=\lceil A\sqrt m\rceil\) for any fixed \(A>0\). Eventually
\(K\le H\). At a global minimizer, (1.6) and nonnegativity give

\[
\begin{aligned}
R_H-4(n-1)B_H
\ge{}&
2(n-4)
\sum_{q\le K}\sum_{j\ge3}\|P_jf_q\|_2^2\\
&+4(n-1)\sum_{q\le K}E_q.
\end{aligned}
\tag{8.4}
\]

Both coefficients in (8.4) are at least \(2(n-4)\). Therefore (8.2)
implies

\[
\boxed{
R_H-4(n-1)B_H
\ge
\left(\frac13-o(1)\right)nW.
}
\tag{8.5}
\]

This is stronger than merely denying an \(o(nW)\) estimate. It puts a
positive asymptotic gap above the proposed baseline.

### The exact failed implication

The corrected criterion proposed

\[
R_H\le4(n-1)B_H+o(nW)
\Longrightarrow
\sum_{q\le H}\frac{O_q}{c_q}=o(W).
\]

The implication is logically valid as a sufficient condition, but its
antecedent is asymptotically impossible for global minimizers by (8.5).
The route is therefore closed.

This conclusion uses all of the following exact facts:

1. integer floor excess, not merely \(L^1\) overload;
2. top-\(\rho_q\) rounding with the sharp cost (6.1);
3. exact point homomesy, hence \(P_1f_q=0\);
4. squared off-\(E_2\) control, not a cancellable signed Rayleigh defect;
5. the entire early block \(q\le m^{1/3}\), not only the first shadow;
6. the fixed-window quantifier \(H=A\sqrt m\), which contains that block.

If any one of these inputs is removed, the contradiction need not follow.

## 9. Scope and remaining theorem status

Proved:

- a self-contained uniform central-slice level-two inequality with explicit
  constant \(256e^2\);
- the improved first-shadow constant \(64e^2\);
- asymptotic relative distance \(1-o(1)\) from \(E_2\) at density
  \(\theta\sim2/m\);
- the one-swap squared-defect lower bound
  \((8-o(1))/m^3\);
- the exact \(m\ge18\) full-facet exclusion;
- a robust \(m\ge100\) facet discrepancy theorem with constants \(2/3\),
  \(34\), and \(9\);
- the sharp top-remainder Boolean rounding lemma;
- the early-rank aggregate identity with limiting constant \(1/3\);
- the unconditional exact-factor slack lower bound (8.2);
- the global-minimizer component-noise gap (8.5).

Not proved or not needed:

1. a complete isomorphism classification of sparse near-extremizers;
2. a fixed-density stability theorem on an interval bounded away from zero;
3. any implication from the failure of the component-noise gate to failure
   of MWB;
4. any obstruction to the positive-cut, adaptive-Hall, hard-quota, product
   box, rotor, or literal-word routes.

The final implication scope is:

\[
\boxed{
\text{the corrected global component-noise gate is impossible,}
}
\]

but

\[
\boxed{
\text{MWB and the contiguous-OR width conjecture remain open.}
}
\]
