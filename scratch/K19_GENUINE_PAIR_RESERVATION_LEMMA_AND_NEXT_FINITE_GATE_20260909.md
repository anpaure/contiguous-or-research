# Genuine pair reservations for the next exact odd dimension

2026-09-09. Pure-proof investigation by `exact_b_finite_frontier`.
No mathematical program, flow, cap census, or new word search was run.

**Proposed next constructive step:** reserve distinct rank-seven targets on
actual two-letter intervals while retaining a specified rank-eight palette
and every native triple. The reservation problem below is an exact integral
flow once a source and independent two-position frame have been fixed.
It changes the pair-frozen lower compiler that is already ruled out at
k=19. It is not another one- or two-seam dimension lift.

## 1. What the new exact words do and do not provide

The supplied words establish nu(17)=24313 and nu(18)=48623. The exact18
structural record reconstructs the latter from a modified optimal17
initializer, a rotated reversed long cycle, and the reversed short cycle.
The initialized update number is lambda_17(P)=W(17)-1. This closes one
odd-to-even extension; it does not supply an even-to-odd exact induction.

The older [entrance/exit obstruction](EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md)
already excludes a bounded-piece exact19 lift. The older all-odd compiler
audit also already observes that k19 has 94,183 targets of ranks one
through seven, more than B(19)=92,381 positions. Thus keeping every pair
at rank eight cannot be a complete lower compiler. Neither fact is new
here and neither is being rerun.

The literal Q/R factor extracted from the new optimal17 word has complete
immediate lower and upper palettes, unlike the older failed K15-to-K17
factor. The existing Pascal diamond theorem can use such data only after
its separate incidence and compiler gates are supplied. Merely replacing
the parent in that theorem does not prove those gates. In particular,
there is currently no already certified single flat resident k19 carrier
of length B(19) to which a lower allocation may silently be attached.

The lemma below is a reusable zero-additional-position component for such
a carrier or for a rigorously specified cyclic bank. Its source hypotheses
are explicit so the two objects cannot be confused.

## 2. A two-position replacement preserving all triples: arbitrary source

Let a linear or cyclic source word have six consecutive letters

    A, B, L, R, C, D.

Only L and R are to be replaced, by nonempty E⊆L and F⊆R; the four
outer letters remain fixed. Assume that these six positions are distinct
in the cyclic case. Define

    P = L minus (A union B),
    Q = R minus (C union D),
    G = ((L union R) minus B) union ((L union R) minus C).

Then every native triple OR survives if and only if

    P⊆E, Q⊆F, and G⊆E union F.                         (2.1)

Proof: exactly four triples meet the edited positions. The first,
A union B union L, imposes P⊆E. The last, R union C union D, imposes
Q⊆F. The two middle triples impose respectively
(L union R) minus B⊆E union F and
(L union R) minus C⊆E union F. Caps cannot introduce an extraneous
coordinate, so these necessary conditions are also sufficient.

Preserving every triple also preserves every longer interval OR: an
interval of length at least three is the union of the triples contained
inside it. Therefore (2.1) preserves four-window middle owners, every
longer upper witness, and the native triple labels. It says nothing by
itself about smaller targets that lose a one- or two-letter witness.

For simultaneous use on an arbitrary source, one sufficient independent
frame separates every two editable two-position blocks by at least two
fixed positions. Then no triple meets two blocks, so the local proof
applies to all blocks at once. This generic statement does not infer the
stronger one-anchor independence available for a separately proved PBBS
source-run geometry.

## 3. Exact genuinely nonliteral pair criterion

The following abstract version applies to any independent two-position
cap menu. Let L,R be the original letters and let P⊆L,Q⊆R be required
subsets. A permitted replacement has

    P⊆E⊆L, Q⊆F⊆R.

For a prescribed target S, require E union F=S and require both E and F
to be proper subsets of S. The latter condition makes S an additional
pair output, rather than either of the two literal outputs. Such E,F
exist exactly when

    P union Q ⊆ S ⊆ L union R,                          (3.1)

