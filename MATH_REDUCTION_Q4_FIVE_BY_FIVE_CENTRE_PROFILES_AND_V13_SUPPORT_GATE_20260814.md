# The q4 five-by-five atom reduces to ten support-feasible V13 cases

**Date:** 2026-08-14
**Status:** exact centre-ledger classification and exact binary support
reduction.  This note does not assert cyclic-window named-owner existence.

## 0. Outcome

For a `q=4` one-owner atom made from five period-10/11 rails on each
shore, the net centre mass is either four or five.

* At net mass four, the four-rail equality ledger is forced to be Profile I
  from the four-by-four obstruction, plus one cancelling centre/period pair.
  The cancellation cannot be centred at the exceptional `t=-5` target.  On
  a thirteen-label ground, each of the other three centre types
  `A,C,exterior` is support-feasible for either cancelling period.
* At net mass five there are exactly six centre profiles, even allowing
  arbitrarily many exterior centre labels.  On a thirteen-label ground,
  Profiles 1 and 6 are support-infeasible by explicit hole-capacity
  arguments; Profiles 2--5 have the literal hole assignments in Section 4.

Thus the first exact cyclic-order search has only ten support-feasible
cases: six mass-four cases and four mass-five cases.  The reduction is at
the named toggle-support level, stronger than the centre character but
weaker than equality of cyclic owner decks.

Moreover a twelve-label ground is support-infeasible in every case.  Thus
thirteen is the minimum reduced-ground size at which a five-by-five atom
can pass even the binary support equations.

## 1. Point and hole equations

Let `a_z,b_z` be the positive-minus-negative counts of period-10 and
period-11 rails centred at `z`.  Let `t_z` be the signed number of
noncentre toggle supports containing `z`.  For target indicator `h_z`,

\[
             10a_z+11b_z+4t_z=h_z.                 \tag{1.1}
\]

Five physical rails per shore imply `|t_z|<=5`.  Since the positive owner
total exceeds the negative owner total by one and both shores contain five
rails,

\[
                   \sum_z a_z=-1,\qquad \sum_zb_z=1. \tag{1.2}
\]

On a ground of size thirteen, a period-10 support has two holes among the
twelve noncentre labels, and a period-11 support has one.  Write `P_z,N_z`
for the positive and negative hole multiplicities at `z`.  Comparing the
five positive and five negative rail slots gives the exact hole equation

\[
                P_z-N_z=-(a_z+b_z)-t_z.             \tag{1.3}
\]

Support feasibility is therefore a finite bipartite degree problem with
row sums one or two, forbidden centre diagonals, and the column differences
in `(1.3)`.

## 2. Net centre mass four

The q4 supporting-plane theorem forces one of the following two target
profiles at mass four:

```text
Profile I:   2*(-1,1,0), 1*(1,1,-5), 2*(0,-1,3)
Profile II:  1*(-1,1,0), 3*(0,-1,3), 1*(0,3,-8).
```

The triples are `(a,b,t)`.  Five physical rails still give `|t|<=5`, so
Profile II is impossible.  Profile I uses four net rails per shore; the
fifth positive and fifth negative rails form one cancelling pair in a
common centre/period class.

Call the three target types in Profile I `A=(-1,1,0)`,
`B=(1,1,-5)`, and `C=(0,-1,3)`.  The cancelling pair cannot be centred at
`B`: three positive rails are then centred at `B`, while one negative rail
is centred there, so at most two positive and four negative noncentre
supports can contain `B`.  Hence `t_B>=-4`, contradicting `t_B=-5`.

Up to the symmetry within the two A labels and the two C labels, the only
remaining cancellation centres are A, C, and an exterior label.  For each
of periods 10 and 11, Section 4 supplies an exact support solution for all
three types.  This leaves six mass-four cases.

## 3. Net centre mass five

At net mass five there is no aggregate centre/period cancellation, so

\[
                  \sum_z(|a_z|+|b_z|)=10.           \tag{3.1}
\]

