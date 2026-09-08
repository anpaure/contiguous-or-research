# The five PBBS motifs at (k=16): exact rethread and cut frontier

Date: 2026-07-29

This note records an exact finite result for the rank-seven (B)-shore in
the (15\to16) lift.  It closes the previously isolated set of 75 locally
locked short runs.  It does **not** yet give a (k=16) word: the remaining
gate is the global braid of the resulting (B)-segments with a resident
rank-eight (A)-shore.

## 1. The centered PBBS baseline

Square the canonical PBBS permutation on the rank-seven subsets of
\([15]\).  The result is a Johnson 2-factor with

* 6435 states in 73 physical cycles;
* all 5005 rank-six intersection colours present;
* rank-six load histogram
  \(1^{3630}2^{1320}3^{55}\);
* every rank-eight union colour present exactly once; and
* positive-run histogram below the required residence four
  \[
      2^{90}3^{855}.
  \]

For a positive run of length three, call its two internal Johnson edges
*available* when at least one of their rank-six colours has multiplicity at
least two.  Exactly 75 runs are unavailable.  Normalizing the distinguished
coordinate to zero shows that these are precisely five
\(\mathbb Z_{15}\)-orbits, each of size 15.  Thus the exceptional set is a
five-motif phenomenon, not 75 unrelated accidents.

The independent baseline census is
[`scratch/audit_k16_pbbs_shore_20260729.py`](scratch/audit_k16_pbbs_shore_20260729.py).

## 2. A small equivariant rethread closes the local obstruction

The arity-three catalogue consists of exact zero-endpoint-boundary circuits
in the quotient sigma model.  Such a circuit changes three lower-orbit
choices while preserving degree two at every middle orbit.  The following
eight catalogue rows are pairwise label-disjoint:

\[
  602,667,705,740,249,308,609,765.                 \tag{2.1}
\]

They change only 24 of the 429 quotient choices.  Direct lifting and a
physical audit give:

* 63 physical cycles;
* all 5005 rank-six colours, with the same load histogram
  \(1^{3630}2^{1320}3^{55}\);
* no hole in any fixed-window lower or upper shadow depth;
* short positive-run histogram
  \[
      2^{105}3^{840};                              \tag{2.2}
  \]
* no length-one run; and
* every run counted in (2.2) has a repeated-colour internal edge.

In particular, the original five locked motif orbits disappear without
losing any q1 colour.  Each of the eight circuits is checked independently
to have zero endpoint boundary, and all 24 labels are checked distinct.

The canonical certificate is
[`scratch/k16_pbbs_special_motif_eight_trade_20260729.json`](scratch/k16_pbbs_special_motif_eight_trade_20260729.json),
SHA-256

```text
5f84d9da5c97e42a53a9873af3ca4e4df23087d335e6b5a838db55c5342a1b80
```

and the independent verifier output is
[`scratch/k16_pbbs_special_motif_eight_trade_20260729.audit.json`](scratch/k16_pbbs_special_motif_eight_trade_20260729.audit.json),
SHA-256

```text
3f648a2ad1f6b6c8be550f354fd0c0962878ef205d92dedb22622989fd07b7fe
```

Reproduction:

```bash
python3 scratch/build_k16_pbbs_special_motif_eight_trade_certificate_20260729.py \
  --output scratch/k16_pbbs_special_motif_eight_trade_20260729.json
python3 scratch/audit_k16_pbbs_special_motif_trade_certificate_20260729.py \
  --output scratch/k16_pbbs_special_motif_eight_trade_20260729.audit.json
```

## 3. Internal cuts are unnecessarily restrictive

If cuts are required to lie strictly inside every short run, the exact
capacitated hitting problem is infeasible.  Even before component opening,
spacing, or rung constraints, its optimum leaves 30 length-three runs
unhit.  This is a valid no-go only for the strict internal-cut subclass.

