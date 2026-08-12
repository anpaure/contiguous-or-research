# Audit of protected-Ore near-shadow localization

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`  
**Method:** second symbolic derivation of every new identity and explicit
endpoint checks.  No finite search or solver is used.

## 1. Shadow-slack identity

Write `n_j=|{U:a_U=j}|` and `M_2=sum_(j>=2)n_j`.  The three independent
counts are

\[
 |N|=n_1+M_2,
 \qquad
 m|A|=n_1+\sum_{j=2}^m jn_j,
 \qquad
 \sigma=n_1+2M_2-2|A|.
\]

Substitution gives

\[
 (m-1)\sigma-(m-2)(|N|-|A|)
 =\sum_{j=2}^{m-1}(m-j)n_j.
\]

Thus the coefficient `(m-2)/(m-1)`, the remainder `b`, and the equality
condition `a_U in {0,1,m}` are all exact.  The remainder is nonnegative and
vanishes in no other case for `m>=3`.

The divisibility check is

\[
 (m-2)s+b=(m-1)\sigma,
\]

so `b-s` is divisible by `m-1`.

## 2. Equality classification

The local condition is closure of every maximal Johnson clique whenever
two of its vertices are selected.  Starting with one selected `k`-set,
an adjacent selected `k`-set introduces at most one new ground coordinate.
Clique closure and connectivity of `J(S,k-1)` then add every `k`-set on
the enlarged support.  Hence each induced Johnson component is exactly
`{S_i choose k}`.

Two distinct supports cannot meet in `k` points, because the components
would share a vertex, and cannot meet in `k-1` points, because the two
complete layers would contain an adjacent pair.  Conversely, intersection
at most `k-2` prevents any upper clique from meeting two components.
Therefore the classification in Theorem 1.2 is both necessary and
sufficient.

For one component on a support of size `t`, the upper shadow has size

\[
 {t\choose m}+(2m-1-t){t\choose m-1}.
\]

Subtracting its `{t choose m-1}` selected vertices gives the summand in
(1.9).  Distinct component shadows cannot overlap, since two selected
facets of one upper owner are Johnson adjacent.  This verifies the exact
equality-cut shadow formula.

## 3. Protected crossing identity

At an owner with `a=1`, the three possible values `p=0,1,2` contribute

\[
 \begin{array}{c|ccc}
 p&0&1&2\\ \hline
 c_P&0&1&2\\
 \rho_P&0&1&1\\
 c_P-\rho_P&0&0&1
 \end{array}
\]

to the crossing formula, exactly matching the protected loss.  At
`a>=2`, the loss and the crossing count are both `p`.  At `a=0`, the owner
is outside `N(A)` and contributes zero.  This verifies
`lambda=c_P-rho_P` owner by owner.

All protected edges out of `A` end in `N(A)`.  Hence the degree difference

\[
 D_P(N(A))-D_P(A)
\]

cancels the protected edges between `A` and `N(A)` and leaves precisely
the edges between `N(A)` and `mathcal L\setminus A`.  This verifies the
second crossing identity.

Clearing the denominator in `lambda>sigma` gives a strict integer
inequality, hence the `-1` in Theorem 3.1 is necessary and correct.

## 4. Endpoint cuts

The following exact checks agree with every formula.

* `A=emptyset`: `s=b=sigma=lambda=0`.
* `A=mathcal L`: `s=b=sigma=lambda=0`.
* `A={x}`: `s=m-1`, `b=0`, `sigma=m-2`; this is an equality cut.
* `A=mathcal L\setminus{x}`: `s=1`, `b=m`, `sigma=2`.
* If `C=mathcal L\setminus A` has size at most `m-2`, every upper owner
  has at least two neighbours in `A`, so `sigma=2|C|` and
  `lambda<=D_P(C)<=2|C|`.

For `C=mathcal L\setminus A`, the baseline `2d_U/m` sums to `2|C|`.
The only deviations occur at `d_U=m-1` (deficit one) and `d_U=m`
(deficit two), proving the exact `theta(C)` formula.  The protected-loss
rebates at those same rows are respectively `min(p_U,1)` and `p_U`, which
verifies Theorem 5.1.

## 5. Spectral constants

For the Johnson graph `J(2m-1,m-1)`,

\[
 \deg=m(m-1),
 \qquad
 \lambda_2=(m-1)^2-m,
 \qquad
 \deg-\lambda_2=2m-1.
\]

The local ratio check in Lemma 4.1 is

\[
 {h_m(1)\over1(m-1)}={m-2\over m(m-1)},
 \qquad
 {h_m(a)\over a(m-a)}={2\over ma}\quad(2\le a\le m-1).
\]

For `m>=4`, both are at least `2/[m(m-1)]`.  Combining this with the
Johnson Poincare inequality gives

\[
 \sigma\ge {2(2m-1)\over m(m-1)}
 {|A|(W-|A|)\over W}.
\]

Comparing with `sigma<ell_P(A)<=e` yields exactly the constants in
(4.4)--(4.6).  The passage to `t=min{|A|,W-|A|}` uses
`t(W-t)/W>=t/2` and therefore introduces no reversed inequality.

## 6. Scope verdict

The theorem proves an exact reduction, not factor extension.  In
particular, singleton cuts lie in the equality class `b=0`; the known
one-cone obstruction can still concentrate protected loss on such a cut.
No residence, component, common-cap, or balanced-reservoir conclusion is
inferred.

**Audit verdict:** GO, subject to an independent reader checking the
standard Johnson spectral input if it is to be used without citation.
