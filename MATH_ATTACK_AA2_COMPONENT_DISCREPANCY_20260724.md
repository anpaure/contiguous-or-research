# Second-wave AA: simultaneous component discrepancy and exact-factor SDP rounding

## 0. Verdict

Fix a window constant \(A_0>0\) and put

\[
H=H_{A_0}:=\lceil A_0\sqrt m\rceil .
\]

Here \(n=2m+1\),

\[
\mathsf W=\binom nm,
\qquad
N_q=\binom n{m-q},
\qquad
c_q=\left\lfloor\frac{\mathsf W}{N_q}\right\rfloor,
\qquad
\operatorname{Cat}_m=\frac{\mathsf W}{n}.
\]

All asymptotic statements have \(A_0\) fixed and \(m\to\infty\); in
particular the window means \(1\le q\le H\).

All component effects below are stacked over the **entire** weighted window
\(q\le H\), and one sign is used for each genuine ownership component at
every depth.  Thus every sign vector occurring in a proof selects complete
component sides and is one literal integral exact factor.  No rankwise
fractional factor is ever used.

The main conclusions are as follows.

1. Correlated fair component signs strictly beat independent fair component
   variance if and only if the aggregate off-diagonal component Gram matrix
   is nonzero.  A diagonal-majorant hyperplane law gives the following
   explicit theorem with audited constants when \(W_0\ne0\):

   \[
   V-\beta\ge
   \frac4{\pi\lambda_{\max}(W_0)}
       \sum_{K<L}w_{KL}^{\,2}
   \ge
   \frac{2\sqrt2}{\pi}
       \left(\sum_{K<L}w_{KL}^{\,2}\right)^{1/2}.
   \tag{0.1}
   \]

   Here \(W_0=(w_{KL})\) is the symmetric zero-diagonal Gram matrix and the
   last norm is over unordered pairs.  The coefficient \(2\sqrt2/\pi\) is
   for residual improvement; the corresponding cut coefficient is
   \(1/(\sqrt2\pi)\).  This improves the first-wave residual coefficient
   \(1/9\) and cut coefficient \(1/36\).

2. The discrete floors can be retained exactly.  If \(\Pi\) is the parity
   floor, \(B\) the sum of independent rowwise minima, \(\gamma\) a
   floor-aware SDP value, and \(\beta\) the true common-sign value, then

   \[
   \Pi\le B\le\gamma\le\beta\le\min\{A,V\}.
   \tag{0.2}
   \]

   Hence the exact cut has a four-level decomposition: parity ideal gain,
   local amplitude loss, fractional synchronization loss, and rounding
   loss.

3. There are three complementary exact-factor rounding theorems.

   * Isotropic conditional-mean rounding transfers a fraction
     \(\rho^{-2}\) of a floor-aware vector-SDP gain, where \(\rho\) is an
     intrinsic slab/coherence parameter.  Rank \(r\) always gives
     \(\rho^2\le r\), and a basis rotation gives
     \(\rho^2\le2\log(4Nr)\).
   * Diluted hyperplane rounding converts **every strict** vector-SDP gain
     below \(V\) into a strict integral gain, with an explicit
     \(D^{3/2}/L^{1/2}\) bound when the gain is small.
   * A zonotope/partial-coloring theorem works directly above \(B\).  A
     synchronization SDP on the signed row-component incidence graph gives
     \(\beta-B\le4\sqrt{T\delta_{\rm sync}}\).

4. These results do not close the conjecture.  Aggregate orthogonal
   Hadamard blocks have \(\beta=V\) while \(B=\Pi\), and a two-depth block
   has perfect balancing at each depth separately but \(\beta=V\) after
   the same component signs are required across both depths.  These are
   abstract integral, nonnegative, pair-orbit-feasible arrays, not proved
   realizable as genuine wreath ownership components.  They show exactly
   which new genuine-chronology statement is still required.

The remainder states and proves all constants and records the exact scope.

## 1. One simultaneous stacked component system

Let \(F\) be an exact factor and fix a coordinate transposition \(\tau\).
For every \(q\le H\), every unordered moved target orbit

\[
p=(q,\{S,\tau S\}),
\]

and every genuine ownership component \(K\) of the overlay between \(F\)
and \(\tau F\), orient the orbit and write

\[
z_{pK}=a_{K,q}(S)-a_{K,q}(\tau S)\in\mathbb Z,
\qquad
\alpha_p=\frac2{c_q}.
\tag{1.1}
\]

Fixed targets make no contribution.  Define the stacked component vector

\[
d_K=(\sqrt{\alpha_p}\,z_{pK})_p
\tag{1.2}
\]

in the Euclidean direct sum over every row at every \(q\le H\).  If
\(\varepsilon_K=+1\) chooses the \(F\)-side of component \(K\) and
\(\varepsilon_K=-1\) chooses the \(\tau F\)-side, put

\[
R(\varepsilon)
=\left\|\sum_K\varepsilon_Kd_K\right\|^2
=\sum_p\alpha_p
  \left(\sum_K\varepsilon_Kz_{pK}\right)^2.
\tag{1.3}
\]

The same \(\varepsilon_K\) appears in every depth.  The genuine ownership
component theorem says that every \(\varepsilon\in\{\pm1\}^{\mathscr K}\)
produces an integral exact factor \(F_\varepsilon\).

Let

\[
G_{KL}=\langle d_K,d_L\rangle,
\qquad
w_{KL}=G_{KL}\quad(K\ne L),
\tag{1.4}
\]

\[
A=R({\bf1})=\left\|\sum_Kd_K\right\|^2,
\qquad
V=\operatorname{tr}G=\sum_K\|d_K\|^2,
\tag{1.5}
\]

and

\[
\beta=\min_{\varepsilon\in\{\pm1\}^{\mathscr K}}R(\varepsilon).
\tag{1.6}
\]

