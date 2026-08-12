# Full flag-neutral circuits admit formal block-product suspension

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The genuine `Q_7` cyclic deck circuit can be antisymmetrized to a nonzero
signed row relation whose cyclic-interval load vanishes at every rank.  This
note proves that full-rank cancellation is stable under a natural
block-concatenation product with an arbitrary cyclic context.

Thus a finite full flag-neutral circuit has a formal suspension to every
larger odd dimension obtained by adding an even number of coordinates.  The
suspended object is still a signed multiset of wreath rows, not necessarily
a simple factor trade: internal middle multiplicities remain the exact
integrality gate.

## 1. Occurrence decks

Let `C` be an oriented cyclic order on a coordinate set `X`, `|X|=a`.
For `0<=r<=a`, define its occurrence deck

\[
 \mathcal I_r(C)
 :=\sum_{i\in\mathbb Z_a}{\bf e}_{I_C(i,r)}.
\tag{1.1}
\]

At `r=0,a` the same target occurs `a` times; retaining this multiplicity
makes the product formula uniform.  For every proper nonzero rank the
cyclic intervals are distinct.

A signed row family

\[
                         z=\sum_Cz_C[C]
\tag{1.2}
\]

is **full flag-neutral** if

\[
 \boxed{
             \sum_Cz_C\mathcal I_r(C)=0
             \qquad(0\le r\le a).}
\tag{1.3}
\]

In particular `sum_C z_C=0`, by either endpoint rank.

## 2. The all-cuts block product

Let `R` be an oriented cyclic order on a disjoint coordinate set `Y`,
`|Y|=b`.  For `i in Z_a`, let `C_i` be the linear word obtained by cutting
`C` immediately before its `i`-th coordinate; define `R_j` similarly.
Put

\[
 \boxed{
 C\star R:=\sum_{i\in\mathbb Z_a}
             \sum_{j\in\mathbb Z_b}[C_iR_j],}
\tag{2.1}
\]

where `C_iR_j` is regarded as a cyclic order on `X sqcup Y`.  Repetitions
are retained with multiplicity.  Extend `star R` linearly to signed row
families.

The point of summing over all cuts is that no pointed-boundary information
survives: every interval count depends only on the unpointed cyclic interval
decks of the two factors.

## 3. Exact deck factorization

### Lemma 3.1 (two-block interval factorization)

Fix `0<=s<=a`, `0<=t<=b`, and put `r=s+t`.  There is a nonnegative integer

\[
                         \kappa_{a,b}(s,t)
\tag{3.1}
\]

depending only on the four displayed integers such that, for every
`A subseteq X`, `|A|=s`, and `B subseteq Y`, `|B|=t`,

\[
 \boxed{
 \left\langle{\bf e}_{A\cup B},
       \mathcal I_r(C\star R)\right\rangle
 =\kappa_{a,b}(s,t),
   \left\langle{\bf e}_A,\mathcal I_s(C)\right\rangle
   \left\langle{\bf e}_B,\mathcal I_t(R)\right\rangle.}
\tag{3.2}
\]

#### Proof

In a cyclic word consisting of one contiguous `X` block and one contiguous
`Y` block, a proper cyclic interval crosses each of the two block boundaries
at most once.  Its intersection with either block is therefore empty, the
whole block, a linear prefix, a linear suffix, or the union of a prefix and
a suffix.  After the block is closed cyclically, each of these is a cyclic
interval in the corresponding factor order.  Hence the left side of (3.2)
vanishes unless `A` is an `s`-interval of `C` and `B` is a `t`-interval of
`R`.

Suppose both interval conditions hold.  The cyclic automorphism group of a
fixed factor order acts transitively on its interval occurrences of a fixed
length.  Consequently the number of triples

\[
 (i,j,k): I_{C_iR_j}(k,r)=A\cup B
\]

is independent of the locations and labels of `A` and `B`; it depends only
on `a,b,s,t`.  Call this number `kappa_(a,b)(s,t)`.  At the trivial ranks,
the repeated occurrences in (1.1) absorb the corresponding factor of `a`
or `b`.  This proves (3.2). \(\square\)

The numerical value of `kappa` is immaterial for cancellation.  For
`0<s<a` and `0<t<b`, the two one-seam orientations already show that it is
positive.

For completeness, the full coefficient table is

\[
\boxed{
\begin{array}{c|ccc}
\kappa_{a,b}(s,t)&t=0&0<t<b&t=b\\ \hline
s=0&a+b&b-t+1&1\\
0<s<a&a-s+1&2&s+1\\
s=a&1&t+1&a+b.
\end{array}}
\tag{3.4}
\]

Here the corner values `a+b` use the convention that the empty or full
target has `a+b` occurrences in each product order, while the corresponding
factor targets have `a` and `b` occurrences.  The off-corner endpoint
values count the cuts which do not split the selected interval (or its
complement).  Thus the full/empty block cases introduce no fractional
coefficient and no exception to (3.2).

### Lemma 3.2 (the all-cuts product is injective on row packets)

Assume `a,b>=2` and keep the labelled partition `X dotcup Y`.  If `C,C'`
are distinct cyclic-order packets on `X`, then the supports of `C star R`
and `C' star R` are disjoint.  In particular

\[
                         z\ne0\quad\Longrightarrow\quad z\star R\ne0.
\tag{3.5}
\]

