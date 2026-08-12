# Independent audit of the Type-II reverse pin-load production circuit

## 1. Verdict

**PASS**, for the frozen production source

```text
3500113db42662e783cb8a4e9d3e247372cad1488f346b8f90b9eb36b55d3e38
  k11_forest_sat.cpp
```

I found no theorem-to-CNF, arithmetic, guard, reuse, inventory, construction,
emission, or diagnostic defect in `K11_FOREST_TYPE2_REVERSE_PIN_LOAD`.

This is an independent source and build audit.  It is not a SAT result, an
UNSAT result, or a change to the current bound on `nu(11)`.

## 2. Independent check of the mathematical projection

In the exact Type-II two-component branch, deleting the distinct literal
rank-five entries leaves two low components whose rank-five witness slacks
sum to three.  The encoded adjacent-pair condition selects the slack-one
component `C1`; the other component `C2` consequently has slack two.

Fix a coordinate `b` absent from `OR(C1)` and put

```text
o_b = #{p in C2 : b in A[p]}.
```

There are 176 rank-at-most-four targets containing `b`.  Their witnesses
cannot meet a literal rank-five separator and cannot lie in `C1`; hence they
lie in `C2`.  The segment slack is two, so each such witness is a singleton
or adjacent pair.  All 176 cells meet one of the `o_b` marked positions.

There are also 210 rank-five targets containing `b`.  At most `z_b` of them
are literal and at most `y2` of the remaining selected witnesses are triples.
Every other selected witness is an adjacent pair in `C2`, again meeting a
marked position.  Since a path with `o` marked vertices has at most `3o`
touched singleton/pair cells,

```text
3 o_b >= 176,
3 o_b + z + y2 >= 386.
```

Thus the two implemented rows

```text
o_b >= 59,
3 o_b + z + y2 >= 386
```

are valid without the optional named-cell module.

The repaired rank-five boundaries give the following profiles:

```text
A: y0=462+h1-h6,          y2=h3+h5-h2-h4,
B: y0=462+h1+h5-h4-h6,   y2=h3-h2,
C: y0=462+h1+h3-h2-h6,   y2=h5-h4.
```

All three satisfy

```text
y0+y2 = 462+h1+h3+h5-h2-h4-h6.                     (2.1)
```

The corrected Type-II stability row, together with the physical inequality
`y0<=z`, forces `z=y0` when there are exactly two components.  Substituting
(2.1) proves that the second theorem row is exactly

```text
h2+h4+h6 <= 3*o_b+h1+h3+h5+76.                     (2.2)
```

The independent checker exhausts all monotone boundary tuples in a small
model, probes 20,000 tuples in the real `0..462` range, and verifies (2.1)
and (2.2) for all three chains.  In particular, the repaired implementation
does not reintroduce the old chain-A-only `y0` error.

## 3. Exact component and occurrence semantics

### Slack-one union

For every coordinate and position the reverse plan creates

```text
occ1[b,p] <-> slack_one_membership[p] AND A[p,b]
```

with the exact three-clause AND.  The clauses

```text
occ1[b,p] -> has1[b]
has1[b] -> OR_p occ1[b,p]
```

make `has1[b]` exactly `b in OR(C1)`.  The reverse implication is present;
the antecedent cannot be escaped by setting `has1[b]` spuriously true.

### Reused slack-two occurrences

`TypeIITwoComponentPinPlan` owns the exact literals

```text
slack_two_occurrence[b][p]
  <-> slack_two_membership[p] AND A[p,b].
```

The reverse plan calls `exact_count` directly on this retained bank.  It does
not allocate a second C2 conjunction bank.  Source inspection finds one
owner and one consumer, and the prerequisite's old inventory and clause
stream are unchanged when the reverse guard is absent.

The selected-component gates are exact under the prerequisite's exact-one
slack orientation.  Outside the two-component branch both membership banks
are false; inside it they are precisely the oriented `C1` and `C2` physical
positions.

## 4. Counter and comparison audit

The 14-clause full adder was exhaustively checked on all 32 assignments of
its five variables.  It accepts exactly

```text
sum=a XOR b XOR c,
carry=majority(a,b,c).
```

For 465 inputs the Wallace compressor has final bucket profile

```text
[1,2,1,1,2,1,2,2].
```

It uses 453 compressor adders followed by eight ripple adders.  The ninth
output bit is the retained final carry, so every `o_b` is the ordinary
integer in `0..465`, not a modular residue.  Weight conservation follows
inductively from the audited full adder; the independent checker additionally
executes the compressor on every possible count `0..465` under several
different input permutations.

The direct conditional `59<=o_b` comparator was exhaustively checked on all
512 counter values and all four escape assignments.  Its five clauses are
active exactly when

```text
two_components=1 and has1[b]=0.
```

The general guarded unsigned comparator was independently reconstructed and
exhausted over every input, both escape bits, and every prefix-equality
auxiliary assignment at width five.  It is satisfiable exactly when an escape
is true or `left<=right`.  The construction is width-generic.  In production
the width is twelve; every one of the 67 comparison/equality clauses carries
the same two escape literals.  Inactive auxiliaries therefore cannot constrain
the surrounding formula.

