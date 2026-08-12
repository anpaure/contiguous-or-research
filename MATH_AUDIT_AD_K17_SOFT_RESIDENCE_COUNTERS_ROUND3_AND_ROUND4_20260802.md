# Independent audit of the K17 soft-residence counters (live direct-413 face and sequential-417 side face)

Date: 2026-08-02  
Lane: AD  
Status: **PASS for the stated fixed-bank CNF projections; no SAT/UNSAT claim beyond the explicit B=213 positive control**

## 1. Scope and hierarchy

There are two distinct constructions.

1. The **live objective** is the direct cumulative bank of 413 quotient blocker
   clauses, SHA-256
   `29773f2946d1a00fc7743176d84c9b2e4e9c4e2ea929cd5dd501e412adf66145`.
   Its independently built fixed-bound formulas use a one-way relaxation and a
   forward Sinz sequential counter at bounds 213, 200, and 180.
2. The later 417-row union with 332 accumulated upper-colouring cuts and bound
   196 is a valid, stronger **sequential-union side face**.  It is not the live
   direct-413 objective and has no integrated incumbent witness.

Neither bank is a complete residence specification.  Every score below is a
score against the named finite blocker bank, not the number of all physical
short runs and not a proof of residence.

## 2. Exact fixed-bank projection lemmas

### Lemma 2.1 (one-way relaxation is exact after projection)

Let `H(x)` be the hard prefix and let `C_1(x),...,C_n(x)` be blocker clauses.
For fresh variables `y_i`, replace each `C_i` by

```text
C_i OR y_i.
```

Conjoin any exact existential encoding of `sum_i y_i <= B`.  The resulting
formula projects onto the old variables as

```text
H(x) AND (at most B of the clauses C_i(x) are false).
```

**Proof.**  If `C_i(x)` is false, its relaxed clause forces `y_i=1`, so a
satisfying extension has at most `B` false blockers.  Conversely, if at most
`B` blockers are false, set `y_i=1` exactly for those false blockers and zero
otherwise, then extend the cardinality encoding.  This satisfies every
relaxed row.  QED.

The `y_i` are **not** reified in arbitrary satisfying models: a satisfied
`C_i` may still have `y_i=1`.  Consequently, a decoded solver model must
recompute the blocker score from its primary variables.  The number of true
`y_i` is only an upper bound on that score.

### Lemma 2.2 (forward Sinz counter)

For inputs `y_0,...,y_(n-1)` and bound `B`, the emitted variables
`s[i][j]` (`0<=i<n-1`, `0<=j<B`) satisfy forward implications saying that
`s[i][j]` is forced whenever the prefix through `i` contains at least `j+1`
true inputs.  The overflow clauses reject the `(B+1)`st true input.  Conversely,
when at most `B` inputs are true, assigning

```text
s[i][j] = 1 iff y_0,...,y_i contain at least j+1 true values
```

satisfies all counter clauses.  Thus this is an exact existential encoding of
`sum y_i <= B`.

The counter clauses do **not** force the displayed biconditional in every
satisfying assignment; the `s` variables are forward indicators.  The
`sinz_rule` string in the positive-control JSON is correct as the rule used to
construct that particular model, not as a formula-wide reification claim.

### Lemma 2.3 (bidirectional blocker reification in the 417 face)

The 417-row builder instead emits, for each blocker
`C_i = OR_j ell_(i,j)`,

```text
C_i OR y_i,
NOT y_i OR NOT ell_(i,j)       for every j.
```

These clauses give

```text
y_i = 1 iff C_i is false.
```

Indeed, a false `C_i` forces `y_i`; while `y_i` forces every literal of `C_i`
false.  Its forward totalizer is again not a bidirectional threshold
reification, but the final negative root unit is an exact existential at-most
constraint.

## 3. Live direct-413 artifacts

### 3.1 Typed bank and strict source

The direct bank has 413 distinct all-negative primary clauses and 1,287
literals, with arity histogram

```text
arity 1: 45
arity 2: 17
arity 3: 196
arity 4: 155.
```

The strict source

```text
round3.strict413.cnf
SHA-256 b30aed5dba8183cc696d6bbdab7e204a3b81b40949565a79e431dfc0bbdfb132
```

has 204,167 variables and 439,560 clauses: the unchanged 439,147-clause hard
prefix followed by exactly the same 413-clause bank.  Literal and clause order
differ between the standalone bank and the source tail.  After sorting
literals within each clause and comparing clause multisets, equality is exact;
both have 413 unique rows.  Raw line comparison is therefore invalid.

### 3.2 Clausewise reconstruction

The builder source has SHA-256
`6efedca5de60025ed02bbec52cac184f12f1095b6f3113f8ce6b70b3ad59dd00`.
For each bound it:

1. appends one fresh `y_i` to each of the final 413 source clauses;
2. allocates `(413-1)B` Sinz variables;
3. emits

```text
1 + (413-2)(2B) + (413-1)
```

counter clauses.

Independent clause-by-clause reconstruction, including the complete counter
suffix and every map row, gives:

