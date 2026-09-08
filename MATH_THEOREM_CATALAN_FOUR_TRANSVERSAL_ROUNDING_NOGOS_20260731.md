# The Catalan four-transversal gate: exact matroid encoding and sharp rounding no-gos

Date: 2026-07-31  
Status: exact five-matroid formulation; direct matroid/delta-matroid and
natural integral-polymatroid routes excluded; the locally equitable-grid
factorization is false already at `m=2`.  The Catalan Linear Matching
Theorem itself remains open.

## 1. Exact common-independent-set formulation

Fix \(|\Omega|=2m\), and use the notation

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1},
\]

\[
 N=|\mathcal L|=|\mathcal U|=m\operatorname {Cat}_m.
\]

Let \(\vec E_m\) be the set of **oriented diamonds**

\[
 e=(L,U,T,H),\qquad L=T\cap H,\quad U=T\cup H,
 \quad T,H\in\mathcal X,quad T\ne H.               \tag{1.1}
\]

On this one ground set define four partition matroids: at most one selected
element with each fixed value of \(L\), respectively \(U,T,H\).  Define
also the graphic matroid obtained by mapping (1.1) to the undirected
Johnson edge \(TH\); the two orientations of one edge are parallel.

### Theorem 1.1 (five-matroid formulation)

The Catalan Linear Matching assertion is equivalent to the existence of a
set of size \(N\) common independent in these four partition matroids and
the graphic matroid.

#### Proof

A common independent set of size \(N\) uses all \(N\) lower colours and,
independently, all \(N\) upper colours exactly once.  Tail and head
independence gives indegree and outdegree at most one at every middle set,
and graphic independence makes the physical lift acyclic.  It is therefore
a spanning linear forest.

Conversely, orient every component of a Catalan linear matching.  Its lower
and upper colours are bijective, its oriented tails and heads are injective,
and its underlying edges form a graphic forest.  This gives the required
common independent set. \(\square\)

Thus there is an exact matroid language, but it is a **five-matroid
intersection**, not ordinary two-matroid intersection.  Before the graphic
condition is imposed, the four partition matroids are exactly a
four-dimensional matching problem on the resource classes
\((L,U,T,H)\).  Ordinary matroid-intersection or parity algorithms do not
apply merely by renaming this system.

This failure can be made intrinsic on the same ground set.  Recall that an
independence system is \(k\)-extendible if, whenever

\[
 A\subseteq B,\quad A+e\text{ is feasible},
\]

one can remove at most \(k\) members of \(B\setminus A\) and then add
\(e\).  An intersection of \(k\) matroids is \(k\)-extendible: in each
matroid, remove one member of the fundamental circuit of \(e\), choosing it
outside \(A\), and take the union of those removals.

### Theorem 1.2 (four independent blockers)

The ordered-diamond independence system is not \(3\)-extendible already at
\(m=3\).  Consequently it is not the intersection of three (and hence not
two) matroids on the oriented-diamond ground set.

#### Proof

On \(\Omega=[6]\), take

\[
                    e=(12,1234,123,124).              \tag{1.4}
\]

The following four ordered diamonds form a common independent set in all
four partition matroids and in the graphic matroid:

\[
\begin{array}{c|cccc|c}
 &L&U&T&H&\text{resource shared with }e\\ \hline
f_L&12&1235&125&123&L\\
f_U&14&1234&124&134&U\\
f_T&13&1236&123&136&T\\
f_H&24&1245&245&124&H.
\end{array}                                             \tag{1.5}
\]

Their physical graph is the disjoint union of the paths

\[
                    125-123-136,
             \qquad 134-124-245.                       \tag{1.6}
\]

Put \(A=\varnothing\) and \(B=\{f_L,f_U,f_T,f_H\}\).
Then \(A+e\) is feasible.  But each \(f_R\) is the unique member of
\(B\) conflicting with \(e\) in resource class \(R\).  All four must be
removed before \(e\) can be added.  Three removals never suffice. \(\square\)

There is a parallel direct no-go for ordinary matroid parity.  The family
of feasible pair collections in any matroid-parity instance is
\(2\)-extendible: add the first element of the new pair and remove the pair
containing one element of its fundamental circuit; repeat for the second
element.  Since the smaller solution plus the new pair was independent,
the circuit element can be chosen outside it.  Thus at most two old pairs
are removed.  The witness (1.4)--(1.5) proves that no encoding in which one
oriented diamond is one parity item can represent this independence system.
A nonlocal gadget encoding on an enlarged ground set is not excluded.

