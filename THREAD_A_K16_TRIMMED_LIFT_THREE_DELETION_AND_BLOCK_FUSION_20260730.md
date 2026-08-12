# Exact three-deletion and block-fusion criteria for the standard trimmed lift

Date: 2026-07-30

Status: theorem and fixed-lift no-go.  This note gives exact
necessary-and-sufficient interval criteria, proves that no three entries can
be deleted from the authenticated standard lift, proves exact one-block and
arbitrary-support rethread floors, and proves that **no uniformly tagged
transformed-half replacement** can shorten that fixed one-transition lift to
`12873`.  It does **not** exclude mixed-tag rethreads of the high-copy
positions, or architectures that also rethread the old-coordinate shore or
move the singleton.

## 1. Setup

Let

\[
        A=(A_1,\ldots,A_n),\qquad \varnothing\ne A_i\subseteq V,
\]

be a universal set-valued word on `V`, and let `x` be a new point.  Its
standard trimmed lift is

\[
 L(A)=A_1,\ldots,A_n,\{x\},
       (\{x\}\cup A_1),\ldots,(\{x\}\cup A_{n-1}).       \tag{1.1}
\]

It has length `2n`.  For `D subseteq [n-1]`, let `L_D(A)` be obtained by
deleting precisely the transformed entries `x union A_d`, `d in D`.
Deleting only in the transformed copy has two important advantages:

1. the intact first copy still witnesses every nonempty old target;
2. the singleton `{x}` remains present.

Thus only targets of the form `{x} union S`, `S nonempty`, have to be
audited.

For an index set `I`, write

\[
                         A(I)=\bigcup_{i\in I}A_i.       \tag{1.2}
\]

## 2. The exact punctured-arc theorem

Call either of the following an **activated `D`-punctured arc**:

\[
 [a,b]\setminus D,
 \quad 1\le a\le b\le n-1,                              \tag{2.1}
\]

provided its first and last retained positions are used, or

\[
 [a,n]\ \cup\ \bigl([1,b]\setminus D\bigr),
 \quad 1\le a\le n+1,\quad 0\le b\le n-1,              \tag{2.2}
\]

where `[n+1,n]` and `[1,0]` mean the empty set.  In (2.2) the activation is
the central entry `{x}`; in (2.1) it is supplied by the transformed copy.
Empty arcs are ignored.

### Theorem 2.1 (exact deletion criterion)

The shortened word `L_D(A)` is universal on `V union {x}` if and only if,
for every nonempty `S subseteq V`, there is an activated `D`-punctured arc
`I` such that

\[
                              A(I)=S.                    \tag{2.3}
\]

#### Proof

The first copy of `A` and the retained singleton `{x}` settle the old
targets and `{x}`.  Consider an interval witnessing `{x} union S`.

If it lies wholly in the transformed block, its old-coordinate projection
is exactly (2.1).  Otherwise it must contain the central singleton.  Its
part before the singleton is a suffix `A_a,...,A_n`, and its part after the
singleton is a prefix of the transformed block with the deleted positions
omitted.  Its projection is exactly (2.2).  Hence every witness gives an arc
satisfying (2.3).

Conversely, the entries indexed by (2.1) are consecutive after the indicated
transformed entries have been deleted, and their union is `{x} union A(I)`.
The suffix, singleton, and punctured prefix in (2.2) are likewise consecutive
and have union `{x} union A(I)`.  Thus (2.3) produces the required witness.
\(\square\)

This theorem includes witnesses newly created by deletion.  It is therefore
strictly stronger than the sufficient test saying that one old witness must
avoid all deleted positions.

### Theorem 2.2 (arbitrary distribution of direct deletions)

Let `E subseteq[n]` be deleted from the first copy and
`F subseteq[n-1]` from the transformed copy, while the central singleton is
retained.  The resulting word is universal if and only if both of the
following hold for every nonempty `S subseteq V`:

1. some punctured first-copy interval `[a,b] setminus E` has union `S`;
2. either some transformed interval `[a,b] setminus F` has union `S`, or
   some punctured seam arc

   \[
        ([a,n]\setminus E)\ \cup\ ([1,b]\setminus F)   \tag{2.4}
   \]

   has union `S`.

Here endpoints may always be normalized to retained positions, and the same
empty-range conventions as in (2.2) apply.

#### Proof

