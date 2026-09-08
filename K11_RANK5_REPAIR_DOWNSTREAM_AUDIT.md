# Downstream audit after the rank-five singleton-boundary repair

## Verdict

**PASS for the repaired dependency stack, with stale-document warnings.**

This audit was made against

```text
f86e80456f2e17fd87774579d11dd090f70f2451e888537212eb1b9613aca6e2
  k11_forest_sat.cpp
```

The current source no longer assumes that a selected rank-five singleton can
occur only in state `00` or `33`.  All three consumers of the physical
rank-five singleton count use the exact selected-chain formula:

```text
A: y0=462+h1-h6,
B: y0=462+h1+h5-h4-h6,
C: y0=462+h1+h3-h2-h6.
```

The three repaired sites are:

1. the Type-II stability comparison and its selected-row tightness flag;
2. the Type-I duplicate-free equality;
3. the Type-I/Type-II named-cell width rows.

An independent scan of every production use of `joint.bits`,
`joint.chain_selector`, and the rank-five state bank found no remaining
chain-A-only substitution.  The only source loop over width-zero states
`{0,9}` is the rank-**six** singleton indicator in `JointBandCutPlan`, where
states `11` and `22` really are excluded by the forced rank-six chain through
`03`.  It is unrelated to the repaired rank-five count.

The Type-I core-subcube, facet, ridge, Type-II component/pin-localization,
and rank-seven modules remain mathematically sound and compose with the
repaired branches.  Their local clauses did not need modification.  The
named-cell module did need, and now contains, corrected B/C arithmetic.

This is an encoding audit, not a SAT or UNSAT result.

## 1. Repaired branch facts used downstream

Choose one singleton witness for every distinct literal rank-five value.
Then

```text
delta5=n5-y0.
```

The repaired Type-II rows are, under the exact-one chain selector,

```text
A: n5+h6+s       <= h1+464,
B: n5+h4+h6+s    <= h1+h5+464,
C: n5+h2+h6+s    <= h1+h3+464.
```

Each is exactly `delta5+s<=2`.  The source defines an equality flag for each
of the three full-width integer comparisons and then makes
`stability_tight` equivalent to the equality flag of the selected chain.
Consequently

```text
duplicate_flag <-> stability_tight AND !two_components
```

again means exactly `(delta5,s)=(1,1)`.  In particular, `s=2` forces
`delta5=0` on A, B, and C, not merely on A.

The repaired Type-I equalities are

```text
A: n5+h6       = h1+462,
B: n5+h4+h6    = h1+h5+462,
C: n5+h2+h6    = h1+h3+462.
```

Each is exactly `n5=y0`, so every literal rank-five occurrence in the suffix
has a distinct value and is represented by a selected singleton witness.
The rank cap and exact one-component counter are independent of the selected
endpoint chain.

The independent implementation audit and executable checker

```text
K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md
python3 scratch/check_k11_rank5_singleton_boundary_repair.py
```

Together they exhaust all three scaled chain-population systems, all plateau
lengths, the selected-row tightness gate, the duplicate gate, and both
named-cell offsets.  The checker reports, among its PASS lines,

```text
source_sha256=f86e80456f2e17fd87774579d11dd090f70f2451e888537212eb1b9613aca6e2 PASS
active_chain_tightness_and_duplicate_truth_table=PASS
type1_type2_named_cell_chain_algebra=PASS
```

## 2. Type-I suffix-core and six-subcube module

### Verdict: unchanged and composable

The Type-I core-subcube circuit uses only these repaired-branch consequences:

* `A[0]=63` is the unique literal rank-six entry;
* every suffix entry has rank at most five;
* deleting position zero leaves the length-464 rank-at-most-five core.

It does not inspect `h1,...,h6`, `y0`, or a rank-five chain selector.  For a
six-set `U`, removal of `A[0]=63` changes the support count only for `U=63`:

```text
p_U^C=p_U       (U!=63),
p_63^C=p_63-1.
```

Therefore the existing exact correction

```text
eta(p_63-1)-gamma(p_63)
  =2*[p_63<=31]+[p_63=32]
```

