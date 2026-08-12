# Independent audit of the rank-seven truncated-width production cut

## Verdict

**PASS.**  The opt-in module under

```text
K11_FOREST_RANK7_TRUNCATED_WIDTH=1
```

is a sound necessary consequence of
`K11_THREE_LAYER_WIDTH_ALIGNMENT.md`, preserves every genuine length-465
model in both rank-filtration branches, is inert when disabled, and has the
claimed exact inventory.

This audit was made against source SHA-256

```text
31dbc54a87af387287e729f708bd31c9fe573a988d62345b0bc10480470c8eda
  k11_forest_sat.cpp
```

The extracted `RankSevenTruncatedWidthPlan` block has SHA-256

```text
44ca7216ff457a381c7805da36d878a39e4deae0dd34abf41f8711b40ddf8be2
```

No solver process was launched or modified in this audit.  All generator
runs used a build-only test double and make no SAT or UNSAT claim.

## 1. Mathematical translation

The audited three-layer theorem gives

```text
Type II:  T7=sum min(width_7,4) >= 930,
Type I:   T7=sum min(width_7,4) >= 940.
```

The branch constants are correct.  In Type II, the rank cap forbids every
literal rank-six entry, hence the selected rank-six schedule has `x0=0`.
The general inequality

```text
T7 >= 945-3e+3x0-2q
```

and `e,q<=3` give 930.  Type I requires rank-six branch one; its unit fixes
the exact JointBand flag `e=x0` to one, and its branch-profile plan supplies
the boundary-localized row used in

```text
T7 >= 952-3e-q >= 940.
```

For a crossed active rank-seven target, the existing adjacent-shadow clauses
force a proper selected rank-six prefix and suffix.  In particular, its
width is at least one.  For each threshold `t=2,3,4`, the new credit bit is
allowed to be true only if the crossed interval has width at least `t`.
Thus an active target contributes at most its actual truncated width.

If a target is inactive, the existing coverage clause assigns it to one of
the six exact generic exception slots.  The new clause

```text
active OR credit
```

gives it all three virtual credits.  Replacing the unknown generic witness's
actual truncated width by the maximum value four can only increase the
left-hand side of a necessary lower bound.  Every location implication also
contains `!active`, so the otherwise-unused crossed interval remains free.
This remains sound if a target happens to have both a crossed and a generic
witness: use the crossed witness when `active` is true.

There are 330 unavoidable width-one units and 990 threshold credits.  If
`D` counts false credits, then

```text
T7_projected = 330+(990-D)=1320-D.
```

Consequently the production comparisons

```text
D<=390  (Type II),
D<=380  (Type I)
```

are exactly the theorem's two projected rows.

## 2. Exhaustive threshold-clause audit

For an exact unary interval `[left,right]`, production uses

```text
!credit OR !active OR !L(p) OR L(p-1) OR R(p+t),
```

with nonexistent boundary literals omitted.  Since `L(p)` means
`left<=p`, only `p=left` can activate the endpoint part.  At that position,
`R(p+t)` is exactly `right>=left+t`; when `p+t>=465`, omission of `R`
correctly forbids the threshold.

The independent checker exhausts all

```text
465*466/2 * 3 * 2 * 2 = 1,300,140
```

combinations of physical interval, threshold, active state, and credit
state.  In every case the emitted local formula is equivalent to

```text
(active OR credit) AND
NOT(active AND credit AND width<t).
```

This simultaneously checks the left boundary, the three right-boundary
truncations, and inactive-target freedom.

## 3. Signed exact counter and comparators

The 14-clause full adder was independently evaluated on all 32 assignments
of its three inputs and two outputs.  Exactly the eight correct
sum/carry assignments survive.  Signed literals are valid adder inputs: the
counter receives the truth values of `!credit`, not unsigned variable IDs.

An independent reconstruction of the dynamic Wallace topology gives

```text
973 compression full adders,
  9 final ripple full adders,
982 full adders total,
 10 exact output bits.
```

The reconstruction was checked for every possible deficit count `0..990`
and 4,096 independently randomized placements of those signed input truth
values.  Its output always equals the ordinary, nonmodular deficit sum.

The direct first-difference comparator was exhausted on all 1,024 ten-bit
values for each constant.  It accepts exactly `0..390` with six clauses and
exactly `0..380` with four clauses.

## 4. Prerequisite and source wiring audit

