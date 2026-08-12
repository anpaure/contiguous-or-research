# Independent audit of the Type-II companion pin-load production circuit

## 1. Verdict

**PASS**, for the frozen production source

```text
2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
  k11_forest_sat.cpp
```

I found no theorem-to-CNF, occurrence-reuse, counter, arithmetic, comparison,
guard, construction, emission, inventory, or repaired-chain-composition defect
in `K11_FOREST_TYPE2_COMPANION_PIN_LOAD`.

The exact incremental inventory is

```text
10,220 variables / 71,628 clauses.
```

This is an independent source/build audit.  It is not a SAT result, an UNSAT
result, or a change to the rigorous bound on `nu(11)`.

## 2. Mathematical row represented by the circuit

In the exact Type-II two-component branch, orient the components as

```text
C1 = the selected slack-one rank-at-most-four component,
C2 = the selected slack-two rank-at-most-four component.
```

Fix a coordinate `b` absent from `OR(C2)`.  Every lower target containing `b`
must be witnessed in `C1`: it cannot meet a literal rank-five separator and it
cannot lie in `C2`.  Every interval of `C1` of length at least two contains an
internal adjacent pair, and all those pairs have rank five.  Thus every target
of rank at most four containing `b` occurs literally in `C1`.  Their number is

```text
C(10,0)+C(10,1)+C(10,2)+C(10,3)
  = 1+10+45+120
  = 176.
```

Writing

```text
o1(b) = #{p in C1 : b in A[p]},
n1    = |C1|,
z     = the number of literal rank-five entries,
```

gives the first encoded row

```text
b notin OR(C2)  =>  o1(b) >= 176.                  (2.1)
```

There are `C(10,4)=210` rank-five targets containing `b`.  At most `z` are
literal.  Every remaining such target must use one of the `n1-1` internal
adjacent pairs of `C1`.  Therefore

```text
n1-1 >= 210-z,
b notin OR(C2)  =>  n1+z >= 211.                   (2.2)
```

Both are necessary rows.  The use of total `z`, rather than the smaller
number of literal rank-five values containing `b`, only weakens (2.2).

## 3. Exact reused semantics

### 3.1 The C1 occurrence bank is not rebuilt

`TypeIIReversePinLoadPlan` already owns the exact literals

```text
occ1[b,p] <-> slack_one_membership[p] AND A[p,b].
```

The three-clause AND appears once in the reverse prerequisite.  The companion
plan calls

```text
exact_count(reverse.slack_one_occurrence[b])
```

directly.  It allocates no second `occ1` bank.  Source inspection finds one
producer and one companion consumer of the retained vector.

### 3.2 The antecedent is exact

`TypeIITwoComponentPinPlan` defines

```text
slack_two_has[b] <-> OR_p(
    slack_two_membership[p] AND A[p,b]
).
```

Both the forward occurrence implications and the long reverse OR clause are
present.  Hence `slack_two_has[b]` cannot be set spuriously true to escape a
row.  Every substantive companion clause has the escape

```text
{-two_components, slack_two_has[b]}.
```

It is active exactly when the two-component branch holds and `b` is absent
from `C2`.

### 3.3 The size row uses exact physical counts

The localization prerequisite owns exact counters

```text
slack_one_rank_count[1],...,[4].
```

Each counts an exact conjunction of `slack_one_membership[p]` with the exact
one-hot entry-rank flag.  Type II forbids ranks six and above, and the selected
low components are exactly the non-rank-five positions.  The word is
zero-free.  Consequently

```text
n1 = count_rank1(C1)+...+count_rank4(C1).
```

`type_two.n5_count` is the exact count `z` of rank-five entries.  The companion
therefore encodes (2.2) from exact physical quantities, without a guessed
component size or a chain-specific singleton formula.

## 4. Counter, arithmetic, and comparator audit

The 14-clause full adder was exhausted on all 32 assignments of
`(a,b,carry,sum,next_carry)`.  It accepts exactly parity and majority.

For 465 inputs the Wallace compression has final bucket profile

```text
[1,2,1,1,2,1,2,2].
```

It uses 453 compressor adders and eight final ripple adders.  The ripple's
last carry is retained, producing a nine-bit ordinary integer in `0..465`,
not a modular residue.  The independent checker executes the compression at
every possible input count `0..465` and preserves weighted value exactly.

The four component rank counters are nine-bit vectors.  The shared size
arithmetic has widths

```text
(9+9), (9+9), (10+10), (11+9),
```

so it uses 39 full adders, or 78 variables and 546 clauses.  Its final width
is twelve bits.  The maximum possible value `n1+z<=465+134=599` cannot
overflow it.

The direct first-difference comparator was independently exhausted for every
nine-bit value at constant 176 and every twelve-bit value at constant 211,
under all four assignments of the two escape literals.  It is satisfiable
exactly when an escape is true or the encoded integer meets the threshold.
The two constants have three and five set bits respectively, so the eleven
named-coordinate guards use `11*3=33` and `11*5=55` clauses.

## 5. Independent inventory

