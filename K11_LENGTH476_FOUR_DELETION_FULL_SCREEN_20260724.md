# Exact full four-deletion plus 15-append screen at length 476

## Scope

Start with the fixed 465-entry word in
`k11_upper549_natural_array.txt`. Delete any four entries, retain all other
entries in their original order, and append exactly 15 nonzero 11-bit masks.
Every completed word in this repair neighborhood has length

```text
465 - 4 + 15 = 476.
```

This report screens all

```text
C(465,4) = 1,923,014,940
```

deletion quadruples. It is a theorem about this fixed-prefix repair
neighborhood, not a lower bound for arbitrary length-476 words and not a
proof that `nu(11)>476`.

## Structural screen

For a retained prefix, every target absent from that prefix needs a witness
ending at one of the 15 appended positions. The suffix-OR values at one
endpoint form an inclusion chain. Consequently, the missing-mask poset must
have width at most 15.

The optimized scanner first applies the rank-layer special case: no rank may
contain more than 15 missing masks. It computes the exact poset width by
maximum bipartite matching only for rank-feasible branches.

The complete ledger is

```text
total branches          1,923,014,940
rank-cap rejected       1,744,611,799
rank-feasible             178,403,141
width <= 15 survivors             790
```

Thus 1,923,014,150 branches are eliminated by a globally necessary
condition. Every survivor has width exactly 15; in particular, no branch in
this complete neighborhood passes the corresponding 14-append screen.

The maximum missing-rank count distribution over all branches is

```text
10:106, 11:80531, 12:1795550, 13:12697973, 14:47622143,
15:116206838, 16:207124203, 17:289225768, 18:332668931,
19:317398136, 20:253972419, 21:171506432, 22:97928484,
23:47185229, 24:19061930, 25:6380862, 26:1730070,
27:367164, 28:56525, 29:5420, 30:226.
```

The exact width distribution among the 178,403,141 rank-feasible branches
is

```text
width 15          790
width 16       23,901
width 17      285,337
width 18    1,820,193
width 19    7,132,201
width 20   18,480,719
width 21   33,215,183
width 22   42,288,500
width 23   38,217,795
width 24   24,089,664
width 25   10,091,256
width 26    2,496,549
width 27      260,959
width 28           94
```

The two distributions sum respectively to 1,923,014,940 and 178,403,141.

## The 790 survivors

Exactly 774 survivors contain deleted index 102. After sorting each deletion
quadruple, those 774 rows agree exactly with the earlier exhaustive
fixed-102 result. The normalized survivor-ledger SHA-256 on both sides is

```text
4ea65707fd0f399294e4eb8205690dbeccb8354d4dcfc5b487a559c12683b9c5
```

The remaining 16 deletion quadruples are

```text
0,1,2,150              missing 26   max-rank count 15
0,272,275,276          missing 27   max-rank count 13
272,275,276,462        missing 28   max-rank count 13
272,275,276,464        missing 29   max-rank count 12
118,119,120,121        missing 30   max-rank count 15
120,272,275,276        missing 31   max-rank count 12
272,275,276,444        missing 31   max-rank count 12
115,116,117,118        missing 32   max-rank count 15
117,118,119,120        missing 32   max-rank count 14
178,272,275,276        missing 32   max-rank count 13
180,272,275,276        missing 32   max-rank count 12
267,272,275,276        missing 32   max-rank count 12
272,275,276,394        missing 32   max-rank count 12
272,275,276,432        missing 32   max-rank count 13
117,118,119,121        missing 34   max-rank count 15
179,272,275,276        missing 35   max-rank count 14
```

Every one has exact width 15. The complete 790-row survivor list, including
deleted values and missing-rank profiles, is archived in

```text
scratch/k11_length476_four_deletion_full_20260723/full_scan_primary.out
```

The missing-family-size distribution over the survivors is

```text
24:1, 25:1, 26:4, 27:4, 28:16, 29:19, 30:32, 31:45,
32:76, 33:80, 34:80, 35:94, 36:113, 37:88, 38:55,
39:32, 40:27, 41:15, 42:6, 43:2.
```

Their maximum missing-rank count distribution is

```text
12:80, 13:274, 14:316, 15:120.
```

## Validation

The primary scanner uses generation-stamped suffix-OR chains, adjacent
deduplication of the monotone suffix chain, a rank-first filter, and an exact
augmenting-path matcher. On 14 local workers the full scan used 1,529.55
seconds wall time, 14,285.99 seconds user CPU, and about 11 MB maximum
resident memory.

Before the full run, its fixed-index-102 mode reproduced all 16,542,064
branches, the complete width distribution, and the 774-row output of the
earlier fixed-102 scan byte for byte.

A separate direct audit then recomputed all physical interval ORs
quadratically for every one of the 790 listed survivors and recomputed their
widths with a separate matcher. It returned

```text
verified=790 containing_102=774 outside_102=16
width_distribution=15:790
```

with the exact missing-size and maximum-rank distributions displayed above.

