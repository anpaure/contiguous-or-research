# Stabilizer-shell decomposition of the centered second-incidence covariance

**Date:** 2026-08-06  
**Method:** fixed-count covariance, Johnson stabilizer orbits, exact
Cartesian-product spectral gaps, and complete-row boundary pairing; no
computation or search  
**Status:** unconditional deterministic reduction and radial closure for
the authenticated FIFO track table. The centered survivor covariance
splits into a radial rooted-collision energy and an angular boundary-star
energy. The radial term is bounded pointwise by \(Ck^{-2}g_x^2\). The
angular inverse gap is \(O(d)\), not \(O(k)=O(d^2)\), because the relevant
graph is a stabilizer shell. The cumulative stopped boundary-star estimate
is not proved here.

This note continues
MATH_THEOREM_CONDITIONED_LINEAR_HIT_COVARIANCE_AND_TWO_HIT_REMAINDER_20260806.md.

## 1. Same-layer blocker shells

Fix an output resource \(x\) and one blocker-resource Johnson layer

\[
                         \Omega_q={ [k]\choose q},
\qquad \epsilon k\le q\le(1-\epsilon)k.
\tag{1.1}
\]

For \(0\le\ell\le\min(q,k-q)\), put

\[
 \Omega_{x,\ell}
 =\{y\in\Omega_q:d_J(x,y)=\ell\}.
\tag{1.2}
\]

Writing \(y=(x-A)\cup B\), the map

\[
 y\longleftrightarrow
 (A,B)\in {x\choose\ell}\times{[k]-x\choose\ell}
\tag{1.3}
\]

identifies \(\Omega_{x,\ell}\) with a product of two Johnson layers.
The stabilizer

\[
                         \operatorname {Sym}(x)\times
                         \operatorname {Sym}([k]-x)
\tag{1.4}
\]

acts transitively on every shell and fixes \(x\) literally.

Let \(P_{x,\ell}\) be the Markov operator which, with probability \(1/2\),
makes one Bernoulli--Laplace exchange in \(A\), and with probability
\(1/2\), makes one in \(B\). Its stationary measure is uniform on the
shell.

### Lemma 1.1 (shell gap)

For \(1\le\ell<\min(q,k-q)\),

\[
 \boxed{
 \operatorname {gap}(P_{x,\ell})
 ={1\over2}\min\left\{
 {q\over\ell(q-\ell)},
 {k-q\over\ell(k-q-\ell)}
 \right\}.}
\tag{1.5}
\]

In particular, uniformly for \(\ell\le C_0d=o(k)\),

\[
                         \operatorname {gap}(P_{x,\ell})^{-1}
 \le C_\epsilon\ell\le C_\epsilon C_0d.
\tag{1.6}
\]

#### Proof

The normalized one-exchange walk on \({[n]\choose\ell}\) has first
nonzero gap \(n/(\ell(n-\ell))\). The spectrum of the half-half product
operator is the average of the two coordinate spectra, so its first
nonzero gap is half the smaller coordinate gap. This gives (1.5), and
centrality plus \(\ell=o(k)\) gives (1.6). \(\square\)

Thus the \(O(k)\) inverse gap of the full central Johnson graph is the
wrong cost for angular blocker fluctuations. Within one distance shell,
the inverse gap is only \(O(\ell)\).

## 2. Radial and angular parts

Fix one accepted-edge stratum \(\sigma\), and let
\(\lambda_{x,y}\) be the linear-hit coefficient from (2.3) of the
conditioned covariance note. For every nonempty shell define

\[
 m_{x,\ell}={1\over|\Omega_{x,\ell}|}
       \sum_{y\in\Omega_{x,\ell}}\lambda_{x,y},
\qquad
 v_{x,y}=\lambda_{x,y}-m_{x,d_J(x,y)}.
\tag{2.1}
\]

Put

\[
 \begin{aligned}
 \operatorname {Rad}_x(\lambda)
 &=\sum_\ell|\Omega_{x,\ell}|m_{x,\ell}^2
   =\sum_\ell
       {(\sum_{y\in\Omega_{x,\ell}}\lambda_{x,y})^2
        \over|\Omega_{x,\ell}|},\\
 \operatorname {Ang}_x(\lambda)
 &=\sum_{\ell}
   \left\langle v_x,(I-P_{x,\ell})v_x
   \right\rangle_{\ell^2(\Omega_{x,\ell})}.
 \end{aligned}
\tag{2.2}
\]

