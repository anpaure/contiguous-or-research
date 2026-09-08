# Exact finite benchmark for the monotone-radius rotor integral gate

## Problem

This benchmark fixes

\[
m=4,\qquad h=1,\qquad H=3,
\]

on eight coordinates.  A queue is a permutation

\[
(z_{-1},z_0,\ldots,z_6)
\]

and exposes three middle centers.  Profiles are restricted to
\(a_1=2\) or \(a_1=3\), i.e. radius sequences \((1,1,0)\) and
\((1,1,1)\).

The requested packing has 24 atoms.  Every one of the 56 rank-3 masks and
56 rank-5 masks must occur exactly once, and every one of the 70 middle
masks must occur at least once.  Since every atom has three centers, the
last condition is exactly middle duplicate excess two.

The depth-incidence equation is

\[
2n_2+3n_3=56,\qquad n_2+n_3=24,
\]

so necessarily

\[
n_3=8,\qquad n_2=16.
\]

## Exact symmetry reduction

Every solution contains a type-3 atom.  Coordinate permutations act
transitively on its eight-coordinate queue, so one type-3 atom may be fixed
to

```text
0 1 2 3 4 5 6 7
```

without loss of generality.  Its three lower and three upper shadows are
then already covered.  Any other selected atom must avoid those six masks.

Enumerating all two profile types over all `8!` queues, removing the fixed
atom and the incompatible queues, leaves

```text
63,625 candidates, of which 30,385 have type 3.
```

## Exact CNF

The generator is

```text
scratch/rotor_m4_h1_packing_sat.cpp
```

and the formula is

```text
scratch/rotor_m4_h1_packing_20260724/packing.cnf
```

with map

```text
scratch/rotor_m4_h1_packing_20260724/packing.map.
```

The formula has

```text
864,951 variables
2,404,043 clauses
5,797,917 literals.
```

Its SHA-256 values are

```text
CNF        312d55510b038f1aa1ead26f9dd5bc46fe72ebc5f0a7c8740aaa4518c8f3f028
map        83b7c6931e7a0a29f7aec98cb3311995c4b501fb1f358736b3cf3f618fb29392
generator  f4a43bcf39e85f355bd635f4ec7c9a27d05b901bb9b6f003beb8758fb759956e
```

For each uncovered rank-3 and rank-5 mask, the CNF has one support clause
and a sequential at-most-one constraint.  Every uncovered middle mask has a
support clause.  An exact unary counter selects seven further type-3 atoms.
Summing the exact rank-3 rows then forces sixteen type-2 atoms, so the total
of 23 additional atoms is a theorem of the CNF rather than an omitted
cardinality assumption.  The 70 middle support rows, together with the
forced 72 center incidences, force duplicate excess exactly two.

## Independent certificate verifier

For a SAT list, the checker

```text
scratch/verify_rotor_m4_h1_packing.py
```

independently verifies:

- 24 permutation queues and profile counts `8/16`;
- exact rank-3 and rank-5 multiplicity one;
- all 70 middle masks and duplicate excess two;
- the actual six-entry MTF reset/update word for every atom; and
- every claimed band mask as a literal suffix OR at the appropriate
  endpoint of the concatenated 144-entry word.

The verifier SHA-256 is

```text
356af8d6537e7099d8f74e96667a2cf3bce1097eb9ad00ccb39d76a05bbf3fa7.
```

## Solver status

The first exact Kissat run reached its 600-second wall limit with
`s UNKNOWN`.  A separate randomized exact-cover traversal has not found a
packing; this is heuristic nonfinding only.  A complementary focused,
phase-zero exact run and a simulated-annealing search were subsequently
stopped without a terminal result when compute was returned to the finite
`k=11` search.  Their durable partial logs are

```text
scratch/rotor_m4_h1_packing_20260724/solve_phase0.log
scratch/rotor_m4_h1_packing_20260724/sa.log
```

No SAT or UNSAT conclusion is recorded until a model is independently
decoded and checked, or an UNSAT proof is independently verified.  In
particular, the present finite benchmark remains **undecided**.
