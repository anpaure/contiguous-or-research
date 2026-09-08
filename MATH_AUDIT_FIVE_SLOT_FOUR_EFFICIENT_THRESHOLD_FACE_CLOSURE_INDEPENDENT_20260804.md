# Independent audit: five-slot size-four-efficient threshold-face closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FIVE_SLOT_FOUR_EFFICIENT_THRESHOLD_FACE_CLOSURE_20260804.md`  
**Method:** exact analytic replay only; no search or sampled numerics.

## Verdict

**PASS.**  The active face `T=A` is strictly positive with the claimed
rational margin `199/2310000`.  Only the two inert composite faces remain
after endpoint normalization.

## 1. Parameter replay

Put `u=A-P`.  From `4A/5<=P<A` and `P+x<=A`,

\[
0<u\le A/5,
\qquad x\le u.
\]

If `z>A/2` and `v=A-z`, then `y+z<=A` gives `y<=v<A/2`, while
`z<=3P/4` gives

\[
v\ge A-3P/4=A/4+3u/4\ge A/4.
\]

These are exactly the interval placements used in the proof.

## 2. First reflected pair

The proved critical-point property forces the minimum of `F` on `[0,u]`
to an endpoint, so

\[
F(x)\ge\min(C,F(u)).
\]

Using reflection at `u`, `C>57/1400`, and
`F(u)<1593/22000`, the two cases `F(u)>=C` and `F(u)<C` both imply

\[
C+F(x)+F(A-u)
>
2{57\over1400}-{1593\over22000}-{1\over20000}
={13813\over1540000}>0.
\]

The direction of every inequality is correct.

## 3. Second reflected pair

For `z<=A/2`, both remaining trains are positive.  For `z>A/2`, reflection
at `v=A-z` gives

\[
F(y)+F(z)>F(y)-F(v)-1/20000.
\]

If `y>=A/4`, then `A/4<=y<=v<A/2` and monotone decrease gives
`F(y)>=F(v)`.  If `y<A/4`, the exact rational train bounds give

\[
F(y)-F(v)>1/25-293/6000.
\]

Adding the two reflection errors produces

\[
2{57\over1400}-{1593\over22000}
+{1\over25}-{293\over6000}-{1\over10000}
={199\over2310000}>0.
\]

The rational identity is exact.

## 4. Scope

The endpoint-period Bellman comparison transfers this positive train
margin to the literal Bellman functional, including every finite head
term.  The argument does not address the inert faces `T=P+x` and
`T=y+z`; no broader five-slot or all-slot conclusion is claimed.
