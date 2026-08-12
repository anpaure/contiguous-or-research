# Design: exact Type-I 2041-core and nested-loss-chain cut

> **Superseded for the residual-lex production portfolio.**  This `5/320`
> design remains a sound pre-lex arbitrary-chain encoding, but residual lex
> fixes the possible loss names to
> `63,1087,1599,1855,1983,2047`.  The current exact selector implementation
> therefore needs no loss flags or pairwise chain clauses and costs only
> `0/32`; see `K11_TYPE1_PREFIX_CHAIN_SELECTOR_COMPRESSION.md`.

## Verdict

The strongest cheap audited-but-unencoded Type-I consequence is the complete
suffix-core loss-chain theorem.  It does **not** require a second universal-
word encoding for the 464-position core.

The current formula already selects one physical witness for every target.
Under Type I, `A[0]=63`; therefore every selected witness not wholly in the
suffix core `1,...,464` is a prefix beginning at zero.  Prefix OR values form
one inclusion chain.  The entire theorem can be exposed with

```text
5 variables / 320 clauses
```

in its minimal form, or

```text
5 variables / 2801 clauses
```

with cheap propagation closure for names that cannot contain `63`.

No production source edit is made in this design note.

## 1. Exact mathematical normal form

The Type-I branch fixes

\[
 A_0=T=63=\{0,1,2,3,4,5\}
\]

as the unique literal six-set.  Its core is the suffix

\[
 C=(A_1,\ldots,A_{464}).
\]

An interval witness lies outside `C` exactly when it contains position zero;
such an interval is necessarily a prefix `[0,j]`.  Hence all target values
whose chosen witnesses are outside `C` are nested.

Moreover, a prefix value must contain `T`.  Writing the five outside
coordinates as `E={6,7,8,9,10}`, the only possible values are

\[
 T\cup X,\qquad X\subseteq E.
\]

Their numbers in ranks six through eleven are

```text
1, 5, 10, 10, 5, 1.
```

The rank-six member is the fixed endpoint value.  Thus only 31 nonfixed
target names can possibly need an endpoint-prefix witness.  Pairwise
comparability of their outside subsets is equivalent to being one chain.
There are exactly 285 incomparable unordered pairs among these 31 names.

Forcing every selected noncore target name into this chain gives at most one
exception in each rank seven through eleven.  Together with the fixed
rank-six endpoint, the selected core witnesses certify at least

\[
 1023+461+329+164+54+10=2041
\]

different nonempty masks wholly inside the suffix core.  This is exactly the
audited boundary--core theorem, now attached to concrete selected-witness
variables.

## 2. Existing variables in ranks eight through eleven

Targets in ranks eight through eleven remain `DirectTarget` records in the
production adjacent/rank-three formula.  For a direct target `S`,

```text
item.M0
```

is the exact literal saying position zero belongs to its chosen witness.
Use that existing literal as the exception flag

\[
 e_S=[0\in I_S].
\]

No new variable is needed.  If `S` does not contain `63`, the base target
clauses and fixed endpoint already force `e_S=false`.  The only live direct
flags therefore correspond to the `10+10+5+1=26` masks containing `63`.

## 3. Five rank-seven exemption flags

Rank seven is represented by the adjacent-shadow compression rather than a
`DirectTarget`.  A target can be covered by:

* `rank_seven_shadow[column].active`, with interval-membership literal
  `rank_seven_shadow[column].M0`; or
* one of the six generic slots, using
  `exception_seven[slot].q[column]` and
  `exception_seven[slot].M0`.

Only the five targets

\[
 63\cup\{b\},\qquad b=6,\ldots,10,
\]

can have a noncore rank-seven witness.  Allocate one exemption variable
`e_b` for each.

For its column add the seven clauses

```text
 e_b OR !active          OR !active_inside_0
 e_b OR !slot_q[column]  OR !slot_inside_0   (six slots).
```

If `e_b=false`, every selected mechanism for that target is core-contained;
the existing rank-seven coverage clause guarantees that at least one such
mechanism exists.  If `e_b=true`, the target is one of the permitted chain
exceptions.

These are satisfiability-preserving witness-selection clauses.  Given a
Type-I word, choose core witnesses for every core-present target.  The only
targets without such a witness are the actual endpoint loss chain, so the
five exemption variables can be set accordingly.  Artificial generic-slot
fillers may duplicate any core-present target using core witnesses, because
their interval variables are independent.

## 4. Named-target competition

Form the 31 pairs

```text
(target mask, exception literal)
```