For the actual braid a short run becomes terminal as soon as **any** edge in
its cyclic closure is cut.  The two boundary edges are therefore legal: the
rung collar extends the terminal run.  This distinction is load-bearing.

## 4. Exact full-closure cut certificate

Use all boundary and internal edges of each short run as its hitting set.
Under the exact rank-six capacities (at least one occurrence of every colour
must remain), the minimum number of cuts is 585.  Requiring cyclic segment
length at least three remains feasible.  Among these solutions, the exact
minimum number of length-three segments is 45.  One optimum has

\[
  3^{45}4^{249}5^{221}6^8 7^{16}8^{20}9^{11}15^{15}.       \tag{4.1}
\]

All 5005 q1 colours survive.  In particular, (4.1) supplies 249 four-state
segments.  A separate direct-COMP3 lemma shows that any such internal
four-state (B)-segment becomes an exact singleton-\(\{z\}\) channel once
its two flanking incidence rungs are legal; no older trace-language filter
is required.

The certificate is
[`scratch/k16_pbbs_eight_trade_fullclosure_minshort_20260729.json`](scratch/k16_pbbs_eight_trade_fullclosure_minshort_20260729.json),
SHA-256

```text
b5021560b76f368c56adb45d92746f9059159d4920f55a4ffe044a1b0f643214
```

generated on the H100 host CPU by

```bash
python3 scratch/solve_k16_pbbs_eight_trade_internal_cuts_20260729.py \
  --certificate scratch/k16_pbbs_special_motif_eight_trade_20260729.json \
  --base scratch/k15_pbbs_trade_baseline.json \
  --output scratch/k16_pbbs_eight_trade_fullclosure_minshort_20260729.json \
  --cut-scope full --no-open-components --min-segment 3 \
  --require-ear --minimize-short-segments
```

## 5. Port matching and the partial macro are exact, but not yet compatible

Against the resident rank-eight factor with component lengths (6390) and
(45), the 1170 endpoints of the 585 certified (B)-segments admit an exact
incidence-port matching to 585 cuts of the long (A)-cycle.  Fixing those
ports, a second exact solve joins the resulting 585 (A)-segments and 585
(B)-segments into one alternating macro cycle.  Thus endpoint supply,
integrality, and macro connectivity are not obstructions.

The corresponding certificates are
[`scratch/k16_pbbs_segment_a_port_matching_20260729.json`](scratch/k16_pbbs_segment_a_port_matching_20260729.json)
and
[`scratch/k16_pbbs_fixed_port_macro_cycle_20260729.json`](scratch/k16_pbbs_fixed_port_macro_cycle_20260729.json),
with SHA-256 values

```text
c9c53bfe7fb416cba0b7329d2374d4e6abd44a2729c0c65f9adfe9786f88dd4b
b2f7869b9916156ce18117a0f856b7ce94dd4c408e26422ed2e0570736e01256
```

The resulting macro contains 9270 states.  Its arbitrary incidence rungs
are **not** shadow-safe: they introduce short residence runs and destroy
q1 colours.  Hole counts from that 9270-state object alone are not factor
statistics, because it omits the small 45-state (A)-cycle and 37 untouched
(B)-cycles.

The authoritative audit restores every omitted owner, giving the complete
12870-state 2-factor with 39 components.  It has

* no lower-q1 holes;
* 533 upper-q1 holes;
* lower/upper q2 holes (195/426);
* lower/upper q3 holes (73/33);
* lower/upper q4 holes (4/0), and no holes at deeper ranks; and
* 971 positive residence violations (lengths below four), including the 45
  unavoidable length-three (z)-runs.

The full audit is
[`scratch/k16_pbbs_full_macro_factor_20260729.audit.json`](scratch/k16_pbbs_full_macro_factor_20260729.audit.json),
SHA-256

```text
1196cdb1c834787214074978a5be96363c3a4e576acba801ff6632eefdd58511
```

This separates two statements that must not be conflated: the port/macro
flow problem is solved exactly, but arbitrary legal rungs do not preserve
the shadow-and-residence structure needed by the lift.

