# Exact fixed-D / residual-Hall Benders loop for the compact K17 projection

Date: 2026-08-01  
Lane: AD  
Status: proved algorithmic reduction; no claim that any pending solve is SAT or UNSAT

## 1. Frozen scope

Let `B` denote the frozen compact-base CNF before the implication-only
rank-10 provider variables.  It has

```text
510712 variables / 3032974 clauses.
```

It contains the fixed-MASS age skeleton, the `D` and `H` incidence perfect
matchings, the age-consumption bridge, same-owner exclusions, and direct
rank-7 coverage.  It does **not** contain topology/voltage, residence, lower
depths 2--6, upper ranks 11--16 or trim-3 opening, common-cap compilation,
or a literal OR word.

Fix a literal `D` perfect matching `D0`.  The authenticated static inner
master `M_D0` has one local variable for each of the 11,438 admissible
`H` incidences, its facet and owner exact-one rows, and all 1,144 rank-10
colour ALOs.  The frozen canonical instance has

```text
11438 variables / 84056 clauses.
```

Thus every satisfying assignment of `M_D0` is exactly a q1-complete
incidence perfect matching `H0`; no age feasibility is asserted yet.

## 2. Exact fixed-`(D,H)` age face

For a static-master solution `H0`, define

\[
 A(D_0,H_0)=B\wedge\bigwedge_{d\in D_0}d
                 \wedge\bigwedge_{h\in H_0}h.
\]

### Theorem 2.1

`A(D0,H0)` is satisfiable if and only if the fixed q1-complete pair
`(D0,H0)` has an age/direct-rank7 extension in the compact pre-topology
skeleton.  It has exactly

```text
510712 variables / (3032974 + 1430 + 1430) = 3035834 clauses.
```

### Proof

The positive `D0` and `H0` units, together with the exact-one rows already
in `B`, fix both complete incidence matchings.  Every remaining variable and
clause is precisely an age, age-consumption, same-owner, or direct-rank7
condition of `B`.  Conversely, any such extension satisfies `B` and the
2,860 units.  The q1 condition needs no further clause because it was
authenticated when `H0` was obtained from `M_D0`.  The clause count is
immediate.  ∎

A SAT result is accepted only after complete DIMACS replay, provider lifting,
replay of the 613,656-variable compact formula, and the independent compact
semantic postprocessor.  An UNKNOWN result has no mathematical consequence.

## 3. Conditional H-core cuts

Write `B_D0 = B and all positive D0 units`.  Suppose `C` is a subset of the
1,430 selected incidences of `H0` and

\[
 B_{D_0}\wedge\bigwedge_{h\in C}h
\]

is proof-verified UNSAT.

### Theorem 3.1 (local cut)

Inside the static master with `D=D0` fixed, the clause

\[
                 \bigvee_{h\in C}\neg h                         \tag{3.1}
\]

is valid.  It excludes every q1 matching containing all edges of `C`, not
only the incumbent `H0`.

### Proof

Any static assignment falsifying (3.1) selects every member of `C`.
An age extension of that assignment would satisfy `B_D0` and all units in
`C`, contradicting the verified UNSAT certificate.  ∎

For an unrestricted joint `(D,H)` master the corresponding valid clause is

\[
 \bigvee_{d\in D_D}\neg d\ \vee\
 \bigvee_{h\in C}\neg h,                                      \tag{3.2}
\]

where `D_D` is any certified subset of `D0` for which
`B and D_D and C` is UNSAT.  Using all 1,430 edges of `D0` is always sound.
The H-only clause (3.1) is **not** globally valid after changing `D`.

An outer master containing only `D` variables cannot use (3.1) or (3.2).
It may exclude `D0` only after the complete cut-augmented static master
`M_D0` is itself proof-verified UNSAT, in which case

\[
                   \bigvee_{d\in D_0}\neg d                    \tag{3.3}
\]

