# The q4 k17 pure-rail lift has one unavoidable typed collision and no adjacent-C8 repair

**Date:** 2026-08-14

**Status:** exact occurrence-level audit of the two explicit 14-rail
recoupled states, with exhaustive H100 polarity and adjacent-C8 searches.
The owner-only positive reserve remains valid.  No typed-simple two-state
package is claimed.

## 0. Outcome

The owner theorem does not lift by assigning both the intersection and the
union to every Johnson edge.  A closed pure rail has one whole-rail
polarity:

```text
lower lift: O_i -- (O_i intersect O_(i+1)) -- O_(i+1),
upper lift: O_i -- (O_i union     O_(i+1)) -- O_(i+1).
```

Either lift is a degree-two incidence cycle.  Selecting both shadows makes
every owner degree four and is not one pure-rail occurrence lift.  Edgewise
mixed polarity is outside the pure-rail host and is not used below.

For each recoupled state, all `2^14` whole-rail polarity choices were
enumerated.  Neither state has a choice whose active lower/upper q1 and q2
banks are all simple.  Nevertheless the obstruction is sharp: each state
has assignments with exactly one excess occurrence, and no other active
collision.

```text
state one: 160 minimum assignments, minimum excess 1,
state two: 320 minimum assignments, minimum excess 1.
```

The smallest polarity UNSAT cores have respectively seven and six clauses.
Exhausting the adjacent-C8 joint-recut compiler over all 480 minimum
assignments finds no repair.  Every cross-Johnson candidate already fails
exact lower-q1 refill.

## 1. Exact occurrence lift and rail residence

Let `O_0,...,O_(N-1)` be one displayed owner rail.  Its two possible q1
decks are

```text
L_i = O_i intersect O_(i+1),
U_i = O_i union O_(i+1).
```

The associated q2 shadows are

```text
L_i^(2) = O_i intersect O_(i+1) intersect O_(i+2),
U_i^(2) = O_i union O_(i+1) union O_(i+2).
```

All indices are cyclic.  A lower pure rail activates `L,L^(2)` and an
upper pure rail activates `U,U^(2)`; the opposite shore is not another
selected occurrence of the same edge.

Every displayed period is 10 or 11.  Along a q4 consecutive-window rail,
three consecutive Johnson supports contain exactly six distinct labels.
The owner positive run is four and the zero run is six or seven.  On the
upper shadow the corresponding runs are five and five or six.  Thus every
individual rail is internally q2-biresident.  The obstruction below is
cross-rail resource equality, not a defect inside one cyclic word.

## 2. Complete projected collision ledgers

Each state has 146 owners and hence 146 occurrences in every projected
q1/q2 shadow.  Before choosing polarities, the exact collision counts are

```text
                         state one                 state two
bank                distinct  collisions      distinct  collisions
lower q1               140       6                140       6
lower q2               131      14                129      16
upper q1               141       5                142       4
upper q2               141       5                144       2
```

The lower-q2 excess counts are 15 and 17 because one resource in each state
has multiplicity three.  Every other displayed maximum multiplicity is two.
The H100 ledger records every bitword and every `(rail,index)` provider.

The complete diagnostic shadow current `state_two-state_one` is

```text
bank          positive  negative  support  maximum absolute coefficient
lower q1         27        27       54                    1
lower q2         21        21       40                    2
upper q1         48        48       96                    1
upper q2         61        61      121                    2.
```

This four-bank current is a projection diagnostic, not a claim that both
q1 shadows were physically selected on every edge.

## 3. Whole-rail polarity is an exact 2-SAT gate

Give rail `R` a Boolean variable which is true for the upper lift.  If two
lower decks repeat a resource, simplicity gives the clause

```text
R is upper OR S is upper.
```

An upper collision gives the dual clause

```text
R is lower OR S is lower.
```

Keeping q1 and q2 occurrence provenance gives 32 distinct clauses for
state one and 30 for state two:

```text
                  lower q1  lower q2  upper q1  upper q2
state one             6        16         5         5
state two             6        18         4         2.
```

The exact minimum UNSAT-core sizes are

```text
state one  7 clauses, with 8 minimum cores,
state two  6 clauses, with 4 minimum cores.
```

Although the formula is UNSAT, the optimum collision excess is one.  The
160 state-one minimizers have exactly three possible sole defects:

