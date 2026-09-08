# Standalone k=17 endpoint lower bound and literal optimality interface

2026-09-08. Independent pure-proof audit by `exact_b_induction` of the
supplied text at
`/Users/amir.nuriyev/.codex/attachments/75a4f2eb-4f95-4711-8ce2-041c4ed52851/pasted-text.txt`.
The entire text was read. No mathematical program was run by this
reviewer. The lower bound and the five displayed seam identities pass.
Root's separate h100 literal-word verification has now also returned
PASS, as recorded below. Together these establish the exact finite
theorem nu(17)=B(17)=24,313 independently of PBBS or the construction
history. The all-dimensional equality conjecture remains open.

## Executed literal certificate received from root

Root independently checked the supplied file with
`scripts/verify_k17_optimal24313.py`. The completed report records:

* exactly24,313 nonempty letters;
* all131,071 nonempty target masks covered;
* all131,071 ordinary nonwrapping witness intervals independently
  replayed by a range-OR segment tree;
* endpoint lower bound24,313 and gap zero.

The verified word SHA-256 is

    7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9

The h100 report is
`/home/amodo/exact-b-k17-optimal24313-20260908/verification.json`, with
the local certificate bundle under `witnesses/k17_optimal24313/`.
Root reported a completed runtime of0.139 seconds. This execution is
attributed to root; it was not rerun by the present reviewer. It
certifies the literal upper bound. Ancillary quotient-generation and
two-block internal-census claims remain subject to the distinctions
in Sections3–4 below.

## 1. Definitions and the exact lower bound

A word is a finite sequence A_1,...,A_N of nonempty subsets of [17].
Its targets are unions of ordinary nonempty intervals [a,b], with
1<=a<=b<=N. Let nu(17) be the smallest length of a word whose targets
are all131,071 nonempty subsets. The proof below also allows empty
letters; forbidding them cannot weaken its lower bound.

Put

    W=binom(17,9)=24310,
    Lambda=sum_(j=1)^8 binom(17,j)=65535.

The second identity follows by complementing subsets of an odd
17-element set: ranks0 through8 contain exactly half the2^17
subsets; then remove the empty set.

For each distinct nine-set, choose one interval witness. Two such
witnesses cannot contain one another. Interval containment implies
containment of the corresponding unions, and distinct sets of equal
size cannot contain one another. Consequently their left endpoints
are all distinct. In particular N>=W; this first step handles every
putative length below W without introducing a negative parameter t.

Write N=W+t with integer t>=0. Order the W chosen witnesses as

    I_i=[ell_i,r_i],   ell_1<...<ell_W.

The right endpoints are also strictly increasing: if i<j but r_j<=r_i,
then I_j would lie inside I_i. Strictly increasing endpoint sequences
of length W in {1,...,N} satisfy

    i<=ell_i<=r_i<=N-(W-i)=i+t.                         (1.1)

Equivalently ell_i=i+alpha_i and r_i=i+beta_i, with
0<=alpha_i<=beta_i<=t.

Every VALID interval of length t+1 is [a,a+t] with

    1<=a<=N-t=W.

By(1.1), it contains I_a. Hence its union has rank at least nine.
Every longer interval contains its first t+1 positions, which are
one of these valid intervals, and therefore also has rank at least
nine. All Lambda targets of ranks1 through8 must consequently use
intervals of length at most t.

For t=0 this statement says there are no possible nonempty low-rank
witnesses. It is not an undefined sum or an omitted special case:
every singleton interval [a,a] contains I_a, so all its letters have
rank nine. The number of nonempty intervals of lengths1 through0
is the empty sum zero.

For every integer t>=0, the total number of nonempty intervals of
length at most t is

    sum_(j=1)^t (N-j+1)
      =tW+t(t+1)/2.                                     (1.2)

Distinct target sets require distinct witness intervals, since one
fixed interval has only one union. It follows that a universal word
must satisfy Lambda<=tW+t(t+1)/2. If t<=2, the right side is at most

    2W+3=48623<65535=Lambda.

