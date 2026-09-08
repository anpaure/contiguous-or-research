# K17 b268 LLR socket-max radius-one chain from deficiency 83 to 77

## Scope and authenticated parent

Fix the canonical protected b268 transfer table with 438 selected transfers,
exact supplier matching rank `16815/16898`, deficiency 83, zero-head count 72,
and Hall shore `93/10`.  Its selected/table/projection hashes are

```text
d85aecb4c07606de79fcfad8c159ac74490f6b62630ba10683d21ec58bab132d
176043baf04bce4c5d3d9e9d36ee6feacb276dcb0bed78b98d7cfc9717611f8d
500b1302b0f5e9015c8678a09fd6710afe52b76cfc2f28ba00f53f3b57c2e3d5
```

Its exact socket tuple, written throughout as

```text
(native b268 phase 0, transported s7 phase 1, both, either),
```

is `(3105,2261,1845,3521)`.  This hash-authenticated tuple supersedes the
weaker incoming branch label `(3105,2260,1845,3520)`.

At each stage below, enumerate the complete one-drop/one-add `SWAP1` face in
the 11,893-edge b268 common-positive LLR catalogue.  For every swap, recompute
the exact neighborhood of the retained current Hall shore.  The resulting
shore deficiency is a valid lower bound on the candidate's exact supplier
deficiency.  The complete move ledger and the materialized portfolio have
identical target-bound swap keys.

Every target-bound candidate is materialized and replayed through the exact
complete supplier projection.  Every true target-deficiency table is then
repriced over all 7,395 short roles in both declared marginals.  Candidates
are ranked lexicographically by

```text
(both, either, native phase 0, transported phase 1),
```

with portfolio ID as the deterministic final tie-break.  Several displayed
maxima are tied; `canonical` below means that deterministic choice, not a
uniqueness assertion.

## Exhaustive stage ledger

| target deficiency | all `SWAP1` | target Hall-bound | exact target | coordinatewise no-regression | chosen exchange | supplier rank; zero; shore | socket tuple |
|---:|---:|---:|---:|---:|---|---|---|
| 82 | 9,349 | 136 | 122 | 108 | `-32928 +58755` | 16816; 71; 92/10 | `(3106,2261,1846,3521)` |
| 81 | 9,350 | 124 | 112 | 100 | `-63751 +67039` | 16817; 70; 91/10 | `(3107,2261,1847,3521)` |
| 80 | 9,351 | 112 | 101 | 90 | `-49888 +51689` | 16818; 70; 89/9 | `(3107,2262,1848,3521)` |
| 79 | 9,351 | 9 | 6 | 6 | `-35565 +44315` | 16819; 69; 88/9 | `(3107,2262,1848,3521)` |
| 78 | 9,353 | 7 | 4 | 4 | `-32175 +62175` | 16820; 68; 88/10 | `(3107,2262,1848,3521)` |
| 77 | 9,354 | 6 | 3 | 3 | `-32995 +33445` | 16821; 67; 87/10 | `(3107,2262,1848,3521)` |
| 76 | 9,357 | 2 | 0 | 0 | none | exact candidates have deficiencies 78 and 77 | none |

Thus every accepted step strictly improves supplier rank by one and regresses
no socket coordinate.  The first three steps also improve socket coordinates;
the last three preserve the tuple.  This is a strict-Pareto independent
fallback through deficiency 77.

The deficiency-76 terminal row is an exact negative certificate for the
declared face from the selected canonical deficiency-77 parent.  Its only two
target-Hall-bound swaps are

```text
-63345 +63384  -> exact matching 16820, deficiency 78,
                  zero 66, shore 91/13, projection edges 74232;
-63345 +64554  -> exact matching 16821, deficiency 77,
                  zero 66, shore 88/11, projection edges 74233.
```

Every other `SWAP1` has retained-shore lower bound at least 77.  Hence no
one-drop/one-add swap from this frozen parent attains deficiency 76.  This is
not a statement about a different tied deficiency-77 parent, a free addition,
a 2x2 alternating cycle, radius two or larger, an unrestricted matching, or a
global recoupling.

## Endpoint and protected-row footprints

The endpoint catalogue stores only the first lexicographic phase witness.
For the six accepted added edges, the stored changed-row and endpoint masks
against the declared protected bank are:

| target | added edge | changed-row mask | endpoint mask | endpoint-safe/canonical-eligible |
|---:|---:|---:|---:|---|
| 82 | 58755 | 0 | 0 | yes/yes |
| 81 | 67039 | 0 | 0 | yes/yes |
| 80 | 51689 | 0 | 36 | no/no |
| 79 | 44315 | 0 | 0 | yes/yes |
| 78 | 62175 | 0 | 60 | no/no |
| 77 | 33445 | 0 | 40 | no/no |

These masks describe only the stored witnesses.  They neither exhaust
occurrence menus nor certify simultaneous endpoint-resource packing.

For every accepted winner, the sorted union of the five ticket fields has
exactly 7,213 row IDs.  Exact canonical-TSV extraction and byte comparison
against literal b268 and against the immediate parent finds zero protected
differences.  Every winner changes exactly two nonprotected table rows from
its parent and 876 total rows from b268.  The common protected-row extract has
SHA

```text
a8b999f8e3c5977587232f3e561d7075c023e6cca265bb6c2040d21f85a942ea.
```

