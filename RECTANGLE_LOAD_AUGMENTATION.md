# Rectangle load augmentation: why the required cycle order grows

## Status

This note audits the convex-load route in Section 8 of
`TWO_SIDED_DIAMOND_2FACTOR.md`.

The most optimistic version of that route is false: a colour-perfect
matching can have a middle load three and be a **strict** local minimum of

\[
 \Phi(G)=\sum_{X\in\mathcal M}\binom{d(X)}2
\]

under every four-diamond rectangle trade.  This already happens for
`m=3`.

The failure is structural rather than numerical.  An overloaded middle
vertex can be pivot-locked: every rectangle touching two of its incident
diamonds is pivoted at that vertex and hence preserves its load, while none
of its incident edges can be removed by a rectangle pivoted at the other
endpoint.

The strict `m=3` trap below is repaired by one alternating six-cycle, and
exhaustive enumeration proves that every overloaded rectangle-local
matching at `m=3` has such a repair.  But even the resulting four-or-six
augmentation statement is false: at `m=4` there is an exact matching with
load three admitting no decreasing rectangle and no decreasing alternating
six-cycle.  One alternating eight-cycle repairs it.

The emerging honest conjecture is dimension-dependent: an improving
alternating cycle using at most `m` selected diamonds may always exist.
Exact results for `m<=3`, an exact order-four trap/repair at `m=4`, and
random tests through `m=5` support this formulation.  It remains unproved.
Acyclicity is not treated here; maximum middle load two is the first
priority.

## 1. Setup and the convex excess identity

Use the notation

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1}.
\]

A colour-perfect selection is a perfect matching between `mathcal L` and
`mathcal U`.  Its selected diamond `(S,U)` projects to the two middle sets
in the interval `[S,U]`.  Let `d(X)` be the resulting middle degree.  If

\[
 W=|\mathcal M|,\qquad N=|\mathcal L|=|\mathcal U|,
\]

then

\[
 \sum_Xd(X)=2N.
\tag{1.1}
\]

There is also the pointwise bound

\[
 d(X)\le m.
\tag{1.1a}
\]

Indeed, every selected diamond through `X` has a different lower colour
`X-a` with `a in X` (and also a different upper colour `X+c` with
`c notin X`).  Matching injectivity therefore permits at most `m` such
diamonds.  This is the first reason an order-`m` exchange bound is natural.

Let `z` be the number of middle vertices of degree zero.  Directly,

\[
 \begin{aligned}
 \Phi-(2N-W)
 &=\sum_X\left(\binom{d(X)}2-d(X)+1\right)\\
 &=z+\sum_{X:d(X)\ge3}\binom{d(X)-1}{2}.
 \end{aligned}
\tag{1.2}
\]

Thus `Phi` detects both isolated vertices and overload.  Its absolute
minimum `2N-W` is attained precisely when every middle degree is one or
two.  This is stronger than the required maximum-degree-two condition,
which permits isolated vertices, so `Phi` should be regarded as a useful
but noncanonical potential.

For the alternative overload potential

\[
 E(G)=\sum_X(d(X)-2)_+,
\tag{1.3}
\]

the same pivot-lock obstruction below still applies.

## 2. Exact rectangle calculus

Fix a middle set `X`, distinct `a,b in X`, and distinct `c,d notin X`.
Suppose the selected matching contains

\[
 (X-a,X+c),\qquad (X-b,X+d).
\]

Write the old secondary vertices as

\[
 P=X-a+c,\qquad Q=X-b+d
\]

and the new secondary vertices after the rectangle switch as

\[
 R=X-a+d,\qquad T=X-b+c.
\]

The four secondary vertices are distinct.  Both old and new diamonds
contribute twice at the pivot `X`, so the pivot cancels from the load
change.

### Lemma 2.1 (exact potential change)

The rectangle trade has

\[
 \Delta\Phi
 =d(R)+d(T)-d(P)-d(Q)+2.
\tag{2.1}
\]

Consequently it strictly improves `Phi` exactly when

\[
 d(P)+d(Q)\ge d(R)+d(T)+3.
\tag{2.2}
\]

#### Proof

Decreasing a load `q` by one changes `binom(q,2)` by `-(q-1)`, while
increasing it by one changes the potential by `q`.  Apply this to `P,Q`
and `R,T`.  QED.

### Corollary 2.2 (complete rectangle-local criterion)

A colour-perfect matching is rectangle-local for `Phi` if and only if,
for every selected pair through every pivot `X`,

\[
 d(P)+d(Q)\le d(R)+d(T)+2.
\tag{2.3}
\]