from:

* the five fresh rank-seven exemptions; and
* the 26 existing `DirectTarget::M0` literals in ranks eight through eleven.

For every pair of incomparable target masks `S,T`, add

```text
!e_S OR !e_T.
```

There are exactly 285 such clauses.  They include all same-rank at-most-one
constraints and all cross-rank failures of nesting.  A family with no
incomparable pair is a chain, so no separate cardinality counter or chain
selector is needed.

The minimal exact inventory is therefore

| component | variables | clauses |
|---|---:|---:|
| five rank-seven exemptions | 5 | 0 |
| gate seven mechanisms for each exemption | 0 | 35 |
| incomparable named-target pairs | 0 | 285 |
| **total** | **5** | **320** |

## 5. Optional propagation closure

The base CNF already implies that a witness containing position zero must
have a target containing `63`.  If this implication is worth exposing
directly, add:

* seven binary clauses for each of the other 325 rank-seven target names,
  forbidding a noncore active or generic-slot mechanism: `2,275` clauses;
* a unit `!item.M0` for every noncandidate direct target in ranks 8--11:
  `155+45+6=206` clauses.

This produces the propagation-closed inventory

```text
5 variables / 2801 clauses.
```

It is logically equivalent to the minimal version in the fixed Type-I base
formula.  The minimal `5/320` version should be tried first; the larger form
is useful only if solver statistics show that the existing target-cardinality
clauses discover the same conflicts too late.

## 6. Exact production dependencies

The proposed guard should require:

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_ADJACENT_SHADOWS=1
```

Type I already requires the exact branch-one, band, joint-band, and local-
density prerequisites.  Branch one supplies `A[0]=63` and the unique rank-six
endpoint.  Adjacent shadows supply the rank-seven active records and six
generic slots.  Ranks eight through eleven use the always-present direct
records.

No containment-cap or subcube-deficiency guard is mathematically required.
The cut composes with both.  It should be rejected in Type II and in portal
formulas whose target structures differ.

A convenient implementation is a small `TypeICoreChainPlan`, constructed
after the direct, rank-seven-shadow, and exception-slot allocations.  It
needs references only to

```text
vector<DirectTarget> direct
vector<int> rank_seven_masks
vector<RankSevenShadow> rank_seven_shadow
vector<ExceptionSlot> exception_seven.
```

## 7. Exactness audit

### Soundness

In a satisfying assignment, every target outside the 31 candidate names has
a selected core witness.  Among the candidates, every target not exempted
also has a selected core witness.  The exempted names are pairwise comparable
and therefore form one chain with at most one name at each rank.  Including
the fixed endpoint six-set, at most six targets lack a selected core witness,
so at least 2041 actual target values occur in the core.

### Completeness

Given any Type-I universal word, choose a core witness for every target that
occurs in the core.  The boundary--core theorem says the remaining targets
form one nested prefix chain beginning with `63`, with at most one target per
rank.  Use those rank-seven names as the fresh exemptions and choose the
corresponding direct prefix witnesses in higher ranks.  All 285 competition
clauses hold.  The adjacent-shadow exception slots may be reselected
independently, so filler slots can use core witnesses and introduce no extra
exception name.

Thus the plan is globally WLOG inside Type I; it is not a construction ansatz.

## 8. Finite checker

The independent script

```text
python3 scratch/check_k11_type1_core_chain_design.py
```

enumerates all 31 candidate names and all 285 incomparable pairs, recomputes
the maximum chain length and the 2041 rankwise coverage, and verifies both
inventories.  It reports

```text
candidate rows 1,5,10,10,5,1: PASS
31 nonfixed prefix targets, 285 incomparable pairs: PASS
nested exception chain has at most five nonfixed targets: PASS
suffix-core coverage 2041: PASS
minimal design: 5 variables / 320 clauses
propagation-closed design: 5 variables / 2801 clauses
```

## 9. Comparison with laminar pin-capacity cuts

The current Type-I filtration already makes the rank-at-most-four suffix
positions one component and fixes the rank-five duplicate excess to zero.
At that level, the general laminar Hall theorem largely collapses to the
already encoded coordinate-complete-core facts; no smaller nonredundant
`k=11` Hall specialization is presently evident.

The named-target chain cut above is therefore preferable: it is exact,
branch-specific, directly reuses physical witness cells, and costs only 320
clauses.  More detailed complement-rectangle or first-occurrence ordering
can be layered on its 31 exposed flags later if solver profiling shows a
remaining endpoint-prefix bottleneck.
