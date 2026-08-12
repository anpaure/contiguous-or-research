# Audit: soliton-gap forcing and hook-sector cycle count

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_SOLITON_GAP_FORCES_EXPONENTIALLY_MANY_SELECTED_CYCLES_20260805.md`  
**Method:** independent symbolic replay  
**Verdict:** PASS, with the converse correctly left open.

## 1. Local forcing check

For a phase of height `H`, the outgoing criterion gives competing block
heights

\[
                         H-1,quad H_{tail}-1,quad H_{later}.
\]

If two primitive factors have height `H`, peak-profile additivity gives
`a_H>=2`.  If the tail after the first deepest child has height `H-1`,
that child and the tail give `a_(H-1)>=2`.  If a later top-level factor
has height `H-1`, it and the height-`H` factor again give
`a_(H-1)>=2`.  Therefore `lambda_2<=H-2` excludes all three ties and
makes the current block uniquely tallest.  PBBS profile invariance makes
this phase-independent.

Nothing in this argument proves the converse when
`lambda_2>=lambda_1-1`; the source does not claim it.

## 2. Hook arithmetic

For `lambda=(h,1^b)`, `b=m-h`, the vacancy numbers are

\[
 q_1=2h-1,qquad q_2=1.
\]

For `gamma|gcd(b,2h-1)`, direct substitution gives

\[
 F_\gamma=
 \begin{pmatrix}(2m-1)/\gamma&2\\2b/\gamma&2h+1\end{pmatrix},
 \qquad
 \det F_\gamma={(2m+1)(2h-1)\over\gamma}.
\]

Replacing column one by `(1,h)^T` gives determinant one.  The
action--angle translation therefore has order equal to the full torus
size.  Multiplicity is `gamma L_gamma/b`, yielding exactly the sum in the
source.

At `b=1` this gives one cycle.  At `b=2`, the odd vacancy makes
`gcd(b,q)=1`, and

\[
 {1\over2}\binom{q+1}{1}=h=m-2.
\]

For `m=3t,h=t,b=2t`, coprimality is again one and the exact count is

\[
 {1\over2t}\binom{4t-2}{2t-1},
\]

which is exponentially large.  The conclusion that an `O(1)` list of
exceptional PBBS cycles cannot suffice is therefore exact.
