# A PBBS facet-word half-cube upper bound for every `k`

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` upper bound  
Status: unconditional theorem, conditional only on PBBS facts already proved
and audited in the cited reports.  This gives a nontrivial general upper
bound, not `B(k)+O(1)`.

## 0. The theorem

For odd `k>=3`, put

\[
 W_k={k\choose (k-1)/2}={k\choose (k+1)/2}.
\]

Then

\[
 \boxed{
 \nu(k)\le
 2^{k-1}-1+{k+2\over k}W_k.}                         \tag{0.1}
\]

For even `k>=4`, put `W_k=binom(k,k/2)`.  Then

\[
 \boxed{
 \nu(k)\le
 2^{k-1}-1+{k+1\over k-1}W_k.}                       \tag{0.2}
\]

The proof uses one exact physical set-word.  It does not combine separate
rankwise rows.  The odd construction is the cyclic rank-`(r-1)` facet word
of the PBBS rank-`r` owner factor, opened componentwise and repaired by the
proved compressed boundary collars.  The even construction is the literal
three-block doubling `A,{z},z+A` of the odd word.

The leading term is one half of the full Boolean lattice.  Since
`W_k=Theta(2^k/sqrt(k))`, both bounds are

\[
                         2^{k-1}+O(2^k/\sqrt k).       \tag{0.3}
\]

This is much weaker than the conjectural `B(k)+O(1)`, whose scale is
`Theta(2^k/sqrt(k))`; its value is that it is an unconditional reusable
all-dimensional consequence of the PBBS flag theorem and seam collar.

## 1. Imported PBBS facts

Let

\[
                         k=2m+1,\qquad r=m+1,
 \qquad W={2m+1\choose m}.
\]

We use the following already proved facts about the complement-projected
step-two PBBS factor.

1. It is a cycle factor on all `W` rank-`r` owners.
2. Every consecutive pair is Johnson adjacent.  Its rank-`m` edge facets
   collectively contain every rank-`m` mask.  Since there are exactly `W`
   directed factor edges and exactly `W` such masks, every facet occurs
   exactly once: the factor is lower-q1-rainbow.
3. Every target `U` of rank at least `r` is a cyclic interval union of
   owners in one PBBS component.  This is the upper half of the complete
   PBBS all-depth flag theorem.
4. Every PBBS orbit has length `ell*k`.  Its step-two cycles have length
   `ell*k/gcd(2,ell*k)`.  Since `k` is odd, this is `ell*k` when `ell` is
   odd and `(ell/2)k>=k` when `ell` is even.  Thus every projected cycle
   has length at least `k`; equivalently the number `c` of projected cycles
   satisfies
   \[
                               c\le {W\over k}.         \tag{1.1}
   \]

Facts 2--4 are proved together for this same complement-projected factor in
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`
(Theorem 1.1(4), Theorem 2.2, and Corollary 2.3), with the underlying PBBS
flag inputs independently audited there.  No PBBS Hamiltonization or
compiler antecedent is imported here.

## 2. Owners become adjacent unions of facets

Fix one PBBS owner cycle

\[
               T_0,T_1,\ldots,T_{L-1}\in{[k]\choose r}
\]

with cyclic indices, and define its facet cycle

\[
                         F_i=T_i\cap T_{i+1}.          \tag{2.1}
\]

Every `F_i` has rank `r-1=m`.

### Lemma 2.1 (facet expansion of owner intervals)

For every `i`,

\[
                         T_i=F_{i-1}\cup F_i.          \tag{2.2}
\]

Consequently every cyclic owner interval satisfies

\[
 \bigcup_{h=a}^{b}T_h
   =\bigcup_{h=a-1}^{b}F_h,                            \tag{2.3}
\]

where both ranges are read cyclically.  Thus every PBBS upper target is a
cyclic interval union in the facet cycle.

#### Proof

Both `F_(i-1)` and `F_i` are rank-`m` facets of `T_i`.  They are distinct,
because the global facet deck is rainbow.  Two distinct rank-`m` subsets of
the rank-`(m+1)` set `T_i` have union exactly `T_i`, proving (2.2).
Taking the union of (2.2) over the consecutive owner range gives (2.3).
If the owner interval is the entire component, the written facet range
repeats its endpoint; deleting that repetition leaves the full facet cycle
with the same union, which is an allowed full cyclic interval.
The imported PBBS upper-support theorem then gives the last assertion.
QED.

Notice that this step uses q1 rainbowness, not merely support with
multiplicity.  If two incident facets could coincide, (2.2) would fail.

## 3. Opening the facet cycles

Delete one cyclic transition from each of the `c` facet cycles and write
the resulting linear facet paths consecutively.  Call this word `Q`.  It
has exactly `W` nonzero letters and contains every rank-`m` mask as a
singleton.

For one deleted facet-cycle transition, apply the compressed boundary-grid
collar theorem with letter rank `m=r-1`.  Its collar length is at most

