# Audit of the `k=11` Type-I rank-filtration encoding

> **Superseded/retracted implementation verdict (2026-07-23).**  The old
> equality `y0=h1+462-h6` is valid only on chain A.  Chains B/C contain the
> additional width-zero states `22`/`11`, so the frozen formula audited below
> was an A-biased subformula.  The theorem itself survives.  See
> `K11_RANK5_SINGLETON_BOUNDARY_REPAIR.md` and the independent repaired-source
> audit `K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## Verdict

**PASS after one implementation repair.**  During the audit, the first draft
of `RankFiltrationTypeIPlan::add_unsigned` was found to omit its final carry.
That would have made the counters and duplicate equality modular.  The carry
is now retained, the production inventory changed by the expected four
clauses, and all independent checks pass.

The final guarded module

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
```

is sound and satisfiability-complete for the Type-I array-level branch of
`RANK_FILTRATION_STABILITY_AUDIT.md`.  It adds exactly 2,341 variables and
17,354 clauses and has no guard-off allocation or clause effect.

Audited files:

```text
ab9a3e1cce0325469adbb57d8c39c9a5b660f194c20b9ff6b099497f0ba9c4ea
  k11_forest_sat.cpp
cad5528c40f2cfc9b89fe1035cf618df4b15ef0a56091ed1ac4a323e3805bd15
  scratch/verify_k11_rank_filtration_type1.cpp
```

## 1. Branch anchor and prerequisites

Type I requires the already audited `K11_FOREST_RANK6_BRANCH=1`.  That branch
in turn requires the coordinate-canonical, oriented-boundary, rank-six band,
and joint-band modules.  Its exact anchor and unit imply

```text
A[0]=63,
no other literal rank-six array entry exists.
```

The new parser additionally requires local-density rank one-hot literals and
both band plans.  Missing prerequisites, branch zero, or an absent branch all
exit with status 2 before allocation.  The mode is listed among the structural
options prohibited by the separate portal formula.

## 2. Rank cap and rank-five count

The reused one-hot rank flags are exact.  Units forbid ranks 6--11 at each of
the 464 suffix positions, contributing

```text
464*6=2784
```

clauses.  Position zero is intentionally not capped because branch one fixes
it to rank six.

The exact Wallace/ripple circuit sums all 465 rank-five flags.  The anchored
position contributes false, so this is exactly the suffix rank-five count.
All nine output bits, including the final carry from the eight-bit Wallace
rows, are retained.  The direct comparator to 133 has six clauses and cannot
wrap around.

## 3. Physical suffix component

After the rank cap, a suffix position is low precisely when its rank-five flag
is false.  The source uses

```text
!rank5[1]
rank5[p-1] AND !rank5[p],  p=2,...,464
```

as the 464 exact start indicators.  The checker exhausts all 1,024 ten-bit
suffix analogues and agrees with a direct maximal-run count in every case.

The count's exact binary output is fixed to one, not merely bounded above by
one.  Thus a nonempty low core is asserted explicitly rather than being left
to an indirect rank-count consequence.

## 4. Literal duplicate equality

Reselecting every distinct literal five-set at a singleton is globally WLOG:
the remaining rank-five targets retain arbitrary witnesses, the equal-rank
family stays incomparable, and every inherited endpoint/band theorem applies
to the reselected family.  Under this choice `y0` equals the number of
distinct literal rank-five values.

The rank-five chain boundaries satisfy exactly

```text
y0=h1+462-h6.
```

Therefore the source equality

```text
n5+h6=h1+462
```

is equivalent to `n5=y0`, hence to duplicate excess zero.  Both additions
retain their tenth carry bit, and all ten result bits are equated in both
directions.  The checker exhausts small multiplicity vectors and all real
`0<=h1<=h6<=462` boundary pairs, confirming both identities.

## 5. Independent inventory

The checker independently models bucket populations rather than including
the production implementation.  It obtains:

```text
n5 count:        461 full adders
component count: 460 full adders
equality sums:    18 full adders
start variables: 463
```

This gives exactly

```text
variables=2341 clauses=17354
rank_cap_clauses=2784
component_definition_clauses=1389.
```

The checker command is

```text
g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  scratch/verify_k11_rank_filtration_type1.cpp \
  -o /tmp/verify_k11_rank_filtration_type1
/tmp/verify_k11_rank_filtration_type1
```

and its output is

```text
suffix_component_start_identity=PASS
duplicate_free_alignment=PASS
type1_variables=2341 clauses=17354
rank_cap_clauses=2784 component_definition_clauses=1389
k11_beta_4_5_6=331,464,465 PASS
```

## 6. Build-only regressions

The production source compiles cleanly against the local CaDiCaL stub.  The
minimal branch-one prerequisite build changes from

```text
variables=4958941 clauses=16059861
```

to

```text
variables=4961282 clauses=16077215
```

when Type I is enabled.  The difference is precisely `2,341 / 17,354`.

The all-off baseline remains

```text
variables=4892622 clauses=15524818,
```

and the earlier Type-II guarded inventory remains exactly

```text
variables=2374 clauses=17557.
```

The fully integrated branch-one build, including the 4.3-million-clause
subcube-deficiency module, succeeds at

```text
variables=3633096 clauses=19448397.
```

## 7. Scope

The Type-I and Type-II guards now cover the two array-level rank-filtration
architectures at a hypothetical `k=11,n=465` optimum.  They do not by
themselves certify SAT or UNSAT.  Any refutation must run both branches,
archive each proof trace, and verify the traces independently; any model must
still pass exhaustive interval-OR verification.
