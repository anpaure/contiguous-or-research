# Audit of the forced-prefix upper flag moments

## Mathematical audit

For a fixed rank-seven `U`, its seven rank-six subsets induce exactly `K_7`
inside `J(11,6)`.  Summing their seven degree-two equations counts an internal
selected edge twice, a real cut edge once, and a dummy endpoint edge once.
Therefore

```text
2*internal + crossing + endpoints = 14
```

is exact.  No connectivity, factorability, shadow, or endpoint-containment
assumption enters the proof.

The full-graph support count was independently recomputed:

* `C(7,2)=21` internal edges, hence 42 repeated occurrences;
* `7*24=168` external cut edges; and
* seven dummy edges.

This totals 217 input occurrences, matching the source initialization log.

## Certificate-path check

The independent checker `scratch/verify_k11_third_orbits.cpp` reverses the
score-549 path to its canonical endpoint and tests every distinct upper colour
among its first four transitions.  It prints

```text
upper_moment upper=127 internal=2 crossing=9 endpoints=1 weighted=14
upper_moment upper=631 internal=2 crossing=10 endpoints=0 weighted=14
upper_moment upper=1651 internal=1 crossing=12 endpoints=0 weighted=14
upper_moment upper=1891 internal=1 crossing=12 endpoints=0 weighted=14
```

and exits zero.  These cases exercise both repeated and singleton prefix upper
colours, and both nonzero and zero endpoint incidence.

## Encoding audit

An internal edge literal is inserted twice into the exact cardinality input.
The already audited counter represents the threshold function for every
assignment of its input positions.  Substituting one Boolean variable for two
positions preserves that equivalence on the diagonal subspace and makes the
integer sum contain coefficient two.  Thus duplicate occurrences are sound.

A no-op solver initialization with the longest tested prefix reported three
unique upper colours, each with 217 occurrences, and completed C++20 formula
construction without error.  No SAT search was run locally.
