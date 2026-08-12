# Certified finite status for the contiguous-OR problem, k<20

> Revalidated finite frontier and direct 2026-07-25 verifier commands:
> `CURRENT_EXACT_K_LT20_FRONTIER_20260725.md`.

Let `nu(k)` denote the minimum length when only the nonzero masks are
required and every word entry is nonzero.  The original problem also asks
for zero.  Since a nonempty OR is zero only when every entry in its witness
is zero, the original minimum is exactly

\[
N(k)=\nu(k)+1.
\]

## Current table

| k | certified nonzero value/bounds `nu(k)` | original value/bounds `N(k)` | status |
|---:|---:|---:|---|
| 0 | 0 | 1 | exact |
| 1 | 1 | 2 | exact |
| 2 | 2 | 3 | exact |
| 3 | 4 | 5 | exact |
| 4 | 7 | 8 | exact |
| 5 | 12 | 13 | exact |
| 6 | 21 | 22 | exact |
| 7 | 37 | 38 | exact |
| 8 | 72 | 73 | exact |
| 9 | 128 | 129 | exact |
| 10 | 254 | 255 | exact |
| 11 | 465--477 | 466--478 | open; first unresolved case |
| 12 | 926 | 927 | exact |
| 13 | 1719--1852 | 1720--1853 | open |
| 14 | 3434--3676 | 3435--3677 | open |
| 15 | 6438--7352 | 6439--7353 | open |
| 16 | 12873--14704 | 12874--14705 | open |
| 17 | 24313--29408 | 24314--29409 | open |
| 18 | 48623--58816 | 48624--58817 | open |
| 19 | 92381--117632 | 92382--117633 | open |

The nonmonotone exact-status phenomenon is real: `k=12` is solved because a
length-926 construction meets its proved lower bound, while the best known
`k=11` construction still has length 477 against lower bound 465.  A solved
higher dimension does not project to an optimal lower-dimensional word;
deleting a coordinate can merge masks and destroy the interval certificates.

## Principal certificates

- General construction and lifts: `construct_or_array.cpp`.  The current
  arm64 binary `construct_or_array` was rebuilt from the checked-in source;
  its SHA-256 is
  `e0245be2f2e7ce86344d29af6b9d72d923eb135199801f57b61578d870ec680c`.
  On stdin `k=0,...,19` it reports the total lengths
  `1,2,3,5,8,13,22,38,73,129,255,478,927,1853,3677,7353,14705,29409,58817,117633`.
- Independent all-k verification: `construct_best_suffix_verification.log`.
- Exact lower-bound arithmetic: `ITERATED_BOUNDARY_CORE_RIGIDITY.md` and
  `scratch/check_iterated_boundary_core_rigidity.py`.
- `k=8`: `k8_optimal.txt`, `k8_length72.analysis`.
- `k=9`: `k9_optimal.txt`, `k9_length128.analysis`.
- `k=10`: `k10_optimal_nonzero.txt`, `k10_optimal_verification.txt`.
- `k=11` upper certificate: `k11_completed_477.txt`,
  `k11_completed_477_exhaustive.log`, and
  `k11_completed_477_suffix.log`.
- `k=12`: `k12_optimal_nonzero.txt`, `k12_optimal_verification.txt`.
- `k=14` upper certificate: `k14_completed_3676.txt`,
  `k14_completed_3676_exhaustive.log`, and
  `k14_completed_3676_suffix.log`.

The current exact `k=11` RunPod search ledger is
`K11_EXACT_PORTFOLIO_20260724.md`.

The newest certified local closure is
`K11_WIDE_R3_EXACT_CLOSURE_20260724.md`: 96 selected radius-three edit sets
around four distinct length-476 one-hole words are DRAT-verified impossible
for all arbitrary nonzero replacement values.  This does not change the
table bounds.

`K11_NEW_PAIR_AND_R3_FRONTIER_CERTIFICATE_20260724.md` adds 26 complete
arbitrary-two-replacement neighborhoods, comprising
12,316,281,313,700 exact position/value tuples, and 72 additional selected
radius-three cases with independently verified DRAT proofs.  It also records
a new radius-8--10 one-hole descendant.  These are local closures only, so
the `k=11` bounds remain unchanged.

The newest proof-only global equality analysis is recorded in
`K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md` and
`K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md`, with independent final audits.
It eliminates one top zero-margin slice and forces any remaining length-465
template into a one-jump Johnson flag path plus a spanning rainbow
\(J(11,5)\) forest with at most six components.  These are strict necessary
conditions but not an impossibility theorem, so the table remains
\(465\)--\(477\) at \(k=11\).

The subsequent audited notes `K11_MIDDLE_LEVELS_NEWLINE_20260724.md` and
`K11_EXTERNAL_OFFSET_CAPACITY_20260724.md` fix the full subset-completion
hierarchy, determine every coordinate's central/external extension split
from its long zero runs, and impose directed set-valued Hall capacities on
the external labels.  These are additional necessary conditions only; the
certified \(k=11\) interval remains \(465\)--\(477\).

For `k=14`, all 26 shards of the 49,920-case one-hole/two-edit common-anchor
portfolio are now DRAT-verified UNSAT; see
`K14_ONEHOLE_TWOEDIT_FULL_PORTFOLIO_CERTIFICATE_20260724.md`.  This excludes
13,398,662,234,880 root/architecture/value tuples.  The unrestricted suffix
problem remains open, so the table is unchanged.

The strictly broader delete-one/two-arbitrary-edit family is specified and
independently audited in `K14_DELETE1_TWOEDIT_NEXT_FRONTIER_20260724.md`.
It contains 6,998,640 architectures and
1,878,453,795,342,960 position/value tuples.  Checked root formulas are being
certified separately; no result from this bounded family changes the current
`k=14` table unless a verified SAT word is found.
