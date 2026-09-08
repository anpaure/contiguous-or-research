# S9: exact restitution and positive durable-forest theorems

Date: 2026-07-25

## 0. Outcome

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
N_h=\binom{2m}{m-h},\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that
\(1\le H<m\).

This report implements the constant-one redirect. It does not use
histogram cancellation as a sufficient condition.

First, the active stopped-thread law is corrected to its exact form. If
\(F^{\rm surv}_{j+1}\) is the actual maximal-retention survivor forest on
\(X_{j+1}\) after level \(j\), then

\[
\boxed{
D_{j+1}-D_j+S_j
=\tau^{\rm term}_{j+1}-\sigma^{\rm src}_j.}
\tag{0.1}
\]

The two boundary histograms have mass exactly

\[
\kappa_{j+1}=c(F^{\rm surv}_{j+1}),
\]

so

\[
\boxed{
\|D_{j+1}-D_j+S_j\|_1\le2\kappa_{j+1}.}
\tag{0.2}
\]

This is a necessary projection of an actual forest. Its converse is false
and is not used.

Second, the exact durable-edge formula has the following positive forest
form, provided both active flag families are nonempty. Let
\(G=F_0[X_1]\) and \(b_0=c(G)\). Among all spanning directed
subforests \(D\subseteq G\) which admit lower and upper active flag systems
making every edge of \(D\) durable through its common lifetime,

\[
\boxed{
K_H^{\min}+b_0=\min_D c(D).}
\tag{0.3}
\]

For the global odd-cut suffix, \(b_0\le W/(m+1)=o(W/H)\). Therefore

\[
\boxed{
K_H^{\min}=o(W/H)}
\]

is equivalent to the existence of one integral admissible durable forest
with

\[
\boxed{c(D)=o(W/H).}
\tag{0.4}
\]

Admissibility of a fixed \(D\) has an exact recursive boundary-Hall
criterion proved in Section 3. This is a positive integral theorem, not a
curvature test.

Third, there is a direct radius-homogeneous positive theorem. For one exact
depth-\(H\) band SCD, let \(\mathcal D_r\) be the directed graph of fully
durable arcs between its lifetime-\(r\) owners, and let
\(\operatorname{pc}(\mathcal D_r)\) be the minimum component count of a
spanning directed path forest. Then

\[
\boxed{
\operatorname{pc}(\mathcal D_r)
=
\min_{\prec}
\max_{S}
\bigl(|S|-|N^+_{\mathcal D_r,\prec}(S)|\bigr),}
\tag{0.5}
\]

where \(\prec\) ranges over total orders and only forward durable arcs are
used in the neighborhood. The corresponding literal central-band word has
exact augmented-prefix length

\[
\boxed{
W+2\sum_{r=1}^H r\,\operatorname{pc}(\mathcal D_r).}
\tag{0.6}
\]

Consequently either of

\[
\sum_{r=1}^H r\,\operatorname{pc}(\mathcal D_r)=o(W),
\tag{0.7}
\]

or the stronger unweighted condition

\[
\sum_{r=1}^H\operatorname{pc}(\mathcal D_r)=o(W/H),
\tag{0.8}
\]

proves \(\mathrm{RSCD}_A\) for this fixed \(A\). Holding for every fixed
\(A\), the accepted outer-tail step and diagonalization give constant one.

Sections 4--5 give degree, fractional-transport, and cycle-cover
sufficient conditions for (0.8). Every condition is supported on literal
jointly durable arcs. None is established by AD7's proved rankwise
support, trace entropy, or aggregate variation arguments.

The remaining existence assertion is exact: construct one integral band
SCD for which the durable path-cover deficiencies in (0.5) have total
\(o(W/H)\), or construct one dynamic admissible forest satisfying the
recursive Hall tests with that many components. This assertion remains
unproved.

---

## 1. Exact active restitution

Let

\[
X_0\supseteq X_1\supseteq\cdots\supseteq X_H,
\qquad |X_j|=N_j,
\]

and fix integral active lower and upper-complement flag systems
\((\mathbf L,\mathbf R)\). For \(1\le j\le H\), define

\[
d_j(v)=L_{j-1}(v)\setminus L_j(v),
\qquad v\in X_j,
\tag{1.1}
\]

and let \(D_j\) be its coordinate histogram. For \(1\le j<H\), let
\(S_j\) be the stopped histogram

\[
S_j(x)=
|\{v\in X_j\setminus X_{j+1}:d_j(v)=x\}|.
\tag{1.2}
\]

Use maximal retention for the fixed flags. Let
\(F^{\rm surv}_{j+1}\) be the directed forest on \(X_{j+1}\) consisting
of the initial edges which satisfy both lower and upper durable identities
at every level \(0,\ldots,j\). Write

