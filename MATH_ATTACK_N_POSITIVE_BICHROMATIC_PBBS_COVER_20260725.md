# Lane N: a Catalan-cycle bichromatic cover and exact depth-one literalization

Date: 2026-07-25

No computation, finite search, or web search is used in this note.

## 1. Scope and verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\frac Wn=\operatorname {Cat}_m,
\]

\[
N=\binom n{m-1}=\frac m{m+2}W,
\qquad
\rho=W-N=\frac{2W}{m+2}.
\tag{1.1}
\]

The following positive statements are proved.

1. There is a spanning maximum-degree-two graph on the middle layer
   having exactly one Johnson edge of every rank-\((m-1)\) intersection
   colour, exactly \(\rho\) noncyclic components, and at most \(B\)
   cyclic components.
2. This graph is literally the projection of two colour classes in a
   proper \((m+2)\)-edge-colouring of a regularized lower--middle
   incidence graph. Thus the ordinary matching/flow relaxation has a
   solution with only Catalan many cycles; no probabilistic cycle-removal
   lemma is needed.
3. For \(m\ge6\), the accepted saturating-cycle theorem and one
   Kruskal--Katona Hall argument give a single Hamilton Johnson cycle on
   all \(W\) middle owners whose lower-colour loads are exactly one or two.
   This is the sharp scalar q=1 cycle-cover relaxation.
4. The full PBBS step-two factor has depth-one overload at most
   \(\rho/2<2B\). Cutting all immediate-return edges and one further edge
   from every still-intact cycle gives an explicit one-update MTF
   literalization of ranks \(m-1,m,m+1\) of length at most

   \[
   W+3\rho+3B
   =W+\left(\frac6{m+2}+\frac3{2m+1}\right)W
   <W+15B.
   \tag{1.2}
   \]

These are genuine positive depth-one theorems. They do **not** construct
an exact wreath factor. The remaining exact gate is to replace the PBBS
cycles, whose lengths are multiples of \(n\), by actual \(n\)-cycles while
changing only \(O(B)\) edges and preserving the centered-owner history.
Neither the bichromatic cover nor the MTF word is promoted to such a
factor.

The only imported input is the already audited PBBS theorem:

* the parenthesis map \(f\) is a permutation of the middle layer and its
  orbits form a spanning factor of the odd graph;
* every orbit length is \(\ell n\) for an integer \(\ell\ge1\), and the
  sum of the levels \(\ell\) is \(B\);
* for

  \[
  e_X=\{f^{-1}(X),f(X)\},
  \qquad
  \chi(X)=f^{-1}(X)\cap f(X),
  \tag{1.3}
  \]

  every \((m-1)\)-set occurs as some \(\chi(X)\), and its multiplicity is
  between one and three.

All consequences of this input are proved below.

## 2. The PBBS step-two factor has at most \(B\) cycles

Let \(P\) be one \(f\)-orbit, written

\[
v_0,v_1,\ldots,v_{L-1},\qquad L=\ell n.
\]

The centered edges on this orbit are

\[
e_{v_i}=v_{i-1}v_{i+1}.
\tag{2.1}
\]

Consequently their graph is the step-two graph on the cyclic group
\(\mathbb Z/L\mathbb Z\), and hence has exactly

\[
\gcd(2,L)=\gcd(2,\ell)
\tag{2.2}
\]

cycles. Since \(n\) is odd,

\[
\gcd(2,\ell)\le \ell
\qquad(\ell\ge1).
\tag{2.3}
\]

Summing (2.3) over all PBBS orbits and using \(\sum\ell=B\) proves the
strictly sharper bound

\[
\boxed{c(J_P)\le B}
\tag{2.4}
\]

for the number of cycles of the full PBBS step-two graph \(J_P\).
The previously recorded estimate \(2B\) loses the level information.

## 3. A complete-colour path/cycle cover

For every lower colour

\[
S\in\binom{[n]}{m-1},
\]

choose one center \(X_S\) with \(\chi(X_S)=S\), and retain the centered
edge \(e_{X_S}\). Let \(H\) be the resulting graph on the \(W\) middle
sets.

### Theorem 3.1 (Catalan-cycle complete-colour cover)

The graph \(H\) has all of the following properties.

1. It has exactly \(N\) edges.
2. Its edge-intersection colours are precisely all \((m-1)\)-sets, each
   once.
3. It is simple and has maximum degree at most two.
4. It has exactly \(\rho\) noncyclic components, where isolated vertices
   count as one-vertex paths.
5. It has at most \(B\) cyclic components.

