# Component noise through Johnson harmonics

Date: 2026-07-25

## 1. Verdict

Fix

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\operatorname{Cat}_m=\frac Wn,
\qquad H=\lceil A\sqrt m\rceil .
\]

This attack does not prove MWB, and it does not construct an exact-factor
family disproving

\[
V_{\tau,H}(F)\le A_{\tau,H}(F)+C_AH\operatorname{Cat}_m.
\tag{CN\(_A\)}
\]

It gives the following unconditional advances.

1. Every ownership-component innovation has Johnson degrees \(0\) and
   \(1\) identically zero.  Its degree-\(j\) part is
   \(\tau\)-anti-invariant.  Thus the component-noise problem decomposes
   exactly, with no cross-isotype terms.

2. On \(E_j\cong S^{(n-j,j)}\), uniform-transposition smoothing removes
   the fraction

   \[
   \kappa_j=\frac{j(n-j+1)}{n(n-1)}
   \]

   of squared norm.  The unique slow mode is \(E_2\), with
   \(\kappa_2=2/n\).

3. Every genuine fixed-\(\tau\) switching cube has zero mean heat gap
   separately at every rank and every Johnson level:

   \[
   \mathbb E_{\text{cube corners}}A_{\tau,q,j}
   =V_{\tau,q,j}.
   \]

   The corresponding stationary covariance identity holds as an operator,
   even after arbitrary equivariant cross-rank filtering.  Consequently
   no Johnson multiplier, generic coboundary, or levelwise frame argument
   can by itself create a strict heat gap.

4. The floor-corrected recurrence separates the unique slow \(E_2\) term
   from an exact nonnegative higher-harmonic rebate.  The unavoidable
   replenishment is

   \[
   \frac2n\sum_{q\le H}\frac{\beta_q}{c_q}
   =\Theta_A(H\operatorname{Cat}_m),
   \]

   not the much larger unscaled floor.

5. At \(q=1\), the full one-step noise excess is reduced to a concrete
   genuine-factor statistic \(s_\tau(F)\): the number of moved
   singleton--singleton target pairs whose unique owners lie in different
   actual overlay components.  At an exactly balanced first shadow,

   \[
   4s_\tau
   \le V_{\tau,1}-A_{\tau,1}
   <4s_\tau+64\operatorname{Cat}_m.
   \]

   Hence a termwise Catalan noise ceiling is equivalent to an
   owner-coalescence theorem \(s_\tau=O(\operatorname{Cat}_m)\).
   No exact family with \(s_\tau/\operatorname{Cat}_m\to\infty\) is known.

6. The slow part of the \(q=1\) noise is nevertheless controlled
   unconditionally:

   \[
   V_{\tau,1,2}
   =O\!\left(\frac{\operatorname{Cat}_m}{n}\right).
   \]

   Over an arbitrarily long fair heat history, its entire geometrically
   propagated contribution is at most

   \[
   (16+o(1))\operatorname{Cat}_m.
   \]

   Thus \(q=1,E_2\) is not the missing mesoscopic obstruction.

7. More generally, every \(E_2\) component contribution is exactly the
   image of a weighted near-antipodal coordinate-distance graph.  This
   yields an explicit bound, but for \(q\asymp\sqrt m\) it is not summably
   small enough.

8. Two natural static commutator mechanisms fail.  A fixed word with
   conditionally fair signs has only suffix-filtered nonnegative
   innovation variances.  A fixed transposition subgroup which annihilates
   the entire ambient \(E_2\) module has one canonical ownership block and
   hence only whole-factor relabelings.  This does not rule out a fixed
   word satisfying the final restitution bound by filtering, correlated
   nonfair choices, or the still-open correlated Haar frame.  Adaptive
   recomputation remains a viable route.

The clean surviving route-specific gates are stated in Section 11.  They
are explicitly **UNPROVED**.  The raw near-floor component-noise gate
already refuted by
the audited sparse Boolean-\(E_2\) theorem is kept distinct from the
still-open \(A\)-relative ceiling \((\mathrm{CN}_A)\).

No finite search, solver, random occupancy model, or web search is used.

---

## 2. Exact setup

At depth \(q\), put

\[
r=m-q,\qquad
N_q=\binom nr,\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\]

\[
\beta_q=N_q\theta_q(1-\theta_q).
\]

For an exact middle wreath factor \(F\), let \(\mu_q(F)\) be its
rank-\(r\) cyclic-interval histogram and set

\[
f_q(F)=\mu_q(F)-\lambda_q\mathbf1,
\qquad
Q_q(F)=\|f_q(F)\|_2^2-\beta_q.
\]

The fixed-window full floor-corrected energy is

\[
\mathcal Q_A(F)=
\sum_{q\le H}\frac{Q_q(F)}{c_q},
\qquad
B_A=\sum_{q\le H}\frac{\beta_q}{c_q}.
\tag{2.1}
\]

For a stacked multirank vector \(g=(g_q)_{q\le H}\), write

\[
\|g\|_A^2=\sum_{q\le H}\frac{\|g_q\|_2^2}{c_q},
\qquad
\langle g,h\rangle_A
=\sum_{q\le H}\frac{\langle g_q,h_q\rangle_2}{c_q}.
\tag{2.1A}
\]

Fix a coordinate transposition \(\tau\).  In the ownership overlay between
\(F\) and \(\tau F\), let \(K\) run through connected components and let
\(L_K,R_K\) be its two row sides.  Define

\[
\Delta_{K,q}
=\mu_q(L_K)-\mu_q(R_K).
\tag{2.2}
\]

