# Gate A: the sequential random-greedy clock, exact hazard contraction, and the surviving state-Palm gate

**Date:** 2026-08-22  
**Status:** unconditional sequential-clock reduction; it removes the
parallel-bite remainder and accepted-count randomness, but it does not prove
the punctured ancestor-row regression

## 0. Verdict

Replacing a parallel isolated-row microbite by one uniformly chosen alive
row is mathematically legitimate and gives two useful exact simplifications.

1. At jump number \(j\), every shore has deterministic size.  There is no
   accepted-count conditioning and no random-size reference mixture.
2. For a carrier family in one deterministic current state, the mean hazard
   after one surviving jump obeys the exact formula

   \[
   \boxed{
   \mu^+=\mu-\frac{\tau+V}{Z-\mu},\qquad
   \tau=\mathbb E T_\gamma,\quad V=\operatorname {Var}h_\gamma.}
                                                               \tag{0.1}
   \]

Thus the finite-bite \(O((p\Delta_C)^2)\) error disappears completely, and
the profile \(\kappa=\tau+V\) isolated in Appendix G.9 of
`MASTER_HANDOFF.md` is the literal one-row decrement.

The change does **not** close Gate A.  The embedded jump chain chooses a row
with probability \(1/Z(H)\), so its exact ancestor-row statistic is still

\[
                         \mathbb E\left[\frac{h(H,\gamma)}{Z(H)}
                                  \mathrel{\Big|}d_{\rm anc}=d\right].
                                                               \tag{0.2}
\]

Poissonizing the chain by giving every alive row rate one removes \(1/Z\)
from the generator at fixed physical time.  But stopping after a prescribed
number of rows, which is what makes the shore sizes deterministic, gives
waiting time \(E_j/Z(H_j)\), with \(E_j\sim\operatorname {Exp}(1)\), and
puts the same factor back.  At fixed physical time the number of selected
rows, hence the shore sizes and realized centers, are random.

More importantly, under either clock a carrier-Palm law is a mixture of
current states.  Conditioning a deterministic-state row does not control
the between-state covariance in the total covariance identity.  The exact
continuous-time form of the remaining theorem is the regression of

\[
 \boxed{
 \kappa_d^{\rm Palm}(t)
 =\mathbb E[T_\gamma\mid d_{\rm anc}=d]
   +\operatorname {Var}(h_\gamma\mid d_{\rm anc}=d),}       \tag{0.3}
\]

where the variance includes the between-state variance.  A literal graph
example in Section 7 has strictly adverse high-tail drift under one uniform
row.  Therefore no generic monotonicity or cap argument can replace the
punctured-specific regression theorem.

What the sequential route rigorously buys is a sharper Gate-A reduction:
parallel-bite Taylor errors and accepted-count fibres disappear, while the
entire future \(1/Z(H_K)\) and survivor-reweighting effect on normalized
hazard is \(O((\Delta_C/Z)^2)\) pointwise and hence exponentially summable.
The live obstacles are the **contemporaneous** stopped state-Palm
hazard--degree regression, the predictable edge-count/center drift, and the
actual/reference erosion comparison.
The sequential chain is a different matching law from the parallel nibble.
Although every selected set is still a legitimate matching, stopped
moment, degree-floor, purge, and descent estimates proved only for the
parallel law must be transferred at generator level; they cannot simply be
quoted for the new process.

## 1. The uniform-row deletion chain

Let \(H=(V,E)\) be a finite simple hypergraph.  For \(K\in E\), write

\[
 \Gamma_H(K)=\{R\in E:R\cap K\ne\varnothing\},\qquad
 C_K=|\Gamma_H(K)|,\qquad Z=|E|,                            \tag{1.1}
\]

and let

\[
 H_K=H[V\setminus K],\qquad E(H_K)=E\setminus\Gamma_H(K). \tag{1.2}
\]

The discrete uniform-row random-greedy chain chooses \(K\) uniformly from
\(E(H)\) and replaces \(H\) by \(H_K\).  Rows selected at different times
are vertex-disjoint.

Suppose every row has exactly \(k_\sigma\) vertices on shore \(V_\sigma\).
If \(N_j\) rows have been selected, then pathwise

\[
             n_{j,\sigma}=n_{0,\sigma}-k_\sigma N_j.       \tag{1.3}
\]

In the embedded chain \(N_j=j\).  Thus all shore sizes are deterministic
at a fixed jump number.

Fix \(m\ge2\).  An ordered \(m\)-carrier is

\[
                   \gamma=(v;F_1,\ldots,F_m),              \tag{1.4}
\]

where the distinct rows \(F_i\) contain the root \(v\).  Put

\[
 B_\gamma=\bigcup_{i=1}^m\Gamma_H(F_i),\qquad
 D_\gamma=E\setminus B_\gamma,\qquad h_\gamma=|B_\gamma|, \tag{1.5}
\]

and, for \(K\in D_\gamma\),

\[
 t_\gamma(K)=|\Gamma_H(K)\cap B_\gamma|,\qquad
 T_\gamma=\sum_{K\in D_\gamma}t_\gamma(K).                \tag{1.6}
\]

