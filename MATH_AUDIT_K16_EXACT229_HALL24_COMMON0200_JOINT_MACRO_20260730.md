# K16 exact229 Hall24/common-`0200` joint macro: a scoped no-go and the exact next port

## 1. Statement

Let (T_{229}) be the authenticated exact/upper-complete carrier

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
```

and let (T_{24}) be the literal length-three block swap

```text
[6608,6611) <-> [12714,12717)
```

in

```text
scratch/s4_exact229_swap6608_12714_l3_20260730.targets.
```

The latter has exact middle replay, capacity (32063), generalized matching
(26308/26332), and sole arbitrary-upper hole `4e79`.  Its matching gain is
the new provider of `4e70` carried by the imported block at `6608`; its upper
loss is the destroyed unique interval

```text
[12713,12715) = 4a79,4e78.
```

Relative to (T_{24}), the two desired late cell edges are

```text
6a29 -- (4654,4655,4656),
4a29 -- (4655,4656).
```

Adding just these two edges to the exact (T_{24}) generalized Hall graph
raises its matching from (26308) to (26310).  Thus a physical macro that
retains the Hall24 graph and realizes the common-`0200` halo would rigorously
give deficiency (24\to22).

### 1.1 Exact split of the three Hall paths

Write the lower deficiency as `deficiency = Z + S`, where `Z` is the number
of degree-zero lower targets and `S` is the deficiency after deleting them.
Direct matching replay gives:

| graph | deficiency | Z | S |
|---|---:|---:|---:|
| `exact229` | 25 | 12 | 13 |
| Hall24 | 24 | 11 | 13 |
| Hall24 + `6a29` edge | 23 | 10 | 13 |
| Hall24 + `4a29` edge | 23 | 11 | 12 |
| Hall24 + both halo edges | 22 | 10 | 12 |

Thus the path roles are exact:

* `4e70` is degree zero in `exact229`; Hall24 creates its unique edge
  `(12714,12715)`. This is the first zero-provider path.
* `6a29` remains degree zero in Hall24; halo cell
  `(4654,4655,4656)` is the second zero-provider path.
* `4a29` is not degree zero. Its new halo edge closes the
  shared-component augmenting path

  ```text
  5a29 -- (6025,6026,6027) -- 4a29 -- (4655,4656).
  ```

  Accordingly it lowers `S`, not `Z`.

Hall24 has one upper hole, so its basin potential is
`Z + H_upper = 11 + 1 = 12`, while the shared term is 13. Closing `4e79`
and adding only the `6a29` edge pays the upper and zero-provider terms but
leaves the shared term unchanged; the independent `4a29` path is necessary
for the full three-unit lower improvement.

The natural joint collar does **not** realize this conditional gain.  More
precisely:

1. all (81) literal five-site (X\times F) commutators fail exact middle
   replay or the forced three-flat schedule;
2. the failure has a common solver-free `8000` carrier certificate;
3. the smallest fixed-schedule destination enlargement is forced to change
   row `12717`, and its complete rank-eight port list is explicit below;
4. all (504) resulting oriented seven-site decks fail exact middle replay;
5. even allowing all six assignments of the three displaced receiver tokens
   gives (3024) failures.

This is a scoped no-go for these literal commutators, not for arbitrary block
braids or extra donor rows.

## 2. Natural five-site commutator

The exact seam-token set at row `3846`, excluding incumbent `6b29`, is

```text
2b39 2ba9 2bb1 2bb8 6b31 6b38 6ba1 6ba8 6bb0.
```

There are nine physical rank-eight facet occurrences (F\ne\texttt{4a79})
whose union with `4a79` is `4e79`:

```text
4c79@3105  4e69@4347  4e39@4507  4e59@4606
0e79@6060  4e71@6320  4e71@6321  4e78@6608
4679@12826.
```

For (X) at (p_X) and (F) at (p_F), test the literal occurrence cycle

```text
positions  [3846,pX,12714,pF,4653]
old values [6b29,X, ce38, F, 69a9]
new values [X,   ce38,F, 69a9,6b29].
```

It places a seam-compatible token at `3846`, restores the adjacent upper
union at `12713`, and places `6b29` at `4653`.  The exact census is:

```text
raw physical cases                         81
cases retaining the Hall block at 6608     72
cases retaining the exact common-0200 halo 72
cases satisfying both local objectives     64
forced-flat schedule failures               18
exact-middle passes                          0
```

The distinction between (81) and (72) Hall-compatible cases matters:
using the unique `4e78@6608` as (F) removes the very token that creates the
Hall24 provider.  Independently, `X=6ba1@4652` changes the left neighbour of
the two halo cells, so it does not realize their claimed signatures.  The
two `4e71` occurrences are the eighteen schedule failures because moving
either member destroys the forced flat at `6320`.

## 3. Solver-free incompatibility

At rows `12714`--`12717` the forced depth is two.  Put any restoring facet
(F\subseteq\texttt{4e79}) at row `12714`.  Every such facet omits bit
`8000`, while

```text
T[12715] = cc3c  contains 8000,
T[12717] = 4e2e  omits    8000.
```

The only three envelope cells available to replay row `12715` are

\[
\begin{aligned}
E_{12715}&=T_{12713}\cap F\cap T_{12715},\\
E_{12716}&=F\cap T_{12715}\cap T_{12716},\\
E_{12717}&=T_{12715}\cap T_{12716}\cap T_{12717}.
\end{aligned}
\]

The first two omit `8000` because they contain (F); the third omits it
because it contains incumbent `4e2e`.  Hence

\[
 8000\not\subseteq E_{12715}\cup E_{12716}\cup E_{12717},
\]

contradicting exact replay of `cc3c`.  This proves all fixed-neighbour cases
at once.  In the fixed depth-two schedule, any successful enlargement must
therefore change row `12717` (or make a more radical change that alters this
local schedule).

## 4. Exact two-row destination port

Allow only rows `12714` and `12717` to vary. Require row `12714` to be a
rank-eight facet restoring `4e79`, row `12717` to remain rank eight, and keep
every other target row and the numerical depth schedule fixed.
Coordinatewise replay first gives the following **algebraic pre-flat** list.

For

```text
F in {0e79,4c79,4e39,4e59,4e78},
```

the allowed row-`12717` masks are

```text
c26e c46e c62e c666 c86e ca2e ca66 cc2e cc66 ce26.
```

For `F=4679`, they are

```text
c86e ca2e ca66 cc2e cc66 ce26.
```

For `F=4e69` or `F=4e71`, there is no rank-eight row-`12717` value. Every
listed value has a unique physical occurrence in the authenticated word.

There are two necessary scope corrections.

1. `Y=cc2e` equals fixed row `12716`, so placing it at `12717` creates an
   additional flat. It belongs to the algebraic pre-flat list but not to the
   frozen-three-flat two-row atlas. It can occur in the later coupled deck
   only because its unique source at `12716` is changed simultaneously.
2. `F=4e78` uses the unique occurrence at `6608`, so it destroys the Hall24
   provider block and is not Hall-compatible.

Consequently the exact physical frozen-three-flat, Hall-compatible port is:

```text
F in {0e79,4c79,4e39,4e59}:
  Y in {c26e,c46e,c62e,c666,c86e,ca2e,ca66,cc66,ce26};

