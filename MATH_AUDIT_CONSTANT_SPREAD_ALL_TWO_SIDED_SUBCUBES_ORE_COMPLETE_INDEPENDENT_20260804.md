# Independent audit: all two-sided Boolean subcubes pass protected Ore

**Date:** 2026-08-04  
**Verdict:** **GO after one harmless uniformity correction.**  The theorem
genuinely proves, for one alternative-random constant-spread reservoir and
all sufficiently large `m`, the protected Ore inequality for every
canonical two-sided subcube `A(C,S)`.  The original use of
`alpha_0=1/12` was infinitesimally too strong after an additive `11/12`
loss; replacing it by `alpha_0=1/13` makes the compactness argument exact.

This audit is independent of the author's self-audit.  No computation,
search, or solver result is used.

## 1. Audited artifacts

| role | file | SHA-256 |
|---|---|---|
| corrected theorem | `MATH_THEOREM_CONSTANT_SPREAD_ALL_TWO_SIDED_SUBCUBES_ORE_COMPLETE_20260804.md` | `c1bcfa900291760974c167c2c02248c65291d28beaf3ef8e66c095a2301f4817` |
| corrected self-audit | `MATH_AUDIT_CONSTANT_SPREAD_ALL_TWO_SIDED_SUBCUBES_ORE_COMPLETE_SELF_20260804.md` | `2e6f9bc1a135da4d01e8c088e934d42db7fc26f7cf1e067b4fcfd9cf4e330b0b` |
| exact two-sided ledger | `MATH_THEOREM_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_20260804.md` | `6499abf7abf9536bdfcf421206ad1e56d3b3f9d2ce05258b92cb8873ddb26dd7` |
| constant-spread reservoir | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |

The pre-correction theorem SHA was
`9bec8eb955e8282bfef4d888a78f6df33bd22cc565ca61872b7feca450295c17`.

## 2. Singleton criterion

For the constant-spread bank every singleton has margin at least

\[
 (m-2)-10=m-12.
\]

At an owner whose selected fibre has size `q>=2`, the exact singleton
block-gluing penalty is at most `q-1`.  If there is no full fibre and
`q<=r_0<m`, then

\[
 q-1\le {r_0-1\over m-r_0}(m-q).
\]

Summing the right side over partial owners gives
`((r_0-1)/(m-r_0))b(A)`.  The exact gluing identity therefore proves
Lemma 1.1.  No independence or average-load assumption is hidden here.

For a two-sided subcube with `c>0`, every nontrivial fibre has size
`rho=m-c<m`, and

\[
 b=c{v\choose\rho},
 \qquad
 {{v\choose\rho}\over{v\choose\rho-1}}
 ={m-u\over\rho}.
\]

Thus the singleton penalty divided by `a=binom(v,rho-1)` is

\[
 {\rho-1\over c}\,c{m-u\over\rho}.
\]

Comparing it with `m-12` and rearranging gives exactly

\[
 u+{m-u\over\rho}\ge12.
\]

Lemma 1.1 and Corollary 1.2 are GO.

## 3. Uniform binomial separation

Write `rho=alpha m`.  For bounded `u`, uniformly on every fixed compact
subinterval of `(0,1]`,

\[
 \log_2{m+\rho-1-u\choose\rho-1}
 =m\bigl((1+\alpha)\log_2(1+\alpha)
          -\alpha\log_2\alpha\bigr)+O(\log m).
\]

For `alpha<=1/2`, the entropy upper bound for `H_rho(m)` leaves exponent

\[
 (1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha)>0.
\]

It has a positive minimum when `alpha>=alpha_0>0`.  For
`alpha>=1/2`, `H_rho(m)<=2^m`, while the binomial exponent is increasing
and at `alpha=1/2` equals `(3/2)H_2(1/3)>1`.  The terms `m` and
`H_d=2^{o(m)}` are negligible.  Lemma 2.1 is GO.

The only correction is its invocation.  From failure of the singleton
criterion,

\[
 \rho>{m-u\over12-u}\ge {m-11\over12}.
\]

This does not literally imply `rho>=m/12`; it implies
`rho>=m/13` for all sufficiently large `m` (indeed for `m>=143`).
The corrected proof uses `alpha_0=1/13`, which is fully sufficient.

## 4. Exhaustive case split

The endpoint `c=0` is a complete-support cut and `u=0` is a principal
up-star.  Both endpoint theorems are proved for the same constant-spread
bank.

Assume `c,u>0`.  If the singleton criterion holds, Corollary 1.2 closes
the cut.  If it fails, then `u<=11` and `rho/m` is bounded below as above.

### 4.1 Case `c<=u`

Both `c` and `u` are bounded by eleven.  Hence

\[
 \rho=m-O(1),\qquad
 a={2m-O(1)\choose m-O(1)}=2^{2m-O(\log m)}.
\]

For `c,u>0`, the exact normalized slack is positive and certainly at
least `2/(m-1)`.  The protected loss is at most the total protected
incidence count `2^{m+o(m)}`.  Therefore

\[
 \lambda_P(A)< {2a\over m-1}\le\sigma(A)
\]

uniformly in this finite parameter range for all sufficiently large `m`.

### 4.2 Case `c>u`

The value `u=11` is impossible: failure would give `rho>m-11`, hence
`c=m-rho<11`, contradicting `c>u`.  Thus `u<=10`.

The corrected exact two-boundary criterion reduces to

\[
 a(c-u)\ge\rho N_\rho,
 \qquad N_\rho=H_\rho(m)+m+H_d.
\]

Uniform separation with `alpha_0=1/13` gives
`a/N_rho=2^{Omega(m)}`.  Since `c-u>=1` and `rho<=m`, the displayed
inequality follows uniformly for all sufficiently large `m`.

The endpoint, singleton, `c<=u`, and `c>u` cases are mutually exhaustive.
No parameter region is omitted.

## 5. Same-reservoir quantifier

All ingredients refer to the single alternative-random constant-spread
reservoir:

1. singleton cap `ell_P<=10`;
2. total incidence size `2^{m+o(m)}`;
3. complete-support endpoint closure;
4. principal-star endpoint closure; and
5. the two-boundary current estimate.

The constrained common-`G_2` bank is not used.  Therefore the theorem is
not a patchwork of incompatible existential choices.

## 6. Exact conclusion and scope

Yes: the corrected theorem genuinely closes **every canonical two-sided
Boolean subcube**

\[
 \{L:C\subseteq L\subseteq S,\ |L|=m-1\}
\]

for one physical reservoir, uniformly for all sufficiently large `m`.

It does not show that every Johnson-connected positive-defect cut is a
two-sided subcube, a union of such subcubes, or close to one.  The remaining
protected-Ore problem is an erosion/classification theorem for arbitrary
partial-colex families.  Component placement, global collar gluing, and
the common cap are also outside this result.