remains valid on chains A, B, and C.  The local incremental inventory remains

```text
25 variables / 189 clauses,
```

inside the unchanged total Type-I subcube plan

```text
646806 variables / 4309599 clauses.
```

The independent checker still passes all charge, comparator, and production
wiring tests.

## 3. Type-I facet and ridge pin loads

### Verdict: unchanged and composable

After the repaired equality `n5=y0`, every literal rank-five position is a
distinct selected singleton.  Since the rank-at-most-four suffix positions
form one component, the exact inner peel is still

```text
P5 || C4 || Q5.
```

All nonliteral rank-five witnesses lie in `C4`; if there are `q` of them,
then `|C4|=q+2`.  This gives the same local slack-two normal form used by both
pin-load theorems.  Nothing in that argument refers to the endpoint state
through which a boundary singleton was reached.  An internal `11` or `22`
singleton simply becomes one more legitimate member of `P5` or `Q5`.

Hence the pointwise laws remain valid:

```text
#{i in C4 : A[i] subseteq R} >=20              (|R|=5),
#{i in C4 : A[i] proper-subset Q} >=10         (|Q|=4).
```

The production gates identify `C4` from exact entry ranks, not from a
boundary formula:

```text
facet[b,i] <-> support_63[i] & !A[i,b] & !rank5[i],
ridge[b,c,i] <-> facet[b,i] & !A[i,c] & !rank4[i].
```

Thus the circuits are chain-neutral once the Type-I prerequisite is exact.
Their unchanged local inventories are

```text
facet:  8304 variables /  49788 clauses,
ridge: 20760 variables / 124470 clauses.
```

Both theorem checkers and both source-aware checkers pass against the repaired
source.  A full repaired build gives the exact successive totals

```text
Type I through subcube/named/rank7: 3640731 / 19988335,
+ facet:                          3649035 / 20038123,
+ ridge:                          3669795 / 20162593.
```

The differences are exactly the two local module inventories, and the hash
stub reports `MAXVAR=DECLARED` in both builds.

## 4. Type-II component and pin-localization modules

### Verdict: local extension unchanged; repaired prerequisite restores completeness

The component automaton depends only on the exact entry-rank flags.  It
labels the first and second physical rank-at-most-four runs and makes
`two_components` equivalent to `s=2`, using the separately enforced
`s<=2`.  It contains no chain-state shortcut.

With the repaired stability row, `s=2` forces `delta5=0` on every selected
chain.  The standard slack identity therefore still gives total component
slack three, and positivity of both component slacks gives `{1,2}`.  It is
then WLOG to select every internal adjacent pair of the slack-one component
in the rank-five witness row.  The support clause enumerates all physical
rank-five states having that exact adjacent pair; it does not restrict the
global chain to A.  In fact an intervening separator can naturally occupy
the `11` or `22` singleton plateau now restored by the repair.

`TypeIITwoComponentPinPlan` uses only:

* the exact two-component flag and first/second membership banks;
* the exact slack-one selector;
* the exact literal rank-five count `n5`;
* exact entry coordinates and ranks.

It never substitutes boundary variables for `y0`.  Since `s=2` now soundly
implies `delta5=0`, its use of `z=n5` as the number of distinct literal
five-set separators is valid on A, B, and C.  The deficit rows and literal
rank-localization rows therefore remain exact.

The pin-localization module remains

```text
11604 variables / 57705 clauses.
```

The repaired Type-II filtration plan is now

```text
10032 variables / 48816 clauses     (duplicate flag not requested),
10072 variables / 49003 clauses     (duplicate flag requested by named cell).
```

The old `9814/47310` whole-plan inventory is obsolete; the unchanged
component extension is still `7440/29753` of that total.  The theorem and
pin-localization checkers pass after the repair.

## 5. Named-cell family

### Verdict: directly repaired and now composable

This was the only downstream module, besides the two filtration plans,
whose own selected-width arithmetic was affected.  Its theorem requires

