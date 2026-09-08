The multitransposition route does not prove \(FEN_A\). It does produce a sharper exact theorem: the previously defined “excess noise” combines three different effects. After separating them, the genuine component noise is exactly a propagated integer-wall crossing count. The remaining bound is an exact-factor fragmentation theorem, not a harmonic estimate.

Let

\[
\beta_q=\frac{r_q(N_q-r_q)}{N_q},\qquad
\|x\|_A^2=\sum_{q\le H_A}\frac{\|x_q\|_2^2}{c_q},
\]

and

\[
\Psi_A(F)=\frac12\left(\|f(F)\|_A^2-
\sum_{q\le H_A}\frac{\beta_q}{c_q}\right).
\]

Here \(\Psi_A=\sum_q\Phi_q/c_q\), so \(O_q\le\Phi_q\).

## 1. A fixed \(O(n)\) coherent-contraction word is proved

At rank \(r=m-q\), every wreath contributes exactly \(r\) intervals through each point. Consequently

\[
U_r f_q=0,
\qquad
f_q\in\bigoplus_{j\ge2}E_j.
\]

For \(P_\tau=(I+\tau)/2\) and \(v_j\in E_j\),

\[
\mathbb E_\tau\|P_\tau v_j\|^2
=
\left(1-\frac{j(n-j+1)}{n(n-1)}\right)\|v_j\|^2
\le\left(1-\frac2n\right)\|v_j\|^2.
\]

Greedily choosing a transposition at every step therefore gives a deterministic word, depending only on \(F\) and fixed before any component signs, such that

\[
T_0=\lceil n\log2\rceil,
\qquad
\boxed{\|Mf\|_A^2\le\frac14\|f\|_A^2.}
\]

The exact sufficient length is

\[
\left\lceil
\frac{\log4}{-\log(1-2/n)}
\right\rceil .
\]

A universal word independent of \(F\) can also be obtained from a fixed 10-regular expander: 1000 complete edge sweeps give a \(5000n\)-term word with the same quarter contraction. That construction uses the standard symmetric-exclusion spectral-gap theorem as an imported input.

## 2. Exact multistep martingale ledger

For the frozen word \(\tau_1,\ldots,\tau_T\), put

\[
P_t=\frac{I+\tau_t}{2},\qquad
M=P_T\cdots P_1,\qquad
Q_t=P_T\cdots P_{t+1}.
\]

At stage \(t\),

\[
f_t=P_tf_{t-1}+\xi_t,\qquad
\xi_t=\frac12\sum_K\varepsilon_{t,K}\delta_{t,K}.
\]

Every leaf remains one genuine integral exact factor. Since the signs are martingale differences,

\[
f_T=Mf+\sum_tQ_t\xi_t
\]

and, defining

\[
\mathcal N_T
=
\sum_t\mathbb E\sum_K\|Q_t\delta_{t,K}\|_A^2,
\]

one has exactly

\[
\boxed{
\mathbb E\|f_T-Mf\|_A^2=\frac{\mathcal N_T}{4}.
}
\]

Thus, with

\[
d=\frac12\left(\|Mf\|_A^2-
\sum_q\frac{\beta_q}{c_q}\right),
\]

\[
\mathbb E\Psi_A(F_T)=d+\frac{\mathcal N_T}{8}.
\]

For a fixed word one may decompose \(Q_t\delta\) harmonically, but one may not replace its \(E_j\)-norm by \(\alpha_j^{T-t}\|\delta^{(j)}\|^2\). That replacement is valid only after averaging an independent random future suffix.

## 3. Exact restitution hierarchy

For each rank define

\[
d_q=\frac{\|M f_q\|^2-\beta_q}{2c_q},
\qquad
D^+=\sum_q(d_q)_+.
\]

Let the terminal mean load be

\[
u_q=\lambda_q\mathbf1+Mf_q,
\qquad \lambda_q=W/N_q,
\]

and put

\[
\Theta(u)
=
\sum_{q,S}\frac{\{u_q(S)\}(1-\{u_q(S)\})}{c_q}.
\]

There are three exact decompositions:

\[
\boxed{
\mathbb E\Psi_A(F_T)
=d_++\frac{\mathcal R^{\rm agg}_T}{8}
=D^++\frac{\mathcal R^{\rm rk}_T}{8}
=h(u)+\frac{\mathcal R^{\rm coord}_T}{8},
}
\]

