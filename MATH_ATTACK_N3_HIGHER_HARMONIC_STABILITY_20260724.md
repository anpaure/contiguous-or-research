# Third-wave N: sparse Boolean stability in higher Johnson harmonics

## 0. Verdict

The sparse Boolean-\(E_2\) phenomenon extends to every fixed Johnson
harmonic degree and to every fixed finite harmonic band.

Let

\[
\Omega_{n,k}=\binom{[n]}k,\qquad
\frac13\le\frac kn\le\frac23,
\]

and let \(\mathcal B\subseteq\Omega_{n,k}\) have density \(\theta\). Put

\[
g=\mathbf1_{\mathcal B}-\theta\mathbf1,
\qquad
L=\log\!\left(\frac{4\sqrt n}{\theta}\right).
\]

For fixed \(j\ge1\), define

\[
D_j=\frac{j^j}{j!}.
\]

For the fixed-level statements below assume

\[
1\le j\le\min(k,n-k),\qquad
\min(k,n-k)\ge j(j-1),\qquad L\ge2.
\]

For a band through level \(J\), replace the middle hypothesis by
\(\min(k,n-k)\ge J(J-1)\). These finite-size conditions are automatic
in the central asymptotic regime with fixed \(j,J\).

The main fixed-level theorem is

\[
\boxed{
\|P_jg\|_{2,\mathrm{prob}}^2
\le
4e^2D_j^2[8(L-1)]^j\theta^2.
}
\tag{0.1}
\]

Hence

\[
\boxed{
\operatorname{dist}_{2,\mathrm{prob}}^2(g,E_j)
\ge
\theta(1-\theta)
-4e^2D_j^2[8(L-1)]^j\theta^2.
}
\tag{0.2}
\]

At density \(\theta\sim2/m\), on \(n=2m+1\) central slices,

\[
\frac{\|P_jg\|_2^2}{\|g\|_2^2}
=O_j\!\left(\frac{\log^jm}{m}\right),
\tag{0.3}
\]

so a sparse Boolean centered indicator is asymptotically almost orthogonal
to every fixed \(E_j\), including every fixed \(j\ge3\).

More generally, for every fixed \(J\ge2\),

\[
\boxed{
\|P_{E_2\oplus\cdots\oplus E_J}g\|_2^2
\le
C_J\theta^2L^J,
\qquad
C_J=4e^2\sum_{j=2}^{J}8^jD_j^2.
}
\tag{0.4}
\]

Thus every fixed low harmonic band captures only

\[
O_J(\theta L^J)
\]

of the variance. For polynomially sparse density this tends to zero.

A separate equality-pattern argument gives dimension-free fourth and
higher moments. For fixed \(j,s\ge2\), on the same central range and
with \(n\ge6j\),

\[
\boxed{
\|h\|_{2s,\mathrm{prob}}
\le
\frac{[6\cdot2s(2s-1)j^2]^j}{\sqrt{j!}}\,
\|h\|_{2,\mathrm{prob}}
\qquad(h\in E_j).
}
\tag{0.5}
\]

In particular, with

\[
\Lambda_j=\frac{(72j^2)^j}{\sqrt{j!}},
\]

\[
\|h\|_{4,\mathrm{prob}}\le\Lambda_j\|h\|_{2,\mathrm{prob}}.
\tag{0.6}
\]

This yields a direct fourth-moment obstruction

\[
\|P_jg\|_{2,\mathrm{prob}}^2\le\Lambda_j^2\theta^{3/2},
\tag{0.7}
\]

and a uniform positive separation on an explicit fixed density interval
depending only on \(j\).

For exact factors, fix \(A>0\), put \(H=\lceil A\sqrt m\rceil\), and
minimize the exact \(H\)-window floor objective. The fixed-band theorem
strengthens the sparse early-rank component-noise lower bound. For each
fixed \(J\ge2\), uniformly over every such same-window global minimizer,

\[
\boxed{
R_H-4(n-1)B_H
\ge
\left(
\frac{4(J-1)}{3(J+1)}-o(1)
\right)nW.
}
\tag{0.8}
\]

Here and below in this consequence, \(o(1)=o_{A,J}(1)\), uniformly over
the minimizer set.

Consequently,

\[
\liminf_{m\to\infty}
\inf_{F\in\mathfrak M_{m,A}}
\frac{R_H(F)-4(n-1)B_H}{nW}
\ge\frac43.
\tag{0.9}
\]

This is only a quantitative strengthening of an already closed route. The
audited Boolean-\(E_2\) skew theorem gives the much larger
\(\Omega_A(nW\sqrt m)\) gap on a positive-density Gaussian subwindow.

No presently live exact-factor gate requires purity in \(E_j\) for a fixed
\(j\ge3\). The higher-harmonic theorem therefore kills no additional
existing route. It does rule out every hypothetical gate that requires an
integer load, after valid Boolean rounding, to concentrate in one fixed
\(E_j\) or in a fixed finite low band. It does not address a band whose
degree grows with \(m\), non-Boolean component increments, or literal-word
constructions.

## 1. Harmonic \(j\)-arrays

All norms in Sections 1--5 are probability norms unless explicitly
labelled otherwise.

Fix

\[
1\le j\le\min(k,n-k).
\]

For a function

\[
a:\binom{[n]}j\longrightarrow\mathbb R,
\]

write \(a_A=a(A)\). Call \(a\) harmonic when

\[
\boxed{
\sum_{i\notin T}a_{T\cup\{i\}}=0
\qquad
\left(T\in\binom{[n]}{j-1}\right).
}
\tag{1.1}
\]

Put

\[
H_a(x)=\sum_{|A|=j}a_A\prod_{i\in A}(x_i-\rho),
\qquad
\rho=\frac kn.
\tag{1.2}
\]

On the slice \(\sum_i x_i=k\), every lower-degree term in the expansion
of (1.2) vanishes by (1.1) and its iterated contractions. Hence

\[
H_a(x)=\sum_{|A|=j}a_A\prod_{i\in A}x_i
\qquad(x\in\Omega_{n,k}).
\tag{1.3}
\]

The image of the harmonic arrays is exactly the Johnson module \(E_j\).
Indeed, if \(A_J\) is the adjacency operator of \(J(n,k)\), direct
summation using (1.1) gives

\[
A_JH_a=\bigl((k-j)(n-k-j)-j\bigr)H_a.
\]

