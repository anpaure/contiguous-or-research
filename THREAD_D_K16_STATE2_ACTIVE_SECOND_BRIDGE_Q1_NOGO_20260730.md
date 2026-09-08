# Thread D: the protected state2 active second bridge is q1-impossible

Date: 2026-07-30

Status: exact scoped no-go.  A lossless solver-free superset of the complete
fixed-collar, two-extra-cut second-bridge class contains 328,835 canonical
five-run chronologies after normalization.  None covers every rank-nine
upper target.  The minimum q1 deficiency in this superset is one, attained
by seven rows.  Therefore the intended exact-phase class contains no
generalized-COMP3 input and changes neither the K16 bracket nor the verified
length-12,874 upper bound.

This theorem does not revisit the closed 27,439-row true-five-cut fibre.

## 1. Frozen chronology and directed services

Let `Q` be

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA-256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464.
```

The class preserves three occurrence-labelled services, not merely their
intersection colours:

1. `A`: the six rows `Q[3276:3282]` stay consecutive and forward at depth
   three; `Q_3278 -> Q_3279` serves `0x4c71`;
2. `G`: `Q[5723:5729]` stays consecutive and forward at depth three;
   `Q_5725 -> Q_5726` serves `0x4c39`;
3. `R_s`, for `s in {4243,5336}`: the four rows
   `Q_12825,Q_12826,Q_s,Q_(s+1)` stay consecutive and forward at depth two;
   the middle seam `Q_12826 -> Q_s` serves `0x4879`.

The outer intervals `Q[:3280]` and `Q[12827:]` remain fixed and forward.
The old CH rows do not preserve this phase-labelled `R_s` service; the
relevant one-bridge parent is BT.

## 2. Canonical active-second-bridge class

Inside `I=Q[3280:12827]`, retain the fixed source cuts `s-1` and `6388`
and choose two distinct additional cut edges `u<v`.  Exact collars give

```text
D_s = [3280,12825]
      \ {s-1,6388,3280,5723,5724,5725,5726,5727,s,12825},
|D_s| = 9536.                                           (2.1)
```

The four cuts partition `I` into five source intervals `p0,...,p4`.  Write
`p_s` for the interval beginning at `s` and `p_G` for the interval containing
the `G` collar.  An admissible signed order has

```text
p0 first and forward;
p4 immediately followed by p_s, both forward;
p_G forward.                                            (2.2)
```

Merge adjacent signed intervals whenever their origin strings form one
longer monotone source run, and give a singleton its positive orientation.
The active second-bridge topology menu consists of the rows with exactly
five maximal internal signed runs.  The intended physical class additionally
requires the literal collars to occur at the depths stated in Section 1.

### Lemma 2.1 (canonicality)

The maximal signed-origin runs uniquely recover `(s,{u,v},order,signs)`.
Consequently the topology parametrization is injective.  Every normalized
BT/CH row has at most four internal runs, so no member of the old
27,439-row census is evaluated here.

The production engine also constructs all old normalized keys explicitly.
Their count is exactly 27,439; the new stream has zero closed-key hits and
zero duplicate keys.

## 3. Lossless q1 anchor and phase reductions

The source misses the rank-nine colour

```text
H0 = 0x4e79.
```

Its complete rank-eight facet-occurrence positions in `Q` are

```text
282,3279,4173,5627,5726,6334,6388,6432,6433,12826.
```

Positions 3279 and 12826 are consumed by the forced `A` and `R_s` contexts;
5726 is internal to `G`; 282 is outside the movable interval.  The fixed
port 6388 supplies only one facet.  Hence a new `H0` seam requires at least
one optional cut in

```text
A = {4172,4173,5626,5627,6333,6334,6431,6432,6433}.      (3.1)
```

This is a necessary, lossless q1 prefilter.  It leaves

```text
9(9536-9) + C(9,2) = 85779
```

unordered pairs for each `s`, or 171,558 total.  Edge 6432 is retained in
the domain: no unsupported assumption about splitting the equal first-flat
pair is used.

There is a second solver-free reduction.  If `p_s=p_G`, the forced depth-two
`R_s` seam occurs before `G` in the same forward piece.  Delivery depth is
nonincreasing, so `G` would have depth at most two, contradicting its
required depth three.  Thus `p_s!=p_G`.  The surviving pair counts are

```text
s=4243: 29408,
s=5336: 21757,
total:  51165.                                          (3.2)
```

Contracting `(p4,p_s)` leaves six block orders and one free signed piece,
so (3.2) gives exactly 613,980 raw signed descriptors.  Singleton
normalization removes 108; maximal-run normalization removes 285,037; the
canonical necessary superset reaching the q1 ledger has

```text
191196 + 137639 = 328835                                (3.3)
```

rows for the two starts.

## 4. Exact adjacent-union ledger

For a rank-nine target `T`, let `n_Q(T)` be the number of source edges whose
endpoint union is `T`.  A canonical row removes exactly

```text
R- = {s-1,6388,u,v,12826}                               (4.1)
```

and adds the four joins between its five internal runs plus the final join
to `Q_12827`; call that set `J+`.  Thus

```text
n'(T) = n_Q(T)
        - sum[e in R-] 1[Q_e union Q_(e+1)=T]
        + sum[(i,j) in J+] 1[Q_i union Q_j=T].           (4.2)
