# Repair audit for the rank-five singleton boundary equations

## Verdict

The current production source is **not satisfiability-complete** for either
rank-filtration branch.  Both `RankFiltrationTypeIIPlan` and
`RankFiltrationTypeIPlan` use

```text
y0 = 462+h1-h6,
```

as though it held on every allowed rank-five state chain.  It holds only on
chain A.  Chains B and C have an additional internal width-zero block:

```text
A = 00 01 02 12 13 23 33
B = 00 01 02 12 22 23 33
C = 00 01 11 12 13 23 33.
```

The exact formulas were already proved and independently checked in
`K11_FOREST_JOINT_SHORT_BAND_CUTS.md` and
`K11_FOREST_JOINT_BAND_IMPLEMENTATION_AUDIT.md`:

| chain | exact `y0` | exact `y2` |
|---|---|---|
| A | `462+h1-h6` | `h3+h5-h2-h4` |
| B | `462+h1+h5-h4-h6` | `h3-h2` |
| C | `462+h1+h3-h2-h6` | `h5-h4` |

Here `y0` is the number of selected rank-five singleton witnesses and `y2`
is the number of selected rank-five witnesses of physical width two.

No theorem in the project makes chain A globally WLOG.  Reversal fixes A and
exchanges B with C.  It cannot remove a nonempty `11` or `22` block.  Thus
the A-only equations at current source lines 1386--1400 and 1979--1984 are a
soundness defect, not a harmless loss of propagation.

The production source hash audited here is

```text
bb42caaee3c5adfc511ed8171a80944889020a4b0a3869069baeb90141034cc3
  k11_forest_sat.cpp
```

No production source was changed during this audit.

## 1. Why chain A is not WLOG

The four possible width-zero rank-five states are `00,11,22,33`.  Unlike the
rank-six schedule, the rank-five schedule does not contain state `03`.
Therefore the rank-six argument that makes `11` and `22` incomparable with a
forced `03` does not apply.  The joint-band theorem deliberately retains B
and C for exactly this reason.

More formally, coordinate permutations act trivially on endpoint states,
while physical reversal acts by

```text
(alpha,beta) -> (3-beta,3-alpha).
```

This involution fixes chain A setwise and exchanges B with C (`22` maps to
`11`).  Hence the full proved symmetry group has two chain orbits,
`{A}` and `{B,C}`.  It can reduce B/C to one orientation, but it cannot make
chain A exhaustive.  No separate witness-reselection theorem eliminating
the internal diagonal block appears in the handoff or its audits.

There is also a concrete endpoint-profile witness that the existing
prerequisites do not eliminate the internal plateau.  On chain B take the
seven block lengths

```text
(20,50,200,50,1,62,79).
```

They sum to 462 and give

```text
(h1,h2,h3,h4,h5,h6)=(20,70,270,320,321,383),
(y0,y1,y2)=(100,162,200).
```

The A-only proxy is only

```text
462+h1-h6=99;
```

the missing unit is the nonempty `22` block `[h4,h5)`.  The reversed profile
is a chain-C profile with a one-slot `11` block.  For example the rank-six
width profile

```text
(x0,x1,x2,x3)=(0,0,259,203)
```

satisfies every generating joint-width row:

```text
x0<=1,
y0+x0<=135,
y1+2*y2>=549+4*x0,
x0+x1<=y0+3,
x0+x1+x2<=y0+y1+3,
y2<=x3+3.
```

The state sequence itself is a valid monotone endpoint schedule: slot `i`
uses `[i+alpha_i,i+beta_i]`, so all selected left and right endpoints are
strictly increasing and lie in the 465-position triangle.  This example is
not asserted to be a complete OR array.  Its purpose is sharper: it proves
that the already encoded endpoint and scalar theorems do not imply chain A.
An A-only restriction would require a new array-level theorem.

The defect can reject profiles allowed by the actual rank-filtration
theorem.  With the B profile above:

* Type II may have `n5=101` and one low component.  The true values are
  `delta=n5-y0=1` and `delta+s=2`; the production proxy gives
  `n5-99+1=3` and rejects it.
* Type I may have `n5=y0=100`, exactly as duplicate-freeness requires; the
  production equality instead demands `n5=99` and rejects it.

## 2. Exact repaired stability equations

Reselect, WLOG, one singleton witness for every distinct literal rank-five
value.  Then

```text
delta5 = n5-y0.
```

### Type II

