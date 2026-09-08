# K16 reduced-cost equality obstruction: the separated master needs at least 96 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, every selected port
permutation that services all 93 fixed q<=3 defects contains at least 96 seams
and cuts.

This strengthens the weight-potential floor 95 by ruling out its equality
case.  The proof is solver-independent and uses no separation, reverse-edge,
q1, survivor, residence, or deeper-shadow condition.

## The floor-95 potential certificate

Give the seven defect phase blocks the integer weights

```text
11, 22, 36, 19, 18, 16, 23
```

with block sizes `15,15,15,15,15,15,3` and common denominator 20.  Their
total numerator is 1899.  The frozen potential

```text
phi : 12,870 transition indices -> {0,...,20}
```

satisfies, for every seam `e : u -> v`, the nonnegative integer reduced-cost
inequality

```text
rho(e) := 20 + phi(v) - phi(u) - weight(H(e)) >= 0,       (1)
```

where `H(e)` is the set of zero-baseline defects gained by `e`; it is empty
for a nonprovider seam.  The independent C++ verifier replays (1) against all
211,604 physical seams, not just the 5,425 providers.

For a selected port permutation with `C` seams, sum (1) around its directed
cycles.  The potential terms cancel exactly:

```text
20 C = sum_e weight(H(e)) + sum_e rho(e).                 (2)
```

Coverage of all defects gives `sum_e weight(H(e)) >= 1899`, yielding the
previous bound `C >= ceil(1899/20)=95`.

## Equality slack is exactly one

Assume for contradiction that `C=95`.  Equation (2) becomes

```text
1900 = gained weighted service + total reduced cost.
```

Every target weight is at least 11.  Therefore no target can be served twice:
one duplicate would make the gained weighted service at least
`1899+11>1900`.  Since all targets must be served, every target is served
exactly once, gained weighted service is exactly 1899, and

```text
sum_e rho(e) = 1.                                         (3)
```

All reduced costs are nonnegative integers.  Hence every selected seam has
`rho(e)<=1`.

## The admissible-cycle obstruction

Let `G_1` be the directed graph on transition indices containing every
physical seam with `rho(e)<=1`, providers and nonproviders alike.  Exact
binary replay gives:

```text
admissible seams in G_1                 3,558
  admissible providers                  2,148
  admissible nonproviders               1,410

strong components                      12,810
nontrivial SCCs                             15, each of size 5

arcs lying on a directed cycle             90
  cycle-eligible providers                 60
  cycle-eligible nonproviders               30
```

A selected port permutation is a union of directed cycles.  Under (3), every
selected seam lies in `G_1`, so every selected seam must lie on a directed
cycle of `G_1`; equivalently, its endpoints lie in the same cyclic SCC.

The 60 cycle-eligible providers jointly expose only 30 of the 93 defects.
Sixty-three defects have no cycle-eligible provider at all.  In particular,
target `33337` is a one-row Hall witness: it must be served, but no provider
that serves it can occur in any directed cycle of `G_1`.

Thus a 95-seam selected port permutation cannot service the defect bank.
Together with the floor 95,

```text
C >= 96.
```

QED.

## Sound eager row

The exact full q<=3 separated-port master may safely add

```text
cut_count >= 96
```

as a redundant propagation constraint.

## Scope

This is a theorem about the frozen source-relative, direction-coherent,
q<=3/upper-width-four separated seam catalogue.  It is not a theorem that no
other K16 carrier or non-separated transformation can work.  All omitted
full-master constraints only strengthen the bound within this catalogue.

## Independent audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

floor-95 potential certificate consumed by the verifier
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

independent C++ verifier
  scratch/audit_ad_k16_provider_weight_potential_floor95_independent_20260730.cpp
  SHA-256 26a2af36e42df7078ef5e9297c9b8ebc10738542b8e54ea843397bac2533d144

independent floor-96 audit
  scratch/k16_provider_weight_potential_floor96_independent_final_20260730.audit.json
  SHA-256 a57e445f266ff88287429712d7701ab70a2957d61de6008ef21a7048c0192a3d

H100 resource ledger
  scratch/k16_provider_weight_potential_floor96_independent_final_20260730.resource.txt
  SHA-256 08d78a9890f04b49cbe9429813ae23b5934c7a3169ae6cad4ab5f34c2203651a

stdout summary
  scratch/k16_provider_weight_potential_floor96_independent_final_20260730.stdout.txt
  SHA-256 cd3f69f192c3567328e883ca1f8f0600f45221080d14a1e435e5c9f85a52e100
```

The independent verifier parses the binary ledger directly, reconstructs the
93 weighted targets, checks every reduced cost, rebuilds the admissible graph,
recomputes its SCCs, and emits the singleton witness `33337`.