\[
\kappa_{j+1}=c(F^{\rm surv}_{j+1})
=N_{j+1}-|E(F^{\rm surv}_{j+1})|.
\tag{1.3}
\]

Define

\[
\tau^{\rm term}_{j+1}(x)
=|\{v\in X_{j+1}:
\operatorname{outdeg}_{F^{\rm surv}_{j+1}}(v)=0,\
d_{j+1}(v)=x\}|,
\tag{1.4}
\]

and

\[
\sigma^{\rm src}_j(x)
=|\{w\in X_{j+1}:
\operatorname{indeg}_{F^{\rm surv}_{j+1}}(w)=0,\
d_j(w)=x\}|.
\tag{1.5}
\]

Isolated vertices occur once in each boundary histogram.

### Theorem 1.1 (exact stopped-thread restitution)

For every \(1\le j<H\),

\[
\boxed{
D_{j+1}-D_j+S_j
=\tau^{\rm term}_{j+1}-\sigma^{\rm src}_j.}
\tag{1.6}
\]

In particular,

\[
\boxed{
\|D_{j+1}-D_j+S_j\|_1\le2\kappa_{j+1}.}
\tag{1.7}
\]

#### Proof

The histogram \(D_j-S_j\) is exactly the \(d_j\)-histogram on the
continuing owners \(X_{j+1}\). Every survivor edge \(v\to w\) satisfies
the coordinate shift

\[
d_{j+1}(v)=d_j(w).
\tag{1.8}
\]

Cancel the \(D_{j+1}\)-contribution at the tail against the
\((D_j-S_j)\)-contribution at the head of every survivor edge. Since the
graph is a directed path forest, every nonterminal is used once as a tail
and every nonsource once as a head. The uncancelled terms are precisely
(1.4) and (1.5), with the displayed signs. This proves (1.6).

Every directed path component has one terminal and one source, including
an isolated vertex. Both boundary histograms therefore have mass
\(\kappa_{j+1}\). The triangle inequality proves (1.7). \(\square\)

For the upper-complement deletion symbols the same proof applies with the
durable shift oriented from the source contribution at level \(j\) to the
head contribution at level \(j+1\); source and terminal roles in the
display are reversed. The boundary mass and the factor \(2\) are
unchanged.

Let

\[
G_{j+1}=F_0[X_{j+1}]
\]

have \(\rho^0_{j+1}\) components, and let \(b_j\) be the number of its
edges which have failed by level \(j\). Maximal retention gives

\[
\boxed{
\kappa_{j+1}=\rho^0_{j+1}+b_j.}
\tag{1.9}
\]

Indeed, deleting one edge from a forest increases its component count by
one. Each globally nondurable edge contributes to \(b_j\) only from its
first failure until an endpoint stops, and hence at no more than \(H\)
levels. Thus

\[
\sum_{j=1}^{H-1}b_j\le HK_H.
\tag{1.10}
\]

For global suffixes on \(p=W/(m+1)\) original paths,

\[
\rho^0_{j+1}\le p.
\tag{1.11}
\]

Equations (1.7)--(1.11) recover the necessary summed bound

\[
\sum_{j=1}^{H-1}
\|D_{j+1}-D_j+S_j\|_1
\le2Hp+2HK_H.
\tag{1.12}
\]

The law has no useful reverse direction. The right side of (1.6) is a
difference of labelled boundary histograms, and distinct components can
cancel in that projection. The positive theorems below retain the actual
forest and its Hall constraints.

---

## 2. Dynamic durable forests

Let

\[
G=F_0[X_1],
\qquad
b_0=c(G)=N_1-|E(G)|.
\tag{2.1}
\]

A triple \((D,\mathbf L,\mathbf R)\) is called **dynamically admissible**
when:

1. \(D\subseteq G\) is a spanning directed path subforest on \(X_1\);
   isolated vertices count as components;
2. \(\mathbf L\in\mathfrak F^-_\tau\) and
   \(\mathbf R\in\mathfrak F^+_\tau\);
3. for every edge \(v\to w\in D\) and every
   \(0\le h<\min\{\tau(v),\tau(w)\}\),
   \[
   L_{h+1}(v)=L_h(v)\cap L_h(w),
   \tag{2.2}
   \]
   \[
   R_{h+1}(w)=R_h(v)\cap R_h(w).
   \tag{2.3}
   \]

Thus every edge of \(D\) is literally durable through its common lifetime.

### Theorem 2.1 (exact durable-forest formula)

If either active flag family is empty, no dynamically admissible triple
exists. Otherwise,

