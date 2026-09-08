# Thread D: exact graded radius-99 cut-space theorem

Date: 2026-07-29

## 1. Frozen instance

Let (F) be the persisted dynamic-cross round-0 factor

`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`

with SHA-256

`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`.

Its 147 current short-residence motifs have edge-union (U) of size 390.
Their overlap graph has 85 components.  Write (U_i) for the edge-union of
component (i).  The sets (U_i) are pairwise disjoint.  The selected edges
outside the motif union form

\[
 X=E(F)\setminus U,\qquad |X|=858-390=468.
\]

The exceptional edge is

\[
 e_*=22511.
\]

It is the unique selected provider of upper-q1 colour ((1,1907)).  The two
motifs in its overlap component include

\[
 \{22511,22520\},\qquad
 \{22511,22692,25634\}.
\]

## 2. Minimum-options plus arbitrary extras is not complete

The tempting radius-99 model chooses one minimum transversal in every motif
component and then marks one or two additional source edges as cuts.  This
misses valid hitting sets: a nonminimum inclusion-minimal local transversal
need not contain any minimum local transversal.

The exhaustive local audit gives the following exact obstruction census.

* If (e_*) is retained, 33 components have rank-plus-one hitting sets that
  contain no safe minimum option; there are 304 such local sets.
* If (e_*) is cut, the same 33 components contribute 304 such sets at
  ordinary excess one.  At excess two, 24 components contribute 2207 sets
  containing no ordinary minimum option.  Among those excess-two sets, 408
  sets in two components are themselves inclusion-minimal; the rest contain
  an excess-one inclusion-minimal core.
* Before conditioning on the (e_*) branch, the ordinary diagnostic is 34
  components at excess one and 25 at excess two: 59 component/excess pairs.
  The two additional pairs are the exceptional component itself.  Retaining
  (e_*) regrades its optimum from one to two, while cutting (e_*) forces
  the local core ({e_*}).  Thus the exact branch-conditioned count is
  (33+24=57), consistently with the branch-blind count 59.

Consequently, a model containing only the 262 palette-safe minimum options
plus one extra edge is not scope-complete at radius 99.

## 3. Exact unique graded decomposition

For each component, let (mathcal M_i) be its local motif family.

In the **retain branch**, forbid (e_*), let (r_i) be the minimum size of a
local hitting set, and define

\[
 {cal R}_{i,j}={S\subseteq U_i\setminus\{e_*\}:
 S\text{ hits }{cal M}_i, |S|=r_i+j},\qquad j=0,1.
\]

The exact local minima satisfy

\[
 \sum_i r_i=98.
\]

In the **delete/replace branch**, require (e_*) in its own local
intersection, let (d_i) be the resulting local optimum, and define

\[
 {cal D}_{i,j}={S\subseteq U_i:
 S\text{ hits }{cal M}_i, |S|=d_i+j,
 e_*\in S\text{ if }e_*\in U_i},\quad j=0,1,2.
\]

Here

\[
 \sum_i d_i=97.
\]

### Theorem 3.1 (radius-99 normal form)

A 99-edge source cut (Csubseteq E(F)) hits all 147 motifs if and only if it
has exactly one of the following unique decompositions.

1. **Retain:** (e_*\notin C), (C\cap U_i\in{cal R}_{i,j_i}), and

   \[
   \sum_i j_i+|C\cap X|=1.
   \]

2. **Delete/replace:** (e_*\in C), (C\cap U_i\in{cal D}_{i,j_i}), and

   \[
   \sum_i j_i+|C\cap X|=2.
   \]

Proof.  Since the (U_i) are disjoint, (C) hits every motif precisely when
each (C\cap U_i) hits (mathcal M_i).  The branch condition fixes the
status of (e_*).  Subtracting the sum of the corresponding local optima
from (|C|=99) gives the displayed budget equation.  Conversely, the local
hitting conditions imply all motif rows, and the budget gives 99 cuts.
Finally, the intersections (C\cap U_i) and (C\cap X) are recovered from
(C), proving uniqueness.  (square)

The aggregate numbers of exact local options at grades (0,1,2) are

\[
 \begin{array}{c|ccc}
 &0&1&2\\ \hline
 \text{retain}&262&958&-\\
 \text{delete/replace}&261&960&3442.
 \end{array}
\]

Let (R_i(z)=\sum_j|{cal R}_{i,j}|z^j) and
(D_i(z)=\sum_j|{cal D}_{i,j}|z^j).  The audited truncated product
coefficients are

\[
 [z^{0,1}]\prod_iR_i(z)=
 (32814901619680178026914088287480053760,
 10956895650811211443186614079189589950464),
\]

and

\[
 \begin{split}
 [z^{0,1,2}]\prod_iD_i(z)=(&16407450809840089013457044143740026880,\\
 &5519466452430205944126949649954145042432,\\
 &903305732507926663711877812832861593534464).
 \end{split}
\]

Multiplying by the appropriate coefficient of ((1+z)^{468}), the numbers
of distinct motif-hitting radius-99 cut sets are

\[
 26314269608821534759782407397730255110144
\]

in the retain branch and

\[
 5279389441842968292775849118951024130785280
\]

in the delete/replace branch.  These are counts of cut sets, not counts of
representations, by the uniqueness in Theorem 3.1.

## 4. Smaller scope-complete extended formulation

It is unnecessary to instantiate all 1220 retain-branch or 4663
delete-branch exact local-intersection options.  Enumerate instead every
inclusion-minimal local core through the available excess.  Their aggregate
counts are

\[
 \begin{array}{c|ccc|c}
 &0&1&2&\text{total}\\ \hline
 \text{retain}&262&304&-&566\\
 \text{delete/replace}&261&304&408&973.
 \end{array}
\]

Use one exactly-one core choice per component and cut binaries (x_e) for
all 858 selected source edges.  Impose

\[
 x_e\geq\mathbf 1[e\text{ lies in the chosen core}],\qquad
 \sum_{e\in E(F)}x_e=99,
\]

together with (x_{22511}=0) or (1) according to the branch.  Every local
hitting set contains an inclusion-minimal hitting subset; the audit checks
that every such subset allowed by the radius budget appears in the core
bank.  Therefore this smaller extended formulation is scope-complete,
although a cut can have more than one core representation.

All 858 quotient nodes occur as endpoints of selected source edges.  Once an
extra cut may occur anywhere in (E(F)), the scope-complete addition atlas is
the full set of 26,570 off-source loopless catalogue edges.  Endpoint degree
balance automatically disables an added seam at a node with no cut
incidence.  To obtain the requested factor model, append:

* exact degree-two balance;
* both q1 palette rows;
* the exact dynamic top-biresidence rows;
* lazy new-residence motif cuts;
* no connectivity constraint initially.

In the delete/replace branch the motif theorem does **not** by itself restore
upper colour ((1,1907)); the q1 rows must force a replacement provider and
the degree equations must route it.  Components and voltages are audited
only after a factor is found.

## 5. Reproducer

The solver-free exhaustive auditor and its explicit core banks are

* `scratch/audit_threadD_k16_r99_cutspace_scope_20260729.py`
* `scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json`

The script SHA-256 is

`9f93d1498c25a34b756b4538ad7c8041c8af12d81c720996b361d5da595536fa`.

The audit SHA-256 is

`b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e`.

