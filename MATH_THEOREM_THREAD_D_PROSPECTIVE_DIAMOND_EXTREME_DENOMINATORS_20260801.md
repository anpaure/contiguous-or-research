# Prospective oriented-diamond vertices are not half-integral, even on a protected predecessor face

Date: 2026-08-01  
Lane: Thread D / prospective `M0` / integral rounding  
Status: exact negative theorem for half-integrality; no negative claim about
integral feasibility or bounded-defect absorption.

## 0. Verdict

The linear relaxation of the prospective oriented-diamond plus residual-`M0`
system is not an odd-circuit/half-integral polytope.

* A five-row literal Boolean basis at `m=3` has determinant `3` and its
  all-one right-hand side has values `1/3,1/3,1/3,2/3,2/3`.
* The **full** `m=3` standard-form polytope has an extreme point of
  denominator `11`.  A positive support minor has determinant `-11`.
* Even after fixing a two-arc correlated predecessor path at value one, the
  resulting nonempty protected face has a full extreme point of denominator
  `4`.  Its positive support minor has determinant `4`.

Thus a rounding proof cannot classify every fractional obstruction as an
odd circuit carrying weight `1/2`.  This remains true after preserving the
maximal `ell=m-1=2` predecessor bank in the smallest nontrivial dimension.
The actual long tight-pivot face is not separately refuted, but any positive
theorem for it must use more than the ambient prospective matrix and the
mere fact that the protected predecessor pairs extend.

## 1. Standard form and the exact vertex test

Use the notation of
`MATH_THEOREM_THREAD_D_PROSPECTIVE_M0_ORIENTED_DIAMOND_AND_RESIDUAL_HALL_20260801.md`.
For an oriented diamond `d=(R;L,T,V)`, let `x_d>=0`; for a residual
incidence pair `L subset T`, let `y_(L,T)>=0`.  Add a head slack `s_V>=0`.
The complete relaxation is

\[
\begin{aligned}
 \sum_{d:R(d)=R}x_d&=1,\\
 \sum_{d:L(d)=L}x_d+\sum_{T\supset L}y_{L,T}&=1,\\
 \sum_{d:T(d)=T}x_d+\sum_{L\subset T}y_{L,T}&=1,\\
 \sum_{d:V(d)=V}x_d+s_V&=1.                    \tag{1.1}
\end{aligned}
\]

Let `A` be this zero-one equality matrix.

**Lemma 1.1 (support criterion).**  A feasible point `z` of (1.1) is a
vertex if the columns `A[:,supp(z)]` are linearly independent.

**Proof.**  If `z=(z'+z'')/2` with `z',z''>=0`, every coordinate zero in
`z` is zero in both endpoints.  Hence `A(z'-z'')=0` is supported inside
`supp(z)`.  Column independence gives `z'=z''`.  `square`

All finite certificates below use this criterion over the rationals; no
floating-point rank claim enters the proof.

## 2. A five-by-five denominator-three Boolean basis

Represent subsets of `[5]` by their ordinary bitmasks.  Use the five rows

\[
 R=29,\quad L=5,\quad L=20,\quad T=13,\quad T=21
\]

and the following columns, in order:

\[
\begin{array}{c|cccc}
 &R&L&T&V\\ \hline
d_1&29&12&13&28\\
d_2&29&20&28&21\\
d_3&29&5&21&13
\end{array},
\qquad y_{5,13},\quad y_{20,21}.
\]

Their restricted matrix is

\[
B=\begin{pmatrix}
1&1&1&0&0\\
0&0&1&1&0\\
0&1&0&0&1\\
1&0&0&1&0\\
0&0&1&0&1
\end{pmatrix},
\qquad \det B=3.                                  \tag{2.1}
\]

Moreover

\[
B(1/3,1/3,1/3,2/3,2/3)^t={\bf1}.                 \tag{2.2}
\]

This is already a literal denominator-three basis of the actual Boolean
system, not a projected or fictitious hypergraph.  By itself it is only a
local basis, so the next section records a full-polytope vertex.

## 3. A full denominator-eleven vertex at `m=3`

All omitted coordinates below are zero.  The displayed numerators are over
the common denominator `11`.

### Diamond columns

\[
\begin{array}{c|rrrr|r}
 &R&L&T&V&11x\\ \hline
1&15&10&11&14&3\\
2&15&12&14&13&5\\
3&15&3&7&11&3\\
4&23&18&19&22&1\\
5&23&20&22&21&4\\
6&23&6&22&7&6\\
7&27&17&25&19&1\\
8&27&3&11&19&8\\
9&27&10&26&11&2\\
10&29&24&25&28&4\\
11&29&20&21&28&3\\
12&29&20&28&21&4\\
13&30&24&28&26&5\\
14&30&10&14&26&6
\end{array}                                                    \tag{3.1}
\]

