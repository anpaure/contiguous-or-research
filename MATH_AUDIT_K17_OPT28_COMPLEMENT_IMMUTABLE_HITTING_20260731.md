# OPTIMAL-28 complement: 724 immutable residence rows and a 452 one-edge hitting floor

Date: 2026-07-31  
Status: exact scoped audit; not a `K17` obstruction and not a move-count bound for circuits

## Result

Fix the authenticated six-swap macro forest and the connected OPTIMAL-28
marked packet.  The marked packet consists of `134` macro components,
`171` macro objects, and `133` old-only `U` singleton objects: `304`
objects and `4108` rank-nine owners in one literal cyclic interval.

After removing this packet, `257` fixed complement macro components contain
exactly `724` strict owner runs `0-1^r-0` with `r<4`:

```text
owner length 2: 320
owner length 3: 404
```

Every such run maps to a facet run of length `r-1<3`.  Its `r+1` entering,
internal, and leaving owner adjacencies are all fixed inside one complement
macro component.  Consequently residual old-`U` b-flow, component
permutation, and component reversal cannot change it.

The anatomy splits exactly as follows.

* `227` old-coordinate length-three runs lie strictly inside `141`
  individual macros.
* `497` new-tag runs occur at fixed macro joins: `240` on `X` and `257` on
  `Y`.

For each row put its inclusive support interval on the linear owner-edge
order of its component.  Earliest-finish interval stabbing gives `452`
points.  The same greedy steps select `452` pairwise disjoint witness
intervals, so packing and transversal numbers agree:

\[
                  \tau(\mathcal I)=\nu(\mathcal I)=452.
\]

Thus any actuator catalogue in which one actuator changes or replaces at
most one adjacency of these frozen component words needs at least `452`
actuators.  This hypothesis is essential.  An occurrence substitution or
an incidence circuit can change several owner adjacencies at once, so
`452` is **not** a lower bound on the number of such moves.  Hitting every
old support is also only necessary: replacement seams can create new short
runs.

Two finer exact transversals are useful for catalogue design:

```text
227 strict within-macro rows:       155 arbitrary interior cut sites
497 new-tag fixed-join rows:         305 existing macro-boundary sites
```

## Complete radius-one marked-bank screen

There are `1430` one-occurrence alternatives around the six-swap state.
Exactly `441` have no changed construction link incident with any of the
`171` frozen marked macro objects.  Rebuilding every one of these forests
shows that `438` preserve all `134` marked component signatures.  The
remaining three pass the node-disjoint screen but occupy a selected empty
port component and therefore do not preserve the complete packet:

```text
z= 2883  (0,1389) -> (0,4525)
z=14944  (0,1808) -> (0,5315)
z=20112  (0,1395) -> (0,3910)
```

The unique best fully preserving single change is

```text
z=18521  (0,4403) -> (0,5651)
```

It hits seven baseline rows, creates one new row, and changes the immutable
count only from `724` to `718` (`225` old-coordinate and `493` tag rows).
Against the frozen carrier's rank-ten ledger its fixed-edge delta gains no
current hole and loses the two unique colours `0x0ec5b,0x1695b`.

There are upper-friendlier columns.  For example `z=3238`, `z=3370`, and
`z=12490` each leave `719` immutable rows while gaining two current
rank-ten holes and losing no current unique rank-ten colour.  These are
only fixed-edge screens; they do not by themselves define a new residual
factor.

The compact `441`-row catalogue records, for every screened alternative:

* literal fixed owner edges added and removed;
* signed owner-degree, rank-eight intersection, and rank-ten union deltas;
* the complete macro-component signature hash;
* exact post-packet port demands and lower-`q1` applicability;
* authenticated static component-interval provider deltas for ranks
  `10,11,12`; and
* a trial using the old connected residual `U` assignment.

All `441` old-factor trials have invalid port incidence.  Therefore none
has a sound inherited chronology: connectivity, literal `Z` residence,
and rank-`10/11/12` interval replay are explicitly `null`, not inferred.
A fresh conditioned residual b-flow is required for every column.

## Scope

This proves a fixed-forest anatomy theorem and a one-edge-actuator hitting
floor.  It does not rule out multi-edge incidence circuits, a different
occurrence transversal, an unrestricted owner/lower-`q1` factor, or a
nonflat compiler.  It does not assert deep-shadow service, a common cap, or
a `K17` word.

## Artifacts

```text
scratch/audit_k17_opt28_complement_immutable_hitting_20260731.py
  SHA256 3e5e72f374e2969750f5c94d4198f330926127152fa2b605265e7a9c34f2c14e

scratch/k17_opt28_complement_immutable_hitting_20260731.audit.json
  SHA256 c27009a318f73404803027b57fa50cc08c6b0c4e89f76a15ce11aa6794344a45
  payload 9e9ccc412b02a8741159972ab4bd935ff0519c3d6b1da58115889296d32c4ca2

scratch/k17_opt28_complement_radius1_columns_20260731.json
  SHA256 d2f77df2c97f95f63cb724ad991cd7ae8d3b21b6dbd1f80c34f8df59016da2ac
  payload 606ffdf8c418db0f83ca8f1dd021d7ead286c3e05eecaec1040a40d22bfb916b
```

The final full replay ran on one H100 CPU core in
`/home/amodo/or15/work/laneL_opt28_complement_audit_20260731`, exited `0`,
used `133572 KiB` peak RSS, and took `2:31.60` wall time.  Both JSON payload
hashes independently replay from the copied local files.
