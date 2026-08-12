# K16 provider-path dual theorem: the separated master needs at least 73 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete audited catalogue of
211,604 direction-coherent, positive-residence-safe seams, every selected port
permutation that services all 93 fixed q<=3 defects contains at least

```text
56 provider seams + 17 nonprovider seams = 73 seams and cuts.
```

The proof is independent of the full SAT master.  It omits cut separation,
reverse-edge exclusions, all nondefect preservation rows, q1 rows, and
survivor constraints.  Each omission relaxes the problem, so the bound applies
to the full separated-port master.

Here “complete audited catalogue” means the fixed q<=3/upper-width-four
211,604-seam ledger.  It does not mean the older combined `WIDTH45` graph:
that graph has 150 additional width-five-only singleton providers, which can
change provider SCCs and path masks.  No transfer to `WIDTH45`, close
interacting windows, or unrestricted rethreads is asserted.

## Provider baseline

A **provider** is a seam that gains at least one of the 45 lower-q2 or 48
upper-q3 zero-baseline defects.  The frozen physical-seam edge-cover audit
proves that any service cover uses at least 56 provider seams.  Provider and
nonprovider seams are disjoint categories, so any independent lower bound on
the number of nonproviders adds to 56.

## Provider paths after deleting nonproviders

Selected seams form a vertex-disjoint union of directed cycles on source
transition indices.  If `z` selected seams are nonproviders, deleting them
leaves provider-only cycles and at most `z` directed provider paths.

The provider graph has 12,804 strongly connected components.  Provider seams
internal to a cyclic SCC jointly service only 45 of the 93 defects.  Let `U`
be the complementary bank of 48 defects.  Provider-only cycles cannot service
`U`, and nonproviders service no defect by definition.  Therefore the at most
`z` provider paths must cover all of `U`.

## The half-weight certificate

Contract the provider SCCs and enumerate, by exact topological dynamic
programming, every attainable distinct-`U` mask of a provider path in the SCC
DAG.  SCC interiors are treated as freely connectable and different paths may
overlap or be reused, so this is an over-approximation of actual selected
paths.  The complete relaxed universe contains 2,506 exact path masks.

There is a fixed subset `S` of 33 members of `U`:

```text
33609 34069 34450 35370 35461 36132 36969 37389 37972 38154 39496
41170 41285 41633 42010 42115 43089 43176 43540 46224 46811 49572
49802 50498 51252 51462 53410 53584 53825 54312 56173 59680 60854
```

Exact replay over all 2,506 masks gives

```text
|path mask intersect S| <= 2
```

for every attainable relaxed provider path.  Equivalently, assign weight
`1/2` to each target in `S` and zero to the other 15 members of `U`.  The
total target weight is `33/2 = 16.5`, while every provider path has weight at
most one.  Thus any family of provider paths covering `U` has at least

```text
ceil(16.5) = 17
```

members.  Hence `z >= 17`.

Combining with the independent provider floor gives

```text
total cuts = providers + nonproviders >= 56 + 17 = 73.
```

QED.

## Sharpness inside the relaxed path-mask universe

An exact integer set-cover solve over all 2,506 masks finds a 17-mask cover of
all 48 targets.  The half-weight certificate proves no cover of size 16.
Therefore 17 is the exact path-cover number of this relaxation; improving the
cut floor further requires coupling path service to provider-seam cost,
vertex-disjointness, physical connector existence, or another omitted global
constraint.

The 17 witness masks are stored in the frozen audit.  This witness establishes
sharpness only in the permissive path-mask universe, not feasibility of a
73-cut port permutation.

## Sound eager rows

The exact full q<=3 master may safely add

```text
sum(provider seam variables)    >= 56
sum(nonprovider seam variables) >= 17
cut_count                        >= 73
```

as redundant propagation constraints.

## Audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

exact rational-dual and integer-cover audit
  scratch/k16_provider_path_dual_floor73_20260730.audit.json
  SHA-256 38aa93ee5a737c9aeed30b9d23ba89c282774e5440a0d6d06dd2fa26a581ac4d

checker
  scratch/audit_k16_provider_path_dual_floor73_20260730.py
  SHA-256 eb2c6e9e2851a70eb9ab032fb7809e0d9ef1fdbdfd8a400d8505294a7ac8fee9

H100 resource ledger
  scratch/k16_provider_path_dual_floor73_20260730.resource.txt
  SHA-256 ff577624d6ca91f14ec2dbbcfeefb027e744e454e409361e6e535251fae7b0dc

stdout summary
  scratch/k16_provider_path_dual_floor73_20260730.stdout.txt
  SHA-256 500b99b25d8a5e1016e56fe0497387383c0242ec3ca5b90ce7ae704bba56d045
```

The audit records the exact rational form with denominator ten: 33 target
weights equal five, total weight 165, and every path inequality has right-hand
side at most ten.  Its strict margin over sixteen paths is five.
