# Genuine four-filter endpoint-12825 reroot: Hall pass and common-cap witness

Date: 2026-07-31  
Status: exact marginal Hall pass; the emitted deterministic perfect matching fails simultaneous replay

## 1. Lineage and endpoint reroot

The audit reads only the independently reconstructed genuine natural target order

```text
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.
```

Numbering target positions from zero, it applies the two disjoint endpoint reroots

```text
reverse [0,6388]
reverse [12826,12869], i.e. the suffix after endpoint p=12825.
```

The removed boundary unions are `0xc3ce,0xf38c`; the replacements are the two formerly missing q1 colours `0xd3cc,0xb3cc`. The resulting order has canonical SHA-256

```text
c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

It is still all 12,870 rank-eight masks exactly once, and all 12,869 transitions are Johnson.

## 2. Complete upper replay

The adjacent q1 deck is complete: 11,440 distinct rank-nine colours from 12,869 occurrences. Its load histogram is

```text
1^10111, 2^1229, 3^100.
```

The exact ending-interval recurrence finds no arbitrary-width upper hole at any rank. Its seen-rank histogram equals the full upper Boolean tower:

```text
8:12870, 9:11440, 10:8008, 11:4368, 12:1820,
13:560, 14:120, 15:16, 16:1.
```

## 3. Exact all-schedule `0x8000` host DP

An independent event-DAG DP ranges over every monotone three-start/three-deadline-hole depth-three P/Q schedule and every length-one through length-three physical host for `0x8000`. Its maximum selected proper-prefix area is 32,224, with deterministic maximizing witness

```text
X = [12870,12871,12872]
Y = [0,1,6388]
host = position 6389, length 1.
```

The uniform `+9` optimistic capacity is 32,233. Boundary truncation leaves exactly 32,230 physical lower cells. The span histogram is

```text
2^6386, 3^6484.
```

The uncapped maximal envelope has rank histogram

```text
5^6481, 6^6388, 7^2, 8^2
```

and replays every middle target. At position 6,389 its value is `0xc304`; capping that singleton cell to `0x8000` alone also replays every middle row.

## 4. Generalized Hall and frozen perfect matching

The independently rebuilt individual-pin graph has:

```text
lower targets       26332
physical cells      32230
incidences         347734
zero hosts              0
matching size       26332
deficiency              0
```

Thus the marginal Hall gate passes exactly. Deterministic Hopcroft--Karp, using numerical lower-target order and ascending physical-cell order, matches `0x8000` to cell 12,781, the singleton `[6389,6390)`. The 26,332 assignments are frozen in the TSV. Their canonical pair-list hash is

```text
73b815d0c891d73e88662f39b3ff40a1dc2bcb66191673ced88a0ec9aa280fb9.
```

## 5. Simultaneous common-cap replay

For every matched target `S` on interval `J`, form the maximal common letter vector by intersecting each envelope position in `J` with `S`, simultaneously over all 26,332 assignments.

All 12,873 resulting letters remain nonzero, and the reserved `0x8000` letter survives. Nevertheless this one matching has:

```text
middle replay failures          1808
matched-lower replay failures   5045.
```

The first failure has a two-cap exact explanation. Middle row 1 wants `0xc36a`; its bit `0x0100` has precisely the three maximal-envelope hosts

```text
position 1: 0xc34a
position 2: 0x834a
position 3: 0x8368.
```

The matching contains the individually legal assignments

```text
target 0xc000 -> cell 2, interval [1,2)
target 0x826a -> cell 5, interval [2,4).
```

Each cap alone preserves the entire middle deck and realizes its own lower target. Together the two disjoint intervals cover all three `0x0100` hosts, while both targets omit that bit. Their capped letters on positions 1,2,3 are

```text
0xc000, 0x824a, 0x8268,
```

whose OR is `0xc26a`, not `0xc36a`. Enumeration of all matching caps that omit `0x0100` on these hosts shows this is the unique minimum-cardinality cover. It is therefore an exact no-good for this deterministic matching.

This does **not** prove common-cap UNSAT. Another perfect matching may avoid this pair, and no claim is made about another schedule, rethread, or non-P/Q architecture.

## 6. Frozen artifacts

```text
scratch/audit_k16_genuine_fourfilter_endpoint12825_commoncap_independent_20260731.py
SHA-256 f301f2131b04a89311a38fd55baeef231d7f7975d764034f5d3bd85f36ddc593

scratch/k16_genuine_fourfilter_endpoint12825_independent_20260731.targets.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906

scratch/k16_genuine_fourfilter_endpoint12825_matching_independent_20260731.tsv
SHA-256 bb9d9991a5698aa9616747c6ae17f110d4eb84bf2ad4be9975ba67c74a5b4b4e

scratch/k16_genuine_fourfilter_endpoint12825_commoncap_independent_20260731.audit.json
SHA-256 df7718a737414ad8ead8f451b92384cec68663d67b7a35eb21f7b7db7d15b702
payload SHA-256 ead4d63267318347768596942464882c876ce5efb27d185eb35a1d0d4327ab6a
```
