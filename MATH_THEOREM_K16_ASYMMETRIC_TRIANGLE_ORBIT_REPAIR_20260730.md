# K16 asymmetric carrier: exact short-rethread theorem

## Frozen objects

Let (F) be the asymmetric two-rail rank-eight factor on ([16]) in

`scratch/k16_asymmetric_two_rail_factor_20260729.json`

with SHA-256

`4f5368d063bcfddfe5c2be6d7f68d5ebc38327ee3c4f40d6b00d9d05c1ace139`.

It has 12,870 distinct middle owners, 28 cyclic components, only Johnson
edges, minimum positive residence four, both (q=1) palettes complete, 45
fixed lower-(q=2) holes, and 78 fixed upper-(q=3) holes.

The exact triangle census is

`scratch/k16_asymmetric_short_rethread_cycles_20260729.audit.json`

with SHA-256

`da6692cdb2547ac708e69d7c780511f33247101c112483cc825875f0234dad33`.

The materialized repair (F^	riangle) is

`scratch/k16_asymmetric_triangle_orbit_repair_20260729.json`

with SHA-256

`6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc`.

## 1. Exact local ledger

Index a displayed transition by (e=(a\to b)).  A directed seam from
(e=(a\to b)) to (f=(c\to d)) replaces the old exit by (a\to d).
A cyclic port permutation on cuts (e_1,\ldots,e_s) replaces

\[
  a_i\to b_i \quad\text{by}\quad a_i\to b_{i+1}
  \qquad (i\bmod s).
\]

The seam relation used in the census is exact for the stated local class:

1. (a_i\triangle b_{i+1}) has size two, so every new edge is Johnson;
2. the nine collar inequalities are exactly the possible positive runs of
   length one, two, or three that can cross one new seam;
3. cuts on one source component are more than three transitions apart.

The last condition makes the affected fixed-window neighborhoods disjoint.
Each cut affects one lower- and one upper-(q=1) label, two lower-(q=2)
windows, and three upper-(q=3) windows.  The code counts these with signed
`Counter` multiplicity.  Thus a lost duplicate is harmless, while loss of a
load-one label fails exactly when `load + delta < 1`.

The rank filters are also exact.  At (r=8), only intersections of size six
are lower-(q=2) targets and only unions of size eleven are upper-(q=3)
targets.  A rethreaded window can collapse or expand past those ranks, so
filtering both the old and new ledgers by `bit_count()==6` and
`bit_count()==11` is necessary, not a relaxation.  The (q=1) labels need
no explicit filter because every admitted seam is Johnson and therefore has
intersection rank seven and union rank nine.

For triangles, pairwise cut separation follows already from the three seam
conditions.  For lengths four and five it is checked explicitly for every
pair of cuts.

## 2. The short-cycle census

On (F), the exact directed relation contains 211,067 valid seams and 2,023
reciprocal two-switches.  No reciprocal switch is simultaneously (q=1)
safe, lower-(q=2)/upper-(q=3) safe, and hole-improving.

Every improving port cycle contains a seam that itself supplies a missing
label.  Seeding on all such provider seams is therefore complete for
positive gain.  Among 694 provider-containing directed triangles, exactly
15 are simultaneously (q=1) safe and lower-(q=2)/upper-(q=3) safe.
Every one gains exactly one upper-(q=3) hole.  Among 3,961
provider-containing separated directed four-cycles, none is simultaneously
safe and improving.

After applying the 15 triangles, the round-one length-five census

`scratch/k16_asymmetric_short_rethread_cycles_round1_len5_20260729.audit.json`

(SHA-256
`fb0e888e186e3e4d9ba00f00174acbd2b8f82548d309e6ad06d895964e5689fc`)
contains 29,521 provider-seeded separated directed five-cycles.  None is
even (q=1) safe.  This is a scoped no-go for one length-five cyclic port
permutation; it does not exclude two compensating port cycles, a longer
braid, or a nonlocal reconstruction.

## 3. The fifteen triangles are one free \(\mathbb Z_{15}\)-orbit

