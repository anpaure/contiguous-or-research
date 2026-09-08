# AA exploration: target-correlated component discrepancy with the exact floor

Date: 2026-07-25

## 0. Verdict

Fix \(A_0>0\), put

\[
n=2m+1,
\qquad
\mathsf W=\binom{n}{m},
\qquad
H=\lceil A_0\sqrt m\rceil,
\qquad
\operatorname{Cat}_m=\frac{\mathsf W}{n},
\]

and take \(m\) sufficiently large that \(H<m\).  This report studies one
genuine ownership overlay at a time.  Every terminal sign vector below
chooses a complete side of every genuine ownership component and is
therefore one literal integral exact factor through the entire window
\(q\le H\).

The frozen exact-middle existence theorem guarantees that the exact-factor
fibre used below is nonempty.

The outcome is a restricted theorem and a sharp incompatibility statement.

1. There are two different discrete floors.  The load floor is already
   subtracted in the collision energy \(\Psi_H\).  For one ownership
   overlay there is a second, targetwise signing floor

   \[
   B_H^{\rm tar}
   =\sum_p\alpha_p
      \min_{\sigma\in\{\pm1\}^{\mathscr K}}
      (z_p\cdot\sigma)^2.
   \]

   If \(\beta_H\) is the best value obtained with one sign per genuine
   component, then

   \[
   \boxed{
   A_H-\beta_H
   =(A_H-B_H^{\rm tar})
    -(\beta_H-B_H^{\rm tar}).}
   \tag{0.1}
   \]

   The first term is the ideal gain obtained by optimizing every target
   separately.  The second is exactly the loss caused by requiring one
   common component signing.

2. Gauging every target row by one of its local minimizers produces a new
   target-labelled signed graph on the component vertices.  If \(S_+\) is
   its total positive constraint weight and \(\delta_+\) its signed
   vector-SDP defect, then a Gaussian hyperplane produces one genuine exact
   child and

   \[
   \boxed{
   \beta_H-B_H^{\rm tar}
   \le \mathfrak f_+
   \le \sqrt{S_+\delta_+}.}
   \tag{0.2}
   \]

   Here \(\mathfrak f_+\) is the exact weighted frustration of the positive
   target constraints.  The constant in (0.2) is \(1\).  The total weight
   has the exact floor-subtracted formula

   \[
   \boxed{
   S_+=\sum_p\alpha_p(L_p^2-b_p).}
   \tag{0.3}
   \]

3. Consequently the following is a proved, exact-factor sufficient
   condition for the requested descent:

   \[
   \boxed{
   A_H-B_H^{\rm tar}-\sqrt{S_+\delta_+}
   \ge
   \eta\Psi_H(F)-C H\operatorname{Cat}_m.}
   \tag{0.4}
   \]

   Under (0.4), one common signing satisfies

   \[
   \boxed{
   R_H(\varepsilon)
   \le A_H-\eta\Psi_H(F)+C H\operatorname{Cat}_m.}
   \tag{0.5}
   \]

   One of its two antipodal exact children then satisfies

   \[
   \boxed{
   \Psi_H(F_*)
   \le
   \left(1-\frac\eta8\right)\Psi_H(F)
   +\frac C8H\operatorname{Cat}_m.}
   \tag{0.6}
   \]

   For a transposition the two antipodes are relabellings, so (0.6) holds
   for either one and the energy identity is individual rather than merely
   averaged.

4. Partial coloring and deterministic conditional expectations give valid
   exact-factor certificates, but no extra move freedom.  For common means
   \(x_K\in[-1,1]\),

   \[
   \mathbb E R_H
   =\|Dx\|_2^2+
     \sum_K(1-x_K^2)\|d_K\|_2^2.
   \tag{0.7}
   \]

   This expression is affine in every coordinate separately, hence its
   minimum on the box is exactly \(\beta_H\).  Conditional expectations
   derandomize a supplied certificate; optimizing the biases is the
   original signed Max-Cut problem in another form.

5. Targetwise optimization cannot survive arbitrary target or depth
   cancellation.  The expected residual of every legal common-sign law
   (equivalently, its expected antipodal average) sees only the aggregate
   off-diagonal Gram coefficients

   \[
   w_{KL}
   =\sum_{q\le H}\frac{
      \langle\Delta_{K,q},\Delta_{L,q}\rangle_2}{c_q}
   =\sum_p\alpha_pz_{pK}z_{pL}.
   \tag{0.8}
   \]

   If all \(w_{KL}=0\), then \(R_H(\varepsilon)\) is constant on the whole
   genuine component cube.  No correlated law, SDP hierarchy, partial
   coloring, or conditional-expectation rule can lower the residual or the
   antipodal average in (2.6).  For a transposition overlay, where
   antipodes have equal energy, no such rule can improve the factor.

6. The report gives same-depth and cross-depth formal arrays with
   \(B_H^{\rm tar}=0\) but \(A_H=\beta_H=\Theta(\mathsf W)\).  They obey the
   stated row-level integrality, parity, weight, incidence, and nonnegative
   pair-table constraints, but are **not proved to be wreath-realizable**.
   They therefore obstruct black-box discrepancy/SDP arguments, not the
   contiguous-OR conjecture.

7. No unconditional Catalan-scale theorem is proved.  The missing genuine
   statement must control, for the same overlay, both the visible target
   gain \(A_H-B_H^{\rm tar}\) and the synchronization loss
   \(\beta_H-B_H^{\rm tar}\).  The quadratic theorem would close the
   fixed-window unlabelled-overload/MWB route if established uniformly.  It
   does not by itself prove the stronger packet statement \(\mathrm{FSP}_A\),
   and it supplies no \(\mathrm{PTAD}_A\) chronology.

The rest proves these assertions and audits every normalization and scope.

## 1. Exact load floor and collision energy

For \(1\le q\le H\), put

\[
N_q=\binom n{m-q},
\qquad
c_q=\left\lfloor\frac{\mathsf W}{N_q}\right\rfloor,
\qquad
r_q=\mathsf W-c_qN_q.
\tag{1.1}
\]

Every exact factor \(F\) has a depth-\(q\) load vector

\[
\mu_{F,q}=(\mu_{F,q}(S))_{S\in\binom{[n]}{m-q}},
\qquad
\sum_S\mu_{F,q}(S)=\mathsf W.
\tag{1.2}
\]

The minimum possible integral squared norm subject only to this total is

\[
M_q^{\rm fl}
=(N_q-r_q)c_q^2+r_q(c_q+1)^2.
\tag{1.3}
\]

Define the collision excess

\[
\Phi_q(F)
=\sum_S\binom{\mu_{F,q}(S)}2
 -\left[
 (N_q-r_q)\binom{c_q}2
 +r_q\binom{c_q+1}2
 \right].
\tag{1.4}
\]

Since the total load is fixed,

\[
\Phi_q(F)
=\frac12\left(\|\mu_{F,q}\|_2^2-M_q^{\rm fl}\right).
\tag{1.5}
\]

The half-normalized floor-subtracted energy used throughout this report is

\[
\boxed{
\Psi_H(F)
=\sum_{q\le H}\frac{\Phi_q(F)}{c_q}
=\frac12\sum_{q\le H}
  \frac{\|\mu_{F,q}\|_2^2-M_q^{\rm fl}}{c_q}.}
\tag{1.6}
\]

