# Independent audit of the `k=11` rank-six branch/profile design

## Verdict

**PASS, with two non-material checker-scope qualifications.**  The design in

```text
K11_FOREST_RANK6_BRANCH_AND_PROFILE_DESIGN.md
SHA-256 2a8816fe2cc312b0c99fb8008e272c48bf03baeb1e91ec7b90e196eae68ae753
```

is mathematically sound and implementation-safe under its four stated
dependencies:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1.
```

The sole 12-literal anchor is satisfiability-preserving and, together with
the existing hard clauses, gives the exact equivalence

```text
A[0]=63 <-> e.
```

Consequently units `-e` and `e` form a disjoint and exhaustive portfolio.
The stronger singleton profile row is transformed correctly on all three
rank-five chains; the constants 544 and 557, all signs, and the exact circuit
inventory `241 variables / 1,659 clauses` are correct.

The supplied checker correctly verifies its small-boundary algebra and all
reported arithmetic inventories.  Two claims in the design's checker
description are broader than its code:

1. it prints, but does not construct or assert, the anchor clause;
2. it does not test the proposed double-guard comparator or proof-certificate
   case split.

These are coverage/documentation limitations, not errors in the design.  I
checked both independently below.  A second independent checker is included
as an audit artifact.

No solver source, main handoff, or design file was edited.

## 1. Exact anchor polarity

The proposed clause is

```text
e
OR -A[0,0] OR ... OR -A[0,5]
OR  A[0,6] OR ... OR  A[0,10].
```

For the canonical mask

```text
63={0,1,2,3,4,5},
```

all eleven array literals are false exactly when `A[0]=63`.  Thus the clause
is exactly

```text
A[0]=63 -> e.
```

It has 12 literals, one clause, no fresh variable, and is automatically true
for every other value of `A[0]`.  The independent checker exhausts all 2,048
entry values and both values of `e`.

## 2. Reverse implication from the existing hard formula

`JointBandCutPlan` first enforces `x0<=1` and then defines `e` in both
directions as the OR of every selected rank-six `00` or `33` state.  These
are exactly the remaining width-zero states in the rank-six band.  Therefore

```text
e=1
```

means that one selected rank-six interval is a physical singleton `[p,p]`.

The central interval/value clauses make the selected central value the exact
OR of its physical interval and separately force rank six.  For a singleton,
the value is exactly `A[p]`, so `A[p]` has rank six.

Under the simultaneous canonical and boundary-entry guards, the only allowed
literal rank-six value/position pair is

```text
(p,A[p])=(0,63).
```

All noncanonical rank-six values are forbidden globally, and 63 is forbidden
at positions 1 through 464.  Hence the existing clauses already imply

```text
e -> A[0]=63.
```

No additional reverse anchor clause is needed.  Notice that this argument
uses the literal-entry guards directly and does not need to infer the
singleton's boundary from a preferred schedule orientation.

If no literal rank-six entry exists, a selected rank-six singleton cannot
exist, because its exact OR would itself be a literal rank-six entry.  Thus
all auxiliary witness encodings necessarily have `e=0` in the no-occurrence
branch.

## 3. Why the forward anchor is a valid WLOG reselection

The forward implication is not true for every arbitrary auxiliary schedule:
an array with `A[0]=63` might initially choose a longer interval as target
63's witness.  The design correctly treats the anchor as a
satisfiability-preserving witness-reselection choice.

Start from a valid array already placed in the audited canonical-left normal
form.  If `A[0]=63`, select `[0,0]` as the witness for target 63 and choose
one witness for every other rank-six target.  No other chosen rank-six
interval can contain position zero.  Such an interval's OR would contain the
six-set 63; because its target also has rank six, it would have to equal 63,
whose sole selected witness has already been fixed.

The reselected equal-rank family remains nonnested.  Its left and right
endpoints are distinct; after sorting, it has the usual unrestricted
monotone-band representation.  The `[0,0]` witness is the first interval in
state `00`, so the exact joint-band definition gives `e=1`.

### 3.1 Composition with every current auxiliary block

I checked that this reselection does not rely on retaining any phase or old
existential auxiliary assignment:

| block | why it can be rebuilt after reselection |
|---|---|
| central target columns | assign target 63 to the new singleton and permute the other exact rank-six columns with their selected intervals |
| central phases | `solver.phase(...)` is heuristic only and imposes no hard clause |
| rank-six band | the band/profile inequalities hold for every selected rank-six family; exact boundaries are recomputed from the new monotone schedule |
| joint rank-five/rank-six band | its inequalities are necessary for every independently selected pair; choose the rank-five family independently and rebuild its chain selector/boundaries |
| singleton-pool cut, if enabled | the short-pool theorem applies to every selected singleton family and gives its required `x3>=95` branch |
| adjacent rank-seven shadows | the endpoint-crossing theorem gives at most six exceptions for every selected rank-six family; active flags and exception slots are existentially reassigned |
| rank-four and rank-three shadows | rebuild from an independently chosen rank-five family; their crossing theorems are universal in that family |
| endpoint alignment | its four lower bounds hold for every independently selected central pair; summaries and conjunctions are deterministic once the schedules are rebuilt |
| rank-five/rank-six forest | shared-endpoint inclusion is a necessary property of the new actual intervals; left/right forest clauses are rematerialized |
| rank-six endpoint summaries | exact begin/end summaries are recomputed from the reselected schedule |
| canonical/boundary literal gates | constrain only the unchanged normalized array, not the auxiliary witness choice |

The optional exception slots do not preserve target identities from a prior
schedule; they are fresh existential witnesses.  No current hard clause fixes
a central target to the phase seed.  Therefore there is no hidden conflict
with central phases, endpoint colours, or compressed shadow auxiliaries.

If no rank-six literal occurs, `e=0` is automatic and the forward anchor is
vacuous.  This proves equisatisfiability of the anchored formula with the
currently normalized existence problem.

## 4. Exact two-branch partition

Let `F` be the guarded formula plus the anchor.  Since `e` is Boolean,

```text
F  ==  (F AND -e) OR (F AND e)
```

as a logical identity.  The two subformulas are disjoint.  The anchored
equivalence gives their precise array meanings:

```text
F AND -e : no literal rank-six entry exists;
F AND  e : A[0]=63 is the unique literal rank-six occurrence.
```

Exhaustiveness relative to the original unrestricted problem follows in the
correct order:

1. the array theorem gives at most one rank-six literal occurrence;
2. coordinate symmetry names its mask 63;
3. reversal moves it, if present, to position zero;
4. witness reselection sets `e=1` in that branch;
5. absence of an occurrence forces `e=0` in the other branch.

The common anchor costs one clause; each branch unit costs one additional
clause.

## 5. Proof-certificate meaning of the case split

Two checked UNSAT results for `F AND e` and `F AND -e` prove `F` unsatisfiable
mathematically.  They are not, merely by concatenation, one standard DRAT or
LRAT proof for `F`, because each proof has a different input unit.

The design's certificate warning is correct.  A proof-producing deployment
must do one of the following:

* use a checker that validates a cube/case-split manifest plus both branch
  proofs;
* transform/discharge the assumptions to derive the opposite units inside a
  common proof and resolve them; or
* rerun the unbranched anchored formula proof-producing after the portfolio
  has served its search purpose.

In addition, the passage from the original labelled/oriented search to `F`
uses the audited human symmetry and reselection theorem; an ordinary CNF
proof checker certifies the anchored CNF, not that external WLOG reduction.
This is the same proof-status convention already used for the other symmetry
guards.

## 6. Rank-six boundary identities and constants

Write the counts of the rank-six chain states

```text
00,01,02,03,13,23,33
```

as `c0,...,c6`.  The production one-based boundaries satisfy

```text
g1=c0,
g2=c0+c1,
g5=c0+c1+c2+c3+c4,
g6=462-c6.
```

Therefore

```text
x0=c0+c6=g1+462-g6=e,
x1=c1+c5=(g2-g1)+(g6-g5),
x0+x1=g2+462-g5,
x1=g2+462-g5-e.
```

Substitute the last identity into the audited singleton-boundary inequality

```text
y2>=x1+82+14e.
```

This gives

```text
g2 + (462+82) + (14-1)e <= y2+g5,
g2 + 544 + 13e             <= y2+g5.
```

Thus the constants are exactly

```text
544 when e=0,
557 when e=1.
```

The subtraction of one copy of `e` through the formula for `x1` is why the
singleton constant is 557 rather than 558.

### Wording qualification about branch zero

For `e=0`, the desired row is `y2>=x1+82`.  It is already a logical
consequence of the currently encoded joint rows.  In fact the encoded fan
and first cumulative-nesting rows imply the slightly stronger

```text
y2>=x1+84
```

when `e=0`.  The production joint plan does not contain a dedicated
`g2+544<=y2+g5` comparator.  Therefore “already encoded joint-pool
inequality” in the design should be read as “already implied by the encoded
joint circuit.”  The conclusion that branch zero needs no new arithmetic is
correct.

## 7. Chain transformations

For a rank-five chain with boundary counts `h1,...,h6`:

### Chain A

```text
00,01,02,12,13,23,33
y2=(h3-h2)+(h5-h4).
```

The `e=1` row is

```text
g2+557+h2+h4 <= h3+h5+g5.
```

### Chain B

```text
00,01,02,12,22,23,33
y2=h3-h2,
g2+557+h2 <= h3+g5.
```

### Chain C

```text
00,01,11,12,13,23,33
y2=h5-h4,
g2+557+h4 <= h5+g5.
```

All three transformations have the correct signs.  The supplied checker
exhausts small monotone boundary tuples; the independent checker instead
exhausts genuine seven-state count compositions for both central chains and
recovers the same equivalences.

The displayed singleton profile

```text
x=(1,0,366,95), y=(0,366,96)
```

satisfies the real row at equality:

```text
g2+557=1+557=558=y2+g5=96+462.
```

## 8. Guard semantics

The anchor must require all four stated dependencies:

* canonical + boundary provide `e -> A[0]=63` and the left-oriented normal
  form;
* band + joint allocate the reused boundaries and exact `e=x0` bit.

For a branch-specialized `e=1` build, all three new rows are generated and
each comparison is guarded by its exact rank-five chain selector.  The unit
`e` makes a second comparison guard unnecessary.  In the `e=0` build no new
profile arithmetic is generated.

For one common formula, every order clause and all five prefix-equality
definition clauses at every comparator bit must contain both `-e` and the
negated chain selector.  Then the comparison is inactive whenever either
guard is false and exact when both are true.  No conjunction variable is
needed.

The ripple adders may remain unguarded.  They are total exact definitions:
for every boundary assignment they have a unique extension to their sum and
carry bits.  Consequently they cannot restrict an inactive branch.  Guarding
all comparator clauses, including the equality definitions, gives the
cleanest existential projection.

## 9. Independent circuit inventory

The production `add_unsigned` at operand width `w` uses

```text
2w variables, 14w clauses, output width w+1.
```

A guarded comparator of final width `w` uses

```text
w-1 variables, 6w-5 clauses.
```

Using the specified left-associative term orders gives:

| row | additions | adder variables/clauses | final comparison width | comparator variables/clauses | total |
|---|---|---:|---:|---:|---:|
| A | left `9+9`, `10+9`, `11+10`; right `9+9`, `10+9` | `98 / 686` | 12 | `11 / 67` | `109 / 753` |
| B | left `9+9`, `10+10`; right `9+9` | `56 / 392` | 11 | `10 / 61` | `66 / 453` |
| C | same widths as B | `56 / 392` | 11 | `10 / 61` | `66 / 453` |
| **total** | | **210 / 1,470** | | **31 / 189** | **241 / 1,659** |

Adding a second guard literal changes neither variables nor clauses.  Constant
557 has ten bits and uses signed literals of the existing true constant, so
it allocates nothing.

The complete increments are therefore exactly:

```text
anchor only:                    0 variables /    1 clause
profile circuit:              241 variables / 1,659 clauses
anchor + common profile:      241 variables / 1,660 clauses
either common-CNF branch:     241 variables / 1,661 clauses

