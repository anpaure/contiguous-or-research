# Fixed colour pairs at depth one: an exact path-factor construction, the local upper ledger, and the lexical capacity obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, or web input
is used.

## 0. Outcome

Put

\[
 \Omega=[2m],\qquad {\cal M}=\binom\Omega m,\qquad
 {\cal L}=\binom\Omega{m-1},\qquad
 {\cal U}=\binom\Omega{m+1},
\]

and

\[
 W=|{\cal M}|,\qquad
 N=|{\cal L}|=|{\cal U}|={m\over m+1}W,
 \qquad D=W-N={W\over m+1}=\operatorname {Cat}_m.
 \tag{0.1}
\]

Let (B_m) be the inclusion graph between ({\cal L}) and
({\cal M}).  Its maximum degree is (s=m+1).  This note audits the
proposal to properly (s)-edge-colour (B_m), fix two colours (a,b),
and suppress every lower vertex between its (a)- and (b)-neighbours.

The conclusions are as follows.

1.  Every colour pair produces a **spanning** lower-rainbow Johnson
    pseudofactor with (N) edges.  It has degrees one and two, exactly
    (2D) degree-one owners, exactly (D) directed path components, and
    some number (c_{ab}) of directed cycles.  Thus its component count is
    exactly (D+c_{ab}).
2.  Conversely, every spanning lower-rainbow Johnson graph with all owner
    degrees in ({1,2}) is the fixed-pair factor of some proper
    (s)-edge-colouring.  The edge-colouring formulation is therefore an
    exact normal form, not a relaxation of the common-owner problem.
3.  The component gate can be closed unconditionally.  Starting from the
    Gregor--Mička--Mütze saturating cycle, adding (D) dummy lower
    vertices, and then restricting an alternating Hamilton factor gives a
    proper colouring and a colour pair whose real factor is a spanning
    linear forest with **exactly (D) paths and no cycles**.  Hence for
    every (H=o(m)), its number of components is (o(W/H)).
4.  This construction changes only (D=o(W)) edges of the projected GMM
    cycle.  Its upper-union defect differs from the GMM triple-union defect
    by at most (D).  Consequently the component construction does not
    solve, but also does not worsen asymptotically, the sole remaining
    upper-colour gate.
5.  For a fixed upper (U), the exact multiplicity of a colour pair is a
    two-dimensional local incidence statistic.  The missing-colour
    histogram supplies only its degree-sum identities.  Exact upper coverage for one fixed
    pair only requires that pair to occur once at every (U); it does
    **not** require all unordered colour pairs to occur once.
6.  The stronger simultaneous all-pairs condition forces every
    missing-colour fibre to be a Steiner system
    (S(m-1,m,2m)).  It is impossible for every odd (m).  A quantitative
    packing form of this obstruction is proved below.
7.  The most direct lexical attempt, obtained by matching ranks (m-1)
    and (m+1) along the Greene--Kleitman symmetric chains, has exact lower
    and upper flags but a linear middle-capacity defect.  Its alternate
    middle map omits exactly (W/2) owners and has exact overload excess
    (W/2-D).  Sparse deletion cannot turn it into a fixed-pair factor.

Thus the new positive theorem completely removes component fusion at
(q=1).  The surviving assertion is sharply isolated: construct a
GMM-type saturating cycle, or an equivalent fixed-pair path factor, whose
upper-union collision excess is (o(W)).  That assertion is not proved
here, so constant one is not claimed.

## 1. Exact fixed-pair structure

Let (C) be a set of (s=m+1) colours and let

\[
 c:E(B_m)\longrightarrow C
 \tag{1.1}
\]

be a proper edge-colouring.  At a lower vertex (R), all (s) colours
occur once.  At a middle vertex (X), exactly (m) colours occur, so it
has a unique missing colour; denote it by (mu(X)).

For (a\ne b), let (X_a(R)) and (X_b(R)) be the unique middle
neighbours of (R) on edges of colours (a) and (b).  Suppress (R)
to the Johnson edge

\[
 e_R=X_a(R)X_b(R).
 \tag{1.2}
\]

The endpoints are distinct because the colouring is proper at (R).
Write (F_{ab}) for the resulting graph on ({\cal M}).

### Theorem 1.1 (fixed-pair path--cycle normal form)

