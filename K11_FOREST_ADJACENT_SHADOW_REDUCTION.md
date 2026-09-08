# Exact adjacent-shadow compression of the unrestricted `k=11` forest formula

## Verdict

The adjacent-shadow theorem does give a globally-WLOG compression; it does
**not** require adding full rank-four and rank-seven monotone schedules.
The guarded implementation is in `k11_forest_sat.cpp` and is enabled by

```text
K11_FOREST_ADJACENT_SHADOWS=1
```

With the option disabled, the previously audited formula is byte-for-byte
unchanged at the clause-generation level.  With it enabled, the formula is
still satisfiable if and only if a universal nonzero 11-bit array of length
465 exists, and its external inventory is

```text
variables = 3,148,302
clauses   = 14,546,194
```

The previous forest formula had 4,892,622 variables and 15,524,818 clauses.
Thus this one theorem removes 1,744,320 variables (35.65 percent) and 978,624
clauses, without a fixed-row, Hamilton-path, Johnson-adjacency, or chosen
exception assumption.

## 1. Why there are only six exceptions in each layer

Fix the already-selected rank-five witness family and independently select one
witness for every rank-four mask.  In either rank the left endpoints are
distinct.  The rank-four and rank-five endpoint sets have sizes 330 and 462
inside 465 physical positions, so they have at least

\[
 330+462-465=327
\]

common left endpoints.  The same holds on the right.  Therefore at least

\[
 327+327-330=324
\]

rank-four masks have both a common-left and a common-right flag through rank
five.  At most six do not.

For such a crossed rank-four witness `J=[l,r]`, its two selected rank-five
neighbors have intervals

```text
[l,x] with x>r,       [y,r] with y<l.
```

Every rank-five witness has length at most three, because every interval of
length at least four contains a selected rank-six witness.  Hence `J` has
length at most two.  This proves that every nonexceptional rank-four target is
represented by one of only

\[
 465+464=929
\]

physical intervals.

The dual count uses the selected rank-six and rank-seven witnesses.  Again at
least 324 rank-seven masks are crossed.  For a crossed witness `J=[l,r]`, its
rank-six neighbors are a proper prefix and suffix,

```text
[l,x] with x<r,       [y,r] with y>l.
```

Their masks are distinct six-subsets of the seven-set target, so their union
is the target.  The rank-seven interval can have length as large as the safe
bound 136; this is why rank seven uses endpoint comparisons rather than an
enumeration of all physical candidates.

These arguments hold for **every** choice of the central selected witnesses.
They therefore compose with the existing unrestricted monotone-band rows and
do not turn them into a fixed derivative row.

## 2. Six generic exception slots

For each of ranks four and seven, the formula creates six generic exact
witness slots.  A slot selects an arbitrary interval within the proved safe
bound, materializes its eleven-bit OR, constrains its cardinality, and chooses
one target of that rank.  Exact cardinality means two distinct same-rank
target flags cannot be simultaneously true, so one positive target clause per
slot is already exact-one.

Each target coverage clause says either:

* it has a certified crossed witness; or
* one of the six generic slots represents it.

Six slots can cover at most six distinct exceptional targets.  Repeated flags
are harmless, so a solution with fewer than six exceptions can fill the
remaining slots with arbitrary already-covered targets.  This is an exact
"at most six" encoding without guessing the exceptional set.

## 3. Rank-four shared short strip

For each singleton or adjacent-pair interval `J`, the generator materializes
its OR bits once.  A target flag `Q[J,S]` implies:

1. the interval OR has cardinality at most four;
2. all four bits of `S` occur, hence the OR is exactly `S`;
3. a selected rank-five interval begins with `J`'s left endpoint and extends
   strictly past its right endpoint;
4. another selected rank-five interval ends with `J`'s right endpoint and
   starts strictly before its left endpoint.

The two endpoint conditions are clauses over the existing ten-state central
schedule variables.  No new rank-four schedule is introduced.  There are
929 times 330 = 306,570 target flags.

