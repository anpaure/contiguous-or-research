# Four-box factor escape: depth-truncated fans give a genuine max-word

## 1. Outcome and theorem ledger

Put

\[
 P_m=[0,m]^4,
 \qquad
 M_m=[z^{2m}](1+z+\cdots+z^m)^4
     ={2m^3+6m^2+7m+3\over3}.
\]

The radius-transfer note produced a two-sided **shadow** walk, but not a
factor word.  This note proves a factor theorem for a substantial part of
that construction.

### New proved result

For every `1<=D<=2m`, there is an explicit word in `P_m`, of length at most

\[
 \boxed{M_m+D(11m^2+13m+3)},                         \tag{1.1}
\]

whose contiguous coordinatewise maxima contain every point of ranks

\[
                  2m-D,2m-D+1,\ldots,2m+D.           \tag{1.2}
\]

The construction is search-free.  It uses the central diagonal blocks and
the radius-transfer fans, but every fan is truncated by **rank depth** rather
than by radius.  A residual tail target at depth `d` has a canonical fan
witness of exactly `d+1` middle points, even if its radius is of order `m`.
After a local run padding, the entire middle row has a delay-`D` maximal
factor.  Thus lower intersections become actual contiguous maxima in the
factor word.

In particular, uniformly for `D=o(m)`, the explicit word has length

\[
                         M_m+o(M_m).                  \tag{1.3}
\]

This is a genuine growing-band factor theorem for the four-box geometry.
It is stronger than a two-sided shadow statement.

At the opposite endpoint, take `D=2m-1` and append the full point literally.
This covers every nonzero point of the box and gives the fully rigorous,
though non-sharp, corollary

\[
 g_4(m,m,m,m)
 \le M_m+22m^3+15m^2-7m-2.                            \tag{1.4}
\]

Thus the construction really is a max-word even at all depths; what fails at
all depths is the desired surface-size error, not validity.

### Also proved

For the literal architecture in which each canonical upper fan is retained
as a contiguous block and one takes a common fixed-delay factor, the run
padding used below is optimal in order of magnitude.  Every upper fan has a
coordinate atom occurring only at its peak.  A delay-`D` factor therefore
forces at least `D` extra peak-containing occurrences in that block.  This
gives an order-independent `Omega(Dm^2)` cost over the `Theta(m^2)` fan
blocks.

For the full, untruncated fans a common delay must be at least `2m-1`; hence
literal blockwise fixed-delay factorization costs `Omega(m^3)`.  It cannot
give `M_m+O(m^2)`.

### Not proved

Equation (1.1) covers only a central rank band.  It does **not** prove

\[
                         g_4(m,m,m,m)\le M_m+O(m^2).
\]

Taking `D=Theta(m)` makes the error in (1.1) itself `Theta(m^3)`.  A complete
surface-error theorem still needs a variable-band or globally interleaved
mechanism that avoids paying one length-`Theta(m)` plateau at every fan
block.  The obstruction proved here applies only to literal canonical fan
blocks with a common fixed delay; it does not rule out such a mechanism.

## 2. Prefix-set model and the factor identity

Represent a point `x=(x_1,x_2,x_3,x_4)` by the prefix set

\[
 \widehat x=\{(c,s):1\le c\le4,\ 1\le s\le x_c\}.
\]

Coordinatewise maximum and minimum then become set union and intersection.
The elements `(c,s)` will be called **atoms**.

Let `T=(T_1,...,T_L)` be a row of points and let `D>=0`.  Define its maximal
delay-`D` factor by

\[
 A_j=\bigcap_{i=\max(1,j-D)}^{\min(L,j)}T_i,
 \qquad 1\le j\le L+D.                              \tag{2.1}
\]

For an atom `b`, inspect the binary incidence word

\[
            (1_{b\in T_1},\ldots,1_{b\in T_L}).
\]

The standard run criterion says that

\[
                 T_i=A_i\vee\cdots\vee A_{i+D}       \tag{2.2}
\]

