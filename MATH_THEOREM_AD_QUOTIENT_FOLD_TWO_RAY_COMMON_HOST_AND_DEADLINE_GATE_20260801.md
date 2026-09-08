# Quotient-fold two-ray residue has one common host, but no internal flat split

Date: 2026-08-01  
Lane: AD, quotient-fold octagon exterior compiler  
Status: exact local host/deadline theorem for every `d>=2`.  It proves a
cost-one variable-deadline realization and a universal obstruction to using
the same host as one internal flat depth-`d` source split.  Ambient planting,
owner occurrence Hall and regenerative contraction remain hypotheses.

## 0. Result

Suppress a fixed core `K` and put

\[
 F[i,j]=\{f_i,f_{i+1},\ldots,f_j\}.
\]

The quotient-fold source residue consists of the two directed rays

\[
 \{z,a_3\}\cup F[1,j]\quad(1\le j\le d-1),            \tag{0.1}
\]

and

\[
 \{z,a_1\}\cup F[j,d]\quad(2\le j\le d),              \tag{0.2}
\]

with `a_1,a_3` exchanged in the opposite phase.  Both rays have one exact
reversible binary host:

\[
 X=\{z,a_1,a_3\},\qquad
 (Z^0,T^0)=(\{z,a_3\},\{z,a_1\}),\qquad
 (Z^1,T^1)=(T^0,Z^0).                                  \tag{0.3}
\]

The literal ray cells have width at most `d`, and replacing `X` by
`Z^epsilon,T^epsilon` preserves every old interval OR by full-block lift.
Thus the residue has an exact cost-one realization with one phase-common
cap `X`.

There is nevertheless no internal **flat** realization obtained by splitting
one letter of a depth-`d` rank-`r` Johnson source.  Every such split forces
`d` decomposition-independent windows of rank at most `r-1`.  The old owner
occurrences crossing the host survive as width-`d+2` full-block lifts, not
as width-`d+1` cells.  Hence the one-host construction is exact for a
one-jump nonflat compiler and impossible in the unmodified flat derivative.

Finally, cutting two owner cycles to the same endpoint is not enough to
splice their maximal erosions.  A common endpoint gives only one guaranteed
common source letter.  A flat depth-`d` splice needs a common source halo of
at least `d` letters on each used side (or a fresh globally recomputed
erosion).  This is the precise extra boundary hypothesis still missing from
the quotient-fold statement.

## 1. Literal two-sided ray word

Consider the local source segment

\[
 f_{d-1},f_{d-2},\ldots,f_1,\quad Z^\epsilon,T^\epsilon,
 \quad f_d,f_{d-1},\ldots,f_2.                          \tag{1.1}
\]

Singleton notation is used in (1.1).  A fixed core may be adjoined to every
letter without changing any identity.

### Theorem 1.1 (exact two-ray carving)

For every `1<=j<=d-1`, the interval beginning at the left occurrence of
`f_j` and ending at `Z^epsilon` has value

\[
                    Z^\epsilon\cup F[1,j].             \tag{1.2}
\]

For every `2<=j<=d`, the interval beginning at `T^epsilon` and ending at
the right occurrence of `f_j` has value

\[
                    T^\epsilon\cup F[j,d].             \tag{1.3}
\]

The witnesses in (1.2)--(1.3) have lengths respectively `j+1` and
`d-j+2`, hence at most `d`.  Equations (0.3), (1.2) and (1.3) give exactly
(0.1)--(0.2) in phase zero and exchange `a_1,a_3` in phase one.

#### Proof

The left rail is written in decreasing filler order, so its suffix starting
at `f_j` is precisely `F[1,j]`.  The right rail is also decreasing, so its
prefix ending at `f_j` is precisely `F[j,d]`.  Adjoining the appropriate
host half proves (1.2)--(1.3) and the length formulas. \(\square\)

### Corollary 1.2 (one common cap and exact contraction)

Both orientations have block union

\[
                         Z^\epsilon\cup T^\epsilon=X.  \tag{1.4}
\]

