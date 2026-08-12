# Four-box interleaving: exact depth ledger and a radius-transfer fan

## 1. Outcome

Let

\[
 P_m=[0,m]^4,
 \qquad
 M_m=[z^{2m}](1+z+\cdots+z^m)^4
     ={2m^3+6m^2+7m+3\over3}.
\]

This note gives three rigorous advances beyond the adjacent-shadow theorem.

1. The block-internal defect at one specified depth `d` has an exact formula.
   For fixed `d` it is `d m^2+O_d(m)` on either side, and through fixed
   depth `D` it is

   \[
      {D(D+1)\over2}m^2+O_D(m)
   \]

   on either side.  Thus the old `Theta(m^4)` total is an accumulation over
   linearly many depths, not a defect already present at bounded depth.

2. Every off-middle four-box point is the join, or respectively the meet, of
   two middle points.  Combining this with the exact ledger gives, for every
   fixed `D`, a middle-layer shadow walk of length

   \[
       M_m+2D(D+1)m^2+O_D(m)
   \]

   whose joins and meets cover all ranks at distance at most `D` from the
   middle.  This is a genuine multi-depth surface theorem.

3. There is an explicit **all-depth radius-transfer fan**.  A fan of only
   `4r-1` middle occurrences covers the `2r^2` upper and lower tail points
   attached to one radius-`r` anchor.  Appending all fans to the original
   diagonal blocks gives a completely explicit all-depth two-sided shadow
   walk of length

   \[
       \boxed{2m^3+5m^2+4m+1}.                         \tag{1.1}
   \]

   Hence variable endpoints compress the `Theta(m^4)` tail defect to
   `Theta(m^3)` occurrences.  This does not yet attain `M_m+O(m^2)`; its
   leading length is three times the width.

There is also a sharp order-of-magnitude obstruction to uniformly short
seam repairs: in any near-width repair, a positive fraction of the residual
tails must use cross-rectangle windows of length `Omega(m)`.  This rules out
literal adjacent-pair or bounded-physical-window gadgets.  It does not rule
out a bounded extension around a block that is itself `Theta(m)` long, nor
using the two-point identities as endpoints of shared long windows.

All statements here concern **middle-layer meet/join shadows**.  They do not
give a factor word for `g_4`.  Section 7 records this distinction precisely.

## 2. Centered hook coordinates

It is useful to rewrite the square hooks without their minimum-rank offset.
For `0<=H<=m` and `-H<=p<=H`, put

\[
 \gamma_H(p)
  =\bigl(H+\min(p,0),\ m-H+\max(p,0)\bigr).             \tag{2.1}
\]

Then

\[
                       |\gamma_H(p)|=m+p,               \tag{2.2}
\]

and `p -> gamma_H(p)` is exactly the hook chain `C_(m-H)` from
`FOUR_BOX_CENTRAL_DIAGONALS.md`.  Every point `(x,y)` of `[0,m]^2` has the
unique representation

\[
 H=\max(x,m-y),\qquad p=x+y-m,qquad (x,y)=\gamma_H(p). \tag{2.3}
\]

Consequently every point of `P_m` is uniquely

\[
               X(H,p;K,q)=(\gamma_H(p),\gamma_K(q)),     \tag{2.4}
\]

and its rank is `2m+p+q`.

The middle diagonal in the chain rectangle `(H,K)` is

\[
 T_{H,K}(s)=(\gamma_H(s),\gamma_K(-s)),
       \qquad -\min(H,K)\le s\le\min(H,K).              \tag{2.5}
\]

Assume `H>K`.  The internal intervals of (2.5) cover exactly the points
`X(H,p;K,q)` with `|p|<=K`.  The residual tails are therefore

\[
 \begin{array}{ll}
 p>K,  &\text{an upper point, since }p+q>0,\\
 p<-K, &\text{a lower point, since }p+q<0.
 \end{array}                                             \tag{2.6}
\]

For `K>H` the same statement holds after transposing the two coordinate
pairs.  This is the centered-coordinate form of the tails calculated in the
previous note.