for every `i` if and only if every internal `1`-run in every atom word has
length at least `D+1`.  Runs meeting either end may be shorter.

We need the following slightly more general erosion identity.

### Lemma 1 (short intersections become factor windows)

Assume the delay-`D` run condition.  If

\[
                    1\le l\le r\le L,
                    \qquad r-l\le D,
\]

then

\[
 \boxed{
   \bigvee_{j=r}^{l+D}A_j=\bigcap_{i=l}^{r}T_i.
 }                                                        \tag{2.3}
\]

For every interval, with no length restriction,

\[
 \boxed{
   \bigvee_{i=l}^{r}T_i=\bigvee_{j=l}^{r+D}A_j.
 }                                                        \tag{2.4}
\]

#### Proof

Work one atom at a time.  Every defining interval of an `A_j` on the left
of (2.3) contains `[l,r]`, because `r<=j<=l+D`.  Therefore absence anywhere
on `[l,r]` forces absence from every such `A_j`.

Conversely, suppose the atom is present throughout `[l,r]`, and let `[a,c]`
be the maximal `1`-run containing it.  If the run is internal, it has length
at least `D+1`; hence there is a `j in [r,l+D]` for which
`[j-D,j] subseteq [a,c]`.  If the run meets a boundary, use the corresponding
truncated interval in (2.1).  Thus the atom belongs to at least one `A_j`.
This proves (2.3).

Taking `l=r=i` in (2.3) gives (2.2).  The union over `i=l,...,r` of the
overlapping factor windows `[i,i+D]` is exactly `[l,r+D]`, proving (2.4).
QED.

## 3. Hook coordinates and the exact depth of a fan window

Use the audited hook coordinates

\[
 \gamma_H(p)=
 \begin{cases}
  (H+p,m-H),&p\le0,\\
  (H,m-H+p),&p\ge0,
 \end{cases}
 \qquad -H\le p\le H.                                \tag{3.1}
\]

Every point of `P_m` is uniquely

\[
             X(H,p;K,q)=(\gamma_H(p),\gamma_K(q)),     \tag{3.2}
\]

and its rank is `2m+p+q`.

Assume `H>K`.  The middle diagonal of the hook rectangle is

\[
 T_{H,K}(s)=(\gamma_H(s),\gamma_K(-s)),
             \qquad -K\le s\le K.                    \tag{3.3}
\]

Its internal joins and meets cover precisely the central square `|p|<=K`.
The residual upper and lower tails have respectively `p=r>K` and `p=-r<-K`.

For fixed `1<=r<=H`, retain the audited fan points

\[
 \begin{array}{ll}
 U_x=(\gamma_H(r-x),(x,m-r)),&0\le x<r,\\
 V_t=(\gamma_H(r-t),(0,m-r+t)),&1\le t\le r,
 \end{array}                                             \tag{3.4}
\]

in the order

\[
                   U_{r-1},\ldots,U_0,V_1,\ldots,V_r.  \tag{3.5}
\]

Their interval from `U_x` to `V_t` has join

\[
                 (\gamma_H(r),(x,m-r+t)).              \tag{3.6}
\]

The lower fan points are

\[
 \begin{array}{ll}
 A_x=(\gamma_H(-x),(x,m)),&0\le x\le r,\\
 B_t=(\gamma_H(-t),(r,m-r+t)),&1\le t<r,
 \end{array}                                             \tag{3.7}
\]

in the order

\[
                    A_0,\ldots,A_r,B_{r-1},\ldots,B_1. \tag{3.8}
\]

The interval from `A_x` through `A_r` and then through `B_t` (ending at
`A_r` when `t=r`) has meet

\[
                 (\gamma_H(-r),(x,m-r+t)).             \tag{3.9}
\]

Here is the crucial depth observation.

### Lemma 2 (fan length equals rank depth)

The upper target (3.6) has depth

\[
                          d=x+t,                        \tag{3.10}
\]