\[
\boxed{
K_H^{\min}+b_0
=
\min_{(D,\mathbf L,\mathbf R)\ {\rm dynamically\ admissible}}
c(D).}
\tag{2.4}
\]

#### Proof

Fix a flag pair. Its full durable edge set is a subset of \(E(G)\), hence
a spanning directed subforest after isolated vertices are included. Its
component count is

\[
N_1-|E^{\rm dur}(\mathbf L,\mathbf R)|.
\tag{2.5}
\]

Conversely, every admissible \(D\) is contained in the full durable edge
set of its flags, so the full durable subforest has no more components
than \(D\). Therefore

\[
\min_{\rm admissible}c(D)
=N_1-\max_{\mathbf L,\mathbf R}|E^{\rm dur}(\mathbf L,\mathbf R)|.
\tag{2.6}
\]

Since

\[
|E^\circ|=|E(G)|=N_1-b_0,
\]

the exact durable-edge formula gives

\[
\begin{aligned}
K_H^{\min}
&=|E^\circ|-\max_{\mathbf L,\mathbf R}|E^{\rm dur}|\\
&=N_1-b_0-\max_{\mathbf L,\mathbf R}|E^{\rm dur}|\\
&=\min_{\rm admissible}c(D)-b_0.
\end{aligned}
\]

This is (2.4). \(\square\)

### Corollary 2.2 (the positive component gate)

For the globally contiguous odd-cut lifetime assignment,

\[
b_0\le\frac{W}{m+1}=o(W/H).
\tag{2.7}
\]

Assume both active flag families are nonempty. Then

\[
\boxed{
K_H^{\min}=o(W/H)}
\]

if and only if there is a dynamically admissible triple with

\[
\boxed{c(D)=o(W/H).}
\tag{2.8}
\]

Moreover, for every \(h\), each component of \(D\) lies in one original
path and is a contiguous interval there. The global set \(X_h\) intersects
that original path in a suffix. Consequently

\[
\boxed{c(D[X_h])\le c(D).}
\tag{2.9}
\]

Thus (2.8) bounds the actual path-reset burden simultaneously at every
depth; no histogram converse is being used.

---

## 3. Exact recursive Hall characterization of admissibility

Fix a spanning directed subforest \(D\subseteq G\). The following theorem
decides its admissibility using only integral partial matchings.

At level \(h\), put

\[
D_h=D[X_{h+1}],
\qquad
\kappa_h=c(D_h).
\tag{3.1}
\]

Assume \(L_h,R_h\) have already been defined. For an edge
\(e=v\to w\in D_h\), define its forced targets

\[
\lambda_h(e)=L_h(v)\cap L_h(w),
\tag{3.2}
\]

\[
\rho_h(e)=R_h(v)\cap R_h(w).
\tag{3.3}
\]

Let \(T_h^-\) be the terminal owners of \(D_h\), and let \(T_h^+\) be its
source owners. Both sets have size \(\kappa_h\).

### Theorem 3.1 (recursive boundary-Hall theorem)

The fixed forest \(D\) is dynamically admissible if and only if one can
iterate the following two independent tests for every
\(0\le h<H\).

**Lower test.**

1. Every \(\lambda_h(e)\) has rank \(m-h-1\), is a facet of \(L_h(v)\),
   and the targets \(\lambda_h(e)\), over all \(e\in E(D_h)\), are
   pairwise distinct.
2. Let
   \[
   Y_h^-=
   \binom{[2m]}{m-h-1}
   \setminus\{\lambda_h(e):e\in E(D_h)\}.
   \tag{3.4}
   \]
   The balanced boundary graph between \(T_h^-\) and \(Y_h^-\), with
   \[
   v\sim S\quad\Longleftrightarrow\quad S\subset L_h(v),
   \tag{3.5}
   \]
   satisfies Hall:
   \[
   \boxed{
   |\{v\in T_h^-:S\subset L_h(v)
       \text{ for some }S\in\mathcal A\}|
   \ge|\mathcal A|
   \quad(\mathcal A\subseteq Y_h^-).}
   \tag{3.6}
   \]

**Upper-complement test.**

1. Every \(\rho_h(e)\) has rank \(m-h-1\), is a facet of \(R_h(w)\),
   and the targets \(\rho_h(e)\) are pairwise distinct.
2. Let
   \[
   Y_h^+=
   \binom{[2m]}{m-h-1}
   \setminus\{\rho_h(e):e\in E(D_h)\}.
   \tag{3.7}
   \]
   The balanced boundary graph between \(T_h^+\) and \(Y_h^+\), with
   \[
   v\sim S\quad\Longleftrightarrow\quad S\subset R_h(v),
   \tag{3.8}
   \]
   satisfies the analogous Hall inequalities.

