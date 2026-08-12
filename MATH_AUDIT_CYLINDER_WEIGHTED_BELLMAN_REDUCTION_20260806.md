# Audit of the cylinder-weighted Bellman reduction

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_CYLINDER_WEIGHTED_BELLMAN_AND_CONDITIONAL_CLEANUP_REDUCTION_20260806.md`,
source SHA-256
`2f4a53243dbe794b67c3133b992b26ed7eaf4e439377850a2f56175dcd76c8d8`

## 1. Probability identities

For a stopping-prefix event `F`, regard `F` as a terminal event on the full
history tree and put

\[
 h_i^F=\Pr(F\mid\mathcal F_i),\qquad
 W_i^F=\mathbb E[{\bf1}_F\sum_{j\ge i}D_j\mid\mathcal F_i].
\]

Because `D_i` is `F_i`-measurable,

\[
 W_i^F=h_i^FD_i+\mathbb E[W_{i+1}^F\mid\mathcal F_i]
\]

is exact.  After `F` has been decided, `h_i^F=1_F`, so no ambiguity arises
from the event being a prefix rather than a terminal payload event.
Conditional Markov gives a common cleanup threshold from the normalized
bound `W_0^F=O(Pr(F)L)`.

## 2. Hereditary conditioning

If `C` is the common cleanup event and
`Pr(C|F)>=c` for every allowed separator-prefix event, then

\[
 \Pr(B\mid C,F)
 ={\Pr(B\cap C\mid F)\over\Pr(C\mid F)}
 \le c^{-1}\Pr(B\mid F).
\]

Thus conditioning on cleanup inflates every subsequent cylinder upper bound
by only one fixed factor.  It is enough to prove the weighted Bellman row
for the separator-prefix event family; no estimate after every fully
labelled stopped history is needed.

This is the exact scope required by the current Atomic portal-tile packing
lemma, which asks for the unordered cylinder after every separator
exposure.  An initial unconditioned expected-leave estimate alone would
require a redesign of that downstream interface and does not satisfy the
lemma as presently stated.

## 3. Remaining comparison

The existing rooted future-fugacity weights are not proved to equal the
Doob ratios

\[
                 h_{i+1}^F/h_i^F.
\]

They were designed to compensate product survival and first-hit killing;
the true prefix event also records the complete ordered occurrence history.
Therefore one must prove either exact equality or a two-sided comparison
strong enough to retain the scale
`Pr(F)M/d^4`.  Cylinder upper bounds alone give no lower comparison with
`Pr(F)` and cannot be substituted here.

## Verdict

The revised probabilistic and quantifier reduction is **PASS**.  It does
not prove `(JCYL)`.  The exact unresolved host-specific row is a
separator-prefix-weighted selected-relation supersolution together with a
proof that its future weights match or dominate the true survival
martingale at the correct initial normalization.
