# Audit of the K16 adjacent-OR braid catalogues

Date: 2026-07-30  
Lane: R  
Status: exact catalogue and literal-word replay PASS; several advertised
no-go scopes corrected

## 1. Frozen objects and independent audit

The independent checker is

```text
scratch/audit_r_k16_adjacent_or_braid_artifacts_20260730.py
SHA256 43b37fa778fa305fe133182ef1918b39f15c04c03be8bc39affc80c941a861e5
```

It was run on one capped H100 CPU and produced

```text
scratch/k16_adjacent_or_braid_independent_20260730.audit.json
SHA256 1309ea7a98d7ce445d8800f0a6ffec62c98445369804f76da40fc9f9c1671155
status PASS_EXACT_CATALOGUE_AND_WORD_REPLAY
```

The checker pins by SHA256 the four supplied audits, their three C++ search
sources, both source words, and the saved candidate words.  It independently
recomputes all contiguous-OR multiplicities, regenerates every serving-braid
catalogue algebraically, applies the advertised debt filters, and replays the
literal words against all 65,535 nonempty masks.

The four supplied audit hashes are respectively

```text
append blocker   5fc2275124fe53ec796d2cb245e5ceb4d608f1c7551a373dc7edcb47dffda119
layer 2          fc7e08ed70ea46d72c11b262912647891584f4f7b4cad04540dc1709e250d4c1
layer 3          ef2e986e6c20d4a07a6e02a9ae260dafd384daa4f98726dbd10bbf1694b02d99
five-phase       54d647a82f4bd9824467f301f03e4592eb75dddf39b6a2a360d3e0b4dd2075ec
```

## 2. The exact adjacent-OR lemma

Let `w` be a word and replace adjacent cells `(w_q,w_{q+1})` by nonzero
`(x,y)` with

```text
x OR y = w_q OR w_{q+1}.
```

Then every interval containing both changed cells has the same OR before and
after the replacement, and every interval containing neither is unchanged.
Consequently only intervals ending at `q` or beginning at `q+1` can change.

If a previously missing target `T` is created, one of those exposed intervals
has OR `T`.  Enumerating all left and right contexts and all nonzero
decompositions of the fixed pair OR therefore enumerates every preserved-OR
adjacent braid which creates `T`.

In particular, if `M` is the current hole set, the union of the serving
catalogues for `T in M` contains every single adjacent braid which strictly
reduces the number of holes: strict reduction necessarily fills at least one
member of `M`.  This proves completeness of each *one-step layer search* for
strict improvement.  It does not prove completeness of neutral routing
followed by a later improving braid.

## 3. Exact replay results

### 3.1 Append-blocker catalogue

For

