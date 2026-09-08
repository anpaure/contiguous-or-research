# Second-wave B: endpoint cuts for the \(k=11\) middle-level path cover

Date: 2026-07-24

## 1. Outcome

Let

\[
\mathcal L=\binom{[11]}5,\qquad
\mathcal R=\binom{[11]}6,
\]

and let \(G\) be the inclusion graph between these two layers.  The
zero-margin normal form supplies a perfect inclusion matching \(M\) and,
together with \(M\), a cover of all \(924\) vertices by
\(c\in\{1,\ldots,6\}\) alternating paths.  Each path begins in
\(\mathcal L\) and ends in \(\mathcal R\).

No contradiction follows from endpoint cuts, aggregate coordinate parity,
or ordinary bipartite isoperimetry alone.  The attack nevertheless gives a
strict exact reduction.

1. After contracting \(M\), the nonmatching edges are a bijection in a
   directed \(5\)-regular Johnson subgraph.  The initial and terminal
   endpoint sets satisfy exact Hall cuts and a stronger acyclic escape cut.
2. Any non-singleton potential endpoint obstruction not already excluded by
   the local contracted-neighborhood estimates has at least \(18\) sources;
   any non-singleton potential closed trap has at least \(17\) sources.
3. In the full middle-level graph,
   \[
   |\Gamma_G(\mathcal X)|
   \ge\min\{|\mathcal X|+5,462\}
   \qquad(\varnothing\ne\mathcal X\subseteq\mathcal L),
   \]
   with a complete equality classification.  Consequently deletion of at
   most five prescribed endpoints on each side always leaves a perfect
   matching; six deletions fail only through one of two isolated full-star
   obstructions.
4. For \(K:=G\setminus M\), every connected component has at least \(43\)
   vertices on each side.  Its Johnson edge count and all eleven coordinate
   loads satisfy exact divisibility identities.
5. Every aggregate coordinate-parity equation, including arbitrary
   coordinate parity cylinders, is already the sum of the identities
   (3.20)--(3.24).  A stronger parity argument must control correlations
   between the entering and leaving labels of the same Johnson transition.

The abstract package is genuinely realizable: cut one nonmatching edge from
an alternating Hamilton cycle of the middle-level graph.  Thus the remaining
lemma must be \(M\)-dependent and order-sensitive.  A precise minimal target
is stated in Section 9.

No finite search, numerical enumeration, or web source is used below.

## 2. Exact contracted model

Let \(A\subseteq\mathcal L\) be the \(c\) initial five-set endpoints and
let \(B\subseteq\mathcal R\) be the \(c\) terminal six-set endpoints.
Write

\[
\Sigma=M^{-1}(B)\subseteq\mathcal L
\]

for the five-set roots whose matching edges are terminal.  Thus

\[
|A|=|B|=|\Sigma|=c.
\]

The non-\(M\) edges form a matching

\[
N:\mathcal L\setminus A\longrightarrow\mathcal R\setminus B.
\tag{2.1}
\]

Write \(\mathscr P=M\cup N\) for the expanded path-cover edge set.

There is a more useful rootward contraction.  For \(S\in\mathcal L\), put

\[
\Gamma_M^+(S)
=
\left\{T\in\mathcal L:
T\ne S,\ T\subset M(S)\right\}.
\tag{2.2}
\]

This set has size five.  If \(S\notin\Sigma\), follow the matching edge
\(S\,M(S)\) and then the nonmatching edge out of \(M(S)\).  Its lower
endpoint is a unique

\[
\pi(S)\in\Gamma_M^+(S).
\]

Every lower vertex outside \(A\) has exactly one nonmatching predecessor.
Therefore

\[
\boxed{
\pi:\mathcal L\setminus\Sigma
\longrightarrow
\mathcal L\setminus A
\text{ is a bijection.}}
\tag{2.3}
\]

Its directed graph is exactly the disjoint union of the \(c\) contracted
paths, each directed from its member of \(A\) to its member of \(\Sigma\).
Singleton contracted components are allowed: they expand to one matching
edge.

For later use define the reverse candidate set

\[
\Gamma_M^-(T)
=
\{S\in\mathcal L:S\ne T,\ T\subset M(S)\}.
\tag{2.4}
\]

It also has size five.

## 3. Exact endpoint Hall and escape cuts

### Theorem 3.1 (prescribed-matching endpoint cuts)

For every \(X\subseteq\mathcal L\setminus\Sigma\),

\[
\boxed{
|\Gamma_M^+(X)\setminus A|\ge |X|.}
\tag{3.1}
\]

