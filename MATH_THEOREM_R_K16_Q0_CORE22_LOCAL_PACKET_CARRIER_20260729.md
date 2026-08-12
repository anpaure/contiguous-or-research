# Lane R: the `k=16` detector-zero core carrier and its exact local packet reduction

Date: 2026-07-29

## 1. Frozen endpoint and scope

This note concerns the fixed resident factor `R` and the detector-zero factor
`Q0` in the following artifacts:

```text
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
SHA-256 17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8

scratch/k16_failedlit0_fullbank_20260729.audit.json
SHA-256 703d44d0e949094a6bc37ed0a44b1a3caca2af74fda24cf0908c84a98246976d

scratch/k16_failedlit0_exact_overlay_20260729.json
SHA-256 4fd0b2d2a15326b9ecfa5c1b939f835814ca2d5303268268ad1ea639e33fdcf2

scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json
SHA-256 2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238

scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951.
```

The resident decoder is pinned to

```text
scratch/k15_pbbs_trade_baseline.json
SHA-256 8955fc7babdfc37698f51115fad2737fb4dd09c2c3a2f387f02ac690154f460f

scratch/k16_pbbs_component_trade_27_factor_20260729.json
SHA-256 91c434654d38466790dd373d26ff4e88f115d7cab1c29f71520a99cc4b349985

scratch/k15_two_component_a_cycles_20260729.json
SHA-256 bc58e466e72c0b418aa24929d45640dcfe6ffbe567caae480939e76367533738.
```

`Q0` is a spanning degree-two factor of `J(16,8)`, has no lower- or
upper-`q1` hole, and has two components of lengths `12857,13`.  It has 2,222
short coordinate runs.  All 954 candidates in the recomputed two-choice bank
were probed and none is double-failed.  This detector-zero statement is only
a necessary screen.  The exact degree-plus-both-`q1`-plus-residence overlay
for `(R,Q0)` is infeasible.

The solver-backed deletion-minimal assumption core, with every degree row
permanently hard, consists of 21 physical `q1` coverage rows and motif 390.
It contains eight lower-`q1` rows and thirteen upper-`q1` rows.  Every
one-row deletion was solved `OPTIMAL`, while the full 22-row set replayed
`INFEASIBLE`; there were no `UNKNOWN` minimization replays.  This is a
solver-backed minimality certificate, not a solver-free derivation of the
core-minus-one primal witnesses.

This note defines a complete enumeration of a **connected core-local** packet
class.  Its finite exhaustion requires all four frozen shards and the merged
physical replay recorded below.  It
does not claim a global radius-four no-go, does not include a disconnected
`C4 disjoint-union C4`, and does not infer overlay feasibility merely from
breaking the old core.

## 2. The exact 22 guarded rows

Each palette row has `Q0`-load one.  Its current `Q0\R` provider and, where
present, its current `R\Q0` provider are:

| row | unique `Q0` provider | `R`-only provider |
|---|---|---|
| lower 18526 | `(18558,26718)` | none |
| lower 47652 | `(47660,47780)` | `(47908,64036)` |
| lower 51230 | `(51358,59422)` | `(51262,59422)` |
| lower 57614 | `(58126,58638)` | none |
| lower 57870 | `(57902,57998)` | `(57871,59918)` |
| lower 57894 | `(58022,59942)` | `(57902,61990)` |
| lower 59406 | `(59918,63502)` | `(59422,60430)` |
| lower 61988 | `(61990,62052)` | `(61989,64036)` |
| upper 27742 | `(26718,27678)` | none |
| upper 47645 | `(45597,47644)` | none |
| upper 47676 | `(47164,47660)` | `(47644,47668)` |
| upper 47772 | `(15004,47644)` | none |
| upper 58254 | `(57998,58250)` | `(50062,58126)` |
| upper 59486 | `(59422,59478)` | `(26718,59478)` |
| upper 59950 | `(59918,59948)` | `(51758,59942)` |
| upper 61998 | `(57902,61994)` | `(57902,61990)` |
| upper 62118 | `(45734,61990)` | none |
| upper 62222 | `(45838,58126)` | `(58126,62214)` |
| upper 64038 | `(55846,59942)` | none |
| upper 64044 | `(64036,64040)` | `(47660,61996)` |
| upper 65060 | `(64036,65028)` | none |

There are 21 distinct blue terms and thirteen red occurrences representing
twelve distinct red edges: `(57902,61990)` occurs in both a lower and an
upper row.  The current term union has 33 edges and 41 endpoints.

