# The reciprocal/odd-circuit closure is still fractional

Date: 2026-07-31  
Status: unconditional exact counterexample at the smallest possible
dimension.  This note concerns the direct ordered-four-transversal
polytope, not the narrower middle-levels trace fibre.

## 1. Statement

Let \(P_m^{\rm known}\) be the relaxation on oriented Boolean-diamond
atoms obtained from

1. every lower and upper equality;
2. every tail and head capacity row;
3. every middle-degree and graphic-forest row;
4. every strong odd resource-circuit inequality; and
5. every reciprocal-completion suspension currently proved in
   `MATH_THEOREM_A_CATALAN_ORDERED_FOUR_TRANSVERSAL_ODD_CIRCUIT_ROUNDING_20260731.md`.

At \(m=2\), item 5 is exactly the family

\[
                         x_{ij}+x_{ji}\leq 1.             \tag{1.1}
\]

### Theorem 1.1 (smallest globally extendible fractional vertex)

The polytope \(P_2^{\rm known}\) has an explicit fractional vertex.
Indeed, the vertex lies in the **full stable-set polytope** of the
four-resource conflict graph, not merely in its strong odd-cycle
relaxation.  Consequently strong odd resource circuits together with all
reciprocal-completion suspensions do not describe the integral ordered
four-transversal polytope.

Dimension \(m=2\) is minimal: the corresponding relaxation at \(m=1\)
is integral.

The point below satisfies all outer equalities.  Thus it is not a local
half-vector whose extendibility to the missing colour rows is being
assumed.

## 2. The two four-atom layers

Take \(\Omega=[4]\).  Write \(e_{ij}\) for the diamond whose lower colour
is \(\{i\}\) and whose upper colour is \([4]\setminus\{j\}\).  Consider
the two derangements

\[
 P_0=(13)(24),
 \qquad
 P_1=(1\mapsto4,\ 2\mapsto1,\ 3\mapsto2,\ 4\mapsto3).       \tag{2.1}
\]

Choose the following orientations of their lifted Johnson edges:

\[
\begin{array}{c|c|c|c|c}
 &e&L&U&T\longrightarrow H\\ \hline
P_0&e_{13}&1&124&12\longrightarrow14\\
   &e_{42}&4&134&14\longrightarrow34\\
   &e_{31}&3&234&34\longrightarrow23\\
   &e_{24}&2&123&23\longrightarrow12\\ \hline
P_1&e_{14}&1&123&12\longrightarrow13\\
   &e_{32}&3&134&13\longrightarrow34\\
   &e_{21}&2&234&23\longrightarrow24\\
   &e_{43}&4&124&24\longrightarrow14.
\end{array}                                                     \tag{2.2}
\]

Thus \(P_0\) is the consistently directed physical four-cycle

\[
                       12\to14\to34\to23\to12,             \tag{2.3}
\]

whereas \(P_1\) is the pair of consistently directed paths

\[
                       12\to13\to34,
                 \qquad23\to24\to14.                       \tag{2.4}
\]

Put weight \(1/2\) on each of the eight displayed oriented atoms and zero
on every other orientation.  Call the resulting oriented vector \(z\),
and let \(x\) be its unoriented projection.

## 3. Exact feasibility audit

### 3.1 Outer equalities and directed capacities

Each layer in (2.1) is a lower--upper perfect matching.  Hence every lower
and every upper row has \(z\)-load

\[
                              \tfrac12+\tfrac12=1.          \tag{3.1}
\]

Within either layer the four lower resources and four upper resources are
pairwise distinct.  Within \(P_0\), consistent orientation of (2.3) makes
all four tails distinct and all four heads distinct.  The same is true in
each path of \(P_1\), and the two paths have disjoint middle vertices
except for no vertex at all.  Therefore each of \(P_0,P_1\) is a stable
set in the four-resource conflict graph.  In particular every tail and
head load in their half-sum is at most one.

This also proves more than all strong odd-circuit rows.  The induced
conflict graph on the eight positive atoms is bipartite, with parts
\(P_0,P_1\).  Equivalently,

