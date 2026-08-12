# Independent audit of the connected `K17` OPTIMAL-28 cycle, banks, and shadows

Date: 2026-07-31  
Status: **literal carrier PASS; complementary-bank residence FAIL**

## Verdict

The authenticated conditioned residual assignment
`scratch/ad_k17_opt28_residual_connected_bflow_20260731.json`
(SHA-256 `b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6`,
payload `a117a304f277a7746405814786fd3f593dffe5073443431582eb711641e7319a`)
independently expands to one literal cycle with:

```text
rank-nine owners                 24310 / 24310, all distinct
Johnson adjacencies              24310 / 24310
rank-eight lower-q1 colours      24310 / 24310, all distinct
port objects                      6435
bank transitions                     2
```

The raw independently reconstructed owner order is exactly equal, token for
token and without rotation or reversal, to the frozen decimal word of SHA-256
`a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa`.
The independent hexadecimal materialization has SHA-256
`5a1dbc412daec65babbcc17c8fe30ad62c13fcf8d4606d2c22bfa839b6654c24`.

The two linear banks are:

```text
bank             owners   strict D2<3   strict D3<4
marked             4108             0             0
complement        20202          1025           547
```

All `1025` complementary D2 violations have length two.  All `547`
complementary D3 violations have length three.  Therefore the connected
lower-rainbow carrier is genuine, but this fixed two-bank chronology is not
residence-clean and cannot be promoted as a passing two-bank construction.

## Exact all-layer shadow ledger

Lower depth `q` means the intersection of `q+1` consecutive cyclic owners.
Upper coverage uses every cyclic interval union and classifies it by rank.

```text
lower q                 1     2     3    4   5  6  7  8
holes                    0  1589  1033  297  28  0  0  0

upper target rank       10    11   12  13  14  15  16  17
holes                  1900   911  128   0   0   0   0   0
```

The maximum first-full cyclic upper interval width is `276`.  The exact
sorted missing-mask sets, not only their counts, are frozen in the shadow-hole
artifact.

## Independent reconstruction scope

The checker does not import either earlier materializer and does not trust a
saved census.  It reconstructs every `A/X/Y` macro owner from the authenticated
`K15` parent, rebuilds and compares all `5005` macro-forest components, replays
the selected 105-edge OPTIMAL-28 packet path, validates all `133` packet and
`4872` residual old-`U` owners, checks all `9744` residual incidences and port
demands, traverses the resulting port cycle, and then recomputes the bank and
shadow ledgers from the literal owners.

No solve was run.  No staircase, common-cap, compiler, universal-word, or
`B(17)` claim is made.

## Frozen artifacts

```text
scratch/audit_independent_k17_opt28_owner_cycle_banks_shadows_20260731.py
  SHA-256 c6834f6e6b168c7a639139b4c04ab01e1a7054018c429bceef3b231c5399e675

scratch/k17_opt28_independent_cycle_banks_shadows_20260731.audit.json
  SHA-256 f79d95403a8a55e820497766a12adf3aeb3ec6a8cbb04195a91895600157c6be
  payload  93a6bf299a5b055b3ad477a77857faf5305f4d6e1582c66f7b0f615dc82a28fe

scratch/k17_opt28_independent_owner_cycle_20260731.cycle
  SHA-256 5a1dbc412daec65babbcc17c8fe30ad62c13fcf8d4606d2c22bfa839b6654c24

scratch/k17_opt28_independent_marked_bank_20260731.word
  SHA-256 0bb73cc44dff4d1726efea7aebb7402536ffebd4b68c36e48fbf4903fb65893d

scratch/k17_opt28_independent_complement_bank_20260731.word
  SHA-256 f75bb11cafcfac375b67a6d64d2be6e5c8905b0b8fd26bbee9397b6f109aeb23

scratch/k17_opt28_independent_shadow_holes_20260731.json
  SHA-256 c418c4a3535dd9f1974ab6a5d111f3a079faf5c08f5c28ac079746981331688c
  payload  fdf5d1c2df1ec4175107600732afa31f4cc35d8f2a86b246415bdff4adc2553a
```

Deterministic replay command:

```text
python3 scratch/audit_independent_k17_opt28_owner_cycle_banks_shadows_20260731.py
```