## 3. Exact defect at every depth

Let `D_(m,d)` denote the number of **upper** points of rank `2m+d` missed by
all block-internal diagonal intervals.  By symmetry this is also the number
of lower points of rank `2m-d` missed internally.

### Theorem 1 (exact depth ledger)

For `1<=d<=2m-1`, set

\[
 A=\min(d,m,2m-d),\qquad
 n_a=m+1-\left\lceil{d+a\over2}\right\rceil .           \tag{3.1}
\]

Then

\[
 \boxed{
 D_{m,d}=\sum_{a=1}^{A}n_a(n_a+1).
 }                                                        \tag{3.2}
\]

In particular, for fixed `d`,

\[
                         D_{m,d}=d m^2+O_d(m),             \tag{3.3}
\]

and, for fixed `D`,

\[
 \sum_{d=1}^{D}D_{m,d}
       ={D(D+1)\over2}m^2+O_D(m).                         \tag{3.4}
\]

### Proof

Consider first `H>K`, and write

\[
                 \delta=H-K.
\]

In the uncentered local coordinates used for the old diagonal calculation,
the upper tail is

\[
   (H+K+a,b),\qquad 1\le a\le\delta,\quad0\le b\le2K.   \tag{3.5}
\]

Its depth above the middle is exactly

\[
                              d=a+b.                      \tag{3.6}
\]

Fix `a`, so `b=d-a`.  The condition `b<=2K` says

\[
                      K\ge K_0:=\left\lceil{d-a\over2}\right\rceil.
\]

For this `K`, the possible imbalances are

\[
                      a\le\delta\le m-K,
\]

so there are `m-K-a+1` rectangles.  Hence the contribution with the first
pair longer is

\[
 \sum_a\sum_{K=K_0}^{m-a}(m-K-a+1).                     \tag{3.7}
\]

Put

\[
 n=m-a-K_0+1
   =m+1-\left\lceil{d+a\over2}\right\rceil.             \tag{3.8}
\]

The inner sum in (3.7) is `n(n+1)/2`.  Transposing the two coordinate pairs
gives the identical contribution from `K>H`, which cancels the factor `1/2`.
The summand exists precisely when

\[
 1\le a\le d,\qquad a\le m,qquad d+a\le2m,
\]

giving the upper limit `A` in (3.1) and proving (3.2).

Within the same imbalanced rectangle, a lower-tail point has depth
`2K+a-b`; the involution `b -> 2K-b` changes this to `a+b`.  Hence the
lower and upper depth ledgers agree exactly, without requiring the hook
decomposition itself to be complement-invariant.

For fixed `d`, one has `A=d` and every `n_a=m+O_d(1)`, proving (3.3).
Summing (3.3) for `1<=d<=D` proves (3.4).  QED.

The formula also recovers the complete one-sided defect:

\[
 \begin{split}
 \sum_{d\ge1}D_{m,d}
  &=2\sum_{H=1}^m\sum_{K=0}^{H-1}(H-K)(2K+1)\\
  &=\boxed{{m(m+1)^2(m+2)\over6}}.                       \tag{3.9}
 \end{split}
\]

For growing `D<=m/2`, (3.2) also gives

\[
        \sum_{d=1}^{D}D_{m,d}=\Theta(m^2D^2).            \tag{3.10}
\]

Thus bounded depth is genuinely a surface problem, but letting the depth
grow linearly necessarily recreates the volume-sized ledger.

## 4. A bounded-depth surface repair

Call a sequence of middle-rank points a **two-sided shadow walk** through
depth `D` if every point of ranks `2m,...,2m+D` is the coordinatewise maximum
of a contiguous interval and every point of ranks `2m-D,...,2m` is the
coordinatewise minimum of a contiguous interval.

The following elementary fact is special to having two coordinate pairs.

### Lemma 2 (two-middle-point hull)

If `X in P_m` has rank `2m+d`, then there are middle points `U,V<=X` with

\[
                              U\vee V=X.                   \tag{4.1}
\]