\[
                       z=\tfrac12\chi^{P_0}
                         +\tfrac12\chi^{P_1}               \tag{3.2}
\]

is literally a convex combination of two stable sets of the complete
resource-conflict graph.  Hence **every** valid resource-conflict
stable-set inequality holds at \(z\).

For a direct check of the requested odd-circuit family, a strong circuit
of length \(2t+1\) cannot have all its vertices in the positive bipartite
support.  It contains at most \(2t\) positive coordinates, and therefore

\[
                    \sum_{e\text{ on the circuit}}z_e
                    \leq (2t)\tfrac12=t.                  \tag{3.3}
\]

### 3.2 Middle capacities and every graphic row

Let

\[
                         S=\{12,14,34,23\}.                \tag{3.4}
\]

The \(P_0\)-degree is two on \(S\) and zero on \(\{13,24\}\).  The
\(P_1\)-degree is one on \(S\) and two on \(\{13,24\}\).  Thus the
weighted middle degrees are respectively \(3/2\) and \(1\), below the
cap two.

It remains to audit every graphic inequality, not only the visible
four-cycle row.  If a nonempty middle-vertex set \(Q\) does not contain
all of \(S\), then the subgraph of the four-cycle (2.3) induced by \(Q\)
is a forest.  The graph (2.4) is always a forest.  Hence

\[
             \tfrac12|E(P_0[Q])|+\tfrac12|E(P_1[Q])|
             \leq |Q|-1.                                  \tag{3.5}
\]

If \(S\subseteq Q\), write
\(r=|Q\cap\{13,24\}|\in\{0,1,2\}\).  Every \(P_1\)-edge joins one
vertex of \(S\) to one of \(\{13,24\}\), two at each latter vertex.
Consequently

\[
 \tfrac12|E(P_0[Q])|+\tfrac12|E(P_1[Q])|
       =\tfrac12(4)+\tfrac12(2r)=2+r
       \leq 3+r=|Q|-1.                                   \tag{3.6}
\]

Equations (3.5)--(3.6) exhaust all graphic rows.

### 3.3 Every reciprocal-completion suspension

The positive projected coordinates are

\[
 x_{13}=x_{14}=x_{21}=x_{24}=x_{31}=x_{32}=x_{42}=x_{43}
              =\tfrac12.                                 \tag{3.7}
\]

The two reciprocal pairs \(13,31\) and \(24,42\) have load one; every
other reciprocal pair has load one half.  Thus (1.1) holds.

For \(m=2\), a four-coordinate suspension necessarily has empty common
core and empty exterior remainder.  Its escape term is zero, so its row
is precisely one of (1.1).  Therefore (3.7) audits the entire currently
proved reciprocal-suspension family, rather than one selected row.

The separate alternating-octagon rank cut has no \(m=2\) instance: its
literal support is a simple eight-cycle in the Johnson graph, whereas
\(J(4,2)\) has only six vertices, and its proved suspension starts at
\(m=3\).  Hence no currently proved octagon row has been silently omitted
from this minimal-dimensional audit.

## 4. Extremality and failure of integral correlation

Let \(R\) be the off-diagonal assignment polytope on variables \(x_{ij}\),
augmented by every reciprocal row (1.1).  At the point (3.7), impose the
four active zero coordinates

\[
                         x_{12}=x_{23}=x_{34}=x_{41}=0      \tag{4.1}
\]

and the active reciprocal equality

\[
                         x_{24}+x_{42}=1.                  \tag{4.2}
\]

These equations together with the assignment equalities have the unique
solution (3.7).  Indeed, put \(a=x_{13}\).  Successively following row
and column equalities around the eight-edge support gives

\[
\begin{array}{c|cccccccc}
ij&13&14&24&21&31&32&42&43\\ \hline
x_{ij}&a&1-a&a&1-a&a&1-a&a&1-a.
\end{array}                                               \tag{4.3}
\]

Equation (4.2) gives \(2a=1\).  Hence \(x\) is a vertex of \(R\).
Since it satisfies all the additional middle, graphic and reciprocal rows,
it remains a vertex after intersecting with those rows.

