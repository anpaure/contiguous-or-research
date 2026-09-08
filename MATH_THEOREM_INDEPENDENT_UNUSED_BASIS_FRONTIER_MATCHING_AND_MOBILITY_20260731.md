# Fixed unused bases: exact frontier Hall duality, alternating mobility, and the K16 Tucker obstruction

Date: 2026-07-31  
Status: exact reduction and authenticated finite-host audit  
Scope: the compiler half of the transparent-packet `B(k)+O(1)` route

## 0. Verdict

The transparent-unused-basis interface removes common-cap paths from every
packet.  Once one trace-guarded compiler matching `M_0` is fixed, a packet's
entire compiler ticket is one unused cell.  Consequently:

1. cap-ticket row energy collapses to ordinary cell-collision energy;
2. selecting distinct packet cells is an ordinary task--cell Hall problem;
3. constructing `M_0` with unused prefixes dominating a residence frontier
   is exactly a target--cell matching problem after deleting one Ferrers
   ideal of cells; and
4. alternating paths give the exact mobility certificate for moving a
   matching off that ideal.

The exact obstruction is

\[
 \delta_H(D)=|\mathcal L|-\nu\bigl(H[\mathcal L,C-D]\bigr)
 =\max_{X\subseteq\mathcal L}
       \bigl(|X|-|N_H(X)\setminus D|\bigr).                       \tag{0.1}
\]

Here `D` is the residence-deletion ideal.  Equality at coefficient one
needs `delta_H(D)=0`; a bounded sidecar needs a uniform absolute bound on
this quantity plus literal repair of the omitted targets.

The deletion geometry is Ferrers, but the actual compiler graph need not be
convex.  In the authenticated K16 complete individual-incidence graph, the
three targets

\[
                  0x0080,\quad0x008a,\quad0x0882
\]

and the singleton cells at starts `223,0,979` induce

\[
             \begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}.    \tag{0.2}
\]

This is the Tucker `M_I(3)` obstruction: no ordering of the cells makes all
three target neighbourhoods intervals.  Thus cap congestion really does
collapse to ordinary Hall, but not automatically to one-dimensional
Ferrers-prefix inequalities.  A pruned trace-guarded convex bank would still
suffice; constructing it is an additional theorem.

The same K16 certificate gives the positive calibration.  Its exact common-
cap matching has first used starts

\[
                           u=(0,2,6390),                            \tag{0.3}
\]

while its residence frontier is

\[
                         \rho=(0,0,6384).                           \tag{0.4}
\]

Hence `u>=rho` componentwise.  This is a genuine instance, not a uniform
construction.

## 1. Forced-core contraction and the fixed guarded bank

Let `H=(L,C;E)` be a trace-guarded target--cell bank in the sense of the
guarded common-cap theorem.  Every target-saturating matching in `H` is then
a literal exact common-cap compiler.

Contract every forced target--cell incidence and delete its target and cell.
If a requested residence prefix contains a forced used cell, the face is
immediately infeasible.  Otherwise write the residual bank again as `H`.

For depth `d`, order the maximal tail-start cells within each row by their
start:

\[
                    C_{i,\ell}=[i,i+\ell-1],
             \qquad1\le\ell\le d.                                 \tag{1.1}
\]

For a nondecreasing residence frontier
`rho=(rho_1,...,rho_d)`, define its Ferrers deletion ideal

\[
                 D(\rho)=\{C_{i,\ell}:0\le i<\rho_\ell\}.          \tag{1.2}
\]

A target-saturating matching `M` has unused-prefix vector `u(M)>=rho` if and
only if no matched cell belongs to `D(rho)`.

## 2. Exact frontier deficiency

### Theorem 2.1 (frontier Hall duality)

Assume `H` has a target-saturating matching.  For any cell set `D`, define

\[
 \delta_H(D)=\min_M |\operatorname{cells}(M)\cap D|,               \tag{2.1}
\]

where the minimum is over all target-saturating matchings in `H`.  Then

\[
\begin{aligned}
 \delta_H(D)
   &=|\mathcal L|-\nu\bigl(H[\mathcal L,C-D]\bigr)\\
   &=\max_{X\subseteq\mathcal L}
          \left(|X|-|N_H(X)\setminus D|\right).                   \tag{2.2}
\end{aligned}
\]

In particular, a trace-guarded matching with unused-prefix vector at least
`rho` exists if and only if

\[
             |N_H(X)\setminus D(\rho)|\ge|X|
                    \qquad(X\subseteq\mathcal L).                 \tag{2.3}
\]

#### Proof

Let `H_0=H[L,C-D]` and let its maximum matching size be `r`.  Any full
matching uses at most `r` cells outside `D`, so it uses at least
`|L|-r` cells of `D`.

