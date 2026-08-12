# Audit of promoted-hook marked double-zero ports

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_HOOK_PROMOTED_PARENT_MARKED_ZERO_PORTS_20260805.md`  
**Method:** independent rooted-word, inverse-map, and level-two audit; no
search  
**Verdict:** **PASS**, with the global sibling-matching row explicitly open.

## 1. Rooted identity

Substitute the displayed formula for `D_h(y)` into `1D_h(y)0`.  Relative
to `D_(h+1)`, the new outer up-step creates an empty first left bank and
the new outer down-step creates an empty last right bank.  Every old bank,
including the central bank, keeps its order and occupancy.  Therefore the
new vector is literally `(0,y,0)`.  The two new slots are adjacent only
after cyclic closure, exactly as claimed.

## 2. Cyclic inverse

Marking the inserted `00` pair removes all ambiguity: delete that pair and
contract its location to recover both `y` and the root cut.  This operation
commutes with cyclic rotation.  Hence the marked map is bijective even for
periodic necklaces; stabilizers merely identify simultaneous rotations and
do not create extra marked preimages.

The child pair is then forced to be `y+e_j,y+e_(j+1)`.  Thus two distinct
simple child edges cannot consume the same marked parent port.

## 3. Loose-hyperstar reduction

A matching in the child transfer graph uses every child component at most
once.  Distinct hyperedges can therefore share no child.  Their parent
actions lie one level lower; two hyperedges either have distinct parents or
share exactly that parent component.  At occurrence level the latter ports
are still distinct by Section 2.  Once the parents are in the old spine,
each hyperedge intersects it in one component and contributes two fresh
children, which is precisely the loose-hyperstar condition.

This deduction requires the matching hypothesis; connectedness alone is
not substituted for matching.

## 4. Two-chip row

On an odd cycle of length `2h-1`, an unordered pair of chip positions is
classified by shorter distance `d=0,...,h-1`, where `d=0` denotes a double
chip.  One adjacent unit transfer changes `d` by one, except that the move
outward at `d=h-1` is a quotient loop.  Deleting loops leaves exactly the
path `C_0-...-C_(h-1)`.

There is only one one-chip necklace.  Hence every level-two connector uses
that parent, proving the `Omega(h)` component-degree lower bound.  The
alternating path matching leaves zero nonnamed children for odd `h` and one
for even `h`.  When `h` is even, `h-1` nonnamed children cannot be partitioned
into pairs, so the one-vertex residual is parity-forced for a loose
hyperstar with both named roots preinstalled.

## 5. Scope

The theorem proves exact marked-port supply, not simultaneous separation of
all companion q2 halos.  It does not prove near-perfect matchings in the
higher chip-necklace graphs.  These limitations are stated in Section 7
and are mathematically necessary at the present stage.