A second independently written all-branch aggregate scanner uses sorted and
uniquified raw suffix-OR rows and a layered maximum matcher.  It did not
produce a result: an execution-session run was externally terminated after
958.36 wall seconds and 12,200.66 user-CPU seconds, and a detached rerun was
externally terminated after 5,246.79 wall seconds and 49,529.05 user-CPU
seconds.  Both terminations occurred before the scanner's atomic final
write, with negligible memory use and no crash report.  Consequently this
report makes no independent all-branch aggregate-agreement claim.  Its
exhaustive aggregate counts come from the primary scan; the fixed-102 slice
and all 790 reported survivors have the separate exact checks above.

## Exact completion proofs for all 790 survivors

Every structural survivor was independently regenerated with the exact
last-occurrence recency append encoding.  It simulates the 15 appended
nonzero masks, requires every missing target to occur as a genuine suffix OR,
and adds the logically redundant endpoint-chain/maximum-antichain clauses.
This implementation shares no interval-selector circuit with the original
production append solver.

All 790 formulas returned UNSAT, and every binary proof was independently
checked by the local `drat-trim` build:

```text
family                 branches  verified  failures/SAT/timeouts
contains index 102          774       774                       0
outside index 102            16        16                       0
total                       790       790                       0
```

For the 774 fixed-102 formulas, the four-worker proof batch used 694.953
seconds and produced 372,918,129 CNF bytes and 1,557,319,713 proof bytes.
For the 16 exceptional formulas, the two-worker batch used 14.724 seconds
and produced 6,829,160 CNF bytes and 36,503,829 proof bytes.  There are
exactly 790 status files containing `VERIFIED`, and every corresponding
verification log contains `s VERIFIED`.

The aggregate proof ledgers are

```text
231190748bda26a5c3f74a1ff5c8ab7a10d1bd3f3209938f9d78333a369af8fc  fixed102 recency_proofs_batch.out
b402baf7f5e032f22969d0b1c2b3f712ad779d84ef2a4ceef44881326adb2e16  fixed102 recency_proofs/MANIFEST.sha256
3066bc0291c3da6ec6afd27dc5ae31b7767d9804246cd78d3f26048df78a7eaf  non102_recency_proofs_batch.out
ada712b40ee72c459710bbf887c481e634de5754987cd94823b94191ce2de2df  non102_recency_proofs/MANIFEST.sha256
```

The proof archives are under

```text
scratch/k11_length476_four_deletion_fixed102_20260723/recency_proofs/
scratch/k11_length476_four_deletion_full_20260723/non102_recency_proofs/
```

The encoding theorem, finite truth-table checks, direct missing-family
recomputations, proof inventories, and status-ledger comparisons are audited
in `APPEND_RECENCY_CIRCUIT_AUDIT.md`.

## Reproducible artifacts

```text
882d51e85777ea86a22890ab9e2eafbdfd473af13ce0a3dc813449147a0e34a6  scan_all_four_deletions_primary.cpp
aae14b458bbb3dbb22ee42daa0e2e3b2ea26d6fbea026b693209b9ff29cc05f1  scan_all_four_deletions_independent.cpp
c61b9d7943c84e4434439c317be09d5bf5740ae7952c3450ccf2a8b69824ce7b  audit_all_four_deletion_survivors.cpp
bf9905eb545eb73ebb783bcdce36e20250a04f5fd7a27b02aff9c7af3cbc7f86  full_scan_primary.out
556987f8a0871ffdcd69419f4e43bcb817ab225ca7b102f35dab2b0c6ad17e00  full_scan_primary.time
b6dbe473ddfba592e3a3f94d91a0beb21f1491f3b3fe6319da1037b85902e070  fixed102_reproduction.out
424fdfdddbba1891aeee925ed166833a03fd78efda6619e6d4a94f45836accdb  fixed102_reproduction.time
b5643ac0cd68aa8a48f108b53acd799644322bf1138581811015d5c33ce2f4da  direct_all_survivors_audit.out
acfc2f6d786ad40cebf04c52210e6b7eee57874a673e922671bc61548a0231fa  direct_all_survivors_audit.time
8ac00a2b6dea6b601767688ee6ac1d1e8becd02526bc71c91fdd913b1576c64a  full_scan_independent.aborted_958s.time
63f5292dc7281a843175e4d714fb4ef5bc6e2485d1c7c3b4c0baafe1d55d5fdf  full_scan_independent.time (second aborted run)
```

The two scanner sources and all output files are under

```text
scratch/k11_length476_four_deletion_full_20260723/
```

## Mathematical status

Width at most 15 is necessary, not sufficient, for a valid 15-entry append
completion.  The exact independently checked formulas eliminate all 790
width survivors.  Consequently no word in this complete fixed-prefix
four-deletion plus 15-append neighborhood is universal.

This remains a restricted-neighborhood theorem.  It says nothing about an
unrelated length-476 word or about the conjectural equality `nu(11)=465`.
