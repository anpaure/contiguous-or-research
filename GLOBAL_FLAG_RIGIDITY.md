# Global flag rigidity near the Boolean width

All statements in Sections 1--4 are proved.  Section 5 is explicitly a
research direction, not a theorem.

Let `A=(A_1,...,A_n)` be a sequence of nonempty subsets of `[k]`, and write

\[
U(l,r)=\bigcup_{i=l}^r A_i.
\]

For every mask in every rank under discussion, choose one witnessing interval.
Put

\[
m_s=\binom{k}{s},\qquad d_s=n-m_s.
\]

### Empty-mask convention

This note treats the nonzero problem and writes its optimum as `nu(k)`.  A
nonempty interval has OR zero exactly when every entry in it is zero.  Hence a
solution to the version requiring the empty mask needs a literal zero entry.
Conversely, deleting all zero entries preserves every nonzero witness after
compression, and prepending one zero to a nonzero solution represents the
empty mask.  Therefore

\[
N(k)=\nu(k)+1.
\]

## 0. Exact global normal form: two ordered orthogonal chain decompositions

The following reformulation uses witnesses for **all** nonempty masks, not only
for selected ranks.

### Theorem 0 (endpoint-decomposition theorem)

Choose one witnessing interval

\[
I_S=[\ell_S,r_S]
\]

for every nonempty `S subseteq [k]`.  For `p,q in [n]`, define

\[
\mathcal L_p=\{S:\ell_S=p\},\qquad
\mathcal R_q=\{S:r_S=q\}.
\]

Then:

1. The nonempty Boolean lattice is partitioned by the `n` families
   `mathcal L_p`, and every nonempty `mathcal L_p` is a chain.
2. It is also partitioned by the `n` families `mathcal R_q`, and every
   nonempty `mathcal R_q` is a chain.
3. These two chain decompositions are orthogonal:

   \[
   |\mathcal L_p\cap\mathcal R_q|\le1
   \quad\hbox{for every }p,q. \tag{0.1}
   \]

4. They carry compatible total orders.  Along a left chain, rank and right
   endpoint strictly increase together.  Along a right chain, rank increases
   while left endpoint strictly decreases.  Every occupied pair `(p,q)` lies
   in the triangular region `p<=q`.

#### Proof

Every mask has one chosen left endpoint, so the `mathcal L_p` partition the
masks.  Two intervals with the same left endpoint are nested.  Their OR masks
are therefore comparable, proving that each `mathcal L_p` is a chain.  If the
masks have different ranks, the larger-rank mask must have the larger interval
and hence the larger right endpoint; equal-rank distinct masks cannot share a
left endpoint.  This proves the ordering assertion for left chains.  The
right-chain claims follow identically, with left endpoints decreasing as rank
increases.

If two distinct masks belonged to `mathcal L_p cap mathcal R_q`, both would
have the same selected interval `[p,q]`.  That interval has only one OR value,
a contradiction.  This proves orthogonality.  Finally, `p<=q` because every
witness is a nonempty interval.  QED.

Thus every solution gives a pair of **ordered triangular orthogonal chain
decompositions** of the punctured Boolean lattice.  At `n=W(k)`, these would be
minimum chain decompositions.  Abstract orthogonality is not itself an
obstruction: Shearer and Kleitman constructed two orthogonal symmetric-chain
decompositions of every Boolean cube.  The extra interval conditions are the
orders, triangular support, and the pin-survival condition below.

### Theorem 0B (exact pin-survival completion)

Conversely, suppose one interval `I_S subseteq [n]` has been prescribed for
every nonempty mask `S`, with no two masks assigned the same interval.  For a
coordinate `b`, define its legal positions by

\[
Z_b=[n]\setminus\bigcup_{S:\,b\notin S}I_S. \tag{0.2}
\]

There are entries `A_1,...,A_n` satisfying

\[
\bigcup_{j\in I_S}A_j=S
\quad\hbox{for every nonempty }S \tag{0.3}
\]

if and only if

\[
I_S\cap Z_b\ne\varnothing
\quad\hbox{for every }S\hbox{ and every }b\in S. \tag{0.4}
\]

Empty positions may be deleted afterward; hence this characterizes existence
of a universal nonzero sequence of length at most `n`.

#### Proof

If (0.3) holds, an interval whose target omits `b` contains no occurrence of
`b`.  Every occurrence of `b` is therefore in `Z_b`.  A positive target
containing `b` must contain at least one such occurrence, proving necessity of
(0.4).

Conversely, put `b` in every position of `Z_b` (or in any hitting subset of
`Z_b` meeting all positive intervals).  A negative interval contains no legal
position for `b`, while (0.4) says every positive interval contains one.
Doing this independently for all coordinates gives (0.3).  QED.

Theorems 0 and 0B give an exact global reduction:

\[
\boxed{\text{universal interval-OR array}}
\quad\Longleftrightarrow\quad
\boxed{\text{ordered triangular orthogonal chain pair + pin survival}}.
\]

The known theory of orthogonal symmetric-chain decompositions supplies the
abstract pair of chain partitions.  It does not supply the compatible endpoint
orders or (0.4); those are the genuinely problem-specific steps.

More explicitly, the converse encoded in the box is as follows.  Start with
two chain partitions

\[
\{\mathcal L_1,\ldots,\mathcal L_n\},\qquad
\{\mathcal R_1,\ldots,\mathcal R_n\}
\]

of the **punctured** cube `2^[k] setminus {emptyset}`.  Assume they are
orthogonal.  Every mask `S` then has unique indices `ell_S,r_S`; require
`ell_S<=r_S`, and assign `I_S=[ell_S,r_S]`.  If the pin condition (0.4) holds,
Theorem 0B constructs entries realizing every assigned mask.  Any positions
receiving no coordinate are zero positions.  Delete them and compress every
assigned interval; each nonempty target still contains its positive pins, so
the resulting sequence is a nonzero universal sequence of length at most
`n`.  To solve the full problem, add one literal zero afterward.

## 1. Common endpoints give flags

### Theorem 1 (multirank common-endpoint theorem)

Let `R` be any nonempty set of ranks and set

\[
D_R=\sum_{s\in R}d_s.
\]

Then at least `n-D_R` array positions occur as the left endpoint of a selected
witness in every rank in `R`.  At each such position, those masks form a
strictly nested flag in increasing rank order.  The same result holds for
right endpoints.

#### Proof

Fix a rank `s`.  No two selected rank-`s` intervals have the same left
endpoint.  If they did, the intervals would be nested, so their OR masks would
be comparable; distinct masks of equal cardinality are incomparable.  Thus
the set `L_s` of selected left endpoints has size `m_s`, and its complement in
`[n]` has size `d_s`.  Therefore

\[
\left|\bigcap_{s\in R}L_s\right|
\ge n-\sum_{s\in R}|[n]\setminus L_s|
=n-D_R. \tag{1}
\]

Now suppose selected witnesses of ranks `a<b` share a left endpoint.  The two
intervals are nested.  The rank-`b` interval cannot be contained in the
rank-`a` interval, because interval containment implies containment of OR
masks, whereas a `b`-set cannot be contained in an `a`-set.  Hence the
rank-`a` interval is contained in the rank-`b` interval, and its mask is a
proper subset of the rank-`b` mask.  Doing this for every pair of ranks at the
common endpoint gives the claimed flag.  When the ranks are consecutive, it
is a saturated Boolean flag.

The proof for right endpoints is identical.  QED.

## 2. Most central masks are crossings of two full flags

### Theorem 2 (crossed-flag theorem)

Under the hypotheses of Theorem 1, fix `s in R`.  At least

\[
\max\{0,\ 2n-2D_R-m_s\} \tag{2}
\]

rank-`s` masks lie simultaneously on a full common-left flag and a full
common-right flag through all ranks in `R`.

#### Proof

Every endpoint in `intersection_{r in R} L_r` is the left endpoint of exactly
one selected rank-`s` witness.  Hence at least `n-D_R` rank-`s` masks are
left-good.  Similarly at least `n-D_R` are right-good.  These are two subsets
of a layer of size `m_s`, so their intersection has size at least

\[
(n-D_R)+(n-D_R)-m_s.
\]

QED.

There is also an exact useful expression for the number of bad masks.  Since
`m_s=n-d_s`, all but at most

\[
2(D_R-d_s) \tag{3}

\]

rank-`s` masks are crossed by the two full flags.

## 3. Exact asymptotic range of the theorem

First take `k=2m` and let

\[
W=\binom{2m}{m},\qquad n=W+e.
\]

For an integer `J>=0`, put

\[
R_J=\{m-J,m-J+1,\ldots,m+J\}.
\]

### Theorem 3 (central-band rigidity)

Uniformly for `J=o(sqrt(k))`,

\[
D_{R_J}=O\left(Je+\frac{WJ^3}{k}\right). \tag{4}

\]

Consequently, suppose

\[
n=(1+\varepsilon_k)W,\qquad \varepsilon_k\to0.
\]

If

\[
J\to\infty,\qquad J=o(k^{1/3}),\qquad J\varepsilon_k=o(1), \tag{5}
\]

then, in every layer belonging to `R_J`, all but `o(W)` masks are crossings of
a saturated common-left flag and a saturated common-right flag through the
entire band `R_J`.

In particular, if the conjectural sharp length

\[
n=B(k)=W+O(\sqrt{k})
\]

holds, then condition `J epsilon_k=o(1)` is automatic and every
`J=o(k^(1/3))` is permitted.

#### Proof

For `j>=0`,

\[
\frac{\binom{2m}{m+j}}{\binom{2m}{m}}
=\prod_{a=1}^j\frac{m-a+1}{m+a}.
\]

