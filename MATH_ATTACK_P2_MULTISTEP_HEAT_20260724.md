# Second-wave lane P: exact multistep heat, restitution, and commutator barriers

## 0. Outcome

This report proves an exact multistep theorem for sequential component heat inside genuine exact middle wreath factors.  The theorem has two telescopes and four energy ledgers.  In the notation introduced below,

\[
 \boxed{
 \mathbb E\Phi_H(F_T)-\Phi_H(F_0)
 =\frac{\mathcal N_w-\mathcal D_w}{4}
 =\frac{\mathcal R_w-\mathcal A_w}{4},
 }
 \tag{0.1}
\]

and

\[
 \boxed{
 \mathcal R_w-\mathcal N_w
 =\mathcal A_w-\mathcal D_w
 =\mathcal F_w\ge 0.
 }
 \tag{0.2}
\]

Here

* \(\mathcal R_w\) is the raw component-effect energy injected over all steps;
* \(\mathcal N_w\) is the part of that energy surviving all later heat projections;
* \(\mathcal A_w\) is the sum of coherent transposition displacements evaluated at the random exact factors actually visited;
* \(\mathcal D_w\) is the deterministic coherent displacement along the product of midpoint projections; and
* \(\mathcal F_w\) is an explicit nonnegative suffix-filtering Dirichlet sum.

Thus fair component noises from different times do **not** cancel one another in expected terminal squared norm.  Earlier noise can nevertheless disappear: later midpoint projections can filter or annihilate it.  Formula (0.2) accounts for that disappearance exactly.  It is dissipation by a suffix, not a negative covariance between different component noises.

At a global minimizer of the same fixed-window integral floor energy, every terminal leaf is another exact factor and therefore

\[
 \boxed{\mathcal N_w\ge \mathcal D_w}
 \tag{0.3}
\]

for every transposition word frozen before the component signs.  For a one-letter word, summing (0.3) over unordered transpositions and using the exact-factor zero-point-margin property gives the corrected sharp spectral floor

\[
 \boxed{
 R_H\ge 4(n-1)\bigl(B_H+\Phi_H(F_*)\bigr).
 }
 \tag{0.4}
\]

The coefficient \(4(n-1)\) is an all-unordered-transpositions **sum**, not a per-step lower bound for a single word.  For a uniform transposition it becomes the average coefficient \(8/n\).  Under a length-\(T\) iid word, the spectral loss telescopes and saturates at at most \(4\|f\|_H^2\); the \(4(n-1)\) floor does not accumulate independently at every time.

Products, palindromes, relators, and commutator words do not reverse midpoint smoothing.  Every heat product is a positive average of all group subwords.  A palindrome has operator \(A^*A\), not \(A^{-1}A\).  Formal signed commutators such as \([P_\tau,P_\sigma]\) can rotate leakage, but they are not legal heat trajectories.  A disconnected transposition graph also preserves exact orbit masses and cannot repair a residual profile that violates one of those orbit constraints.

These are rigorous restitution and capacity barriers.  They do not prove the missing upper bound on propagated exact-factor component noise, and hence do not prove MWB or the contiguous-OR width conjecture.

No finite or computational search is used in this report.

## 1. Fixed-window Hilbert space and integral floor

Let \(n=2m+1\).  Fix an integer depth window \(0\le H\le m\) and positive weights \(c_q\), \(0\le q\le H\).  The application has \(H=\lceil A\sqrt m\rceil\) for fixed \(A\), but the identities below are finite, exact, and valid for every such \(H\).

At depth \(q\), let \(\mu_q(F)\) be the exact-factor target-load histogram on the relevant rank, let \(N_q\) be the number of targets on that rank, and put

\[
 f_q(F)=\mu_q(F)-\frac{W}{N_q}\mathbf 1.
\]

Use the weighted direct-sum inner product

\[
 \langle x,y\rangle_H
 =\sum_{q=0}^H\frac{1}{c_q}\sum_S x_q(S)y_q(S),
 \qquad
 \|x\|_H^2=\langle x,x\rangle_H.
 \tag{1.1}
\]

Write

\[
 W=b_qN_q+a_q,
 \qquad 0\le a_q<N_q.
\]

Among all integral vectors of total mass \(W\), the least possible squared distance from the constant vector is

\[
 \beta_q=\frac{a_q(N_q-a_q)}{N_q}.
 \tag{1.2}
\]

Indeed, a convex exchange reduces the squared norm whenever two coordinates differ by at least two, so a minimizer has \(N_q-a_q\) entries \(b_q\) and \(a_q\) entries \(b_q+1\); direct substitution gives (1.2).  Define

\[
 B_H=\sum_{q=0}^H\frac{\beta_q}{c_q},
 \qquad
 \Phi_H(F)=\|f(F)\|_H^2-B_H,
 \qquad
 \Psi_H(F)=\frac12\Phi_H(F).
 \tag{1.3}
\]

Every exact factor is integral, so \(\Phi_H(F)\ge0\).

Every coordinate transposition \(\tau\) acts orthogonally on (1.1).  Set

\[
 P_\tau=\frac{I+\tau}{2}.
 \tag{1.4}
\]

Since \(\tau\) is an orthogonal involution, \(P_\tau\) is the orthogonal projection onto the \(\tau\)-fixed subspace.  In particular,

\[
 \|x\|_H^2-\|P_\tau x\|_H^2
 =\|(I-P_\tau)x\|_H^2
 =\frac14\|x-\tau x\|_H^2.
 \tag{1.5}
\]

The vectors produced by applying \(P_\tau\) need not be integral and are not asserted to be factors.  They are coherent means used only in the analysis.  Every random leaf used below remains one genuine integral exact factor.

## 2. Exact-factor component heat input

Fix a word

\[
 w=(\tau_1,\ldots,\tau_T)
 \tag{2.1}
\]

before exposing any component signs.  The word may be deterministic, or it may first be sampled and then conditioned upon.  At time \(t\), recompute the exact ownership components for the current factor against \(\tau_t\).  The component family and its effects may depend on the complete preceding heat history, but they must be measurable before the time-\(t\) signs are sampled.