Dually, for every \(Y\subseteq\mathcal L\setminus A\),

\[
\boxed{
|\Gamma_M^-(Y)\setminus\Sigma|\ge |Y|.}
\tag{3.2}
\]

Acyclicity gives the stronger escape condition

\[
\boxed{
\varnothing\ne X\subseteq\mathcal L\setminus\Sigma
\Longrightarrow
\bigl(\Gamma_M^+(X)\setminus A\bigr)\setminus X
\ne\varnothing.}
\tag{3.3}
\]

The reverse escape statement holds with
\((A,\Gamma_M^+)\) and \((\Sigma,\Gamma_M^-)\) interchanged.

#### Proof

Equation (3.1) is Hall's inequality for the restriction of the bijection
\(\pi\) in (2.3); (3.2) is the same assertion for \(\pi^{-1}\).

For (3.3), suppose instead that
\(\Gamma_M^+(X)\setminus A\subseteq X\).  Then
\(\pi(X)\subseteq X\).  Since \(\pi\) is injective and \(X\) is finite,
\(\pi|_X\) is a permutation of \(X\), so it contains a directed cycle.
This contradicts the fact that the contracted graph is a union of paths.
\(\square\)

### Corollary 3.2 (five-neighbour pins)

If \(S\notin\Sigma\), then

\[
|A\cap\Gamma_M^+(S)|\le4.
\tag{3.4}
\]

If four of the five alternatives lie in \(A\), the fifth is the forced value
of \(\pi(S)\).  If all five lie in \(A\), then necessarily
\(S\in\Sigma\), equivalently \(M(S)\in B\).

Dually, if \(T\notin A\), at most four of its five alternative
non-\(M\) cofacets can lie in \(B\); four pins its predecessor and five
force \(T\in A\).

There is one useful singleton consequence.  Suppose \(c=6\), let
\(U\in\mathcal R\), and suppose \(A\) is the set of all six facets of
\(U\).  Put \(S=M^{-1}(U)\).  The other five facets of \(U=M(S)\) all
belong to \(A\), so \(S\in\Sigma\) and \(U\in B\).  Since also
\(S\in A\), the contracted vertex \(S\) has neither predecessor nor
successor.  Hence

\[
\boxed{S-M(S)=S-U
\text{ is a singleton alternating-path component.}}
\tag{3.5}
\]

Merely pinning the five alternative facets forces terminality; the sixth
facet \(S\in A\) is what forces a singleton component.

## 4. Small-set isoperimetry relative to \(M\)

The endpoint cuts in Section 3 are local only if small sets can have small
candidate neighborhoods.  They cannot.

For distinct \(S,T\in\mathcal L\),

\[
|\Gamma_M^+(S)\cap\Gamma_M^+(T)|\le1.
\tag{4.1}
\]

Indeed, the distinct six-sets \(M(S),M(T)\) have at most one common
five-set facet.

Let \(X\subseteq\mathcal L\), \(t=|X|\), and

\[
u=|\Gamma_M^+(X)|.
\]

For a target \(V\), let \(r_V\) be the number of source neighborhoods
containing it.  The intersection graph of the \(t\) neighborhoods is
\(K_8\)-free.  To see this, a clique maps to pairwise Johnson-adjacent
six-sets \(M(S)\).  A clique in \(J(11,6)\) has size at most seven:
relative to one fixed six-set, an adjacent six-set replaces a pair
\((a,b)\) with \(a\) inside and \(b\) outside; pairwise adjacency forces
all replacement pairs to share \(a\), or all to share \(b\).  Including
the fixed set gives clique sizes at most six and seven respectively.

Turán's theorem and (4.1) give

\[
\sum_V\binom{r_V}{2}
\le\frac{3t^2}{7}.
\tag{4.2}
\]

Since \(\sum_Vr_V=5t\),

\[
\sum_Vr_V^2
=5t+2\sum_V\binom{r_V}{2}
\le5t+\frac{6t^2}{7}.
\]

Cauchy--Schwarz now yields

\[
(5t)^2
\le
u\sum_Vr_V^2,
\]

and hence

\[
\boxed{
u\ge
\left\lceil\frac{175t}{35+6t}\right\rceil.}
\tag{4.3}
\]

### Theorem 4.1 (first possible nonlocal cuts)

Let \(A\subseteq\mathcal L\) with \(|A|=c\le6\).  For every
non-singleton \(X\subseteq\mathcal L\),

