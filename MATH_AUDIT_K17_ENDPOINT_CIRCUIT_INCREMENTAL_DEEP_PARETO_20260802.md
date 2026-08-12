# K17 endpoint-circuit incremental deep-Pareto audit

Date: 2026-08-02  
Status: exact scoped construction/audit.  A new incremental scorer gives a
complete census of the requested simple quotient `C10`--`C18` endpoint
circuits around a fixed authenticated marker58/c68b carrier.  Every connected
candidate is independently fully recounted.  The search has produced literal
carriers improving ranks 11--13 without increasing the positive residence
count.  It does not produce a resident carrier or a `k=17` word.

## 1. Exact changed-edge identity

Let `C` and `C'` be the old and new physical owner Hamilton cycles.  A
quotient circuit replaces a `Z_17`-developed set `E_old` of physical edges by
`E_new`.  Removing these edges from either cycle leaves the same path forest.

Every cyclic interval of `C` avoiding `E_old` lies in one forest path.  The
same vertex interval, possibly read in reverse, is a cyclic interval of `C'`
avoiding `E_new`, and has the same set union.  This is a union-preserving
bijection.  Hence for every upper target `S`,

```text
witnesses_C'(S)
 = witnesses_C(S)
   - old intervals crossing E_old with union S
   + new intervals crossing E_new with union S.
```

The implementation marks the changed adjacencies and enumerates, from every
start owner, only intervals which have crossed a mark.  Monotonicity of union
allows it to stop once rank exceeds 16.  It tracks exact witness
multiplicities and holes at ranks 11 through 16.

The scorer also does an independent full all-start interval recount for
**every** connected candidate and fails closed on any disagreement.  Positive
length-two/three runs are replayed literally on the changed 24,310-owner
cycle.  The supplied cumulative purely-negative blocker bank is evaluated
directly under the candidate quotient model.

Source:

```text
scratch/search_k17_c68b_endpoint_circuit_deep_incremental_20260802.cpp
SHA256 3439de1f9ed2fdf641a4f467771bc2e8b9dbfd0132f963ac4d26ae6e88d8096b
```

H100 O3 binary root:

```text
/home/amodo/or15/work/qa_k17_endpoint_deep_incremental_20260802_quotientaudit
```

## 2. Complete C10--C14 results

The complete quotient-length 5--7 census gives:

| seed | residence | old holes 11/12/13 | accepted joint moves | best length | new residence | new holes 11/12/13 |
|---|---:|---:|---:|---:|---:|---:|
| floor3502 | 3502 | 1802/425/17 | 16 | C14 | 3502 | 1751/408/17 |
| floor2958 | 2958 | 1904/408/0 | 15 | C14 | 2958 | 1853/391/0 |
| floor2754 | 2754 | 1853/357/0 | 8 | C14 | 2754 | 1785/340/0 |
| floor2703 | 2703 | 1853/374/0 | 10 | C14 | 2703 | 1819/357/0 |
| floor2618 | 2618 | 1921/408/0 | 10 | C14 | 2601 | 1887/391/0 |
| floor2584 | 2584 | 1870/425/0 | 8 | C12 | 2584 | 1836/391/0 |
| floor2567 | 2567 | 1904/425/0 | 10 | C12 | 2567 | 1853/391/0 |
| floor2482 | 2482 | 1921/408/0 | 11 | C14 | 2482 | 1853/408/0 |
| floor2397 | 2397 | 1938/408/0 | 6 | C10 | 2397 | 1887/408/0 |
| floor2312 | 2312 | 1904/408/0 | 9 | C14 | 2295 | 1836/408/0 |
| floor2278 | 2278 | 1887/408/0 | 12 | C14 | 2261 | 1819/408/0 |
| floor2210 | 2210 | 1802/374/0 | 10 | C14 | 2193 | 1785/374/0 |
| floor2193-main | 2193 | 1768/340/0 | 7 | C14 | 2176 | 1768/323/0 |
| floor2159 | 2159 | 1751/306/0 | 7 | C10 | 2142 | 1751/289/0 |
| floor2091 | 2091 | 1683/323/0 | 9 | C14 | 2074 | 1683/306/0 |
| floor2057 | 2057 | 1717/374/0 | 8 | C12 | 2040 | 1683/340/0 |
| floor2023 | 2023 | 1734/323/0 | 4 | C14 | 2023 | 1717/323/0 |
| floor1989 | 1989 | 1751/340/17 | 3 | C14 | 1989 | 1717/357/0 |

