# Adversarial audit of the three-box shell report

Source audited: MATH_ATTACK_T_THREEBOX_SHELL_REPORT_RAW_20260724.md

Date: 2026-07-24

## 1. Executive verdict

The principal mathematical claims survive, with one local witness correction,
two hidden architecture hypotheses that must be made explicit, and a narrower
implication scope.

1. **Literal triangular-shell word: valid after a boundary repair in the
   proof.**  The length, coverage theorem for \(R\ge2\), both parity formulas
   for the width, and the identity relating length to width are exact.  The
   first two displayed witness recipes are not valid verbatim for every
   \(t=1\) target because the initial \(A_1\) was deleted.  The theorem remains
   valid because the seven max-one targets have the explicit special
   witnesses recorded in Section 3 below.

2. **Arbitrary contiguous-ring obstruction: valid and nonsharp.**  The report's
   exact inequality
   \[
   \sum_i d_i\le
   2a^3+6a^2+4a+1+18aD
   \]
   and its consequent leading constant \(2/21\) are correct.  A complete
   one-run-per-ring charge proves the stronger inequality
   \[
   \sum_i d_i\le
   2a^3+3a^2+a+(12a+1)D
   \]
   and hence the stronger leading constant \(2/15\).

3. **Canonical-ring obstruction: valid once “canonical” is defined.**  The raw
   report omitted the required enumeration and congestion proof.  Section 5
   supplies both.  They prove the reported inequality
   \[
   \sum_i d_i\le2a^3+2a^2+1+7aD
   \]
   and therefore its \(1/5\) consequence.  The same certificate in fact gives
   \[
   \sum_i d_i\le2a^3+2a^2+2+(5a+1)D,
   \]
   which strengthens the asymptotic excess constant to \(1/4\) for the
   canonical cut.

4. **Fixed-coordinate raster obstruction: valid under an induced-witness-order
   hypothesis, and nonsharp.**  The exact denominator \(35a+15\) and leading
   constant \(4/35\) check.  Charging each row directly to its own endpoint
   improves them to \(19a+7\) and \(4/19\), respectively.

5. **Ordered shell-occurrence compression: valid in its stated
   occurrence-by-occurrence model.**  It is not a lower bound for arbitrary
   words, for a rebundling that does not represent every virtual occurrence,
   or for crossing endpoint orders.

6. **Final implication claims: partly unsupported.**  Positive-density
   cross-radius interleaving and long cross-radius corridors are plausible
   design responses, not proved necessities.  The bounded-component-net
   conclusion needs the quantitative hypotheses isolated in Section 8.  None
   of the architecture-local obstructions proves the compact balanced
   three-box theorem or its negation.

No finite search or computational verification is used in this audit.

## 2. Common interval calculus

This section states the exact facts used in both obstruction arguments and
fixes their quantifiers.

Let
\[
\mathcal H_a=\{(x,y,z)\in[0,2a]^3:x+y+z=3a\}.
\]
Its cardinality, which is also the width of the cube, is
\[
M_a=3a^2+3a+1.
\tag{2.1}
\]
By rank symmetry, the number of nonzero targets strictly below rank \(3a\)
is
\[
\begin{aligned}
V_a
&=\frac{(2a+1)^3-M_a}{2}-1\\
&=4a^3+\frac92a^2+\frac32a-1.
\end{aligned}
\tag{2.2}
\]

Consider a universal word of length \(M_a+D\).  Select one witness interval
for each of the \(M_a\) distinct middle targets and order the intervals by
their left endpoints:
\[
I_i=[\ell_i,r_i],\qquad 1\le i\le M_a.
\]
Both endpoint sequences are strictly increasing.  Indeed, equal left
endpoints would make the two intervals nested; and if
\(\ell_i<\ell_j\) but \(r_i\ge r_j\), then \(I_j\subseteq I_i\).
Coordinatewise maxima on nested intervals are comparable.  Two distinct
rank-\(3a\) targets cannot be comparable, so neither event is possible.

