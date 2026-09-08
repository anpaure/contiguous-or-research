# The best saved regenerative `K15` parent has exact occurrence debt `150`

Date: 2026-07-31  
Status: exact finite census, checked occurrence bound, and literal `K17`
parent-induced lift; no `K17` word or all-parent lower bound is claimed

## 0. Result

An independent scan of the current repository reconstructs `40` distinct
literal `K15` lower-rainbow factors.  Eight pass all four parent gates:

1. every owner-coordinate run has length at least four;
2. every rank-six colour occurs;
3. every rank-five lower colour occurs; and
4. every upper target occurs as a cyclic owner interval.

The previously used `6390+45` parent has `165` rank-seven `0-111-0`
patterns whose four supporting rank-six colours are all unique.  The exact
minimum over all one-occurrence-per-rank-six-colour transversals is not
`165` but `180`.

Two already saved octahedral parents are strictly better:

```text
scratch/k15_octahedral_translation_descent_r1.factor.json
scratch/k15_octahedral_translation_descent_r2.factor.json
```

They are resident and all-depth complete, have the exact occurrence profile

\[
                 1^{3630}2^{1320}3^{55},
\]

and have only `135` unique-colour forced patterns.  A checked cardinality
CNF proves that at most `149` surviving patterns is impossible, while a
literal occurrence transversal with exactly `150` survives.  Hence