It is a strict rectangle-local minimum if every such inequality is strict
in the integer sense

\[
 d(P)+d(Q)\le d(R)+d(T)+1.
\tag{2.4}
\]

This is a local certificate: no global matching computation is needed once
the selected diamonds and their middle loads are known.

## 3. Pivot-locked overloads

Let `G` be the projected middle graph of a colour-perfect matching.

### Lemma 3.1 (rectangle-removability)

An incidence `XY` can be removed by one rectangle trade in a way that
decreases `d(X)` if and only if `d(Y)>=2`.

#### Proof

Every rectangle containing the selected diamond `XY` has one of its two
middle endpoints as pivot.

* If it is pivoted at `X`, two old and two new edges remain incident with
  `X`, so `d(X)` is unchanged.
* If it is pivoted at `Y`, it requires a second selected edge at `Y` and the
  switch replaces `YX` by a different secondary edge.  Such a second edge
  exists exactly when `d(Y)>=2`.

Any two selected diamonds through one pivot have distinct lower deletions
and distinct upper insertions, because the lower and upper colours are
matched injectively.  Hence they always form the legal rectangle used in
the second case.  QED.

Call `X` **pivot-locked** when all its selected neighbours have degree one.
Lemma 3.1 says that no rectangle can reduce the load of a pivot-locked
vertex.  Rectangles centered at `X` can move its neighbours, but preserve
`d(X)`.

In particular, if `d(X)>=3` and all its neighbours are leaves, then no
single rectangle can decrease the overload potential (1.3).  This is the
smallest structural obstruction to a rectangle-only augmentation proof.

## 4. A strict `m=3` counterexample

Take the ground set `[6]`.  The following table gives a perfect matching
from the fifteen two-sets to the fifteen four-sets:

| lower | upper | lower | upper | lower | upper |
|---|---|---|---|---|---|
| `12` | `1234` | `13` | `1235` | `23` | `2345` |
| `14` | `1345` | `24` | `1246` | `34` | `2346` |
| `15` | `1245` | `25` | `2456` | `35` | `3456` |
| `45` | `1456` | `16` | `1256` | `26` | `2356` |
| `36` | `1236` | `46` | `1346` | `56` | `1356` |

Every lower set lies in its assigned upper set, and every four-set occurs
once.  Its middle loads are

\[
 d(145)=3,
\tag{4.1}
\]

\[
 d(X)=2\quad\text{for }X\in
 \{123,124,234,236,346,156,256,356\},
\tag{4.2}
\]

and all other triples have degree one.  Hence

\[
 \Phi=11=(2N-W)+1,
\]

where `N=15` and `W=20`.

The overload `145` is pivot-locked.  Its three incident diamonds are

\[
 (14,1345),\qquad(15,1245),\qquad(45,1456),
\]

and their other middle endpoints `134,125,456` all have degree one.

There are exactly eleven legal rectangles.  Their complete delta list is

\[
 1,1,1,1,\quad 2,2,2,2,2,\quad 3,3.
\tag{4.3}
\]

For hand verification, the row pairs grouped by delta are

\[
\begin{array}{c|l}
\Delta\Phi&\text{lower-row pairs}\\ \hline
1&(12,13),(34,46),(25,26),(35,56)\\
2&(12,24),(23,34),(14,45),(16,56),(26,36)\\
3&(14,15),(15,45).
\end{array}
\tag{4.4}
\]

The checker recomputes every old and new load rather than relying on this
summary.  Equations (4.3)--(4.4) prove that the matching is a **strict**
rectangle-local minimum with maximum load three.  Therefore neither `Phi`
nor the overload potential can support a monotone rectangle-only proof.

## 5. One alternating six-cycle repairs the strict trap

Consider the three selected rows

\[
 12\mapsto1234,\qquad
 13\mapsto1235,\qquad
 14\mapsto1345.
\]

Cyclically reassign their upper sets as

\[
 12\mapsto1235,\qquad
 13\mapsto1345,\qquad
 14\mapsto1234.
\tag{5.1}
\]

All three new containments are valid, so (5.1) is one alternating six-cycle
in the lower--upper incidence graph.  The only net middle-load changes are

\[
 d(123):2\to1,\qquad d(145):3\to2,
\]

\[
 d(125):1\to2,\qquad d(134):1\to2.
\tag{5.2}
\]

Thus

\[
 \Phi:11\to10,\qquad \Delta(G):3\to2.
\tag{5.3}
\]

This establishes that six is the first necessary alternating-cycle length
for monotone convex descent: four-cycles alone are insufficient even in the
first nontrivial case, while a six-cycle escapes the strict trap directly.

