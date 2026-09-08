# Easy-line completion of the complementary portal core: an exact scoped barrier

## 1. Outcome

Put

\[
 P_m=[0,m]^4,\qquad R=2m-1,
 \qquad 1\le q\le \lfloor m/3\rfloor .
\]

`COMPLEMENTARY_SEAM_RECTANGLE_TILING.md` gives a word on (L_R) of
length

\[
 |L_R|+4q(q-1)
\]

covering every depth-at-most-(q) target missed by both complementary
complete-line systems.  Its unresolved step is to retain the targets which
do have a complete ({1,2})- or ({3,4})-line witness.

This note rules out the most literal completion of that step.  Complete
every physical line touched by a portal arm, or, more weakly, insist that
every adjacent pair on every such line remain an actual adjacent pair of
the word.  Then the required repeat count is already cubic at linear
depth:

\[
 \boxed{
 |W|-|L_R|\ \ge J_q
   ={2\over3}q^3+O(q^2). }
\]

The exact quasi-polynomial (J_q) is displayed in Theorem 2 below.
Consequently this natural completion cannot give
(M_m+o(m^3)) when (q=\lfloor\alpha m\rfloor), for fixed
(alpha>0).

This is deliberately a scoped no-go.  It does **not** say that the easy
targets themselves require cubic repetition.  A successful construction
must choose one witness direction target by target, and must replace a
positive-density family of literal line witnesses by mixed or nonlocal
portal witnesses.

There is also a useful exact description of the balanced demand graph.  Its
canonical components really are monotone paths

\[
 E(A-1,B-1)-O(A-1,B)-E(A,B)-O(A,B+1)-E(A+1,B+1).
\]

However, the two requests on every shared line use nested arms pointing in
the same direction.  Thus the path structure alone does not produce a
physical braid: turning at the next seam cuts the preceding long arm.

## 2. The physical line families forced by the hard core

Let

\[
 \mathcal N_q=\{(A,B)\in\mathbb Z_{\ge0}^2:A+B\le q-1\}.
\]

For ((A,B)\in\mathcal N_q), the (X)-arm in the hard portal core lies on
the coordinate-({1,2}) line whose fixed last pair is

\[
 (m-B-1,A),                                             \tag{2.1}
\]

or its coordinate-(3,4) reversal.  Reversing coordinates (1,2)
changes which end of the same physical line is used, but not the line.
Call the resulting set of distinct physical lines (mathcal X_q).
Similarly, the (Y)-arms lie on the coordinate-({3,4}) lines whose
fixed first pair is

\[
 (m-A-1,B),                                             \tag{2.2}
\]

or its coordinate-(1,2) reversal; call this family (mathcal Y_q).
Thus

\[
 |mathcal X_q|=|mathcal Y_q|=q(q+1).                 \tag{2.3}
\]

The high/low gap used in the hard-core theorem implies that all these lines
are distinct.  On one line of \(\mathcal X_q\), the two first-pair
orientations occupy opposite ends.  Thus the two **portal arms** do not
overlap; this by itself does not assert that the outer tails can be attached
in the required word order.  The analogous statement holds for
\(\mathcal Y_q\).  The obstruction below comes from intersections between
the two line families.

## 3. Exact crossing count

For an integer (d), put

\[
 n_q(d)=#\{(A,B)\in\mathcal N_q:A-B=d\}
 =\begin{cases}
 \left\lfloor{q+1-|d|\over2}\right\rfloor,&|d|\le q-1,\\
 0,&|d|\ge q.
 \end{cases}                                          \tag{3.1}
\]

Consider the (X)-line indexed by ((A,B)) and the (Y)-line indexed by
((C,D)).  Their fixed coordinates form a point of (L_R) precisely when

\[
 (m-B-1+A)+(m-C-1+D)=2m-1,
\]

or equivalently

\[
                 (A-B)-(C-D)=1.                     \tag{3.2}
\]

There are four independent high/low orientations.  Hence the total number
of crossings is

\[
 4S_q,
 \qquad
 S_q=\sum_d n_q(d)n_q(d-1).                         \tag{3.3}
\]

For the local adjacency argument we retain only crossings which are
interior points of both physical lines.  It is enough to impose

\[
                         A\ge1,\qquad D\ge1.         \tag{3.4}
\]

