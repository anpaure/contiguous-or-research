# K16 upper-complete facet carrier: exact P/Q area--chain tradeoff

**Date:** 2026-07-31  
**Status:** exact solver-free fixed-order no-go; carrier-order rethread remains live

## 1. Result

Fix the authenticated two-reversal carrier

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43
```

It is a permutation of all `12870` rank-eight masks, its adjacent Johnson
colours cover all `11440` rank-nine masks, and every upper target of ranks
`9..16` occurs as a carrier interval.  Its unconstrained three-hole P/Q
schedule has scalar lower capacity `27588+9=27597>26332`.

Scalar capacity is nevertheless insufficient.

> **Theorem 1 (complete fixed-order no-go).**  No realizable three-start-hole,
> three-deadline-hole P/Q schedule for this fixed rank-eight order can supply
> both
>
> 1. enough proper-prefix cells to cover all `26332` lower targets, and
> 2. enough positive-depth start chains to cover the `11440` rank-seven
>    targets.
>
> Consequently no length-`12873` universal word can induce this fixed
> distinct-middle order.

The complete terminal Pareto frontier, with coordinates

```text
(selected proper-prefix area, positive selected starts),
```

is exactly

```text
(27588, 10939)
(22766, 11828)
(12578, 12577).
```

Even after granting the three omitted starts their maximum possible
contributions, the necessary thresholds are

```text
selected area             >= 26332 - 9 = 26323,
positive selected starts  >= 11440 - 3 = 11437.
```

No frontier point lies in this northeast quadrant.

This closes the proposed K-best/beam search over alternative P/Q schedules
for this **same order**.  The live next move must change the carrier order or
its endpoints while retaining q1 and all-upper coverage.

## 2. The rank-seven chain lemma

Consider one physical start position `p`.  Its proper-prefix interval ORs are

\[
 A_p,
 \quad A_p\cup A_{p+1},
 \quad A_p\cup A_{p+1}\cup A_{p+2},
\]

up to the first selected rank-eight deadline.  They form a nested chain.

### Lemma 2.1

One physical start can realize at most one distinct rank-seven target.

### Proof

Two members of the prefix family are comparable by inclusion.  Distinct
rank-seven subsets are never comparable: if `S subseteq T` and
`|S|=|T|=7`, then `S=T`.  Hence a single nested start chain contains at most
one distinct rank-seven mask.  \(\square\)

A selected start with span zero has no proper lower prefix and contributes no
rank-seven chain.  Thus a schedule with `c` positive selected spans supplies
at most `c` rank-seven occurrences from its selected starts.  We additionally
credit each of the three omitted starts with one rank-seven occurrence,
whether or not a literal completion can attain it.  Since

\[
 {16\choose7}=11440,
\]

the necessary inequality is

\[
 c+3\ge11440,
 \qquad\text{or equivalently}\qquad c\ge11437.       \tag{2.1}
\]

This lemma uses no maximal-envelope or Hall approximation.

## 3. The total lower-area inequality

Let the selected starts and deadlines be

\[
 p_0<\cdots<p_{W-1},\qquad q_0<\cdots<q_{W-1}.
\]

The selected start `p_i` has exactly `q_i-p_i` proper-prefix cells.  Therefore
the total selected lower-cell count is

\[
 A=\sum_i(q_i-p_i).                                  \tag{3.1}
\]

At equality the three omitted starts have depth at most three.  Granting all
three the full three cells gives the optimistic upper bound `A+9`.  Covering
all nonempty targets of ranks one through seven requires

\[
 A+9\ge\sum_{j=1}^7{16\choose j}=26332,
\]

so

\[
 A\ge26323.                                          \tag{3.2}
\]

The omitted-start credits in (2.1) and (3.2) are deliberately independent
and optimistic.  Any literal coupling can only make the obstruction stronger.

## 4. Exact two-objective P/Q recurrence

Scan physical positions `j=0,...,12872`.  A streaming state is

```text
(x, y, Q),
```

where `x,y` are the numbers of used start and deadline holes and `Q` is the
ordered queue of accumulated maximal-envelope ORs for active middle rows.
This is the same exact state used by the audited scalar P/Q dynamic program.

For transition bits

```text
sx = 1[j is a start hole],
dy = 1[j is a deadline hole],
```

the area increment is the identity

\[
 j(sx-dy),                                           \tag{4.1}
\]

because at termination

\[
 \sum_i(q_i-p_i)=\sum X-\sum Y.
\]

If `sx=0`, a selected row starts at `j`.  It has positive depth unless it is
immediately ended at the same position.  Immediate ending occurs exactly
when the incoming active queue is empty and `dy=0`.  Hence the positive-chain
increment is

\[
 \mathbf1\{sx=0\}\,
 \mathbf1\{|Q|>0\text{ or }dy=1\}.                  \tag{4.2}
\]

At each fixed streaming state retain the nondominated pairs

```text
(area so far, positive starts so far).
```

This Pareto pruning is exact: all future legal transitions, row replays, and
increments (4.1)--(4.2) depend only on the current streaming state.  A record
weakly smaller in both coordinates can never produce a better terminal
record.

The computation never has more than

```text
17 base states in one layer,
23 total Pareto records in one layer,
3 records at one base state.
```

Its terminal frontier is the three-point set in Section 1.

## 5. Frontier witnesses

The three frontier schedules are:

| area | positive selected starts | start holes `X` | deadline holes `Y` |
|---:|---:|:---|:---|
| 27588 | 10939 | `5722,10950,10951` | `10,12,13` |
| 22766 | 11828 | `10949,10950,11840` | `10,12,10951` |
| 12578 | 12577 | `10949,11839,12589` | `10,10950,11839` |

The first is the known scalar-capacity maximizer.  Its exact generalized
lower host graph has maximum matching `24328/26332`, deficiency `2004`, and
`1478` zero-host targets.  Moving the first start hole from `5722` to `5718`
creates a literal singleton-`8000` socket but only changes the static Hall
deficiency to `2003`.  Those finite audits calibrate the theorem, but neither
is needed for the all-schedule conclusion.

## 6. Scope and the next exact gate

Proved:

1. the frozen carrier is perfect-middle, q1-complete, and all-upper;
2. every realizable three-hole P/Q schedule for its fixed order lies below at
   least one of the two necessary compiler thresholds; and
3. no lower Hall, common-cap, or SAT solve for this order can succeed.

Not proved:

1. a global impossibility for another ordering of the same rank-eight deck;
2. a no-go for another q1-safe segment reversal or endpoint rerooting;
3. a lower bound `nu(16)>12873`.

For any proposed new order `T'`, the first exact screen is now:

