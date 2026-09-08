# Independent audit of `LINE_WORD_MULTILAYER_EXTENSION.md`

## Verdict

The six substantive claims in the note are correct:

1. the (2q(m+1)(2m+1)) shallow-slice extension;
2. the orientation-free pair-line criterion and the hard-family constant
   (1/12);
3. the complementary-pair fibre-tiling capacity;
4. the seam-local mixed-orientation lower bound;
5. the same-pair length-at-most-two atom run; and
6. the lower-band requirement (d\ge(3/4-o(1))m).

I found no off-by-one error or false implication in the stated theorems.
Two scope qualifications should be made explicit in the source:

* the sentence preceding (5.4) must assume not only (D^dA=T), but also
  that (A) covers every nonzero target below rank (R); the derivative
  equation alone does not imply lower universality;
* the conclusion after (3.14) concerns a word whose rank-(R) spine is the
  displayed complete-line tiling.  It bounds witnesses internal to its line
  blocks and forces the other upper targets to use cross-block intervals;
  it does not constrain a construction which separately appends literal or
  unrelated auxiliary entries.

These are presentation repairs, not changes to any quantitative conclusion.

## 1. Shallow-slice construction

For a rank-(R+s) target in the balanced box, the line criterion is

\[
 y_1,y_2\ge s.
\]

If it fails and (s\le q), one of (y_1,y_2) is an integer in
({0,\ldots,q-1}).  A universal three-box word embedded in that constant
coordinate slice witnesses the target without using an interval that
crosses a concatenation seam.

The audited three-box hook word has nonzero length

\[
 (m+1)(2m+1)-1.
\]

For a positive fixed coordinate, its omitted local origin is a nonzero
slice target and costs one additional literal position.  For the zero slice
it remains the omitted global origin, so the same quantity

\[
 G_m=(m+1)(2m+1)
\]

is a valid uniform upper bound.  There are exactly (2q) appended slices.
Thus (2.5) follows, including the endpoints (q=0) and (q=m).  Since
(qG_m=O(qm^2)), the error is (o(m^3)) exactly when (q=o(m)).

## 2. Pair criterion and the (1/12) hard volume

Let (|y|=R+s).  If (y_i,y_j\ge s), then

\[
 y-se_i\quad\hbox{and}\quad y-se_j
\]

are rank-(R) points on the same coordinate-({i,j}) line, and the
maximum of the segment between them is (y).  Conversely, a segment of
span (s) has maximum with both varying coordinates at least (s).  This
proves Lemma 3.1 with no missing boundary case.

Put (u_i=m-y_i), (U=\sum u_i), and sort
(u_1\le u_2\le u_3\le u_4).  Since (s=2m+1-U),

\[
 y_i\ge s\iff U-u_i\ge m+1.
\]

The triple sums (U-u_i) are decreasing in this sorted order.  At most one
is at least (m+1) iff the second largest satisfies

\[
 U-u_2=u_1+u_3+u_4\le m.
\]

This inequality also implies (U\le m+u_3\le3m/2), hence (s\ge0);
there is no separately omitted rank condition.

After scaling by (m), the ordered polytope is

\[
0\le u_1\le u_2\le u_3\le u_4,
\qquad u_1+u_3+u_4\le1.
\]

Its volume is

\[
 \int_0^{1/3}\int_{u_1}^{(1-u_1)/2}
 (u_3-u_1)(1-u_1-2u_3)\,du_3\,du_1
 =\frac1{288}.
\]

Multiplying by (4!) gives (1/12).  Ties and facets have dimension at
most three, hence contribute (O(m^3)).  Theorem 3.2 is therefore correct.

## 3. Complementary-pair fibre tilings

At fixed (q=x_3+x_4), the rank-(R) slice really is the complete grid
(A_q\times B_q).  A complete ({1,2})-line is a row and a complete
({3,4})-line is a column.  Since every row meets every column, a
disjoint complete-line partition of one nonempty slice cannot mix the two
orientations.

The cardinalities are

\[
(a_q,b_q)=
\begin{cases}
(q+2,q+1),&0\le q\le m-1,\\
(2m-q,2m-q+1),&m\le q\le2m-1.
\end{cases}
\]

A row tiling has (b_q\binom{a_q+1}{2}) internal intervals, while a
column tiling has (a_q\binom{b_q+1}{2}).  Taking the larger and summing
the symmetric halves gives

\[
2\sum_{t=0}^{m-1}\frac{(t+1)(t+2)(t+3)}2
=\sum_{n=1}^{m}n(n+1)(n+2)
=\frac{m(m+1)(m+2)(m+3)}4.
\]