Thus

\[
R(\varepsilon)=V+2\sum_{K<L}w_{KL}\varepsilon_K\varepsilon_L,
\qquad
\mathbb E_{\rm fair}R=V.
\tag{1.7}
\]

Here and below every pair sum is over unordered pairs \(K<L\).  The matrix
Frobenius norm satisfies

\[
\|G-\operatorname{diag}G\|_F
=\sqrt{2\sum_{K<L}w_{KL}^2}.
\tag{1.8}
\]

### 1.1 Exact energy interface

For the full floor energy

\[
\mathcal Q_{A_0}(F)
=\sum_{q\le H}\frac1{c_q}
  \sum_{S}
  (\mu_{F,q}(S)-c_q)(\mu_{F,q}(S)-c_q-1),
\tag{1.9}
\]

the transposition-equivariant pair calculation gives, for every signing,

\[
\boxed{
\mathcal Q_{A_0}(F_\varepsilon)-\mathcal Q_{A_0}(F)
=\frac{R(\varepsilon)-A}{4}.}
\tag{1.10}
\]

Indeed, on a moved pair the pair sum is invariant and only the square of
the pair difference changes.  The two target coordinates account for the
factor \(2/c_q\) in (1.1), while the quadratic expansion of (1.9) supplies
the factor (1/4).

Consequently the best genuine component cut is

\[
\boxed{C^*=\frac{A-\beta}{4}.}
\tag{1.11}
\]

For a direct overlay between \(F\) and a general relabelled factor
\(\sigma F\), the same stacked theory applies with ordinary target rows and
weight \(1/c_q\).  In that case the always-valid statement is the antipodal
identity

\[
\frac{\mathcal Q_{A_0}(F_\varepsilon)
      +\mathcal Q_{A_0}(F_{-\varepsilon})}{2}
=\mathcal Q_{A_0}(F)+\frac{R(\varepsilon)-A}{4},
\tag{1.12}
\]

so the better antipode has the decrease asserted by (1.11).  Only the
transposition case makes (1.10) an individual-child identity automatically.

## 2. The parity, row, SDP, and integral floors

For each row put

\[
\pi_p=\left(\sum_Kz_{pK}\right)\bmod2\in\{0,1\},
\tag{2.1}
\]

\[
b_p=\min_{\eta\in\{\pm1\}^{\mathscr K}}
       \left(\sum_K\eta_Kz_{pK}\right)^2,
\tag{2.2}
\]

and

\[
\Pi=\sum_p\alpha_p\pi_p,
\qquad
B=\sum_p\alpha_pb_p.
\tag{2.3}
\]

Because every sign is \(1\pmod2\), every signed row sum has the same parity
as \(\sum_Kz_{pK}\).  Therefore

\[
\Pi\le B\le\beta\le\min\{A,V\}.
\tag{2.4}
\]

The bound \(\beta\le A\) uses the all-old signing and \(\beta\le V\) uses
independent fair signs.  The integer quantization is also exact:

* if \(\pi_p=0\), then \(b_p-\pi_p\) and every
  \((z_p\cdot\varepsilon)^2-b_p\) are multiples of \(4\);
* if \(\pi_p=1\), the corresponding differences are multiples of \(8\).

Thus \(B-\Pi\) is **local amplitude locking**, while \(\beta-B\) is the
loss from requiring one common component signing across all rows and all
depths.

### 2.1 A floor-aware SDP

Let \(\mathcal E_B\) be the set of matrices satisfying

\[
X\succeq0,
\qquad X_{KK}=1,
\qquad z_p^TXz_p\ge b_p\quad\hbox{for every }p.
\tag{2.5}
\]

One may strengthen this set by all three-variable cut-metric inequalities,
or by any higher valid cut constraints, without changing the arguments
below.  Define

\[
S(X)=\langle G,X\rangle
=\sum_p\alpha_pz_p^TXz_p,
\qquad
\gamma=\min_{X\in\mathcal E_B}S(X).
\tag{2.6}
\]

Every cut matrix \(\varepsilon\varepsilon^T\) is feasible.  The identity
matrix is feasible because

\[
b_p\le\mathbb E_{\rm fair}(z_p\cdot\varepsilon)^2
=\sum_Kz_{pK}^2.
\tag{2.7}
\]

It follows that

\[
\boxed{\Pi\le B\le\gamma\le\beta\le\min\{A,V\}.}
\tag{2.8}
\]

Combining (1.11) and (2.8) gives the exact four-level decomposition

\[
\boxed{
C^*
=\frac{A-\Pi}{4}
-\frac{B-\Pi}{4}
-\frac{\gamma-B}{4}
-\frac{\beta-\gamma}{4}.}
\tag{2.9}
\]

The first-wave three-floor identity is recovered by combining the last two
terms.  Parity-only SDP constraints are not enough: one row
\(z=2(1,1,-1)\) has \(\Pi=0\), \(B=\beta=4\), and \(V=12\), while three
unit vectors with \(u_1+u_2-u_3=0\) give basic elliptope value \(0\).

## 3. The diagonal-majorant correlated-sign theorem

Write

\[
W_0=G-\operatorname{diag}G.
\tag{3.1}
\]

Thus \((W_0)_{KL}=w_{KL}\) off the diagonal and \(\operatorname{tr}W_0=0\).

### Theorem 3.1 (diagonal-majorant hyperplane rounding)

Let \(\Lambda=\operatorname{diag}(\lambda_K)\) have strictly positive
diagonal and satisfy

\[
\Lambda-W_0\succeq0.
\tag{3.2}
\]

Then there is a fair-marginal correlated distribution on genuine component
signings for which

\[
\mathbb E R(\varepsilon)=V-\Gamma_\Lambda,
\tag{3.3}
\]