Thus the full squared floor energy in some earlier reports is
\(\mathcal Q_H=2\Psi_H\).  This distinction accounts for the factors
(1/8) and (1/4) in later heat identities.

For completeness, define the lower and upper balanced deviations

\[
D_q(F)=\sum_S(c_q-\mu_{F,q}(S))_+,
\qquad
E_q(F)=\sum_S(\mu_{F,q}(S)-c_q-1)_+,
\tag{1.7a}
\]

and define balanced overload by

\[
O_q(F)=\max\{D_q(F),E_q(F)\}.
\tag{1.7b}
\]

The exact identity

\[
2\Phi_q(F)
=\sum_S(\mu_{F,q}(S)-c_q)
       (\mu_{F,q}(S)-c_q-1)
\tag{1.7c}
\]

shows that \(\Phi_q(F)\ge D_q(F)+E_q(F)\): a value \(c_q-d\)
contributes \(d(d+1)/2\ge d\), and a value \(c_q+1+e\) contributes
\(e(e+1)/2\ge e\).  Hence

\[
O_q(F)\le\Phi_q(F),
\tag{1.7}
\]

and therefore

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}\le\Psi_H(F).
\tag{1.8}
\]

For fixed \(A_0\), the ratios

\[
\frac{\mathsf W}{N_q}
=\prod_{i=1}^q\frac{m+1+i}{m-q+i}
\tag{1.9}
\]

are bounded above by a constant depending only on \(A_0\), uniformly for
\(q\le H\) and all sufficiently large \(m\).  Thus
\(1\le c_q\le K^{\rm load}_{A_0}\), and (1.8) also gives

\[
\sum_{q\le H}O_q(F)\le K^{\rm load}_{A_0}\Psi_H(F).
\tag{1.10}
\]

No component-side floor introduced later is part of (1.6); those are
overlay-dependent discrepancy floors.

## 2. One genuine overlay and the weighted vector-discrepancy problem

Let \(F\) be an exact factor and let \(G=\sigma F\) be a coordinate
relabeling.  Form the bipartite middle-ownership overlay between \(F\) and
\(G\), cancel common wreaths, and let \(\mathscr K\) be its connected
components.  For \(K\in\mathscr K\), write \(L_K\subset F\) and
\(R_K\subset G\) for its two complete sides, oriented so that choosing all
left sides gives \(F\).  Put

\[
\Delta_{K,q}
=\mu_q(L_K)-\mu_q(R_K).
\tag{2.1}
\]

For every sign vector \(\varepsilon\in\{\pm1\}^{\mathscr K}\), choosing
\(L_K\) when \(\varepsilon_K=+1\) and \(R_K\) when
\(\varepsilon_K=-1\) gives one integral exact factor \(F_\varepsilon\),
with

\[
\mu_q(F_\varepsilon)
=\frac{\mu_q(F)+\mu_q(G)}2
 +\frac12\sum_K\varepsilon_K\Delta_{K,q}.
\tag{2.2}
\]

The antipodal factor \(F_{-\varepsilon}\) chooses the other complete side
in every component.  Define

\[
R_H(\varepsilon)
=\sum_{q\le H}\frac1{c_q}
  \left\|\sum_K\varepsilon_K\Delta_{K,q}\right\|_2^2,
\tag{2.3}
\]

\[
A_H
=R_H(\mathbf1)
=\sum_{q\le H}\frac{
  \|\mu_q(F)-\mu_q(G)\|_2^2}{c_q},
\tag{2.4}
\]

and

\[
\beta_H=\min_{\varepsilon\in\{\pm1\}^{\mathscr K}}
R_H(\varepsilon).
\tag{2.5}
\]

The notation \(R_H(\varepsilon)\) in (2.3) is the signed residual for this
one overlay.  It must not be confused with the all-transposition
self-energy also denoted \(R_H(F)\) in other reports.

### The exact heat identity

The parallelogram identity in (2.2), the factor-independent floor (1.3),
and relabeling invariance \(\Psi_H(G)=\Psi_H(F)\) give

\[
\boxed{
\Psi_H(F_\varepsilon)+\Psi_H(F_{-\varepsilon})
=2\Psi_H(F)+\frac14
  \bigl(R_H(\varepsilon)-A_H\bigr).}
\tag{2.6}
\]

Therefore one of the two integral exact antipodes satisfies

\[
\boxed{
\Psi_H(F_*)
\le\Psi_H(F)+\frac18
\bigl(R_H(\varepsilon)-A_H\bigr).}
\tag{2.7}
\]

If \(G=\tau F\) for a transposition \(\tau\), then
\(F_{-\varepsilon}=\tau F_\varepsilon\), so their energies agree and

\[
\boxed{
\Psi_H(F_\varepsilon)-\Psi_H(F)
=\frac18\bigl(R_H(\varepsilon)-A_H\bigr).}
\tag{2.8}
\]

For \(\mathcal Q_H=2\Psi_H\), the coefficient in (2.8) is \(1/4\).

### Target rows

For a general permutation overlay, let a row \(p=(q,S)\) denote one target
coordinate and put

\[
z_{pK}=\Delta_{K,q}(S),
\qquad
\alpha_p=\frac1{c_q}.
\tag{2.9}
\]

Then

\[
R_H(\varepsilon)
=\sum_p\alpha_p(z_p\cdot\varepsilon)^2.
\tag{2.10}
\]

For a transposition \(\tau\), fixed targets contribute zero and moved
targets occur in opposite pairs.  Choosing one orientation from each moved
orbit

\[
p=(q,\{S,\tau S\})
\tag{2.11}
\]

Write \(a_{K,q}=\mu_q(L_K)\) for the left-side depth-\(q\) histogram and
set

\[
z_{pK}=a_{K,q}(S)-a_{K,q}(\tau S),
\qquad
\alpha_p=\frac2{c_q}
\tag{2.12}
\]

again gives exactly (2.10).  All later row theorems apply to (2.9) or to
the compressed transposition form (2.12).

Let \(D\) be the matrix whose \(K\)-th column is

\[
d_K=(\sqrt{\alpha_p}\,z_{pK})_p.
\tag{2.13}
\]

Then

\[
R_H(\varepsilon)=\|D\varepsilon\|_2^2,
\qquad
\mathbf G=D^TD,
\qquad
g_K=\mathbf G_{KK}=\|d_K\|_2^2.
\tag{2.14}
\]

Put

\[
V_H=\operatorname{tr}\mathbf G=\sum_Kg_K,
\qquad
w_{KL}=\mathbf G_{KL}\quad(K\ne L).
\tag{2.15}
\]

Thus

\[
R_H(\varepsilon)
=V_H+2\sum_{K<L}w_{KL}\varepsilon_K\varepsilon_L,
\qquad
\mathbb E_{\rm fair}R_H=V_H.
\tag{2.16}
\]

Every distribution used below is a distribution on genuine sign vectors.
Its probabilistic expectation is only a proof that one integral outcome is
good.

## 3. Exact targetwise floors and the compatibility ledger

For every target row define

\[
b_p
=\min_{\sigma\in\{\pm1\}^{\mathscr K}}
  (z_p\cdot\sigma)^2,
\tag{3.1}
\]

\[
\pi_p
=\mathbf1_{\{\sum_Kz_{pK}\text{ is odd}\}}
\in\{0,1\}.
\tag{3.2}
\]

The parity is unchanged by signing, so

