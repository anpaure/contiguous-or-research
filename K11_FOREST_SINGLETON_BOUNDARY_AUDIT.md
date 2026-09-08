# Independent audit of the k=11 singleton-boundary reduction

## 1. Verdict

**PASS, with one terminology clarification and no correction to either
inequality.**

The boundary-localization theorem, deletion/compression argument, and the
strengthened joint short-pool cuts in
`K11_FOREST_ENDPOINT_ALIGNMENT_SECOND_ORDER.md` are correct:

```text
x0+x1+y0+y1 <= 380-13*x0,
y2            >= x1+82+14*x0.
```

In particular, in the `x0=1` branch,

```text
y2>=x1+96.
```

The displayed surviving profile and interval schedules are also valid and
show that these scalar and endpoint constraints do not eliminate the
singleton branch.

The terminology clarification is that the coefficient 13 is an exact loss
of **net short-pool capacity**, not the deletion of thirteen physical
intervals.  Deleting a boundary position removes exactly two physical
singleton-or-pair slots.  The remaining eleven units arise because twelve
additional lower targets become forced into the short pool while the selected
rank-six singleton itself is removed from the counted witness set.  The net
strengthening is `2+12-1=13`.

## 2. Localization of a selected rank-six singleton

Every selected rank-six witness lies in the unrestricted monotone band

```text
I_i=[i+alpha_i,i+beta_i],
0<=alpha_i<=beta_i<=3,
```

with both offset coordinates nondecreasing.  The already audited pool theorem
gives

```text
x3>=93,
```

so state `03=(0,3)` occurs.

The four width-zero states are `00,11,22,33`.  Of these, only `00` and `33`
are comparable with `03` in the coordinatewise state order:

```text
00 < 03 < 33,
11 and 22 incomparable with 03.
```

Since the monotone schedule is a chain, a width-zero occurrence must therefore
be `00` or `33`.  If `x0=1`, its occurrence is unique.

* A unique `00` must be schedule index zero.  Any earlier state would have to
  be at most `00`, hence would be another `00`.  Its interval is `[0,0]`.
* A unique `33` must be schedule index 461.  Any later state would have to be
  at least `33`, hence would be another `33`.  Its interval is
  `[461+3,461+3]=[464,464]`.

Thus

```text
x0=1 -> the selected singleton is at physical position 0 or 464.
```

There is no hidden fixed-row assumption beyond the unrestricted monotone-band
normal form for the selected rank-six antichain.

The witness-choice quantifier is also strong enough for an array-level
corollary: if any literal rank-six array entry occurred at an interior
position, deliberately choosing it as that target's singleton witness would
contradict the localization theorem.  Hence every literal rank-six entry of a
length-465 solution must itself be at position zero or 464.  The audited
source only needs the weaker selected-schedule formulation.

## 3. Deleting the boundary singleton

Let `[p,p]` be the selected rank-six singleton with value `U`, where
`p in {0,464}`.  Any interval containing `p` has OR containing the 6-set `U`.
It therefore cannot witness a target of rank at most five.

Consequently every existing witness for every mask of ranks one through five
avoids `p`.  Delete the boundary entry.  Because `p` is an endpoint, every
such witness remains an unchanged contiguous interval after the obvious
index shift.  The reduced word has length

```text
n'=464
```

and still covers every mask through rank five.

In particular, all 462 selected rank-five witnesses survive.  They remain
pairwise nonnested and have distinct left and right endpoints.  Their new
endpoint slack is exactly

```text
n'-C(11,5)=464-462=2.
```

The standard band argument now says that every reduced-word interval of
length at least three contains one of these selected rank-five witnesses:
an interval beginning at `a` contains `[a,a+2]`, which contains the selected
rank-five interval indexed by `a`.

An interval representing a target of rank at most four cannot contain a
rank-five witness.  Since all such targets are still covered in the reduced
word, every one of the

```text
C(11,1)+C(11,2)+C(11,3)+C(11,4)
=11+55+165+330
=561
```

targets has a witness of physical length at most two.

This proves the claimed strengthening from the earlier 549 forced-short
targets to all 561.  No witness is assumed to survive a noncontiguous interior
deletion; the singleton was first proved to be at a physical boundary.

## 4. Which central witnesses survive the deletion

Every selected rank-five interval avoids `p`, because its target has rank
five.  Therefore all `y0+y1` selected rank-five witnesses of physical length
one or two remain short intervals in the reduced word.

No other selected rank-six witness can contain `p`.  If it did, its OR would
contain `U`; because its OR also has rank six, it would have to equal `U`.
But `[p,p]` is already the one selected witness for target `U`, and the
selected family uses one witness per distinct target.  Thus every one of the
`x1` non-singleton rank-six length-two witnesses avoids the deleted entry and
survives with unchanged length.

