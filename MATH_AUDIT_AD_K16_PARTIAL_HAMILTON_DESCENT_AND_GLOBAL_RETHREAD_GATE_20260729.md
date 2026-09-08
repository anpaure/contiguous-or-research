# k=16 partial-Hamilton topology descent and global-rethread gate

Date: 2026-07-29  
Lane: AD  
Status: exact finite certificates and proved splice lemmas; **no k=16 word or COMP3 certificate is claimed**

## 1. Executive boundary

There are two different k=16 Hamilton carriers in this note.  They must not
be conflated.

1. `scratch/k16_connected_q1_lower2_hamilton_20260729.json` is a physical
   Hamilton carrier with every upper-q1 quotient row but two missing lower-q1
   quotient orbits.  Those two orbits expand to 20 literal colours.  Its
   corrected status is `PARTIAL_Q1_PHYSICAL_HAMILTON`, not a COMP3-ready
   status.  A 31-move topology descent improves its deeper-shadow and
   two-sided-residence ledgers, but retains all 20 literal lower holes.
2. `scratch/k16_qfactor_q1_topresident_hamilton_20260729.json` is a different
   physical Hamilton carrier with both q1 quotient palettes complete and the
   distinguished top coordinate biresident.  Its old-coordinate residence
   defects cannot all be hit while retaining one *current* provider of every
   q1 row.  On the exact radius-147 face, keeping its 80 AB edge orbits fixed
   also makes the joint same-shore degree/q1 completion model infeasible.

Thus the surviving construction is a genuinely joint global rethread.  It
must change the cross-edge pattern at minimum radius 147, or move beyond
radius 147, while simultaneously rebuilding q1 palettes and controlling new
residence motifs.  Neither certificate proves that such a rethread does not
exist.

## 2. Quotient and ledger conventions

The group is the regular (C_{15}) action rotating coordinates
(0,ldots,14) and fixing coordinate 15.  The quotient has 858 rank-eight
vertices and 27,456 Johnson-edge orbits.  Every factor in this note is
loopless unless stated otherwise.

For a connected quotient cycle, its physical lift is one Hamilton cycle on
all

\[
\binom{16}{8}=12870
\]

owners exactly when its total voltage is a unit modulo 15.

A quotient q1 hole is an orbit of literal masks, not one literal mask.  In
particular, the two lower holes

\[
33371=0\mathrm{x}825b,\qquad 38053=0\mathrm{x}94a5
\]

have orbit sizes 15 and 5.  They therefore represent exactly 20 literal
rank-seven colours.  The two endpoint cells of a linear COMP3 opening can
absorb at most two literal q1 colours, not two quotient orbits.

For a physical Hamilton cycle (F), define

\[
\Phi(F)=(h_2(F),u(F),\rho_+(F),\rho_-(F)),              \tag{2.1}
\]

where

* (h_2) is the lower-q2 orbit-hole count;
* (u) is the sum of arbitrary-width upper orbit holes over all positive
  depths;
* (ho_+) and (ho_-) are the positive- and negative-run defect masses
  \(\sum_{r=1}^3(4-r)n_r\).

All support updates use occurrence counters before passing to support sets;
set subtraction alone is not sound when a seam colour also occurs elsewhere.

## 3. Exact promoted partial Hamilton

### Theorem 3.1 (radius-13 factor plus voltage promotion)

Start from the connected soft factor and first apply

\[
\{25126,23360\}\longrightarrow\{25046,23361\}.          \tag{3.1}
\]

The exact radius-13 exchange relative to that base is

\[
\begin{aligned}
R_{13}={}&\{4537,7892,9838,10435,12922,14967,15047,15079,\
           16521,22847,22963,26000,27103\},\\
A_{13}={}&\{4529,7893,9854,10448,10995,11491,12932,14958,\
           16524,22866,22947,24242,27221\}.
\end{aligned}                                           \tag{3.2}
\]

It gives one quotient 858-cycle of voltage 12 and hence three physical
cycles of length 4290.  The parallel replacement

\[
13230\longrightarrow13232                               \tag{3.3}
\]

keeps quotient endpoints ((322,408)), keeps upper colour 6587, changes
lower colour (4915\to2459), and changes total voltage (12\to8\pmod {15}).
The resulting selected-edge digest is

```text
02078ab691a57372de7a540417ce7005ac0fb52265a3a05d728518a23bc3131d
```