\[
 2(k-m)+1=2(k-r+1)+1=k+2.                         \tag{3.1}
\]

The collar realizes every cyclic facet interval which crossed that cut.
Intervals avoiding the cut remain inside the corresponding linear block
of `Q`.  Therefore, by Lemma 2.1, `Q` together with these `c` collars
covers every mask of rank at least `r` as well as every rank-`m` mask.

Let `mu(k,m-1)` denote the minimum length of a word covering the complete
nonempty ideal through rank `m-1`.  Appending any such lower-ideal word
gives the exact modular estimate

\[
 \boxed{\nu(k)\le W+\mu(k,m-1)+c(k+2)
       \le W+\mu(k,m-1)+{k+2\over k}W.}              \tag{3.2}
\]

This is a legitimate Pascal-recursion interface, but
`MATH_THEOREM_R_ALLK_LITERAL_FACET_RETENTION_BARRIER_20260730.md` proves
that retaining the literal facet deck still costs at least
`W+binom(k,m-1)+delta`; recursion alone cannot approach the deadline.

Append once, as literal one-cell words, every nonempty mask of rank at most
`m-1`.  Appending destroys no old witness.  The resulting word is universal
on `[k]`.

Its length is at most

\[
 W+\sum_{s=1}^{m-1}{k\choose s}+c(k+2).                \tag{3.3}
\]

By symmetry of the odd binomial row,

\[
 \sum_{s=0}^{m}{2m+1\choose s}=2^{2m},
 \qquad {2m+1\choose m}=W,                            \tag{3.4}
\]

and hence

\[
 W+\sum_{s=1}^{m-1}{k\choose s}=2^{k-1}-1.            \tag{3.5}
\]

Using (1.1) in (3.3) proves (0.1).

### Audit of the seam implication

The collar is applied to the **facet** cycle, not to the owner cycle.  Its
rank parameter is therefore `m`, which is why the cost is `k+2`, rather
than the `k` cost for a rank-`r` owner cycle.  It repairs every cyclic facet
interval, including the two-facet interval (2.2) for the owner at the cut.
No lower compiler is needed because all masks below the facet rank are
supplied literally.

## 4. Even dimensions by exact three-block doubling

Let `n=k-1` be odd and let

\[
                         A=(A_1,\ldots,A_L)
\]

be the odd universal word just constructed on `[n]`.  Add a new coordinate
`z` and define

\[
 z+A=(\{z\}\cup A_1,\ldots,\{z\}\cup A_L).            \tag{4.1}
\]

### Lemma 4.1 (universal doubling)

The nonzero word

\[
                         A,\ \{z\},\ z+A              \tag{4.2}
\]

is universal on `[n] union {z}` and has length `2L+1`.

#### Proof

Every nonempty old target `S subseteq [n]` has a witness inside the first
copy `A`.  The singleton `{z}` is the central letter.  If `S` is nonempty
and an interval of `A` has union `S`, the corresponding interval in `z+A`
has union `{z} union S`.  These are all nonempty masks on the enlarged
coordinate set.  QED.

Apply (0.1) to `n=k-1`.  With

\[
 W_n={k-1\choose k/2-1},\qquad
 W_k={k\choose k/2}=2W_n,                             \tag{4.3}
\]

Lemma 4.1 gives

\[
\begin{aligned}
 \nu(k)
 &\le2\left(2^{k-2}-1+{k+1\over k-1}W_n\right)+1\\
 &=2^{k-1}-1+{k+1\over k-1}W_k,
\end{aligned}                                         \tag{4.4}
\]

which is (0.2).

The proof of Lemma 4.1 uses only witnesses wholly within one of the two
copies.  No boundary residence, common carrier, or mixed-seam assertion is
hidden in the even lift.

## 5. Exact scope against `k=11`--`k=16`

* For odd `k=11,13,15`, the retained optimal certificates are far shorter
  than (0.1): they solve the exact carrier/compiler gate at length `B(k)`.
  The present theorem is compatible with, but does not explain, that
  equality.
* For `k=16`, the authenticated length-`B(16)+1` word is likewise much
  shorter than (0.2).  The three-block lift is only an unconditional
  all-dimensional fallback and does not constrain the finite gap-one
  search.
* The theorem makes no inference from the `k=16` word to a flat derivative
  factor and no inference from finite equality through `k=15` to all `k`.

## 6. Proved and unproved boundary

Proved here:

1. the exact facet expansion (2.2)--(2.3);
2. the odd half-cube bound (0.1), using the audited PBBS upper flag factor,
   q1 rainbow deck, component count, and compressed collar theorem; and
3. the even bound (0.2) by literal universal doubling.

Not proved or claimed:

1. `nu(k)<=B(k)+O(1)`;
2. a compiler antecedent for the opened PBBS owner chronology;
3. preservation of PBBS lower flags after component opening (they are not
   needed because ranks below `m` are literal and rank `m` is the facet
   deck);
4. a collar shorter than `k+2` per odd PBBS component; or
5. optimality of either displayed upper bound.