Motif 390 is the four-vertex path

```text
61994 -- 57902 -- 57998 -- 58250
```

with closure

```text
(57902,61994), (57902,57998), (57998,58250).
```

These three edges are already guarded palette terms.  They are respectively
the unique `Q0` providers of upper 61998, lower 57870, and upper 58254.
Thus a switch which deletes a motif-390 edge necessarily has palette-row
contact as well.

## 3. Full palette and one-star carriers

### Theorem 3.1 (exact physical provider fibres)

Let `c` be a rank-seven lower colour and `u` a rank-nine upper colour.  Their
physical `q1` provider sets in `J(16,8)` are

\[
 P_c^- = \{\{c\cup\{i\},c\cup\{j\}\}:i<j,\ i,j\notin c\},
\]

and

\[
 P_u^+ = \{\{u\setminus\{i\},u\setminus\{j\}\}:i<j,\ i,j\in u\}.
\]

Each set has exactly `binom(9,2)=36` edges.  For the eight lower and thirteen
upper rows above there are 288 lower occurrences, 468 upper occurrences, and
24 lower/upper overlaps.  Their union `P` therefore has exactly

\[
                         |P|=288+468-24=732
\]

physical Johnson edges.

For a packet `(D,A)`, define **palette-row contact** to mean
`(D union A) intersection P` is nonempty, and define **`V`-degree-row
contact**, for `V` defined immediately below, to mean that an edge of
`D union A` has an endpoint in `V`.  Contact means that the packet changes
selected variables occurring in the row.  It does not mean that the balanced
packet violates a degree equation, and it may replace a provider while
preserving the numerical palette load.

#### Proof

A lower provider has two rank-eight endpoints whose intersection is `c`.
Each endpoint adds one of the nine coordinates outside `c`, and the two
added coordinates must be distinct.  This gives one edge for every unordered
pair of outside coordinates.  The upper statement is complementary.  A
lower fibre `P_c^-` and upper fibre `P_u^+` share exactly one edge when
`c subset u`, and share none otherwise.  In the displayed row order, the
eight lower colours are contained in respectively

```text
2,4,1,2,4,4,2,5
```

of the thirteen upper colours, totalling 24 shared edges.  QED

All 24 overlap edges are absent from `Q0`; exactly `(57902,61990)` belongs to
`R`.  The other 23 belong to neither factor.

Let `V` be the 41 endpoints of the 33 current guarded terms.  Their **33-term
endpoint one-star** `Star(V)` has 2,521 Johnson edges.  Exactly 61 of them
belong to `Q0`.  Of the 711 absent edges in `P\Q0`, exactly 435 meet `V` and
276 have both endpoints outside `V`.

### Theorem 3.2 (the 61-plus-276 target reduction)

Define

\[
 T^- = Q0\cap\operatorname{Star}(V),\qquad |T^-|=61,
\]

and

\[
 T^+ = \{e\in P\setminus Q0:e\cap V=\varnothing\},\qquad |T^+|=276.
\]

Let `(D,A)` be any finite exact factor packet with

\[
 D\subseteq Q0,\quad A\subseteq E(J(16,8))\setminus Q0,
 \quad \deg_D(v)=\deg_A(v)\quad\hbox{for every }v.
\]

Then `(D,A)` has palette-row contact or `V`-degree-row contact if and only if

\[
                     D\cap T^-\ne\varnothing
       \quad\hbox{or}\quad A\cap T^+\ne\varnothing.             \tag{3.1}
\]

In particular, (3.1) covers every packet which destroys motif 390.

#### Proof

If a deleted edge has an endpoint in `V`, it meets `T^-`.  Every `Q0`
provider of a guarded colour is one of the 21 current blue terms and hence
also lies in `Star(V)`, so a guarded-provider deletion again meets `T^-`.

Suppose instead that an added edge `a` contacts a guarded palette row.  If its
two endpoints avoid `V`, then `a` lies in `T^+`.  If `a` meets some `v in V`,
local degree balance gives `deg_D(v)=deg_A(v)>0`; consequently `D` contains a
`Q0` edge at `v`, which lies in `T^-`.  The same balance argument handles an
arbitrary added edge which contacts a degree row at `V`.  Conversely, an edge
of `D intersection T^-` gives `V`-degree-row contact, while an edge of
`A intersection T^+` is a provider in `P` and gives palette-row contact.  QED

This reduction is exact for the declared local contact property; it is not a
claim that `T^- union T^+` carries the whole UNSAT proof.

