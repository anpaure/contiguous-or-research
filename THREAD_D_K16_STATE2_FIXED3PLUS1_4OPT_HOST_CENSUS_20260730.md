# Thread D: fixed-three-plus-one 4-opt host census

Date: 2026-07-30

## 1. Input and purpose

The capacity-rich upper-complete state with target SHA

```text
6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0
```

is the standard pattern-4 three-cut rethread of the frozen state-2 source at
cuts

```text
5725, 6388, 12826.
```

It has forced depth mass `31512` and zero upper holes, but its exact generalized
compiler atlas has the two zero-host lower targets

```text
0x4879, 0x4c39.
```

The source

```text
scratch/threadD_k16_state2_fixed3plus1_4opt_lower_host_census_20260730.cpp
```

defines the smallest complete standard 4-opt stratum above this row.  This
note records its exact quantifier and the reductions used in the executable.

## 2. Exact fixed-three-plus-one fibre

Keep the three cuts `5725,6388,12826`.  Choose one further cut

```text
d in {0,...,12868} \ {5725,6388,12826}.
```

After sorting the four cuts `x0<x1<x2<x3`, let

```text
S0 = Q[x0+1..x1],
S1 = Q[x1+1..x2],
S2 = Q[x2+1..x3].
```

The prefix `Q[0..x0]` and suffix `Q[x3+1..12872]` are fixed.  The three
internal segments may be put in any of `3!` orders and each may independently
be reversed.  Thus there are exactly

```text
(12869-3) * 3! * 2^3 = 617568
```

quantified representations.  This includes the known three-cut row (usually
with a redundant split of one of its unchanged segments), but also every
standard four-cut reconnection with the three distinguished cuts.  The bound
`d<12869` deliberately leaves the two terminal flat pairs in the exterior
suffix; this is not the previously rejected terminal-flat lane.

## 3. Exact rank-nine join filter

**Lemma 3.1 (oriented-segment boundary localization).**  Let a chronology be
formed by permuting and reversing fixed contiguous segments.  Every interval
wholly inside one output segment has the same union as an interval of the
source.  If a rank-nine mask `H` was absent from the source but is present in
the output, then some new adjacent boundary pair has union exactly `H`.

**Proof.**  Reversal bijects internal output intervals with source intervals
and does not change their unions.  Hence a new witness interval for `H` crosses
an output segment boundary.  Along that interval, take the adjacent pair at
the first crossed boundary.  The two distinct rank-eight endpoint rows have a
rank-nine union contained in `H`; because `H` itself has rank nine, equality
holds.  QED.

The state-2 source has precisely the upper holes `0x4e79,0xc679`.  Therefore a
four-cut representation can be upper-complete only if its four new boundary
joins contain a union `0x4e79` and a union `0xc679`.  Testing those eight
endpoint masks is an exact necessary filter, not a heuristic.  Every row that
passes it is still replayed by the unrestricted accumulated-union oracle, so
loss of an old upper witness is also detected.

## 4. Exact lower-host test

For a carrier-clean forced schedule write `P_j` for the maximal cell envelope.
For a proper-prefix cell `C=[i,i+l)`, `1<=l<=d_i`, define

```text
Allowed(C)   = OR_{j in C} P_j,
Mandatory(C) = {b : one complete middle-row carrier of b lies in C}.
```

**Lemma 4.1 (fixed-envelope host criterion).**  A lower target `S` can be
assigned to `C` if and only if

```text
S subset Allowed(C),
Mandatory(C) subset S,
P_j intersect S is nonempty for every j in C.
```

**Proof.**  Necessity follows from nonempty source cells, the cell envelopes,
and every carrier trapped inside `C`.  Conversely set
`A_j=P_j intersect S` on `C` and `A_j=P_j` outside `C`.  The cells on `C` are
nonempty and their union is exactly `S` by the first and third conditions.  A
middle-row bit in `S` retains every occurrence that lies on `C`; a middle-row
bit outside `S` retains an occurrence outside `C`, since otherwise it would
belong to `Mandatory(C)`.  Hence every middle row is still recovered exactly.
This is the standard exact candidate lemma used by the generalized compiler.
QED.

Because every delivery depth is at most three, only rows in
`[i-3,i+l-1]` can contribute to `Mandatory(C)`.  The executable first tests
this criterion for `0x4879` and `0x4c39`.  Rows passing G=0, fixed terminal
flats, exact carrier/capacity, both named hosts, and upper completeness receive
a full all-ranks-lower host census by enumerating submasks of each cell's
rank-at-most-eight allowed mask.

## 5. Exact census result

The source SHA-256 is

```text
1795fb26a4597581cc1b0d8b45bd740b9e047725ebfd0b627fb06a2089ce6af2.
```

It was compiled and run on one H100 CPU core under a 1 GiB address-space cap.
The complete ledger is:

```text
quantified representations       617568
rank-nine join-filter passes      25867
carrier/capacity passes           12876
named-lower-host passes               1
upper-complete passes                 1
full static lower-atlas passes        0
```

The sole row passing both named hosts and every upper target is

```text
extra cut       3278
sorted cuts     3278,5725,6388,12826
segment order   2,0,1
reverse bits    0
capacity        29065
flat starts     3322,12869,12871
```

It is exactly the already known rotation-3110 chronology (target SHA
`9a96c2c...3f14b`) and its full lower atlas again has the sole zero host
`0x4c71`.  Thus the fixed-three-plus-one standard 4-opt fibre contains no
static generalized-COMP3 candidate.

The remote run used 71.85 user seconds, 72.65 wall seconds, and 5,120 KiB
maximum RSS.  Its exact result is

```text
scratch/threadD_k16_state2_fixed3plus1_4opt_20260730/result.json
SHA-256 15ce5db604b1557572be862b1e1f888f039fed619b519e74222669f36bb1a677
```

An independent reconstruction checks every ledger partition, rebuilds the
sole surviving chronology from its four cuts, and re-enumerates its 361,816
lower-host incidences:

```text
scratch/threadD_k16_state2_fixed3plus1_4opt_20260730/independent.audit.json
SHA-256 b9e849998c58ca71bca6f6f08e8ad63adcdeb807333b096019aa2bf8a887725e
```

## 6. Scope

Consequently:

* a zero-host-free row is only past the static necessary gate; the common
  integral generalized-COMP3 assignment must still be solved and literally
  replayed;
* a no-pass census closes only this fixed-three-plus-one standard 4-opt fibre;
  it does not close a movable original cut, a terminal-flat cut, a five-cut
  rethread, or a nonstandard duplicated segment operation.
