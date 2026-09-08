# Future-weighted affine insertion Hardy inequality and the potential-cap reduction

**Date:** 2026-08-06  
**Method:** exact future-fugacity drift, killed occupation, and the affine
shared-insertion eigenmode; no computation or search  
**Status:** proof-safe closure of the frozen one-coordinate affine
insertion mode, conditional on one explicit scalar potential cap.  The
`Theta(d^2)` is recovered by the negative future-service drift, not by a
path Poincare inequality.  For the actual adapted vector, the additional
mark-innovation term in Remark 1.2 remains.  This note does not by itself
close that innovation or every higher shared-insertion Hoeffding mode.

## 1. A future-weighted killed occupation lemma

Let `A_i` be a monotonically decreasing finite candidate set.  A live row
`a in A_i` has current coefficient `c_i(a)>=0` and a fixed real mark
`psi(a)`.  If transition `G` were taken without deleting the row, let its
hypothetical next coefficient be

\[
 \widehat c_i(a;G)=c_i(a)R_i(a;G),
 \qquad R_i(a;G)\ge1.
\tag{1.1}
\]

The row actually survives iff `G` misses its literal support.  Put

\[
 \Phi_i=\sum_{a\in A_i}c_i(a)\psi(a)^2.
\tag{1.2}
\]

Assume that there is a deterministic service number `s_i in [0,1]` and a
nonnegative hazard-defect number `e_i(a)` such that, for every live row,

\[
 \mathbb E_i\!\left[
 R_i(a;G){\bf1}_{\{a\text{ survives }G\}}-1
 \right]
 \le -s_i+e_i(a).
\tag{1.3}
\]

### Theorem 1.1 (marked killed-service Hardy inequality)

For every stopping time `tau`, with all quantities killed at `tau`,

\[
 \boxed{
 \mathbb E\sum_{i<\tau}s_i
       \sum_{a\in A_i}c_i(a)\psi(a)^2
 \le
 \Phi_0+
 \mathbb E\sum_{i<\tau}\sum_{a\in A_i}
       c_i(a)e_i(a)\psi(a)^2.}
\tag{1.4}
\]

Consequently, if predictable `b_i>=0` satisfies

\[
 b_i\le\epsilon s_i,
\tag{1.5}
\]

then

\[
 \boxed{
 \mathbb E\sum_{i<\tau}b_i
       \sum_{a\in A_i}c_i(a)\psi(a)^2
 \le\epsilon\Phi_0+\epsilon
 \mathbb E\sum_{i<\tau,a}c_i(a)e_i(a)\psi(a)^2.}
\tag{1.6}
\]

#### Proof

Multiplying `(1.3)` by `c_i(a)psi(a)^2`, summing the live rows, and using
monotonicity gives

\[
 \mathbb E_i(\Phi_{i+1}-\Phi_i)
 \le-s_i\Phi_i+
 \sum_{a\in A_i}c_i(a)e_i(a)\psi(a)^2.
\]

Sum through `tau`, telescope, and discard the nonnegative terminal
potential.  This proves `(1.4)`.  Equation `(1.6)` follows from `(1.5)`.
\(\square\)

No spatial spectral gap appears.  The lemma is a time-direction Hardy
inequality: a marked row may have an arbitrarily slow position profile,
but its future coefficient carries a negative service drift at every
occupied time.

### Remark 1.2 (adapted marks)

If the mark changes predictably from \(\psi_i(a)\) to the hypothetical
next value \(\widehat\psi_i(a;G)\), the same proof gives (1.4) with the
additional right-hand term

\[
 \mathcal I_i^\psi=
 \sum_{a\in A_i}c_i(a)\,
 \mathbb E_i\!\left[
 R_i(a;G)
 \bigl(\widehat\psi_i(a;G)^2-\psi_i(a)^2\bigr)_+
 \right].
\tag{1.7}
\]

This is the usual actual-vector drift/carre-du-champ term.  The killed
occupation argument removes the spatial \(d^2\) loss but does not silently
pay (1.7).

## 2. Exact specialization to the pair future fugacity

For a live pair-potential row `a=(Q,E,F)`, let `c_i(a)` be its summand in
`(FP2)`.  Use the notation `(FP4)`:

\[
 R_i(a)=\rho_i^{-u_N(a)}\rho_{s,i}^{-u_S(a)},
 \qquad
 q_i(a)=1-\rho_i^{u_N(a)+2}\rho_{s,i}^{u_S(a)}.
\]

Let

\[
 \kappa_i(a)={\Lambda_i(E\cup F)\over X(i)}
\]

be its actual next-step kill probability.  The identity

