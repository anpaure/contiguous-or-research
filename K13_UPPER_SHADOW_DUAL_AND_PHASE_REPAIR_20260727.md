# The upper-shadow dual at the current `k=13` bridge

Date: 2026-07-27

## 1. An exact cut identity

Let `T_i` be a cyclic Johnson walk on rank-seven sets and put

\[
U_i=T_i\cup T_{i+1}\in\binom{[13]}8.
\]

Consecutive `U` values are either equal or Johnson-adjacent.  For a rank-nine
set `B`, define

* `L_B = #{i: U_i subset B}`;
* `e_B = #{i: U_i=U_{i+1} subset B}`;
* `R_B` to be the number of cyclic runs of indices satisfying `U_i subset B`;
* `m_B = #{i: U_i union U_{i+1}=B}` (only rank-nine unions count).

Every internal adjacency of the index set is either a loop counted by `e_B`
or a genuine `B`-coloured Johnson edge.  Since a cyclic set with `L_B`
positions and `R_B` runs has `L_B-R_B` internal adjacencies,

\[
\boxed{m_B=L_B-e_B-R_B
      =L_B-e_B-\frac12|\partial\{i:U_i\subset B\}|.}
\]

Thus an upper-q2 hole is a saturated cut, not merely a missing occupancy.
Repairing it requires merging two compatible q1 blocks (or changing a loop),
which is a chronological condition invisible to the q1 load histogram.

There is a local degree version as well.  If `l_A=#{i:U_i=A}` and `e_A` is
the number of loops at a rank-eight set `A`, then

\[
\sum_{B\supset A}m_{A,B}=2(l_A-e_A),
\]

where `m_{A,B}` counts incidences at `A` of non-loop transitions coloured
`B`.  This is the upper analogue of the lower compiler charging identity:
the q1 loads are vertex degrees and the q2 loads are Johnson-edge colours.

## 2. The old `(6,2)` bridge

For `scratch/k13_bridge_q2h26.certificate.json`, the two missing q2 orbit
representatives were `1663` and `2011`.  At either physical representative,

\[
(L_B,e_B,R_B,m_B)=(10,0,10,0).
\]

All ten compatible q1 occurrences were isolated.

* `1663` contained no missing q1 orbit and only one duplicated compatible
  q1 orbit (`1647`).  It was necessarily a pure chronology repair.
* `2011` contained the then-missing q1 orbit `1743` and duplicated compatible
  q1 orbits `1439,1499`, so it admitted a coupled q1/q2 move.

An explicit arity-three endpoint circulation

```
lower 1357: add 1,7  -> 1,9
lower 1235: add 5,12 -> 5,9
lower 1229: add 5,12 -> 5,8
```

filled `1663`, kept the six q1 holes, preserved lower q2 and both q3 shadows,
and kept one quotient cycle of voltage one.  Its only failure was one
residence-defect orbit: coordinate `8` was inserted at quotient position 64
and deleted after a run of length two.  The defect window uses lower choices
`1235,723,423`.

Exhausting a second simple endpoint circulation through support six found no
compensation other than the inverse move.  This accurately predicted the
later successful length-eleven mesoscopic circuit: the q2 defect was not
locally removable, but it was removable.

## 3. The current `(5,1)` bridge

The authoritative cycle is

```
scratch/k13_bridge_l11_q1h65_q2h13.certificate.json
sha256 966251fda4a0eddf24fb7c06b00e8b941b6441911de4d37b19c3f63fe8774501
```

Its cyclic upper-q1 orbit holes are

```
639, 703, 951, 1965, 2775
```

and its sole upper-q2 hole is `2011`.  (The list containing `863,1277` was
from the earlier length-eight seed.)

For `B=2011`, the cut remains maximally fragmented:

\[
(L_B,e_B,R_B,m_B)=(10,0,10,0).
\]

The nine compatible q1-subset orbit loads are all one except `1275`, whose
load is two.  None of the five q1 holes lies in this `B`-clique.  Therefore
the current 65 rank-eight misses and 13 rank-nine misses form a genuine
inclusion antichain: filling `2011` cannot automatically fill a q1 hole.