Thus the image lies in the usual degree-\(j\) Johnson eigenspace.
One self-contained dimension proof is as follows. Let \(U_r\) and
\(D_{r+1}=U_r^*\) be Boolean-lattice up and down operators. The identity

\[
D_{r+1}U_r-U_{r-1}D_r=(n-2r)I
\]

makes \(U_{j-1}\) injective when \(j\le n/2\). Therefore

\[
\dim\ker D_j=\binom nj-\binom n{j-1}=\dim E_j.
\]

The positive norm formula below makes the restriction map injective, so
the eigenvalue statement and dimension equality identify its image with
\(E_j\).

### Lemma 1.1 (exact slice and product norms)

For harmonic \(j\)-arrays \(a,b\), where
\(1\le j\le\min(k,n-k)\),

\[
\boxed{
\mathbb E_{\Omega_{n,k}}H_aH_b
=c_{n,k,j}\sum_{|A|=j}a_Ab_A,
\qquad
c_{n,k,j}
=\frac{(k)_j(n-k)_j}{(n)_{2j}}.
}
\tag{1.4}
\]

Under independent Bernoulli coordinates of mean \(\rho=k/n\),

\[
\boxed{
\mathbb E_{\mu_\rho}H_aH_b
=[\rho(1-\rho)]^j\sum_{|A|=j}a_Ab_A.
}
\tag{1.5}
\]

### Proof

For (1.5), the centered product monomials are mutually orthogonal.

For (1.4), let

\[
h_t(S)=\sum_{\substack{A\subseteq S\\|A|=j}}a_A
\qquad(S\in\binom{[n]}t).
\]

Then

\[
U_th_t=(t+1-j)h_{t+1}.
\]

On the harmonic degree-\(j\) image,

\[
U_t^*U_t
\]

has eigenvalue

\[
(t+1-j)(n-t-j).
\]

This follows inductively from
\(D_{t+1}U_t-U_{t-1}D_t=(n-2t)I\), starting with
\(D_ja=0\).

Consequently,

\[
\|h_{t+1}\|_{2,\mathrm{count}}^2
=\frac{n-t-j}{t+1-j}\,
\|h_t\|_{2,\mathrm{count}}^2.
\]

Starting from

\[
\|h_j\|_{2,\mathrm{count}}^2=\sum_Aa_A^2
\]

and iterating to \(t=k\) gives

\[
\|h_k\|_{2,\mathrm{count}}^2
=\binom{n-2j}{k-j}\sum_Aa_A^2.
\]

Division by \(\binom nk\) gives

\[
\frac{\binom{n-2j}{k-j}}{\binom nk}
=\frac{(k)_j(n-k)_j}{(n)_{2j}},
\]

which is (1.4). Polarization gives the bilinear statement. \(\square\)

The exact slice-to-product squared-norm ratio is

\[
\mathcal R_{n,k,j}
=
\frac{c_{n,k,j}}{[\rho(1-\rho)]^j}
\]

\[
=
\prod_{r=0}^{j-1}\left(1-\frac rk\right)
\prod_{r=0}^{j-1}\left(1-\frac r{n-k}\right)
\prod_{r=0}^{2j-1}\left(1-\frac rn\right)^{-1}.
\tag{1.6}
\]

If

\[
\min(k,n-k)\ge j(j-1),
\]

then

\[
\prod_{r=0}^{j-1}\left(1-\frac rk\right)
\ge1-\frac{j(j-1)}{2k}\ge\frac12,
\]

and similarly on the complementary side. Therefore

\[
\boxed{\mathcal R_{n,k,j}\ge\frac14.}
\tag{1.7}
\]

This factor two between product and slice \(L^2\) norms is the only
norm-comparison loss used below.

## 2. Product-chaos moment bound

Let \(X_i\) be independent Bernoulli variables of mean \(\rho\), and put

\[
\xi_i=\frac{X_i-\rho}{\sqrt{\rho(1-\rho)}}.
\]

For \(p\ge2\), define

\[
\beta_p(\rho)=\|\xi_i\|_p.
\]

If \(\rho\in[1/3,2/3]\), then

\[
\beta_p(\rho)\le\|\xi_i\|_\infty\le\sqrt2.
\tag{2.1}
\]

### Lemma 2.1 (random-colour decoupling)

For every harmonic \(H_a\) of degree \(j\),

\[
\boxed{
\|H_a\|_{p,\mu_\rho}
\le
D_j[2\beta_p(\rho)\sqrt{p-1}]^j
\|H_a\|_{2,\mu_\rho},
\qquad
D_j=\frac{j^j}{j!}.
}
\tag{2.2}
\]

### Proof

Multiplying every degree-\(j\) coefficient by
\([\rho(1-\rho)]^{j/2}\) rewrites \(H_a\) as a homogeneous chaos in the
standardized variables \(\xi_i\); this common scale cancels from the norm
ratio. We work in that normalization.

Colour every coordinate independently and uniformly with one of \(j\)
colours. Retain only monomials whose \(j\) coordinates receive all
different colours. Every \(j\)-set is rainbow with probability

\[
\frac{j!}{j^j}.
\]

If \(H_\chi\) is the retained chaos, then

\[
H_a=D_j\,\mathbb E_\chi H_\chi.
\tag{2.3}
\]

For a fixed colouring, the \(j\) colour classes are independent. The
one-block estimate

\[
\left\|\sum_i\xi_iV_i\right\|_p
\le
2\beta_p(\rho)\sqrt{p-1}
\left(\sum_i\|V_i\|_p^2\right)^{1/2}
\tag{2.4}
\]

follows by independent-copy symmetrization, the scalar Rademacher moment
bound \(\sqrt{p-1}\), and Minkowski in \(L_{p/2}\). Iterating (2.4)
through the \(j\) independent colour blocks gives

\[
\|H_\chi\|_p
\le
[2\beta_p(\rho)\sqrt{p-1}]^j\|H_\chi\|_2.
\]

The rainbow coefficient tensor has \(L^2\) norm at most that of the full
tensor. Minkowski in (2.3) proves (2.2). \(\square\)

## 3. Conditioning back to the slice

Let

\[
\Pi_{n,k}
=\Pr\{\operatorname{Bin}(n,k/n)=k\}.
\]

The integer \(k\) is a mode of this binomial law. Its variance is at most
\(n/4\). Chebyshev gives probability at least \(3/4\) to the fewer than
\(3\sqrt n\) integers satisfying

\[
|N-k|<\sqrt n.
\]

Every one of those point masses is at most the modal mass
\(\Pi_{n,k}\), so