Conversely choose an `r`-edge matching in `H_0`.  Regard its `r` right cells
as an independent set in the transversal matroid on `C` induced by the left
shore `L`.  Since `H` has rank `|L|`, extend this independent set to a basis
of that transversal matroid.  A basis matching saturates `L`, retains all
`r` chosen outside cells, and therefore uses exactly `|L|-r` cells of `D`.
This proves the first equality.  The deficiency form of Hall's theorem gives

\[
 |L|-r=\max_{X\subseteq L}(|X|-|N_{H_0}(X)|),
\]

which is the second equality.  Trace guarding turns any matching witnessing
zero deficiency into an exact common cap.  \(\square\)

### Corollary 2.2 (bounded compiler sidecar)

Suppose a terminal repair theorem can realize any `c` omitted lower targets
at absolute extra cost `g(c)`.  If every reachable frontier satisfies

\[
                         \delta_H(D(\rho))\le c,                   \tag{2.4}
\]

then the compiler contributes at most `g(c)` to the additive error.  Thus an
absolute uniform deficiency suffices for `B(k)+O(1)`, while zero deficiency
is the coefficient-one row.

This corollary requires a literal terminal repair.  Merely deleting
`delta_H(D)` targets is not itself a universal-word construction.

### Corollary 2.3 (one matching for a whole reachable frontier family)

Let \(\mathfrak R\) be any family of nondecreasing residence frontiers and define its
componentwise maximum

\[
                  \rho^*_\ell=\max_{\rho\in\mathfrak R}\rho_\ell. \tag{2.5}
\]

One trace-guarded matching has `u(M)>=rho` for **every**
\(\rho\in\mathfrak R\) if and only if

\[
                         \delta_H(D(\rho^*))=0.                   \tag{2.6}
\]

#### Proof

The maximum of nondecreasing vectors is nondecreasing, and

\[
             \bigcup_{\rho\in\mathfrak R}D(\rho)=D(\rho^*).
\]

A common matching works for the family exactly when it avoids this union;
apply Theorem 2.1.  \(\square\)

Thus a bounded/O(`d`) macro state family does not create a new cap object:
for a common compiler face it creates one worst-frontier matching test.
Hopcroft--Karp on `H-D(rho^*)` either constructs the matching or returns an
alternating-reachability Hall witness.  Weighted/min-cost matching can be
used when several feasible frontiers are to be optimized lexicographically,
but it is not needed for the decision theorem.

## 3. Alternating-path mobility

Fix one target-saturating matching `M`.  Direct its alternating exchange
graph as follows.  From a matched cell `c=M(S)` pass through its target `S`
to every alternative cell `c' in N_H(S)-{c}`.  A path ends successfully at
a cell unused by `M` and outside `D`.

### Theorem 3.1 (exact prefix-clearing linkage)

There is a target-saturating matching `M'` avoiding `D` if and only if the
cells `cells(M) intersect D` are the initial endpoints of pairwise
vertex-disjoint `M`-alternating paths ending at distinct `M`-unused cells
outside `D`, with every noninitial cell of every path outside `D`.

#### Proof

If the paths exist, flip `M` along all of them.  Disjointness preserves a
matching, every path moves one used cell from `D` to a distinct safe unused
cell, and no path re-enters `D`.

Conversely let `M'` avoid `D`.  Every component of `M triangle M'` is an
alternating cycle or an even alternating path.  A cell of `cells(M) cap D`
cannot be internal or incident with an `M'` edge, so it is the `M`-endpoint
of a path.  The other endpoint is an `M'`-used, `M`-unused cell outside `D`.
The components are disjoint and give the required linkage.  \(\square\)

This is the exact alternating-path form of (2.3).

### Corollary 3.2 (private one-cell mobility)

Let `R` be a possible-risk bank of matched cells.  If every `c in R` has a
distinct currently unused safe cell `phi(c)` with

\[
                       \phi(c)\in N_H(M^{-1}(c)),                  \tag{3.1}
\]

then every frontier `D subseteq R` can be cleared simultaneously by direct
one-edge exchanges.

Private alternates are sufficient, not necessary.  The exact weaker
condition is the alternating-linkage rank in Theorem 3.1.

### Proposition 3.3 (smallest mobility obstructions)

1. One target `S`, cells `a,b`, and the sole edge `S-a` have one unused cell
   and scalar slack one, but the frontier `D={a}` has deficiency one.
2. With targets `S_1,S_2`, current cells `a_1,a_2`, one unused safe cell `z`,
   and edges `S_i-a_i,S_i-z`, each one-cell frontier can be cleared, but
   `D={a_1,a_2}` has deficiency one.

