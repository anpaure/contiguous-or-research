# Third-wave AA: multirank correlated signs after the Boolean-\(E_2\) no-go

## 0. Verdict

Fix \(A_0>0\), and take \(m\) sufficiently large that
\(\lceil A_0\sqrt m\rceil\le m-2\).  Put

\[
n=2m+1,\qquad
\mathsf W=\binom nm,\qquad
H=\lceil A_0\sqrt m\rceil,\qquad
\operatorname{Cat}_m=\frac{\mathsf W}{n},
\]

and use the exact weights

\[
c_q=\left\lfloor
\frac{\mathsf W}{\binom n{m-q}}
\right\rfloor,\qquad 1\le q\le H.
\]

The AA2 diagonal-majorant theorem remains valid on the whole window, but
the third-wave issue is now completely visible:

1. For one transposition \(\tau\), every legal randomized
   ownership-component move has one sign vector, hence one correlation
   matrix, common to all depths.  Its expected quadratic energy depends on
   the depth Grams only through their weighted sum.  No biased,
   nonuniform, anisotropic, block, SDP, or adaptive rounding rule producing
   one final signing can recover an interaction that cancels in that sum.

2. If \(W_{\tau,q}\) is the zero-diagonal component Gram at depth \(q\)
   and \(W_\tau=\sum_qW_{\tau,q}\), then

   \[
   \boxed{\beta_\tau<V_\tau\iff W_\tau\ne0.}
   \]

   Thus correlated fair signs beat independent fair variance exactly when
   a nonzero aggregate component edge survives.  The AA2 theorem gives

   \[
   V_\tau-\beta_\tau
   \ge
   \frac{2\sqrt2}{\pi}
   \left(\sum_{K<L}w_{\tau,KL}^2\right)^{1/2}.
   \]

3. Rankwise gains have an exact synchronization ledger.  If
   \(\beta_{\tau,q}\) is the optimum at depth \(q\), then

   \[
   V_\tau-\beta_\tau
   =
   \sum_q(V_{\tau,q}-\beta_{\tau,q})
   -
   \mathfrak F_{\tau,\mathrm{depth}},
   \]

   where

   \[
   \mathfrak F_{\tau,\mathrm{depth}}
   =
   \beta_\tau-\sum_q\beta_{\tau,q}\ge0.
   \]

   All rankwise gain survives precisely when the rank minimizers have a
   common signing; all of it is erased precisely when
   \(W_\tau=0\).  A signed depth-component synchronization SDP gives the
   proved bound

   \[
   \mathfrak F_{\tau,\mathrm{depth}}
   \le4\sqrt{S_\tau\delta_{\tau,\mathrm{depth}}}.
   \]

4. There is an exact signed-multigraph normal form.  Cross-depth reversal
   first cancels parallel positive and negative edges on each component
   pair; ordinary signed-cycle holonomy acts only on the surviving
   aggregate graph.  If \(T_{\tau,\mathrm{agg}}\) is its total absolute
   weight and \(\operatorname{fr}_{\tau,\mathrm{hol}}\) its minimum
   frustration, then

   \[
   \boxed{
   V_\tau-\beta_\tau
   =
   2T_{\tau,\mathrm{agg}}
   -4\operatorname{fr}_{\tau,\mathrm{hol}}.}
   \]

   The current factor descends only when its current frustration is larger
   than the minimum.  Variance improvement and descent are not the same.

5. The proved Boolean-\(E_2\) inequality and three-slack ledger alone do
   not force Gram survival.  At a same-window global minimizer they force
   the **floor plus high-harmonic** slacks to be

   \[
   \Omega_{A_0}(n\mathsf W\sqrt m),
   \]

   but give no lower bound on

   \[
   R_H-D_H
   =
   \sum_\tau(V_\tau-\beta_\tau),
   \]

   the only slack measuring aggregate component-Gram survival.

6. The following conditions are sufficient for a route-critical Catalan
   improvement, but only together with a same-\(\tau\) ideal-gain estimate.
   They require an additional genuine ownership hypothesis:

   \[
   B_\tau-\Pi_\tau
   +\sum_q(\beta_{\tau,q}-B_{\tau,q})
   +4\sqrt{S_\tau\delta_{\tau,\mathrm{depth}}}
   =
   O_{A_0}\!\left(
   \frac{H\operatorname{Cat}_m}{n}\right),
   \]

   Alternatively one may use the global covariance-dominance inequality
   (8.5) below.  Neither route follows from the Boolean-\(E_2\) inequality
   and three-slack ledger alone, nor from zero margins, parity, bounded
   incidence, or generic SDP geometry.

7. The canonical MSW two-for-two family does have genuine aggregate Gram
   survival: its audited deep Dyck pile makes its internal aggregate
   coherence positive.  This is not yet descent, because its alignment
   with the larger components is unknown and its positive internal
   coherence is far too large for the naive \(p=1/n\) Bernoulli argument.

8. A bounded-degree bipartite two-depth array has parity-perfect rankwise
   minima but a diagonal aggregate Gram, so every common signing has the
   same energy.  At \(N=\Theta(\operatorname{Cat}_m)\) its bundling loss is
   \(\Theta(\operatorname{Cat}_m)\), a factor
   \(\Theta_{A_0}(\sqrt m)\) above
   \(H\operatorname{Cat}_m/n\).  It is not a wreath realization, and
   identifies exactly the cyclic-prefix theorem still missing.

All theorems below fix one transposition and its one genuine ownership
partition before stacking depths.  Combining component systems belonging
to different transpositions is illegal.

## 1. Exact full-window component calculus

Fix an exact factor \(F\) and a coordinate transposition \(\tau\).  Let
\(\mathscr K_\tau(F)\) be the genuine ownership components of the overlay
between \(F\) and \(\tau F\).  For component \(K\), let \(a_{K,q}\) be its
left-side depth-\(q\) histogram and put

\[
d_{K,q}=\tau a_{K,q}-a_{K,q}.
\tag{1.1}
\]

Every \(d_{K,q}\) has zero total and zero point margins.  Stack the whole
window:

\[
d_K=
\left(c_q^{-1/2}d_{K,q}\right)_{q=1}^H.
\tag{1.2}
\]

For later use, set

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac{\mathsf W}{N_q},\qquad
\theta_q=\lambda_q-c_q,
\tag{1.2a}
\]

\[
\mu_q=\sum_Ka_{K,q},\qquad
f_q=\mu_q-\lambda_q\mathbf1,qquad
V_q^{\min}=N_q\theta_q(1-\theta_q),
\tag{1.2b}
\]

and define the fixed-window integer floor excess

\[
\mathcal Q_H(F)
=
\sum_{q=1}^H
\frac{\|f_q\|_2^2-V_q^{\min}}{c_q}.
\tag{1.2c}
\]

Here \(V_q^{\min}\) is the minimum squared centered norm among integer
loads of total mass \(\mathsf W\) on \(N_q\) targets.  Write
\(f=(c_q^{-1/2}f_q)_{q=1}^H\) for the stacked centered histogram.

Define the depth and aggregate Gram matrices

\[
(G_q)_{KL}
=
\frac1{c_q}\langle d_{K,q},d_{L,q}\rangle,
\qquad
G=\sum_{q=1}^HG_q,
\tag{1.3}
\]

and their zero-diagonal parts

\[
W_q=G_q-\operatorname{diag}G_q,
\qquad
W=G-\operatorname{diag}G=\sum_qW_q.
\tag{1.4}
\]

Write

\[
w^q_{KL}=(G_q)_{KL},\qquad
w_{KL}=\sum_qw^q_{KL}\quad(K\ne L).
\tag{1.5}
\]

For one common component signing
\(\varepsilon\in\{\pm1\}^{\mathscr K_\tau(F)}\), put

\[
R_q(\varepsilon)=\varepsilon^TG_q\varepsilon,
\qquad
R(\varepsilon)=\sum_qR_q(\varepsilon)=\varepsilon^TG\varepsilon.
\tag{1.6}
\]

