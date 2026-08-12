# The fixed-`M0` rooted-arc tensor is a biregular rainbow-matching problem

Date: 2026-08-01  
Lane: Thread D / upper-tail-head correlation  
Status: exact equivalence, exact degrees, unconditional fractional min--max,
and a sharp abstract integral counterexample.  Existence of a full rainbow
matching for every Boolean `M0` remains open here; graphic acyclicity is a
strictly later condition.

## 0. Outcome

Fix a perfect matching `M0` between ranks `m-1` and `m` of `[2m-1]`.
The upper-exact incidence-matching gate is precisely a rainbow matching
which saturates every upper colour in one edge-coloured bipartite graph.
Equivalently it is a matching saturating the colour shore of a three-partite
three-uniform hypergraph.

The tensor has exact degrees

\[
 d_{\rm tail}=d_{\rm head}=m-1,
 \qquad d_{\rm colour}=m+1.                            \tag{0.1}
\]

Consequently the constant weight `1/(m+1)` is an exact fractional matching
saturating all upper colours, with tail and head load

\[
                         {m-1\over m+1}<1.              \tag{0.2}
\]

Even more, for every nonempty set `S` of colours, the ordinary bipartite
graph formed by those colour classes has matching number at least

\[
            \left\lceil {m+1\over m-1}|S|\right\rceil
                 \ge |S|+1.                            \tag{0.3}
\]

Thus every scalar Hall/matching-rank cut has strict slack.  This still does
not prove an integral rainbow matching: rainbow matching is an intersection
of three partition constraints, not a bipartite matching or two-matroid
intersection.  A six-edge coloured cycle gives fractional optimum three and
integral optimum two while satisfying every natural union-matching Hall
inequality.

For the actual Boolean tensor, (0.1)--(0.3) remove fractional feasibility
and marginal Hall as obstructions.  They neither prove nor refute the
remaining integral correlation.  Even a positive rainbow matching supplies
only an upper-exact incidence matching; the rooted links must additionally
be selected acyclic to obtain a Catalan forest.

## 1. The three-partite rooted-arc tensor

Put

\[
 \mathcal L={{[2m-1]}\choose {m-1}},\qquad
 \mathcal O={{[2m-1]}\choose m},\qquad
 \mathcal U={{[2m-1]}\choose {m+1}},                  \tag{1.1}
\]

and

\[
 W=|\mathcal L|=|\mathcal O|,qquad U=|\mathcal U|,
 \qquad {U\over W}={m-1\over m+1}.                    \tag{1.2}
\]

Use two copies `A,B` of `mathcal O`.  A vertex `T in A` is a rooted tail;
write

\[
                         L(T)=M_0^{-1}(T).              \tag{1.3}
\]

For every `R in mathcal U` and every facet `T subset R`, let `b` be the
unique member of `R-T` and put

\[
                 V(R,T)=L(T)\cup\{b\}\in\mathcal O.   \tag{1.4}
\]

Since `L(T) subset T` and `b notin T`, the incidence

\[
             L(T)\ --\ V(R,T)                         \tag{1.5}
\]

lies outside `M0`, and

\[
             M_0(L(T))\cup V(R,T)=T\cup V(R,T)=R.     \tag{1.6}
\]

Define the three-partite hypergraph `mathcal H(M0)` on `A,B,mathcal U` by

\[
                    \{T,V(R,T),R\}\in E(\mathcal H). \tag{1.7}
\]

Equivalently, define a bipartite graph `G(M0)` from `A` to `B`, put in the
edge `T V(R,T)`, and colour it by `R`.  For a fixed pair `(R,T)` there is
exactly one such edge.

## 2. Exact degrees and codegrees

### Theorem 2.1 (biregular degree ledger)

The tensor `mathcal H(M0)` satisfies:

1. every tail has degree `m-1`;
2. every head has degree `m-1`;
3. every upper colour has degree `m+1`;
4. tail--head and tail--colour codegrees are at most one; and
5. for a head `V` and a colour `R`,

   \[
   d(V,R)=0\quad\hbox{unless }V\subset R,              \tag{2.1}
   \]

   while for `R=V union {b}`,

   \[
   d(V,R)=\#\{a\in V:
       M_0(V-\{a\})=(V-\{a\})\cup\{b\}\},            \tag{2.2}
   \]

   with the unique lower facet matched by `M0` to `V` omitted.  Hence
   `0<=d(V,R)<=m-1`, and these codegrees sum to `m-1` over the colours
   containing `V`.

#### Proof

A tail `T` lies in exactly `m-1` upper `(m+1)`-sets, and (1.4) gives one
edge for each.  A head owner `V` contains `m` lower facets; one is
`M0^{-1}(V)` and produces the forbidden matching edge, while every other
facet produces exactly one incoming rooted arc.  Thus both endpoint degrees
are `m-1`.

For a fixed colour `R`, its `m+1` facets `T` each give one edge by (1.4).
Conversely every edge of colour `R` has one of those facets as its rooted
tail, so the colour degree is exactly `m+1`.

The construction makes the tail--colour pair unique.  A tail and head
determine at most one physical incidence and its colour, proving the other
unit codegree.  Finally an incoming edge to `V` has lower facet `V-{a}`.
It has colour `V union {b}` precisely under (2.2), proving the last row.
\(\square\)

In particular

\[
 |E(\mathcal H)|=W(m-1)=U(m+1).                        \tag{2.3}
\]

The head--colour codegree is the asymmetric entry: it can exceed one.  At
`m=3`, the explicit rooted table in
`MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md`
already has two distinct tails entering the same head with colour `1234`.

## 3. Exact rainbow-matching equivalence

### Theorem 3.1

The following objects are equivalent.

