# Complete `WIDTH45` safe-cycle floor `105`

Date: 2026-07-30  
Status: exact source-relative theorem; not a global lower bound for arbitrary
`K=16` carriers.

## Theorem

Fix the frozen `K=16` source carrier, the complete direction-coherent seam
catalogue, isolated `WIDTH45` target services, and cyclic global `Sep5`
condition used by the preceding `C=103` and `C=104` audits.  Every balanced
capacity-one full-service circulation in this catalogue uses at least

\[
                              105
\]

seams.

Thus the previously proved source-relative floor `104` is strict.

## Complete `C=104` cycle atlas

The authenticated `C=104` graph has `209,966` directed arcs.  Complete native
enumeration of every simple cyclic `Sep5` cycle having individual residual
cost at most eight gives exactly `29,284` cycle columns.  The enumeration
finished without a cutoff.

```text
graph SHA-256
c4fedc7fc166e3f1cfe9e9e15838faa0d9ec08f374fb779741cc1d9e82445e51

complete JSON pool SHA-256
02e9177a07a5d468c593a1b9253832ffb33ef6de280d6fc734bb9deb1bda221c

native audit atlas SHA-256
914d8a4819e82abdd69f3285f5db769ef166315feb12f593f6148568126e7bad
```

The generator is
`scratch/r_k16_width45_c104_residual8_cycle_pricer_20260730.cpp`; the
independent native exporter is
`scratch/export_r_k16_width45_c104_anneal_atlas_20260730.py`.

## Monotone residual

For a selected collection of cycle columns put

\[
 \rho=4L-w(U),
\]

where `L` is its total seam count, `U` is the set of distinct service targets
covered so far, and `w(U)` is their total dual weight.  The per-column identity
is

\[
 4L=\operatorname{service}+\operatorname{slack}.
\]

Consequently `rho` is the sum of service repetition and slack.  It is
nonnegative and monotone under adding a disjoint cycle column.  A full
`C=104` solution covers targets of total weight `408`, so

\[
                    \rho=4\cdot104-408=8.
\]

Therefore every prefix of such a solution must have `rho<=8`.  Conversely,
every individual cycle of a `C=104` solution has residual at most eight, so it
appears in the complete atlas above.

## Exact Algorithm-X exhaustion

The independent checker

```text
scratch/audit_r_k16_width45_c104_complete_algorithm_x_20260730.py
SHA-256 b86a712eac6286b476b5fcbec2eec41bd89a9fdc561cd52c2e7050bf166a4342
```

parses only the authenticated graph and native atlas.  At every node it
chooses the uncovered target with the fewest currently compatible provider
cycles, then branches over all of them.  Compatibility checks:

1. disjoint global-`Sep5` footprints;
2. total length at most `104`;
3. total slack at most eight; and
4. the monotone residual `rho<=8`.

Every nonredundant cycle of a solution covers some first uncovered target and
is therefore reached by this branching.  Once all targets are covered, a
remaining redundant cycle would increase `rho` by four times its length.  As
cycles have length at least two, the only possible completion is one
length-two filler from residual zero; the checker tests it explicitly.

The full tree has only `1,377` nodes.  Every leaf is blocked and no solution
exists:

```text
status                 PASS_UNSAT_EXHAUSTED
nodes                  1377
elapsed_seconds        1.0877139568328857
audit SHA-256          f35ecf50559536653b15847096dd579fdf796941b3669c0c0d235091f618ce51
payload SHA-256        49b0db980e99b82e9538ac7140284ce24278ef2b3b60e28ec2822d812be4b020
```

The terminal blocker histogram is

```text
target 0: 1280
target 1:   80
target 2:    2
target 5:    6
target 8:    3
target12:    2
target13:    1
```

An independently implemented CP-SAT cycle master also returned `INFEASIBLE`
for one complete-pool seed, and each exact repeat-ledger branch returned
`INFEASIBLE`; these are corroboration rather than the proof above.

## Scope

This proves only the floor inside the frozen source-relative
`WIDTH45`/global-`Sep5` catalogue.  It does not exclude:

* a different `K=16` carrier;
* services outside `WIDTH45`;
* seams outside the complete direction-coherent catalogue; or
* a repair not representable as a balanced capacity-one circulation here.