Thus the (m^4/4+O(m^3)) capacity statement is exact.  Since the upper
half contains (m^4/2+O(m^3)) targets and one physical interval has only
one maximum, at least (m^4/4-O(m^3)) targets must use intervals crossing
line-block boundaries, conditional on this tiling being the chosen spine.

## 4. Seam-local counting

A seam between blocks of lengths (a,b\le m+1) has exactly (ab)
crossing suffix-prefix intervals, hence at most ((m+1)^2) different
crossing maxima.

For completeness, the sharper same-pair count is valid.  In the varying
coordinates, a suffix maximum is of one of the forms

\[
(h,x)\quad\hbox{or}\quad(x,h),
\]

and a prefix maximum has the analogous form.  If their fixed-high
coordinates agree, their join fixes that coordinate.  If they differ,
say the fixed heights are (h_1<h_2), every value in the coordinate whose
opposite block has height (h_1) is at most (h_1<h_2); that coordinate
is fixed by (h_2), and only the other coordinate can vary.  The transverse
coordinates are fixed throughout both blocks.  Hence at most (m+1)
different maxima occur across a same-pair seam.

An internal line interval cannot represent a hard-family member.  Charging
one chosen seam-local witness for each hard target to its crossed seam gives

\[
|\mathcal H_m|\le p(m+1)^2+(B-1-p)(m+1).
\]

When (B=O(m^2)), the second term is (O(m^3)).  Combining this with
(|\mathcal H_m|=m^4/12+O(m^3)) gives

\[
p\ge(1/12-o(1))m^2.
\]

This proves only a seam-local obstruction; the source correctly leaves
long intervals crossing complete intermediate blocks outside its scope.

## 5. Same-pair atom-run obstruction

Write a nontrivial line's varying-coordinate endpoints as
((\ell,h)) and ((h,\ell)), with (ell<h).

For two lines in the same orientation, the outgoing peak atom of the first
would fail to terminate at the seam only if (ell_2\ge h_1).  The incoming
peak atom of the second would fail to begin there only if
(ell_1\ge h_2).  Both inequalities would give

\[
\ell_2\ge h_1>\ell_1\ge h_2>\ell_2,
\]

which is impossible.  Thus one of the two atoms has a singleton internal
run.

For opposite orientations, the relevant peak atoms lie in the same
coordinate.  Unequal peak heights give a singleton run at the larger peak;
equal heights give a run consisting exactly of the last vertex of the first
line and the first vertex of the second.  Nontriviality supplies an absent
neighbor on both sides, so the run is internal and has length two.

The direct line portion has ((m+1)^2-1) blocks and exactly two singleton
blocks.  For (m\ge2), every ordering therefore contains adjacent
nontrivial blocks.  A (D^d) image has no internal positive atom run shorter
than (d+1), so it cannot equal this intact fixed-pair spine for (d\ge2).

## 6. Lower-band delay

The exact number of nonzero targets below (R=2m-1) is

\[
L_m=\frac{(m+1)^4-3M_m}{2}+m
=\frac12m^4+O(m^3).
\]

Here symmetry gives

\[
\sum_{j=0}^{2m-2}|(P_m)_j|
=\frac{(m+1)^4-M_m}{2}-|(P_m)_{2m-1}|,
\]

and (|(P_m)_{2m-1}|=M_m-(m+1)); subtracting the zero target yields the
displayed formula.

Now explicitly assume that (A), of length (N_0+d), both satisfies
(D^dA=T) and covers all these lower targets.  Every interval of (A) of
length at least (d+1) contains a derivative window, whose maximum has
rank at least (R).  Hence every lower target uses one of

\[
\sum_{\ell=1}^{d}(N_0+d-\ell+1)
=dN_0+\frac{d(d+1)}2
\]

short intervals.  Since (N_0=(2/3+o(1))m^3), the inequality

\[
L_m\le dN_0+\frac{d(d+1)}2
\]

implies (d\ge(3/4-o(1))m): if (d\) is superlinear this is immediate,
and if (d=O(m)), the quadratic term is lower order and comparison of the
leading coefficients gives (1/2\le(2/3)(d/m)+o(1)).

This is incompatible with the intact-spine factorability condition
(d\le1) for all sufficiently large (m).

## Final scope

The audited note proves a sublinear-depth positive extension and three
barriers for intact line architectures.  It does **not** prove a lower
bound for unrestricted four-box words, rule out variable witness widths,
or rule out nonlocal portal intervals.  Its final proposed
surface-scale/variable-band braid is therefore correctly labeled as the
remaining construction target rather than as a theorem.
