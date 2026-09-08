# The \(s=1\) cyclic-cut capacitated tail master

Date: 2026-07-31  
Lane: D, exact \(K_{17}\) GK-tail completion

## 1. Frozen fixture

The shift-\(1\) base \(M_0\) is a matching:

\[
|M_0|=3640,\qquad |V(M_0)|=7280,\qquad c(M_0)=3640.
\]

Let \(B=V(M_0)\), and let \(U\) be the unused rank-seven owners. Then
\(|B|=7280\) and \(|U|=12168\). The peeled supported-provider projection has

\[
|L|=8736,\qquad |R|=13817,\qquad |I|=272992,
\]

and ordinary rank-six/rank-eight matching rank \(8736\).

For a Johnson edge \(e=xy\), write

\[
d(e)=x\cap y,\qquad q(e)=x\cup y.
\]

If \(D\subset Q\), \(|D|=6\), and \(|Q|=8\), then \((D,Q)\) determines its
physical edge uniquely: if \(Q\setminus D=\{a,b\}\), the endpoints are
\(D+a\) and \(D+b\).

## 2. Exact provider-capacity projection

For every supported incidence \(e=(D,Q)\), introduce \(p_e\in\{0,1\}\), and
put

\[
b(v)=
\begin{cases}
1,&v\in B,\\
2,&v\in U.
\end{cases}
\]

The exact first projection is

\[
\begin{aligned}
\sum_{e:d(e)=D}p_e&=1 &&(D\in L),\\
\sum_{e:q(e)=Q}p_e&\le 1 &&(Q\in R),\\
\sum_{e\ni v}p_e&\le b(v) &&(v\in B\cup U).
\end{aligned}
\tag{2.1}
\]

### Theorem 2.1

System (2.1) is feasible if and only if the supported core contains one
physical provider for every missing rank-six colour, with all selected
rank-eight unions distinct, base capacity one, and unused-owner capacity two.

The proof is literal incidence-vector replay. This is not an ordinary
Dulmage--Mendelsohn problem: each column uses resources \(D,Q,x,y\), so the
rank-six/rank-eight matching is only a projection.

The frozen ordinary matching is not a valid pin. It overloads \(1289\)
rank-seven vertices by \(1356\) total units:

\[
\begin{array}{c|cc}
&\text{overloaded vertices}&\text{excess}\\\hline
B&772&814\\
U&517&542.
\end{array}
\]

Separate necessary projections both pass: rank-six/rank-eight Hall is
\(8736/8736\), and the endpoint-capacity flow is \(17472/17472\). Only their
coupled integral correlation remained.

## 3. Forced EE rows and fixed-bank obstructions

Exactly \(572\) missing rank-six rows have no supported non-EE provider.
Therefore every completion uses at least \(572\) new EE edges. It may use
more; no equality is forced.

The \(572\)-row direct selector has \(3861\) columns, \(1001\) rank-eight
resources, and \(1573\) touched base vertices. Two distinct certificates are
frozen, with SHA-256 prefixes 7abcbd84 and 8afb0d8f. Each selects \(572\) EE
edges with distinct rank-eight labels, \(1144\) distinct base endpoints, and
\(1144\) distinct boundary rank-nine turns.

Both particular banks fail their residual raw b-factor model. With a bank
fixed, that model selects \(12698\) further edges, covers all \(8164\)
remaining rank-six colours, uses fresh rank-eight labels, uses \(6134\)
remaining base endpoints, and gives exactly \(9631\) unused owners degree
two. It has no topology or ear-shape cuts and no global rank-nine
all-different row. Presolve proves infeasibility in \(6.03\) seconds for
7abcbd84 and \(5.85\) seconds for 8afb0d8f.

These are bank-specific obstructions. They do not rule out every
\(x_{\rm EE}=572\) bank and do not prove \(x_{\rm EE}>572\). They prove that
direct selection and residual degree completion are integrally correlated.
As evidence about the unrestricted fibre they are only two failed seeds;
structural necessity of an additional EE edge would require either exhausting
all feasible 572-edge banks or proving a bank-independent valid cut.

## 4. One conditioned positive projection

Conditioned on 7abcbd84, the residual provider-capacity problem is SAT. An
exact certificate selects \(8164\) providers with

\[
b=3065\ \text{BU},\qquad 5099\ \text{UU},
\]

distinct rank-eight labels and all endpoint capacities respected. Its unused
degree histogram is \(0^{4416}1^{2241}2^{5511}\). The eventual repeat quotas
are

\[
\operatorname{repeat}_{BU}=6134-b=3069,\qquad
\operatorname{repeat}_{UU}=b-1600=1465.
\]

This is a capacity certificate only. The selected providers have \(17\)
illegal local wedges, \(1764\) rank-nine collision units, and four cycle
components. Moreover, the fixed-bank raw b-factor no-go above shows that no
choice of repeats can finish this particular direct bank under the exact
degree/q8/q6 ledger.

## 5. Unrestricted joint full-turn master

Let \(\mathcal E\) be the complete raw locally legal edge catalogue relative
only to \(M_0\). It has

