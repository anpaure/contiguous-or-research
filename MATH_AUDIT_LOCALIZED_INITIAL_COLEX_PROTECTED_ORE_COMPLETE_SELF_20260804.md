# Self-audit: localized initial-colex protected Ore closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_LOCALIZED_INITIAL_COLEX_PROTECTED_ORE_COMPLETE_20260804.md`

The audit is purely deductive and uses no computation or search.

## 1. Scope audit

The theorem concerns only lower cuts obtained by complementing initial
colex segments and satisfying the frozen small-side bound

\[
 |F|=O(m^2 2^m).
\]

It does not claim a protected compression theorem for arbitrary cuts.  The
full-shore endpoint is correctly separated: `c_m=2m-1` exhausts the whole
upper shore, has no literal pivot, violates the small-side hypothesis
asymptotically, and is trivially safe independently.

## 2. Aperture monotonicity and localization

Since the canonical upper entries are strictly increasing integers,

\[
 c_{j+1}\ge c_j+1,
\]

and hence `rho_(j+1)>=rho_j`.  Thus `r=rho_m` is indeed the maximum
aperture.

The top binomial term is

\[
 b_m=\binom{m+r-1}{m}.
\]

At `r=m/2` its exponential rate is
`(3/2)H_2(1/3)>1`, and the rate only increases with `r`.  Therefore
`r<m/2` follows uniformly from the rate-one localization.

## 3. Fibre-cap slack

With every aperture at least two, the nested active-core theorem gives

\[
 2\le a_U\le r+1
\]

for every active owner.  The regular incidence identity

\[
 m|A|=\sum_U a_U
\]

therefore implies `|N(A)|>=m|A|/(r+1)`.  Since every active fibre is
two-covered,

\[
 \sigma(A)=2(|N(A)|-|A|),
\]

which gives equation (2.2).  No truncated-fibre correction is omitted.

For `r<=m/10`, its coefficient tends uniformly to 18; choosing the
eventual bound `35/2` is valid.  Combining it with
`lambda<=15|A|+2m` gives the claimed strict margin whenever
`|A|>=2m+1`.

If a canonical DNF has size below `2m+1`, an aperture-three clause is
already too large.  An aperture-two clause has size `m+1`; two distinct
such stars intersect in at most one lower vertex because their distinct
incomparable `(m-2)`-cores have union of size at least `m-1`.  Their union
therefore has size at least `2m+1`.  The only nonempty residual case is one
aperture-two principal star.  Its exact slack is

\[
 {2(m-2)\over2}(m+1)=(m-2)(m+1),
\]

so its displayed quadratic margin is correct.

## 4. Negative-credit sum

A negative Macaulay term has `j<rho_j<=r`.  Its magnitude is bounded by

\[
 \binom{j+\rho_j-1}{j}
 \le\binom{j+r-1}{j}.
\]

Summing all possible indices and applying the hockey-stick identity yields

\[
 \sum_{j=1}^{r-1}\binom{j+r-1}{j}
 =\binom{2r-1}{r-1}-1.
\]

This deliberately overcounts missing canonical terms, so it is a valid
uniform upper bound.

## 5. Protected-current budget

The clause-wise branch of the nested multi-run current theorem gives

\[
 \lambda_P(A)\le2\sum_t h_tN_{\rho^{(t)}}.
\]

The trace counts are monotone in their rank argument, every run aperture
is at most `r`, and the disjoint run widths sum to at most `m`.  Hence the
budget `2mN_r` is correct.  The proof never sums a root-boundary current
once per clause; using the clause-wise branch here is merely the simpler
of two already certified bounds.

## 6. Entropy-gap audit

For `alpha=r/m in [1/10,1/2]`, the top credit has rate

\[
 f(\alpha)
 =(1+\alpha)\log_2(1+\alpha)-\alpha\log_2\alpha.
\]

The protected trace budget has rate at most `H_2(alpha)`, and the entire
negative-credit bank has rate at most `2alpha`.  The first gap is

\[
 f(\alpha)-H_2(\alpha)
 =(1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha).
\]

It vanishes only at zero and is therefore uniformly positive on the
closed interval used here.

For the second gap, `f(alpha)-2alpha` is concave.  A concave function on an
interval is bounded below by the smaller endpoint value, and both endpoint
values displayed in (3.14) are positive.  Hence both gaps have one fixed
positive minimum.  Polynomial factors, the `m` multiplier, and the
subexponential `H_d` term cannot close either gap.  This validates the
uniform, not merely pointwise, conclusion in Lemma 3.2.

The scalar identity supplies `sigma/2=sum g_j`; after subtracting every
possible negative term, the remaining top credit exceeds `mN_r` by an
exponential amount.  Since `lambda<=2mN_r`, the strict margin in Corollary
3.3 has the correct factor of two.

## 7. Aperture-one tail

Monotonicity makes all `rho_j=1` terms one initial interval.  There
`c_j=j`, `b_j=1`, so the head--tail erosion contribution is exactly
`sum(j-12)`.  Its negative part over all positive indices is

\[
 -11-10-\cdots-1=-66.
\]

Every nonempty aperture-at-least-two head is itself a canonical localized
initial-colex complement and has margin greater than 66 by the preceding
two cases.  Thus the erosion debt is genuinely absorbed, not merely
bounded as a terminal sidecar.

If there is no head, the aperture-one DNF is one common-root family of `h`
singletons.  An owner contains at most two of them, so

\[
 \sigma=h(m-2).
\]

The exact path-forest identity bounds its loss by the sum of the singleton
losses plus at most one endpoint term for each of the `binom(h,2)` double
owners.  This proves `lambda<=10h+binom(h,2)`.  Since `h<=m`, the final
inequality is nonnegative for all sufficiently large `m`.

## 8. Exhaustion and mechanical checks

The proof partitions the canonical possibilities into:

1. all apertures at least two, with `r<=m/10`;
2. all apertures at least two, with `m/10<=r<m/2`;
3. an aperture-one tail with a nonempty head; and
4. a pure aperture-one run.

These cases are exhaustive.  At freeze time, display-math delimiter
balance is zero and `git diff --check` reports no whitespace errors.

