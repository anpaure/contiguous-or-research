# K16 state-2 `u0`: host-aware relocation and symmetric fixed-four no-go

## 1. Scope and authenticated inputs

This note proves two finite, source-relative no-go statements.  It does not
exclude arbitrary length-12,873 K16 words and does not change the global
bracket.

The dominant state-2 chronology is

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA-256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464
```

It has exact `G=0`, scalar capacity 32,175 and strict-upper holes
`{0x4e79,0xc679}`.  Its upper-complete `u0` rethread is

```text
scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/best_targets.txt
SHA-256 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
```

with maximal envelope SHA-256

```text
57669ee5934872f766cdd1666f5a418d6710040f1edafe2c59f2d8ddf146b54a.
```

Its flat starts are `3322,12869,12871`, its scalar capacity is 29,065,
and its sole zero-degree lower target is

```text
H = 0x4c71 = 19569.
```

## 2. Exact individual-host criterion

Let `T_i` be a rank-eight target chronology with forced no-gap depths `d_i`.
Its maximal source envelopes are

```text
E_p = intersection { T_i : i <= p <= i+d_i }.
```

For a proper-prefix cell `I=[s,s+l)`, `1<=l<=d_s`, put

```text
A_I = OR { E_p : p in I }.
```

Let `M_I` contain a bit `b` when some middle row containing `b` has its
complete maximal carrier

```text
C_(i,b) = { p in [i,i+d_i] : b in E_p }
```

inside `I`.  Then a lower mask `S` has an exact individual static host at
`I` if and only if

```text
S subset A_I,
M_I subset S,
E_p intersects S for every p in I.                 (2.1)
```

Necessity is immediate from nonempty source cells, exact interval OR and the
middle carrier rows.  For sufficiency set the cells in `I` to `E_p intersect
S` and all cells outside `I` to their maximal envelopes.  The first and third
conditions make the selected cells nonempty with interval OR exactly `S`.
The mandatory condition says that every middle bit excluded from `S` retains
at least one carrier position outside `I`; hence every middle row remains
covered.  Thus (2.1) is an exact one-target gate, although simultaneous hosts
for all lower masks can still conflict.

Every rank-below-eight source interval is a proper prefix: once an interval
starting at `s` reaches offset `d_s`, it already contains the rank-eight row
`T_s`.  Consequently the proper-prefix catalogue is exhaustive.

## 3. Complete minimal relocation theorem

Remove the first flat pair `0x4e71,0x4e71` from `u0` and insert it at every
possible final position.  The same census was then applied to the three
minimal contiguous superblocks containing this pair:

```text
pair2   = [pair],
left3   = [left neighbour,pair],
right3  = [pair,right neighbour],
both4   = [left neighbour,pair,right neighbour].
```

For every row the deterministic census tests, in order, exact `G=0`, scalar
capacity at least 26,332, maximal-envelope middle recovery, an exact host for
`0x4c71` by (2.1), and strict-upper completeness.  The complete counts are:

| family | generated | G0 | capacity | exact middle | H host | survivors |
|---|---:|---:|---:|---:|---:|---:|
| `pair2` | 12,872 | 12,870 | 12,281 | 1 | 0 | 0 |
| `left3` | 12,871 | 12,869 | 12,281 | 1 | 0 | 0 |
| `right3` | 12,871 | 12,869 | 12,280 | 1 | 0 | 0 |
| `both4` | 12,870 | 12,868 | 12,280 | 1 | 0 | 0 |

In every family the unique exact-middle row is the identity chronology `u0`.
It has no `0x4c71` host.  Therefore no upper audit is needed and all four
relocation families are impossible.

The pair family was executed twice, once alone and once as the prefix of the
extended run; all 12,872 candidate-table rows agree byte for byte.  The
independent table audit authenticates all 51,484 extended rows, every
insertion domain, each staged count and the header-only host/survivor ledgers.

## 4. Symmetric `u0`-frozen fixed-three-plus-one theorem

Return to the dominant `77dd...` chronology.  Freeze the three `u0` cuts

```text
{3278,6388,12826}.
```

Add every extra cut in `[0,12868]` other than those three.  Sort the four
cuts, retain the outer prefix and suffix, and reconnect the three internal
segments in every one of

```text
3! * 2^3 = 48
```

order/orientation states.  This gives exactly

```text
(12869-3)*48 = 617568
```

representations.

Both source upper holes have rank nine.  A missing rank-nine interval can
become present only across a new join: all old internal adjacencies are
preserved up to reversal, and reversal preserves their endpoint union.
Therefore requiring a new join of union `0x4e79` and another of union
`0xc679` is an exact necessary prefilter.

The exhaustive ledger is

```text
quantified representations          617568
reject rank-nine join necessity      591701
join-prefilter pass                   25867
reject G0 / terminal flats                6
reject carrier / scalar capacity      12985
exact carrier pass                    12876
reject one of the protected hosts     12876
protected-host pass                       0
full static pass                          0
```

The protected host set is

```text
{0x4879,0x4c39,0x4c71}.
```

Thus every exact carrier in this fixed-four fibre fails before the upper and
complete-atlas gates.  This closes the symmetric `u0`-frozen fibre and is
disjoint from the previously closed complementary fibre with frozen cuts
`{5725,6388,12826}`.

The independent audit authenticates the result and all count partitions,
rebuilds the dominant and `u0` maximal-envelope geometries, and replays the
distinguished `u0` profile:

```text
upper holes: 0,
host counts: 0x4879 -> 1, 0x4c39 -> 1, 0x4c71 -> 0.
```

It deliberately does not repeat the 617,568-case production loop.

## 5. Frozen artifacts

Minimal relocation engine:

```text
scratch/k16_state2_flat_host_relocation_20260730/
  search_k16_state2_flat_host_relocation_20260730.cpp
    SHA 3781493af9cbdb3a7d384fd73966e70e57225141792d0b446114fcfd791d5f9a
  h100_extended_run/summary.json
    SHA 3da44d91365cdbda32b2716743044f4a24ce7d665916e88d25af5256d4b7dd07
  h100_extended_run/candidates.tsv
    SHA 72ff4d637adfaf0900261beda7c4546a6a0cfb9f8d9c3b5a128889f92e810843
  audit_k16_state2_flat_host_relocation_20260730.py
    SHA 151a02ad0f02c67c1d4e909d0740f53c6ba5bad9d5cd3c2b2b9688f79db06507
  independent.audit.json
    SHA 071c3f66053ad2c8295383e830634c612fa09540eed96ee7863d581eb6030b31
    payload 5aca3f41f992cb53f40d3e9ae49bbad8b70ed8006458d4b5accd0dfe690e6592
