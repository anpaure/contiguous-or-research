# Independent audit: exact finite-pool q4 k17 E46 mixed depth-three boundary

**Date:** 2026-08-14

**Verdict:** **PASS**.  On the frozen 223,564-pair/3,749-self snapshot,
there is no negative PPS, PSS, or SSS depth-three exchange at the audited
E46 state.  Every self replacement stays in its removed fixed-matching
group.  The least exact delta among the sixteen negativity-capable leaves
actually tested is `+2`; this is not a global minimum over all pruned
nonnegative exchanges.

## 1. Audited implementation

```text
scratch/search_q4_k17_z17_reflection_exact_mixed_three_exchange_20260814.py
sha256 3100726996aac637eb5755c09ced594eaa00914cce932ff919bb2035f3eddb31
```

The implementation uses the frozen exact mixed depth-three score and
typed menu minima.  PPS uses two distinct unselected pair indices and one
same-group self alternative.  PSS uses one unselected pair and one self
alternative from each of the two removed groups.  SSS uses one alternative
from each of three labelled removed groups.  Each face, singleton, and
prefix cut drops only nonnegative incoming overlaps.  Every final leaf
restores all missing overlaps before its sign is tested.

The PSS code grows a pair+first-self prefix rather than the self+self
prefix displayed in the abstract theorem.  This is an equally complete
instance of the same recurrence: the omitted third-group overlap is
nonnegative, its literal group minimum supplies the cut, and its two exact
prefix overlaps are restored at closure.

## 2. Exact E46 finite-snapshot result

The outgoing face partition and surviving-face counts are

```text
kind     faces   survivors   exact leaves
PPS     50,085          76             11
PSS     32,130           9              5
SSS      6,545           0              0
total   88,760          85             16.                    (2.1)
```

No exact leaf is negative.  The least tested-leaf value is the PPS move

```text
remove pairs 16092,18997; self 1674
add    pairs 204462,219234; self 1675
Delta  +2.                                                     (2.2)
```

```text
scratch/audit_q4_k17_z17_augmented205k_exact_mixed_three_20260814.h100.json
sha256 cff3a0fd8f4caac08b3953730a81911feaf76372d3e7fd4a782995bc18edfdbc

E46 source state sha256
e208ae02dfcfc596829145ae657bb36b1f8cf6afb843d31dc8d72e9ec1aeff49

223,564-pair finite instance sha256
96c1e6b46822296dc9830c88ad387d4b1c0501490fce6fd532c9c8c3953d2891
```

Although the source-state bytes equal the E46 state used by the earlier
204,462-pair four-exchange audit, the column pool is larger and its
instance hash is different.  The two finite-snapshot claims must not be
conflated.

## 3. Independent full replay

The independent audit reconstructs the source loads, recomputes all
88,760 face cuts and typed candidate menus, compares every one of the 85
reported surviving faces, and directly replays the row-load delta of all
sixteen exact leaves.

```text
scratch/audit_q4_k17_z17_finite_pool_mixed_three_exchange_e46_20260814.py
sha256 40efcfbcf34609c2612db1591017a2d596d243379f5bf8cd04f174cac5fefd47

scratch/audit_q4_k17_z17_finite_pool_mixed_three_exchange_e46_20260814.h100.out
sha256 c55c3b15f8a49ca374a4a89d693182694e4e3bf50cbd013b3191ce0e3147d51f
status PASS
```

## 4. Scope boundary

The result is complete only for PPS/PSS/SSS depth-three exchanges in this
finite 223,564-pair/3,749-self snapshot.  It does not rule out a pair-only
three-exchange unless the separate three-pair report is invoked, a column
absent from this pool, a neutral pivot followed by descent, four-or-more
configurations, changing the fixed matching, or an owner/lower-ticket
exact cover.

All computation, replay, and hashing ran on H100.
