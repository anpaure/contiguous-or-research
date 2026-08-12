# Self-audit: constant trace spread, zero-defect cuts, and principal stars

**Date:** 2026-08-04  
**Status:** author self-audit **GO**, pending independent review.  No search,
solver, or sampled computation was used.

## 1. Audited theorem and dependencies

The audited theorem is

`MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`

with SHA-256

`d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65`.

The frozen inputs used are:

* hybrid clipped-resident reservoir: `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314`;
* common-core upper-damage reservoir: `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983`;
* protected Ore weighted-boundary theorem: `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891`;
* near-shadow localization and equality classification: `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0`.

## 2. Corrections incorporated before this audit

The theorem does **not** retain the earlier common-`G_2` alignment of all
triple paths.  It independently randomizes each triple path.  These are
alternative banks: imposing common `G_2` would give linear singleton load
at the corresponding star.

The deterministic top endpoints are not included in the claimed private
endpoint-spread bound.  The common core lies below all `m` top starts, so a
uniform endpoint bound would be false.  Instead all `2m` top endpoints are
priced additively in every cut.

Earlier draft SHA `a52aeb941772cb93236dbebfd4a39ecbb10dc3584c41d466a102a7fac4350df7`
is superseded and must not be cited.

## 3. Constant-spread check

For an external level `s`, put `B_s={m-1\choose s}`.  The number of lower
vertices on the level is exactly

\[
 {m\choose s}{m-1\choose s}={m\over m-s}B_s^2.
\]

The private paths capable of contributing to one such vertex are indexed
by distinct traces, hence their choices are independent.  Their random
internal-owner mean is at most

\[
 \mu_s={(m-s)(s+1)\over B_s};
\]

the endpoint mean is smaller.  For the low range `2\le s\le m-3`, the
ratio

\[
 {mu_{s+1}\overmu_s}={s+2\over m-s}
\]

shows that the maximum is the common endpoint value `6/(m-1)`.

The threshold-six union sum is exactly bounded by

\[
 \sum_{s=2}^{m-3}
 {m(m-s)^5(e(s+1)/6)^6\over B_s^4}=o(1).
\]

At `s=2,m-3` the terms are respectively `O(m^{-2})` and
`O(m^{-1})`; at the next two levels they are smaller; throughout
`4\le s\le m-5`, `B_s\ge {m-1\choose4}` gives `O(m^{-4})` per term.
Thus every random contribution is at most five simultaneously.

The fixed top bank contributes at most four singleton-loss incidences by
the two cyclic deletion and two cyclic addition candidates.  The own-trace
path contributes at most one.  Hence `l_P(x)\le10`; private endpoint
exposure is at most six and is safely recorded as at most ten.

## 4. Adaptive high-tail check

A monotone Johnson geodesic contributes at most one to each singleton and
private-endpoint load.  Once a vertex reaches ten, forbidding all `m`
owners above it prevents any further contribution.  Summed load is at
most `m` times the selected resource count, so this adds only a polynomial
multiple of `2^m+H_d` forbidden owners.  The hybrid theorem's
`2^{2m-o(m)}` resource denominators still make the forbidden probability
`2^{-m+o(m)}`.  Thus the cap ten is preserved.

## 5. All-cut and equality-cut check

The exact path-forest identity gives

\[
 \lambda_P(A)\le
 \sum_{x\in A}l_P(x)+\frac12
 \sum_{x\in A}e_P^{\rm priv}(x)+2m
 \le15|A|+2m.
\]

No top endpoint is hidden in the half-sum.  Therefore every failed cut has
`\sigma(A)<15|A|+2m`.

For one zero-defect support `A_S={S\choose m-1}`, boundary owners have
exactly one selected facet.  Endpoints cannot cause protected loss there;
loss is exactly the number `\theta_P(S)` of degree-two boundary owners
whose two incidences miss that facet.  Direct counting gives

\[
 \lambda_P(A_S)=\theta_P(S),\qquad
 \sigma(A_S)={u(m-2)\over m}{|S|\choose m-1}.
\]

The cap ten handles all nonconstant codimensions.  For the remaining
`u=O(1)`, total internal-owner count is `2^{m+o(m)}`, while the displayed
slack is `2^{2m-o(m)}`.  Separated equality supports have disjoint upper
shadows, so both sides add.  This validates all `b(A)=0` cuts.

## 6. Principal-star check

For `\mathcal A_C={x:C\subseteq x}`, put `c=|C|` and `r=m-c`.
For `2\le r\le m-1`, protected loss is exactly the number of protected
path edges crossing the owner star.  Each path crosses at most twice,
because every coordinate has one occurrence interval and intersections of
intervals are intervals.

Writing `a=|C\cap K|`, any low fixed-trace path meeting the star has trace
`T\supseteq C\cap E` and `|T|\le m-a`; hence its count is at most

\[
 \sum_{j=0}^{r}{r+a\choose j}
 \le\sum_{j=0}^{r}{m\choose j}=H_r(m).
\]

Adding the `m` top paths and at most `H_d` high paths yields the exact
sufficient bound used in the theorem.  Meanwhile

\[
 |\mathcal A_C|={m+r-1\choose r-1},\qquad
 \sigma(\mathcal A_C)={2c\over m}{m+r-1\choose r}
 ={2c\over r}|\mathcal A_C|.
\]

For `r\le m/10`, the general `15|A|+2m` bound is strictly smaller.  For
`m/10\le r\le m/2`, the ratio between the last binomial and
`{m\choose r}` is `\exp(\Omega(m))`; for `r\ge m/2`, its entropy exponent
is at least `(3/2)H_2(1/3)>1`.  These dominate `H_r(m)+m+H_d` uniformly.

## 7. Scope

The audited theorem proves:

1. a constant-spread protected witness bank;
2. localization of any failed Ore cut to `\sigma(A)<15|A|+2m`;
3. protected Ore closure of every `b(A)=0` cut; and
4. protected Ore closure of every principal up-star.

It does **not** prove the residual path-forest extension, the common cap,
component joining, global residence after collars are glued, or
`\nu(k)\le B(k)+O(1)`.  In particular, no claim is made for arbitrary
compressed, partial-colex, or stability-perturbed families.

