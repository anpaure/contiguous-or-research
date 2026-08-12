# Thread D: seven-run service atoms versus the carrier3 Hall witness

Date: 2026-07-30

Status: exact fixed-witness comparison.  The corrected 81,600-row state2
seven-run census contains no exact carrier.  Its previously omitted
root-3 split `w=6387` has at most one *gross* new neighbour of the fixed
carrier3 Hall shore, and that neighbour comes from the remotely relocated
`5335->5970` service rather than either new split-middle seam.  The exact
local A/G/R package has gross gain two.  Neither local fact is a legal
carrier3 rethread, and neither closes the fixed deficiency 22.

The K16 bracket remains

```text
12873 <= nu(16) <= 12874.
```

## 1. Frozen objects

The corrected source catalogue is

```text
scratch/threadD_k16_state2_sevenrun_2f59b19f_h100/output/q1_survivors.tsv
SHA-256 07f99de266e9377faf559a9a7699e9ef8093a38862e056af1d299f77076d5bd8,
4944 literal q1/G0 descriptors.
```

It is the surviving part of the exact 81,600-row census proved in
`THREAD_D_K16_STATE2_SEVENRUN_TWO_REBUILT_SERVICE_CARRIER_NOGO_20260730.md`.
The relevant final counts are

```text
81600 raw -> 66132 canonical -> 4944 q1/G0
          -> 1436 scalar-capable -> 904 full-upper
          -> 0 exact capacity-plus-envelope carriers.
```

The comparison chronology is carrier3,

```text
scratch/threadD_k16_carrier3_sevenrun_compare_20260730/carrier_3.targets
SHA-256 6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0,
pattern 4, cuts 5725/6388/12826,
flats 5769/12869/12871,
31512 proper-prefix cells.
```

Its exact lower-host graph has 26,332 left targets and 31,512 right cells.
The maximum matching has size 26,310.  Its frozen canonical Hall witness is

```text
|U| = 519,    |N_C(U)| = 497,    deficiency = 22.
```

The witness contains 19 rank-five, 113 rank-six and 387 rank-seven masks.
Its audit is

```text
scratch/threadD_k16_carrier3_sevenrun_compare_20260730/carrier_3.hall.audit.json
SHA-256 56a89bd61470a5a670fc19b0e9bc71374adbcdd6666f55f29308707fd53ded0a.
```

## 2. The positional Hall test

For a proper-prefix slot `J=(s,l)`, let `E_p` be its exact local maximal
envelopes, put

```text
allow(J) = OR_{p in J} E_p,
```

and let `must(J)` be the set of bits for which some required middle
incidence has its whole available carrier inside `J`.  A lower target `T`
is individually realizable at this right vertex exactly when

```text
must(J) subseteq T subseteq allow(J),
T intersect E_p != empty for every p in J.                 (2.1)
```

This gives the exact fixed-shore degree

```text
D_U(J) = {T in U : T satisfies (2.1)}.                     (2.2)
```

### Lemma 2.1 (positional gain criterion)

A replacement profile at slot `J` adds a right neighbour to the fixed Hall
shore only if `J` is not already in `N_C(U)` and `D_U(J)` is nonempty.  A
signature novel elsewhere but installed at an old neighbour does not add a
right vertex; conversely, an old signature at a new slot can add one.

In particular, the intersection of the two middle states at a seam is only
a weak native-token screen.  It does not determine `allow`, `must`, the
nonempty-cell conditions, or the delivery phase, so it is not itself a Hall
neighbour certificate.

More precisely, extend the cell indicator by zero at slots absent under a
given deadline schedule and define

```text
Delta_U(C',C) = sum_J (1[J in N_C'(U)] - 1[J in N_C(U)]). (2.3)
```

For the fixed shore the displayed Hall deficiency becomes
`22-Delta_U(C',C)`.  This is why additions and losses must both be counted,
and why a newly created length-three slot is a real positional addition.

