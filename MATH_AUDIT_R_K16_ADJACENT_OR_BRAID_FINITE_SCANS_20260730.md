# Adversarial audit of the K16 adjacent OR-braid finite scans

Date: 2026-07-30

Status: **valid finite counts and saved-word replays, with essential scope
corrections**.  These scans are only local information for the remaining
length-12,873 compression problem.  A length-12,874 universal word now exists,
so none of the negative scan labels can be read as a length-12,874 no-go.

No H100 solve was run for this audit.  The independent replay is a 13-second,
low-memory compressed/count-delta calculation.

## 1. Frozen programs and audits

The audited sources are:

```text
search_k16_adjacent_or_braid_blocker_20260730.cpp  ab9abe0957fffbd9bf6bff5a58eedb9561d46f2cfb78de5facec86504cddc779
search_k16_adjacent_or_braid_layer_20260730.cpp    104f3d02912ed91e8841ff159a6f83b57f394ccde3d1e60d83d16be63ebb89f0
search_k16_adjacent_or_braid_two_gate_20260730.cpp 8b644bfd78a2e533530876c4c9f3e65dfd9fe75282dee41cf9a86efb66a70e21
search_k16_or_braid_chain_20260730.cpp             0e4d85ea6dd5f7ca532f6e1d1904b76ad12991d982fa101c60617fc57ef488e5
```

The five scalar ledgers found with this family are:

```text
k16_append0200_adjacent_or_braid_blocker_20260730.audit.json
  5fc2275124fe53ec796d2cb245e5ceb4d608f1c7551a373dc7edcb47dffda119
k16_append0200_adjacent_or_braid_layer2_20260730.audit.json
  fc7e08ed70ea46d72c11b262912647891584f4f7b4cad04540dc1709e250d4c1
k16_append0200_adjacent_or_braid_layer3_20260730.audit.json
  ef2e986e6c20d4a07a6e02a9ae260dafd384daa4f98726dbd10bbf1694b02d99
k16_append0200_braid_best3_chain_20260730.audit.json
  37caf3532e749922ed17d76cf39d023c223de825bdee4fa05e093138a1772bd0
k16_fivephase_adjacent_or_braid_two_gate_20260730.audit.json
  54d647a82f4bd9824467f301f03e4592eb75dddf39b6a2a360d3e0b4dd2075ec
```

## 2. `pair_delta`: VALID

Let the adjacent old pair at positions `q,q+1` be `(a,b)` and the replacement
be `(x,y)`, with

```text
a OR b = x OR y.
```

Every interval belongs to exactly one of four classes:

1. it contains neither changed position, so it is unchanged;
2. it contains both, so the equality of the pair OR makes it unchanged;
3. it contains `q` but not `q+1`, hence it ends at `q`;
4. it contains `q+1` but not `q`, hence it starts at `q+1`.

The two loops in `pair_delta` enumerate classes 3 and 4 literally, subtracting
the old OR and adding the new OR once per physical interval.  Stopping when
both values reach `0xffff` is sound because all longer extensions remain
`0xffff`; the full target also retains the unchanged whole-word witness from
class 2.  Thus the delta lemma is exact, including multiplicities.

The implementation's `touched` vector can contain a duplicate if a delta
returns to zero and is touched again.  This is a real generic coding caveat,
but the independent regeneration found **zero cutoff disagreements** between
the vector count and the distinct-debt count in both concrete cutoff scans.
It therefore does not alter any reported count below.

## 3. `serving_braids`: VALID WITH ITS EXPLICIT SCOPE

Fix the old pair OR `u`.  For a left-exposed interval ending at `q`, let `c`
be the OR of its unchanged context.  A new left cell serves target `t` exactly
when

```text
c OR x = t,  x subseteq u,  x != 0.
```

The code writes the forced part as `t & ~c` and independently chooses every
optional bit in `t & u & c`.  `add_decompositions` then enumerates every
nonzero `y` with `x OR y=u`.  The right-exposed case is symmetric.  Once the
outward context has a bit outside `t`, monotonicity makes the early break
sound.  Deduplication by `(x,y)` is exact.

Consequently `serving_braids` is complete for:

* nonzero same-pair-OR replacements;
* which create the named target on one exposed side;
* and, when `forbidden_pos` is supplied, whose advertised serving interval
  avoids that position.

It is not a catalogue of arbitrary two-cell replacements, nonadjacent moves,
pair-OR-changing moves, or witnesses that cross the forbidden gate.

## 4. Independent catalogue counts

All scalar counts regenerate exactly:

| scan | independent result | verdict |
|---|---:|---|
| append blocker catalogue | 2,558 decompositions/candidates | VALID |
| blocker safe fortifications | 0 | VALID |
| blocker cutoff-eligible states | 514 | VALID |
| blocker portal replays | `514*16=8,224` | VALID |
| layer 2 | 27,976 candidates/evaluations | VALID |
| layer 3 | 2,234 candidates/evaluations | VALID |
| greedy chain | `27,976+3,044=31,020` candidates | VALID |
| five-phase two-gate catalogue | 2,558 candidates | VALID |
| two-gate cutoff-eligible states | 578 | VALID |
| two-gate replays | `578*16=9,248` | VALID |