If `s` is the number of physical rank-at-most-four components, the theorem is

```text
n5-y0+s <= 2.
```

After substituting the selected chain's exact `y0`, the three guarded rows
are

```text
A: n5+h6+s       <= h1+464,
B: n5+h4+h6+s    <= h1+h5+464,
C: n5+h2+h6+s    <= h1+h3+464.
```

The exact tightness flag must refer to equality in the selected one of these
three rows.  Equivalently, after materializing `y0`, compare

```text
n5+s == y0+2.
```

The existing logical identity then remains valid:

```text
duplicate_flag <-> stability_tight AND !two_components.
```

Indeed the feasible `(delta5,s)` cases remain `(0,1),(1,1),(0,2)`.

The current flag instead tests `delta5+s+p=2`, where

```text
p = h5-h4 on B,
p = h3-h2 on C.
```

For instance `(delta5,s,p)=(0,1,1)` is incorrectly labeled as the duplicate
case.  This can activate the named-cell length-two cap without its theorem's
hypothesis.

### Type I

The exact theorem is `delta5=0`, hence `n5=y0`.  The three guarded equalities
are

```text
A: n5+h6       = h1+462,
B: n5+h4+h6    = h1+h5+462,
C: n5+h2+h6    = h1+h3+462.
```

The rank caps, the `n5<=133`/`n5<=134` bounds, and the component counters are
independent of this repair and remain valid.

## 3. Correct named-cell width rows

The named-cell theorem uses `z=y0`, not merely the number of `00` and `33`
states.  For a required offset `c`, the exact comparison is

```text
y2 >= c+y0.
```

Using a shared exact `y0`, the cheapest guarded boundary forms are

```text
A: h2+h4+y0+c <= h3+h5,
B: h2+y0+c    <= h3,
C: h4+y0+c    <= h5.
```

Without a shared `y0`, the equivalent direct substitutions are

```text
A: h2+h4+h1+(462+c)       <= h3+h5+h6,
B: h2+h1+h5+(462+c)       <= h3+h4+h6,
C: h4+h1+h3+(462+c)       <= h5+h2+h6.
```

The current chain-B and chain-C rows omit the internal plateau from `y0`.
They are weaker than the theorem by `h5-h4` and `h3-h2`, respectively.  In
isolation this is a loss of strength, not a false exclusion, but it must be
repaired once the upstream A-only equation no longer suppresses those
plateaux.

## 4. Recommended source design

The robust repair is to materialize the physical count once and make every
consumer use it.  Add an optional `RankFiveSingletonCountPlan`, constructed
whenever either rank-filtration branch is enabled, with one nine-bit vector
`y0`.  Reuse the joint plan's exact chain selectors and boundary bits and
encode

```text
base_left  = y0+h6,
base_right = h1+462,

A: base_left       = base_right,
B: base_left+h4    = base_right+h5,
C: base_left+h2    = base_right+h3,
```

where each equality is guarded by its exact chain selector.  Guarded bitwise
equality is sufficient; the arithmetic definitions themselves are total and
cannot restrict an inactive chain.

This centralization has three advantages:

1. Type I becomes the direct equality `n5=y0`.
2. Type II becomes the direct inequality `n5+s<=y0+2`, and its exact
   tightness flag compares those same two sums.
3. `NamedCellFamilyPlan` can encode the three short rows displayed in
   Section 3 instead of repeating signed boundary algebra.

The plan must be constructed after `JointBandCutPlan` and before either
rank-filtration plan.  `RankFiltrationTypeIPlan`,
`RankFiltrationTypeIIPlan`, and `NamedCellFamilyPlan` should receive it by
const reference.  No production chain selector should be fixed to A.

### Predicted exact inventory

The following counts are exact gate arithmetic for this design, but must be
confirmed by an independent implementation checker and build-only regression
before a new source freeze.

The shared `y0` plan uses 58 full adders, nine output bits, and 64 guarded
bit-equivalence clauses:

```text
RankFiveSingletonCountPlan: 125 variables / 876 clauses.
```

After removing the old A-only sums, the revised module inventories,
**excluding** the shared plan, are predicted to be:

| module | variables | clauses |
|---|---:|---:|
| Type-I filtration | 2,305 | 17,100 |
| Type-II filtration, duplicate flag not exposed | 9,793 | 47,164 |
| Type-II filtration, duplicate flag exposed | 9,805 | 47,218 |
| named-cell, Type I | 185 | 37,459 |
| named-cell, Type II | 377 | 38,669 |

