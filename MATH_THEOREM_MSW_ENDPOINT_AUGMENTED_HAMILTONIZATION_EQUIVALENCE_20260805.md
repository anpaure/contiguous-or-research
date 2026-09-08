# MSW endpoint-augmented Hamiltonization: the exact protected-stem gate

**Date:** 2026-08-05  
**Method:** pure mathematics and primary-source theorem audit; no finite
computation, search instance, or solver  
**Status:** unconditional theorem for every `r>=3`.  The displayed augmented
graph is Hamiltonian by direct specialization of the published
Mütze--Nummenpalo--Walczak (MNW) construction.  Consequently the protected
middle-levels stem bank exists in every sufficiently large dimension.

## 0. Outcome

Let `Omega` be a `2r`-set and put

\[
 W={2r\choose r},\qquad U={2r\choose r-1},\qquad
 C=W-U={1\over r+1}{2r\choose r}=\operatorname {Cat}_r.
\tag{0.1}
\]

The Mütze--Standke--Wiechert Chung--Feller construction gives a canonical
family

\[
                    \mathcal P_r=\{P_x:x\in\mathcal D_r\}
\tag{0.2}
\]

of `C` vertex-disjoint complementary Johnson geodesics which partition
`binom(Omega,r)`.  Every `P_x` has `r` edges, its two endpoints are
complements, and its edge unions enumerate `binom(Omega,r+1)` globally,
once each.

Let `E_r` be the `2C` endpoints and let

\[
 M_r=\{X_x\overline {X_x}:x\in\mathcal D_r\}
\tag{0.3}
\]

be the endpoint matching of the paths.  Form the graph

\[
 \boxed{
 \mathcal A_r=
 \left({\Omega\choose r-1}\longleftrightarrow
       {\Omega\choose r}\right)+M_r, }
\tag{0.4}
\]

where the first term is the usual containment graph and the only edges
inside the rank-`r` shore are the `C` matching edges in (0.3).

The first result is the exact equivalence

\[
\begin{array}{c}
 \mathcal A_r\text{ has a Hamilton cycle}\tag{A}\\[1mm]
 \Updownarrow\\[-1mm]
 \text{the lifted MSW factor can be Hamiltonized while fixing its entire
 `z`-free half}\tag{B}\\[1mm]
 \Updownarrow\\[-1mm]
 \text{there is }H\subseteq\operatorname {ML}(2r+1)
 \text{ with }F_z(H)=\mathcal P_r.\tag{C}
\end{array}
\tag{0.5}
\]

The second result is that these statements do hold for every `r>=3`.
MNW start from precisely the cycles `P_x+X_x bar(X_x)`.  Every one of their
flipping cycles lies wholly in the bipartite incidence graph.  Therefore
their symmetric-difference Hamiltonization preserves every edge of `M_r`
and introduces no other rank-`r` internal edge.  Their Hamilton cycle lies
in `mathcal A_r`, not merely in the full odd graph.

It follows that **all** `C` components of
`F_z(H)` have an initial generalized balanced-collar stem of every length
`s<=r`.  In particular, for the required `s=Theta(sqrt(r))`, any `C-1`
components give the protected stem bank.  Their owners are disjoint and
their upper colours are globally distinct automatically.

Thus the protected-spacing problem is solved.  It does not require an arbitrary
middle-levels Hamilton cycle with a probabilistically balanced coordinate.
The published MNW construction already Hamiltonizes the canonical MSW
wreath factor while preserving its unique `z`-labelled edge in every
wreath.

This route is genuinely nonlexical.  The canonical GMN lexical factor has
the fixed-coordinate run spectrum proved in
`MATH_THEOREM_GMN_LEXICAL_FIXED_COORDINATE_RUN_SPECTRUM_AND_STEM_NOGO_20260805.md`;
about half its runs are submacroscopic and its published pulls only permute
that spectrum.  Therefore lexical coordinate-wall Hamiltonization cannot
prove (0.5), but the MSW/MNW route does.

## 1. The canonical complementary-geodesic factor

For `x in D_r`, the Chung--Feller factor supplies a path

\[
 P_x=(X^x_0,Y^x_0,X^x_1,Y^x_1,\ldots,
      Y^x_{r-1},X^x_r)                                \tag{1.1}
\]

in the incidence graph between ranks `r` and `r+1` of `Omega`, with

\[
 X^x_i\subset Y^x_i\supset X^x_{i+1},\qquad
 X^x_r=\overline {X^x_0}.                             \tag{1.2}
\]

After suppressing the `Y` vertices, (1.1) is a Johnson geodesic from a set
to its complement.  Hence there are pairwise distinct labels

\[
 \lambda^x_1,\ldots,\lambda^x_r\in X^x_0,
 \qquad
 \rho^x_1,\ldots,\rho^x_r\in\overline {X^x_0}         \tag{1.3}
\]