where

\[
\mathcal R^{\rm agg}_T
=\mathcal N_T-8(-d)_+,
\]

\[
\mathcal R^{\rm rk}_T
=\mathcal N_T-8\sum_q(-d_q)_+,
\]

\[
\mathcal R^{\rm coord}_T
=\mathcal N_T-4\Theta(u),
\]

and

\[
h(u)=
\frac12\sum_q
\frac{\|Mf_q\|^2+
\sum_S\{u_q(S)\}(1-\{u_q(S)\})-\beta_q}{c_q}.
\]

All three remainders are nonnegative and

\[
\mathcal R^{\rm agg}_T
\ge\mathcal R^{\rm rk}_T
\ge\mathcal R^{\rm coord}_T.
\]

More precisely,

\[
\mathcal R^{\rm agg}_T-\mathcal R^{\rm rk}_T
=
8\left[
\sum_q(-d_q)_+
-\left(-\sum_qd_q\right)_+
\right],
\]

and

\[
\mathcal R^{\rm rk}_T-\mathcal R^{\rm coord}_T
=
8(h-D^+).
\]

Hence the published \(\mathcal R_T\) is not purely excess component noise: it also contains cross-rank cancellation and unused coordinate-floor restitution.

The coordinate formula follows from the exact scalar identity

\[
\operatorname{Var}(Z)
=
\{u\}(1-\{u\})
+
\mathbb E[(Z-\lfloor u\rfloor)(Z-\lfloor u\rfloor-1)]
\]

for integer \(Z\) with mean \(u\). Thus \(\mathcal R^{\rm coord}_T\) is precisely the variance beyond the optimal two-adjacent-integer rounding.

A crucial scale correction is that

\[
\sum_{q\le H_A}\frac{N_q}{c_q}
=\Theta_A(H_AW)
=\Theta_A(nH_A\operatorname{Cat}_m).
\]

Therefore coordinate restitution cannot be absorbed into the allowed \(H_A\operatorname{Cat}_m\) error; that would lose a factor \(n\).

## 4. The exact harmful-noise formula

Reveal the component signs one at a time. Immediately before revealing \(\varepsilon_{t,K}\), let \(b\) be the conditional terminal mean of one load coordinate. The two children are

\[
b\pm u,\qquad
u=\frac12(Q_t\delta_{t,K})_{q,S}.
\]

For

\[
\phi(x)=x^2+\{x\}(1-\{x\}),
\]

whose derivative jumps by \(2\) at every integer,

\[
\boxed{
\frac{\phi(b+u)+\phi(b-u)}2-\phi(b)
=
\sum_{\ell\in\mathbb Z}
(|u|-|b-\ell|)_+.
}
\]

Telescoping these conditional Jensen gaps gives

\[
\boxed{
\frac{\mathcal R^{\rm coord}_T}{4}
=
\mathbb E
\sum_{t,K,q,S}\frac1{c_q}
\sum_{\ell\in\mathbb Z}
\left(
\frac{|(Q_t\delta_{t,K})_{q,S}|}{2}
-|b_{t,K,q,S}-\ell|
\right)_+.
}
\]

This is the exact answer to “bound only harmful excess component noise”: only suffix-filtered component intervals that cross an integer load wall contribute.

For one transposition this specializes to the audited parity decomposition. If

\[
d_K=a_K(S)-a_K(\tau S)
\]

on a moved pair and \(C_p\) is its component excess, then