Thus aggregate unused capacity does not imply even one-cell mobility, and
individual mobility does not compose without Hall/linkage expansion.

The first pattern occurs literally in the K16 Pascal host: after the
`0x8000` pin is imposed, that singleton has exactly one physical cell, the
length-one cell at start `6389`, despite thousands of other unused cells.
The actual K16 residence frontier does not delete this cell, but any proposed
frontier which did would fail by this one-row Hall cut.

## 4. Joint packet and compiler matching

The fixed-unused-basis interface can be co-designed without alternating cap
paths.

Let `I` be transparent packet tasks and let `A_i subseteq C` be the cells
which task `i` can delete.  Let `D_0` be a fixed residence ideal not already
accounted for by tasks.  Form one bipartite graph with left shore

\[
                  \mathcal L\ \dot\cup\ I\ \dot\cup\ R_0,        \tag{4.1}
\]

where

* a lower target `S` has its trace-guarded edges in `H`;
* task `i` has neighbours `A_i`; and
* for every `c in D_0`, one reservation vertex has the singleton neighbour
  `{c}`.

For the co-designed statement, a task--cell edge is retained only when its
physical option is **bank transparent**: apart from deleting its named cell,
it preserves every incidence and trace guard of `H` which could belong to a
disjoint target matching.  If transparency has been checked only against one
already selected `M_0`, use the fixed-`M_0` task--cell Hall problem instead;
the joint theorem below would otherwise reverse a load-bearing quantifier.

### Theorem 4.1 (joint unused-basis Hall theorem)

A matching saturating (4.1) is equivalent to the simultaneous choice of

1. one trace-guarded compiler matching `M_0`;
2. one distinct deletion cell for every packet task; and
3. all fixed residence cells unused by `M_0` and by the other tasks.

It exists if and only if the ordinary Hall inequalities hold in this one
combined graph.

#### Proof

In a saturating matching, reservation and task cells are distinct.  The
lower-target edges therefore use none of them and form `M_0`; trace guarding
makes it exact.  Conversely the three displayed objects are disjoint and
their union is a matching saturating (4.1).  Hall's theorem is exact for
this bipartite graph.  \(\square\)

This is the strongest genuine collapse supplied by compiler transparency:
the common cap becomes ordinary matching.  Physical packet compatibility,
upper/internal transparency and regeneration remain separate rows.

For a bounded-defect statement, fixed reservation vertices are not allowed
to be the unmatched ones.  Contract their forced singleton edges first and
write `G_res` for the residual graph on lower targets, packet tasks and the
remaining cells.  Define the **combined deficiency**

\[
            \delta_{comb}=|\mathcal L|+|I|-\nu(G_{res}).           \tag{4.2}
\]

Thus `delta_comb` counts only lower targets and packet tasks left for the
declared terminal sidecar; every fixed residence reservation remains exact.

If every neighbourhood in the combined graph is an interval in one common
cell order, Theorem 4.1 reduces to the interval-capacity inequalities and
earliest-deadline greedy.  Singleton reservation rows are already intervals.
Without target-neighbourhood convexity the full Hall system remains.

## 5. Compiler row energy on the lean face

For a fixed `M_0`, let `P_i` be the physical options for task `i`, each naming
one deletion cell `b(p) in B=C-cells(M_0)`.  Put

\[
 a_i(b)=|\{p\in P_i:b(p)=b\}|,
 \qquad A(b)=\sum_j a_j(b).                           \tag{5.1}
\]

### Theorem 5.1 (exact cell-only energy)

The compiler-token witness row is exactly

\[
 R_i^B={1\over|P_i|}\sum_{b\in B}a_i(b)(A(b)-a_i(b)).              \tag{5.2}
\]

If one physical realization is retained for each eligible task--cell pair,
then

\[
 R_i^B={1\over|N(i)|}\sum_{b\in N(i)}(\deg(b)-1)
       \le\Delta_B-1.                                             \tag{5.3}
\]

#### Proof

This is Theorem 1.1 of the full-ticket row-energy note with the token set
reduced to the single named cell.  In the simple task--cell graph,
`a_i(b)` is zero or one and `A(b)=deg(b)`.  \(\square\)

If Theorem 4.1 is solved jointly, compiler cell collisions are satisfied
exactly and need not be charged to Haxell at all.  The residual row energy is
only physical/internal packet conflict.  This is the main quantitative gain
over attaching an alternating common-cap path to every option.

## 6. Ferrers duality and its limit

For one fixed matching `M_0`, the residence statement itself is Ferrers:
`u(M_0)>=rho` exactly when `D(rho)` lies in its unused basis.  This is the
fixed-basis prefix theorem.

Finding `M_0`, however, uses the restricted target graph

\[
                           H_\rho=H[\mathcal L,C-D(\rho)].         \tag{6.1}
\]

