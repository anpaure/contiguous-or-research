# Algebraic audit: Rayleigh long-wrap continuum duty-cycle dichotomy

**Date:** 2026-08-05  
**Method:** pure mathematics; independent hand replay, no computation,
search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_LONG_WRAP_CONTINUUM_DUTY_CYCLE_DICHOTOMY_20260805.md`  
**Verdict:** **SELF-GO.**  The long-wrap table is a literal primitive Apéry
table, the Riemann normalization and endpoint correction are exact, and the
continuum scalar is the Rayleigh value of an honest nondecreasing
subadditive price.  Its sign remains open.

## 1. Carry and density

For shifts `s_r=r alpha/g`, every no-carry inequality is equality.  Every
carry inequality has the same slack

\[
 P+s_{i+j-g}-s_i-s_j=P-\alpha\ge0.
\]

Proper density is `alpha/g`; endpoint density is `P/g`.  Thus `alpha<P`
is exactly the primitive long-wrap case and `alpha=P` is exactly the
arithmetic boundary.

## 2. Riemann normalization

With mesh `h=alpha/g`, the formal phase sum is the left Riemann sum

\[
 \Phi_g=\sum_{r=0}^{g-1}F_P(rh).
\]

Hence the normalized object is `h Phi_g`, not `Phi_g/g` without the factor
`alpha`.  Summing the variation error over all cells gives

\[
 |h\Phi_g-J_P(\alpha)|
 \le h\operatorname {Var}_{[0,\alpha]}F_P,
\]

which is equivalent to the source's finite error bound.  Converting the
trapezoidal sum to the left sum adds

\[
 {h\over2}(F_P(0)-F_P(\alpha)),
\]

so after division by `h` the endpoint term in (2.4) has the displayed
positive orientation.

## 3. Duty-cycle subadditivity

For residues `r,s`, no carry uses

\[
 \min(r+s,\alpha)\le\min(r,\alpha)+\min(s,\alpha).
\]

For a carry, assume `r<=s`.

* If `r>=alpha`, the right side is `2alpha`, the maximum possible left
  side.
* If `r<alpha<=s`, the carry residue `u=r+s-P` satisfies `u<=r`, so
  `alpha+u<=alpha+r`.
* If `s<alpha`, then `u<alpha` and
  `alpha+u=alpha+r+s-P<=r+s`.

These cases are exhaustive and use only `alpha<=P`.  Therefore the price
is genuinely subadditive, not merely a periodic occupation heuristic.

## 4. Tail-integration identity

The price is absolutely continuous with derivative

\[
 H'(t)={\bf1}_{\{t\bmod P<\alpha\}}
\]

almost everywhere.  Standard tail integration gives

\[
 EH(X)-EH(Y)=\int H'(t)K(t)dt.
\]

Splitting into `P`-blocks gives exactly

\[
 \sum_{q\ge0}\int_{qP}^{qP+\alpha}K(t)dt=J_P(\alpha).
\]

Gaussian absolute convergence justifies the block sum.

## 5. Endpoints

At `alpha=0`, the integral is empty.  At `alpha=P`, the selected blocks
partition the half-line, so `J_P(P)=integral K=0`.  Differentiation gives
`J'_P=F_P`.  Thus

\[
 J'_P(0)=C(P)>c_*,
\]

while

\[
 J'_P(P)=C(P)-M<-c_*
\]

by the independently audited large-socket tail inequality.  The signs are
consistent: the function leaves zero upward at the left endpoint and
returns to zero from above if no interior negative excursion occurs.

At `alpha=P`, the Riemann leading term vanishes and the endpoint correction
is `(F_P(0)-F_P(P))/2=M/2`, agreeing with the Euler--Maclaurin limit of
`C(P/g)`.

## 6. Scope

A negative `J_P(alpha)` would be a real all-price counterexample and would
produce actual negative primitive Apéry clocks, not merely a failed lower
bound.  The theorem finds no such point and proves no nonnegativity.  It
also leaves finite periods near a zero continuum value and general
multi-kink clocks open.
