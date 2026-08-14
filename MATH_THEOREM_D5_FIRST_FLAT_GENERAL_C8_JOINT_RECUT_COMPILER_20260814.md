# A general adjacent C8 joint recut repairs the first flat D5 router collar

**Date:** 2026-08-14

**Status:** exact positive cut-open compiler on the first frozen rank-11,
ground-23 flat factor, with exhaustive H100 construction and a standalone
hostile replay.  The literal relation has 126 q2-simple boundary extensions.
Its five-state exchange-support quotient propagates on all 25 tree blocks
and has no obstruction on any of the eight `K2,2` cores.  Literal
all-factor boundary identification and global resource packing are not
claimed.

## 0. Outcome

The canonical C6 strand collar solved q1 but forced the fixed support word

```text
{0,2}, {3,5}, {1,2},
```

so coordinate `2` returned after only two owner steps.  Adding an extra cut
inside the same common-core C8 family does not change that join.  The repair
is instead the other C8 topology: keep the prescribed context and router
cuts adjacent in the old matching, join one endpoint pair directly, and
route the other endpoint pair through two freely chosen auxiliary cuts.

For the first actual flat factor, exhaustive search over all such Johnson
C8s gives

```text
63   endpoint orientations with a legal direct Johnson edge,
21   endpoint orientations whose direct edge is not Johnson,
3087 exact lower/upper-q1 path-current joins,
357  owner-simple, C8-q1-simple joins,
336  complete 25-edge q1-exact/simple joins in both router phases,
147  joins with every determined fixed-side run resident and q2 current zero,
126  joins also having simple lower-q2 and upper-q2 internal decks.
```

The 21 rejected at the last line are exactly the seven extensions of source
witnesses `2,9,16`: their lower-q2 internal deck has size 29 rather than 30.
This audit repair is material.  Every theorem below uses the final count
`126`, not the raw count `147`.

## 1. The first positive joint-recut class

Orient the prescribed context cut as `A0--B0` and the prescribed router cut
as `A1--B1`.  Choose four fresh auxiliary owners `A2,B2,A3,B3`.  The old and
new matchings are

```text
old: A0--B0, A1--B1, A2--B2, A3--B3,
new: B0--A1, B1--A2, B2--A3, B3--A0.          (1.1)
```

Thus one new edge is the direct context--router join and the other side is
the five-edge alternating path

```text
B1--A2--B2--A3--B3--A0.                       (1.2)
```

The two auxiliary old edges can be dummy cuts at a degree-one token, one
dummy and one future router cut at degree two, or two further router cuts at
degree three.  In every case (1.1) is an ordinary cut-open four-versus-four
matching switch.  It identifies no owners and introduces no degree-four
vertex.

For each orientation, the search enumerates every length-two Johnson half
path from `B1` and `A0`.  If `I_L,I_R` are their signed lower/upper-q1
currents and `e` is the middle edge, exact refill is the hash-join equation

```text
I_L + q1(e) + I_R
  = q1(A0--B0) + q1(A1--B1) - q1(B0--A1).     (1.3)
```

Hence the `3087` count is exhaustive for the declared C8 class; it is not a
sampled auxiliary menu.

## 2. One literal compiler

One final witness uses the following four removed edges:

```text
00100100110110111110000 -- 10000100110110111110000
00100110110110110110000 -- 10100100110110110110000
00100110110110111100000 -- 10100110110110110100000
00000110110110111110000 -- 10000110110110111100000
```

and the following four added edges:

```text
00100100110110111110000 -- 10100100110110110110000
00100110110110110110000 -- 10100110110110110100000
00100110110110111100000 -- 10000110110110111100000
00000110110110111110000 -- 10000100110110111110000.
```

All eight owners are distinct and every displayed pair is a Johnson edge.
The first two removed edges are the actual first-token context edge and the
selected phase-common `P2--Q0` router edge.  The last two are the cut-open
boundary edges.

