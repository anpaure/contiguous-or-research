# Mathematical attack J, wave two: bounded wreath-fibre connectivity

Date: 2026-07-25

Method: pure mathematics only. No web search, literature search, finite
search, solver, or computer-assisted enumeration was used.

## 0. Verdict

This wave gives a concrete bounded/slowly-growing trade connectivity
theorem, but not connectivity of the entire exact-factor fibre.

1. For arbitrary exact factors \(F_0,F_1\), the exact fibre supported on
   \(F_0\cup F_1\) is a weighted Boolean cube, one coordinate for every
   connected component of their middle-ownership overlay. In the
   degree-\(D\) graph restricted to this face, the bits of components larger
   than \(D\) are complete conserved invariants.

2. For the canonical MSW factor \(F_m\) and \(\tau=(2\ 3)\), truncating the
   exact Catalan component hierarchy at \(J\) gives an exact cube of
   dimension
   \[
   d_{m,J}=\sum_{j=0}^J\operatorname{Cat}_{m-j-2}
   \]
   whose coordinate trades have degree at most
   \[
   D_J=\operatorname{Cat}_J+\operatorname{Cat}_{J+1}.
   \]
   If \(J\to\infty\) and \(J=o(m)\), then
   \[
   d_{m,J}=\left(\frac1{12}+o(1)\right)\operatorname{Cat}_m,
   \]
   and its antipodes differ on
   \[
   \left(\frac38+o(1)\right)\operatorname{Cat}_m
   \]
   wreaths per side.

3. Taking \(J=\lfloor\log_4\log m\rfloor\) gives \(D_J=O(\log m)\).
   Thus the \(O(\log m)\)-degree exact-factor graph contains
   \[
   2^{(1/12+o(1))\operatorname{Cat}_m}
   \]
   mutually connected factors and a path replacing a macroscopic
   \(3/8+o(1)\) fraction of one factor. For every fixed
   \(\varepsilon>0\), a constant \(D_\varepsilon\) already gives cube
   dimension at least \((1/12-\varepsilon)\operatorname{Cat}_m\) and
   antipodal replacement at least
   \((3/8-\varepsilon)\operatorname{Cat}_m\).

4. This is sharp inside the two-endpoint support face. Its top MSW
   component has degree
   \[
   \operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1}
   =\left(\frac5{16}+o(1)\right)\operatorname{Cat}_m.
   \]
   Every path from \(F_m\) to \(\tau F_m\) staying in their union uses a
   move at least this large. Hence the endpoint-monotone lifted-Graver
   theorem from wave one cannot be made subexponential merely by refining
   its conformal decomposition.

5. The known universal two-for-two MSW switches are not a Markov basis.
   When \(m\) is even, a well-defined sign on unoriented cyclic orders gives
   a negative-sign census preserved by every universal switch. A genuine
   degree-three MSW component changes that census. This is an invariant of
   the universal two-switch graph, not yet of the graph containing every
   possible degree-two trade.

6. Conversely, no additive invariant of the observed lower-rank load
   vectors can separate any exact factors if it is conserved by all
   applicable degree-two edges. Any conserved full-column additive
   separator factors through a quotient whose separation is witnessed on
   the all-observed-depth-neutral quotient.

The remaining global gate is an outside-face escape for the macroscopic
MSW components. No claim about MWB, labelled synchronization, or the
contiguous-OR conjecture is made.

## 1. Exact factors, trades, and endpoint faces

Put

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\operatorname{Cat}_m=\frac Wn.
\]

Let \(\Omega_m\) be the unoriented cyclic orders on \([n]\), and let
\(A_m=B_m\) be middle-interval incidence. The exact-factor fibre is

\[
\mathfrak F_m
=\{x\in\mathbb Z_{\ge0}^{\Omega_m}:A_mx=\mathbf1\}.
\tag{1.1}
\]

Every member is the indicator of \(B\) pairwise middle-disjoint wreaths.
A reduced trade is

\[
z=\mathbf1_P-\mathbf1_N\in\ker_{\mathbb Z}A_m,
\qquad
\deg z=|P|=|N|.
\tag{1.2}
\]

It is applicable at \(F\) when \(N\subseteq F\).

Let \(F_0,F_1\) be exact factors and put

\[
H=F_0\cap F_1,\qquad
L=F_0\setminus H,\qquad
R=F_1\setminus H.
\tag{1.3}
\]

Their reduced middle-ownership overlay \(\Gamma(F_0,F_1)\) is the bipartite
graph on \(L\mathbin{\dot\cup}R\) in which every middle target not owned by
\(H\) joins its unique owner in \(L\) to its unique owner in \(R\).
Every vertex has degree \(n\). For a connected component \(K\), put

