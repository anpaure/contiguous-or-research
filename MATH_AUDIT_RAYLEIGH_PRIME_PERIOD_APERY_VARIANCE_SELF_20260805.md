# Self-audit of prime-period Apéry variance and positivity

**Date:** 2026-08-05  
**Method:** independent additive-combinatorial and majorization replay;
pure mathematics; no computation, search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_PRIME_PERIOD_APERY_VARIANCE_AND_FORMAL_POSITIVITY_20260805.md`  
**Verdict:** **PASS.**  The sublevel sumset inclusion, quantile
subadditivity, prefix-majorization direction, square sum, and final phase
implication all check.  Composite stabilizer induction and finite
shoulders remain explicitly open.

## 1. Quantile subadditivity

If `B_s={r:e_r<=s}`, cyclic subadditivity gives

\[
 B_s+B_t\subseteq B_{s+t}.
\]

The balls at ordered values `q_i,q_j` have sizes at least `i+1,j+1`.
Under Cauchy--Davenport growth, their sum has at least `i+j+1` elements
when `i+j<g`, proving `q_(i+j)<=q_i+q_j`.  The physical bounds
`e_r<=r` put the `j+1` residues `0,...,j` below level `j`, so `q_j<=j`.
Both directions are correct even in the presence of ties.

For prime `g`, Cauchy--Davenport supplies the growth hypothesis.  If a
proper zero exists, the zero set is the whole prime group and the clock
has already collapsed; the ordered argument still applies with all
quantiles zero.

## 2. Prefix ratio and majorization

For `S_n=sum_(j<=n)q_j`, summing

\[
 q_n\le q_j+q_{n-j}
\]

over `j=0,...,n` gives `(n+1)q_n<=2S_n`.  Substitution
`q_n=S_n-S_(n-1)` yields

\[
 (n-1)S_n\le(n+1)S_{n-1},
\]

so `S_n/[n(n+1)]` is nonincreasing for `n>=1`.  Comparing to the terminal
ratio gives

\[
 S_n\ge{\mu n(n+1)\over N}.
\]

The linear sequence `ell_j=2mu j/N` has exactly these prefix sums and the
same total.  Since both vectors are sorted increasingly, larger lower
prefix sums mean that `q` is less spread than `ell`; convex-square
majorization therefore has the direction

\[
 \sum q_j^2\le\sum\ell_j^2.
\]

The square average is

\[
 {4\mu^2\over3}+{2\mu^2\over3N}.
\]

Finally `q_j<=j` gives `mu<=N/2`, so the correction is at most `mu/3`.
Subtracting `mu^2` produces exactly

\[
 \operatorname {Var}(q)\le{\mu(\mu+1)\over3}.
\]

The reference `q_j=j` attains equality.

## 3. Rayleigh implication

Sorting preserves the defect mean and variance.  The independently
audited phase-moment theorem states that precisely this variance inequality
makes the positive Fourier zero mode strictly dominate all nonzero modes
for `P<=zeta`.  Thus every prime true-period formal clock is positive.

## 4. Composite boundary

Kneser's theorem recovers the `|A|+|B|-1` bound whenever the stabilizer of
`A+B` is trivial.  Therefore failure of the proof is genuinely equivalent
to a nontrivial stabilizer in some critical sublevel sumset.  The source
does not claim that quotienting this stabilizer already preserves the
variance inequality; it identifies that coset induction as the next gate.

## 5. Scope

The proof signs the formal periodic phase, not the nonperiodic finite
availability shoulder.  No all-price or Boolean conclusion is inferred.

**Final verdict: PASS.**