All intervals counted in the three groups

```text
561 lower targets,
y0+y1 selected rank-five targets,
x1 selected rank-six targets
```

are physically distinct.  Two groups cannot share an interval because its OR
would then have two different masks or ranks; within one group the target
masks are distinct.

## 5. Exact short-pool count and the coefficient 13

A word of length 464 has

```text
464 singleton intervals + 463 adjacent pairs = 927
```

physical intervals of length at most two.  Therefore, in the `x0=1` branch,

```text
561+(y0+y1)+x1 <= 927,
```

or

```text
x1+y0+y1<=366.                                  (5.1)
```

The previously audited joint-pool inequality is

```text
x0+x1+y0+y1<=380.                               (5.2)
```

For `x0=0`, retain (5.2).  For `x0=1`, equation (5.1) is equivalent to

```text
x0+x1+y0+y1<=367.
```

Because `x0` is already proved Boolean, the two branches combine exactly as

```text
x0+x1+y0+y1<=380-13*x0.                        (5.3)
```

The coefficient accounting can be seen by comparing the two proofs in the
singleton branch:

```text
old: 549 lower + 1 selected singleton + x1+y0+y1 <= 929,
new: 561 lower                        + x1+y0+y1 <= 927.
```

The new upper bound on `x1+y0+y1` is smaller by

```text
(561-549) + (929-927) - 1 = 13.
```

Only `929-927=2` of these units are deleted physical slots.  This distinction
does not affect the inequality.

Finally, since

```text
y0+y1+y2=462,
```

substitution into (5.3) gives

```text
y2>=x1+82+14*x0.
```

The coefficient 14 is correct: one copy comes from moving `x0` on the left,
and thirteen from the branch-dependent right side.

## 6. Independent check of the surviving profile

The claimed profile is

```text
x=(1,0,366,95),
y=(0,366,96).
```

It satisfies the new pool row at equality:

```text
x0+x1+y0+y1=1+0+0+366=367=380-13,
y2=96=x1+82+14.
```

Its monotone interval schedules are

```text
upper:
  I_0       =[0,0],
  I_i       =[i,i+2]  for 1<=i<=366,
  I_i       =[i,i+3]  for 367<=i<=461;

lower:
  J_i       =[i+1,i+2] for 0<=i<=365,
  J_i       =[i+1,i+3] for 366<=i<=461.
```

Direct enumeration gives exactly the stated width profiles.  The endpoint
sets have

```text
461 common left endpoints,
460 common right endpoints,
3 path components.
```

At every common left endpoint, the lower interval is a proper prefix of the
upper interval.  At every common right endpoint, it is a proper suffix.  No
pair receives both endpoint colours.  The width-qualified alignment counts
are

```text
Z324 left/right = 461,460,
Z24  left/right = 95,95,
```

so all four audited alignment lower bounds hold.

The profile also satisfies the previously audited scalar inequalities:

```text
x3=95=93+2*x0,
y1+2*y2=558>=549+4*x0,
x0+x1<=y0+3,
x0+x1+x2<=y0+y1+3,
W6-W5=1017-558=459>=455.
```

No masks are assigned, so this is correctly presented only as a surviving
endpoint schedule, not as an OR-array construction.

## 7. Checker audit

The supplied checker

```text
scratch/enumerate_k11_second_order_profiles.cpp
SHA-256 347d5fb615eff837c0f8b7da37973171e39c4db74f7f1ceb6817f79cf5e8a62e
```

was compiled with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic
```

and independently reproduced every displayed profile count:

```text
previous x0=0: 33454 upper, 290393090 joint
previous x0=1: 32852 upper, 273169120 joint
plus x3 cut:   32835 upper, 273168882 joint
plus boundary: 31918 upper, 272277079 joint
```

It also reconstructs the explicit schedules and prints

```text
sample_endpoint_schedule common_L=461 common_R=460 components=3
Z324_LR=461,460 Z24_LR=95,95 PASS
```

I independently checked the checker inequalities against the previously
audited scalar ledger.  Its lower and upper bounds on `y2` encode exactly the
rank-five fan cuts, both cumulative nesting cuts, the joint pool row, and the
total-width separation.  The boundary row is inserted as

```text
y2>=x1+82+14*x0,
```

with the correct polarity.

## 8. Certified scope

The boundary theorem is conditional on the selected rank-six witness family
having `x0=1`; it does not assert that every arbitrary auxiliary witness
selection must contain a singleton whenever the array has a rank-six literal.
Because witness selection is free, however, it also proves the array-level
corollary that any literal rank-six entry must occur at a physical boundary.

The cuts are necessary consequences for every length-465 universal array and
every selected central schedule after the indicated branch choice.  They do
not prove that the displayed endpoint schedule admits compatible masks, and
they do not resolve k=11.

