# Independent audit of the fixed-prefix `k=14` 242-entry append

## Verdicts

### Explicit construction and coverage: **PASS**

The certified 3,434-entry prefix
`k14_pinnable_factor_missing260.txt`, followed by the 242 entries of
`k14_append_242.txt`, is term-for-term `k14_completed_3676.txt`.  The resulting
3,676-entry nonzero word covers all 16,383 nonzero 14-bit masks.  Consequently

\[
\nu(14)\le 3676,\qquad N(14)\le 3677.
\]

This is an upper bound, not an optimality proof for the unrestricted problem.

### Fixed-prefix lower bound: **PASS**

Every suffix completing this particular 3,434-entry prefix has length at
least 241.  Thus the currently certified fixed-prefix interval is

\[
241\le q_{\min}(P)\le242.
\]

The proof does **not** assume the retracted statement that at most one missing
rank-nine witness can cross the old/new seam.  The exact old-suffix
compatibility graph permits as many as three, and the proof below handles all
three.

### Detailed `q=241` seam reduction: **PASS**, as a necessary finite reduction

The endpoint-profile table, the 27 two-crossing branches, the six
three-crossing branches, their minimal nested appended-prefix OR requirements,
and the cutoff at the first six appended-prefix states all agree with direct
enumeration.  These facts reduce a prospective exact search; they neither
construct a 241-entry suffix nor exclude one.

For literal completeness, the note does not tabulate the `x=1` target choices:
there are also 27 one-crossing start/target choices
(`18+7+1+1`).  They are implicit in the old-suffix compatibility table and do
not affect any stated count for the two- or three-crossing cases.  Therefore
the phrase "complete seam branching" should be read as the endpoint profiles
plus the implicit one-crossing cases, the 27 listed two-crossing cases, and the
six listed three-crossing cases.

## 1. Independent reconstruction of the append

The old standalone completion has 243 entries.  Its one-based entries

```text
81, 82, 152, 153, 243
```

are respectively

```text
8014, 15694, 13423, 48, 8015.
```

The independent checker deleted exactly those five entries, prepended

```text
1095 8014 15694
```

and appended `13757`.  The resulting vector is exactly
`k14_append_242.txt`, including order, and has

```text
243 - 5 + 3 + 1 = 242
```

entries.

The checker independently recomputed the prefix's coverage.  It found exactly
260 omissions: 238 masks of rank nine and 22 masks of rank ten.  It also
compared this recomputed family, mask and rank, against
`k14_missing_260.txt`.

Exhaustively enumerating the 29,403 intervals of the new append alone covers
258 of those omissions.  The residual family is exactly

```text
13423 13439
```

and both are supplied across the old/new seam.

## 2. Old suffix chain and seam witnesses

The old suffix OR values, recomputed directly from the unchanged prefix, are:

| one-based old start | suffix OR |
|---:|---:|
| 3434 | 12329 |
| 3433 | 12393 |
| 3432 | 12409 |
| 3431 | 12411 |
| 3430 | 12415 |
| 3429, 3428, 3427 | 12671 |

Every suffix beginning at or before old position 3426 has rank at least
eleven.  Direct containment against the independently regenerated omission
family gives rank-nine compatibility counts

```text
12329:18, 12393:7, 12409:1, 12411:1, 12415:0, 12671:0.
```

For both `12409` and `12411`, the sole compatible missing rank-nine target is
`12923`.  Against the eight hard rank-ten targets, the compatible lists are

```text
12329: 13439,13757
12393: 13439
12409: 13439
12411: 13439
12415: 13439
12671: none.
```

The five certificate records were parsed rather than trusted as prose.  Their
zero-based and one-based indices agree, their target ranks agree, and direct
OR recomputation gives:

| target | zero-based interval | recomputed OR |
|---:|---:|---:|
| 13423 | `[3433,3434]` | 13423 |
| 13439 | `[3431,3434]` | 13439 |
| 8015 | `[3434,3435]` | 8015 |
| 16206 | `[3435,3436]` | 16206 |
| 13757 | `[3675,3675]` | 13757 |

In particular, the first two are precisely

```text
12329 OR 1095 = 13423
12409 OR 1095 = 13439.
```

