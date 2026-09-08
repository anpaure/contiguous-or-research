# Audit of the service-damped Johnson Duhamel reduction

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_SERVICE_DAMPED_JOHNSON_LYAPUNOV_DUHAMEL_REDUCTION_20260806.md`  
**Method:** exact spectral replay and adversarial finite models; no search  
**Verdict:** **PASS AS AN ALGEBRAIC REDUCTION, NOT AS A GDIR PROOF.**
The discount removes the known slow-sector denominator.  It does not prove
the host coefficient rows `(D1)--(D2)`, and same-first-resource switch
stars must be treated as rooted one-entry squares rather than as `FE3`.

## 1. Scalar replay of the Lyapunov equation

On a common eigenspace let `L=theta`, `B=chi`, and
`P=1-theta/X`.  Equation

\[
 r={\chi\over X}+aP^2r
\]

has the unique solution

\[
 r={\chi\over X(1-a(1-\theta/X)^2)}
  ={\chi\over X(1-a)+2a\theta-a\theta^2/X}.
\]

This verifies (1.6), including the final `X` factor.  If `X(1-a)` is
bounded above and below, the denominator is `Theta(1+theta)`.

## 2. Exact Duhamel signs

For `S_P(H)=H-aP^*HP`, subtraction gives

\[
 S_{\widetilde P}(\widetilde R-R)
 ={\widetilde B-B\over X}
 +a(\widetilde P^*R\widetilde P-P^*RP).
\]

Writing `Delta P=widetilde P-P` yields the two linear terms with positive
sign and the positive quadratic term.  Under generator deletion
`widetilde L=L-A`, one has `Delta P=A/X`, so (2.6) has the stated signs.
No continuous-time approximation is used.

## 3. Affine and degree-two obstructions

For a central Johnson layer with `k=Theta(d^2)`,

\[
 \vartheta_1=Theta(d^{-2}),\qquad
 \vartheta_2=Theta(d^{-2}).
\]

The authenticated FIFO examples have
`widehat chi_1=Theta(d)` and, after near-antipodal cancellation of the odd
mode, `widehat chi_2=Theta(d)`.  Therefore

\[
 {\widehat\chi_s\over\vartheta_s}=Theta(d^3),
 \qquad
 {\widehat\chi_s\over\lambda+2a\vartheta_s+o(1)}=Theta(d)
 \quad(s=1,2).
\]

The damped proposal genuinely survives both known counterexamples.
Multiplication by `\beta\le C\varepsilon_P/d^2` leaves
`O(\varepsilon_P/d)`.

## 4. The `K_3` first-kill counterexample is not erased

Take the regular three-state model with `B=L=I` on `1^perp`, and kill the
row whose current coordinate is zero for `f=(0,1,-1)`.  The killed
covariance contribution is zero while the incident switch flux is
positive.  Adding `lambda>0` merely replaces the pristine Green scalar by
a finite positive scalar; it does not change this sign mismatch.

Thus `Delta B/X` and the two linear `Delta P` terms in (2.4) must remain
grouped under the chronological inverse.  Any proof bounding the linear
terms by the killed row pointwise is still false.

## 5. Adapted two-block counterexample

Let the current generator have two regular components and let the actual
vector be constant with opposite signs on the two blocks.  The undamped
current Green operator is singular on this vector.  Service damping makes
the Gramian finite, of size `B_block/lambda`, but if the adapted covariance
projector has eigenvalue `Theta(N)`, the damped cost is still `Theta(N)`.

Therefore damping removes the component singularity but does not turn
equivariance, regular degrees, or the pristine trace into a current-state
bound.  The selected-relation coefficient row remains indispensable.

## 6. Same-anchor off-diagonal obstruction

Two distinct private switches may both become unavailable because their
switched mates hit the same physical resource `x` of the selected blocker.
Their cross term in `A R A` is off-diagonal as a switch-edge term, but it
has only one physical hit.  Sending it to the two-distinct-hit `FE3` ledger
would be a multiplicity error.

The proof-safe partition is:

* one common blocker resource, including different switch edges: rooted
  one-entry/star square (`ROc` or root carré);
* two distinct blocker resources: `FE3`;
* changed slots and owner-parallel resources: their named ledgers.

The theorem source now states this partition explicitly.

## 7. Final scope

The discrete spectrum, trace, edge resistance, Duhamel formula, and frozen
predictable identity pass.  The following implication is **not** proved:

\[
 \text{earliest-blocker geometry alone}
 \Longrightarrow (D1)+(D2).
\]

It additionally needs the actual future/cylinder coefficient and the
rooted same-anchor star normalization.  No known affine, even-sector,
regular-kernel, or occurrence-multiplicity counterexample contradicts the
corrected conditional statement.
