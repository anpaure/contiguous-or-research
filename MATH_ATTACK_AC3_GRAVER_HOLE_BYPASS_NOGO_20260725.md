# AC master redirect: factor-scale decorated circuits and an exact hole-bypass no-go

## 0. Outcome

The generic polynomial-Graver/semigroup-hole version of this lane closes
in the negative, with two new exact obstructions and one sharp composition
theorem.

1. The actual exact-wreath matrix has an explicit applicable decorated
   circuit of factor degree
   \[
   s_m=\operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1}
   >\frac5{16}\operatorname{Cat}_m.
   \]
   It remains a primitive circuit after adjoining all fixed-window lower
   histograms and after adjoining the mobile quota/surplus/deficit variables.
   The underlying restricted wreath semigroup is normal and its exact fibre
   has two points, yet every Markov basis of this restricted support
   configuration must contain the circuit.  Hence semigroup normality and
   absence of holes do not imply polynomial or even subexponential Graver
   degree.

2. There is an explicit linear objective on the same exact-wreath fibre for
   which the minimum improving trade degree is exactly \(s_m\).  Every
   smaller move which leaves the two-endpoint face strictly increases the
   objective, while every smaller move inside the face is trivial.  Thus no
   monotone polynomial-support augmentation theorem can hold for general
   separable linear objectives on the decorated wreath matrix.  The
   objective is deliberately coordinate-specific, so this is not asserted
   to be an MWB local minimum.

3. Conversely, even constant-size Graver circuits and saturation index two
   do not control the absolute repair cost.  A binary \(K_4\)-block
   decorated exact-cover family has a genuine mobile semigroup hole of
   saturation index exactly two, an exact support-eight Graver basis for its
   zero-overload mobile matrix, and a balanced double cover which splits
   into two exact factors, but every
   degree-one factor has overload exactly \(W_0/4\).  Even the best
   factor-preserving deletion bypass costs
   \((1/8+o(1))W_0\).

The positive statement that would still compose to the sharp
contiguous-OR theorem is an **absolute** local-minimum-height bound
\(o(W)\), not a support bound and not relative descent to the unknown global
minimum.  The exact composition is proved in Section 1.

No web search, solver, finite search, or computer enumeration is used.

## 1. The sharp augmentation-to-literal composition theorem

Put
\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]
For fixed \(A>0\), let
\[
H_A=\lceil A\sqrt m\rceil,\qquad
J_A(F)=\sum_{q=1}^{H_A}\frac{O_q(F)}{c_q},
\qquad
J_A^\star=\min_FJ_A(F).
\tag{1.1}
\]
Here \(F\) is one integral exact middle wreath factor, \(O_q(F)\) is its
mobile floor/ceiling overload, and
\[
c_q=\left\lfloor
\frac{\binom{2m+1}{m}}{\binom{2m+1}{m-q}}
\right\rfloor.
\]

Let \(P_A(m)\) be any positive integer, and let
\(\mathscr T_{A,P}(m)\) be a specified symmetric library of applicable
decorated Graver moves whose wreath degrees are at most \(P_A(m)\).
A \(P_A\)-local minimum means an exact factor \(F\) for which no move in
\(\mathscr T_{A,P}(m)\) produces, after reoptimizing all mobile quota
variables at its endpoint, a factor \(F'\) with \(J_A(F')<J_A(F)\).
Define
\[
L_{A,P}(m)=
\max\{J_A(F):F\text{ is a }P_A\text{-local minimum}\}.
\tag{1.2}
\]
The maximum exists: the exact-factor fibre is finite and contains a global
minimum, which is local for every move library.

### Theorem 1.1 — exact absolute composition criterion

If, for every fixed \(A>0\),
\[
\boxed{L_{A,P}(m)=o(W),}
\tag{1.3}
\]
then
\[
\boxed{\nu(k)\le(1+o(1))
\binom{k}{\lfloor k/2\rfloor}.}
\tag{1.4}
\]

For fixed \(A\), strict \(P_A\)-descent reaches a \(P_A\)-local minimum
after at most
\[
\boxed{\Lambda_AWH_A}
\tag{1.5}
\]
moves, where one may take
\[
M_A=\left\lceil e^{3(A+2)^2}\right\rceil,
\qquad
\Lambda_A=\operatorname{lcm}(1,\ldots,M_A).
\tag{1.6}
\]
Every intermediate object remains one integral exact factor.  The literal
OR word uses only the terminal factor; the augmentation path is not
concatenated into the word.

