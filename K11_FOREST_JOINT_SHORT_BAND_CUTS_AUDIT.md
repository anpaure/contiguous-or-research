# Independent audit of the proposed joint `k=11` short-pool and band cuts

## Verdict

All asserted inequalities in `K11_FOREST_JOINT_SHORT_BAND_CUTS.md` are
globally valid for every universal nonzero array of length 465:

```text
x0 <= 1
y0 <= 135
y1+2*y2 >= 549
x0+x1+y0+y1 <= 380
x0+x1 <= y0+3
x0+x1+x2 <= y0+y1+3
(x1+2*x2+3*x3)-(y1+2*y2) >= 455.
```

The latest note also proves the strictly sharper `x0`-coupled fan forms

```text
y0+x0 <= 135,
y1+2*y2 >= 549+4*x0.
```

Here `xj` counts selected rank-six witnesses of width `j`, and `yj` counts
selected rank-five witnesses of width `j`.  Width is physical length minus
one.  The proofs use only unrestricted selected witness families and do not
assume a fixed derivative row, Johnson adjacency, or central connectivity.

I specifically checked the potentially delicate simultaneous use of the
rank-three and rank-four crossing theorems.  Their guaranteed short witnesses
can be chosen at the same time, are physically distinct, and may therefore be
added.  Together with ranks one and two they force 549 distinct singleton or
adjacent-pair intervals.

The supplied profile checker is arithmetically correct.  An independent
direct enumeration, looping over `y0` and explicit `y2` ranges rather than its
`d=y2-y0` organization, reproduces

```text
old rank-six profiles       130,204
unconstrained profile pairs 13,985,992,864
surviving profile pairs     563,562,210.
```

The joint short-pool inequality is a valid independent theorem but is
numerically redundant once `y1+2*y2>=549` and the first cumulative nesting
cut are both imposed.  The independent enumeration returns the same
563,562,210 count with the pool inequality deleted.  The total-width 455 row
is likewise redundant after `x0<=1` and both cumulative nesting cuts.

This is a theorem audit only.  The cuts are not implemented in the frozen
solver and prove no SAT or UNSAT result.

Frozen source hashes:

```text
K11_FOREST_JOINT_SHORT_BAND_CUTS.md
75968aec941a03f6503bc8af147b82b5006cc002467c874eddf835b257f514e9

scratch/verify_k11_forest_joint_short_cuts.cpp
108c15dfa835cb958c2bd1260636eb61e14619cc52ef5b9461e991ba1c1570a2
```

## 1. Common setup

Choose one witness interval for every rank-five mask and sort the 462
intervals by left endpoint.  Equal-rank incomparability makes both endpoint
sequences strictly increasing.  With `n=462+3`, their unrestricted band is

```text
I_i=[i+alpha_i,i+beta_i],
0<=alpha_i<=beta_i<=3.
```

Every physical interval of length at least four contains a selected rank-six
witness: if it begins at `a`, then `a<=462` and it contains the rank-six
selected interval lying inside `[a,a+3]`.  Its OR therefore has rank at least
six.  Consequently every exact rank-five witness has length at most three and
width at most two.  Thus

```text
y0+y1+y2=462.
```

The selected rank-six widths lie in `0,...,3`, so

```text
x0+x1+x2+x3=462.
```

These facts are unrestricted interval geometry, not fixed-row assumptions.

## 2. Independent audit of the rank-five fan cuts

The already-audited fan-capped avoidance theorem says that for a target
family of interval-containment chain height at most `h`, all of whose witness
intervals avoid containing a selected central witness,

```text
|F| <= sum_i min(width_i,h) + h*D,
```

where here `D=465-462=3`.

### 2.1 The cut `y0<=135`

Take the 330 rank-four masks.  Their chosen intervals are an antichain:
nesting would make two distinct equal-cardinality OR masks comparable.  They
all avoid containing a selected rank-five witness, because such containment
would make their OR have rank at least five.  Therefore `h=1` and

