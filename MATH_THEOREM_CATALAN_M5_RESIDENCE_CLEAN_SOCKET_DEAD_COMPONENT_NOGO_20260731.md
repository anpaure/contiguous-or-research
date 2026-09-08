# A two-dead-socket obstruction for the residence-clean `m=5` forest

Date: 2026-07-31  
Status: solver-free no-go for endpoint-only joining of the fixed item 2188
forest; exact local socket criterion; no obstruction to a further interior
rethread

## 0. Verdict

Item 2188 proves that the immediate Catalan palettes admit a 42-path forest
with no internal positive coordinate run of length one or two.  Endpoint
joining alone cannot complete that particular forest.

The exact endpoint catalogue has 84 formal ports, 304 legal formal Johnson
pairs and 293 distinct physical connector edges.  Raw topology and connector
palettes are not the problem: a literal 42-edge connector matching is one
component cycle and uses 42 distinct lower and 42 distinct upper connector
colours.

Residence is the obstruction.  Only 69 of the 304 formal pairs are
pair-safe, and 15 ports have pair-safe degree zero.  Both ports of the path

~~~text
01f 21e 31c 398 3d0 3e0 1e8 1ac
~~~

are dead.  Every legal neighbour at either end creates a bounded positive
run of length one or two.  The two resulting defect collars are edge-disjoint
for every choice compatible with a connected component cycle.  The unique
overlap choice joins both ends to the two ends of component 13 and isolates
those two components as a 2-cycle.  One arbitrary opening edge therefore
cannot destroy both defects.

Consequently there is no endpoint-only, depth-two-resident Hamilton
chronology of the fixed item 2188 path bodies.  This is a solver-free local
no-go before the 21 deeper targets, connector-colour all-different rows or
the lower compiler.  The smallest escape is another interior actuator which
creates a pair-safe neighbour for at least one of the two dead sockets (or
otherwise splits/replaces this component attachment).  At this `m=5` base
the clean quotient has `h=1`, so primitive voltage is vacuous.

## 1. Exact pair-safe seam criterion

Fix an oriented endpoint port `p` of a path fragment and write its inward
coordinate ray as

\[
             b_0,b_1,\ldots,b_{r-1},
\]

where `b_0` is the endpoint.  For a second port `q`, a physical seam joins
the two rays in the local word

\[
 b_{r-1},\ldots,b_1,b_0,c_0,c_1,\ldots,c_{s-1}.       \tag{1.1}
\]

### Lemma 1.1 (local transfer test)

A legal Johnson seam `pq` is pair-safe for depth two if and only if (1.1)
has no positive coordinate run of length one or two which is bounded by
zeroes inside the two-fragment collar and meets one of the two seam
endpoints.

Equivalently, for every coordinate retain at each port:

1. the endpoint bit;
2. the inward positive-run length, capped at three;
3. whether that run reaches the far end of the whole fragment; and
4. the corresponding far-end bit/run state.

If the seam bits are `11`, the two endpoint runs merge and are rejecting
exactly when the merged run is internally bounded and has total length below
three.  If they are `10` or `01`, the positive endpoint run becomes bounded
at the seam and is rejecting exactly when its other end is already bounded
and its length is below three.  The `00` case creates no positive seam run.

#### Proof

The old fragment interiors are already residence-clean.  Thus a newly
bounded short run must meet the new seam, and its maximal local extent is
read exactly from the two endpoint rays.  Conversely every short run found
by this scan is bounded wholly inside (1.1); no exterior connector or path
orientation can lengthen it.  Reversal preserves its length and its two
bounding zeroes. \(\square\)

This criterion is precisely the coordinate-run part of the full exported
collar signature in
`MATH_THEOREM_CATALAN_INTERIOR_RETHREAD_GAIN_BRAUER_ACTUATOR_20260731.md`.
It is separate from palette balance, affected-witness coverage and
gain--Brauer topology.

## 2. The literal 11-row certificate

For the left socket `01f`, all five legal endpoint neighbours fail:

| neighbour | forced short run |
|---:|---:|
| `05e` | bit 0, length 1 |
| `08f` | bit 0, length 2 |
| `097` | bit 0, length 2 |
| `21d` | bit 1, length 2 |
| `217` | bit 0, length 2 |

For the right socket `1ac`, all six fail:

| neighbour | forced short run |
|---:|---:|
| `0ec` | bit 6, length 2 |
| `1b4` | bits 2, 3 and 4, each length 2 |
| `0bc` | bit 2, length 2 |
| `1b8` | bit 2, length 1 |
| `12e` | bit 1, length 1 |
| `13c` | bit 2, length 2 |

Every listed run and its bounding collar are replayed literally by the audit.
The safe-port degree histogram on all 84 formal ports is

\[
 0^{15}1^{30}2^{19}3^{14}4^2 5^4.                 \tag{2.1}
\]

## 3. Two-dead-socket theorem

Let `I` be the fixed involution pairing the two ports along every path body,
and let `M` be any physical endpoint connector matching.  A cyclic closure
requires `I union M` to be one occurrence cycle; a linear chronology is the
same object with one edge opened.

### Theorem 3.1

No connector matching and no single opening edge produce a depth-two-resident
Hamilton word while keeping all 42 item 2188 path bodies intact.

#### Proof

Each of the two ports of component 0 has pair-safe degree zero, so every
selected connector at that port creates one of the short-run collars in
Section 2.

For the five-by-six left/right neighbour choices, the audit compares the
literal collar edge sets.  In all 29 choices using distinct neighbour
components, the canonical left and right collars are edge-disjoint.  Hence
one opening edge can destroy at most one of them.

The only intersecting pair is

~~~text
01f--08f  and  1ac--0ec,
~~~

whose collars share the forest edge `08f--0ce`.  The two neighbour ports are
the two ends of component 13.  Selecting both connectors gives every port of
components 0 and 13 degree two inside their two-component block, hence an
isolated 2-cycle; it cannot occur in a connected 42-component closure.

Thus every connected closure has two edge-disjoint forced defect collars.
Opening one arbitrary connector or forest edge leaves at least one collar
internal.  The resulting word is not depth-two resident. \(\square\)

For a direct Hamilton-path formulation, the same proof says that exposing
one dead socket as a global boundary still leaves the other socket internally
matched to an unsafe seam.  Exposing both would isolate component 0 from the
remaining 41 fragments.

## 4. Separation from socket topology and palettes

The raw endpoint graph itself is healthy: it has no dead port.  The frozen
audit includes a 42-edge connector witness whose component projection is
connected and 2-regular.  Its lower connector labels are all distinct, and
so are its upper connector labels.  The canonical physical connector-list
SHA-256 is

~~~text
82355eba85f37805630a5883cfba2432b4257c9edd07e3c6579f9c8a546a8afb
~~~

This diagnostic witness proves that gain--Brauer one-cycle topology and the
cap-two connector palette rows pass before the run filter is imposed.  It is
not a resident chronology.

The pair-safe no-go also precedes the 21 internal deeper-shadow debts of item
2188.  Those debts do not weaken Theorem 3.1; adding their service clauses can
only remove connector matchings.

## 5. Reusable boundary law and scope

For any fixed residence-clean path forest, form the pair-safe port graph by
Lemma 1.1.  A cyclic endpoint-only closure requires a perfect connector
matching in this graph plus the gain--Brauer one-cycle test.  A linear
closure may expose two formal ports, but a component whose two ports both
have pair-safe degree zero cannot be embedded in a Hamilton chronology with
any other component.  More generally, arbitrary openings must stab every
forced short-run collar; disjoint collar families give an immediate hitting
lower bound.

This is a necessary local law, not an all-`m` construction.  It does not rule
out:

1. another exact rank-4/rank-6 matching;
2. an additional interior rethread of item 2188;
3. a move which changes path bodies and connector sockets jointly; or
4. a controlled-debt macro which exports the changed pairing/run/witness
   state and is accepted only after joint stacking.

The all-`m` seam-run theorem still shows that aggregate residence mass is
ample.  The present obstruction identifies its missing local distribution:
component 0 must acquire at least one usable pair-safe socket.

## 6. Reproduction

Run

~~~text
python3 scratch/audit_catalan_m5_residence_clean_socket_dead_component_h2_20260731.py
~~~

The replay authenticates the literal candidate, reconstructs all 304 formal
endpoint pairs, scans every two-fragment coordinate collar, checks the
11-row certificate and the unique overlap exception, and independently
validates the raw colour-injective one-cycle diagnostic witness.
