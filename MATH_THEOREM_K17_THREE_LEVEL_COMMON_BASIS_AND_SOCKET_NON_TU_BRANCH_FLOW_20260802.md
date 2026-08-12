# K17 three-level common basis and the socket non-TU branch--flow gate

**Date:** 2026-08-02  
**Status:** exact static equivalence and polynomial common-basis algorithm;
exact conditional flow decomposition for the marginal socket rows; no claim
that the socket-expanded instance is solved.

## 1. Three layers

Let

\[
 L=\binom{[17]}1\cup\cdots\cup\binom{[17]}6,
 \quad M=\binom{[17]}7,
 \quad R=\binom{[17]}8.
\]

Their sizes are

\[
 |L|=21777,\qquad |M|=19448,\qquad |R|=24310.       \tag{1.1}
\]

Write `l~m`, `l~r`, and `m~r` for strict Boolean containment.  A no-singleton
three-level table chooses

* one edge `x_mr` from every `m in M` to a distinct root `r in R`;
* one edge `y_lm` or `y_lr` from every `l in L`;
* exactly one incoming selected edge at every root `r`; and
* at most one selected lower predecessor at every `m`.

Equivalently,

\[
\begin{aligned}
 \sum_r x_{mr}&=1 &&(m\in M),\\
 \sum_mx_{mr}+\sum_ly_{lr}&=1 &&(r\in R),\\
 \sum_my_{lm}+\sum_ry_{lr}&=1 &&(l\in L),\\
 \sum_l y_{lm}&\le1 &&(m\in M).                     \tag{1.2}
\end{aligned}
\]

Counting forces `16915` chains `l-m-r`.  The remaining `2533` middle
targets form `m-r` chains and the remaining `4862` low targets form `l-r`
chains, for exactly

\[
                       (n_1,n_2,n_3)=(0,7395,16915). \tag{1.3}
\]

Without extra socket rows, (1.2) is the bipartite matching incidence system
with left shore `L_out disjoint_union M_out` and right shore
`M_in disjoint_union R_in`; hence its displayed matrix is totally
unimodular.

## 2. Exact two-matroid reduction

Let `M_7` be the rank-`19448` transversal matroid on ground set `R`: a root
set is independent when its roots can be matched injectively to distinct
contained rank-seven targets.
Let `M_L` be the rank-`21777` transversal matroid on ground set

\[
                         E=M\mathbin{\dot\cup}R,
\]

where a set is independent when all of its receiver vertices can be matched
injectively to distinct contained low targets.  Finally put

\[
             N=M_7^*\oplus U_{16915,M}.              \tag{2.1}
\]

The first summand lives on `R`; the second is the rank-`16915` uniform
matroid on `M`.  Both `M_L` and `N` have rank `21777`.

### Theorem 2.1 (common basis iff exact static normal-form table)

A set `C subset E`, together with representing matchings, is a common-basis
witness for `M_L` and `N` if and only if it is the receiver set of an exact
no-singleton **three-level normal-form** table satisfying (1.2).  Here normal
form means that every chain is exactly one of

\[
             l-m-r,\qquad l-r,\qquad m-r.           \tag{2.1a}
\]

In particular, a length-three chain containing two comparable members of
`L` is excluded.  The histogram alone does not imply this normal form.  The
correspondence is between tables and triples `(C,mu_L,mu_7)`, not between
tables and the element set `C` alone: one common basis can have several
representing matchings.

#### Proof

Suppose first that `C` is a common basis.  Since it is a basis of `N`,

\[
 |C\cap M|=16915,qquad |C\cap R|=4862,              \tag{2.2}
\]

and `C_R=C cap R` is a basis of `M_7^*`.  Therefore

\[
                         B=R-C_R                     \tag{2.3}
\]

is a basis of `M_7`.  Choose a matching of all low targets into `C`, and a
matching of all rank-seven targets into `B`.  A low target matched to
`m in C cap M` followed by the rank-seven edge out of `m` gives an
`l-m-r` chain.  A low target matched to `r in C_R` gives an `l-r` chain.
Every `m outside C` gives an `m-r` chain.  The two receiver shores
`C_R,B` partition `R`, so every target and root is used exactly once and
(1.2) holds.

Conversely, read any table satisfying (1.2).  Let `C_M` be the middle
vertices having a low predecessor and `C_R` the roots having a direct low
predecessor.  The selected `y` edges match all low targets into
`C=C_M disjoint_union C_R`, so `C` is a basis of `M_L`.  The selected `x`
edges match all rank-seven targets into `B=R-C_R`, making `B` a basis of
`M_7`, hence `C_R` a basis of `M_7^*`.  The counts give
`|C_M|=16915`; therefore `C` is also a basis of `N`. \(\square\)

