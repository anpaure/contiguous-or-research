# The protected J7 path has no support-eight splice in the frozen MMM cycle

Date: 2026-08-01  
Lane: H2 / bounded J7 component splice  
Status: **exact finite no-go at changed-tail support eight; no statement for
support at least nine, another quotient cycle, or global K17.**

## 1. Frozen scope

The host is the authenticated quotient cycle

```text
scratch/k17_mmm_quotient_cycle.tsv
SHA-256 4439b89f56b513416a418cbe0f7e8d9fa9e1bff9538ff432c497aa8cb473145f
```

It contains all `1430` rank-nine owner orbits and all `1430` rank-eight
lower-q1 orbits exactly once, with total voltage `1 mod 17`.

The protected J7 owner path may be used in either direction:

\[
  A=7711\to B=8077\to C=13623,
  \qquad C\to B\to A.                                \tag{1.1}
\]

Both orientations have a literal nonempty six-cell depth-three source and
the same certified type IDs `(3,7,0)`.  Same-successor rephasings are
allowed throughout the enumeration: a changed tail may retain its successor
orbit while changing its voltage and lower/upper labels.

The corrected support-at-most-seven theorem is
`MATH_THEOREM_H2_K17_J7_UNIT_VOLTAGE_COMPONENT_SPLICE_SUPPORT8_GATE_20260801.md`.
Its exhaustive counts are `179` forward and `3001` reverse closure states,
with zero solutions.

## 2. Exact support-eight enumeration

Let `sigma` be the frozen successor permutation and let

\[
             S=\{u:\text{the labelled outgoing arc at }u\text{ changes}\}.
                                                                    \tag{2.1}
\]

For every selected quotient Johnson arc `u -> v` with lower label `l`, two
tails are forced into `S`:

\[
                    \sigma^{-1}(v),\qquad\lambda^{-1}(l),           \tag{2.2}
\]

where `lambda` is the old lower-rainbow tail-to-colour bijection.  At a
closed leaf, exact owner and lower-q1 preservation is equivalent to

\[
 \{v_u:u\in S\}=\sigma(S),\qquad
 \{l_u:u\in S\}=\lambda(S).                            \tag{2.3}
\]

The forward seed forces five tails and the reverse seed forces four.  The
audit enumerates all `72` voltage-labelled quotient Johnson arcs at every
new tail, applies (2.2), retains same-successor rephasings, and stops a
branch only when its closure exceeds eight.

### Theorem 2.1

There is no labelled successor exchange with `|S|=8` which contains either
orientation of J7 and preserves both the owner-orbit and lower-q1-orbit
bijections of the frozen cycle.

#### Proof

The exact closure search visits

```text
forward:  2,355 states
reverse: 39,895 states
```

and has zero leaves satisfying (2.3).

For completeness, consider any alleged support-eight exchange.  Starting
with its forced J7 arcs, whenever the audit processes a changed tail, choose
the arc used by the alleged exchange.  Both tails added by (2.2) belong to
its final support, so this branch never exceeds eight.  Once every forced
tail is processed, the branch reaches its full closed support and satisfies
(2.3), contradicting the zero-leaf census.

An independently balanced changed component disjoint from the forced J7
closure cannot be missed.  Its removal would leave a smaller closed J7
exchange; the corrected support-at-most-seven theorem excludes that case.
Thus the closure enumeration is exhaustive for all support-eight exchanges.
\(\square\)

## 3. Downstream filters and exact interpretation

The audit implements the following filters after owner/lower feasibility:

1. the replacement successor permutation must be one 1430-cycle;
2. its voltage

   \[
      1+\sum_{u\in S}(\delta'_u-\delta_u)\pmod {17}                 \tag{3.1}
   \]

   must be nonzero;
3. the 24,310-owner physical lift must have no bounded positive run below
   four intersecting a J7 block or either J7 boundary; and
4. the eight new upper-q1 orbit labels must be distinct and must create no
   new missing upper-q1 orbit relative to the old host.

The frozen upper-q1 host itself covers `996/1144` target orbits, with `148`
holes and `434` repeat units.  These values are independently replayed.

For support eight, however, all four downstream counts are zero because
their owner/lower input family is empty.  This is a **vacuous downstream
filter**, not evidence that voltage, residence or upper-q1 individually
caused the obstruction.

There are therefore no exact survivors to list; the survivor TSV contains
only its schema header.

## 4. Smallest remaining catalogue

The first open fixed-cycle class is now `|S|=9`.  It must retain:

* both J7 path arcs and their literal six-cell source/type state;
* the head and lower closure equalities (2.2)--(2.3);
* one-cycle topology and nonzero voltage;
* the signed J7 boundary-run state; and
* literal upper-q1 palette impact.

This support-nine statement is only the smallest remaining catalogue for
this fixed MMM owner/lower cycle.  Reselecting the lower matching, changing
the owner cycle, or embedding J7 in a path forest lies outside the theorem.
Ranks at least eleven and common-cap compilation remain downstream even if
a support-nine survivor is found.

## 5. Artifacts

```text
scratch/audit_h2_k17_j7_component_splice_support8_20260801.py
scratch/h2_k17_j7_component_splice_support8_20260801.audit.json
scratch/h2_k17_j7_component_splice_support8_20260801.survivors.tsv
```

The run is a lightweight deterministic enumeration.  It launches no SAT
solver and does not touch the active H100 global model.