## 6. A scoped no-go for cut-first optimization

A longer chain of 19 additional zero-boundary arity-three trades reduces the
(B)-factor from 63 components, 20 of which have no repeated q1 edge, to 21
components with only one such component.  The resulting factor still covers
all 5005 lower-q1 colours and has no internally locked short run.

If the cuts are then optimized *before* seam reachability is represented, the
exact lexicographic optimum (lost lower-q1 colours, length-three segments,
cuts) opens all 21 components with 552 cuts.  It has 60 length-three segments
and loses 16 lower-q1 colours.  This looks better than (4.1), but it is not a
jointly feasible interface.

Indeed, enumerate every genuine (B)-to-(B) Johnson seam between the 1104
exposed endpoint states.  Of the 16 lost rank-six colours, 15 have no seam of
that colour at all; the remaining colour has two candidates.  Since an
(A)-to-(B) rung has an old rank-seven lower colour, neither it nor an
(A)-to-(A) seam can restore a missing (z+)rank-six colour.  Therefore:

> **Fixed-cut no-go.**  No rewire of the 552-cut certificate, using arbitrary
> AA, AB, and BB Johnson seams, can have complete lower-q1 support.

This is a theorem about that fixed cut certificate, not about the 27-trade
factor.  It identifies the required correction: cut selection and BB
restoration must be solved together.  The strengthened cut model makes every
lost colour admit a simultaneously selectable, vertex-disjoint BB restoring
seam before minimizing the remaining objectives.

The strengthened model is feasible and solved to optimality.  Its exact
lexicographic optimum has 17 lost lower-q1 colours, 60 length-three segments,
and 567 cuts.  All 17 lost colours are simultaneously restored by 17
vertex-disjoint BB seams.  Thus seam reachability costs exactly one additional
lost colour and 15 additional cuts relative to the unreachable optimum, while
the number of mandatory short-segment BB attachments remains 60.  The
certificate is
[`scratch/k16_pbbs_component27_bbrestorable_cuts_20260729.json`](scratch/k16_pbbs_component27_bbrestorable_cuts_20260729.json),
SHA-256

```text
3ed33e6a32cbf3e93beccd183f85deb439f3bac43d015422e14bbb260ccf5f27
```

The unreachable fixed-cut certificate is
[`scratch/k16_pbbs_component27_joint_ready_cuts_20260729.json`](scratch/k16_pbbs_component27_joint_ready_cuts_20260729.json),
SHA-256

```text
8c4bbb12d96646e6077c6a54b1efa2d8974b0681e6dd5681c4fbc030a81c8418
```

There is a second, independent reachability condition on the upper shore.
The resident (A)-factor's rank-nine edge-colour loads are

\[
  1^{3675}2^{1230}3^{100}.
\]

Consequently 2220 of its 6435 states have no incident edge that can be cut
without deleting the last occurrence of an old rank-nine colour.  In the
567-cut lower-restorable certificate, exactly 62 cut (B)-upper colours
\(z+U\) have both of the following properties:

* the exposed (B)-ports admit no BB seam of union (U); and
* the (A)-state (U) has no safe incident cut edge.

Those 62 colours cannot be restored by any AB+BB rewire.  This remains true
after dropping the length-three, A-component-opening, and cut-spacing
constraints: lower q1 alone is feasible, while upper q1 alone is infeasible.
Thus upper reachability must also be built into the cut solve.  The current
strengthened model requires a selected BB seam whenever a cut B-upper colour
has no safe A incident edge.

## 7. Exact remaining gate

### Relation to the strict equivariant bilayer model

The independent `biword.py` model in the Opus work directory gives an exact
normal form for a much narrower class: a unit-voltage, single-cycle,
\(\mathbb Z_{15}\)-equivariant bilayer encoded by one low-coordinate trace
\(c\in\{0,1\}^{12870}\) and one top trace
\(t\in\{0,1\}^{858}\).  Its class-sum, start/end, and run constraints make
Johnson adjacency and residence automatic, but it must still solve two
simultaneous zero-spare necklace bijections and every shadow decoration.
No k=16 certificate for that strict class is currently present.

