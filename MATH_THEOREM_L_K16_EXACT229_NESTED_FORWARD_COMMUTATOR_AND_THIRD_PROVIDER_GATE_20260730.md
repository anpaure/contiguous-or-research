# Exact229 nested forward commutator and third-provider gate

Date: 2026-07-30  
Status: **four exact/all-upper Hall-24 carriers authenticated; exact local
Hall-23 provider signatures proved; no physical Hall-23 successor claimed**

## 1. Result

Start with the authenticated exact229 target chronology

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA-256 cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974.
```

For `L in {16,18}` and `l in {9,13,15}`, perform, without reversal,

```text
[6611,6611+L)  <-> [12718,12718+L),
[6613,6613+l)  <-> [12721,12721+l).
```

Exactly four of the six named compositions are middle-exact,
arbitrary-upper-complete, and generalized Hall-24:

| `(L,l)` | frozen word | SHA-256 | incidences | Hall shore `L/R` |
|---|---|---|---:|---:|
| `(16,9)` | `pass_33.targets` | `2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec` | 347649 | 211/187 |
| `(16,13)` | `pass_46.targets` | `bf3ee02110f70c168dc9863e1c8258cc54debfa408dd4c97fe5b57c6a4116754` | 347809 | 211/187 |
| `(18,9)` | `pass_35.targets` | `42420e0eea7102a07227b25e49663a127f89219b8c41cb18ee7de699385d9b04` | 347649 | 198/174 |
| `(18,15)` | `pass_55.targets` | `e1166c6ae5f6c671c779bfb9f692fa8332aa7b9978cfcd93671b64244c5f1f69` | 347737 | 198/174 |

Every row has rank eight, the only flats remain `6320,12869,12871`, the
proper-prefix cell capacity is 32,063, all upper masks occur, and the complete
26,332-left-target matching is 26,308.  Hence the deficiency is 24.

The two other nominal words are not carriers:

* `(16,15)` is not nested in the right outer destination.  Rows 6627 and
  12735 respectively lose carriers `0010` and `8000`, and upper mask `cda5`
  is absent.
* `(18,13)` is upper-complete but rows 12734 and 12735 both lose their
  `8000` carrier.

Their canonical word hashes are respectively `155c4188...2415` and
`2f53858e...be06`.  Thus the authenticated family has four carriers, not six.

## 2. Boundary-cancellation normal form

Put `a=6611`, `b=12718`,

\[
 A=W[a,a+L),\qquad B=W[b,b+L).
\]

After the outer exchange the left destination contains `B` and the right
destination contains `A`.  The inner exchange begins at offsets two and
three.  Therefore, whenever `l<=L-3`, the final destinations are exactly

\[
\begin{aligned}
 L'&=B[0,2)\,A[3,3+l)\,B[2+l,L),\\
 R'&=A[0,3)\,B[2,2+l)\,A[3+l,L).       \tag{2.1}
\end{aligned}
\]

All successor relations internal to the displayed chunks cancel from the
boundary difference.  The four start-side seams are invariant across the
four valid carriers:

| cut after | source labels | values | union |
|---:|---:|---:|---:|
| 6610 | `6610 -> 12718` | `cc2e,4a6e` | `ce6e` |
| 6612 | `12719 -> 6614` | `0a6f,825f` | `8a7f` |
| 12717 | `12717 -> 6611` | `4e2e,ca2e` | `ce2e` |
| 12720 | `6613 -> 12720` | `8a4f,0a5f` | `8a5f` |

These are the **exact four invariant exposed seams** of the commutator core.
They are not all literal discontinuities.  The tail closures are

```text
(16,9):  6621 6626 12729 12733
(16,13): 6625 6626       12733
(18,9):  6621 6628 12729 12735
(18,15): 6627 6628       12735.
```

Thus generic members have eight raw seams; when `l=L-3`, one right-tail cut
coalesces and seven remain.  Discarding the tail seams would be unsound: the
two invalid nominal compositions fail precisely at their closure rows.

The common right core retains the endpoint-minimal upper witnesses

```text
ce2e : [12717,12719), sources (12717,6611),
8a5f : [12720,12722), sources (6613,12720),
ca5f : [12720,12723), sources (6613,12720,12721).
```

A third overlap must preserve these occurrence-labelled intervals or provide
independently replayed replacements.

## 3. The common Hall gain

All four carriers have the same eleven zero-provider targets:

```text
2665 28e9 291d 29a9 2f28 4879
48e9 4e70 6989 6a29 6c70.
```

Compared with exact229, only `8000` has acquired a provider.  Its unique cell
is

```text
J31761 = [12720,12721), source label 6613,
ordered envelope (8a0e), allowed 8a0e, mandatory 8000.
```

The mandatory `8000` is forced by rows 12718, 12719, and 12720, whose only
`8000` carrier is envelope position 12720.  Relative to the exact229 matching,
the exchange is

```text
8000 -- J31761 -- 0a4e -- J31763,
```

where the old matching used `0a4e--J31761`; the carrier matching uses
`8000--J31761` and `0a4e--J31763`.

Each carrier's canonical alternating shore decomposes into exactly 24
deficiency-one components: the eleven isolated zero targets above and
thirteen nonzero components.  Hence

\[
 Z=11,\qquad \operatorname{def}=24,\qquad
 \operatorname{def}-Z=13.                \tag{3.1}
\]

Twelve of the thirteen nonzero roots are common.  The length-16 carriers
have the additional component `05a4` of size `18/17`; the length-18 carriers
replace it by `85a4` of size `5/4`.  This accounts exactly for the two shore
sizes in the table.

## 4. Exact positive-cut theorem

Fix one carrier graph `G` and its stored maximum matching `M`.  Orient every
unmatched edge left-to-right and every matched edge right-to-left.  Let

* `F_L` be the left vertices reachable from a free left vertex; and
* `B_R` be the right vertices from which a free right vertex is reachable.

Suppose the old graph is retained and one absent edge `(q,c)` is added.  Then

\[
 \nu(G+(q,c))=\nu(G)+1
 \quad\Longleftrightarrow\quad
 q\in F_L\ \hbox{ and }\ c\in B_R.        \tag{4.1}
\]

Indeed, the two reachability paths and the new edge concatenate to an
augmenting path.  Their old-graph portions cannot intersect in a way that
reaches a free right vertex, since `M` was maximum.  Conversely, an
augmenting path in the one-edge extension must use the new edge; splitting it
there gives the two reachability conditions.  A single new edge can increase
matching by at most one, proving equality.

For a proper-prefix cell `c`, with ordered maximal envelopes `P_p`, allowed
union `E_c`, and mandatory mask `F_c`, the literal incidence condition is

\[
 F_c\subseteq q\subseteq E_c,qquad
 q\cap P_p\ne\varnothing\quad\hbox{for every }p\in c,
 \qquad |q|<8.                            \tag{4.2}
\]

Equations (4.1)--(4.2) are the exact provider signature.  Marginal allowed or
mandatory masks alone are insufficient, and if a physical move deletes an
old matching edge, (4.1) is no longer a final certificate: the complete graph
must be rematched.

## 5. The four local defect-one ports

In the two dependency windows with cell starts

```text
[6595,6650) union [12700,12765),
```

define the defect of zero target `q` at cell `c` by

\[
 d(q,c)=|q\setminus E_c|+|F_c\setminus q|
       +|\{p\in c:q\cap P_p=\varnothing\}|.             \tag{5.1}
\]

Complete enumeration of all eleven zero targets and all cells in these
windows gives exactly four rows with `d=1`, identically in every carrier:

| target/cell | interval | ordered envelopes | `(E,F)` | missing | `c in B_R` | matching after abstract edge |
|---|---|---|---|---|---|---:|
| `4879/J31748` | `[12713,12715)` | `4a61,4a70` | `4a71/0051` | `0008` | no | 26308 |
| `4e70/J19536` | `[6607,6609)` | `c660,ce20` | `ce60/4a40` | `0010` | yes | 26309 |
| `4e70/J19538` | `[6608,6610)` | `ce20,cc30` | `ce30/0a10` | `0040` | yes | 26309 |
| `4e70/J31749` | `[12714,12715)` | `4a70` | `4a70/0050` | `0400` | yes | 26309 |

The `4879` row is a genuine decoy: adding its edge removes one isolated zero
but joins it to a saturated component.  The zero count falls `11->10`, the
nonzero term rises `13->14`, and deficiency remains 24.

Each `4e70` row crosses the positive cut and has an explicit augmenting path:

```text
A: 4e70-J19536-ce40-J21197-c640-J27739(exposed),
B: 4e70-J19538-ce30-J21028-8a30-J29401(exposed),
C: 4e70-J31749-4a70-J3007-0a70-J14208(exposed).
```

The three paths are alternatives sharing start target `4e70`; each is
vertex-disjoint from the protected `8000` exchange.  Because the first cell
is currently matched, a physical profile must create the new edge **and**
retain that matched edge.  The exact paired conditions are:

| port | targets required at first cell | equivalent profile condition |
|---|---|---|
| A | `{4e70,ce40}` | `E'` contains `ce70`, `F'` is a submask of `4e40`, every `P'_p` meets both |
| B | `{4e70,ce30}` | `E'` contains `ce70`, `F'` is a submask of `4e30`, every `P'_p` meets both |
| C | `{4e70,4a70}` | `E'` contains `4e70`, `F'` is a submask of `4a70`, every `P'_p` meets both |