\[
\Pi_H^{\rm tar}=\sum_p\alpha_p\pi_p,
\qquad
B_H^{\rm tar}=\sum_p\alpha_pb_p
\tag{3.3}
\]

satisfy

\[
\boxed{
\Pi_H^{\rm tar}
\le B_H^{\rm tar}
\le\beta_H
\le\min\{A_H,V_H\}.}
\tag{3.4}
\]

The first inequality is the exact row parity floor.  The second holds
because every common signing has every row at least at its row minimum.
The last two bounds use the all-left signing and independent fair signs.

The value \(B_H^{\rm tar}\) is attained if every row may use a different
component sign vector.  That object is not an exact factor.  The exact
common-sign loss is

\[
L_H^{\rm sync}=\beta_H-B_H^{\rm tar}.
\tag{3.5}
\]

The ideal targetwise room is

\[
I_H^{\rm tar}=A_H-B_H^{\rm tar}.
\tag{3.6}
\]

Consequently

\[
\boxed{
A_H-\beta_H
=I_H^{\rm tar}-L_H^{\rm sync}.}
\tag{3.7}
\]

Restoring parity gives the three-loss decomposition

\[
A_H-\beta_H
=(A_H-\Pi_H^{\rm tar})
 -(B_H^{\rm tar}-\Pi_H^{\rm tar})
 -(\beta_H-B_H^{\rm tar}).
\tag{3.8}
\]

The middle term is local amplitude locking; the last is target/component
incompatibility.  A same-overlay theorem must control both.  Perfect
synchronization cannot create ideal gain, and large ideal gain is useless
if synchronization consumes all of it.

## 4. Target-gauged signed Max-Cut

This section gives the main new theorem.

For every \(p\), choose one local minimizer

\[
\sigma^p\in\operatorname*{argmin}_{\sigma}
(z_p\cdot\sigma)^2,
\tag{4.1}
\]

and put

\[
s_{pK}=z_{pK}\sigma_K^p,
\qquad
L_p=\sum_K|z_{pK}|.
\tag{4.2}
\]

Tied choices in (4.1) may be optimized jointly.  All assertions below are
valid for each fixed choice.

### Theorem 4.1 — exact target-gauged cut expansion

For every common signing \(\varepsilon\),

\[
\boxed{
\alpha_p\left[(z_p\cdot\varepsilon)^2-b_p\right]
=\sum_{K<L}
  (-4\alpha_ps_{pK}s_{pL})
  \mathbf1_{\{\varepsilon_K\sigma_K^p
              \ne\varepsilon_L\sigma_L^p\}}.}
\tag{4.3}
\]

#### Proof

Set \(x_K=\varepsilon_K\sigma_K^p\).  Since \(x_K\in\{\pm1\}\),

\[
(z_p\cdot\varepsilon)^2
=\left(\sum_Ks_{pK}x_K\right)^2,
\qquad
b_p=\left(\sum_Ks_{pK}\right)^2.
\]

The diagonal terms cancel.  For \(K<L\),

\[
2s_{pK}s_{pL}(x_Kx_L-1)
=-4s_{pK}s_{pL}\mathbf1_{\{x_K\ne x_L\}}.
\]

Multiplying by \(\alpha_p\) and summing proves (4.3). \(\square\)

Some coefficients in (4.3) can be negative.  Their total can never make
the row excess negative because \(\sigma^p\) is a row minimizer.  Keeping
only positive coefficients gives an upper bound that has a clean signed
constraint interpretation.

Define, for every target-labelled component pair,

\[
a_{pKL}=4\alpha_p(-s_{pK}s_{pL})_+,
\qquad
\chi_{pKL}=\sigma_K^p\sigma_L^p.
\tag{4.4}
\]

The signed multigraph keeps only the positive-weight edge occurrences
\[
E_+=\{(p,K,L):a_{pKL}>0\};
\tag{4.4a}
\]
zero-weight labelled pairs are ignored.

The constraint on this edge is

\[
\varepsilon_K\varepsilon_L=\chi_{pKL}.
\tag{4.5}
\]

Let

\[
\mathfrak f_+(\boldsymbol\sigma)
=\min_{\varepsilon}
 \sum_{p,K<L}a_{pKL}
 \mathbf1_{\{\varepsilon_K\varepsilon_L\ne\chi_{pKL}\}}.
\tag{4.6}
\]

### Corollary 4.2 — positive target frustration

For every joint choice \(\boldsymbol\sigma=(\sigma^p)_p\),

\[
\boxed{
\beta_H-B_H^{\rm tar}
\le\mathfrak f_+(\boldsymbol\sigma).}
\tag{4.7}
\]

#### Proof

Sum (4.3) over \(p\) and discard its nonpositive edge coefficients.  This
gives, for every \(\varepsilon\),

\[
R_H(\varepsilon)-B_H^{\rm tar}
\le
\sum_{p,K<L}a_{pKL}
\mathbf1_{\{\varepsilon_K\varepsilon_L\ne\chi_{pKL}\}}.
\]

Minimize the right side. \(\square\)

### Lemma 4.3 — exact total constraint mass

Let

\[
S_+=\sum_{p,K<L}a_{pKL}.
\tag{4.8}
\]

Then

\[
\boxed{
S_+=\sum_p\alpha_p(L_p^2-b_p).}
\tag{4.9}
\]

#### Proof

For one row let \(P_p\) and \(N_p\) be the total positive and absolute
negative masses among the \(s_{pK}\).  Then

\[
L_p=P_p+N_p,
\qquad
b_p=(P_p-N_p)^2.
\]

The positive coefficients in (4.3) are exactly the pairs with opposite
signs, whose total is \(4\alpha_pP_pN_p\).  Since

\[
4P_pN_p=(P_p+N_p)^2-(P_p-N_p)^2,
\]

the row contribution equals \(\alpha_p(L_p^2-b_p)\). \(\square\)

### Theorem 4.4 — target-pair SDP rounding with constant one

For a fixed joint choice \(\boldsymbol\sigma\), define

\[
\delta_+(\boldsymbol\sigma)
=\min_{\|u_K\|=1}
 \sum_{p,K<L}a_{pKL}
 \frac{1-\chi_{pKL}\langle u_K,u_L\rangle}{2}.
\tag{4.10}
\]

Then

\[
\boxed{
\begin{aligned}
\beta_H-B_H^{\rm tar}
&\le\mathfrak f_+(\boldsymbol\sigma)\\
&=
\inf_{\|u_K\|=1}
\sum_{p,K<L}a_{pKL}
\frac{\arccos(\chi_{pKL}\langle u_K,u_L\rangle)}{\pi}\\
&\le\sqrt{S_+\delta_+(\boldsymbol\sigma)}.
\end{aligned}}
\tag{4.11}
\]

One may minimize the last two expressions over all tied local minimizers
in (4.1).

#### Proof

Given unit vectors \(u_K\), choose a centered isotropic Gaussian \(g\) and
set

\[
\varepsilon_K=\operatorname{sgn}\langle g,u_K\rangle.
\tag{4.12}
\]

For one labelled edge,

\[
\Pr(\varepsilon_K\varepsilon_L\ne\chi_{pKL})
=\frac{\arccos(\chi_{pKL}\langle u_K,u_L\rangle)}{\pi}.
\tag{4.13}
\]

Thus some integral common signing has cost no larger than the angular
expression.  Conversely an optimal integral signing is represented by
collinear unit vectors \(u_K=\varepsilon_Ku\), and its angular cost is
exactly its discrete violation cost.  This proves the equality in (4.11).

