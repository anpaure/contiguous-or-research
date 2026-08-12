# Independent audit of the saturated-atom cross-line argument

## 1. Verdict

The saturated-atom obstruction is correct.  The current
`SATURATED_ATOM_CROSSLINE.md` correctly uses

\[
 I\ge (1-28\varepsilon^2-o(1))a^2,                 \tag{1.1}
\]

in (4.4).  The `28` is the sum of `4` from worst-case concentration of
the direction counts and `24` from the allowance for nonintersecting
fringe pairs; the latter term must not be omitted.  Combining this bound
with (5.5) gives a contradiction for every fixed
`0<epsilon<1/10`, in particular for `epsilon=1/100`.

This audit gives a proof independent of the prose of the source file.  It
also checks the two worst possible degeneracies: concentration of the
chosen levels into only two coordinate directions, and overlap of plateau
vertex sets at word seams.

## 2. Setup and the consequence of weak convergence

Let

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                  \ |x|,|y|,|z|\le a\}
\]

and let `T_1,...,T_(M_a)` be a permutation of its points.  A plateau
`P=[l,r]` has edge length `lambda(P)=r-l`.  Every coordinate line has at
most `2a+1` points, so every plateau satisfies

\[
                         0\le {\lambda(P)\over a}\le2.           \tag{2.1}
\]

Assume for contradiction that

\[
 \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}
       \Longrightarrow2\delta_{3/2}.                            \tag{2.2}
\]

Fix `0<epsilon<1/10`, and call `P` regular if

\[
 (3/2-\varepsilon)a<\lambda(P)<(3/2+\varepsilon)a.              \tag{2.3}
\]

The endpoints of the corresponding normalized interval carry no mass
under the limiting measure.  Hence weak convergence gives

\[
             m:=\#\{P:P\text{ regular}\}=(2+o(1))a.             \tag{2.4}
\]

It also gives the required first-moment statement.  One way to avoid any
discontinuous-test-function issue is to note that `x` is bounded by `2` on
the common compact support.  Thus the total first moments converge to `3`,
while the mass, and therefore the first moment, outside the regular
interval tends to zero.  Consequently

\[
             \sum_{P\text{ regular}}\lambda(P)=(3+o(1))a^2.    \tag{2.5}
\]

Thus both the regular count and its edge mass follow from (2.2); no
unbounded-moment or uniform-integrability assumption is missing.

## 3. Exact line capacity and uniqueness on a level

For fixed `x=t`, the possible values of `y` form the integer intersection

\[
 [-a,a]\cap[-t-a,-t+a].
\]

It has exactly

\[
                         2a-|t|+1                               \tag{3.1}
\]

elements.  The same formula holds in the other two directions.  A plateau
with `lambda` edges uses `lambda+1` distinct points, because the word is a
permutation.  Therefore a regular plateau on level `t` obeys

\[
 \lambda+1\le2a-|t|+1,
 \qquad |t|\le2a-\lambda<(1/2+\varepsilon)a.                    \tag{3.2}
\]

There cannot be two regular plateaux of the same coordinate and level.
Indeed, they are different maximal constant intervals of the same scalar
coordinate word, so their vertex sets are disjoint.  For large `a` their
combined number of vertices is greater than
`2(3/2-epsilon)a`, whereas the whole line has at most `2a+1` points.

Write `n_x,n_y,n_z` for the regular counts in the three directions and

\[
                         S_2=n_x^2+n_y^2+n_z^2.                  \tag{3.3}
\]

Then

\[
 n_x+n_y+n_z=(2+o(1))a,\qquad
 n_i\le(1+2\varepsilon)a+O(1).                                 \tag{3.4}
\]

The second bound follows by counting the integer levels in (3.2), using
the just-proved same-level uniqueness.

## 4. Omission budget

For a regular plateau `P` at level `t(P)`, let `r(P)` be the number of
points of its full line which it does not use.  Exactly,

\[
 r(P)=(2a-|t(P)|+1)-(\lambda(P)+1)
     =2a-|t(P)|-\lambda(P).                                    \tag{4.1}
\]

Let `R=sum_P r(P)`, over regular plateaux.  By (2.4)-(2.5),