#### Proof

The exact ratio formula is
\[
\frac{W}{N_q}
=\prod_{j=1}^q\frac{m+1+j}{m+1-j}.
\]
For \(q\le A\sqrt m+1\) and all sufficiently large \(m\),
\[
\log\frac{W}{N_q}
\le
\sum_{j=1}^q\frac{2j}{m+1-j}
\le
\frac{q(q+1)}{m+1-q}
<3(A+2)^2.
\]
Thus \(1\le c_q\le M_A\).  Each \(O_q(F)\) is an integer, so
\[
J_A(F)\in\Lambda_A^{-1}\mathbb Z_{\ge0}.
\tag{1.7}
\]
Also \(O_q(F)\le W\): compare the load with any balanced nonnegative quota
of the same total mass; its total positive surplus cannot exceed the total
load \(W\).  Hence
\[
0\le J_A(F)\le WH_A.
\tag{1.8}
\]
Every strict descent is at least \(1/\Lambda_A\), so after at most
\(\Lambda_AWH_A\) moves it stops at a local minimum.  The middle equations
remain \(A_mx=\mathbf1\); nonnegativity therefore makes every intermediate
\(x\) a \(0/1\) exact-factor indicator.

Under (1.3), the terminal factor has \(J_A=o(W)\) for every fixed \(A\).
To make the diagonal quantifiers explicit, for every integer \(j\ge1\)
choose \(m_j\) increasing so that for all \(m\ge m_j\),
\[
\frac{L_{j,P}(m)}W\le\frac1j,
\]
and enlarge \(m_j\) so that \(m_j\ge j^7\) and all fixed-\(j\) transfer
estimates hold.  Put
\[
A(m)=\max\{j:m_j\le m\}.
\]
Then \(A(m)\to\infty\), \(A(m)\le m^{1/7}=o(m^{1/6})\), and
\[
H=\lceil A(m)\sqrt m\rceil=o(m^{2/3}),
\qquad
\frac{J_H}{W}\le\frac1{A(m)}\to0.
\]
Integer \(A\) suffices because the controlled windows are nested.
The audited literal wreath construction gives
\[
|\mathcal W_{\rm OR}|
\le
W+O(HW/m)+2J_H+\operatorname{Tail}(m,H).
\tag{1.9}
\]
Here \(HW/m=o(W)\), and the proved symmetric-chain tail estimate gives
\(\operatorname{Tail}(m,H)=o(W)\) because
\(H/\sqrt m\to\infty\) and \(H=o(m)\).  Thus (1.9) is \(W+o(W)\) in odd
dimension.  The standard trimmed one-bit lift gives the same leading
constant in even dimension. \(\square\)

### Theorem 1.2 — sharpness of the absolute threshold

Suppose every factor which is not globally \(J_A\)-optimal admits an
improving move in the same library \(\mathscr T_{A,P}(m)\).  Then
\[
\boxed{L_{A,P}(m)=J_A^\star.}
\tag{1.10}
\]
For the unrestricted full decorated Graver move library, with no degree
cutoff, the analogous equality
\[
L_{A,\mathrm{Gr}}(m)=J_A^\star
\tag{1.10a}
\]
holds unconditionally.

#### Proof

Under the hypothesis, every \(P_A\)-local minimum is global.  Conversely a
global minimum has no strictly decreasing move.  Thus the two sets coincide
and their common objective value is \(J_A^\star\).

For the full decorated Graver library, take optimal auxiliary variables over
the current factor and over a global optimizer.  A conformal Graver
decomposition of their difference has an improving summand whenever the
current objective is larger.  This is the established exact-overload
Graver descent theorem, so the hypothesis holds. \(\square\)

Therefore a polynomial support theorem plus relative descent supplies no
absolute information:
\[
\boxed{
\text{it composes to constant one only after one proves }
J_A^\star=o(W).}
\tag{1.11}
\]
If one instead insists on literally concatenating the augmentation path,
one needs the separate estimate
\(\sum_t\operatorname{splice\_toll}(g_t)=o(W)\).  A per-move support bound
does not imply that estimate.  The standard MWB transfer avoids this issue
by using only the terminal factor.