| component | variables | clauses |
|---|---:|---:|
| eleven reused-bank 465-input counters | 10,142 | 70,994 |
| eleven guarded `176<=o1(b)` comparisons | 0 | 33 |
| one shared exact `n1+z` addition tree | 78 | 546 |
| eleven guarded `211<=n1+z` comparisons | 0 | 55 |
| **total** | **10,220** | **71,628** |

The production diagnostics agree exactly:

```text
type2_companion_pin_load_variables=10220
type2_companion_pin_load_clauses=71628
type2_companion_pin_load_counter_variables=10142
type2_companion_pin_load_counter_clauses=70994
type2_companion_pin_load_arithmetic_variables=78
type2_companion_pin_load_arithmetic_clauses=546
type2_companion_pin_load_threshold_clauses=88
```

Here the final `88` is the combined `33+55` direct-comparison clauses.

## 6. Guard and repaired-chain composition

The source has every required integration point:

* it parses `K11_FOREST_TYPE2_COMPANION_PIN_LOAD` independently;
* it rejects that guard unless `K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1`;
* the reverse prerequisite transitively requires exact two-component
  localization and the repaired Type-II filtration;
* the companion is included in the portal-mode exclusion;
* the plan is constructed after all three prerequisites and before
  `variable_total` is frozen;
* every stored clause is emitted before build-only return or solving;
* the main summary reports the guard, total inventory, and every subinventory.

The companion row is chain-independent.  It uses actual component memberships,
actual entry ranks, and actual `n5`; it does not substitute a chain-A formula
for `y0`.  The independent source scan nevertheless verifies all three
repaired Type-II stability rows:

```text
A: n5+h6+s       <= h1+464,
B: n5+h4+h6+s    <= h1+h5+464,
C: n5+h2+h6+s    <= h1+h3+464.
```

It also verifies the exact-one slack-component selector.  Thus composition
does not reintroduce the old A-only zero-state bug.

All unguarded companion clauses are exact definitions of fresh counters and
sums.  The only projected restrictions are (2.1) and (2.2), and every clause
of both carries the exact escape.  The module is therefore
satisfiability-neutral outside its intended branch.

An invalid standalone invocation exits with status two and prints

```text
K11_FOREST_TYPE2_COMPANION_PIN_LOAD requires
K11_FOREST_TYPE2_REVERSE_PIN_LOAD
```

The minimal transitive prerequisite portfolio also builds successfully;
adjacent shadows, rank-three compression, named-cell Hall, rank-seven,
subcube, containment, and residual-lex modules are not hidden requirements.

## 7. Independent emitted-CNF builds

I compiled the frozen source with

```text
g++ -O2 -std=c++20 -Wall -Wextra -Wpedantic \
  -Iscratch/rank7_independent_hash_stub \
  k11_forest_sat.cpp -o /tmp/k11_type2_companion_independent_hash_current
```

Hashes were

```text
2a5f23f1e310ecff7cf9c27596ef047787ab92240e24a2e02f899ea62cdc727c
  scratch/rank7_independent_hash_stub/cadical.hpp
839b1d6dfc7cbf939205f1e634ef3c0995ab7a9729190d54be746ddcefb7a4a0
  /tmp/k11_type2_companion_independent_hash_current
```

On the strongest repaired Type-II portfolio, both an absent companion guard
and an explicit zero produce the identical stream

```text
variables=3676391 clauses=20175839
INDEPENDENT_FNV64=d71c0707b32d9ce8
ADD_CALLS=89098872 ZEROES=20175839 LITERALS=68923033
DECLARED=3676391 MAXVAR=3676391
```

This proves guard-off identity at the complete emitted-literal-stream level,
not merely equal clause totals.

Enabling the companion gives

```text
variables=3686611 clauses=20247467
INDEPENDENT_FNV64=a26c53da59943576
ADD_CALLS=89426759 ZEROES=20247467 LITERALS=69179292
DECLARED=3686611 MAXVAR=3686611
```

The exact difference is

```text
+10,220 variables / +71,628 clauses.
```

`MAXVAR=DECLARED` in both builds, so every allocated variable is declared and
no emitted clause references an out-of-range variable.  No SAT solve was
performed by the audit double.

## 8. Independent checker

Running

```text
python3 scratch/audit_k11_type2_companion_pin_load_source_independent.py
```

prints

```text
source_sha256=2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
full_adder_truth_table=PASS
conditional_ge176_and_ge211_truth_tables=PASS
wallace_carry_and_width_audit=PASS
theorem_constants_and_shared_sum_widths=PASS
retained_C1_bank_and_C2_guard_source_scan=PASS
repaired_A_B_C_prerequisite_scan=PASS
independent_inventory=10220_variables/71628_clauses
PASS
```

The checker SHA-256 is

```text
77e2005be2f778cecdf519b505d8cc416391165faca46590620653026a223b03
  scratch/audit_k11_type2_companion_pin_load_source_independent.py
```

## 9. Final scope

`K11_FOREST_TYPE2_COMPANION_PIN_LOAD` is a sound optional strengthening of
the repaired Type-II two-component branch and is ready for a no-proof
candidate-search benchmark.  It does not prove that the branch is satisfiable
or unsatisfiable.  A SAT candidate still needs both independent interval-OR
verifiers, while an UNSAT claim still requires an archived proof trace and
independent proof checking.
