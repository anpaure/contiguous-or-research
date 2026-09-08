# Audit of the compact pair-shadow encoding

The independent checker

```text
scratch/verify_k11_compact_pair.cpp
```

reconstructs the complete `J(11,6)` graph, enumerates all 200,970 unordered
pairs of incident real edges, and checks directly that:

* every rank-four triple intersection uses different removal groups;
* every rank-eight triple union uses different addition groups;
* every rank-four target has exactly 525 explicit pair witnesses;
* every rank-eight target has exactly 1008 explicit pair witnesses; and
* target `958` has exactly 1008 witnesses.

It independently recomputes both CNF sizes and exits zero only if all counts
match.  Its retained output is

```text
vertices=462 Johnson_edges=6930
rank4_targets=330 centers_each=21 groups=5x5 witnesses_each=525
rank8_targets=165 centers_each=28 groups=6x6 witnesses_each=1008
target958 witnesses=1008
old_pair_variables=200970 old_pair_clauses=603405
compact_centers=11550 compact_variables=34650 compact_clauses=182985
saved_variables=166320 saved_clauses=420420
PASS
```

A no-op-solver initialization independently reports:

```text
target 958 only: 28 centers, 84 variables, 336 group-edge occurrences
all rank4/rank8: 11550 centers, 34650 variables, 124740 occurrences
```

The modified main source passes C++20 syntax checking.  No SAT solve was run
locally.