This gives the correct local branching rule: a repair must create an internal
edge of the ten-block cut, and only one compatible q1 orbit supplies duplicate
vertex slack.

## 4. Double-endpoint audit

The targeted program

```
scratch/search_k13_l11_double_q2_repair.py
```

enumerates a one-choice `2011` witness with endpoint delta
`+a+b-c-d` and closes it by two directed endpoint paths.

There are 34 distinct q1-safe double witnesses.  With each compensation path
of length at most three (total arity at most seven), the exact census is

| stage | count |
|---|---:|
| compatible path pairs | 5,137 |
| retain at most five q1 holes | 605 |
| connected, nonzero voltage | 211 |
| fill `2011` | 42 |
| residence-safe | **0** |

Allowing path length four produced 428,834 compatible pairs and 1,473
connected/q1-safe/q2-exact candidates.  Exactly one was residence-safe, but
it failed the lower-q2/q3 constraints.  Thus no bounded double circuit in
this audited class closes the current seed.

The best small near-motif has arity four:

```
lower 219: add 5,10 -> 8,9        (double endpoint move)
lower 237: add 1,12 -> 1,8
lower 123: add 2,11 -> 2,7
lower 729: add 1,12 -> 10,12
```

It fills `2011`, retains all five q1 holes and both q3 shadows, but creates
two residence-defect orbits and two lower-q2 holes (`61,173`).  Exhausting a
second simple circulation through support five produced 227 connected,
q2-exact candidates and no residence-safe one.  This is a relocation, not a
closure.

The corresponding artifacts are

```
scratch/k13_l11_double_q2_p3.json
scratch/k13_l11_double_q2_p4.json
```

## 5. The better near state and a phase-level repair target

The most useful state is not the double motif but the stored residence-perfect
length-eleven circuit

```
scratch/k13_bridge_near_q1h65_q2h0_lq2h13_q3d13.certificate.json
```

It has exact upper q2, five upper-q1 holes, one lower-q2 hole (`405`), and one
lower-q3 hole (`337`).  For its rank-five lower-q2 word

\[
Y_i=T_i\cap T_{i+1}\cap T_{i+2},
\]

the lower dual of the cut identity shows that target `R=337` has

\[
(L_R,e_R,R_R,m_R)=(1,0,1,0).
\]

There is only one aligned carrier, at quotient position 117:

```
Y_116 = {0,2,4,6,11}, canonical orbit 341, phase 2
Y_117 = {0,4,6,8,11}, the unique carrier of R
Y_118 = {0,4,5,8,11}
```

The decisive observation is that orbit `341` at phase zero is

```
{0,2,4,6,8}.
```

Replacing only the phase of `Y_116` from two to zero would keep exactly the
same lower-q2 orbit while making

\[
Y_{116}\cap Y_{117}=\{0,4,6,8\}=337.
\]

So the q3 defect has a **zero-orbit-cost phase repair**.  The involved local
edge lowers are `343,1365,663`.

The remaining q2 hole `405` is also locally plausible: many rank-five orbit
occurrences of load at least two are one set-swap from a phase of `405`.
Consequently the sharp next SAT/LNS target is:

1. enforce the phase-`0` witness of orbit `341` adjacent to the unique
   `337` carrier at position 117;
2. transfer one duplicated rank-five occurrence into orbit `405`;
3. freeze outside the two carrier neighborhoods while retaining the exact
   upper side and residence.

This is stronger than asking globally for lower q2/q3 again.  It identifies
the two exact phase movements that can close the best near state without
paying another shadow orbit.

## 6. Exact-q2 lane and the forced-star compiler obstruction

An exact-q2, residence-perfect carrier was obtained with nine upper-q1 hole
orbits, and a two-edge endpoint circuit reduced this to eight while preserving
every q2 target.  Exhaustive single-circuit search through length eight then
found no second reduction.

The initially promising `compiler_core_missing_count=0` condition is only a
pointwise condition: every lower target has at least one envelope window.  It
does not express simultaneous feasibility.  On the length-ten core-feasible
candidate, the exact rank-5/6 compiler is already UNSAT.  Deletion shrinking
gives the four-mask obstruction