Thus

\[
R(\varepsilon)
=
V+2\sum_{K<L}w_{KL}\varepsilon_K\varepsilon_L,
\qquad
V=\operatorname{tr}G=\sum_K\|d_K\|^2.
\tag{1.7}
\]

Let

\[
A=R(\mathbf1)
=\left\|\sum_Kd_K\right\|^2,
\qquad
\beta=\min_\varepsilon R(\varepsilon).
\tag{1.8}
\]

Write \(d=\sum_Kd_K\).  For \(I\subseteq\mathscr K_\tau(F)\), put

\[
d_I=\sum_{K\in I}d_K,
\qquad
I^c=\mathscr K_\tau(F)\setminus I,
\tag{1.8a}
\]

and let \(\varepsilon^I_K=-1\) on \(I\) and \(+1\) on \(I^c\).  Then
\(\sum_K\varepsilon_K^Id_K=d-2d_I\); switching precisely the components
in \(I\) gives the corresponding exact factor.

Every \(\varepsilon\) chooses one complete side of every genuine component
at every depth and therefore produces one integral exact factor
\(F_\varepsilon\).  The exact transposition energy identity is

\[
\boxed{
\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F)
=\frac{R(\varepsilon)-A}{4},}
\tag{1.9}
\]

so

\[
\boxed{
C_\tau^*
=\max_I\langle d_I,d_{I^c}\rangle
=\frac{A-\beta}{4}.}
\tag{1.10}
\]

Indeed, \(d_I\) is \(\tau\)-anti-invariant, while
\(f+\tau f\) is \(\tau\)-invariant.  Hence

\[
2\langle f,d_I\rangle=-\langle d,d_I\rangle.
\]

Switching \(I\) changes the stacked centered histogram from \(f\) to
\(f+d_I\), so its weighted squared-norm change is

\[
2\langle f,d_I\rangle+\|d_I\|^2
=-\langle d_I,d_{I^c}\rangle.
\]

The load floors are fixed, and

\[
R(\varepsilon^I)-A
=\|d-2d_I\|^2-\|d\|^2
=-4\langle d_I,d_{I^c}\rangle,
\]

which proves (1.9)--(1.10), including every factor of four.

For every moved target orbit \(p=(q,\{S,\tau S\})\), choose an orientation,
write

\[
z_{pK}=a_{K,q}(S)-a_{K,q}(\tau S),
\qquad
\alpha_p=\frac2{c_q},
\tag{1.11}
\]

and define

\[
\pi_p
=\mathbf1_{\{\sum_Kz_{pK}\text{ is odd}\}}
\in\{0,1\},
\qquad
b_p=\min_{\eta_K=\pm1}
\left(\sum_K\eta_Kz_{pK}\right)^2.
\tag{1.12}
\]

Because every signed displacement is \(\tau\)-anti-invariant, its two
coordinates on a moved target orbit are opposite.  Therefore

\[
\boxed{
R(\varepsilon)
=\sum_p\alpha_p
\left(\sum_K\varepsilon_Kz_{pK}\right)^2.}
\tag{1.12a}
\]

This also proves directly that every signed row residual has parity
\(\pi_p\) and is at least \(b_p\).

At depth \(q\), let

\[
\Pi_q=\sum_{p:\,q(p)=q}\alpha_p\pi_p,
\qquad
B_q=\sum_{p:\,q(p)=q}\alpha_pb_p,
\tag{1.13}
\]

and put

\[
\Pi=\sum_q\Pi_q,\qquad B=\sum_qB_q.
\tag{1.14}
\]

These are the parity and rowwise amplitude floors.  They are distinct from
the global load-floor baseline used in the Boolean-\(E_2\) ledger.

## 2. Aggregate covariance collapse

### Theorem 2.1 (one covariance for the whole window)

Let \(\varepsilon\) have any probability law on whole-component signings
and put

\[
C_{KL}=\mathbb E(\varepsilon_K\varepsilon_L).
\tag{2.1}
\]

Then

\[
C\in
\operatorname{conv}
\{\eta\eta^T:\eta\in\{\pm1\}^{\mathscr K_\tau(F)}\}
\tag{2.2}
\]

and

\[
\boxed{
\mathbb E R(\varepsilon)
=\langle G,C\rangle
=V+2\sum_{K<L}w_{KL}C_{KL}.}
\tag{2.3}
\]

Conversely, every matrix in the convex hull (2.2) is the correlation
matrix of such a law.

#### Proof

Equation (2.2) is the definition of the cut-correlation polytope.
Linearity and (1.6) give

\[
\mathbb E R
=\sum_q\langle G_q,C\rangle
=\left\langle\sum_qG_q,C\right\rangle.
\]

The converse follows by sampling the sign vectors in a convex
representation of \(C\).  \(\square\)

### Consequences

1. The depths enter every covariance method only through \(G=\sum_qG_q\).
   A family of separate matrices \(C_q\) is illegal unless all arise from
   the same final sign law.  Choosing different sides for one ownership
   component at different depths does not define one exact factor.

2. Marginal fairness is free.  Given any signing law, multiply the whole
   sign vector by one independent fair sign.  Every marginal becomes fair,
   while every product \(\varepsilon_K\varepsilon_L\), the energy, and the
   chosen exact-factor antipodal pair remain unchanged.

3. Biased or nonuniform marginals cannot enlarge the optimum.  If
   signs are dependent, the expected cut is already a convex combination
   of deterministic cut values.  If component \(K\) is independently
   switched with probability \(p_K\), the expected component cut is

   \[
   \mathcal C(p)
   =
   \sum_{K<L}w_{KL}
   (p_K+p_L-2p_Kp_L).
   \tag{2.4}
   \]

   This is affine in each \(p_K\) separately.  Repeatedly moving one
   coordinate to an endpoint proves

   \[
   \boxed{
   \max_{p\in[0,1]^{\mathscr K}}\mathcal C(p)
   =
   \max_{p\in\{0,1\}^{\mathscr K}}\mathcal C(p)
   =
   C_\tau^*.}
   \tag{2.5}
   \]

   Nonuniform probabilities are useful certificates, not an extra move
   class.

4. The exact AA2 dichotomy becomes

   \[
   \boxed{\beta<V\iff W\ne0.}
   \tag{2.6}
   \]

   If \(W=0\), (1.7) is constant.  If \(w_{KL}\ne0\), force only
   \(\varepsilon_K\varepsilon_L=-\operatorname{sgn}(w_{KL})\) and leave
   every other seed independent and fair.  Then

   \[
   V-\beta\ge2|w_{KL}|>0.
   \tag{2.7}
   \]

For fixed \(A_0\), there is an integer \(C_{A_0}^{\mathrm{wt}}\),
independent of all sufficiently large \(m\), such that
\(c_q\le C_{A_0}^{\mathrm{wt}}\) for every
\(q\le H\).  Indeed,

\[
\frac{\binom nm}{\binom n{m-q}}
=
\prod_{t=0}^{q-1}\frac{m+t+2}{m-t},
\qquad
\log\frac{\binom nm}{\binom n{m-q}}
\le
\frac{q(q+1)}{m-q+1},
\tag{2.8}
\]

so, for example, one may take
\(C_{A_0}^{\mathrm{wt}}=\lceil e^{2(A_0+1)^2}\rceil\) after increasing the lower
threshold for \(m\).  Fix

\[
L_{A_0}
=
\operatorname{lcm}\{1,\ldots,C_{A_0}^{\mathrm{wt}}\}.
\tag{2.9}
\]

Then the orbit formula gives

\[
w_{KL}\in\frac2{L_{A_0}}\mathbb Z.
\tag{2.10}
\]

Thus nonzero survival gives the constant lower bound

\[
V-\beta\ge\frac4{L_{A_0}}.
\tag{2.11}
\]

This quantization is far below every Catalan scale and is only a strictness
statement.

## 3. Exact depth-resolved floors and synchronization

For each depth define

