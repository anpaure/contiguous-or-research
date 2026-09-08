# Independent audit: fixed-first-factor coloured matching reduction

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_FIXED_FIRST_FACTOR_COLORED_MATCHING_REDUCTION_20260803.md`  
**Audit status:** **PASS**.  The regularity, colour-class census,
fractional point, colour-moment projection, cap-two integral
characterization, fixed-duplicate-family three-partition-matroid
formulation, and explicit determinant-two minor are all correct.  No
all-parameter integral selector theorem follows from these statements.

This audit is independent in the following sense: every numerical identity
and every incidence used by the determinant witness is recomputed below from
the definitions.  It performs no finite search and makes no computational
existence claim.

## 1. Parameters and Catalan difference

Let

\[
 n=2m-1,\qquad
 W={2m-1\choose m-1}={2m-1\choose m},\qquad
 U={2m-1\choose m+1}.
\]

The binomial ratio gives

\[
 {U\over W}={m-1\over m+1}.
\]

Therefore

\[
 W-U={2W\over m+1}
 ={1\over m+1}{2m\choose m}
 =\operatorname {Cat}_m.
\]

Thus the theorem's parameters `W`, `U`, and `C` are consistent.

## 2. The residual graph and its upper colours

The containment graph between ranks `m-1` and `m` of `[2m-1]` is
`m`-regular on each shore.  Removing a perfect matching `F_0` therefore
leaves an `(m-1)`-regular bipartite graph `H`.

Fix an upper set `R` of rank `m+1`.  For each of its `m`-facets `S`, put

\[
 q=F_0^{-1}(S),\qquad b=R\setminus S,\qquad T=q\cup\{b\}.
\]

Then `q` is contained in both `S` and `T`, while `T` is not `S` because it
contains `b`.  Hence `qT` belongs to `H` and

\[
 F_0(q)\cup T=S\cup T=R.
\]

Conversely, an edge of colour `R` determines the facet `S=F_0(q)` and then
forces the unique element `b=R-S` and the set `T=q+b`.  This proves a
bijection

\[
 {R\choose m}\longleftrightarrow E_R
\]

and hence

\[
 |E_R|=m+1.
\]

The classes `E_R` partition `E(H)`, because two distinct `m`-supersets of
the same `(m-1)`-set have an `(m+1)`-set as their unique union.

## 3. Uniform fractional feasibility

At every lower or middle vertex, the vector

\[
 x_e={1\over m-1}
\]

has load one.  At each upper colour it has load

\[
 x(E_R)={m+1\over m-1}.
\]

For `m>=3`, this number lies in `[1,2]`, with equality to `2` only at
`m=3`.  Thus the claimed uniform point is feasible for all stated
parameters.  At `m=2`, `H` is a one-factor of size three and its only upper
colour has load three, so the theorem's exclusion of that case is also
correct.

As a consistency check,

\[
 |E(H)|=W(m-1)=U(m+1),
\]

where the last equality follows from `U/W=(m-1)/(m+1)`.

## 4. Independent derivation of the colour moments

Let `x` be any fractional perfect matching of `H`, and write

\[
 y_R=x(E_R).
\]

Because the colour classes partition the edge set,

\[
 \sum_R y_R=W.
\]

For an edge `qT`, set `S=F_0(q)`.  Since `S` and `T` are distinct
`m`-supersets of `q`,

\[
 S\cap T=q,
\]

so for each coordinate `i`,

\[
 1_{i\in S\cup T}=1_{i\in S}+1_{i\in T}-1_{i\in q}.
\]

After weighting by `x`, the three terms sum respectively to

\[
 {2m-2\choose m-1},\qquad
 {2m-2\choose m-1},\qquad
 {2m-2\choose m-2}.
\]

The first count uses that `F_0` bijects the lower shore with all middle
sets; the other two use the column and row equations.  Hence

\[
 \sum_{R\ni i}y_R
 =2{2m-2\choose m-1}-{2m-2\choose m-2}.
\]

Put `z_R=y_R-1`.  There are

\[
 {2m-2\choose m}
\]

upper sets containing `i`.  By symmetry

\[
 {2m-2\choose m}={2m-2\choose m-2},
\]

and therefore

\[
 \begin{aligned}
 \sum_{R\ni i}z_R
 &=2{2m-2\choose m-1}-2{2m-2\choose m-2}\\
 &={2\over m}{2m-2\choose m-1}
 =2\operatorname {Cat}_{m-1}.
 \end{aligned}
\]

Together with `W-U=Cat_m`, this proves exactly

\[
 \sum_Rz_R=\operatorname {Cat}_m,
 \qquad
 \sum_{R\ni i}z_R=2\operatorname {Cat}_{m-1}.
\]

For the uniform point, `z_R=2/(m-1)`; substituting this value into the two
identities gives the same totals, providing a second check.

## 5. Integral cap two and the duplicate design

For an integral perfect matching `F_1`, every `y_R` is integral.  Under
the bounds `1<=y_R<=2`, one has uniquely

\[
 y_R=1+1_{\mathcal D}(R)
\]

for a simple family `D` of upper sets.  The moment equations then force

\[
 |\mathcal D|=\operatorname {Cat}_m,
 \qquad
 \deg_{\mathcal D}(i)=2\operatorname {Cat}_{m-1}.
\]

These equations are mutually consistent: double counting incidences in
`D` gives

\[
 (m+1)\operatorname {Cat}_m
 =(2m-1)\,2\operatorname {Cat}_{m-1}.
\]

They are necessary projections of a matching, not a sufficiency theorem;
the audited theorem states this qualification correctly.

At `m=3`, there are five upper sets, each the complement of one coordinate.
The total colour load is ten, while the coordinate equation says that the
sum of the four colours containing a fixed coordinate is eight.  The omitted
colour consequently has load two.  Thus every integral perfect matching is
automatically balanced, as claimed.

## 6. Fixed `D` is exactly three partition-matroid bases

Fix a candidate family `D` satisfying the displayed design equations and
put

\[
 b_R=1+1_{\mathcal D}(R).
\]

The lower blocks, middle blocks, and colour blocks are each genuine
partitions of `E(H)`.  Give capacities one, one, and `b_R`, respectively.
The three partition matroids all have rank `W`:

* the lower and middle partitions each have `W` nonempty blocks;
* the colour partition has total capacity

  \[
  \sum_Rb_R=U+|\mathcal D|=U+\operatorname {Cat}_m=W,
  \]

  and every colour class has size `m+1>=2>=b_R`.

If a set `F` of size `W` is independent in all three matroids, its size
forces every lower and middle capacity to be saturated, so `F` is a perfect
matching.  Its size also equals the sum of all colour capacities, forcing

\[
 |F\cap E_R|=b_R
\]

for every colour.  Conversely, a matching with these colour loads is visibly
independent and rank `W` in all three matroids.  Hence fixed-`D` feasibility
is exactly a common base of the three stated partition matroids.

This is not an instance of ordinary two-matroid intersection.

## 7. Independent check of the `m=4` first factor

Work first in zero-based `Z_7`.  The five lower representatives and their
cyclic gap triples are

\[
\begin{array}{c|c}
012&(1,1,5)\\
013&(1,2,4)\\
014&(1,3,3)\\
015&(1,4,2)\\
024&(2,2,3).
\end{array}
\]

No two gap triples are cyclic rotations, so these are five distinct
translation orbits.  Since every nonempty proper subset of `Z_7` has an
orbit of size seven, they account for all `5*7=35` lower vertices.

Adjoining `3,5,2,4,3`, respectively, produces the five four-set orbits
represented in the theorem.  Their complements lie in the five distinct
three-set orbits above (in the order `012,024,015,014,013`), so the image
orbits are also pairwise distinct and cover all 35 middle vertices.  The
equivariant map is therefore a perfect matching.

Converting the three relevant values to one-based notation gives

\[
 F_0(123)=1234,
 \qquad
 F_0(125)=1235,
 \qquad
 F_0(126)=1256.
\]

For the five claimed residual edges one obtains directly

\[
\begin{array}{c|c|c|c}
 &q&T&F_0(q)\cup T\\ \hline
e_0&123&1235&12345\\
e_1&123&1236&12346\\
e_2&126&1236&12356\\
e_3&125&1256&12356\\
e_4&125&1245&12345.
\end{array}
\]

Each `T` differs from `F_0(q)`, so every displayed edge really lies in
`H`.  The five chosen constraint rows meet the five columns in the pattern

\[
 A_5=
 \begin{pmatrix}
 1&1&0&0&0\\
 0&1&1&0&0\\
 0&0&1&1&0\\
 0&0&0&1&1\\
 1&0&0&0&1
 \end{pmatrix}.
\]

This is `I+P`, where `P` is a cyclic permutation matrix of odd order five.
Thus

\[
 \det(A_5)=1-(-1)^5=2.
\]

It is a square submatrix of the lower/middle/colour incidence matrix, so
that matrix is not totally unimodular.  Changing a colour row's sign when
encoding a lower inequality changes only the sign of the determinant, not
its absolute value.

The theorem also scopes the consequence correctly: a determinant-two
minor defeats the naive TU certificate, but does not itself prove that the
specific right-hand-side polytope is nonintegral and does not rule out an
extended formulation.

## 8. Final audited boundary

The theorem establishes an exact reduction:

\[
 \boxed{
 \text{choose a regular Catalan duplicate family and find a common base
 of three partition matroids.}}
\]

It also establishes a perfectly balanced fractional point and a concrete
obstruction to applying the ordinary bipartite-flow/TU theorem directly.
It does **not** establish the required integral coloured matching for every
`m`, does not force the union `F_0 union F_1` to be connected, and does not
address deeper upper shadows, residence, or the terminal compiler.