\[
\boxed{\Pi_{n,k}\ge\frac1{4\sqrt n}.}
\tag{3.1}
\]

Conditioning the product law on \(\sum_iX_i=k\), using (1.7), (2.1), and
(2.2), gives

\[
\boxed{
\|h\|_{p,\mathrm{slice}}
\le
2(4\sqrt n)^{1/p}D_j
[2\sqrt{2(p-1)}]^j
\|h\|_{2,\mathrm{slice}}
}
\tag{3.2}
\]

for \(h\in E_j\), provided

\[
\rho\in[1/3,2/3],
\qquad
\min(k,n-k)\ge j(j-1).
\]

The factor \((4\sqrt n)^{1/p}\) is the conditioning cost. Taking
\(p\asymp\log(n/\theta)\) makes it harmless for sparse Boolean functions.

## 4. Sparse Boolean-\(E_j\) stability

### Theorem 4.1 (fixed-level stability)

Assume the hypotheses of (3.2), let
\(\mathcal B\subseteq\Omega_{n,k}\) have density \(0<\theta<1\), and put

\[
g=\mathbf1_{\mathcal B}-\theta.
\]

Let

\[
L=\log\!\left(\frac{4\sqrt n}{\theta}\right)\ge2.
\]

Then

\[
\boxed{
\|P_jg\|_2^2
\le
4e^2D_j^2[8(L-1)]^j\theta^2.
}
\tag{4.1}
\]

Consequently,

\[
\boxed{
\operatorname{dist}_2^2(g,E_j)
\ge
\theta(1-\theta)
-4e^2D_j^2[8(L-1)]^j\theta^2.
}
\tag{4.2}
\]

### Proof

Let \(h=P_jg=P_j\mathbf1_{\mathcal B}\). Orthogonal projection and
Hölder give

\[
\|h\|_2^2
=\langle\mathbf1_{\mathcal B},h\rangle
\le
\theta^{1-1/p}\|h\|_p.
\tag{4.3}
\]

Apply (3.2) and divide by \(\|h\|_2\):

\[
\|h\|_2
\le
2(4\sqrt n)^{1/p}D_j
[2\sqrt{2(p-1)}]^j
\theta^{1-1/p}.
\]

Square and choose \(p=L\). Since

\[
(4\sqrt n)^{2/L}\theta^{-2/L}=e^2,
\]

one obtains (4.1). Pythagoras gives (4.2). \(\square\)

An equivalent classification statement is:

> If
> \[
> \operatorname{dist}_2^2(g,E_j)
> \le\varepsilon\theta(1-\theta),
> \]
> then necessarily
> \[
> (1-\varepsilon)(1-\theta)
> \le
> 4e^2D_j^2[8(L-1)]^j\theta.
> \tag{4.4}
> \]

Thus genuinely near-\(E_j\) Boolean functions cannot have
\(\theta L^j\to0\).

### Corollary 4.2 (density \(2/m\))

Let \(n=2m+1\), fix \(j\), and fix \(C<\infty\). Uniformly for
\(|k-m|\le C\sqrt m\), at density \(\theta=2/m\),

\[
\frac{\|P_jg\|_2^2}{\theta(1-\theta)}
\le
\frac{
8e^2D_j^2[8(L-1)]^j
}{m(1-2/m)}
=O_j\!\left(\frac{\log^jm}{m}\right),
\tag{4.5}
\]

where

\[
L=\log\!\bigl(2m\sqrt{2m+1}\bigr).
\]

Therefore

\[
\boxed{
\operatorname{dist}_2^2(g,E_j)
=(1-o(1))\theta(1-\theta).
}
\tag{4.6}
\]

The same conclusion holds whenever

\[
\theta\log^j(4\sqrt n/\theta)\longrightarrow0.
\]

## 5. Fixed finite harmonic bands

### Theorem 5.1 (band stability)

Fix \(J\ge2\), assume

\[
\min(k,n-k)\ge J(J-1),
\]

and retain the central-slice hypotheses. Then

\[
\boxed{
\|P_{E_2\oplus\cdots\oplus E_J}g\|_2^2
\le
C_J\theta^2L^J,
}
\tag{5.1}
\]

where

\[
\boxed{
C_J=4e^2\sum_{j=2}^{J}8^j
\left(\frac{j^j}{j!}\right)^2.
}
\tag{5.2}
\]

### Proof

The Johnson levels are orthogonal, so sum (4.1) over \(2\le j\le J\).
Since \(L\ge2\),

\[
[8(L-1)]^j\le8^jL^J.
\]

This proves (5.1). \(\square\)

Consequently,

\[
\frac{
\|P_{E_2\oplus\cdots\oplus E_J}g\|_2^2
}{\theta(1-\theta)}
\le
\frac{C_J\theta L^J}{1-\theta}.
\tag{5.3}
\]

Every fixed low band therefore captures \(o(1)\) of the Boolean variance
whenever

\[
\theta L^J\to0.
\]

No assertion is made for \(J=J(m)\to\infty\).

## 6. Direct fourth and higher moments

The optimized product argument is sharp enough for the sparse application.
There is also a dimension-free moment proof entirely inside the slice.
All unlabelled norms in this section are probability norms unless
explicitly labelled as counting norms.

Assume

\[
\frac13\le\frac kn\le\frac23,
\qquad
n\ge6j.
\]

### Lemma 6.1 (terminal tensor contraction)

Let \(\mathcal H=(V;E_1,\ldots,E_r)\) be a finite multihypergraph in which
every vertex has degree at least two. For functions

\[
b_\ell:[n]^{E_\ell}\longrightarrow\mathbb C,
\]

one has

\[
\boxed{
\sum_{x_V}\prod_{\ell=1}^{r}|b_\ell(x_{E_\ell})|
\le
\prod_{\ell=1}^{r}\|b_\ell\|_{2,\mathrm{count}}.
}
\tag{6.1}
\]

### Proof

Induct on \(|V|\). Choose a vertex \(v\) of degree \(d\ge2\). For fixed
values of all other variables, apply \(d\)-fold Hölder in \(x_v\) to the
\(d\) incident factors. Replace each incident \(b_\ell\) by

\[
\widetilde b_\ell
=
\left(\sum_{x_v}|b_\ell|^d\right)^{1/d}.
\]

Deleting \(v\) leaves every other vertex degree unchanged, hence still at
least two. Also

\[
\|\widetilde b_\ell\|_2\le\|b_\ell\|_2
\]

