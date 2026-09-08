# Hostile audit: q4 k17 orientation-word lift fibres and Minkowski menu

**Date:** 2026-08-14

**Verdict:** **PASS** at the exact owner-orientation, additive-ledger, and
directed-phase reduction scope.  No lift-fibre nonemptiness, joint-master
feasibility, or physical resource packing is inferred.

## 1. Audited theorem

```text
MATH_REDUCTION_Q4_K17_ORIENTATION_WORD_LIFT_FIBRES_AND_MINKOWSKI_MENU_20260814.md
sha256 89b0e189917a911a4656875a0b5d3f9ba645d947bf4e6bc9a388c5420957f4ce
```

For a fixed nonself ten-row footprint, each row has two reflected owner
necklaces.  The orientation word selects one.  Therefore equality of the
ten bits is exactly equality of the oriented owner deck.  In
`u+rho(v)`, the two shores above a row have bits `eps_u` and `1-eps_v`;
they cover both necklaces once exactly when `eps_u=eps_v`.

There are 1,024 raw orientation words.  Whole-rail reflection complements
all bits and has no fixed word, leaving 512 complement classes.  Fixing one
anchor bit to zero gives the same 512 normalized fibres.  The theorem now
distinguishes these from the 1,024 unnormalized `W(M,eps)` fibres.

## 2. Anchored completeness

The anchor `A` is a physical rank-nine subset representing the chosen
reference necklace.  If the unique target-row occurrence lies in the
opposite necklace, reflect the whole witness.  Freeness of translation on
rank-nine subsets then gives one translate taking that occurrence to `A`,
and its unique owner position fixes the cyclic start.  The core, ordered
four-window, and ordered remaining six support labels are precisely the
anchored parameters

```text
                         C(9,5) 4! P(8,6)=60,963,840.
```

Thus filtering one anchored enumeration by a selected footprint and its
nine remaining orientation bits is complete modulo the declared whole-rail
reflection normalization.  This is a symbolic completeness theorem, not a
claim about the number of realized signatures.

## 3. Additive menu and phase audit

For any additive typed signature `s`, an owner-exact option contributes

```text
                             s(u)+rho s(v).
```

Writing `s(w)=s(w_0)+d(w)` gives the exact finite affine Minkowski menu

```text
                 s(w_0)+rho s(w_0)+D+rho D.
```

If the first shore `u_0` is frozen, the exact relative current is instead
the one-sided `rho(s(v)-s(u_0))`.  The theorem correctly warns that this
difference alone is incomplete when both shores are free, because the
literal baseline depends on `u`.

The rank-seven word remains directed.  Rotation is absorbed by a phase in
`Z_10`; reversal is not removed without a reversed 72-state certificate.
On phase-decorated pair options, complement normalization sends

```text
(eps,u,v,delta_u,delta_v)
  -> (1-eps,rho(v),rho(u),delta_v,delta_u),
```

so both physical shores and their phases swap.  The rows
`L3_load-unmarked=1` and `L3_load<=2` are exactly the load-one/mark-zero or
load-two/mark-one alternatives required by the frozen pure-face schedule.

## 4. Independent H100 replay

```text
scratch/verify_q4_k17_orientation_word_lift_fibre_minkowski_menu_20260814.py
sha256 41c656753323c63a19b9f5056aac8094e336fc65294d1e30472041e3a932414f

scratch/verify_q4_k17_orientation_word_lift_fibre_minkowski_menu_20260814.h100.out
sha256 844168e2e50009e64ae129fa90bdf7e889818e8e3dbcd6629628dc1619bd8d6e
status PASS
```

The replay checks all `2^20=1,048,576` pairs of orientation words, the
1,024/512/512 raw/complement/anchor counts, the anchored raw count, exact
one-sided and two-sided affine identities on a synthetic involutive ticket
group, complement/phase swapping, directed rotation-phase covariance, and
the complete local rank-seven truth table.

## 5. Scope boundary

Signature deduplication is exact only for the rows represented in the
signature.  A phase master must retain the directed rank-seven word, and a
physical master must retain witness multiplicities or regenerating keys and
all resource/collar decorations.  The theorem neither proves that an
off-diagonal fibre exists over any selected footprint nor replaces the
final simultaneous SDR/conflict, residence, topology, or actuator gates.

All finite replay and hashing ran on H100.  The Mac was used only for
reading, editing, transfer, and Git.