Consequently, deleting one edge from every cyclic component produces a
spanning linear forest with at most

\[
\boxed{\rho+B<5B}
\tag{3.1}
\]

path components.

#### Proof

Different lower colours select different centers, because one center has
only one angle. Thus there are \(N\) distinct selected edges and their
colours are exactly as asserted.

The full graph \(J_P\) is two-regular: at a vertex \(Y\), its two incident
centered edges are \(e_{f(Y)}\) and \(e_{f^{-1}(Y)}\). Hence its subgraph
\(H\) has maximum degree two. A Johnson edge has a unique intersection,
so the selected graph has neither loops nor parallel edges.

Let \(p\) and \(c\) be the numbers of noncyclic and cyclic components of
\(H\). Every noncyclic maximum-degree-two component has one fewer edge
than vertices, while every cyclic component has equally many. Therefore

\[
W-N=p.
\]

This gives \(p=\rho\). Every cycle of \(H\) is a cycle of \(J_P\), so
\(c\le c(J_P)\le B\) by (2.4). Cutting one edge in every cycle leaves
\(p+c\le\rho+B\) paths. Finally,

\[
\frac\rho B=\frac{2n}{m+2}=4-\frac6{m+2}<4,
\]

which proves (3.1). \(\square\)

There is a simultaneous upper-colour fact. The endpoints of \(e_X\) are
two distinct \(m\)-subsets of \(X^c\), whose size is \(m+1\). Hence

\[
f^{-1}(X)\cup f(X)=X^c.
\tag{3.2}
\]

The selected upper colours are therefore distinct as well. There are only
\(N\) selected edges, so this statement does not by itself cover all
\(W\) upper \((m+1)\)-sets.

## 4. Exact realization as two colour classes of a regularization

Let \(\mathcal I\) be the bipartite incidence graph whose left vertices
are the middle sets \(X\in\binom{[n]}m\), whose right vertices are the
lower colours \(S\in\binom{[n]}{m-1}\), and whose edges are the
inclusions \(S\subset X\). Its degrees are

\[
d_{\mathcal I}(X)=m,
\qquad
d_{\mathcal I}(S)=m+2.
\tag{4.1}
\]

### Theorem 4.1 (bichromatic extension theorem)

There is a bipartite \((m+2)\)-regular multigraph \(\widehat{\mathcal I}\)
obtained from \(\mathcal I\) by adjoining exactly \(\rho\) dummy right
vertices, and a proper \((m+2)\)-edge-colouring of
\(\widehat{\mathcal I}\), with two colours \(\alpha,\beta\), such that
the \(\alpha\beta\)-projection at the real lower vertices is exactly the
graph \(H\) of Theorem 3.1.

In particular, the proper-colouring relaxation admits a pair with exactly
\(\rho\) path components and at most \(B\) cycle components.

#### Proof

Orient every path and cycle component of \(H\). If the edge of lower colour
\(S\) is directed from \(X\) to \(Y\), give the incidence \(S\subset X\)
colour \(\alpha\) and the incidence \(S\subset Y\) colour \(\beta\).
At each real lower vertex there is exactly one incidence of either colour.
At a middle vertex there is at most one of either colour, because the
oriented graph has indegree and outdegree at most one. Thus the
\(\alpha\)- and \(\beta\)-incidences are two disjoint matchings, each of
size \(N\), saturating all real lower vertices.

Adjoin a dummy right set \(D\) of size \(\rho=W-N\). Complete each of the
two matchings arbitrarily to a perfect matching between the \(W\) middle
vertices and the \(W=N+\rho\) real-or-dummy right vertices. Parallel dummy
edges are allowed; they are distinct edges and cause no problem in a
bipartite multigraph.

A middle vertex of degree \(d_H(X)\) has acquired \(2-d_H(X)\) dummy
edges in these two perfect matchings. Add \(d_H(X)\) further dummy edges
at \(X\). Then every middle vertex has exactly two dummy edges in total,
and hence total degree \(m+2\). The number of further dummy-edge stubs is

\[
\sum_Xd_H(X)=2N.
\tag{4.2}
\]

Every dummy vertex already has two incident edges, one in each perfect
matching, and needs \(m\) more. The required number of right stubs is

\[
m\rho
=m\frac{2W}{m+2}
=2\frac{mW}{m+2}
=2N,
\tag{4.3}
\]

so the remaining stubs can be paired arbitrarily. This constructs the
\((m+2)\)-regular multigraph and preserves all real incidence edges.

