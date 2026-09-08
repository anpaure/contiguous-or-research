# The `k=17` complement-dual singleton: exact direct-`A` topology LNS

Date: 2026-08-01  
Lane: K  
Status: theorem-level fixed-exterior reduction; the direct-`A` singleton
radius-two face is independently DRAT-UNSAT and its radius-three face is
resource-bounded UNKNOWN.  Neither verdict is an unrestricted `k=17`
obstruction.

## 1. Frozen input and scope

Let `D` be the authenticated quotient incidence matching

```text
scratch/threadD_k17_complement_dual_splice_20260801/seed.best.tsv
SHA256 a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3
```

and put `A=CD`.  Exact replay gives two cycles of lengths `1429,1`; the
singleton owner is `s=425`.  The rank-ten and complementary rank-seven turn
palettes both cover all 1,144 quotient colours, with 286 excess occurrences
on each shore.

Sections 2--6 study only complement-dual replacements of `D` which retain
rank-ten surjectivity and make `A` Hamilton.  The resulting factor is
`A^2`, hence has two quotient cycles, not one.  Sections 7--11 separately
study the frozen non-dual candidate1911 endpoint.  Deletion-spine
feasibility, residence, deeper shadows, opening and the compiler remain
separate gates throughout.

## 2. Relative assignment normal form

Write `A_0` for the frozen permutation.  Every legal direct-`A` arc `e`
has a tail `u` and head `h`.  Contract the frozen assignment by assigning
to `e` the root

\[
                         r(e)=A_0^{-1}(h).              \tag{2.1}
\]

Thus `e` is a possibly parallel directed root arc `u -> r(e)`.  The frozen
arc at `u` is the loop `u -> u`.

### Lemma 2.1 (exchange-cycle normal form)

A selected direct-`A` perfect assignment is equivalent to a permutation
`sigma` of the 1,430 roots, together with one literal parallel arc for every
map `u -> sigma(u)`, and

\[
                         A=A_0\circ\sigma.             \tag{2.2}
\]

Consequently its symmetric difference from the seed is a disjoint union of
directed root-simple assignment cycles.  The direct master's local
incoming-label/outgoing-label inequality is exactly `D cap C(D)=emptyset`.

#### Proof

If the selected arc out of `u` has head `h`, define
`sigma(u)=A_0^{-1}(h)`.  Exactly one selected incoming arc at every head says
that `sigma` is bijective.  Equation (2.2) is then its definition.  Conversely
a literal arc realizing every arrow of a permutation has one outgoing and
one incoming head at every root, hence is a perfect assignment.  Decomposing
`sigma` into cycles gives the last assertion.  The labelled `p!=n` identity
was independently replayed on all 12,870 direct arcs.  \(\square\)

Because `A_0` has two cycles and a Hamilton permutation has one,

\[
 \operatorname{sgn}(A_0)=+1,\qquad
 \operatorname{sgn}(A_{\rm Ham})=-1.                 \tag{2.3}
\]

Hence an odd number of the nontrivial cycles of `sigma` have even length.
In particular, a single Hamiltonizing exchange cycle has even support.  The
literal support-two rectangle is already empty, so support four is the first
possible single exchange.

## 3. Exact singleton balls

Let `G` be the undirected graph obtained from all nonloop root arcs of
Section 2, retaining adjacency but forgetting direction and parallelity,
and let `B_r(s)` be its radius-`r` ball around the singleton.

The radius-`r` LNS leaves free exactly those direct-`A` variables whose tail
and contracted head both lie in `B_r(s)`.  Every other direct-`A` variable is
pinned to its exact seed value.  Thus no selected assignment cycle crosses
the ball boundary.

### Theorem 3.1 (fixed-exterior equivalence)

The satisfying assignments of the restricted CNF are exactly the
complement-dual direct-`A` assignments which:

1. agree with the frozen seed outside the induced assignment graph on
   `B_r(s)`;
2. satisfy the literal `p!=n` rows;
3. cover all 1,144 rank-ten turn colours; and
4. make `A` one Hamilton cycle.

