# Audit of the MNW leaf endpoint-transfer hex

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_LEAF_ENDPOINT_TRANSFER_HEX_AND_Q2_SAFE_CURRENT_20260807.md`  
**Verdict:** PASS.

## 1. Alternation

With core `K=0010001101` and active labels `1,2,9`, the hexagon owners and
colours are exactly those in (1.3)--(1.4).  In the canonical-plus-relay
factor, the touching-step rule selects additions `5,9` at `X_2`; `X_9` is a
reverse endpoint whose sole addition is `1`; mirror gamma supplies the
selected `XR` edge.  Hence the status word is `101010`.

**Result:** PASS.

## 2. q2 current

The turn at `X` changes `1110101101 -> 1010101111`; the turn at `X_2`
changes `0110101111 -> 1110101101`; `X_9` is an endpoint.  Cancellation
gives `+[1010101111]-[0110101111]`.

**Result:** PASS.

## 3. Multiplicities

The exact inverse witnesses are

\[
1010101111:(3,9),(1,10),
\qquad
0110101111:(5,9),(3,10).
\]

There are no other eligible `q` positions.  Both initial loads are exactly
two, and neither appears in the first relay current.

**Result:** PASS.

## 4. Suffix and ordering scope

Dyck suffixing preserves incidence status and inverse multiplicity.  Suffix
projection proves pairwise disjointness.  The theorem correctly notes that
the hex toggles one source-boundary edge as well as the destination edge;
it does not overclaim compatibility with a full MNW-tree completion, the
standard annulus order, or a component effect.

**Overall verdict:** PASS.
