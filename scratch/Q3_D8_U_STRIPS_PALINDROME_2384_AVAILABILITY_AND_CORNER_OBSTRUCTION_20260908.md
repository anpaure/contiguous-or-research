# Pure obstructions to the 2384 two-plane endpoint gate

2026-09-08. One authorized h100 process stopped at its necessary
availability screen after 0.103648 seconds. No LP or CP ran. Root
then supplied the pure corner proof below; direct_route and
ternary_lift independently audited it and found no correction.

The availability failure first identified an incorrect choice of
critical orbit omitted by the short bank. Section 4 derives the
corrected condition, which was not executed. The later independent
projection argument in Section 5 excludes the entire stated
charge-2384 two-plane construction, including that correction.
Its lower bound is 2408. No additional optimization is warranted
for this construction.

## 1. The actual endpoint construction and the tested restriction

Use 168 physical rows with both four-coordinate shore chains
cropped to ranks 1,...,7. The base charge is 2352. The short bank
uses whole translation/complement bundles from the 5208 copied
and 1176 admissible affine diamond catalogues.

Select one generic U16 bundle on H=0123 with v=4. Up to affine
normalization, the two relative orientations have literal words

    C=01023231, D=00132321,
    C=01023321, D=00132231.

Restore the C zero endpoint in the eight original translates and
the corresponding C top endpoint in the eight complemented rows.
This costs 16. Since D starts 00, these strips cover all bottom
axes and top coaxes. Their rank-seven contribution is precisely
the E_H orbit, and their rank-five witness contribution is W_H.

Also select an old copied palindrome P4 on a different direction
plane K. Restore both endpoints on both shores of its four rows,
at cost 16. This repairs both global corners. Its new critical
orbit is E_K and its new rank-five witness is W_K. Thus a complete
bank would have charge 2352+16+16=2384. The two repair choices
must upgrade short bundles actually selected in the bank.

The executed test imposed exact short coverage of every one of
the 126 critical translation orbits other than E_H, and prohibited
short coverage of E_H. It allowed all 144 normalized palindromic
P4 choices with K distinct from H. This particular restriction,
not the endpoint restoration itself, is impossible.

## 2. The pure obstruction

Consider the rank-eight corner

    x_H = 2 * 1_H = (2,2,2,2,0,0,0,0).

The U endpoint strips have ranks 1,...,7 and 9,...,15, so they
contain no rank-eight point. A full copied palindrome has an
all-opening first half. Its only shore states with every entry
in {0,2} are the two endpoints. Consequently its only whole-row
pure corners are 0, 2*1_K, 2*1_(K complement), and 2*1_E.
None is x_H when the direction planes K and H differ.

Therefore some short row must cover x_H. In any saturated
four-plus-four row cropped to ranks 1,...,7, the two shore states
at x_H have even ranks from {2,4,6}. Decrease the last increment
on either shore. The resulting predecessor remains in the
cropped chain and changes one coordinate of H from 2 to 1.
It is a rank-seven target of the E_H translation orbit.

Thus any short bank covering x_H necessarily covers E_H. This
contradicts the executed restriction. The proof applies to
arbitrary saturated cropped four-plus-four rows, without copied
partners, affine shore restrictions, or catalogue assumptions.

## 3. Independent finite availability certificate

The source read the two already saved catalogues; it did not
enumerate a new row family. It checked that their target indices
agree. Excluding E_H reduced 6384 short bundles to 6264.

For each normalized U, let F be its twelve critical target
orbits. Any exact critical completion may use only that U and
short bundles whose critical sets avoid F. The availability test
took the union of every such short bundle, every P upgrade whose
underlying short bundle is compatible, and the chosen U strips.
This enlarges every possible completion, since it selects all
compatible rows and all compatible P upgrades simultaneously.

| Normalized U | Filtered short ID | Compatible shorts | Compatible P upgrades | Missing target IDs |
| --- | ---: | ---: | ---: | --- |
| 01023231 / 00132321 | 5623 | 3979 | 124 | 19, 26, 182 |
| 01023321 / 00132231 | 5622 | 3979 | 124 | 19, 26, 182 |

The missing representatives, decoded in coordinate order 0,...,7
with code sum x_i*3^i, are:

| Target ID | Code | Literal target | Rank | Translation orbit size |
| ---: | ---: | --- | ---: | ---: |
| 19 | 26 | (2,2,2,0,0,0,0,0) | 6 | 8 |
| 26 | 80 | (2,2,2,2,0,0,0,0) | 8 | 2 |
| 182 | 242 | (2,2,2,2,2,0,0,0) | 10 | 8 |

The rank-eight entry is exactly the universal corner obstruction.
The rank-six and rank-ten entries are additional finite-family
availability failures and are complements up to translation.

Artifacts:

- `q3_d8_u_strips_palindrome_2384_attempt_20260908.py`
- `Q3_D8_U_STRIPS_PALINDROME_2384_SUMMARY_20260908.jsonl`
- `Q3_D8_U_STRIPS_PALINDROME_2384_CERTIFICATE_20260908.json`
- `Q3_D8_U_STRIPS_PALINDROME_2384_MISSING_TARGETS_20260908.json`