Moreover every single exchange cycle through `s` on at most `2r+1` roots is
contained in this face.

#### Proof

The positive and negative pins fix every exterior or boundary assignment
arc.  Exact one-in/one-out rows then make every change a union of assignment
cycles wholly induced by the released roots.  Conversely every such union
is left free.  The direct base contains the `p!=n`, rank-ten, and exact
Hamilton rows verbatim.

For a root-simple cycle of length `t` through `s`, every cycle vertex is at
undirected distance at most `floor(t/2)` from `s`.  Hence `t<=2r+1` implies
containment in `B_r(s)`.  \(\square\)

The last sentence is deliberately one-way.  An exchange through `s` plus a
disjoint compensation cycle far away need not lie in `B_r(s)` even when its
total support is small.

## 4. The exact direct-`A` base

The base has

```text
95,810 variables
925,391 clauses
12,870 direct-A arc variables
51,480 turn variables
1,144 eager rank-ten rows
```

Its rooted binary-order encoding is equivalent to one Hamilton `A`: owner
zero has order zero; every other owner has nonzero order; every selected arc
not returning to owner zero increments the order by one without overflow;
loops are forbidden.  A separate cycle not containing zero would force a
strict cyclic order increase, while the unique cycle containing zero must
contain all vertices.  No `D <-> H` orientation-breaking row is present.

This last qualification is essential.  The older complement-dual matching
master contains a globally valid orientation symmetry break.  After fixing
the exterior `D` assignment, reversal can leave the LNS fibre, so importing
that symmetry-break row would make an LNS UNSAT verdict unsound.  The runs
below use the direct-`A` base only.

## 5. Radius-two theorem and radius-three boundary

For `r=2`, the contracted graph has 146 released roots and 612 free actual
parallel arc variables.  There are 12,258 pins, giving 937,649 clauses.
Kissat returned UNSAT, and `drat-trim` independently verified the proof:

```text
CNF SHA256   8604ff265946fbaf4601572a854a6a6d1a3df4c6f7d7098714a50c3e1ae9f923
DRAT SHA256  16d7bfd326a4378a2a7eded90a59099fab5d1118075e83226b456a17cdc40054
verification 7,270 core clauses; 2,071 core lemmas; 25,040 resolutions; VERIFIED
```

### Corollary 5.1

No complement-dual, rank-ten-complete direct-`A` Hamilton can be obtained by
any family of exchange cycles wholly contained in `B_2(s)`.  In particular,
no single Hamiltonizing exchange through the singleton has support two or
four.  Therefore a single Hamiltonizing exchange, if it exists, has support
at least six.

For `r=3`, the exact face has 771 released roots, 4,976 free arcs, 7,894
pins, and 933,285 clauses.  A one-core, `nice 15`, 4-GiB, 600-second H100
run ended with exit 124.  Its 2,645,557,248-byte proof prefix is incomplete
and was not verified.  The radius-three status is therefore **UNKNOWN**,
not UNSAT.  This face contains every single exchange through `s` of support
at most seven and hence, by parity, every support-six single exchange.

### Theorem 5.2 (support-six is one ticket short)

An independent solver-free physical assignment-cycle census resolves the
single-support part left undecided by the radius-three timeout.  At support
six it finds

```text
243 geometric assignment cycles through s
120 factor-edge-disjoint strict-dual cycles
37 with A Hamilton
0 with complete rank-ten palette
minimum rank-ten debt 1
```

The best row is candidate 72.  It changes the six `D` rows

\[
 (425,375,1221,1332,655,135),                         \tag{5.1}
\]

makes `A` one 1,430-cycle of voltage 15, and makes `A^2` two 715-cycles,
each of voltage 15.  Its sole rank-ten hole is `0x03e4f`; complement duality
gives the sole rank-seven hole `0x00d87`.  Exact load histograms on both
shores are

```text
load 1: 876 colours
load 2: 248 colours
load 3: 18 colours
load 4: 1 colour.
```