#### Proof

Every product order has exactly two cross edges between the labelled blocks
`X` and `Y`.  Deleting those cross edges and restricting to `X` recovers
the cyclic order `C`, up to rotation and reversal.  Therefore the same
product wreath packet cannot arise from a distinct base wreath packet
`C'`.  Linear combinations supported on distinct base packets cannot
cancel under `star R`. \(\square\)

### Theorem 3.2 (formal suspension)

If `z` is full flag-neutral on `X`, then `z star R` is full flag-neutral on
`X sqcup Y`:

\[
 \boxed{
       \sum_Cz_C\mathcal I_r(C\star R)=0
       \qquad(0\le r\le a+b).}
\tag{3.3}
\]

#### Proof

Fix `S subseteq X sqcup Y`, write `A=S cap X`, `B=S cap Y`, and put
`s=|A|`, `t=|B|`.  Lemma 3.1 gives

\[
\begin{aligned}
 \left\langle{\bf e}_S,
   \sum_Cz_C\mathcal I_{s+t}(C\star R)\right\rangle
 &=\kappa_{a,b}(s,t)
   \left\langle{\bf e}_B,\mathcal I_t(R)\right\rangle
   \left\langle{\bf e}_A,
      \sum_Cz_C\mathcal I_s(C)\right\rangle\\
 &=0
\end{aligned}
\]

by (1.3).  This holds for every target `S`, proving (3.3). \(\square\)

## 4. Application to the `Q_7` circuit

Let `z` be the signed three-row deck circuit from Theorem 17.1 of
`MATH_THEOREM_PRIME_CYCLE_ROW_POWER_RIGIDITY_20260725.md`, and let `tau`
advance one step around its first-shadow six-cycle while fixing the seventh
coordinate.  The audited antisymmetrization

\[
                         y=z+\tau z
\tag{4.1}
\]

is nonzero and satisfies