```

Symmetric fixed-three-plus-one engine:

```text
scratch/k16_state2_u0_fixed3plus1_4opt_20260730/
  search_k16_state2_u0_fixed3plus1_4opt_20260730.cpp
    SHA a7277116e6ab00bbcefd5e48f7f89d7d1400ea1e7879601a2312fe8263814949
  result.json
    SHA 8cc88267bd5e1595cbc778c4430f5941c709b52dc60c76990151792d47d8f76e
  run.stdout
    SHA 0698c67f7eeca4370f75ffedfd2dc524cedf4b54b64e80af5b6cbbf83360106e
  run.stderr
    SHA e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  audit_k16_state2_u0_fixed3plus1_4opt_20260730.py
    SHA cc4f57cd9d960ff70a044cc01157673de832e31faed2fb16378eedef56dca204
  independent.audit.json
    SHA 82b88d315b3280e4b5c5b426b06d807058c41f991ce708eb49c2798fd110c466
    payload 6dd1e1e8de80a574a0a9258c3a0fb26de49e0fe1af85621e3f349ee8be02beb7
```

Both H100 runs used one CPU core, a 4 GiB address-space cap and a 900-second
wall cap; both exited zero with empty stderr.  No CP/SAT solver was run.

## 6. Remaining scope

Open are relocations of larger/noncontiguous blocks, movable frozen cuts,
terminal-flat cuts, five-cut rethreads, nonstandard duplication and unrelated
chronologies.  Even a static-host survivor would still require the exact
simultaneous lower COMP3 solve.  No unrestricted K16 no-go follows here.