Since the endpoints are distinct integers in an interval of length
\(M_a+D\), they have the normal form
\[
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\tag{2.3}
\]
where
\[
0\le\alpha_1\le\cdots\le\alpha_{M_a}\le D,\qquad
0\le\beta_1\le\cdots\le\beta_{M_a}\le D,
\tag{2.4}
\]
and \(\alpha_i\le\beta_i\).  Put
\[
d_i=r_i-\ell_i=\beta_i-\alpha_i.
\tag{2.5}
\]
Thus the agreement of left- and right-endpoint orders is automatic for
distinct equal-rank targets; it is not an additional factor assumption.

### 2.1 Exact rank-capped-start inequality

Every universal word in this setup satisfies
\[
\boxed{
V_a\le\sum_{i=1}^{M_a}d_i+(3a-1)D.
}
\tag{2.6}
\]

To prove it, choose one witness for every nonzero below-middle target and
group these lower witnesses by their left endpoint.

At a selected middle start \(\ell_i\), a lower witness must end before
\(r_i\); otherwise it contains \(I_i\), and its maximum dominates a
rank-\(3a\) target.  There are at most \(d_i\) possible endpoints.

There are exactly \(D\) physical starts not among the \(M_a\) selected
middle starts.  At any one fixed start, increasing the right endpoint
produces a chain of maxima.  A chain of distinct nonzero targets below rank
\(3a\) contains at most one target in each rank \(1,\ldots,3a-1\), hence at
most \(3a-1\) targets.  Summing the two contributions proves (2.6).

### 2.2 Exact necessary run inequality

Fix one coordinate increment and write its incidence on the ordered middle
targets.  Let \([u,v]\) be an internal positive run.  The preceding negative
interval \(I_{u-1}\) forbids that increment through position \(r_{u-1}\);
the following negative interval \(I_{v+1}\) forbids it from position
\(\ell_{v+1}\) onward.  Any occurrence serving any positive witness in the
run must therefore lie strictly between these two forbidden intervals.
Consequently
\[
r_{u-1}+2\le\ell_{v+1},
\]
or, using (2.3),
\[
\boxed{
\beta_{u-1}-\alpha_{v+1}\le v-u.
}
\tag{2.7}
\]

This proof does not assume one pin common to the entire positive run.
One occurrence in any positive witness already forces the nonempty
corridor.  Thus (2.7) is necessary for general multipin factorability.
It is not asserted to be sufficient.

Writing \(k=v-u\), (2.7) and monotonicity give, for every index \(i\),
\[
d_i\le
\begin{cases}
k+\alpha_{v+1}-\alpha_i,&i<u,\\[1mm]
k+(\beta_i-\beta_{u-1})+(\alpha_{v+1}-\alpha_i),
   &u\le i\le v,\\[1mm]
k+\beta_i-\beta_{u-1},&i>v.
\end{cases}
\tag{2.8}
\]
The middle line follows by inserting
\(\beta_{u-1}-\alpha_{v+1}\) between \(\beta_i\) and
\(\alpha_i\).  Formula (2.8) is the complete charging inequality used
below.

## 3. Audit of the literal triangular-shell word

For \(t\ge1\), the block \(\mathcal C_t\) consists of:

- \(t+1\) points on the edge from \(A_t\) to \(B_t\);
- \(t\) new points from just after \(B_t\) through \(C_t\);
- \(t\) new points from just after \(C_t\) through the terminal \(A_t\).

Therefore
\[
|\mathcal C_t|=3t+1.
\tag{3.1}
\]
Replacing the four-entry block \(\mathcal C_1\) by
\((B_1,C_1,A_1)\) saves one entry, so for \(R\ge2\)
\[
\begin{aligned}
|W_R|
&=3+\sum_{t=2}^R(3t+1)\\
&=\boxed{\frac{3R(R+1)}2+R-1}.
\end{aligned}
\tag{3.2}
\]

### 3.1 Coverage for shells \(t\ge2\)

Let \((x,y,z)\ne(0,0,0)\), and let
\(t=\max(x,y,z)\).  For \(t\ge2\), use the following priority order.

