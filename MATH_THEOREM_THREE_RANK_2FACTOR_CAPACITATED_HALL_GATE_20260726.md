# The three-rank \(2\)-factor problem: an exact capacitated-Hall gate

Date: 2026-07-26

Method: pure mathematics.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 \mathcal X=\binom{[n]}m,\qquad
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1},
\]

\[
 W=|\mathcal X|=|\mathcal U|,\qquad
 N_1=|\mathcal L|=\frac{m}{m+2}W,\qquad
 d=W-N_1=\frac{2W}{m+2}=o(W).
\tag{0.1}
\]

A spanning \(2\)-factor in the middle-level inclusion graph selects, at
each \(U\in\mathcal U\), two of its middle facets \(A,B\).  Suppressing
\(U\) gives the Johnson edge \(AB\), with lower color \(A\cap B\) and
upper color \(U=A\cup B\).

This note does not prove the requested factor.  It gives a
necessary-and-sufficient completion theorem which isolates the exact
remaining obstruction.

> Start with one Johnson edge of every lower color.  If these \(N_1\)
> edges have distinct upper colors and middle degree at most two, then
> completing them to the desired spanning \(2\)-factor is exactly an
> integral bipartite \(b\)-matching problem.  Its capacitated Hall
> inequalities below are necessary and sufficient.

If the core has only \(o(W)\) cycle components—in particular, if it is a
forest—every successful completion has \(o(W)\) cycles automatically.

**Subsequent audit.**  The Hall cuts admit the exact waste-slack form

\[
 \omega_F(\mathcal A)\le\sigma(\mathcal A),
\]

derived in
`MATH_AUDIT_THREE_RANK_HALL_CORE_AND_Q2_BOWTIE_20260726.md`.  That audit
also proves that the known fixed-girth conflict-free construction can be
prescribed to isolate one middle vertex while using all of its upper
cofacets, violating the singleton Hall cut.  Hence its asymptotic
two-sided-rainbow conclusion does not imply extendibility.  Exactifying
its missing lower colors is a separate determinant-two matching problem;
if that exactification and the waste-slack cuts are solved by `o(W)`
edits, the desired bound `c(F)=o(W)` follows automatically.

This separates the two unresolved issues sharply.

1. The known max-flow lower-rainbow near-\(2\)-factor gives every lower
   color and degree at most two, but may repeat upper colors.  Repeated
   upper colors cannot be repaired by merely adding edges.
2. Even after upper injectivity is imposed, the residual degree slots and
   unused upper colors have exactly equal mass.  They must satisfy a
   zero-slack capacitated Hall condition.

Thus ordinary lower-side Hall or fractional degree completion does not
prove the three-rank statement.

## 1. Cores and their residual data

For a Johnson edge \(e=AB\), write

\[
 \ell(e)=A\cap B\in\mathcal L,\qquad
 u(e)=A\cup B\in\mathcal U.
\tag{1.1}
\]

Call \(F\subseteq E(J(n,m))\) an **admissible lower core** if

1. every \(R\in\mathcal L\) occurs on exactly one edge of \(F\);
2. the upper colors \(u(e)\), \(e\in F\), are pairwise distinct; and
3. \(d_F(A)\le2\) for every \(A\in\mathcal X\).

Necessarily

\[
 |F|=N_1.
\tag{1.2}
\]

Define the middle degree deficit

\[
 \delta_F(A)=2-d_F(A)\in\{0,1,2\},
\tag{1.3}
\]

and the unused upper-color family

\[
 \mathcal U_0(F)=\mathcal U\setminus u(F).
\tag{1.4}
\]

The masses agree exactly:

\[
 \sum_{A\in\mathcal X}\delta_F(A)
 =2W-2N_1=2d,
\qquad
 |\mathcal U_0(F)|=W-N_1=d.
\tag{1.5}
\]

Each unused \(U\) must therefore contribute exactly two incidence edges
to middle facets, and the resulting two facets must fill exactly two
units of (1.3).

## 2. The residual incidence network

Form the bipartite graph

\[
 G_F=(\mathcal U_0(F),\mathcal X;\subset).
\tag{2.1}
\]

Give every \(U\in\mathcal U_0(F)\) demand \(2\), every
\(A\in\mathcal X\) demand \(\delta_F(A)\), and every incidence
\(A\subset U\) capacity one.

