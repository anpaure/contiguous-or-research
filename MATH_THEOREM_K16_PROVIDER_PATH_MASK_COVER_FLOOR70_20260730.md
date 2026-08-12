# K16 provider-path mask-cover theorem: the separated master needs at least 70 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its audited catalogue of 211,604
direction-coherent, positive-residence-safe seams, every port permutation that
services all 93 fixed q<=3 defects selects at least

```text
56 provider seams + 14 nonprovider seams = 70 seams and cuts.
```

This is a solver-independent strengthening of the earlier provider-path
capacity floor 66.  It uses neither cut separation nor any nondefect
q1/q2/q3 preservation row, so it applies a fortiori to the full separated-port
master.

## Frozen service facts

A **provider** is a seam that gains at least one of the 45 lower-q2 or 48
upper-q3 zero-baseline masks.  Exact independent audits give:

```text
defects                                      93
provider seams                            5,425
one-hit provider seams                    5,232
two-hit physical provider seams             193
exact provider-only service-cover floor       56
```

In the directed provider graph on the 12,870 transition indices, provider
arcs lying on a directed provider cycle jointly service only 45 defects.
Consequently the complementary bank `U` of 48 defects must be serviced on
provider path components after the selected nonprovider arcs are deleted.

## Exact path-mask census

Contract the strongly connected components of the provider graph.  For each
directed path in the resulting DAG, record the 48-bit mask of **distinct**
members of `U` hit by its physical provider seams.  Internal SCC arcs hit no
member of `U` by definition.

An exact topological dynamic program, retaining the nondominated distinct-hit
masks at every SCC, gives:

```text
SCCs in the provider graph                    12,804
ordered pairs in the condensation DAG          5,350
nondominated DP states                         24,538
unique achievable path masks                    2,192
globally maximal path masks                     1,094
maximum distinct U-hits on one path                 4

path-mask cardinality histogram
  0: 1,  1: 48,  2: 375,  3: 1,348,  4: 420
```

The SCC model is deliberately permissive: internal SCC connectivity is free,
different paths may overlap or be reused, and vertex-disjointness is ignored.
It is therefore an over-approximation of actual selected provider paths.

## Thirteen-path impossibility

Take the 1,094 inclusion-maximal achievable masks.  A deterministic memoized
set-cover search asks whether thirteen of them cover all 48 bits of `U`.
It explores 3,480,019 states and returns no cover.

Discarding a nonmaximal mask is sound because replacing it by an achievable
superset can only help this relaxed cover problem.  Allowing the remaining
masks to overlap, repeat, and come from mutually incompatible graph paths also
only helps.  Thus the failed thirteen-mask cover is a certificate for the
stronger statement that no thirteen actual provider paths can service `U`.

## Proof of the cut floor

Let a feasible selected port permutation contain `p` provider seams and `z`
nonprovider seams.

The exact provider edge-cover theorem gives `p >= 56`.

The selected seams form a vertex-disjoint union of directed cycles.  Delete
the `z` selected nonprovider arcs.  The remaining provider subgraph is a
union of provider-only cycles and at most `z` provider paths.  Provider-only
cycles service none of the 48 masks in `U`; hence the provider paths must
cover all of `U`.

The exact relaxed path-mask census proves that thirteen provider paths cannot
do so.  Therefore `z >= 14`, and

```text
p + z >= 56 + 14 = 70.
```

QED.

## Sound eager rows

The exact full q<=3 master may safely add

```text
sum(provider seam variables)    >= 56
sum(nonprovider seam variables) >= 14
cut_count                        >= 70
```

as redundant propagation rows.

## Audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

exact distinct-path audit
  scratch/k16_defect_service_structure_floor70_20260730.audit.json
  SHA-256 411fb4b3423ef12ae2865b141f85186d8f02346709822b01633a3cdd440f8290

checker
  scratch/audit_k16_defect_service_structure_20260730.py
  SHA-256 c4b32c1009296c17672634d410bcdbc0d66a073c78e14452b49d6571d92791e9

H100 resource ledger
  scratch/k16_defect_service_structure_floor70_20260730.resource.txt
  SHA-256 d812ce5449da51d8710cb5a170cbcc75a0f3a38e849d26addf9e67242d7a20c7
```

As an independent computational cross-check, the much stronger selected
provider-pseudoforest relaxation at exact total count 70 is infeasible in
1.46 seconds.  Its frozen output is
`scratch/k16_provider_path_cover_exact70_20260730.audit.json`; that solve is
not used in the proof above.