\[
V_q=\operatorname{tr}G_q,\qquad
\beta_q=\min_\varepsilon R_q(\varepsilon),
\qquad
\Delta_q=V_q-\beta_q.
\tag{3.1}
\]

Put

\[
\beta_{\mathrm{sep}}=\sum_q\beta_q,
\qquad
\mathfrak F_{\mathrm{depth}}
=\beta-\beta_{\mathrm{sep}}.
\tag{3.2}
\]

### Theorem 3.1 (depth-resolved four-floor identity)

One has

\[
\boxed{
\Pi\le B\le\beta_{\mathrm{sep}}\le\beta\le\min\{A,V\},}
\tag{3.3}
\]

\[
\boxed{
\beta-\Pi
=
(B-\Pi)
+(\beta_{\mathrm{sep}}-B)
+\mathfrak F_{\mathrm{depth}},}
\tag{3.4}
\]

and therefore

\[
\boxed{
C_\tau^*
=
\frac{A-\Pi}{4}
-\frac{B-\Pi}{4}
-\frac{\beta_{\mathrm{sep}}-B}{4}
-\frac{\mathfrak F_{\mathrm{depth}}}{4}.}
\tag{3.5}
\]

The four terms are respectively ideal parity gain, row amplitude locking,
within-rank common-component loss, and cross-depth common-sign
frustration.

Moreover,

\[
\boxed{
V-\beta
=
\sum_q\Delta_q-\mathfrak F_{\mathrm{depth}}.}
\tag{3.6}
\]

Finally,

\[
\boxed{
\mathfrak F_{\mathrm{depth}}=0
\iff
\bigcap_{q=1}^H\operatorname{argmin}R_q\ne\varnothing.}
\tag{3.7}
\]

#### Proof

Every common signing is admissible separately at each depth, so

\[
\beta
=\min_\varepsilon\sum_qR_q(\varepsilon)
\ge\sum_q\min_\varepsilon R_q(\varepsilon)
=\beta_{\mathrm{sep}}.
\]

The row-floor inequalities give \(B_q\le\beta_q\), and fair common signs
give \(\beta\le V\).  The current all-plus signing gives \(\beta\le A\).
This proves (3.3).  Equations (3.4)--(3.6) are algebraic.  Equality in the
minimum-of-a-sum inequality holds precisely when one signing minimizes
every summand, proving (3.7).  \(\square\)

Thus rankwise variance gains survive exactly when

\[
\mathfrak F_{\mathrm{depth}}<\sum_q\Delta_q.
\tag{3.8}
\]

All rankwise variance gain is erased exactly when

\[
\mathfrak F_{\mathrm{depth}}=\sum_q\Delta_q,
\tag{3.8a}
\]

equivalently, by (2.6), when \(W=0\).

### Theorem 3.2 (depth-component synchronization SDP)

For each \(q\), choose

\[
\sigma^q\in\operatorname{argmin}R_q
\tag{3.9}
\]

and set

\[
s_{qK}=\sum_{L\ne K}|w^q_{KL}|,
\qquad
S=\sum_{q,K}s_{qK}.
\tag{3.10}
\]

Define

\[
\delta_{\mathrm{depth}}
=
\min
\sum_{q,K}s_{qK}
\frac{1-\sigma_K^q\langle u_K,v_q\rangle}{2},
\tag{3.11}
\]

where the minimum is over all choices of rank minimizers in (3.9) and all
unit vectors \(u_K,v_q\).  Then

\[
\boxed{
\mathfrak F_{\mathrm{depth}}
\le4\sqrt{S\delta_{\mathrm{depth}}}.}
\tag{3.12}
\]

The sharper angular form is

\[
\boxed{
\mathfrak F_{\mathrm{depth}}
\le
4\inf
\sum_{q,K}s_{qK}
\frac{\arccos(\sigma_K^q\langle u_K,v_q\rangle)}{\pi}.}
\tag{3.13}
\]

If deleting a set \(E_0\) of labeled depth-component incidences makes the
desired relations

\[
\varepsilon_K=t_q\sigma_K^q
\tag{3.14}
\]

satisfiable, then

\[
\boxed{
\mathfrak F_{\mathrm{depth}}
\le4\sum_{(q,K)\in E_0}s_{qK}.}
\tag{3.15}
\]

In particular a forest incidence system is exactly synchronizable.

#### Proof

Fix \(q\).  Given a global signing \(\varepsilon\) and an auxiliary sign
\(t_q\), let

\[
I_q=\{K:\varepsilon_K\ne t_q\sigma_K^q\}.
\]

Only Gram edges crossing \(I_q\) change their product relative to
\(\sigma^q\), so

\[
\begin{aligned}
R_q(\varepsilon)-\beta_q
&=
-4
\sum_{\substack{K\in I_q\\L\notin I_q}}
\sigma_K^q\sigma_L^q w^q_{KL}\\
&\le
4\sum_{K\in I_q}s_{qK}.
\end{aligned}
\tag{3.16}
\]

Hyperplane-round \(u_K,v_q\) to obtain \(\varepsilon_K,t_q\).  The
violation probability is

\[
\frac{\arccos(\sigma_K^q\langle u_K,v_q\rangle)}{\pi},
\]

which proves (3.13) after summing (3.16).  Since

\[
\frac{\arccos x}{\pi}
\le\sqrt{\frac{1-x}{2}},
\]

weighted Cauchy--Schwarz proves (3.12).  Propagating signs after deleting
\(E_0\) proves (3.15).  Every rounded outcome is one common
whole-component signing.  \(\square\)

If the nonzero rank Gram graph is disconnected, one may sharpen
(3.11)--(3.15) by using one auxiliary sign and one right vertex for every
connected component of that rank graph.  The proof is unchanged.

Combining Theorem 3.2 with any rankwise AA2 gains
\(\Delta_q\ge\Gamma_q\) gives the exact-factor bound

\[
\boxed{
V-\beta
\ge
\sum_q\Gamma_q
-4\sqrt{S\delta_{\mathrm{depth}}}.}
\tag{3.17}
\]

This is the first quantitative answer to the multirank synchronization
question: a large sum of rankwise vector gains is useful only after paying
the signed depth-component holonomy.

## 4. Signed-multigraph normal form

For every rank edge \(e=(q,K,L)\), give \(e\) weight

\[
t_e=|w^q_{KL}|
\tag{4.1}
\]

and desired product

\[
\varepsilon_K\varepsilon_L
=-\operatorname{sgn}(w^q_{KL}).
\tag{4.2}
\]

Let

\[
T=\sum_et_e
\tag{4.3}
\]

and let \(\operatorname{viol}(\varepsilon)\) be the total weight of violated
desired products.  Let

\[
\operatorname{fr}
=\min_\varepsilon\operatorname{viol}(\varepsilon)
\tag{4.4}
\]

be the frustration of the rank-expanded signed multigraph.  For one depth
alone, write

\[
T_q=\sum_{K<L}|w^q_{KL}|
\]

and let \(\operatorname{fr}_q\) be its minimum frustration.

### Theorem 4.1 (three exact cancellation stages)

For every signing,

\[
\boxed{
R(\varepsilon)
=V-2T+4\operatorname{viol}(\varepsilon),}
\tag{4.5}
\]

and hence

\[
\boxed{
\beta=V-2T+4\operatorname{fr}.}
\tag{4.6}
\]

Rankwise,

\[
\beta_q=V_q-2T_q+4\operatorname{fr}_q.
\tag{4.6a}
\]

Consequently the depth-synchronization loss from Section 3 is exactly

\[
\boxed{
\mathfrak F_{\mathrm{depth}}
=
4\left(
\operatorname{fr}
-\sum_q\operatorname{fr}_q
\right).}
\tag{4.6b}
\]

For each component pair put

\[
P_{KL}=\sum_q(w^q_{KL})_+,
\qquad
M_{KL}=\sum_q(-w^q_{KL})_+.
\tag{4.7}
\]

