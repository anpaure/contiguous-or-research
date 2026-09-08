# Independent audit: next Type-I boundary-face hierarchy

## Verdict

**PASS as a theorem package and as a proposed incremental CNF design.**

The audit was made against

```text
e47329f65ecf049a0b5ef92629c019ad691524e47cef1a844f5653a09b66e97e
  K11_TYPE1_FACE_HIERARCHY_NEXT.md
afd4360f7fb909fa74e03dcd2e9aaf669b383710ea77dda7d1f271dd80189784
  scratch/check_k11_type1_face_hierarchy_next.py
```

The three new necessary inequalities are correct:

```text
s_Q >= 5                                      (|Q|=3),
c_1 >= 6,  c_1+2*c_2 >= 30                    (inside T=63),
n_1+2*n_2 >= 110                              (all coordinates).
```

The three advertised incremental inventories also reproduce exactly:

```text
twenty endpoint triple rows:  27,680 variables / 165,960 clauses,
endpoint pair profile:         2,788 variables /  15,810 clauses,
global pair profile:           1,864 variables /  13,053 clauses.
```

These are redundant propagation lemmas for the exact Type-I formula, not a
SAT/UNSAT result.

## 1. Common core and the three-face threshold

In the exact Type-I peel, the rank-at-most-four core has length `q+2` and
contains selected witnesses for the `q` nonliteral rank-five masks.  Ordering
those witnesses gives

```text
I_i subseteq [i,i+2].
```

Therefore every core interval of length at least three contains a rank-five
witness.  A run of entries that are proper subsets of a fixed set of rank at
most four consequently has length at most two.

For a triple `Q`, let `a_Q` and `b_Q` count its rank-one and rank-two strict
support positions.  The three singleton targets give `a_Q>=3`.  A rank-two
target either has a literal rank-two occurrence or is represented by an
adjacent pair of its two atoms.  Distinct atom-pair witnesses cannot overlap:
two overlapping adjacent pairs would be three consecutive singleton entries,
contradicting the preceding core fact.  Hence

```text
b_Q+floor(a_Q/2) >= 3.
```

For integers this is equivalent to `a_Q+2*b_Q>=6`, and minimizing
`a_Q+b_Q` subject to `a_Q>=3` gives five.

The checker's four-position exhaustion is complete.  With four strict
positions, covering six proper targets requires all six available cells, so
the run partition is forced to be `2+2`; all other run partitions have at
most five cells.  Exhausting the two two-position runs therefore covers the
only capacity-tight case.  The displayed five-position gadgets verify local
sharpness.  As the theorem note now states, this is sharp for the isolated
face/run problem, not a proof that a complete Type-I word can attain five at
a prescribed triple.

## 2. Endpoint and global pair profiles

The same disjointness argument is valid over the six coordinates of `T` and
over all eleven coordinates.  In Type I all rank-one and rank-two entries lie
inside `C_4`.  A pair target without a literal rank-two occurrence must use
an adjacent pair of atoms, and the atom-pair witnesses for distinct targets
form a matching.  Thus

```text
c_2+floor(c_1/2) >= C(6,2)=15,
n_2+floor(n_1/2) >= C(11,2)=55.
```

Parity makes these exactly equivalent to

```text
c_1+2*c_2 >= 30,
n_1+2*n_2 >= 110.
```

The endpoint construction with six atoms, three atom pairs, and twelve
literal pair values attains `(c_1,c_2)=(6,12)`.  The global construction with
twelve atom occurrences in six distinct atom pairs and the other 49 pair
values literal attains `(n_1,n_2)=(12,49)`.  Both are valid sharpness examples
for the isolated rank-one/rank-two target system.  Neither is asserted to
satisfy all Type-I core constraints.

The incidence comparisons are also correct.  Summing the twenty endpoint
triple rows gives `10*c_1+4*c_2>=100`; the endpoint pair profile together
with `c_1>=6` gives the stronger aggregate value 108.  Summing all 165 triple
rows gives `45*n_1+9*n_2>=825`, hence `5*n_1+n_2>=92`, already weaker than
the current cumulative rank rows.

