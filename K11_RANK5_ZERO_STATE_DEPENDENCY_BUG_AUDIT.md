# Authoritative audit: rank-five intermediate-zero-state bug and repair map

## 1. Verdict

**CRITICAL ENCODING DEFECT; FOUNDATIONAL THEOREMS SURVIVE.**

The current production source and several implementation audits use

```text
y0 = h1+462-h6.                                        (1.1)
```

for every one of the three allowed rank-five maximal chains.  Equation
(1.1) is true only on chain A, or on chain B/C when the intermediate
width-zero state has population zero.  The first false sentence is that all
three chains have width-zero states only at their first and last vertices.
In fact

```text
A = 00,01,02,12,13,23,33,
B = 00,01,02,12,22,23,33,
C = 00,01,11,12,13,23,33.
```

Chain B contains the width-zero state `22`; chain C contains the width-zero
state `11`.

This is not a defect in rank-filtration stability itself.  The exact
mathematical laws

```text
Type II: n5-y0+s <= 2,
Type I:  n5=y0
```

remain valid under the canonical singleton witness choice.  The defect is
the conversion of `y0` to boundary arithmetic.  Consequently:

* `RankFiltrationTypeIIPlan` is not satisfiability-complete as written;
* its `stability_tight` and `duplicate_flag` are not certified exact;
* `RankFiltrationTypeIPlan` is not satisfiability-complete as written;
* the chain-B/C named-cell selected-width rows use the wrong `z=y0`;
* every production portfolio inheriting either filtration guard is not a
  valid exhaustive branch search until these three direct circuits are
  repaired.

The Type-II reverse pin-load optimization itself is algebraically correct.
Its proposed `15,945 / 96,149` circuit must not be deployed on top of the
current broken prerequisite.

No production source was edited by this audit.

## 2. Exact chain arithmetic

Let `h_j` be the number of slots in the first `j` states of the selected
seven-state chain, in the production one-based notation.  Directly summing
state populations gives:

| chain | `y0` | `y2` | missed by (1.1) |
|---|---|---|---|
| A | `462+h1-h6` | `h3+h5-h2-h4` | `0` |
| B | `462+h1+h5-h4-h6` | `h3-h2` | `h5-h4=#22` |
| C | `462+h1+h3-h2-h6` | `h5-h4` | `h3-h2=#11` |

These are already recorded correctly in
`K11_FOREST_JOINT_BAND_IMPLEMENTATION_AUDIT.md`.  In all three cases,

```text
y0+y2 = 462+h1+h3+h5-h2-h4-h6.                       (2.1)
```

Equation (2.1) is the valid chain-independent identity used by the optimized
reverse pin-load design.

The current endpoint-only expression is

```text
y0_endpoint=h1+462-h6=#00+#33.
```

Thus current Type-II arithmetic enforces

```text
n5-y0_endpoint+s = (n5-y0)+s+#intermediate-zero <=2,  (2.2)
```

not the stability theorem.  It silently charges every selected `11` or `22`
singleton as if it were a literal duplicate.

## 3. Exact counterprofiles

The following profiles are endpoint schedules, not claimed OR arrays.  That
is enough to refute the asserted algebraic equivalence and to show that the
existing band/joint prerequisites do not remove the missing states.

### 3.1 Type II, two components, chain B

Use the chain-B state populations

```text
(#00,#01,#02,#12,#22,#23,#33)
  = (0,0,200,0,1,162,99).                             (3.1)
```

Then

```text
(h1,h2,h3,h4,h5,h6)=(0,0,200,200,201,363),
(y0,y1,y2)=(100,162,200).
```

The physical intervals are especially transparent:

* 200 state-`02` triples lie in positions `0,...,201`;
* the state-`22` singleton is physical position `202`;
* 162 state-`23` pairs lie in positions `203,...,365`;
* 99 state-`33` singletons are positions `366,...,464`.

Thus the schedule has exactly two prospective low components, of slacks two
and one, separated by a literal singleton, followed by a literal rank-five
suffix block.  Put `n5=100` and `s=2`.  The true stability row is tight:

```text
n5-y0+s=100-100+2=2.
```

The current source rejects it:

```text
n5+h6+s = 465 > 464 = h1+464.
```

The repaired chain-B row is exact:

```text
n5+h4+h6+s = 665 = h1+h5+464.                         (3.2)
```

The rank-six profile

```text
(x0,x1,x2,x3)=(0,100,160,202)
```

satisfies every existing rank-six band and joint rank-five/rank-six scalar
cut, including the strengthened `x0<=1` row.

### 3.2 Type I, one suffix core, chain C

Use the chain-C populations

```text
(#00,#01,#11,#12,#13,#23,#33)
  = (0,0,1,0,200,162,99).                             (3.3)
```

Then

```text
(h1,h2,h3,h4,h5,h6)=(0,0,1,1,201,363),
(y0,y1,y2)=(100,162,200).
```

The selected singleton positions are exactly

```text
1,366,367,...,464,
```

