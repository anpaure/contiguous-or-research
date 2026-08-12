# Second audit of the stronger three-box shell constants

Source cross-audited:
`MATH_ATTACK_T_THREEBOX_SHELL_AUDIT_O_AGENT_20260724.md`.

## 1. Verdict

The three strengthened constants requested for this cross-audit are correct.

1. For arbitrary cuts of complete contiguous radius rings, one internal
   extreme run per ring gives
   \[
   \sum_i d_i
   \le
   2a^3+3a^2+a+(12a+1)D,
   \]
   and hence
   \[
   \boxed{
   D\ge
   \frac{2a^3+\frac32a^2+\frac12a-1}{15a}
   =\left(\frac2{15}+o(1)\right)a^2.
   }
   \]

2. For the explicitly defined outward canonical enumeration and \(a\ge2\),
   the assignment in Section 5 of the source has exact base
   \(2a^3+2a^2+2\), \(\alpha\)-congestion at most \(a+2\),
   \(\beta\)-congestion at most \(4a-2\), and one center charge \(D\).
   Therefore
   \[
   \sum_i d_i
   \le
   2a^3+2a^2+2+(5a+1)D,
   \]
   which gives
   \[
   \boxed{
   D\ge
   \frac{2a^3+\frac52a^2+\frac32a-3}{8a}
   =\left(\frac14+o(1)\right)a^2.
   }
   \]

3. For the stated fixed-\(x\), contiguous, monotone-row raster, the sampled
   row-endpoint runs have length at most three, only the first and last
   global rows can create boundary exceptions, and each internal
   \(\alpha\)- or \(\beta\)-increment is charged at most twice.  Direct
   interpolation inside each row gives
   \[
   \sum_i d_i
   \le
   (2a+1)(4a+2+8D),
   \]
   and hence
   \[
   \boxed{
   D\ge
   \frac{4a^3-\frac72a^2-\frac{13}{2}a-3}{19a+7}
   =\left(\frac4{19}+o(1)\right)a^2.
   }
   \]

There is no hidden endpoint, base-sum, or factor-of-two error in these three
proofs.  Their architectural scopes remain essential: the first two require
complete contiguous ring blocks in the induced middle-witness order, and
the third requires the designated row-contiguous raster order.  The
canonical \(1/4\) certificate refers only to the explicit enumeration in
the source, not to an undefined universal meaning of “canonical.”

This audit is entirely deductive.  No finite search, numerical experiment,
or solver evidence is used.

## 2. The exact run charge used in all three proofs

Let \([u,v]\) be an internal positive run for one coordinate increment and
put
\[
k=v-u.
\]
The necessary corridor inequality is
\[
\beta_{u-1}-\alpha_{v+1}\le k.
\tag{2.1}
\]

Writing
\[
\Delta\alpha_j=\alpha_j-\alpha_{j-1},
\qquad
\Delta\beta_j=\beta_j-\beta_{j-1},
\]
the three cases of the source's inequality (2.8) are equivalently
\[
d_i\le
\begin{cases}
k+\displaystyle\sum_{j=i+1}^{v+1}\Delta\alpha_j,
   &i<u,\\[3mm]
k+\displaystyle\sum_{j=u}^{i}\Delta\beta_j
  +\displaystyle\sum_{j=i+1}^{v+1}\Delta\alpha_j,
   &u\le i\le v,\\[3mm]
k+\displaystyle\sum_{j=u}^{i}\Delta\beta_j,
   &i>v.
\end{cases}
\tag{2.2}
\]

Thus:

* an index before the run pays base \(k\) and an \(\alpha\)-path ending at
  \(v+1\);
* an index in the run pays base \(k\), a \(\beta\)-path starting at \(u\),
  and an \(\alpha\)-path ending at \(v+1\); and
* an index after the run pays base \(k\) and a \(\beta\)-path starting at
  \(u\).

The total available variation satisfies
\[
\sum_j\Delta\alpha_j\le D,
\qquad
\sum_j\Delta\beta_j\le D.
\tag{2.3}
\]
Consequently a congestion bound is valid precisely when it bounds how many
assigned paths cross each individual increment.  The three proofs below do
that; none merely counts the number of assigned indices.

