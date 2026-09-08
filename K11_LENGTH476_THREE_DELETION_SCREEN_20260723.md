# Exact screen of the 465-prefix three-deletion plus 14-append neighborhood

## Scope

Start with the fixed 465-entry word in
`k11_upper549_natural_array.txt`. Delete any three entries, retain all other
entries in their original order, and append exactly 14 nonzero 11-bit masks.
Every resulting completed word has length

```text
465 - 3 + 14 = 476.
```

This report screens all

```text
C(465,3) = 16,649,480
```

choices of the deleted positions. It is a theorem about this fixed-prefix
repair neighborhood, not a lower bound for arbitrary length-476 words and
not a proof that `nu(11)>476`.

## Structural screen

For a fixed retained prefix, every target absent from that prefix needs a
witness ending at one of the 14 appended positions. The suffix OR values at
one endpoint form an inclusion chain. Consequently the missing-mask poset
must have width at most 14.

The implementation first applies the cheaper rank-layer special case. It
then computes the exact width by maximum matching in the bipartite strict-
inclusion graph for every rank-feasible branch.

The complete ledger is

```text
total branches        16,649,480
rank-cap rejected     14,720,119
rank-feasible          1,929,361
width <= 14 survivors        159
```

The exact width distribution among the 1,929,361 rank-feasible branches is

```text
width 14       159
width 15     3,332
width 16    27,584
width 17   117,761
width 18   296,094
width 19   474,431
width 20   496,076
width 21   336,542
width 22   141,399
width 23    32,902
width 24     3,081
```

Thus exactly 159 branches survive the complete scalar endpoint-chain
screen, and every survivor has width exactly 14.

## Structure of the 159 survivors

Of the survivors, 158 contain deleted index 102. They are exactly index 102
together with the 158 pairs surviving the independently checked fixed-102
two-additional-deletion scan. Their missing-count distribution, together
with the one exceptional branch below, is

```text
missing masks  22  23  24  25  26  27  28  29  30  31  32  33  34  35
branches        2   1   3   9  12  14  14  28  31  21   9   8   4   3
```

The complete 159-row list, including deleted values, missing counts, widths,
and missing-rank profiles, is archived in
`scratch/k11_length476_three_deletion_screen_20260723/full_scan_primary.out`.

The assertion that every survivor contains index 102 is false by exactly
one branch:

```text
deleted indices       272, 275, 276
deleted values         136, 516, 320
missing masks                    25
maximum matching                 11
missing-poset width              14
rank profile       5:6, 6:5, 7:12, 8:2
```

Its missing masks are

```text
155 219 251 493 607 782 838 846 906 910 941 956 958 1267 1364
1468 1694 1763 1860 1862 1876 1884 1946 1990 1998
```

One explicit maximum antichain is

```text
251 493 607 846 910 941 956 1267 1468 1694 1763 1884 1946 1990
```

Pairwise incomparability and matching optimality were checked
independently.

## Independent full-scan agreement

Two independently written full scanners agree exactly.

Their reproducible sources are

```text
scratch/k11_length476_three_deletion_screen_20260723/scan_all_triple_deletions_primary.cpp
scratch/k11_length476_three_deletion_screen_20260723/scan_all_triple_deletions_independent.cpp
```

They can be rebuilt and run with

```sh
g++ -O3 -march=native -std=c++20 -pthread \
  scratch/k11_length476_three_deletion_screen_20260723/scan_all_triple_deletions_primary.cpp \
  -o /tmp/scan_all_triple_primary
/tmp/scan_all_triple_primary k11_upper549_natural_array.txt 12

g++ -O3 -march=native -std=c++20 -pthread \
  scratch/k11_length476_three_deletion_screen_20260723/scan_all_triple_deletions_independent.cpp \
  -o /tmp/scan_all_triple_independent
/tmp/scan_all_triple_independent k11_upper549_natural_array.txt 10
```

The primary scanner uses generation-stamped suffix-OR chains, adjacent
chain deduplication, a rank-first filter, and a simple augmenting-path
matcher. On 12 local workers it used 9.12 seconds wall time, 88.75 seconds
user CPU, and about 11 MB maximum resident memory.

The second scanner instead sorts and uniquifies every suffix-OR row and uses
a layered maximum matcher. It independently reproduced all aggregate counts:

