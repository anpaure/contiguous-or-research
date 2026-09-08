# Rank-seven truncated-width production cut: independent recommendation

## Verdict

The rank-seven consequence in `K11_THREE_LAYER_WIDTH_ALIGNMENT.md` is valid,
but its proposed production projection is unnecessarily expensive.  The
proof of the width moment never uses widths above four: equation (5.3)
actually proves

```text
sum_S min(w_S,4) >= 930     (Type II),
sum_S min(w_S,4) >= 940     (Type I),
```

where one witness is selected for every one of the 330 rank-seven targets.
This is stronger than merely proving the same lower bound for the untruncated
width sum.

Under the existing adjacent-shadow compression, replace a target not using
its crossed (`active`) witness by the maximum possible truncated credit four.
No rank-seven generic witness needs to be materialized in the counter.  This
gives the exact safe projection

```text
sum_(S active) min(w_S,4) + 4*(330-A7) >= 930  (Type II),
sum_(S active) min(w_S,4) + 4*(330-A7) >= 940  (Type I).
```

This projection is valid even if crossed and generic witnesses coexist for a
target.  Choose the crossed witness whenever `active` is true and one generic
slot otherwise.  Replacing an inactive target's actual truncated width by
four can only increase the left side.

## Recommended encoding

For every rank-seven shadow target `S` and `t in {2,3,4}`, allocate one
virtual credit bit `u[S][t]`.  Its intended extension is

```text
u[S][t] = true,  if S is inactive;
u[S][t] = (w_S>=t), if S is active.
```

Exact equivalence is unnecessary.  The following implications are sufficient
and preserve every original model:

1. `active[S] OR u[S][t]`.  Thus an inactive target receives full virtual
   credit.
2. If `active[S] AND u[S][t]`, the existing crossed interval has width at
   least `t`.

The second implication can use the existing unary left/right thresholds with
no endpoint-selector auxiliaries.  For a possible exact left endpoint `p`,
emit

```text
!u OR !active OR !L(p) OR L(p-1) OR R(p+t)       (p>0, p+t<465),
!u OR !active OR !L(0) OR R(t)                   (p=0),
```

omitting `R(p+t)` when `p+t>=465`.  The unique `0...01...1` transition of
`L` makes the clause active only at the actual left endpoint.  It then says
that the actual right endpoint is at least `p+t`.

Every active crossed rank-seven witness has width at least one: its selected
rank-six prefix and suffix are both proper.  Hence the total virtual truncated
credit is

```text
330 + sum_(S,t) u[S][t].
```

Equivalently, count the 990 signed literals `!u[S][t]` and impose

```text
count(!u) <= 390   (Type II),
count(!u) <= 380   (Type I).
```

The credit bits need not be made monotone in `t`.  Each positive bit
independently certifies one valid unit of truncated width, and every original
model extends by setting all valid thresholds true.

## Exact prerequisite audit

Required:

* `K11_FOREST_ADJACENT_SHADOWS=1`, which supplies `active`, `L0`, and `R0`
  for all 330 crossed rank-seven targets;
* exactly one rank-filtration architecture:
  `K11_FOREST_RANK_FILTRATION_TYPE1=1` or
  `K11_FOREST_RANK_FILTRATION_TYPE2=1`.

The rank-filtration guards already require the band, joint-band, and local
density modules used in the mathematical derivation.  Type I also requires
rank-six branch one, whose `RankSixBranchProfilePlan` encodes the
boundary-localized row used to obtain 940.  Type II forbids literal rank-six
entries and hence has `x0=0`, giving 930.

`K11_FOREST_CONTAINMENT_CAPS` is **not** required for this truncated encoding.
The cap nine is needed by the earlier full-width `+9*(330-A7)` projection,
but every omitted truncated witness has unconditional maximum credit four.

There is no hidden generic-slot issue.  The six exception slots certify that
every inactive target has a genuine alternative witness; their actual widths
are deliberately projected away.  The width clauses above are guarded by
`active`, so forcing virtual credit for an inactive target does not constrain
its otherwise-unused shadow interval.

## Exact expected inventory

Reuse the existing constant-one literal and the existing rank-seven
`active/L/R` variables.  No existing rank-seven width bits or reusable counter
output exists.

For 330 targets and three thresholds:

```text
virtual credit variables                         990
left-transition implication clauses       330*3*465 = 460350
inactive-credit clauses                    330*3     =    990
```

A Wallace exact count of 990 signed literals using the production 14-clause,
two-variable full adder takes 973 compression adders plus nine final ripple
adders:

```text
counter variables                           2*982 =   1964
counter clauses                            14*982 =  13748
```

The direct constant comparator contributes six clauses for 390 and four for
380.  Therefore the exact expected plan totals are

```text
Type II: 2954 variables, 475094 clauses,
Type I : 2954 variables, 475092 clauses.
```

This is substantially smaller than the nine-threshold full-width encoding:
that version would require 2,970 threshold variables before its counter and
about 1.38 million left-transition clauses.

## Production recommendation

Implement the truncated plan, not the full-width plan.  Keep separate Type-I
and Type-II build inventories, hash the guard-off clause stream, and audit:

1. every left-transition clause under all exact intervals;
2. inactive targets with arbitrary unused shadow intervals;
3. the 990-input signed-literal counter and both constant comparators;
4. source-level prerequisites and exact guard-off identity.

The standalone checker
`scratch/check_k11_rank7_truncated_width_encoding.cpp` verifies the local
threshold semantics, comparator constants, and the inventory above.