where

\[
\boxed{
\Gamma_\Lambda
=\frac4\pi\sum_{K<L}|w_{KL}|
  \arcsin\!\left(
   \frac{|w_{KL}|}{\sqrt{\lambda_K\lambda_L}}
  \right).}
\tag{3.4}
\]

Consequently

\[
\boxed{
\beta-P\le V-P-\Gamma_\Lambda
\quad(P=\Pi\text{ or }B).}
\tag{3.5}
\]

In particular \(\Gamma_\Lambda\le V-B\); this last inequality is not an
extra hypothesis but follows because every sampled signing obeys its row
floors.

#### Proof

Set

\[
X=\Lambda^{-1/2}(\Lambda-W_0)\Lambda^{-1/2}.
\tag{3.6}
\]

Then \(X\succeq0\), \(X_{KK}=1\), and

\[
X_{KL}=-\frac{w_{KL}}{\sqrt{\lambda_K\lambda_L}}.
\tag{3.7}
\]

The \(2\times2\) principal minors imply \(|X_{KL}|\le1\).  Choose unit
vectors \(u_K\) with Gram matrix \(X\), take a standard centered Gaussian
vector \(g\), and define

\[
\varepsilon_K=\operatorname{sgn}\langle g,u_K\rangle.
\tag{3.8}
\]

Every marginal is fair.  The elementary planar-angle identity gives

\[
\mathbb E\varepsilon_K\varepsilon_L
=\frac2\pi\arcsin X_{KL}.
\tag{3.9}
\]

Substitution in (1.7), oddness of \(\arcsin\), and (3.7) give (3.3).
Every realization of (3.8) is a whole-component signing, so it is an exact
factor.  Some realization is no worse than the mean, proving (3.5).
\(\square\)

### Corollary 3.2 (uniform spectral/Frobenius bound)

If \(W_0\ne0\), then

\[
\lambda_+:=\lambda_{\max}(W_0)>0.
\tag{3.10}
\]

Indeed, a nonzero negative-semidefinite matrix with trace zero cannot
exist.  Taking \(\Lambda=\lambda_+I\) is feasible.  Moreover
\(\lambda_+\ge|w_{KL}|\) by testing
\((e_K+\operatorname{sgn}(w_{KL})e_L)/\sqrt2\), and

\[
\lambda_+\le\|W_0\|_F
=\sqrt2\,\sigma,
\qquad
\sigma:=\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
\tag{3.11}
\]

Since \(\arcsin x\ge x\) on \([0,1]\), Theorem 3.1 yields

\[
\boxed{
V-\beta
\ge\frac4{\pi\lambda_+}\sigma^2
\ge\frac{2\sqrt2}{\pi}\sigma.}
\tag{3.12}
\]

Equivalently,

\[
\boxed{
C^*\ge
\max\left\{0,
\frac{A-V}{4}+\frac{\sigma}{\sqrt2\pi}
\right\}.}
\tag{3.13}
\]

The maximum with zero is essential because \(A-V\) can be negative.  At a
component-cut-local factor, \(\beta=A\), so if

\[
W_+=\sum_{w_{KL}>0}w_{KL},
\qquad
W_-=-\sum_{w_{KL}<0}w_{KL},
\tag{3.14}
\]

then \(A=V+2(W_+-W_-)\), and (3.12) forces

\[
\boxed{W_--W_+\ge\frac{\sqrt2}{\pi}\sigma.}
\tag{3.15}
\]

This independently checks every factor of \(2\) and \(\sqrt2\): the
residual coefficient is \(2\sqrt2/\pi\), the cut coefficient is
\(1/(\sqrt2\pi)\), and the cut-local coherence coefficient is
\(\sqrt2/\pi\).

### Corollary 3.3 (signed-degree/sparsity majorant)

After deleting isolated zero rows of \(W_0\), put

\[
\lambda_K=\sum_{L\ne K}|w_{KL}|.
\tag{3.16}
\]

Then

\[
x^T(\Lambda-W_0)x
=\sum_{K<L}|w_{KL}|
  (x_K-\operatorname{sgn}(w_{KL})x_L)^2\ge0,
\tag{3.17}
\]

and hence

\[
\boxed{
V-\beta\ge
\frac4\pi\sum_{K<L}
\frac{w_{KL}^2}{\sqrt{\lambda_K\lambda_L}}.}
\tag{3.18}
\]

This is the natural sparsity-sensitive version.  It still requires an
independent genuine-ownership estimate on the signed degrees before it can
be converted to Catalan error.

### Corollary 3.4 (exact qualitative dichotomy)

\[
\boxed{\beta<V\quad\Longleftrightarrow\quad W_0\ne0.}
\tag{3.19}
\]

The forward obstruction is immediate: if \(W_0=0\), (1.7) is the constant
\(V\) for every signing and every correlated law.  Conversely, Theorem 3.1
is strict when some \(w_{KL}\ne0\).  An even shorter qualitative proof
couples one nonzero pair with product
\(-\operatorname{sgn}(w_{KL})\) and leaves every other sign independent;
the expected residual is \(V-2|w_{KL}|\).

Thus correlated signs answer the fair-variance question completely.  They
do **not** answer descent completely: descent requires \(\beta<A\), not
merely \(\beta<V\).  Gauging an abstract system by a minimizing sign vector
can arrange \(A=\beta<V\), in which case the correlated law merely
rediscovers the current cut minimum.

### Corollary 3.5 (matching followed by spectral block rounding)

Let \(M\) be any matching in the component Gram graph.  On each matched
edge choose fixed internal relative signs that contribute
\(-2|w_{KL}|\), and treat each matched pair and unmatched singleton as one
block \(B\).  If

\[
g_B=\sum_{K\in B}\theta_Kd_K,
\tag{3.20}
\]