For every proper colouring (1.1) and every pair (a\ne b):

1. (F_{ab}) has exactly (N) edges, and
   (e_R\mapsto R=X_a(R)\cap X_b(R)) is a bijection from its edges to
   ({\cal L});
2. for every (X\in{\cal M}),

   \[
    d_{F_{ab}}(X)=
    \begin{cases}
      1,&\mu(X)\in\{a,b\},\\
      2,&\mu(X)\notin\{a,b\};
    \end{cases}
    \tag{1.3}
   \]

3. each missing-colour fibre
   ({\cal M}_a=\{X:\mu(X)=a\}) has size (D);
4. after orienting every edge from its (a)-neighbour to its
   (b)-neighbour, (F_{ab}) is the disjoint union of exactly (D)
   directed paths from ({\cal M}_b) to ({\cal M}_a), together with
   (c_{ab}) directed cycles.  In particular,

   \[
                    \operatorname {comp}(F_{ab})=D+c_{ab}.
    \tag{1.4}
   \]

#### Proof

There is one edge (1.2) for each lower vertex, and its intersection is
that lower vertex.  This proves the first assertion.

At (X), every present colour occurs on exactly one incident inclusion
edge.  Hence exactly the colours among ({a,b}) which are present at
(X) contribute to (1.3).

A fixed colour class is a matching which saturates all (N) lower
vertices.  It consequently meets (N) distinct middle vertices and misses
exactly (W-N=D), proving the third assertion.

Orient (1.2) from (X_a(R)) to (X_b(R)).  A vertex missing (b) has
outdegree one and indegree zero, a vertex missing (a) has indegree one
and outdegree zero, and every other vertex has indegree and outdegree one.
Thus every noncyclic component is a directed path from ({\cal M}_b) to
({\cal M}_a).  The two endpoint fibres both have size (D), so there
are exactly (D) paths.  The remaining components are directed cycles.
\(\square\)

The converse shows that no hidden edge-colouring restriction remains.

### Theorem 1.2 (extension of every lower-rainbow degree-(1/2) factor)

Let (F\subseteq J(2m,m)) be spanning and suppose that

* every (R\in{\cal L}) is the intersection colour of exactly one edge
  of (F); and
* (1\le d_F(X)\le2) for every (X\in{\cal M}).

Then there is a proper (s)-edge-colouring of (B_m) and a pair of
colours (a,b) whose suppressed factor is exactly (F).

#### Proof

Subdivide the edge of (F) with lower colour (R) by the lower vertex
(R).  The resulting subgraph (H\subseteq B_m) has degree two at every
lower vertex and degree (d_F(X)\in\{1,2}) at every middle vertex.  It is
bipartite and has maximum degree two, so each of its path and even-cycle
components has a proper two-edge-colouring by (a,b).

Delete (H) from (B_m).  Every lower vertex now has degree (m-1), and
every middle vertex has degree (m-d_F(X)\le m-1).  By Koenig's line
colouring theorem, the residual bipartite graph has a proper edge-colouring
with (m-1) new colours.  Combining the two colourings gives a proper
((m+1))-edge-colouring of (B_m), and suppression of (a,b) recovers
(F). \(\square\)

### Corollary 1.3 (the exact one-pair target)

For a fixed pair factor define

\[
 k_U(a,b)=|\{R\subset U:|R|=m-1,\ X_a(R)\cup X_b(R)=U\}|.
 \tag{1.5}
\]

Then

\[
 \sum_{U\in{\cal U}}k_U(a,b)=N=|{\cal U}|.
 \tag{1.6}
\]

Consequently its number of missing upper colours is

\[
 h_{ab}=|\{U:k_U(a,b)=0\}|
       =\sum_U(k_U(a,b)-1)_+
       ={1\over2}\sum_U|k_U(a,b)-1|.
 \tag{1.7}
\]

An exact upper-rainbow spanning linear forest is therefore equivalent to a
pair with

\[
 k_U(a,b)=1\quad(U\in{\cal U}),\qquad c_{ab}=0.
 \tag{1.8}
\]

It has exactly (D) path components.  More generally, when (H=o(m)),
the desired component rate (o(W/H)) follows from

\[
                         c_{ab}=o(W/H),                 \tag{1.9}
\]

because (D=W/(m+1)=o(W/H)).

