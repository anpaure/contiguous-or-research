# Ordered overlapping refinements and simultaneous context certificates

Date: 2026-09-09. Status: pure-proof PASS with the boundary and disjoint-
operation hypotheses below. No execution or edit-schedule replay.

This audits the exact formulas transcribed by the root. The reported
644-edit optimization trace was not supplied and is not certified here.
Independent verification of the supplied final words is a separate task.

## 1. Ordered overlapping representations preserve every old interval OR

Let A_1,...,A_m be nonempty old letters, m>=1, and F_1,...,F_n a nonempty
new word. Suppose each old letter has a nonempty interval representation

    union_(j=l_i)^(r_i) F_j = A_i,

with l_i and r_i nondecreasing, and

    l_(i+1) <= r_i+1.

The intervals may overlap or touch. For every a<=b, their union is exactly
[l_a,r_b]: monotonicity fixes its endpoints, and the displayed condition
leaves no gap. Therefore

    union_(i=a)^b A_i = union_(j=l_a)^(r_b) F_j.         (1.1)

No disjointness or strict endpoint ordering is required inside this
representation. The assertion preserves OR values; it does not claim
an injective map on all old physical intervals with possibly equal values.

When this replaces a block inside a larger word, require additionally

    l_1=1,       r_m=n.                               (1.2)

These conditions preserve old block prefixes and suffixes at the actual
new block boundaries. An old interval inside the block uses (1.1); an
interval entering from the left or leaving to the right uses the matching
new prefix or suffix; one crossing the whole block uses its full union.
Thus the replacement preserves every interval-OR target in ANY unchanged
external context. Without (1.2), extra unrepresented new boundary letters
could contaminate a crossing interval; they may not be silently included.

This generalizes the retained disjoint single-letter split construction
and its boundary-fragment normal form in
[the split-letter theorem, Section1](../MATH_THEOREM_H2_SPLIT_LETTER_SOURCE_SUPPORT_RESET_AND_ESSENTIAL_BOUNDARY_OBSTRUCTION_20260801.md).
Here the old letters can instead have ordered OVERLAPPING new interval
representations. Existence of such representations is an input to (1.1).

## 2. Exact nonempty pair inflation

Seek nonempty F_0,...,F_m satisfying

    F_(i-1) union F_i = A_i,       1<=i<=m.             (2.1)

Such a factorization exists if and only if

    A_i intersect A_(i+1) is nonempty, 1<=i<m,
    A_i subseteq A_(i-1) union A_(i+1), 2<=i<m.        (2.2)

Necessity: each internal F_i is a nonempty subset of A_i intersect
A_(i+1). Each interior A_i is supplied by its two factors, contained in
the two neighboring A letters. For sufficiency take the maximal factors

    F_0=A_1,  F_m=A_m,
    F_i=A_i intersect A_(i+1), 1<=i<m.                 (2.3)

The endpoint pair unions are immediate; the interior pair union equals
A_i intersect (A_(i-1) union A_(i+1))=A_i. Every factor is nonempty by
(2.2) and the original nonempty-letter assumption. For m=1 the conditions
are vacuous and F_0=F_1=A_1 works; m=2 only needs its one nonempty
intersection.

The intervals [i-1,i] satisfy Section1 and cover both new boundaries, so
all old interval ORs survive. Attribution: this is exactly the depth1
specialization of the already proved maximal flat compiler in
[MASTER_HANDOFF Section3.2](../MASTER_HANDOFF.md), including its truncated
endpoint factors and nonempty-intersection criterion. It is not a new
general factorization theorem.

## 3. Safe insertion at one original gap

Between A_i and A_(i+1), insert a nonempty X satisfying

    X subseteq A_i union A_(i+1).                      (3.1)

An old interval not crossing that gap is unchanged. The expanded witness
for an interval crossing it contains both neighboring old letters, whose
union already contains X. Thus every old OR survives. Nonemptiness of X
is needed when the output is required to remain a nonempty-letter word.

