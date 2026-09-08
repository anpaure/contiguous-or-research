# Exact crossing-survivor rebuild and bounded suffix-19 portfolio at `k=15`

Date: 2026-07-29  
Lane: AD  
Status: exact model repair proved and solver-free regressions passed; bounded
H100-CPU portfolio recorded below

## 1. Verdict

The former crossing-aware version of

```text
scratch/solve_k15_exact_compiler_with_suffix.py
```

was positive-sound but negative-incomplete.  It created exact witnesses for
intervals crossing the prefix/suffix seam only after it had imposed the
prefix survivor equivalence.  Consequently a crossing witness could require
a prefix incidence to be zero while the old prefix-only lower clause forced
that incidence to one.  `INFEASIBLE` from that model was not a valid negative
certificate, although every decoded and exhaustively verified positive word
would still have been valid.

Source SHA

```text
f93b4066efb27afe24c09604d57650b01c054b70873e9ffecb061fe7bb1ebe10
```

repairs this exactly.  It builds the prefix selector/incidence skeleton,
creates every suffix-only and crossing witness, forms the combined blocker
sets, and imposes the survivor lower clauses once.  The exact-OR implication
of a crossing witness already supplies its negative `z+w<=1` implications,
so the repaired source does not duplicate them.  At suffix 19, only 21
existing survivor rows acquire respectively `16,758` and `20,919` new
witness literals for union34 and union41.  No variable or constraint is
needed for those added literals.

The solver-free audit

```text
scratch/audit_k15_exact_compiler_suffix_rebuild_20260729.py
```

passes locally and on H100.  It reconstructs a complete model assignment for
the known suffix-20 word, checks a crossing-only unit fixture rejected by the
old encoding, independently derives every suffix/crossing increment from the
audited frozen prefix baseline, and freezes every input and relation hash.  It
imports no solver.  The prefix baseline itself is separately decomposed into
the seven row families in Section 6.

## 2. Exact rebuilt survivor theorem

Fix the audited H19 carrier `T`, put

\[
 k=15,\qquad d=3,\qquad W=6435,\qquad L=W+d=6438,
\]

and let `P_p` be the maximal erosion envelope of `T` at prefix position
`p`.  The source has a Boolean incidence `z_(p,a)` exactly when `a in P_p`.

A prefix selector `y_(X,I)` labels a prefix interval `I` of length at most
three by lower target `X`.  A tail selector `w_(X,J)` labels either a
suffix-only interval or a crossing interval `J` that begins at one of
`L-3,L-2,L-1` and ends in the suffix.  Define, for every supported prefix
incidence,

\[
\begin{split}
B_{p,a}={}&\{y_{X,I}:p\in I,\ a\notin X\}\\
&\mathbin{\cup}
\{w_{X,J}:p\in J\cap[0,L),\ a\notin X\}.
\end{split}                                            \tag{2.1}
\]

Suffix-only witnesses contribute no prefix blockers.

### Theorem 2.1 (exact combined maximal closure)

Within the declared fixed-carrier, fixed-pool architecture, it is without
loss of generality to impose

\[
             z_{p,a}=1\quad\Longleftrightarrow\quad
             \sum_{b\in B_{p,a}}b=0.                  \tag{2.2}
\]

An exact encoding is

\[
 z_{p,a}+b\le1\quad(b\in B_{p,a}),\qquad
 z_{p,a}+\sum_{b\in B_{p,a}}b\ge1,                   \tag{2.3}
\]

with `z_(p,a)=1` when `B_(p,a)` is empty.  For crossing witnesses, the first
family in (2.3) may be omitted because it follows from the selected
witness's reified exact interval-OR equality.  The combined lower clause may
not omit those crossing witnesses, and the old prefix-only lower clause may
not remain alongside it.

#### Proof

For soundness, a selected prefix or crossing occurrence labelled `X` forces
every supported outside-`X` incidence in its prefix part to zero.  For a
prefix occurrence this is the explicit first family in (2.3).  For a
crossing occurrence, `w => OR_J=X`, together with the exact `AddMaxEquality`
recurrence for every bit, gives the same implication.  The combined lower
clause forces every incidence not deleted by a selected occurrence to one.
The positive target clauses then make every selected prefix interval exactly
its target; reified bit equalities do the same for each selected tail
interval.  The unconditional middle clauses give `D^3 A=T`, and the
nonempty clauses forbid zero letters.  Thus every feasible assignment decodes
to the claimed literal word.