The same eight-edge face exposes an explicit inequality of the missing
mixed species.  Let

\[
 {\cal S}=P_0\cup P_1,
 \qquad {\cal E}_{\rm esc}=E(B_2)\setminus{\cal S}.       \tag{4.4}
\]

### Proposition 4.1 (mixed completion--graphic escape cut)

Every integral Catalan linear matching at \(m=2\) satisfies

\[
       \sum_{e\in P_0}x_e
       \le 2\sum_{e\in{\cal E}_{\rm esc}}x_e.            \tag{4.5}
\]

The fractional vertex \(x\) violates (4.5), with left side two and right
side zero.

#### Proof

If an integral perfect matching has no escape edge, the eight-edge graph
\({\cal S}\) is one alternating cycle on the lower--upper shores, so its
only perfect matchings are \(P_0\) and \(P_1\).  The lift of \(P_0\) is the
four-cycle (2.3), hence a Catalan linear matching supported on \({\cal S}\)
must be \(P_1\), and the left side is zero.

If there is an escape edge, its integral count is at least one.  The four
edges of \(P_0\) are the two reciprocal pairs
\(\{e_{13},e_{31}\}\) and \(\{e_{24},e_{42}\}\).  The two valid reciprocal
rows (1.1) bound their total selected mass by two.  Therefore the left side
is at most two, while the right side is at least two. \(\square\)

Thus (4.5) is not a further resource-conflict inequality: it combines an
alternating assignment completion, the graphic exclusion of \(P_0\), and
an escape disjunction.  No dimension-uniform suspension of (4.5) is claimed
here.

Finally consider any convex decomposition of the oriented point \(z\)
inside \(P_2^{\rm known}\).  Projection to unoriented diamonds decomposes
the vertex \(x\) inside \(R\), so every summand has projection \(x\).
For every positive diamond in (2.2), its unused reverse orientation has
coordinate zero in \(z\); nonnegativity forces that reverse coordinate to
be zero in every summand.  The used orientation is then forced to equal
the projected coordinate.  Every unsupported diamond is similarly zero.
Thus every summand equals \(z\), proving that \(z\) itself is a fractional
vertex.

Because all integral ordered four-transversals belong to
\(P_2^{\rm known}\), a fractional vertex of this relaxation cannot be a
convex combination of them.  The missing inequality must couple the
resource stable-set choice to graphic acyclicity: layer \(P_0\) is
resource-feasible but cyclic, layer \(P_1\) is a forest, and their half-sum
repairs every graphic row without becoming integrally roundable.

## 5. Minimality and exact boundary

For \(m=1\) there is one unoriented diamond and its two orientations.  The
lower and upper equalities reduce the relaxation to the segment

\[
                              z_++z_-=1,
                         \qquad z_+,z_-\geq0.              \tag{5.1}
\]

Its two vertices are integral, and there is no odd resource circuit or
reciprocal-completion minor.  Thus Theorem 1.1 occurs at the smallest
possible dimension.

The theorem proves the following sharp obstruction:

* even the **entire** resource-conflict stable-set polytope, all current
  reciprocal-completion suspensions, and the full graphic matroid polytope
  can have a fractional intersection;
* consequently adding stronger resource odd-cycle or clique cuts alone
  cannot close the ordered-four-transversal theorem.

It does **not** exclude a different bounded-rank extended formulation with
new variables coupling the graphic and four-resource states.  Nor does it
assert that the single \(m=2\) face is the only missing correlation.  Its
role is to refute the proposed exact description and to identify the first
missing species: a mixed resource--graphic completion inequality.

## 6. Mechanical audit

The exact standard-library reproducer

`scratch/audit_thread_a_ordered_four_transversal_reciprocal_odd_vertex_20260731.py`

checks all atom identities, the eight outer equalities, every directed
capacity, all 63 nonempty graphic subsets, all six reciprocal rows, the
two stable conflict layers, rational rank 12 of the active projected
system, and all six forest derangements against the mixed cut (4.5).  Its
frozen payload is

`scratch/thread_a_ordered_four_transversal_reciprocal_odd_vertex_20260731.audit.json`.
