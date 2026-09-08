# Lane R: exact staging of the k16 PBBS joint cut/seam model and the first AA relaxation

Date: 2026-07-29

## 1. Exact verdicts from the no-AA runs

The first full joint no-AA model selected A cuts, B cuts, AB seams, and
nonfactor BB seams simultaneously.  It enforced:

1. opening every source component;
2. cyclic cut separation at least three;
3. a cut in every closure of each source-B positive run of length two or
   three;
4. exact seam degree one at every exposed state and zero at every unexposed
   state;
5. complete physical rank-seven intersection and rank-nine union palettes;
   and
6. an external BB continuation for every selected three-state B segment.

It did not enforce old-coordinate seam residence, connectivity, deeper
shadows, or `COMP3`.  It contained 12,870 cut variables, 6,435 three-state
segment indicators, and

\[
51{,}480\ \mathrm{AB}+173{,}745\ \mathrm{BB}=225{,}225
\]

seam variables.  The unhinted H100 run returned `UNKNOWN` with no incumbent
after 1806.458477901 seconds.  Its report is
`scratch/k16_pbbs_joint_cut_seam_q1_noaa_unhinted_unknown_20260729.json`,
SHA-256

```text
22358704e898f3369b3920caad89e588b17dcc3600a8764ffb37717fe13fc488
```

Thus this run proves neither feasibility nor infeasibility.

Two warm retries likewise have no mathematical status.  The first used only
2,324 positive literals from the saved 596-B-cut/566-A-cut geometric
scaffold; it terminated without an output report.  The second fixed only the
counts 566 and 596, supplied a complete repair hint, reached about 72.7 GB
resident memory, and terminated without an output report.  Neither event may
be called `UNKNOWN`, `INFEASIBLE`, or an obstruction, because no solver status
was persisted.

The original writer omitted the new coordinate `TOP=2^15` when serializing B
segments.  The no-incumbent artifact contains no segments, so that bug did
not corrupt a mathematical witness.  The current writer serializes every B
state as `old_mask | TOP`; the fixed-segment adapter restores TOP
idempotently for old files; and the independent replay requires that the A
and B segment decks partition all 12,870 rank-eight states, with TOP absent
from every A state and present in every B state.

## 2. The smallest sound staged outcome before AA

Fixing only the cut counts did not make the hard model operationally small.
A sound soft-q1 stage retained all geometry, degree, and TOP-residence rows,
fixed the counts to

\[
a=566,\qquad b=596,
\]

and maximized the two q1 cover counts.  It returned a `FEASIBLE` scaffold
with

\[
\#AB=1132,\qquad \#BB=30,
\]

and exact hole counts

\[
H_7=204,\qquad H_9=459.
\]

There are 59 three-state B segments.  Independent physical replay gives six
components with lengths

\[
10,41,53,60,1751,10955,
\]

no short TOP run, and old-coordinate residence defects

\[
1^{145}2^{395}3^{413}.
\]

The candidate and independent audit are respectively

```text
scratch/k16_pbbs_joint_cut_seam_softq1_counts566_596_20260729.json
SHA-256 8c9364c192391cbac8db1d196d39609e523585fecac9f3497a7f6163366b44f6

scratch/k16_pbbs_joint_cut_seam_softq1_counts566_596_20260729.independent.audit.json
SHA-256 81ef22259c92374a11576e27a05b8d35a54eba6d59b730f4a225cd7f88293b43
```

This is a rigorously replayed partial scaffold, not a q1 factor.

## 3. Fixed-cut AA stage

Let

\[
V_A=\binom{[15]}8,
\qquad
V_B=\{\mathrm{TOP}\}\mathbin\cup\binom{[15]}7.
\]

The A source is the audited two-component rank-eight factor.  The B source is
the audited 21-component PBBS 27-trade factor.  Freeze the 566 A cuts of the
saved geometric scaffold and the 596 B cuts of the saved both-shore-reachable
certificate.  Their exposed port counts are 1,132 and 1,192.

Admit exactly the following new edges:

* AA: a Hamming-two pair of exposed A states that is not an original A-factor
  edge;
* AB: an exposed B state `TOP union R` and exposed A state `R union {a}`;
* BB: a Hamming-two pair of exposed B states that is not an original B-factor
  edge.

No arbitrary incidence rung and no deleted same-shore rail edge is admitted.
The solver-independent catalogue contains exactly