The audited exact component-switching theorem gives

\[
 f_t=P_tf_{t-1}+\xi_t,
 \qquad
 P_t=P_{\tau_t},
 \qquad
 \xi_t=\frac12\sum_{K}\varepsilon_{t,K}\delta_{t,K},
 \tag{2.2}
\]

where, conditionally on the past, the \(\varepsilon_{t,K}\) are independent fair Rademacher signs.  A complete sign choice selects one side in each current ownership component and produces an integral exact factor.  The same component sign is used simultaneously at all depths; \(\delta_{t,K}\) in (2.2) is the full direct-sum multidepth effect.

For the canonical transposition overlay, component equivariance gives

\[
 \tau_t\delta_{t,K}=-\delta_{t,K}.
 \tag{2.3}
\]

Each component effect also has zero total and zero point margins on every rank.  Thus its Johnson decomposition, like that of an exact-factor centered histogram, begins in degree \(2\).  The main martingale theorem below needs neither (2.3) nor the zero-margin assertion; those properties are used later for filtering and the sharp spectral constants.

The exact-factor component-switching theorem is an imported, previously audited structural input.  This report does not reprove the existence or description of the ownership components.

## 3. Exact four-ledger multistep theorem

Define the word operator and its suffixes by

\[
 M_w=P_TP_{T-1}\cdots P_1,
 \qquad
 Q_t=P_TP_{T-1}\cdots P_{t+1},
 \qquad Q_T=I.
 \tag{3.1}
\]

The order in (3.1) matters.  In general \(Q_t\) is neither an orthogonal projection nor self-adjoint.

Define the deterministic coherent path

\[
 g_0=f_0,
 \qquad
 g_t=P_tg_{t-1}.
 \tag{3.2}
\]

The four ledgers are

\[
 \mathcal D_w
 =\sum_{t=1}^T
   \|g_{t-1}-\tau_tg_{t-1}\|_H^2,
 \tag{3.3}
\]

\[
 \mathcal N_w
 =\sum_{t=1}^T
   \mathbb E\sum_K\|Q_t\delta_{t,K}\|_H^2,
 \tag{3.4}
\]

\[
 \mathcal A_w
 =\sum_{t=1}^T
   \mathbb E\|f_{t-1}-\tau_tf_{t-1}\|_H^2,
 \tag{3.5}
\]

and

\[
 \mathcal R_w
 =\sum_{t=1}^T
   \mathbb E\sum_K\|\delta_{t,K}\|_H^2.
 \tag{3.6}
\]

The expectations in (3.4)--(3.6) include the earlier heat history on which the current components may depend.

### Theorem 3.1 (exact multistep heat and double telescope)

Under the filtration and fairness hypotheses of Section 2,

\[
 \boxed{
 f_T=M_wf_0+\sum_{t=1}^TQ_t\xi_t,
 }
 \tag{3.7}
\]

\[
 \boxed{
 \mathbb E\left\|f_T-M_wf_0\right\|_H^2
 =\frac14\mathcal N_w,
 }
 \tag{3.8}
\]

and

\[
 \boxed{
 \mathcal D_w
 =4\bigl(\|f_0\|_H^2-\|M_wf_0\|_H^2\bigr).
 }
 \tag{3.9}
\]

Consequently,

\[
 \boxed{
 \mathbb E\Phi_H(F_T)-\Phi_H(F_0)
 =\frac{\mathcal N_w-\mathcal D_w}{4},
 }
 \tag{3.10}
\]

or, in the half-energy normalization,

\[
 \boxed{
 \mathbb E\Psi_H(F_T)-\Psi_H(F_0)
 =\frac{\mathcal N_w-\mathcal D_w}{8}.
 }
 \tag{3.11}
\]

There is also the exact one-step stochastic telescope

\[
 \boxed{
 \mathbb E\Phi_H(F_T)-\Phi_H(F_0)
 =\frac{\mathcal R_w-\mathcal A_w}{4}.
 }
 \tag{3.12}
\]

Finally, define, for \(t<s\),

\[
 h_{t,K}^{(t)}=\delta_{t,K},
 \qquad
 h_{t,K}^{(s)}=P_sP_{s-1}\cdots P_{t+1}\delta_{t,K},
 \tag{3.13}
\]

and define the suffix-filtering energy

\[
 \mathcal F_w
 =\frac14\sum_{1\le t<s\le T}
   \mathbb E\sum_K
   \left\|h_{t,K}^{(s-1)}-
       \tau_sh_{t,K}^{(s-1)}\right\|_H^2.
 \tag{3.14}
\]

Then

\[
 \boxed{
 \mathcal R_w-\mathcal N_w
 =\mathcal A_w-\mathcal D_w
 =\mathcal F_w\ge0.
 }
 \tag{3.15}
\]

#### Proof

Iterating (2.2) gives (3.7).  Because the word was frozen before the signs, every \(Q_t\) is deterministic after conditioning on the word.  If \(s<t\), then \(Q_s\xi_s\) is measurable before the time-\(t\) signs, while

\[
 \mathbb E(\xi_t\mid\mathcal F_{t-1})=0.
\]

Therefore

\[
 \mathbb E\langle Q_s\xi_s,Q_t\xi_t\rangle_H=0.
\]

The same conditional mean-zero property kills the cross term with \(M_wf_0\).  At one time, conditional independence of the component signs gives

\[
 \mathbb E\|Q_t\xi_t\|_H^2
 =\frac14\mathbb E\sum_K\|Q_t\delta_{t,K}\|_H^2.
\]

Summing proves (3.8).

Apply (1.5) to \(g_{t-1}\).  Since \(g_t=P_tg_{t-1}\),

\[
 \|g_{t-1}\|_H^2-\|g_t\|_H^2
 =\frac14\|g_{t-1}-\tau_tg_{t-1}\|_H^2.
\]

Summing over \(t\) proves (3.9).  Equations (3.8) and (3.9) give

