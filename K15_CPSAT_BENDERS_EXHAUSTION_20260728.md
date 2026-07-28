# k=15 CP-SAT Hall-cut exhaustion (2026-07-28)

## Exact model

`scratch/search_k15_segment_dm_order_cpsat.py` represents a segmented carrier
as one optional-node circuit:

- exactly one orientation is selected for every component;
- selected oriented components form one Hamilton path through a dummy node;
- every seam is residence-safe;
- every upper colour lost by cutting the source is restored by a selected seam;
- every failed exact compiler matching contributes its canonical
  Dulmage--Mendelsohn inequality

  `fixed(A) + sum_e contribution_A(e) x_e >= |A|`.

The inequality is exact because the compiler-cell signature multiset is the
sum of component-intrinsic signatures and selected-seam signatures.  Every
decoded chronology is independently checked for residence, the structural
identity, all upper ranks, and exact Hall deficiency before use.

Remote invocation uses the CPU only:

```sh
PYTHONPATH=/dev/shm/orlib python3 search_k15_segment_dm_order_cpsat.py ...
```

OR-Tools is installed under `/dev/shm/orlib`; no GPU code is involved.

## Regression

The CP-SAT model reproduces the prior Kissat results exactly:

- targeted N32: Hall 30, one DM cut, infeasible;
- targeted N46: Hall 30, one DM cut, infeasible;
- DM-designed N96: the source Hall-30 cut is feasible, the resulting
  chronology has Hall 140, and the two-witness system is infeasible.

The N96 result replaces a 600-second Kissat `UNKNOWN` with an exact closure in
well under ten seconds including Python signature evaluation.

## Exhaustion of the 256 native segmentations

`scratch/run_k15_cpsat_benders_batch.py` screened all 256 distinct native
segmentations in `cpp_diverse/ranked.tsv` (64 each at N32, N46, N64, N96).

Exact result:

| quantity | result |
|---|---:|
| segmentations | 256 |
| `BENDERS_INFEASIBLE` | 256 |
| best Hall deficiency | 30 in all 256 |
| best zero candidates | 7 in all 256 |
| DM cuts before infeasibility | 1 in all 256 |
| aggregate process-seconds | 727.08 |
| maximum process time | 3.79 s |

Thus none of these 256 component/orientation/seam graphs can even satisfy the
canonical Hall-30 witness.  This is a complete statement about the fixed
segmentations, not a heuristic sample of their chronologies.

## Larger locality-safe segmentations

All components below have length at least 12, so the same additive compiler
decomposition applies.

| components | outcome | cuts | alternate Hall deficiencies |
|---:|---|---:|---|
| 128 | exact infeasible | 1 | none |
| 160 | exact infeasible | 1 | none |
| 192 | exact infeasible | 3 | 289, 136 |
| 256 | unknown after 180 s on the fourth solve | 3 | 240, 254 |
| 320 | unknown after 180 s on the fifth solve | 4 | 277, 428, 202 |

No decoded chronology had Hall deficiency below 30.  Larger segmentations do
cross the first witness, but the defect relocates into large, different DM
blocks.

## Palette corridors and exact-zero roots

On the DM-designed N96 segmentation:

- preserving all but 4 or 8 newly cut source q1 colours is infeasible after
  the first DM cut;
- q1 caps 12, 16, and 24 are infeasible after two or three DM cuts;
- the joint `(q1,q2,q3)=(16,20,8)` corridor is infeasible after two cuts.

Assumption-core audits show that generation is presently the bottleneck:

- canonical exact-zero N46/N64/N96 segmentations have one- or two-root cores
  even after roots with no physical candidate arc are omitted;
- the rich native N96 `n96_s12014` is Hamilton-compatible with all three roots
  it exposes (`5801,10794,21588`), but the remaining four Hall-zero roots have
  no candidate seam.

## Consequence

The search has not solved k=15: the certified incumbent remains Hall 30.
What has changed is that fixed reordering/reversal uncertainty has largely
been removed.  The next search must generate genuinely new resident,
all-upper carrier material (or mix carriers), rather than spend more time on
ordering the same segment families.
