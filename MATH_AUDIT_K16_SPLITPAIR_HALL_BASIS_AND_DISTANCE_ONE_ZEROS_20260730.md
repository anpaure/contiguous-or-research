# K16 split-pair Hall basis: the current eight-carrier span has deficiency eleven

Date: 2026-07-30  
Status: **exact diagnostic theorem; union incidence is a relaxation, not a physical carrier**

## Exact individual and union counts

AD's split-pair census contains eight distinct middle-exact,
arbitrary-upper-complete chronologies, represented by IDs

```text
151,155,162,178,229,231,233,282.
```

Their exact generalized lower-Hall deficiencies are

```text
151:26, 155:26, 162:26, 178:28,
229:25, 231:27, 233:26, 282:27.
```

Carrier 229 is individually best.  It has matching `26307/26332`, canonical
shore `212 -> 187`, and twelve zero-degree targets:

```text
2665 28e9 291d 29a9 2f28 4879
48e9 4e70 6989 6a29 6c70 8000.
```

Take the union of the eight incidence graphs, allowing a lower target to use
a cell supplied by any carrier.  This is a relaxation: it need not correspond
to one chronology.  Even this union has exact deficiency eleven.  Its eight
persistent zero-degree targets are

```text
2665 28e9 29a9 48e9 4e70 6989 6c70 8000.
```

The canonical union shore is `20 -> 9`.  It decomposes into eleven
independent deficiency-one components.  Eight are the isolated zeroes above;
the other three are

```text
{21a9,21ab,a1a9}                 -> 2 cells,
{4a29,4a2b,5a29,6a29,ca29}      -> 4 cells,
{6c30,6cb0,6d30,ec30}           -> 3 cells.
```

Therefore a physical carrier outside the current basis must create at least
eleven effective new right cells relative to this union, although one
chronology edit may create several cells.  On carrier 229's shore, the best
two-carrier unions `155+178` and `155+233` already attain the same deficiency
eleven.  Consequently recombining only the incidence cells already present
in the eight saved carriers cannot close Hall; a new chronology must create
genuinely new cells.

## Distance-one near-cell structure

For each persistent zero target, rank every proper-prefix cell by

```text
missing allowed bits + excess mandatory bits + disjoint envelope positions.
```

Each of the seven rank-seven zeroes has score one: there are cells whose
mandatory set is already contained in the target and whose envelope positions
all meet the target, but whose allowed union misses exactly one target bit.

The singleton `8000` is also score one, in the dual direction.  The sharp
cell is

```text
start 6324, length 1,
allowed 8071,
mandatory 8010,
context c671,c879,a879,a86d,a46d,946d.
```

The exact carrier explanation is:

- row 6322 `c671` forces bit `8000` solely at cell 6324;
- row 6324 `a879` forces bit `0010` solely at cell 6324;
- the `0010` carrier positions for row 6324 are exactly `(6324,)` because
  the next row `a86d` drops that bit.

Thus extending the `0010` envelope run across cell 6325 removes the unwanted
mandatory bit from the singleton cell while retaining its forced `8000` bit.
This is the sharp constructive collar target.  The other seven targets each
need one missing allowed bit introduced at one of their listed near cells.

The same calculation on all twenty vertices of the union shore, excluding
the nine already-used union cells, gives score one for every target.  Several
positions offer score-one cells for more than one deficient component:

```text
start 6459: 8000(excess 0001) and {4a29,ca29}(missing 0008),
start 6561: 8000(excess 4000) and {4a29,4a2b,ca29}(missing 0020),
start 6609: 8000(excess 0010) and {6c30,ec30}(missing 2000),
start 8122: {21a9,a1a9,29a9,6989} at score one.
```

These are preferable joint-collar search loci: one chronology edit may create
several of the eleven new right cells required by the union theorem.

## Consequence

The Hall gap is not diffuse.  Within the current split-pair basis it is
supported on an eleven-unit union obstruction, including eight literal
zero-degree targets.  All eight are exactly one local incidence condition
from service.  Any successful next move must nevertheless be new: no hybrid
of the existing eight incidence graphs can supply them.

## Artifacts

```text
scratch/analyze_k16_splitpair_hall_basis_20260730.py
SHA256 d6499649e41730f833e8d335fc85c8001c05875d383c76c9befa6d9cf5b21eb9

scratch/analyze_k16_hall_zero_near_cells_20260730.py
SHA256 e509c4927fb509a3c248497140dd64040715043c202c08946bc707123e3a830e

scratch/k16_splitpair_hall_basis_20260730/splitpair_hall_basis_v2.audit.json
SHA256 95034ac7fe29abf07a2549c278ddc92c218e326a77e8f39b022dd807c92b603b
payload 5e552d8b72750559bf9a15dc5bf34beeb1d6aac57bec09b968bec206313dbcca

scratch/k16_splitpair_hall_basis_20260730/exact229.hall.audit.json
SHA256 85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0
payload c5c99fead7b99c2b2bf35540440f10434ae4c1c42345f72f331348bd2de25eb3

scratch/k16_splitpair_hall_basis_20260730/exact229.zero_near_cells.json
SHA256 41c51eecf0373cccf9dace084c765c6ad03a3bf7b4f5726a6758275f03dae427

scratch/analyze_k16_union_shore_new_cell_targets_20260730.py
SHA256 fa259176b898d61bf13e082032ea9215d1f8ab6e0fb2e9e821389af350e215fb

scratch/k16_splitpair_hall_basis_20260730/exact229.union_shore_new_cells.json
SHA256 d545bf8166f6d963b80466eea56955436078a7790ceb0795c82db69f7e92113f
```
