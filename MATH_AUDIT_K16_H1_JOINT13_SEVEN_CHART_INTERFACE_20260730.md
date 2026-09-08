# K16 H1 joint13: seven-chart interface and two final local cuts

Status: **GO for the decoded interface and the chart-6/chart-15 cuts,
conditional only on the named exact near-capacity mask census.**

This note is confined to the frozen arbitrary-value thirteen-cell fibre of
the authenticated H1 word.  It does not normalize a word with another edit
support into this fibre and it does not prove an unrestricted K16 no-go.

## 1. Frozen interfaces

The explicit-witness model has 55 targets, 29 charts per target, 1,790
variables and 55,852 clauses.  The hole

\[
H=\mathtt{0x2c6d}
\]

is target index 16 in the sorted 55-target ledger.  Its 29 explicit chart
variables are, without contraction,

\[
x_{465+j}\qquad(0\leq j<29).
\]

The compact proxy/supply model has 469 variables.  Its five H-code variables
are `[81,82,83,84,85]` in least-significant-bit order, and the numeric code is
the old chart index.  Direct parsing of both CNFs checks the H exactly-one row
`(465 ... 493)`, all 406 explicit H mutexes, and the compact invalid-code rows
for 29, 30 and 31.

The all-H scalar capacity theorem leaves precisely:

| chart | explicit variable | compact exclusion clause | physical interval |
|---:|---:|---|---|
| 6 | 471 | `(81,-82,-83,84,85)` | `[4486,4489]` |
| 15 | 480 | `(-81,-82,-83,-84,85)` | `[6438,6440]` |
| 20 | 485 | `(81,82,-83,84,-85)` | `[12869,12870]` |
| 21 | 486 | `(-81,82,-83,84,-85)` | `[12869,12871]` |
| 24 | 489 | `(81,82,83,-84,-85)` | `[12870,12871]` |
| 27 | 492 | `(-81,-82,83,-84,-85)` | `[12871,12872]` |
| 28 | 493 | `(81,82,-83,-84,-85)` | `[12872,12872]` |

The 1,878 ternary resolvents, 876 target-ejection implications and six meet
states from item 1970 are all conditional on `x467`, chart 2.  The all-H
capacity theorem proves `-x467`; consequently those rows are now vacuous.
Their construction is reusable, but the rows themselves are not constraints
on any of the seven surviving charts.

## 2. Exact near-capacity mask interface

For a canonical tuple in collar `b`, let `Gamma_b` be the 55-bit set of
targets having at least one valid local chart.  The existing exhaustive
closure enumerator retains every generic mask at distance at most one from
the sharp collar capacity.  Its four families are:

| collar | capacity | retained layers | distinct masks |
|---:|---:|---|---:|
| 0 | 7 | 6, 7 | 17 = 15 + 2 |
| 1 | 23 | 22, 23 | 4 = 3 + 1 |
| 2 | 14 | 13, 14 | 4 = 3 + 1 |
| 3 | 12 | 11, 12 | 114 = 105 + 9 |

The hole bit is absent from every generic mask.  Put

\[
P=\mathtt{0x4879},\qquad Q=\mathtt{0x6879}.
\]

Neither P nor Q occurs in any retained generic mask of collars 0, 1 or 2.
Exactly three retained collar-3 masks contain both; all have size 11:

| id | 55-bit mask | target labels |
|---|---|---|
| R0 | `0x2d4830001c00` | `286d,2879,287d,4879,6879,8ce6,9ce6,a86d,a87d,ac6d,bcef` |
| R1 | `0x20225e30000800` | `2879,4879,6879,8c62,8c67,8ce6,8ce7,9ce6,a879,bcef,e879` |
| R2 | `0x202f4830000800` | `2879,4879,6879,8ce6,9ce6,a86d,a879,a87d,ac6d,bcef,e879` |

The maximum generic masks used below are:

| id | collar | mask | target labels |
|---|---:|---|---|
| A0 | 0 | `0x40108140200020` | `246d,346d,766d,806d,a46d,b46d,f66d` |
| A1 | 0 | `0x5010a100000020` | `246d,806d,946d,a46d,b46d,d46d,f66d` |
| B | 1 | `0x8fdee3df` | `2265,226d,22e5,22ed,22f5,2669,266d,26ed,26fd,28c9,2af5,2c69,2cc9,2ce9,2e69,2e6d,38c9,39c9,3cc9,3ce9,3dc9,3de9,79c9` |
| C | 2 | `0x701fa100001c00` | `286d,2879,287d,806d,946d,a46d,a86d,a879,a87d,ac6d,b46d,d46d,e879,f66d` |

All statements in this section were rechecked directly from the explicit
target/chart ledger and the emitted mask families.  Completeness of the mask
families is the only nontrivial enumerative input.

## 3. Exact exclusion of chart 6

Chart 6 is the full four-cell interval of collar 1 and has need H.  If it is
selected, the OR of the four canonical cell values is both a submask and a
supermask of H, hence is exactly H.  Every subinterval OR is therefore a
submask of H.  In this collar every chart of P needs P and every chart of Q
needs Q.  Since both labels have the outside-H part `0x4010`, neither P nor Q
belongs to the conditioned collar-1 set.

The sharp capacity sum under chart 6 is

\[
7+23+14+12=56.
\]

An exact cover of 55 targets can lose at most one unit of this scalar sum.
Because P and Q are unavailable in conditioned collar 1 and in every
distance-at-most-one mask of collars 0 and 2, collar 3 must contain both.
The preceding exact ledger says its only possibilities are R0, R1 and R2,
all of size 11.  This consumes the unique slack unit.  Thus collars 0 and 2
must use a maximum mask, respectively A0/A1 and C, while conditioned collar
1 has at most 23 targets.

