# Global lower-bound structure for universal interval-OR arrays

Let `A=(A_1,...,A_n)` be a nonzero set-valued sequence on `[k]`, and write

\[
U(l,r)=A_l\cup A_{l+1}\cup\cdots\cup A_r.
\]

Assume every nonempty subset of `[k]` occurs as some `U(l,r)`.  For every
target used below, choose one witnessing interval once and for all.

This note records what can, and what cannot, be obtained from Sperner/LYM and
endpoint counting alone.  Its main conclusion is that a width-optimal or
near-width-optimal construction necessarily consists of two transverse,
almost-spanning systems of Boolean flags.  This is a global condition not
visible in the rank-slack inequality.

## 1. Rank-slack is complete for all one-sided chain-capacity arguments

Put

\[
W=\binom{k}{\lfloor k/2\rfloor}.
\]

Fix a rank `r` with `binom(k,r)=W`, suppose `n=W+t`, and select one witness for
every rank-`r` mask.  The usual interval-slack argument implies that every mask
of rank below `r` has a witness of length at most `t`.

### Proposition 1 (all one-endpoint inequalities)

Let `F` be any family of masks of ranks below `r`, and let `h(F)` be the maximum
number of members of `F` in a chain.  Then the witnesses of `F` satisfy

\[
|F|\le qn-\binom q2,
\qquad q=\min\{t,h(F)\}. \tag{1}
\]

In particular, if `F` is the union of any `q<=t` rank layers, then

\[
|F|\le qn-\binom q2. \tag{2}
\]

#### Proof

Assign every chosen witness to its right endpoint.  At endpoint `e`, there are
only `min(t,e)` intervals of length at most `t`.  Their ORs form an inclusion
chain, so at most `h(F)` of them can belong to `F`.  Hence endpoint `e`
contributes at most `min(q,e)`, and

\[
|F|\le\sum_{e=1}^n\min(q,e)=qn-\binom q2.
\]

The same statement follows from left endpoints.  QED.

### Corollary 2 (why this does not improve rank-slack)

None of the inequalities (1), including all LYM/Sperner inequalities applied
separately at one endpoint, strengthens the width bound plus the rank-slack
count.

Indeed, if `q<=t`, Erdos's extension of Sperner gives `|F|<=qW`, while

\[
qn-\binom q2=qW+qt-\binom q2\ge qW.
\]

If `h(F)>=t`, the right side is the total number

\[
tn-\binom t2=tW+\binom{t+1}2
\]

of intervals of length at most `t`, and the rank-slack inequality is exactly
the assertion that this capacity is at least the entire lower ideal.

Thus a stronger lower bound cannot come merely from saying that suffix ORs are
chains, even if one applies the full LYM theorem or arbitrary unions of ranks.
It must couple the two endpoints, or use the union recurrence inside the
interval triangle.

## 2. The multirank endpoint-flag theorem

For a rank `s`, let

\[
m_s=\binom{k}{s},\qquad d_s=n-m_s.
\]

Let `L_s` and `R_s` be respectively the sets of left and right endpoints of the
chosen rank-`s` witnesses.  Equal-rank incomparability implies

\[
|L_s|=|R_s|=m_s.
\]

### Theorem 3 (simultaneous flags)

Let `R` be any collection of ranks and put

\[
D_R=\sum_{s\in R}d_s.
\]

Then:

1. At least `n-D_R` left endpoints carry one selected witness from every rank
   in `R`; the masks at such an endpoint form a strictly nested flag in rank
   order.
2. The same holds at at least `n-D_R` right endpoints.
3. For any fixed `s in R`, at least

   \[
   2n-2D_R-m_s \tag{3}
   \]

   rank-`s` masks lie simultaneously on a full left flag and a full right
   flag through all ranks in `R`.

Negative lower bounds in these statements are, of course, read as zero.

#### Proof

The complement of `L_s` in `[n]` has size `d_s`.  Therefore the union bound
gives

\[
\left|\bigcap_{s\in R}L_s\right|\ge n-D_R.
\]

If witnesses of ranks `a<b` share a left endpoint, their intervals are nested.
The rank-`b` interval cannot be the smaller one, since interval containment
would then imply that its larger mask is contained in the rank-`a` mask.
Hence the rank-`a` interval is contained in the rank-`b` interval, and their
masks are strictly nested.  Consecutive ranks therefore give a saturated
Boolean flag.  This proves the first assertion, and the right-endpoint proof is
identical.

At rank `s`, the left-good masks and right-good masks each have cardinality at
least `n-D_R`.  They are two subsets of a layer of size `m_s`; their
intersection has size at least `2(n-D_R)-m_s`.  QED.

### Corollary 4 (an unbounded crossed central band is necessary)

Suppose `k=2m`, `n=W+e`, and take

\[
R_J=\{m-J,m-J+1,\ldots,m+J\}.
\]

Uniformly for `J=o(sqrt(k))`, the central binomial ratios give

\[
D_{R_J}=O\left(Je+\frac{WJ^3}{k}\right). \tag{4}
\]

Consequently, if `n=(1+epsilon_k)W`, where `epsilon_k->0`, and

\[
J\to\infty,\qquad J=o(k^{1/3}),\qquad J\epsilon_k=o(1),
\]

