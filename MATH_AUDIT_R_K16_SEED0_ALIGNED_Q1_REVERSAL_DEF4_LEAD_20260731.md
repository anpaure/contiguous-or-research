# Exact K16 aligned-q1 reversal and deficiency-four compiler lead

Date: 2026-07-31  
Lane: R  
Status: proved for the stated target order and P/Q schedule; not yet a K16 word

## 1. Lineage correction

The file `scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word`
has SHA-256
`e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452`.
Its numerical carrier and compiler calculations are valid, but its filename is
misleading. Its first 6,435 targets are exactly the reverse width-four trace of
`scratch/k15_repeatfree_parents_20260730/k15seed_0.word`, whose SHA-256 begins
`018fa0a98239950d`. That parent is not repeat-free at width three: the rank-seven
mask `0x39c8` occurs at starts 45 and 5,223. Consequently this is a seed0-derived
basin, not the independently authenticated four-filter/repeat-free basin.

For reference, the actual four-filter K15 seed on H100 has SHA-256
`51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4`,
and its natural K16 target order has canonical newline-terminated SHA-256
`0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c`.
The theorem below concerns the seed0-derived basin only.

## 2. Exact switch

Number target positions from zero. Starting from the `e483...` target order,
cut after positions 2,129 and 10,447 and reverse the inclusive block

\[
T[2130\ldots10447].
\]

The removed boundary colours are `0x29cf` and `0xa98f`; the inserted boundary
colours are `0xa9ce` and `0xa9cf`. The frozen target order is

`scratch/threadA_k16_fourfilter_q1_twoopt_frontier_20260731/cuts_2129_10447.targets`

with SHA-256

`0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b`.

It consists of all \(\binom{16}{8}=12{,}870\) rank-eight masks exactly once.
Its q1 deficit is the singleton `0xb8ce`. Its complete arbitrary-width upper
deficit is exactly

\[
\{\mathtt{0xa9fe},\mathtt{0xb8ce},\mathtt{0xb8cf}\}.
\]

Thus this reversal repairs `0xa9ce` and `0xa9de` from the original five-hole
tower, but not the displayed three masks.

## 3. Exact P/Q capacity

The exact depth-three event-DAG dynamic program has maximum-area schedule

\[
X=(10457,12871,12872),\qquad Y=(0,1,6101).
\]

Its selected proper-prefix area is 30,098. Including the nine optimistic
omitted-start cells gives scalar capacity 30,107, above the 26,332 lower
targets. The span histogram is \(2^{8512},3^{4358}\). The maximal envelopes
are all nonzero, replay every middle row literally, and have rank histogram
\(4^3,5^{4354},6^{8512},7^2,8^2\).

## 4. Exact generalized lower Hall witness

For the schedule in Section 3, include every individually feasible physical
lower interval pin of length at most three. A target \(S\) is adjacent to a
cell \(C\) exactly when

1. \(S\subseteq O_C\), where \(O_C\) is the OR of its maximal envelopes;
2. the mandatory carrier mask \(M_C\) is contained in \(S\); and
3. every envelope in the cell meets \(S\).

This graph has 26,332 targets, 30,104 selected lower cells, and 357,316
incidences. Its maximum matching has size 26,328. The canonical alternating
shore has 29 targets and exactly 25 neighbouring cells, hence certifies
\(\operatorname{def}=29-25=4\).

The three zero-host targets are `0x29cc`, `0x8000`, and `0x898d`. The remaining
unit of deficiency is one 26-target/25-cell component. Its targets are

```text
0169 016b 017b 01e9 01eb 0369 03e9 0569 056b 0769 0969 096b 0979
09e9 0b69 0d69 11e9 1969 8169 816b 8179 81e9 8369 8569 8969 9169
```

and its common core is `0x0169`. The full shore and cell indices are frozen in
`scratch/k16_seed0_q1_a9ce_2129_10447_maxarea_generalized_hall_20260731.audit.json`,
whose file SHA-256 is
`1711d80db837adac26a84d52128037c5f9b4a639017e8903b6dcdb96ac76dc99`
and payload SHA-256 is
`4cec9a7eaa788e19421bc0e4f23ad726708e84c7f190a0ab2cbc6efd55cc8d17`.

## 5. Complete single-reversal boundary

There are 136 endpoint-compatible single reversals offering at least one of
the original missing q1 colours. Exactly four strictly reduce the q1 deficit
without creating another q1 hole. None installs both missing q1 colours. Only
the reversal in Section 2 retains scalar compiler capacity at least 26,332;
the other three have best capacities 26,082, 23,710, and 25,839.

From the Section 2 order, the only q1-completing single reversal is the
inclusive reversal `T[6099..6172]`. Its exact maximum scalar capacity is only
25,751. Therefore no second single reversal can complete q1 while retaining
the necessary scalar compiler capacity.

The independent census is
`scratch/k16_seed0_q1safe_single_reversal_area_20260731.audit.json`, SHA-256
`ad7c568223fb30f00f333b9b3cad1ad6970b0ade424b7264107bdbf9cc2a4624`.

## 6. Exact remaining task

A successful continuation must be a genuinely compound rethread. It must
simultaneously:

1. install q1 colour `0xb8ce`;
2. create upper witnesses for `0xa9fe` and `0xb8cf` without losing existing
   upper targets;
3. retain a P/Q schedule with selected area at least 26,323; and
4. add independent support for `0x29cc`, `0x8000`, and `0x898d`, plus one
   extra neighbour for the 26/25 `0x0169` component, or change the Hall
   decomposition so a recomputed matching is perfect.

Protecting only the three zero hosts is insufficient: the 26/25 component is a
fourth independent obstruction. Scalar area alone is also insufficient. Every
compound move must be replayed against the exact maximal envelopes and the full
29-versus-25 shore.

No literal K16 word follows yet. Middle and upper coverage, lower Hall,
simultaneous capped-envelope realization, and literal replay remain distinct.
