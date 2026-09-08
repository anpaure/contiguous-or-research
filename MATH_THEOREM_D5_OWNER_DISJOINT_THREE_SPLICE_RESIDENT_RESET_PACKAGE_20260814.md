# An owner-disjoint three-splice C6 package realizes both D5 reset terminals

**Date:** 2026-08-14  
**Status:** exact finite local theorem with independent H100 replay.  The
theorem is an individual-package statement for each of the adjacent and hard
D5 terminal types.  Simultaneous resource-disjoint planting of all 212
prescribed reset occurrences is not claimed here.

## 0. Theorem

At rank seven on the ground set `[13]`, there are two ambient resident C6
cycles `E_B,E_C`, one new resident cable C6 `D`, and the three new C6 router
cycles `R_0,R_1,R_2` with the following properties.

1. All 36 owner occurrences are distinct.  The cable/router addition costs
   24 owners; the 12 owners of `E_B,E_C` are ambient hypotheses.
2. Three ordinary owner-disjoint degree-two edge splices join `E_B` directly
   to `R_0` and join `E_C` to `R_1` through `D`.  No owner is identified.
3. In the old router phase the spliced graph has components of lengths
   `6,12,18`; in the new router phase it is one 36-cycle.
4. On marked ports `(B,U,C)` the old first-return action is the identity and
   the new action is `(B U C)`.  Suppressing the internal auxiliary port `U`
   gives `(B C)` on the two external heads.
5. The owner, lower-q1, upper-q1, lower-q2 and upper-q2 occurrence multisets
   agree exactly between the old and new phases.  Each of the five banks has
   36 distinct values.  In particular both q2 occurrence currents vanish.
6. The exact nonconstant-coordinate run minima on the owner and immediate-
   upper traces are `(3,3)` and `(4,2)` in both phases.
7. A distinct ambient owner `T`, not used by the 36-cycle bank and left
   unchanged, may be chosen so that `(T,B,C)` has either the adjacent D5
   signature `(1,1,1,6,9)` or the hard signature `(1,1,2,5,9)`.

Adding four common-one coordinates to every set and six unused-zero
coordinates lifts these two signatures to the actual rank-11, ground-23 D5
signatures

```text
adjacent: (1,1,1,10,13),    hard: (1,1,2,9,13).
```

This lift preserves every Johnson edge, component action, typed-resource
equality, distinctness assertion and nonconstant-coordinate run minimum.

## 1. Literal owner bank

Write a set as an increasing digit string.  The cable and router are common
to the two terminal variants:

```text
D:
0123568  0123578  01357812  035781112  035681112  02356811

R0:
1279101112  1289101112  1589101112
135891112   135791112   123791112

R1:
2789101112  2689101112  5689101112
356891112   357891112   237891112

R2:
2679101112  1269101112  1569101112
135691112   356791112   236791112
```

For avoidance of ambiguity, the same data with braces and separators are in
the literal H100 table listed in Section 6; for example `035781112` means
`{0,3,5,7,8,11,12}`, not decimal digits.

The second exterior cycle is also common:

```text
EC:
0123456  0123457  01234711  01347911  01346911  0134569
```

For the adjacent terminal use

```text
EB-adj:
13458911  13457911  13457910  01345710  01345810  01345811

T = 12347911,    B = 13457911 = EB-adj[1],
C = 01347911 = EC[3].
```

For the hard terminal use

```text
EB-hard:
134581112  134571112  1457101112
1247101112 1248101112 123481112

T = 01345711,    B = 134571112 = EB-hard[1],
C = 0123457 = EC[1].
```

In both cases the hidden auxiliary port is

```text
U = R2[0] = 2679101112.
```

The displayed `T` is not one of the 36 physical bank owners.  It is a fixed
ambient spectator occurrence, not another vertex inserted into the spliced
cycle.

## 2. The three physical splices

The router phase switch replaces the three seam edges

```text
R_i[0]--R_i[1]  by  R_i[0]--R_(i-1)[1]   (indices modulo 3).
```

This is the marked-C6 switch.  The following three ordinary splices are
made identically in both router phases.

### 2.1 EC to cable

Delete

```text
0123456--0123457,       0123568--0123578
```

and add

```text
0123456--0123568,       0123457--0123578.
```

### 2.2 Cable to R1

Delete

```text
035681112--035781112,   356891112--357891112
```

and add

```text
035781112--357891112,   035681112--356891112.
```

### 2.3 EB to R0

Delete the phase-common router edge

```text
135791112--135891112.
```

In the adjacent variant also delete `13457911--13458911` and add