\[
5574\ \mathrm{AA}+2573\ \mathrm{AB}+7825\ \mathrm{BB}=15972
\]

candidate seams.  The cut geometry has 60 three-state B segments and hits all

\[
195\text{ length-two}+615\text{ length-three}
\]

source-B short-run closures.

If a selected matching contains (x,y,z) AA, AB, BB seams, exact exposed-port
degree gives

\[
2x+y=1132,\qquad y+2z=1192.
\]

Equivalently,

\[
z-x=30,\qquad y=1132-2x.
\]

These identities replace the no-AA equations.  In particular, neither the
old certificate-specific lower bound 47 nor the redundant scalar
fixed-successor BB bound is imposed in the joint AA model.  All q1 and
per-segment requirements are expressed by their exact integral rows.

The independent input census is

```text
scratch/k16_pbbs_joint_fixedcuts_aa_input_20260729.audit.json
SHA-256 e0436e7a320bea2cd5f2369c8773396159f1c22ccbcb37d0d478577dd46cff5c
```

and its verifier is

```text
scratch/audit_k16_pbbs_joint_fixedcuts_aa_input_20260729.py
SHA-256 0a60814b99bebae0864aeb963b51b3d5e8632ea50cbbe2db1010857c041af631
```

## 4. Soundness theorem for the staged AA model

### Theorem 4.1

Suppose the fixed-cut AA model returns an integral feasible solution with hard
q1 rows.  Retain every uncut source-factor edge and insert every selected
seam.  Then the resulting graph is a physical degree-two factor on all
12,870 rank-eight subsets of `[16]`, it contains every rank-seven
intersection colour and every rank-nine union colour, and every positive TOP
run has length at least four.

### Proof

Cut separation implies that each state is incident with at most one deleted
source edge.  An unexposed state retains both source edges and is incident
with no seam.  An exposed state retains one source edge, and its exact port
row gives it one selected seam.  Hence every state has degree two.  The two
source shores are disjoint and together equal the full rank-eight layer, so
the graph is a physical factor on exactly 12,870 states.

For every rank-seven colour (L), the hard lower row is the number of
retained source edges with intersection (L), minus precisely the cut source
edges already removed, plus selected seams with intersection (L); it is at
least one.  The rank-nine union rows are identical with union in place of
intersection.  Thus both q1 palettes are complete.

Every B segment consists entirely of TOP states.  A segment of length at
least four is already safe.  For every three-state B segment, the model
requires an incident BB seam and forbids the BB chord joining that segment's
own two endpoints.  Therefore one endpoint joins an external B state and the
TOP run extends beyond the three-state segment.  Hence no TOP run has length
below four.  \(\square\)

### Exact scope

The theorem does not assert old-coordinate residence, connectivity, deeper
shadow support, compiler compatibility, or a literal word.  Those remain the
obligations of the fixed-segment successor and the final exhaustive verifier.
Conversely, infeasibility of this stage would rule out only this pair of fixed
cut sets with the stated AA/AB/BB seam library; it would not rule out other
jointly chosen cuts or interior-changing packets.

## 5. Implementation corrections frozen in this stage

The current joint solver:

1. writes physical B states with TOP restored;
2. binds the PBBS base, B certificate, A factor, and fixed-cut hints by
   SHA-256 when the available source hash is present;
3. rejects out-of-range or wrong-source fixed cut indices;
4. records all hint hashes in its output;
5. excludes every original AA and BB rail edge from the seam catalogue;
6. enforces an external, rather than self-closing, BB continuation for each
   selected three-state B segment; and
7. contains no stale scalar fixed-successor lower bound.

The solver-independent output auditor reconstructs every segment from the cut
indices, checks exact TOP serialization and the full middle deck, recomputes
the seam kinds and q1 colours, rejects original rail reinsertion, verifies the
perfect port matching, recomputes the physical factor, and reports components
and all-coordinate residence defects.

Current source hashes are

```text
scratch/solve_k16_pbbs_joint_cut_seam_q1_20260729.py
SHA-256 f12ef5392d4c121b8da131c958d5438dbdfd06af8214d7d3ab5905ed67809119

scratch/solve_k16_pbbs_fixed_segments_q1_residence_20260729.py
SHA-256 461fbaa5c0f78efb3fea837f8d143db1244f7c2eaf8e097f8edbeb69b2ecb451

scratch/audit_k16_pbbs_joint_cut_seam_q1_20260729.py
SHA-256 571ca35990d4781685509b0bb118d5cef91e3184987056dc4aa299c4d9873ac6
```