```text
branches=16649480
rank_reject=14720119
rank_feasible=1929361
survivors=159
widths=14:159,15:3332,16:27584,17:117761,18:296094,
       19:474431,20:496076,21:336542,22:141399,23:32902,24:3081
```

Direct quadratic interval enumeration separately rechecked the missing
families and widths of all 159 survivors.

The durable scan artifacts have SHA-256 hashes

```text
7e16ddfd535b7e288322e3f6c4ba75b699542a5b40519a451ba5bbc551e79048  scan_all_triple_deletions_primary.cpp
20132b8e81c91c560575f436980541274ba31069ab482de785cf603d3fd01a4b  scan_all_triple_deletions_independent.cpp
fa71ca38a1c6963cdccb3426252dfea0ea80e7ce0a7dbc85b6a060383817d61c  full_scan_primary.out
2ba32177f2732b6c94e0a6f19219e9992d7902859e0088beceef84f20b860bc8  full_scan_primary.time
293ff4b4eba50b0f93a98d8b016a3fd335c28b92d815a5a797fe98e1d75038bc  full_scan_independent.out
```

Fresh recompilation reproduced `full_scan_primary.out` and
`full_scan_independent.out` byte for byte.

## Certified exceptional branch

The unique survivor not containing index 102 was encoded with the audited
full endpoint-chain append formula. Its exact inventory was

```text
variables                              3,198
clauses                              234,999
witness candidates                     2,694
endpoint flags                            350
rank endpoint-distinctness clauses      1,288
cross-rank incomparability clauses       2,492
saturated-antichain supports                 14
```

CaDiCaL returned UNSAT. An independent binary-DRAT check then reported

```text
s VERIFIED
3,581,787 resolution steps
142.854 seconds verification time
```

The archived certificate hashes are

```text
a5b209c05be73216559cd795253033b61fbe2c6a93059153a8323889c53cf241  triple_272_275_276.cnf
c83c29011d17e92c99b3aa2101155d62d8dfd0ae3a6429fccef22bb9c0c53444  triple_272_275_276.dratb
f127ba88c258f406fa743126e9a2694549e16f70da3b0f46a442337d94f89250  triple_272_275_276_drat_trim.log
386f5f4358280c4df76f23818a240dc8128d2be9c6e35fc9a064bb1c21116aba  generator.log
```

They are stored under
`scratch/k11_length476_three_deletion_screen_20260723/exception_272_275_276/`.

## Certified status of the 158 index-102 branches

All 158 branches were regenerated with the independent exact last-occurrence
recency encoding.  CaDiCaL returned UNSAT for every formula, and the local
`drat-trim` build independently reported `s VERIFIED` for every binary proof.
The bounded four-worker batch completed in 45.344 seconds and produced

```text
branches                         158
verified                         158
failures/timeouts/SAT              0
aggregate CNF bytes       58,150,617
aggregate proof bytes    214,067,333
```

The archived batch and aggregate-manifest hashes are

```text
497087026d16bd0c9364ff798ebe3463b5aa1aec2a3da3846ee172ade785103f  fixed102_recency_proofs_batch.out
2e30ea806ccb47fcc48e1e5c231c15424fc4d53f4957460ec6c7bf19a6699b66  fixed102_recency_proofs/MANIFEST.sha256
```

There are exactly 158 `.status` files, all containing `VERIFIED`; every
corresponding verifier log contains `s VERIFIED`.  The CNFs, binary proofs,
solver logs, verifier logs, statuses, and per-branch manifests are under

```text
scratch/k11_length476_three_deletion_screen_20260723/fixed102_recency_proofs/
```

The recency generator is independent of the original interval-selector
encoding.  It is `scratch/append_completion_recency_sat.py`, SHA-256

```text
441f2065e5e13c1c8f7fa68c0e4a9c8ec11e71a7aa24b14b3f7c0dea5ac82b80.
```

Together with the independently verified exceptional branch, all 159 exact
width survivors are now proof-certified UNSAT.  Hence the complete rigorous
conclusion is:

- 16,649,321 branches are eliminated structurally by rank or exact width;
- all 159 remaining branches are eliminated by archived, independently
  verified UNSAT proofs;
- therefore no word in this fixed-prefix three-deletion plus 14-append
  neighborhood has length 476 and covers all nonzero masks.

Nothing in this report excludes a length-476 word outside the stated
fixed-prefix three-deletion-and-append neighborhood.