\[
|\mathcal E|
=458934
=20655\ ({\rm EE})+147102\ ({\rm EU})+291177\ ({\rm UU}).
\]

Introduce \(x_e\in\{0,1\}\) for \(e\in\mathcal E\) and
\(y_u\in\{0,1\}\) for \(u\in U\). The joint system is

\[
\begin{aligned}
\sum_e x_e&=13270,\\
\sum_{e:q(e)=Q}x_e&\le1 &&(Q\text{ fresh rank eight}),\\
\sum_{e:d(e)=D}x_e&\ge1 &&(D\text{ missing rank six}),\\
\deg_x(b)&\le1 &&(b\in B),\\
\sum_{b\in B}\deg_x(b)&=7278,\\
\deg_x(u)&=2y_u &&(u\in U),\\
\sum_{u\in U}y_u&=9631.
\end{aligned}
\tag{5.1}
\]

Rows (5.1) force the \(572\) exceptional EE services but allow arbitrary
additional EE edges.

For each selected unused centre, ten outside-coordinate bits are linked to
its two incident edges. Booleanity forces the two additions to be distinct,
and their union determines its literal rank-nine central turn. At a base
vertex, its fixed mate and selected edge determine the boundary turn.
Unselected vertices receive private dummy labels. A single all-different row
is therefore exactly global injectivity of the

\[
9631+7278=16909
\]

physical rank-nine turns.

### Theorem 5.1 (round-zero equivalence)

System (5.1) plus the turn equations and all-different row is feasible if and
only if the raw \(s=1\) catalogue contains \(13270\) new edges which

- cover all \(8736\) missing rank-six colours;
- use distinct fresh rank-eight unions;
- leave exactly two base terminals;
- use exactly \(9631\) unused owners, all at degree two; and
- use \(16909\) distinct physical rank-nine turns.

No direct bank, EE count, ear schedule, or topology is fixed. The proof is
literal reconstruction in both directions.

## 6. Topology is a post-SAT graphic CEGAR

After adjoining the \(3640\) fixed base edges, any round-zero solution has

\[
V=7280+9631=16911,\qquad E=3640+13270=16910.
\]

Every selected vertex has degree two except two base vertices of degree one.
Thus the graph is one path plus zero or more cycles. It is a Hamilton path
exactly when it is acyclic. Each detected cycle component yields the valid
lazy row

\[
|M_0[S]|+\sum_{e\in\mathcal E[S]}x_e\le |S|-1.
\tag{6.1}
\]

No topology row is needed before the first SAT candidate.

## 7. Equivalent decomposed port ledger

Suppose instead that the \(8164\) unique providers and a direct bank form a
clean forest. Let \(b\) be the number of BU providers and \(s\) the number of
used unused owners. Add \(z=9631-s\) zero-degree unused owners as singleton
nodes. The provider forest has \(s-5096\) components, hence the contracted
graph always has

\[
(s-5096)+(9631-s)=4535
\]

nodes. Exactly \(4534\) repeat edges must form a spanning path, with quotas

\[
\operatorname{repeat}_{BU}=6134-b,\qquad
\operatorname{repeat}_{UU}=b-1600.
\]

For the conditioned capacity hint \(b=3065,s=7752\), one has \(z=1879\),
repeat quotas \(3069/1465\), and \(5312\) old forest endpoints; a spanning
path uses \(5310\) and leaves two terminals.

## 8. Rank-five compiler after the conditioned topology

In the \(b=3065,s=7752\) profile, the \(1879\) activated singleton owners
each receive two repeats and become Boolean-diamond centres. They consume
\(3758\) repeat edges and each expose a 20-element ordered deletion-pair
domain. The remaining

\[
4534-3758=776
\]

repeat edges are singleton connector cells, each with at least four allowed
deletions. Thus the final rank-five compiler is a grouped SDR on \(1879\)
pair domains plus \(776\) singleton domains, covering \(4534\) distinct
rank-five targets. This is conditional on obtaining that topology and
profile; it is not a generic common-cap assertion.

## 9. Reproducibility and current status

- Provider rows:
  scratch/k17_gk_cyclic_cut_s1_supported_provider_matching_20260731.tsv,
  SHA-256
  6b2d9802d028cca79064278a65020d8ec28e3cc1b04d59c518d29b66b1a68e97.
- Capacity model/replayer:
  scratch/threadD_k17_s1_rank6_rank8_vertex_capacity_20260731.py.
- First direct bank:
  scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv, SHA-256
  7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d.
- Second direct bank:
  scratch/k17_gk_shift1_forced_direct_matching_20260731.tsv, SHA-256
  8afb0d8f6e754ab31aa6d2f8f2dbe161cdcddce8c81883239195000d9f4afb71.
- Conditioned residual capacity certificate:
  scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv, SHA-256
  7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff.
- Unrestricted joint source:
  scratch/threadD_k17_s1_joint_fullturn_master_20260731.py.

The two named direct banks are raw-residual UNSAT only in their precise
fixed-bank scopes. The unrestricted joint round-zero model is the live exact
gate. A timed or resource-limited run is UNKNOWN unless it emits either a
replayed solution or a completed exact infeasibility result.