then

\[
\sum_B\|g_B\|^2
=V-2\sum_{KL\in M}|w_{KL}|.
\tag{3.21}
\]

Define the off-diagonal block Gram matrix by

\[
W_{\rm block}
=G_{\rm block}-\operatorname{diag}G_{\rm block}.
\]

For any strictly positive block diagonal majorant
\(\Lambda_{\rm block}\) with
\(\Lambda_{\rm block}-W_{\rm block}\succeq0\), let
\(\Gamma_{\rm block}\) denote (3.4) for this block system.  If
\(W_{\rm block}=0\), set \(\Gamma_{\rm block}=0\).  Theorem 3.1 then gives

\[
\boxed{
\beta\le
V-2\sum_{KL\in M}|w_{KL}|-\Gamma_{\rm block}.}
\tag{3.22}
\]

This genuinely combines, rather than merely maximizes, the first-wave
matching gain and the new spectral gain.  Every block signing lifts to one
whole-component signing and remains an exact factor.

## 4. General floor-aware SDP rounding

The anti-Gram construction of Section 3 does not need its correlation
matrix to satisfy the floor-aware SDP constraints: its output is already a
distribution on true cuts.  This section instead starts from an arbitrary
floor-feasible SDP point and quantifies its rounding loss above \(B\).

### Theorem 4.1 (master angular formula)

For every correlation matrix \(X=(X_{KL})\), Gaussian hyperplane rounding
produces fair whole-component signs satisfying

\[
\boxed{
\mathbb E R
=V+\frac4\pi\sum_{K<L}w_{KL}\arcsin X_{KL}.}
\tag{4.1}
\]

In particular, the right side is an upper bound for \(\beta\), and one may
subtract either \(B\) or \(\Pi\) because the rounded outcomes obey both
floors samplewise.

### Theorem 4.2 (diluted hyperplane conversion of every strict SDP gain)

Let \(X\in\mathcal E_B\) satisfy \(S(X)\le V\) (in particular, one may
take an SDP minimizer), and set

\[
D=V-S(X)\ge0,
\qquad
L_3(X)=\sum_{K<L}|w_{KL}|\,|X_{KL}|^3,
\tag{4.2}
\]

and choose \(0<t\le1/2\).  The diluted matrix

\[
Y_t=(1-t)I+tX
\tag{4.3}
\]

is a correlation matrix.  Hyperplane rounding and

\[
|\arcsin y-y|\le\frac{|y|^3}{3}
\qquad(|y|\le1/2)
\tag{4.4}
\]

give

\[
\boxed{
\beta\le
V-\frac{2t}{\pi}D
+\frac{4t^3}{3\pi}L_3(X).}
\tag{4.5}
\]

If \(D>0\), this is strictly below \(V\) for sufficiently small \(t\).
More explicitly, define

\[
\Phi(D,L)=
\begin{cases}
\dfrac{4}{3\pi\sqrt2}\dfrac{D^{3/2}}{\sqrt L},
   &0<D\le L/2,\\[6pt]
\dfrac{2D}{3\pi},&D\ge L/2,
\end{cases}
\tag{4.6}
\]

with \(\Phi(0,L)=0\).  Optimizing (4.5) at
\(t=\sqrt{D/(2L)}\) in the first case and \(t=1/2\) in the second gives

\[
\boxed{
\beta-P\le V-P-\Phi(D,L_3(X))
\quad(P=\Pi\text{ or }B).}
\tag{4.7}
\]

If \(L_3(X)=0\), then \(D=0\), so no exceptional positive-gain case is
missing.

This theorem is dimension-free but additive.  An odd-cycle example in
Section 7 shows that no universal multiplicative bound of
\(\beta-B\) by \(S(X)-B\) is possible for the basic elliptope.

### Theorem 4.3 (isotropic conditional-mean rounding)

Factor a floor-feasible correlation matrix as

\[
X_{KL}=\langle u_K,u_L\rangle,
\qquad u_K\in\mathbb R^r,
\qquad r=\operatorname{rank}X.
\tag{4.8}
\]

Suppose a random vector \(Y\in\mathbb R^r\) satisfies

\[
\mathbb E YY^T=I_r,
\qquad
|\langle Y,u_K\rangle|\le\rho
\quad\text{almost surely for every }K.
\tag{4.9}
\]

Let \(\delta\) be an independent fair sign.  Conditional on \((Y,\delta)\),
choose the component signs independently with means

\[
\mathbb E(\varepsilon_K\mid Y,\delta)
=\delta\frac{\langle Y,u_K\rangle}{\rho}.
\tag{4.10}
\]

Then the component marginals are fair and, for \(K\ne L\),

\[
\mathbb E\varepsilon_K\varepsilon_L=\rho^{-2}X_{KL}.
\tag{4.11}
\]

Consequently

\[
\boxed{
\beta-P
\le
\rho^{-2}(S(X)-P)
+(1-\rho^{-2})(V-P),
\quad P\in\{\Pi,B\}.}
\tag{4.12}
\]

For \(P=\Pi\), the exact fully separated form is

\[
\boxed{
\beta-\Pi
\le
(B-\Pi)
+(1-\rho^{-2})(V-B)
+\rho^{-2}(S(X)-B).}
\tag{4.13}
\]

#### Proof

The conditional means in (4.10) lie in \([-1,1]\).  Symmetry of \(\delta\)
makes every marginal fair.  Conditional independence and (4.9) yield

\[
\mathbb E\varepsilon_K\varepsilon_L
=\rho^{-2}\mathbb E
  \langle Y,u_K\rangle\langle Y,u_L\rangle
=\rho^{-2}X_{KL}.
\]

The diagonal sign correlations remain (1), so the realized cut
correlation matrix in expectation is

