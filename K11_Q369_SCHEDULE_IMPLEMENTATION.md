# k=11 arithmetic-only `q369_schedule` branch

## Status

Implemented in `k11_forest_sat.cpp` as an opt-in exact-search branch selected by

```text
K11_FOREST_PORTAL_BRANCH=q369_schedule
```

This is a conditional branch of the unrestricted length-465 problem.  It is
not asserted to be without loss of generality, and SAT/UNSAT for this branch
alone does not settle the unrestricted problem.

## Exact semantics

The rank-six central layer has 462 selected witnesses in increasing endpoint
order.  If `state(i,alpha,beta)` denotes that ordered witness `i` uses the
zero-based physical interval

```text
[i + alpha, i + beta],
```

then `q369_schedule` adds exactly these 462 unit clauses:

```text
state(i,0,2)       for 0 <= i <= 368,
state(i,0,3)       for 369 <= i <= 461.
```

Equivalently, the first 369 ordered rank-six witnesses are the canonical
triple windows `[i,i+2]`, and the final 93 are the canonical quadruple windows
`[i,i+3]`.

The branch deliberately does **not** fix:

- any rank-six mask value or permutation;
- any array entry;
- any rank-seven portal value or location;
- mask 958 or any other upper target;
- any additional lower-row labeling.

All ordinary exact target clauses remain present.  Therefore a SAT model is a
complete 465-entry universal nonzero array, not merely a central-row object.
The schedule itself does not say that a portal must take an upper-rank value;
that behavior, if it occurs, must follow from the full formula.

## Compatibility guard

The existing portal-mode guard is reused unchanged in strength.  This branch
requires exactly the adjacent-shadow and rank-three-shadow kernel:

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
```

`K11_FOREST_CONTAINMENT_CAPS=1` is optional.  Band cuts, joint band cuts,
endpoint alignment, canonical/boundary rank-six-entry modules, singleton-pool
cuts, local-density PB, rank-six portfolio branches, and minimum-component
branches must all be absent.

No variables are allocated by `q369_schedule`.  Its 462 units are emitted at
the same proof-traced location as the pre-existing q19 portal clauses.  The
old q19 modes retain their clause order and counts.

## Remote build audit

The source was copied to the RunPod at
`root@157.157.221.29:27423:/root/q369_schedule_audit` and compiled there, not
on the Mac, with:

```text
g++ -O3 -std=c++2a -Wall -Wextra -Wpedantic \
    -I/root/cadical/src k11_forest_sat.cpp \
    /root/cadical/build/libcadical.a -lpthread \
    -o k11_forest_sat_q369
```

The compilation produced no warnings.  SHA-256 values for the audited remote
copy are:

```text
88ef71fe519f07a6e7f39446345ad4fe8ceec515939f1ee76711e54c5f152f19  k11_forest_sat.cpp
5764bd08323a1c74dc736b53fb6c97cdb5dfa32f5794ca44c213d0be2ab36d6a  k11_forest_sat_q369
```

The local source hash matched the remote source hash exactly.

## Build-only clause audit

All rows below use the same 465-entry phase seed and the exact adjacent plus
rank-three kernel.  Variable count is 2,882,282 in every row.

With containment caps enabled:

| mode | clauses | branch clauses | delta from base |
|---|---:|---:|---:|
| none | 14,459,492 | 0 | 0 |
| `q19_factor_prefix` | 14,460,196 | 704 | +704 |
| `q19_fixed_row` | 14,459,977 | 485 | +485 |
| `q369_schedule` | 14,459,954 | 462 | **+462** |

This reproduces both previously recorded q19 counts exactly.

Without containment caps:

| mode | clauses | branch clauses | delta from base |
|---|---:|---:|---:|
| none | 14,352,124 | 0 | 0 |
| `q369_schedule` | 14,352,586 | 462 | **+462** |

Thus the implementation has the intended invariant in both allowed
configurations:

```text
delta variables = 0
delta clauses   = 462
```

Only build-only formula generation was run.  No heavy SAT solve was launched.