Soundness is immediate from item 2: every asserted target is the physical OR
of `J`.  Items 3--4 are redundant witnesses of the theorem's crossed geometry
and supply propagation.  Completeness follows by assigning the at least 324
crossed rank-four selected witnesses and using the six generic slots for the
rest.

## 4. Rank-seven endpoint comparison

For the selected rank-six row, introduce the summaries

```text
B[l,d]  iff the selected interval beginning at l is [l,l+d],
E[r,d]  iff the selected interval ending at r is [r-d,r],
```

for `0<=d<=3`.  Each definition is a bidirectional disjunction of the
existing schedule-state variables; it cannot guess a nonexistent central
interval.

For every rank-seven target `S`, an activation bit guards one unary interval
`J=[l,r]` of length at most 136.  When active, the clauses require:

```text
some B[l,d] with l+d<r,
some E[r,e] with r-e>l,
no bit outside S at any position of J.
```

The first two central intervals lie physically inside `J`, so their rank-six
masks are subsets of `S`.  They are distinct: one has left endpoint `l` but
not right endpoint `r`, while the other has right endpoint `r` but not left
endpoint `l`; the central row is a permutation.  Two distinct six-subsets of
a seven-set have union exactly that seven-set.  Hence every bit of `S` occurs
inside `J`; the negative-bit clauses then prove `OR(J)=S`.  Positive-bit
occurrence variables are unnecessary.

The comparison is represented in unary form:

```text
selected left=l and B[l,d]  => selected right >= l+d+1,
selected right=r and E[r,d] => selected left  <= r-d-1.
```

There are 330 times 2 times 465 times 4 = 1,227,600 such local comparison
clauses.  This is substantially cheaper in variables than retaining seven
positive-bit occurrence arrays for every target.

## 5. Exactness theorem

### Theorem

With `K11_FOREST_ADJACENT_SHADOWS=1`, `k11_forest_sat.cpp` is satisfiable if
and only if a universal nonzero 11-bit array of length 465 exists.

### Soundness

Ranks other than four and seven retain the previously audited exact encoding.
Every generic exception slot is an exact physical witness.  Every rank-four
shadow flag fixes the OR of its one- or two-position interval to its target.
Every active rank-seven interval contains two distinct selected rank-six
subsets whose union is its target and excludes every outside bit.  The target
coverage clauses cover all 330 masks in each replaced layer.  Therefore every
nonzero mask occurs as a contiguous-subarray OR.

### Completeness

Start with any universal length-465 array and choose the two central witness
families represented by the existing band rows.  Choose witnesses in ranks
four and seven.  The endpoint-intersection count above makes at least 324
targets crossed in each layer.  Assign those targets to their crossed
physical intervals and put the at most six remaining targets in the generic
slots.  All guarded clauses are then satisfied.  Thus no genuine optimum is
removed.

## 6. Independent inventory and verifier

The optional formula contains the following external variables:

```text
array bits                                      5,115
direct ranks 1,2,3,8,9,10,11               1,832,565
two central band rows                           446,292
twelve generic exception slots                   82,212
rank-four shared short strip                     317,718
rank-seven activated intervals                   460,680
rank-six endpoint/length summaries                 3,720
                                               ---------
total                                          3,148,302
```

The new clause categories are:

```text
generic exception slots                         246,246
rank-four shadow strip                        2,601,060
rank-six endpoint summaries                      12,960
rank-seven crossed intervals                  3,024,780
```

Together with the retained direct and central categories these total
14,546,194 clauses.

`scratch/verify_k11_forest_adjacent.cpp` independently checks the layer
sizes, safe bounds, all interval-geometry implications, all 6,930 unordered
rank-six pairs inside rank-seven targets, and the complete variable/clause
inventory.  Compile and run it with:

```text
g++ -O3 -std=c++20 scratch/verify_k11_forest_adjacent.cpp \
    -o scratch/verify_k11_forest_adjacent
scratch/verify_k11_forest_adjacent
```

Its expected final line is:

```text
variables=3148302 clauses=14546194
```

For a real CaDiCaL build-only reconstruction, use the same environment option
together with `K11_FOREST_BUILD_ONLY=1`.  Proof and DIMACS hooks remain in
their original positions and are unaffected by this guarded reduction.