The same exhaustive catalogue closes strict-dual single supports four,
six, and eight: none is rank-ten complete after making `A` Hamilton.
Therefore the next single strict-dual assignment cycle has support at least
ten.  This is a finite-seed theorem, not an all-seed obstruction.

The independently reconstructed factor is

```text
scratch/k17_dual_splice_dev5_independent_20260801/
  seed17931.best_paired_dual.factor.tsv
SHA256 f1d21146512662a54ad0c3811b8a4c901e738c6e3e7c2f42e835017c662134c0
```

## 6. Reproducibility

The proof-generating builder and independent semantic checker are

```text
scratch/build_k17_direct_A_topology_lns_20260801.cpp
scratch/audit_k17_direct_A_topology_lns_scope_20260801.cpp
```

The small frozen audits and verification log are in

```text
scratch/k17_direct_A_singleton_lns_20260801/
```

The large CNFs and proofs remain under

```text
/home/amodo/or15/work/laneK_dual_rectangle_20260801/
```

No GPU and no local heavy process was used.

## 7. The connected one-side shell

The same exact shell census supplies a different, non-dual endpoint.  An
eight-row `H` assignment circuit on

\[
 (425,395,396,665,650,608,157,135)                    \tag{7.1}
\]

gives one quotient factor cycle of length 1,430 and voltage 9, hence one
physical cycle of length 24,310.  Its rank-ten palette is complete.  Its
rank-seven palette has exactly the two holes

\[
                         0x00e0f,\quad 0x01547.        \tag{7.2}
\]

The exact load histograms are

```text
rank 10: {1:878, 2:247, 3:18, 4:1}
rank  7: {1:874, 2:249, 3:18, 4:1}.
```

The independently reconstructed factor is