and its physical lift is one 12,870-cycle.

Its exact starting ledger is

\[
\Phi(F_0)=(89,129,5805,5835),                           \tag{3.4}
\]

with arbitrary-width lower/upper orbit-hole counts

\[
\begin{array}{c|rrrrrrrr}
q&1&2&3&4&5&6&7&8\\ \hline
L_q&2&89&27&3&0&0&0&0\\
U_q&0&96&30&3&0&0&0&0.
\end{array}                                             \tag{3.5}
\]

The positive short-run histogram is

\[
(n_1,n_2,n_3)=(375,1635,1410),
\]

and the negative histogram is

\[
(345,1560,1680).                                        \tag{3.6}
\]

The lower-q1 holes are the two quotient orbits in Section 2, hence 20
literal masks.  Every upper-q1 literal mask is present.

#### Proof

The route auditor independently rebuilds the catalogue, checks selected and
unselected membership, balances quotient endpoint incidences at every move,
traverses the quotient cycle and computes voltage, constructs all 12,870
physical edges, and exhausts every contiguous lower/upper interval and both
run orientations.  It also verifies the internal payload hash and enumerates
the 20 literal lower holes.  These checks give (3.1)--(3.6).  \(\square\)

### Scope of the radius lower bound

The earlier relaxed CP-SAT model enforces loopless degree two, zero upper-q1
quotient holes, and at most two lower quotient holes around the base in
(3.1), but omits connectivity and unit voltage.  Its retained run transcript
reports INFEASIBLE through radius 10, UNKNOWN at radii 11 and 12, and a
radius-13 factor.  Because connectivity/voltage are omitted, INFEASIBLE is a
sound lower bound for a physical Hamilton target.  UNKNOWN proves nothing.
The promoted Hamilton is at radius 14 after (3.3).  No minimality is claimed
at radii 11--13, and the CP-SAT transcript has no independent proof log.

## 4. Exact cyclic-splice compiler

The full theorem and proof are in
`MATH_THEOREM_AD_CYCLIC_SPLICE_INCREMENTAL_SHADOW_RESIDENCE_20260729.md`.
The decisive statements are as follows.

### Theorem 4.1 (seam counter identity)

Cut a cyclic set-word into directed arcs.  Reglue the same arcs after allowed
coordinate rotations and optional reversal.  For intersection or union, the
old and new orbit-occurrence counters differ exactly by

\[
M(W')-M(W)=\operatorname{Cross}(W')-\operatorname{Cross}(W), \tag{4.1}
\]

where `Cross` counts precisely intervals not contained in one cut arc.

Consequently a fixed width (w) has only (w-1) affected starts per seam.
A connected 2-opt has two old and two new seams, so lower q2 needs at most
four old and four new triples.  This is not an arbitrary-width theorem:
all-upper unions and arbitrary-width lower intersections require exact
prefix/suffix saturation rectangles, including intervals containing complete
intermediate arcs.  There is no universal constant locality radius.

For residence, each arc and coordinate is summarized by its endpoint bits,
endpoint run lengths, constant flag, and internal zero/one run counters.
Summary concatenation merges equal boundary bits and is an exact monoid.
It updates both run orientations; a positive-only audit says nothing about
negative residence.

For a regular cyclic voltage lift, a parallel replacement changes only the
sheet gluing (t\mapsto t+\omega).  A connected 2-opt is the corresponding
two-arc splice with one arc reversed and signed dart voltages.  Quotient
connectivity must still be supplemented by unit total voltage.

## 5. Fixed-cycle parallel obstruction

On (F_0), 43 selected quotient adjacencies have a parallel choice, with 50
alternative edge orbits.  A short positive run is forced by its entering,
internal, and exiting physical edges.  If every quotient adjacency in that
local witness has a singleton parallel menu, every parallel reassignment
retains the run.

Exactly

\[
(360,1455,1185)                                         \tag{5.1}
\]

of the length-one/two/three positive runs have such rigid witnesses, for a
total of 3000.  Thus a fixed-quotient-cycle parallel reassignment cannot make
(F_0) resident.  This is positive-run only, fixed-adjacency only, and
artifact-pinned; it does not survive a topology-changing 2-opt without a new
audit.

## 6. Exact 31-move PARTIAL20 descent

