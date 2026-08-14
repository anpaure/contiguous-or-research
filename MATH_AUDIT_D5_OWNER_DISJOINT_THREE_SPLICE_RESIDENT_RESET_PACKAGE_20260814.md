# Hostile audit of the owner-disjoint three-splice resident reset package

**Date:** 2026-08-14

**Audited source:**
`MATH_THEOREM_D5_OWNER_DISJOINT_THREE_SPLICE_RESIDENT_RESET_PACKAGE_20260814.md`

**Verdict:** **PASS as an individual closed local package, with the source's
cut-open-context proviso essential.**  Both literal terminal variants have
36 distinct rank-seven owners, exact old component lengths `6,12,18`, one
new 36-cycle, marked action `(B U C)`, suppressed action `(B C)`, equal and
simple occurrence decks at all five typed levels through q2, and the stated
two-shore run minima.  The adjacent/hard spectators lift to the exact
rank-11, ground-23 signatures.  The result does not yet give a physical
two-dart graft into the frozen D5 factor, simultaneous planting of 212
copies, or a global owner/q1/q2 palette theorem; the source explicitly
excludes all three stronger readings.

## 1. Literal graph audit

The six input C6 cycles are `EB,EC,D,R0,R1,R2`.  The literal owner table has
six rank-seven owners in each cycle and all 36 occurrences are distinct.
The accounting is therefore exact:

```text
ambient EB,EC owners       12
new cable D owners          6
new router R0,R1,R2        18
--------------------------------
physical owner bank        36.
```

The three ordinary splices delete two edges and add two cross edges each.
The source transcribes all six removed and all six added pairs literally;
comparison with both frozen witnesses and the literal-table dump finds no
reversed endpoint, omitted edge, or variant mismatch.  Every new pair has
rank-seven symmetric difference two.  Reconstructing adjacency from the
edge sets gives degree exactly two at every owner, so no splice identifies
owners or creates a degree-four vertex.

The router seam replacement changes only `R_i[0]--R_i[1]` to
`R_i[0]--R_(i-1)[1]`; the `R0[3]--R0[4]` edge used by the exterior splice is
phase-common as claimed.  After the identical exterior splices, independent
edge traversal gives

```text
old: 6,12,18
new: 36.
```

Thus the added-owner charge is 24 relative to the two assumed ambient C6
cycles, not 36.  The source correctly labels the 12 exterior owners as an
ambient hypothesis rather than as a free construction.

The cut-open reduction now requires each further collar cut to be both
nonincident with its marked owner and retained after the three internal
splices.  Both restrictions are necessary.  In particular, for the adjacent
variant the internal `EC--D` cut is nonincident with the chosen mark `C`, so
nonincidence alone would still permit deleting the same edge twice.  The
final source explicitly excludes this case.

## 2. Marked action and the boundary scope

For both terminal variants, direct oriented traversal of the frozen cycle
lists gives

\[
 B\mapsto U,\qquad U\mapsto C,\qquad C\mapsto B.      \tag{2.1}
\]

The old components each contain exactly one of the three marks, so the old
first-return action is the identity.  Omitting `U` from the marked set turns
`(2.1)` into `B<->C`.  This verifies the stated local monodromy, including
its direction, rather than merely checking that the new map is some
three-cycle.

This is not yet the full physical boundary-dart theorem needed by the D5
factor.  A closed marked cycle determines the oriented first-return
permutation used above, but a context substitution must additionally choose
the two cut darts at each exterior strand, prove every cross edge Johnson,
and prove that suppressing the package reconstructs the prescribed factor
edges and complete q1 palettes.  The theorem's Section 3.1 makes exactly
this distinction and lists the missing global checks.  Accordingly the
local first-return result passes; reading it as an already instantiated
cut-open D5 graft would be an overclaim.

The tail `T` is likewise only a distinct, unchanged spectator owner.  It is
not part of the 36-cycle bank and supplies no cycle or residence collar by
itself.  This is sufficient for the terminal Venn signature, but a context
compiler must provide the physical tail strand and its collars separately.
The source states this limitation correctly.

## 3. Typed occurrence decks and residence

For each oriented owner cycle `V`, the audit independently recomputed

\[
 V_j,\quad V_j\cap V_{j+1},\quad V_j\cup V_{j+1},\quad
 V_j\cap V_{j+1}\cap V_{j+2},\quad
 V_j\cup V_{j+1}\cup V_{j+2}.                       \tag{3.1}
\]

