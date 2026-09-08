# Native inverse-pair wreath moves have two-rail all-width current

## Status

The inverse-pair wreath substitution preserves the two central palettes and
has one immediate-upper birail current.  This note computes its **complete**
proper interval current.  At every lower interval length, and hence at every
upper width, the current is the sum of exactly two `2 x 2` rectangles carried
by four nested prefix/suffix rails.  The number of relation types is
independent of the width.

Consequently an aligned serial chain of inverse-pair moves telescopes at
every width simultaneously.  A closed aligned chain has zero signed upper
current at all widths.

This is an equality of palette multisets.  It does not by itself prove that
the old palette remains covered at every intermediate phase, that the
required aligned row pairs coexist in one factor, or that the move joins
components.

No computation or search is used.

## 1. Adjacent-transposition current

Let a cyclic word contain adjacent distinct labels `alpha,beta`.  Write `P_j`
for the set of the `j` labels immediately preceding `alpha`, and `S_j` for
the set of the `j` labels immediately following `beta`.  Assume the two
arcs do not overlap.  Swapping `alpha,beta` changes the multiset of cyclic
length-`j+1` interval sets by

\[
 [P_j+\beta]+[S_j+\alpha]
 -[P_j+\alpha]-[S_j+\beta].                          \tag{1.1}
\]

Indeed, the only changed intervals are the one ending at the first position
and the one starting at the second position.  Formula (1.1) is their exact
new-minus-old current.

## 2. The inverse-pair current at every proper lower length

Use the inverse-pair rows

\[
 \begin{aligned}
 r_0&=(a,b,X,c,d,Y),&
 r_1&=(b,d,X,a,c,Y),\\
 r'_0&=(b,a,X,d,c,Y),&
 r'_1&=(d,b,X,c,a,Y),                                \tag{2.1}
 \end{aligned}
\]

where

\[
 |X|=m-2,\qquad |Y|=m-1,\qquad N=2m+1.               \tag{2.2}
\]

For `0<=j<=m-2`, let

\[
 \begin{aligned}
 X^-_j&=\{x_1,\ldots,x_j\},&
 X^+_j&=\{x_{m-1-j},\ldots,x_{m-2}\},\\
 Y^-_j&=\{y_1,\ldots,y_j\},&
 Y^+_j&=\{y_{m-j},\ldots,y_{m-1}\}.                 \tag{2.3}
 \end{aligned}
\]

Empty ranges mean the empty set.  Put `ell=j+1`, and let `Delta_ell` be the
signed change in the union of the two cyclic length-`ell` interval
palettes.

### Theorem 2.1 (two-rectangle normal form)

For every `1<=ell<=m-1`, with `j=ell-1`,

\[
\boxed{
 \begin{aligned}
 \Delta_\ell={}&
   \bigl([Y^+_j+d]+[Y^-_j+a]
        -[Y^+_j+a]-[Y^-_j+d]\bigr)\\
 &+\bigl([X^-_j+a]+[X^+_j+d]
        -[X^-_j+d]-[X^+_j+a]\bigr).
                                                               \tag{2.4}
 \end{aligned}}
\]

Thus the complete current at every proper lower length is carried by only
the prefix and suffix rails of `X` and `Y`.

#### Proof

Because `ell<=m-1`, no affected interval meets both swapped adjacent pairs
in the same row.  Formula (1.1) can therefore be added independently for
the two swaps.

For `r_0 -> r'_0`, the swap `ab` contributes

\[
 [Y^+_j+b]+[X^-_j+a]-[Y^+_j+a]-[X^-_j+b],           \tag{2.5}
\]

and the swap `cd` contributes

\[
 [X^+_j+d]+[Y^-_j+c]-[X^+_j+c]-[Y^-_j+d].           \tag{2.6}
\]

For `r_1 -> r'_1`, the swap `bd` contributes

\[
 [Y^+_j+d]+[X^-_j+b]-[Y^+_j+b]-[X^-_j+d],           \tag{2.7}
\]

and the swap `ac` contributes

\[
 [X^+_j+c]+[Y^-_j+a]-[X^+_j+a]-[Y^-_j+c].           \tag{2.8}
\]

Adding (2.5)--(2.8) cancels every term containing `b` or `c` and gives
exactly (2.4). \(\square\)

When `ell=m-1`, the two `X` rails both equal `X`, so the second rectangle
vanishes.  The first rectangle is precisely the immediate-upper current
previously obtained from the inverse pair.

## 3. Upper widths

The owner row of one wreath consists of cyclic length-`m+1` intervals in a
ground set of size `2m+1`.  The union of `t+1` consecutive owners is the
cyclic interval of length `m+1+t`; its complement is the cyclic interval of
length

\[
                         (2m+1)-(m+1+t)=m-t.          \tag{3.1}
\]

Let `Delta^up_t` be the signed palette current of these upper width-`t`
unions.

### Corollary 3.1 (two all-width upper rails)

For `1<=t<=m-1`, put `j=m-t-1`.  Then `Delta^up_t` is obtained by
complementing every term in (2.4).  In particular it is the sum of two
`2 x 2` rectangles, on the nested rail pairs

\[
                         (Y^-_j,Y^+_j),
 \qquad                 (X^-_j,X^+_j).               \tag{3.2}
\]

