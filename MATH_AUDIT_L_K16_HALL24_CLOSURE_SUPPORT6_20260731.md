# K16 nested Hall-24 portal closures: complete actual-support-six census

Date: 2026-07-31  
Status: **complete scoped no-pass for arbitrary occurrence permutations of
actual support at most six on the 22 portal/protection closure rows**

## 1. Exact scope

Start from each of the four authenticated nested Hall-24 parents

```text
pass33  (L,l)=(16,9)
pass46  (L,l)=(16,13)
pass35  (L,l)=(18,9)
pass55  (L,l)=(18,15).
```

The exact profile-dependency closures are common to all four:

```text
J19536 : [6603,6611)
J19538 : [6604,6612)
J31749 : [12710,12717)
J31761 : [12716,12723)   (the protected 8000 cell).
```

Their union is the 22-row deck

```text
D = [6603,6612) union [12710,12723).
```

The census applies every occurrence-labelled permutation whose **actual
support** is a subset of `D` of size `s=2,3,4,5,6`.  It is not a single-cycle
restriction: every derangement on the selected support is included.  In
particular it contains the three-transposition alpha move

```text
[6608,6611) <-> [12714,12717).
```

No row outside `D` moves.  Thus this note is disjoint from the remote
`3846 -> 4653` compatibility-cycle lane.

## 2. Complete count

For support size `s`, the number of literal occurrence permutations is

\[
             {22\choose s},!s,
\]

where `!s` is the derangement number.  The exact per-parent rows are

| support | `!s` | formal | middle-exact | named `4e70` portal | portal + `8000` | portal + `8000` + all-upper |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 231 | 1 | 0 | 0 | 0 |
| 3 | 2 | 3,080 | 1 | 0 | 0 | 0 |
| 4 | 9 | 65,835 | 1 | 0 | 0 | 0 |
| 5 | 44 | 1,158,696 | 0 | 0 | 0 | 0 |
| 6 | 265 | 19,772,445 | 3 | 1 | 1 | 0 |

Hence the exact formal total is

```text
4 * (231 + 3080 + 65835 + 1158696 + 19772445)
  = 84,001,148.
```

The partition is identical in counts on all four parents.  The native table
also stores two order-sensitive 64-bit trace digests for every
parent/support row; the complete table has SHA-256
`d3f3f0e396423e1dd3e0fc07c29a1f028a0b456c41683d6bc34192aa52d3a235`.

## 3. Why the enumeration is exact

All 22 deck values are distinct, and none equals either exterior boundary
value at rows `6602,6612,12709,12723`.  Therefore every deck permutation
preserves exactly the three flats `6320,12869,12871` and hence preserves the
forced depth schedule.

For a selected support, only envelopes whose defining windows contain a
moved row can change.  Only target rows whose replay windows contain one of
those envelopes can then change status.  The native engine reconstructs each
such envelope as the literal intersection of its incoming target rows and
checks every affected target-row OR equation.  Every equation outside this
finite dependency set is unchanged.  This is an exact locality identity, not
a heuristic filter.

For every middle-exact row, the independent audit rebuilds the full 12,873-
row geometry.  It then checks the three literal named cells
`J19536,J19538,J31749`, rebuilds all proper-prefix incidences, checks all
65,535 mask ORs, and runs a fresh occurrence-labelled Hopcroft--Karp matching.
No stored matching or addition-only positive-cut shortcut is used.

## 4. The three support-six exact rows

The same three literal support-six permutations occur on every parent.  In
the notation `permutation[destination]=source` on the displayed sorted
positions, they are:

| positions | permutation | upper holes | named portal / `8000` | fresh matching |
|---|---|---|---|---:|
| `6606,6607,6608,6609,6610,12718` | `1,2,3,4,5,0` | `ce6a,ce6b,ce72` | none / none | 26307 |
| `6608,6609,6610,12714,12715,12716` | `3,4,5,0,1,2` | `4e79` | `4e70--J19538` / `8000--(6613)` | 26309 |
| `6608,6609,6610,12715,12716,12717` | `3,4,5,0,1,2` | none | none / none | 26307 |