```text
330 <= sum_i min(width_i,1)+3
    = (462-y0)+3.
```

Rearranging gives exactly

```text
y0<=135.
```

### 2.2 The cut `y1+2*y2>=549`

Take one interval for every nonempty mask of ranks one through four.  There
are

```text
11+55+165+330 = 561
```

such masks.  A chain of their OR masks has at most four members, so their
interval-containment height is at most four.  Again, no witness may contain a
selected rank-five interval.  Since each selected rank-five width is at most
two,

```text
561 <= sum_i min(width_i,4)+4*3
    = y1+2*y2+12.
```

Hence

```text
y1+2*y2>=549.
```

Using `y0+y1+y2=462`, this is equivalently

```text
y2>=y0+87.
```

Both uses of the fan theorem have the correct chain heights and off-by-one
width convention.

### 2.3 The `x0`-coupled fan refinement

Every selected rank-six singleton position `p` is one of the three omitted
rank-five right endpoints, as proved in Section 3 below.  More strongly, no
target of rank at most four can have a witness ending at `p`, because that
interval would contain the rank-six array entry at `p`.  In the right-endpoint
proof of the fan theorem, this free endpoint therefore contributes zero
rather than the generic height cap.

The `x0` singleton positions are distinct, so the free-endpoint term improves
from `h*3` to `h*(3-x0)`.  Repeating the two applications gives

```text
330 <= (462-y0)+(3-x0),
561 <= y1+2*y2+4*(3-x0).
```

Equivalently,

```text
y0+x0<=135,
y1+2*y2>=549+4*x0,
y2>=y0+87+4*x0.
```

This refinement is valid: it uses actual impossibility of a lower witness at
those physical endpoints, not merely the fact that they are absent from the
selected rank-five endpoint set.  Since `x0<=1`, it only strengthens the
`x0=1` branch, to `y0<=134` and `y2>=y0+91`.

## 3. Omitted-endpoint proof of `x0<=1`

Let `O_L` and `O_R` be the three physical positions omitted by the selected
rank-five left and right endpoint sets.  Since each occupied endpoint set is
the complement of its omitted triple in `{0,...,464}`,

```text
sum_i (right_i-left_i) = sum(O_L)-sum(O_R).
```

The sign is correct: selected-right sum is total-position sum minus
`sum(O_R)`, while selected-left sum is total-position sum minus `sum(O_L)`.
The left side is `y1+2*y2`.

Now let `[p,p]` be a selected rank-six singleton witness.  No rank-five
witness can begin at `p`: it would contain the rank-six array entry and hence
have OR rank at least six.  Nor can a rank-five witness end at `p`.  Therefore

```text
p in O_L intersection O_R.
```

Different selected rank-six singleton targets occupy different positions,
because a physical singleton has one OR value.  Consequently

```text
|O_L intersection O_R|>=x0.
```

If two three-subsets have `c` common points, remove their common contribution
from the sum difference.  Put `q=3-c`.  The largest possible remaining
difference uses the `q` largest positions on the left and the `q` smallest on
the right:

```text
sum(O_L)-sum(O_R) <= q*(465-q).
```

Because `c>=x0` and this expression increases for `0<=q<=3`,

```text
y1+2*y2 <= (3-x0)*(462+x0).
```

If `x0>=2`, its right side is at most

```text
(3-2)*(462+2)=464,
```

contradicting the fan lower bound 549.  Hence

```text
x0<=1.
```

This sharpening genuinely uses the rank-five width-mass cut; the omitted-set
identity alone only supplies the displayed upper bound.

## 4. Cumulative cross-layer nesting

Fix `t` in `{0,1,2}` and let

```text
X_t=x0+...+xt.
```

The `X_t` selected rank-six intervals have distinct left endpoints.  The
selected rank-five left endpoint set omits only three positions, so at least
`X_t-3` of these endpoints are shared.

