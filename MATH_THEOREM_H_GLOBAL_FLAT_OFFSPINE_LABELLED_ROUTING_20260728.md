# Global flat off-spine labelled routing for the \(k\mapsto k+2\) diamond lift

Date: 2026-07-28

## 0. Outcome

This note gives the strongest positive exact formulation currently available
for the same-parity lift. It does not prove an all-\(k\) induction.

The main advances are:

1. the four-sector child deck has an exact finite owner graph; degree and
   cut equations characterize one literal Hamilton chronology;
2. the entire immediate-lower seam ledger has four exact signed identities;
3. the \(A\)-sector is a colored flag linear forest with a constructive
   capacitated endpoint Hall theorem;
4. the \(U\)-sector is exactly a ternary rank-star routing: every old
   rank-\(r\) label is assigned to a \(UU\) pair, a \(U\)-port singleton,
   or a vertical \(XY\) edge;
5. direct shared endpoints have an exact pseudoforest/SDR criterion;
6. a maximal-envelope theorem characterizes feasible global flat data
   \((T,\phi)\) exactly, while a core-preserving form gives a constructive
   common multirow compiler retaining residence and all installed pins;
7. combining these objects gives an exact finite characterization of the
   Johnson-flat off-spine routing lane.

The frozen exact \(k=11\) and \(k=13\) certificates pass this formulation.
Relative to coordinates \(12,13\), the exact \(k=13\) chronology contains
an exact \(132\)-component Catalan \(A\)-forest and an exact ternary
\(U\)-routing. Of its \(330\) \(AA\) edges, \(307\) are off the frozen
\(k=11\) native \(C\)-spine; \(198\) of its \(222\) \(UU\) edges and
\(144\) of its \(216\) \(U\)-ports are likewise nonnative.

Thus global off-spine routing is not merely a relaxation: it is the
mechanism used by the known exact child. The remaining open lemma is to
construct this object uniformly from parent data.

## 1. The exact four-sector owner graph

Let the old ground set be \(K=[2r-1]\), and adjoin \(x,y\). Put

\[
 W=\binom{2r-1}{r},\qquad
 b=W-\binom{2r-1}{r+1}
   =\frac{2W}{r+1}=C_r.
\tag{1.1}
\]

The child middle rank is \(r+1\). Its owners are

\[
\begin{aligned}
 A_C&=C\cup\{x,y\},&&C\in\binom K{r-1},\\
 X_T&=T\cup\{x\},&&T\in\binom K r,\\
 Y_T&=T\cup\{y\},&&T\in\binom K r,\\
 U_V&=V,&&V\in\binom K{r+1}.
\end{aligned}
\tag{1.2}
\]

Their counts are \(W,W,W,W-b\), so the child width is \(4W-b\).

### Lemma 1.1 (complete allowed-edge list)

The Johnson edges between child owners are exactly:

1. \(A_CA_{C'}\) when \(C,C'\) are Johnson adjacent;
2. \(U_VU_{V'}\) when \(V,V'\) are Johnson adjacent;
3. \(A_CX_T\) and \(A_CY_T\) when \(C\subset T\);
4. \(U_VX_T\) and \(U_VY_T\) when \(T\subset V\);
5. \(X_TX_{T'}\) and \(Y_TY_{T'}\) when \(T,T'\) are Johnson adjacent;
6. the vertical edge \(X_TY_T\).

There is no \(A\)-\(U\) edge and no \(X_TY_{T'}\) edge for \(T\ne T'\).

#### Proof

Every child owner has rank \(r+1\), so two are Johnson adjacent exactly
when their intersection has rank \(r\). Checking their new-coordinate
signatures gives the six displayed cases. For example,

\[
 A_C\cap X_T=C\cup\{x\}
\]

has rank \(r\) exactly when \(C\subset T\), while
\(X_T\cap Y_{T'}=T\cap T'\) has rank \(r\) exactly when \(T=T'\).
An \(A\)-state and a \(U\)-state differ on both new coordinates and have
intersection rank at most \(r-1\). \(\square\)

Let \(G_r\) be this finite owner graph.

### Theorem 1.2 (exact Hamilton routing system)

Put a binary variable \(z_e\) on every \(e\in E(G_r)\), and a binary
endpoint variable \(\varepsilon_v\) on every owner. The selected edges form
one Hamilton path through the entire child middle layer if and only if

\[
 \sum_{e\ni v}z_e=2-\varepsilon_v
 \qquad(v\in V(G_r)),
\tag{1.3}
\]

\[
 \sum_v\varepsilon_v=2,
\tag{1.4}
\]

and

\[
 \sum_{e\in\delta(S)}z_e\ge1
\quad
(\varnothing\ne S\subsetneq V(G_r)).
\tag{1.5}
\]

#### Proof

A Hamilton path satisfies all equations. Conversely, (1.3)--(1.4) give
total degree \(2|V|-2\), hence exactly \(|V|-1\) selected edges. The cut
conditions make the selected graph connected. It is therefore a tree, and
its maximum degree is two, so it is one spanning path. \(\square\)

The induced graph in each of the four sectors is automatically a linear
forest. Thus (1.3)--(1.5) are also an exact shared-endpoint fusion system:
sector path components may be built separately and joined at their literal
owner endpoints without duplicate ownership.

## 2. Exact component and immediate-shadow ledgers

Let a Hamilton path be fixed. Write

\[
 a,c_X,c_Y,u
\]

for the numbers of induced components in the \(A,X,Y,U\) sectors. Let
\(\eta_A,\eta_X,\eta_Y,\eta_U\) count its two global endpoints by sector.
Write

\[
 e_{AX},e_{AY},e_{UX},e_{UY},e_{XY}
\]

for the undirected cross-edge counts, with \(e_{XY}\) counting vertical
edges.

### Lemma 2.1 (component endpoint equations)

\[
\begin{aligned}
E_{AA}&=W-a,&
e_{AX}+e_{AY}&=2a-\eta_A,\\
E_{XX}&=W-c_X,&
e_{AX}+e_{UX}+e_{XY}&=2c_X-\eta_X,\\
E_{YY}&=W-c_Y,&
e_{AY}+e_{UY}+e_{XY}&=2c_Y-\eta_Y,\\
E_{UU}&=W-b-u,&
e_{UX}+e_{UY}&=2u-\eta_U.
\end{aligned}
\tag{2.1}
\]

#### Proof

A linear forest on \(n\) vertices with \(c\) components has \(n-c\)
internal edges. Its \(2c\) component endpoints are used by cross edges,
except for each global endpoint lying in that sector. \(\square\)

For any target family, let \(h\) be its number of holes and let

\[
 \rho=\sum_Z(\ell_Z-1)^+
\]

be its repeat excess. Then

\[
 \rho-h=(\text{number of occurrences})-(\text{number of targets}).
\tag{2.2}
\]

### Theorem 2.2 (four signed immediate-lower identities)

Let the subscripts \(xy,x,y,0\) denote the four new-coordinate signatures
of immediate-lower targets. Then

\[
\boxed{\rho_{xy}-h_{xy}=b-a,}
\tag{2.3}
\]

\[
\boxed{\rho_x-h_x=e_{AX}-c_X,}
\tag{2.4}
\]

\[
\boxed{\rho_y-h_y=e_{AY}-c_Y,}
\tag{2.5}
\]

\[
\boxed{\rho_0-h_0=u+e_{XY}-\eta_U-b.}
\tag{2.6}
\]

#### Proof

Both-new lower labels arise only on \(AA\) edges. There are \(W-a\)
occurrences and \(W-b\) targets, giving (2.3).

An \(x\)-only lower label arises on an \(XX\) edge or an \(A\)-\(X\)
edge. Its occurrence count is \(W-c_X+e_{AX}\), while its target count is
\(W\). This proves (2.4), and (2.5) is symmetric.

An old-only lower label arises on a \(UU\) edge, a \(U\)-cross edge, or a
vertical \(X_TY_T\) edge. By (2.1), its occurrence count is

\[
 (W-b-u)+(2u-\eta_U)+e_{XY}.
\]

Subtracting the \(W\) targets gives (2.6). \(\square\)

In particular, collision-free complete routing forces

\[
 a=b,\qquad
 e_{AX}=c_X,\qquad
 e_{AY}=c_Y,\qquad
 u+e_{XY}-\eta_U=b.
\tag{2.7}
\]

These are exact seam balances, not estimates.

## 3. The \(A\)-sector: colored flags and port completion

Every \(AA\) edge has a unique lower colour

\[
 R=C\cap C'\in\binom K{r-2}
\]

and a unique upper top

\[
 T=C\cup C'\in\binom K r.
\]

Equivalently, it is specified by a flag

\[
 R\subset T,\qquad |T\setminus R|=2,
\tag{3.1}
\]

whose two intermediate rank-\((r-1)\) sets are the edge endpoints.

### Theorem 3.1 (Catalan flag-forest equivalence)

Choose one top \(f(R)\supset R\) for every
\(R\in\binom K{r-2}\), and let \(F_A\) be the resulting \(AA\) edge set.
Then:

1. every both-new immediate-lower colour occurs exactly once;
2. \(F_A\) is a spanning linear forest if and only if

   \[
   \deg_{F_A}(C)\le2
   \quad\text{for every }C\in\binom K{r-1},
   \tag{3.2}
   \]

   and \(F_A\) is acyclic;
3. whenever (3.2) holds and \(F_A\) is acyclic, it has exactly

   \[
   W-(W-b)=b
   \tag{3.3}
   \]

   path components, and the endpoint multiplicity

   \[
   \rho_A(C)=2-\deg_{F_A}(C)
   \tag{3.4}
   \]

   satisfies \(\sum_C\rho_A(C)=2b\).

#### Proof

The selected edge for \(R\) has lower colour \(R\), proving the first
claim. A graph is a linear forest exactly when it is acyclic and has
maximum degree two. There are

\[
 \binom{2r-1}{r-2}=W-b
\]

selected edges on \(W\) vertices, so a forest has \(b\) components. The
endpoint identity is the degree sum. \(\square\)

This formulation is completely off-spine. The inherited occurrence
selector is only the restriction that \(f(R)\) be the top of one of the
native occurrences of colour \(R\).

### Theorem 3.2 (capacitated \(A\)-port completion)

Assume \(F_A\) is a Catalan linear forest and no global endpoint lies in
the \(A\)-sector. Let \(P_A\) be its multiset of \(2b\) endpoint
occurrences, where an occurrence \(p\) has core \(C(p)\).

Let \(Z_0\subseteq\binom K r\) be the tops already covered by selected
vertical edges \(X_TY_T\). Let

\[
 M_A=
 \left\{
 T\in\binom K r:
 T\notin Z_0,\ 
 T\ne f(R)\text{ for every }R
 \right\}
\tag{3.5}
\]

be the residual both-new immediate-upper holes.

There is an assignment of every endpoint \(p\in P_A\) to a top
\(g(p)\supset C(p)\), with top capacity at most two, which covers every
top in \(M_A\), if and only if

\[
 |Z|
 \le
 \sum_{\substack{C:\ C\subset T\\\text{for some }T\in Z}}
 \rho_A(C)
 \qquad(Z\subseteq M_A).
\tag{3.6}
\]

Moreover the assignments can be two-coloured \(X,Y\) so that the two ends
of every \(A\)-component receive different shores and each physical
\(X_T,Y_T\) is used at most once.

#### Proof

Consider the bipartite graph from the endpoint occurrences \(P_A\) to the
rank-\(r\) tops, with \(p\sim T\) when \(C(p)\subset T\). Give each top
upper capacity two and each member of \(M_A\) lower quota one.

For a general bipartite graph with unit left demands, right capacity two,
and lower quota one on \(M\), an integral assignment exists exactly when

\[
 |Q|\le2|N(Q)|\quad(Q\subseteq P)
\tag{U}
\]

and

\[
 |Z|\le|N(Z)|\quad(Z\subseteq M).
\tag{L}
\]

This follows from the integral circulation with arcs

\[
 s\to p:[1,1],\qquad
 p\to T:[0,1],\qquad
 T\to t:[\mathbf1_M(T),2],
 \qquad t\to s:[|P|,|P|].
\]

The Hoffman cuts reduce to (U) and (L).

For completeness, the mixed cuts introduce nothing further. In an upper
cut with endpoint subset \(Q\) and top subset \(Z\), put

\[
 Q_0=\{p\in Q:N(p)\subseteq Z\}.
\]

Every \(p\in Q\setminus Q_0\) contributes an edge leaving \(Z\), while
(U) applied to \(Q_0\) gives \(|Q_0|\le2|N(Q_0)|\le2|Z|\). In a lower
cut, the right side has the form

\[
 |P_A\setminus Q|+e(Q,Z)
 \ge |N(Z)\setminus Q|+|N(Z)\cap Q|
 =|N(Z)|,
\]

so (L) implies that cut as well.

Here (L) is exactly (3.6). Condition (U) is automatic. Indeed, the
rank-\((r-1)\)/rank-\(r\) inclusion graph on \(K\) is \(r\)-regular with
equal shores, so every set of distinct endpoint cores has at least as many
top neighbours; each core occurs at most twice by (3.4).

Contract each \(A\)-component and join it to the assigned tops of its two
ends. The resulting bipartite multigraph has degree two on every component
and degree at most two on every top. Each path or even cycle has a proper
two-edge-colouring. Use the two colours as the \(X,Y\) shores. \(\square\)

Thus vertical \(XY\) choices in the \(U\)-routing and missing-top repair in
the \(A\)-routing are coupled through the set \(Z_0\).

The scope is exact but deliberately restricted: this is the
**fresh-owner** \(A\)-port architecture, in which no physical \(X_T\) or
\(Y_T\) is incident with two \(A\)-components. An unrestricted Hamilton
path may instead contain a passage \(A-X_T-A\) or \(A-Y_T-A\). Therefore
failure of (3.6) is not an unrestricted no-go; the full owner equations
(1.3)--(1.5) retain those shared-owner possibilities.
Even when (3.6) holds, installation into a preselected \(X/Y/U\) routing
still requires residual owner-degree compatibility and the global cut
conditions. Theorem 3.2 supplies the fresh port layer, not the whole path.

### Corollary 3.3 (native cut-port injection)

Suppose a completed native \(C\)-path has distinct edge tops and omits one
top \(T_*\) containing a boundary endpoint core. Then every native
exact-colour subforest passes (3.6).

#### Proof

Its missing tops are the tops of the \(b-1\) cut native edges together
with \(T_*\). Assign every cut-edge top to one of the two port occurrences
created by that cut, and assign \(T_*\) to the unused boundary port. These
are distinct endpoint occurrences and give an explicit injection from every
missing-top subfamily into its neighbour ports. \(\square\)

Within the fresh-owner architecture, this closes \(AA\) lower colours,
both-new immediate-upper holes, and exact \(X/Y\) port ownership for the
native adaptive \(A\)-half. It does not settle residence or its alignment
with the \(U\)-half.

### Proposition 3.4 (the first frozen hazard is exchangeable)

At the audited \(k=11\) root, the first selector uses edge \(253\) for

\[
 R=\{3,5,8,9\}.
\]

Replace it by the other native occurrence, edge \(286\). This preserves:

1. one edge of every colour;
2. degree at most two and acyclicity;
3. \(132\) components;
4. distinct selected edge tops.

It removes the coordinate-\(1\) internal pattern \(0\,1^3\,0\) at
\(253,\ldots,257\) and creates no new internal short run in the changed
components.

#### Proof

Before the exchange, the affected components are

\[
 [252,257],\qquad[285,286],\qquad[287,288].
\]

Deleting edge \(253\) and adding edge \(286\) changes them to

\[
 [252,253],\qquad[254,257],\qquad[285,288].
\]

The removed and added edges have the same lower colour. Both are native
path edges, so no degree or cycle defect arises. Their tops are distinct
in the completed native path. Direct coordinate inspection shows that the
old bad run becomes the component prefix \(1,1,1,0\), while every
coordinate on the joined component is a prefix, suffix, all-one, or
all-zero pattern. \(\square\)

The frozen audit in Section 10 verifies these component changes and the
global short-internal-run count \(45\to44\). Thus the first-occurrence
no-go is not invariant even inside the native path. A simultaneous choice
eliminating every hazard and meeting the \(U\)/compiler constraints remains
open.

## 4. The \(U\)-sector: ternary rank-star routing

For \(T\in\binom K r\), define its cofacet star

\[
 \Gamma(T)=\{V\in\binom K{r+1}:T\subset V\}.
\tag{4.1}
\]

### Theorem 4.1 (ternary star-routing equivalence)

A collision-free complete routing of all old-only immediate-lower labels is
equivalent to choosing, for every \(T\in\binom K r\),

\[
 \pi_T\subseteq\Gamma(T),\qquad |\pi_T|\in\{0,1,2\},
\tag{4.2}
\]

with the following meanings:

* \(|\pi_T|=2\): join its two \(U\)-owners by the \(UU\) edge labelled
  \(T\);
* \(|\pi_T|=1\): use that \(U\)-owner at a cross-shore endpoint port
  labelled \(T\);
* \(|\pi_T|=0\): use the vertical edge \(X_TY_T\).

The size-two choices must form a spanning linear forest \(F_U\), and every
\(U_V\) must satisfy

\[
 \deg_{F_U}(V)
 +\#\{T:\pi_T=\{V\}\}
 =2-\varepsilon_V,
\tag{4.3}
\]

where \(\varepsilon_V\) records a global endpoint in the \(U\)-sector.

#### Proof

The three displayed edge types are exactly the three possible sources of
the old-only lower label \(T\), by Lemma 1.1. Collision-free completeness
selects exactly one source, giving (4.2). The pair choices are precisely
the internal \(UU\) edges. A \(U\)-owner has its remaining degree supplied
by singleton cross ports, giving (4.3). Conversely, (4.2)--(4.3) literally
construct all \(U\)-components, their ports, and one occurrence of every
old-only lower label. \(\square\)

This equivalence is the exact \(U\)-sector occurrence/degree ledger.
Choosing the singleton shores and installing them together with the
\(A,X,Y\) sectors still requires owner-degree compatibility and the global
Hamilton cuts.

If \(u\) is the number of \(U\)-components and \(e\) is the number of zero
choices, then

\[
\begin{aligned}
\#\text{pairs}&=W-b-u,\\
\#\text{singletons}&=2u-\eta_U,\\
\#\text{zeros}&=e,
\end{aligned}
\]

and partitioning all \(W\) labels is equivalent to

\[
 u+e-\eta_U=b,
\tag{4.4}
\]

the collision-free case of (2.6).

### Corollary 4.2 (old-only \((US^*)\))

The empty-signature upper condition holds exactly when, for every
\(Z\subseteq K\) with \(|Z|>r+1\), some contiguous subpath

\[
 V_s,V_{s+1},\ldots,V_t
\]

of one component of \(F_U\) satisfies

\[
 Z=V_s\cup V_{s+1}\cup\cdots\cup V_t.
\tag{4.5}
\]

#### Proof

An upper interval avoiding both new coordinates can contain only
\(U\)-states. Its consecutive middle states therefore lie in one
\(U\)-component, and the converse is literal. \(\square\)

This is the positive global replacement for first/last occurrence
selectors.

## 5. Direct shared ports and the pseudoforest criterion

Suppose an \(A\)-component endpoint \(C\) is paired directly with a
\(U\)-component endpoint \(V\), where

\[
 C\subset V,\qquad |C|=r-1,\quad |V|=r+1.
\]

There are exactly two intermediate rank-\(r\) sets between them:

\[
 \mathcal T(C,V)=\{T:C\subset T\subset V\}.
\tag{5.1}
\]

Either intermediate gives a direct passage

\[
 A_C-X_T-U_V
\quad\text{or}\quad
 A_C-Y_T-U_V.
\]

Let \(M\) be a family of paired endpoint flags \((C,V)\). Form a multigraph
\(\mathcal G_M\) whose vertices are the rank-\(r\) intermediates and whose
edge for \((C,V)\) joins the two members of \(\mathcal T(C,V)\).

### Theorem 5.1 (shared-port SDR)

1. If every flag must use one fixed shore, distinct physical ports can be
   chosen for all flags if and only if \(\mathcal G_M\) is a pseudoforest:
   every component has at most one cycle.
2. If either shore may be used, distinct physical ports can be chosen if
   and only if

   \[
   |F|\le2|V(F)|
   \qquad(F\subseteq E(\mathcal G_M)),
   \tag{5.2}
   \]

   where \(V(F)\) is the set of intermediate vertices incident with \(F\).

#### Proof

With one shore, the candidate ports of a flag are the two endpoints of its
edge in \(\mathcal G_M\). Hall's theorem says that every edge subfamily
must touch at least as many vertices as edges. This is equivalent to every
component having edge count at most vertex count, namely the pseudoforest
condition.

With two shores, every intermediate vertex supplies two physical ports.
The candidate union of a flag subfamily has size \(2|V(F)|\), so Hall is
exactly (5.2). \(\square\)

After the port SDR, one must still require the component-contraction graph
to be a path. This is enforced exactly by (1.3)--(1.5).

## 6. Exact finite upper-window constraints

For an upper target \(Z\), let \(\mathcal J_Z\) be the finite family of
simple paths in \(G_r\) whose vertex union is exactly \(Z\). Introduce
binary witness variables \(w_{Z,J}\). The constraints

\[
 w_{Z,J}\le z_e\qquad(e\in E(J))
\tag{6.1}
\]

and

\[
 \sum_{J\in\mathcal J_Z}w_{Z,J}\ge1
\tag{6.2}
\]

are necessary and sufficient for \(Z\) to occur as a consecutive union in
the Hamilton path selected by \(z\).

#### Proof

Every interval of the selected Hamilton path is a simple selected subpath.
Conversely, if all edges of \(J\) are selected, its internal vertices
already have their two Hamilton edges inside \(J\), so \(J\) is a literal
consecutive subpath. \(\square\)

For empty-signature targets, (6.1)--(6.2) reduce to (4.5). For a
single-\(x\) target, every witness lies in the induced \(X\cup U\) graph;
the \(y\)-case is symmetric. This gives an exact finite all-signature form
of \(F4\).

## 7. Exact global flat data and the core-preserving compiler

Now let \(n=k+2\), let \(R\) be the child middle rank, and put

\[
 N=\binom nR,\qquad L=N+d.
\]

Orient a Hamilton path

\[
 T=(T_0,\ldots,T_{N-1}),
\]

put \(J_i=[i,i+d]\), and define the maximal central envelope

\[
 E_p(T)=\bigcap_{i:p\in J_i}T_i.
\tag{7.1}
\]

Let

\[
 \phi:\{S\subseteq[n]:1\le|S|<R\}
 \hookrightarrow
 \{(s,j):0\le s<d,\ 0\le j<L-s\}
\tag{7.2}
\]

be injective. Write \(\phi(S)=(s_S,j_S)\) and
\(I_S=[j_S,j_S+s_S]\). Define the maximal post-pin envelopes

\[
 P_p=
 E_p(T)\cap
 \bigcap_{S:p\in I_S}S.
\tag{7.3}
\]

### Theorem 7.1 (exact feasible-flat-data criterion)

The pair \((T,\phi)\) is realized by a nonzero word \(A\), meaning

\[
 D^dA=T,\qquad
 \bigcup_{p\in I_S}A_p=S
 \quad\text{for every lower }S,
\tag{7.4}
\]

if and only if its maximal envelopes satisfy

\[
 \boxed{P_p\ne\varnothing\quad(0\le p<L),}
\tag{F1}
\]

\[
 \boxed{\bigcup_{p\in J_i}P_p=T_i\quad(0\le i<N),}
\tag{F2}
\]

and

\[
 \boxed{\bigcup_{p\in I_S}P_p=S
 \quad\text{for every lower }S.}
\tag{F3}
\]

When these conditions hold, \(A=P\) works and is the unique
coordinatewise maximal realizing word.

#### Proof

If \(A\) realizes \((T,\phi)\), then \(A_p\subseteq T_i\) whenever
\(p\in J_i\), and \(A_p\subseteq S\) whenever \(p\in I_S\). Hence
\(A_p\subseteq P_p\), so (F1) follows. On every central interval and every
pin interval, respectively,

\[
 T_i=\bigcup_{p\in J_i}A_p
 \subseteq\bigcup_{p\in J_i}P_p\subseteq T_i,
 \qquad
 S=\bigcup_{p\in I_S}A_p
 \subseteq\bigcup_{p\in I_S}P_p\subseteq S.
\]

Thus (F2)--(F3) hold. Conversely, (F1)--(F3) say literally that \(P\)
is a nonzero realizing word. Every realizing word lies coordinatewise below
\(P\), proving maximality. \(\square\)

This is the exact characterization of global flat data \((T,\phi)\). It is
a simultaneous coordinate condition, not a marginal matching condition.

For constructive extension, choose a nonzero core word

\[
 C=(C_0,\ldots,C_{L-1})
\]

such that

\[
 C_p\subseteq E_p(T),\qquad
 \bigcup_{p\in J_i}C_p=T_i.
\tag{7.5}
\]

Equivalently, \(D^dC=T\).

### Theorem 7.2 (exact core-preserving pin extension)

There exists a word \(A\) satisfying

\[
 C\subseteq A,\qquad
 D^dA=T,\qquad
 \bigcup_{p\in I_S}A_p=S
 \quad\text{for every lower }S
\tag{7.6}
\]

if and only if

\[
 \boxed{C_p\subseteq S\quad(p\in I_S)}
\tag{N}
\]

for every pin and

\[
 \boxed{S\subseteq\bigcup_{p\in I_S}P_p}
\tag{P}
\]

for every lower target. When these conditions hold, \(A=P\) works.

#### Proof

Suppose \(A\) exists. On a pin interval \(I_S\), every \(A_p\subseteq S\);
since \(C\subseteq A\), condition (N) follows. Central equality and all
pin equalities imply \(A_p\subseteq E_p(T)\) and
\(A_p\subseteq S\) whenever \(p\in I_S\). Hence \(A_p\subseteq P_p\),
and taking unions on \(I_S\) gives (P).

Conversely, (N) implies \(C_p\subseteq P_p\), so every \(P_p\ne\varnothing\).
For every central interval,

\[
 T_i=\bigcup_{p\in J_i}C_p
 \subseteq\bigcup_{p\in J_i}P_p
 \subseteq T_i.
\]

For every lower pin, \(P_p\subseteq S\) on \(I_S\), while (P) gives the
reverse inclusion after union. Thus \(A=P\) satisfies (7.6). \(\square\)

Condition (P) has the coordinate-routing form

\[
\forall S,\ \forall q\in S,\ \exists p\in I_S:
\quad q\in E_p(T)
\quad\text{and}\quad
q\in S'\text{ for every pin }I_{S'}\ni p.
\tag{7.7}
\]

This is the exact common multirow PCSH condition. It is not a family of
independent target-to-cell Hall tests.

### Corollary 7.3 (batch extension)

Suppose a partial pin family already satisfies Theorem 7.2. Add a batch of
new pins and intersect their labels into the affected envelopes. The batch
is feasible exactly when:

1. no new negative pin kills the core;
2. every new interval still unions to its new label;
3. every old interval still unions to its old label.

If the final batch passes, every ordering of that batch passes.

#### Proof

These are conditions (N) and (P) after the batch. Intermediate envelopes
are supersets of the final envelopes. \(\square\)

The core protects central ownership, nonzero entries, and the residence
certificate encoded by \(D^dC=T\), while the maximal-envelope test protects
all lower rows simultaneously.

## 8. Master equivalence for the Johnson-flat lane

Here \(d=B(n)-N\), so the flat target length is \(L=N+d=B(n)\).

### Theorem 8.1 (global off-spine flat routing)

There is a universal word of length \(B(n)\) whose \(d\)-th row is a
Johnson Hamilton path if and only if there exist:

1. an edge selection \(z\) and endpoints \(\varepsilon\) satisfying
   (1.3)--(1.5);
2. upper witness variables satisfying (6.1)--(6.2) for every target of
   rank greater than \(R\);
3. an orientation \(T\) of the selected path and one injective all-lower
   pin map \(\phi\) whose maximal envelopes satisfy (F1)--(F3).

Equivalently, item 3 may be certified constructively by a nonzero core
\(C\) satisfying (7.5), together with (N) and (P) of Theorem 7.2.

When these data exist, the maximal post-pin word \(P\) in (7.3) is
universal.

#### Proof

The Hamilton system gives one owner-exact middle path. The upper witnesses
give \(F4\). Theorem 7.1 says that \(P\) is nonzero, has middle row \(T\),
and realizes every lower target. Hence \(P\) is universal.

Conversely, an optimal flat word with Johnson middle row supplies its
Hamilton edges and upper intervals. A target of rank below \(R\) cannot
occur at row \(d\) or above, because every such cell contains a rank-\(R\)
middle state. Select one of its row-\(<d\) witness cells; distinct target
values give distinct cells, hence an injective \(\phi\). Theorem 7.1 gives
(F1)--(F3). Taking \(C=A\) also gives the equivalent core certificate.
\(\square\)

The \(A\)-flag forest, \(U\)-ternary routing, and flag-port SDR are
constructive sufficient substructures inside this exact equivalence. They
are not imposed by every flat word.

## 9. Exact depth-three off-spine rescue dichotomy

### Proposition 9.1

Let \(A\) be a nonzero universal flat word with

\[
 D^3A=(T_0,\ldots,T_{N-1}),
\]

where \(T\) is a rank-\(R\) Johnson Hamilton path. Let \(H\) have rank
\(R-2\), with \(H\not\subseteq T_0,T_{N-1}\). Then every occurrence of
\(H\) forces at least one of:

1. three internal consecutive middle states whose intersection contains
   \(H\);
2. an internal rank-\((R-1)\) edge colour \(Q\supset H\) occurring on at
   least two distinct middle edges.

#### Proof

A row-zero witness is contained in at least four consecutive middle
windows, and a row-one witness in at least three, unless it is supported at
a global boundary. Boundary support would put \(H\) inside \(T_0\) or
\(T_{N-1}\), so either case gives the first alternative.

A row-two witness is uniquely under an internal adjacent pair
\(T_j,T_{j+1}\). Its edge colour

\[
 Q=T_j\cap T_{j+1}
\]

has rank \(R-1\) and contains \(H\). Universality realizes the target
\(Q\) in some interval of length at most three. Since \(Q\supset H\), that
witness cannot be boundary-supported. A row-zero or row-one witness for
\(Q\) lies under at least four or three consecutive middle states,
respectively, and hence gives at least three or two \(Q\)-coloured edges.
A row-two
witness gives a \(Q\)-coloured edge; it cannot be the original edge,
because the unique row-two interval under that edge already has union
\(H\ne Q\). Thus the second alternative holds. \(\square\)

This is a sharply scoped no-go: every successful depth-three rethreading
must create one of these two resources for each protected hole.

## 10. Frozen exact \(k=11\to13\) audit

The proof-safe audit is

/Users/amir.nuriyev/Documents/problem/scratch/audit_k11_k13_global_flat_routing.rb

with SHA-256

9fa8bfcb4a60eb56d8b4e6c05b79045b2323488f0169a32cbda7a61fd589505c.

It reads only the frozen artifacts

\[
\begin{array}{c|l}
\text{object}&\text{SHA-256}\\ \hline
k=11\text{ carrier}&
a23b8d6847dba4350cca8dc8b9da89519e77067e58c866422713115887aaf397\\
k=13\text{ path}&
baa204bf8208c531cc1905c6cf53a2438db85a0b778231c0e59a631eef4b7973\\
k=13\text{ word}&
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0.
\end{array}
\]

It runs in under one second and performs no search. It checks all owner
ranks and Johnson adjacencies, and scans the full \(1,478,340\)-cell OR
triangle of the frozen word.

Take \(x=12,y=13\). The exact \(k=13\) middle path has:

\[
\begin{array}{c|rrrr}
\text{sector}&A&X&Y&U\\ \hline
\text{owners}&462&462&462&330\\
\text{components}&132&137&128&108.
\end{array}
\tag{10.1}
\]

Its edge census is

\[
\begin{array}{c|r}
AA&330\\
UU&222\\
XX&325\\
YY&334\\
XY\text{ vertical}&24\\
A\!X&136\\
A\!Y&128\\
U\!X&112\\
U\!Y&104.
\end{array}
\tag{10.2}
\]

Both global endpoints lie in the \(X\)-sector. Consequently:

\[
 a=b=132,
\qquad
 u+e_{XY}=108+24=132,
\]

and every one of the \(330\) both-new and \(462\) old-only immediate-lower
labels occurs exactly once. The single lost immediate-lower colour is in
the \(x\)-only family, with no repeat excess; the other three signatures
are exact rainbows:

\[
 e_{AX}-c_X=136-137=-1.
\tag{10.3}
\]

The \(108\) \(U\)-components satisfy (4.5) for all \(232\) old upper
targets:

\[
 165,\ 55,\ 11,\ 1
\]

at ranks \(8,9,10,11\), respectively.

The route is genuinely off-spine relative to the frozen \(k=11\) carrier:

\[
\begin{array}{c|r}
AA\text{ native}&23\\
AA\text{ off-spine}&307\\
UU\text{ native}&24\\
UU\text{ off-spine}&198\\
U\text{-ports natural}&72\\
U\text{-ports off-spine}&144.
\end{array}
\tag{10.4}
\]

There are \(40\) direct \(A\)-cross-\(U\) flags, split \(20/20\) between
the shores. Their intermediate candidate graph is a forest with component
histogram

\[
 (2,1)^{28}(3,2)^4(5,4)^1,
\tag{10.5}
\]

where \((v,e)\) records vertices and edges. Thus even the stronger
one-shore pseudoforest condition in Theorem 5.1 passes.

Finally, the audit constructs a deterministic nonzero core and a first-cell
pin injection for all \(4095\) lower targets. Its exact census is

\[
\begin{array}{c|r}
\text{pin row }0&990\\
\text{pin row }1&1391\\
\text{pin row }2&1714\\ \hline
\text{word mass}&5760\\
\text{core mass}&5417\\
\text{maximal post-pin mass}&6271.
\end{array}
\tag{10.6}
\]

It verifies (N), (P), \(D^3P=T\), and every lower equality. Since the
frozen middle path already satisfies all upper windows, Theorem 8.1 yields
another exact maximal word \(P\) in memory. Independently, the full
triangle scan verifies all \(8191\) nonempty targets of the frozen input
word.

This audit proves compatibility of the off-spine forest, ternary star,
shared-port, and common-core formulations on one frozen exact lift. It does
not decode the child from the parent by a uniform rule.

## 11. Precise open boundary

### Proved

1. Exact four-sector owner and Hamilton constraints.
2. Exact component and signed immediate-shadow ledgers.
3. Catalan flag-forest equivalence and capacitated \(A\)-port completion.
4. Ternary \(U\)-star equivalence and old-only upper path criterion.
5. Shared-port pseudoforest/SDR theorem.
6. Exact finite all-upper witness constraints.
7. Exact \((T,\phi)\) maximal-envelope criterion and its core-preserving
   common multirow extension.
8. Master equivalence for the Johnson-flat lane.
9. The depth-three rescue dichotomy.
10. A frozen exact \(11\to13\) realization of all interfaces.

### Not proved

No theorem here constructs these data for every \(r\). In particular, it
remains open to select simultaneously:

* a resident Catalan \(A\)-flag forest;
* a ternary \(U\)-star forest satisfying every upper subpath demand;
* a connected shared-endpoint \(X/Y\) routing;
* a central core and one common pin map satisfying (N)--(P).

This simultaneous construction is the smallest exact replacement lemma for
the failed first-occurrence induction. Marginal Hall, independent
depthwise selectors, and native occurrence priorities do not imply it.