## 3. One-run arbitrary-cut proof and \(2/15\)

On the radius-\(r\) hexagonal ring, each of the three extreme-coordinate
supports
\[
x=r,\qquad y=r,\qquad z=r
\]
is an arc of \(r+1\) vertices.  The three arcs are disjoint.  Cutting the
cycle into a linear ring block creates two boundary vertices, so at least
one of the three arcs contains neither boundary vertex.  Its two cyclic
neighbors remain inside the same block and are zero for that threshold.
It is therefore an internal positive run in the full induced order.

This includes every boundary case:

* for \(r=1\), the three two-vertex arcs partition the six-cycle, and two
  cut-boundary vertices can meet at most two of them;
* on the outer ring the chosen run's immediate neighbors still lie in that
  ring block; and
* placing the ring block first or last globally does not matter because the
  chosen run avoids both endpoints of the block.

The run has \(r+1\) vertices, so its parameter in (2.2) is
\[
k=r.
\]
Assign all \(6r\) indices of the ring to this run.  Every index pays base
\(r\), giving ring base
\[
6r^2.
\tag{3.1}
\]

Every \(\alpha\)-path and every \(\beta\)-path in this assignment stays
inside the same ring block: both neighboring zero indices \(u-1\) and
\(v+1\) are internal to that block.  A fixed increment in the block can
therefore be crossed by at most all \(6r\) assigned paths.  Since the ring
blocks are disjoint and \(r\le a\), the global charges are bounded by
\[
\text{\(\alpha\)-charge}\le6aD,
\qquad
\text{\(\beta\)-charge}\le6aD.
\tag{3.2}
\]

The center is the only unassigned radius-zero target and satisfies
\[
d_{\rm center}\le D.
\]
The exact base sum is
\[
6\sum_{r=1}^a r^2
=a(a+1)(2a+1)
=2a^3+3a^2+a.
\tag{3.3}
\]
Equations (3.1)--(3.3) prove
\[
\boxed{
\sum_i d_i
\le
2a^3+3a^2+a+(12a+1)D.
}
\tag{3.4}
\]

The rank-capped-start inequality contributes a further
\((3a-1)D\).  Its coefficient combines with \(12a+1\) without a residual
constant:
\[
(12a+1)+(3a-1)=15a.
\tag{3.5}
\]
Using
\[
V_a=4a^3+\frac92a^2+\frac32a-1
\]
and subtracting the base (3.3) gives
\[
V_a-(2a^3+3a^2+a)
=2a^3+\frac32a^2+\frac12a-1.
\tag{3.6}
\]
Therefore
\[
\boxed{
D\ge
\frac{2a^3+\frac32a^2+\frac12a-1}{15a}.
}
\tag{3.7}
\]

The one-run arbitrary-cut proof, all boundary cases, and the leading
constant \(2/15\) are correct.

## 4. Canonical outward enumeration and \(1/4\)

For radius \(r\), let
\[
b_r=2+3r(r-1)
\]
and let \(B_{r,0},\ldots,B_{r,5}\) be the six consecutive side blocks of
length \(r\).  The two chosen runs are
\[
Y_r=[b_r+2r,b_r+3r],
\qquad
Z_r=[b_r+4r,b_r+5r].
\tag{4.1}
\]
Each has \(r+1\) indices and run parameter \(r\).

The immediate zero neighbors of \(Y_r\) always lie in ring \(r\).  The same
is true for \(Z_r\) when \(r\ge2\).  For \(r=1<a\), the right neighbor of
\(Z_1\) is the first point
\[
c_2=(2,-2,0),
\]
which is zero for \(z\ge1\).  Thus every run used in the assignment is
internal when \(a\ge2\), including \(Z_a\): for \(a\ge2\), its right zero
neighbor is the second point of the last side block of the same outer ring.

### 4.1 Assignment and exact base

The assignment has the following ledger.