The PBBS macro route is more general: its two shores are already resident
exact factors, and equivariance is used only to obtain exact local trades.
Its remaining variables are exposed ports and seams rather than a global
12870-bit trace.  Consequently the strict bilayer CEGAR engine should not
replace the present model.  Three pieces do transfer:

1. its q1 arithmetic proves that every top-q1 target needs a BB seam;
2. `lift5.py`'s prefix/suffix collar tables independently implement the same
   seam-residence test used by the fixed-segment successor model; and
3. its witness-interval kill index is the natural extension for auditing
   q2 and higher shadows after q1+residence feasibility is obtained.

Two further facts prevent (4.1) from being called a finished shore braid.

1. Requiring all segments to have length at least four is infeasible.  The
   45 length-three segments in (4.1) are optimal inside this cut model.  They
   must be joined to another (B)-piece by a shadow-safe (B\)-to-\(B)
   rethread, or absorbed by a wider collar construction.
2. Only 26 of the 63 physical cycles are cut in (4.1).  Twenty physical
   cycles contain no repeated q1 edge at all, so the pure-delete model cannot
   open them without losing a colour.  These cycles need colour-restoring
   (B\)-to-\(B) splices, not additional deletion capacity.

Thus the exact state after the five-motif repair is

\[
\boxed{
  \text{local motif lock solved}
  \;\Longrightarrow\;
  \text{capacitated segment cover solved}
  \;\Longrightarrow\;
  \text{global colour-restoring macro braid open}.
}
\]

The next finite object should combine the 585 certified cuts with
shadow-preserving (B\)-to-\(B) splices and incidence rungs to the resident
two-component rank-eight (A)-factor.  The final audit must simultaneously
check both shores' residence, all q1 colours, macro connectivity, and the
common exact `COMP3` compiler.

## 8. The cut and cross pattern must be chosen simultaneously

The 27-trade enlargement of the (B)-shore reduces its source factor to 21
components while retaining complete q1 support and eliminating every sealed
short-run lock.  It also makes the failure of the sequential interface exact.
Three progressively strengthened cut-first certificates were tested:

* 552 cuts, 16 lost lower colours, and 60 length-three segments: 15 of the
  lost colours have no exposed BB restoring seam;
* 567 cuts, 17 lower-restorable colours, and 60 length-three segments: 62
  lost upper colours have neither a BB restorer nor a safely exposable
  (A)-port; and
* 596 cuts with simultaneous lower/upper reachability and an explicit BB
  attachment available for every selected length-three segment: after fixing
  those cuts, lower q1 and upper q1 are each separately infeasible in the
  restricted AB+BB port matching.

The last statement is not an obstruction to the 27-trade factor.  It proves
that even reachability summaries are weaker than the paired port Hall
conditions.  Independently, fixing the cross-shore pattern of the best direct
factor and allowing arbitrary same-shore replacement seams is infeasible for
residence plus both q1 palettes.  Thus neither cuts nor the cross pattern may
be selected first.

The current exact model
[`scratch/solve_k16_pbbs_joint_cut_seam_q1_20260729.py`](scratch/solve_k16_pbbs_joint_cut_seam_q1_20260729.py)
selects both shores' cuts and the state-level seam matching in one CP-SAT
instance.  In its no-AA form it has

\[
  51{,}480\ \mathrm{AB}+173{,}745\ \mathrm{BB}=225{,}225
\]

seam variables, 12,870 cut variables, and 6,435 length-three indicators,
for 244,530 primary Booleans.  It enforces component opening, distance-three
cut spacing, every full short-run closure, exact exposed-state degree, both
physical q1 palettes, and a selected BB attachment for every selected
three-state (B)-segment.  Old-coordinate seam residence and connectivity are
deliberately deferred to the smaller fixed-segment successor.