because \(\ell_d\le\ell_2\) for \(d\ge2\). Apply the induction hypothesis
to the smaller hypergraph. If deleting \(v\) leaves an empty edge, its
function is simply a scalar factor and the same induction applies.
\(\square\)

### Theorem 6.2 (dimension-free \(2s\)-moment bound)

For every fixed \(j\ge1\), integer \(s\ge2\), and \(h\in E_j\),

\[
\boxed{
\|h\|_{2s}
\le
\Lambda_{j,s}\|h\|_2,
\qquad
\Lambda_{j,s}
=
\frac{[6\cdot2s(2s-1)j^2]^j}{\sqrt{j!}}.
}
\tag{6.2}
\]

### Proof

Write \(h=H_a\) with harmonic coefficient array \(a\), and put

\[
T=\sum_{|A|=j}a_A^2.
\]

Put \(z_i=x_i-k/n\). In ordered form,

\[
h=
\frac1{j!}
\sum_{\substack{(i_1,\ldots,i_j)\in[n]^j\\
                 i_1,\ldots,i_j\ {\rm distinct}}}
a_{\{i_1,\ldots,i_j\}}z_{i_1}\cdots z_{i_j}.
\tag{6.2a}
\]

There are \(N=2sj\) labelled coordinate slots in the expansion. For a
compatible partition \(\pi\) of those slots, let \(V(\pi)\) be its blocks,
let \(E_r\subseteq V(\pi)\) be the \(j\) distinct blocks used by the
\(r\)-th tensor, and define

\[
S_\pi
=
\sum_{\phi:V(\pi)\hookrightarrow[n]}
\prod_{r=1}^{2s}a_{\phi(E_r)}.
\]

Exchangeability of the slice makes

\[
M_\pi
=
\mathbb E\prod_{v\in V(\pi)}
z_{\phi(v)}^{\deg(v)}
\]

independent of the injection \(\phi\), and \(|M_\pi|\le1\). Therefore

\[
\mathbb Eh^{2s}
=
\frac1{(j!)^{2s}}\sum_\pi M_\pi S_\pi.
\tag{6.2b}
\]

We first discard the moment weights:
\(|M_\pi S_\pi|\le|S_\pi|\). This order is essential; leaf elimination
below is applied only to the unweighted coefficient contraction
\(S_\pi\), because a collision can change \(M_\pi\).

There are at most

\[
(2sj)^{2sj}
\]

equality patterns among them.

Fix one pattern. Its contraction is a \(2s\)-edge, \(j\)-uniform quotient
multihypergraph. If a quotient vertex is a leaf, sum its coordinate first.
The harmonic identity (1.1) makes the unrestricted sum zero. The injective
sum is therefore the negative sum over collisions with coordinates already
used outside that edge. There are at most

\[
(2s-1)j
\]

such choices. Each collision removes one quotient vertex. At most \(2sj\)
leaf eliminations occur.

After every leaf is removed, Lemma 6.1 applies. In the ordered tensor
normalization,

\[
\|a_{\mathrm{ordered}}\|_2^2=j!T,
\]

so a terminal \(2s\)-tensor contraction is at most

\[
(j!T)^s.
\]

The symmetrized ordered expansion contributes \((j!)^{-2s}\). Combining
the already-discarded moment weights, the pattern count, the collision
branches, and the terminal contraction gives

\[
\mathbb E|h|^{2s}
\le
\frac{
[2s(2s-1)j^2]^{2sj}
}{(j!)^s}
T^s.
\tag{6.3}
\]

On the central range and for \(n\ge6j\), (1.4) gives

\[
c_{n,k,j}\ge6^{-2j}.
\]

Indeed every numerator factor in
\((k)_j(n-k)_j\) is at least \(n/6\), while every denominator factor in
\((n)_{2j}\) is at most \(n\).

Hence

\[
T\le6^{2j}\|h\|_2^2.
\]

Insert this into (6.3) and take a \(2s\)-th root to obtain (6.2).
\(\square\)

At \(s=2\), define

\[
\boxed{
\Lambda_j=\Lambda_{j,2}
=\frac{(72j^2)^j}{\sqrt{j!}}.
}
\tag{6.4}
\]

Then

\[
\boxed{
\mathbb E h^4
\le
\Lambda_j^4(\mathbb E h^2)^2.
}
\tag{6.5}
\]

### Corollary 6.3 (higher-moment Boolean obstruction)

For every Boolean family of density \(\theta\) and every \(s\ge2\),

\[
\boxed{
\|P_jg\|_2^2
\le
\Lambda_{j,s}^2\theta^{\,2-1/s}.
}
\tag{6.5a}
\]

Indeed, for \(h=P_jg=P_j\mathbf1_{\mathcal B}\), Hölder gives

\[
\|h\|_2^2
\le
\theta^{\,1-1/(2s)}\|h\|_{2s}
\le
\Lambda_{j,s}\theta^{\,1-1/(2s)}\|h\|_2.
\]

At \(s=2\), this becomes

\[
\boxed{
\|P_jg\|_2^2
\le
\Lambda_j^2\theta^{3/2}.
}
\tag{6.6}
\]

equivalently,

\[
\|h\|_2^2
=\langle\mathbf1_{\mathcal B},h\rangle
\le\theta^{3/4}\|h\|_4
\le\Lambda_j\theta^{3/4}\|h\|_2.
\]

The higher moments alone also recover a polylogarithmic sparse bound.
If \(\ell=\log(1/\theta)\ge8j\) and
\(s=\lceil\ell/(4j)\rceil\), then

\[
\boxed{
\|P_jg\|_2^2
\le
\frac{(16e^4)^j}{j!}\,
\theta^2\ell^{4j}.
}
\tag{6.6a}
\]

Indeed \(s\le3\ell/(8j)\),
\(6\cdot2s(2s-1)j^2\le4\ell^2\), and
\(\theta^{-1/s}\le e^{4j}\). The optimized
product-conditioning theorem (4.1), with \(\ell^j\) rather than
\(\ell^{4j}\), is stronger; (6.6a) records exactly what the direct slice
moment argument proves.

Consequently,

\[
\boxed{
\operatorname{dist}_2^2(g,E_j)
\ge
\theta(1-\theta)-\Lambda_j^2\theta^{3/2}.
}
\tag{6.7}
\]

Let

\[
\vartheta_j
=
\left(
\frac{\sqrt{\Lambda_j^4+4}-\Lambda_j^2}{2}
\right)^2.
\tag{6.8}
\]

