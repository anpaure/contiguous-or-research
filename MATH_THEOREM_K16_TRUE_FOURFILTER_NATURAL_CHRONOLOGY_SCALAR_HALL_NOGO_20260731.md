# Genuine four-filter K16 natural chronology: exact scalar and Hall no-go

Date: 2026-07-31  
Status: authenticated fixed-natural-order theorem  
Scope: genuine four-filter parent; no unrestricted K16 claim

## 1. Parent authentication and lineage guard

The genuine four-filter K15 parent is

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4
length 6,438
```

The local bytes agree with H100 `/dev/shm/K15_FOURFILTER_SEED.word`.  Its
metadata has SHA
`d1006c375c2cb69f595e7d56ffd0e585d4741ae3d4562bfd9e3d1141f223fea7`
and records

```text
opening = (5134,0,5,1,0), direction = fwd,
scores = {deficit:0, reps:0, singl:0, t62:26}.
```

No seed0-derived target is read by either independent reconstruction.  In
particular, the historically named `e483...`, `0a3a...`, endpoint-transport,
and cut1004 files belong to the separate seed0 basin and are not evidence
about the chronology below.

## 2. Exact natural K16 chronology

Let `D2` and `D3` be the consecutive triple-OR and quadruple-OR rows of the
parent.  `D3` is a permutation of all 6,435 rank-eight masks on the old 15
coordinates.  `D2` has 6,436 entries: 6,435 distinct rank-seven masks and one
rank-six entry

```text
D2[6390] = 0x13c8.
```

Tag every rank-seven `D2` mask by the new bit `0x8000`, and split at the junk
entry.  The natural order is exactly

```text
reverse(0x8000 | D2[:6390])
  + D3
  + reverse(0x8000 | D2[6391:]).
```

Its segment lengths are `6390 + 6435 + 45 = 12870`.  The canonical
newline-terminated serialization is

```text
scratch/true_fourfilter_chronology_20260731/natural_targets.word
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.
```

It contains every rank-eight K16 mask exactly once.  All 12,869 adjacencies
are Johnson edges.  The two piece joins are

```text
0xc3cc -> 0x43ce, union 0xc3ce;
0x738c -> 0xb38c, union 0xf38c.
```

Two implementations, including an independent event-jump interval replay,
reconstruct byte-identical target order and spectrum.

## 3. Exact upper spectrum

The adjacent rank-nine holes are

```text
0xb3cc, 0xd3cc.
```

Exhaustive arbitrary-width interval-OR replay sees 39,197 masks and leaves
exactly six upper holes:

```text
0xb3cc (rank 9),  0xd3cc (rank 9),
0xd3ce (rank10),  0xf3cc (rank10),
0xdbce (rank11),  0xfbce (rank12).
```

The covered-set digest is
`84c8d0ace51d8bd5c75938732f12305efe701c626e95df6dc53cf67a211188cb`.

## 4. All-schedule scalar-capacity theorem

The exact event DAG exhausts every monotone depth-three schedule with three
omitted starts and three omitted deadlines.  Its global optimum is

```text
X = {12826,12827,12872},
Y = {0,6390,6391},
selected proper-prefix area = 25,744.
```

The DP has only 16 states at its peak.  Even granting every omitted start the
uniform maximum of three lower cells gives

```text
25,744 + 9 = 25,753 < 26,332.
```

Therefore the entire three-hole P/Q fibre of this fixed natural target order
is compiler-impossible by scalar capacity alone.  The literal endpoint
credits are `3,3,1`, so the maximizing schedule has only 25,751 physical
lower cells.  Its maximal-envelope replay has no empty cell and no failed
middle row; its span histogram is `1^6433 3^6437`.

This all-schedule conclusion is stronger than any fixed-schedule Hall
failure and makes SAT/common-cap solving unnecessary for the natural order.

## 5. Exact Hall audit of the scalar optimum

For completeness, the exact generalized individual-host graph of the
maximizing schedule contains every feasible proper-prefix lower pin.  It has

```text
25,751 physical lower cells,
343,156 incidences,
maximum matching 22,822 / 26,332,
deficiency 3,510.
```

The 12 zero-host targets are

```text
8000,8001,8002,8004,8010,8020,8040,8200,8400,8800,a000,c000.
```

The canonical alternating Hall shore has 9,949 targets and 6,439 cells,
hence deficiency 3,510.  Its target-rank profile is

```text
1^1 2^15 3^105 4^455 5^1365 6^3003 7^5005,
```

and its right-length profile is `1^6435 2^2 3^2`.  The shore target digest is
`4989d292b7651194be8a381439a5b22f83ee82cd85c70a57e836436decac3ff8`.

This shore has a closed form.  Its left side is exactly every lower mask
containing `0x8000`, so

```text
|L| = sum_{j=0}^6 C(15,j) = 9,949.
```

Its neighborhood consists of the 6,435 singleton prefixes at physical
positions `0..6389` and `12828..12872`, plus exactly four longer cells

```text
(start,length) = (6389,2), (6389,3), (12826,3), (12827,2).
```

Thus `|N(L)|=6435+4=6439` and the Hall deficit is immediately
`9949-6439=3510`, without relying on the matching algorithm for the upper
bound.  The independently replayed matching of size 22,822 proves equality.

## 6. Consequence and exact open scope

The genuine natural four-filter chronology is now authenticated and closed.
It is much farther from the lower compiler gate than the misleading seed0
chronologies: its scalar deficit is already 579 before Hall, and its
maximizing-schedule Hall deficit is 3,510.

This theorem does **not** close a rethreaded four-piece chronology from the
same genuine parent, a different physical equality architecture, or K16
globally.  The correct next four-filter task is a target-order rethread that
first raises the exact all-schedule scalar bound above 26,332, then repairs
the six displayed upper holes and recomputes full Hall.  Continuing endpoint
repairs of `e483...` or `0a3a...` is duplicate seed0 work and is outside this
lane.

## 7. Frozen artifacts

```text
scratch/true_fourfilter_chronology_20260731/audit_true_fourfilter_chronology.py
  SHA 8b2cdca382368ffe2b4df37624be48df90ecf375825144e322877144fa0a6629