### Corollary 1.4 (capacitated rank-two Hall form)

Let \(G^{(2)}_m\) be the bipartite graph on \({\cal L}\dot\cup{\cal U}\)
in which \(R\) and \(U\) are adjacent when \(R\subset U\).  For a
matching \(\phi:{\cal L}\to{\cal U}\), define its middle load by

\[
 d_\phi(X)=|\{R\in{\cal L}:R\subset X\subset\phi(R)\}|.
 \tag{1.10}
\]

An exact two-sided fixed-pair pseudofactor is equivalent to a perfect
matching \(\phi\) of \(G^{(2)}_m\) satisfying

\[
                         1\le d_\phi(X)\le2
                         \quad(X\in{\cal M}).            \tag{1.11}
\]

Under this equivalence, the selected interval \([R,\phi(R)]\) is the
Johnson edge between its two middle members.  Requiring the resulting
graph to be acyclic is equivalent to obtaining exactly \(D\) paths.

The natural fractional system is feasible: with

\[
 K=\binom{m+1}{2},\qquad x_{R,U}=K^{-1}\quad(R\subset U),
 \tag{1.12}
\]

every lower and upper equation has load one and every middle vertex has
load

\[
                         {m^2\over K}={2m\over m+1}.
 \tag{1.13}
\]

This fractional feasibility does not round by total unimodularity.  For
one fixed \(U\), choose three of its middle facets
\(X_1,X_2,X_3\).  The three interval columns corresponding to the pairs
\(X_1X_2,X_2X_3,X_3X_1\), restricted to the three middle-load rows, form

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad \det=2.                                         \tag{1.14}
\]

Thus (1.11) is the exact capacitated Hall/integral-grouping gate; ordinary
perfect matching in \(G^{(2)}_m\) and the symmetric fractional point do
not settle it.

#### Proof

For a fixed-pair factor, put
\(\phi(R)=X_a(R)\cup X_b(R)\).  Equation (1.5) says that exact upper
coverage is precisely bijectivity of \(\phi\), and (1.3) says that its
middle loads are in \(\{1,2\}\).

Conversely, every selected interval has exactly two middle members.
Joining them produces a spanning lower- and upper-rainbow graph with
degrees (1.10).  Theorem 1.2 realizes it as a fixed-pair factor.  If it is
acyclic, it has \(W-N=D\) components.

There are \(K\) rank-two supersets of every \(R\), \(K\) rank-two subsets
of every \(U\), and \(m^2\) intervals through every \(X\), proving
(1.12)--(1.13).  The displayed minor proves the last assertion.
\(\square\)

## 2. The component gate is solvable exactly

The next theorem is the main positive result of this note.

### Theorem 2.1 (GMM--dummy Hamilton augmentation)

For every (m\ge2), there is a proper ((m+1))-edge-colouring of (B_m)
and a pair (a,b) whose suppressed factor is a spanning lower-rainbow
linear forest on ({\cal M}) with exactly (D) path components and no
cycle components.

Moreover, if (P) denotes the projected Gregor--Mička--Mütze saturating
cycle used in the construction and (F) the resulting forest, then (F)
is obtained from (P) by replacing exactly (D) edges.  Hence, if

\[
 c_+(P)=N-|\{X\cup Y:XY\in E(P)\}|                  \tag{2.1}
\]

and (h_+(F)) is the analogous upper-hole count for (F), then

\[
                         |h_+(F)-c_+(P)|\le D.          \tag{2.2}
\]

#### Proof

Gregor--Mička--Mütze give a saturating cycle in (B_m).  Write it as

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0,          \tag{2.3}
\]

where all lower vertices occur and the (X_i)'s are distinct.  Let

\[
 {\cal E}={\cal M}\setminus\{X_0,\ldots,X_{N-1}\};
 \qquad |{\cal E}|=D.                                  \tag{2.4}
\]

We first choose distinct facets of the omitted owners.  For every nonempty
({\cal A}\subseteq{\cal E}), write
(\partial{\cal A}\subseteq{\cal L}) for its lower shadow.  If
(|{\cal A}|=\binom{x}{m}) in the generalized-binomial notation, the
Lovasz form of Kruskal--Katona gives

\[
 |\partial{\cal A}|\ge\binom{x}{m-1}.
 \tag{2.5}
\]

Since