Define the intended one-neighbourhood \(\mathcal N(F)\) to consist of:

1. replacing one selected edge orbit by one unselected parallel orbit; or
2. cutting two nonadjacent quotient-cycle edges with four distinct endpoints
   and using any orbit assignment on the unique non-original endpoint pairing
   that reconnects the two retained arcs into one quotient cycle.

The other endpoint pairing closes the retained arcs separately and is not a
connected 2-opt.  Adjacent-cut double-parallel replacements and trades of
support at least three are outside \(\mathcal N\).

A neighbour is hard-admissible when it is loopless, has zero upper-q1
quotient holes, has at most two lower-q1 quotient holes, and has unit voltage.

### Theorem 6.1 (monotone descent and terminal local minimum)

The 31 chronological trades in
`scratch/k16_partial20_secondary_lex_route_ad_20260729.json` form a literal
route

\[
F_0,F_1,\ldots,F_{31}.
\]

Every prefix is a physical Hamilton cycle on 12,870 distinct owners, has zero
upper-q1 quotient holes, and has exactly the same two lower quotient holes,
hence the same 20 literal lower holes.  Every step belongs to
\(\mathcal N(F_i)\) and is componentwise nonworsening in \(\Phi\), with at
least one strict coordinate.  The endpoint has selected digest

```text
53a08b5b24f9b5e40a77e5168fedd7989ed17b09f237e9ebcf700fc0a75b39a0
```

and voltage 14.  Its exact ledger is

\[
\Phi(F_{31})=(70,95,4875,5220).                         \tag{6.1}
\]

The all-upper split at depths (2,3,4) improves

\[
(96,30,3)\longrightarrow(76,19,0).                     \tag{6.2}
\]

Its positive histogram is

\[
(240,1410,1335),
\]

and its negative histogram is

\[
(255,1395,1665).                                        \tag{6.3}
\]

At (F_{31}), exhaustive enumeration gives 3806 raw intended move
descriptions.  Of these, 114 pass the two q1 gates.  Fifty are nonunit, with
voltage histogram

\[
0^{10},3^{10},5^6,6^3,9^9,10^3,12^9.
\]

The remaining 64 distinct selected sets are hard-admissible.  None strictly
improves \(\Phi\) componentwise, and none has exactly the same vector.
Therefore there is no exact-vector neutral first router followed by an
improver.

#### Proof

The frozen route auditor reconstructs every prefix and its physical lift,
recomputes all interval and dual-run ledgers, and verifies the endpoint
incidence balance and move language.  It then derives all cycle cut pairs,
all catalogue orbit assignments on the connected pairing, and every parallel
replacement, deduplicating by selected set.  A slower independent physical
graph/trace reconstruction agrees at the terminal.  The resulting counts are
exactly those above.  A second auditor, with its own catalogue construction
and terminal move classification, independently replays all 32 states and
obtains the same hard-neighbourhood SHA and candidate-vector SHA.  \(\square\)

This is only a local minimum in \(\mathcal N\).  It excludes neither an
adjacent double-parallel macro, a support-three-or-larger alternating trade,
nor a global rethread.  More importantly, every state remains `PARTIAL20` and
is not COMP3-boundary feasible.

## 7. A different q1-perfect/top-resident source

Let

```text
H = scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
SHA-256 = f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5
```

This is one quotient 858-cycle of unit voltage 11 and one physical
12,870-cycle.  It covers all 764 lower and all 764 upper q1 quotient rows and
is biresident in the distinguished coordinate.  It is not (F_0): their
selected sets have intersection 783 and 75 private edge orbits on each side.

For every current positive short old-coordinate run, let its motif be the set
of quotient edge orbits on its entering/internal/exiting local path.  Keeping
all motif edges in any degree-two replacement retains that short run, even if
the path is reversed.  Hence every positive-resident equivariant replacement
must delete at least one edge from every old motif.

Direct expansion gives 3390 physical short runs,

\[
1^{330}2^{1620}3^{1440},
\]

which compress exactly into 226 (C_{15})-motifs with size histogram

\[
2^{22}3^{108}4^{96}.                                    \tag{7.1}
\]

They are cyclic intervals along the quotient cycle.  Cutting at an uncovered
edge, earliest-finish greedy supplies both 147 pairwise edge-disjoint motifs
and a 147-edge transversal.  Therefore the old-motif transversal number is
exactly 147, solver-free.