The overlay is \(n\)-regular bipartite, so

\[
|L_K|=|R_K|=:s_K,
\qquad
\sum_Ks_K=|F|=t.
\tag{2.3}
\]

Moreover \(R_K=\tau L_K\).  Indeed, every wreath row has a middle window
containing both transposed coordinates or neither: the two coordinates
have \(2m=n-1\) total incidences among its \(n\) middle windows, so not
every window can contain exactly one.  That fixed mask joins \(C\) to
\(\tau C\) inside the same component.

Put

\[
A_{\tau,q}
=\left\|\sum_K\Delta_{K,q}\right\|_2^2,
\qquad
V_{\tau,q}
=\sum_K\|\Delta_{K,q}\|_2^2,
\tag{2.4}
\]

and

\[
A_{\tau,H}=\sum_{q\le H}\frac{A_{\tau,q}}{c_q},
\qquad
V_{\tau,H}=\sum_{q\le H}\frac{V_{\tau,q}}{c_q}.
\tag{2.5}
\]

For a component signing
\(\varepsilon=(\varepsilon_K)_K\in\{\pm1\}^{\mathcal K}\), the integral
child factor satisfies

\[
f_q(F_\varepsilon)
=P_\tau f_q(F)
+\frac12\sum_K\varepsilon_K\Delta_{K,q},
\qquad
P_\tau=\frac{I+\tau}{2}.
\tag{2.6}
\]

All choices are common across depths.  Equation (2.6) is an identity
between histograms of actual exact factors, not a fractional construction.

---

## 3. Exact Johnson-isotype decomposition

Write the rank-\(r\) Johnson module as

\[
\mathbb R^{\binom{[n]}r}
=E_{q,0}\oplus E_{q,1}\oplus\cdots\oplus E_{q,r},
\qquad
E_{q,j}\cong S^{(n-j,j)},
\tag{3.1}
\]

and let \(\Pi_{q,j}\) denote orthogonal projection.

### Theorem 3.1 — component innovations begin at level \(2\)

For every \(K,q\),

\[
\boxed{
\Pi_{q,0}\Delta_{K,q}
=\Pi_{q,1}\Delta_{K,q}=0,
\qquad
\tau\Delta_{K,q}=-\Delta_{K,q}.}
\tag{3.2}
\]

#### Proof

Every wreath contributes exactly \(n\) cyclic rank-\(r\) intervals, and
exactly \(r\) of them contain any fixed coordinate.  By (2.3), the two
sides of a component therefore have equal total mass and equal point
margins.  Their difference is orthogonal to \(E_{q,0}\oplus E_{q,1}\).

Since \(R_K=\tau L_K\),

\[
\tau\Delta_{K,q}
=\mu_q(\tau L_K)-\mu_q(\tau R_K)
=\mu_q(R_K)-\mu_q(L_K)
=-\Delta_{K,q}.
\]

This proves (3.2). \(\square\)

Put

\[
\Delta_{K,q,j}=\Pi_{q,j}\Delta_{K,q},
\]

\[
A_{\tau,q,j}
=\left\|\sum_K\Delta_{K,q,j}\right\|_2^2,
\qquad
V_{\tau,q,j}
=\sum_K\|\Delta_{K,q,j}\|_2^2.
\tag{3.3}
\]

Orthogonality gives

\[
A_{\tau,q}=\sum_{j\ge2}A_{\tau,q,j},
\qquad
V_{\tau,q}=\sum_{j\ge2}V_{\tau,q,j}.
\tag{3.4}
\]

Thus

\[
\boxed{
A_{\tau,q,j}-V_{\tau,q,j}
=2\sum_{K<L}
\langle\Delta_{K,q,j},\Delta_{L,q,j}\rangle.}
\tag{3.5}
\]

The heat gap is exactly a cross-component Gram-correlation statement
inside each isotype.

### Theorem 3.2 — exact levelwise heat identity

For every \(q,j\ge2\),

\[
\boxed{
\mathbb E_\varepsilon
\|f_{q,j}(F_\varepsilon)\|_2^2
=
\|f_{q,j}(F)\|_2^2
+\frac14\bigl(V_{\tau,q,j}-A_{\tau,q,j}\bigr).}
\tag{3.6}
\]

#### Proof

The two terms in (2.6) are respectively \(\tau\)-invariant and
\(\tau\)-anti-invariant, hence orthogonal after projection to \(E_{q,j}\).
Also

\[
\sum_K\Delta_{K,q}=f_q(F)-\tau f_q(F)
=2(I-P_\tau)f_q(F),
\]

so

\[
\|P_\tau f_{q,j}\|_2^2
=\|f_{q,j}\|_2^2-\frac14A_{\tau,q,j}.
\]

Independent signs kill cross-component products and contribute
\(\frac14V_{\tau,q,j}\). \(\square\)

### Theorem 3.3 — exact spectral coefficients

For a uniform unordered coordinate transposition,

\[
\boxed{
\mathbb E_\tau A_{\tau,q,j}
=4\kappa_j\|f_{q,j}\|_2^2,
\qquad
\kappa_j=
\frac{j(n-j+1)}{n(n-1)}.}
\tag{3.7}
\]

In particular,

\[
\kappa_2=\frac2n,
\qquad
\kappa_j-\frac2n
=\frac{(j-2)(n-j-1)}{n(n-1)}
\quad(j\ge3).
\tag{3.8}
\]

#### Proof

The Johnson Laplacian identity is