Every target has `|a|+|b|>=1`, since `(1.1)` is impossible at a target
when `a=b=0`.  Because the total norm in `(3.1)` is ten, a target state
in a global profile has norm at most six, while a nonzero exterior state
has norm at most five.  The target states of norm at most five and the
nonzero exterior states of norm at most five are

```text
target h=1:
 T1=(-3, 1, 5)   T2=(-2, 3,-3)   T3=(-1, 1, 0)
 T4=( 0,-1, 3)   T5=( 1, 1,-5)   T6=( 2,-1,-2)

exterior h=0, excluding zero:
 E1=(-3, 2, 2)   E2=(-2, 0, 5)   E3=(-1, 2,-3)
 E4=( 1,-2, 3)   E5=( 2, 0,-5)   E6=( 3,-2,-2).
```

Indeed `(1.1)` first forces `2a+3b=h mod 4`; the displayed norm and
support bounds then leave exactly the finite states above.  There is one
additional target state of norm six,

```text
 T7=(3,-3,1).
```

It cannot occur globally: its norm six forces each of the other four
targets to have the unique norm-one state `T4=(0,-1,3)`, with no exterior
state.  The resulting sums are `sum a=3` and `sum b=-7`, contradicting
`(1.2)`.  Thus `T1,...,T6` and `E1,...,E6` are the complete states that
can occur in a mass-five global profile.  Notice that five rails per shore
does not by itself imply the false local bound `|a|+|b|<=5`: opposite-sign
short/long centre counts can have larger norm.  The global mass argument
above is what excludes them.

Solving `(1.2)` and `(3.1)` over five target slots and any number of
nonzero exterior slots gives exactly six multisets:

| profile | target states | exterior states |
|---:|---|---|
| 1 | `T1,T4,T4,T5,T5` | none |
| 2 | `T2,T4,T4,T4,T5` | none |
| 3 | `T3,T3,T3,T4,T4` | `E5` |
| 4 | `T3,T3,T3,T4,T6` | none |
| 5 | `T3,T4,T4,T4,T5` | `E3` |
| 6 | `T3,T4,T4,T5,T5` | `E2` |

This table is exhaustive: every nonzero exterior state has norm at least
two, so `(3.1)` bounds the number of exterior slots by five; direct
substitution into the three sum equations leaves precisely the six rows.

### Proposition 3.1 (Profiles 1 and 6 fail on V13)

Profile 1 contains `T1=(-3,1,5)`.  Three negative short rails and one
positive long rail are centred there.  Only four positive noncentre rails
remain, so `t<=4`, contrary to `t=5`.

For Profile 6, the exterior `E2=(-2,0,5)` forces all three negative rails
not centred there to use that label as a hole.  Each of the two `T5`
labels has hole difference `P_z-N_z=3` by `(1.3)`; hence every one of the
three positive rails not centred at that `T5` must have a hole there.
The unique positive long rail centred at `T3` is noncentred at both `T5`
labels, so it would need both as holes.  A period-11 support on V13 has
only one hole, a contradiction.

Profiles 2--5 are support-feasible by the explicit assignments below.

### Proposition 3.2 (the twelve-label ground is impossible)

On twelve labels, period-10 rails have one hole and period-11 rails have
none.  In the mass-four branch, Profile I requires hole difference `+3`
at `B`, while there are at most two positive short rails even when the
cancelling pair is short.  Thus every mass-four case fails.

For mass-five Profiles 1 and 6, the preceding support arguments already
apply.  Profile 2 needs total positive hole difference `2+3=5` at its
`T2,T5` columns but has only one positive short rail.  Profile 3 needs
positive hole difference `3` at `E5` but has only two positive short
rails.  In Profile 4, both positive short rails are centred at its `T6`
column, yet that column requires hole difference `+1`; no positive rail
capable of making a hole there remains.  In Profile 5, the sole positive
short rail is centred at its `T5` column, which requires hole difference
`+3`.  Hence all six mass-five profiles fail as well.

This proves the reduced-ground lower bound `|V|>=13` without cyclic-order
considerations.

## 4. Literal V13 support certificates