### Theorem 7.1 (solver-free palette coupling)

No deletion set can hit all 226 motifs while retaining at least one *current*
provider of every current lower and upper q1 quotient row.

#### Proof

Sorted motif 1 is

\[
\{1091,1406\}.                                          \tag{7.2}
\]

Edge 1091 is the unique current provider of upper row ((0,1915)), and edge
1406 is the unique current provider of upper row ((0,3005)).  Hitting (7.2)
deletes one of them and therefore destroys an upper q1 row.  More globally,
only 36 selected edges are individually safe in both palettes, and 186 of
the 226 motifs contain no such edge.  \(\square\)

This theorem concerns retention of old providers.  New edges may restore the
lost rows, so it is a coupling theorem, not a resident-factor no-go.

### Exact transcript and replayed witness

The retained lexicographic CP-SAT result minimizes

\[
1000(\text{lost lower rows}+\text{lost upper rows})
+\text{removals}.                                       \tag{7.3}
\]

Since (1000>858), this is a valid lexicographic objective.  The solver
reports optimum 180 lost quotient rows and tie-break 148 removals.  The saved
148-edge witness independently hits every motif and loses 88 lower plus 92
upper quotient rows.  These expand to 1320 lower plus 1370 upper literal
colours, total 2690.  Of the 180 rows, 179 have a unique current provider;
the only nonsingleton loss is lower row ((1,1611)), with providers
\(\{21303,22078\}\).

The witness and objective replay exactly, but the optimum/lower bound 180148
has no retained solver proof log or independent dual.  It remains exact
CP-SAT transcript scope.  The unconstrained 147 transversal optimum is the
separate solver-free theorem above.

## 8. Fixed-cross radius-147 no-go

The source (H) has exactly 80 selected AB edge orbits.  Fix all of them and
forbid every off-source AB orbit.  Let \(\mathcal P\) be the certified family
of 147 pairwise edge-disjoint motifs; its union has 476 selected edges.

### Lemma 8.1 (radius-147 normal form)

Any replacement that hits all old motifs and removes exactly 147 selected
edges must remove exactly one edge from every member of \(\mathcal P\) and
no edge outside their union.

#### Proof

The 147 motifs in \(\mathcal P\) are pairwise edge-disjoint, so hitting them
requires at least 147 distinct removals.  Equality forces one in each and
leaves no removal for an edge outside their union.  \(\square\)

### Finite theorem 8.2 (fixed-cross same-shore obstruction)

There is no radius-147 quotient selection satisfying all of the following:

1. the 80 AB edge orbits are exactly those of (H);
2. exactly one selected edge is deleted from each packed motif and every one
   of the 226 original motifs is hit;
3. exactly 147 unselected, nonloop AA/BB edge orbits are added;
4. every quotient vertex has degree two; and
5. all 764 lower and all 764 upper q1 quotient rows remain covered.

The source sector census is (389) AA, (80) AB, and (389) BB edges.
The packing union contains (233) AA, (36) AB, and (207) BB edges.
The exact model has 476 formal cut variables; pinning its 36 packed AB edges
leaves 440 effective same-shore cut choices.  It has 23,218 off-source,
nonloop same-shore seam variables, split equally as 11,609 AA and 11,609 BB.
It is a relaxation of the desired carrier: quotient connectivity, unit
voltage, top residence, and newly-created old-coordinate motifs are not
required before its first solve.  CP-SAT returns INFEASIBLE in round zero,
with 160,567 branches and 12,640 conflicts in 3.036 seconds.  Thus the
infeasibility implies the same no-go for every connected/unit-voltage
resident carrier on this fixed-cross radius face.

Fixing every old AB edge, forbidding every new AB edge, and forbidding new
loops are explicit model restrictions.  This finite infeasibility is
transcript-audited but has no retained proof log.  The model implication and
Lemma 8.1 are solver-free; the final variable-cut UNSAT lower bound is
CP-SAT transcript scope.  A solver-free zero-candidate q1 cut exists for the
retained 147-edge hint, but it does not certify infeasibility when the 147
cuts vary and is not used as a proof of Theorem 8.2.

### Corollary 8.3 (necessary global move)

Within the (C_{15})-equivariant quotient architecture, a resident,
q1-complete replacement of (H) at the minimum possible old-edge radius 147
must change the AB cross pattern.  If the cross pattern is fixed, its radius
must exceed 147.