After deleting the two displayed perfect matchings, the remainder is an
\(m\)-regular bipartite multigraph. Hall's theorem supplies a perfect
matching: for a left set \(A\), regular edge counting gives
\(m|A|\le m|N(A)|\). Removing a perfect matching preserves regularity,
so induction decomposes the remainder into \(m\) perfect matchings.
Colouring them with the remaining \(m\) colours proves the theorem.
\(\square\)

The dummy vertices are a proof device. They are not middle owners, wreath
rows, or legal exact-factor packets.

### Theorem 4.2 (sharp balanced Hamilton relaxation)

Assume \(m\ge6\). There is one simple Hamilton cycle on all \(W\) middle
sets such that every rank-\((m-1)\) intersection colour has multiplicity
one or two, with exactly \(\rho\) colours of multiplicity two.

#### Proof

Use the accepted saturating-cycle theorem on the two consecutive levels
\(m-1,m\) of the Boolean lattice on \([n]\). It gives an alternating cycle

\[
X_0,S_0,X_1,S_1,\ldots,X_{N-1},S_{N-1},X_0,
\tag{4.4}
\]

where the \(S_i\)'s are all \((m-1)\)-sets and the \(X_i\)'s are distinct
middle sets. Contracting every \(S_i\) gives a simple \(N\)-cycle on the
\(X_i\)'s, and the edge \(X_iX_{i+1}\) has colour \(S_i\).

Let

\[
\mathcal U=\binom{[n]}m\setminus\{X_0,\ldots,X_{N-1}\};
\qquad |\mathcal U|=\rho.
\]

We claim that the members of \(\mathcal U\) have distinct representatives
among their \((m-1)\)-facets. For any \(\mathcal A\subseteq\mathcal U\),

\[
|\mathcal A|\le\rho\le\binom{2m-1}m.
\tag{4.5}
\]

The second inequality is equivalent to

\[
4(2m+1)\le(m+1)(m+2),
\]

or \(m^2-5m-2\ge0\), which holds for \(m\ge6\). Write
\(|\mathcal A|=\binom xm\) with real \(x\le2m-1\). The Lovasz form of
Kruskal--Katona gives

\[
|\partial\mathcal A|
\ge\binom{x}{m-1}
=\frac{m}{x-m+1}\binom xm
\ge|\mathcal A|.
\tag{4.6}
\]

Hall's theorem therefore supplies an injection

\[
g:\mathcal U\longrightarrow\binom{[n]}{m-1},
\qquad g(U)\subset U.
\tag{4.7}
\]

If \(g(U)=S_i\), subdivide the cycle edge \(X_iX_{i+1}\) by \(U\).
The three sets \(X_i,U,X_{i+1}\) are distinct \(m\)-supersets of the
same \((m-1)\)-set \(S_i\), so both new Johnson edges have intersection
exactly \(S_i\). The representatives are distinct, so distinct old edges
are subdivided, and every omitted middle set is inserted exactly once.
The resulting graph is one simple Hamilton cycle on all \(W\) middle sets.

An unmatched colour still occurs once. A matched colour loses its one old
edge and gains two new edges, so it occurs twice. There are
\(|\mathcal U|=\rho\) matched colours. \(\square\)

Equivalently, clone each matched lower slot once. Then (4.4), after these
subdivisions, is one alternating Hamilton cycle on \(W\) middle vertices
and \(W=N+\rho\) balanced lower slots.

The high-colour family \(g(\mathcal U)\) need not have the exact point
margins of a wreath factor. Thus Theorem 4.2 is a sharp scalar and Hall
relaxation, not an exact-factor theorem. The PBBS construction below is
weaker scalarly but retains centered owners and the exact point affine
slice.

## 5. Exact PBBS depth-one overload

Let

\[
a_j=\#\{S:\mu_P(S)=j\},\qquad j=1,2,3.
\]

The PBBS theorem and conservation give

\[
a_1+a_2+a_3=N,
\qquad
a_1+2a_2+3a_3=W=N+\rho,
\]

and hence

\[
a_2+2a_3=\rho.
\tag{5.1}
\]

For \(m\ge3\), the balanced depth-one floor is one and the number of
quota-two cells is exactly \(\rho\). Since there are no holes, the exact
optimal overload is

\[
O_1(P_m)=\rho-(a_2+a_3)=a_3.
\tag{5.2}
\]

Equation (5.1) yields

\[
\boxed{O_1(P_m)=a_3\le\rho/2=\frac W{m+2}<2B.}
\tag{5.3}
\]

