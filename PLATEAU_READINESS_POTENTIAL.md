# A readiness potential on constant-Phi diamond plateaux

## Status

Strict one-move convex descent needs exchange cycles of orders three, four,
and five in the frozen examples at `m=3,4,5`; see
`NEGATIVE_CYCLE_DUALITY_AUDIT.md`.  That does not rule out a bounded move
language if neutral moves are allowed.

This note identifies a concrete secondary potential which exactly explains
the certified neutral escapes at `m=4,5` and survives a substantial
adversarial test.

At a rectangle-local overloaded matching, let `r_j` be the number of legal
rectangles which remove an incidence from a current maximum-load middle
vertex and have exact potential change `j`.  Compare the finite vector

\[
 \mathcal R(P)=(r_{2-2D},r_{3-2D},\ldots,r_{2+2D})             \tag{0.1}
\]

lexicographically, preferring the larger vector, where `D=max_X d(X)`.
Call this the **relief-readiness word**.

On the frozen paths its cheapest relief cost evolves as

\[
 m=4:\quad1\longrightarrow0\longrightarrow-1,
 \qquad
 m=5:\quad0\longrightarrow-1.                                \tag{0.2}
\]

All arrows in (0.2) are neutral rectangles.  The next rectangle strictly
decreases `Phi` and leaves maximum load two.

The exact all-`m` readiness alternative is not proved.  Deterministic tests
find no counterexample among 7,700 independently generated rectangle-local
states at `m=4,5` (two seeds, 7,000 at `m=4` and 700 at `m=5`): every
overloaded state either has a max-safe decreasing rectangle/triangle or a
max-safe neutral rectangle/triangle which increases (0.1).  This is evidence,
not a theorem.

Several simpler secondary-potential classes fail rigorously on the two
frozen paths.  In particular, no potential depending only on the middle-load
histogram can move at all; degree assortativity wants opposite orientations
at `m=4` and `m=5`; and immediate overload-to-leaf distance is non-strict.

## 1. Definition and finite range

Let `P` be a colour-perfect diamond matching and `d(X)` its projected middle
load.  A rectangle trade has old secondary vertices `P,Q`, new secondary
vertices `R,T`, and

\[
 \Delta\Phi=d(R)+d(T)-d(P)-d(Q)+2.                            \tag{1.1}
\]

Let

\[
 \mathcal O(P)=\{X:d(X)=D\},\qquad D=\max_Xd(X).
\]

A rectangle is a **relief rectangle** if its load-change vector `eta`
satisfies

\[
 \eta(X)<0\quad\hbox{for some }X\in\mathcal O(P).             \tag{1.2}
\]

For every integer `j`, let `r_j(P)` count relief rectangles with exact change
`j`.  Since all current loads lie in `[0,D]`, (1.1) lies in
`[2-2D,2+2D]`; this gives the finite word (0.1).

On a rectangle-local state all negative entries of (0.1) vanish.  Increasing
`r_0` creates more neutral ways to move a maximum-load token; after a neutral
move, a positive `r_{-1}` exposes a strict exit.  Lexicographic order captures
both effects without choosing a distinguished overloaded vertex.

## 2. Two rigorous local facts

### Lemma 2.1 (preparation identity)

Let `A` be a legal relief rectangle at `P`, and let `B` be a neutral
rectangle producing `P'`.  Suppose `A` remains a legal rectangle with the
same four secondary vertices after `B` (for example, the two trades have
disjoint lower and upper colours).  If `eta_B` is the load change of `B`,
then