For \(-1\le x\le1\),

\[
\frac{\arccos x}{\pi}
\le\sqrt{\frac{1-x}{2}}.
\tag{4.14}
\]

Apply (4.14) edgewise to an SDP minimizer and use weighted
Cauchy--Schwarz:

\[
\sum_ea_e\sqrt{t_e}
\le\sqrt{\left(\sum_ea_e\right)
          \left(\sum_ea_et_e\right)}
=\sqrt{S_+\delta_+}.
\]

Here
\[
t_e=\frac{1-\chi_e\langle u_K,u_L\rangle}{2}.
\]

Every rounded outcome uses one common component sign vector, so it is an
exact factor. \(\square\)

### Exact balance and feedback consequences

The positive signed constraint multigraph is balanced when there is a
signing satisfying every edge label (4.5).  The following statements are
immediate but useful.

1. If it is balanced for one joint choice of local row minimizers, then

   \[
   \beta_H=B_H^{\rm tar}.
   \tag{4.15}
   \]

2. Conversely, if \(\beta_H=B_H^{\rm tar}\), choose an optimal common
   signing as the local minimizer for every row.  The corresponding signed
   graph is balanced.  Hence

   \[
   \boxed{
   \beta_H=B_H^{\rm tar}
   \iff
   \text{some joint choice of tied local minimizers is balanced}.}
   \tag{4.16}
   \]

3. If deleting positive constraint edges of total weight \(e\) leaves a
   balanced signed graph, then

   \[
   \boxed{
   \beta_H-B_H^{\rm tar}\le e.}
   \tag{4.17}
   \]

4. If every target row has at most two active components, no negative
   coefficient was discarded in (4.3).  Therefore

   \[
   \boxed{
   \beta_H-B_H^{\rm tar}=\mathfrak f_+.}
   \tag{4.18}
   \]

   In this arity-two regime, signed-cycle frustration is the exact
   incompatibility rather than merely an upper certificate.

### Sharpness of the square-root SDP conversion

Consider an inconsistent signed cycle of length \(k\), with every edge of
weight \(a>0\).  Its integral frustration is \(a\).  Planar unit vectors
with a twist \(\pi/k\) per edge give

\[
\delta_+
\le\frac{ka}{2}\left(1-\cos\frac\pi k\right)
\le\frac{a\pi^2}{4k},
\qquad
S_+=ka.
\tag{4.19}
\]

Thus there is no universal linear estimate
\(\mathfrak f_+\le C\delta_+\).  Moreover

\[
a\le\sqrt{S_+\delta_+}
\le\left(\frac\pi2+o(1)\right)a
\qquad(k\to\infty).
\tag{4.20}
\]

The lower bound is (4.11), since \(\mathfrak f_+=a\); the upper bound uses
the displayed vector solution in (4.19).  Thus the square-root scale is
order-sharp, and a universal coefficient in front of that scale cannot be
smaller than \(2/\pi\).  This is an analytic signed-graph sharpness model,
not a claimed wreath realization.

## 5. The restricted Catalan descent theorem

Put

\[
E_H=H\operatorname{Cat}_m.
\tag{5.1}
\]

### Theorem 5.1 — target-floor heat descent

Fix one genuine overlay \(F\) versus \(\sigma F\).  Suppose that for some
\(\eta>0\) and \(0\le C<\infty\), and for one joint choice of local target
minimizers,

\[
\boxed{
A_H-B_H^{\rm tar}
-\sqrt{S_+\delta_+}
\ge\eta\Psi_H(F)-CE_H.}
\tag{5.2}
\]

Then there is one common component signing \(\varepsilon\) satisfying

\[
\boxed{
R_H(\varepsilon)
\le A_H-\eta\Psi_H(F)+CE_H.}
\tag{5.3}
\]

One of \(F_\varepsilon,F_{-\varepsilon}\) is an integral exact factor with

\[
\boxed{
\Psi_H(F_*)
\le
\left(1-\frac\eta8\right)\Psi_H(F)
+\frac C8E_H.}
\tag{5.4}
\]

For a transposition, \(F_\varepsilon\) itself obeys (5.4).

#### Proof

Theorem 4.4 gives

\[
\beta_H
\le B_H^{\rm tar}+\sqrt{S_+\delta_+}.
\]

Together with (5.2), this is (5.3).  Apply (2.7), or (2.8) in the
transposition case. \(\square\)

The theorem may be separated into two more geometric hypotheses.  For the
same overlay and the same joint choice of local gauges, suppose
\(\eta_0>0\), \(C_0,C_1\ge0\), and \(0\le\rho<1\).  If

\[
A_H-B_H^{\rm tar}
\ge\eta_0\Psi_H(F)-C_0E_H,
\tag{5.5}
\]

and

\[
\sqrt{S_+\delta_+}
\le\rho(A_H-B_H^{\rm tar})+C_1E_H,
\tag{5.6}
\]

then (5.2) holds with

\[
\eta=(1-\rho)\eta_0,
\qquad
C=(1-\rho)C_0+C_1.
\tag{5.7}
\]

This makes the two missing inputs explicit: same-overlay visibility (5.5)
and target synchronization (5.6).

### Corollary 5.2 — uniform route implication

Fix \(A_0\).  Suppose there are constants

\[
\eta_{A_0}>0,
\qquad
C_{A_0}\in[0,\infty),
\qquad
m_0(A_0)\in\mathbb N,
\tag{5.8}
\]

such that for every \(m\ge m_0(A_0)\) and every exact factor \(F\), some
coordinate relabeling \(\sigma\) and its genuine overlay satisfy (5.2)
with these constants.  Then, for each such \(m\), there exists an exact
factor \(F_*\) such that

\[
\boxed{
\Psi_H(F_*)
\le\frac{C_{A_0}}{\eta_{A_0}}
H\operatorname{Cat}_m.}
\tag{5.9}
\]

#### Proof

Let \(F_{\min}\) be a global minimizer of \(\Psi_H\) on the finite
exact-factor fibre.  Apply Theorem 5.1 to \(F_{\min}\).  Since neither
exact antipode can have smaller energy, (5.4) implies

\[
0\le-\frac{\eta_{A_0}}8\Psi_H(F_{\min})
+\frac{C_{A_0}}8E_H,
\]

which is (5.9) with \(F_*=F_{\min}\). \(\square\)

The same conclusion follows at the natural one-transposition scale if
(5.2) is replaced by

\[
A_H-B_H^{\rm tar}-\sqrt{S_+\delta_+}
\ge\frac{\eta_{A_0}\Psi_H(F)-C_{A_0}E_H}{n}.
\tag{5.9a}
\]

The common factor \(1/n\) cancels at the global minimum.

Since

\[
H\operatorname{Cat}_m
=O_{A_0}\left(\frac{\mathsf W}{\sqrt m}\right)
=o(\mathsf W),
\tag{5.10}
\]

(1.10) gives fixed-window unlabelled overload \(o(\mathsf W)\).  Establishing
Corollary 5.2 for every fixed \(A_0\), followed by the frozen
diagonalization, would prove MWB.  The hypotheses (5.5)--(5.6) are
**unproved** on the genuine factor fibre.

## 6. Partial coloring and deterministic conditional expectations

The target-pair theorem uses correlated hyperplane signs.  This section
tests independent biased signs, partial coloring, and deterministic
conditional expectation.

### Theorem 6.1 — exact biased-rounding identity