F=4679:
  Y in {c86e,ca2e,ca66,cc66,ce26}.
```

It has exactly `4*9+5=41` pairs. The larger algebraic list has 56 pairs;
after exact flat recount it has 50; imposing Hall retention leaves the
displayed 41. These are exact port signatures, not heuristic candidate lists.

The choice `Y=ca2e` uses the unique occurrence immediately at row `6611`,
the first row after the protected Hall block `[6608,6611)`. Excluding this
protected-closure contact removes one choice for each of the five admissible
facets, so exactly `41-5=36` tail pairs avoid it.

They are nevertheless a **local interface**, not a completed occurrence
permutation. Naively making just these two row substitutions closes `4e79`
but never preserves the complete upper deck: 14 of the 41 pairs leave sole
debt `ce3c`, and the other 27 leave debts `{ce2e,ce3c}`. Thus a literal macro
must return the displaced `ce38,4e2e` occurrences in a way that restores
those witnesses without changing the three Hall-path cells. No pair in the
41-entry tail atlas is upper-complete by itself.

## 5. Seven-site and receiver-complete no-go

For every allowed triple (X,F,Y), test the uniquely oriented extension

```text
[3846,pX,12714,pF,12717,pY,4653]
```

by passing each old token to the preceding displayed position.  There are
exactly (504) physical cases, (414) of which retain the Hall-producing
block at `6608`.  None has exact middle replay.

The audit also releases the orientation while keeping the four desired
values

```text
T[3846]=X, T[12714]=F, T[12717]=Y, T[4653]=6b29.
```

The receiver positions (p_X,p_F,p_Y) must then receive the displaced values
`ce38,4e2e,69a9` in some order.  All (6\cdot504=3024) assignments fail.
Among the (2484) assignments retaining the Hall block, at least two middle
rows fail.  The four one-row near misses all use `F=4e78@6608`, hence destroy
the Hall24 gain and are not joint candidates.

A representative Hall-compatible minimum has

```text
X=2b39@437, F=4e59@4606, Y=ca2e@6611,
receivers [pX,pF,pY] <- [ce38,69a9,4e2e],
```

and fails exactly at

```text
row437  missing c400,
row4606 missing 01a0.
```

Thus the next genuinely live physical object is not another choice of the
same ports: it needs an additional source-collar absorber for these returned
tokens (or a block braid changing their neighbourhoods).

## 6. Scope and implication

The positive statement is conditional and exact: if a future exact,
upper-complete macro preserves the Hall24 graph and installs the two displayed
halo edges, generalized deficiency is at most (22).

The negative theorem closes only:

* the stated five-site (X\times F) commutator;
* the exact two-row destination enlargement;
* the stated seven-site orientation; and
* all permutations of its three receiver values.

It does not close extra donor rows, a change of the depth/flat schedule,
longer occurrence cycles, or nonlocal block rethreading.  Since every tested
joint word is middle-inexact, none is eligible for arbitrary-upper or Hall
acceptance; no compiler improvement is claimed.

The known separate `8000`-provider marginal trade has upper debt `4e7e`.
It is not an alternative completion of the present port: its advertised
`4e79` witness and Hall24's provider both require source occurrence `12714`
at incompatible physical positions. Hence `4e7e` remains a reciprocal-trade
route requiring a wider occurrence braid, not a hidden member of the
41-pair fixed-tail atlas.

## 7. Frozen authority

```text
scratch/audit_k16_exact229_hall24_common0200_joint_macro_20260730.py
SHA256 93f0d51bc66f35d7110b681ad553e9666a53bba05135d22cd130cba3c411617f

scratch/k16_exact229_hall24_common0200_joint_macro_20260730.audit.json
SHA256 67bb5812fc1a6ed1e5918ffce855fb93376baefb908f7fdccbaad07be2f45b85
payload 8ab08822fb78dd489756983a2053b8d302fe8559f073b7c52a5833a1c18fa264
```

Authenticated inputs:

```text
exact_229.targets
cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974

s4_exact229_swap6608_12714_l3_20260730.targets
955dc2fb350cd399f050e4dafb481925633e0024eaa438ee3cf4f984e0acb995

s4_exact229_swap6608_12714_l3_20260730.audit.json
a4bd251a95e51dce73bdfa8dc7ba440a70eccb458542cea5987d704a8efbcd30

s4_exact229_swap6608_12714_l3_20260730.hall.json
898d565fac11171de48bc714379317f4a61780d25e9fa49f5a3a64f5c68fd281

k16_exact229_hall24_two_trade_join_20260730.audit.json
5a0a3c56dd4c70e4c1b0aa2f8dcc91fb0275e673219e8105b967462cd1ab6f17
```