```text
135891112--13458911,    135791112--13457911.
```

In the hard variant instead delete `134571112--134581112` and add

```text
135891112--134581112,   135791112--134571112.
```

Every displayed new pair has symmetric difference two, so every added edge
is a Johnson edge.  Each splice deletes one edge on each of two
owner-disjoint degree-two components and inserts one of the two cross
pairings.  Consequently the operation creates no repeated occurrence and no
degree-four owner.

The boundary-role map is therefore exact:

```text
external B  -- EB -- direct splice ---------- R0 port B
external C  -- EC -- splice -- D -- splice -- R1 port C
hidden U    --------------------------------- R2 port U
tail T      -- distinct unchanged ambient spectator
```

## 3. Component action

Before the seam switch, `R_2` remains the length-six component through `U`,
the `EB--R_0` splice gives the length-12 component through `B`, and the
`EC--D--R_1` serial pair gives the length-18 component through `C`.  Hence
the first-return map on `{B,U,C}` is the identity.

The seam switch joins the three router ports cyclically.  The same external
splices then produce a single length-36 component, and literal traversal
gives

```text
B -> U,    U -> C,    C -> B.
```

Thus the full action is `(B U C)`.  If `U` is not marked, the first marked
return from `B` skips `U` and reaches `C`, while `C` returns to `B`; the
quotient action is `(B C)`.

### 3.1 Conditional substitution interface

The package has the following black-box interpretation.  Retain only the
boundary marks `B,C` and the fixed spectator `T`, and suppress every other
occurrence of `EB,EC,D,R0,R1,R2`, including `U`.  The induced old boundary
matching fixes both successor heads; the induced new boundary matching
transposes them.  The separate tail occurrence is fixed in both states.
Thus, **provided the context supplies audited cut-open exterior collars**, an
owner-exact degree-two row discrepancy

```text
old: T fixed, B fixed, C fixed
new: T fixed, B and C transposed
```

may be replaced by the package without changing its suppressed boundary
history.  All owner occurrences inside the replacement are the same in the
two states, and its complete internal q2 occurrence current is zero.

The exact degree-balanced cut-open interface is an overlap-one graft.  At
`B`, let the context segment be `X--B--Y`.  Identify its occurrence `B` with
the marked occurrence on `EB`, write a chosen cut edge of that cyclic collar
as `L--R`, require `L,R != B`, and otherwise keep the context and package
owner-disjoint.  (The cut edge must not be incident with the marked owner;
otherwise the deletion count leaves `B` with degree one.)  Delete

```text
X--B,  B--Y,  L--R
```

and add either `X--L,Y--R` or the crossed pairing, requiring both new pairs
to be Johnson edges.  If the context has `N` vertices, the union before the
graft has `N+6-1` distinct vertices; after three deletions and two additions
it has `N+5` edges as well, and every vertex has degree two.  Perform the
same overlap-one graft at `C`, again cutting a collar edge not incident with
`C`.  At both marks, `L--R` must be a retained phase-common collar edge,
not one of the edges already deleted by the three internal splices; this is
an additional condition in the adjacent `C` variant, where the internal
`EC--D` cut is nonincident with the mark.  The old package path pairs the
two retained boundary darts in the identity pattern, whereas the new router monodromy
crosses the `B,C` paths after the hidden port is suppressed.

This paragraph is an **interface reduction, not an existence claim for the
frozen D5 neighbors**.  The closed witness below proves the internal atom;
the actual choices of `L--R`, the two cross pairings at each head, all mixed
q1/q2 windows and the complete palette refill still require a separate
search/audit against the literal context neighbors `X,Y`.

The exterior-collar proviso is essential.  Merely placing 212 disjoint
*closed* copies does not reconnect the shared frozen-D5 wires, and deleting
the original `B,C` factor incidences can leave q1 palette holes.

Several copies compose by disjoint union only under all of the following
interface conditions.

1. Distinct package interiors are owner-disjoint.  Each package may meet the
   context only in its prescribed `B,C` occurrences through the overlap-one
   graft above; no cable/router/exterior-interior occurrence is reused.
2. Every new cross edge is Johnson and every owner remains degree two.
3. Their owner/lower-q1/upper-q1/lower-q2/upper-q2 footprints are mutually
   simple and avoid the protected context bank except at declared boundary
   resources.
4. Every q2 window crossing a context/package cut is audited in both states,
   and every owner or upper run crossing the cut meets the collar residence
   bound.
5. After suppressing all package interiors, the **whole** boundary matching
   is the prescribed context matching; if the target is the frozen D5
   factor, the rebuilt graph must also have its complete q1 palettes and
   required global component topology.