The singleton shell contributes only to \(\operatorname {Rad}\).

Let \(K_x^\sigma\) be the unnormalized conditioned covariance matrix in
this stratum. Assume:

1. every accepted edge in \(\sigma\) contains at most \(C_sd\) blockers
   of the present type; and
2. the current one-resource loads obey
   \(Y_{y\mid\bar x,\sigma}\le C_Y\).

### Theorem 2.1 (radial-angular covariance aperture)

If the nonrigid blocker incidences are supported on shells
\(\ell\le C_0d\), then

\[
 \boxed{
 \lambda_x^*K_x^\sigma\lambda_x
 \le C d\,\operatorname {Rad}_x(\lambda)
      +C d^2\,\operatorname {Ang}_x(\lambda).}
\tag{2.3}
\]

Rigid, macroscopically separated, or cross-half shells may be retained as
an additional named exceptional term (including both their radial and
angular parts); no smallness of those shells is asserted by (2.3).

#### Proof

Write \(\lambda=m+v\), with \(m\) shell-constant and \(v\) shell-mean
zero. Positivity gives

\[
 \lambda^*K\lambda\le2m^*Km+2v^*Kv.
\tag{2.4}
\]

For any vector \(u\), deterministic row size and Cauchy--Schwarz give

\[
 \begin{aligned}
 u^*K_x^\sigma u
 &\le\sum_{G\in\sigma,\ x\notin G}
       a_G\left(\sum_{y\in G}u_y\right)^2\\
 &\le C_sd\sum_yY_{y\mid\bar x,\sigma}u_y^2
 \le C_sdC_Y\sum_yu_y^2.
 \end{aligned}
\tag{2.5}
\]

For \(u=m\), its square norm is exactly \(\operatorname {Rad}_x\).
For \(u=v\), apply Lemma 1.1 on every shell:

\[
 \sum_{y\in\Omega_{x,\ell}}v_{x,y}^2
 \le C\ell
 \left\langle v_x,(I-P_{x,\ell})v_x\right\rangle.
\tag{2.6}
\]

Since \(\ell\le C_0d\), (2.4)--(2.6) prove (2.3).
\(\square\)

The same statement holds for unequal resource shores after replacing
\(\ell\) by the finite stabilizer-orbit signature. Every nonrigid FIFO
signature is a product of a bounded number of Johnson slices of size
parameter \(O(d)\), so its product gap has inverse \(O(d)\). Rigid
signatures stay in the named exceptional bank.

## 3. Exact boundary-star identity for the angular edges

Let \(\tau\) be one of the coordinate transpositions generating
\(P_{x,\ell}\). Then

\[
                         \tau x=x,
\qquad
                         \tau y=z
\tag{3.1}
\]

for adjacent \(y,z\) in the same stabilizer shell.

Let \(\bar\mu_A\) denote the structural composite coefficient before the
live indicator is applied, and let \(l_A\in\{0,1\}\) indicate that the
literal row \(A\) is live. On a complete coordinate orbit,

\[
 \bar\mu_{\tau A}=\bar\mu_A,\quad
 t_{\tau A}=t_A,\quad
 z_{\tau A}(x)=z_A(x),\quad
 \chi_{\tau A}(z)=\chi_A(y).
\tag{3.2}
\]

### Lemma 3.1 (angular differences are stopped boundary stars)

For every generator (3.1),

\[
 \boxed{
 \lambda_{x,y}-\lambda_{x,z}
 =\sum_A\bar\mu_A t_Az_A(x)\chi_A(y)
          (l_A-l_{\tau A}).}
\tag{3.3}
\]

Thus rows for which both \(A,\tau A\) are live, or both are dead, cancel
exactly. Only the stopped symmetric-difference boundary survives.

#### Proof

Start from

\[
 \lambda_{x,z}
 =\sum_B\bar\mu_Bt_Bz_B(x)\chi_B(z)l_B
\]

and substitute \(B=\tau A\). Equations (3.2) turn this into

\[
 \lambda_{x,z}
 =\sum_A\bar\mu_At_Az_A(x)\chi_A(y)l_{\tau A}.
\]

Subtract from the corresponding formula for \(\lambda_{x,y}\).
\(\square\)