### Corollary 2.2 (exact static algorithm)

Static global recoupling in the normal form (2.1a) is ordinary weighted
matroid intersection.  For an arbitrary subset, transversal independence
means that the chosen receiver subset is saturated by distinct witnesses;
only a full-size basis matching necessarily uses every target on the witness
shore.  The independence oracle for `M_L` is one containment matching.  For
the dual
summand use

\[
 r_{M_7^*}(X)=|X|-r(M_7)+r_{M_7}(R-X),              \tag{2.4}
\]

again obtained from a containment matching; the uniform summand is a
cardinality oracle.  Protected receiver elements are handled by common
deletion/contraction minors after checking that every forced element is
independent in both matroids and that both residual ranks equal the required
remaining basis cardinality (not merely each other).
Additive **receiver-element** root/menu prices may
therefore be optimized exactly on this static face.  Prices depending on a
chosen matching witness or occurrence state are not ground-set weights and
remain outside this corollary.

This is stronger than treating root recoupling as an arbitrary chronology
move.  It does not choose compatible occurrence-labelled socket witnesses.

The exact unweighted min--max is Edmonds' common-basis criterion

\[
 r_{M_L}(X)+r_N(E-X)\ge21777\qquad(X\subseteq E).     \tag{2.4a}
\]

Writing `X_M=X cap M` and `X_R=X cap R`, this is the explicit matching-rank
family

\[
\boxed{
 r_{M_L}(X)+4862-|X_R|+r_{M_7}(X_R)
 +\min\{16915,|M-X_M|\}\ge21777 .}                  \tag{2.4b}
\]

Thus any failed static recoupling has a proof-safe cut consisting only of
two containment-matching ranks and one cardinality term.

### Corollary 2.3 (root retirement is common-basis exchange)

In a current common basis `C`, put `B=R-C_R`.  To retire a bad physical root
`b in B` from the rank-seven receiver bank and promote `r in C_R`, set

\[
 B'=B-b+r,\qquad C'=C-r+b.                           \tag{2.5}
\]

This exchange is statically legal exactly when

\[
 B'\text{ is a basis of }M_7
 \quad\text{and}\quad
 C'\text{ is a basis of }M_L.                       \tag{2.6}
\]

Relative to representing matchings, the first test is a fundamental
alternating path in the rank-seven/root containment graph: `b` must belong to
the fundamental circuit of `r` over `B`.  The second is a separate
alternating-path test in the low/receiver graph.  Passing the first test does
not imply the second.  For a batch of retirements, Edmonds' weighted
common-basis exchange graph performs the necessary correlated sequence and
may also exchange elements of `C cap M`.  Thus one need not repair the same
old P2 label at the same root.  Protected roots/receivers are imposed as
deletion/contraction minors before the exchange graph is built.

For element weights, weighted matroid intersection optimizes this correlated
exchange exactly.  Minimum root-bank Hamming change, for example, is a linear
weight on `C cap R`.  A hard retirement is imposed by deletion/contraction or
an explicit membership constraint; a finite weight merely encourages it.

### Lemma 2.4 (element weights cannot encode occurrence sockets)

No weight on the common-basis ground elements alone can enforce a property
of the representing matching edge.  Already on a `K_(2,2)` rank-seven/root
graph, let only the two diagonal matching edges be socket-positive.  The
same root basis has both the positive diagonal representation and the
negative off-diagonal representation, so every element-weight vector assigns
them the same value.  The same issue occurs on the low-receiver matching.

Hence weighted matroid intersection is an exact outer allocator and pricing
oracle, but the selected matching witnesses and their occurrence-labelled
DNFs must remain explicit in the inner master.

### Corollary 2.5 (specialized min-cost-flow implementation)

For receiver-element weights, the K17 common-basis optimization can be
implemented more directly as one min-cost version of the bipartite
`x/y`-matching system (1.2).  Give every `y_lm` edge cost `w_m`, every
`y_lr` edge cost `w_r`, and every `x_mr` edge cost zero.  Each receiver in
`C` is used by exactly one `y` edge, so the flow objective is exactly

\[
                         \sum_{v\in C}w_v.
\]

The integral min-cost flow returns the common basis and both representing
matchings simultaneously.  A cost on the complementary root bank
`B=R-C_R` is either put directly on `x_mr` or converted to a cost on `C_R`
by subtracting the constant total root weight.  Forced or forbidden
receiver membership is a lower or upper bound on that receiver's incoming
`y` degree, subject to feasibility.

This is an implementation specialization of weighted matroid intersection,
not an occurrence-socket lift: costs or constraints depending on *which*
`l` or `m` supplies a receiver remain matching-edge data.

## 3. Marginal socket rows

