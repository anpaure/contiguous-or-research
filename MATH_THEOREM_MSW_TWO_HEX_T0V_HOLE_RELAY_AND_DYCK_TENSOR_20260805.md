# An exact two-hex MSW relay repairs the entire `T_0V` q2 family

**Date:** 2026-08-05  
**Method:** explicit canonical-path incidences and the exact `Gamma` inverse
criterion; no solver  
**Status:** unconditional for the canonical MSW q2 factor.  The construction
repairs the `Cat_(r-6)` targets `T_0V` and preserves every target that was
already covered.  It does **not** assert that all other canonical q2 holes are
repaired.

## 0. Result

Use one-based coordinates in a twelve-coordinate prefix and put

```text
T0 = 110011001111,
B  = 101111001101.
```

In the canonical semilength-six MSW factor there are two alternating
incidence hexagons `H1,H2` with the following effect on the upper-q2 turn
multiset.

```text
H1:
  101111001101  -> 101110001111
  100011101111  -> 101011101101
  111010001111  -> 110011001111

H2:
  101111010101  -> 101111001101
  101001111101  -> 101011110101
  101011101101  -> 101001111101
```

The first switch creates `T0` and moves the unique hole to `B`.  The second
switch recreates `B`.  After both switches every target covered before the
switches is still covered.

For every `r>=6` and every Dyck word `V` of semilength `r-6`, append `V` on
fresh coordinates to every displayed prefix.  The same two hexagons remain
alternating, their complete multiplicity ledger is unchanged, and their
support is disjoint from the support belonging to any other suffix `V'`.
Consequently all `Cat_(r-6)` missing targets

```text
                         T0 V
```

can be inserted simultaneously without deleting any previously represented
q2 target.

On the lifted odd middle-levels two-factor, the two switches merge five MSW
wreath cycles into one.  Thus applying the macro for every suffix lowers the
component count by exactly

```text
                         4 Cat_(r-6).
```

All changed incidences lie in the first six edges of their canonical paths.
Hence, whenever `h<=r-6`, the reverse depth-`h` stem at the suffix-side
endpoint of every affected path is literally untouched.

## 1. The five canonical prefix paths

For a Dyck root `x`, write the rank-six owners of its canonical MSW path as

```text
X_0(x), X_1(x), ..., X_6(x).
```

Only the following five roots occur in the construction.  Their owner rows
are displayed completely, so every selected-incidence claim below can be
checked simply by taking the union of adjacent rows.

```text
x0 = 111111000000
  111111000000
  101111000001
  101011000101
  101010010101
  101000110101
  100000111101
  000000111111

x1 = 111110100000
  111110100000
  101110100001
  101010100101
  101001100101
  101001010101
  100001011101
  000001011111

x2 = 111110010000
  111110010000
  101110010001
  101110000101
  101010001101
  101001001101
  100001101101
  000001101111

x11 = 111100110000
  111100110000
  101100110001
  101001110001
  100011110001
  100011100101
  100011001101
  000011001111

x62 = 110101110000
  110101110000
  110100110001
  110100100101
  110100001101
  110000001111
  100010001111
  001010001111
```

The labels `x11,x62` are names, not numerical operations.  They record the
indices of these paths in the canonical semilength-six list.

For an owner `O`, let `Q^-` be the selected rank-seven colour deleted by a
switch, `Q^+` the unselected colour inserted by it, and `E` the other
selected colour at `O`.  The old and new q2 turns are respectively

```text
                         E union Q^-,
                         E union Q^+.
```

## 2. First hexagon: `T0` is created and the hole moves to `B`

The first hexagon has rank-five core and cyclic active triple

```text
S1 = {1,5,9,10,12},       (a,b,c) = (3,6,11).
```

It is the reverse orientation of the incidence hex on that data.  Its three
literal incidence checks are:

| owner `O` | canonical position | deleted selected `Q^-` | inserted unselected `Q^+` | other selected `E` | old q2 turn | new q2 turn |
|---|---:|---|---|---|---|---|
| `101010001101` | `x2,j=3` | `101011001101` (`x2`, edge 3) | `101010001111` (`x62`, edge 5) | `101110001101` (`x2`, edge 2) | `101111001101` | `101110001111` |
| `100011001101` | `x11,j=5` | `100011001111` (`x11`, edge 5) | `101011001101` (`x2`, edge 3) | `100011101101` (`x11`, edge 4) | `100011101111` | `101011101101` |
| `100010001111` | `x62,j=5` | `101010001111` (`x62`, edge 5) | `100011001111` (`x11`, edge 5) | `110010001111` (`x62`, edge 4) | `111010001111` | `110011001111` |