\[
\begin{array}{c|c|c|c}
\text{indices}&\text{assigned run}&\text{position relative to run}
&\text{base per index}\\ \hline
B_{1,0}\cup B_{1,1}&Y_1&\text{before}&1\\
B_{1,2}\cup B_{1,3}&Y_1&\text{in or after}&1\\
B_{1,4}\cup B_{1,5}&Z_1&\text{in or after}&1\\
B_{r,0}\cup B_{r,1},\ r\ge2&Z_{r-1}&\text{after}&r-1\\
B_{r,2}\cup B_{r,3},\ r\ge2&Y_r&\text{in or after}&r\\
B_{r,4}\cup B_{r,5},\ r\ge2&Z_r&\text{in or after}&r
\end{array}
\]

For \(r=1\), all six indices pay base one.  For \(r\ge2\), the first
\(2r\) indices pay \(r-1\) and the remaining \(4r\) indices pay \(r\).
Hence
\[
\begin{aligned}
\text{base}
&=6+\sum_{r=2}^a\bigl(2r(r-1)+4r^2\bigr)\\
&=2a^3+2a^2+2.
\end{aligned}
\tag{4.2}
\]
The constant \(+2\) is correct; it is the replacement of the generic
radius-one contribution \(4\) by the actual contribution \(6\).

### 4.2 \(\alpha\)-congestion

By (2.2), an assigned index has an \(\alpha\)-path only when it is before
or inside its run.

For \(r\ge2\), the first two side blocks are assigned backward to
\(Z_{r-1}\) and hence have no \(\alpha\)-term.  Among the \(2r\) indices
assigned to \(Y_r\), exactly the \(r+1\) indices in \(Y_r\) have an
\(\alpha\)-term; the remaining \(r-1\) lie after the run.  The same holds
for \(Z_r\).  These nested paths create congestion at most \(r+1\).

The \(Y_r\) and \(Z_r\) \(\alpha\)-ranges are disjoint: the \(Y_r\) paths
end at \(v(Y_r)+1\), while the \(Z_r\) paths start strictly after that
increment.  Ranges from different rings are also disjoint, except that a
\(Z_1\) path may end at the first index of ring two.  The first two side
blocks of ring two are assigned backward and have no \(\alpha\)-paths; the
next \(\alpha\)-range starts only at \(Y_2\).  Hence that exceptional
cross-ring increment creates no overlap.

At radius one, the two forward indices in
\(B_{1,0}\cup B_{1,1}\) overlap the two \(Y_1\) paths.  Their maximum
combined multiplicity is four.  They do not overlap the \(Z_1\) paths:
the forward paths end at \(u(Z_1)\), whereas \(Z_1\)'s own paths cross only
increments strictly after \(u(Z_1)\).

Therefore
\[
\text{\(\alpha\)-congestion}
\le\max(4,a+1)\le a+2
\qquad(a\ge2),
\tag{4.3}
\]
and the total \(\alpha\)-charge is at most \((a+2)D\).

### 4.3 \(\beta\)-congestion

An index in or after its assigned run has a \(\beta\)-path beginning at
the run's left boundary.

The \(2r\) indices assigned to \(Y_r\) give multiplicity at most \(2r\).
Their paths end before the first increment used by \(Z_r\).  The \(2r\)
indices assigned to \(Z_r\) also give multiplicity at most \(2r\).

For \(r<a\), the first \(2(r+1)\) indices of ring \(r+1\) are assigned
backward to \(Z_r\).  Their \(\beta\)-paths overlap the \(Z_r\) paths and
give the only double overlap:
\[
2r+2(r+1)=4r+2\le4a-2.
\tag{4.4}
\]
Those backward paths end immediately before the first increment used by
\(Y_{r+1}\), so no third family overlaps.  At the outer run \(Z_a\), there
is no backward family from a later ring and the multiplicity is only
\(2a\).  All \(Y_r\) multiplicities are also at most \(2a\).

Thus
\[
\text{\(\beta\)-congestion}\le4a-2
\qquad(a\ge2),
\tag{4.5}
\]
and the total \(\beta\)-charge is at most \((4a-2)D\).

### 4.4 Sum and boundary \(a=1\)

