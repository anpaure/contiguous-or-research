# Independent audit: localized initial-colex protected Ore closure

**Date:** 2026-08-04  
**Verdict:** **GO**.  No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_LOCALIZED_INITIAL_COLEX_PROTECTED_ORE_COMPLETE_20260804.md`,
SHA-256
`1c1ca29979c511534bfaf3adfa558be5ba9bfec5d6b93dcc33d6e44451e0c96a`.

Author self-audit:
`MATH_AUDIT_LOCALIZED_INITIAL_COLEX_PROTECTED_ORE_COMPLETE_SELF_20260804.md`,
SHA-256
`2f5d9161deeb9aa7d6f8555efa3003cac38dfda271b4e3f6d52b43991e2d10cb`.

The theorem's display typo in (3.8) was repaired before the authoritative
hash above was frozen.  No further correction is required.

## 1. Scope and top-aperture localization

Complementation is a bijection from the initial colex family `F` of
`m`-sets to the lower family `A`, so `|A|=|F|`.  The canonical apertures
satisfy

\[
 \rho_{j+1}-\rho_j=c_{j+1}-c_j-1\ge0,
\]

and hence `r=rho_m` is their maximum.

The top binomial term is

\[
 b_m={m+r-1\choose m}.
\]

If `r>=m/2`, monotonicity in `r` and the uniform entropy estimate give
exponential rate at least

\[
 {3\over2}H_2(1/3)>1.
\]

This contradicts `|F|=O(m^2 2^m)` for sufficiently large `m`, with the
threshold allowed to depend on the implicit constant.  Thus `r<m/2`.

The exceptional endpoint `c_m=2m-1` is correctly separated.  It is the
complete upper shore, violates the localization asymptotically, and its
complement is the complete lower shore, for which both protected loss and
Ore slack are zero.

## 2. Fibre-cap margin and small-family classification

Assume every aperture is at least two.  The nested active-core theorem gives
for each nonempty owner fibre

\[
 2\le a_U\le r+1.
\]

Therefore

\[
 m|A|=\sum_U a_U\le(r+1)|N(A)|.
\]

Because all nonempty fibres have size at least two, the exact protected-Ore
slack reduces to

\[
 \sigma(A)=2(|N(A)|-|A|),
\]

and hence

\[
 \sigma(A)\ge {2(m-r-1)\over r+1}|A|.
\]

For `r<=m/10`, the coefficient tends uniformly to `18`, so the eventual
lower bound `35/2` is valid.  Subtracting
`lambda_P(A)<=15|A|+2m` leaves at least

\[
 {5\over2}|A|-2m.
\]

At `|A|>=2m+1`, this is `3m+5/2>66` eventually.

The residual small-family classification is exact.  A principal star of
aperture at least three has size at least

\[
 {m+2\choose2}>2m.
\]

Two distinct aperture-two star cores are incomparable `(m-2)`-sets, so the
corresponding stars intersect in at most one lower vertex and their union
has size at least `2m+1`.  Thus the only nonempty family below that threshold
is one aperture-two star.  It has `m+1` lower vertices, every active owner
fibre has size two, and its exact slack is

\[
 (m-2)(m+1).
\]

The resulting margin `m^2-18m-17` exceeds `66` for sufficiently large `m`.

## 3. Negative Macaulay credit

For

\[
 g_j=\left({j\over\rho_j}-1\right)b_j,
\]

negativity implies `j<rho_j<=r`.  Therefore

\[
 -g_j
 \le {j+r-1\choose j}.
\]

Summing over every possible negative index deliberately overcounts the
canonical terms and gives

\[
 \sum_{j:g_j<0}(-g_j)
 \le\sum_{j=1}^{r-1}{j+r-1\choose j}
 ={2r-1\choose r-1}-1.
\]

The hockey-stick index and the subtracted `j=0` term are both correct.

## 4. Protected path current and its factor of two

The clause-wise nested-current bound gives

\[
 \lambda_P(A)
 \le 2\sum_t |X_t|N_{\rho^{(t)}}.
\]

Every run aperture is at most `r`, `N_q` is nondecreasing, and the disjoint
run widths contain at most one clause per Macaulay index, so their sum is at
most `m`.  Consequently

\[
 \lambda_P(A)\le2mN_r.
\]

This factor of two is handled correctly in the medium-aperture margin.
Since the exact scalar identity is

\[
 {\sigma(A)\over2}=\sum_j g_j,
\]

one obtains

\[
 \mu_P(A)
 \ge2\left(
 g_m-{2r-1\choose r-1}-mN_r
 \right).
\]

Thus the proof does not mistakenly compare the full protected current to
half the scalar slack.

## 5. Uniform entropy gaps

Writing `alpha=r/m`, uniformly for
`alpha in [1/10,1/2]`, the top credit has exponent

\[
 f(\alpha)
 =(1+\alpha)\log_2(1+\alpha)-\alpha\log_2\alpha.
\]

The trace budget has exponent at most `H_2(alpha)`, since
`H_d=2^{o(m)}` for the frozen `d=O(sqrt m)`, while the complete negative
credit bank has exponent at most `2alpha`.  The first gap is

\[
 f(\alpha)-H_2(\alpha)
 =(1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha),
\]

which is strictly increasing from zero for positive `alpha` and is therefore
uniformly positive on the closed interval.

The function `f(alpha)-2alpha` is concave.  A concave function lies above
the chord between its endpoint values, and both displayed endpoint values
are positive.  Hence this second gap is also uniformly positive.  Uniform
Stirling errors, the multiplier `m`, and all polynomial or subexponential
terms are negligible relative to these fixed exponential gaps.  Lemma 3.2
and the strict `>66` conclusion follow.

## 6. Aperture-one erosion debt

Monotonicity of the aperture sequence makes all `rho_j=1` terms one initial
interval of indices.  For them `c_j=j` and `b_j=1`, so the exact head-tail
erosion contribution is `j-12`.  Its complete negative part is

\[
 \sum_{j=1}^{11}(j-12)=-66.
\]

Any actual tail omits some of these negative terms or adds nonnegative ones.
If the aperture-at-least-two head is nonempty, it remains a canonical
localized colex complement, has the same top aperture, and has strict margin
greater than `66` by one of the preceding two regimes.  It therefore absorbs
the entire tail debt without leaving a sidecar.

## 7. Pure aperture-one union

If every term has aperture one, the constant run has the exact form

\[
 A=\{R\cup\{x\}:x\in X\},
 \qquad |R|=m-2,
 \qquad h=|X|\le m.
\]

Every upper owner contains at most two selected facets.  Hence
`min(2,a_U)=a_U` at every owner, and regularity gives

\[
 \sigma(A)=\sum_Ua_U-2h=mh-2h=h(m-2).
\]

For each selected singleton, the frozen singleton loss is at most ten.
At an owner containing two selected facets, passing from the sum of the two
singleton cuts to their union can create at most one additional unit of
protected loss.  There is exactly one such owner for each unordered pair of
selected pivots.  Therefore

\[
 \lambda_P(A)\le10h+{h\choose2}.
\]

The difference is

\[
 h\left(m-12-{h-1\over2}\right),
\]

which is nonnegative uniformly for `h<=m` once `m>=23`.  This validates the
pure-aperture-one row.

## 8. Exhaustion and scope

The four regimes are exhaustive:

1. all apertures at least two and `r<=m/10`;
2. all apertures at least two and `m/10<=r<m/2`;
3. a nonempty aperture-at-least-two head followed by the aperture-one tail;
4. a pure aperture-one run.

The theorem therefore proves every localized canonical initial-colex cut is
protected-Ore safe.  It does not prove the missing compression statement
that an arbitrary low-expansion violating cut can be replaced by such a
colex cut without reducing protected deficit.

The independent verdict is **GO** at the hashes listed above.