The complete q1 flag table is

```text
old lower                    old upper
00000100110110111110000      10100100110110111110000
00100100110110110110000      10100110110110110110000
00100110110110110100000      10100110110110111100000
00000110110110111100000      10000110110110111110000

new lower                    new upper
00100100110110110110000      10100100110110111110000
00100110110110110100000      10100110110110110110000
00000110110110111100000      10100110110110111100000
00000100110110111110000      10000110110110111110000.
```

Both columns are permutations.  More strongly, after adjoining the common
18-owner router and the other two strand collars, the verifier checks 25
distinct lower-q1 values and 25 distinct upper-q1 values before and after,
in both router phases, with exact occurrence-Counter equality.

The C8 is installed identically in the two router phases.  Since its router
cut is phase-common, it changes only the cut-open conjugation of the router;
the router's old identity and new prescribed three-cycle port actions are
unchanged.

## 3. The crossing q2 and residence ledger

At the formerly bad router-side boundary, the witness now has supports

```text
{0,18}, {3,5}, {1,2}.                           (3.1)
```

Their union has size six.  The repeated label `2` in the old
`{0,2},{3,5},{1,2}` word has been replaced by the fresh transition label
`18`, so every owner run determined on this side has length at least three.
The context-side determined word is

```text
{0,6}, {1,12}, {10,11},                         (3.2)
```

also with union size six.  Neither consecutive pair of q2 windows in
(3.1) or (3.2) repeats a lower or an upper resource.  The same two words
occur in both router phases.

For each of the 126 final witnesses, the hostile replay checks

```text
30 internal q2 centres in each phase,
30 distinct lower-q2 values in each phase,
30 distinct upper-q2 values in each phase,
empty old-to-new lower-q2 Counter delta,
empty old-to-new upper-q2 Counter delta,
12 determined boundary-inward three-support windows, all with union size 6.
```

The two endpoints joined across the auxiliary--auxiliary middle edge remain
genuine boundary darts.  Their exterior q2 windows are deliberately not
invented here; they are inputs to the finite extension relation.  Thus this
is a literal cut-open compiler, not a falsely closed box.

## 4. The finite boundary relation

Every final C8 has four old exchange supports

```text
{p,c}, {p,r}, {p,u}, {p,v},                     (4.1)
```

for a common pivot `p`.  They correspond respectively to the context cut,
current router cut, incoming auxiliary cut, and added auxiliary cut.  In the
representative

```text
(p,c,r,u,v) = (0,2,6,16,18).
```

The full boundary state is the literal tuple consisting of the two
auxiliary owner edges, their orientations, the two phase-independent inward
support words, and their q1 flags.  All 126 such states are printed in the
seven exhaustive partition certificates and replayed owner by owner.

There is also a useful exchange-support quotient.  For each of the three
possible placements of logical token zero among the router ports, it has

```text
input states   {5,8,9,11,16,17},
output states  {8,9,11,12,14,16,17,18},
42 literal support pairs.
```

On the common reusable domain

```text
D = {8,9,11,16,17}                              (4.2)
```

the relation is exactly

```text
R_D = {(u,v) in D^2 : u != v}.                  (4.3)
```

The same `K5` relation occurs at all three router-port placements.  This is
the finite interface to feed into a full typed-factor propagation solver.
The support quotient alone does not identify literal owner edges belonging
to two different factor types; those identifications remain a separate
global compilation gate.

## 5. Tree propagation and the eight support holonomies

The flat router--token incidence graph has 25 tree components and eight
unicyclic components with two-core `K2,2`.  Relation (4.3) gives four
successors from every state, so it never blocks greedy propagation on a
tree.

Coordinate transport between two typed local charts may permute the five
states.  A transported `R_D` edge therefore forbids at most one successor
of any current state.  On a four-cycle, choose states successively.  There
are at least

