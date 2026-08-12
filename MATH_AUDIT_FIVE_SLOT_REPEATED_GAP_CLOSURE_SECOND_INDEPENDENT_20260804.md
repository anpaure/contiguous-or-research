# Second independent audit of the proposed five-slot repeated-gap closure

**Date:** 2026-08-04  
**Verdict:** **FAIL — retraction confirmed.**  The proposed positivity
closure contains one fatal reversal of the no-interior-minimum implication.
The valid preliminary lemmas do not repair that reversal.

## Exact bindings

The originally submitted positivity claim had SHA-256

`510f45f174dad000848d5eee421a0d6087b2c2aa455818531ba63a53f54f4558`.

It is now marked `RETRACTED — DO NOT CITE` at

`MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_REPEATED_GAP_COMPLETE_CLOSURE_20260804.md`

with final SHA-256

`a80155e51bb5d4b64dc9af1557ccd6e1db10c15e5cb401f63f5286c3b3eca417`.

The first independent retraction audit is

`MATH_AUDIT_FIVE_SLOT_REPEATED_GAP_COMPLETE_CLOSURE_RETRACTION_20260804.md`

with SHA-256

`bef93e4b052021bf651ebdb17bdce1a9c4ccf0dc0a61bea12a2ea51876dabed7`.

This second audit independently reaches the same conclusion.

## Valid pieces

The composite-endpoint descent is correct.  If a superadditive clock has

\[
 V_0,\ldots,V_4<A<V_5=E,
\]

then superadditivity gives `V_(5q+i) >= qE+V_i`.  For `q>=1` both sides
are in the interval where `K` is increasing, and hence

\[
 \sum_mK(V_m)\ge\sum_{i=0}^4F_E(V_i)
                 \ge\sum_{i=0}^4F_A(V_i).
\]

The first six values and domains are also exact:

\[
\begin{array}{c|cccccc}
\mathcal R&0&a&y&a+2\beta&2y&3y-a\\
\mathcal P&0&a&2a&p&p+a&p+2a,
\end{array}
\qquad y=a+\beta.
\]

The stated domains put precisely the first five values below `A` and the
sixth above `A`; `a<=beta` and `p>3a` give the required superadditivity.

The extension

\[
 F_A(v)<64/1000\qquad(0\le v\le A/2)
\]

is valid.  The half-train completion is exact, the theta lower bound is
`Theta(t)>=2-epsilon`, the two leading Gaussian terms retain their maximum
on the already-isolated critical interval, and the remaining tail is less
than `(1/125)/(1-1/100)<1/120`.  Thus

\[
 F_A(At)<11/200+1/120+1/20000=3803/60000<64/1000.
\]

The reflected-train substitutions and the final rational arithmetic would
also be correct **if** the missing forward-difference estimates were
available.

## Fatal implication reversal

If every interior critical point of `F_A` on `[0,A/2]` is a strict local
maximum, then the minimum on `[0,v]` occurs at an endpoint.  Therefore the
valid statement is

\[
 \boxed{F_A(u)\ge\min\{C(A),F_A(v)\}}
 \qquad(0\le u\le v\le A/2).
\]

The proposed closure instead uses

\[
 F_A(v)\ge\min\{C(A),F_A(u)\},
\]

which reverses the endpoint and the interior point.  The critical-point
property does not imply this: a decreasing interval has no interior
minimum and is a direct abstract counterexample to the implication.

Consequently the short-singleton estimate

\[
 F_A(y)-F_A(u)>C(A)-64/1000
\]

for `u<y`, and both long-singleton estimates

\[
 F_A(2a)-F_A(u)>C(A)-64/1000,
 \qquad
 F_A(a)-F_A(v)>C(A)-64/1000
\]

for `v<a<u<2a`, are unsupported.  These are exactly the extra
`C(A)>43/1000` contributions needed for the claimed `9/10000` margins.
Deleting them destroys both positivity proofs.

## Consequence

The previously audited conditional reduction remains valid:

`MATH_THEOREM_FIVE_SLOT_COMPLETE_TWO_REPEATED_GAP_REDUCTION_20260804.md`

SHA-256

`b7763d92d857ce811de7a0b2a9cc8e3b283e2f141536be9c3d176c47388708a6`,

with independent audit SHA-256

`43cfe0ebc5311bf956b2346dd84025db77cea023c49ec3ee159274fe4b6c15b9`.

It says that the two inequalities `R>0` and `P>0` would close the last
five-slot branch.  The retracted note proves neither inequality.  Hence
one may **not** conclude that every Bellman table with grid size at most
five is positive.  The size-two, size-four, and size-five branches are
closed; the two pulse-free size-three gates remain open.
