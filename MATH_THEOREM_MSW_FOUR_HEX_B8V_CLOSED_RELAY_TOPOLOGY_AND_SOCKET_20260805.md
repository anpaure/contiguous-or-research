# A four-hex MSW relay repairs every `11101101 V` q2 hole

**Date:** 2026-08-05  
**Method:** explicit MSW touching-step rules, exact base multiplicities, and
Dyck concatenation; no solver  
**Status:** unconditional for the displayed canonical MSW cylinder.  The
q2 repair is exact and length-neutral.  It exports one two-edge z-free path
socket per suffix; it does not prove the all-q upper theorem.

## 0. Outcome

Work first on eight prefix coordinates and write a rank-six target by the
two-coordinate complement of its one-set.  The canonical semilength-four
MSW q2 multiplicities needed below are

```text
complement: 24 47 46 37 36 45 35 34 38 28
base load:   2  0  1  1  1  2  1  1  1  2.
```

In particular

```text
B8 = 11101101,  complement 47,
B1 = 11101011,  complement 46,
C1 = 11011101,  complement 37.
```

There is a sequence of four alternating owner--q1-colour hexagons with
signed complement-pair currents

```text
H0: +47 +36 -46 -37,
H1: +46 +35 -45 -36,
H2: +37      -38,
H3: +38      -28.
```

Therefore the complete macro has current

```text
                         +47 +35 -45 -28.
```

It raises the missing target `B8` from load zero to one, raises complement
`35` from one to two, and lowers the two redundant targets `45,28` from
two to one.  Every target covered before the macro remains covered.

For every Dyck suffix `V`, the same macro tensors literally to the target
`B8 V`.  Distinct suffixes give disjoint supports.  Thus all
`Cat_(r-4)` members of the classical hereditary family `11101101 V` are
repaired simultaneously.

On the lifted odd factor the macro turns six canonical wreath cycles into
one, a component change of `-5` per suffix.  On the z-free half it leaves
six paths and all twelve endpoints, but one resulting path has exactly two
edges and joins two forward endpoints.  This is the precise socket exported
by the construction.

## 1. Incidence notation

For a rank-four owner `O`, its two canonical selected rank-five colours are
obtained by adjoining the `d_0(O)`-th and `(d_0(O)+1)`-st down-steps touching
height zero.  Equivalently they are `g'(O)` and `g(O)`.  At a Dyck endpoint
only `g(O)` occurs in the z-free path.

In each table, `Q^-` is the selected incidence removed by the hexagon,
`Q^+` is the unselected incidence inserted, and `E` is the other selected
colour at an internal owner.  Its q2 turn changes from `E union Q^-` to
`E union Q^+`.  Endpoint rows have no q2 turn.

## 2. `H0`: create `B8`, exposing `B1,C1`

Use

```text
S0={1,5,8},          active cycle (6,7,2).
```

| owner | `Q^-` | `Q^+` | `E` | old turn | new turn | complement change |
|---|---|---|---|---|---|---|
| `10001101` | `10001111` | `11001101` | `10101101` | `10101111` | `11101101` | `24 -> 47` |
| `10001011` | `11001011` | `10001111` | `10101011` | `11101011` | `10101111` | `46 -> 24` |
| `11001001` | `11001101` | `11001011` | `11011001` | `11011101` | `11011011` | `37 -> 36` |

The touching-step rule gives selected additions `{3,7}`, `{2,3}`, and
`{4,6}` at the three owners.  Hence every `Q^-` is selected and every
`Q^+` unselected.  The three colours cycle, so this is an alternating
hexagon.  Its net current is the stated current of `H0`.

## 3. `H1`: restore `B1` without a new hole

After `H0`, use

```text
S1={1,7,8},          active cycle (5,6,2).
```

| owner | `Q^-` | `Q^+` | `E` | old turn | new turn | complement change |
|---|---|---|---|---|---|---|
| `10001011` | `10001111` | `11001011` | `10101011` | `10101111` | `11101011` | `24 -> 46` |
| `10000111` | `11000111` | `10001111` | `10100111` | `11100111` | `10101111` | `45 -> 24` |
| `11000011` | `11001011` | `11000111` | `11010011` | `11011011` | `11010111` | `36 -> 35` |

At the first owner, `H0` changed the selected pair from `{2,3}` to
`{6,3}`; `H1` changes it back.  The other selected pairs are canonically
`{2,3}` and `{4,5}`.  Thus the three checks are literal.  Complement `45`
has load two and complement `36` has load two after `H0`, so no target is
lost.  At this point `B8` and `B1` are both covered; only `C1` is missing.

## 4. `H2`: move the remaining hole from `37` to `38`

Use

```text
S2={1,2,6},          active cycle (8,7,4).
```

| owner | `Q^-` | `Q^+` | `E` | old turn | new turn | complement change |
|---|---|---|---|---|---|---|
| `11000101` | `11000111` | `11010101` | `11001101` | `11001111` | `11011101` | `34 -> 37` |
| `11000110` | `11010110` | `11000111` | `11001110` | `11011110` | `11001111` | `38 -> 34` |
| `11010100` | `11010101` | `11010110` | endpoint | none | none | none |

The first two owners have canonical selected additions `{5,7}` and
`{4,5}`.  The third word `11010100` is Dyck, and its unique z-free
endpoint colour is obtained by adjoining `8`.  Hence the incidence checks
are exact.  Complement `34` cancels between the two internal rows, so the
net q2 effect is `+37-38`.

## 5. `H3`: consume one redundant `28` provider

Finally use

```text
S3={1,4,7},          active cycle (6,3,2).
```