\[
\sum_{\tau}(I-\tau)=L_{J(n,r)}.
\]

Its eigenvalue on \(E_{q,j}\) is \(j(n-j+1)\).  Hence

\[
\sum_\tau\|g-\tau g\|_2^2
=2j(n-j+1)\|g\|_2^2.
\]

Divide by \(\binom n2\).  Equation (3.8) is direct algebra.
\(\square\)

The \(\tau\)-anti-invariant part of \(E_{q,j}\), as an
\(S_{n-2}\)-module, is

\[
E_{q,j}^-(\tau)\cong S^{(n-j-1,j-1)}
\tag{3.9}
\]

and has dimension

\[
\binom{n-2}{j-1}-\binom{n-2}{j-2}.
\tag{3.10}
\]

Thus the slow space is not one-dimensional:

\[
\dim E_{q,2}^-(\tau)=n-3.
\tag{3.11}
\]

---

## 4. The exact floor and higher-harmonic rebate

Define

\[
\mathscr R_q(F)
=\mathbb E_\tau\frac{V_{\tau,q}}4
\tag{4.1}
\]

and

\[
s_q(F)
=\sum_{j\ge3}
\frac{(j-2)(n-j-1)}{n(n-1)}
\|f_{q,j}(F)\|_2^2.
\tag{4.2}
\]

Equations (3.7)--(3.8) give

\[
\mathbb E_\tau\frac{A_{\tau,q}}4
=\frac2n\|f_q\|_2^2+s_q.
\tag{4.3}
\]

Combining this with (3.6) and subtracting the factor-independent floor
gives the audited recurrence in its exact harmonic form:

\[
\boxed{
\mathbb E Q_q(F')
=\left(1-\frac2n\right)Q_q(F)
+\left(\mathscr R_q(F)-\frac2n\beta_q\right)
-s_q(F).}
\tag{4.4}
\]

Thus:

* \(2\beta_q/n\) is the unavoidable integer-floor replenishment;
* \(s_q\) is the exact higher-harmonic surplus;
* after subtracting both, the only unreimbursed coherent mode is \(E_2\).

Summing with weights \(1/c_q\), the floor term has precisely the desired
scale.  Indeed, the audited Riemann-sum formula

\[
\frac{B_A}{W\sqrt m}\longrightarrow
\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx
=:\kappa_A>0
\tag{4.5}
\]

implies

\[
\boxed{
\frac2nB_A=\Theta_A(H\operatorname{Cat}_m).}
\tag{4.6}
\]

A noise estimate which ignores \(s_q\) tries to erase genuine Boolean
high-harmonic mass.  The scale-correct one-step drift target remains

\[
\sum_{q\le H}\frac1{c_q}
\left[
\mathscr R_q-\frac2n\beta_q-s_q
\right]
\le
\frac{2-\eta_A}{n}\mathcal Q_A
+\frac{C_A}{n}H\operatorname{Cat}_m.
\tag{4.7}
\]

This is the corrected \(MHG_A\) gate.  A bound
\(V_{\tau,H}\le A_{\tau,H}+C_AHt\) is a different, insufficient
statement: it is pointwise in \(\tau\), limits only an upward fair-heat
fluctuation, and supplies no negative multiple of \(\mathcal Q_A\).
Neither statement is asserted to imply the other.

---

## 5. Exact-cell and stationary replenishment obstruction

### Theorem 5.1 — every exact switching cube has zero mean harmonic gap

Fix one genuine \(\tau\)-cell with component vectors
\(\Delta_{K,q,j}\).  At a corner
\(\sigma\in\{\pm1\}^{\mathcal K}\),

\[
A_{\tau,q,j}(F_\sigma)
=\left\|\sum_K\sigma_K\Delta_{K,q,j}\right\|_2^2,
\]

while

\[
V_{\tau,q,j}(F_\sigma)
=\sum_K\|\Delta_{K,q,j}\|_2^2
\]

is corner-independent.  Therefore

\[
\boxed{
\mathbb E_\sigma A_{\tau,q,j}(F_\sigma)
=V_{\tau,q,j}.}
\tag{5.1}
\]

The same identity holds after stacking ranks and inserting any positive
semidefinite quadratic form on the multiplicity space of copies of
\(E_j\).

#### Proof

Passing to a corner reverses the sign of precisely the switched component
vectors.  Expanding the squared norm and averaging independent signs kills
every \(K\ne L\) product. \(\square\)

This is a genuine exact-factor family, but it is not a counterexample to
\((\mathrm{CN}_A)\): a zero average gap does not force a corner with a
super-Catalan positive gap.

There is an operator version.

### Theorem 5.2 — stationary covariance is replenished level by level

Let \(\pi\) be the uniform distribution on a communicating class of the
fair component-heat chain.  Stack all rank copies of \(E_j\) as

\[
\mathcal M_j\cong\mathbb R^{h_j}\otimes E_j
\]

and put

\[
\Sigma_j=\mathbb E_\pi[f_jf_j^*].
\]

Since the class is \(S_n\)-invariant and \(j\ge2\),
\(\mathbb E_\pi f_j=0\); thus \(\Sigma_j\) is also the covariance
operator.

For fixed \(\tau\), let

\[
P_{\tau,j}
=I\otimes\frac{I+\rho_j(\tau)}2,
\]

\[
C_{F,\tau,j}
=\frac14\sum_K
\Delta_{K,j}\Delta_{K,j}^*.
\]

Then

\[
\boxed{
\mathbb E_\pi C_{F,\tau,j}
=(I-P_{\tau,j})\Sigma_j(I-P_{\tau,j}).}
\tag{5.2}
\]

In particular,

\[
\boxed{
\mathbb E_\pi V_{\tau,q,j}
=\mathbb E_\pi A_{\tau,q,j}.}
\tag{5.3}
\]

After averaging \(\tau\),

\[
\boxed{
\mathbb E_{\pi,\tau}V_{\tau,q,j}
=4\kappa_j\,
\mathbb E_\pi\|f_{q,j}\|_2^2.}
\tag{5.4}
\]

#### Proof

For fixed \(\tau\), its intrinsic interaction cells partition the exact
factor state space, and fair component heat is uniform averaging on each
cell.  Hence the fixed-\(\tau\) kernel is a self-adjoint idempotent and
preserves the uniform law on every closed communicating class.

The full class is invariant under \(S_n\): the all-one-side corner sends
\(F\) to \(\tau F\), and transpositions generate \(S_n\).  Schur's lemma
therefore gives

\[
\Sigma_j=M_j\otimes I_{E_j},
\]

so \(\Sigma_j\) commutes with \(P_{\tau,j}\).

Conditionally on \(F\),

\[
f_j'=P_{\tau,j}f_j+\xi_j,
\qquad
\mathbb E(\xi_j\mid F)=0,
\qquad
\mathbb E(\xi_j\xi_j^*\mid F)=C_{F,\tau,j}.
\]

Stationarity gives

\[
\Sigma_j=P_{\tau,j}\Sigma_jP_{\tau,j}
+\mathbb E_\pi C_{F,\tau,j}.
\]

Commutation and \(P_{\tau,j}^2=P_{\tau,j}\) give (5.2).  Taking block
traces proves (5.3), and (3.7) gives (5.4). \(\square\)

Consequently every equivariant positive semidefinite harmonic filter sees
component covariance exactly restore the covariance removed by coherent
smoothing in stationarity.  A coefficient improvement below \(2/n\) is
equivalent to proving low stationary excess energy; harmonic analysis does
not supply it for free.

---

## 6. What the sparse Boolean-\(E_2\) no-go does and does not refute

Let

\[
D_H=\sum_\tau A_{\tau,H},
\qquad
R_H=\sum_\tau V_{\tau,H}.
\]

The exact spectral identity is

\[
\boxed{
\begin{aligned}
D_H-4(n-1)B_A
={}&4(n-1)\mathcal Q_A\\
&+
2\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}
(j-2)(n-j-1)\|f_{q,j}\|_2^2.
\end{aligned}}
\tag{6.1}
\]