and there are distinct coordinates

    a in (S intersect R) minus P,
    b in (S intersect L) minus Q.                      (3.2)

When these conditions hold, an explicit choice is

    E=(L intersect S) minus {a},
    F=(R intersect S) minus {b}.                        (3.3)

Proof of sufficiency: E contains P and F contains Q by (3.1)–(3.2).
Every coordinate of S is still in their union: the only deleted
coordinates a,b are retained respectively in F,E because they are
distinct and occur on those shores. E omits a and F omits b. Moreover
E contains b and F contains a, so both are nonempty. Their union S is
different from each literal, and the two literals are different from
one another. Thus this block supplies three distinct targets E,F,S.

For necessity, choose a∈F minus E and b∈E minus F from the two proper
inclusions. These sets are disjoint, so a≠b. Required-coordinate
containment gives a∉P and b∉Q, while availability gives (3.2).

The existence test in (3.2) is particularly cheap: its two displayed sets
must be nonempty and their union must have size at least two. No search
over all letter caps is needed. The least valid ordered pair (a,b)
provides a deterministic literal representative.

Here "nonliteral" is local to the two selected letters: S differs from
E and F. It can still equal a literal letter elsewhere in the bank,
including at a frozen anchor. A count of these pair reservations is
therefore not automatically a count of globally nonliteral targets.

For the arbitrary-source triple-preservation setting of Section2, add
G⊆S to (3.1). Then (3.3) preserves all four affected triples as well.

## 4. PBBS specialization and the exact independent frame

This section is conditional on a supplied and checked cyclic bank with
the following data; it does not assert a single exact-length k19 word.

On every editable component, let D_i be a nonempty rank-seven source
letter, with every native adjacent pair of rank eight and every native
triple of rank nine. Let Pin_i be its mandatory source-run endpoints.
Assume the proved native-deck pin/gap criterion: every cap between Pin_i
and D_i preserves all triples whenever every three consecutive positions
contain a full anchor. The criterion and its PBBS derivation are in
[the exact short-cap theorem](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md),
Sections5–6. The present application must independently check that its
source satisfies those hypotheses.

Fix anchors at positions0,3,6,... in each given cyclic component. The
last cyclic gap is at most three. Each intervening editable block has
one or two positions; leave one-position blocks unchanged and use only
the two-position blocks. With full anchors, any choices
Pin_i⊆E_i⊆D_i at the editable positions simultaneously preserve all
triples. Also require the separately checkable boundary-pair property:
every native pair touching an anchor keeps its old union for all these
caps. For the retained PBBS source this follows because the difference
between adjacent native letters is a pinned private coordinate.

There is also a direct finite certificate that avoids importing any
run-geometry argument: set every nonanchor letter simultaneously to its
Pin_i and every anchor to D_i. If this single minimum word reproduces
every native triple and every boundary pair, then every intermediate
choice does too, by coordinatewise monotonicity between the minimum and
the original source. The proposed diagnostic requires this literal test.

For a two-position block use L=D_i,R=D_(i+1),P=Pin_i,Q=Pin_(i+1).
Generate rank-seven S satisfying Section3. Its old internal pair
V=L union R has rank eight. Every such replacement changes only this
internal pair among the rank-eight pair occurrences; all boundary pairs
are unchanged. All native triples and all longer cyclic interval ORs
remain exactly as before.

In the graded PBBS case each shore has seven coordinates and the pair
has eight, so each shore has a private coordinate. Both private
coordinates are pinned. Hence any admissible rank-seven S must be
obtained by deleting one shared unpinned coordinate from V; both maximal
caps L intersect S and R intersect S then already have size six and
are proper subsets of S. This is a useful specialization of the general
criterion, to be checked against the literal source rather than assumed
for an arbitrary word.

## 5. Zero-additional-position pair reservation by integral flow

Assume that before editing, every rank-eight target has a native witness
either among these internal pairs or in the frozen part of the bank.
The frozen part includes boundary pairs, untouched components, and any
other explicitly retained rank-eight witnesses. This palette premise
must be checked independently; it is not implied by the word "bank".

