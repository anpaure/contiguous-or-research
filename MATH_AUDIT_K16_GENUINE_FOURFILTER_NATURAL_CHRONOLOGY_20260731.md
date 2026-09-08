# Genuine four-filter K15 lineage and its natural K16 chronology

Date: 2026-07-31  
Status: exact fixed-order P/Q scalar no-go with independent Hall diagnostic  
Scope: the authenticated natural chronology only; no global K16 claim

## 1. Lineage authentication

The source is the genuine four-filter K15 physical word

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4
```

with authenticated metadata

```text
opening = (5134,0,5,1,0), direction = fwd
meta SHA-256 d1006c375c2cb69f595e7d56ffd0e585d4741ae3d4562bfd9e3d1141f223fea7.
```

No historically named `k16_fourfilter_insert_aug*` file is used: those
orders were independently proved seed0-derived.

For the 6,438-cell parent \(W\), define

\[
D_2(i)=W_i\vee W_{i+1}\vee W_{i+2},\qquad
D_3(i)=W_i\vee W_{i+1}\vee W_{i+2}\vee W_{i+3}.
\]

The \(D_3\) list consists of all 6,435 rank-eight masks on the old 15
coordinates exactly once.  The \(D_2\) list has 6,436 distinct values:
all 6,435 rank-seven masks once, plus the unique rank-six value `0x13c8`
at zero-based index 6,390.  With `top=0x8000`, the natural K16 order is

```text
reverse(top | D2[:6390])
  + D3
  + reverse(top | D2[6391:]).
```

Its piece lengths are `6390+6435+45=12870`.  Canonical decimal serialization
with one trailing newline gives

```text
scratch/k16_genuine_fourfilter_natural_targets_20260731.word
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.
```

The order contains every rank-eight K16 mask exactly once and every adjacent
edge is a Johnson edge.  This byte identity independently fixes the natural
chronology; the metadata opening is not a license to substitute a different
four-piece concatenation.

## 2. Exact upper audit

All 12,869 adjacent unions have rank nine.  They cover 11,438 of the 11,440
rank-nine masks, leaving

```text
q1 holes = {0xb3cc, 0xd3cc}.
```

Exhaustive arbitrary-width interval-OR replay leaves exactly six upper holes:

```text
rank  9: 0xb3cc, 0xd3cc
rank 10: 0xd3ce, 0xf3cc
rank 11: 0xdbce
rank 12: 0xfbce.
```

All upper masks of ranks 13 through 16 are present.

## 3. Complete P/Q area theorem

The exact event DAG ranges over every monotone depth-three schedule with
three omitted starts and three omitted deadlines.  Its state records the two
hole counts and the accumulated OR queue of active middle rows; histories
with the same state are dominated exactly by larger selected area because
all future transitions depend only on that state.

The unique reported maximum is

```text
X = {12826,12827,12872},
Y = {0,6390,6391},
selected proper-prefix area = 25744.
```

All maximal envelopes are nonzero and all 12,870 middle rows replay exactly.
Even the uniform omitted-start grant gives

\[
25744+9=25753<26332
  =\sum_{r=1}^{7}{16\choose r}.
\]

The final omitted start is boundary-truncated, so the literal credit is only
`3+3+1=7` and the exact physical lower-cell count is 25,751.  Therefore no
three-hole depth-three P/Q realization of this fixed natural target order can
cover all lower masks.  This conclusion is scalar and does not require SAT,
Hall, or a choice of lower providers.

## 4. Exact Hall diagnostic at the maximizer

For completeness, the generalized individual-pin graph of the maximizing
schedule contains

```text
26,332 lower targets,
25,751 exact physical lower cells,
343,156 incidences,
maximum matching 22,822,
deficiency 3,510,
canonical Hall shore 9,949 targets / 6,439 cells.
```

Its 12 zero-host targets are

```text
8000 8001 8002 8004 8010 8020 8040 8200 8400 8800 a000 c000.
```

The deficiency has a closed-form Hall witness.  Let `z=0x8000` and let `L`
be all nonempty lower targets containing `z`.  Then
`|L| = sum_(j=0)^6 binom(15,j) = 9,949`.

Exact profile replay shows that its neighborhood consists of 6,435 singleton
cells—positions `0..6389` and `12828..12872`—and exactly four nonsingleton
cells `(6389,2)`, `(6389,3)`, `(12826,3)`, `(12827,2)`.  Hence
`|N(L)|=6,439` and `|L|-|N(L)|=3,510`.

The exhibited matching has size `26,332-3,510=22,822`, so this shore
certifies both the upper and lower bounds on the exact matching number.

This Hall row is schedule-specific and only diagnostic; the all-schedule
scalar theorem in Section 3 is the decisive fixed-order obstruction.

## 5. Scope and next boundary

The result closes only the canonical natural chronology of SHA `0f6d64e...`
inside the depth-three, three-hole P/Q architecture.  Rethreads constructed
from the genuine parent remain open and must be authenticated against the
`51f57125...` source.  No seed0 fixed-order obstruction transfers by name,
and no claim is made for a non-P/Q construction or for K16 globally.

## 6. Frozen evidence

```text
scratch/audit_k16_true_fourfilter_lineage_independent_20260731.py
  SHA bb53fe09788c4e5521f8b67b13fc3b62bcc5ea43575d95d5e86ec272775216d1
scratch/k16_true_fourfilter_lineage_independent_20260731.audit.json
  SHA f56c64f2f9721918d44faf005c946337df5a71b3947f333cf1f64444a4c46d38
  payload 8bd6b12d3d3d6584ea2722f7adb4f2aafc1a24effe98c1ae2c8f7581119fd19e
scratch/audit_r_k16_true_fourfilter_natural_20260731.py
  SHA 7e5c6d268c2a75e8a350eaf8c8a29dafb40ef7df4f093ec510ba4b046f46df5c
scratch/k16_true_fourfilter_natural_20260731.audit.json
  SHA 20c10fef2e22b6d8069b00ac4bb4849e6dbbd2d4f270754508255fa91cf63f3a
  payload f5b9ad6bed8e15e390fdaba6775c62e4f59a5ec55cd10e8bdf60c2261d7f53b0
scratch/k16_genuine_fourfilter_natural_generalized_hall_20260731.audit.json
  SHA ad8330303bf6f5f771efdd920c6e562311bcd4f2ad46c84eb056e4e87a13232f
  payload 384e72d18f7ed54d78db81af0a50b11adc0b739bf952d14b14b1c086ca51ddbc
```

All three JSON certificates above have parse-replay-stable payload hashes.
The independent lineage replay reconstructs the chronology from the K15
parent, recomputes every upper interval, and resolves the complete P/Q event
DAG in 0.37 seconds with 37.6 MB maximum RSS on the local audit run.