specialized e=0 branch:         0 variables /    2 clauses
specialized e=1 branch:       241 variables / 1,661 clauses.
```

## 10. Audit of the supplied checker

The supplied checker has SHA-256

```text
d4a51d25a458ad0025b9e34002617a04aad82f3dee0d59aeb0edc1b68181d80e.
```

It compiles warning-free and prints the documented output.  Its implemented
checks are correct:

* the small monotone-boundary algebra for all three chains;
* the real explicit profile equality;
* the exact width-by-width adder and comparator costs.

Its final anchor line is a literal `cout`; no anchor clause or truth table is
constructed, despite the design description saying the checker asserts that
inventory.  It also does not instantiate the double-guard comparator or
certificate split.  These omissions do not make any reported arithmetic
false, but they should not be cited as machine verification of those parts.

The independent audit checker is

```text
scratch/audit_k11_rank6_branch_profile_design_independent.cpp
SHA-256 289e40fa1a52c8fbb8041720e27a376b671cff83d237f41ba333d28f1541ac39
```

It exhausts the actual anchor truth table, genuine small chain-count
profiles, both guard values, the arithmetic inventories, and the Boolean
case partition.  It reports:

```text
anchor_truth_table=PASS length=12 clauses=1 variables=0
genuine_chain_profile_algebra=PASS constants=544,557
profile_circuit_variables=241 clauses=1659
branch_partition=PASS
independent_rank6_branch_profile_design_audit=PASS
```

## 11. Certified scope

This is a correct design, not yet an implemented solver guard or a search
result.  An implementation still needs an independent source-level audit of
guard dependencies, clause polarities, variable declaration, and exact
formula deltas.  Two UNSAT branch searches still need properly packaged and
checked proof evidence before they support an exact mathematical claim.
