# Exact `k=17` c68b residence descent: local floors and paired topology debt

## Status

This note freezes an exact, narrowly scoped computation on the authenticated
connected `c68b` quotient factor.  Every accepted terminal factor has:

- all 24,310 rank-eight facets exactly once;
- all 24,310 rank-nine owners with degree two;
- all 19,448 rank-ten caps covered;
- all 3,944 protected physical edges unchanged; and
- one physical cycle.

The computation does **not** produce residence at depth three.  It also makes
no claim about the deeper upper deck, a source antecedent, or the lower
compiler.  Its positive result is that a strict one-circuit residence floor
can be escaped by a pair of circuits which temporarily carries topology or
cap debt.

**Superseding checkpoint.**  Sections 1--6 retain the earlier trajectory for
reproducibility.  Section 7 freezes the later exact `1,615` scoped floor, its
same-residence `C6+C6` deep-deck rethread, the independent `C18` upper-deck
point, and the mixed `C6+(C10/C14)` escape to `1,581`.

## 1. Exact residence metric

For a cyclic owner order and each coordinate, count every maximal cyclic
one-run and zero-gap of length below four.  The lexicographic objective used
below is

```text
(number of short one-runs,
 one-run deficit to length four,
 number of short zero-gaps,
 zero-gap deficit to length four).
```

The authenticated connected double-fusion factor starts at

```text
short one-runs:  5,372 = 2,873 of length two + 2,499 of length three
one deficit:     8,245
short zero-gaps: 8,976 = 3,502/2,958/2,516 of lengths one/two/three
zero deficit:   18,938
```

All counts are multiples of 17, as required by the `Z_17` action.  There are
316 short one-run orbits and 528 short zero-gap orbits.

## 2. One quotient-circuit descent and its first strict floor

An endpoint-retaining quotient move replaces one selected endpoint of one
facet orbit.  A directed cycle of three such moves is called a quotient
`C6`; a directed cycle of four is a quotient `C8`.  They change respectively
51 and 68 physical edges after development.  A candidate is accepted only
after literal development proves cap coverage and one physical component.

Greedy exact re-enumeration after every accepted move applies 48 quotient
`C6/C8` circuits and reaches

```text
short one-runs:  4,199 = 2,312 of length two + 1,887 of length three
one deficit:     6,511
short zero-gaps: 8,874 = 3,519/2,907/2,448
zero deficit:   18,819
```

At this factor the complete one-circuit quotient neighborhood contains

```text
1,888 quotient C6s,  63 cap-safe, 30 physically connected;
6,259 quotient C8s,  59 cap-safe, 24 physically connected.
```

None improves the one-run count or deficit.  Thus this is an exact strict
floor for the stated single quotient `C6/C8` move class.

There is also an independent literal physical-`C6` census on this same
factor:

```text
raw triples              2,333,760
active physical C6s         47,753
protected-blocked            21,267
cap-safe                       1,003
residence-improving                0
connected-improving                0
```

Therefore 4,199 is simultaneously a strict single quotient-`C6/C8` floor
and a strict single individual physical-`C6` floor.  Individual physical
`C8`s are outside this note.

The frozen factor is

```text
scratch/k17_c68b_double_fusion_residence_greedy_20260802/
  c68b.greedy48.factor.tsv
```

with SHA-256

```text
b1343737cb0e3d99dec503e526e566521504478af1c5792c9a7949b6a5796616
```

Its independently reconstructed owner order has SHA-256

```text
48abe6a6d3685d4f4ee6820fba2a39ce20dd7781becab3d5d5b056689093fbea
```

and the independent residence audit has SHA-256

```text
7a9fca4902f9d326c334bb5ed5bc53c609ffba7df3c06e12000db255b7666a03.
```

The physical-`C6` replay transcript has SHA-256

```text
026b4f4bfe707ad0843ec46c6501dd445456d51966882cd0d463308d1b8ee361.
```

## 3. Exact paired quotient neighborhood

At a strict floor, enumerate every directed quotient `C6/C8`, then every
pair supported on disjoint facet orbits.  Either half may be invalid as a
standalone terminal factor: it may uncover a bounded number of caps, split
the physical cycle, or fail literal phase balance.  The union is retained
only if literal development restores every cap, every owner degree, and one
physical cycle.

This is an exact two-step lookahead, not a random or heuristic portfolio.
At the 4,199 floor it has:

```text
circuits                         8,147
disjoint pairs              32,769,892
final cap-safe pairs             7,294
final connected literal pairs    2,249
residence-improving pairs             4
```

The best pair is `C8+C8`.  Its union gives

```text
4,199 -> 4,165 short one-runs
6,511 -> 6,460 one deficit
8,874 -> 8,806 short zero-gaps
18,819 -> 18,632 zero deficit.
```

One half alone has 19 physical components; the other half alone has one.
Both halves cover all caps, and their union is one physical cycle.  Two
subsequent single circuits, which leave the one score unchanged, reduce the
zero-gap count from 8,806 to 8,721.

At that next strict floor the exact paired census has 17 improving pairs.
The best is `C6+C6`; either half alone has two physical components, while
their union is connected.  It gives

```text
4,165 -> 4,148 short one-runs
6,460 -> 6,426 one deficit
8,721 -> 8,636 short zero-gaps
18,513 -> 18,394 zero deficit.
```

A third paired census finds another strict improvement.  Its first half has
one cap hole and is not a literal standalone factor; its second half is
cap-safe and connected.  The union is literal-valid and gives

```text
4,148 -> 4,131 short one-runs
6,426 -> 6,392 one deficit.
```

That paired move opens a further single-circuit cascade.  Four accepted
single circuits first reach the strict one-circuit floor

```text
short one-runs:  4,080 = 2,210 of length two + 1,870 of length three
one deficit:     6,290
short zero-gaps: 8,602 = 3,468/2,822/2,312
zero deficit:   18,360
```

The literal checkpoint factor

```text
scratch/k17_c68b_double_fusion_residence_greedy_20260802/floor004.factor.tsv
```

has SHA-256

```text
1557fa99a0b7fe725604f44a0535208dab0b2ae51d66d534823d9cdc965ecc1e
```

and its model, owner order, quotient verification audit, and residence audit
have respective SHA-256 values

```text
7cc0345dda66052154102843a82daa3e38d7b58828127f5ebab8d99c40d82aa9
e7e3bd37452282b2b91f0bb6e72ba5ff9f97ef11906a3535a509bc3b9d2589fb
e49f121678e59b4d9f144948e1b60e7534740718c949308ff5271a4fe14c13f0
5813f5b3385c2784572a91bc9aa9875131abb2e6929c33a5693ee6d1a0718abb.
```

Continued exact alternation between paired packets and single cleanup gives
the following authenticated positive-run trajectory:

| stage | short one-runs | short zero-gaps |
|---|---:|---:|
| initial connected c68b | 5,372 | 8,976 |
| 48 single quotient circuits | 4,199 | 8,874 |
| paired rounds 1--3 and cleanup | 4,080 | 8,602 |
| paired rounds 4--5 and cleanup | 3,995 | 8,738 |
| paired rounds 6--8 and cleanup | 3,910 | 8,738 |
| paired round 9 and cleanup | 3,876 | 8,585 |

At 3,876, the complete single `C6/C8` and disjoint paired `C6/C8`
neighborhoods are both closed.  The paired census has 8,122 circuits,
32,568,595 disjoint pairs, 7,928 final cap-safe pairs, 2,529 final connected
pairs, and no strict lexicographic improvement.

This is not a global floor.  Enabling longer simple quotient circuits gives:

| circuit | exact simple circuits | cap-safe | connected | improving-one | best one-runs |
|---|---:|---:|---:|---:|---:|
| `C10` | 50,583 | 128 | 41 | 6 | 3,842 |
| `C12` | 414,132 | 313 | 106 | 9 | 3,825 |
| `C14` after `C12` | 3,829,899 | 856 | 271 | 13 | 3,774 |
| `C16` after C14 cleanup | 36,989,415 | 2,313 | 693 | 51 | 3,672 |

The `C14` winner opens a short-`C6` cleanup cascade to 3,740 before `C16`
is applied.  That authenticated `C16` factor has

```text
short one-runs:  3,672 = 2,057 of length two + 1,615 of length three
one deficit:     5,729
short zero-gaps: 8,466 = 3,400/2,771/2,295
zero deficit:   18,037
```