```text
64  lower q2 10011000000001111  p10c4_1[1] = p11c0[6]
32  lower q2 00100000110001111  p11c2[0]   = pX1[2]
64  upper q2 11011100110001111  p10c4_1[3] = p11c1[7].
```

The 320 state-two minimizers have four possible sole defects:

```text
128 lower q2 01000000110001111  n10c1[4]  = nX2[5]
 64 lower q1 01100000110001111  n10c2[0]  = nX2[5]
 64 upper q1 11101000110001111  n10c1[3]  = n10c2[0]
 64 lower q2 00010000110001111  n11c3[10] = nX1[2].
```

These seven literal equalities are the complete minimum collision menu.

## 4. Why the adjacent-C8 compiler does not close the gate

For each q2 defect, either of the two owner edges in each bad three-owner
window was allowed as the prescribed pair of cuts.  Two further cuts were
chosen from arbitrary same-polarity rail occurrences.  The search exhausts

* both orders and both endpoint orientations of all four cuts;
* eight distinct cut owners;
* Johnson legality of all four cross edges;
* exact lower- and upper-q1 occurrence equality;
* complete active q1/q2 simplicity after rethreading; and
* the three-support residence condition on every resulting component.

For the two q1 sole defects, a q1-current-zero C8 is immediately inapplicable:
preserving the q1 Counter preserves the repeated occurrence.  This accounts
for 128 state-two minimum assignments.

For the q2 cases, the exact search counts are

```text
                         state one      state two
minimum assignments          160            320
target cut pairs with
  a direct Johnson join       256            192
target cut pairs without
  a direct Johnson join       384            576
complete cross-Johnson C8s    832            128
lower-q1-exact C8s              0              0.
```

Hence the adjacent-C8 interface proved for the D5 router does not apply to
any minimum q4 collision state: its first algebraic gate, exact lower-q1
refill, already fails.  No residence or topology conclusion is inferred
from a nonexistent q1-exact recut.

## 5. Sharp scope and next class

The obstruction is scoped to

```text
the two frozen 14-rail decompositions
+ whole-rail pure lower/upper polarity
+ one owner-disjoint adjacent alternating C8
+ two auxiliary cuts already present on same-polarity rails
+ exact lower and upper q1 refill.
```

It does not rule out:

* a current-moving mixed C4 which replaces the one repeated ticket by a
  missing ticket;
* a non-adjacent C8;
* a coupled `C6+C8` or a C10;
* a coupled pair of independently relabelled reserves;
* changing the cyclic orders while retaining the owner identity; or
* leaving the pure whole-rail host.

The smallest next target is therefore exactly one ticket: use a
current-moving local unit, rather than a q1-current-zero C8, to replace one
of the seven displayed duplicate occurrences without creating a q2 or
residence defect on either state.

## 6. H100 provenance

```text
typed occurrence/collision/current ledger
2cb1bccccb64142b8fc1eac7ae035ec0662a36eef40b39c21d955393c68be155
  scratch/audit_q4_k17_recoupled_typed_rail_ledgers_20260814.py
51e54a0422d4d850085b19502e2b4ac2e2b69d6102531588e1c48d481c6f380b
  scratch/audit_q4_k17_recoupled_typed_rail_ledgers_20260814.h100.out

exact polarity UNSAT/minimum-core replay
66f094f12e33ba96acd14a62f83caba1cc4fc8ed5eecac288bbc7d78c33cbb53
  scratch/audit_q4_k17_typed_polarity_unsat_core_20260814.py
4e033dfc912d91c802627c43de0ef8030e87f1117e64770cc4d41f232ee8e5b9
  scratch/audit_q4_k17_typed_polarity_unsat_core_20260814.h100.out

adjacent-C8 exhaustive search
666212f93c1bdad3c7f8c22e8a2534e2a00b1f90ab2c31b2b5f580766710c22b
  scratch/search_q4_k17_all_minimum_polarity_adjacent_c8_repair_20260814.py
c623e16ed6070f77d3d69563a80d45f51747b823da066fce2820c5880b8d9b9a
  scratch/search_q4_k17_all_minimum_polarity_adjacent_c8_repair_20260814.h100.out

shared C8 mechanics
136d27842979d888d028a68651b4d417a8650fccb0d552d44bb350fa48bb8e7d
  scratch/search_q4_k17_first_minimum_polarity_adjacent_c8_repair_20260814.py
```

All Python compilation, enumeration, replay, and hashing ran through SSH on
H100.  The local Mac was used only for reading, editing, transfer, and Git.