For `j=o(sqrt(k))`, taking logarithms (or using elementary product bounds)
gives

\[
1-\frac{\binom{k}{m+j}}{W}=O\left(\frac{j^2}{k}\right). \tag{6}
\]

Therefore

\[
d_{m+j}=n-\binom{k}{m+j}
=e+O\left(\frac{Wj^2}{k}\right).
\]

Summing this over `|j|<=J` proves (4), since
`sum_{|j|<=J}j^2=O(J^3)`.

Under (5), equation (4) gives `D_R=o(W)`.  Theorem 1 yields `W-o(W)` common
left endpoints and common right endpoints, while Theorem 2 yields `W-o(W)`
crossed masks in each layer.  QED.

For odd `k`, center `R_J` at the two equal middle layers.  The same product
estimate and proof apply.

The quantifier `J epsilon_k=o(1)` matters: the bare hypothesis
`n=(1+o(1))W` does not allow an arbitrarily prescribed `J=o(k^(1/3))`.
It does, however, always allow some `J=J(k)->infinity` satisfying (5).

## 4. Crossed flags force exact Boolean diamonds

### Lemma 4 (interval uncrossing)

For `a<=b<=c<=d`,

\[
U(a,c)\cup U(b,d)=U(a,d), \tag{7}
\]

and

\[
U(b,c)\subseteq U(a,c)\cap U(b,d). \tag{8}
\]

Consequently, for `rho(l,r)=|U(l,r)|`,

\[
rho(a,d)+rho(b,c)\le rho(a,c)+rho(b,d). \tag{9}

\]

Thus the rank triangle of interval ORs satisfies an anti-Monge inequality.

#### Proof

The union of the position intervals `[a,c]` and `[b,d]` is `[a,d]`, proving
(7).  Their positional intersection is `[b,c]`, which proves (8).  Apply
`|X union Y|+|X intersection Y|=|X|+|Y|`, using that the set in (8) may be a
proper subset of the set-theoretic intersection, to obtain (9).  QED.

### Theorem 5 (forced diamond at a flag crossing)

Suppose the consecutive ranks `s,s+1` lie in `R`, and a selected rank-`s` mask
`S` is crossed by a full left and right flag.  Let `X` and `Y` be its
rank-`s+1` neighbors in the left and right flags.  Then

\[
X=S\cup\{x\},\qquad Y=S\cup\{y\},\qquad x\ne y, \tag{10}
\]

and the hull of the witness intervals of `X` and `Y` is an interval whose OR
is exactly

\[
X\cup Y=S\cup\{x,y\}. \tag{11}

\]

If `s-1` also lies in `R`, the two lower flag neighbors are distinct
one-element deletions of `S` and their set union is `S`.

#### Proof

Write the selected witness of `S` as `[l,r]`.  Its upper neighbor in the left
flag has witness `[l,r']` with `r'>r`; its upper neighbor in the right flag has
witness `[l',r]` with `l'<l`.  Both masks are one-element extensions of `S`.
They are distinct: if they were the same selected mask, its single chosen
interval would share both endpoints with `[l,r]`, hence would equal `[l,r]`,
which is impossible because its rank is larger.  This proves (10).

The two upper witness intervals overlap in `[l,r]` and have hull `[l',r']`.
Lemma 4 gives

\[
U(l',r')=U(l,r')\cup U(l',r)=X\cup Y,
\]

which proves (11).  The lower flag neighbors are similarly distinct
codimension-one subsets of `S`, so their union is `S`.  QED.

Combining Theorems 3 and 5: any asymptotically width-optimal solution contains,
on almost every mask throughout a growing central band, two transverse flags
whose turns close to exact Boolean diamonds.  This is a much stronger
necessity statement than a middle-layer Hamilton path.

## 5. Research direction (not proved)

The preceding theorems do **not** prove that the local diamonds globally
iterate to an embedded cube or a full distributive growth diagram.  Different
diamonds can reuse the same outer union, and the inner interval in Lemma 4 can
have OR strictly smaller than the set-theoretic intersection unless it is a
selected flag witness.

The precise next question is:

> Can the almost-everywhere crossed flags be coherently iterated, or must their
> forced outer unions collide so often that `n=B(k)` becomes impossible?

There are two legitimate outcomes.

* An **existence theorem** for two compatible, nearly orthogonal systems of
  central Boolean flags, with a realizable anti-Monge growth diagram, would be
  a plausible route to `nu(k)=B(k)`.
* A **collision theorem** showing that too many flag turns share outer unions
  (or force strict inner-intersection loss) would yield a genuinely stronger
  global lower bound.

What is already ruled out is obtaining such an improvement from one-sided
Sperner/LYM counting alone: that information is exhausted by the rank-slack
bound.  The new mathematical object is the coupling of the left and right flag
systems.
