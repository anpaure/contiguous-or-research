# The complete q4 k17 fixed-lower quotient-self catalogue has matching number eight

**Date:** 2026-08-14  
**Status:** exact finite theorem for owner-simple, immediate-lower-simple
period-ten q4 columns.  Owner reflection is imposed only in the translation
quotient, its induced involution may be nondihedral, and its translating lift
may depend on the row.

## 0. Result

Put the ground on `Z_17`.  A period-ten q4 column is specified by a
five-core `C` and ten distinct cyclic support labels `s_0,...,s_9`, with

```text
owner O_i = C union {s_i,s_(i+1),s_(i+2),s_(i+3)},
lower L_i = C union {s_(i+1),s_(i+2),s_(i+3)}.       (0.1)
```

All subscripts are modulo ten and all rows below are translation
necklaces.  Require both the ten owners and the ten immediate-lower rows
to be distinct.  Call the column **owner-self** when its owner deck is
closed under reflection `[X] -> [-X]`; no action on starts and no common
physical reflection centre is assumed.

The complete catalogue of owner-self columns containing at least one
fixed lower bracelet has the following form.

1. Up to multiplication by `Z_17^*`, there are exactly four distinct
   owner/lower typed columns.  This count is by the pair of unordered
   owner and lower decks, not by physical `(C,sigma)` realizations.
2. Every one has exactly two fixed owner bracelets, exactly two fixed
   lower bracelets, a nondihedral owner involution, and a nonconstant
   rowwise translating lift.  None has a reflection-closed lower deck.
3. Multiplier development gives exactly sixteen owner/lower typed
   columns but only eight owner decks.  Each owner deck has two lower-deck
   realizations; they are reflections of one another and therefore cannot
   both be selected without repeating all ten owners.
4. The fixed-owner edges of the eight owner decks form eight disjoint
   `K_2` components and 54 isolated vertices on the 70 fixed owner
   bracelets.  Their fixed-lower edges do the same on the 70 fixed lower
   bracelets.  Both maximum matching numbers are exactly eight.

Thus the quotient-twisted nondihedral escape exists locally, but it is far
too small to close the joint reflection master.  In any reflection owner
master in which nonself columns occur in literal reflected pairs, a fixed
lower bracelet receives even load from every nonself pair.  Consequently,
any odd aggregate contribution from a reflection orbit of selected columns
must come from an owner-self orbit (columns with a repeated lower row
are already inadmissible for an exact lower ledger).  Only sixteen of the 70
fixed lower bracelets occur in that complete catalogue.  Hence:

> **Theorem 0.1 (quotient-twisted joint reflection no-go).**  No literal-
> reflection q4 period-ten owner master, even after adjoining all
> owner-dependent-translation quotient-self columns, can simultaneously
> cover every immediate-lower bracelet exactly once.

This closes the nondihedral fixed-lower escape left open by the dihedral
edge-axis no-go.

## 1. Complete normalization

Suppose a fixed rank-eight lower necklace `[L]` occurs.  There is an affine
reflection `x -> t-x` preserving a representative of `[L]`.  Translation
conjugates its centre to zero.  An eight-set invariant under `x -> -x`
cannot contain zero, so it is exactly four of the eight pairs
`{+a,-a}`.  There are therefore

```text
                         binom(8,4)=70             (1.1)
```

literal normalized lower masks.  Rotating the ten starts puts the chosen
fixed lower at `L_0`.  Its five-core is any five-subset of `L_0`, giving
`binom(8,5)=56` core choices; the remaining three elements of `L_0` are
exactly `s_1,s_2,s_3`.  The endpoints `s_0,s_4` lie outside `L_0`.
Consequently this normalization loses no column containing a fixed lower
bracelet.

There is a second exact symmetry reduction.  Every multiplier
`x -> ax`, `a in Z_17^*`, commutes with negation and preserves translation
necklaces, cyclic-window incidence, simplicity, fixed-row status, and the
induced reflection permutations.  Modulo `{+1,-1}`, the multiplier group
is cyclic of order eight and acts regularly on the eight reflection pairs.
Burnside's count on their four-subsets is

```text
                         (70+2+2+6)/8=10.           (1.2)
```

The ten orbit sizes are

```text
                         8,8,8,8,8,8,8,2,8,4,       (1.3)
```

which sum to 70.  It is therefore enough to enumerate

```text
                         10*56=560                 (1.4)
```

normalized `(fixed lower,core)` tasks rather than 3,920.

## 2. Exact tail join and census

For a fixed task, permute the active triple into positions `1,2,3` and
choose distinct outside endpoints in positions `0,4`.  These five labels
determine `O_0` and `O_1`.  If the full owner deck is reflection-self, the
two necklaces `[-O_0]` and `[-O_1]` must occur among its ten four-windows.

For each possible physical target window and cyclic start, record the
required unknown positions `P_j subset {5,...,9}` and required remaining
labels `W_j`.  A constraint for target zero and one is compatible exactly
when the four membership classes

```text
P0 intersect P1,  P0-P1,  P1-P0,  outside(P0 union P1)          (2.1)
```

have the same sizes as the corresponding four classes of `W0,W1`.
Equivalently, after the individual cardinalities are fixed, it suffices to
match the intersection cardinality.  Bijections within these four classes
generate every compatible five-label tail and no incompatible tail.
Deduplication is by the literal tail before reconstructing the column.

Every reconstructed order is then checked directly for ten distinct owner
necklaces, ten distinct lower necklaces, and closure of the entire owner
deck under reflection.  No dihedral action or common translation is used.
The H100 census is