Under these hypotheses the local zero q2 currents add to zero and the
boundary transpositions substitute independently.  Conditions 3--5 are the
remaining global compilation gate; they do not follow from the present
closed local witness.

## 4. Complete typed-resource audit

For a cyclic owner trace `V=(V_j)`, define

```text
owner:    V_j
lower-q1: V_j intersection V_(j+1)
upper-q1: V_j union        V_(j+1)
lower-q2: V_j intersection V_(j+1) intersection V_(j+2)
upper-q2: V_j union        V_(j+1) union        V_(j+2).
```

The independent replay reconstructs the graphs from the literal removed and
added edge sets, checks degree two and Johnson adjacency, and computes all
five occurrence decks from scratch.  In each terminal variant it proves

```text
                         old distinct   new distinct   old multiset = new
owner                         36             36               yes
lower-q1                      36             36               yes
upper-q1                      36             36               yes
lower-q2                      36             36               yes
upper-q2                      36             36               yes
```

The complete 180 old and 180 new literal occurrences for each variant are
recorded in the two palette dumps in Section 6.  This is stronger than a
support comparison: both signed q2 occurrence currents are identically
zero.

The same replay scans all nonconstant coordinates cyclically.  On owners,
the least one-run and zero-run lengths are `(3,3)`; on immediate-upper
unions they are `(4,2)`.  These are exact in both states, including across
all six newly added cross edges.  Constant coordinates introduced by the
common-core lift do not create a finite run and therefore do not change the
minima.

## 5. Terminal types and scope

For the adjacent witness,

```text
|T-B|=1, |T-C|=1, |B-C|=1, |T intersection B intersection C|=6,
|T union B union C|=9.
```

For the hard witness the corresponding values are `(1,1,2,5,9)`.  Adding
four common-one coordinates changes only the fourth and fifth entries by
four, while adding six unused-zero coordinates changes neither.  This gives
the exact frozen D5 Venn signatures at rank 11 on 23 coordinates.

The theorem proves one literal package for each of the two terminal types.
It does not assert that 212 relabelled copies can simultaneously avoid the
protected frozen-D5 owner/q1/q2 bank.  A finite conflict-hypergraph selector
is only the first resource row of that problem; cut-open boundary
compilation, q1 refill and global traversal remain separate gates.

## 6. H100 provenance

All search and verification computation was run on the H100.  SHA-256:

```text
89fdd5fcecd85683529116111e2ccf38b46035bf966f0caafe45a4d7ace8917d
  scratch/search_d5_complete_owner_disjoint_three_splice_reset_20260814.py
207e9e6e82268c3ed937e0fe93584cbabbfbaba314da361d1b12906c2ed4d1ac
  scratch/search_d5_complete_owner_disjoint_three_splice_reset_adjacent_20260814.h100.out
dda4a8f5fd4b05ae31e19b00ebbbe61fb11f92738e30fdc394cb5ae8ae06ebb4
  scratch/search_d5_complete_owner_disjoint_three_splice_reset_hard_20260814.h100.out

5c1e93fe44c13717af8dd19e885d088c07dfe45ea747bf248c6c6b180f5c773c
  scratch/verify_d5_complete_owner_disjoint_three_splice_reset_20260814.py
563ffbe87729ff14e9cb73de0b87de6a171c5eecd94b4eb3100e70e296a0ddd3
  scratch/verify_d5_complete_owner_disjoint_three_splice_reset_adjacent_20260814.h100.out
f2b2e82503ae8ef8c4c14ed8604ac72702230e312491bc2d64ada9fff995a072
  scratch/verify_d5_complete_owner_disjoint_three_splice_reset_hard_20260814.h100.out

231f0d32cc38a5ba47df311bdc650a958f7626ad4574466cb3578436245a718d
  scratch/d5_complete_splice_literal_tables_20260814.h100.out

9221575d6ea72cc428f41af0f3ca910f41ee8b10f855ed4372c4d9bd6c7d04ee
  scratch/dump_d5_complete_splice_palettes_20260814.py
500286642c7d2a6db36c8d991e569604e23c0c8cec1ff8eb4f98a07c70de1bce
  scratch/dump_d5_complete_splice_palettes_adjacent_20260814.h100.out
0bb3d2dbca28d63e503bed34f8e3f9a2c9f3f3b9a2c2214251c69f319ca8d802
  scratch/dump_d5_complete_splice_palettes_hard_20260814.h100.out
```

The search witnesses are discovery certificates.  The verifier and palette
dumper do not repeat the random search; they replay the frozen literal
cycles independently.
