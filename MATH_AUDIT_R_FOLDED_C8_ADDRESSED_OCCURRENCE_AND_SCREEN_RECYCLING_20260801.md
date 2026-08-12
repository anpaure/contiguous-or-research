# Independent audit of the folded-C8 address lift and recycled screen

Date: 2026-08-01  
Verdict: `PASS` with the complete-cap, guard, sidecar and two-cell-ticket
scope restrictions stated in the theorem.

Audited theorem:

```text
MATH_THEOREM_R_FOLDED_C8_ADDRESSED_OCCURRENCE_BIJECTION_AND_ZERO_CHARGE_SCREEN_20260801.md
```

## 1. Fibre bijection

For each phase the physical address set is exactly
`{(i,j):0<=i<=j<n}`, of size `n(n+1)/2`.  Partitioning this finite set by

```text
(j-i+1, interval OR core, interval common cap, complete guard type)
```

shows immediately that equality of fibre cardinalities is necessary and
sufficient for a type-preserving address bijection.  Pairing equal
lexicographic ranks is a genuine bijection: it is injective separately in
each disjoint fibre and its image has the full cardinality of that fibre.

The replay independently checks both projections of the listed pairs, so it
does not merely compare counters.  It then recomputes core and cap directly
from each paired source address.  Verdict: valid.

The compiler implication is valid only after a complete cap state is fixed.
On the one-core face the cell neighbourhood is the Boolean interval
`[core,cap]`; equality of these endpoints is exactly equality of cell
neighbourhoods.  Address-dependent guard deletions must be included in the
key.  The pointwise union of two phase letters is only a containment-cap
candidate until the owner/pin/protected rows admit it.  These restrictions
are correctly explicit in the theorem.

## 2. Literal ray addresses

For

```text
G_e=(X_L,L_e,f_2,...,f_(d-1),R_e,X_R)
```

the positions are `0,...,d+1`.  Direct union gives

```text
P_e(j)     = OR G_e[1..j],
S_e(j+1)   = OR G_e[j+1..d]       (1<=j<d).
```

The two intervals are disjoint.  Their spanning interval contains both
`a1,a3`; hence it is neither ray target.  Therefore an antidiagonal
`(P0(j),S1(j+1))` or `(P1(j),S0(j+1))` is two occurrence tickets, in
opposite phase words, and cannot be one capacity-one compiler column.
Verdict: the correction is necessary and valid.

## 3. Screen recycling

The proof's five classes are exhaustive: fixed exterior, packet interior,
left crossing, right crossing, and both boundaries.  Every left-crossing or
two-sided interval contains the immediate-left ambient letter `H`, so
`E subseteq H` makes the screened prefix equation apply.  Right-crossing
intervals use the suffix equation.  Widths are unchanged classwise.  Since
`H` already exists, the source charge is zero.

Immediate adjacency cannot be deleted.  For example, take

```text
U=({a},{b},{a,b}),   V=({b},{a},{a,b}),   E={a,b}.
```

The internal graded decks and suffix chains agree and `E` screens the prefix
chains.  If a new intervening letter `{c}` is placed after the screening
letter, the interval beginning at `{c}` and ending at the first packet
letter is `{a,c}` in one phase and `{b,c}` in the other.  It does not meet
the screen.  Thus the theorem's immediate-left (or equivalent suffix-screen)
hypothesis is sharp.

Length neutrality also does not imply incidence neutrality.  If
`H=E union {x}` and an intended crossing target omits `x`, the crossing
address is not a provider.  Hence the theorem correctly requires either
unused crossing cells or literal target containment and guard checks.

## 4. Exact replay verdict

The dependency-free replay covers both screen choices and all eleven depths
`2,...,12`.  It checks fresh, recycled, and fixed two-sided-context words.
Every enriched fibre agrees, every canonical map is bijective, and every
ray-shore assertion passes.

Frozen hashes:

```text
audit script  247e4aa93100dd6d7d4c282daf6e2183e4ca95c70049aa0cefc807d72bf24dcc
audit JSON    c7c99e1cf57ec490bd3a7136349d047a06fa6af249c1a65363cb639a26bf4cd3
payload       8ee79f497d8ae1951dd28d16b61dfa0d7a4b5fa15e9cae455dd28df5ddf21368
```

No all-`d`, owner, `q1`, protected-guard, complete-cap-existence, or
regeneration statement is certified by this finite replay.