An interval for an old target cannot meet the central or transformed block,
because every entry there contains `x`; this gives condition 1.  An interval
for `{x} union S` is either wholly transformed or crosses the central
singleton, giving the two alternatives in condition 2.  Conversely, the
punctured sets displayed in the two conditions are consecutive after
deletion and lift to the claimed targets. \(\square\)

The central singleton itself cannot be directly deleted: all other entries
containing `x` have a nonempty old projection, so no remaining interval can
have union exactly `{x}`.  Thus every direct three-deletion is described by
Theorem 2.2 with `|E|+|F|=3`.  The one-sided specialization `E=emptyset` is
Theorem 2.1 and avoids the additional requirement that the punctured first
copy remain universal.

### Proposition 2.3 (optimal-base shore rigidity)

Suppose `A` has minimum possible length `n=nu(|V|)`.  Then every universal
word `W` on `V union {x}` has at least `n` entries avoiding `x`.
Consequently:

* every direct three-deletion from `L(A)` must delete three transformed
  entries and must retain the central singleton;
* more generally, any length-`2n-3` block replacement of the lift has at
  most `n-3` entries containing `x`.

#### Proof

Partition the entries of `W` avoiding `x` into their maximal runs.  Every
old target has a witness wholly inside one such run.  Concatenate those runs,
discarding all entries containing `x`.  All the old witnesses survive, so
the concatenation is a universal word on `V`; it therefore has at least `n`
entries.

For a direct three-deletion from (1.1), deleting even one first-copy entry
would leave at most `n-1` entries avoiding `x`, contrary to the first part.
The center is undeletable by the preceding paragraph, so all three deletions
lie in the transformed copy.  The block-replacement bound follows by
subtracting the at least `n` low-shore entries from total length `2n-3`.
\(\square\)

For the retained `k=15` word this proposition is unconditional because
`nu(15)=6438=n` has already been proved.  Hence Theorem 2.1 is not merely a
convenient restricted model: it classifies **all** direct three-deletions of
its standard lift.

## 3. Compatible runs and the exact three-point fusion law

There is a useful equivalent form.  Form the projected word

\[
 \Pi_D=
 A_1,\ldots,A_n,\varnothing,
 A_1,\ldots,\widehat{A_d},\ldots,A_{n-1},               \tag{3.1}
\]

where hats occur exactly at `d in D`.  For a target `S`, call an entry
`S`-compatible when it is contained in `S`.  Call a run **activated** when
it meets the central empty entry or the second traversal.

### Theorem 3.1 (maximal-run form)

For fixed `D`, `L_D(A)` is universal if and only if, for every nonempty
`S subseteq V`, at least one activated maximal `S`-compatible run of
`Pi_D` has union exactly `S`.

#### Proof

Every interval with union `S` consists solely of `S`-compatible entries and
is contained in a maximal compatible run.  Enlarging it inside that run can
add no point outside `S`, so the maximal run still has union `S`.  The
converse is immediate.  Activation is exactly the requirement that the
corresponding lifted interval contain `x`.  Apply Theorem 2.1. \(\square\)

Now let `D={d_1,d_2,d_3}`.  Relative to `Pi_emptyset`, deleting a compatible
position merely removes its contribution from its run.  Deleting an
incompatible position can merge the compatible runs on its two sides; more
generally, two runs merge precisely when **every** position of the
incompatible barrier between them belongs to `D`.  Consequently every new
activated run is obtained by:

1. concatenating old compatible runs across barriers whose total deleted
   support lies in the three-point set `D`; and
2. removing the sets contributed by compatible positions in `D`.

This is an exact three-deletion fusion law.  There is no other way for a new
witness to appear.  In particular, an interior punctured arc consists of at
most four ordinary base intervals.  A seam arc consists of one intact suffix
and at most four prefix intervals.

### Private-witness obstruction

For fixed `D`, a target `S` is lost exactly when every activated maximal run
in Theorem 3.1 omits at least one point of `S`.  Hence if a transformed
singleton `x union A_d` is the sole activated saturated compatible run for
some `S=A_d`, and the allowed fusions across `D` still have union properly
below `S`, then `d` is undeletable.  This is the exact version of a
"private-witness" obstruction; occurrence counts alone are not sufficient.

## 4. A laminar interval sufficient theorem

For nonempty `S subseteq V`, let