```

### Lemma 4.1 (q1 equivalence)

A row covers every upper q1 target if and only if `n'(T)>0` for every
rank-nine `T`.

Indeed, a rank-nine target is the union of a nontrivial consecutive middle
interval precisely when it is the union of an adjacent distinct pair in
that interval.  Reversing an intact source interval preserves all internal
undirected unions, so (4.2) accounts for every change.  It suffices to test
the two source holes and colours touched by (4.1) or `J+`; all other positive
source multiplicities are unchanged.

The split edge `s-1` also removes the unique source occurrence of
`0x58f9` for `s=4243`, or `0x497b` for `s=5336`.  Equation (4.2), rather than
a hole-only proxy, includes those and every unique-provider debt created by
`u` or `v`.

## 5. Exact result

### Theorem 5.1 (protected active-second-bridge no-go)

No exact-phase chronology in the class of Sections 1--3 is q1-complete.

#### Proof

Lemma 2.1 exhausts the canonical topology menu without duplicates.  The
anchor in (3.1) and phase condition (3.2) are necessary, so every intended
exact-phase row lies among the 328,835 retained rows; no claim that all
328,835 pass the remaining phase equalities is needed.  Applying the exact
identity (4.2) to this lossless superset gives the deficiency histogram

```text
deficiency 1:      7
deficiency 2:  27274
deficiency 3: 117471
deficiency 4: 174619
deficiency 5:   9464.                                   (5.1)
```

In particular the q1-complete count is zero.  Since q1 completeness is
necessary for arbitrary upper coverage, no row can reach the subsequent
G0/envelope/capacity/static-host/COMP3 gates.  \(\square\)

The seven deficiency-one rows of the necessary superset are exactly

```text
s     u     v     order       reversed piece   sole hole
4243  5626  6432  0,4,1,3,2   none             0x58f9
4243  5627  6387  0,2,4,1,3   none             0x58f9
4243  5627  6432  0,4,1,3,2   3                0x58f9
5336  5626  5969  0,3,2,4,1   none             0xc679
5336  5626  6432  0,4,1,3,2   none             0x497b
5336  5627  6387  0,2,4,1,3   none             0x497b
5336  5627  6432  0,4,1,3,2   3                0x497b.   (5.2)
```

Thus six rows repair both inherited holes but leave precisely the unique
split-start colour `J_s`; the exceptional `s=5336` row repairs `J_s` and
leaves only inherited `0xc679`.  The exact extraction certificate records
all five removed edge colours with source multiplicities and all five added
seam endpoint masks/unions.  This shows the obstruction is sharp in the
q1 topology superset, not a coarse side-count failure.  It does not assert
that all seven rows pass the deferred exact phase equalities.