At a global minimizer of this same fixed-window energy,

\[
R_H\ge D_H.
\tag{6.2}
\]

The audited sparse Boolean-\(E_2\) stability theorem proves, at every
same-window global minimizer and on every fixed nonzero Gaussian window,

\[
R_H-4(n-1)B_A
=\Omega_A(nW\sqrt m).
\tag{6.3}
\]

It therefore refutes the former near-baseline target

\[
R_H\le4(n-1)B_A+o(nW).
\]

It gives no positive quantitative lower bound on \(R_H-D_H\) beyond
(6.2).  The right side of (6.3) may be paid entirely by the coherent
excess and the higher-harmonic term already present in (6.1).  Thus it
does not refute
\((\mathrm{CN}_A)\), whose content is an upper bound on component noise
relative to \(A_{\tau,H}\).

This distinction is essential: raw component variance cannot be
Catalan-small on a Gaussian window, while an \(A\)-relative component
ceiling remains open.

---

## 7. Why representation theory alone cannot prove the ceiling

For \(\tau=(1\,2)\), an explicit integral vector in the
\(\tau\)-anti-invariant part of \(E_{q,j}\) is

\[
v_j(S)=
\prod_{i=1}^j
\left(
\mathbf1_{\{2i-1\in S\}}
-\mathbf1_{\{2i\in S\}}
\right),
\tag{7.1}
\]

with

\[
\|v_j\|_2^2
=2^j\binom{n-2j}{r-j}.
\tag{7.2}
\]

Formally take two component vectors

\[
d_1=kv_j,\qquad d_2=-kv_j.
\]

Then

\[
A_j=0,\qquad
V_j=2k^2\|v_j\|_2^2.
\tag{7.3}
\]

For even \(k\), write

\[
u_1=b-\frac k2v_j,\qquad
u_2=b+\frac k2v_j
\]

with a sufficiently large \(\tau\)-invariant integral constant vector
\(b\).  Then

\[
\tau u_1-u_1=d_1,\qquad
\tau u_2-u_2=d_2,
\]

and \(u_1,u_2\) are nonnegative integral vectors with the correct total
and point-margin symmetries.

This is not asserted to be row-realizable by genuine exact-factor
components.  It proves the precise negative statement:

\[
\boxed{
\text{anti-invariance, integrality, and all degree-\(0,1\) identities
alone do not bound }V/A.}
\]

The missing input must concern actual ownership components.

---

## 8. The exact \(q=1\) owner-coalescence criterion

At \(q=1\),

\[
c_1=1,\qquad
N_1=\binom n{m-1},
\qquad
b:=W-N_1=\frac{2W}{m+2}<4t,
\tag{8.1}
\]

\[
Q_1=\sum_S(\mu_1(S)-1)(\mu_1(S)-2).
\tag{8.2}
\]

Fix \(\tau\).  For a moved pair
\(p=\{S,\tau S\}\), let \(x_K,y_K\) be the occurrence counts of
\(S,\tau S\) in the left side of component \(K\), and put

