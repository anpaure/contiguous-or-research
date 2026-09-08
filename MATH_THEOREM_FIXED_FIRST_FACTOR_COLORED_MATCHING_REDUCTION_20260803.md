# Fixed-first-factor coloured matching reduction

**Date:** 2026-08-03  
**Status:** unconditional exact reduction, fractional feasibility, and a
proof-safe obstruction to a direct TU/flow argument.  This note does **not**
prove that the required integral coloured perfect matching exists for every
parameter.

## 0. Statement

Let `m>=3`, put `n=2m-1`, and write

\[
 \mathcal L={ [n]\choose m-1},\qquad
 \mathcal M={ [n]\choose m},\qquad
 \mathcal U={ [n]\choose m+1}.
\]

Set

\[
 W=|\mathcal L|=|\mathcal M|,qquad
 U=|\mathcal U|,qquad
 C=W-U=\operatorname {Cat}_m.
\]

Let `G` be the bipartite containment graph between `mathcal L` and
`mathcal M`, and fix one perfect matching `F_0` of `G`.  Delete `F_0` and
put

\[
                         H:=G-F_0.                         \tag{0.1}
\]

For an edge `e=qT` of `H`, define its upper colour by

\[
                  \kappa(e):=F_0(q)\cup T\in\mathcal U.   \tag{0.2}
\]

For `R in mathcal U`, let `E_R` be the colour class
`kappa^(-1)(R)`.

Then:

1. `H` is `(m-1)`-regular on both shores;
2. every upper colour class has the exact size

   \[
                              |E_R|=m+1;                    \tag{0.3}
   \]

3. the constant vector

   \[
                              x_e={1\over m-1}              \tag{0.4}
   \]

   is a fractional perfect matching of `H`, and every upper colour has
   load

   \[
                         x(E_R)={m+1\over m-1}.              \tag{0.5}
   \]

In particular, for `m>=3`, (0.4) belongs to the cap-two coloured perfect
matching polytope

\[
 \mathcal P(F_0)=\left\{
 x\ge0:
 x(\delta(q))=x(\delta(T))=1,
 \quad 1\le x(E_R)\le2
 \right\}.                                                  \tag{0.6}
\]

An integral perfect matching `F_1 subseteq E(H)` has every upper-colour
multiplicity in `{1,2}` exactly when

\[
       y_R:=|F_1\cap E_R|=1+1_{\mathcal D}(R)               \tag{0.7}
\]

for a simple family `mathcal D subseteq mathcal U` satisfying

\[
 |\mathcal D|=\operatorname {Cat}_m,
 \qquad
 \deg_{\mathcal D}(i)=2\operatorname {Cat}_{m-1}
 \quad(i\in[n]).                                            \tag{0.8}
\]

The conditions in (0.8) are automatic consequences of `F_1`; they are not
asserted to be sufficient by themselves.  For a **fixed** candidate
`mathcal D`, existence of `F_1` is exactly a common-base problem for three
partition matroids.

Finally, the natural constraint matrix in (0.6) is not totally unimodular
in general.  At `m=4` there is an explicit fixed first factor `F_0` for
which it contains a `5 by 5` odd-cycle submatrix of determinant `2`.
Consequently the uniform fractional point cannot be rounded merely by
invoking the standard TU/network-flow theorem for bipartite matchings.
This determinant does **not** prove that the particular polytope (0.6) is
nonintegral, and it does not rule out a Boolean-specific extended
formulation or exchange theorem.

## 1. Exact regularity and colour degrees

The graph `G` is `m`-regular: an `(m-1)`-set has `m` one-element
extensions in `[2m-1]`, and an `m`-set has `m` one-element deletions.
Deleting a perfect matching proves that `H` is `(m-1)`-regular.

Fix `R in mathcal U`.  For each facet `S in {R choose m}`, let

\[
                            q_S:=F_0^{-1}(S).                 \tag{1.1}
\]

There is one element `b_S in R-S`.  Since `q_S subset S`, the set

\[
                            T_S:=q_S\cup\{b_S\}              \tag{1.2}
\]

has size `m` and contains `q_S`.  It is different from `S`, because
`b_S notin S`; hence `q_ST_S` is an edge of `H`.  Moreover

\[
                         F_0(q_S)\cup T_S=S\cup T_S=R,       \tag{1.3}
\]