The center contributes at most \(D\).  Combining (4.2)--(4.5) gives
\[
\begin{aligned}
\sum_i d_i
&\le
2a^3+2a^2+2
+\bigl((a+2)+(4a-2)+1\bigr)D\\
&=
2a^3+2a^2+2+(5a+1)D.
\end{aligned}
\tag{4.6}
\]

The proof uses \(a\ge2\) only to make \(Z_1\) internal.  When \(a=1\),
the stronger certificate is not needed; the trivial estimate
\(\sum_i d_i\le7D\) handles the source's weaker all-\(a\) statement.

For \(a\ge2\), adding the rank-capped-start term gives total \(D\)-coefficient
\[
(5a+1)+(3a-1)=8a.
\tag{4.7}
\]
Subtracting the base from \(V_a\) gives
\[
V_a-(2a^3+2a^2+2)
=2a^3+\frac52a^2+\frac32a-3.
\tag{4.8}
\]
Therefore
\[
\boxed{
D\ge
\frac{2a^3+\frac52a^2+\frac32a-3}{8a}
=\left(\frac14+o(1)\right)a^2.
}
\tag{4.9}
\]

The canonical \(1/4\) proof is correct for the explicit enumeration and its
stated range.

## 5. Direct raster charge and \(4/19\)

At fixed \(x\), the middle-layer row is
\[
\max(0,a-x)\le y\le\min(2a,3a-x).
\]
There are \(2a+1\) rows and each has at most
\[
B=2a+1
\tag{5.1}
\]
indices.  Let \(e_x\) be the maximum-\(y\) endpoint of row \(x\).

### 5.1 Endpoint run shapes

For \(x\le a\), the endpoint level is \(U_x=2a\).  Every relevant row
contributes only its maximum-\(y\) endpoint to the threshold \(y\ge2a\).
Two such singleton pieces can join across one row seam, but a component
cannot cross two seams: a nontrivial row's maximum endpoint cannot be both
the first and last position of that row.  Hence the component through
\(e_x\) has one or two indices.

For \(x>a\), put \(t=U_x=3a-x\).  Row \(x\) contributes only \(e_x\).
Row \(x-1\) has maximum \(t+1\), so it contributes at most its top two
points.  If these points meet \(e_x\) across the seam, they form a terminal
two-point segment of row \(x-1\).  It is preceded by a negative point:
row \(x-1\) has length \(t+2\ge a+2\ge3\).  The component therefore cannot
continue through the preceding seam.  Row \(x+1\) has maximum \(t-1\) and
contributes nothing.  Thus the component through \(e_x\) has at most three
indices.

Only the component through \(e_0\) can touch the first global order
boundary, and only the component through \(e_{2a}\) can touch the last.
For example, a plateau component containing both \(e_0\) and \(e_1\)
requires \(e_0\) to be the last point of row zero, so it cannot also touch
the first global boundary.  The descending case has the same
first-versus-last endpoint exclusion.  Consequently there are at most two
boundary exceptions.

Every other endpoint belongs to an internal run with
\[
v_x-u_x\le2.
\tag{5.2}
\]
Applying the middle case of (2.2) at \(i=e_x\) gives
\[
d_{e_x}
\le
2+(\beta_{e_x}-\beta_{u_x-1})
+(\alpha_{v_x+1}-\alpha_{e_x}).
\tag{5.3}
\]

### 5.2 Internal congestion

On the plateau, the only overlapping endpoint charges arise when two
singleton endpoint pieces join across one seam.  Applying the same
one- or two-index run to its one or two sampled endpoints charges each
\(\alpha\)- or \(\beta\)-increment at most twice.

On the descending part, a three-index component has the form
\[
\{\text{top two points of row }x-1\}\cup\{e_x\}.
\]
For this to occur, \(e_{x-1}\) is the last point of row \(x-1\) and
\(e_x\) is the first point of row \(x\).  The component for
\(e_{x-1}\)'s own, one-level-higher threshold is then a singleton: the
orientation which puts \(e_{x-1}\) last prevents it from also connecting
to row \(x-2\).  Thus its charge can overlap the \(e_x\) charge, but no
third sampled-endpoint charge can overlap them.

