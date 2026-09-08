# Literal19: fixed-Phi Hamilton carrier and an actual pair-changing compiler

2026-09-09. One bounded deterministic structural reconstruction by
`exact_equality_structure`, read in full by root and independently by
`exact_b_finite_frontier` before root authorized execution.

**PASS.** The supplied 92,381-letter word consists of one 92,378-letter
cyclic period plus its first three letters. Its cyclic triples and four
windows give the complete two middle layers exactly once. The outgoing
matching is precisely the canonical Phi, while 70,452 incoming edges
differ from the pinned canonical PBBS factor. Its actual caps preserve
every triple but change 12,654 pairs, supplying 11,324 targets below
rank eight that have no literal witness anywhere in the period.

All 169,765 targets of ranks one through eight were independently checked
here by their actual one- or two-letter witnesses. Full-cube universality
and the matching endpoint lower bound are recorded by root/frontier's
separate full-word verification; this note does not replace that audit
with middle-layer or low-rank counts.

## 1. Inputs, execution, and complete artifacts

The supplied word is
[`answers/k19_optimal92381.word`](../answers/k19_optimal92381.word), SHA-256

    1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414.

The directly existing canonical file was

    /home/amodo/exact-b-k19-height-adaptive-20260908/height_adaptive_canonical_cycles.json

with SHA-256

    5e44113db3152b216af7761766f69a7b389db54b5c1f5dce9ac227ba6e6e71cd.

The exact executed source is
[`k19_literal_structure_20260909/checker.py`](k19_literal_structure_20260909/checker.py),
SHA-256

    4db31c92fd839768205d10a1e0a2168a9a7520215e466b4aca0537ea125627d7.

It ran exactly once on h100 (`arboghast`), in 2.659485 seconds, under
60 CPU seconds, 90 wall seconds, 2 GiB address space, and 1 GiB per output
file. There was no search, trial switch, retry, relabeling attempt, or
word edit. The existing canonical input was parsed directly; no new PBBS
factor was generated. Actual Phi agreement was a diagnostic rather than
an assumed input condition.

The complete output bundle is
[`scratch/k19_literal_structure_20260909/`](k19_literal_structure_20260909/).
Every copied JSON file passed its remote SHA-256 manifest locally.
The exact certificate is
[`literal19_structural_reconstruction_certificate.json`](k19_literal_structure_20260909/literal19_structural_reconstruction_certificate.json),
SHA-256

    68c2187cd9ec3d7ccf14c35588265e32fb96daacafe48e63d1325b3f2e02c566.

The bundle also retains the execution log, all named carrier rows, every
lower short witness, complete literal/pair mask sets by rank, all changed
pair positions, all incoming alternating circuits, all recovered rotation
rows, and the two empty violation lists. No output family was omitted.

## 2. Literal phase and the complete middle carrier

Let A be the supplied linear word and let C=A[:92378]. Direct equality
checks give

    A=C followed by C_0,C_1,C_2.

With all indices of C interpreted cyclically, define

    R_i=C_i union C_(i+1) union C_(i+2),
    U_i=C_i union ... union C_(i+3).                       (2.1)

The 92,378 R_i are distinct rank-nine masks, and the 92,378 U_i are
distinct rank-ten masks. Since both layer sizes are 92,378, each list is
a bijection onto its complete layer. Every consecutive pair satisfies

    R_i union R_(i+1)=U_i,
    U_(i-1) intersect U_i=R_i.                            (2.2)

Therefore the alternating list

    R_0,U_0,R_1,U_1,...,R_(92377),U_(92377)

is one Hamilton cycle of the nineteen-cube's middle-level graph. This is
a fact recovered from the literal word, not an invocation of an arbitrary
middle-level Hamiltonicity theorem.

Put

    E_i=U_(i-3) intersect U_(i-2) intersect U_(i-1) intersect U_i.
                                                                 (2.3)

The exact phase is

    C_i subseteq E_i,
    E_i union E_(i+1) union E_(i+2)=R_i,
    E_i union ... union E_(i+3)=U_i.                       (2.4)

These identities were checked on all actual masks, including wraparound.
There is no index shift under convention (2.1). For the general proof,
each factor in (2.3) contains C_i. Each of E_i,E_(i+1),E_(i+2) is contained
in U_(i-1) and U_i, whose intersection is R_i by (2.2). This sandwiches
their union between R_i and itself. The four-window identity follows
by taking the union of two neighboring triple identities.

Every E_i has rank seven and every E_i union E_(i+1) has rank eight.
Lowering the envelopes E_i to the supplied C_i preserves EVERY triple
and hence every cyclic interval of length at least three: a longer
interval is the union of its contained triples. The compilation changes
some pairs; preserving every pair was deliberately not imposed.

## 3. Fixed Phi and actual residence

For a rank-nine binary mask R on nineteen sites, take the FIRST index
attaining the global minimum of its ones-minus-zeros prefix walk. It is
the cyclic unmatched zero. Phi(R) adds that coordinate. This is the exact
gauge established in
[`PBBS_PHI_LEXICAL_MATCHING_AND_PUBLISHED_HAMILTON_RESIDENCE_AUDIT_20260909.md`](PBBS_PHI_LEXICAL_MATCHING_AND_PUBLISHED_HAMILTON_RESIDENCE_AUDIT_20260909.md),
Section 3.

The literal carrier satisfies

    U_i=Phi(R_i) for EVERY i.                             (3.1)

There are zero fixed-Phi violations. If b_i and d_i are the inserted
and deleted singleton labels in R_i to R_(i+1), both exclusions hold:

    b_i != d_(i+1),   b_i != d_(i+2) for every i.           (3.2)

