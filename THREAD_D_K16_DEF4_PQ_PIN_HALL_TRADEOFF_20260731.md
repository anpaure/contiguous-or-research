# K16 seed0-derived deficiency-four carrier: exact P/Q pin--Hall diagnostic

**Date:** 2026-07-31  
**Lane:** D  
**Status:** historical seed0 diagnostic, superseded by an all-schedule scalar-capacity no-go; no K16 word claim

## 1. Frozen carrier and the retired three-cut branch

The diagnostic target order is

```text
scratch/k16_fourfilter_def4_reversal_targets_20260731.word
SHA-256 0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b
```

Despite the historical `fourfilter` filename, this order is derived from
seed0.  It is not descended from the genuine four-filter K15 parent
`51f57125...`, whose canonical natural K16 chronology is `0f6d64e...`.

The preceding connected three-cut repair is now retired.  Its exact order is

```text
S0 + S2 + reverse(S1) + S3,
cuts (2128,6404,6478),
scratch/k16_fourfilter_q1complete_3cut_rank10_targets_20260731.word,
SHA-256 1133c5d4c7aff3a9888125c9d34b5ac29b0463bb03d8d8fc34b9c5e745124a89.
```

The third new seam has rank ten, so the former rank-nine-only census did not
cover it.  The exact global three-hole P/Q dynamic program has maximum
selected area `25830`; even the optimistic nine omitted-start cells give

\[
 25830+9=25839<\Lambda=26332.                         \tag{1.1}
\]

It is attained at

\[
 X=(6480,6481,12872),\qquad Y=(0,1,2).
\]

Consequently no P/Q rematching of that fixed three-cut chronology can pass
the necessary scalar lower-capacity gate.  This is a fixed-order theorem,
not a K16 theorem.  The endpoint-incidence classification and its precise
scope are recorded in
`THREAD_D_K16_FOURFILTER_Q1_THREECUT_ENDPOINT_INCIDENCE_AUDIT_20260731.md`.

## 2. Maximum-area schedule of the deficiency-four carrier

For the frozen seed0-derived order, the exact maximum-area schedule is

\[
 X_0=(10457,12871,12872),\qquad Y_0=(0,1,6101).       \tag{2.1}
\]

Its selected area is `30098`; endpoint truncation gives `30104` actual lower
cells.  Every maximal envelope is nonempty and the literal middle replay has
zero failures.  The exact generalized lower Hall graph has

```text
targets                 26332
cells                   30104
incidences             357316
maximum matching        26328
deficiency                  4
canonical shore          29 / 25
```

The three isolated zero-host targets are

\[
 \mathtt{29cc},\qquad \mathtt{8000},\qquad \mathtt{898d}. \tag{2.2}
\]

The fourth unit is the nontrivial `26/25` component inside the displayed
`29/25` shore.  Thus merely installing the three isolated targets cannot by
itself prove Hall feasibility.

This target order also misses upper masks

\[
 \mathtt{a9fe},\qquad \mathtt{b8ce},\qquad \mathtt{b8cf}. \tag{2.3}
\]

Under (2.1), the exact arbitrary-width capped-envelope checker finds no legal
physical pin for any one of (2.3).  Hence this fixed schedule is already
compiler-impossible before any common-cap SAT solve.

## 3. Exact common three-pin projection over every P/Q schedule

The natural schedule-only repair asks for one common maximal-envelope word
that simultaneously realizes the three isolated lower masks (2.2).  This is
strictly stronger than three independent one-pin tests because overlapping
pin intervals share the same capped letters.

The exact event-DAG dynamic program ranges over **every** monotone three-hole,
depth-three P/Q schedule of the frozen order.  Among schedules admitting all
three pins in one common capped word, its maximum selected area is `28993`.
One maximizing schedule is

\[
 X_1=(10457,12338,12340),\qquad Y_1=(0,1,6141),       \tag{3.1}
\]

with exact pins

```text
29cc : start 12338, length 2
8000 : start  6142, length 1
898d : start 12340, length 1
```

The literal capped-envelope replay has no empty letter, no middle failure,
and realizes all three masks exactly.  The optimistic total lower capacity is

\[
 28993+9=29002,                                      \tag{3.2}
\]

so the named-pin projection has ample scalar slack.  Its audit is

```text
scratch/threadD_k16_fourfilter_def4_threepin_capacity_20260731.audit.json
file SHA-256 1469bc0bd2644b8c5f9629fdb1ad6460eb70d84fd84eea32ae006e4eead10f64
payload SHA-256 59d0388db211710cac8c4f718698522a8c2780e9563992957f9a5f6c02525a2b
reproducer scratch/audit_ad_k16_fourfilter_def4_multipin_capacity_dp_20260731.py
reproducer SHA-256 c4afd73c845e389100fcaaad5aadba35c2dde972497aa7132a553ef77ba37169
```