**Case 1: \(y=t\).**  The interval
\[
(x,t-x,0)\longrightarrow B_t\longrightarrow(0,t-z,z)
\]
lies in the first two sides of \(\mathcal C_t\).  Along it the respective
coordinate maxima are \(x,t,z\), so its maximum is \((x,t,z)\).
This includes all ties involving \(y=t\).

**Case 2: \(y<t\) and \(z=t\).**  The interval
\[
(0,y,t-y)\longrightarrow C_t\longrightarrow(x,0,t-x)
\]
lies in the second and third sides.  Its maximum is \((x,y,t)\).
The endpoint cases \(x=0\) and \(y=0\) are included.

**Case 3: \(x=t\), \(y<t\), and \(z<t\).**  Begin in the third side of
\(\mathcal C_{t-1}\) at
\[
(t-1-z,0,z),
\]
take its suffix through the terminal \(A_{t-1}\), cross the seam to the
initial \(A_t\), and stop on the first side of \(\mathcal C_t\) at
\[
(t-y,y,0).
\]
The old suffix has \(z\)-maximum \(z\), the seam supplies \(x=t\), and the
new prefix has \(y\)-maximum \(y\).  The resulting maximum is
\((t,y,z)\).  The endpoint \(z=t-1\) starts at \(C_{t-1}\), while \(z=0\)
starts at the terminal \(A_{t-1}\); both are legitimate.

At \(t=2\), the only possible starts in the shortened preceding block are
\(C_1\) and \(A_1\), exactly the two points retained.  Hence the seam
argument has no hidden failure at its smallest value.

### 3.2 The exceptional shell \(t=1\)

The first displayed recipe in the raw report is not literal when
\(t=1,x=1\), because the initial occurrence \(A_1\) was deleted.
Accordingly the generic recipes must be stated only for \(t\ge2\).

The shortened word \(B_1,C_1,A_1\) has the following maxima:
\[
\begin{array}{c|c}
\text{interval}&\text{maximum}\\ \hline
[B_1]&(0,1,0)\\
[C_1]&(0,0,1)\\
[A_1]&(1,0,0)\\
[B_1,C_1]&(0,1,1)\\
[C_1,A_1]&(1,0,1)\\
[B_1,C_1,A_1]&(1,1,1).
\end{array}
\]
The seventh max-one target, \((1,1,0)\), occurs as a singleton on the first
side of \(\mathcal C_2\).  This is why \(R\ge2\) is essential to the stated
construction.  All seven max-one boundary cases are now accounted for.

Combining Sections 3.1 and 3.2 proves
\[
\boxed{
g_3(R,R,R)\le\frac{3R(R+1)}2+R-1
\qquad(R\ge2).
}
\tag{3.3}
\]
This is a literal contiguous-OR word; it does not invoke a labelled
factor or a shadow-to-pin implication.

### 3.3 Exact width and excess

For \(R=2s\), the unique central rank is \(3s\).  Inclusion-exclusion gives
\[
\begin{aligned}
w_R
&=\binom{3s+2}{2}-3\binom{s+1}{2}\\
&=3s^2+3s+1.
\end{aligned}
\tag{3.4}
\]
No double upper-bound violation can occur at this rank.

For \(R=2s+1\), either central rank may be used; at rank \(3s+1\),
\[
\begin{aligned}
w_R
&=\binom{3s+3}{2}-3\binom{s+1}{2}\\
&=3(s+1)^2.
\end{aligned}
\tag{3.5}
\]
Again there is no double upper-bound violation.

The length and excess in the two parities are
\[
\begin{array}{c|c|c}
R&|W_R|&|W_R|-w_R\\ \hline
2s&6s^2+5s-1&3s^2+2s-2\\
2s+1&6s^2+11s+3&3s^2+5s.
\end{array}
\tag{3.6}
\]
Equivalently,
\[
\boxed{
|W_R|=2w_R-\left\lfloor\frac R2\right\rfloor-3.
}
\tag{3.7}
\]
Thus \(|W_R|=(2-o(1))w_R\), and its excess over width is
\(\frac34R^2+O(R)\).  The raw formulas are exact.

