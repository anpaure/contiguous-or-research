# Exact upper-layer endpoint cuts for the unrestricted `k=11,n=465` solver

## Status

This note proves a globally-WLOG propagation cut for the existing exact direct
witnesses in ranks eight, nine, and ten.  It does not replace those witnesses
and therefore does not rely on the false assertion that two distinct
six-subsets of an eight-set must already union to the eight-set.

The cut is not yet implemented in `k11_forest_sat.cpp`.  It composes naturally
with `K11_FOREST_ADJACENT_SHADOWS=1`, because that guard already defines the
rank-six physical endpoint/length summaries needed below.

## 1. One-sided endpoint theorem

Fix a rank `s>6`, and choose one witnessing interval for every one of its

\[
 m_s={11\choose s}
\]

targets.  Their left endpoints are distinct.  The selected rank-six family
has 462 distinct left endpoints among 465 physical positions.  Consequently

\[
 |L_s\cap L_6|\ge m_s+462-465=m_s-3.              \tag{1}
\]

At every common left endpoint, the selected rank-six interval is a proper
prefix of the selected rank-`s` interval.  The reverse containment would
force an `s`-set to be a subset of a six-set, and equal physical intervals
would force unequal-rank ORs to agree.

The identical statement holds at right endpoints: all but at most three
selected rank-`s` intervals have a selected rank-six proper suffix.

Thus one may choose flags `P_S,Q_S` for each rank-`s` target such that

```text
at most 3 flags P_S are false,
at most 3 flags Q_S are false,
P_S -> the direct witness of S has a selected rank-6 proper prefix,
Q_S -> the direct witness of S has a selected rank-6 proper suffix.
```

This one-sided formulation retains more propagation than merely asserting
that all but six targets are crossed at both ends.

## 2. Forced crossed counts

Inclusion-exclusion inside the `m_s` selected targets gives at least

\[
 m_s-6                                                   \tag{2}
\]

targets with both flags.  Numerically:

| rank `s` | `m_s` | forced left | forced right | forced both |
|---:|---:|---:|---:|---:|
| 8 | 165 | 162 | 162 | 159 |
| 9 | 55 | 52 | 52 | 49 |
| 10 | 11 | 8 | 8 | 5 |

Rank eleven has only one target, so (1) supplies no positive guarantee and it
should retain its ordinary direct encoding without this cut.

## 3. Why no stronger union claim is being used

For a target with both endpoint flags, let `C,D` be the two selected rank-six
masks.  Their physical intervals are different proper prefix/suffix intervals,
and the selected rank-six row is a permutation, so `C!=D`.  Negative-bit
clauses from the direct target encoding give

\[
 C\cup D\subseteq S,
 \qquad |C\cup D|\ge7.                              \tag{3}
\]

For rank seven, (3) proves equality and is why the existing rank-seven shadow
compression needs no positive-bit occurrences.  For rank eight or above,
the union may still have only seven bits.  The current theorem deliberately
keeps every original positive-bit occurrence clause, so it remains exact
without assuming equality in (3).

Equation (3) does identify a later, optional compression: a crossed rank-`s`
target needs at most `s-7` additional bit occurrences beyond its two central
endpoint masks.  Exploiting that fact exactly requires a mux tying the chosen
physical endpoints to their selected rank-six value bits, plus a
pin-occurrence selector for the residual bits.  That replacement should be
audited separately; it is not part of this cut.

## 4. Guarded CNF cut

The current direct target already has unary thresholds `L[p],R[p]` selecting
its exact physical interval.  The adjacent-shadow option already has

```text
B[l,d] iff the selected rank-six interval beginning at l is [l,l+d],
E[r,d] iff the selected rank-six interval ending at r is [r-d,r],
```

for `0<=d<=3`.

For a left flag `P_S`, use the same local implications as the audited
rank-seven encoding:

```text
P_S and selected-left=l
    -> some B[l,d] is true,

P_S and selected-left=l and B[l,d]
    -> selected-right >= l+d+1.
```

The right flag `Q_S` gets the dual clauses.  Add a small sequential counter
for

```text
sum_S (!P_S) <= 3,
sum_S (!Q_S) <= 3
```

separately in each of ranks eight, nine, and ten.

The implications are sound because they only require certified selected
rank-six physical intervals.  For completeness, start with any universal
array and choose witnesses in rank `s`; set flags on their common endpoint
sets.  Inequality (1) satisfies the two counters, and the proper-containment
argument satisfies every guarded comparison.

Therefore adding these clauses preserves satisfiability if and only if a
universal nonzero array of length 465 exists.

## 5. Size and scope

There are only

\[
 2(165+55+11)=462
\]

new endpoint flags, plus small at-most-three sequential counters.  Reusing the
rank-six summaries, the straightforward local comparison form emits ten
endpoint/length clauses per physical position per target, or

\[
 10\cdot465\cdot(165+55+11)=1,074,150
\]

guarded local clauses before the counters.  This increases the raw clause
inventory, but it couples 231 formerly independent long-interval witnesses
to the six-component central endpoint forest.  Whether that improves CaDiCaL
enough to justify the clause cost is an empirical guarded-option question;
the mathematical cut itself is exact.

No SAT or UNSAT conclusion follows from the cut alone.  SAT output still
requires independent OR verification, and UNSAT still requires an archived
CNF/proof pair with independent proof checking.
