# The authenticated m=9 SCD forest fails the unchanged multiblock source face, and its canonical minimum residence split has 322 unserviceable rank-10 colours

Date: 2026-08-01  
Lane: H2 / K17 finite SCD multi-component carrier audit  
Status: exact independent reconstruction and scoped solver-free no-go.  This
does not exclude another phase-detachment forest, another minimum cut set, a
nonminimal split, or an interior rethread.

## 0. Verdict

The authenticated `m=9` phase-detachment model is a genuine physical forest
on all

\[
 W={17\choose9}=24310
\]

rank-nine owners.  It has `19448` edges and `Cat_9=4862` directed path
components.  It cannot, however, be used as `4862` unchanged depth-three
maximal-source blocks: exactly `1213` components fail owner reconstruction.
Their obstruction consists of `1736` strictly internal owner-coordinate
one-runs of length below four.  Exterior block ordering cannot repair such a
run, because every feasible source letter is contained in the corresponding
componentwise maximal intersection.

The exact minimum interval-stabbing repair makes `1419` internal cuts.  The
canonical right-end greedy optimum gives `6281` pieces, all of which have a
nonempty maximal depth-three source, exact owner replay, and zero strict D2
or D3 residence defect.  It preserves `18029` forest edges and deletes
`1419` pairwise-distinct lower and upper q1 colours.

This repaired face is also closed negatively.  Among all `10,022,670`
oriented two-piece seams whose concatenated maximal source replays exactly,
`322` of the deleted rank-ten colours have no provider.  Adding the strict
D3 and maximal-D2 residence tests removes no seam: all three arc sets are
identical.  A rank-ten target cannot first appear only on a longer
multi-seam interval, because every adjacent pair of distinct rank-nine
owners inside such an interval already has that same rank-ten union.
Therefore no ordering and orientation of these canonical `6281` pieces can
be an upper-complete maximal-source K17 word.

## 1. Authenticated input and independent reconstruction

The frozen inputs are

| artifact | SHA-256 |
|---|---|
| `phase_m9.winner.out` | `75946e58bea2147d3899eae3f0f99aca9ba4ea413682c938ca59534b980a687c` |
| `phase_m9.selected.tsv` | `49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de` |
| root audit stdout | `af3da9868158df3e187f859e1c1056e5a5e7c91767f1f1c7db7c8848b5dbb082` |

The Python audit does not import the encoder.  It rebuilds the increasing
Greene--Kleitman SCD on the fifteen-coordinate ground, the four-row
inclusion matching `M0`, every untouched provider, both edges of each of the
`8008` selected options, and every directed component.  It obtains

```text
owners 24310, edges 19448, components 4862, maximum component order 27,
upper q1 distinct 19448, lower q1 distinct 19448, cycles 0.
```

The component-order histogram is stored literally in the audit JSON.

## 2. Exact component maximal-source test

For one physical owner path

\[
 P=(O_0,\ldots,O_t)
\]

at depth three, define its componentwise-largest source by

\[
 K_p(P)=\bigcap_{\max(0,p-3)\le i\le\min(t,p)}O_i,
 \qquad 0\le p\le t+3.                              \tag{2.1}
\]

Every source realizing the owner rows is pointwise contained in `K(P)`.
Consequently a source exists iff every `K_p` is nonempty and

\[
 O_i=K_i\cup K_{i+1}\cup K_{i+2}\cup K_{i+3}
 \quad(0\le i\le t).                                \tag{2.2}
\]

The audit gives

| row | pass | fail |
|---|---:|---:|
| owner-only maximal source | 3649 | 1213 |
| owner + internal q1 + terminal-sink maximal common-Q | 3292 | 1570 |

There are no empty `K_p`; the `1213` owner failures are precisely the
components containing one of the `1736` strict internal positive runs of
length one, two, or three.  Reversing a component does not change this
criterion.  Adding owners outside the component only intersects more caps
into boundary letters, so it cannot restore a coordinate already missed by
(2.2).  This proves the unchanged `4862`-block face impossible before the
upper deck or generalized lower assignment is considered.

The terminal-sink row is not used as the decisive obstruction: a compiler
which omits inter-block lower seams may release all but one terminal row.

## 3. Minimum cut-to-resident decomposition

Let a strict internal positive run occupy owner indices `[s,e)` with
`e-s<4`.  A cut is an integer `c` between owners `c-1,c`.  After splitting
the path, the run is no longer strict internal iff

\[
                         c\in[s,e].                  \tag{3.1}
\]

Thus the minimum number of cuts is exactly the minimum stabbing number of
these intervals.  On a line, sorting by right endpoint and taking the next
unhit right endpoint is optimal.  Applied independently to all `4862`
components, it selects exactly `1419` cuts.  The resulting exact ledger is

```text
pieces                         6281
preserved internal edges      18029
deleted upper q1 colours       1419, all distinct
deleted lower q1 colours       1419, all distinct
missing lower q1 colours       6281
maximal-source/replay failures    0
strict D2/D3 defects              0 / 0
```

The sum of block source lengths still has the correct length after
three-letter overlap:

\[
 \sum_i(|P_i|+3)-3(6281-1)=24310+3=24313.          \tag{3.2}
\]