## 2. A determinant-three ordered-transversal minor

The determinant-two unsigned Johnson triangle is not the end of the matrix
obstruction.  It is already possible to obtain determinant three at
\(m=2\).

Take \(\Omega=\{1,2,3,4\}\).  Use the five ordered-diamond columns

\[
\begin{array}{c|cccc}
 &L&U&T&H\\ \hline
e_1&1&134&14&13\\
e_2&3&234&34&23\\
e_3&4&234&24&34\\
e_4&4&124&14&24\\
e_5&4&134&34&14
\end{array}                                             \tag{2.1}
\]

and the five incidence rows

\[
 T_{34},\quad U_{234},\quad U_{134},\quad L_4,\quad T_{14}.
\]

The resulting minor is

\[
 A=
 \begin{pmatrix}
 0&1&0&0&1\\
 0&1&1&0&0\\
 1&0&0&0&1\\
 0&0&1&1&1\\
 1&0&0&1&0
 \end{pmatrix},
 \qquad \det A=-3.                                    \tag{2.2}
\]

Hence the ordered four-transversal incidence system is not even
bimodular.  In particular, neither total-unimodularity nor a purely
half-integral/bidirected-matrix explanation can round it.

## 3. The natural matching/cap/forest polytope is fractional

The determinant obstruction can be upgraded to an actual fractional
vertex of the precise relaxation used for Catalan Linear Matching.

At \(m=2\), identify a lower singleton with \(i\in[4]\), and identify an
upper triple with its omitted element \(j\).  The diamond graph is the
crown graph

\[
             B_2=K_{4,4}-\{(i,i):i\in[4]\}.            \tag{3.1}
\]

Let

\[
 \pi_0=(2,1,4,3),\qquad \pi_1=(2,3,4,1).              \tag{3.2}
\]

Regard each permutation as the incidence vector of a perfect matching in
(3.1), and put

\[
                    x={1\over2}(\chi^{\pi_0}+\chi^{\pi_1}).             \tag{3.3}
\]

The physical lift of \(\pi_0\) is the four-cycle on

\[
                    S=\{13,14,23,24\},                 \tag{3.4}
\]

while the lift of \(\pi_1\) is the two-path forest

\[
             14-13-23,\qquad 12-24-34.                 \tag{3.5}
\]

### Theorem 3.1 (fractional vertex)

The point (3.3) satisfies both perfect-matching margins, every middle
capacity constraint, and every graphic-forest inequality.  It is a
fractional vertex of that relaxation.

#### Proof

Both summands are perfect matchings and both physical lifts have maximum
degree two, so the matching and capacity constraints hold after averaging.
The only forest inequality violated by the four-cycle \(\pi_0\) is the
one on its complete vertex set \(S\).  On that set \(\pi_0\) contributes
four internal edges and \(\pi_1\) contributes two, so (3.3) contributes
three, exactly \(|S|-1\).  Every other forest inequality holds in both
summands or has enough extra vertices to absorb the one cycle.

For extremality, take all eight matching-margin rows, the six nonnegativity
rows corresponding to zero coordinates of \(x\), and the tight forest row
on \(S\).  Their rank is the full variable dimension twelve.  Therefore
\(x\) is a vertex, and four of its coordinates equal \(1/2\). \(\square\)

### Corollary 3.2 (integral-polymatroid no-go, in the natural variables)

The relaxation cannot itself be an intersection of integral polymatroids,
nor can it be the integer-coordinate projection of an integral-polyhedral
extended formulation: such a polytope and every coordinate projection of
it have integral vertices.

This does **not** exclude an extended formulation for the convex hull of
the genuine solutions.  It excludes the proposed shortcut of recognizing
the already-written matching/cap/forest relaxation as an integral
polymatroid intersection.

Even deleting every graphic inequality does not restore integrality.

### Theorem 3.3 (the cap-only polytope is fractional)

The perfect-matching plus middle-cap polytope has a fractional vertex at
\(m=3\).

#### Proof

Write an upper four-set by its omitted pair.  Let \(P_0\) be the perfect
matching in (5.3), and define a second perfect matching \(P_1\) by

