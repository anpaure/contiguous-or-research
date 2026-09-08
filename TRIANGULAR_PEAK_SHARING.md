# Triangular peak sharing: an order-optimal construction and a canonical obstruction

## 1. Outcome and theorem ledger

Fix one `c`-diagonal in the four-box upper-tail reduction, and put

\[
                           R=m-c.
\]

The triangular peak-sharing problem has an explicit solution of length

\[
                         \boxed{R(R+1)}.                \tag{1.1}
\]

It uses every nonpeak arm point exactly once.  Its peak occurrences have
quadratic total multiplicity.

This is optimal in order of magnitude, even if arbitrary middle points and
arbitrary, noncanonical witnesses are allowed: one fixed-rank antichain of
targets has size

\[
                         \left\lfloor{(R+1)^2\over4}\right\rfloor, \tag{1.2}
\]

so every word has length `Omega(R^2)`.

There is a sharper obstruction for the exact arm--peak architecture isolated
in `FOUR_BOX_FACTOR_ESCAPE_RESEARCH.md`.  If the target indexed by `(u,r,x)`
must use its canonical two providers `E_(c,r,x)` and `P_(c,u)`, then the
total number of peak occurrences is itself `Omega(R^2)`.  More explicitly,
with `h=ceil(R/2)`, it is at least

\[
 {1\over2}\left(hR-{h(h-1)\over2}\right)
       =\left({3\over16}+o(1)\right)R^2.                \tag{1.3}
\]

Consequently the hoped-for packing

\[
 \text{every arm once}+O(R)\text{ total peak occurrences}        \tag{1.4}
\]

is impossible for canonical two-provider witnesses, irrespective of how
the fan blocks are ordered or interleaved.  This is an order-independent
obstruction to the literal peak-sharing route.

The lower reflection is obtained by one order-reversing involution.  An
upper word and its reflected reverse may be concatenated to cover both
halves in `O(R^2)` occurrences.  Their canonical point alphabets are disjoint
except for one boundary point, so there is no literal occurrence sharing
between upper and lower canonical arms beyond that point.  A noncanonical
three-provider interleaving is not ruled out.

The statements above solve the fixed-`c` triangular problem at the correct
asymptotic scale and close the canonical near-once packing proposal.  They do
not produce a four-box word of width plus `O(m^2)`: summing the forced
quadratic peak multiplicity over all `c` gives a main-order cubic term.

## 2. Exact triangular reduction

For

\[
 0\le u<r\le R,\qquad0\le x<r,
\]

define the peak and arm points

\[
 \begin{split}
 P_u&=P_{c,u}=(c+u,m-c,0,m-u),\\
 E_{r,x}&=E_{c,r,x}=(c+r,m-c-x,x,m-r).
 \end{split}                                             \tag{2.1}
\]

Notice that `E_(r,0)=P_r`; also retain the extra boundary peak `P_0`.
Their join is the target

\[
 Z_{u,r,x}:=E_{r,x}\vee P_u
           =(c+r,m-c,x,m-u).                            \tag{2.2}
\]

These are exactly the upper residual tails in the first orientation, after
putting `u=r-t` in the radius-transfer parametrization.

It is useful to forget the fixed affine coordinates.  Identify `E_(s,y)`
with the triangular lattice cell `(s,y)` and `P_0` with `(0,0)`.  Then

\[
 \mathcal T_R=\{(0,0)\}\cup
       \{(s,y):1\le s\le R,\ 0\le y<s\}.               \tag{2.3}
\]

### Lemma 1 (bounding-rectangle criterion)

An interval of arm/peak points has maximum `Z_(u,r,x)` if and only if its
cells have

\[
                  \min s=u,\quad\max s=r,
                  \quad\min y=0,\quad\max y=x.          \tag{2.4}
\]

Equivalently, all its cells lie in

\[
                  [u,r]\times[0,x]                     \tag{2.5}
\]

and its bounding box is exactly that rectangle.

#### Proof

For a collection of cells `(s,y)`, the four coordinates of the join of the
corresponding points (2.1) are

\[
 c+\max s,\qquad m-c-\min y,
 \qquad\max y,\qquad m-\min s.                         \tag{2.6}
\]

Comparing (2.6) with (2.2) gives (2.4), and (2.5) is an equivalent
restatement.  QED.

In particular, the two canonical providers `E_(r,x)` and `P_u` already have
the required bounding box.  A canonical witness need only keep all
intervening cells inside (2.5).

## 3. Explicit quadratic word

For `1<=r<=R`, define the radius block

\[
 \mathcal F_r=
  (E_{r,r-1},E_{r,r-2},\ldots,E_{r,0},
      P_{r-1},P_{r-2},\ldots,P_0).                     \tag{3.1}
\]

The first half is the radial arm and the second half is the descending peak
spine.  Its length is `2r`.

