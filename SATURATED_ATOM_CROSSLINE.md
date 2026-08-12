# Cross-line packing excludes the saturated `3/2` atom

## 1. Result

Let

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                  \ |x|,|y|,|z|\le a\}
\]

and let a word be a permutation of its
`M_a=3a^2+3a+1` points.  For every directed internal coordinate-peak
plateau `P`, let `lambda(P)` be its number of word edges and define

\[
             \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}.
\]

### Theorem 1 (saturated-atom obstruction)

No sequence of such words satisfies

\[
                         \mu_a\Longrightarrow2\delta_{3/2}.       \tag{1.1}
\]

The proof is purely geometric.  A plateau of length near `3a/2` uses most
points of one central coordinate line.  Plateaux in different coordinate
directions have quadratically many line intersections.  Almost every such
intersection must be omitted by all but one of the incident plateaux.  The
available line omissions are at most one half of the pair-intersection count,
whereas avoiding duplicate word points requires at least two thirds.

Combined with `BOUNDARY_RESERVOIR_PROFILE.md`, this eliminates the entire
one-atom continuum

\[
                     2\delta_x,qquad 4/3\le x\le3/2,
\]

under the boundary theorem's explicit vanishing-seam hypotheses when
`x<3/2`, and unconditionally at the remaining saturated endpoint.  It does
not classify non-atomic or positive-seam profiles.

## 2. Coordinate lines and regular plateaux

Fix a small constant `epsilon>0`, eventually chosen at most `1/100`.  Call a
directed peak plateau regular when

\[
             (3/2-\varepsilon)a<\lambda(P)
                  <(3/2+\varepsilon)a.              \tag{2.1}
\]

Under (1.1), if `m` is the number of regular plateaux, then

\[
                    m=(2+o(1))a,
 \qquad \sum_{P\ \mathrm{regular}}\lambda(P)=(3+o(1))a^2.       \tag{2.2}
\]

This follows from weak convergence on the compact interval `[0,2]`, first
for the mass and then for the bounded continuous first moment.  All `o(1)`
terms below are for fixed `epsilon` as `a` tends to infinity.

A coordinate line at level `t`, for example `x=t`, contains exactly

\[
                              2a-|t|+1               \tag{2.3}
\]

points of `H_a`.  Hence a regular plateau on that line satisfies

\[
                             |t|<(1/2+\varepsilon)a.              \tag{2.4}
\]

Two regular plateaux with the same fixed coordinate and level cannot both
exist: their disjoint vertex sets would contain more than `2a-|t|+1` points.
Thus regular plateaux in one coordinate direction use distinct integer
levels.

Write `n_x,n_y,n_z` for the numbers in the three directions.  Then

\[
                         n_x+n_y+n_z=m=(2+o(1))a.     \tag{2.5}
\]

## 3. The omission budget

For a regular plateau `P` at level `t`, call the points of its full coordinate
line not used by `P` its omissions.  Their number is

\[
             r(P)=(2a-|t|+1)-(\lambda(P)+1)
                  =2a-|t|-\lambda(P).               \tag{3.1}
\]

Let `R=sum_P r(P)`.  By (2.2),

\[
                         R=(1+o(1))a^2-\sum_P|t(P)|. \tag{3.2}
\]

Among `n` distinct integer levels, the minimum possible sum of absolute
values is `floor(n^2/4)`.  Applying this independently in the three
directions gives, with

\[
                         S_2=n_x^2+n_y^2+n_z^2,
\]

the upper bound

\[
                         R\le a^2-{S_2\over4}+o(a^2).             \tag{3.3}
\]

## 4. Cross-line intersections

Let `I_0` be the number of pairs of selected regular lines in different
coordinate directions:

\[
 I_0=n_xn_y+n_yn_z+n_zn_x
    ={m^2-S_2\over2}
    =2a^2-{S_2\over2}+o(a^2).                      \tag{4.1}
\]

An `x=t` line and a `y=s` line intersect in `H_a` exactly when
`|t+s|<=a`.  By (2.4), a nonintersecting positive pair must have both levels
in `((1/2-epsilon)a,(1/2+epsilon)a)`, and similarly at the negative end.
There are only `2epsilon*a+O(1)` available integer levels in each such end
interval.  Summing over signs and the three direction pairs, the number of
nonintersecting selected-line pairs is at most

\[
                         24\varepsilon^2a^2+O(a).    \tag{4.2}
\]

Let `I` be the number of pairs which really intersect.  Equations
(4.1)--(4.2) give

\[
 I\ge I_0-24\varepsilon^2a^2-O(a).                 \tag{4.3}
\]

Because every direction has at most `(1+2epsilon)a+O(1)` available regular
levels, concentrating (2.5) into as few directions as possible shows

\[
                         I\ge(1-28\varepsilon^2-o(1))a^2.         \tag{4.4}
\]

Here `4 epsilon^2` comes from concentrating the level counts and
`24 epsilon^2` from the possibly nonintersecting extreme pairs.  In
particular, `I=Omega(a^2)` for fixed sufficiently small `epsilon`.

## 5. Every intersection consumes omissions

At a point `p in H_a`, let `d_p` be the number of selected regular coordinate
lines through `p`.  Then `d_p` is zero, one, two, or three, and

\[
                         I=\sum_p {d_p\choose2}.      \tag{5.1}
\]

Let `u_p` be the number of corresponding regular plateaux which actually use
`p`.  A word point normally belongs to at most one regular plateau.  It can
belong to two only when it is the shared endpoint of two consecutive plateau
blocks: regular plateau edge sets are disjoint, and only the two word edges
adjacent to one position are available.  Consequently the number of points
with `u_p=2` is `O(m)=O(a)`, and `u_p<=1` everywhere else.

The number of omission incidences at `p` is `d_p-u_p`.  Away from the
`O(a)` shared endpoints,

\[
                 d_p-u_p\ge d_p-1
                    \ge {2\over3}{d_p\choose2}.      \tag{5.2}
\]

The final inequality is checked only at `d_p=2,3`.  Summing (5.2), and
absorbing the shared endpoints, proves

\[
                              R\ge{2\over3}I-O(a).   \tag{5.3}
\]

On the other hand, (3.3), (4.1), and (4.3) give

\[
                              R\le{1\over2}I
                                  +12\varepsilon^2a^2+o(a^2).    \tag{5.4}
\]

Combining (5.3)--(5.4),

\[
                  {1\over6}I\le12\varepsilon^2a^2+o(a^2).       \tag{5.5}
\]

But (4.4) makes the left side at least
`(1-28epsilon^2-o(1))a^2/6`.  Choosing, for example,
`epsilon=1/100` and then taking `a` sufficiently large contradicts (5.5).
This proves Theorem 1.

## 6. Scope ledger

### Proved here

* The saturated atom `2 delta_(3/2)` cannot be the directed-peak length
  profile of permutations of `H_a`.
* The obstruction uses only line capacities, cross-direction intersections,
  and the fact that the word does not repeat a middle point.

### Not used

* witness slack `D`;
* the run-spectrum inequality;
* the first-dangerous seam functional; or
* any assumed rotating/periodic order of plateau directions.

### Not proved

* exclusion of arbitrary mixtures of plateau lengths;
* a uniform quantitative stability theorem near the atom; or
* the full three-box and Boolean-lattice conjectures.