such that

\[
 X^x_j=
 \left(X^x_0\setminus\{\lambda^x_1,\ldots,
                         \lambda^x_j\}\right)
 \cup\{\rho^x_1,\ldots,\rho^x_j\}.                  \tag{1.4}
\]

The paths partition the rank-`r` shore and their intervening vertices
partition the rank-`r+1` shore.  Numerically,

\[
 Cr={r\over r+1}{2r\choose r}={2r\choose r+1},        \tag{1.5}
\]

as required.

## 2. The lifted MSW two-factor

Adjoin a new coordinate `z`.  For every (1.1), retain the `z`-free path
itself.  Its opposite path is

\[
 z+\overline {X^x_0},\quad
 z+\overline {Y^x_0},\quad
 z+\overline {X^x_1},\quad\ldots,\quad
 z+\overline {Y^x_{r-1}},\quad
 z+\overline {X^x_r},                                \tag{2.1}
\]

where the owner vertices `z+bar(X)` have rank `r+1` and the intervening
vertices `z+bar(Y)` have rank `r`.  Add the two vertical edges at the
endpoints.  Since `X^x_r=bar(X^x_0)`, this makes one cycle.

As `x` varies, these are `C` disjoint cycles covering all of
`ML(2r+1)`.  The `z`-free halves are exactly `mathcal P_r`; the
`z`-present halves use every rank-`(r-1)` subset of `Omega` after deleting
`z`, because the `Y` vertices in (1.1) enumerate rank `r+1` and
complementation sends that layer bijectively to rank `r-1`.

Each lifted cycle contains exactly one edge of the odd-graph wreath whose
omitted coordinate is `z`; in the middle-levels lift that edge is the pair
of vertical endpoint edges.  Preserving the `z`-free half is therefore the
same as preserving the endpoint matching (0.3) after the fixed half is
contracted.

## 3. Endpoint-augmented Hamiltonicity

Write

\[
 \mathcal L={\Omega\choose r-1},\qquad
 \mathcal R={\Omega\choose r}.
\tag{3.1}
\]

The shores have sizes

\[
                   |\mathcal R|=W,qquad
                   |\mathcal L|=W-C.                 \tag{3.2}
\]

### Lemma 3.1 (the matching is forced)

Every Hamilton cycle of `mathcal A_r` uses every edge of `M_r`.

#### Proof

Every vertex of `mathcal L` has both Hamilton-cycle edges in the
containment graph.  Thus the cycle uses exactly `2(W-C)` containment-edge
ends on the `mathcal R` shore.  The total degree demand on `mathcal R` is
`2W`, leaving exactly `2C` degree ends to be supplied by edges internal to
`mathcal R`.  The only such edges are the `C` independent edges of `M_r`,
and each supplies two ends.  All of them are therefore used. `square`

### Lemma 3.2 (remove the forced matching)

If `K` is a Hamilton cycle of `mathcal A_r`, then

\[
                         Q=K\setminus M_r             \tag{3.3}
\]

is a spanning `C`-path forest in the containment graph with endpoint set
exactly `E_r`.  Conversely, such a forest `Q` gives a Hamilton cycle of
`mathcal A_r` exactly when `Q union M_r` is connected.

#### Proof

After deleting `M_r`, every endpoint in `E_r` has degree one, every other
vertex has degree two, and no cycle component can remain because it would
already be a proper cycle component of `K`.  Hence (3.3) is a path forest
with `2C` endpoints and therefore `C` paths.  The converse is immediate:
adding `M_r` restores degree two at every endpoint, and a connected finite
degree-two graph is one cycle. `square`

### Theorem 3.3 (exact equivalence)

Statements (A)--(C) in (0.5) are equivalent.

#### Proof

Assume (A), and let `Q` be the forest from Lemma 3.2.  Interpret its
`mathcal R` vertices as the `z`-present owners `z+R` and its `mathcal L`
vertices as `z+L`.  Restore the fixed `z`-free paths `P_x` and the vertical
edge at every member of `E_r`.  Contracting each fixed path together with
its two vertical edges gives exactly the matching edge in `M_r`.  The
remaining edges are exactly `Q`.  Thus the restored graph is connected
because `Q union M_r` is the Hamilton cycle `K`; all vertices have degree
two, so it is a Hamilton cycle `H` of `ML(2r+1)`.  Its `z`-free projection
is `mathcal P_r`.  This proves (B) and (C).

Conversely, assume (C).  Delete the fixed `z`-free paths from `H` and
delete `z` from the remaining `z`-present vertices.  This leaves a spanning
containment path forest `Q` whose endpoint set is `E_r`.  Contracting each
fixed `P_x` and its two vertical edges gives the matching `M_r`.  Since
`H` was connected, `Q union M_r` is connected, and by Lemma 3.2 it is a
Hamilton cycle of `mathcal A_r`.  Thus (A) holds. `square`

