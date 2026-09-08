# The clean paired package and its four halos are arcs of one tight wreath row

**Date:** 2026-08-13  
**Status:** exact local set identity; the simultaneous protected-row
extension problem remains separate

## 1. Normal form

Use the notation of
`MATH_THEOREM_CLEAN_FACET_GEODESIC_PAIRED_BACKUP_AND_POLYNOMIAL_SOURCE_HALO_20260813.md`.
Thus the ground-set size is `2R-1`, `S` has rank `R-q`,
`Z=bar S`, `L_0 subset Z` has rank `R-1`,

\[
 I=Z\setminus L_0=\{i_1,\ldots,i_q\},\qquad
 D=\{d_1,\ldots,d_q\}\subset L_0,
\tag{1.1}
\]

and `C=L_0\setminus D`.  Put

\[
 m=R-1,qquad n=2m+1=2R-1.
\tag{1.2}
\]

Write

\[
 C=(c_1,\ldots,c_{m-q}),\qquad
 S=(s_1,\ldots,s_{m+1-q}),
\tag{1.3}
\]

and take the cyclic coordinate order

\[
 \pi=(d_1,\ldots,d_q,\ c_1,\ldots,c_{m-q},\
       i_1,\ldots,i_q,\ s_1,\ldots,s_{m+1-q}).
\tag{1.4}
\]

For cyclic subscripts define

\[
 L_t=I_\pi(t,m),\qquad
 A_t=I_\pi(t-1,m+1)=L_{t-1}\cup L_t.
\tag{1.5}
\]

The first identity in `(1.5)` agrees with the clean-package geodesic for
`0<=t<=q`: shifting the length-`m` window deletes `d_t` and inserts
`i_t`.

## 2. Exact antipodal identities

For every cyclic index `t`, complementation gives

\[
 \overline{L_t}=I_\pi(t+m,m+1)=A_{m+t+1},
\tag{2.1}
\]

and

\[
 \overline{A_t}=I_\pi(t+m,m)=L_{m+t}.
\tag{2.2}
\]

Consequently the clean upper-witness path is the arc

\[
 A_1-L_1-A_2-\cdots-L_{q-1}-A_q,
\tag{2.3}
\]

while its complementary intersection path is the antipodal arc

\[
 W_0-F_1-W_1-\cdots-F_q-W_q,
\tag{2.4}
\]

with the literal indices

\[
 \boxed{W_j=A_{m+j+1}},\qquad
 \boxed{F_j=L_{m+j}}.
\tag{2.5}
\]

Thus the two central paired paths already lie in one tight wreath row.

## 3. The four halos

Assume `q<=d` and `R>=3d+3`.  Use the following literal banks from the
ordered `C,S` blocks:

\[
\begin{array}{c|c|c}
&\text{deleted bank}&\text{inserted bank}\\ \hline
\text{intersection, left}&
 \{s_{m-d-q+1},\ldots,s_{m+1-q}\}&
 \{c_{m-d-q},\ldots,c_{m-q}\}\\
\text{intersection, right}&
 \{s_1,\ldots,s_{d+1}\}&
 \{c_1,\ldots,c_{d+1}\}.
\end{array}
\tag{3.1}
\]

The first line is traversed from the right endpoint of each displayed
block toward the left.  For the upper-witness halo take

\[
 J^-=\{s_{m-d-q+1},\ldots,s_{m+1-q}\},\quad
 K^-=\{c_{m-d-q+1},\ldots,c_{m-q}\},
\tag{3.2}
\]

\[
 J^+=\{s_1,\ldots,s_{d+1}\},\quad
 K^+=\{c_1,\ldots,c_d\}.
\tag{3.3}
\]

Here its first left exchange deletes the forced label `i_1`, its first
right exchange deletes the forced label `d_q`, and the remaining
deletions are `K^-` and `K^+`.  The size hypotheses in the clean-halo
theorem make the left and right banks disjoint.

With these choices, the four halo arms are literally the tight-row arcs

\[
 A_{-d},A_{-d+1},\ldots,A_1,
 \qquad
 A_q,A_{q+1},\ldots,A_{q+d+1},
\tag{3.4}
\]