The source rejects the guard unless adjacent shadows are enabled and exactly
one rank-filtration architecture is selected.  Executed negative tests gave
exit status two for:

* Type II without adjacent shadows;
* adjacent shadows without either rank-filtration branch;
* Type II without its local-density prerequisite.

The rank-filtration validation is transitive:

* Type II requires local density, band cuts, and joint-band cuts;
* Type I requires those three modules and rank-six branch one;
* branch one in turn requires the canonical and oriented rank-six boundary
  modules and constructs the exact Type-I branch-profile rows.

The new plan is built from the 330 existing `RankSevenShadow` records, uses
the existing constant-one literal, is emitted once, and prints every module
subtotal.  The portal specialization explicitly excludes this guard.  No
containment-cap prerequisite is needed because all omitted witnesses receive
only the unconditional truncated maximum four.

The source-level audit also freezes the existing active-witness facts needed
for the constant base unit: exact active left endpoints must select a
rank-six interval starting there, and the comparison forces the rank-seven
right endpoint past that interval.

## 5. Exact inventory

The independently derived module inventory is

```text
credit variables                                      990
counter variables                                    1964
total variables                                      2954

location clauses                         330*3*465 = 460350
inactive-credit clauses                      330*3 =    990
counter clauses                              982*14 =  13748
comparator clauses                         Type II =      6
                                           Type I  =      4

total clauses                              Type II = 475094
                                           Type I  = 475092
```

Fresh build-only reconstruction of the actual generator reproduced these
subtotals and the following full inventories:

```text
minimal Type II off: 3,224,194 variables / 14,912,057 clauses
minimal Type II on : 3,227,148 variables / 15,387,151 clauses

minimal Type I off : 3,216,962 variables / 15,098,591 clauses
minimal Type I on  : 3,219,916 variables / 15,573,683 clauses

full Type II on    : 3,660,029 variables / 20,076,856 clauses
full Type I on     : 3,640,493 variables / 19,989,126 clauses
```

The full Type-II build includes the coordinate-pin localization module; the
full Type-I build includes the canonical prefix-chain module.  These totals
match the implementation note exactly.

## 6. Fresh clause-stream regression

The audit compiled the source against a new independent hash stub that:

* hashes every literal and clause terminator;
* counts add calls, clauses, and nonzero literals;
* aborts if an emitted variable exceeds the declared range; and
* reports the maximum emitted variable.

The minimal absent and explicit-`0` logs are byte-identical in each branch:

```text
Type II off: FNV64=c763ec344354e911, ADD_CALLS=62109310
Type I  off: FNV64=a2c6f8cb54144c8e, ADD_CALLS=64580628
```

Guard-on and full fingerprints are

```text
minimal Type II on: FNV64=acdaa57fbdf21350, ADD_CALLS=64933307
minimal Type I  on: FNV64=2027252822032bf8, ADD_CALLS=67404613
full Type II on:    FNV64=b54e178368e1f4d3, ADD_CALLS=88666811
full Type I  on:    FNV64=151bd51155629c61, ADD_CALLS=88275995
```

In every build, `MAXVAR=DECLARED`.  Therefore the fresh rebuild found no
out-of-range variable and confirms exact guard-off identity at the complete
clause-stream level.

The reproducible independent artifacts are

```text
scratch/audit_k11_rank7_truncated_width_source.py
scratch/rank7_independent_hash_stub/cadical.hpp
scratch/run_k11_rank7_independent_hash_audit.sh
```

Their SHA-256 values at audit time are

```text
8cc522383ff54f9fb67134943d61c705a61dc4529bdab6e21d1b4ddecee9487e
  scratch/audit_k11_rank7_truncated_width_source.py
2a5f23f1e310ecff7cf9c27596ef047787ab92240e24a2e02f899ea62cdc727c
  scratch/rank7_independent_hash_stub/cadical.hpp
907247014bf48b526b4a4a5b58212661272431ce6bde8574d20e2aaa8c39586e
  scratch/run_k11_rank7_independent_hash_audit.sh
```

The source-audit checker prints

```text
PASS: independent rank-seven truncated-width source audit
threshold_cases=1300140
counter_assignments=5087 comparator_values=2048
Type II module=2954 variables/475094 clauses
Type I module=2954 variables/475092 clauses
```

The supplied theorem-profile and implementation checkers were rerun only as
corroboration; both pass.  The verdict above rests on the independent
clause-template, arithmetic, source, and fresh-generator checks described
here.
