# Exact five-parent intrinsic support-eight census at `k=15`

## Result

Relative to the Hall-29 parent `P0`, and using the five canonical parent
successor sets `P0,...,P4`, every globally intrinsic transfer permutation with
support exactly eight that can satisfy all of the following was exhausted:

1. the transferred closed factor opens to one Hamilton path on all 6435
   middle vertices;
2. depth-three residence is exact;
3. every upper target at depths `q=1,...,7` remains covered.

There are exactly **486** such paths.  Their exact depth-three compiler Hall
deficiencies have minimum **34**, so none improves the Hall-29 parent.

This is a finite theorem about the five-parent atlas, not a theorem about
arbitrary `k=15` paths.

## Normal-form completeness

A fixed-point-free permutation on an eight-point support must have even sign
in order for the even closed base cycle to remain one even closed cycle.  The
complete cycle-type list is therefore

```
6+2, 5+3, 4+4, 2+2+2+2.
```

No other derangement type on eight points has the required parity.

The first three types are exhaustively formed from the complete bounded-degree
transfer-digraph cycle lists.  Their exact census is:

| type | disjoint | globally intrinsic | Hamilton | residence-safe | all-upper | Hall values |
|---|---:|---:|---:|---:|---:|---|
| `6+2` | 406,784 | 368,335 | 73,303 | 7 | 0 | — |
| `5+3` | 147,152 | 127,070 | 24,810 | 0 | 0 | — |
| `4+4` | 49,060 | 42,408 | 8,581 | 11 | 3 | `34,35,36` |

Global intrinsic status is the AND of **all eight directed source masks**.
It is not approximated by a componentwise-rainbow test.

## Exact `2+2+2+2` index

There are 818 literal transfer transpositions and

```
binom(818,4) = 18,518,759,260
```

raw four-edge subsets.  They are not scanned.  Sort the eight endpoints in
base-cycle order and retain their chord matching.  Among the 105 perfect
matchings of eight cyclic positions, exact first-return monodromy gives

```
21 one-component, 70 three-component, 14 five-component patterns.
```

Only the 21 one-component patterns can be Hamilton.  Each such pattern has a
canonical split into two crossing chord pairs.  The physical index contains
118,600 crossing-pair kernels.  For each partial pair, every residence
violation supplies a necessary clause: a completing pair must change a tail
on that violating word.  If no available outside transposition touches the
clause, the violation survives every disjoint completion, so discarding that
kernel is proof-safe.  This rejects 114,918 impossible kernels and leaves
3,682 indexed kernels.

The 21 exact positional boxes plus the necessary mutual-rescue clauses scan
512,108 postings, of which 45,614 meet the exact chord box and 1,638 meet both
necessary rescue ledgers.  Literal full-permutation replay then gives:

| quantity | count |
|---|---:|
| globally intrinsic candidates after proof-safe prefilters | 1,523 |
| parent-pure candidates after the same prefilters | 115 |
| intrinsic residence-safe | 1,505 |
| intrinsic residence-safe and all-upper | **483** |
| parent-pure candidates | 115 (not evaluated in this intrinsic run) |

The 483 legal intrinsic paths have Hall distribution

```
39:5, 40:33, 41:87, 42:124, 43:115, 44:77,
45:29, 46:12, 47:1.
```

Thus the `2+2+2+2` minimum is 39.

## Independent replay

Production source:

```
scratch/enumerate_k15_intrinsic_multiparent_support3_8.cpp
SHA-256 722731a8fdc51b4c3924be165e9a83d59f6e07da8dd3191bab75e460aa2d2d94
```

Compact frozen output:

```
scratch/k15_support8_intrinsic_20260728/summary.json
SHA-256 91ba35ce110080655e32893dabb865893968ae20d1a99d6899ae784a64842ea3

scratch/k15_support8_intrinsic_20260728/hall.jsonl
SHA-256 81043d44130c6b8b2254cde94c9d5e63a808fc47083da462916badd77c5462ad
```

An independently organized Python checker literally reconstructs each
transfer from the five raw parent paths, verifies global source-mask AND zero,
traverses all 6435 vertices, recomputes residence and all seven upper shadows,
and rebuilds the compiler Hall graph in Python.  It agrees candidate-by-
candidate with the optimized C++ Hall auditor:

```
scratch/audit_k15_support8_exact.py
SHA-256 209c23f896bf400c310094c95667c3b5ca54af8e9a44aa5e65f4cfc20ce18a47

scratch/k15_support8_intrinsic_20260728/independent_audit.json
SHA-256 6a41486740c16b05f6bb3fa8d1f6243db9edfc056d042b375f75c4bc893a13a6
```

The independent Hall histogram over all 486 paths is

```
34:1, 35:1, 36:1, 39:5, 40:33, 41:87, 42:124,
43:115, 44:77, 45:29, 46:12, 47:1.
```

## Exact scope left open

This closes globally intrinsic, single-transfer moves of support at most eight
inside the five canonical parent atlas once combined with the frozen
support-`<=7` census.  The zero-valued parent-pure residence/upper counters in
the production summary are **not** no-go counts: parent-pure cases were counted
but deliberately skipped by this intrinsic run.  Parent-pure support seven was
audited separately because it can improve a seed without being intrinsically
multiparent.  Parent-pure support eight, support nine and larger, compositions
of several transfers, and paths using arcs outside the five-parent union are
not consequences of this note.
