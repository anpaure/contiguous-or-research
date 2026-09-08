# K17 receiver circuits: parent binding and the protected-row obstruction

**Date:** 2026-08-02  
**Status:** proof-complete parent-lineage lemma and exact finite calibration.
This note does not decide the mixed-`F` `C8` or all-`P2` `C10` socket
catalogues.  It states what those catalogues can prove before a common
parent is materialized.

## 1. The two parents must not be identified

Let

* `A` be the warm47-derived receiver/LLR parent whose current structural
  calibration is
  `scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.table.tsv`;
* `B` be the literal private-bank parent
  `scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv`;
  and
* `P` be the union of the physical row occurrences named by the selected
  private tickets: the short row, predecessor and successor host rows, and
  the real predecessor and successor token rows.

The occurrence counts are

\[
   (|P_{\rm short}|,|P_{\rm host}|,|P_{\rm token}|)
     =(1748,3496,3495),
\]

and their deduplicated union has

\[
                              |P|=7213.              \tag{1.1}
\]

These are occurrence and row-address facts.  They do not make `B` a
certificate on `A`.

The independently reconstructed common-parent contract is

```text
original.res1972.tsv           db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
selected_tickets.tsv           d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
complete_outer_matching.tsv    179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
private_h_outer_materialized   b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

The first three objects reconstruct the fourth literally on all 24,310
rows.  Thus `B` is not merely a convenient table with the right roots: it is
the selected-parent output of that exact occurrence-labelled contract.

Literal replay gives

\[
 \bigl|\{p\in P:A(p)\ne B(p)\}\bigr|=6479.          \tag{1.2}
\]

The typed mismatch counts are `1564` short, `2946` host and `2927` token
rows; they overlap, so they must not be summed to recover (1.2).  Across all
24,310 rows the two tables differ at 16,034 addresses.

The mismatch is also semantic rather than cosmetic.  On the uniquely forced
root map, `A` retains zero of the 1,748 complete tickets of `B`.  Ticket zero
already witnesses this: its unique-root row 14337 must be
`[68402,72498]` on `B`, whereas it is
`[67888,68402,72498]` on the warm47-derived table.

## 2. Exact parent-binding lemma

### Lemma 2.1 (outside-support edits cannot transport a foreign certificate)

Let `A` and `B` be labelled row tables on the same row set, let `P` be a
declared protected row set, and let `c` be any edit with physical support
`S(c)`.  If

\[
                             S(c)\cap P=\varnothing, \tag{2.1}
\]

then

\[
                 A^c|_P=A|_P.                              \tag{2.2}
\]

Consequently

\[
                 A^c|_P=B|_P\quad\Longleftrightarrow\quad
                 A|_P=B|_P.                                \tag{2.3}
\]

In particular, if `A` and `B` differ on `t` rows of `P`, every edit that
literally turns `A|_P` into `B|_P` has support at least `t`.

#### Proof

An edit changes only rows in its support.  Condition (2.1) therefore fixes
every row in `P`, proving (2.2).  Equation (2.3) follows by substitution.
If literal equality with `B` is required, every one of the `t` differing
row addresses must belong to the edit support.  \(\square\)

### Corollary 2.2 (the 7,213-row receiver filter is footprint-only)

On the frozen calibration, every receiver circuit accepted merely because
its changed rows avoid `P` leaves all 6,479 protected-row discrepancies
unchanged.  Such a circuit does **not** preserve the selected literal
private tickets on their authenticated parent.  This conclusion is
independent of circuit support, socket counts, or supplier rank.

If one insists on transporting that exact row-valued certificate from `B`
to `A`, the row-support lower bound is 6,479.  This bound does not exclude
selecting a different private bank on `A`, nor a receiver circuit built and
replayed directly on `B`.

## 3. Proof-safe common-parent contract

A receiver packet may be called composable only relative to one explicitly
hashed parent tuple

\[
 \Pi=(T^0,T^1,\tau,\mathcal U,\mathcal B,\mathcal M_{\rm out},
       \mathcal S,\mathcal C),                              \tag{3.1}
\]

where `T^0,T^1` are the transported literal tables, `tau` is the occurrence
transport, `U` is the complete endpoint/state occurrence selection,
`B` is the private ticket bank, `M_out` is its bottom/outer matching,
`S` is the selected-parent supplier record and matching, and `C` is the
cyclic-cell ledger.  For a circuit `c`, one literal child of this same tuple
must replay:

1. the exact target/root/owner and row-length ledger;
2. one transported occurrence for every changed role in both phases;
3. all private tickets and their exact host/token bottom pins;
4. the endpoint-state and cyclic-cell equations;
5. the selected-parent supplier graph and its required matching; and
6. every declared capacity-one occurrence resource.

Separate phasewise socket existence, an old supplier projection, and
row-address avoidance are only necessary projections of (3.1).

## 4. Consequences for the active `C8/C10` census

There are now exactly two proof-safe outcomes.

* If complete enumeration shows that every circuit in a declared family
  already fails an exact rowwise two-phase socket, that is a valid family
  no-go: later private/supplier/state gates cannot repair a zero local
  occurrence.
* If a circuit passes the rowwise socket screen on `A`, it remains only a
  warm47/receiver-parent candidate.  It is not a positive packet until a
  tuple (3.1) is materialized.  Avoiding the 7,213 row addresses proves only
  footprint avoidance by Corollary 2.2.

Likewise, enumeration directly on `B` can genuinely inherit the phase-zero
private certificate, but it still needs an independently replayed phase-one
transport, selected-parent supplier, cyclic-cell, bottom-pin and endpoint
state before a two-phase composability claim.

## 5. Exact artifact bindings

At the time of this note the load-bearing hashes are:

```text
34838ee1e8d2149feaa5254bcd51fb02f4659c6a35bb77b4938bf2d73f9e674e
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.table.tsv

b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv

d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  scratch/k17_phase0_retained_witness_private_basis_20260802/selected_tickets.tsv

179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
  scratch/k17_phase0_retained_witness_private_basis_20260802/complete_outer_matching.tsv

92b8c0062aa68516a0666813dc4fb76541eb0f375524c8c68751cd0346d06da2
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.independent.audit.json

ac49a16af8fc153653308887ac29878c25daa47a23995a572fcdeb2fbb37a656
  scratch/audit_k17_llr_fullprivate470_independent_20260802.cpp
```

The corrected global theorem carrying the same qualification is
`MATH_THEOREM_ROOT_K17_FULLPRIVATE_LLR_SUPPLIER_RANK_BENDERS_20260802.md`.
The exact reconstruction and nontransport replay is frozen in
`MATH_AUDIT_K_K17_PRIVATE_BANK_COMMON_PARENT_CONTRACT_20260802.md`, SHA-256
`df67912d2e8fd8b0971bd4d028ac8c361fe69e66b62ef9e2d2a45e30b3abf5ca`.
