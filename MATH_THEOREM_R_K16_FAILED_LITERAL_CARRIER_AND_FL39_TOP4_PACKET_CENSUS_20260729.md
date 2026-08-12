# Lane R: failed-literal carrier transport and the complete connected top-four `FL39` packet census

Date: 2026-07-29

## 1. Frozen slice and exact result

This note audits the historical `FL39` slice

```text
Q39 = scratch/k16_q1_endpoint_resume1_failedlit39_20260729.json
SHA-256 db809954e287b1468dcd75b46ba2cd2f3fde4618c427d14c377dbedd381ca1be

F39 = scratch/k16_failedlit39_fullbank_20260729.audit.json
SHA-256 da9631d4c7ce9846b1e3e96317e035fc1e7389979788a4c79ff65f699948ba56

R   = scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951.
```

The exact resident decoder is also pinned to

```text
scratch/k15_pbbs_trade_baseline.json
SHA-256 8955fc7babdfc37698f51115fad2737fb4dd09c2c3a2f387f02ac690154f460f

scratch/k16_pbbs_component_trade_27_factor_20260729.json
SHA-256 91c434654d38466790dd373d26ff4e88f115d7cab1c29f71520a99cc4b349985

scratch/k15_two_component_a_cycles_20260729.json
SHA-256 bc58e466e72c0b418aa24929d45640dcfe6ffbe567caae480939e76367533738.
```

These decode `R` to physical-edge digest
`c0b263de249c1e125dac6cdaeaa3f1f7b78274c23e170a6c0d88b7f95f39fc9c`.

Here `Q39` is a simple spanning degree-two factor of `J(16,8)` with zero
lower- or upper-`q1` holes.  Against fixed `R`, exact signed-inequality unit
propagation has

```text
red variables                    12478
blue variables                   12478
rows                              50849
short-run motifs                   2235
unhit two-choice motifs             504
probed two-choice variables          956
double-failed variables               39
components                            3 = 1030+2069+9771
residence violations               2235 = 1^133 2^906 3^1196.
```

The four requested present blue edges are

```text
e1=(42139,42201), e2=(42169,42680),
e3=(51562,57706), e4=(53434,55354).
```

Each occurs in eleven of the 39 stored two-branch proofs.  A separate
deterministic regeneration of every connected alternating packet of
replacement radius two, three, or four through at least one of these edges
gives 56 `q1`-exact packets.  A strict-token octahedral `C6` gives

\[
             (\Phi,\operatorname{Res},c):
             (39,2235,3)\longmapsto(34,2235,3).
\]

Thus this neighborhood does not have a floor at 39.  The exact move is

```text
delete (49518,51502), (51562,57706), (57646,59690)
add    (49518,51562), (51502,57646), (57706,59690).
```

The materialized factor and independent full-bank replay are

```text
scratch/k16_q1_endpoint_resume1_failedlit34_20260729.json
SHA-256 bd872b21b98a98a7cbda6b94823b39d2ba5b77dea5d21a9db2a174f6fdd96717

scratch/k16_failedlit34_fullbank_20260729.audit.json
SHA-256 51b3709fc5a93ee9afcf5f3326736e20897b6c99b236ac2dfe1823e3f7bd4986.
```

Subsequent shared work has moved beyond this historical endpoint.  This
note certifies the requested `39 -> 34` transition and its complete stated
neighborhood; it does not relabel `Q34` as the current global frontier.

## 2. The exact overlay rows

For fixed factors `R,Q`, write `a_e` for adding a red edge
`e in R\Q` and `b_e` for removing a blue edge `e in Q\R`.  The physical
overlay system used here consists of the following signed unit-coefficient
Boolean inequalities.

At every overlay-active middle vertex `v`,

\[
 \sum_{e\in R\setminus Q:e\ni v}a_e-
 \sum_{e\in Q\setminus R:e\ni v}b_e\le0,
 \qquad
 -\sum_{e\in R\setminus Q:e\ni v}a_e+
 \sum_{e\in Q\setminus R:e\ni v}b_e\le0.       \tag{2.1}
\]

For every lower or upper `q1` colour `c`, put `lambda(e)=x intersect y`
or `lambda(e)=x union y`, respectively, for `e=xy`.  If
`m_Q(c)=#{e in Q:lambda(e)=c}`, the palette row is

\[
 \sum_{e\in Q\setminus R:\lambda(e)=c}b_e-
 \sum_{e\in R\setminus Q:\lambda(e)=c}a_e
 \le m_Q(c)-1.                                  \tag{2.2}
\]

For every short positive-run occurrence with closure `C`,

