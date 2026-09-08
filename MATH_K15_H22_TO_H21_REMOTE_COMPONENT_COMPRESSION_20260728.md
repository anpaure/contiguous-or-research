# Exact Hall 22 to Hall 21 remote-component compression

Date: 2026-07-28

Status: independently reconstructed and audited outer-Hall descent with an
all-native certificate on the final critical DM shore.  This is not yet a
length-6438 universal word or a common-word lift of one full global matching.

## 1. The route

From the canonical Hall-22/six-zero carrier,

\[
 H22\xrightarrow{\operatorname{FF}(1320,5339,6194)}H22^{\rm port}
 \xrightarrow{\operatorname{FR}(778,2292,6368)}H21.             \tag{1.1}
\]

The exact states are

```text
scratch/k15_segment_braid_hall22_zero6.json
scratch/k15_segment_braid_hall22_portal_to21.json
scratch/k15_segment_braid_hall21_zero6.json
```

with SHA-256 values

```text
bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778
0f8b287ad290139e61a4387e90cf5c7eaaa3166a2e20ac642815ce9604e974ea
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
```

Their matching ranks, Hall deficiencies, and zero counts are

\[
\begin{array}{c|ccc}
&H22&H22^{\rm port}&H21\\ \hline
\nu&16361&16361&16362\\
h&22&22&21\\
z&6&6&6.
\end{array}                                                       \tag{1.2}
\]

Every state is a permutation of all `6435` rank-eight masks, a Johnson path,
depth-three resident, complete in every upper support layer `q=1,...,7`, and
has four immediate-lower holes.  The deeper lower-hole vectors are

\[
 (4,18,6,1,0,0,0),\quad
 (4,18,8,1,0,0,0),\quad
 (4,18,9,1,0,0,0).                                               \tag{1.3}
\]

Thus only immediate-lower support and the full compiler rank, not every
deeper lower support, are protected along this route.

## 2. What the neutral router does

In the initial H22 canonical DM decomposition there is a `160/159` gap-one
component rooted at `449`.  The first braid removes that component from the
canonical shore and replaces it by a much smaller `24/23` gap-one component
rooted at `458`.  The new component targets are

\[
\begin{aligned}
\{&458,462,474,475,478,490,494,1482,1486,1498,1514,2506,2510,2522,\
&2538,4554,4570,5578,16842,16846,16858,17866,18890,20938\}.
\end{aligned}                                                     \tag{2.1}

The first transition changes 29 physical cell shores but preserves matching
rank.  With a common core of rank `16337`, its contracted boundary rank is

\[
 24\longrightarrow24.                                           \tag{2.2}
\]

This is a literal component **compression**, not a conjugacy or transport of
the old `160/159` incidence graph.  It is another exact example of a neutral
global chronology acting as a state-dependent router.

## 3. The splitter

Inside the intermediate `24/23` component, cancel the 22 unchanged restricted
cell shores.  The old exceptional shore is

\[
 \{462,16846\}.                                                   \tag{3.1}
\]

The improving braid replaces it by

\[
 \{458,462\},\qquad\{16842,16846\}.                              \tag{3.2}
\]

There is already one unchanged `{458,462}` cell, so the complete profile has
23 old cells and 24 final cells.  The exact changed final cells are

\[
\begin{array}{c|c|c|c}
\text{cell}&(d,s)&\text{restricted shore}&(\text{envelope},\text{mandatory})\\ \hline
7216 &(1,778)&\{458,462\}&(462,448)\\
13652&(2,777)&\{16842,16846\}&(16846,16832).
\end{array}                                                       \tag{3.3}
\]

The full common-core rank is `16344`, and the contracted boundary rank is

\[
 17\longrightarrow18.                                           \tag{3.4}
\]

Hence the global matching rank rises by exactly one.  The intermediate
component disappears completely from the final canonical DM shore.

## 4. Exact Hall and native certificates

The independently recomputed cross-shore gap matrix is

\[
 \begin{pmatrix}
 22&21&21\\
 21&22&21\\
 21&21&21
 \end{pmatrix}.                                                   \tag{4.1}
\]

The explicit matching gives final deficiency at most 21; every column of
(4.1) supplies a gap-21 shore, proving equality.

The final canonical shore has size `846/825`, decomposes into exactly 21
gap-one components, and all 825 right cells have pairwise distinct native
traces under the one final maximal erosion controller.  Thus its native
critical-shore common-pin gap is exactly 21.

There is a stronger literal lift on the **former intermediate shore**.  Its
870 targets split as the final 825-target native basis, the 24 targets in
(2.1), and 21 exposed roots.  Every nonroot target in (2.1) has its own native
cell; target `462` has the two distinct native cells `7216` and `8268`.
Assign cell `8268` to `462`, shrink cell `7216` from native `462` to root
`458`, and keep every other pin native.  This gives

\[
 825+24=849=870-21                                             \tag{4.2}
\]

distinct target/cell pins in one literal word.  The only controller change is

\[
 (P_{778},P_{779})=(398,206)\longmapsto(394,202),               \tag{4.3}
\]

which deletes coordinate bit `2`.  Exact reconstruction verifies every
central window, all 849 selected pins, and nonemptiness at every physical
position.  Hence the transition pays one genuine common-`Q` unit, not merely
one projected matching-rank unit.

This remains shore-local: it does not yet install all 16,362 edges of an
arbitrary global maximum matching into one word.

## 5. Reproducibility and next gate

The independent audit is

```text
scratch/audit_k15_segment_braid_hall22_to21.json
scratch/audit_k15_h21_remote_component_common_q.py
scratch/k15_h21_remote_component_common_q_certificate.json
```

with SHA-256

```text
cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c.
```

It is generated by

```text
python3 scratch/audit_k15_segment_braid_descent.py \
  --base scratch/k15_segment_braid_hall22_zero6.json \
  --step scratch/k15_segment_braid_hall22_portal_to21.json \
  --step scratch/k15_segment_braid_hall21_zero6.json
```

The next finite target is the same statewise architecture at Hall 21: a
neutral router which compresses or rethreads one of the 21 gap-one components,
followed by a splitter which raises the contracted boundary rank by one while
retaining six-zero control and one common physical compiler.