### Theorem 3.4 (MNW prove the augmented Hamiltonicity)

For every `r>=3`, `mathcal A_r` has a Hamilton cycle.

#### Proof

Use the notation of MNW.  Their graph `G_r` is the incidence graph induced
by the weight-`r` and weight-`(r+1)` bitstrings of length `2r`.  Their graph
`G_r^+` adds the full complement matching on the weight-`r` shore.  For
every Dyck word `x in D_r`, their canonical path `P(x)` lies in `G_r`, runs
from `x` to `bar(x)`, and the paths partition `G_r`.  Their starting cycle
factor is exactly

\[
 \mathcal C_r=
 \{P(x)+\{x,\bar x\}:x\in\mathcal D_r\}.             \tag{3.4}
\]

The decisive support statement is part of their definition: a flipping
cycle is a cycle **in `G_r`**, not merely in `G_r^+`.  Their conflict-free
spanning-tree lemma selects a family of such flipping cycles whose
symmetric difference with (3.4) is one Hamilton cycle `K` in `G_r^+`.
Since every toggled edge belongs to `G_r`, none of the closure edges

\[
                   \{x,\bar x\},\qquad x\in\mathcal D_r,
\tag{3.5}
\]

is removed, and no other complement edge is inserted.  Thus `K` belongs to
the smaller spanning graph

\[
                         G_r+M_r.                     \tag{3.6}
\]

Complement every `2r`-bit vertex.  This maps the rank-`(r+1)` shore of
`G_r` to `binom(Omega,r-1)`, fixes the rank-`r` shore setwise, preserves
containment adjacency, and preserves every unordered edge
`{x,bar(x)}`.  Therefore (3.6) is isomorphic to `mathcal A_r`, and the
image of `K` is a Hamilton cycle of `mathcal A_r`. `square`

This uses more than the headline theorem that the odd graph is Hamiltonian.
It uses the support statement in the proof (the definition of flipping
cycles and the conflict-free spanning-tree reduction).  MNW themselves
invoke exactly this retained-closure property in their alternative proof
of the Middle Levels Theorem.

## 4. Every canonical path supplies a balanced stem

Fix `1<=s<=r`, set `h=s-1`, and take the first `s` Johnson edges of one
path (1.4):

\[
                  X_0,X_1,\ldots,X_h,X_s.             \tag{4.1}
\]

Put

\[
 Q=X_0\setminus\{\lambda_1,\ldots,\lambda_h\},
 \qquad q_+=\lambda_s,\qquad zeta=\rho_s.             \tag{4.2}
\]

Then `q_+ in Q`, `zeta notin X_h`, and

\[
 X_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
          \cup\{\rho_1,\ldots,\rho_j\}
             \quad(0<=j<=h),                         \tag{4.3}
\]

while

\[
 X_s=(Q\setminus\{q_+\})
          \cup\{\rho_1,\ldots,\rho_h\}\cup\{zeta\}.
\tag{4.4}
\]

Equations (4.2)--(4.4) are exactly the nonrepeated stem of the generalized
balanced collar (equations (2.14)--(2.16) of the pivot-gluing theorem).
Its `s` union colours are distinct because (4.1) is a geodesic: the
`j`-th union records the first `j` inserted labels and the not-yet-deleted
labels.

Different `P_x` are owner-disjoint, and their upper vertices in (1.1) are
globally disjoint.  Hence choosing the initial `s` edges on any `C-1`
paths gives `C-1` pairwise owner-disjoint stems with pairwise distinct
upper resources.  There is no packing or collision theorem left at this
stage.

### Corollary 4.1 (unconditional protected-stem theorem)

For every `r>=3`, there is a Hamilton cycle `H` of `ML(2r+1)` and a fixed
coordinate `z` such that `F_z(H)=mathcal P_r`.  Consequently the protected
initial-stem gate in the half-projection theorem holds for every `s<=r`, in
particular for `s=Theta(sqrt(r))`.

#### Exact half tracking

MNW's alternative middle-levels construction makes this assertion literal.
Start with their retained-closure Hamilton cycle in `G_r^+`, remove every
edge `{x,bar(x)}` with `x in D_r`, and replace it in the `z=1` half by the
complemented fixed path `bar(P(x))`.  Its `z=0` half is the rethreaded
forest and its `z=1` half is the fixed complemented MSW forest.  Now
complement every `(2r+1)`-bit vertex.  This is an automorphism of the
middle-levels graph, swaps the two shores, and sends

\[
                         \overline{P(x)},1
            \longmapsto P(x),0.                     \tag{4.5}
\]