All adders retain their carry.  The relevant maxima fit their produced
widths:

```text
h2+h4                         < 2^10,
h2+h4+h6                      < 2^11,
h1+h3+h5+76                   < 2^11,
3*o_b                         < 2^11,
3*o_b+h1+h3+h5+76            < 2^12.
```

## 5. Independent inventory

The inventory follows directly from the audited circuits:

| component | variables | clauses |
|---|---:|---:|
| exact C1 coordinate unions | 5,126 | 20,471 |
| eleven 465-input C2 counters | 10,142 | 70,994 |
| shared/per-coordinate arithmetic and prefix comparisons | 677 | 4,629 |
| eleven conditional `o_b>=59` rows | 0 | 55 |
| **total** | **15,945** | **96,149** |

The arithmetic row consists of 47 shared full adders, 21 per-coordinate
full adders, and eleven prefix-equality variables per coordinate.  This
reconstruction agrees exactly with the plan's independent diagnostics.

## 6. Guard, construction, emission, and diagnostics

The source has all required integration points:

* the environment guard is parsed independently;
* the guard is rejected unless
  `K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1`;
* that prerequisite transitively requires the repaired Type-II filtration,
  local-density plan, and joint rank-five boundary plan;
* the reverse plan is constructed after the oriented component plan and
  before `variable_total` is frozen;
* every stored clause is emitted before solving or build-only return;
* the portal-mode exclusion includes the new guard;
* the main summary reports the guard, total inventory, all three variable and
  clause subinventories, and the threshold clause count.

All unguarded clauses in the reverse plan are exact definitions of fresh
variables.  The only clauses which project a restriction onto old variables
are the two theorem comparisons, and both use the exact escape

```text
{-two_components, slack_one_has[b]}.
```

Thus the module is satisfiability-neutral outside its intended branch.

An invalid standalone invocation exits with status two and prints

```text
K11_FOREST_TYPE2_REVERSE_PIN_LOAD requires
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION
```

The documented minimal prerequisite portfolio also builds successfully;
`named-cell`, `rank-seven`, `subcube`, and residual-lex modules are not hidden
requirements.

## 7. Fresh independent build-only evidence

I compiled the frozen source with

```text
g++ -O2 -std=c++20 -Wall -Wextra -Wpedantic \
  -Iscratch/rank7_independent_hash_stub \
  k11_forest_sat.cpp -o /tmp/k11_type2_reverse_independent_hash
```

The build-only double has SHA-256

```text
2a5f23f1e310ecff7cf9c27596ef047787ab92240e24a2e02f899ea62cdc727c
  scratch/rank7_independent_hash_stub/cadical.hpp
```

It fingerprints every declared variable and emitted literal and aborts if an
emitted variable exceeds `DECLARED`.

On the strongest repaired Type-II portfolio, both an absent reverse guard
and an explicit zero give exactly

```text
variables=3660446 clauses=20079690
INDEPENDENT_FNV64=19f50fb16569305f
ADD_CALLS=88679844 ZEROES=20079690 LITERALS=68600154
DECLARED=3660446 MAXVAR=3660446
```

This is the previously frozen pre-module fingerprint, so retaining the C2
occurrence vectors is a zero-CNF refactor, not merely an equal-count rewrite.

Enabling the reverse guard gives

```text
variables=3676391 clauses=20175839
INDEPENDENT_FNV64=d71c0707b32d9ce8
ADD_CALLS=89098872 ZEROES=20175839 LITERALS=68923033
DECLARED=3676391 MAXVAR=3676391
```

The exact difference is therefore

```text
+15,945 variables / +96,149 clauses.
```

No SAT solve was launched in these runs.

## 8. Independent checker

Running

```text
python3 scratch/audit_k11_type2_reverse_pin_load_source_independent.py
```

prints

```text
source_sha256=3500113db42662e783cb8a4e9d3e247372cad1488f346b8f90b9eb36b55d3e38
full_adder_truth_table=PASS
exact_component_union_truth_table=PASS
conditional_ge59_truth_table=PASS
guarded_unsigned_leq_truth_table=PASS
wallace_carry_and_width_audit=PASS
all_chain_y0_plus_y2_algebra=PASS
retained_occurrence_and_integration_scan=PASS
independent_inventory=15945_variables/96149_clauses
PASS
```

The checker SHA-256 is

```text
36374e6e57a9c90335b3c1c03f7249575acdde57f12cabbb69de276772af7b14
  scratch/audit_k11_type2_reverse_pin_load_source_independent.py
```

## 9. Final scope

The guard is a sound optional strengthening of the repaired Type-II
two-component branch and is ready for a no-proof candidate-search portfolio.
It does not prove that the branch is satisfiable or unsatisfiable.  Any SAT
candidate still requires both independent interval-OR verifiers, and an
UNSAT claim still requires an archived proof trace and independent checking.