## 3. Complete seam screen

The 4,944 persisted rows have exactly 29,664 directed output joins.  They
collapse to 293 directed source-seam types and 117 distinct intersection
labels.  Only one of those labels belongs to `U`, namely `0x4879`.  It
occurs 1,340 times through twelve directed seam types:

```text
6387->12826, 12826->6387,
6387->4243,  12826->4243, 1209->4243,
4243->6387,  4243->12826,
6387->5336,  5336->12826, 12826->5336,
5336->6435,  6435->5336.
```

This inventory identifies where a lower service can possibly be rebuilt,
but Lemma 2.1 is the required exact test.  In particular the frozen repair
intersections

```text
5627 <-> 6388 : 0x4659,
6388 <-> 12827: 0x4639,
5335 -> 5970 : 0x4963
```

are outside `U`; `U` also contains no submask of any of these three masks.

The positional profile scan is deliberately broader than that intersection
screen but consumes only the persisted 4,944 rows; it does not regenerate a
root.  It finds nine `U`-adjacent local profile signatures on ten directed
atoms.  The two strongest descriptors have gross addition three, both in
root 1 with split `w=1209`; none of those profiles belongs to a frozen root
service atom, and no enclosing descriptor passes the final carrier gate.
Thus these are exact local routing columns, not legal right vertices of a
new Hall graph.

## 4. The omitted `w=6387` split-middle topology

The corrected census adds exactly 960 root-3 descriptors with `w=6387`.
Exactly 96 survive q1/G0.  Every one contains the literal chain

```text
5335 -> 5970,    12827 -> 6388 -> 5627.                 (4.1)
```

The two new split-middle services in (4.1), `12827->6388` and
`6388->5627`, add no fixed-shore neighbour in their complete local collars.
Their intersections are `0x4639` and `0x4659`; the three-state common
intersection is `0x4619`.

The complete collar replay gives a sharper statement.  Forty-eight of the
96 rows have gross positional addition one, and the other forty-eight have
no addition.  Every positive row gains its sole neighbour through the remote
`5335->5970` service.  The four mutually alternative positive slots are

| rows | slot | `allow` | `must` | sole target in `U` |
|---:|---:|---:|---:|---:|
| 24 | `(5339,1)` | `0x404b` | `0x0008` | `0x404b` |
| 8 | `(5630,1)` | `0x404b` | `0x0008` | `0x404b` |
| 8 | `(6018,1)` | `0x494b` | `0x0108` | `0x414b` |
| 8 | `(5727,1)` | `0x494b` | `0x0108` | `0x414b` |

Carrier3 has a non-neighbour cell at each of those same slots.  The complete
three-service-collar current, however, must also debit destroyed old
neighbours.  Its exact `(add,loss,net)` histogram is

```text
40*(0,0,0) + 24*(1,0,+1) + 24*(1,1,0) + 8*(0,1,-1).     (4.2)
```

The 24 offsetting losses occur at `(5340,3)`; the eight negative rows lose
the old neighbour at `(12065,1)`.  Hence the maximum complete-collar net
gain is exactly one, changing `497` to at most `498` and leaving
fixed-witness deficiency at least 21.  This is not a legal
transplant: all 96 complete rows have at least one upper hole and all fail
the exact carrier gate.  The result therefore says that the omitted
split-middle seam itself gives zero; its whole exceptional descriptor has
only a remote one-neighbour gross potential.

## 5. Exact local A/G/R service package

The unique row retaining the old protected A/G/R phases is root 5 with
`w=5969`.  Its three exact local profiles are

| atom | slot | envelope cells | `allow` | `must` | `D_U` |
|---|---:|---|---:|---:|---|
| A | `(3279,3)` | `0x0c61,0x0471,0x4461` | `0x4c71` | `0x4830` | empty |
| G | `(5852,3)` | `0x4831,0x4c21,0x4429` | `0x4c39` | `0x4c38` | `{0x4c39}` |
| R | `(12534,2)` | `0x4871,0x4859` | `0x4879` | `0x0039` | `{0x4879}` |