All immediate palettes, protected edges, and one-cycle topology remain
exact.  The exact `C18` census on this factor subsequently completed.  Safe
partial cap-debt pruning rejected 1,624,892,557 prefixes and left 6,847
cap-safe `C18` circuits, of which 1,827 were physically connected and 84
improved the positive-run count.  Its best terminal score was 3,621; this
matched, but did not beat, the shorter `C10`/`C8` cleanup route.

Continuing exact alternation between `C10`/`C12`, `C14`, and complete
single-`C6/C8` cleanup gives the following further authenticated trajectory:

| stage | short one-runs | short zero-gaps | violated clauses in cumulative 421 |
|---|---:|---:|---:|
| `C16`, then `C10+C8` cleanup | 3,621 | 8,415 | 208 |
| `C12`, then `C6` cleanup | 3,553 | 8,500 | 202 |
| `C10` | 3,502 | 8,534 | 198 |
| `C12`, then `C6` cleanup | 3,434 | 8,568 | 198 |
| `C12`, then eight `C6/C8` cleanups | 3,281 | 8,415 | 183 |
| `C10` | 3,247 | 8,432 | 178 |
| zero-gap cleanup, then `C14` | **3,213** | **8,296** | **174** |

Every row still has all 24,310 facets and owners, all 19,448 caps, all 3,944
protected edges, and one physical cycle.  The last row has 1,785 length-two
and 1,428 length-three positive runs.  It exposes 189 exact quotient blocker
orbits; 174 already occur in the independently normalized cumulative-421
bank and 15 are new relative to that bank.

After independently promoting those clauses, the same sequential procedure
continues

```text
3,213 -> 3,196 -> 3,162 -> 3,145 -> 3,111 -> 3,094 -> 3,060.
```

The final `C14` factor has 1,564 length-two and 1,496 length-three positive
runs, 8,177 short zero gaps, and violates 174 clauses in the independently
promoted cumulative-445 bank.  As always, this adaptive-bank score is not
directly comparable to the older score without naming the bank.

## 4. Blocker and deep-upper calibration

The 4,029-run checkpoint exposes 237 exact quotient residence blockers.  Of
these, 168 overlap the original 316 and 69 are new, giving a cumulative set
of 385 model-specific necessary clauses.  The exact round-two CNF has
204,167 variables and 439,532 clauses.

Against those 385 blockers, the principal checkpoints violate:

| checkpoint | violated clauses |
|---|---:|
| 3,876 paired floor | 206 |
| `C12` winner | 203 |
| raw `C14` winner | 197 |
| cleaned `C14` winner | 192 |
| `C16` winner | 186 |

Thus the cleaned `C14` factor is a constructive `B192` positive control for
the frozen 385-clause projection.  A later 413-clause cumulative projection
is different: the `C16` model violates 213 of those 413 clauses.  Neither
projection is a residence certificate.

An independently normalized third blocker bank contains 421 clauses.  The
3,502-run factor was the first factor in this lane below 200 on that bank:
it violates 198 clauses.  Its exact current blocker set has 206 clauses,
with 198 old and eight new.  Subsequent long-circuit escape and local cleanup
lower the same frozen-bank score to 174 at the 3,213-run factor.  Its exact
current blocker set has 189 clauses, with 174 old and 15 new.  These figures
are literal-set comparisons after sorting and deduplicating the literals in
each clause; raw byte comparison is invalid because older and newer blocker
writers use opposite literal orders.

Residence descent does not monotonically destroy the upper deck.  The exact
rank-11/12/13 cyclic owner-union holes are:

| checkpoint | rank 11 | rank 12 | rank 13 |
|---|---:|---:|---:|
| initial connected c68b | 1,972 | 510 | 51 |
| 3,876 paired floor | 1,819 | 425 | 34 |
| `C12` winner | 1,836 | 408 | 34 |
| raw `C14` winner | 1,836 | 374 | 34 |
| cleaned `C14` winner | 1,836 | 408 | 34 |
| `C16` winner | 1,836 | 408 | 17 |
| 3,502-run `C10` factor | 1,802 | 425 | 17 |
| 3,400-run `C12` factor | 1,887 | 425 | 17 |
| 3,281-run cleanup factor | 1,921 | 459 | 17 |
| current 3,213-run factor | 1,972 | 442 | 17 |
| current 3,060-run factor | 1,955 | 442 | 17 |

Every listed factor remains complete at ranks 14--17.  The table also shows
real coupling: the local cleanup after raw `C14` pays 34 additional rank-12
holes for better residence and blocker score.

