# Independent audit: K17 S47 source with a single N helper

**Date:** 2026-08-03  
**Verdict:** **GO**, in the narrow scope stated below.

## Authenticated H100 package

The audited run is

```text
/home/amodo/or15/work/codex_019fc39a_k17_s47_n_prefix_aperture_20260803
```

and a compact local snapshot is retained at

```text
scratch/audit_k17_s47_n7_h100_independent_20260803/remote_snapshot
```

The remote `sha256sum -c FINAL_MANIFEST.sha256` replay passed every listed
entry. The exact identities are:

```text
FINAL_MANIFEST.sha256 file
  0c4e2b404bb1d8f8bc3a0cea50a45def575cfad8cde51598bb5e29f1bbf7289f
RUN_INPUTS.sha256 file
  ccf3c6bd4470ecd657732f13bd423cf8ecdd9e4a7f7e19d81656f99005fcd281
OUTPUTS.sha256 file
  7424dd0f43edc1bc47ed750453364329a66769454539b10fd65cd9a28db2d89e
producer source
  02e946595b4db261dc278206566e0a663fa7dfa7381dbff530ee41daefd4fe87
H100 binary
  3899c788ecde7c2f85d1f952398aae31d22ca5da378edbc34a0fe74e7a59acc8
upper TSV
  534180a4038eb404d7c649ed279f1d9538691e50d43d2194871a6c4892a92feb
upper audit
  891d979201f141400538f5eaa5f91fd8e835066d421394e19bc14a361f358bdf
stdout / stderr
  8324532531b050c5bf99c95a5fb2ffd5fa821e925a10165dff9bd1e487647e91
  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The run reports

```text
PASS_K17_DROP12_S47_N_PARTNER_HOST_APERTURE_UPPER
seeds=329 phasewise_upper=0 first_pair_consistent_diagnostic=0
```

The output TSV is exactly its header.

## Domain and losslessness

The SHA-bound all-U classification contains 47 `S` modes and seven `N`
modes. The seven `N` modes are exactly edges `52844,...,52850`, all with
host row 14851. Every one of the `47*7=329` directed `S x N` pairs has
disjoint transfer endpoints.

Fix an `S` source `s` and an `N` helper `n`. The authenticated S47 unary
replay has no exact two-phase same-key source option. Passing from the unary
child to the pair child changes the long-provider bank only by deleting the
helper donor and installing the helper host.

For every one of the 329 pairs the H100 checker constructs the complete
phase-ticket bank after both selected donors are removed and both selected
hosts are installed. It excludes the private 7,213 rows, reserves the exact
20 incumbent rows independently in each phase, admits an opposite-only row
only at its fixed flag, retains the incumbent LLR hosts, and exhausts all 90
declared keys, both provider sides, and the literal five-cell predicate.

The rejection test is deliberately permissive: it asks only whether some
declared key has at least one physical ticket in each phase. It does not
require the two tickets to have consistent cross-phase flags; it does not
require a helper-role option, joint capacity, materialization, or supplier
gain. Therefore every exact two-phase source prefix would appear in the
upper ledger. Since the complete ledger is empty, no `S` source has a
single-`N`-helper prefix.

An independent local specialization of the previously promoted broad S47
aperture source produced the same header-only TSV byte for byte; its compact
reproduction bundle is

```text
scratch/audit_k17_s47_n7_prefix_zero_20260803
```

with top manifest file SHA
`4afc7df728b14eab7f913091d6d93dd307cf162b91a53bcfbb246d0b0bcb47a3`.

## Theorem scope

Within the canonical `e878/fa491` parent and endpoint-disjoint U112621
catalogue:

> An `S` source supported by exactly one helper of class `N` is
> occurrence-dead.

Indeed, in any larger selection whose source option uses `h_n` and no other
new helper host, delete the other transfers. The selected source tickets use
none of their installed hosts and none of their absent donors, so the same
physical option restricts to the impossible `S x N` prefix.

For a target-capable no-H triple of class `S,S,N`, this closes the
single-`N`-helper orientation. The single-`S`-helper orientation restricts
to an `S x S` prefix and is outside this audit; it is handled only when the
separate complete `S x (S union Z)` prefix theorem is invoked. A source
using both helpers is bilateral and is also outside this result.

This audit makes **no** claim about a single `S` helper by itself, bilateral
source options, H-containing triples, full supplier rank, chronology,
residence, upper shadows, compiler feasibility, or a K17 word. Phase 1 is
the authenticated transported-owner phase, not a new native-phase claim.

