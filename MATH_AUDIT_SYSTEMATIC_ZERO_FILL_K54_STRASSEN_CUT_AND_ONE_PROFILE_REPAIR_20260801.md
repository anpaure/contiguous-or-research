# Systematic age profiles: the first zero-fill Strassen cut and its one-profile repair

Date: 2026-08-01

Status: exact finite audit and proof-safe correction of the canonical
completion.  The systematic residue profiles with canonical leading-zero
completion satisfy the Strassen circulation gate for every `3 <= k <= 53`,
but fail at `k=54`.  The failure has deficiency exactly 54 and an explicit
principal down-set witness.  It does **not** refute the systematic-profile
construction: changing the completion of exactly 54 occurrences of one
four-mark profile restores an exact stationary age circulation.  This is an
age-quotient result only; it does not round one copy of every owner or solve
topology, higher decks, or the common cap.

## 1. Setup

For age depth `d`, write

```text
c=(c_0,...,c_d),  sum_i c_i=r,  c_0>=1,
P(c)=(c_0,...,c_(d-1)),  Q(c)=(c_1,...,c_d).
```

An age transition `c -> c'` is legal exactly when

```text
Q(c') <= P(c)
```

coordinatewise.  A law `pi` on age types therefore supports a stationary
circulation exactly when `Q_*pi <=_st P_*pi`.

For the systematic residue profiles, let `A_a` be the set of marked deficits
in residue row `a`.  The canonical **zero-fill** completion pads a row of
size less than `d` by leading zero deficits and then takes the unique gap
composition.  This is a natural completion, but it is not part of the
systematic-profile theorem and need not be stationary.

The interval checker computes the profile histogram without iterating over
the `W` residues: every coordinate `T_(a+jW)` is constant between the exact
breakpoints `N_t-jW`.  It then checks the complete integral Strassen coupling
by max flow on the age-type relation.

## 2. Exact range and first failure

The exact interval audit gives

```text
zero-fill PASS for every 3 <= k <= 53;
zero-fill FAIL for k=54.
```

At the first failure,

```text
k=54, r=27, d=5, h=0,
W=C(54,27)=1,946,939,425,648,112.
```

The systematic profile

```text
A_*={1,2,3,5,26}
```

occurs on the exact residue interval

```text
[245971839324433,245971839324487),
```

so it has multiplicity 54.  Since it already has all five marks, its age
type is forced:

```text
C=(1,21,2,1,1,1).
```

Indeed, the suffix deficits recovered from `C` are `1,2,3,5,26`.

Among the 27 zero-fill types there is no target `C'` with

```text
Q(C') <= P(C)=(1,21,2,1,1).
```

Thus the source shore consisting only of `C` has mass 54 and empty target
neighbourhood.  Equivalently, for the principal down-set

```text
D = {x : x <= (1,21,2,1,1)},
```

the zero-fill law has

```text
Pr(P in D)=54/W,  Pr(Q in D)=0,
```

contradicting the down-set form of `Q_*pi <=_st P_*pi`.  The exact max-flow
deficiency is 54.  This is a genuine Strassen cut, not a solver timeout.

Therefore the statement

> pad every systematic row by zero deficits and use the resulting law

is false in general.  The first audited counterexample is `k=54`.

## 3. The systematic profiles themselves survive

The obstruction disappears after changing only 54 occurrences of one
profile.  The profile

```text
A={1,2,4,7}
```

has multiplicity

```text
104,435,680,894,699.
```

Its zero-fill type is

```text
B=(20,3,2,1,1,0),
```

whose available deficits are `0,1,2,4,7`.  On exactly 54 occurrences,
replace the leading zero by the unmarked deficit 8.  The new type is

```text
D=(19,1,3,2,1,1),
```

with available deficits `1,2,4,7,8`; hence it still contains every required
mark of `A`.

The modified type law admits an exact stationary circulation.  Its new
54-unit part has the transparent five-cycle

```text
C=( 1,21,2,1,1,1)
 -> D=(19, 1,3,2,1,1)
 -> E=(19, 4,1,1,1,1)
 -> B=(20, 3,2,1,1,0)
 -> F=(21, 2,2,1,1,0)
 -> C.
```

Every displayed arrow satisfies `Q(target)<=P(source)` coordinatewise.
After subtracting 54 copies of each type on this cycle, the remaining law of
mass

```text
1,946,939,425,647,842
```

also has an exact stationary coupling.  The complete integral flow is frozen
in `scratch/systematic_k54_repair_20260801.out` and is independently replayed
by the C++ audit.

Consequently the systematic marked vector at `k=54` **does** pass the
age-composition circulation gate after a one-profile completion repair.  By
the age-quotient lift, this proves membership in the rank-symmetric
fractional marked-trace polytope at this dimension.

## 4. What the repair says analytically

The smallest zero-fill obstruction is an endpoint-supply defect, exactly as
predicted by the terminal-gap audit.  Its scale is not `W`: it is the extreme
binomial multiplicity

```text
C(54,1)=54.
```

The repair uses one unmarked suffix rank to turn a dead forced type into the
entrance of a bounded age cycle.  This is a concrete unit-descent actuator:

```text
one extreme forced block
  + one equal-size completion change
  + one bounded legal type cycle.
```

This suggests the correct all-dimensional statement is not canonical
zero-fill.  It is a bounded family of completion surgeries which routes each
extreme terminal-gap block into a stocked self-loop/cycle reservoir.  No
general theorem that such reservoirs always exist is proved here.

Later work sharpens this warning.  A parametric single-hole cycle actuator
does exist, but at `k=76` the fixed systematic profiles contain a forced type
with no compatible successor profile under *any* completion.  Thus the marked
profile assignment itself must eventually change.  See
`MATH_THEOREM_TERMINAL_GAP_ACTUATOR_AND_K76_SYSTEMATIC_OBSTRUCTION_20260801.md`.

## 5. Exact scope

Proved/audited here:

1. exact zero-fill Strassen feasibility for `3<=k<=53` under the canonical
   triangular boundary used by the systematic construction;
2. the exact `k=54` principal-down-set obstruction and deficiency 54;
3. an exact one-profile, 54-occurrence repair;
4. an exact stationary age-type circulation after that repair.

Not proved here:

* a uniform completion-repair theorem for every `k`;
* an integral one-copy owner/target selector;
* a connected rooted Euler support or Johnson chronology;
* residence after literal owner selection;
* arbitrary-width upper shadows;
* the physical lower/common-cap compiler;
* `nu(k)<=B(k)+O(1)` or `nu(k)=B(k)`.

## 6. Artifacts

```text
scratch/probe_systematic_zero_fill_strassen_20260801.cpp
d26c2b5f02c78f96594b752895654d2b1750fb5b0aad62294739c9b70c2a01a9

scratch/probe_systematic_zero_fill_strassen_interval_20260801.cpp
375f56dabf4ecd1e813dbecbab1c926902ef0d6b3b9b3f1029a2e345a965e459

scratch/audit_systematic_profile_dead_type_20260801.cpp
c4a704329bb5b047641b4e4119c15492247a1571cebf109de71e5fc3e5f447b9

scratch/systematic_zero_fill_interval_k3_k54_20260801.tsv
a8c855f2fa82e5d0233f602593824f262c9fd7119c553db4754ba66d2d1969c1

scratch/systematic_k54_repair_20260801.out
229211308b5e93c10fb1bac5e3bf6fd8c9f2dac4040347a7b113d8fc1d6f5d8c

scratch/systematic_k54_strassen_repair_20260801.audit.json
4ace008d2485999461d621f04b2785ebc3827a50e6305ff240bddca015b750f0
```
