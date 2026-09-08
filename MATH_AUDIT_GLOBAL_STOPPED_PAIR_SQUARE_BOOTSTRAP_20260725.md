# Global stopped martingale versus hereditary pair-square propagation

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The weighted stopped-martingale lemma in
GLOBAL_STOPPED_WEIGHTED_MARTINGALE_REPLACEMENT_20260725.md is correct.
It is a useful improvement: once a global drift-plus-quadratic-variation
budget \(B_mW=o(W)\) is available, one fixed corridor replaces all
roundwise tolerances.

It does not prove hereditary pair-square propagation. Three corrections
are essential.

1. A target fibre must be stopped **before** its direct consumption and
   must not count the consuming jump. Otherwise the diagonal lower bound
   is \(\Theta(KT)=\Theta(W\sqrt m)\).
2. The compensator is tautologically defined, but its bound is not. The
   predictable drift of a pair link is exactly the still-unproved
   conditioned mean-link estimate (CM).
3. The aggregate pair-square functional is neither a submartingale nor a
   supermartingale from codegree monotonicity. Its one-step drift contains
   both the conditioned link mean and the conditioned link variance. The
   existing raw triangle controls neither after the owner/priority tilt;
   the unsummed cross-slice physical-label term remains.

Thus global stopping removes the former tolerance/maximal-inequality
problem, but not CM, CFW, or physical square-label dispersal.

## 1. Audit of the abstract weighted Doob lemma

Let \(M_{t,F}\) be a square-integrable martingale, let \(A_{t,F}\) be
predictable, and put \(X=M+A\). If

\[
 \tau_F=\inf\{t:|X_{t,F}|\ge\eta\}\wedge(R+1),
\]

then on \(\{\tau_F\le R\}\), either

\[
 \sup_{t\le\tau_F}|A_{t,F}|\ge\eta/2
\]

or

\[
 \sup_{t\le\tau_F}|M_{t,F}|\ge\eta/2.
\]

Markov and Doob's \(L^2\) inequality therefore give

\[
 \Pr(\tau_F\le R)
 \le
 \frac{2}{\eta}\mathbb E\sup_{t\le\tau_F}|A_{t,F}|
 +\frac{16}{\eta^2}
 \mathbb E\langle M_F\rangle_{\tau_F\wedge R}.
 \tag{1.1}
\]

The coefficient four used for the first term in the source note is merely
looser. Multiplying by deterministic nonnegative fibre weights and summing
is valid. Hence if both weighted budgets total \(B_mW\), the choice
\(\eta=B_m^{1/4}\) charges \(O(B_m^{1/2}W)=o(W)\).

This theorem requires no maximum-increment bound. That is its genuine
advantage over a fibrewise Freedman union bound.

## 2. The direct-consumption lifetime

Let \(\lambda_x\) be the first bite in which a tentative or accepted chunk
directly uses target \(x\). The logarithm

\[
 \log\frac{D_t(x)}
 {D_0(x)\prod_{u<t}\rho_{u,s(x)}}
 \tag{2.1}
\]

is defined only while \(x\) is live. At \(\lambda_x\), the degree becomes
zero because the fibre leaves the residual problem.

If that jump is included, its relative loss is one. Summing its square
over consumed targets gives at least \(K\) per selected chunk and hence

\[
 \Theta(KT)=\Theta(W\sqrt m)
 \tag{2.2}
\]

through tag density \(1/\log m\). This is not a fluctuation ledger.

A correct stopped construction must use one of the following equivalent
forms.

* Work under the pair-root survival law, whose exact per-tag denominator
  is \(1-\alpha q_U(x)\), and freeze the fibre before direct consumption.
* Enlarge the filtration by the direct-hit indicators, and form the
  compensated process only on the no-direct-hit branch.
* Define the exit event as corridor exit strictly before \(\lambda_x\),
  and omit the consuming increment from both drift and quadratic
  variation.

Simply writing \(D_t(F)>0\) for a “live fibre” does not perform this
correction: the random lifetime and the terminal jump must enter the
definition of the stopped martingale.

## 3. What logarithmic degree stopping proves

On the survival branch, suppose the one-bite relative degree change has
absolute value at most \(1/2\). Then

\[
 \Delta X_{t,x}
 =
 \bigl(\Delta X_{t,x}
 -\mathbb E[\Delta X_{t,x}\mid\mathcal F_t]\bigr)
 +\mathbb E[\Delta X_{t,x}\mid\mathcal F_t]
 \tag{3.1}
\]

is an exact martingale-plus-predictable-drift decomposition. If its global
budgets are \(o(W)\), Theorem 1.1 gives simultaneous denominator
comparability outside \(o(W)\) fibres.

Two qualifications remain.

First, defining the compensator in (3.1) does not bound it. The claimed
common stratum contraction requires

\[
 \mathbb E[D_{t+1}(x)\mid\mathcal F_t,\ x\text{ survives}]
 =(1+o_t(1))a_tD_t(x).
 \tag{3.2}
\]