Let \(x\in[-1,1]^{\mathscr K}\).  Independently choose signs with

\[
\mathbb E\varepsilon_K=x_K.
\tag{6.1}
\]

Then

\[
\boxed{
\mathbb E R_H(\varepsilon)
=\|Dx\|_2^2+
 \sum_K(1-x_K^2)g_K.}
\tag{6.2}
\]

Moreover, exposing the signs one at a time and always choosing a branch
whose conditional expectation does not increase produces a deterministic
common signing with residual at most (6.2).

#### Proof

Write \(\varepsilon=x+(\varepsilon-x)\).  The centered coordinates are
independent, have mean zero, and have variances \(1-x_K^2\).  Therefore

\[
\mathbb E\|D\varepsilon\|_2^2
=\|Dx\|_2^2+
 \sum_K(1-x_K^2)\|d_K\|_2^2.
\]

At each exposure step the present conditional expectation is the convex
combination of the two child conditional expectations, so one child is no
larger.  After all signs are fixed, the remaining conditional expectation
is the residual of one integral exact factor. \(\square\)

The same proof allows a fixed outside residual.  If \(J\subseteq\mathscr K\),
\(r=\sum_{K\notin J}\eta_Kd_K\), and only \(K\in J\) are rounded, then

\[
\beta_H
\le
\left\|r+\sum_{K\in J}x_Kd_K\right\|_2^2
+\sum_{K\in J}(1-x_K^2)g_K.
\tag{6.3}
\]

### Corollary 6.2 — floor-targeted zonotope partial coloring

Choose integer roots \(r_p\) with \(r_p^2=b_p\), and put

\[
h=(\sqrt{\alpha_p}\,r_p)_p.
\tag{6.4}
\]

If there is an \(x\in[-1,1]^{\mathscr K}\) satisfying

\[
Dx=h,
\tag{6.5}
\]

then

\[
\boxed{
\beta_H-B_H^{\rm tar}
\le
\Phi_{\rm pc}(x):=\sum_K(1-x_K^2)g_K.}
\tag{6.6}
\]

Hence the explicit restricted condition

\[
A_H-B_H^{\rm tar}-\Phi_{\rm pc}(x)
\ge\eta\Psi_H(F)-CE_H
\tag{6.7}
\]

implies the requested residual bound (5.3).

The feasibility condition (6.5) is the exact zonotope condition

\[
h\in\sum_K[-d_K,d_K].
\tag{6.8}
\]

It is not automatic.  If the affine box fibre in (6.5) is nonempty, an
extreme point has at most

\[
r_D=\operatorname{rank}D
\tag{6.9}
\]

fractional coordinates: otherwise its fractional columns would be
linearly dependent and a small two-sided kernel perturbation would remain
inside the fibre.  Therefore

\[
\Phi_{\rm pc}(x)
\le\sum_{j=1}^{r_D}g_{(j)},
\tag{6.10}
\]

where \(g_{(j)}\) are the component energies in decreasing order.  Exact
floor cancellation plus Catalan-small total action of these boundary
components is a valid restricted theorem.  Neither the zonotope reachability
nor a Catalan bound on (6.10) is known; \(r_D\) can equal the number of
components.

### Proposition 6.3 — optimizing common biases is tautologically exact

Expanding (6.2) gives

\[
\mathcal E(x)
:=\mathbb E R_H
=V_H+2\sum_{K<L}w_{KL}x_Kx_L.
\tag{6.11}
\]

This is affine in each coordinate separately.  Pushing the coordinates
successively to endpoints without increasing the value proves

\[
\boxed{
\min_{x\in[-1,1]^{\mathscr K}}\mathcal E(x)
=\min_{\varepsilon\in\{\pm1\}^{\mathscr K}}R_H(\varepsilon)
=\beta_H.}
\tag{6.12}
\]

Thus nonuniform common means and conditional expectations are useful
certificates and derandomizations, but they do not enlarge the move class.
One common law has the single mean
\(x_K=\mathbb E\varepsilon_K\), independent of \(p\).  Target-dependent
means \(x_{pK}\) are therefore illegal unless they are actually independent
of \(p\); the same common-law restriction applies to pair correlations.

More generally, every correlated law is a convex combination of integral
cut vertices and has expected residual at least \(\beta_H\).  Multiplying
an arbitrary signing by one independent fair global sign makes every
component marginal fair without changing \(R_H\).  Hence the requirement
of fair one-component marginals places no restriction on the optimum.

### Theorem 6.4 — a genuine restricted Bernoulli gain

At the all-plus corner define

\[
\gamma_K=\sum_{L\ne K}w_{KL}.
\tag{6.13}
\]

Flip component \(K\) independently with probability \(p_K\).  Then

\[
\boxed{
\mathbb E R_H
=A_H-4\sum_Kp_K\gamma_K
+8\sum_{K<L}w_{KL}p_Kp_L.}
\tag{6.14}
\]

Conditional expectations give a deterministic common signing no worse
than this mean.  In particular, let

\[
T\subseteq\{K:\gamma_K>0\},
\qquad
\Gamma_T=\sum_{K\in T}\gamma_K,
\qquad
E_T^+=\sum_{\substack{K<L\\K,L\in T}}(w_{KL})_+.
\tag{6.15}
\]

Flip every \(K\in T\) with a common probability \(p\), and no other
component.  Optimizing the lower bound

\[
A_H-\mathbb E R_H
\ge4p\Gamma_T-8p^2E_T^+
\tag{6.16}
\]

gives

\[
\boxed{
A_H-\beta_H\ge
\begin{cases}
\Gamma_T^2/(2E_T^+),
&0<\Gamma_T\le4E_T^+,\\[2mm]
4\Gamma_T-8E_T^+\ge2\Gamma_T,
&\Gamma_T\ge4E_T^+.
\end{cases}}
\tag{6.17}
\]

If \(E_T^+=0\), the first case is omitted and \(p=1\) gives gain at least
\(4\Gamma_T\).  This is a genuine partial-randomization theorem.  It is
useful only when its right side dominates
\(\eta\Psi_H-CE_H\).  At a corner locally minimal under every singleton
component flip, every \(\gamma_K\le0\), so this certificate is empty.

## 7. Aggregate Max-Cut, matching, and correlated-sign SDP

The target-gauged graph of Section 4 remembers where pair constraints came
from.  The actual quadratic objective nevertheless collapses to the one
aggregate Gram graph in (2.16).

Put

\[
W_+=\sum_{w_{KL}>0}w_{KL},
\qquad
W_-=-\sum_{w_{KL}<0}w_{KL},
\qquad
T_W=W_++W_-.
\tag{7.1}
\]

An aggregate edge wants

\[
\varepsilon_K\varepsilon_L=-\operatorname{sgn}(w_{KL}).
\tag{7.2}
\]

Let \(\operatorname{fr}_W(\varepsilon)\) be positive uncut weight plus
negative cut weight, and let \(\operatorname{fr}_W^*\) be its minimum.
Then exactly

\[
R_H(\varepsilon)
=V_H-2T_W+4\operatorname{fr}_W(\varepsilon),
\tag{7.3}
\]

\[
\boxed{
\beta_H=V_H-2T_W+4\operatorname{fr}_W^*,}
\tag{7.4}
\]

and, since the all-plus corner violates precisely the positive edges,

\[
\boxed{
A_H-\beta_H
=4(W_+-\operatorname{fr}_W^*).}
\tag{7.5}
\]