Indeed, at such a crossing both fixed coordinate pairs have one coordinate
in ([1,m-1]), and the other is also in ([1,m-1]) because
(q\le m/3).  Thus the crossing has two neighbours in each line.

After replacing (A) by (A-1) and (D) by (D-1), the restricted
count in one orientation is (S_{q-1}).  Therefore the number of distinct
interior crossings is

\[
                         J_q=4S_{q-1}.               \tag{3.5}
\]

### Lemma 1 (closed form for (S_q))

For (q\ge1),

\[
 S_q=
 \begin{cases}
 \displaystyle {q(2q-1)(q+2)\over12},&q\text{ even},\\[6pt]
 \displaystyle {q(2q-1)(q+2)-3\over12},&q\text{ odd}.
 \end{cases}                                         \tag{3.6}
\]

#### Proof

The summand at \(d\) equals the summand at \(1-d\), because
\(n_q(-d)=n_q(d)\).  Hence

\[
 S_q=2\sum_{d\ge1}n_q(d)n_q(d-1).                  \tag{3.9}
\]

For \(d\ge0\), equation (3.1) counts the integers

\[
 A=d+B,qquad 0\le B\le {q-1-d\over2}.
\]

If \(q=2h\), the nonzero values for nonnegative \(d\) are

\[
 n_q(2j)=n_q(2j+1)=h-j\qquad(0\le j<h).
\]

The half-sum in (3.9) is therefore

\[
 \sum_{k=1}^{h}k^2+\sum_{k=1}^{h-1}k(k+1)
   ={h(h+1)(4h-1)\over6}.
\]

Doubling gives

\[
 S_{2h}={h(h+1)(4h-1)\over3}
       ={(2h)(4h-1)(2h+2)\over12}.
\]

If \(q=2h+1\), then

\[
 n_q(2j)=h+1-j,\qquad n_q(2j+1)=h-j.
\]

Now the half-sum is

\[
 \sum_{k=1}^{h}\bigl(k^2+k(k+1)\bigr)
   ={h(h+1)(4h+5)\over6}.
\]

After doubling and rewriting in terms of \(q=2h+1\), this is the odd
formula in (3.6).  \(\square\)

Combining (3.5)--(3.6) gives the promised exact formula

\[
 \boxed{
 J_q=
 \begin{cases}
 \displaystyle {q(2q+1)(q-2)\over3},&q\text{ even},\\[6pt]
 \displaystyle {q(2q+1)(q-2)+3\over3},&q\text{ odd}.
 \end{cases}}                                        \tag{3.7}
\]

It is valid also at (q=1,2), when (J_q=0), and satisfies

\[
                         J_q={2\over3}q^3+O(q^2).    \tag{3.8}
\]

## 4. The literal easy-line barrier

Call a word (W) an **adjacency-preserving completion** of the portal line
families when

1. every point of (L_R) occurs in (W); and
2. for every line in \(\mathcal X_q\cup\mathcal Y_q\), every two
   consecutive lattice points on that line occur consecutively somewhere
   in (W), in either order.

Condition 2 is weaker than asking that every demanded physical line occur
as one complete contiguous block.  It is exactly what is required if the
completion promises to retain every canonical depth-one line witness on
all portal lines.

### Theorem 2 (cubic barrier for literal line preservation)

Every adjacency-preserving completion satisfies

\[
                         |W|\ge |L_R|+J_q.           \tag{4.1}
\]

#### Proof

Let (p) be one of the (J_q) interior crossings.  It has two distinct
neighbours \(x^-,x^+\) on its \(\mathcal X_q\)-line and two distinct
neighbours \(y^-,y^+\) on its \(\mathcal Y_q\)-line.  The four neighbours
are mutually distinct, because the two coordinate directions are
complementary.

Condition 2 requires all four unordered word adjacencies

\[
 \{p,x^-\},\quad\{p,x^+\},\quad
 \{p,y^-\},\quad\{p,y^+\}.                          \tag{4.2}
\]

One occurrence of (p) has at most two neighbours in a linear word.  Thus
(p) must occur at least twice.  Distinct physical line pairs have
distinct crossings, so the (J_q) forced extra occurrences are distinct.
Every other base point occurs at least once by condition 1.  This proves
(4.1).  (square)

For (q=\lfloor\alpha m\rfloor), fixed
(0<\alpha<1/3), Theorem 2 gives

