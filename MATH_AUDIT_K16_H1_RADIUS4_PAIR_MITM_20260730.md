# K16 H1 four-edit pair/MITM audit

Date: 2026-07-30

## Purpose and source

This lane attacks genuine four-substitution circuits around

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12873; sole hole 11373 = 0x2c6d.
```

It does not duplicate the stronger arbitrary-value `joint13` CNF.  Instead it
forms two exact edit-pair actions, hashes them by the private targets which
one pair must restore for the other, and independently replays every retained
four-site assignment using the ten consecutive edited-site interval classes.

## Audited finite catalogue

The builder

```text
scratch/build_k16_h1_radius4_mitm_catalogue_20260730.py
```

uses the requested inputs:

* the exact H1, H43117, and H2 provider atlases;
* all saved portal-composition atlases and persistent circuit/depth-two words
  in `scratch/k16_portal_compositions.tar.gz` and
  `scratch/k16_portal_compositions_depth2.tar.gz`;
* all sites in the twelve rows of
  `scratch/k16_nested_portal_interacting12_20260730.tsv`; and
* the independently audited 245-value closure domain on every persistent or
  interacting site.

The resulting finite domain is

```text
scratch/k16_h1_radius4_mitm_catalogue_20260730.tsv
SHA-256 19a48659bdd50abf0a17d3baa3755b79fa88ab7c69a1361dd39a51eb9cd2d4a0
288 positions; 7099 literal position/value moves.
```

In particular, it contains every position participating in a recorded exact
provider move with at most eight intermediate holes, the six persistent
circuit sites, and all sites from the twelve interacting triples.  The
closure domain is exhaustive only at the 26 named closure sites.  This is a
finite high-signal closure, not the unrestricted `288 x 65535` value domain.

The catalogue lineage and input hashes are frozen in
`scratch/k16_h1_radius4_mitm_catalogue_20260730.audit.json`.

## Exact pair and four-site delta formulae

For edits at `p<q`, every changed interval belongs to exactly one of

```text
p, q, pq.
```

For four edits at `a<b<c<d`, every changed interval belongs to exactly one of

```text
a, b, c, d, ab, bc, cd, abc, bcd, abcd.
```

Within a class, the exact label multiset is a product of the compressed left
suffix chain, the fixed bridge OR, the selected edited values, and the
compressed right prefix chain.  The engine subtracts the old product and adds
the new product at full multiplicity.  Thus its sparse delta is an identity,
not a presence-only approximation.

The independent test

```text
scratch/test_k16_h1_radius4_pair_mitm_delta_20260730.cpp
```

compares 500 random pair deltas and 500 random four-site deltas with a fresh
complete multiplicity count on all 65,536 labels.  It also compares 500
random saturated-gap four-site deltas with the sum of their two pair deltas
on all 65,536 labels.  Every comparison passes.

## Exact separated-pair lemma

Suppose the two spatial edit pairs are separated by a fixed middle gap whose
OR is `0xffff`.  Every interval meeting both pairs then has label `0xffff`
before and after either pair.  Consequently the two pair deltas are literally
additive on every target, including `0xffff`.  Universality is therefore
equivalent to the complementary private-target inequalities checked by the
MITM plus the final exact four-site replay.

Therefore the engine is complete in the following finite scope:

1. all four values belong to the frozen catalogue;
2. one spatial pair installs the source hole in isolation;
3. each pair-alone intermediate has at most eight holes; and
4. the two spatial pairs are separated by a fixed `0xffff` bridge.

For interleaving or short-gap pairs, the engine additionally checks every row
in which the repair pair independently has positive multiplicity delta on all
portal-pair debts.  A found word is always conclusive because it receives a
full literal replay.  A negative result in this screened nonlaminar extension
does **not** exclude a solution whose essential witness exists only as a
four-site cross interval.

## Run and disposition

The O3 engine is

```text
scratch/search_k16_h1_radius4_pair_mitm_20260730.cpp
```

and the one-core H100 run is isolated at

```text
/home/amodo/or15/work/root_k16_h1_radius4_pair_mitm_20260730_19a48659
```

on CPU core 28, with an 1800-second cap.  No `joint13` solver was duplicated.

<!-- RUN_DISPOSITION_20260730 -->

The screened run exhausted with no completion:

```text
catalogue moves / positions               7,099 / 288
distinct-position move pairs             24,348,717
portal prefilter / retained actions       4,111,372 / 224,114
induced residual targets                  1,625
repair pairs / retained actions           24,348,717 / 775,506
complement rows                           897,885,352
exact four-site replays                   27,141,316
separated saturated geometry rows         94,353,810
separated saturated exact replays          2,515,178
universal candidates                               0
```

The process used one H100 CPU core for 17:08.47 wall time, 1028.20 user CPU
seconds, and 115,468 KiB maximum RSS.  Exit status `1` is the engine's normal
exhausted-without-candidate disposition.

Frozen run artifacts:

| artifact | SHA-256 |
|---|---|
| `scratch/k16_h1_radius4_pair_mitm_20260730.audit.json` | `74c7578326175f9589befa3bde56a3c5f8c9813356496d7c318964699804b794` |
| `scratch/k16_h1_radius4_pair_mitm_20260730.resource.txt` | `3f0dfa114573d8bbb0d95057ac39314f098cb4f8dcf78175ae0629469a8c7d6f` |
| exact serial run source | `ab7744951aa15e3b70c80c9e427f118b97aaf12f074d2224a506e5c70efc8f89` |
| compiled H100 binary | `9d76aea1082f16e52a385ddc98309d29a2063bb72c9a35cfdd03715d78462990` |

The independent final audit rebuilds the catalogue byte for byte, recomputes
the exact distinct-position pair count, compiles the random delta/additivity
tester against the precise serial run source, and cross-checks every final
counter against the resource transcript.  It returns `GO_SCOPED_NO_COMPLETION`:

```text
scratch/k16_h1_radius4_pair_mitm_final_independent_20260730.audit.json
SHA-256 a3f4308da250bd9a664ae04259b3f8792592162acda2289e3bc45ba8e611de0e
payload ce046b2006cb4158031f53c1e0126ec47dfd735588a51a982b9d7a7ba4b65571
```

The mathematical disposition is therefore two-tiered:

1. **Exact scoped no-go:** no catalogue-valued four-edit completion exists
   in the separated, saturated, pair-alone-cap-eight class stated above.
2. **Broader screened no-go:** none of the retained interleaving or short-gap
   rows works when its repair pair independently supplies every portal debt.
   This second statement is a large candidate census, not a cross-only
   nonlaminar impossibility theorem.

## Claim boundary

A literal PASS would be a universal word of length 12873 and prove
`nu(16)=12873`.  A scoped negative result excludes only the finite catalogue,
the pair-alone hole cap, and the pair geometry stated above.  In particular it
does not exclude arbitrary values on the 288 positions, a cross-only
four-site witness, edits outside the catalogue support, or an unrelated
length-12873 basin.