Fix the owner/carrier occurrence associated with every candidate receiver.
Let `q_lr` say that the direct short `l-r` has at least one admissible
occurrence-labelled socket DNF, and let `p_mr` say the same for `m-r`.  If
the owner is itself variable, these are occurrence variables rather than the
unary predicates used here.

Marginal positivity deletes every direct edge with `q_lr=0`.  This merely
changes the presentation of `M_L` to another transversal matroid, so the
common-basis theorem and weighted algorithm remain exact for this direct-low
marginal condition.  A middle edge `m-r` may be socket-negative only when
`m` receives a low predecessor.  Writing

\[
                         z_m=\sum_l y_{lm},
\]

the exact integer marginal rows are

\[
                    x_{mr}\le p_{mr}+z_m.            \tag{3.1}
\]

Using `sum_r x_mr=1`, the aggregate row

\[
             z_m+\sum_{r:p_{mr}=1}x_{mr}\ge1        \tag{3.1a}
\]

is equivalent to (3.1) on integral `x`.  It is stronger fractionally:
(3.1) makes `z_m` dominate the largest selected negative edge, while
(3.1a) makes it dominate their sum.  They must not be treated as the same
LP row.

The occurrence-labelled master must replace the Boolean predicates by the
full endpoint/state DNFs.  Equation (3.1) is only their union projection.

### Proposition 3.1 (the literal socket implications are not TU in general)

Suppose one middle has two socket-negative containing-root choices `r_1,r_2`.
Take its exact-one row and the two literal implications in (3.1).  On columns
`x_(m,r_1),x_(m,r_2),z_m` their submatrix is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&-1\\
 0&1&-1
 \end{pmatrix},
 \qquad\det=2.                                      \tag{3.2}
\]

There is also an objective-gap witness for the literal formulation.  Take
`M={a,b}`, `R={1,2}`, one low target which may feed either middle, complete
middle/root containment, and

\[
 p_{a1}=p_{b2}=1,\qquad p_{a2}=p_{b1}=0,
 \qquad z_a+z_b=1.                                  \tag{3.3}
\]

The all-half point `x_(ij)=1/2`, `z_a=z_b=1/2` satisfies the doubly
stochastic equations and (3.1), and has
`x_(a,2)+x_(b,1)=1`.  Integrally, the off-diagonal matching would require
both middles to have a low predecessor, contradicting `z_a+z_b=1`; only the
diagonal matching is feasible and that objective is zero.  Thus the natural
witness polytope is nonintegral.

This rules out importing base matching integrality after merely appending
(3.1).  It does not prove that no larger, problem-specific TU extended
formulation exists.  Branch plus matching-flow separation is the presently
proof-safe exact formulation.

## 4. Exact branch--flow and min-cut formulation

Put `h_m=1` when `m` receives a low predecessor and `d_r=1` when `r`
receives a low predecessor directly.  A compact integer master is

\[
\begin{aligned}
 \sum_r x_{mr}&=1 &&(m\in M),\\
 \sum_m x_{mr}+d_r&=1 &&(r\in R),\\
 \sum_m h_m&=16915,\\
 x_{mr}&\le p_{mr}+h_m &&(m\subset r),              \tag{4.1}
\end{aligned}
\]

with containment-forbidden `x` absent and `x,h,d` binary.  Summing the root
rows forces `sum_r d_r=4862`.  Thus `x` explicitly witnesses that
`B={r:d_r=0}` is an `M_7` basis and enforces the conditional rank-seven
short predicate.

For fixed master values, the low recourse is

\[
\begin{aligned}
 \sum_m y_{lm}+\sum_r y_{lr}&=1 &&(l\in L),\\
 \sum_l y_{lm}&=h_m &&(m\in M),\\
 \sum_l y_{lr}&=d_r &&(r\in R),                     \tag{4.2}
\end{aligned}
\]

where `l-m` is present only for containment and `l-r` only for containment
with `q_lr=1`.  This is one bipartite flow.

For `S subset L`, define

\[
\begin{aligned}
 N_M(S)&=\{m:\exists l\in S,\ l\subset m\},\\
 N_R^q(S)&=\{r:\exists l\in S,\ l\subset r,\ q_{lr}=1\}.
\end{aligned}
\]

### Theorem 4.1 (exact low-flow Benders oracle)

The recourse (4.2) exists if and only if

\[
 \boxed{\displaystyle
   \sum_{m\in N_M(S)}h_m+
   \sum_{r\in N_R^q(S)}d_r\ge |S|
   \qquad(S\subseteq L).}                           \tag{4.3}
\]

