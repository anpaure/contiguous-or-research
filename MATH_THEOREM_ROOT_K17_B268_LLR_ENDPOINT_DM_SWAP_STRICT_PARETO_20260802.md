# K17 b268 LLR endpoint/DM swap: scoped strict-Pareto theorem

Date: 2026-08-02

## Status

This file proves one finite, static-table statement on the authenticated b268
parent.  It does **not** prove ticket-state composability or a K17 word.

The literal parent table is

```text
b268.private_h_outer_materialized.tsv
SHA256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

The supplier parent is the 438-transfer deficiency-95 table with selected and
table hashes

```text
d6dca87229b542481f4f686f851c15700939db9b952cd26ce9df3b47d19bb8f0
ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374
```

Throughout this note:

- `native phase 0` means the literal b268 owner bank in the table above;
- `transported phase 1` means the root-aligned `round047.s7.phase1` owner
  overlay, SHA
  `736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058`;
- `s7 phase 0` is the distinct transported
  `round047.s7.phase0` overlay, SHA
  `ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207`.

The s7-phase-0 marginal is retained as a separate ledger.  It is not the
native-phase-0 coordinate.

## Complete structural/first-witness catalogue

The b268 protected structural edge file has SHA
`30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89`
and contains 93,234 edges.  Exact marginal pricing gives:

| census | count |
|---|---:|
| native-phase-0 positive | 23,342 |
| transported-phase-1 positive | 25,173 |
| positive in both declared marginals | 11,893 |

For all 93,234 edges the endpoint catalogue records the first lexicographic
phase witness, the ticket/forced-outer row mask derived from the five ticket
fields and declared forced outer pairs, baseline first-witness endpoint hits,
and edge IDs touched in one frozen supplier matching.  Its SHA is

```text
5d811072d2939e9e0b6dc9ab1990ba7c7f1a0856a072d848ec1bd928f9d3ef9d
```

All 11,893 common-positive edges avoid the 7,213 protected ticket rows at
their two changed rows.  Only 4,567 also avoid those rows at the two stored
first-witness endpoints in both marginals.  A deterministic one-trial greedy
packing on this restricted first-witness face selects 174 edges; 208 is only
the row-matching upper bound on that restricted face.  Neither number is a
packing optimum for complete occurrence menus.

The catalogue is existential and first-witness-only.  Its supplier footprint
is a frozen matching-edge-ID footprint, not an exact supplier-rank delta.

## Residual-shore enumeration

The deficiency-95 parent has exact complete 6/9/4 projection data

```text
matching 16803 / 16898
deficiency 95
zero heads 80
DM shore 109 / 14
```

The exact selected materialization and Hall-neighborhood authentication give:

| bounded move class | count |
|---|---:|
| free additions | 1,453 |
| one-conflict one-for-one swaps | 8,407 |
| reciprocal 2x2 alternating cycles | 33 |

No common-positive edge has a donor in any of the 80 zero-head rows, so there
is no direct zero-head addition or one-swap donor replacement.  Of the
one-for-one swaps, 659 activate one new supplier row in the retained current
Hall shore and therefore weaken its exact lower bound from 95 to 94.

The top 96 endpoint-ranked one-swaps were materialized and replayed through a
fresh complete supplier projection.  Their exact deficiencies are:

| exact deficiency | candidates |
|---|---:|
| 94 | 55 |
| 95 | 32 |
| 96 | 7 |
| 97 | 2 |

Every one of the 55 exact deficiency-94 tables was then repriced across all
7,395 short roles in native phase 0, s7 phase 0, and transported phase 1.
This is a bounded portfolio computation, not a global optimization over all
11,893-edge matchings.

## Scoped strict-Pareto theorem

Let `T95` be the deficiency-95 parent above.  Remove global common edge 38,682
and add global common edge 46,720.  Both use LMR row 16,006, so the table
changes only LR rows 14,133 and 15,981 and retains 438 transfers.

Then the resulting table `T94e` has:

| coordinate | `T95` | `T94e` | change |
|---|---:|---:|---:|
| native phase 0 positive | 3,098 | 3,100 | +2 |
| transported phase 1 positive | 2,253 | 2,254 | +1 |
| positive in both declared marginals | 1,839 | 1,840 | +1 |
| positive in either declared marginal | 3,512 | 3,514 | +2 |
| supplier matching rank | 16,803 | 16,804 | +1 |
| supplier deficiency | 95 | 94 | -1 |

Thus `T94e` strictly improves every displayed socket and supplier coordinate
relative to `T95`.

The exact supplier replay for `T94e` is

```text
projection edges 74126
matching 16804 / 16898
deficiency 94
zero heads 80
DM shore 107 / 13
graph FNV64 b0c93881804b04a9
```

The separate s7-phase-0 ledger is

| coordinate | `T95` | `T94e` | change |
|---|---:|---:|---:|
| s7 phase 0 positive | 2,170 | 2,171 | +1 |
| s7 phase 0 AND transported phase 1 | 1,767 | 1,768 | +1 |
| s7 phase 0 OR transported phase 1 | 2,656 | 2,657 | +1 |

The 3,100 and 2,171 counts are different marginals on different owner banks;
they are not contradictory.

Relative to literal b268 baseline

```text
(native p0, transported p1, both, either, supplier rank)
= (2687, 1891, 1422, 3156, 16796),
```

`T94e` gains `(+413,+363,+418,+358,+8)`.

Within the exactly repriced 55-table deficiency-94 portfolio, `T94e` is
lexicographically best for `(both, either, native p0, transported p1)`.
This is the only optimization claim made here.

## Exact edge and footprint ledger

The removed and added edges are

```text
38682: LR 14133, LMR 16006,
       upper/lower/middle/receiver/LLR-root
       71701/71696/79928/79992/71773

