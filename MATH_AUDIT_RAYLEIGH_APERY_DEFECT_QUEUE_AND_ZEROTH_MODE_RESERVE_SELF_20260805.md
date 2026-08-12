# Self-audit: Rayleigh Apéry defect queue and zeroth-mode reserve

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited file:**
`MATH_THEOREM_RAYLEIGH_APERY_DEFECT_QUEUE_AND_ZEROTH_MODE_RESERVE_20260805.md`

**Verdict:** **SELF-GO.**  The least-critical period cap, cyclic averaging,
counting-queue identity, all signs in the signed-tail pairing, shoulder-area
bound, and total-defect spreading replay exactly.  The result is an exact
reduction, not a proof of the centered covariance, all-price positivity, or
a Boolean reserve.

## 1. Period cap

If the least critical index `h` is proper, then `g<=h` and
`P=g lambda<=h lambda=c_h<zeta`.  If `h=N` and saturation chose a proper
partition value `P_N>=zeta`, equality

\[
 \sum_i c_{j_i}=N\lambda=\sum_i j_i\lambda
\]

would force every part to be critical, contradicting least criticality.
Thus the endpoint is exactly `zeta`; with no other critical index,
`g=N` and `P=zeta`.  No inert-endpoint case was overlooked.

## 2. Cyclic averaging

For an exact fill, subtracting its value from `lambda` times its total
capacity gives `sum_j(lambda j-c_j)` with no cocycle term.  Minimizing over
exact fills is `lambda m-V_m`; minimizing over residue walks is `-beta_r`.
This verifies the two shortest-path formulas and identifies the shoulder as
their nonnegative difference.

For a maximizer `a`, cyclic subadditivity gives
`d_a<=d_r+d_(a-r)` for every residue.  The involution/permutation
`r -> a-r` makes the two sums equal, proving
`2 sum d_r>=g Delta`.  Equality is possible already on the group of order
two, so the factor one half cannot be improved from subadditivity alone.

## 3. Queue endpoints and signs

For `m=qg+r`, both `U_m=qP+s_r` and
`lambda m=qP+r lambda` lie in the same period block.  Hence the counting
excess is precisely the sum of half-open displacement intervals and is
periodic.  Endpoint choices are invisible to the absolutely continuous
Rayleigh deviation measure.

With `sigma(dx)=-K'(x)dx`,

\[
 \sigma([u,v))=K(u)-K(v).
\]

Therefore moving an arithmetic point left gives
`K(U_m)-K(lambda m)`, with the positive sign in (4.5).  Similarly the
physical shoulder gives `K(V_m)-K(U_m)`, with the positive sign in (5.3).
Also

\[
 \int_0^P\sum_{q\ge0}-K'(qP+x)dx
 =K(0)-K(\infty)=K(0).
\]

Thus the zeroth-mode term is exactly `M overline(w)`, not its negative.

## 4. Shoulder area

The function `2x exp(-x^2)` has maximum `sqrt(2/e)<1`.  On the compact
branch `K'` is a difference of two values in `[0,sqrt(2/e)]`; on the tail
it is one such value.  Hence `||K'||_infty<1`.  Termwise mean-value bounds
give

\[
 \mathscr S^-\le ||K'||_\infty\sum_m(U_m-V_m).
\]

The strict lower bound on queue area is invoked only when the debt is
positive, so there is no false strict inequality in the zero-shoulder case.

## 5. Total defect

Maximum density gives `e_m>=0`; superadditivity of `V` reverses to
subadditivity of `e`.  Summing the `m-1` split inequalities counts each
proper prefix defect twice.  At level `t`, every split of an active index
has an active half-level endpoint, yielding the exact factor-two prefix
cover.  The count may be infinite below an eventual cyclic defect level;
then the inequality remains valid and is used only as a one-way structural
constraint.

## 6. Scope boundary

The positive mean `M overline(w)` is only the zeroth mode of the formal
phase pairing.  The centered covariance can be negative.  The finite
shoulder area is likewise unsigned after pairing with `-K'`.  Neither
quantity is an occurrence-faithful Boolean socket bank.  The source states
all three limitations explicitly.