This is row identity only.  No ticket was replayed on these tables, and no
private-bank, occurrence-packing, or selected-parent composability result
follows.

## Exact winner hashes

The selected/table/projection hashes are:

| deficiency | selected | table | projection audit |
|---:|---|---|---|
| 82 | `1e523aea1f9bc83675dff2362f3890809b7678c570c608e30494c1869a52265b` | `ce04e9a5f7ebc2f5ced75ca7a033309a648e17f82edc3109b25da190beff3e5c` | `ef3daa37b30187857d6164933d20b16f0e7a7f084480d4c1373ed1e28e143aa9` |
| 81 | `c7ed725311d04872172580527e5dab55ee0071faf7ad9c7d7123577b88abc1da` | `35dd4e140120f067bb8caaddbfa10df8aa6f86db64ddc44de0d8428ba7532085` | `1198b5c17bd5550b3b4583035c21cd40860f828de8937e0ffabb0a8d77759408` |
| 80 | `8944a63d5ee9dbb8347cdb4f32b176dd650ce18427d3077bd1febe657dfdce99` | `12e12870d66915fda4d7e98c2810a87e1b7b6434ca5a9bbad72fde2ddd334ff8` | `221542df05a9f574da9cacaed621224fad19b7fca98be2cb8af5c1852ed24e92` |
| 79 | `a00c6b0fc71964ba93b5b8a74ee30ffe8e96d28df0ca625885623cf81e35e3b4` | `28efad16242365efde09b471f2229812b781b6aa5a1f0f1637d880f7ea0d2ecb` | `f4780aa59b6f0ae0456eda1149ecf94aab01bdb3cff3e3d58b1c58ef4ba25bca` |
| 78 | `90bd89bbc44a8f42fd1006ef4ea5247dfed9bcfa1372ddfce3d84ca3efa81ec3` | `1f6b23a21f8e07f1d137eef1b08143cd94911851c31dc03236ac80f97868669b` | `b735ba20807f082c69af9f6f8f694f2da94ea660fde00e6f5d162c0b44b3b3ec` |
| 77 | `171437939d3966532a16fa712772734a5b0928d2214bc005bec052b0db05d614` | `61502d2eb7ef7c4666158bb2124e2e0e834bd5487b262b3a99f7b74a8fe411aa` | `90a7f1f270327bafdfe57190c5d5ff6641a788d2fc33bd174a54357fc9decbda` |

## Frozen stage roots and manifests

The persistent H100 base is

```text
/home/amodo/or15/work/root_k17_llr_transfer_price_20260802/
  def83max_socket_chain_v1/
```

The stage-manifest hashes are

```text
def82 a436688752bdb6ded04fcd488d54a58a55e4aa9c4696e6d5c8be96ac7fa0d065
def81 30d8478bcf61b002819acb6c51519d712a2396fc82e267f9ddb8737e7bb8cd51
def80 43d6b97b84f363219fdf7a7341a714be4355f4de544025ad2ff7a6d6fcba536d
def79 0ddea2b993f97511abcea09f57f947acb55d0ab212edcffc99e0e1868962d5df
def78 da349de24993617bfd1903adf71452cb08a0033220411af0d467bb5c9ec34b7a
def77 e2200fa0f2be1f94c4a95612151d58d7261a0540b2012927406c179a5a92c9e4
def76 7f019d033a41e5b6bb113b9237957538e98ed6950c7c796a8e82a93add987fba
```

All generic manifests and the terminal manifest were independently replayed
with no missing, duplicate, or extra paths.  The compact local bundle is

```text
scratch/root_k17_llr_transfer_price_20260802/
  def83max_to77_socket_chain_v1/
```

Its own `MANIFEST.sha256` authenticates the copied winners, complete move and
portfolio ledgers, exact supplier/socket summaries, terminal audits, and
source scripts.  The copied stage manifests authenticate the larger complete
H100 roots, not merely the compact local subset.

## Marginal scope, supersession, and explicit nonclaims

`native phase 0` means the literal b268 owner table.  `transported phase 1`
means only the root-aligned `round047.s7.phase1` owner overlay.  `both` is the
rowwise intersection of these two marginal-positive censuses; it is not a
common occurrence-labelled witness or one simultaneous phase state.

This chain is now an independent historical fallback.  Mainline work first
superseded it with a fully occurrence-pinned all-27 parent reported at exact
supplier deficiency 22 and final SHA prefix `dd608ae5`.  A later root-subset
search reported a provisional deficiency-21 table obtained by deleting
actions 12, 15, and 16.  The canonical best subset and its hashes are not
frozen in this theorem.  No further descent from this old fixed-parent chain
is authorized or competitive, and no socket-max computation should use the
stale all-27 edge IDs.  Rebase remains paused until the canonical best-subset
parent and a fresh parent-specific catalogue are authenticated.

This theorem does not claim:

- optimality outside the declared one-drop/one-add `SWAP1` face;
- closure from another tied parent or under a larger-radius exchange;
- completeness of endpoint occurrence menus or endpoint packing;
- a selected-parent supplier graph or residual outer perfect matching;
- literal ticket replay, private-bank composability, or a shared phase state;
- transported phase 1 as an opened common carrier phase;
- unrestricted Benders/global optimality, chronology, residence, arbitrary
  upper shadows, common cap, compiler, or a K17 word.
