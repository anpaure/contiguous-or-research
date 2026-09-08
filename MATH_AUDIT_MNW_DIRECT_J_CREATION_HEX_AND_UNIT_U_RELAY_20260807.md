# Audit: direct `J`-creation face and unit `U` relay

**Date:** 2026-08-07  
**Method:** independent hand replay of the six incidences and chamber
inverse test; no computation or search

## Incidence replay

With `K=1100000101` and active labels `5,6,9`, the owners and colours are

```text
owners:  1100100101  1100010101  1100000111
colours: 1100110101  1100010111  1100100111
```

The selected-addition pairs are respectively `{6,7}`, `{7,9}`, and
`{4,5}`.  Hence the selected cyclic edges are `Z-P`, `Z6-N`, `Z9-Q`, and
the complementary three edges are unselected.  The face alternates.

## Turn replay

```text
1100111101 -> 1100101111
1100011111 -> 1100111101
1101100111 -> 1101010111
```

The first target on the left cancels the second target on the right, giving

```text
+1100101111 +1101010111 -1100011111 -1101100111.
```

The inverse pairs are

```text
1100011111 : (7,9)
1101100111 : (4,5), (8,9)
1101010111 : (8,9)
```

so the negative `1100011111` is a unit provider and the negative
`1101100111` is redundant.  Combined with the preceding two-face current
`+1010101111-1100101111`, the unique terminal hole is
`1100011111`.

## Scope replay

All owners, colours, and turns are distinct from the two earlier boundary
faces.  Dyck suffix projection separates different tensor copies.  No
claim is made about a later spanning-tree completion or component action.

