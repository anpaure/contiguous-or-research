# Self-audit: two-layer footprint gives bounded wedge defect

**Date:** 2026-08-04  
**Method:** symbolic proof replay only; no computation or search  
**Target:**
`MATH_THEOREM_TWO_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`  
**Target SHA-256:**
`42b522abb25158fe06ca54a60b10ad6b3a9b7028e55e640c595d4f385b5befe8`  
**Verdict:** **GO within the stated endpoint-factorized scope.**

## Checks

1. At one source the unordered pair-to-terminal map is injective.  Thus
   the local inactive count is at most ({r_i\choose2}+s_i), with overlap
   only helping.
2. The exact retained-menu threshold is
   (B_{p-1}={m\choose2}-{m-p+1\choose2}); therefore the badness row is
   exactly the weak inequality
   ({r_i\choose2}+s_i\ge T).
3. Two distinct rank-((m-1)) source stars share at most one rank-(m)
   owner.  The owner incidence energy and the root
   (Phi(f,p)) therefore replay exactly.
4. If two sources are at Johnson distance one, their union has rank (m)
   and has (m-1) rank-((m+1)) supersets.  At distance two the union is
   the unique common terminal; at greater distance no common terminal
   exists.  Hence every source pair is counted in at most (m-1) damaged
   terminal clouds.
5. With (J=\sum_i s_i=\sum_Ze_Z), Cauchy--Schwarz gives

   \[
   J^2\le gJ+g(m-1)p(p-1),
   \]

   whose positive root is the displayed (Psi(g,p,m)).  The case (g=0)
   is handled separately and agrees with the formula.
6. For any admissible (R), a bad source with (r_i<R) must have
   (s_i\ge S_R).  Markov counting of the two incidence sums proves the
   union bound (C_R).  Minimizing over (R) is legitimate because every
   fixed (R) gives a complete covering of the bad set.
7. Deleting all bad sources leaves menus strictly larger than the original
   (B_{p-1}), hence larger than the threshold for the smaller retained
   family.  The exact packing/private-direct-routing theorem applies.
8. For (R=\lfloor m/2\rfloor+1), the denominator

   \[
   S_R={m-p+1\choose2}-{\lfloor m/2\rfloor\choose2}
   \]

   is at least (m^2/4) eventually when (p=O(\sqrt m)).  The two
   quadratic-root estimates then give exactly the coarse constant in
   (0.11).
9. The nonadjacent refinement is valid: owner stars are disjoint and
   terminal clouds intersect at most once.  The hidden-hole extension uses
   only (sum_i h_i=H), so its Markov bound is valid without any overlap
   assumption.
10. The protected-factor edge budget is explicitly separated.  No
    occurrence materialization, phase typing, endpoint factorization,
    hidden-resource pricing, or regenerative statement is inferred from
    value-level counting.

## Conclusion

The proof is sound.  The new quantitative gain is real: under the raw
endpoint-factorized interface, owner footprint (O(m)), terminal footprint
(O(m^2)), and (p=O(\sqrt m)) force only (O(1)) bad source menus.  This
does not establish that the current Pascal/common-cap construction has that
interface.