\[
z_K=x_K-y_K.
\]

### Lemma 8.1 — orbitwise component gap

\[
\boxed{
(V_{\tau,1}-A_{\tau,1})_p
=2\sum_Kz_K^2
-2\left(\sum_Kz_K\right)^2.}
\tag{8.3}
\]

#### Proof

On the two target coordinates, the component difference is
\((z_K,-z_K)\), up to the harmless global sign convention.  Its squared
norm is \(2z_K^2\); the coherent sum has squared norm
\(2(\sum_Kz_K)^2\). \(\square\)

Let \(s_\tau(F)\) count moved pairs for which

* \(\mu_1(S)=\mu_1(\tau S)=1\); and
* the two unique owner wreaths lie in different genuine
  \(\tau\)-overlay components.

### Theorem 8.2 — exact first-shadow reduction

\[
\boxed{
\left|
V_{\tau,1}-A_{\tau,1}-4s_\tau(F)
\right|
\le40b+60Q_1(F).}
\tag{8.4}
\]

If \(Q_1(F)=0\), then

\[
\boxed{
4s_\tau(F)
\le V_{\tau,1}-A_{\tau,1}
\le4s_\tau(F)+16b
<4s_\tau(F)+64t.}
\tag{8.5}
\]

#### Proof

A singleton--singleton pair in one component has \(z_K=0\) and contributes
zero.  If its occurrences lie in two components, the two nonzero values
are \(1,-1\), and (8.3) contributes \(4\).

Let

\[
\mathcal E=\{S:\mu_1(S)\ne1\}.
\]

If \(h\) is the number of holes, then

\[
\sum_S(\mu_1(S)-1)=b,
\qquad
Q_1\ge2h,
\]

so

\[
|\mathcal E|\le b+Q_1.
\tag{8.6}
\]

Moreover,

\[
\sum_{S\in\mathcal E}\mu_1(S)^2
\le4b+\frac{13}{2}Q_1.
\tag{8.7}
\]

Indeed, the load-two contribution is at most \(4(b+h)\), while for
\(k\ge3\),

\[
k^2\le\frac92(k-1)(k-2).
\]

For an exceptional moved orbit with endpoint loads \(X,Y\), (8.3) gives

\[
\left|(V-A)_p\right|
\le4(X+Y)^2
\le8(X^2+Y^2).
\tag{8.8}
\]

The exceptional orbits are disjoint, and at most
\(|\mathcal E|\) singleton partners must be added.  Equations
(8.6)--(8.8) give

\[
8\left(
\sum_{S\in\mathcal E}\mu_1(S)^2+|\mathcal E|
\right)
\le40b+60Q_1.
\]

This proves (8.4).

If \(Q_1=0\), every load is \(1\) or \(2\), and exactly \(b\) targets
have load \(2\).  A \((2,1)\) orbit contributes between \(0\) and \(8\);
a \((2,2)\) orbit contributes between \(0\) and \(16\).  At most \(b\)
orbits meet a double target.  This proves (8.5). \(\square\)

For fixed \(\tau\), the number of moved first-shadow target pairs is

\[
\binom{2m-1}{m-2}
=\frac{m-1}{2(2m+1)}W
=\Theta(W).
\tag{8.9}
\]

Therefore a Catalan-scale \(q=1\) ceiling at a floor-balanced factor is
equivalent, up to the explicit constants in (8.5), to

\[
s_\tau(F)=O(t).
\tag{8.10}
\]

It forces almost every one of the \(\Theta(W)\) singleton pairs to have
its two unique owners in one actual overlay component.

A genuine termwise counterfamily would be:

> exact factors \(F_m\) with \(Q_1(F_m)=0\), and transpositions
> \(\tau_m\), such that
> \[
> s_{\tau_m}(F_m)=\omega(\operatorname{Cat}_m).
> \]

No such exact-factor family is constructed here.  Abstract separated-owner
patterns do not suffice.

---

## 9. Exact degree-two distance-graph theorem

The preceding criterion controls the full \(q=1\) gap but does not identify
its harmonic location.  The slow \(E_2\) part admits a stronger theorem.

For \(2\le r=m-q\), let

\[
D_{r,2}g(e)=
\sum_{\substack{S\supset e\\|S|=r}}g(S)
\tag{9.1}
\]

be the down-incidence map to coordinate pairs.  For a wreath \(C\), let
\(d_C(e)\in\{1,\ldots,m\}\) be the shorter cyclic distance between the
endpoints of \(e\).  Let \(A_{K,d}(e)\) be the difference between the two
component sides in the number of wreaths with \(d_C(e)=d\).

### Theorem 9.1 — weighted near-antipodal representation

\[
\boxed{
D_{m-q,2}\Delta_{K,q}
=\sum_{\ell=1}^q
\ell\,A_{K,m-q+\ell}.}
\tag{9.2}
\]

Put

\[
\alpha_q=\binom{n-4}{m-q-2}.
\tag{9.3}
\]

Then

\[
\boxed{
\|\Pi_{q,2}\Delta_{K,q}\|_2^2
=\frac1{\alpha_q}
\left\|
\sum_{\ell=1}^q
\ell\,A_{K,m-q+\ell}
\right\|_2^2.}
\tag{9.4}
\]

#### Proof

A pair at cyclic distance \(d\) lies in

\[
h_s(d)=(s-d)_+
\]

cyclic \(s\)-intervals.  The two component sides have identical middle
support and equal row count, hence

\[
\sum_dh_m(d)A_{K,d}=0,
\qquad
\sum_dA_{K,d}=0.
\tag{9.5}
\]

