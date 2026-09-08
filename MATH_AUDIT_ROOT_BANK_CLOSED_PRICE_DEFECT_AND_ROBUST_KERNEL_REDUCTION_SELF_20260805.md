# Self-audit: root-bank closed-price and robust-kernel reduction

**Date:** 2026-08-05  
**Method:** pure mathematical audit; no computation or solver  
**Audited source:**
`MATH_THEOREM_ROOT_BANK_CLOSED_PRICE_DEFECT_AND_ROBUST_KERNEL_REDUCTION_20260805.md`

## 1. Verdict

**PASS with the stated socket-admissibility qualification.**  The closure
argument, exact bank opportunity cost, workload-defect transform, and
perturbed-kernel equivalence are valid.  The result does not derive the
perturbed inequality from the Apéry dichotomy.

## 2. Closure and physical qualification

For an exact fragmentation price, concatenation gives subadditivity and
trimming gives monotonicity.  Replacing each physical part price by the
configuration minimum at that part length is idempotent: every new
fragmentation can be expanded into old fragmentations, and an old optimum
is available in the new menu.

The replacement lowers the price of every exact physical capacity, but
need not lower the dot product with an arbitrary coordinatewise
nonnegative tail.  Therefore the source correctly assumes that the bank
tail can be removed at the exact-capacity level, so the residual tail is
the conjugate of a nonnegative physical histogram.  Without this premise,
testing only closed prices would not be justified.

## 3. Opportunity formula

At a closed price `f`, the one-part state `u^(j)` costs the job minimum
`f(j)`.  The state `v^(j)=(j-1,1)` costs `f(j-1)+f(1)`.  Hence

\[
 \Pi_G=\sum_{j=2}^DR_j\bigl(f(j-1)+f(1)-f(j)\bigr).
\]

No factor two is missing: only the `v` copy in each two-state pair pays
opportunity cost.

## 4. Workload-defect algebra

The function

\[
 g(q)=qf(1)-f(q)
\]

is nonnegative by repeated subadditivity, nondecreasing by the one-step
subadditivity inequality, and superadditive by subadditivity of `f`.
Moreover

\[
 \Delta g(q)=f(q-1)+f(1)-f(q).
\]

Exact work balance gives `sum_q Q_q=0`, so summation by parts yields

\[
 S=-\sum_qQ_q\Delta g(q).
\]

Subtracting the bank opportunity gives exactly

\[
 S-\Pi_G=-\sum_q(Q_q+R_q^*)\Delta g(q).
\]

The reverse-window inequality for `Delta g` is just
`g(x+t)-g(x)>=g(t)`.  Thus the robust-kernel formulation has precisely
the asserted cone and sign.

## 5. Zero face and counterexample

If every `R_j` is positive, all nonnegative summands in `Pi_G` vanish
exactly when `Delta g(j)=0` for `2<=j<=D`, i.e. when the closed price is
workload-linear on the physical range.

The finite counterexample is exact.  Two capacity-two plus two
capacity-one sockets have tail `(4,2)`.  The root pair `(2)` and `(1,1)`
has tail `(3,1)`, leaving the physical tail `(1,1)` of one capacity-two
socket.  Two residual singleton jobs cannot both occupy that one socket.
At the closed price `f(1)=f(2)=1`, complete slack is zero and bank cost is
one.  Hence bare all-price feasibility does not imply the fixed bank.

## 6. Apéry scope

The near-arithmetic conclusion is explicitly conditional on the finite
normalization `S/W=Phi(V)+o(1)`.  Under that premise, the displayed
small-displacement and small-shoulder bounds leave a fixed positive
continuum margin, which dominates a polynomial bank.

The converse defect branches are not reserve theorems.  Large
displacement only invalidates the BV lower bound, while adverse shoulder
debt subtracts from the formal margin.  A proof for those branches must
establish the new perturbed inequality; it cannot be inferred from the
existing dichotomy.

## 7. Exact nonclaims

The audited theorem does not prove unperturbed all-price positivity, the
root-bank robust inequality, adjacent-depth or same-depth named Hall,
physical occurrence selection, boundary realization, protected
serialization, `B(k)+O(1)`, or coefficient zero.
