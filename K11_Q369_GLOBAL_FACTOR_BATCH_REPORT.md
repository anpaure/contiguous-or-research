# k=11 q369 mixed-schedule global-factor batch

## Status

This report concerns only the fixed single-switch central schedule

\[
I_i=[i,i+2]\quad(1\le i\le369),\qquad
I_i=[i,i+3]\quad(370\le i\le462).
\]

It is not an unrestricted exclusion of a length-465 array.

All 79 local files containing a permutation of the 462 rank-six masks were
enumerated.  For each row the exact generator measured:

- `central_empty_pins`: whether the prescribed central equations already have
  an empty coordinate pin clause;
- `empty_targets`: lower masks of ranks 1 through 5 with no individually legal
  interval of length at most three;
- `selectors`: the number of individually legal target/interval pairs;
- `upper_missing`: masks of ranks 7 through 11 absent from the consecutive-union
  closure of the rank-six row.

The factorable Pareto frontier in `(empty_targets, upper_missing, selectors)` is

| row | empty | upper missing | selectors |
|---|---:|---:|---:|
| `k11_lower956_upper549.txt` | 0 | 13 | 3248 |
| `k11_lower956_upper541.txt` | 0 | 21 | 3239 |
| `k11_recovery_focus11_current.txt` | 0 | 23 | 3166 |
| `k11_lower956_upper543.txt` | 1 | 19 | 3189 |
| `k11_upper_full_candidate.txt` | 60 | 0 | 3201 |
| `k11_upper_full_snapshot2.txt` | 63 | 0 | 3183 |

The last two points show that upper completeness alone is very far from lower
feasibility for this schedule.

## Exact SAT batch

Every factorable row with `empty_targets=0` was encoded, solved by Kissat, and
checked independently by `drat-trim`.  All 17 formulas are UNSAT and all 17
proofs verify.

| row | upper missing | selectors | Hall matching | deficiency | core clauses | core lemmas |
|---|---:|---:|---:|---:|---:|---:|
| `lower956_upper549` | 13 | 3248 | 1018 | 5 | 66 | 19 |
| `lower956_upper546` | 16 | 3266 | 1020 | 3 | 78 | 25 |
| `lower956_upper541` | 21 | 3239 | 1020 | 3 | 9 | 1 |
| `focus14_recover500` | 23 | 3201 | 1019 | 4 | 59 | 13 |
| `recovery_focus11_current` | 23 | 3166 | 1017 | 6 | 26 | 6 |
| `lower956_upper539` | 23 | 3209 | 1016 | 7 | 18 | 1 |
| `lower956_upper533` | 28 | 3216 | 1017 | 6 | 39 | 11 |
| `lower956_upper530` | 32 | 3218 | 1019 | 4 | 27 | 7 |
| `rotated_focus11` | 34 | 3193 | 1016 | 7 | 16 | 1 |
| `focus14_seed` | 35 | 3228 | 1021 | 2 | 200 | 53 |
| `labelable_954_beam` | 38 | 3275 | 1017 | 6 | 15 | 1 |
| `lower_full_956` | 38 | 3275 | 1017 | 6 | 15 | 1 |
| `l949_labelbeam` | 39 | 3261 | 1018 | 5 | 5 | 1 |
| `labelable_953_snapshot` | 40 | 3238 | 1018 | 5 | 5 | 1 |
| `labelable_952_snapshot` | 42 | 3234 | 1017 | 6 | 5 | 1 |
| `lower_random_955` | 46 | 3254 | 1019 | 4 | 24 | 8 |
| `labelable_955_snapshot` | 47 | 3260 | 1016 | 7 | 19 | 5 |

The complete formulas, proofs, solver logs, checker logs, and hashes are in
`scratch/certificates/k11_q369_global_factor/batch_zero_empty/`.

## A cheaper exact obstruction: short-cell Hall deficiency

Let \(\mathcal L\) be the 1023 masks of ranks 1 through 5.  Let \(\mathcal I\)
be the 1392 physical intervals of lengths 1, 2, and 3.  Join a target
\(S\in\mathcal L\) to \(J\in\mathcal I\) when `compatible(S,J)` passes all
four necessary central-envelope tests:

1. the union of the maximal envelopes on \(J\) contains \(S\);
2. every factor position in \(J\) can remain nonzero while contained in \(S\);
3. no prescribed central interval contained in \(J\) has a bit outside \(S\);
4. erasing bits outside \(S\) on \(J\) does not erase every possible pin of an
   intersecting central constraint.

Any genuine factor chooses a different interval for every different target:
one physical interval has only one OR value.  Therefore it induces a matching
saturating all 1023 left vertices.  Failure of Hall's condition is consequently
a rigorous no-go before simultaneous coordinate pinning is considered.

Every one of the 17 rows fails this gate.  Their maximum matchings have sizes
1016 through 1021.  In particular, the best current lower seed is
`k11_focus14_seed.txt`, with deficiency only 2 and 35 missing upper masks.  The
best upper seed, `k11_lower956_upper549.txt`, has deficiency 5 and 13 missing
upper masks.

This changes the correct search score.  `empty_targets=0` checks only the
singleton Hall inequalities.  The next exact gate is

\[
1023-\nu(G_T),
\]

where \(\nu(G_T)\) is the maximum short-cell matching.  Sparse factor SAT is
worth running only after this deficiency reaches zero.

## A nine-clause semantic core

For `k11_lower956_upper541.txt`, an independently extracted core has nine input
clauses and one lemma.  It has the following direct interpretation (positions
are one-based, bit numbers zero-based):

- mask 11 has the unique legal witness `[273,273]`, forcing bit 7 absent there;
- mask 139 has exactly two legal witnesses, `[273,273]` and `[393,395]`;
- the first is impossible because mask 139 contains bit 7, so mask 139 is
  forced to `[393,395]`;
- mask 651 has the unique legal witness `[393,395]`;
- mask 139 omits bit 9 and therefore forces bit 9 absent throughout that
  triple, while mask 651 contains bit 9 and requires it somewhere in the same
  triple.

Here

\[
11\subset139\subset651.
\]

Several other rows have an even smaller five-clause core.  For example,
`k11_l949_labelbeam.txt` forces both masks 89 and 93 to the same pair
`[202,203]`; because the masks differ, this is impossible.

These cores confirm that the batch failures are not difficult SAT phenomena.
They are small short-cell allocation obstructions, exactly detected by the
Hall gate.

## Next search target

Run permutation/path local search with the lexicographic or Pareto score

1. mixed-schedule central pin deficit;
2. lower short-cell Hall deficiency;
3. upper missing masks;

and invoke the exact sparse-factor SAT encoding only at Hall deficiency zero.
The first four seeds should be:

- `k11_focus14_seed.txt`: Hall 2, upper 35;
- `k11_lower956_upper546.txt`: Hall 3, upper 16;
- `k11_lower956_upper541.txt`: Hall 3, upper 21;
- `k11_lower956_upper549.txt`: Hall 5, upper 13.

Moves should retain the rank-five/top-layer feasibility and Johnson-forest
structure when possible.  A repaired row must first cross the Hall-zero gate;
only then do the genuinely harder simultaneous pin-survival constraints become
relevant.
