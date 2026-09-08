# K16 carrier3: exhaustive 22-circuit span audit

Date: 2026-07-30

Status: **PASS_EXHAUSTIVE_NO_HALL_IMPROVEMENT**, within the precisely
defined alternating-circuit span below.

## Scope

Start from the authenticated carrier3 chronology

```text
SHA256 6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0
```

and the 22 unique primitive alternating circuits obtained from all 21
content-unique saved parents.  Enumerate all `2^22 = 4,194,304` circuit
subsets.  A subset survives only when its switched edge set is
degree-compatible, connected, schedule-valid under maximal erosion, and has
complete upper coverage.  This theorem does **not** quantify over arbitrary
new rethreads, new parent factors, or edge circuits outside this catalogue.

## Exact census

| stage | count |
|---|---:|
| all circuit subsets | 4,194,304 |
| degree-compatible | 98,304 |
| connected paths | 36,864 |
| schedule/geometry valid | 4,838 |
| upper-complete | 4,802 |

Every one of the 4,802 terminal chronologies was passed through an exact
Hopcroft--Karp lower-compiler matching audit.

* minimum Hall deficiency: **22**;
* unique minimizer: the unchanged carrier3 (`id=0`);
* next deficiencies: `23, 24, 25, 25, 25, 27, ...`;
* hence no circuit combination improves the carrier3 Hall score.

An independent provider-diagonal replay gives a stronger structural census.
Among the 22 missing cells of the authenticated Pascal Hall diagonal, a
terminal state regenerates at most three, and no state regenerates any of the
19 rank-5 private providers:

| regenerated diagonal cells | states |
|---:|---:|
| 0 | 14 |
| 2 | 1,944 |
| 3 | 2,844 |

The exact nonzero bit patterns are `0x280000` (648), `0x300000` (1,296), and
`0x380000` (2,844).  Thus this alternating-circuit span cannot transport the
rank-5 diagonal and is the wrong move space for the optimal repair.

## Frozen artifacts

Bundle:

```text
scratch/k16_carrier3_full22_circuit_cube_nogo_20260730/
```

Primary hashes:

```text
hall.full.tsv                 96b5db75ea99fd30210cfb249dc4948e0ccc986358660be276f6960ba462be3c
meta.tsv                      83ac53096d49e70fa805c9ec762acf0951aeb175ac881b76cf59dda84830475a
circuits.tsv                  18d2d0c13b4cd978046a3e0e4c851651e621d027ff8b9e007b49c03fe9a857c1
fullcube.diagonal22.tsv       c7663b430900ee276d9776a9747be2081505ae73b6ade4465a27818c84f400d9
fullcube.diagonal22.audit.json 7f626c6d045384fea991186dacf96d92a1a7457a0fa3565cc9685f7c4546781b
audit.json                    b5bc4c0303e488a20768d193f413e377b314cab87501df7c98f47f26c99568f9
```

Independent compact audit:

```text
scratch/audit_k16_carrier3_full22_circuit_cube_nogo_20260730.py
SHA256 59a6042ecd0e0b304c07525e69b7f54ffda247ef23dfd5d384f03f0aeefc1cff
```

Its canonical payload hash is
`738f3dac259d6d059c6ab05c2682589639e75fe43b1868204c2c2c095d98280a`.

## Disposition

Close the saved-parent 22-circuit hybrid lane.  The next search must introduce
a genuinely new rethread that crosses the two K15 parent-reflection domains or
otherwise regenerates/transports the 19 rank-5 private providers.  Generic
selection inside the old circuit span is now exhaustively refuted.
