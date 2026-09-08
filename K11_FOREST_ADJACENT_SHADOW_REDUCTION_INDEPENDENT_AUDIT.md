# Independent audit of the `k=11` adjacent-shadow forest reduction

## 1. Scope and verdict

This is an independent audit of:

* `K11_FOREST_ADJACENT_SHADOW_REDUCTION.md`;
* the `K11_FOREST_ADJACENT_SHADOWS` branch of `k11_forest_sat.cpp`;
* `scratch/verify_k11_forest_adjacent.cpp`.

I did not use `K11_FOREST_ADJACENT_SHADOW_REDUCTION_AUDIT.md` as evidence.
The exact composed source audited here has SHA-256

```text
0a3db930fc343589fd9840b042a896c2b428459de6c3e3203ed45d676d10b9bc  k11_forest_sat.cpp
```

and throughout this audit `K11_FOREST_BAND_CUTS=0`.  Thus the separately
guarded band-cut construction is outside the logical scope of this report.

**Verdict: pass.**  The adjacent-shadow reduction is globally WLOG.  With

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_BAND_CUTS=0
```

the frozen formula is satisfiable if and only if a universal nonzero
eleven-bit array of length 465 exists.  I found no lost witness family,
off-by-one error, polarity error, variable overlap, or false fixed-row
assumption.  The exact external inventory is

```text
variables = 3,148,302
clauses   = 14,546,194
```

The supplied checker reproduces these numbers, but it is important to state
its scope accurately: it is an independent combinatorial and arithmetic
checker, not a parser or evaluator of the generated CNF.  The source-level
claims below were therefore checked separately against the frozen source.

## 2. The globally WLOG endpoint theorem

Select one interval for every mask of a fixed rank.  Two selected intervals
of that rank cannot share a left endpoint or a right endpoint: sharing one
endpoint makes the intervals nested, and interval containment makes their OR
masks comparable, whereas distinct masks of the same rank are incomparable.
The endpoint sets therefore have the same size as the corresponding Boolean
layer.

### Rank four through rank five

Let `L_4,L_5` be the selected left-endpoint sets.  They are subsets of the 465
physical positions of sizes 330 and 462.  Hence

\[
 |L_4\cap L_5|\ge330+462-465=327.
\]

At least 327 selected rank-four masks are left-good.  The same calculation
for right endpoints makes at least 327 right-good.  These are two subsets of
the 330 rank-four masks, so at least

\[
 327+327-330=324
\]

rank-four masks are simultaneously good on both sides.  Thus at most six are
exceptions.

If a crossed rank-four witness is `J=[l,r]`, its common-left rank-five witness
must be `[l,x]` with `x>r`: `x<=r` would put a rank-five OR inside a rank-four
OR (or make the physical intervals equal).  Dually, its common-right
rank-five witness is `[y,r]` with `y<l`.

Every rank-five witness in a length-465 array has length at most three.  This
is the rank-six interval-slack consequence: after selecting and sorting all
462 rank-six witnesses, the `i`-th lies in `[i,i+3]`, so every physical
interval of length at least four contains one of them and has rank at least
six.  Therefore `[l,x]` has `x<=l+2`.  Since `r<x`, one has `r<=l+1`, and
`J` has length at most two.  The complete physical candidate set is exactly

\[
 465+464=929
\]

singletons and adjacent pairs.

### Rank six through rank seven

The identical endpoint count for sizes 462 and 330 shows that at least 324
selected rank-seven masks are crossed and at most six are exceptions.

For a crossed rank-seven witness `J=[l,r]`, the rank-six interval sharing its
left endpoint must be a proper prefix `[l,x]`, `x<r`; the one sharing its
right endpoint must be a proper suffix `[y,r]`, `y>l`.  Their physical ORs
are rank-six subsets of the rank-seven OR of `J`.  The two selected rank-six
intervals are different.  Moreover, the selected rank-six row is a
permutation of the 462 masks: every mask is required in one of 462 exact-rank
slots, and one slot cannot support two distinct rank-six masks.  Consequently
the two rank-six subsets are distinct, and two distinct six-subsets of one
seven-set have union equal to that seven-set.

This argument is about arbitrary selected witness families in an arbitrary
universal length-465 array.  It does not assume a fixed derivative row,
Johnson path, Hamilton path, or a preselected exceptional set.

The generic bounds used by the source are also sufficient.  Rank four has
safe bound three (in fact its crossed witnesses have length at most two), and
sorting one witness for each of the 330 rank-seven masks gives every selected
rank-seven witness length at most

\[
 465-330+1=136.
\]

Thus the particular crossed witnesses used in the completeness proof fit the
encoded domains.

## 3. Six generic exception slots are exact

Lines 435--457 allocate six independent slots for each of ranks four and
seven.  Lines 689--760 encode them.

For each slot, the `L`, `R`, and `Inside` threshold clauses select one
nonempty contiguous interval of length at most the safe bound.  For every bit
`b`, the clauses have the exact meaning

\[
 \texttt{value[b]}\iff\bigvee_{p\in J}A_{p,b}.
\]

The forward direction uses an occurrence variable `H[b,p]`; the reverse
direction is `Inside[p] AND A[p,b] => value[b]`.  The two families of subset
clauses force the value to have exactly the requested rank.

A target flag `q_S` implies all bits of `S` in `value`.  Since both sets have
the same rank, this gives `value=S`.  Two distinct same-rank flags cannot both
hold, even though pairwise at-most-one clauses are omitted.  The positive
clause over all target flags therefore makes every slot choose exactly one
target.

If fewer than six targets are exceptional, unused slots may repeat any target
of the layer and any bounded witness for it.  Conversely, six slots can name
at most six distinct exceptional targets.  Hence this is an exact encoding of
"at most six", not merely a relaxation.

All relevant polarities are correct:

```text
-H or Inside                    H => position is in J
-H or A                         H => the bit occurs there
-Inside or -A or value          occurrence in J => value bit
-value or H_0 or ... or H_464   value bit => some occurrence
-q_S or value[b]                q_S => S subset value
```

## 4. Rank-four shared strip

Lines 462--472 allocate exactly 929 physical intervals.  Lines 767--821 encode
their shared OR bits and target flags.

For each interval and bit, lines 768--775 encode `value[b]` exactly as the OR
of that physical singleton or pair.  The conditional five-subset clauses at
lines 778--782 enforce rank at most four whenever `at_most_four` is true.
For a target flag `q_S`, the clauses then impose:

* `at_most_four`;
* the four bits of `S` in `value`;
* one selected rank-five interval with the same left endpoint and a strictly
  larger right endpoint;
* one selected rank-five interval with the same right endpoint and a strictly
  smaller left endpoint.

The first two bullets and exact physical OR materialization prove
`OR(J)=S`.  The two extension clauses are safe redundant propagation: in the
completeness assignment they are supplied by the crossed witnesses proved in
Section 2.  Empty extension lists correctly reduce to `-q_S`.

No explicit at-most-one target clause is needed here either.  Two different
rank-four flags would force at least five distinct value bits while
`at_most_four` is true.

Every target coverage clause contains all 929 strip flags and the six generic
slot flags.  Thus all rank-four masks are covered, and at most six may avoid
the certified crossed geometry.

## 5. Rank-six endpoint summaries and rank-seven logic

Lines 488--495 allocate

```text
B[l,d]  for a selected rank-six interval [l,l+d],
E[r,d]  for a selected rank-six interval [r-d,r],
```

for `0<=d<=3`.  Lines 826--846 define each summary bidirectionally:

```text
-B[l,d] or z_1 or ... or z_t    B => some matching schedule state
-z or B[l,d]                    matching state => B
```

and dually for `E`.  All ten rank-six schedule states have length at most
four, so the four values of `d` are exhaustive.  Monotonicity of the schedule
makes selected left and right endpoints unique, although the OR definitions
would remain logically sound without relying on uniqueness.

For each rank-seven target, lines 857--858 select a nonempty interval `J` of
length at most 136.  The interval exists even when `active` is false; only the
shadow conditions are guarded.  This is harmless and leaves a completion for
exceptional targets.

The threshold meaning is:

```text
L(p) = true  iff p >= left(J),
R(p) = true  iff p <= right(J).
```

Thus exact left endpoint `l` is detected by `L(l) AND NOT L(l-1)`, with the
obvious boundary convention.  Lines 867--881 say:

1. if active and the exact left endpoint is `l`, some `B[l,d]` is true;
2. if that `B[l,d]` is true, `R(l+d+1)` must be true, so
   `right(J)>=l+d+1` and `[l,l+d]` is a proper prefix.

The out-of-range case omits `R(l+d+1)` and therefore correctly forbids that
choice.  Lines 883--898 are the exact dual: an `E[r,d]` at the selected right
endpoint forces `L(r-d-1)`, hence `left(J)<=r-d-1` and a proper suffix.

The four bits outside the target are forbidden at every position of an active
`J`.  Its proper rank-six prefix and suffix are therefore two distinct
six-subsets of the target.  Their union is the target, so all seven positive
bits occur in `J`; explicit positive occurrence arrays are unnecessary.
It follows that an active interval has OR exactly the target.

The polarity audit of the two central comparison clauses is:

```text
-active or -L(l) or -B[l,d] or L(l-1) or R(l+d+1)
-active or -R(r) or -E[r,d] or R(r+1) or L(r-d-1)
```

At the exact endpoint, the predecessor/successor threshold literal is false,
leaving precisely the required strict containment literal.  At every other
endpoint the clause is vacuous.  The signs are therefore correct.

Finally, `active OR exception_1 OR ... OR exception_6` covers each rank-seven
target.  Since each exception slot names only one target, at least 324 targets
must be active, exactly as the WLOG theorem permits.

## 6. Full soundness and completeness

### Soundness

Ranks other than four and seven retain the exact direct or central encoding.
Section 3 proves every exception-slot flag is an exact physical witness.
Section 4 proves every rank-four strip flag is an exact physical witness.
Section 5 proves every active rank-seven interval is an exact physical
witness.  The two replacement-layer coverage clauses therefore cover all
330 masks of each rank.  Hence every SAT model gives a universal nonzero
length-465 array.

### Completeness

Start with any universal nonzero length-465 array.  Choose and sort witnesses
for ranks five and six to populate the existing monotone central schedules.
Choose bounded witnesses for ranks four and seven.  Section 2 makes at least
324 selected targets crossed in each of those layers.  Assign their actual
intervals to the strip/active encodings and assign the remaining at most six
targets to the six generic slots.  Fill surplus generic slots by repeating
bounded witnesses.  All target, endpoint, OR, and guard clauses are then
satisfied.  Therefore no genuine length-465 solution is removed.

## 7. Independent inventory

The variable count follows directly from the frozen allocation loops:

```text
array bits                                             465*11 =       5,115
direct ranks 1,2,3,8,9,10,11                         =   1,832,565
two central schedules                 2*462*(10+11+462) =     446,292
12 generic slots                    12*(3*465+11+11*465+330) = 82,212
rank-four strip                       929*(1+11+330) =     317,718
rank-seven active intervals             330*(1+3*465) =     460,680
rank-six endpoint summaries                  2*465*4 =       3,720
                                                               ---------
                                                               3,148,302