Now

\[
h_{m-q}(d)=h_m(d)-q+g_q(d),
\]

where

\[
g_q(m-q+\ell)=\ell
\quad(1\le\ell\le q),
\qquad
g_q(d)=0
\]

otherwise.  Equation (9.2) follows from (9.5).

The pair module is \(E_0\oplus E_1\oplus E_2\), and Theorem 3.1 kills
the first two levels.  The squared singular value of \(D_{r,2}\) on
\(E_2\) is

\[
\binom{n-2}{r-2}
-2\binom{n-3}{r-3}
+\binom{n-4}{r-4}
=\binom{n-4}{r-2}
=\alpha_q.
\]

This proves (9.4). \(\square\)

The weighted graph on either component side in (9.2) has, per wreath,
weighted degree

\[
2\sum_{\ell=1}^q\ell=q(q+1),
\]

and each edge has weight at most \(q\).

### Corollary 9.2 — unconditional \(E_2\) component bound

\[
\boxed{
V_{\tau,q,2}
\le
\frac{4q^2(q+1)}{\alpha_q}
\sum_Ks_K^2
\le
\frac{4q^2(q+1)t^2}{\alpha_q}.}
\tag{9.6}
\]

#### Proof

Let \(\tau=(uv)\), and let \(a_x,b_x\) be the two weighted stars at
\(u,v\) on one component side.  Relabelling gives the other side, so

\[
\left\|
\sum_{\ell=1}^q\ell A_{K,m-q+\ell}
\right\|_2^2
=2\sum_{x\ne u,v}(a_x-b_x)^2.
\]

Here

\[
a_x,b_x\le qs_K,
\qquad
\sum_xa_x,\sum_xb_x\le q(q+1)s_K.
\]

Therefore

\[
2\sum_x(a_x-b_x)^2
\le2\sum_x(a_x^2+b_x^2)
\le4q^2(q+1)s_K^2.
\]

Use (9.4) and sum \(K\). \(\square\)

For \(q\le A\sqrt m\),

\[
\frac W{\alpha_q}=O_A(1),
\]

so (9.6) becomes

\[
V_{\tau,q,2}
\le C_A\frac{q^2(q+1)}n\,t.
\tag{9.7}
\]

This is not summably small enough on the full Gaussian window.

### Corollary 9.3 — the complete slow \(q=1\) noise is harmless

For \(q=1\),

\[
\alpha_1=\binom{n-4}{m-3},
\]

and the distance-\(m\) pairs of one odd cyclic order form a Hamilton
cycle.  The sharper star bound gives

\[
\boxed{
V_{\tau,1,2}\le\frac{8t^2}{\alpha_1}.}
\tag{9.8}
\]

Moreover,

\[
\frac W{\alpha_1}
=\frac{4(2m+1)(2m-1)}{(m+1)(m-2)}
=16+O(m^{-1}).
\tag{9.9}
\]

Hence

\[
\boxed{
V_{\tau,1,2}
\le
\frac{32(2m-1)}{(m+1)(m-2)}\,t
=O\!\left(\frac tn\right).}
\tag{9.10}
\]

This controls only \(E_2\), not the full expression in (8.5).

---

## 10. Multistep harmonic ledger and commutator no-go

Let transpositions be independent uniform choices and let every component
signing be conditionally fair.  Put

\[
\lambda_j=1-\kappa_j,
\qquad
\rho=\lambda_2=1-\frac2n.
\]

### Theorem 10.1 — exact multistep isotype identity

For every \(j\ge2\),

\[
\boxed{
\begin{aligned}
\mathbb E\|f_{T,q,j}\|_2^2
={}&\lambda_j^T\|f_{0,q,j}\|_2^2\\
&+\frac14\sum_{s<T}
\lambda_j^{T-1-s}\,
\mathbb EV_{s,q,j}.
\end{aligned}}
\tag{10.1}
\]

#### Proof

At time \(s\),

\[
f_{s+1,q,j}=P_{\tau_s}f_{s,q,j}+\xi_{s,q,j},
\]

where the innovation has conditional mean zero and conditional second
moment

\[
\mathbb E(\|\xi_{s,q,j}\|_2^2\mid F_s,\tau_s)
=\frac14V_{s,q,j}.
\]

Equation (3.7) gives

\[
\mathbb E_{\tau_s}\|P_{\tau_s}g\|_2^2
=\lambda_j\|g\|_2^2.
\]

Iterate. \(\square\)

Define the exact nonnegative higher-harmonic rebate

\[
\begin{aligned}
\mathcal D_T={}&
\sum_{q,j\ge3}
\frac{(\rho^T-\lambda_j^T)
\|f_{0,q,j}\|_2^2}{c_q}\\
&+\frac14\sum_{s<T}\sum_{q,j\ge3}
\frac{
(\rho^{T-1-s}-\lambda_j^{T-1-s})
\mathbb EV_{s,q,j}}{c_q}.
\end{aligned}
\tag{10.2}
\]

Then (10.1) is equivalently

\[
\boxed{
\begin{aligned}
\mathbb E\mathcal Q_A(F_T)
={}&\rho^T\mathcal Q_A(F_0)\\
&+\sum_{s<T}\rho^{T-1-s}
\left[
\frac14\mathbb E
\sum_{q,j\ge2}\frac{V_{s,q,j}}{c_q}
-\frac2nB_A
\right]
-\mathcal D_T.
\end{aligned}}
\tag{10.3}
\]