Thus the requested inequality is exactly equivalent to

\[
W_+-\operatorname{fr}_W^*
\ge\frac14\left(
\eta\Psi_H(F)-CE_H
\right).
\tag{7.6}
\]

### Theorem 7.1 — diagonal-majorant correlated rounding

Let \(W_0\) be the symmetric zero-diagonal matrix with entries \(w_{KL}\).
Suppose a positive diagonal matrix

\[
\Lambda=\operatorname{diag}(\lambda_K)
\tag{7.7}
\]

satisfies

\[
\Lambda-W_0\succeq0.
\tag{7.8}
\]

Then one correlated common signing satisfies

\[
\boxed{
\beta_H\le V_H-\Gamma_\Lambda,}
\tag{7.9}
\]

where

\[
\boxed{
\Gamma_\Lambda
=\frac4\pi\sum_{K<L}|w_{KL}|
\arcsin\left(
\frac{|w_{KL}|}{\sqrt{\lambda_K\lambda_L}}
\right).}
\tag{7.10}
\]

#### Proof

The matrix

\[
X=\Lambda^{-1/2}(\Lambda-W_0)\Lambda^{-1/2}
\tag{7.11}
\]

is a correlation matrix and

\[
X_{KL}=-\frac{w_{KL}}{\sqrt{\lambda_K\lambda_L}}.
\]

Represent \(X\) as a Gram matrix of unit vectors and hyperplane-round them.
The sign correlation is \((2/\pi)\arcsin X_{KL}\).  Substitution in
(2.16) gives (7.9)--(7.10). \(\square\)

If \(W_0\ne0\), then \(\lambda_+=\lambda_{\max}(W_0)>0\), and
\(\Lambda=\lambda_+I\) is admissible.  With

\[
\sigma_W=\left(\sum_{K<L}w_{KL}^2\right)^{1/2},
\tag{7.12}
\]

one obtains

\[
\boxed{
V_H-\beta_H
\ge\frac{2\sqrt2}{\pi}\sigma_W.}
\tag{7.13}
\]

Indeed, \(\arcsin x\ge x\), while

\[
\lambda_+\le\|W_0\|_F=\sqrt2\,\sigma_W.
\]

Therefore the proved restricted SDP criterion

\[
\boxed{
A_H-V_H+\frac{2\sqrt2}{\pi}\sigma_W
\ge\eta\Psi_H(F)-CE_H}
\tag{7.14}
\]

implies (5.3).  The sharper \(\Gamma_\Lambda\) may replace the Frobenius
term.

### Matching and sparsity certificate

Let \(\mathfrak M\) be the maximum total absolute weight of a matching in
the aggregate Gram graph.  Force every matched edge to have its preferred
relative sign, independently randomize one sign per matched block and per
unmatched vertex, and then derandomize the block signs.  All unmatched
cross-block terms have mean zero, so

\[
\boxed{
\beta_H\le V_H-2\mathfrak M.}
\tag{7.15}
\]

Hence

\[
\boxed{
A_H-V_H+2\mathfrak M
\ge\eta\Psi_H(F)-CE_H}
\tag{7.16}
\]

is another exact-factor sufficient condition.  If the nonzero aggregate
Gram graph has maximum degree \(\Delta\ge1\), greedy weighted matching gives

\[
\mathfrak M
\ge\frac{\sum_{K<L}|w_{KL}|}{2\Delta-1}.
\tag{7.17}
\]

The reason is that a selected maximum remaining edge deletes at most
\(2\Delta-1\) edges, each no heavier than the selected one.  This is the
precise point at which a genuine aggregate sparsity theorem would yield a
Catalan-scale result.  No such uniform sparsity theorem is proved, and
large targetwise interactions may cancel before the aggregate graph is
formed.

### Floor-aware ordinary SDP

One may also define

\[
\gamma_H
=\min\left\{
\langle \mathbf G,X\rangle:
X\succeq0,
\ X_{KK}=1,
\ z_p^TXz_p\ge b_p\ \forall p
\right\}.
\tag{7.18}
\]

Every cut matrix is feasible, hence

\[
B_H^{\rm tar}\le\gamma_H\le\beta_H.
\tag{7.19}
\]

For any correlation matrix \(X\), hyperplane rounding has the exact
expected residual

\[
V_H+\frac4\pi\sum_{K<L}w_{KL}\arcsin X_{KL}.
\tag{7.20}
\]

A constant-factor Max-Cut or Grothendieck approximation is generally
scale-useless here: if the total pair mass is much larger than \(E_H\), a
fixed multiplicative loss leaves a super-Catalan additive remainder.  The
near-integral additive estimate (4.11), a Catalan-small matching remainder,
or an equally strong genuine geometry theorem is required.

## 8. Exact cancellation and what target dependence cannot recover

Equation (0.8) is the decisive common-sign constraint.  If a randomized
scheme produces one final sign vector, its expected objective is

\[
\mathbb ER_H
=V_H+2\sum_{K<L}w_{KL}
  \mathbb E(\varepsilon_K\varepsilon_L).
\tag{8.1}
\]

It depends on the targetwise or depthwise Gram pieces only through their
sum \(w_{KL}\).  Supplying a different covariance matrix for every target
or every depth is not a distribution on exact factors.

### Theorem 8.1 — constant-cube characterization

For one genuine ownership cube,

\[
\boxed{
R_H(\varepsilon)\text{ is constant on }
\{\pm1\}^{\mathscr K}
\iff
w_{KL}=0\quad\text{for every }K\ne L.}
\tag{8.2}
\]

In that case

\[
\boxed{
A_H=V_H=\beta_H.}
\tag{8.3}
\]

#### Proof

The forward implication follows because the degree-two Fourier characters
\(\varepsilon_K\varepsilon_L\) in (2.16) are linearly independent.  The
reverse implication is immediate from the same formula. \(\square\)

Thus exact cross-depth cancellation

\[
\sum_{q\le H}\frac{
\langle\Delta_{K,q},\Delta_{L,q}\rangle_2}{c_q}=0
\tag{8.4}
\]

can erase arbitrarily large rankwise pair interactions.  In the constant
case, Theorem 4.4 itself forces the target synchronization obstruction

\[
\boxed{
V_H-B_H^{\rm tar}
\le\sqrt{S_+\delta_+}.}
\tag{8.5}
\]

Target gauging does not evade aggregate cancellation; it records the
amount of frustration required to explain it.

### Depthwise ledger

Define

\[
R_q(\varepsilon)
=\frac1{c_q}\left\|\sum_K\varepsilon_K\Delta_{K,q}\right\|_2^2,
\qquad
A_q=R_q(\mathbf1),
\qquad
\beta_q=\min_\varepsilon R_q(\varepsilon).
\tag{8.5a}
\]

Thus \(\beta_q\) is the optimum when depth \(q\) is allowed to choose its
own component signs, while \(\beta_H\) uses one common sign through all
depths.  Then

\[
\mathfrak F_{\rm depth}
=\beta_H-\sum_{q\le H}\beta_q\ge0,
\tag{8.6}
\]

and

\[
\boxed{
A_H-\beta_H
=\sum_{q\le H}(A_q-\beta_q)
 -\mathfrak F_{\rm depth}.}
\tag{8.7}
\]

All rankwise gain survives exactly when the rankwise argmin sets have a
common signing.  No biased, anisotropic, or target-dependent law changes
this identity.

