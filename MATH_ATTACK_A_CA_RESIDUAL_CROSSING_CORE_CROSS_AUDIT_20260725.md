# Cross-audit of the residual crossing core and its two companion A reports

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

Audited reports:

1. `MATH_ATTACK_A_CA_RESIDUAL_CROSSING_CORE_20260725.md`;
2. `MATH_ATTACK_A_CA_COMPLEMENT_STAR_FLOOR_COLLAR_20260725.md`;
3. `MATH_ATTACK_A_CA_PRIME_EQUIVARIANT_PACKET_COUPLING_20260725.md`.

## 0. Corrected verdict

The central theorem of the residual-crossing report is correct: for one
fixed exact factor, one fixed system of balanced quotas, and one common
exceptional owner set, the survival inequalities together with all directed
crossing-cover inequalities are **equivalent** to an integral residual
nested completion.  There is no missing compatibility condition between
the adjacent-rank matchings.

The two companion reports also pass audit.  Their conclusions have narrower
scope than a construction of the required common cyclic core:

* the complementary-star collar optimizes the two adjacent quota vectors
  separately for each cut, so it rules out only quota-independent
  fixed-order star obstructions;
* the prime-equivariant theorem rounds a residual flag flow once its
  pointwise box condition is supplied, but it does not select a
  near-complete invariant wreath core;
* the depth-one crossing phenomenon has linear **packet rank**.  It does
  not imply a linear lower bound for the cardinality or cost of a cover.

No theorem in the three reports proves the fixed-window alignment theorem
or the constant-one contiguous-OR bound.

## 1. Exact audit of the crossing-cover equivalence

Use the notation of the residual-crossing report.  Thus

\[
 f_q^E=\ell_q-a_q^E,
 \qquad
 r_q^E=b_q-\ell_q+a_q^E,
\]

and, for \(\mathcal A\subseteq V_q\),

\[
 \mathcal C_q(\mathcal A)
 =\{X:\Gamma_{q-1}(X)\in N_q(\mathcal A),
          \Gamma_q(X)\notin\mathcal A\},
\]

\[
 \kappa_q^b(\mathcal A)
 =b_{q-1}(N_q(\mathcal A))-b_q(\mathcal A).
\]

The two counting identities

\[
 |\mathcal C_q(\mathcal A)|
 =\ell_{q-1}(N_q(\mathcal A))-\ell_q(\mathcal A)
\]

and

\[
 |E\cap\mathcal C_q(\mathcal A)|
 =a_{q-1}^E(N_q(\mathcal A))-a_q^E(\mathcal A)
\]

have the asserted signs.  Direct subtraction therefore gives

\[
\boxed{
 r_q^E(\mathcal A)-r_{q-1}^E(N_q(\mathcal A))
 =|\mathcal C_q(\mathcal A)|
  -|E\cap\mathcal C_q(\mathcal A)|
  -\kappa_q^b(\mathcal A).}
\tag{1.1}
\]

The survival inequalities are exactly \(r_q^E(S)\ge0\).  Once they hold,
the residual masses at every two adjacent ranks are nonnegative integers
with the common total \(|E|\).  By (1.1), the crossing inequalities are
exactly

\[
 r_q^E(\mathcal A)
 \le r_{q-1}^E(N_q(\mathcal A))
 \qquad(\mathcal A\subseteq V_q),
\]

which are all child-side Hall inequalities in the cloned Boolean inclusion
graph.  Hall gives an integral matching between each adjacent pair of
ranks.  At an intermediate node the incoming and outgoing copy sets have
the same cardinality \(r_q^E(S)\), so an arbitrary bijection between those
two copy sets concatenates all adjacent matchings into \(|E|\) common
nested paths.  Thus separate applications of Hall do not create
incompatible path ownership.  Conversely, any common residual path system
implies node nonnegativity and every adjacent Hall inequality.  Theorem 2.1
is therefore an exact if-and-only-if statement.

### Packet and row projection

For \(0\le\kappa<|\mathcal C|\), requiring at most \(\kappa\) surviving
members of \(\mathcal C\) is equivalent to meeting every
\((\kappa+1)\)-subset of \(\mathcal C\).  If \(\kappa<0\), even deleting
all of \(\mathcal C\) cannot satisfy the inequality; if
\(\kappa\ge|\mathcal C|\), the condition is void.  Hence the packet form
has no endpoint error.

When exceptions are whole wreath rows, projecting an owner packet to the
set of rows containing its owners and deleting repetitions is lossless.  A
selected row set misses the projected packet if and only if its owner
closure misses the original packet.  Thus the weighted row inequality in
Section 3 is neither weaker nor stronger than the owner inequality under
the whole-row restriction.

