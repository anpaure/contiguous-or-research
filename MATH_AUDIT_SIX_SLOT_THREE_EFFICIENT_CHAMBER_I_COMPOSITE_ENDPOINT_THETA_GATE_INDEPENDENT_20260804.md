# Independent audit: six-slot `h=3` chamber-I composite-endpoint theta gate

**Date:** 2026-08-04  
**Method:** pure algebra and inequalities only; no numerical search or
enumeration.  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_I_COMPOSITE_ENDPOINT_THETA_GATE_20260804.md`  
**Audited source SHA-256:**
`a4b56d4aef91595582cc21e5c4a24a1a3624d37edebaf6fc6386521ae729fad4`

## Verdict

**PASS as an exact reduction.**  The displayed compact gate is derived
correctly and its domain is exactly the chamber-I domain under the stated
change of variables.  The note does not prove the compact gate positive,
and the audit makes no such claim.

## 1. Literal Bellman table

Writing `x=b-a`, the three corrections to
`L_3(p;a,2a)` replace precisely the formal capacity-one, capacity-two,
and capacity-five values.  The resulting first seven Bellman values are

\[
 (0,x,b,p,p+a,p+b,2p).
\]

This is the table `(0,x,b,p,p+a,p+b,2p)`.  Its nontrivial internal
superadditivity inequalities reduce to

\[
 b\ge2x,
 \quad p\ge x+b,
 \quad p+a\ge p+x,
 \quad p+a\ge2b,
 \quad p\ge a+b.
\]

They follow respectively from `b<=2a`, `b<=2a` together with `p>=3a`,
`b<=2a`, and `p>=3a`.  The remaining inequalities are equalities or
weaker repetitions.  Thus the asserted table is internally
superadditive.

Its stabilized residue shifts are indeed `a` and `2a`: in residue one,
`2b-p<=4a-p<=a`, and in residue two, `b<=2a`.  At capacities six,
seven, and eight the stabilized values are already realized by
`2p`, `2p+a`, and `2p+2a`.  Hence there is no omitted availability
correction after capacity five.

## 2. First threshold and endpoint descent

The chamber inequalities give

\[
 x,b<p+b<A,
 \qquad p+a<A,
 \qquad p<A,
\]

while `2p>=A`.  Therefore capacities zero through five are compact and
capacity six is the first threshold point, including the boundary
`2p=A`.

For the Bellman clock `W`, superadditivity gives

\[
 W_{6q+i}\ge qW_6+W_i\ge qA+W_i
 \qquad(q\ge1,\ 0\le i<6).
\]

Both compared arguments are then at least `A`, where `K` is increasing.
At `q=0`, the Bellman values equal the table entries.  Summing by residue
therefore proves exactly

\[
 \mathcal G_{\rm I}\ge\sum_{i=0}^{5}F(W_i).
\]

No strict threshold crossing is used.

## 3. Coordinate domain

With

\[
 a=b-x,\qquad p=A-b-d,
\]

the original inequalities are equivalent to

\[
 0\le x\le b/2,
 \quad d>0,
 \quad b+d\le A/2,
 \quad d+4b-3x\le A.
\]

Indeed:

- `0<=x<=b/2` is exactly `a<=b<=2a` (and implies `a,b>=0`);
- `d>0` is exactly `b<A-p`;
- `b+d<=A/2` is exactly `p>=A/2`;
- `d+4b-3x<=A` is exactly `p>=3a`.

Conversely these inequalities give `p<A` because `b+d>0`, so no source
condition is lost.

The six train arguments become

\[
 0, x, b, A-(d+b), A-(d+x), A-d.
\]

All of `x,b,d,d+x,d+b` lie in `[0,A/2]`.  Applying
`F(w)+F(A-w)=rho(w)` to the last three entries gives exactly

\[
 C+F(x)+F(b)-F(d)-F(d+x)-F(d+b)
 +\rho(d)+\rho(d+x)+\rho(d+b).
\]

Finally, `|rho|<1/20000` makes the phase-free margin `3/20000`
sufficient exactly as stated.

## 4. Scope check

The source proves only

\[
 \mathcal Q_{\rm I}>0\Longrightarrow \mathcal G_{\rm I}>0.
\]

It does not sign `Q_I`, close chamber I, close the `h=3` branch, or make
an all-grid assertion.  The source's scope paragraph is accurate.