## 9. Obstructions

This section separates an exact-factor incompatibility theorem from formal
row systems.  Only the first subsection is an unconditional statement
about genuine exact factors.

### 9.1 A genuine transposition cube has a non-descending orientation

Fix a genuine transposition component cube and choose a vertex \(F_0\)
minimizing \(\Psi_H\) on that finite cube.  Reorient every component so
that the all-plus corner is \(F_0\).  The antipode of every vertex is its
transposition relabeling, so (2.8) applies at this reoriented corner.
Every vertex has energy at least \(\Psi_H(F_0)\); hence

\[
R_H(\varepsilon)\ge A_H
\quad\text{for every }\varepsilon.
\]

Since equality holds at the all-plus corner,

\[
\boxed{
\beta_H=A_H,
\qquad
A_H-B_H^{\rm tar}
=\beta_H-B_H^{\rm tar}.}
\tag{9.1}
\]

Thus the ideal target gain is exactly canceled by common-sign
incompatibility at this transposition-cube orientation.  No probability
distribution, SDP rounding, partial coloring, or conditional-expectation
strategy inside the same cube can descend.  This is not a counterexample
to Theorem 5.1: if (5.2) held uniformly for every orientation of this
particular transposition cube, it would force its minimum to have
\(\Psi_H=O(E_H)\).  Corollary 5.2 needs less—it requires only that some
overlay work at a global fibre minimum, not that every transposition-cube
minimum be small.

At a global \(\Psi_H\)-minimum on the whole exact-factor fibre, (9.1) does
hold for every genuine overlay, including general permutation overlays:
the two original endpoints are relabellings and have equal energy, while
every antipodal child is a global-minimum competitor.  Equation (2.6) then
gives \(R_H(\varepsilon)\ge A_H\).  Hence a route-closing discrepancy
theorem must use special wreath geometry strong enough to prove that this
global minimum already has \(\Psi_H=O(E_H)\).

There is also a visibility obstruction independent of synchronization.  In
the transposition case, define the centered load by

\[
f_q=\mu_{F,q}-\frac{\mathsf W}{N_q}\mathbf1,
\tag{9.1a}
\]

and put \(f_q^-=(f_q-\tau f_q)/2\).  Then

\[
\|x\|_H^2
=\sum_{q\le H}\frac{\|x_q\|_2^2}{c_q}
\tag{9.1b}
\]

and

\[
\boxed{
A_H
=\|f-\tau f\|_H^2
=4\|f^-\|_H^2.}
\tag{9.2}
\]

Component signing cannot manufacture gain from the \(\tau\)-invariant
part of the energy.  A proof needs a same-transposition visibility theorem
as well as synchronization.

### 9.2 Formal same-depth target cancellation

The next construction is an integral signed-row array, not a wreath
ownership construction.

Let \(\mathcal G\) be a \(d\)-regular graph on \(N\) formal component
vertices.  At depth \(q=1\), where \(c_1=1\) for \(m>2\) and the actual
orbit weight is \(\alpha=2\), insert for every graph edge \(ij\) the four
distinct target rows

\[
\pm(e_i+e_j),
\qquad
\pm(e_i-e_j).
\tag{9.3}
\]

Every row has unit coefficients and exact parity and row floor zero.  The
two signs give zero column sums, and every \(\{\pm1\}\)-row has a
nonnegative pair-table representation.  For one edge, the four row Grams
sum to

\[
4\alpha(e_ie_i^T+e_je_j^T).
\tag{9.4}
\]

All off-diagonal terms cancel.  Therefore

\[
\boxed{
B_H^{\rm tar}=\Pi_H^{\rm tar}=0,
\qquad
A_H=V_H=\beta_H=8\alpha|E(\mathcal G)|.}
\tag{9.5}
\]

Every target separately is perfectly balanceable, but every common signing
has the same residual.  Taking

\[
N=\Theta(\operatorname{Cat}_m),
\qquad
d=\Theta(n)
\tag{9.6}
\]

gives \(\Theta(\mathsf W)\) total residual, whereas
\(E_H=\Theta_{A_0}(\mathsf W/\sqrt m)\).  The row count is
\(\Theta(n\operatorname{Cat}_m)=\Theta(\mathsf W)\), and every component
has \(O(n)\) row incidences.  Thus bounded coefficients, actual orbit
weights, row parity, nonnegative row-level pair tables, and the natural
incidence budget do not imply Catalan synchronization.

What is missing from (9.3) is decisive: unique global middle ownership,
squarefree cyclic wreath support, connectivity of the actual ownership
overlay, point margins in every rank, and one nested prefix chronology.
No exact factor realizing (9.3) is asserted.

### 9.3 Formal cross-depth cancellation

Let \(L\in\mathbb N\), and choose distinct depths
\(q_+,q_-\le H\), which is possible for all sufficiently large \(m\).
With two formal components, at depth \(q_+\) take normalized repeated rows

\[
\pm(1,1),
\tag{9.7}
\]

and at a second depth \(q_-\) take

\[
\pm(1,-1).
\tag{9.8}
\]

Use \(c_{q_+}L\) and \(c_{q_-}L\) copies respectively so that the exact
weights \(2/c_q\) give equal aggregate coefficients.  Each depth separately
has \(B_q=\beta_q=0\): the first wants opposite component signs and the
second wants equal signs.  Their Gram matrices add to a diagonal matrix,
so over the common window

\[
\boxed{
B_H^{\rm tar}=0,
\qquad
A_H=V_H=\beta_H.}
\tag{9.9}
\]

This survives the exact cut polytope and every SDP hierarchy because the
objective itself is constant.  It is again only a row-level formal model,
not a proved wreath realization.

### 9.4 Odd-cycle relaxation obstruction

At arity two, take an odd cycle of length \(k\), with one row
\(e_i+e_{i+1}\) of weight \(a>0\) on every edge.  Then

\[
B_H^{\rm tar}=0,
\qquad
\beta_H=4a
\tag{9.10}
\]

because every signing violates at least one edge.  Planar vectors make the
ordinary floor-aware SDP value \(O(a/k)\).  This proves that there is no
universal multiplicative
bound

\[
\beta_H-B_H^{\rm tar}
\le C(\gamma_H-B_H^{\rm tar})
\tag{9.11}
\]

for the basic elliptope.  The angular target-pair rounding is honest: its
expected cost is the integral frustration, and the square-root estimate
(4.11) has the correct order.  No wreath realization of this odd-cycle
family is claimed.

## 10. Deterministic target synchronization and controlled sequences

The pair-gauged graph is not the only way to state a restricted theorem.
For completeness, choose local minimizers \(\sigma^p\) and auxiliary row
phases \(t_p\in\{\pm1\}\).  Define the target mismatch mass

\[
h_p(\varepsilon,t)
=\sum_K|z_{pK}|
 \mathbf1_{\{\varepsilon_K\ne t_p\sigma_K^p\}},
\tag{10.1}
\]

and

\[
\mathcal H
=\min_{\varepsilon,t,\boldsymbol\sigma}
 \sum_p\alpha_ph_p(\varepsilon,t)^2.
\tag{10.2}
\]

After factoring out \(t_p\), changing the mismatched terms moves the local
row sum by at most \(2h_p\).  Therefore

\[
|z_p\cdot\varepsilon|
\le\sqrt{b_p}+2h_p.
\tag{10.3}
\]

Minkowski and Cauchy--Schwarz give