\[
\mathbb E\|f_T\|_H^2
 =\|f_0\|_H^2+\frac14(\mathcal N_w-\mathcal D_w),
\]

which proves (3.10) and (3.11), because \(B_H\) is factor-independent.

Conditioning directly at time \(t\), equations (1.5) and (2.2) give

\[
 \mathbb E\bigl(\|f_t\|_H^2-\|f_{t-1}\|_H^2
       \mid\mathcal F_{t-1}\bigr)
 =\frac14\left(
   \sum_K\|\delta_{t,K}\|_H^2
   -\|f_{t-1}-\tau_tf_{t-1}\|_H^2
   \right).
\]

Taking expectations and summing proves (3.12).

For fixed \(t,K\), apply (1.5) successively to (3.13):

\[
\|h_{t,K}^{(s-1)}\|_H^2-
\|h_{t,K}^{(s)}\|_H^2
=\frac14
 \|h_{t,K}^{(s-1)}-\tau_sh_{t,K}^{(s-1)}\|_H^2.
\]

Telescoping from \(s=t+1\) to \(T\) gives

\[
\|\delta_{t,K}\|_H^2-
\|Q_t\delta_{t,K}\|_H^2
=\frac14\sum_{s=t+1}^T
 \|h_{t,K}^{(s-1)}-\tau_sh_{t,K}^{(s-1)}\|_H^2.
\]

After summing and taking expectations, this is

\[
 \mathcal R_w-\mathcal N_w=\mathcal F_w.
\]

Equating (3.10) and (3.12) now gives

\[
 \mathcal A_w-\mathcal D_w
 =\mathcal R_w-\mathcal N_w
 =\mathcal F_w.
\]

Every summand in (3.14) is nonnegative, proving (3.15).  \(\square\)

### Interpretation of the four ledgers

Equation (3.8) is an exact orthogonality statement in the probability Hilbert space.  The surviving noises \(Q_t\xi_t\) from different times have zero expected inner product.  Noncommutativity of the projections does not change this.

Equation (3.15) identifies the only way raw fair noise disappears.  A later projection dissipates part of an earlier component effect.  Exactly the same amount reappears as the excess of the random-state coherent displacement \(\mathcal A_w\) over the deterministic-mean displacement \(\mathcal D_w\).  Thus it would be misleading both to say that multistep noise is never reduced and to say that independent noises cancel.  It is reduced by suffix filtering, and the surviving terms do not cancel in expected squared norm.

The last heat step is completely unfiltered:

\[
 \mathcal N_w\ge
 \mathbb E\sum_K\|\delta_{T,K}\|_H^2.
 \tag{3.16}
\]

Therefore a palindrome or a sweep can erase some old noise but cannot erase fresh terminal noise unless the final component effects themselves vanish.

## 4. Integral restitution

The preceding theorem used only Hilbert geometry and conditional fairness.  Integrality supplies an additional lower bound.

For each rank define

\[
 \mathcal N_{w,q}
 =\sum_t\mathbb E\sum_K
   \|(Q_t\delta_{t,K})_q\|_2^2.
 \tag{4.1}
\]

Put

\[
 u_q=\frac{W}{N_q}\mathbf1+(M_wf_0)_q,
 \qquad
 \Theta_q(u_q)
 =\sum_S\{u_q(S)\}\bigl(1-\{u_q(S)\}\bigr),
 \tag{4.1a}
\]

where \(\{x\}\) denotes fractional part.

### Proposition 4.1 (universal rankwise integer-floor restitution)

For every starting exact factor and every frozen word,

\[
 \boxed{
 \mathcal N_{w,q}
 \ge4\Theta_q(u_q)
 \ge4\left(\beta_q-\|(M_wf_0)_q\|_2^2\right)_+.
 }
 \tag{4.2}
\]

Consequently,

\[
 \boxed{
 \mathcal N_w
 \ge4\sum_{q=0}^H
 \frac{\left(\beta_q-\|(M_wf_0)_q\|_2^2\right)_+}{c_q}
 \ge4\left(B_H-\|M_wf_0\|_H^2\right)_+.
 }
 \tag{4.3}
\]

Equivalently,

\[
 \boxed{
 \mathcal N_w\ge
 \left(\mathcal D_w-4\Phi_H(F_0)\right)_+.
 }
 \tag{4.4}
\]

#### Proof

For an integer-valued random variable \(Z\) with mean \(z=k+p\), where
\(k\in\mathbb Z\) and \(0\le p<1\), the pointwise inequality

\[
 (Z-k)(Z-k-1)\ge0
\]

gives

\[
 \operatorname{Var}(Z)\ge p(1-p).
 \tag{4.5}
\]

Every terminal coordinate \(\mu_{T,q}(S)\) is integral, and its mean is
\(u_q(S)\).  The rankwise form of (3.8) therefore gives

\[
 \frac14\mathcal N_{w,q}
 =\sum_S\operatorname{Var}\bigl(\mu_{T,q}(S)\bigr)
 \ge\Theta_q(u_q).
 \tag{4.6}
\]

It remains to compare this scalar wall with the rank floor.  Put
\(p_S=\{u_q(S)\}\).  Since \(\sum_Su_q(S)=W\) is integral,
\(\sum_Sp_S=L\) is an integer.  The hypersimplex

\[
 \{p\in[0,1]^{N_q}:\sum_Sp_S=L\}
\]

is the convex hull of the \(0\)-\(1\) vectors having exactly \(L\) ones.
For completeness, if a point of this polytope has two fractional
coordinates, transfer the largest possible equal amount from one to the
other in the two opposite directions and express the original point as the
corresponding convex combination.  At least one new coordinate reaches
\(0\) or \(1\); induction on the number of fractional coordinates proves
the convex-hull assertion.  Hence there is a random such vector \(Y\) with
\(\mathbb EY_S=p_S\).  The vector

\[
 Z_S=\lfloor u_q(S)\rfloor+Y_S
\]

is integral of total mass \(W\), has mean \(u_q\), and satisfies