Concatenate

\[
                         \mathcal W_R^+
      =\mathcal F_1\Vert\mathcal F_2\Vert\cdots\Vert\mathcal F_R. \tag{3.2}
\]

### Theorem 2 (upper triangular construction)

Every target `Z_(u,r,x)` occurs as the maximum of a contiguous interval of
`mathcal W_R^+`.  The word has exact length `R(R+1)`.

#### Proof

Inside `mathcal F_r`, start at `E_(r,x)`.  Continue through

\[
 E_{r,x-1},\ldots,E_{r,0}=P_r,
 P_{r-1},\ldots,P_u.                                  \tag{3.3}
\]

The cells in (3.3) have first coordinates between `u` and `r`, and second
coordinates between `0` and `x`.  They attain all four boundary values:
`E_(r,x)` supplies `r` and `x`, while `P_u` supplies `u` and `0`.
Lemma 1 proves that their maximum is `Z_(u,r,x)`.

Finally,

\[
                  |\mathcal W_R^+|=\sum_{r=1}^R2r=R(R+1). \tag{3.4}
\]

QED.

Every nonpeak point `E_(r,x)` with `x>0` occurs exactly once.  Peak
multiplicities are

\[
 \operatorname{occ}(P_0)=R,
 \qquad
 \operatorname{occ}(P_u)=R-u+1\quad(1\le u\le R).     \tag{3.5}
\]

Thus the total number of peak occurrences is

\[
                  {R^2+3R\over2},                     \tag{3.6}
\]

and the `R(R-1)/2` nonpeak arms account for the rest of (3.4).

## 4. An unrestricted quadratic lower bound

The construction has the correct order even without imposing canonical
providers.

### Theorem 3 (one-rank antichain bound)

Every word whose interval maxima include all `Z_(u,r,x)` has length at least

\[
                         \left\lfloor{(R+1)^2\over4}\right\rfloor. \tag{4.1}
\]

This remains true if entries outside the triangular arm/peak alphabet are
allowed.

#### Proof

The rank excess of (2.2) over the middle is

\[
                         d=r-u+x.                      \tag{4.2}
\]

Take `d=R` and write `a=r-u`.  Then `x=R-a`.  Feasibility is equivalent to

\[
 1\le a\le R,
 \qquad \max(a,R-a+1)\le r\le R.                     \tag{4.3}
\]

For fixed `a`, (4.3) gives

\[
                         \min(a,R-a+1)                 \tag{4.4}
\]

targets.  Therefore the number of depth-`R` targets is

\[
 \sum_{a=1}^R\min(a,R-a+1)
       =\left\lfloor{(R+1)^2\over4}\right\rfloor.     \tag{4.5}
\]

They are distinct points of one rank, hence form an antichain.

For a fixed right endpoint of a word, the maxima of suffixes ending there
form an inclusion chain.  Such a chain contains at most one member of an
equal-rank antichain.  Assign one witnessing interval to every target in
(4.5) and charge it to its right endpoint.  Distinct targets need distinct
endpoints, proving (4.1).  QED.

Thus `Theta(R^2)` total length is unavoidable.  Theorem 3 alone does not
force peak repetitions; that stronger conclusion needs the canonical
two-provider hypothesis below.

### Proposition 3a (a permutation is impossible)

For every `R>=3`, no permutation of `mathcal T_R`--that is, no word
consisting of every triangular cell exactly once and no additional
entries--can cover all target rectangles, even with unrestricted witnesses.
Thus any word confined to this alphabet either repeats a cell or uses more
general entries outside the triangle.

#### Proof

First consider the targets with `x=0`.  Their witnesses contain only peak
cells.  The target `(u,r,x)=(0,R,0)` gives a peak-only interval joining
`P_0` to `P_R`.  For each `s`, the two targets `(0,s,0)` and `(s,R,0)` force
the unique `P_s` to be peak-only connected to both ends.  Hence all

\[
                         P_0,P_1,\ldots,P_R             \tag{4.6}
\]

occupy one contiguous peak-only block.

For each `i`, the target `(i,i+1,0)` can use only `P_i` and `P_(i+1)` as
its two extreme values, and no other peak value may lie between them.  Thus
every consecutive pair `P_i,P_(i+1)` is adjacent inside (4.6).  The block
order is therefore

\[
             P_0,P_1,\ldots,P_R
       \quad\text{or its reverse}.                     \tag{4.7}
\]

Assume the displayed orientation.  Every nonpeak cell lies outside this
block.  An interval containing a nonpeak on the left and any peak necessarily
enters the block through `P_0`, so its minimum first coordinate is zero.  An
interval containing a nonpeak on the right and any peak necessarily enters
through `P_R`, so its maximum first coordinate is `R`.  An interval spanning
both sides has both defects.