\[
 |{\cal A}|\le D\le {W\over2}=\binom{2m-1}{m},         \tag{2.6}
\]

we have (x\le2m-1), and therefore

\[
 {\binom{x}{m-1}\over\binom{x}{m}}
 ={m\over x-m+1}\ge1.                                 \tag{2.7}
\]

Thus (|\partial{\cal A}|\ge|{\cal A}|) for every
({\cal A}\); the empty family is trivial.  Hall's theorem therefore supplies
an injective facet map

\[
                 \phi:{\cal E}\longrightarrow{\cal L},
                 \qquad \phi(Y)\subset Y.              \tag{2.8}
\]

Fix one of the two alternating perfect matchings of the cycle (2.3).  For
each (Y\in{\cal E}), let (R_Y=\phi(Y)) and let (X_Y) be the middle
neighbour of (R_Y) selected by this fixed alternating matching.  The
(R_Y)'s are distinct, so the (X_Y)'s are distinct.  They lie on the
cycle and hence are disjoint from ({\cal E}).

Partition all (W=D(m+1)) middle vertices into (D) groups

\[
 G_Y\quad(Y\in{\cal E}),\qquad |G_Y|=m+1,              \tag{2.9}
\]

so that ({Y,X_Y}\subseteq G_Y).  This is possible because the (2D)
specified vertices are distinct; distribute the remaining
(D(m-1)) vertices with (m-1) to each group.

For every (Y), add one dummy lower vertex (d_Y), adjacent to all
vertices of (G_Y).  The augmented bipartite graph \(\widetilde B_m\)
has (N+D=W) vertices on each shore and is ((m+1))-regular: a real lower
vertex already had degree (m+1), every dummy has degree (m+1), and
every middle vertex has its original (m) incidences plus its unique
dummy incidence.

In (2.3), replace the distinct incidence edges (X_YR_Y) by the
three-edge paths

\[
                         X_Y,d_Y,Y,R_Y.                 \tag{2.10}
\]

All inserted vertices are new to (2.3), and every omitted owner and every
dummy is inserted once.  Thus the result is a Hamilton cycle
(\widetilde C) of \(\widetilde B_m\).

Colour the edges of (\widetilde C) alternately (a,b).  After deleting
them, the residual graph is ((m-1))-regular and bipartite, so it splits
into (m-1) perfect matchings.  Colour those matchings with the remaining
(m-1) colours.  This is a proper ((m+1))-edge-colouring of
(\widetilde B_m).

Delete the dummy vertices and restrict the colouring to (B_m).  Every
real lower vertex still sees all (m+1) colours.  Every middle vertex has
lost its unique dummy edge and so misses exactly its colour.  Hence the
restriction is a proper ((m+1))-edge-colouring of (B_m).

Deleting the (D) dummy vertices from the Hamilton cycle
(\widetilde C) leaves exactly (D) alternating paths which span every
middle and every real lower vertex.  No middle vertex is adjacent to two
dummies on (\widetilde C), because the designated vertices (Y,X_Y)
are all distinct.  Suppressing the real lower vertices therefore gives a
spanning Johnson linear forest with exactly (D) nonempty paths.  Every
real lower vertex occurs once, so its lower colours are exact.

At (R_Y), the projected edge of (P) joining the two old cycle
neighbours is replaced by the edge joining (Y) to the old neighbour
other than (X_Y).  All other projected edges are unchanged.  Exactly
(D) entries of the upper-colour multiset are therefore replaced.  The
support size of a multiset changes by at most the number of replaced
entries, which proves (2.2). \(\square\)

### Corollary 2.2 (precise surviving gate)

For the construction in Theorem 2.1,

\[
 h_+(F)=o(W)\quad\Longleftrightarrow\quad c_+(P)=o(W),  \tag{2.11}
\]

because (D=o(W)).  Thus the fixed-pair route has no residual component
or edge-colouring problem: it is exactly the GMM opposite-colour problem,
up to the negligible (D)-edge insertion.

## 3. Exact upper multiplicity and the endpoint cut

Fix (U\in{\cal U}).  For distinct (x,y\in U), put

\[
 A_U(y,x)=c\bigl(U\setminus\{x,y\},\ U\setminus\{y\}\bigr). \tag{3.1}
\]

