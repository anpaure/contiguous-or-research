# Hostile audit: the canonical square is a phase obstruction, while the six-owner cable closes the local two-dart topology

**Date:** 2026-08-14  
**Audited files:**

* `MATH_LEMMA_D5_DISTANCE_TWO_RESET_COMPLETES_TO_UNIQUE_JOHNSON_SQUARE_20260814.md`;
* `MATH_THEOREM_ADJACENT_TERMINALS_HAVE_A_MINIMAL_SIX_OWNER_RESIDENT_TWO_CHANNEL_CABLE_20260814.md`.

**Verdict:** **PASS** after the incidence-scope and residence wording repairs
recorded below.  The square theorem is a normal-form and phase-obstruction
theorem, not an isolated alternating factor trade.  The cable theorem is an
exact closed local construction and an architecture-relative six-owner
minimum.  At rank seven, a cable and the 18-owner marked-C6 router can be
chosen with disjoint q1 and q2 interiors for each of the three endpoint
orbits.  This is a cut-open local compatibility result; no simultaneous
164-row planting, endpoint splice, or crossing-current theorem follows.

## 1. Canonical distance-two normal form

For

\[
 d_J(T,B)=d_J(T,C)=1,\qquad d_J(B,C)=2,
\]

write

\[
 T=K+x+u,\qquad B=K+u+y,\qquad C=K+x+v.
\]

The four active labels are distinct, and

\[
                         D=K+y+v
\]

is the unique opposite corner obtained by commuting the two disjoint
exchanges `x<->y` and `u<->v`.  There are two additional common Johnson
neighbours of `B,C`; they are not counterexamples because their adjacent
exchanges share an active label and do not form this commuting square.

The four edge intersections are

\[
 K+u,\quad K+y,\quad K+v,\quad K+x,
\]

and the four unions are

\[
 K+x+u+y,\quad K+u+y+v,\quad K+x+y+v,\quad K+x+u+v.
\]

Both palettes are simple on one square.  This does not make the square a
fixed-bank factor switch: the two owner matchings use different two-element
lower and upper subpalettes.  After subdivision, a selected Johnson edge is
a two-incidence arc, not one edge of an alternating matching on the
incidence `C8`.  The source note now states this distinction explicitly.

The cyclic active trace is `1100`; its proper owner runs are `(2,2)`, one
below the D5 lower-owner depth-two target `(3,3)`.  Thus the square is also
not an undilated resident collar.

## 2. Exact frozen phase census

For a square to be the literal suppressed-owner two-switch at one D5 row,
the old collateral edge `DC` must be in the old factor and `DB` in the new
factor.  The H100 replay gives

```text
DC old  DB new  rows
   0       0     139
   0       1      12
   1       0      13
```

No row has both phases.  Likewise, none of the 48 adjacent-head triangle
geometries has its third old edge `BC`.  Hence none of the 212 canonical
owner circuits is an isolated D5 factor trade.

The independent full-square census sharpens the resource obstruction:

```text
commuting D occurrences / distinct values       164 / 163
D occurrence multiplicities                     162 x 1, 1 x 2
D occurrences hitting prescribed terminals       20
D occurrences hitting touched D5 owner bank       50

four-edge lower occurrences / distinct values   656 / 629
lower multiplicities                             602 x 1, 27 x 2
four-edge upper occurrences / distinct values   656 / 572
upper multiplicities                             490 x 1, 80 x 2, 2 x 3
```

All 572 distinct square upper values already occur in both frozen factors;
516 of the 629 lower values occur in the old factor and 510 in the new.
Every forced `D` is, of course, already a middle-level owner in the spanning
factor, so installing a square requires recutting rather than adjoining a
new disjoint owner.  The former count of 209 mixed these 164 fourth-corner
occurrences with prescribed owners from the 48 triangles and is not an
auxiliary-owner statistic; the corrected source no longer uses it.

This leaves exactly the source note's two routes: globally telescope the
collateral actions, or absorb each one in a separate marked-socket collar.

## 3. Why a one-edge lead is insufficient

A factor socket has two boundary darts.  Moving an internal socket `E` to an
external terminal `C` conjugates a return map only when there are two
state-independent channels

