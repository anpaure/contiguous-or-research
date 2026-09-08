# The minimal MNW phase creator has a unit q2 debt, and opposite SDR phases do not remove the shared-edge conflict

**Date:** 2026-08-07  
**Method:** literal edge overlap, boundary parity, and the exact source-hex
classification; no computation or search  
**Status:** unconditional obstruction to two minimal augmentations of the
one-edge-defective B8 annulus.  A larger compound phase creator remains
possible.

## 1. Exact shared edge

Use the notation of the singleton-defect annulus theorem.  The fused
source cycle

\[
 C_{01}=O_a-A-O_2-D-O_3-B-O_c-C-O_a
\]

has selected source incidence

\[
 e_*=(01O_a,01A)
     =(0110001101,0110001111).                     \tag{1.1}
\]

The endpoint-transfer transport face `H_leaf` has cyclic edge row

\[
 XR, X_2R, X_2M, X_9M, X_9Q, XQ             \tag{1.2}
\]

with status word

\[
                         101010.                    \tag{1.3}
\]

Here

\[
 X_2=01O_a,qquad M=01A,
\]

so its selected edge `X_2M` is exactly `e_*`.

Thus the source cycle and the available orientation of `H_leaf` both
remove the same old selected physical incidence.

## Theorem 1.1 (opposite-phase ordered-SDR no-go)

There is no ordered two-SDR `F=M_0 dotcup M_1` in which the current
orientation of `C_{01}` is a phase-0 balanced packet and the current
orientation of `H_leaf` is a phase-1 balanced packet.

The same conclusion holds with phases zero and one exchanged.

### Proof

The old bank of the source packet contains `e_*`, so the phase-0
hypothesis requires `e_* in M_0`.  The old bank of `H_leaf` also contains
`e_*`, so the phase-1 hypothesis requires `e_* in M_1`.  But the two
perfect matchings of an ordered two-SDR are edge-disjoint.  This is a
contradiction.  \(\square\)

This is not a missing choice of component orientation.  Reversing the
orientation of a factor component exchanges the names `M_0,M_1` on every
edge of that component but cannot give one physical incidence both
colours.

## 2. Reversing the leaf face is not a free workaround

The reverse leaf packet would take the complementary triple in (1.2) as
its old bank and would add the triple containing `e_*`.  In the inherited
gamma--alpha factor that complementary triple is not selected, so the
reverse face is not presently alternating.

Moreover, in the phase-resolved balanced-switch lemma every new edge is
required to lie outside the initial two-factor.  The reverse packet would
add `e_*`, which already belongs to the source packet's old bank.  Hence it
violates the stated private-new-edge premise unless another simultaneous
packet first vacates and phase-transfers that incidence.  Such a transfer
is an additional operation, not a recolouring of the same two packets.

## 3. What a boundary phase creator must do

After `H_leaf` is toggled, the destination incidence is repaired but the
source incidence `e_*` is removed.  The source cycle therefore has exactly
one wrong edge and is not alternating.  Any augmentation that later uses
the source cycle must, before that use, change the status of `e_*` once
more or change at least one additional source-cycle edge so that the whole
cycle phase becomes alternating.

The smallest direct option is a second incidence hexagon at the source
owner

\[
                         Y=01O_a=0110001101          \tag{3.1}
\]

which swaps the selected rail colour `R=Y+1` back to the source colour
`M=Y+9` without touching the repaired destination edge.

The exact source-hex classification proves that, apart from simply undoing
`H_leaf`, there is exactly one such alternating hexagon: its active core
label is `c=3`.

## Theorem 3.1 (unique one-hex unlock has unit q2 debt)

Let `H_3` denote that unique nonreversing source-restoring hexagon.  Then

\[
 \partial_2(H_{\rm leaf}+H_3)
   =[1010101111]-[1100101111].                     \tag{3.2}
\]

The negative target

\[
                         J=1100101111               \tag{3.3}
\]

has exactly one canonical provider, namely the occurrence removed by
`H_3`.  Therefore the unique one-hex boundary unlock is not q2-support
safe.

### Proof

Uniqueness and (3.2) are the exact conclusions of the source-boundary
restore classification: the only admissible nontrivial core among
`c in {3,7,8,10}` is `c=3`.  The same theorem gives the unique inverse
witness `(5,9)` for `J`.  Hence its load falls from one to zero.  \(\square\)

The theorem asserts only the necessary boundary repair.  It does not
claim that the auxiliary transport rails have already reached the phase
needed for the remaining annulus sweep; that stronger row still belongs
to the ordered host.

## 4. Sharp finite-module consequence

Two tempting minimal repairs are now excluded.

1. **Put the source cycle and leaf face in opposite SDR phases.**  This is
   impossible by Theorem 1.1 because their old banks share `e_*`.
2. **Append one source-restoring hexagon after the leaf face.**  The only
   such nontrivial hexagon opens the unit q2 hole `J` by Theorem 3.1.

Therefore a support-safe ten-bit module needs a genuinely compound phase
creator.  It must do at least one of the following:

* restore `e_*` while simultaneously providing a second occurrence of
  `J`;
* change a larger even set of boundary incidences whose net q2 negatives
  all retain providers; or
* implement an occurrence-level phase transfer in which every edge moved
  between `M_0` and `M_1` is vacated on one side and installed on the
  other, with the complete colour and socket ledger balanced.

The existing direct `J` creator only relays the unit hole to `U`, and the
known longer `C_8` chain relays it again to `R_0`; neither is a closed
phase creator.  Hence none of the currently frozen local continuations is
yet the required augmentation.

## 5. Revised exact target

The finite ordered-two-SDR target should no longer be stated as the bare
B8 source annulus or as two phase-resolved copies of its first source and
transport cycles.  The proof-safe target is:

> **Support-closed phase-transfer module.**  In one ordered two-SDR,
> realize the inherited gamma--alpha boundary together with a compound
> phase-transfer circuit whose final boundary enables the complete B8
> carry, whose signed q2 negative support retains literal providers, and
> whose combined socket permutation agrees with the higher connector
> interface.

This module may still be finite on ten prefix bits, but it requires at
least one ingredient beyond the current source `C_8`, `H_leaf`, and the
unique one-hex boundary restorer.