The first unhinted no-AA run returned `UNKNOWN` after 1806.46 seconds: it
found no incumbent but proved no infeasibility.  Its report is
[`scratch/k16_pbbs_joint_cut_seam_q1_noaa_unhinted_unknown_20260729.json`](scratch/k16_pbbs_joint_cut_seam_q1_noaa_unhinted_unknown_20260729.json),
SHA-256

```text
22358704e898f3369b3920caad89e588b17dcc3600a8764ffb37717fe13fc488
```

A complete/partial-hint retry and the controlled AA relaxation are the next
finite tests.  AA is a legitimate extension rather than an ad hoc escape:
the independently verified k=14 braid uses a genuine AA seam.  No length
12,873 word is claimed until a joint scaffold passes the fixed-segment
all-coordinate residence/connectivity audit and the universal compiler plus
exhaustive verifier.

For calibration, independently materializing the 596-(B)-cut/566-(A)-cut
geometry-only warm scaffold gives 420 lower-q1 holes and 756 upper-q1 holes.
Their split is

\[
  H_7=(403\text{ without }z)+(17\text{ with }z),\qquad
  H_9=(317\text{ without }z)+(439\text{ with }z).
\]

Thus that artifact is a valid geometric seed, not a near-q1 certificate.  A
successful simultaneous solve must perform a global reorganization; local
repair around the saved seam matching is not expected to close 1,176 holes.

With the cut counts fixed at 566 and 596 but their positions and all seams
free, a soft-q1 solve improves this to 204 lower and 459 upper holes.  The
independent replay has six components, no short run of the new coordinate,
but 953 old-coordinate residence violations.  The artifact is
[`scratch/k16_pbbs_joint_cut_seam_softq1_counts566_596_20260729.json`](scratch/k16_pbbs_joint_cut_seam_softq1_counts566_596_20260729.json),
SHA-256

```text
8c9364c192391cbac8db1d196d39609e523585fecac9f3497a7f6163366b44f6
```

Freezing the improved 566/596 cuts obtained by a ten-minute soft-q1 solve is
still impossible before any Hall subtlety: its residence-safe oriented-port
graph has 441 zero-degree ports in the no-AA class (347 A and 94 B).  Adding
all genuine AA seams leaves 141 zero-degree ports (47 A and 94 B).  The exact
fixed-segment q1+residence model consequently proves infeasibility in
presolve.  This is a statewise certificate that residence must participate in
cut selection rather than being imposed on a saved cut pattern.
The fixed-cut infeasibility report has SHA-256
`c87ff4606430ff9ebf02e4dcafbfb03f2ca81cec87c40f343674d87475478f0d`.

The correct integrated variables are **oriented cut-edge ports**.  Each
possible factor-edge cut creates its left and right endpoint ports; the port
orientation fixes the surviving segment direction and therefore its terminal
run profile through radius three.  Residence-incompatible seams can then be
deleted before search, while a selected pair of cuts at distance three gets
an exact per-coordinate extension constraint.  The resulting global census is

\[
\begin{array}{c|r|r|r|r}
 &\text{ports}&AA&AB&BB\\ \hline
\text{no-AA}&25{,}740&0&88{,}155&175{,}935\\
\text{AA allowed}&25{,}740&222{,}375&88{,}155&175{,}935
\end{array}
\]

and there are zero globally dead ports in both rows.  Thus full old-coordinate
residence raises the seam count only from 225,225 state-level candidates to
264,090 no-AA oriented candidates; it does not cause an exponential blow-up.
The exact implementation is
[`scratch/solve_k16_pbbs_oriented_port_joint_residence_q1_20260729.py`](scratch/solve_k16_pbbs_oriented_port_joint_residence_q1_20260729.py).

The first ten-minute no-AA soft-q1 run of this integrated model is feasible.
Its independently replayed 12,870-state factor has seven components of lengths