Thus (A_U(y,x)) is the colour obtained by adding (x) to the lower set
(U\setminus\{x,y\}).  Properness gives

* for fixed (y), the values (A_U(y,x)), (x\ne y), are all distinct
  and form (C\setminus\{\mu(U\setminus\{y\})\});
* (A_U(y,x)\ne A_U(x,y)).

Associate to the coordinate edge ({x,y}\subset U) the colour edge

\[
             p_U(\{x,y\})=\{A_U(y,x),A_U(x,y)\}.        \tag{3.2}
\]

### Proposition 3.1 (local colour-pair multigraph)

Let

\[
 n_a(U)=|\{y\in U:\mu(U\setminus\{y\})=a\}|.          \tag{3.3}
\]

Then the multigraph on colour set (C) consisting of the
(\binom{m+1}{2}) edges (3.2) has no loops and satisfies

\[
 k_U(a,b)=|p_U^{-1}(\{a,b\})|,                          \tag{3.4}
\]

and

\[
                 \sum_{b\ne a}k_U(a,b)=m+1-n_a(U).     \tag{3.5}
\]

#### Proof

The no-loop assertion is the second properness bullet.  Equation (3.4)
is precisely the definition of the suppressed edge at
(R=U\setminus\{x,y\}).  Colour (a) occurs once in row (y) unless it
is the missing colour of (U\setminus\{y\}).  Counting its occurrences
over the (m+1) rows proves (3.5). \(\square\)

The histogram (n_a(U)) supplies the degree sequence (3.5), whereas the
individual edge multiplicities (3.4) require the full array (3.1).  In particular, the correct
fixed-pair condition is only (k_U(a,b)=1).  Requiring all unordered
pairs once is the stronger assertion that (p_U) is a bijection.

There is also an exact common-owner cut which every proposed pair must
pass.  Let

\[
 {\cal E}_{ab}={\cal M}_a\mathbin{\dot\cup}{\cal M}_b  \tag{3.6}
\]

be the (2D) degree-one owners, and write (d_{\cal A}(x)) for the number
of sets in a family ({\cal A}) containing coordinate (x).

### Theorem 3.2 (endpoint point-margin identity)

For every coordinate (x\in\Omega),

\[
 d_{{\cal E}_{ab}}(x)-D
       =-\sum_{\substack{U\in{\cal U}\\x\in U}}
                   (k_U(a,b)-1).                        \tag{3.7}
\]

Consequently

\[
 \boxed{\quad
 \sum_{x\in\Omega}|d_{{\cal E}_{ab}}(x)-D|
       \le2(m+1)h_{ab}.\quad}                           \tag{3.8}
\]

In particular, exact upper coverage forces the endpoint family to be
point-regular:

\[
                         d_{{\cal E}_{ab}}(x)=D
                         \quad(x\in\Omega).              \tag{3.9}
\]

#### Proof

For a Johnson edge with lower colour (R), upper colour (U), and middle
endpoints (X,Y), one has the pointwise diamond identity

\[
                         1_R+1_U=1_X+1_Y.                \tag{3.10}
\]

Sum (3.10) over (F_{ab}).  Every lower colour occurs once, upper (U)
occurs (k_U(a,b)) times, and every middle owner has degree two except the
members of ({\cal E}_{ab}), which have degree one.  Hence

\[
 d_{\cal L}(x)+\sum_{U\ni x}k_U(a,b)
       =2d_{\cal M}(x)-d_{{\cal E}_{ab}}(x).             \tag{3.11}
\]

The binomial identities

\[
 2d_{\cal M}(x)-d_{\cal L}(x)-d_{\cal U}(x)=D          \tag{3.12}
\]

give (3.7) after subtracting the baseline (k_U=1).
By (1.7),
(sum_U|k_U-1|=2h_{ab}).  Apply the triangle inequality to (3.7) and
sum over (x); each (U) contains (m+1) coordinates.  This proves
(3.8), and (3.9) follows when (h_{ab}=0). \(\square\)

For the forest of Theorem 2.1, the endpoint family is exactly

\[
                 {\cal E}\mathbin{\dot\cup}\{X_Y:Y\in{\cal E}\}.
 \tag{3.13}
\]

Thus (3.8) is a concrete necessary condition on the facet SDR and the
choice of alternating cycle neighbours.  It is a genuine cut, but it is
not sufficient for upper injectivity.