| owner | `Q^-` | `Q^+` | `E` | old turn | new turn | complement change |
|---|---|---|---|---|---|---|
| `10010110` | `10110110` | `11010110` | `10011110` | `10111110` | `11011110` | `28 -> 38` |
| `10110010` | `11110010` | `10110110` | endpoint | none | none | none |
| `11010010` | `11010110` | `11110010` | endpoint | none | none | none |

At the internal owner the touching-step candidates give selected additions
`{3,5}`.  Both other owner words are Dyck.  Their unique endpoint additions
are respectively `2` and `6`.  Thus `H3` is alternating and has the sole q2
effect `28 -> 38`.  Since complement `28` has canonical load two, it remains
covered.

The colour

```text
                         11010110 = {1,2,4,6,7}
```

is the relay shared by `H2,H3`.  Initially its selected endpoints are the
second owner of `H2` and the third owner of `H3`.  `H2` moves the former
endpoint to its Dyck endpoint row; `H3` moves the latter to its internal
row.  Its degree is two throughout.

## 6. Exact multiplicity proof

The complete semilength-four `Gamma` complement table gives, for the ten
values used above,

```text
24:2, 47:0, 46:1, 37:1, 36:1,
45:2, 35:1, 34:1, 38:1, 28:2.
```

Equivalently these counts follow by applying the exact height/corridor/
ordinal inverse test to the corresponding six-one words.  Applying the
four signed ledgers in order gives

```text
after H0: 47=1, 46=0, 37=0, 36=2;
after H1: 46=1, 45=1, 36=1, 35=2;
after H2: 37=1, 38=0, 34=1;
after H3: 38=1, 28=1.
```

All unlisted multiplicities are unchanged.  This proves complete q2
coverage preservation and the final net current

```text
                         +47+35-45-28.
```

## 7. Dyck-suffix tensoring

Let `V` be Dyck of semilength `r-4`, on coordinates `9,...,2r`, and append
its up-set to every mask in Sections 2--5.

The MSW insertion and deletion orders concatenate on Dyck words.  Therefore
the first four edges of every path rooted at `xV` are the displayed
semilength-four edges with the common suffix up-set adjoined.  Every
selected and unselected incidence check remains valid.

Every displayed q2 prefix ends at height four.  A Dyck suffix read from
height four introduces no eligible low or high step and no forbidden
height-two/three barrier in the exact `Gamma` inverse test.  Hence every
base multiplicity in Section 6 remains exact after appending `V`.

The three endpoint owners used in `H2,H3`,

```text
11010100, 10110010, 11010010,
```

are Dyck roots.  Their concatenations with `V` are again full forward
endpoints, not newly internal states.  Thus the endpoint rows continue to
carry no q2 turn; no hidden suffix-boundary target enters the ledger.

Distinct Dyck words have distinct up-sets.  Projection to suffix coordinates
therefore proves that packets for different `V` have disjoint owners,
colours, incidences, and q2 targets.  All `Cat_(r-4)` packets commute.

## 8. Exact topology and the exported short socket

The six canonical roots involved are

```text
A=11110000, B=11010100, C=11011000,
D=11010010, E=11100010, F=10110010.
```

Write `R_0,R_r` for the forward and reverse endpoints of path `R`.  Directly
tracing the six changed canonical edges through `H0,H1,H2,H3` gives the
following six z-free paths:

```text
A_0 -- D_r,
C_0 -- B_r,
C_r -- A_r,
D_0 -- F_r,
F_0 -- E_0,
E_r -- B_0.
```

The path `F_0--E_0` consists of exactly two Johnson edges (equivalently,
four owner--colour incidence edges).  In owner-only notation it is

```text
                         F_0 -- E_1 -- E_0,
```

where the first Johnson edge uses the old `E` edge-1 colour and the second
uses the unchanged edge-0 colour.  Its length is independent of the suffix
length.

The fixed lifted closure pairs `R_0` with `R_r` for each root.  Alternating
the six displayed path pairings with those six closure pairings gives the
single cycle

```text
A0-D_r-D0-F_r-F0-E0-E_r-B0-B_r-C0-C_r-A_r-A0.
```

Hence six lifted wreath cycles become one: the component count changes by
exactly `-5` per suffix, and by `-5 Cat_(r-4)` over the complete suffix
family.  There is no topology debt in the lifted factor.

All changed incidences have prefix edge index at most three.  Thus every
reverse depth-`h` stem, which uses edges `r-h,...,r-1`, is untouched whenever
`h<=r-4`.  All six original reverse stems survive literally.  However the
new z-free path `F_0--E_0` contains no reverse endpoint and has only two
edges.  Consequently a theorem requiring one depth-`h` stem on every
z-free path still has exactly one unmatched short-path socket per suffix.

This distinction is important: the lifted cycle topology improves, while
the pathwise protected-stem interface exports a Catalan-scale socket family.

## 9. Scope

Proved:

* exact q1/owner preservation;
* exact repair of every `11101101V` q2 hole;
* no loss of any old q2 target;
* support-disjoint tensoring over all Dyck suffixes;
* lifted component gain `5 Cat_(r-4)`; and
* a complete endpoint/stem ledger, including the unique two-edge socket.

Not proved:

* repair of the other suffix-irreducible chambers in the full q2 language;
* absorption of the short sockets into a uniform protected-stem factor;
* preservation or telescoping of upper widths `q>=3`;
* residence and the lower common-cap compiler; or
* `nu(k)=B(k)+O(1)`.

The next exact question is whether the short sockets can be paired by the
two-rail matched-hook construction while the higher-width changes of a
matched pair telescope.