But every target with `x>0` needs a nonpeak and a peak.  The interior target

\[
                         (u,r,x)=(1,2,1)                \tag{4.8}
\]

exists when `R>=3` and has neither `u=0` nor `r=R`.  It cannot be represented.
The reversed peak order is symmetric.  QED.

Proposition 3a proves only that the exact-once hope fails.  It gives no
quadratic repetition lower bound; the stronger result in Section 5 uses the
canonical provider pair.

## 5. Canonical peak multiplicity is necessarily quadratic

Call a realization **canonical** when, for every `(u,r,x)`, its chosen
witness contains occurrences of both `P_u` and `E_(r,x)`.  Since their join
already equals the target, the witness may be shortened to the physical
interval between those two occurrences.

For fixed `u`, put

\[
 \mathcal A_u=\{(r,x):u<r\le R,\ 0\le x<r\},          \tag{5.1}
\]

ordered coordinatewise:

\[
                   (r,x)\preceq(s,y)
       \quad\Longleftrightarrow\quad r\le s\text{ and }x\le y. \tag{5.2}
\]

### Lemma 4 (one oriented peak side is one chain)

Fix one physical occurrence of `P_u` and one of its two oriented sides in
the word.  The target types canonically witnessed using that occurrence and
an arm occurrence on that side form a chain in `mathcal A_u`.

#### Proof

Move away from the chosen `P_u` occurrence along the chosen side.  Suppose
the occurrence of `E_(r_1,x_1)` is encountered before that of
`E_(r_2,x_2)`.  The interval from `P_u` to the farther arm contains the
nearer arm.  Since its maximum is `Z_(u,r_2,x_2)`, every entry in it is
coordinatewise below that target.  In particular,

\[
                         E_{r_1,x_1}\le Z_{u,r_2,x_2}.
\]

Comparing the first and third coordinates directly forces

\[
                         r_1\le r_2,
                         \qquad x_1\le x_2.             \tag{5.3}
\]

Thus the types increase coordinatewise with distance.  QED.

### Theorem 5 (canonical peak lower bound)

Let `k_u` be the number of physical occurrences of `P_u`.  Every canonical
realization satisfies

\[
                         2k_u\ge\operatorname{width}(\mathcal A_u). \tag{5.4}
\]

In particular, with `h=ceil(R/2)`,

\[
 \sum_{u=0}^{R-1}k_u
 \ge {1\over2}\sum_{q=1}^{R}\min(q,h)
 ={1\over2}\left(hR-{h(h-1)\over2}\right).            \tag{5.5}
\]

#### Proof

Assign every target type in `mathcal A_u` to the selected occurrence of
`P_u` in its canonical witness and to the side containing its selected arm.
By Lemma 4, the `2k_u` resulting classes are chains.  Any chain cover has at
least `width(mathcal A_u)` members, proving (5.4).

For an explicit antichain in `mathcal A_u`, take

\[
                         r+x=R.                         \tag{5.6}
\]

Here

\[
 r=\max(u+1,\lfloor R/2\rfloor+1),\ldots,R,
\]

so (5.6) has

\[
                         \min(R-u,\lceil R/2\rceil)
                         =\min(R-u,h)                   \tag{5.7}
\]

members.  Increasing `r` strictly decreases `x`, so they are pairwise
incomparable.  Thus

\[
              \operatorname{width}(\mathcal A_u)
                    \ge\min(R-u,h).                    \tag{5.8}
\]

This is in fact equality.  In any antichain, order the `q` members so that

\[
 r_1<r_2<\cdots<r_q.
\]

Incomparability forces `x_1>x_2>...>x_q>=0`, hence `x_1>=q-1` and
`r_1>=q`.  Therefore

\[
 R\ge r_q\ge r_1+q-1\ge2q-1,
\]

so `q<=ceil(R/2)=h`; trivially also `q<=R-u`, the number of available
rows.  Consequently

\[
 \boxed{
   \operatorname{width}(\mathcal A_u)=\min(R-u,h).
 }                                                       \tag{5.8a}
\]

Sum (5.4) and use `q=R-u`.  Finally,

\[
 \sum_{q=1}^R\min(q,h)
 ={h(h+1)\over2}+(R-h)h
 =hR-{h(h-1)\over2}.                                  \tag{5.9}
\]

QED.

Since `h=(1/2+o(1))R`, (5.5) is `(3/16+o(1))R^2`.
The bound allows duplicated arms and arbitrary interleaving: only the
canonical choice of the two providers is used.  Hence duplicating or
reordering the fan arms cannot reduce canonical peak multiplicity to
`O(R)`.

Summed over `c=0,...,m-1`, where `R=m-c`, (5.5) forces

\[
                         \Omega\!\left(\sum_{R=1}^mR^2\right)
                         =\Omega(m^3)                   \tag{5.10}
\]