Let \(\rho\) rotate coordinates (0,\ldots,14) and fix coordinate 15.  Take
the triangle with transition indices

\[
  (6708,9581,7768),
\]

which supplies upper-(q=3) mask 39911.  Direct rotation of all three old
directed edges shows that

\[
 \bigl\{\operatorname{can}(\rho^j(6708,9581,7768)):0\le j<15\bigr\}
\]

is exactly the set of 15 safe triangle orders in the census.  Here
`can` means cyclic rotation of the three ports, not reversal.  Likewise the
15 gained masks are exactly

\[
  \{\rho^j(39911):0\le j<15\}.
\]

The action is free: both sets have size 15.  All 45 cuts are distinct, all
lie in source component 2, and their minimum cyclic gap is seven.

## 4. Simultaneous action is exact

For each triangle, the old and new lower-(q=1) multisets are equal and the
old and new upper-(q=1) multisets are equal.  This is stronger than mere
coverage safety.  Each triangle is also exactly lower-(q=2) neutral.  Its
upper-(q=3) signed ledger consists of two (-1) and two (+1) terms; one
positive term fills its orbit member and neither negative term kills a
covered label.

Applying all 15 port permutations simultaneously is well-defined because
the 45 tails and 45 heads are distinct.  It merely permutes those heads in
15 disjoint 3-cycles, so the successor map remains a permutation of all
12,870 owners.  The minimum cut gap seven makes all (q\le3) local ledgers
independent.  A separate full physical replay, which does not use this
additivity argument, proves:

* 12,870 distinct rank-eight owners remain;
* every edge remains Johnson;
* the component count and length multiset remain unchanged;
* minimum positive residence remains four;
* both entire (q=1) signed load vectors have delta zero;
* the lower-(q=2) load vector has delta zero, so its 45 holes are unchanged;
* upper-(q=3) holes fall from 78 to 63, removing exactly
  \(\{\rho^j(39911)\}\), with no new upper-(q=3) hole.

Thus the orbit repair is a genuine exact descent by 15 physical holes, not
15 separately compatible moves whose simultaneous composition was assumed.

## 5. Fixed-width \(q=4\) is not arbitrary-upper coverage

The repair creates 15 fixed upper-(q=4) holes.  These form the orbit

\[
  \{\rho^j(40443):0\le j<15\}.
\]

“Fixed (q=4)” means union of exactly five consecutive middle states.  It
does **not** mean that the corresponding rank-12 target is absent from all
interval unions.  Independent exhaustive replay finds every one of these 15
rank-12 masks as the union of six consecutive states.  Consequently

\[
  H^{\mathrm{fixed}}_{q=4}=15,
  \qquad
  H^{\mathrm{arbitrary}}_{\mathrm{rank} 12}=0.
\]

The new fixed-width orbit violates an all-fixed-shadows sufficient carrier
condition, but it creates no actual arbitrary-upper rank-12 hole.  The
remaining arbitrary-upper deficit is exactly the same 63 rank-11 masks as
the remaining fixed upper-(q=3) deficit.

## 6. Independent replay and scope

The independent checker

`scratch/audit_k16_triangle_orbit_independent_20260730.py`

reconstructs the two physical successor maps, proves the rotation orbit,
replays every fixed load counter and cyclic positive run, and finds the
minimum arbitrary width of the 15 rank-12 masks without importing the
materializer or its audit helpers.  Its output is

`scratch/k16_asymmetric_triangle_orbit_independent_20260730.audit.json`.

It returns `PASS`.

The result is a theorem about this frozen factor and the enumerated local
port-permutation class.  It is not a proof that no compound repair exists.
After the orbit repair, the primary fixed ledger still has 45 lower-(q=2)
holes and 63 upper-(q=3) holes, so (F^\triangle) is a near-carrier, not an
optimal (k=16) word certificate.

The historical census schema string still says `reciprocal-2switch`; that is
a metadata label inherited by the length-three/four/five extensions, not a
restriction of the enumerated data.  The materializer's output-path helper
was also repaired so relative and out-of-repository output paths replay
without affecting the frozen factor bytes.