## 2. Remaining theorems in the residual-crossing report

### Monotonicity

Adding one exceptional owner with parent \(R\) and child \(S\) changes a
cut defect by

\[
 \mathbf1_{\{S\in\mathcal A\}}
 -\mathbf1_{\{R\in N_q(\mathcal A)\}}\in\{0,-1\}.
\]

It also increases one residual node load by one.  Proposition 4.1 is
correct for fixed quotas.  It makes no assertion after the high-quota sets
are reselected.

If \(b\) is the load vector of one common nested flow, every unit entering
\(\mathcal A\) comes from \(N_q(\mathcal A)\), so

\[
 b_q(\mathcal A)\le b_{q-1}(N_q(\mathcal A)),
 \qquad \kappa_q^b(\mathcal A)\ge0.
\]

This use of common flow, rather than separate rankwise quotas, is essential.

### Minimal Hall cores

For the one-transition deficiency

\[
 D(\mathcal A)=v(\mathcal A)-u(N(\mathcal A)),
\]

exact subtraction at \(S\in\mathcal A\) gives

\[
 D(\mathcal A)-D(\mathcal A\setminus\{S\})
 =v(S)-p_{\mathcal A}(S).
\]

If \(\mathcal A\) is inclusion-minimal with deficiency \(d>0\), this
implies

\[
 p_{\mathcal A}(S)\le v(S)-d,
 \qquad
 1\le d\le\min_{S\in\mathcal A}v(S).
\]

The positive-parent intersection graph must be connected, or deficiency
would add over its components.  Summing the private-parent inequalities
and subtracting from \(u(N(\mathcal A))=v(\mathcal A)-d\) gives shared
parent mass at least \((|\mathcal A|-1)d\).  The peeling rule and the
supermodular inequality have the stated directions.  The theorem bounds
only deficiency.  It does not bound the cardinality, order, or number of
minimal cores, and its bounded-deficiency application presupposes the
survival inequalities so that the residual node loads are nonnegative.

### Linear packet rank

At depth one,

\[
 |\mathcal C_1(\{S\})|=m+2-\ell_1(S),
 \qquad
 \kappa_1^b(\{S\})=m+2-b_1(S).
\]

If \(b_1(S)-\ell_1(S)>0\), the active packet rank is exactly

\[
 m+3-b_1(S)\ge m+1
\]

for \(m\ge2\).  For \(1\le q\le m-1\), a fixed singleton crossing set
contains at most one owner from each oriented wreath row, so projection
preserves this rank.  More generally, in a fixed window an active singleton
packet has rank at least \(m+q-C_A+1\).

This is a statement about hyperedge rank.  The covering requirement for a
depth-one deficit \(d_S\) is only to choose at least \(d_S\) owners from
that large crossing set; here \(d_S\le2\).  No disjointness or low-overlap
theorem for the family of active packets is proved.  Therefore the report
does **not** prove an \(\Omega(m)\) exceptional-owner or exceptional-row
lower bound.

At depths \(q\ge2\), a positive target deficit alone need not activate the
singleton crossing packet.  With

\[
 g_q(S)=b_q(S)-\ell_q(S),
\]

the exact activity condition is

\[
 |\mathcal C_q(\{S\})|-\kappa_q^b(\{S\})
 =g_q(S)-g_{q-1}(N_q(S))>0.
\tag{2.1}
\]

The corollary in the report correctly says “if the packet is active”; (2.1)
should be recorded explicitly to prevent the stronger, false reading.

### Depth-one potential formula

The min-cost transportation formulation is correct.  Formally, after one
side of the bipartite constraint matrix is signed, it is a directed
node--arc incidence matrix and is totally unimodular; with integral right
hand side it is also TDI.  Hence both primal and dual integral optima exist.
The normalization \(\min z=0\), the formula for the optimal parent
potential, and the layer-cake passage to the nested level-set formula all
check.  “Feasible \(b_1\)” must mean feasible in the middle-to-facet
inclusion transportation graph, not merely a nonnegative vector of the
correct total mass.  The theorem is one-transition only.

## 3. Audit of the complementary-star floor collar

The balanced star interval in (1.4) is exact: it is precisely the possible
intersection range of the high-quota set with the star.  Expanding the two
endpoints gives the floor margins (1.6)--(1.7), including integral and
boundary cases.

For a fixed \(t\)-set \(T\), the row identity