This is impossible. Therefore, entirely independently of PBBS,
matching, recency, asymptotic, or solver arguments,

    boxed: nu(17)>=W+3=24313.                           (1.3)

The endpoint formula first permits t=3, since 3W+6=72936>=Lambda.
Thus this is the stated B(17)=24313 endpoint lower bound. This last
inequality alone does not supply an attaining word.

## 2. What a passing literal certificate proves

The delivered file has now passed the separate checks for exactly24,313
nonempty masks in the17-bit range and ordinary interval witnesses for
all131,071 nonempty masks. That finite word directly proves
nu(17)<=24313. Combined with(1.3), it proves

    nu(17)=B(17)=24313.

Only the literal letters and their verified ordinary witnesses are
needed for this implication. The assertion does not depend on the
user's quotient-search program, construction history, asymptotic
manuscript, or an unprovided generator certificate. The executed
literal report supplies the actual pass status and file hash; the
user's claimed counts were not substituted for those checks.

## 3. Exact two-block opening that can be checked from the word alone

The proposed opening has

    V=Q followed by Q_0,                |Q|=85, |V|=86,
    Z=R followed by R_0,R_1,            |R|=24225, |Z|=24227,
    final word=V followed by Z,         length24313.

From the delivered final word, using one-based positions, the claimed
pieces are recovered as

    Q=positions1..85,
    R=positions87..24311.

The three copied-letter assertions are exactly

    position86=position1,
    position24312=position87,
    position24313=position88.                           (3.1)

These equalities and the separate linear coverage sets of V and Z
are directly testable from the final word. If those internal sets
have union all nonempty targets except the five below, the displayed
seam witnesses finish an independent proof of the opening mechanism.
Neither separate block is required to retain its entire cyclic deck.

The supplied six-letter boundary is

    (19076,19106,8834 | 25249,689,12849),

which would occupy final positions84 through89. In hexadecimal its
letters are

    (4A84,4AA2,2282 | 62A1,02B1,3231).

Direct bitwise union gives:

| Target | Hex mask | Rank | Local interval | Final one-based interval |
|---:|---:|---:|---:|---:|
| 27299 | 6AA3 | 8 | [2,4] | [85,87] |
| 27303 | 6AA7 | 9 | [1,4] | [84,87] |
| 27315 | 6AB3 | 9 | [2,5] | [85,88] |
| 27319 | 6AB7 | 10 | [1,5] | [84,88] |
| 29363 | 72B3 | 9 | [3,6] | [86,89] |

Every interval crosses the boundary between positions86 and87 and
is an ordinary, nonwrapping interval. The hexadecimal popcounts give
the stated ranks. These identities are exact and were checked
symbolically in this audit.

If the internal-union census really omits exactly these five masks,
concatenation preserves every internal witness and the five seam
intervals supply the remainder. That is a complete two-block upper
proof. Independent verification of the internal sets is still required;
their claimed sizes639 and130,747, or the claimed union size131,066,
are not inferred merely from the six-letter identities.

## 4. Claims requiring additional artifacts or checks

The final word and its extracted Q,R pieces can in principle certify
the two periodic decks, their rank8/rank9 cyclic windows, the short
window table, and the joint opening by direct enumeration. None of
those needs a search transcript. However a literal full-coverage
check alone does not automatically certify every such ancillary count.

The1,430 rotation-quotient rows, successor shifts, fourteen reported
successor changes, and exact regeneration from the quotient require
the separate construction certificate and generator. They should not
be presented as independently replayed if that package has not been
supplied. The reference to the original P phase15,321 is likewise
a generator convention; the already rotated R extracted from the
final word is sufficient for the ordinary-word proof.

The all-k conjecture remains distinct. A verified24,313-letter
universal word closes exactly the k=17 case and extends known finite
attainment through17. It does not by itself establish nu(k)=B(k)
for every dimension.
