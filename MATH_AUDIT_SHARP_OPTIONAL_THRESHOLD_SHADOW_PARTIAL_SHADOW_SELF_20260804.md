# Self-audit: sharp optional threshold shadow from partial shadows

**Date:** 2026-08-04  
**Artifact audited:**
`MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`  
**Verdict:** **GO**, conditional only on the correctly quoted Chao--Yu
partial-shadow theorem.  The implication from that theorem is elementary
and exact.

## 1. Domain audit

The theorem assumes `mathcal C` is nonempty and every `(k+1)`-set in it
contains at least `D` members of `mathcal A`.  Hence automatically
`D<=k+1`.  Thus

\[
 r=k+1,
 \qquad s=r-D
\]

are legal partial-shadow parameters with `0<=s<=r` and `r-s=D`.

Every `C in mathcal C` has at most `s` missing facets.  No converse,
closure, induced-family, or completeness hypothesis is used.

## 2. Numerical audit

For `M=|mathcal C|>=1`, the equation

\[
                         M=\binom{x}{D}
\]

has a unique real solution `x>=D`.  The cited theorem gives

\[
                         |\mathcal A|\ge\binom{x}{D-1}.
\]

The balance chain is

\[
 \binom{x}{D}=|\mathcal C|
 \ge|\mathcal A|
 \ge\binom{x}{D-1}.
\]

The exact ratio

\[
 {\binom{x}{D}\over\binom{x}{D-1}}
 ={x-D+1\over D}
\]

forces `x>=2D-1`, and monotonicity gives

\[
                         |\mathcal A|
                         \ge\binom{2D-1}{D-1}.
\]

There is no reversal of the partial-shadow inequality and no rounding
step.

## 3. Equality and strictness audit

Equality in the final bound forces equality at every member of the chain,
so `x=2D-1` and

\[
 |\mathcal A|=|\mathcal C|
 =\binom{2D-1}{D-1}.
\]

The Chao--Yu equality theorem then applies directly.  Its fixed redundant
set has size

\[
 s=r-D=k+1-D,
\]

and its variable ranks are `D-1,D`, giving exactly the displayed lifted
middle pair.

Therefore strict side imbalance excludes equality.  Since cardinalities
are integral, it adds at least one to the sharp lower bound.

## 4. Optional-core substitution

The authenticated optional-core hypotheses are

\[
 |Q|\ge|B^-|+1,
 \qquad
 d_{B^-}(U)\ge d-3\quad(U\in Q).
\]

Substituting `D=d-3` gives

\[
 2D-1=2d-7,
 \qquad D-1=d-4,
\]

and hence

\[
 |B^-|\ge\binom{2d-7}{d-4}+1.
\]

The asymptotic identity

\[
 \binom{2D-1}{D-1}
 ={1\over2}\binom{2D}{D}
 \sim {4^D\over2\sqrt{\pi D}}
\]

is correct.

## 5. Scope audit

This proves the formerly conjectural threshold-shadow lower bound.  It
does not contradict any known ambient upper bound on `|B^-|`, so it does
not eliminate the optional core or prove the global OR-word theorem.
The source theorem is deep; this audit does not claim a new elementary
compression proof of Chao--Yu.