```text
scratch/k17_dual_splice_dev5_independent_20260801/
  seed17931.minimum_debt_assignment_cycle.factor.tsv
SHA256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

This connected two-ticket endpoint is now the primary topology target.  It
is not a full carrier: only incidence matching, immediate palettes,
quotient topology and voltage have been replayed.

## 8. Sharp remaining move classes

The first undecided strict-dual single exchange has support ten.  The
smallest parity-compatible remote two-switch still has one even
Hamiltonizing support-four cycle through `s` and one odd support-three
compensation cycle elsewhere, for total disjoint support seven.  Such a
remote compensation is not excluded by the radius-two theorem.  Terminal
turns must be reconstructed after both switches; adding their separate
palette deltas is valid only when their affected owner sets are disjoint.

Thus the next exact finite catalogue is sharply scoped:

* on the strict-dual candidate (5.1), find an odd compensation circuit that
  supplies `0x03e4f` without deleting a unique old colour and while keeping
  `A` Hamilton; or
* on the connected non-dual candidate (7.1), find an `H`/`D` circuit that
  supplies both targets (7.2), retains every upper colour, and keeps the
  factor Hamilton with nonzero voltage.

The second route is strictly closer topologically.  A positive result in
either route would still leave deletion-spine/residence, deep shadows,
opening and the common-cap compiler.

### Lemma 8.1 (exact strict-dual one-hole provider section)

For candidate 72, put `U=0x03e4f`.  Exactly 45 quotient turn variables have
upper colour `U`, one for each unordered pair `{p,n}` contained in a fixed
physical representative of `U`.  Indeed the corresponding rank-nine owner
is

\[
                  a=\overline{U\setminus\{p,n\}},                 \tag{8.1}
\]

and the `Z_17` orbit of `U` is free, so canonicalization identifies no two
of the 45 pairs.  Each turn has exactly two literal orientations,

\[
       (\hbox{incoming }p,\hbox{ outgoing }n),\qquad
       (\hbox{incoming }n,\hbox{ outgoing }p),                    \tag{8.2}
\]

giving 90 ordered provider arc-pairs.  Every strict-dual repair of the one
hole selects at least one of these pairs.

This gives a proof-safe provider-halo formulation.  Contract the candidate72
seed arcs, seed the root set with all relative endpoints of the chosen
provider pair (or branch over the 90 pairs), take a ball in the nonloop
direct-`A` assignment graph, free precisely the arcs whose two contracted
endpoints lie in that ball, and pin all other arcs.  The exact direct-`A`
master retains permutation, `p!=n`, all 1,144 rank-ten rows and Hamilton
`A`; strict duality supplies the complementary rank-seven row.  Unlike the
fixed-`D` model below, the turn condition is genuinely quadratic in the two
incident arcs, so Theorem 9.1 cannot be imported.

Independent map replay finds 89 distinct relative roots among all provider
pairs.  The union-provider balls have the exact sizes

| radius | roots | free direct-`A` arcs |
|---:|---:|---:|
| 0 | 89 | 298 |
| 1 | 706 | 4,316 |
| 2 | 1,422 | 12,737 |

Branching on one ordered provider pair is substantially sharper: at radius
one a branch has 42--64 roots and 102--176 free arcs; at radius two it has
339--643 roots and 1,711--3,537 free arcs.  These counts show that the
90-branch formulation, rather than the nearly global union radius-two ball,
is the natural next exact solve.

The radius-zero **union-provider** face is exact and UNSAT.  It leaves all
298 direct arcs induced by the 89 provider roots free and pins the other
12,572 arc variables (1,341 positively and 11,231 negatively) to candidate
72.  The resulting exact direct-`A` formula has 95,810 variables and 937,963
clauses.  Kissat returned UNSAT and `drat-trim` independently returned
`s VERIFIED`; the extracted core has 1,987 input clauses and one lemma and
is unit-propagational.

Thus no strict-dual repair wholly supported on the induced 89-root provider
section can fill the complementary hole pair while retaining Hamilton `A`
and all immediate colours.  This does **not** exclude a return circuit that
leaves those roots.

The radius-one union-provider formula has 95,810 variables and 933,945
clauses.  Its one-core 300-second run exited 124 with empty stdout, no model
and no UNSAT line.  The 1,040,187,392-byte partial proof was renamed
`.INCOMPLETE`, was not verified, and is non-evidentiary.  Radius one is
exactly `UNKNOWN`.  The 90 smaller provider branches, remote compensation,
residence and every deeper gate remain open.

```text
scratch/audit_k17_candidate72_strict_dual_provider_halo_20260801.py
SHA256 418ecce53abea65beb3cc87ee4eb0904fbe25aa375197504075c5e5dd13ed045

scratch/k17_candidate72_strict_dual_provider_halo_20260801.audit.json
SHA256 298ab9480f6439693e60ab90bdfe8f19c04452124f5537abefda7b09ba28df1c

scratch/k17_candidate72_strict_dual_provider_halo_r0_20260801.units
SHA256 1cb449f074491b8d09f9bd7b2e9bc8173289878312d6a53772a6e9122be32865

remote radius-zero CNF / DRAT / verification log SHA256
fa151d1525ac0dae50bd387dc3e567bfde0f17c17e2b7ef78c3081cd14348998
03a017e06d5d39dfdb31865ddaf3973e6333af619d374b3a3b4d0c6922d5773d
08436c823eb276a18f40e9118c4d243daa2cd28236b8bbc5a74e157afbfc14a7

extracted core SHA256
1d3dff0a997b33e7c3d6239bb1d0763d0d65cdd3ddd64de59a75bcc802fbce34