Thus the alpha exchange is the **only** member on each parent that installs
one of the three named `4e70` portals while retaining an `8000` provider.  It
retains the original edge at physical singleton `[12720,12721)` with source
label `6613`, fully rematches to deficiency 23 with `(Z,S)=(10,13)`, and owes
exactly the one upper mask `4e79`.

The phrase “zero exact+upper rows” in this scoped result means zero rows after
the required named-portal-and-`8000` gate.  There are exact all-upper rows
without those lower providers; they are not candidate escapes.

## 5. Full-rematch diagnostic and consequence

There are six middle-exact nonidentity rows per parent, 24 total.  The
independent audit fully rematches all 24, including rows rejected before the
production Hall gate.  Its exact histogram is

```text
matching 26306 :  8
matching 26307 : 12
matching 26309 :  4.
```

The upper-hole-set histogram is

```text
none             : 16
4e79             :  4
ce6a,ce6b,ce72   :  4.
```

The four matching-26309 rows are precisely the four alpha rows, and all four
owe `4e79`.  Consequently **no member reaches the all-upper full-Hall
candidate gate**.  The matching-26309 computation is a diagnostic fact about
the inadmissible alpha states, not a K16 construction.

## 6. Independent audit and resources

The independent Python audit reconstructs and fully rematches all 24 exact
rows and replays 180 deterministic negatives (`160` middle-inexact and `20`
exact-without-named-portal).

It does **not** claim a second enumeration of all 84,001,148 rows.  Exhaustive
partition authority is the native trace together with the exact
`binom(22,s)!s` cardinalities; the independent layer authenticates every
positive row and samples both populated negative stages.  Its payload is

```text
8d0ca73b46ed1c4c31eeb175ce0eb0286142fd83ca587d68752d958904a1bb85.
```

The complete 84,001,148-row native enumeration ran locally as a genuinely
light bounded replay: exit 0, 9.150516 seconds wall, 9.107229 seconds user,
13,369,344 bytes maximum RSS on Darwin 24.6.0 arm64.  It used no SSH and no
H100.  A repeated resource-measured run reproduced all four TSV hashes
exactly.  The independent 24-word full-rematch audit took about 37 seconds
locally; neither job was a broad search.

## 7. Frozen artifacts

```text
scratch/laneL_k16_hall24_closure_support6_census_20260731.cpp
  SHA-256 dd4142035ec752705da43006ded7a184ad0f88eb4e4610c39616e7bcb551fa3b

scratch/audit_laneL_k16_hall24_closure_support6_20260731.py
  SHA-256 9ab22707de809da828fa088045db7acf9f199e8a8ed1ebadcf54e7ef989b11d3

scratch/laneL_k16_hall24_closure_support6_20260731.summary.tsv
  SHA-256 d3f3f0e396423e1dd3e0fc07c29a1f028a0b456c41683d6bc34192aa52d3a235

scratch/laneL_k16_hall24_closure_support6_20260731.survivors.tsv
  SHA-256 b9f8f913da97746d9154a06da620b15ad25b8747ba214387bf0d77104b0a95c5

scratch/laneL_k16_hall24_closure_support6_20260731.exact.tsv
  SHA-256 71123d8a3ba4d621d5c0dd3b1d8ade7aa4145f7d8ae592660f42971e5ccf49ce

scratch/laneL_k16_hall24_closure_support6_20260731.samples.tsv
  SHA-256 77f13aed3dca29f9e0d2a11fe3c867b5c0f3388c8c77b479469abea0b3342fff

scratch/laneL_k16_hall24_closure_support6_20260731.resource.json
  SHA-256 10266654b454c0bdfa3aeb3f5edf3b49d7b25547fb23bc26d1cd3b6abcbf72e6

scratch/laneL_k16_hall24_closure_support6_20260731.audit.json
  SHA-256 88df8f26573dd4db9711cb66d2a970ab00d248c82875536f76880b026f11a1dd
```

This closes only the stated 22-row, actual-support-at-most-six family.  It
does not exclude support seven or larger, donor rows outside the four closure
sets, different carrier parents, or a remote compatibility braid.