Distinct insertions in consecutive original gaps are allowed: the
unchanged middle old letter can be shared by the two gap descriptions.
Each crossed inserted letter is contained in the two old neighbors also
present in the expanded interval.

## 4. Simultaneous disjoint operations preserve all local certificates

Fix operations on the ORIGINAL word with these hypotheses:

1. Selected replacement blocks are pairwise disjoint as old position
   intervals. Each has a representation satisfying Sections1 and (1.2).
2. Insertions use distinct original gaps. NEITHER old neighbor of an
   insertion gap lies in any selected replacement block, and (3.1) holds.
3. Every claimed local target has a genuine ordinary-interval witness
   when its own operation is performed alone in the original word.

The local certificates in condition3 may be wholly internal new intervals,
old left suffixes joined to new prefixes, new suffixes joined to old right
prefixes, or intervals using both contexts. In the last case the interval
necessarily contains the ENTIRE intervening new block. A noncontiguous
selection of a middle subblock and both contexts is not such a certificate.

All operations commute as edits of identified original blocks and gaps.
Adjacent replacement blocks simply concatenate their new words. Distinct
consecutive insertion gaps share only an unchanged old letter. The guard
in condition2 prevents an insertion inside or immediately beside an
edited block from changing its local source or boundary description.

Each replacement preserves every interval OR of the current word in its
arbitrary exterior context, by Section1. Its old source block is still
unchanged when that operation is performed, because the blocks are
disjoint. Each insertion likewise preserves every current interval OR:
its two original neighbors still occur unchanged and adjacent at that
particular unfilled gap. Other distinct insertion gaps do not alter this.

Now fix ANY locally certified target S and order the operations with its
own focal operation first. Its certificate is then valid in the original
context. Every later operation preserves S. Since the final word is
independent of the operation order, this proves S appears in the same
final word as every other certified target. It also proves all original
targets survive. This argument permits the certified witness contexts to
overlap and to cross other replacement blocks; it does not require their
old absolute endpoint indices to remain unchanged.

The original REPLACEMENT BLOCKS must still be disjoint under this theorem.
Overlapping interval representations inside a block and overlapping
certificate contexts do not authorize conflicting edits to one original
position. This statement is also different from the common-cap theorem
for simultaneous overlapping target assignments in
[the exact short-target note, Section4](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md),
which checks shared-letter feasibility instead of applying independent
target-preserving operations.

## 5. The endpoint budget still constrains every transported witness

The old endpoint theorem states that if an N-letter word represents M_s
distinct rank-s targets, EVERY interval realizing one of those targets has
length at most N-M_s+1. To include a particular interval in the proof,
select it as that target's witness and then complete the equal-rank
witness family. The common containment argument gives the length bound.
It is not merely a bound on the shortest witness for each target.

Consequently, if the final refined F is universal and an old rank-s
interval [a,b] is transported as [l_a,r_b], then necessarily

    r_b-l_a+1 <= N-binom(k,s)+1.                       (5.1)

For exact dimension21 at s=11, N=B(21)=binom(21,11)+3, the right side is4.
An old four-letter rank11 witness transported to a five-position interval
therefore rules out exactness for THAT final refinement. An alternative
shorter witness does not remove the violation. Later operations would
have to shorten or change that particular transported interval if the
bound is to be avoided.

This uses the existing endpoint theorem; it is not a claim that the new
353094 word cannot be improved, that every refinement fails, or that a
general exact construction is impossible. The verified upper words and
any unprovided644-edit schedule remain separate factual questions.

## 6. Audit result

All transcribed general claims pass with their explicit nonempty-word,
boundary, original-block disjointness and insertion-gap guards. The
simultaneous proof above covers adjacent replacement blocks and
consecutive insertion gaps. No optimizer, specific edit schedule,
numerical outcome or new literal word was replayed by this audit.

