# The `K17` greedy296 marked-preserving exchange master and literal guard oracle

Date: 2026-07-31  
Lane: AD, packet-safe occurrence checkpoint to exact complement rethread  
Status: exact sparse rank-ten master and literal chronology oracle; the master
has been built but no feasible repaired factor or common compiler is claimed

## 1. Rebased checkpoint

The authoritative inputs are

```text
occurrence forest
  scratch/k17_opt28_occurrence_greedy296_verified_20260731.flow.json
  SHA-256 079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f

corrected residual
  scratch/k17_opt28_occurrence_greedy296_connected_bflow_v2_20260731.json
  SHA-256 63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0

literal owner cycle
  scratch/k17_opt28_occurrence_greedy296_connected_full_20260731.owner_cycle.word
  SHA-256 801896cd15cc6b0b202db75421b93c1dc0e13a33b67fbc902ce283e242c381a6
```

The `v2` residual has exactly the same `4872` assignment rows as the earlier
connected residual, but corrects its embedded flow pin from the stale
`55f8af1f...` value to the final `079f5cd...` forest.  The catalogue here is
bound to `v2`; no stale delta is accepted.

The marked path is unchanged as a literal `4108`-owner word.  The new
complement chronology is not.  Its two cross edges, in marked-first linear
orientation, are

```text
P_a=83766 -- Q_1=18358, lower colour 18230
Q_b=7418  -- P_1=71930, lower colour  6394.
```

The second is the cyclic closing edge and is omitted from the linear
rank-ten baseline.

The authenticated literal ledger is

```text
strict D2 / D3 bad                       1875 / 1874
maximal-envelope empty / replay bad          0 / 2769
replay missing bits                              2901
upper holes ranks 10/11/12               1908/929/149
upper holes rank 13                                2.
```

Thus greedy296 improves residence and replay substantially over the original
OPTIMAL28 carrier, but does not itself pass the compiler or upper gates.

## 2. Why the exchange bank must be rebuilt

The marked owner set is the same, so the complement owner set and the
superset-count profile remain the same.  But the source edge chosen for a
lower colour changes on almost the entire complement chronology.  Since an
exchange column is “new same-colour edge minus that colour's **current**
source edge”, old column deltas are not portable.

Rebuilding from the literal greedy296 cycle gives

```text
complement colours                              20201
off-source columns                             545721
columns with implicit keeps                    565922
new canonical column-stream SHA-256
  ab27e28d780ab036669ae8d1fc058b150d585343b684ed4426e6411442b835af.
```

The colour profile is again

\[
 3^{15},4^{129},5^{454},6^{1601},7^{3836},8^{6748},9^{7418},
\]

but the excluded old pair in a colour group is the greedy296 pair.  The
direct packed stream has SHA
`7bb6ea4b1aae117c0f6b986b1c2892a24983d38fea57b511fe9635d285ab97ed`.

## 3. Exact signed rank-ten rows

Rotate the cycle to

\[
 P_1,\ldots,P_{4108},Q_1,\ldots,Q_{20202},P_1.
\]

For each complement source colour `c`, let `a_cb_c` be its current edge and
let `x_(c,uv)` select an off-source complement edge with `u cap v=c`.  Put

\[
 y_c=\sum_{uv}x_{c,uv}\in\{0,1\},                 \tag{3.1}
\]

where `y_c=0` retains `a_cb_c`.  Exact complement degree balance is

\[
 \sum_{c,uv}x_{c,uv}{\bf1}_{w\in\{u,v\}}
 -\sum_c y_c{\bf1}_{w\in\{a_c,b_c\}}=0
 \quad(w\in Q).                                   \tag{3.2}
\]

Let `L_0(S)` count the greedy296 linear owner edges, omitting only the frozen
closing cross `Q_bP_1`, whose union is rank-ten target `S`.  The exact zipper
rank-ten row is

\[
 L_0(S)+\sum_{c,uv}x_{c,uv}{\bf1}_{u\cup v=S}
 -\sum_c y_c{\bf1}_{a_c\cup b_c=S}\ge1.           \tag{3.3}
\]

Equation (3.3) is exact, not a fixed-window proxy: every complement edge is
represented by its three consecutive facet rows, every marked edge is a
literal owner pair, and the first cross is represented by the initial
owner/facet triple.  The closing cross has no linear suffix and stays outside
`L_0`.

Greedy296 has `1908` missing rank-ten rows.  They have exactly

```text
provider incidences                             66606
distinct provider colour groups                16445
support per row                                 10..45
zero-support rows                                   0.
```

One selected column has one gain label, so every complete solution satisfies

\[
                         \sum_c y_c\ge1908.         \tag{3.4}
\]

An exact max-flow chooses `1908` distinct donor groups, each with source
rank-ten surplus, and covers every missing row without creating a signed
rank-ten loss.  Hence (3.4) is tight in the service/group relaxation.  The
exported seed is deliberately not called a factor: it has nonzero degree
delta at `4195` complement owners, total `L1=4536`, maximum absolute delta
three.  Degree-balanced extension is the first genuine correlation gate.

