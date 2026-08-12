# Cross-port telescope audit for the truncated static rotor cube

Date: 2026-07-25

Method: pure mathematics only.

## 0. Result

There is a genuine local telescope which is not visible in the audit of one
flush/reload route.  At an internal port (j), pair the source flush of

\[
 C_{j-1}\longrightarrow A_j
\]

with the source flush of

\[
 A_j\longrightarrow B_j.
\]

The two source states have the same phase.  Their cores differ by the one
crossing column swap \(\beta_j\), and the first tail choices in the two
routes are the two opposite labels of that swap.  Consequently their
``core plus first tail label'' sets are exactly equal.  The two routes can
also use the same buffer labels.  This makes their long source-flush traces
directly comparable.

Fix row (i), and write (x=x^j), (z=x^{j-1}).  Let

\[
 D_j=\{k:x_k^j=x_k^{j-1}\}
\tag{0.1}
\]

be the set of rows which do not change between the two columns.  In the
upper collar half (Q<h<2Q), the paired source trace for the whole-row
toggle \(\alpha_i\) has the following exact behavior.

* If (i\in D_j), all ordinary terms cancel.  For every
  (k\in D_j-\{i\}), exactly one four-mask
  \(\alpha_i\)-by-\(\alpha_k\) rectangle remains.  These rectangles have
  disjoint supports.  Hence

  \[
  \boxed{\|\Delta^{\rm src,+}_{i,j}\|_2^2
  =4(|D_j|-1).}
  \tag{0.2}
  \]

* If (i\notin D_j), the two source traces have the same rather than
  opposite orientation.  Away from the at most (p-1) row-interaction
  ranks they double.  Therefore

  \[
  \boxed{\|\Delta^{\rm src,+}_{i,j}\|_2^2
  \ge16(Q-p).}
  \tag{0.3}
  \]

It follows pointwise, for every pair of adjacent column signatures, that

\[
 \boxed{
 \sum_{i=0}^{p-1}\|\Delta^{\rm src,+}_{i,j}\|_2^2
 \ge4p(p-1).}
\tag{0.4}
\]

Thus the same-phase pairing does not produce a bounded row-update kernel.
It merely converts the original \(\Omega(Q)\)-rank trace into explicit
row-by-row interaction rectangles when a row is unchanged between the two
columns.

For the especially favorable constant-column choice

\[
 x^0=x^1=\cdots=x^{t-1},
\tag{0.5}
\]

all rows lie in every (D_j).  The surviving rectangle attached to
\((i,k,j)\) has a positional base which loses the two new left-boundary
labels and gains the two new right-boundary labels when (j) increases by
one.  The four selectable row labels are disjoint from these moving
boundary labels.  Hence rectangles at different ports have disjoint
supports.  In this case the residual is already aggregate in time:

\[
 \boxed{
 \sum_i\left\|\sum_{j=1}^{t-1}
       \Delta^{\rm src,+}_{i,j}\right\|_2^2
 =4p(p-1)(t-1)=\Theta(MQ).}
\tag{0.6}
\]

There is therefore no cross-port telescope for the constant-column cube
vertex.  Alternating or partially changing columns removes some of these
rectangles, but replaces them with the doubled ordinary traces in (0.3).
The local lower bound (0.4) remains.  A completely general aggregate
lower bound for arbitrary changing columns would additionally have to rule
out buffer-dependent matches between a (K)-term at one port and a
special (J)-term at another.  That last equality problem is not settled
here; the fixed positional rectangles in (0.2), including all of (0.6),
cannot participate in such a cancellation.

## 1. Phase and collar positions

Put (n=2Q).  At phase (s_j=2j), write the base collar in the form

\[
 z_1,z_2,\ldots,z_n.
\]

The row transposition \(\alpha_i\) occupies adjacent collar positions

\[
 r_i(j),\ r_i(j)+1,
 \qquad
 r_i(j)=Q-a_i+s_j
\tag{1.1}
\]

with the harmless global shift caused by the cut convention.  Since

\[
 a_i=4t+2i,
\]

we have

\[
 r_k(j)-r_i(j)=2(i-k).
\tag{1.2}
\]

The active row pairs all lie below the middle-owner collar boundary:

\[
 r_i(j)<Q.
\tag{1.3}
\]

For a source transposition at positions (r,r+1), the one-route audit
decomposes its flush trace into:

1. boundary terms (K_h), (h=r,r+1,\ldots,n);
2. opposite special-state terms (J_h), (h=0,1,\ldots,n).

At (h=n), the two terms cancel.  At every (r<h<n), their four masks
are distinct.

## 2. Why the two source cores normalize exactly

Let (A) be the unordered core of (A_j), and let the crossing column
swap be

\[
 \beta_j=(a\ b),\qquad a\in A,\quad b\in B.
\]

The source core of (C_{j-1}\) is

\[
 A-a+b,
\]

whereas the source core of (A_j\) is (A).  The incoming route

\[
 C_{j-1}\longrightarrow A_j
\]

uses (b) as its core element to remove and (a) as its first tail
choice.  The outgoing route

\[
 A_j\longrightarrow B_j
\]

uses (a) as its core element to remove and (b) as its first tail
choice.  Hence

\[
 (A-a+b)+a=A+b.
\tag{2.1}
\]

All later boundary bases (K_h), and all special bases (J_h), depend on
the source core and first tail choice only through this common augmented
set.  Choose the (2Q) buffer labels in the common core (A-a), and use
the same ordered buffer list in both routes.  This is legal because

\[
 |A-a|=m-Q-1\ge2Q
\]

in the calibrated regime.

The sole boundary base which does not use (2.1) is the initial (K_r)
term.  It lies below the upper-half projection used in (0.2)--(0.4).

## 3. The source trace as an affine row-interaction expansion

Fix (i), orient its two labels canonically, and let

\[
 \mathcal D_{i,j}(y_{-i})
\]

denote the upper-half source-flush difference when the other row-pair
orientations are (y_{-i}).  The sign of the actual toggle is

\[
 \epsilon(y_i)=1-2y_i.
\tag{3.1}
\]

Only one boundary term can notice a fixed other row pair.

* If (k<i), its collar positions lie after those of (i).  It is split
  once in a (K)-base, at rank

  \[
  h_{ik}=n+1-2(i-k).
  \tag{3.2}
  \]

* If (k>i), its collar positions lie before those of (i).  It is split
  once in a (J)-base, at rank

  \[
  h_{ik}=n+1-2(k-i).
  \tag{3.3}
  \]

All these ranks satisfy

\[
 h_{ik}\ge n+1-2(p-1)>Q.
\tag{3.4}
\]

At every other upper-half rank the source trace is independent of all
other row orientations.  Consequently there are four-mask rectangles
\(R_{ik,j}\) such that

\[
 \boxed{
 \mathcal D_{i,j}(y_{-i})
 =\mathcal D^0_{i,j}
  +\sum_{k\ne i}y_kR_{ik,j}.}
\tag{3.5}
\]

Here the two terms with (k=i-d) and (k=i+d), when both exist, live at
the same rank but have disjoint support.  The first contains exactly one
label of row pair (i-d) and both labels of row pair (i+d); the second
has the reverse property.  Hence all the rectangles in (3.5) are
orthogonal, even when their ranks agree, and

\[
 \|R_{ik,j}\|_2^2=4.
\tag{3.6}
\]

This affine formula is exact.  There are no higher row interactions: a
prefix boundary can split at most one of the disjoint adjacent row pairs.

## 4. Pairing consecutive columns

At phase (s_j), the outgoing source (A_j) has row signature (x^j).
The incoming source (C_{j-1}) has row signature

\[
 \mathbf1-x^{j-1}.
\]

Under the whole-row (i) toggle, the paired source difference is therefore

\[
\begin{aligned}
 \Delta^{\rm src,+}_{i,j}
  ={}&\epsilon(x_i^j)\mathcal D_{i,j}(x^j_{-i})\\
    &-\epsilon(x_i^{j-1})
      \mathcal D_{i,j}((\mathbf1-x^{j-1})_{-i}).
\end{aligned}
\tag{4.1}
\]

This displays the exact cancellation condition:

\[
 \boxed{
 x_i^j=x_i^{j-1},qquad
 x_k^j=1-x_k^{j-1}\quad(k\ne i).}
\tag{4.2}

When (4.2) holds, the entire upper-half source trace for row (i)
cancels.

Suppose first that (i\in D_j).  The common terms in (4.1) have opposite
sign.  A row (k\ne i) cancels precisely when (k\notin D_j), and leaves
one signed copy of (R_{ik,j}) precisely when (k\in D_j).  Equations
(3.6) and the support disjointness prove (0.2).

Now suppose (i\notin D_j).  Then the two source states have the same
orientation at row (i), so their row-toggle traces have the same sign.
There are (Q-1) upper-half ranks (Q<h<n).  At most (p-1) are the
interaction ranks (3.2)--(3.3).  At every remaining rank the two identical
source traces double.  A single trace there consists of two disjoint
transposition edges and has squared norm four, so the doubled trace has
squared norm sixteen.  This proves (0.3).

Let (d=|D_j|).  Summing (0.2)--(0.3) gives

\[
 \sum_i\|\Delta^{\rm src,+}_{i,j}\|_2^2
 \ge4d(d-1)+16(p-d)(Q-p).
\tag{4.3}
\]

Since the compilation has (p\le Q/2), the right side is minimized at
(d=p), where it equals (4p(p-1)).  This proves (0.4).

Notice also why the conditions cannot hold for every row simultaneously.
For row (i), (4.2) asks that row (i) be unchanged and every other row
be complemented.  Two different choices of (i) impose contradictory
requirements as soon as (p\ge2).

## 5. Exact positional support of the residual rectangles

The support description is simplest in the underlying cyclic positions.
Let the pair \(\alpha_i\) occupy the two positions adjacent to cut (a_i).
Up to the common one-step cut-index convention, the common base of
\(R_{ik,j}\) is the union of the two positional arcs

\[
 \boxed{
 [s_j-Q,\ a_{\min(i,k)}-2]
 \ \cup\ 
 [a_{\max(i,k)}+1,\ s_j+m],}
\tag{5.1}
\]

and each of its four masks is obtained by choosing one label from the
\(\alpha_i\)-pair and one from the \(\alpha_k\)-pair.  Formula (5.1) can
equivalently be read directly from the collar bases: it consists of the
common augmented core, the prefix before the later collar boundary, and
the suffix after the earlier collar boundary.

When (j\) is increased by one, (s_j) increases by two.  The base in
(5.1) loses two labels at its left moving boundary and gains two labels at
its right moving boundary.  These four labels are disjoint from every row
pair by the calibration inequalities.  Therefore

\[
 \operatorname{supp}R_{ik,j}
 \cap\operatorname{supp}R_{ik,j'}=\varnothing
 \qquad(j\ne j').
\tag{5.2}
\]

The same membership signature shows disjointness if (k) is changed:
the masks in (R_{ik,j}) contain exactly one label from row pair (k),
whereas a rectangle indexed by a different row pair contains either both
or neither, except for the symmetric (i-d,i+d) case already separated in
Section 3.

For constant columns, every (D_j=[p]).  Equations (0.2), (3.6), and
(5.2) now sum without any aggregate cancellation and give (0.6).

The target-reload traces cannot cancel these rectangles: target order
differences are supported only at (h\le r_i(j)<Q), whereas every
rectangle rank (3.2)--(3.3) is strictly greater than (Q).  The two cyclic
bridge steps likewise see a row swap only at its lower collar boundary and
do not enter these upper ranks.

## 6. Consequence and remaining loophole

The hoped-for identity

\[
 \sum_j C_{ij}=O(1)
\]

does not follow from pairing the two source flushes at each phase.  The
pairing has an exact kernel, but it is the code

\[
 x^j=x^{j-1}\ \text{at row }i,qquad
 x^j=\mathbf1-x^{j-1}\ \text{off row }i,
\]

which is different for every (i).  Its unavoidable simultaneous defect
is the quadratic lower bound (0.4).

For the constant-column vertex, the defect survives aggregation exactly
as (0.6); no choice of buffers can change it because the residual bases
(5.1) are buffer-free.  For arbitrary changing columns, (0.3) supplies a
large local defect.  Proving that all of those doubled ordinary traces
also survive aggregation would require excluding cross-port equalities
between buffer-dependent special (J)-bases and ordinary (K)-bases.
The present calculation neither assumes nor proves that final exclusion.

Thus the same-phase telescope is real but insufficient.  It replaces a
vague connector-variance problem by two exact alternatives:

1. buffer-free, cross-port-disjoint interaction rectangles when consecutive
   columns retain several common rows;
2. doubled ordinary source traces when consecutive columns complement
   those rows.

Any successful global coboundary must cancel the second alternative while
also avoiding the first for all (p) row-update directions.  The current
static cube chronology supplies no such simultaneous code.