\[
 \mathbb E\left\|Z-\frac{W}{N_q}\mathbf1\right\|_2^2
 =\|(M_wf_0)_q\|_2^2+\Theta_q(u_q).
 \tag{4.7}
\]

Every realization of \(Z\) has squared centered norm at least \(\beta_q\)
by (1.2).  Thus (4.7) is at least \(\beta_q\), proving the second
inequality in (4.2).

Alternatively, the weaker second inequality follows immediately from the
fact that every terminal leaf has an integral rank-\(q\) load vector of
total mass \(W\):

\[
 \mathbb E\|(f_T)_q\|_2^2\ge\beta_q.
\]

The rankwise form of (3.8) gives

\[
\mathbb E\|(f_T)_q\|_2^2
 =\|(M_wf_0)_q\|_2^2+\frac14\mathcal N_{w,q}.
\]

This also proves the second inequality in (4.2).  Sum with weights
\(1/c_q\), and use that a sum of positive parts is at least the positive
part of the sum, to obtain (4.3).  Finally,

\[
 4(B_H-\|M_wf_0\|_H^2)
 =\mathcal D_w-4\Phi_H(F_0),
\]

which proves (4.4).  \(\square\)

The constant \(4\) is forced by the normalization
\(\xi_t=\frac12\sum_K\varepsilon_{t,K}\delta_{t,K}\).  Proposition 4.1
is valid without global minimality.  It says that whenever the fractional
coherent product falls below the closest integral floor, surviving
component variance must refill the deficit.  The coordinatewise
integer-variance wall remains valid for any centered terminal law;
conditional sign independence is used to identify that law's variance
with \(\mathcal N_{w,q}/4\).

## 5. Global-minimizer restitution

Fix the window \(H\) and its weights, and let \(F_*\) globally minimize \(\Phi_H\) over all exact middle wreath factors.  The minimizer may depend on \(H\), and in the Gaussian application it may depend on the fixed constant \(A\).

### Theorem 5.1 (wordwise restitution at a global minimizer)

For every transposition word frozen before its heat signs,

\[
 \boxed{
 \mathcal N_w(F_*)\ge\mathcal D_w(f_*).
 }
 \tag{5.1}
\]

Equivalently,

\[
 \boxed{
 \mathcal R_w(F_*)\ge\mathcal A_w(F_*).
 }
 \tag{5.2}
\]

Together with (3.15), this yields

\[
 \boxed{
 \mathcal R_w(F_*)
 \ge\mathcal D_w(f_*)+\mathcal F_w.
 }
 \tag{5.3}
\]

Equality in (5.1) holds if and only if every positive-probability terminal leaf is a global minimizer.  In the standard component cube, the all-old side choice has positive probability and leaves the current factor unchanged.  Hence equality is equivalently characterized by every exact factor reachable at every intermediate level lying in the global-minimizer set.

#### Proof

Every terminal leaf is an exact factor, so

\[
 \Phi_H(F_T)\ge\Phi_H(F_*)
\]

pointwise.  Taking expectations in (3.10) proves (5.1).  Equation (3.12) gives (5.2), and (3.15) then gives (5.3).

The nonnegative random variable \(\Phi_H(F_T)-\Phi_H(F_*)\) has expectation zero exactly when it is zero at every positive-probability terminal leaf.  If an intermediate factor is reachable, choosing all-old sides at every remaining step preserves it through the end, proving the final equivalence.  \(\square\)

The conclusion is an expected restitution inequality, not a pathwise comparison of \(Q_t\delta_{t,K}\) with the coherent displacement.  It is also false for a general nonminimal starting factor: component heat can then have negative expected drift.

If a deterministic word satisfies

\[
 \|M_wf_*\|_H^2\le\theta\|f_*\|_H^2,
 \qquad 0\le\theta\le1,
\]

then (3.9) and (5.1) give

\[
 \boxed{
 \mathcal N_w(F_*)
 \ge4(1-\theta)\|f_*\|_H^2.
 }
 \tag{5.4}
\]

In particular, a coherent quarter-contraction forces

\[
 \mathcal N_w(F_*)\ge3\|f_*\|_H^2
 =3\bigl(B_H+\Phi_H(F_*)\bigr).
 \tag{5.5}
\]

Thus at a global minimizer strong coherent smoothing necessarily creates, or leaves, commensurate propagated component variance.

## 6. The corrected \(4(n-1)\) floor and iid words

### 6.1 Exact-factor Johnson support

For every coordinate \(x\), exact wreath regularity gives the same point-star sum for \(\mu_q(F)\) as for its constant mean.  Therefore

\[
 \sum_{S\ni x}f_q(S)=0
 \tag{6.1}
\]

for every \(x\), and also \(\sum_Sf_q(S)=0\).  Hence the Johnson degrees \(0\) and \(1\) vanish.  Write

\[
 f_q=\sum_{j\ge2}f_q^{(j)}.
\]

For unordered coordinate transpositions, counted once,

\[
 \sum_\tau\|v-\tau v\|_2^2
 =2\sum_j j(n-j+1)\|v^{(j)}\|_2^2.
 \tag{6.2}
\]

It follows that

\[
 \boxed{
 \sum_\tau\|f-\tau f\|_H^2
 \ge4(n-1)\|f\|_H^2.
 }
 \tag{6.3}
\]

The coefficient is attained on the ambient Johnson degree-\(2\) space.  This is spectral sharpness; it is not an assertion that an exact factor attains equality.

### 6.2 Recovery of the one-step component-noise floor

For a one-letter word \(w=(\tau)\),

\[
 \mathcal D_\tau=\|f_*-\tau f_*\|_H^2,
 \qquad
 \mathcal N_\tau=\sum_K\|\delta_{\tau,K}\|_H^2.
\]

Theorem 5.1 applies separately to every \(\tau\).  Therefore, with

\[
 R_H(F_*)=\sum_\tau\sum_K\|\delta_{\tau,K}\|_H^2,
\]

equations (5.1) and (6.3) give

\[
 \boxed{
 R_H(F_*)
 \ge \sum_\tau\|f_*-\tau f_*\|_H^2
 \ge4(n-1)\|f_*\|_H^2.
 }
 \tag{6.4}
\]