This PASS is a necessary projection only.  It says neither that (3.1) is the
only three-pin schedule nor that any three-pin schedule has a perfect Hall
matching.

## 4. Full Hall replay of the maximizing three-pin schedule

Rebuilding the complete generalized Hall graph for (3.1), with every
individually feasible length-at-most-three lower cell, gives

```text
targets                 26332
cells                   29002
incidences             340116
maximum matching        25988
deficiency                344
zero-host targets         308
canonical shore         637 / 293
```

All maximal envelopes remain nonempty and the middle replay remains exact.
The three upper holes (2.3) also remain.  The exact fixed-schedule certificate
is

```text
scratch/threadD_k16_fourfilter_def4_threepin_pq_hall_20260731.audit.json
file SHA-256 f3c5db0de7d1df9b10a5fed7a5a1f47b70010d97f8e3f54d755cffa99d39fb14
payload SHA-256 d3f59d8ac80f2a409c5fd81e7137a06b9141514a95a56e16f9864ea78d9ec5ff
```

Therefore the implication

\[
 \text{large scalar area + the three named pins}
 \Longrightarrow \text{lower Hall feasibility}
\]

is false, even on this one carrier.  Retiming the schedule to create the
missing singleton hosts can destroy hundreds of other host rows.

The conclusion is deliberately schedule-specific: the computation does
**not** prove that every non-maximizing three-pin schedule is Hall-deficient.

### 4.1 The sharp one-pin step and the fixed-X obstruction

The schedule-only pivot is not wholly negative.  The exact all-schedule
single-pin DP for `0x8000` changes only the third deadline hole:

\[
 X=(10457,12871,12872),\qquad Y=(0,1,6141).           \tag{4.1}
\]

It has selected area `30058`, exact cell count `30064`, and full Hall
matching

\[
 26329/26332.                                         \tag{4.2}
\]

The remaining zero hosts are exactly `0x29cc,0x898d`, and the canonical
shore is `28/25`.  Thus `0x8000` is a genuine rank-neutral schedule pin:
it improves deficiency four to deficiency three without creating a new
zero-host target.  The upper holes (2.3) are unchanged.

There is also an exact explanation for why this cheap retiming does not
finish.  If the high-Hall start-hole set

\[
 X=(10457,12871,12872)                                \tag{4.3}
\]

is fixed, then a common realization of just `0x29cc` and `0x898d` has maximum
selected area `25919`, hence optimistic capacity only

\[
 25919+9=25928<26332.                                 \tag{4.4}
\]

Adding `0x8000` lowers this further to `25879+9=25888`.  Consequently a
schedule-only repair of the remaining two zeros must move the start holes;
retiming only the deadlines cannot retain the high-Hall geometry.  The four
optimizer schedules and their exact Hall replays are frozen in

```text
scratch/k16_fourfilter_def4_host_dp_bundle_20260731.audit.json
file SHA-256 4148a7edb9126209f0a41e8d6c793fe73ca53c1de29a4f4530d1112b9b618af3
payload SHA-256 7e608f5883343250b574dcc674a1da66da1b3a44d24f58833bb5b829cd7807cd
```

## 5. Sequential q1 repair is also closed

Starting from the diagnostic order, the complete second connected two-opt census
has one q1-completing descendant, with cuts `(6098,6172)` in the census
convention and target SHA

```text
dfbc14ffc786b93b8ed2a69ed1feee32f65745a99947135a33142bbe69c55063.
```

It still has three upper holes, and its exact maximum lower capacity is only

\[
 25751<26332.                                         \tag{5.1}
\]

Thus a second sequential single reversal cannot finish this carrier.  This
does not exclude simultaneous multi-cut rethreads or a different target
order.

## 6. Superseding all-schedule scalar theorem

The later short-provider theorem supersedes every schedule-specific branch
above.  Because `0xb8ce` is an actual upper hole and every physical witness
for it has length at most seven, the exact capped-envelope event DAG can range
over every admissible P/Q schedule and every possible `b8ce` pin.  Its maximum
selected proper-prefix area is 25,745, so even the deliberately optimistic
uniform boundary credit gives

\[
 25745+9=25754<26332.                                 \tag{6.1}
\]

Thus the whole fixed target-order P/Q fibre is compiler-UNSAT before Hall or
common-cap SAT.  Sections 2--5 remain useful only as a demonstration that
large scalar area plus a few named hosts is not a valid Hall surrogate.  They
do not define a live seed0 repair branch.

The corresponding theorem is
`MATH_THEOREM_AD_K16_DEF4_B8CE_ALL_SCHEDULE_SHORTPIN_CAPACITY_NOGO_20260731.md`.
Any continuation must either rethread the target order or use a non-P/Q
architecture.  Work on the genuine four-filter lineage must begin from K15
parent SHA `51f57125...`, not from this file.
