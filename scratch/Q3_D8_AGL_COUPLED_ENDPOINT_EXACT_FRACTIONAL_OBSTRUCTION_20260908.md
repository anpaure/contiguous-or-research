# The affine translated-partner endpoint family has exact fractional cost 2856

2026-09-08. One h100 LP, with exact unscaled rational primal and dual
certificates. The complete family described below has fractional
optimum 2856, so every integral cover in that family has charge at
least 2856. This is above the improvement gate. No integer search ran.

The cover_selectors agent independently audited the source and then
read this complete note against the certificate, including all six
dual representatives and all fifteen primal entries. Both audits
passed the normalization, exact arithmetic, and stated family scope.

## 1. Exact family and absence of a symmetry assumption on the bank

Fix the coordinate labeling E=F_2^3. A physical row chooses an affine
four-point hyperplane H, a vector v outside its direction subspace,
and any full ternary geodesic C on H. Its partner full chain is the
coordinate translate C+v on the complementary shore. The two shores
independently retain one of these rank intervals:

    mode0: 0..8;  mode1: 1..8;  mode2: 0..7;  mode3: 1..7.

The row charge is the sum of its retained shore lengths, between
14 and 18. There is no requirement that C be individually
self-complementary, that a bank be complement-closed, that modes
match, or that a bank have any prescribed number of full rows.

The shore chains must be translates of the same full geodesic
before these independent endpoint deletions. All shores belong to
the fixed affine geometry on E. Arbitrary unrelated partner chains,
row-dependent relabelings that leave this affine family, and shorter
nonsaturated or more extensively truncated chains are outside scope.

No symmetry is assumed of a hypothetical integral or fractional
bank. Group averaging is used only to solve its fractional cover
problem and to obtain an invariant dual valid on every physical row.

## 2. Complete row normalization: 1050 types

An affine coordinate transformation can send the first axis of C
to zero, its shore to H={0,1,2,3}, and v to four. The residual linear
action on H fixes zero and permutes its three nonzero coordinates
arbitrarily. Thus the 630 full words with first axis zero have 105
orbits under this S3 action.

Independently, these representatives are precisely the words whose
first-occurrence order is 0,1,2,3. The code generated all 630 words,
canonicalized under the six residual maps, and independently
filtered for this first-occurrence condition. Both methods gave
the same set of 105 words.

Translation by v exchanges shores, so an endpoint-mode pair can be
put in unordered order m<=n. There are ten pairs with repetition.
The complete physical row family therefore has

    105*10 = 1050 invariant row types.                (1)

This normalization does not identify target orbits under arbitrary
coordinate permutations.

## 3. The actual affine target orbits

The group is AGL(3,2), of order 1344. The exact generators used were
translations by 1,2,4, the Singer map

    [0,2,4,6,3,1,7,5],

and the linear map interchanging the first two basis vectors,

    [0,2,1,3,4,6,5,7].

Their permutation closure was checked to have size 1344. A separate
union-find construction on all 6561 ternary targets gave 60 target
orbits. Every resulting orbit was independently replayed using all
1344 group elements. An independent Burnside cycle count gave the
same total of 60.

The 60 orbits refine the 45 coordinate histograms: thirty histograms
have one orbit each, and fifteen split into two orbits each. For
example, the central-corner histogram (4,0,4) splits into the fourteen
affine-plane supports and the 56 other four-point supports.

The orbit-size distribution is:

| Size | Number of target orbits |
| ---: | ---: |
| 1 | 3 |
| 8 | 6 |
| 14 | 3 |
| 28 | 6 |
| 56 | 18 |
| 84 | 3 |
| 168 | 6 |
| 224 | 9 |
| 336 | 6 |

Every target orbit is individually eligible in the complete row
family. The obstruction below is a simultaneous fractional cost
bound, not a missing-target obstruction.

## 4. Exact fractional formulation and result

Let A_(i,j) count how many points of representative physical row j
belong to target orbit i, and let d_i be that orbit's cardinality.
Let c_j be the row's actual endpoint charge. The LP is

    minimize sum_j c_j x_j,
    subject to sum_j A_(i,j) x_j >= d_i for every i,
    x_j >= 0.                                        (2)

All 60 target orbits and all 1050 row types are included. Each column
was built from literal full-chain prefix sums and its retained
Cartesian product; its sum was checked against the actual rectangle
cardinality.