and its canonical witness in (3.5) has exactly `d+1` points.

The lower target (3.9) has depth

\[
                          d=2r-x-t,                     \tag{3.11}
\]

and its canonical witness in (3.8) again has exactly `d+1` points.

#### Proof

The second pair in (3.6) and (3.9) has centered rank deviation

\[
                  q=x+(m-r+t)-m=x-r+t.
\]

Adding `p=r` gives (3.10), while adding `p=-r` gives rank deviation
`x+t-2r`, proving (3.11).

In (3.5), the interval from `U_x` through `U_0` has `x+1` terms and the
part through `V_t` has `t` terms.  Its length is `x+t+1`.  In (3.8), write
`a=r-x` and `b=r-t`.  The interval has `a+1` terms through `A_r` and then
`b` terms in the `B` arm, for total `a+b+1=2r-x-t+1`.  QED.

This identity is the reason a large-radius fan does not need a large delay
when only a shallow rank band is required.

## 4. Depth-truncated fan blocks

Fix `D`.  For every `(H,r)` with `1<=r<=H<=m`, define the upper truncated
block

\[
 \mathcal U_{H,r}^{(D)}=
   (U_a,U_{a-1},\ldots,U_0,V_1,\ldots,V_b),             \tag{4.1}
\]

where

\[
                  a=\min(D-1,r-1),\qquad b=\min(D,r). \tag{4.2}
\]

It contains every upper fan witness of depth at most `D`.

Define the lower truncated block

\[
 \mathcal L_{H,r}^{(D)}=
   (A_{r-c},A_{r-c+1},\ldots,A_r,
      B_{r-1},B_{r-2},\ldots,B_{r-e}),                 \tag{4.3}
\]

where

\[
                  c=\min(D,r),\qquad e=\min(D-1,r-1),\tag{4.4}
\]

and the `B` part is empty when `e=0`.  It contains every **residual** lower
fan witness (`x<r`) of depth at most `D`.  When `D<r`, the only shallow
canonical witness omitted by this wording is `x=r,t=r-D`; its target has
hook radius `K=r`, so it belongs to the central square and is already
covered by a complete middle diagonal.

Both blocks have length at most `2D`.  Include also their transposes, which
cover the tails with the second hook radius longer than the first.

For the central square, retain every complete middle diagonal (3.3).  Thus
the raw row consists of:

1. all `(m+1)^2` complete diagonal blocks;
2. the upper and lower truncated fan block for every `(H,r)`;
3. the two transposed fan blocks for every `(H,r)`.

The diagonal blocks contain every middle point exactly once.  The fan blocks
are additional middle occurrences.

## 5. A local padding lemma

We next make the raw row delay-`D` factorable.

### Lemma 3 (run shapes inside the blocks)

For every atom:

1. its incidence word in a diagonal block is a prefix, a suffix, all ones,
   or all zeros;
2. its incidence word in a lower truncated fan is a union of a prefix and a
   suffix (either may be empty);
3. its incidence word in an upper truncated fan has at most one internal
   `1`-run, and every such internal run contains the peak `U_0`.

#### Proof

Along (3.3), `gamma_H(s)` is coordinatewise increasing and
`gamma_K(-s)` is coordinatewise decreasing.  This proves item 1.

In a lower fan, the first-pair parameter decreases to `-r` and then
increases.  Since each coordinate of `gamma_H(p)` is nondecreasing in `p`,
its `1`-set is a prefix union a suffix.  In the second pair, the first
coordinate increases and the second decreases, giving a suffix and a prefix
respectively.  This proves item 2.

In an upper fan, the first-pair parameter increases to `r` and then
decreases.  Any internal `1`-run therefore contains the peak.  In the second
pair, the first coordinate decreases and the second increases, so their
incidence words touch a boundary.  This proves item 3.  QED.

Perform the following padding independently in every block:

* replace its first term and its last term by `D+1` copies;
* in every upper fan block, also replace the peak `U_0` by `D+1` copies.