This is the point at which the stabilizer shell is essential. A general
transposition taking \(y\) to \(z\) also sends \(x\) to \(\tau x\), and
then (3.3) acquires a separate output-transport term. The shell generator
fixes \(x\), so no such term occurs.

## 4. The radial row closes pointwise

For a composite row \(A\), an output state \(x\), and one same-shore
blocker layer, put

\[
 c_{A,x,\ell}
 =|\{y\in S_A\cap\Omega_q:d_J(x,y)=\ell\}|.
\tag{4.1}
\]

The authenticated atomic normal form has a constant number of lower and
owner FIFO tracks in each macro half, a constant last-two fan, and a
constant number of macro halves in one composite row. Relative to a fixed
state \(x\), its distance table has only the following forms:

1. on the track containing \(x\), at most two states occur at each
   distance;
2. on a different same-half track, all but one distance have constant
   multiplicity, while a plateau of multiplicity \(m\) may occur only at
   distance at least \(m-O(1)\);
3. the last-two fan has constant size; and
4. opposite-half tracks lie at distance \(\Theta(k)\).

These are exactly the track classes used in the proof of the sharp first
collision estimate in the rank-compensated doublet note.

### Lemma 4.1 (pointwise track aperture)

Uniformly over every literal composite row and output occurrence,

\[
 \boxed{
 \sum_{\ell\ge1}{c_{A,x,\ell}^2\over
 {q\choose\ell}{k-q\choose\ell}}
 \le {C\over k^2}+e^{-ck}.}
\tag{4.2}
\]

The analogous unequal-shore orbit sum is exponentially smaller.

#### Proof

For a central layer,

\[
 N_\ell={q\choose\ell}{k-q\choose\ell},
\qquad N_1=\Theta(k^2),
\tag{4.3}
\]

and \(N_\ell\) is increasing for \(\ell=O(d)=o(k)\). A simple track
therefore contributes

\[
 C\sum_{\ell\ge1}N_\ell^{-1}=O(k^{-2}).
\tag{4.4}
\]

For a plateau of multiplicity \(m\) at distance
\(\ell\ge m-C_0\), absorb the constant shift into the finitely many cases
\(m\le2C_0\). For larger \(m\),

\[
 {m^2\over N_\ell}
 \le m^2\left({Cm\over k}\right)^{2m}
 =o(k^{-2}).
\tag{4.5}
\]

There are only constantly many tracks and plateaux. The fan changes the
constant in (4.4). At distance \(\Theta(k)\), the orbit size is
\(\exp[\Theta(k)]\), while a row has only \(O(d)\) roles, giving the last
term in (4.2). Unequal-shore stabilizer orbits are at least as large as
the private-tail or containment orbits used in the first-collision audit,
and are exponentially negligible. \(\square\)

### Proposition 4.2 (pointwise radial second-incidence bound)

For the literal coefficient \(\lambda\),

\[
 \boxed{
                         \operatorname {Rad}_x(\lambda)
 \le {C\over k^2}g_x^2+e^{-ck}g_x^2.}
\tag{4.6}
\]

#### Proof

For one shell, set

\[
 L_{x,\ell}=\sum_{y\in\Omega_{x,\ell}}\lambda_{x,y}
 =\sum_A\mu_Az_A(x)t_Ac_{A,x,\ell}.
\tag{4.7}
\]

Weighted Cauchy--Schwarz gives

\[
 L_{x,\ell}^2
 \le\left(\sum_A\mu_Az_A(x)t_A\right)
      \left(\sum_A\mu_Az_A(x)t_Ac_{A,x,\ell}^2\right).
\tag{4.8}
\]

Divide by \(N_\ell\), sum \(\ell\), and apply Lemma 4.1. Since
\(t_A\le C_t\), both coefficient sums in (4.8) are at most a fixed
multiple of \(g_x\). This proves (4.6). \(\square\)

Let \(\mathcal P_i^{\rm row}=\sum_Ac_i(A)\) be the current nonnegative
future-potential mass of the composite family under consideration. For
the generic pair family this is the summand mass of \(\mathcal P_i\).
For a root or marked family, retain as an explicit premise the
corresponding scaled occupation estimate

\[
 \mathbb E\sum_{i<\tau}{\mathcal P_i^{\rm row}\over X_i}
 \le C\mathsf A.
\tag{4.9a}
\]

This distinction is necessary because an uncentered root second moment
may contain a large mean-square baseline. On one step,