Since \(\|f_*\|_H^2=B_H+\Phi_H(F_*)=B_H+2\Psi_H(F_*)\),

\[
 \boxed{
 R_H(F_*)
 \ge4(n-1)\bigl(B_H+\Phi_H(F_*)\bigr)
 =4(n-1)\bigl(B_H+2\Psi_H(F_*)\bigr).
 }
 \tag{6.5}
\]

This is the corrected floor.  The older coefficient \(2n\) used only mean zero and missed the exact-factor zero-point-margin constraint.

There are \(\binom n2\) unordered transpositions.  Dividing (6.4) by \(\binom n2\), the corresponding uniform-transposition average is

\[
 \boxed{
 \mathbb E_\tau\mathcal N_\tau
 \ge\frac8n\|f_*\|_H^2.
 }
 \tag{6.6}
\]

An ordered-transposition sum would double (6.4).  These normalization facts are essential: \(4(n-1)\) must not be inserted as a lower bound for each letter of one word.

### 6.3 Exact iid coherent and suffix-noise formulas

Let the letters \(\tau_t\) be iid uniform unordered coordinate transpositions, sampled with replacement independently of all heat signs.  Require the component policy at time \(t\) to be nonanticipating: it may use the prefix \(\tau_1,\ldots,\tau_t\) and the previous heat signs, but not the future suffix.

For Johnson degree \(j\), put

\[
 \alpha_j
 =1-\frac{j(n-j+1)}{n(n-1)}.
 \tag{6.7}
\]

Equation (6.2) and (1.5) give exactly

\[
 \mathbb E_\tau\|P_\tau v^{(j)}\|_2^2
 =\alpha_j\|v^{(j)}\|_2^2.
 \tag{6.8}
\]

For \(j\ge2\),

\[
 \alpha_j\le\alpha_2=1-\frac2n=:\rho.
 \tag{6.9}
\]

Independence of successive letters gives

\[
 \boxed{
 \mathbb E_w\|M_wf_0\|_H^2
 =\sum_{q=0}^H\sum_{j\ge2}
   \frac{\alpha_j^T\|f_{0,q}^{(j)}\|_2^2}{c_q}
 \le\rho^T\|f_0\|_H^2.
 }
 \tag{6.10}
\]

Consequently,

\[
 \boxed{
 \mathbb E_w\mathcal D_w
 =4\sum_{q=0}^H\sum_{j\ge2}
   \frac{(1-\alpha_j^T)\|f_{0,q}^{(j)}\|_2^2}{c_q}
 \ge4(1-\rho^T)\|f_0\|_H^2.
 }
 \tag{6.11}
\]

Every component effect has Johnson degrees \(j\ge2\).  Since the future iid suffix is independent of a prefix-measurable \(\delta_{t,K}\), the same calculation gives the exact annealed suffix formula

\[
 \boxed{
 \mathbb E_w\mathcal N_w
 =\sum_{t=1}^T\sum_{q=0}^H\sum_{j\ge2}
   \frac{\alpha_j^{T-t}}{c_q}
   \mathbb E\sum_K\|\delta_{t,K,q}^{(j)}\|_2^2.
 }
 \tag{6.12}
\]

Combining (3.11), (6.11), and (6.12) gives the exact annealed master identity

\[
\boxed{
\begin{aligned}
 \mathbb E_{w,\varepsilon}\Psi_H(F_T)-\Psi_H(F_0)
 =\frac18\Bigg[&
 \sum_{t,q,j\ge2}
 \frac{\alpha_j^{T-t}}{c_q}
 \mathbb E\sum_K\|\delta_{t,K,q}^{(j)}\|_2^2\\
 &-4\sum_{q,j\ge2}
 \frac{(1-\alpha_j^T)\|f_{0,q}^{(j)}\|_2^2}{c_q}
 \Bigg].
\end{aligned}}
 \tag{6.13}
\]

At a global minimizer, the bracket in (6.13) is nonnegative.  In particular,

\[
 \boxed{
 \mathbb E_w\mathcal N_w(F_*)
 \ge4(1-\rho^T)
 \bigl(B_H+\Phi_H(F_*)\bigr).
 }
 \tag{6.14}
\]

For

\[
 T_0=\lceil n\log2\rceil,
\]

one has \(\rho^{T_0}\le e^{-2T_0/n}\le1/4\), and therefore

\[
 \boxed{
 \mathbb E_w\mathcal N_w(F_*)
 \ge3\bigl(B_H+\Phi_H(F_*)\bigr).
 }
 \tag{6.15}
\]

Formula (6.12) is not valid for a fixed deterministic suffix after replacing \(\|Q_t\delta^{(j)}\|^2\) by \(\alpha_j^{T-t}\|\delta^{(j)}\|^2\).  It requires averaging a future iid suffix independent of the current effect.

### 6.4 Why the spectral floor does not accumulate per step

For every deterministic word,

\[
 0\le\mathcal D_w
 =4(\|f_0\|_H^2-\|M_wf_0\|_H^2)
 \le4\|f_0\|_H^2.
 \tag{6.16}
\]

Thus coherent losses add letter by letter but telescope to a bounded endpoint loss.  The one-step \(4(n-1)\) coefficient appears only after summing a one-step inequality over all \(\binom n2\) transpositions.  In an iid word it becomes the contraction rate \(8/n\) and then the geometric factor \(1-(1-2/n)^T\).  There is no legitimate bound obtained by multiplying \(4(n-1)B_H\) by the word length.

## 7. Products, palindromes, and commutators

### 7.1 A heat word is a positive subword average

For any word \(w=(\tau_1,\ldots,\tau_T)\), direct expansion gives

\[
 \boxed{
 M_w
 =2^{-T}\sum_{\epsilon\in\{0,1\}^T}
   \tau_T^{\epsilon_T}\cdots\tau_1^{\epsilon_1}.
 }
 \tag{7.1}
\]

