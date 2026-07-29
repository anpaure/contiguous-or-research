# `k=15` is exact: `nu(15)=6438`

Date: 2026-07-29

Status: independently verified optimal certificate.

## Result

For `k=15`,

```text
r = 8,
W = binom(15,8) = 6435,
d(15) = 3,
B(15) = W+d = 6438.
```

The general deadline/depth theorem proves `nu(15) >= 6438`.  The canonical
retained word is `answers/k15.word`, byte-identical to the search artifact

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    arbitrary_seams.s44.t12863.word
```

has length `6438` and SHA-256

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b.
```

The independent verifier reports

```text
covered nonempty masks     32767
missing masks                  0
middle row exact             yes
middle width                6435
word length                 6438
lower bound B(15)           6438
status          VERIFIED_OPTIMAL
```

Therefore

```text
nu(15) = 6438.
```

## Construction chain

The source is the independently audited all-depth resident factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.best.json
```

with SHA-256

```text
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555.
```

It has two physical cycles of lengths `6390` and `45`, minimum coordinate
run four, and zero cyclic lower or upper shadow holes at every depth.

All `2,300,400` directed state pairs between the two cycles were enumerated.
The exact ledger was

```text
residence-safe pairs             34740
upper-safe pairs                   480
boundary-SDR/compiler candidates    60
```

The winning opening is

```text
source state       44
target state    12863
component order   0,1
cut positions    22,41
orientations       0,1
```

Its connecting seam is Johnson (`symmetric_difference_size=2`) but is not a
lower-q1 recycling seam.  Consequently the linear middle carrier has exactly
two missing rank-seven colours,

```text
18033, 18553,
```

and no missing lower target at any other depth.  Those two colours have an
injective assignment to the two global high boundary cells.  Every upper
target survives or is recreated by a literal cross-seam interval.

The exact generalized compiler then has

```text
base literal targets          4943
boundary residual targets        2
ordinary Hall deficiency          0
assigned targets              4945
adaptive CP-SAT wall time     2.389 s
```

and emits the retained word.  The full search/compiler audit is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    arbitrary_seams_compile.audit.json
```

with SHA-256

```text
5eeb04a61d8a085e89b05db9ca1075cfd64e5f95a9a35bcbb80711617579d125.
```

The separate local verification record is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    arbitrary_seams.s44.t12863.independent.verify.json.
```

A second root-level replay is retained as

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    arbitrary_seams.s44.t12863.root.verify.json.
```

The exhaustive seam enumerator is
`scratch/search_k15_two_cycle_arbitrary_seam_20260729.py`.

## Structural lesson

The final seam does **not** recycle either removed lower-q1 colour.  The old
one-recycled-colour restriction was unnecessarily strong: with two opened
cycles, the two global boundaries can absorb both cut colours exactly.  This
is the decisive endpoint mechanism:

```text
two all-depth resident cycles
    + one upper-safe seam
    + two boundary q1 assignments
    + exact lower compiler
    = an optimal word.
```

This is reusable.  For a `c`-component resident all-depth factor, seam search
must optimize the joint trade between recycled cut colours and the `c+1`
special row-`d-1` cells; requiring every seam to recycle a colour can exclude
the optimal opening.
