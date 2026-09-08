# Production encoding of the rank-seven truncated-width moment

## Status

`k11_forest_sat.cpp` now contains an opt-in exact consequence under

```text
K11_FOREST_RANK7_TRUNCATED_WIDTH=1
```

No remote process was launched or modified during this implementation.

## Mathematical row

The corrected three-layer theorem proves the four-truncated moment

```text
T7=sum min(width_7,4)>=930  in Type II,
T7=sum min(width_7,4)>=940  in Type I.
```

For every one of the 330 rank-seven targets, the adjacent-shadow module has
an `active` crossed witness with existing unary endpoint vectors `L` and `R`.
If the target is inactive, one of the generic exception slots supplies its
actual witness.  Projecting that unknown witness to its maximum truncated
credit four gives a necessary condition.

The production plan allocates virtual credit literals for thresholds
`2,3,4`.  Inactive targets force all three credits.  For active targets, a
positive credit is guardedly tied to the actual crossed interval width.  The
unavoidable width-one unit is constant.  Thus an exact count of false credit
literals obeys

```text
deficits<=390  in Type II,
deficits<=380  in Type I.
```

## Prerequisites

The guard requires:

```text
K11_FOREST_ADJACENT_SHADOWS=1
```

and exactly one of

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_RANK_FILTRATION_TYPE2=1.
```

Their existing validation transitively supplies the band, joint-band, and
local-density modules needed by the theorem.  Type I also supplies rank-six
branch one and its boundary-profile row.  Containment caps are deliberately
not a prerequisite because the moment is truncated at four.

## Encoding

For target `S`, threshold `t`, and possible exact left endpoint `p`, the plan
uses

```text
active(S) OR credit(S,t),

!credit(S,t) OR !active(S) OR !L_S(p)
    OR L_S(p-1) OR R_S(p+t).
```

The unavailable boundary literals are omitted.  Since `L` has exactly one
false-to-true transition, the second clause enforces width at least `t` at
the actual left endpoint and is inert elsewhere.  Its explicit `!active`
guard leaves every inactive shadow interval semantically free.

The 990 signed deficit literals are compressed by the same exact 14-clause,
two-variable full-adder pattern used by the audited production counters.  A
direct first-difference comparison enforces the branch constant.

## Exact module inventory

```text
credit variables                                      990
counter variables                                    1964
total variables                                      2954

left-transition clauses                 330*3*465 = 460350
inactive-credit clauses                  330*3     =    990
counter clauses                                      13748
comparator clauses                         Type II =      6
                                           Type I  =      4

total clauses                              Type II = 475094
                                           Type I  = 475092
```

The solver prints every subtotal in its build inventory.

## Local regression evidence

Syntax-only compilation against the build-only CaDiCaL stub passed.

The guard-absent and explicit-`0` minimal Type-II builds are identical:

```text
variables=3224194 clauses=14912057
CLAUSE_STREAM_FNV64=fbd5f82691918512 ADD_CALLS=62109310
```

The corresponding guard-on module inventories are exactly:

```text
minimal Type II: variables=3227148 clauses=15387151
minimal Type I:  variables=3219916 clauses=15573683
```

With all currently deployed structural guards, including the Type-II pin
localization or Type-I prefix chain, the build-only totals are:

```text
Type II: variables=3660029 clauses=20076856
         CLAUSE_STREAM_FNV64=e6e5210a4f79076e ADD_CALLS=88666811

Type I:  variables=3640493 clauses=19989126
         CLAUSE_STREAM_FNV64=6c486c759a46835c ADD_CALLS=88275995
```

These are build-only fingerprints, not SAT or UNSAT results.

The independent checker

```text
scratch/check_k11_rank7_truncated_width_encoding.cpp
```

exhausts every physical interval and threshold, verifies the active/inactive
clause semantics, checks both direct comparators for all counts `0..990`,
reproduces the exact inventory, and freezes the critical source anchors.  Its
output is

```text
PASS: rank-seven truncated-width encoding
Type II: 2954 variables, 475094 clauses
Type I:  2954 variables, 475092 clauses
```