There are four rail types for all widths together, not a new unstructured
damage family at each width.

#### Proof

Equation (3.1) is a value-preserving bijection between upper unions and
complements of lower cyclic intervals.  Apply Theorem 2.1. \(\square\)

## 4. Simultaneous telescoping

For two profiles `P,Q` and active labels `x,y`, write

\[
 \mathcal R_{P,Q}(x,y)
   =[P+y]+[Q+x]-[P+x]-[Q+y].                          \tag{4.1}
\]

It satisfies the cocycle identity

\[
 \mathcal R_{P,Q}(x,y)+\mathcal R_{P,Q}(y,z)
                         =\mathcal R_{P,Q}(x,z).       \tag{4.2}
\]

Theorem 2.1 is the sum of one such cocycle on the `Y` rails and one, with
the opposite profile order, on the `X` rails.

### Theorem 4.1 (aligned all-width telescoping)

Suppose a serial family of inverse-pair substitutions has the same ordered
banks `X,Y` and active endpoint sequence

\[
                         z_0,z_1,\ldots,z_s,           \tag{4.3}
\]

so that move `i` has `(a,d)=(z_i,z_(i+1))` after the harmless relabelling
of its two intermediate coordinates.  Then, at every lower length and every
upper width, the total signed current equals the single endpoint current
obtained by replacing `(a,d)` with `(z_0,z_s)` in (2.4).

If `z_s=z_0`, the total signed current is zero simultaneously at every
width.

#### Proof

For each fixed width, both rectangles in (2.4) have fixed profiles and
their active labels follow (4.3).  Apply (4.2) to each rectangle separately.
The endpoint formula follows, and both endpoint rectangles vanish when
`z_s=z_0`. \(\square\)

This proves a genuine all-width zero-current network without requiring a
same-phase native `C6` collar.  Its limitation is equally exact: alignment
keeps the ordered banks `X,Y` fixed.  The theorem does not connect different
bank fibres or prove that the canonical MSW inverse-pair catalogue contains
the required serial chain.

## 5. Same-slot aligned chains are only involutions

The missing serial-chain premise cannot be obtained by repeatedly using one
fixed displayed inverse-pair slot.

For fixed ordered banks `X,Y`, write

\[
 \mathcal P(a,d;b,c)=
 \bigl\{(a,b,X,c,d,Y),\ (b,d,X,a,c,Y)\bigr\}.         \tag{5.1}
\]

Let `T` be the inverse-pair substitution (2.1), with row order forgotten.

### Theorem 5.1 (fixed-slot two-cycle rigidity)

For distinct active labels,

\[
                 \boxed{T\mathcal P(a,d;b,c)
                         =\mathcal P(d,a;b,c).}       \tag{5.2}
\]

Moreover the parameters in (5.1) are uniquely recoverable from the
unordered row pair once the two ordered banks and their four boundary slots
are fixed.  Consequently

\[
                         T^2=1,                       \tag{5.3}
\]

and a same-slot aligned chain can only alternate

\[
                         a\longleftrightarrow d.      \tag{5.4}
\]

It cannot realize an endpoint sequence with three distinct consecutive
labels.

#### Proof

The output rows in (2.1) are

\[
 (b,a,X,d,c,Y),\qquad(d,b,X,c,a,Y).
\]

After exchanging their order, these are exactly

\[
 (d,b,X,c,a,Y),\qquad(b,a,X,d,c,Y),                  \tag{5.5}
\]

which is `mathcal P(d,a;b,c)`.  This proves (5.2), and applying it twice
proves (5.3).

For uniqueness, let `S_0,S_1,S_m,S_(m+1)` be the unordered pairs of labels
occupying the four active positions across the two rows.  From (5.1),

\[
 \begin{aligned}
 S_0&=\{a,b\},&S_1&=\{b,d\},\\
 S_m&=\{c,a\},&S_{m+1}&=\{d,c\}.                    \tag{5.6}
 \end{aligned}
\]

Therefore

\[
 \begin{aligned}
 a&=S_0\cap S_m,& b&=S_0\cap S_1,\\
 c&=S_m\cap S_{m+1},& d&=S_1\cap S_{m+1}.           \tag{5.7}
 \end{aligned}
\]

All four intersections are singletons, proving recovery and the final
claim. \(\square\)

Thus a nontrivial aligned circulation must change the physical slot: it
needs a second inverse-pair representation at another cut whose new
`X,Y` rails are identified with the old rails by a proved transport.  Raw
availability of many disjoint `1100/1010` blocks gives commuting involutions,
not the open endpoint chain required by Theorem 4.1.

## 6. Remaining constructive gate

The native inverse-pair route has now reduced upper protection to a
finite-profile transport problem:

1. use open aligned chains to route immediate-upper holes by their endpoint
   currents;
2. combine chains into closed circulations so every deeper-width current
   cancels; and
3. choose the chains occurrence-disjointly inside one exact root/owner
   factor.

The exact missing theorem is an **aligned inverse-pair circulation
packing across changing slots**, with a proved rail-transport map and
bounded terminal endpoint set.  A positive theorem would
simultaneously settle the former q1 span and arbitrary-width compensation
rows for this move family.  Component joining and the strict-lower compiler
would still require their separate protected interfaces.