If \(\Delta_C=\max_KC_K\), then

\[
 h_\gamma\le m\Delta_C,\qquad
 0\le t_\gamma(K)\le\Delta_C,\qquad
 0\le T_\gamma\le h_\gamma\Delta_C.                      \tag{1.7}
\]

## 2. Exact one-row carrier identities

### Theorem 2.1 (one carrier)

For a fixed current carrier \(\gamma\), let \(A_\gamma\) be its survival
event through the next uniform-row jump.  Then

\[
 \boxed{\Pr(A_\gamma\mid H,\gamma)=1-\frac{h_\gamma}{Z}.}   \tag{2.1}
\]

Conditional on \(A_\gamma\), the selected row is uniform on \(D_\gamma\),
and

\[
 \boxed{
 h_\gamma(H_K)=h_\gamma-t_\gamma(K),\qquad
 \mathbb E[h_\gamma(H_K)\mid A_\gamma,H,\gamma]
 =h_\gamma-\frac{T_\gamma}{Z-h_\gamma}.}                  \tag{2.2}
\]

#### Proof

The carrier survives exactly when the selected row meets none of the
\(F_i\), namely when \(K\notin B_\gamma\).  This proves (2.1) and makes the
conditional choice uniform on \(D_\gamma\).  When \(K\in D_\gamma\), all
carrier rows survive, while precisely the rows of
\(B_\gamma\cap\Gamma_H(K)\) disappear.  Hence the first identity in (2.2)
holds.  Averaging it over the \(Z-h_\gamma\) rows of \(D_\gamma\) proves
the second.  \(\square\)

### Theorem 2.2 (a whole carrier family)

Let \(\mathcal C\) be a nonempty labelled carrier family in one
deterministic state \(H\), sampled uniformly.  Define

\[
 \mu=\mathbb E_{\mathcal C}h_\gamma,\qquad
 \tau=\mathbb E_{\mathcal C}T_\gamma,\qquad
 V=\operatorname {Var}_{\mathcal C}h_\gamma.               \tag{2.3}
\]

Sample \(\gamma\) uniformly from \(\mathcal C\), make one uniform-row
jump, and condition on carrier survival.  If \(Z>\mu\), then

\[
 \boxed{
 \mathbb E[h_\gamma(H_K)\mid A_\gamma,H,\gamma\in\mathcal C]
 =\mu-\frac{\tau+V}{Z-\mu}.}                              \tag{2.4}
\]

#### Proof

The surviving pair \((\gamma,K)\), before normalization, is uniform on

\[
                 \{(\gamma,K):\gamma\in\mathcal C,
                                      K\in D_\gamma\}.      \tag{2.5}
\]

Its total size is \(|\mathcal C|(Z-\mu)\).  Therefore the numerator of
the conditional mean in (2.4), divided by \(|\mathcal C|\), is

\[
 \mathbb E_{\mathcal C}\left[(Z-h_\gamma)h_\gamma-T_\gamma\right]
 =Z\mu-\mathbb E h_\gamma^2-\tau.                         \tag{2.6}
\]

Since \(\mathbb E h^2=\mu^2+V\), division by \(Z-\mu\) gives (2.4).
\(\square\)

The variance term in (2.4) is structural.  It is the exact size-bias from
the fact that lower-hazard carriers have more possible surviving rows.

### Corollary 2.3 (the next predictable rate)

Assume \(\Delta_C\le D\) and \(Z>D\).  Under the surviving-pair law of
Theorem 2.2, put

\[
 q^+_{\mathcal C}
 =\mathbb E\left[\frac{h_\gamma(H_K)}{|E(H_K)|}
                  \mathrel{\Big|}A_\gamma,H,
                  \gamma\in\mathcal C\right].             \tag{2.7}
\]

Then, with \(\kappa=\tau+V\),

\[
 \boxed{
 q^+_{\mathcal C}
 =\frac1Z\left(\mu-\frac{\kappa}{Z-\mu}\right)
   +\varepsilon_{\mathcal C},\qquad
 0\le\varepsilon_{\mathcal C}
 \le\frac{mD^2}{Z(Z-D)}.}                                 \tag{2.8}
\]

#### Proof

For the selected \(K\), \(|E(H_K)|=Z-C_K\).  Hence

\[
 \frac{h_\gamma(H_K)}{Z-C_K}-\frac{h_\gamma(H_K)}Z
 =\frac{h_\gamma(H_K)C_K}{Z(Z-C_K)}.                      \tag{2.9}
\]

The right side is nonnegative and at most
\(mD^2/[Z(Z-D)]\).  Average (2.9) and use (2.4).  \(\square\)

Thus the variation of the **immediate** child denominator is uniformly
tiny when \(D/Z\) is tiny.  This does not compare \(Z(H)\) between two
different state histories in a carrier-Palm mixture.

### Theorem 2.3bis (pointwise normalized-hazard persistence)

For one carrier state put

