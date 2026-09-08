# Promotion-frame owner resolution sits at the square-codegree threshold

## Exact fractional point, growing-uniformity accounting, and a literal odd triangle

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{m-H},
\tag{0.1}
\]

and take the critical calibration in which

\[
 \lambda:=\frac{MN}{W}=\frac{M}{R_H}\le1,
 \qquad 1-\lambda=o(1).
\tag{0.2}
\]

Let \(\mathcal G_H\) be the owner-resolution hypergraph whose vertices
are rank-\(M\) tops and rank-\(m\) owners, and whose edge
\(e(U,\pi)\) consists of one top \(U\) and the \(M\) cyclic
rank-\(m\) windows of a directed cyclic order \(\pi\) on \(U\).
Thus its uniformity is

\[
                         r=M+1.
\tag{0.3}
\]

The uniform fractional point is exact: weight \(1/(M-1)!\) on every
edge. Every top then has load one and every owner has load \(\lambda\).
It has total edge weight \(N\) and total owner mass
\(MN=W-o(W)\).

The exact maximum normalized pair codegree is

\[
 \boxed{\frac{\Delta_2}{d_{\min}}=\frac{2}{m^2},}
\tag{0.4}
\]

where \(d_{\min}\) is the owner degree. Consequently

\[
 r\frac{\Delta_2}{d_{\min}}=o(1),\qquad
 r^2\frac{\Delta_2}{d_{\min}}=2+o(1).
\tag{0.5}
\]

Thus the catalogue is sparse enough for isolated infinitesimal bites,
but it is exactly critical at the square-uniformity scale. A theorem
whose growing-uniformity hypothesis is
\(r^2\Delta_2=o(d_{\min})\) cannot be applied here.

There is also a literal integral obstruction. Three actual promotion
frames on three distinct tops have pairwise owner intersections but no
common owner. Their three columns contain the matrix

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
\tag{0.6}
\]

whose determinant is two. Weight \(1/2\) on each column is feasible,
whereas an integral matching takes at most one of the three. Hence the
physical owner-incidence matrix is not totally unimodular or balanced.

Finally, deleting the dense three-top seed does not create a fractional
obstruction. If the bank has \(K\le W/P_H\) packets, restricting the
uniform fractional point away from its \(3K\) tops and \(3MK\) owners
loses total edge weight at most

\[
 3K+3MK\lambda=o(N)
\tag{0.7}
\]

at the calibrated scale. Thus the seeded residual remains fractionally
near-spanning. Equations (0.5)--(0.6) prove why this does not round by
any currently available local or polyhedral argument.

The exact surviving gate is integral seeded resilience, not fractional
capacity: after deleting the bank resources, prove a matching of
\(N-o(N)\) ordinary frames, or construct a growing absorber which
crosses the odd triangles while preserving the owner leave.

## 1. Exact degrees

Let

\[
 R=(M-1)!
\tag{1.1}
\]

be the number of directed cyclic orders on a fixed labelled top. Every
top has degree \(R\).

Fix an owner \(X\). Choose its extra \(H\) top labels in
\(\binom mH\) ways. In a fixed compatible top, making \(X\) and its
\(H\)-set complement the two cyclic intervals gives exactly
\(m!H!\) directed cycles. Hence every owner has degree

\[
 D=\binom mH m!H!
   =\frac{(m!)^2}{(m-H)!}.
\tag{1.2}
\]

Double counting top--frame--owner incidences gives

\[
                         \frac DR=\frac{MN}{W}=\lambda.
\tag{1.3}
\]

Under (0.2), \(D=d_{\min}\). Weighting every edge by \(1/R\)
therefore gives top load one and owner load \(D/R=\lambda\), proving
the fractional assertion in Section 0.

A compatible top--owner pair has codegree \(m!H!\), so its normalized
codegree is

\[
 \frac{m!H!}{D}=\binom mH^{-1}=o(m^{-A})
\tag{1.4}
\]

for every fixed \(A\) in the Gaussian regime.

## 2. Exact owner-pair codegrees

For distinct owners \(X,Y\), put

\[
 d=|X\setminus Y|=|Y\setminus X|.
\tag{2.1}
\]

If \(d>H\), no rank-\(M\) top contains both owners, so their codegree
is zero. Suppose \(1\le d<H\). A common top is obtained by adding an
\((H-d)\)-set to \(X\cup Y\), giving

\[
                         \binom{m-d}{H-d}
\tag{2.2}
\]

choices. In such a top, the two complementary \(H\)-sets overlap in
\(H-d\) labels. For both to be cyclic intervals, their exclusive,
common, exclusive, and outside blocks occur in one of two orientations.
Ordering within those blocks gives

\[
                         2d!^2(H-d)!(m-d)!
\tag{2.3}
\]

cycles. Multiplication and division by (1.2) yield

\[
 d_{\mathcal G}(X,Y)
 =\frac{2d!^2(m-d)!^2}{(m-H)!},
 \qquad
 \frac{d_{\mathcal G}(X,Y)}D
 =\frac{2}{\binom md^2}.
\tag{2.4}
\]