For both adjacent and hard witnesses, each old and each new bank in `(3.1)`
has 36 distinct values, and the old/new occurrence Counters agree exactly
at every typed level.  Thus lower-q2 and upper-q2 currents vanish as
occurrence currents, not merely after support reduction.

The original independent verifier asserts simplicity directly through q1
and prints q2 distinct counts `36,36`; the palette dumps record all 180
old/new occurrences and explicitly report q2 distinctness and multiset
equality.  The new hostile replay additionally asserts q2 distinctness,
closing the minor assertion-strength gap in the original verifier without
changing the theorem.

Scanning every nonconstant coordinate cyclically gives, in both phases,

```text
owner trace:          one/zero minima 3,3
immediate-upper trace one/zero minima 4,2.
```

The scan includes the six new cross edges and every cyclic closing join.
Moreover, each of the six input C6 ingredients separately has the same
`(3,3,4,2)` minima.  This proves the claimed closed-package residence.  It
does not audit new runs formed after cutting the package and attaching an
external context; those collar checks remain among the source's explicit
conditions.

## 4. Terminal geometry and lift

The adjacent spectator/head triple has

\[
 (d(T,B),d(T,C),d(B,C),|T\cap B\cap C|,|T\cup B\cup C|)
 =(1,1,1,6,9),                                      \tag{4.1}
\]

and the hard triple has `(1,1,2,5,9)`.  In each case `T` is a rank-seven
owner outside the complete 36-owner bank.

Adjoining the same four new coordinates to every owner raises ranks from
seven to eleven, raises the triple-intersection and triple-union sizes by
four, and preserves the three Johnson distances.  Six further unused-zero
coordinates raise the ground size from 17 to 23 without changing any set.
The lifted signatures are therefore exactly

```text
adjacent: (1,1,1,10,13)
hard:     (1,1,2, 9,13).
```

Common-one and unused-zero coordinates are constant on every trace, so the
lift preserves Johnson adjacency, typed-deck equality and injectivity,
component action, and all nonconstant-coordinate run minima.

## 5. Exact scope after audit

The theorem proves:

1. one literal closed resident package for the adjacent terminal type;
2. one literal closed resident package for the hard terminal type;
3. owner charge 24 relative to two assumed six-owner exterior cycles;
4. exact local three-cycle/two-mark quotient action; and
5. zero typed occurrence current through q2.

It does **not** prove:

1. that the frozen D5 terminal occurrences already contain the two ambient
   exterior cycles;
2. a cut-open two-dart substitution into one prescribed D5 row;
3. simultaneous resource-disjoint coinstantiation of 212 copies;
4. preservation of q2 windows or residence collars crossing context cuts;
5. recovery of the complete frozen-D5 factor topology after all grafts.

These exclusions agree with the source's status and Sections 3.1 and 5.
No source correction is required.

## 6. H100 replay and hashes

All replay and hashing used `ssh h100`.  The new standalone hostile audit
imports none of the search/verifier/palette code.  Its outputs explicitly
record `cut_open_context_substitution_verified: false` to prevent the local
PASS from being promoted to a global compiler theorem.

| artifact | H100 SHA-256 |
|---|---|
| theorem source | `4fc8a4aa81cbd1c139bf30317fa03f2c77962db1b43d9c1972fa3d6d31615cf6` |
| original independent verifier | `5c1e93fe44c13717af8dd19e885d088c07dfe45ea747bf248c6c6b180f5c773c` |
| original adjacent verifier output | `563ffbe87729ff14e9cb73de0b87de6a171c5eecd94b4eb3100e70e296a0ddd3` |
| original hard verifier output | `f2b2e82503ae8ef8c4c14ed8604ac72702230e312491bc2d64ada9fff995a072` |
| palette dumper | `9221575d6ea72cc428f41af0f3ca910f41ee8b10f855ed4372c4d9bd6c7d04ee` |
| adjacent palette dump | `500286642c7d2a6db36c8d991e569604e23c0c8cec1ff8eb4f98a07c70de1bce` |
| hard palette dump | `0bb3d2dbca28d63e503bed34f8e3f9a2c9f3f3b9a2c2214251c69f319ca8d802` |
| standalone hostile audit | `6ebf74bd52f5293b8ddf3cb61d40087a8530e16cf7455a0256afcbc55a838098` |
| hostile adjacent output | `4f544541aeac8f34cd4b7c7b90f3c296ccc408c58fcf68c7f4f699caa0e4cc74` |
| hostile hard output | `235479e4cd7f404498c35f36bf9814a9068774ffc2887bee92aa356bd9396c92` |

The theorem, this audit, and the two hostile replay outputs are safe to
freeze together in the stated local scope.
