# Upward high-hole cones and the sharpened boundary-moment theorem

## Verdict

This note gives a strict strengthening of the audited hole-spectrum / boundary-
moment inequality.  It is unconditional in the equality-length setup, but its
scalar corollary still does not contradict `n=B(k)` for any maximizing rank
through `k=19`, including `k=11`.

The new input is interval geometry: holes whose OR has rank at least the chosen
rank form an upward-closed family.  Such holes destroy at most two cover edges
each, rather than the four edges allowed by the previous degree-only bound.
Low-rank holes may destroy four, but they contribute a positive avoidance
moment.  Optimizing this tradeoff yields the theorem below.

## 1. Setup

Fix `k,r`, put

\[
 M=\binom kr,\qquad n=M+d,
\]

and choose one witness of length at most `d` for every nonempty mask of rank
below `r`.  Let `B_(n,d)` be the physical interval band of lengths at most
`d`, and let `H` be the unselected cells.  Then

\[
 |H|=\sigma=dM+\binom{d+1}{2}-\sum_{s=1}^{r-1}\binom ks.
\]

Throughout, `d>=1`, the word is zero-free, and out-of-range binomial
coefficients are zero.  The zero-free hypothesis is used only for the
`2r-3` rhombus ceiling in Section 7.

Write

\[
 H_< =\{I\in H:|U(I)|<r\},\qquad
 H_\ge=\{I\in H:|U(I)|\ge r\},
\]

and put `h=|H_<|`.  The cover graph of `B_(n,d)` is oriented from a physical
interval to a one-position extension.  Its edge count is

\[
 E=(d-1)(2n-d).
\]

## 2. High holes are an upset

### Lemma 1

`H_>=` is upward closed in the short interval band.

### Proof

If `I` is a high hole and `I subseteq J` is another short physical interval,
then `U(I) subseteq U(J)`, so `|U(J)|>=r`.  A selected cell represents a mask
of rank below `r`; therefore `J` is also a high hole.  QED.

This is a genuine cone condition, not just a statement about hole labels.

## 3. Edge-deletion tradeoff

### Lemma 2

The number of selected-selected cover edges is at least

\[
 e_{\rm sel}(h)=\max\{E-2\sigma-2h,0\}.                 \tag{1}
\]

### Proof

Every cover edge incident with `H_>=` has its upper endpoint in `H_>=`: if its
lower endpoint is high, upward closure forces its upper endpoint high.  Charge
the edge to that upper endpoint.  A physical interval has at most two immediate
subintervals, so these edges number at most `2|H_>=|`.

After those edges are removed, every remaining edge incident with a hole is
incident with a low hole.  The band cover graph has maximum degree four, so at
most `4|H_<|` further edges are removed.  Thus the total number removed is at
most

\[
 2(\sigma-h)+4h=2\sigma+2h.
\]

Subtract from `E` and truncate at zero.  QED.

The old theorem used only `E-4 sigma`.  Formula (1) interpolates exactly
between `E-2 sigma` when every hole is high and `E-4 sigma` when every hole is
low.

## 4. Low holes pay an avoidance moment

For `q>=1`, define as in the audited theorem

\[
 H_q=\sum_{I\in H}\binom{k-|U(I)|}{q}.
\]

### Lemma 3

\[
 H_q\ge h\binom{k-r+1}{q}.                              \tag{2}
\]

### Proof

Every low hole has OR rank at most `r-1`, hence avoids at least `k-r+1`
coordinates.  High-hole contributions are nonnegative.  Sum.  QED.

Every selected-selected cover edge joins two distinct lower masks.  Its
`q`-gradient is at least

\[
 b_q:=\binom{k-r+1}{q-1}.                               \tag{3}
\]

Consequently

\[
 G_q\ge e_{\rm sel}(h)b_q.                              \tag{4}
\]

## 5. Sharpened weighted theorem

Let

\[
 Z_q=\sum_i\binom{k-|A_i|}{q},\qquad
 R_q=\binom{k}{q}\sum_{s=1}^{r-1}\binom{k-q}{s},
\]

where the first binomial in `R_q` means `binom(k,q)`.

### Theorem 4

For the actual number `h` of low holes,

\[
dZ_q\ge R_q
 +h\binom{k-r+1}{q}
 +\frac d4\max\{E-2\sigma-2h,0\}
       \binom{k-r+1}{q-1}.                              \tag{5}
\]

Therefore the following entirely numerical inequality is necessary:

\[
\begin{split}
d\binom{k}{q}(n-B(q))\ge R_q+\min_{0\le h\le\sigma}\Bigg[
&h\binom{k-r+1}{q}\\
&+\frac d4\max\{E-2\sigma-2h,0\}
 \binom{k-r+1}{q-1}\Bigg].                             \tag{6}
\end{split}
\]

### Proof

The audited boundary-moment theorem gives

\[
 dZ_q\ge R_q+H_q+\frac d4G_q.
\]

