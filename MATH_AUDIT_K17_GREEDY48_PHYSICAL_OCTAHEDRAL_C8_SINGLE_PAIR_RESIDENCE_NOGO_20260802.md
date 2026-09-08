# `k=17` greedy48: octahedral-`C8` single and complementary-pair census

Date: 2026-08-02  
Status: complete finite no-go for one rank-six-core octahedral `C8`, and for
every facet-disjoint pair of such octagons whose cap debt can be restored by
the partner, on the frozen `greedy48` factor.

This result is separate from the rank-seven-core star-`C8` audit.  It does
not cover mixed star/octahedral pairs, incidence-overlapping compounds, or
three or more circuits.

## 1. Single octahedra

For a rank-six core `S` and distinct petals `a0,a1,a2,a3`, put

```text
C_i = S + a_i + a_(i+1),
T_i = S + a_i + a_(i+1) + a_(i+2).
```

The directed old phase consists of `(C_i,T_i)` and the new phase of
`(C_i,T_(i-1))`.  Modulo cyclic rooting, the complete geometric face has

```text
binom(17,6) * (11*10*9*8)/4 = 24,504,480
```

directed rotation classes.  Reverse orientation is retained as a distinct
directed phase.

The exact gate ledger is:

| gate | count |
|---|---:|
| active | 72,420 |
| protected-facet blocked | 36,295 |
| duplicate-incidence blocked | 11,084 |
| preserve all rank-ten caps | 204 |
| also remain one physical cycle | 85 |

None of the final `85` improves the number of positive runs of lengths two
and three, total positive short-run count, or residence deficit.  All have
`delta length-1 = 0`.  Their exact `(delta length-2,delta length-3)`
histogram is

| delta length-2 | delta length-3 | count |
|---:|---:|---:|
| 0 | +1 | 34 |
| 0 | +2 | 17 |
| +1 | -1 | 17 |
| +1 | 0 | 17 |

The deeper deck does move.  Of the `85` retained toggles, `68` reduce the
total number of rank-11--13 holes.  Per rank, respectively `51`, `17`, and
`34` candidates improve the rank-11, rank-12, and rank-13 count.  The best
lexicographic upper candidate has key

```text
core 377, petals (1,11,2,13)
```

and changes

```text
holes: (2006,391,34) -> (2004,392,34)
runs:  (0,2312,1887) -> (0,2312,1888).
```

It is therefore another upper/residence trade rather than a joint repair.

## 2. Complementary octahedral pairs

After protection and duplicate-incidence filtering there are `25,041`
clean active octagons.  For each octagon the program records its exact cap
multiplicity delta and the caps that would fall to zero if it were applied
alone.

For a pair `i<j` to restore every cap, every zero-load debt of `i` must be a
positive cap delta of `j`, and conversely.  The primary search is exhaustive:

* if `i` has no debt it tests every later `j`;
* otherwise it chooses the rarest debt cap and tests every later octagon
  that adds that cap;
* it then replays the complete combined cap delta, so the index causes no
  false acceptance.

Restricting to facet-disjoint pairs gives:

| pair gate | count |
|---|---:|
| indexed candidates | 2,572,003 |
| facet-disjoint | 2,569,778 |
| restore every rank-ten cap | 20,706 |
| also leave one physical cycle | 7,038 |
| improve positive residence | 0 |

For all `7,038` retained pairs, the full `24,310`-owner cycle is rebuilt and
all positive runs are replayed literally.  Several pairs reduce one run
length while increasing another, but none decreases total short-run count;
none decreases residence deficit either.  No residence witness exists in
this face.

## 3. Independent replay

A separate verifier reconstructs each octagon from its core/petal key,
replays all `85` retained singles including their rank-11--13 decks, and
replays all `7,038` retained pairs including protection, facet disjointness,
combined cap coverage, connectivity, and exact residence deltas.  It passes
all rows.  Pair-list completeness rests additionally on the necessary-hole
index proof above.

## 4. Exact scope

The proved no-go is relative to the frozen
`c68b.greedy48.factor.tsv`, its `3,944` protected facets, exact rank-eight
facet use, rank-nine degree two, complete rank-ten coverage, and one physical
component.

Excluded are:

* star/oct mixed pairs;
* overlapping-support compound circuits;
* three or more circuits;
* temporary multi-step paths that leave the cap-complete or connected face;
* other factors, source letters, lower compilation, and a universal word.

## 5. Frozen artifacts

```text
d962bbd93245cb739e7fc5afbfcfc7e36bb4994f0e5256d46a5f7ced1d2a2635  scratch/enumerate_k17_greedy48_physical_octahedral_c8_20260802.cpp
40791a37be2e33a74991cd273c1283c155ce6f6cac51bc3c5e2b374a0f640141  scratch/search_k17_greedy48_physical_octahedral_c8_pairs_20260802.cpp
cc186fb8fe032b0af1c6122cc74e39718df89c979ec7341f15685f3a27827ea7  scratch/verify_k17_greedy48_physical_octahedral_c8_pairs_20260802.cpp
24e4e74e269947d534db269061d85f5de38a63e80944f5c873f0922e3e20e4ba  scratch/k17_greedy48_physical_octahedral_c8_20260802/pc8_oct_single.audit.json
10f094cede72dfd61da7ee7a83448b0043a0aa6aff685701f860841c628bd967  scratch/k17_greedy48_physical_octahedral_c8_20260802/pc8_oct_single.valid.tsv
cc6bc7edeb6ca0ea6943defbf962dc5ea029adfedad947a497f56c264eae09ff  scratch/k17_greedy48_physical_octahedral_c8_20260802/pc8_oct_single.delta23.tsv
809c3d9e610dc7d531cf27377ad0c3d22a3b3594a075926ab65698c88b68cae5  scratch/k17_greedy48_physical_octahedral_c8_20260802/pc8_oct_single.best_upper.factor.tsv
eddb599a0d2d67f95ff31eecc99e64ba9f3dbe6902ddff2ec4ebd5dbe501a2c7  scratch/k17_greedy48_physical_octahedral_c8_20260802/pc8_oct_single.best_upper.patch.tsv
eae8394d5f8ee963600a7b8d0924d22475eab7ba386c56e5c6f02ccea6374ea3  scratch/k17_greedy48_physical_octahedral_c8_pairs_20260802/pc8_oct_pairs.audit.json
a2b7d56aa42dd2da51c350818bac85bf274a311d81c68e45274c0f6097f37051  scratch/k17_greedy48_physical_octahedral_c8_pairs_20260802/pc8_oct_pairs.connected.tsv
4613cadf8cae2243b6a72da9d01d9cc4679489805904bc1ec54f19e5cb1f6c13  scratch/k17_greedy48_physical_octahedral_c8_pairs_20260802/pc8_oct_pairs.delta123.tsv
bfa7ed9f409c616df3bef6117f6f67f72b6a5921bd78f746b4b67b40baaec9e4  scratch/k17_greedy48_physical_octahedral_c8_pairs_20260802/pc8_oct.independent.audit.json
```

Remote O3 CPU roots:

```text
/home/amodo/or15/work/pc8_oct_greedy48_single_20260802
/home/amodo/or15/work/pc8_oct_greedy48_pairs_20260802
/home/amodo/or15/work/pc8_oct_greedy48_verify_20260802
```