The same orientation exclusion prevents adjacent three-index components
from propagating along multiple seams.  It also covers the transition from
the plateau to the descending rows.  Hence every internal
\(\Delta\alpha_j\) and every internal \(\Delta\beta_j\) is charged at most
twice.

The internal endpoint bases contribute at most \(2(2a-1)=4a-2\), and the
two variation families contribute at most \(2D+2D=4D\).  Charging each of
the two boundary exceptions by \(d_{e_x}\le D\) yields
\[
\sum_x d_{e_x}
\le4a-2+6D
\le4a+2+6D.
\tag{5.4}
\]
This verifies the source's convenient endpoint ledger, including arbitrary
independent row orientations and the smallest case \(a=1\).

### 5.3 Direct interpolation inside rows

For any row index \(i\) and its endpoint \(e=e_x\), monotonicity of
\(\alpha,\beta\) gives
\[
d_i\le
\begin{cases}
d_e+\alpha_e-\alpha_i,&i<e,\\
d_e+\beta_i-\beta_e,&i>e.
\end{cases}
\tag{5.5}
\]

Each row has at most \(B=2a+1\) indices.  Its endpoint width is therefore
charged at most \(B\) times.  All interpolation paths stay inside their own
contiguous row block, so paths from different rows do not share an
increment.  Within a row, any fixed \(\alpha\)- or \(\beta\)-increment is
crossed by at most \(B\) paths.  Using the global variation bounds (2.3)
gives
\[
\sum_i d_i
\le
B\left(\sum_xd_{e_x}+2D\right).
\tag{5.6}
\]

Substituting (5.4),
\[
\boxed{
\sum_i d_i
\le
(2a+1)(4a+2+8D).
}
\tag{5.7}
\]

The base is
\[
(2a+1)(4a+2)=2(2a+1)^2,
\tag{5.8}
\]
and after adding the rank-capped-start term the exact coefficient of \(D\)
is
\[
8(2a+1)+(3a-1)=19a+7.
\tag{5.9}
\]
Finally,
\[
\begin{aligned}
V_a-2(2a+1)^2
&=
4a^3+\frac92a^2+\frac32a-1
-(8a^2+8a+2)\\
&=
4a^3-\frac72a^2-\frac{13}{2}a-3.
\end{aligned}
\tag{5.10}
\]
Equations (5.7)--(5.10) prove
\[
\boxed{
D\ge
\frac{4a^3-\frac72a^2-\frac{13}{2}a-3}{19a+7}
=\left(\frac4{19}+o(1)\right)a^2.
}
\tag{5.11}
\]

For small \(a\) the numerator may be negative, so the real inequality is
vacuous; this does not affect its validity or its asymptotic constant.

## 6. Final ledger

- **Run inequality (2.8):** correctly applied in all three arguments.
- **Arbitrary-ring boundary cases:** complete, including \(r=1\), the
  outer ring, and globally first/last ring blocks.
- **Arbitrary-ring base:** \(6\sum r^2=2a^3+3a^2+a\), correct.
- **Arbitrary-ring congestion:** at most \(6aD\) separately for
  \(\alpha\) and \(\beta\), correct.
- **One-run arbitrary-cut constant:** \(2/15\), correct.
- **Canonical run boundaries:** correct for every \(a\ge2\), including the
  \(Z_1\)-to-\(c_2\) seam and the outer \(Z_a\) run.
- **Canonical base:** \(2a^3+2a^2+2\), correct.
- **Canonical \(\alpha\)-congestion:** at most \((a+2)D\), correct.
- **Canonical \(\beta\)-congestion:** at most \((4a-2)D\), correct; there
  are no triple overlaps.
- **Canonical leading constant:** \(1/4\), correct for the explicit outward
  order.
- **Raster endpoint components:** at most three indices with only two
  possible global-boundary exceptions, correct.
- **Raster endpoint congestion:** at most two for each variation family,
  correct.
- **Direct-row interpolation:** row load and variation congestion are both
  at most \(2a+1\), correct.
- **Direct-raster denominator and constant:** \(19a+7\) and \(4/19\),
  correct.
- **Scope:** none of these constants applies to arbitrary interleavings or
  arbitrary induced witness orders.