Consequently, a middle-exact and all-upper third overlap that retains the
stored carrier matching and realizes any one of A--C has matching at least
26,309 and deficiency at most 23.  This is the smallest local production
gate found in the two-shore windows.

## 6. What the common-`0200` halo proves—and does not prove

There is a stronger exact profile relaxation remote from the four seams.
Changing only target row 4653 from `69a9` to `6b29` gives

```text
J13964=[4654,4657): P=(6221,4a21,0a29), E/F=6a29/6809,
J13966=[4655,4657): P=(4a21,0a29),      E/F=4a29/4809.
```

On every one of the four carriers this relaxed chronology is middle-exact,
all-upper, and has a complete rematched value

```text
matching 26310, deficiency 22, zero count 10, nonzero term 12.
```

The two decisive paths are

```text
6a29 -- J13964,
5a29 -- J18077 -- 4a29 -- J13966.
```

This is not an integral escape.  The replacement adds one `6b29` occurrence
and deletes the unique `69a9` occurrence.  It also loses 16 old incidences,
including three stored matching edges, while gaining 54, so deficiency 22 is
a full-rematch fact rather than an addition-only shortcut.

The independent fixed-neighbour row census in the nested-port theorem
sharpens this representative calculation: the two halo profiles and exact
middle replay occur exactly for