## 4. Complete connected C4/C6/C8 enumeration

Call `(D,A)` an exact-radius-`r` connected packet if

```text
D subset Q0, A subset E(J(16,8))\Q0,
|D|=|A|=r,
deg_D(v)=deg_A(v) for every v,
and the support D union A is connected.
```

Edges are simple but vertices may repeat.  Thus “C4/C6/C8” below means an
alternating closed trail of lengths `4,6,8`, not necessarily a vertex-simple
cycle.

### Theorem 4.1 (alternating-Euler normal form)

For a fixed `d in Q0`, the deletion recursion used in
`connected_alternating_trades(d,r,...)` enumerates exactly all connected
exact-radius-`r` packets with `d in D`.  For a fixed absent edge `a`, the
addition recursion used in `connected_trades_through_added(a,r,...)`
enumerates exactly all such packets with `a in A`.

#### Proof

Every recursion branch is a closed alternating word with `r` distinct blue
and `r` distinct red edges.  The blue edges belong to `Q0`, the red edges do
not, and each visit contributes one incidence of each colour.  Its support is
therefore connected and locally balanced.

Conversely, colour `D` blue and `A` red.  A connected two-coloured graph with
equal blue and red degree at every vertex has an alternating Euler tour.
Pair blue and red half-edges at each vertex.  If the resulting pairing has
several alternating circuits, connectedness supplies a shared vertex at
which two pairings may be crossed, merging two circuits.  Iterate.  Rotate
and orient the final tour so the distinguished edge is first.  The recursion
contains every subsequent choice of that tour.  QED

Combined with Theorem 3.2, enumerating the 61 deleted targets and 276 added
targets, then canonical-deduplicating, is complete for all connected
radius-two, -three, or -four packets with the declared local contact.

The exact physical `q1` filter is also necessary and sufficient for
hole-free lower/upper coverage after factor legality: because
`Q0` already covers every lower and upper colour, only colours carried by a
deleted edge can lose their last provider, and the test uses the exact
integer load

\[
       m_{Q0}(c)-m_D(c)+m_A(c)\ge1
\]

for both palettes.  This does not assert rainbow multiplicity, residence, or
any deeper shadow.

## 5. Sharp degree-closure obstruction

The 22-row artifact is an assumption core, not a complete sparse Farkas
trace through the hard degree equations.  This distinction is decisive.

### Theorem 5.1 (finite audit: degree closure is global)

The deterministic replay

```text
scratch/k16_q0_core22_degree_closure_20260729.audit.json
SHA-256 0061abe4b404ef8137f1ade48c7207d223e504672d94965955be6c4abb265526

scratch/audit_k16_q0_core22_degree_closure_20260729.py
SHA-256 541a3b9597dde30bc0631fffe9cbe2e05bdf70b56e1bc9afa58caf01e57a9615
```

reconstructs both frozen physical factors, without optimization or search,
and proves the following finite statement.

The symmetric-difference graph `R triangle Q0` is one connected component
on all 24,958 overlay variables and 12,867 active middle vertices.  The only
inactive middle vertices are

```text
37833, 43256, 62340,
```

and they are pairwise nonadjacent in `J(16,8)`.  Therefore recursively closing
the current guarded terms under hard degree rows and then taking full
physical row carriers yields every one of the

\[
          |E(J(16,8))|=\frac{\binom{16}{8}\,8\,8}{2}=411840
\]

Johnson edges.

#### Proof

The deterministic replay supplies the one-component assertion, its 24,958
edge and 12,867 vertex counts, and the three inactive masks.  Every current
core term lies in that component.  A hard degree row couples all overlay
variables incident with its vertex, so iterative degree closure reaches all
variables and all active vertices.  The full physical carrier of those degree
rows contains every Johnson edge with an active endpoint.  An edge omitted
from this carrier would have both endpoints among the three inactive
vertices, but the replay also checks that no two of them are Johnson
adjacent.  QED

Consequently this component-closure transport method applied to the available
assumption-core artifact yields no nontrivial local no-go.  Hitting the
732-edge palette carrier or the
2,521-edge one-star breaks verbatim row identity, but only a fresh full
overlay replay, or a newly derived sparse analytic certificate, can decide
the new factor.  A smaller carrier-transport theorem would require an explicit
sparse proof trace through the hard degree rows.

## 6. Complete finite connected radius-four census

The four frozen generator shards are