An integral feasible \(b\)-matching \(M\) in \(G_F\) chooses two distinct
middle facets \(A_U,B_U\) at every unused upper set \(U\).  Adding the
Johnson edge \(A_UB_U\) then uses upper color \(U\) and supplies one
degree unit at each endpoint.

### Theorem 2.1 (exact completion equivalence)

An admissible lower core \(F\) extends to a spanning \(2\)-factor \(H\) of
the middle-level inclusion graph such that

* every \(U\in\mathcal U\) is used exactly once, and
* every \(R\in\mathcal L\) is used at least once,

if and only if the residual network \(G_F\) has the integral
\(b\)-matching described above.

#### Proof

Suppose first that \(M\) exists.  For each unused \(U\), its two selected
facets are distinct because incidence capacities are one.  Add the
Johnson edge between them.  The \(A\)-demands make the final Johnson
degree exactly two at every middle vertex.  The \(U\)-demands use every
previously unused upper color exactly once.  The core already uses every
lower color, so lower coverage persists.  Lifting each Johnson edge
through its unique upper union gives the required spanning \(2\)-factor
in the bipartite inclusion graph.

Conversely, if a spanning \(2\)-factor extends \(F\), suppress its upper
vertices.  At every unused \(U\), the factor selects two distinct middle
facets.  The selected incidences have degree two at \(U\), and at \(A\)
their number is exactly \(2-d_F(A)=\delta_F(A)\).  They are therefore the
required integral \(b\)-matching. \(\square\)

## 3. The exact Hall inequalities

For \(\mathcal A\subseteq\mathcal X\), put

\[
 d_{\mathcal A}(U)=|\{A\in\mathcal A:A\subset U\}|.
\tag{3.1}
\]

### Theorem 3.1 (capacitated Hall criterion)

The completion in Theorem 2.1 exists if and only if, for every
\(\mathcal A\subseteq\mathcal X\),

\[
 \boxed{
 \sum_{A\in\mathcal A}\delta_F(A)
 \le
 \sum_{U\in\mathcal U_0(F)}
 \min\{2,d_{\mathcal A}(U)\}.}
\tag{3.2}
\]

#### Proof

Necessity is immediate: an unused \(U\) can send at most two units in
total and at most one unit to each incident middle facet, so its
contribution to the demand inside \(\mathcal A\) is at most the summand
on the right of (3.2).

For sufficiency, construct the standard flow network

\[
 s\longrightarrow\mathcal U_0(F)\longrightarrow\mathcal X
 \longrightarrow t,
\]

with capacity \(2\) on \(sU\), capacity \(1\) on every inclusion
\(UA\), and capacity \(\delta_F(A)\) on \(At\).  Total source and sink
capacities both equal \(2d\) by (1.5).  The max-flow/min-cut criterion for
this bipartite \(b\)-matching is exactly (3.2).  All capacities are
integral, so a full flow is integral. \(\square\)

The singleton cut already records a nontrivial obstruction:

\[
 \delta_F(A)
 \le |\{U\in\mathcal U_0(F):A\subset U\}|.
\tag{3.3}
\]

Thus any deficient middle set must retain enough unused cofacets.  The
lower-rainbow max-flow theorem alone contains no such guarantee.

### Proposition 3.2 (the Hall gate can fail even for a forest core)

Upper injectivity, complete lower coverage, maximum degree two, and
acyclicity do not imply (3.2).

#### Proof

Take \(m=2,n=5\), abbreviating sets by their elements.  The five lower
colors are the singletons.  Select the following five Johnson edges,
displayed as

\[
 \text{lower color}\ ;\ \text{upper color}\ ;\ \text{two endpoints}:
\]

\[
\begin{array}{c|c|c}
3&123&13\!-\!23\\
4&124&14\!-\!24\\
5&125&15\!-\!25\\
1&134&13\!-\!14\\
2&235&23\!-\!25.
\end{array}
\tag{3.4}
\]

Every lower color occurs exactly once and the five upper colors are
distinct.  The induced middle graph has maximum degree two and is a
forest: its components are

\[
 24-14-13-23-25-15
\]

with the final edge \(23-25\) already included in this path, together
with the isolated middle sets \(12,34,35,45\).  (Equivalently, reading
the five edges in (3.4) directly shows there is no cycle.)