These inequalities are separated by one minimum cut in the network
`source -> L -> (M disjoint_union R) -> sink`, using unit source arcs,
allowed containment arcs, and sink capacities `h_m,d_r`.  This also
separates fractional master points.  With integral master values and all
cuts (4.3), bipartite-flow integrality returns an integral `y`.  Therefore
(4.1)--(4.3) are an exact branch--Benders formulation for the two stated
marginal socket predicates.

Equivalently, one may branch only on `(h,d)`.  For fixed `(h,d)`, the low
flow above and the rank-seven matching from `M` to `{r:d_r=0}`, with
negative `m-r` edges allowed only when `h_m=1`, are two independent ordinary
matching oracles.  Keeping `x` in the master is preferable once the actual
socket occurrences on the selected rank-seven/root edges must be named.

Deleting `q`-negative direct-low edges and running weighted matroid
intersection gives an exact common-basis outer relaxation, including any
additive receiver/root-type objective.  It supplies `(h,d)` branches and
fundamental basis exchanges.  Constraint (3.1), however, depends on the
representing `M_7` matching edge, so ordinary element-weighted matroid
intersection cannot enforce it.  The witness `x` plus min-cut family (4.3)
is the exact lift.

The following two conditioned views remain useful diagnostics.

### Fix `x`

Let `R_0` be the `4862` roots not hit by `x`, and let

\[
 D_M=\{m:p_{m,r(x,m)}=0\}.                            \tag{4.4}
\]

Then `y` must be a matching saturating every `l in L`, every root in `R_0`,
and every middle in `D_M`; other middle receivers are optional.  This is a
bipartite flow with lower bounds on the mandatory right vertices.  It has
an exact max-flow/min-cut oracle and returns either a completion or a Hall
shore.  Direct `L-R` arcs are already filtered by `q_lr`.

### Fix `y`

Fix an integral `y` satisfying every low-target degree equation and the
receiver capacity inequalities inherited from (1.2).  Put
`C_R={r:sum_l y_lr=1}` and
`S_M={m:sum_l y_lm=0}`.  Then `x` is a matching of all `M` into
`B=R-C_R`, with edges out of `S_M` restricted to `p_mr=1` and edges out of
`M-S_M` unrestricted.  The completion exists if and only if
`|B|=|M|` and this restricted graph has a perfect matching between both
shores `M` and `B`; merely saturating `M` is insufficient when `B` is larger.
This is an ordinary bipartite matching, again with an exact Hall separator.

Consequently a proof-safe exact solver may use the weighted common-basis
solution as its outer seed and alternate:

1. root-basis/low-receiver exchanges;
2. a low matching flow with mandatory receivers;
3. a rank-seven matching flow with short-edge restrictions; and
4. occurrence/state and supplier Hall cuts activated by the same selected
   parent edges.

Independent positive matchings at the four projections are not sufficient;
their edge identities must agree.

## 5. Literal K17 fixture

The protected private-H materialized table is a literal common-basis
witness.  Independent replay gives

```text
L/M/R targets             21777 / 19448 / 24310
common basis C_M/C_R      16915 / 4862
M7 basis B                19448
chain histogram           0 / 7395 / 16915
```

with all low and rank-seven matching edges strict and every target used
once.

```text
scratch/audit_k17_three_level_common_basis_equivalence_20260802.cpp
  60911fa22a41d33a8eda3975ab51e36e6fc071eb10fd692c38831763700f4bfe
scratch/k17_rank7_p2_hh_c6_audit_20260802/common_basis_fixture.audit.json
  cb2f3403d054a7110b58c41c5daa487836bcf10291d8dec54952a15c4d064cc4
```

On that protected completion, the separately audited state projection is

\[
 (P_0,Z_0,\Omega_0)=(16796,4708,3878),
\]

with all `1748` private H tickets retained.  These numbers are a warm
fixture, not consequences of the common-basis theorem.

## 6. Remaining exact gate

The static root/chain allocation is closed by two-matroid intersection.  The
remaining K17 selector must jointly choose:

* a common basis `C` and its two matching witnesses;
* one occurrence-labelled socket DNF for every resulting short chain;
* common endpoint flags and the residual long--long completion; and
* a selected-state supplier matching of rank `16898`.

The positive P2--H--H C6 columns are correlated warm/absorber columns in
this larger master.  The fixed-root SCC obstruction proves only that 162
current bad labels cannot themselves move on the frozen root bank.  It does
not prove that 162 root exchanges are needed, nor that every socket-complete
table must change the bank: an unchanged label can be repaired by changing
its lower-predecessor type, regenerating endpoint modes through other H
middles, changing owner/carrier incidence, or enlarging the state grammar.
The SCC result forces a bank change only for a move-each-defect architecture
(or after a separate socket-zero invariance lemma).  Chronology,
residence, upper shadows, common cap/compiler feasibility, and the word
remain separate.
