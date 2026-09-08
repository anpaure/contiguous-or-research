# Atomic portal-packet normal form for exact K16 substitution search

Date: 2026-07-30

## Scope

Fix a word `x` of nonzero 16-bit masks, a declared set `A` of editable
positions, and a Hamming-support budget `r`.  A completion is a universal word
`y` whose final support

```text
P = {p in A : y[p] != x[p]}
```

has size at most `r`.  Intermediate words may have arbitrarily many holes.
This report concerns substitution feasibility around this fixed rooted
instance.  It does not reduce all length-12873 words to any particular support
and does not prove an unrestricted K16 no-go.

## The atomic portal-packet theorem

Let `h` be any target missing from the current word `x`.  If a completion `y`
exists with support `P`, choose any interval `I` whose OR in `y` is exactly
`h`, and put

```text
Q = P intersect I.
```

Then:

1. `Q` is nonempty and `|Q| <= r`;
2. every unchanged `x[i]`, `i in I \ Q`, is a submask of `h`;
3. every final value `y[q]`, `q in Q`, is a nonzero submask of `h` and differs
   from `x[q]`;
4. applying the assignments on `Q` simultaneously already installs an
   `h`-witness; and
5. `y` differs from that intermediate word only on `P \ Q`.

Consequently an exact radius-`r` search may, without loss, choose a current
hole and branch on simultaneous portal packets of sizes `1,...,r`.  Size-one
packets are the mathematical single-cell provider moves.  Larger packets
capture every synergistic portal for which no individual edit is a provider.

### Proof

Every cell of an interval whose OR is `h` is a submask of `h`, proving item 2
and the submask part of item 3.  The strict change `y[q] != x[q]` follows from
`q in Q subseteq P`.  If `Q` were empty, `x` and `y` would agree throughout `I`, so `I`
would already witness `h` in `x`, contrary to the choice of a hole.  Edits
outside `I` cannot affect the OR of `I`; hence applying precisely the final
assignments on `Q` makes that OR equal `h`.  Substitutions at distinct
positions commute, and the remaining final assignments are exactly those on
`P \ Q`.  This proves all five items.

The theorem permits temporary debt.  Along the branch extracted from the
chosen completion, the installed interval `I` survives because
`(P \ Q) intersect I` is empty.  An unrelated search branch may later edit
inside `I` and reopen the hole, so implementations must still replay every
state.  A chronological non-provider edit outside `I` can be deferred; it is
not lost.

## Exact corridor enumeration

For a chosen hole `h`, define the current bad positions

```text
D_h = {i : x[i] has a bit outside h}.
```

In a final `h`-witness interval `I`, the set

```text
B = D_h intersect I
```

is a consecutive block in the ordered list `D_h`, and every position of `B`
must belong to `Q`.  For a nonempty block `B`, let `C(B)` be the maximal
interval beginning just after the preceding bad position and ending just
before the following bad position.  Thus the only currently bad positions in
`C(B)` are those in `B`.  If `B` is empty, `C(B)` means the particular maximal
`h`-clean component containing `I`; every clean component is enumerated
separately.

The witness interval satisfies `I subseteq C(B)`.  After applying `Q`, every
cell of `C(B)` is a submask of `h`.  Since `C(B)` contains the interval `I`
whose OR is `h`, extending from `I` to `C(B)` cannot change that OR: the whole
corridor also has OR exactly `h`.

It is therefore complete to enumerate:

1. every empty clean component and every consecutive bad block `B` with
   `|B| <= r` and `B subseteq A`;
2. every possibly nonconsecutive set
   `B subseteq Q subseteq C(B) intersect A`, with `1 <= |Q| <= r`;
3. every assignment `0 < v[q] subseteq h`, `v[q] != x[q]`, satisfying

```text
OR(x[i] for i in C(B) \ Q) OR OR(v[q] for q in Q) = h.
```

For `r >= 1`, there are `O(r*n)` candidate bad-block corridors before
optional-position and value expansion.  Literal duplicate packets arising
from different corridors may be merged.

`C(B)` is a witness envelope, not a locked region.  Only `Q` is consumed by a
recursive branch.  Positions of `C(B) \ Q` remain editable because the unknown
completion may change one of them later while preserving a smaller witness
inside the corridor.

Three small examples guard the implementation boundary:

- `x=(4,1)`, `h=3`, `y=(1,2)` has `B={0}` but the required packet is
  `Q={0,1}`; neither assignment is an individual provider.
- `x=(1,1,1)`, `h=7`, `y=(2,1,4)` has an empty bad block and a
  nonconsecutive packet `Q={0,2}`.
- `x=(4,1,1)`, `h=3`, `y=(2,1,4)` first uses `Q={0}` and witness `[0,1]`,
  while the later edit at position 2 remains inside the maximal envelope.

Thus restricting packets to the bad block, to consecutive editable cells, or
locking the whole envelope is incomplete.

## Exact support lower bound for one hole

The minimum number of arbitrary substitutions needed merely to install `h`
on the declared support `A` is

```text
rho_A(h) = min over corridors C:
  |B_C|,  if B_C is nonempty and B_C subseteq A;
  1,      if B_C is empty and C intersect A is nonempty;
  infinity otherwise.
```

Necessity follows because every current bad cell inside a witness must change,
and a currently clean corridor cannot already witness the missing target.
For sufficiency, in a nonempty block set one edited bad cell to `h` and every
other bad cell to any nonzero submask of `h`; in an empty corridor set one
editable cell to `h`.  These are genuine changes because a bad incumbent has
an outside bit and a clean incumbent equal to `h` would already be a singleton
witness.  Thus `rho_A(h) > r` is a sound exact prune for the selected hole.

For the unrestricted nonzero substitution domain used in this theorem, this
quantity collapses to `rho_A(h)=1` whenever `A` is nonempty, and to infinity
when `A` is empty: one may set any editable cell directly to `h`, producing a
singleton witness.  The corridor formula becomes a substantive prune only
after additional value domains or packet restrictions are independently
specified and the bound is adapted to them; the displayed unrestricted
formula must not simply be reused.  In all cases it concerns installation of
`h` only and makes no assertion about collateral targets, which require exact
replay or further sound bounds.

## Witness-piercing protection theorem

Let `t` currently be covered, and let `W_x(t)` be all incumbent witness
intervals for `t`.  The projection of a witness interval `W` is literally the
set intersection `W intersect A`, viewed in the induced order on `A`; no
endpoint rounding or convexification is allowed.

- If one projection is empty, that witness is immutable in the current
  subtree.
- Otherwise the projections are intervals in the order on `A`.  The minimum
  number `tau_A(t)` of future editable positions that hit every incumbent
  witness equals the maximum number of pairwise disjoint projected witnesses.
  The common value is obtained greedily by increasing right endpoint.

The equality is the interval transversal theorem.  Hence `tau_A(t) > r`
proves that `t` cannot become a hole within the remaining budget.  A packet
`Q` can create an immediate debt `t` only if `Q` hits every incumbent witness.
Hitting every old witness is necessary, not sufficient: modified or new
witnesses may still cover `t`, so exact replay remains mandatory before
recording a debt.

Raw witness multiplicity is not a reserve certificate.  The relevant reserve
quantity is the interval piercing number, or, for a known future packet `F`,
the explicit existence of a witness disjoint from `F`.

## Complete recursion

An exact fixed-support radius search can use the following recursion.

```text
Solve(x, A, r):
    replay x exactly
    if x is universal: return x
    if r == 0: fail
    choose one canonical current hole h
    if rho_A(h) > r: fail
    enumerate every corridor portal packet (Q,v), |Q| <= r
    for each packet:
        z = x with Q simultaneously assigned v
        apply only proved support/piercing lower bounds
        Solve(z, A \ Q, r - |Q|)
```

Induction on `r` using the atomic packet theorem proves completeness.  A
repeated chronological edit at one position is normalized to its final value;
no-op assignments are excluded.  Deduplication must retain the actual rooted
word (or an exact equivalent state), not merely its hole set or count-delta
vector.

The following restrictions are unsound without an additional theorem:

- requiring every individual edit to be a provider;
- bounding the number of intermediate holes or debts;
- discarding a packet because it temporarily destroys a blocker;
- equating states from identical hole counts, singleton/doubleton counts, or
  raw multiplicities; and
- treating a selected local support as globally exhaustive.

Verified automorphisms of the rooted word/support instance and literal
duplicate packets are safe symmetry reductions.  All terminal candidates
must undergo independent full contiguous-OR replay.