Then every compact interval \(I\subset(0,\vartheta_j)\) has a constant
\(\varepsilon_{I,j}>0\) such that

\[
\operatorname{dist}_{2,\mathrm{count}}^2(g,E_j)
\ge
\varepsilon_{I,j}\binom nk
\qquad(\theta\in I).
\tag{6.9}
\]

Thus a dimension-free fixed-density sparse stability interval exists for
every fixed \(j\). The constants are deliberately crude.

### Skew formulation

Equation (6.5) also gives

\[
\frac{|\mathbb Eh^3|}{(\mathbb Eh^2)^{3/2}}
\le\Lambda_j^2,
\tag{6.10}
\]

because
\(|\mathbb Eh^3|\le\|h\|_2\|h\|_4^2\).

The centered Boolean skew is

\[
\frac{\mathbb Eg^3}{(\mathbb Eg^2)^{3/2}}
=
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}}.
\tag{6.11}
\]

Hence a pure Boolean \(E_j\) function is impossible whenever

\[
0<\theta<
\eta_j
:=
\frac12\left(
1-\frac{\Lambda_j^2}{\sqrt{\Lambda_j^4+4}}
\right).
\tag{6.12}
\]

This is the direct higher-\(j\) analogue of the audited Boolean-\(E_2\)
skew method. For \(j=2\), the sharp matrix calculation gives the much
better constant \(2\sqrt2\) and the cutoff

\[
\frac{3-\sqrt6}{6}.
\]

The generic tensor constants in (6.4) are not claimed sharp.

There is also a literal quantitative near-purity version of the skew
argument. Put

\[
V=\theta(1-\theta),\qquad
h=P_jg,\qquad
\delta=\|g-h\|_2^2,\qquad
\varepsilon=\frac{\delta}{V}.
\]

If \(0<\theta<1/2\) and \(0\le\varepsilon<1\), Booleanity gives

\[
(1-2\theta)\|h\|_2^2=\langle g^2,h\rangle.
\]

Writing \(r=g-h\), using \(|g|\le1\), and then (6.5),

\[
\left|\langle g^2,h\rangle-\mathbb Eh^3\right|
=|\langle r(g+h),h\rangle|
\le
\|h\|_2\sqrt\delta
+\Lambda_j^2\|h\|_2^2\sqrt\delta.
\tag{6.13}
\]

Since \(\|h\|_2^2=V-\delta\), (6.10) and (6.13) imply

\[
\boxed{
1-2\theta
\le
\Lambda_j^2\sqrt{V(1-\varepsilon)}
+\sqrt{\frac{\varepsilon}{1-\varepsilon}}
+\Lambda_j^2\sqrt{\varepsilon V}.
}
\tag{6.14}
\]

In particular, if

\[
\Gamma=1-2\theta-\Lambda_j^2\sqrt V>0,
\]

then

\[
\boxed{
\varepsilon
\ge
\min\left\{
\frac12,\,
\frac{\Gamma^2}{(\sqrt2+\Lambda_j^2\sqrt V)^2}
\right\}.
}
\tag{6.15}
\]

Thus \(\delta=o(V)\), equivalently relative \(o(1)\) proximity to
\(E_j\), is impossible throughout every density range on which
\(\Gamma\) stays positive. This is the
literal higher-\(j\) skew-stability analogue of the audited \(E_2\)
argument. The projection estimate (4.1) is much stronger at density
\(\theta\asymp1/m\).

On the exactly self-complementary slice \(n=2k\), complementation sends a
pure \(E_j\) function to \((-1)^jh\), so odd moments vanish for odd
\(j\). This parity identity cannot be imported to the relevant odd
ground-set slices \(n=2m+1\); the uniform fourth/\(2s\)-moment argument
above does not use it.

## 7. Exact first-shadow arithmetic

There is also a simple exact-only obstruction for every fixed \(j\ge3\).

Let

\[
n=2m+1,\qquad k=m-1,\qquad\theta=\frac2m.
\]

Consider a family of this density, if the density is arithmetically
realizable; otherwise nonexistence is already trivial. Let
\(\Delta_J\) be the positive Laplacian of \(J(n,k)\). Its eigenvalue on
\(E_r\) is

\[
\mu_r=r(n+1-r).
\]

If \(g=\mathbf1_{\mathcal B}-\theta\) lies in \(E_j\), then
\(\mathcal B\) is an equitable two-colouring of \(J(n,k)\). Its
outside-to-\(\mathcal B\) degree must be

\[
\theta\mu_j
=\frac2m\,j(2m+2-j)
=4j-\frac{2j(j-2)}m.
\tag{7.1}
\]

This must be an integer. Therefore:

\[
\boxed{
j\ge3,\quad m>2j(j-2)
\quad\Longrightarrow\quad
\text{no Boolean density-\(2/m\) pure }E_j\text{ family}.
}
\tag{7.2}
\]

For \(j=2\), the remainder vanishes and the ideal degree is \(8\), which
explains why the deeper \(E_2\) obstruction was needed.

The arithmetic statement has a quantitative residual but not useful
stability by itself. If

\[
m>4j(j-2),
\]

then every vertex has cross-degree residual at least

\[
\frac{2j(j-2)}m,
\]

so

\[
\|(\Delta_J-\mu_jI)g\|_{2,\mathrm{prob}}^2
\ge
\frac{4j^2(j-2)^2}{m^2}.
\tag{7.3}
\]

Indeed, for \(S\notin\mathcal B\) the residual is
\(-[b_{\rm in}(S)-\theta\mu_j]\), while for
\(S\in\mathcal B\) it is
\(b_{\rm out}(S)-(1-\theta)\mu_j\). The two target cross-degrees have
distance \(2j(j-2)/m<1/2\) from the integers.

For an exact distance conversion put

\[
M_{n,k,j}
=
\max_{0\le r\le k}|\mu_r-\mu_j|
\le k(n+1-k)=O(m^2).
\]

Then

\[
\boxed{
\operatorname{dist}_{2,\mathrm{prob}}^2(g,E_j)
\ge
\frac{
4j^2(j-2)^2
}{
m^2M_{n,k,j}^2
}
=\Omega_j(m^{-6}).
}
\tag{7.4}
\]

This exact arithmetic stability is far weaker than Theorem 4.1.

## 8. Exact-factor early-rank finite-band obstruction

All norms in Sections 8--12 are unnormalized counting norms on the
indicated rank unless explicitly stated otherwise. Thus an application of
Theorem 5.1 at rank \(q\) multiplies its probability-norm right side by
\(N_q\).