Every coefficient is nonnegative.  Thus \(M_w\) is the transition operator of an inhomogeneous lazy walk through group subwords.  Cancellation in the full group product \(\tau_T\cdots\tau_1\) does not cancel the other \(2^T-1\) subwords.

There is an exact equality criterion.  For every vector \(x\),

\[
 \boxed{
 \|M_wx\|_H=\|x\|_H
 \quad\Longleftrightarrow\quad
 \tau_tx=x\ \text{for every }t.
 }
 \tag{7.2}
\]

To prove this, write the subword permutations in (7.1) as \(U_\epsilon\).  All \(U_\epsilon x\) have norm \(\|x\|_H\), and

\[
 \frac1{2^T}\sum_\epsilon\|U_\epsilon x\|_H^2
 -\left\|2^{-T}\sum_\epsilon U_\epsilon x\right\|_H^2
 =\frac1{2^{2T+1}}
   \sum_{\epsilon,\eta}
   \|U_\epsilon x-U_\eta x\|_H^2.
 \tag{7.3}
\]

Equality of norms forces all subword images to agree.  Comparing the empty subword with each singleton subword gives \(\tau_tx=x\).  The converse is immediate.

In particular, even if the full group product is the identity, the sequential heat product is the identity only on the common fixed space of all letters.  Group relators do not undo heat.

For two transpositions, the group commutator is
\(\tau\sigma\tau^{-1}\sigma^{-1}=\tau\sigma\tau\sigma\).  It is a
relator only when \(\tau\) and \(\sigma\) commute; distinct transpositions
sharing one coordinate give a nontrivial group element.  The heat-product
conclusion above applies in either case.

### 7.2 Blocking and palindromes

Parenthesize the letters into any consecutive blocks.  If a block has heat operator \(A\) and receives coherent input \(x\), its complete internal contribution to \(\mathcal D_w\) is exactly

\[
 4(\|x\|_H^2-\|Ax\|_H^2)\ge0.
 \tag{7.4}
\]

Calling the block a product, relator, or commutator does not change this nonnegative telescope.

Let

\[
 A=P_{\tau_L}\cdots P_{\tau_1}.
\]

Appending the reverse word produces

\[
 \boxed{
 M_{ww^{\mathrm R}}=A^*A.
 }
 \tag{7.5}
\]

This is positive semidefinite and contractive; it is not \(A^{-1}A\).  Its eigenvalue-one space is precisely

\[
 \bigcap_{i=1}^L\ker(I-\tau_i).
 \tag{7.6}
\]

Thus a palindrome applies further smoothing.  It may filter noise born in its first half, but its second half injects fresh component noise, with the last contribution unfiltered by (3.16).

### 7.3 Projection commutator and leakage

For two transpositions,

\[
 \boxed{
 [P_\tau,P_\sigma]
 =P_\tau P_\sigma-P_\sigma P_\tau
 =\frac14(\tau\sigma-\sigma\tau).
 }
 \tag{7.7}
\]

The commutator vanishes for commuting transpositions.  Since the projections are self-adjoint, \([P_\tau,P_\sigma]\) is skew-adjoint, so

\[
 \langle x,[P_\tau,P_\sigma]x\rangle_H=0.
 \tag{7.8}
\]

It measures order-sensitive leakage; it is a signed difference of two legal mean operators, not itself a legal heat step.

Suppose \(\tau\delta=-\delta\), as for a \(\tau\)-component effect.  Then \(P_\tau\delta=0\).  A consecutive repeat of \(\tau\) therefore annihilates this earlier noise.  More generally, if a later \(P_\tau\) is separated only by projections commuting with \(P_\tau\), it still annihilates the effect.  In contrast, an intervening noncommuting \(P_\sigma\) can recreate a \(\tau\)-symmetric component:

\[
 \boxed{
 P_\tau P_\sigma\delta
 =[P_\tau,P_\sigma]\delta
 =\frac14(\tau\sigma-\sigma\tau)\delta,
 }
 \tag{7.9}
\]

which need not vanish.

For a general future suffix \(S\), a particular old effect \(\delta\) is exactly filtered if and only if

\[
 S\delta=0.
 \tag{7.10}
\]

Every \(\tau\)-anti-invariant effect is filtered if and only if

\[
 \boxed{
 S(I-\tau)=0,
 \quad\text{equivalently}\quad S=S\tau.
 }
 \tag{7.11}
\]

Equations (7.9)--(7.11) show why a repeated or palindromic schedule has no blanket annihilation theorem once noncommuting letters intervene.

### 7.4 Endpoint heat is not sequential heat

Let \(\sigma=\tau_T\cdots\tau_1\).  A direct endpoint cube comparing \(F\) with \(\sigma F\) has coherent mean

\[
 P_\sigma f=\frac{I+\sigma}{2}f
\]

and components obtained from the single endpoint overlay.  Here
\(P_\sigma\) is only notation for the endpoint midpoint; unless
\(\sigma^2=I\), it is not an orthogonal projection.  Sequential
recomputation has coherent mean

\[
 M_wf=P_{\tau_T}\cdots P_{\tau_1}f
\]

and a new component partition after every exact heat choice.  In general

\[
 P_\sigma\ne M_w.
 \tag{7.12}
\]

If \(\sigma=I\), endpoint heat is the identity, whereas (7.2) says sequential heat still contracts every vector moved by at least one letter.  Endpoint bundle identities and sequential martingale identities therefore cannot be substituted for one another.

## 8. Exact answer to the cancellation question

There are three distinct notions that must not be conflated.

### 8.1 Fresh fair component heat: no cross-step cancellation

Under Theorem 3.1's hypotheses,

\[
 \mathbb E\left\|\sum_tQ_t\xi_t\right\|_H^2
 =\sum_t\mathbb E\|Q_t\xi_t\|_H^2
 =\frac14\mathcal N_w.
 \tag{8.1}
\]

There are no negative cross-time terms and no negative same-time cross-component terms.  Commutators do not change (8.1).

### 8.2 Suffix filtering: exact disappearance is possible

An early component effect can be attenuated or annihilated by \(Q_t\).  The complete amount erased is the nonnegative quantity

