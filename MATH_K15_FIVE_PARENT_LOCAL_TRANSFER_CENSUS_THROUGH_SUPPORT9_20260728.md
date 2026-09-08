# k=15 five-parent local-transfer census through support nine

Date: 2026-07-28

## Exact scope

Let the five frozen parent carriers be

```text
scratch/k15_doubletrans_05_213_hall29.json
scratch/k15_outer2_p1_h30_bridge.json
scratch/k15_trans1113_balanced_hall31.json
scratch/k15_transposition_parent_winner.json
scratch/k15_accumulated_zero_parent_winner.json
```

The following finite statement is now exhausted.

> Every globally intrinsic, single successor-transfer whose moved-tail
> support has size at most nine, and whose transfer is a disjoint union of
> permutation cycles, has been enumerated over the five-parent arc atlas.
> Each resulting path was tested for Hamiltonicity, depth-three residence,
> all upper shadows, and the exact lower Hall matching.  No candidate has
> lower deficiency below 29.

Here *globally intrinsic* means that every moved tail has all of its selected
source arcs present in the five-parent atlas.  The theorem does **not** cover
compositions of transfers, arbitrary seam/boundary reroutings, non-permutation
moves, or parent-pure transfers of support eight or nine.

Parent-pure transfers are additionally closed through support seven.  The
support-three-through-six compact audit contains 100 legal parent-pure paths;
the support-seven `3+2+2` census contains 163 more.  None improves deficiency
29.

## Support-nine census

There are four derangement types on nine moved tails.

| type | disjoint | intrinsic | Hamilton | resident | all-upper | best Hall deficiency |
|---|---:|---:|---:|---:|---:|---:|
| `9` | 3,046 | 2,974 | 464 | 0 | 0 | -- |
| `5+2+2` | 121,659,059 | 115,282,784 | 20,189,552 | 34 | 0 | -- |
| `4+3+2` | 103,466,091 | 97,428,472 | 18,833,257 | 2,880 | 706 | 31 |
| `3+3+3` | 10,878,676 | 10,183,981 | 2,139,144 | 3,638 | 347 | 29 |

Thus 1,053 support-nine candidates survive every carrier-side condition.
Exactly 47 of them retain Hall deficiency 29, all of type `3+3+3`; none
improves it.

The exact Hall-29 root targets are

```text
2575, 5801, 13616, 13620, 17738, 21641, 29776.
```

Every one of the 1,053 legal support-nine candidates gives degree zero to
all seven targets.  This is stronger than merely retaining deficiency 29:
the root obstruction is locally immobile throughout the exhausted scope.

Support-nine moves can nevertheless reorganize the old Dulmage--Mendelsohn
shore substantially.  Among the Hall-29 ties, type `3+3+3` candidate 66
changes the original 1,524-target shore neighbourhood from 1,495 cells to
1,497 cells (1,051 cells added and 1,049 removed), while the seven root
targets remain isolated.  Type `4+3+2` candidate 74 reaches 1,499 cells on
that old shore but worsens the global Hall deficiency to 37.  Consequently
the fixed shore is not itself invariant; only the seven zero roots survive
the complete local census.

## Frozen artifacts

Support three through six, intrinsic plus parent-pure:

```text
scratch/k15_parent_pure_support_le6_compact_audit.json
sha256 cb209ca07ad451aaae862dadc4bc15dc357f3fa082dc4c6d3f7e06f02c6c43d6
```

Support seven:

```text
scratch/k15_support7_all_20260728/cycle7/summary.json
sha256 69dd0a02f536582f70463137e76c32dd67a755fc45898ecdf9a0f22c4e59e131

scratch/k15_support7_all_20260728/type322/summary.json
sha256 8b27471af36c3739daf15fb7a05f0ada1cc36ed6a5543910ae54e3d165bc8319

scratch/k15_support7_all_20260728/type322/hall.jsonl
sha256 d942e9f1e4897fd31888c762979421e3b4d7b918b065943727ec290e9da40c6b
```

Support eight is recorded separately in
`MATH_K15_FIVE_PARENT_INTRINSIC_SUPPORT8_CENSUS_20260728.md`.

Support nine summaries:

```text
type9/summary.json    d3dce2a5fd3fe79396734e642edb2bd101a27142285ca0f7af64d3cb34df9d80
type522/summary.json  1cff668857e48d9f62a83d9fe9f4d555e9857b15a2eefdfe8b1d58624ac30a35
type432/summary.json  9f52742d69d1febc6fd253248c3b3fe688fb911963eecbd8f532a19206c79709
type333/summary.json  673c109fc9c1fc2e051484f603c81c06e0d2d353510331a61a4bf81f7f34dd82
```

Independent candidate-by-candidate audits:

```text
type432/independent_audit.json
sha256 874334497d6af5d7c0de83b829e45b2f58bd118ae8fbcb63ca495b802a8226a6

type333/independent_audit.json
sha256 80acb4398311ecb6ec4a3f9f0047af9988e0824e1a06969efbf6a5d371c85936
```

Exact Hall and fixed-root files:

```text
type432/hall.jsonl
sha256 dd0a753706fbb7b43e4e9248630794727b59fc5c7bd661f965a4a84a58a0c503
type432/hall_fixedzero.jsonl
sha256 5d60ebfca5088d5124c6826efdcf7deb2da053ae60db5845e9ada1a644319ca8
type432/dm_delta.jsonl
sha256 c435612212cc08532a5b6312c9f517f0b6cbdaa70712ab553343ad6c1f0c8d93

type333/hall.jsonl
sha256 848ba0a7fd09a710dde33d07e85d67060a5a215bfa05ecea23cfed37a360164a
type333/hall_fixedzero.jsonl
sha256 8e48eb69cbebf5b5b0438354f5a95271fa365f064387a7225631a4047f6ef1f
type333/dm_delta.jsonl
sha256 aa5897944701cd9854ee73ae8d5b2e8a526a39cc5a627c097e4b05e25503a3b0
```

The production support-eight/nine enumerator base is

```text
scratch/enumerate_k15_intrinsic_multiparent_support3_8.cpp
sha256 722731a8fdc51b4c3924be165e9a83d59f6e07da8dd3191bab75e460aa2d2d94
```

and the support-nine wrapper is

```text
scratch/enumerate_k15_intrinsic_multiparent_support3_9.cpp
sha256 47403cf00cd754a2a2204f1928e90918629aed633d41fda046d0d4051c6b4e72
```

## Consequence

The next meaningful move cannot be another globally intrinsic single
transfer of support at most nine.  It must use at least one capability absent
from that model: a composition, a larger support, a parent-pure support-eight
or support-nine move, or an explicit seam/boundary-changing chronology.  The
last option is especially natural because the seven root targets have known
local physical-cell motifs, but installing them requires a global fragment
ordering rather than a single permutation transfer.
