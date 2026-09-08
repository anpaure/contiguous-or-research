# `j=3959`: fixed universal-star boundary outer no-go and exterior-`2665` repair catalogue

Date: 2026-07-30

Status: **PASS solver-free scoped no-go; alternative outer boundaries remain
open**.

This note completes the outer-embedding gate left open in handoff item 2045.
It applies to the authenticated `j=3959` chronology and to the proposed lift
which combines an authenticated upper-service block with the consecutive
right-boundary rows

```text
D=4d39, R0=0767, R1=076d, R2=027f.
```

The conclusion is deliberately source-relative.  It rules out this literal
boundary for all 2,250 depth-three-surviving service blocks.  It does not rule
out those blocks with a different or buffered boundary, another Hall lift,
another parent/layout, or an unrestricted K16 construction.

## 1. The missing outer-row condition

Item 2045 correctly observes that, at depth two, the two right-straddling
envelopes

```text
D & R0 & R1 = 0521,
R0 & R1 & R2 = 0265
```

are nonzero and have union `0765`.  They therefore form an exact local cell
for the star leaf `0765`.  This cell test, however, does not reconstruct the
target row `R0=0767`.

### Theorem 1 (isolated-bit obstruction)

Let three consecutive, pairwise nonflat target rows be `D,R0,R1` at a common
positive compiler depth.  If a bit belongs to `R0` and to neither `D` nor
`R1`, then no source envelope covering `R0` carries that bit.  Consequently
`R0` cannot replay exactly.

**Proof.**  Let `R0` start at target index `i`, and let the common positive
depth be `d`.  At the first source position `p=i`, the preceding row `D`
covers `p`, so its missing bit kills the bit in the envelope.  At every other
source position `i+1 <= p <= i+d`, the successor `R1` covers `p`; its missing
bit again kills the bit.  Thus the bit occurs in none of the envelopes whose
union must reconstruct `R0`.  Distinct adjacent rows create no flat, so the
depth does not change between these three rows.  ∎

For the frozen boundary, take the bit `b=0002`.  Its membership trace on

```text
4d39,0767,076d
```

is exactly `0,1,0`.  Hence Theorem 1 applies at every positive depth.  At the
advertised depth two, even maximizing the unspecified predecessor gives the
three upper envelopes

```text
0521, 0521, 0265,
```

whose union is only `0765`.  With the actual preceding block row `W=4e39`,
the exact three envelopes are smaller:

```text
W & D & R0 = 0421,
D & R0 & R1 = 0521,
R0 & R1 & R2 = 0265.
```

Their union is again `0765`, and the missing part of `R0` is exactly `0002`.
The globally reversed adjacency has the same two zero neighbours and is
equally impossible.

This does not invalidate the local `0765` Hall cell from item 2045.  It shows
that the surrounding target-row chronology needed to realize that cell is
not a physical compiler chronology.

## 2. Exhaustion of the 2,250-block face

The independent audit authenticates the frozen service-block catalogue and
regenerates its exact depth-three projection without importing the prior
survivor list:

```text
34,560 raw blocks
 -> 5,166 internally depth-two-resident blocks
 -> 2,250 depth-three middle-reconstruction/run-residence survivors.
```

The two independently computed 2,250-member survivor lists agree in source
order.  Every member has the same terminal block rows `W=4e39,D=4d39`, and
the proposed universal suffix fixes `R0,R1,R2`.  The obstruction in Theorem 1
is independent of the first four block rows, predecessor choices, source
occurrences, and exterior anchors.  Therefore the exact cascade is

```text
depth-three block survivors                       2250
fixed-boundary exact-middle survivors                0
occurrence-disjoint physical placements              0
placements retaining all five upper witnesses        0
placements entering the nine-target/full Hall audit   0.
```

The upper-five and lower-Hall stages are empty-domain consequences, not
separate Hall failures.  In particular, this theorem does not claim that the
2,250 blocks fail the lower compiler under other outer embeddings.

## 3. Exterior `P=2665` normal form

Although no `P` anchor can repair the already-failed boundary, a separate
exact catalogue identifies the smallest replacement topology.

