# Independent audit of the K17 `c=312` cut and first-bundle gate

Date: 2026-07-31  
Status: **GO** for the exact cut-exposure optimum and the joint first-bundle
witness. **OPEN** for the remaining ears, prefix, and upper ranks. No
length-24313 word is claimed.

## 1. Independent reconstruction

I reconstructed the two-cut Greene--Kleitman forest directly from the two
last-maximum pivots, without importing either producer replay. The resulting
forest has

```text
10152 edges, 15376 vertices,
10448 degree-one vertices, 4928 degree-two vertices,
4072 unused rank-seven vertices,
2224 missing rank-six colours.
```

Exactly 674 missing rank-six colours have no original endpoint superset.
Exactly 294 of those have all eleven supersets unused. Thus the cut-exposure
target is exactly the complementary set of 380 colours.

## 2. Independent optimization

I used a different CP formulation from the producer. A binary assignment
variable selects a triple

\[
  (\text{colour},\ \text{internal provider vertex},\
    \text{incident edge used to expose it}).
\]

Every colour selects exactly one triple, at most one colour uses a provider
vertex, and the selected cut edges form a matching in the old forest. This is
equivalent to the exposure problem but does not use the producer's
colour-to-vertex/linking-row formulation.

On the H100 CPU, CP-SAT independently returned

```text
primary:   OPTIMAL, objective = bound = 312 cuts
secondary: OPTIMAL, objective = bound = 90 endpoint--internal cuts
```

The alternate model has 2,865 candidate cuts and 5,696 assignment triples.
The first one-worker run found a feasible solution but did not close the
bound in 300 seconds; the eight-worker run closed both bounds. Thus `312/90`
is an independently reproduced computational optimum, not a formal DRAT
proof certificate.

## 3. Frozen exposure certificate

The immutable exposure certificate has SHA-256

```text
30e0812da947f999a5c6d91ca52c323c7ca25302c127daf3434262faed9e9474
```

Literal replay verifies:

* 312 distinct old edges are cut;
* all 624 cut endpoints are pairwise distinct;
* the cut types are 90 endpoint--internal and 222 internal--internal;
* all 380 target colours are assigned once to 380 distinct exposed internal
  vertices;
* 244 cuts carry one assignment and 68 carry two.

After deleting these edges, direct graph traversal gives

```text
degree 0: 90, degree 1: 10892, degree 2: 4394,
9840 retained edges, 5536 components, 90 isolated components.
```

The 90 one-sided and 222 two-sided cuts destroy

\[
  90+2(222)=534
\]

old turns, leaving 4,394.

## 4. Independent joint first-bundle replay

The stronger joint certificate has SHA-256

```text
ad6fb0631c9c336f229846cdb2a78a8f1a8f3a6532968310b964f5f560c0e9e4
```

For every one of the 380 hard colours, I independently checked a selected
tuple

\[
 (D,v,e,n_v,w,q_8,h_9),
 \qquad q_8=v\cup w,\quad h_9=n_v\cup v\cup w,
\]

where `v` is an internal old port, `e` is its selected exposure cut, `n_v`
is the retained old neighbour, and `w` is genuinely unused. The replay checks
the stronger exact identity `v intersect w = D`, not only containment.

The certificate has simultaneously:

```text
380 distinct colours,
380 distinct exposed ports,
380 distinct unused partners,
380 distinct rank-eight q8 colours,
380 distinct rank-nine h9 colours.
```

For each `q8` already used by the seed, its unique owner edge is selected for
cutting. For each `h9` already used by a seed turn, at least one of the two
owner edges is selected for cutting. There are 274 dynamically released q8
values and 273 h9 values whose old owners are dynamically broken. Every one
of the 312 cuts is an exposure cut; there are no palette-only cuts.

Because every joint bundle solution is also an exposure solution, the
independent exposure lower bounds imply that a joint witness cannot use fewer
than 312 cuts, nor fewer than 90 endpoint--internal cuts on the 312-cut face.
The literal joint witness attains both. This proves the joint optimum from the
independent optimization plus the certificate, without trusting the joint
optimizer's status field.

## 5. Correct scalar accounting, including isolated components

Keeping the same 1,535 inserted rank-seven vertices gives 5,535 joins and
7,070 new edges. The scalar ear count

\[
 (x_1,x_2,x_3,x_4)=(4336,905,252,42)
\]

satisfies

\[
 \sum x_i=5535,
 \quad \sum(i-1)x_i=1535,
 \quad \sum i x_i=7070.
\]

The naive new-turn count is 12,605. Each of the 90 isolated endpoint
components causes exactly one double-count in that formula, so the correct
new-turn count is 12,515. Hence

\[
 9840+7070=16910,
 \qquad 4394+12515=16909.
\]

Deleting 312 unique old rank-six edges enlarges the rank-six debt from 2,224
to 2,536. Therefore the new-edge ledger is

\[
 7070=2536+4534.
\]

This ear vector is only a scalar schedule. The audit does not assert that all
of its ears can be selected simultaneously.

## 6. Exact scope

The result closes the first physical bundle for the 380 cut-exposed colours.
It does **not** yet provide:

* a simultaneous ordering of all 5,535 ears;
* the 294 all-unused hard colours;
* the remaining 1,844 original-missing and 312 cut-created rank-six debts;
* the 4,534 repeated/decorated rank-six slots;
* freshness of all remaining rank-eight and rank-nine values;
* the alternating prefix completion;
* ranks 10 through 17; or
* a universal word of length 24,313.

The earlier fixed-assignment partner Hall obstruction (`368/380`) remains a
correct no-go for that frozen exposure assignment. It is not a contradiction:
the joint certificate reoptimizes cuts, assignments, and partners together.

## 7. Independent artifacts

* `scratch/audit_independent_k17_gk_cut312_20260731.py`
* `scratch/independent_k17_gk_cut312_20260731.audit.json`
* `scratch/audit_independent_k17_gk_joint_cut_bundle_20260731.py`
* `scratch/independent_k17_gk_joint_cut_bundle_20260731.audit.json`

The independent optimization payload hash is

```text
27b7d97848c22880eb7df12724d5ea55f7d381f692dfb4f9c2b8eca69bc92e60
```

and the independent joint payload hash is

```text
13fc01a23cd5a8c43febc3874351ff19d4b41d9f3d627cdedb9e8d81e3c3978c
```
