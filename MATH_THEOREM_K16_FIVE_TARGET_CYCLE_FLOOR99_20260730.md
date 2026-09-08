# K16 five-target cycle theorem: the separated master needs at least 99 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, every selected port
permutation that services all 93 fixed q<=3 defects contains at least 99 seams
and cuts.

This is solver-independent.  It strengthens the earlier three-target floor 98
by solving the exact relaxed cycle-partition problem for five distinguished
defects.

## Reduced-cost accounting

The denominator-20 target-weight/port-potential certificate assigns every
seam `e:u->v` the nonnegative integer reduced cost

```text
rho(e) = 20 + phi(v) - phi(u) - weight(H(e)) >= 0,
```

where `H(e)` is the defect set gained by `e`.  The total weight of one copy of
all 93 defects is 1899.  If a selected port permutation contains `C` seams,
its directed cycles telescope the potential and give

```text
20 C = A + R,
```

where `A` is its gained weighted service, including duplicates, and
`R=sum rho(e)`.  Coverage implies `A>=1899`.

## Five-target cycle partition

Use the target bank

```text
T = {46811, 56173, 60854, 39791, 36343}.
```

An exhaustive replay of all 211,604 seams verifies that **no provider seam
hits two members of `T`**.  Choose one selected provider occurrence for every
member of `T`; the selected directed cycles partition these five distinct
occurrences.

For every nonempty subset `S` of `T`, the audit computes the minimum reduced
cost of a closed walk containing one provider for every target in `S`:

1. exact Dijkstra distances are computed in the complete nonnegative-cost
   seam graph between all relevant provider endpoints;
2. a Held--Karp dynamic program chooses and orders one physical provider seam
   per member of `S` and closes the walk;
3. an exact set-partition dynamic program partitions all five targets among
   cycles.

The minimum partition has cost

```text
min_partition_cost(T) = 62,
```

attained in the relaxed calculation by the partition

```text
{56173,39791} | {46811,60854,36343}.
```

The computation is deliberately permissive: connecting walks may reuse ports
or arcs, may incidentally service other defects, and cycles are not required
to be vertex-disjoint.  It therefore supplies a lower bound for every physical
selected port permutation.  Consequently `R>=62`.

## Cut floor

Combining weighted coverage and cycle cost,

```text
20 C = A + R >= 1899 + 62 = 1961,
```

so

```text
C >= ceil(1961/20) = 99.
```

QED.

## Sound eager row

The exact full q<=3 separated-port master may safely add

```text
cut_count >= 99
```

as a redundant propagation constraint.

## Scope

The theorem is source-relative to the frozen direction-coherent,
q<=3/upper-width-four separated seam catalogue.  It uses only endpoint
balance and the 93 service rows.  It does not use separation, reverse-edge,
q1, survivor, residence, or deeper-shadow constraints, and does not rule out a
different K16 carrier or a non-separated transformation.

## Reproduction

Run on the H100 CPU host `arboghast`:

```text
python3 scratch/explore_k16_multi_target_cycle_partition_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --certificate scratch/k16_provider_weight_potential_floor95_20260730.audit.json \
  --target 46811 --target 56173 --target 60854 \
  --target 39791 --target 36343 \
  --output NEW_OUTPUT.audit.json
```

## Frozen lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

weight/potential certificate
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

five-target checker
  scratch/explore_k16_multi_target_cycle_partition_20260730.py
  SHA-256 6688371d754e4d3941244ca141312d6a39ecaab0794057c8860384d5720e2f31

five-target audit
  scratch/k16_five_target_cycle_partition_floor99_20260730.audit.json
  SHA-256 6ece4edb1eb5504fd2e69677855326c15f5083d5b4e8c7ab7e86560b6095913e

H100 resource ledger
  scratch/k16_five_target_cycle_partition_floor99_20260730.resource.txt
  SHA-256 a7b57a9dc0567b20349049d535306aabaa433a286b74a7bbfe8fbbe0e2833113

stdout summary
  scratch/k16_five_target_cycle_partition_floor99_20260730.stdout.txt
  SHA-256 7fb5657105a696b2dcb913ea7ca09dbe91e3c11b72fb149a56036cb19512a034
```