If `X` has rank `2m-d`, then there are middle points `U,V>=X` with

\[
                              U\wedge V=X.                 \tag{4.2}
\]

### Proof

Write `X=(x_1,x_2,x_3,x_4)`.  In the upper case,

\[
 x_1+x_2\ge d,qquad x_3+x_4\ge d,                        \tag{4.3}
\]

because the complementary pair has sum at most `2m` and the total is
`2m+d`.  Remove exactly `d` units from the first pair to obtain `U`, and
remove exactly `d` units from the last pair to obtain `V`.  Both have rank
`2m`; the two decrement supports are disjoint, so their coordinatewise
maximum is `X`.

In the lower case the total unused capacity is `2m+d`.  Each coordinate
pair has unused capacity at least `d`, since the other pair has capacity at
most `2m`.  Add `d` units in the first pair to obtain `U` and in the last
pair to obtain `V`.  Their coordinatewise minimum is `X`.  QED.

### Theorem 3 (fixed-band shadow theorem)

For every `D<=2m-1`, there is a two-sided shadow walk through depth `D` of
length at most

\[
              M_m+4\sum_{d=1}^{D}D_{m,d}.                 \tag{4.4}
\]

In particular, for every fixed `D` its length is

\[
              \boxed{M_m+2D(D+1)m^2+O_D(m)}.              \tag{4.5}
\]

### Proof

Start with any concatenation of all central diagonal paths (2.5), using
each middle point once.  Its internal intervals cover everything in the
central square of each chain rectangle.  For every internally missed upper
point through depth `D`, append the two middle points supplied by (4.1).
For every internally missed lower point, append the pair supplied by (4.2).
Each appended pair is itself a contiguous witnessing interval.  There are
`sum_(d<=D)D_(m,d)` points on each side, so the added length is at most four
times this number.  Equation (4.5) follows from (3.4).  QED.

This construction is deliberately wasteful: it does not credit any target
already repaired by a seam.  Its value is that it proves, without a matching
or factorability assumption, that every fixed band has the correct
`M_m+O_D(m^2)` shadow scale.

## 5. Radius transfer and quadratic fan compression

Lemma 2 can be made compatible with the hook rectangles.  The resulting
identity exposes exactly which rectangles must be braided.

### Lemma 4 (radius-transfer identity)

Assume `H>K`, let `p` satisfy `|p|=r>K`, and let `|q|<=K`.  Put

\[
 R=H-r+|q|,
\]

and define the two middle points

\[
 \begin{split}
 P&=(\gamma_R(-q),\gamma_K(q)),\\
 Q&=(\gamma_H(p),\gamma_r(-p)).                           \tag{5.1}
 \end{split}
\]

If `p=r`, then

\[
                 P,Q\le X(H,r;K,q),\qquad P\vee Q=X(H,r;K,q).
                                                                  \tag{5.2}
\]

If `p=-r`, then

\[
                 P,Q\ge X(H,-r;K,q),\qquad P\wedge Q=X(H,-r;K,q).
                                                                  \tag{5.3}
\]

### Proof

Both points in (5.1) are middle points because their two centered deviations
sum to zero.  Also `|q|<=R<=H`: the first inequality follows from
`R=H-r+|q|` and `r<=H`, and the second from `|q|<r`.  Thus
`gamma_R(-q)` is well-defined.

For `p=r`, the second component of `P` is the target's second component,
whereas the first component of `Q` is the target's first component.  The
other component of `Q` is

\[
                       \gamma_r(-r)=(0,m-r)\le\gamma_K(q).
\]

Using (2.1), separately for `q>=0` and `q<=0`, gives

\[
                       \gamma_R(-q)\le\gamma_H(r).
\]

Thus their join is the target.  The same calculation reverses both
inequalities for `p=-r`; now

\[
                       \gamma_r(r)=(r,m)\ge\gamma_K(q),
\]

and their meet is the target.  QED.