radius-one CNF / incomplete proof prefix SHA256
7b43e889b0ea23a65d0f65f559e91c3603104fca34bbf1a0f415283f0dd1f304
61b30d9443baadba51a2188fe7eefce3507062dd2ce2c7bca06f50f03d3ca23f
```

## 9. Exact fixed-`D`, one-`H`-matching repair master

Candidate (7.1) has a useful linearization which is stronger than a generic
two-factor formulation.  Freeze `D` and vary only the second incidence
matching `H`.  For an incidence `e=(u,f,s)`, let `d_u=D(u)` and let
`d^f=D^{-1}(f)`.  In the gauge of `u` and `f`, respectively, define

\[
 \ell(e)=Q(d_u)\cap Q(e),\qquad
 u(e)=T(d^f)\cup T(e).                               \tag{9.1}
\]

Here `Q` is the aligned rank-eight facet and `T` the aligned rank-nine
owner.  An edge with `e=d_u` is forbidden.  Every remaining edge has
`rank(ell(e))=7` and `rank(u(e))=10`.

### Theorem 9.1 (linear palette master)

With `D` fixed, a selected incidence matching `H` has complete immediate
lower and upper palettes if and only if

\[
 \begin{aligned}
 &\sum_{e\ni u}h_e=1 &&\text{for every owner }u,\\
 &\sum_{e\ni f}h_e=1 &&\text{for every facet }f,\\
 &\sum_{e:\ell(e)=L}h_e\ge1 &&\text{for every rank-seven orbit }L,\\
 &\sum_{e:u(e)=U}h_e\ge1 &&\text{for every rank-ten orbit }U,
 \end{aligned}                                                   \tag{9.2}
\]

together with `h_(D(u))=0`.  No turn-conjunction variable is needed.

Moreover an edge `e=(v,f)` induces the factor arc

\[
                       D^{-1}(f)\longrightarrow v.                \tag{9.3}
\]

Thus the selected `H` is quotient-connected exactly when the arcs (9.3)
form one Hamilton permutation.  Rooted order variables or ordinary subtour
cuts give an exact topology row.

#### Proof

At owner `u`, the two factor incidences are `D(u)` and the unique selected
`H` edge out of `u`; their intersection is precisely `ell(e)`.  At facet
`f`, the two inverse matching incidences are the fixed `D` edge and the
unique selected `H` edge at `f`; their union is `u(e)`.  Hence every
selected `H` edge contributes one fixed label on each shore, proving (9.2).
Following `D` from `D^{-1}(f)` and then `H` backwards from `f` ends at the
owner of `e`, proving (9.3).  \(\square\)

For candidate (7.1), each missing lower target has exactly ten raw one-edge
providers in this master.  The next proof-safe LNS contracts the current
`H` assignment, releases those provider arcs and an incidence-alternating
return halo, pins the exterior, retains all rows (9.2), and imposes the exact
Hamilton condition (9.3).  SAT must still replay voltage and all physical
phases; UNSAT closes only that provider halo.  This is the precise targeted
replacement for another generic singleton-ball solve.

## 10. Exact one-circuit provider no-go through support nine

There are exactly ten direct providers for each target in (7.2) on each
choice of the moving shore `D` or `H`, hence 40 typed provider arcs.  A
complete global catalogue starts a simple relative matching cycle at each
such arc, retains every parallel incidence, and deduplicates only cyclic
rotations of the same literal owner-edge assignment.

For one moving shore and cycle length at most nine, the exact counts are

| support | provider-containing cycles | upper-safe | connected and upper-safe |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 3 | 3 | 0 | 0 |
| 4 | 18 | 1 | 0 |
| 5 | 90 | 2 | 0 |
| 6 | 528 | 8 | 0 |
| 7 | 3,383 | 21 | 6 |
| 8 | 22,512 | 81 | 0 |
| 9 | 154,929 | 260 | 36 |

All 181,464 terminal assignments are replayed as literal `D/H` matchings.
None of the 42 connected upper-safe rows at supports seven and nine fills
both lower holes.  In fact the minimum terminal lower debt is still two.
The best support-nine row merely transports

\[
       \{0x00e0f,0x01547\}\longmapsto
       \{0x00755,0x01547\}.                         \tag{10.1}
\]

The catalogue was then extended in a second, clean-exit run by retaining
only cycles which directly gain **both** missing lower targets.  This is a
necessary condition for any one-circuit exact repair.  Over supports
`3,4,5,6,7,8,9,11` on both moving shores it finds

```text
68,456 targeted literal cycles
68,456 factor-edge-disjoint cycles
8,073 connected nonzero-voltage cycles
0 terminal two-palette survivors.
```

Support eleven alone contributes 41,704 targeted H cycles and 25,160
targeted D cycles.  Four H rows and two D rows are upper-safe; none is also
lower-safe.  Supports ten and twelve are excluded by the Hamilton sign row,
not skipped heuristically.

### Corollary 10.1

No single one-shore matching circuit of support at most eleven repairs
candidate (7.1) while retaining quotient connectedness and all upper
colours.  Since both the initial and terminal factor permutations are
Hamilton, a single relative assignment cycle must have odd support.
Therefore the next one-circuit support is at least thirteen.

The exact finite result does **not** exclude two disjoint relative cycles,
simultaneous changes of `D` and `H`, or a support-thirteen-or-larger circuit.
Those are precisely why the multiple-cycle provider-halo master of Section
9 remains live.

Frozen result:

```text
scratch/k17_candidate1911_targeted_repair_20260801/audit9.json
SHA256 f840b2d504f36019464a35ff9f043aba596de0a94c3668bfcec470af563510e1

