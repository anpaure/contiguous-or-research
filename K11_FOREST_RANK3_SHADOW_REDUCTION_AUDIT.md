# Independent audit of the proposed `k=11` rank-three shadow reduction

## Verdict

The mathematical reduction in `K11_FOREST_RANK3_SHADOW_REDUCTION.md` is
sound and complete.  I rebuilt the endpoint argument, the shortness theorem,
the six-exception encoding, and the inventory without assuming the note's
proof, and found no counterexample.

The exact conclusion is:

> Conditional on the already-audited adjacent-shadow forest formula, its 165
> direct rank-three blocks may be replaced by the proposed crossed-short-strip
> encoding plus six generic exact slots without changing satisfiability.

The projected inventory

```text
variables = 2,885,308
clauses   = 14,360,485
```

is arithmetically exact relative to the frozen adjacent-shadow plus band-cut
inventory `3,151,328/14,554,555`.

There is one important status qualification.  The rank-three replacement is
not present in the frozen `k11_forest_sat.cpp` audited here.  Therefore these
are exact **projected** totals, not a generated-CNF inventory.  The standalone
checker verifies the combinatorial and inventory arithmetic but cannot prove
that a future implementation matches the design.  A real guarded generator,
build-only count, source audit, and ultimately the normal SAT/UNSAT certificate
checks remain necessary after implementation.

Frozen artifacts inspected:

```text
k11_forest_sat.cpp SHA-256
0a3db930fc343589fd9840b042a896c2b428459de6c3e3203ed45d676d10b9bc

K11_FOREST_RANK3_SHADOW_REDUCTION.md SHA-256
7cdf889bb00b183c633f6db5c8bf7b403fba74ca7e678abfbb03fade1a3543f0

scratch/verify_k11_forest_rank3_shadow.cpp SHA-256
c9d6d76621e5eaa2640f21723fa4c7355862e37ff090a1fd8b9622a4db208e43
```

## 1. Endpoint count rebuilt from first principles

Choose one exact witnessing interval for each rank-three target and one for
each rank-five target in an arbitrary universal nonzero array of length 465.

Within any fixed rank, the chosen left endpoints are distinct.  If two
distinct equal-rank targets had the same left endpoint, their two intervals
would be nested.  Containment of physical intervals implies containment of
their OR masks; two different sets of the same cardinality cannot contain one
another.  The same argument proves that the right endpoints are distinct.

Consequently the rank-three and rank-five left-endpoint sets have sizes 165
and 462 inside a 465-element universe.  Their intersection has size at least

```text
165+462-465 = 162.
```

The two right-endpoint sets also intersect in at least 162 positions.  Index
these properties by the 165 chosen rank-three witnesses.  At least 162 have a
rank-five witness sharing their left endpoint, and at least 162 have one
sharing their right endpoint.  Inclusion-exclusion within those 165 targets
gives

```text
162+162-165 = 159
```

witnesses having both endpoint flags.  Thus at most six are exceptions.

No correlation between the independently selected rank-three and rank-five
families was assumed.  The bound is also set-theoretically tight at this
level: the three failures on the left and the three failures on the right may
be disjoint, leaving exactly 159 doubly flagged targets.  Therefore reducing
the generic reserve below six would require an additional theorem.

## 2. Why every crossed witness has length at most two

This is the step most likely to hide a fixed-row assumption, so I checked it
independently.

### 2.1 The global rank-five length bound

Independently choose one witness for each of the 462 rank-six masks and sort
them by left endpoint.  The equal-rank nonnesting theorem orders their right
endpoints in the same direction.  With `n=462+3`, the standard band argument
places the `i`th selected interval inside

```text
[i,i+3].
```

Every physical interval `[a,b]` of length at least four has `a<=462` and
contains `[a,a+3]`, hence contains the selected rank-six witness indexed by
`a`.  Its OR therefore has rank at least six.  An exact rank-five witness can
never have length four or more.

Thus **every** selected rank-five witness in every universal length-465 array
has physical length at most three.  This uses only the unrestricted rank-six
antichain and interval geometry; it does not assume `T=D^3 A`, a Johnson path,
or a fixed central row.

