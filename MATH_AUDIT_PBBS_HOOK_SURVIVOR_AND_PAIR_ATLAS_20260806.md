# Audit of the hook survivor formula and complete pair atlas

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_PBBS_HOOK_SURVIVOR_ENVELOPE_AND_COMPLETE_PAIR_ATLAS_20260806.md`  
**Verdict:** **PASS** within the stated eventual range and dependency
scope.

## 1. Root/core identity

In the hook word, the terminal bank `(10)^z` contributes `2z` sites and
the rooted update contributes the following one site.  Direct iteration
of the same first-maximum factorization gives

\[
                         r'=r-(2z+1).
\]

The entrance label of the depth-`h-1` source cell is `r`; the `h`-step
exit deletion is `r-2z=r'+1`.  Thus the mandatory core is exactly
`{r,r-2z}`.  At `z=0` it is a loop; at `z=1` it is a distance-two pair.

Summing over the `p` rotated slots gives displacement

\[
 -(2b+p)=-(2m-1)=2\pmod{2m+1},
\]

so the corrected centered identity is `tau^p=rho^2`.

## 2. Survivor-envelope bijection

With terminal occupancy zero, write the nonterminal slot multiset as
`1<=c_1<=...<=c_b<=p-1`.  The physical free-leaf labels are

\[
                         w_i=c_i+2i.
\]

They satisfy

\[
 3\le w_1<\cdots<w_b\le n-3,
 \qquad w_{i+1}-w_i\ge2.
\]

The inverse formula `c_i=w_i-2i` has values in `[1,p-1]` and is
nondecreasing.  Hence the map is bijective.  Its count is

\[
 \binom{(2m-4)-b+1}{b}
 =\binom{m+d-2}{b}
 =\binom{m+d-2}{2d-1},
\]

exactly matching the independently established zero-terminal weak-
composition count.

## 3. Extension bound

The path on `{3,...,n-3}` has `2m-4` vertices and independence number
`m-2`.  If a prescribed independent set `Q` has `q` vertices, start from
a maximum independent set; inserting each missing prescribed vertex and
deleting its at most two old neighbours loses at most one vertex.  Thus a
superset of `Q` exists with size at least `(m-2)-q`.

For `q<=d-1`, this is at least `m-d-1=b`.  Deleting surplus vertices gives
an independent `b`-set containing `Q`.  This validates the exact loop-
ticket criterion and, in particular, all pair distances at least three.

## 4. Pair orbit ledger

* distance at least three: one loop cell, using the survivor extension;
* distance two: one `z=1` cell with mandatory core `{r,r-2}`;
* distance one: two consecutive `z=0` cells.  The root recurrence changes
  `r` to `r-1`, so their singleton union is `{r,r-1}`.

The two-cell changed block has length two and hence lies within the
short-gap theorem for `d>=2`.

## 5. Distinct-component supply

After the indicated terminal constraints, the remaining weak-composition
counts are the binomial coefficients displayed in Section 5 of the
theorem.  For a distance `q>=3`, fixing

\[
 (i,c_i)=
 \begin{cases}
 ((q-1)/2,1),&q\text{ odd},\\
 (q/2-1,2),&q\text{ even}
 \end{cases}
\]

makes `c_i+2i=q`.  The free nondecreasing suffix has the stated multiset
count.  Even at `q=m`, it has length `m/2-O(d)` and a value alphabet of
size `Theta(d)`, so the count is
`exp(Omega(d log(m/d)))`.  Dividing by the maximum `np` rooted
occurrences per component leaves more than `n^2` candidate components
eventually.

Greedy component-disjoint assignment to all `binom(n,2)` pair targets is
therefore valid.

## 6. Scope

The proof imports the exact rooted hook update, hook-component census,
and mandatory-core short-gap theorem.  It does not claim:

1. an atlas for ranks `3,...,d`;
2. residence outside the selected hook components;
3. a global component join/opening;
4. a terminal common cap; or
5. the additive-constant conjecture.

Within this scope, rank two is closed without owner rethreading.