\[
(1-\rho^{-2})I+\rho^{-2}X.
\]

Taking its Gram objective proves (4.12); splitting at \(B\) gives (4.13).
Every conditional outcome is an actual sign vector.  \(\square\)

Define \(\rho_{\rm iso}(X)\) as the least slab radius in (4.9).  This least
radius is attained: the \(u_K\) span \(\mathbb R^r\), so every fixed-radius
slab intersection is compact, and a weak limit preserves both support and
the second-moment constraint.  Uniform
surface measure on the sphere of radius \(\sqrt r\) is isotropic and gives

\[
1\le\rho_{\rm iso}(X)\le\sqrt r.
\tag{4.14}
\]

Thus every rank-\(r\) point has the exact-factor rounding

\[
\boxed{
\beta-P\le
\frac{S(X)-P}{r}
+\left(1-\frac1r\right)(V-P).}
\tag{4.15}
\]

The use of surface measure matters: uniform volume measure on the unit ball
would have covariance \(I/(r+2)\), not \(I/r\).

There is an exact lossless characterization:

\[
\boxed{
\rho_{\rm iso}(X)=1
\quad\Longleftrightarrow\quad
X\text{ lies in the cut-correlation polytope}.}
\tag{4.16}
\]

For the forward direction,
\(\mathbb E\langle Y,u_K\rangle^2=1\) while the absolute value is at most
\(1\), so every projection is a sign almost surely and
\(X=\mathbb E ss^T\).  Conversely, suppose \(X=\mathbb E ss^T\) and form
the full-row-rank matrix \(U=[u_1\ \cdots\ u_N]\), so \(X=U^TU\).
Every \(s\) in the support lies in \(\operatorname{im}U^T\): for
\(a\in\ker U\), one has
\(\mathbb E(a^Ts)^2=a^TXa=0\).  Therefore

\[
Y=(UU^T)^{-1}Us
\]

satisfies \(U^TY=s\), and direct substitution gives
\(\mathbb EYY^T=I_r\).  This is the required radius-one isotropic lift.

### Corollary 4.4 (coherence bound)

Let \(N=|\mathscr K|\).  There is an orthonormal basis in which

\[
\max_{K,j}|u_K(j)|
\le\sqrt{\frac{2\log(4Nr)}{r}}.
\tag{4.17}
\]

To see this, Haar-rotate the basis.  For a fixed entry, the exact sphere
moments give

\[
\mathbb E(\sqrt r\,U_1)^{2k}
=\frac{r^k(2k-1)!!}{r(r+2)\cdots(r+2k-2)}
\le(2k-1)!!.
\tag{4.18}
\]

Hence \(\sqrt r\,U_1\) is \(1\)-subgaussian; a union bound over \(Nr\)
entries proves (4.17) for some rotation.  Taking
\(Y=\pm\sqrt r\,e_J\), with \(J\) uniform, gives

\[
\boxed{
\rho_{\rm iso}(X)^2
\le\min\{r,2\log(4Nr)\}.}
\tag{4.19}
\]

When \(S(X)\le V\), one can therefore transfer at least a
\(1/\min\{r,2\log(4Nr)\}\) fraction of the SDP gain \(V-S(X)\).  Since
\(N\le\operatorname{Cat}_m\) in the genuine ownership setting,
\(\log N=O(n)\); this is still only an \(O(1/n)\)-fraction in the worst
case and is not by itself a Catalan-floor theorem.

### Theorem 4.5 (local-cut hierarchy interpolation)

Assume \(N\ge2\) and \(2\le t\le N\).  Suppose every principal restriction
of \(X\) to at most \(t\) components
is the pair-correlation matrix of a fair sign law.  Write

\[
N=at+s,
\qquad0\le s<t,
\tag{4.20}
\]

and set

\[
\lambda_{N,t}
=\frac{at(t-1)+s(s-1)}{N(N-1)}.
\tag{4.21}
\]

Randomly partition the components into \(a\) blocks of size \(t\) and one
block of size \(s\), and independently sample the prescribed fair sign law
in each block.  A fixed pair shares a block with probability
\(\lambda_{N,t}\); cross-block correlations vanish.  Therefore

\[
\boxed{
\beta-P\le
(1-\lambda_{N,t})(V-P)
+\lambda_{N,t}(S(X)-P),
\quad P\in\{\Pi,B\}.}
\tag{4.22}
\]

Three-variable triangle/perimeter inequalities give the \(t=3\) local
condition.  A genuine level-\(t\) local-marginal/Lasserre solution gives the
general condition.  The coefficient becomes (1) only at \(t=N\); fixed
local levels have coefficient \(O(t/N)\) without additional component
geometry.

For \(N=1\), the objective is identically \(V\) and no rounding statement
is needed.

## 5. Direct floor-centered vector discrepancy

The SDP theorems interpolate between \(V\) and a fractional value.  The
next two theorems target the row floor \(B\) itself.

Let \(D\) be the matrix whose columns are the \(d_K\), and let

\[
g_K=\|d_K\|^2.
\tag{5.1}
\]

### Theorem 5.1 (zonotope floor targeting and partial coloring)

Choose integer roots \(s_p\) with \(s_p^2=b_p\), and define

\[
h=(\sqrt{\alpha_p}\,s_p)_p.
\tag{5.2}
\]

Suppose there is \(x\in[-1,1]^N\) satisfying

\[
Dx=h.
\tag{5.3}
\]

Then

\[
\boxed{
\beta-B\le
\Phi(x):=\sum_K(1-x_K^2)g_K.}
\tag{5.4}
\]

Moreover, one may choose an extreme point of the affine box fiber in
(5.3).  Its fractional columns are linearly independent, so at most

\[
r_D=\operatorname{rank}D
\tag{5.5}
\]

coordinates remain fractional.

#### Proof

