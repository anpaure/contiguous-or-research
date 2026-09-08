# Self-audit: two-sided subcube protected Ore reduction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_20260804.md`

## Verdict

Original self-audit **superseded after independent-scope correction**.
The exact owner, slack, defect, and protected-loss formulas remain GO.
The original path paragraph was too pessimistic about the core current,
and the original endpoint paragraph mixed two alternative reservoir
choices.  See the separate independent audit for the corrected theorem.

## Exact checks

Let `c=|C|`, `u=(2m-1)-|S|`, `r=m-1-c`, and
`v=|S|-c`.  Then:

1. a selected lower vertex is `C` plus an `r`-subset of `S-C`, so its
   count is `binom(v,r)`;
2. an internal owner is `C` plus an `(r+1)`-subset of `S-C` and has exactly
   `r+1=m-c` selected facets;
3. an outside owner has one point outside `S` and exactly one selected
   facet, giving `u binom(v,r)` such owners;
4. therefore
   `S_2=2 binom(v,r+1)+u binom(v,r)` and subtraction of twice the lower
   count gives the displayed `sigma`;
5. `v-r=m-u` and `r+1=m-c`, giving the normalized formula;
6. only internal owners enter the positive clique defect, each with weight
   `c`, proving `b=c binom(v,r+1)`;
7. at an internal owner, an unselected facet is obtained exactly by
   deleting a core coordinate; at an outside owner, loss occurs exactly
   when its unique selected facet is not protected and its protected degree
   is two.  These two disjoint cases prove the protected-loss identity;
8. the formulas specialize to the frozen complete-support and principal
   up-star endpoint formulas.

## Scope guard

The old claim that the support restriction can increase the core-exit
current was false: a core-deleting incidence is still a boundary edge of
the unsplit core-star interval, so every path contributes at most two.
The corrected theorem records this as Lemma 4.1 and derives a quantitative
two-boundary sufficient inequality.  It also uses the single
alternative-random reservoir for both endpoint statements, rather than
mixing that bank with the constrained common-`G_2` bank.