When the tests pass, assign every nonterminal lower owner its forced target
\(\lambda_h(e)\), match the terminals to \(Y_h^-\), assign every
nonsource upper-complement owner its forced target \(\rho_h(e)\), and match
the sources to \(Y_h^+\). These choices define \(L_{h+1},R_{h+1}\).

#### Proof

Suppose first that \(D\) is admissible. Every nonterminal \(v\) is the tail
of a unique edge \(e=v\to w\), and durability forces

\[
L_{h+1}(v)=\lambda_h(e).
\]

Since \(L_{h+1}\) is a bijection, the forced targets are valid and
pairwise distinct. Exactly

\[
|X_{h+1}|-|E(D_h)|=\kappa_h
\]

rank-\((m-h-1)\) targets remain unused, and the unforced owners are exactly
the \(\kappa_h\) terminals. The restriction of \(L_{h+1}\) to these
owners is a perfect matching in (3.5), so Hall holds. This proves necessity
of the lower test. The upper identities force targets at the heads of
edges, leaving precisely the sources free, and give the upper test.

Conversely, assume both tests pass. Hall gives literal integral perfect
matchings on the two boundary graphs. Together with the forced assignments
they define bijections

\[
L_{h+1},R_{h+1}:X_{h+1}
\longrightarrow\binom{[2m]}{m-h-1}.
\]

Every assigned target is a facet of its current endpoint, so nesting holds.
Every edge of \(D_h\) satisfies (2.2)--(2.3) at level \(h\). Starting from

\[
L_0(v)=v,\qquad R_0(v)=[2m]\setminus v,
\]

iteration through \(h=0,\ldots,H-1\) constructs two active flag systems
and makes every edge of \(D\) durable through its common lifetime.
\(\square\)

### Corollary 3.2 (exact positive optimization)

Let \(\mathscr D\) be the set of spanning subforests \(D\subseteq G\) for
which the recursive tests of Theorem 3.1 can be passed. Assume both active
flag families are nonempty. Then

\[
\boxed{
K_H^{\min}
=\min_{D\in\mathscr D}\bigl(c(D)-b_0\bigr).}
\tag{3.9}
\]

In particular, the sought constant-one estimate follows from the genuinely
positive statement

\[
\boxed{
\min_{D\in\mathscr D}c(D)=o(W/H).}
\tag{3.10}
\]

Theorem 3.1 is stronger than rankwise support and weaker than prescribing
all flags in advance. It exposes exactly where a positive proof can act:
choose one large path forest whose forced colours are injective and whose
small terminal/source boundary graphs have perfect matchings at every
level.

### Corollary 3.3 (fractional boundary certificate)

At any fixed level, the relevant boundary Hall condition follows if its
balanced bipartite graph supports nonnegative weights for which every
boundary owner and every missing target has weighted degree \(1\).

#### Proof

Such weights are a fractional perfect matching. The bipartite matching
polytope is integral, so the graph has an integral perfect matching.
\(\square\)

This use of fractional weights is safe: it certifies an integral matching
inside the one already fixed forest and flag history. It is not a
fractional averaging argument across different SCDs or exact factors.

### Corollary 3.4 (boundary-regular positive theorem)

Suppose there is a spanning \(D\subseteq G\) with

\[
c(D)=o(W/H)
\]

with the following robust property: after **every** partial sequence of
lower and upper boundary matchings allowed by Theorem 3.1, at the next
recursive level and on both signs,

1. all forced targets in Theorem 3.1 are valid and pairwise distinct;
2. each balanced terminal/source boundary graph is positive-degree
   biregular.

Then \(D\) is dynamically admissible and the constant-one recursive gate
holds.

#### Proof

Every positive-degree balanced biregular bipartite graph supports the
constant fractional perfect matching which assigns the reciprocal of its
left degree to every edge. Corollary 3.3 integralizes it. The robust
quantifier makes the same assertion available after the chosen matching,
so induction iterates through all \(H\) levels. Corollary 2.2 gives
\(K_H^{\min}=o(W/H)\). \(\square\)

More generally, "biregular" may be replaced by an explicitly supplied
doubly stochastic boundary weighting with the same robust quantifier. A
merely layerwise existence statement is insufficient because a matching
chosen now changes the endpoint flags and hence the next boundary graph.

### Theorem 3.5 (recursive rainbow cycle closure)

Fix a spanning \(D\subseteq G\). Suppose there is one recursively
consistent sequence with the following property at every
\(0\le h<H\). Starting from the already constructed \(L_h,R_h\), augment

\[
D_h=D[X_{h+1}]
\]

