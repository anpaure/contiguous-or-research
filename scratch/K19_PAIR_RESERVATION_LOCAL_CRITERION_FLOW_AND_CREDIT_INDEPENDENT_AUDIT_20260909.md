# Independent audit of genuine pair reservations at k19

Date: 2026-09-09. Pure-proof review by `exact_equality_structure` of
[the pair-reservation proposal](K19_GENUINE_PAIR_RESERVATION_LEMMA_AND_NEXT_FINITE_GATE_20260909.md),
read in full. No flow, cap census, solver, or mathematical program was
executed or authored for this audit.

**Verdict:** the local proper-pair criterion, the independent-frame
triple preservation, and the integral block/target/old-rank-eight-label
flow are correct under the stated source and frozen-palette hypotheses.
One capacity interpretation needed correction: a locally proper pair
does not imply that its target is absent from literals elsewhere.
With root's authorization, the original note now states that distinction
and the exact corrected fixed-literal credit ledger below.

## 1. Exact local triple-preservation criterion

For six distinct consecutive cyclic positions, or six positions in a
linear source, write the letters as `A,B,L,R,C,D`. Replace only the
middle two by caps `E subseteq L`, `F subseteq R`. Exactly four triples
meet an edited position. Their equality with the originals is equivalent
to

    L minus (A union B) subseteq E,
    R minus (C union D) subseteq F,
    (L union R) minus B subseteq E union F,
    (L union R) minus C subseteq E union F.

Caps cannot introduce any new coordinate into those triples. Thus the
displayed conditions are both necessary and sufficient, proving the
proposal's `P,Q,G` formulation. Nonempty E,F remain a separate literal
requirement, supplied by its proper-pair construction.

Keeping every triple keeps every longer interval: its original OR is
the union of its consecutive triple ORs. This preserves all existing
triple/longer witnesses, not arbitrary lost singleton or pair witnesses.
Full upper coverage follows only if that original source bank was
already proved to cover the corresponding targets.

## 2. Exact two-proper-subletter criterion

Assume `P subseteq L` and `Q subseteq R`. Nonempty proper subsets
`E,F` of S with

    P subseteq E subseteq L,
    Q subseteq F subseteq R,
    E union F=S

exist if and only if

    P union Q subseteq S subseteq L union R

and there are distinct coordinates

    a in (S intersect R) minus P,
    b in (S intersect L) minus Q.

For necessity, take `a in F minus E` and `b in E minus F`; the proper
inclusions and union equality ensure both differences are nonempty.
For sufficiency, the displayed construction

    E=(L intersect S) minus {a},
    F=(R intersect S) minus {b}

keeps every mandatory coordinate. It covers every coordinate of S:
a remains in F and b in E, because they are distinct. It also gives
`b in E minus F` and `a in F minus E`, so E and F are nonempty,
different from each other, and both proper subsets of S. This includes
the cases where a or b was already absent from the opposite shore.

The two candidate coordinate sets admit a distinct ordered pair exactly
when they are both nonempty and their union has size at least two.
For the arbitrary-source triple criterion, the additional requirement
`G subseteq S` is sufficient and necessary because S is the final pair
union. The rank-seven/rank-eight PBBS specialization is correct when
both private coordinates are pinned: S must delete one shared coordinate
that is pinned on neither shore, and the two maximal caps have rank six.

## 3. Simultaneous frame and source hypotheses

Two fixed positions between neighboring editable pairs ensure that no
triple meets both pairs. The generic local proofs therefore combine
without an interaction assumption.

The stronger one-anchor PBBS frame is justified differently. Its
source-run/pin theorem is an explicit premise, and the proposal also
requires a direct test of the word with all editable positions set to
their minimum pins. If that minimum word and the original word have
equal triples and equal anchor-boundary pairs, every intermediate cap
choice has the same unions by coordinatewise monotonicity. This one
global minimum test proves simultaneous compatibility even for triples
meeting editable positions on both sides of an anchor.