\[
                         \mathcal I_r(y)=0
                         \qquad(0\le r\le7).
\tag{4.2}

For any cyclic context `R` on `2s` new coordinates, Theorem 3.2 therefore
gives a nonzero formal interval-deck relation on `7+2s` coordinates:

\[
 \boxed{
                         \mathcal I_r(y\star R)=0
                         \qquad(0\le r\le7+2s).}
\tag{4.3}
\]

This is an all-dimensional algebraic suspension of the finite seed.  It is
stronger than middle neutrality: every lower and upper interval ledger
cancels exactly.

## 5. The remaining simple-trade gate

The two signs of `y` are not middle-disjoint.  Each six-row sign has middle
histogram

\[
                         0^5,1^{18},2^{12}.
\tag{5.1}
\]

The block product preserves the signed identity but does not automatically
turn either sign into a matching.  The next theorem needed from this route
is therefore a **simple disjointization theorem**:

> Choose a sufficiently rich family of even contexts and decompose the
> positive and negative block-product multisets into paired simple wreath
> matchings, losing only `o(W)` middle targets.

Because (4.3) has already removed every shadow equation, this gate concerns
only internal middle multiplicities.  A solution would give scalable legal
factor circuits without any additional multidepth balancing loss.

## 6. Single-context disjointization is forced into two-row trades

The exact coefficient table exposes a strong congestion phenomenon.  Put

\[
                         a=7,qquad b=2s,qquad
                         M={a+b-1\over2}=s+3,
\]

and assume `s>=4`.  Let `T subseteq Y` be any length-`M` interval of the
context row `R`.  In the middle-rank target `T`, the base part is empty.
Formula (3.2) and the table (3.4) give, on either sign of `y star R`,

\[
\begin{aligned}
 \mu_M(T)
 &=\kappa_{7,2s}(0,M)
   \sum_{C\text{ on that sign}}
       \langle{\bf e}_\varnothing,\mathcal I_0(C)\rangle\\
 &=(2s-M+1)\,(6\cdot7)\\
 &=\boxed{42(s-2)}.
\end{aligned}
\tag{6.1}

Thus any edge-colouring of one sign into middle packings needs at least

\[
                         42(s-2)
\tag{6.2}

colours.

There are

\[
                         6ab=84s
\tag{6.3}

row occurrences on each sign.  Moreover a nonzero paired simple trade
cannot have one row on each side: equality of the two middle packets would,
by Lemma 7.2 of the prime-cycle note, make the two wreath rows identical and
cancel them.

### Proposition 6.1 (two-row concentration)

Suppose the complete positive and negative block-product multisets are
decomposed into `T` nonzero paired simple wreath trades.  If their row sizes
are `k_1,...,k_T` on either sign, then

\[
                         42(s-2)\le T\le42s,
\tag{6.4}
\]

and

\[
 \boxed{
                         \sum_{j=1}^T(k_j-2)le168.}
\tag{6.5}

In particular all but at most `168` of the pieces are two-row-for-two-row
trades.

#### Proof

The lower bound in (6.4) is (6.2).  Every nonzero piece has `k_j>=2`, while
their total row mass is `sum_jk_j=84s`; this gives `T<=42s`.  Finally

\[
 \sum_j(k_j-2)=84s-2T
 \le84s-84(s-2)=168.
\]

Every piece with more than two rows contributes at least one to the left
side, proving the last assertion. \(\square\)

Therefore a single fixed context cannot be disjointized by a soft generic
colouring alone.  An exact decomposition would have to manufacture
`42s-O(1)` genuine two-row wreath trades.  The alternatives are:

1. prove an abundant two-row trade theorem for these block products; or
2. mix many context rows before colouring, so that pure-context middle
   targets no longer impose the one-context congestion (6.1).

This does not rule out the block-product route, but it identifies the exact
reason a sufficiently rich context **family**, rather than one symmetric
context, is required.

### Proposition 6.2 (same-context packings have at most two rows)

Assume `s>=7`.  Any middle packing chosen from product rows

\[
                         C_iR_j
\]

using one fixed context order `R` contains at most two rows, independently
of the base rows `C` and their cuts `i`.

#### Proof

Let `B` be a context interval of length `M=s+3`.  In the product order,
`B` remains a contiguous middle interval exactly when the context cut `j`
does not lie in one of the `M-1` internal gaps of `B`.  Its allowed cut set
is therefore a cyclic interval of

\[
                         2s-(M-1)=s-2
\tag{6.6}
\]

consecutive context gaps.

Two product rows with context cuts `j,j'` share some context-only middle
target precisely when the two cuts lie in one such interval.  To avoid a
collision, their shorter cyclic gap distance must consequently be at least
`s-2`.

If three cuts were pairwise collision-free, the three successive arc gaps
between them around the `2s`-cycle would each be at least `s-2`.  Their sum
would be at least `3s-6>2s` for `s>=7`, a contradiction. \(\square\)

This makes the concentration conclusion structural: for a single context,
large simple pieces do not exist at all.  Every viable disjointization is
forced into two-row pieces before any positive/negative matching condition
is imposed.

## 7. Exponentially many band-disjoint contexts exist

Although one context is congested, there is no global context-catalogue
shortage.  Let `b=2s` and consider the eight ranks

\[
                         \mathcal J_s=\{s-4,s-3,\ldots,s+3\}.
\tag{7.1}
\]

These are exactly the possible context intersection sizes of a middle
target in a `7+2s` block product.

### Theorem 7.1 (band-disjoint context family)

For all sufficiently large `s`, there is a family `mathcal R_s` of oriented
cyclic orders on the same `2s` coordinates such that no two distinct orders
share a cyclic interval at any rank in `mathcal J_s`, and

\[
 \boxed{
                         |\mathcal R_s|
                         =\Omega\left({2^{2s}\over s^{5/2}}\right).}
\tag{7.2}
\]

#### Proof

There are `(2s-1)!` oriented cyclic orders modulo rotation.  A fixed
`v`-set is a cyclic interval in the fraction

\[
                         {2s\over\binom{2s}{v}}
\tag{7.3}
\]

of them.  A fixed cyclic order contains `2s` rank-`v` intervals.  Hence the
fraction of all context orders sharing some rank-`v` interval with it is at
most

\[
                         {(2s)^2\over\binom{2s}{v}}.
\tag{7.4}
\]

Summing over the eight ranks in (7.1), the conflict fraction is

\[
 O\left({s^{5/2}\over2^{2s}}\right),
\tag{7.5}
\]

by the central-binomial estimate, uniformly across a fixed-width central
band.  The conflict graph on all context orders therefore has maximum
degree at most this fraction times its number of vertices.  Greedy
independent-set selection gives (7.2). \(\square\)

### Corollary 7.2 (the formal catalogue has the correct global scale)

For every `R in mathcal R_s`, one sign of `y star R` contains

\[
                         6\cdot7\cdot2s=84s
\tag{7.6}
\]

row occurrences.  Therefore the full band-disjoint context catalogue has
row mass

\[
 \boxed{
 \Omega\left({2^{2s}\over s^{3/2}}\right),}
\tag{7.7}
\]

which is the same order as the number

\[
 {1\over2s+7}\binom{2s+7}{s+3}
 =\Theta\left({2^{2s}\over s^{3/2}}\right)
\tag{7.8}
\]

of wreath rows in an exact factor on `2s+7` coordinates.

Moreover, product rows using distinct contexts in `mathcal R_s` cannot
share a middle target: equality of a product middle target would force its
context part to be a common interval at one of the ranks (7.1).

Thus the formal suspension is neither exponentially too small nor forced to
collide across different contexts.  The remaining problem is local to one
context: resolve its all-cuts product into the two-row simple trades forced
by Proposition 6.2, and pair the positive and negative resolutions with
equal middle unions.  A successful uniform two-row resolution could then be
placed over the band-disjoint family at exactly the ambient factor scale.

## 8. Balanced shuffles remove the single-context congestion

The two-row obstruction in Section 6 is a feature of the **contiguous**
two-block skeleton.  There is another exact suspension operator in which the
seven seed coordinates are spread around the context cycle.  For that
operator the old three-row circuit itself lifts to a genuine simple middle
trade.

Let `a=7`, `b=2s`, `N=a+b`, and let `omega` be a cyclic binary word of
length `N` with seven `X`-slots and `b` `Y`-slots.  If `C` is a cyclic order
on `X`, `R` a cyclic order on `Y`, and `i in Z_7`, `j in Z_b`, write

\[
                    \operatorname{Sh}_{\omega}(C_i,R_j)
\tag{8.1}
\]

for the cyclic order obtained by reading `omega` and filling its `X`-slots,
in order, from the cut `C_i`, and its `Y`-slots, in order, from the cut
`R_j`.  For a fixed context phase `j`, define the one-sided phase lift

\[
 \boxed{
 L_{\omega,R,j}(C)
   :=\sum_{i\in\mathbb Z_7}
       [\operatorname{Sh}_{\omega}(C_i,R_j)].}
\tag{8.2}
\]

### Lemma 8.1 (one-sided shuffle factorization)

Fix `A subseteq X`, `B subseteq Y`, with `|A|=u`, `|B|=v`, and put
`r=u+v`.  There is a nonnegative integer

\[
                         \lambda_{\omega,R,j,r,u}(B)
\tag{8.3}
\]

independent of the seed row `C` and of the location of the interval `A` in
`C`, such that

\[
 \boxed{
 \left\langle {\bf e}_{A\cup B},
       \mathcal I_r(L_{\omega,R,j}(C))\right\rangle
 =\lambda_{\omega,R,j,r,u}(B)
   \left\langle {\bf e}_A,\mathcal I_u(C)\right\rangle .}
\tag{8.4}
\]

Consequently every full flag-neutral signed seed `v` has a full
flag-neutral one-sided shuffle lift:

\[
                         B_rL_{\omega,R,j}(v)=0
                         \qquad(0\le r\le N).
\tag{8.5}
\]

#### Proof

Fix a start position `h` in the shuffle skeleton.  The length-`r` skeleton
window beginning at `h` contains some `u_h` consecutive `X`-slots and
`v_h=r-u_h` consecutive `Y`-slots.  Hence the corresponding coordinate
target is the union of a cyclic `u_h`-interval of `C` and a cyclic
`v_h`-interval of `R`.

Assume `u_h=u`.  As the base phase `i` runs through `Z_7`, the start of the
base interval runs once through every cyclic start of `C`.  Thus the number
of phases producing the prescribed base target `A` is exactly

\[
                         \langle {\bf e}_A,\mathcal I_u(C)\rangle,
\]

including the retained multiplicities at `u=0,7`.  Whether the context part
equals `B` depends only on `omega,R,j,h`.  Summing over the skeleton starts
`h` gives (8.4).  Applying (8.4) target by target and using
`\mathcal I_u(v)=0` for every `u` proves (8.5). \(\square\)

The middle-rank packing statement needs two elementary properties of the
skeleton.  Put

\[
                         M={N-1\over2}=s+3.
\tag{8.6}
\]

For a length-`M` skeleton window starting at `h`, let `k_h` be its number of
`X`-slots and let `beta_h in Z_b` be the index, in the fixed context phase,
of its first `Y`-slot.  Call `omega` **separating half-balanced** when

\[
 k_h\in\{3,4\}\quad\text{for every }h,
 \qquad
 h\longmapsto(k_h,\beta_h)\quad\text{is injective}.
\tag{8.7}
\]

### Lemma 8.2 (separating half-balanced skeletons exist)

For every sufficiently large `s` there is a separating half-balanced
skeleton with seven `X`-slots and `2s` `Y`-slots.

#### Proof

Use the cyclic mechanical word

\[
 x_h=\left\lfloor{7(h+1)\over N}+\theta\right\rfloor
     -\left\lfloor{7h\over N}+\theta\right\rfloor,
 \qquad h\in\mathbb Z_N,
\tag{8.8a}
\]

with a generic intercept `theta`, and declare the positions with `x_h=1`
to be the `X`-slots.  The sum telescopes to seven.  The same telescoping
calculation on an interval of length `L` shows that its number of marked
slots is either the floor or the ceiling of `7L/N`.  Since

\[
                         3<{7M\over N}<4,
\]

every half-window contains three or four `X`-slots.

Equivalently the marked positions are Beatty roundings of seven equally
spaced points.  Their cyclic gaps are the floor or the ceiling of `N/7`,
so for large `s` the marks are isolated.  A difference between the `r`-th
and `(r+d)`-th marks differs by less than one from `dN/7`.  Only `d=3,4`
could equal `M`; but

\[
 M-{3N\over7}={N-7\over14}={s\over7},
 \qquad
 {4N\over7}-M={N+7\over14}={s+7\over7}.
\tag{8.8b}
\]

These quantities exceed the rounding error for all sufficiently large
`s`.  Hence no two marked positions are at cyclic difference `M`.

It remains to verify injectivity.  Two starts with the same first context
index are equal unless one begins at the isolated `X` immediately preceding
the other, which begins at the following `Y`.  Moving between those two
starts deletes that `X`; the `X`-count could remain unchanged only if the
new terminal slot, at cyclic displacement `M`, were another `X`.  This was
excluded.  Hence the two starts have different `k_h`, proving (8.7).
\(\square\)

Let

\[
 z=(\sigma^2D+\sigma A+\sigma B)-(D+A+B)
\tag{8.8}
\]

be the genuine three-row `Q_7` trade of Theorem 17.1 in the prime-cycle
note.  Both three-row signs are middle packings.  Their length-four packets
are also packings, since on seven coordinates complementation bijects
length-three and length-four intervals.

### Theorem 8.3 (genuine balanced-shuffle suspension of the `Q_7` trade)

Let `omega` be separating half-balanced and fix any context row `R` and
context phase `j`.  Then

\[
 \boxed{
                         L_{\omega,R,j}(z)}
\tag{8.9}
\]

is a genuine simple `21`-row-for-`21`-row middle wreath trade on
`7+2s` coordinates.  In particular, each sign is a middle packing and the
two signs cover exactly the same `21N` middle targets.

Its signed interval action can occur only on targets whose intersection
with the seven seed coordinates has size two or five.

#### Proof

By (8.7), every middle window of every shuffled row has a seed part of size
three or four.  Lemma 8.1 and the identities

\[
                         B_3z=B_4z=0
\]

therefore show that the two signs of (8.9) have equal middle occurrence
decks.

We prove that one sign is a packing; the other is identical.  Suppose two
of its product rows share a middle target.  The two context parts have the
same proper size and are cyclic intervals of `R`.  Hence they have the same
context start.  Injectivity in (8.7) forces the same skeleton start `h` and
the same seed size `k_h`.

The two seed parts are consequently equal length-`k_h` intervals in two of
the three seed rows on that sign.  At ranks three and four those three seed
packets are pairwise disjoint, so the seed rows agree.  Distinct base phases
of the same row give distinct proper cyclic intervals, so the phases agree
as well.  The two product rows were therefore identical.  Thus each sign is
a packing.  It has three seed rows times seven base phases, hence `21` rows,
and each row has `N` middle targets.

Finally the seed relation `z` is neutral at seed ranks
`0,1,3,4,6,7`; its only possibly nonzero interval decks are at ranks two
and five.  Formula (8.4) therefore confines every lifted signed target to
seed intersection size two or five. \(\square\)

The evenly spaced skeleton gives substantially more than middle
neutrality.

### Corollary 8.4 (an exact linear-depth band-invisible trade)

Take the balanced mechanical skeleton in Lemma 8.2.  Then

\[
 \boxed{
 B_rL_{\omega,R,j}(z)=0
 \qquad\left({3N\over7}<r<{4N\over7}\right).}
\tag{8.10}
\]

In particular, writing `M=(N-1)/2`, the genuine middle trade of Theorem
8.3 preserves every interval rank

\[
                         M-H,\ldots,M+H
\tag{8.11}
\]

for every integer `H<s/7`.

#### Proof

Every cyclic length-`r` interval of the balanced mechanical skeleton has
either

\[
                         \left\lfloor{7r\over N}\right\rfloor
 \quad\text{or}\quad
                         \left\lceil{7r\over N}\right\rceil
\]

seed slots.  In the range displayed in (8.10), these two values are three
and four.  Since `B_3z=B_4z=0`, Lemma 8.1 gives (8.10).

Finally

\[
 M-{3N\over7}={N-7\over14}={s\over7},
 \qquad
 {4N\over7}-M={N+7\over14}={s+7\over7},
\]

so (8.11) follows whenever `H<s/7`. \(\square\)

### Consequence

The finite circuit now has a genuine simple suspension in every large odd
dimension; the obstruction is no longer middle positivity for one lifted
copy.  The balanced version is in fact exactly invisible on a central band
of linear depth, far deeper than the `sqrt(N) omega(1)` band required by the
constant-one transfer.

What is still missing for constant one is a width-scale **extendible
packing** of these `21`-row trades (or a construction of a good factor on
which they act).  Outside the balanced regime, the same lift supplies
rank-two/rank-five seed directions which may be used for defect correction;
inside it, Corollary 8.4 supplies a genuinely band-preserving absorber.
This is a more flexible gate than the `42s-O(1)` two-row decomposition
forced by the contiguous-block product: balanced shuffling eliminates the
pure-context middle targets responsible for that congestion.

## 9. Uneven half-balanced shuffles transport the six-cycle only locally

Theorem 8.3 does not require the mechanical discrepancy condition away
from the middle rank.  Keep only the middle assumptions (8.7), and let

\[
                         r_q=M-q\qquad(q\ge1).
\tag{9.1}
\]

For a skeleton start `h`, write

\[
 k_h=|X\cap[h,h+M)|,
 \qquad
 d_{h,q}=|X\cap[h+M-q,h+M)|.
\tag{9.2}
\]

Thus the shortened window has exactly `k_h-d_{h,q}` seed slots.  Let
`beta_{h,q}` be the start, in context coordinates, of its context part.
Write

\[
 \Delta=B_2z
 =({\bf e}_{02}+{\bf e}_{14}+{\bf e}_{56})
  -({\bf e}_{01}+{\bf e}_{25}+{\bf e}_{46}).
\tag{9.3}
\]

### Theorem 9.1 (exact lower action formula)

For every half-balanced separating skeleton,

\[
 \boxed{
 B_{M-q}L_{\omega,R,j}(z)
 =\sum_{\substack{h\in\mathbb Z_N\\
                   k_h-d_{h,q}=2}}
     \Delta\otimes
     {\bf e}_{I_R(\,j+\beta_{h,q},\,M-q-2\,)}.}
\tag{9.4}
\]

Here the tensor notation means that the pair coordinate in `X` is united
with the displayed context interval in `Y`.  Repeated global targets are
added with their signed multiplicities.

Moreover

\[
 \boxed{
 \#\{h:k_h-d_{h,q}=2\}\le7q,}
\tag{9.5}
\]

and consequently

\[
 \boxed{
 \bigl|\operatorname{supp} B_{M-q}L_{\omega,R,j}(z)\bigr|\le42q,
 \qquad
 \left|B_{M-q}L_{\omega,R,j}(z)\right|_1\le42q.}
\tag{9.6}
\]

#### Proof

At the lower rank `M-q`, a skeleton window has at most four seed slots.
The seed relation `z` is neutral at seed sizes zero, one, three, and four;
its only possible contribution is therefore at seed size two.  Applying
the one-sided factorization proof start by start gives exactly (9.4).

Every start counted in (9.5) has `d_{h,q}>=1`.  Double-counting incidences
between starts and seed marks in the deleted terminal arcs gives

\[
                         \sum_{h\in\mathbb Z_N}d_{h,q}=7q,
\tag{9.7}
\]

because each of the seven seed marks belongs to exactly `q` such arcs.
Hence the number of starts with positive `d_{h,q}` is at most `7q`, proving
(9.5).  The vector `Delta` has six nonzero unit coordinates, so the triangle
inequality gives (9.6). \(\square\)

There is a precise crossing-depth description.  For a fixed start `h`,
list the backward distances from the terminal boundary `h+M` to the seed
marks inside its middle window as

\[
                         1\le a_1(h)<\cdots<a_{k_h}(h)\le M.
\tag{9.8}
\]

Then this start contributes to (9.4) exactly on the following interval of
depths:

\[
 \boxed{
 \begin{array}{ll}
 k_h=3:&a_1(h)\le q<a_2(h),\\[1mm]
 k_h=4:&a_2(h)\le q<a_3(h).
 \end{array}}
\tag{9.9}
\]

Thus a three-seed half-window begins transporting the six-cycle at its
first `3 to 2` crossing, while a four-seed half-window begins only after its
second deleted seed mark.

The upper side is dual.  If

\[
 e_{h,q}=|X\cap[h+M,h+M+q)|,
\tag{9.10}
\]

then `B_(M+q)L(z)` is a sum of context-weighted copies of `B_5z`, indexed
by the starts satisfying `k_h+e_{h,q}=5`.  Again

\[
 \#\{h:k_h+e_{h,q}=5\}\le7q,
 \qquad
 |B_{M+q}L(z)|_1\le42q.
\tag{9.11}
\]

### Proposition 9.2 (separation forces exact first-shadow neutrality)

If the skeleton is separating half-balanced, then

\[
 \boxed{
 B_{M-1}L_{\omega,R,j}(z)=0,
 \qquad
 B_{M+1}L_{\omega,R,j}(z)=0.}
\tag{9.12}
\]

#### Proof

Consider a seed mark `t` as the terminal position of a middle window.  The
length-`M` window ending at `t` contains either three or four seed marks.
It produces a lower `3 to 2` crossing after one deletion exactly when it
contains three.

For every unordered pair of seed marks, exactly one cyclic orientation has
backward distance at most `M`, since `N=2M+1`.  A pair at distance exactly
`M` is not counted inside either of the two length-`M` windows ending at its
members (the initial endpoint is just outside).  Therefore, if `p` is the
number of unordered seed pairs at cyclic distance `M`, then the sum, over
the seven terminal seed marks, of the numbers of *other* seed marks in the
corresponding windows is `21-p`.

Each summand is two or three.  Hence exactly `p` of them equal two.  In
other words, the number of lower first-depth acting starts is exactly the
number of seed pairs at distance `M`.

But such a pair contradicts separation.  If `u` and `u+M` are both seed
marks, compare the skeleton starts `u` and `u+1`.  They have the same first
context slot: the first start merely begins one position earlier inside the
same run of seed slots.  Moving the start deletes the mark at `u` and adds
the mark at `u+M`, so their seed counts are equal.  Thus they have the same
pair `(k_h,beta_h)`, contrary to (8.7).  Therefore `p=0`, and the lower
identity in (9.12) follows from (9.4).

For the upper identity, if adding the slot at `h+M` changed a four-seed
middle window to five seed slots, half-balance of the next middle window
would force the deleted initial slot `h` also to be a seed mark.  Again the
two marks are at distance `M`, which was just excluded. \(\square\)

### Corollary 9.3 (all-phase capacity ceiling)

Summing the lift over all `2s` context phases uses `42s` rows on either
sign and satisfies

\[
 \boxed{
 \left|
 B_{M-q}\sum_{j\in\mathbb Z_{2s}}L_{\omega,R,j}(z)
 \right|_1
 \le84sq.}
\tag{9.13}
\]

At the first shadow the left side is in fact zero by Proposition 9.2.
Therefore a separating balanced-shuffle suspension cannot repair any
first-shadow defect at all.  At depth `q` its capacity is at most `O(q)` per
fixed-phase `21`-row trade.  These lifts are naturally band-preserving
absorbers or local corrections below the first shadow; the bulk
near-rainbow construction, and in particular depth one, must come from
another mechanism or from a weaker packing condition than (8.7).

#### Proof

Sum (9.6) over the `2s` phases.  The row count is
`21(2s)=42s` on either sign. \(\square\)

## 10. The exact two-rank context-packing problem

The balanced shuffle uses only context intervals of sizes `s` and `s-1`
at the middle rank.  Thus the eight-rank disjointness imposed in Section 7
is stronger than necessary.  The sharp context problem has a useful folded
Johnson formulation.

Put `Y=[2s]` and let

\[
 \mathcal P_s=
 \left\{\{A,Y\setminus A\}:A\in\binom Ys\right\}
\tag{10.1}
\]

be the set of complementary middle pairs.  A cyclic context order `R`
defines

\[
 E_s(R)=
 \left\{
   \{I_R(j,s),I_R(j+s,s)\}:j\in\mathbb Z_s
 \right\}\subseteq\mathcal P_s
\tag{10.2}
\]

and the lower-colour packet

\[
                         L_{s-1}(R)=mathcal I_{s-1}(R).
\tag{10.3}
\]

Thus `|E_s(R)|=s` and `|L_(s-1)(R)|=2s`.  A family of context orders is
pairwise interval-disjoint at ranks `s,s-1` exactly when its `E_s(R)` are a
matching in `mathcal P_s` and its lower-colour packets are pairwise
disjoint.

### Proposition 10.1 (exact core degrees)

In the multihypergraph on `mathcal P_s` whose edges are the `E_s(R)`, count
oriented cyclic orders modulo rotation.  Every vertex has degree

\[
                         D=s!^2.
\tag{10.4}
\]

If two distinct complementary pairs have representatives `A,B` with
`|A\setminus B|=d`, `1<=d<=s-1`, then their codegree is

\[
                         2d!^2(s-d)!^2,
\tag{10.5}
\]

and hence

\[
 \boxed{
 {\operatorname{codeg}(A,B)\over D}
 ={2\over\binom sd^2}\le {2\over s^2}.}
\tag{10.6}

For a lower colour `T in binom(Y,s-1)`, its degree is

\[
                         D_-=(s-1)!(s+1)!.
\tag{10.7}

If `T subset A`, the cross-codegree of the complementary pair
`{A,A^c}` and `T` is

\[
 \boxed{
                         {2D\over s}.}
\tag{10.8}

#### Proof

A fixed `s`-set is a cyclic interval in

\[
                         {(2s)!\over\binom{2s}s}=s!^2
\]

oriented cyclic orders modulo rotation, proving (10.4).  Once `A` occupies
one half of the coordinate cycle, a second half-window `B` with
`|A\setminus B|=d` can meet it in either cyclic direction.  In either
direction the four successive difference blocks have sizes

\[
                         d,\ s-d,\ d,\ s-d.
\]

Their internal orders are arbitrary, giving (10.5).

The same interval count at rank `s-1` gives (10.7).  Finally, conditioned
on `A` being a half-window, `T=A\setminus\{x\}` is an `(s-1)`-window exactly
when `x` is one of the two endpoints of the internally uniform order of
`A`.  This has probability `2/s`, proving (10.8). \(\square\)

The ratio `2/s^2` is favorable: after complementary pairs are collapsed,
the core edge size is `s`, so the core codegree contribution is
`s(2/s^2)=o(1)`.  The lower colours are the genuine remaining difficulty:
the nested cross-ratio `2/s` is larger by a factor of `s` and is exactly the
near-rainbow first-shadow correlation.

### Proposition 10.2 (folded Johnson cycle equivalence)

Let `A_j=I_R(j,s)` and `P_j={A_j,A_(j+s)}`.  Then

\[
                         P_0P_1\cdots P_{s-1}P_0
\tag{10.9}
\]

is a simple `s`-cycle in the folded Johnson graph on complementary
`s`-pairs.  Its edge `P_jP_(j+1)` carries exactly the two lower colours

\[
                         I_R(j+1,s-1),
 \qquad                 I_R(j+s+1,s-1).
\tag{10.10}

Conversely, a lifted cycle of this form recovers the cyclic context order
up to dihedral symmetry.

Hence a sharp context catalogue is precisely a lower-rainbow packing of
these special `s`-cycles which covers almost all folded Johnson vertices.

#### Proof

Successive half-windows exchange one coordinate, so their complementary
pairs are adjacent in the folded Johnson graph.  The pairs are distinct
for `j mod s`, and `P_s=P_0`, giving a simple cycle.  Intersecting the two
successive representatives in each of the two opposite halves gives
(10.10).  Reading the leaving coordinates around a lifted cycle recovers
`R`, exactly as in the middle-packet reconstruction lemma. \(\square\)

The counting upper bound for such a catalogue is

\[
 K\le
 \min\left\{{\binom{2s}s/2\over s},
             {\binom{2s}{s-1}\over2s}\right\}
 ={1\over2(s+1)}\binom{2s}s
 =\Theta\left({4^s\over s^{3/2}}\right).
\tag{10.11}

This is exactly the ambient factor-row scale.  The elementary greedy family
from Section 7 has only `Theta(4^s/s^(5/2))` members, a factor `s` below
(10.11).  For packing a positive density of the `21`-row seed trades, the
needed context theorem is the weaker constant-density statement:

> Construct a lower-rainbow packing of the special folded-Johnson
> `s`-cycles with `Omega(binomial(2s,s)/s)` cycles.

Reaching `(1-o(1)) binom(2s,s)/(2(s+1))` would be asymptotically sharp, but
is not required for the absorber application.

The core matching has relative codegree `O(s^-2)`; only the attached lower
colours retain the `O(s^-1)` correlation.  Thus this is not an ordinary
large-uniformity matching problem but a cyclic first-shadow design problem.

For absorber accounting, one fixed seed set and the greedy catalogue give
only `Theta(B_N/s)` disjoint fixed-phase trades, where

\[
                         B_N={1\over N}\binom NM.
\tag{10.12}

This is insufficient even for a `B_N/sqrt(s)` residual.  Reaching a
Catalan-scale `Theta(B_N)` correction therefore requires either the sharp
catalogue (10.11), variation of the seven-coordinate seed embedding, or a
sequential re-use mechanism; the present greedy catalogue alone is only a
`B_N/s`-scale absorber.

## 11. General odd-seed balanced-shuffle suspension

The balanced-shuffle argument is not special to seven coordinates.  Let

\[
                         a=2r+1
\]

and let `z` be a simple `t`-row-for-`t`-row middle wreath trade on an
`a`-element seed set.  Thus both signs are rank-`r` packings and
`B_r z=0`; by complementation both signs are also rank-`r+1` packings and
`B_(r+1)z=0`.

Add an even context of size `b`, put `N=a+b`, `M=(N-1)/2`, and choose an
`a`-mark skeleton such that every length-`M` window has `r` or `r+1`
seed slots and the analogue of

\[
                         h\longmapsto(k_h,\beta_h)                \tag{11.1}
\]

is injective.  Define the one-sided lift by summing over all `a` seed
phases, exactly as in (8.2).

### Theorem 11.1 (general simple suspension)

For every fixed context row and phase, the lifted relation is a genuine
simple `(at)`-row-for-`(at)`-row middle wreath trade on `N` coordinates.

#### Proof

Every middle skeleton window sees seed rank `r` or `r+1`, so the two lifted
middle decks agree by the one-sided factorization and
`B_rz=B_(r+1)z=0`.  If two same-sign product rows shared a middle target,
equality of the proper context intervals and injectivity of (11.1) would
force the same skeleton start and seed rank.  The seed parts would then be
equal intervals in two same-sign seed rows.  Packing at ranks `r,r+1`
forces the seed row to agree, and proper-interval injectivity forces the
seed phase to agree.  Thus the product rows were identical.  There are
`t` seed rows and `a` phases on each sign.  \(\square\)

Take now a mechanical balanced skeleton, for which every length-`ell`
window contains floor or ceiling of `a ell/N` seed marks.  Whenever

\[
                         {rN\over a}<\ell<{(r+1)N\over a},        \tag{11.2}
\]

the only seed ranks seen are `r,r+1`; hence

\[
                         \boxed{B_\ell L(z)=0.}                   \tag{11.3}
\]

Since

\[
 M-{rN\over a}={b\over2a},
 \qquad
 {(r+1)N\over a}-M={b\over2a}+1,                                \tag{11.4}
\]

the lift preserves the entire central band `M+-H` for every

\[
                         H<{b\over2a}.                            \tag{11.5}
\]

Finally, separation forces first-shadow neutrality for every odd seed
size.  A lower first-depth action would require a length-`M` window with
`r` marks whose deleted endpoint is a seed mark.  Double-counting oriented
seed pairs shows that such starts are in bijection with seed-mark pairs at
cyclic distance `M`; any such pair produces two starts with the same
`(k_h,beta_h)`, contradicting (11.1).  The upper statement is dual.

Thus every finite simple odd-seed trade has an all-dimensional legal
central-band absorber suspension.  For fixed `a`, however, its depth-`q`
action is supported on at most `a q` skeleton starts.  As in Section 9,
fixed-size seeds cannot provide bulk first-shadow transport under this
clean packing mechanism; their natural role is absorption and sparse
correction.

## 12. Finite warning: the deleted-point owner graph need not be bipartite

One natural attempt starts from the exact MSW factor on `2s+1`
coordinates, fixes a coordinate `z`, and deletes `z` from every row.  For
each row, the `s+1` original middle windows avoiding `z` are disjoint across
the factor and partition all `s`-sets of the remaining coordinates.  The
deleted context row also contains the complements of its `s-1` internal
avoiding-`z` windows.  Join the source row of each internal window to the
MSW owner of its complement.

For the standard `Q_7` factor and `z=0`, direct calculation gives

\[
\begin{array}{c|c}
C_1&\{C_4,C_5\}\\
C_2&\{C_3,C_5\}\\
C_3&\{C_2,C_4\}\\
C_4&\{C_1,C_3\}\\
C_5&\{C_1,C_2\}.
\end{array}
\tag{10.13}
\]

Thus the underlying owner graph is exactly

\[
                         C_1-C_4-C_3-C_2-C_5-C_1.
\tag{10.14}
\]

It is an odd cycle, so a universal Dyck-parity bipartition is false already
at `s=3`.  Its independent-set density is nevertheless `2/5`; a viable
positive-density theorem would have to control the degeneracy or chromatic
number of the owner graph, rather than prove literal bipartiteness.

There is no automatic bounded-degree explanation for this small example.
In general each deleted MSW row owns `s+1` middle windows avoiding `z`, of
which exactly `s-1` are internal and two are endpoints.  Complementation is
a perfect matching on all middle sets of the remaining `2s` coordinates.
Consequently the directed owner multigraph has indegree and outdegree
exactly `s-1` (counting multiplicity).  The degree-two `Q_7` graph is thus
the special value `s-1=2`, not evidence for a dimension-free degree bound.