This is only a scalar identity; the overlaps must still be realized by one
literal common source.

With every internal q1 and one terminal-sink row imposed separately on
each new piece, `4434` pieces pass maximal common-Q and `1847` fail.  Seam
omission again means this count is diagnostic rather than the no-go used
below.

## 4. Exact arbitrary-interval upper casualties

For each path piece the audit enumerates every contiguous interval of at
least two owners and records its OR by rank.  Before the residence cuts the
internal missing bank is

| rank | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| holes | 0 | 911 | 608 | 135 | 8 | 0 | 0 | 0 |

After the canonical cuts it is

| rank | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| holes | 1419 | 2454 | 1655 | 608 | 122 | 15 | 0 | 0 |
| newly cut-generated | 1419 | 1543 | 1047 | 473 | 114 | 15 | 0 | 0 |

The rank-fifteen casualties are real and must not be dropped merely because
the first old missing bank ended at rank fourteen.

## 5. Exact oriented two-piece graph

Give every piece its two orientations.  For oriented pieces `A,B`, form the
owner word `AB`, then its maximal depth-three source by (2.1).  The arc

\[
                         A\longrightarrow B          \tag{5.1}
\]

is admitted when all maximal letters are nonempty and the four-letter OR
row is exactly `AB`.  Two stronger filters additionally require no strict
D3 run below four and no strict maximal-D2 run below three.

Exhaustive H100 CPU replay under a 900-second/4-GiB cap gives the same graph
at all three stages:

```text
oriented states                  12562
legal arcs                    10022670
zero indegree / outdegree states    0 / 0
internally viable states          12562
forced-endpoint physical pieces       0
```

Thus the pair graph has no elementary endpoint obstruction.  Its crossing
upper support is

| rank | missing | supported | zero | provider range when positive |
|---:|---:|---:|---:|---:|
|10|1419|1097|322|2--132|
|11|2454|2428|26|2--934|
|12|1655|1655|0|32--6578|
|13|608|608|0|534--20086|
|14|122|122|0|3014--49736|
|15|15|15|0|26292--107840|

The stored witness table gives one literal oriented pair and its two ray
lengths for every positive row.  An independent Python audit replays every
stored witness and exhausts every oriented endpoint pair for all `1419`
rank-ten rows, reproducing exactly `322` zero rows.

### Theorem 5.1 (rank-ten zero rows are a global obstruction)

Assume an ordering/orientation of these pieces has a literal depth-three
source.  Every consecutive pair then has a feasible source obtained by
restricting the global source.  Its two-piece maximal source also replays:
maximal letters can only add coordinates already allowed by all incident
owner rows.  Hence every seam belongs to (5.1).

Suppose a contiguous interval crossing one or more seams has OR `X` of
rank ten.  Every owner in the interval is a rank-nine subset of `X`.  At
each crossed seam the two adjacent owners are distinct, so their union has
rank at least ten and is contained in `X`; it is therefore exactly `X`.
That seam would be a two-piece provider for `X`.  The `322` zero rows have
no such seam, contradiction.  \(\square\)

This proof uses maximal-source factorability only.  The equality of the
three audited graphs shows that the D2/D3 residence filters introduce no
hidden qualification here.

## 6. Exact scope and surviving alternatives

Two negative statements are proved.

1. The authenticated forest cannot be serialized as its original `4862`
   unchanged maximal-source blocks, because `1213` blocks fail (2.2).
2. The canonical right-end greedy minimum residence split cannot be
   serialized into an upper-complete maximal-source word, because of the
   `322` rank-ten zero rows.

The result does **not** prove that every optimum `1419`-cut stabbing set has
the same zero rows.  A different minimum cut set, extra cuts within the
remaining scalar slack, a change of phase-detachment assignment, or a
genuine interior rethread may alter the endpoint bank.  The `26` rank-eleven
one-seam zeros are not promoted to a global obstruction: a rank-eleven
interval can acquire its last coordinate only after crossing more than one
seam.

The generalized lower compiler is downstream only after one of these
upper/source obstructions is escaped.  No unrestricted K17 or all-k claim
is made.

## 7. Artifacts

The final hashes are recorded in the independent audit JSON and should be
used rather than any interrupted exploratory Python one-seam run.

```text
scratch/audit_h2_k17_m9_scd_multiblock_upper_20260801.py
scratch/h2_k17_m9_multicomponent_20260801/h2_multiblock_upper.audit.json
scratch/h2_k17_m9_multicomponent_20260801/h2_residence_pieces.json
scratch/h2_k17_m9_multicomponent_20260801/h2_residence_pieces.tsv
scratch/h2_k17_m9_multicomponent_20260801/h2_postcut_upper_holes.tsv
scratch/audit_h2_k17_m9_residence_piece_pair_graph_20260801.cpp
scratch/h2_k17_m9_multicomponent_20260801/h2_residence_piece_pair_graph.audit.json
scratch/h2_k17_m9_multicomponent_20260801/h2_residence_piece_pair_graph.witnesses.tsv
scratch/verify_h2_k17_m9_residence_piece_rank10_nogo_20260801.py
scratch/h2_k17_m9_multicomponent_20260801/h2_residence_piece_rank10_nogo.independent.audit.json
```