The unavoidable cross-depth parallel-edge cancellation is

\[
C_{\mathrm{depth}}
=\sum_{K<L}\min(P_{KL},M_{KL}),
\tag{4.8}
\]

and the surviving aggregate edge has signed weight

\[
w_{KL}=P_{KL}-M_{KL}
\tag{4.9}
\]

and absolute weight

\[
|w_{KL}|=P_{KL}+M_{KL}-2\min(P_{KL},M_{KL}).
\tag{4.10}
\]

Define

\[
T_{\mathrm{agg}}=\sum_{K<L}|w_{KL}|
=T-2C_{\mathrm{depth}},
\tag{4.11}
\]

and let \(\operatorname{fr}_{\mathrm{hol}}\) be the minimum frustration in
this final aggregate signed component graph.  Then

\[
\boxed{
\operatorname{fr}
=C_{\mathrm{depth}}+\operatorname{fr}_{\mathrm{hol}},}
\tag{4.12}
\]

\[
\boxed{
V-\beta
=2T_{\mathrm{agg}}
-4\operatorname{fr}_{\mathrm{hol}}.}
\tag{4.13}
\]

The current all-plus signing violates exactly the positive aggregate edges.
Writing

\[
W_+=\sum_{w_{KL}>0}w_{KL},
\tag{4.14}
\]

one has

\[
\boxed{
C_\tau^*
=W_+-\operatorname{fr}_{\mathrm{hol}}.}
\tag{4.15}
\]

#### Proof

A satisfied edge contributes \(-2t_e\) to the off-diagonal part of
\(R\), while a violated edge contributes \(+2t_e\), proving (4.5).
Oppositely signed parallel edges on a fixed pair force the smaller total
weight to be violated under every signing.  Removing that constant leaves
one edge of weight \(|P_{KL}-M_{KL}|\), proving (4.10)--(4.13).  The
all-plus product is \(+1\), so it violates precisely the positive
aggregate edges.  Subtracting the optimal and current residuals proves
(4.15).  \(\square\)

The exact meanings are now separate:

* **variance survival**

  \[
  W\ne0
  \iff
  \operatorname{fr}_{\mathrm{hol}}<T_{\mathrm{agg}}/2;
  \tag{4.16}
  \]

* **a gain \(V-\beta\ge E\)**

  \[
  \operatorname{fr}_{\mathrm{hol}}
  \le T_{\mathrm{agg}}/2-E/4;
  \tag{4.17}
  \]

* **literal descent**

  \[
  \operatorname{fr}_{\mathrm{hol}}<W_+.
  \tag{4.18}
  \]

Signed-cycle holonomy cannot annihilate a nonzero aggregate \(W\), but it
can make the surviving fraction arbitrarily small.  Exact annihilation
occurs earlier, through parallel cancellation making every \(w_{KL}=0\).

### Orbit-atom refinement

At an orbit row \(p\), define

\[
r_{p,KL}=\alpha_pz_{pK}z_{pL}.
\tag{4.19}
\]

For every \((q,K,L)\), put

\[
P^q_{KL}
=\sum_{p:\,q(p)=q}(r_{p,KL})_+,
\qquad
M^q_{KL}
=\sum_{p:\,q(p)=q}(-r_{p,KL})_+.
\tag{4.19a}
\]

Then \(w^q_{KL}=P^q_{KL}-M^q_{KL}\).  Before (4.8), oppositely
signed atoms can therefore cancel inside one fixed \((q,K,L)\).  Define

\[
T_{\mathrm{atom}}
=\sum_{p,K<L}|r_{p,KL}|,
\qquad
C_{\mathrm{target}}
=\sum_{q,K<L}\min(P^q_{KL},M^q_{KL}).
\tag{4.19b}
\]

Retain \(C_{\mathrm{depth}}\) for the second stage, now applied after the
within-rank atom collapse.  Then the complete quadratic cancellation
identity is

\[
\boxed{
\beta
=
V-2T_{\mathrm{atom}}
+4\left(
C_{\mathrm{target}}
+C_{\mathrm{depth}}
+\operatorname{fr}_{\mathrm{hol}}
\right).}
\tag{4.20}
\]

These are target/orbit mixing, cross-depth reversal, and global component
holonomy.  This pair-interaction identity is separate from the integer
row-floor identity (3.5).

## 5. Quantitative survival criteria

Write

\[
\sigma(X)
=
\left(\sum_{K<L}X_{KL}^2\right)^{1/2}
\tag{5.1}
\]

for the unordered-edge Frobenius norm of a zero-diagonal symmetric matrix.
Also write

\[
\langle X,Y\rangle_{\mathrm{edge}}
=\sum_{K<L}X_{KL}Y_{KL}.
\tag{5.1a}
\]

### 5.1 Constant-depth mode

The orthogonal projection of the depth sequence onto its constant mode
gives the exact identity

\[
\boxed{
\sum_{q=1}^H\sigma(W_q)^2
=
\frac{\sigma(W)^2}{H}
+
\sum_{q=1}^H
\sigma\left(W_q-\frac WH\right)^2.}
\tag{5.2}
\]

Thus \(\sigma(W)^2/H\) is precisely the surviving constant-depth energy
and the last term is depth oscillation.  Define

\[
\eta_{\mathrm{depth}}
=
\frac{\sigma(W)^2}
{H\sum_q\sigma(W_q)^2}
\in[0,1]
\tag{5.3}
\]

when the denominator is nonzero.  AA2 gives

\[
\boxed{
V-\beta
\ge
\frac{2\sqrt2}{\pi}
\sqrt{
\eta_{\mathrm{depth}}H
\sum_q\sigma(W_q)^2}.}
\tag{5.4}
\]

Equivalently, if the depth Gram

\[
\mathcal C_{qr}
=\sum_{K<L}w^q_{KL}w^r_{KL}
\tag{5.5}
\]

satisfies

\[
\mathbf1^T\mathcal C\mathbf1
\ge\kappa\,\operatorname{tr}\mathcal C,
\qquad \kappa\ge0,
\tag{5.6}
\]

then

\[
V-\beta
\ge
\frac{2\sqrt{2\kappa}}{\pi}
\left(\sum_q\sigma(W_q)^2\right)^{1/2}.
\tag{5.7}
\]

Positive semidefiniteness of \(\mathcal C\) alone gives no positive
\(\kappa\).

Useful sufficient hypotheses include:

* \(\langle W_q,W_r\rangle_{\mathrm{edge}}\ge0\) for all \(q,r\);
* one fixed sign for every nonzero entry \(w^q_{KL}\) across all depths;
* a common pointed cone with a unit dual witness \(Y\) such that

  \[
  \langle Y,W_q\rangle_{\mathrm{edge}}
  \ge\kappa_0\sigma(W_q);
  \]

* one dominant rank, by the triangle bound

  \[
  \sigma(W)
  \ge
  \left(
  \sigma(W_{q_0})
  -\sum_{q\ne q_0}\sigma(W_q)
  \right)_+.
  \]

None is implied by zero margins or by the Boolean-\(E_2\) inequality and
three-slack ledger alone.

### 5.2 Pairwise noncancellation and signed degrees

Put

\[
\ell_{KL}=\sum_q|w^q_{KL}|,
\qquad
S_K=\sum_{L\ne K}\ell_{KL}.
\tag{5.8}
\]

The diagonal matrix \(\Lambda=\operatorname{diag}(S_K)\) satisfies

\[
\Lambda-W\succeq0.
\tag{5.9}
\]

Indeed, \(|w_{KL}|\le\ell_{KL}\), and edgewise signed-Laplacian squares
plus the unused diagonal mass give (5.9).  The AA2 diagonal-majorant
theorem therefore gives

\[
\boxed{
V-\beta
\ge
\frac4\pi
\sum_{\substack{K<L\\w_{KL}\ne0}}
\frac{w_{KL}^2}{\sqrt{S_KS_L}}.}
\tag{5.10}
\]

Isolated vertices with \(S_K=0\) are omitted from this formula.