Fix \(A>0\), put

\[
H=\lceil A\sqrt m\rceil,
\]

and return to

\[
n=2m+1,\qquad
W=\binom nm,\qquad
N_q=\binom n{m-q}.
\]

Put

\[
a_q=\frac W{N_q}=c_q+\theta_q,\qquad
c_q=\lfloor a_q\rfloor,\qquad
\rho_q=N_q\theta_q=W-c_qN_q.
\]

Let \(F\) be an exact factor, let \(\mu_q\) be its depth-\(q\)
histogram, and define

\[
f_q=\mu_q-a_q\mathbf1.
\]

Exact point homomesy gives

\[
P_0f_q=P_1f_q=0.
\tag{8.1}
\]

Set

\[
x_q=\mu_q-c_q\mathbf1,
\qquad
E_q=\sum_Sx_q(S)(x_q(S)-1).
\tag{8.2}
\]

Because every \(x_q(S)\) is an integer, \(E_q\ge0\), with equality
exactly for floor-balanced loads \(x_q(S)\in\{0,1\}\).

Equivalently,

\[
E_q
=
\|f_q\|_2^2-N_q\theta_q(1-\theta_q).
\]

Define

\[
B_H
=
\sum_{q=1}^{H}
\frac{N_q\theta_q(1-\theta_q)}{c_q},
\qquad
Q_H
=
\sum_{q=1}^{H}\frac{E_q}{c_q}.
\tag{8.2a}
\]

For an unordered coordinate transposition \(\tau\), put

\[
D_H
=
\sum_\tau\sum_{q=1}^{H}
\frac{\|f_q-\tau f_q\|_2^2}{c_q}.
\tag{8.2b}
\]

If \(u_{q,C}\) and \(w_{q,C}\) are the two complete-side depth-\(q\)
histograms in an overlap component \(C\) of \(F\) with its
\(\tau\)-relabeling, define the audited unscaled component-noise
functional

