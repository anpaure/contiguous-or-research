# k=15: exact DM-compression router descent to Hall 20

Date: 2026-07-28

## Result

There is now an exact carrier chain

\[
H21 \longrightarrow H21_{\rm compressed} \longrightarrow H20
\]

given by the two segment braids

\[
\operatorname{RF}(1510,5017,6136),\qquad
\operatorname{RF}(885,1393,3668).
\]

This is a Hall/compiler improvement, not yet a universal word of length
6438.  The final carrier still has Hall deficiency 20 and six degree-zero
lower targets.

## Frozen certificates

| state | file | SHA-256 |
|---|---|---|
| canonical H21 | `scratch/k15_segment_braid_hall21_zero6.json` | `8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447` |
| compressed H21 | `scratch/k15_segment_braid_hall21_compressed_dm702.json` | `ea5259c4bb8a15444da135f7c6369e11fbc059f322c570fd3db2e6b8509af337` |
| H20 | `scratch/k15_segment_braid_hall20_zero6.json` | `9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1` |

All three are exact permutations of the 6,435 rank-eight masks, Johnson
paths, and depth-three resident.  Their audited statistics are:

| state | matching | deficiency | zero | DM left/right | lower holes q1..q7 | upper holes q1..q7 |
|---|---:|---:|---:|---:|---|---|
| H21 | 16,362 | 21 | 6 | 846/825 | 4,18,9,1,0,0,0 | all zero |
| compressed H21 | 16,362 | 21 | 6 | 702/681 | 4,18,11,1,0,0,0 | all zero |
| H20 | 16,363 | 20 | 6 | 677/657 | 4,18,11,1,0,0,0 | all zero |

The neutral router pays two additional native q3 holes, but it preserves q1,
q2, q4..q7 and the entire upper tower.  The improving move changes no shadow
support count.

## Exact component mechanism

Every deficient component in all three states is a gap-one rooted native
basis: if its target set is `L`, its native physical traces are precisely
`L \ {root}`, where `root` is the intersection of all targets in the
component.

The neutral move changes exactly one abstract component:

\[
(169,168)_{\text{root }1920}
\quad\longmapsto\quad
(25,24)_{\text{root }1801}.
\]

The other twenty component target sets remain identical.  This explains the
DM compression

\[
846/825\longmapsto702/681.
\]

The second braid then removes the entire 25/24 component rooted at 1801; the
other twenty components again remain identical:

\[
702/681\longmapsto677/657,qquad H21\longmapsto H20.
\]

For root 1801, the old native basis has 24 pins and axes

\[
\{1,2,5,6,12,13,14\}.
\]

On that target block, the final neighbourhood has 25 cells and exact matching
rank 25.  Twenty-three restricted cell-shore profiles are common.  The only
profile change is

\[
\{1801,1803,1833,1835\}
\longmapsto
\{1801,1833\}\sqcup\{1803,1835\}.
\]

The native trace 1801 remains absent and trace 1833 is duplicated, but the
two refined shores make the full 25-by-25 block matchable.  This is why raw
trace coverage alone would miss the Hall gain.

## Contraction audit

The first braid changes 29 of 19,311 cell-shore profiles.  Its contracted
boundary ranks are 24/24, so it is exactly neutral.  The second changes 32
profiles and has contracted boundary ranks 17/18, giving the one-unit rank
gain.

The cross-gap matrix for the three canonical DM shores against the three
graphs is

\[
\begin{pmatrix}
21&20&20\\
20&21&20\\
20&20&20
\end{pmatrix}.
\]

Thus the neutral state has not reduced the deficiency yet; it has replaced a
large obstruction by a small obstruction which one subsequent local braid
can discharge.

## Search consequence

This compression criterion was prospectively predictive.  Among all 687
nonidentity H21-neutral states, candidate 0575 is the unique extreme:

\[
|DM_L|=702,
\]

while the next two have 814 and the median is 846.  Exact second-neighbourhood
scans of the five best compression-ranked states found an H20 move only from
candidate 0575.

Compression is not a logically necessary condition: a distinct H22 neutral
state, candidate 0180, reaches another H21 endpoint without compressing its
first-state shore.  That endpoint has the same 21 abstract rooted components
as canonical H21 but a different physical pin embedding; its complete direct
one-braid scan does not reach H20.  Therefore DM compression should rank the
beam, not prune all noncompressed states.

## Verification

- `scratch/audit_k15_h21_h20_compression_descent.json` is the generic
  segment-braid descent audit.
- `scratch/audit_k15_h21_h20_compression_theorem.py` checks the hashes,
  materialization, all state invariants, component replacement, rooted native
  bases, contraction ranks, cross-gap matrix and the root-1801 discharge.
- `scratch/audit_k15_h21_h20_compression_theorem.json` is its full output.

The natural next experiment is the identical neutral-state DM census at H20,
followed by exhaustive second-neighbourhood scans in compression order.