\[
\boxed{
2C_p
=
\sum_Kd_K^2-\mathbf1_{\sum_Kd_K\text{ odd}}
=
\sum_K\bigl(d_K^2-\mathbf1_{d_K\text{ odd}}\bigr)
+2\left\lfloor\frac{\#\{K:d_K\text{ odd}\}}2\right\rfloor.
}
\]

Thus one odd unit is forced restitution; harmful noise is magnitude excess plus collisions between multiple odd restitution units.

## 5. Strictly weaker corrected target

For an iid-uniform word,

\[
\mathbb E_w D^+(w)
\le
\left(1-\frac2n\right)^T\Psi_A(F).
\]

Indeed, if \(X_q=\|f_q\|^2\) and \(Y_q=\|M_wf_q\|^2\), then \(0\le Y_q\le X_q\) and

\[
(Y_q-\beta_q)_+
\le
\frac{X_q-\beta_q}{X_q}Y_q.
\]

Consequently \(T_0=\lceil n\log2\rceil\) gives

\[
\mathbb E_wD^+(w)\le\frac14\Psi_A(F).
\]

The original FEN can therefore be weakened to the following joint or annealed rankwise theorem:

\[
\boxed{
\mathbb E_w\mathcal R^{\rm rk}_{T_0}(F,w)
\le
4\Psi_A(F)+C_AH_A\operatorname{Cat}_m.
}
\tag{\(\mathrm{RFEN}_A\), UNPROVED}
\]

It would imply

\[
\mathbb E_{w,\varepsilon}\Psi_A(F_T)
\le
\frac34\Psi_A(F)
+\frac{C_A}{8}H_A\operatorname{Cat}_m.
\]

Equivalently, writing \(J_{\rm wall}=\mathcal R^{\rm coord}_T/4\), the same-word structural requirement is

\[
\boxed{
J_{\rm wall}+2(h-D^+)
\le
\Psi_A(F)+\frac{C_A}{4}H_A\operatorname{Cat}_m.
}
\tag{UNPROVED}
\]

This is the cleanest surviving lane-M theorem: a propagated lattice-wall crossing bound plus control of the coordinate-floor residue.

## 6. Legal endpoint and iteration, conditional on RFEN

Some integral leaf satisfies

\[
\Psi_A(F')
\le
\frac34\Psi_A(F)
+\frac{C_A}{8}H_A\operatorname{Cat}_m.
\]

Iterating selected leaves gives

\[
\Psi_A(F_k)
\le
\left(\frac34\right)^k\Psi_A(F_0)
+\frac{C_A}{2}H_A\operatorname{Cat}_m.
\]

Since

\[
\mu_q(S)\le\operatorname{Cat}_m,\qquad
\Psi_A(F_0)\le\frac{H_AW^2}{2n},
\]

at most

\[
\left\lceil\log_{4/3}(W/2)\right\rceil=O(n)
\]

macrosteps, hence \(O(n^2)\) legal transposition steps, reach

\[
\Psi_A=O_A(H_A\operatorname{Cat}_m)=O_A(W/\sqrt m)=o(W).
\]

This proves fixed-window overload, hence MWB by diagonalization.

Alternatively, at a global minimizer one application suffices:

\[
\Psi_{\min}
\le
\frac34\Psi_{\min}
+\frac{C_A}{8}H_A\operatorname{Cat}_m
\quad\Longrightarrow\quad
\Psi_{\min}\le\frac{C_A}{2}H_A\operatorname{Cat}_m.
\]

Thus FEN at only one global minimizer already contains the desired conclusion. An all-factor FEN would force the same Catalan-scale minimum in every heat communicating class and is substantially stronger than MWB.

## 7. Exhaustion and obstruction audit

The remaining inequality cannot follow from harmonic smoothing alone:

- A transposition-rigid exact factor—one whose overlay is connected for every transposition—would have every heat leaf equal to a coordinate relabeling. Then \(\Psi_A\) is constant and a quarter-contracting word satisfies

  \[
  \mathcal R^{\rm agg}_T
  =8(\Psi_A-d_+)\ge6\Psi_A.
  \]

  Hence coefficient-4 FEN fails above \(C_AH_A\operatorname{Cat}_m/2\). No genuine high-energy rigid factor is known, so this is conditional, not a counterexample.

- Point-regular higher-harmonic integer profiles exist for which every one-step parity-corrected ideal gain vanishes. These are histogram relaxations, not exact-factor histograms.

- Repeating a transposition only shifts noise to its last occurrence. A palindrome does not annihilate noise after intervening noncommuting projections. Expander sweeps filter early noise but leave the last sweep undiscounted.

- Signed octahedral lifts furnish countermodels to spectral/lattice-only proofs, but not genuine nonnegative exact factors.

Therefore the route is genuinely exhausted at:

\[
\boxed{
\text{an exact-factor fragmentation/anti-cancellation theorem controlling}
\atop
\text{the terminal lattice-wall crossings and coordinate-floor residue.}
}
\]

That decisive statement remains unproved. No web or finite search was used, and no workspace files were edited.
