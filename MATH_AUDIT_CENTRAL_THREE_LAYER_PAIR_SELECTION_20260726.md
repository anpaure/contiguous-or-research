# Exact LP audit of the central three-layer pair selection

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let `n=2m+1` and `W=binom(n,m)`.  The proposed construction is the
following exact integer problem.

* For every `(m+1)`-set `U`, choose one unordered pair of its `m`-facets.
* Every `m`-set must occur in exactly two chosen pairs.
* Every `(m-1)`-set must occur as the intersection of at least one chosen
  pair.

The fractional problem is solved exactly by symmetry, with strict lower
colour slack `2/m`.  Its min-hole LP has a short exact dual, given below.
What symmetry does **not** provide is integrality.  The constraint matrix
contains the unsigned incidence matrix of a triangle as a minor, of
determinant two.  Equivalently, the pair-at-`U` variables retain a local
odd-cycle correlation which disappears if one projects only to the
ordinary bipartite `2`-factor marginals.

After fixing one perfect matching, the necessary representative-matching
matrix even contains an explicit `C_5` blossom at `m=3`: its five
half-columns have fractional value `5/2`, while an integral representative
matching uses at most two.  This is a literal odd-set obstruction to that
rounding route, not just a failed TU test.

Thus the three-layer proposal is a clean reduction, not yet a proof.  Its
remaining theorem is an integral coloured-`2`-factor statement.  Even
after that statement, the number of cycles is a separate gate: the exact
constraints do not currently imply `o(W)` cycles, and the total duplicate
colour budget is only `2W/(m+2)`.

## 1. Pair variables and exact constraints

Put

\[
 \mathcal U=\binom{[n]}{m+1},\qquad
 \mathcal A=\binom{[n]}m,\qquad
 \mathcal R=\binom{[n]}{m-1}.                           \tag{1.1}
\]

For `R subset U`, let `U\R={x,y}`.  The variable

\[
                         x_{U,R}\in\{0,1\}              \tag{1.2}
\]

selects the pair of facets

\[
                         R\cup\{x\},\qquad R\cup\{y\}. \tag{1.3}
\]

The exact system is

\[
 \boxed{
 \begin{aligned}
  \sum_{R\in\binom U{m-1}}x_{U,R}&=1
       &&(U\in\mathcal U),\\
  \sum_{\substack{U\supset A\\R\subset A}}
       x_{U,R}&=2
       &&(A\in\mathcal A),\\
  \sum_{U\supset R}x_{U,R}&\ge1
       &&(R\in\mathcal R).
 \end{aligned}}                                         \tag{1.4}
\]

The first line chooses one pair at every upper set.  In the second line,
`R subset A subset U` says exactly that `A` is one endpoint of the pair.
The last line is lower-colour coverage.

### Lemma 1.1 (bipartite `2`-factor normal form)

An integral solution of the first two lines of (1.4) is equivalent to a
spanning `2`-factor of the rank-`m`/rank-`m+1` inclusion graph.  At an
upper vertex `U`, its two selected neighbours are the facets in (1.3),
and the colour of the resulting length-two path is their intersection
`R`.

#### Proof

Given `x`, retain the two inclusion edges from `U` to the facets in
(1.3).  The first line gives degree two at every `U`, and the second gives
degree two at every `A`.  Conversely, the two neighbours of a degree-two
upper vertex are distinct facets; their intersection is the unique `R`
which recovers `x_{U,R}=1`. \(\square\)

Thus the desired integral object is precisely a coloured bipartite
`2`-factor which uses every lower colour.

### Corollary 1.2 (two-perfect-matching form)

Every integral solution is equivalently a pair of edge-disjoint perfect
matchings, written as facet bijections
`f_0,f_1:mathcal U -> mathcal A`, such that

\[
 U\longmapsto f_0(U)\cap f_1(U)                         \tag{1.5}
\]

is surjective onto `mathcal R`.  The number of bipartite cycles is the
number of cycles of the relative permutation `f_1^{-1}f_0` on
`mathcal U`.

#### Proof

Every even cycle of a bipartite `2`-factor has a unique alternating
two-edge-colouring up to exchanging the colours on that component.
Taking the two colour classes gives `M_0,M_1`; the reverse construction is
their union.  Formula (1.5) is the colour definition at `U`.  Contracting
one matching turns the other into the relative permutation and contracts
each bipartite cycle to one permutation cycle. \(\square\)

Fixing `f_0` makes the remaining integrality gate especially transparent.
Delete the `f_0` edge at every `U`.  Every remaining incidence edge
`U--A` receives the lower colour

\[
                         \kappa(U,A)=f_0(U)\cap A.       \tag{1.6}
\]

