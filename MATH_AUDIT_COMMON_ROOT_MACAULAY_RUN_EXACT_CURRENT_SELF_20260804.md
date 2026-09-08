# Self-audit: common-root Macaulay runs and exact protected current

**Date:** 2026-08-04  
**Verdict:** **SELF-GO.**  The common-root representation, fibre counts,
binomial slack formula, and protected-current bounds have been rederived
below.  The theorem reduces a saturated run to one explicit current
inequality; it does not prove that inequality in every parameter range.

No computation, search, or solver result is used.

## 1. Audited artifact

`MATH_THEOREM_COMMON_ROOT_MACAULAY_RUN_EXACT_CURRENT_20260804.md`

SHA-256:
`00bd9db3dbfd987c039af4bf796a43b7a4598388a5e8f91a88fde34e6b353bb1`.

This is an author self-audit, not an independent audit.

## 2. Run geometry

Constant `rho_j=rho` forces `c_j=j+rho-1` and consecutive pivots
`p_j=j+rho`.  At index `j`, the higher pivots in the same run remove every
coordinate from `rho+j+1` through `rho+b`, while `[c_j]` removes everything
through `rho+j-1`.  The sole surviving run coordinate is `p_j`; all other
surviving coordinates form one fixed root `R`.  Hence

\[
 C_j=R+\{p_j\}.
\]

The clause union is exactly the lower sets containing `R` and hitting the
pivot set `X`.  Its complement inside the principal star of `R` is the
two-sided interval containing `R` and avoiding `X`.  This verifies all
three identities in Theorem 1.1.

The excluded set `Q_b union [rho+b]` has size `m+rho`, so

\[
 |R|=(2m-1)-(m+\rho)=m-\rho-1.
\]

## 3. Fibre and scalar counts

An owner containing `R` chooses `rho+1` outside coordinates.  With one
chosen point of `X`, the active-core intersection is `R+x` and the fibre
has size `rho`; with at least two, the intersection is `R` and the fibre
has size `rho+1`.  For `rho>=2`, every active fibre is two-covered.

A selected lower set chooses `rho` outside coordinates and must hit `X`;
an active owner chooses `rho+1` and must hit `X`.  This gives (2.3)--(2.5).
Pascal telescoping gives at step `t`

\[
\begin{aligned}
 &\binom{m+\rho-t-1}{\rho}
 -\binom{m+\rho-t-1}{\rho-1}\\
 &\qquad={m-\rho-t\over\rho}
 \binom{m+\rho-t-1}{\rho-1},
\end{aligned}
\]

which verifies (2.6).  Individual summands can be negative; the direct
cardinality difference (2.5) remains the primary nonnegative expression.

## 4. Protected-current identity

At a unique-hit owner, the unselected deletions are exactly `R+x`; at a
multiple-hit owner, they are exactly `R`.  Since every active fibre has
size at least two, protected loss is just the number of protected
unselected deletions.  It splits disjointly into root deletions and
unique-hit coordinate deletions, proving (3.3).

Along one resident owner path, positions containing every coordinate of
`R` form one interval, so at most its two boundary incidences delete a
root coordinate.  Each `x in X` likewise has one occurrence interval and
at most two boundary incidences deleting `x`.  This proves the path bound.

Alternatively, every union-loss incidence is a loss incidence for at
least one active clause `R+x`.  Summing the frozen principal-star bounds
gives `2hN_rho`.  Taking the minimum with the root-path bound proves (3.9).
Since (2.5) is half the scalar slack, (3.10) is exactly the sufficient
protected Ore inequality after dividing both sides by two.

## 5. Uniform broad-run closure

The owner-fibre cap `rho+1` and regularity give

\[
 \sigma\ge {2(m-\rho-1)\over\rho+1}|D|.
\]

For `rho<=m/10`, this coefficient is at least sixteen for large `m`.
With two clauses, the family has size at least `2m+1` at `rho=2`; for
`rho>=3`, one clause already has more than `2m` members.  The frozen
`15|D|+2m` loss estimate therefore closes this range; one clause is the
already closed principal-star endpoint.

For `m/10<=rho<=m/2` and `h<=rho`, all summands in (2.6) are nonnegative.
The first summand has exponent

\[
 (1+\alpha)\log_2(1+\alpha)-\alpha\log_2\alpha,
 \qquad \alpha=\rho/m,
\]

while `N_rho` has exponent at most `H_2(alpha)`.  Their difference is

\[
 (1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha)>0
\]

uniformly on `[1/10,1/2]`.  Thus the first summand alone exceeds
`hN_rho`, proving Theorem 4.1.

Finally, a localized colex segment cannot have top aperture at least
`m/2`: its top binomial term would have exponential rate at least
`(3/2)H_2(1/3)>1`, contradicting `O(m^2 2^m)`.  Apertures are
nondecreasing with the Macaulay index, and a run with `j<=rho` has width at
most `rho`.  This verifies Corollary 4.2, with `rho=1` handled by the
singleton theorem.

## 6. Scope

The theorem proves that constant-aperture runs are common-root star unions,
replaces their exponential inclusion--exclusion description by one root
current and one unique-hit current, and closes every localized intrinsic
broad run.  It still does not control gluing between distinct runs.  The
`rho=1` singleton case is correctly excluded from the two-covered formula.

**SELF-GO** at theorem SHA
`00bd9db3dbfd987c039af4bf796a43b7a4598388a5e8f91a88fde34e6b353bb1`.