The point `Q` is an endpoint of rectangle `(H,r)`, while `P` lies on the
middle diagonal of rectangle `(H-r+|q|,K)`.  Thus (5.1) is a literal transfer
of the residual radius from the imbalanced rectangle into two different
central rectangles.

Using every pair (5.1) separately would still cost `Theta(m^4)`.  Variable
left and right endpoints compress an entire fibre at once.

### Lemma 5 (the two-arm fan)

Fix `1<=r<=H<=m`.  The following upper fan has `2r` middle occurrences:

\[
 \begin{array}{ll}
 U_x=(\gamma_H(r-x),(x,m-r)),&x=r-1,r-2,\ldots,0,\\[2mm]
 V_t=(\gamma_H(r-t),(0,m-r+t)),&t=1,2,\ldots,r.
 \end{array}                                               \tag{5.4}
\]

For every `0<=x<=r-1` and `1<=t<=r`, the interval from `U_x` through `V_t`
has maximum

\[
                    (\gamma_H(r),(x,m-r+t)).               \tag{5.5}
\]

The following lower fan also has `2r` occurrences:

\[
 \begin{array}{ll}
 A_x=(\gamma_H(-x),(x,m)),&x=0,1,\ldots,r,\\[2mm]
 B_t=(\gamma_H(-t),(r,m-r+t)),&t=r-1,r-2,\ldots,1.
 \end{array}                                               \tag{5.6}
\]

The interval from `A_x` through `A_r` and, when `t<r`, through `B_t`, has
minimum

\[
                    (\gamma_H(-r),(x,m-r+t)).              \tag{5.7}
\]

The last point of (5.4) equals the first point of (5.6), so the two fans can
be concatenated with one shared occurrence, in total length `4r-1`.

### Proof

Every displayed point is middle-ranked: the rank deviations of its two
coordinate-pair components are opposites.

In the interval in (5.5), the first-pair maximum is attained at `U_0` and is
`gamma_H(r)`.  Along the horizontal arm the second-pair maximum has first
coordinate `x`; along the vertical arm it has second coordinate `m-r+t`.
All intervening coordinates are no larger.  This proves (5.5).

For (5.7), `A_r` supplies the first-pair minimum `gamma_H(-r)`.  The first
arm supplies second-pair first coordinate `x`, and the second arm supplies
second coordinate `m-r+t`; all intervening coordinates are no smaller.
This proves (5.7).

Finally,

\[
                     V_r=A_0=(\gamma_H(0),(0,m)),
\]

which proves the sharing claim.  QED.

The points `(x,m-r+t)` in (5.5)--(5.7), with

\[
                   0\le x<r,qquad1\le t\le r,             \tag{5.8}
\]

are exactly the `r^2` square points whose hook radius is smaller than `r`:

\[
 \max(x,m-(m-r+t))=\max(x,r-t)<r.                          \tag{5.9}
\]

Therefore one combined fan covers all `r^2` upper tails with first component
`gamma_H(r)` and all `r^2` lower tails with first component `gamma_H(-r)`,
simultaneously over every shorter rectangle `K<r`.

### Theorem 6 (explicit all-depth shadow walk)

There is an all-depth two-sided shadow walk for `P_m` of length

\[
                         2m^3+5m^2+4m+1.                   \tag{5.10}
\]

### Proof

First concatenate all middle diagonals (2.5), at cost `M_m`.  Their internal
intervals cover the central square in every chain rectangle.

For every `1<=r<=H<=m`, append the combined fan of Lemma 5.  By (5.8)--(5.9)
these fans cover every upper and lower tail in all rectangles with first
radius longer than the second.  Append the transposed fans to cover every
rectangle with the second radius longer than the first.  Balanced rectangles
have no tails.

The added length is

\[
 \begin{split}
 2\sum_{H=1}^m\sum_{r=1}^H(4r-1)
 &= {4\over3}m(m+1)(m+2)-m(m+1)\\
 &= {m(m+1)(4m+5)\over3}.                                \tag{5.11}
 \end{split}
\]

Adding `M_m` gives

\[
 {2m^3+6m^2+7m+3+m(m+1)(4m+5)\over3}
   =2m^3+5m^2+4m+1.
\]

