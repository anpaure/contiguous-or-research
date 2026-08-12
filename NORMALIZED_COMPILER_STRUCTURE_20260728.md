# Raw exact-word structural census

This report is generated only from `answers/kNN.word` by
`scratch/analyze_raw_optimal_words.py`.

| k | L | d | slack | flat middle | Johnson | min residence | lower holes | upper holes | exceptional section blocks |
|---:|---:|---:|---:|:---:|---:|---:|---:|---:|---:|
| 6 | 21 | 1 | 0 | yes | 19/19 | 2 | 0 | 0 | - |
| 7 | 37 | 2 | 10 | yes | 34/34 | 3 | 2 | 0 | - |
| 8 | 72 | 2 | 51 | yes | 67/69 | 3 | 1 | 0 | 8+8 |
| 9 | 128 | 2 | 0 | yes | 125/125 | 3 | 3 | 0 | - |
| 10 | 254 | 2 | 122 | yes | 251/251 | 3 | 0 | 0 | 23+24 |
| 11 | 465 | 3 | 369 | yes | 461/461 | 4 | 2 | 0 | - |
| 12 | 926 | 2 | 266 | yes | 923/923 | 3 | 1 | 0 | 26+25 |
| 13 | 1719 | 3 | 1059 | yes | 1715/1715 | 4 | 1 | 0 | - |
| 14 | 3434 | 2 | 392 | yes | 3431/3431 | 3 | 0 | 0 | 3+3 |

`lower holes` and `upper holes` sum the missing exact-rank sliding
shadows over every available depth. `exceptional section blocks` is
the minimum zero-block plus one-block count of a coordinate in an
even-dimensional central path.

## Deadline slack and compiler attenuation

| k | unused capacity | repeated lower cells | maximal entries kept | derivative error cells | max deleted run |
|---:|---:|---:|---:|:---|---:|
| 6 | 0 | 0 | 14/21 | [7, 0] | 1 |
| 7 | 0 | 10 | 27/37 | [10, 2, 0] | 2 |
| 8 | 1 | 50 | 63/72 | [9, 2, 0] | 2 |
| 9 | 0 | 0 | 81/128 | [47, 3, 0] | 2 |
| 10 | 2 | 120 | 197/254 | [57, 1, 0] | 2 |
| 11 | 2 | 367 | 397/465 | [68, 3, 1, 0] | 3 |
| 12 | 2 | 264 | 625/926 | [301, 30, 0] | 2 |
| 13 | 2 | 1057 | 1300/1719 | [419, 84, 1, 0] | 3 |
| 14 | 1 | 391 | 1910/3434 | [1524, 289, 0] | 2 |

The last derivative always has zero error.  Thus the compiler may
delete hundreds of coordinate occurrences at depth 0 while its error
collapses to zero by the prescribed central depth.

## Cyclic carrier recovery from the raw path

| k | circulant L1 defect | edge-orbit occupancy | recovered cyclic factor |
|---:|---:|:---|:---|
| 6 | 11 | `{'1': 6, '2': 2, '3': 3}` | - |
| 7 | 19 | `{'1': 9, '2': 6, '3': 3, '4': 1}` | - |
| 8 | 37 | `{'1': 29, '2': 15, '3': 2, '4': 1}` | - |
| 9 | 67 | `{'1': 44, '2': 28, '3': 4, '4': 2, '5': 1}` | - |
| 10 | 89 | `{'1': 117, '2': 46, '3': 10, '4': 3}` | - |
| 11 | 1 | `{'10': 1, '11': 41}` | valid; components [462]; +1/-0 |
| 12 | 309 | `{'1': 502, '2': 158, '3': 31, '4': 3}` | - |
| 13 | 3 | `{'1': 1, '12': 2, '13': 130}` | valid; components [169, 1547]; +2/-1 |
| 14 | 1063 | `{'1': 1540, '2': 454, '3': 182, '4': 69, '5': 20, '6': 9, '7': 1}` | - |

For k=11 and k=13, the literal coordinate labels expose an almost
circulant transition matrix.  Completing every occupancy-(k-1) edge
orbit and deleting every occupancy-1 seam reconstructs the invariant
2-factor and certifies its component count.

## Missing central shadows and where the word pays for them