is valid.

## 4. Fail-closed extraction from a DRAT input core

The direct age-face generator appends the `D0` units and then the `H0`
units to `B`.  A raw `drat-trim -c` output is a useful candidate clause core,
but it is not by itself the published proof of a conditional cut.  Use the
following exact procedure.

1. Independently DRAT/LRAT-verify UNSAT of the full 3,035,834-clause face.
2. Ask `drat-trim` for an input core `K`.
3. Parse `B`, `D0`, `H0`, the full face, and `K` as DIMACS clause
   **multisets**, canonicalizing literal order but preserving multiplicity.
4. Check `K` is a clause-multisubset of the full face.
5. Subtract the multiset of `B_D0` from `K`.  Every positive remainder must
   be a one-literal clause `(h)` with `h` one of the authenticated selected
   original-H variables of `H0`, and its remainder multiplicity must be one.
   Any other remainder makes extraction fail closed.  Let `C0` be these H
   variables.
6. Rebuild from frozen inputs the direct reduced formula

   \[
        R(C_0)=B_{D_0}\wedge\bigwedge_{h\in C_0}h.
   \]

   Solve it proof-producing and independently verify its proof.  Only this
   re-verification promotes `C0` to a sound cut.  If `C0` is empty, the
   verified result is instead a `D0` no-go and gives (3.3).

The multiset subtraction handles the otherwise ambiguous case that `B`
already contains a syntactically identical unit.  Equivalently, future
faces may use fresh selector variables `a_h` and clauses
`(-a_h or h), (a_h)` to make assumption identity explicit.  Such selector
models must be projected back to variables 1 through 510,712 before the
existing provider lifter, which deliberately rejects out-of-range literals.

The current projector

```text
scratch/extract_ad_k17_fixed_DH_assumption_core_cut_20260801.cpp
SHA c5549cc794454ab3571c24915eab97211a34ec81686a341f1b4baec01f99effb
```

implements a stronger fast acceptance condition: it authenticates the face
as a literal base prefix followed by exactly the selected `D/H` units,
performs the clause-multiset subtraction, and accepts only when ordinary
unit propagation already derives contradiction on the input core.  On that
explicit `UP_UNSAT` status, no further proof of the reduced core is needed:
the core itself is an independently checked unsatisfiable clause subset of
the reduced formula.  A legitimate DRAT input core need not be UP-UNSAT,
however.  Failure of this fast check is only extraction `UNKNOWN`, never
evidence that no shorter conditional cut exists; use a proof-producing
re-solve of the reduced formula or the full 1,430-edge incumbent cut.

### Core shrinking

Starting from a verified `C0`, test `R(C-{h})` for each `h` in a fixed order.
Delete `h` only after a new independently verified UNSAT proof.  Retain `h`
after a fully replayed SAT result or an UNKNOWN result.  Iterate until no
certified deletion occurs.  If every single-deletion test terminated
decisively, the result is inclusion-minimal.  It is not necessarily a
minimum-cardinality core; neither `drat-trim` nor a deletion pass proves
that stronger optimization claim.  The implementation should therefore
call it `verified_shrunk_H_core`, not `minimum_H_core`.

Chunk deletion before the final singleton pass is sound under the same
rule and can reduce the number of solver calls.

### Frozen canonical calibration

For the first canonical static solution, DRAT-trim returned the following
independently UP-UNSAT 11-clause input core:

```text
133450 -2681 0
133451 -133450 0
-133451 -2683 0
160 -98731 0
64578 -160 -98740 0
2683 -64578 -99733 0
2681 -99742 0
98731 0
99733 0
98740 0
99742 0
```

The four unmatched face assumptions are `D_30,D_531,H_34,H_535`;
therefore the fixed-`D_0` cut is the binary row

```text
not H_34 or not H_535
```

