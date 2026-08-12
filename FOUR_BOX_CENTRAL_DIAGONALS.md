# Four-chain boxes: a two-sided adjacent-shadow theorem and its exact limitation

## 1. Status

Let

\[
P_m=[0,m]^4
\]

with coordinatewise join, and let

\[
M_m=[z^{2m}](1+z+\cdots+z^m)^4
    ={2m^3+6m^2+7m+3\over3}
\]

be its width.

There is an explicit ordering, in `O(m^2)` contiguous blocks, of all `M_m`
middle-rank points with the following property:

* the joins of adjacent points cover all but at most `m(m+1)` points of
  rank `2m+1`;
* the meets of adjacent points cover all but at most `m(m+1)` points of
  rank `2m-1`.

Before the blocks are concatenated, the internal block edges leave exactly
`m(m+1)` targets uncovered on each side.  The extra seam edges can only
decrease those two defect sets.

Thus four dimensions genuinely evade the rigid three-dimensional
adjacent-shadow obstruction: both first shadows are complete up to a
quadratic surface term.

This is **not** a proof that

\[
g_4(m,m,m,m)\le M_m+O(m^2).
\]

For the same block paths, the total defect over all lower (or all upper)
depths is exactly

\[
{m(m+1)^2(m+2)\over6}=\Theta(m^4).
\]

In particular, the tempting assertion that every point of an imbalanced
chain rectangle is a consecutive minimum or maximum of its central diagonal
is false.  The first-shadow theorem survives; the all-depth version does not.

## 2. The square hook decomposition

For `0<=h<=m`, let `C_h` be the standard symmetric chain in `[0,m]^2`

\[
\begin{split}
C_h={}&(0,h),(1,h),\ldots,(m-h,h),\\
     &(m-h,h+1),\ldots,(m-h,m).
\end{split}                                                    \tag{2.1}
\]

It has height

\[
2H,\qquad H=m-h.
\]

The `m+1` chains `C_0,...,C_m` partition `[0,m]^2`.  Apply this
decomposition independently to the first and last coordinate pairs.  The
products

\[
                         C_h\times C_k                         \tag{2.2}
\]

partition `P_m`.  Write

\[
                         H=m-h,\qquad K=m-k.
\]

In chain coordinates, (2.2) is the rectangle

\[
                         [0,2H]\times[0,2K].                  \tag{2.3}
\]

The minimum of (2.2) has global rank `h+k`, so the global middle rank
`2m` is the local diagonal of rank

\[
                         s=H+K.                                \tag{2.4}
\]

## 3. The central diagonal path

Put

\[
 L=\max(0,H-K),\qquad R=\min(2H,H+K).
\]

The middle points in the rectangle (2.3), in their natural order, are

\[
                         q_i=(i,s-i),\qquad L\le i\le R.       \tag{3.1}
\]

In the original four coordinates, `(i,j)` means the point whose first
coordinate-pair component is the `i`-th member of `C_h` and whose second
coordinate-pair component is the `j`-th member of `C_k`.

Every consecutive pair in (3.1) satisfies

\[
\begin{split}
 q_i\wedge q_{i+1}&=(i,s-i-1),\\
 q_i\vee q_{i+1}&=(i+1,s-i).
\end{split}                                                    \tag{3.2}
\]

This remains true in the original four coordinates.  One component chain
makes one upward cover step and the other makes one downward cover step;
the two steps lie in disjoint coordinate pairs.

The path (3.1) has

\[
                         2\min(H,K)+1                          \tag{3.3}
\]

vertices and `2 min(H,K)` internal edges.

## 4. Exact adjacent-shadow defect in one rectangle

### Lemma 1

If `H=K`, the values in each line of (3.2) are respectively every point of
local rank `s-1` and every point of local rank `s+1`.

If `H!=K`, each line of (3.2) misses exactly one point of the corresponding
adjacent rank.

### Proof

The lower-rank points have the form

\[
                         (i,s-1-i)
\]

subject to the two coordinate bounds.  The intersections in (3.2) use
exactly

\[
       \max(0,H-K)\le i\le\min(2H-1,H+K-1).          \tag{4.1}
\]

If `H=K`, (4.1) is the entire lower diagonal.  If `H>K`, the one omitted
point is

\[
                         (H-K-1,2K),                          \tag{4.2}
\]

whereas if `K>H` the transposed point is omitted.

The upper-rank points have the form `(i,s+1-i)`.  The unions in (3.2) use
first coordinates from `L+1` through `R`.  Again this is the entire upper
diagonal when `H=K`.  If `H>K`, the omitted point is

