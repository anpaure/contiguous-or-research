# `k=15`: a resident all-depth-complete nine-cycle factor

## Result

The fixed-perfect-matching factor fibre now contains an independently
verified non-loop factor with all of the carrier conditions except
connectivity:

```text
physical middle vertices                 6435 / 6435
physical cycles                          9
cycle lengths                            1890, 774, 774, 774, 774,
                                         774, 555, 75, 45
minimum coordinate run                   4
residence bad runs                       0
upper q1 holes                           0
lower q2 holes                           0
geodesic upper q2 holes                  0
lower q3 positive-degree holes           0
upper holes over every rank              0
collision-floor excess Xi                9
```

Thus `validate_cycle_cover` returns

```text
carrier_pass_ignoring_connectivity = true
connectivity_pending = true
```

This is not yet a length-6438 word.  The nine cycles must be opened and
concatenated, and the resulting linear carrier must pass the exact lower
compiler.  It costs eight seams against the `k=15` scalar lower-bound slack
`3*6435 + binom(4,2) - 16383 = 2928`,
but affordability alone is not a Hall proof.

## Exact residence reduction

Fix one perfect matching `M0` of an equivariant middle/lower incidence
factor and select the second matching `P`.  On physical rank-seven states,

```text
tau = M0^(-1) P,       L_(i+1) = tau(L_i).
```

For an arc `e_i=(L_i,L_(i+1))`, put

```text
ins(e_i) = L_(i+1) \ L_i,
del(e_i) = L_i \ L_(i+1).
```

On the searched non-loop face, a lower trace `101` would force
`P(L)=M0(L)`.  Hence one-zero gaps cannot merge positive runs under the
one-step Boolean dilation from the lower trace to the middle trace.  Middle
residence at least four is therefore equivalent to

```text
ins(e_i) != del(e_(i+1)),
ins(e_i) != del(e_(i+2)).
```

These are exact all-negative clauses of width two and three.  For the PBBS
step-19 seed orientation used below the compiler generated 20,943 minimal
residence clauses.  All four tested orientations were SAT at round zero;
their solve times were below 1.6 seconds after clause generation.

The independent `k=9,d=2` regression generated 50 binary clauses.  An
unconstrained exact-double-shadow model had 18 physical bad runs and
violated two minimal clauses; the strengthened model found a single
126-cycle resident exact-double-shadow factor in 0.006 seconds.

## Geodesic shadow witnesses

For a selected lower path

```text
L_0 -> L_1 -> ... -> L_t,
T_i = L_i union L_(i+1),
```

the conjunction of its selected `P` variables is a sound witness for the
union or intersection of the consecutive `T_i`.  The SAT extension uses a
one-way existential Tseitin variable `y`:

```text
y -> x_e                  for every path edge e,
OR y_path                 for every requested target orbit.
```

This encoding is exact for minimum-length `q+1`-middle-state witnesses.  It
is sufficient but not necessary for unrestricted interval coverage, since a
target rank can also be reached after a longer path with rank-stalling
steps.  Every retained SAT point is therefore replayed against the literal
physical factor; no final coverage claim is inferred from Tseitin variables.

For the successful joint instance:

```text
base matching variables                   2,999
path auxiliaries                          1,069,003
base + residence + extension clauses      4,191,754
upper-q2 witness conjunctions             125,360
lower-q3 witness conjunctions             871,212
upper-q3 witness conjunctions             622,282
Kissat seed 801 process time              20.49 s
```

The decoded factor passed the independent O3 evaluator, the independent
Python physical factor/shadow auditor, and the full graded
`validate_cycle_cover` replay.

## Frozen evidence

Primary files:

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  u2u3l3_s801.engine.json
  u2u3l3_s801.audit.json
  u2u3l3_s801.fixture.txt
  u2u3l3_s801.kissat.out
  u2u3l3.witness.report.json
```

SHA-256:

```text
886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83  engine JSON
f2ab5b997199e788c1f18d2de2579020751020a35d8ef1394cb0b06a40494bd7  independent audit
2004ca654fdda5d36a24fe6c3c23d821b6788b0fd647392e949278a9c8af1e48  fixture
51d3480b88435c97036746455117cfee02860b0cae161b0f6c45d2da9d04bdcf  Kissat transcript
e0157b0ff14e823779191ca3848543aa063f81d552c4a629ea9b9650b48f0e43  witness report
```

Reproducible sources:

```text
scratch/k15_fixed_matching_double_shadow_sat_20260729.py
scratch/k15_fixed_matching_residence_cegar_20260729.py
scratch/k15_fixed_matching_minimal_residence_motifs_20260729.py
scratch/k15_fixed_matching_shadow_path_witnesses_20260729.py
scratch/convert_k15_dual_descent_factor_20260729.py
scratch/audit_k15_global_rainbow_factor_candidate_20260729.py
```

## Exact scope

This certificate proves existence of a resident, all-depth-complete,
equivariant nine-cycle factor in the fixed-`M0` fibre.  It does **not** prove
that the nine cycles admit shadow-safe seams, that the linearized carrier has
the required one-hole lower palette, that the lower Hall compiler is
satisfiable, or that `nu(15)=6438`.