\[
s_K:=|K\cap L|=|K\cap R|.
\tag{1.4}
\]

The equality follows by comparing the degree sums on the two sides.
Define the two-endpoint support face

\[
\mathfrak F[F_0,F_1]
=
\{F\in\mathfrak F_m:\operatorname{supp}F\subseteq F_0\cup F_1\}.
\tag{1.5}
\]

### Theorem 1.1 (exact weighted-cube face theorem)

There is a canonical bijection

\[
\boxed{
\mathfrak F[F_0,F_1]
\cong
\{0,1\}^{\pi_0(\Gamma(F_0,F_1))}.}
\tag{1.6}
\]

More precisely:

1. every face factor contains \(H\);
2. on every component \(K\), it contains either all of \(K\cap L\) or all
   of \(K\cap R\);
3. every independent collection of such side choices is an exact factor;
4. if two face factors differ on the component set \(\mathcal I\), their
   reduced trade has degree
   \[
   \boxed{\deg(F'-F)=\sum_{K\in\mathcal I}s_K.}
   \tag{1.7}
   \]

#### Proof

Let \(C\in H\). Each middle target of \(C\) has no other owner in \(F_0\)
and no other owner in \(F_1\). Thus \(C\) is the only column of
\(F_0\cup F_1\) covering those targets, so every exact factor supported in
the union contains \(C\).

Remove \(H\). For \(v\in L\mathbin{\dot\cup}R\), let
\(x_v\in\{0,1\}\) record whether \(v\) is selected. A middle target
represented by an overlay edge \(uv\), \(u\in L,v\in R\), is covered
exactly once precisely when

\[
x_u+x_v=1.
\tag{1.8}
\]

Along a connected bipartite component these equations force one of the two
alternating assignments: all left vertices and no right vertices, or all
right vertices and no left vertices. Conversely either assignment covers
every edge of the component exactly once. Components have disjoint target
sets, so their choices are independent. This proves (1.6) and assertions
1--3.

Changing the bit of \(K\) removes its \(s_K\) current-side wreaths and
inserts its \(s_K\) opposite-side wreaths. Different components have
disjoint column supports, so degrees add, proving (1.7). \(\square\)

Every coordinate trade of (1.6) is an applicable ordinary
\(A_m\)-Graver move because its ownership overlay is connected.

### Corollary 1.2 (complete degree-\(D\) face invariant)

In the degree-\(D\) Markov graph induced on
\(\mathfrak F[F_0,F_1]\), the orientation bit of every component with
\(s_K>D\) is conserved. Two face vertices are connected if and only if
they agree on all these large-component bits.

Consequently,

\[
\boxed{
\min_{\substack{\text{paths from }F_0\text{ to }F_1\\
\text{inside }\mathfrak F[F_0,F_1]}}
\ \max_{\text{path moves}}\deg z
=\max_Ks_K.}
\tag{1.9}
\]

#### Proof

By (1.7), a face move changing a bit of weight \(s_K>D\) has degree larger
than \(D\), so that bit is invariant. Conversely, every bit of weight at
most \(D\) can be toggled individually by its applicable component trade.
This gives the connectivity classification. The same argument proves the
lower bound in (1.9), while toggling every component separately gives the
matching upper bound. \(\square\)

This invariant is exact only on a specified two-endpoint support face. A
path using a third wreath outside \(F_0\cup F_1\) can leave the cube.

## 2. The established MSW component hierarchy

We use the already-proved component theorem in
MSW_BOUNDARY_CONNECTIVITY.md and
MSW_COMPONENT_HIERARCHY_REDUCTION.md.

Let \(F_m\) be the canonical MSW factor and let \(\tau=(2\ 3)\). For
\(0\le j\le m-2\), the overlay \(\Gamma(F_m,\tau F_m)\) has exactly

\[
N_{m,j}=\operatorname{Cat}_{m-j-2}
\tag{2.1}
\]

components of side size

\[
s_j=\operatorname{Cat}_j+\operatorname{Cat}_{j+1}.
\tag{2.2}
\]

The components are explicitly indexed by
\(R\in\mathcal D_{m-j-2}\), and their root sets on either side are

\[
\mathcal C_{j,R}=\{AR:A\in\mathcal A_j\},
\tag{2.3}
\]

where

\[
\mathcal A_j
=
\{1u0:u\in\mathcal D_{j+1}\}
\mathbin{\dot\cup}
\{10\,1v0:v\in\mathcal D_j\}.
\tag{2.4}
\]

The exact Catalan convolution

\[
\sum_{j=0}^{m-2}
(\operatorname{Cat}_j+\operatorname{Cat}_{j+1})
\operatorname{Cat}_{m-j-2}
=\operatorname{Cat}_m
\tag{2.5}
\]

confirms that these components partition each endpoint factor.
Equations (2.1)--(2.5) are established inputs; all deductions below are
proved here.

## 3. A bounded and logarithmic-degree exact cube

For \(0\le J\le m-2\), freeze every component with \(j>J\) on its
\(F_m\)-side and allow independent side choices on every component with
\(j\le J\). Denote this face subcube by \(\mathcal Q_{m,J}\).

### Theorem 3.1 (exact cutoff-cube connectivity)

The set \(\mathcal Q_{m,J}\) consists of

\[
\boxed{
2^{d_{m,J}}\text{ exact factors},\qquad
d_{m,J}=\sum_{j=0}^J\operatorname{Cat}_{m-j-2}.}
\tag{3.1}
\]

It is connected by always-applicable ordinary Graver trades of degree at
most

\[
\boxed{
D_J=s_J=\operatorname{Cat}_J+\operatorname{Cat}_{J+1}.}
\tag{3.2}
\]

Its two antipodes differ on

\[
\boxed{
v_{m,J}
=\sum_{j=0}^J
(\operatorname{Cat}_j+\operatorname{Cat}_{j+1})
\operatorname{Cat}_{m-j-2}}
\tag{3.3}
\]

wreaths per side, hence on \(2v_{m,J}\) indicator coordinates. Any two
cube vertices can be connected by toggling precisely the component
coordinates on which they differ.

#### Proof

Theorem 1.1 gives one independent Boolean coordinate per selected overlay
component. Their number is (3.1). Catalan numbers, and hence \(s_j\), are
nondecreasing, so every coordinate degree is at most \(s_J\). Switching
all selected components removes the sum of their side sizes, which is
(3.3). Every intermediate side selection is an exact factor by Theorem
1.1. \(\square\)

For \(m\ge4\), the two global sides are disjoint:

\[
F_m\cap\tau F_m=\varnothing.
\tag{3.4}
\]

Indeed, in one wreath the two transposed coordinates have total incidence
\(2m=n-1\) among its \(n\) middle intervals. Some middle interval therefore
contains both or neither and is fixed by \(\tau\). If \(C,\tau C\in F_m\),
these rows share that middle target, so exactness forces \(C=\tau C\).
But a transposition cannot stabilize an unoriented odd cyclic order: its
stabilizer is dihedral, and no nonidentity rotation or reflection has the
cycle type of a single transposition. Thus (3.3) is literal row distance
per side, without endpoint cancellation.

### Lemma 3.2 (uniform Catalan ratio)

If \(0\le\ell<m\), then

\[
\frac{\operatorname{Cat}_{m-\ell}}{\operatorname{Cat}_m}
=
4^{-\ell}
\prod_{t=0}^{\ell-1}
\left(1+\frac3{2(m-t)-1}\right).
\tag{3.5}
\]

Consequently, uniformly for \(\ell=o(m)\),

\[
\frac{\operatorname{Cat}_{m-\ell}}{\operatorname{Cat}_m}
=4^{-\ell}(1+o(1)).
\tag{3.6}
\]

#### Proof

The exact adjacent ratio is

\[
\frac{\operatorname{Cat}_{k-1}}{\operatorname{Cat}_k}
=
\frac{k+1}{4k-2}
=
\frac14\left(1+\frac3{2k-1}\right).
\tag{3.7}
\]

Multiplication for \(k=m,m-1,\ldots,m-\ell+1\) gives (3.5). If
\(\ell=o(m)\), the logarithm of the product after \(4^{-\ell}\) is

\[
O\!\left(\sum_{t=0}^{\ell-1}\frac1{m-t}\right)
=O(\ell/m)=o(1),
\]

which proves (3.6). \(\square\)

### Theorem 3.3 (sharp cutoff asymptotics)

If

\[
J=J(m)\longrightarrow\infty,
\qquad
J=o(m),
\tag{3.8}
\]

then

\[
\boxed{
d_{m,J}
=\left(\frac1{12}+o(1)\right)\operatorname{Cat}_m}
\tag{3.9}
\]

and

\[
\boxed{
v_{m,J}
=\left(\frac38+o(1)\right)\operatorname{Cat}_m.}
\tag{3.10}
\]

#### Proof

By Lemma 3.2, uniformly for \(j\le J\),

\[
\frac{\operatorname{Cat}_{m-j-2}}{\operatorname{Cat}_m}
=4^{-j-2}(1+o(1)).
\tag{3.11}
\]

Therefore

\[
\frac{d_{m,J}}{\operatorname{Cat}_m}
=(1+o(1))\sum_{j=0}^J4^{-j-2}
\longrightarrow
\frac1{16}\frac1{1-1/4}
=\frac1{12}.
\tag{3.12}
\]

For the mass sum, the same uniform factor gives

\[
\frac{v_{m,J}}{\operatorname{Cat}_m}
=(1+o(1))
\sum_{j=0}^J
\frac{\operatorname{Cat}_j+\operatorname{Cat}_{j+1}}{4^{j+2}}.
\tag{3.13}
\]

Let \(C(z)=\sum_{j\ge0}\operatorname{Cat}_jz^j\). The Catalan identity
\(C(z)=1+zC(z)^2\) gives \(C(1/4)=2\). Hence

\[
\begin{aligned}
\sum_{j\ge0}
\frac{\operatorname{Cat}_j+\operatorname{Cat}_{j+1}}{4^{j+2}}
&=
\frac1{16}C(1/4)
+\frac14\bigl(C(1/4)-1\bigr)\\
&=\frac18+\frac14=\frac38.
\end{aligned}
\tag{3.14}
\]

The series is nonnegative and convergent, so its partial sums in (3.13)
tend to \(3/8\). This proves (3.10). \(\square\)

### Corollary 3.4 (logarithmic-degree macroscopic connectivity)

Take

\[
J(m)=\left\lfloor\log_4\log m\right\rfloor.
\tag{3.15}
\]

Since \(\operatorname{Cat}_j\le4^j\),

\[
D_J\le5\cdot4^J\le5\log m.
\tag{3.16}
\]

Thus the degree-\(5\log m\) exact-factor graph has a connected component
containing a Boolean cube of dimension

\[
\left(\frac1{12}+o(1)\right)\operatorname{Cat}_m
\tag{3.17}
\]

and therefore at least

\[
2^{(1/12+o(1))\operatorname{Cat}_m}
\tag{3.18}
\]

vertices. Two of those vertices differ on

\[
\left(\frac38+o(1)\right)\operatorname{Cat}_m
\tag{3.19}
\]

wreaths per side.

The distance between these antipodes in the full degree-\(D_J\) graph is
at least

\[
\frac{v_{m,J}}{D_J}
=\Omega\!\left(\frac{\operatorname{Cat}_m}{\log m}\right),
\tag{3.20}
\]

because every move removes at most \(D_J\) wreaths belonging to the initial
endpoint. The coordinate-by-coordinate cube path gives the upper bound
\(d_{m,J}=(1/12+o(1))\operatorname{Cat}_m\).

### Corollary 3.5 (constant-degree form)

For every \(\varepsilon>0\), choose a fixed \(J=J(\varepsilon)\) so that

\[
\sum_{j=0}^J4^{-j-2}>\frac1{12}-\varepsilon
\]

and

\[
\sum_{j=0}^J
\frac{\operatorname{Cat}_j+\operatorname{Cat}_{j+1}}{4^{j+2}}
>\frac38-\varepsilon.
\]

Then the constant

\[
D_\varepsilon
=\operatorname{Cat}_{J(\varepsilon)}
+\operatorname{Cat}_{J(\varepsilon)+1}
\tag{3.21}
\]

has the following property for all sufficiently large \(m\): the
degree-\(D_\varepsilon\) graph contains a cube of dimension at least
\((1/12-2\varepsilon)\operatorname{Cat}_m\), with antipodes differing on at
least \((3/8-2\varepsilon)\operatorname{Cat}_m\) wreaths per side.

Thus constant-degree trades already connect a double-exponentially large
family on the natural dimension scale, while the logarithmic-degree choice
reaches the sharp small-component limits \(1/12\) and \(3/8\).

## 4. The exact endpoint-face bottleneck

### Theorem 4.1 (macroscopic Graver degree is forced in the endpoint face)

The top MSW component, corresponding to \(j=m-2\), has degree

\[
s_{\mathrm{top}}
=\operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1}.
\tag{4.1}
\]

Moreover,

\[
\boxed{
\frac{s_{\mathrm{top}}}{\operatorname{Cat}_m}
\longrightarrow\frac5{16}.}
\tag{4.2}
\]

Every path from \(F_m\) to \(\tau F_m\) whose intermediate supports remain
inside \(F_m\cup\tau F_m\) contains a trade of degree at least

\[
\left(\frac5{16}+o(1)\right)\operatorname{Cat}_m.
\tag{4.3}
\]

#### Proof

The top component bit differs between the two antipodes. Corollary 1.2
forces a face move changing that bit, and every such move has degree at
least \(s_{\mathrm{top}}\). Finally,

\[
\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_m}
=\frac{m+1}{4m-2}\longrightarrow\frac14
\]

