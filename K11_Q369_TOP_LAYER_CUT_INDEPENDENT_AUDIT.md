# Independent audit: q369 top-layer cut

## Verdict

**PASS**, relative to the explicit `q369_schedule` branch and the previously
audited adjacent-shadow/exception-slot encoding. I found no added clause that
can remove a genuine solution of that branch.

Audited source:

```text
4e63cce6d95099cb0571aa5aa50b405b1d63b05bb18742e5262c484ac6325c07  k11_forest_sat.cpp
```

The conclusion is deliberately branch-relative. An UNSAT result with this cut
would refute `q369_schedule`, not the unrestricted length-465 problem.

## 1. Short-cell saturation

The branch units at source lines 1476--1483 fix rank-six row `i` to
`[i,i+2]` for `0 <= i < 369` and to `[i,i+3]` thereafter. In any 465-entry
solution all 1023 targets of ranks 1 through 5 have witnesses of length at
most three. Together with the 369 distinct selected rank-six triples, this
gives

```text
1023 + 369 = 1392 = 465 + 464 + 463
```

distinct target values in the 1392 physical intervals of lengths at most
three. Their selected cells must therefore biject with the physical cells.
Every nonfixed triple/pair/singleton has rank at most five, and all short-cell
OR values are different. This justifies the saturation premise used at source
lines 1558--1572.

## 2. Exact 463-cell rank-five pool

Deleting fixed triples `[s,s+2]`, `0 <= s <= 368`, leaves exactly these
maximal cells:

```text
P_s = [s,s+1], 0 <= s <= 368       (369 cells)
T_s = [s,s+2], 369 <= s <= 462     (94 cells)
```

There are 463. A rank-five short cell outside this pool would have a strict
remaining supercell with a distinct rank-at-most-five OR, an impossibility.
The 462 rank-five targets therefore use the pool with one omission.

When the omitted pool index is `e`, ordered row `i` uses pool index `i` for
`i<e` and `i+1` for `i>=e`. In the source's zero-based `(alpha,beta)` states
this is exactly:

```text
i=0..367   : 01 or 12
i=368      : 01 or 13
i=369..461 : 02 or 13
```

The positive clauses at lines 1576--1588, exact-one clauses at 1804--1809,
and coordinatewise monotonicity at 1864--1869 admit exactly the 463
false-then-true `skip` thresholds. They biject with omissions `e=0,...,462`;
no schedule is lost.

## 3. Rank-four crossed candidates

After removing the fixed rank-six cells and the 462 selected rank-five cells,
the residual 561 cells are:

```text
all 465 singletons;
late pairs [p,p+1], 369 <= p <= 463;
the one omitted pool cell e.
```

Every rank-four cell is maximal in this residual poset. Its maximal cells are
precisely `e`, early singletons `[p,p]` for `0 <= p <= 368` not contained in
`e`, and late pairs `[p,p+1]` for `369 <= p <= 463` not contained in `e`.

The omitted cell itself cannot be a crossed candidate: an omitted early pair
has no proper selected rank-five extension with the same left endpoint, and
an omitted late triple is outside the singleton/pair crossed-candidate
universe. Thus source lines 1620--1637 disable only impossible crossed
rank-four assignments.

The guard polarity at lines 1608--1618 is correct:

```text
e=0     iff skip(0)
0<e<462 iff !skip(e-1) and skip(e)
e=462   iff !skip(461)
```

For an early singleton `p`, the only containing omitted cells are `P_p` and
(when `p>0`) `P_(p-1)`. For a late pair starting at `p`, they are `T_p` when
`p<=462` and `T_(p-1)` when `p>369`. These are exactly the guarded calls at
lines 1629--1636, including boundary cases `p=0,368,369,463`.

The six generic rank-four exception slots at lines 2076--2124 remain wholly
unrestricted by the cut. The previously proved adjacent-shadow theorem bounds
noncrossed rank-four targets by six, and the omitted cell (if rank four) is
included in that count. Hence the cut does not create a seventh exception or
silently require the omitted cell to be crossed.

## 4. Independent exhaustive check and counts

I independently enumerated all 1392 short intervals and all 463 possible
omissions. For every omission, direct containment computation agreed exactly
with the maximal-cell description and every generated guard:

```text
PASS short=1392 pool=463 residual_maxima_sizes=[463,464]
     disallowed=153450 guards=305250 total=458700
```

The arithmetic is:

```text
disallowed = ((465-369) + (464-95))*330 = 153450
guards     = ((369+368) + (94+94))*330  = 305250
```

Adding the 462 rank-five pool clauses gives 459162 new clauses and no new
variables.

The frozen remote binary and logs independently match the recorded build:

```text
b60cf2d72526148c74a66504ede874603fe897ca8c4a8c0e638ea7bc13c45c8c  binary
7fc296997a65c27ff67e417fa7180499b67ce5ab2a073fa4d133f10237a1277f  baseline.log

baseline: variables=2882282 clauses=14459954
cut:      variables=2882282 clauses=14919116
          q369_top_layer_clauses=462
          q369_rank_four_clauses=458700
```

I reran the invalid-gate check against the frozen binary; it returned status 2
with the required `q369_schedule` diagnostic.

## 5. Scope

This audit certifies only the theorem cut introduced at source lines
1558--1640. It relies on the existing soundness of the unrestricted central
schedule encoding and the six-slot adjacent-shadow theorem. It neither
certifies SAT/UNSAT output nor promotes `q369_schedule` to a globally necessary
normal form.