Thus this concrete Phi-containing Hamilton carrier also has the required
two-step residence. It is outside the standard book-proof pull family
audited in the cited note, whose outputs have a one-position positive
run. No assertion about all-r existence of carriers satisfying (3.1)
and (3.2) follows from this one instance.

The individual triple-deficit pins have sizes one at 15,561 positions
and two at 76,817 positions. Every actual C_i contains its required
pin. The compiler check uses the actual simultaneous caps and every
triple identity; it does not infer simultaneous preservation merely
from each individual pin containment.

## 4. Complete lower compiler and genuine global pair credit

The exact short-target census is:

| Rank | Distinct literals | Distinct pairs | Literal/pair overlap | Distinct total | Pair-only |
|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 0 | 0 | 19 | 0 |
| 2 | 171 | 0 | 0 | 171 | 0 |
| 3 | 969 | 0 | 0 | 969 | 0 |
| 4 | 3,857 | 19 | 0 | 3,876 | 19 |
| 5 | 11,438 | 228 | 38 | 11,628 | 190 |
| 6 | 26,030 | 1,178 | 76 | 27,132 | 1,102 |
| 7 | 40,375 | 11,210 | 1,197 | 50,388 | 10,013 |
| 8 | 0 | 75,582 | 0 | 75,582 | 75,582 |

Every total equals the entire binomial layer. All 169,765 masks have an
actual ordinary one- or two-letter witness inside A, and each witness
was directly replayed. Since every triple of A has rank nine, no interval
of length at least three can supply a missing target of rank at most
eight. The table is therefore the exact complete mechanism for these
ranks, not a partial sample or a count-only plausibility check.

All occurrence counts here refer to the cyclic period C; the three
copied collar letters add no new literal or pair labels. There are
92,378 period literal occurrences and 82,859 distinct literal labels.
Exactly 12,654 pairs shrink from their rank-eight envelope union. Their
occurrence ranks are

    rank4:19, rank5:228, rank6:1178, rank7:11229.

The remaining 79,724 pair occurrences still have rank eight and supply
all 75,582 rank-eight targets. The complete pair set contains 88,217
distinct labels.

Crucially, the pairs supply 11,324 targets of ranks at most seven that
occur NOWHERE as a literal. This is global, not merely the local fact
that each is a proper union of its two witness letters. The exact
capacity identity is

    94,183 - 82,859 = 11,324
                    = (94,183-92,378) + (92,378-82,859).
                                                                 (4.1)

Thus the pair-only labels pay for both the 1,805-position deficit below
the rank-seven literal-only count and the 9,519 repeated literal
occurrences. The actual census resolves the double-credit concern from
the earlier proper-pair reservation discussion: these 11,324 labels are
verified disjoint from the full actual literal palette.

A rank-eight-pair-preserving compiler could not do this, since every
pair would then stay rank eight and every target below eight would need
a literal. The actual pair-changing compiler is therefore a substantive
construction feature needed at nineteen, not an optional normalization.

## 5. Exact comparison with the existing canonical PBBS factor

The pinned canonical factor has 360 components. After naming each
lower vertex by its actual rank-nine mask, define its two incident
upper matchings as in the previous seventeen-coordinate comparison.
The canonical outgoing matching is independently checked to be Phi.

For the literal carrier:

    canonical outgoing edges changed:       0;
    canonical incoming edges unchanged: 21,926;
    canonical incoming edges changed:   70,452.

The unordered two-edge incidence sets share one edge at 70,452 lower
vertices and both edges at 21,926 lower vertices. Thus the result is
independent of a hidden component phase choice.

The difference of the incoming perfect matchings is a permutation on
named lower masks. It has 1,755 nontrivial alternating circuits with
the following exact length/multiplicity census:

    3:1216, 5:399, 6:38, 7:38, 9:19, 11:19,
    361:1, 684:1, 690:19, 1178:1, 2166:1,
    2945:1, 21147:1, 22344:1.

All circuits, old/new upper masks, common cores, active coordinates,
and touched native component/height labels are saved. No circuit was
tried as a surgery. This is a comparison with the specified canonical
PBBS input only; it does not identify the number of edits relative to
an unprovided intermediate generator or certificate.

## 6. Recovered 4,862 rotation rows

All rank-nine masks have nineteen-element rotation orbits. The exact
orbit count is 4,862. The following named fields have ZERO rotation-
equivariance violations:

    successor, outgoing matching, incoming matching,
    literal cap, envelope, individual triple pins.

One representative per orbit therefore determines the full labelled
carrier and its cap assignment. The saved quotient includes the actual
successor orbit and rotation shift, literal/envelope/pin values, and
the positions of all nineteen orbit members in the supplied period.
The complete named carrier is also retained.

This is an exact quotient recovered from the actual literal. Its phase
is inherited from that literal. It is not a reproduction of an absent
compact-generator program, nor a search certificate for why this
particular incoming matching was selected.

## 7. Consequence for the constructive goal

The finite success has three simultaneously verified ingredients:

1. one complete Phi-containing Hamilton carrier with the two-step
   residence exclusions;
2. a rotation-equivariant cap of its rank-seven envelopes preserving
   every middle triple and every longer source interval;
3. genuinely new pair-only lower labels, together with a complete
   literal/pair allocation of every target below the middle layers.

These properties explain the actual nineteen-coordinate mechanism.
They do not imply the same carrier or cap allocation exists in every
dimension. The earlier canonical-chronology cap obstructions remain
scoped to their frozen sources; the new incoming matching changes
70,452 named edges and is not such a frozen source.

All outputs have been copied and inspected, and no mathematical job
remains live. The next all-dimensional step is a theorem generating
compatible carriers and pair-changing lower allocations, not an
additional replay of this already checked instance.
