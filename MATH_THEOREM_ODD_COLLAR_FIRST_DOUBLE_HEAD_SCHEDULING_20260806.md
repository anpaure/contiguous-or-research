# Collar-first scheduling removes the generic one-interior odd gate

**Date:** 2026-08-06  
**Method:** maximal cross-pairing, a fixed collar berth, and delayed packet
internal pairing; no computation or search  
**Status:** **CONDITIONAL / DO NOT CITE THEOREM 5.1 AS CLOSED.**  Sections
1--3, with the corrected two-cross relay, remove the generic fixed-berth
one-interior row.  The dependency audit
`MATH_AUDIT_ODD_PACKAGE_DEPENDENCY_CLOSURE_20260806.md` finds that Section 5
does not prove its stationary-corridor alphabet premise before the double
head exists: with two residuals, either processing order crosses a raw
extreme or a newly written `M=11`.  The protected application therefore
still requires the anchored pre-head bootstrap isolated in that audit.

## 1. Choose the pairing in the right order

Let `P` be the unfinished packet and let the two fixed collar blocks be the
collar bank.  Their total extreme charge is zero.  Choose opposite pairs by
the following deterministic rule.

1. Pair an opposite collar pair internally, if it exists.
2. Pair every remaining collar extreme with an opposite packet extreme,
   in physical collar order and then packet-address order.
3. Pair the remaining packet extremes internally.

Neutral collar blocks are processed locally by `20 -> 11 -> 02` and
neutral packet blocks remain fixed.

### Lemma 1.1 (at most one delayed packet pair)

After steps 1--2, every collar position can be converted to `H=02`, and
the remaining packet extreme bank has size at most two.  If nonempty, it is
one opposite pair.

#### Proof

Let \(c\in\{-2,-1,0,1,2\}\) be the signed collar charge and let
\(e_1\in\{-1,0,1\}\) be the first-connector charge.  The residual packet
bank has charge \(-(e_1+c)\) and, before the first connector is included,
contains only extremes of that sign.  The exact cases are as follows.

* If \(|c|=0\), an opposite collar pair is consumed internally.  For
  \(e_1=0\) no packet extreme remains; for \(|e_1|=1\), the first connector
  and the unique residual extreme form one opposite pair.
* If \(|c|=1\), cross-pairing consumes one opposite packet extreme.  Nothing
  remains when \(e_1\) is zero or opposite to \(c\); when it has the sign of
  \(c\), exactly one opposite packet pair remains.
* If \(|c|=2\), cross-pairing consumes two opposite packet extremes.  Again
  nothing remains unless \(e_1\) has the collar sign, in which case exactly
  one opposite packet pair remains.

Thus the unprocessed packet bank is empty or one opposite pair.
\(\square\)

Thus no packet--packet shuttle is required before both collar positions are
literal heads.

## 2. Every pre-head shuttle has a fixed endpoint berth

The only remote pre-head operation is now a cross pair consisting of one
packet extreme and one collar extreme.  Move the packet block toward the
fixed collar berth through the neutral/tag word supplied by noncrossing
cancellation.

* A zero-interior shuttle is already local.
* A corridor of length at least two uses the stationary-corridor guard
  theorem.
* If the corridor consists of one block `Y`, the physical support is
  
  \[
                 X\mid Y\mid Z,
  \tag{2.1}
  \]
  
  where `Z` is the still literal collar block at its fixed berth.  Keep
  `Z` fixed while traversing a simple token path from `X|Y` to `Y|X`.
  The collar record identifies `Z`, its physical berth identifies the
  active four-coordinate window, local mass and the existing branch bit
  identify the ordered endpoint type, and simplicity identifies the
  microstep.

After `X` reaches `Z`, apply the spatially oriented cross path

\[
                         X|Z\longrightarrow M|H.
\tag{2.2}
\]