Insert (2) and (4), proving (5).  Projection to a `q`-set gives
`Z_q<=binom(k,q)(n-nu(q))`; the proved lower bound `nu(q)>=B(q)` gives the
left side of (6).  Finally minimize the unknown integer `h`.  QED.

This dominates the old scalar corollary (and is strictly stronger in cases
such as `k=11`, though degenerate parameters can give equality).  At
`h=sigma` it retains the old
edge term and adds the positive low-hole moment; at `h=0` it replaces
`E-4 sigma` by `E-2 sigma`.

## 6. The exact `k=11` assessment

At the conjectured value,

```text
k=11, r=6, n=465, d=3, sigma=369, E=1854.
```

For `q=1`, (5) gives

\[
3Z_1\ge7007+6h+\frac34(1116-2h)
       =7844+\frac92h.
\]

The worst case is therefore `h=0`: making every hole high minimizes the new
right side.  Projection gives `3Z_1<=15312`, leaving slack 7468.  Thus the
new theorem is substantially stronger than the old boundary term
`(3/4)(378)`, but it does not rule out length 465.

For the exact q369 branch all 369 holes are the prescribed rank-six triples.
Hence

\[
 H_q=369\binom5q
\]

and the selected-edge lower bound is 1116.  The resulting margins remain
positive; at `q=1` the right side is

\[
7007+1845+837=9689,
\]

leaving slack 5623.  So even the exact q369 hole labels do not make the
averaged moment inequality contradictory.

## 7. Rhombus/cone isoperimetric refinement

For a rhombus with outer interval `O`, side intervals `L,R`, and inner interval
`I`, anti-Monge rank geometry gives

\[
 |U(O)|+|U(I)|\le |U(L)|+|U(R)|.                         \tag{7}
\]

If `O` is a minimal high hole and both sides are nonhigh, then

\[
 |U(O)|\le
 \begin{cases}
 2r-2,& |O|=2,\\
 2r-3,& |O|\ge3,
 \end{cases}                                             \tag{8}
\]

because array entries are nonempty, so a nonempty inner interval has rank at
least one.  This gives positive avoidance weight to minimal nonsingleton high
holes whenever the displayed upper rank is below `k`.

Singleton minima do not invalidate all further information: they have no
downward cover edges, and one minimal interval can generate only a bounded
number of cells in its upward cone.

Let `x` be the number of high singleton holes and `m` the number of minimal
nonsingleton high holes.  Put

\[
 C_1=\binom{d+1}{2},\qquad C_2=\binom d2,
 \qquad c=\max\{k-2r+2,0\}.
\]

The cone of a singleton contains at most `C_1` short intervals, while the cone
of a nonsingleton contains at most `C_2`.  Every high hole lies above a minimal
high hole, so

\[
 C_1x+C_2m\ge\sigma-h.                                  \tag{9}
\]

Moreover, charging high-incident edges to their high upper endpoints now
gives

\[
 e_{\rm sel}\ge
 \max\{E-2\sigma-2h+2x,0\},                             \tag{10}
\]

because a singleton upper endpoint has zero immediate subintervals.  Finally,
(8) gives

\[
 H_q\ge h\binom{k-r+1}{q}+m\binom cq.                   \tag{11}
\]

Consequently (6) can be sharpened by minimizing

\[
 h\binom{k-r+1}{q}+m\binom cq
 +\frac d4\max\{E-2\sigma-2h+2x,0\}
       \binom{k-r+1}{q-1}                               \tag{12}
\]

over nonnegative integers `h,x,m` satisfying

\[
 h\le\sigma,\quad x+m\le\sigma-h,\quad
 C_1x+C_2m\ge\sigma-h.                                 \tag{13}
\]

This is an unconditional location/rank coupling.  When `c=0`, it can reduce
to the first tradeoff; at the upper middle rank `c` is one in odd dimension,
while at the unique middle rank it is two in even dimension.

For `k=11,q=1`, the minimum is

```text
h=0, x=61, m=1, selected-edge lower bound=1238,
extra term=929.5.
```

Thus the refined necessary inequality is

\[
3Z_1\ge7007+929.5=7936.5,
\]

leaving projection slack 7375.5.  It remains far from a contradiction, but
it is stronger than the `7844` bound from (6).  The exact q369 rank-six hole
spectrum still gives the stronger branch-specific right side `9689`.

The remaining escape is now precise rather than qualitative: many high holes
can be organized into cones above well-separated high singleton entries.  A
further theorem must couple those singleton-cone locations to the zero-run
quantities `Z_q,Lambda_q` or to literal rank moments.

## 8. Reproducibility

`check_hole_upset_moments.cpp` evaluates (6) exactly after multiplying by
four.  `HOLE_UPSET_NUMERICAL_CHECK_K19.txt` records every maximizing rank for
`1<=k<20`; there are no violations.  The stronger cone optimization (12) is
not implemented by that checker; its stated `k=11,q=1` minimum was separately
exhaustively enumerated and independently audited.
