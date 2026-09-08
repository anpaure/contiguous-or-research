# Ribbon incidence, exact punctured-wreath grouping, and the co-design gate

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** exact profiles and exact reduction proved; the correlated
grouping/matching theorem remains open

## 0. Outcome

Put

\[
 b=2r+1,\qquad
 \mathcal M=\binom{[b]}r,\qquad
 \mathcal L=\binom{[b]}{r-1},\qquad
 N=|\mathcal M|.
\tag{0.1}
\]

Throughout, \(r\ge2\).

A **ribbon** is the unordered pair of flagged endpoints

\[
 R=\{(X,S),(Y,T)\},
 \qquad
 X,Y\in\mathcal M,\quad X\cap Y=\varnothing,\quad
 S\in\binom X{r-1},\quad T\in\binom Y{r-1}.
\tag{0.2}
\]

Equivalently, it is the four-target incidence edge
\(\{X,Y,S,T\}\), with the containments remembering which lower target is
attached to which middle target.

There are two exact hypergraphs.

1. The target-incidence hypergraph \(\mathcal A_r\) is the \(4\)-graph on
   \(\mathcal M\sqcup\mathcal L\) whose edges are the ribbons.  It has

   \[
   \begin{aligned}
   |E(\mathcal A_r)|&={N r^2(r+1)\over2},\\
   d_{\mathcal M}&=r^2(r+1),\\
   d_{\mathcal L}&=r(r+1)(r+2),\\
   \Delta_2(\mathcal A_r)&=r(r+1).
   \end{aligned}
   \tag{0.3}
   \]

   Since the rank is fixed, the two degrees have ratio \(1+O(1/r)\), and
   \(\Delta_2/d_{\mathcal M}=1/r\), the standard fixed-rank nibble gives a
   matching \(P\subseteq E(\mathcal A_r)\) with

   \[
             |P|={|\mathcal L|\over2}-o(N).
   \tag{0.4}
   \]

   Thus abstractly one can match almost every lower target and all but
   \(o(N)\) middle targets.

2. The grouping hypergraph \(\mathcal G_r\) has the ribbons as vertices.
   A directed punctured wreath groups its \(2r\) clean middle windows, and
   their attached lower-prefix windows, into \(r\) ribbons.  Then

   \[
   \begin{aligned}
   |E(\mathcal G_r)|&=b!,\\
   D:=d_{\mathcal G_r}(R)&=2r!(r-1)!,\\
   \Delta_t(\mathcal G_r)
      &=(r-t+1)((r-t)!)^2\qquad(2\le t\le r).
   \end{aligned}
   \tag{0.5}
   \]

   In particular,

   \[
     \Delta_2=(r-1)((r-2)!)^2,
     \qquad
     {r\Delta_2\over D}={1\over2(r-1)}.
   \tag{0.6}
   \]

   More generally, if each endpoint flag remembers the nested same-start
   prefixes through depth \(H\), then

   \[
   D_H=2r((r-H)!)^2,
   \qquad
   \Delta_t^{(H)}
     =(r-t+1)((r-H-t+1)!)^2
   \tag{0.6a}
   \]

   for \(1\le H\le r-1\) and \(2\le t\le r-H+1\).  In particular,
   \(r\Delta_2^{(H)}/D_H=(r-1)/(2(r-H)^2)=o(1)\) uniformly for
   \(H=o(r)\).

The two positive statements do not compose independently.  A uniformly
random ribbon set of the maximum relevant size has expected number of
complete grouping edges

\[
 b!\,{(m)_r\over(|V(\mathcal G_r)|)_r}=o(1).
\tag{0.7}
\]

Thus even before target-disjointness, an independent ribbon selection
almost surely contains no punctured wreath at all.

The exact remaining co-design theorem is:

> Find a matching \(P\) in \(\mathcal A_r\) satisfying (0.4) such that
> \(\mathcal G_r[P]\) has a matching covering \(|P|-o(N)\) ribbon
> vertices.

This condition is exactly equivalent to a target-disjoint family of
directed punctured wreaths covering all but \(o(N)\) middle and first-shadow
targets.