canonical peak occurrences.  In a middle-row architecture that already
enumerates every middle point once, all but `O(m^2)` of these are repeated
peak occurrences.  Thus canonical two-provider peak sharing cannot yield a
surface-size `O(m^2)` repair.

The last sentence is architecture-scoped.  An unrestricted witness may use
a row-`u` nonpeak to provide `min s=u` and a different peak to provide
`min y=0`; it need not contain `P_u`.  Theorem 5 does not rule out that
three-provider mechanism.

## 6. The lower reflection

Define the pairwise reverse-complement involution

\[
 \vartheta(a,b,d,e)=(m-b,m-a,m-e,m-d).                 \tag{6.1}
\]

It reverses coordinatewise order and exchanges joins with meets.  Directly,

\[
 \begin{split}
 \vartheta(E_{c,r,x})
   &=(c+x,m-c-r,r,m-x),\\
 \vartheta(P_{c,u})
   &=(c,m-c-u,u,m),\\
 \vartheta(Z_{u,r,x})
   &=(c,m-c-r,u,m-x).                                 \tag{6.2}
 \end{split}
\]

As `u` and `x` independently range from `0` to `r-1`, the last line is
exactly the complete lower reflected tail fibre at radius `r` and fixed
`c`.

### Proposition 6 (reflected word)

If `W` covers all upper targets by interval joins, then

\[
                         \vartheta(\operatorname{rev}W) \tag{6.3}
\]

covers all lower reflected targets by interval meets.  Consequently

\[
 W\Vert\vartheta(\operatorname{rev}W)                  \tag{6.4}
\]

covers both families and is invariant under reverse-complement.

#### Proof

Reversal preserves contiguity.  Applying `vartheta` to every term changes
the join of an interval into the meet of its image.  Formula (6.2) identifies
the target family.  Applying reverse-complement twice is the identity, so
(6.4) is self-dual.  QED.

Taking `W=mathcal W_R^+` gives a two-sided word of length `2R(R+1)`.
For each `r`, concatenate the new block `mathcal F_r` and its reflected
reverse, merging their common fixed boundary point `P_(c,0)`.  This saves one
occurrence per radius and gives instead

\[
                         2R^2+R.                       \tag{6.5}
\]

Both bounds are `Theta(R^2)`.

There is almost no literal point sharing between the two alphabets.  If

\[
                         E_{c,r,x}=\vartheta(E_{c,s,y}), \tag{6.6}
\]

then comparison of the first and third coordinates gives `r=y` and `x=s`,
contradicting simultaneously `x<r` and `y<s`.  The only fixed boundary point
is

\[
                         P_{c,0}=\vartheta(P_{c,0}).     \tag{6.7}
\]

The cross equalities are also impossible: a reflected nonzero peak has first
coordinate `c`, whereas an upper arm has first coordinate `c+r>c`, and its
third coordinate rules out equality with an upper peak.  Two peaks can be
equal across the reflection only when both indices are zero.

Thus a literal upper-arm occurrence cannot double as a literal lower-arm
occurrence, except at (6.7).  Intervals from the two halves may still be
globally interleaved, and noncanonical providers may still reduce the total;
neither possibility is excluded here.

## 7. Consequence for the four-box route

For one orientation, summing the explicit upper word (3.4) over all
`c=0,...,m-1` gives

\[
 \sum_{R=1}^{m}R(R+1)
   ={m(m+1)(m+2)\over3}.                               \tag{7.1}
\]

This is already main-order `Theta(m^3)`.  The canonical lower bound (5.10)
shows that no reordering which continues to insist on the provider pair
`E_(c,r,x),P_(c,u)` can reduce the peak part to a surface term.

As a consistency check, summing the two-sided length (6.5) over `c` and then
over the two coordinate-pair orientations gives

\[
 2\sum_{R=1}^{m}(2R^2+R)
   ={m(m+1)(4m+5)\over3}.                              \tag{7.2}
\]

This is exactly the added occurrence count in the audited all-depth
radius-transfer fan theorem.  The cross-radius peak reformulation changes
the providers and exposes the obstruction, but it does not secretly improve
that theorem's leading length.

Therefore the exact next escape must abandon at least one canonical feature:

1. use a nonpeak row-`u` provider and a different peak for the same target;
2. let one interval simultaneously cross and couple several `c`-diagonals;
3. factor below the middle row so the target is not realized by a literal
   middle-point join; or
4. replace the fan geometry by a genuinely four-dimensional growth diagram.

The triangular problem is no longer an unknown source of a subquadratic
packing: `Theta(R^2)` is necessary and sufficient.  What remains open is
whether an unrestricted three-provider or cross-`c` mechanism can absorb
that quadratic local mass into the already necessary global width, rather
than append it as repeated peaks.
