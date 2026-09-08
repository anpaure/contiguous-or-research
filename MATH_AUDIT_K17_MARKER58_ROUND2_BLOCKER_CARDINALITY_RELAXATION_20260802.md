# `k=17` marker58 round-two blocker-cardinality relaxation audit

Date: 2026-08-02  
Status: generator and positive-control audit **GO**; exact `B=200` and
`B=150` solver lanes are running.  This is a relaxation of the frozen 385
residence blockers, not a resident-factor certificate.

## 1. Exact relaxation

The frozen round-two master is

```text
272d0f23bedd0b22c830c4bc08883ad9bf7883de61ce1f448e648df9752f2e93
  marker58_residence_round2.cnf
```

with `204167` variables and `439532` clauses.  Its last 385 clauses are,
after sorting literals inside each clause, exactly the cumulative round-two
blocker multiset.  The canonicalized multiset SHA is

```text
f0c134c0be74c2f5694d7c17a4365a609ced4fc7e30629a283400741e4bf972f.
```

For each tail clause `C_i`, introduce a fresh relaxation literal `y_i`,
replace it by `C_i or y_i`, and impose

```text
sum_i y_i <= B
```

with the sequential Sinz counter.  Thus SAT means only that a factor can
violate at most `B` of these 385 already-known necessary clauses.  It does
not mean that the factor is resident: the literal oracle must reconstruct
the physical factor and separate all of its current length-two and
length-three runs again.

The builder source is

```text
6efedca5de60025ed02bbec52cac184f12f1095b6f3113f8ce6b70b3ad59dd00
  scratch/relax_dimacs_tail_clauses_cardinality_20260802.cpp
```

## 2. Independent generator audit

The independent parser/auditor is

```text
c172056aa87cd3bc347ff89817dccc80879a6c44d536927da4842287032a7f86
  scratch/audit_relax_dimacs_tail_clauses_cardinality_20260802.cpp
```

It does not use the builder parser.  It checks:

1. token-level DIMACS syntax and literal ranges;
2. byte-order equality of every untouched prefix clause;
3. exact `C_i -> C_i or y_i` replay for every tail clause;
4. relaxation-map ordering and uniqueness;
5. the fresh-variable and counter-clause censuses; and
6. existential truth of the counter after fixing every possible `y` row.

The exhaustive calibration covers all `1 <= n <= 9` and all
`0 <= B <= n`: 54 formula instances and 9,216 complete `y` truth rows.
Every row is extendible in the generated counter exactly when its Hamming
weight is at most `B`.

The actual formulas replay independently as

```text
B=200: 281352 variables, 593117 clauses
B=150: 262152 variables, 554817 clauses.
```

Their hashes are

```text
46a9a8fb21aab833806f3faf15b69b423f7a888abcc92ddc07b2a5769508ac45
  round2.relax_b200.cnf
a1028cdc1c74ab47e120090645318146544768a50e0278ea0f85412cedda5bd9
  round2.relax_b150.cnf
```

## 3. Exact positive control at `B=237`

The authenticated `paired_escape005` factor falsifies exactly 237 of the
385 cumulative clauses.  The positive-control builder independently:

1. reconstructs the authenticated base-CNF counter assignment from the
   selected primary factor;
2. sets `y_i=1` exactly when the original tail clause is false; and
3. sets every new counter bit `s[i][j]` to one exactly when the prefix
   `y_0,...,y_i` has at least `j+1` true values.

The resulting complete 295,560-variable assignment satisfies all 621,459
clauses of the `B=237` formula.  The source and principal artifacts are

```text
c3eb0f9f69218a12b9ba8e4b4737ef2fe220f738eb071be587653b8c88ee2ba3
  scratch/build_audit_k17_marker58_blockercard_positive_control_20260802.cpp
61fce46d62fc47eda3a371ec91d73fe906b18e7247b15ce437f78c517ddd7df8
  paired_escape005.b237.full.model
c2db4c679cf93bb033e2f41c13aa77f98334dbcc1489dff4f5147ef5da848bb0
  paired_escape005.b237.positive_control.audit.json
```

The full frozen factor/topology/residence oracle then independently reports:

```text
quotient/physical connectivity: PASS
physical short runs:            4029
unique current blockers:         237
terminal status:                 NEED_CEGAR
```

This is the required positive control: the cardinality encoding accepts the
known 237-violation witness, while the literal oracle correctly refuses to
call it resident.

## 4. Sharpened constructive bracket

After the first launch, the independently authenticated `floor010` factor
reduced the positive-run count to 3,876 and its cumulative-385 score to
exactly 206:

```text
violated arity 1/2/3/4: 30 / 9 / 95 / 72
bf7e7e650bf6eceb3d4873f840b397d91255b669ae7260cefc277d302529d780
  floor010.cumulative385.audit.json
a5d69414208494455135dfbd90a26a1bdf0fd66fe762d6b3a976e199b5709fa2
  floor010.cumulative385.violated.tsv
```

A second deterministic positive control at `B=206` independently replays
all 597,713 clauses.  The frozen literal oracle reconstructs one physical
component, 3,876 short positive runs and 228 current unique blockers, then
correctly returns `NEED_CEGAR`.  Hence `B=200` is only six cumulative
clauses below a constructive factor, even though it remains far from literal
residence.

The subsequent authenticated `c12_escape001` factor sharpens the
constructive score again to 203.  Its deterministic `B=203` extension
replays all 595,415 clauses of a 282,504-variable formula.  The original
factor oracle and the hardened transition-label flip-gap validator agree
independently on

```text
physical components:       1
positive short runs:       3825
current unique blockers:    225
terminal status:           NEED_CEGAR.
```

An independent cyclic upper-deck replay gives rank-11/12/13 holes
`1836/408/34`; ranks 14--17 remain complete.  This trades against
`floor010`'s `1819/425/34` rather than strictly improving every deep rank.
The old `B=205` Kissat lane was therefore stopped as theorem-redundant with
exit 143.  Its partial proof is retained under an explicit supersession
status, and no solver verdict is claimed.

Two further authenticated descents sharpen this again:

```text
c14_escape001: 3774 short runs, cumulative score197, deep holes1836/374/34
floor_c14clean: 3740 short runs, cumulative score192, deep holes1836/408/34.
```

The cleaned factor's arity contribution is `30/9/86/67`.  Its deterministic
`B=192` model replays all 586,989 clauses of the 278,280-variable formula.
Both residence implementations agree on 3,740 short runs.  The current
factor produces 220 unique blockers; 192 overlap the old bank, so the exact
CEGAR union has 413 clauses.  The cleanup improves residence/cardinality but
pays 34 additional rank-12 upper holes, so raw C14 remains the stronger
deep-upper seed.

The `B=200` Kissat and CaDiCaL lanes and the briefly launched `B=196`
Kissat lane were stopped as theorem-redundant.  Every partial proof remains
retained with an explicit supersession file; none is reported as a solver
verdict.

## 5. Live exact lanes

The remaining proof-retaining CPU lanes, each capped at 1,800 seconds and
8 GiB, are running on the H100:

```text
B=150: Kissat core 42; CaDiCaL core 43
B=192: explicit deterministic SAT control from floor_c14clean
```

Every SAT output is automatically replayed against its complete relaxed
CNF and then passed through the frozen quotient-factor, physical-topology,
voltage, and residence oracle.  An UNSAT solver status is not promoted to a
theorem without checking its retained proof.  A SAT result bounds only this
385-clause relaxation; any new literal short-run blockers must be added in a
new CEGAR round.

## 6. Round-three rebase

The 220 blockers from `floor_c14clean` contribute 25 clauses not in the old
385-bank.  The independently frozen round-three formula is therefore

```text
439145 base clauses + 2 component cuts + 413 blocker clauses
= 439560 strict clauses.
```

Byte-level replay independently checks the entire base prefix, both cut
clauses and the exact 413-clause tail.  On this active bank:

```text
floor_c14clean score: 220
c16_escape001 score:  213
```

The `c16_escape001` factor has 3,672 short positive runs, exact q1/caps and
one component.  Its deterministic `B=213` model replays all 615,059 clauses;
the hardened oracle emits 216 current blockers.  Of these, 213 already lie
in the round-three bank, producing a prospective 416-clause next union.
Its deep-upper holes are `1836/408/17`, so it also halves the rank-13 debt
from 34 to 17.

The next authenticated descent, `floor3553`, is the current common
residence/cardinality seed.  Against the same round-three bank it has

```text
short positive runs: 3553 = 209 Z_17 orbits
cumulative413 score: 202
deep holes r11/r12/r13: 1836/425/17.
```

Its deterministic `B=202` extension replays all 606,017 clauses of a
287,804-variable formula.  Both residence validators emit 209 current
blockers.  Exactly 202 lie in the 413-bank, giving a 420-clause prospective
union.  Therefore the live `B=200` round-three portfolio is only two known
rows below an actual factor, although the factor still has 3,553 physical
short runs and is emphatically not resident.

The new soft formulas independently replay as

```text
B=200: 286980 variables, 604373 clauses
B=180: 278740 variables, 587933 clauses.
```

Immutable per-run launchers now drive proof-retaining Kissat and CaDiCaL
lanes at each bound.  The older 385-bank `B=150` lanes remain only a scoped
seed search and require manual postprocessing because their shared wrapper
was superseded while they were live.