The middle set \(12\) has deficit \(\delta_F(12)=2\).  Its three upper
cofacets \(123,124,125\) are all already used by the core.  Hence no
unused upper color contains \(12\), and the singleton cut
\(\mathcal A=\{12\}\) in (3.2) reads

\[
 2\le0,
\]

which is false.  Thus this core has no additive completion. \(\square\)

The example does not refute the desired \(2\)-factor at \(m=2\); it
refutes the inference that an arbitrary lower-perfect, upper-injective
bounded-degree forest can be completed without a residual Hall design.

## 4. Cycle count is free once the core is nearly acyclic

Let \(c(F)\) be the number of cycle components of the graph \(F\).

### Theorem 4.1 (component bound)

If an admissible lower core \(F\) satisfies (3.2), then every completion
constructed in Theorem 2.1 has at most

\[
 d+c(F)
\tag{4.1}
\]

cycle components.  In particular, if \(c(F)=o(W)\), the completed
\(2\)-factor has \(o(W)\) cycles.  If \(F\) is a forest, the bound is
simply \(d=2W/(m+2)=o(W)\).

#### Proof

Before completion, \(F\) has \(W\) vertices and \(N_1=W-d\) edges.
Every non-cycle component is a path or an isolated vertex because the
maximum degree is two.  Adding the \(d\) completion edges can create at
most one new cycle component per added edge.  Existing cycle components
of \(F\) persist or merge but cannot contribute more than \(c(F)\).
This proves (4.1). \(\square\)

A more exact count is also useful: a degree-at-most-two core has

\[
\#\{\text{path or isolated components of }F\}=d.
\tag{4.2}
\]

Indeed, a cycle component contributes equally many vertices and edges,
whereas every path or isolated component contributes exactly one more
vertex than edge.  Hence \(W-N_1=d\) is exactly the number of non-cycle
components.

## 5. Converse extraction from any desired factor

The gate is not merely sufficient.

### Theorem 5.1 (exact core characterization)

Suppose \(H\) is a spanning \(2\)-factor using every upper color exactly
once and every lower color at least once.  Choose one \(H\)-edge of each
lower color and call the resulting set \(F\).  Then

1. \(F\) is an admissible lower core;
2. the unused edges of \(H\) witness (3.2); and
3. \(c(F)\le c(H)\).

Consequently, the requested \(o(W)\)-cycle theorem is equivalent to
finding such cores \(F\) with \(c(F)=o(W)\) satisfying (3.2).

#### Proof

The chosen edges have all lower colors exactly once.  They inherit
distinct upper colors and maximum degree two from \(H\), proving
admissibility.  The incidences of the remaining factor edges form the
residual \(b\)-matching of Theorem 2.1, so (3.2) follows.  Finally, a
cycle in the subgraph \(F\) is also a cycle component of the
degree-two graph \(H\): every vertex on that cycle already has both of its
incident \(H\)-edges in \(F\), so no additional \(H\)-edge leaves it.
Hence \(c(F)\le c(H)\). \(\square\)

## 6. Relation to the three existing partial theorems

The exact gate explains why the known results do not combine formally.

### 6.1 Lower-rainbow max flow

The lower-rainbow near-\(2\)-factor selects one edge of every lower color
and has middle degree at most two.  It proves conditions 1 and 3 in the
definition of an admissible core, but not upper-color injectivity.
If two selected edges have the same upper union, no additive completion
can repair the collision: the old edges themselves already use one upper
vertex twice.  They must first be exchanged.

### 6.2 Two-sided-rainbow pseudofactor

The fixed-uniformity four-graph matching theorem gives \(W-o(W)\)
Johnson edges with distinct lower and upper colors and middle degree at
most two.  It does not force every lower color, and its residual
uncovered sets are not known to satisfy (3.2).

### 6.3 Complete lower-rainbow forest / balanced Hamilton cycle

Rado's theorem gives one edge of every lower color in a forest, solving
the cycle-count side optimally.  The saturating-cycle theorem even gives
a connected lower-balanced Hamilton Johnson cycle.  Neither theorem
controls distinct upper unions.  Once upper unions repeat, the residual
network (2.1) is not defined with the required cardinality.

Thus the missing simultaneous statement is precisely:

\[
\boxed{
\begin{array}{c}
\text{one edge per lower color}\\
+\ \text{distinct upper colors}\\
+\ \Delta\le2\\
+\ c(F)=o(W)\\
+\ \text{the capacitated Hall inequalities (3.2).}
\end{array}}
\tag{6.1}
\]

No presently proved theorem in the project supplies all five clauses.

## 7. Color supply and the fractional core are both automatic

The new obstruction is not a shortage of compatible lower--upper color
pairs.

### Proposition 7.1 (exact lower-to-upper color matching)

There is a family \(F_0\) of \(N_1\) Johnson edges which uses every lower
color exactly once and has pairwise distinct upper colors.

#### Proof

Consider the bipartite color-incidence graph

\[
 \mathcal I=(\mathcal L,\mathcal U;\subset).
\tag{7.1}
\]

Its degrees are

\[
 d_{\mathcal L}=\binom{m+2}{2},\qquad
 d_{\mathcal U}=\binom{m+1}{2}.
\tag{7.2}
\]

For every \(\mathcal A\subseteq\mathcal L\), double counting edges from
\(\mathcal A\) to its neighborhood gives

\[
 d_{\mathcal L}|\mathcal A|
 \le d_{\mathcal U}|N(\mathcal A)|,
\]

and hence

\[
 |N(\mathcal A)|
 \ge\frac{m+2}{m}|\mathcal A|
 \ge|\mathcal A|.
\tag{7.3}
\]

Hall's theorem supplies a matching saturating \(\mathcal L\).  A matched
pair \(R\subset U\), with \(|U\setminus R|=2\), determines the unique
Johnson edge joining the two intermediate \(m\)-sets in the interval
\([R,U]\).  The matching properties give the two color assertions.
\(\square\)

What Proposition 7.1 does not control is the degree of the induced graph
on \(\mathcal X\).

There is not even a fractional middle-degree obstruction.  Put

\[
 x_{R,U}=\binom{m+2}{2}^{-1}
\qquad(R\subset U).
\tag{7.4}
\]

Then every lower color has total weight one.  Every upper color has load

\[
 \binom{m+1}{2}\binom{m+2}{2}^{-1}
 =\frac{m}{m+2}<1,
\tag{7.5}
\]

and a fixed middle set \(A\) lies in \(m(m+1)\) intervals
\([R,U]\), so its fractional Johnson degree is

\[
 m(m+1)\binom{m+2}{2}^{-1}
 =\frac{2m}{m+2}<2.
\tag{7.6}
\]

Thus the admissible-core problem is a genuine integral simultaneous
rounding problem: both color marginals and middle capacities have a
strictly feasible symmetric fractional point.

## 8. The no-slack form for the saturating-cycle insertion

For the lower-rainbow cycle on \(N_1\) middle vertices, let
\(\mathcal E\) be the \(d\) omitted middle vertices.  If its \(N_1\)
upper colors happened to be distinct, then

\[
 \delta_F(A)=
 \begin{cases}
 2,&A\in\mathcal E,\\
 0,&A\notin\mathcal E.
 \end{cases}
\tag{7.1}
\]

The completion condition becomes

\[
 2|\mathcal A|
 \le
 \sum_{U\in\mathcal U_0(F)}
 \min\{2,|\{A\in\mathcal A:A\subset U\}|\}
\qquad(\mathcal A\subseteq\mathcal E).
\tag{7.2}
\]

Equivalently, the bipartite inclusion graph between
\(\mathcal E\) and \(\mathcal U_0(F)\) must contain a spanning
\(2\)-regular subgraph.  Both shores have size \(d\); there is no spare
vertex on either side.

This is the exact two-stage absorption obstruction.  Ordinary facet Hall
only finds one cofacet per omitted vertex.  The desired completion needs
degree two on both shores simultaneously.

## 9. Status

The proposed three-rank \(2\)-factor theorem is not refuted.  It is also
not a consequence of the existing lower-rainbow flow, Rado forest, or
fixed-uniformity pseudofactor.  Its exact remaining finite theorem is the
existence of admissible cores satisfying (3.2) and \(c(F)=o(W)\).

The useful gain is that the completion and cycle-count issues are now
fully solved:

* integrality of the completion is free by max flow;
* the only completion obstruction is the explicit cut (3.2); and
* a forest core automatically yields at most \(2W/(m+2)=o(W)\) cycles.

What remains is the simultaneous upper-injective lower-rainbow core.
