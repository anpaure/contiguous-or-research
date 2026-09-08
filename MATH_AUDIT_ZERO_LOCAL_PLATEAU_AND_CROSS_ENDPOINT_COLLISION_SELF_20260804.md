# Self-audit: zero local plateau and cross-endpoint collisions

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_ZERO_LOCAL_PLATEAU_AND_CROSS_ENDPOINT_COLLISION_NORMAL_FORM_20260804.md`

## Verdict

**PASS** under `r>=2d` and the hypotheses of the two-sided collar theorem.

For a right-endpoint extension whose new left position is `p<=W-2`, the
departure `alpha_p` belongs to `A_p` and is absent from the complete next
owner window, which contains all later positions of the short cell.  At
`p=W-1`, the new envelope has rank at least `r-d>=d`, while the later
singleton suffix has rank at most `d-1`.  For `p>=W`, distinct consecutive
arrival singletons give novelty.  Hence every right chain is strict.

The left-endpoint argument is the time reverse: the arrival at a new right
position `p>=d+1` is absent from the preceding owner window; the initial
departure collar is distinct; and the pivot envelope `E_d` has rank at
least `d`, larger than the preceding collar part.  Hence every left chain
is strict.

The zero-rank-leakage theorem applies to the same cells.  Partitioning all
cells by right endpoint therefore partitions their occurrence multiset
into genuine chains, with target multiplicity equal to the number of
endpoint chains containing it.  This proves

\[
 D=\sum_S(\#\hbox{endpoint chains containing }S-1)_+
   =(\Lambda+\sigma)-|\hbox{support}|.
\]

No claim about the size of this cross-chain collision term is made.