## 5. Mathematical conclusion

Requiring every intermediate rethread to remain one connected factor is
strictly too strong.  The first authenticated escapes exhibit, in order,

1. a 19-component intermediate;
2. two complementary two-component intermediates; and
3. an intermediate with one missing cap and invalid literal phase balance.

In every case the paired union restores the complete protected factor and
strictly improves residence.  Nine consecutive paired floors were escaped
before the exact paired face closed at 3,876.  The correct local object is
therefore a
**balanced packet of alternating circuits with bounded temporary debt**, not
an individually feasible circuit.

The long-circuit census proves a second point: support length pays.  The
number of improving terminal circuits and their best orbit reduction both
increase from `C10` through `C16`.  This is evidence for the regenerative
packet architecture, but it is not a contraction theorem.  The current best
factor still has 3,060 short positive runs and 8,177 short zero gaps.  No
uniform fractional decrease, residence completion, or all-dimensional supply
theorem has been proved.

## 6. Reproduction scope

The principal exact sources are

```text
scratch/search_k17_c68b_double_fusion_residence_c6c8_20260802.cpp
scratch/count_k17_c68b_double_fusion_paired_c6c8_20260802.cpp
scratch/export_k17_marker58_quotient_model_factor_20260802.cpp
scratch/audit_k17_c68b_double_fusion_residence_20260802.cpp
scratch/search_k17_double_fusion_residence_c6_20260802.cpp
scratch/audit_k17_connected_deep_upper_20260802.cpp
scratch/audit_sparse_model_negative_blockers_20260802.cpp
scratch/merge_k17_residence_blocker_round_20260802.cpp
```

Heavy enumeration was performed as optimized C++ on H100 under

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802
```

Every named terminal factor was then independently exported, quotient-audited,
and replayed by the literal cyclic residence auditor.

## 7. Superseding `1,615` scoped floor and mixed-circuit escape

### 7.1 Authenticated base

The later strict-clean base is

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/
  greedy_residence/after_c16x3_c10_c14x3_c12_clean1615_deep1496_255/
```

and has

```text
short positive runs: 1,615 = 731 of length two + 884 of length three
positive deficit:     2,346
short zero gaps:      8,007
rank-11/12/13 holes:  1,496 / 255 / 0
```

Ranks 13--17 are complete.  Literal replay also proves all 24,310 rank-eight
facets, all 24,310 rank-nine owners, all 19,448 rank-ten caps, all 3,944
protected edges, and one physical cycle.  The model and factor hashes are

```text
model   f54d56ba27177cbb9306967008cdc3023edb43326cdd13b9efc79c17802a14bf
factor  a3e5d3eaab97bdac908afb884ec479168446fe81b91f5ebe72cd8dacbe687072
```

This is not a resident carrier: 1,615 forbidden positive runs and 8,007 short
zero gaps remain.  It has no depth-three source antecedent or lower compiler.

### 7.2 Exact single-circuit theorem on this literal base

Every census below fixes the protected facets, requires every rank-ten cap,
requires one literal physical component, replays positive residence exactly,
and fully recounts ranks 11--16 for every connected candidate.

| quotient support | simple circuits | cap-safe | connected | residence-nonpositive | accepted joint improvement |
|---|---:|---:|---:|---:|---:|
| `C6` | 1,878 | 69 | 37 | -- | 0 residence decrease |
| `C8` | 6,210 | 38 | 14 | -- | 0 residence decrease |
| `C10` | 50,937 | 127 | 45 | 2 | 0 |
| `C12` | 415,051 | 244 | 75 | 2 | 0 |
| `C14` | 3,838,450 | 684 | 203 | 2 | 0 |
| `C16` | 36,971,370 | 2,049 | 582 | 5 | 0 |
| `C18` | 6,040 after 1,528,159,889 pruned prefixes | 6,040 | 1,612 | 18 | 4, all at residence 1,615 |

Thus no accepted simple endpoint-retaining `C6` through `C18` decreases the
1,615 positive-run count on this exact base.  The `C18` row is independently
replayed and is not a residence escape: its best point keeps residence 1,615
while improving the rank-11/12/13 holes to

```text
1,462 / 238 / 0.
```

Its model and factor are