“Accepted” means:

* the quotient owner/facet equations remain exact;
* all rank-ten cap orbits remain covered;
* the physical factor is one component;
* positive short-run count does not increase;
* `(holes11,holes12,holes13)` decreases lexicographically;
* ranks 14--17 remain complete.

The floor2754 best C14 has an independently exported literal model/factor:

```text
/home/amodo/or15/work/qa_k17_endpoint_deep_incremental_20260802_quotientaudit/
  validated_floor2754_c14/model
  validated_floor2754_c14/factor.tsv
```

Literal replay gives residence `2754`, holes `1785/340/0`, and blocker score
`158` against the cumulative 474-bank.  Quotient verification, factor export,
rank-ten coverage, one-component topology, literal residence, all-width upper
coverage, model-specific blocker extraction, and the independent fail-closed
flip-gap validator all pass.

The later residence-primary floor2703 likewise has a verified equal-residence
deep C14 at `2703,1819/357/0`.  Its current 159 blocker clauses add one novel
row to the cumulative 488-bank, producing an exact 489-bank.

The residence-primary floor2618 has a stronger joint move: one C14 lowers
residence to 2601 and holes `1921/408/0 -> 1887/391/0`.  Its exact current
153 blockers add three rows to the 499-bank, producing a 502-bank.

The later floor2584 and floor2567 seeds both have verified C12 deep controls.
The former keeps residence 2584 and improves `1870/425/0 -> 1836/391/0`;
the latter keeps residence 2567 and improves `1904/425/0 -> 1853/391/0`.
The floor2584 candidate passes the complete literal replay against bank506;
the floor2567 candidate passes against bank514.  These controls show that the
deep deterioration of residence-primary descent is not locally forced, but
neither move improves residence itself.

The later descent exposes a stronger joint sequence.  Complete C10--C14
censuses on floors 2482, 2397, 2312 and 2278 remain nonempty.  In particular,
the floor2312 C14 gives `2295,1836/408/0`, and the floor2278 C14 improves this
again to `2261,1819/408/0`.  The latter passes quotient, cap, physical
one-cycle, literal residence, exact all-width upper, model-specific blocker,
and independent fail-closed flip-gap replay.  Its 133 current blockers are
all already present in the canonical 526-bank, whose SHA is
`44b873d2e5d09f5df1e2d93548c1cd7217a17c369bc80006ab301323fd077989`.
The lexicographically lowest floor2278 point is `2278,1802/425/0`; the chosen
`2261,1819/408/0` control is the stronger joint Pareto point because it does
not pay a rank-twelve regression.

The authenticated main descent later produced strict dominators at floors
2210, 2193, 2159 and 2091.  Exact rebased circuit censuses remained nonempty
at every step.  Their most useful separate controls are:

```text
floor2210: lex 2210,1751/374/0; joint 2193,1785/374/0
floor2193: lex 2193,1717/340/0; joint 2176,1768/323/0
floor2159: lex 2159,1717/289/0; joint 2142,1751/289/0
floor2091: lex 2091,1649/323/0; joint 2074,1683/306/0
```

The floor2091 seed itself is currently the strongest simultaneous main-line
checkpoint (`2091,1683/323/0`).  The joint floor2074 factor passes the full
literal replay and adds three new sound blocker rows, giving the cumulative
554-bank with SHA
`b71c8c0b12700a28e058b9d17ef07f959495057aeae7868020d31dae66291771`.
None of these points is resident or compiler-complete.

The next residence branch reached 2057 and then 2023.  Its exact C12 control
is `2040,1683/340/0`; its C10--C14 neighbourhood at floor2023 contains only
four accepted moves and no residence reduction.  A later residence-primary
factor reached 1989 while reopening one rank-thirteen orbit.  The exact C14
scorer repairs that orbit and yields a clean `1989,1717/357/0` factor.  This
strictly dominates the older floor2057 clean control, but does not dominate
the deeper `2091,1683/323/0` or `2040,1683/340/0` points.  The clean floor1989
factor passes every scoped replay gate and extends the sound blocker bank to
570 rows, SHA
`4bb3344fb5e156a6bd8781392ade5ea4d4ebc33cf210061ff4931313b7703a4e`.

