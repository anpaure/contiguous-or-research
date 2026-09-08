# Independent audit of the balanced midpoint and stationary-guard proposals

**Date:** 2026-08-06  
**Files audited:**

* `MATH_THEOREM_ODD_BALANCED_MIDPOINT_PACKET_ELIMINATES_RESERVOIR_20260806.md`;
* `MATH_THEOREM_ODD_STATIONARY_CORRIDOR_GUARD_SHUTTLE_20260806.md`;
* `MATH_THEOREM_ODD_ZIPPER_SPLIT_MIDPOINT_PACKET_AND_BETA_COLLAR_GATE_20260806.md`.

No computation or scalar-connectivity argument is used.

## Verdict

The arbitrary private reservoir is unnecessary.  The exact charge identity,
all displayed midpoint paths, and the zipper split of the protected first
connector pass.  They cover the algebra of residual multiplicities
`0,1,2,3` and retain a literal source decoder.

The first stationary-guard draft had a fatal return-orientation error: the
displayed move erased a mark but did not move the active block.  The current
file has been corrected.  It now carries the active block across every
still-marked block and erases marks only afterward.  This proves literal
occurrence labelling for corridors with at least two stationary blocks and,
by the same argument, for bounded trains.

The complete odd collar is **not yet proved**.  Two finite interfaces remain:

1. a strict-state table/guard for a generic one-interior shuttle; and
2. the terminal `B_1 -> B_1^*` beta-collar while changing/retiring the active
   `p_1` clock and returning the collar block to its fixed berth.

Thus the proof-safe boundary is

\[
 \boxed{\text{unknown reservoir removed; exact finite beta/short-corridor
 interface still open.}}
\]

## 1. Charge audit

Put `e_i=epsilon(a_i)` and `c=epsilon(a)+epsilon(b)`.  The work residual has
charge `q_res=-(e_1+c)`.  Hence the first connector plus residual has charge

\[
             e_1+q_{\rm res}=-c,
\]

which is exactly opposite the collar.  After internal opposite pairs are
removed, the remaining packet extremes have one sign and the remaining
collar extremes the other.  Their counts are equal and at most two, because
the collar has only two blocks.  This sharpens the raw residual bound
`|q|<=3`: three residual occurrences may exist, but the cross remainder after
internal pairing is never three.

Replacing an extreme of charge `e` by `M=11` changes mass by `-2e`.  The
source-to-midpoint and midpoint-to-complement changes are equal.  Therefore
both halves of the collar conversion are balanced separately.

For the protected first connector, the zipper identities give

\[
 G^*-G=B^*-B=-2e_1.
\]

The residual half contributes `2(e_1+c)`, so residual plus either zipper
half contributes `2c`, opposite the collar increment `-2c`.  This verifies
the split calculation in every case, including `q=0`.

## 2. Literal path audit

Every arrow below changes two adjacent coordinates by `(x,y)->(x-1,y+1)`
or its reverse, with all coordinates in `{0,1,2}`:

\[
 \begin{aligned}
 0022&\to0112\to0121\to0211,\\
 2200&\to2110\to1210\to1120\to1111\to0211,\\
 20&\to11\to02,\\
 002&\to011\to020,\\
 220&\to211\to121\to112\to022.
 \end{aligned}
\]

Their endpoints are respectively

\[
 A|C\to H|M,quad C|A\to H|M,quad B\to H,quad
 A|2\to H|0,quad C|0\to H|2.
\]

Reversal gives the complementary branch.  Spatial reflection gives the
opposite physical orientation.  Hence all local midpoint and zipper-bit
claims are literal.

## 3. Midpoint source recovery

At a macro checkpoint no marked shuttle corridor remains.  A packet `M=11`
therefore identifies a cross-paired address, while `01|21` or `21|01`
records an internally paired orientation and `B=20` is fixed.  The stored
ordered collar type and deterministic pairing rule recover the source type
of every cross `M`.

In the zipper-split version, the mixed pair `(B_1,G_1^*)` need not determine
`a_1`; this is harmless.  The collar record gives `a,b` and the signed
residual bank gives `q`, so

\[
             e_1=q-epsilon(a)-epsilon(b)
\]

recovers it, including when the residual is empty.  The record is therefore
copy-before-erase rather than an information-counting assertion.

## 4. Stationary-guard correction

After the outward shuttle the tape is

\[
        \mu(Y_1)\cdots\mu(Y_s)X'.
\]

The rejected return

\[
        \mu(Y_j)|X'\to Y_j|X'
\]

does not move `X'`.  The corrected return is

\[
        \mu(Y_j)|X'\to X'|\mu(Y_j),
        \qquad j=s,s-1,\ldots,1.
\]

For `j=s`, `mu(Y_(s-1))` is a fixed left guard; for the final `j=1`, the
already crossed `mu(Y_2)` is a fixed right guard.  Thus `s>=2` is
load-bearing.  The endpoint is

\[
        X'\mu(Y_1)\cdots\mu(Y_s),
\]

and every mark is then erased by its single in-block edge.  This both moves
the active block back and avoids an unguarded final swap.

The proof is unchanged for a fixed-length active train: replace the local
four-coordinate token graph by the nonextreme fixed-mass graph on the train
plus one stationary block.  A marked corridor still fixes the physical
window and the simple local path fixes the microstep.

## 5. Why one-interior is still a real finite row

When `s=1`, premarking the unique stationary block leaves no second fixed
mark during the interchange.  It is not enough to say that a deterministic
simple path was chosen: two source-indexed simple paths can share a strict
state.  The old collision `ABCB -> ACBB` is exactly this logical failure at
the unmarked level.

For a shuttle immediately adjacent to the common fixed collar berth, the
physical berth and collar record can serve as the missing guard.  A generic
remote cancellation pair or the initial gathering of a two-residual train
need not be at that berth.  It therefore needs either an explicit
marker-preserving three-block table or one extra stationary mark outside the
active window.  No such uniform table is yet written in the audited files.

## 6. Exact protected-first-connector boundary

Advancing `G_1` during setup is proof-safe: `(G_1,B_2)` lies after the
selected `p_1` clock, the active row is unchanged, and the three-state collar
record survives.  The displayed three-coordinate paths give its exact local
mass exchange with one collar extreme.

Advancing `B_1` is different because `B_1` belongs to the active clock.
The shadow-clock lift only applies to work disjoint from that clock.  The
existing aperture-retirement theorem proves how to reach the final target
once an appropriate protected predecessor is present; it does not by itself
transport a complemented collar block back to its fixed berth after the
clock is changed.  This is precisely the Terminal beta-collar lemma, and it
cannot be replaced by unlabelled component connectivity.

## 7. Minimal exact obstruction

There is no remaining scalar mass, residual-count, or unknown-source-bank
obstruction.  The smallest unresolved directed object is a finite labelled
path family with state

\[
 (\text{ordered collar record},\ \text{root phase},\
  \text{one short marked corridor},\ \text{selected }p_1\text{ row}),
\]

which implements the one-interior interchange and the two beta-collar
branches while keeping a later target clock.  Proving this finite interface
would close `DH` and all four residual cases; absent it, the odd package must
remain conditional.