The diagonal blocks and the two orientations of the fans exhaust the unique
rectangle decomposition (2.4), so every point of `P_m` is covered.  QED.

The fan is the promised mathematical repair of the old volume ledger: its
two independently movable interval endpoints encode an `r` by `r` tail
fibre using only `O(r)` occurrences.  What remains is to reuse these fan arms
inside one near-Hamilton middle order instead of appending them separately.

## 6. Why local seam stitching cannot finish the proof

The total number of upper residual tails is the quantity in (3.9):

\[
                       E_m={m(m+1)^2(m+2)\over6}.           \tag{6.1}
\]

No interval internal to a different chain rectangle can produce one of
these targets: within one factor, the join or meet of members of a fixed hook
chain remains in that hook chain, and the hook rectangles partition `P_m`.
Thus every repair of (6.1) must use a window crossing the old rectangle
partition.

### Proposition 7 (linear-window obstruction)

Let a middle-layer sequence have length `n` and cover all upper residual
tails.  If every selected tail witness has length at most `L`, then

\[
                              nL\ge E_m.                    \tag{6.2}
\]

Consequently, if `n=M_m+O(m^2)`, then

\[
                         L\ge(1/4-o(1))m.                   \tag{6.3}
\]

Moreover at least half of the upper tails require witnesses of length at
least

\[
                         {E_m\over2n}=(1/8-o(1))m.          \tag{6.4}
\]

### Proof

A length-`n` sequence has at most `nL` intervals of length at most `L`, and
one interval has only one coordinatewise maximum.  Distinct targets need
distinct witnessing intervals, proving (6.2).  Since

\[
 E_m=(1/6+o(1))m^4,qquad M_m=(2/3+o(1))m^3,
\]

(6.3) follows.  There are at most `n(E_m/(2n))=E_m/2`
intervals shorter than the threshold in (6.4), proving the last assertion.
QED.

Thus a braid can succeed only through linearly long, coherently nested
windows.  Replacing old seams by literal adjacent cross-rectangle pairs or
realizing every two-point identity of Lemma 4 as its own bounded gadget
cannot resolve all depths.  A bounded halo is excluded only when it bounds
the entire physical witness length; it may still surround a block of length
`Theta(m)`.  Likewise, the transfer identities may remain useful as
endpoints of shared long windows.  The `O(r)` fan windows have exactly the
linear scale forced by Proposition 7.

## 7. Exact remaining gap to `g_4`

Theorems 3 and 6 are shadow theorems, not four-box OR-word theorems.

If the middle targets of a genuine OR word are represented by physical
intervals, their ordered joins and intersections impose upper and lower
shadow conditions.  The converse is false.  In particular:

* an upper point which is a maximum of middle points is already an OR of
  those middle-point labels;
* a lower point in this note is a **minimum** of middle points, not their OR;
* realizing those minima as OR windows requires a factor row with variable
  middle-target witness intervals, exact coordinate pinning, and survival of
  all lower witnesses; and
* no such factorization is supplied by the fan calculation.

There are therefore two independent gaps between Theorem 6 and

\[
                         g_4(m,m,m,m)\le M_m+O(m^2).        \tag{7.1}
\]

First, the fan walk has leading length `3M_m`, not `M_m`: almost all of its
arms must be packed into the existing middle occurrences, with only
`O(m^2)` repetitions.  Second, that packed shadow order must admit a
variable-band factor and lower-target pinning.  Proposition 7 shows that the
successful intervals cannot remain local; a positive fraction must have
linear length.

The surviving precise target is consequently:

> Interleave the diagonal points so that the two arms of all radius-transfer
> fans are realized by shared, linearly long intervals in a middle walk of
> length `M_m+O(m^2)`, and then prove a compatible variable-witness
> factorization.

The fixed-depth theorem proves the correct surface scale for every bounded
band, while the all-depth fan proves that the residual geometry admits
quadratic endpoint compression.  Neither result, alone or together, is a
proof of (7.1).
