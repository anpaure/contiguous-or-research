Verdict: lane Y remains open. I did not prove that some communicating class has mean \(O_A(H_A\operatorname{Cat}_m)\), and no unconditional high-energy class invariant was found. The stationary problem does, however, reduce exactly to a class-covariance selection theorem; reversibility, entropy, parity floors, and harmonic smoothing do not control that covariance.

## 1. Exact stationary structure

Let \(\mathfrak F_m\) be the finite set of exact factors and

\[
K=\binom n2^{-1}\sum_\tau K_\tau
\]

the fair component heat kernel.

For every transposition \(\tau\):

- The overlay of \(F\) and \(\tau F\) has components with sides \(L_i,\tau L_i\).
- For \(m\ge2\), \(F\cap\tau F=\varnothing\). Indeed, \(C\) and \(\tau C\) share a \(\tau\)-fixed middle interval, while no transposition stabilizes an unoriented odd cyclic order.
- Thus a \(k\)-component overlay gives exactly \(2^k\) distinct exact factors.
- These factors form an intrinsic \(\tau\)-cell, and \(K_\tau\) uniformly averages over that cell.

Consequently,

\[
K_\tau^2=K_\tau,\qquad K_\tau^*=K_\tau.
\]

Every communicating class \(\mathscr C\) is a union of complete \(\tau\)-cells for every \(\tau\). Its unique stationary law \(\pi_{\mathscr C}\) is uniform and satisfies

\[
\pi_{\mathscr C}K_\tau=\pi_{\mathscr C}
\quad\text{for every fixed }\tau.
\]

Moreover, every class is \(S_n\)-stable because choosing every opposite component side gives \(\tau F\). The full invariant algebra is exactly

\[
\boxed{\ker(I-K)=\bigcap_\tau\operatorname{Ran}K_\tau.}
\]

This characterizes class invariants, but no more explicit nonlinear description of the intersection is currently proved.

## 2. Stationary energy is near-minimal integer variance

Write

\[
\lambda_q=\frac W{N_q}=c_q+\theta_q,\qquad 0\le\theta_q<1.
\]

For a fixed rank-\((m-q)\) target \(S\), set \(Z_q=\mu_q(F,S)\). Class transitivity gives

\[
\mathbb E_{\pi_{\mathscr C}}Z_q=\lambda_q.
\]

Therefore, exactly,

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}Q_q
=
N_q\left(\operatorname{Var}_{\pi_{\mathscr C}}Z_q
-\theta_q(1-\theta_q)\right).
}
\]

Hence the requested theorem is precisely a classwise near-minimal integer-variance theorem:

\[
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A
=
\sum_{q\le H_A}\frac{N_q}{c_q}
\left(\operatorname{Var}Z_q-\theta_q(1-\theta_q)\right).
\]

Stationarity determines the mean of \(Z_q\), but not this excess variance.

## 3. Exact covariance reduction

Let

\[
B=\operatorname{Cat}_m=\frac Wn,\qquad
M=\frac{(n-1)!}{2},
\]

and let \(x_F\in\{0,1\}^M\) be the wreath-indicator vector. Put

\[
p=\frac BM,\qquad y_F=x_F-p\mathbf1,\qquad
\Sigma_{\mathscr C}=\mathbb E_{\pi_{\mathscr C}}y_Fy_F^{\mathsf T}.
\]

Then

\[
\operatorname{Tr}\Sigma_{\mathscr C}=B(1-p),
\qquad
A_m\Sigma_{\mathscr C}=0.
\]

For a fixed \(\tau\), let \(P_\tau=(I+\tau)/2\) and let

\[
z_K=\mathbf1_{\tau K}-\mathbf1_K
\]

be the indicator effect of component \(K\). Stationarity under \(K_\tau\) gives

\[
\boxed{
\Sigma_{\mathscr C}
=P_\tau\Sigma_{\mathscr C}P_\tau
+\mathbb E_{\pi_{\mathscr C}}\frac14\sum_Kz_Kz_K^{\mathsf T}.
}
\]

Since \(\Sigma_{\mathscr C}\) is \(S_n\)-equivariant,

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\frac14\sum_Kz_Kz_K^{\mathsf T}
=(I-P_\tau)\Sigma_{\mathscr C}.
}
\]

Pointwise,

\[
\boxed{
\operatorname{Tr}\left(\frac14\sum_Kz_Kz_K^{\mathsf T}\right)
=\frac B2,
}
\]

because \(\|z_K\|^2=2|K|\) and \(\sum_K|K|=B\). Thus the total indicator-noise trace is independent of the number of components. Conditional cube entropy records \(k\log2\), while covariance trace remains \(B/2\); entropy cannot control the needed lower-shadow alignment.

If \(f_{q,j}\) is the degree-\(j\) Johnson component, then for every fixed transposition,

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}
\frac14\sum_K\|\Delta_{K,q,j}\|_2^2
=
\kappa_j\,
\mathbb E_{\pi_{\mathscr C}}\|f_{q,j}\|_2^2,
\quad
\kappa_j=\frac{j(n-j+1)}{n(n-1)}.
}
\]

This is an equality: component noise simply tracks whatever harmonic energy the class already has.

Define

\[
T_A=\sum_{q\le H_A}\frac{A_{m-q}^{\mathsf T}A_{m-q}}{c_q},
\qquad
\beta_A=\sum_{q\le H_A}\frac{\beta_q}{c_q}.
\]

Then

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A
=\operatorname{Tr}(T_A\Sigma_{\mathscr C})-\beta_A.
}
\]

Thus the exact remaining statement is:

> **UNPROVED \(SCOV_A\).** For every fixed \(A\), some communicating class \(\mathscr C_m\) satisfies
> \[
> \operatorname{Tr}(T_A\Sigma_{\mathscr C_m})-\beta_A
> =O_A(H_A\operatorname{Cat}_m).
> \]

## 4. Exact cell-floor decomposition

Fix \(q,\tau\), and write

\[
h_q(z)=(z-c_q)(z-c_q-1).
\]

For a moved pair \(p=\{S,\tau S\}\), put

\[
\ell_p=\mu_q(S)+\mu_q(\tau S),
\]

and

\[
H_q(\ell)=h_q(\lfloor\ell/2\rfloor)+h_q(\lceil\ell/2\rceil).
\]

If \(d_{K,p}=a_K(S)-a_K(\tau S)\), define

\[
J_{q,\tau}
=
\sum_{\tau S=S}h_q(\mu_q(S))
+\sum_pH_q(\ell_p),
\]

\[
C_{q,\tau}
=
\frac12\sum_p
\left(\sum_Kd_{K,p}^2-(\ell_p\bmod2)\right).
\]

Both are nonnegative and constant on the entire \(\tau\)-cell. Moreover,

\[
Q_q=J_{q,\tau}+G_{q,\tau},
\]

where

\[
G_{q,\tau}
=
\frac12\sum_p
\left((\mu_q(S)-\mu_q(\tau S))^2-(\ell_p\bmod2)\right),
\]

and fair cell averaging gives

\[
\boxed{K_\tau Q_q=J_{q,\tau}+C_{q,\tau}.}
\]

Therefore every stationary class obeys, for every fixed \(\tau\),

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}Q_q
=
\mathbb E_{\pi_{\mathscr C}}J_{q,\tau}
+
\mathbb E_{\pi_{\mathscr C}}C_{q,\tau},
\qquad
\mathbb E G_{q,\tau}=\mathbb E C_{q,\tau}.
}
\]

This is the exact stationary obstruction: pair-sum floors and component bundling are two nonnegative, uncontrolled class parameters. The gain-versus-noise equality supplies no upper bound.

## 5. Variational characterization

Let

\[
\Theta_A=\min_{\mathscr C}
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A.
\]

Finite-state duality gives

\[
\boxed{
\Theta_A
=
\inf_{\pi K=\pi}\mathbb E_\pi\mathcal Q_A
=
\sup_h\min_{F\in\mathfrak F_m}
\left[\mathcal Q_A(F)+(I-K)h(F)\right].
}
\]

For equality, solve on each class

\[
(I-K)h
=
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A-\mathcal Q_A.
\]

Thus \(\Theta_A=O_A(H_A\operatorname{Cat}_m)\) is equivalent to requiring that for every potential \(h\), some exact factor satisfy the corresponding bound. This is strictly stronger than merely finding one good factor or proving the positive-cut/local-minimum lemma: a good factor may belong to a class with much larger uniform mean.

## 6. Invariant audit

No unconditional obstruction survived.

- The signed-lattice saturation theorem implies that every additive or modular invariant annihilating all signed middle-preserving shadow trades factors only through point margins. Those margins equal \(r\operatorname{Cat}_m\mathbf1\) for every exact factor.
- This does not rule out nonlinear, support-feasible heat-class invariants.
- Cyclic-order parity is not a heat invariant. For \(m=4\), the archived \(Q_9\) factor has a genuine size-three component under \(\tau=(3\,9)\), built from
  \[
  \begin{aligned}
  &(1,2,4,7,6,9,3,8,5),\\
  &(1,3,7,9,2,6,5,8,4),\\
  &(1,4,7,6,3,2,5,8,9).
  \end{aligned}
  \]
  Their 27 middle intervals form a \(\tau\)-invariant set. The three old orders are even, their \(\tau\)-images odd, and the closed \(3\)-by-\(3\) overlay has no singleton component; hence it is connected. Switching it flips factor parity. The full literal certificate is in [SELECTOR_COMPOSITE_PACKING_AUDIT_20260724.md](/Users/amir.nuriyev/Documents/problem/SELECTOR_COMPOSITE_PACKING_AUDIT_20260724.md).

A hypothetical load-congruence invariant would be decisive. If all values \(Z_q\) in one class belonged to a coset \(a+d\mathbb Z\), with consecutive allowed values \(u<v\) surrounding \(\lambda_q\), then

\[
\operatorname{Var}Z_q\ge(\lambda_q-u)(v-\lambda_q).
\]

For parity, the excess above the usual integer floor is \(N_q\theta_q\) or \(N_q(1-\theta_q)\). Away from an integer threshold this is \(\Omega_A(W)\), far above

\[
H_A\operatorname{Cat}_m=O_A(W/\sqrt m).
\]

No such class congruence was found.

## 7. Conditional rigid-orbit obstruction

If an exact factor \(F\) has connected overlay with \(\tau F\) for every transposition, then its coordinate orbit \(S_nF\) is exactly one communicating class. Every heat step is merely a complete coordinate relabeling, so

\[
\boxed{
\mathbb E_{\pi_{S_nF}}\mathcal Q_A=\mathcal Q_A(F).
}
\]

Thus a high-energy transposition-rigid family would give a genuine high-energy stationary class and refute every-class Lyapunov contraction. Its existence is **UNPROVED**, and even such a family would not disprove the weaker assertion that some other class has low mean.

So the stationary lane ends at \(SCOV_A\): a new exact-factor pair-correlation or covariance-selection theorem is necessary. The first-wave synthesis and corrected implication scopes are consistent with this conclusion: [MATH_ATTACK_FIRST_WAVE_SYNTHESIS_20260724.md](/Users/amir.nuriyev/Documents/problem/MATH_ATTACK_FIRST_WAVE_SYNTHESIS_20260724.md).
