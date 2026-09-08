# Independent audit of the balanced-subcube fractional collar completion

Date: 2026-07-31  
Status: **GO for Theorem 5.1 as a fractional statement**; no integral
rounding, acyclicity, or collar-braid conclusion

## 1. Scope and independence

This note independently audits Theorem 5.1 of
`MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md`.
Only the displayed definitions (5.1)--(5.4) were used.  No existing audit
implementation was read, imported, or called.

The clean-room program enumerates both orientations of every ambient
diamond, deletes exactly the atoms touching the balanced reserve, applies
both signed path families with `Fraction` arithmetic, and recomputes every
lower, upper, tail, and head load.

The audited Section-5 excerpt has SHA-256

```text
d1f6ebcc894ff129bdec07e9b8c9a7cf43fc83f38a2f929e5ee6c5114162e644
```

At replay time the complete source theorem had SHA-256

```text
201f080014022cc9c9bad39409fd65436a28ff8037b227bd8f3fee14280bc11b
```

## 2. Counts obtained independently

Write `n=m-a`.

For (5.1), the number of directed adjacent pairs `(X,Y)` of `n`-subsets
of a `2n`-set is

```text
binom(2n,n)n^2.
```

Consequently the total number of first-collar paths is

```text
P_1=a^2(a-1)binom(2n,n)n^2.
```

A fixed first-collar lower or upper endpoint lies in exactly

```text
a(a-1)n^2
```

paths.  Multiplication by `alpha_1` gives the required outer correction
`2/(m+1)`.

For (5.3), choose `X` and then the two points of `X-Y`.  The total number
of second-collar paths is

```text
P_2=binom(a,2)^2 binom(2n,n+1)binom(n+1,2).
```

A fixed second-collar lower or upper endpoint lies in exactly

```text
binom(a,2)binom(n+1,2)
```

paths.  Its correction is therefore `2/[m(m+1)]`.

These identities held literally in all six enumerated cases.

## 3. Negative multiplicities and atom nonnegativity

Fix a negative diamond of (5.1).  Its traces determine `d,e,z,Y,V`.
The remaining `X` is `V-{y}` for one of the `n` elements `y` of `Y`, so
the multiplicity is exactly `n`.  Each ordered orientation therefore
loses

```text
n alpha_1/2 = 1/[(m+1)a(a-1)n].
```

This is at most `w_0=1/[m(m+1)]` precisely when
`m<=a(a-1)n`.

A negative diamond of (5.3) determines `D,Z,X,Y`, hence belongs to exactly
one path.  Each orientation loses `alpha_2/2<=w_0`.

The exhaustive replay found exactly these multiplicities pointwise and no
negative final ordered-atom weight.  Deleted reserve atoms have weight zero.
Every reserve-avoiding atom remains strictly positive: for the two negative
families the loss-to-baseline ratios are respectively

```text
m/[a(a-1)n] < 1,
1/[binom(a,2)binom(n+1,2)] < 1.
```

## 4. Exact middle corrections

Tail and head corrections agree pointwise because both orientations of
every diamond receive the same signed half-coefficient.  The only nonzero
trace corrections are:

```text
family (5.1):
  (1,0)   +(n+1)/[(m+1)n]
  (1,1)   +2/[a(m+1)]
  (2,1)   -n(n+1) alpha_1

family (5.3):
  (2,1)   +2/[a m(m+1)]
  (1,2)   +2/[a m(m+1)]
  (2,2)   -n^2 alpha_2/2.
```

The two negative formulas are not needed for the theorem's upper bound,
but the clean-room enumeration recovers them exactly and finds no other
nonzero middle type.

For type `(1,0)`, the final load is

```text
1-2/(m+1)+(n+1)/[(m+1)n]
 =1-(n-1)/[(m+1)n] <=1.
```

For type `(1,1)`, it is

```text
1-1/m+2/[a(m+1)] <=1,
```

since `2m<=a(m+1)` for `a>=3`.  A type `(1,2)` resource starts with at
least `1/(m+1)` slack and gains only `2/[a m(m+1)]`; type `(2,1)` has the
same small positive correction and also the negative first-family term.
All other nonzero corrections are negative.  Thus every middle capacity
inequality is valid.  The exhaustive calculation checks the stronger
statement resource by resource.

## 5. Independent finite calibration

| `(m,a)` | `P_1` | `P_2` | negative (5.1) diamonds | negative (5.3) diamonds | maximum middle load |
|---:|---:|---:|---:|---:|---:|
| `(4,3)` | 36 | 9 | `36 x 1` | `9 x 1` | `1` |
| `(5,3)` | 432 | 108 | `216 x 2` | `108 x 1` | `11/12` |
| `(6,3)` | 3240 | 810 | `1080 x 3` | `810 x 1` | `13/14` |
| `(6,4)` | 1152 | 432 | `576 x 2` | `432 x 1` | `13/14` |
| `(7,3)` | 20160 | 5040 | `5040 x 4` | `5040 x 1` | `79/84` |
| `(7,4)` | 8640 | 3240 | `2880 x 3` | `3240 x 1` | `103/112` |

In every case:

1. both path-count and endpoint-multiplicity formulas were exact;
2. every nonreserve lower and upper resource had final load exactly one;
3. tail and head loads agreed pointwise;
4. every nonreserve middle load was at most one; and
5. every final ordered-atom weight was nonnegative.

The smallest case `(4,3)` is the unique tested tight middle case.  The
three requested new cases `(6,4),(7,3),(7,4)` all have strict middle slack.

## 6. Frozen artifacts

```text
scratch/audit_k_catalan_fractional_collar_theorem51_cleanroom_20260731.py
SHA-256 9a98c17dff6166d174eed7cf3c77b28926423e3d668e635b97aa6a8898185958

scratch/k_catalan_fractional_collar_theorem51_cleanroom_20260731.audit.json
SHA-256 3803e10ca87a8f41341355998b1a92f81109c3371859d409a307770e58b9ad05
```

## 7. Exact conclusion

Theorem 5.1 is independently verified at the stated fractional scope.  In
particular, the deterministic balanced reserve plus its explicit collar
state removes the fractional space obstruction exactly.  What remains is
an integral-correlation problem: the audit proves neither disjoint path
selection nor physical cycle elimination.
