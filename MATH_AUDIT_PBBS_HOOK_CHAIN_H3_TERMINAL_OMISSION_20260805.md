# Audit: h=3 hook-chain terminal omission

**Date:** 2026-08-05  
**Audited source:**
MATH_THEOREM_PBBS_HOOK_CHAIN_H3_TERMINAL_OMISSION_20260805.md  
**Method:** independent rooted-word replay  
**Verdict:** PASS.

At h=3 the three predecessor shapes are, up to the displayed alternating
tail,

\[
 M_4(10)^b,\qquad
 1^30^2\,10(10)^b0,\qquad
 M_3\,1(10)^b0.
\]

Their first maxima have heights 4,3,3 and their later maxima have heights
at most 1,2,2.  Thus the first zero after the initial one-run is the common
reverse survivor d.  The six q1 rows in the source theorem still have one
nonempty block, of height 3 or 2, against two empty blocks.  No equality is
introduced at the connector itself.

For the near-hook phase,

\[
\phi\bigl(1(10)^b0\,111000\bigr)
 =111000(10)^{b-1}1100.
\]

The first and last primitive factors have heights 3 and 2.  The outgoing
block of the first factor has height 2, exactly tying the last factor.
Choosing the latter block omits the current edge.  The q2 section theorem
allows this tie choice because its protected witnesses use uniquely tallest
blocks.  Hence the terminal donor is genuinely omission-bearing.