\[
 s=\frac hZ,\qquad a=1-s,qquad
 \beta_s=\mathbb E\left[
   \mathbf1_{A_\gamma}\frac{h_\gamma(H_K)}{|E(H_K)|}
                         \mathrel{\Big|}H,\gamma\right].    \tag{2.9a}
\]

If \(\Delta_C\le D<Z\), then

\[
 \boxed{
 \beta_s=as+r_s,\qquad
 |r_s|\le\frac{2hD}{Z(Z-D)}
          \le\frac{2mD^2}{Z(Z-D)}.}                        \tag{2.9b}
\]

This estimate is pointwise in the full state and carrier; no state fibre
or common value of \(Z\) is assumed.

#### Proof

On survival by a row \(K\in D_\gamma\), write \(C=C_K\) and
\(t=t_\gamma(K)\).  Then

\[
 \frac{h-t}{Z-C}-\frac hZ=\frac{hC-Zt}{Z(Z-C)}.            \tag{2.9c}
\]

Since both \(\beta_s\) and \(as\) average the two terms of (2.9c) with
unconditional row weight \(1/Z\),

\[
 |r_s|
 \le\frac1Z\sum_{K\in D_\gamma}
       \frac{hC_K+Zt_\gamma(K)}{Z(Z-C_K)}
 \le\frac{hD+T_\gamma}{Z(Z-D)}.                           \tag{2.9d}
\]

Use \(T_\gamma\le hD\) and \(h\le mD\).  \(\square\)

Now let \(\mu\) be **any** carrier law, possibly a mixture of states and
possibly restricted to one predictably chosen ancestor cohort.  Assume

\[
             \theta=\sup_{(H,\gamma)\in\operatorname {supp}\mu}
                         \frac{\Delta_C(H)}{Z(H)},qquad
             m\theta<1.                                   \tag{2.9e}
\]

Write \(\bar s=\mathbb E_\mu s\), and let \(\bar s^+\) be the mean child
normalized hazard under the surviving-carrier Palm law.  Averaging
(2.9b) gives the exact identity and uniform bounds

\[
 \boxed{
 \bar s^+-\bar s
 =\frac{-\operatorname {Var}_\mu(s)+\mathbb E_\mu r_s}
        {1-\bar s},}                                      \tag{2.9f}
\]

\[
 \boxed{
 \bar s^+-\bar s
 \le \frac{2m\theta^2}{(1-\theta)(1-m\theta)},\qquad
 |\bar s^+-\bar s|
 \le\frac{m^2\theta^2/4+2m\theta^2/(1-\theta)}
          {1-m\theta}.}                                   \tag{2.9g}
\]

Indeed \(\mathbb E(as)=\bar s-\mathbb Es^2\),
\(\mathbb Ea=1-\bar s\), and a variable in
\([0,m\theta]\) has variance at most \(m^2\theta^2/4\).

Theorem 2.3bis removes the hidden **future** global-size factor: even after
arbitrary state mixing, the mean normalized hazard of a fixed ancestor
cohort can rise by only \(O_m(\theta^2)\) in one jump.  It does not refresh
or regularize that cohort.  If \(\bar s\) already has adverse covariance
with ancestor degree, (2.9f) says that the covariance persists up to a
quadratic error.  This persistence is precisely why the theorem is a
reduction rather than a closure.

### Proposition 2.4 (the extension hierarchy is exact for one row)

Fix a set \(B\) of root labels.  Let \(X_t(B;H)\) count tuples consisting
of a labelled carrier rooted in \(B\) and \(t\) ordered rows which are
pairwise vertex-disjoint and disjoint from every carrier row.  Then

\[
                  \boxed{\sum_{K\in E(H)}X_t(B;H_K)
                         =X_{t+1}(B;H).}                    \tag{2.10}
\]

Consequently one uniform-row jump satisfies

\[
                 \boxed{\mathbb E[X_t(B;H_K)\mid H]
                         ={X_{t+1}(B;H)\over Z}.}           \tag{2.11}
\]

If \(q_t=X_{t+1}/X_t\), then, whenever the denominator is positive,

\[
 \boxed{
 {\mathbb E[X_1(B;H_K)\mid H]
  \over\mathbb E[X_0(B;H_K)\mid H]}=q_1(B;H).}             \tag{2.12}
\]

#### Proof

Prefixing an object counted by \(X_t(B;H_K)\) with \(K\) gives a unique
object counted by \(X_{t+1}(B;H)\).  Conversely, deleting the first
extension row of an object counted by \(X_{t+1}\) leaves its unique suffix
in the corresponding \(H_K\).  This proves (2.10); division by \(Z\) gives
(2.11)--(2.12).  \(\square\)

This is the cleanest sequential use of the avoidance hierarchy: the
deterministic-parent descendant row is exactly \(q_1\), to which the
fixed-state curvature estimate of Appendix G.7 applies.  For a state law
\(\nu\), however,

\[
 {\mathbb E_{\nu P}X_{t+1}\over\mathbb E_{\nu P}X_t}
 =\frac{\mathbb E_\nu[X_{t+2}/Z]}
        {\mathbb E_\nu[X_{t+1}/Z]}.                        \tag{2.13}
\]

