# `k=16`: the complete length-eight orbit repair

Date: 2026-07-30  
Status: exact finite construction and independent literal replay; no
length-`12873` word is claimed.

## 1. Source

Start from the triangle-orbit-repaired asymmetric carrier

```text
scratch/k16_asymmetric_triangle_orbit_repair_20260729.json
SHA-256 6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc
```

It is a spanning positive-resident factor of `J(16,8)`, has both q1
palettes complete, and has `45` lower-q2 and `63` arbitrary upper rank-11
holes.

## 2. Exact length-eight census

The authenticated C++/OpenMP port-permutation census enumerates the exact
q1-safe length-eight class (with the same positive-residence seam and cut
separation semantics as the earlier Python census).  It visits
`1,624,768,405` DFS nodes and proves:

```text
q1-safe, deep-safe, positive-gain length-eight cycles: 15
gain of every such cycle:                            1
```

The fifteen cycles are exactly the full `Z_15` orbit of one cycle under
rotation of coordinates `0,...,14`.  Reconstructing the transition indices
from the frozen factor verifies this directly, without trusting labels from
the enumerator.  Their `15*8=120` cut transitions are pairwise distinct.
Consequently their successor permutations commute.

For the representative transition cycle

```text
[8641,10464,7052,5569,5060,3977,3298,4012]
```

the exact signed q1 ledger is

```text
lower q1: +{15497,39957,46213} -{38037,48257,56340}
upper q1: +{56980}             -{16013}
```

The four negatively charged source targets have multiplicity two
(`38037,48257,56340` below and `16013` above), so the move leaves them
covered.  Its newly covered rank-11 mask is `48373`.  The full orbit repair
covers exactly the missing orbit with canonical representative `40623`:

```text
40623,43983,44861,48373,48478,53079,54759,55198,
56954,59307,60147,62421,62841,63978,64188
```

```text
scratch/audit_k16_asymmetric_long_port_cycles_20260730.cpp
scratch/k16_asymmetric_long_port_len8_20260730.audit.json
```

## 3. Simultaneous orbit repair

Apply all fifteen cycles.  The independent materializer checks:

1. the reported cycles form one complete rotation orbit;
2. all cuts are distinct;
3. the simultaneous successor map is a bijection;
4. every new edge is a Johnson edge;
5. the resulting components partition all `12,870` middle vertices.

The independent physical replay then audits cyclic residence, every fixed
intersection/union width, and arbitrary-width upper unions.  It returns:

```text
middle owners                                  12,870 distinct
components                                    29
minimum positive run                          4
positive-residence violations                 0
lower-q1 holes                                0
upper-q1 holes                                0
lower-q2 holes                                45
upper-q3 / arbitrary rank-11 holes            48
fixed-width upper-q4 holes                    15
arbitrary-width rank-12 holes                 0
all other arbitrary upper ranks               complete
```

Thus the objective-relevant deficit is now

\[
                         45+48=93,
\]

down from `123` in the original asymmetric factor and `108` after the
triangle orbit repair.  The fixed-q4 holes are not objective holes: every
one of those masks is still an interval union at a different width.

## 4. Artifacts

```text
scratch/materialize_k16_asymmetric_len8_orbit_repair_20260730.py
SHA-256 c636db72b5ce8ff7b7a128c1bfe8bcb4a2d344a677b3a85acd8e43e8964fdfb6

scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204

scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json
SHA-256 3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87
```

## 5. Scope

This theorem is a strict constructive descent, not a completion theorem.
The factor still has `93` objective holes and is not compiler-ready.  It
does prove that the certified absence of q1-safe repairs through length seven
is a locality barrier rather than rigidity: the first source-relative
positive circuit occurs at length eight, and symmetry turns its unit gain
into a full-orbit gain of fifteen.

The next exact step is to rerun the long-cycle census on the new factor; its
seam graph and missing-orbit ledger have changed, so source-relative no-go
certificates from the preceding factor do not transfer automatically.

## 6. Exact rerun through length nine

