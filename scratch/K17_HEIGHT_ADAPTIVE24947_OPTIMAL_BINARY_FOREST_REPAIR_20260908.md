# Universal 24,947-word from an optimal fixed-hole binary-forest repair

Date: 2026-09-08. Status: exact finite construction and verification passed.

Keep the previously verified height-adaptive 24,829-letter prefix unchanged.
Its 128 missing targets can be covered by an explicit 118-letter repair,
giving a universal word of length 24,947. All 131,071 nonempty targets have
ordinary interval witnesses, independently replayed by a segment-tree OR
calculation. Thus the established lower bound and this word give

    24,313 <= nu(17) <= 24,947.

The repair length 118 is optimal within the precisely specified binary-forest
model below. Neither this repair nor the complete 24,947-word is claimed
optimal among unrestricted OR words. The fixed prefix, cycle openings,
cycle ordering, and all its letters are unchanged; no deletion or cut search
is used.

## 1. Fixed input and the binary-forest model

The input is `k17_height_trimmed24829.word` from
`K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md`.
Its complete missing-target set H is recorded in
`k17_height_adaptive_20260908/height_adaptive_fixed_certificate.json`.
It has 128 members: 65 of rank ten, 49 of rank eleven, and 14 of rank twelve.

Every vertex of the repair forest is one of these 128 targets, used once.
A vertex P can be internal only if it selects one pair of distinct children
A,B in H with

    A union B=P, |A|<|P|, |B|<|P|.

Each parent chooses at most one pair. Each child belongs to at most one
parent. A target may itself have both a parent and children. Strictly
decreasing ranks rule out directed cycles, so the selected pairs define a
forest on H. All vertices without parents are roots, including every
unselected target that is not another target's child.

Emit the leaves of each tree in depth-first order, taking the smaller
integer child first and taking roots in increasing integer order. The
leaves below a vertex occupy one contiguous block. Induction up the tree
shows that their union is exactly that vertex. Consequently this literal
leaf word covers every target in H by an ordinary interval. Concatenating
it to the unchanged prefix therefore gives a universal word.

If I vertices are internal, there are 128-I leaves, because each of the
128 vertices is either internal or a leaf. Thus each chosen internal
vertex saves exactly one repair letter compared with listing H directly.

## 2. Exhaustive candidate count and exact optimality bound

One bounded h100 census tested every unordered pair of distinct targets
in H. It retained a pair precisely when its union is a strictly larger
target in H. There are exactly 56 retained pairs, grouped by ranks as
follows; the children in the table retain increasing integer-mask order.

| Parent rank | Child ranks | Number of candidates |
|---:|:---|---:|
| 11 | 10,10 | 7 |
| 12 | 10,10 | 26 |
| 12 | 11,10 | 19 |
| 12 | 11,11 | 4 |

Only ten different targets can be parents in any such pair:

    14267,15291,15743,15855,15863,15867,
    73087,73151,73207,73211.

Two have rank eleven and eight have rank twelve. Therefore every forest
in this model has I<=10 and requires at least 128-10=118 repair letters.
This is an exact finite combinatorial upper bound on savings, independent
of an optimization solver's numerical status.

## 3. The ten simultaneously compatible pairs

The following choices attain all ten eligible parents:

| Parent P | Child A | Child B |
|---:|---:|---:|
| 14267 | 14011 | 14251 |
| 15291 | 7099 | 11195 |
| 15743 | 3455 | 13691 |
| 15855 | 7663 | 13679 |
| 15863 | 3575 | 13783 |
| 15867 | 11755 | 13787 |
| 73087 | 7551 | 68991 |
| 73151 | 7615 | 69055 |
| 73207 | 7671 | 69111 |
| 73211 | 7675 | 69115 |

Every row is checked by exact integer OR. All twenty child targets are
distinct and no parent is assigned twice. In this particular solution no
parent is itself a child: the ten displayed pairs form ten two-leaf trees,
and the other 98 vertices form singleton-root trees. Their leaf word has
20+98=118 letters. These choices attain the upper bound I<=10 and prove
optimality within the stated forest model.

The full 118-mask leaf sequence, the sorted roots, all selected pairs, and
an exact repair-subword witness for every one of the 128 targets are saved
in the certificate. Each repair witness was also rechecked in the full
word after adding the prefix offset 24,829.

## 4. One bounded optimization, followed by exact checking

After inspecting the census of 56 candidates, one single-thread MILP was
run, with a 30-second limit. It has one binary variable per candidate pair.
For each target, one constraint permits at most one selected pair with
that target as parent; a separate constraint permits at most one selected
pair using that target as child. Maximizing the sum of variables therefore
maximizes I in exactly the model of Section 1.

HiGHS returned ten pairs, status optimal, zero reported gap, and one search
node. The chosen triples were independently checked with exact integers
against every parent/child constraint and every union/rank condition.
The exact upper bound in Section 2 and the exact feasible table in Section 3
are the optimality certificate; floating-point solver output is not a
premise of the mathematical optimality claim.

No larger target catalogue, unrestricted leaf alphabet, alternative prefix,
cross-root repair optimization, interval-deletion heuristic, or alternative
cycle cut was considered. Such changes lie outside the proved 118 lower
bound and could in principle give a shorter repair.

## 5. The literal universal word and its complete verification

The resulting word is

    fixed_prefix24829 + binary_forest_repair118,

with exact length 24,947 and SHA-256

    a358c7d539ea8af286c61a45f621b7d9bc1227c292829ea3bb981acd1f975389.

Every letter is a nonzero mask within the 17 coordinates. The prefix is
retained literally. Every original prefix witness therefore survives, and
the 128 old holes all have tree witnesses in the repair.

A complete suffix-OR enumeration additionally records one nonwrapping
interval for every target from 1 through 131071. A separately constructed
segment tree replays every one of these 131,071 range ORs exactly. It also
replays all 128 explicit forest witnesses. All checks pass, with zero
missing targets.

This improves the previous verified 24,957-word by ten letters and leaves
a gap of 634 above the endpoint lower bound. It is a concrete finite
construction result, independent of whether the general height-adaptive
asymptotic proof or the earlier quantitative PBBS proof is accepted.

## 6. Exact artifacts and execution scope

All output files are in

    scratch/k17_height_adaptive_20260908/binary_forest_repair/.

They are:

* `binary_forest_candidate_catalogue.json`: all 128 input holes and all
  56 possible strict binary decompositions, with the candidate census.
* `binary_forest_repair_certificate.json`: selected forest, exact upper
  bound, leaf sequence, every hole witness, solver record, full coverage
  report, and checksum.
* `binary_forest_repair_suffix.word`: the 118-letter repair.
* `k17_height_forest24947.word`: the full universal word.
* `k17_height_forest24947_target_witnesses.json`: all 131,071 ordinary
  interval witnesses, with zero-based inclusive endpoints.

The exact scripts are

    scratch/census_k17_height128_binary_forest_candidates_20260908.py
    scratch/optimize_k17_height128_binary_forest_repair_20260908.py.

Both mathematical executions ran only on h100, using
`/home/amodo/exact-b-k17-height-adaptive-20260908/binary_forest_repair/`
for their output. Each process had limits of 90 CPU seconds, 110 wall
seconds, and 1 GiB address space; the sole MILP had its additional
30-second, single-thread limit. The census and the construction/checking
run both completed successfully. No further optimization was attempted.
