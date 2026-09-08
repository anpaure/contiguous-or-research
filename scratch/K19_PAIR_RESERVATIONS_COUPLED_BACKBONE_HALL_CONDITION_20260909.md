# Pair reservations need a coupled residual allocation certificate

2026-09-09. Pure-proof follow-up by `exact_b_finite_frontier`.
No code, solver, flow, census or mathematical execution was performed.

**Recommendation:** defer a standalone numerical proper-pair reservation
flow. Its positive result constructs useful designated pair witnesses,
but a large raw reservation count does not certify a net lower-coverage
gain. A future fixed-instance proposal should pair it with the explicit
backbone and residual matching certificate below, and should only call
the lower compiler closed if that coupled certificate passes.

## 1. What the earlier flow actually proves

The [proper-pair reservation lemma](K19_GENUINE_PAIR_RESERVATION_LEMMA_AND_NEXT_FINITE_GATE_20260909.md)
correctly constructs q distinct targets S on fixed adjacent letters E,F,
with E union F=S and E,F both proper subsets of S. It preserves the
certified triple deck and reserves an original or frozen witness for
every rank-eight label displaced by those block edits.

"Proper" is local. S can still be the literal letter at another source
position. In particular it may already be present at a frozen anchor;
then designating its pair witness removes no remaining literal demand.
Different selected blocks can also produce repeated fixed subletters.
Those consume positions without supplying the same number of distinct
lower targets. The corrected ledger in Section6.1 of the earlier note
accounts for both effects.

Even that corrected scalar ledger is insufficient. It ignores which
remaining targets can use which positions, and simultaneous literal
assignments can destroy the rank-eight witness that the reservation flow
left available. Therefore a reservation max-flow followed only by a
count of free positions is not a complete lower-target allocation.

## 2. Fixed data for a coupled certificate

Assume exactly the source and independent-frame hypotheses of the earlier
lemma. This may be a checked cyclic bank; no single optimal-length k19
carrier is assumed to exist.

On its editable H3 components:

* D_i is the original available letter and Pin_i its mandatory subset.
* Full anchors and pins certify that every intermediate cap preserves
  every native triple; boundary pairs are invariant as stated there.
* Native rank-eight internal pairs and the already invariant/frozen
  witnesses cover the full rank-eight palette.
* The native triples plus untouched components cover the rank-nine
  layer, and their longer intervals cover every higher target.

These are explicit source/palette hypotheses, to be checked for any
actual candidate rather than inferred from its dimension or name.

Fix some selected proper-pair reservations and their actual two letters.
Let F be every now-fixed H3 position: anchors, unchanged singleton blocks,
and both positions of each reserved pair. Let L_F be the set of distinct
literal labels at these fixed positions, and let T be the distinct
reserved pair labels. Any additional immutable lower witnesses may be
included too, but must have explicit witnesses. For clarity below, use
only L_F union T.

The remaining required low targets are

    R={S subseteq [19]:1<=|S|<=7} minus (L_F union T).

Let I be the free H3 positions, outside F. The intended restricted
completion assigns every target in R to a distinct literal position in I.
This is a clearly specified route; other uncounted pair outputs might
permit a more general completion and are not ruled out by its failure.

## 3. Protect one witness per rank-eight label, not every old pair

For each rank-eight label V that has no already invariant/frozen witness,
choose ONE unselected internal two-position block `(i,j)` whose original
pair union is V. The earlier rank-eight group-capacity rule guarantees an
unselected block exists, but choosing it does not by itself protect it
against the upcoming literal edits.

Choose explicit coordinate backbones B_i,B_j at that block satisfying

    Pin_i subseteq B_i subseteq D_i,
    Pin_j subseteq B_j subseteq D_j,
    B_i union B_j=V.                                    (3.1)

Different chosen internal blocks are disjoint in the frame; one block has
only one native rank-eight label, so two distinct V labels cannot require
the same block. At every other free position put B_i=Pin_i. The fixed
positions keep their already specified letters.