\[
 \Delta_{P'}\Phi(A)-\Delta_P\Phi(A)
 =\eta_B(R)+\eta_B(T)-\eta_B(P)-\eta_B(Q).                    \tag{2.1}
\]

#### Proof

Apply (1.1) before and after `B` and subtract.  QED.

Thus a neutral trade which moves one unit away from a prospective new
secondary vertex of `A`, without an offsetting signed change on the other
three vertices, reduces the exact cost of `A` by one.  This is precisely what
the two neutral `m=4` rectangles do: they prepare the two new secondary
vertices of the final relief rectangle one at a time.

Call a matching **safe-rectangle-local** if it has no rectangle which both
decreases `Phi` and does not increase the current maximum load.

### Lemma 2.2 (conditional termination)

Assume the following local alternative holds in a fixed dimension `m`:

> Every overloaded safe-rectangle-local matching either has a max-safe
> decreasing directed triangle, or has a max-safe neutral
> rectangle/triangle which decreases the maximum load or, at fixed maximum
> load, strictly increases `mathcal R`.

Then repeated rectangles and directed triangles reach maximum middle load at
most two.

#### Proof

First apply max-safe decreasing rectangles until safe-rectangle-local.  At
fixed `Phi`, a neutral step either lowers the nonnegative integer maximum load
or, at fixed maximum, strictly raises the readiness word.  There are finitely
many perfect matchings and finitely many possible readiness words, so neutral
steps cannot continue forever or cycle.  A max-safe decreasing triangle must
eventually occur.  It lowers the nonnegative integer `Phi`.  Restart.

If the process terminated while still overloaded, it would be
safe-rectangle-local and would violate the assumed alternative.  Hence it
ends at maximum load at most two, and the maximum never increases.  QED.

This lemma would prove the non-acyclic orthogonal two-SDR theorem if the local
alternative were established for every `m`.  Acyclicity remains separate.

## 3. Exact behaviour of the frozen paths

The checker `scratch/check_plateau_readiness.py` recomputes the following
data from the full matchings.

### The `m=4` path

The successive relief histograms have cheapest costs

\[
 1,\quad0,\quad-1.
\]

The two neutral rectangles have successive global statistics

\[
\begin{array}{c|ccc}
 &P_0&P_1&P_2\\ \hline
 \sum_{XY\in E}d(X)d(Y)&173&172&171\\
 \sum_{XY\in E}|d(X)-d(Y)|&26&28&30\\
 \#\{\hbox{leaf--leaf selected edges}\}&3&2&1.
\end{array}                                                    \tag{3.1}
\]

The unique overload's selected-graph distance to a leaf remains one at all
three stages.

### The `m=5` path

The cheapest relief cost changes from zero to `-1` in one neutral rectangle.
That rectangle moves the unique overload from one middle vertex to another.
The corresponding statistics are

\[
\begin{array}{c|cc}
 &P_0&P_1\\ \hline
 \sum_{XY\in E}d(X)d(Y)&681&683\\
 \sum_{XY\in E}|d(X)-d(Y)|&74&74\\
 \#\{\hbox{leaf--leaf selected edges}\}&7&7.
\end{array}                                                    \tag{3.2}
\]

Equations (3.1)--(3.2) give immediate adversarial audits of natural choices:

* any symmetric separable load moment `sum_X f(d(X))` is constant, because
  every neutral step preserves the complete load histogram;
* degree assortativity decreases at `m=4` and increases at `m=5`, so neither
  orientation works on both;
* edge-gradient, leaf counts, and overload-to-leaf distance are non-strict
  on at least one path.

The readiness word is the first tested local statistic which is strict in
the same orientation on every frozen neutral step.

## 4. Rectangles alone still do not suffice for readiness

There is an explicit `m=4` rectangle-local matching of profile

\[
 1^{29}2^{40}3^1
\]

and `Phi=43` with these properties:

* it has nine neutral rectangles;
* its relief histogram is exactly `r_1=1`;
* every one of the nine neutral rectangles leaves that histogram unchanged;
* no rectangle decreases `Phi`;
* the neutral directed triangle `(0,5,21)` changes the relief histogram to
  `r_0=1`.

The full 56-column matching is frozen in the checker as
`P4_RECTANGLE_READINESS_TRAP`.  This is a concrete counterexample to a
rectangle-only readiness theorem.  It also explains why directed triangles
belong in the plateau language even though many sampled states need only
rectangles.

The same matching has no decreasing directed triangle at the initial state;
the triangle is useful precisely because it is neutral and prepares a later
rectangle.

## 5. Adversarial sampling

For each trial, the checker:

1. generates a perfect lower--upper matching by randomized augmenting paths;
2. exhausts strictly decreasing rectangles;
3. if the result is overloaded, enumerates every directed simple cycle of
   orders two and three;
4. accepts only a max-safe strict descent or a max-safe neutral move which
   strictly raises (0.1).

The default deterministic run gives

\[
\begin{array}{c|r|r|r|r}
m&\text{trials}&\text{already solved}&\text{direct descent}&
\text{readiness step}\\ \hline
4&2000&412&79&1509\\
5&200&0&0&200.
\end{array}                                                    \tag{5.1}
\]

A second run with seed `47` gives

\[
\begin{array}{c|r|r|r|r}
4&5000&1047&203&3750\\
5&500&0&2&498.
\end{array}                                                    \tag{5.2}
\]

There are no failures in (5.1)--(5.2).  The earlier exhaustive `m=3` census
already proves that every overloaded rectangle-local matching has a
decreasing directed triangle, so the local alternative holds there without
using readiness.

Sampling cannot prove the all-dimensional alternative.  It does show that
the readiness word survives exactly the adversarial population on which the
strict four-or-six conjecture failed.

## 6. Correct next lemma

The most targeted local theorem is now:

### Rectangle-triangle readiness conjecture

Every overloaded safe-rectangle-local colour-perfect diamond matching has
either

1. a max-safe decreasing directed triangle, or
2. a max-safe neutral rectangle or directed triangle which lowers the
   maximum load or, at fixed maximum, strictly increases the
   relief-readiness word (0.1).

By Lemma 2.2 this implies maximum middle load at most two in every dimension.
It is compatible with all exact certificates through `m=5`, unlike the
one-step four-or-six conjecture.

A proof must use more than the immediate selected neighbourhood of an
overload.  The first `m=4` neutral steps leave that neighbourhood unchanged
while altering the loads on *prospective* new secondary vertices.  Formula
(2.1) identifies the right objects: signed intersections between a neutral
trade and the four secondary vertices of currently cheapest relief
rectangles.

The remaining proof problem is to show that if no such signed preparation is
available, then the cheapest relief rectangles and the overloaded stars
force a decreasing triangle.  The fixed rectangle-only trap shows that
triangles cannot be removed from this statement.