by exactly one directed closure arc out of every terminal and one into
every source, so that

\[
\overline D_h
\]

is a directed cycle cover of \(X_{h+1}\). Require every closure arc, and
hence every arc \(e=v\to w\) of \(\overline D_h\), to have valid forced
facets

\[
\lambda_h(e)=L_h(v)\cap L_h(w),
\qquad
\rho_h(e)=R_h(v)\cap R_h(w),
\tag{3.11}
\]

and require the two colour maps

\[
e\longmapsto\lambda_h(e),
\qquad
e\longmapsto\rho_h(e)
\tag{3.12}
\]

to be injective.

Then \(D\) is dynamically admissible. In particular, if

\[
c(D)=o(W/H),
\tag{3.13}
\]

the recursive constant-one gate holds.

#### Proof

The cycle cover has \(|X_{h+1}|=N_{h+1}\) arcs. There are exactly
\(N_{h+1}\) targets of rank \(m-h-1\). Hence each injective colour map in
(3.12) is a bijection onto the full target rank.

Assign to every tail \(v\) the lower colour of its unique outgoing cover
arc, and assign to every head \(w\) the upper-complement colour of its
unique incoming cover arc. These assignments define bijections
\(L_{h+1},R_{h+1}\), are nested by validity of (3.11), and force every arc
of \(D_h\) to satisfy the two durable identities at level \(h\).
Iterating the assumed recursively consistent closures proves
admissibility. Corollary 2.2 gives the last assertion. \(\square\)

The closure arcs are boundary certificates; they need not be retained in
the fixed forest \(D\). Theorem 3.5 is therefore a useful target for exact
wreath data: close the few durable path components into a two-sided-rainbow
cycle cover at every layer. At \(h=0\), this exposes the current sharp
limitation of the odd-cut input: its join ledger is controlled, but the
complete meet-rainbow ledger required by (3.12) is not proved.

---

## 4. Radius-homogeneous fully durable graphs

Now start with one exact integral depth-\(H\) band SCD, equivalently one
pair of active flag systems. Let

\[
V_r=\{v:\tau(v)=r\}
\qquad(0\le r\le H).
\tag{4.1}
\]

Thus

\[
|V_r|=N_r-N_{r+1}\quad(0\le r<H),
\qquad |V_H|=N_H.
\tag{4.2}
\]

For \(1\le r\le H\) and distinct \(v,w\in V_r\), write

\[
v\Rightarrow_r w
\]

when, for every \(0\le h<r\),

\[
L_{h+1}(v)=L_h(v)\cap L_h(w),
\tag{4.3}
\]

\[
R_{h+1}(w)=R_h(v)\cap R_h(w).
\tag{4.4}
\]

Let \(\mathcal D_r\) be this directed graph on \(V_r\). Every one of its
arcs is a literal rotor transition between the complete radius-\(r\)
states of the two SCD chains.

There is an equivalent purely Boolean form:

\[
L_{h+1}(v)\subset L_h(w),
\qquad
R_{h+1}(w)\subset R_h(v)
\quad(0\le h<r).
\tag{4.5}
\]

Indeed, the reverse containments into \(L_h(v)\) and \(R_h(w)\) already
follow from flag nesting. The rank-\((m-h)\) endpoints belonging to
distinct owners are distinct by bijectivity. If two distinct sets of that
rank contain the same rank-\((m-h-1)\) set, their intersection is exactly
that common facet. This proves equivalence of (4.3)--(4.5).

Let \(\operatorname{pc}(\mathcal D_r)\) denote the minimum number of
components in a spanning vertex-disjoint directed path forest of
\(\mathcal D_r\), with isolated vertices allowed.

For a total order \(\prec\) on \(V_r\), let
\(\mathcal D_{r,\prec}\) contain only forward arcs \(v\Rightarrow_r w\)
with \(v\prec w\). Split its vertices into an out-copy and an in-copy, and
put

\[
\delta_r(\prec)
=\max_{S\subseteq V_r}
\left(|S|-|N^+_{\mathcal D_{r,\prec}}(S)|\right).
\tag{4.6}
\]

The empty set is allowed in the maximum.

### Theorem 4.1 (Hall--acyclic path-cover min--max)

For every \(1\le r\le H\),

\[
\boxed{
\operatorname{pc}(\mathcal D_r)
=\min_{\prec}\delta_r(\prec).}
\tag{4.7}
\]

#### Proof

Fix \(\prec\). Hall's deficiency theorem says that a maximum matching in
the split bipartite graph has

\[
|V_r|-\delta_r(\prec)
\]

edges. Interpreted as directed arcs on \(V_r\), a matching has indegree and
outdegree at most one. Every arc is forward in \(\prec\), so there is no
directed cycle. The matching arcs therefore form a spanning directed path
forest with exactly

