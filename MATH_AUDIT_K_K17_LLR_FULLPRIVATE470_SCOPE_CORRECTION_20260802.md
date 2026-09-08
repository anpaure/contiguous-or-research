# Independent audit: K17 LLR `fullprivate470` scope correction

Date: 2026-08-02  
Lane: K, independent replay  
Verdict: **the numerical transfer-graph claims pass, but the literal
full-private interpretation is false**

## 1. Executive statement

The corrected transfer-graph program reports

```text
common-positive edges after protected-address deletion  4803
common-only matching rank                              470
structural matching rank                              1012 / 1018
```

An independently written C++ replay reproduces all three numbers.

However, the graph and its `470`-edge materialization are based on the
warm47 table

```text
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
  scratch/ad_k17_s7_carrier_adapter_20260802/input/round047.table.tsv
```

and merely delete transfer edges whose two changed row **addresses** meet a
protected address.  The authoritative private bank is materialized on the
different table

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    private_h_outer_materialized.tsv
```

Consequently `fullprivate470` is not a literal full-private table.  It is a
warm47-based, protected-address-avoiding static transfer table.

## 2. Protected occurrence bank

The ticket file has exactly

```text
short occurrences       1748, all row-distinct
host occurrences         3496, all row-distinct
token occurrences        3495, all row-distinct
unique row addresses     7213
```

The category sets overlap, so the three occurrence counts must not be added
to obtain the unique-row count.  The independently parsed input is

```text
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    selected_tickets.tsv
```

Deleting every transfer edge whose donor or receiver row belongs to this
7,213-row set gives the following exact warm47 graph:

| graph | edges | maximum matching |
|---|---:|---:|
| structural, protected-address avoiding | not asserted separately | `1012/1018` |
| phase-common before deletion | `6804` | not needed |
| phase-common, protected-address avoiding | `4803` | `470/1018` |

Thus six left roles are structurally uncovered, and 548 are uncovered on the
phase-common face.  These are exact matching deficiencies of this scoped
warm47 graph.

## 3. The materialized 470 table

The selected structural matching contains `1012` row-disjoint transfers, of
which exactly `470` are phase-common.  The frozen `470` table materializes
exactly those `470` common transfers:

```text
changed rows                  940
length histogram              (0,7395,16915)
lower target partition        all 65535 rank-1 through rank-8 masks once
root/owner columns             unchanged from warm47
```

The table hash is

```text
34838ee1e8d2149feaa5254bcd51fb02f4659c6a35bb77b4938bf2d73f9e674e
  scratch/q1_k17_llr_socket_matching_20260802/
    llr_fullprivate470.table.tsv
```

This proves a valid warm47 static recoupling.  It does not prove private-bank
survival.

## 4. Literal private-bank failure

Comparing the candidate against the authoritative `b268...` materialization
gives

```text
all differing table rows                    16034
differing unique protected rows               6479 / 7213
differing protected short occurrences         1564 / 1748
differing protected host occurrences          2946 / 3496
differing protected token occurrences         2927 / 3495
```

Therefore row-address avoidance is not a substitute for retaining the
literal short/host/token occurrences.  In particular, replaying a ticket
whose row IDs are untouched is unsound when the contents initially occupying
those rows come from warm47 rather than from `b268...`.

There is a smaller literal residual face.  Among the 4,803 warm47
phase-common, address-avoiding edges, require that the old `LR` and `LMR`
chain identities actually occur at the same rows of `b268...`.  The exact
census is

```text
edges       1900
left rows    933
right rows   118
matching     118
```

If one also requires every old phase-0 and phase-1 predecessor and successor
witness row named by the warm47 prices to be unchanged between warm47 and
`b268...`, the residual is

```text
edges        263
left rows    258
right rows    12
matching      12
```

These last 263 edges are only legacy-witness-preserving candidates.  The old
prices are not an authoritative complete price catalogue on `b268...`; a
rank-generic two-phase rebuild is still required.

## 5. Current repricing output, with exact scope

The current warm47-based `470` candidate has supplied marginal short-DNF
outputs:

```text
phase 0 positive shorts      1770 / 7395
phase 1 positive shorts      1781 / 7395
positive in both phases      1437 / 7395
```

Every repriced bottom and root agrees with the candidate table.  The phasewise
owner columns differ from the static table at 3,599 and 3,700 rows,
respectively; that is expected phase transport and is not treated as an
error.  This audit consumes the `exists` bits and does not independently
rederive five-cell feasibility.

The producer's exact generalized supplier projection on this same candidate
reports

```text
matching                  16872 / 16898
deficiency                   26
zero heads                   23
Hall shore                   36 -> 10
projection edges             73247
```

with audit hash

```text
b52184e189fac458bcadc1dd2761dc256654570cdc57c671ce1b4aa2d83508eb
  scratch/q1_k17_llr_socket_matching_20260802/
    llr_fullprivate470.projection.audit.json
```

This supplier result belongs to the warm47-based table; it is not a
private-bank-compatible supplier result.

## 6. Proof-safe replacement statement

The exact statement that survives is:

> On the warm47 LLR transfer catalogue, deletion of all edges whose two
> changed row addresses meet the 1,748-short/3,496-host/3,495-token address
> bank leaves a structural matching of size 1,012 and a phase-common graph of
> 4,803 edges with matching rank 470.  One maximum common submatching gives an
> exact static 470-transfer table.  This does not retain the literal private
> bank materialized on `b268...`.

The next exact selector must start from `b268...`, regenerate literal LLR
columns and both phase-state catalogues there, and then couple the surviving
columns to supplier rank.  The warm470 table is calibration only.

## 7. Independent audit artifacts

```text
ac49a16af8fc153653308887ac29878c25daa47a23995a572fcdeb2fbb37a656
  scratch/audit_k17_llr_fullprivate470_independent_20260802.cpp

92b8c0062aa68516a0666813dc4fb76541eb0f375524c8c68751cd0346d06da2
  scratch/q1_k17_llr_socket_matching_20260802/
    llr_fullprivate470.independent.audit.json
```

Independent replay command:

```bash
clang++ -O3 -std=c++20 \
  scratch/audit_k17_llr_fullprivate470_independent_20260802.cpp \
  -o /tmp/audit_k17_llr_fullprivate470_independent

/tmp/audit_k17_llr_fullprivate470_independent \
  scratch/q1_k17_llr_socket_matching_20260802/llr_all_edges.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_all.phase0.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_all.phase1.tsv \
  scratch/k17_phase0_retained_witness_private_basis_20260802/selected_tickets.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate_socket_matching.selected.tsv \
  scratch/ad_k17_s7_carrier_adapter_20260802/input/round047.table.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.table.tsv \
  scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.phase0.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.phase1.tsv \
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.independent.audit.json
```

Excluded throughout: selected simultaneous state DNFs, literal supplier
rematching on the protected table, chronology, residence, upper shadows,
compiler, and word.
