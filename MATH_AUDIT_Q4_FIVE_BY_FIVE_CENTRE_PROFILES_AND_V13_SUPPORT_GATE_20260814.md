# Hostile audit: q4 five-by-five centre profiles and V13 support gate

**Date:** 2026-08-14
**Verdict:** PASS after one completeness repair.  The exact conclusion is
that V13 is the minimum support-level ground and has ten support-feasible
cases, not ten named-owner atoms.

## 1. Audited source

```text
MATH_REDUCTION_Q4_FIVE_BY_FIVE_CENTRE_PROFILES_AND_V13_SUPPORT_GATE_20260814.md
SHA-256 27ad58f0bdcaab7b46aedec054b24688cbcd9988b831216d4886607d1594c347
```

The source was read symbolically and both supplied and independent
solver-free replays were run over SSH on H100.  No local Mac computation
was used.

## 2. Completeness defect found and repaired

The first draft used `|a|+|b|<=5` as a local consequence of five rails on
each shore.  That implication is false when the short- and long-centre
differences have opposite signs.  In particular the target character has
the additional norm-six state `(3,-3,1)`; still larger character states
also exist locally.

The repaired proof uses the global mass instead.  Every one of the five
target labels has positive centre norm, while the total norm is ten.
Consequently a target has norm at most six and a nonzero exterior label
has norm at most five.  Enumeration in these valid ranges gives the six
displayed target states, the one extra target state

```text
(3,-3,1),
```

and the six displayed nonzero exterior states.  If the extra target state
occurs, the remaining four targets must all be the unique norm-one state
`(0,-1,3)` and no exterior state can occur.  Its aggregate is then
`(sum a,sum b)=(3,-7)`, not `(-1,1)`.  Thus it is excluded, and the six
global profiles in the theorem remain exhaustive.  The supplied verifier
now enumerates this extra state before excluding it by the global sums.

## 3. Symbolic checks

1.  The character equation `10a_z+11b_z+4t_z=h_z`, the shore equations
    `sum a=-1`, `sum b=1`, and the V13 hole equation
    `P_z-N_z=-(a_z+b_z)-t_z` have the stated signs.
2.  At net mass four, norm eight leaves exactly one common
    centre/period cancellation pair.  Profile II violates `|t|<=5`.
    Cancelling at the `T5=(1,1,-5)` target leaves at most four negative
    noncentre supports there, so that case is impossible.  The A, C, and
    exterior cancellation types for each of periods 10 and 11 are the six
    remaining cases.
3.  At net mass five, the repaired finite enumeration gives exactly the
    six displayed global centre profiles.
4.  Profile 1 fails before any cyclic-order question: at its
    `T1=(-3,1,5)` target one positive rail is centred, so at most four
    positive noncentre supports can contribute to `t=5`.
5.  In Profile 6, `E2=(-2,0,5)` forces all five positive noncentre
    supports to contain the exterior label and all three eligible negative
    supports to omit it.  Each of the two `T5` labels forces all three
    eligible positive supports to omit that label.  The unique positive
    period-11 rail centred at `T3` is eligible at both `T5` labels and
    would need two holes, whereas a period-11 row on V13 has one.  This is
    a genuine support obstruction.
6.  Every one of the four mass-five and six mass-four literal tables has
    five rails on each shore, the correct one/two-hole row size, no hole
    at its own centre, and signed point ledger `[1,1,1,1,1,0,...,0]`.
    The independent replay also checks the hole equation column by column.
7.  On V12, a period-10 rail has one hole and a period-11 rail has none.
    In the mass-four branch the `B` column requires positive-minus-negative
    hole load `+3`, but even a short cancelling pair leaves at most two
    positive short rows.  For mass-five Profiles 2--5, respectively, the
    required positive hole loads exceed the one available positive short
    row at `T2,T5`, exceed the two available rows at `E5`, occur at `T6`
    where both positive short rows are centred, and occur at `T5` where
    the sole positive short row is centred.  Profiles 1 and 6 retain their
    earlier support contradictions.  This proves all fourteen V12 centre
    cases infeasible; the supplied replay independently exhausts their
    legal one-hole assignments.

## 4. Replay provenance

Supplied solver-free verifier:

```text
scratch/verify_q4_five_by_five_centre_profiles_v13_support_20260814.py
SHA-256 69e71dbf9258ec7f14bcd329211196ecb5c42d2c64b3a18f5f26f45d074bf439

scratch/verify_q4_five_by_five_centre_profiles_v13_support_20260814.h100.out
SHA-256 2adccfcb84592534d9d39b1f6fde8335f065374d289b80e2d75f72e0a50bde58
```

Independent replay:

```text
scratch/verify_q4_five_by_five_centre_profiles_and_v13_support_20260814.py
SHA-256 7df4980c66303602b2346b933dbbd99d3095825cf5ad2dbe0be7013981ef5b30

scratch/verify_q4_five_by_five_centre_profiles_and_v13_support_20260814.out
SHA-256 08d75a9ab516f43a3b4014e2064d86300616d91800f66e33bea24a58eaef7bc9
```

The supplied replay reports seven mass-admissible target character states
before the global-sum exclusion, seven exterior states including zero,
six global mass-five profiles, four feasible and two infeasible mass-five
support profiles, six feasible mass-four support cases, and PASS.
It also reports all fourteen V12 centre cases support-infeasible.

## 5. Exact scope

This audit certifies centre-ledger classification and binary toggle-support
feasibility only.  It does not certify a cyclic order, owner simplicity,
or equality of named owner decks.  Current full-search observations
(`p10A` and `p10C` infeasible, `p10X` unknown at its time limit) are not
used in the theorem or this PASS verdict.  A fixed-support or time-limited
failure cannot eliminate a centre profile without a support-independent
argument or an exhaustive search over every feasible support.