## 4. Why simultaneous perfection of all colour pairs is too strong

Suppose now that, for every (U), the map (p_U) in (3.2) is a
bijection between the coordinate edges and the colour edges.  Then its
colour multigraph is (K_{m+1}).  Equation (3.5) gives

\[
                         n_a(U)=1                       \tag{4.1}
\]

for every colour (a) and every upper (U).

### Theorem 4.1 (Steiner obstruction to all-pairs perfection)

If every (p_U) is bijective, then for every colour (a), the missing
fibre ({\cal M}_a) is a Steiner system

\[
                         S(m-1,m,2m).                    \tag{4.2}
\]

Consequently simultaneous all-pairs perfection is impossible whenever
(m) is odd.

#### Proof

By (4.1), every ((m+1))-set contains exactly one member of
({\cal M}_a) as a facet.  Thus no two members of ({\cal M}_a) can share
an ((m-1))-subset.  Since (|{\cal M}_a|=D), the members of
({\cal M}_a) contain exactly

\[
                         mD=N=|{\cal L}|                \tag{4.3}
\]

((m-1))-subsets in total.  They therefore contain every member of
({\cal L}) exactly once, which is (4.2).

Fix an ((m-2))-set (A).  The blocks of (4.2) containing (A) add
pairs from the remaining (m+2) points.  Every ((m-1))-set
(A\cup\{x\}) must occur exactly once, so these added pairs form a perfect
matching of those (m+2) points.  Hence (m+2) is even.  Therefore (m)
must be even. \(\square\)

The obstruction has a quantitative packing form.  Define the upper-shadow
hole count of one missing fibre by

\[
 h_a=|\{U\in{\cal U}:n_a(U)=0\}|.                       \tag{4.4}
\]

### Proposition 4.2 (odd-(m) aggregate defect)

If (m) is odd, then for every colour (a),

\[
 h_a\ge {W\over(m+1)(m+2)}.                             \tag{4.5}
\]

Moreover, if

\[
 \delta_U=\sum_{\{a,b\}\subset C}(1-k_U(a,b))_+        \tag{4.6}
\]

is the number of missing colour pairs at (U), then

\[
 \sum_{U\in{\cal U}}\delta_U
 =\sum_{\{a,b\}\subset C}h_{ab}
 \ge {W\over2(m+2)}.                                   \tag{4.7}
\]

#### Proof

Let ({\cal I}\subseteq{\cal M}) be independent in (J(2m,m)).  For a
fixed ((m-2))-set (A), the pairs (I\setminus A), over
(I\in{\cal I}) containing (A), are disjoint.  When (m) is odd there
are at most ((m+1)/2) such pairs.  Double-counting incidences
(A\subset I) gives

\[
 |{\cal I}|\binom m2
 \le\binom{2m}{m-2}{m+1\over2},
\]

and hence

\[
                         |{\cal I}|\le {W\over m+2}.     \tag{4.8}
\]

For fixed (a), one has

\[
 \sum_U n_a(U)=m|{\cal M}_a|=mD=N=|{\cal U}|,          \tag{4.9}
\]

so

\[
 h_a=\sum_U(n_a(U)-1)_+.                                \tag{4.10}
\]

From each (U) with (n_a(U)>1), mark all but one of its
({\cal M}_a)-facets for deletion.  The union of all marked sets has size
at most the right side of (4.10), and the surviving family is independent.
Therefore (D-h_a\le W/(m+2)).  Since (D=W/(m+1)), this is (4.5).

At a fixed (U), the colour multigraph has the same total number of edges
as (K_{m+1}).  Thus its missing-edge count equals its repetition excess,
which proves the equality in (4.7) after summing (1.7) over colour pairs.
Also, from (3.5), the degree deficit at colour (a) is (n_a(U)-1).
Every missing colour edge pays for at most two units of positive degree
deficit, so

\[
 \delta_U\ge {1\over2}\sum_a(n_a(U)-1)_+.              \tag{4.11}
\]

Sum (4.11), use (4.10), (4.5), and (|C|=m+1), obtaining

\[
 \sum_U\delta_U\ge {1\over2}\sum_a h_a
 \ge {m+1\over2}{W\over(m+1)(m+2)},
\]

which is (4.7). \(\square\)

