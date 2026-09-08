# Audit of `k11_forest_sat_histcuts.cpp`

## Verdict

The histogram implementation is sound as written.  No missing branch row,
incorrect constant, guard error, overflow, or inventory mismatch was found.

Audited source:

```text
scratch/k11_core_incidence/k11_forest_sat_histcuts.cpp
sha256 447b17b9eb91910fb8159e6933b9e0e05b09ee884980a4303f07c4562f9867aa
```

## Exact histogram identities

For ranks `r=1,2,3,4`, put

```text
c=(11,55,165,330),
F=sum_r max(nr-cr,0),
E=sum_r r*max(nr-cr,0).
```

The code uses

```text
F=max_R sum_(r in R)(nr-cr),
E=max_R sum_(r in R)r(nr-cr)
```

over all sixteen subsets.  These identities are exact because each summand
is separable: an optimizing subset contains precisely the positive terms.
Consequently, enforcing all subset rows has the correct direction and is
equivalent to charging the full surplus.

## Count rows

Write `y1=even-odd`, where

```text
even=h2+h4+h6,  odd=h1+h3+h5.
```

* Type I: `y2>=96+n5+F` and `y1+y2=462-n5` give
  `2*n5+y1+F<=366`.
* Type-II duplicate/one-core: `z=n5-1` and
  `y1+y2=462-z=463-n5` give `2*n5+y1+F<=368`.
* Type-II two-core: `z=n5`, `y1+y2=462-n5`, and the offset 95 give
  `2*n5+y1+F<=367`.

For each subset `R`, the implementation compares

```text
2*n5+even+sum_R nr <= odd+C+sum_R cr,
```

with `C=366,368,367`, respectively.  This is exactly the rearranged row.
The Type-II rows are guarded by `duplicate_flag` and
`two_components_flag`; no count row is incorrectly imposed on the
no-duplicate one-core branch.

## Pair-incidence rows

Removing surplus singleton cells lowers the available singleton/pair rank
capacity by `E`.  The exact rows are

```text
3*S-5*y1-E >= 1938      Type I and duplicate Type II,
3*S-5*y1-E >= 1940      two-component Type II.
```

The extra two in the last row is the additional endpoint deficit from two
low components.  The source compares

```text
C+5*even+sum_R r*nr <= 3*S+5*odd+sum_R r*cr,
```

with `C=1938` or `1940`, so its sign and constants are correct.

## Triple-incidence rows

The exact histogram-strengthened physical rows are

```text
6*S+5*n5-E >= 4254      Type I and Type-II (0,1),
6*S+5*n5-E >= 4259      Type-II (1,1) and (0,2).
```

The implementation emits the 4254 family unconditionally in Type II and
the 4259 family under each of `duplicate_flag` and `two_components_flag`.
This covers precisely the three corrected alternatives.  Reusing one
`tight_right` arithmetic vector in two independently guarded exact
comparators is safe.

## Guards and exactness

* `RankFiltrationTypeIIPlan` is constructed with
  `named_cell_hall || core_cell_incidence`, so `duplicate_flag` is never the
  invalid literal zero when the new plan uses it.
* `two_components_flag` is already exact and always exposed.
* Type-I `n5_count` is retained as a field and reused without a second count.
* Every addition retains its final carry.
* Every guarded prefix-equality clause carries its guard; inactive rows do
  not constrain their arithmetic inputs.
* Maximum subset constants and totals fit comfortably in the retained raw
  widths; no modular wraparound is possible.

## Independent inventory reconstruction

A raw-width operation simulation matching the source primitives gives:

| branch | counter vars/clauses | arithmetic vars/clauses | comparator vars/clauses | total |
|---|---:|---:|---:|---:|
| Type I | 3688 / 25816 | 3922 / 27454 | 734 / 4463 | **8344 / 57733** |
| Type II | 3688 / 25816 | 5170 / 36190 | 1725 / 10483 | **10583 / 72489** |

The comparator clause column includes the direct constant clauses.  These
totals exactly equal the reported build inventories.

With histogram surplus disabled, the existing totals remain

```text
Type I:  4057 variables / 28395 clauses,
Type II: 4057 variables / 28405 clauses.
```

## Non-blocking inefficiency

The empty subset is intentionally included.  Its count, pair, and triple
rows duplicate already-emitted base inequalities through newly materialized
arithmetic wires.  This increases the inventory but is not a correctness
problem.  It may be removed later only after re-auditing the expected
inventory deltas.