The only component noise not given an extra spectral rebate is \(E_2\).
Innovations born near time \(T\) receive little or no future filtering.

Corollary 9.3 and the geometric sum give, for every horizon \(T\),

\[
\boxed{
\frac14\sum_{s<T}
\rho^{T-1-s}\mathbb EV_{s,1,2}
\le
(1-\rho^T)\frac{nt^2}{\alpha_1}
=(1-\rho^T)\frac W{\alpha_1}t.}
\tag{10.4}
\]

Thus the entire propagated \(q=1,E_2\) noise is at most

\[
\frac{126}{5}t
\quad(m\ge4),
\]

and asymptotically at most

\[
(16+o(1))t.
\tag{10.5}
\]

This is negligible compared with the allowed \(Ht\) floor.

### Fixed words do not manufacture negative noise covariance

For a transposition word fixed before the component signs, unroll the
recurrence as

\[
f_T=Mf_0+\sum_{s<T}Q_s\xi_s,
\tag{10.6}
\]

where \(Q_s\) is the suffix product of coordinate projections.
Conditional martingale orthogonality gives exactly

\[
\boxed{
\mathbb E\|f_T\|_A^2
=\|Mf_0\|_A^2
+\sum_{s<T}\mathbb E\|Q_s\xi_s\|_A^2.}
\tag{10.7}
\]

This does not assert nonnegative covariance for the raw heat increments.
It states that a frozen word with fair signs can only suffix-filter earlier
centered innovations; it creates no negative innovation cross term.

For pairwise commuting transpositions, let \(\ell_i\) be the last
occurrence of generator \(\tau_i\).  Since an innovation born at
\(\tau_i\) lies in \(\ker P_{\tau_i}\), all its earlier occurrences are
killed by the last \(P_{\tau_i}\).  Hence

\[
\boxed{
f_T=P_\Gamma f_0+
\sum_i
\left(\prod_{\ell_j>\ell_i}P_{\tau_j}\right)
\xi_{\ell_i},
\qquad
\Gamma=\langle\tau_1,\ldots,\tau_d\rangle.}
\tag{10.8}
\]

The last innovation of every generator remains.  Repetition refreshes
commuting heat noise; it does not eliminate the terminal wall.

On the exact-factor state space, the fixed-\(\tau\) fair kernel
\(K_\tau\) is the orthogonal projection onto functions constant on
intrinsic \(\tau\)-cells.  Therefore

\[
[K_\tau,K_\sigma]^*
=-[K_\tau,K_\sigma],
\qquad
\boxed{\langle h,[K_\tau,K_\sigma]h\rangle=0.}
\tag{10.9}
\]

A first Markov commutator has no Dirichlet form.  A closed global
coordinate commutator also has zero energy drift because its endpoint is a
relabeling of the starting factor.

### Static subgroup obstruction for \(E_2\)

Let \(G\) be generated by coordinate transpositions.  Its coordinate
orbits are blocks \(B_1,\ldots,B_s\), and

\[
G=S_{B_1}\times\cdots\times S_{B_s}.
\]

Unless the block partition is

\[
\{[n]\}
\quad\hbox{or}\quad
\{\{x\},[n]\setminus\{x\}\},
\tag{10.10}
\]

some union \(B\) has \(2\le|B|\le n-2\).  On a central rank,
\(|S\cap B|\) has at least three feasible values.  The quadratic

\[
|S\cap B|(|S\cap B|-1)
\]

is \(G\)-invariant and has degree at most \(2\); after subtracting its
\(E_0\oplus E_1\) part, a nonzero \(G\)-invariant \(E_2\) vector remains.
Thus \(P_G\) does not annihilate the bad mode.

In the two exceptional cases, the canonical joined ownership partition
has one block:

* for \(G=S_n\), there is one middle-set orbit;
* for the point stabilizer \(S_{n-1}\), there are two middle-set orbits,
  according as the fixed point is present, and every wreath row owns
  \(m\) masks of the first type and \(m+1\) of the second.

Hence:

\[
\boxed{
\begin{gathered}
\text{no fixed transposition subgroup both annihilates }E_2\\
\text{and retains a nontrivial canonical exact component choice.}
\end{gathered}}
\tag{10.11}
\]

This does not exclude extra perfect matchings inside combined supports or
an adaptive policy which changes the factor and recomputes components.

---

## 11. Clean surviving route-specific gates

The aggregate \(A\)-relative question remains:

> **Component-noise ceiling \((\mathrm{CN}_A)\) — UNPROVED.**
> For every fixed \(A\), is there \(C_A<\infty\) such that every exact
> factor and every coordinate transposition satisfy
> \[
> V_{\tau,H}
> \le A_{\tau,H}+C_AH\operatorname{Cat}_m?
> \]

The stronger termwise \(q=1\) restriction, at \(Q_1=0\), is equivalent
up to constants by Theorem 8.2 to the genuine owner-coalescence bound
\((\mathrm{OC}_1)\):

\[
\boxed{s_\tau(F)=O(\operatorname{Cat}_m).}
\tag{11.1}
\]

Statement \((\mathrm{OC}_1)\) is **UNPROVED**.

A counterfamily with \(s_\tau/\operatorname{Cat}_m\to\infty\) would
disprove the termwise \(q=1\) ceiling.  No such exact family is known.

Even \((\mathrm{CN}_A)\) would not prove MWB.  The scale-correct fair
one-step theorem still needs the negative energy term in (4.7).

For multistep fair heat, define

