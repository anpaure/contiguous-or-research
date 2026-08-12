# PBBS short residences are not FIFO or LIFO across a seam

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

A proposed linear-cost seam repair would order the positive coordinate runs
crossing one cut by their insertion times and hope that their removal times
are monotone (FIFO or LIFO).  This endpoint-order property is false in the
canonical PBBS, already inside the explicit three-root component used in
the gap-five/gap-seven analysis.

For every \(r\ge4\), there is one projected cut crossed by three short
residences of lengths \(3,6,6\) whose insertion order is

\[
 x_4,\ x_1,\ x_6,
\]

whereas their removal order is

\[
 x_1,\ x_4,\ x_6.
\]

Thus the permutation is \(213\), neither increasing nor decreasing.
No seam theorem may infer a contiguous run block merely from PBBS
no-overtaking.

## 1. The explicit PBBS component

Put \(N=2r+1\), and use the three quotient roots

\[
\begin{aligned}
D_0&=110100(10)^{r-3},\\
D_1&=1011(01)^{r-3}00,\\
D_2&=(10)^{r-3}110010.
\end{aligned}
\]

Their one-step PBBS voltages are

\[
 2,\quad4,\quad N-5,
\]

and the three-step sum is \(N+1\).  Normalize the first omitted physical
label to zero.  On the lifted component of length \(3N\), the omitted-label
word is therefore

\[
 \boxed{
  \lambda_{3j}=j,\qquad
  \lambda_{3j+1}=j+2,\qquad
  \lambda_{3j+2}=j+6
  \pmod N.}
 \tag{1.1}
\]

Indeed the first two formulas add the voltages \(2,4\), and the third
voltage advances the next three-block origin from \(j\) to \(j+1\).

## 2. Three crossing short runs

For a fixed label \(x\), three consecutive occurrences, using integer
lifts in one period, are

\[
 3x-16,\qquad3x-5,\qquad3x.
 \tag{2.1}
\]

Thus the first gap has length eleven and the second has length five.
Consider the three occurrences

\[
\begin{array}{c|c|c|c}
\text{label}&\text{insertion time}&\text{removal time}&\text{odd gap}\\ \hline
x_4&-4&7&11\\
x_1&-2&3&5\\
x_6& 2&13&11.
\end{array}
\tag{2.2}
\]

All three insertion times are even.  Hence their complement-projected
step-two residence intervals use odd transition edges.  With the exact
PBBS residence convention

\[
 I_i=\{i-1,i+1,\ldots,i+g\},
\]

the three intervals are

\[
\begin{aligned}
I_{-4}&=\{-5,-3,-1,1,3,5,7\},\\
I_{-2}&=\{-3,-1,1,3\},\\
I_{2}&=\{1,3,5,7,9,11,13\}.
\end{aligned}
\tag{2.3}
\]

They all cross the projected transition edge \(1\).  Their positive owner
residence lengths are

\[
 {11+1\over2}=6,\qquad {5+1\over2}=3,\qquad
 {11+1\over2}=6.
\]

Reading (2.2), insertion order is \(x_4,x_1,x_6\), while removal order is
\(x_1,x_4,x_6\).  This proves the claim.

## 3. Scope

The counterexample refutes only the proposed monotone-endpoint shortcut.
It does not refute an \(O(H)\) or \(O(H\log H)\) shared seam based on a
more general permutation braid.  In fact the crossing-run data at a seam
should now be regarded as a genuine permutation diagram; a successful
linear seam theorem must exploit more than FIFO/LIFO contiguity.