The state-dependent reciprocal does not cancel outside one deterministic
parent.  Equation (2.13) is an exact form of the surviving global-size
Simpson obstruction.

### Corollary 2.5 (backward extension martingale and exact path tilt)

Fix an integer horizon \(L\).  Along the uniform-row chain, for
\(0\le j\le L\), put

\[
 \boxed{
 M_j^{(L)}=\left(\prod_{i<j}Z_i\right)X_{L-j}(B;H_j).}      \tag{2.14}
\]

Until extinction, \(M_j^{(L)}\) is a martingale.  In particular,

\[
 \boxed{
 \mathbb E\left[X_0(B;H_L)\prod_{i<L}Z_i\right]
 =X_L(B;H_0).}                                             \tag{2.15}
\]

#### Proof

Conditioning at time \(j\) and applying (2.11) with \(t=L-j-1\) gives

\[
\begin{aligned}
 \mathbb E[M_{j+1}^{(L)}\mid\mathcal F_j]
 &=\left(\prod_{i<j}Z_i\right)Z_j
   {X_{L-j}(B;H_j)\over Z_j}\\
 &=M_j^{(L)}.
\end{aligned}                                               \tag{2.16}
\]

This proves both claims.  \(\square\)

There is a useful likelihood interpretation.  An ordered matching path
\(P=(K_0,\ldots,K_{L-1})\) has random-greedy probability

\[
                         \Pr_{\rm RG}(P)=\prod_{i<L}Z_i(P)^{-1}.
                                                               \tag{2.17}
\]

Consequently the terminal random-greedy carrier-Palm law is the uniform
counting law on carrier--extension pairs tilted by the exact path weight

\[
             \exp\left\{-\sum_{i<L}\log Z_i(P)\right\}.    \tag{2.18}
\]

The extension martingale therefore does not itself remove state-Palm
mixing; it identifies its likelihood ratio.  Even exponentially small
martingale noise of each \(Z_i\) about its own predictable compensator does
not compare (2.18) across histories.  Such a comparison would require a
bound for the accumulated path action \(\sum_i\log Z_i\), including the
state-dependent predictable drift.  This is an alternative formulation of
the global-size gate, not a consequence of the cap.

## 3. Exact Palm recursion and the deterministic-size reference

Let \(\nu\) be any finite law on current states and adjoin every current
labelled carrier with counting multiplicity.  Write \(\widehat\nu\) for
the normalized carrier-Palm law.  Let \(\Phi\ge0\) be a carrier test which
does not increase on a surviving transition.  Put

\[
 a(H,\gamma)=1-\frac{h(H,\gamma)}{Z(H)},                    \tag{3.1}
\]

and let \(e(H,\gamma)\ge0\) be the expected loss of \(\Phi\) along
surviving transitions.  If \(A=\mathbb E_{\widehat\nu}\Phi\), the unique
labelled-parent count gives the exact recursion

\[
 \boxed{
 A^+-A=
 \frac{-\operatorname {Cov}_{\widehat\nu}(h/Z,\Phi)
       -\mathbb E_{\widehat\nu}e}
      {1-\mathbb E_{\widehat\nu}(h/Z)}.}                  \tag{3.2}
\]

There is no Taylor remainder in (3.2).  The only sign-indefinite term is
the covariance with the literal sequential rate \(h/Z\).

At jump number \(j\), (1.3) permits a deterministic uniform-slice
reference.  Delete a uniformly chosen \(k_\sigma\)-subset from every shore.
If a carrier uses \(b_{\gamma\sigma}\) distinct targets on shore
\(\sigma\), its exact reference survival factor is

\[
 \boxed{
 a^0_j(\gamma)=
 \prod_\sigma
 \frac{(n_{j,\sigma}-k_\sigma)_{b_{\gamma\sigma}}}
      {(n_{j,\sigma})_{b_{\gamma\sigma}}}.}                \tag{3.3}
\]

The uniform nested kernel maps the uniform slice at jump \(j\) to the
uniform slice at jump \(j+1\).  Hence the usual reference Palm recursion
is exact and no random-size mixture is needed.  Equations (3.2)--(3.3),
however, still leave the one-sided comparison of the actual and reference
survival-payoff quotients, including favourable erosion.

## 4. Embedded jump number versus physical time

Give every alive row an independent rate-one exponential clock.  When a
clock rings, select that row and pass to \(H_K\).  The generator is

\[
                 (\mathcal Lf)(H)=
                 \sum_{K\in E(H)}\{f(H_K)-f(H)\}.           \tag{4.1}
\]

Its embedded chain is exactly the uniform-row chain, because the total
rate is \(Z(H)\) and each row has the same rate.

### Theorem 4.1 (exact carrier generator)

Let \(I_\gamma(t)\) be the indicator that a fixed labelled carrier history
is alive, and put \(Y_\gamma=I_\gamma h_\gamma\).  Then

\[
 \boxed{\mathcal LI_\gamma=-I_\gamma h_\gamma,\qquad
 \mathcal LY_\gamma=-I_\gamma(h_\gamma^2+T_\gamma).}       \tag{4.2}
\]

