# PCTBRG: fixed-AA curvature, exact turn service, and the minimal obstruction

Date: 2026-07-30<br>
Lane: K<br>
Status: **proved exact endpoint/turn-service plus residual-flow theorem;
proved fixed-AA curvature obstruction; proved a smallest explicit typed-flow
counterexample at \(r=3\); authenticated on \(k=11,13,15\). No all-\(r\)
buffered-forest construction is claimed.**

## 0. Verdict

The weakest version of `PCTBRG(r,d)` cannot be obtained by fixing the child
`AA` forest and then solving only endpoint quotas and `BB` turns.

There are three exact reasons.

1. For a fixed `AA` path forest \(P_z\), its component sizes are precisely
   the positive-run lengths of the new Pascal coordinate \(z\). Hence

   \[
   \phi^-_{h,z}
   =\sum_{C\in\operatorname{comp}(P_z)}(h-|C|)^+.                 \tag{0.1}
   \]

   This is invariant under every endpoint or `BB`-turn completion, bounded
   or unbounded. A short `AA` component cannot be repaired downstream.

2. The exact \(q=1\) completion problem does have a sharp positive
   decomposition: first select one literal endpoint service for every
   missing `AA`-upper target and one literal turn service for every
   no-\(z\) upper target; after those atoms are fixed, the remainder is one
   integral bipartite \(b\)-flow.

3. Whenever the local configuration (5.1) exists—as it does abundantly in
   the authenticated matrices—the natural service matrix contains a
   \(3\times3\) determinant-two triangle. More strongly, an explicit
   \(r=3\) rank-two-rainbow `AA` forest admits the complete typed circulation
   but has one no-\(z\) upper target with no internal provider.

The authenticated factors identify the common symbolic object. It is not a
local reverse-Pascal rule: it is a pair of nonlocal Catalan path routers
joined by cross arcs. Their fixed `AA` forests contain respectively

\[
                         13,\qquad 33,\qquad 95                  \tag{0.2}
\]

paths of length four. At the next test \(h=5\), no fixed-`AA` turn library
can remove even these split-coordinate lower defects.

The weakest viable new-coordinate state is therefore:

* choose an \(h\)-buffered rank-\((r-1)\)-rainbow `AA` forest before the TU
  completion;
* choose the endpoint/turn service section and pass its residual Hall cuts;
* require every finite `BB` path to have at least \(h\) vertices.

The remaining all-\(r\) problem is existence of this buffered, protected,
compiler-compatible forest-and-service section. No generic search, SAT/CP
solve, web access, or K16 seam computation was used.

## 1. Pascal split and exact counts

Let \(\Omega\) have size \(2r\), let \(z\notin\Omega\), and put

\[
 \mathcal A=\{z\}+\binom{\Omega}{r},\qquad
 \mathcal B=\binom{\Omega}{r+1}.                                  \tag{1.1}
\]

Write

\[
 C=\operatorname{Cat}_r=\frac1{r+1}\binom{2r}{r}.                 \tag{1.2}
\]

Fix a spanning nonisolated linear forest \(P\) on
\(\binom{\Omega}{r}\) whose edge intersections enumerate
\(\binom{\Omega}{r-1}\) exactly once. Then

\[
 |V(P)|=(r+1)C,\qquad |E(P)|=rC,\qquad
 \#\operatorname{comp}(P)=C.                                    \tag{1.3}
\]

Let \(E\) and \(I\) be its degree-one and degree-two vertex sets. Since every
component is a nontrivial path,

\[
                         |E|=2C,\qquad |I|=(r-1)C.                \tag{1.4}
\]

The \(B\)-owner and no-\(z\) upper-target counts are

\[
 |\mathcal B|=rC,\qquad
 |\mathcal V|:=\left|\binom{\Omega}{r+2}\right|
 =\frac{r(r-1)}{r+2}C.                                          \tag{1.5}
\]

Thus a complete `BB` turn map has forced excess

\[
 |I|-|\mathcal V|=\frac{2(r-1)}{r+2}C.                           \tag{1.6}
\]

This scalar excess does not imply provider Hall or right-degree
compatibility.

## 2. The common symbolic turn selector

