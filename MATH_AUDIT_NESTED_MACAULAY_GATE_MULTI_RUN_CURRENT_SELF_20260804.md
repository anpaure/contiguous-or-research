# Self-audit: nested Macaulay gate multi-run current

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_NESTED_MACAULAY_GATE_MULTI_RUN_CURRENT_20260804.md`

This audit is purely deductive.  It uses no finite search or solver output.

## 1. Indexing and canonical correspondence

The theorem indexes maximal Macaulay runs from larger Macaulay indices to
smaller indices.  In that order the apertures strictly decrease and the
roots strictly increase:

\[
 \rho^{(0)} > \rho^{(1)} > \cdots > \rho^{(T)},
 \qquad
 R_0\subset R_1\subset\cdots\subset R_T.
\]

Thus "least active" in the theorem means the same thing as "uppermost
active" in the two-run theorem.  Reversing the run order would replace
least by greatest everywhere but would not change the statement.

The strict-jump relation

\[
 R_t=R_{t-1}\mathbin{\dot\cup}G_t,
 \qquad
 |G_t|=\rho^{(t-1)}-\rho^{(t)}
\]

is exactly the frozen two-run relation.  Its coordinate-interval proof
also makes all gate banks and pivot banks pairwise disjoint from the base
root and from one another.  Hence the abstract hypotheses really hold for
the canonical DNF.

The formal full-shore endpoint `c_m=n` is excluded before this
identification: its pivot is `n+1`, outside the ground set.  Its scalar
contribution is zero and it is handled separately.

## 2. Active-core law

Let `t` be the least active run.

* If its unique active clause is the only active clause globally, its core
  intersection is `R_t+x`.
* If its row has at least two active pivots, their intersection is `R_t`.
* If any later run is active, one later clause has core `R_u+y` with
  `R_t subset R_u`; disjointness gives

\[
 (R_t\cup\{x\})\cap(R_u\cup\{y\})=R_t.
\]

This exhausts the cases and proves the active-core table.  Under the
aperture-at-least-two hypothesis every clause core has size at most `m-2`,
so every nonzero owner fibre has size at least two.  This is exactly the
hypothesis needed to identify protected loss with deletion current in the
active-core intersection.

## 3. Exact current partition

If the least active run is `t`, then

\[
 R_t=R_0\mathbin{\dot\cup}G_1\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}G_t.
\]

Therefore a protected deletion in the active core belongs to exactly one
of the disjoint currents `xi_0,xi_1,...,xi_t`, except that a sole active
clause contributes its unique pivot current `eta_t` as well.  The current
families are disjoint and exhaustive, proving the equality in Theorem 2.1.

For `T=1`, the formula specializes to

\[
 \xi_{R}+\eta_{\rm upper}+\xi_G+\eta_{\rm lower},
\]

which is exactly the frozen strict two-run four-current identity.  This is
an independent consistency check on both the state partition and the run
ordering.

## 4. Path-bound audit

On one resident simple path, the owners containing a fixed root form one
interval.  A deletion from that root can occur on at most its two boundary
incidences.  Likewise each pivot coordinate has one occurrence interval
and at most two deleting boundary incidences.  The least-active and
sole-active restrictions only remove incidences.  Hence

\[
 \xi_i\le2|\mathscr P(R_i)|,
 \qquad
 \eta_t\le2|X_t||\mathscr P(R_t)|.
\]

Summing gives the displayed all-run bound.  No factor proportional to the
number of deeper gates is missing: a gate is charged only while it belongs
to the root of the least active run; once an earlier run is active, the
gate is absent from the common core.

## 5. Disjoint scalar categories

For a rank-`q` set to have least active run `t`, it must:

1. contain `R_t`;
2. avoid `X_0 union ... union X_(t-1)`; and
3. hit `X_t`.

Because those banks are disjoint, the available universe outside `R_t`
has size

\[
 m+\rho_t-H_t,
 \qquad H_t=\sum_{u<t}|X_u|.
\]

Subtracting choices that also avoid `X_t` gives exactly

\[
 \binom{m+\rho_t-H_t}{q-|R_t|}
 -\binom{m+\rho_t-H_t-|X_t|}{q-|R_t|}.
\]

The least-active categories are disjoint and exhaustive.  At ranks `m-1`
and `m`, the lower arguments are respectively `rho_t` and `rho_t+1`, so
their upper-minus-lower sum is precisely equation (4.3).  For `T=1`, this
partition is equivalent to the two-run inclusion--exclusion formula but
uses two disjoint terms rather than three overlapping terms.

## 6. Canonical scalar identity and criterion

Kruskal--Katona for the initial colex segment gives

\[
 |\partial F|=\sum_j\binom{c_j}{j-1},
 \qquad |F|=\sum_j\binom{c_j}{j}.
\]

Since

\[
 \binom{c_j}{j-1}={j\over c_j-j+1}\binom{c_j}{j}
 ={j\over\rho_j}b_j,
\]

equation (4.5) follows.  Combining the exact current with either the
root-path count or the clause-wise principal-current count gives exactly
the two alternatives in (4.6); both sides are half-slack quantities, so no
factor of two is missing.

## 7. Scope and nonclaims

The theorem does **not** prove the scalar criterion (4.6) for every
localized Macaulay profile.  It also does not absorb an aperture-one run;
that case still requires the separate singleton-erosion argument.  What is
closed is the multi-jump algebra: active cores, protected current, and
scalar slack all decompose linearly by the least active run.

## 8. Mechanical document checks

At freeze time:

* display-math delimiter balance is zero;
* `git diff --check` reports no whitespace errors;
* no unpriced computational or empirical premise occurs in the proof.

