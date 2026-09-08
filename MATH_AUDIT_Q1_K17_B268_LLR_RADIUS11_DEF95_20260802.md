# Q1 audit: a one-for-one protected LLR exchange reaches K17 supplier deficiency 95

**Date:** 2026-08-02  
**Status:** exact finite positive theorem on the authoritative `b268` target
parent.  A radius-`(drop 1, add 1)` exchange preserves all measured socket
counts of the 438-transfer seed and improves exact supplier rank by one.  It
is the primary supplier-descent incumbent on this face, not a chronology or
K17 word.

## 1. Authenticated parent and seed

The target parent is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_h_outer_materialized.tsv
SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

Every admissible transfer belongs to the `93,234`-edge native protected
catalogue.  That catalogue excludes the exact union of all `7,213` short,
host, and nonnegative token rows used by the authenticated private ticket
bank.

The radius search starts from the independently audited `438`-transfer table
obtained by adding global protected edge `57336` to the DM-fixed `437` table:

```text
seed table SHA-256       7206ab1c9f3763aa0cfad7e88516753142d2bbbb858627b45fa3f49dee514655
seed supplier matching  16802 / 16898
seed deficiency         96
```

## 2. Exact bounded exchange

Constrain the selector to exactly one deletion and one insertion relative to
the seed, within all `11,893` native-phase0/transported-phase1 marginal-common
protected edges.  The exact first Benders iteration returns

```text
removed global edge index    41
added global edge index       89826
selected transfers            438
```

The resulting artifact is

```text
table SHA-256
  ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374
selected-edge SHA-256
  d6dca87229b542481f4f686f851c15700939db9b952cd26ce9df3b47d19bb8f0
```

## 3. Independent exact replay

An independent protected-row comparison finds

```text
table rows                         24310
rows whose target chain changed     876
authenticated protected rows       7213
protected rows changed                 0
```

The independent generalized supplier replay constructs `74,129` row-pair
edges and returns

```text
matching       16803 / 16898
deficiency     95
zero heads     80
DM shore       109 heads / 14 neighbors
graph FNV64    a554eccc7fd8416f
```

Its audit SHA is

```text
54ec235f807cdc73ce09f1b42fa8639b1f10820f0c9aea5e2f54fbf164d733ae
```

The two full short-DNF replays give

```text
native b268 phase 0 positive               3098
transported root-aligned phase 1 positive  2253
positive in both                            1839
positive in either                          3512
```

These are exactly the socket counts of the seed.  The exchange is therefore
socket-neutral on all four complete-table metrics and raises supplier rank by
one.

### Bounded-exchange theorem

On the protected common-positive `b268` LLR face, there are two row-disjoint
438-transfer selections differing by one removed and one added transfer such
that:

1. both complete tables have socket tuple
   `(3098,2253,1839,3512)`;
2. the first has supplier rank `16802` and the second rank `16803`;
3. every one of the `7,213` authenticated ticket rows is identical to its
   literal `b268` value in both tables.

#### Proof

The selected TSVs differ exactly by global edges `41` and `89826`.  Direct
materialization validates the target partition and row-disjointness.  The two
full DNF enumerations give the displayed socket tuple.  A separately compiled
supplier auditor reproduces the selected table's entire edge hash, maximum
matching, zero-head census, and DM shore.  Direct row comparison establishes
the ticket-row identity claim.  No marginal additivity assumption is used.
\(\square\)

## 4. Relation to the 454-transfer table

The earlier free-addition lane has a socket-richer `454`-transfer Pareto point
with tuple `(3115,2266,1855,3526)` and supplier rank `16802`.  It is not
falsified.  The present `438` table supersedes it as the **primary supplier
descent incumbent** because its rank is `16803`; the two are Pareto
incomparable if socket count and supplier rank are retained as separate
objectives.

The exact next finite task is bounded exchange from this table toward
deficiency `94`, followed by full repricing and independent replay of any
strict supplier improvement.

## 5. Frozen artifacts and scope

The local package is

```text
scratch/q1_k17_b268_llr_radius_def95_20260802/
```

Key hashes are

```text
iter1.table.tsv                         ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374
iter1.selected.tsv                      d6dca87229b542481f4f686f851c15700939db9b952cd26ce9df3b47d19bb8f0
iter1.projection.audit.json             54ec235f807cdc73ce09f1b42fa8639b1f10820f0c9aea5e2f54fbf164d733ae
iter1.native_phase0.dnf.tsv             09e3c0303134781c985be87221749a2c520e39702df36731e0f213c2d2542874
iter1.transported_phase1.dnf.tsv        343c0c7b25ed4da8e94458ef98594926db3552401c9fce31613b7d3a81d364f8
```

Phase 0 is literal on the `b268` owner table.  Phase 1 remains a root-aligned
transported `round047.s7` owner marginal; the common carrier-opening transport
is not proved.  The theorem also does not replay the residual complete outer
matching after target-row exchanges, construct one common occurrence-labelled
state, or establish chronology, residence, arbitrary upper shadows, common
cap, compiler feasibility, a universal K17 word, or a new upper bound for
`nu(17)`.