The independent one-layer minima also agree:

```text
three-hole input {18553,26745,32768}:
  minimum one-braid hole count 1,
  unique lexicographic minimizer (q,x,y)=(6437,32768,18553),
  residual {43129};

two-hole input {18553,26745}:
  minimum one-braid hole count 1,
  first sorted minimizer (6437,32768,18553),
  residual {43129}.
```

The blocker and two-gate ledgers report `x=49233`; the independent sorted
enumeration first encounters the tied value `x=49152`.  This is not a
contradiction: the production scanners iterate an `unordered_set`, and the
saved `x=49233` words replay with the same minimum three-hole profile.

## 5. Debt cutoffs: CORRECTED SCOPE

The blocker scanner directly replays only candidates with at most four
pre-portal debts.  The two-gate scanner directly replays only candidates with
at most five pre-gate debts.  The concrete eligible/replay counts are exact,
and vector duplicates do not affect membership here.

However, neither source proves that the later portal can repair at most four
debts, or that the two fixed gates can repair at most five debts.  A single
changed cell can participate in several new interval witnesses.  Therefore:

* `PASS_EXHAUSTED_NO_UNIVERSAL` is **valid only after explicitly adding the
  stated debt cutoff and forbidden-witness conditions**;
* interpreting it as exhaustion of every adjacent same-pair-OR braid followed
  by the portal/gates is **UNSUPPORTED**.

The layer scans have no such cutoff.  They are complete for a strict reduction
of the hole count by one same-pair-OR braid from the named input: any strict
reduction must serve at least one old hole, and every such serving braid is in
the catalogue.

The chain is different.  Each visited round exhausts its current hole-serving
one-braid catalogue, but choosing one lexicographically best move and repeating
is greedy.  Its multi-round `NO_UNIVERSAL` label is **not** a complete
multi-braid no-go.  In the saved run, round 0 has the unique minimum above;
the resulting one-hole state has 3,044 serving braids, and none improves the
lexicographic `(holes,singletons)` score.  This validates the recorded greedy
stall, not all two-braid paths.

## 6. Independent full replay of saved words

An independent ending-OR/multiplicity replay gives:

| saved word | SHA-256 | exact holes |
|---|---|---|
| `k16_append0200_adjbraid_best3.word` | `c98743216079553315b669e7d2c79ef568fbd7df15c4d4808a8d1af9eba84b67` | `{18553,26745,32768}` |
| `k16_append0200_adjbraid_layer2_best2.word` | `a04f85bf44d953302a520503e2af674d0a6153f8317287cd2e12dd9f818caf07` | `{18553,26745}` |
| `k16_append0200_braid_best3_chain_20260730.partial.word` | `1a31caade945c5db32b031062203f292defe54d3316f0b698f4694e3921989f3` | `{43129}` |
| `k16_fivephase_adjacent_or_braid_two_gate_best3.word` | `9fa102cce639df6e1248051a1d68bf8142f309077a2493d5908d932bfb87b7e5` | `{18553,26745,32768}` |

The additional saved one-hole state
`k16_append0200_blocker_prepay_to_hole43129.word`, SHA-256
`dc7c5ebebf9361e045d2b4cb1b5a43efb730c2c3506144cb2be57d07074485c3`,
also replays with the sole hole `{43129}`.

The physical move provenance checks exactly:

* append source to `best3`: the pair at `q=6437` changes to
  `(49233,34937)` with pair OR `51321` preserved, and portal `p6440` changes
  to `8196`;
* `best3` to `best2`: the pair at `q=0` changes with old/new OR `43053`;
* `best3` to the chain partial: `q=6437` changes to `(32768,18553)` with
  old/new OR `51321`;
* five-phase source to its best3: `q=6436` changes to `(49233,34937)` with
  OR `51321`, `p6439` changes to `8196`, and `p12873` changes to `2`.

Thus all saved scalar profiles are VALID.  None of these words is universal.

## 7. Independent audit artifact and final verdict

```text
scratch/audit_r_k16_adjacent_or_braid_scans_20260730.py
SHA-256 c4d0c762c22a43fec292c55a52e74bf2a0e73167840a5629b59c7f076c7941ff

scratch/r_k16_adjacent_or_braid_scans_crossaudit_20260730.audit.json
SHA-256 a2b725fb39522a32352a29b71893f8fcc4a888c674e191556d395d813543851c
```

Final classification:

* `pair_delta`: **VALID**;
* exposed-side `serving_braids` completeness: **VALID IN THE STATED CLASS**;
* finite catalogue counts and saved profiles: **VALID**;
* blocker/two-gate global exhaustion without the debt cutoffs: **UNSUPPORTED**;
* greedy-chain multi-braid exhaustion: **UNSUPPORTED**;
* corrected cutoff-relative and visited-round local no-go statements:
  **VALID**.