Assume a child factor contains \(P\) as its `AA` edges and has the exact
lower \(q=1\) deck. For each \(T\in\binom{\Omega}{r}\), write the unique edge
of lower colour \(T\) as

\[
                        (T+a)(T+b),\qquad p(T)=\{a,b\}.            \tag{2.1}
\]

Here \(a,b\in(\Omega\cup\{z\})\setminus T\).

### Theorem 2.1 (split-selector normal form)

For every old owner \(T\),

\[
 z\in p(T)\quad\Longleftrightarrow\quad T\in E,                  \tag{2.2}
\]

and then \(p(T)\setminus\{z\}\) is its unique cross mark. Also

\[
 z\notin p(T)\quad\Longleftrightarrow\quad T\in I,               \tag{2.3}
\]

and then \(p(T)\) is its `BB` turn.

#### Proof

The \(A\)-owner \(z+T\) already has \(d_P(T)\) incident `AA` edges. If
\(d_P(T)=1\), degree two forces exactly one cross edge. Its intersection is
\(T\), so lower exactness identifies it with (2.1), and one mark is \(z\).
If \(d_P(T)=2\), the \(A\)-owner is saturated; the unique lower-\(T\) edge
must lie on the \(B\) shore. The converse implications are identical.
\(\square\)

For \(T\in I\), put

\[
 V(T)=T\cup p(T)\in\binom{\Omega}{r+2}.                            \tag{2.4}
\]

The selected `BB` edge is the Boolean diamond

\[
 T+a\quad -- \quad T+b,\qquad V(T)=T+a+b.                         \tag{2.5}
\]

Thus every turn is a rank-two flag \((T,V)\) with \(T\subset V\). This is
the common symbolic turn pattern in all three authenticated packages.

Let \(Q\) be the selected `BB` graph on \(\mathcal B\). Cross edges pair the
endpoint stubs of \(P\) with the non-cycle stubs of \(Q\). In the
authenticated packages, \(Q\) is a linear forest with \(C\) components,
isolated vertices allowed. Contracting the \(P\)- and \(Q\)-paths gives the
nonlocal component router.

## 3. Exact endpoint-turn service plus one residual flow

For an `AA` edge \(TT'\), its upper colour is \(T\cup T'\). Let

\[
 M=\{U\in\mathcal B:
 U\ne T\cup T'\text{ for every }TT'\in P\}.                       \tag{3.1}
\]

For \(T\in I\), \(V\in\mathcal V\), \(T\subset V\), write

\[
 V\setminus T=\{a,b\},\qquad
 \mu(T,V)=\{T+a,T+b\}\subseteq\mathcal B.                         \tag{3.2}
\]

An **endpoint service section** is a set
\(\mathscr R\subseteq E\times M\) containing exactly one pair \((T,U)\)
for every \(U\in M\), with \(T\subset U\), and using each \(T\in E\) at
most once. Write
\(E_{\mathscr R}=\{T:\exists U,\ (T,U)\in\mathscr R\}\).

A **turn service section** is a set
\(\mathscr S\subseteq I\times\mathcal V\) containing exactly one pair
\((T,V)\) for every \(V\in\mathcal V\), with \(T\subset V\), and using each
\(T\in I\) at most once. It forces the two incidences in \(\mu(T,V)\).
Write \(I_{\mathscr S}=\{T:\exists V,\ (T,V)\in\mathscr S\}\).

Let \(f_U\) be the forced incidence load of \(U\) and require \(f_U\le2\).
Put

\[
 L=(E\setminus E_{\mathscr R})
   \sqcup(I\setminus I_{\mathscr S}),                             \tag{3.3}
\]

\[
 d_T=\begin{cases}1,&T\in E,\\2,&T\in I,\end{cases}
 \qquad b_U=2-f_U,                                                 \tag{3.4}
\]

and, for \(X\subseteq L\),

\[
                    \Gamma_X(U)=|\{T\in X:T\subset U\}|.         \tag{3.5}
\]

### Theorem 3.1 (exact service-section/Gale-Hall theorem)

The fixed `AA` forest extends to a degree-two child factor having both lower
\(q=1\) decks exact and both upper \(q=1\) decks complete if and only if
there is a service section \((\mathscr R,\mathscr S)\) satisfying