The combined deltas relative to the current source are therefore small:

| enabled portfolio | repaired total for these plans | delta |
|---|---:|---:|
| Type I, no named cell | `2,430 / 17,976` | `+89 / +622` |
| Type II, no named cell | `9,918 / 48,040` | `+104 / +730` |
| Type I plus named cell | `2,615 / 55,435` | `+33 / +230` |
| Type II plus named cell | `10,307 / 86,763` | `-9 / -59` |

These totals include exactly one shared `125/876` plan.  The negative final
Type-II named-cell delta is possible because the shared count removes several
larger repeated boundary sums.

## 5. Downstream soundness ledger

### Directly unsound and requiring source repair

* `RankFiltrationTypeIIPlan`: its stability comparison and, when exposed,
  `stability_tight` and `duplicate_flag` use the A-only count.
* `RankFiltrationTypeIPlan`: its duplicate-free equality uses the A-only
  count.
* `NamedCellFamilyPlan`: its Type-II `short_mode` consumes the misclassified
  duplicate flag, and its B/C selected-width rows omit the internal singleton
  plateau.

The corresponding PASS verdicts are revoked in:

```text
K11_RANK_FILTRATION_ENCODING.md
K11_RANK_FILTRATION_ENCODING_AUDIT.md
K11_RANK_FILTRATION_TYPE1_ENCODING.md
K11_RANK_FILTRATION_TYPE1_ENCODING_AUDIT.md
K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING.md
K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING_AUDIT.md
K11_NAMED_CELL_FAMILY_ENCODING.md
K11_NAMED_CELL_FAMILY_ENCODING_AUDIT.md
```

The old finite checkers also encode the same A-only algebra and therefore do
not audit the repaired claim:

```text
scratch/verify_k11_rank_filtration_type1.cpp
scratch/verify_k11_rank_filtration_type2.cpp
scratch/check_k11_named_cell_family.py
```

The mathematical rank-filtration stability theorem and the abstract
named-cell theorem are not refuted.  Their translation into the selected
chain boundaries is what failed.

### Locally valid, but every current integrated CNF is upstream-poisoned

The following plans do not themselves use the false `y0` identity and can be
retained after the upstream repair:

* the Type-II component automaton, coordinate-complete-component selector,
  and slack-one adjacent-pair clauses;
* `TypeIITwoComponentPinPlan`;
* the Type-I core-subcube, canonical-prefix, facet, and ridge modules;
* residual coordinate lex, rank-seven truncated width, and the independent
  subcube run-credit circuit.

Their local theorems remain valid conditional on the true Type-I/Type-II
architecture.  Nevertheless, a CNF containing any of them together with the
current filtration plan is not a complete search of that architecture.

`K11_TYPE2_REVERSE_PIN_LOAD_IMPLEMENTATION.md` is only a design, not current
production source, and already records the correct chain-specific `y0`
formulas.  It is useful as an independent precedent for the repair.

### Search and handoff consequences

Every deployed onion portfolio in
`K11_ONION_SUBCUBE_DEPLOYMENT_20260723.md` (v1 through v7), and every later
microbenchmark based on the same Type-I/Type-II guards, searched a strict
A-biased subformula.  Therefore:

* a verified SAT candidate would still be valid;
* an UNSAT result or proof would eliminate only that restricted subformula;
* absence of a candidate, conflict counts, and relative solver speed are not
  evidence about the full Type-I or Type-II branch.

Items 1108--1111 of `MATHEMATICAL_HANDOFF.md`, their frozen inventories, and
any later statement that the two current guards form an exact exhaustive
case split require an erratum.  The unrestricted numerical bracket remains
unchanged.

## 6. Required validation before relaunch

1. Implement the shared `y0` plan without fixing a chain selector.
2. Add a standalone exhaustive arithmetic checker for all
   `0<=h1<=...<=h6<=462` and all three chains.
3. Check both directions of every guarded equality, including final carries.
4. Exhaust the logical table for `(delta5,s,plateau)` and verify the repaired
   duplicate flag against `delta5=1`.
5. Update the named-cell finite checker to use physical `y0` on B/C.
6. Recompute guard-off identity and every guarded inventory.
7. Freeze a new source hash and only then relaunch Type-I/Type-II searches.

Until those steps pass, the production filtration guards must not be used in
an UNSAT claim or described as exhaustive.