\[
\boxed{
\begin{aligned}
|\Gamma_M^+(X)\setminus A|<|X|
&\Longrightarrow |X|\ge18,\\
\Gamma_M^+(X)\setminus A\subseteq X
&\Longrightarrow |X|\ge17.
\end{aligned}}
\tag{4.4}
\]

#### Hall-cut proof

If the first hypothesis in (4.4) holds, then

\[
u\le |X|-1+|A|\le t+5.
\tag{4.5}
\]

For \(2\le t\le16\), (4.3) gives \(u\ge t+6\).  This follows directly
from

\[
\frac{175t}{35+6t}>t+5.
\]

It remains to exclude \(t=17\).  If \(u\le22\), the \(85\) incidences
distributed over at most \(22\) targets give, by convexity,

\[
\sum_V\binom{r_V}{2}
\ge19\binom42+3\binom32=123.
\tag{4.6}
\]

If the neighborhood-intersection graph is \(K_7\)-free, the sharp
\(K_7\)-free Turán bound on \(17\) vertices is \(120\).  If it contains a
\(K_7\), the corresponding six-sets are the seven facets of one seven-set.
Every other six-set is adjacent to at most two of those facets, so even
allowing all edges among the ten remaining vertices gives at most

\[
\binom72+2\cdot10+\binom{10}2=86
\]

intersection edges.  Both alternatives contradict (4.6).  Therefore
\(u\ge23\), excluding the first obstruction in (4.4) at \(t=17\).

#### Escape-cut proof

If the second hypothesis in (4.4) holds, then

\[
\Gamma_M^+(X)\subseteq X\cup A,
\qquad
u\le t+6.
\tag{4.7}
\]

For \(t=2\), (4.1) gives \(u\ge9=t+7\).  For \(3\le t\le14\),
(4.3) gives \(u\ge t+7\).

If \(t=15\) and \(u\le21\), the \(75\) incidences give at least

\[
12\binom42+9\binom32=99
\]

intersecting pairs, while the \(K_8\)-free Turán maximum on \(15\)
vertices is \(96\).

If \(t=16\) and \(u\le22\), the \(80\) incidences give at least

\[
14\binom42+8\binom32=108
\]

intersecting pairs.  A \(K_7\)-free graph on \(16\) vertices has at most
\(106\) edges.  If a \(K_7\) occurs, the remaining nine vertices have at
most two neighbors each in it, so the total is at most

\[
\binom72+2\cdot9+\binom92=75.
\]

Both cases are impossible.  Thus \(u\ge t+7\) also for \(t=15,16\),
proving (4.4).

The theorem is only a lower bound on the first possible obstruction.  It
does not assert that cuts of sizes \(17\) or \(18\) exist.

The same multiplicity and Turán proof applies to the five non-\(M\)
upper neighbors
\(\Gamma_K(S)=\Gamma_G(S)\setminus\{M(S)\}\), and dually on the upper
side, with \(J(11,5)\) replacing \(J(11,6)\) in the clique argument.
Hence a non-singleton potential Hall obstruction to selecting a matching
\(N\subseteq K\) likewise needs at least \(18\) source vertices.  For the
assumed path cover the actual \(N\) already exists, so its Hall inequalities
hold; this sentence records the first obstruction size not ruled out by the
local estimates, not an obstruction present in the cover.

## 5. Sharp ordinary middle-level isoperimetry

The preceding theorem depends on \(M\).  The corresponding theorem in the
full inclusion graph is sharp and completely classifiable.

### Lemma 5.1 (small-half shadow surplus)

Let
\(\mathcal F\subseteq\binom{[11]}6\) with
\(1\le t:=|\mathcal F|\le231\).  Then

\[
|\partial\mathcal F|\ge t+5,
\tag{5.1}
\]

with equality only for \(t=1\).

#### Proof

By Kruskal--Katona compression, the lower shadow is minimized by the initial
colex segment \(\mathcal C_t\).  We bound its shadow in four ranges.

For \(t=1\), the shadow has size six.  For \(2\le t\le9\), two distinct
six-sets have at most one common facet, so

\[
|\partial\mathcal F|
\ge6t-\binom t2
>t+5.
\tag{5.2}
\]

For \(10\le t\le24\), the colex segment lies in
\(\binom{[8]}6\).  Each five-set in its shadow belongs to at most three
six-sets on \([8]\), so incidence counting gives

\[
|\partial\mathcal C_t|\ge2t>t+5.
\tag{5.3}
\]