The six outer unions are:

| collar-0 mask | collar-3 mask | outer union mask | size | size + 23 |
|---|---|---|---:|---:|
| A0 | R0 | `0x703fe970201c20` | 22 | 45 |
| A0 | R1 | `0x703fff70201c20` | 25 | 48 |
| A0 | R2 | `0x703fe970201c20` | 22 | 45 |
| A1 | R0 | `0x703fe930001c20` | 20 | 43 |
| A1 | R1 | `0x703fff30001c20` | 23 | 46 |
| A1 | R2 | `0x703fe930001c20` | 20 | 43 |

Here each outer union already includes C.  Even the largest possible union
with conditioned collar 1 has size only 48.  This proves

\[
-x_{471},
\]

or compactly excludes code 6 by `(81,-82,-83,84,85)`.

## 4. Exact exclusion of chart 15

Chart 15 is the full three-cell interval of collar 2 and likewise forces the
full-collar OR to equal H.  P and Q cannot be served there: their collar-2
needs are respectively `0x4040` and `0x6040` on charts 13--15 and their full
labels on charts 16--18; every case requires bit `0x4000`, absent from H.

Again the sharp scalar capacity is 56.  The same P/Q argument forces collar
3 to one of R0, R1, R2 and consumes the unique slack.  Collars 0 and 1 must
therefore use A0/A1 and B.  Each of the six outer unions has size exactly 41,
so conditioned collar 2 would have to cover its exact 14-target complement:

| collar-0 | collar-3 | complement mask | required target labels |
|---|---|---|---|
| A0 | R0 | `0x3fc23600010000` | `2c6d,8c62,8c67,8ce7,946d,a879,cc61,cc63,cc67,cce7,ce61,ce63,d46d,e879` |
| A0 | R1 | `0x1fcd2000011400` | `286d,287d,2c6d,946d,a86d,a87d,ac6d,cc61,cc63,cc67,cce7,ce61,ce63,d46d` |
| A0 | R2 | `0x1fc03600011400` | `286d,287d,2c6d,8c62,8c67,8ce7,946d,cc61,cc63,cc67,cce7,ce61,ce63,d46d` |
| A1 | R0 | `0x2fc21640210000` | `2c6d,346d,766d,8c62,8c67,8ce7,a879,cc61,cc63,cc67,cce7,ce61,ce63,e879` |
| A1 | R1 | `0x0fcd0040211400` | `286d,287d,2c6d,346d,766d,a86d,a87d,ac6d,cc61,cc63,cc67,cce7,ce61,ce63` |
| A1 | R2 | `0x0fc01640211400` | `286d,287d,2c6d,346d,766d,8c62,8c67,8ce7,cc61,cc63,cc67,cce7,ce61,ce63` |

All six complements contain `T=0xcc61`.  Every collar-2 chart of T has need
exactly `0xcc61`.  But every subinterval OR under chart 15 is a submask of H,
and

\[
\mathtt{0xcc61}\setminus H=\mathtt{0xc000}\ne0.
\]

Therefore T is not available in conditioned collar 2.  This one physical-bit
blocker kills all six complements and proves

\[
-x_{480},
\]

or compactly excludes code 15 by `(-81,-82,-83,-84,85)`.

## 5. Remaining exact status

The existing exact join artifact treats the other five survivors
`20,21,24,27,28`.  Its complete emitted conditioned-family sizes are
`27,2,11,4,3`; after the scalar layer filter it checks respectively
`81,4,22,8,6` Cartesian combinations.  Their maximum union sizes are
`44,45,47,47,51`, so the corresponding candidate learned units are

\[
-x_{485},-x_{486},-x_{489},-x_{492},-x_{493}.
\]

The small Cartesian replay independently checks those emitted families.
At the time of this note, the separate independent replay of the underlying
`216^w` tuple-to-family enumeration was still active; therefore this note
does not by itself promote the five units or the resulting full-fibre UNSAT
claim.  Once that replay authenticates the family census, the five units
above together with the two units proved here exhaust the seven-chart clause;
combined with the 22 already authenticated scalar units, they prove UNSAT of
the frozen joint13 fibre only.

## 6. Frozen hashes

- explicit witness CNF: `f7c7c00592a682b994f6656ddf8f335ab272cd1517fb44a6cbd4e29061e19e47`;
- explicit witness map: `146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a`;
- compact proxy/supply CNF: `f03c8c3e38caf4d4f47bb7ae4569e07526afdd7689acc2c1b32b8dfd71ab488e`;
- compact proxy/supply map: `f5f50ec0563adb1175500ef1426144f753dd72ed37f360f787ebb840feeb5ed8`;
- all-H capacity result: `1cf38f49743dce287d3151f60b88831e9bc8cbf8d8c74802a33edb4ad5a46e54`;
- independent all-H capacity audit: `ed1215e3f908c22384b0402f021b0e4421274cc401f0054d20cc0b5f7f29d62e`;
- primary near-layer/join source: `2ce315811b6839e0629ae3356ab397a46438dc13a8ab9202b3a5cb1becd870e4`;
- primary near-layer/join result: `4b881f6399fcbb0be0374a77cc7d0318982b2b156e7fe66cb32b85d3fabae60a`;
- Cartesian family audit: `8e182b21698707f98e975e52b54e73449c090bf7492cf4d407f27337b7b24891`.