\[
 \boxed{
 \sum_{T\in X}d_T
 \le
 \sum_{U\in\mathcal B}\min\{b_U,\Gamma_X(U)\}
 \quad\text{for every }X\subseteq L.}                             \tag{3.6}
\]

#### Proof

Given a completion, select one cross edge witnessing every \(U\in M\) and
one `BB` edge witnessing every \(V\in\mathcal V\). Distinct upper targets
use distinct endpoint or internal lower colours, giving
\((\mathscr R,\mathscr S)\). Removing them leaves a bipartite containment
\(b\)-matching from \(L\) to \(\mathcal B\), with left demands \(d_T\),
right capacities \(b_U\), and unit edge capacities. Its max-flow cuts give
(3.6).

Conversely, force the service section and form

\[
                         s\longrightarrow T\longrightarrow U
                           \longrightarrow t                       \tag{3.7}
\]

with capacities \(d_T,1,b_U\). Equation (3.6) is exactly its capacitated
Hall condition. Total residual demand equals total residual right capacity,
so integral max flow gives one remaining cross incidence at each unused
endpoint and two distinct incidences at each unused internal owner. The
latter form a literal `BB` edge. The service atoms cover \(M\) and all of
\(\mathcal V\). \(\square\)

This is the sharp positive result. The nonlinear part of the \(q=1\) gate
is only the literal service section; after it is fixed, no rounding remains.

A first necessary condition follows before right capacities:

\[
 \boxed{
 |\{T\in I:T\subset V\text{ for some }V\in\mathcal W\}|
 \ge|\mathcal W|
 \quad(\mathcal W\subseteq\mathcal V).}                           \tag{3.8}
\]

This **turn-Hall inequality** chooses distinct internal providers. It is not
sufficient for (3.6), because each diamond consumes two intermediate-owner
capacities.

## 4. Conserved Pascal point degrees

Let \(c_U\) be the cross-edge load of \(U\in\mathcal B\), and let \(b_V\) be
the turn load of \(V\in\mathcal V\). Write \(\mathbf1_S\) for a set's
coordinate-incidence vector.

### Proposition 4.1 (Pascal moment identity)

Every completion satisfies

\[
 2\sum_{U\in\mathcal B}\mathbf1_U
 =\sum_{U\in\mathcal B}c_U\mathbf1_U
  +\sum_{T\in I}\mathbf1_T
  +\sum_{V\in\mathcal V}b_V\mathbf1_V.                            \tag{4.1}
\]

#### Proof

A cross edge contributes \(\mathbf1_U\). A turn \((T,V)\), with
intermediate owners \(T+a,T+b\), contributes

\[
 \mathbf1_{T+a}+\mathbf1_{T+b}
 =\mathbf1_T+\mathbf1_{T+a+b}
 =\mathbf1_T+\mathbf1_V.                                         \tag{4.2}
\]

Sum the two incidences at every \(B\)-owner. \(\square\)

If \(b_V=1+e_V\), then \(\sum_Ve_V\) is (1.6), and for every coordinate
\(x\in\Omega\),

\[
 \gamma_x:=\sum_{V\ni x}e_V
 =2\binom{2r-1}{r}
  -\sum_{U\ni x}c_U
  -|\{T\in I:x\in T\}|
  -\binom{2r-1}{r+1}.                                              \tag{4.3}
\]

Hence \(0\le\gamma_x\le\sum_Ve_V\) is a necessary hypersimplex marginal
condition on the endpoint selector. It does not imply turn Hall, right
degrees, or chronology.

## 5. Why the natural joint matrix is not TU

Linearize a turn by \(y_{T,V}\). It contributes one unit to each of the two
intermediate owners in \(\mu(T,V)\).

### Theorem 5.1 (minimal determinant-two turn minor)

Fix \(V\in\mathcal V\). Choose \(a,b,c\in V\) such that

\[
 T_{ab}=V\setminus\{a,b\},\quad
 T_{bc}=V\setminus\{b,c\},\quad
 T_{ca}=V\setminus\{c,a\}                                       \tag{5.1}
\]

all lie in \(I\). On the intermediate-owner rows
\(U_a=V-a,U_b=V-b,U_c=V-c\), the corresponding columns contain

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad \det=2.                                                   \tag{5.2}
\]

