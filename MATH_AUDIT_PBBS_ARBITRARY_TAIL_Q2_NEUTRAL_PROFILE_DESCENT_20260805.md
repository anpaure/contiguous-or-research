# Audit of the arbitrary-tail q2-neutral PBBS descent

**Date:** 2026-08-05  
**Method:** independent symbolic dependency check; no computation or search

## Verdict

The theorem in
`MATH_THEOREM_PBBS_ARBITRARY_TAIL_Q2_NEUTRAL_PROFILE_DESCENT_20260805.md`
is proof-safe under

\[
                         0\le\operatorname {ht}(E)<t,
 \qquad h\ge t+3.
\]

The check has four independent rows.

1. **PBBS shore.**  Flipping one of the three displayed unmatched zeros
   gives the rooted words in (2.1).  Their dominant heights are
   `h,h,h+1`; all competitors have height at most `t+1`.  The reverse
   survivor is therefore the common first mountain descent `c`, while the
   forward survivor is the remaining unmatched zero.  This proves the
   three old centered edges.

2. **Common pivot.**  A direct first-maximum complement gives the three
   predecessor words (3.1).  Their initial heights are `h+1,h,h`; the
   later height bounds in (3.2) are strict under the displayed hypotheses.
   The reverse survivor is the second mountain descent `d` in every row.
   Hence all companion intersections are `P_i-d`.

3. **Selection and topology.**  Peak-pruning additivity and the wrapper
   identity give exactly the three sibling profiles
   `b+e_(e+1),b+e_(t+1),b+e_(h+1)`.  They are distinct.  Their soliton-gap
   bound is at least two, so the imported forcing theorem selects all six
   occurrences.  Distinct action profiles put the three old edges on
   distinct PBBS components, and a clean C6 merges three cycles into one.

4. **q2 row.**  The exact clean-C6 common-deletion theorem applies with
   pivot `d`.  It fixes the upper q1 colours edgewise and cyclically
   permutes, rather than merely covers, the three affected q2 values.

No statement is made about equal-height tails, angle-torus expansion,
physical disjointness of many gadgets, q3, residence, or the common cap.
Those exclusions are necessary.