If \(\kappa_0>0\) and

\[
|w_{KL}|\ge\kappa_0\ell_{KL}
\tag{5.11}
\]

on every pair with \(\ell_{KL}>0\), then

\[
\boxed{
V-\beta
\ge
\frac{4\kappa_0^2}{\pi}
\sum_{\substack{K<L\\\ell_{KL}>0}}
\frac{\ell_{KL}^2}{\sqrt{S_KS_L}}.}
\tag{5.12}
\]

If also \(S_K\le D\), this is at least

\[
\frac{4\kappa_0^2}{\pi D}
\sum_{\substack{K<L\\\ell_{KL}>0}}\ell_{KL}^2.
\tag{5.13}
\]

These statements retain heterogeneous component degrees.  They still
control improvement over fair variance, not the residual above the
discrete floor and not descent from the current corner.

### 5.3 Nonuniform component preconditioning

For arbitrary positive numbers \(a_K\), define

\[
\lambda_K(a)
=
\sum_{L\ne K}|w_{KL}|\frac{a_L}{a_K}.
\tag{5.14}
\]

Again, isolated vertices are removed; they do not affect the objective.

Then

\[
\Lambda(a)-W\succeq0.
\tag{5.15}
\]

Indeed, the contribution of edge \(KL\) to the quadratic form is

\[
|w_{KL}|
\left[
\frac{a_L}{a_K}x_K^2
+\frac{a_K}{a_L}x_L^2
-2\operatorname{sgn}(w_{KL})x_Kx_L
\right]\ge0.
\tag{5.16}
\]

Consequently there is a fair correlated whole-component law with gain

\[
\boxed{
\Gamma(a)
=
\frac4\pi\sum_{\substack{K<L\\w_{KL}\ne0}}|w_{KL}|
\arcsin\left(
\frac{|w_{KL}|}
{\sqrt{\lambda_K(a)\lambda_L(a)}}
\right),}
\tag{5.17}
\]

and

\[
\boxed{
\beta\le V-\Gamma(a).}
\tag{5.18}
\]

The ratios \(a_K\) are a genuine nonuniform covariance preconditioner.
They adapt to component heterogeneity, but they still use only the
aggregate \(W\).  No choice of \(a_K\) can see an edge erased before
(5.14).

## 6. Genuine ownership-collision interpretation

The aggregate condition has a literal prefix-collision meaning.  From
(1.1),

\[
\boxed{
w^q_{KL}
=
\frac2{c_q}
\left(
\langle a_{K,q},a_{L,q}\rangle
-
\langle a_{K,q},\tau a_{L,q}\rangle
\right).}
\tag{6.1}
\]

Thus

\[
\boxed{
W=0}
\tag{6.2}
\]

if and only if, for every genuine component pair \(K<L\), the weighted
same-side lower-prefix collision total equals its crossed collision total
over the whole window.  This is an exact necessary and sufficient
chronology statement, not a relaxation.

For a genuine component subfamily \(J\), put

\[
d_J=\sum_{K\in J}d_K,\qquad
V_J=\sum_{K\in J}\|d_K\|^2,
\tag{6.3}
\]

\[
\mathfrak B_J
=\|d_J\|^2-V_J
=2\sum_{K<L\in J}w_{KL}.
\tag{6.4}
\]

If \(\mathfrak B_J\ne0\), then \(W\ne0\).  Assume \(|J|\ge2\), and write

\[
e_J=\binom{|J|}{2}.
\]

Cauchy--Schwarz and AA2 then give

\[
\boxed{
\sigma(W)\ge\frac{|\mathfrak B_J|}{2\sqrt{e_J}},
\qquad
V-\beta
\ge
\frac{\sqrt2}{\pi\sqrt{e_J}}
|\mathfrak B_J|.}
\tag{6.5}
\]

For any anchor depth \(q_0\),

\[
\boxed{
\mathfrak B_J
\ge
\frac1{c_{q_0}}
\left\|\sum_{K\in J}d_{K,q_0}\right\|_2^2
-V_J.}
\tag{6.6}
\]

Thus one sufficiently coherent rank certifies that no cancellation at the
other ranks can erase all aggregate component geometry.

### Genuine MSW consequence

Continue to assume \(m\) is sufficiently large that \(H\le m-2\).
For the canonical MSW factor, \(\tau=(2\,3)\), and its
\(\operatorname{Cat}_{m-2}\) genuine two-for-two components \(J\), the
audited formulas give

\[
V_J
=
\operatorname{Cat}_{m-2}
\left(
\frac4{c_1}
+8\sum_{q=2}^H\frac1{c_q}
\right)
\le(8H-4)\operatorname{Cat}_{m-2}.
\tag{6.7}
\]

Put \(M=m-2\).  The exact deep-Dyck pile gives, at every eligible depth,

\[
\left\|\sum_{K\in J}d_{K,q}\right\|_2^2
\ge
2\operatorname{Cat}_{M-q}\operatorname{Cat}_q^2.
\tag{6.8}
\]

For completeness, index these components by Dyck words
\(R\in\mathcal D_M\), and write \(R=UV\) with
\(U\in\mathcal D_q\) and \(V\in\mathcal D_{M-q}\).  The insertion list
satisfies

\[
\mathsf A(UV)=\mathsf A(U)\Vert(2q+\mathsf A(V)).
\]

After the first \(q\) deletions, one positive suffix arm has core

\[
K_{q,V}=(4+2q+\mathsf A(V))\cup\{n\},
\]

independent of \(U\).  Thus its coefficient is
\(\operatorname{Cat}_q\).  Distinct \(V\)'s give distinct cores, and no
opposite-sign arm contains \(n\), so these coefficients cannot cancel.
Each resulting transposition dipole has squared norm \(2\), and there are
\(\operatorname{Cat}_{M-q}\) choices of \(V\).  This proves (6.8).

Taking \(q=H\) in (6.6) yields

\[
\boxed{
\mathfrak B_J
\ge
\frac{
2\operatorname{Cat}_{M-H}\operatorname{Cat}_H^2
}{c_H}
-O(H\operatorname{Cat}_M).}
\tag{6.9}
\]

In particular,

\[
\frac{\mathfrak B_J}{V_J}
\ge
\Omega_{A_0}\left(\frac{4^H}{H^4}\right),
\tag{6.10}
\]

because, uniformly for \(H=O_{A_0}(\sqrt M)\),

\[
\frac{\operatorname{Cat}_{M-H}}{\operatorname{Cat}_M}
=\Theta_{A_0}(4^{-H}),
\qquad
\operatorname{Cat}_H
=\Theta\left(\frac{4^H}{H^{3/2}}\right),
\]

while \(c_H=O_{A_0}(1)\) and \(V_J=O(H\operatorname{Cat}_M)\).
Thus \(\mathfrak B_J>0\) for large \(m\).  The genuine local MSW family
therefore survives the full multirank sum: its internal aggregate Gram
cannot cancel to zero.

This does not prove descent.  For \(0\le p\le1\), the exact Bernoulli
subfamily theorem is

\[
\boxed{
C_\tau^*
\ge
p\mathfrak G_J-p^2\mathfrak B_J,}
\tag{6.11}
\]

where

\[
\mathfrak G_J
=
\langle d_J,d\rangle-V_J
=
\mathfrak B_J+\langle d_J,d_{J^c}\rangle.
\tag{6.12}
\]

Here \(d=\sum_Kd_K\), as in Section 1, and
\(d_{J^c}=\sum_{K\notin J}d_K\).
To prove (6.11), select each component of \(J\) independently with
probability \(p\) and no component outside \(J\).  Then

\[
\mathbb E d_I=pd_J,
\qquad
\mathbb E\|d_I\|^2=pV_J+p^2\mathfrak B_J.
\]

Since
\(\langle d_I,d_{I^c}\rangle=\langle d_I,d\rangle-\|d_I\|^2\),
the expected cut is exactly the right side of (6.11), and some literal
component cut attains at least that expectation.