\[
 \sum_A\mu_A\le C\mathcal P_i^{\rm row},
\qquad
 \sum_xg_x=\sum_A\mu_A|U_A^\circ\cap T|
 \le Cd\mathcal P_i^{\rm row}.
\tag{4.9}
\]

The first inequality uses
\(\mu_A=c_i(A)R_i(A)\), \(R_i(A)=\exp[O(d/X_i)]=O(1)\), and the second is
the literal row-size bound.

Because \(c_x=\beta_TY_x\) and
\(\sum_x(g_x-c_x)=0\),

\[
 \sum_x{g_x^2\over c_x}
 =\sum_xc_x+\Psi_i
 =\sum_xg_x+\Psi_i.
\tag{4.10}
\]

### Corollary 4.3 (RAD4 is absorbed)

On the stopped interval \(k=\Theta(d^2)\), \(h_iX_i=\Theta(1)\),

\[
 \boxed{
 {d\over X_i}\sum_x{\operatorname {Rad}_x(\lambda)\over c_x}
 \le {C\over d^2}{\mathcal P_i^{\rm row}\over X_i}
      +{C\over d^3}h_i\Psi_i
      +e^{-ck}\left({\mathcal P_i^{\rm row}\over X_i}
                    +h_i\Psi_i\right).}
\tag{4.11}
\]

Consequently, for the pair family (and for every other family satisfying
either (4.9a) or the corresponding small-cap bound), the
future-potential estimate and a fixed fraction of the direct chi-square
service give

\[
                         \operatorname {RAD4}\le C\mathsf A.
\tag{4.12}
\]

#### Proof

Insert (4.6) into the left side and use (4.10):

\[
 {Cd\over k^2X_i}\left(\sum_xg_x+\Psi_i\right).
\]

Apply (4.9), \(k=\Theta(d^2)\), and \(X_i^{-1}=\Theta(h_i)\).
This gives (4.11). If (4.9a) is available, sum it directly. Otherwise the
small-cap bound
\(\sup_{i<\tau}\mathcal P_i^{\rm row}\le C\mathsf A\), together with the
deterministic clock estimate

\[
                         \sum_{i<\tau}{1\over X_i}=O(\log d),
\]

costs only \(O((\log d)/d^2)\mathsf A=O(\mathsf A)\) because of the first
factor in (4.11). Finally absorb the \(O(d^{-3})\) fraction of
\(\sum h_i\Psi_i\). \(\square\)

Thus no new stopped PC transfer is required for the radial part. The
pointwise literal track aperture is stronger than the averaged
first-collision identity needed by ROc.

## 5. The exact remaining angular coefficient row

Combining Theorem 2.1 with the centered covariance identity reduces the
linear part of SCOV4 to:

\[
 \begin{aligned}
 \operatorname {RAD4}
 &=\mathbb E\sum_{i<\tau}{d\over X_i}
   \sum_{x,\sigma}{\operatorname {Rad}_{x,i}(\lambda)
   \over c_x},\\
 \operatorname {ANG4}
 &=\mathbb E\sum_{i<\tau}{d^2\over X_i}
   \sum_{x,\sigma}{\operatorname {Ang}_{x,i}(\lambda)
   \over c_x}.
 \end{aligned}
\tag{5.1}
\]

Corollary 4.3 proves the first estimate below. The sole remaining
coefficient estimate is the second:

\[
                         \operatorname {RAD4}
                         +\operatorname {ANG4}
 \le C\mathsf A.
\tag{5.2}
\]

Their structures are now different and explicit.

* \(\operatorname {RAD4}\) is a sum of squared shell codegrees divided by
  shell sizes. In the pristine one-macro orbit this is exactly the
  first-collision expression

  \[
  \sum_\ell{\bar c_\ell^2\over
  {q\choose\ell}{k-q\choose\ell}}=O(k^{-2})=O(d^{-4}).
  \tag{5.3}
  \]

  Proposition 4.2 supplies the stronger pointwise composite-row bound,
  and Corollary 4.3 closes its stopped normalization.

* \(\operatorname {ANG4}\) is, by Lemma 3.1, a squared star of
  first-kill boundary rows under transpositions that fix the output root.
  The spectral cost is only \(d^2\): one factor \(d\) from accepted-edge
  size and one from the shell inverse gap. The raw private first-entry
  scale \(O(d^{-3})\) therefore has one spare factor \(d^{-1}\), provided
  the boundary-star coefficients coalesce capacity-faithfully.