A third implementation reconstructs each of the seven full 12,873-row
origin permutations without importing either enumerator.  It derives the
effective removed and added edges from the source-position map and recomputes
all `C(16,9)` adjacent-union counts.  Each full replay has exactly the sole
hole displayed in (5.2).

A continuation must either add another genuinely active run/bridge or
rebuild one protected collar/service occurrence.  Merely restoring a
conceptual cut collapses back to a normalized lower-run topology and is not
a new case.

## 6. Independent replay and resources

The production C++ engine and a structurally separate Python auditor agree
on every count in (2.1)--(5.1).  The Python audit independently rebuilds
the origin runs, singleton normalization, exact removed/added edge ledger,
and the full deficiency histogram.  Both use (3.2) only as a necessary
phase filter; since the broader stream already has no q1 survivor, later
exact phase replay is logically unnecessary.

The production H100 run used one CPU, 0.58 seconds wall, 0.47 seconds user,
and 42,496 KiB maximum RSS.  Exit one is the engine's documented exact
no-candidate status, not UNKNOWN.  The independent run used one CPU,
11.41 seconds wall and 21,504 KiB maximum RSS; it exited zero with audit
status `PASS_EXACT_SECOND_BRIDGE_Q1_AUDIT`.

Frozen artifacts:

```text
scratch/threadD_k16_state2_secondbridge_sixcut_20260730.cpp
  SHA 03c9d498cf5e4ca7835de7f29d0092761fe89bc959dbfc66020b7db5121e3213

scratch/threadD_k16_state2_secondbridge_sixcut_20260730/result.json
  SHA 27a4c2a88f5d0107849a58a1dc899e1177cbf87726ee4165b423032af68a2c34

scratch/audit_threadD_k16_state2_secondbridge_sixcut_q1_20260730.py
  SHA 62cb9c6f8d4d6c060e690a65e54117b0bd94cc098223fb70b76348ff412a3b9d

scratch/threadD_k16_state2_secondbridge_sixcut_20260730/independent_q1.audit.json
  SHA 5b44ea5881d8d045c86cb90cc66453a24e6ae7f69ccbb8fba6cfd8aa63746cce
  payload e1fdc723c9f3f7dc6522603742ad99a392a67e27dc48745d3b1c32603428cfc4

scratch/extract_threadD_k16_state2_secondbridge_def1_20260730.py
  SHA 6bfe0a86fbd19ee3d8d4383514a500d7466b2e89af13f6b698f9d23cba1b8c08

scratch/threadD_k16_state2_secondbridge_sixcut_20260730/def1.final.audit.json
  SHA fca25ab94da72f4728ee7c80ab6a631a2ce7098daefa0b76a59182c5e48c8db1
  payload 57247a0452aa22ef54a3b9e3c710a20bd036c96c512d96bdeb5a2410db315a8c

scratch/audit_threadD_k16_state2_secondbridge_def1_direct_replay_20260730.py
  SHA 113d998720c3402fcda8bf51c2d8b0c8a0ba641481eaab2aa6375ac50f0372fb

scratch/threadD_k16_state2_secondbridge_sixcut_20260730/def1.direct_replay.audit.json
  SHA 4f7b883f246ca74bdf5ec91e61ab23835d05267ec8323272a84dbbe63930084e
  payload c8b1fe71fc85fab28d994c7be01fcef127af02e8e5333b86eaf1faec70e233d0

scratch/threadD_k16_state2_secondbridge_normal_form_20260730.md
  SHA 3b9537f935a78c74ffeecacb5899038aa11cad64d649062d82e354897d6c8320
```

## 7. Scope

This theorem is complete for two optional cuts inside `Q[3280:12827]`,
fixed outer intervals, exactly five maximal internal signed runs, and the
three literal phase-labelled source services of Section 1.  It does not
cover a cut in an outer interval, a third optional internal cut, a reversed
or rebuilt `A/G` collar, or a different occurrence of one of the three
service colours.

The global exact bracket remains

```text
12873 <= nu(16) <= 12874.
```
