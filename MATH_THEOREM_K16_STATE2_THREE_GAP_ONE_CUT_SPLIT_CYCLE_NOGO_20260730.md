# K16 state2 three-gap one-cut split-cycle theorem

Date: 2026-07-30

## 1. Exact minimal separated-fragment class

Fix either authenticated state2 one-blocker source and an unordered triple of
distinct radius-three cofacet centres.  Remove the three seven-row collars
and preserve the residual core, its order, and every row value.  Choose one
labelled gap from each of the three frozen pairwise-disjoint repair sets.

Choose one collar, orient all three collars independently, and cut the chosen
oriented collar once at an internal position \(k\in\{1,\ldots,6\}\).  This
gives four labelled pieces: two nonempty split fragments and two intact
oriented collars.  Distribute them over the three labelled gaps subject to:

1. every gap receives a nonempty ordered block; and
2. the two split fragments occur at distinct gaps.

Exactly one gap therefore receives two pieces.  Both orders of that pair and
both assignments of the singleton pieces to the other gaps are included.
This is a minimal separated-fragment extension of the intact three-gap class
in added cut count: it adds one internal collar cut and no value edit or
residual-core move.  The descriptor definition uses no directed value
transfer or core-segment atom; no disjointness of resulting physical words
from other search fibres is claimed.

## 2. Exact size

For one oriented cut, choose the doubleton gap, its unordered pair other than
the forbidden split-fragment pair, the singleton assignment, and the order
inside the doubleton block.  The number of allocations is

\[
 3\cdot5\cdot2\cdot2=60.                                    \tag{1}
\]

There are three choices of split collar, six cut positions, and \(2^3\)
global collar orientations, hence

\[
 3\cdot6\cdot 2^3\cdot60=8640                              \tag{2}
\]

layouts per labelled repair-gap triple.  The frozen catalogue has 14,560
repair-gap triples across the two sources, so the exact descriptor count is

\[
 14560\cdot8640=125{,}798{,}400.                            \tag{3}
\]

The census represents these by 1,451,520 piece layouts and takes the product
of their three exact compatible-gap sets; it does not materialize the raw
125-million-row table.

## 3. Exact local projection

All 21 selected collar values are globally unique in their source for every
centre triple; every selected collar avoids the three source flat pairs; and
every frozen repair gap avoids splitting a retained core flat.  Thus all
three old flats survive every descriptor and no piece or insertion seam can
create a new flat.  The first flat may translate, but every descriptor has
the source flat order and the authenticated depth phase at each repair port.

For each ordered block at each labelled gap, replay every row whose
depth-at-most-three dependency cone meets that block, including all internal
piece seams and the removal closure.  The three repair neighborhoods remain
disjoint even at the maximum fourteen-row doubleton block.  Hence these
constant-phase port tests are necessary and factor independently; outside
the three neighborhoods the source replay is unchanged.

The complete projection is

| stage | representations |
|---|---:|
| exact descriptors | 125,798,400 |
| locally carrier-compatible | **21** |

The 21 rows split 14/7 by source and occur in only 20
`(source,centre-triple)` instances.  Every one uses:

- forward orientation for all collars;
- the three zero-offset closure gaps; and
- an endpoint cut \(k=1\) or \(k=6\).

They collapse to three physical words, each represented seven times by the
choice of an inert third collar.

A structurally separate permutation/divider enumeration reproduces all
1,451,520 layouts and 125,798,400 descriptor weights.  Its ordered projected-
layout digest is
`63abb1ef3731d18cbf06e68501f6d0118744aa8e7c34c6140319d776d33ba135`,
and its survivor set matches the primary 21-row catalogue exactly.

## 4. Minimal compatibility cycle

The intact class kept seven rows at every repair gap, so its length offset
was identically zero and any nonidentity assignment required a missing donor
permutation cycle.  A separated one-cut move permits the shorter split block
to contribute \(-1\) row at one port and the paired block to contribute
\(+1\) at another.  The exact port table leaves only the two unit excursions

\[
 0\longrightarrow-1\longrightarrow0,
 \qquad
 0\longrightarrow+1\longrightarrow0.                       \tag{4}
\]

Thus a length-balance cycle, rather than a donor permutation cycle, is the
minimal escape within this class from the intact theorem.  All non-endpoint
cuts \(k=2,3,4,5\), reversed orientations, nonzero gap offsets, and larger
excursions in this class fail a literal port equation.