\[
 R_i(a)(1-q_i(a))=\rho_i^2
\tag{2.1}
\]

gives, exactly,

\[
 R_i(a)(1-\kappa_i(a))-1
 =-(1-\rho_i^2)+R_i(a)(q_i(a)-\kappa_i(a)).
\tag{2.2}
\]

Thus Theorem 1.1 applies with

\[
 \boxed{
 s_i=1-\rho_i^2,
 \qquad
 e_i(a)=R_i(a)(q_i(a)-\kappa_i(a))_+.}
\tag{2.3}
\]

This is the marked version of the exact future-overlap drift `(FP5)`.
The error in `(2.3)` is the already isolated hazard defect; no new error
has been introduced.

## 3. The affine insertion mode

Put `n=d-1` and

\[
 \psi(\ell)=B\left(\ell-{n+1\over2}\right),
 \qquad1\le\ell\le n.
\tag{3.1}
\]

For one coordinate-star resource vector, equations `(2.4)--(2.5)` in the
ANOVA note show that the shared-insertion main effect is exactly `(3.1)`.
Moreover the Johnson resolvent acts by a positive scalar on this
sector-one vector.  Hence, on any induced live insertion-order graph,

\[
 \langle P_Ug,\Lambda_U P_UKRf\rangle
 =r_1\langle P_Ug,\Lambda_UP_Ug\rangle\ge0.
\tag{3.2}
\]

The pure affine part of the killed Green residue is therefore at most its
candidate covariance mass:

\[
 \boxed{
 [\mathcal D_U^{\rm aff}(f)]_+
 \le\sum_{a\in U}m_a\psi(\ell(a))^2.}
\tag{3.3}
\]

This inequality includes the cut flux automatically; it is simply the
original definition `B_U-RL_U` before discrete Green summation.  In
particular, one must not bound the interior and cut terms separately.

Since

\[
 \|\psi\|_\infty^2\le C B^2d^2,
\tag{3.4}
\]

Theorem 1.1 recovers the full quadratic path loss whenever the Bellman
prefactor is \(O(d^{-2})\) relative to the service coefficient.  This
statement has a frozen coordinate-star amplitude.  For the adapted
\(f_{T,i}\), add (1.7) and its transpose/noise analogue.

### Theorem 3.1 (affine `(IPH)` from a coefficient ratio)

Fix the coordinate-star vector \(f^{(z)}\) producing the affine mark
\(\psi\) in (3.1).  Suppose, throughout the stopped good interval,

\[
 {\beta_T(i)\over X(i)}\le {C_\beta\over d^2}(1-\rho_i^2),
\tag{3.5}
\]

Then the pure affine shared-insertion contribution satisfies

\[
 \boxed{
 \begin{aligned}
 \mathbb E\sum_{i<\tau}{\beta_T(i)\over X(i)}
       [\mathcal D_{U_i}^{\rm aff}(f^{(z)})]_+
 \le{}&{C\over d^2}\Phi_0\\
 &+{C\over d^2}\mathbb E\sum_{i<\tau,a}
 c_i(a)R_i(a)(q_i(a)-\kappa_i(a))_+
       \psi(\ell(a))^2.
 \end{aligned}}
\tag{3.6}
\]

Consequently

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{\beta_T(i)\over X(i)}
       [\mathcal D_{U_i}^{\rm aff}(f^{(z)})]_+
 \le C\left(\mathcal P_0+\mathbb E\sum_{i<\tau}\mathcal J_i\right).}
\tag{3.7}
\]

where

\[
 \mathcal J_i=\sum_a c_i(a)R_i(a)
       (q_i(a)-\kappa_i(a))_+.
\tag{3.8}
\]

#### Proof

Apply `(1.6)` with \(b_i=\beta_T(i)/X(i)\),
\(\epsilon=C_\beta/d^2\), and use
`(3.3)`.  Then use `(3.4)` in the initial and error terms:

\[
 d^{-2}\Phi_0\le C\sum_ac_0(a)=C\mathcal P_0,
\]

and similarly the marked hazard error is at most \(C\mathcal J_i\).
\(\square\)

This is the desired `Theta(d^2)` recovery.  The adjacent-path Poincare
ratio is `Theta(d^2)`, but it is never used; the same factor comes from the
small Bellman incidence coefficient in `(3.5)` and the future-service
occupation identity.

## 4. Deriving the coefficient ratio from one scalar cap

The remaining condition `(3.5)` has a transparent sufficient form.  Let
`N_T(i)` be the number of live resources in the relevant Johnson layer.
On the good-load interval,

\[
 \sum_{x\in T_i}Y_x(i)\ge c_0N_T(i).
\tag{4.1}
\]

