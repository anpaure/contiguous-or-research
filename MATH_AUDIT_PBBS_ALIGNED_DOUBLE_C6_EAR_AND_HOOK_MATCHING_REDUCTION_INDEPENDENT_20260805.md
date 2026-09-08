# Independent audit: aligned double-C6 ear and hook-matching reduction

**Date:** 2026-08-05  
**Object audited:**
`MATH_THEOREM_PBBS_ALIGNED_DOUBLE_C6_EAR_AND_HOOK_MATCHING_REDUCTION_20260805.md`  
**Method:** cut-path replay and scheduling-quantifier audit; no search

## 1. Double-ear topology

Cut the two edges `A_i,B_i` on each of three cycles.  With

\[
 X_i:\operatorname{head}(A_i)\leadsto\operatorname{tail}(B_i),
 \qquad
 Y_i:\operatorname{head}(B_i)\leadsto\operatorname{tail}(A_i),
\]

the aligned reconnections trace

\[
 X_0,Y_1,X_2,Y_0,X_1,Y_2,X_0.
\]

All six cut paths occur once.  Reversing both C6 orientations gives the
same conclusion; reversing only one does not.  Theorem 1.1 is therefore
correct, independently of the metric separation between the two cuts on
each old cycle.

## 2. Hyperstar induction

After one double ear, the parent and its first two fresh children form one
cycle.  At every later step the reserved parent edge lies on that one
cycle and the matched child pair consists of two untouched cycles.
Theorem 1.1 again applies to exactly three distinct current cycles.  Thus
arbitrary unmarked parent-component degree is topologically harmless.

This argument requires the two constituent C6s of each ear to be installed
as one atomic disjoint switch.  Sequentially, the first C6 already merges
the three old cycles, but the combined cut permutation is exactly the one
audited in Section 1.

## 3. What rotation proves

The hook-angle theorem gives `2m+1` cyclic translates of one six-owner C6
support.  A fixed support forbids at most `6^2=36` rotations, so `m>=18`
does give two vertex-disjoint **six-owner** lifts on the same component
triple.  Coordinate rotation preserves the canonical C6 orientation, so
they are topologically aligned.

This does **not by itself** prove disjointness of the unchanged companion
q2 halos.  Those halos contain additional physical incidences.  The
palette-transparent and global statements are proof-safe only because
Theorem 4.1 separately assumes global support/halo disjointness in its
hypothesis 2.

## 4. Increasing-`b` scheduling

The scheduling quantifier is sound under the two stated hypotheses.

* At level `b`, every matched child torus is fresh because matchings use
  each child at most once and the level has not yet been processed.
* Its promoted parent lies at level `b-1`, already inside exactly one
  previously constructed one-cycle block.
* Named level-`b` tori are excluded from the matching.  Hence each starts
  a separate descendant block and distinct named roots are not merged
  before the final named-spine operation.
* A named torus may serve as a promoted parent for later children; this
  only enlarges its own block.  It does not join two named-root blocks.

Consequently every double ear meets one existing parent block and two
fresh child cycles, and after all increasing-`b` stages the named-spine
connectors still begin on their intended distinct blocks.  The explicit
port reservation in hypothesis 2 is needed so that installing descendants
does not consume a later named-spine edge or halo.

## 5. Two wording corrections

The mathematical reduction is correct, but two sentences should be read
with the following qualifications.

1. The status line says the hook consequence is conditional only on the
   near-perfect matching.  It is also conditional on Theorem 4.1(2), the
   simultaneous halo-separated physical lift and named-port reservation.
2. Section 3's two rotated copies form an aligned **topological** double
   ear at `m>=18`.  Palette transparency additionally needs their q2 halos
   disjoint; this is not supplied by the six-owner rotation count alone.

Neither issue invalidates Theorem 4.1 because its second hypothesis states
the missing condition explicitly.

## 6. Verdict

**PASS as a conditional reduction**, after retaining both hypotheses:

\[
 \text{near-perfect sibling matchings}
 \quad+\quad
 \text{globally halo-disjoint reserved double lifts}.
\]

No unconditional global hook packing, post-q2 compiler result, or
`B(k)+O(1)` conclusion follows from the theorem alone.