\[
|V_r|-\bigl(|V_r|-\delta_r(\prec)\bigr)
=\delta_r(\prec)
\]

components. This proves
\(\operatorname{pc}(\mathcal D_r)\le\min_\prec\delta_r(\prec)\).

Conversely, let a spanning directed path forest have \(q\) components.
Choose a total order which lists every path in its directed order, with
the paths placed arbitrarily relative to one another. Its
\(|V_r|-q\) arcs form a matching in the corresponding forward split graph.
Hence the maximum matching there has size at least \(|V_r|-q\), so
\(\delta_r(\prec)\le q\). Minimize first over orders and then over path
forests. \(\square\)

This theorem includes acyclicity exactly. An unrestricted split-graph
matching can contain directed cycles and is not by itself a path forest.

### Theorem 4.2 (exact positive RSCD theorem)

For each \(1\le r\le H\), choose a minimum-component spanning directed
path forest of \(\mathcal D_r\). The union of these forests is integral,
uses only chains of the one fixed band SCD, and has exact hard-prefix toll

\[
\boxed{
\widehat\Phi_H
=2\sum_{r=1}^H r\,\operatorname{pc}(\mathcal D_r).}
\tag{4.8}
\]

Equivalently, the literal central-band word obtained by independently
initializing these rotor paths has exact augmented-prefix length

\[
\boxed{
L_{\rm band}
=W+2\sum_{r=1}^H r\,\operatorname{pc}(\mathcal D_r).}
\tag{4.9}
\]

#### Proof

All vertices in one selected path have the same lifetime \(r\), and every
arc satisfies (4.3)--(4.4) through all \(r\) layers. It is therefore a
genuine directed rotor path of complete radius-\(r\) chain states.

A rotor path with \(s\) states has augmented-prefix length \(s+2r\): its
first state costs \(2r+1\) useful blocks and every later state one core
block. Summing the \(s\)-terms over all paths and all radii gives one per
SCD chain, hence \(W\); summing the reset terms gives (4.9). Subtracting
the baseline \(W\) gives (4.8). Radius-zero chains contribute no reset
toll. \(\square\)

### Corollary 4.3 (constant-one quantitative condition)

Either

\[
\sum_{r=1}^H r\,\operatorname{pc}(\mathcal D_r)=o(W)
\tag{4.10}
\]

or the stronger condition

\[
\sum_{r=1}^H\operatorname{pc}(\mathcal D_r)=o(W/H)
\tag{4.11}
\]

gives \(\widehat\Phi_H=o(W)\) for this exact band SCD. The established
band-extension theorem preserves every band chain and rotor edge while
completing it to one full integral SCD. The accepted literal outer-tail
construction then gives constant one if the condition is achieved for
every fixed \(A\), followed by the usual \(A\to\infty\) diagonalization.

No selected state, arc, path, or SCD in this implication is fractional.

---

## 5. Checkable positive sufficient conditions

The Hall deficiency in Theorem 4.1 can be controlled without collapsing
labelled arcs into coordinate histograms.

### Theorem 5.1 (bounded-congestion durable extension)

Fix \(r\) and a total order \(\prec_r\) on \(V_r\). Suppose there are an
integer \(d_r\ge1\) and an exceptional source set
\(B_r\subseteq V_r\), \(|B_r|=b_r\), such that in the forward durable
split graph:

1. every left vertex in \(V_r\setminus B_r\) has outdegree at least
   \(d_r\);
2. every right vertex has indegree at most \(d_r\).

Then

\[
\boxed{
\delta_r(\prec_r)\le b_r,
\qquad
\operatorname{pc}(\mathcal D_r)\le b_r.}
\tag{5.1}
\]

#### Proof

For \(S\subseteq V_r\), count actual forward durable arcs from
\(S\setminus B_r\) to its neighborhood:

\[
d_r(|S|-b_r)
\le d_r|S\setminus B_r|
\le e(S,N^+(S))
\le d_r|N^+(S)|.
\]

When \(|S|<b_r\), the desired inequality is trivial; otherwise division
by \(d_r\) gives

\[
|N^+(S)|\ge|S|-b_r.
\]

Thus every Hall deficiency is at most \(b_r\). Apply Theorem 4.1.
\(\square\)

The hypotheses concern simultaneous Boolean extensions (4.5), not
separate lower and upper degrees and not same-coordinate histogram mass.

### Corollary 5.2 (positive bounded-congestion criterion)

If one exact band SCD admits orders and data as in Theorem 5.1 with

\[
\sum_{r=1}^H b_r=o(W/H),
\tag{5.2}
\]