Every `Q^-` is visibly the union of the owner at the displayed position and
the next owner in the corresponding path.  Every `Q^+` is a canonical edge
colour on another displayed path, but its incidence with the owner in its
row is not selected.  The three `Q^-` colours are the three `Q^+` colours in
cyclic order.  Hence the six owner-colour incidences form an alternating
hexagon, and toggling it preserves every owner degree and every q1-colour
degree.

## 3. Second hexagon: the transported hole closes

The second hexagon has

```text
S2 = {1,3,6,10,12},       (a,b,c) = (5,8,9),
```

again in the reverse orientation.  Its three incidence checks are:

| owner `O` | canonical position | deleted selected `Q^-` | inserted unselected `Q^+` | other selected `E` | old q2 turn | new q2 turn |
|---|---:|---|---|---|---|---|
| `101011000101` | `x0,j=2` | `101011010101` (`x0`, edge 2) | `101011001101` (`x2`, edge 3) | `101111000101` (`x0`, edge 1) | `101111010101` | `101111001101` |
| `101001010101` | `x1,j=4` | `101001011101` (`x1`, edge 4) | `101011010101` (`x0`, edge 2) | `101001110101` (`x1`, edge 3) | `101001111101` | `101011110101` |
| `101001001101` | `x2,j=4` | `101011001101` (`x2`, edge 3) | `101001011101` (`x1`, edge 4) | `101001101101` (`x2`, edge 4) | `101011101101` | `101001111101` |

This is another alternating hexagon by the same direct adjacent-owner
check.

The owner sets of `H1` and `H2` are disjoint.  Their twelve toggled
incidences are also disjoint.  The two hexagons share exactly one q1 colour,

```text
                         Q = 101011001101.
```

This is a useful relay, not a collision.  Initially `Q` is selected at the
two owners `X_3(x2)` and `X_4(x2)`.  The first switch replaces the former
incidence by the incidence at `X_5(x11)`; the second replaces the latter by
the incidence at `X_2(x0)`.  Thus `Q` has degree two before, between, and
after the switches.  The switches commute as incidence toggles, although
the displayed order is the convenient order for reading the one-hole q2
relay.

## 4. Exact q2 multiplicities

For a rank-eight binary word `Z` of length twelve, the exact MSW `Gamma`
inverse criterion counts pairs `p<q` of up-step positions satisfying:

1. the step at `p` starts at height zero or one;
2. the step at `q` starts at height two or three;
3. no intervening down-step starts at height two or three; and
4. the number of height-zero up-steps before `p` equals the number of
   height-three up-steps after `q`.

For every target used by the macro, the complete candidate-pair list is:

| target | inverse pairs | multiplicity |
|---|---|---:|
| `101111001101` | `(4,6)` | 1 |
| `101110001111` | `(3,5)` | 1 |
| `100011101111` | `(1,12),(7,11)` | 2 |
| `101011101101` | `(5,7)` | 1 |
| `111010001111` | `(2,3),(9,11)` | 2 |
| `110011001111` | none | 0 |
| `101111010101` | `(1,12),(3,10),(4,8)` | 3 |
| `101001111101` | `(1,12),(3,10),(7,9)` | 3 |
| `101011110101` | `(1,12),(3,10),(5,8),(6,7)` | 4 |

The table is a direct exhaustive application of the four displayed inverse
conditions; it uses no search hypothesis.

Before `H1`, the relevant multiplicities are therefore

```text
B:1, 100011101111:2, 111010001111:2,
101110001111:1, 101011101101:1, T0:0.
```

After `H1` they are

```text
B:0, 100011101111:1, 111010001111:1,
101110001111:2, 101011101101:2, T0:1.
```

For `H2`, the old multiplicities at that moment are

```text
101111010101:3,
101001111101:3,
101011101101:2.
```

The new targets are `B`, `101011110101`, and `101001111101`.  Hence after
`H2`:

```text
B:1,
101111010101:2,
101011101101:1,
101001111101:3,          # one deletion and one insertion cancel
101011110101:5,
T0:1.
```

Every target deleted by either hex remains represented after the complete
two-hex macro.  This proves exact q2 closure for the base prefix.

## 5. Dyck-suffix tensor theorem

Let `V` be a Dyck word of semilength `r-6`, supported on coordinates
`13,...,2r`, and write `U(V)` for its up-step set.  For any displayed
prefix mask `Z`, put

```text
                         Z[V] = Z union U(V).
```

### Theorem 5.1 (literal tensoring)

Replacing every owner, q1 colour, and q2 target in Sections 2--4 by its
`[V]` version gives the same pair of alternating hexagons inside the
canonical semilength-`r` MSW factor.  Every q2 multiplicity in Section 4
is unchanged.

