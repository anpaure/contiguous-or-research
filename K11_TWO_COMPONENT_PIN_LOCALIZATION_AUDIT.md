# Adversarial audit of the two-component pin-localization theorem

## Verdict

**PASS, with one corrected nonredundancy witness.**  The literal-family
localization and all numerical deficit bounds in
`K11_TWO_COMPONENT_PIN_LOCALIZATION.md` follow from the already audited
Type-II two-component structure.  The production
`TypeIITwoComponentPinPlan` is an exact guarded encoding of those
consequences.  The result is necessary, not sufficient, and applies only
after a slack-one/slack-two orientation has been selected.

## 1. Witness-choice dependence

In the two-component branch, choose one witness for every nonliteral
five-set.  If `q_i` witnesses are assigned to a component of length `n_i`,
then `t_i=n_i-q_i` is positive.  The total slack is three, so the two slacks
are `{1,2}` for every fixed valid witness choice.

The theorem orients the names using one such choice.  It does not assert that
a component has the same slack under every possible choice.  This is enough
for a SAT specialization: the existing Type-II plan already existentially
selects a component whose internal adjacent pairs occur in the selected
rank-five row, which is exactly the slack-one certificate used by the proof.

## 2. Why lower targets cannot escape the two components

Every position outside the two low components is a literal rank-five entry.
An interval with OR-rank at most four cannot contain such a position.  Hence
every lower witness lies wholly in one of the two components.

If `S` meets `D_2`, then `S` is not contained in `V_2`.  Every interval in
`C_2` has OR contained in `V_2`, so no such interval represents `S`.
Universality therefore forces a witness in `C_1`.

## 3. Why representation in the slack-one component means literal

For a component of length `n_1` containing `q_1=n_1-1` selected incomparable
rank-five witnesses, ordered-antichain containment puts every selected
witness in a singleton or adjacent pair.  Singletons are impossible because
all component entries have rank at most four.  There are exactly `n_1-1`
adjacent pairs, so every adjacent pair is a selected rank-five witness.

Every interval of length at least two contains an adjacent pair and hence has
rank at least five.  A rank-at-most-four target represented in `C_1` must
therefore use a singleton interval.  This validates the literal conclusion;
it is stronger than component eligibility alone.

## 4. Counting literal values

For a deficit of size `d`, the number of rank-`s` masks meeting the deficit is

\[
 \binom{11}{s}-\binom{11-d}{s}.
\]

One position cannot be literally equal to two different masks, so these
targets require distinct physical entries.  Summing over ranks one through
four gives `Phi(1)=176`, `Phi(2)=306`, and `Phi(3)=399`.

There is no multiplicity loophole: repeated occurrences would use still more
positions, while the proof only asks for one occurrence of each required
value.

## 5. The component-length upper bound

All literal five-set occurrences are distinct in the two-component branch;
thus their number `z` is both a position count and a distinct-value count.
The selected nonliteral rank-five counts satisfy

\[
q_1+q_2=462-z.
\]

The two component capacities are `q_1+1` and `2q_2+3`.  Since 561 lower
targets must fit,

\[
561\le q_1+1+2q_2+3=466-z+q_2,
\]

so `q_2>=95+z`.  Therefore

\[
n_1=465-z-(q_2+2)\le368-2z.
\]

Two components require at least one intervening literal rank-five position,
so `z>=1` and `n_1<=366`.  This excludes deficit three because `399>366`.
The same comparison gives the thresholds 31 and 96 without rounding loss.

## 6. Nonredundancy and scope

The original draft profile `v_2=8,q_2=96` was too coarse: 96 distinct
rank-five targets cannot be contained in eight coordinates, because
`C(8,5)=56`.  This has been corrected in the theorem note and checker.

In fact, natural rank-five component eligibility gives

\[
 q_2\le\binom{|V_2|}{5}.
\]

Together with `q_2>=95+z`, this independently proves `|V_2|>=9`, and
`|V_2|=9` forces `z<=31`.  Thus `d<=2` and
`z>=32 => d<=1` are not new once this otherwise unmaterialized rank-five
component support count is retained.

The corrected abstract profile

\[
 z=97,\quad(q_1,q_2)=(173,192),\quad(n_1,n_2)=(174,194),
 \quad(|V_1|,|V_2|)=(11,10)
\]

passes physical capacity, separate coordinate eligibility, and natural
rank-five eligibility (`192<=C(10,5)=252`).  Nevertheless its coupled lower
capacity is