and

\[
 A_{m-d},A_{m-d+1},\ldots,A_{m+1},
 \qquad
 A_{m+q+1},A_{m+q+2},\ldots,A_{m+q+d+2}.
\tag{3.5}
\]

Every exchange is just the next shift of a cyclic length-`m` window.
The coordinate words on each protected arc are therefore the monotone
words already proved in the clean-halo theorem.  Together with the two
central paths, `(3.4)--(3.5)` form the two collared owner-index blocks

\[
 [-d,q+d+1],\qquad[m-d,m+q+d+2]\pmod n.
\tag{3.6}
\]

Their starts differ by `m`, and

\[
                         m=R-1\ge3d+2.
\tag{3.7}
\]

Since `q<=d`, the cyclic gap between the two owner-index blocks in either
direction is

\[
                         m-q-2d-2\ge0.
\tag{3.8}
\]

Thus the blocks are owner-disjoint.  In the equality case their far-port
owners are consecutive in the row, but the intervening connector facet
is not part of either protected halo.  This recovers resource
disjointness directly from the row indices.

### Theorem 3.1

Every clean facet-geodesic paired package with its four compatible
length-`d+1` monotone halo arms admits a relabelling in which those four
arms are exactly the four arcs `(3.4)--(3.5)` of one tight wreath row.
Together with the two central paths they form the two disjoint collared
row blocks `(3.6)`, and their central arcs obey `(2.5)`.

#### Proof

The window shift in `(1.5)` gives, for every cyclic `r`,

\[
 A_r\longrightarrow A_{r+1}:quad
 \text{delete }\pi_{r-1},\quad\text{insert }\pi_{r+m},
\tag{3.9}
\]

and

\[
 A_r\longrightarrow A_{r-1}:quad
 \text{delete }\pi_{r+m-1},\quad\text{insert }\pi_{r-2}.
\tag{3.10}
\]

Starting at `A_1` and using `(3.10)` first deletes `i_1`, then the
rightmost `d` members of `C`, while inserting the rightmost `d+1`
members of `S`.  Starting at `A_q` and using `(3.9)` first deletes
`d_q`, then the leftmost `d` members of `C`, while inserting the leftmost
`d+1` members of `S`.  These are exactly `(3.2)--(3.4)`.

By `(2.5)`, the complementary central path begins at `A_{m+1}` and ends
at `A_{m+q+1}`.  Applying `(3.10)` at its left end deletes the rightmost
`d+1` members of `S` and inserts the rightmost `d+1` members of `C`.
Applying `(3.9)` at its right end does the same with the leftmost banks.
This is `(3.1)` and `(3.5)`.

Finally `(3.8)` proves that the two owner-index intervals do not meet.
The used facets of an owner interval `[a,b]` are
`L_a,L_{a+1},...,L_{b-1}`.  Thus those lower-resource intervals are also
disjoint; if the owner intervals are consecutive, their single joining
facet is outside both lists.  This proves the resource and arc claims.
\(\square\)

## 4. Exact extension consequence and limitation

Whenever the known exact wreath factor at this parameter is available, a
single prescribed tight row always extends: relabel one of its rows to the
prescribed cyclic order.  Therefore one isolated clean package, protected
by prescribing its whole host row, has an exact-factor extension.

This does not prove simultaneous extension of a polynomial family of
package rows.  The separate obstruction
`MATH_OBSTRUCTION_PROTECTED_TIGHT_WREATH_ROWS_NOT_HEREDITARILY_EXTENDABLE_20260813.md`
shows that even two pairwise window-disjoint prescribed rows can fail to
extend at `m=3`.  A global application must exploit special structure of
the chosen clean rows or allow protected-arc-preserving row trades; plain
pairwise resource-disjointness is insufficient.

## 5. Finite identity audit

The standard-library script

`scratch/verify_clean_package_one_wreath_row_20260813.py`

replays `(1.5)`, `(2.5)`, `(3.1)--(3.5)`, and both resource-disjointness
claims.  It passed `7,600` parameter triples on `h100`.  This replay is a
check on the displayed indices; the proof above is symbolic.
