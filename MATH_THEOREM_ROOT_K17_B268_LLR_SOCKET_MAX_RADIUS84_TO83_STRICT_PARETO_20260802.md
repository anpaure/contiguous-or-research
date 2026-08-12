# K17 b268 LLR radius-one socket maxima at supplier deficiencies 84 and 83

Date: 2026-08-02

## Status and scope

This note proves two finite strict-Pareto steps on the authenticated b268 LLR
common-positive transfer face.  The optimization is exhaustive only over the
literal one-drop/one-add neighborhood of each stated parent.  It is not a
global matching theorem and it does not prove a K17 word.

The two socket marginals are deliberately different:

- phase 0 uses the literal b268 owner table
  `private_h_outer_materialized.tsv`, SHA
  `b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc`;
- phase 1 uses the root-aligned transported owner overlay
  `round047.s7.phase1.tsv`, SHA
  `736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058`.

Thus `both` below means positive in both of these declared marginal owner
tables.  It does not mean one shared occurrence-labelled carrier state.

The complete first-witness catalogue has 93,234 structural rows, 11,893
common-positive rows, SHA
`5d811072d2939e9e0b6dc9ab1990ba7c7f1a0856a072d848ec1bd928f9d3ef9d`,
and manifest SHA
`b6c2d85b39c92dd8f23819dbe6c4e64e39980e694ee33adb80f8dc12f4f64214`.

## Exhaustive bounded method

For a fixed 438-transfer parent matching:

1. enumerate every unselected common-positive edge;
2. retain exactly those edges conflicting with one selected edge, so replacing
   that edge gives a literal one-drop/one-add matching of size 438;
3. authenticate the parent Hall shore and recompute the exact neighborhood of
   every retained parent-Hall requirement under each changed row;
4. discard every move whose retained-shore Hall lower bound cannot reach the
   requested deficiency;
5. materialize every survivor and recompute the complete 6/9/4 supplier
   projection and maximum matching;
6. fully reprice all 7,395 short roles in literal-b268 phase 0 and transported
   s7 phase 1 for every table having the requested exact deficiency;
7. maximize lexicographically `(both,either,native_p0,transported_p1)`.

The Hall number in step 3 is only a lower bound.  No candidate is accepted
without steps 5 and 6.

## First step: strict deficiency 85 to socket-maximal deficiency 84

The parent has selected/table/projection-audit hashes

```text
0fb9a812e0afd7e9590d6ba690d2c3d7bee3f15a9462e3236b784a17de48b59f
ea0e8803b666dd51e4e5b073e50938ca5c508f3c2d7066f04ec2a0bd9f083aa8
038739aa6dad705ce48ac0aee0fba80d3eacd858dcf9c7de8a255e44a4460637
```

Its exact data are

```text
supplier rank/deficiency = 16813/85
zero heads              = 72
DM shore                = 98/13
(native p0,p1,both,either) = (3102,2259,1843,3518).
```

The radius-one census is:

| item | count |
|---|---:|
| all one-drop/one-add swaps | 9,347 |
| retained-Hall lower bound 84 | 284 |
| exact supplier deficiency 84 | 219 |
| exact `both >= 1843` | 218 |

The 284 exact supplier outcomes have deficiency counts
`84:219, 85:56, 86:8, 87:1`.  Among the 219 exact-deficiency-84 tables, the
`both` counts are `1842:1, 1843:199, 1844:19`.

The lexicographic maximum is obtained by removing edge 38,682 and adding edge
46,720.  Both use LMR row 16,006; only LR rows 14,133 and 15,981 change.

The resulting selected/table/projection-audit hashes are

```text
a91c42ffb2535437ea77d77dbd037605fdcf0611b062558f2bcca226e1ea6a3e
ba67651b9188bb9f8e5d20259a6e1063d018512331d20beab66edf671b962e69
4f862774a2fd23b4ef65ef896e900ba5157cd2ab20a888fa8cf7603932eccfdc
```

Its exact coordinates are

| coordinate | deficiency-85 parent | socket-max deficiency 84 | change |
|---|---:|---:|---:|
| native phase 0 | 3,102 | 3,104 | +2 |
| transported phase 1 | 2,259 | 2,260 | +1 |
| both | 1,843 | 1,844 | +1 |
| either | 3,518 | 3,520 | +2 |
| supplier rank | 16,813 | 16,814 | +1 |

The exact projection has 74,192 edges, zero-head count 72, shore 96/12, and
graph FNV64 `ed526341ea5fe6ff`.

The native and transported DNF hashes are

```text
e102a4430b0212ba2d69ff0e9ddfd75e9f31623dbfa04017a1403f7b5682133f
33edf6272a89040b966d9546d7decf61d612d19cfd0fe99030151cc818c54e8b
```

This table also weakly dominates the separate authoritative release-
compensation deficiency-84 fallback `(3102,2260,1844,3518)` at the same
supplier rank, improving native phase 0 and `either` by two.  It remains an
independent fallback rather than the root controller's parent.

## Second step: strict socket-max deficiency 84 to socket-max deficiency 83

Using the socket-maximal table above as the literal parent gives

```text
supplier rank/deficiency = 16814/84
zero heads              = 72
DM shore                = 96/12
(native p0,p1,both,either) = (3104,2260,1844,3520).
```

The next radius-one census is:

| item | count |
|---|---:|
| all one-drop/one-add swaps | 9,349 |
| retained-Hall lower bound 83 | 200 |
| exact supplier deficiency 83 | 140 |
| no regression in any parent socket coordinate | 125 |