The frozen forest formula implements precisely this WLOG fact.  Its rank-five
monotone schedule has states `(alpha,beta)` with `0<=alpha<=beta<=3`, and the
clause

```text
not state(0,3)
```

forbids the only state of width three.  Hence every selected rank-five
interval in the formula has width at most two, i.e. length at most three.
The independently recomputed safe-bound table also gives

```text
safe_bound(3)=3,
safe_bound(5)=3,
safe_bound(6)=4.
```

### 2.2 Proper extension of the rank-three interval

Let the crossed rank-three witness be `J=[l,r]`.  Let its same-left
rank-five witness be `[l,x]`.  If `x<r`, the rank-five interval is contained
in `J`, forcing a five-set OR to be a subset of a three-set OR.  If `x=r`,
the same physical interval would have two different OR values.  Both are
impossible, so `x>r`.

Since `[l,x]` has length at most three,

```text
x<=l+2 and r<x,
```

which implies `r<=l+1`.  Therefore `J` is a singleton or adjacent pair.  The
same-right rank-five witness is dually a proper extension `[y,r]` with
`y<l`.  Both proper extensions required by the proposed clauses really exist.

This proves that at least 159 rank-three masks have crossed witnesses among
the exact set of

```text
465+464 = 929
```

singleton and adjacent-pair intervals.

## 3. Audit of the projected short-strip clauses

The proposal composes with `K11_FOREST_ADJACENT_SHADOWS=1`.  In the frozen
solver, every one of the 929 short intervals already has eleven materialized
bits, and the existing clauses make each bit equivalent to the physical OR
of that interval.  These bits can therefore be reused without new OR-bit
variables or clauses.

For a short interval `J`, the proposed gate `G_J` has one clause for every
four-coordinate subset:

```text
G_J -> not(all four OR bits).
```

The 330 clauses are exactly the condition `|OR(J)|<=3` when `G_J` is true.
For a rank-three target `S`, `Q[J,S]` implies `G_J` and the three target OR
bits.  Hence

```text
S subseteq OR(J) and |OR(J)|<=3=|S|,
```

so `OR(J)=S`.  This establishes soundness independently of the endpoint
extension clauses.  It also means two flags for distinct rank-three targets
cannot simultaneously use one physical interval; explicit pairwise clauses
are unnecessary.

The two remaining `Q[J,S]` clauses are disjunctions of existing rank-five
schedule states:

* one selected interval has left endpoint `left(J)` and a strictly larger
  right endpoint;
* one selected interval has right endpoint `right(J)` and a strictly smaller
  left endpoint.

The frozen schedule gives every slot exactly one state and has strictly
increasing physical endpoints.  Thus these disjunctions cannot fabricate a
rank-five extension.  If a boundary interval has no legal extension, its
disjunction is empty and the resulting unit clause simply forbids that short
flag.  Every genuinely crossed witness from Section 2 appears in both lists,
which proves completeness of the short side.

## 4. Six generic slots are sound and complete

Each generic slot uses the same exact threshold/inside encoding as the frozen
exception slots, with safe bound three.  It materializes eleven value bits
equivalent to the OR of its chosen nonempty contiguous interval, constrains
that value to have exactly three bits, and has one flag per rank-three target.

A target flag forces its three bits into the exact rank-three value, so it
fixes the value to that target.  Two distinct rank-three flags would force a
union of at least four bits and are therefore incompatible.  The one positive
target clause is consequently exact-one even without pairwise target clauses.

For soundness, every generic flag is thus an ordinary exact physical witness.
For completeness, assign the at most six noncrossed targets to the six slots.
If fewer than six are needed, duplicate any already represented rank-three
target and its witness in the unused slots; slots are not required to use
distinct targets or intervals.

Conversely, six exact-one slots can cover at most six distinct targets.  Hence
the combined target clauses cannot conceal a seventh target missing from the
short strip.  This is an exact encoding of “at most six exceptions,” not a
guess of their identities.

## 5. Independent inventory reconstruction

### 5.1 Removed direct rank-three layer