## 3. Gate semantics and exact inventories

For an endpoint triple `Q=T\{b,c,d}`, a retained ridge literal already means

```text
i in C_4,  A[i] subseteq T\{b,c},  |A[i]|<=3.
```

Conjoining it with `!A[i,d]` gives containment in `Q`; conjoining with the
exact `!rank3[i]` flag excludes the only contained nonproper value.  The
proposed three-input equivalence therefore denotes precisely the strict
triple support.

The production Wallace convention uses 452 compressor full adders and an
eight-stage final ripple for 464 inputs, or 460 full adders total.  For 465
inputs it uses 453 compressors and the same eight-stage ripple, or 461 full
adders.  Every full adder contributes two variables and fourteen clauses.
This gives:

```text
twenty triple rows:
  gates       20*464                    =  9,280 vars /  37,120 clauses
  counters    20*460 full adders        = 18,400 vars / 128,800 clauses
  >=5         20*popcount(5)            =      0 vars /      40 clauses
  total                                    27,680 vars / 165,960 clauses

endpoint pair profile:
  gates       2*464                     =    928 vars /  2,784 clauses
  counters    2*460 full adders         =  1,840 vars / 12,880 clauses
  ten-bit add                            =     20 vars /    140 clauses
  >=6, >=30                              =      0 vars /      6 clauses
  total                                     2,788 vars / 15,810 clauses

global pair profile:
  counters    2*461 full adders         =  1,844 vars / 12,908 clauses
  ten-bit add                            =     20 vars /    140 clauses
  >=110                                  =      0 vars /      5 clauses
  total                                     1,864 vars / 13,053 clauses.
```

The ripple widths retain the final carry, so none of the sums is modular.
The comparator clause counts are the popcounts of `5`, `6`, `30`, and `110`
under the existing direct first-difference encoding.

## 4. Separation-certificate scope

The three deterministic multisets pass the numerical rows that the checker
actually evaluates: cumulative rank bounds, the displayed moment bounds,
pointwise nested-support thresholds, the six endpoint facet rows, the fifteen
endpoint ridge rows, and (where displayed) the selected-width projections.
All three have minimum six-support at least 32, so every six-subcube
deficiency charge is zero.  (On the frozen audited snapshot the direct
recomputation gives minima 37, 40, and 42 respectively.)

They correctly show separation in the **listed projected numerical ledger**:

* the first violates both the endpoint profile and one endpoint triple row;
* the second satisfies the endpoint profile but violates one endpoint triple
  row;
* the third satisfies the face rows but violates the global pair profile.

They are not assignments to the complete auxiliary CNF.  In particular, a
width profile written beside a multiset is not itself a construction of all
selected endpoint variables and exact OR witnesses.  This is not a flaw in
the theorem note because it expressly says the objects need not satisfy the
base interval-OR formula and calls the comparison projected.  It does mean
that phrases such as "not a consequence of the current summaries" should be
read narrowly as "not a consequence of the explicitly checked scalar/
pointwise projection," not as a formal SAT separation from every auxiliary
circuit with the base clauses removed.

## 5. Presentation and evidence scope

The final audited snapshot has already incorporated the presentation repairs
identified during review:

* it calls each constant locally sharp only for its stated isolated problem;
* it limits the multiset separation claim explicitly to the checked projected
  numerical ledger; and
* the checker now instantiates and verifies the global `(12,49)` sharpness
  gadget.

The third separation certificate also supplies explicit compatible projected
width profiles

```text
x=(1,100,135,226),  y=(133,100,229),  z7=(0,4,42,284),
```

and checks the joint, named-cell, and rank-seven numerical rows used in the
claim.  As everywhere in Section 4, this remains a projected certificate,
not a construction of exact OR witnesses.

## Final conclusion

The pointwise three-face theorem, both pair-profile theorems, their local
sharpness claims, and all three proposed CNF inventories survive independent
audit.  The global `1,864/13,053` row is the natural first microbenchmark;
the endpoint row is a cheap coordinate-sensitive complement, and the twenty
triple rows are a larger pointwise branch.  No bound on `nu(11)` changes.