## 4. Arbitrary contiguous-ring cuts

Translate the middle layer to
\[
H_a=\{(x,y,z):x+y+z=0,\ |x|,|y|,|z|\le a\}.
\]
The positive-radius-\(r\) ring has \(6r\) vertices.  Each of
\[
x=r,\qquad y=r,\qquad z=r
\tag{4.1}
\]
is the support of a coordinate threshold on an arc of \(r+1\) consecutive
vertices.  These three arcs are disjoint.  A linear cut of the cyclic ring
has two boundary vertices, so at least one of the three arcs contains
neither boundary vertex and remains an internal positive run.  This
argument includes \(r=1\).  It also covers an outer ring and a ring block
placed first or last globally, because both neighbors of the chosen run lie
inside that ring block.

Choose one such run \([u_r,v_r]\) on every ring.  Its run parameter is
\[
v_r-u_r=r.
\tag{4.2}
\]
Apply (2.8) to every one of the \(6r\) indices in that ring block.  Every
index contributes base at most \(r\), for total \(6r^2\).

Every \(\alpha\)-difference charged by these indices lies inside the same
ring block, and any fixed difference is charged by at most \(6r\le6a\)
indices.  The ring blocks are disjoint, so all \(\alpha\)-charges together
are at most \(6aD\).  The identical argument bounds all \(\beta\)-charges
by \(6aD\).  The center, which is the only radius-zero target, contributes
at most \(D\).  Therefore
\[
\boxed{
\sum_{i=1}^{M_a}d_i
\le6\sum_{r=1}^a r^2+(12a+1)D
=2a^3+3a^2+a+(12a+1)D.
}
\tag{4.3}
\]

This is a complete proof with one run per ring; no common-pin condition and
no assumption \(D=O(a)\) is used.  Since for every \(a\ge1\)
\[
2a^3+3a^2+a\le2a^3+6a^2+4a+1
\]
and
\[
12a+1\le18a,
\]
(4.3) proves the raw inequality
\[
\boxed{
\sum_i d_i\le2a^3+6a^2+4a+1+18aD.
}
\tag{4.4}
\]

Combining (4.4) with (2.6) gives exactly
\[
\boxed{
D\ge
\frac{2a^3-\frac32a^2-\frac52a-2}{21a-1}.
}
\tag{4.5}
\]
The numerator can be negative for small \(a\), in which case the displayed
real inequality is merely vacuous.  Its asymptotic content is nevertheless
exact:
\[
D\ge\left(\frac2{21}+o(1)\right)a^2.
\tag{4.6}
\]

Using the stronger ledger (4.3) instead gives
\[
\boxed{
D\ge
\frac{2a^3+\frac32a^2+\frac12a-1}{15a}
=\left(\frac2{15}+o(1)\right)a^2.
}
\tag{4.7}
\]
Thus the report's arbitrary-cut constant is valid but nonsharp.

The quantifier is architecture-local: the order induced by the chosen
middle witnesses must consist of complete contiguous radius-ring blocks.
Their cuts, orientations, coordinate names, and block permutation may all
be arbitrary.  The conclusion does not apply once arcs from distinct radii
are genuinely interleaved in the induced witness order.

## 5. Canonical-cut certificate

The raw report did not define its canonical cut.  The following standard
outward enumeration supplies a precise interpretation and proves its
claimed constant.

Put the center at index \(1\).  For \(1\le r\le a\), let
\[
b_r=2+3r(r-1)
\tag{5.1}
\]
be the first index of radius \(r\), and put
\[
B_{r,k}=[b_r+kr,\ b_r+(k+1)r-1],
\qquad0\le k\le5.
\tag{5.2}
\]
Starting at \(c_r=(r,-r,0)\), the six half-open blocks list, for
\(0\le t<r\), the following vertices:
\[
\begin{array}{c|c}
k&\text{vertex in }B_{r,k}\\ \hline
0&(r,-r+t,-t)\\
1&(r-t,t,-r)\\
2&(-t,r,-r+t)\\
3&(-r,r-t,t)\\
4&(-r+t,-t,r)\\
5&(t,-r,r-t).
\end{array}
\tag{5.3}
\]
These are the \(6r\) vertices exactly once.

