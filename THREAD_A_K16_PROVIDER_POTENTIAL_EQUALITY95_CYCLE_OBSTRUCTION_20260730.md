# K16 provider-potential equality theorem: balanced floor 96

Date: 2026-07-30  
Status: proved, solver-independent finite certificate in the frozen
source-relative `q<=3`/upper-width-four seam catalogue.  No 96-cut carrier,
compiler, or K16 word is claimed.

## 1. Scope and notation

The source is

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

and the authenticated seam catalogue is

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

It contains 12,870 transition ports and 211,604 nonold,
direction-coherent, positive-collar-safe seams.  The defect bank `D` consists
of the 45 old lower-`q2` holes and the 48 old upper-`q3` holes.  Thus
`|D|=93`.

For a seam `a`, let `l(a)` and `r(a)` be its left and right transition
ports.  Let `H(a)` be the set of defects supplied by its isolated signed
`q<=3` column.  A seam is a **provider** if `H(a)` is nonempty and a
**nonprovider** otherwise.  There are 5,425 providers: 5,232 singleton and
193 double providers.

A balanced port assignment has the same selected left and right port sets,
with capacity one on each shore.  Hence its selected seams, oriented
`l(a)->r(a)`, form a vertex-disjoint union of directed cycles.

Everything below concerns this balanced, additive, frozen catalogue.  It is
not a theorem about the older combined `WIDTH45` classification, close
interacting seams, unrestricted rethreads, a different source carrier, or an
open-boundary assignment.

## 2. General weighted port-potential theorem

### Theorem 2.1

Let `w:D->Z_{>0}`, let `K` be a positive integer, and let
`phi` be an integer potential on the transition ports satisfying

```text
0 <= phi <= K
```

and, for every provider seam `a`,

```text
w(H(a)) <= K + phi(r(a)) - phi(l(a)).                 (2.1)
```

Then every balanced selected seam set which services all defects has at
least

```text
ceil(sum_{d in D} w(d) / K)
```

seams.

#### Proof

For a selected provider define

```text
sigma(a) = K + phi(r(a)) - phi(l(a)) - w(H(a)) >= 0,
```

and for a selected nonprovider define

```text
kappa(a) = K + phi(r(a)) - phi(l(a)) >= 0.
```

The second inequality follows from `0<=phi<=K`.  If `P` and `Z` are the
selected provider and nonprovider sets, balance gives

```text
sum_{a in P union Z} (phi(r(a))-phi(l(a))) = 0.
```

Consequently

```text
sum_{a in P} w(H(a))
  = K(|P|+|Z|) - sum_{a in P} sigma(a) - sum_{a in Z} kappa(a)
  <= K(|P|+|Z|).                                      (2.2)
```

Every defect is supplied at least once and all weights are positive, so the
left side is at least `sum_D w`.  Division by `K` and integer rounding prove
the claim.  QED.

This cycle proof is equivalent to deleting the nonproviders and telescoping
over provider paths, but (2.2) retains the exact equality slack needed below.

### Corollary 2.2 (provider-path form)

If a directed provider pseudoforest covers `D`, has `p` provider arcs and
`t` nonempty path components (with any number of provider cycles), then

```text
p+t >= ceil(sum_D w / K).                              (2.3)
```

Indeed, the potential cancels on each provider cycle and contributes at most
`K` on each provider path.  Thus the total supplied weight is at most
`K(p+t)`.  This form does not assume that endpoint connectors exist.

## 3. The authenticated scale-20 certificate

The 93 target numerators are constant on seven phase blocks:

| block size | numerator |
|---:|---:|
| 15 | 11 |
| 15 | 22 |
| 15 | 36 |
| 15 | 19 |
| 15 | 18 |
| 15 | 16 |
| 3 | 23 |

Thus

```text
sum_D w = 15(11+22+36+19+18+16)+3(23) = 1899.        (3.1)
```

The frozen certificate gives an integer `phi` on all 12,870 ports with
range `[0,20]`.  Independent raw-catalogue replay verifies (2.1), with
`K=20`, on all 5,425 providers.  The provider-slack census begins

```text
slack 0: 1388 arcs
slack 1:  760 arcs
```

and has no negative value.  Theorem 2.1 therefore gives

```text
number of selected seams >= ceil(1899/20) = 95.       (3.2)
```

This already couples provider service and the physical price of threading
providers into balanced port cycles.  It strictly supersedes the independent
`56+17=73` edge-cover/path-mask floor.

## 4. Equality at 95 is impossible

### Lemma 4.1 (unit equality budget)

Suppose a balanced servicing assignment has exactly 95 seams.  Then every
defect is supplied by exactly one selected provider and

```text
sum_{a in P} sigma(a) + sum_{a in Z} kappa(a) = 1.    (4.1)
```

#### Proof

Write

```text
R = sum_{a in P} w(H(a)) - 1899 >= 0.
```