Thus the non-wreath PBBS factor already has Catalan-scale depth-one
overload. What fails is its component length, not its lower histogram.

There is no hidden point-margin defect in this PBBS statement. In every
spanning odd-graph two-factor, let \(t_a\) be the number of factor edges
whose omitted coordinate is \(a\). Counting selected-edge endpoints which
contain \(a\) gives

\[
W-t_a=2\binom{n-1}{m-1}=(n-1)B,
\]

and hence

\[
t_a=B.
\tag{5.4}
\]

At a center \(X\), its angle is

\[
\chi(X)=X^c\setminus\{\lambda_1(X),\lambda_2(X)\},
\]

where \(\lambda_1,\lambda_2\) are the omitted labels of its two incident
odd edges. Therefore, for every coordinate \(a\),

\[
\sum_{S\ni a}\mu_P(S)
=\binom{n-1}m-2t_a
=(m+1)B-2B
=(m-1)B.
\tag{5.5}
\]

This is exactly the wreath lower-shadow point margin. Theorem 4.2 does not
automatically have (5.5).

## 6. A self-contained depth-one path literalization

The next lemma is stated for an arbitrary ground-set size. It is the
\(H=1\) instance of the audited one-update MTF construction.

### Lemma 6.1 (one-update path word)

Let

\[
T_0,T_1,\ldots,T_{K-1}
\]

be a Johnson path of \(m\)-sets, with

\[
T_{i+1}=T_i-\{p_i\}+\{q_i\}.
\tag{6.1}
\]

Prescribe an incoming coordinate \(u\notin T_0\) and a terminal departure
\(v\in T_{K-1}\). Assume

\[
q_i\ne p_{i+1}\qquad(0\le i\le K-3),
\tag{6.2}
\]

and, when \(K\ge2\), assume that \(v\in T_{K-2}\). Put

\[
p_{K-1}=v,
\qquad
L_i=T_i-\{p_i\}.
\tag{6.3}
\]

Then there is a literal contiguous-OR word of exactly \(K+3\) entries
which exposes every middle set \(T_i\), every internal intersection and
union, the terminal lower set \(T_{K-1}-v\), and the initial upper set
\(T_0+u\).

#### Proof

At the initial state use the ordered partition

\[
\Pi_0=(L_0,\{p_0\},\{u\},R_0),
\tag{6.4}
\]

where \(R_0\) is the residual block. For \(i\ge1\), use

\[
\Pi_i=(L_i,\{p_i\},\{p_{i-1}\},R_i),
\tag{6.5}
\]

deleting empty residual blocks. Condition (6.2) says
\(p_{i+1}\in L_i\). Direct block subtraction then gives

\[
\Pi_{i+1}=M_{L_{i+1}}(\Pi_i),
\tag{6.6}
\]

where \(M_A\) moves the elements of \(A\) to the first block and preserves
the residual block order. The statement remains true when
\(q_i=p_{i-1}\): that coordinate is simply extracted from the displayed
upper singleton.

Write the four blocks of \(\Pi_0\) in reverse order and then append
\(L_1,\ldots,L_{K-1}\). This uses \(4+(K-1)=K+3\) entries. The current
suffix blocks are exactly \(\Pi_i\), so their prefix unions expose

\[
L_i,\qquad T_i=L_i+\{p_i\},
\]

and, for \(i\ge1\),

\[
T_i+\{p_{i-1}\}=T_{i-1}\cup T_i.
\]

At \(i=0\) the corresponding upper prefix is \(T_0+u\); at the terminal
state the lower prefix is \(T_{K-1}-v\). This proves the claim. \(\square\)

The case \(K=1\) uses the single state

\[
(T_0-v,\{v\},\{u\},R)
\]

and requires only \(u\ne v\), which follows from
\(u\notin T_0\), \(v\in T_0\).

## 7. A complete three-rank literal word from PBBS

Orient every cycle of the full PBBS step-two factor \(J_P\). Along an
oriented Johnson cycle write

\[
T_{i+1}=T_i-\{p_i\}+\{q_i\}.
\]

An immediate positive return occurs at \(i\) precisely when

\[
q_i=p_{i+1}.
\tag{7.1}
\]

But (7.1) is equivalent to equality of the two consecutive lower colours:

\[
T_i\cap T_{i+1}
=T_{i+1}-\{q_i\}
=T_{i+1}-\{p_{i+1}\}
=T_{i+1}\cap T_{i+2}.
\tag{7.2}
\]

Let \(R\) be the total number of such cyclic adjacent equalities.

### Lemma 7.1 (exact immediate-return bound)