This is the one-resource mean-spread statement. Its weighted physical
sum is not a consequence of the raw triangle.

Second, a bite which changes a surviving fibre by more than \(1/2\) can
be declared an exit, but its total physical weight still needs proof.
The pathwise deadline Bernstein bound does not automatically imply the
corresponding target-fibre degree bound after the current tilt. This
large-jump ledger is part of (3.2) or of the conditioned maximum-influence
statement; it cannot merely be asserted as already scalar.

## 4. Pair-square has no automatic martingale sign

For a live anchor \(x\), write

\[
 S_{t,h}(x)
 =
 \sum_{|y|=|x|+h}
 \frac{C_t(x,y)^2}{D_t(x)D_t(y)}.
 \tag{4.1}
\]

Although \(C_{t+1}(x,y)\le C_t(x,y)\), both denominators also decrease.
Consequently (4.1) has no deterministic monotonicity. The exact
concentration gadget in
MATH_AUDIT_DYNAMIC_QUARANTINE_FOUR_WALK_CONDITIONING_GATE_20260725.md
has

\[
 S_t(x)=O(1/m)
 \quad\text{and}\quad
 S_{t+1}(x)\ge1
 \tag{4.2}
\]

after one legal width-two choice, whereas deleting the common
\((x,y)\)-link instead makes its contribution decrease to zero. Thus,
by choosing the law of the legal trigger, either drift sign is possible.

More formally, on the good denominator event

\[
 D_{t+1}(v)\ge(1-e_t)a_tD_t(v),
\]

the exact second-moment identity gives

\[
\begin{aligned}
 \mathbb E S_{t+1,h}(x)
 \le \frac{1}{(1-e_t)^2a_t^2}
 \sum_y
 \frac{
  \bigl(\mathbb E C_{t+1}(x,y)\bigr)^2
  +\operatorname{Var}C_{t+1}(x,y)}
 {D_t(x)D_t(y)}.
 \tag{4.3}
\end{aligned}
\]

The first term in (4.3) needs the conditioned mean-link contraction

\[
 \mathbb E[C_{t+1}(x,y)\mid\mathcal A_{xy}]
 =(1+o_t(1))b_tC_t(x,y),
 \tag{CM}
\]

and the second needs the conditioned four-walk estimate

\[
 \sum_y
 \frac{\operatorname{Var}(C_{t+1}(x,y)\mid\mathcal A_{xy})}
 {D_t(x)D_t(y)}
 \le
 O(\alpha_t\beta)b_t^2S_{t,h}(x)+b_t^2E_{t,h}(x).
 \tag{CFW}
\]

Only after (CM) and (CFW), with \(b_t^2/a_t^2=q_t^{-2}\), does the desired
one-bite drift follow. Optional stopping changes none of these algebraic
requirements.

If one instead defines the Doob decomposition of \(S_t\) itself, the
martingale part is automatic but its predictable drift is precisely the
right side of (4.3) minus \(S_t\). Its quadratic variation involves
fluctuations of the squared links and is not bounded by the original
one-anchor triangle without another higher or truncated influence
estimate. This reformulation is therefore circular.

## 5. Existing raw triangle versus stopped tilts

The refined raw estimate

\[
 \mathfrak T_0(x)
 =
 O\left(m^{-1}+gm^{-3/2}\right)
 =m^{-1+o(1)}
 \tag{5.1}
\]

is sufficient numerically. Summed over the Gaussian target band and
inflated by \(z^{-2}\) through \(z=1/\log m\), it gives the prospective
budget

\[
 B_mW=m^{-1/2+o(1)}W=o(W).
 \tag{5.2}
\]

What is absent is the implication from (5.1) to the same estimate under
the stopped, owner/priority-weighted, two-root survival law. Down-set
entropy counts

\[
 \sum_{\omega,x,y}N_\omega(x,y),
\]

whereas (CFW) contains the cross-slice square

\[
 \sum_{x,y}
 \frac{\bigl(\sum_\omega N_\omega(x,y)\bigr)^2}
 {D_t(x)D_t(y)}.
 \tag{5.3}
\]

Stopping at small degree CV controls one-resource denominators. It does
not disperse the physical pair labels in (5.3), and it does not prove
(CM).

## 6. Exact boundary

The global stopped-martingale theorem may now be used as follows:

1. impose the direct-consumption lifetime correction of Section 2;
2. prove the weighted stopped one-resource drift and quadratic-variation
   budget for logarithmic degrees;
3. separately prove (CM) and (CFW), or the equivalent stopped
   physical square-label dispersal inequality; and
4. apply one global corridor with \(\eta=B_m^{1/4}\).

Step 4 is fully proved and removes the former roundwise tolerance loss.
The current raw triangle, cube erosion, and down-set entropy inputs do not
prove Steps 2--3 under the required residual quantifiers. In particular,
the aggregate pair-square functional is not presently a controlled
submartingale. The exact surviving statement is the pair-rooted,
survival-conditioned physical-label theorem, not another maximal
inequality.

No coefficient-one conclusion follows.
