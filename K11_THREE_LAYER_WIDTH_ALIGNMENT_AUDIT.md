# Audit of `K11_THREE_LAYER_WIDTH_ALIGNMENT.md`

## Verdict

**PASS.**  The endpoint-omission inequalities, named three-layer capacity,
and rank-seven truncated-width moments are valid for every hypothetical length-465
word.  The exact scalar consequences are

```text
Type II: T7=sum min(w7,4)>=930,
Type I:  T7=sum min(w7,4)>=940.
```

The exhaustive checker confirms that both constants are tight in the current
integer-profile relaxation, so the note correctly claims a propagation cut
rather than a contradiction.

## Checks

1. Each central endpoint set has deficit three.  Hence
   `d_L,d_R<=3`.  A rank-seven endpoint can miss the rank-six endpoint set
   only at one of its three omitted positions, giving `e_L,e_R<=3`.
2. At a shared endpoint, unequal-rank witness intervals are strictly nested
   in rank order.  This proves the two cumulative inequalities without a
   fixed-row or connected-path assumption.
3. A rank-seven endpoint outside the common rank-five/rank-six set is either
   outside rank six or in `E6\E5`, proving the loss budget `d+e` in the named
   three-layer row.
4. Rank filtration gives no literal rank-seven entry, so `z0=0`.  The
   containment-blocker deadline gives the additional full-width cap ten, but
   is not needed for the four-truncated consequence.
5. The first four terms of the tail-sum identity are exactly `T7`, not merely
   a lower estimate for `W7`.  Splitting at `x3=132+e` therefore reproduces
   the stronger `T7>=945-3e+3x0-2q`.  The Type-I boundary row similarly gives
   `T7>=952-3e-q`.

The checker

```text
scratch/check_k11_three_layer_width_alignment.cpp
```

enumerates all central integer width profiles satisfying the audited fan,
endpoint, alignment, total-width, and branch-sensitive short-pool rows.  For
every `e,q in {0,1,2,3}` it exactly reproduces the parameterized formulas,
including the infeasibility of `q=0` when `x0=1`.  It also includes the
Type-I named-cell row `y2>=96+y0`.  The displayed Type-II equality profile is
assigned to the one-component/no-duplicate subcase; the conditional
two-component and duplicate rows are therefore not silently discarded.

Compile and run with

```text
g++ -O3 -std=c++20 scratch/check_k11_three_layer_width_alignment.cpp \
  -o /tmp/check_k11_three_layer_width_alignment
/tmp/check_k11_three_layer_width_alignment
```

The expected output is

```text
PASS: exact three-layer truncated-width-profile minima
Type II minimum T7=930; Type I minimum T7=940
```

## Relation to existing cuts

* The rank-seven full-width cap is available when
  `K11_FOREST_CONTAINMENT_CAPS=1` is enabled, but the truncated moment does
  not require that guard.
* The rank-five/rank-six cumulative row is the exact per-side refinement of
  the previously recorded component-defect inequality.
* The rank-six/rank-seven endpoint existence is implicit in the audited
  adjacent-shadow theorem, but neither its width-profile cumulative form nor
  the `T7` moment was previously a production scalar cut.
* The named `H2/H3` rows retain physical endpoint information and are not
  recovered from profile totals alone.  After names are projected away,
  their scalar forms are redundant.

The preferred production projection uses virtual inactive credit four and
three crossed-width thresholds, giving deficit bounds 390 in Type II and 380
in Type I.  The former nine-threshold, credit-nine full-width projection is
valid but superseded.  The alternative named low-width endpoint clauses are
profile-redundant but may offer different propagation.  Neither changes the
current mathematical bound.
