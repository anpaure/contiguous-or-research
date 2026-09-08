# Independent implementation audit of the rank-five singleton-boundary repair

## Verdict

**PASS.**  At the frozen source

```text
f86e80456f2e17fd87774579d11dd090f70f2451e888537212eb1b9613aca6e2
  k11_forest_sat.cpp
```

the repaired Type-I and Type-II rank-filtration circuits encode the exact
rank-five singleton count on all three admitted maximal chains.  The Type-II
`stability_tight` and `duplicate_flag` literals are bidirectionally exact for
the selected chain.  The chain-B/C named-cell rows now include the formerly
omitted `22`/`11` singleton blocks.  Every arithmetic addition retains its
final carry, and every inactive guarded comparison is projection-free.

This audit found no defect in the repair.  It does not revive the old audit
hashes: the earlier A-only Type-I, Type-II, and named-cell implementation
verdicts remain superseded.  It certifies only the corrected source above.

No production source was edited during this audit.

## 1. Exact chain substitutions

Let `h1,...,h6` be the six cumulative boundaries of the selected rank-five
state chain.  Direct state-population summation gives

| chain | `y0` | `y2` |
|---|---|---|
| A: `00 01 02 12 13 23 33` | `462+h1-h6` | `h3+h5-h2-h4` |
| B: `00 01 02 12 22 23 33` | `462+h1+h5-h4-h6` | `h3-h2` |
| C: `00 01 11 12 13 23 33` | `462+h1+h3-h2-h6` | `h5-h4` |

The production Type-II arrays are exactly

```text
A: n5+h6+s       <= h1+464,
B: n5+h4+h6+s    <= h1+h5+464,
C: n5+h2+h6+s    <= h1+h3+464,
```

each guarded by its exact-one `joint.chain_selector`.  Substitution reduces
all three to the theorem `n5-y0+s<=2`.

The Type-I arrays are exactly

```text
A: n5+h6       = h1+462,
B: n5+h4+h6    = h1+h5+462,
C: n5+h2+h6    = h1+h3+462,
```

again guarded by their corresponding selectors.  These are precisely
`n5=y0`, so the literal rank-five values are duplicate-free without excluding
the B/C intermediate singleton blocks.

The named-cell theorem is `y2>=y0+offset`.  Production directly encodes the
equivalent rows

```text
A: h2+h4+h1+(462+offset) <= h3+h5+h6,
B: h2+h1+h5+(462+offset) <= h3+h4+h6,
C: h4+h1+h3+(462+offset) <= h5+h2+h6.
```

Thus B charges the complete `22` block `h5-h4`, and C charges the complete
`11` block `h3-h2`.  The independent checker exhausts every nondecreasing
six-boundary vector in a seven-slot analogue, every small `n5`, component
count, and offset, and verifies equivalence to the three abstract laws.

## 2. Boolean exactness

### Guarded comparison

`add_leq_guarded` prefixes every comparison and every prefix-equality clause
with `-guard`.  When the guard is false, every assignment of the auxiliaries
satisfies the circuit.  When true, the five-clause equality recurrence makes
`equal_above` exact and the leading clause forbids the first unequal pair
`x=1,y=0`.  Exhaustion at width four gives

```text
exists auxiliaries <=> !guard OR x<=y,
```

and confirms that all auxiliary assignments are permitted when inactive.

### Tightness selection

`define_equal_flag` makes one exact XNOR per sum bit and one exact conjunction
of all XNORs.  The source then uses, for each chain `i`,

```text
selector[i] AND chain_equal[i] -> stability_tight,
stability_tight AND selector[i] -> chain_equal[i].
```

Because the joint plan enforces exactly one selector, this is exactly

```text
stability_tight <-> chain_equal[active_chain].
```

Inactive-chain equality values cannot activate or suppress the flag.

The final three clauses are the prime bidirectional encoding

```text
duplicate_flag <-> stability_tight AND !two_components.
```

Under `n5-y0+s<=2`, with the nonempty low ideal giving `s>=1`, the feasible
cases are `(delta,s)=(0,1),(1,1),(0,2)`.  Tightness selects the latter two;
conjoining `!two_components` selects exactly `(1,1)`.  Exhaustive Boolean
truth tables independently verify both gates.