#### Proof

Each of the \(h_\gamma\) rows in \(B_\gamma\) kills the carrier and hence
changes \(I_\gamma\) by \(-1\) and \(Y_\gamma\) by \(-h_\gamma\).  A row
\(K\in D_\gamma\) preserves the carrier and changes its hazard by
\(-t_\gamma(K)\).  Summing these generator increments gives (4.2).
\(\square\)

Let \(\mathcal C_0\) be any initial labelled carrier cohort and set

\[
 X_{\mathcal C}(t)=\mathbb E\sum_{\gamma\in\mathcal C_0}I_\gamma(t),
 \qquad
 Y_{\mathcal C}(t)=\mathbb E\sum_{\gamma\in\mathcal C_0}
                                  I_\gamma(t)h_\gamma(t).   \tag{4.3}
\]

When \(X_{\mathcal C}(t)>0\), let \(\widehat\mu_{\mathcal C,t}\) be the
law obtained by sampling an alive carrier with its expected counting
multiplicity, and put

\[
 \mu_{\mathcal C}(t)=\mathbb E_{\widehat\mu}h_\gamma,
 \qquad
 \kappa_{\mathcal C}(t)=
 \mathbb E_{\widehat\mu}T_\gamma+
 \operatorname {Var}_{\widehat\mu}h_\gamma.                \tag{4.4}
\]

### Corollary 4.2 (exact continuous hazard contraction)

At every regular time before extinction,

\[
 \boxed{
 \frac d{dt}\log X_{\mathcal C}(t)=-\mu_{\mathcal C}(t),
 \qquad
 \frac d{dt}\mu_{\mathcal C}(t)=-\kappa_{\mathcal C}(t).} \tag{4.5}
\]

#### Proof