Uniformly developing row j under AGL distributes A_(i,j) occurrences
uniformly over the d_i targets in orbit i. Thus a feasible x gives
an actual fractional target cover. Conversely, averaging any
fractional physical cover gives (2) with unchanged cost. Therefore
(2) is exactly the fractional cover problem for Section 1's family.

The sole LP returned 2856. Rationalization needed no scaling:
the reconstructed primal and dual were already feasible exactly,
and their exact objectives agreed. Hence

    K_fractional = 2856.                             (3)

The improvement threshold is 76545/32=2392+1/32. Its deficit is

    2856 - 76545/32 = 14847/32.                       (4)

In particular no integral endpoint cover in this family can meet
the threshold, regardless of its mixture of endpoint modes or its
number of full orbits. The earlier proposed 2384 two-full-orbit
variant is also excluded within this same fixed affine family.

## 5. Six-orbit exact dual

Give every point in the AGL orbit of a listed representative the
listed weight, and give all other targets weight zero. These are
geometric orbits, not entire coordinate histograms.

| Representative in coordinate order 0,...,7 | Orbit size | Weight per target |
| --- | ---: | ---: |
| (2,2,2,0,0,0,0,0) | 56 | 1 |
| (2,2,2,2,1,0,0,0) | 56 | 1 |
| (2,2,2,0,2,0,0,0) | 56 | 7/2 |
| (2,2,1,1,2,0,0,0) | 336 | 7/2 |
| (2,1,2,1,1,1,0,0) | 336 | 7/2 |
| (2,1,1,1,1,1,1,0) | 56 | 7/2 |

All 1050 row inequalities were checked in exact rational arithmetic:
the total target weight in each row is at most its actual charge.
The row normalization in Section 2 makes this valid for every
physical row in the family. Total target weight is

    56+56+(7/2)*(56+336+336+56) = 2856.               (5)

Summing row inequalities over any physical cover proves the lower
bound directly. This argument requires no symmetry of that cover.

## 6. Matching exact primal

Rows in the certificate are indexed from zero. The 105 canonical
words are in lexicographic order; for each word, mode pairs are
listed by combinations-with-replacement in lexicographic order.
The following fifteen nonzero total family weights give an exact
feasible primal of cost 2856:

| Row-type index | Total family weight |
| ---: | ---: |
| 62 | 14 |
| 69 | 14 |
| 79 | 14 |
| 96 | 20 |
| 116 | 4 |
| 134 | 9 |
| 139 | 5 |
| 218 | 4 |
| 229 | 10 |
| 289 | 14 |
| 488 | 24 |
| 489 | 32 |
| 709 | 4 |
| 759 | 24 |
| 839 | 4 |

These integers are weights of uniformly averaged row families.
They are not a selection of fifteen or 196 physical rectangles,
and they do not supply an integral cover. All sixty primal orbit
inequalities were checked exactly, along with equality of its
objective to (5).

## 7. Runtime, artifacts, and exact checks

The complete process ran once on h100 under a five-second outer
cap, two-CPU affinity, and a 1 GiB address-space limit. The LP had
a three-second solver limit. Actual times were:

    catalogue and independent orbit checks: 0.10143136512488127 s;
    sole LP: 0.027600964065641165 s;
    complete process including exact certificates: 0.42087069898843765 s.

No second LP, integer search, mathematical restart, or physical
cover claim occurred. Both rational scaling factors were exactly
one; the primal-dual gap was exactly zero.

Files:

* `q3_d8_agl_coupled_endpoint_fractional_gate_20260908.py`;
* `Q3_D8_AGL_COUPLED_ENDPOINT_FRACTIONAL_SUMMARY_20260908.jsonl`;
* `Q3_D8_AGL_COUPLED_ENDPOINT_FRACTIONAL_CERTIFICATE_20260908.json`.

The certificate contains all sixty target representatives, orbit
sizes and histograms; all 1050 literal row words and endpoint modes;
the complete integer incidence matrix; and the exact sparse primal
and dual. The one command was

```text
ssh h100 'timeout 5s python3 -' < scratch/q3_d8_agl_coupled_endpoint_fractional_gate_20260908.py > scratch/Q3_D8_AGL_COUPLED_ENDPOINT_FRACTIONAL_SUMMARY_20260908.jsonl
```
