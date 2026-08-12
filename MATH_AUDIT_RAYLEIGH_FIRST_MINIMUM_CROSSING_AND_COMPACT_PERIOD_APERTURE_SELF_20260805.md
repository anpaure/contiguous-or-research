# Self-audit: first-minimum normalization and compact period aperture

**Date:** 2026-08-05  
**Method:** line-by-line pure-mathematical audit; no computation or solver  
**Object audited:**
`MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`

## 1. Verdict

**PASS after scope restriction.**  The reduction is valid for counting
clocks with finite Rayleigh functional (and, harmlessly, the identically
zero clock with value `+infinity`).  It proves a sufficient compact
all-period aperture and proves that every negative clock yields a negative
finite aperture.  The half-step family correctly proves that this
sufficient aperture is false in general and that the maximum-density Apéry
tail must be retained.  It does **not** prove Apéry-shoulder positivity.

## 2. First crossing exists

If `a_m>0` for some `m`, then

\[
 a_{qm}\ge q a_m\to\infty,
\]

so the first crossing `N` of `zeta` exists.  If no positive term exists,
the clock is identically zero and every term is `K(0)>0`; it cannot be a
negative certificate.  This validates the split made before (1.1).
If the first nonzero value is the cemetery value `infinity`, it is itself
the first crossing; saturation replaces it by a finite endpoint `T`, and
the same monotonic comparison uses `K(infinity)=0`.

## 3. Bellman minorant direction

For every partition `m=sum i_j`, superadditivity gives

\[
 \sum_j a_{i_j}\le a_m.
\]

Therefore `V_m<=a_m`, while the one-part representation gives equality
for `m<=N`.  For `m>=N`, the exact-fill convention must allow a fill of
`m-N`.  It does: denomination one is present, possibly with value zero.
Thus `V_m>=a_N>=zeta`.  Since `K` is increasing after `zeta`, lowering the
clock lowers the functional.  The inequality direction in (1.5) is
correct.

## 4. Endpoint saturation and the strict factor two

Every lower-index partition of `N` can be split into a first positive part
of capacity `j` and the remaining parts of capacity `N-j`.  Their total
value is at most

\[
 a_j+V_{N-j}=a_j+a_{N-j}<2\zeta.
\]

The equalities use `N-j<N`, and strictness uses first crossing.  This works
even when the remaining side has several parts.  Hence `P_N<2zeta` and
`T=max(zeta,P_N)<2zeta`.

Lowering the endpoint to `T` preserves precisely all inequalities ending
at `N`; earlier inequalities do not see it.  It also leaves all capacities
below `N` unchanged.  Both old and new tails stay at least `zeta`, so the
functional direction in (2.6) is correct.

The inertness statement uses an attaining partition.  The maximum in
`P_N` is over finitely many integer partitions of `N`, so attainment is
automatic.

## 5. Residue-tail direction

For `m=qN+r`, Bellman superadditivity gives

\[
 W_m\ge qW_N+W_r=qT+a_r.
\]

When `q>=1`, the lower argument is at least `T>=zeta`; the upper argument
is larger and therefore also on the increasing branch.  Hence

\[
 K(W_m)\ge K(qT+a_r),
\]

not the reverse.  Summation proves that the actual functional is bounded
**below** by the compact period aperture.  Therefore a nonnegative aperture
is sufficient, while a negative actual clock necessarily has a negative
aperture.  No converse realization of an arbitrary aperture prefix is
claimed.

## 6. Endpoint conventions and convergence

Repeated zero positions before `N` cause no problem.  Since `T>0`, the
saturated clock satisfies

\[
 W_m\ge\lfloor m/N\rfloor T,
\]

and every periodized series has a Gaussian tail.  Thus all rearrangements
of the infinite sums are absolutely justified after a finite compact head.

The atom at zero occurs once in the strict counting-clock normalization.
Integer multiplicities at zero correspond to repeated initial positions;
the same proof works verbatim because the first positive crossing remains
finite and the Bellman prefix retains all repetitions.

## 7. Exact nonclaims

The theorem does not prove:

1. `mathcal A_N>=0` for unbounded `N`;
2. that the crude periodic lower train is itself superadditive;
3. that arithmetic grids minimize the aperture;
4. that the maximum-density Apéry shoulder is automatically nonnegative;
5. the fractional configuration gate; or
6. any literal carrier or OR-word upper bound.

The phrase “strictly finite-dimensional for each N” does not mean a
uniform finite-dimensional theorem.  The remaining scalar lemma is still
an all-period statement.

## 8. Audit of the half-step no-go

The sign in (5.2) is strict using only authenticated inequalities:

\[
 K(0)+2K(\zeta)<0.09-0.10<0,
\]

and every omitted tail term is negative.  Absolute convergence gives
continuity of `F_zeta` at the right endpoint, so (5.3) follows.

For `N=2M+1`, two indices from the positive proper block are at least
`M+1` each and therefore sum past `N`.  Hence every internal constraint
contains at most one positive proper value.  This validates (5.4), and the
largest proper partition value at capacity `N` is exactly
`zeta-epsilon`.  The aperture count has `M+1` zero residues and `M` high
residues, so (5.5) is exact.

The family is deliberately **not** asserted to have a negative true
Bellman functional.  Its shorter high-density denomination is precisely
why (3.2) can be a loose lower bound.

## 9. Audit of the corrected Apéry identity

Equation (6.2) is the existing maximum-density residue theorem applied to
the normalized finite table.  It gives equality after the safe conductor
`N(N-1)`, so (6.3) is an identity.  When `U_m<=zeta`, one has
`W_m<=U_m<=zeta`; decreasingness of `K` gives

\[
 K(W_m)-K(U_m)\ge0.
\]

Thus only indices (6.4) can contribute negatively.  No sign is claimed for
those cells, and no descent in `N` is asserted.

## 10. Audit of the zero-margin statement

The measures `rho_h` are scaled counting clocks and hence satisfy every
anchored-window inequality.  Their unit-interval normalization tends to
one.  Continuity and Gaussian integrability of `K` give the right-endpoint
Riemann-sum limit (8.3).  The identity `integral K=0` is the exact equal-work
row of the Rayleigh socket/job measures.  Therefore no estimate of the form

\[
 \int K\,d\rho\ge\epsilon\rho([0,1])
\]

with fixed `epsilon>0` can hold on the complete price cone.

The refinement (8.6) uses the first Euler--Maclaurin/trapezoidal error
formula.  The Rayleigh kernel is continuous and `C^1` at `A`; its second
derivative is integrable on the two sides and has only a finite jump there.
Hence the global trapezoidal error is `O(h^2)`.  Restoring the missing half
of the endpoint atom gives the main term `hK(0)/2`.

Identity (8.7) is the authenticated Poisson formula for reciprocal ceiling
prices.  Its correction is strictly smaller than
`2q exp(-4pi q^2)/(1-exp(-12pi q^2))`, so it is positive for every integer
`q>=1` and tends to `K(0)/2`.  Consequently the scaled comb margin at
`q asymp sqrt(k)` is indeed `Theta(k^(-1/2))`, not exponentially small.
