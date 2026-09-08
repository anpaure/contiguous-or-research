# The selected-row endpoint bit closes the bounded one-interior odd shuttle

**Date:** 2026-08-06  
**Method:** copy-before-erase, the endpoint orientation of a selected
two-state clock row, and parity of a directed shadow-clock lift; no
computation or search  
**Status:** **SUPERSEDED / DO NOT CITE.**  The endpoint/parity idea does not
by itself locate the active physical window: recovering the microstep from
the local path presupposes knowing which window to read.  The safer
collar-first schedule in
`MATH_THEOREM_ODD_COLLAR_FIRST_DOUBLE_HEAD_SCHEDULING_20260806.md`
eliminates every generic remote one-interior shuttle before the double head
exists.  The algebra below is retained only as a record of the rejected
shortcut.

## 1. The two available register bits

After the collar type has been copied, the first scan pair lies in one of
the three selected unordered rows

\[
 \mathcal R=\{\{01,10\},\{02,11\},\{12,21\}\}.
\tag{1.1}
\]

The exterior source tape determines `a+b`, and the unordered row
`R_(a,b)` determines the remaining order class of the collar.  Therefore
the choice of **endpoint** inside `R_(a,b)` is not used by the collar
record.  Write this endpoint bit as `e in {0,1}`.

The protected root/boundary register has the independent branch bit
`b in {0,1}` from
`MATH_THEOREM_ODD_MARKED_CORRIDOR_VISIBLE_CART_20260806.md`.  Its pass bit
continues to distinguish setup from teardown and is not used below.

Thus, while the unordered row remains fixed, `(b,e)` is a four-state
temporary register.

## 2. Only two addresses are ever needed in one class

First pair all possible opposite packet extremes internally, and pair an
opposite collar pair internally.  The exact packet--collar balance then
leaves packet extremes of one sign and collar extremes of the opposite
sign.  Their common number is at most two because the collar has two
positions.

Hence the cross-packet operations have an address

\[
                         j\in\{0,1\}.
\tag{2.1}
\]

The internally paired packet operations also number at most two.  They are
performed in a separate pass subphase, so the same two addresses may be
reused.  The train version for two equal cross extremes is one operation
with one address.

For a fixed local mass, the ordered moving/stationary endpoint type has
multiplicity at most two.  Give those two possibilities the branch labels
`b=0,1`.  Give the two possible addresses the initial selected-row endpoint
labels `e=0,1`.

Before altering the active local window, the literal source/checkpoint is
still present.  Route the operational branch register to `b` and choose
the required endpoint `e` of the already selected row.  This is a
copy-before-erase operation: during the finite register route the untouched
source tape itself identifies `(j,b)`.

## 3. Parity recovers the initial endpoint

Fix one of the finite simple physical token paths

\[
                         z_0,z_1,\ldots,z_\ell
\tag{3.1}
\]

used to interchange an active block or fixed-length train with the unique
interior block.  The branch bit identifies which ordered endpoint type,
and hence which path (3.1), is active.

The shadow-clock compilation theorem lifts each physical edge
`z_i z_(i+1)` to two directed arcs.  At the next majority checkpoint the
selected row has toggled once.  At the intervening minority state its
unique following selected edge identifies the same step.  Consequently,
from the current literal local state and the fixed branch bit one recovers
the microstep `i`, and therefore the parity of the number of completed
selected-row toggles.

If `e_cur` is the currently visible endpoint of `R_(a,b)`, then

\[
                 e_0=e_{\rm cur}\oplus(i\bmod2)
\tag{3.2}
\]

at majority checkpoints, with the analogous uniquely determined formula
at a minority intermediate.  Thus the initial endpoint bit, and hence the
address `j`, is recoverable throughout the lifted path.

### Theorem 3.1 (endpoint-bit one-interior decoder)

For every one-interior setup or teardown shuttle belonging to the bounded
midpoint packet, the full literal state together with the pass recovers

1. the ordered collar source;
2. the internal-pair or cross-pair subphase;
3. the active address `j`;
4. the ordered local endpoint type; and
5. the current microstep.

Therefore the directed lifted paths for all sources are pairwise
vertex-disjoint.  After the active block returns to its labelled address,
the branch register and selected-row endpoint may be returned to their idle
values before the next operation.

#### Proof

The exterior checkpoint and the unordered selected row recover the collar
by the three-row record theorem.  The pass and the already completed
midpoint/tag checkpoints identify the operation class.  The fixed branch
gives the ordered endpoint type, so simplicity of (3.1) gives the local
microstep.  Equation (3.2) then recovers the initial endpoint bit and the
address `j`.

All tape blocks outside the active window are at a decoded checkpoint.
Reinsert the recovered ordered endpoint blocks at the recovered address to
obtain the complete source tape.  Hence equality of two strict lifted
states forces equality of source, class, address, endpoint type, and
microstep.  The paths are pairwise disjoint.

At the returned checkpoint the literal tape again contains the active
block at its original address.  It therefore labels the finite route which
restores `(b,e)`; copy-before-erase gives the same disjointness argument for
that restoration.  No tape coordinate or mass reservoir was added.
\(\square\)

## 4. Consequence and exact scope

The former generic one-interior warning is real for an unlabelled remote
swap: a simple path alone does not identify its physical occurrence.  In
the balanced midpoint packet, however, the required address bank has size
at most two in each subphase.  The selected-row endpoint bit is precisely
the missing address bit, while the existing branch bit labels the two
ordered endpoint types.

Together with the stationary-corridor theorem for corridors of length at
least two and the explicit adjacent paths for length zero, Theorem 3.1
closes every finite short-corridor shuttle used to create and later retire
the midpoint packet.

This theorem keeps the unordered `p_1` row fixed.  It therefore does **not**
close the terminal `B_1 -> B_1^*` operation, which changes the active clock
row data.  The remaining odd statement is exactly the Terminal
beta-collar lemma from
`MATH_THEOREM_ODD_ZIPPER_SPLIT_MIDPOINT_PACKET_AND_BETA_COLLAR_GATE_20260806.md`.

## 5. Dependencies

The three-row collar record and endpoint freedom are in
`MATH_THEOREM_ODD_COPY_BEFORE_ERASE_NINE_RECORD_COLLAR_20260806.md`.
The four-state pass/branch register is in
`MATH_THEOREM_ODD_MARKED_CORRIDOR_VISIBLE_CART_20260806.md`.
The directed two-arc lifting and unique minority mate are Theorem 4.1 of
`MATH_AUDIT_ODD_COMPLEMENT_ONE_SOCKET_INDEPENDENT_20260806.md`.
The cross-remainder bound and train construction are in
`MATH_THEOREM_ODD_STATIONARY_CORRIDOR_GUARD_SHUTTLE_20260806.md`.