At the fractional level the co-design is already exact: common weight
\([2(r+2)r!(r+1)!]^{-1}\) on every directed configuration saturates every
lower target, loads every middle target by \(r/(r+2)\), and has the optimal
total mass \(N/[2(r+2)]\).  The unsolved content is integral correlated
rounding of this symmetric point.

A grouping factor does not make a black-box nibble automatic.  If a perfect
matching \(\mathcal F\) of \(\mathcal G_r\) partitions all ribbons and one
forms its quotient \(4r\)-graph on the actual targets, then its degrees are
exactly the two values in (0.3), but every such quotient has

\[
 \Delta_2\ge r(r+1),
 \qquad
 {4r\Delta_2\over d_{\mathcal M}}\ge4.
\tag{0.8}
\]

The floor is forced by pairs \(S\subset X\), not by a poor choice of factor.
A randomized or structured factor may still succeed through additional
geometry, but it cannot cross the naive growing-rank
\(k\Delta_2/D=o(1)\) gate.

## 1. The four-target incidence hypergraph

The number of middle targets is \(N\), and

\[
               |\mathcal L|=\binom b{r-1}={r\over r+2}N.
\tag{1.1}
\]

There are \(N(r+1)/2\) unordered disjoint pairs \(\{X,Y\}\) in the odd
graph.  Each endpoint has \(r\) lower facets, so

\[
                     |E(\mathcal A_r)|={Nr^2(r+1)\over2}.
\tag{1.2}
\]

### Lemma 1.1 (degrees)

Every \(X\in\mathcal M\) has degree \(r^2(r+1)\), and every
\(S\in\mathcal L\) has degree \(r(r+1)(r+2)\).

#### Proof

For fixed \(X\), choose the disjoint endpoint \(Y\) in \(r+1\) ways and
then choose the two lower facets in \(r^2\) ways.

For fixed \(S\), its attached middle endpoint is \(X=S\cup\{x\}\), with
\(r+2\) choices for \(x\).  Choose a disjoint \(Y\) in \(r+1\) ways and
its lower facet in \(r\) ways.  The attachment is unique because two
disjoint \(r\)-sets cannot both contain the nonempty \((r-1)\)-set \(S\).
\(\square\)

### Lemma 1.2 (complete pair-codegree table)

For distinct target vertices, the nonzero codegrees are

\[
\begin{array}{c|c|c}
\text{types}&\text{condition}&\text{codegree}\\ \hline
\mathcal M,\mathcal M&X\cap Y=\varnothing&r^2\\
\mathcal M,\mathcal L&S\subset X&r(r+1)\\
\mathcal M,\mathcal L&S\cap X=\varnothing&2r\\
\mathcal L,\mathcal L&S\cap T=\varnothing&6.
\end{array}
\tag{1.3}
\]

All other pair codegrees vanish.  Hence, for every \(r\ge2\),

\[
                         \Delta_2(\mathcal A_r)=r(r+1).
\tag{1.4}
\]

#### Proof

For a disjoint middle pair, choose its two facets in \(r^2\) ways.

If \(S\subset X\), choose the other middle endpoint in \(r+1\) ways and
its facet in \(r\) ways.  If instead \(S\cap X=\varnothing\), the middle
endpoint containing \(S\) is obtained by adding one of the two elements of
\([b]\setminus(X\cup S)\), and the facet at \(X\) has \(r\) choices.

Finally, two lower targets must attach to disjoint middle endpoints, so they
must be disjoint.  If they are disjoint, their union leaves three
coordinates.  Choose distinct added coordinates for the two endpoints in
\(3\cdot2=6\) ways.  This proves the table. \(\square\)

### Corollary 1.3 (abstract near-perfect matching)

There is a matching \(P\) in \(\mathcal A_r\) for which

\[
 |\mathcal L\setminus V(P)|=o(N),
 \qquad
 |\mathcal M\setminus V(P)|={2N\over r+2}+o(N)=o(N).
\tag{1.5}
\]

#### Proof

