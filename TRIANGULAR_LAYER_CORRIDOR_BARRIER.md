# Cross-layer sharing is necessary in a subquadratic triangular braid

Let

\[
 \mathcal T_R=\{(0,0)\}\cup
 \{(s,y):1\le s\le R,\ 0\le y<s\},
\]

and require every rectangle

\[
 [u,r]\times[0,x],\qquad0\le u<r\le R,\quad0\le x<r,
\]

as the bounding box of a contiguous subword.

## 1. Defect-layer corridor obstruction

For

\[
 2\le s\le R,\qquad1\le d\le s-1,
\]

consider the adjacent-row target

\[
 T_{d,s}=[s-1,s]\times[0,s-d].
\]

Any witnessing interval contains a point of height zero.  Since its first
coordinate is constrained to `{s-1,s}`, it contains `P_(s-1)` or `P_s`.

Suppose targets of distinct defect values `d` are handled in disjoint
physical corridors.  For one fixed `d`, the peak labels occurring in its
corridor meet every edge

\[
 (d,d+1),(d+1,d+2),\ldots,(R-1,R)
\]

of the path on labels `d,...,R`.  They are therefore a vertex cover and
number at least

\[
 \left\lceil{R-d\over2}\right\rceil.
\]

Summing over the disjoint corridors gives

\[
 P\ge\sum_{d=1}^{R-1}\left\lceil{R-d\over2}\right\rceil
   =\left\lceil{R^2-1\over4}\right\rceil,
\]

where `P` is the number of peak occurrences.  Since the alphabet itself has
only `R+1` distinct peaks, the repetition excess satisfies

\[
 q\ge\left\lceil{R^2-1\over4}\right\rceil-(R+1)
   =\Omega(R^2).
\]

Thus fixed-defect concatenation, including a separate corridor for every
height layer, cannot give subquadratic excess.

## 2. Bounded cross-layer congestion is also impossible

More generally, suppose one physical peak occurrence is used for at most
`C` defect values on each of its two incident adjacent-row pairs.  It can
then serve at most `2C` of the `R(R-1)/2` targets `T_(d,s)`.  Hence

\[
 P\ge {R(R-1)\over4C}.
\]

In particular, an `O(R log R)`-excess construction must contain portals
which simultaneously serve

\[
 \Omega(R/\log R)
\]

different defect layers.  A successful braid must put row span and height
into the two independent chains of the same portal grid; bounded-congestion
layer stitching cannot work.

This theorem is architectural.  It does not exclude an unrestricted
subquadratic triangular word; the existing portal-grid normal form is
specifically capable of the required unbounded sharing.