\[
\begin{array}{rrrrr}
12\mapsto46,&13\mapsto26,&14\mapsto23,&15\mapsto36,&16\mapsto24,\\
23\mapsto15,&24\mapsto56,&25\mapsto34,&26\mapsto35,&34\mapsto12,\\
35\mapsto16,&36\mapsto45,&45\mapsto13,&46\mapsto25,&56\mapsto14.
\end{array}                                             \tag{3.6}
\]

Their symmetric difference is the single alternating cycle whose lower
shore order is

\[
 12,13,14,15,25,26,24,23,34,56,35,45,46,16,36.        \tag{3.7}
\]

Hence \([P_0,P_1]\) is an edge of the bipartite perfect-matching polytope.
The only load-three vertices of \(P_0\) are \(123,356\), while the only
load-three vertex of \(P_1\) is \(125\).  At these three vertices the
other matching has load one.  At every other middle vertex the two loads
sum to at most four.  Therefore

\[
                       y={1\over2}(\chi^{P_0}+\chi^{P_1})               \tag{3.8}
\]

satisfies every cap \(y(\mathcal R_X)\le2\).

The cap at \(123\) cuts the relative interior of the matching-polytope edge
\([P_0,P_1]\) exactly at its midpoint.  The intersection of a polytope
halfspace with the relative interior of an edge has that crossing point as
a new vertex.  Thus (3.8) is a fractional cap-polytope vertex. \(\square\)

Consequently neither integrality nor normality of the obvious cap polytope
can yield a two-balanced one-factorization.  Such a factorization, if it
exists, is a correlated integer-decomposition statement strictly stronger
than its fractional relaxation.

## 4. Direct matroid and delta-matroid representations fail

Still at \(m=2\), let \({\cal B}\) be the family of full perfect diamond
matchings whose physical lifts are linear forests.  Consider

\[
 P=(2,3,4,1),\qquad Q=(2,4,1,3).                      \tag{4.1}
\]

Their lifts are respectively

\[
 14-13-23\ \sqcup\ 12-24-34,
\]

and

\[
 13-14-24\ \sqcup\ 12-23-34,                         \tag{4.2}
\]

so both belong to \({\cal B}\).  Remove the edge \((3,4)\) from \(P\).
The three edges of \(Q\setminus P\) are

\[
                    (2,4),\quad(3,1),\quad(4,3).       \tag{4.3}
\]

Adding the first or third repeats a lower shore vertex; adding the second
repeats upper vertex 1, which is still used by \((4,1)\).  Thus no element
of \(Q\setminus P\) exchanges for \((3,4)\).

### Theorem 4.1 (basis-exchange obstruction)

The natural family of full Catalan linear matchings on the diamond-edge
ground set is not the base family of a matroid.  It is also not the
feasible-set family of a delta-matroid.

#### Proof

The preceding pair violates basis exchange.  All members of \({\cal B}\)
have the same cardinality.  If an equicardinal family satisfies symmetric
exchange, then for \(e\in P\setminus Q\) the second toggled element must lie
in \(Q\setminus P\); all other possibilities change cardinality.  Thus an
equicardinal delta-matroid is a matroid base family, and the same example
rules it out. \(\square\)

This is a direct-ground-set statement.  It does not logically exclude a
highly nonlocal gadget reduction to matroid parity on a larger ground set.
What it does show is that no direct delta-matroid exchange theorem is hiding
behind the observed solutions.

## 5. Why local equitable edge colouring does not finish the problem

For \(X\in\mathcal X\), let

\[
 \mathcal R_X=\{(L,U):L\subset X\subset U\}\cong K_{m,m}.              \tag{5.1}
\]

In a proper \(d\)-edge-colouring of the diamond graph, every colour is a
matching inside every \(\mathcal R_X\).  Requiring the restriction to each
grid to be equitable in the standard sense is stronger than two-balance:
because

\[
 {m^2\over d}={2m\over m+1}\in(1,2),                 \tag{5.2}
\]

standard local equity forces every colour to occur **once or twice** in
every grid.  Two-balance only requires zero, one, or two.

### Theorem 5.1 (the stronger locally equitable factorization is false)

There is no proper three-edge-colouring of \(B_2\) that is equitable on
all six local \(K_{2,2}\) grids.

#### Proof

A colour factor of the crown graph (3.1) is a derangement \(\pi\) of four
points.  If \(\pi\) has cycle type \((2,2)\), its physical lift is a
four-cycle plus two isolated middle vertices; hence it has grid loads zero
and two and is not locally equitable.  If \(\pi\) is a four-cycle, its lift
is two three-vertex paths, so every middle load is one or two; it is locally
equitable.

