# Residual coordinate-lex symmetry for the exact `k=11` onion branches

## Status

`k11_forest_sat.cpp` now has the optional guard

```text
K11_FOREST_RESIDUAL_COORD_LEX=1.
```

It is accepted only when exactly one of the two exhaustive rank-filtration
branches is enabled.  It changes no mathematical solution set modulo
coordinate relabelling.

## Symmetry left after the branch split

In Type II every entry has rank at most five and no literal rank-six entry
exists.  The canonical-rank-six clauses are consequently vacuous at the
array level, and the whole hard formula is invariant under `S_11` acting on
coordinates.

In Type I the sole literal rank-six entry is fixed to

```text
A[0]={0,1,2,3,4,5}.
```

The residual stabilizer is `S_6 x S_5`: coordinates `0,...,5` may be
permuted among themselves, as may coordinates `6,...,10`.  All central
target layers are complete families, and every structural, density,
containment, onion, and subcube circuit is coordinate-equivariant.  Seed
values affect only solver phases and are not hard constraints.

For coordinate `b`, let its occurrence column be

```text
(A[0,b],A[1,b],...,A[464,b]).
```

Every orbit has a representative in which these columns are sorted
lexicographically.  The guard imposes adjacent comparisons on:

```text
Type II: 0<=1<=...<=10;
Type I:  0<=1<=...<=5 and 6<=7<=...<=10.
```

Equal columns cause no problem.  In a universal word they are in fact
excluded by singleton coverage, but the symmetry argument does not need
that fact.

## Exact comparator circuit

For adjacent columns `x,y`, an exact prefix-equality literal is carried down
the 465 positions.  At each position the clause

```text
equal_prefix -> (!x or y)
```

forbids the first unequal pair `(1,0)`.  Five clauses define the next
prefix-equality literal bidirectionally as

```text
next_equal <-> equal_prefix and (x==y).
```

Thus an auxiliary assignment cannot turn equality off early to evade the
comparison.

## Exact inventory

The guard adds:

```text
Type II: 4,641 variables and 27,851 clauses;
Type I:  4,177 variables and 25,066 clauses.
```

On the enhanced onion/subcube formulas this gives:

```text
Type II: 3,644,969 variables / 19,504,545 clauses;
Type I:  3,637,298 variables / 19,473,652 clauses.
```

Both optimized build-only paths and a separate syntax build pass.  This is a
search symmetry reduction, not evidence for SAT or UNSAT.