```text
T[4653] in {6aa9,6b29}.
```

Their unique old occurrences are `6aa9@2934` and `6b29@3846`; both direct
donor exchanges fail at their source collars.

The natural occurrence-preserving shifted-eight return on positions

```text
3846 2328 3933 3522 2063 817 238 4653
```

does install the `6b29` halo profiles and remains all-upper, but row 3845
loses its `0200` carrier.  It is therefore middle-inexact and Hall-ineligible.
A genuine third overlap along this route must place `6aa9` or `6b29` at 4653,
return `69a9`, and repair the corresponding donor collar; the `6b29` route
specifically needs a seam-compatible `0200` token at the 3846 source collar.

## 7. Bounded physical no-go and open scope

An independent exact census applies one more equal-block exchange to each of
the four carriers, with

```text
a in [6598,6618], b in [12704,12728], length in {1,2,3},
and independent reversal flags on the two incoming blocks.
```

This is `21*25*3*4=6300` formal moves per carrier, 25,200 total.  The exact
formal/unique-nonroot counts are respectively

```text
pass33: 16/10, pass46: 20/14, pass35: 16/10, pass55: 20/14.
```

None is simultaneously middle-exact, all-upper, and retains a provider for
`4e70` or `8000`.  This proves only a length-at-most-three, fixed-window
third-swap no-go.  Longer overlaps, extra receiver rows, unequal block
rethreads, and nonlocal occurrence cycles remain open.

The final unrestricted acceptance test is still literal: a candidate must
preserve the occurrence multiset, pass every middle row, cover every upper
mask, and have a full 26,332-target matching of at least 26,309.  This note
does not supply such a word and makes no unrestricted K16 no-go claim.

## 8. Frozen authority

Primary independent replay:

```text
scratch/audit_k16_exact229_nested_forward_commutator_20260730.py
SHA-256 559f7cb41410cd4e277a1857bc29e3b97571257433eb1abc0072230dd3a6d6eb

scratch/k16_exact229_nested_forward_commutator_20260730.audit.json
SHA-256 51e0415ad2307d30aa00b4a5a3fc08fd7e20c23e3b08c080da92abb34c1a8687
payload 9b9a4eb34a8abe1fb20ac7ad308a089c0b8f9aa5e63ee4abb39a26e6e56d1200
```

Independent local-port/census audit:

```text
scratch/k16_exact229_nested_four_third_overlap_gate_20260730.audit.json
SHA-256 59fdeccb1b6225d10f7b41dc88efebf074e04921f11dd3b8d2cce30b77c3fc2d

scratch/search_defect_transport_two_shore_swap_bfs_20260730.cpp
SHA-256 26143c927380c3e2eaeb9aad7bc8581ce81b20dd56a9c161aab57a2734b358b7
```

Independent sharp-row/nested-tail authority:

```text
MATH_THEOREM_K16_EXACT229_NESTED_SWAP_THREE_PATH_PORT_20260730.md
SHA-256 1a2d56774f1f0c2f4ddf6604b029104f8842ebcb1b6f9e481d2870976c68d325

scratch/audit_k16_exact229_nested_swap_three_path_port_20260730.py
SHA-256 8ef85074369d12dcaa208a8485275195ebdec4d7a7b9d410596f4bdeda2edf68

scratch/k16_exact229_nested_swap_three_path_port_20260730.audit.json
SHA-256 e96ed3a781b63ba86025ad7e468477827942c92c04e3604a336bab6cb3762948
payload 69ef2f01fdd64e5546a6f70357c526593b627ec27c272e9fb4ed8b480cb71667
```

The primary replay reconstructs all six words from occurrence labels,
authenticates the four materialized words and Hall JSON payloads, rebuilds all
four generalized incidence graphs, checks both alternating shores, replays
the complete rank-above-eight upper spectrum, derives the exact local
defect-one catalogue,
verifies the displayed augmenting paths, fully rematches the relaxed halo,
and rejects the shifted-eight integral return before Hall.