```

There are 463 direct targets.  Deriving the direct count rank by rank gives
4,771,277 clauses.  The retained central/forest categories contribute

```text
nonzero entries                                             465
rank-five central slots                               1,607,298
rank-six central slots                                1,820,280
monotone state transitions                               46,100
central target coverage                                      924
endpoint-forest propagation                              414,804
                                                        ---------
                                                        3,889,871
```

The new categories are:

```text
12 generic exception slots                              246,246
rank-four strip                                       2,601,060
rank-six endpoint summaries                              12,960
rank-seven active intervals                           3,024,780
```

Therefore

\[
 3,889,871+4,771,277+246,246+2,601,060+12,960+3,024,780
 =14,546,194.
\]

As a second arithmetic check, the two removed direct layers had 6,863,670
clauses and the replacement has 5,885,046, a reduction of 978,624 from the
audited parent count 15,524,818.  The corresponding variable reduction is
2,608,650 minus 864,330, namely 1,744,320.

Compiling the supplied checker with

```text
g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
    scratch/verify_k11_forest_adjacent.cpp \
    -o /tmp/verify_k11_forest_adjacent_independent
/tmp/verify_k11_forest_adjacent_independent
```

produced

```text
PASS k11 adjacent-shadow reduction
rank4_candidates=929 rank4_target_flags=306570
rank7_pair_types=6930 rank7_endpoint_comparisons=1227600
variables=3148302 clauses=14546194
```

A real CaDiCaL build-only reconstruction of the exact frozen source, with
`K11_FOREST_ADJACENT_SHADOWS=1` and `K11_FOREST_BAND_CUTS=0`, independently
reported

```text
variables=3148302 clauses=14546194 direct_targets=463
exact_direct_phase=462/463 exact_central_phase=1,1
forest_cases_LR=46092,46092
adjacent_shadows=1 band_cuts=0
shadow4_candidates=929 shadow4_flags=306570
shadow7_comparisons=1227600 exception_slots=6,6
```

The phase counts depend only on the supplied phase seed and are not clauses.
The structural and inventory fields exactly match the independent derivation.

The checker correctly verifies the layer sizes, safe bounds, candidate and
pair counts, and inventory arithmetic.  Its rank-four geometry loop samples
all geometries already satisfying the proper-extension length restrictions;
the universal implication that these restrictions force length at most two
is supplied by the algebra in Section 2, not by that loop alone.  It also
copies the retained central/forest subtotal and does not inspect source clause
polarity, guard-off behavior, or proof-hook placement.  These are limitations
of the checker, not errors in the reduction.

## 8. Guard-off identity

With `K11_FOREST_ADJACENT_SHADOWS` unset or equal to `0`:

* lines 382 and 426 leave ranks four and seven in the original direct target
  list;
* no exception, strip, active-target, or endpoint-summary variable is
  allocated;
* the entire replacement clause block at lines 688--905 is skipped;
* the central schedules and final forest block retain their original variable
  numbering and clause order.

With `K11_FOREST_BAND_CUTS=0`, `band_cut_plan` is null at lines 498--499 and
adds neither variables nor clauses at lines 523--525.  The class definition
itself has no runtime effect.  Therefore the guard-off external formula is the
parent forest formula: 4,892,622 variables and 15,524,818 clauses.  The extra
environment reads and diagnostic fields do not enter the CNF.

## 9. Proof and certificate hooks

The proof hooks remain correctly placed in the frozen source.

* `trace_proof` is called at lines 506--509 after external-variable
  declaration but before the first clause is submitted.  Failure to open the
  proof returns code 6 rather than silently continuing.
* Every adjacent-shadow clause uses the same two clause helpers as the parent
  formula, so it is included in both the solver and proof stream.
* `write_dimacs` is called only after all adjacent-shadow and forest clauses
  have been emitted and before build-only return or solving.  It is passed
  `variable_total`, preserving all declared external variables in the header;
  a write error returns code 7.
* A SAT result writes only the 465 array masks.  It must still be checked by
  the independent exhaustive and suffix-OR verifiers.  An UNSAT result must
  still be promoted only with an independently verified proof against the
  matching DIMACS file.  The hooks make those certificates possible; they do
  not replace external certificate checking.

## 10. Final conclusion

Conditioning away the orthogonal band cuts, the adjacent-shadow compression is
an exact globally-WLOG reduction of the unrestricted `k=11,n=465` problem.
Its central insight is valid on arbitrary selected witness schedules: only six
targets in each of ranks four and seven can evade the two-sided adjacent flag.
The frozen CNF encodes the 324 forced targets and six generic exceptions with
the correct interval geometry and polarities, and its claimed size and proof
hooks check out.