The missing quantity is alignment with the larger components.  At
\(p=1/n\), a scale-correct sufficient pair would be

\[
\mathfrak G_J
\ge
\eta_{A_0}\mathcal Q_H
-C_{1,A_0}H\operatorname{Cat}_m,
\tag{6.13}
\]

\[
\mathfrak B_J
\le
C_{2,A_0}nH\operatorname{Cat}_m.
\tag{6.14}
\]

Then

\[
C_\tau^*
\ge
\frac{\eta_{A_0}}n\mathcal Q_H
-
\frac{(C_{1,A_0}+C_{2,A_0})
H\operatorname{Cat}_m}{n}.
\tag{6.15}
\]

But (6.10) shows that the full local MSW family violates the hoped-for
\(O(n)\) internal-coherence ratio by an exponential-in-\(H\) factor.  A
naive sparse \(p=1/n\) proof does not work.  One needs favorable larger
component alignment or a genuinely pruned multiscale family.

## 7. Boolean-\(E_2\) stability and the exact surviving slack

Now let \(F\) be a global minimizer of the same fixed \(H\)-window floor
energy.  For each transposition \(\tau\), let
\(d_{\tau,K},G_{\tau,q},W_{\tau,q},V_{\tau,q},\beta_{\tau,q},
V_\tau,A_\tau,\beta_\tau\),
and likewise \(\Pi_{\tau,q},B_{\tau,q},\Pi_\tau,B_\tau\), denote the
Section 1 objects formed from that transposition's own genuine ownership
partition; set \(W_\tau=\sum_qW_{\tau,q}\).
For each transposition,

\[
\beta_\tau=A_\tau.
\tag{7.1}
\]

Therefore

\[
\Delta_\tau
:=
V_\tau-\beta_\tau
=V_\tau-A_\tau
\ge0.
\tag{7.2}
\]

By (2.6), the following are equivalent:

\[
\boxed{
\begin{aligned}
W_\tau=0
&\iff \Delta_\tau=0\\
&\iff V_\tau=A_\tau\\
&\iff\text{the fair component cube has zero drift}\\
&\iff\text{the whole \(\tau\)-switching cube is energy-flat}\\
&\iff
\langle d_{\tau,K},d_{\tau,L}\rangle=0
\quad(K\ne L).
\end{aligned}}
\tag{7.3}
\]

These statements are aggregate over all depths.  They do not imply
rankwise orthogonality or targetwise disjoint wall supports.  The prior
component-noise audit derives targetwise disjointness under the much
stronger exact global-baseline equality, including floor balance and
Johnson-\(E_2\) spectral equality; no converse is asserted here.

In all sums below, \(\tau\) ranges over the \(\binom n2\) unordered
coordinate transpositions, each counted once.  Let

\[
R_H=\sum_\tau V_\tau,\qquad
D_H=\sum_\tau A_\tau.
\tag{7.4}
\]

Then the first component-noise slack has the exact correlated-sign form

\[
\boxed{
R_H-D_H
=\sum_\tau\Delta_\tau
=\sum_\tau
\left(
2T_{\tau,\mathrm{agg}}
-4\operatorname{fr}_{\tau,\mathrm{hol}}
\right).}
\tag{7.5}
\]

Recall \(\mathcal Q_H\) from (1.2c), and define the unavoidable rank-load
variance baseline

\[
\mathcal B_H^{\mathrm{load}}
=\sum_{q\le H}\frac{V_q^{\min}}{c_q}.
\tag{7.6}
\]

Write \(f_q=\sum_jf_q^{(j)}\) for the orthogonal Johnson decomposition of
the centered load, where \(f_q^{(j)}\) is the Johnson-\(E_j\) projection.
The exact
three-slack identity refines to

\[
\boxed{
\begin{aligned}
R_H-4(n-1)\mathcal B_H^{\mathrm{load}}
={}&
\sum_\tau
\left(
2T_{\tau,\mathrm{agg}}
-4\operatorname{fr}_{\tau,\mathrm{hol}}
\right)\\
&+
2\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}
(j-2)(n-j-1)\|f_q^{(j)}\|_2^2\\
&+
4(n-1)\mathcal Q_H.
\end{aligned}}
\tag{7.7}
\]

All three lines are nonnegative at the minimizer.

Choose fixed numbers

\[
0<u<v<\min\{A_0,\sqrt{\log(17/16)}\}.
\tag{7.7a}
\]

The audited sparse Boolean-\(E_2\) stability theorem, applied on
\(u\sqrt m\le q\le v\sqrt m\), proves that for all sufficiently large
\(m\) the **last two lines together** satisfy

\[
\boxed{
2\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}
(j-2)(n-j-1)\|f_q^{(j)}\|_2^2
+
4(n-1)\mathcal Q_H
\ge
\kappa_{A_0}n\mathsf W\sqrt m}
\tag{7.8}
\]

for some \(\kappa_{A_0}>0\) depending on the fixed subwindow choice.

Equation (7.8), together with the three-slack ledger alone, gives no lower
bound at all on (7.5).  It can be paid entirely by floor or high-harmonic
slack.  Hence that Boolean-\(E_2\) inequality and ledger neither prove nor
refute aggregate Gram survival on the genuine factor fibre.

If one separately knew, for some \(\xi>0\),

\[
R_H-D_H\ge\xi n\mathsf W\sqrt m,
\tag{7.9}
\]

then some transposition would satisfy

\[
\Delta_\tau
\ge
\frac{\xi n\mathsf W\sqrt m}{\binom n2}
=
\Omega_{A_0}(H\operatorname{Cat}_m).
\tag{7.10}
\]

This is a Catalan-scale fair-variance gain.  At the minimizer it is still
**zero descent**, because
\(\beta_\tau=A_\tau\).  The antipodal current-factor law already realizes
that fair-variance improvement.

The formal connected-overlay model from the component-noise audit makes
the independence explicit in the relaxed component model: one component
for every \(\tau\) forces \(W_\tau=0\) while allowing arbitrarily large
centered high-harmonic energy.  It is not an exact middle ownership model
and therefore is not a counterexample on the genuine factor fibre.

## 8. Nonuniform covariance and Catalan-scale sufficient theorems

### 8.1 Fair gain versus descent

Let \(\Gamma_\tau\ge0\) be any proved correlated-sign improvement below fair
variance:

\[
\beta_\tau\le V_\tau-\Gamma_\tau.
\tag{8.1}
\]

This may be the AA2 diagonal-majorant gain, the nonuniform gain (5.17), an
attenuated hyperplane gain, or a contracted-block gain.  Then

\[
\boxed{
C_\tau^*
\ge
\frac{
\Gamma_\tau-(V_\tau-A_\tau)
}{4}.}
\tag{8.2}
\]

Thus a Catalan-scale fair gain is useful only after it exceeds the
coherent deficit \(V_\tau-A_\tau\).  At a factor locally minimal under
every genuine move in the \(\tau\)-component cube,

\[
\boxed{
\Gamma_\tau\le V_\tau-A_\tau}
\tag{8.3}
\]

for every legal covariance certificate.

### 8.2 Global covariance dominance

Let

\[
M=\binom n2.
\]

Averaging (8.2) gives

\[
\boxed{
\max_\tau C_\tau^*
\ge
\frac{
\sum_\tau\Gamma_\tau-(R_H-D_H)
}{4M}.}
\tag{8.4}
\]

This averages numerical lower bounds only.  The final move uses one
transposition and one genuine switching cube; no common cut across
transpositions is asserted.

Consequently, for fixed constants \(\eta_{A_0}>0\) and
\(C_{A_0}^{\mathrm{cov}}<\infty\), the following is a route-closing
sufficient hypothesis:

\[
\boxed{
\sum_\tau\Gamma_\tau
\ge
(R_H-D_H)
+
2(n-1)
\left[
\eta_{A_0}\mathcal Q_H
-C_{A_0}^{\mathrm{cov}}H\operatorname{Cat}_m
\right].}
\tag{8.5}
\]