```text
/home/amodo/or15/work/qa_k17_clean1615_deep1496_255_independent_20260802_quotientaudit/c18/
  best.model       SHA fb8e8aa64e092fdf532c0d166f5b3c413818c327788c75353515e966c991f3ff
  best.factor.tsv  SHA 5c8e864807c641109b6f430a21064c219417c912000a0d2c9a8cc6317e67c955
```

The exact audit hashes for `C6/C8`, `C10/C12`, `C14`, `C16`, and `C18` are,
respectively,

```text
a5d1ba32c54cb85a98d5967aad39101ba080505aa9d5ae24e34b7518d06bef78
65ccdb8d341b580fc812bff31cea2adb4d2154f18c8869cdd1fea428ac7c74e8
ea4ec87019fbaa1922d93dfbcf278d45edda2264522554c1433376254ea0decf
df3c5a600b2543bd270a48e6920c6bba64e7e6c9f8360b687b103dbac596a0d8
7fc7d145e5c30cd89989cf42b17b511bb60a06835838e1ca3bcd51f0e39436fd
```

### 7.3 Exact disjoint `C6/C8` pair theorem

The complete endpoint-retaining disjoint-pair catalogue contains

```text
8,088 circuits
32,291,639 disjoint pairs
5,622 final cap-safe pairs
1,476 final exact-cap pairs
1,997 final connected pairs.
```

No pair lowers residence below 1,615.  One pair improves only the zero-gap
coordinate.  Exact deep replay of all 31 nonworsening-residence pairs finds a
safe exact-cap `C6+C6` rethread with the same residence and holes

```text
1,479 / 255 / 0.
```

This same-residence point is useful as a new launch state but does not refute
the scoped residence floor.  The pair-census audit SHA is

```text
ed695744372d633ec39df9a66f58613bc161fbc1a02906378e9e079de8cb6710.
```

### 7.4 Mixed `C6+(C10/C14)` escape

The next exact census starts from that same-residence `C6+C6` rethread.  It
enumerates every disjoint pair consisting of one individually cap-safe `C6`
and one individually cap-safe `C10` or `C14`.  Either half may be physically
disconnected; the union must cover every cap and have one physical component.

```text
individually cap-safe C6 circuits:       69
individually cap-safe C10/C14 circuits: 851
disjoint mixed pairs:                56,711
final cap-safe pairs:                56,400
final connected pairs:               15,317
residence-lex improving pairs:            52
```

Full literal deep replay of every residence-decreasing pair finds a winner
with

```text
short positive runs: 1,581 = 748 of length two + 833 of length three
positive deficit:     2,329
short zero gaps:      8,007
rank-11/12/13 holes:  1,462 / 255 / 0.
```

The first half alone has two physical components; the second has one.  Their
union has one physical cycle and passes every stated palette, protection,
connectivity, residence, and deep-upper gate.  The authenticated artifacts are

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/
  greedy_residence/after_mixed_c6_long_clean1581_deep1462_255/

model   SHA 178a91fc4979f359448704085a6ae92f41caff9bf8cb23ab5713a4475af98cfe
factor  SHA 14903257c9dd4082ef571a82aefea753a5cda958807d90958f5e43454d2c9497
```

The mixed enumerator source and O3 binary hashes are

```text
source  7baf227cadb31b912a193f563a4ddb05ea168a68bbc1bc1bba9ee2c06bae28ee
binary  05223ebe412f673cdc39e514610cbfe773aeb32c42de10820556478a7970844e
audit   d6bcb3b42a0d59cc37b0bcdbf010a6f8b47f3728ff1d8fd70bca87d132ad350f
```

### 7.5 Exact scope and exclusions

The frozen negative theorem is only this: on the named 1,615 base there is
no residence-decreasing accepted simple endpoint-retaining circuit of quotient
length 3--9, and no residence-decreasing accepted disjoint `C6/C8` pair.  It
does **not** exclude overlapping circuits, three-or-more-circuit packets,
other mixed support pairs, non-equivariant physical rethreads, linear opening
changes, or changes to the protected marker paths.

The mixed witness proves those exclusions matter: a strict floor for every
tested single circuit and every disjoint short pair is escaped by one
`C6+(C10/C14)` packet.  Even the 1,581 factor is not resident and is not a
`k=17` word or certificate.  It still has 1,581 positive short runs, 8,007
short zero gaps, and no source antecedent or lower compiler.