and

\[
\frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
=
\frac{m(m+1)}{4(2m-3)(2m-1)}
\longrightarrow\frac1{16}.
\]

Their sum proves (4.2). \(\square\)

An endpoint-monotone path has every coordinate between its two endpoint
values, so it is contained in their support face. Therefore Theorem 4.1
applies in particular to the endpoint-monotone lifted-Graver path of wave
one. The applicable Graver basis itself contains the top component trade,
of degree \((5/16+o(1))\operatorname{Cat}_m\).

The endpoint loads satisfy

\[
B_r\mathbf1_{\tau F_m}
=\tau B_r\mathbf1_{F_m}
\tag{4.4}
\]

at every rank. Hence their load multisets and all coordinate-symmetric
separable window objectives agree. This equality does not assert that the
canonical MSW factor is balanced.

There is also a sharp ceiling for the native component atlas. If
\(D_m=e^{o(m)}\), then every component of degree at most \(D_m\) has
\(j=o(m)\), because

\[
s_j\ge\operatorname{Cat}_{j+1}\ge2^j.
\tag{4.5}
\]

Theorem 3.3 then shows that native subexponential component toggles can
alter at most

\[
\left(\frac38+o(1)\right)\operatorname{Cat}_m
\tag{4.6}
\]

canonical rows. The excluded component coordinates carry at least
\(5/8-o(1)\) of the row mass. If the permitted native cutoff also
tends to infinity, then the excluded coordinate count is \(o(B)\) and
their row mass is \(5/8+o(1)\). For bounded cutoffs the excluded coordinates
need not be few. This is an obstruction to the fixed-overlay atlas, not to
a path which introduces outside wreaths.

