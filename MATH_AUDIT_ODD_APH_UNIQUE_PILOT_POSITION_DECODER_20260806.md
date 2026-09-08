# Audit of the unique-pilot position decoder

**Date:** 2026-08-06  
**Audited file:** `MATH_THEOREM_ODD_APH_UNIQUE_PILOT_POSITION_DECODER_20260806.md`  
**Audited SHA-256:** `392bcaf38aa8bbac377cf4b30082024ff88941b3051bbf74d3d8ee73b6f24e9f`  
**Verdict:** **FAIL.**  Theorem 4.1 is false under its stated hypotheses.
The unique pilot address separates macro checkpoints with different completed
counts, but it does not mark which of the two later adjacent pairs is active.

## 1. An exact collision on an intended application row

Use the literal application values

```text
H = 02,   M = 11,   B = 20,   P = 01.
```

Take the train `X1|X2|P = H|H|P` and cross the tape block `Y=B`.
For both the second and third arrows of (3.1), choose the following simple
path in the capacity-two, mass-four layer:

```text
H|B = 0220
    -> 0211
    -> 0202
    -> 0112
    -> 1012
    -> 1102
    -> 2002 = B|H.
```

Every displayed step transfers one unit across one adjacent physical edge,
and all seven vertices are distinct.  It is therefore a valid fixed simple
path of exactly the kind assumed in Section 3.

During arrow 2, the active path occupies block positions 2--3.  At its local
state `1102 = M|H`, the full four-block word is

```text
H | M | H | P = 02 | 11 | 02 | 01.                 (1.1)
```

During arrow 3, the active path occupies block positions 1--2.  At its local
state `0211 = H|M`, the full four-block word is again

```text
H | M | H | P = 02 | 11 | 02 | 01.                 (1.2)
```

The two occurrences have the same source, the same protected record `Q`, the
same direction, the same crossing count, the same literal pilot value, and
the same physical pilot address.  They have different arrow numbers and
different local microsteps.

All pilot hypotheses hold.  A stationary `D` may be placed elsewhere; `P`
is the unique pilot block; `B` is not in the pilot alphabet; and the same `Q`
labels both occurrences.  The two special bullets in Section 3 constrain
only first-arrow routes, so they do not exclude this arrow-2/arrow-3
intersection.  With only one first-arrow branch they can be satisfied
vacuously.

This is also within the intended application alphabet: the earlier pilot
proposal explicitly allows an `H|H|P` train and a crossed background block
`B`.

## 2. Exact proof failure

The sentence

> Inside the second and third arrows the pilot is fixed immediately beside
> the active pair. Its side distinguishes the two arrows.

is false for two independent reasons.

First, in arrow 3 the trailing pilot has the fixed `X2` block between it and
the active pair.  Second and more importantly, the active pair is not
literally marked in the full word.  At (1.1)--(1.2), the same word can be
parsed either as

```text
H | (M|H) | P       [arrow 2]
```

or as

```text
(H|M) | H | P       [arrow 3].
```

Individual path simplicity proves injectivity only within one chosen path.
It gives no disjointness between two differently embedded paths.  Hence the
ordered endpoint type is not recoverable before the arrow number is already
known; invoking it is circular.

## 3. Scope of the failure

The counterexample disproves assertions 4 and 5 of Theorem 4.1 and therefore
the claimed equality-of-full-states conclusion.  It does not disprove the
possibility of a repaired pilot construction.

A proof-safe repair must add at least one of the following and verify it for
the actual literal path bank:

1. a phase tag distinguishing arrows 2 and 3 throughout their strict
   interiors;
2. a joint path-bank theorem saying that the two differently embedded paths
   are disjoint except at their declared common endpoint, together with the
   analogous adjacent-crossing exclusions; or
3. a specially selected local route table for which those disjointness
   statements are checked directly.

The first-arrow meeting hypothesis alone is insufficient.

Corollary 4.2 depends on Theorem 4.1 and is consequently unproved.  Its
inverse-permutation restoration statement remains algebraically plausible,
but simplicity/disjointness of the out-and-back graph walk does not follow.

Finally, setup and teardown were never consequences of Theorem 4.1: Section
6 itself lists their literal routes as remaining finite rows.  This audit
does not treat those conditional routes as supplied, and makes no stronger
negative claim about them.