## 2. An exponential primitive circuit in the actual decorated wreath matrix

Let \(F_m\) be the canonical MSW exact factor and let
\(\tau=(2\ 3)\).  We use the established, independently audited MSW
ownership-component hierarchy.  Its unique top component
\(K_{\rm top}\) has the two sides
\[
K^-\subseteq F_m,\qquad
K^+\subseteq\tau F_m,
\]
of common size
\[
s_m=\operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1}.
\tag{2.1}
\]
The component ownership graph on \(K^-\dot\cup K^+\) is connected.
Switch only this component and put
\[
F'_m=(F_m\setminus K^-)\cup K^+,
\qquad
g_m=\mathbf1_{K^+}-\mathbf1_{K^-}.
\tag{2.2}
\]
Then \(F'_m\) is an exact factor with common completion
\(F_m\setminus K^-\).

### Theorem 2.1 — exact factor-scale circuit

For every \(m\ge4\),
\[
\ker_{\mathbb Z}
\left(A_m\big|_{K^-\cup K^+}\right)
=\mathbb Zg_m.
\tag{2.3}
\]
Hence \(g_m\) is a primitive linear circuit and a Graver element of
\(A_m\).  Its degree satisfies
\[
\boxed{
\frac{s_m}{\operatorname{Cat}_m}
=
\frac{(m+1)(5m-6)}
{4(2m-3)(2m-1)}
=
\frac5{16}
+\frac{36m-39}{16(2m-3)(2m-1)}
>\frac5{16}.}
\tag{2.4}
\]
In particular,
\[
\boxed{
s_m>
\frac{5\cdot4^m}{16(2m+1)(m+1)}.}
\tag{2.5}
\]

#### Proof

Restrict a kernel vector \(z\) to the component columns.  Every middle set
owned by this component is one edge \(uv\) of the ownership graph, with
\(u\in K^-\), \(v\in K^+\).  Its row equation is
\[
z_u+z_v=0.
\]
Connectedness propagates one value \(-a\) over \(K^-\) and the opposite
value \(a\) over \(K^+\).  Thus \(z=ag_m\).  Over the integers the
primitive generator is \(g_m\), whose nonzero coefficients are
\(\pm1\).  This proves (2.3) and the circuit assertion.

The Catalan ratios are
\[
\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_m}
=\frac{m+1}{2(2m-1)}
\]
and
\[
\frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
=\frac{m(m+1)}{4(2m-3)(2m-1)}.
\]
Their sum is (2.4).  Finally, the central binomial coefficient is at least
the average binomial coefficient:
\[
\binom{2m}{m}\ge\frac{4^m}{2m+1}.
\]
Divide by \(m+1\) and use (2.4) to obtain (2.5). \(\square\)

### Theorem 2.2 — the circuit survives both decorated lifts