## 5. A genuine invariant for the universal degree-two atlas

Wave one used the following universal exact edge. For distinct
\(\alpha,\beta,\gamma,\delta\), and ordered complementary lists
\(|E|=m-1\), \(|O|=m-2\), put

\[
\begin{aligned}
C&=(\delta,\gamma,E,\beta,\alpha,O),\\
D&=(\beta,\delta,E,\alpha,\gamma,O),\\
C'&=(\delta,\beta,E,\gamma,\alpha,O),\\
D'&=(\gamma,\delta,E,\alpha,\beta,O).
\end{aligned}
\tag{5.1}
\]

The trade

\[
e_{C'}+e_{D'}-e_C-e_D
\tag{5.2}
\]

is a genuine applicable two-for-two edge after a suitable exact
completion. Let \(\mathfrak G_2^{\mathrm{univ}}\) be the graph generated by
all relabelled instances of (5.2). It is important that this is only the
known universal subfamily of degree-two edges.

Assume throughout this section that \(m\) is even. Fix one unoriented
cyclic order \(C_0\). If \(C=\sigma C_0\), define

\[
\epsilon(C)=\operatorname{sgn}(\sigma)\in\{\pm1\}.
\tag{5.3}
\]

This is well-defined. The stabilizer of \(C_0\) is the dihedral group
\(D_{2m+1}\); every rotation of odd length is even, and a reflection has
sign \((-1)^m=1\). Hence \(D_{2m+1}\subseteq A_{2m+1}\).