\[
R_H
=
\sum_\tau\sum_C\sum_{q=1}^{H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\tag{8.2c}
\]

Let \(\mathfrak M_{m,A}\) be the set of exact factors minimizing
\(B_H+Q_H=\sum_{q\le H}\|f_q\|_2^2/c_q\). Since \(B_H\) is
factor-independent, this is equivalently the set minimizing \(Q_H\).
The finite-band argument through (8.7) holds for every exact factor; only
the switching inequality in Section 9 requires
\(F\in\mathfrak M_{m,A}\).

The exact-factor part imports three previously audited theorems: exact
point homomesy, \(R_H-D_H\ge0\) at a same-window global minimizer, and the
three-slack identity (11.1). It also compares with the previously proved
strong \(E_2\) gap (9.4). Those inputs are not reproved here; every new
higher-band consequence from them is proved below.
The gate classifications and fixed-permutation \(E_2\)-invariant fact in
Section 11.2 are likewise imported from the audited synthesis rather
than reproved in this report.

Choose \(\mathcal B_q\) to consist of the \(\rho_q\) largest entries of
\(x_q\), and put

\[
b_q=\mathbf1_{\mathcal B_q}-\theta_q\mathbf1.
\]

The exact top-remainder rounding identity is

\[
\boxed{
\|f_q-b_q\|_2^2
\le E_q.
}
\tag{8.3}
\]

Indeed,

\[
\|x_q-\mathbf1_{\mathcal B_q}\|_2^2-E_q
=2\sum_{S\notin\mathcal B_q}x_q(S)\le0.
\]

The last sum is nonpositive because the selected entries are the
\(\rho_q\) largest integers and \(\sum_Sx_q(S)=\rho_q\).

Let

\[
K=\lfloor m^{1/3}\rfloor.
\]

For fixed \(A>0\), \(K\le H\) for all sufficiently large \(m\). Every
sum \(q\le K\) below means \(1\le q\le K\).

Uniformly for \(q\le K\),

\[
c_q=1,\qquad
\theta_q=O(m^{-1/3}),
\]

and

\[
\boxed{
\sum_{q\le K}N_q\theta_q(1-\theta_q)
=\left(\frac13+o(1)\right)W.
}
\tag{8.4}
\]

For completeness, the constant \(1/3\) follows from

\[
\log a_q
=
\sum_{t=0}^{q-1}
\log\left(1+\frac{2(t+1)}{m-t}\right)
=
\frac{q(q+1)}m
+O\left(\frac{q^3}{m^2}+\frac{q^4}{m^3}\right)
\tag{8.4a}
\]

uniformly for \(q\le K\). Hence \(\log a_q=o(1)\), so \(c_q=1\), and

\[
\frac{N_q\theta_q(1-\theta_q)}W
=
\frac{a_q-1}{a_q}(2-a_q)
=
\frac{q(q+1)}m
+O\left(
\frac{q^3}{m^2}+\frac{q^4}{m^2}
\right).
\]

Summing the main term gives

\[
\frac1m\sum_{q=1}^{K}q(q+1)=\frac13+o(1),
\]

while the summed error is \(O(m^{-1/3})\).

Fix \(J\ge2\). Theorem 5.1 gives

\[
\sum_{q\le K}
\|P_{E_2\oplus\cdots\oplus E_J}b_q\|_2^2
=o(W),
\tag{8.5}
\]

This follows quantitatively as follows. With
\(L_q=\log(4\sqrt n/\theta_q)\),

\[
\begin{aligned}
\sum_{q\le K}
\|P_{E_2\oplus\cdots\oplus E_J}b_q\|_2^2
&\le
C_J
\left[
\sup_{q\le K}
\frac{\theta_qL_q^J}{1-\theta_q}
\right]
\sum_{q\le K}N_q\theta_q(1-\theta_q)\\
&=o(W),
\end{aligned}
\]

because
\(\sup_{q\le K}\theta_qL_q^J=o(1)\).

Thus

\[
\boxed{
\sum_{q\le K}
\|P_{E_1\oplus E_{\ge J+1}}b_q\|_2^2
=\left(\frac13+o(1)\right)W.
}
\tag{8.6}
\]

Put

\[
E=\sum_{q\le K}E_q,
\qquad
T_J=\sum_{q\le K}\sum_{\ell\ge J+1}\|P_\ell f_q\|_2^2.
\]

By (8.1), (8.3), and direct-sum Minkowski,

\[
\boxed{
\sqrt{\left(\frac13-o(1)\right)W}
\le\sqrt E+\sqrt{T_J}.
}
\tag{8.7}
\]

In particular,

\[
E+T_J\ge\left(\frac16-o(1)\right)W.
\tag{8.8}
\]

Equation (8.7) is stronger and gives the optimal weighted consequence of
that two-variable constraint below; no sharpness for exact factors is
claimed.

## 9. Quantitative component-noise consequence

Let \(F\in\mathfrak M_{m,A}\). At this same-window global minimizer, the
corrected three-slack identity gives

\[
\begin{aligned}
R_H-4(n-1)B_H
\ge{}&
4(n-1)E\\
&+
2\sum_{q\le K}\sum_{\ell\ge J+1}
(\ell-2)(n-\ell-1)\|P_\ell f_q\|_2^2.
\end{aligned}
\tag{9.1}
\]

The supported Johnson levels satisfy \(\ell\le m-q\le m\). For

\[
h(\ell)=(\ell-2)(n-\ell-1)
\]

one has

\[
h(\ell+1)-h(\ell)=n-2\ell>0
\qquad(\ell\le m).
\]

Therefore, for fixed \(J\),

\[
(\ell-2)(n-\ell-1)
\ge
(J-1)(n-J-2)
\qquad(\ell\ge J+1).
\]

Put

\[
\alpha=4(n-1),
\qquad
\beta_J=2(J-1)(n-J-2).
\]

Weighted Cauchy gives

\[
(\sqrt E+\sqrt{T_J})^2
\le
\left(\frac1\alpha+\frac1{\beta_J}\right)
(\alpha E+\beta_JT_J).
\]

Combining this with (8.7) and (9.1),

\[
R_H-4(n-1)B_H
\ge
\frac{\alpha\beta_J}{\alpha+\beta_J}
\left(\frac13-o(1)\right)W,
\]

and hence

\[
\boxed{
R_H-4(n-1)B_H
\ge
\left(
\frac{4(J-1)}{3(J+1)}-o(1)
\right)nW.
}
\tag{9.2}
\]

The error \(o(1)=o_{A,J}(1)\) is uniform over
\(F\in\mathfrak M_{m,A}\).

For example, the constants are

\[
\frac49\quad(J=2),
\qquad
\frac23\quad(J=3).
\]

Since (9.2) holds for every fixed \(J\),

\[
\boxed{
\liminf_{m\to\infty}
\inf_{F\in\mathfrak M_{m,A}}
\frac{R_H(F)-4(n-1)B_H}{nW}
\ge\frac43.
}
\tag{9.3}
\]

The quantifiers in (9.3) are: first fix \(J\), let \(m\to\infty\), and
then take the supremum over fixed \(J\). No uniform theorem for
\(J=J(m)\) is being used. The number \(4/3\) is the supremum of this
family of valid lower bounds; it is not asserted to be attained or sharp.

This improves the sparse-block constant from the \(E_2\)-only argument,
but not the best known component-noise no-go. The audited Boolean-\(E_2\)
third-moment theorem on a positive-density subwindow already gives

\[
R_H-4(n-1)B_H=\Omega_A(nW\sqrt m).
\tag{9.4}
\]

Thus higher-level stability supplies a structural refinement, not a new
qualitative closure.

## 10. Hypothetical shifted \(E_j\) baselines

The transposition energy on rank \(r\) is

\[
\sum_\tau\|f-\tau f\|_2^2
=2\sum_{\ell\ge0}\ell(n-\ell+1)\|P_\ell f\|_2^2.
\tag{10.1}
\]

Exact wreath point homomesy kills only \(E_0,E_1\). Therefore the true
lowest admissible module is \(E_2\), and the true spectral coefficient is

\[
4(n-1).
\]

Here is the precise conditional statement. Suppose hypothetically that a
new exact invariant killed

\[
P_\ell f_q=0
\qquad
(0\le\ell<j,\ 1\le q\le H)
\]

for some fixed \(j\ge3\), throughout the entire controlled window, and
let \(F\in\mathfrak M_{m,A}\). The shifted spectral baseline would then be

\[
\gamma_j=2j(n-j+1).
\]

The first surplus coefficient, at \(E_{j+1}\), would be

\[
\sigma_j
=2\bigl[(j+1)(n-j)-j(n-j+1)\bigr]
=2(n-2j).
\]

In fact the exact spectral identity is

\[
\boxed{
D_H-\gamma_j(B_H+Q_H)
=
2\sum_{q\le H}\frac1{c_q}
\sum_{\ell\ge j+1}
(\ell-j)(n+1-j-\ell)\|P_\ell f_q\|_2^2.
}
\tag{10.1a}
\]

All terms are nonnegative on the supported central ranks. Together with
\(R_H-D_H\ge0\) at the minimizer, the early-block rounding argument
charges \(E\) at coefficient \(\gamma_j\) and the tail at coefficient at
least \(\sigma_j\).

Near equality, together with small floor-rounding error, would force a
Boolean bonus family close to \(E_j\), which Theorem 4.1 forbids on the
sparse block. More explicitly, Theorem 5.1 through level \(j\) and the
full lower-level annihilation hypothesis give

\[
\sqrt{\left(\frac13-o(1)\right)W}
\le
\sqrt E+
\left(
\sum_{q\le K}\sum_{\ell\ge j+1}\|P_\ell f_q\|_2^2
\right)^{1/2}.
\]

Weighted Cauchy with coefficients \(\gamma_j\) and \(\sigma_j\) then
gives

\[
\boxed{
R_H-\gamma_jB_H
\ge
\left(
\frac{2j}{3(j+1)}-o(1)
\right)nW.
}
\tag{10.2}
\]

This is a conditional proposition only. The full-window annihilation
hypothesis is essential: if lower levels survive at some controlled
\(q>K\), they contribute negatively relative to the shifted baseline and
(10.2) need not follow. No known wreath identity annihilates
\(E_2,\ldots,E_{j-1}\), and harmonic projection is not an integral
operation. There is therefore no present \(E_j\)-baseline exact-factor
gate to which (10.2) applies.

## 11. Audit of existing gates

### Normalization warning

Throughout Sections 9--11, \(\tau\) ranges over the
\(\binom n2\) unordered coordinate transpositions, and \(D_H,R_H\) are
unaveraged sums. The functional \(R_H\) uses the unscaled complete-side
squared-difference convention, four times fair component variance. If

\[
\lambda_\ell=\ell(n-\ell+1)
\]

is the positive Johnson-Laplacian eigenvalue, then on \(E_\ell\)

\[
\sum_\tau\|f-\tau f\|_2^2
=2\lambda_\ell\|f\|_2^2.
\tag{11.0}
\]

Thus the unscaled \(E_2\) coefficient is \(4(n-1)\). Dividing the
squared-displacement sum by \(\binom n2\) changes the coefficient to

\[
\frac{4\lambda_\ell}{n(n-1)},
\]

which is \(8/n\) at \(\ell=2\). For the fair projection
\(\mathsf P_\tau=(I+\tau)/2\), the averaged squared-norm multiplier is

\[
1-\frac{\lambda_\ell}{n(n-1)},
\]

which is \(1-2/n\) at \(\ell=2\). Summing ordered transpositions doubles
both \(D_H\) and \(R_H\). Normalizing the Johnson Laplacian by the graph
degree is yet another convention. Equations (9.2) and (10.2) use only
the unscaled unordered convention; under any alternative convention,
baseline and surplus must be rescaled together.

There is a second, logically separate normalization issue. Suppose
\(\Delta_m\) is a nonnegative *linear* Rayleigh/Dirichlet spectral surplus
above the \(E_j\) baseline, with nonnegative spectral coefficients on the
allowed complement, and the smallest such separation from \(E_j\) is
\(\gamma_m\). The spectral theorem gives only

\[
\operatorname{dist}_2^2(f,E_j)
\le\frac{\Delta_m}{\gamma_m}.
\tag{11.0a}
\]

Therefore the Boolean stability theorem becomes applicable only when the
gate proves

\[
\Delta_m=o(\gamma_m\theta)
\]

after valid rounding, not merely \(\Delta_m=o(\theta)\). For a standard
normalized Johnson walk, adjacent fixed-degree levels can have
\(\gamma_m=\Theta(1/m)\), so this distinction is decisive. The
unnormalized transposition ledger avoids ambiguity by displaying its
actual coefficients. If instead \(\Delta_m\) denotes a squared operator
residual \(\|(\mathsf T-\lambda_jI)f\|_2^2\), then (11.0a) has
\(\gamma_m^2\) in the denominator and the required scale is
\(o(\gamma_m^2\theta)\).

### 11.1 The one existing Johnson near-equality gate

The corrected global component-noise gate is anchored at \(E_2\):

\[
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)
+4(n-1)Q_H\\
&+
2\sum_{q\le H}\frac1{c_q}
\sum_{\ell\ge3}
(\ell-2)(n-\ell-1)\|P_\ell f_q\|_2^2.
\end{aligned}
\tag{11.1}
\]

