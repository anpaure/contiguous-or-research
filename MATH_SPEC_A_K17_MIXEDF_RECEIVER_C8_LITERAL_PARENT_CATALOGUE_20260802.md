# Exact launch specification for the K17 mixed-F receiver C8 catalogue

**Date:** 2026-08-02  
**Lane:** A, receiver-bank joint chain-slot packets  
**Status:** proof-audited finite specification; computation queued during the
H100 resource hold.  All structural and socket verdicts below are therefore
`UNKNOWN`, not negative.

## 1. Two literal structural parents

The same already-generated cycle list must not be transported between
parents.  The catalogue is rebuilt independently on:

1. the warm47-derived 470-transfer parent
   `scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.table.tsv`,
   SHA-256
   `34838ee1e8d2149feaa5254bcd51fb02f4659c6a35bb77b4938bf2d73f9e674e`;
2. the authenticated phase-zero private parent
   `scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv`,
   SHA-256
   `b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc`.

The immutable original-P2 label is the set of 3,899 chain IDs in
`phase0.p2_global_union.metrics.tsv`, SHA-256
`b45713072b1d54d315c9d6de3512741aaa8c143966316bece76b80d0ec5ae137`.
It is not reconstructed from a candidate parent's current chain lengths.

The remaining exact inputs are bound as follows:

```text
origin res1972                         db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
fixed-root 623-role ledger             80d53fa5ab4d0c356bbf9be55099f103a6b77c15265e05161c0aa7de77117581
selected 1748 ticket records           d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
transported owner phase 0              ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
transported owner phase 1              736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
origin-bound potential-p edge atlas    d39b58f679f4d9219b72209b06ea71387db64cdecac649a4f390c9f7ed13da25
```

## 2. Exact C8 object and canonicalization

For a literal parent let `A_v` be the current lower target and `R_v` the
rank-eight root of a current length-two row `v`.  A simple directed C8 is an
ordered four-tuple of distinct rows `(i,j,k,l)` satisfying

\[
 A_i\subsetneq R_j,\qquad A_j\subsetneq R_k,\qquad
 A_k\subsetneq R_l,\qquad A_l\subsetneq R_i.       \tag{2.1}
\]

It replaces the four bottoms by `(A_l,A_i,A_j,A_k)`.  The target partition,
physical rows, roots, owners, and row lengths are therefore unchanged.

The mixed-F catalogue requires:

* at least one row among the fixed anchor set

```text
23021 23042 23046 23070 23336 23340
23471 23850 23955 23987 24051 24055;
```

* at least one current length-two row outside the fixed 3,899-row
  original-P2 set.

Only directed rotations are identified.  The canonical representative is
the lexicographically least of the four rotations.  Reversal is retained as
a different object whenever it is directed-legal.

### Completeness

Every eligible directed C8 contains an anchor.  Start (2.1) at that anchor;
the three indexed forward adjacency steps and the closing containment
enumerate it.  Conversely every enumerated tuple satisfies all four strict
containments and is a target/root matching circuit.  Rotation minimization
selects exactly one representative, including when a cycle contains more
than one anchor.  Hence the generator is complete and duplicate-free for
the declared face.

## 3. The 7,213-row field is avoidance only

The union of the nonnegative row-valued fields

```text
short_row, pred_host, pred_token, succ_host, succ_token
```

over the 1,748 selected ticket records has size 7,213.  There is one
fixed-soft token value `-1`, which is not a physical row and is excluded from
the union.  Every C8 records its number of hits on this set.

Zero hits proves only physical-address avoidance.  It does **not** prove
private-ticket preservation: neither structural parent currently has a
proved common contract containing the same literal table, both owner-phase
occurrences, protected tickets/outer matching, selected-parent supplier,
cyclic cells, bottom pins, and endpoint state.

## 4. Rowwise socket replay and the b268 phase obstruction

For every distinct `(physical row,new bottom)` key used by the
`fullprivate470` catalogue, the queued exact marginal replay fixes the
current bottom/root, installs each transported round47 owner phase in turn,
and searches all 2,129,483 dynamic origin-bound potential-p modes plus the 17
fixed-soft modes.  It enumerates all nine short families and uses the exact
nonempty five-cell coordinate DP.  A cycle passes the rowwise necessary gate
only when all four keys have a literal witness in both phases.

This does not impose one joint cyclic cell, bottom-pin matching, or shared
endpoint state and is not composability.

The same two-phase command is invalid for `b268`: its phase-zero owner column
already differs from round47 phase zero on 1,863 of the 3,899 original-P2
rows, and no authenticated transported b268 phase-one owner/state table is
frozen.  Thus only the b268 structural catalogue is queued.  A one-phase
marginal b268 audit may use b268's own owner column, but no two-phase b268
verdict is permitted from present inputs.

## 5. Frozen launch sources and resource contract

The proof source, exact scope, sharded pricer, and aggregator are at

```text
scratch/a_k17_mixedf_c8_20260802/
```

The H100 campaign root is

```text
/home/amodo/or15/work/a_k17_mixedf_c8_20260802
```

and has been populated with source and immutable inputs only.  No compile or
enumeration was launched under the resource hold.  The runbook enforces at
most eight socket shards and a 16 GiB address-space cap per process.

Current exclusions: a positive/negative finite verdict, private or supplier
preservation, common cyclic-cell/bottom-pin/endpoint-state replay,
chronology, topology, residence, upper/source/common-cap/compiler rows, and a
word.
