# Audit: K17 residence-1972 exact minimum-long recoupling

**Date:** 2026-08-02  
**Status:** exact positive static optimum and exact negative projection result
for one explicitly bounded reroute family.  No literal-state or word claim.

## 1. Static optimum

Let `x_l` denote the number of chains of length `l`.  Any depth-at-most-three
partition of all 65,535 lower targets into 24,310 rank-eight-rooted chains
satisfies

\[
x_1+x_2+x_3=24310,
\qquad
x_1+2x_2+3x_3=65535.
\]

Subtracting twice the first equation gives

\[
                         x_3-x_1=16915.
\]

Therefore `x3>=16915`.  Equality holds exactly when `x1=0`, and then
`x2=7395`.

The O3 H100 builder starts from the residence-1972 table with histogram
`(1748,3899,18663)`.  It matches every one of its 1,748 root-only rank-eight
rows to a distinct hard long-row bottom contained in that free root.  The
complete broad reroute graph has 401,754 edges.  All 17 bottom-rank-one long
rows are forbidden as donors and remain long.  A full 1,748 matching exists,
so the emitted histogram is the exact optimum

```text
(x1,x2,x3) = (0,7395,16915).
```

Every one of the 65,535 targets occurs exactly once, every chain is strict and
ends at a distinct rank-eight root, and each of the two owner tables is a
24,310-edge perfect selected-factor phase.  Independent map/model replays
pass for both tables.

## 2. Complete one-transition menu

For a row of length one, two, or three, the declared source class assigns its
targets to a strict nested chain of nonempty contiguous intervals of three
cells.  The exhaustive flag counts are respectively `6/9/4`.  For each
supplier/head flag pair, coordinatewise Boolean lower and upper intervals are
intersected; all three letters must be nonempty and all named source covers
must reproduce exactly.

On the best phase-zero table, reference and independent implementations both
give

```text
hard heads                 16898
length-two supplier pairs  29539
length-three pairs         42279
total pairs                71818
zero hard heads               45
maximum matching           16841
deficiency                    57
Hall shore                    72 -> 15
```

The alternate owner phase is worse:

```text
length-two/three pairs      29367 / 42388
zero hard heads               120
maximum matching           16760 / 16898
deficiency                    138
Hall shore                    195 -> 57
```

Thus occurrence-labelled state consistency is not reached in either phase.

## 3. Search and exact restricted-family stop

The search first preserved the exact minimum histogram, both owner phases,
all 17 soft long rows, and the exact cumulative Hall-donor optimum `167/306`.
It then used the complete menu itself to score donor/free-root pairings and
ran a 64-seed fixed-donor portfolio.  Seed 4015 is the strict phase-zero best,
with matching `16841/16898` and 45 isolated hard heads.

The final no-go is stronger than failure of that one table.  Fix those 45
heads and take the optimistic union over the whole declared bottom-transfer
family:

1. all 401,754 legal free-root/hard-donor pairs;
2. every short state created on the free and donor rows;
3. direct removal of a zero head by selecting it as donor; and
4. every original long state which an alternative donor selection could
   restore.

Exactly 859 candidate pairs reach at least one current zero, but they reach
only six distinct zeros.  Five current zeros are movable donor rows.  All
18,663 original long states contribute zero additional providers.  The union
therefore addresses only six of 45 heads; the remaining 39 are

```text
29,165,198,495,498,520,645,1169,1520,2150,2395,3038,3246,
3798,3822,6459,6470,6483,6554,6649,6794,7254,7290,8178,9891,
10801,12870,12872,12905,12948,12950,14613,15095,19309,19320,
19376,19506,21033,22401.
```

Consequently no table in this exact reroute family can close the phase-zero
hard-head projection.  This is a union relaxation: simultaneous matching,
state consistency, and Euler constraints could only delete possibilities.

## 4. Scope

The negative result is not a theorem about every depth-three chain partition.
It does not cover a general recomputation of the `P0/P1/P2` path cover,
multi-transition or multi-row payload macros, nonnested/noncontiguous address
states, or a changed H1 factor/owner phase.  The newer residence-1943 carrier
was deliberately not used because the source projection is still negative.
Residence, deeper upper coverage, DM, common cap, compiler, and final word all
remain fail-closed.

Frozen bundle:

```text
scratch/ad_k17_h1_res1972_minlong_recoupling_20260802/
```