For an exact factor \(F\), define its negative-sign census

\[
N_-(F)=|\{C\in F:\epsilon(C)=-1\}|.
\tag{5.4}
\]

### Theorem 5.1 (universal two-switch census invariant)

Every edge of \(\mathfrak G_2^{\mathrm{univ}}\) preserves \(N_-\).

#### Proof

Let \(\rho=(\beta\ \gamma)\). Equation (5.1) gives

\[
C'=\rho C,\qquad D'=\rho D,
\tag{5.5}
\]

so \(\rho\) reverses both signs.

Relative to the readout \(C\), the position word of \(D\) is

\[
(m+2,1,3,4,\ldots,m+1,m+3,2,m+4,\ldots,2m+1).
\tag{5.6}
\]

Its inversion count is

\[
(m+1)+(m-1)+1=2m+1,
\tag{5.7}
\]

which is odd. Therefore

\[
\epsilon(D)=-\epsilon(C).
\tag{5.8}
\]

The old pair contains one sign of each kind. Applying \(\rho\) flips both
signs, so the new pair again contains one sign of each kind. Thus (5.2)
preserves the exact census \(N_-\). Relabelling the entire configuration
does not change this conclusion. \(\square\)

### Corollary 5.2 (the universal two-switch family is not a Markov basis)