If two of these distinguished terms coincide as positions, redundant copies
may be omitted; retaining them only enlarges the stated upper bound.

### Lemma 4 (global run condition)

After the padding, the concatenation of the blocks in any order satisfies
the delay-`D` run condition.

#### Proof

By Lemma 3, a run internal to one block either already meets a block boundary
or contains the upper peak.  It therefore contains a plateau of length
`D+1`.

A run crossing a seam contains the terminal plateau of the left block, the
initial plateau of the right block, or both.  A run cut by a zero at the seam
still has the appropriate plateau on its own side.  Hence every global
internal `1`-run has length at least `D+1`.  QED.

Padding preserves all canonical joins and meets.  For a lower witness, use
the copy of a padded endpoint nearest the block interior.  No lower witness
passes through an upper peak plateau.  Therefore every lower witness retained
in Sections 3--4 still has physical length at most `D+1`.

## 6. The fixed-band max-word theorem

### Theorem 5

For every `1<=D<=2m`, the maximal delay-`D` factor of the padded row is a
word whose contiguous maxima contain every point of `P_m` with rank between
`2m-D` and `2m+D`.

#### Proof

Every point is uniquely `X(H,p;K,q)`.  Assume first `H>=K`.

If `|p|<=K`, it is in the central square.  When `p+q>=0`, the interval

\[
                  T_{H,K}(-q),\ldots,T_{H,K}(p)        \tag{6.1}
\]

has join `X(H,p;K,q)`.  When `p+q<=0`, the interval

\[
                  T_{H,K}(p),\ldots,T_{H,K}(-q)       \tag{6.2}
\]

has meet `X(H,p;K,q)`.  In either case its length is
`|p+q|+1`, at most `D+1` inside the required band.

If `p>K`, put `r=p`.  Write the second square point uniquely as

\[
                       (x,m-r+t),
 \qquad 0\le x<r,\quad1\le t\le r.                    \tag{6.3}
\]

By Lemma 2 its upper depth and its upper-fan witness length minus one are
both `x+t`.  Thus a target of depth at most `D` occurs in (4.1).

If `p<-K`, put `r=-p` and use the same parametrization (6.3).  Its lower
depth and lower-fan witness length minus one are both `2r-x-t`, so a target
of depth at most `D` occurs in (4.3).

The case `K>H` is supplied by the transposed blocks.  We have therefore
represented every upper target in the band as a join of a `T`-interval and
every lower target as a meet of a `T`-interval of length at most `D+1`.

Lemma 4 permits the maximal factor (2.1).  Formula (2.4) turns every upper
join into a factor-word maximum, and (2.3) turns every retained lower meet
into a factor-word maximum.  Middle points follow from (2.2).  QED.

Zero factor entries, if any, may be deleted after choosing the witnesses:
deleting zeros preserves the maximum of every nonzero witnessing interval.

## 7. Exact length accounting

The raw diagonal blocks have total length `M_m`.  There are

\[
                         (m+1)^2                         \tag{7.1}
\]

of them.

There are

\[
                    N={m(m+1)\over2}                    \tag{7.2}
\]

pairs `(H,r)`.  For each pair and each of the two orientations there are an
upper and a lower block.  Since every such block has length at most `2D`,
all raw fan blocks contribute at most

\[
                         8DN=4Dm(m+1).                 \tag{7.3}
\]

The total number of blocks is

\[
       (m+1)^2+4N=(m+1)(3m+1).                         \tag{7.4}
\]

Endpoint padding contributes at most twice `D` times (7.4).  There are
`2N=m(m+1)` upper fan blocks, so peak padding contributes at most
`Dm(m+1)`.  Hence the padded middle row has length at most