For \(d=H\), the two complementary \(H\)-sets are disjoint. Contract
each to one cyclic block. Together with the \(m-H\) outside labels
there are \(m-H+2\) cyclic objects, so

\[
 d_{\mathcal G}(X,Y)=H!^2(m-H+1)!,
 \qquad
 \frac{d_{\mathcal G}(X,Y)}D
 =\frac{m-H+1}{\binom mH^2}.
\tag{2.5}
\]

The maximum occurs at \(d=1\), proving (0.4). Since
\(r=M+1=m+H+1\), (0.5) follows.

## 3. A literal determinant-two triangle

Assume \(m\ge4H\). Choose pairwise disjoint sets

\[
 |C|=m-H,\qquad |A_1|=|A_2|=|A_3|=H,
\tag{3.1}
\]

and define cyclically

\[
 U_1=C\cup A_1\cup A_2,\quad
 U_2=C\cup A_2\cup A_3,\quad
 U_3=C\cup A_3\cup A_1,
\tag{3.2}
\]

\[
 X_i=C\cup A_i\qquad(i=1,2,3).
\tag{3.3}
\]

On \(U_1\), choose a directed cyclic order in which \(A_1\) and
\(A_2\) are cyclic intervals. Its owner deck contains
\(U_1\setminus A_1=X_2\) and
\(U_1\setminus A_2=X_1\). Define frames on \(U_2,U_3\)
cyclically in the same way. The resulting three columns contain the
incidence pattern (0.6).

No owner belongs to all three columns: such an owner would be an
\(m\)-subset of

\[
                         U_1\cap U_2\cap U_3=C,
\tag{3.4}
\]

but \(|C|=m-H<m\). Therefore putting weight \(1/2\) on every one of
the three complete frame columns respects every owner capacity, not
only the three displayed rows. It also respects the three distinct top
capacities. On the other hand, every pair of columns shares one of the
owners \(X_1,X_2,X_3\), so an integral matching contains at most one.
This proves the asserted determinant and the literal \(3/2\)-versus-1
local integrality gap.

The triangle is not a global no-go: every top has many other frame
columns. Its exact force is narrower and important. Fractional
feasibility, degree regularity, and pair-codegree estimates do not imply
integral completion without a global resilience or absorber theorem.

## 4. Fractional robustness of the dense seed

Let \(\mathscr B\) be a resource-disjoint packet bank with \(K\) packets.
Delete its \(3K\) top vertices and \(3MK\) owner vertices from
\(\mathcal G_H\). Restrict the uniform fractional point of Section 1
to surviving edges.

Edges incident with the deleted tops carry total weight exactly \(3K\).
For every deleted owner, all incident edges carry total weight
\(\lambda\le1\). By the union bound, owner deletion removes additional
weight at most \(3MK\lambda\). This proves (0.7).

At the calibrated scale,

\[
 \frac{K}{N}\le\frac{R_H}{P_H}=o(1),
\tag{4.1}
\]

and

\[
 \frac{MK}{N}
 \le\frac{MR_H}{P_H}
 \le\frac{M}{256\sum_{q=1}^Hq^2}
 =o(1).
\tag{4.2}
\]

Thus (0.7) is \(o(N)\). The residual augmented system, after adjoining
one fixed packet shore per seed, is fractionally near-spanning.

This is deliberately not promoted to an integral statement. Vertex
deletion can concentrate the surviving links along later matching
trajectories, (0.5) is critical rather than subcritical at square
uniformity, and Section 3 excludes total-unimodularity rounding.

The previously proposed catalogue-specific slow-bite proof does not
remove this gap. Its unconditional conclusion was retracted in
`MATH_AUDIT_REPAIRED_RING_BUFFERED_STOPPED_GENERATOR_ESCAPE_20260727.md`:
the stopped generator contains unbounded repeated-next-edge and
compensation-coin diagonal energies. The surviving conditional statement
requires the dynamic diagonal link-energy inequality MDLE, not merely the
static pair-codegree formulas above. Thus no known growing-uniformity
theorem has been silently invoked here.

## 5. Exact boundary

Proved:

1. the exact fractional root factor and its \(W-o(W)\) owner mass;
2. every ordinary degree and pair-codegree ratio needed at growing
   uniformity;
3. the critical identity \(r^2\Delta_2/d_{\min}=2+o(1)\);
4. a literal determinant-two triangle of complete physical frames; and
5. fractional near-spanning robustness after deleting the dense packet
   seed.

Not proved:

1. an integral matching of \(N-o(N)\) residual frames;
2. a hereditary degree theorem along a fine nibble;
3. the MDLE/ADLE dynamic diagonal-energy bound;
4. a growing absorber crossing the odd triangles; or
5. coefficient one.

Together with
`MATH_THEOREM_THREE_TOP_BANK_OWNER_RESOLUTION_PROJECTION_AND_COLLAR_WALL_20260727.md`,
this closes the packet-shore and shared-collar routes while isolating
seeded integral resilience as the sole remaining owner-installation
statement.