Use \(D=r^2(r+1)\).  Lemmas 1.1--1.2 give every degree
\((1+O(1/r))D\) and maximum codegree \(D/r\).  The uniformity is the fixed
value four, so Pippenger's fixed-uniformity nearly-regular low-codegree
matching theorem gives a matching leaving
\(o(|\mathcal M|+|\mathcal L|)=o(N)\) vertices.  Each ribbon covers two
targets from each class.  Therefore its size is
\(|\mathcal L|/2-o(N)\), which gives (1.5) using (1.1). \(\square\)

This corollary is deliberately abstract: it does not say that the selected
ribbons can be grouped into physical wreaths.

## 2. Directed punctured wreaths

Index a directed punctured wreath by a linear permutation

\[
                         w=(w_0,w_1,\ldots,w_{2r}).
\tag{2.1}
\]

The linear origin is the dirty start.  For \(i\in\mathbb Z_b\), put

\[
 M_i=\{w_i,w_{i+1},\ldots,w_{i+r-1}\},
 \qquad
 L_i=\{w_i,w_{i+1},\ldots,w_{i+r-2}\},
\tag{2.2}
\]

with cyclic indices.  Delete \(M_0\), and for \(1\le k\le r\) form

\[
 R_k(w)=
 \{(M_k,L_k),(M_{k+r},L_{k+r})\}.
\tag{2.3}
\]

The \(2r\) middle targets and the \(2r\) lower targets in (2.3) are all
distinct.  Thus

\[
                         G(w)=\{R_1(w),\ldots,R_r(w)\}
\tag{2.4}
\]

is an \(r\)-set of ribbon vertices.

### Lemma 2.1 (configuration reconstruction)

The map \(w\mapsto G(w)\) is injective.  Hence \(\mathcal G_r\) is a
simple \(r\)-graph with exactly \(b!\) edges.

#### Proof

For a ribbon \(R=\{(X,S),(Y,T)\}\), its three intrinsic singleton labels
are the unused coordinate

\[
 z(R)=[b]\setminus(X\cup Y)
\tag{2.5}
\]

and the two unordered flag differences \(X\setminus S\),
\(Y\setminus T\).  In the group (2.4), write these for \(R_k\) as

\[
 \begin{aligned}
 z_k&=w_{k-1},\\
 x_k&=w_{k+r-1},\\
 y_k&=w_{k-2}\quad\text{(indices modulo }b\text{)}.
 \end{aligned}
\tag{2.6}
\]

Among the ribbons of the group, the relation

\[
 z(R)\in\{X'\setminus S',Y'\setminus T'\}
\tag{2.7}
\]

holds exactly for the consecutive pairs
\(R_k\to R_{k+1}\), \(1\le k<r\): it is the equality
\(z_k=y_{k+1}\).  Indeed, the \(z_k\)'s are
\(w_0,\ldots,w_{r-1}\), the \(x_k\)'s are
\(w_r,\ldots,w_{2r-1}\), and the \(y_k\)'s are
\(w_{2r},w_0,\ldots,w_{r-2}\).  Thus (2.7) recovers the directed path

\[
                         R_1\to R_2\to\cdots\to R_r.
\tag{2.8}
\]

For \(k\ge2\), the incoming equality identifies \(y_k\), hence also
\(x_k\) and the two endpoint flags.  It orients \(R_2\).  The orientation
of \(R_1\) is then unique: in the correct naming,

\[
 |X_1\cap X_2|+|Y_1\cap Y_2|=2(r-1),
\tag{2.9}
\]

whereas swapping the two endpoint flags of \(R_1\) gives total overlap
one.  Finally (2.6) recovers