\[
X=5410=\{1,5,8,10,12\},\qquad
X+\{2\},\ X+\{3\},\ X+\{4\}.
\]

The three rank-6 supersets have unique length-three windows, starting at
`1496`, `1618`, and `408`.  The rank-5 target has eight candidate windows.
The three coincident windows would erase the unique extra coordinate of the
corresponding rank-6 target.  The other five windows, starting at
`253,472,574,714,1610`, erase the final middle support of coordinates
`6,9,11,7,0`, respectively.  Every three masks are feasible; all four are
not.

The script

```
scratch/sigma_rank56_forbidden_star_screen.py
```

implements the resulting unit/Hall screen.  On the cyclic carrier it finds
117 forbidden rank-5 targets, exactly the nine missing lower-q2 orbits.  The
linear seam rescues six physical targets, leaving 111 forbidden.  This is a
strictly stronger scalar objective than pointwise core reachability.

## 7. The q6 Hall obstruction is twelve copies of one rooted component

After a neutral six-cycle and a q1-improving seven-cycle, the carrier has six
upper-q1 holes, exact q2, and zero residence defects, but the all-lower Hall
matching has deficiency twelve.  Its alternating witness splits into twelve
disjoint components, each with ten targets and nine cells.

The rank-4 roots are the translation orbit of `393`, except for the one seam
rotation `2146`.  A representative root is

```
R = 6288 = {4,7,11,12}.
```

Its component consists of `R`, the three rank-5 targets
`6292,6320,6800`, and the six rank-6 targets
`6324,6384,6801,6802,6804,6832`.  The nine neighboring cells are three
depth-1 branch cells and six depth-2 leaf cells.  There is no depth-0 cell
for `R`, giving deficiency one in every translated component.

This identifies a cheap compiler-facing screen: a lower-q3 hole orbit is bad
when its rotations have no safe depth-0 maximal-erosion cell.  Hole orbit
`393` is bad in precisely this sense; not every lower-q3 hole is bad.

## 8. A six-cycle repairs Hall without returning either q1 hole

The endpoint circuit

```
7 -> 95 -> 92 -> 121 -> 106 -> 10 -> 7
```

with lower masks

```
303, 1253, 1229, 1331, 371, 311
```

replaces lower-q3 hole `393` by the benign hole `225`, preserves all six q1
gains, exact q2, and residence.  In the repaired carrier the representative
root `6288` receives a safe depth-0 cell at position `1464`, whose envelope
is exactly `6288`; this supplies the missing tenth cell in every translated
Hall component.

The resulting certificate is

```
scratch/k13_q1h6_neutralB_l6.certificate.json
```

and its exact linear depth-3 compiler is SAT in 0.24 seconds.  The compiled
word covers every lower target and misses only 79 upper masks: 78 of rank 8
and one of rank 9.  Thus the lower compiler gate is now closed at q1 defect
six; the remaining task is an upper-side improvement that preserves this
new safe-erosion geometry.

## 9. The seam can be chosen for free, and q1 descends to five

For the six-hole carrier there are 507 physical cuts at which the omitted
upper-q1 carrier is duplicated and both omitted upper-q2 carriers retain
another occurrence.  At cut shift seven the lower Hall condition remains
feasible and the compiled word misses exactly 78 masks, all at rank 8.  Thus
the apparent rank-9 miss of the first linearization was only a seam artifact.

The subsequent Hamming-nine repair

```
scratch/k13_q1h5_repairu2_hamming9.certificate.json
```

reduces the upper-q1 defect to five orbits while keeping exact q2, residence,
and lower Hall feasibility.  It again has hundreds of jointly safe seams;
cut shift seven gives a SAT lower compiler whose word misses exactly 65 masks,
all rank 8:

```
scratch/k13_q1h5_repairu2_hamming9.cut7.word
```

The current quotient q1 profile is

\[
0^5 1^{60}2^{31}3^2 4^1.
\]

Direct donor-to-hole routing has minimum endpoint imbalance six, so closing
all five holes requires at least three compensator arcs and at least eight row
changes.  This is consistent with, rather than contradicted by, the observed
Hamming-nine repair scale.
