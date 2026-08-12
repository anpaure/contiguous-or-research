# Independent audit of the PBBS rigid-soliton q2-transparent C6 escape

**Date:** 2026-08-05  
**Audited theorem (same displayed gadget, proof-safe `m>=4` version):**
`MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md`  
**Method:** direct cyclic parenthesis matching and set algebra; no finite
search or computation

## 0. Verdict

The displayed clean `C6` and its q1/q2-transparency proof are correct for

\[
                              m\ge 4.
\]

In that range all three old edges are literal PBBS `g=f^2` edges, all six
q1 occurrences used in the q2 comparison are selected by the max-height
rule, and the three changed q2 colours rotate exactly as claimed.

The asserted extension to `m=3` is **false**.  At `m=3` the second inverse
neighbour is

\[
 B_1=\{1,4,5\},\qquad L_1=P_1\cap B_1=\{1,4\}=R_2,
\]

not the specialization `B_1={3,4,5}`, `L_1={3,4}` of the displayed
formula.  Thus the old switch edge `P_2Q_2` and the alleged companion edge
`B_1P_1` are two occurrences of the same q1 colour `R_2`; a one-occurrence
section cannot select both.  Under either max-height tie choice the local
q2 multiset changes.  The theorem and its status line should therefore be
restricted to `m>=4`, with `m=3` removed or handled by a different gadget.

The exact topological effect is also determined below.  If the other two
old edges lie on distinct PBBS factor cycles, the trade merges the three
input cycles into one.  If they lie on one common cycle, the trade replaces
the rigid cycle plus that cycle by two output cycles: one contains the
entire opened rigid path, while the other is the complementary path of the
second cycle closed by one new edge.  Thus the component count changes by
`-2` or `0`, respectively.

## 1. The three forward PBBS calculations

Use positions `0,1,...,2m` and put

\[
K=\{1,\ldots,m-2\},\quad
(a_0,a_1,a_2)=(m-1,m,m+1),\quad c=0.
\]

Then

\[
\begin{array}{lll}
P_0=\{1,\ldots,m\},
&&Q_0=\{0,\ldots,m-1\},\\
P_1=K\cup\{m,m+1\},
&&Q_1=K\cup\{m,0\},\\
P_2=K\cup\{m-1,m+1\},
&&Q_2=K\cup\{m+1,0\}.
\end{array}
\]

For each `P_i`, forward cyclic cancellation leaves `0`.  Hence

\[
\begin{aligned}
 f(P_0)&=\{m+1,\ldots,2m\},\\
 f(P_1)&=\{m-1,m+2,\ldots,2m\},\\
 f(P_2)&=\{m,m+2,\ldots,2m\}.
\end{aligned}
\]

Rooting these three words at the next forward survivor gives respectively

\[
0_m1^m0^m,
\qquad
0_{m+1}1^{m-1}0^{m-1}10,
\qquad
0_{m-1}10\,1^{m-1}0^{m-1}.
\]

Their survivors are `m`, `m+1`, and `m-1`, so

\[
                              f^2(P_i)=Q_i
\]

for all three indices.  This part of the attacked proof is correct, also
at `m=3`.

## 2. The three old max-height occurrences

The old q1 rows are

\[
R_0=\{1,\ldots,m-1\},\quad
R_1=K\cup\{m\},\quad
R_2=K\cup\{m+1\}.
\]

Their relevant deficit-three blocks are

\[
\begin{aligned}
R_0:&\quad 1^{m-1}0^{m-1},\\
R_1:&\quad 1^{m-2}0\,1\,0^{m-2},\\
R_2:&\quad 1^{m-2}00\,1\,0^{m-3}.
\end{aligned}
\]

For `m>=4`, these choose respectively the pairs of added coordinates

\[
(0,m),\qquad(0,m+1),\qquad(0,m-1),
\]

and therefore select `P_iQ_i` for `i=0,1,2`.  The third block has unique
maximum `m-2`, immediately followed by the down-step `m-1`.