```text
y2 >= offset+y0,
offset=96  in Type I and duplicate Type II,
offset=95  in two-component Type II.
```

The current source uses the correct direct substitutions:

```text
A: h2+h4+h1+(462+offset) <= h3+h5+h6,
B: h2+h1+h5+(462+offset) <= h3+h4+h6,
C: h4+h1+h3+(462+offset) <= h5+h2+h6.
```

For Type II, the branch guard is an exact conjunction of the relevant
subcase flag and the exact-one chain selector.  For Type I, it is the chain
selector itself.  All inactive comparison auxiliaries are guarded, while the
unconditional sum auxiliaries merely define arithmetic and impose no
restriction.

The corrected duplicate flag also restores the exact short-witness mode:

```text
short_mode <-> two_components OR duplicate.
```

In the optimized full formulas (66 direct targets and twelve exception
slots), the current named-cell plan inventories are

```text
Type I:  327 variables / 38451 clauses,
Type II: 661 variables / 40653 clauses.
```

The older `241/37851` and `489/39453` figures used A-only B/C substitutions
and must not be cited for the repaired source.

## 6. Rank-seven truncated-width module

### Verdict: unchanged and composable

The Type-II constant 930 uses only `x0=0`, endpoint losses at most three,
and the universal chainwise rank-five/rank-six inequalities.  Type II caps
all entries at rank five, so `x0=0` is independent of the rank-five chain.

The Type-I constant 940 uses the boundary-localized row

```text
y2>=x1+96.
```

`RankSixBranchProfilePlan` already encoded this separately on A, B, and C
using the correct formulas

```text
A: y2=(h3-h2)+(h5-h4),
B: y2=h3-h2,
C: y2=h5-h4.
```

It never used the false A-only expression for `y0`.  Therefore neither the
three-layer theorem nor its production projection changes under the repair.
The extracted production plan still has SHA-256

```text
44ca7216ff457a381c7805da36d878a39e4deae0dd34abf41f8711b40ddf8be2
```

and the independent source audit passes against the repaired whole-source
hash.  The local inventories remain

```text
Type II: 2954 variables / 475094 clauses,
Type I:  2954 variables / 475092 clauses.
```

## 7. Complete source scan for hidden A-only assumptions

Every production read of the rank-five joint boundary/state plan falls into
one of the following classes:

| consumer | status after repair |
|---|---|
| `JointBandCutPlan` | authoritative A/B/C chainwise arithmetic |
| `RankSixBranchProfilePlan` | correct A/B/C formulas for `y2` |
| endpoint-alignment summaries | enumerate all ten physical states directly |
| Type-II filtration | repaired A/B/C `y0` rows and selected-row equality |
| slack-one pair support | enumerates all ten physical states directly |
| Type-I filtration | repaired A/B/C duplicate-free equalities |
| named-cell width rows | repaired A/B/C `y0,y2` substitutions |
| base endpoint-forest clauses | enumerate all ten physical states directly |

No other production object derives rank-five width zero from only `00` and
`33`.  No chain selector is fixed to A.  Reversal is not used to discard B
or C; this is important in Type I because the fixed left endpoint makes such
a reversal especially inappropriate.

The current full build-only fingerprints relevant to composition are

```text
full Type I, no facet/ridge:
  3640731 variables / 19988335 clauses
  FNV64=c2812c85d3757e29

full Type II, with named cell, pin localization, and rank7:
  3660446 variables / 20079690 clauses
  FNV64=19f50fb16569305f
```

These are formula fingerprints only, not search conclusions.

## 8. Stale documents and checkers

### Semantically revoked until rewritten

The following documents still explicitly assert the false all-chain identity
`y0=h1+462-h6`, or certify the old source translation:

```text
K11_RANK_FILTRATION_ENCODING.md
K11_RANK_FILTRATION_ENCODING_AUDIT.md
K11_RANK_FILTRATION_TYPE1_ENCODING.md
K11_RANK_FILTRATION_TYPE1_ENCODING_AUDIT.md
K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING.md          (Section 1 and totals)
K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING_AUDIT.md    (old prerequisite/totals)
K11_NAMED_CELL_FAMILY_ENCODING.md
K11_NAMED_CELL_FAMILY_ENCODING_AUDIT.md
```