Indeed, since \(4M=2n(n-1)\), (8.4) gives

\[
\boxed{
\max_\tau C_\tau^*
\ge
\frac{\eta_{A_0}}n\mathcal Q_H
-
\frac{C_{A_0}^{\mathrm{cov}}}nH\operatorname{Cat}_m.}
\tag{8.6}
\]

Unlike the refuted global-noise gate, (8.5) compares covariance gain only
with the first switching slack \(R_H-D_H\).  It allows the large
Boolean-\(E_2\) floor and high-harmonic slacks in (7.8).  At a factor
locally minimal under every genuine transposition-component cube move,
(8.3) forces the reverse inequality
\(\sum_\tau\Gamma_\tau\le R_H-D_H\); therefore (8.5) is exactly the new
genuine geometry burden, not a consequence of the old ledger.

### 8.3 Nonuniform depth tilting

For auxiliary multipliers \(\lambda_q>0\), define

\[
R_\lambda(\varepsilon)=\sum_q\lambda_qR_q(\varepsilon),
\qquad
B_\lambda=\sum_q\lambda_qB_q,
\tag{8.7}
\]

\[
\beta_\lambda=\min_\varepsilon R_\lambda(\varepsilon),
\qquad
\lambda_*=\min_q\lambda_q.
\]

Since every depth excess \(R_q(\varepsilon)-B_q\) is nonnegative,

\[
\boxed{
\beta-B
\le
\frac{\beta_\lambda-B_\lambda}{\lambda_*}.}
\tag{8.8}
\]

The theorem is scale invariant, so one may normalize \(\lambda_*=1\).
Moreover,

\[
\inf_{\lambda_q>0}
\frac{\beta_\lambda-B_\lambda}{\lambda_*}
=\beta-B,
\tag{8.9}
\]

because (8.8) is a lower bound on every tilted expression and
\(\lambda_q\equiv1\) attains equality.  Depth tilting is therefore a
preconditioner for proof certificates, not a new exact-factor freedom.

More generally, partition components into blocks, fix internal relative
signs \(\theta_K\), and put

\[
g_{D,q}=\sum_{K\in D}\theta_Kd_{K,q}.
\tag{8.10}
\]

Stack \(\sqrt{\lambda_q/c_q}\,g_{D,q}\) over \(q\).  Let
\(V_{\lambda,\mathscr D}\) be the sum of the block squared norms.  For a
positive diagonal \(\Lambda\) majorizing the zero-diagonal contracted
block Gram as in Theorem 3.1 of AA2, let
\(\Gamma_{\lambda,\mathscr D,\Lambda}\) be its valid angular gain.  Then

\[
\boxed{
\beta-B
\le
\frac{
V_{\lambda,\mathscr D}
-B_\lambda
-\Gamma_{\lambda,\mathscr D,\Lambda}
}{\lambda_*}.}
\tag{8.11}
\]

Every block-sign outcome lifts to whole original components.

There is an important exact limitation.  If the infimum is unrestricted,
then

\[
\boxed{
\inf_{\text{all admissible }(\lambda,\mathscr D,\theta,\Lambda)}
\frac{
V_{\lambda,\mathscr D}
-B_\lambda
-\Gamma_{\lambda,\mathscr D,\Lambda}
}{\lambda_*}
=\beta-B.}
\tag{8.12}
\]

Indeed, (8.11) gives the lower bound.  For the reverse bound, take
\(\lambda_q=1\), put every component in one block, and choose its internal
signs \(\theta\) to attain \(\beta\).  The one-vertex contracted Gram has
zero off-diagonal part, so \(\Gamma=0\), while
\(V_{\lambda,\mathscr D}=\beta\).  Thus unrestricted nonuniform
preconditioning merely hides the unknown optimum and supplies no new
theorem.

To obtain a genuine certificate, fix in advance a nonempty controlled
admissible class \(\mathfrak C_\tau\) of tilts, blocks, internal signs, and diagonal
majorants, defined from literal ownership geometry without knowing an
optimal signing, and write \(\mathfrak R_\tau(\mathfrak C_\tau)\) for the
same infimum restricted to that class.  The nonuniform sufficient
condition is

\[
B-\Pi+\mathfrak R_\tau(\mathfrak C_\tau)
=
O_{A_0}\!\left(
\frac{H\operatorname{Cat}_m}{n}\right).
\tag{8.13}
\]

By (8.11), condition (8.13) implies
\(\beta-\Pi=O_{A_0}(H\operatorname{Cat}_m/n)\).  Together with a
scale-correct ideal-gain estimate for the same transposition, it proves the
lane-AA local-minimum theorem.  No such controlled class satisfying
(8.13) is known for genuine factors.

### 8.4 A simpler depth-synchronization sufficient condition

Theorems 3.1--3.2 show that it is enough to prove, for the same
transposition,

\[
B-\Pi
=
O_{A_0}\!\left(
\frac{H\operatorname{Cat}_m}{n}\right),
\tag{8.14}
\]

\[
\sum_q(\beta_q-B_q)
=
O_{A_0}\!\left(
\frac{H\operatorname{Cat}_m}{n}\right),
\tag{8.15}
\]

\[
S\delta_{\mathrm{depth}}
=
O_{A_0}\!\left(
\frac{H^2\operatorname{Cat}_m^2}{n^2}\right).
\tag{8.16}
\]

These are respectively local amplitude, within-rank synchronization, and
cross-depth synchronization.  All three are **UNPROVED** on the genuine
factor fibre.  The Boolean-\(E_2\) inequality and three-slack ledger alone
control none of (8.14)--(8.16).

## 9. Sharp bounded-degree multirank obstruction

This section constructs an abstract signed-row system.  It satisfies the
listed integral and marginal constraints but is not asserted to be a
genuine ownership-component system of an exact factor.

Let \(\mathcal G\) be a connected \(d\)-regular bipartite graph on an even
number \(N\) of component vertices.  Give every row a common weight
\(a=2\), the actual orbit-row weight at depths with \(c_q=1\).

At depth \(+\), for every graph edge \(ij\), use the two rows

\[
\pm(e_i+e_j).
\tag{9.1}
\]

At depth \(-\), use

\[
\pm(e_i-e_j).
\tag{9.2}
\]

Then

\[
G_+
=
2a\sum_{ij\in E(\mathcal G)}
(e_i+e_j)(e_i+e_j)^T
=2a(dI+A_{\mathcal G}),
\tag{9.3}
\]

\[
G_-
=
2a\sum_{ij\in E(\mathcal G)}
(e_i-e_j)(e_i-e_j)^T
=2a(dI-A_{\mathcal G}).
\tag{9.4}
\]

The bipartition signing makes the \(+\) objective zero, while the
all-equal signing makes the \(-\) objective zero.  Hence

\[
\Pi_+=B_+=\beta_+=0,
\qquad
\Pi_-=B_-=\beta_-=0.
\tag{9.5}
\]

But

\[
\boxed{
G_++G_-=4adI_N,}
\tag{9.6}
\]

so

\[
\boxed{
\Pi=B=0,\qquad
A=V=\beta=4adN.}
\tag{9.7}
\]

Every common signing has the same full-window energy.  Equivalently,

\[
\mathfrak F_{\mathrm{depth}}
=\Delta_++\Delta_-
=V,
\tag{9.8}
\]

so all rankwise gain is consumed by depth synchronization.

The array has:

* row arity two and coefficients in \(\{0,\pm1\}\);
* exact parity and row floor zero;
* balanced columns, because every row has its negated twin;
* component incidence degree \(4d\);
* nonnegative row-level \(0/1\) old/new pair tables, without any assertion
  of unique global middle-mask ownership;
* zero derivative point margins when the rows are placed on distinct
  transposition cores.

It survives the full cut polytope, every SDP or sum-of-squares hierarchy,
all metric constraints, diagonal majorants, conditional-product rounding,
block contraction, and partial coloring, because the aggregate objective
is literally constant.

