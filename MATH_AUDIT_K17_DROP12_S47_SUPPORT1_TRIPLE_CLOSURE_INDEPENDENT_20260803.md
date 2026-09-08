# Independent audit: K17 S47 support-one triple closure

**Date:** 2026-08-03  
**Verdict:** **GO**, with the exact quantifier and exclusions below.

## 1. Authenticated three-prefix H100 result

The audited run is

```text
/home/amodo/or15/work/root_k17_s47_support1_sz3_20260803_08d45ad52d80
```

and the compact independent snapshot is

```text
scratch/audit_k17_s47_support1_sz3_independent_20260803/remote_snapshot
```

The remote `sha256sum -c FINAL_MANIFEST.sha256` check passed. The principal
hashes are:

```text
FINAL_MANIFEST.sha256 file
  13f09c24b3ab43ab4843a4a6c702e105749096a1cd1ce8394f8f659b8923629b
RUN_INPUTS.sha256 file
  957da903494ba682d13c4707bf0f215d464a7a86ae94662ceeb3505d5889b082
OUTPUTS.sha256 file
  d443d347bf798cf05f39ff3b7f1c56319605cb234978dad1041e5b3d75cd792f
run script
  b4e6a2f0e916b211fec0d924cc918418c669f799cf20b5fe63250f41345020fe
common source
  08d45ad52d809952ef2747a47ef4ac25863412ce0b55181d102244f94061bf34
upper source / binary
  0b0fdd50a237db041645c8679fcea53a27026506e7910d692bbfe35aef0fa2e0
  e910f85ae2a826117d4bb2fa62bb7c9feca84295bbb9bdb1a452a2755a049a38
exact source / binary
  165cf0c09fabe3a805b26724ec24977a7f5d2a930b67fb10b13674f5446090c9
  391805a50f9fec8df9d45f0df80475f5b3d036904b48f1f2ccab1056af69fcfd
upper TSV / audit
  e636a9ee27e90d57934fbd9bfff7d8dd766557d3d07bdefef6414e16172dc2dd
  924ffb1c86aa5818f0554f4434f91f2fedb8672a01c1b2399bc1323ea1e6aa69
exact TSV / audit
  d5783322d678673e798e8ef004a168df81956d9a31b984043646138b8327ca33
  96cfe80671f4c4d4a335587aac2ff7b00284f7638fd276509e35a5f063bbff14
```

The upper result is

```text
raw prefix/third rows                 336438
endpoint-and-prefix-disjoint rows     334639
per-prefix shores         110864 / 112007 / 111768
third class S rows                       138
third class Z rows                    334501
helper-option survivors                    0
per-prefix survivors                    0/0/0
```

The exact consumer therefore receives zero requests and writes a
header-only exact ledger. No positive child exists to materialize or send to
supplier replay in this branch.

## 2. Why the upper zero is lossless

The complete S47 pair-prefix theorem leaves exactly three source options:

```text
source 92903, helper 25925, key 70
source 92903, helper 25927, key 70
source 92903, helper 25929, key 70
```

All three helpers are class `Z`, share host row 9054, and have distinct
donors. The source option is unique for each helper and has physical tickets

```text
phase 0: (9054,8994)
phase 1: (9069,8994)
```

For each prefix, the upper enumerates every `S`-or-`Z` third mode. It keeps
only six-endpoint-disjoint modes and also requires both the third host and
third donor to avoid the fixed source footprint. This is the exact condition
under which the frozen source option survives unchanged and continues to use
the old helper but not the third host.

The helper has no phase-0 pair-child ticket in any of the three prefixes.
For helpers 25927 and 25929 it also has no phase-1 ticket. Accordingly the
upper rebuilds the complete helper ticket relation after all three donor
deletions and host insertions, requires every formerly empty phase to use the
third host, joins equal declared keys across phases, checks the helper's
cross-phase flag map, and checks compatibility with the fixed source option.
It exhausts all physical alternatives; it never rejects on a first witness
or diagnostic bit.

The third role itself is deliberately not tested in this upper. Therefore
every exact three-role support-one packing would first produce a surviving
helper option and appear in the upper ledger. Zero helper-option survivors
is a proof-safe rejection of all 334,639 third shores.

The exact verifier was also statically audited. Had an upper row existed, it
would have rebuilt all six role/phase menus after simultaneous three-transfer
materialization, filtered the source to use the frozen helper host and not
the third host, enforced equal keys and internal flag consistency for the
helper and third roles, phase-local unit capacity across all three roles, and
one global row-to-flag map. Its zero-request execution is consistent with the
stronger upper no-go.

## 3. Combining the N-helper branch

The three-prefix run covers helpers and thirds in `S union Z`. The missing
no-H supplier-relevant class pattern was `S,S,N`: singleton inherited-shore
credits are `+1,+1,-1`.

That branch is independently closed by the authenticated H100 `S x N`
source-prefix replay:

```text
/home/amodo/or15/work/codex_019fc39a_k17_s47_n_prefix_aperture_20260803
```

Its final-manifest file SHA is
`0c4e2b404bb1d8f8bc3a0cea50a45def575cfad8cde51598bb5e29f1bbf7289f`.
It exhausts all `47*7=329` `S`-source/`N`-helper pairs and returns zero
phasewise same-key source prefixes. The independent audit note is

```text
MATH_AUDIT_K17_DROP12_S47_N_HELPER_PREFIX_NOGO_INDEPENDENT_20260803.md
```

at SHA
`2a33d3e228b21022a7e8631c914de7f0e3e1e5c09936b71e608a550b85c53997`.

If an `S,S,N` triple source used only the `N` helper, deleting the other `S`
transfer would restrict it to the impossible `S x N` prefix. If it used only
the other `S` helper, deleting the `N` transfer would restrict it to an
`S x S` prefix; the complete `S x (S union Z)` prefix theorem has only the
three helpers above, all class `Z`. Thus `S,S,N` has no support-one source
orientation.

## 4. Exact conclusion and exclusions

On the canonical `e878/fa491` parent and endpoint-disjoint U112621
catalogue:

> Every no-H, supplier-relevant, occurrence-valid triple with a
> distinguished `S` source must use both of its helper hosts at that source.
> Equivalently, all no-H S-source support-one triple branches are closed, so
> the residual S-source triple frontier is forced bilateral.

The quantifier is exactly triples. This audit makes **no claim** that a
bilateral triple exists or is impossible, no claim for arbitrary higher
arity, and no claim about H-containing triples, another parent or catalogue,
overlapping transfers, native phase 1, full supplier rank after a bilateral
selection, chronology, residence, upper shadows, compiler feasibility, or a
K17 word.