| k | central lower deficits | witnesses outside the central row |
|---:|:---|:---|
| 7 | q1:13, q1:70 | 13@D1[0]/bd0; 70@D0[36]/bd0,D1[35]/bd0 |
| 8 | q1:76 | 76@D0[71]/bd0 |
| 9 | q1:170, q2:42, q3:10 | 170@D1[126]/bd0; 42@D0[126]/bd1; 10@D0[85]/bd42 |
| 11 | q1:155, q2:154 | 155@D2[0]/bd0; 154@D0[464]/bd0 |
| 12 | q3:152 | 152@D0[663]/bd262 |
| 13 | q1:2135 | 2135@D0[1718]/bd0 |

A missing colour of the linear central carrier is not necessarily a
defect of the OR word: the compiler can pay it in a shorter row.  The
k=11 and k=13 payments are literal boundary flags.

## Even-dimensional section fingerprints

| k | distinguished coordinate | block lengths | lower coverage (0/1) | upper coverage (0/1) | circulant defects (0/1) | recovered structured side |
|---:|---:|:---|:---|:---|:---|:---|
| 8 | 6 | `1:3 0:5 1:3 0:2 1:9 0:4 1:4 0:4 1:4 0:8 1:3 0:5 1:6 0:6 1:3 0:1` | 24/35 / 23/35 | 21/21 / 21/21 | 19 / 17 | - |
| 10 | 1 | `1:13 0:5 1:3 0:3 1:6 0:6 1:6 0:2 1:3 0:15 1:7 0:5 1:4 0:3 1:8 0:8 1:6 0:5 1:4 0:2 1:7 0:4 1:7 0:6 1:3 0:1 1:4 0:3 1:3 0:6 1:3 0:3 1:3 0:2 1:7 0:6 1:5 0:10 1:7 0:13 1:6 0:4 1:4 0:1 1:6 0:13 1:1` | 90/126 / 93/126 | 84/84 / 84/84 | 56 / 69 | - |
| 12 | 12 | `0:47 1:10 0:13 1:19 0:14 1:4 0:5 1:37 0:13 1:10 0:7 1:3 0:20 1:4 0:13 1:10 0:10 1:37 0:4 1:4 0:7 1:10 0:3 1:8 0:33 1:25 0:7 1:3 0:12 1:29 0:19 1:14 0:9 1:21 0:29 1:31 0:33 1:29 0:10 1:24 0:27 1:19 0:38 1:30 0:5 1:5 0:13 1:70 0:68 1:6 0:3` | 428/462 / 426/462 | 330/330 / 330/330 | 132 / 127 | - |
| 14 | 14 | `0:419 1:3 0:270 1:966 0:1027 1:747` | 1713/1716 / 1713/1716 | 1287/1287 / 1287/1287 | 362 / 9 | 1:[169, 1547] |

At k=14 the distinguished coordinate splits the path into exactly six
long sections.  One transformed side independently reconstructs an
almost Z_13-invariant carrier; the other is an asymmetric completion
forest.  This is a raw-word signature of an asymmetric odd-to-even
braid, not a literal copy of the saved k=13 answer.

## Rank-quantile boundary exceptions

| k | minimum replacements by precentral depth | exceptional masks |
|---:|:---|:---|
| 6 | [0] | [] |
| 7 | [0, 0] | [] |
| 8 | [0, 0] | [] |
| 9 | [0, 0] | [] |
| 10 | [0, 0] | [] |
| 11 | [1, 1, 0] | [31, 159] |
| 12 | [0, 0] | [] |
| 13 | [3, 1, 0] | [1552, 2135, 2147, 2161, 2167] |
| 14 | [38, 0] | [51, 77, 97, 172, 323, 356, 404, 534, 833, 1049, 1105, 1217, 1601, 1794, 2054, 2136, 2322, 2625, 2832, 3077, 4178, 4230, 4418, 4642, 4680, 4868, 5154, 5504, 6192, 6464, 6672, 7232, 8229, 8353, 8466, 9219, 9249, 9498, 10280] |

Exact rank grading is therefore not the right general invariant:
k=13 and k=14 use small, nested terminal exceptions.  A uniform
construction should preserve a bounded boundary flag rather than
forbid every quantile impurity.

