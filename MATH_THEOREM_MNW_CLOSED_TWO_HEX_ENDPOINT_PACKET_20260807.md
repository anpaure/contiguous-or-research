# The MNW endpoint defect has a closed two-hex q2 packet

**Date:** 2026-08-07  
**Method:** exact incidence cancellation and q2 inverse multiplicities; no
computation or search  
**Status:** unconditional literal local theorem in the gamma-alpha relay
state.  The packet is q1-degree preserving, q2-support closed, and tensors
over every Dyck suffix.  Its final q1 boundary is the source-flipped state
after the first leaf face.  Annulus and spanning-hypertree compatibility are
separate.

## 1. The first leaf face

Use the already proved leaf-transfer hex `H_leaf`.  Its owners are

\[
 1010001101,\qquad0110001101,\qquad0010001111,
\]

and its exact q2 current is

\[
 \partial_2H_{\rm leaf}=[A]-[B],                    \tag{1.1}
\]

where

\[
 A=1010101111,\qquad B=0110101111.                  \tag{1.2}
\]

Both targets have canonical multiplicity two.  Thus this face by itself is
q2-support safe.  It installs the missing destination incidence and flips
one named source-boundary incidence.

## 2. The compressed companion hex

Put

\[
 K=1100100100
\]

and use active labels `10,6,4`.  The lower owners are

\[
\begin{aligned}
 Z  &=K+10=1100100101,\\
 E_4&=K+4 =1101100100,\\
 E_6&=K+6 =1100110100,
\end{aligned}                                       \tag{2.1}
\]

and the upper colours are

\[
\begin{aligned}
 P  &=K+10+6=1100110101,\\
 R_2&=K+4+6 =1101110100,\\
 R_1&=K+4+10=1101100101.
\end{aligned}                                       \tag{2.2}
\]

The touching-step rule gives:

* `Z` selects addition six, so `ZP` is selected and `ZR_1` is not;
* `E_4` is a Dyck endpoint selecting addition ten, so `E_4R_1` is selected
  and `E_4R_2` is not;
* `E_6` is a Dyck endpoint selecting addition four, so `E_6R_2` is selected
  and `E_6P` is not.

Hence

\[
 Z-P-E_6-R_2-E_4-R_1-Z                             \tag{2.3}
\]

is a literal alternating incidence hexagon.  Call it `H_*`.

Only `Z` is an internal lower owner.  Its untouched mate is addition seven,
and toggling (2.3) changes its q2 turn as

\[
  Z+\{6,7\}=1100111101
   \longmapsto
  Z+\{4,7\}=1101101101.                             \tag{2.4}
\]

Put

\[
 K_0=1100111101,\qquad F_0=1101101101.              \tag{2.5}
\]

Then

\[
 \boxed{\partial_2H_*=[F_0]-[K_0].}                \tag{2.6}
\]

The target `K_0` has exactly two canonical inverse witnesses,

\[
                         (5,8),\qquad(6,7).          \tag{2.7}
\]

Thus one copy remains after (2.6).

## 3. Closed endpoint packet

The owner, colour, and incidence supports of `H_leaf` and `H_*` are
disjoint.  They can therefore be toggled in either order.  Their complete
q2 current is

\[
 \boxed{
 \partial_2(H_{\rm leaf}+H_*)
    =[A]+[F_0]-[B]-[K_0].}                          \tag{3.1}
\]

The two negative terms have multiplicity two before the packet, and the
two earlier gamma-alpha tuples do not change either target.  Consequently
both negative terms retain a provider.  Every q2 target covered before the
packet remains covered afterward.

This gives a literal support-closed endpoint transfer with only two
incidence hexagons.  The longer sequence consisting of the direct `J` face,
the unique C8, the reverse contextual hex, and the final `R0` face has the
same incidence difference as `H_*`; all of its internal incidences cancel.
The second boundary-restoring face and its later reversal cancel as well.
They are useful as a derivation of (2.3), but are unnecessary in the final
packet.

## 4. Exact q1 boundary state

Every constituent is an alternating incidence cycle, so owner degrees and
q1-colour degrees are preserved exactly.  The companion `H_*` is disjoint
from the leaf source/destination boundary.  Therefore the final boundary
state is exactly the state after `H_leaf`:

1. the desired positive-context destination incidence is installed;
2. the corresponding source-context incidence is flipped;
3. all other named boundary incidences are unchanged.

Equivalently, this is the one-source-flipped state that the interleaved
annulus sweep was designed to consume.  Whether it is literally the first
shell of a globally plantable annulus is not asserted by this theorem.

## 5. Dyck suffixing

Append a Dyck word `v` to every owner, colour, and target.  MSW
concatenation preserves all selected-incidence tests.  Every q2 prefix in
(1.1) and (2.4) ends at height four, so the inverse multiplicities remain
exact.  Distinct suffixes have disjoint supports by suffix projection.

Hence the full bank

\[
 \{(H_{\rm leaf}+H_*)v:v\in\mathcal D_{m-5}\}       \tag{5.1}
\]

is a simultaneous, q1-exact and q2-support-closed endpoint packet.

## 6. Remaining scope

The theorem closes the literal local q1/q2 packet.  It does not yet prove:

1. that the source-flipped boundary is absorbed by a complete alternating
   `01 -> 10` annulus;
2. the component permutation of the packet after lifted closure;
3. extension of the complete suffix bank to one conflict-free MNW spanning
   hypertree; or
4. preservation of q3 and all wider upper decks.

