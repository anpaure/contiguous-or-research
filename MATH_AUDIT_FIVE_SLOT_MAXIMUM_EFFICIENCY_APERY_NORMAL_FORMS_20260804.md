# Independent audit: five-slot maximum-efficiency Apéry normal forms

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FIVE_SLOT_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md`  
**Method:** independent residue-walk derivation and branch-by-branch
transient accounting.  No numerical search is used.  
**Verdict:** **PASS** as an exact reduction; no five-slot positivity claim is
made.

## 1. Scope and first crossing

The first-crossing theorem has the correct comparison direction: after the
first generator at or above `A`, deletion lowers all later Bellman values
but keeps them in the increasing Gaussian tail.  Therefore it cannot
increase the functional.  Complete positivity through four slots then
implies that a five-slot counterexample, if one exists, has

\[
 c_1,c_2,c_3,c_4<A\le c_5.
\]

Internal superadditivity gives `c_2>=2c_1`, so size one need not be a
separate maximum-efficiency branch.  The four branches `h=2,3,4,5` are
exhaustive, including ties.

## 2. Exact availability-filtered path identity

Fix a maximizing size `h`, set `lambda=c_h/h`, and give denomination `j`
reduced weight `d_j=c_j-j lambda<=0`.  An exact fill of capacity `m` is a
walk on `Z/hZ` ending at `m mod h`.

If a residue vertex repeats, deleting the intervening segment:

1. removes a nonnegative capacity divisible by `h`;
2. does not decrease reduced weight, since every `d_j<=0`;
3. leaves a simple path whose capacity is at most `m`.

Conversely, an available simple path can be padded to capacity `m` by
size-`h` generators, because its capacity has the same residue as `m` and
each padding generator has zero reduced weight.  Hence

\[
 V_m=\lambda m+
 \max\{d(Q):Q\text{ simple},\ \ell(Q)\le m\}
\]

is exact at every capacity, not only eventually.

Zero-weight cycles caused by tied maximizers do not create a gap: deleting
them preserves rather than increases reduced weight, and size-`h` padding
restores their total capacity.  Thus the theorem does not need the gcd of
all maximizing indices.

## 3. Stabilization and finite-head count

A simple path on `h` residues has at most `h-1` edges.  The largest allowed
edge capacity is five unless `h=5`, when it is four.  Therefore

\[
 (L_2,L_3,L_4,L_5)=(5,10,15,16).
\]

For `m>=L_h`, every simple witness is physically available.  The formal
lattice then equals the true clock term by term.  Subtracting the formal
lattice only for `m<L_h` proves the finite-head formula exactly.

The shift bounds are also correct.  The path of `r<h` size-one steps is
simple and gives `s_r>=r c_1>=0`; nonpositive reduced weights give
`s_r<=r lambda<h lambda=c_h`.  Thus every shift lies in the stated
fundamental interval.

## 4. Independent audit of the `h=2` branch

Write `(c_1,...,c_5)=(x,y,z,w,T)` and

\[
 s=T-2y.
\]

The asserted inequalities follow independently as

\[
 z\ge x+y,
 \qquad T\ge y+z,
 \qquad T\le {5y\over2},
 \qquad 2y\le w\le2y.
\]

Thus `x<=z-y<=s<=y/2` and `w=2y`.

Modulo two, the only simple nonzero-residue witness is one odd
denomination.  The size-five reduced weight dominates size three because
`T-y>=z`, and dominates size one because `T-2y>=x`.  It becomes available
at capacity five.  Hence the only mismatches with the eventual odd lattice
are

\[
 V_1=x\quad\text{instead of }s,
 \qquad
 V_3=z\quad\text{instead of }y+s.
\]

This gives exactly the two corrections in the theorem.  No size-four
transient is missing because internal superadditivity and maximal
efficiency force `c_4=2c_2`.

## 5. Independent audit of the `h=3` branch

Put `p=c_3`, `a=c_4-p`, and `b=c_5-p`.  The best residue-one step is size
four and the best residue-two step is size five, because

\[
 c_4\ge p+c_1,
 \qquad c_5\ge p+c_2.
\]

The two simple path types to each nonzero residue give

\[
 s_1=\max\{a,2b-p\},
 \qquad s_2=\max\{b,2a\}.
\]

The double size-five witness for residue one has capacity ten; the double
size-four witness for residue two has capacity eight.  Direct inspection
before those thresholds gives

\[
 V_7=\max\{p+c_4,c_5+c_2\},
 \qquad
 V_8=\max\{2c_4,p+c_5\}.
\]

All other partitions are dominated by these candidates using internal
superadditivity and the fact that size four dominates size one while size
five dominates size two in reduced weight.  The residue-one corrections
occur at capacities `1,4,7`; the residue-two corrections occur at `2,5`.
That is exactly the five-pulse formula.  Multiples of three are always
`q p` by maximal efficiency and size-three attainment.

## 6. Independent audit of the `h=4` path list

Let `P=c_4` and `e=c_5-P`.  Since `c_5>=c_4+c_1`, the eventual
residue-one edge of size five dominates the edge of size one.  After this
dominance reduction there is one best edge of each nonzero residue, with
weights `d_1,d_2,d_3` from the theorem.

For a fixed nonzero target in `Z/4Z`, a simple path is direct, has one of
two possible intermediate vertices, or has both intermediate vertices in
one of two orders.  The two one-intermediate orders have the same sum of
edge weights.  Enumerating the distinct sums yields

\[
\begin{array}{c|l}
1&d_1, d_2+d_3, d_1+2d_2, 3d_3,\\
2&d_2, 2d_1, 2d_3, d_1+d_2+d_3,\\
3&d_3, d_1+d_2, 3d_1, 2d_2+d_3.
\end{array}
\]

These are exactly the twelve forms displayed.  Three size-five steps give
the largest possible capacity fifteen.  The theorem correctly retains
all capacities below fifteen through the availability filter, including
the early size-one edge before size five is available.

## 7. Independent audit of the `h=5` path count

For `h=5`, each nonzero residue difference has a unique denomination in
`{1,2,3,4}`.  A simple path from zero to a fixed nonzero residue is
determined by an ordered list of distinct intermediate vertices selected
from the other three nonzero residues.  Its possible numbers of
intermediate vertices are `0,1,2,3`, so the exact count is

\[
 1+3+6+6=16.
\]

Every such path has at most four edges of capacity at most four, giving
the stabilization threshold sixteen.  Thus the endpoint-efficient branch
really is four maxima of sixteen linear forms plus the exact head at
capacities `0,...,15`.

## 8. Boundary of the result

The reduction is finite and exact, but none of the remaining Gaussian
gates is signed here.  In particular:

* the two- and three-efficient pulse corrections need not be discarded;
* the `h=4` and `h=5` maxima remain piecewise-defined;
* no conclusion about five-slot positivity follows without new Gaussian
  inequalities.

**Final verdict: PASS.**  The theorem is a complete exact normal-form
reduction for `n=5`, with every finite transient retained.  It does not
prove the universal Bellman inequality or `nu(k)<=B(k)+O(1)`.