#### Proof

For Dyck words `x,V`, the canonical MSW insertion and deletion orders
concatenate:

```text
I(xV) = I(x) followed by (12+I(V)),
D(xV) = D(x) followed by (12+D(V)).
```

Therefore the first six Johnson exchanges on `P_(xV)` are exactly the six
exchanges on `P_x`; the suffix up-set `U(V)` is present throughout those
six exchanges.  Taking `x` among the five roots of Section 1 tensors every
selected edge, every unselected incidence, and every other selected colour
in the two literal tables by the same common suffix set.  Both hexagons
remain alternating.

For multiplicity, every displayed rank-eight prefix ends at path height
four.  Reading a Dyck suffix from height four introduces no up-step starting
at heights zero, one, two, or three, no down-step starting at height two or
three, and no height-three up-step to the right of a prefix candidate.
Thus the complete candidate list in the exact `Gamma` inverse criterion is
unchanged.  The table in Section 4 is therefore the exact multiplicity table
for `Z[V]` as well.  `square`

### Corollary 5.2 (pairwise-disjoint simultaneous repair)

If `V!=V'`, then `U(V)!=U(V')`.  The suffix-coordinate projection of every
owner and colour in the packet for `V` is exactly `U(V)`.  Hence packets for
different suffixes have disjoint owner sets, colour sets, incidence sets,
and q2-target sets.

All `Cat_(r-6)` packets may consequently be toggled simultaneously.  They
create every `T0V`, and no target represented by the original canonical
factor is lost.

## 6. Exact topology effect

In the lifted odd middle-levels factor, each Dyck root labels one MSW wreath
cycle.  For a fixed suffix `V`, `H1` uses one internal incidence in each of

```text
                         x2 V, x11 V, x62 V.
```

Deleting one edge from each of three distinct cycles and reconnecting them
cyclically by an alternating hex produces one cycle.  Thus `H1` merges those
three cycles and lowers the component count by two.

Next `H2` uses the cycles rooted at

```text
                         x0 V, x1 V, x2 V.
```

The `x2V` incidence now lies in the component just created by `H1`, while
the `x0V` and `x1V` cycles are untouched.  Therefore `H2` again merges three
distinct components into one and lowers the component count by two.  The
five original wreath cycles become one, for a net change of `-4`.

Different suffix packets are support-disjoint, so their component changes
add.  Starting from the canonical lifted factor with `Cat_r` cycles, after
all packets the number is exactly

```text
                         Cat_r - 4 Cat_(r-6).
```

On the even-ground z-free half, all toggled owners are internal.  Hence all
original path endpoints and their degrees survive.  The operation re-pairs
the five forward endpoints with the five reverse endpoints; it does not
consume an endpoint.  This is the path-level form of the cycle merges after
the fixed closure edges are restored.

## 7. Protected reverse stems

The six changed owners occur at canonical positions

```text
x0: 2,       x1: 4,       x2: 3 and 4,
x11: 5,      x62: 5.
```

Every deleted or inserted q1 colour belongs to one of the first six prefix
edges, with edge index at most five.  Under concatenation with `V`, these
indices do not change.

The reverse depth-`h` stem of a semilength-`r` path uses edge indices

```text
                         r-h, ..., r-1.
```

If `h<=r-6`, then `r-h>=6`, so this entire stem is incidence-disjoint from
the two-hex support.  Every rethreaded path still has one forward and one
reverse endpoint, and the reverse endpoint segment is unchanged.  Thus each
affected path can be oriented from an untouched suffix-side depth-`h` stem.

This proves literal protected-stem avoidance for the asymptotic regime in
which the required deadline satisfies `h<=r-6`.  It does not prove that an
independently prescribed global sign pattern or a later Hamiltonization
chooses all of these orientations simultaneously.

## 8. Exact scope

The theorem proves all of the following:

* exact owner and q1-palette preservation;
* repair of every `T0V` q2 hole;
* no loss of any previously represented q2 target;
* pairwise-disjoint tensoring over all Dyck suffixes;
* a component reduction of `4 Cat_(r-6)` in the lifted factor; and
* an untouched reverse depth-`h` stem when `h<=r-6`.

It does **not** prove:

* full q2 surjectivity of the rethreaded canonical factor;
* preservation or completion of upper widths `q>=3`;
* a global residence orientation compatible with every later connector;
* a lower common-cap compiler; or
* `nu(k)=B(k)+O(1)`.

The result is nevertheless a literal Catalan-scale repair macro for the
specific infinite missing family that previously supplied the canonical
MSW q2 obstruction.  The remaining q2 problem is the classification and
repair of the other missing-language classes, not the `T0V` family.
