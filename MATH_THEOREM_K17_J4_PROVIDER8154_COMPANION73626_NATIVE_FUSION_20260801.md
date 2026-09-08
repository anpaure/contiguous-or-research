# K17 J4 native fusion for provider 8154 and companion 73626

Date: 2026-08-01

## Result

The first propagation obstruction in the joint rich-socket/provider model has
an exact native three-owner repair.  Replace the provider occurrence of upper
colour `8154` and its otherwise unsupported cut child `73626` by the Johnson
path

```text
8152  ->  8090  ->  69530
```

at source positions

```text
(component 155, position 0),
(component 282, position 1),
(component 282, position 2).
```

Its immediate palettes are

```text
upper: 8154, 73626
lower: 8088, 3994.
```

All three owners have rank 9, are distinct, and successive owners differ in
exactly two coordinates.  The clipped three-owner chronology is resident: it
contains no internal positive coordinate run of length below four.

The installation forces cuts

```text
(155,1), (282,1), (282,3)
```

and keeps `(282,2)` intact.  The three exposed boundary colours are

```text
16344, 16282, 102298.
```

They have respectively `20`, `42`, and `24` rows in the authenticated
extendable-provider atlas.  Thus the macro has no individually unsupported
boundary child.

## Why this is the correct repair

The first unified r4 CNF was immediately UNSAT.  Its DRAT-verified four-clause
core consists of the two witnesses for provider target `8154`, both implying
cut `(282,2)`, together with the unit prohibition of that cut because its
child colour `73626` was not priced.  Making `73626` a separate rich socket
does not compose: all 262 self-feasible `73626` rows conflict with the
provider-8154 footprint and force a provider-forbidden cut.

The path above internalizes both colours instead.  Therefore the corrected
joint model must:

1. remove `8154` from the external-provider exact-one bank;
2. not add a separate `73626` socket group;
3. force the three displayed boundary cuts and forbid the internal cut;
4. retain the ordinary provider clauses for the three boundary colours.

This is an exact local replacement of the propagation core; it is not a
relaxation of the missing colour.

## Audit

The independent C++ replay reads the frozen SCD component table and the
extendable-provider atlas and checks:

- the three exact source owners and positions;
- rank, distinctness, and Johnson adjacency;
- both immediate palettes;
- clipped residence;
- the forced/forbidden cut pattern;
- literal support of every exposed boundary colour.

Artifacts:

```text
scratch/audit_k17_j4_provider8154_companion73626_20260801.cpp
scratch/k17_j4_provider8154_companion73626_20260801.audit.json
```

The audit status is

```text
PASS_SCOPED_J4_NATIVE_FUSION
```

The frozen input hashes are

```text
components.tsv
  dc4557fb557dccb87bec15476e11b81655d17c6c6c5295b020fec95adbcb47ef
extendable_arcs.tsv
  9ef66394ffc8c40a04292e836c02fa4838c395c3b338b41908ae994e3555f2c2
```

## Scope

This proves only the local owner/immediate-palette installation and the
individual availability of its boundary providers.  It does **not** prove:

- simultaneous selection with the remaining rich sockets and providers;
- compatibility after dynamic fragment coalescence and orientation;
- a global path or Hamilton chronology;
- coverage at ranks 11 and above;
- the common-Q/lower compiler;
- or a length-24313 universal word for `k=17`.

The same r4 audit exposed eight further provider groups with analogous
unpriced-child propagation cores.  They remain open until independently
fused, reoptimized, or jointly priced.