### Carries and widths

The full-adder's fourteen clauses are exact under all 32 input/output
assignments.  Each `add_unsigned` in the three repaired plans appends the
final carry.  Comparisons and equalities zero-extend their operands to the
larger complete width.  The largest repaired Type-II side is below 2048, and
the generated nested sums expose at least twelve bits; no integer can wrap.
The Type-I and named-cell sums have the same nonmodular safety margin.

## 3. Independent executable checker

The checker

```text
ef354009471f11d297e93513ff3fd871ec3bd79bf9da1f05fb83fe9884df7050
  scratch/check_k11_rank5_singleton_boundary_repair.py
```

does not include the C++ source.  It independently checks the affine chain
identities and Boolean truth tables, then verifies that the frozen production
source contains the audited A/B/C expressions and retained-carry statements.

Running

```text
python3 scratch/check_k11_rank5_singleton_boundary_repair.py
```

prints

```text
source_sha256=f86e80456f2e17fd87774579d11dd090f70f2451e888537212eb1b9613aca6e2 PASS
full_adder_truth_table=PASS
guarded_unsigned_leq_truth_table=PASS
exact_equality_flag_truth_table=PASS
active_chain_tightness_and_duplicate_truth_table=PASS
type1_type2_named_cell_chain_algebra=PASS
```

The production source also compiles cleanly with
`-Wall -Wextra -Wpedantic` against the independent build-only CaDiCaL stub.

## 4. Repaired module inventories

Build-only generation reproduces the following exact plan inventories:

| plan/mode | variables | clauses |
|---|---:|---:|
| Type I filtration | 2,493 | 18,462 |
| Type II filtration, duplicate not exposed | 10,032 | 48,816 |
| Type II filtration, duplicate exposed | 10,072 | 49,003 |
| named cell, Type I | 327 | 262,563 |
| named cell, Type II | 661 | 264,282 |

The large named-cell clause totals in this minimal regression use all 1,123
direct targets.  In the optimized full formulas, adjacent/rank-three shadow
compression leaves only 66 direct targets and twelve exception slots, giving
38,451 Type-I named-cell clauses and 40,653 Type-II named-cell clauses.  The
width subcircuits themselves are exactly `327 / 2,259` for Type I and
`661 / 4,536` for Type II (the latter total also includes the three mode
clauses and location auxiliaries in its variable count).

Independent local build-only generation gives:

| formula | variables | clauses | clause-stream FNV64 |
|---|---:|---:|---|
| all optional guards off | 4,892,622 | 15,524,818 | `ad22e261832b9ae2` |
| Type I + named-cell minimal prerequisites | 4,961,761 | 16,340,886 | `5a9d99501be6ac9d` |
| Type II + named-cell minimal prerequisites | 4,969,433 | 16,156,656 | `c2cb4d5865fe4b47` |
| full Type I, including facet and ridge | 3,669,795 | 20,162,593 | `e0a78e073e9f129a` |
| full Type II | 3,660,446 | 20,079,690 | `97fd4ee01d10aa7a` |

The two full inventories agree exactly with independent remote build-only
generation.  The FNV values are local fingerprints from
`scratch/cadical_hash_stub`; they are build evidence, not SAT evidence.

For the Type-II prerequisites, absent and explicit-zero filtration/named-cell
guards both produce

```text
variables=4,958,700 clauses=15,843,371
CLAUSE_STREAM_FNV64=6ea1dff3eaf69eae.
```

Thus the repaired plans allocate and emit nothing when disabled.  The same
construction guards are used for Type I.  Within an enabled named-cell plan,
the exact conjunction of its branch literal with the active chain selector
guards every A/B/C width comparator.

## 5. Scope

This is an exact implementation audit, not a SAT or UNSAT result for
`k=11,n=465`.  It restores satisfiability-completeness of the three circuits
poisoned by the intermediate-zero-state bug.  The remote solver portfolios
must use this repaired source or a byte-identical audited copy; results from
the superseded A-only formulas cannot certify either complete branch.
