# K16 floor 101 and the correct global compound/Graver face

Date: 2026-07-30  
Lane: L  
Status: exact solver-independent endpoint dual, independently replayed against
the raw seam binary.  No 101-cut assignment, physical carrier, compiler, or
K16 word is claimed.

## 1. Frozen scope and conclusion

Let `E` be the authenticated catalogue of 211,604 direction-coherent seams
on the 12,870 transition ports of the frozen length-eight K16 factor.  Let
`D` be its fixed bank of 93 zero-baseline additive defects: 45 lower-q2 and
48 upper-q3 targets.  For a seam `e:u->v`, let

```text
H(e) subset D
```

be the set of defects supplied by that seam's isolated signed q<=3 column.

The main theorem is

```text
every nonnegative endpoint-balanced x with Hx >= 1_D satisfies

                 sum_e x_e >= 501/5 = 100.2.             (1.1)
```

Consequently every integral balanced selection satisfying all 93 additive
service rows uses at least

```text
                           101 seams.                      (1.2)
```

This strictly supersedes the frozen cycle-packing floor 98.  It also means
that complete additive repairs of support 98, 99, or 100 do not exist; there
is no count-98 tightness witness to seek in this catalogue.

The quantifier `additive service rows` is essential.  A nearby compound
window can in principle create a physical target which belongs to no
individual `H(e)`.  Such nonseparated chronology, the combined `WIDTH45`
classification, seams outside `E`, and other source factors are not covered.

## 2. The two exact endpoint certificates

The first frozen certificate consists of positive integer target weights
`w_t`, of total weight

```text
                           sum_t w_t = 1899,               (2.1)
```

and an integer port potential `phi`.  For every seam `e:u->v`, put

```text
rho(e) = 20 + phi(v)-phi(u) - sum_{t in H(e)} w_t.         (2.2)
```

Exact replay gives `rho(e)>=0` on all 211,604 seams.

The new denominator-seven certificate consists of nonnegative integers
`A_t` and integers `P_v` satisfying

```text
sum_t A_t = 735,                                          (2.3)

sum_{t in H(e)} A_t + P_u-P_v <= 7 rho(e)                 (2.4)
```

for every seam.  Its exact census is

```text
A_t in [0,105], with 44 positive target prices,
P_v in [-266,154],
211604 inequalities checked,
34031 tight inequalities,
exact slack range [0,553].                                (2.5)
```

The floating LP which discovered `A,P` is not used as a proof of validity or
optimality.  Every displayed number is recovered as an integer numerator and
every inequality (2.4) is replayed with integer arithmetic.

## 3. One scale-140 Farkas certificate

Define

```text
beta_t := 7 w_t + A_t,
Psi_v  := 7 phi_v + P_v.                                  (3.1)
```

Multiplying (2.2) by seven and using (2.4) gives, seam by seam,

```text
sum_{t in H(e)} beta_t <= 140 + Psi_v-Psi_u.               (3.2)
```

All `beta_t` are positive integers, with

```text
min beta_t = 77,
max beta_t = 266,
sum_t beta_t = 7*1899+735 = 14028.                         (3.3)
```

### Theorem 3.1 (fractional balanced-service floor)

If `x_e>=0`, endpoint balance holds at every port, and every target has
additive service at least one, then

```text
140 sum_e x_e >= 14028.                                    (3.4)
```

#### Proof

Multiply (3.2) by `x_e` and sum over all seams.  Endpoint balance cancels

```text
sum_e x_e(Psi_{r(e)}-Psi_{l(e)})
```

exactly.  Hence

```text
140 sum_e x_e
  >= sum_t beta_t (Hx)_t
  >= sum_t beta_t
   = 14028,
```

where the second inequality uses `(Hx)_t>=1` and `beta_t>0`.  This proves
(3.4), and integrality of the seam count gives (1.2).  QED.

This is a genuine Farkas row for the fractional endpoint-balance/service
relaxation.  It uses neither q1 nor cycle integrality.  In particular, the
specific three-target certificate proving floor 98 was sound but strictly
weaker.  No optimum of the broader cycle-packing relaxation is asserted.

## 4. Independent raw-binary replay

Two conceptually different checks now exist.

The primary checker consumes the canonical catalogue parser, reconstructs
`rho`, rounds the denominator-seven arrays, and checks (2.4) on every seam.
It reports exact minimum slack zero, 34,031 tight rows, and the floor 101.

The Lane-L checker imports no project parser and invokes no optimizer.  It
parses the raw `K16SEAM1` records directly, authenticates the binary, base
certificate and discovery artifact, reconstructs both certificates, and
checks the equivalent combined inequality (3.2) on every seam.  It also
checks the 5,425-provider census, the complete slack histogram, and the
count-101 repeat bank.  A fresh capped H100 CPU replay returned