For \(25\le t\le210\), the colex segment lies in
\(\binom{[10]}6\).  Each shadow five-set belongs to at most five six-sets
on \([10]\), and therefore

\[
|\partial\mathcal C_t|
\ge\frac65t\ge t+5.
\tag{5.4}
\]

Equality in (5.4) and (5.1) could occur only at \(t=25\), with every
shadow facet having all five possible extensions in the family.  Starting
from one member, this condition closes the family under every Johnson swap
in \(J(10,6)\).  That graph is connected, so the family would be all
\(\binom{[10]}6\), of size \(210\), a contradiction.

Finally, for \(211\le t\le231\), the colex segment contains all
\(\binom{[10]}6\), and its shadow therefore contains all
\(\binom{[10]}5\), giving

\[
|\partial\mathcal C_t|\ge252>t+5.
\]

This proves the lemma and its equality statement. \(\square\)

### Theorem 5.2 (sharp full-graph endpoint expansion)

For every nonempty \(\mathcal X\subseteq\mathcal L\),

\[
\boxed{
|\Gamma_G(\mathcal X)|
\ge\min\{|\mathcal X|+5,462\}.}
\tag{5.5}
\]

More precisely:

* for \(1\le|\mathcal X|\le456\), equality in the nonsaturated bound occurs
  only when \(|\mathcal X|=1\), or when
  \[
  |\mathcal X|=456,\qquad
  \mathcal L\setminus\mathcal X
  =\binom{U}{5}
  \]
  for one \(U\in\mathcal R\);
* every family of size at least \(457\) has full upper shadow.

#### Proof

Complement every member of \(\mathcal X\).  This gives a six-uniform family
\(\overline{\mathcal X}\) of the same size, and

\[
|\Gamma_G(\mathcal X)|
=|\partial\overline{\mathcal X}|.
\tag{5.6}
\]

If \(a:=|\mathcal X|\le231\), Lemma 5.1 applies directly.

Suppose \(a>231\).  Let

\[
\mathcal H
=\binom{[11]}6\setminus\overline{\mathcal X},
\qquad h=|\mathcal H|=462-a,
\]

and let \(\mathcal T\) be the missing part of the lower shadow:

\[
\mathcal T
=\binom{[11]}5\setminus\partial\overline{\mathcal X},
\qquad t=|\mathcal T|.
\]

Every six-set containing a member of \(\mathcal T\) belongs to
\(\mathcal H\), so

\[
\Gamma_G(\mathcal T)\subseteq\mathcal H.
\tag{5.7}
\]

The already existing perfect matching \(M\) gives
\(t\le|\Gamma_G(\mathcal T)|\le h\le230\).  If \(t>0\), Lemma 5.1,
applied after complementation, therefore gives

\[
h\ge|\Gamma_G(\mathcal T)|\ge t+5.
\tag{5.8}
\]

Hence

\[
|\partial\overline{\mathcal X}|-a
=(462-t)-(462-h)
=h-t\ge5.
\]

Equality with \(t>0\) forces \(t=1\), \(h=6\), and
\(\mathcal H\) to be the full six-set star over the unique member of
\(\mathcal T\).  Complementing back gives the \(456\)-vertex equality
family in the statement.

If \(t=0\), the shadow is full.  Its surplus is \(h\), which equals five
only at \(a=457\).  In particular \(h\le5\) makes \(t>0\) impossible by
(5.8), proving full shadow for every \(a\ge457\). \(\square\)

### Corollary 5.3 (complete endpoint-deletion classification)

Let \(P\subseteq\mathcal L\) and \(Q\subseteq\mathcal R\) satisfy
\(|P|=|Q|=c\le6\).  Consider the induced graph

\[
G[\mathcal L\setminus P,\mathcal R\setminus Q].
\]

* If \(c\le5\), it always has a perfect matching.
* If \(c=6\), it fails to have a perfect matching if and only if at least
  one of the following isolated-vertex obstructions occurs:
  \[
  Q=\Gamma_G(\{S\})
  \quad\text{for some }S\notin P,
  \tag{5.9}
  \]
  or
  \[
  P=\binom{U}{5}
  \quad\text{for some }U\notin Q.
  \tag{5.10}
  \]

#### Proof

Apply Hall to
\(\mathcal X\subseteq\mathcal L\setminus P\).  If its shadow is full, then

\[
|\Gamma_G(\mathcal X)\setminus Q|
=462-c
\ge|\mathcal X|.
\]

If its shadow is proper, Theorem 5.2 gives five units of surplus.  Deleting
at most five upper endpoints cannot violate Hall.

