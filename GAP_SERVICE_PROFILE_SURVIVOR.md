# A coherent multiscale survivor of the scalar-gap/full-line ledgers

## 1. Outcome

**Status correction.**  The process below really is a survivor of the
listed scalar marked ledgers, but its concrete finite realization is now
known to admit a direct bounded-congestion run assignment of cost

\[
                       Q\le {7\over2}a^3+O(a^2).
\]

It therefore does **not** survive the full heterogeneous run-cover theorem.
See `GAP_SERVICE_PROFILE_SURVIVOR_AUDIT.md`.  The remainder of this file is
retained because it is the exact counterexample to the scalar relaxation
that exposed the missing service information.

The full selected-line coarea law, additive threshold contraction, scalar
gap lengths, and absorbed-edge lifetimes still do not close the general
three-box seam method.  There is one nested two-direction marked process
satisfying all of those recorded laws with

\[
\boxed{\inf_{1<c<2}U(c)={389\over84}=4.63095\ldots>4.}      \tag{1.1}
\]

The process is not claimed to be a counterexample to the local three-box
theorem.  Its contracted gaps hide cheaper internal runs which the scalar
gap mark `z` forgets.  Thus it isolates the next necessary state variable: a
gap internal-run **service profile**.

## 2. Bottom marked-line template

Use only the `x`- and `y`-direction lines with positive levels

\[
S_x=S_y=[0,1],\qquad S_z=\varnothing.
\]

Assign the line at level `t` the plateau length

\[
s(t)=
\begin{cases}
2-2t,&0\le t\le1/2,\\
1,&1/2\le t\le1.
\end{cases}                                                 \tag{2.1}
\]

Pair reflected parameters so that `p(t)=s(1-t)` and alternate the two fixed
directions.  Insert normalized complement-gap mass `1/2` before every long
member.

The formal bottom ledger has

\[
f=2,qquad \ell={5\over2},qquad
\tau=1,qquad I={1\over2},qquad J=0,
\]

and therefore saturates the complete-line gate:

\[
\ell=2f-\tau-I={5\over2}.                                  \tag{2.2}
\]

The length-one separators disappear at every legitimate continuity
threshold `c>1`.  No conclusion below depends on treating them as retained
dangerous plateaux at `c=1`.

## 3. Static plateau packing is compatible with directed skips

The inherited definition of a directed plateau is a contiguous **word**
block whose points form a directed subsequence of one coordinate line.  The
varying coordinate is strictly monotone, but it may skip lattice levels.
Geometric interval contiguity on the line is not required.

In the positive `x/y` intersection triangle, assign an intersection `(t,u)`
to the `y`-plateau exactly when

\[
(t,u)\in Q:={t\ge1/2\}
 \cup\{t\le1/2,\ u\le t\}.                                  \tag{3.1}
\]

For a low `x`-level `t<=1/2`, the corresponding plateau consists of all
exclusive points with `y<0` together with the positive points `t<y<=1-t`.
Ordered by increasing `y`, this is a legal directed subsequence and has
normalized length

\[
1+(1-2t)=2-2t.
\]

The symmetric statement holds for low `y`-levels.  High levels use only
their exclusive negative half-line and have length one.  The rule (3.1)
partitions all selected-line intersections and all exclusive points, so the
plateau vertex sets are disjoint and attain (2.2).

This point is important: a proposed reciprocal geometric-interval kernel is
not an inherited constraint, because skipped levels are legal.

## 4. Exact contraction for every `c>1`

Order the long plateaux by length so that those deleted at a later threshold
form a terminal block, and use length-one separators between consecutive
long members.  Away from one negligible component join, deleting the
separators gives typical retained predecessor-successor data

\[
p=s,qquad z={3\over2}.                                     \tag{4.1}
\]

At threshold `c>1`, the retained length measure is

\[
\mu_c(ds)=1_{[c,2]}(s)\,ds.
\]

Consequently

