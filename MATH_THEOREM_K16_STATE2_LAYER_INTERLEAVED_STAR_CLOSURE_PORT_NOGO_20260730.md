# K16 state2 layer-interleaved star: closure-port obstruction

## Statement

Fix either authenticated state2 root

| case | target SHA-256 | blocker | first flat | star centers |
|---|---|---:|---:|---|
| 0 | `762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407` | `0x1639` | 1102 | 6, 1058, 2167, 4387, 10966, 11032, 11287, 11366, 12199 |
| 1 | `1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8` | `0x1879` | 2031 | 617, 1987, 4025, 5316, 6061, 10681, 11190, 12387, 12768 |

Choose an ordered triple of distinct star centers and an independent
orientation for each strand.  Delete the three source collars

\[
 C_p=[p-3,p+3]
\]

and insert their 21 rows, interleaved layer by layer as in the authenticated
source `scratch/search_k16_buffered_facet_star_braid_20260730.cpp`, as one
contiguous block at one core gap.  No such chronology has an exact middle
carrier.  This holds for every valid insertion gap, hence in particular for
every host-cell insertion tested by that source.

The exact enumerated fibre has

\[
 9P3\,2^3=504\cdot8=4032
\]

representations per root, 8064 for each fixed insertion gap.

This is a source-relative no-go for the single-block layer-interleaved
collar fibre.  It is not an unrestricted K16 no-go, does not cover multiple
inserted blocks, and does not cover the distinct outward-arm semantics.

## Local closure calculation

Deleting `C_p` while retaining source order creates the directed core seam

\[
 Q_{p-4}\longrightarrow Q_{p+4}.
\]

The audit explicitly checks `Q_{p-4} != Q_{p+4}` for all 18 centers, so none
of these deletion closures creates a new flat.

All relevant collars are disjoint from the three flats.  Their actual local
depth is therefore constant: depth 3 before the first flat and depth 2 after
it.  In a constant-depth neighborhood,

\[
 E_c=\bigwedge_{j=0}^{d}Q_{c-j},\qquad
 R_r=\bigvee_{c=r}^{r+d}E_c.
\]

The independent audit evaluates these identities literally after compressing
out `C_p`.  The following nonzero losses certify `R_r != Q_r`; every gain is
zero.

| case | center | actual depth | failing row relative to right seam row | `Q_r & ~R_r` |
|---:|---:|---:|---:|---:|
| 0 | 6 | 3 | 0 | `0x4010` |
| 0 | 1058 | 3 | 0 | `0x4210` |
| 0 | 2167 | 2 | 0 | `0x0204` |
| 0 | 4387 | 2 | 0 | `0x0200` |
| 0 | 10966 | 2 | 0 | `0x4008` |
| 0 | 11032 | 2 | 0 | `0x0004` |
| 0 | 11287 | 2 | 0 | `0x0002` |
| 0 | 11366 | 2 | 0 | `0x0300` |
| 0 | 12199 | 2 | 0 | `0x0080` |
| 1 | 617 | 3 | 0 | `0x4081` |
| 1 | 1987 | 3 | 0 | `0x4200` |
| 1 | 4025 | 2 | 0 | `0x1000` |
| 1 | 5316 | 2 | 0 | `0x0010` |
| 1 | 6061 | 2 | -1 | `0x0800` |
| 1 | 10681 | 2 | 0 | `0x0008` |
| 1 | 11190 | 2 | 0 | `0x0028` |
| 1 | 12387 | 2 | 0 | `0x1800` |
| 1 | 12768 | 2 | 0 | `0x0001` |

The flexible-depth cross-check has exactly one compatible counterphase:
case 1, center 617 passes at depth 2.  Its actual phase is depth 3, so it is
not an escape.  Case 0 has no depth-2-or-3 compatible center; every other
case-1 center fails at both depths.

## Directed repair ports

For a canonical failing row `r`, its complete dependency support is

\[
 [r-d,r+d]
\]

in compressed-core row coordinates.  An inserted block outside the internal
gaps of this interval only translates the support and leaves the failure
byte-for-byte unchanged.  The audit therefore places a conservative directed
edge

\[
 \text{insertion gap}\longrightarrow\text{closure }p
\]

for each internal support gap.  These are possible-influence edges, not a
claim that insertion actually repairs the closure.

For a selected center `p`, if `m` selected collars lie below it, the closure
gap in the 21-row-deleted core is exactly

\[
 g(p)=p-3-7m.
\]

The audit exhausts all `2*C(9,3)=168` unordered collar sets.  Ordered strand
labels and the eight orientations do not alter these ports.  The exact
separation ledger is:

| case | flexible-compatible centers | minimum center separation | minimum compacted closure-gap separation | minimum repair-port separation | maximum closures influenced by one gap | minimum untouched failures |
|---:|---|---:|---:|---:|---:|---:|
| 0 | none | 66 | 59 | 56 | 1 | 2 |
| 1 | 617 at counterphase depth 2 only | 381 | 374 | 371 | 1 | 2 |

Thus the three possible-influence port sets are disjoint for every center
triple.  One contiguous insertion can alter at most one canonical witness;
at least two exact local carrier failures persist.

Finally, all 21 moved rows are globally unique, no collar meets a flat, and
all 18 retained closure endpoint pairs are unequal.
Consequently neither the interleaved block nor either block/core join creates
a new flat.  If insertion splits an original flat, G0 has only two flats and
already fails.  Otherwise the original flat order and the actual depth phases
used above remain unchanged.  This closes every insertion position.

## Independent audit and catalogues

The checker is structurally separate from the production C++ enumerator.  It
authenticates both words and envelopes, replays the complete roots, derives
all 18 local losses, and exhausts all 168 closure-port triples.

- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/audit_k16_state2_layer_interleaved_closure_obstruction_20260730.py`
  SHA-256 `fa9a0d2b81930756cc79ace0dcfba4a7fa9b4c975dd2ab31765bac0cfda34ea4`.
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/independent.audit.json`
  SHA-256 `332a9cb257ea4a80ffaf40097f851a22eeb787775976783af86ba9c3e3cfbd4d`,
  payload SHA-256 `32d196d894bb8818b67ba9593e45dfdb496100ae9b2645c33b53cd075114da6d`.
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/closure_catalogue.tsv`
  SHA-256 `b3c24ae420775250fe2e1d001a2ee86e38ac4c2fb3ff50da5492e91059e7751b`.
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/triple_port_catalogue.tsv`
  SHA-256 `333e320875547ece1112bfdd4b5b305268cff946b140dbabbdbe5bb614ebd7fb`.
- `scratch/k16_state2_layer_interleaved_closure_obstruction_20260730/directed_repair_ports.tsv`
  SHA-256 `017e5f50c984e2c7ac3e66df8ba3f1793dbecf7678676b03863112d07ba55f04`.

The authenticated weave source has SHA-256
`12d8b4d704f2c0ee1dcb5db0eafb8b3b9c0ef0b2a02ba305342108ed7ef97587`;
the frozen input audit has SHA-256
`a189324d549d1e4caa6f6cb2b070ee30dd62df578177b76b9962180ee1f2d233`
and payload SHA-256
`b6da8299168dd81ca9cb2d28607785ad6f4731d9f07d2eb75a146cb108d19514`.