\[
 \mathcal I_S={[a,b]\subseteq[1,n-1]:
                     A_a\cup\cdots\cup A_b=S\}.         \tag{4.1}
\]

Call `S` terminally witnessed if `A_a union ... union A_n=S` for some `a`.

### Proposition 4.1 (literal-witness preservation)

A set `D subseteq[n-1]` is safe if, for every nonempty `S`, either `S` is
terminally witnessed or some interval in `I_S` is disjoint from `D`.

#### Proof

A terminal witness lifts through `A_a,...,A_n,{x}` and uses no transformed
position.  An interval in `I_S` disjoint from `D` survives verbatim in the
transformed block. \(\square\)

Let `tau(I_S)` denote the minimum number of points meeting every interval in
`I_S`.  The elementary interval transversal theorem says that `tau(I_S)` is
also the maximum number of pairwise disjoint members of `I_S`: greedily take
an interval with smallest right endpoint, stab at that endpoint, and repeat.
Therefore:

### Corollary 4.2 (four-witness theorem)

If every nonterminally witnessed `S` has four pairwise disjoint intervals in
`I_S`, then **every** three-set `D subseteq[n-1]` is safe.

More generally, for a chosen `D`, Proposition 4.1 fails at `S` exactly when
`D` is a transversal of `I_S` and `S` has no terminal witness.  Thus, if
`Bad(S)` denotes the three-element transversals of `I_S`,

\[
 \sum_{S\text{ nonterminal}} |Bad(S)|
          < {n-1\choose3},                              \tag{4.2}
\]

then at least one safe three-set exists.  This is only a sufficient counting
criterion because punctured-run fusion can rescue triples counted as bad.

Universality alone cannot replace these hypotheses.  For example,
`A=({1},{2})` is universal on two points, but deleting its only transformed
entry `x union {1}` loses that target: the seam suffix contains `{2}`.  Thus
even one black-box deletion can fail.

## 5. Exact terminal three-trim theorem

The simplest candidate is to omit the last three transformed entries.  Put

\[
             D_{\rm tail}=\{n-3,n-2,n-1\}.              \tag{5.1}
\]

### Theorem 5.1 (three-entry terminal compression)

The word

\[
 A_1,\ldots,A_n,\{x\},
 (\{x\}\cup A_1),\ldots,(\{x\}\cup A_{n-4})          \tag{5.2}
\]

has length `2n-3` and is universal if and only if every nonempty
`S subseteq V` is the union of either

\[
 A_a,\ldots,A_b,\qquad 1\le a\le b\le n-4,             \tag{5.3}
\]

or

\[
 A_a,\ldots,A_n,A_1,\ldots,A_b,
 \qquad 1\le a\le n+1,\quad0\le b\le n-4.             \tag{5.4}
\]

#### Proof

These are exactly the arcs (2.1)--(2.2) after substituting (5.1). \(\square\)

Let `H` be the family of targets not witnessed inside the prefix
`A_1,...,A_{n-4}`.  Theorem 5.1 equivalently says that the terminal trim
works precisely when every `S in H` has a wrapping witness (5.4).

There is an immediate and useful obstruction:

### Corollary 5.2 (last-entry containment obstruction)

If `S` does not contain `A_n`, then no wrapping interval (5.4) can witness
`S`.  Hence terminal three-trimming requires every such `S` to be witnessed
inside `A_1,...,A_{n-4}`.  In particular, whenever

\[
                         A_n\nsubseteq A_{n-j},          \tag{5.5}
\]

for `j=1,2,3`, the omitted projection `A_{n-j}` itself must have a second
witness wholly in the first `n-4` entries.

The familiar descending-chain condition

\[
 A_{n-3}\supseteq A_{n-2}\supseteq A_{n-1}\supseteq A_n
                                                               \tag{5.6}
\]

is sufficient, because any witness meeting the last four positions can be
extended to the end without changing its union.  Theorem 5.1 is strictly
weaker than (5.6): it permits target-dependent wrapping witnesses and does
not require the endpoint states themselves to be nested.

## 6. Application to the retained `k=15` word

For `A=answers/k15.word`, `n=6438`.  Therefore any safe three-set in the
transformed copy gives a literal `k=16` word of length

\[
                         2n-3=12873.                    \tag{6.1}
\]

The last four retained entries are