Round the coordinates independently to signs with means \(x_K\).  Then

\[
\mathbb E R
=\|Dx\|^2+\sum_K(1-x_K^2)\|d_K\|^2
=B+\Phi(x).
\tag{5.6}
\]

Multiplying all rounded signs by one independent fair sign makes every
component marginal fair without changing \(R\).  If the fractional columns
at an extreme fiber point were dependent, a small two-sided perturbation
in their kernel would stay in the same affine box fiber, contradicting
extremality.  Finally, \(\Phi\) is concave on the box, so its minimum on the
compact affine fiber is attained at an extreme point and is no larger than
its value at the initially supplied \(x\).  \(\square\)

The feasibility condition (5.3) is exactly the zonotope membership

\[
h\in\sum_K[-d_K,d_K],
\tag{5.7}
\]

equivalently

\[
|\langle y,h\rangle|
\le\sum_K|\langle y,d_K\rangle|
\quad\text{for every }y.
\tag{5.8}
\]

Taking the always-feasible zero fiber \(Dx=0\) gives the unconditional
rank partial-coloring bound

\[
\boxed{
\beta\le\sum_{j=1}^{r_D}g_{(j)}\le r_Dg_{\max},}
\tag{5.9}
\]

where the \(g_{(j)}\) are the largest component energies.  The floor-target
version (5.4) can be much stronger, but its zonotope reachability is a real,
unproved ownership condition.

### Corollary 5.2 (matching inside a fractional floor fiber)

For a fractional pair with means \(x_i,x_j\), set

\[
\kappa_{ij}(x)=
\begin{cases}
1-|x_i+x_j|+x_ix_j,&w_{ij}>0,\\
1-|x_i-x_j|-x_ix_j,&w_{ij}<0.
\end{cases}
\tag{5.10}
\]

Both expressions are nonnegative.  Couple disjoint matched pairs at the
Fréchet endpoint opposing the sign of \(w_{ij}\), and leave distinct blocks
independent.  Their individual means remain \(x_i,x_j\), while the expected
Gram objective improves by \(2|w_{ij}|\kappa_{ij}(x)\).  Hence

\[
\boxed{
\beta-B\le
\Phi(x)-2\max_M\sum_{ij\in M}|w_{ij}|\kappa_{ij}(x).}
\tag{5.11}
\]

Separately, apply the same Fréchet coupling to the always-feasible
zero-mean rounding, without imposing a nonzero floor target.  This gives
the first-wave matching bound
\(\beta\le V-2\mathfrak M\).  When \(h=0\), it is exactly (5.11) with
\(x=0\).

### Theorem 5.3 (signed-incidence synchronization SDP)

For every row \(p\), choose a local minimizing pattern
\(\sigma^p\in\{\pm1\}^{\mathscr K}\), so

\[
(z_p\cdot\sigma^p)^2=b_p.
\tag{5.12}
\]

Only incidences with \(z_{pK}\ne0\) are used.  Put

\[
L_p=\sum_K|z_{pK}|,
\qquad
a_{pK}=\alpha_pL_p|z_{pK}|,
\qquad
T=\sum_{p,K}a_{pK}=\sum_p\alpha_pL_p^2,
\tag{5.13}
\]

and define

\[
\delta_{\rm sync}
=\min_{\|u_K\|=\|v_p\|=1}
  \sum_{p,K}a_{pK}
  \frac{1-\sigma^p_K\langle u_K,v_p\rangle}{2}.
\tag{5.14}
\]

Then

\[
\boxed{\beta-B\le4\sqrt{T\delta_{\rm sync}}.}
\tag{5.15}
\]

There is also the sharper angular statement

\[
\boxed{
\beta-B\le
4\inf_{u,v}\sum_{p,K}a_{pK}
\frac{\arccos(\sigma^p_K\langle u_K,v_p\rangle)}{\pi}.}
\tag{5.16}
\]

#### Proof

Hyperplane-round the vectors \(u_K,v_p\), giving global component signs
\(\varepsilon_K\) and auxiliary row signs \(t_p\).  Call incidence \(pK\)
violated when

\[
\varepsilon_K\ne t_p\sigma^p_K.
\tag{5.17}
\]

If \(M_p\) is the sum of \(|z_{pK}|\) over violated incidences, then, after
factoring out \(t_p\), the new row sum is obtained from the local optimizer
by reversing precisely those terms.  Writing the reversed and unreversed
partial sums separately gives

\[
(z_p\cdot\varepsilon)^2-b_p\le4L_pM_p.
\tag{5.18}
\]

Thus the total excess is at most four times the violated edge mass.  The
violation probability is the normalized angle in (5.16).  Finally

\[
\frac{\arccos a}{\pi}
\le\sqrt{\frac{1-a}{2}}
\qquad(-1\le a\le1),
\tag{5.19}
\]

and weighted Cauchy--Schwarz gives (5.15).  Every rounded
\(\varepsilon\) is again a whole-component exact factor.  \(\square\)

If deleting incidence edges \(E_0\) leaves a forest, propagate the desired
relative signs on that forest.  Only \(E_0\) can be violated, so the
deterministic feedback bound is

\[
\boxed{
\beta-B\le4\sum_{pK\in E_0}a_{pK}.}
\tag{5.20}
\]

Amplitude locking remains separate.  Greedy number partitioning gives

\[
b_p\le m_p^2,
\qquad
m_p=\max_K|z_{pK}|,
\tag{5.21}
\]

Indeed, after absorbing the signs of the coefficients, assign each
successive magnitude opposite to the current partial sum; induction keeps
the absolute partial sum at most the largest magnitude seen.
For an all-zero row, define \(m_p=0\).

Consequently,

\[
\boxed{
B-\Pi\le\sum_p\alpha_p(m_p^2-\pi_p).}
\tag{5.22}
\]

