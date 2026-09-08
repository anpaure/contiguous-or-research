# Exact two-replacement no-go around the canonical 476-entry near-word

Date: 2026-07-24

## Result and scope

Let `W` be the first 476 entries of `k11_completed_477.txt`, i.e. delete its
last entry `493`.  Direct interval-OR enumeration gives

```text
length=476 covered=2046/2047 missing=1
missing: 493
```

Every array obtained from `W` by changing the values at zero, one, or two
arbitrary positions remains nonuniversal.  Replacement values range over all
2,047 nonzero 11-bit masks.  This is an exact local theorem, not a proof that
an unrestricted universal 476-entry word is impossible.

The result has two independent exact derivations: a canonical position-pair
solver that enumerates the full value square for every pair, and a separate
hole-witness decomposition.  Their algorithms and state spaces are different.

## 1. Canonical position-pair solver

The primary solver is
`scratch/search_two_replacements_by_pair.cpp`.  It selects every pair
`p<q`.  For each target whose old witnesses all meet `{p,q}`, it precomputes
the three exact categories of changed intervals:

1. intervals containing `p` only, with value `base | x`;
2. intervals containing `q` only, with value `base | y`;
3. intervals containing both, with value `base | x | y`.

It then checks every ordered value pair
`(x,y) in {1,...,2047}^2`.  Allowing either value to equal the old entry also
includes zero- and one-change words.  Targets outside the pair's repair mask
retain an untouched old witness.  Therefore equality between the repair mask
and the union of the three category tables is necessary and sufficient.

The completed run reports

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450 max_base_counts=40,40,40
```

where

```text
113050 = binom(476,2)
473703127450 = 113050 * 2047^2.
```

The process status is `20`.  Thus the count is the literal full Cartesian
product, not a sampled or target-restricted screen.

### Independent audit

`K11_476_TWO_REPLACEMENT_PAIR_SOLVER_INDEPENDENT_AUDIT.md` proves the
position-pair repair-mask formula and the three interval-category tables.  Its
independent Python-integer-bitset oracle checked:

```text
PASS cases=3757 sat_cases=2522 position_pairs=25934
     value_pairs=938638 black_box_cases=120 seed=18274
LARGE_WORD length=476 pairs=113050 old_missing=1
           max_pair_missing=33 pairs_le_33=113050
```

The same test under AddressSanitizer and UndefinedBehaviorSanitizer passed
3,357 cases and 60 black-box runs.

### Frozen hashes

```text
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b  k11_completed_477.txt
69b6669501785d9fc8c15c226c109610cdd645029149dcd077eec19aff709f9d  scratch/search_two_replacements_by_pair.cpp
f1acf4ea4dc696a8083de66ef233e9776dba5db13e64fb81ede90d31c5040b09  scratch/k11_476_two_replace_pairwise_full.out
fbfad674e7bcf7c412234455fe3081709b8ef16a72aada849988155f1438cf2b  scratch/k11_476_two_replace_pairwise_full.log
5378796307535df3ec8d8b15a2e2dc5641419c3d3060cfe32238c0fa973f7aa3  scratch/k11_476_two_replace_pairwise_full.status
8f10c5bb159eb31d56ceeb5cf63c807022610c4676cbe216530a7306390dcc0d  K11_476_TWO_REPLACEMENT_PAIR_SOLVER_INDEPENDENT_AUDIT.md
```

The independent-audit note records SHA-256
`5555be7513e6f21d6a19d3dab2024060edaac3f521280c3640c5cb29a390a0ab`
for the oracle snapshot used in that audit.  The live oracle file was extended
after the note was frozen, so its later workspace hash is intentionally not
substituted for the audited snapshot hash.

## 2. Independent hole-witness decomposition

The second derivation uses only the fact that `493` is absent from `W`.
Consider any final word differing at at most two positions and choose an
interval whose final OR is `493`.

### Case A: the witness meets one changed position

Changing that position alone to its final value already creates `493`.
`search_literal_hole_two_replacements.cpp` enumerates every such
target-creating first value.  After it computes the complete intermediate
missing family, it intersects, at every second position, the exact value sets
that can create every missing target.  A surviving value is materialized and
verified by full interval enumeration.

The full result is

```text
NONE first_candidates=4514
     pairs=2144150
     intersections=35596
     evaluated=35596
     minimum_intermediate_missing=1