## 3. Independent proof of the fixed-prefix bound `q>=241`

Select one witness for each of the 238 missing rank-nine masks.  All selected
right endpoints are new because no target occurred in the old prefix.  They
are distinct: suffix ORs at one fixed right endpoint form an inclusion chain,
which contains at most one distinct rank-nine mask.  Thus `q>=238`; write

```text
q = 238 + t.
```

Equal-rank selected intervals are nonnested, so their left endpoints are also
distinct.  Let `x` be the number whose left endpoint is old.  The exact
compatibility graph above has maximum matching size three, hence `x<=3`.
Consequently there are exactly `t+x` new positions unused as selected
rank-nine left endpoints and `t` new positions unused as selected rank-nine
right endpoints.  These are side-specific endpoint resources.

Among the 22 missing rank-ten masks, the hard family is exactly

```text
7676 8015 13287 13439 13757 14285 15334 15346.
```

Relative to the missing rank-nine family, `15346` contains none and each of
the other seven contains exactly one.  Hence the witness for `15346` can share
neither side endpoint with a selected rank-nine witness.  A witness for one
of the other seven can share at most one side.  More specifically, if its
right endpoint is shared with its unique lower witness, then its left endpoint
must be lower-free: sharing both would give the identical physical interval,
and there is no second contained missing rank-nine target available.

The hard rank-ten right endpoints are mutually distinct.

* If `t=0`, `15346` has no available lower-free new right endpoint.
* If `t=1`, `15346` consumes that endpoint.  The other seven hard witnesses
  share their right endpoints with their lower bases, so all eight require
  lower-free left endpoints.  At most `1+x<=4` are new.  Direct matching of
  old starts to hard targets has size only two (`13439` and `13757`), giving
  at most six rather than eight.
* If `t=2`, at least six of the seven unique-base hard targets share their
  right endpoints with their bases.  Together with `15346`, seven hard
  witnesses require lower-free left endpoints.  The crude capacity is at most
  `(2+x)+2<=7`.  Equality forces `x=3` and both usable old hard targets.  But
  `13757` is compatible only with old start 3434, so 3434 must remain
  lower-free.  Excluding that start, direct matching of old starts to distinct
  missing rank-nine targets has size only two: starts 3431 and 3432 both have
  the sole target `12923`.  This contradicts `x=3`.

Therefore `t>=3` and `q>=241`.  Notice that the argument uses the exact
three-crossing capacity rather than any at-most-one assertion.

## 4. Audit of the `q=241` branch tables

For `q=241`, the three new right endpoints not selected for rank-nine targets
give the endpoint inequalities in the source note.  If `f` of the seven
unique-base hard targets use free right endpoints, then `f<=2`, and at least
`8-f` hard witnesses require lower-free left endpoints.  Comparing this with
`3+x+h`, where `h<=2` is the usable old-hard-start capacity, gives exactly:

| `x` | necessary profiles |
|---:|---|
| 1 | `f=2,h=2` |
| 2 | `f=2,h>=1` or `f=1,h=2` |
| 3 | `f=2`, or `f=1,h=1` |

For `x=3`, the three lower old starts are forced to be 3434, 3433, and one of
3431/3432.  Thus 13757 loses its only old start and `h<=1`, which excludes
the apparent `f=0,h=2` arithmetic case.

Nonnesting orders the selected right endpoints in the same order as their
left endpoints.  The first `x` selected endpoints in a 238-subset of 241 new
positions are at most 4, 5, and 6, respectively.  Thus only the first six
appended-prefix OR states can participate in the old-start rank-nine events.

Finally, let nested old suffixes `C superset C'` be assigned targets `S,S'`.
If the corresponding appended-prefix ORs are `P subseteq P'`, then

```text
S = C OR P,   S' = C' OR P'.
```

Necessity gives `S without C subseteq S'`.  Conversely, under that condition
take

```text
P  = S without C,
P' = P OR (S' without C').
```

These are nested and realize both targets, proving the criterion.  Iterating
the same construction gives the triple criterion.

Direct enumeration from the actual 238-target family reproduced all six
two-suffix counts

```text
0, 2, 9, 2, 6, 8
```

