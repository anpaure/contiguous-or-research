# Independent proof audit: run-transparent pair-cell squares

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_RUN_TRANSPARENT_PAIR_CELL_SQUARES_AND_EXCEPTIONAL_PORT_GATE_20260804.md`

## 1. Same-stratum square

For

\[
 x_0=P_p+q^0+R,\quad x_1=P_p+q^1+R,
\]

and

\[
 y_0=p^0+P_q+R,\quad y_1=p^1+P_q+R,
\]

the four symmetric differences are

\[
\begin{array}{c|c}
\text{edge}&\text{support}\\ \hline
x_0x_1&\{q^0,q^1\}\\
y_0y_1&\{p^0,p^1\}\\
x_0y_0&\{p^1,q^1\}\\
x_1y_1&\{p^0,q^0\}.
\end{array}
\]

So (2.3) is a genuine Johnson square and its two seams use opposite
physical members.  The second cube's complemented cut bit reverses its
local endpoint gauge while allowing both long opened paths to have the
same transition word `w`.  A retained common direction loses at most the
one distinguished cut position per period, so its gap drops by at most
one.  The cut pair itself is protected by the old gap to the nearest other
occurrence.  The bound `rho-1` is therefore correct.

The matching corollary is scoped correctly: because no cell participates
twice, there is no unpriced interaction among splice collars.

## 2. Cross-stratum correction

When a double pair `p` and empty pair `q` become singleton, the two square
seams use the same removed `p` member and the same added `q` member.  Both
pairs are active in the larger cube.  Hence the statement

> the seam occurrences are separated by the two long opened arcs

is insufficient: a `p`- or `q`-transition may occur on the first retained
large-cube edge.  The theorem correctly adds the missing large-side
`p,q` collar exclusion.

For an unchanged common pair, the seam itself creates no transition.
The only new short gap can straddle the seam, so disjoint inward direction
collars are a valid strong certificate.  The proof of Theorem 3.1 checks
all coordinate classes.

For Corollary 3.2, each two-sided collar union has size at most `2L-2`.
After reserving the cut direction, `m>=4L` leaves at least `2L-1` common
labels outside the small-side collar union.  This accommodates the entire
large-side collar union.  The two extra large-cube directions `p,q` can be
chosen outside its own collar union.  The counting is conservative but
valid.

## 3. Small-cell obstruction and port degrees

Every Johnson triangle is `K+u,K+v,K+w`; at the middle vertex its unique
extra coordinate changes twice consecutively.  Thus the claimed pulse-one
obstruction applies to the naive `Q_0` triangle ear and to the analogous
endpoint attachment of `Q_1`.  It does not exclude longer buffered ears,
and the theorem does not claim that it does.

For the incidence between singleton strata `m` and `m+2`, the lower degree
is

\[
             t\cdot t\cdot2\cdot2=4t^2,
\]

and the upper degree is the number of ordered distinct singleton-pair
choices,

\[
             (m+2)(m+1).
\]

The double-clone Hall argument under ratio at least two is exact.  Its
scope is explicitly only abstract owner ports.

## 4. Scope verdict

**PASS**, with the following nonclaims essential:

1. no multiport or spanning-tree splice theorem is proved;
2. no resident absorption of all `m=0,1` owners is proved;
3. the automatic cross-stratum range is `m>=4L`, not the critical
   `m=L+O(log r)` range;
4. no immediate-palette, arbitrary-upper, or lower-compiler property is
   inferred.

The theorem therefore gives a proof-safe local residence advance and a
sharp statement of the remaining occurrence-labelled buffer gate.

