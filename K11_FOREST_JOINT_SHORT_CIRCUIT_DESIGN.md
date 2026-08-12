# Exact compact CNF design for the new `k=11` joint band cuts

## Status

This note gives a simpler exact circuit for the inequalities proved in
`K11_FOREST_JOINT_SHORT_BAND_CUTS.md`.  It avoids selecting one of the four
maximal rank-five state chains.  It is a design only: the production solver is
unchanged until this circuit receives an independent source-level audit.

The intended future guard is

```text
K11_FOREST_JOINT_BAND_CUTS=1
```

and it should require the already-audited rank-six `BandCutPlan`, whose binary
boundaries are denoted `b1,...,b6` below.

## 1. Exact per-slot width indicators

The rank-five row has exactly one of ten state variables true at every slot.
State `03` is already forbidden.  Define

```text
Y0[i] iff state[i] is one of 00,11,22,33,
Y2[i] iff state[i] is one of 02,13.
```

Because the ten state variables are exact-one, each definition needs only

```text
state -> Y       for every listed state,
Y -> OR(listed states).
```

Thus the 462 slots use 924 variables and

```text
462*(5+3)=3,696 clauses.
```

The exact profile counts are

\[
 y_0=\sum_iY0_i,
 \qquad
 y_2=\sum_iY2_i.                                    \tag{1}
\]

No maximal-chain case split is needed.

## 2. Exact nine-bit sequential increment counters

For either indicator word, start from the nine-bit value zero and process its
462 literals in order.  At one step, let `c_0=Y[i]`; for bits `j=0,...,8`, set

```text
out[j]     = in[j] XOR c[j],
c[j+1]     = in[j] AND c[j]       (only for j<8).
```

An XOR uses four clauses and an AND uses three.  The final carry after bit
eight is unnecessary: at most 462 unit increments occur, strictly below
`2^9=512`, so modular and ordinary nine-bit addition agree.

Reusing the fixed-false literal already present in `BandCutPlan` for the
initial nine input bits, one counter allocates per step nine output bits and
eight internal carries.  The two counters therefore add

```text
variables = 2*462*(9+8) = 15,708
clauses   = 2*462*(9*4+8*3) = 55,440.
```

Together with the width indicators, the exact count extraction costs

```text
16,632 variables
59,136 clauses.
```

Every auxiliary is functionally determined by the rank-five schedule.  The
counter is therefore exact in both directions, not merely a one-sided
cardinality bound.

## 3. Comparisons against the rank-six boundaries

The existing rank-six chain gives

\[
 x_0=b_1+462-b_6,
 \quad
 x_0+x_1=b_2+462-b_5,
 \quad
 x_3=b_4-b_3.                                      \tag{2}

The new theorems are encoded by the following unsigned comparisons:

```text
# x0 <= 1 (strengthens the current x0 <= 3 comparator)
b1 + 461 <= b6

# y0 + x0 <= 135
y0 + b1 + 327 <= b6

# y2 >= y0 + 87 + 4*x0
y0 + 4*b1 + 1935 <= y2 + 4*b6

# x0+x1 <= y0+3
b2 + 459 <= b5 + y0

# y2 <= x3+3
y2 + b3 <= b4 + 3.
```

The third line is just

\[
 y_0+87+4(b_1+462-b_6)\le y_2
\]

with negative terms moved to the other side.  Multiplication by four is a
two-bit shift, so no multiplier is required.

All values fit in twelve unsigned bits.  The exact ripple adders and
most-significant-first comparator already audited in `BandCutPlan` can be
reused verbatim.  The independent short-pool inequality and the total-width
455 corollary need not be encoded: they follow algebraically from the five
displayed comparisons and remain useful regression assertions.

The arithmetic layer should add only a few hundred variables and a few
thousand clauses; its exact inventory must be frozen from the implementation,
then independently reconstructed, rather than guessed in this design note.

## 4. Exactness argument

The state definitions and increment circuits compute the literal profile
counts (1).  Equations (2) are exact identities of the existing rank-six
boundary selectors.  Each displayed comparator is algebraically equivalent
to one of the globally necessary inequalities proved in the companion note.
Therefore every genuine universal length-465 array extends to a satisfying
assignment of the circuit.

Conversely, the circuit adds only necessary comparisons to the existing exact
forest formula.  It cannot create a spurious array model, and the functional
counter auxiliaries cannot choose false profile values.  Enabling the future
guard will therefore preserve satisfiability if and only if `nu(11)=465`.

## 5. Required implementation audit

Before deployment:

1. keep guard-off clause generation byte-for-byte unchanged;
2. independently enumerate all 462-step counter values and truth-table-check
   the XOR/AND CNF templates;
3. compare every arithmetic comparator against direct integer evaluation on
   exhaustive feasible profile triples `(x,y)` and randomized block-boundary
   schedules;
4. reproduce the complete variable/clause inventory in a real CaDiCaL
   build-only run;
5. preserve the usual SAT double-verification and UNSAT proof requirements.

The companion checker already validates the profile algebra on 300,000
deterministic boundary cases:

```text
scratch/verify_k11_forest_joint_short_cuts.cpp
```

It does not yet validate the unimplemented CNF circuit.