The source received complete independent static audits from root
and direct_route before execution. Both checked the actual endpoint
set differences, links to selected shorts, shared LP/CP constraints,
and the literal 6561-point replay prepared for any future witness.
The LP/CP branch and witness replay were not reached in this run.
The subsequent representative read only decoded three saved
target entries on h100; it did not enumerate or optimize anything.

## 4. The necessary corrected critical equations

The corner argument forces short coverage of E_H. Every critical
orbit other than E_H and E_K also requires short coverage, because
the endpoints supply neither. Therefore all 126 orbits other than
E_K require short coverage. The 168 short rows have exactly
168*6=1008 critical point occurrences, equal to the total size of
those 126 orbits. Hence the short bank must cover all of them
exactly once and must avoid E_K completely.

This is necessary for the entire stated two-plane endpoint
construction, not an optional further restriction. Its unique
repeated final critical orbit is E_H, supplied once by the shorts
and once by the U strips. It also precludes intrinsically
critical-colliding short bundles.

For palindrome selector p_P, the unexecuted corrected joint
equations would be

    short_critical_load(t) + sum_{P: E_K(P)=t} p_P = 1

for every critical target orbit t. Use all 6384 admissible short
bundles before these equations, rather than filtering out E_H.
Keep the selected-U/P links, all 891 literal target constraints,
physical short-row count 168, and the proved witness cuts.

This model change was recorded only. No new process, LP, CP,
enumeration, or solver restart was run. The next pure obstruction
also rules out this corrected gate. No full cover or improved
asymptotic coefficient is claimed.

## 5. Projection waste rules out the entire stated construction

Root supplied the following stronger argument after the terminated
availability read. Direct_route and ternary_lift independently
audited all orbit sizes, complement identities, and charges: PASS.
This section uses no computation or catalogue premise.

Recall the nonnegative projection weight

    y(x) = (1/4) * #{i : sum_{j != i} x_j = 7},
    sum_x y(x)=2358.

Its charge on any balanced four-plus-four chain pair is at most
the actual row charge. Indeed, for a coordinate i on the first
shore and a fixed first-shore state, the equation in the definition
of y fixes the rank of the second-shore state, so there is at most
one such state in its chain. Summing over the four coordinates on
each shore gives at most the sum of the two chain lengths.
Consequently every balanced cover has charge at least 2358 plus
its weighted excess target loads. At rank eight, y(x) is n1(x)/4.

Write the generic outer-ab diamond on H={a,b,c,d}, with the other
shore H+v and h=a+b=c+d. Its two words have identical odd states

    C1=D1=e_a,
    C3=D3=2e_a+e_b,
    C5=D5=2e_a+e_b+e_c+e_d,
    C7=D7=2*1_H-e_b.

Both relative cd orientations have these same states. The U16
bundle consists of eight translated original rows and their eight
distinct complemented rows.

For the outer central cells (1,7) and (7,1), take

    Q17 = e_a + 2*1_(H+v) - e_(b+v).

The two cells are translates by v. This target has three zeros,
so its translation orbit is free: an invariant zero set under a
nonzero F_2 translation would have even cardinality. Global
complementation of Q17 is translation by h+v. Therefore all four
outer central cells, two from each constituent orbit, lie in one
eight-point target orbit. Each target has load four from U alone.
There are two ones, so their excess projection charge is

    8*(4-1)*(1/2)=12.

For the inner central cells (3,5) and (5,3), take

    Q35 = 2e_a+e_b + 2e_(a+v)+e_(b+v)+e_(c+v)+e_(d+v).

Again the two cells are translates by v. The zero pair is {c,d},
with difference h, and the two-valued pair is {a,a+v}, with
difference v. Since h differs from v, a translation stabilizing
both pairs must be zero. Thus this orbit also has eight points.
It differs from its complemented orbit: translation preserves
pair differences, whereas complementation exchanges the zero
pair difference h and the two pair difference v.

Each of these two distinct inner target orbits has load two from
U. Its points have four ones and hence y=1. They contribute

    8*(2-1) + 8*(2-1)=16

of excess projection charge. These inner orbits differ from the
outer one by their number of ones. Thus every balanced cover
retaining the U16 short cells has charge at least

    2358+12+16=2386.                                  (1)

The selected copied palindrome P4 contains all ones in each of
its four physical rows. That target has y=2, so its excess charge
is at least (4-1)*2=6. It is distinct from all three U target
orbits above. Retaining both bundles therefore gives

    charge >=2358+28+6=2392.                          (2)

Finally, the actual endpoint construction forces short coverage
of x_H by Section 2. An immediate predecessor lies in E_H. An
immediate successor also remains in the cropped row: its even
shore rank is at most six. This successor lies in the complemented
rank-nine E_H orbit. Translation closure of the short bank gives
all eight points in each orbit. The U endpoint strips supply each
orbit again, so both have load at least two.

The rank-seven E_H points have four zeros and y=1; their rank-nine
complements have four twos and y=1. These two orbits are disjoint
from all preceding rank-eight targets, and add excess charge 16.
Hence every balanced cover satisfying the stated two-plane endpoint
construction has

    charge >=2358+28+6+16=2408 >2384.                 (3)

This closes the construction itself, without depending on the
incorrect E_H exclusion or the finite candidate pool. It assumes
the full U16 bundle, the selected palindrome P4, the stated U
endpoint strips and P full upgrade, K distinct from H, and a
translation-closed saturated short bank. It does not give a global
lower bound of 2408 for arbitrary chain-pair covers.