One must find a perfect matching `f_1` in this residual bipartite graph
which uses every colour.  This is the intersection of the two ordinary
matching partitions with a third, lower-colour covering partition.  In
other words it is a structured three-dimensional matching problem; the
third partition is exactly what is absent from the integral bipartite
`2`-factor projection.

More precisely, every such `f_1` contains a **representative submatching**
`Z`: choose one `f_1` edge of each lower colour.  Then `Z` uses every
colour exactly once and uses every `U` and `A` at most once.  Conversely,
a representative submatching is useful only if it extends to a perfect
matching in the residual bipartite graph.  Thus there are two gates:
three-partite representative matching, followed by extendability.

## 2. Symmetry solves the fractional problem

Let

\[
                         D=\binom{m+1}{2}.               \tag{2.1}
\]

Set `x_(U,R)=1/D` for every admissible pair.  Every upper equation is
immediate.  A fixed `m`-set `A` has `m+1` upper extensions, and inside
each one there are `m` pairs containing `A`; hence its fractional degree
is

\[
                         {m(m+1)\over D}=2.              \tag{2.2}
\]

A fixed lower set `R` has `binom(m+2,2)` upper extensions.  Its colour
load is therefore

\[
             {\binom{m+2}{2}\over\binom{m+1}{2}}
             ={m+2\over m}=1+{2\over m}.                \tag{2.3}
\]

So (1.4) is fractionally feasible with exact slack `2/m` in every colour.

## 3. Exact min-hole LP dual

Introduce `h_R>=0` and relax `x>=0`.  The fractional minimum number of
uncovered lower colours is

\[
 \begin{aligned}
 H^{LP}=\min\quad&\sum_Rh_R\\
 \text{subject to}\quad
 &\text{the first two equalities of (1.4)},\\
 &\sum_{U\supset R}x_{U,R}+h_R\ge1\quad(R\in\mathcal R).
                                                               \tag{3.1}
 \end{aligned}
\]

### Theorem 3.1 (three-layer fractional dual)

One has

\[
 \boxed{
 \begin{aligned}
 H^{LP}=\max\quad
  &\sum_Ua_U+2\sum_Ab_A+\sum_Rc_R\\
 \text{subject to}\quad
  &a_U+b_{R\cup\{x\}}+b_{R\cup\{y\}}+c_R\le0
       &&(U\setminus R=\{x,y\}),\\
  &a_U,b_A\in\mathbb R,\qquad0\le c_R\le1.
 \end{aligned}}                                         \tag{3.2}
\]

In particular `H^(LP)=0`.

#### Proof

Use unrestricted multipliers `a_U,b_A` for the two equality families and
nonnegative multipliers `c_R` for the lower inequalities.  Minimizing over
`h_R>=0` gives `c_R<=1`; minimizing over `x_(U,R)>=0` gives the displayed
column inequality.  Strong LP duality proves (3.2).

For a direct check of the last assertion, multiply every column
inequality by the symmetric value `1/D` and sum.  Equations (2.2)--(2.3)
give

\[
 \sum_Ua_U+2\sum_Ab_A+{m+2\over m}\sum_Rc_R\le0.
\]

Consequently the dual objective is at most
`-(2/m)sum_R c_R<=0`.  The zero dual solution has value zero, proving
`H^(LP)=0`. \(\square\)

If holes are forbidden outright, the same formula holds with
`c_R>=0` unbounded.  The strict slack in (2.3) again makes every dual
objective nonpositive.  Hence there is no fractional or cut obstruction.

## 4. Why the fractional proof does not round automatically

For one fixed `U`, choose three distinct facets `A_1,A_2,A_3`.  The three
pair columns `(A_1A_2),(A_2A_3),(A_3A_1)`, restricted to the three middle
degree rows, form

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix},
 \qquad\det=2.                                           \tag{4.1}
\]

This is the unsigned incidence matrix of an odd triangle.  Therefore the
matrix in (1.4) is not totally unimodular.  The obstruction is local and
survives all permutation symmetry: relabelling only produces more copies
of (4.1).

There is also an explicit blossom obstruction **after one perfect matching
has been fixed**, so it is not an artefact of the pair-variable
extension.  Take `m=3,n=7` and use a perfect facet matching `f_0` which
contains

\[
 0123\mapsto012,\qquad
 0236\mapsto023,\qquad
 0135\mapsto035.                                        \tag{4.2}
\]

These three prescribed edges extend to a perfect matching.  One direct
certificate for the remaining upper sets is