For \(c=6\), failure requires shadow surplus exactly five and all six
deleted upper vertices to lie in the shadow.  If the Hall family is a
singleton, this is exactly (5.9).  In the \(456\)-vertex equality case,
the Hall family must be all of \(\mathcal L\setminus P\); Theorem 5.2
then gives \(P=\binom{U}{5}\), and all six deleted uppers lie in
\(\mathcal R\setminus\{U\}\), so \(U\notin Q\).  This is (5.10).
Each displayed condition plainly isolates its remaining vertex, so each is
also sufficient for failure. \(\square\)

For a fixed \(j\)-set \(T\), \(1\le j\le5\), let

\[
\mathcal X_T=\{S\in\mathcal L:T\subseteq S\}.
\]

Its exact shadow surplus is

\[
|\mathcal X_T|=\binom{11-j}{5-j},
\qquad
|\Gamma_G(\mathcal X_T)|=\binom{11-j}{6-j},
\]

and hence

\[
\begin{array}{c|ccccc}
j&1&2&3&4&5\\ \hline
|\Gamma_G(\mathcal X_T)|-|\mathcal X_T|
&42&42&28&14&5.
\end{array}
\tag{5.11}
\]

Thus coordinate cylinders of codimension at most four retain at least
fourteen units of ordinary Hall slack against six endpoints.  Only a full
five-coordinate star can be tight.

Corollary 5.3 is a barrier, not a sufficiency theorem for the actual path
cover: the actual matching \(N\) must lie in \(G\setminus M\), and its union
with \(M\) must be acyclic.

## 6. Exact cuts and components of \(K=G\setminus M\)

Let

\[
K:=G\setminus M.
\]

It is a \(5\)-regular bipartite graph.  For
\(\mathcal X\subseteq\mathcal L\), put

\[
\mathcal Y=\Gamma_K(\mathcal X),
\qquad
\delta_M(\mathcal X)=|\mathcal Y|-|\mathcal X|.
\]

### Theorem 6.1 (endpoint flux and boundary)

The actual nonmatching matching \(N\) satisfies

\[
\boxed{
e_N(\mathcal L\setminus\mathcal X,\mathcal Y)
=
\delta_M(\mathcal X)
+|A\cap\mathcal X|
-|B\cap\mathcal Y|.}
\tag{6.1}
\]

Consequently

\[
\boxed{
|B\cap\Gamma_K(\mathcal X)|
-|A\cap\mathcal X|
\le\delta_M(\mathcal X).}
\tag{6.2}
\]

The ambient graph has the exact edge-boundary identity

\[
\boxed{
e_K(\mathcal L\setminus\mathcal X,\mathcal Y)
=5\delta_M(\mathcal X).}
\tag{6.3}
\]

#### Proof

The upper vertices of \(\mathcal Y\) carry
\(|\mathcal Y|-|B\cap\mathcal Y|\) edges of \(N\).  Exactly
\(|\mathcal X|-|A\cap\mathcal X|\) of these have their lower endpoint in
\(\mathcal X\).  Their difference is (6.1), and nonnegativity gives (6.2).

All \(5|\mathcal X|\) edges out of \(\mathcal X\) end in
\(\mathcal Y\).  The vertices of \(\mathcal Y\) have total \(K\)-degree
\(5|\mathcal Y|\); the remaining incidences are precisely the boundary in
(6.3). \(\square\)

For a singleton \(S\), (6.2) says

\[
S\notin A
\Longrightarrow
\left|B\cap
\bigl(\Gamma_G(S)\setminus\{M(S)\}\bigr)\right|\le4.
\tag{6.4}
\]

This is the upper-endpoint dual of Corollary 3.2.

### Theorem 6.2 (macroscopic \(K\)-components)

Let \((\mathcal C,\mathcal D)\) be a connected component of \(K\), with
\(\mathcal C\subseteq\mathcal L\) and
\(\mathcal D\subseteq\mathcal R\).  Put

\[
a=|\mathcal C|=|\mathcal D|,
\]

and let \(s\) be the number of edges of \(M\) between
\(\mathcal C\) and \(\mathcal D\).  Then

\[
\boxed{
e_{J(11,5)}(\mathcal C)=10a+5s,}
\tag{6.5}
\]

\[
\boxed{
a+10s\le\frac{11a^2}{462},}
\tag{6.6}
\]

and in particular

\[
\boxed{a\ge43.}
\tag{6.7}
\]

If \(43\le a\le50\), then \(s=0\).

For each coordinate \(x\), define