For each of 165 direct targets, the frozen formula allocates three 465-entry
endpoint/inside arrays and one 465-entry occurrence array for each of the
three present bits:

```text
variables per target = 6*465 = 2,790.
```

Its clauses per target are

```text
threshold/inside and bound-3 clauses  2,788
eight absent-bit position clauses     8*465 = 3,720
three present-bit occurrence blocks   3*(2*465+1) = 2,793
                                      -----------------
                                      9,301.
```

Therefore removal subtracts

```text
variables  165*2,790 =   460,350
clauses    165*9,301 = 1,534,665.
```

### 5.2 Added exact replacement

One generic rank-three slot has

```text
variables = 3*465 + 11 + 11*465 + 165 = 6,686
clauses   = 2,788 + 11*(3*465+1)
            + C(11,4)+C(11,9) + 165*3 + 1
          = 19,025.
```

The complete replacement is therefore

| category | variables | clauses |
|---|---:|---:|
| six generic slots | 40,116 | 114,150 |
| 929 at-most-three gates | 929 | 306,570 |
| `929*165` short target flags | 153,285 | 919,710 |
| target coverage | 0 | 165 |
| **total added** | **194,330** | **1,340,595** |

Each short target flag contributes exactly six clauses: gate, three target
bits, proper-left extension, and proper-right extension.  Empty endpoint
lists do not change the count; they produce a unit clause.

The net saving is exactly

```text
variables  460,350-194,330   = 266,020
clauses    1,534,665-1,340,595 = 194,070.
```

Subtracting this from the independently audited adjacent-shadow plus band-cut
formula gives

```text
variables  3,151,328-266,020 = 2,885,308
clauses    14,554,555-194,070 = 14,360,485.
```

The supplied checker compiled with `g++ -O3 -std=c++20` and reported

```text
rank3=165 rank5=462 common_each_side=162 crossed=159 exceptions=6
old_variables=460350 old_clauses=1534665
new_variables=194330 new_clauses=1340595
saved_variables=266020 saved_clauses=194070
projected_total_variables=2885308 projected_total_clauses=14360485 PASS
```

I independently recomputed every displayed number above.  The checker is a
useful arithmetic regression test, but it contains only `static_assert`s and
does not parse `k11_forest_sat.cpp`, generate CNF, test truth tables, or inspect
the endpoint clauses.  Its `PASS` must not be misreported as implementation or
SAT certification.

## 6. Counterexample stress tests

I checked the natural ways the argument could fail:

* **Repeated same-rank endpoints.**  They force nested intervals and hence
  comparable equal-cardinality masks, so they cannot occur for distinct
  targets.
* **A same-left rank-five interval ending inside `J`.**  It would put a
  five-set OR inside a three-set OR and is impossible; equality of intervals
  is impossible for the same reason.
* **A length-four rank-five extension.**  Every length-four interval contains
  a selected rank-six witness in the unrestricted `n=462+3` band, so its OR
  has rank at least six.
* **One short interval covering two targets.**  Its physical OR is unique, and
  the at-most-three gate plus either target's three forced bits fixes it
  exactly.
* **One generic slot covering two targets.**  two distinct three-sets have
  union of size at least four, contradicting the exact-rank-three clauses.
* **Fewer than six real exceptions.**  Repeated target assignments fill the
  spare generic slots without changing the array.
* **A boundary short interval with a fictitious extension.**  The extension
  list is built only from exact physical central states; an empty list forces
  the corresponding `Q` false.

None yields a counterexample.

## 7. Exact scope

The rank-three shadow theorem is globally WLOG within the unrestricted
length-465 forest formulation.  It assumes the already-proved rank-five and
rank-six monotone witness schedules and reuses the exact short-interval OR
bits supplied by the adjacent-shadow guard.  It does not assume a fixed
derivative row, Hamilton path, Johnson adjacency, central connectivity, or a
preselected exceptional family.

It proves no SAT or UNSAT result.  Before the projected totals may be called a
real formula inventory, the reduction must be implemented behind a guard and
audited against the generated clauses.  Any future SAT array still requires
both independent OR verifiers; any future UNSAT theorem still requires a
frozen CNF/proof pair and independent proof verification.