Define the two internal extreme runs
\[
Y_r=[b_r+2r,\ b_r+3r],\qquad
Z_r=[b_r+4r,\ b_r+5r].
\tag{5.4}
\]
They are respectively the supports of \(y\ge r\) and \(z\ge r\), have
\(r+1\) vertices, and hence have run parameter \(r\).
The immediate neighbors of \(Y_r\) have \(y<r\).  The immediate neighbors
of \(Z_r\) have \(z<r\); for \(r\ge2\) they lie in the same ring.  When
\(r=1<a\), the right zero neighbor of \(Z_1\) is the first point \(c_2\).
Thus every run used below is internal when \(a\ge2\).  The case \(a=1\)
will be handled separately.

### 5.1 Assignment and base term

On ring \(1\):

- assign \(B_{1,0}\cup B_{1,1}\) forward to \(Y_1\);
- assign \(B_{1,2}\cup B_{1,3}\) to \(Y_1\);
- assign \(B_{1,4}\cup B_{1,5}\) to \(Z_1\).

On each ring \(r\ge2\):

- assign \(B_{r,0}\cup B_{r,1}\) backward to \(Z_{r-1}\);
- assign \(B_{r,2}\cup B_{r,3}\) to \(Y_r\);
- assign \(B_{r,4}\cup B_{r,5}\) to \(Z_r\).

Charge the center separately by \(d_1\le D\).  The six ring-one indices
each pay base \(1\).  At radius \(r\ge2\), the first \(2r\) indices pay
base \(r-1\), and the remaining \(4r\) indices pay base \(r\).  Hence the
total base is
\[
\begin{aligned}
6+\sum_{r=2}^a\bigl(2r(r-1)+4r^2\bigr)
&=2a^3+2a^2+2.
\end{aligned}
\tag{5.5}
\]

### 5.2 Exact variation congestion

Write
\[
\Delta\alpha_j=\alpha_j-\alpha_{j-1},\qquad
\Delta\beta_j=\beta_j-\beta_{j-1}.
\]
Each total variation is at most \(D\).

For the \(\alpha\)-charges in (2.8):

- the two indices of \(B_{1,0}\cup B_{1,1}\) give two forward differences
  ending at \(v(Y_1)+1\);
- among the indices assigned to \(Y_r\), only the \(r+1\) indices actually
  in \(Y_r\) have an \(\alpha\)-term;
- among the indices assigned to \(Z_r\), only the \(r+1\) indices actually
  in \(Z_r\) have an \(\alpha\)-term;
- the increment ranges belonging to different runs are disjoint, apart
  from the two ring-one forward charges overlapping the \(Y_1\) charges.

Thus a fixed \(\Delta\alpha_j\) is charged at most
\[
\max(4,a+1)\le a+2
\qquad(a\ge2)
\]
times.  The total \(\alpha\)-charge is at most \((a+2)D\).

For the \(\beta\)-charges:

- the \(2r\) indices assigned to \(Y_r\) give congestion at most \(2r\);
- the \(2r\) indices assigned to \(Z_r\) give congestion at most \(2r\);
- the first two side blocks of ring \(r+1\), assigned backward to \(Z_r\),
  give congestion at most \(2(r+1)\);
- a \(Y_r\) range is disjoint from every other \(\beta\)-range, while a
  \(Z_r\) range overlaps only the backward range coming from the first two
  sides of ring \(r+1\).

There are no triple overlaps.  In the only double overlap,
\[
2r+2(r+1)=4r+2\le4a-2
\qquad(r\le a-1).
\]
Every other multiplicity is smaller, so the total \(\beta\)-charge is at
most \((4a-2)D\).

Combining (2.8), (5.5), the two variation bounds, and the center yields
\[
\boxed{
\sum_i d_i
\le2a^3+2a^2+2+(5a+1)D
\qquad(a\ge2).
}
\tag{5.6}
\]