Equation (2.2), now as an identity, gives

```text
R + sum sigma + sum kappa = 20(95)-1899 = 1.         (4.2)
```

If any target is supplied by two selected providers, then `R` is at least
the minimum target weight, which is 11.  This contradicts (4.2).  Therefore
`R=0`, and (4.1) follows.  QED.

Call a provider **unit-admissible** when `sigma<=1`, and a nonprovider
unit-admissible when `kappa<=1`.  Lemma 4.1 implies that every seam in a
95-cut candidate is unit-admissible.

### Lemma 4.2 (cycle-support obstruction)

In the complete directed graph of unit-admissible seams:

```text
all arcs                              3558
provider arcs                         2148
nonprovider arcs                      1410
nontrivial SCCs                       15
size of every nontrivial SCC           5
arcs lying in a directed cycle          90
cycle-eligible provider arcs            60
cycle-eligible nonprovider arcs          30
```

The 60 cycle-eligible provider seams jointly supply only 30 members of `D`;
63 required defects have no cycle-eligible provider.

#### Proof

The independent checker forms the complete unit-admissible graph directly
from the 211,604 frozen columns and computes its strongly connected
components by a fresh Kosaraju replay.  A non-loop arc lies on a directed
cycle if and only if its endpoints lie in the same nontrivial SCC.  A
self-loop is retained separately; there are no omitted singleton-SCC loops.
The displayed counts and the 63-target missing list are then literal finite
replays.  QED.

### Theorem 4.3 (balanced service floor 96)

Every balanced port assignment in the frozen catalogue which services all
93 defects uses at least 96 seams.

#### Proof

Theorem 2.1 excludes counts below 95.  At count 95, Lemma 4.1 restricts every
selected seam to the unit-admissible graph.  Since a balanced assignment is a
union of directed cycles, every selected seam must be cycle-eligible there.
Lemma 4.2 says that 63 defects then have no possible provider.  Hence count
95 is impossible.  QED.

## 5. Exact boundary of this obstruction

At 96 seams, the analogue of (4.2) has budget

```text
20(96)-1899 = 21.
```

The necessary graph containing every seam of individual cost at most 21 has
201,178 arcs.  Its cycle-eligible part has 201,043 arcs and one SCC of size
12,855.  Every target has between 17 and 92 cycle-eligible providers.

Therefore the coarse individual-cost/SCC missing-provider test stops at 96.
This does not show that the full aggregate potential-budget obstruction
stops: no balanced cycle union of total cost at most 21 has been exhibited.
It is not a construction: the budget sum, port capacity, physical
reverse-edge, four-separation, q1, survivor, residence, deeper-shadow, and
compiler conditions remain untested.  Exact 96 remains open even in the
balanced service relaxation.

## 6. Consequence for the proposed 73 lift

The corrected `joint_v6` 17-mask witness partitions the 48
cycle-unserviceable targets and passes the elementary membership budget, but
it cannot be lifted to a 56-provider/17-path skeleton: Corollary 2.2 already
forces

```text
provider arcs + nonempty provider paths >= 95.
```

In particular, 56 providers require at least 39 provider paths, while 17
paths require at least 78 providers.  The earlier overlapping 17-mask witness
is even more immediately impossible: its seven repeated exceptional
memberships exceed the one-repeat budget of any 56-provider edge cover.

Thus endpoint connector matching is not the first obstruction at radius 73;
the provider chronology itself already fails.

## 7. Frozen artifacts

Original weight-potential certificate:

```text
scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56
  payload  719a76301864ad4ce54071daf32e0267b17a11ef3233e6fb96b0b09d94987966

scratch/audit_k16_provider_weight_potential_floor95_20260730.py
  SHA-256 294893b2c3bf678c4f1c67b7615e1230a0510720347df273e4a21c4d4f95fed6
```

Lane-A independent equality replay:

```text
scratch/threadA_audit_k16_provider_potential_floor95_and_equality_face_20260730.py
  SHA-256 ebff922ce388607b0b91acc8884a5d39909dd5a1686b2972ca71012717d57459

scratch/threadA_k16_provider_potential_floor96_v2_20260730.audit.json
  SHA-256 f2690358e51df3546d96ca79942b75fede07c18e7707225c4b98381b4ca00ada
  payload  b31dac838bf0f972e3aaff11ab5b6cb3d5d836c50b7a6c25a36407bacbd4e4e0

scratch/threadA_k16_provider_potential_floor96_v2_20260730.resource.txt
  SHA-256 863c9e06b6714ff1400b810bb4f94a873e121dc71532144b21c7f75542d48b0c
```

The Lane-A replay used one H100 CPU, a 2 GiB address-space cap, 3.66 seconds
wall time, 378,048 KiB maximum RSS, and no GPU.  Local work was limited to
source inspection, syntax checking, and compact certificate verification.