For every even \(m\ge4\), the graph
\(\mathfrak G_2^{\mathrm{univ}}\) has at least

\[
\boxed{\operatorname{Cat}_{m-3}+1}
\tag{5.9}
\]

connected components.

#### Proof

The \(j=1\) MSW stratum has
\(\operatorname{Cat}_{m-3}\) independent components, each with three
wreaths on either side. The component descriptions (2.3)--(2.4) pair the
old rows \(P_m(x)\) with the new rows \(\tau P_m(x)\) for the same three
roots \(x\). Since a coordinate transposition reverses \(\epsilon\), if one
side contains \(a\) negative rows, the other contains \(3-a\). Switching
the component changes \(N_-\) by

\[
3-2a\in\{-3,-1,1,3\},
\tag{5.10}
\]

which is never zero.

Within the face cube, choose in each \(j=1\) component the side with the
smaller census contribution, keeping every other component fixed. Now
toggle the \(j=1\) components one at a time toward their larger-census
sides. This produces \(\operatorname{Cat}_{m-3}+1\) exact factors with
strictly increasing \(N_-\). By Theorem 5.1 no two lie in the same
universal-edge component. \(\square\)

This invariant separates exact factors with identical symmetric load
objectives. Indeed, Corollary 5.2 produces factors with more than one
census value, so choose one \(F\) with
\(N_-(F)\ne\operatorname{Cat}_m/2\). For any coordinate transposition
\(\sigma\),

\[
N_-(\sigma F)=\operatorname{Cat}_m-N_-(F)\ne N_-(F),
\]

while \(B_r\mathbf1_{\sigma F}=\sigma B_r\mathbf1_F\) at every rank.
Thus \(F\) and \(\sigma F\) have identical load multisets and equal values
of every coordinate-symmetric overload or collision objective, but lie in
different components of the universal two-switch graph. This does not
assert that either factor is balanced.

The smallest unproved extension is

\[
\boxed{
\epsilon(C')\epsilon(D')
=\epsilon(C)\epsilon(D)
\quad\text{for every reduced genuine degree-two trade}.}
\tag{5.11}
\]

No classification of arbitrary two-for-two wreath trades is currently
available. Therefore (5.11), and disconnectedness of the full degree-two
graph, remain **UNPROVED**.

## 6. No conserved additive lower-window invariant can separate factors

We now rule out the lower-window additive invariant search.
For \(1\le r\le n-1\), let

\[
X_r=\mathbb Z^{\binom{[n]}r}
\]

and let \(U_r:X_r\to\mathbb Z^n\) be point-versus-\(r\)-set incidence.
Fix \(H\) with \(m>2H+2\), put \(r_q=m-q\), and write

\[
X_H=\bigoplus_{q=1}^HX_{r_q},
\qquad
\mathcal B_H=(B_{r_1},\ldots,B_{r_H}).
\tag{6.1}
\]

Let \(L_2\) be the integer span of all globally occurring applicable
degree-two exact-factor edge labels. Wave one proved

\[
\boxed{
\mathcal B_H(L_2)
=
\bigoplus_{q=1}^H\ker_{\mathbb Z}U_{r_q}.}
\tag{6.2}
\]

### Theorem 6.1 (no lower-window additive separator)

Let \(G\) be any abelian group and let \(\Psi:X_H\to G\) be a
homomorphism. Define

\[
I_\Psi(F)=\Psi(\mathcal B_H\mathbf1_F).
\tag{6.3}
\]

If \(I_\Psi\) has equal values at the endpoints of every applicable
degree-two edge, then it is constant on the entire exact-factor fibre.
The conclusion remains true if conservation is assumed for every trade of
degree at most \(D\), for any \(D\ge2\), fixed or growing.

#### Proof

For every actual degree-two edge label \(g\), endpoint conservation and
additivity give

\[
\Psi(\mathcal B_Hg)=0.
\]

Thus \(\Psi\) vanishes on the global span
\(\mathcal B_H(L_2)\), which equals the right side of (6.2).

