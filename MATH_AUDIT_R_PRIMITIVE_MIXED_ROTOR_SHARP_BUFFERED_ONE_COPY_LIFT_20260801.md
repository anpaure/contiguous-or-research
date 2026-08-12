# Audit: primitive mixed rotor sharp buffered one-copy lift

Date: 2026-08-01  
Audited file: `MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`  
Verdict: **PASS**, with the exact scope stated in Section 6 below.

## 1. Primitive role coefficients

For `a=d-1,b=d+1`, the aggregate mixed coefficients are

```text
q_(a,b)=C(1,1)=1,       p_(a,b)=C(1,0)=1.
```

The reduced positive compositions of `3` into two cells are `(1,2)` and
`(2,1)`.  After appending `d-1` singleton cells their types are exactly

```text
P=(s-1,2,1,...,1),       H=(s,1,...,1),       s=r-d.
```

Thus the claimed primitive signature is `e_(d-1)+e_(d+1)`, and each added
short-buffer occurrence really is one `e_(d-1)` role on type `H`.

## 2. Universal owner-simple lower bound

For a cyclic source word of period `L`, every depth-`d` owner is the union
of `d+1` consecutive source letters.  If `2<=L<=d+1`, this interval contains
every period letter, so all owners coincide.  A period-one component has
owner equal to its one repeated source.  Since the source sizes of `P` and
`H` are `s-1,s<r`, neither primitive occurrence can lie in such a singleton
component.

Therefore any owner-simple cover containing either primitive occurrence
has at least `d+2` total occurrences.  Starting from two primitive roles,
at least `d` more roles are necessary.  This remains true if the added
roles have arbitrary types.  No assumption about owner labels, mark
choices, or upper guards enters the proof.

## 3. Exact unbuffered multiplicity

For `m` primitive copies there are `2m` occurrences, all with source size
below `r`.  The preceding lower bound therefore gives

```text
m>=ceil((d+2)/2).
```

The matching construction is exact.  Put `m_0=ceil((d+2)/2)`, choose a
common set `G` of size `s-2`, a common point `b`, and `2m_0` private tags.
Around the alternating type word `(PH)^m_0`, use source `G+tag` at a `P`
position and `G+b+tag` at an `H` position.  No two `P` positions are
adjacent.  At `P`, the preceding `H` contributes `b` and its tag to age
one; at `H`, the current source refreshes `b`; every older age cell is the
corresponding private tag.  Thus the types are exactly `P,H` alternately.

Because `2m_0>d+1`, the owners are the distinct unions of `d+1` consecutive
private-tag sources.  At ranks `s-1` and `s`, respectively, the `P` and `H`
source prefixes are distinct.  At every higher rank, all marked prefixes
use one common interval length below `2m_0`, hence their private-tag
intervals are distinct.  This verifies both the positive construction and
the exact factor `ceil((d+2)/2)` claimed in Theorem 3.1.

## 4. Literal source replay

The construction uses `L=d+2` and

```text
S_0=G union {w},
S_i=G union {b,v_i},       1<=i<=d+1,
|G|=s-2.
```

All displayed symbols are disjoint, so the ambient support has size

```text
(s-2)+2+(d+1)=r+1,
```

which explains the exact hypothesis `k>=r+1`.

At time zero,

```text
C_(0,0)=G union {w},
C_(0,1)={b,v_(d+1)},
C_(0,j)={v_(d+2-j)}              (2<=j<=d),
```

so the type is `P`.  At a nonzero time `t`, `C_(t,0)` has size `s` and
each older cell consists of the private tag of the corresponding earlier
source; hence the type is `H`.  The definition by literal set differences
immediately gives the shift recurrence, with no type-only inference.

## 5. Owners and owner injectivity

Let

```text
Z=G union {b,w,v_1,...,v_(d+1)}.
```

It has size `r+1`.  A depth-`d` owner window includes `L-1` of the `L`
sources.  Omitting `S_0` removes only its private tag `w`; omitting `S_i`
removes only `v_i`, because `G` is everywhere and `b` is present in all
other nonzero sources.  Therefore the owners are exactly the `d+2`
distinct rank-`r` facets

```text
Z-{w}, Z-{v_1},...,Z-{v_(d+1)}.
```

This proves literal one-copy ownership for the module.

## 6. Marks and rankwise target injectivity

The `P` occurrence offers ranks

```text
s-1,s+1,s+2,...,r-1,
```

whereas each `H` occurrence offers

```text
s,s+1,...,r-1.
```

Marking all offers on the primitive `P,H` pair and only the top `d-1`
offers on each of the other `d` copies of `H` yields multiplicities

```text
rank s-1:                 1,
rank s:                   1,
each rank s+1,...,r-1:    d+2.
```

This is exactly `v_(d+1)+(d+1)v_(d-1)`, equivalently
`g_(d-1,d+1)+d e_(d-1)`.

At rank `s-1` and rank `s` there is only one marked occurrence.  At every
higher marked rank all states use the same source-interval length
`j in {2,...,d}`.  Since `j<L`, two distinct cyclic intervals have different
sets of private tags, and therefore different literal prefix unions.  The
rankwise target deck is injective.

## 7. Exact scope

The theorem proves a local owner-simple lower-flag module at one copy.  It
does not prove that its target sets equal a prescribed canonical Ferrers
residual family, that many modules can be owner/target-disjointly packed,
or that the construction preserves upper shadows, residence, Ore--Ryser
rows, connectivity between modules, or common-cap/compiler assignments.

The formal primitive successor edges are deliberately rethreaded into the
length-`d+2` cycle.  This is permitted by NRFC, whose successor permutation
is not required to preserve the aggregate package decomposition.

No flaw was found in the coefficient, chronology, owner-facet, or
rankwise-injectivity claims.
