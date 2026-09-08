# Audit of the cross-diagonal central-line proposal

## Verdict

**PASS as an exact zero-repeat partial upper word; FAIL as a reduction to a
genuinely three-provider residual.**

The displayed cross-diagonal line represents every advertised target, and
the lines bijectively partition the chamber `z_2+z_3<=m`.  This is a useful
global sharing identity: the `x<=c` triangular portals disappear completely
inside one coordinate orientation.

It does not prove a coefficient-one construction.  The permuted line
families require incompatible physical orders, the word contains only
central entries and hence no lower targets, and the targets missed by every
coordinate-pair line can still be joins of two arbitrary central providers.

## 1. Exact segment theorem

Let

\[
 G_{a,x}(s)=(a+s,m-a-x,x,m-s)
\]

and suppose `x<=c`, `a=c-x`.  For

\[
 0\le u<r\le m-c,\qquad 0\le x<r,
\]

the segment `s=u,...,r+x` is legal because

\[
 r+x\le m-c+x=m-a.
\]

Its maximum is

\[
 (a+r+x,m-a-x,x,m-u)
   =(c+r,m-c,x,m-u)=Y(c;u,r,x).
\]

Every entry has coordinate sum `2m`.  Thus this is an actual max word in the
four-chain product, not an abstract interval labeling.  Exhaustive integer
checks pass through `m=12`.

## 2. Chamber partition and counts

The map `(a,x,s)->G_(a,x)(s)` with

\[
 a,x\ge0,\quad a+x\le m,\quad0\le s\le m-a
\]

is a bijection onto

\[
 C_{23}=\{z\in[0,m]^4:|z|=2m,\ z_2+z_3\le m\}.
\]

The inverse is

\[
 a=m-z_2-z_3,\qquad x=z_3,\qquad s=z_1-a=m-z_4.
\]

Therefore

\[
 |C_{23}|=\sum_{j=0}^{m}(j+1)^2
 =\frac{(m+1)(m+2)(2m+3)}6.
\]

There are only `C(m+2,2)` lines.  Concatenating them adds no repeated entry;
every selected witness remains internal to its own line.  The number of
advertised oriented targets represented is

\[
 \sum_{c=0}^{m}\sum_{r=1}^{m-c}r\min\{r,c+1\}.
\]

Here `r` counts `u=0,...,r-1`, while the admissible heights are
`x=0,...,min(c,r-1)`.  The earlier `sum r^2` expression incorrectly omitted
the advertised condition `x<=c`.

These two counts refer respectively to letters and targets and must not be
identified.

## 3. Exact general pair-line criterion

For fixed coordinates two and three, the complete central line is

\[
 (t,m-c,x,m+c-x-t).
\]

To represent `Y(c;u,r,x)`, its forced segment is

\[
 t=c+u-x,\ldots,c+r.
\]

It lies in the cube precisely when

\[
 x\le c+u,\qquad r+x\le m.
\]

If

\[
 d=|Y|-2m=r+x-u
\]

is the excess above the central rank, these conditions are

\[
 Y_1\ge d,\qquad Y_4\ge d.
\]

For an arbitrary coordinate pair `{i,j}`, a two-coordinate central line
exists exactly when `Y_i,Y_j>=d`.  Consequently all six pair directions miss
exactly the targets with at most one coordinate at least `d`.

This is an algebraic classification only.  The six directions are six
different line foliations of the middle layer, not one physical word.

## 4. No-pair-line does not mean three-provider

At `m=2`, take

\[
 Y=Y(0;0,2,1)=(2,2,1,2),\qquad d=3.
\]

Every coordinate is below three, so no coordinate-pair line can represent
`Y`.  Nevertheless

\[
 (0,1,1,2)\vee(2,2,0,0)=(2,2,1,2),
\]

and both providers have central sum four.

In fact every upper point `Y` in `[0,m]^4` is the join of two central points.
Write `|Y|=2m+d`.  Choose the two largest coordinates as one block `A` and
the other two as `B`.  Then

\[
 d\le Y(A)\le2m,\qquad Y(B)=2m+d-Y(A)\ge d.
\]

Subtract a total of `d` units from coordinates in `A` to obtain one central
point, and subtract `d` units from `B` to obtain another.  The deficit
supports are disjoint, so their join is `Y`.  This is the established hull
lemma from `FOUR_BOX_INTERLEAVING_AUDIT.md`.

Thus the residual line-hard family is still a two-provider family; only its
providers cannot be constrained to one coordinate-pair line.

## 5. Remaining gates

The theorem leaves all of the following open:

* simultaneous near-once ordering of several line foliations;
* coverage of lower ranks by the same physical word;
* a derivative/factor bridge and global pin survival;
* a uniform unequal-box construction; and
* a subcubic four-box error.

Accordingly the cross-diagonal chamber should be retained as a valid partial
module, but no unconditional asymptotic constant changes.