and every non-singleton rank-five witness lies in positions `2,...,365`.
This has precisely the Type-I physical architecture: the unique rank-six
entry may be position zero, literal rank-five entries form prefix/suffix
boundary blocks, and the rank-at-most-four entries form one central suffix
core.

With `n5=100`, duplicate freedom is exactly `n5=y0`.  The current equality
fails,

```text
n5+h6=463 !=462=h1+462,
```

while the repaired chain-C equality holds:

```text
n5+h2+h6=463=h1+h3+462.                               (3.4)
```

The branch-one-compatible rank-six profile

```text
(x0,x1,x2,x3)=(1,99,160,202)
```

satisfies the band, joint, and branch-one `y2>=x1+82+14*x0` rows.

These examples do not prove that either profile extends to a complete OR
word.  They prove the narrower and decisive point: the claimed boundary
identity is false on schedules explicitly admitted by the exact joint-chain
encoding, including schedules with the intended physical onion geometry.

## 4. Exact production repairs

### 4.1 Type-II stability row

Retain the theorem `n5-y0+s<=2`, but guard the following exact comparisons by
the existing chain selectors:

| chain | corrected comparison |
|---|---|
| A | `n5+h6+s <= h1+464` |
| B | `n5+h4+h6+s <= h1+h5+464` |
| C | `n5+h2+h6+s <= h1+h3+464` |

The current unguarded A row must be removed.  Every sum must retain its final
carry and every inactive chain comparison must guard the complete prefix-
equality circuit.

When the named-cell guard requests a duplicate flag, define
`stability_tight` as equality in the one selected corrected row.  The final
Boolean identity remains

```text
duplicate_flag <-> stability_tight AND !two_components_flag.   (4.1)
```

Under the corrected theorem cases `(delta,s)=(0,1),(1,1),(0,2)`, (4.1) is
again exact.  Reusing the current equality flag from the endpoint-only row is
not safe: with an intermediate zero state it tests
`delta+s+#intermediate-zero=2`.

### 4.2 Type-I duplicate-free equality

Guard the following exact equalities by the selected rank-five chain:

| chain | corrected equality |
|---|---|
| A | `n5+h6 = h1+462` |
| B | `n5+h4+h6 = h1+h5+462` |
| C | `n5+h2+h6 = h1+h3+462` |

The rank cap, `n5<=133`, and exact one-component suffix circuit are
independently valid and need no mathematical change.

### 4.3 Named-cell width rows

The theorem rows are unchanged:

```text
y2>=y0+c,
c=96  in Type I and duplicate Type II,
c=95  in two-component Type II.
```

For `K=462+c`, the exact chainwise comparisons are:

| chain | corrected comparison |
|---|---|
| A | `h2+h4+h1+K <= h3+h5+h6` |
| B | `h2+h1+h5+K <= h3+h4+h6` |
| C | `h4+h1+h3+K <= h5+h2+h6` |

The source currently has the correct A row but omits `h5/h4` in B and
`h3/h2` in C.  Its checker makes the same mistake by assigning the A formula
for `y0` to every chain.

### 4.4 Optimized reverse pin-load row

In the corrected two-component branch, stability still gives duplicate
excess zero, hence `z=y0`.  Combining this with (2.1) makes

```text
3*o_b+z+y2>=386
  <=> h2+h4+h6 <= 3*o_b+h1+h3+h5+76.                 (4.2)
```

Therefore the optimized reverse design is not affected by the chain-B/C
correction.  Its local circuit and frozen inventory remain:

```text
preferred reuse: 15,945 variables / 96,149 clauses,
fallback rebuild: 21,060 variables / 111,494 clauses.
```

It saves exactly `1,335 / 7,640` relative to the earlier
`17,280 / 103,789` materialized-`y2` design.  Deployment is blocked only by
the prerequisite repair and subsequent source audit.

## 5. Complete source/module dependency ledger

### 5.1 Directly broken production logic

| source object | status | required action |
|---|---|---|
| `RankFiltrationTypeIIPlan` stability comparison | **broken** | replace the unguarded A row by the three guarded rows in 4.1 |
| `RankFiltrationTypeIIPlan::stability_tight` | **broken** | equality of the selected corrected row |
| `RankFiltrationTypeIIPlan::duplicate_flag` | **not exact through bad input** | Boolean gate may remain after `stability_tight` is repaired |
| `RankFiltrationTypeIPlan` duplicate equality | **broken** | use the three guarded equalities in 4.2 |
| `NamedCellFamilyPlan::add_width_rows` B/C rows | **broken** | add the missing boundary terms from 4.3 |

The stale source comments at the Type-I/II plans and named-cell plan must be
replaced at the same time; leaving the old identity in documentation would
make a future regression likely.

### 5.2 Directly stale documents/checkers

The following artifacts assert or test (1.1) for every chain and must lose
their prior PASS status until updated:

```text
K11_RANK_FILTRATION_ENCODING.md
K11_RANK_FILTRATION_ENCODING_AUDIT.md
K11_RANK_FILTRATION_TYPE1_ENCODING.md
K11_RANK_FILTRATION_TYPE1_ENCODING_AUDIT.md
K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING.md
K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING_AUDIT.md
K11_NAMED_CELL_FAMILY_ENCODING.md
K11_NAMED_CELL_FAMILY_ENCODING_AUDIT.md
scratch/verify_k11_rank_filtration_type1.cpp
scratch/check_k11_named_cell_family.py
MATHEMATICAL_HANDOFF.md (the corresponding implementation-ledger entries)
```

`K11_FOREST_JOINT_BAND_IMPLEMENTATION_AUDIT.md` and
`K11_FOREST_JOINT_SHORT_BAND_CUTS_AUDIT.md` contain the correct table and are
authoritative for the boundary algebra.

### 5.3 Theorems/circuits that remain mathematically valid

| artifact family | theorem/circuit verdict | dependency consequence |
|---|---|---|
| `RANK_FILTRATION_STABILITY.md` and audit | **theorem valid** | its `delta+s<=2` law is the repair target |
| `K11_ONION_NAMED_CELL_HALL.md` and audit | **theorem valid** | only the source substitution for `z=y0` is wrong |
| `K11_TWO_COMPONENT_PIN_LOCALIZATION.md` and audit | **theorem/circuit valid conditional on a real two-component branch** | no local clause change from this bug; global WLOG claim waits for repaired Type II |
| Type-I core/subcube run-credit circuit | **valid conditional Type-I consequence** | no local arithmetic change; cannot support an exhaustive UNSAT claim through the current Type-I prerequisite |
| Type-I facet and ridge pin-load theorems/circuits | **valid conditional Type-I consequences** | inventories/gates remain correct; transitive branch completeness is blocked |
| residual-coordinate lex and Type-I canonical-prefix chain | **valid symmetry/consequence circuits** | do not use (1.1), but inherit the incomplete Type-I guard |
| rank-seven truncated-width circuit | **valid branch-conditional theorem** | no local change; exhaustive use waits for both filtration repairs |
| rank-six branch profile circuit | **valid** | already uses the correct chainwise `y2` formulas |
| Type-II reverse pin-load theorem and optimized design | **valid conditional theorem/design** | deploy only after the Type-II/NamedCell prerequisite stack is repaired |

The distinction is important.  There is no newly found counterexample to a
pin-load, subcube, facet, ridge, or rank-filtration theorem.  The error is an
incorrect endpoint-state projection in the SAT realization of those valid
theorems.

## 6. Search consequences

Any SAT model produced with the current guards is still a legitimate
candidate after ordinary independent interval-OR verification: the defect
only adds restrictions.  An UNSAT result or prolonged failure under either
current filtration guard does **not** eliminate the full Type-I/Type-II
branch, because valid chain-B/C witness schedules may have been discarded.

In particular, current runs using any of the following transitive stacks
cannot be promoted to a global branch refutation without rebuilding:

```text
RANK_FILTRATION_TYPE1 -> core/subcube -> facet -> ridge,
RANK_FILTRATION_TYPE2 -> two-component pin localization,
either filtration -> named-cell Hall,
Type II localization -> proposed reverse pin load.
```

This does not erase the mathematical information learned from those modules.
It invalidates only the claim that their present CNF portfolios exhaust all
hypothetical `n=465` arrays.

## 7. Required repair audit before relaunch

1. Implement the three guarded Type-II comparisons and selected-row tight
   flag.
2. Implement the three guarded Type-I equalities.
3. Correct chain-B/C in `NamedCellFamilyPlan::add_width_rows`.
4. Replace the two stale checkers by full chain-population enumeration, not
   free `h1,h6` pairs.
5. Recompute every affected module inventory and complete-build inventory;
   the old Type-I `2,341/17,354`, Type-II `9,814/47,310`, and named-cell
   totals will change.
6. Recheck absent/explicit-zero clause-stream identity and every guard
   prerequisite failure.
7. Reaudit the exact-one chain selector, retained carries, and guarded prefix
   comparators at source level.
8. Only then integrate the reverse occurrence-bank refactor and verify its
   `15,945/96,149` delta independently.

## 8. Independent regression checker

Run

```text
python3 scratch/audit_k11_rank5_zero_state_dependency.py
```

It exhausts all small seven-state population vectors, verifies the three
`y0/y2` formulas and invariant, checks both concrete `k=11` endpoint
profiles and the joint scalar cuts, verifies every corrected named-cell row,
recomputes the optimized reverse inventory, and confirms that the stale
source formulas are still present.  Its current output is

```text
all three y0/y2 chain formulas and invariant: PASS
Type-II state-22 two-component counterprofile: PASS
Type-I state-11 boundary-core counterprofile: PASS
corrected stability/equality/named-cell rows: PASS
optimized reverse inventory 15945/96149: PASS
current production stale formulas: DETECTED (expected; no edit made)
```

This audit is the authoritative status correction for the affected `k=11`
search stack.  It establishes neither SAT nor UNSAT.