```text
380, 410, 769, 1107, 1314, 3986, 4904
```

and **zero residence violations in all 16 coordinates**.  It uses 510 A cuts,
1702 B cuts, 1020 AB seams, and 1192 BB seams.  Its q1 deficit is still large:
758 lower and 993 upper holes.  This is not a lift certificate, but it is the
first object in this lane that solves the previously incompatible global
rethreading and all-coordinate residence gates in one exact factor.  The
artifact is
[`scratch/k16_pbbs_oriented_noaa_softq1_20260729.json`](scratch/k16_pbbs_oriented_noaa_softq1_20260729.json),
SHA-256

```text
50c3c3786762907b67281142e33cf69c2d476282b0e1bb70a6e74a6fb43c6cbf
```

The live residual is now quantitative and honest: reduce 1,751 q1 holes to
zero while retaining the oriented-port residence constraints, then connect
the seven components and run the universal compiler/verifier.

A second ten-minute solve, warm-started from that resident factor, improves
the same exact model to **two components** of lengths 4,435 and 8,435, still
with zero residence violations.  Its q1 deficit is 492 lower plus 698 upper,
for 1,190 holes total.  It uses 386 A cuts, 1,627 B cuts, 772 AB seams, and
1,241 BB seams.  The artifact is
[`scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json`](scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json),
SHA-256

```text
d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
```

This establishes genuine descent inside the fully resident class: one warm
round removes 561 q1 holes and reduces seven components to two.

### Overlay trade test against the q1-perfect endpoint

The resident factor and the independently audited q1-perfect equivariant
factor share only 392 physical edges.  Their symmetric difference is one
connected support on 12,869 vertices, but degree-four vertices admit many
alternating-circuit decompositions.  A random pairing produces 21 circuits;
15 are two-edge trades, while one circuit contains 12,324 edges.  The small
circuits carry essentially no useful q1/residence drift; almost all of the
trade-off sits in the giant circuit.

More decisively, the entire alternating-circuit lattice can be searched
without choosing a pairing.  Put a binary variable on every one of the 12,478
resident-only and 12,478 q1-only edges, impose equal selected red/blue degree
at every vertex, preserve every physical q1 colour, and require at least one
removed q1 edge from each of the 2,205 physical short-run closures.  This
exact circulation model is infeasible in presolve.  Therefore this particular
pair of endpoints cannot be bridged by any union of their alternating
circuits while preserving q1 and repairing every original short run.  The
computational certificate/report is
[`scratch/k16_resident_q1_overlay_circulation_cegar_infeasible_20260729.json`](scratch/k16_resident_q1_overlay_circulation_cegar_infeasible_20260729.json),
SHA-256

```text
ec86d9378c2e64f7c343b9fbbff59c1d66439b1de43e2d01ebc474912564991d
```

The overlay no-go is endpoint-specific.  It does not obstruct continued
descent in the oriented-port model or overlays against a different q1-perfect
factor.

A third ten-minute no-AA descent round improves the palette further.  The
independently replayed factor has four components of lengths

```text
1647, 1661, 2034, 7528
```

and again has zero residence violations.  Its q1 deficit is 443 lower plus
646 upper, for 1,089 holes total.  The artifact is
[`scratch/k16_pbbs_oriented_noaa_softq1_resume2_20260729.json`](scratch/k16_pbbs_oriented_noaa_softq1_resume2_20260729.json),
SHA-256

```text
3a276725c0d4a0635ebdfd7c2bc56033b887245ec003a09b9097bee9b61a0536
```

Thus the best topology and best palette currently occur in different
incumbents: resume 1 has two components and 1,190 holes, whereas resume 2 has
four components and 1,089 holes.  The next direct relaxation is to admit the
222,375 genuine AA seams already present in the exact oriented-port model.

The three circulation failures (the initial resident factor and resumes 1
and 2 against the same q1-perfect endpoint) admit a much smaller common Hall
certificate.  In the q1 endpoint, short-run motif 1993 is the length-two run
of coordinate 9 with closure