so it has colour `R`.

Conversely, if `qT` has colour `R`, then `S=F_0(q)` is an `m`-facet of
`R`, and (1.2) is forced.  Thus

\[
 S\longmapsto q_ST_S
\]

is a bijection from the `m+1` facets of `R` to `E_R`.  This proves
(0.3).

Equation (0.4) has vertex load `(m-1)/(m-1)=1`, and (0.3) gives (0.5).
For `m>=3`,

\[
                         1\le {m+1\over m-1}\le2,            \tag{1.4}
\]

which proves fractional feasibility in (0.6).  The excluded case `m=2`
has colour load `3`, so the cap-two requirement is impossible there.

## 2. The exact colour-load projection

The following identities hold for every fractional perfect matching `x`
of `H`, not only for integral points.  Put

\[
                              y_R=x(E_R).                    \tag{2.1}
\]

Since the colour classes partition `E(H)`,

\[
                              \sum_R y_R=W.                  \tag{2.2}
\]

Fix a coordinate `i`.  For an edge `qT`, put `S=F_0(q)`.  The two
different `m`-supersets `S,T` of `q` satisfy `S cap T=q`; hence

\[
 1_{i\in\kappa(qT)}=1_{i\in S}+1_{i\in T}-1_{i\in q}.      \tag{2.3}
\]

Sum (2.3) with weights `x_(qT)`.  The row equations at the lower shore,
the column equations at the middle shore, and the fact that `F_0` is a
bijection give

\[
 \sum_{R\ni i}y_R
 =2{2m-2\choose m-1}-{2m-2\choose m-2}.                     \tag{2.4}
\]

Define `z_R=y_R-1`.  Using

\[
 W-U=\operatorname {Cat}_m
\]

and subtracting the one-copy incidence vector of the complete upper
layer from (2.2)--(2.4), one obtains

\[
 \boxed{
 \sum_R z_R=\operatorname {Cat}_m,
 \qquad
 \sum_{R\ni i}z_R=2\operatorname {Cat}_{m-1}
 \quad(i\in[n]).}                                           \tag{2.5}
\]

Indeed, the coordinate difference is

\[
 \begin{aligned}
 &2{2m-2\choose m-1}
 -{2m-2\choose m-2}-{2m-2\choose m}\\
 &\hspace{35mm}=2\operatorname {Cat}_{m-1}.                 \tag{2.6}
 \end{aligned}
\]

Inside (0.6), `0<=z_R<=1`.  Therefore the colour-load projection of
`mathcal P(F_0)` lies in the fractional regular-Catalan-design polytope
defined by (2.5).

If `x=1_(F_1)` is integral, then `y_R` is an integer.  Consequently

\[
 1\le y_R\le2\quad\hbox{for every }R
\]

is equivalent to `z=1_mathcal D` for a simple family `mathcal D`, and
(2.5) becomes exactly (0.8).  Conversely (0.7) plainly gives loads one or
two.  This proves the asserted characterization.

As a calibration, when `m=3` every integral perfect matching of `H` is
automatically balanced.  Here an upper colour is the complement of one
coordinate in `[5]`; (2.2) and (2.4) force each of the five loads to be
exactly `2`.

## 3. Exact three-partition-matroid formulation

Fix a candidate duplicate family `mathcal D subseteq mathcal U` satisfying
(0.8), and set

\[
                   b_R:=1+1_{\mathcal D}(R).                 \tag{3.1}
\]

On the common ground set `E(H)`, define three partition matroids:

* `P_L`, whose blocks are `delta(q)`, `q in mathcal L`, each of capacity
  one;
* `P_M`, whose blocks are `delta(T)`, `T in mathcal M`, each of capacity
  one;
* `P_U(mathcal D)`, whose blocks are `E_R`, `R in mathcal U`, with
  capacity `b_R`.

Because

\[
                  \sum_R b_R=U+|\mathcal D|=U+C=W,           \tag{3.2}
\]

a set `F subseteq E(H)` of size `W` is independent in all three matroids
if and only if

\[
 |F\cap\delta(q)|=|F\cap\delta(T)|=1,
 \qquad
 |F\cap E_R|=b_R.                                           \tag{3.3}
\]

Thus `F` is exactly the desired coloured perfect matching.  Equivalently:

\[
 \boxed{
 \text{fixed-}\mathcal D\text{ feasibility}
 =\text{ a common base of three partition matroids}.}       \tag{3.4}
\]

This is a genuine exact combinatorial structure, but it is not the
ordinary two-matroid-intersection theorem.  The first two partitions alone
give the usual integral bipartite perfect-matching polytope; the upper
colour partition is a third simultaneous resource.

## 4. An explicit determinant-two obstruction

We now exhibit a fixed first factor at `m=4` for which the standard
constraint matrix is not totally unimodular.

Work on `Z_7`, with addition modulo `7`.  The five translation orbits of
three-subsets have representatives

\[
 012,\quad013,\quad014,\quad015,\quad024.                    \tag{4.1}
\]

Define `F_0` equivariantly by adjoining, respectively,

\[
                         3,\quad5,\quad2,\quad4,\quad3.       \tag{4.2}
\]

Thus, for example,

\[
 F_0(012+t)=0123+t,
 \qquad
 F_0(014+t)=0124+t.                                         \tag{4.3}
\]

The image four-subsets in (4.2) lie in the five distinct translation
orbits represented by

\[
 0123,\quad0135,\quad0124,\quad0134,\quad0125.               \tag{4.4}
\]

Every nontrivial subset has a translation orbit of size seven.  Hence
(4.1) partitions all `35` lower vertices, (4.4) partitions all `35`
middle vertices, and (4.2) defines a perfect matching.

Return to one-based notation.  Three values that will be used are

\[
 F_0(123)=1234,qquad
 F_0(125)=1235,qquad
 F_0(126)=1256.                                             \tag{4.5}
\]

Consider the following five edges of `H`, with their upper colours:

\[
\begin{array}{c|c|c|c}
&q&T&\kappa(e)\\ \hline
e_0&123&1235&12345\\
e_1&123&1236&12346\\
e_2&126&1236&12356\\
e_3&125&1256&12356\\
e_4&125&1245&12345
\end{array}                                                 \tag{4.6}
\]

Select the five constraint rows

\[
 123_{\mathcal L},\quad
 1236_{\mathcal M},\quad
 12356_{\mathcal U},\quad
 125_{\mathcal L},\quad
 12345_{\mathcal U}.                                       \tag{4.7}
\]

In the edge order `e_0,...,e_4`, their incidence submatrix is

\[
 A_5=
 \begin{pmatrix}
 1&1&0&0&0\\
 0&1&1&0&0\\
 0&0&1&1&0\\
 0&0&0&1&1\\
 1&0&0&0&1
 \end{pmatrix}.                                             \tag{4.8}
\]

This is the vertex-edge incidence matrix of an odd cycle of length five,
and

\[
                              \det A_5=2.                    \tag{4.9}
\]

Therefore the matrix consisting of the lower-vertex, middle-vertex, and
upper-colour rows is not totally unimodular.  In particular, appending
the colour constraints to the usual bipartite matching matrix destroys
the direct TU/network-flow certificate already inside this Boolean
instance.

The conclusion is intentionally limited.  A non-TU submatrix does not by
itself show that the right-hand sides in (0.6), or any fixed target
(3.1), have a fractional extreme point.  It also does not exclude an
extended formulation with additional variables.  It proves only that
ordinary bipartite-flow integrality and a naive TU claim do not close the
fixed-first-factor selector.

## 5. Exact remaining theorem

The fixed-first-factor route has no fractional degree or colour-moment
obstruction: (0.4) is feasible and has exactly the required regular
Catalan colour projection.  The integral question is

\[
 \boxed{
 \begin{minipage}{0.82\linewidth}
 choose a simple regular Catalan duplicate family `mathcal D` and a
 common base of the three partition matroids in Section 3.
 \end{minipage}}                                            \tag{5.1}
\]

Equivalently, find a perfect matching `F_1` of `G-F_0` whose upper colour
loads are all one or two.  If the two-factor `F_0 cup F_1`, compressed on
the middle shore, is also required to be one cycle, that is a further
graphic/topological condition not imposed by (0.6).

Thus fixing the first factor converts the owner/q1 selector into one
coloured perfect-matching problem with an exact uniform fractional point.
What remains is a specifically Boolean integral three-resource rounding
theorem; neither standard flow/TU nor ordinary two-matroid intersection
supplies it automatically.