If the target neighbourhoods of `H_rho` are intervals in one cell order,
zero deficiency is equivalent to

\[
 \left|\{S:N_{H_\rho}(S)\subseteq[a,b]\}\right|
                       \le b-a+1                                  \tag{6.2}
\]

for every cell interval `[a,b]`.  This is a valid proof route.

The Ferrers shape of `D(rho)` alone does not imply interval neighbourhoods
in `H_rho`.  The authenticated K16 bank gives a literal obstruction.

### Theorem 6.1 (actual K16 complete-bank Tucker obstruction)

In the complete individually sound residual K16 compiler graph frozen in
the exact `nu(16)=12873` certificate, take cells

\[
 C_1=(223,1),\qquad C_2=(0,1),\qquad C_3=(979,1)                  \tag{6.3}
\]

and targets

\[
 S_1=0x0080,\qquad S_2=0x008a,\qquad S_3=0x0882.                 \tag{6.4}
\]

Their incidence matrix is (0.2).  Therefore no ordering of the complete
cell bank makes every target neighbourhood an interval.

#### Proof

The frozen map contains exactly the six displayed incidences and omits the
three complementary incidences on these rows and columns; the audit script
replays this directly.  In any ordering of three columns, one column is
middle.  The row omitting that middle column has ones at both ends and a
zero between them, contradicting consecutive ones.  Consecutive-ones
matrices are closed under deleting rows and columns, so no ordering of the
full bank can repair the obstruction.  \(\square\)

This does not refute a **pruned trace-guarded convex subbank**.  The complete
K16 individual-incidence bank is not trace guarded: arbitrary marginal
matchings can destroy middle traces.  The theorem says that convexity must
be constructed by correlated pruning; it is not inherited from Pascal cell
geometry.

## 7. K16 positive frontier calibration

The exact K16 common-cap model selects `26,332` distinct cells from `32,230`,
leaving `5,898` unused cells.  Reading the selected matching gives

\[
\begin{array}{c|ccc}
\text{cell length}&1&2&3\\ \hline
\text{first used start }u_\ell&0&2&6390\\
\text{residence frontier }\rho_\ell&0&0&6384.
\end{array}                                                     \tag{7.1}
\]

Thus the exact winner has six units of length-three prefix margin.  This
authenticates the fixed-unused-basis mechanism at the first even depth-three
case.  It does not give a preselection description of a large matching-
complete guarded bank: the selected matching itself supplies the guards ex
post.

## 8. Exact sufficient theorem for bounded regenerative defects

The compiler half of a `B(k)+O(1)` induction is closed by the following
package.

### Theorem 8.1 (frontier-mobile guarded-bank implication)

Assume that after forced-core contraction, every state in one bounded
reachable regenerative family has:

1. a trace-guarded bank `H`;
2. a residence ideal `D(rho)` and transparent packet task lists represented
   in the joint graph (4.1);
3. combined Hall deficiency (4.2), after contracting every fixed
   reservation, at most an absolute constant `c`;
4. a literal bounded terminal repair for the at most `c` omitted obligations
   (lower targets or packet tasks);
5. physical/internal transparent options for the selected task--cell edges,
   compatible on the common connector; and
6. regeneration into the same bounded family.

Then the compiler contributes only `O(1)` to the word length.  If `c=0`, it
contributes zero.

#### Proof

Apply the deficiency form of Hall to (4.1), omit at most `c` unmatched lower
tasks/targets as declared by the terminal-repair interface, and use the
matching for all other target and packet cells.  Trace guarding preserves the
same `M_0`; transparent unused-basis composition removes cap-path and upper-
witness recourse.  The bounded repair pays the omissions and clause 6 closes
the induction.  \(\square\)

The theorem is exact but conditional in the one place that matters.  The
next construction target is not a cap router.  It is a guard-safe incidence
bank with uniformly bounded combined Hall deficiency against the reachable
Ferrers ideals, preferably equipped with private direct alternates as in
Corollary 3.2.

## 9. Dependencies and scope

This note uses:

* `MATH_THEOREM_O1_TRANSPARENT_PACKET_UNUSED_BASIS_COMPOSITION_20260731.md`;
* `MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md`;
* `MATH_THEOREM_PROSPECTIVE_COMMON_BASIS_AVOIDANCE_AND_COMPILER_DUAL_RADO_20260731.md`; and
* `MATH_THEOREM_INDEPENDENT_FULL_TICKET_ROW_ENERGY_AND_CAP_BOTTLENECK_20260731.md`.

It proves the compiler reduction and audits the actual K16 host.  It does
not construct the uniform trace-guarded subbank, transparent packet menus,
physical common connector, or regenerative terminal repair.