Equations (5.15) and (5.22) are a fully proved separation of amplitude and
holonomy with explicit constants.

## 6. Catalan-scale implication and the remaining genuine lemma

Let

\[
E_{A_0,m}:=\frac{H\operatorname{Cat}_m}{n}.
\tag{6.1}
\]

The floor-aware theorems give several rigorous **sufficient certificates**
for

\[
\beta-\Pi=O_{A_0}(E_{A_0,m}).
\tag{6.2}
\]

For example, (5.15) and (5.22) give (6.2) if

\[
\sum_p\alpha_p(m_p^2-\pi_p)=O_{A_0}(E_{A_0,m}),
\tag{6.3}
\]

\[
T\delta_{\rm sync}=O_{A_0}(E_{A_0,m}^2).
\tag{6.4}
\]

Alternatively, Theorem 4.3 gives (6.2) if

\[
B-\Pi=O_{A_0}(E_{A_0,m})
\tag{6.5}
\]

and, for one floor-feasible \(X\),

\[
(S(X)-B)+(\rho^2-1)(V-B)
=O_{A_0}(\rho^2E_{A_0,m}).
\tag{6.6}
\]

This displays an important obstruction: if \(V-B\) is factor-scale, a
fixed \(\rho>1\) leaves a fixed fraction of that excess.  The exact
condition on this term is

\[
1-\rho^{-2}
=O_{A_0}\!\left(\frac{E_{A_0,m}}{V-B}\right).
\]

In the intended small-ratio regime this is equivalent to both
\(\rho^2-1=O_{A_0}(E_{A_0,m}/(V-B))\) and
\(\rho=1+O_{A_0}(E_{A_0,m}/(V-B))\).  Alternatively, \(V-B\) itself
must already be Catalan-small.