\[
       -\sum_{e\in C\cap(Q\setminus R)}b_e\le-1. \tag{2.3}
\]

These are precisely the nontrivial rows in `build_constraints`.  At the
three middle vertices with no red or blue overlay incidence, the omitted
vertex-row pair is just two copies of `0<=0` and may be adjoined without
changing the system.  No rankwise or abstract replacement is being
substituted for the common physical factor.

## 3. Failed-literal certificate transport

### Theorem 3.1 (physical row-carrier transport)

Let `R,Q,Q'` be spanning degree-two factors of `J(16,8)`, with `R` fixed.
Let `B` be one recorded, causally closed branch contradiction in the overlay
system for `(R,Q)`: it contains every reason row of every base-propagation
or branch-propagation ancestor and its physical branch-assumption pivot
`e_B`.  Give each row of `B` its full physical carrier

\[
\begin{aligned}
 \operatorname{Car}(\mathrm{vertex},v)
   &=\{e:v\in e\},\\
 \operatorname{Car}(\mathrm{lower},c)
   &=\{xy:x\cap y=c\},\\
 \operatorname{Car}(\mathrm{upper},c)
   &=\{xy:x\cup y=c\},\\
 \operatorname{Car}(\mathrm{motif},C)&=C,
\end{aligned}                                      \tag{3.1}
\]

where all physical edges are Johnson edges on rank eight.  Let
`Car(B)` be the union of these carriers together with `{e_B}`.  If