The new fixed residual-pair fibre separately has `177` zero-support targets,
all among the current holes.  Releasing complement interiors gives them
`4973` exchange incidences with support `10..44`; hence this is a fixed-pair
obstruction, not an exchange-domain obstruction.

## 4. Exact sparse master

The frozen CP-SAT proto contains

```text
off-source edge Booleans                         545721
changed-colour Booleans                           20201
total Booleans                                   565922
colour equalities                                 20201
owner-degree equalities                           20202
rank-ten signed rows                              19448
initial rows total                                59851
binary proto size                                  14 MiB.
```

It minimizes `sum_c y_c` subject to (3.1)--(3.3).  A returned degree-two
factor may be one `Q_1`--`Q_b` path plus cycles.  Each disconnected cycle is
removed by the exact final-edge cut

\[
                  y(\delta_Q(R))\ge1               \tag{4.1}
\]

for that component, and the model is re-solved.  Only a connected final
graph is decoded as one owner cycle.

No occurrence/split column from the old base is accepted.  The wrapper
rejects `--split-columns`; a compound actuator must first export literal
greedy296-relative removed and added edges.

The `1908`-column service seed is installed only as a CP-SAT hint.  It is not
an equality, a feasibility claim, or an imported physical delta.

The frozen build result is

```text
scratch/ad_k17_opt28_greedy296_signed_rank10_master_20260731.bin
  SHA-256 9ffdf790808361d0d84a1c0428958610a0e75da56d833eb0359b0534de7697be
scratch/ad_k17_opt28_greedy296_signed_rank10_master_20260731.build.json
  SHA-256 4c992430ce8fad42d3f0ef412a021a8dbc35de8fcfb343eb8f4848e91f1e2516
  payload 1f831f7d37235ea3a7ca9e912c124dfeec0b443a114239aa6b6f63c4ecb1ae98
```

The H100 build was CPU-only, one process, capped at `12 GiB`; it used
`408268 KiB` maximum RSS and `6.94 s` wall time.

## 5. Literal compound-column oracle

Ranks eleven and twelve, residence, and compiler envelopes are not affine
column scores: they depend on the whole selected path order.  Therefore a
degree-balanced connected master incumbent is passed to the exact literal
oracle, which:

1. fixes the unchanged marked path and both new cross edges;
2. traverses the selected complement path;
3. materializes
   \(Z=P_1\cdots P_aF_0\cdots F_b\);
4. checks the complete lower palette and the additive rank-ten delta;
5. scans every rank-ten, eleven, and twelve interval;
6. checks strict `D2/D3` runs, all maximal-envelope cells, and exact replay;
   and
7. exports the pre-common-cap guard and scalar ledger.

For greedy296's empty selection the oracle gives

```text
replay missing bits                              2901
envelope volume                                150843
minimum envelope size                               6
host redundancy                                256785
rank10--12 hole demand total                      2986
scalar common-cap slack                           3293
scalar margin after those demands                  307.
```

The last line is only a scalar diagnostic.  Common-cap matching remains an
unsolved correlated rank-three clutter even after all prior gates pass.

The oracle's v2 seed authenticates the carrier SHA, target IDs, exact service
count/profile, and the complete baseline regression:

```text
scratch/ad_k17_opt28_greedy296_marked_exchange_seed_20260731.bin
  bytes 3956
  SHA-256 73fa8c68bc4534866fa9acef378256e407ef3225c7f5ebddda8a04be86600147
scratch/ad_k17_opt28_greedy296_marked_exchange_catalogue_20260731.meta.json
  SHA-256 aeb9aa3459978a3ce07e271dc32739346137113c0a254388a640c71defbad6f0
scratch/ad_k17_opt28_greedy296_marked_exchange_incumbent_20260731.eval.json
  SHA-256 1477402454205f288226fa23bbc6792c0aecd5f19f25f27f01b0e62f4d9404e8
```

The hashes of the final generic evaluator and greedy296 exporter are to be
read from their independent audit, because the evaluator was extended after
the first OPTIMAL28 regression to accept authenticated v2 expectation
trailers and compiler-guard fields.

## 6. Exact boundary

Proved and exported:

* a fresh, complete `545721`-column bank relative to greedy296/bflow_v2;
* all exact signed rank-ten rows and the sharp service-relaxation floor
  `1908`;
* an exact sparse degree/rank-ten master with lazy connectivity cuts;
* a nonphysical but exact full-rank-ten hint exposing the endpoint-balance
  debt; and
* an exact post-connectivity oracle for residence, ranks `10--12`, and the
  compiler pre-guards.

Unproved:

* feasibility of the degree-balanced connected rank-ten master;
* a connected selection improving residence/ranks eleven and twelve;
* preservation of ranks thirteen through seventeen (greedy296 currently has
  two rank-thirteen holes);
* common-cap matching; and
* a `K17` equality word.

Any future compound packet is admitted only after it is expressed as literal
removed/added greedy296 edges and replayed through this same factor and
chronology oracle.  Marginal or old-base deltas are not sufficient.