Thus the natural endpoint-plus-turn matrix is neither totally unimodular
nor balanced. This is the smallest possible non-TU \(0/1\) minor.

#### Proof

Each turn uses the two codimension-one intermediates between its lower and
upper flag. Reading those incidences gives (5.2). Every \(1\times1\) or
\(2\times2\) \(0/1\) determinant has absolute value at most one.
\(\square\)

This does not exclude a larger extended formulation. After all cross edges
are fixed, let \(c_U\) be their load at \(U\) and put
\(\beta_U=2-c_U\), the full required \(BB\)-degree. For the selected
\(BB\) graph \(F\), the missing parity state is the usual degree-cut parity

\[
 |F\cap\delta(S)|\equiv\sum_{U\in S}\beta_U\pmod2.                \tag{5.3}
\]

## 6. The common bounded turn motif

Fix a rank-\((r-1)\) core \(R\) and four labels
\(\{0,1,2,3\}\) outside it. Put

\[
 T_i=R+i,\qquad
 V_j=R+\bigl(\{0,1,2,3\}\setminus\{j\}\bigr),
 \qquad i\ne j,                                                   \tag{6.1}
\]

and denote turn \((T_i,V_j)\) by \(q_{ij}\).

### Theorem 6.1 (four-label turn kernel)

A signed change \(z=(z_{ij})\) preserves every lower colour, upper colour,
and intermediate-owner degree in this cell if and only if

\[
 z_{ij}=-z_{ji},\qquad
 \sum_{j\ne i}z_{ij}=0.                                          \tag{6.2}
\]

Thus the local integer kernel is the circulation lattice of \(K_4\). It is
generated by oriented triangles, and a minimum-support nonzero squarefree
change is

\[
 q_{ab}+q_{bc}+q_{ca}
 -q_{ba}-q_{cb}-q_{ac}.                                          \tag{6.3}
\]

It changes three old turns to three new turns: a literal alternating
\(C_6\). Support six is minimal. Simple four-cycle circulations may also be
primitive; only minimum support and triangle generation are asserted.

#### Proof

Lower-colour preservation gives

\[
                         \sum_{j\ne i}z_{ij}=0.                   \tag{6.4}
\]

For intermediate owner \(\{i,j\}\), degree preservation gives

\[
 \sum_{\ell\notin\{i,j\}}(z_{i\ell}+z_{j\ell})=0.                \tag{6.5}
\]

Combining the two row equations (6.4) with (6.5) gives
\(z_{ij}+z_{ji}=0\). Conversely, skew-symmetry and the row sums imply every
upper and intermediate row. \(\square\)

This is the bounded motif suggested by the authenticated turn tables. It is
a genuine exact-factor exchange, but it fixes the entire `AA` forest.

## 7. Fixed-AA curvature rigidity

For a completed physical factor, the states containing \(z\) are exactly
the \(A\)-owners, and the induced graph on them is exactly \(P\).

### Theorem 7.1 (AA components are the positive-run spectrum)

The finite positive \(z\)-runs are in bijection with the path components of
\(P\), preserving lengths. Consequently,

\[
 \boxed{
 \phi^-_{h,z}
 =\sum_{C\in\operatorname{comp}(P)}(h-|C|)^+.}                    \tag{7.1}
\]

Every completion, endpoint reassignment, turn circulation, or compound turn
packet which fixes \(P\) has

\[
                         \Delta\phi^-_{h,z}=0.                    \tag{7.2}
\]

#### Proof

Every internal vertex of a \(P\)-path has both factor edges in the \(A\)
shore. Each path endpoint has exactly one `AA` and one cross edge. Therefore
entering the \(A\) shore traverses one whole \(P\)-component and then leaves
it. No completion choice can split or concatenate such positive blocks
without changing an `AA` edge. Apply the run-curvature identity. \(\square\)

Let \(Q\) be the selected `BB` graph. Every path component of \(Q\),
including an isolated vertex, is one finite zero-gap of the \(z\)-trace. A
cycle component of \(Q\) is an all-zero physical component and contributes
no finite gap. Hence

\[
 \phi^+_{h,z}
 =\sum_{D\in\operatorname{pathcomp}(Q)}(h-|D|)^+.                 \tag{7.3}
\]