At a shared left endpoint, the rank-five interval must be a proper prefix of
the rank-six interval.  If it ended at or after the rank-six interval, it
would contain a six-set witness while having a five-set OR.  Equality is also
impossible.  A rank-six interval of width at most `t` therefore maps to a
rank-five interval of width at most `t-1`.

The map is injective because selected rank-five left endpoints are distinct.
Thus

```text
x0+...+xt <= 3+y0+...+y_(t-1).
```

For `t=0` this is the older `x0<=3`.  The two new cases are exactly

```text
x0+x1 <= y0+3,
x0+x1+x2 <= y0+y1+3.
```

The right-endpoint argument is dual and yields the same scalar inequalities.
The second cut is equivalently

```text
y2<=x3+3.
```

I found no reversal or injection error in either direction.

## 5. Simultaneous forced short witnesses

### 5.1 Ranks one and two

A length-465 optimum is zero-free.  Deleting a zero entry preserves every
nonzero interval OR after compression and would give a forbidden length-464
universal array.

An interval with rank-one OR consists entirely of the same nonzero singleton,
so one of its entries is a singleton witness.  For a rank-two target
`{a,b}`, either some entry already equals `{a,b}`, or every entry in a witness
is `{a}` or `{b}`.  Both values occur, so an adjacent transition has OR
`{a,b}`.  Therefore all 11 rank-one and 55 rank-two masks have witnesses of
length at most two.

### 5.2 Ranks three and four really are simultaneous

For an arbitrary chosen rank-five witness family, independently choose one
witness for every rank-three and every rank-four target.  The endpoint-set
crossing arguments give, for **every** such choice,

```text
at least 159 of 165 rank-three witnesses of length at most two,
at least 324 of 330 rank-four witnesses of length at most two.
```

Neither conclusion consumes or modifies the rank-five family used by the
other.  Hence the two guarantees hold simultaneously, not merely in two
different existential choices.

All selected lower short intervals are physically distinct.  One physical
interval has one OR value, so it cannot represent two different masks, and in
particular cannot represent masks of two different ranks.  Thus the counts
may be added:

```text
11+55+159+324 = 549.
```

This resolves the main possible obstruction to the joint-pool count.

## 6. The joint short-pool inequality

There are exactly

```text
465 singleton intervals + 464 adjacent pairs = 929
```

physical intervals of length at most two.  Besides the 549 lower witnesses,
the selected central families use

```text
y0+y1
```

rank-five intervals and

```text
x0+x1
```

rank-six intervals in this pool.  They are distinct within each selected
family by target uniqueness, across the two central ranks, and from every
lower witness because a physical interval cannot have OR masks of different
ranks.

Therefore

```text
549+(y0+y1)+(x0+x1)<=929,
```

or

```text
x0+x1+y0+y1<=380.
```

Equivalently,

```text
y2>=x0+x1+82.
```

No connectivity or fixed-window hypothesis enters this count.

## 7. Numerical relations and redundancy

The rank-five width-mass cut gives

```text
y2>=y0+87.
```

The first nesting cut gives

```text
y0>=x0+x1-3.
```

Combining them yields the strictly stronger scalar consequence

```text
y2>=x0+x1+84.
```

Hence the pool requirement `y2>=x0+x1+82` is redundant once those two cuts
are installed.  It remains independently valid and is useful as a regression
check because its proof uses the short-witness geometry rather than the fan
theorem.

In the existing rank-six boundary notation,

```text
x0+x1=b2+462-b5,
```

so the pool inequality becomes

```text
y2+b5-b2>=544.
```

The algebra is correct.  The stronger `x0<=1` merely changes the existing
boundary comparison from `b1+459<=b6` to `b1+461<=b6`.

The omitted-endpoint upper bound is numerically redundant after `x0<=1`: for
`x0=0` or 1 its right side is at least 926, while the maximum possible
rank-five width mass is `2*462=924`.

### 7.1 Total central width: 453 directly and 455 cumulatively