The test must concern the actual proposed source, including cyclic
wraps. It is not enough to import pins or rank formulas from a different
chronology. Selected proper pairs are nonempty by Section2, and unused
positions remain their original nonempty letters.

## 4. The reservation flow is integral and exact for its stated subproblem

Each target S has capacity one, each editable block capacity one, and
each original rank-eight label V has capacity `b_V` if there is a frozen
witness or `b_V-1` otherwise. The stated complete rank-eight palette
premise ensures the latter is nonnegative. The network has integral
capacities, so an integral maximum flow exists.

An integral path chooses one target and one block. Its local criterion
constructs actual two-letter caps; the independent-frame test makes
all selected choices coexist. A selected internal pair changes from
rank eight to rank seven, while every boundary pair remains unchanged.
The V capacities keep at least one old internal or frozen witness
for each required rank-eight label. Thus every flow gives precisely the
claimed reservation bank.

Conversely, an assignment in that architecture selects distinct targets
and blocks, and cannot displace all b_V occurrences of an unfrozen V.
It therefore supplies a flow of the same value. There is no unmodeled
shared cap variable between blocks and no simultaneous literal-target
assignment being claimed. This is why the ordinary flow is exact here,
unlike the earlier coupled multi-output block menus.

The result preserves the specified complete rank-eight palette and all
native rank-nine triples and longer windows. It may lose old rank-seven
literal targets. It does not provide complete rank-seven or smaller
coverage, nor a legal opening of the cyclic bank into B(19) positions.

## 5. Corrected credit ledger: local properness is not global novelty

The selected S is different from its own two subletters, but may be a
literal at another position. In particular a frozen anchor can already
contain exactly S. Counting such a reservation as one globally additional
low target would double-count its benefit.

Here is an exact necessary ledger for the proposed subsequent stage
in which the reserved pair labels form T and every other low target
must be supplied literally. Let P be the number of H3 positions, F
the frozen H3 positions after reservations, and L_F their set of distinct
literal labels. All these literal labels have rank at most seven.
The unserved target set has size

    94183 - |T union L_F|.

It must fit in `P-|F|` free literal positions. At the specified canonical
bank P=87514, this is equivalent to

    |T minus L_F| >=6669 + |F|-|L_F|.                  (5.1)

Thus both overlaps with fixed literals and repeated fixed literal labels
cost capacity. Before flow, use only the permanent original anchors and
unchanged one-slot blocks as F_0. Candidate pair labels already in L_F0
have zero credit toward this necessary condition; filtering them and
using threshold `6669+|F_0|-|L_F0|` gives a concrete initial gate.

After selecting pairs, both of their actual subletters are frozen and
must be added to F. Their duplicates can strengthen(5.1), so the final
ledger must be recomputed. Passing it still does not supply literal
host eligibility, injection, or the common cap assignment. If a later
compiler creates other short-pair outputs, add their actual labels to T
before using the same inequality; the ledger is not a no-go theorem
for unrestricted pair-changing compilers.

The original proposal has been amended in Section3, new Section6.1 and
its proposed finite-gate steps to avoid claiming that raw flow value
6669 solves this deficit. This correction does not affect the proper-pair
lemma or the exact flow theorem for selecting reservations.

## 6. Is the proposed finite gate useful?

Yes, with the corrected credit test and its source premises verified
first. It releases internal rank-eight pairs while protecting their
labels elsewhere, which is excluded by the already refuted pair-frozen
compiler. It is a different dimension and source from the completed
canonical17 cap obstructions, so those do not decide this instance.

A deficient filtered flow would rule out this particular reservation
frame and subsequent literal-only remainder model. A sufficiently large
filtered flow with a passing post-selection ledger would provide actual
protected pairs and a concrete residual common-allocation problem.
Neither outcome settles an unrestricted k19 carrier, all lower targets,
the cyclic-to-linear opening, or the all-dimensional exact objective.

No proposed flow has been run or authorized by this audit.