This aggregate lower bound does **not** obstruct one selected pair from
having (h_{ab}=o(W)).  It only rules out the stronger exact orthogonal
array simultaneously for all pairs.

## 5. The Greene--Kleitman lexical flag matching has linear capacity loss

There is a tempting exact flag construction.  Take the standard
Greene--Kleitman symmetric-chain decomposition of (2^\Omega).  Every
chain meeting rank (m-1) also meets rank (m+1), so following a chain
defines a bijection

\[
 \Phi:{\cal L}\longrightarrow{\cal U},\qquad R\subset\Phi(R). \tag{5.1}
\]

The interval ([R,\Phi(R)]) has two middle owners.  One is the rank-(m)
member on the same chain, called the primary owner; call the other the
alternate owner.  Thus (5.1) has exact lower and upper flags.  The issue is
the multiplicity of the alternate map.

Use binary words, with (1) an opening parenthesis and (0) a closing
parenthesis, and greedily match (1)'s to later (0)'s.  A balanced word
(Y\in{\cal M}) has a unique decomposition

\[
 Y=P_0\,0\,P_1\,0\cdots0\,P_j\,1\,P_{j+1}\,1\cdots1\,P_{2j}. \tag{5.2}
\]

where the displayed (0)'s and (1)'s are the unmatched symbols and
every (P_i) is a Dyck word.  Factor the central Dyck word (P_j) uniquely
into primitive Dyck words.  Let \(\rho(Y)\) be the number of those primitive
factors.

### Lemma 5.1 (exact alternate multiplicity)

The number of lower sets \(R\) whose alternate owner is \(Y\) is exactly
\(\rho(Y)\).

#### Proof

At rank (m-1), the unmatched symbols of a chain word have the form
(0^{j+2}1^j).  The primary middle owner is obtained by flipping the
rightmost unmatched zero, while the alternate owner is obtained by
flipping the preceding unmatched zero.  In the alternate word, those two
positions become the opening and closing symbols of one primitive Dyck
factor in the central slot of (5.2).

Conversely, choose any primitive factor in (P_j), and change its initial
(1) to (0).  Its terminal (0) and the changed initial symbol become
two consecutive unmatched zeros; all symbols inside the primitive factor
remain matched.  The resulting rank-((m-1)) word has (Y) as its
alternate owner.  These operations are inverse. \(\square\)

Let

\[
 C(z)=\sum_{r\ge0}\operatorname {Cat}_r z^r,
 \qquad P(z)=zC(z)                                      \tag{5.3}
\]

be the generating functions of Dyck words and primitive Dyck words.

### Theorem 5.2 (exact half-layer lexical failure)

For (m\ge1),

\[
 |\{Y\in{\cal M}:\rho(Y)=0\}|={W\over2},               \tag{5.4}
\]

and

\[
 \sum_{Y\in{\cal M}}(\rho(Y)-1)_+={W\over2}-D.         \tag{5.5}
\]

Consequently, if (p(Y)) is one for a non-singleton-chain middle owner
and zero for a singleton-chain owner, then

\[
 \sum_Y(p(Y)+\rho(Y)-2)_+\ge {W\over2}-2D.              \tag{5.6}
\]

At least

\[
                  \max\left\{0,{W\over4}-D\right\}       \tag{5.7}
\]

of the interval edges in (5.1) must be deleted merely to make every
middle degree at most two.  In particular, deletion of (o(W)) flags
cannot turn the lexical construction into a fixed-pair factor.

#### Proof

For fixed (j) in (5.2), the unmatched symbols contribute (z^j), and
the (2j) noncentral Dyck slots contribute (C(z)^{2j}).  Requiring the
central slot to have exactly (k) primitive factors contributes
(P(z)^k).  Hence the generating function for words with
\(\rho(Y)=k\) is

\[
 B_k(z)={P(z)^k\over1-zC(z)^2}={P(z)^k\over2-C(z)},     \tag{5.8}
\]

where (zC(z)^2=C(z)-1).  In particular,

\[
 B_0(z)={1\over2-C(z)}.
\]

Writing (s=\sqrt{1-4z}), one has (C(z)=2/(1+s)), and therefore

\[
 B_0(z)={1+s\over2s}={1\over2\sqrt{1-4z}}+{1\over2}.   \tag{5.9}
\]