\[
\begin{array}{c|c|l}
 i & A_i & \text{support}\ \\ \hline
 n-3 &3169=\mathtt{0x0c61}&\{0,5,6,10,11\}\\
 n-2 &19521=\mathtt{0x4c41}&\{0,6,10,11,14\}\\
 n-1 &2657=\mathtt{0x0a61}&\{0,5,6,9,11\}\\
 n   &18033=\mathtt{0x4671}&\{0,4,5,6,9,10,14\}.
\end{array}                                             \tag{6.2}
\]

Thus the endpoint-chain hypothesis (5.6) fails.  More sharply,

\[
\begin{aligned}
 A_n\setminus A_{n-3}&=\{4,9,14\},\\
 A_n\setminus A_{n-2}&=\{4,5,9\},\\
 A_n\setminus A_{n-1}&=\{4,10,14\}.
\end{aligned}                                           \tag{6.3}
\]

Consequently Corollary 5.2 gives three mandatory prefix tests for the naive
terminal trim: each of the masks `3169`, `19521`, and `2657` must be an
interval union wholly inside positions `1,...,6434`.  Passing these three
tests is necessary, not sufficient; the exact remaining test is Theorem 5.1
on the prefix-hole family `H`.

No conclusion about those prefix witnesses is inferred merely from the
already verified universality of `A`: their displayed singleton occurrences
lie in the omitted tail and hence do not settle the question.

The next section supersedes this last uncertainty: no terminal trim, and in
fact no pure three-deletion anywhere in the lift, can work.

## 7. Rank-seven saturation forbids every pure three-deletion

We first record a stability lemma for the interval-containment poset.

### Lemma 7.1 (near-maximum interval antichains are short)

Let `C=(C_1,...,C_L)` be any set-valued word.  Suppose `t` distinct sets of
one fixed cardinality are witnessed by intervals of `C`.  One may choose
their witness intervals so that every chosen interval has length at most

\[
                              L-t+1.                    \tag{7.1}
\]

#### Proof

Choose one witness interval `[l_i,r_i]` for each target.  No chosen interval
can contain another: containment of intervals implies containment of their
unions, and two distinct sets of the same cardinality cannot contain one
another.  Thus the witnesses form an antichain.

Order them so that

\[
                    l_1<\cdots<l_t.
\]

Antichainness forces `r_1<...<r_t`.  Hence `l_i>=i`, while `r_i`, the `i`-th
member of a `t`-set in `[L]`, satisfies `r_i<=L-t+i`.  Therefore

\[
                    r_i-l_i+1\le L-t+1.
\]

This proves (7.1). \(\square\)