scratch/k17_candidate1911_targeted_repair_20260801/result9.tsv
SHA256 836f72ae8aa84689f1911460761764f6c77f524fa3ffbef09177a5241a18294a

scratch/k17_candidate1911_targeted_repair_20260801/
  clean.second_circuits_B.audit.json
SHA256 936dfd01dc7c3f44a44536ca518a0a8bf56e034e885f30d175d47f6a5e25b499

scratch/k17_candidate1911_targeted_repair_20260801/
  clean.second_circuits_B_summary.tsv
SHA256 c40db77b5a0523cddf2c631350886e277150dfdb11b2fd67af41be66f73382d7
```

### Corollary 10.2 (the frozen-relative two-rectangle face)

There are 19 literal `D` rectangles and 20 literal `H` rectangles in
candidate (7.1).  An independent terminal replay closes every pair of
rectangles defined relative to the frozen factor: same-shore pairs with
disjoint owner pairs, and arbitrary-overlap mixed `D/H` pairs.  The mixed
census has 380 raw pairs, 336 terminal edge-disjoint pairs, 156 connected
factors, 15 upper-complete factors, and zero lower-complete factors.  Only
18 rows gain either original hole, and every one gains `0x00e0f` alone.

This does not by itself enumerate a sequential second same-shore rectangle
defined relative to the intermediate matching.  A one-owner overlap is a
three-owner assignment circuit and is covered by the separate one-circuit
census above.  Same-pair sequential returns were independently replayed
(17 `DD`, 18 `HH`) and gain neither hole.  Thus the exact conclusion is a
frozen-relative two-rectangle no-go, not an unrestricted two-circuit no-go.

```text
MATH_AUDIT_K17_CANDIDATE1911_MIXED_TWO_RECTANGLE_INDEPENDENT_20260801.md
SHA256 d3e3f62ffe2986f9a57663f4acd21c808957e890953c36095a449ad21496b0f2

