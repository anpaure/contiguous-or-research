# K16 provider-port cycle theorem: the separated master needs at least 57 cuts

Date: 2026-07-30

## Frozen setting

Use the audited length-eight K16 source and its 211,604 positive-safe directed
seams.  There are 93 zero-baseline fixed targets: 45 lower-q2 masks and 48
upper-q3 masks.  Call a seam a **provider** if it gains at least one of these
93 targets.

The independent binary census gives:

```text
provider seams                 5,425
one-hit seams                  5,232
two-hit physical seams           193
distinct two-hit target pairs     119
isolated vertices in pair graph    18
maximum matching in pair graph      37
exact provider cover floor          56
```

The exact floor 56 is proved and independently certified in
`MATH_THEOREM_K16_DEFECT_PROVIDER_EDGE_COVER_FLOOR56_20260730.md` and
`scratch/k16_defect_service_cover_20260730.audit.json`.

## Port digraph

Make a directed graph on the 12,870 source transitions.  A provider seam whose
left cut is `i` and whose right cut is `j` is the arc `i -> j`.

The exact strongly-connected-component census of this graph is:

```text
vertices                              12,870
provider arcs                          5,425
strong components                     12,804
nontrivial strong components               9
largest strong component                  45
provider arcs lying on a directed cycle   75
defects serviced by cycle arcs            45
defects not serviced by any cycle arc      48
```

The 48 masks are recorded explicitly in
`scratch/k16_defect_service_structure_v4_20260730.audit.json`.

## Theorem

Every feasible direction-coherent port permutation of this source that
services all 93 defects selects at least one nonprovider seam.  Consequently
it has at least 57 cuts.

### Proof

In a port permutation, every selected cut index has exactly one selected seam
leaving it and exactly one selected seam entering it.  Therefore the selected
seams are a vertex-disjoint union of directed cycles in the port digraph.

Suppose every selected seam were a provider.  Then every selected seam would
lie on a directed cycle of the provider-only digraph.  The frozen SCC census
shows that provider cycle arcs jointly service only 45 of the 93 defects; 48
defects cannot be gained by any such arc.  Hence a provider-only port
permutation cannot service the defect bank.  At least one selected seam is a
nonprovider.

Separately, every service cover contains at least 56 providers.  Thus every
feasible port permutation contains at least `56 + 1 = 57` seams and cuts.
QED.

## Sound eager cuts

The full q<=3 master may add both redundant rows

```text
sum(provider seam variables)    >= 56
sum(nonprovider seam variables) >= 1
```

and may set the cut-count lower bound to 57.  These rows do not assume cut
separation, q1 preservation, residence, or any deeper shadow condition; all
of those constraints can only strengthen the bound.

## Audit lineage

```text
binary seam ledger
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

SCC/service audit
  scratch/k16_defect_service_structure_v4_20260730.audit.json
  SHA-256 91d70c1efdf4bd062b20838a467159602bf1ef3e244cf208f38ab5caa81fd2b3

checker
  scratch/audit_k16_defect_service_structure_20260730.py
  SHA-256 d80d90f89e4ed4c3be5e4c45794b765fdc3fe43cd9521f31f0479c83a1b975f5
```

The independent CP-SAT port-only relaxation also reports exact-count 56
INFEASIBLE in presolve, with zero branches and zero conflicts.  The theorem
above is solver-free and explains that result.

