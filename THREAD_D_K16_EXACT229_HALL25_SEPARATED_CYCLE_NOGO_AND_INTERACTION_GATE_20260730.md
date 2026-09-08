# Exact229 Hall-25 separated-cycle no-go and interaction gate

Date: 2026-07-30

Status: **proved scoped no-go for one separated bounded token cycle; the
distance-7 interaction class remains live**.

## 1. Authoritative carrier and Hall witness

The frozen chronology is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974
```

It has length 12,873, exactly 12,870 distinct rank-eight targets, flats at
`6320,12869,12871`, scalar capacity 32,063, exact nonzero maximal-envelope
reconstruction, and no arbitrary-width upper hole.  The exact generalized
compiler audit is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.hall.k.audit.json
SHA 85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0
payload c5c99fead7b99c2b2bf35540440f10434ae4c1c42345f72f331348bd2de25eb3
```

It has 26,332 lower targets, 32,063 proper-prefix cells, 347,875
incidences, and a maximum matching of size 26,307.  Its canonical
alternating-reachability shore satisfies

\[
       |U|=212,\qquad |N(U)|=187,\qquad |U|-|N(U)|=25.       \tag{1.1}
\]

The induced witness graph `U union N(U)` has exactly 25 connected
deficiency-one components.  Twelve are isolated `1/0` components; the
others have sizes

```text
(3/2)^2, (4/3)^3, 6/5, 7/6, 15/14, 18/17,
23/22, 34/33, 35/34, 44/43.
```

These are components of the induced witness graph, not automatically the
DM components of the full Hall graph.

An independent replay is frozen in

```text
THREAD_D_K16_EXACT229_HALL25_ENDPOINT_LOCALITY_AUDIT_20260730.md
scratch/threadD_k16_exact229_hall25_independent_20260730/
```

Its H100 run used one CPU, exited zero in 6.33 seconds, and reached 66,664
KiB RSS.  The principal audit has SHA
`165c6cdd19f2ad349b5bc9787f7f1f81a93d301525f84743f149676e64f590ff`
and payload
`82534ab571a3e187333965c4808ce5a8c773926fff36c07d9c6ca7f4490ea5d8`.

## 2. Exact fixed-shore column and current

For a proper-prefix cell `c=(s,l)`, `1<=l<=d_s<=3`, let `P_j` be the
maximal envelope, let `M_c` be its exact mandatory mask, and put

\[
                         A_c=\bigvee_{j=s}^{s+l-1}P_j.
\]

A lower target `T` is incident with `c` exactly when

\[
 M_c\subseteq T\subseteq A_c,
 \qquad T\cap P_j\ne\varnothing\quad(s\le j<s+l).   \tag{2.1}
\]

Thus the full occurrence profile is

\[
              \pi(c)=\left(M_c,\{P_s,\ldots,P_{s+l-1}\}\right), \tag{2.2}
\]

where the braces denote a set: order and repeated equal envelope masks do
not affect (2.1).  For the fixed shore define the projected column

\[
                 B_U(c)=\{T\in U:T\sim c\}.                   \tag{2.3}
\]

The incumbent has 30,977 distinct full profiles but only 216 projected
columns, 215 of them nonempty.  There are 535 incidences between the shore
and its 187 neighbour cells; their length histogram is `7,80,128` for
lengths `1,2,3`.

For any new exact chronology define

\[
 G_U=N_{new}(U)\setminus N_{old}(U),\qquad
 L_U=N_{old}(U)\setminus N_{new}(U).
\]

Then

\[
 |N_{new}(U)|-|N_{old}(U)|=|G_U|-|L_U|.             \tag{2.4}
\]

Every compiler-feasible exchange from exact229 must therefore have

\[
                           |G_U|-|L_U|\ge25.          \tag{2.5}
\]

Condition (2.5) is necessary, not sufficient; every survivor must rerun
the complete matcher because a different shore may remain or become
deficient.

## 3. Local replacement columns

A directed arc `p <- q` replaces target row `p` by the target currently at
row `q`.  It is locally legal when it preserves the frozen flat ledger and
every maximal-envelope equation that can change.  A closed directed token
cycle preserves the target multiset.

The exact COMP3 profile of a cell starting at `s` depends only on target and
depth rows `s-6,...,s+5`.  Consequently an edit at row `p` can affect only
cell starts in

\[
                              W_p=[p-5,p+6].          \tag{3.1}
\]

This proof-safe interval includes effects transmitted through a changed
envelope letter and through the carrier defining a mandatory mask.  The
earlier narrower interval `[p-3,p+4]` is not used for a theorem.

If edit positions have pairwise distance at least 12, the intervals (3.1)
are disjoint.  The exact fixed-shore current of the simultaneous cycle is
then the sum of its one-arc currents.  Exact middle replay is also local;
arbitrary-width upper completeness is not, and is always replayed on the
whole candidate.

## 4. Complete wide-12 census