Every composite row has at most `C_0d` occurrences of type `T`.  Since
the incidence coefficient in `(FP9)` is \(c_i(a)R_i(a)\), the definition
`(4.4)` of \(\beta_T\) gives

\[
 \boxed{
 \beta_T(i)\le {C_0d\,\mathcal P_i^+\over c_0N_T(i)},
 \qquad
 \mathcal P_i^+=\sum_a c_i(a)R_i(a).}
\tag{4.2}
\]

On the density bootstrap \(u_N+u_S=O(d)\), while one density step is
exponentially small in \(d\), so \(R_i(a)\le2\) for all sufficiently
large \(d\).  Thus \(\mathcal P_i^+\le2\mathcal P_i\); the finitely
many small values are absorbed into the absolute constant.

Fix a small absolute parameter \(\varepsilon_P>0\) and assume the scalar
potential cap

\[
 \boxed{
 \mathcal P_i\le \varepsilon_P{N_T(i)\over d^3}.}
\tag{PCAP}
\]

Then

\[
 \beta_T(i)\le {C\varepsilon_P\over d^2}.
\tag{4.3}
\]

On the global rate bootstrap,

\[
 X(i)\ge c_X{p_iM\over2d},
 \qquad
 1-\rho_i={2d\over p_iM},
\]

and hence

\[
 {1\over X(i)}\le C_X(1-\rho_i^2).
\tag{4.4}
\]

Equations `(4.3)--(4.4)` prove `(3.5)` with
\(C_\beta=C\varepsilon_P\).  Tracking this constant in Theorem 3.1
gives the sharper form

\[
 \boxed{
 \operatorname {IPH}_{\rm aff}
 \le C\varepsilon_P
 \left(\mathcal P_0+
       \mathbb E\sum_{i<\tau}\mathcal J_i\right).}
\tag{4.5}
\]

This makes the apparent circularity with the hazard-gradient row
absorbable.  More precisely, if the remaining first-order calculation has
the form

\[
 \mathbb E\sum_i\mathcal J_i
 \le A_0+A_1\operatorname {IPH}_{\rm aff}
          +\mathcal R_{\rm other},
\tag{4.6}
\]

where \(A_1\) is absolute, choose
\(C\varepsilon_PA_1\le1/2\).  Substitution in `(4.5)` gives

\[
 \operatorname {IPH}_{\rm aff}
 \le2C\varepsilon_P
   (\mathcal P_0+A_0+\mathcal R_{\rm other}),
\tag{4.7}
\]

and then `(4.6)` closes with no circular term.  Thus `(3.7)` should not be
read as treating \(\mathcal J_i\) as previously controlled; the
small-constant absorption `(4.5)--(4.7)` is the load-bearing conclusion.

The cap `(PCAP)` is at the correct scale.  At the separator density
\(p_*=c/d\), its right side is
\(\varepsilon_PcM/d^4\).  Since
\(\mathcal P_0\le C_0M/d^4\), choosing the separator constant
\(c\ge2C_0/\varepsilon_P\) gives a factor-two initial margin even after
\(\varepsilon_P\) has been chosen small enough for `(4.7)`.  Hence the
small absorption constant is compatible with the scalar bootstrap; no new
inverse power of \(d\) is required.

## 5. What is and is not closed

The theorem proves that the explicit affine position obstruction from the
ANOVA note costs no `d^2` loss.  Under `(PCAP)`, its contribution is bounded
by the initial future potential and the **unweighted** hazard defect already
present in `(FP5)`.  Thus weighting the hazard defect by the square of the
position does not create a new scale.

Three issues remain outside this note.

1. The full shared-insertion Hoeffding main effect for an arbitrary
   resource vector may contain higher position representations, not only
   the sector-one affine mode.  Each such mode needs either the same marked
   occupation argument with a uniform `O(d)` sup bound or a separate
   decomposition.
2. The actual-vector mark innovation (1.7) and its transpose/noise terms
   must be charged by the existing root/pair variation ledger or by an
   additional stopped estimate.  They are not part of the frozen affine
   theorem.
3. `(PCAP)` must be included in, and closed by, the joint stopped
   bootstrap.  The estimate above shows that the affine row itself does
   not obstruct that closure.  It does not independently prove the maximal
   probability of the cap event.

Without a coefficient condition such as `(3.5)`, monotone deletion alone
cannot prove the desired estimate: take no deletions for an arbitrarily
long deterministic interval.  The affine mode then has mass `Theta(d^2)`
while its adjacent Dirichlet energy stays `Theta(1)`.  Thus the
future-service weight is genuinely load-bearing.
