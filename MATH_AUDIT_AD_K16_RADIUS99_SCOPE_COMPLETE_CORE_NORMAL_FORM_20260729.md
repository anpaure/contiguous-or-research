# Audit: scope-complete radius-99 core normal form at k=16

Date: 2026-07-29

## Frozen data and scope

Let (F_1) be the persisted quotient factor

`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`

with SHA-256

`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`.

It has 858 selected, loopless quotient edges on all 858 quotient nodes.  Its
current short-positive-run hypergraph has 147 motif rows.  The motif edge
union (U) has 390 edges and its edge-overlap graph has 85 components.  If
(U_i) is the edge union of component (i), then the (U_i) are pairwise
disjoint.  The remaining selected source edges form

\[
 X=E(F_1)\setminus U,
 \qquad |X|=858-390=468.
\]

The exceptional source edge is

\[
 e_*=22511.
\]

It is the unique selected provider of upper-q1 colour ((1,1907)), but it is
not permanently forbidden at radius 99: a cut outside (U) can expose nodes
needed by a replacement provider.  Exact scope therefore requires both the
branch retaining (e_*) and the branch deleting/replacing (e_*).

## Exact two-branch cut theorem

For a source cut (C\subseteq E(F_1)), write

\[
 C_i=C\cap U_i,
 \qquad C_X=C\cap X.
\]

Because motif-overlap components have disjoint edge unions, (C) hits all
147 current motifs if and only if every (C_i) hits its local motif family
(\mathcal M_i).  Moreover,

\[
 |C|=\sum_i|C_i|+|C_X|. \tag{1}
\]

### Retain branch

Impose (e_*\notin C).  Let (r_i) be the minimum local hitting-set size
after forbidding (e_*) in its component.  Exact enumeration gives

\[
 \sum_i r_i=98. \tag{2}
\]

For every radius-99 cut, (1) and (2) imply

\[
 \sum_i(|C_i|-r_i)+|C_X|=1. \tag{3}
\]

Thus every local intersection has grade zero or one.  Across all 85
components there are 262 exact grade-zero intersections and 958 exact
grade-one intersections.  Among these, the inclusion-minimal local hitters
number

\[
 262+304=566. \tag{4}
\]

The other 654 grade-one intersections contain a grade-zero core and need no
new core selector.

### Delete/replace branch

Impose (e_*\in C).  In its exceptional component require (e_*) in the
local intersection, and let (d_i) be the resulting local optimum.  The two
motifs in that component are

\[
 \{22511,22520\},
 \qquad \{22511,22692,25634\},
\]

so the singleton ({22511}) is already an inclusion-minimal local hitter.
The exact branch optimum is

\[
 \sum_i d_i=97. \tag{5}
\]

Consequently every radius-99 cut in this branch satisfies

\[
 \sum_i(|C_i|-d_i)+|C_X|=2. \tag{6}
\]

Every local intersection therefore has grade zero, one, or two.  Their
aggregate exact counts are 261, 960, and 3442.  The corresponding
inclusion-minimal core bank has

\[
 261+304+408=973 \tag{7}
\]

cores.  The remaining exact intersections contain a smaller enumerated
core.

Equations (3) and (6) are necessary and sufficient.  Hence the two branches
together cover every 99-edge source cut hitting all 147 current motifs.

## Why the core selectors preserve the exact projection

For either branch, introduce one cut Boolean (x_e) for every one of the 858
source edges.  For each component (i), introduce one selector (y_{i,K})
for every core (K) in the appropriate 566- or 973-core bank, and impose

\[
 \sum_{K\in\mathcal K_i}y_{i,K}=1,
 \qquad x_e\ge y_{i,K}\quad(e\in K),
 \qquad \sum_{e\in E(F_1)}x_e=99. \tag{8}
\]

Also fix (x_{22511}=0) in the retain branch or (x_{22511}=1) in the
delete/replace branch.

Soundness is immediate: a selected core hits every motif in its component,
so its containing cut intersection does too.  The driver additionally keeps
all 147 direct motif rows as redundant safeguards.

For completeness, take any valid branch cut (C).  By (3) or (6), every
local intersection (C_i) lies within the enumerated branch grade.  Remove
redundant local edges until an inclusion-minimal hitting subset remains.  In
the delete branch, the exceptional component can always choose the contained
core ({22511}).  The exhaustive audit checks every one of the 1220 retain
local intersections and every one of the 4663 delete/replace local
intersections: each contains at least one bank core.  Select any such core in
each component.  This extends (C) to variables satisfying (8), so no valid
projected cut is lost.

The extension is not injective.  A local intersection can contain as many as
two retain cores or four delete/replace cores.  This creates selector
symmetry but does not affect SAT or UNSAT after projection.  Solver assignment
counts must not be reported as counts of distinct cuts.

## Exact loopless rethread projection

The quotient catalogue has 27,456 edges, including 28 quotient loops.  Since
all 858 source edges are loopless, the complete off-source loopless seam
atlas has

\[
 27456-28-858=26570
\]

edges.  Introduce one add Boolean (z_f) for every such seam and impose

\[
 \sum_fz_f=99. \tag{9}
\]

For every quotient node (v), impose exact incidence balance

\[
 \sum_{e\ni v}x_e=\sum_{f\ni v}z_f. \tag{10}
\]

Because (F_1) has degree two at every node and all represented edges are
loopless, (10) is necessary and sufficient for the edited quotient graph to
remain degree two.  Both lower and upper q1 decks contribute exactly 764
provider rows each.  Therefore the two branch models project exactly onto
all loopless (C_{15})-equivariant degree-two radius-99 edits about (F_1)
that hit the 147 current motifs and preserve both q1 palettes.

Global exact scope requires retaining the SAT/UNSAT artifact for both
branches.  Connectivity and voltage are post-audited, not constrained.
Dynamic top/complement-top residence is a later optional gate; newly created
top motifs must be separated lazily.  An infeasible CP-SAT transcript is not
a formal proof log.

## Failure of the earlier safe-minimum-plus-one form

The 262 safe minima plus one arbitrary distinct source edge form only a
proper subfamily.  Component 10 has motifs

\[
 \{185,311,2169\},
 \qquad \{2169,5603,9704\}.
\]

Its sole safe minimum is ({2169}), while ({185,5603}) is an
inclusion-minimal grade-one hitter containing no safe minimum.  Replacing
({2169}) by ({185,5603}) in any safe 98-cut base yields an omitted
radius-99 cut in the retain branch.

That earlier representation is also noninjective.  Component 0 has safe
minima ({1917,2898}) and ({1917,2906}); their common union can be
represented using either minimum and declaring the other differing edge to
be the extra cut.

## Reproducers

The independent solver-free verifier is

`scratch/audit_ad_k16_r99_safe_min_extra_scope_20260729.py`

with SHA-256

`ab494d222dcc39d8ede096d1f1418e821ca392c9d2d594bee6d4fa267bfcdf76`.

Its PASS audit is

`scratch/ad_k16_r99_safe_min_extra_scope_20260729.audit.json`

with SHA-256

`c70f14b44dc55de927a3815406f0141a844f2cdba182b134983f2d506eec89a0`.

The audited scope-complete driver is

`scratch/search_ad_k16_recenter_r99_scope_complete_20260729.py`

with SHA-256

`be0aef35b977e7539620101ff284ae7ed490408d8bfded9ca333c2576ae1148f`.