then all but `o(W)` masks in every rank of `R_J` lie at the crossing of a full
left saturated flag and a full right saturated flag through `R_J`.

For the conjectural value `n=B(k)=W+O(sqrt(k))`, the condition
`J epsilon_k=o(1)` is automatic, so every `J=o(k^(1/3))` is allowed.

#### Proof

For `|j|=o(sqrt(k))`,

\[
W-\binom{k}{m+j}=O\left(\frac{Wj^2}{k}\right).
\]

Thus

\[
d_{m+j}=e+O\left(\frac{Wj^2}{k}\right),
\]

and summing over `|j|<=J` proves (4).  Theorem 3 then applies.  The odd case is
identical after centering the band at the two middle ranks.  QED.

This is a necessary condition on any asymptotically optimal family.  A single
Hamilton ordering of the middle layer is not the full global object: one needs
two transverse near-decompositions into flags across an unbounded number of
central layers.

## 3. Uncrossing and forced Boolean diamonds

The interval triangle has more structure than an abstract poset map.

### Lemma 5 (set-valued uncrossing)

If `a<=b<=c<=d`, then

\[
U(a,c)\cup U(b,d)=U(a,d), \tag{5}
\]

and

\[
U(b,c)\subseteq U(a,c)\cap U(b,d). \tag{6}
\]

In particular, with `rho(l,r)=|U(l,r)|`,

\[
rho(a,d)+rho(b,c)
\le rho(a,c)+rho(b,d). \tag{7}
\]

Thus the rank array of interval ORs is anti-Monge.

The proof is immediate from union of the two crossing position intervals and
from containment of their overlap.

### Corollary 6 (diamond at a crossed flag)

Assume `s-1,s,s+1` belong to `R`, and let a rank-`s` mask `S` be left-good and
right-good in Theorem 3.  Its two rank-`s+1` flag neighbors are distinct sets

\[
S\cup\{x\},\qquad S\cup\{y\},\qquad x\ne y.
\]

Their witness intervals cross, their positional intersection is the selected
witness of `S`, and their hull is an interval whose OR is

\[
S\cup\{x,y\}. \tag{8}
\]

Similarly, the two rank-`s-1` flag neighbors are two distinct one-element
deletions of `S`, and their union is `S`.

#### Proof

Write the selected witness of `S` as `[l,r]`.  Its left-flag upper neighbor is
`[l,r']` with `r'>r`; its right-flag upper neighbor is `[l',r]` with `l'<l`.
They cannot be the same selected mask, because that would force both endpoints
to equal those of `S`.  Since both are one-element extensions of `S`, their
new elements differ.  Equation (5) says that the hull `[l',r']` has OR equal
to their union, proving (8).  The lower statement is dual at the level of the
two selected subsets.  QED.

Hence a near-width solution gives an almost-everywhere Boolean growth diagram:
left flags and right flags cross, and almost every crossing closes to exact
diamonds.  Repeated union shadows in this growth diagram, not missing
one-sided capacity, are the plausible source of any lower bound beyond `B(k)`.

## 4. Coordinate deletion gives a separate moment hierarchy

The following constraint uses the actual array entries rather than only the
chosen witness intervals.

### Lemma 7 (literal filtering)

For `Q subseteq [k]`, delete every entry meeting `Q`.  The remaining sequence is
universal on `[k] setminus Q`.  Consequently, if `|Q|=q`,

\[
\#\{i:A_i\cap Q=\varnothing\}\ge \nu(k-q). \tag{9}
\]

Averaging (9) over all `q`-subsets `Q` gives

\[
\sum_{i=1}^n \binom{k-|A_i|}{q}
\ge \binom{k}{q}\nu(k-q). \tag{10}
\]

#### Proof

A witness for a target disjoint from `Q` contains no entry meeting `Q`.
Deleting all contaminated entries therefore preserves that witness as a
contiguous block in the filtered sequence.  Double-count pairs `(i,Q)` with
`A_i cap Q` empty to obtain (10).  QED.

For example, `q=1` yields

\[
\sum_i |A_i|\le k\bigl(n-\nu(k-1)\bigr). \tag{11}
\]

These moment inequalities do not by themselves beat the middle-layer width,
but they are independent of rank-slack and are natural constraints to combine
with the crossed-flag growth diagram.

## 5. Consequence for the main conjecture

The likely exact formula remains

\[
\nu(k)=B(k),
\]

where `B(k)` is the rank-slack bound.  The results above explain both why this
formula is plausible and why current lower-bound methods stop there:

* rank-slack already captures every one-sided chain/LYM capacity obstruction;
* equality or asymptotic equality forces two transverse, almost-spanning flag
  systems through a growing central band;
* their crossings obey the anti-Monge uncrossing law and force Boolean
  diamonds.

Accordingly, the next mathematical target should not be another refinement of
Sperner counting.  It should be one of the following two statements.

1. **Existence direction:** construct two compatible central flag systems (or
   two suitably orthogonal symmetric-chain decompositions) whose Boolean
   growth diagram can be realized by interval ORs with the rank-slack delay.
2. **Obstruction direction:** prove that the forced diamonds create too many
   repeated outer unions or incompatible inner intersections unless the
   length exceeds `B(k)`.

Either direction attacks information not already exhausted by the rank-slack
calculation.