Suppose a one-factorization used only four-cycles.  Relabel so its first
factor is \((1\,2\,3\,4)\).  After deleting the identity diagonal and this
factor from \(K_{4,4}\), the remaining two-regular bipartite graph has only
its two alternating perfect matchings: one is \((1\,4\,3\,2)\), while the
other is \((1\,3)(2\,4)\).  The latter has type \((2,2)\), a contradiction.
\(\square\)

In fact the four unlabelled one-factorizations of \(B_2\) consist of three
having two four-cycle factors and one \((2,2)\) factor, and one having three
\((2,2)\) factors.

Nor does solving all local grids separately recover diamond properness.
In \(J(4,2)\), colour red the triangle on

\[
                \{12,13,23\}
\]

and the triangle on \(\{14,24,34\}\).  The remaining six edges form a
cycle; colour it alternately blue and green.  At every middle vertex the
three colour loads are \(2,1,1\), the unique equitable profile.  But the
three edges in the upper diamond clique \(U=123\) are all red.  Thus the
Johnson/local-grid marginal can be perfectly equitable while failing even
properness at a diamond shore.

The converse marginal implication also fails inside the Boolean family.

### Theorem 5.2 (proper diamond colouring need not be two-balanced)

At \(m=3\), there is a perfect matching of the diamond graph whose physical
load at \(X=123\) is three.  Consequently there is a proper six-edge-
colouring containing an overloaded colour.

#### Proof

Identify an upper four-set with its omitted two-set \(C\).  The following
table is a bijection from lower two-sets \(L\) to omitted two-sets \(C\),
and every displayed pair is disjoint:

\[
\begin{array}{rrrrr}
12\mapsto45,&13\mapsto46,&14\mapsto26,&15\mapsto23,&16\mapsto25,\\
23\mapsto56,&24\mapsto35,&25\mapsto36,&26\mapsto34,&34\mapsto15,\\
35\mapsto14,&36\mapsto24,&45\mapsto16,&46\mapsto13,&56\mapsto12.
\end{array}                                             \tag{5.3}
\]

Thus \(L\mapsto U=\Omega\setminus C\) is a perfect diamond matching.
The three rows

\[
             12\mapsto45,\qquad13\mapsto46,
             \qquad23\mapsto56                         \tag{5.4}
\]

all lift to an edge incident with \(123\), so its load is three.  Removing
this perfect matching leaves a five-regular bipartite graph, which
one-factorizes by Kőnig's theorem.  Reinsert (5.3) as the sixth factor.
\(\square\)

Therefore:

* equitable colouring of the Johnson/local-grid marginal does not enforce
  the diamond-star marginal;
* arbitrary proper/equitable colouring of the diamond graph does not
  enforce local two-balance; and
* demanding both simultaneously is precisely a new common-colouring
  theorem, while demanding standard equity on every grid is too strong and
  already false.

## 6. Scoped conclusion

The Catalan Linear Matching gate has not been solved here.  What is now
settled is the exact status of the standard rounding proposals:

1. the honest positive formulation is common independence in four partition
   matroids and one graphic matroid;
2. the direct matroid and delta-matroid interpretations fail at \(m=2\);
3. the ordered incidence matrix has determinant three, not merely the known
   determinant-two triangle;
4. the natural matching/cap/forest LP has an explicit fractional vertex at
   \(m=2\), ruling out its recognition as an integral polymatroid
   intersection; and
5. conventional local equitable edge colouring is not the missing theorem.

The surviving routes must exploit the Boolean correlation across overlapping
rectangles, for example a specially controlled alternating-cycle sequence or
the decorated middle-levels trace criterion.  Generic matroid, parity,
polymatroid, and marginal-equitability theorems do not supply that
correlation.

## 7. Mechanical audit

The standard-library script

`scratch/audit_catalan_four_transversal_rounding_nogos_20260731.py`

checks (2.2), all constraints and full active rank for (3.3), the basis-
exchange pair (4.1), the four-blocker witness (1.4)--(1.5), all four
\(m=2\) one-factorizations, the locally equitable but diamond-improper
Johnson colouring, the matching and load-three claim in (5.3), and the
adjacent cap-feasible fractional midpoint (3.6)--(3.8).