\[
 R=2am-\sum_P\lambda(P)-\sum_P|t(P)|
  =a^2-\sum_P|t(P)|+o(a^2).                                   \tag{4.2}
\]

For `n` distinct integer levels, the least possible sum of absolute values
is obtained by taking the `n` integers nearest zero, and equals
`floor(n^2/4)`.  Applying this independently in each coordinate direction
gives

\[
 \sum_P|t(P)|\ge {S_2\over4}-O(1),
 \qquad R\le a^2-{S_2\over4}+o(a^2).                           \tag{4.3}
\]

This is valid even for a maximally adversarial, asymmetric selection of
levels; no balance among the three directions has been assumed.

## 5. Intersecting line pairs, including the worst concentration

The number of pairs of selected regular lines in different directions,
whether or not their intersection lies in the hexagon, is

\[
 I_0=n_xn_y+n_yn_z+n_zn_x
    ={(n_x+n_y+n_z)^2-S_2\over2}
    =2a^2-{S_2\over2}+o(a^2).                                  \tag{5.1}
\]

An `x=t` line and a `y=s` line meet at `(t,s,-t-s)`, and this point is in
`H_a` exactly when `|t+s|<=a`; (3.2) already ensures the other two
coordinate bounds.  Put `B=(1/2+epsilon)a`.  If `|t|,|s|<B` but
`t+s>a`, then necessarily

\[
              (1/2-\varepsilon)a<t,s
                         <(1/2+\varepsilon)a.                   \tag{5.2}
\]

Indeed, if (say) `t<=(1/2-epsilon)a`, then `t+s<a`.  The case
`t+s<-a` is the reflected negative fringe.  Each fringe contains at most
`2 epsilon a+O(1)` integer levels.  Thus one unordered pair of coordinate
directions has at most

\[
 2(2\varepsilon a+O(1))^2
       =8\varepsilon^2a^2+O(a)                                 \tag{5.3}
\]

nonintersecting selected pairs.  Summing over `xy,yz,zx`, if `N` denotes
the total number of nonintersecting pairs,

\[
 N\le24\varepsilon^2a^2+O(a).                                 \tag{5.4}
\]

Let `I=I_0-N` be the number of genuinely intersecting selected-line pairs.
Then

\[
 I\ge2a^2-{S_2\over2}-24\varepsilon^2a^2+o(a^2).               \tag{5.5}
\]

For completeness, consider the level-count distribution that minimizes
`I_0`.  Under (3.4), the convex function `S_2` is maximized by filling one
direction to its cap, putting the remainder in a second direction, and
using no levels in the third.  Up to `o(a)`, this is the explicit
adversarial distribution

\[
 (n_x,n_y,n_z)=((1+2\varepsilon)a,
                (1-2\varepsilon)a,0).                           \tag{5.6}
\]

It yields

\[
 S_2\le\big((1+2\varepsilon)^2+(1-2\varepsilon)^2\big)a^2
          +o(a^2)
      =(2+8\varepsilon^2)a^2+o(a^2),                            \tag{5.7}
\]

and hence `I_0>=(1-4 epsilon^2)a^2-o(a^2)`.  After the independent
worst-case fringe deduction (5.4), the valid conclusion is

\[
                   I\ge(1-28\varepsilon^2)a^2-o(a^2).           \tag{5.8}
\]

Allowing both (5.6) and the maximum fringe loss simultaneously only makes
this lower bound more conservative, so it covers any correlation between
count concentration and end-fringe placement.

## 6. Seam overlaps and the local omission charge

The edge sets of distinct coordinate plateaux are pairwise disjoint.  For
plateaux of the same coordinate this follows from maximality of constant
blocks.  If an edge of the permutation belonged to plateaux in two
different coordinates, its two endpoint points would agree in those two
coordinates; the equation `x+y+z=0` would force agreement in the third,
contradicting that the permutation points are distinct.