```text
PASS_INDEPENDENT_RAW_BINARY_FLOOR101
211604 seams checked
34031 tight seams
minimum combined slack 0
maximum combined slack 553
14028/140 = 501/5
integral floor 101.                                         (4.1)
```

The independent replay used one CPU, a 256 MiB address-space cap, 0.61
seconds wall time, and 29,696 KiB maximum resident memory.

## 5. The exact first possible additive face

For later work define the combined nonnegative seam slack

```text
sigma(e) = 140 + Psi(r(e))-Psi(l(e)) - beta(H(e)).          (5.1)
```

If an integral balanced selection has count `c` and service multiplicities
`mu=Hx`, endpoint telescoping gives the exact restitution identity

```text
140c - 14028
 = sum_t beta_t(mu_t-1) + sum_e sigma(e)x_e.                (5.2)
```

At the first unexcluded count `c=101`, the right side is exactly

```text
                              112.                           (5.3)
```

Since the smallest `beta_t` is 77, there can be at most one repeated target.
Exactly fifteen targets have `beta_t<=112`; their combined weights are

| combined weight | number of targets | remaining seam-slack budget |
|---:|---:|---:|
| 77 | 2 | 35 |
| 82 | 2 | 30 |
| 83 | 2 | 29 |
| 84 | 6 | 28 |
| 85 | 1 | 27 |
| 86 | 1 | 26 |
| 91 | 1 | 21 |

Thus count 101 has eight weight strata: no repeat with slack budget 112, or
one repeated target in one of the seven rows above.  Equivalently there are
sixteen target-specific affine branches: one no-repeat branch and fifteen
single-repeat branches.  No second repeat, higher multiplicity, or repeat of
any other target is possible.

The exact list of repeat-eligible targets is

```text
33337:84  33906:83  35044:91  36417:85  36935:77
37320:84  40066:77  41102:84  41872:82  47364:84
49436:82  50976:84  51235:83  58385:84  61960:86.           (5.4)
```

There are 70,207 catalogue seams of individual combined slack at most 112,
of which 34,031 are tight.  These are only necessary candidate columns: a
selected seam must also lie on a selected directed cycle, and the aggregate
slack, service, capacity and physical rows still couple all columns.

## 6. Correct circuit/Graver formulation at global scale

Let `B` be directed port incidence, `Q` the complete signed lower/upper-q1
matrix, and `H` the 93-row additive service matrix.  In one fixed count-101
branch let `r` be either zero or the unit vector of its repeated target, and
let `R=112-beta^T r`.

Every exact-q1 point in that branch satisfies

```text
Bx = 0,
Qx = 0,
Hx = 1+r,
1^T x = 101,
sigma^T x = R,                                             (6.1)
```

with `x` binary, outgoing port capacity at most one, and all required
physical conflict and chronology conditions.  The last equality is redundant
in the integer lattice because

```text
sigma = 140*1 + B^T Psi - H^T beta.                         (6.2)
```

Nevertheless it is valuable for pruning and replay.

For a branch of budget `R`, delete every seam with `sigma(e)>R` and every
remaining seam which lies on no directed cycle of that reduced graph.  On
the resulting directed multigraph choose a spanning forest of the underlying
undirected graph and let `C` be its signed fundamental-cycle matrix.  Then

```text
C : Z^d -> ker_Z B                                         (6.3)
```

is a lattice bijection.  Hence the unrestricted integer equality problem is

```text
[ Q C ] z   [ 0   ]
[ H C ] z = [ 1+r ],                                       (6.4)
[ 1^T C]    [ 101 ]
```

followed by `0<=Cz<=1`, port capacity and the physical rows.  Smith or
Hermite normal form of (6.4) gives a solver-free divisibility obstruction.
Passing that test is not a construction because it omits the binary and
conflict geometry.

The signed matrix `C` does not preserve conformal order.  Therefore one must
not map a Graver basis of the cycle-coordinate matrix through `C` and call it
the Graver basis in seam space.  Differences of two points in the same branch
lie in

```text
ker_Z [ B ; Q ; H ; 1^T ],                                 (6.5)
```

and seam-space conformal minimality must be tested there (or in an augmented
system retaining both seam and cycle coordinates).

## 7. Support-six-plus meet-in-the-middle boundary

The floor 101 makes support-six enumeration irrelevant for a **complete
additive repair**.  It does not settle a local `93 -> 92` descent or a
nonadditive compound witness.

For a six-seam packet in any declared seam universe, the complete algebraic
meet-in-the-middle key of a three-seam half `P` is