This is the reflected branch of the tabulated `A|C`/`C|A` conversion: `M`
must occupy the packet-side position and `H` the collar berth.  The new `H`
remains fixed at that berth while `M` is returned through
the same corridor.  In the one-interior case it is again the fixed outside
guard for the reverse local path.  Thus both directions are
occurrence-labelled without a generic remote three-block table.

If both collar positions are cross-paired and the packet tape approaches
the collar from one side, the second packet extreme cannot pass through the
first newly written `H` using the ordinary corridor alphabet.  Once that
second extreme `X` reaches the near side, use instead the guarded relay

```
X | H | Z  ->  H | X | Z  ->  H | M | H  ->  M | H | H.
```

The far literal collar `Z`, then the left `H`, then the right `H` is fixed
at the three successive stages.  Every active token graph has fixed
nonextreme mass, and the middle conversion again uses the branch ending in
`M|H`.  Hence the relay is occurrence-labelled and leaves a literal double
head.

### Theorem 2.1 (fixed-berth cross shuttle)

Every cross pair in step 2 of Section 1 has pairwise source-disjoint setup
and return paths, for every corridor length.  It restores every crossed
block to its old address and leaves `H` at the named collar position.

#### Proof

The zero and long cases are the cited local and stationary-corridor
theorems.  In the length-one case the untouched collar record and physical
berth locate (2.1) at every strict state.  Deleting the active window leaves
a decoded checkpoint; the branch and simple path recover its ordered source
and microstep.  The same decoder applies after (2.2), with the fixed `H`
as an even stronger berth marker.  In the two-cross case the three successive
fixed guards displayed above give the same information.  Different source
paths therefore cannot meet.
\(\square\)

## 3. Create the head before touching the delayed pair

Process the collar positions in physical order.  An internal opposite
collar pair uses the local `A|C -> H|H` path.  A neutral collar position is
changed locally.  Every cross-paired position uses Theorem 2.1.  Hence both
collar positions become

\[
                             H|H
\tag{3.1}
\]

before the possible packet pair from Lemma 1.1 is touched.

Now use the proved double-head visible-cart theorem to bring (3.1) beside
that one delayed packet pair.  The double head labels every strict local
state, so the pair can be converted to its oriented `01|21` tags and the
head returned to its fixed berth.  No unguarded packet--packet shuttle
occurs.

The teardown order is reversed: use the double head while it still exists
to finalize the delayed packet pair, then tear down the **far** cross pair
first by reversing the three-block relay, and finally process the near cross
pair by the single-cross route.  For a cross pair, the still-literal head at
its collar berth again guards a one-interior return.  The final collar paths
write the complemented collar.

### Theorem 3.1 (collar-first midpoint schedule)

Assuming the already audited stationary-corridor and double-head transport
theorems, every midpoint-packet shuttle in residual cases `0,1,2,3` has an
occurrence-labelled literal path.  No generic one-interior table, endpoint
address register, or anonymous reservoir is required.

#### Proof

Lemma 1.1 and Theorem 2.1 cover every operation before (3.1).  The
double-head theorem covers the sole possible delayed internal pair.  The
same phase decomposition in reverse covers teardown.  At each checkpoint
the collar record, midpoint/tag bank, and deterministic pairing recover the
source.  At every strict state either the fixed berth, a stationary marked
corridor, or the double head supplies the occurrence label.  Hence source,
phase, active address, and microstep are always recoverable.
\(\square\)

## 4. Consequence and scope

Subject to an independent audit of the Section 5 protected-connector
formulation, this theorem removes the finite one-interior row listed in
`MATH_AUDIT_ODD_BALANCED_MIDPOINT_AND_GUARD_SHUTTLE_20260806.md` without
constructing a twelve-case table.  The only remaining odd interface is the
terminal beta-collar, for which the active `p_1` row itself changes.  A
candidate relay-clock construction is in
`MATH_THEOREM_ODD_RELAY_CLOCK_TERMINAL_BETA_COLLAR_20260806.md` is a failed
lineage attempt and must not be used: `p_1=11` is selected nonquiet, not a
handoff state.  A genuine terminal beta path remains open.