```text
scratch/k16_append0200_12874_onehole.word
SHA256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

the sole hole is `H=0x287d` and `A=0xa879` has multiplicity one.  There are
exactly 2,558 adjacent braids which create another `A` witness avoiding portal
position 6440.  No such braid is debt-free while retaining at least two `A`
witnesses.  Exactly 514 have at most four preportal debts, giving `514*16 =
8,224` literal portal replays.  None is universal; the best has three holes.

The saved best word

```text
scratch/k16_append0200_adjbraid_best3.word
SHA256 c98743216079553315b669e7d2c79ef568fbd7df15c4d4808a8d1af9eba84b67
```

uses the braid at `q=6437`

```text
(0x8000,0x4879) -> (0xc051,0x8879), common OR 0xc879,
```

and portal `w_6440=0x2004`.  Its exact holes are
`{0x4879,0x6879,0x8000}`.

### 3.2 The two layer searches

Starting from that three-hole word, layer 2 evaluates exactly 27,976 serving
braids.  Its actual one-hole optimum is

```text
scratch/k16_append0200_braid_best3_chain_20260730.partial.word
SHA256 1a31caade945c5db32b031062203f292defe54d3316f0b698f4694e3921989f3
sole hole 0xa879.
```

It is obtained by replacing cells 6437--6438 with
`(0x8000,0x4879)`, preserving their OR.

The separately saved file whose name ends in `layer2_best2.word` is not that
optimum.  It is the two-hole branch

```text
scratch/k16_append0200_adjbraid_layer2_best2.word
SHA256 a04f85bf44d953302a520503e2af674d0a6153f8317287cd2e12dd9f818caf07
holes {0x4879,0x6879},
```

obtained from the three-hole word by a braid at `q=0`.

Layer 3 starts from this two-hole branch, not from layer 2's one-hole optimum.
It evaluates exactly 2,234 serving braids and again reaches sole hole
`0xa879`.  The independently materialized result is

```text
scratch/k16_append0200_adjbraid_layer3_derived_best1.word
SHA256 8097b6e295c626d148eca686669e8cef8b7f64e802e472583b3686407e5badf4.
```

Thus both layer audits are valid individually, but any description of them as
one greedy three-hole -> one-hole -> improved continuation is false.

### 3.3 Five-phase two-gate catalogue

For

```text
scratch/k16_fivephase_rex_hole20067.word
SHA256 eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5
```

the sole hole is `E=0x4e63` and `A=0xa879` has multiplicity one.  Exactly
2,558 braids create another `A` witness avoiding gate 2.  Of these, 578 retain
at least two `A` witnesses and have at most five pregate debts.  The fixed
gate-1 edit and 16 gate-2 values therefore give `578*16=9,248` exact replays.
None is universal; the best has three holes.

The best saved word

```text
scratch/k16_fivephase_adjacent_or_braid_two_gate_best3.word
SHA256 9fa102cce639df6e1248051a1d68bf8142f309077a2493d5908d932bfb87b7e5
```

uses the preserved-OR braid at `q=6436`, gate 2
`w_6439=0x2004`, and gate 1 `w_12873=0x0002`; its exact holes are
`{0x4879,0x6879,0x8000}`.

## 4. Adversarial scope verdicts

**Valid.**  The pair-OR preservation lemma, algebraic serving catalogues,
candidate counts, debt-filter counts, saved edit signatures, and literal hole
sets all independently replay.

**Valid with a narrow scope.**  The append result excludes only the class:

1. one preserved-OR adjacent braid not touching position 6440;
2. an additional preportal `A` witness whose interval avoids position 6440;
3. at most four preportal debts and at least two `A` witnesses; and
4. one of the listed 16 portal values.

The avoidance condition means the newly certified `A` occurrence survives
overwriting the portal.  It does not assert that all braid-affected intervals
avoid the portal.

**Valid with a narrow scope.**  The five-phase result excludes only the class:

1. one preserved-OR adjacent braid touching neither gate coordinate;
2. an additional pregate `A` witness avoiding gate 2 (it may include gate 1);
3. at most five pregate debts and at least two pregate `A` witnesses;
4. the fixed gate-1 edit followed by one of 16 gate-2 values.

Final literal replay makes witnesses involving gate 1 safe to enumerate, since
destruction by the gate is detected.  In contrast, a solution in which the
gates and braid create `A` only jointly, with no qualifying pregate witness
avoiding gate 2, lies outside the catalogue.

**Corrected.**  Layer 3 is a branch from the saved two-hole intermediate;
the apparent layer-2/layer-3 input-hole mismatch is real bookkeeping, not a
replay error.

**Unsupported.**  These artifacts do not prove a global adjacent-braid no-go,
a neutral-route no-go, an unrestricted one-braid-plus-portal/two-gate no-go,
or any radius statement beyond their explicit filters.  The debt bounds four
and five are search restrictions, not consequences of universality.

## 5. Current global boundary and handoff correction

These local results are explanatory no-go evidence only.  The authenticated
word

```text
answers/k16_upper12874.word
SHA256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

has already established `nu(16) <= 12874`.  Therefore any handoff statement
still giving `12873 <= nu(16) <= 12875`, or calling length 12874 open, is stale
and must be replaced by

```text
12873 <= nu(16) <= 12874.
```

Nothing in this audit proves or obstructs the remaining one-cell compression.