```text
(45358,45614), (45614,47630), (47246,47630).
```

Repairing that run requires removing at least one q1-only edge in the
closure.  For every one of the three resident endpoints, every removable
candidate is statically forbidden: it is the unique q1 occurrence of either
its lower or upper colour, and the resident-only shore contains no edge of
that colour that could replace it.  Resume 1 additionally shares the first
closure edge with the q1 factor, leaving only the two upper-blocked edges.
Consequently the motif constraint and the two q1 palettes alone are
inconsistent; vertex-circulation and higher CEGAR cuts are unnecessary.

The reproducible audit is
[`scratch/audit_k16_overlay_static_hall_obstructions_20260729.py`](scratch/audit_k16_overlay_static_hall_obstructions_20260729.py),
SHA-256

```text
c952b32e56f2721983782c9dcca12f47a5781af6a073ef5a5d630c979264d0fe
```

and its three-endpoint report is
[`scratch/k16_overlay_three_endpoints_static_hall_obstruction_20260729.json`](scratch/k16_overlay_three_endpoints_static_hall_obstruction_20260729.json),
SHA-256

```text
524189d73e165ad4f4735af4414227d127d0d64a60073837756a68291e3e135f
```

The numbers of independently sufficient static motif obstructions are 6, 2,
and 3 respectively, with motif 1993 common to all three.  This explains the
three opaque CP-SAT `INFEASIBLE` results by one literal palette cut.  It also
sharpens their scope: the failure is a property of this fixed q1 endpoint,
not evidence against AA-enabled direct oriented-port descent or against a
different q1-perfect endpoint.

That endpoint-specific qualification is constructive.  Quotient edge-orbit
24034 is the orbit of the first physical closure edge of motif 1993.  There
is no q1-preserving one-orbit replacement, but the exact two-orbit trade

```text
remove 18185,24034; add 18183,24035
```

preserves quotient degree two and both complete q1 palettes.  It removes the
blocked motif, although its new cycle structure creates another common
static obstruction.  Two more q1-preserving two-orbit trades give the net
radius-five pretrade

```text
remove 2678,4423,18185,24034,24140
add    2693,4421,18183,24038,26703.
```

The resulting q1 endpoint remains an exact equivariant spanning 2-factor,
has both q1 supports equal to 764, and has five physical components of
lengths

```text
515, 515, 515, 705, 10620.
```

Against the two-component resident resume-1 factor it has **zero static
palette/motif Hall obstructions**.  Its certificate is
[`scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json`](scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json),
SHA-256

```text
5ae4948c96a32b592871c84ba9fe34301a40992ec1592175edd2626249e01af8
```

and the paired static report is
[`scratch/k16_overlay_radius5_portal_resume1_resume2_static_hall_20260729.json`](scratch/k16_overlay_radius5_portal_resume1_resume2_static_hall_20260729.json),
SHA-256

```text
9a3d9a025321f3fbd310e8e6e957a095ba5723d9f2c64715ecdb11aff7e73a6c
```

The full exact circulation instance for this new endpoint pair builds with
24,959 Boolean variables, 37,997 constraints, 12,479 red and 12,479 blue
edge variables, and 2,250 distinct initial motif cuts.  It has no common-edge
motif and no static blocker.  The build-only report is
[`scratch/k16_resume1_portalq1_overlay_circulation_model_build_20260729.json`](scratch/k16_resume1_portalq1_overlay_circulation_model_build_20260729.json),
SHA-256

```text
17cc94b12b566c735c8d5bdc899bd21377a6b7d37144eeda612e0d6839b89a47
```

Thus the previous presolve no-go has been removed by a five-orbit endpoint
pretrade.  This does not yet prove that the circulation instance is feasible:
global circulation and aggregate palette Hall cuts remain.  It does identify
the smallest currently known portal through the former endpoint obstruction,
and makes an exact solve of the new instance the next decisive overlay test.
