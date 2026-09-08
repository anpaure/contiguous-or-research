# Audit: paired hub-fan promotion and binary socket flow

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_PAIRED_HUB_FAN_PARITY_FLOW_20260805.md`  
**Method:** literal cut-set and matching-state replay; no search  
**Verdict:** PASS with its stated fresh-receiver and exceptional-anchor
premises.  Quotient Hall and next-level extension remain open.

## 1. Two-petal replay

Let the passive endpoints carry cuts `p` and `r`.  Joint admissibility
gives the two next-level states

\[
 z_0=H\cup\{p,r\},
 \qquad
 z_1=H\cup\{p+1,r\}.
\]

The edge from the first exposed endpoint to `z_0` inserts `r`; the edge
from the second exposed endpoint to `z_1` inserts `p+1`.  The two receiver
states differ by the shifted cut `p <-> p+1`, so they are an adjacent
balanced pair.

Each passive odd cycle with its common hub deleted is an even path and is
perfectly matched.  The two vertical receiver edges cover the exposed
petal endpoints.  The common hub is deliberately not covered inside the
relative gadget; the external incoming edge covers it.  Thus no vertex is
double-used.

## 2. Parity replay

If the hub is free, one of `d` petals is active and `d-1` are passive.  If
the hub is externally consumed, all `d` are passive.  With the theorem's
convention this is

\[
                         m=d-1+\epsilon.
\]

Pairing passive petals consumes `floor(m/2)` adjacent receiver pairs and
leaves exactly `m mod 2` passive petals.  The latter needs one singleton
receiver.  This proves

\[
                         \eta\equiv d-1+\epsilon\pmod2.
\]

For `epsilon=1,d=1`, no second petal exists from which to obtain an anchor;
the explicit compatible-anchor sidecar is therefore necessary and is not
silently inferred.

## 3. Potential replay

Petal endpoints have one more cut than their hub.  Every double expansion
adds a second cut to that hub and hence lies exactly one cut level above
the endpoints.  The cut-count potential strictly increases on both paired
and singleton receiver exports.  Dependencies cannot return to a lower
level.

This acyclicity does not imply a matching by itself.  A receiver is a
physical next-level critical vertex, and the next-level matching must
extend the prescribed adjacent receiver pairs while omitting any incoming
singleton.  The theorem records this as its exact remaining extension
gate.

## 4. Quotient replay

All cut choices are literal before quotienting.  Rotations can coalesce
different pointed receiver pairs, and different hub fans can request the
same receiver orbit.  The theorem explicitly requires fresh, pairwise
distinct physical receivers and sends the quotient problem to an
occurrence-coalesced Hall selector.  Therefore its binary current law is
proved, while no unsupported orbit-packing claim is made.