## 6. Exact small-dimensional classification

The programs

* `scratch/rectangle_load_checker.py`, and
* `scratch/rectangle_load_exhaust_m3.cpp`

give the following exact census.

For `m=2` there are nine colour-perfect matchings.  Six have
`Phi=2,max d=2`; the other three have `Phi=4,max d=2` and an improving
rectangle.  There is no overload because every middle load is at most
`m=2`.

For `m=3` there are exactly

\[
 3,013,854
\]

colour-perfect matchings.  Among them:

* `308,724` are rectangle-local for `Phi`;
* `99,480` rectangle-local matchings have maximum load three;
* `5,160` are strict overloaded rectangle-local minima;
* the strict traps split into `2,880` with load profile
  `3^1 2^8 1^11` and `2,280` with profile `3^2 2^6 1^12`;
* **every one** of the `99,480` overloaded rectangle-local matchings has an
  alternating six-cycle that lowers `Phi` without increasing the maximum
  load.

The last statement is an exhaustive finite theorem for `m=3`, not an
all-dimensional proof.  The enumeration ignores acyclicity.

## 7. Four-or-six fails at `m=4`; an eight-cycle repairs it

Order each layer of the eight-cube by increasing binary mask.  The following
column vector specifies a perfect matching: its `i`th entry is the zero-based
index of the upper set assigned to the `i`th lower set.

```text
7 1 38 29 15 4 2 9 0 45 27 31 26 13 12 35 18 5 54 3 6 16 48 8
19 39 40 17 10 44 11 46 14 55 20 23 22 21 37 50 51 24 25 42 43 28
34 32 33 30 41 36 47 49 53 52
```

The deterministic certificate checker verifies all of the following.

* It is a permutation of all `56` upper colours and every assigned
  containment is valid.
* Its load profile is

  \[
  3^1\,2^{40}\,1^{29},
  \]

  with unique overload `1246`, maximum load three, and `Phi=43`.
* It has `43` legal rectangles.  Their delta histogram is

  \[
  0^6\,1^{22}\,2^{10}\,3^5;
  \]

  in particular, none decreases `Phi`.
* Its matched-row exchange digraph has `250` directed triangles.  The
  minimum `Delta Phi` among all of them is zero.

Thus it is a joint local minimum under all alternating cycles of lengths
four and six while its maximum middle load is still three.  This is an
exact counterexample to the four-or-six augmentation conjecture.

The directed four-cycle on zero-based lower-row indices

\[
 (0,1,35,26)
\tag{7.1}
\]

is improving.  In set notation it cyclically changes

\[
\begin{array}{c|c|c}
\text{lower}&\text{old upper}&\text{new upper}\\ \hline
123&12357&12346\\
124&12346&12458\\
128&12458&12578\\
157&12578&12357.
\end{array}
\tag{7.2}
\]

This is an alternating eight-cycle in the original lower--upper incidence
graph.  It changes `Phi:43->42` and the maximum load `3->2`.

The net load changes are

\[
\begin{array}{c|rrrrrrrr}
X&1235&1245&1236&1246&1237&1357&1278&1578\\ \hline
\Delta d(X)&-1&+1&+1&-1&-1&+1&+1&-1.
\end{array}
\tag{7.3}
\]

This example makes the progression sharp through four dimensions:
rectangles can be trapped at `m=3`, and rectangles plus directed triangles
can be trapped at `m=4`.

## 8. The corrected augmentation target

Fix a colour-perfect matching `P`.  Make an auxiliary directed graph on its
selected diamonds: put an arc `e_i -> e_j` when the lower colour of `e_i`
is contained in the upper colour of `e_j`.  A directed simple cycle of
length `t` is exactly an alternating cycle of length `2t` in the original
bipartite graph, and cyclic reassignment of the upper colours is the
associated colour-preserving switch.

### Theorem 8.1 (a negative first-variation cycle always exists)

For `m>=2`, every colour-perfect matching has an alternating cycle whose
load-change vector `delta` satisfies

\[
 \sum_Xd(X)\delta(X)<0.
\tag{8.1}
\]

#### Proof

Give a diamond with middle endpoints `X,Y` the linear weight

\[
 w(XY)=d(X)+d(Y).
\]

The current perfect matching has total weight

\[
 \sum_Xd(X)^2.
\tag{8.2}
\]

The lower--upper incidence graph is
`D=binom(m+1,2)`-regular.  Its uniform fractional perfect matching assigns
weight `1/D` to every diamond and gives every middle vertex fractional load

