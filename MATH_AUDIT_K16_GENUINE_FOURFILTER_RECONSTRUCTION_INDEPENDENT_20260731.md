# Genuine four-filter K16 natural chronology: independent reconstruction

Date: 2026-07-31  
Status: exact lineage, middle, seam, upper, and residence audit for the fixed natural order

## 1. Authenticated source

The only data inputs are:

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4

scratch/K15_FOURFILTER_SEED_20260731.meta.json
SHA-256 d1006c375c2cb69f595e7d56ffd0e585d4741ae3d4562bfd9e3d1141f223fea7
opening (5134,0,5,1,0), direction fwd
```

No seed0-derived K16 target, despite any historical `fourfilter` name, is read by the audit.

## 2. Derivatives and exact block formula

For the 6,438-cell source word `A`, define

```text
D2[i] = OR(A[i:i+3])
D3[i] = OR(A[i:i+4]).
```

`D2` has 6,436 distinct entries. Its exact rank histogram is
`rank6^1, rank7^6435`; the unique break is

```text
index 6390, value 0x13c8.
```

Deleting that entry leaves the entire rank-seven layer of `[15]` exactly once, split into two Johnson cycles of lengths `6390` and `45`. Their direct filtered join is non-Johnson (symmetric difference four), so the natural order leaves it external.

`D3` has 6,435 distinct rank-eight entries and is exactly the rank-eight layer of `[15]`. The opening cut `5134` splits it into blocks of lengths `5134` and `1301`. With `z=0x8000`, the metadata-explicit order is

```text
reverse(z|D2[:6390])
+ D3[:5134]
+ D3[5134:]
+ reverse(z|D2[6391:]).
```

Thus the four lengths are `6390 | 5134 | 1301 | 45`. Coalescing the two same-orientation `D3` blocks gives the equivalent three-piece formula

```text
reverse(z|D2[:6390]) + D3 + reverse(z|D2[6391:]).
```

The canonical decimal-space/newline target serialization has 12,870 distinct rank-eight masks, equals the full rank-eight layer of `[16]`, and has SHA-256

```text
0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.
```

## 3. Johnson topology and seams

Every one of the 12,869 path edges is Johnson: the complete symmetric-difference histogram is `2^12869`. The three explicit assembly boundaries are:

| cut after | left | right | union | q1 load |
|---:|---:|---:|---:|---:|
| 6389 | `c3cc` | `43ce` | `c3ce` | 2 |
| 11523 | `6cd1` | `74d1` | `7cd1` | 2 |
| 12824 | `738c` | `b38c` | `f38c` | 2 |

All three have rank-seven intersection and symmetric difference two. There are no internal non-Johnson seams.

The excluded endpoint closure is `b1cc -> d38c`. It has intersection `918c` of rank six, union `f3cc` of rank ten, and symmetric difference four. This is precisely the suppressed join between the two rank-seven `D2` components; it is not an edge of the linear chronology.

## 4. Exact upper interval audit

The adjacent-union q1 deck has 12,869 occurrences, 11,438 distinct rank-nine colours, and holes

```text
0xb3cc  0xd3cc.
```

Its load histogram is `1^10107, 2^1231, 3^100`, with duplicate excess 1,431.

Replaying every arbitrary-width linear interval OR gives exactly six upper holes:

```text
rank 9:   0xb3cc  0xd3cc
rank 10:  0xd3ce  0xf3cc
rank 11:  0xdbce
rank 12:  0xfbce
```

There are no holes at ranks 13 through 16. The numbers of seen masks by rank are

```text
8:12870, 9:11438, 10:8006, 11:4367, 12:1819,
13:560, 14:120, 15:16, 16:1.
```

## 5. Residence and run ledger

For linear positive coordinate runs, excluding endpoint-touching runs from the depth-three defect test, there are 1,426 internal runs shorter than four:

```text
length 2: 2
length 3: 1424
```

The two length-two runs are `(bit2, positions 6389..6390)` and `(bit7, positions 12824..12825)`. The complete short-run tuple deck is hash-locked in the JSON.

The new coordinate has positive runs `0..6389` and `12825..12869`, of lengths 6,390 and 45, separated by one zero run of length 6,435. Under endpoint identification its two positive runs merge, giving cyclic positive and zero runs both of length 6,435.

As a separate literal check, the unshifted clipped depth-three maximal-envelope schedule has no zero envelopes but fails 3,482 middle rows, with 4,276 missing-bit incidences. This is consistent with the internal short-run defects; it is not the optimized P/Q schedule.

## 6. Frozen artifacts and scope

```text
scratch/audit_k16_genuine_fourfilter_reconstruction_independent_20260731.py
SHA-256 bcfccc00d83f721b8261f2f630e61ad3a37a4bec5e90e5024c4af7b12d4eba46

scratch/k16_genuine_fourfilter_reconstruction_independent_20260731.targets.word
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c

scratch/k16_genuine_fourfilter_reconstruction_independent_20260731.audit.json
SHA-256 bc3ae2fd144de713e3f628d8efcfbf1d2e9f91e7f93ff968aa96f0e3c10fff7c
payload SHA-256 2d5c23c03eb0360c3520045c72bd3600d051ea18c53a354ca5854cf774416503
```

This closes authentication of the genuine natural chronology and its full upper interval deck. It does not claim that a rethreaded genuine-fourfilter order is impossible, and it does not replace the separate all-schedule P/Q or generalized lower-Hall audits.