```text
0124:024 0125:015 0126:016 0134:014 0136:013
0145:145 0146:146 0156:156 0234:034 0235:025
0245:245 0246:046 0256:026 0345:045 0346:346
0356:036 0456:056 1234:124 1235:123 1236:136
1245:125 1246:126 1256:256 1345:135 1346:134
1356:356 1456:456 2345:234 2346:236 2356:235
2456:246 3456:345
```

In the residual three-partite hypergraph of (1.6), consider the five
edges

\[
\begin{array}{c|c|c}
U&A&\kappa(U,A)\\ \hline
0123&013&01\\
0123&023&02\\
0236&026&02\\
0236&036&03\\
0135&013&03.
\end{array}                                             \tag{4.3}
\]

On the five resource rows

\[
 U_{0123},\ R_{02},\ U_{0236},\ R_{03},\ A_{013},       \tag{4.4}
\]

their incidence matrix is the unsigned cycle matrix of `C_5`.  Assigning
weight `1/2` to all five columns gives load one on every displayed
resource and total value `5/2`; an integral matching can use at most two
of the five when it is used as the representative submatching `Z`.  The
missing valid inequality for that necessary representative polytope is
the literal blossom

\[
                         \sum_{e\in C_5}z_e\le2.         \tag{4.5}
\]

This is an actual odd-set obstruction in the central-three-layer
representative geometry.  (A full `f_1` may repeat a colour, so (4.5) is
not asserted for all of its edges; it applies after one witness per colour
is selected.)  It does not prove that the full symmetric instance has no
integral solution; it proves that any representative-rounding proof must
control blossoms such as (4.5), not only the symmetric degree and colour
cuts.

There is a useful explanation of exactly what is lost.  Define the
incidence marginals

\[
 y_{U,A}=\sum_{\substack{R\subset A\\R\subset U}}x_{U,R}. \tag{4.6}
\]

Then

\[
 \sum_{A\subset U}y_{U,A}=2,\qquad
 \sum_{U\supset A}y_{U,A}=2,\qquad0\le y_{U,A}\le1.    \tag{4.7}
\]

This is the ordinary bipartite `2`-factor polytope and is integral.  But
the lower colour records **which pair** of the two incidences at `U` is
chosen.  It is not a linear function of the marginals `y`.  Decomposing a
fractional `y` into integral bipartite `2`-factors can therefore destroy
all the lower-colour inequalities.

Thus symmetry plus ordinary bipartite uncrossing proves only (4.7).  It
does not prove the integral system (1.4).  Equation (4.1) identifies the
missing odd-set/blossom layer.  It is not, by itself, a proof that the
special all-ones right-hand side in (1.4) is infeasible; the existence of
an integral colour-covering factor remains a separate theorem.

## 5. The cycle gate is independent

Let `c(F)` be the number of cycles of the bipartite `2`-factor supplied by
an integral solution.  The constraints (1.4) prescribe degrees and
colours but contain no connectivity or subtour inequalities.  Hence their
LP/dual gives no bound on `c(F)`.

The exact duplicate-colour budget is

\[
 W-|\mathcal R|
 =W-\binom{n}{m-1}
 ={2W\over m+2}.                                        \tag{5.1}
\]

After choosing one protected witness occurrence for each lower colour,
only the quantity in (5.1) remains freely removable.  Therefore a merging
argument which spends even one duplicate occurrence per joined cycle can
be guaranteed from this ledger only when

\[
                         c(F)=O(W/m)=o(W).               \tag{5.2}
\]

For an arbitrary solution of (1.4), this bound is not known.  A local
cycle join changes the selected pair at one or more upper vertices and can
delete a uniquely represented lower colour.  Thus the usual uncoloured
`2`-factor switching theorem cannot simply be imported.

Two valid conditional conclusions are:

1. if the integral construction itself yields `c(F)=o(W)`, no further
   asymptotic cycle theorem is needed;
2. if it yields `c(F)=O(W/m)` and one can choose every joining trade to
   remove only duplicate colours (or replace each removed witness in the
   same trade), then all but `o(W)` cycles can be merged without losing
   coverage.

Neither condition follows from (1.4) alone.

## 6. Exact remaining theorem

The direct central-three-layer lane has been reduced to the following
standalone integral assertion.

> There is a `0`--`1` solution of (1.4) whose associated bipartite
> `2`-factor has `o(W)` components, or admits colour-preserving joins down
> to `o(W)` components.

The uniform fractional solution and Theorem 3.1 show that all capacity
and cut ledgers are exactly favourable.  The triangle minor (4.1) shows
why this assertion is not a consequence of total unimodularity.  Proving
it requires a genuine coloured-factor theorem (including its odd-set
constraints), not another symmetric fractional averaging argument.
