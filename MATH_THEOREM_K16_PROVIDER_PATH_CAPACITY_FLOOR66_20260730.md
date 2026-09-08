# K16 provider-path capacity theorem: the separated master needs at least 66 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and the audited catalogue of 211,604
direction-coherent, positive-residence-safe seams, every port permutation that
services all 93 fixed q<=3 defects selects at least

```text
56 provider seams + 10 nonprovider seams = 66 seams and cuts.
```

This lower bound uses neither cut separation nor any nondefect q1/q2/q3
preservation row.  It therefore applies to the full separated-port master.

## Frozen provider data

A **provider** is a seam that gains at least one of the 45 lower-q2 or 48
upper-q3 zero-baseline masks.  The exact binary census is:

```text
defects                                      93
provider seams                            5,425
one-hit provider seams                    5,232
two-hit physical provider seams             193
distinct double-defect pairs                119
double-graph isolated defects                 18
maximum double-graph matching                 37
exact provider-only service-cover floor       56
```

The floor 56 has two independent certificates: an explicit 37-edge matching
plus 19 singleton services, and a direct physical-seam cover of size 56.

## Provider port graph and its condensation

Make a directed graph `G` on the 12,870 source transitions.  A provider seam
with left cut `i` and right cut `j` is the arc `i -> j`.

The exact SCC census is:

```text
vertices of G                              12,870
arcs of G                                   5,425
strong components                          12,804
nontrivial strong components                    9
largest strong component                       45
provider arcs internal to a cyclic SCC          75
defects hit by those internal arcs               45
remaining defects                               48

condensation-DAG arcs                         5,350
maximum unweighted condensation path              9 arcs
maximum additive remaining-defect weight/path     5
```

For each inter-SCC condensation arc, its weight is the maximum number in
`{0,1,2}` of the 48 remaining defects hit by one physical provider seam on
that ordered SCC pair.  A standard topological dynamic program gives maximum
additive path weight five.  The recorded maximizing path has weights

```text
1, 0, 1, 1, 1, 1, 0
```

and in fact repeats one target, so its five-unit additive weight is a safe
overestimate of distinct coverage.

## Proof

Let a feasible selected port permutation contain `p` providers and `z`
nonproviders.

First, provider service alone requires `p >= 56` by the exact edge-cover
certificate.

The selected seams form a vertex-disjoint union of directed cycles on source
transition indices: every selected cut has one selected seam entering and one
leaving.  Delete the `z` selected nonprovider arcs.  What remains is a union
of provider-only directed cycles and at most `z` provider paths.  Empty path
segments only reduce this number.

Every provider arc internal to a nontrivial SCC lies on a directed provider
cycle.  Conversely, every provider-only cycle is internal to one SCC.  The
internal arcs jointly hit only 45 defects, so the other 48 defects cannot be
supplied by any provider-only cycle.  Nonprovider arcs hit no defect by
definition.  Thus all 48 remaining defects must be supplied along the at most
`z` provider paths.

Contract the SCCs visited by one provider path.  Its inter-SCC arcs form a
directed path in the condensation DAG; an SCC cannot be revisited because the
condensation is acyclic.  Internal SCC arcs hit none of the 48 remaining
defects.  Each inter-SCC physical seam contributes at most the audited weight
of its condensation arc.  Therefore the number of distinct remaining defects
hit along one provider path is at most its additive condensation weight, at
most five.  Counting a repeated target more than once only weakens this upper
bound.

Consequently

```text
48 <= 5 z,
```

so `z >= 10`.  Together with `p >= 56`, the selected cut count is at least
`p+z >= 66`.  QED.

## Sound eager rows

The exact full q<=3 master may safely add

```text
sum(provider seam variables)    >= 56
sum(nonprovider seam variables) >= 10
cut_count                        >= 66
```

as redundant propagation cuts.  These do not impose rotational invariance,
connectivity, a fixed number of components, or any new geometric assumption.

## Subtlety checks

1. **Paths through SCCs.** A provider path may use many internal SCC arcs,
   but those arcs hit none of the selected 48-defect complement by its very
   definition.  Only inter-SCC arcs matter.
2. **Parallel condensation arcs.** The weight of an ordered SCC pair is the
   maximum over all physical provider seams on that pair, so replacing the
   selected physical arc by this weight is an upper bound.
3. **Repeated targets.** The DP adds arc weights without deduplicating target
   masks.  This can only overestimate distinct service, making the derived
   connector floor conservative.
4. **Several nonproviders on one selected cycle.** Deleting `r` such arcs
   creates at most `r` provider path segments.  Summing over cycles gives at
   most `z` paths total.
5. **Provider-only selected cycles.** They remain as cycles after deletion,
   but service none of the 48 complement defects and hence do not affect the
   path-capacity inequality.

## Audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

independent floor-66 census
  scratch/k16_defect_service_structure_floor66_20260730.audit.json
  SHA-256 31314bc077f81fc311b58d3aba483a0a06a77d2d05a4d4d424db606db3e0c4c8

checker
  scratch/audit_k16_defect_service_structure_20260730.py
  SHA-256 009b7b90e96e1f1681a034e40bc91c5d1f3f01116e0011541799efad7288fae8

independent exact provider-cover audit
  scratch/k16_defect_service_cover_20260730.audit.json
  SHA-256 ad14505e6080e188240559c7949e51536a89579dda1ddb20e303b9115de603c7
```