\[
 \begin{split}
 L
 &\le M_m+4Dm(m+1)+2D(m+1)(3m+1)+Dm(m+1)\\
 &=M_m+D(11m^2+13m+2).                              \tag{7.5}
 \end{split}

The maximal factor has length `L+D`, proving (1.1).

For fixed `D` this is the exact surface scale `M_m+O_D(m^2)`.  More
importantly, the proof is uniform: every `D=o(m)` gives `M_m+o(M_m)` while
covering a band whose depth tends to infinity at an arbitrary sublinear
rate.

## 8. A matching obstruction for literal fixed-delay fan blocks

The padding above is not merely a loose convenience within its architecture.

### Proposition 6 (the peak-atom obstruction)

Fix `r>=2`.  In the canonical upper fan (3.5), the atom

\[
                 b_{H,r}=(2,m-H+r)                    \tag{8.1}
\]

of the first coordinate pair occurs at exactly one canonical position,
the peak `U_0`.

Suppose a row retains this fan as a contiguous ordered block, possibly with
extra terms inserted between its canonical terms, and suppose the two
canonical neighbours of `U_0` remain on opposite sides of the peak region.
If the whole row has a delay-`h` factor, at least `h` additional
`b_(H,r)`-containing occurrences must be inserted into that peak region.

#### Proof

For nonnegative `p`, the second coordinate of `gamma_H(p)` is `m-H+p`.
The first-pair parameters in (3.5) increase to `r` and then decrease.  Thus
the threshold `m-H+r` is attained only at `p=r`, namely at `U_0`; its two
canonical neighbours omit the atom.

The atom therefore forms an internal `1`-run confined to the peak region.
The delay-`h` run criterion forces that run to have length at least `h+1`.
Besides the canonical peak occurrence, at least `h` further containing
occurrences are necessary.  QED.

The peak regions of disjoint literal fan blocks are disjoint, irrespective
of the order of those blocks.  There are `Theta(m^2)` upper fan blocks over
both orientations.  Consequently a common delay `h` costs

\[
                            \Omega(hm^2)                \tag{8.2}
\]

extra occurrences in this architecture.  Translating every lower witness
of every full fan by the erosion identity requires

\[
                            h\ge2m-1,                   \tag{8.3}
\]

because the longest canonical lower-fan witness has `2m` terms.  Therefore
literal full-fan blocks plus one fixed-delay factor incur `Omega(m^3)`
extra length.

For the depth-truncated construction with `D>=2`, both canonical neighbours
of the peak are retained, so `h=D` in Proposition 6 and (8.2) matches the
`Theta(Dm^2)` plateau term in (7.5).  At `D=1` the raw fan mass is already
`Theta(m^2)`, but Proposition 6 alone does not certify padding optimality.
Thus, for growing depth, improving (1.1) inside this exact block architecture
cannot come from more economical padding.  It must come from sharing peaks
across fan blocks, interleaving the canonical terms so the singleton peak
runs disappear, or abandoning a common fixed delay.

## 9. Exact remaining implication

The radius-transfer geometry itself is now factor-compatible at every
sublinear depth.  The unresolved all-depth step is sharper than before:

> Interleave the `Theta(m^2)` upper fan peaks so that their atom runs are
> shared globally, while retaining the `d+1`-term lower witnesses at every
> depth `d`, or replace the common delay by a variable-band factor with the
> same effect.

Theorem 5 proves that there is no separate Hall or pinning obstruction for
any prescribed sublinear band in this explicit geometry: the maximal factor
itself works.  Proposition 6 explains exactly why simply extending the same
literal blocks to depth `Theta(m)` loses a main-order term.

What remains open is not the existence of local factors.  It is global peak
sharing across radii and hook rectangles.  Until that is proved, no
surface-error bound for the complete four-box max-word, and hence no
constant-one theorem for the original Boolean problem, follows.

### Direct generation rule

For completeness, the proof is algorithmic in the following literal sense.

```text
FOUR_BOX_BAND_WORD(m,D):
    blocks = []

    for H=0..m:
        for K=0..m:
            append (T_HK(s) : s=-min(H,K)..min(H,K)) to blocks

    for both orientations of the two coordinate pairs:
        for H=1..m:
            for r=1..H:
                append the truncated upper block (4.1) to blocks
                append the truncated lower block (4.3) to blocks

    in every block repeat its first and last point D additional times
    in every upper block repeat U_0 D additional times
    concatenate the padded blocks to obtain T[1..L]

    for j=1..L+D:
        A[j] = coordinatewise_minimum(
                   T[max(1,j-D)..min(L,j)])

    return A
```

All coordinates are integers in `[0,m]`.  Replacing coordinate `x_c` by the
prefix of length `x_c` in the corresponding disjoint increment chain turns
this directly into a bitmask word.  A sliding minimum queue gives
`O(L)` arithmetic operations per coordinate; even the naive `O(DL)` version
is output-polynomial.

## 10. Five-point audit and the aggregation boundary

This section records the exact scope checks needed before the theorem is used
elsewhere.

### 10.1 It is an actual max-word

The factor entries (2.1) are coordinatewise minima of points of `P_m`, hence
are themselves points of `P_m`.  Under the prefix-set encoding, their
contiguous bitwise OR is exactly their coordinatewise maximum.  Equations
(2.3)--(2.4) therefore produce legal intervals in one ordinary word; no
Johnson adjacency, monotonicity of the factor entries, or shadow-only
interpretation is being assumed.

For a Boolean chain box, replace coordinate value `x_c` by the first `x_c`
increments of its saturated chain.  The same factor entries are then legal
subsets of the original coordinate blocks.  Thus Theorem 5 is genuinely a
local `g_4`-type band result.

### 10.2 Concatenation creates no contamination

Every chosen witness in `T` lies inside one raw block.  Repeating an endpoint
or an upper peak does not change its meet or join; lower witnesses choose the
plateau copy nearest the interior and retain length at most `D+1`.

The corresponding factor-word interval may extend beyond that raw block.
This causes no contamination: (2.3) is a global identity in the fully
concatenated row, and (2.4) follows from the exact global factor equation
`T_i=vee_(j=i)^(i+D) A_j`.  The run padding was imposed after all blocks were
concatenated, so these identities already include every seam.

### 10.3 The boundary formula is exact

At the left boundary, a maximal `1`-run beginning at position `1` is handled
by choosing `j=r` in (2.3); its truncated factor window ends at `r` and lies
inside the run.  At the right boundary, choose `j=l+D`; its truncated window
is `[l,min(L,l+D)]` and lies inside the run.  An internal run admits a full
length-`D+1` window as proved in Lemma 1.  Hence (2.3), including `l=1` or
`r=L`, has no unstated cyclic or sentinel assumption.

### 10.4 Padding is per block, not per atom

One repeated endpoint simultaneously lengthens the runs of every atom it
contains.  The construction repeats physical **points**, not coordinate
atoms separately.  There are `(m+1)(3m+1)` blocks and `m(m+1)` upper peaks,
so (7.5) accounts for every repetition.  There is no hidden factor `m` in
the additive term.

### 10.5 Why literal tails do not finish the four-box problem

Let `R_m(D)` be the number of points of `P_m` outside the central band
`|rank-2m|<=D`.  The band itself contains at most

\[
                         (2D+1)M_m                       \tag{10.1}
\]

points.  Consequently, if `D=o(m)`,

\[
 R_m(D)\ge(m+1)^4-(2D+1)M_m=\Theta(m^4).               \tag{10.2}
\]

In particular,

\[
                         D\asymp\sqrt{m\log m}          \tag{10.3}
\]

followed by literal tails has length `Theta(m^4)`, not
`M_m+o(M_m)`.  The sum of four independent uniform chain coordinates has
fluctuation scale `Theta(m)`, unlike the `Theta(sqrt(k))` rank scale of a
`k`-dimensional Boolean cube.

Even taking `D` close to the full half-range illustrates the conflict.  Put
`D=2m-h` with `h<=m`.  One extreme tail alone contains

\[
                    {h+3\choose4}=\Theta(h^4)           \tag{10.4}

points (the ranks `0,...,h-1`).  Making literal
tails `o(M_m)` requires `h=o(m^(3/4))`, hence `D=(2-o(1))m`; but then the
proved padding term `Theta(Dm^2)` is itself `Theta(M_m)`.

Therefore Theorem 5 does not satisfy the uniform full-box hypothesis in
`FIXED_DIMENSION_GRID_REDUCTION.md`.  Applying that reduction still requires

\[
                 g_4(\ell_1,\ldots,\ell_4)
                 \le w(\ell_1,\ldots,\ell_4)
                    +O((1+\ell_1+\cdots+\ell_4)^2)      \tag{10.5}
\]

for complete, generally unequal boxes.  A central-band theorem plus literal
tails cannot substitute for (10.5).

There is also a qualitative aggregation warning: typical SCD chain heights
are of order `sqrt(k)`.  A global Boolean band of half-width
`sqrt(k log k)` already exceeds the full rank range of many such local
boxes.  On those boxes Theorem 5 must be used with `D=Theta(m)`, exactly the
regime where its displayed additive term is main-order.  Thus the moment
estimate currently used in the chain-box reduction does not by itself remove
the loss; any successful averaging refinement would need an additional
weighted construction or cancellation theorem not proved here.

The audited conclusion is therefore precise:

* Theorem 5 is a valid single max-word and a uniform near-width factor for
  every sublinear four-box band.
* It removes factorability as an obstruction for depth-truncated fans.
* It does not prove a full four-box surface theorem or an asymptotic
  constant-one Boolean construction.

## 11. The exact peak-sharing problem after the factor theorem

The peak atoms are not unrelated.  Reparametrize an upper fan by

\[
                         c=H-r.
\]

For `0<=u<r<=m-c` and `0<=x<r`, put

\[
 \begin{split}
 P_{c,u}&=(c+u,m-c,0,m-u),\\
 E_{c,r,x}&=(c+r,m-c-x,x,m-r).
 \end{split}                                             \tag{11.1}
\]

Here `P_(c,u)` is the peak `U_0` of radius `u` (with the harmless radius-zero
boundary included), and `E_(c,r,x)=U_x` is an upper-arm point.  A direct
coordinate calculation gives

\[
 \boxed{
 E_{c,r,x}\vee P_{c,u}
      =(c+r,m-c,x,m-u).
 }                                                        \tag{11.2}
\]

Writing `u=r-t`, the right side is exactly the upper tail target

\[
                 (\gamma_{c+r}(r),(x,m-r+t)).           \tag{11.3}
\]

Thus every upper tail in one orientation has a canonical two-provider form
using one arm point and one peak from the **same `c`-diagonal**.  All fans
with fixed `c` also share the same critical atom `(2,m-c)`; there are only
`m+1` such critical atom levels, not `Theta(m^2)` unrelated ones.

This identifies the most economical possible escape from Proposition 6:

> Order the triangular family `E_(c,r,x)` together with the peak chain
> `P_(c,0),...,P_(c,m-c)` so that every pair in (11.2) is joined by an
> interval staying below its target, and couple these orders across `c` and
> with the reflected lower family.

The original radius fan realizes (11.2) separately for every `r`; the open
problem is to reuse the same physical peak chain for many radii.  Intervening
peaks `P_(c,s)` are harmless exactly when `u<=s<=r`, since then they lie below
the target in (11.2).  This is the precise nesting that a successful global
braid must exploit.

Equation (11.2) is a reduction, not a packing theorem.  Arm points from a
different radius can exceed the target in coordinate three, so simply
placing every arm next to one common peak chain does not work.  The remaining
object is a triangular interval-ordering problem, together with its lower
reflection and factor compatibility.  It is substantially smaller and more
structured than an arbitrary ordering of the `Theta(m^3)` middle points.