At `m=3`, the third displayed string is not itself one Dyck block.  The
actual decomposition of `R_2={1,4}` is

\[
0_0(10)\,0_3(10)\,0_6,
\]

and choosing the first height-one block does select `P_2Q_2`.  Thus the
attacked note's old-edge tie choice is legitimate; the failure at `m=3`
occurs in the companion calculation, not here.

## 3. Reverse neighbours and the exact boundary failure

For `m>=4`, reverse cancellation gives first survivors

\[
r_-(P_0)=m+1,qquad r_-(P_1)=m+2,qquad r_-(P_2)=m+2.
\]

After one inverse step, the next reverse survivor is `1` in every case.
Consequently

\[
\begin{aligned}
B_0&=g^{-1}(P_0)=\{2,\ldots,m+1\},\\
B_1&=g^{-1}(P_1)=\{2,\ldots,m-2,m,m+1,m+2\},\\
B_2&=g^{-1}(P_2)=\{2,\ldots,m-1,m+1,m+2\},
\end{aligned}
\]

and

\[
\begin{aligned}
L_0&=P_0\cap B_0=\{2,\ldots,m\},\\
L_1&=P_1\cap B_1=\{2,\ldots,m-2,m,m+1\},\\
L_2&=P_2\cap B_2=\{2,\ldots,m-1,m+1\}.
\end{aligned}
\]

The condition `m>=4` is essential in the second line.  At `m=3`,

\[
P_1=\{1,3,4\},\qquad r_-(P_1)=5,qquad
f^{-1}(P_1)=\{0,2,6\}.
\]

In the word of `\{0,2,6\}`, the rightmost maximum occurs at coordinate
`2`, so the next reverse survivor is `3`, not `1`.  Hence

\[
 B_1=f^{-2}(P_1)=\{1,4,5\},
 \qquad L_1=\{1,4\}=R_2.
\]

This also follows immediately by reverse `01` cancellation:
`​(1,2)` and `(5,6)` cancel first, then `(4,0)`, leaving the zero at
`3`.

## 4. All three companion rows are selected for `m>=4`

The attacked note's conclusion is correct in the stated safe range, and
can be checked directly without importing any q2 theorem.  The relevant
deficit-three blocks, each preceded by the unmatched zero `1`, are

\[
\begin{aligned}
L_0:&\quad 1^{m-1}0^{m-1},\\
L_1:&\quad 1^{m-3}0\,11\,0^{m-2},\\
L_2:&\quad 1^{m-2}0\,1\,0^{m-2}.
\end{aligned}
\]

For `L_0`, the distinguished down-step is `m+1`, selecting
`P_0=L_0+1` and `B_0=L_0+(m+1)`.

For `L_1`, the unique maximum is attained after the second displayed
extra `1`, at coordinate `m+1`; its following down-step is `m+2`.
Thus the selected endpoints are `P_1=L_1+1` and
`B_1=L_1+(m+2)`.

For `L_2`, the maximum `m-2` is attained once at the end of the initial
run and again, later, at coordinate `m+1`.  The rightmost maximum is
therefore followed by `m+2`, selecting `P_2=L_2+1` and
`B_2=L_2+(m+2)`.

All six rows `R_0,R_1,R_2,L_0,L_1,L_2` are distinct for `m>=4`, so these
six occurrences coexist in a one-occurrence q1 section.  This distinctness
is precisely what fails at `m=3`.

## 5. Clean-C6 algebra and q2 rotation

The old edges have

\[
P_i\cap Q_i=R_i,qquad P_i\cup Q_i=U_i,
\]

while the new edges satisfy

\[
P_i\cap Q_{i+1}=R_{i+1},qquad P_i\cup Q_{i+1}=U_i.
\]