### Corollary 7.2 (fixed-AA PCTBRG no-go)

If \(P\) has a component of size \(<h\), no endpoint-quota/`BB`-turn
circulation with \(P\) fixed can produce an \(h\)-buffered child. This holds
even for unbounded-support, overlapping, or nonlocal turn packets.

In particular, the alternating \(C_6\) in Theorem 6.1 has zero lower
split-coordinate curvature charge. It may alter other coordinates and the
upper split curvature through its physical halos, but it cannot remove the
defect in (7.1).

Thus the architecture

\[
 \text{fix }P
 \longrightarrow \text{solve endpoint quota and turns}
 \longrightarrow \text{regenerate the buffer}                   \tag{7.4}
\]

is false. The `AA` forest must be selected buffered from the outset, or the
atlas must contain columns which change `AA` edges.

## 8. Authentication on \(k=11,13,15\)

Here the child dimension is \(k=2r+1\), the split is \(z=k-1\), and the next
outer test is \(h=5\).

### 8.1 Exact path-curvature table

\[
\begin{array}{c|c|c|c|c}
k&r&C&P\text{ sizes }<5&Q\text{ sizes }<5\\ \hline
11&5&42&4^{13}&1^4,2^5,3^{10},4^4\\
13&6&132&4^{33}&1^9,2^{23},3^{17},4^{13}\\
15&7&429&4^{95}&1^{22},2^{39},3^{73},4^{33}.
\end{array}                                                       \tag{8.1}
\]

Therefore (7.1)--(7.3) give

\[
\begin{array}{c|r|r}
k&\phi^-_{5,z}&\phi^+_{5,z}\\ \hline
11&13&55\\
13&33&152\\
15&95&384.
\end{array}                                                       \tag{8.2}
\]

These are the per-split-coordinate versions of global defects

\[
 (143,605),\qquad(429,1976),\qquad(1425,5760).                    \tag{8.3}
\]

Thus no fixed-`AA` turn deck can pay the required split charges

\[
 (-13,+55),\qquad(-33,+152),\qquad(-95,+384).                    \tag{8.4}
\]

### 8.2 No strict local reverse-Pascal rule

\[
\begin{array}{c|c|c}
k&\text{endpoint equality}&\text{internal pair equality}\\ \hline
11&8/84&23/168\\
13&18/264&50/660\\
15&44/858&271/2574.
\end{array}                                                       \tag{8.5}
\]

No complete `AA` component obeys the elementary line-graph rule. The exact
turn-load histograms are

\[
\begin{array}{c|l}
k&\text{load: number of no-}z\text{ upper targets}\\ \hline
11&1{:}72,\ 2{:}48\\
13&1{:}360,\ 2{:}105,\ 3{:}30\\
15&1{:}1470,\ 2{:}492,\ 3{:}40.
\end{array}                                                       \tag{8.6}
\]

This authenticates the nonlocal selector normal form; it does not prove
that every conceivable bounded labelled rule is impossible.

### 8.3 Non-TU minors and Pascal moments

\[
\begin{array}{c|r|c}
k&\text{triangle minors}&\text{upper rows containing one}\\ \hline
11&1226&120/120\\
13&9980&495/495\\
15&78811&1998/2002.
\end{array}                                                       \tag{8.7}
\]

The excess-turn counts are \(48,165,572\). Their coordinate point-degree
ranges are

\[
                         [32,35],\qquad[107,117],\qquad[355,386]. \tag{8.8}
\]

All pass their hypersimplex bounds. Marginal feasibility is not the missing
finite gate.

## 9. A smallest explicit turn-Hall obstruction

Let

\[
 \Omega=\{0,1,2,3,4,5\},\qquad W=\{1,2,3,4,5\}.                  \tag{9.1}
\]

Pair the ten edges of \(K_5\) by the disjoint-edge involution

\[
 12\leftrightarrow34,\quad
 13\leftrightarrow45,\quad
 14\leftrightarrow25,\quad
 15\leftrightarrow23,\quad
 24\leftrightarrow35.                                            \tag{9.2}
\]

Call it \(\pi\). For every \(e\in\binom W2\), define

\[
 I_e=\{0\}\cup e,\qquad H_e=W\setminus\pi(e).                    \tag{9.3}
\]