1. An incidence matching `Q0 subset ML_m-M0` containing exactly one edge
   of every immediate-upper colour.
2. A matching in `G(M0)` containing exactly one edge of every colour.
3. A hypergraph matching in `mathcal H(M0)` saturating the colour part
   `mathcal U`.

#### Proof

The identification (1.3)--(1.6) is bijective on physical incidences outside
`M0`.  Distinct lower endpoints are exactly distinct rooted tails; distinct
middle endpoints are exactly distinct heads; and (1.6) identifies the upper
colour.  Hence the matching and colour conditions agree in all three
languages.  \(\square\)

A protected ticket `(R,T)` forces the single hyperedge (1.7).  Thus the
head-collision example with two protected tickets is a literal obstruction
to extending an arbitrary prescribed upper-tail semimatching.

Theorem 3.1 does **not** contain the graphic row.  Under the rooted
identification, the selected links are the directed edges `T->V`.  A rooted
Catalan forest requires their underlying labelled graph to be acyclic in
addition to the rainbow-matching conditions.

## 4. Fractional min--max and automatic marginal Hall

Let `x_e>=0`.  The fractional rainbow-matching relaxation is

\[
\begin{aligned}
 \max\quad&\sum_e x_e\\
 \text{subject to}\quad
 &\sum_{e\ni T}x_e\le1 &&(T\in A),\\
 &\sum_{e\ni V}x_e\le1 &&(V\in B),\\
 &\sum_{e:\,c(e)=R}x_e\le1 &&(R\in\mathcal U).
                                                               \tag{4.1}
\end{aligned}
\]

Its exact LP dual is the fractional three-partite vertex cover

\[
\begin{aligned}
 \min\quad&\sum_T\alpha_T+\sum_V\beta_V+\sum_R\gamma_R\\
 \text{subject to}\quad
 &\alpha_T+\beta_V+\gamma_R\ge1
   &&(\{T,V,R\}\in E(\mathcal H)),\\
 &\alpha,\beta,\gamma\ge0.                              \tag{4.2}
\end{aligned}
\]

### Proposition 4.1

Both programs have optimum `U`.  The primal optimum is attained by

\[
                              x_e={1\over m+1},          \tag{4.3}
\]

and the dual optimum by `gamma_R=1` for every colour and all other weights
zero.

#### Proof

By Theorem 2.1, (4.3) gives colour load one and endpoint load
`(m-1)/(m+1)`.  Its total weight is `|E|/(m+1)=U`.  The colour constraints
upper-bound every feasible objective by `U`, and the displayed dual has
weight `U`.  \(\square\)

There is also strict ordinary matching slack.  For `S subset mathcal U`,
let `G[S]` be the union of its colour classes.  It has `(m+1)|S|` edges and
maximum degree at most `m-1`.  By the bipartite edge-colouring theorem its
edges split into at most `m-1` matchings.  Therefore

\[
 \nu(G[S])\ge
  \left\lceil{(m+1)|S|\over m-1}\right\rceil.          \tag{4.4}
\]

For every nonempty `S`, the right side is at least `|S|+1`.  Hence the
necessary family

\[
                            \nu(G[S])\ge|S|             \tag{4.5}
\]

is automatic, with strict slack, for every fixed `M0`.

## 5. Why this is not an integral min--max theorem

Condition (4.5) is not sufficient for a rainbow matching in a general
edge-coloured bipartite graph.  Let the two shores be

\[
 A=\{a_1,a_2,a_3\},\qquad B=\{b_1,b_2,b_3\},           \tag{5.1}
\]

and colour the six-cycle by

\[
\begin{array}{c|cc}
 \text{red}&a_1b_1&a_2b_2\\
 \text{blue}&a_3b_3&a_1b_2\\
 \text{green}&a_2b_3&a_3b_1.
\end{array}                                             \tag{5.2}
\]

Every one- or two-colour union has a matching of the required size, and the
whole six-cycle has a perfect matching.  Thus (4.5) holds for every colour
set.  However the cycle has only two perfect matchings:

\[
 \{a_1b_1,a_2b_2,a_3b_3\}
 \quad\hbox{and}\quad
 \{a_1b_2,a_2b_3,a_3b_1\};                             \tag{5.3}
\]

their colour multisets are respectively `red,red,blue` and
`blue,green,green`.  Hence there is no rainbow matching of size three.

Putting weight `1/2` on every edge gives one unit at every vertex and every
colour.  Thus the fractional optimum is three while the integral rainbow
matching number is two.  This is the smallest alternating-cycle form of the
determinant-two obstruction: adding the colour partition to the two endpoint
partition constraints destroys total unimodularity and König min--max.

This example is abstract; it does not have the Boolean degree profile
(0.1).  Its role is to refute the inference that the marginal inequalities
(4.5), or the fractional point alone, form an integral theorem.  The degree
profile (0.1) gives extra structure, but no proof here turns that structure
into integrality.

## 6. Exact surviving gate

For a fixed Boolean `M0`, the strongest conclusions proved here are:

1. the upper-exact incidence problem is exactly the colour-saturating
   rainbow matching of Theorem 3.1;
2. all fractional and ordinary union-matching Hall obstructions vanish by
   Proposition 4.1 and (4.4); and
3. arbitrary protected upper-tail tickets can still fail immediately by a
   head collision, as in the explicit `m=3` two-ticket example.

Accordingly one needs either:

* a Boolean-specific integral rainbow-matching theorem for every admissible
  correlated `M0`;
* a joint choice theorem for `M0` and the rainbow representatives; or
* an actual Boolean `M0` with integral rainbow deficiency.

No such all-dimensional theorem or counterexample is proved here.  Even a
positive answer leaves the Catalan graphic-forest and subsequent port-path
conditions untouched.