\[
          (Q\mathbin\triangle Q')\cap\operatorname{Car}(B)=\varnothing,
                                                        \tag{3.2}
\]

then the same signed branch contradiction transports to the overlay system
for `(R,Q')`, after identifying variables by their physical edges and
reindexing any surviving motif row by its physical closure.

For a double-failure certificate
`P_f=(B_(f,0),B_(f,1))`, put

\[
 K_f=\{e_f\}\cup\operatorname{Car}(B_{f,0})\cup
     \operatorname{Car}(B_{f,1}),                    \tag{3.3}
\]

where `e_f` is the physical pivot edge.

If `(Q triangle Q')` misses `K_f`, both Boolean branches for the pivot
remain contradictory, and hence the full overlay for `(R,Q')` is
infeasible.

#### Proof

If (3.2) holds for a vertex row, membership in `Q` is unchanged for every
physical edge incident with that vertex.  Its red/blue variable list and
both inequalities (2.1) are therefore identical.

For a palette row, every physical provider of `c` retains its membership.
Thus its shore, coefficient, and the right-hand side `m_Q(c)-1` in (2.2)
are identical.

For a motif row, every edge in its closure remains.  The closure is a
consecutive local path.  Because `Q'` has degree two, its internal
continuation cannot change; reversing the containing component merely
reverses the same `0 1^ell 0` occurrence.  Hence (2.3) remains.

Every signed row and every named physical variable in the causally closed
implication DAG is now identical.  The numerical motif tag may differ, but
the closure-indexed inequality is the same.  Induction in the recorded
reason order forces the same values and reaches the same contradictory row.
This proves branch transport.  Applying it to values zero and one of the
pivot proves the last statement.  QED

### Corollary 3.2 (exact support transversal condition)

For the 39 stored certificates and
`Delta=Q39 triangle Q'`, define

\[
 h(\Delta)=\#\{f:\Delta\cap K_f\ne\varnothing\}.      \tag{3.4}
\]

At least `39-h(Delta)` stored double-branch certificates remain valid.
Consequently, if the rebuilt overlay system for `(R,Q')` is feasible, then
`Delta=Q39 triangle Q'` must intersect every one of the 39 carrier sets
`K_f`.

This is a certificate-survival count, **not** automatically a lower bound
on the recomputed numerical potential `Phi(Q',R)`: the candidate bank,
motif indexing, and base propagation state may change.  One surviving
double-branch certificate is nevertheless already enough to prove
infeasibility.

### Why raw literal incidence is only a targeting statistic

Let `L_f` be only the set of physical edge variables that occur as terms in
the two serialized cores.  Usually `L_f` is strictly smaller than `K_f`.
A trade can change a vertex or colour row by inserting a new provider which
was absent from the old row, without touching any old term.  Therefore a
census through high-incidence current literals is complete only for its
declared packet neighborhood.  It is not a global feasibility cut.

## 4. Exact `FL39` literal-support audit

The union of the 39 raw supports has exactly 630 physical edges:

```text
blue-remove edges 354
red-add edges      276.
```

Counting each edge at most once per double certificate gives the occurrence
histogram

\[
 1^{196},2^{165},3^{88},4^{75},5^{27},6^{65},7^8,8^1,11^5. \tag{4.1}
\]

The five multiplicity-eleven edges are the four requested present blue
edges and the red-add edge `(42141,42169)`.  Their exact data are

| edge | variable | lower/upper colour | certificates | branch split `0/1/both` |
|---|---:|---|---:|---|
| `(42139,42201)` | 21462 | `42137/42203` | 11 | `5/5/1` |
| `(42169,42680)` | 21474 | `42168/42681` | 11 | `5/5/1` |
| `(51562,57706)` | 23262 | `49514/59754` | 11 | `7/4/0` |
| `(53434,55354)` | 23599 | `53306/55482` | 11 | `6/5/0` |

The first two edges hit the same zero-based certificate-index set

```text
{2,3,7,11,16,17,19,24,32,35,38},
```

while the second two hit the same, disjoint set

```text
{1,5,6,9,10,13,25,28,29,30,37}.
```

Thus the four-edge union touches only 22 of 39 stored certificates, not 39.
For each of these four edges its full carrier incidence is also eleven: no
additional certificate contains it merely through another used vertex or
palette carrier.

The raw-support hypergraph has exact transversal number eight.  The lower
bound follows from the pairwise disjoint raw supports of zero-based
certificates

```text
0,2,4,5,8,14,18,22.
```

The matching upper bound is the explicit transversal

```text
(22716,39100), (42169,42680), (47553,59841), (51403,59593),
(53434,55354), (60232,61192), (63592,63816), (64036,65028).
```

Hence `tau_raw=8`.  This is not a lower bound of eight on arbitrary physical
packet radius, because an edge outside the raw term set can hit an expanded
row carrier.

## 5. Connected packet normal form and completeness

### Lemma 5.1 (alternating Euler normal form)

For another factor `Q'`, take the canonical symmetric-difference shores
`D=Q\Q'` and `A=Q'\Q`.  Suppose `|D|=|A|=r`, the red and blue incidence
degrees agree at every physical vertex, and `D union A` is connected.  Then
it has a closed alternating Euler tour using every edge once.

#### Proof

At every vertex pair each deleted half-edge with an added half-edge.  The
pairing decomposes the support into alternating circuits.  If there is more
than one circuit, connectedness gives two circuits sharing a vertex; swapping
their local pairings merges them.  Repeating produces one alternating Euler
tour.  QED

Starting such a tour with a distinguished named deleted edge proves
completeness of the enumerator for this canonical, connected, exact-radius
class: it alternately chooses an added non-`Q` Johnson edge and a deleted
`Q` edge, forbids edge repetition, and closes after `r` edges of each colour.
Conversely every enumerated closed support has zero incidence boundary and
gives another spanning degree-two factor.  Repeated vertices are allowed;
they are reported separately below.

### Lemma 5.2 (exact `q1` filter)

For either lower or upper colour map `lambda`, the switched factor is
`q1`-complete if and only if

\[
     m_Q(c)-m_D(c)+m_A(c)\ge1\qquad\text{for every colour }c. \tag{5.1}
\]

Thus (5.1) on both shores is the exact filter, not a proxy.  The stronger
strict-token condition is equality of the two full multiplicity counters
on both shores.

## 6. Complete connected top-four census

Both orientations are enumerated and trades are globally deduplicated by
their sorted deleted/added edge sets.  The exact counts are

| radius | per-edge raw counts | raw incidences | raw union | per-edge `q1` counts | `q1` incidences | `q1` union |
|---:|---|---:|---:|---|---:|---:|
| 2 | `8,11,7,9` | 35 | 35 | `1,0,0,2` | 3 | 3 |
| 3 | `359,398,359,393` | 1509 | 1497 | `3,2,1,2` | 8 | 8 |
| 4 | `23997,24693,23476,24459` | 96625 | 95925 | `25,1,0,20` | 46 | 45 |

There are therefore 56 distinct connected `q1`-exact packets.  Their
physical shapes are

```text
radius 2: 3 simple C4
radius 3: 7 simple C6 + 1 connected repeated-vertex packet
radius 4: 39 simple C8 + 6 seven-vertex bow-tie packets.
```

Each bow tie has six non-articulation vertices with deleted/added degree
`(1,1)` and one articulation with degree `(2,2)`, so it is a legal
degree-preserving packet, although not a simple `C8`.

Exactly two radius-three packets are strict-token.  No retained `C4` and no
retained radius-four packet is strict-token.  In particular, the strict-token
permutation normal form is a proper subclass of `q1` coverage here.

The frozen exact score ledger is

```text
C4:  39^2,43^1
C6:  34^1,36^2,38^1,39^1,41^1,42^2

radius four:
  ordinary-unit contradiction 12
  numerical 35^1,36^4,38^2,39^14,40^1,41^3,42^3,
            43^1,44^1,47^1,51^1,53^1.
```

The separate auditor regenerated all 56 packet keys and matched them exactly
to the frozen scored catalogue; it also checked every stored physical edge
set and digest.  This regeneration shares the trusted low-level alternating
DFS and `q1` predicate with the original search, so it is not claimed as an
implementation-independent enumerator.  Independent adversarial count and
shape audits were also performed.  Under the active resource moratorium the
auditor did not rerun all 56 full propagations.  It separately rebuilt and
fully replayed the best endpoint, obtaining `Phi=34` again.

The scored catalogue used for reconciliation is

```text
scratch/k16_failedlit39_global_top9_targeted_packets_20260729.json
SHA-256 61898e9c231e7462221f09bb2c3e353fc880829e25e6ab341a8b6df442ce7d95.
```

## 7. The strict octahedral `C6`

Use bit coordinates `0,...,15` and put

```text
K={1,3,5,8,14,15},  a=2, b=6, c=11, d=13.
```

The six rank-eight vertices are

```text
K+ab=49518, K+ac=51502, K+bc=51562,
K+bd=57706, K+ad=57646, K+cd=59690.
```

The switch replaces the matching

\[
 \{ab-ac,\ bc-bd,\ ad-cd\}
 \quad\text{by}\quad
 \{ab-bc,\ ac-ad,\ bd-cd\}.                         \tag{7.1}
\]

Its lower token multisets are both `{K+a,K+b,K+d}`.  Its upper token
multisets are both

```text
{K+a+b+c, K+b+c+d, K+a+c+d}.
```

It therefore preserves both complete `q1` multiplicity ledgers, rather than
merely retaining one provider per colour.  Fresh physical replay gives

```text
degree-two vertices             12870
lower/upper q1 holes              0/0
residence violations             2235 = 1^133 2^906 3^1196
components                          3 = 1030+5685+6155
unhit two-choice motifs            506
candidate bank                     960
failed literals                     34
minimum two-branch core-row total   23
physical digest
03bac8f56fa3836273214de5e42e29205a8ec1c41ad19ac052b40962111fc6e2.
```

Relative to `F39`, exactly the five physical failure identities

```text
blue_remove (49511,49638), blue_remove (50146,50148),
blue_remove (50148,52068), blue_remove (53466,54474),
blue_remove (53466,61594)
```

disappear and none is created.

For comparison, the unique radius-four endpoint with minimum defined
numerical score `Phi=35` is a non-strict-token simple `C8`:

```text
delete (42139,42201), (45211,45465),
       (45459,46481), (46227,46233)
add    (42139,45211), (42201,46233),
       (45459,45465), (46227,46481).
```

It gives `Phi 39->35`, residence `2235->2236`, and two components
`1030+11840`.  Its ledger changes are

\[
 \Delta_{\rm lower}=e_{41115}-e_{45209},\qquad
 \Delta_{\rm upper}=e_{46297}-e_{42203},             \tag{7.2}
\]

with all resulting multiplicities still positive.

## 8. Audited scope and remaining boundary

The proved statements are exactly:

1. avoidance of every row carrier and pivot in a stored causally closed
   branch core transports the same signed contradiction after closure-based
   motif reindexing;
2. any feasible endpoint must hit all 39 expanded carrier sets;
3. the raw serialized support has exact transversal number eight, but this
   is not a general packet-radius lower bound;
4. the connected radius-two/three/four `q1`-exact neighborhood through the
   four requested present edges has exactly 56 packets;
5. it contains the explicit strict-token `C6` giving `39->34` with unchanged
   residence.

No completeness is claimed for disconnected packets, packets avoiding all
four targets, larger supports, or trades which change a proof row by adding
a previously absent provider.  `Phi=34>0`, so this endpoint is still
certifiably overlay-infeasible.  Nothing here constructs a resident
circulation, deeper-shadow carrier, exact compiler, or literal `k=16` word.

The independent audit is

```text
scratch/audit_k16_fl39_top4_complete_connected_packets_20260729.py
SHA-256 037ce54c2332529c60c2783f71fe64cf52e5eed1aac1a86f898778f1a8dbe307

scratch/k16_fl39_top4_complete_connected_packets_20260729.audit.json
SHA-256 b369b6b2e74e6f9580610fe408a4ac2bbf80e1fb18e64f8b184ee00b7dfbc279.
```

All enumeration and replay in this note was deterministic and local-light.
No SAT/CP solve, H100 job, GPU task, or web query was launched.
