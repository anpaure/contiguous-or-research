# Audit of the explicit PBBS clean-C6 q2/graphic effect

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_PBBS_CLEAN_C6_Q2_NEUTRAL_GRAPHIC_NEUTRAL_20260805.md`  
**Method:** independent symbolic replay; no computation or search  
**Verdict:** **PASS** for `m>=4`.

## 1. Local palettes

From the definitions,

\[
 P_i\cap Q_i=K+a_i=R_i,
 \qquad
 P_i\cap Q_{i+1}=K+a_{i+1}=R_{i+1}.
\]

Also `L_i=P_i-{1}`.  Literal intersections give

\[
 (R_i\cap L_i)_{i=0}^2=(A,B,C),
 \qquad
 (R_{i+1}\cap L_i)_{i=0}^2=(B,C,A).
\]

At `Q_i`, the new edge comes from `P_(i-1)` and
`P_(i-1) cap Q_i=R_i`; hence that endpoint contributes no change.  Every
changed factor edge has one `P` and one `Q` endpoint, so this accounts for
all six affected q2 turns.  The q2 multiset is exactly preserved.

## 2. Two-soliton orbit

The rooted identities

\[
 A_j\mapsto B_j\mapsto A_{j+1},
 \qquad
 A_{m-1}\mapsto A_1
\]

follow by complementing the suffix after the first maximum.  There are
`m-1` A-shapes of displacement `m-1` and `m-2` B-shapes of displacement
`m+1`.  Thus the shape period is `p=2m-3` and its voltage is

\[
 (m-1)^2+(m-2)(m+1)=(m-2)(2m+1)+1.
\]

The literal states are `P_2=(0,A_1)` and `P_1=(0,B_(m-2))`, so they lie
on the same lifted cycle.  Its length `np` is odd, hence `f` and `f^2`
have the same component.  `P_0=(0,1^m0^m)` has the different one-soliton
profile, so exactly two components are touched.

## 3. Full selection replay

For A-shapes, the outgoing rows and block-height triples are

\[
 \{1,\ldots,m-2,m+j\}:
 \begin{cases}
 (m-2,0,0),&j\le m-3,\\
 (m-2,1,0),&j=m-2,
 \end{cases}
\]

and `(m-2,0,1)` at `A_(m-1)`.  The distinguished down-step is `m-1`.

For B-shapes the row is

\[
 \{1,\ldots,m\}\setminus\{j+1\},
\]

with one nonempty block of height `m-2`; its rightmost maximum is followed
by `m+1`.  Since `m-2>1`, every displayed block choice is forced.  Adding
the corresponding down-step and unmatched root zero recovers the current
factor edge.  Coordinate rotation covers every spatial lift.  Therefore
the entire two-soliton component, as well as the known single-soliton
component, has omission count zero.

## 4. Topology and lengths

One full `p`-step f-shape tour raises the root by one.  Since `Q_1` is
`A_1` at root `-1` and `P_2` is `A_1` at root zero,

\[
 g^{p(m+1)}Q_1=P_2,
\]

because `2p(m+1)-p=np`.  Hence the two paths obtained by cutting the
two-soliton cycle have lengths `p(m+1)` and `pm-2`.  The single-soliton
remainder has length `n-1`.  Reconnection by `P_iQ_(i+1)` yields cycles of
lengths

\[
 n+p(m+1)+1,
 \qquad
 pm-1.
\]

Their sum is `n+np`, the total old edge count.  Both inherit only selected
old positions and selected new positions, so both have omission count
zero.  The claimed q2-neutral/graphic-neutral verdict follows.