Hence the `z`-free half of the complemented Hamilton cycle is exactly
`mathcal P_r`, with its original order up to harmless path reversal.  It is
not merely an unspecified conjugate or a factor with the same spectrum.

The corollary supplies the nonrepeated stems.  Any separate requirement on
the formal repeated left seam, declared terminal endpoints `P_j`, or a
specific component order remains part of the later collar-gluing theorem;
it is not hidden in this statement.

## 5. Odd-graph formulation

Fix `z` in the odd graph `KG(2r+1,r)`.  Relabel a `z`-free vertex `A` by
`bar(A) in binom(Omega,r)`, and relabel a `z`-present vertex `z+L` by
`L in binom(Omega,r-1)`.  Cross-sector odd-graph adjacency becomes

\[
                 A\cap(z+L)=\varnothing
       \quad\Longleftrightarrow\quad L\subseteq\bar A. \tag{5.1}
\]

The `z`-free odd-graph edges are the full complement matching on
`binom(Omega,r)`.  Therefore `mathcal A_r` is the spanning subgraph obtained
by retaining only the `C` complement edges `M_r` selected one per MSW
wreath.

Consequently (A) is equivalent to:

> The MSW minimum-cycle odd-graph factor can be Hamiltonized while
> preserving, in every wreath, its unique edge whose omitted coordinate is
> `z`, and using no other `z`-free complement edge.

The published MNW proof has exactly this restriction.  Its flipping cycles
lie wholly in `G_r`, so they touch no complement edge at all.  The selected
one-per-wreath complement edges survive unchanged and no unselected
complement edge enters.  This is the content used in Theorem 3.4.

## 6. Why the lexical route cannot substitute

The GMN lexical factor and the MSW complementary-geodesic factor are
different path factors.  For the lexical factor, the exact number of
fixed-`z` paths with `2h` owners is

\[
          \operatorname {Cat}_{h-1}\operatorname {Cat}_{r-h}.
\tag{6.1}
\]

For every `s to infinity` with `s=o(r)`, asymptotically one half of those
paths have fewer than `s` Johnson edges.  Moreover the canonical GMN
equal-depth suffix pulls preserve the multiset (6.1).  Hence no choice of
its pull tree can produce `C-1` length-`s` stems.

By contrast, every MSW path in (0.2) has exactly `r` Johnson edges.  The
MNW endpoint-preserving Hamiltonization turns this perfect spacing into the
required middle-levels Hamilton cycle.

## 7. Closed theorem and remaining downstream boundary

Combining Theorems 3.3--3.4 and Corollary 4.1 gives:

\[
 \boxed{
 \textbf{MSW endpoint-augmented Hamiltonicity: }
 \mathcal A_r\text{ is Hamiltonian for every }r\ge3. }
\tag{7.1}
\]

and

\[
 \boxed{
 \begin{gathered}
 \text{There is }H\subseteq ML(2r+1)\text{ and a coordinate }z\\
 \text{whose }z\text{-free projection is the canonical family of }C
 \text{ complementary }r\text{-edge geodesics.}
 \end{gathered}}
\tag{7.2}
\]

Thus the Catalan-scale bank of `C-1` initial balanced stems is not a
remaining owner/upper-q1 conjecture.  It is an imported all-dimensional
theorem.

What (7.2) does **not** settle is downstream compiler structure not encoded
by the nonrepeated stems: a prescribed formal repeated left seam, arbitrary
declared terminal endpoints `P_j`, a particular formal component order,
deeper upper shadows, or residence for coordinates other than the protected
run coordinate.  Those must be charged to their own later gates; they must
not be folded back into the now-closed spacing statement.

In fact the frozen canonical endpoints cannot satisfy the first three of
those stronger requirements for `r>=4`.  The exact characterization in
`MATH_THEOREM_MSW_CANONICAL_SEAM_ENDPOINT_CHARACTERIZATION_AND_PRIMITIVE_NOGO_20260805.md`
shows that `Cat_(r-1)-1` primitive MSW components have no legal repeated-seam
predecessor in either orientation.  Thus endpoint repair or a longer
interface is genuinely necessary; the unconditional theorem here should
not be overextended to the full collar-adapted normal form.

## 8. Small-rank audit

The MNW odd-graph Hamiltonization theorem used above applies for `r>=3`.
The small cases behave as follows.

* `r=1`: `A_1` is a triangle and (7.1) holds directly.
* `r=2`: `G_2^+` is the Petersen graph.  Hence neither it nor the spanning
  subgraph `A_2` has a Hamilton cycle.  This is the unique exception to
  (7.1).

The exception does not affect the asymptotic protected-stem theorem.  The
middle-levels graph itself is Hamiltonian at `r=2`; only this particularly
rigid one-sided MSW projection fails there.  Any finite induction using the
protected bank should therefore start at `r>=3` (or handle `r=2` by its
separate explicit middle-levels cycle).