in the displayed order, totaling 27.  It also reproduced exactly the six
three-crossing branches and prefix requirements:

```text
12411: 12923,12911,13103 -> 512,518,774
12411: 12923,13163,13103 -> 512,770,774
12411: 12923,13163,15147 -> 512,770,2818
12409: 12923,12911,13103 -> 514,518,774
12409: 12923,13163,13103 -> 514,770,774
12409: 12923,13163,15147 -> 514,770,2818.
```

## 5. Independent coverage checks

The audit checker implemented both exhaustive interval enumeration and the
distinct-suffix-OR recurrence.  Their complete seen sets agree.  Separately,
the two production verifier sources were rebuilt remotely with optimized C++
and rerun from the explicit completed word.  The fresh results were:

```text
length=3676 covered=16383 required=16383
length=3676 covered=16383/16383 missing=0
```

The fresh log hashes exactly match the checked-in logs.  The independent audit
checker returned:

```text
PASS
prefix=3434 old_completion=243 append=242 completed=3676
old_missing=260 rank9=238 rank10=22 append_alone_covers=258 residual=13423,13439
old_start_matching rank9=3 rank9_without_3434=2 hard_rank10=2
q241_branches ordered_pairs=27 ordered_triples=6 max_prefix_state_index=6
full_nonzero_coverage=16383/16383 fixed_prefix_append_lower_bound=241
```

## 6. Audited hashes

The audit covers the following exact artifacts:

```text
9be5e7b8c329a56565eca9bea092adde63719b98edc383a6743f82456b7f892e  K14_CROSS_SEAM_COMPLETION_NEXT.md
4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad  k14_pinnable_factor_missing260.txt
152e7e9d951e96c0600875d674f78333b634622e4c34262f44de51053fbd64ab  k14_missing_260.txt
06f4b5a06f411a896df9d471b4e2f60d97eea537b4c81710f5e1c62117d68b19  k14_completion_best.txt
63a5f7a51e7e873db394e92cfd606c027405971598377fa96a838a9c0ac58590  k14_completion_243_witnesses.txt
d5fc5c13685ca0e2eb182de0d245e93368453d0aaeaf6e2f5cfdff219a59c83c  k14_completed_best.txt
41d7028668cde93d6f9347ae881b352dfbc3de446845324a185b21414099d8a8  k14_append_242.txt
f7e362a9248ae1aaf32036bd47904e246342fd5c7b231584d04be4d6e5b5b38d  k14_append_242_seam_certificate.txt
df86beff2854227f215a8720a7959489c689d3d3d5747e9847a2ff9fd3aeac94  k14_completed_3676.txt
49e044c4d1be8a144bec80026ac4ceef41002fe7b1c133a64dd97952ed8ceed5  k14_completed_3676_exhaustive.log
c8565cc9d1f594bcbe479cd8844535eb3dcfbe6a5d865285225c0cb34c59ea13  k14_completed_3676_suffix.log
2ef221f819cc6df5eea81aebcb194a1ff76bf0229c47333b3caa367c01df80c4  verify_or_array.cpp
7bd7892532882e31c828e750c1ec960029f0571cd11584b897240c2a051fdbaa  verify_or_suffix.cpp
7ac0da32ee40a024cbc99177bd8834562ce8537011e52ab0ef82214c8cbc733a  scratch/audit_k14_append242.cpp
```

The remotely compiled independent checker had SHA-256
`423c8c26154296258d1cdf4f3e18fdc380f09ad140b1185737e4c05c4e073248`;
its output had SHA-256
`84e6b47ad98dddce240773eefc77081e06f2a7baba107e117d6408b45bd63392`.

## Exact certified scope

This audit proves:

1. the explicit fixed prefix plus explicit 242-entry append is universal;
2. the claimed seam witnesses and old-to-new transformation are exact;
3. no suffix of length at most 240 can complete this fixed prefix; and
4. the stated necessary finite branch reduction for a possible 241-entry
   suffix is arithmetically and combinatorially correct.

It does not prove that a 241-entry suffix exists or does not exist, does not
prove that 242 is fixed-prefix optimal, and does not prove the global optimum
for `k=14`.