The subsequent exact C16 census produced a connected cap-safe factor with
residence count 1887.  Independent replay at

```text
/home/amodo/or15/work/qa_k17_c16_floor1887_independent_20260802_quotientaudit
```

passes the factor, owner/q1, literal one-component, fail-closed positive-run,
and exact deep-upper audits.  Its exact state is

```text
residence = 1887 = 1003 length-two + 884 length-three runs
deep holes rank 11/12/13 = 1717/442/34
zero-gap defects = 8041
```

The factor SHA is
`02dac5915b9daff85893bc4c6b48288048f2ac5e82749b15fbc935f634fb0bae`.
Against union582 it violates 103 blockers; its 111 exact current blockers
have eight novel clauses, extending the canonical sound bank to union590,
SHA
`ced9c4b36e5913f7c9c078595e5cd0c751272c626bac9f38ccbf549537f1b2aa`.

The complete nonduplicate C10--C14 incremental census over union590 has one
accepted joint move at each length and no further residence reduction.  Its
three Pareto outputs are

```text
C10: 1887, 1700/442/34, blocker score 110
C12: 1887, 1700/408/17, blocker score 111
C14: 1887, 1666/425/34, blocker score 109
```

No C10--C14 move repairs rank 13 completely.  The exact census audit SHA is
`57a7bc72b17a7c5b3456376f01c633f1c0edcf804ec8aa347910cd750d686e3e`.
The clean floor1955/floor1989 factors and the deeper floor2091/floor2040
controls remain necessary Pareto controls.

A further authenticated C14 move then reaches a new clean residence minimum:

```text
residence = 1819 = 969 length-two + 850 length-three runs
deep holes rank 11/12/13 = 1717/476/0
zero-gap defects = 7990
```

The independent root is
`/home/amodo/or15/work/qa_k17_c14_floor1819_independent_20260802_quotientaudit`
and the factor SHA is
`03df8fee975817414402399284d20ad7c52058ea8b5c6b8f9bf5f653ef1768b1`.
Its 107 current blockers add four new rows to union590, producing union594,
SHA
`533adc1eb56d02a7249596c3b97966e58c52011e43dc6f69f28cbaceb0ed4b98`.

The complete C10--C14 follow-up has zero, one, and two accepted joint moves,
respectively, and again no residence reduction.  The best clean deep control
is a C14 at `1819,1683/459/0`; it is independently applied and replayed at

```text
/home/amodo/or15/work/qa_k17_endpoint_deep_incremental_20260802_quotientaudit/validated_floor1819_c14_deep1683_bank594
```

with factor SHA
`01beba9d08fee74f99c66c2ddace5fbc10c69612b9a560c2f751b5ba7e0be763`.
It exposes no new residence blocker.  The complete census audit SHA is
`fed28ae589e09164a25f3dbf81f15570baa9667a1a2881c9611daa3fbb7d8332`.

The sequential residence branch has since reached 1751.  Independent replay
at

```text
/home/amodo/or15/work/qa_k17_floor1751_independent_20260802_quotientaudit
```

gives

```text
residence = 1751 = 918 length-two + 833 length-three runs
deep holes rank 11/12/13 = 1734/493/17
zero-gap defects = 8024
```

The factor SHA is
`a386d9dec73a0525cb949e77304fc34f2ef7748a824865c2510c28068cbbdb6a`.
It violates 102 rows of union594 and exposes one new sound blocker, giving
union595 SHA
`8535045b2f99506b9c36150e0e53d10de3072293de4ff0845d508158e312644b`.
This is the residence minimum, but it is not rank-thirteen clean and does not
dominate the clean floor1819 controls.

## 3. C16/C18 partial results

Completed C16 censuses already give:

| seed | accepted C16 | best residence | best holes 11/12/13 |
|---|---:|---:|---:|
| floor3502 | 33 | 3468 | 1717/408/0 |
| floor2958 | 25 | 2941 | 1836/408/0 |
| floor2754 | 18 | 2737 | 1785/374/0 |

The complete floor2958 C18 census has 46 accepted circuits and best deep key
`1819/408/0` at unchanged residence 2958.  The floor3502 C18 census has 71
accepted circuits and best deep key `1717/459/17` at unchanged residence
3502.  These are additional Pareto points; they do not dominate the C14/C16
points in every coordinate.