\[
t_x=|\{U\in\mathcal D:x\in U\}|
-|\{S\in\mathcal C:x\in S\}|.
\tag{6.8}
\]

Then

\[
\boxed{
t_x\ge0,\qquad
\#\{\text{\(x\)-labelled \(K\)-edges in the component}\}=5t_x,}
\tag{6.9}
\]

\[
\boxed{
\sum_{x=1}^{11}t_x=a.}
\tag{6.10}
\]

Across all \(K\)-components,

\[
\boxed{\sum_{\text{components }i}t_{i,x}=42.}
\tag{6.11}
\]

Finally, the actual endpoints balance separately in every \(K\)-component:

\[
\boxed{
|A\cap\mathcal C|=|B\cap\mathcal D|.}
\tag{6.12}
\]

#### Proof

Five-regularity gives equal side sizes.  Every \(U\in\mathcal D\) has its
five \(K\)-facets in \(\mathcal C\), plus its matched facet exactly when
that edge of \(M\) is internal.  A six-set outside \(\mathcal D\) has at
most one facet in \(\mathcal C\), since every other incident edge belongs
to \(K\).  A Johnson edge inside \(\mathcal C\) has a unique six-set union.
Therefore

\[
e_{J(11,5)}(\mathcal C)
=10(a-s)+15s
=10a+5s,
\]

proving (6.5).

The adjacency eigenvalues of \(J(11,5)\) are

\[
30,\ 19,\ 10,\ 3,\ -2,\ -5.
\]

For the indicator of an \(a\)-vertex family, the largest nonconstant
eigenvalue gives

\[
2e_{J(11,5)}(\mathcal C)
\le
19a+\frac{11a^2}{462}.
\tag{6.13}
\]

Substituting (6.5) gives (6.6).  Since \(s\ge0\), a nonempty component has
\(a\ge42\).  Equality \(a=42\) would force \(s=0\) and equality in
(6.13), hence

\[
\mathbf1_{\mathcal C}\in E_0\oplus E_1.
\]

A Boolean affine function on the five-slice is constant, a coordinate
dictator, or its complement.  Indeed, writing it as
\(c+\sum_iw_i\mathbf1_{i\in S}\), swaps show that the \(w_i\)'s have at
most two values differing by one; Booleanity then forces the exceptional
weight class to have size one or ten.  The possible support sizes are

\[
0,\ 462,\ 210,\ 252,
\]

not \(42\).  Thus \(a\ge43\).

For \(a\le50\), (6.6) gives

\[
10s\le\frac{a(a-42)}{42}<10,
\]

so \(s=0\).

To prove (6.9), count incidences of \(x\) over the \(K\)-edges of the
component.  The upper-end total is \(5|\mathcal D_x|\), the lower-end
total is \(5|\mathcal C_x|\), and their difference counts exactly the
edges adding \(x\).  This proves (6.9).  Summing point incidences gives
(6.10), and summing over components gives

\[
\binom{10}{5}-\binom{10}{4}=252-210=42,
\]

which is (6.11).

Finally, \(N\subseteq K\) matches all lower vertices outside \(A\) to all
upper vertices outside \(B\), component by component.  Equal remaining
side sizes give (6.12). \(\square\)

In particular \(K\) has at most ten connected components.  This theorem
does not say that the alternating paths remain inside one \(K\)-component:
the removed matching edges \(M\) may join distinct components.

## 7. Coordinate parity and run counts

For a coordinate \(x\), let

\[
\tau_x=|\{S\in A:x\in S\}|,\quad
\sigma_x=|\{S\in\Sigma:x\in S\}|,\quad
\mu_x=|\{U\in B:x\in U\}|.
\]

Let \(d_x\) be the number of terminal matching edges adding \(x\).  Since
each terminal upper set is its root plus its matching label,

\[
\mu_x=\sigma_x+d_x.
\tag{7.1}
\]

The endpoint totals are

\[
\sum_x\tau_x=\sum_x\sigma_x=5c,\qquad
\sum_x\mu_x=6c,\qquad
\sum_xd_x=c.
\tag{7.1a}
\]

Every perfect inclusion matching between the two middle levels adds a fixed
coordinate exactly

\[
\binom{10}{5}-\binom{10}{4}=42
\tag{7.2}
\]

times.  Consequently the contracted gaining-label count is

\[
f_x=42-d_x,
\tag{7.3}
\]

which is (3.20).

Let \(g_x\) be the number of nonmatching inclusion edges deleting \(x\).
Endpoint balance on the expanded paths gives

\[
\mu_x-\tau_x=42-g_x,
\]

and therefore

\[
\boxed{g_x=42-\mu_x+\tau_x.}
\tag{7.4}
\]

On the contracted lower paths,

\[
f_x-g_x=\sigma_x-\tau_x.
\tag{7.5}
\]

These are exactly the endpoint bridges in (3.23)--(3.24).

### Proposition 7.1 (all aggregate parity cylinders)

The expanded alternating path cover has exactly

\[
\boxed{
\ell_x=42+g_x=84-\mu_x+\tau_x}
\tag{7.6}
\]

edges toggling coordinate \(x\).  Hence

\[
\ell_x\equiv\mu_x+\tau_x\pmod2.
\tag{7.7}
\]

For an arbitrary coordinate set \(C\subseteq[11]\), let
\(\mathcal V_C\) be the vertices for which \(|V\cap C|\) is odd.  An
inclusion edge crosses the cut
\((\mathcal V_C,\mathcal V_C^c)\) exactly when its unique toggled
coordinate belongs to \(C\), so

\[
\boxed{
e_{\mathscr P}(\mathcal V_C,\mathcal V_C^c)
=84|C|+\sum_{x\in C}(\tau_x-\mu_x),}
\tag{7.8}
\]

\[
e_{\mathscr P}(\mathcal V_C,\mathcal V_C^c)
\equiv
\sum_{x\in C}(\tau_x+\mu_x)
\pmod2.
\tag{7.9}
\]

Thus every aggregate coordinate-parity cylinder is the sum of the eleven
single-coordinate identities.  It adds no new marginal constraint.

After contraction, one transition first adds a coordinate \(a\) and then
deletes a distinct coordinate \(b\).  It crosses the \(C\)-parity cut on
\(\mathcal L\) exactly when exactly one of \(a,b\) lies in \(C\).  If
\(\kappa_C\) counts transitions with both labels in \(C\), the contracted
crossing count is

\[
\boxed{
f(C)+g(C)-2\kappa_C.}
\tag{7.10}
\]

The unknown \(\kappa_C\) is a genuine two-label correlation.  Equations
(3.20)--(3.24) determine only the marginals \(f_x,g_x\), so (7.10)
pinpoints the missing data in any stronger parity attack.

### Proposition 7.2 (exact one-run and zero-run totals)

Orient every contracted path from its initial vertex to its root.  Then
\(f_x\) counts \(0\)-to-\(1\) transitions and \(g_x\) counts
\(1\)-to-\(0\) transitions.  The total numbers of one-runs and zero-runs
of coordinate \(x\), treating components separately, are

\[
\boxed{
O_x=f_x+\tau_x=g_x+\sigma_x
=42-d_x+\tau_x,}
\tag{7.11}
\]

\[
\boxed{
Z_x=g_x+c-\tau_x=f_x+c-\sigma_x
=42+c-\mu_x.}
\tag{7.12}
\]

In particular,

\[
\boxed{
\sum_xO_x=462+4c,\qquad
\sum_xZ_x=462+5c.}
\tag{7.13}
\]

For a path containing \(t\) lower vertices, the initial five-set starts five
one-runs and six zero-runs; each of the \(t-1\) swaps starts one new run of
each kind.  Its contributions are therefore \(t+4\) and \(t+5\).
This also verifies the singleton case \(t=1\).

Equations (7.6)--(7.13) show that aggregate parity and run counting close as
identities.  They do not force a seventh path or an endpoint collision.

## 8. A rigorous barrier: the abstract package is realizable

The middle-level graph \(G\) has a Hamilton cycle.  Alternate its cycle
edges into two perfect inclusion matchings \(M_0,N_0\), and delete one edge
of \(N_0\).  Then

\[
M_0\cup(N_0\setminus\{e\})
\]

is one alternating Hamilton path covering all \(924\) vertices.

Contracting \(M_0\) gives a Hamilton path through all \(462\) five-sets.
Every one of its \(461\) Johnson edges has a distinct six-set union color,
because it comes from a distinct upper vertex of the alternating path.
The omitted color is the upper endpoint created by deleting \(e\).

Every coordinate labels exactly \(42\) matching edges by (7.2), and all
endpoint, parity, and run identities above hold with \(c=1\).  Thus the
following abstract data are simultaneously realizable:

* at most six alternating paths;
* a perfect middle-level matching;
* a rainbow spanning Johnson forest;
* the \(42\)-per-coordinate extension law;
* (3.20)--(3.24);
* all ordinary endpoint Hall cuts; and
* every aggregate coordinate-parity identity.

This example does not realize the physical interval-offset schedule of a
zero-margin word.  It proves the narrower and essential barrier: no argument
using only the abstract path-cover package can yield a contradiction.

## 9. The exact remaining lemma

The full-graph shadow theorem loses precisely the information that the
second matching must avoid \(M\).  For
\(\mathcal X\subseteq\mathcal L\), define the \(M\)-private-neighbor count

\[
p_M(\mathcal X)
=
\#\left\{
U\in\Gamma_G(\mathcal X):
\binom{U}{5}\cap\mathcal X=\{M^{-1}(U)\}
\right\}.
\tag{9.1}
\]