```text
5 * 4 * 4 * 3 = 240                             (5.1)
```

closures under arbitrary transport bijections.  With aligned charts the
exact number is

```text
trace((J-I)^4) = 4^4 + 4 = 260.                 (5.2)
```

The replay reconstructs the flat graph and applies (5.1) to all eight
actual cores, whose router pairs are

```text
(141,142), (153,154), (165,166), (175,176),
(187,188), (198,199), (211,212), (224,225).
```

Thus there is no holonomy obstruction at the exchange-support quotient.
This is not yet a literal all-factor holonomy theorem: a global solver must
still instantiate the full auxiliary owner-edge states, prove their typed
extension relations on every encountered factor, and enforce cross-package
owner/q1/q2 disjointness.

## 6. Minimality and the next global gate

Within the declared search ladder—canonical three-cut C6 followed by all
placements of a general four-cut C8 that keep the selected canonical router
cut—the repair is minimal in owner count.

1. The three-cut C6 collar has the exact fixed run-two obstruction already
   frozen.
2. A canonical common-core C8 extension has 189 owner/q1-simple candidates,
   but every one retains a bad union-five fixed window.
3. In a general C8 with the context and router cuts opposite, exhaustive
   length-three path joining finds 47,040 raw side paths on each shore and
   zero exact q1 joins.
4. The remaining placement is the adjacent general C8 of (1.1), and it has
   the 126 positive witnesses above.

Up to cyclic reversal, adjacent and opposite are the only placements of two
prescribed edges in a four-edge matching cycle.  Therefore eight owners and
four old cuts are the smallest repairing class in this exhausted ladder.
No claim is made here about a noncanonical three-cut C6 outside the frozen
strand-seam family or about changing the router cut itself.

The next gate is not another local C8 search.  It is the literal typed
extension solver over the 33-component pseudoforest, using the complete
owner-edge boundary records rather than only (4.3), followed by global
owner/q1/q2 packing.  The quotient audit proves that the eight cycles do not
fail merely from support-state holonomy.

## 7. H100 provenance

```text
canonical-C8 subclass search
9d578041b8fa53b2480f72bbf368f741fa7ca8dee53c6f119e211a82b0545b69
  scratch/search_d5_first_flat_token0_c8_transition_collar_20260814.py
ae3927fdb0534382c34f777301be092b1fb0d6b46a7e308ce624cca02da8308f
  scratch/search_d5_first_flat_token0_c8_transition_collar_20260814.h100.out

opposite-placement general-C8 search
65b7e8e28c9e2d9047bf6b97422c7bb087994e64a935a0d309f1783ecc48be95
  scratch/search_d5_first_flat_token0_general_c8_joint_recut_20260814.py
b6bf906f447eab27148934d93bc0c2ed8b973875a9fb1647ddbb4161814b658f
  scratch/search_d5_first_flat_token0_general_c8_joint_recut_20260814.h100.out

adjacent-placement exhaustive search
cb5a640be1930640e94c6bc61a003600f1cf194ae1781d3a2097130b410afaeb
  scratch/search_d5_first_flat_token0_general_c8_adjacent_recut_20260814.py

standalone q2-simple relation/holonomy replay
03c394de71e3324daad27db39f71d99f16cc4db0c17c2d9787a7139787ca90a5
  scratch/audit_d5_first_flat_c8_transition_relation_and_holonomy_20260814.py
f8348a39bad49c6bc2270d2e49c1f7b77b86b76c35e3331dfd9cd00cdc68086a
  scratch/audit_d5_first_flat_c8_transition_relation_and_holonomy_20260814.h100.out
```

The seven adjacent-search partition output hashes are recorded verbatim in
the standalone replay output.  All enumeration, Python compilation,
reconstruction, replay, q2 filtering, holonomy arithmetic, and hashing ran
through SSH on H100.  The local Mac was used only for reading, editing,
transfer, and Git.