scratch/true_fourfilter_chronology_20260731/chronology.audit.json
  SHA ec14b3f2566f0c6bfd7a2fa52ebef68a30bca83d49aa3283134226a8498d584f
  payload 6e8116f081bcd4d00f3799fc8799f0c194a06b0e599f2927e15003d8c5adb6a1
scratch/true_fourfilter_chronology_20260731/verify_true_fourfilter_chronology_independent.py
  SHA 6a0ec6c299865b1bfeec73a1129c02782cea82890f6144edcfa8f509dbfa31a5
scratch/true_fourfilter_chronology_20260731/chronology.independent.audit.json
  SHA ddcbf298f59d51a6b486a4b67ceee86c819221385d6068388d8c168c81cf7113
  payload 0b0e3fc04116988a85d1c8bc3780d55a1b98cf613279f8aacba009a67bf5d215

scratch/true_fourfilter_hall_20260731/audit_true_fourfilter_natural_hall.py
  SHA 3352467d8ddd6e82686a2c37960b6d18bc03397c850c4e6045d149b4730a6396
scratch/true_fourfilter_hall_20260731/audit.json
  SHA d4950d6e1733b6e82a9e23b5cd7be28243211a917cf978bcd5a2dc36e8d5a3bb
  payload 03e7b9200fa242827ffe871485a8733098d66182a2b3e7b472a7c246d3c26937
scratch/true_fourfilter_hall_20260731/lower_hall_edges.tsv
  SHA 176e2e3fb792ac382ea016db3ef31cfb224effe6e3c59bec05e0bebac8cc96c8
scratch/true_fourfilter_hall_20260731/canonical_hall_left.tsv
  SHA 9c87a71eae6a066fdbf072c94c1e68a298e7c6590e7bd4abcca9047e6efb18ce
scratch/true_fourfilter_hall_20260731/canonical_hall_right.tsv
  SHA 616c3be64c2f20b8320b6d9a80e439a0079846891eeb0d6483a4c28a93a72be4
scratch/true_fourfilter_hall_20260731/verify_true_fourfilter_hall_certificate.py
  SHA 4e9f80efb0cd02fffbbc6d18ac42463956634547741e3793344f961d25bdb59c
scratch/true_fourfilter_hall_20260731/verification.json
  SHA 6f0a89fd31e501edf7717162f99abf66b53d6fede66ff814be72328243f532d0
  payload d52288f9a0f6be5667f9c942325e5833cd47ae7f845d9bc69ef9c875de202583

scratch/audit_k16_true_fourfilter_natural_chronology_20260731.py
  SHA c92caa67625abef0b332f86b93191eb0fdc37abcaa36b4082a269c62a70ee1c8
scratch/k16_true_fourfilter_natural_chronology_20260731.audit.json
  SHA e2e25c123fe6fd5d6bba6e956f55120b38ec71b4838be9f6d67c0ffe437ab5d6
  payload a61dbf1746ca325d8ca4fe77174367e87f4637d50626ea0a747b4f49969a5a9c
```