| bound | variables | clauses | CNF SHA-256 |
|---:|---:|---:|---|
| 213 | 292,336 | 615,059 | `7045238b13722e62117a9da07b480127090be23ea12c994ceb4e254445bd92bc` |
| 200 | 286,980 | 604,373 | `c816c7c207dee04c3d2a289c9f8b9af977574fb0dacd0b599c267a3df2f66d05` |
| 180 | 278,740 | 587,933 | `522fa921fc86ae04a56200d891759b184d51818968ef3f90cdf42b7adac49a6a` |

All three relaxation maps are byte-identical, SHA-256
`e62fba0d6ea26fcad1fb3b2a08ca4e4d7a052824b1c4ffa912edbdd7f9357617`.

The explicit B=213 model, SHA-256
`272c4c00b8dc74e60e83dba1462a5017c1b0deeba6015bafb824dbac6f712452`,
independently satisfies all 615,059 clauses.  It has 1,198 selected primary
variables, exactly 213 false direct-bank blockers, and exactly 213 true
relaxation variables.  This is a genuine fixed-bank B=213 positive control.

B=200 and B=180 have only been built and audited.  No SAT or UNSAT result is
claimed here.

The packaged audit program of SHA-256 `c172056a...` checks the source/tail
transformation, counter dimensions, clause census, and new-variable range; its
large-instance line does not itself compare every counter clause.  The new
independent checker closes that gap:

```text
scratch/ad_k17_round3_soft413_audit_20260802/
  audit_round3_soft413_sequential_independent_20260802.cpp
  SHA-256 5802b2458b360bb84c6faa815653193850132df021f39ef2773aabf06b68d350

  round3.soft413.independent2.audit.out
  SHA-256 b108d01ab79142f4f125f1ec3d7d9c45d8385a2c215438314190f558323f78d8
```

Its output is

```text
PASS direct413 control_y=213 control_false=213 control_clauses=615059
 B213=292336/615059 B200=286980/604373 B180=278740/587933
```

## 4. Sequential-union 417 / hard-upper 332 / B=196 side face

The source has 204,167 variables and 439,564 clauses: the same 439,147 hard
prefix plus 417 residence rows.  The emitted formula consists of

```text
439147 unchanged hard-prefix clauses
   332 hard upper-colouring clauses
  1714 blocker-reification clauses (= 417 + 1297)
 90394 forward-totalizer clauses
     1 bound unit
------
531588 clauses.
```

It has 208,242 variables.  The 417 relaxation variables are 204168--204584;
the totalizer has 3,658 auxiliary variables.  The threshold-197 root is
variable 208022 and the final bound unit is `-208022`.

Frozen hashes:

```text
builder  8da6f591df504ee6683dde1c13ad243b26c492d8bb7dd13a084ac623e7ac47d8
CNF      55e8314d3ed81a1cd297bb96fd26206800fde9348c0653482b0e02411aba75fa
map      1ca2de0ac673ab58ebd5df93b465252f7999e1deb48a2867e492c90d6c59eb5b
audit    64cf3a83004c82a42623593fa924cde9099cb46e6d461293899f61fa76035e72
```

The independent checker reconstructed the complete formula and map:

```text
scratch/ad_k17_round4_soft_upper_audit_20260802/
  audit_round4_soft_upper_totalizer_independent_20260802.cpp
  SHA-256 4a7236d07ec52b67a2fc07720014713e937c626e0a0a415ece4884c34a9efa07

  marker58_round4_softres417_upper332_B196.independent.audit.out
  SHA-256 5696c25ee001f12a84735df967adc383b8ae5810d69a0bc795780fe6cacc4fb2
```

The clean-C14 incumbent scores 220 on this 417 bank and falsifies 158 of the
332 hard-upper rows.  Its earlier score 192 applies only to the old 385 bank.
It is not an integrated B=196 witness.

## 5. Exact limitations and operational consequences

1. The 413 and 417 objectives are finite discovered-blocker objectives.  A SAT
   candidate must be materialized and rescanned by the hardened transition-gap
   oracle; new motifs extend the CEGAR bank.
2. The live direct-413 formulas contain no 332-row higher-upper bank.  The
   417/B196 formula contains only the supplied lazy upper-colouring cuts, not a
   complete all-width certificate.
3. Connectivity/topology closure, voltage, linear opening, source chronology,
   compiler/common-cap, and literal OR-word verification remain outside both
   formulas.
4. Each direct-413 bound is a separate fixed-B rebuild, not one incremental
   assumption counter.  The 417 formula can be monotonically tightened below
   196 with stronger negative root units, but relaxing it upward requires a
   rebuild or an assumption-based version without the hard unit.
5. The generic 417 builder has an incomplete mixed-polarity tautology check,
   but all frozen typed rows are homopolar; this does not affect the artifact.
   Its incumbent-model reader is diagnostic rather than a complete-assignment
   verifier; formula correctness is independent of that diagnostic input.

Thus the exact proved boundary is: both fixed-bank cardinality encodings are
sound and projection-complete for their named clause banks; only direct-413
B=213 has a positive witness, and none of the global residence, upper,
topology, opening, or compiler gates is closed by these encodings alone.