If \(D=0\), every \(d_i=0\).  If \(D\ge1\) and \(a\ge2\), then
\[
1+(5a+1)D\le7aD.
\]
Thus (5.6) implies the exact raw bound
\[
\boxed{
\sum_i d_i\le2a^3+2a^2+1+7aD.
}
\tag{5.7}
\]
For \(a=1\), the trivial estimate
\(\sum_i d_i\le M_1D=7D\) also implies (5.7).  This covers the small ring,
center, and outer boundary cases.

Combining (5.7) with (2.6) gives the exact consequence omitted from the raw
report:
\[
\boxed{
D\ge
\frac{2a^3+\frac52a^2+\frac32a-2}{10a-1}
=\left(\frac15+o(1)\right)a^2.
}
\tag{5.8}
\]
For \(a\ge2\), the stronger certificate (5.6) gives
\[
\boxed{
D\ge
\frac{2a^3+\frac52a^2+\frac32a-3}{8a}
=\left(\frac14+o(1)\right)a^2.
}
\tag{5.9}
\]
Therefore the raw canonical constant is valid, but the raw report was
missing its definition and proof and its constant is nonsharp.

## 6. Fixed-coordinate raster audit

Work first in \([0,2a]^3\) at rank \(3a\).  For fixed \(x\), the row has
\[
L_x=\max(0,a-x)\le y\le
U_x=\min(2a,3a-x).
\tag{6.1}
\]
There are \(2a+1\) rows, and every row has at most \(2a+1\) targets.
The architectural hypothesis is:

- the order induced by increasing left endpoints of the selected middle
  witnesses has the rows in increasing \(x\);
- every row is contiguous;
- within each row, \(y\) is monotone, with either orientation allowed
  independently.

A literal visual traversal of the rows is not enough if the chosen middle
witness intervals induce some different order.

Let \(e_x\) be the target with \(y=U_x\).  Consider the threshold
\(y\ge U_x\).

If \(x\le a\), then \(U_x=2a\).  Each relevant row contributes only its
maximum-\(y\) endpoint to this threshold.  Such singleton endpoints can
join across at most one row seam, since a nontrivial row endpoint cannot
simultaneously be the first and last point of its row.

If \(x>a\), then \(U_{x-1}=U_x+1\) and \(U_{x+1}=U_x-1\).  The component
through \(e_x\) contains \(e_x\) and, at worst, the top two points of row
\(x-1\).  That two-point terminal segment is preceded within its row by a
negative point, so it cannot continue through another seam.

Thus in every case the positive component through \(e_x\) has at most three
ordered targets.  Except for the endpoints belonging to the first and last
global rows, it is an internal run \([u_x,v_x]\) with
\[
v_x-u_x\le2.
\tag{6.2}
\]

For an internal endpoint \(e=e_x\), (2.8) gives
\[
d_e\le
2+(\beta_e-\beta_{u_x-1})
(\alpha_{v_x+1}-\alpha_e).
\tag{6.3}
\]
There are only two boundary exceptions, each bounded trivially by \(D\).
A direct check of the two component shapes just described shows that each
\(\alpha\)-increment and each \(\beta\)-increment is charged by at most two
row endpoints: on the plateau the only overlap is a pair of singleton
endpoints across one seam, and on the descending part the only overlap is
the endpoint together with the adjacent two-point terminal segment.
Therefore the internal variation charge is at most \(4D\).  Enlarging the
base by four harmless units gives the report's exact convenient bound
\[
\boxed{
\sum_x d_{e_x}\le2(2a+1)+6D.
}
\tag{6.4}
\]
This includes both global boundary orientations.

### 6.1 The reported interpolation and constant

