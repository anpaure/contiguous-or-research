# Direct chi-square channel contraction and the physical mismatch gate

**Date:** 2026-08-06  
**Method:** weighted data processing, an exact conditional coupling, and
one-step Young absorption; no computation or search  
**Status:** unconditional analytic theorem and proof-safe reduction.  It
bypasses every freely normalized auxiliary switch generator.  The sole
remaining analytic input is a coefficient-faithful bound on one literal
next-state mismatch carre.  The later authoritative expansion
`MATH_THEOREM_LITERAL_FIFO_DIAGONAL_CHISQUARE_UPDATE_AND_ADJOINT_FOURTH_ORDER_GATE_20260806.md`
shows that complete-row blocker conjugation can pay a switch-dependent
subface under the response aperture in Section 6, but the full native FIFO
mismatch also contains an adjoint survivor innovation which need not
factor through current switch scores.

## 1. The normalized incidence potential

Fix one resource type.  Let

\[
 c_x=\beta Y_x>0,\qquad e_x=g_x-c_x,\qquad
 f_x={e_x\over c_x}.
\tag{1.1}
\]

Because \(\beta=(\sum_xg_x)/(\sum_xY_x)\),

\[
 \sum_xe_x=0,
 \qquad
 \Psi=\sum_x{e_x^2\over c_x}=\sum_xc_xf_x^2.
\tag{1.2}
\]

This is exactly the potential in
`MATH_THEOREM_NORMALIZED_INCIDENCE_CHISQUARE_SERVICE_IDENTITY_20260806.md`,
and

\[
                         \Psi={\mathfrak G_T\over\beta_T}.
\tag{1.3}
\]

The purpose of this note is to transport \((c,e)\) together before
expanding the one-step Bregman formula coordinate by coordinate.

## 2. Reference channels

Let \(c'_y>0\) and \(e'_y\) be the actual next-state reference and
centered incidence measures on a possibly different finite set.  A
nonnegative matrix \(J=(J_{xy})\) is called a **\(\sigma\)-reference
channel** when

\[
 \sum_xJ_{xy}=c'_y,
 \qquad
 \sum_yJ_{xy}\le \sigma c_x.
\tag{2.1}
\]

The allowed support of \(J\) is part of the definition in an application.
For the FIFO host it must consist of literal identity transports and
literal resource transports certified by the accepted transition.  An
unrestricted product coupling is algebraically legal but physically
useless.

Transport the old likelihood error through \(J\):