\[
 \boxed{\min_{\text{saved regenerative parents}}
        \min_{\text{occurrence transversals}}
        \#(\text{internal }0\,111\,0)=150.}
\]

This is a finite-corpus theorem, not a universal lower bound over all
possible factors.

The exact circular edge-stabbing number of the forced four-edge packets
drops from `120` on the old parent to `105` on both `r1` and `r2`.  Thus a
nonflat lift needs at least `105` parent-edge actuators on these factors,
before any other constraint is imposed.

## 1. What was censused

The audit accepts a factor only after literal replay:

* all `6435` owners are distinct rank-eight sets;
* every cyclic edge is Johnson;
* the `6435` edge intersections are the complete rank-seven deck, once each.

It discovers both stable quotient-choice artifacts and literal component
arrays under `middle_components`, `cycles`, or `physical_cycles`, then
deduplicates by the complete undirected physical edge set.  The exact
summary for the eight regenerative factors is:

| factor | components | `0-111-0` | unique-forced | stabbing | coherent-upper floor |
|---|---:|---:|---:|---:|---:|
| old optimal parent | `6390,45` | 1425 | 165 | 120 | 505 |
| old four-cycle | `5715,600,75,45` | 1410 | 165 | 120 | 475 |
| iterative octahedral | `1990^3,115^3,75,45` | 1305 | 150 | 105 | 320 |
| **octahedral r1** | `2355,2355,1680,45` | 1365 | **135** | **105** | **405** |
| old nine-cycle | `1890,774^5,555,75,45` | 1395 | 165 | 120 | 368 |
| old three-cycle | `5790,600,45` | 1425 | 165 | 120 | 475 |
| octahedral r3 | `5475,840,75,45` | 1335 | 150 | 105 | 490 |
| **octahedral r2** | `2355,1680,1440,840,75,45` | 1350 | **135** | **105** | **405** |

The **coherent-upper floor** is computed as follows.  For every rank-six
colour group `Z`, let `u_Z` be the number of its physical occurrences whose
parent upper union has globally unique multiplicity.  Retaining one
occurrence of `Z` destroys at least

\[
                    \sum_Z (u_Z-1)^+
\]

unique upper witnesses.  This gives `505` for the old parent and `405` for
both best octahedral parents.  It is a lower bound on fixed-macro upper debt,
not a complete upper-provider theorem.

## 2. Exact occurrence-transversal minimum

For every repeated rank-six colour, introduce exactly-one variables for its
physical occurrences.  A `0-111-0` pattern survives iff all of its four
supporting occurrences are chosen.  Unique-colour supports give the fixed
offset `135`; each other pattern gets one violation variable equivalent to
the conjunction of its selected occurrence variables.

For `r1`:

```text
extra <= 14:  UNSAT, DRAT checked
extra <= 15:  SAT, independently replayed
total:        135 + 15 = 150
```

The `r2` `extra <= 14` formula is independently DRAT checked as well.  Every
other regenerative factor in the census already has at least `150` unique-
colour forced patterns.  These facts prove the displayed corpus minimum.

The exact `r1` witness selects all `5005` rank-six colours and has `150`
surviving patterns.  It is not merely a solver assignment: the verifier
reconstructs every occurrence choice and every surviving physical pattern.

## 3. Exact actuator number

Every unique-colour forced pattern is a proper four-edge circular interval
on one parent component.  An optimum point transversal must hit one of the
four points of an arbitrary first interval.  After choosing that point, the
remaining intervals avoid the cut and become ordinary line intervals, for
which greedy choice of right endpoints is exact.  Trying the four first
points gives the exact circular optimum.

The component totals are:

```text
old parent:       120 + 0 = 120
r1:               45 + 45 + 15 + 0 = 105
r2:               45 + 15 + 30 + 15 + 0 + 0 = 105
```

## 4. The zero-forced factor is not regenerative

The census contains one exact lower-rainbow factor with **zero** unique-
colour `0-111-0` patterns:

```text
scratch/k15_degreefactor_upper1_global_hint.json
```

This proves there is no positive lower bound from lower-q1 exactness alone.
It does not solve the parent problem.  Its owner chronology has

```text
930 runs of length 2,
735 runs of length 3,
```

and its rank-seven shore has `30` unique-colour forced `0-11-0` patterns.
Moreover it misses `1065` rank-six colours and `498` rank-five colours.
Thus the apparent zero at length three simply moves the obstruction to
length two and destroys the complete occurrence deck.

## 5. Full `r1` parent-induced `K17` test

The minimum-150 occurrence witness was fed through the exact existing
`A/X/Y + U` macro construction.  Its deleted-edge profile is

```text
581, 576, 263, 10,
```

so all four parent components open into `1430` macros.  The residual port
demands are

```text
macro degree: 0^3780 1^2450 2^205,
demand:       2^3780 1^2450 0^205.
```

The exact bipartite `b`-flow is feasible.  Deterministic flow seed `80` is
connected, and expansion gives a literal Hamilton cycle on every one of the
`24310` rank-nine `K17` owners with every rank-eight intersection exactly
once.

Its downstream defect census is:

| gate | old first-parent child | new `r1` child |
|---|---:|---:|
| upper-q1 holes | 1891 | **1883** |
| lower-q2 holes | 1623 | 1677 |
| lower-q3 holes | 1013 initially / 809 after hex descent | **926** |
| all short positive runs | 2892 | **1850** |
| immutable internal macro runs | 605 first-occurrence; 180 best possible | **150** |

The full upper-hole profile of the `r1` child is

```text
rank 10: 1883
rank 11:  876
rank 12:  172
rank 13:    2
rank 14+:   0.
```

Thus the better parent genuinely improves the full child residence pipeline;
the improvement is not an artifact of the parent score.  It does not finish
the flat construction: the `150` immutable internal macro runs survive every
port flow, macro permutation, and macro reversal.  The lower-q2 deck also
regresses slightly and must be optimized jointly with the upper flow.

## 6. Small-switch scope

The complete saved `r2` recensus contains `360` generic octahedral `C6`
atoms that individually preserve all upper/lower shadows and owner
residence.  Literal replay gives

```text
forced count 135: 270 atoms
forced count 136:  75 atoms
forced count 137:  15 atoms.
```

Therefore no single atom in that complete safe library reduces the forced
debt below `135`.  This does not exclude a compound switch, a temporarily
unsafe route, an asymmetric packet, or a larger circuit.  It says the
remaining debt is not one ordinary local octahedral repair away.

## 7. Frozen evidence

Main census:

```text
scratch/audit_k15_regenerative_parent_census_20260731.py
scratch/k15_regenerative_parent_census_20260731.audit.json
```

Exact occurrence bound:

```text
scratch/build_k15_occurrence_transversal_min_cnf_20260731.py
scratch/k15_r1_occurrence_extra14_20260731.{cnf,drat,kissat.out,dratcheck.out,map.json}
scratch/k15_r2_occurrence_extra14_20260731.{cnf,drat,kissat.out,dratcheck.out,map.json}
scratch/k15_r1_occurrence_extra15_20260731.{cnf,kissat.out,map.json}
scratch/k15_r1_occurrence_min150_20260731.witness.json
```

Literal child lift:

```text
scratch/audit_k17_r1_parent_induced_macro_port_cycle_20260731.py
scratch/k17_r1_parent_induced_macro_port_cycle_20260731.{cycle,flow.json,audit.json}
```

Complete one-switch replay:

```text
scratch/audit_k15_r2_safe_c6_forced_floor_20260731.py
scratch/k15_r2_safe_c6_forced_floor_20260731.audit.json
```

## 8. Exact remaining theorem

For this parent-induced route, the unresolved statement is now:

> Construct a complete resident/all-depth `K15` lower-rainbow factor and an
> occurrence transversal with zero internal short patterns, or supply a
> nonflat `K17` compiler whose actuator set hits the `105` forced packet
> intervals while retaining the lower and upper palettes.

The finite evidence shows that changing the parent is effective, and that
lower-rainbow exactness alone permits zero forced length-three debt.  It does
not yet prove that the four simultaneous regenerative conditions permit zero.