46720: LR 15981, LMR 16006,
       upper/lower/middle/receiver/LLR-root
       79889/71696/79928/79992/79923
```

Their stored first witnesses agree in both declared marginals:

```text
q=7, alpha=0, beta=0, predecessor row 16201, successor row 14179.
```

Both changed-row and first-witness endpoint ticket masks are zero.  The added
edge is canonical-eligible and has zero baseline first-witness hits.  This is
only a certificate about the stored witnesses; alternative occurrence menus
were not catalogued.

After exact simultaneous repricing, 407 of the 438 selected new-MR rows are
positive in both declared marginals and 413 are positive in at least one.
Therefore the 438 prospective common flags are not treated as simultaneous
successes.

## Ticket-row identity

The literal ticket bank has SHA
`d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1`
and the exact census

```text
1748 tickets
1748 short rows
3496 host rows
3495 nonnegative token rows
7213 rows in their union
```

An exact canonical-TSV comparison finds 876 rows changed between b268 and
`T94e`, two rows changed between `T95` and `T94e`, and zero changed rows in
the 7,213-row ticket union in either comparison.

This proves row identity only.  It does not replay the tickets on `T94e`,
choose one occurrence-labelled state shared by both marginals, or extend the
residual outer matching.

## Frozen artifacts

Local bundle:

```text
scratch/root_k17_llr_transfer_price_20260802/
  b268_dm_activation_438_v1/final_rank3_def94/
```

The bundle manifest SHA is
`95e27c514e4cc223638d20c0b6091e90630ffff58615d1aa3fddb6b31745a279`.
Key artifact hashes are:

```text
4d42944fb6de35e2d44c3c0848e4686f35ca501d752089f383593d141b98a1dd  winner.selected.tsv
0bfe5a85d4d13416938e45dcd06a940a7d5ebfbc4c781e8ff3ffbf137aea2491  winner.table.tsv
882cfb0d74d49db653f48d52c7db971072bd3505e7126ad4e4b4353bd62ba3bb  winner.projection.audit.json
cb1c146beaddedf72d71a4579ca531207b021e2c1ae56ed47e561f2792b976b4  winner.native_phase0.tsv
437715cd7c5b38e99c400ea9973ed38a19de59dff0efa01b1feff9d715108cba  winner.transported_phase1.tsv
c7401e7441a7d6407660cbd7fa7917035f5952824a48d38d7d2f68324ff5e1e4  winner.s7_phase0.tsv
5a19c9ba039a0da2f2a72c0c2bc03c55163efa6ff6849cc70d2e5f12fbc4f951  winner.ticket_row_identity.audit.json
```

The corrected endpoint-catalogue audit has SHA
`675e3a551e852fb4886d898ae197cdf50ca13d632e4c5bf7b504e8e7b4b3845b`.

H100 bundle:

```text
/home/amodo/or15/work/root_k17_llr_transfer_price_20260802/
  b268_dm_activation_438_v1/
```

## Explicit nonclaims

This theorem does not claim:

- global optimality among the 659 Hall-activating swaps, all 8,407 one-swaps,
  or all 11,893 common-positive edges;
- completeness of endpoint witness menus or simultaneous endpoint packing;
- a selected-parent supplier graph or residual outer perfect matching;
- literal ticket replay, private-bank composability, or a shared state across
  native phase 0 and transported phase 1;
- transported phase 1 as an opened common carrier phase;
- chronology, residence, arbitrary upper shadows, common cap, compiler, or a
  K17 word.

The earlier 34,757-edge warm47 experiment remains calibration only because
its ticket-row reservation was across mismatched parents.  Its 219-transfer
gain is not imported into this theorem.

At the time of this freeze, a separate authoritative root-clean radius chain
had reached supplier deficiency 90 with socket tuple
`(3099,2255,1840,3514)`.  Therefore `T94e` is not asserted to be the current
global supplier incumbent.