The complete floor2754 C18 census has 30 accepted circuits.  Its best deep
key is `1785/357/0` at unchanged residence 2754 and blocker score 157.  The
C14 point is strictly better in the requested deep lexicographic objective
(`1785/340/0`), while the C18 has one fewer blocker-bank violation.

The complete floor2703 C18 census has 27 accepted circuits.  Its best deep
key is `1802/391/0` at unchanged residence 2703 and blocker score 156.  The
floor2703 C14 control remains better balanced at `1819/357/0`.

## 4. Nonflat deadline-particle diagnostic

The authenticated evaluator
`scratch/evaluate_v_k17_physical_phi_g2_20260802.cpp` was run with protected
reference comparison.  Results are:

| carrier | short runs | maximum G2 | best Phi |
|---|---:|---:|---:|
| floor3502 | 3502 | 92 | 48436 |
| floor3009 | 3009 | 87 | 48446 |
| floor2992 | 2992 | 87 | 48446 |
| floor2975 | 2975 | 94 | 48432 |
| floor2958 | 2958 | 87 | 48446 |
| floor2907 | 2907 | 79 | 48462 |
| floor2754 | 2754 | 74 | 48472 |
| floor2754 + deep C14 | 2754 | 74 | 48472 |
| floor2618 | 2618 | 92 | 48436 |
| floor2618 + joint deep C14 | 2601 | 88 | 48444 |
| floor2584 + deep C12 | 2584 | 96 | 48428 |
| floor2567 | 2567 | 88 | 48444 |
| floor2567 + deep C12 | 2567 | 96 | 48428 |
| floor2482 | 2482 | 134 | 48352 |
| floor2397 | 2397 | 93 | 48434 |
| floor2312 | 2312 | 98 | 48424 |
| floor2312 + joint deep C14 | 2295 | 98 | 48424 |
| floor2278 | 2278 | 104 | 48412 |
| floor2278 + joint deep C14 | 2261 | 104 | 48412 |
| floor2210 | 2210 | 102 | 48416 |
| floor2210 + joint deep C14 | 2193 | 83 | 48454 |
| floor2193-main | 2193 | 86 | 48448 |
| floor2159 | 2159 | 86 | 48448 |
| floor2159 + joint deep C10 | 2142 | 66 | 48488 |
| floor2091 | 2091 | 82 | 48456 |
| floor2091 + joint deep C14 | 2074 | 82 | 48456 |
| floor2057 | 2057 | 82 | 48456 |
| floor2057 + joint deep C12 | 2040 | 82 | 48456 |
| floor2023 | 2023 | 83 | 48454 |
| floor1989 | 1989 | 102 | 48416 |
| floor1989 + rank13-clean C14 | 1989 | 102 | 48416 |
| floor1887 | 1887 | 126 | 48368 |
| floor1819 | 1819 | 134 | 48352 |
| floor1819 + clean deep C14 | 1819 | 127 | 48366 |
| floor1751 | 1751 | 134 | 48352 |

For every row the global optimum is at forward cut 0, and the best q1-safe,
unprotected-wrap optimum is at forward cut 2.  Here the exact identity is

```text
Phi = 2W - 2 G2.
```

The nonflat scalar gate requires `Phi<=7401`, equivalently `G2>=20610`.
Observed `G2` is only 74--134.  Thus the long-circuit residence descent is
primarily reducing a distributed defect count; it remains nowhere near
clustering defects into the 7,401-cell nonflat budget.  The floor2618 C14
improves both residence and deep holes but changes `G2:92->88` and
`Phi:48436->48444`, proving that even the joint local objective is not a
proxy for deadline-particle clustering.  The newer floor2482 is a real but
small countertrend (`G2=134`): descent can improve clustering, just not at a
rate remotely sufficient for the formal gate (`G2>=20610`).

Frozen evaluator root:

```text
/home/amodo/or15/work/qa_k17_phi_g2_latest_20260802_quotientaudit
```

## 5. Scope

The positive result is a local Pareto theorem for simple equivariant
one-endpoint-retaining circuits in the enumerated length ranges.  It excludes
multi-circuit packets, non-equivariant physical circuits, linear openings,
the source factor, deep lower/compiler matching, and global infeasibility.
No listed carrier is resident: thousands of length-two/three positive runs
remain.
