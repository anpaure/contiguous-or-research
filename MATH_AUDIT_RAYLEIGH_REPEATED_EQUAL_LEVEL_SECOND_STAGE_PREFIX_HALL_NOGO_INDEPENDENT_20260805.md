# Independent audit: repeated Rayleigh equal-level second-stage prefix-Hall no-go

**Date:** 2026-08-05  
**Method:** independent pure-mathematical reconstruction; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_REPEATED_EQUAL_LEVEL_SECOND_STAGE_PREFIX_HALL_NOGO_20260805.md`  
**Audited source SHA-256:**
`f545f5743a42881dd69d8881d4bf8c5bb16478685361ff965c61402402b87e1f`  
**Verdict:** **GO with no correction.**  The corner inverse asymptotic,
positive new-job density, zero unused-socket density, and prefix-Hall
contradiction are exact.  The no-go applies only to two consecutive
equal-level subtractions; it does not obstruct the one-shot overlap
cancellation followed by a different compact packet coupling.

## 1. First transformed corner

The independently audited one-well theorem gives

\[
 \widetilde K'(b-)=L_-<0,
 \qquad
 \widetilde K'(b+)=L_+>0.
\]

Thus `b` is a genuine corner minimum, not a smooth quadratic minimum.  For
`v downarrow widetilde m`, the one-sided inverse expansions are

\[
 \widetilde\ell(v)
 =b+{v-\widetilde m\over L_-}+o(v-\widetilde m),
\]

and

\[
 \widetilde r(v)
 =b+{v-\widetilde m\over L_+}+o(v-\widetilde m).
\]

The first displacement is negative and the second positive, as required by
their branch locations.

## 2. New-job density

Subtracting the two expansions gives

\[
 \widetilde z(v)
 =(v-\widetilde m)
 \left({1\over L_+}-{1\over L_-}\right)
 +o(v-\widetilde m).
\]

The coefficient is strictly positive.  Its reciprocal is

\[
 {1\over1/L_+-1/L_-}
 ={(-L_-)L_+\over -L_-+L_+}>0.
\]

Since the level base measure is `dv`, this reciprocal is exactly the right
density of the new-job pushforward at zero.  No Jacobian orientation is
missing.

## 3. Unused sockets

The second equal-level rule consumes precisely the left-branch socket bank
`(widetilde b,b)`.  Its unused bank is therefore

\[
 -\widetilde K'(y){\bf1}_{(0,\widetilde b)}dy.
\]

At the origin, `K'(0)=0`.  In the first transform both equal-level endpoint
slopes tend to zero as their endpoints coalesce at the smooth minimum `c`;
their parallel sum `u'(t)` consequently tends to zero.  Hence

\[
 \widetilde K'(0+)=K'(0)+u'(0+)=0.
\]

The unused socket density is continuous from the right with value zero, so
its cumulative mass is `o(t)`.  The theorem does not need a stronger
quadratic asymptotic.

## 4. Prefix Hall

In every finite positive-piece coagulation, a job of size at most `t` has
its chosen first piece at most `t`.  If `kappa` is the first-piece marginal,

\[
 \widehat\nu(0,t]\ge\kappa(0,t]
 \ge\widehat\mu(0,t].
\]

The new-job density gives

\[
 \widehat\mu(0,t]=h_0t+o(t),\qquad h_0>0,
\]

whereas the unused socket bank gives `widehat nu(0,t]=o(t)`.  These are
incompatible for all sufficiently small `t`.  This is a literal Hall
obstruction, not merely a failure of a guessed coupling.

## 5. Scope

The first equal-level reduction and the first transformed overlap
cancellation remain valid.  What fails is appending the equal-level socket
again and asking the *second remainder* to coagulate.  A continuation which
uses the small transformed sockets before creating the corner remainders is
outside the no-go.  In particular, the separately proved one-shot
normalization plus Gaussian-tail removal leaves a compact pair without
performing this forbidden second subtraction.  No original-Rayleigh,
discrete, or OR-word impossibility follows.