\[
 \mathcal F_w=\mathcal R_w-\mathcal N_w.
 \tag{8.2}
\]

This is the only cancellation-like phenomenon present in fresh fair heat.  It is a positive Dirichlet telescope, not interference between distinct random increments.

### 8.3 Correlated, deterministic, or adaptive choices: negative cross terms are possible algebraically

For arbitrary, nonmartingale increments \(z_t=Q_t\xi_t\), the terminal norm contains

\[
 2\sum_{s<t}\langle z_s,z_t\rangle_H
 +2\sum_t\langle M_wf_0,z_t\rangle_H.
 \tag{8.3}
\]

These terms can be negative.  Marginal fairness of each sign is not enough; conditional fairness given the past is what kills (8.3).  Likewise, if future transpositions are chosen after observing current signs, then the suffix \(Q_t\) is sign-dependent and the frozen-word proof of (3.8) fails.

Therefore deterministic or jointly correlated component choices may in principle arrange actual cancellation.  No theorem in this report excludes that possibility inside exact factors.  Conversely, no exact-factor correlated-sign theorem is proved that achieves useful cancellation.  Such a result would be a new signed-cut or routing theorem, not a consequence of heat projection or commutator algebra alone.

There is no abstract Hilbert-space obstruction to this: two propagated
increments \(z\) and \(-z\) cancel exactly.  What is unproved is their
simultaneous realization by legal component choices of genuine wreath
factors.  Moreover, if a correlated terminal law is still centered at a
fixed coherent midpoint, the scalar argument (4.5) forces its total
variance to be at least the fractional wall
\(\sum_q\Theta_q(u_q)/c_q\).  Correlation can cancel diagonal component
variance only down to that integral wall; a biased deterministic leaf
changes the mean and is not covered by this centered-law statement.

There are two intermediate scopes.  With frozen, or otherwise
sign-independent, future suffixes, conditional mean zero alone still kills
cross-time terms.  If signs within one time are correlated, however, the
diagonal expression in (3.8) must be replaced by

\[
 \sum_t\mathbb E\|Q_t\xi_t\|_H^2,
\]

including its within-time covariance Gram terms.  Conversely, if
\(\tau_t\) is chosen predictably from the previous heat history but before
the current signs, the one-step formula survives:

\[
\boxed{
 \mathbb E\Phi_H(F_T)-\Phi_H(F_0)
 =\frac14\sum_t\mathbb E\left[
   \sum_K\|\delta_{t,K}\|_H^2
   -\|f_{t-1}-\tau_tf_{t-1}\|_H^2
 \right].
}
\tag{8.4}
\]

What is then lost is the representation by one deterministic \(M_w\) and
deterministic suffixes \(Q_t\).  Adaptive routing can deliberately target
old noise, but it lies outside the frozen-word terminal orthogonality
theorem.

## 9. Orbit and short-word barriers

### 9.1 Multistep group-orbit invariant

Every exact component update under \(\tau_t\) has the form

\[
 \mu_t-\mu_{t-1}=(\tau_t-I)a_t
 \tag{9.1}
\]

for a suitable integral local vector \(a_t\).  Let

\[
 G=\langle\tau_1,\ldots,\tau_T\rangle.
\]

For every \(G\)-orbit \(\mathcal O\) of rank targets, \(\tau_t\) permutes \(\mathcal O\), so summing (9.1) over \(\mathcal O\) gives

\[
 \boxed{
 \sum_{S\in\mathcal O}\mu_T(S)
 =\sum_{S\in\mathcal O}\mu_0(S).
 }
 \tag{9.2}
\]

This remains true with dynamically recomputed components and arbitrarily correlated legal choices.

Let the graph on the \(n\) coordinate labels have edges \(\tau_1,\ldots,\tau_T\), with connected components \(V_1,\ldots,V_s\).  Then

\[
 G=\prod_{i=1}^s\operatorname{Sym}(V_i),
\]

and its orbits on rank-\(r\) subsets are exactly the profile classes

\[
 \mathcal O_{\mathbf k}
 =\{S:|S\cap V_i|=k_i\text{ for every }i\}.
 \tag{9.3}
\]

If \(t_{\mathcal O}\) is the invariant total in an orbit and balanced rank loads must be \(b_q\) or \(b_q+1\), a necessary condition for exact balance is

\[
 \boxed{
 b_q|\mathcal O|
 \le t_{\mathcal O}
 \le(b_q+1)|\mathcal O|
 \quad\text{for every }\mathcal O.
 }
 \tag{9.4}
\]

The coherent operator has the corresponding quantitative floor.  If \(\Pi_G\) denotes averaging within each orbit, then

\[
 \Pi_GM_wf=\Pi_Gf,
 \qquad
 \|M_wf\|_2^2
 \ge\|\Pi_Gf\|_2^2
 =\sum_{\mathcal O}
   \frac{\left(\sum_{S\in\mathcal O}f(S)\right)^2}{|\mathcal O|}.
 \tag{9.5}
\]

Hence a fixed finite-coordinate commutator cannot remove the part of a
discrepancy projected onto its invariant orbit classes.  The exact
criterion for a nonzero **coherent** orbit residue is

\[
 \boxed{\Pi_G f\ne0.}
 \tag{9.6}
\]

For integral floor balancing, the exact **orbit-total obstruction** is
instead the violation of one of the interval conditions (9.4); a nonzero
coherent residue can still be compatible with assigning \(b_q\) and
\(b_q+1\) inside each orbit.  Satisfaction of (9.4) does not by itself
prove reachability by legal component switches or common multidepth Hall
compatibility.

Connectivity of the transposition graph is sufficient to remove the
barrier on a fixed rank, because \(S_n\) is transitive there, but it is not
necessary on the exact-factor discrepancy space.  For example, if the
coordinate components have sizes \(n-1\) and \(1\), every orbit-invariant
rank function depends only on whether the isolated coordinate is present
and therefore lies in Johnson degrees \(0\) and \(1\).  Exact-factor
centered histograms are orthogonal to those degrees, so \(\Pi_Gf=0\)
automatically.  The familiar \(n-1\)-edge connectedness lower bound applies
to arbitrary unconstrained rank histograms, not to every zero-point-margin
exact-factor histogram.

