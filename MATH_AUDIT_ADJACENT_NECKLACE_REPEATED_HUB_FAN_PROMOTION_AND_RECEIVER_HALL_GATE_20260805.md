# Audit: repeated-hub fan promotion and its receiver Hall gate

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_REPEATED_HUB_FAN_PROMOTION_AND_RECEIVER_HALL_GATE_20260805.md`  
**Method:** split-position, matching-state, zero-count, and Hall replay; no
search  
**Verdict:** PASS as a fixed-cut-level reduction.  It does not establish
the receiver Hall inequalities or cross-level regeneration.

## 1. Split compatibility

Two selected edges over one hub cannot be the two edges of one `P_3`
split block, because those edges share the middle expansion.  In one
merged gap, distinct blocks have endpoint-cut sets

\[
                         \{a,a+1\},
 \qquad                  \{a+6t,a+6t+1\},
 \qquad t\ne0,
\]

whose cyclic separation is at least five before reaching a hub boundary.
In distinct hub gaps, every inserted cut is at distance at least four from
the intervening old cut.  Thus every anchor/donor endpoint pair really is
a 2-independent double expansion.

## 2. Petal matching state

An odd circulation petal is an odd cycle through the critical endpoint
`x` and hub `h`, plus the tail `hy`.  If `h` is free, use `hy` and match
the cycle minus `h`; all vertices are covered.  If `h` is already used,
match the cycle minus `h`; exactly `y` is exposed.  Reversing the shifted
cut reverses which endpoint is exposed.

Therefore a colour class with `d` selected edges uses one active petal
and `d-1` passive petals.  It has exactly `d-1` exposed endpoints.  Each
chosen double expansion is adjacent to one exposed endpoint and covers it.
This proves the one-hub fan matching with no parity omission.

## 3. Collision replay

At one cut level, distinct pointed shifted edges have distinct nonhub
circulation vertices by the fixed-level injectivity theorem.  Quotient
coalescence occurs only for rotated pointed data and is already removed
when the input edges are taken as necklace edges.

A receiver has `k+1` cuts and hence `k+1` zero coordinates.  A nonhub
circulation vertex from a `k`-cut endpoint has `k` or `k-1` zeroes.  Thus
no receiver can collide with a petal interior at this level.  The theorem
correctly does not assert the analogous statement across neighboring cut
levels.

## 4. Hall equivalence

After one anchor is fixed per hub colour, every excess petal needs exactly
one physical receiver.  A receiver can serve at most one job in a matching.
Thus any fan-promotion lift gives an injection from jobs to their legal
receiver lists.  Conversely an SDR supplies the distinct double-expansion
vertices required by the one-hub theorem.  This is precisely ordinary
bipartite Hall:

\[
                         |N(X)|\ge|X|
 \qquad(X\subseteq J_k).
\]

The lists are occurrence-coalesced before Hall is applied.  Hence the
theorem does not confuse four pointed endpoint choices with four physical
necklace receivers.

## 5. Scope boundary

The receiver is a critical state at the next cut level.  If a separately
chosen next-level matching already uses it, consuming the receiver reopens
that matching edge.  This is why the theorem is only a fixed-level
reduction and why its final two open rows—joint Hall across levels or a
top-down alternating-ear order—are necessary.

The corrected repeated-colour example is literal: both edges in

\[
 (4,17,4,6)-(5,16,4,6),
 \qquad
 (10,11,4,6)-(11,10,4,6)
\]

delete to `(21,4,6)`, and their cut-position pairs are separated by at
least five.  It validates the need for the reduction without relying on
the former invalid `(9,9,h)` display.