\[
 \lambda=\frac{m^2}{D}=\frac{2m}{m+1}.
\]

Its linear cost under `w` is therefore

\[
 \lambda\sum_Xd(X).
\tag{8.3}
\]

The difference between (8.2) and (8.3) is

\[
 \sum_X(d(X)-\lambda)^2>0,
\]

because the mean load is `lambda` and `lambda` is nonintegral for `m>=2`.
The bipartite perfect-matching polytope is integral, so the uniform
fractional point is a convex combination of integral perfect matchings.
At least one of those matchings has smaller linear weight than the current
one.  Their symmetric difference is a disjoint union of alternating cycles;
linear cost is additive across those cycles.  At least one cycle has
negative cost change, which is (8.1).  QED.

The theorem does not yet give a decreasing **discrete** switch.  For one
alternating cycle,

\[
 \Delta\Phi
 =\sum_Xd(X)\delta(X)+\frac12\sum_X\delta(X)^2,
\tag{8.4}
\]

because `sum_X delta(X)=0`.  Thus the cycle must pay the nonnegative
quadratic integrality toll in (8.4).  The strict `m=3` trap and joint `m=4`
trap say precisely that all shorter cycles fail to have enough negative
first variation to pay this toll.

The computational result identifies the sharp next statement.

### Bounded-order augmentation conjecture

If a colour-perfect diamond matching has a middle load at least three, then
there is a directed simple cycle in its matched-row exchange graph of order
at most `m` whose alternating switch lowers `Phi` without increasing the
maximum load.

Repeated application would terminate because `Phi` is a nonnegative
integer.  If termination always has maximum load at most two, this proves
the orthogonal two-SDR lemma.

The conjecture is exact for `m<=3`: there is no overload for `m<=2`, and the
`m=3` statement follows from the exhaustive census.  At `m=4`, the exact
certificate above shows that order four can really be required.

The sampler `scratch/bounded_cycle_load_sampler.cpp` stops as soon as
maximum load two is reached, so it does not count irrelevant convex cleanup
after the degree target is already solved.  With seed `20260723` it gives:

* `100,000/100,000` solved trials at `m=4`, including `1,623` improving
  order-four switches taken while the current maximum exceeded two;
* `10,000/10,000` solved trials at `m=5`, including `120` improving
  order-five switches taken only after all shorter orders failed.

These are randomized data, not existence proofs.  They do show that the
order-`m` cutoff is not an artificial weakening made only to accommodate
the `m=4` certificate: the same greedy protocol encounters genuine
order-five local traps at `m=5`.

There are two mathematically credible ways forward.

1. **Pivot-release path lemma.**  Start from a pivot-locked overload and
   follow upper-colour reassignments that remove one incidence at the pivot.
   Prove that a first improving return occurs after at most `m` selected
   diamonds.  The exact `m=3,4,5` behavior suggests that the available
   deleted coordinates, rather than a fixed cycle length, control the
   return time.
2. **Negative-cycle duality.**  Weight exchange arcs by the marginal middle
   loads.  Show that the uniform fractional matching forces a negative
   alternating cycle, then prove that a shortest admissible negative cycle
   can be shortened to order at most `m` in this Boolean incidence graph.

The shortening step is the real issue.  The strict `m=3` trap and the joint
`m=4` trap prove that no dimension-free bound of two or three can work.
Any valid argument must use the Boolean coordinate structure to explain the
dimension-dependent cutoff.

## 9. Corrected ledger

**Proved mathematically**

* the exact rectangle delta formula (2.1);
* the complete local inequalities (2.3)--(2.4);
* the rectangle-removability and pivot-lock criterion;
* an explicit strict overloaded rectangle-local matching at `m=3`;
* an explicit decreasing alternating six-cycle repairing that matching;
* an explicit overloaded matching at `m=4` local under every alternating
  cycle of lengths four and six;
* an explicit decreasing alternating eight-cycle repairing the `m=4` trap.

**Proved by exhaustive finite verification**

* the full `m=2` census;
* the full `m=3` census above;
* every overloaded rectangle-local `m=3` matching has a decreasing
  alternating six-cycle with nonincreasing maximum load.

**Open**

* the bounded-order augmentation conjecture for all `m`;
* whether order greater than `m` is necessary in some dimension;
* cycle elimination / acyclicity after maximum degree two is reached.

The practical conclusion is unambiguous: do not spend further effort trying
to prove strict rectangle descent or a universal four-or-six theorem.  The
correct local move language appears to contain alternating cycles whose
order grows with the dimension.