For the authenticated source word, whose SHA-256 is

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b,
```

a direct linear audit gives the following exact facts.

### Lemma 7.2 (the three finite source facts)

Let `n=6438` and `A^-=A_1,...,A_{n-1}`.

1. The distinct suffix unions of `A` have the following start positions,
   masks, and cardinalities:

\[
\begin{array}{c|c|c}
 n+1&0&0\\
 6438&18033&7\\
 6437&20081&8\\
 6434&20083&9\\
 6433&20087&10\\
 6432&20215&11\\
 6431&24311&12\\
 6430&32503&13\\
 6429&32511&14\\
 6428&32767&15.
\end{array}                                             \tag{7.2}
\]

2. Among the letters of `A^-`, exactly one has cardinality seven:
   `A_1=18553`.
3. Among the adjacent pairs of `A^-`, exactly two have union cardinality
   seven.  They start at positions `2` and `6436`, and their unions are
   respectively `10361` and `20065`.

For the reversed orientation, the relevant suffix profile is the prefix
profile of `A`; its masks are

\[
0,18553,26745,26749,27773,31869,32381,32509,32511,32767,
\]

again with cardinalities `0,7,8,...,15`.  The two endpoint rank-seven
letters are interchanged, so the reversed trimmed block again contains one
rank-seven letter, and the same two rank-seven adjacencies remain (in reverse
order).  Thus all three **counts** used below are orientation-invariant.

These are source facts, not a search hypothesis.  They require only one pass
through the 6,438 displayed masks.

### Lemma 7.3 (all three deletions would have to be transformed)

Assume the proved equality `nu(15)=6438`.  If three entries could be deleted
from `L(A)` while leaving a universal word, then all three deleted entries
would be transformed entries `x union A_i`, `i<n`.

#### Proof

A target not containing `x` can be witnessed only inside the first,
untransformed copy of `A`.  Deleting a letter from that copy would therefore
leave a universal word on 15 points of length at most `6437`, contradicting
`nu(15)=6438`.  Deleting the singleton `{x}` is also impossible: every other
letter containing `x` contains a nonempty old set, so none can witness
`{x}`.  The assertion follows. \(\square\)

### Theorem 7.4 (pure three-deletion no-go)

No three entries can be deleted from the authenticated length-`12876`
standard trimmed lift of `answers/k15.word` while preserving universality.
The conclusion also holds for the lift of the reversed source word.

#### Proof

By Lemma 7.3 the deletions have the form `D subseteq[n-1]`, `|D|=3`.  Let

\[
                 C_D=(A_1,\ldots,A_{n-1})\setminus D.
\]

Then `C_D` has length

\[
                              L=6434.                   \tag{7.3}
\]

There are `binom(15,7)=6435` old rank-seven targets.  By Theorem 2.1, a
target containing `x` is witnessed either internally in `C_D` or by a suffix
union of `A` joined to a prefix union of `C_D`.

For one fixed suffix state, the outputs obtained as the prefix grows form a
chain, and hence contain at most one distinct rank-seven set.  By (7.2), only
two suffix states have cardinality at most seven: the empty state and
`18033`.  Consequently the seam can supply at most two distinct rank-seven
targets.  At least

\[
                        6435-2=6433=L-1               \tag{7.4}
\]

distinct rank-seven targets must therefore be witnessed internally in
`C_D`.

Apply Lemma 7.1 with `t=L-1`.  Those targets admit distinct witnesses of
length at most two.  But Lemma 7.2 shows that before deletion `A^-` has only
one rank-seven singleton and only two adjacent pairs with rank-seven union.
Deleting three positions creates at most three new adjacencies in the
compressed word.  Thus `C_D` has at most

\[
                              1+2+3=6                  \tag{7.5}
\]

intervals of length at most two whose union has cardinality seven.  This
contradicts (7.4).  Reversal preserves all three source counts used in the
argument. \(\square\)

The proof is deliberately stronger than a failed search: it excludes
simultaneous-only triples, including triples whose witnesses arise by
four-piece fusion as in Section 3.

There is also a useful general saturation law.  After deleting `d<=3`
transformed entries, the transformed block has length `6437-d`, but at least
`6433` rank-seven targets must still be internal.  Lemma 7.1 therefore forces
a selected witness for each of them of length at most `5-d`.  At `d=3` this
collapses to length two and yields the contradiction above.

## 8. Exact bounded-block replacement signature

The deletion set need not be treated globally.  Let a word `W` be split as

\[
                         W=P\,B\,R,                     \tag{8.1}
\]

and replace `B` by a word `C`.  Fix a target `T`.  In `P`, record the union
`lambda_T` of the maximal `T`-compatible suffix; in `R`, record the union
`rho_T` of the maximal compatible prefix.  Also record whether an unaffected
maximal compatible run away from these two collars already has union `T`.
Form the short boundary word consisting of the left compatible collar, the
entries of `C`, and the right compatible collar.  Put a separator at every
incompatible entry of `C` (and at a missing collar), and take the unions of
the resulting maximal compatible segments.  Thus a collar is also retained
as a candidate when the adjacent boundary entry of `C` is incompatible; if
`C` is empty, the two collars concatenate directly.

### Theorem 8.1 (complete block signature)

The replacement `P C R` witnesses `T` if and only if either

1. an unaffected outside run already has union `T`; or
2. one of the boundary-word compatible segments just described has union
   `T`.

#### Proof

The maximal compatible runs listed above are exactly the maximal
`T`-compatible runs of `P C R`.  A target has a witness if and only if one
such run has union `T`, by the same enlargement argument as in Theorem 3.1.
\(\square\)

For a block wholly inside the transformed half of (1.1), require every entry
of `C` to contain `x` and apply Theorem 8.1 to the old-coordinate
projections.  Old targets remain covered by the intact first copy.  Hence a
replacement of `b` transformed entries by `b-3` entries yields a universal
length-`2n-3` word **exactly when** its boundary signature satisfies Theorem
8.1 for every `{x} union S` not already externally witnessed.

This is the promised bounded fusion theorem.  Its input is not all intervals
of the word, but only:

* the externally uncovered target family;
* one compatible suffix union and one compatible prefix union per such
  target; and
* the compatible-run unions of the replacement block.

For the authenticated lift, the rank-seven saturation argument forces this
exact signature to be macroscopic.

### Theorem 8.2 (single-block support floor, arbitrary replacement letters)

Suppose one contiguous block of `b>=3` entries in the transformed tail of
`L(A)` is replaced by `b-3` arbitrary nonempty `16`-point letters, with the
first copy of `A` and the singleton `{x}` left fixed.  The replacement
letters need not all contain `x`.  If the resulting length-`12873` word is
universal, then

\[
                              b\ge3218.                 \tag{8.2}
\]

In particular, no bounded-support or local block replacement can close the
three-letter gap.

#### Proof

Let `T` be the resulting tail, of length `L=6434`, and project every tail
letter to the old coordinates.  Among tagged rank-seven targets, an interval
using the central singleton and an empty old suffix contributes at most one
prefix-union state of rank seven.  An interval using a nonempty suffix of
`A` contributes at most the single state `A_n=18033`, because that suffix
already contains this rank-seven set.  Every other tagged rank-seven target
must be witnessed by an interval wholly in `T` that contains `x`.  Thus at
least `6435-2=6433=L-1` distinct rank-seven old projections are internal to
`T`.  Lemma 7.1 forces a chosen witness for each of them to have length at
most two.

Outside the replaced block, at most the three original length-at-most-two
rank-seven intervals from Lemma 7.2 survive.  Put `c=b-3`.  If `c>0`, the
new block contributes at most `c` singleton intervals, `c-1` internal
adjacent pairs, and two boundary adjacent pairs, a total of `2c+1=2b-5`.
If `c=0`, the direct new boundary adjacency gives one interval, which obeys
the same bound.  Hence the whole transformed projection has at most

\[
                             3+(2b-5)=2b-2             \tag{8.3}
\]

length-at-most-two intervals of rank-seven union.  Necessarily

\[
                             2b-2\ge6433,
\]

which is equivalent to (8.2). \(\square\)

For a uniformly tagged tail, the preceding support floor is superseded by
the following saturation theorem.  The improvement is that an empty-suffix
seam witness is already an internal prefix witness of the transformed word
and must not be counted as a genuinely external target.

### Theorem 8.3 (dimension-uniform fixed-anchor tagged-tail bound)

Let `A=(A_1,...,A_n)` be universal on a `k`-point ground set and suppose

\[
                         |A_n|=r\ge2.                  \tag{8.4}
\]

For an arbitrary word `C=(C_1,...,C_m)` of old-coordinate subsets, allowing
empty `C_i`, if

\[
 A_1,\ldots,A_n,\{x\},
 (\{x\}\cup C_1),\ldots,(\{x\}\cup C_m)              \tag{8.5}
\]

is universal, then

\[
                              m\ge {k\choose r}.        \tag{8.6}
\]

For the authenticated source, `(k,r)=(15,7)`, so a uniformly tagged tail
needs at least `6435` entries and the fixed-anchor word has length at least

\[
                         6438+1+6435=12874.             \tag{8.7}
\]

In particular, no arbitrary `6434`-entry uniformly tagged replacement, with
the first copy and central singleton fixed, reaches length `12873`.  The same
assertion holds with the source word reversed.

#### Proof

Consider the `{k choose r}` targets `{x} union S` with `|S|=r`.  A seam witness
with empty old-coordinate suffix has the form

\[
 \{x\},\{x\}\cup C_1,\ldots,\{x\}\cup C_j.
\]

For `j>=1` its union is already witnessed by the internal prefix

\[
 (\{x\}\cup C_1),\ldots,(\{x\}\cup C_j),
\]

and `j=0` gives only `{x}`.  Hence a rank-seven target having no internal
witness must use a nonempty suffix of `A`.

Every nonempty suffix contains the rank-`r` last entry `A_n`.  If its union
with a prefix of `C` has rank `r`, the output is therefore exactly `A_n`.
At most one rank-`r` target can lack an internal witness.  Consequently `C`
internally witnesses at least

\[
                              {k\choose r}-1
\]

distinct rank-`r` targets.

The fixed-rank interval antichain bound in Lemma 7.1 gives
`m>={k choose r}-1`.  If equality held, Lemma 7.1 would force every chosen
witness to have length one.  All `m` entries of `C` would then be distinct
rank-`r` sets.  Since `r>=2`, no target `{x,v}`, `v in V`, could be
witnessed: a nonempty internal interval has old rank at least `r`, a seam
with nonempty suffix contains `A_n`, and an empty-suffix seam is either
`{x}` or duplicates a nonempty internal prefix.  Equality is impossible,
proving (8.6).

For the reversed source, its last entry is the original first entry
`18553`, again of rank seven, so the same proof applies. \(\square\)

Theorem 8.3 uses only the endpoint rank, not the singleton/adjacency census
of Lemma 7.2.  It allows simultaneous changes at every transformed position
and therefore strictly contains Theorems 7.4 and 8.2 within the uniformly
tagged one-transition architecture.

We now quantify the minimum support of a completely general mixed-tag tail
rethread.  The definition records exactly which original high-copy letters
are genuinely retained.

### Definition 8.4 (order-preserving rethread support)

Let

\[
 H=(\{x\}\cup A_1,\ldots,\{x\}\cup A_{6437})
\]

be the original high copy, of length `M=6437`.  For a tail `T` of length
`M-3=6434`, define its support `s=s(T)` by

\[
 s=M-\max\{|J|:H_J\text{ occurs in }T
              \text{ unchanged and in order}\}.       \tag{8.8}
\]

Equivalently, `T` is obtained by deleting `s` letters of `H` and inserting
`s-3` arbitrary nonempty 16-point letters at arbitrary gaps, while every
undeleted letter remains unchanged and in its original relative order.

This model permits scattered replacements, mixed `x`-status, and arbitrarily
many edited blocks; it excludes only a permutation of letters declared
"unchanged."

### Theorem 8.5 (general high-copy rethread fraction)

If

\[
 A_1,\ldots,A_{6438},\{x\},T_1,\ldots,T_{6434}       \tag{8.9}
\]

is universal and `T` has order-preserving support `s`, then

\[
                s\ge1610,
 \qquad s-3\ge1607,
 \qquad \frac{s}{6437}\ge\frac{1610}{6437}>\frac14. \tag{8.10}
\]

Thus even after allowing arbitrary mixed tags and scattered edits, more than
one quarter of the old high copy must be rethreaded.  For one contiguous
block, Theorem 8.2 improves this to `3218/6437`.

#### Proof

As in Theorem 8.2, at most two tagged rank-seven targets can avoid an
activated tail interval.  More explicitly, prefixes ending before the first
`x`-tag form one nested chain, while a prefix reaching an `x`-tag is already
an activated tail prefix; a nonempty old suffix contributes only `A_n`.
Hence `T` contains at least `6433=M-4` distinct rank-seven old projections
witnessed by intervals.  Lemma 7.1, with tail length `M-3`, makes every
selected witness have length at most two.

Fix a maximizing unchanged-subsequence embedding `H_J` in `T` from
Definition 8.4.  In the original tail `H`, Lemma 7.2 gives exactly one rank-seven singleton
and exactly two rank-seven adjacent pairs.  Therefore the other

\[
                    (M-1)+(M-3)=2M-4               \tag{8.11}
\]

original intervals of length at most two have old union of rank different
from seven.  Under a support-`s` rethread, at most `s` of these protected
singletons disappear.  Deleting endpoints destroys at most `2s` protected
adjacent pairs, and the `s-3` insertions can split at most `s-3` further
protected adjacent pairs.  Thus at least

\[
                    2M-4-(4s-3)=2M-1-4s           \tag{8.12}
\]

non-rank-seven short intervals survive in `T`.

The length-`M-3` word `T` has exactly

\[
                    2(M-3)-1=2M-7                 \tag{8.13}
\]

singleton-or-adjacent intervals altogether.  Consequently at most

\[
                    (2M-7)-(2M-1-4s)=4s-6         \tag{8.14}
\]

of them have rank-seven old union.  The required `M-4=6433` distinct
rank-seven witnesses force

\[
                    M-4\le4s-6,
\]

or `4s>=M+2=6439`.  Hence `s>=1610`; the insertion and fraction statements
follow. \(\square\)

The three support conclusions have different logical strengths:

* Theorem 7.4: a three-position subsequence edit is impossible.
* Theorem 8.2: an arbitrary one-block edit needs `b>=3218` old positions.
* Theorem 8.5: an arbitrary scattered mixed-tag edit needs `s>=1610` old
  positions.
* Theorem 8.3: if every tail letter still contains `x`, even `s=6437` does
  not suffice.

## 9. Audit of sequential-deletion search and the exact remaining gate

The comment at lines 194--196 of
`scratch/k16_trimmed_lift_delete_search_20260730.cpp` claims that every
universal three-deletion subsequence admits an ordering in which each single
deletion preserves universality.  That monotonicity assertion is false.

On three points, encode subsets by their nonzero binary masks and take

\[
                         W=(1,3,4,5,2,6,1).             \tag{9.1}
\]

The word is universal: masks `1,...,6` occur as letters and `7=3 union 4`.
Deleting positions `2,4,6` gives

\[
                         (1,4,2,1),                     \tag{9.2}
\]

whose intervals realize `1,2,4` as letters, `5=1 union 4`, `6=4 union 2`,
`3=2 union 1`, and `7=1 union 4 union 2`.  Yet deleting position `2` alone
loses mask `3`, deleting position `4` alone loses mask `5`, and deleting
position `6` alone loses mask `6`.  No first deletion in the successful
triple is safe.

Thus that DFS explores only the sequentially safe subclass unless a special
sequentialization theorem is supplied.  Theorem 7.4 makes its completeness
irrelevant for the authenticated standard lift: the pure-deletion class is
empty by a separate proof.

For the verified length-`12876` standard lift, Theorem 7.4 closes pure
puncturing and Theorem 8.3 closes the uniformly tagged fixed-transition form

\[
                         A,\{x\},\{x\}\cup C.          \tag{9.3}
\]

Therefore no uniformly high transformed-side compiler, even one supported
on all 6,434 final positions, can close the gap while the old copy and
singleton remain fixed.  A mixed-tag compiler is not excluded, but Theorem
8.5 forces it to replace/delete at least 1,610 old high-copy positions and
insert at least 1,607 new letters.  The next construction must therefore do
at least one of:

1. the old-coordinate shore itself (while respecting the optimal-base count
   in Proposition 2.3);
2. the placement/role of the singleton `{x}`; or
3. the one-transition high-bit topology, necessarily at the macroscopic
   support quantified in (8.10), so that more than one genuinely external
   seam can serve the saturated rank-seven layer.

Theorem 8.1 remains the exact local signature for any individual block.
Inside (9.3), Theorem 8.3 rules out the uniformly tagged architecture; for
mixed tags, Theorems 8.2 and 8.5 rule out local support.  Neither
universality of the base word, endpoint-chain folklore, raw witness
multiplicities, nor a sequential-deletion DFS reaches the surviving global
rethread architectures.

## 10. Frozen source and audit artifacts

The theorem uses the following frozen finite inputs.

```text
answers/k15.word
  SHA-256 f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

