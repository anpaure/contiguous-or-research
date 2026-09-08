# The existing subroot PBBS word has a macroscopic literal hole family

2026-09-08. Pure proof by ternary_lift; no mathematical execution,
catalogue, or optimization. Appendix_a full-file independent audit: PASS.
Root full-file audit, including the literal erosion and staircase source
letters and both aggregate limits: PASS.

This assesses the user's finite cylinder-completion theorem on an ACTUAL
unconditional PBBS word. The conclusion is a hole lower bound, not merely
the absence of a proved coverage theorem. It also excludes a specific
cheaper compile: keeping a positive fraction of that PBBS alphabet while
trying to obtain a near-width density-almost-cover by changing the rest.
It does not exclude a bulk replacement of the alphabet or a deeper erosion
whose physical target coverage still has to be proved.

## 1. The actual near-width word under inspection

Put n=2r+1, W=binom(2r+1,r), and B=Cat_r=W/(2r+1). Choose integers

    H>=1, H=o(sqrt(r)), 2H<=r+1.

Use the literal central-band compiler of Sections22 and24 of
`../PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, as consolidated in
`PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md`.
No exterior-tail word is appended. The proved subroot estimate in
`../MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md`
gives its actual length

    L <= W+2HB+2(5H-1)nu_H(P_r)=W+o(W).            (1)

The construction uses these literal kinds of letters:

* An erosion letter is the intersection of at most H+1 consecutive
  rank-(r+1) Johnson owners, allowing constant endpoint repetitions.
  It has size at least r+1-H.
* A lower cut-chart letter is P_(s,t), the intersection of s+t
  consecutive owners, with1<=s,t<=H. It has size at least r+2-s-t,
  hence at least r+2-2H.
* An upper chart letter is an original owner, of size r+1.
* Repeated collars use those same erosion letters or owners.

These facts follow directly from Lemma22.1 and the literal staircase
letters in `../MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md`.
Each Johnson step removes only one coordinate of an initial owner.
No residence estimate is needed for these size lower bounds.

Consequently EVERY letter of the actual word in(1) has size at least

    d=r+2-2H.                                    (2)

Concatenating paths, charts, and cycles cannot change this assertion.
Treating the completed linear word as a cycle cannot change it either.

## 2. Exact aggregate holes of this actual word

A nonempty interval union contains each of its letters. Thus a word
whose letters all have size at least d has NO target of size below d,
including intervals crossing joins or a cyclic seam. In particular,
the PBBS word in(1) has at least

    h >= sum_(j=1)^(r+1-2H) binom(2r+1,j)
      >= 2^(2r)-1-(2H-1)W                        (3)

nonempty holes. The second inequality removes at most2H-1 ranks from
the exact lower half of the odd-dimensional cube and bounds each by W.
Since W/2^n=Theta(1/sqrt(r)),

    h/2^n >= 1/2-o(1).                           (4)

This does NOT claim that all upper targets are covered. They may give
additional holes. Equation(4) is already enough to show that this
particular W+o(W)-length word is not a density-almost-cover.

The special depth-two word of Section19, of length W+4B, makes the
same issue especially transparent: every one of its letters has size
r-1, so every nonempty rank below r-1 is absent.

## 3. Exact endpoint bound after arbitrary small edits

Consider ANY nonzero linear or cyclic word on n coordinates. Suppose
all but b of its positions have letters of size at least d. There is
no restriction on the other b letters or on where they are placed.
For every j<d, any interval realizing a j-set must use only these b
exceptional positions: one large letter would already exceed j.

At a fixed right endpoint, all interval unions form a nested family.
Thus distinct targets of the same rank need distinct right endpoints.
Every such endpoint is exceptional, proving the finite inequalities

    number of covered j-sets <= min{b,binom(n,j)},
    h >= sum_(j=1)^(d-1) [binom(n,j)-b]_+.         (5)

The cyclic statement uses intervals of at most one period; growing
backward intervals from a fixed endpoint remain nested. A longer
interval has the whole-period union and cannot give an additional
proper small target.

In particular, start with the PBBS word in(1), and insert or replace
at most b letters by arbitrary nonempty sets. Allow arbitrary deletions
and reorderings of the unmodified large letters as well. Formula(5)
still applies. It is not limited to an append-only word or separate
repair gadgets.

If b=o(W) and H=o(sqrt(r)), (5) gives

    h >= (1/2-o(1))2^n.                           (6)

Here is a direct proof of the aggregate limit. Fix A>0 and count only
ranks from r-floor(A sqrt(r)) through d-1. They contain the lower
half of the cube except a binomial tail of probability O(A^(-2))
and O(H) central ranks of total probability o(1). There are O(A sqrt(r))
such ranks; subtracting b at each loses O(A sqrt(r)b)=o_A(2^n).
First let r tend to infinity and then A tend to infinity. The tail
estimate is elementary Chebyshev for Bin(2r+1,1/2), whose variance is
(2r+1)/4. No local limit or numerical tail estimate is required.

## 4. A density-almost-cover must replace almost the entire alphabet

There is a stronger qualitative consequence. Suppose a word of length

    L<=(1+o(1))W

has h=o(2^n) holes, and let b be its number of letters with size below
d=r+2-2H, where H=o(sqrt(r)). Then

    b>=(1-o(1))W.                                (7)

To prove this, suppose b<=(1-epsilon)W along a subsequence for some
fixed epsilon>0. Choose a fixed a>0 sufficiently small. The elementary
adjacent-rank product bound, or the central-binomial estimate already
proved in the master, gives uniformly for0<=q<=a sqrt(r)

    binom(2r+1,r-q)>=(1-epsilon/2)W

for all sufficiently large r. The interval2H-1<=q<=floor(a sqrt(r))
contains(a+o(1))sqrt(r) ranks below d. Each contributes at least
(epsilon/2)W to(5). Since W sqrt(r)=Theta(2^n), this yields a positive
liminf for h/2^n, a contradiction.

Combining(7) with L<=(1+o(1))W shows that only o(W) letters of such an
almost-cover can have size at least d. Therefore retaining ANY positive
fraction of the original subroot PBBS letters is incompatible with both
the near-width length budget and vanishing aggregate hole density.
A successful modification must replace almost all of that alphabet;
merely adding o(W) seam, tail, or repair letters cannot suffice.

This is an obstruction to retention of these actual large letters.
It does not say PBBS owner information cannot be reused to construct
different, much smaller letters.

## 5. Relation to the user's completion theorem and the open gate

`USER_FINITE_CYLINDER_COMPLETION_WITHOUT_DIMENSION_FLOOR_20260908.md`
removes the dimension-only error floor for an actual partial word with
small hole density eta. Equations(3)-(6) show that the existing
unconditional subroot PBBS word, even after o(W) arbitrary letter
changes, has eta bounded below by1/2-o(1). The new finite estimate
therefore cannot supply coefficient one from this particular input.

The prior subroot/tail note proves a length lower bound for a separately
appended exterior word. The obstruction here is different and stronger
for the proposed partial-word shortcut: it bounds actual aggregate holes,
allows all incidental interval coverage and arbitrary joins, and gives
the bulk-replacement necessity(7).

No missing shadow-support theorem has been assumed: the full PBBS turn
support is already proved. What fails for this concrete cheap word is
that its emitted letters are all too large for the lower Gaussian half
of the cube. Neither the open abundance/packing assertion nor a deep
erosion's actual hole count has been proved here. No new full-cube upper
coefficient is asserted.