\[
 \min(174,561)+\min(387,385)=559<561.
\]

This valid summary profile shows that the genuinely new numerical row is
`z>=97 => D_2=empty`.  The four rank-by-rank literal rows contain additional
information not present in any scalar rank-five support cap.

As with every valid strengthening of a SAT encoding of the original problem,
the complete base formula semantically implies the theorem.  “Nonredundant”
therefore does not mean logical independence from the full CNF.  It means
that the currently exposed component summaries do not materialize the
`q_2`/support or lower-target localization consequences for propagation.

No claim is made about the deficit of the slack-one component when the
slack-two component is coordinate-complete.  The direction of the theorem is
essential.

## 7. Finite and circuit checker

The command

```text
python3 scratch/check_k11_two_component_pin_localization.py
```

passes.  It independently verifies the binomial tables, the corrected
strictness profile, and the complete integer-profile threshold table.  It
also exhausts the selected-component and conjunction gates, the coordinate
OR bank through four positions, all 32 full-adder assignments, and every
nine-bit input to all conditional constant comparators.  Its independent
Wallace calculation gives 922 variables and 6,454 clauses for one exact
465-input counter.

The archived exact words through `k=9` have no two-component
`{1,2}`-slack instance, so their check is vacuous and is reported as such
rather than presented as experimental confirmation.

## 8. Production-plan audit

The guarded `TypeIITwoComponentPinPlan` in `k11_forest_sat.cpp` is sound.

* Two exact selected-component banks orient the existing first/second low
  memberships by the exact-one slack selector.  They are false outside the
  two-component branch.
* For every coordinate, 465 conjunctions and one reverse OR clause define
  its occurrence in the slack-two component in both directions.
* The 165 triple clauses are exactly `|D_2|<=2`.  Conditional comparisons
  enforce `z<=96` for every missing coordinate and `z<=31` for every missing
  coordinate pair.
* Four exact counters count literal ranks one through four in the selected
  slack-one component.  The conditional lower comparisons are precisely the
  two rows `(1,10,45,120)` and `(2,19,81,204)`.

No target-name variable is guessed, every auxiliary gate is bidirectional,
and every new substantive clause is escaped outside `two_components`.

The independently recomputed inventory is

```text
membership                 930 variables /  4,650 clauses
coordinate union         5,126 variables / 20,471 clauses
deficit clauses              0 variables /    165 clauses
z thresholds                 0 variables /    297 clauses
four exact rank counters  5,548 variables / 31,396 clauses
rank-vector rows             0 variables /    726 clauses
----------------------------------------------------------------
total                    11,604 variables / 57,705 clauses
```

A build through the local CaDiCaL hash stub reports those exact subtotals.
With the guard absent and with it explicitly set to zero, the complete stderr
streams are byte-identical and both end in

```text
CLAUSE_STREAM_FNV64=451f2f5d3b18094d ADD_CALLS=56875968.
```

The enabled minimal-prerequisite build adds exactly 11,604 variables and
57,705 clauses.  The current full Type-II guard set builds at

```text
3,657,075 variables / 19,601,762 clauses.
```

## 9. Smaller safe implementation option

The production plan is exact and reasonably compact, but not the smallest
possible reuse of the existing Type-II state.  If rebuilding it is useful,
retain the already allocated coordinate-complete selector and its
`chosen_low` membership bank.  Introduce one flag saying that this selected
complete component is also the selected slack-one component.  Only in that
case can the other component have a nonzero slack-two deficit; otherwise the
slack-two component is already the encoded complete component.

Define the other membership by `low AND NOT chosen_low`, use one deterministic
coordinate-prefix bank for its eleven union bits, and count ranks inside the
already existing `chosen_low` bank.  Direct clauses for the three numerical
rows use the existing `z<=134` fact:

* 165 clauses for deficit at most two;
* `3*C(11,2)=165` clauses for `z>=32 => d<=1`, using count bits 5, 6, 7;
* 66 clauses for `z>=97 => d=0`, since below 128 this is
  `bit6 AND bit5 AND OR(bits0..4)`, while bit7 covers 128--134.

Including the same four exact rank counters and 726 rank-row clauses, this
full-strength variant costs exactly

```text
11,129 variables / 54,367 clauses,
```

provided the existing complete selector and `chosen_low` vector are exposed
as fields rather than reallocated.  It saves 475 variables and 3,338 clauses.
The current 11,604/57,705 plan is nevertheless fully safe; this is an
implementation-size recommendation, not a correctness objection.