## 6. Executed AA outcome

The four-worker, low-priority H100 run returned `INFEASIBLE` after
0.045897924 solver seconds.  Its persisted report is

```text
scratch/k16_pbbs_joint_fixedcuts_aa_q1_s20260729.json
SHA-256 836c72e2e7ff3c3111bcae2b3af192ba5ecefb5ab6461350014705b9da1b4b34
```

The report binds the PBBS base, B certificate, A factor, and both fixed-cut
hints to the hashes listed above; records 5,574/2,573/7,825 AA/AB/BB
candidates; and declares `allow_aa`, `fix_a_cuts`, and `fix_b_cuts` true with
cut counts 566 and 596.  The status is independently implied by the following
pointwise theorem, so it does not rest on CP-SAT.

### Theorem 6.1: zero-candidate colour obstruction

Let (C_A,C_B) be the two frozen cut sets.  After deleting them, there are
583 missing rank-seven intersection colours and 913 missing rank-nine union
colours.  Among the missing colours, exactly 121 lower and 169 upper colours
are the colour of no admissible genuine nonfactor AA, AB, or BB seam between
exposed states.  Therefore no perfect seam matching, and in fact no subset of
the seam catalogue, can make both q1 palettes complete.

The candidate-count histograms over the retained-factor holes are

\[
\begin{aligned}
\text{lower: }&0^{121}2^{223}5^{157}9^{60}14^{16}20^6,\\
\text{upper: }&0^{169}2^{315}4^7 5^{201}8^3 9^{143}
13^3 14^{63}20^8 27^1.
\end{aligned}
\]

### Proof

For each retained-factor lower hole (L), independently enumerate every pair
of exposed rank-eight states with intersection (L), retain it exactly when
it is one of the three admitted seam types, and reject original A- or
B-factor edges.  The analogous enumeration for each upper hole (U) uses
union (U).  This is the complete seam catalogue: two rank-eight states are
Johnson adjacent exactly when their intersection has rank seven, equivalently
their union has rank nine.  Direct counting gives the two displayed
histograms.  A zero-candidate missing colour cannot be restored by any seam
selection, proving infeasibility.  \(\square\)

### Canonical lower witness

Take (L=886).  Across both source shores its unique q1 provider is A edge

\[
9078-887,
\]

edge index 3319, and this edge is cut.  The nine possible rank-eight
supersets of (L) are obtained by adjoining one point outside (L).  Under
the frozen cuts, the only exposed such states are exactly 887 and 9078.
Their pair is the deleted original A edge, which is not a genuine rethreading
seam.  Hence no allowed seam has intersection 886.

There is an equally explicit upper witness.  For (U=3325), the unique
source provider is the cut A edge

\[
3321-2301
\]

of index 5815; these are the only exposed rank-eight subsets of (U), so
again the sole formal replacement is reinsertion of the deleted rail edge.

The complete zero-candidate lists and both canonical provider replays are in
the solver-independent input audit of Section 3.

## 7. Precise boundary and next sound relaxation

The fixed-cut AA class is closed.  This is stronger than the earlier fixed-cut
no-AA obstruction, but it is not an obstruction to the PBBS 21-component
factor or to the full joint model.  In particular, a mobile cut can expose a
third rank-eight state in one of the obstructed colour fibres; equivalently,
the full model can choose not to make the self-only cut in the first place.

For any missing lower colour (L), an AA-enabled fixed-cut scaffold must
expose two rank-eight supersets of (L) whose pair is not a deleted original
same-shore rail edge.  The dual necessary condition for an upper colour (U)
is two exposed rank-eight subsets of (U) forming an admitted nonfactor seam.
The 121/169 failures show that the next relaxation must move cuts, not merely
add more matching freedom on these ports.

The smallest class-level continuation is therefore one of the two exact
restricted joint models already supported by the formulation:

1. freeze the 596 B cuts, allow the A cuts to move, and admit AA/AB/BB seams;
   or
2. freeze the 566 A cuts, allow the B cuts to move, and admit AA/AB/BB seams.

Infeasibility of either model would remain scoped to its frozen opposite
shore.  A class-wide theorem requires the integral cut master plus the exact
fixed-cut seam oracle and sound no-goods for complete cut vectors.  No
resident Hamilton carrier, deeper-shadow carrier, `COMP3` certificate, or
literal k16 word is claimed here.