For each rank-eight label V, let b_V be the number of editable two-letter
blocks whose original internal pair equals V. Define

    c_V=b_V       if V has a frozen witness,
    c_V=b_V-1     otherwise.                           (5.1)

An absent frozen witness then implies b_V≥1, so the capacity is
nonnegative. The subtraction reserves at least one unchanged occurrence
of V when all its witnesses lie in the editable internal pairs.

Make an integral flow network:

1. Source to each candidate rank-seven target S, capacity1.
2. S to editable block j, capacity1, exactly when the genuine pair
   criterion of Section3 is satisfied in that block.
3. Block j to its original rank-eight label V_j, capacity1.
4. V to sink, capacity c_V.

An integral flow of value q constructs q distinct protected rank-seven
pair targets at q distinct blocks. Use (3.3) at a selected block, with
its assigned target S; leave all other letters full. The independent
frame proves every native triple and upper interval survives. The group
capacities prove that every old rank-eight target retains a witness.
Each selected pair target is actually supplied by its two adjacent
letters, both proper subsets of it, at zero added positions.

Conversely, every assignment in precisely this architecture—one distinct
rank-seven reservation per selected block and a retained original or
frozen witness for every displaced rank-eight label—gives a flow of
the same value. Thus a single integral max-flow is an exact decision
for this pair-reservation subproblem. It is not merely a necessary
channel-capacity relaxation and needs no configuration-consistency
solver afterward: each selected block has an explicit local realization,
and the blocks are independent by hypothesis.

This does NOT guarantee that all rank-seven targets or smaller targets
survive. In particular selected blocks can lose their old literal labels.
Their replacement or reservation belongs to the next global lower
allocation. A reserved pair label is allowed to serve as that label's
fixed witness in such a subsequent allocation; later edits must keep the
selected two letters fixed. The residual literal domains and all remaining
rank-seven obligations must then be rebuilt against the combined caps.
No count is being substituted for that remaining common-cap problem.

## 6. A useful fixed-bank capacity ledger

If the canonical height-adaptive k19 bank is capped at H=min(h,3) and
its H1/H2 components are frozen, only the H3 positions can serve targets
of ranks at most seven. There are 2^(r-1)=256 Dyck roots of height at
most two for r=9: a height-two word is a concatenation of primitive
components determined by a composition of r. Their 19 physical roots
therefore use 4,864 positions. The candidate H3 bank has

    W(19)-19*256 = 92,378-4,864 = 87,514 positions.

The 94,183 required targets of ranks one through seven thus force at
least 6,669 distinct pair targets not supplied literally, within this
frozen-low-height architecture. This is a stricter architecture-specific
ledger than the already known unrestricted 1,802 shortfall at B19.
It is not a general lower bound on every k19 construction.

Equivalently, there are 50,388 rank-seven labels and 43,795 smaller
targets. Reserving all rank-seven labels literally would leave only
87,514-50,388=37,126 slots for the smaller targets. Moving q distinct
rank-seven obligations to fixed proper pairs changes that scalar bound
to 37,126+q, hence requires q≥6,669 in this rank-seven-reservation route.
The scalar equality does not supply literal eligibility, injectivity,
or protection of the newly fixed pairs.

This is why the flow should measure distinct genuinely nonliteral pair
reservations, rather than merely report that some lower-rank pair masks
are individually possible. It also explains why a full result needs
the residual lower assignment after the reservation stage.

### 6.1 Correction: reserve credit must exclude fixed literal overlap

Independent audit by `exact_equality_structure`,2026-09-09: the flow
counts distinct proper-pair witnesses, not a net increase of q distinct
targets beyond the fixed literal palette. The raw test q>=6,669 alone
does not compensate the literal-capacity deficit.

For the specific next-stage architecture in which the reserved rank-seven
pairs supply a set T of targets and every other target of rank at most
seven must be supplied literally, let F be the frozen H3 positions and
let L_F be their distinct literal labels. All these labels have rank at
most seven. The other H3 positions number87,514-|F|. Necessarily

    |T minus L_F| >=6,669+(|F|-|L_F|).                   (6.1)