Equation (4.2) gives \(X'=-Y\) and

\[
 Y'=-X\,\mathbb E_{\widehat\mu}(h^2+T).                    \tag{4.6}
\]

Differentiate \(Y/X\).  The result is
\(-\mathbb E(h^2+T)+(\mathbb Eh)^2=-\mathbb ET-\operatorname {Var}h\).
\(\square\)

If cohorts are indexed by an ancestor degree \(d\), (4.5) says

\[
 \mu_e(t)-\mu_d(t)=\mu_e(0)-\mu_d(0)
 -\int_0^t\{\kappa_e(s)-\kappa_d(s)\}\,ds.                \tag{4.7}
\]

Thus the continuous clock removes the explicit predictable rate, but it
does not prove that the hazard ordering is preserved.  It turns the gate
exactly into the state-Palm regression of \(\kappa_d\).

There is also an exact common-contraction normalization in one deterministic
state.  Let

\[
 \bar C=\frac1Z\sum_{K\in E}C_K.                           \tag{4.8}
\]

The infinitesimal mean edge-count drift is \(Z'=-Z\bar C\).  For a carrier
family at that state, (4.5) gives \(\mu'=-\kappa\), and hence

\[
 \boxed{
 \left.\frac d{dt}\frac\mu Z\right|_{H}
 =-\frac{\kappa-\bar C\mu}{Z}.}                            \tag{4.9}
\]

With the notation of Appendix G.9,

\[
 \kappa-\bar C\mu
 =V+\mathbb E J_\gamma-
   \mathbb E[b_\gamma^TAb_\gamma],                        \tag{4.10}
\]

and \(0\le b_\gamma^TAb_\gamma\le W_\gamma\).  Thus (4.9)
removes the dominant common contraction and identifies the sharper local
profile \(V+\mathbb EJ-\mathbb E(b^TAb)\).  It is a deterministic-state
tangent, not permission to average ratios over a state mixture.

### Proposition 4.3 (the clock tradeoff)

Conditional on the embedded jump-chain path
\(H_0,H_1,\ldots\), the holding times are

\[
                   \Delta t_j=\frac{E_j}{Z(H_j)},
 \qquad E_j\stackrel{\rm iid}{\sim}\operatorname {Exp}(1). \tag{4.11}
\]

Consequently, for every predictable nonnegative \(g_j\),

\[
 \mathbb E\left[\sum_{j<J}g_j\Delta t_j
                    \mathrel{\Big|}H_0,H_1,\ldots\right]
 =\sum_{j<J}\frac{g_j}{Z(H_j)}.                            \tag{4.12}
\]

In particular, continuous time removes \(1/Z\) at a deterministic physical
time, whereas stopping after \(J\) selected rows restores it exactly in
conditional expectation.  At deterministic physical time, (1.3) has the
random clock \(N_t\) in place of \(j\).  No choice of these two standard
clocks simultaneously makes both the shore size and the row rate
deterministic.

## 5. Stopped jump and predictable quadratic-variation bounds

The sequential chain does give very strong control of martingale noise.
The distinction between noise and predictable drift is essential.

Fix a stopping time before which

\[
             Z_j\ge Z_*>D,\qquad \Delta_C(H_j)\le D.        \tag{5.1}
\]

Freeze the chain after the stop.  Let \(K_j\) be the row chosen at jump
\(j\), and define

\[
 \bar C_j=\frac1{Z_j}\sum_KC_K,\qquad
 V_{C,j}=\frac1{Z_j}\sum_K(C_K-\bar C_j)^2.                \tag{5.2}
\]

### Theorem 5.1 (edge count, one root, and one carrier)

The following are martingales for the embedded chain:

\[
 M^Z_J=Z_J-Z_0+\sum_{j<J}\bar C_j,                         \tag{5.3}
\]

and, for a vertex \(v\), with its degree set to zero after deletion,

\[
 M^v_J=d_J(v)-d_0(v)+\sum_{j<J}
 \frac1{Z_j}\sum_{F\ni v}C_F.                             \tag{5.4}
\]

For a fixed carrier history, put
\(I_j=\mathbf1_{\{\gamma\ {\rm alive}\}}\) and \(Y_j=I_jh_j\).  Then

\[
 M^I_J=I_J-I_0+\sum_{j<J}I_j\frac{h_j}{Z_j},               \tag{5.5}
\]

\[
 M^Y_J=Y_J-Y_0+\sum_{j<J}I_j\frac{h_j^2+T_j}{Z_j}          \tag{5.6}
\]

are martingales.  Their jumps and predictable quadratic variations obey

\[
 |\Delta M^Z_j|\le D,qquad
 \Delta\langle M^Z\rangle_j=V_{C,j}\le D^2,               \tag{5.7}
\]

\[
 |\Delta M^v_j|\le D,qquad
 \Delta\langle M^v\rangle_j
 \le\frac{d_j(v)^2D}{Z_j}\le\frac{D^3}{Z_j},              \tag{5.8}
\]

\[
 |\Delta M^I_j|\le1,qquad
 \Delta\langle M^I\rangle_j
 =I_j\frac{h_j}{Z_j}\left(1-\frac{h_j}{Z_j}\right),       \tag{5.9}
\]

and

\[
 |\Delta M^Y_j|\le mD,qquad
 \Delta\langle M^Y\rangle_j
 \le\frac{I_j}{Z_j}
 \left(h_j^3+\sum_{K\in D_{\gamma,j}}t_j(K)^2\right)
 \le\frac{I_j(m^3+m)D^3}{Z_j}.                            \tag{5.10}
\]

#### Proof

One jump gives \(Z_{j+1}-Z_j=-C_{K_j}\), proving (5.3) and (5.7).
Define

\[
 a_K(v)=|\{F\in E(H_j):v\in F,\ F\cap K\ne\varnothing\}|.\tag{5.11}
\]

Then \(d_{j+1}(v)-d_j(v)=-a_{K_j}(v)\), including the case
\(v\in K_j\), and double counting gives

\[
 \sum_Ka_K(v)=\sum_{F\ni v}C_F.                           \tag{5.12}
\]

Moreover \(a_K(v)\le d_j(v)\) and the right side of (5.12) is at most
\(d_j(v)D\).  Hence

\[
 \frac1{Z_j}\sum_Ka_K(v)^2
 \le\frac{d_j(v)^2D}{Z_j},                                \tag{5.13}
\]

which proves (5.4) and (5.8).  Equation (5.5) is the Bernoulli death
compensator from (2.1).  For \(Y\), the raw decrement is \(h_j\) for each
of the \(h_j\) killing rows and \(t_j(K)\) for a surviving row \(K\).
Its conditional mean and second moment are respectively

\[
 \frac{h_j^2+T_j}{Z_j},\qquad
 \frac{h_j^3+\sum_{K\in D_j}t_j(K)^2}{Z_j}.                \tag{5.14}
\]

Finally \(\sum_Kt_j(K)^2\le DT_j\le h_jD^2\) and
\(h_j\le mD\), proving (5.6), (5.9), and (5.10).  \(\square\)

The normalized carrier hazard has an even smaller bracket.  Put
\(S_j=I_jh_j/Z_j\), let \(\theta_j=\Delta_C(H_j)/Z_j\), and let
\(r_{s,j}\) be the signed remainder in (2.9b), with value zero after
carrier death.  Then

\[
 \mathbb E[\Delta S_j\mid\mathcal F_j]
 =I_j\{-S_j^2+r_{s,j}\}.                                  \tag{5.10a}
\]

The corresponding centered martingale has jump bound

\[
 b_m(\theta_j)=
 \max\left\{m\theta_j,\,
       \frac{(1+m\theta_j)\theta_j}{1-\theta_j}\right\},    \tag{5.10b}
\]

and bracket increment at most

\[
 \boxed{
 I_j\left[
 m^3\theta_j^3+
 \frac{2m\theta_j^3+2m^2\theta_j^4}{(1-\theta_j)^2}
 \right].}                                                \tag{5.10c}
\]

Indeed, carrier death has probability \(s_j\) and squared jump \(s_j^2\).
On survival, (2.9c) is the jump.  Using
\((x-y)^2\le2x^2+2y^2\),
\(\sum_{K\in D}t(K)^2\le DT\), \(T\le hD\), and
\(h/Z\le m\theta\) gives (5.10c).  This controls random fluctuation of a
fixed normalized carrier hazard.  It does not control covariance created
by adaptively sorting carrier histories according to their current root
degree.

The continuous-time martingales have the same formulas with sums replaced
by time integrals and the factors \(1/Z_j\) removed from their bracket
rates.  For example,

\[
 N_t-\int_0^tZ_s\,ds,\qquad
 Z_t-Z_0+\int_0^t\sum_KC_K\,ds                             \tag{5.15}
\]

are martingales with brackets

\[
 \int_0^tZ_s\,ds,qquad
 \int_0^t\sum_KC_K^2\,ds,                                 \tag{5.16}
\]

and the stopped brackets for \(d(v)\) and \(Y_\gamma\) are at most
\(D^3t\) and \((m^3+m)D^3t\), respectively.

For reference, the exponential-supermartingale proof of Freedman's
inequality gives, for any of the discrete martingales with jump bound \(b\),

\[
 \Pr\left(\max_{j\le J}|M_j|\ge a,
                 \langle M\rangle_J\le v\right)
 \le2\exp\left\{-\frac{a^2}{2(v+ba/3)}\right\}.           \tag{5.17}
\]

Thus cap-conditional martingale noise is quantitatively harmless.  The
centering terms \(\bar C_j\), \(\sum_{F\ni v}C_F/Z_j\), and
\((h_j^2+T_j)/Z_j\) are predictable, state-dependent drifts; (5.17) does
not compare them between histories.

## 6. Punctured scale

In the punctured process, every row contains \(2r\) targets on each of two
shores.  Write \(n\) for a representative current shore size and \(z\) for
its average degree.  Under the stopped degree cap and shore comparability,

\[
                    D=O(rz),\qquad Z=\frac{nz}{2r},qquad
                    \frac DZ=O\left(\frac{r^2}{n}\right).  \tag{6.1}
\]

Throughout the descent \(n\ge x_*n_0\), where \(x_*\) is polynomially
small and \(n_0=e^{\Omega(r)}\).  Therefore Corollary 2.3 gives, over at
most \(n_0/(2r)\) jumps,

\[
 \sum_j\varepsilon_{\mathcal C,j}
 =O_m\left(\frac{r^3}{x_*^2n_0}\right)=e^{-\Omega(r)}.      \tag{6.2}
\]

The same calculation gives

\[
 \sum_j\theta_j^2
 =O\left(\frac{r^3}{x_*^2n_0}\right)=e^{-\Omega(r)},\qquad
 \theta_j=\sup_H\frac{\Delta_C(H)}{Z(H)}.                  \tag{6.2a}
\]

Hence Theorem 2.3bis applies even after mixing all current states in one
predictable ancestor-degree cohort.  If

\[
 \widetilde q_{j-1}(d)=
 \mathbb E\left[\frac{h_{j-1}}{Z_{j-1}}
                  \mathrel{\Big|}d_{j-1}=d\right]           \tag{6.2b}
\]

under the parent carrier-Palm law, and \(q_j^{\leftarrow}(d)\) is the
corresponding mean child rate among surviving descendants, then uniformly

\[
 \boxed{
 q_j^{\leftarrow}(d)=\widetilde q_{j-1}(d)
                     +O_m(\theta_{j-1}^2).}                \tag{6.2c}
\]

Thus the future denominator, survivor state-reweighting, and arbitrary
variation of \(\kappa_d\) contribute only the exponentially summable error
(6.2a).  The remaining regression is the contemporaneous profile
\(d\mapsto\widetilde q_j(d)\).  The one-row clock preserves this profile;
it does not prove its sign.

Likewise, if the ratio \(z_{\max}/z_{\min}\) stays polynomially bounded,
(5.7) gives

\[
 \langle M^Z\rangle_J\le JD^2=O(n_0rz_{\max}^2).           \tag{6.3}
\]

Compared with \(Z_*^2\asymp n_*^2z_{\min}^2/r^2\), the ratio in (6.3) is
exponentially small.  Freedman therefore makes the edge-count martingale
noise exponentially small relative to \(Z_*\).

This statement is deliberately centered at the random predictable sum

\[
                         Z_0-\sum_{i<j}\bar C_i.            \tag{6.4}
\]

It does not say that (6.4) is close to a deterministic reference center.
Cap control alone cannot say this.  For example, take \(3s\) disjoint graph
edges, and compare them with \(s\) disjoint triangles plus \(3s\) isolated
vertices.  The two graphs have the same number of vertices, the same
number \(Z=3s\) of edges, the same average degree, and both satisfy
\(\Delta_C\le3\).  Nevertheless every row has \(C_K=1\) in the first graph
and \(C_K=3\) in the second.  Their predictable edge-count drifts differ by
a factor of three while their martingale variances are zero.

The punctured catalogue has much more structure than these graphs, but a
punctured-specific theorem is needed to exploit it.  A cap-conditional
quadratic-variation estimate is not such a theorem.

## 7. The state-Palm and literal high-tail obstructions

Let \(\rho\) be the state marginal of a carrier-Palm law and let
\(\widehat\nu_H\) be its conditional carrier law in state (H).  For any
carrier statistic \(S\) and ancestor test \(\Phi\), total covariance gives

\[
\begin{aligned}
 \operatorname {Cov}_{\widehat\nu}(S,\Phi)
 ={}&\mathbb E_\rho
       \operatorname {Cov}_{\widehat\nu_H}(S,\Phi)\\
 &+\operatorname {Cov}_\rho
       \left(\mathbb E_{\widehat\nu_H}S,
             \mathbb E_{\widehat\nu_H}\Phi\right).
                                                               \tag{7.1}
\end{aligned}
\]

For the embedded chain \(S=h/Z\); for the continuous clock \(S=h\).
The first term is the deterministic-state row term.  The second is the
stopped Simpson term.  Equivariance and a theorem proved separately in
every state do not determine its sign.

The same point appears in (4.4).  Conditional on an ancestor bucket \(d\),

\[
\begin{aligned}
 \operatorname {Var}(h\mid d)
 ={}&\mathbb E[\operatorname {Var}(h\mid H,d)\mid d]\\
 &+\operatorname {Var}(\mathbb E[h\mid H,d]\mid d).        \tag{7.2}
\end{aligned}
\]

The second, between-state term is part of the exact decrement
\(\kappa_d^{\rm Palm}\).  Dropping it repeats the variance error already
exhibited in Appendix G.9, now at the state-mixture level.

There is also a deterministic literal obstruction to generic high-tail
contraction.  Let

\[
                         H=K_{14}\mathbin{\dot\cup}M K_{12,12},
 \qquad M\ge1,                                             \tag{7.3}
\]

regarded as a \(2\)-uniform hypergraph, and take ordered \(12\)-carriers at
all roots.  Put

\[
 T_H=14(13)_{12},\qquad T_L=24(12)_{12}.                    \tag{7.4}
\]

For \(\varphi_{12}(d)=(d-12)_+^{12}/(d)_{12}\), the initial carrier-Palm
scalar is

\[
                         A_{12}=\frac{14}{T_H+MT_L}.         \tag{7.5}
\]

Choose one row uniformly.  There are \(91\) high-component rows and \(144\)
rows in each low component.  A high carrier is killed by every row in its
own \(K_{14}\) and has hazard \(91\); a low carrier is killed by every row
in its own \(K_{12,12}\) and has hazard \(144\).  A surviving carrier is
unchanged, so erosion is zero.  Direct counting gives

\[
 A_{12}^+=
 \frac{14M(144)}
 {M(144)\{T_H+(M-1)T_L\}+91MT_L}.                          \tag{7.6}
\]

Cross-multiplication yields

\[
                         \boxed{A_{12}^+>A_{12}}             \tag{7.7}
\]

because \(144>91\).  The same strict increase is the time-zero derivative
under the rate-one continuous clock.  This is not asserted to be a
punctured residual.  It proves that uniform-row selection, cap bounds, and
favourable erosion do not generically imply the required scalar descent.

## 8. Exact revised Gate-A obligation

The sequential clock proves the following reductions.

1. The parallel-bite quadratic survival error is absent.
2. Fixed jump number gives deterministic shore sizes and an exact nested
   uniform-slice reference.
3. The child-denominator correction in (2.8) accumulates to
   \(e^{-\Omega(r)}\) under the punctured cap.
4. Edge-count, root-degree, carrier-survival, and carrier-hazard martingale
   noises have the stopped brackets (5.7)--(5.10).
5. The dominant deterministic-state hazard contraction is removed by the
   normalized residual profile (4.9)--(4.10).

It leaves the following theorem genuinely open.  Under the stopped
punctured carrier-Palm history law, uniformly over every relevant terminal
threshold and ancestor degree pair, prove a summable downward-inversion
bound for

\[
 \boxed{
 q_j^{\leftarrow}(d)
 =\mathbb E\left[\frac{h_j}{Z_j}
                  \mathrel{\Big|}d_{j-1}=d\right]}          \tag{8.1}
\]

in embedded time.  By (6.2c), this is equivalent up to
\(e^{-\Omega(r)}\) to the contemporaneous stopped state-Palm regression

\[
 \boxed{
 \widetilde q_j(d)=
 \mathbb E\left[\frac{h_j}{Z_j}\mathrel{\Big|}d_j=d\right].} \tag{8.1a}
\]

An alternative physical-time proof would have to control the integrated
contemporaneous hazard regression; equation (4.7) expresses its evolution
through \(\kappa_d^{\rm Palm}\), with the between-state variance retained.
A deterministic-state route may instead control the residual

\[
 V_d+\mathbb E J_\gamma-
       \mathbb E(b_\gamma^TAb_\gamma)                      \tag{8.2}
\]

together with the Simpson covariance (7.1) and the deterministic-center
transfer.

Even after (8.1), the coefficient-one argument still needs the
actual/reference erosion-payoff comparison and the realized center/purge
ledger, as well as a sequential-law version of every moment and degree-floor
estimate used to reach the base stop.  Accordingly, the one-row process is
a real simplification and a useful replacement candidate, but it reduces
rather than closes Gate A.
