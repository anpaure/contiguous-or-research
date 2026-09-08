# Independent direct audit: finite-shoulder Pareto frontiers and one-defect cocycles

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_APERY_FINITE_SHOULDER_PARETO_FRONTIER_AND_ONE_DEFECT_COCYCLE_20260804.md`  
**Audited source SHA-256:**
`a15aff104c48a7e2fb095a06d00131489e2d9e5f0ea0940fc49d6127ab4b3def`  
**Verdict:** **GO**, subject to the explicit scope at the end.  The theorem
is an exact reduction and does not claim the unresolved Gaussian sign.

This audit rederives the identities directly from the Bellman and
configuration definitions.  No finite search, symbolic solver, or numerical
kernel evaluation is used.

## 1. Seed-cocycle factorization

For `j<=n`, internal superadditivity gives `V_j=c_j`.  Therefore

\[
 e_j=W_j-c_j=W_j-V_j=\Delta_j\ge0.
\]

For every legal last part `j`,

\[
 \begin{aligned}
 \sigma_{m,j}
 &=W_m-W_{m-j}-c_j\\
 &=(W_j-c_j)+(W_m-W_{m-j}-W_j)\\
 &=e_j+\kappa_W(m-j,j).
 \end{aligned}
\]

For a complete configuration `mathbf j` of capacity `m`,

\[
 W_m-\sum_i c_{j_i}
 =\sum_i e_{j_i}+W_m-\sum_iW_{j_i}.
\]

Minimizing this expression is exactly `W_m-V_m=Delta_m`.  This verifies
(1.4)--(1.6).  Nonnegativity of the formal cocycle and of its iterated
version follows from superadditivity of `W`.

## 2. Critical-coordinate bookkeeping

Let `H` be an original critical denomination.  Since `g` divides `H`,

\[
 W_{m+H}=W_m+H\lambda=W_m+L.
\]

For `r_j=[r-j]_H`, the integer

\[
 \ell_{rj}={j-r+r_j\over H}
\]

is nonnegative: if `j<=r`, it is zero after ordinary subtraction; if
`j>r`, it is the positive number of wraps needed to bring `r-j` into the
standard residue interval.  Direct substitution gives

\[
 r+qH-j=r_j+(q-\ell_{rj})H.
\]

Thus `j` is available exactly at `q>=ell_(rj)`.  Its slack is

\[
 W_{r+qH}-W_{r_j+(q-\ell_{rj})H}-c_j
 =x_r-x_{r_j}+\ell_{rj}L-c_j,
\]

which is independent of `q`.  This verifies (2.5)--(2.8).

Two boundary checks remove the possible off-by-one ambiguity:

* for the critical edge `j=H`, one has `r_j=r`, `ell_(rj)=1`, and
  `s_(rj)=0`, giving `delta_(r,q)<=delta_(r,q-1)`;
* for `1<=r<H`, the direct displayed denomination `j=r` has
  `r_j=0`, `ell_(rj)=0`, and `s_(rj)=e_r`.  Hence the active prefix is
  killed at height `t>=e_r`, as required by `delta_(r,0)=e_r`.

Residue zero must be a boundary state rather than another Bellman edge.
Indeed `Delta_(qH)=0` for every `q`, so `N_0(t)=0` for `t>=0`, whereas
the convention `N_0(t)=infinity` for `t<0` correctly means that a slack
larger than the current height imposes no restriction.

## 3. Active-prefix Bellman equation

Fix `r,t,j`.  Under the `j`-edge, all `q<ell_(rj)` survive because the
edge is unavailable.  For `q>=ell_(rj)`, survival means

\[
 \delta_{r_j,q-\ell_{rj}}>t-s_{rj}.
\]

Because every deficit chain is nonincreasing, this is a prefix.  Its
length is

\[
 \ell_{rj}+N_{r_j}(t-s_{rj}),
\]

using the stated infinity convention below height zero.  The minimum in
the deficit recursion exceeds `t` if and only if every candidate exceeds
`t`; intersection of the candidate prefixes therefore takes the minimum
of their lengths.  This independently verifies (2.10).

Since

\[
 N_r(t)=\min\{q:\Delta_{r+qH}\le t\},
\]

the configuration formula from Section 1 gives (2.11) immediately.

If `j` attains the minimum, its right side is finite, so `t>=s_(rj)`.  The
identity

\[
 x_r-t+\ell_{rj}L=x_{r_j}-(t-s_{rj})+c_j
\]

then splits the derivative train after exactly `ell_(rj)` terms.  This
verifies (2.12), including its translated start.

## 4. Shoulder sign convention

The cited layer-cake theorem gives

\[
 \mathcal H(V,W)
 =-\sum_r\int_0^{\Delta_r}
 J_{L,N_r(t)}(x_r-t)\,dt.
\]

Its net debt is `mathfrak S=-mathcal H`.  Since `Delta_0=0` and
`Delta_r=e_r` for `1<=r<H`, equation (3.2) has the correct positive sign:

\[
 \mathfrak S_H(V\mid W)
 =\sum_{r=1}^{H-1}\int_0^{e_r}
 J_{L,N_r(t)}(x_r-t)\,dt.
\]

Therefore `Phi(V)=Phi(W)-mathfrak S`, and (3.3)/(6.1) are exact.  No
termwise sign of `J` is asserted.

## 5. Formal cocycle audit

### Uniform

For `W_m=alpha m`, all linear terms cancel, so both the binary cocycle and
every iterated cocycle are zero.  The path cost is exactly `sum e_(j_i)`.

### Short-first affine

For

\[
 W_m=\alpha m-\beta\lceil m/g\rceil,
\]

one obtains

\[
 \kappa_W(a,b)=\beta\bigl(
 \lceil a/g\rceil+\lceil b/g\rceil-
 \lceil(a+b)/g\rceil\bigr).
\]

The integer in parentheses is one exactly when both residues are positive
and their sum is at most `g`; otherwise it is zero.  For a full
configuration, writing `j_i=q_i g+rho_i` and
`R=sum rho_i`,

\[
 C_-=p_+-\lceil R/g\rceil.
\]

Since `0<R<=p_+(g-1)` when `p_+>0`, this vanishes exactly when
`R>(p_+-1)g`.  This verifies (4.5)--(4.11), including the equality case
`R=(p_+-1)g`, which costs one cocycle quantum.

### Long wrap

For

\[
 W_m=am+\eta\lfloor m/g\rfloor,
\]

one gets

\[
 \kappa_W(a,b)=\eta\bigl(
 \lfloor(a+b)/g\rfloor-\lfloor a/g\rfloor-
 \lfloor b/g\rfloor\bigr).
\]

The integer is one exactly when the two residues sum to at least `g`.
For a full configuration it is `floor(R/g)`, so it vanishes exactly when
`R<g`.  This verifies (4.13)--(4.18).  Since all seed deficits are
nonnegative, the floor budget bounds (4.19) follow in both one-defect
families.

## 6. Defect-spreading audit

Concatenating optimal physical fills gives

\[
 V_{i+j}\ge V_i+V_j.
\]

Using `W_(i+j)=W_i+W_j+kappa_W(i,j)` yields

\[
 \Delta_{i+j}\le\Delta_i+\Delta_j+\kappa_W(i,j).
\]

Summing over all `m-1` nontrivial splits counts every earlier deficit
twice and proves

\[
 (m-1)\Delta_m
 \le2\sum_{i=1}^{m-1}\Delta_i+
 \sum_{i=1}^{m-1}\kappa_W(i,m-i).
\]

The cocycle sum is exactly

\[
 (m-1)W_m-2\sum_{i=1}^{m-1}W_i
\]

and is at most `(m-1)theta`.  Subtracting this bound, and observing that
the remaining right side is nonnegative, justifies the positive-part form
(5.5).  If `Delta_m>t+theta`, every split has
`Delta_i+Delta_(m-i)>t`, and hence at least one side exceeds `t/2`.
Covering the `m-1` split indices by the active set and its reflection gives
`m-1<=2A_(<m)(t/2)<=2A(t/2)`.  This verifies (5.4)--(5.8).

## 7. Scope boundary

The theorem proves all of the following exactly:

1. the full cross-residue recursion for `N_r(t)`;
2. the constrained configuration/Pareto interpretation;
3. the derivative-train decomposition through any attaining edge;
4. the explicit uniform, affine, and long-wrap cocycle budgets; and
5. the cross-height spreading inequalities.

It does **not** prove

\[
 \mathfrak S_H(V\mid W)<\Phi(W).
\]

That missing inequality cannot be inferred merely from translation in
(2.12), because the Rayleigh kernel derivative changes sign.  The audit
therefore approves the file as an unconditional structural theorem and
exact finite-shoulder reduction, not as a positivity closure.
