# Cyclic-interval symmetric-chain resolutions

> **Initialization update.**  The uniform-depth argument below is enough
> for the conditional asymptotic theorem.  A stronger nonuniform ledger is
> now proved in `CYCLIC_INTERVAL_LIFT_INITIALIZATION_AUDIT.md`: if `H_pi`
> is the largest radius assigned to order `pi`, then every exact resolution
> satisfies
> `sum_pi H_pi=O(W sqrt(log(n)/n))`, and it linearizes in
> `W+O(W sqrt(log(n)/n))` entries without literal tails.  That note also
> proves that a literal necklace-poset rotation lift cannot supply the
> required wreath bundles on more than `o(W)` chains.

## 1. The global object

Let

\[
                         n=2m+1,
 \qquad W=\binom{n}{m},
 \qquad B=\frac Wn=\frac1{m+1}\binom{2m}{m}.
\]

For a cyclic order

\[
                 \pi=(x_0,x_1,\ldots,x_{n-1})
\]

of the ground set, define the cyclic interval

\[
 I_\pi(j,r)=\{x_j,x_{j+1},\ldots,x_{j+r-1}\},
 \qquad 0\le r\le n,
\]

with indices modulo `n`.

Choose a threshold `a_{\pi,j}` in `{0,...,m}` and form

\[
 \mathcal C_{\pi,j}
   =\bigl(I_\pi(j,r):a_{\pi,j}\le r\le n-a_{\pi,j}\bigr).
                                                        \tag{1.1}
\]

This is a saturated symmetric chain in `B_n`.

### Definition

A **cyclic-interval SCD resolution** is a family of `B` cyclic orders and
thresholds such that the `nB=W` chains in (1.1) partition `B_n`.

The middle member of `C_{\pi,j}` is `I_\pi(j,m)`.  Therefore the middle
members belonging to one order form a tight cyclic wreath, and every
resolution induces a decomposition of the whole middle layer into wreaths.
Consequently this object is at least as strong as the Baranyai--Katona wreath
conjecture in the coprime case `(n,m)=(2m+1,m)`.

Its extra content is vertical: the same cyclic orders must resolve all
Boolean ranks into symmetric chains.

## 2. Move-to-front meaning

The maximal prefix chain of the rotation

\[
                (x_j,x_{j+1},\ldots,x_{j-1})
\]

contains `C_{\pi,j}`.  Moving the last symbol `x_{j-1}` to the front changes
this rotation to the preceding one.  Thus one cyclic order is a cycle of
move-to-front states, and a cyclic-interval SCD resolution is precisely an
SCD bundled into such state cycles.

This is weaker and more intrinsic than demanding that a predetermined SCD
such as Greene--Kleitman have a compatible projection.

## 3. Erosion block

Fix `H<m`.  For one cyclic order put

\[
                         E_j=I_\pi(j,m-H).
                                                        \tag{3.1}
\]

For `0\le r\le 2H+1`, overlapping cyclic intervals give

\[
 E_j\cup E_{j+1}\cup\cdots\cup E_{j+r}
       =I_\pi(j,m-H+r).                              \tag{3.2}
\]

Linearize the cyclic block by writing

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.       \tag{3.3}
\]

Every cyclic witness in (3.2) is now an ordinary contiguous interval.

## 4. Conditional asymptotic theorem

### Theorem

If cyclic-interval SCD resolutions exist for all sufficiently large odd
dimensions, then

\[
       \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
                                                        \tag{4.1}
\]

The same conclusion follows from resolutions with `o(W)` defects, provided
the total number of uncovered chain members is `o(W)`.

### Proof

First let `k=n=2m+1`.  Choose

\[
             H=(1/2+\varepsilon)\sqrt{n\log n}.
                                                        \tag{4.2}
\]

Use block (3.3) for each of the `B=W/n` cyclic orders.  Consider a set `S`
whose rank lies in

\[
            m-H,\ldots,m,m+1,\ldots,m+1+H.             \tag{4.3}
\]

The resolution puts `S` in a unique chain `C_{\pi,j}`.  Hence

\[
                         S=I_\pi(j,|S|),
\]

and (3.2) represents it as a contiguous OR in the corresponding erosion
block.

Append every nonempty set outside (4.3) literally.  The resulting length is

\[
 W+(2H+1)\frac Wn
   +2\sum_{r=0}^{m-H-1}\binom nr-1.                    \tag{4.4}
\]

The seam term is `o(W)` because `H=o(n)`.  A Chernoff bound gives

\[
 2\sum_{r=0}^{m-H-1}\binom nr
   \le 2^{n+1}\exp\!\left(-\frac{2H^2}{n}+o(1)\right)
   =o(W),                                               \tag{4.5}
\]

using `W=Theta(2^n/sqrt(n))` and (4.2).  This proves (4.1) in odd
dimension.

The trimmed one-bit lift satisfies

\[
                         \nu(k+1)\le2\nu(k).
\]

Also

\[
 \binom{2m+2}{m+1}=2\binom{2m+1}{m}.
\]

Therefore the same asymptotic ratio holds in the following even dimension.
QED.

## 5. Exact rank ledger

If a chain has threshold `a=m-d`, call `d` its radius.  Rank `m-q` is
present exactly when `d\ge q`, and its symmetric partner is rank
`m+1+q`.  Hence every resolution necessarily has

\[
 \#\{(\pi,j):d_{\pi,j}=d\}
   =\binom{2m+1}{m-d}-\binom{2m+1}{m-d-1}.             \tag{5.1}
\]

This is the odd-dimensional version of the radius law already derived from
the typed fractional matching.  It shows that the thresholds are not free:
only their placement around the cyclic orders remains to be constructed.

## 6. Exact remaining conjecture

The clean asymptotic target is:

> For `n=2m+1`, all but `o(W)` chains of some SCD of `B_n` can be bundled
> into cyclic orders so that every bundled chain consists of fixed-start
> intervals of its order.

This is strictly more global than a Johnson Hamilton path and strictly less
rigid than forcing a canonical SCD projection.  It packages the required
middle enumeration, move-to-front transitions, radius distribution, and all
two-sided shadows into one object.

An exact resolution would imply the wreath conjecture, so proving it may be
too ambitious as a first step.  The approximate statement is enough for
(4.1) and is the appropriate research target.

## 7. Outer-tail compression lowers the required depth

The literal-tail estimate in Section 4 is not optimal.  The construction in
`TRUNCATED_IDEAL_PRODUCT.md` proves the following.  On `2s` coordinates, for

\[
 \sqrt s\le H=o(s^{2/3}),
\]

both tails `|S|<=s-H` and `|S|>=s+H` can be covered together by an OR word of
length

\[
 O\!\left(
   \left(1+\frac{H^2}{s}\right)\binom{2s}{s-H}
 \right).                                                   \tag{7.1}
\]

Consequently, if

\[
                 H=\sqrt{s\,\omega(s)},
 \qquad          \omega(s)\longrightarrow\infty
                                                        \tag{7.2}
\]

arbitrarily slowly, (7.1) is `o(binomial(2s,s))`.  Thus an approximate
cyclic-interval resolution only needs to control a central band of half-width

\[
                         \sqrt s\,\omega(1),             \tag{7.3}
\]

not `Theta(sqrt(s log s))`.  The same conclusion transfers between odd and
even dimensions by the trimmed one-bit lift.

This does not prove the approximate resolution, but materially weakens the
vertical demand: the unresolved depth may be chosen arbitrarily slowly above
the Gaussian `sqrt(s)` scale.