Labels `0,...,4` are target labels and exterior centres, when present, use
label `5`.  An entry `rail:xy` lists the one or two holes of that rail.
All omitted labels other than the centre lie in its toggle support.

```text
mass5 Profile 2
 n10c0_1:1,3 n10c0_2:1,12 n11c1:2 n11c2:3 n11c3:2
 p10c4:0,12 p11c0_1:4 p11c0_2:4 p11c0_3:4 p11c4:0

mass5 Profile 3
 n10c0:1,7 n10c1:3,9 n10c2:4,10 n11c3:4 n11c4:3
 p10c5_1:7,9 p10c5_2:1,10 p11c0:5 p11c1:5 p11c2:5

mass5 Profile 4
 n10c0:3,5 n10c1:0,3 n10c2:1,3 n11c3:0 n11c4:3
 p10c4_1:0,1 p10c4_2:0,5 p11c0:3 p11c1:4 p11c2:3

mass5 Profile 5
 n10c0:1,11 n10c5:1,2 n11c1:3 n11c2:3 n11c3:2
 p10c4:5,11 p11c0:4 p11c4:5 p11c5_1:4 p11c5_2:4
```

For the mass-four branch, the following compact ledger records one
certificate per cancellation type/period.  It is read in the same way.

```text
cancel p10 at A:
 n10A:3,11 n10A0:3,4 n10A1:3,4 n11C3:12 n11C4:0
 p10A:2,12 p10B:0,3 p11A0:2 p11A1:2 p11B:11

cancel p10 at C:
 n10A0:3,11 n10A1:3,5 n10C:4,11 n11C3:4 n11C4:0
 p10B:5,11 p10C:0,2 p11A0:2 p11A1:2 p11B:11

cancel p10 exterior:
 n10A0:3,11 n10A1:3,4 n10X:4,11 n11C3:4 n11C4:1
 p10B:4,11 p10X:1,2 p11A0:2 p11A1:2 p11B:11

cancel p11 at A:
 n10A0:3,5 n10A1:0,12 n11A:4 n11C3:4 n11C4:3
 p10B:0,5 p11A:2 p11A0:2 p11A1:2 p11B:12

cancel p11 at C:
 n10A0:3,12 n10A1:3,11 n11C:4 n11C3:4 n11C4:3
 p10B:3,11 p11A0:2 p11A1:2 p11B:12 p11C:2

cancel p11 exterior:
 n10A0:3,7 n10A1:3,11 n11C3:4 n11C4:12 n11X:4
 p10B:7,11 p11A0:2 p11A1:2 p11B:12 p11X:2
```

Substitution in `(1.3)` verifies every column, and every row has the
required one or two holes away from its centre.

## 5. Exact remaining search

For each of the ten cases, choose a cyclic order on every certified or
alternative feasible support and form the rank-five owner deck consisting
of its centre plus every cyclic four-window.  The required conditions are:

1. each shore is owner-simple;
2. the positive owner occurrence vector equals the negative vector plus
   the single target owner; and
3. every rail is a simple Johnson cycle, including its wrap edge.

These named conditions imply the point equations but are much stronger.
Failure of one displayed support does not eliminate its centre profile;
the cyclic search must range over every support solution unless it proves a
support-independent obstruction.

The H100 search source is

```text
scratch/search_q4_near_c_five_by_five_v13_atom_20260814.py
```

An independent solver-free replay enumerates the local states and six
global profiles, checks every displayed hole certificate directly, and
exhausts the V12 one-hole assignments in all fourteen centre cases:

```text
scratch/verify_q4_five_by_five_centre_profiles_v13_support_20260814.py
SHA-256 69e71dbf9258ec7f14bcd329211196ecb5c42d2c64b3a18f5f26f45d074bf439

H100 output
scratch/verify_q4_five_by_five_centre_profiles_v13_support_20260814.h100.out
SHA-256 2adccfcb84592534d9d39b1f6fde8335f065374d289b80e2d75f72e0a50bde58
```

All support enumeration and verification used to obtain this reduction was
run via SSH on H100.  The local Mac was used only for editing and Git.
