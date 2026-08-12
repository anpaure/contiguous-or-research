# K16 u0 two-block braid: exact source-relative static census

Date: 2026-07-30

Status: **production census queued**.  The scope, authenticated input fibre,
relocation-view completeness lemma, slow/view cross-check, runner, and
independent replay are frozen below.  Replace the marked production-result
block only after all 24 capped H100 shards exit zero and the canonical replay
passes.

## 1. Frozen first-stage fibre

The parent census is the exact run of
`scratch/search_k16_u0_local_block_relocations_20260730.cpp` on the
authenticated upper-complete u0 target chronology.  Its two
orientation-preserving move families were:

* **A:** remove every nonempty block contained in current rows
  `3317..3326` and insert it at every core position before the fixed terminal
  flats;
* **B:** remove every current pre-tail block of length at most ten and insert
  it at every core position `3317..3327`.

After deduplication of overlapping A/B tuples this is exactly 2,122,010
relocation representations.  The exact gates leave

```
flat profile        1,877,927
local middle check          141
full carrier                141
upper0                        9
```

The 141 carrier rows represent 140 distinct physical chronologies.  Rows 55
and 56 are the one duplicate pair; both have target-word SHA-256
`9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b`.
The nine upper-complete representations are roots
`1,34,35,55,56,126,133,135,136`.  The independently computed full static
rank-1..7 atlas has an empty neighbourhood for

```
H = 0x4c71
```

on every one of the 141 carrier representations, including all nine upper0
rows.  Thus no first-stage root alone passes the static lower gate.

The frozen package is

```
/home/amodo/or15/work/root_k16_u0_twoblock_braid_20260730_9d6d2e/
    frozen_u0_first_stage_141_20260730.tar.gz
```

with archive SHA-256
`d898b14cc66be4e4be39286ac25f6786d0fe476426aecab6a693aa76a66c598d`.
It contains the first engine, `meta.tsv`, and 141 each of target words,
maximal envelopes, and static-atlas JSONs.  Its 425-entry manifest has
SHA-256
`d4fae611e669d7a5d3f6364567249f2af8d54fd0bb1de2ce80873ec5daa5912f`
and verifies without error.  In particular,

```
first engine source  1dbe0158eadbc5adddca1b9c495aabd8fd77f622cb39e050db3aa34e96f47230
first meta.tsv       0c2fc93ed28cb892e0fb4d0b63850012ca5ce79f4481a40a8553fd9bbf43a640
```

## 2. Exact second-block domain

For each of the 141 frozen carrier **representations**, independently apply
the same complete A/B family in the current root coordinates.  Overlapping
A/B tuples are again deduplicated before evaluation.  There are exactly

```
141 * 2,122,010 = 299,203,410
```

ordered `(first-root, second-relocation)` representations.  Retaining the
duplicate first roots is intentional: final target words are SHA-deduplicated
only after the census, while all root/family/cut/insertion provenance and its
multiplicity are retained.

This is the exhaustive closure of the 141-root coupled-block family and is
the minimal nonstandard braid extension beyond the fixed3+1 census.  It is
not a representation-disjoint partition: some compositions can undo the
first move or land on a chronology also represented in fixed3+1.  Final-word
deduplication and provenance multiplicities make those overlaps explicit.

Every representation is filtered in this order:

1. exact three-flat G0 chronology with terminal flat starts 12869 and 12871;
2. necessary exact middle replay in every changed-seam and flat
   neighbourhood;
3. full forced-depth scalar capacity, maximal envelope, and all-middle replay;
4. the cheap mandatory-free necessary host gate for `0x4c71`, including its
   missing near-host bit `0x0010` and nonzero physical positions;
5. the exact proper-prefix `0x4c71` host test, including every forced
   middle-carrier mandatory bit;
6. complete upper replay (`upper0`);
7. the complete static rank-1..7 lower atlas.

Every exact-host+upper0 representation is dumped before the last verdict.
The independent audit reconstructs it byte-for-byte from its frozen root and
`(family,a,b,p)`, then independently rebuilds depths, envelopes, mandatory
carriers, upper coverage, and all 26,332 lower-target candidate counts.  No
SAT or CP model is used.

## 3. Relocation-view completeness lemma

Let a chronology `q` have exactly three equality pairs, and relocate the
orientation-preserving block `[a,b)` of length `l=b-a` before position `p` of
the deleted core.  Every adjacency internal to the moved block and to each
unchanged core segment is preserved.  Hence every equality pair in the new
chronology is one of:

* a mapped old equality pair whose two endpoints remain consecutive; or
* one of the three new seam adjacencies beginning at

  ```
  p-1,
  p+l-1,
  a-1 + (l if p <= a-1 else 0).
  ```

Conversely, directly comparing the endpoints at these mapped/seam positions
finds every new equality.  Sorting these positions, requiring exactly three
nonadjacent equality starts, and requiring the two terminal starts gives
exactly the materialized flat profile.  The forced depth at every row follows
from those three starts.

The exact middle value of a seam-neighbourhood row depends on at most the
four source rows covering each of at most four envelope positions.  It can
therefore be evaluated directly through the relocation index map, without
materializing or scanning all 12,873 rows.  These local checks are only used
as necessary rejections.  Every surviving representation is then
materialized; its full flat profile is asserted byte-equal to the view
profile, and the complete global carrier replay is performed.  Therefore the
view optimization cannot remove a representation accepted by the original
staged gates.

## 4. Authenticated slow/view equivalence

Root 0 was exhaustively evaluated both by the original materialize-first
engine and by the relocation-view engine.  The slow run used 41.05 CPU
seconds (82.60 wall seconds at 49% CPU); the view run used 1.53 CPU seconds
(3.71 wall seconds at 43% CPU).  Both give exactly

```
jobs             2,122,010
flat             2,121,735
local                  492
carrier                492
bit10 allowed            0
exact H host              0
upper0                    0
static pass               0
```

The following result-file hashes are byte-identical between the two runs:

```
candidate TSV  57a0454eee7fb3e0196805af5bca487e223ba9dbd30d3f816ed2bd5656cbcc2a
root ledger    6f1f52411fa875c315b30311a13f9598cffdc38a49431d910416ed4280099ffb
stdout         159d354b53c4d32a31501f56c9a5317855f66943a883ccef73caa6ee975ffcde
summary        4818af37f4c1259a009d1e88cf439ce32ab78479d08e3a5723b4504fcd7545e0
```

The final production source additionally asserts the view/materialized flat
profile equality on every local-pass representation and emits no worker
stderr.

## 5. Frozen second-stage machinery

```
scratch/k16_state2_u0_two_block_braid_20260730/
    search_k16_u0_second_block_braid_20260730.cpp
    launch_k16_u0_second_block_braid_20260730.py
    audit_k16_u0_second_block_braid_20260730.py
```

Current authenticated hashes are:

```
second engine source  64c7d01205046e7be47508e24641b531494847b56d7bef5e0cb4aa9a291d4e1b
H100 binary           e8d575e4fc780d6adfc61f00379e1ce8e11e9e2703ebd7c6bbfa8bc6c6946ee2
24-shard launcher     8d95b504f38036753e89345fc62c776400ded46a13a71dcf0e6a10513e79b3bc
independent audit     606e3ebe3e65b4de69f695911953e9c476de93686ab9d144fd150085f21ab277
```

Each of the 24 shards owns five or six roots and is capped at 900 seconds,
2 GiB address space, and nice level 19 on an explicitly checked H100 core.
The audit requires empty stderr, zero timed-resource exit, the exact capped
command shape, complete worker/root partitions, per-root stage monotonicity,
all actual root hashes equal to the frozen manifest, `dumped=upper0`, and
representation static-pass counts equal to the independent replay.

## 6. Production result — pending

> **PENDING H100 PRODUCTION.** Fill in exact totals, deduplicated word counts,
> static survivors, canonical audit hash/payload hash, and archive hash only
> after all shards and the independent replay complete.

## 7. Exact noncoverage and theorem scope

This is a source-relative chronology theorem only.  It does **not** cover:

* reversed blocks or arbitrary segment permutations;
* a second source block longer than ten unless that block lies wholly in rows
  3317..3326;
* a second insertion outside `3317..3327` unless the removed block lies wholly
  in rows `3317..3326`;
* terminal-flat moves (both terminal flat starts are fixed);
* two relocations whose first intermediate chronology failed the first-stage
  carrier gate but whose final chronology might recover;
* non-relocation substitutions, arbitrary new target rows, general 4/5-opt
  rethreads outside A/B, or unrestricted K16 words;
* physical COMP3 feasibility after a static pass (the static atlas is only a
  necessary gate).

Accordingly, even a zero-survivor production census is not an unrestricted
K16 no-go and does not by itself improve the global lower bound.
