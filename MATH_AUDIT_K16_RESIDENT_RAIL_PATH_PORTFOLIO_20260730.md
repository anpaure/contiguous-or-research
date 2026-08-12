# Exact resident quotient-rail portfolios for the K=16 two-rail skeleton

## 1. Why the first exact A/B pair cannot work

The independently audited paths

```text
scratch/claude_exact_arail_n15_20260730.audit.json
scratch/claude_exact_brail_n15_20260730.audit.json
```

solve their respective quotient label problems, but an exact open-path phase
audit gives `INFEASIBLE` for each rail separately, in both orientations.  The
audit imposes physical Johnson adjacency and positive-run residence on every
run bounded strictly inside the path; both endpoint collars are omitted.
Thus the earlier 32 affine/reversal pair failures are not primarily a bad seam
choice: neither displayed chronology has any internally resident gauge.

The diagnostic is

```text
scratch/audit_k16_rail_path_phase_residence_20260730.py
```

and its scope is intentionally only one open rail.

## 2. Exact static single-rail model

The replacement search is

```text
scratch/search_k16_resident_rail_path_portfolio_20260730.py
```

For every selected ordered quotient arc it chooses one exact physical witness

```text
(intersection-label orbit, phase increment).
```

At each quotient vertex it stores the previous three inserted coordinates.
For a selected physical transition `i -> j`, with inserted coordinate `b` and
deleted coordinate `a`, the constraints are exactly

```text
a not in history[i]
history[j] = (b, history[i][0], history[i][1]).
```

The dummy-to-start arc initializes the history with a sentinel, so runs
touching the left endpoint remain free.  The end-to-dummy arc carries no
deletion, so runs touching the right endpoint remain free.  This is the exact
open-path convention needed by a later two-seam collar.

Palette semantics are literal:

* `cover` requires every rank-`r-1` necklace label to be chosen by an edge;
* `rainbow` uses every such label at most once.  With 429 vertices and 428
  path edges, this is exactly the one-missing-label B condition.

The old lazy version had not found an `n=9` A rail after 578 sound motif cuts.
The static model finds an exact resident `n=9` A-cover path in 2.04 seconds and
an exact resident B-rainbow path in 1.53 seconds.  This is the regression for
the insertion-history encoding.

## 3. Endpoint and seam collar

`--seam-b-path` fixes one transformed resident B path and adds, before the A
search:

1. `A_end subset B_start`;
2. `rot(A_start,1) subset B_end`;
3. the missing B label is the A start or A end necklace;
4. the B-to-A seam deletion avoids the last three B insertions;
5. A's initial history is `(top, last-B-insertion, previous-B-insertion)`;
6. the first three B deletions avoid the history propagated through the
   A-to-B seam.

These are exactly the two positive-residence collars, not a heuristic endpoint
score.

A solver-free portfolio audit enumerates both rail orientations, every
relative multiplier in `Z_n^*`, and every relative translation:

```text
scratch/audit_k16_resident_rail_portfolio_compatibility_20260730.py
```

It replays the complete `n`-revolution physical lift, both seams, missing-label
absorption, Johnson adjacency, and cyclic positive residence.  Upper-q1,
deeper shadows, and compiler feasibility remain outside its scope.

On an uncoupled `n=9` 16-by-16 resident portfolio, only 77 of 55,296 affine
variants pass both seam containments.  The closest failures have exactly nine
bad runs of length three, one rotation orbit, all beginning at the A-to-B seam.
This proves that endpoint containment alone is insufficient and motivated the
hard collar above.

The complete pipeline passes a known smaller case.  At `K=8` (`n=7`, depth
two), the static search exhaustively found ten resident A-cover paths and ten
resident B-rainbow paths up to the imposed endpoint-pair exclusions.  The
complete affine compatibility audit found a literal two-seam PASS after 1,008
tested variants.  It replayed all seven revolutions, Johnson adjacency,
missing-label absorption, and cyclic residence.  The frozen H100 artifact is

```text
scratch/k8_staticresident_portfolio16_compatibility_20260730.audit.json
sha256 adf303768d4da4880f13566c86779d002f7a58f04557e57576c2ffa0e1ad2a05
```

This is a genuine end-to-end regression of the displayed two-block skeleton,
not merely two independently satisfiable rail models.

## 4. K=16 live scope

For `n=15`, rank 7 A-cover has:

```text
429 quotient vertices
335 required label orbits
24,182 arc variables (including dummy arcs)
23,996 exact label/delta witness variables
```

Model construction used about 2.20 GiB RSS.  The first 8 GiB A and B runs both
reached their address-space guards after about 3.5 minutes; this is
`RESOURCE_LIMIT`, not infeasibility.  Resource-distinct 12 GiB unhinted and
artifact-hinted A/B searches were then launched on H100 CPU, two workers each,
with explicit 1,800-second solver limits.

No emitted member will be called a K=16 carrier until it passes the independent
portfolio compatibility replay and the still-separate upper/deeper/compiler
gates.

## 5. Phase-free moving-frame compression

The absolute phases can be eliminated completely.  Store every insertion
history in the canonical coordinate frame of its quotient vertex.  For one
exact edge option

```text
(u,v; label, voltage delta, deleted a, inserted b),
```

the residence and transport equations are

```text
a not in h_u,
h_v[0] = b-delta mod n,
h_v[j] = h_u[j-1]-delta mod n.
```

The sentinel is fixed under transport.  This is equivalent to the expanded
phase model because a physical coordinate represented by `x` at `u` is
represented by `x-delta` at `v`.

The independently implemented compact search is

```text
scratch/search_k16_moving_frame_resident_rail_portfolio_20260730.py
```

It exactly replays the expanded model at `n=9`; A/B solve times improve from
`2.04/1.53` seconds to `0.62/0.81` seconds.  At `n=15` the build uses about
1.49 GiB RSS and contains only

```text
24,182 arc variables
23,996 exact physical edge-option variables
1,287 history integers.
```

This replaces roughly 360,000 phase-by-option conjunction variables and their
millions of reified history constraints.  The compact A/B searches are the
current authoritative computational lane; the expanded model remains an
independent small-case cross-check rather than a resource competitor.