then it satisfies \(\mathrm{RSCD}_A\), and the accepted tail implication
gives constant one when this holds for every fixed \(A\).

### Theorem 5.3 (joint durable fractional transport)

Fix \(r\), an order \(\prec_r\), and a nonnegative integer \(b_r\). Suppose
the forward durable split graph
supports nonnegative edge weights \(x_e\) satisfying

\[
\sum_{e\ni v_{\rm out}}x_e\le1,
\qquad
\sum_{e\ni w_{\rm in}}x_e\le1,
\tag{5.3}
\]

and

\[
\sum_e x_e\ge |V_r|-b_r.
\tag{5.4}
\]

Then

\[
\boxed{\operatorname{pc}(\mathcal D_r)\le b_r.}
\tag{5.5}
\]

#### Proof

Equations (5.3) define a fractional matching in a bipartite graph.
Integrality of the bipartite matching polytope gives an integral matching
of size at least \(|V_r|-b_r\), supported on the same actual forward
durable arcs. Forwardness makes it acyclic, so it is a path forest with at
most \(b_r\) components after isolated vertices are included. \(\square\)

This is the only safe fractional bridge in this report. The weights already
live on literal jointly durable arcs of one fixed integral SCD. Exact
state marginals or separate-depth fractional covers do not provide
(5.3)--(5.4).

### Proposition 5.4 (durable cycle/path cover)

Suppose a matching in the unrestricted split graph of \(\mathcal D_r\)
has \(|V_r|-b_r\) arcs and, when interpreted on \(V_r\), has \(q_r\)
directed cycle components. Then

\[
\boxed{\operatorname{pc}(\mathcal D_r)\le b_r+q_r.}
\tag{5.6}
\]

In particular, a spanning durable directed cycle cover with \(q_r\)
cycles gives a spanning path forest with \(q_r\) components.

#### Proof

A directed graph arising from a split matching is a disjoint union of
directed paths, directed cycles, and isolated vertices. Since it has
\(|V_r|-b_r\) arcs, it has exactly \(b_r\) path components, with isolated
vertices counted as paths. Delete one arc from each of its \(q_r\) cycles.
The result is a spanning directed path forest with \(b_r+q_r\) components.
\(\square\)

Thus a positive cyclic theorem would also suffice:

\[
\sum_{r=1}^H(b_r+q_r)=o(W/H).
\tag{5.7}
\]

This formulation is tailored to exact wreath data, but it still requires
the cycle arcs to be fully durable in one exact SCD. An uncoloured or
pseudo-coloured cycle cover is not enough.

### Theorem 5.5 (port-disjoint durable cycle fusion)

Fix \(r\), and suppose \(\mathcal C_r\) is a spanning directed cycle cover
using arcs of \(\mathcal D_r\). For two distinct cover cycles, choose cover
arcs

\[
a\to a',
\qquad
b\to b'.
\]

Call these two arcs a legal switch port when both cross arcs

\[
a\to b',
\qquad
b\to a'
\tag{5.8}
\]

also belong to \(\mathcal D_r\). Replacing the two cover arcs by the two
cross arcs merges the two directed cycles.

Suppose there is a family of legal switch ports such that:

1. no cover arc is used by two switches;
2. the multigraph whose vertices are the original cover cycles and whose
   edges are the chosen switches is a spanning forest, in the multigraph
   sense, with \(s_r\) components.

Then

\[
\boxed{\operatorname{pc}(\mathcal D_r)\le s_r.}
\tag{5.9}
\]

#### Proof

Consider one tree of the cycle-incidence forest. Choose a leaf cycle and
apply its unique incident switch. The two exchanged cover arcs merge the
leaf cycle with its neighboring cycle into one directed cycle. Because all
switch ports are cover-edge-disjoint, every port reserved for a remaining
tree edge is still present on the merged cycle. Contract the leaf edge and
iterate. The whole tree becomes one directed cycle. Perform this operation
independently in all \(s_r\) trees, obtaining a spanning durable cycle
cover with \(s_r\) cycles. Delete one arc from each cycle. \(\square\)

Consequently, if one exact band SCD has durable cycle covers with
port-disjoint switch forests satisfying

\[
\sum_{r=1}^H s_r=o(W/H),
\tag{5.10}
\]

then it proves \(\mathrm{RSCD}_A\). A connected switch tree in every
positive radius would give only \(H\) total components, which is
\(o(W/H)\) because \(W\) is exponential and \(H=O_A(\sqrt m)\).

As an abstract digraph theorem this identifies a possible cycle-fusion
mechanism. The next proposition shows that the particular reciprocal
two-edge mechanism cannot occur for distinct Boolean durable cycles.