The equality is algebraic for every exact factor; at
\(F\in\mathfrak M_{m,A}\), all three displayed slacks are nonnegative
because \(R_H-D_H\ge0\). Only in that minimizer scope does near equality
force low floor excess and negligible mass above \(E_2\).
It never forces a profile near \(E_j\) for \(j\ge3\).

This gate is already quantitatively impossible by the sharp Boolean-\(E_2\)
skew theorem, with gap \(\Omega_A(nW\sqrt m)\). Sections 8--9 merely give
an independent finite-band explanation: on the sparse early block, any
near-floor Boolean profile must send its variance beyond every fixed
harmonic band.

### 11.2 Gates not affected

The following live or separately audited statements are not fixed-level
Boolean near-equality assertions:

- RFEN and multistep propagated-noise bounds;
- the positive-cut/local-minimum gate \(LM_A\);
- stationary-class \(SCOV_A\) itself;
- correlated Haar-frame and component-cut inequalities;
- adaptive Hall/recourse and cyclic-alignment gates;
- hard-quota completion and packetized matching;
- subgroup orbit-profile floors;
- Graver, rotor/SCD, and literal-word routes.

Their variables are component increments, propagated signed vectors, cut
covariances, orbit totals, or integral flows. Such vectors need not be
Boolean, and they need not concentrate in any one fixed Johnson module.
Boolean-\(E_j\) stability cannot be applied to them without an additional
rounding and spectral-purity theorem.

The stationary harmonic identity tracks every \(E_j\) component with its
correct character coefficient, but permits an arbitrary mixture of
degrees. A near-\(E_2\) noise-baseline estimate is already dead; \(SCOV_A\)
only asks for low mean floor energy and does not impose that near-baseline
noise estimate.

Likewise, one coordinate permutation cannot create a universal
\(E_j\), \(j\ge3\), lowest surviving space: every such permutation has a
nonzero invariant pure-\(E_2\) zero-margin tangent. Whole-subgroup
invariants are orbit-profile data, not a Boolean \(E_j\) profile.

## 12. Exact scope

Unconditionally proved:

1. exact harmonic \(j\)-array representation and slice/product norm
   constants;
2. the random-colour decoupling constant \(j^j/j!\);
3. the explicit sparse Boolean-\(E_j\) inequality (4.1);
4. fixed-band stability (5.1);
5. dimension-free direct \(2s\)-moment bounds (6.2);
6. direct higher-moment, fourth-moment, pure-skew, and near-purity
   obstructions (6.5a)--(6.15);
7. exact first-shadow nonexistence and residual stability for pure
   \(E_j\), \(j\ge3\);
8. the fixed-band early-rank obstruction (8.7);
9. the quantitative component-noise refinement (9.2)--(9.3), uniformly
   over same-window global minimizers.

Conditionally proved:

1. If a new exact invariant annihilates every level below \(E_j\) at
   every rank in the controlled window, then the shifted-baseline
   inequality (10.2) holds. No such invariant is known.

Not proved:

1. sharp fourth or third moment constants for \(E_j\), \(j\ge3\);
2. a structural classification of near-extremizing harmonic tensors;
3. any theorem for \(j\) or \(J\) growing with \(m\);
4. any Boolean conclusion for projected component vectors without valid
   integral rounding;
5. any implication from a normalized Rayleigh deficit without the
   \(o(\gamma_m\theta)\) linear-surplus scale required by (11.0a), or the
   \(o(\gamma_m^2\theta)\) scale for a squared operator residual;
6. any new obstruction to RFEN, \(LM_A\), \(SCOV_A\), adaptive Hall,
   hard-quota completion, or literal words;
7. MWB, labelled synchronization, or the contiguous-OR width conjecture.

The final mathematical conclusion is:

\[
\boxed{
\text{sparse Boolean profiles escape every fixed Johnson harmonic band,}
}
\]

but the only current exact-factor near-equality architecture governed by
such a fixed band was the already-refuted \(E_2\) component-noise gate.