\[
                         (H+K+1,0),                            \tag{4.3}
\]

and for `K>H` its transpose is omitted. \(\square\)

## 5. Global adjacent-shadow theorem

### Theorem 2

Concatenate the paths (3.1), in any order and either orientation, over all
`(h,k) in {0,...,m}^2`.  The result is a permutation `T` of the global
middle layer of `P_m`.  Its block-internal adjacent meets and joins cover
all but exactly

\[
                         m(m+1)                                \tag{5.1}
\]

points in each adjacent layer.  Consequently the full adjacent shadows of
`T`, including its seam edges, miss at most `m(m+1)` points on either side.

### Proof

The product rectangles partition `P_m`, so their middle diagonals partition
the global middle layer.  This proves the permutation claim.

By Lemma 1, a rectangle contributes one defect on each side precisely when
`H!=K`.  There are

\[
                  (m+1)^2-(m+1)=m(m+1)                       \tag{5.2}
\]

ordered unequal pairs.  This proves the exact block-internal count.  A seam
between two blocks merely adds another adjacent meet and join, and therefore
cannot destroy an already represented target. \(\square\)

As a consistency check, the adjacent rank size is

\[
 [z^{2m-1}](1+z+\cdots+z^m)^4=M_m-(m+1).                     \tag{5.3}
\]

The block paths have altogether

\[
                         M_m-(m+1)^2                          \tag{5.4}
\]

internal edges, and the difference between (5.3) and (5.4) is exactly
`m(m+1)`.

## 6. Exact all-depth limitation

The following calculation is the required guardrail against an incorrect
all-depth extrapolation.

Assume `H>=K`.  For a consecutive interval `q_i,...,q_j` of (3.1),

\[
\begin{split}
 \bigwedge_{t=i}^j q_t&=(i,s-j),\\
 \bigvee_{t=i}^j q_t&=(j,s-i).                               \tag{6.1}
\end{split}
\]

The consecutive maxima cover exactly the upper-half points of the rectangle
with first coordinate at most `H+K`.  They miss the complete tail

\[
       \{H+K+1,\ldots,2H\}\times\{0,\ldots,2K\},             \tag{6.2}
\]

which has size

\[
                         (H-K)(2K+1).                          \tag{6.3}
\]

Dually, the consecutive minima miss the complete lower tail

\[
       \{0,\ldots,H-K-1\}\times\{0,\ldots,2K\},              \tag{6.4}
\]

of the same size.  When `K>H`, transpose the two coordinates.  Thus the
one-sided all-depth defect of one rectangle is

\[
                         |H-K|(2\min(H,K)+1).                  \tag{6.5}
\]

Summing (6.5) over all ordered pairs gives

\[
\begin{split}
D_m
 &=2\sum_{H=1}^m\sum_{K=0}^{H-1}(H-K)(2K+1)\\
 &=2\sum_{H=1}^m {H(H+1)(2H+1)\over6}\\
 &=\boxed{{m(m+1)^2(m+2)\over6}.                              \tag{6.6}
\end{split}
\]

This is `Theta(m^4)`, the same order as the volume of `P_m`.  Hence the
central-diagonal product construction has a surface-sized defect at depth
one but a volume-sized defect over all depths.

## 7. What this does and does not establish

The construction proves a useful structural distinction between three and
four local dimensions:

* in three dimensions the simultaneous adjacent-shadow matching is forced
  into concentric rings;
* in four dimensions there is an explicit `O(m^2)`-block central
  permutation whose two adjacent shadows have only `O(m^2)` defects.

The old three-dimensional rare-coordinate fixed-row obstruction also no
longer applies numerically.  In `[0,m]^4`, a top coordinate increment occurs
in `Theta(m^2)` middle points, whereas the rank-slack delay is only
`Theta(m)`.  This removes that particular no-go theorem, but it does not
prove factorability.

To obtain the desired four-box surface bound, one still needs a new global
mechanism that does at least one of the following:

1. interleaves the imbalanced rectangles so their long tails in (6.2)--(6.4)
   are represented across blocks;
2. supplies a variable-band factor whose short range maxima encode those
   tails with only `O(m^2)` extra positions; or
3. replaces the product-hook rectangles by a genuinely four-dimensional
   ordered orthogonal-chain or growth-diagram construction.

Nothing in Theorem 2 supplies the lower-half OR labels or the required pin
survival.  Therefore the rigorous conclusion of this pass is the adjacent-
shadow theorem plus the exact `Theta(m^4)` limitation, not a new bound on
`g_4`.