reconstructed standard lift, canonical one-space rendering
  SHA-256 9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8

scratch/audit_threadA_k16_trimmed_lift_three_deletion_rank7_20260730.py
  SHA-256 e3405bc184ae07ecab3d8eb066f52a22f992a566add9314cec0f6a604f3e38ba

scratch/threadA_k16_trimmed_lift_rethread_bounds_20260730.audit.json
  SHA-256 1f0e05b717aa94332353588301c5d1fec92e3759d93f8bf833472c7168dea651

scratch/audit_threadA2_k16_trimmed_lift_witness_structure_20260730.py
  SHA-256 4d6d1da9e7e710a7dd6d3bec6fcd2a7e5d6c2e3b89c3445cbfa09c70eb3bd242

scratch/threadA2_k16_trimmed_lift_witness_structure_20260730.audit.json
  SHA-256 7504a74c47234602aa7bfdfda9d885215016ab1fdfa61f2b9fb398ec29c969cd
```

Both scripts are linear/lightweight certificate audits; neither searches a
deletion set or replacement.  The JSON ledger freezes the arithmetic for the
`3218` one-block floor, the `1610` arbitrary-support floor, and the uniformly
tagged full-rewrite no-go.  The hash of this theorem note is reported in the
handoff after the note is frozen, avoiding a self-referential hash.