Deleting \(M\) removes exactly these neighbors, so

\[
\boxed{
|\Gamma_K(\mathcal X)|
=|\Gamma_G(\mathcal X)|-p_M(\mathcal X).}
\tag{9.2}
\]

Combining (6.2) and (9.2), an \(M\)-relative Hall contradiction is exactly
the assertion that some \(\mathcal X\) satisfies

\[
\boxed{
p_M(\mathcal X)
+|B\cap\Gamma_K(\mathcal X)|
-|A\cap\mathcal X|
>
|\Gamma_G(\mathcal X)|-|\mathcal X|.}
\tag{9.3}
\]

By the \(K\)-neighborhood analogue of Theorem 4.1, unless (9.3) is the
explicit singleton pin, such a family must contain at least \(18\)
sources.

Even if every Hall cut holds, the selected matching may create alternating
cycles.  A direct sufficient obstruction to acyclicity is a root-free set

\[
\varnothing\ne\mathcal X\subseteq\mathcal L\setminus\Sigma
\]

with

\[
\boxed{
\Gamma_M^+(\mathcal X)\setminus A
\subseteq\mathcal X.}
\tag{9.4}
\]

Every endpoint-feasible successor map then permutes a nonempty subset of
\(\mathcal X\), forcing a directed cycle.  Unless it is a singleton pin,
Theorem 4.1 gives \(|\mathcal X|\ge17\).