The three surviving physical moves are exactly:

| case | literal one-row relocation | offset cycle |
|---:|---|---|
| 0 | move source row 1055 immediately before collar 2167 | `0,-1,0` |
| 0 | move source row 4390 immediately after collar 2167 | `0,+1,0` |
| 1 | move source row 5319 immediately after collar 4025 | `0,+1,0` |

## 5. Full G0, upper, and lower filters

Independent materialization and full replay give:

| physical word SHA-256 | flats | capacity | upper holes | static-lower holes |
|---|---|---:|---|---|
| `1a0a384f3b330914a677c9f275ddb4bac6fa7c18fbb1c2a7a9740c7634dd41d0` | `1101,12869,12871` | 26,844 | `0x197b,0x397a` | `0x1639,0x9932` |
| `9cf9146e1d15f0fedf32171589541e25930b448541b68515a9d41e6e2538f1b6` | `1102,12869,12871` | 26,845 | `0x539d,0x53ed,0x579d` | `0x1639` |
| `135f9a6429ff29ab51c4729c56deaa6f3b6e4bce9e052f8bf91f52bbd78ed022` | `2031,12869,12871` | 27,774 | `0x14df` | `0x1879,0x949c` |

All three are exact tail-fixed G0 carriers with nonzero maximal envelopes,
capacity at least 26,332, and literal middle replay.  None is upper-complete,
and none is static-lower-zero-free.  Therefore this exact class contains no
word satisfying G0, upper completeness, and lower zero simultaneously.

## 6. Audit boundary

The primary census binds the two source words, their source audit, the frozen
repair catalogue, and the static compiler helper.  The independent program
uses a different permutation/divider normal form and separately coded virtual
insertion replay to re-enumerate the complete local projection.  It then
reconstructs all 21 origin permutations without importing the producer,
deduplicates them to the three one-row relocations above, and independently
recomputes G0, capacity, maximal envelopes, upper interval-OR coverage, and
the complete static lower atlas.

Frozen artifacts:

- `scratch/k16_state2_three_gap_one_cut_split_20260730/explore_one_cut_split.py`,
  SHA-256 `6c15be7eb093346059ac3ff26b7c6b2b57ca967b018ceff0524ee2e3163f38b7`;
- `scratch/k16_state2_three_gap_one_cut_split_20260730/one_cut_split.audit.json`,
  SHA-256 `8643545dc4777b168bd7c2ef0805efda4be68a38312a22e283115f4b432e87d5`,
  payload SHA-256
  `d5c421907a0746fe25249dfbc246a7e9d939d7eb2f77f0e20dadd6d671e978e9`;
- `scratch/k16_state2_three_gap_one_cut_split_20260730/one_cut_split_survivors.tsv`,
  SHA-256 `261db1913bc5dc482bb206f11b6d17c1b21b5987caedf8d7512dd1463b49ab95`;
- `scratch/k16_state2_three_gap_one_cut_split_20260730/one_cut_split_physical_templates.tsv`,
  SHA-256 `bc878d4242f74d6cbc21c66806275a3e7b6d7e567661e38e90257e9fb27dce67`;
- `scratch/k16_state2_three_gap_one_cut_split_20260730/independent_replay_one_cut_split.py`,
  SHA-256 `626239e61e408b72a38b507a2239fe2465e82167961337b8ccba3bbf03e74526`;
- `scratch/k16_state2_three_gap_one_cut_split_20260730/independent_replay.audit.json`,
  SHA-256 `78b118608b5e860e16f777ab8840b6232b32e79201d3ef6d2ec0f506047483e1`,
  payload SHA-256
  `56ccf1de412fa56830614e6fed2441ee19dd76fea508822c6613ad4d22742b0f`.

No H100 process or solver was used; the six-port projection is a finite local
calculation.

## 7. Exact scope

This theorem covers exactly one cut in one globally oriented seven-row
collar, two intact globally oriented collars, separated split fragments,
three labelled frozen repair gaps, unchanged values, and a source-ordered
residual core.  It does not cover two or more collar cuts, same-gap
recombination or rotation of the two split fragments, arbitrary three-collar
interleavings, row-value edits, moved core segments, wider atoms, other
sources, or unrestricted K16.  The bracket remains

\[
 12873\le\nu(16)\le12874.
\]