independent audit JSON SHA256
b6c003f3a2dc0dc8817d573d1aa5d747fbc1488ebe46f7e9bc15a59490d7b746
```

## 11. Multiple-cycle provider-halo LNS

The master of Theorem 9.1 was implemented directly.  Its exchange graph
contracts the frozen `H` matching.  Crucially, an incidence already used by
fixed `D` is globally forbidden and is excluded from the BFS adjacency as
well as from the free/pinned H-edge census.  Including such edges in the BFS
would not change the CNF's satisfying assignments, but would falsely enlarge
the claimed geometric halo and invalidate a minimal-radius interpretation.

The twenty H-side provider edges for (7.2) have 34 distinct contracted
endpoint roots.

### Theorem 11.1 (radius-one fixed-`D` halo is UNSAT)

At radius one the exact induced halo has

```text
332 released roots
1,356 feasible free H incidences
2,600 boundary incidences
1,098 positive exterior pins
8,986 negative exterior pins
44,330 variables
659,786 clauses.
```

The model contains exact H owner/facet matching, all lower and upper palette
rows, and the rooted Hamilton encoding (9.3).  Kissat returned UNSAT.
`drat-trim` independently verified the proof; its extracted core has only
686 clauses and one lemma and is itself unit-propagation UNSAT.

The core has a transparent terminal conflict.  Its unit closure forces 685
edge literals (71 true and 614 false).  It then forces both incidence 3515
and incidence 3830 at facet 315, contradicting that facet's AMO clause
`(-3516,-3831)`.  The complete reason closure uses 34 lower-palette rows,
27 upper-palette rows, eight facet ALOs, two owner ALOs, 93 matching AMOs,
ten fixed-D forbiddances, and 511 exterior negative pins.  Thus the small
core is a genuine coupled matching/palette obstruction, not an MTZ-only
topology artifact.

```text
CNF SHA256
014b7d3d6fd96ef887d38af1a8645bb20d4f10f0357e497cd6b7fe80575f1a1a

full DRAT SHA256
8290784b5cca107fb283bf438da494492265b73e56da5ae93e1f1a256435740f

verification log SHA256
f7c64b407a3e67ca96629fe9b2ec09acc87fe64a12a4fa23d95ae03f3b883858

core CNF / core DRAT SHA256
10e2647bb518ce69e800880b3b932d8c394e948c576337977e62447ccc90a08b
6e5b856bb4b3d7cac627883d30abc7843dd6e33c80a5fded53cd08647ef5d4e5
```

This excludes arbitrary **multiple** relative H cycles contained in the
radius-one provider halo, not merely one short circuit.  It is still a
fixed-`D`, fixed-exterior theorem.

### Radius-two boundary

At radius two the exact halo has 1,266 released roots and 9,246 free H
incidences; the master has 44,330 variables and 651,896 clauses.  Its CNF
SHA is

```text
0df97e669bdcda42a8d05fed3ad41fb9595429646b1f3fa7ae4c9426d29b8934.
```

The single-core H100 run reached its 300-second cap with exit 124, no model,
no UNSAT line and no proof.  Radius two is exactly **UNKNOWN**.  No larger
halo was launched.

Frozen implementation and small audit package:

```text
scratch/build_k17_fixed_D_H_palette_halo_master_20260801.cpp
SHA256 475a9542cf9f71311ac48bf7287d3374a14d69b627a0af6718e6e48f865ff7ed

scratch/k17_fixedD_H_provider_halo_20260801/

independent scope checker SHA256
949260250cc84d3335878b09325f7cc6f5cfb1b5471c165f759298189b013c25

independent core classifier SHA256
5f67ff30c7297649c1866e289a2c9984a19ef59e871a2dedc8472340a2c4ee89
```

## 12. Proved boundary

For the frozen seed, all of the following are now exact.

1. No support-two D/H cross rectangle exists.
2. No strict-dual single assignment cycle through support eight gives an
   A-Hamilton, complete-palette seed; candidate 72 is one ticket short.
3. Candidate 72 has no repair in its induced radius-zero union-provider
   face; the radius-one provider branches remain open.
4. Candidate 1911 is a connected, nonzero-voltage, upper-exact factor with
   exactly two lower tickets missing.
5. No one-shore single circuit through support eleven repairs candidate
   1911.
6. No pair in the frozen-relative two-rectangle face repairs candidate
   1911; the sequential-overlap qualification is stated in Corollary 10.2.
7. No arbitrary collection of H exchange cycles confined to its radius-one
   typed-provider halo repairs it with fixed D.

The first unclosed finite faces are the radius-two fixed-D H halo, a
support-thirteen-or-larger one-shore circuit, simultaneous D/H changes, and
the candidate72 radius-one provider branches or a return circuit leaving its
radius-zero provider section.  Every positive immediate-palette result would
still require residence/deletion-spine, deeper-shadow opening and compiler
replay.
