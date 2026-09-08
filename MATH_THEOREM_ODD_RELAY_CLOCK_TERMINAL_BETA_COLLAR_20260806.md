# FAILED LINEAGE — a prepared relay clock does not close the terminal odd beta-collar

**Date:** 2026-08-06  
**Method:** first-nonquiet priority, an explicit three-coordinate path, and
copy-before-erase from the partially written target collar; no computation
or search  
**Status:** **FAIL / DO NOT CITE.**  The exact matching rows are
`01 <-> 10`, `02 <-> 11`, and `12 <-> 21`; in particular `11` is selected
nonquiet, not quiet.  Thus priority never passes from `p_1` to `p_2` at the
claimed states.  Moreover, the displayed work changes `B_1`, a coordinate
of `p_1`, so the shadow-clock lifting theorem is inapplicable.  The first
forced matching steps are `020 -> 011 -> 012` and
`022 -> 112 -> 111`, not the paths claimed below.  This file is retained
only to record the rejected construction.  The authoritative failure audit
is `MATH_AUDIT_ODD_COLLAR_FIRST_ENDPOINT_BIT_AND_RELAY_BETA_20260806.md`.

## 1. Prepare a relay before changing `p_1`

The active first clock is

\[
                         p_1=c(B_1)=(1,B_1),
             \qquad B_1\in\{0,2\}.
\tag{1.1}
\]

While `p_1` is still selected, choose the next work pair `p_2`, disjoint
from the collar and `p_1`, and put it in a fixed selected nonquiet row.
Its old two-coordinate value is retained in the zipper interface.  Since
`p_1` precedes `p_2`, `p_1` remains the selected clock until it becomes
quiet.  If that happens, `p_2` is immediately the first nonquiet pair.

This preparation is an ordinary work path lifted through `p_1`.  The
source collar/three-row record is still literal while it is performed, so
copy-before-erase makes the preparation occurrence-injective.

## 2. The complete local handoff is explicit

Put `H=02`, and place one returned head block next to the `B_1` coordinate.
The two nontrivial beta branches are

\[
 \begin{aligned}
  a_1=0:\quad&020\longrightarrow011\longrightarrow002,\\
  a_1=2:\quad&022\longrightarrow112\longrightarrow121
                 \longrightarrow211\longrightarrow220.
 \end{aligned}
\tag{2.1}
\]

The first two coordinates are the collar block and the last coordinate is
`B_1`.  Every arrow is one unit transfer across one physical edge.  The
endpoints are exactly

\[
 H|0\longrightarrow 00|2,
       \qquad H|2\longrightarrow22|0.
\tag{2.2}
\]

Thus the head becomes the required complemented extreme and

\[
                         B_1^*=2-G_1.
\tag{2.3}
\]

For `a_1=1`, `B_1=B_1^*=2`; no beta change is needed, and the neutral
collar conversion `02 -> 11 -> 20` is ordinary work disjoint from `p_1`.

### Lemma 2.1 (directed relay lift)

After preparing `p_2`, every path in (2.1) has a directed lift in the fixed
matching contraction.  Whenever the displayed last coordinate is `0` or
`2`, `p_1` is first nonquiet and its selected edge follows the physical
transfer.  Whenever that coordinate is `1`, `p_1=11` is quiet, so the
prepared `p_2` row is first nonquiet and its selected edge follows instead.
No state lacks a selected clock.

#### Proof

At a majority state perform the next physical transfer in (2.1).  The
matching rule chooses the first nonquiet scan pair in the resulting
minority state.  By construction that pair is `p_1` when `B_1` is `0` or
`2`, and is `p_2` when `B_1=1`.  Toggle its selected row to return to the
majority shore.  Repeating this for every displayed arrow gives the
directed lift.  Both rows have two possible starting endpoints; choose
them so their forced parity ends at the required target endpoints.
\(\square\)

## 3. The changing record does not erase the source

Before (2.1), complete every other collar--packet conversion.  Thus one
collar position is already its literal complemented target and the other
is the head `H` used in (2.1).  The oriented residual midpoint/tag bank and
the deterministic pairing remain fixed.

At the first strict state of a nontrivial branch, the total local mass
distinguishes `a_1=0` from `a_1=2`.  The residual signed count gives

\[
 q=\epsilon(a_1)+\epsilon(a)+\epsilon(b).
\tag{3.1}
\]

The already written target collar position gives one of `a,b`, and its
physical position gives the order.  Equation (3.1) therefore recovers the
other collar digit even while the unordered `p_1` record passes through
the quiet row `11`.  The simple path (2.1) gives the microstep.  Hence the
source remains decoded throughout the beta handoff.

The non-one root flag is retained.  At quiet-`p_1` states the prepared
`p_2` row is nonquiet, and at the other states `p_1` is nonquiet.  Thus no
strict state lies on the old quiet-source promotion/aperture linkage.

## 4. Return the literal target collar

Bring the original `H|H` head to the `p_1` neighbourhood by the proved
double-head transport before applying Section 2.  Keep the second head
block until all non-beta collar--packet conversions have been completed in
that same bounded neighbourhood.  Section 2 then writes the last target
collar block.  At this checkpoint the complete literal complemented collar
is present, so the old three-row record is no longer needed.

Return the two-block target collar train to its fixed berth before
finalizing the remaining noncrossing tags.  Its corridor therefore consists
only of `20,01,21` blocks.  Corridors of length at least two use the
stationary-corridor train theorem, length zero is local, and length one uses
the selected-row endpoint-bit theorem.  All crossed blocks return to their
labelled addresses.

Once the target collar is back at its berth, use the now-selected target
`p_1` row as shadow clock to restore the prepared `p_2` work record.  Then
run the audited aperture-retirement collar and root exit.

### Theorem 4.1 (terminal beta-collar)

Assume the one-interior endpoint-bit decoder.  The schedule in Sections
1--4 changes `B_1` to `B_1^*`, writes and returns the complemented collar,
restores the relay clock, and retains a source/stage decoder at every strict
state.  Its paths are pairwise vertex-disjoint over all odd sources and it
uses no anonymous reservoir.

#### Proof

The outward head transport is the double-head theorem.  Lemma 2.1 supplies
the only phase handoff.  Section 3 proves injectivity while the old row
record is being overwritten.  The target collar then becomes the permanent
copy of its source data.  The return is occurrence-injective by the three
corridor cases in Section 4.  Finally `p_1` is again nonquiet, so restoration
of `p_2` is ordinary shadow-clock work.  These phase labels are mutually
exclusive; within each phase the cited decoder recovers source and
microstep.  Equality of two route states therefore forces equality of the
entire labelled route.
\(\square\)

## 5. Consequence and scope

Together with
`MATH_THEOREM_ODD_ENDPOINT_BIT_ONE_INTERIOR_REGISTER_20260806.md`, this
theorem supplies the two finite rows left open by
`MATH_AUDIT_ODD_BALANCED_MIDPOINT_AND_GUARD_SHUTTLE_20260806.md`:

1. the one-interior occurrence label; and
2. the terminal `B_1 -> B_1^*` beta-collar.

All scalar residual cases `0,1,2,3`, arbitrary corridors, and the protected
first connector are then covered without a private reservoir.  The claim
is only as strong as the endpoint-bit decoder and should not be promoted to
the odd all-k package until both notes receive an independent literal audit.