### Proposition 5.6 (Boolean no-two-switch theorem)

In an exact Boolean endpoint-flag system at any positive radius, no two
vertex-disjoint durable cover arcs admit the reciprocal switch (5.8).
Equivalently, the split bipartite graph of every positive-radius fully
durable graph is \(C_4\)-free.

#### Proof

For an owner \(x\), let \(d(x)\) be the unique element of
\(x\setminus L_1(x)\). For an owner \(y\), write
\[
U_1(y)=[2m]\setminus R_1(y)
\]
and let \(u(y)\) be the unique element of \(U_1(y)\setminus y\).
Every durable arc \(x\to y\) satisfies
\[
d(x)=u(y)=x\setminus y.
\tag{5.11}
\]

Suppose \(a\to a'\), \(b\to b'\), \(a\to b'\), and \(b\to a'\) were all
durable, with distinct sources and distinct targets. Equation (5.11)
forces
\[
d(a)=d(b)=u(a')=u(b')=:c.
\]
Put
\[
S=a-\{c\},\qquad T=b-\{c\}.
\]
Both targets \(a',b'\) contain \(S\cup T\) and omit \(c\). If \(S=T\),
then \(a=b\). If \(S\ne T\), the existence of an \(m\)-set containing
both rank-\((m-1)\) sets forces \(|S\cup T|=m\), so that containing
\(m\)-set is unique and \(a'=b'\). Both alternatives contradict
vertex-disjointness. \(\square\)

Therefore Theorem 5.5 is a formally correct digraph theorem but its
two-edge switch premise is Boolean-vacuous for distinct durable cycles.
Actual Boolean cycle fusion must instead use one-way path splices or
alternating trades of length at least six. No pairwise necklace-switch
argument can instantiate (5.10).

---

## 6. Precise boundary

### Proved

1. The stopped-thread law is the exact source/terminal restitution identity
   (1.6); its norm bound measures the literal survivor component count.
2. The dynamic defect satisfies the exact positive forest identity (2.4).
   For global suffix lifetimes, \(K_H^{\min}=o(W/H)\) is equivalent to one
   admissible spanning durable forest with \(o(W/H)\) components.
3. Theorem 3.1 gives necessary and sufficient integral recursive Hall tests
   for a fixed candidate forest.
4. The Hall--acyclic min--max (4.7) gives the exact path-cover number of
   each fully durable radius graph in one band SCD.
5. The exact literal toll is (4.8)--(4.9).
6. Bounded congestion on actual durable arcs, a joint durable fractional
   matching, or a durable cycle cover with the totals in Section 5 gives
   the required \(o(W/H)\) components. The abstract two-switch theorem is
   Boolean-vacuous by Proposition 5.6; one-way splicing or longer
   alternating trades are required.

### Unproved

No present argument constructs the required SCD or dynamic forest.
Specifically unproved is either one of the following positive assertions:

\[
\min_{D\in\mathscr D}c(D)=o(W/H),
\tag{6.1}
\]

for the recursive boundary-Hall family \(\mathscr D\), or

\[
\sum_{r=1}^H\operatorname{pc}(\mathcal D_r)=o(W/H)
\tag{6.2}
\]

for the fully durable radius graphs of one exact band SCD.

AD7's proved support-surjective owner construction does not furnish the
active bijections required in (6.1). Its proved variation and trace
estimates project away labelled arcs and therefore do not establish
(6.2). The standard product SCD and
uncoupled state-marginal resolutions are already obstructed by the audited
indegree-zero and recolouring no-go theorems.

The surviving target is now positive and literal: construct many actual
joint Boolean extensions (4.5), with small Hall deficiency after an
acyclic ordering, or construct one large candidate subforest which passes
the two boundary Hall systems at every layer.

No coefficient-one theorem is claimed until one of (6.1)--(6.2) is
proved.

---

## 7. Audit record

The restitution identity was derived independently from the actual
maximal-retention survivor forest. The sign of \(S_j\), the level range
\(1\le j<H\), and the source/terminal orientations were checked by direct
edge cancellation.

The dynamic component identity was checked independently against

\[
K_H^{\min}
=|E^\circ|-\max|E^{\rm dur}|,
\qquad
|E^\circ|=N_1-b_0.
\]

The recursive Hall theorem was audited in both directions: nonterminal
tails and nonsource heads are exactly the forced owners; terminals and
sources are exactly the free owners; both free shores have cardinality
equal to the actual component count.

Finally, the path-cover min--max was proved in both directions. Forward
matching arcs are acyclic, while every directed path forest supplies its
own topological order. This explicitly closes the cycle loophole in an
ordinary split-graph matching.