\[
\boxed{R\le\rho.}
\tag{7.3}
\]

#### Proof

Fix a lower colour \(S\). Its occurrences in the disjoint cycle family
form proper cyclic runs. No whole step-two cycle can have colour \(S\):
every such cycle has length at least \(n\ge5\), whereas
\(\mu_P(S)\le3\). A run of \(k\) occurrences therefore contributes
exactly \(k-1\) adjacent equalities. Summing over the runs of \(S\) gives
at most \(\mu_P(S)-1\). Hence

\[
R\le\sum_S(\mu_P(S)-1)=W-N=\rho,
\]

using complete support. \(\square\)

Cut the entry edge of every immediate return. In every cycle untouched by
these cuts, cut one arbitrary edge. If \(d\) is the total number of cuts,
then by (2.4) and (7.3)

\[
\boxed{d\le R+c(J_P)\le\rho+B.}
\tag{7.4}
\]

The cut cycles become exactly \(d\) paths, counting singleton paths caused
by adjacent cuts. Every resulting path satisfies (6.2). At a cut edge

\[
T\longrightarrow T'=T-\{p\}+\{q\},
\]

prescribe \(p\) as the initial upper coordinate on the path beginning at
\(T'\), and as the terminal departure on the path ending at \(T\).
If the preceding edge is retained, the terminal legality
\(p\in T_{K-2}\) follows because otherwise that preceding edge would be
another immediate-return entry and would also have been cut. Adjacent cuts
give the separately covered \(K=1\) case of Lemma 6.1.

Every retained edge has its intersection and union exposed internally.
Every deleted edge has its intersection exposed by the terminal lower
prefix and its union exposed by the initial upper prefix. Thus all PBBS
edge colours survive. The lower support is the complete rank-\((m-1)\)
layer by the PBBS theorem. The upper colour of the edge centered at \(X\)
is \(X^c\) by (3.2), so the upper colours are all \(W\) rank-\((m+1)\)
sets exactly once. The middle vertices are all \(W\) middle sets.

Summing the exact \(K+3\) length of Lemma 6.1 over the \(d\) paths gives:

### Theorem 7.2 (PBBS three-rank literalization)

For every \(m\ge2\), there is a literal contiguous-OR word covering every
set in the three ranks

\[
m-1,\quad m,\quad m+1
\]

whose length is at most

\[
\boxed{
W+3(\rho+B)
=W+\left(\frac6{m+2}+\frac3{2m+1}\right)W
<W+15B.}
\tag{7.5}
\]

This construction uses one coherent PBBS history and literal MTF states;
it is not a fractional or independently rankwise object.

## 8. The exact unresolved packetization gate

Theorems 3.1 and 4.1 settle the coloured cycle-cover relaxation with an
\(O(B)=o(W)\) component toll. Theorem 7.2 settles the corresponding
three-rank literal word directly. Neither theorem gives an adaptive
orientation inside one exact wreath factor.

The missing conversion is the following precise statement.

> **PBBS-to-wreath conversion gate.** Replace the PBBS odd-graph factor by
> a spanning factor all of whose components have length exactly
> \(n=2m+1\), changing \(O(B)\) odd edges (equivalently \(O(B)\) centered
> histories, up to an absolute factor of two), while retaining all but
> \(O(B)\) PBBS first-angle
> occurrences.

Every odd-graph \(n\)-cycle is a genuine wreath, so this gate would produce
an exact factor with

\[
O_1=O(B)=o(W).
\]

The centered owner cannot be discarded during the conversion: an arbitrary
Johnson two-factor or the dummy regularization need not satisfy reciprocal
odd adjacency, and cycles of the wrong length are not wreath packets.

The known owner-phase theorem shows why unchanged long PBBS segments alone
cannot finish the conversion. Inside a level-\(\ell>1\) PBBS component,
every common path with an exact wreath factor has at most \(m\) retained
centered edges. Thus a level-\(\ell\) component of step-two length \(L\)
requires at least

\[
\left\lceil\frac{L}{m+1}\right\rceil
\tag{8.1}
\]

removed PBBS edges: if \(t\) edges are removed, the \(L-t\) retained edges
lie in at most \(t\) paths, each of length at most \(m\), so
\(L-t\le mt\). This is only a Catalan-scale lower bound after summation;
it is compatible with the desired \(O(B)\) conversion and is not a no-go.

No theorem here constructs the required reciprocal sewing, controls its
component lengths, or proves that a suitable distant exact factor exists.
That is the exact proved/conditional boundary.