\[
\mathcal N_T=
\frac14\sum_{s<T}\rho^{T-1-s}
\mathbb E\sum_{q,j\ge2}\frac{V_{s,q,j}}{c_q}
-\mathcal D_T.
\tag{11.2}
\]

Equation (10.3) shows that the exact sufficient statement is:

> **Suffix-filtered component restitution
> \((\mathrm{SFCR}_A)\) — UNPROVED.**
> There are \(C_A<\infty\) and \(T=\Theta_A(n)\), uniform in the starting
> exact factor \(F\), such that iid uniform transpositions and
> conditionally fair component signs satisfy
> \[
> \boxed{
> \mathcal N_T
> \le
> (1-\rho^T)B_A
> +C_AH\operatorname{Cat}_m.}
> \tag{11.3}
> \]

It would give an actual integral endpoint with

\[
\mathcal Q_A(F_T)
\le
\rho^T\mathcal Q_A(F_0)
+C_AH\operatorname{Cat}_m.
\tag{11.4}
\]

One \(O(n)\)-step block gives only constant contraction.  From a worst
starting factor, reaching the \(H\operatorname{Cat}_m\) scale requires
\(O_A(n\log W)=O_A(n^2)\) total steps, or one may apply a suitable
inequality at a global minimizer.

Theorem 10.1 and Corollary 9.3 remove the entire \(q=1,E_2\) part of
\((\mathrm{SFCR}_A)\).  Its exact remaining content is:

* suffix-filtered \(E_2\) weighted-distance-graph noise for \(q\ge2\);
* recent \(E_{j\ge3}\) innovations which have not yet earned the rebate
  in (10.2); and
* one common integral factor choice across all ranks.

A genuinely adaptive commutator could, in principle, correlate future
suffixes with earlier signs and create negative cross-time covariance.
No such exact circuit is constructed.  Section 10 rules out a Dirichlet
gain from a first Markov commutator and rules out simultaneous annihilation
of the full ambient \(E_2\) module by a nontrivial canonical static group
component product.  It does not rule out a fixed fair word satisfying
\((\mathrm{SFCR}_A)\) through suffix filtering, a correlated Haar choice,
or a nonfair exact-factor circuit.

---

## 12. Adversarial audit

### Exact factors versus abstract vectors

Every switching-cube, distance-graph, and owner-coalescence theorem above
uses genuine exact factors.  The vectors in Section 7 are deliberately
marked formal; they refute only a representation-and-margins proof, not an
exact-factor implication.

### What the exact cube proves

Equation (5.1) proves zero mean gap inside a cell.  It does not exhibit a
corner with \(V-A\gg H\operatorname{Cat}_m\), so it is not a counterexample
to \((\mathrm{CN}_A)\).

### Connected overlays

If an overlay is connected, there is one component and

\[
V_{\tau,H}=A_{\tau,H}.
\]

It exactly saturates the proposed ceiling and gives no integral smoothing.
It does not disprove the ceiling.

### The Boolean-\(E_2\) theorem

The sparse Boolean theorem refutes a bound on \(R_H\) relative to the
floor baseline \(4(n-1)B_A\).  It does not refute a bound on
\(R_H-D_H\), or on \(V_{\tau,H}-A_{\tau,H}\).

### Scope of the \(q=1\) theorem

Theorem 8.2 controls the full \(q=1\) gap but leaves the owner statistic
\(s_\tau\) open.  Corollary 9.3 controls only its \(E_2\) projection;
the \(E_{j\ge3}\) terminal noise remains part of
\((\mathrm{SFCR}_A)\).

The report does not assert that exactly floor-balanced first shadows
\(Q_1=0\) are realized by exact wreath factors for every \(m\).

A large positive \(q=1\) gap would refute a termwise \(q=1\) ceiling, but
would not by itself refute an aggregate Gaussian-window inequality if
deeper ranks supplied negative gaps.

### Scope of the commutator no-go

The frozen-word identity assumes conditionally fair centered signs.
The subgroup conclusion concerns the canonical joined component-side
mechanism.  Neither excludes additional perfect matchings, correlated
nonfair sign choices, palindromic products, or state-dependent adaptive
recomputation.

### Logical strength

\((\mathrm{CN}_A)\) is only a noise ceiling.  It lacks the
\(-\eta_A\mathcal Q_A/n\) drift needed for MWB.
\((\mathrm{SFCR}_A)\) is a sufficient multistep restitution theorem, not
known equivalent to MWB.

---

## 13. Final theorem-level status

The harmonic decomposition is exact:

\[
\boxed{
\text{component noise begins at }E_2,\quad
\kappa_2=\frac2n,\quad
\mathbb E_{\rm cell}A_{q,j}=V_{q,j}.}
\]

The first-shadow slow mode is completely controlled:

\[
\boxed{
V_{\tau,1,2}=O(\operatorname{Cat}_m/n),\qquad
\text{discounted total}=O(\operatorname{Cat}_m).}
\]

But the full one-step ceiling is neither proved nor disproved by a genuine
exact-factor family.  At exact first-shadow floor balance, its stronger
termwise \(q=1\) restriction is equivalent to the explicit
owner-coalescence problem (11.1).  Across the Gaussian window, the
remaining slow mode is the weighted near-antipodal \(E_2\) graph in
(9.2), together with recent higher-harmonic lattice restitution.

First commutators and full-\(E_2\)-annihilating canonical static subgroup
products do not remove it.  Suffix filtering by a fixed fair word,
correlated exact choices, and adaptive state-dependent component
recomputation remain open routes to \((\mathrm{SFCR}_A)\).