\[
 |W|-|L_R|\ge
 \left({2\over3}\alpha^3+o(1)\right)m^3.           \tag{4.3}
\]

Thus neither “finish every extracted arm to its full line” nor “restore
every broken canonical line adjacency” is compatible with a near-once
linear-depth construction.

## 5. Exact canonical balanced-demand paths

The balanced catalogue of the source has seam label ((A,B)), with
(delta=A+B).  Write (E(A,B)) when (delta=2r), and (O(A,B)) when
(delta=2r+1).  Fix the canonical odd baseline

\[
 (c,d)=(r,r+1).                                      \tag{5.1}
\]

The row-line label is ((m-B-1,d)), and the column-line label is
((m-A-1,c)).  Direct comparison gives

\[
\begin{array}{lll}
 E(A,B)&\text{shares its row line with}&O(A-1,B),\\
 E(A,B)&\text{shares its column line with}&O(A,B+1),\\
 O(A,B)&\text{shares its row line with}&E(A+1,B),\\
 O(A,B)&\text{shares its column line with}&E(A,B-1),
\end{array}                                          \tag{5.2}
\]

whenever the displayed neighbouring seam belongs to the actual catalogue.
It follows that every component is an induced subpath of

\[
 \cdots-E(A-1,B-1)-O(A-1,B)-E(A,B)-O(A,B+1)
       -E(A+1,B+1)-\cdots .                          \tag{5.3}
\]

There are no cycles: the coordinates increase monotonically along either
orientation of (5.3).  In particular, the degree-two statement is exact
for the fixed convention (5.1), including arbitrary deletions at the true
catalogue boundary.

This path theorem is useful but not yet the required braid.  For example,
the column line shared by (E(A,B)) and (O(A,B+1)) contains the seam
points

\[
 (m-A-1,r,m-B,r),qquad
 (m-A-1,r,m-B-1,r+1).                               \tag{5.4}
\]

They are consecutive.  Moreover the (O)-arm is literally the (E)-arm
with its first point deleted:

\[
\begin{aligned}
 E:&\ (m-B-v,r+v),&&v=0,1,2,\ldots,\\
 O:&\ (m-B-1-v,r+1+v),&&v=0,1,2,\ldots .
\end{aligned}                                        \tag{5.5}
\]

The same nesting holds at shared row lines.  A traversal of (5.3) turns
from the shared line at the second seam point and therefore retains only
one step of the preceding arm.  Keeping both long conventional arms would
require a duplicated nested tail, or a witness which passes nonlocally
through further seams.

Thus the maximum-degree-two demand graph removes a combinatorial branching
problem, but not the physical-order problem.

## 6. Consequence for the next construction

The hard portal core itself remains valid and near-once.  What Theorem 2
shows is that it cannot be completed by restoring both literal line systems
wherever an arm was extracted.  At every one of a cubic family of row--
column incidences, a near-once word must choose which local line direction
survives.

The corrected positive target is therefore an **oriented witness-selection
braid**:

* choose one of the available line directions separately for each easy
  target;
* allow the choice to change across the path components (5.3);
* route the targets abandoned at those changes through mixed, possibly
  nonlocal, seam intervals;
* never demand all four local adjacencies at an interior row--column
  crossing.

A min-comparison or concentric-shell partition has exactly this form.  Its
unresolved theorem is not line completion, but proof that the discarded
line windows admit a bounded-overlap mixed-seam reassignment.

## 7. Verification and status

`scratch/verify_portal_easy_line_completion.py` checks, for
(1\le q\le80):

* the formula for (n_q(d));
* both parity formulas for (S_q) and (J_q);
* the direct interior-crossing enumeration;
* the canonical path adjacencies (5.2);
* the one-step nesting identity (5.5).

The proof-grade ledger is:

| statement | status |
|---|---|
| explicit hard portal core | inherited, proved |
| canonical balanced demand graph is a union of paths | proved |
| shared canonical arms are nested on the same ray | proved |
| exact interior crossing count (J_q) | proved |
| literal full-line/adjacency completion costs (Omega(q^3)) repeats | proved |
| target-selective easy-line completion with (o(m^3)) repeats | open |

The negative result is intentionally narrower than the original OR problem.
It identifies a precise architectural mistake: preserving both complete-line
witness systems is too expensive, even though preserving the target family
by a judicious mixture may still be possible.