Let
\[
B_H=(A_{m-1},\ldots,A_{m-H}),\qquad
1\le H\le m-2,
\]
and define the histogram lift
\[
\widehat A_{m,H}
=
\begin{pmatrix}
A_m&0\\
B_H&-I
\end{pmatrix}.
\tag{2.6}
\]
Then
\[
\boxed{\widehat g_m=(g_m,B_Hg_m)}
\tag{2.7}
\]
is a primitive circuit of \(\widehat A_{m,H}\), applicable from the lift
of \(F_m\) to the lift of \(F'_m\).

The same holds for the full mobile repair equality matrix.  With variables
\((x,h,s,p,d)\) and homogeneous rows
\[
A_mx,\qquad
h_q+s_q,\qquad
\mathbf1^Th_q,\qquad
B_qx-h_q-p_q+d_q,
\tag{2.8}
\]
the vector
\[
\boxed{
\Gamma_m=
\bigl(g_m,0,0,(B_Hg_m)^+,(B_Hg_m)^-\bigr)}
\tag{2.9}
\]
is a primitive circuit and hence a Graver element.  Here
\(v^+=\max(v,0)\), \(v^-=\max(-v,0)\), so \(v=v^+-v^-\).

#### Proof

If \((z,v)\) is a kernel vector of (2.6) supported inside
\(\operatorname{supp}\widehat g_m\), then \(A_mz=0\).  Theorem 2.1 gives
\(z=ag_m\), and the lower rows force
\[
v=B_Hz=aB_Hg_m.
\]
Every nonzero scalar uses the full support, and the \(\pm1\) entries of
\(g_m\) make the circuit primitive.

For (2.9), a supported kernel vector has zero \(h,s\) coordinates.  Its
\(x\)-part is \(ag_m\).  On a coordinate where
\((B_Hg_m)_j>0\), the \(d\)-coordinate is unavailable and the row forces
\(p_j=a(B_Hg_m)_j\).  Where \((B_Hg_m)_j<0\), it forces
\(d_j=-a(B_Hg_m)_j\).  The positive and negative supports are disjoint.
Thus every supported kernel vector is \(a\Gamma_m\); primitivity again
comes from the \(x\)-coordinates. \(\square\)

The orientation in (2.9) is feasibility-applicable from any nonnegative
mobile extension over \(F_m\): it switches to \(F'_m\) while increasing
the displayed \(p,d\) coordinates.  It generally does not carry an
auxiliary-optimal extension to another auxiliary-optimal extension and need
not decrease the standard mobile repair cost.

Consequently the actual decorated wreath Graver basis contains circuits of
degree \(>m^C\) for every fixed \(C\) and all sufficiently large \(m\).
In fact no \(e^{o(m)}\) bound is possible.

## 3. Normal and hole-free, but with an indispensable macro move

The preceding circuit is not created by a semigroup hole.

Let \(G\) be its connected bipartite ownership graph and let \(Q_G\) be
the edge-by-vertex unsigned incidence matrix:
\[
(Q_Ga)_{uv}=a_u+a_v.
\]

### Theorem 3.1 — exact normality of the top-component semigroup

\[
\boxed{
Q_G\mathbb Z_{\ge0}^{V(G)}
=
\operatorname{cone}(Q_G)\cap
\operatorname{gp}(Q_G).}
\tag{3.1}
\]
Nevertheless, for the all-ones edge target
\[
b_G=\mathbf1_{E(G)},
\]
the nonnegative integral fibre consists of exactly two points,
\[
\boxed{
\{a\ge0:Q_Ga=b_G\}
=\{\mathbf1_{K^-},\mathbf1_{K^+}\}.}
\tag{3.2}
\]
Thus the toric ideal is principal on this component and every Markov basis
connecting (3.2) must contain \(\pm g_m\), of degree \(s_m\).

#### Proof

Connected bipartiteness gives
\[
\ker_{\mathbb R}Q_G=\mathbb Rg_m,
\qquad
\ker_{\mathbb Z}Q_G=\mathbb Zg_m.
\tag{3.3}
\]
Take
\[
y=Q_Ga^0=Q_Ga
\]
with \(a^0\in\mathbb Z^{V(G)}\) and \(a\in\mathbb R_{\ge0}^{V(G)}\).
Then \(a=a^0+tg_m\).  Orient \(g_m=+1\) on \(K^+\) and \(-1\) on
\(K^-\).  Nonnegativity is the interval
\[
\max_{v\in K^+}(-a_v^0)
\le t\le
\min_{v\in K^-}a_v^0.
\tag{3.4}
\]
Both endpoints are integers.  Since the interval is nonempty, it contains
an integer \(k\), and \(a^0+kg_m\) is a nonnegative integral preimage of
\(y\).  This proves normality.

For (3.2), each edge equation is \(a_u+a_v=1\).  Nonnegative integrality
makes the endpoints complementary \(0/1\) values; connectedness propagates
one of the two bipartition assignments. \(\square\)

Adjoining the forced common completion \(F_m\setminus K^-\) takes a direct
product with a free semigroup.  Hence the column semigroup restricted to
the two-factor support \(\mathcal U\) is also normal, its exact-factor
fibre is \(\{F_m,F'_m\}\), and its unique restricted transition remains
the degree-\(s_m\) circuit.

This proves an exact logical separation:
\[
\boxed{
\text{normality and complete hole elimination do not bound Graver degree}.}
\tag{3.5}
\]

## 4. A genuine monotone augmentation trap on the wreath fibre

Put
\[
\mathcal U=F_m\cup F'_m,
\qquad
s=s_m,
\]
and define the nonnegative integral linear objective
\[
\mathcal L_m(X)
=
s\,|X\setminus\mathcal U|
+|X\cap K^-|
\tag{4.1}
\]
on exact factors \(X\).

### Theorem 4.1 — the minimum improving degree is exactly \(s_m\)

\[
\mathcal L_m(F_m)=s,\qquad
\mathcal L_m(F'_m)=0.
\tag{4.2}
\]
If
\[
d(F_m,X)=|F_m\setminus X|=|X\setminus F_m|<s,
\]
then
\[
\boxed{\mathcal L_m(X)\ge\mathcal L_m(F_m),}
\tag{4.3}
\]
with strict inequality whenever \(X\not\subseteq\mathcal U\).
Consequently:

1. no trade of degree \(<s_m\) improves \(\mathcal L_m\) at \(F_m\);
2. the top circuit \(g_m\), of degree \(s_m\), does improve it;
3. no nonincreasing path whose moves all have degree \(<s_m\) can even
   leave \(F_m\).

#### Proof

Put
\[
a=|K^-\setminus X|,
\qquad
t=|X\setminus\mathcal U|.
\]
Then
\[
\mathcal L_m(X)=st+s-a,
\qquad
\mathcal L_m(X)-\mathcal L_m(F_m)=st-a.
\tag{4.4}
\]
If \(t\ge1\), then \(a\le d(F_m,X)<s\), so
\[
st-a\ge s-a>0.
\]
If \(t=0\), then \(X\) lies in the two-point support face of Section 3.
Thus \(X\in\{F_m,F'_m\}\); the inequality \(d(F_m,X)<s\) excludes
\(F'_m\), so \(X=F_m\).  This proves (4.3).  The trade \(g_m\) reaches
\(F'_m\) and proves exactness of the threshold. \(\square\)

Extend \(\mathcal L_m\) to either decorated equality fibre by assigning
zero cost to all auxiliary variables.  Then every feasible extension over
\(F_m\) is a nonglobal local minimum for every factor-changing move of
degree \(<s_m\), while an extension over \(F'_m\) has cost zero.
The coefficient \(s_m\) has only \(O(m)\) bits.

Thus there is no generic polynomial-support monotone Graver augmentation
theorem for separable linear objectives on the decorated wreath matrix.
The exact scope is important: \(\mathcal L_m\) breaks \(S_n\)-symmetry.  An
\(S_n\)-invariant linear cost on wreath coordinates is constant, and
Theorem 4.1 does not construct a local minimum for the rank-symmetric MWB
overload.

## 5. Constant circuits and saturation two can still have linear repair

The preceding theorem is wreath-specific.  The next analytic countermodel
shows that the abstract algebraic package requested in this lane would be
insufficient even if polynomial circuit control happened to hold.

For one block, let \(A\) be the vertex-edge incidence matrix of \(K_4\).
Its exact factors are the three perfect matchings
\[
P=\{12,34\},\qquad
Q=\{13,24\},\qquad
R=\{14,23\}.
\tag{5.1}
\]
Introduce three lower targets \(\alpha,\beta,\gamma\).  Give the two edges
of \(P\) lower support \(\{\alpha,\beta\}\), the two edges of \(Q\)
support \(\{\beta,\gamma\}\), and the two edges of \(R\) support
\(\{\alpha,\gamma\}\).  Every column of both \(A\) and \(B\) has two
ones.  The matching profiles are
\[
BP=(2,2,0),\qquad
BQ=(0,2,2),\qquad
BR=(2,0,2).
\tag{5.2}
\]
Take \(K\) disjoint copies.  An exact factor chooses one matching in each
block.  Its lower mass is
\[
W_0=4K
\]
on \(N=3K\) targets, so the floor quota is \(c=1\) and the number of high
quotas is \(\rho=K\).

### Theorem 5.1 — exact mobile hole and linear absolute repair

For the mobile zero-overload equations
\[
Ax=t\mathbf1,\qquad
Bx-h=t\mathbf1,\qquad
h+s=t\mathbf1,
\tag{5.3}
\]
the degree-one target is a genuine hole and
\[
\boxed{
\{t\ge0:tb\text{ is in the semigroup}\}
=\{0,2,3,4,\ldots\}.}
\tag{5.4}
\]
Thus the saturation index of this hole and the balanced-ray conductor are
both \(2\); no assertion is made about the conductor of the entire affine
semigroup.

Nevertheless every degree-one exact factor \(F\) has
\[
\boxed{
O(F)=K=\frac{W_0}{4},}
\tag{5.5}
\]
and the half floor energy also equals \(K\).  The degree-two balanced
witness is already a sum of two exact factors, but every constituent in
every exact-factor decomposition still has overload \(K\).

#### Proof

Blockwise cone membership at degree one is witnessed by
\[
x=\frac12(P+Q),\qquad
h=(0,1,0),\qquad
s=(1,0,1).
\tag{5.6}
\]
An integer-lattice witness is
\[
x=P,\qquad
h=(1,1,-1),\qquad
s=(0,0,2).
\tag{5.7}
\]
No nonnegative integral degree-one witness exists: \(Ax=\mathbf1\) chooses
one of \(P,Q,R\), every profile in (5.2) has a zero coordinate, while
\(Bx=\mathbf1+h\) with \(h,s\ge0\) forces every load into
\(\{1,2\}\).  Thus \(b\) is in cone intersect lattice but outside the
semigroup.

At degree two, use
\[
x=P+Q,\quad
Bx=(2,4,2),\quad
h=(0,2,0),\quad
s=(2,0,2).
\tag{5.8}
\]
At degree three, use
\[
x=P+Q+R,\quad
Bx=(4,4,4),\quad
h=(1,1,1),\quad
s=(2,2,2).
\tag{5.9}
\]
Adding the degree-two and degree-three solutions produces every degree
\(t\ge2\), proving (5.4).

Every exact factor has \(2K\) load-two targets and \(K\) load-zero
targets.  A balanced quota has only \(K\) high tokens.  Place them on
\(K\) of the double targets; the other \(K\) double targets each contribute
one unit of overload.  This is optimal, so (5.5) holds.  The floor energy
\(\frac12(z-1)(z-2)\) charges exactly the \(K\) zero targets.

The degree-two witness \(P+Q\) is the union of two exact factors.  In one
block its support is a \(4\)-cycle, whose only perfect matchings are
\(P,Q\).  Any global coloring may swap the two colors from block to block,
but each constituent remains an arbitrary exact factor and therefore has
overload \(K\). \(\square\)

### Theorem 5.2 — exact constant Graver basis

For one block, every middle-kernel vector is
\[
p(a,b)=aP+bQ-(a+b)R,
\tag{5.10}
\]
and
\[
Bp(a,b)=(-2b,\,2(a+b),\,-2a).
\tag{5.11}
\]
For the zero-overload mobile matrix
\[
\mathcal M=
\begin{pmatrix}
A&0&0\\
B&-I&0\\
0&I&I
\end{pmatrix},
\tag{5.12}
\]
the Graver basis consists exactly of the six signed lifts of
\[
P-Q,\qquad P-R,\qquad Q-R.
\tag{5.13}
\]
Every such element has projected degree \(2\), coordinate support \(8\),
and \(\ell_1\)-norm \(12\).  The same bounds hold for every \(K\).

#### Proof

Every kernel vector of (5.12) is
\[
\bigl(p(a,b),Bp(a,b),-Bp(a,b)\bigr).
\]
Its common orthant fan in the \((a,b)\)-plane is cut by
\[
a=0,\qquad b=0,\qquad a+b=0.
\]
The six resulting two-dimensional cones are unimodular.  Their primitive
Hilbert rays are
\[
\pm(1,0),\quad \pm(0,1),\quad \pm(1,-1),
\]
which give (5.13).  Direct sums have Graver bases supported in one block,
because a vector nonzero in two blocks conformally decomposes into its block
parts. \(\square\)

### Theorem 5.3 — the deletion/survival-packet bypass is also linear

Even after optimizing over the factor and all balanced high quotas, the
minimum fractional and integral number of deleted factor columns needed to
leave a quota-safe core is
\[
\boxed{
\vartheta_K^\star=\tau_K^\star
=\left\lceil\frac K2\right\rceil
=\left(\frac18+o(1)\right)W_0.}
\tag{5.14}
\]

#### Proof

In each block, the two selected matching edges have the same two lower
targets.  The block is quota-safe without deletion only if both of those
targets receive high quotas.  There are only \(K\) high tokens, so at most
\(\lfloor K/2\rfloor\) blocks can be protected this way.  Every remaining
block has one common two-owner survival packet and needs fractional as well
as integral cover mass one.  These packets are disjoint across blocks.
This gives the lower bound \(\lceil K/2\rceil\).

For equality, give both high tokens to \(\lfloor K/2\rfloor\) blocks and
delete one selected edge from each remaining block.  When \(K\) is odd,
place the one leftover high token arbitrarily on one of those remaining
blocks.  The resulting core is quota-safe. \(\square\)

This countermodel is not a wreath construction.  Its role is exact:
\[
\boxed{
\begin{gathered}
\text{binary equal-column incidence, saturation two,}\\
\text{factorability of the saturated cover, and constant Graver support}\\
\text{can coexist with linear optimal repair.}
\end{gathered}}
\tag{5.15}
\]
Any positive theorem must use additional cyclic-wreath geometry.

## 6. Exact high-multiplicity repair criterion for the wreath problem

For \(q\le H\), put
\[
V_q=\binom{[n]}{m-q},\qquad
N_q=|V_q|,\qquad
W=c_qN_q+\rho_q,
\qquad
d_q=\frac{n!}{2N_q}.
\]
Let \(u=\mathbf1_{\Omega_m}\), let
\[
d_0=\frac{m!(m+1)!}{2},
\qquad
\eta_q=d_q-c_qd_0
=d_0\frac{\rho_q}{N_q},
\]
and put
\[
U^{\mathrm{dec}}_{m,H}
=2W\left(u,(\eta_q\mathbf1_{V_q})_{q\le H}\right).
\tag{6.1}
\]
This is the universal exactly balanced decorated orbit multicover.  Every
factorization contains
\[
T=n!=2Wd_0
\tag{6.2}
\]
degree-one factors.

For a factor \(F\) and high families \(H_q\), define the constituent repair
\[
\mathcal E_H(F,H)
=
\sum_{q\le H}\frac1{c_q}
\sum_{S\in V_q}
\left(B_q\mathbf1_F-c_q\mathbf1-\mathbf1_{H_q}\right)_+(S).
\tag{6.3}
\]
Then
\[
\min_{\substack{H_q\subseteq V_q\\|H_q|=\rho_q\ (q\le H)}}
\mathcal E_H(F,H)=J_H(F).
\tag{6.3a}
\]

### Theorem 6.1 — exact colored-IDP no-gain identity

\[
\boxed{
\min_{\substack{
U^{\mathrm{dec}}_{m,H}
=\sum_{i=1}^{n!}
(\mathbf1_{F_i},(\mathbf1_{H_{i,q}})_q)\\
F_i\ {\rm exact},\ |H_{i,q}|=\rho_q}}
\frac1{n!}\sum_{i=1}^{n!}
\mathcal E_H(F_i,H_i)
=J_H^\star.}
\tag{6.4}
\]
The analogous minimum of the largest constituent repair is also
\(J_H^\star\).

#### Proof

Every constituent has repair at least \(J_H^\star\), proving the lower
bound.  Choose a minimizing decorated pair \((F^\star,H^\star)\) and take
all of its \(n!\) coordinate relabelings.  Transitivity gives
\[
\sum_{\sigma\in S_n}\mathbf1_{\sigma F^\star}=2Wu
\]
and
\[
\sum_{\sigma\in S_n}\mathbf1_{\sigma H_q^\star}
=\frac{n!\rho_q}{N_q}\mathbf1
=2W\eta_q\mathbf1.
\]
Thus the orbit is a decomposition of (6.1), and every constituent has the
same repair \(J_H^\star\). \(\square\)

There is always an uncolored zero-repair representation of the
degree-\(n!\) mobile target:
\[
x=2Wu,\qquad
h_q=2W\eta_q\mathbf1,\qquad
s_q=n!\mathbf1-h_q.
\tag{6.5}
\]
But (6.5) admits a color-preserving decomposition into degree-one
zero-repair states if and only if a perfectly balanced exact factor exists.
More generally, a colored decomposition of any multiplicity \(t\) with
total repair \(R_t\) yields one factor of repair at most \(R_t/t\).
Therefore the condition
\[
\boxed{R_t=o(tW).}
\tag{6.6}
\]
is sufficient for an arbitrary colored decomposition to yield MWB.  It is
not necessary for one fixed decomposition merely to contain a good
constituent.  After minimizing total constituent repair, however, the
criterion is exact for the universal orbit target: (6.4) gives
\[
\min R_{n!}=n!J_H^\star,
\]
so (6.6) is equivalent there, with constant exactly one, to
\(J_H^\star=o(W)\).

Thus cone membership, a finite or polynomial saturation index, normality of
a multiple, and uncolored IDP do not bypass a degree-one hole.  The needed
statement is color-separable constituent repair, which is already the
one-factor theorem in averaged form.

### Unproved imported illustration 6.2 — aggregate cancellation may hide linear defect

The following asymptotic estimate for the canonical MSW factor is quoted in
one prior attack report, but no proof or independent audit of it was located
in the present workspace:
\[
M_1(F_m^{\mathrm{MSW}})
\ge(1/16-o(1))W.
\tag{6.7}
\]
Accordingly, **(6.7) is an unproved input here and is not used in any
theorem or in the lane closure.**  Conditional on (6.7), since \(c_1=1\)
and \(M_1(F)\le O_1(F)\), one obtains
\[
J_H(F_m^{\mathrm{MSW}})
\ge(1/16-o(1))W
\qquad(H\ge1).
\tag{6.8}
\]
Every relabeling would then have the same defect, while its full orbit has
exactly zero aggregate decorated discrepancy by (6.1).  Thus (6.7), if
proved, would give an actual perfectly balanced wreath multicover with a
natural exact-factor coloring in which every constituent has linear defect.

This conditional illustration would not rule out a different good
refactorization; the proved Theorem 6.1 says that optimizing all
refactorizations is exactly the original value \(J_H^\star\).

## 7. Final implication and lane closure

The full decorated Graver basis of the actual wreath matrix has no
polynomial-in-\(m\) support bound:

\[
\boxed{
\text{it contains an applicable decorated circuit of degree }
>\frac5{16}\operatorname{Cat}_m.}
\]
Its middle-incidence restriction is indispensable on the normal
two-endpoint support configuration.  Indispensability in every Markov basis
of the unrestricted full wreath matrix is not asserted.

The requested semigroup-hole bypass is not an algebraic consequence of
normality, saturation, IDP, or bounded Graver support:

* the actual macro circuit already lives in a normal, hole-free wreath
  subsemigroup;
* the \(K_4\) family has saturation two and constant Graver support but
  linear optimal repair;
* on the actual universal orbit, the optimum colored repair is exactly
  \(J_H^\star\).

Therefore the generic algebraic AC route cannot by itself prove the
constant-one theorem.  A surviving augmentation theorem must exploit the
\(S_n\)-invariant wreath overload objective, allow objective-specific move
or path geometry outside the restricted two-point face, and prove the
absolute bound
\[
L_{A,P}(m)=o(W)
\]
for every fixed \(A\).  By Theorem 1.1 that stronger bound would prove
constant one and always implies \(J_A^\star=o(W)\).  It is equivalent to
the latter estimate only under the additional relative
\(\mathscr T_{A,P}\)-augmentation hypothesis of Theorem 1.2; in no case is
it a consequence of Graver support control or semigroup normality alone.

No claim is made against MWB, labelled synchronization, or the
contiguous-OR conjecture itself.  What is closed is precisely the proposed
generic polynomial-Graver/semigroup-hole route.

## 8. Independent audit

A fresh adversarial audit checked the descent-grid constant and diagonal
quantifiers in Theorem 1.1; the rank-one kernel, primitive decorated lifts,
and exact \(5/16\) ratio in Section 2; the restricted-support scope of the
Markov-basis claim; the exact improving-degree threshold in Section 4; all
\(K_4\) cone, lattice, hole, Graver, overload, and deletion calculations;
and the \(2W\), \(n!\), and \(\eta_q\) coefficients in Theorem 6.1.  Its final
verdict was **pass** with no remaining false theorem, constant, or
quantifier.  The audit identified (6.7) as lacking a proof in the available
reports; it is therefore explicitly marked unproved, conditional, and
unused above.