```text
scratch/k16_q0_core22_local_halo_s0of4_20260729.json
SHA-256 4429cf79bdee1ad71c606e4837381512c216627ac6449406aa36f79dec24b611

scratch/k16_q0_core22_local_halo_s1of4_20260729.json
SHA-256 650ab01c8752db26b991c8984ac9d9bf0bff752b3025297f323b1c1e4c0809f6

scratch/k16_q0_core22_local_halo_s2of4_20260729.json
SHA-256 b991709b99c5ddf9a2f97f0c5f3d9faa42d01c417cdcd1a124a5ce714e775f9e

scratch/k16_q0_core22_local_halo_s3of4_20260729.json
SHA-256 9a05aa4234166918b6321003c108ebf68f78d1ae67009e00f95825fe00e16e6a
```

They bind the executed generator to SHA-256
`f4215c960ef10447c483b91c3f5b17c56f783dfe3e70e53b3617746e4f41959d`.
Each shard has status `PASS_SELECTED_CORE_HALO_SHARD_COMPLETE`, and the four
shard pairs are exactly `(i/4,i/4)` for `i=0,1,2,3`.  Each process had a
1,536 MiB address-space cap, at most four workers plus the parent, and a
10,000 retained-candidate cap.  The retained-candidate cap did not bind: the
four selected-scope ledgers have sizes `272,276,207,196`.  Every shard
completed under the stated per-process address-space limit; no peak-RSS claim
is made.

The separate hash-bound merge and fresh physical replay is

```text
scratch/k16_q0_core22_local_halo_merged_20260729.audit.json
SHA-256 400b5259bbb21508eafe3bb4a260239712ae54e0c20dea767836bd9ae5a6c1c1
```

and has status
`PASS_COMPLETE_CONNECTED_CORE_LOCAL_C4_C6_C8_CATALOGUE`.  The merger itself
has SHA-256
`9a2fc6db839f032087e1101ee94487f13f05524a08cc0cd541adb36d50710a7c`.

### Theorem 6.1 (exact census)

Among connected edge-simple exact packets `(D,A)` with
`|D|=|A| in {2,3,4}`, declared local contact as in Theorem 3.2, and switched
factor `Q=(Q0\D) union A` hole-free on both physical `q1` palettes, there are
exactly 877 packets.  Their radius histogram is

| radius | raw target incidences | `q1`-safe target incidences | distinct packets |
|---:|---:|---:|---:|
| 2 | 623 | 22 | 20 |
| 3 | 25,941 | 136 | 122 |
| 4 | 1,675,767 | 825 | 735 |

The first two numerical columns count incidences with the 61 deletion and
276 addition targets, so the same physical packet can occur more than once.
Only the last column counts canonical physical packets.  Exactly 47 of the
877 packets delete at least one motif-390 closure edge.

#### Proof

Theorem 3.2 reduces complete local contact to the 337 targets.  Theorem 4.1
proves completeness of each target recursion.  The four modulo-four shards
partition both target lists.  Every retained row was replayed from its edge
sets, checked connected and balanced, and checked against the exact physical
lower and upper `q1` ledgers.  Canonical edge-set deduplication gives the last
column.  The executed-code and input hashes, shard partition, uncapped ledgers
ledgers completed without the retained-candidate cap binding, and replay
equality are all assertions of the merged audit.  QED

As a calibration, the merged catalogue contains each previously proved C4
portal exactly once:

```text
motif-390 portal, merged index 19:
  del (25135,29230),(57902,61994)
  add (25135,57902),(29230,61994)

U27742 portal, merged index 246:
  del (25662,27678),(25694,25722)
  add (25662,25722),(25694,27678)

L57614 portal, merged index 206:
  del (57487,57615),(57550,57742)
  add (57487,57550),(57615,57742).
```

The search score, minimized lexicographically only inside this finite class,
is

```text
(motif390 survives,
 -number of rewired guarded rows,
 -number of guarded rows with load at least two,
 -number of contacted guarded palette rows,
 short-run violations,
 physical components,
 radius).
```

Its unique recorded optimum has score `(0,-3,-1,-4,2220,3,4)` and digest
`953c0ed2f5d3de4254143d6a54271b8791d7f3314e61db111bfab69dda590f65`:

```text
del (45838,58126),(57902,57998),(58022,59942),(60166,62214)
add (45838,62214),(57902,58022),(57998,58126),(59942,60166).
```

It destroys motif 390, leaves both physical `q1` palettes hole-free, reduces
the short-run count from 2,222 to 2,220, and has three components of lengths
`13,2185,10672`.  This score does not by itself imply feasibility of the
fixed-resident overlay.