Depth tilting is exactly powerless.  For \(\lambda_+,\lambda_->0\),
every graph edge costs \(8a\lambda_+\) when its endpoints agree and
\(8a\lambda_-\) when they differ.  The all-equal and bipartition signings
give

\[
\boxed{
\beta_\lambda
=4adN\min\{\lambda_+,\lambda_-\},}
\tag{9.9}
\]

so

\[
\frac{\beta_\lambda}{\min\{\lambda_+,\lambda_-\}}
=4adN=\beta
\tag{9.10}
\]

for every tilt.

For \(q=1,2\), one has \(c_1=c_2=1\) for all sufficiently large \(m\), so
the two orbit-row weights are already identical in the actual window
normalization; in the convention above their actual value is \(a=2\).
Take \(d=2\) and let \(\mathcal G=C_N\), so a connected regular bipartite
graph exists for every even \(N\ge4\).  Setting

\[
N=2\left\lfloor
\frac{\operatorname{Cat}_m}{2}
\right\rfloor
\tag{9.11}
\]

gives

\[
\beta-B=\Theta(\operatorname{Cat}_m),
\tag{9.12}
\]

whereas

\[
\frac{H\operatorname{Cat}_m}{n}
=
\Theta_{A_0}\left(
\frac{\operatorname{Cat}_m}{\sqrt m}
\right).
\tag{9.13}
\]

The separation factor is \(\Theta_{A_0}(\sqrt m)\).

For \(q=1,2\), the exact number of moved target orbits is

\[
\binom{n-2}{m-q-1}
=\Theta(\mathsf W)
=\Theta(n\operatorname{Cat}_m),
\tag{9.13a}
\]

so ambient row capacity is not the issue.  The array is nevertheless
**not proved** to arise from complete cyclic-window histograms or connected genuine
ownership components.  The absent property is exactly common
nested-prefix chronology.

### Holonomy can also make the surviving fraction vanish

At the final aggregate signed-graph stage, ordinary signed-cycle holonomy
can leave only a vanishing fraction of gross correlation.  For
every Hadamard order \(s\), for instance \(s=2^k\), let
\(\mathcal H_s\) be an \(s\times s\) Hadamard matrix and use its signs as
weights on \(K_{s,s}\).  Adding a sufficiently large common diagonal
makes the resulting symmetric matrix positive semidefinite, hence a
formal signed Gram graph, without changing any signing gain.  The
aggregate absolute edge mass is \(s^2\), but

\[
\max_{x,y\in\{\pm1\}^s}|x^T\mathcal H_sy|
\le
\|x\|_2\|\mathcal H_s\|_{\mathrm{op}}\|y\|_2
=s^{3/2}.
\tag{9.14}
\]

Thus the best correlated-sign gain is at most \(O(s^{3/2})\), only an
\(O(s^{-1/2})\) fraction of the gross edge mass.  This is another formal
Gram graph, not a wreath obstruction.  It shows that mere noncancellation
is weaker than the aggregate holonomy control needed to turn (8.2) into
descent.

## 10. Exact final implications and remaining lemmas

The third-wave results distinguish four burdens.  All constants below may
depend on the fixed \(A_0\) but not on \(m\); require
\(\eta_{A_0}>0\) and \(C_{A_0}^{\mathrm{id}}<\infty\).

1. **same-transposition ideal gain**

   \[
   A_\tau-\Pi_\tau
   \ge
   \frac{4\eta_{A_0}}n\mathcal Q_H
   -
   \frac{C_{A_0}^{\mathrm{id}}H\operatorname{Cat}_m}{n};
   \]

2. **local amplitude**

   \[
   B_\tau-\Pi_\tau
   =
   O_{A_0}(H\operatorname{Cat}_m/n);
   \]

3. **within-rank component synchronization**

   \[
   \sum_q(\beta_{\tau,q}-B_{\tau,q})
   =
   O_{A_0}(H\operatorname{Cat}_m/n);
   \]

4. **cross-depth synchronization**

   \[
   \mathfrak F_{\tau,\mathrm{depth}}
   =
   O_{A_0}(H\operatorname{Cat}_m/n).
   \]

If these four estimates hold for one and the same transposition, then

\[
C_\tau^*
\ge
\frac{\eta_{A_0}}n\mathcal Q_H
-
O_{A_0}\left(
\frac{H\operatorname{Cat}_m}{n}\right).
\tag{10.1}
\]

Consequently, any factor for which the four estimates hold and which is
locally minimal under all genuine transposition-component cube moves has

\[
\mathcal Q_H=O_{A_0}(H\operatorname{Cat}_m),
\tag{10.2}
\]

which yields fixed-window unlabelled overload for this fixed \(A_0\).  If
the statement holds for every fixed \(A_0>0\), the frozen diagonalization
then yields MWB and the asymptotic contiguous-OR width theorem.  It does
not give labelled common-owner synchronization.

No theorem in this report proves the four genuine estimates.  The exact
new candidate is:

> **UNPROVED genuine multirank signed-ownership lemma.**  
> For every fixed \(A_0>0\), there are constants
> \(\eta_{A_0},C_{A_0}^{\mathrm{thr}},C_{A_0}^{\mathrm{id}}>0\) and
> \(m_0(A_0)\) such that, whenever
> \(m\ge m_0(A_0)\) and an exact factor satisfies
> \[
> \mathcal Q_H(F)>C_{A_0}^{\mathrm{thr}}H\operatorname{Cat}_m,
> \]
> there is one transposition \(\tau\) whose literal cyclic-prefix
> ownership components satisfy the same-\(\tau\) ideal-gain inequality and
> either (8.14)--(8.16), or a geometrically controlled nonuniform
> certificate of the form (8.13).

A weaker rank-faithfulness estimate such as

\[
\sigma\left(\sum_qW_{\tau,q}\right)^2
\ge
\rho_{A_0}H\sum_q\sigma(W_{\tau,q})^2,
\qquad \rho_{A_0}>0,
\tag{10.3}
\]

proves only improvement over fair variance.  It does not control the
discrete residual \(V_\tau-B_\tau\), holonomy strongly enough relative to
\(T_{\tau,\mathrm{agg}}\), or current-corner optimality, and therefore is
not route-closing by itself.

Adaptive moves which switch a factor and then recompute ownership
components can escape the fixed-overlay obstruction.  They are a
different theorem: the covariance-collapse result applies to every move
which fixes one ownership partition before choosing one final exact
factor.

## 11. Independent audit record

The decisive identities were independently rederived in three
normalizations.

* The covariance-collapse identity (2.3) uses one cut-correlation matrix
  and is exact for arbitrary dependent signs.
* The depth-frustration constant in (3.12) is \(4\); it comes from the
  exact mismatch-cut expansion (3.16).
* With unordered-edge Frobenius norm, the AA2 coefficient is
  \(2\sqrt2/\pi\); with the full symmetric matrix Frobenius norm it is
  \(2/\pi\).
* The signed-multigraph formulas (4.13) and (4.15) independently recover
  the AA2 distinction between fair-variance gain and literal descent.
* The bounded-degree obstruction has
  \(G_++G_-=4adI_N\), \(\beta=4adN\), and route-critical separation factor
  \(n/H=\Theta_{A_0}(\sqrt m)\).
* The Boolean-\(E_2\) bridge was checked against the exact three-slack
  normalization: its quantitative lower bound is on the floor and
  high-harmonic lines of (7.7), not on the component-Gram line.

The theorem-level conclusion is therefore exact:

\[
\boxed{
\text{Nonuniform correlated signs can exploit only the aggregate
same-\(\tau\) Gram that survives the whole window.}}
\]

The present ledger proves Catalan-scale descent from the current factor if
genuine cyclic-prefix geometry controls amplitude, within-rank
frustration, cross-depth reversal, aggregate holonomy, and current-sign
optimality at the displayed scales.  The Boolean-\(E_2\) inequality and
three-slack ledger alone supply none of these signed ownership controls.