The A slot is carrier3 cell 9839 with the identical profile and is already
outside `N_C(U)`; it gains nothing because `D_U` is empty.  The G length-3
slot is absent from carrier3 because carrier3 has depth two at 5852.  The R
slot is carrier3 cell 30839, whose old profile is

```text
allow=0x38b2, must=0x1812,
```

and has no `U` incidence.  Therefore an otherwise lossless simultaneous
installation of all three exact local atoms would add exactly two right
vertices, one for `0x4c39` and one for `0x4879`:

```text
|N_C(U)|: 497 -> 499,    residual fixed-witness deficiency: 20.   (5.1)
```

Equation (5.1) is a gross local-profile bound, not a chronology theorem.
The root-5 row fails exact envelope reconstruction and also misses upper
target `0x6f79`.  Moving carrier3's first flat to create the G length-3 slot
is nonlocal, and any real rethread may destroy existing neighbours.  Thus
no surviving descriptor realizes the two gains in a valid carrier.

## 6. Conclusion

The comparison gives three precise answers.

1. The corrected 81,600-row service census is closed and still has zero
   exact carriers.
2. The omitted `w=6387` split-middle chain adds no Hall neighbour itself.
   A complete exceptional descriptor can expose one remote C-service
   neighbour, never more, but every such descriptor is globally illegal.
3. Exact local G and R atoms each have one useful fixed-shore profile; A has
   none.  Even a lossless joint transplant leaves the displayed 519/497
   witness deficient by 20, and no quantified chronology performs that
   transplant.

Hence the service atlas does identify the two relevant missing-target atoms
`0x4c39` and `0x4879`, but it does not repair carrier3.  A useful next move
must be a genuinely larger, phase-changing multi-atom circulation that adds
at least 22 net positional neighbours (or changes the Hall shore) while
preserving exact envelope reconstruction and all upper targets.  Restarting
the broad sharp-root census is not justified by these data.

## 7. Audit artifacts

The independent exact local replay is

```text
scratch/threadD_k16_carrier3_sevenrun_compare_20260730/
  audit_threadD_k16_carrier3_sevenrun_service_cells_20260730.py
    SHA 20b6eda9d7a6233aee0575292b702750995b186f74e328c978af788d2f4c3fa3

  carrier3_sevenrun_service_cells.audit.json
    SHA 93934d9c9e9448b5331900f16f31ad7d8541ce17ccca16de0c6f48e82e4d24d7
    payload 4948a56688edb0e2487b7d2bc96d7740bfe47220bdc7e73b275709e0ca886fee
```

The audit consumes all 96 corrected exceptional descriptors and replays
their complete 30-cell three-service collars.  It ran in 0.95 seconds in a
local-light process and a second run was byte-identical.  It is deliberately
scoped to the fixed carrier3 witness.  It does not assert that a local
profile can be spliced into carrier3, nor that this particular Hall shore
persists after a global rethread.

The independent persisted-TSV profile engine is

```text
scratch/threadD_k16_carrier3_sevenrun_compare_20260730/
  compare_carrier3_sevenrun_service_atoms_20260730.cpp
    SHA 39624c512303f52031784b206523796e933563d78f2f83de3fecf166eb5b77fc

  comparison.audit.json
    SHA c7afe77f0153faf0abc98151b8ea39c4af295be397b42ee873ccabffd853d204

  RUN_MANIFEST.md
    SHA 0d7ae3d957d6993726b445f4e878bdd1f78a839c3940abdd469147854e131f5f
```

It used one H100 CPU under a 512 MiB address-space cap: 3.10 seconds wall,
3.08 seconds user time, 8,704 KiB maximum RSS, exit zero.