Every regular plateau has positive length.  Hence, if a word position lies
in its vertex interval, at least one of the at most two word edges incident
to that position belongs to the plateau.  Edge disjointness therefore
implies that a word position can lie in at most two regular plateau vertex
sets.  If it lies in two, each plateau uses one of the two incident edges,
so the position is a common endpoint of consecutive plateau edge blocks.
It cannot be an interior point of either plateau.  Since the `m` plateaux
have only `2m` endpoint incidences, the number of such shared positions is
at most `m=O(a)` (and the sharper `m-1` bound is also immediate from the
linear edge order).  In particular, triple plateau membership at a seam is
impossible.

Now fix a geometric point `p in H_a`.  Let `d_p` be the number of selected
regular coordinate lines through it and `u_p` the number of their plateaux
which use it.  There is at most one selected line through `p` in each
coordinate direction, so `0<=d_p<=3`.  Every intersecting pair of selected
lines has a unique intersection point, including when three pairs coincide
at a triple point.  Therefore

\[
                         I=\sum_{p\in H_a}{d_p\choose2}.         \tag{6.1}
\]

The number of omission incidences at `p` is exactly `d_p-u_p`; summing over
`p` gives `R`.  Away from the `O(a)` shared endpoints, `u_p<=1`, and direct
checking for `d_p=0,1,2,3` gives

\[
 d_p-u_p\ge d_p-1
       \ge {2\over3}{d_p\choose2}.                              \tag{6.2}
\]

Here the only nonzero cases are `d_p=2`, where `1>=2/3`, and `d_p=3`,
where equality `2=2` holds.  At a shared endpoint `u_p=2`; relative to
(6.2), the loss is at most `1` even if `d_p=3`.  Thus all seam overlaps
together cost only `O(a)`, and

\[
                         R\ge {2\over3}I-O(a).                   \tag{6.3}
\]

This proves the local charge without assuming a rotating order, literal
adjacency of all regular plateaux, or disjointness of their vertex sets.
Only their edge sets must be disjoint; the possible shared endpoints have
been charged explicitly.

## 7. Final comparison and constants

Equations (4.3) and (5.1) give

\[
 R\le {1\over2}I_0+o(a^2).
\]

Since `I_0=I+N`, (5.4) implies

\[
 R\le {1\over2}I+12\varepsilon^2a^2+o(a^2).                    \tag{7.1}
\]

This is exactly source equation (5.4): the factor `12` is one half of the
`24` in the nonintersection allowance, and its `O(a)` remainder is absorbed
by `o(a^2)`.

Comparing (6.3) and (7.1), and absorbing `O(a)` into `o(a^2)`, yields

\[
                         {1\over6}I
             \le12\varepsilon^2a^2+o(a^2).                     \tag{7.2}
\]

But the corrected lower bound (5.8) makes the left side at least

\[
 {1-28\varepsilon^2\over6}a^2-o(a^2).                          \tag{7.3}
\]

The simultaneous asymptotic inequalities (7.2)-(7.3) would require

\[
 {1-28\varepsilon^2\over6}\le12\varepsilon^2,
 \quad\text{equivalently}\quad 1\le100\varepsilon^2.          \tag{7.4}
\]

This is false for the fixed choice `epsilon=1/100` (indeed for every
`epsilon<1/10`).  The assumed weak convergence is therefore impossible.

## 8. Audit ledger

* Weak convergence controls both the regular count and regular first
  moment because all normalized plateau lengths lie in `[0,2]`.
* The hexagon line size is exactly `2a-|t|+1`.
* Same-coordinate, same-level regular plateaux are excluded by disjointness
  of scalar maximal blocks and line capacity.
* The omission formula has no lost endpoint term: the two `+1` terms cancel
  exactly.
* The nonintersection loss is at most `24 epsilon^2 a^2+O(a)`.
* The worst count concentration is the two-direction distribution (5.6).
* A permutation position belongs to at most two positive-length plateau
  intervals; all double memberships are shared endpoints and number
  `O(a)`.
* Triple line intersections are counted correctly through
  `binom(d_p,2)` and require exactly the factor `2/3` in the lower omission
  charge.
* The current source coefficient `1-28 epsilon^2` in (4.4) is correct.
* The current source (5.4) is also correct: `R<=I_0/2+o(a^2)` and
  `I_0<=I+24 epsilon^2 a^2+O(a)` give its coefficient `12`.
* The final comparison remains valid with these constants.
