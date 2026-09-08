# Exact variable-delete formula for the five-deletion plus 16-append neighborhood

## Scope

Start with the fixed 465-entry partial word in
`k11_upper549_natural_array.txt`.  Delete exactly five entries, retain the
other entries in order, and append exactly sixteen nonzero 11-bit masks.  The
completed word has length

```text
465-5+16=476.
```

There are

```text
C(465,5)=177,301,977,468
```

fixed deletion branches, too many for the preceding branch-by-branch screen.
The formula described here represents all of them simultaneously.  It is a
restricted repair neighborhood, not the unrestricted length-476 problem.

## Exact recency state

For every original prefix position, a Boolean variable chooses whether that
entry is deleted.  A deterministic one-hot counter forces exactly five
deletions.

The formula carries the last-occurrence state through all 465 original
positions.  A deleted position preserves the state; a retained position
updates it with the fixed entry.  The state records

- whether each coordinate has appeared;
- every strict comparison between the last occurrences of two coordinates;
- the exact last fifteen retained physical entries for each coordinate.

The sixteen appended masks are variable and nonzero.  Each performs the same
exact move-to-front recency transition.

At a physical endpoint, target `T` is a suffix OR exactly when every bit of
`T` has appeared later than every bit outside `T`.  One selected endpoint is
required for every nonempty mask.  Original endpoints are guarded against
being deleted.

## Exact containment caps and endpoint cuts

At total length 476, the audited containment theorem gives target witness
deadlines

```text
rank 1-5     14
rank 6       15
rank 7       21
rank 8       42
rank 9       98
rank 10     224
rank 11     476.
```

The 15-entry history register enforces the first six ranks exactly.  Higher
ranks retain the unrestricted, still exact suffix criterion; omitting their
redundant longer caps does not change satisfiability.

Ranks five and six each contain 462 targets.  Their selected witnesses are
explicitly at-most-one per physical endpoint.  A compact selected-label
channel enforces containment when consecutive ranks share an endpoint.
These clauses are logically implied by the suffix-chain semantics but improve
propagation.

## Production inventory

The frozen production command is

```sh
scratch/delete_append_recency_cnf \
  11 5 16 \
  k11_upper549_natural_array.txt \
  scratch/k11_length476_five_deletion_variable_20260724/delete5_append16.cnf \
  scratch/k11_length476_five_deletion_variable_20260724/delete5_append16.map \
  5,6 15
```

It produced

```text
endpoints                         481
target occurrence variables  984,607
variables                   2,523,666
clauses                    43,004,593
literals                  131,092,440
CNF bytes               1,000,837,997
generation wall time          42.27 s
```

The durable hashes are

```text
5fa707184dbec376f20566a885d9acc102bc21ba2901fbff5ff8278e5b5465b6  delete_append_recency_cnf.cpp
6ef35d27ff056be36b60f644c5c24b9e874fb5b47487a216781e5a336bcf0546  production generator binary
7362799ace9a7d8062658f646a5a079858c0c14263ac116e4fff161d6faf0f55  delete5_append16.cnf
262e23f644625d61b1dad97fd1b0507a84986debcea7e49cc7f14ebdd005b64c  delete5_append16.map
```

## Independent validation

The finite checker compares the formula with literal enumeration of every
deletion set and append word on 1,601 exhaustive/sampled small instances.  It
decodes every SAT model and rechecks its completed word by quadratic interval
OR enumeration:

```text
PASS exhaustive_and_sampled_instances=1601
```

A separate audit exercised history caps 0, 1, and 2 on another 1,074
instances, covering the unbounded-state fallback.

An independent streaming DIMACS parser confirmed the exact declared counts,
maximum variable, literal count, clause termination, and absence of empty or
out-of-range clauses.  The map was parsed independently.  Finally, a
separately compiled binary regenerated the one-billion-byte CNF and map byte
for byte.

The detailed source and production audits are

```text
DELETE_APPEND_RECENCY_CNF_AUDIT.md
APPEND_RECENCY_CIRCUIT_AUDIT.md
```

with SHA-256 values

```text
9569fb8f81f4444626d2527dad2305e05021ce0ed0d5fa696dfcdf700d799087
a9bae42ce62b94becfcfe3ea039b2e4072cf506cec743f719cff6ba7c51daec2
```

## Width-gated constructive and fixed-branch search

A separate joint annealing search mutates both the five deleted prefix
positions and the sixteen appended masks.  Published scores use exact
contiguous-OR coverage, followed by an exact directed mask distance and
capped physical witness multiplicity.  An independent quadratic counter
agrees on 1,204 test words.  Exact Dilworth width of the retained prefix's
missing family is now a hard gate: a branch of width greater than sixteen
cannot be completed by sixteen new right endpoints.

This gate caught an instructive false lead.  The heuristic reached
`2045/2047`, but its deletion set had missing-family width seventeen, so the
near-solution was structurally impossible.  It is archived as
`infeasible_width17_covered2045.*` rather than reported as a feasible search
record.  The current source and independent auditor hashes are

```text
632dc89e385de81351654fc11ee25dd0ca9dc2c8f2729a0358433ff144410e85  search_joint_delete_append_sa.cpp
4b1571b661f3848abe45ed347faed9bf6c6e547cda819b90b7f2270e3fcdbd64  audit_joint_delete_append_sa.py
```

The 790 certified width-fifteen four-deletion survivors were also extended
by every possible fifth deletion.  The deterministic scan checked

```text
790 * 461 = 364,190
```

extensions.  Exactly 9,225 raw extensions have width sixteen, collapsing to
2,727 distinct five-deletion sets.  Their branch-list SHA-256 is

```text
66da2008b63968237625bd6c24cbfe50e491d23e9bd25e27b5bd8d21986b8bf3.
```

An exact fixed-prefix recency batch over those 2,727 sets is in progress.
This is a targeted construction neighborhood, not an exhaustive reduction
of the five-deletion formula: a width-sixteen five-deletion family need not
have a four-deletion subset of width at most fifteen.  More generally,
missing families are not monotone under restoring a deleted entry: deletion
compression can create new cross-gap interval ORs, and restoring the entry
can destroy those representations.  Even retaining all width-sixteen
four-deletion bases would therefore not by itself prove exhaustiveness.

## Solver status

The exploratory local Kissat run was externally terminated after about
4,825 CPU seconds.  Its log contains no terminal SAT/UNSAT line; the wrapper's
stored zero is not a solver verdict because the timing record reports signal
termination.  Until a run returns SAT with a
completed word passing both independent interval-OR verifiers, or UNSAT with
an independently checked proof, this section establishes only that the exact
finite decision problem has been encoded correctly.