For completeness, begin with any word in the declared scope and designate
one occurrence for every required target.  Turn on every supported prefix
incidence not forbidden by a designated prefix or crossing occurrence.  This
maximalized prefix contains the original prefix: an actual occurrence
labelled `X` never has an outside-`X` bit in its interval.  It remains below
the erosion envelope, so it creates no false middle bits; containing the
original prefix preserves every required middle bit and nonempty letter.
Every designated occurrence retains its positive bits and still has all
outside bits blocked.  Therefore maximalization satisfies (2.2) without
losing any literal occurrence.  This proves that the survivor closure is
exact rather than a restriction.  ∎

There is no circular proof hidden here.  Selecting `w` may delete prefix
bits used in the OR defining `w`, but the resulting interval must still pass
all 15 exact OR-bit equalities.  A selected witness is consequently a real
occurrence in the final decoded word.

## 3. Why only three crossing starts are complete

A lower target has rank at most seven.  Any interval beginning at or before
`L-4` and ending in the suffix contains the final four prefix letters.  Their
OR is the final rank-eight carrier state.  By monotonicity that interval
cannot be a lower target.  Hence the three starts

\[
                       L-3,\quad L-2,\quad L-1          \tag{3.1}
\]

are the complete crossing family, not a short-window heuristic.  For suffix
length `s`, the exact tail family has

\[
                    \frac{s(s+1)}2+3s                  \tag{3.2}
\]

intervals.  At `s=19` this is `190+57=247`; at `s=20` it is
`210+60=270`.

## 4. Solver-free seam regression

For the frozen carrier, the last erosion envelope is

\[
 P_{6437}=7779=7267\mathbin{\cup}\{9\}.
\]

Take the maximal erosion prefix, clear coordinate 9 only at position 6437,
append suffix letter `1`, and select the crossing witness

```text
w_7267_c_2_3 = 1.
```

The final prefix letter becomes 7267 and its OR with suffix letter 1 is still
7267.  All 6,435 third-derivative windows remain the carrier and every source
letter remains nonzero.  At incidence `(6437,9)` there is no selected prefix
blocker and this crossing witness is the sole blocker.  The old lower clause
forced `z_(6437,9)=1` and rejected the state.  The repaired clause

\[
                 z_{6437,9}+w_{7267,c_{2,3}}\ge1       \tag{4.1}
\]

accepts `z=0,w=1`, as exact literal semantics require.

## 5. Full suffix-20 model-assignment regression

The known word

```text
scratch/k15_joint_compiler_suffix20_union34_regression_v3.word
```

has length 6458 and SHA

```text
b34c5770146b60c74478773809c6f49d9fb24152a2c8c4c7a15eda57d2b58e6c
```

Its first 6438 letters have third derivative exactly the frozen carrier.  The
prefix misses exactly the following 21 lower masks:

```text
685 964 1359 2420 2575 2676 5237 5801 7267 7504 8729
9524 13616 13620 17683 17738 18970 19568 21641 24730 29776
```

All lie in union34.  Independently evaluating the 19,311 prefix cells yields
19,310 literal lower cells covering 16,362 distinct targets.  A deterministic
choice of one cell per target covers all 2,879 deleted erosion incidences:

* 1,683 target choices are forced by a uniquely coverable deleted incidence;
* the initial deterministic choices leave 53 incidences uncovered;
* 24 deterministic gain-minus-loss switches cover them all;
* the canonical 16,362-line selector map has SHA
  `fa7d4494d0e260585720ba3b28953066fe0130476686400efe3f8c49452f7f88`.

Thus the model's maximal closure reconstructs the known prefix itself, not
merely another prefix.  Every one of the 21 residuals has a unique suffix
interval witness.  Twenty are singleton cells; the exception is

\[
                         9524\mathbin{|}13616=13620
\]

at suffix interval `(5,6)`.  The canonical witness map has SHA
`761ddeb2e078ca7757cf0fb38ab4552cbbe8dbdfefd1c851fe7cba5f7927c978`.
There is no accidental lower crossing occurrence in this word.  Direct
enumeration of all literal intervals covers all 32,767 nonzero masks.

This is a complete solver-free feasible assignment for the repaired
union34/suffix20 model with `minimum_explicit=16362`.

## 6. Exact model sizes

The unchanged prefix skeleton has 166,054 variables and 1,034,732
constraints.  Its constraint ledger is

| family | rows |
|---|---:|
| target capacity | 16,377 |
| cell capacity | 19,311 |
| prefix negative implication | 333,307 |
| survivor closure | 32,202 |
| selected-target positive witness | 575,617 |
| middle positive witness | 51,480 |
| nonempty prefix letter | 6,438 |
| total | 1,034,732 |

The crossing repair changes literals in 21 survivor rows but does not add
rows.  Independent formulas and the actual H100 dry builds agree exactly:

| pool / suffix | variables | constraints | crossing blocker literals |
|---|---:|---:|---:|
| union34 / 19 | 178,203 | 1,180,817 | 16,758 |
| union41 / 19 | 179,932 | 1,206,752 | 20,919 |
| union34 / 20 | 179,330 | 1,192,901 | 17,640 |
| union41 / 20 | 181,220 | 1,221,251 | 22,020 |

The canonical crossing-relation hashes are respectively

```text
union34/s19  3b01dccfb8958999c16ebe556dcde170f836a165be84cbb4e6f37f4af621e359
union41/s19  b9f1a8f1a85906fb3a5ac8356cd63a0a113336f3fb2fcb6242d00bd3bde4afe9
union34/s20  84b5bc5379ad8b3ce1f54ea2178c9bd6490c72223cffc6cad8dd56a582fc4f42
union41/s20  68393ce7c404b0cb9e687db541d891392598f299652f813eec0883c590290c35
```

## 7. Objective, pool, and negative-certificate scope

The repaired source explicitly calls `ClearObjective`; it is a feasibility
model.  Every target outside the named pool is constrained to have exactly
one prefix selector.  At least 16,362 total prefix selectors are required.
Every pool target must have a prefix, suffix-only, or crossing selector.
All selector capacities and exact literal witness clauses remain enforced.

Therefore:

* Any `FEASIBLE` word that passes exhaustive verification is an
  unconditional literal length-6457 certificate.
* `INFEASIBLE` for union34 excludes only the fixed carrier SHA
  `86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b`,
  suffix length 19, union34 SHA
  `4fbddba352f1e13dee95cb50f71e0bd84caaa5ee7210c1bb771da400df5045c2`,
  outside-pool-prefix ownership, and `minimum_explicit=16362`.
* The corresponding union41 scope replaces the pool SHA by
  `6b7e2ef5309587ec288644f2075560c699940ad19b1fb1940810fe80cd1b4fe0`.
* Union34 forces 16,349 nonpool targets plus at least 13 pool targets into
  the prefix.  Union41 forces 16,342 plus at least 20.
* Union41 strictly contains union34, so `INFEASIBLE` for union41 subsumes
  union34 only under all the identical fixed-model assumptions above.
* `UNKNOWN` proves nothing.  No fixed-model result proves
  `nu(15)>6457`.

## 8. Frozen H100 deployment

All heavy work is CPU-only on host `arboghast`; no local solve and no GPU
work is permitted.  The manifest-frozen remote bundle is

```text
/home/amodo/or15/k15_suffix_cross_exact_f93b4066_20260729
```

with manifest

```text
scratch/k15_suffix_cross_exact_f93b4066_20260729.sha256
```

Every manifest entry passed `sha256sum -c` remotely.  Python is 3.12.3 and
OR-Tools is 9.15.6755.  Both suffix-19 dry builds returned the exact counts in
Section 6.  The bounded two-case runner is

```text
scratch/run_k15_suffix19_exactcross_f93b4066_h100.sh
```

It disables CUDA and BLAS/OpenMP oversubscription, pins union34 and union41
to disjoint eight-CPU sets, uses seeds 2101 and 2102, gives each CP-SAT case
3,600 seconds with a 3,900-second external bound, and writes distinct result
files.  Any returned word must pass both the solver's internal exhaustive
enumeration and an independent `graded_quotient_pipeline.py verify`; a
length-6457 word must additionally pass the carrier-aware near-optimal
verifier.

The result status and independent verification, if any, are recorded in the
final subsection after launch.  Earlier suffix-only and pre-repair crossing
jobs in the shared remote directory are not negative certificates for this
model.

### 8.1 Bounded portfolio result

The corrected portfolio launched at `2026-07-28T22:45:03Z` after the three
obsolete jobs were terminated.  At launch the outer shell was PID 3096547,
the main runner script 3096549, the two `run_case` subshells 3096552 and
3096553, the timeout/taskset wrappers 3096554 and 3096556, and the Python
solvers 3096557 and 3096558.  Both cases passed the manifest gate and emitted
the exact `MODEL_BUILT` records in Section 6 before entering search.  Final
solver statuses are pending inside the declared external time bound.

## 9. Sharp remaining boundary

The crossing witness bug is closed: inside the stated fixed-carrier/pool
scope, both positive and negative statuses now have exact literal semantics.
What remains open is feasibility itself for suffix 19 and, beyond this fixed
architecture, whether another carrier, a residual outside the chosen pools,
or a prefix with fewer than 16,362 explicitly assigned lower targets yields
a length-6457 word.  No conclusion about the global optimum follows from a
bounded `UNKNOWN` run.