The index distance between consecutive selected row endpoints is at most
\(4a+2\).  Assigning every middle index to a neighboring endpoint and using
monotonicity gives
\[
d_i\le
\begin{cases}
d_e+\alpha_e-\alpha_i,&i<e,\\
d_e+\beta_i-\beta_e,&i>e.
\end{cases}
\tag{6.5}
\]
The assignment load and the variation congestion are each at most
\(4a+2\).  With (6.4),
\[
\boxed{
\sum_i d_i\le(4a+2)(4a+2+8D).
}
\tag{6.6}
\]
Combining this with (2.6), the coefficient of \(D\) is
\[
8(4a+2)+(3a-1)=35a+15.
\]
Hence
\[
\boxed{
D\ge
\frac{V_a-(4a+2)^2}{35a+15}
=\left(\frac4{35}+o(1)\right)a^2.
}
\tag{6.7}
\]
The numerator is negative for some small \(a\), making the real inequality
vacuous there, but the exact algebra and asymptotic constant are correct.

### 6.2 A stronger direct row charge

Every index in a row can instead be assigned directly to that row's own
endpoint \(e_x\).  The row has at most \(B=2a+1\) indices.  Summing (6.5)
inside disjoint row blocks charges the endpoint widths at most \(B\) times
and each offset variation at most \(B\) times.  Consequently
\[
\begin{aligned}
\sum_i d_i
&\le B\left(\sum_xd_{e_x}+2D\right)\\
&\le(2a+1)(4a+2+8D).
\end{aligned}
\tag{6.8}
\]
Together with (2.6), this proves the stronger exact estimate
\[
\boxed{
D\ge
\frac{V_a-2(2a+1)^2}{19a+7}
=
\frac{4a^3-\frac72a^2-\frac{13}{2}a-3}{19a+7}
=\left(\frac4{19}+o(1)\right)a^2.
}
\tag{6.9}
\]
Thus the raw raster obstruction is valid but not optimized.

### 6.3 Balanced rectangular boxes

Let
\[
\delta R\le p,q,r\le CR
\]
with fixed \(\delta,C>0\), and let \(h\) be a central rank of
\([0,p]\times[0,q]\times[0,r]\).  In the fixed-\(x\) raster, the \(y\)-range
of row \(x\) is
\[
\max(0,h-x-r)\le y\le\min(q,h-x).
\tag{6.10}
\]
There are \(\Theta_{\delta,C}(R)\) nonempty rows, every row has
\(O_C(R)\) targets, and consecutive row maxima change by at most one.
The endpoint threshold component therefore has uniformly bounded size,
with only the first and last global rows as boundary exceptions.

The analogue of (6.4) is
\[
\sum_xd_{e_x}=O_{\delta,C}(R+D),
\]
and direct row interpolation gives
\[
\sum_i d_i=O_{\delta,C}(R^2+RD).
\tag{6.11}
\]
The box has \(\Theta_{\delta,C}(R^3)\) points.  Rank symmetry and the
\(O_C(R^2)\) central width show that the number of nonzero targets strictly
below the central rank is \(\Theta_{\delta,C}(R^3)\), while
\(h=O_C(R)\).  The rank-capped-start inequality therefore yields
\[
\Theta_{\delta,C}(R^3)
\le O_{\delta,C}(R^2+RD),
\]
and hence
\[
\boxed{D=\Omega_{\delta,C}(R^2).}
\tag{6.12}
\]
This validates the rectangular statement after supplying its omitted
uniformity argument.  It remains a theorem only for the designated
fixed-coordinate, contiguous, monotone-row induced witness order.

## 7. Ordered compression of the shell occurrences

Let \(T_1,\ldots,T_L\), where \(L=|W_R|\), denote every virtual occurrence
of the shell word in order, including repeated occurrences of a shell
endpoint.  Assume that a physical word of length \(n\) represents each
\(T_i\) by a nonempty integer interval
\[
J_i=[a_i,b_i],
\]
with both endpoint sequences nondecreasing and with
\(\max J_i=T_i\).

If \(b_{i+1}=b_i\), then \(a_i\le a_{i+1}\) gives
\[
J_{i+1}\subseteq J_i,
\]
and hence
\[
T_{i+1}\le T_i.
\tag{7.1}
\]
Inside one shell block, every adjacent pair consists of distinct points of
the same rank and is therefore incomparable.  This includes every adjacency
of the shortened block \(B_1,C_1,A_1\).  At the seam between shells,
\[
T_i=A_t<A_{t+1}=T_{i+1},
\]
which also contradicts the reverse comparison (7.1).  Thus
\[
b_1<b_2<\cdots<b_L.
\]
There are only \(n\) possible right endpoints, so
\[
\boxed{n\ge L=|W_R|.}
\tag{7.2}
\]