Accordingly the smallest replacement lemma for this route is one of the
following.

> **Physical-order private-neighbor lemma.**  
> For the endpoint-order matching \(M\) forced by every zero-margin
> survivor, the physical state blocks and central \(03\) interval force a
> family satisfying (9.3).

or

> **Physical-order closed-trap lemma.**  
> They force a root-free family satisfying (9.4), or more generally force
> every endpoint-feasible matching in \(G\setminus M\) to contain an
> \(M\)-alternating cycle.

Neither lemma follows from (3.20)--(3.24), coordinate marginals, or ordinary
middle-level isoperimetry.  The missing input must couple the physical
offset order to \(M\)-private neighbors or to the two-label correlations in
(7.10).

## 10. Adversarial audit

The main steps were independently rederived and cross-checked.

1. **The shadow constant five is sharp.**  Lemma 5.1 includes the
   compression ranges and all equality cases; no unproved finite
   Kruskal--Katona digit minimization is hidden.
2. **The \(17/18\) thresholds use integer equality cases.**  The continuous
   bound (4.3) alone stops earlier.  The \(t=15,16,17\) cases were checked
   by convexity of multiplicities, the exact Turán numbers, and the
   classification of a seven-clique in \(J(11,6)\).
3. **The full-\(G\) theorem has limited scope.**  It permits the deleted
   matching edge and does not enforce acyclicity.  It is used only as a
   barrier and as the isolated-star classification, never as a construction
   of the actual \(N\).
4. **\(K\)-components are not path components.**  Equation (6.12) holds
   componentwise because \(N\subseteq K\), but the removed matching \(M\)
   may connect different \(K\)-components.  No path-containment claim is
   made.
5. **Parity is only exhausted at the marginal level.**  Equation (7.10)
   explicitly retains the unknown pair correlation \(\kappa_C\).  The
   report does not claim that all order-sensitive parity information is
   determined.
6. **The Hamilton-cycle example is abstract.**  It refutes an abstract
   endpoint/parity/isoperimetric contradiction, not the possibility of a
   contradiction after the physical interval schedule is imposed.

Therefore this route does not prove that the zero-margin templates exist or
that they are impossible.  Its strongest unconditional advance is the exact
endpoint-cut reduction (3.1)--(4.4), the sharp full-graph classification
(5.5)--(5.10), and the macroscopic prescribed-matching component theorem
(6.5)--(6.12).