\[
 \begin{aligned}
 (w_0,\ldots,w_{r-1})&=(z_1,\ldots,z_r),\\
 (w_r,\ldots,w_{2r-1})&=(x_1,\ldots,x_r),\\
 w_{2r}&=y_1.
 \end{aligned}
\tag{2.10}

Thus the group determines \(w\) uniquely. \(\square\)

## 3. Exact grouping degrees and all maximum codegrees

### Lemma 3.1 (ribbon degree)

Every ribbon belongs to exactly

\[
                         D=2r!(r-1)!
\tag{3.1}
\]

directed punctured-wreath groups.

#### Proof

Fix \(R=\{(X,S),(Y,T)\}\), and write
\(x=X\setminus S\), \(y=Y\setminus T\), and
\(z=[b]\setminus(X\cup Y)\).  Choose which endpoint flag comes first in
two ways, order the elements of its lower facet in \((r-1)!\) ways, order
the other lower facet in \((r-1)!\) ways, and choose the position
\(k\in[r]\) of the ribbon relative to the dirty start.  Relative to the
ribbon start, the word is

\[
              (\text{an order of }S,\ x,
               \text{an order of }T,\ y,\ z).
\tag{3.2}
\]

These choices give \(2r((r-1)!)^2=2r!(r-1)!\) configurations, and
Lemma 2.1 shows that their grouping edges are distinct. \(\square\)

For the higher codegrees, the following exact refinement is useful.

### Lemma 3.2 (gap formula)

Let \(\mathcal U\) be a set of \(t\ge2\) distinct ribbons which occurs in
one grouping edge.  Their positions and direction are intrinsic.  Write

\[
 1\le k_1<\cdots<k_t\le r,
 \qquad d_j=k_{j+1}-k_j,
 \qquad u=r-\sum_{j=1}^{t-1}d_j.
\tag{3.3}
\]

Then the number of grouping edges containing \(\mathcal U\) is

\[
 \boxed{
 \lambda(\mathcal U)
  =u((u-1)!)^2
    \prod_{\substack{1\le j<t\\ d_j\ge2}}
       (d_j-2)!(d_j-1)!.}
\tag{3.4}
\]

#### Proof

Anchor the first ribbon and use its oriented normal form

\[
 (s_1,\ldots,s_{r-1},x,
  t_1,\ldots,t_{r-1},y,z).
\tag{3.5}
\]

For a second ribbon at positive offset \(d\), direct comparison of its two
middle sets, two attached facets, unused coordinate, and flag differences
recovers both the direction and the offset.  Explicitly, after the unique
consistent endpoint naming, its middle-intersection matrix with the anchor
is

\[
 \begin{pmatrix}
 r-d&d-1\\ d&r-d
 \end{pmatrix},
\tag{3.6}
\]

and its unused and two flag-difference coordinates occur at
\(s_d,t_d,s_{d-1}\), with \(s_0:=z\).  These boundary labels resolve the
possible numerical ties in (3.6).  Applying this to every pair with the
anchor recovers the ordered positions in (3.3).

Between two selected positions at gap \(d_j\ge2\), the first bank has
\(d_j-2\) freely ordered interior labels and the second bank has
\(d_j-1\).  After the last selected position, each bank has \(u-1\)
freely ordered labels.  Finally the whole position pattern may be translated
inside \([r]\) in exactly \(u\) ways.  Multiplying the independent block
orders and translations gives (3.4). \(\square\)

### Theorem 3.3 (maximum \(t\)-codegrees)

For every \(2\le t\le r\),

\[
 \boxed{
 \Delta_t(\mathcal G_r)
   =(r-t+1)((r-t)!)^2.}
\tag{3.7}
\]

Equality is attained by any \(t\) consecutive ribbons of a configuration.

#### Proof

Put \(e_j=d_j-1\ge0\), \(E=\sum e_j\), and \(n=r-t\).  Then
\(u=n+1-E\).  The two products of free-block factorials in (3.4) are each
at most \(n!\): their block sizes sum to at most \(n\).  Also
\(u\le n+1\).  Hence (3.4) is at most
\((n+1)(n!)^2\).  If every gap equals one, then \(E=0\), \(u=n+1\), and
all the gap factors are empty, so equality holds. \(\square\)

Equations (3.1) and (3.7) give (0.6).  They also show that the uniform
weight \(1/D\) on every grouping edge is an exact fractional perfect
matching of \(\mathcal G_r\).  No integral grouping factor is asserted.

## 3A. Mesoscopic nested flags

Fix \(1\le H\le r-1\).  A depth-\(H\) endpoint flag is

\[
 \left(M_i;
 L_i^{(1)},L_i^{(2)},\ldots,L_i^{(H)}\right),
 \qquad
 L_i^{(q)}=\{w_i,\ldots,w_{i+r-q-1}\}.
\tag{3A.1}
\]

Thus the flag remembers the nested same-start prefixes of ranks
\(r-1,\ldots,r-H\), equivalently the ordered last \(H\) labels of the
rank-\(r\) window.  Pair the two flags at starts \(k\) and \(k+r\), as in
(2.3), to obtain a depth-\(H\) ribbon.  Let
\(\mathcal G_{r,H}\) be the grouping hypergraph on these ribbons, and write
\((r)_H=r!/(r-H)!\).

### Theorem 3A.1 (nested grouping profile)

The hypergraph \(\mathcal G_{r,H}\) is simple, has \(b!\) grouping edges,
and has

\[
 \begin{aligned}
 |V(\mathcal G_{r,H})|
   &={N(r+1)\over2}(r)_H^2,\\
 D_H
   &=2r((r-H)!)^2.
 \end{aligned}
\tag{3A.2}
\]

For every \(2\le t\le r-H+1\),

\[
 \boxed{
 \Delta_t(\mathcal G_{r,H})
   =(r-t+1)((r-H-t+1)!)^2.}
\tag{3A.3}
\]

The maximum is attained by \(t\) consecutive ribbons.

#### Proof

For a fixed disjoint middle pair, a depth-\(H\) flag at either endpoint is
specified by an ordered \(H\)-tuple of distinct deleted suffix labels.
This gives \((r)_H^2\) ribbons per unordered Kneser edge and proves the
vertex count.

Forgetting all but the first facet sends every depth-\(H\) grouping edge to
the depth-one grouping edge in Section 2.  Lemma 2.1 therefore proves
simplicity and the count \(b!\).

Fix a depth-\(H\) ribbon.  After choosing its endpoint orientation, the
ordered \(H\)-label suffix at each endpoint is fixed.  The two remaining
prefix cores have size \(r-H\) and may be ordered independently.  Choosing
the ribbon position relative to the dirty start gives

\[
                 2r((r-H)!)^2
\]

distinct configurations, proving the degree formula.

Now fix \(t\ge2\) compatible depth-\(H\) ribbons.  Their depth-one
projections recover their direction and distinct positions by Lemma 3.2.
Use the two endpoint-order banks in the gap decomposition (3.5)--(3.6):
terminal labels which cross from one endpoint block to the other are assigned
to the adjacent first or last gap block, exactly as in the two factorial
products in (3.4).  Substitution in (2.2) then shows that a ribbon at
position \(k\) exposes, in **each** straightened bank, the translate by
\(k\) of one interval of \(H\) ordered boundary positions.  For \(t\)
distinct translates of an \(H\)-interval on a cyclic order of length \(r\),
the union has size at least \(H+t-1\) whenever \(H+t-1\le r\): cut
immediately after a largest gap between the translate origins and apply the
linear interval-union bound.  Thus each bank exposes at least \(H+t-1\)
labels; equality is attained by consecutive origins.
Thus, when \(t\le r-H+1\), at most

\[
                         r-H-t+1
\]

labels remain freely orderable in each bank.  The position pattern has at
most \(r-t+1\) translations inside the \(r\) clean-pair positions.  Hence
every \(t\)-codegree is at most the right side of (3A.3).  Consecutive
ribbons leave exactly those two free cores and admit all \(r-t+1\)
translations, so equality holds. \(\square\)

The normalized pair parameter is

\[
 {r\Delta_2(\mathcal G_{r,H})\over D_H}
   ={r-1\over2(r-H)^2}.
\tag{3A.4}
\]

This remains \(o(1)\) on the intended mesoscopic scale \(H=o(r)\), including
\(H=\Theta(\sqrt{r\log r})\).  It is only a grouping profile.  The
target-incidence edge of a depth-\(H\) ribbon has rank \(2(H+1)\), so
Corollary 1.3's fixed-rank nibble cannot simply be reused when \(H\to\infty\).

## 4. Exact co-design equivalence

For \(P\subseteq V(\mathcal G_r)=E(\mathcal A_r)\), let
\(\mathcal G_r[P]\) be the induced grouping hypergraph.

### Theorem 4.1 (ribbon/group matching equivalence)

The following data are equivalent.

1. A matching \(P\) in \(\mathcal A_r\) and a matching \(\mathcal Q\) in
   \(\mathcal G_r[P]\).
2. A target-disjoint collection of the directed punctured wreaths indexed by
   \(\mathcal Q\), together with unused ribbons
   \(P\setminus V(\mathcal Q)\), such that the target sets of **all** wreath
   ribbons and unused ribbons are mutually disjoint.

If \(\ell=|P|-|V(\mathcal Q)|\), then the selected wreaths cover exactly

\[
                   2(|P|-\ell)
\tag{4.1}
\]

middle targets and the same number of lower targets.

#### Proof

Every grouping edge consists of \(r\) ribbons whose \(2r\) middle targets
and \(2r\) lower targets are internally distinct.  Since \(P\) is a
matching in the target-incidence hypergraph, distinct ribbons of \(P\) have
disjoint targets.  Therefore disjoint grouping edges inside
\(\mathcal G_r[P]\) give target-disjoint punctured wreaths and (4.1).

Conversely, expand every target-disjoint punctured wreath into its \(r\)
ribbons.  Their union is a matching in \(\mathcal A_r\), and the wreaths
are disjoint grouping edges on those ribbon vertices. \(\square\)

### Corollary 4.2 (the sufficient co-design theorem)

Suppose there is a matching \(P\) in \(\mathcal A_r\) and a matching
\(\mathcal Q\) in \(\mathcal G_r[P]\) such that

\[
 |P|={|\mathcal L|\over2}-o(N),
 \qquad
 |P|-|V(\mathcal Q)|=o(N).
\tag{4.2}
\]

Then the selected directed punctured wreaths miss only \(o(N)\) lower
targets and

\[
                {2N\over r+2}+o(N)=o(N)
\tag{4.3}

middle targets.  Their number is

\[
                 {|\mathcal L|\over2r}-o(N/r)
                 =(1-o(1)){N\over2r}.
\tag{4.4}

One dirty middle window per selected wreath costs only \(O(N/r)=o(N)\)
source occurrences.  Complementation on \([b]\) bijects these lower
rank-\((r-1)\) targets with the corresponding upper rank-\((r+2)\) targets,
so the same first-shadow deficit bound holds on the upper shore.

This is an exact positive reduction.  It does not prove (4.2).

## 4A. The common fractional point and inclusion-deck form

Let \(B_r\) be the bipartite inclusion graph between \(\mathcal L\) and
\(\mathcal M\).  It is \((r+2,r)\)-biregular.  A directed configuration
\(w\) has the flag deck

\[
 \mathsf F(w)=\{(L_i,M_i):1\le i\le2r\},
\tag{4A.1}
\]

which is a \(2r\)-edge matching in \(B_r\).  Pairing its flags at opposite
starts recovers the \(r\) ribbons in \(G(w)\).

### Proposition 4A.1 (inclusion-deck equivalence)

A collection of directed punctured wreaths is target-disjoint if and only if
the union of their flag decks is a matching in \(B_r\).  Consequently the
co-design problem is equivalently the problem of finding a matching in
\(B_r\) of size
\(|\mathcal L|-o(N)\) which, after deleting \(o(N)\) edges, is a disjoint
union of complete \(2r\)-edge decks \(\mathsf F(w)\).

#### Proof

The endpoints of an inclusion edge are exactly its lower and middle targets.
Within one deck, the proper cyclic intervals \(L_i\) are distinct, as are
the \(M_i\).  Across decks, target-disjointness is therefore exactly the
ordinary matching condition in \(B_r\).  Grouping the \(2r\) flags into
opposite pairs is (2.3). \(\square\)

Let \(\mathcal C_r\) be the \(4r\)-uniform multi-hypergraph on
\(\mathcal M\sqcup\mathcal L\), indexed by all \(b!\) directed
configurations and using their clean target sets as edges.

### Proposition 4A.2 (exact optimum fractional matching)

The configuration degrees are

\[
 \begin{aligned}
 D_{\mathcal M}^{\rm conf}
   &=2r\,r!(r+1)!,\\
 D_{\mathcal L}^{\rm conf}
   &=2(r+2)r!(r+1)!.
 \end{aligned}
\tag{4A.2}
\]

Giving every directed configuration the common weight

\[
                   \omega={1\over D_{\mathcal L}^{\rm conf}}
\tag{4A.3}
\]

saturates every lower target, gives every middle target load
\(r/(r+2)\), and has total mass

\[
 \sum_w\omega={N\over2(r+2)}={|\mathcal L|\over2r}.
\tag{4A.4}
\]

This is the maximum possible fractional mass under unit target capacities.

#### Proof

The symmetric group is transitive on each target layer.  Every one of the
\(b!\) configuration edges contains \(2r\) targets from each layer, so
double counting incidences gives

\[
 D_{\mathcal M}^{\rm conf}={2r b!\over N},
 \qquad
 D_{\mathcal L}^{\rm conf}={2r b!\over|\mathcal L|}.
\]

Use \(b!/N=r!(r+1)!\) and (1.1) to obtain (4A.2).  Equations
(4A.3)--(4A.4) follow.  Finally every configuration consumes \(2r\) lower
targets, so the lower capacity sum gives the matching upper bound
\(|\mathcal L|/(2r)\). \(\square\)

There is also a concrete stronger sufficient target.  By Kőnig's line
colouring theorem, \(B_r\) has a proper \((r+2)\)-edge-colouring.  Every
colour class saturates \(\mathcal L\).  If one can choose such a colouring
for which all but \(o(N)\) edges of one colour class decompose into decks
\(\mathsf F(w)\), Proposition 4A.1 closes the co-design gate.  No such
structured colouring is proved here.  A generic colouring or matching is
not expected to work; Section 5 quantifies the corresponding grouping
desert.

## 5. Why independent ribbon selection fails

Let

\[
 R=|V(\mathcal G_r)|={Nr^2(r+1)\over2},
 \qquad
 m=\left\lfloor{|\mathcal L|\over2}\right\rfloor.
\tag{5.1}
\]

Choose a uniformly random \(m\)-subset \(P_0\) of the ribbon vertices,
without even imposing target-disjointness.

### Proposition 5.1 (random-subset grouping desert)

The expected number of grouping edges contained in \(P_0\) is

\[
 \mathbb E e(\mathcal G_r[P_0])
   =b!{(m)_r\over(R)_r}
   \le b!\left({1\over r(r+1)(r+2)}\right)^r
   =o(1).
\tag{5.2}

Consequently \(P_0\) contains no complete directed punctured-wreath group
with probability \(1-o(1)\).

#### Proof

Each of the \(b!\) grouping edges has inclusion probability
\((m)_r/(R)_r\).  By (1.1) and (5.1),

\[
 {m\over R}\le {1\over r(r+1)(r+2)},
\tag{5.3}

and \((m)_r/(R)_r\le(m/R)^r\).  Finally Stirling's formula gives

\[
 \log b!-r\log(r(r+1)(r+2))
   =-r\log r+O(r)\longrightarrow-\infty.
\tag{5.4}

Markov's inequality proves the last assertion. \(\square\)

This proposition concerns the uniform subset law, not every possible random
greedy matching law.  Its implication is exact: a successful matching in
\(\mathcal A_r\) must be correlated with the grouping geometry by an
exponential factor.  One cannot first take a generic fixed-rank nibble and
then hope to group its output.

The inclusion-deck version has the same failure at a milder but still
exponential scale.  The graph \(B_r\) has \(Nr\) incidence edges.  If
\(F_0\) is a uniformly random \(|\mathcal L|\)-subset of them, then

\[
 \begin{aligned}
 \mathbb E\#\{w:\mathsf F(w)\subseteq F_0\}
   &=b!{(|\mathcal L|)_{2r}\over(Nr)_{2r}}\\
   &\le {b!\over(r+2)^{2r}}\\
   &=\exp\{2r(\log2-1)+O(\log r)\}=o(1).
 \end{aligned}
\tag{5.5}
\]

Here \(|\mathcal L|/(Nr)=1/(r+2)\).  Thus a generic inclusion-edge set of
the correct cardinality contains no complete deck with probability
\(1-o(1)\), even before the ordinary matching constraint is imposed.  This
does not cover every distribution on proper inclusion matchings; it rules
out independent selection as the source of the required deck structure.

## 6. Grouping-factor quotients and a forced codegree floor

Assume, conditionally, that \(\mathcal F\) is a perfect matching of
\(\mathcal G_r\), so every ribbon belongs to exactly one selected grouping
edge.  Let \(\mathcal Q_{\mathcal F}\) be the \(4r\)-uniform
**multi-hypergraph indexed by the factor groups** on
\(\mathcal M\sqcup\mathcal L\): a factor group contributes its target set
as one indexed edge, even if two different groups happen to have the same
unlabelled target set.  Degrees and codegrees below count these indexed
factor groups with multiplicity.

### Proposition 6.1 (exact quotient degrees)

Every middle target has degree \(r^2(r+1)\) in
\(\mathcal Q_{\mathcal F}\), and every lower target has degree
\(r(r+1)(r+2)\).

#### Proof

A target occurs at most once inside a directed punctured wreath.  Hence the
ribbons incident with a fixed target belong to distinct factor groups.
Since \(\mathcal F\) partitions every ribbon, the quotient degree is exactly
the number of incident ribbons, given by Lemma 1.1. \(\square\)

### Proposition 6.2 (factor-independent pair floor)

For every \(X\in\mathcal M\) and \(S\in\mathcal L\) with \(S\subset X\),

\[
 d_{\mathcal Q_{\mathcal F}}(X,S)\ge r(r+1).
\tag{6.1}
\]

Consequently

\[
 \Delta_2(\mathcal Q_{\mathcal F})\ge r(r+1),
 \qquad
 {4r\Delta_2(\mathcal Q_{\mathcal F})
       \over\min_vd_{\mathcal Q_{\mathcal F}}(v)}\ge4.
\tag{6.2}

#### Proof

Lemma 1.2 gives exactly \(r(r+1)\) ribbons containing the pair \((X,S)\).
The grouping factor assigns each such ribbon to a group.  No group can
contain two of them, because its actual middle and lower target occurrences
are distinct.  These ribbons therefore produce \(r(r+1)\) distinct quotient
edges containing \((X,S)\).  Proposition 6.1 gives the minimum degree
\(r^2(r+1)\), proving (6.2). \(\square\)

Thus even a perfectly balanced integral grouping factor cannot make its
target quotient satisfy the natural sparse-codegree condition
\(k\Delta_2/D=o(1)\).  This is not a nonexistence theorem for a quotient
matching.  It proves that any positive proof must exploit the forced
same-ribbon clusters, for example through a cluster-aware nibble, a direct
co-design of \(P\) and \(\mathcal Q\), or a structured factor with an
additional deterministic matching theorem.

## 7. Scope

The proved content is:

1. the complete four-target incidence profile;
2. the configuration reconstruction and \(b!\) simplicity;
3. every grouping maximum \(t\)-codegree, including the exact gap formula;
4. an abstract near-perfect ribbon matching by a genuinely fixed-rank
   theorem;
5. the exact matching/grouping equivalence;
6. the inclusion-deck equivalence and exact optimum common fractional point;
7. a rigorous random-subset failure and a factor-independent quotient
   codegree floor.

The note does **not** prove an integral factor of \(\mathcal G_r\), the
co-designed matching (4.2), a growing-rank matching theorem for the quotient,
target-disjoint co-design for the deeper nested flags, endpoint-disjoint
factor ordering, or a physical universal-word lift.  These scopes are
separate.
