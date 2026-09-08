# Unit C4, opposite C8, and C10 do not repair the sole q4 k17 typed collision

**Date:** 2026-08-14

**Status:** exact continuation of the frozen whole-rail polarity audit.  All
480 minimum-collision polarity states are exhausted on H100.  No
typed-simple resident recoupling exists in the three declared single-switch
classes.  A coupled multi-switch or cross-copy current transfer remains
open.

## 0. Starting point

Each frozen 14-rail state admits pure lower/upper polarity assignments with
exactly one active collision and no others:

```text
state one  160 assignments, three possible q2 collision types,
state two  320 assignments, two q2 and two q1 collision types.
```

The adjacent q1-current-zero C8 already has no exact q1 witness.  This note
tests the next three single-switch classes:

1. the exact mixed-C4 unit current from the GMM normal form;
2. a q1-zero C8 with the two prescribed cuts opposite; and
3. a q1-zero C10 with the prescribed cuts at both cyclic distances.

Every search uses the literal owner cycles and active pure-rail polarities,
not just their resource names.

## 1. Mixed C4 unit-current search

For every minimum assignment, one old cut must touch one provider window
of the sole collision.  The second old cut may be any owner-disjoint edge
on a rail of the same polarity.  Both cross matchings and all endpoint
orientations are enumerated.

A candidate is accepted as a mixed C4 only when its lower and upper q1
currents are both elementary units:

```text
one positive resource, one negative resource, coefficients +/-1.
```

This is exactly the occurrence form of

```text
lower:  e_(K+a) - e_(K+b),
upper:  e_(K+p+b+c) - e_(K+p+a+c).
```

The exhaustive census is

```text
                                  state one   state two
owner-disjoint old edge pairs        46592       59584
legal cross-Johnson C4s                896        2368
mixed unit-current C4s                 512         960
typed-simple results                     0           0.
```

All 1,472 unit C4s leave or create an active collision.  In state one, 256
leave excess one and 256 leave excess two.  In state two, the counts are
576 and 384.  Thus the mixed unit has exactly the right current scale but
not the right literal target pair.

The best state-one near miss moves

```text
lower  +{0,1,4,9,13,14,15,16} -{1,3,4,9,13,14,15,16},
upper  +{1,3,4,8,9,10,13,14,15,16}
       -{0,1,4,8,9,10,13,14,15,16},
```

and leaves one upper-q2 duplicate.  The best state-two near miss leaves one
lower-q1 duplicate.  Both have minimum three-support union four, so neither
is resident even before attempting a second closure.

Consequently a single mixed C4 cannot be the typed reserve compiler.  Its
proper role, if any, is as the current-moving half of a coupled repair.

## 2. Opposite-placement C8

For every q2 minimum assignment, one edge in each bad window is prescribed.
The two cuts occupy opposite positions in the old four-edge matching, with
two arbitrary same-polarity auxiliary cuts.  All orientations are tried.
The two q1-defect types are excluded for the exact reason that a q1-zero
switch cannot remove a q1 multiplicity.

The search finds

```text
state one  384 complete cross-Johnson C8s, 0 lower-q1-exact,
state two    0 complete cross-Johnson C8s;
             128 q1-defect assignments interface-impossible.
```

Thus changing the relative C8 placement does not evade the adjacent-C8
obstruction.

## 3. Five-cut C10

The C10 search uses five old same-polarity rail edges and their cyclic cross
matching.  The two bad-window cuts are placed at each inequivalent distance
one and two in the five-cycle.  A sparse DFS enumerates every oriented
cross-Johnson cycle and all three auxiliary cuts.

Exact counts are

```text
state one  2,368 cross-Johnson C10s, 0 lower-q1-exact,
state two    224 cross-Johnson C10s, 0 lower-q1-exact,
             128 q1-defect assignments interface-impossible.
```

No candidate reaches upper-q1, active-q2, or residence testing because the
lower-q1 occurrence Counter already fails.

## 4. Sharp remaining gate

The following single-switch ladder is now exhausted on all minimum
whole-rail polarity states:

```text
adjacent q1-zero C8,
opposite q1-zero C8,
five-cut q1-zero C10,
one mixed unit-current C4.
```

The q1-zero switches fail exact lower refill.  The current-moving C4 exists
but cannot simultaneously hit the missing lower and upper tickets, remove
the q2 duplicate, and preserve residence.

The smallest unresolved classes are therefore genuinely coupled:

* one mixed C4 followed by a collar-restoring C6/C8;
* an aggregate-q1-zero `C6+C8` whose individual switches carry opposite
  q1 currents; or
* two independently relabelled reserve copies with a cross-bank mixed C4
  moving a duplicate ticket of one copy into a missing ticket of the other.

No generic C8/C10 atlas conclusion is claimed.  The no-go is specific to
the seven sole-collision types and the displayed existing-cut menus.

## 5. H100 provenance

```text
mixed-C4 unit-current search
8312cfbbcd97983b5e228cc2df70fb7f63ab96d204d6b5a294981e99507de318
  scratch/search_q4_k17_all_minimum_polarity_mixed_c4_repair_20260814.py
052b4462c4a870eb1147925124b07ec0184093c4d741862c5df4540f4daae9e9
  scratch/search_q4_k17_all_minimum_polarity_mixed_c4_repair_20260814.h100.out

opposite-C8 search
67db00a7b5b3257a3a965a5a895abfed44da5be426873ca309aa1bda0ebef594
  scratch/search_q4_k17_all_minimum_polarity_opposite_c8_repair_20260814.py
d9d18922b05f0f3919545312e00109b31539499d6d2eba6ac44c5fa9fdb538c0
  scratch/search_q4_k17_all_minimum_polarity_opposite_c8_repair_20260814.h100.out

C10 search
7c4023c34a1ad70b41951a9bef1893cbb6000fe0aa3f7d0c6eb06503466ca6f8
  scratch/search_q4_k17_all_minimum_polarity_c10_repair_20260814.py
80f4f593752308c890eade6cbf3dfde9eeb3a709d19fa1e680f2550b4c7b104a
  scratch/search_q4_k17_all_minimum_polarity_c10_repair_20260814.h100.out
```

All Python compilation, enumeration, replay, and hashing ran through SSH on
H100.  The local Mac was used only for reading, editing, transfer, and Git.
