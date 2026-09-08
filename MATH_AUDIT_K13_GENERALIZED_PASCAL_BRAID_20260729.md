# The exact k=13 carrier is a generalized Pascal braid

Date: 2026-07-29

Status: exact reconstruction and solver-free audit of the verified source
factor and of the final one-seam path.  No new `k=15` word is claimed.

Reproducer:

```text
python3 scratch/audit_k13_pascal_braid.py
```

Machine-readable output:

```text
scratch/k13_pascal_braid_audit.json
```

## 1. The test

Distinguish coordinate `z=12` and split the rank-7 vertices of the exact
`k=13` source factor into

```text
A = z+T, |T|=6,             B = U, |U|=7.
```

An elementary common-colour Pascal block has cyclic order

```text
zT_a,...,zT_b,U_{b-1},...,U_a,
```

where `U_i=T_i union T_{i+1}`.  Consequently it has one maximal `A` run,
one maximal `B` run, its run lengths differ by one, and the `B` run is the
reverse of the adjacent-union sequence of the `A` run.

The audit reconstructs the two physical cycles directly from

```text
scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json
```

using the quotient choices and voltages, rather than trusting any cached
physical cycle.

## 2. Exact verdict

The two quotient components have lengths `119,13` and lift to physical
cycles of lengths `1547,169`.  Their sector statistics are

| physical cycle | A vertices | B vertices | A runs | B runs |
|---:|---:|---:|---:|---:|
| 1547 | 833 | 714 | 119 | 119 |
| 169  | 91  | 78  | 13  | 13  |
| total | **924** | **792** | **132** | **132** |

Thus neither physical component is one forward old-rank-6 path followed by
its reversed adjacent-union path.  The gross count alone proves this: one
elementary block contributes `|A|-|B|=1`, whereas the two physical cycles
together have

```text
|A|-|B| = 924-792 = 132 = Cat(6),
```

not two.

The stronger local test also fails completely.  For each of the 132 maximal
`A` runs, let `E` be its sequence of adjacent unions.  In an elementary
block the following `B` run must be `reverse(E)`.  The number of exact runs
is

```text
0 / 132.
```

Moreover the 792 `AA` transitions have all 792 distinct lower colours but
only 645 distinct upper colours:

```text
AA intersections: 792 / 792 rank-5 colours,
AA unions:         645 / 792 rank-7 colours,
load histogram:    1^516 2^111 3^18.
```

Because every lower colour occurs on exactly one `AA` edge, the associated
old-`k=12` common-colour occurrence graph has maximum matching exactly

```text
645 / 792,
```

an exact deficiency of `147`.  Therefore the verified `k=13` optimum is not
obtainable from the strict common-colour theorem by merely choosing a
different pairing or starting point.

## 3. What the carrier does instead

It is an exact **two-sector braid**.  Its edge types and their shadow
channels are

```text
AA = 792,       AB = 132,       BA = 132,       BB = 660.
```

| channel | occurrences | distinct / target | load histogram |
|---|---:|---:|---:|
| `AA` lower, with z removed, rank 5 | 792 | **792/792** | `1^792` |
| `AB+BA+BB` lower, no z, rank 6 | 924 | **924/924** | `1^924` |
| `AA+AB+BA` upper, with z removed, rank 7 | 1056 | **792/792** | `1^576 2^168 3^48` |
| `BB` upper, no z, rank 8 | 660 | **495/495** | `1^360 2^105 3^30` |

So the first lower shadow is perfect in both sectors.  The strict Pascal
route would require the `AA` upper colours themselves to be the full
rank-7 deck.  The actual solution instead lets the 264 cross-sector edges
repair and rebalance the missing `AA` upper colours.  This is exactly the
freedom discarded by the common-colour matching reduction.

The factor is `Z_13`-equivariant, and the audit verifies that every choice
of distinguished coordinate has the identical signature

```text
A924 B792, 132 A-runs, 792 AA edges,
792 distinct AA-lower colours, 645 distinct AA-upper colours.
```

Thus the phenomenon is intrinsic, not an artefact of choosing coordinate
12.

## 4. The final splice preserves the braid

The optimal path certificate

```text
scratch/k13_two_cycle_one_seam_path_000.json
```

removes the two source edges

```text
2395--2515,       2167--2391
```

and inserts the seam

```text
2515--2391.
```

All three are `BB` edges.  Hence the opened and spliced path retains all
`792 AA`, `132 AB`, and `132 BA` transitions, while `BB` drops from 660 to
659.  This is why it loses exactly one native lower-q1 colour while retaining
all upper shadows; the depth-3 compiler absorbs that one deliberate hole.

## 5. General two-sector counting law

For an even-to-odd step `2r -> 2r+1`, let

```text
A = z + C([2r],r),             B = C([2r],r+1).
```

If a cyclic factor has a perfect first lower shadow, then the number `R` of
maximal `A` runs is forced:

```text
R = |A|-|B| = C(2r,r)-C(2r,r+1) = Cat(r).
```

The edge counts are then forced as well:

```text
AA = |A|-R = |B|,
AB+BA = 2R,
BB = |B|-R.
```

Perfect lower q1 is equivalent to the two exact rainbows

```text
AA intersections                    = C([2r],r-1),
cross intersections + BB intersections = C([2r],r).
```

Upper coverage only requires

```text
AA unions + cross unions cover C([2r],r+1),
BB unions cover C([2r],r+2).
```

No equality between the `AA` union deck and the `B` vertex deck is needed.
The strict common-colour lift is the special case imposing precisely that
extra equality and a reverse-order pairing.

## 6. Consequence for the k=15 search

For `14 -> 15`, the generalized target has the exact forced counts

```text
A vertices = C(14,7) = 3432,
B vertices = C(14,8) = 3003,
R = Cat(7) = 429,
AA = 3003,
AB+BA = 858,
BB = 2574.
```

The current common-colour lane tries to make all 3003 `AA` upper colours
distinct.  Its best exact matching `2918/3003` has deficiency 85.  The
solved `k=13` example proves that this is a sufficient-condition deficit,
not a construction barrier: cross-sector edges can supply missing upper
colours while preserving a perfect lower shadow.

The more faithful `k=15` target is therefore a two-sector factor with

1. exact `A` and `B` vertex decks;
2. 429 alternating runs;
3. exact lower rainbows in the two channels above;
4. upper coverage after `AA` and cross contributions are combined;
5. depth-3 residence, deeper shadows, and a compatible compiler.

This is broader than the strict forward/reverse Pascal lift but still has
fully prescribed sector sizes and local edge-channel constraints.  The
verified `k=13` certificate is its first exact template.