The declared class consists of one directed token cycle on two through
eight positions, equivalently at most seven nonroot tokens, with every two
positions at distance at least 12.  The least position is the canonical
root; inverse orientation is retained as a different permutation.

The exact arc catalogue is:

```text
tested ordered replacements   165,701,250
locally legal arcs                 165,666
positive-current arcs                 4,681
maximum one-arc additions / net        4 / 4
```

The complete gain histogram is stored in `result.json`.  The DFS uses the
safe upper bound

\[
           current\ score+(remaining\ arcs)\cdot4.              \tag{4.1}
\]

The remaining count includes the closing arc, so (4.1) cannot prune a
cycle of total current at least 25.  The exact result is

```text
DFS nodes                         100,373
safe bound prunes                 590,071
closures reached after pruning        680
cycles with fixed-shore current >=25    0
```

The 680 closures are not asserted to be all low-current cycles.  They are
the closures reached after the sound threshold pruning; this is sufficient
for the no-go because every pruned continuation has certified current below
25.  Since no row passes the necessary shore cut, full upper and Hall calls
are neither needed nor licensed.

Authoritative artifacts are

```text
scratch/threadD_k16_exact229_hall_arc_cycle_census_20260730.cpp
  SHA 8696ee77e017bf4e8a42885263cb5af58e46d336027694363f9ef8b13c86bbf2

scratch/threadD_k16_exact229_hall_arc_cycles_wide12_20260730/result.json
  SHA d3a64db866222785f472ec213e8411cee8540b56daf27082f8057f8ec32be719

scratch/threadD_k16_exact229_hall_arc_cycles_wide12_20260730/RUN_MANIFEST.md
  SHA cc9b9cd04d2fb981ba1b4f2bb606ca23704e024d574561a5c84bc917d141cbc1
```

The run used one H100 CPU, no GPU, a 2 GiB address-space cap, and a 1,200
second wall cap.  It completed with exit zero in 12.73 seconds and 6,656
KiB maximum RSS.  The sibling separation-8 result is explicitly
quarantined and supplies no no-go.

An independent C++ implementation rebuilt all 165,701,250 ordered tests
and all 165,666 legal arcs, with zero legality disagreements.  Its positive
arc file is byte-identical to production (SHA `8d45283c...`) and it
reproduces every histogram and DFS count.  It also persisted and literally
replayed all 680 reached closures:

```text
every reached closure exact                 680
arbitrary-upper-complete closures            90
maximum fixed-shore current                    4
closure current histogram
  -3:1, -2:4, -1:18, 0:508, 1:116, 2:27, 3:5, 4:1
closure sizes
  2:544, 3:136
maximum upper bound at a pruned prefix        24
```

The independent artifacts are

```text
scratch/audit_threadD_k16_exact229_wide12_cycles_independent_20260730.cpp
  SHA 1a0276b284d47071f73016abf0ef7e013e6f4f22e5af986d6553c69e9c4e91bc
scratch/threadD_k16_exact229_wide12_independent_20260730/independent.audit.json
  SHA 406f4527dc52f7da2fb4ac35e0e5830d2d2ffbc5a75967ce11b6c2b8c4ed1541
scratch/threadD_k16_exact229_wide12_independent_20260730/independent_closures.tsv
  SHA 2cc8534c9b65167b0ba41acc45897d749a60e754508606853e01f9f37a0d447d
```

This audit used one H100 CPU for 21.55 seconds and 7,112 KiB RSS.

## 5. Minimal live interaction extension

Middle-envelope legality for two individually legal row edits has the
smaller dependency interval `[p-3,p+3]`.  Therefore positions at distance
at least seven can still be combined without a middle-replay cross term.
For distances `7,...,11`, however, their Hall intervals (3.1) overlap.

Let `w(a)` be the one-arc current.  For two compatible arcs `a,b`, define
the exact pair correction

\[
 \kappa(a,b)=\Delta_U(a,b)-w(a)-w(b),               \tag{5.1}
\]

where `Delta_U(a,b)` is computed by applying both replacements to the
literal overlapping cell profiles.  If all vacancy positions are at least
seven apart, no cell start belongs to three intervals (3.1): three ordered
positions span at least 14, while each interval has endpoints `p-5,p+6`.
Möbius expansion therefore stops at order two, and every closed cycle has
the exact current

\[
             \Delta_U(C)=\sum_{a\in C}w(a)
               +\sum_{\{a,b\}\subseteq C}\kappa(a,b).          \tag{5.2}
\]

Only pairs whose vacancies differ by `7,...,11` can have nonzero
`kappa`.  Equation (5.2) is the required non-separated interaction model.
It retains exact target ownership and makes the next census finite; it does
not assume independence.  Score-qualified cycles must still pass literal
maximal-envelope and arbitrary-upper replay before the full Hall matcher is
called.

The wide-12 no-go does not exclude this interacting class, cycles on more
than eight positions, multiple cycles, blocks rather than singleton rows,
or other rethread topologies.