For every positive (m), the coefficient of (z^m) is (W/2), proving
(5.4).

There are (N=W-D) lower sets, so Lemma 5.1 gives

\[
                         \sum_Y\rho(Y)=N.               \tag{5.10}
\]

Since

\[
 \sum_Y(1-\rho(Y))
 =|\{\rho=0\}|-\sum_Y(\rho(Y)-1)_+=W-N=D,              \tag{5.11}
\]

equations (5.4) and (5.11) prove (5.5).

There are exactly (D) singleton chains.  Relative to the baseline
capacity of one alternate owner, each singleton can absorb at most one
additional alternate occurrence.  Thus (5.6) follows from (5.5) after
subtracting at most (D).

Deleting one interval removes its two middle incidences and can reduce the
sum of positive degree excesses by at most two.  Therefore at least half
the quantity in (5.6) must be deleted; taking the maximum with the trivial
lower bound zero gives (5.7). \(\square\)

The obstruction concerns this fixed lexical interval matching.  It does
not rule out compound rerouting of a linear number of its flags, nor does
it apply to the GMM--dummy construction of Theorem 2.1.

## 6. Final boundary

The fixed-pair proposal yields the following proved chain:

\[
 \text{GMM saturating cycle}
 \Longrightarrow
 \text{proper colour-pair factor with exactly (D) paths}
 \Longrightarrow
 \text{component cost }D=o(W/H)\quad(H=o(m)).            \tag{6.1}
\]

The only unproved estimate in this chain is

\[
 \boxed{
 N-\bigl|\{R_{i-1}\cup R_i\cup R_{i+1}:i\in\mathbb Z/N\mathbb Z\}\bigr|
 =o(W),}                                                 \tag{6.2}
\]

for a suitable GMM saturating cycle ((R_i)).  For a general fixed-pair
route, the corresponding target is the conjunction
\(h_{ab}=o(W)\) and \(c_{ab}=o(W/H)\); Theorem 2.1 makes the second
condition automatic for the particular GMM--dummy construction.  The endpoint inequality
(3.8) is a necessary capacitated Hall cut for (6.2), while Theorem 4.1 and
Theorem 5.2 eliminate two stronger but invalid shortcuts.  No argument in
this note proves (6.2).

## 7. Adversarial audit of the positive theorem

The following are the points at which the dummy augmentation could most
easily be overread.

1.  The facet SDR uses the smallness \(|{\cal E}|=D\), not merely the
    ordinary normalized-shadow inequality.  Equations (2.5)--(2.7) verify
    Hall for every subfamily of \({\cal E}\).
2.  The designated cycle neighbours are distinct because one *fixed*
    alternating perfect matching of the GMM cycle is used.  Choosing an
    arbitrary incident neighbour separately at every selected facet would
    not justify the group partition.
3.  The groups in (2.9) do not need any Boolean or inclusion structure.
    Their only role is to add one dummy incidence at every middle vertex
    and thereby regularize the bipartite graph.
4.  Restriction from \(\widetilde B_m\) deletes one edge at each middle
    vertex but none at a real lower vertex.  Hence it leaves a proper
    \(m+1\)-colouring of the nonregular real graph: every lower sees all
    colours and every middle misses exactly the colour of its dummy edge.
5.  The factor has \(D\) paths because it is literally one Hamilton cycle
    with \(D\) pairwise nonadjacent dummy vertices removed.  This is
    stronger than a component estimate obtained by abstract splicing.
6.  Only \(D\) projected edges change, so (2.2) is a support-Lipschitz
    estimate.  It gives no absolute upper-defect bound unless the original
    GMM cycle already satisfies (6.2).
7.  The Steiner obstruction concerns simultaneous perfection of every
    colour pair.  It is not a counterexample to one selected pair.
8.  The lexical lower bound (5.7) rules out sparse deletion of the fixed
    Greene--Kleitman interval matching.  A linear rerouting or a different
    symmetric-chain decomposition lies outside that conclusion.

After these scope restrictions, no unproved step remains in Theorems 1.1,
1.2, 2.1, 3.2, 4.1, 4.2, or 5.2.  The only imported existence/inequality
inputs are the GMM saturating cycle, the Lovasz--Kruskal--Katona shadow
bound, Hall's theorem, and Koenig's bipartite line-colouring theorem.