```text
kappa(P) = (B P, Q P).                                      (7.1)
```

Two internally capacity-safe halves form an exact port/q1 packet precisely
when their keys are opposite and their tail, head and physical footprints are
cross-compatible.  Every six-seam packet occurs in each of its ten unordered
`3+3` splits.  This covers all port-cycle types

```text
C6, C4+C2, C3+C3, C2+C2+C2,                               (7.2)
```

without enumerating six-cycles.  Hash equality is only an index; the full
integer key must be recomputed after every join, and residence plus every
all-depth shadow must be replayed on the completed packet.

For moves **within** a fixed count-101 branch, use the enlarged signed key

```text
kappa_101(P) = (B P, Q P, H P, 1^T P),                    (7.3)
```

because service and count must also return.  The slack coordinate is
dependent by (6.2).  A signed six-column exchange is exact exactly when two
halves have opposite (7.3), the signs agree with the current binary point,
and their union is physically feasible.

Returning here to a **nonnegative source-relative binary six-cut packet**
(not the mixed-sign same-branch exchange of the preceding paragraph), the
prior support-five theorem proves that the authenticated bank has no physical
exact packet of support one or two.  Consequently such a nonnegative exact
support-six packet is conformally decomposable only as two individually exact
three-cycles.  This shortcut is bank-scoped; it does not classify mixed-sign
six-column exchanges between count-101 points and must be re-audited after
adding omitted seams or close-collar atoms.  Even a decomposable pair must be
retained in a nonlinear all-depth search, because simultaneous chronology can
improve when neither summand does.

## 8. Proved boundary

Proved here:

1. the frozen additive endpoint-balance/service relaxation has fractional
   minimum at least `501/5` and integral cut floor 101;
2. the old count-98 face is empty, before q1 or physical constraints;
3. count 101 has the exact sixteen-branch restitution ledger above;
4. circuit/SNF and `3+3` MITM formulations give complete algebraic
   coordinates without enumerating long cycles.

Not proved:

1. existence or nonexistence of a 101-cut additive balanced assignment;
2. exact q1 or physical feasibility at count 101;
3. absence of a six-seam local strict descent;
4. any bound for a genuinely interacting witness not represented in `H`;
5. a K16 carrier, compiler, word, or global nonexistence theorem.

The correct next additive attack is a floor-102 separation on the sixteen
count-101 branches, not any count-98 search.  The correct nonseparated attack
remains literal support-six-plus MITM with exact all-depth replay.

## 9. Frozen lineage

```text
source factor
  scratch/k16_asymmetric_len8_orbit_repair_20260730.json
  SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204

binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

base scale-20 certificate
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

denominator-seven discovery vector (used only to recover candidate integer
numerators; validity comes solely from exact replay)
  scratch/k16_second_stage_cycle_dual_20260730.exploratory.json
  SHA-256 7049c20541189b2a9fd9e2f5bbf0915eaa8926f0a61b4bd6138bdbe4997ea4f5

primary exact checker version used by the fresh replay
  scratch/audit_l_k16_second_stage_cycle_dual_exact_pinned_20260730.py
  SHA-256 23c81cb301371b41b0e05e84d5834ea975ce12e6c508e06827ab877b2488a3a4

fresh primary exact replay
  scratch/k16_second_stage_cycle_dual_exact_floor101_20260730.audit.json
  SHA-256 15816ff538bfcc5005782f8eaa7395293d529bfd35ba38b0cd11a0d8467069a4
  payload SHA-256 c29aff51fda1ca5a44745102e20c100c36f9367c621d00cc3bd3f7d8635d9afd

primary H100 resource ledger
  scratch/k16_second_stage_cycle_dual_exact_floor101_20260730.resource.txt
  SHA-256 560bd9b26c48377c55e2e37e0d1764e389d7cc34c516e5b53b2afaaf65991d78

independent raw-binary checker
  scratch/audit_l_k16_second_stage_cycle_dual_raw_20260730.py
  SHA-256 a479a67abfa0bd5295a4629debbec4637d719f421c628ec8b26b1461d0bda120

independent raw-binary replay
  scratch/k16_second_stage_cycle_dual_floor101_raw_independent_20260730.audit.json
  SHA-256 12e6881a6235a82cc084a8192e839802abcc4bd0352a64280a520ee68c664178
  payload SHA-256 2b2a1b9933b939f97c33d0e6a669f96f7b86e438ffea240adcff7a2993e4b0ec

independent H100 resource ledger
  scratch/k16_second_stage_cycle_dual_floor101_raw_independent_20260730.resource.txt
  SHA-256 56d1c28e3fc308426325c05f7ce73118f614da08e4a9062a4a4eb0e835bbdcdc
```