For arbitrary exact factors \(F,F'\), put
\[
z=\mathbf1_{F'}-\mathbf1_F.
\]
Summing the middle equations gives \(\sum_Cz_C=0\). Every point belongs to
exactly \(r\) cyclic \(r\)-intervals of each wreath, so

\[
U_rB_rz
=r\left(\sum_Cz_C\right)\mathbf1
=0.
\tag{6.4}
\]

Hence \(\mathcal B_Hz\) belongs to the right side of (6.2), and

\[
I_\Psi(F')-I_\Psi(F)
=\Psi(\mathcal B_Hz)=0.
\]

This proves constancy. \(\square\)

The use of edge labels based at different factors is legitimate here only
because \(\Psi\) is additive. The theorem is not a path statement.

### Proposition 6.2 (exact integral and modular annihilators)

For \(1\le r\le n-1\), put \(K_r=\ker_{\mathbb Z}U_r\). Then

\[
U_rX_r
=
\left\{d\in\mathbb Z^n:\sum_id_i\in r\mathbb Z\right\}.
\tag{6.5}
\]

Moreover, an integer coefficient vector \(a=(a_S)\) annihilates \(K_r\)
if and only if

\[
\boxed{
a_S=k+\sum_{i\in S}b_i}
\tag{6.6}
\]

for some \(k,b_1,\ldots,b_n\in\mathbb Z\).

Modulo a prime \(p\), the annihilator of the reduction of the integral
lattice \(K_r\) consists exactly of

\[
\boxed{
a_S=c+\sum_{i\in S}\lambda_i,
\qquad c,\lambda_i\in\mathbb F_p.}
\tag{6.7}
\]

If \(p\mid r\), the constant term in (6.7) is the one extra direction not
contained in the row space of \(U_r\); it measures only total mass.

#### Proof

Every column of \(U_r\) has coordinate sum \(r\), proving one inclusion in
(6.5). For \(i\ne j\), choose an \((r-1)\)-set \(T\) disjoint from
\(\{i,j\}\). Then

\[
U_r(e_{T\cup i}-e_{T\cup j})=e_i-e_j.
\tag{6.8}
\]

Thus the root lattice \(\{\sum d_i=0\}\) lies in the image. Adding one
\(r\)-set incidence vector gives every vector whose sum is divisible by
\(r\), proving (6.5).

If \(a\) kills \(K_r\), it induces a homomorphism

\[
\psi:U_rX_r\longrightarrow\mathbb Z,
\qquad
\psi(U_r\mu)=\langle a,\mu\rangle.
\]

Set \(b_i=\psi(e_i-e_n)\) for \(i<n\), and \(b_n=0\). After subtracting
\(d\mapsto\sum_ib_id_i\), the resulting homomorphism kills the root
lattice. The quotient of (6.5) by the root lattice is \(\mathbb Z\), via
\(d\mapsto(\sum_id_i)/r\). Hence the residual homomorphism equals
\(k(\sum d_i/r)\) for some \(k\in\mathbb Z\). Evaluation at
\(d=\mathbf1_S\) gives (6.6). The converse is immediate.

The lattice \(K_r\) is primitive and has rank \(\binom nr-n\). Its
reduction modulo \(p\) therefore has the same dimension, so its annihilator
has dimension \(n\). Every vector in (6.7) annihilates the reduction. The
map

\[
(c,\lambda_1,\ldots,\lambda_n)
\longmapsto
\left(c+\sum_{i\in S}\lambda_i\right)_S
\]

has a one-dimensional kernel: comparison of two \(r\)-sets sharing
\(r-1\) elements forces every \(\lambda_i=t\), and then \(c+rt=0\).
Its image therefore has dimension \(n\), proving (6.7).

If \(p\nmid r\), the constant vector is in the point-row span. If
\(p\mid r\), the point rows have the unique relation
\(\lambda_1=\cdots=\lambda_n\), hence rank \(n-1\), while a constant-one
set function cannot equal \(\sum_{i\in S}\lambda_i\), since this would
force \(rt=1\). Thus the extra direction is exactly the constant term.
\(\square\)

Here primitivity follows from
\(X_r/K_r\cong U_rX_r\subseteq\mathbb Z^n\), which is torsion-free. When
\(p\mid r\), one must not replace the reduction \(\overline K_r\) of the
integral lattice by the larger kernel of the reduced matrix:

\[
\dim\ker_{\mathbb F_p}\overline U_r
=\binom nr-n+1
=\dim\overline K_r+1.
\tag{6.8a}
\]

The extra constant character annihilates \(\overline K_r\), not this whole
larger kernel.

For an exact factor \(F\), its rank-\(r\) load
\(\mu_r=B_r\mathbf1_F\) satisfies

\[
\sum_S\mu_r(S)=W,
\qquad
U_r\mu_r=rB\mathbf1.
\tag{6.9}
\]

Therefore every integral statistic (6.6) has the fixed value

\[
kW+rB\sum_ib_i,
\tag{6.10}
\]

and the same calculation modulo \(p\) handles (6.7), including \(p\mid r\).
Thus integer-linear, modular, and multiplicative monomial statistics built
from the observed lower loads and conserved by every degree-two edge cannot
separate any exact factors, balanced or otherwise.

### Theorem 6.3 (where a full-column additive invariant must live)

Put

\[
N_H
=
\ker_{\mathbb Z}A_m\cap\ker_{\mathbb Z}\mathcal B_H.
\tag{6.11}
\]

Then

\[
\boxed{
\ker_{\mathbb Z}A_m=L_2+N_H}
\tag{6.12}
\]

and hence

\[
\boxed{
\ker_{\mathbb Z}A_m/L_2
\cong
N_H/(N_H\cap L_2).}
\tag{6.13}
\]

#### Proof

If \(z\in\ker_{\mathbb Z}A_m\), summing all middle rows gives
\(\sum_Cz_C=0\). Equation (6.4) then shows

\[
\mathcal B_Hz\in
\bigoplus_{q=1}^H\ker_{\mathbb Z}U_{r_q}.
\]

By (6.2), choose \(\ell\in L_2\) with
\(\mathcal B_H\ell=\mathcal B_Hz\). Then \(z-\ell\in N_H\), proving
(6.12). Equation (6.13) is the second isomorphism theorem. \(\square\)

Thus a genuinely full-column additive invariant conserved by every
degree-two edge is not excluded. Any such separator factors through
\(\ker A_m/L_2\), and by (6.13) its separation is witnessed on a relation
neutral at every observed lower depth. Association-scheme or
lower-histogram characters alone cannot see it.

## 7. Exact remaining lemma and adversarial audit

The smallest global escape statement left by Theorems 3.1 and 4.1 is:

> **Top-component escape lemma -- UNPROVED.** There is
> \(D_m=e^{o(m)}\) and a path in the full exact-factor graph, using moves
> of degree at most \(D_m\), between two vertices of
> \(\mathfrak F[F_m,\tau F_m]\) having opposite orientations on the top
> MSW component.

Such a path must introduce at least one wreath outside
\(F_m\cup\tau F_m\). A stronger sufficient statement would implement
every macroscopic endpoint component by an outside-face path while
restoring the other endpoint-face bits. Concatenating those implementations
would connect \(F_m\) to \(\tau F_m\) by slowly growing trades.

The following qualifications are essential.

1. **Subfamily, not full fibre.** Theorems 3.1--3.5 construct a huge
   connected subcube. They do not connect an arbitrary exact factor to the
   canonical MSW factor.

2. **Degree, not path length.** The \(O(\log m)\) bound is the maximum
   number of wreaths replaced in one coordinate move. An antipodal path
   still has \((1/12+o(1))\operatorname{Cat}_m\) steps, and the full
   degree-bounded distance is at least
   \(\Omega(\operatorname{Cat}_m/\log m)\).

3. **The \(3/8\) ceiling is real.** Small MSW components dominate component
   count but carry only \(3/8\) of the wreath mass. The remaining
   \(5/8\) is concentrated in the large Catalan end of the convolution.

4. **Face bits are not global invariants.** Corollary 1.2 classifies the
   graph induced on one endpoint union. A path leaving that support may
   change a large-component orientation using small trades.

5. **Endpoint-monotone obstruction.** The \(5/16\) lower bound applies to
   every path confined to the endpoint face, including the lifted-Graver
   path from wave one. It does not lower-bound unrestricted paths.

6. **Parity scope.** \(N_-\) is proved invariant only for the relabelled
   universal moves (5.2), not for every genuine two-for-two trade.
   Equation (5.11) is explicitly unproved.

7. **No additive lower-load invariant.** Theorem 6.1 rules out all
   abelian-group-valued additive statistics factoring through the observed
   lower loads. It does not rule out nonlinear support invariants or
   arbitrary wreath-column weights. Theorem 6.3 localizes only full-column
   additive weights conserved by all degree-two edges, when they separate
   two factors, to the fully neutral quotient.

8. **No balance conclusion.** Relabelled endpoints have equal symmetric
   objective values, but the canonical MSW factor is not asserted to be
   balanced. No theorem here decreases overload or proves fixed-window MWB.

Subject to these qualifications, every theorem and estimate above is
unconditional relative only to the established exact MSW component
hierarchy. The two statements explicitly marked UNPROVED are the
full-degree-two parity extension (5.11) and the top-component escape lemma.
