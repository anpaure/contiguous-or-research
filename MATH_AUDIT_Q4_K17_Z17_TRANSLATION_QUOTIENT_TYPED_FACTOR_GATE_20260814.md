# Hostile audit: the `Z_17` typed-factor quotient reduction is exact

**Date:** 2026-08-14
**Verdict:** PASS as a finite reduction; it contains no feasibility claim.

## 1. Scope audited

Source:

```text
MATH_REDUCTION_Q4_K17_Z17_TRANSLATION_QUOTIENT_TYPED_FACTOR_GATE_20260814.md
SHA-256 4b73ac3d28e72cf24c0a66b37982500fd8809c8c2f811bbb095818ac8f1aec1a
```

Independent replay:

```text
scratch/verify_q4_k17_z17_translation_quotient_typed_factor_gate_20260814.py
SHA-256 d3122e75c5cf3e754a57545ddcc69840b21817a20b4c7795dd4d17e3e09ee4e5

scratch/verify_q4_k17_z17_translation_quotient_typed_factor_gate_20260814.h100.out
SHA-256 b70b8ff6605fd5aff4b5416a9bee8ee8e605d1469189f31b1f7e9b2ad4281b5c
```

## 2. Exact checks

The translation action is free on every nonempty proper subset of
`Z_17`, since 17 is prime.  Thus a quotient-simple rail column develops
one occurrence of a rank-nine orbit into its 17 distinct physical owners.
This proves both directions of the owner exact-cover equivalence, not only
the forward construction.  The scalar count is consequently
`10*143=1430`, giving 2,431 developed rails and all 24,310 rank-nine
owners exactly once.

For a period `N in {10,11}`, direct cyclic intersection and union give

\[
 \bigcap_{t=0}^{j-1}O_{i+t}
   =C\cup\{s_{i+j-1},\ldots,s_{i+3}\},\qquad
 \bigcup_{t=0}^{j-1}O_{i+t}
   =C\cup\{s_i,\ldots,s_{i+j+2}\}
\]

for `1<=j<=4`, including wraparound.  Hence the lower-`q1` exact rows and
upper-`q1` load-`{1,2}` rows develop literally to their physical typed
tickets.  The forced histograms through `q3` follow from the common total
of 1,430 occurrences and the stated orbit counts.  Translation also gives
the claimed point degrees without any additional balancing assumption.

The mixed-period Diophantine faces are exactly

\[
 10a+11b=1430
 \quad\Longleftrightarrow\quad
 (a,b)=(143-11t,10t),\quad0\le t\le13.
\]

The source correctly limits the period-eleven extension to the owner and
typed formulas through `q3`.  It does not transfer the period-ten-only
rank-fifteen coefficient-ten refinement to period eleven.

## 3. Hostile scope boundary

No selected-column certificate is supplied by this reduction.  In
particular it does not prove owner-cover feasibility, simultaneous reserve
placement, chronology, topology, residence, seam compatibility, or the
terminal cap.  Conversely, any quotient certificate satisfying the stated
rows can be expanded and checked without an additional symmetry or
integrality hypothesis.  This is the strongest exact scope supported by
the source and replay.

All replay and hashing for this audit were performed over SSH on H100.  The
local Mac was used only to read and edit files and to use Git.
