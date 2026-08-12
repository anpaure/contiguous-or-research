# K16 reduced-cost cycle theorem: the separated master needs at least 97 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, every selected port
permutation that services all 93 fixed q<=3 defects contains at least 97 seams
and cuts.

The proof starts from the exact denominator-20 weight/potential certificate,
uses the floor-96 equality obstruction already proved, and excludes every
possible 96-cut reduced-cost pattern by SCC and shortest-cycle arguments.

## The exact 96-cut budget equation

For every seam `e : u -> v`, let

```text
rho(e) = 20 + phi(v) - phi(u) - weight(H(e)) >= 0,
```

where `H(e)` is its gained defect set.  The total defect weight is 1899.
For a selected port permutation of `C` directed seams, potentials telescope:

```text
20 C = gained weighted service + total reduced cost.       (1)
```

Suppose `C=96`.  Write the gained service as `1899+Q`, where `Q` is the
weighted over-service beyond one copy of every target, and write `R` for the
total reduced cost.  Then

```text
Q + R = 21.                                                (2)
```

Every target weight is at least 11, so there can be at most one extra target
occurrence.  The only five cases are:

| case | repeated weight | reduced-cost budget R |
|---|---:|---:|
| no repeat | 0 | 21 |
| one repeat | 11 | 10 |
| one repeat | 16 | 5 |
| one repeat | 18 | 3 |
| one repeat | 19 | 2 |

Weights 22, 23, and 36 exceed the total over-service budget.  Two repeats,
even of weight 11, also exceed it.

## The four repeat cases fail cyclic service

In a case with total reduced-cost budget `R`, every selected seam has
`rho(e)<=R`.  Form the directed graph of all physical seams satisfying this
individual bound, providers and nonproviders.  Every selected seam belongs to
a directed selected cycle, hence must lie in a cyclic SCC of this admissible
graph.

Exact SCC replay gives:

| repeated weight | R | cycle-eligible providers | defects with degree zero |
|---:|---:|---:|---:|
| 11 | 10 | 522 | 3 |
| 16 | 5 | 237 | 3 |
| 18 | 3 | 150 | 3 |
| 19 | 2 | 120 | 33 |

For repeat weights 11, 16, and 18, the same three residual-block targets

```text
46811, 56173, 60854
```

have no cycle-eligible provider.  The weight-19 case misses 33 targets.  Thus
all four repeat cases are impossible before imposing port capacity, exact
budget sharing, separation, or any nondefect condition.

## The no-repeat case has only 21 units for three expensive cycles

It remains to exclude `Q=0, R=21`.  Every target is then served exactly once.
Focus on the same three residual-block targets

```text
T = {46811, 56173, 60854}.
```

The physical seam census confirms that no provider seam hits two members of
`T`; each occurrence therefore has its own distinguished provider seam.

Give every physical seam its exact nonnegative reduced cost `rho(e)`.  For a
provider seam `a : u -> v`, the minimum reduced cost of a directed closed walk
containing `a` is

```text
rho(a) + shortest_reduced_cost_path(v,u).
```

Exact Dijkstra replay on the full 211,604-seam directed graph gives minimum
cycle cost 17 for each member of `T`.  Enumerating the possible cyclic order
of two or three distinguished provider seams gives:

```text
one specified target on a cycle          17
any specified pair on one cycle          39
all three targets on one cycle            55
```

These are permissive closed-walk lower bounds: shortest return segments may
repeat vertices or arcs and ignore degree-disjointness, so they cannot
overstate the cost of an actual selected simple cycle.

The selected cycles partition the three target occurrences.  The five set
partitions have lower bounds:

```text
three singleton cycles                 17+17+17 = 51
one pair plus one singleton                39+17 = 56
one triple                                      55
```

Thus every union of selected cycles that serves all three costs at least 51.
But the entire no-repeat 96-cut face has total reduced-cost budget only 21.
Contradiction.

All five cases in (2) are impossible.  Therefore no 96-cut selected port
permutation services the defect bank, and

```text
C >= 97.
```

QED.

## Sound eager row

The exact full q<=3 separated-port master may safely add

```text
cut_count >= 97
```

as a redundant propagation constraint.

## Scope

This theorem is source-relative: it closes counts at most 96 inside the frozen
direction-coherent, q<=3/upper-width-four separated seam catalogue.  It does
not rule out a different K16 carrier or a non-separated transformation.

## Audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

potential certificate
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

five-case SCC/service audit
  scratch/k16_exact96_cost_layers_20260730.audit.json
  SHA-256 dbd3a51aed4dd60a6dff9f4f43ab78b2fb552e06dcad8caa041b80278b40b24a

five-case checker
  scratch/audit_k16_exact96_cost_layers_20260730.py
  SHA-256 9df65e4963e80cc268e6e555b2ff750ecfd81f08a80653a2d3c0da5d9da53c38

three-target cycle-partition audit
  scratch/k16_exact96_special_cycle_cost_20260730.audit.json
  SHA-256 3cf4a5156439c79a950427ca98349b3ec0ef452489bc69637e44a294299c9a9e

cycle-partition checker
  scratch/audit_k16_exact96_special_cycle_cost_20260730.py
  SHA-256 6aabffb6006a00688ae766c4d93eec0a5f4ddf8f6fbdc778e571de364641e1c5

cycle-partition H100 resource ledger
  scratch/k16_exact96_special_cycle_cost_20260730.resource.txt
  SHA-256 c9baf10ab33f57116a1b9d1bf701add0206260401b05f2f8c283fbb1a11001ae

independent per-target Dijkstra audit
  scratch/k16_floor97_target_cycle_cost_independent_20260730.audit.json
  SHA-256 9dca9e7085a583e85de918361a0ebca17ed7a0c63b10c60f0c125c197126744e

independent per-target checker
  scratch/audit_k16_floor97_target_cycle_cost_20260730.py
  SHA-256 dd139cee912d24aa8ac9093cfd3e8ecf381b5755ae729403a7d1ce46b8315a07
```

The independent per-target audit confirms all three singleton minima equal
17.  The partition audit additionally enumerates every two- and three-target
cyclic order needed for the 39 and 55 bounds.