> compute its realizable P/Q Pareto frontier and require an intersection with
> `area>=26323` and `positive starts>=11437`, while separately retaining
> middle squarefreeness, q1 coverage, and all upper shadows.

Only after that intersection exists is the full lower occurrence Hall/common-
cap compiler worth solving.

## 7. Reproducible audit

```text
scratch/audit_k16_facet_uppercomplete_pq_area_chain_pareto_20260731.py
SHA-256 c0b67e12f482e244562e0e7a745a9a8f763e9d6a8234023e0f187b0c1bc7f4f3

scratch/k16_facet_uppercomplete_pq_area_chain_pareto_20260731.audit.json
SHA-256 e85be739ed659a84ab1ee44a0f8da980792e41a3f8410de31bc2e4d38379ebd7
payload SHA-256 8cef70fcb7281d5b507e44568a4ce83b744a008276d2d8dfb7a7a07c110be8b3

scratch/audit_independent_k16_facet_uppercomplete_pq_area_chain_pareto_20260731.py
SHA-256 18c3343360c7f241c22c503f284e100fc011531d1d2da78e96b0bfd5f1f29c04

scratch/audit_independent_k16_facet_uppercomplete_pq_area_chain_pareto_20260731.audit.json
SHA-256 3e6568e81d54925ef1420052b815552a9500e5b3e323c427e6d72ac593877fa2
payload SHA-256 7eaed9becf5697265f74ff9e7220d2760f2475303e4af1b562d14fe00d230114
```

The audit pins the carrier SHA and the authoritative facet-audit payload,
replays every maximal-envelope transition, recomputes both objective
increments, performs exact Pareto pruning, and reconstructs all three
terminal witnesses.  It runs locally in under one second and uses no solver.
The independent implementation reconstructs the transition system and depth
histograms separately and reproduces the same three-point frontier.