There is a valid independent 453 bound.  Match selected rank-five and rank-six
intervals by common left endpoint.  If `d` endpoints occur only in either
family, then `d<=3`.  Each of the `462-d` common endpoints contributes at
least one to `width_6-width_5`; each rank-six-only endpoint contributes at
least zero; and each rank-five-only endpoint costs at most two.  Therefore

```text
W6-W5 >= (462-d)-2*d >= 453.
```

The source's stronger 455 theorem is also valid.  Add

```text
x0<=1,
x0+x1<=y0+3,
x0+x1+x2<=y0+y1+3
```

to obtain

```text
3*x0+2*x1+x2 <= 2*y0+y1+7.
```

Since

```text
W6 = 3*462-(3*x0+2*x1+x2),
W5 = 2*462-(2*y0+y1),
```

this is exactly

```text
W6-W5>=455.
```

Thus 455 is a regression consequence of the three stronger rows, not an
independent pruning cut.

The boundary expression is

```text
W6=g4+g5+g6-g1-g2-g3,
W5=462-y0+y2.
```

Consequently a direct unsigned comparator for `W6-W5>=C` is

```text
(462+C)+y2+g1+g2+g3 <= y0+g4+g5+g6.
```

For `C=453` the constant is 915; for the displayed `C=455` theorem it is
917.  The latest equation (17) and the primary checker's `row5` both use 917
and test `W6-W5>=455` exactly.

## 8. Rank-five state-chain classification

After state `03` is forbidden, the coordinatewise state poset has exactly the
four maximal chains listed in the source note:

```text
00 01 02 12 13 23 33
00 01 02 12 22 23 33
00 01 11 12 13 23 33
00 01 11 12 22 23 33.
```

On all four chains, width-zero states are among `00,11,22,33`, width-one
states among `01,12,23`, and width-two states are `02,13`.  The last chain
contains no width-two state and therefore cannot satisfy
`y1+2*y2>=549`, since its total width mass is at most 462.  This classification
supports a small future boundary circuit.

For the remaining chains A, B, and C, let `h1,...,h6` be cumulative block
boundaries.  Directly summing the seven state widths verifies every row of the
source table:

```text
A: y0=462+h1-h6,             y2=h3+h5-h2-h4
B: y0=462+h1+h5-h4-h6,       y2=h3-h2
C: y0=462+h1+h3-h2-h6,       y2=h5-h4.
```

Writing `e=x0` (which is 0 or 1), substitution verifies, chain by chain, the
four guarded comparisons for

```text
y0+x0<=135,
y2>=y0+87+4*x0,
x0+x1<=y0+3,
y2<=x3+3.
```

The global comparison `g1+461<=g6` is exactly `x0<=1`.  Exact-one selection
among A/B/C is complete: every valid monotone rank-five schedule extends to a
maximal chain, and the only omitted maximal chain violates the width-mass
cut.  Schedules using only states shared by multiple chains may select any one
containing chain.

Eleven unsigned bits suffice for the displayed boundary rows in the context
of the existing base cuts.  The largest three-boundary-plus-`549+4e` side is
at most 1,939.  For the total-width row, the prior `W6>=1008` cut implies

```text
g1+g2+g3<=378,
```

so the 917 left side is at most `917+462+378=1757`; the right
side is at most 1,848.  Hence there is no hidden overflow if the future circuit
retains final carries as the existing `BandCutPlan` does.

What exists today is an algebraic circuit specification, not CNF.  Exact
guarding, selector uniqueness, arithmetic-wire allocation, and comparator
clauses still require implementation and a separate source/CNF audit.

## 9. Independent profile enumeration

The supplied checker starts from rank-six profiles satisfying the four
previously audited cuts

```text
x0<=3,
2*x0+x1<=138,
x1+2*x2+3*x3>=1008,
x3>=93,
sum xj=462.
```

It finds 130,204 such profiles.  For a rank-five profile it enforces

```text
y0+y1+y2=462,
y0<=135,
y2>=y0+87.
```

For fixed `xshort=x0+x1`, `x3`, and `W6`, put `d=y2-y0`.  The latest primary
checker uses