Join \(I_e\) to \(H_e\). These ten edges cover every rank-two colour not
containing \(0\). Identify \(W\) with \(\mathbb Z_5\), and for every
\(j\in\mathbb Z_5\), join

\[
 I_{\{j-1,j\}}\quad\text{to}\quad I_{\{j-2,j\}}.                 \tag{9.4}
\]

The five pairs in (9.4) partition the internal vertices, and their
intersections are the five colours \(\{0,j\}\). Thus (9.3)--(9.4) form five
four-vertex paths and enumerate every rank-two lower colour exactly once.
Their internal set is

\[
                         I=\{T\in\binom{\Omega}{3}:0\in T\}.      \tag{9.5}
\]

The typed containment circulation is feasible:

1. the ten endpoint edges have all ten distinct upper colours containing
   \(0\), so the missing `AA`-upper targets are the five four-subsets of
   \(W\);
2. orient \(K_5\) as a regular tournament and, for endpoint \(H_e\), cross
   to the four-subset of \(W\) obtained by deleting the chosen head of
   \(\pi(e)\); every missing target receives exactly two cross edges;
3. for internal \(I_e\), among the three triples \(H\subset W\) containing
   \(e\), omit \(H_e\) and use the two rank-four owners
   \(\{0\}\cup H\) from the other two triples as its `BB` incidences. Since
   \(e\mapsto H_e\) is a perfect edge-triangle matching, every \(B\)-owner
   containing \(0\) receives exactly two incidences.

All typed left quotas, right degrees, and missing `AA`-upper rows pass.
Nevertheless

\[
                              W=\{1,2,3,4,5\}                    \tag{9.6}
\]

has no turn provider: every \(T\in I\) contains \(0\), while a provider
must satisfy \(T\subset W\). The displayed completion covers the other five
rank-five targets twice and misses \(W\).

This violates the singleton case of (3.8). It is minimal in semilength. For
\(r=2\), the only rank-\((r+2)\) target is \(\Omega\). Every internal
\(T\) has exactly two rank-three \(B\)-supersets; its typed demand is two,
so every feasible typed completion must select both, and their union is
\(\Omega\). Thus the unique upper turn row is automatic at \(r=2\).

### Theorem 9.1 (minimal typed-flow counterexample)

At \(r=3\), a rank-two-rainbow nonisolated Catalan `AA` forest can have a
feasible complete typed lower-bound circulation but an infeasible paired
upper-turn system. Thus turn-provider Hall state is necessary in every
all-\(r\) theorem; it cannot be derived from typed flow or scalar excess.

## 10. One bounded motif is not a universal curvature regenerator

A curvature charge belongs to a **closed \(h\)-collared physical motif
type**, not merely to abstract labels. Old and new \(h\)-collars must be
fixed. Relabelling, translation, reversal, and fixed-core extension then
preserve scalar charge. Disjoint copies add; an overlapping cluster must be
materialized as a new compound type.

Put

\[
 \kappa(g)=(\Delta\Phi_h^-(g),-\Delta\Phi_h^+(g)).                \tag{10.1}
\]

### Proposition 10.1 (rank-one motif obstruction)

If a library has only one nonzero collared charge type, plus zero-charge
relays, every repair demand lies on one integer ray. The authenticated
demands

\[
 D_{11}=(-143,605),\quad
 D_{13}=(-429,1976),\quad
 D_{15}=(-1425,5760)                                               \tag{10.2}
\]

do not. Their pair determinants are

\[
 -23023,\qquad38445,\qquad344760.                                 \tag{10.3}
\]

The gcd of their absolute values is one. Consequently any fixed integer
charge lattice containing all three demands has rank two and equals
\(\mathbb Z^2\).

#### Proof

Copies of one collared type have charges \(n\kappa\); zero columns do not
change the span. Nonzero determinants prove noncollinearity. The index of a
lattice generated in \(\mathbb Z^2\) is the gcd of its \(2\times2\) minors.
\(\square\)

This is necessary, not a physical construction. The primitive arithmetic
columns

\[
                         u=(-1,4),\qquad v=(-1,5)                 \tag{10.4}
\]

represent all three demands with nonnegative coefficients:

\[
\begin{array}{c|r|r}
k&\#u=5\Phi^-_5-\Phi^+_5&\#v=\Phi^+_5-4\Phi^-_5\\ \hline
11&110&33\\
13&169&260\\
15&1365&60.
\end{array}                                                       \tag{10.5}
\]

Thus scalar curvature has no two-column arithmetic obstruction on these
packages. Literal owner, Johnson, path, halo, witness, and compiler
compatibility remain.

For the turn-only motif (6.3), Theorem 7.1 is sharper than the ray test: its
split-coordinate lower charge is identically zero, whatever its six
physical halos.

## 11. The exact extra state now forced

### Corollary 11.1 (new-coordinate buffered-router criterion)

A completion is \(h\)-biresident in coordinate \(z\) if and only if

1. every `AA` path component has at least \(h\) vertices; and
2. every finite `BB` path component has at least \(h\) vertices.

`BB` cycle components are constant-zero traces and do not count as finite
gaps.

For fixed \(h\), condition 2 is a finite bounded-CSP extension of the turn
system: forbid every selected endpoint-to-endpoint `BB` path with fewer
than \(h\) vertices, including an isolated \(B\)-owner. It is not a network
row. Condition 1 must hold when \(P\) is chosen.

The scalar averages are

\[
 \frac{|V(P)|}{C}=r+1,\qquad
\frac{|\mathcal B|}{C}=r.                                       \tag{11.1}
\]

The second ratio is the mean finite-\(BB\)-path length when (Q) has (C)
path components and no cycle component, as in the intended router class.
Hence (h\le r) has no component-mass obstruction.

The weakest viable `PCTBRG` interface must carry:

* an \(h\)-buffered `AA` forest, or explicit `AA`-changing columns;
* a literal endpoint/turn service section satisfying (3.6);
* turn Hall and the required blossom parity for the protected atlas;
* the finite `BB` short-path state;
* the already isolated all-depth witness section and three compiler Hall
  systems.

## 12. Frozen deterministic audits

The authenticated symbolic replay is

```text
scratch/audit_k11_k13_k15_pctbrg_turn_pattern_20260730.py
910866c75a135e48a833e6ac376f19c8570db3ba28940aaac8ea367c4eadfd02

scratch/k11_k13_k15_pctbrg_turn_pattern_20260730.audit.json
b7ba3a2e5329751c61239be4d66b6a781e205a53a380c9b1a697c4a5f7370c31
```

It hash-pins the six authenticated source factors/compiler words;
reconstructs the `AA` and `BB` forests; checks selector rows, turn loads,
Pascal moments, hypersimplex bounds, and determinant-two minors; and records
the complete component-size histograms.

The explicit smallest obstruction is

```text
scratch/audit_r3_pctbrg_typed_flow_turn_hall_obstruction_20260730.py
be97ea793a1d391ebe23e4ffc514e7bac8e4037204abc2e16d11979444bcfa98

scratch/r3_pctbrg_typed_flow_turn_hall_obstruction_20260730.audit.json
ac5d535d654c7702d18b55e462d751edc2712e2c5a3b6a6263b2b6f52436cd3b
```

It constructs the five four-vertex `AA` paths, literal typed completion, and
forced uncovered target \(62=\{1,2,3,4,5\}\).

Both replays are solver-free, deterministic, and complete for their stated
finite objects. They do not search for another forest, turn map, or all-\(r\)
construction.

## 13. Final proved boundary

The exact \(q=1\) gate is now

\[
 \boxed{\text{literal endpoint/turn service section}
        +\text{ residual capacitated Hall}.}                      \tag{13.1}
\]

The fixed-`AA` regeneration strategy is closed:

\[
 \boxed{P\text{ fixed and short}
        \Longrightarrow
        \phi^-_{h,z}>0\text{ for every turn completion}.}         \tag{13.2}
\]

Typed flow alone is closed by the explicit \(r=3\) obstruction. What
remains is one sharply strengthened all-\(r\) lemma: construct an
\(h\)-buffered rank-\((r-1)\)-rainbow `AA` forest together with a protected
turn service section satisfying (3.6), finite `BB` path buffering, all-depth
literal witnesses, and the three compiler Hall systems.

No unconditional coefficient-one or all-\(r\) construction follows yet.