## 5. Zipper-split fixed-berth accumulator

The unfinished-packet pairing in Sections 1--3 contains the raw first
connector only as an algebraic charge.  In the protected construction that
connector is not moved.  Instead setup changes the ordinary work record
`(G_1,B_2)` while keeping the selected `p_1` row fixed.

Each residual extreme changes to `M=11`, so its mass change is `+2` for
`A` and `-2` for `C`.  The `G_1` change is

\[
                         G_1^*-G_1=-2\epsilon(a_1).
\tag{5.1}
\]

Call these values the **external increments**.  Their sum is

\[
                         2(\epsilon(a)+\epsilon(b)).
\tag{5.2}
\]

The source collar mass is

\[
                         m_0=2(a+b)=4+2(\epsilon(a)+\epsilon(b)),
\tag{5.3}
\]

so paying the negative of each external increment from the collar ends at
mass four, the mass of `H|H`.

Order the nonzero external increments as follows.  While the current collar
mass is above four, process a `+2` increment; while it is below four,
process a `-2` increment; at mass four process opposite signs in pairs.
Equation (5.2) guarantees that the requested sign exists whenever it is
needed.  Every intermediate collar mass lies in `{0,2,4,6,8}`.

For one increment, shuttle only its remote work block to the fixed collar
berth.  In the `G_1` case orient `(G_1,B_2)` with `G_1` inward and append
`B_2` unchanged.  A zero-interior move is local; a corridor of length at
least two uses stationary marks; and a length-one move is guarded by the
fixed collar berth and three-row record.

The remote source/target pair and the old/new collar states have equal
combined mass.  If that mass is extreme the states agree.  Otherwise the
capacity-two token graph on this bounded contiguous interval is connected,
so choose a simple local path.  Return the transformed remote block to its
old address immediately, reversing the marked corridor.  Thus different
remote corridors never overlap in their nonrestored state.

After the last increment the collar has mass four.  Its source type and the
completed external targets are still recorded, so choose a fixed-mass
simple path inside the four collar coordinates to the particular state
`H|H`.  The literal double head now exists before any remaining internal
packet pair is processed.

### Conditional Theorem 5.1 (zipper-split fixed-berth accumulator)

Assume every remote increment can be ordered so that its full shuttle
corridor is in the stationary alphabet `{20,01,21}` (or is supplied with a
separate occurrence-labelled non-guardable crossing).  Then the complete
setup half of the balanced midpoint packet, including every
residual multiplicity `0,1,2,3` and the protected first-connector payment,
has an occurrence-labelled path which keeps `p_1` fixed and ends with a
literal double head.  It uses no raw first-connector move, anonymous
reservoir, or generic one-interior table.

#### Proof

Equation (5.2) is Theorem 2.1 of
`MATH_THEOREM_ODD_ZIPPER_SPLIT_MIDPOINT_PACKET_AND_BETA_COLLAR_GATE_20260806.md`.
The sign ordering keeps the collar within capacity and every two-party
operation at fixed total mass.  The fixed row/record and berth identify its
simple local path, while the stationary-corridor decoder identifies the
shuttle and its reverse.  Since each remote corridor is restored before the
next begins, these occurrence labels compose.  The final collar-only path
creates the double head, which gives the audited decoder for any delayed
internal packet pair.  Concatenation proves the claim.
\(\square\)

The added alphabet assumption is not presently derived; see the dependency
audit cited at the top of this file.  Subject to it, the teardown batch is
the reverse construction except for `B_1`, which is
part of the active clock rather than the ordinary work block.  That one
coordinate is exactly the terminal beta-collar gate.  The separate
relay-clock note is retained only as failed lineage; its claimed path is
not a path in the full matching contraction.