Indeed the still-required literal targets number
94,183-|T union L_F|, and each free position supplies at most one.
Rearranging that capacity inequality gives(6.1).

Before selecting any pair, apply this with F_0 consisting of the full
anchors and unchanged one-position H3 blocks. Pair targets already in
L_(F_0) have zero credit toward this necessary ledger. An initial useful
flow gate therefore filters them out and uses the stronger threshold
6,669+|F_0|-|L_(F_0)|. After selection, F must also include both fixed
proper subletters of every selected pair; their duplicate literals can
raise the right side further. The exact ledger must be recomputed then.

Passing(6.1) remains only a necessary scalar condition for the subsequent
common literal allocation. It does not prove eligible injective hosts or
preservation of the remaining rank-seven labels. If the later compiler
also creates additional lower pair outputs, their labels must explicitly
be included in T before applying the same counting argument. The lemma
does not exclude such a more general pair-changing compiler.

## 7. One proposed bounded diagnostic, not yet authorized or run

The exact finite candidate input would be the canonical 360-component
record saved by the existing verified k19 height-adaptive generator:

    h100:/home/amodo/exact-b-k19-height-adaptive-20260908/
          height_adaptive_canonical_cycles.json.

Its source is [verify_k19_height_adaptive_fixed_construction_20260908.py](verify_k19_height_adaptive_fixed_construction_20260908.py).
The conventions are fixed: f(A)=complement(A) minus the unique unmatched
zero, g=f^2, each cycle begins at its least integer owner, and cycles
are sorted by that owner. This dataset has 92,378 owner positions,
360 components and height sum1,384. The new task would use those
uncut periodic owner records, NOT the 94,786-letter collar construction
or the 94,161-letter repaired word as if either were an exact carrier.

A reviewed script could perform exactly one deterministic instance:

1. Read and record the input SHA. Construct each capped source D at
   H=min(h,3). Verify the H3 rank-seven letters, rank-eight pairs,
   rank-nine triples, rank-ten owner windows, pins, and fixed palette.
   Freeze every H1/H2 component.
2. Fix the single anchor frame0,3,6,... . Replay the all-minimum cap and
   boundary-pair equalities, proving the advertised block independence
   for this actual source. Abort the proposed flow interpretation if
   any source or palette premise fails.
3. Generate only the at most eight rank-seven deletions of each native
   rank-eight internal pair and apply the exact proper-pair criterion.
   Retain one deterministic literal realization per eligible label/block.
4. Compute the fixed-literal credit ledger of Section6.1 first. For this
   gate discard candidate target labels already fixed literally, and
   compare the group-capacity sum with6,669+|F_0|-|L_(F_0)|. If it is
   smaller, retain that exact restricted-architecture obstruction.
   Otherwise the proposed ONE integral max-flow uses this same filtered
   target set and stops with a complete flow/min-cut certificate.
5. If the filtered value reaches that necessary threshold, materialize
   the resulting capped cyclic bank, recompute(6.1) including the two
   newly fixed letters per selected block, and
   independently replay every preserved triple, every rank-eight target,
   and every assigned proper pair. Export all displaced old literal
   labels and the exact newly fixed pair positions for a later, separate
   lower-target assignment. If deficient, export the exact min-cut/Hall
   certificate for this fixed frame and reservation rule.

Suggested hard limits are 60 CPU seconds, 90 wall seconds, and 2 GiB on
h100. There is no frame search, cycle fusion, alternative transversal,
full lower CSP, construction restart, or broad dimension enumeration.
The script must be written and independently reviewed before execution.

This would change a live gate by either constructing protected proper-pair
witnesses with an explicitly checked necessary credit ledger, or ruling
out one completely specified reservation frame before investing in a
full compiler. It would still be a cyclic-bank result. Joining the bank
with all witnesses protected and within B19 is a separate unsolved step.
If a different flat resident k19 carrier is produced first, the same
reservation lemma applies after its stated local/frame/palette hypotheses
are checked, without dependence on the canonical PBBS chronology.