```

### Case B: the witness meets both changed positions

Every unchanged seed entry inside the final `493` witness must be a submask of
`493`; otherwise it would contaminate the OR.  Therefore the corresponding
seed interval contains at most two non-submask ("bad") entries, and every bad
entry is one of the selected positions.

`search_joint_hole_two_bad.cpp` enumerates every such interval, every
admissible position pair inside it, and every nonzero submask assignment
`(x,y)` satisfying

```text
OR(unchanged interval entries) | x | y = 493.
```

It deduplicates identical `(p,q,x,y)` candidates and verifies each remaining
word exactly.  The result is

```text
NONE configurations=1524
     generated=7432393
     unique_tested=3848263
```

Cases A and B exhaust every possible final `493` witness.  Hence this is an
independent exhaustive proof of the same two-replacement no-go.

An end-to-end small-instance audit compared the union of the two programs
with direct brute force on 169 one-hole words in dimensions one through
three:

```text
PASS cases=169 one_hole_words_k1_to_k3=1
```

Frozen hashes:

```text
f8242093bd0b5c63b86548faba1ab6c53d004aba7eb1ed456e45e67bd3c0385f  scratch/search_literal_hole_two_replacements.cpp
bbec0b20061f3c203bc3315a2d3528c994f9588649560627c0e0fd80e49d0da1  scratch/search_joint_hole_two_bad.cpp
43ed43cc82e8d4989ea28f78d38327c42969dde714b580f850b0552916f2b81e  scratch/audit_two_replacement_hole_decomposition.py
1e5e986111951a6f11de6b079b8df6013eaa6bbba1e4a63f6edc92ea5106830e  scratch/k11_476_one_sided_hole_two_replacements.log
c01a209ffbef99c8726fdfc9f460425a0d70c2ddbf0d8ddea879d8fc0f1c7d7a  scratch/k11_476_joint_hole_all_inside.log
```

## 3. A second relocated near-word

The word `scratch/k11_476_drop_last_one_move.word` is obtained from the same
seed basin by one arbitrary relocation.  It independently verifies as

```text
length=476 covered=2046/2047 missing=1
missing: 493
```

The canonical full pair/value solver also returned the complete negative
ledger on this word:

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450 max_base_counts=40,40,40
```

Hashes:

```text
660cb2ac66e1e357e7276be2b01b6399f9781485715cd2afb0964eeea11089ad  scratch/k11_476_drop_last_one_move.word
f1acf4ea4dc696a8083de66ef233e9776dba5db13e64fb81ede90d31c5040b09  scratch/k11_476_relocated_two_replace_full.out
d38c6899157ce856e22bdf00639d111444b7898b781590b137621f3fd708e8fe  scratch/k11_476_relocated_two_replace_full.log
5378796307535df3ec8d8b15a2e2dc5641419c3d3060cfe32238c0fa973f7aa3  scratch/k11_476_relocated_two_replace_full.status
```

This is a separate local theorem; relocation plus two replacements is not the
same move family as two replacements around `W`.

## 4. Other exact one-move screens and unrestricted heuristic result

Before the full pair theorem, the following one-move families around `W`
were exhausted:

```text
all-value one-position replacements       973,896
all swaps                                  113,050
all single relocations                     226,576
all interval reversals                     113,050
```

None is universal.

An unrestricted two-thread annealing run made about 27.8 million exact
evaluations using replacements, bit edits, swaps, relocations, reversals, and
coupled rewrites.  It found a substantially different 476-entry word, with 54
positions differing from `W`, that still misses exactly one rank-seven mask:

```text
length=476 covered=2046/2047 missing=1
missing: 1763
```

Its capped witness redundancy improved from 3382 to 3386.  Two independent
interval-OR evaluators agree on its missing family.  A deterministic plateau
search then expanded 1,000 one-hole states and checked

```text
4,334,714 exact target-creating repairs
5,638,551 neutral/interleaved neighbors
347,488 distinct one-hole states discovered
```

without improving 2046/2047.

The canonical pair/value solver was then run over the complete two-replacement
neighborhood of this 54-position-different SA word as well.  It returned

```text
UNSAT_SCREEN selected_pairs=113050 value_pairs=473703127450 max_base_counts=40,40,38
```

with status `20`.  Hence the strongest heuristic basin is also locally exact
through two arbitrary additional replacements; this is substantially stronger
than the plateau walk alone.

Hashes:

```text
e866a1fb22dbb8675d9e33fad6d803eaf75721fd5b6c85d4e4186d652688cd87  scratch/k11_unrestricted_476_best.word
f21a76645a8af007c98713a2fc82ccb39b9f54c8a378155d4df9d4769fa396a0  scratch/k11_unrestricted_476_best.verify_quadratic.txt
d00631638d5280011cf1072bf68e9b44bf2a035f32f62266ab951597c948d889  scratch/k11_unrestricted_476_best.verify_suffix.txt
bb27f58db3faf95a11ac6418c3a330b96fd42901f8241a9e7463fc59f29e1dd5  scratch/k11_476_plateau_from_sa_best_1000.log
88d1160ff4995d695b50c6bccf121f4361412b1ac487836ee648a927c2d951ff  scratch/k11_476_sa_two_replace_full.out
80f017bb44ef64eede6ce9948188f37f0efe882d7413988a160877a35ea70733  scratch/k11_476_sa_two_replace_full.log
5378796307535df3ec8d8b15a2e2dc5641419c3d3060cfe32238c0fa973f7aa3  scratch/k11_476_sa_two_replace_full.status
```

## 5. Exact three-replacement progress, with limited scope

The complete radius-three replacement neighborhood of `W` has **not** been
exhausted.  Two exact fixed-first branches and one exhaustive hole-witness
case have, however, been closed.

### 5.1 Two complete fixed-first branches

Positions in this section are zero-based.  Starting from `W`, consider the
two intermediate words

```text
branch A: position 469 changes from 941 to 493
          intermediate missing family = {941}

branch B: position   0 changes from 128 to 429
          intermediate missing family = {504, 1528}
```

For each intermediate word, the canonical pair/value solver selected all
`binom(476,2)=113050` residual position pairs and all `2047^2` ordered
nonzero value pairs.  In both branches it returned

```text
UNSAT_SCREEN selected_pairs=113050
             value_pairs=473703127450
             max_base_counts=40,40,40
```

with status `20`.  Thus neither fixed first edit can be followed by zero, one,
or two arbitrary value replacements to produce a universal word.  The
residual replacements are allowed to include the position of the fixed edit,
so overwriting that edit is included as well.

Frozen hashes:

```text
f1acf4ea4dc696a8083de66ef233e9776dba5db13e64fb81ede90d31c5040b09  scratch/k11_476_three_edit_469_493_full.out
81afe0a08e377e1abae7df762b040676c2ed746ad5fe200c440a153b4877c8ea  scratch/k11_476_three_edit_469_493_full.log
5378796307535df3ec8d8b15a2e2dc5641419c3d3060cfe32238c0fa973f7aa3  scratch/k11_476_three_edit_469_493_full.status
f1acf4ea4dc696a8083de66ef233e9776dba5db13e64fb81ede90d31c5040b09  scratch/k11_476_three_edit_0_429_full.out
8c46b25fcb7209f44a84ed17a97d9e307797f41f96763fcbc7cd6c8da8bf4f08  scratch/k11_476_three_edit_0_429_full.log
5378796307535df3ec8d8b15a2e2dc5641419c3d3060cfe32238c0fa973f7aa3  scratch/k11_476_three_edit_0_429_full.status
```