The 200 exact supplier outcomes have deficiency counts
`83:140, 84:51, 85:8, 86:1`.  Among the 140 exact-deficiency-83 tables, the
`both` counts are `1843:1, 1844:130, 1845:9`.

The lexicographic maximum is attained by two candidates.  The lower
endpoint-portfolio rank removes edge 40,092 and adds edge 56,802.  Both use
LMR row 14,664; only LR rows 14,624 and 18,043 change.

The resulting selected/table/projection-audit hashes are

```text
d85aecb4c07606de79fcfad8c159ac74490f6b62630ba10683d21ec58bab132d
176043baf04bce4c5d3d9e9d36ee6feacb276dcb0bed78b98d7cfc9717611f8d
500b1302b0f5e9015c8678a09fd6710afe52b76cfc2f28ba00f53f3b57c2e3d5
```

Its exact coordinates are

| coordinate | socket-max deficiency 84 | socket-max deficiency 83 | change |
|---|---:|---:|---:|
| native phase 0 | 3,104 | 3,105 | +1 |
| transported phase 1 | 2,260 | 2,261 | +1 |
| both | 1,844 | 1,845 | +1 |
| either | 3,520 | 3,521 | +1 |
| supplier rank | 16,814 | 16,815 | +1 |

The exact projection has 74,200 edges, zero-head count 72, shore 93/10, and
graph FNV64 `50f3d20234c7e813`.

The native and transported DNF hashes are

```text
56b61f11e982a55383be4eb98a18e034baf96f060ddef8b0258cc2e2659d587b
66109e1c557a89bae39c3bb364edd97657df5164083b356e034e51d763ffa594
```

There is a secondary tradeoff at `(3104,2262,1844,3522)`, but it loses one
unit of `both`; the declared objective therefore selects
`(3105,2261,1845,3521)`.

## Endpoint and ticket-row scopes

For the deficiency-85 to 84 step, the added edge has zero changed-row and
stored first-witness endpoint masks and is canonical-eligible.

For the deficiency-84 to 83 step, edges 40,092 and 56,802 have zero
changed-row masks but stored first-witness endpoint mask 48.  Their stored
phase witnesses are

```text
native phase 0: q=7, flags 0/0, predecessor 15098, successor 14785
transported p1: q=7, flags 0/0, predecessor 14607, successor 14794.
```

Therefore the winning table preserves all named ticket rows, but the stored
new-edge witnesses are not private from that row bank.  No ticket-
composability claim follows.

In both strict steps, exact canonical-TSV comparison gives:

```text
1748 ticket records
7213 protected rows
876 table rows differing from literal b268
2 table rows differing from the immediate parent
0 protected rows differing from literal b268 or the immediate parent.
```

The ticket-row audit SHA is
`5a19c9ba039a0da2f2a72c0c2bc03c55163efa6ff6849cc70d2e5f12fbc4f951`.
This proves row identity only, not literal ticket replay.

After full simultaneous repricing, the selected-new-MR status is 410/438 in
`both` and 415/438 in `either` at both displayed winners.  Hence the 438
prospective common flags are not treated as simultaneous successes.

## Frozen bundles

Deficiency-84 socket maximum:

```text
scratch/root_k17_llr_transfer_price_20260802/
  def85_to84_socket_lane_v1/final_socket_max_def84/
MANIFEST.sha256
  57acfd43947b34ec881e3467ba685454f259cbba4bda42dad5185d1e630ca3b7
```

Key exact-ledger hashes are

```text
aba3689a0e4590f498c0390c0ecdc9ffaa0423682ce2f167d8e2909926fe1dc9  exact_socket_summary.tsv
4c19ffa2d3894faf8b6a5acb06b9b9621f6a15311a78216ee5bfd74f6999055c  exact_socket_ranking.tsv
144400f7e5628383fa391d9107be8175fd5c5e2270741798488e32022724a4e7  supplier_exact_summary.tsv
```

Deficiency-83 socket maximum:

```text
scratch/root_k17_llr_transfer_price_20260802/
  def84max_to83_socket_lane_v1/final_socket_max_def83/
MANIFEST.sha256
  75b8a33cfe72665cac7da3f2bea7b98ae56aa5e478fa83345f99a94982c7c6dc
```

Key exact-ledger hashes are

```text
dfc8bf64b7111ce5ac6b33cc40cba34daaf26eda6e7c35ec07cd5da20a6b0a97  exact_socket_summary.tsv
f21585a8690b31b4a38384236db76121b5f017bfbb52a150c0017b7460a3d8a5  exact_socket_ranking.tsv
7d33e47c82cee5d1dd08c8aa4b863e5cd94c8a916dce244f8491e260180716b6  supplier_exact_summary.tsv
d83455d1bf61f973aadb3c9eada9f8730f7fd93545596ffae52f16ffd43ea128  no_regression_from_def84max.tsv
```

H100 roots are, respectively,

```text
/home/amodo/or15/work/root_k17_llr_transfer_price_20260802/
  def85_to84_socket_lane_v1/
  def84max_to83_socket_lane_v1/
```

## Explicit nonclaims

The theorem does not claim:

- optimality outside the stated one-drop/one-add neighborhoods;
- an unrestricted Benders or global matching optimum;
- complete endpoint occurrence menus or simultaneous endpoint packing;
- a selected-parent supplier graph or residual outer perfect matching;
- ticket replay, private-bank composability, or one shared phase state;
- that transported phase 1 is an opened common carrier phase;
- chronology, residence, arbitrary upper shadows, common cap, compiler, or a
  K17 word.

The separate root floor controller had already reached lower supplier
deficiencies.  These socket-maximal tables are therefore frozen as independent
Pareto fallbacks, not asserted as the current global supplier incumbents.