```text
fixed-lower boundary seeds                         241920
seeds with both compulsory mate windows             40912
compatible constraint pairs                         58936
deduplicated completed orders                    72639808
owner-nonsimple orders                             3627836
lower-nonsimple orders                               11864
owner-simple but not owner-self                   69000100
owner-self orders                                         8.   (2.2)
```

The final four status counts sum to `72,639,808`.  The eight retained
orders collapse to four distinct unordered `(owner deck,lower deck)`
pairs.  Literal reconstruction independently confirms on every retained
representative:

```text
fixed owners=2, fixed lowers=2,
owner action=nondihedral,
lower deck reflection action=undefined,
owner translating lift=nonconstant.                 (2.3)
```

The `11,864` lower-nonsimple orders are not silently discarded evidence:
each repeats a positive immediate-lower resource inside one column and is
therefore unusable in an exact lower ledger.

## 3. Multiplier closure and the matching-eight obstruction

Multiply the four normalized typed columns by all sixteen nonzero ground
elements, canonically translate every owner and lower row, and deduplicate
again by the two unordered decks.  The exact closure is

```text
owner/lower typed columns                              16
distinct owner decks                                    8
lower-deck realizations over each owner deck             2
distinct fixed-owner edges                               8
distinct fixed-lower edges                               8
distinct joint (owner edge,lower edge) pairs              8.   (3.1)
```

For each owner deck, its two lower decks are exchanged by reflection.
They share all ten owners, so using both would give owner load two on the
entire deck.  The eight owner fixed edges are pairwise vertex-disjoint;
the eight lower fixed edges are also pairwise vertex-disjoint.  Thus both
70-vertex graphs have the exact structure

```text
8 components of size 2, 54 components of size 1,
degree histogram 16 at degree1 and 54 at degree0,
maximum matching size 8.                               (3.2)
```

These eight owner decks are genuinely new relative to the frozen strong-self
catalogue.  Direct comparison with all `136,456` strong-self owner decks and
their `1,260` fixed distance-two edges gives

```text
candidate owner decks already strong                         0
candidate fixed edges in the strong distance-two graph       0
candidate fixed edges in the sample-zero fixed matching      0.   (3.3)
```

They may therefore augment an unfrozen owner-only master by a new fixed-edge
class.  They add no lift to the current sample-zero matching face, whose 35
fixed edges must be changed before any of them is selectable.

### Proposition 3.1 (the new edge class completes to an owner face)

Normalize each fixed owner bracelet to `0` plus four reflection pairs.  The
two four-pair sets on every new edge intersect in three elements.  Thus all
eight new edges are Johnson-distance-one edges, whereas the strong-self
projection consists of the 1,260 Johnson-distance-two edges.  This explains
their disjointness structurally.

Remove the sixteen new-edge endpoints from the strong distance-two graph.
The residual graph has 54 vertices and 756 edges, and its exact maximum
matching has size 27.  In the stable owner-orbit indexing returned by
`owner_orbits()`, the eight new edges are

```text
(22,31) (246,1391) (341,1290) (497,1301)
(509,1362) (704,832) (799,1347) (899,1145).          (3.4)
```

One strong-edge completion is

```text
(0,329) (16,227) (27,519) (165,1184) (200,1337)
(258,506) (285,1216) (310,1112) (369,1397) (384,502)
(396,1172) (425,1321) (430,802) (629,779) (752,1287)
(792,1366) (940,1381) (969,1156) (1107,1119) (1116,1396)
(1161,1195) (1200,1292) (1212,1377) (1221,1245)
(1333,1422) (1357,1429) (1368,1403).                 (3.5)
```

Their union is a verified perfect matching of all 70 fixed owner rows.
Hence the eight new decks do define a concrete new owner-only Benders face:
use one of their two lower realizations on the eight new edges and strong
self lifts on the 27 completion edges.  This positive owner statement does
not weaken the lower obstruction below; its fixed-lower support still has
only sixteen vertices.

A lower-exact reflection master would need odd load on all 70 fixed lower
rows.  Literal reflected nonself pairs contribute even load there.  The
only admissible owner-self columns with any fixed lower rows are `(3.1)`,
and owner exactness permits at most one lower realization above each of
their eight owner decks.  They can make at most sixteen fixed-lower loads
odd.  At least 54 fixed lower rows therefore retain the wrong parity,
which proves Theorem 0.1.

### Corollary 3.1 (unit mixed-C4 transport lower bound)

In a literal-reflection owner master augmented by the complete catalogue
`(3.1)`, at least 54 fixed-lower parities are wrong.  A unit mixed C4
lower-ledger move toggles exactly two lower rows, so any post-factor repair
using only such moves requires at least

```text
                              54/2=27                 (3.6)
```

mixed C4s.  On the strong-self-only face, none of the 70 fixed lower rows
is made odd, giving the sharper face-specific bound `70/2=35`.

This is a bound for unit lower-ledger C4 transports.  It is not asserted
for arbitrary larger atoms that may toggle more rows at once.

## 4. Scope

Proved here:

* complete normalization of every lower-simple period-ten column with a
  fixed lower bracelet;
* arbitrary nondihedral owner action and arbitrary rowwise translating
  lifts;
* the complete owner/lower typed catalogue and multiplier development;
* exact fixed-owner, fixed-lower, and joint edge graphs; and
* the joint lower-q1 no-go for literal reflected-pair owner masters.

Not proved here:

* a no-go after abandoning the reflected-pair owner architecture;
* a no-go for symmetry-breaking non-reflected representatives;
* a no-go after a successful mixed-C4 or larger post-factor transport; or
* any claim that the sixteen typed columns are all physical rails with
  different `(core,order)` data.

All substantive enumeration, replay, graph matching, compilation, and
hashing ran via SSH on H100.  The Mac was used only for reading, editing,
file transfer, and Git.