\[
 \bar e'_y=\sum_xJ_{xy}f_x,
 \qquad
 h'_y=e'_y-\bar e'_y,
 \qquad
 H(J)=\sum_y{(h'_y)^2\over c'_y}.
\tag{2.2}
\]

Coordinates with \(c'_y=e'_y=0\) are omitted.  A state with
\(c'_y=0\ne e'_y\) has infinite mismatch and is correctly rejected.

### Lemma 2.1 (exact channel contraction)

For every \(\sigma\)-reference channel,

\[
 \boxed{
 \sum_y{(\bar e'_y)^2\over c'_y}\le\sigma\Psi.}
\tag{2.3}
\]

#### Proof

Columnwise Cauchy--Schwarz gives

\[
 {\left(\sum_xJ_{xy}f_x\right)^2\over\sum_xJ_{xy}}
 \le\sum_xJ_{xy}f_x^2.
\]

Sum over \(y\), use (2.1), and obtain

\[
 \sum_y{(\bar e'_y)^2\over c'_y}
 \le\sum_xf_x^2\sum_yJ_{xy}
 \le\sigma\sum_xc_xf_x^2.
\]

This is (2.3). \(\square\)

Thus all motion common to the numerator and its reference measure is
automatically paid.  Pure thinning, pure death, deterministic
rescaling, and scalar motion of \(\beta\) create no nonlinear loss when
they are placed in the same channel.

## 3. Random next states and the direct service inequality

Condition on the present state.  Let \(\omega\) denote the accepted next
transition.  For every \(\omega\), choose a physical
\(\sigma_\omega\)-reference channel \(J^\omega\), and define
\(H_\omega=H(J^\omega)\).  Assume

\[
                         \mathbb E_i\sigma_\omega\le a_i<1.
\tag{3.1}
\]

In the balanced-doublet application, \(a_i=\rho_i^2\).

### Theorem 3.1 (coefficient-faithful chi-square service)

For every \(0<\varepsilon<1\),

\[
 \boxed{
 \mathbb E_i\Psi_{i+1}
 \le
 \bigl(a_i+\varepsilon(1-a_i)\bigr)\Psi_i
 \left(1+{a_i\over\varepsilon(1-a_i)}\right)
       \mathbb E_iH_\omega.}
\tag{3.2}
\]

In particular,

\[
 \boxed{
 \mathbb E_i\Psi_{i+1}
 \le
 \left(1-{1-a_i\over2}\right)\Psi_i
 {2\over1-a_i}\mathbb E_iH_\omega.}
\tag{3.3}
\]

#### Proof

In the Hilbert norm \(\|u\|_{c'^{-1}}^2=\sum_yu_y^2/c'_y\),

\[
 \Psi_{i+1}
 =\|\bar e'^{\,\omega}+h'^{\,\omega}\|_{c'^{-1}}^2
 \le \sigma_\omega\Psi_i
      +2\sqrt{\sigma_\omega\Psi_iH_\omega}+H_\omega
\tag{3.4}
\]

by Lemma 2.1.  Conditional Cauchy--Schwarz and (3.1) give

\[
 \mathbb E_i\sqrt{\sigma_\omega H_\omega}
 \le\sqrt{a_i\mathbb E_iH_\omega}.
\]

Apply

\[
 2\sqrt{a_i\Psi_i\mathbb E_iH_\omega}
 \le \varepsilon(1-a_i)\Psi_i
    +{a_i\over\varepsilon(1-a_i)}\mathbb E_iH_\omega.
\]

This proves (3.2).  Take \(\varepsilon=1/2\) and use

\[
 1+{2a_i\over1-a_i}={1+a_i\over1-a_i}
 \le {2\over1-a_i}
\]

to obtain (3.3). \(\square\)

No likelihood-ratio maximum and no Johnson Poincare inequality appears.
The coefficient of \(H_\omega\) is forced by the physical service
\(1-a_i\); there is no rescalable orbit scalar.

## 4. Stopped cumulative form and `GDIR`

Put \(h_i=1-a_i\).  Iterating (3.3) to any finite stopped time \(\tau\)
and using \(\Psi_\tau\ge0\) gives

\[
 \boxed{
 \mathbb E\sum_{i<\tau}h_i\Psi_i
 \le2\Psi_0+4\mathbb E\sum_{i<\tau}{H_i\over h_i},}
\tag{4.1}
\]

where \(H_i=\mathbb E_iH_\omega\).

There is also a local absorption form.  If

\[
 H_i\le\eta h_i^2\Psi_i+h_iJ_i,
 \qquad 0\le\eta<\frac14,
\tag{4.2}
\]

then

\[
 \boxed{
 \left({1\over2}-2\eta\right)
 \mathbb E\sum_{i<\tau}h_i\Psi_i
 \le\Psi_0+2\mathbb E\sum_{i<\tau}J_i.}
\tag{4.3}
\]

For example, \(\eta=1/8\) gives

\[
 \mathbb E\sum_{i<\tau}h_i\Psi_i
 \le4\Psi_0+8\mathbb E\sum_{i<\tau}J_i.
\tag{4.4}
\]

On the authenticated global-rate stop,

\[
 0<\lambda_-\le X_i(1-a_i)\le\lambda_+<\infty,
\tag{4.5}
\]

and in fact \(X_i(1-a_i)=2+o(1)\).  Hence

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{\mathfrak G_T(i)\over
                              \beta_T(i)X_i}
 =\mathbb E\sum_{i<\tau}{\Psi_i\over X_i}
 \le {1\over\lambda_-}
       \mathbb E\sum_{i<\tau}h_i\Psi_i.}
\tag{4.6}
\]

Equations (4.1) or (4.3) therefore prove `GDIR` as soon as the literal
channel mismatch has the corresponding cumulative budget.  At the
complete orbit \(\Psi_0=0\).

## 5. Relation to the adapted Bregman identity

Theorem 3.1 is not a new potential.  It is a grouped form of the exact
identity in
`MATH_THEOREM_NORMALIZED_INCIDENCE_CHISQUARE_SERVICE_IDENTITY_20260806.md`.
For the ideal diagonal channel with \(c'=a_ic\),

\[
 \bar e'=a_ie,
 \qquad
 h'=e'-a_ie=\delta g-\delta c.
\tag{5.1}
\]

Expanding \(\|a_ie+h'\|^2/(a_ic)\) gives the same linear and quadratic
terms as the Bregman identity.  A nontrivial reference channel performs
the common root/reference transport before expansion.  This automatically
coalesces:

* scalar motion of \(\beta\);
* the mean one-root motion;
* every genuinely common numerator/reference death; and
* the predictable part of the adapted innovation.

The residual \(h'\) is exactly the part for which numerator incidence and
reference mass do not use the same literal transition.  It is the direct
chi-square version of the signed Duhamel boundary plus its centered
innovation.  Therefore a bound on \(H_i\) is coefficient-faithful by
construction.

## 6. Exact interface with complete-row blocker conjugation

For the actual first-kill boundary, write

\[
 \mathcal E_i^{\rm row}
 =\sum_{(A,\tau,G)\in\mathcal B_i}
   w_i(A,\tau,G)(g_A-g_{\tau A})^2,
 \qquad
 g_A=\sum_{x\in U_A^\circ\cap T}f_x.
\tag{6.1}
\]

Here \(w_i\) is the literal transition/future coefficient from the
complete-row theorem; it is not an auxiliary conductance.  The proved
blocker conjugation implication supplies

\[
 \mathbb E\sum_{i<\tau}{\beta_T(i)d\over X_i}
                 \mathcal E_i^{\rm row}\le C\mathsf A
\tag{6.2}
\]

once its explicitly stated complete-row first-entry input is present.

The exact normalization-free aperture needed to combine (6.2) with
Theorem 3.1 is

\[
 \boxed{
 H_i\le
 \eta h_i^2\Psi_i
 +C h_i{\beta_T(i)d\over X_i}\mathcal E_i^{\rm row}
 +h_iJ_i^{\rm root/two},
 \qquad \eta<\frac14.}
\tag{CHA}

Under `(CHA)`, (4.3) and (6.2) give

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{\mathfrak G_T(i)\over
                              \beta_T(i)X_i}
 \le C\left(\Psi_0+\mathsf A+
       \mathbb E\sum_{i<\tau}J_i^{\rm root/two}\right).}
\tag{6.3}
\]

Thus `(CHA)`, rather than `(NORM)`, is a sufficient direct `GDIR`
theorem whenever the displayed decomposition is valid.  Its coefficients
are forced: dividing `(CHA)` by
\(h_i\asymp X_i^{-1}\) produces exactly the already authenticated weight
\(\beta_Td/X_i\) in (6.2).

There is an exact operator version.  Let \(q_i\) be the vector with
coordinates \(g_A-g_{\tau A}\), and let \(W_i\) be diagonal with entries
\(w_i(A,\tau,G)\).  Suppose the literal channel residual has a response
factorization

\[
                         h'^{\,\omega}=R_i^\omega q_i+r_i^\omega.
\tag{6.4}
\]

If

\[
 \boxed{
 \mathbb E_i (R_i^\omega)^*D_{(c'^\omega)^{-1}}R_i^\omega
 \preceq C h_i{\beta_T(i)d\over X_i}W_i,}
\tag{6.5}
\]

and

\[
 \mathbb E_i\|r_i^\omega\|_{(c'^\omega)^{-1}}^2
 \le\eta_0h_i^2\Psi_i+h_iJ_i^{\rm root/two},
\tag{6.6}
\]

then `(CHA)` follows, with explicit constants, from
\(\|u+v\|^2\le(1+\theta)\|u\|^2+(1+\theta^{-1})\|v\|^2\).
For instance \(\theta=1\) gives the row coefficient \(2C\) and
\(\eta=2\eta_0\); it is enough that \(\eta_0<1/8\).

Equation (6.5) is the **physical response aperture**.  Unlike the former
switch normalization, every object in it is literal:

* \(R_i^\omega\) is the actual next-likelihood response;
* \(c'^\omega\) is the actual next reference measure;
* \(W_i\) contains the actual transition and future coefficients; and
* the external factor is exactly the already present
  \(h_i\beta_Td/X_i\).

No scalar \(\alpha_i\) can be freely rescaled.

## 7. Sharp obstruction: current conjugation cannot pay new mismatch

The physical response aperture is not a consequence of service and
current complete-row conjugation alone.

### Proposition 7.1 (two-point innovation obstruction)

Let the current resource space have two points and take

\[
 c=(1,1),\qquad g=(1,1).
\tag{7.1}
\]

Then \(f=0\) and \(\Psi=0\).  Fix \(0<a<1\) and \(0<\epsilon<a\), and
let

\[
 c'=(a,a),\qquad g'=(a+\epsilon,a-\epsilon).
\tag{7.2}
\]

For every reference channel, \(\bar e'=J^*f=0\), and hence

\[
 \boxed{H(J)=\Psi'={2\epsilon^2\over a}>0.}
\tag{7.3}
\]

At the current state every complete-row score and every conjugate
difference is zero.  Also \(c'=ac\), so the reference/root motion relative
to ideal service is zero.  Therefore no inequality using only

\[
 (1-a)\Psi,qquad
 (g_A-g_{\tau A})^2,qquad
 \hbox{and the reference-motion carre}
\]

can bound the next chi-square creation.

#### Proof

All assertions except (7.3) follow from \(f=0\).  The next centered error
is \(e'=(\epsilon,-\epsilon)\), so

\[
 \Psi'={\epsilon^2\over a}+{\epsilon^2\over a}.
\]

This proves (7.3). \(\square\)

The example does not say that the FIFO host realizes this arbitrary
innovation.  It proves the exact logical boundary: the current complete-
row theorem must be supplemented by a theorem identifying the actual
next incidence response.  If the existing root-carre ledger already
contains that numerator innovation with the correct coefficient, it is
part of \(J_i^{\rm root/two}\); otherwise it is genuinely missing.

## 8. Zero mismatch and convex order

When \(\sum_yc'_y=\sigma\sum_xc_x\), every inequality in (2.1) is an
equality after summing over \(x\).  Normalize \(J\) to a coupling of the
probability measures proportional to \(c\) and \(c'\).  If \(H(J)=0\),
then

\[
 {e'_y\over c'_y}
 =\mathbb E\left[f(X)\mid Y=y\right].
\tag{8.1}
\]

Thus the next likelihood-ratio law is a conditional expectation of the
current one.  In particular it is below the current law in convex order,
and every convex divergence contracts.  This is the exact information-
theoretic meaning of a zero-loss physical channel.

The FIFO problem does not need zero mismatch.  It needs the much weaker
cumulative estimate

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{1\over1-a_i}
   \inf_{J\in\mathcal J_i^{\rm physical}}H_i(J)
 =O(\mathsf A),}
\tag{8.2}
\]

or the local aperture `(CHA)`.  This is now the sharp normalization-free
analytic target.

## 9. Proof boundary

The direct chi-square route unconditionally proves:

1. common numerator/reference transport contracts with its literal mass
   coefficient;
2. the entire nonlinear Bregman remainder reduces to one physical
   mismatch carre \(H_i\);
3. service converts its cumulative price to `GDIR` with exact constants;
4. complete-row blocker conjugation closes the row part if the physical
   response aperture (6.5) is proved; and
5. no arbitrary switch normalization or orbit scalar is required.

The later literal FIFO expansion shows that (6.5) is not the whole native
gate: a balanced current profile can acquire next-state mismatch from a
row kill even when every current switch score is zero.  Thus (6.5) remains
a useful sufficient theorem for the conjugate switch subface, while the
full remaining analytic theorem is:

\[
 \boxed{
 \text{couple the actual next reference motion physically, prove (6.5)
 on the switch-dependent subface, and bound the literal adjoint survivor
 carre (5.2) of the diagonal FIFO update.}}
\]

This is strictly coefficient-faithful and is immune to the scaling
counterexample for an auxiliary private-switch measure.
