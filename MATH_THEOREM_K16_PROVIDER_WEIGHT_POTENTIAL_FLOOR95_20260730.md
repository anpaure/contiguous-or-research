# K16 provider weight-potential theorem: the separated master needs at least 95 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete audited catalogue of
211,604 direction-coherent, positive-residence-safe seams, every selected port
permutation that services all 93 fixed q<=3 defects contains at least 95 seams
and cuts.

The proof is an exact integer target-weight and port-potential certificate.  It
does not invoke the full SAT master and omits cut separation, reverse-edge
exclusions, all nondefect preservation rows, q1 rows, and survivor conditions.
These omissions only relax the problem.

## Target weights

The 93 defects split into the seven audited phase blocks of sizes

```text
15, 15, 15, 15, 15, 15, 3.
```

Assign the following integer weights, with common denominator 20:

| phase block | size | numerator per defect |
|---|---:|---:|
| lower-q2 block 0 | 15 | 11 |
| lower-q2 block 1 | 15 | 22 |
| lower-q2 block 2 | 15 | 36 |
| upper-q3 block 0 | 15 | 19 |
| upper-q3 block 1 | 15 | 18 |
| upper-q3 block 2 | 15 | 16 |
| upper-q3 residual block | 3 | 23 |

The total numerator is

```text
15(11+22+36+19+18+16) + 3(23) = 1899.
```

Every defect must be gained by at least one selected provider seam, so the sum
of gained target weights over selected providers is at least 1899.

## Port potential

Make the directed provider graph on the 12,870 source transition indices.  A
provider seam `e : u -> v` gains a set `H(e)` of one or two defects.  The
frozen audit records an integer potential

```text
phi : transition indices -> {0,1,...,20}
```

such that, for every one of the 5,425 provider seams,

```text
sum(weight(t), t in H(e)) <= 20 + phi(v) - phi(u).       (1)
```

This is checked exactly with integer arithmetic against the full binary seam
catalogue.  The maximum violation is zero.  The potential is the minimal
solution of the difference constraints

```text
phi(v) >= phi(u) + sum(weight(t), t in H(e)) - 20;
```

starting from zero at every vertex.  Relaxation converges after five complete
passes and has range exactly `[0,20]`, so the certificate is independently
reconstructible rather than solver-state-dependent.

## Telescoping proof

Let a feasible selected port permutation contain `p` providers and `z`
nonproviders.  Delete the `z` nonprovider arcs.  The remaining provider
subgraph is a union of directed provider cycles and at most `z` directed
provider paths.

Sum (1) along one provider cycle with `l` arcs.  The potential terms telescope
to zero, so its gained-weight sum is at most `20l`.

Sum (1) along one provider path with `l` arcs.  The potential terms telescope
to `phi(end)-phi(start)`, at most 20 because `phi` lies in `[0,20]`.  Thus its
gained-weight sum is at most `20(l+1)`.

Summing over all provider components gives

```text
1899
  <= gained target-weight numerator
  <= 20 (number of provider arcs + number of provider paths)
  <= 20 (p + z).
```

Therefore

```text
p + z >= ceil(1899/20) = 95.
```

QED.

## Why this subsumes the earlier floors

The previous independent bounds separated provider service from nonprovider
connectors, culminating in `56 + 17 = 73`.  The potential certificate couples
them: a high-weight service seam may be cheap as a provider but expensive to
thread into a path, and the potential accounts exactly for this tradeoff.
Consequently the scalar floor 95 supersedes floors 56, 57, 66, 70, and 73.
The split rows remain useful for propagation but are no longer the strongest
aggregate count bound.

## Sound eager row

The exact full q<=3 master may safely add

```text
cut_count >= 95
```

as a redundant propagation constraint, together with any independently sound
provider/nonprovider split rows.

## Audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

exact weight/potential audit
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

checker
  scratch/audit_k16_provider_weight_potential_floor95_20260730.py
  SHA-256 294893b2c3bf678c4f1c67b7615e1230a0510720347df273e4a21c4d4f95fed6

H100 resource ledger
  scratch/k16_provider_weight_potential_floor95_20260730.resource.txt
  SHA-256 3cc55f33415009028fbcf7da035cce4552122971e6c8910746aa014c57d289da

stdout summary
  scratch/k16_provider_weight_potential_floor95_20260730.stdout.txt
  SHA-256 5e450e3116f9d3cf27d29e09da1f7b64b35f00f2d6d02e3def83ca00f2c3763b
```

The audit stores all 12,870 potential values, all 93 target weights, the exact
slack histogram over the 5,425 provider arcs, and hashes of the 1,388 tight
provider seams.