This does not assert existence at larger radius or with a changed pattern.

## 9. Exact remaining model

The next carrier model must co-design all of the following in one integral
selection:

* old motif cuts and replacement edges;
* variable AB cross edges, not only AA/BB seams;
* degree two, quotient connectivity, and unit voltage;
* reconstruction of every lost lower and upper q1 row;
* elimination of newly-created positive and negative short runs;
* arbitrary-width upper coverage and the literal COMP3 chronology.

The old-motif rows are necessary but not sufficient: additions can create new
motifs.  Rankwise palette balance and residence cannot be optimized in
separate phases.  No result in this note supplies a literal source word or
proves k=16 universality.

## 10. Reproducible artifacts

The principal frozen files are:

* promoted partial carrier:
  `scratch/k16_connected_q1_lower2_hamilton_20260729.json`, SHA-256
  `16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8`;
* independent promoted audit:
  `scratch/audit_ad_k16_promoted_hamilton_20260729.py`, SHA-256
  `58f61a7ebd72cd6af662533990eb7b05c6280d68704e701f43197527108b0ae0`,
  and output SHA-256
  `202e6175c9b972e5235f0125e2064c70a1bf9dbaa6ebffbc365d5752ef25aff9`;
* cyclic-splice theorem:
  `MATH_THEOREM_AD_CYCLIC_SPLICE_INCREMENTAL_SHADOW_RESIDENCE_20260729.md`,
  SHA-256 `daff074c4ffa9e9c4b059c9777af69656f9842374453dff3f7e400910f392fe5`;
* 31-move route:
  `scratch/k16_partial20_secondary_lex_route_ad_20260729.json`, SHA-256
  `c921f389e91c0a2e09b708589c299133fdf5739272d51d6b3c15c4d57fd2e217`;
* route auditor and output:
  `scratch/audit_k16_partial20_secondary_lex_route_ad_20260729.py`, SHA-256
  `9454c57a2a8e4bbbc59ed2dbf7cd96a72a74ac2d3b0557f1ad4a527dc25ede46`,
  and output SHA-256
  `95e34450b041ba57e04f76ec36608edac5683b6d098ff2098bf4bcd9320f962e`;
* independent route/census auditor and output:
  `scratch/audit_k16_secondary_topology_descent_independent_20260729.py`,
  SHA-256
  `2fc8d3c4b0755851c4c0699f6e13f6d7f2e406fd9f2f23d10ccceff936b14668`,
  and `scratch/k16_secondary_topology_descent_independent_20260729.audit.json`,
  SHA-256
  `3645dc15d1d0f4a816022a6991be294df3f7b214d93c612b262d52f71968582d`;
* q1-perfect/top-resident source:
  `scratch/k16_qfactor_q1_topresident_hamilton_20260729.json`, SHA-256
  `f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5`;
* residence/palette coupling audit:
  `AD_K16_RESIDENCE_PALETTE_COUPLING_AUDIT_20260729.md`, SHA-256
  `1f0d7de96d89985bad8891e2ec6c24b068be524fc08d41c4115d5e7ababc3b6e`;
* fixed-cross radius-147 result:
  `scratch/k16_same_shore_radius147_noab_cegar_20260729.json`, SHA-256
  `9ebd21730c08d6ddb848012821dd7d91ff1d2fe141f089555bd9052dfcfd3a95`,
  with model source
  `scratch/search_k16_same_shore_joint_cut_seam_cegar_20260729.py`, SHA-256
  `b62d40be67f3dd7b02c3ac044763f537b7f3a50b53af32b891f48637c058ff52`;
* independent fixed-cross model audit:
  `AD_K16_SAME_SHORE_RADIUS147_NOAB_CEGAR_AUDIT_20260729.md`, SHA-256
  `9dc237594c578081e8e531a823d1cf8764eaa2e89570adcfd9d1c537427e365a`,
  with replay script SHA-256
  `a1bfd20254358401aefaea8451469d323d05281cf1947e12484f8fd40ec27d46`
  and output SHA-256
  `b10db7d1a4ae0104e49711d2e2afad7d7e4b6e5ff7e0295cef9cae9076ce3fe7`.

Every byte hash above is file-specific.  The selected digest is the stable
mathematical identity when a JSON artifact is later relabelled without an
edge-set change.