Equality is attained by the physical word \(W_R\) itself with singleton
certificates \(J_i=[i,i]\).  Therefore the occurrence-by-occurrence optimum
under the two monotone endpoint orders is exactly
\[
\boxed{
\frac{3R(R+1)}2+R-1.
}
\tag{7.3}
\]

The quantifiers here are essential.  This theorem does not cover:

- a construction that does not assign a factor to every virtual occurrence;
- deletion or rebundling followed by a new literal coverage proof;
- endpoint sequences that cross because occurrences from different shells
  have different ranks;
- a different order of the shell occurrences; or
- an unrelated physical word covering the same target box.

If a linked-factor transfer is intended, adjacent physical factors also
need the appropriate connected-union property.  The lower bound (7.2) does
not require that extra hypothesis, and the singleton equality construction
satisfies it.

## 8. Implication-scope audit

The exact surviving theorem ledger is:

- \(W_R\) is an unconditional literal word of length
  \((2-o(1))w_R\).
- Every universal word whose selected middle witnesses induce complete
  contiguous radius-ring blocks has \(D=\Omega(a^2)\).  The certified
  arbitrary-cut leading constant is \(2/15\), stronger than the report's
  \(2/21\).
- The standard canonical ring cut has certified leading constant \(1/4\),
  stronger than the report's \(1/5\).
- Every universal word whose selected middle witnesses induce the stated
  fixed-coordinate raster has \(D=\Omega(a^2)\).  The direct-row constant is
  \(4/19\), stronger than the report's \(4/35\).
- This particular shell occurrence sequence has no shorter
  occurrence-by-occurrence representation with both endpoint orders
  monotone.

The raster proof supports the following robust formulation, and no broader
one without additional hypotheses.  Suppose an ordered middle family of
\(\Theta(R^2)\) targets has:

1. \(\Theta(R)\) sampled targets whose consecutive index gaps are \(O(R)\);
2. for every sampled target except \(O(1)\) boundary exceptions, an internal
   positive threshold component of uniformly bounded size;
3. bounded overlap in the offset-variation charge intervals; and
4. an interpolation assignment of load \(O(R)\) from all targets to the
   samples.

Then
\[
\sum_i d_i=O(R^2+RD),
\]
and a balanced-box lower volume of \(\Theta(R^3)\) forces
\(D=\Omega(R^2)\).  The raw phrase “every \(O(R)\)-spaced net of bounded
components” silently needs all four conditions.

Accordingly, the following statements in the raw “Exact surviving gap” are
not proved as universal necessities:

- **Positive-proportion radius interleaving.**  The audit has no stability
  theorem saying how many rings must be broken.  It proves only that keeping
  all complete rings as contiguous blocks fails.
- **Avoidance of every bounded-component net.**  This is valid only with
  the mesh, boundary, overlap, and interpolation hypotheses just stated.
- **Long cross-radius coordinate corridors.**  This is a reasonable design
  response to the ring and raster obstructions, but it is not a theorem.

The ordered-compression conclusion must also be stated as a trichotomy:
a compression of this virtual shell word must abandon monotone occurrence
endpoints, change the virtual order, or abandon occurrence-by-occurrence
representation and prove coverage anew.

Finally, upper-shadow or meet-shadow coverage alone is not a literal
contiguous-OR theorem.  A factor-based proof must keep the required labels
and lower-target pins integral inside one exact physical factor.  A direct
literal word, such as \(W_R\), bypasses that separate transfer obligation by
exhibiting the actual intervals.

Nothing in this report proves
\[
g_3(at,bt,ct)=w(at,bt,ct)+o(t^2)
\]
for any general primitive positive triple, including the cubic ray.  The
compact balanced three-box theorem remains open, and none of the
architecture-specific lower bounds may be promoted to an unrestricted
quadratic lower bound.