The parameterized C++ census was rerun from the full length-eight-orbit
factor.  Its new directed seam graph has `211604` valid seams and `5425`
provider seams.  The exact q1-safe census proves:

```text
lengths 3 through 7: no q1-safe positive cycle
length 8:            45 q1-safe cycles, all fail lower-q2/upper-q3 safety
length 9:            30 q1/lower-q2/upper-q3-safe gain-one cycles
```

The thirty length-nine cycles again form two `Z_15` orbits.  Within either
orbit, cuts conflict at relative shifts `+/-4`; between the two orbits they
conflict at shifts `0,+/-4`.  After multiplying shift indices by `4^{-1}`
modulo `15`, the compatibility graph projects to `C_15`, so its exact
independence number is seven.  A size-seven packing attains the bound and is
safe in the four-family signed ledger used by the C++ census.

However, the independent all-depth physical replay rejects this as a carrier
descent: each representative also destroys two unit-load upper-q2 masks and
one unit-load lower-q3 mask.  The maximum packing changes the full ledger to

```text
lower-q2 holes 45, upper-q2 holes 14,
lower-q3 holes 7,  upper-q3 holes 41,
```

so its seven desired gains cost twenty-one new opposite-side holes.  Thus the
full length-eight orbit factor has no all-depth-safe single repair through
port-cycle length nine.  The next census must either go to length at least ten
or include upper-q2/lower-q3 in its early signed pruning.

A second, separately written materializer replays all thirty retained
length-nine examples one by one against every fixed lower intersection and
every arbitrary-width upper union.  Each has the identical complete-objective
vector

```text
rank-11 holes  -1,
rank-10 holes  +2,
lower-q3 holes +1,
net objective  +2.
```

Thus the all-depth failure is orbitwise structural, not an unlucky choice of
the size-seven packing.

```text
scratch/k16_asymmetric_len8_source_long_port_3_9_20260730.audit.json
SHA-256 b55983f3de8816c4457fec92d713b26ebc833304e6f19cde548e7ffee95d122f

scratch/materialize_k16_asymmetric_len9_maxpacking_20260730.py
SHA-256 8bea34543cd46c510ac4d2add99e7aa5f6a2c7349cf514e75d98dcc07a8b75fd

scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.json
SHA-256 81118d55bc16a7b80ae5f95355a0d4a81cdc841dad6fe839cb16501c38b36473

scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.audit.json
SHA-256 5ea654e46119b11f2f9e451841adfd034a2e9ba1873b8addf467f1fe66e860f4

scratch/audit_k16_long_cycle_full_objective_20260730.py
SHA-256 9f6913445e6793a10b29942e8802a12972586e2e5571aa6c2aedcd682fbf9485

scratch/k16_asymmetric_len8_orbit_source_len9_full_objective_20260730.audit.json
SHA-256 ce024402a264ff994b5b6583702e7553dd9a53703fbfeed835f2c2695662af72
```

## 7. Length-ten boundary

The exact q1-pruned C++ search was extended to length ten under a 600-second
cap.  It fully exhausted 1,777 of the 5,425 canonical provider anchors
(`32.8%`), visiting `22,461,503,095` DFS nodes and classifying `2,226,907`
gainful cycles.  In that certified region there is no q1-safe cycle that also
preserves both q2/q3 sides; 44 q1-safe cycles fail the deeper local ledger.

This is **not** a length-ten no-go: 3,648 provider anchors were not searched.
The artifact records the completed anchor indices explicitly so the scope is
replayable.  Since bounded-length growth is already exponential, the next
constructive search uses the separated global port-permutation master rather
than silently promoting this partial census to a theorem.

```text
scratch/k16_asymmetric_len8_source_long_port_len10_partial_20260730.audit.json
SHA-256 988daed98a927dac853b1455f7665922af10f4dadfb2aa3b8488fe0defa99b94

scratch/k16_asymmetric_len8_source_long_port_len10_partial_20260730.resource.txt
SHA-256 a6c3eea15c494cb59eb8158d0b6999c38a912d0424b1e860824eb711887dbead
```
