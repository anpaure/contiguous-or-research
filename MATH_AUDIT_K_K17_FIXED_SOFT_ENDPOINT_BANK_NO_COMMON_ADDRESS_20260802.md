# K17 fixed-soft endpoint bank: exact no-common-address obstruction

**Date:** 2026-08-02  
**Status:** independently replayed exact obstruction for one restricted
endpoint bank.  This is not a global `1S-ROTS` no-go.

## 1. Question and input

The input table is

```text
scratch/ad_k17_h1_res1972_minlong_recoupling_20260802/
  k17_depth3_owner_payload.res1972.tsv
```

with SHA-256

```text
db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
```

It has `18,646` hard long rows and `17` fixed soft-long rows whose native
bottom is a singleton.  For each hard row `v`, shorten its payload to the
two-target chain `(M_v,U_v)` and consider all nine relaxed short addresses.
The question audited here is deliberately restricted:

> Can this shortened row be placed between two of the 17 fixed soft-long
> rows, with one of four long flags on each side, satisfying the exact
> common five-cell state?

All 17 rows are offered on both sides even when their owner/root is not a
literal neighbor of `v`.  Thus the audited bank is an overapproximation of
the physically indexed fixed-soft bank.  Proving it empty is valid for the
restricted fixed-soft/fixed-soft face.

## 2. Exact marginal reduction

For every short slot/address `(v,q)`, define

\[
 I(v,q)=\{(h,\alpha):h\text{ is a fixed soft row and the exact incoming
 four-cell box is feasible}\},
\]

and define `O(v,q)` analogously for the outgoing side.  Every common
five-cell socket must first satisfy

\[
                         I(v,q)\ne\varnothing,
 \qquad                   O(v,q)\ne\varnothing.       \tag{2.1}
\]

The producer reconstructs the four long flags, all nine short addresses,
and the exact maximal lower/upper box on each four-cell overlap.  It then
joins only a common `(v,q)`, checks `beta<=alpha`, the same-row/same-flag
resource rule, and finally the literal five-cell cover.

## 3. Exact result

The final census is

\[
\begin{array}{c|r}
\text{accepted incoming marginals}&289\\
\text{accepted outgoing marginals}&304\\
\text{rows with some incoming marginal}&120\\
\text{rows with some outgoing marginal}&125\\
\text{rows having both at possibly different addresses}&1\\
\text{slot/address keys having both sides}&\boxed{0}.
\end{array}
\]

The unique row with both marginal directions is row `6743`, but its sides
occur at disjoint addresses:

```text
OUT: q=0,1 through fixed row 136, flag 2
 IN: q=5,6 through fixed row 137, flag 0
```

Therefore the raw Cartesian join is already empty.  No direction, resource,
or five-cell filtering is needed after (2.1).

### Theorem 3.1 (fixed-soft endpoint obstruction)

No hard dummy-short slot in this table has an exact relaxed-nine
fixed-soft/fixed-soft socket.  Equivalently, every literal common-state
socket for a hard short role must use at least one dynamically materialized
real-bottom long endpoint.

#### Proof

Every exact five-cell socket has a common short address `q`; restricting it
to either four-cell overlap gives one member of `I(v,q)` and one member of
`O(v,q)`.  The exhaustive independently replayed catalogue has no `(v,q)`
for which both sets are nonempty.  This contradicts (2.1).  The second
statement is the contrapositive.  \(\square\)

## 4. Independent replay

The producer is

```text
scratch/k_rots_k17_joint_1s_20260802/
  audit_k17_dummy_short_fixed_soft_endpoint_bank_20260802.cpp
```

SHA-256:

```text
a0d18723a412e137851792c13ced1b8270fcf7353d1a708177fbdf8a93d19545
```

Its exact audit JSON is

```text
scratch/k_rots_k17_joint_1s_20260802/fixed_soft_endpoint_bank/
  soft_endpoint_bank.audit.json
```

SHA-256:

```text
8e26379b28149be640a225b03217170155c57bef7415291ae73fb1627f5d0dc5
```

The independent source reconstructs every four-cell maximal box directly,
compares the complete marginal record set, and checks the empty common-key
join:

```text
scratch/k_rots_k17_joint_1s_20260802/
  audit_k17_fixed_soft_endpoint_marginals_independent_20260802.cpp
scratch/k_rots_k17_joint_1s_20260802/fixed_soft_endpoint_bank/
  soft_endpoint_bank.independent.audit.json
```

SHA-256 values:

```text
de0a76be03c9ee1aab64378c6388158a27505fca06f8eb72af76426b5ba547fc
5c5873b4c2c2d1ee9ad678a77f7fd1c868afc3128681ade75a2ce60051c8b25d
```

The run used one H100 CPU lane at `nice 15`, an 8 GiB virtual-memory cap,
and `5,632` KiB peak RSS.  The persistent root is

```text
/home/amodo/or15/work/k_rots_k17_socket_softbank_20260802
```

## 5. Scope and the defect-zero rebase

This theorem does **not** say that any hard slot is globally socketless.
It excludes only sockets whose two long endpoints both come from the 17
fixed soft-long rows.  Mixed fixed/dynamic and dynamic/dynamic endpoints
remain live, and they require their full occurrence-labelled tickets in the
joint selector.

The phase-0 relay table with lower projection matching `16898/16898` after
47 strict exchanges is now independently replayed and frozen under

```text
scratch/k_rots_k17_joint_1s_20260802/warm47/
```

The table SHA is
`95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`;
the independent projection audit SHA is
`2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a`.
Thus the lower projection defect is closed.  It does not alter Theorem 3.1:
the remaining gate is literal state/reset consistency on the selected
dynamic endpoint placements, followed by reattachment to the authoritative
carrier and both owner phases.  No residence, upper-shadow, topology,
compiler, or word claim is made here.

In particular, the defect-zero table must be used as an outer warm start,
not pinned as a fixed child: its exhaustive relaxed-nine state census has
`5,969` zero short roles and is fixed-table UNSAT.  The live exact move is to
change outer placements while preserving a perfect hard-head projection.