The final phrase is a genuine gate. Complete-row conjugation pays each
full row switch with its literal first-kill coefficient, but (3.3) squares
a sum of rows sharing the output \(x\). Passing from the diagonal
first-entry ledger to this same-root star requires either:

1. a positive-operator capacity aperture;
2. a rooted-star square already present in the marked ROc ledger; or
3. a direct Schur bound for the literal boundary matrix.

No trace or unweighted switch count is sufficient.

### 5.1 The smallest sufficient boundary-star aperture

Let \(\mathcal B_i^{\rm star}\ge0\) be an explicitly priced excess. The
coefficient-faithful angular statement needed here is

\[
 \boxed{
 \sum_{x,\sigma}{\operatorname {Ang}_{x,i}(\lambda)\over c_x}
 \le {C\over d^3}\sum_x{g_x^2\over c_x}
      +\mathcal B_i^{\rm star},}
\tag{BCAP}
\]

together with

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{d^2\over X_i}
             \mathcal B_i^{\rm star}
 \le C\mathsf A.}
\tag{5.4}
\]

Under these two rows, ANG4 closes:

\[
 \begin{aligned}
 {d^2\over X_i}
 \sum_{x,\sigma}{\operatorname {Ang}_{x,i}(\lambda)\over c_x}
 &\le {C\over dX_i}\left(\sum_xg_x+\Psi_i\right)
      +{d^2\over X_i}\mathcal B_i^{\rm star}\\
 &\le {C\mathcal P_i^{\rm row}\over X_i}
      +{C\over d}h_i\Psi_i
      +{d^2\over X_i}\mathcal B_i^{\rm star}.
 \end{aligned}
\tag{5.5}
\]

The pair/root occupation estimate, a fixed \(O(d^{-1})\) fraction of
direct chi-square service, and (5.4) prove
\(\operatorname {ANG4}\le C\mathsf A\).

The power \(d^{-3}\) in BCAP is exact for this route: the deterministic
fixed-count and shell-gap losses total \(d^2\), leaving an absorbable
\(d^{-1}\) service fraction.

### 5.2 Why current complete-row data do not imply BCAP

There is a minimal stopped-fibre obstruction. Take one output \(x\) with
\(c_x=g_x=1\). In one blocker shell, retain a single positive structural
row \(A\) of unit coefficient through \(x,y\), and declare every
coordinate mate \(\tau A\) unavailable. Supply all ordinary physical
one-resource loads by disjoint rows, so the good-load interval remains
valid. Equal structural coefficients on the complete orbit and the exact
identity (3.3) still hold.

The blocker profile is a point mass:

\[
                         \lambda_{x,y}=1,\qquad
                         \lambda_{x,z}=0\quad(z\ne y).
\tag{5.6}
\]

Its normalized shell Dirichlet energy is a fixed positive multiple of one,
whereas

\[
                         d^{-3}\sum_x{g_x^2\over c_x}=d^{-3}.
\tag{5.7}
\]

Thus the homogeneous form of BCAP fails by \(\Theta(d^3)\). This is the
adjoint same-output version of live private-degree collapse. It does not
contradict complete-row blocker conjugation: that theorem prices the one
individual killed/live switch, while BCAP asks to coalesce all persistent
boundary responses through \(x\).

Therefore the exact remaining task is not another incidence count. It is
one of:

* prove that such angular concentration is charged, at its first birth,
  by \(\mathcal B_i^{\rm star}\) satisfying (5.4);
* maintain a stopped positive-operator aperture that rules it out; or
* add the boundary-star future potential whose service pays its
  occupation.

## 6. Proof boundary

The full-graph \(O(k)\) Poincaré loss and its output-transport defect are
not intrinsic. Stabilizer shells give the proof-safe decomposition:

\[
 \boxed{\text{SCOV4}
 \quad\longrightarrow\quad
 \text{radial rooted collision}
 +\text{angular fixed-root boundary star}.}
\]

All deterministic factors are now favorable: \(d\) for fixed-count
covariance and at most \(d\) for the angular inverse gap. The remaining
work is coefficient-faithful:

* prove BCAP with (5.4), equivalently coalesce the angular boundary stars
  without losing the spare \(d^{-1}\).

Those are narrower than the original uncentered fourth-order PINC4
estimate, but they are not proved in this note.