```text
d>=87+4*x0,
d<=W6-917,
max(0,xshort-3)<=y0<=min(135-x0,(462-d)/2,x3+3-d).
```

These are respectively the sharpened rank-five fan mass, the 455 width bound,
first nesting, `y1>=0`, and second nesting.  The short-pool cut is omitted
because the fan and first nesting inequalities imply it more strongly.  The
outer loop separately enforces `x0<=1`.

I reproduced its result with a different direct enumeration.  For each old
rank-six profile with `x0<=1`, loop over

```text
max(0,xshort-3) <= y0 <= 135-x0
```

and count the integer values

```text
max(y0+87+4*x0,xshort+82) <= y2 <= min(462-y0,x3+3),
```

This gives exactly

```text
old_rank6_profiles=130204
old_joint_profiles=13985992864
surviving_joint_profiles=563562210.
```

Deleting `xshort+82` from the lower maximum gives the same survivor count.
Adding either explicit upper bound

```text
y2-y0<=W6-915   (453),
y2-y0<=W6-917   (455)
```

also gives the same count, independently confirming that both the pool and
total-width rows are redundant in the full scalar system.

The profile census counts scalar width triples, not concrete endpoint block
lengths, SAT assignments, or universal arrays.  Its role is only to measure
cut strength.

## 10. Checker audit and counterexample tests

The supplied checker compiled cleanly with `g++ -O3 -std=c++20` and printed

```text
crossed_rank3=159 crossed_rank4=324 forced_lower_short=549 joint_capacity=380
rank5_y0_limit=135 rank5_width_mass=549 x0_limit=1
old_rank6_profiles=130204 old_joint_profiles=13985992864 surviving_joint_profiles=563562210 boundary_circuit_cases=300000 PASS
```

Its constants, omitted-sum values, direct profile loop, chain-width table, and
four principal guarded comparison rows are correct.  Its 300,000 boundary
cases are deterministic random regression tests, not exhaustive enumeration.
Its fifth row uses 917 and correctly checks `W6-W5>=455`.  The checker does not
itself prove the endpoint, fan, or simultaneous-witness theorems; those were
audited above.

I added an independent checker using direct `y2` ranges rather than the
primary checker's `d=y2-y0` loop:

```text
scratch/verify_k11_forest_joint_short_cuts_independent.cpp
SHA-256 3f191dea6d5863242caf4c46e9a30b91309f31ce590e4d2fde52076b69ffb45e
```

It reports

```text
crossed3=159 crossed4=324 forced_short=549 capacity=380
old_x_profiles=130204 unconstrained_pairs=13985992864
surviving_pairs=563562210 without_pool=563562210 with_453=563562210 with_455=563562210
pool_and_width_cuts_redundant=PASS
independent_joint_short_cuts=PASS
```

The counterexample attempts checked explicitly were:

* repeated endpoints within one rank—impossible by equal-rank nonnesting;
* two rank-six singleton witnesses using one position—impossible because the
  singleton interval has one OR value;
* a rank-five interval sharing a singleton's endpoint—then it contains the
  rank-six entry and cannot have rank five;
* a shared-left rank-five interval extending beyond the rank-six interval—this
  would contain a six-set witness and reverses the necessary prefix relation;
* incompatibility between the rank-three and rank-four crossing choices—the
  two bounds hold for arbitrary simultaneous choices against the same row;
* overlap among lower or central short witnesses—one physical interval cannot
  have two different OR targets; and
* zero entries invalidating the rank-two transition argument—zeros are
  impossible in a length-465 optimum by deletion and the proved lower bound.

None produces a counterexample.

## 11. Scope

The displayed inequalities are globally necessary cuts for the exact unrestricted
`k=11,n=465` forest/band search.  They do not establish existence or
impossibility.  Before using them in production, their joint rank-five/
rank-six boundary circuit must be implemented and audited independently.
Any eventual SAT model still requires both interval-OR verifiers; any UNSAT
theorem still requires a frozen CNF and independently verified proof trace.