### 5.2 Exact case: the final `493` witness meets all three changes

Suppose a final word differs from `W` at three positions `p<q<r`, and some
final interval witnessing the missing mask `493` contains all three changed
positions.  Every unchanged seed entry between `p` and `r` must then be a
submask of `493`; any outside bit would contaminate every such witness.

`scratch/search_three_replacements_joint_hole.cpp` enumerates every triple
satisfying that necessary condition.  For each triple it builds the seven
exact changed-interval categories (`p`, `q`, `r`, `pq`, `pr`, `qr`, and
`pqr`) and screens every assignment of three nonzero submasks of `493`.
Enumerating all submask assignments is conservative: it includes assignments
that do not themselves create `493`, which simply fail the exact target
coverage test.

The completed run reports

```text
UNSAT_SCREEN eligible_triples=1071
             assignments=2193818193
             maximum_endangered=36
             maximum_bases=36
```

with status `20`.  Therefore no three-replacement solution exists whose final
`493` witness contains all three changed positions.

An independent black-box audit compared the solver against direct exhaustive
enumeration on 250 one-hole words in dimensions at most three:

```text
PASS cases=250 joint_three_hole_black_box=1
```

Frozen hashes:

```text
ad1184e22f45c4bf07c0c05635f8e45a7faff7d3f4f59ae238bead96bf1121a4  scratch/search_three_replacements_joint_hole.cpp
77e26446a594f4133cc5a715924e1e8ab1cbde3a4a24a5c5e95b1e178b767a8b  scratch/k11_476_three_replace_joint_hole.out
0855fa6f079c587f454a5220b8c4980621007601182629e7403fece3edece0eb  scratch/k11_476_three_replace_joint_hole.log
5378796307535df3ec8d8b15a2e2dc5641419c3d3060cfe32238c0fa973f7aa3  scratch/k11_476_three_replace_joint_hole.status
5fe3b3e33b0e310835ebaef0205416d83539eb5a64b2267a561d999f8301885f  scratch/audit_three_replacements_joint_hole.py
3b4daf648625c515c452d282bea801791285aff53a1b29d867a26df6ebd18a85  scratch/k11_476_three_replace_joint_hole.audit.out
```

These results do not close the remaining cases in which a final `493`
witness meets only one or two of three changed positions.  In particular,
only two of the 4,514 possible target-creating first assignments have received
the full residual pair/value screen.  This section is therefore exact within
its stated branches, not a proof that every three-replacement word is
nonuniversal.

## 6. Redundant exact recency CNF

An independent at-most-two-replacement last-occurrence CNF was also built.
Targets with three pairwise-disjoint exact seed witnesses are omitted because
two changed positions cannot hit all three witnesses.  This leaves

```text
robust targets       173
nonrobust targets  1,874
variables       1,850,373
clauses        33,004,991
CNF size             819 MB
```

The generator agrees with direct brute force on 274 exhaustive/random small
instances and was regenerated byte for byte.  A 300-second Kissat run did not
return a verdict.  The canonical pair solver and independent hole
decomposition already establish the local theorem, so this redundant large
benchmark was stopped rather than consuming further resources.

## Conclusion

The canonical 476-entry near-word is not one or two value changes away from a
solution, and even a natural relocated near-word has no solution within two
further replacements.  The best unrestricted search word remains at
2046/2047.  This materially deepens the local negative radius but leaves the
global bounds unchanged:

```text
465 <= nu(11) <= 477.
```

Further constructive work must use at least three coordinated value changes
from the canonical seed, a move family outside the audited relocation basin,
or a qualitatively different 476-entry architecture.  The exact results in
Section 5 close two full fixed-first radius-three branches and the all-three-
inside-hole witness case, but they do not establish a complete radius-three
no-go theorem.