\[
\boxed{
\beta_H
\le
\left(\sqrt{B_H^{\rm tar}}+2\sqrt{\mathcal H}\right)^2.}
\tag{10.4}
\]

Suppose deleting a set \(D_0\) of target-component incidences makes the
remaining signed incidence graph satisfiable.  Define

\[
E(D_0)
=\sum_p\alpha_p
 \left(
 \sum_{K:(p,K)\in D_0}|z_{pK}|
 \right)^2.
\tag{10.5}
\]

Satisfy every retained incidence.  Then

\[
\mathcal H\le E(D_0),
\tag{10.6}
\]

and hence

\[
\boxed{
\beta_H
\le B_H^{\rm tar}
 +4\sqrt{B_H^{\rm tar}E(D_0)}
 +4E(D_0).}
\tag{10.7}
\]

In particular, a balanced incidence graph has \(E(D_0)=0\) and
\(\beta_H=B_H^{\rm tar}\).  Every forest is balanced after one compatible
local pattern is fixed for each row.  Thus

\[
\begin{aligned}
A_H-B_H^{\rm tar}
&-4\sqrt{B_H^{\rm tar}E(D_0)}-4E(D_0)\\
&\ge\eta\Psi_H(F)-CE_H
\end{aligned}
\tag{10.8}
\]

is a fully deterministic restricted theorem implying (5.3).

Repeatedly recomputing sides for the same transposition does not supply
target-dependent signs: the intrinsic component cube is unchanged, and
every terminal state is one original common signing.  Changing the
transposition can leave the cube, but then the target system itself changes.
Stagewise gains against changing targets need not telescope; only actual
decrease of \(\Psi_H\) or overload does.  Therefore a controlled sequence
does not bypass the common-sign obstruction without a separately proved
monotone potential theorem.

## 11. Scope relative to MWB, FSP, and PTAD

The exact quadratic theorem has a clear scope.

### MWB

If the quantified hypothesis in Corollary 5.2 is proved for every fixed
\(A_0\), then (5.9), (1.10), and the frozen diagonalization give MWB.  This
is a genuine exact-factor implication.  No labelled common-owner
synchronization is used.

### FSP

The factor-side packet theorem requires the much smaller scale

\[
o_{A_0}\left(\frac{\operatorname{Cat}_m}{\sqrt m}\right)
\tag{11.1}
\]

for a common quota-safe deletion/overload certificate.  The additive error

\[
H\operatorname{Cat}_m
=\Theta_{A_0}\left(\frac{\mathsf W}{\sqrt m}\right)
\tag{11.2}
\]

in the heat theorem is larger by a factor of order \(n\).  Moreover,
quadratic collision descent does not directly construct the packet cover.
The AA5 target-pair theorem gives a separate sufficient condition of the
form

\[
\Omega_{\rm sep}
+\sqrt{S_{\rm tar}\delta_{\rm tar}}
=o_{A_0}\left(\frac{\operatorname{Cat}_m}{\sqrt m}\right),
\tag{11.3}
\]

which is unproved.  The present report neither implies nor replaces it.

### PTAD

PTAD additionally requires one literal \(H\)-legal MTF path system,
ordering, bridges, a hole family, and a common trace set with small total
chronology cost.  A sequence of exact factor states is not such a word.
No implication from (5.3) to PTAD is claimed.

## 12. Exact theorem ledger and independent audit points

### Proved in this report

1. The exact load-floor normalization (1.3)--(1.6).
2. The general antipodal heat identity (2.6), the \(1/8\) child constant
   (2.7), and the transposition identity (2.8).
3. The exact target-floor chain (3.4) and ideal/synchronization split
   (3.7)--(3.8).
4. The target-gauged cut identity (4.3).
5. The positive-frustration bound (4.7), exact mass identity (4.9), and
   SDP/hyperplane theorem (4.11) with constant \(1\).
6. The balance, feedback, arity-two, and odd-cycle consequences.
7. The restricted Catalan descent theorem (5.1) and its uniform exact-factor
   implication (5.9).
8. The partial-coloring identity (6.2), zonotope floor theorem (6.6),
   extreme-fibre rank bound, and exact multiaffine obstruction (6.12).
9. The deterministic Bernoulli gain (6.17).
10. The aggregate signed-Max-Cut identity (7.5), diagonal-majorant bound
    (7.10), Frobenius constant \(2\sqrt2/\pi\), and matching bound (7.15).
11. The constant-cube characterization (8.2) and exact transposition-cube
    minimum-corner incompatibility (9.1), together with its global-minimum
    general-overlay extension.
12. The deterministic feedback-incidence certificate (10.7).

### Unproved and not claimed

1. A genuine same-overlay visibility estimate

   \[
   A_H-B_H^{\rm tar}
   \ge\eta_{A_0}\Psi_H(F)-O_{A_0}(E_H).
   \]

2. A genuine synchronization theorem making

   \[
   \beta_H-B_H^{\rm tar}
   \quad\text{or}\quad
   \sqrt{S_+\delta_+}
   \]

   Catalan-small relative to the same visible gain.
3. Wreath realization of any formal array in Section 9.
4. FSP or PTAD from the quadratic heat theorem.

### Constant and quantifier audit

The decisive constants were independently rederived as follows.

* In (4.3), a disagreeing relative pair changes
  \(2s_{pK}s_{pL}\) to \(-2s_{pK}s_{pL}\), producing
  \(-4s_{pK}s_{pL}\), not \(-2s_{pK}s_{pL}\).
* The total positive pair mass is
  \(4\alpha_pP_pN_p=\alpha_p(L_p^2-b_p)\), proving (4.9) with no missing
  factor of two.
* Hyperplane disagreement is exactly angle divided by \(\pi\), and
  (4.14) plus weighted Cauchy--Schwarz gives coefficient \(1\) in (4.11).
* The energy \(\Psi_H\) is half the full squared floor energy.  Therefore
  the residual-to-child coefficient is \(1/8\), while it is \(1/4\) for
  \(\mathcal Q_H=2\Psi_H\).
* Every sufficient estimate uses one overlay, one fixed window, and one
  common component signing.  No estimates from different transpositions
  or independently optimized depths are added as though they formed one
  factor.
* The formal arrays are labelled non-genuine at their first use and are
  invoked only to delimit black-box methods.

## 13. Final conclusion

Target-by-target correlated signs do yield a clean theorem, but only after
the exact target floors are exposed.  The useful quantity is not fair
component variance by itself.  It is the net room

\[
\boxed{
(A_H-B_H^{\rm tar})
-(\beta_H-B_H^{\rm tar}).}
\]

The first term is visibility; the second is synchronization.  The new
target-gauged signed graph gives the rigorous estimate

\[
\boxed{
\beta_H-B_H^{\rm tar}
\le\sqrt{S_+\delta_+},}
\]

and therefore the exact restricted descent theorem (5.2).  Partial
coloring, aggregate SDP/Max-Cut, matching, and conditional expectations
give complementary certificates, all producing literal exact factors.

The route remains open because no known genuine ownership theorem forces
the ideal target room to see a fixed fraction of \(\Psi_H\) while keeping
the target/depth synchronization loss below it up to
\(O_{A_0}(H\operatorname{Cat}_m)\).  Same-depth and cross-depth cancellation
show why that missing input must use the actual cyclic ownership chronology,
not only generic vector discrepancy, parity, sparsity, or SDP geometry.