### Residual and slack columns

\[
\begin{array}{c|rr|r@{\qquad}c|r|r}
 &L&T&11y&&V&11s\\ \hline
1&5&7&3&&7&5\\
2&5&21&8&&11&6\\
3&9&13&5&&19&2\\
4&9&25&6&&13&6\\
5&17&19&10&&21&3\\
6&6&7&5&&25&11\\
7&18&22&1&&14&8\\
8&18&26&9&&22&10\\
9&12&13&6&&28&4\\
10&24&28&2&&&
\end{array}                                                    \tag{3.2}
\]

Direct summation verifies every one of the five upper rows, ten lower
rows, ten tail rows, and ten head-with-slack rows of (1.1).  All 33
displayed coordinates are positive.  The 33 rows listed in the audit JSON
cut out a `33 by 33` support minor of determinant `-11`.  Lemma 1.1 makes
the point a vertex, and its denominator is exactly `11`.

## 4. A denominator-four vertex preserving a predecessor path

Fix the two diamonds

\[
 (15;3,7,11),\qquad (27;10,11,26)                 \tag{4.1}
\]

at value one.  Their middle arcs are the simple Johnson predecessor path

\[
              7\longrightarrow11\longrightarrow26,                \tag{4.2}
\]

with distinct lower colours `3,10` and upper colours `15,27`.  This is a
maximal `ell=m-1` protected bank for the small protected-extension theorem
at `m=3`.

The face is integrally nonempty: the audit enumerates 289 integral
completions.  Nevertheless it has the following non-half-integral vertex.
Again all omitted coordinates vanish.

\[
\begin{array}{c|rrrr|r}
 &R&L&T&V&x\\ \hline
1&15&3&7&11&1\\
2&23&17&19&21&1/2\\
3&23&18&22&19&1/2\\
4&27&10&11&26&1\\
5&29&20&21&28&1/4\\
6&29&9&13&25&1/4\\
7&29&20&28&21&1/4\\
8&29&17&25&21&1/4\\
9&30&6&14&22&1
\end{array}                                                    \tag{4.3}
\]

\[
\begin{array}{c|rr|r@{\qquad}c|r|r}
 &L&T&y&&V&s\\ \hline
1&5&13&1/2&&7&1\\
2&5&21&1/2&&19&1/2\\
3&9&25&3/4&&13&1\\
4&17&21&1/4&&25&3/4\\
5&18&19&1/2&&14&1\\
6&12&13&1/4&&28&3/4\\
7&12&28&3/4&&&\\
8&20&22&1/2&&&\\
9&24&26&1&&&
\end{array}                                                    \tag{4.4}
\]

Every row of (1.1) sums to one.  The 24 positive support columns have a
`24 by 24` minor of determinant `4`; hence they are independent and the
point is a vertex by Lemma 1.1.  In particular, conditioning on a genuine
correlated predecessor path does not restore half-integrality in the
smallest protected face.

## 5. Consequences for rounding and absorption

1. **Odd-circuit rounding is insufficient.**  Neither the ambient vertex
   nor the protected-face vertex decomposes into independent `1/2` odd
   circuits.  The residual `y` columns and the four diamond resources can
   couple several circuits into determinants `4` and `11`.

2. **Unused Catalan slots do not by themselves give a defect bound.**  The
   equality `C=W-U` supplies residual matching slots, but an extreme-point
   argument has not bounded the number of coupled fractional components or
   shown that one slot absorbs one component.  Such a statement requires a
   new Boolean exchange lemma.

3. **The protected bank remains compatible with a positive theorem.**  The
   face in Section 4 contains many integral points.  The result refutes a
   proposed *method* (half-integral circuit rounding), not integral
   existence, bounded-defect rounding, or the actual long tight-pivot
   theorem.

4. **A safe next target.**  Prove an absorber for a bounded collection of
   general support circuits of (1.1), measured by their consumed
   `(L,T,V)` boundary rather than by denominator or odd-cycle count.  To
   obtain `B+O(1)`, one must additionally prove that a chosen optimal/basic
   fractional solution has only `O(1)` exposed circuit boundary after the
   tight-pivot contraction.  Neither fact follows from LP extremality.

## 6. Exact audit artifacts

The full denominator-eleven vertex is generated and verified by

* `scratch/audit_threadD_oriented_diamond_vertex_denominators_20260801.py`;
* `scratch/threadD_oriented_diamond_denominator11_vertex_20260801.audit.json`.

The protected-face denominator-four vertex is generated and verified by

* `scratch/audit_threadD_protected_face_vertex_denominators_20260801.py`;
* `scratch/threadD_protected_path_denominator4_vertex_20260801.audit.json`.

The generators reconstruct every value over `Q`, verify all 35 standard
form rows exactly, and compute the displayed support determinants by
fraction-free elimination.