\[
 C_q^F(T)=M_{q-1}^F(T)-M_q^F(T)
 =\sum_{R\in F}\mathbf1_{\{a_R(T)\ge q\}}\le B
\]

is correct.  Substitution in residual Hall gives the exact certificate

\[
 |E\cap\mathcal C_q^F(T)|
 \ge(C_q^F(T)-H_{q,t})_+,
\]

and weighted summation gives the packed-star dual with the displayed
congestion.

For fixed \(A,t\), the circle-distance estimate gives

\[
 \frac{H_{q,t}}B>\frac{4\eta_t}{\Lambda_A}q.
\]

The stated choice of \(Q_{A,t}\) therefore makes \(H_{q,t}\ge B\).  For
each fixed \(q\), the exact asymptotic is

\[
 \frac{H_{q,t}}B
 \longrightarrow
 2q(q-1)+\frac{2q+t}{2^{t-1}}.
\]

It is greater than one for every \(q\ge2\).  At \(q=1\) it is
\((t+2)/2^{t-1}\), so a separate-quota fixed-order obstruction can survive
only for \(q=1,t\ge4\).  The double-counting identities in Section 5 and
the Catalan congruence obstruction in Section 6 are also correct.

The essential limitation is unchanged: \(U_{q-1,t}\) and \(L_{q,t}\)
are separate extrema for one cut.  The theorem does not put all those
extrema into one common nested balanced quota flow, and it controls no star
whose order grows with \(m\).

## 4. Audit of the prime-equivariant companion

Theorem 2.1 is correct under its pointwise box hypothesis.  Every proper
subset and every deletion arc has a free orbit under the prime cycle.  The
uniform residual deletion flow descends to the quotient with integral
per-representative node bounds.  Network integrality gives integral quotient
paths, and a quotient path has a unique lift after its source representative
is fixed.  Taking all prime translates uses every residual middle root once
and preserves the frozen core exactly.

Taking the core \(G=\varnothing\) is legitimate: then

\[
 u_q^E(S)=\frac{\binom{m+q+1}{q}}{\binom mq}
 =\frac W{\binom n{m-q}}=\lambda_q\in[c_q,c_q+1].
\]

Thus the theorem supplies an unconditional prime-equivariant common
balanced flag flow in prime dimensions.  This application has no canonical
core and supplies no alignment with an exact wreath factor.

The classification of fixed rows as affine step orders gives exactly
\(m=(p-1)/2\) fixed underlying rows.  Also

\[
 \operatorname{Cat}_m\equiv2(-1)^m\pmod p.
\]

For odd \(m\), an invariant partial factor must leave at least \(m-1\)
rows, and an invariant full exact factor is impossible.  The corresponding
owner leave is \(p(m-1)\), which is polynomial and therefore
\(o(W/\sqrt m)\).  The obstruction rules out exact equivariance, not an
asymptotically adequate near-equivariant core.  It also shows why quotient
network integrality cannot be transferred to wreath-packet selection.

## 5. Formal corrections to the residual-crossing report

The following changes are required for a publication-level statement but
do not invalidate a theorem.

1. Define
   \[
   K=\lceil A\sqrt m\rceil\le m-1
   \]
   before its first use.
2. In Lemma 6.1, replace the trailing phrase “This holds for every
   \(q\ge1\)” by the stated admissible range \(1\le q\le m-1\).  The
   terminal empty-set case \(q=m\) is vacuous and may be handled
   separately.
3. Attach \(m\ge2\) to the assertion that balanced depth-one quotas are
   one or two and hence that the packet rank is at least \(m+1\).
4. Add the exact general-depth activity identity (2.1).
5. In Theorem 7.1, replace the informal phrase “the inclusion matrix is a
   network matrix” by the signed bipartite-incidence/TU statement above,
   and state graph-feasibility of \(b_1\).

## 6. Final proved boundary

The reports establish an exact integral residual criterion and identify
its two packet systems.  Bounded residual capacities imply bounded
deficiency of a minimal Hall core, but neither bounded core size nor a
small common cover.  Fixed-order stars are harmless outside one shallow
collar, while high-order singleton cuts already have linear packet rank.
Prime equivariance supplies a common balanced flag flow but cannot select
an invariant exact factor in the odd prime congruence class.

The quantitative unresolved assertion isolated by these reports is a
common-ownership cover theorem for all survival and directed crossing
packets.  Separate depthwise covers, separate quota extrema, and a
fractional or unextendible wreath packing do not satisfy it.  This is the
remaining gate within the audited residual-core route, not a claim that it
is logically weakest among every possible proof of constant one.
