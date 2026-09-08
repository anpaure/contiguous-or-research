# K16 nested commutator and the exact Hall-23 third swap

Date: 2026-07-31  
Status: **four Hall-24 carriers independently replayed; one common third swap
gives Hall 23 but creates one upper hole; several natural return classes are
solver-free finite no-goes.  No universal word is claimed.**

## 1. Frozen inputs

The parent is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA-256 cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974
```

The four independently replayed descendants are:

| pass | outer length | inner length | SHA-256 |
|---:|---:|---:|---|
| 33 | 16 | 9 | `2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec` |
| 35 | 18 | 9 | `42420e0eea7102a07227b25e49663a127f89219b8c41cb18ee7de699385d9b04` |
| 46 | 16 | 13 | `bf3ee02110f70c168dc9863e1c8258cc54debfa408dd4c97fe5b57c6a4116754` |
| 55 | 18 | 15 | `e1166c6ae5f6c671c779bfb9f692fa8332aa7b9978cfcd93671b64244c5f1f69` |

All have length 12,873, exact middle ownership, unrestricted upper coverage,
and generalized matching 26,308/26,332, hence Hall deficiency 24.

## 2. Exact block algebra

Put `a=6611`, `b=12718`.  Write the original length-`L` blocks as

\[
 A=(A_0,\ldots,A_{L-1}),\qquad B=(B_0,\ldots,B_{L-1}).
\]

First exchange `A` and `B`.  Then exchange the length-`l` blocks beginning
at `a+2` and `b+3`, where `l<=L-3`.  Direct substitution gives the two final
shore words

\[
\begin{aligned}
 a\text{-shore}:&\quad
 B_0,B_1,A_3,\ldots,A_{l+2},B_{l+2},\ldots,B_{L-1},\\
 b\text{-shore}:&\quad
 A_0,A_1,A_2,B_2,\ldots,B_{l+1},A_{l+3},\ldots,A_{L-1}.
\end{aligned}
\tag{2.1}
\]

Thus the two overlapping swaps are not two independent trades: the inner
swap cancels the interior of the outer swap with a one-position phase slip.
The prefix

```text
A0,A1,A2,B2,...
```

at the second shore is independent of `L,l`.  In particular original row
6613 (`A2`) always lands at physical row 12720.  Its maximal one-cell
compiler profile is

```text
source occurrence (6613), physical [12720,12721),
allowed 8a0e, mandatory 8000.
```

It therefore creates the formerly absent edge `8000 -- (6613)`.
The resulting alternating augmenting path is

```text
8000 -- (6613) -- 8a0c -- (6724) -- 8e0c -- (11217).
```

This explains the parameter invariance of the score.  In all four cases the
Hall decomposition is exactly

\[
 24=11\text{ zero-provider targets}+13\text{ shared-component units}.
\tag{2.2}
\]

The outer swap alone remains at deficiency 25.  The inner swap alone is not
middle-exact.  Their ordered composition is middle-exact and provides the
one new augmenting path above.  “Cancellation” here is literal occurrence
algebra (2.1), not an entropy heuristic.

## 3. A common third swap really reaches Hall 23

The adjacent blocks `[6608,6611)` and `[12714,12717)` are untouched by the
two operations above.  On **each** of the four descendants, exchange these
two length-three blocks forward.  Full replay gives:

```text
middle ownership: exact
provider 8000: occurrence cell (6613), retained
provider 4e70: occurrence cell (12714,12715), newly created
maximum matching: 26309
Hall deficiency: 23 = 10 zero-provider + 13 shared-component
upper holes: exactly 4e79
```

So this is an exact, parameterized third compensating swap that genuinely
reduces Hall below 24.  It is **not** yet an admissible carrier because it
destroys the unique adjacent-facet delivery of upper mask `4e79`.

The missing fourth operation has a precise job: return a different facet of
`4e79` to physical row 12714 while preserving both occurrence-labelled
provider cells above.  If the two already-audited halo incidences

```text
6a29 -- (4654,4655,4656)
4a29 -- (4655,4656)
```

could also be realized physically, their full matching effect after the
third swap would be deficiency 21 (nine zero-provider plus twelve shared
units).  These conditional edges are not asserted to come from a legal word.

## 4. Scoped return searches

Four focused finite searches were run at `-O3`; every survivor was replayed
at the literal middle/upper level, and all all-upper survivors in the broad
single-swap search received full occurrence-labelled Hall matching.

1. **Direct halo block exchange.**  For each of the four parents, every
   forward/reversed equal-block exchange of length at most 64 whose two
   blocks contain the unique `6b29` source and halo row 4653 was tested:
   357,760 candidates per parent, **zero middle-exact**.
2. **One further equal-block exchange from pass 33.**  Up to length 32,
   77,866,496 candidates were tested.  There were 1,293 two-collar exact
   candidates, 48 with a named persistent-target hit, and five all-upper
   candidates.  Their Hall deficiencies by length were
   `(19,25),(21,25),(23,24),(25,25),(29,25)`: none beats 24.
3. **Three-block facet circulation.**  The natural circulation
   `B->A, C->B, A->C`, with the `C->B` end forced to be a facet of `4e79`,
   was exhausted for widths 3 through 64: 3,472 oriented cases, 2,480 with
   the right flat schedule, **zero middle-exact**.
4. **Protected facet return after Hall 23.**  Every equal-block return of
   length at most 32 that imports a `4e79` facet at row 12714 while avoiding
   both provider collars was tested: 1,026,280 cases, 640 facet-compatible,
   480 flat-compatible, **zero middle-exact**.
5. **Protected arbitrary facet 3-cycle after Hall 23.**  For every physical
   `4e79` facet donor and every third occurrence, the cycle
   `facet -> row12714 -> third -> donor` was replayed: 102,856 cases,
   77,106 flat-compatible, **zero middle-exact**.

These are architecture no-goes only.  They do not exclude a dependency-
overlapping multirow braid, a move that migrates a provider cell, or an
unrelated carrier.

## 5. Reproducibility

Authoritative audit:

```text
scratch/audit_k16_nested_hall24_commutator_and_third_swap_20260731.py
scratch/k16_nested_hall24_commutator_and_third_swap_20260731.audit.json
```

Focused enumerators:

```text
scratch/search_k16_nested_hall24_halo_blockswap_20260731.cpp
scratch/search_k16_nested_hall24_threeblock_circulation_20260731.cpp
scratch/search_k16_nested_hall23_facet_return_blockswap_20260731.cpp
scratch/search_k16_nested_hall23_facet_return_3cycle_20260731.cpp
```

The audit payload SHA-256 is
`cf0984fd2e26ee39e53a5a756193727679ec2882df12804c3249890f164a69d7`.