Their theorem-level statements `delta5+s<=2`, `delta5=0`, the component
extension, and the abstract named-cell theorem survive.  Their A-only source
algebra, PASS verdicts for that algebra, frozen hashes, and inventories do
not.

These old checkers also remain stale and can print PASS while testing the
superseded circuit:

```text
scratch/verify_k11_rank_filtration_type1.cpp
scratch/verify_k11_rank_filtration_type2.cpp
scratch/verify_k11_rank_filtration_type2_components.py   (old whole-plan total)
scratch/check_k11_named_cell_family.py
```

They must be replaced or clearly labeled historical.  The new repair
implementation audit and checker are authoritative for the chainwise
boundary algebra.

### Mathematically valid but with stale integrated hashes/counts

The local theorem/circuit claims in the following artifacts remain valid,
but their recorded whole-source hashes and full-portfolio inventories predate
the repair:

```text
K11_TYPE1_CORE_SUBCUBE_ENCODING.md
K11_TYPE1_CORE_SUBCUBE_ENCODING_AUDIT.md
K11_TYPE1_FACET_PIN_LOAD_IMPLEMENTATION.md
K11_TYPE1_RIDGE_PIN_LOAD_IMPLEMENTATION.md
K11_TYPE1_RIDGE_PIN_LOAD_IMPLEMENTATION_AUDIT.md
K11_TWO_COMPONENT_PIN_LOCALIZATION.md
K11_TWO_COMPONENT_PIN_LOCALIZATION_AUDIT.md
K11_RANK7_TRUNCATED_WIDTH_IMPLEMENTATION.md
K11_RANK7_TRUNCATED_WIDTH_IMPLEMENTATION_AUDIT.md
K11_ONION_SUBCUBE_DEPLOYMENT_20260723.md
MATHEMATICAL_HANDOFF.md
```

The module-local facet, ridge, pin-localization, subcube, and rank-seven
inventories remain correct; only integrated totals and old prerequisite
source hashes must be superseded.

In particular, `MATHEMATICAL_HANDOFF.md` items 1108--1111 still display the
A-only Type-I/Type-II rows and old inventories.  They cannot be used as the
current implementation ledger.

## 9. Reproducible checks performed

The following independent theorem/source checks all passed:

```text
python3 scratch/check_k11_rank5_singleton_boundary_repair.py
python3 scratch/check_k11_rank5_singleton_boundary_repair_source.py
python3 scratch/verify_k11_type1_core_subcube_encoding.py
python3 scratch/check_k11_type1_boundary_facet_pin_load.py
python3 scratch/check_k11_type1_facet_pin_load_source.py
python3 scratch/check_k11_type1_boundary_ridge_pin_load.py
python3 scratch/check_k11_type1_ridge_pin_load_source.py
python3 scratch/check_k11_two_component_pin_localization.py
python3 scratch/audit_k11_rank7_truncated_width_source.py
g++ -O2 -std=c++20 scratch/check_k11_three_layer_width_alignment.cpp \
  -o /tmp/check_k11_three_layer_width_alignment
/tmp/check_k11_three_layer_width_alignment
```

Fresh full build-only runs against the independent hash stub reproduced every
module delta quoted above, retained every final carry, and reported
`MAXVAR=DECLARED`.

## Final conclusion

The chainwise repair is sufficient for the audited downstream stack.  It
does not invalidate the Type-I core/subcube/facet/ridge mathematics, the
Type-II component/pin mathematics, or the rank-seven moment.  It repairs the
only downstream arithmetic consumer, named-cell Hall, and restores the exact
Type-II duplicate flag on which named short-mode depends.

There is no remaining chain-A-only assumption in the current production
source.  The remaining risk is documentary and evidentiary: old PASS notes,
checkers, hashes, and deployment logs still describe the poisoned pre-repair
formula and must not be cited for an exhaustive search or UNSAT claim.
