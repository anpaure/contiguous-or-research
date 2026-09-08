# Audit of the linear-excess triangular endpoint braid

## Verdict

**PASS, with the pin-obstruction statement understood for `R>=2`.**

The construction gives a valid ordered orthogonal pair of the two stated
chain partitions in exactly

```text
N_R+R=|T_R|+R-1
```

positions.  Every assigned interval is forward and has length at most
`2R+1`.  For `R>=2`, the intervals assigned to height-zero targets cover all
physical positions, so the first positive height atom has no legal pin.

This is a theorem about the abstract endpoint layer.  It does not construct a
factorable triangular word or improve the current asymptotic upper bound.
It also does not assign the physical letters from `T_R` or enforce that every
letter of `T_R` occurs.  Those are separate constraints in the strict
triangular spanning problem.

## 1. Endpoint order

Write each block as

```text
A_r=(a_(r,0),...,a_(r,r-1))
```

and order

```text
A_R,A_(R-1),b_R,A_(R-2),b_(R-1),...,A_1,b_2,b_1.
```

Target `(u,r,x)` starts at `a_(r,u)`.  Its right endpoint is
`a_(r-1,x)` for `x<r-1` and `b_r` for `x=r-1`.  Both choices occur after
the complete block `A_r`, so every interval is forward.

For fixed `(r,u)`, increasing `x` moves the right endpoint forward exactly
as the height target grows.  For fixed `(r,x)`, increasing `u` moves the
left endpoint forward exactly as the rectangle shrinks.  Hence both endpoint
fibres have the correct inclusion order.

The two partitions are orthogonal: fixing `(r,u)` and `(s,x)` gives an empty
intersection when `r!=s` and the unique target `(u,r,x)` when `r=s`.

## 2. Position and bandwidth counts

There are `sum_(r=1)^R r=N_R` positions in the `A` blocks and `R` positions
`b_r`.  Pairing `A_r`'s left chain with the next level's right chain accounts
for the saving over two disjoint endpoint sets.

For `x<r-1`, the physical interval crosses at most a suffix of `A_r`, one
intervening `b_(r+1)` position (absent at the top), and a prefix of
`A_(r-1)`.  For `x=r-1`, it additionally reaches `b_r`.  Thus the maximum
length is at most `2R+1`.

## 3. Exact pin failure

For `r>=2`, all targets `(u,r,0)` end at `a_(r-1,0)`.  Taking their union
over `u` gives the complete interval from the beginning of `A_r` through
`a_(r-1,0)`.  These intervals overlap consecutively as `r` descends.  The
remaining rank-one interval runs from `a_(1,0)` through `b_1`.  Together
they cover every position in the construction.

Every height-zero target omits the first positive height atom `h_1`.
Therefore the union of its negative intervals is the entire physical word,
and

```text
Z_(h_1)=empty.
```

For `R=1`, there is no positive-height cell or target requiring `h_1`, so the
statement is vacuous rather than a pin obstruction.

## 4. Interpretation

The theorem proves that chain decomposition, orthogonality, triangular
placement, and short intervals require only linear excess.  In the
unrestricted Boolean ordered-chain/pinning model, coordinate pin survival is
the remaining realizability axiom for this interval assignment.  Globally
empty maximal-factor positions, if any in a future pin-compatible schedule,
may be deleted without increasing length; they are not a separate asymptotic
obstruction.

For the auxiliary triangular word `g_triangle(R)`, however, physical entries
are required to belong to the triangular alphabet and the word must span that
alphabet.  The endpoint construction does not encode either requirement.
Separate surviving extrema/threshold pins can combine into an ambient product
point that violates the coherent-letter condition `0<=y<s`; ordinary pin
survival alone does not prevent this.
Likewise, the four-box route requires compatible central-point inventory and
global superposition.  Therefore the strongest justified interpretation is
that quadratic excess is **not forced by endpoint geometry alone**.  The
theorem does not prove the literal identity "quadratic portal cost = pin
separation cost" for the constrained triangular/four-box construction.

The proposed protected-backbone lemma remains unproved.  It is precisely a
pin-compatible superposition theorem, so neither the triangular recurrence
nor the coefficient-one Boolean construction follows yet.

There is a slightly stronger negative conclusion for this particular
endpoint assignment.  It cannot be repaired by insertion-only padding.  Map
the existing positions order-preservingly into any longer line and retain all
the assigned endpoints.  The height-zero intervals form a connected cover
from the first old position to the last old position.  Their images therefore
cover every new position inserted between old positions as well.  Positions
inserted outside that hull belong to none of the unchanged positive-height
witnesses.  Hence the first positive height atom still has no legal pin.

Consequently a protected-backbone construction must genuinely reroute at
least one endpoint family (or duplicate endpoints and select different
witnesses).  Adding separator positions to this exact schedule is
insufficient.

## 5. Exhaustive regression

The checker

```text
scratch/audit_triangular_endpoint_braid.py
```

verifies all endpoint assignments, inclusion directions, bandwidths, and
height-zero negative unions through `R=100`, and explicitly checks every
left/right chain intersection through `R=20`.  It reports

```text
PASS targets=8670850 radius<=100
```

Its SHA-256 is

```text
f659203fe5eb28870bd2ba5249bb8c3561a89a1c94128f82bd63112c51ce254e.
```
