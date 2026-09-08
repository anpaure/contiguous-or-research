# K16 H1 `x467`: zero-meet block-capacity Hall contradiction

Date: 2026-07-30  
Status: **GO, exact and solver-independent on the frozen joint13 fibre**

## Scope

Fix the authenticated explicit-witness joint13 model with 55 residual targets
and 29 one-block charts per target.  Condition on the hole target
`H=0x2c6d` choosing its flat-1 singleton chart `x467`.  This note eliminates
only the three physical flat-1 meet states whose earlier first-collar cascade
minimum was zero:

```text
0x286d, 0x2c69, 0x2c6d.
```

It does not prove that `x467` is forced, does not eliminate the other three
meet states, and is not a no-go outside the thirteen editable positions.

## Canonical-closure lemma

Choose one valid chart for every residual target.  Replace the value at each
editable cell by the intersection of the labels of all selected charts which
cross that cell, taking `0xffff` when no selected chart crosses it.

This replacement preserves every selected chart.  The old cell was a submask
of each crossing target, so the new intersection only adds bits; it remains a
submask of each crossing target and cannot destroy any residual need.  Every
canonical cell is therefore an intersection of a subset of the 55 target
labels.  Their exact meet closure has 216 masks, all containing common bit 6.

For a chart with target `T`, residual need `N`, and interval-cell OR `V`, chart
validity is exactly

```text
V & ~T = 0       and       N & ~V = 0.
```

The first condition is equivalent to every cell on the interval being a
submask of `T`; the second is exactly `N subseteq V`.

## Exact per-block capacities

The other three safe blocks have widths 4, 3, and 4.  Exhausting every tuple
of 216 canonical masks gives:

| block flats | charts | tuples exhausted | maximum targets |
|---|---:|---:|---:|
| `[2,6)` | 3--12 | `216^4 = 2,176,782,336` | 23 |
| `[6,9)` | 13--18 | `216^3 = 10,077,696` | 14 |
| `[9,13)` | 19--28 | `216^4 = 2,176,782,336` | 12 |

The maximizing-sequence counts are respectively 137, 48, and 328.  The
lexicographically first maximizing tuples and their complete covered-target
sets were independently replayed from the original chart ledger.

Thus the three remaining blocks have total target capacity at most

```text
23 + 14 + 12 = 49.                                      (1)
```

This is a target-count capacity, not a cell-capacity assumption.  It already
allows every target every original chart in that block and independently
overapproximates the canonical cell tuples; hence it is a valid upper bound.

## Collar-0 capacities and Hall cut

With flat 1 fixed to the three zero states, exhaustive enumeration of all
65,535 nonzero physical flat-0 values gives the sharp collar-0 capacities

```text
cap0(0x286d) = 5,
cap0(0x2c69) = 5,
cap0(0x2c6d) = 3.
```

Choose one valid chart for each of the 55 targets and assign the target to
that chart's safe block.  These four assigned target sets are disjoint, and
each is bounded by its block capacity.  Equations (1) and the collar-0 bounds
therefore give

```text
0x286d: 5 + 49 = 54 < 55,
0x2c69: 5 + 49 = 54 < 55,
0x2c6d: 3 + 49 = 52 < 55.
```

All three zero-meet branches are impossible in the frozen joint13 fibre under
`x467`.

The inequality crucially couples overlapping intervals through their shared
physical cell values.  If every interval OR is allowed to vary independently,
each zero state has an explicit integral cover of all 55 targets; consequently
no nonnegative weighted Hall inequality in that weaker cone can close a
branch.  The canonical-cell identities are the missing interface.

## Authentication

Primary inputs and results:

```text
witness map
  SHA-256 146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a

capacity enumerator source
  SHA-256 cd55a5d1662a431ec7c674a5fe79bdc491b5d152fe92b81b62bf3ee040170edb

primary capacity result
  SHA-256 effeceba208052b798eb93356ce9a6bca36ec47c5bef588545404947123b014c

sharp collar-0 audit v3
  SHA-256 d3faedd4dc1b247b3dc608cf53c7016c758641923a3e26b9c38c45f19d5fa0e0
```

An independent H100 replay used unique directory

```text
/home/amodo/or15/work/root_hall_cut_capacity_audit_20260730_cd55a5d1
```

on CPU core 52 with a 60-second wall cap and 512 MiB address-space cap.  It
finished with exit 0 in 32.32 seconds using 9,100 KiB maximum RSS and
reproduced every structural output field—closure size, tuple counts, maxima,
maximizer counts, lexicographic witnesses, and covered-target sets.  Only the
timing fields differ.

```text
replay result
  SHA-256 347cac44f792f72254a42cae4385d2baf24ffd999707691743fe2fe5c14d5d7b

independent semantic/replay audit
  SHA-256 f9c262957c8eb2800484f39fa7387525da4031c3a8b50f043211216372dd1850
```

No SAT solver result is used in the proof.