The backbone choice is part of the finite certificate. Trivial choices
such as full D letters always protect the pair but can leave insufficient
literal flexibility; no useful residual Hall property follows merely
from the existence of some backbone.

Every final cap with B_i subseteq A_i subseteq D_i keeps each designated
rank-eight witness: its pair union is at least B_i union B_j=V and at
most D_i union D_j=V. All other native rank-eight pairs may change;
preserving their individual occurrences is not required. This is more
flexible than restoring the old pair-frozen compiler everywhere.

Because B_i contains every pin, and full anchors remain full, the same
certified minimum-word argument preserves every native triple and hence
every longer interval throughout the simultaneous assignment.

## 4. Exact residual Hall condition and literal construction

Build a bipartite graph whose left vertices are R and whose right vertices
are the free positions I. Its edges are

    S~i iff B_i subseteq S subseteq D_i.                (4.1)

For these fixed reservations, witness choices and backbones, the following
condition is necessary and sufficient for the stated residual literal
assignment:

    |A| <= |{i in I: some S in A satisfies (4.1)}|
    for EVERY A subseteq R.                            (4.2)

This is ordinary bipartite Hall, equivalently saturation of an integral
unit-capacity matching network. It is a complete condition for assigning
every required residual target to a different permitted literal position;
it is not a channel-capacity approximation to that assignment problem.

**Coupled completion theorem.** If the proper-pair reservations, designated
rank-eight backbones, and a matching saturating R are supplied, an actual
complete lower cap of the bank is constructed by:

1. Keeping every fixed position in F exactly as specified.
2. Setting a matched free position i to its matched target S.
3. Leaving every unmatched free position at its original D_i.

All letters remain nonempty. Every final free letter contains its B_i
and lies inside D_i. Thus the frame preserves every native triple and
all longer targets. The selected backbones preserve one witness for each
rank-eight label lacking an invariant witness. The untouched invariant
witnesses supply the others. Every low target in L_F union T has its
fixed literal or proper-pair witness, and every other required low target
has the matched literal witness. Hence every rank is covered under the
stated source-palette hypotheses.

This is a simultaneous construction, not separate successful lower and
upper tests on different caps. Old rank-seven literals destroyed by the
reservation step are included again in R unless they really have a
fixed witness in L_F union T; they cannot silently disappear from the
remaining obligation list.

The fixed scalar credit inequality from the earlier note is weaker than
(4.2): it bounds the neighborhood of the entire residual set by the
number of all free positions, without checking any actual eligibility
neighborhood or the added backbone restrictions. Passing that scalar
inequality therefore cannot be promoted to passing this coupled theorem.

## 5. What to require before a future computation

A useful future fixed-instance proposal should specify:

* The actual source/frame/palette certificate.
* The actual proper-pair targets and fixed two-letter representatives.
* One designated original witness per remaining rank-eight obligation
  and its explicit backbone.
* The full residual demand set R and a matching saturating it, or an
  exact Hall-deficient set if that fixed coupled choice fails.

The last step may be one ordinary max-flow after the preceding objects
are fixed. It does not require solving a general common-cap SAT instance.
However the earlier reservation max-flow does not choose its targets or
subletters with this residual graph in view. An arbitrary maximum
reservation flow can therefore lead to a bad coupled instance even if
another reservation choice would work. A failed residual matching would
refute that exact choice, not all proper-pair approaches.

This makes the present decision clear: **do not run the standalone q-flow
as though q>=6669 closes a useful lower compiler gate.** It is worth
running only as part of a reviewed, fully specified coupled attempt whose
acceptance includes the residual saturation certificate and literal
replay. Until such choices are fixed, retain the flow lemma as a valid
construction interface and defer its numerical instance.

Even a successful coupled certificate would first give a complete cap of
the stated cyclic bank. An optimal-length single word still requires a
separate witness-preserving fusion/opening argument. No exact19 or
all-dimensional equality claim follows from this pure-proof note.