(`-74 -1298` in static-local coordinates), while the unrestricted guarded
row has all four negative literals.  The next three replayed static models
again yielded 11-clause UP cores with exactly two `D` and two `H`
assumptions.  This is evidence about the frozen canonical face, not a theorem
that every future core is binary; the loop retains the full-core fallback.

## 5. Exact loop

```text
input: frozen B, canonical or outer-master D0, fixed-D static master M
cuts := empty

loop:
    S := M plus cuts
    solve S proof-producing

    if UNKNOWN:
        return UNKNOWN_FIXED_D0_BENDERS

    if verified UNSAT:
        publish OR_{d in D0} not d        // D-only outer cut
        return VERIFIED_D0_NO_EXTENSION

    replay the complete SAT assignment of S
    decode and recheck H0 as a 1430-edge facet/owner perfect matching
    recheck all 1144 fixed-D q1 colours

    build A(D0,H0) from frozen B/maps; hash and replay its construction
    solve A(D0,H0) proof-producing

    if UNKNOWN:
        archive runtime UNKNOWN; add no cut; optionally try a different
        static-master H by the full 1430-edge incumbent no-good, labelled
        heuristic diversification only

    if SAT:
        replay A(D0,H0)
        provider-lift to the compact model and replay compact CNF/semantics
        run topology and later CEGAR stages
        return VERIFIED_PRETOPOLOGY_INCUMBENT (or its exact later status)

    if verified UNSAT:
        obtain candidate core C by Section 4
        re-prove B_D0 plus C UNSAT
        optionally deletion-shrink with separately verified proofs
        append OR_{h in C} not h to M
```

This loop is finite for fixed `D0`: absent a shorter core, the full
1,430-edge incumbent clause removes at least the current `H0`, and the static
master has finitely many perfect matchings.  This is a completeness theorem,
not a practical iteration bound.

## 6. Residual-Hall integration

The coloured representative/residual-Hall formulation can replace or
strengthen the static CNF.  For representative indicators `p_e`, a failed
residual perfect matching returns by alternating reachability a facet shore
`S` and the exact row

\[
 \sum_{e:f(e)\in S}p_e-\sum_{e:o(e)\in N(S)}p_e
       \ge |S|-|N(S)|.                                         \tag{6.1}
\]

This row is coefficient-one and exact for the fixed `D0` static graph.
It addresses q1 representative/residual matching failure before the age
subproblem.  It does not replace an age-face H-core cut: age availability is
not determined by the static residual graph.  Conversely, an H-core cut
does not certify a residual Hall shore.  The two families are complementary.

## 7. Required artifact ledger per iteration

Every accepted iteration freezes hashes for:

- frozen base CNF/map and fixed-D layer map;
- static master CNF/map plus every accumulated cut, with an iteration
  manifest fixing clause order and local-to-original H translation;
- solver binary, stdout/status/resource log, and complete SAT model or full
  UNSAT proof;
- fixed-DH face CNF and units map;
- full-face DRAT/LRAT verification;
- candidate input core, multiset audit, reduced-core CNF, and its independent
  proof verification;
- for SAT, provider lift, compact replay, semantic replay, and topology
  postprocessing.

Partial proofs, timeouts, missing `s` lines, malformed/incomplete models,
hash drift, ambiguous unit translation, or failed replay are all `UNKNOWN`
and produce no mathematical cut.

The independently source-audited proof-producing runner implementing this
loop is

```text
scratch/run_ad_k17_canonical_D0_core_benders_loop_20260801.sh
SHA 86ec6aad8bb7619a8e96d296fea4e097d1fc0024f035f07023ae351b264563fd
```

Expected Kissat return codes 10 and 20 are captured inside explicit shell
conditionals; every genuinely unexpected command failure is trapped as
`UNKNOWN_PIPELINE_ERROR`.  This control-flow detail is part of the
fail-closed contract, because Bash's `ERR` trap fires even around a command
executed after `set +e` unless the command itself is conditional.
