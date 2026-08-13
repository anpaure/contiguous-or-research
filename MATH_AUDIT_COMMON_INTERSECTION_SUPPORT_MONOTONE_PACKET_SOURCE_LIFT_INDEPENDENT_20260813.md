# Independent audit: common-intersection aggregate-support packet lift

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_COMMON_INTERSECTION_SUPPORT_MONOTONE_PACKET_SOURCE_LIFT_20260813.md`  
**Audited and corrected source SHA-256:**
`b71a6178df56e14fe1a16f9aa89eb890dcff95254ecc384848df458a9797ea82`  
**Verdict:** **PASS for the owner-edge immediate-upper row, after a
substantive scope correction.**  It does not lift the selected MSW `q2`
turn current of the counter-carry packets.

## 1. Exact width-`d+2` current

At one planted fragment

\[
                 (X_i,C_1,\ldots,C_d,Y_i),
\]

the two owner windows are `A_i=H union X_i` and `B_i=H union Y_i`.
After moving the complete tagged residual beginning at `Y_j`, the new seam
has owners `A_i,B_j`.  Every width-`d+2` source interval avoiding a changed
seam stays inside one transported residual path.  At a changed seam, the
one interval beginning at `X_i` has old/new values

\[
                         A_i\cup B_i,
             \qquad     A_i\cup B_j.
\]

An interval starting later is a common-history suffix followed by a
literal prefix of the same tagged residual and maps back to its old seam.
Cut separation prevents a second changed seam from appearing before the
complete intervening left block.  Therefore the signed width-`d+2`
current is exactly the aggregate ledger in (1.9), including multiplicity.
The support inequality (2.1) is consequently sufficient and necessary for
no old support casualty in that row.

## 2. Strict-lower transport and residence

A seam-crossing interval which reaches `X_i` contains
`H union X_i=A_i`, of rank `R`.  Every strict-lower seam interval is thus
a history suffix followed by a prefix of one tagged residual.  Moving it
to the old seam before that same residual preserves its complete literal
word, width, value, and occurrence tag.  The inverse residual permutation
gives bijectivity.  This remains valid with several cuts on one old cyclic
component because the cuts define disjoint occurrence-labelled residual
paths.

The corrected source explicitly assumes cyclic ambient source words of
length at least `d+1`.  Every source occurrence then contributes to `d+1`
consecutive owner windows.  Positive supports are unions of such cyclic
blocks, so every nonempty positive component has length at least `d+1`.
No zero-gap conclusion follows.

## 3. Essential MSW bookkeeping boundary

The counter-carry search works in the bipartite incidence factor between
rank-`R` owners `O` and selected q1 colours `Q`.  At a toggled incidence,
let `E` be the other selected q1 colour at `O`.  Its searched current is

\[
                         E\cup Q^-
             \longmapsto E\cup Q^+.
\]

This is the union of two consecutive q1 colours, equivalently the union of
three consecutive owners.  In a depth-`d` source it belongs to width
`d+3`.  By contrast, the theorem's ledger

\[
                         A_i\cup B_i
             \longmapsto A_i\cup B_{\pi(i)}
\]

is the union of two consecutive owners, at width `d+2`.  An alternating
owner--q1 incidence circuit preserves that q1 edge-colour row, so its
width-`d+2` current can be zero while its searched `q2` turn current is
nonzero.

Accordingly the common-intersection sizes found in the rank `8,10,12`
packets certify prospective strict-lower transport and positive residence,
but the present theorem does not certify their counter-carry support
ledger after source planting.  A valid extension must retain the untouched
mate `E`, or equivalently a third owner occurrence, and prove the complete
width-`d+3` cut-current identity.  Turn-faithful exterior chronology is a
genuine additional hypothesis.

## 4. Corrections incorporated

The audit incorporated the following proof-scope corrections:

1. the ambient source is explicitly cyclic and occurrence-labelled;
2. the controlled row is named the owner-edge immediate-upper row;
3. Corollary 3.1 is restricted to owner-edge head rethreads represented by
   the displayed permutation; and
4. the selected MSW `q2` turn ledger is explicitly excluded and its first
   missing datum is identified.

At that corrected scope, no further flaw was found.