Even when connectivity, or the exceptional zero-margin phenomenon, removes
this orbit obstruction, it does not prove component-noise control,
support-feasible mixing, or common multidepth Hall correction.

### 9.2 Untouched degree-two direction

Suppose the word touches at most \(n-4\) coordinates.  Choose four untouched coordinates \(a,b,c,d\).  On any central rank with \(2\le r\le n-2\), define

\[
 v(S)=
 (\mathbf1_{a\in S}-\mathbf1_{b\in S})
 (\mathbf1_{c\in S}-\mathbf1_{d\in S}).
 \tag{9.7}
\]

Then \(v\ne0\), its total and point margins vanish, and every letter of the word fixes it.  Hence

\[
 M_wv=v.
 \tag{9.8}
\]

In particular, if \(2T\le n-4\), a length-\(T\) word has no universal coherent gap on the full zero-point-margin signed space.  This is a signed-space obstruction only.  It is **not** an exact-factor counterexample: no nonnegative, packing-compatible realization of (9.7) as an exact-factor discrepancy is proved.

## 10. What the theorem proves, and what remains unproved

The exact conclusions are:

1. Every sequential heat leaf stays inside one integral exact factor.

2. For a word frozen before fresh conditionally independent component signs, the terminal component noises are orthogonal in expectation after their actual ordered suffixes.

3. Raw noise can be filtered, and the exact filtered amount is \(\mathcal F_w\).  No additional cross-step cancellation exists in the fair \(L^2\) ledger.

4. At a global fixed-window minimizer, propagated component noise must restitute the entire deterministic coherent loss: \(\mathcal N_w\ge\mathcal D_w\).

5. The one-step specialization recovers the corrected \(4(n-1)\) all-unordered-transpositions floor.  The iid multistep normalization is the contraction factor \(1-2/n\), not a repeated \(4(n-1)\) baseline.

6. Palindromes and group relators cannot reverse coherent smoothing.  Noncommuting projections can move old anti-invariant noise out of a future kernel, but cannot create negative fair variance.

7. A disconnected transposition graph preserves nontrivial orbit masses
exactly; it cannot absorb a residual defect that violates one of its orbit
mass constraints.

The following needed assertions remain **UNPROVED**:

* **UNPROVED propagated-noise upper bound.**  Nothing here bounds \(\mathcal N_w\) above by the coherent loss plus Catalan-scale or \(o(W)\) error.  This is the missing RFEN-type exact-factor input.

* **UNPROVED correlated cancellation theorem.**  Deterministic or jointly correlated component signs can have negative Hilbert cross terms algebraically, but no legal exact-factor assignment is proved to exploit them simultaneously across the Gaussian depth window.

* **UNPROVED commutator absorber.**  The identities in Section 7 do not prove that recomputed noncommuting overlays fragment into enough independently useful components, nor that their signs solve a bundled multidepth Hall problem.

* **UNPROVED connected-word mixing theorem.**  Connectivity of the
transposition graph removes the displayed profile-orbit obstruction but is
far from sufficient for exact-factor mixing.

* **UNPROVED realization of the signed obstruction.**  The untouched \(E_2\) vector (9.7) is not known to occur as the centered histogram of one exact factor.

* **UNPROVED implication to MWB.**  A quadratic heat identity alone does not construct a literal contiguous-OR word and does not prove the unlabelled overload bound.  The exact-factor route still needs a genuinely structural upper theorem on component restitution or a separate productive correlated-cut theorem.

## 11. Independent audit of the decisive step

The multistep theorem and its constants were independently checked in three directions.

* The martingale audit confirmed the factors \(1/4\) for \(\Phi_H\) and \(1/8\) for \(\Psi_H\), and confirmed that predictable recomputation of components is allowed while sign-dependent future letters are not.

* The spectral audit confirmed that the exact-factor centered histograms and component effects lie in Johnson degrees \(j\ge2\), that \(\alpha_j=1-j(n-j+1)/(n(n-1))\), and that the one-step unordered-transposition sum is exactly bounded below by \(4(n-1)\|f\|_H^2\).  It also confirmed that the corresponding uniform average is \(8\|f\|_H^2/n\), and that ordered transpositions would double the summed coefficient.

* The operator audit confirmed the subword expansion, palindrome operator \(A^*A\), commutator identity, exact filtering criterion, and the group-orbit invariant.  A separate challenge audit confirmed that marginally fair but temporally correlated signs may have negative cross terms; therefore the no-cancellation theorem must retain conditional fairness and a frozen word.

The audits also identified four scope warnings retained throughout the report: \(Q_t\) is not generally a projection; \(\mathcal D_w\) uses the deterministic coherent path rather than the random current factors; harmonic factors \(\alpha_j^{T-t}\) require an independent iid future suffix; and \(\mathcal N_w\ge\mathcal D_w\) requires global minimality or, equivalently, nonnegative expected terminal drift for the chosen start and word.

## 12. Final barrier statement

The strongest rigorous second-wave P conclusion is the following.

> **Exact multistep restitution barrier.**  Fix a depth window and an exact-factor global minimizer.  For every transposition product, palindrome, relator, or commutator schedule frozen before fresh component signs, the expected terminal energy change is the surviving suffix-filtered component variance minus the telescoping coherent Dirichlet loss, with factor \(1/4\).  Surviving component increments have no negative cross-time covariance.  Any reduction of earlier raw noise is exactly suffix Dirichlet filtering, and the total surviving noise is at least the coherent loss.  At one step, summing over unordered transpositions gives the corrected \(4(n-1)\) spectral floor.  No grouping of letters into commutators can lower this restitution requirement.  Escaping it requires either a new exact-factor upper bound on propagated component effects or a genuinely correlated deterministic routing theorem outside the fair heat ledger.

That barrier is exact.  The proposed multistep commutator route does not presently supply either missing theorem.