The new edges are not pre-existing outside edges: for every `i`,
`Q_{i+1}` differs from both old neighbours `Q_i` and `B_i` of `P_i`.
Thus the switch is a simple spanning-two-factor trade, not a multigraph
operation.

At each `Q_i`, the old selected row `R_i` is replaced by the new occurrence
of the same row on `P_{i-1}Q_i`; its q2 turn is unchanged.  At `P_i`, the
selected row changes from `R_i` to `R_{i+1}` while the selected companion
row `L_i` remains fixed.

Put

\[
A=\{2,\ldots,m-1\},\quad
B=\{2,\ldots,m-2,m\},\quad
C=\{2,\ldots,m-2,m+1\}.
\]

For `m>=4`, direct intersection gives

\[
(R_0\cap L_0,R_1\cap L_1,R_2\cap L_2)=(A,B,C)
\]

and

\[
(R_1\cap L_0,R_2\cap L_1,R_0\cap L_2)=(B,C,A).
\]

Hence the occurrence-labelled q2 values at the only three changed selected
turns rotate as `(A,B,C)->(B,C,A)`.  The global q2 multiset is exactly
preserved.

## 6. Explicit failure of q2 transparency at `m=3`

At `m=3`, the relevant rows are

\[
\begin{aligned}
&(R_0,R_1,R_2)=(\{1,2\},\{1,3\},\{1,4\}),\\
&(L_0,L_1,L_2)=(\{2,3\},\{1,4\},\{2,4\}).
\end{aligned}
\]

The two maximum-height occurrences of `R_2` are exactly `P_2Q_2` and
`B_1P_1`.  Choose `P_2Q_2`, as required by the attacked note.  Then
`B_1P_1` is unselected.  The changed q2 turns at `P_0,P_2` are

\[
\{2\},\{4\}\longmapsto\{3\},\{2\},
\]

so one occurrence of `\{4\}` is lost and one of `\{3\}` is gained.

If instead the old section chooses `B_1P_1`, then `P_2Q_2` is unselected.
The changed local multiset is

\[
\{2\},\{1\}\longmapsto\{3\},\{2\},
\]

so one occurrence of `\{1\}` is lost and one of `\{3\}` is gained.
Therefore neither max-height tie choice makes the displayed trade
q2-multiset-transparent at `m=3`.

## 7. Exact component effect

Orient every old factor edge as

\[
e_i:P_i\longrightarrow Q_i=g(P_i).
\]

The single-soliton component consists exactly of cyclic intervals of size
`m`, so `e_0` lies on it while `e_1,e_2` do not.

If `e_0,e_1,e_2` lie on three distinct cycles, deleting them leaves paths

\[
\Pi_i:Q_i\leadsto P_i.
\]

The new edges concatenate

\[
\Pi_0, P_0Q_1, \Pi_1, P_1Q_2, \Pi_2, P_2Q_0
\]

into one cycle.  Three components become one.

If `e_1,e_2` lie on one common cycle, deleting them splits that cycle into

\[
\Pi_{12}:Q_1\leadsto P_2,qquad
\Pi_{21}:Q_2\leadsto P_1.
\]

The trade produces exactly the two cycles

\[
\Pi_0\cup P_0Q_1\cup\Pi_{12}\cup P_2Q_0
\]

and

\[
\Pi_{21}\cup P_1Q_2.
\]

Thus two input components remain two.  In both cases the original rigid
cycle is genuinely cut: no output component consists solely of its old
vertices.  The attacked note's remaining global warning is nevertheless
necessary, because in the second case the standalone `\Pi_{21}` cycle need
not contain an omitted q1 occurrence.

## 8. Required correction

The proof-safe theorem is:

> For every `m>=4`, the centered PBBS two-factor admits the displayed
> q1/q2-transparent clean `C6` through the rigid single-soliton component.

Delete both claims that the same display works at `m=3`.  A separate
`m=3` trade, if desired, must avoid the collision `L_1=R_2` or explicitly
coordinate additional occurrence changes outside this six-vertex face.