\[
f(c)=2-c,qquad
\ell(c)=2-{c^2\over2},qquad
e(c)={ (2-c)^2\over2}.                                     \tag{4.2}
\]

The retained marked lines are

\[
\kappa_x=\kappa_y
=1_{[0,(2-c)/2]}(t)\,dt,qquad s=2-2t,
\qquad \kappa_z=0.                                         \tag{4.3}
\]

Writing `a_c=(2-c)/2`, their line terms are

\[
T(c)=a_c^2,qquad I(c)=a_c^2,qquad J(c)=0.
\]

Hence

\[
\ell(c)=2f(c)-T(c)-I(c)                                   \tag{4.4}
\]

at every threshold.  Every weighted complete-line coarea inequality is
therefore an equality.

The scalar contracted-gap mass is

\[
{3\over2}(2-c)
\le3-\ell(c),
\]

because

\[
3-\ell(c)-{3\over2}(2-c)
={ (c-1)(c+4)\over2}\ge0.                                 \tag{4.5}
\]

Declare no retained seam absorbed for `c>1`.  The absorbed-flow and common
absorbed-edge lifetime laws are then satisfied trivially.

## 5. Exact seam functional

For the retained process,

\[
H(c)={3\over4}(2-c)^2.                                     \tag{5.1}
\]

Also

\[
\phi(s,s,3/2)=
\begin{cases}
0,&s\le3/2,\\
(5/2-s)(s-3/2),&s>3/2.
\end{cases}                                                 \tag{5.2}
\]

For `1<c<=3/2`, (4.2), (5.1), and (5.2) give

\[
U(c)=3c+{7\over4}(2-c)^2-{1\over12}.                        \tag{5.3}
\]

Its minimum occurs at `c=8/7` and equals

\[
U(8/7)={389\over84}.                                       \tag{5.4}
\]

For `3/2<=c<2`, put `q=2-c`.  Then

\[
U(c)=6-{13\over4}q+{7\over4}q^2+{1\over3}q^3,              \tag{5.5}
\]

whose minimum on that interval is

\[
U(3/2)={233\over48}.                                       \tag{5.6}
\]

Equations (5.4)--(5.6) prove (1.1).

## 6. What the scalar gap has forgotten

Every contracted gap of normalized length `3/2` consists of two visibly
different pieces:

1. a deleted directed plateau of normalized cost one; and
2. a complement-wedge (cross-line-desert) chunk of normalized size `1/2`.

Both pieces remain potential sources of admissible internal threshold runs
after contraction.  Replacing them by the single scalar `z=3/2` discards:

- the distribution of internal run costs;
- how many safe starts each run can serve;
- their one-sided spans; and
- congestion when several starts use the same internal run.

The exact missing state is therefore a **gap service profile**: for each
contracted gap, the capacity of its internal avoiding runs indexed by cost
and safe-start interval, together with an additive/monotone merge law under
threshold contraction.

## 7. Former missing lemma, now proved for this template

A lemma sufficient to kill this survivor is:

> In the nested two-direction template above, the `a+o(a)` contracted gaps,
> each formed from one cost-`a` separator and `a/2+o(a)` desert positions,
> admit a bounded-congestion forward reassignment of enough starts to lower
> the aggregate first-dangerous cost by more than
> \[
> \left({389\over84}-4\right)a^3={53\over84}a^3.
> \]

The lemma holds with substantial room.  In every
`long -> separator -> desert -> next long` record, send starts in the long
block and desert to the cost-one separator, and send separator starts to the
next long run.  The maximum span is `7a/2+O(1)`, congestion is `O(a)`, and
the total cost is

\[
                         {7\over2}a^3+O(a^2).
\]

The recovered saving is `95/84`, larger than the required `53/84`.  Thus the
concrete template is closed independently of the internal desert ordering.
What remains open is a universal service theorem for arbitrary coherent
mixed profiles, not the service profile of this example.