Fix \(A_0\).  Suppose there are constants
\(\eta_{A_0}>0,C_{A_0},C'_{A_0}<\infty\) and \(m_0(A_0)\), independent of
\(m\) and \(F\), with the following property for every \(m\ge m_0(A_0)\)
and every exact factor \(F\).  The **UNPROVED SAME-TRANSPOSITION
IDEAL-GAIN LEMMA** supplies a transposition \(\tau\) such that

\[
A_\tau-\Pi_\tau
\ge
\frac{4\eta_{A_0}}n\mathcal Q_{A_0}(F)
-\frac{C_{A_0}H\operatorname{Cat}_m}{n}.
\tag{6.7}
\]

For that **same** \(\tau\), additionally assume that one of the AA2
certificates proves

\[
\beta_\tau-\Pi_\tau
\le\frac{C'_{A_0}H\operatorname{Cat}_m}{n}.
\tag{6.8}
\]

Then (1.11) gives

\[
C_\tau^*
\ge
\frac{\eta_{A_0}}n\mathcal Q_{A_0}(F)
-\frac{(C_{A_0}+C'_{A_0})H\operatorname{Cat}_m}{4n}.
\tag{6.9}
\]

Every transposition-component-cut-local exact factor would therefore obey

\[
\boxed{
\mathcal Q_{A_0}(F)
\le
\frac{C_{A_0}+C'_{A_0}}{4\eta_{A_0}}
H\operatorname{Cat}_m.}
\tag{6.10}
\]

Finite descent would then prove the fixed-window unlabelled overload
statement and, by the frozen diagonal argument for every fixed \(A_0\), MWB
and the asymptotic contiguous-OR width theorem.  It would not prove the
strictly stronger labelled common-owner synchronization statement.

Neither (6.7) nor any uniform genuine-factor hypothesis (6.3)--(6.6) is
proved here.  The same-transposition and same-window quantifiers cannot be
separated.

## 7. Sharp obstructions and scope

### 7.1 Aggregate orthogonality can consume the entire floor-subtracted room

Take the four rows

\[
(+,+,+),\quad(+,-,-),\quad(-,+,-),\quad(-,-,+)
\tag{7.1}
\]

with common weight \(\alpha\).  These are three mutually orthogonal
balanced columns of a \(4\times4\) Hadamard matrix.  Every row has

\[
\pi_p=b_p=1,
\]

but

\[
G=4\alpha I_3.
\tag{7.2}
\]

Therefore

\[
\boxed{
\Pi=B=4\alpha,
\qquad
A=V=\beta=12\alpha,
\qquad
\beta-B=8\alpha.}
\tag{7.3}
\]

The objective is constant on the full cut polytope.  No correlated law,
metric strengthening, or SDP hierarchy can improve fair variance.  More
generally, \(k\) mutually orthogonal \(\{\pm1\}\)-columns have
\(G=\alpha NI_k\); their row floor is \(0\) for even \(k\) and \(1\) for
odd \(k\).

### 7.2 An exact abstract simultaneous-depth cancellation block

This is a stacked integral coefficient array, not a claimed wreath
realization.

Fix a positive integer \(L\).  At depth \(q_+\), use
\(c_{q_+}L\) copies of each of the two orbit rows

\[
(1,1),\qquad(-1,-1),
\tag{7.4}
\]

and at depth \(q_-\), use \(c_{q_-}L\) copies of each of

\[
(1,-1),\qquad(-1,1).
\tag{7.5}
\]

Thus the total weights \(2/c_q\) agree exactly.  Each depth separately has
\(B_q=\Pi_q=\beta_q=0\):
the first prefers opposite component signs and the second equal signs.  But
the stacked Grams are proportional to

\[
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\tag{7.6}
\]

whose sum is diagonal.  Hence over the common window

\[
\boxed{B=\Pi=0,\qquad A=V=\beta.}
\tag{7.7}
\]

This obstruction survives the exact cut polytope.  It proves that one may
not optimize component correlations separately at each rank and add the
gains.  All vector and SDP constructions must use the single aggregate
stacked vectors (1.2).

### 7.3 Amplitude and holonomy are independent

* A disjoint row with one coefficient \(z=2\) has
  \(\Pi=0\), \(B=\beta=V=4\).  Its incidence graph is a forest and there is
  no correlation to exploit.  This is pure amplitude locking.
* Three unit rows supported on component pairs \(12,23,31\), each with
  coefficients \((1,1)\), have \(B=\Pi=0\), but every signing leaves at
  least one equal-sign edge, so \(\beta=4\).  This is pure one-cycle
  holonomy.  Disjoint replication makes the loss linear while row and
  column degrees stay two.

### 7.4 No multiplicative basic-SDP rounding above the floor

On an odd cycle of length \(L=2k+1\), put one row \((1,1)\) on every edge.
Then \(B=\Pi=0\) and \(\beta=4\).  Choose planar unit vectors with successive
angle \(\pi-\pi/L\); the cycle closes because

\[
L(\pi-\pi/L)=(L-1)\pi=2k\pi.
\]

The basic vector residual is

\[
4L\sin^2\!\left(\frac\pi{2L}\right)<\frac{\pi^2}{L},
\tag{7.8}
\]

which tends to zero.  Thus there is no universal constant \(C\) such that

\[
\beta-B\le C(\gamma-B)
\tag{7.9}
\]

for the basic elliptope.  Angular hyperplane rounding is nevertheless
honest: for the displayed vectors it has expected residual \(4\), hence
exactly one violated edge in expectation.  Since every odd-cycle signing
violates at least one edge, it has exactly one violated edge almost surely.

### 7.5 Triangle metrics still miss global parity

For five components and a positive integer \(t\), put one row

\[
z_{ij}=t(e_i+e_j)
\]

for every pair \(i<j\).  Then every row has \(b_{ij}=\pi_{ij}=0\), and

\[
R(\varepsilon)
=t^2\left(15+\left(\sum_{i=1}^5\varepsilon_i\right)^2\right).
\tag{7.10}
\]

Therefore \(\beta=16t^2\) and \(V=20t^2\).  The regular-simplex matrix

\[
X_{ii}=1,
\qquad X_{ij}=-\frac14
\tag{7.11}
\]

is positive semidefinite, satisfies every three-variable triangle and
perimeter inequality, satisfies all row floors, and has value
\(15t^2\).  Positive semidefiniteness proves this is optimal because the
objective is \(t^2(15+{\bf1}^TX{\bf1})\).  The missing cut inequality is
the odd global parity constraint \({\bf1}^TX{\bf1}\ge1\).  Scaling \(t\)
makes the additive metric gap arbitrary.

### 7.6 What the abstract obstructions do and do not prove

The \(\{\pm1\}\)-coefficient Hadamard and two-depth arrays satisfy:

* integral coefficients and exact row parity;
* exact local floors;
* balanced anti-invariant component columns;
* a nonnegative pair-orbit realization via

  \[
  a_K(S_p)=\frac{1+z_{pK}}2,
  \qquad
  a_K(\tau S_p)=\frac{1-z_{pK}}2;
  \tag{7.12}
  \]

* compatibility with every metric or exact cut correlation constraint.

Formula (7.12) is asserted only for these \(\{\pm1\}\)-coefficient arrays;
it is not a realization formula for the \(t\)-scaled five-component metric
example.

They are **not proved** to be genuine ownership components of one exact
wreath factor.  Missing are squarefree middle support, realization by
complete cyclic-window histograms, connectivity of the middle ownership
overlay, absolute component rank totals and point margins, and especially
the common nested-prefix chronology coupling all depths.  Thus they are not
counterexamples to \(LM_{A_0}\) or MWB.  They prove that parity, local
floors, nonnegative pair tables, degree bounds, metric consistency, and
generic SDP rounding do not by themselves imply the needed Catalan error.

Finally, even perfect bundling \(\beta=\Pi\) does not create descent when
\(A=\Pi\).  The audited integer \(1\)-Lipschitz Johnson obstruction attacks
this independent ideal-gain side.  A complete proof must control ideal gain
and floor-subtracted bundling for the same transposition.

## 8. Independent audit record and final status

The decisive diagonal-majorant step was independently rederived from the
zero-diagonal matrix normalization.  The audit checked:

\[
R(\varepsilon)=V+\varepsilon^TW_0\varepsilon,
\]

\[
\|W_0\|_F=\sqrt2\,\sigma,
\]

\[
V-\beta\ge
\frac{2}{\pi\lambda_+}\|W_0\|_F^2
=\frac4{\pi\lambda_+}\sigma^2
\ge\frac{2\sqrt2}{\pi}\sigma,
\]

and the cut conversion by division by \(4\).  The floor-aware SDP chain,
isotropic rank coefficient \(1/r\), coherence coefficient, hyperplane
dilution constants, zonotope variance identity, and synchronization
Lipschitz constant \(4\) were separately checked.  The old three-vector
elliptope obstruction was not reused as an obstruction to metric SDPs;
Sections 7.4--7.5 state the correct restricted gaps.

The theorem-level answer to AA2 is therefore:

\[
\boxed{
\text{Correlated fair whole-component signs beat fair variance exactly
when }W_0\ne0,}
\]

with the quantitative bounds (3.4), (3.12), (4.7), (4.12), (5.4), and
(5.15), all producing genuine exact-factor signings whenever their input
vectors come from a genuine ownership overlay.  What remains unproved
is a genuine cyclic-ownership theorem preventing aggregate cross-depth Gram
cancellation and forcing one of these floor-subtracted certificates to

\[
O_{A_0}\!\left(\frac{H\operatorname{Cat}_m}{n}\right)
\]

for the same transposition that has the scale-correct ideal Johnson gain.