Contracting the two consecutive halves to `X` maps every old interval to an
equal-OR interval injectively.  Conversely, reversing the two halves changes
the ray phase without changing the host union.  The positionwise cap `X` is
therefore exact, not merely a containing ambient set.

This is an OR statement.  Ray-only cells disappear on contraction, so a
regenerative use still needs their protected assignments to have native or
common alternatives, equivalently the appropriate simultaneous contraction
Hall condition.

## 2. The flat owner obstruction

Let

\[
 Q=(Q_0,\ldots,Q_{N-1}),\qquad
 O_i=\bigcup_{q=i}^{i+d}Q_q
\]

be a source whose displayed owners form a rank-`r` Johnson path.  Split an
internal source letter

\[
                         Q_p=Z\cup T,qquad Z,T\ne\varnothing. \tag{2.1}
\]

For `1<=s<=d`, the new width-`d+1` window with start `p-d+s` is

\[
 C_s=\bigcup_{q=p-d+s}^{p+s-1}Q_q.                     \tag{2.2}
\]

It contains both split halves, hence (2.2) is independent of their order or
overlap.  If `a=p-d+s`, then

\[
 C_s\subseteq O_{a-1}\cap O_a.                         \tag{2.3}
\]

Adjacent distinct rank-`r` Johnson owners have intersection rank `r-1`, so

\[
                             |C_s|\le r-1.              \tag{2.4}
\]

### Theorem 2.1 (no internal flat two-ray host)

No decomposition (2.1), including the common host (0.3), leaves the natural
depth-`d` dilation on rank `r`.  It creates `d` forced deficient rows.
Therefore the quotient-fold two-ray host cannot be inserted as one current
internal source split in a flat rank-`r` chronology.

On the other hand, an old owner interval containing `Q_p` has an injective
full-block lift containing both `Z,T`.  Its width rises exactly from `d+1`
to `d+2`; all other old intervals retain their widths.  Consequently:

* every old owner value and its order are preserved;
* the selected owner residence trace is literally unchanged;
* the new ray cells have width at most `d`; and
* precisely the inherited crossing bank needs the one-unit deadline jump.

This proves an exact nonflat escape and an exact flat obstruction.

## 3. Same endpoints versus a source halo

For an owner word `O=(O_0,...,O_(L-1))`, its maximal depth-`d` erosion is

\[
 E_p(O)=\bigcap_{i=\max(0,p-d)}^{\min(L-1,p)}O_i,
                     \qquad0\le p<L+d.                 \tag{3.1}
\]

If two owner words agree in their first `h` rows, their maximal erosions
agree in their first `h` source positions; the reversed assertion holds at
the right boundary.  Thus agreement of the first/last `d` owner rows is a
simple sufficient condition for the source halos needed by a flat
depth-`d` exterior splice.

Agreement of endpoints alone gives only `E_0=E'_0` and
`E_(L+d-1)=E'_(L+d-1)`.  It gives no second source letter.  The smallest
example is at rank two and depth one:

\[
 (12,13,34),\qquad(12,24,34).                           \tag{3.2}
\]

Their maximal erosions are

\[
 (12,1,3,34),\qquad(12,2,4,34),                        \tag{3.3}
\]

so only the outermost letters agree.

### Corollary 3.1 (exact quotient-fold scope)

An upper-complete quotient-fold cycle pair with common cut endpoints does
not yet provide a flat source replacement.  It becomes flat if one further
proves either:

1. common first/last source halos long enough for every crossing
   width-`d+1` window; or
2. that the globally recomputed maximal erosion is nonempty, dilates exactly
   to the chosen owner chronology, has equal phase lengths and satisfies the
   prescribed common caps.

Without one of these clauses, the proved construction is the cost-one
nonflat host of Sections 1--2, not a flat `D^d` packet.

## 4. Scope and replay

The light replay

```text
python3 scratch/audit_ad_quotient_fold_two_ray_deadline_gate_20260801.py --write
```

checks (1.2)--(1.4) for `2<=d<=64`, literal old-interval contraction on
finite symbolic contexts, the width gap `d` versus `d+2`, and the endpoint
counterexample (3.2)--(3.3).  The all-`d` flat obstruction is the symbolic
containment (2.3), not a finite-search conclusion.