\[
 C^{\rm in}\longrightarrow E^{\rm in},\qquad
 E^{\rm out}\longrightarrow C^{\rm out}.
\]

One undirected Johnson edge `CE` supplies only one channel.  Traversing it
twice repeats a factor resource; retaining both closed endpoint incidences
instead gives degree three or four.  This is why the metric three-choice
common-neighbour SDR is not itself a physical connector.

## 4. The six-owner resident cable

For adjacent `C,E`, write

\[
 H=C\cap E,\quad C=H+z,\quad E=H+b,
\]

choose `a in H`, put `K=H-a`, choose distinct `x_1,x_2 in K`, and choose
distinct exterior `y_1,y_2`.  The displayed cycle

\[
 C,E,P_1,P_2,Q_0,Q_1,C
\]

has the two `C--E` arcs

\[
 C-E,\qquad C-Q_1-Q_0-P_2-P_1-E.
\]

These are the required two distinct channels.  Direct formula comparison
verifies six distinct owners, six distinct lower q1 resources, six distinct
upper q1 resources, and six distinct values on each q2 shore.  The owner
trace has exact nonconstant run pair `(3,3)`, while direct reading of the
immediate-upper trace gives `(4,2)`.  Installing the same cable in both
states gives zero signed q2 current internally.

The rank hypothesis `r>=4` is sharp for the displayed choices:
`K` has size `r-2` and must contain two clocks.  The H100 verifier rebuilt a
normalized representative at every rank `4<=r<=40` and checked all five
simple resource decks and both residence minima.

The six-owner lower bound is valid in the stated cyclic architecture.  Any
nonconstant q2-biresident owner cycle has a coordinate with a positive run
of at least three and a zero run of at least three.  A tapped larger router
or a noncyclic boundary fragment lies outside this minimum, as the theorem
states.

## 5. Rank-seven cable/router compatibility

Normalize a rank-seven distance-two terminal triple.  For each of the three
common neighbours `E` different from the occupied tail, the H100 search
enumerated:

```text
endpoint orbit  cable candidates  marked-C6 router candidates
      1               2320                    5520
      2               2320                    5760
      3               2240                    6720
```

For every orbit it finds a cable and 18-owner marked-C6 router such that:

* their owner intersection is exactly the intended boundary owner `E`;
* their lower-q1 and upper-q1 interiors are disjoint;
* their lower-q2 and upper-q2 decks are disjoint;
* the cable interior avoids prescribed `T,B`; and
* the router interior avoids prescribed `T,C`.

The witness is deliberately interpreted after cutting at `E`.  The union of
the two *closed* cycles would give `E` degree four and is not a factor.  The
search does not certify which endpoint incidences are replaced, the q2
windows crossing that splice, the fixed tail spectator, or compatibility
among 164 simultaneous copies.  These remain the exact gate.

## 6. H100 binding

All compilation, replay, and hashing below were performed on H100.

```text
canonical-square phase verifier
  5b52960e5b1d525e8d32ff027e5ecacbb1fcca72dc7616a3dde34aa0f0b8ed23
canonical-square phase output
  386fc81923fd207a9ed6793a2211f01c7146e96f080d6bb2e00ed7c9550cc8a4

full-square collision verifier
  b5a58029a6271b874b6f0cc7d6e6a7f3faac5a660d41b65c5fed20104941e4bd
full-square collision output
  fa3b00f8ef9946315419555721b7163859b0be7ab859f44eb1abe73e7be6bcd2

resident-cable/rank-seven compatibility verifier
  985bfbee998a8c41fe63c32c48620c17b9bec9a13d231d6b72a838de62f4dfc8
resident-cable/rank-seven compatibility output
  9b6ec28c6ebfaff1290398e7dbfb9ae776b9a5c27612e32a9a023e894c93c7bc
```

The sharp remaining gate is a simultaneous cut-open splice theorem: select
164 endpoint/cable/router packages disjointly from the D5 bank and from one
another, add the 48 adjacent-terminal packages and fixed spectators, and
audit every lower/upper q2 window and residence collar crossing the replaced
endpoint incidences.