At constant depth two, a shortest nonflat length-two `P` cell has the six-row
normal form

```text
L, T0, P+x, P+y, T3, R,
```

where `x,y` are distinct singleton bits outside the rank-seven mask `P` and

```text
x is contained in L and T0,
y is contained in T3 and R,
P is contained in T0 | T3.
```

Indeed the two cell envelopes are `P&T0` and `P&T3`; the displayed conditions
make their union exactly `P`, while the outer occurrences of `x` and `y`
replay the two central rank-eight rows.  A nonflat length-one `P` cell is
impossible: exact replay of its central rank-eight extra bit forces an
adjacent equal row, hence a flat.

In the authenticated source there are exactly nine rank-eight supersets
`P+one bit`, giving 13 oriented left ports and 13 oriented right ports.
Literal occurrence-disjoint joining leaves exactly 130 valid six-row ports;
60 avoid all six old-star source halos.

If one nevertheless retains the tail `(L,T0)=(076d,027f)`, its common extra
bit forces

```text
x=0008,  T1=266d,
```

and `266d` has the unique source occurrence 5859.  Exactly seven right ports
are occurrence-disjoint; five also avoid every old-star halo.  Their source
triples are

```text
542,543,544
542,541,540
3751,3752,3753
5602,5603,5604
6389,6388,6387.
```

These five rows are a proof-safe repair catalogue only.  None is a candidate
for the fixed universal-boundary branch, because `R0=0767` has already failed
middle replay.

For additional context, the full frozen geometry has 34 cells whose envelope
misses exactly one bit of `2665`; 28 are exterior to the old nine-target
shore and 26 avoid every old-star halo.  Their minimum blocker histogram is
`8,7,6,5` at blocker counts `1,2,3,4`, and exhaustive full-geometry one-row
replacement leaves exactly four local `2665` lifts.  These counts diagnose
the next changed-boundary search; they are not universal-word certificates.

## 4. Frozen audits

Primary exterior-`P` catalogue and literal fixed-boundary audit:

```text
scratch/audit_k16_j3959_p_anchor_boundary_catalogue_20260730.py
  SHA 918ac06ccf8bf327f95c1541ff64909874150c6002f395e8d46d1e44059ab6ff
scratch/k16_j3959_p_anchor_boundary_catalogue_20260730.audit.json
  SHA e49e5ccb24dbba7e993f6d008cbd7d82eac4d575f33d510dd5c9e9942fc01503
  payload b8f4c88da5423d647d3c14e9888932be796c80b5181d6bf22fb42c34c965ba4a
scratch/k16_j3959_p_anchor_boundary_catalogue_20260730.tsv
  SHA 7f141f2dc4b624a457b4307097321b0f3316eb2ac1590451c212a43a01cd89f0
```

Independent 2,250-block regeneration and fixed-boundary replay:

```text
scratch/audit_k16_j3959_universal_star_boundary_outer_nogo_20260730.py
  SHA 725a3635a4f6f1b2cd41cfe55113d48011acb72fea33f9cfef943412b0edc7f5
scratch/k16_j3959_universal_star_boundary_outer_nogo_20260730.audit.json
  SHA 1dc351852e8359289630d0429bfd61358b32dc47063ed59ef02e15e593a4c1f3
  payload 4a29b576b240f7590ad297b57f101912a3edabfd0b000ff7225f159b5462a98f
```

Authenticated source chronology:

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
  SHA edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
```

Both audit programs replay locally and require no SAT/CP solver.  The second
program verifies byte-for-byte equality with its frozen JSON.  No heavy Mac
or H100 computation was used because the solver-free row obstruction empties
the requested face before placement enumeration.

## 5. Exact surviving scope

The smallest useful next search must change the topology which created the
isolated `0002` run.  It may replace one of `D,R0,R1`, insert a buffer between
them, create a longer `0002` run, or use a different physical star leaf.  The
130-port/60-halo-safe `2665` catalogue can then be joined to a replayable
star boundary before any upper-five or full Hall audit.  Nothing in this note
is an unrestricted K16 no-go.
