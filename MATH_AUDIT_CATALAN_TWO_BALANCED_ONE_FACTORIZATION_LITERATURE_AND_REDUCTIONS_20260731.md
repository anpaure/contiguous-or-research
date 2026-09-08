# Two-balanced one-factorizations: literature boundary and exact reductions

Date: 2026-07-31  
Status: rigorous scoped audit.  The standard equitable-colouring theorems
solve the two marginal problems separately but not their conjunction.  Two
exact finite reformulations are proved below.  No all-\(m\) integral
factorization or acyclicity theorem is claimed.

## 1. Setup

Let \(|\Omega|=2m\), \(m\ge2\), and write

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1}.
\]

The diamond graph \(B_m\) is the bipartite containment graph on
\(\mathcal L\sqcup\mathcal U\).  It is

\[
 d=\binom{m+1}{2}
\]

regular.  The map

\[
 (L,U)\longmapsto
 \psi(L,U)=\{L+a,L+b\},\qquad U\setminus L=\{a,b\},       \tag{1.1}
\]

is a bijection from \(E(B_m)\) to the edge set of the Johnson graph
\(J(2m,m)\).  Thus the same ground set \(E\) carries two incidence
structures.

A \(d\)-colouring \(c:E\to[d]\) is a **two-balanced
one-factorization** when

1. every colour occurs once at every vertex of \(B_m\); and
2. every colour occurs at most twice at every vertex of \(J(2m,m)\).

Equivalently, every colour is a perfect matching of \(B_m\) whose Johnson
lift has maximum degree at most two.

## 2. What the equitable-colouring literature gives

There are two unconditional marginal theorems, but they give different
colourings.

### 2.1 The diamond shore alone

De Werra's bipartite equitable-colouring theorem gives an equitable
\(d\)-edge-colouring of \(B_m\).  Since every vertex has degree \(d\),
each colour occurs exactly once there.  This is precisely an ordinary
one-factorization of \(B_m\).

The additional words *balanced* and *equalized* do not add the required
Johnson control in this instance.  The graph is simple, so pairwise
multiplicity balance is vacuous; and every colour already has
\(|\mathcal L|\) edges.  Hence the theorem supplies no information about

\[
 g_j(X)=|\{e:c(e)=j,\ X\in\psi(e)\}|.                  \tag{2.1}
\]

### 2.2 The Johnson shore alone

Hilton and de Werra proved that a simple graph has an equitable
\(k\)-edge-colouring whenever no vertex degree is divisible by \(k\).
Apply this to \(J(2m,m)\) with \(k=d\).  Its degree is \(m^2\), and

\[
 d\mid m^2
 \quad\Longrightarrow\quad
 m+1\mid 2m
 \quad\Longrightarrow\quad
 m+1\mid2,
\]

which is impossible for \(m\ge2\).  The theorem therefore gives a
\(d\)-colouring for which every local count is one or two:

\[
 g_j(X)\in\{1,2\}.                                    \tag{2.2}
\]

Indeed the mean is

\[
 {m^2\over d}={2m\over m+1}\in(1,2),
\]

and equitability forces exactly \(m\) singleton colours and
\(m(m-1)/2\) double colours at each \(X\).  This is stronger than the
desired cap on the Johnson side, but it need not be proper on \(B_m\).

Thus the two marginal colourings exist unconditionally:

\[
 \begin{array}{c|c|c}
 &B_m&J(2m,m)\\ \hline
 \text{de Werra on }B_m&\text{proper}&\text{uncontrolled}\\
 \text{Hilton--de Werra on }J&\text{uncontrolled}&1/2\text{-balanced}.
 \end{array}                                           \tag{2.3}
\]

No theorem among these results identifies the two colourings.

### 2.3 Why the unimodular-hypergraph theorem does not combine them

Let \(\mathcal Q_m\) be the constraint hypergraph whose vertices are the
diamonds \(E\), with hyperedges

\[
 S_L=\{e:e\ni L\},\quad S_U=\{e:e\ni U\},\quad
 R_X=\{e:X\in\psi(e)\}.                               \tag{2.4}
\]

An equitable \(d\)-colouring of \(\mathcal Q_m\) would simultaneously
give one copy of every colour on each \(S_L,S_U\), and one or two copies
on every \(R_X\).  It would therefore prove the stronger, zero-free form
of two-balance.

De Werra's 1971 hypergraph theorem gives equitable colourings for
**unimodular** hypergraphs.  The present hypergraph is not unimodular.
Fix \(L\in\mathcal L\) and three distinct absent coordinates \(a,b,c\).
For

\[
 e_{ab}=(L,L+a+b),\quad e_{ac}=(L,L+a+c),\quad
 e_{bc}=(L,L+b+c),
\]

and \(X_a=L+a,X_b=L+b,X_c=L+c\), the rows
\(R_{X_a},R_{X_b},R_{X_c}\) and columns
\(e_{ab},e_{ac},e_{bc}\) contain

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},                                       \tag{2.5}
\]

whose determinant is \(-2\).  Equivalently, this restriction is the
incidence matrix of a triangle and has no equitable bicolouring.  This is
the minimal obstruction to invoking the unimodular-hypergraph theorem;
it is not an obstruction to the desired \(d\)-colouring.

The multiply-balanced detachment theorems likewise balance one fixed
graph incidence structure.  Their stated conclusions do not force the
same colour on the four incidences \(L,U,X,Y\) belonging to one diamond
while balancing both \(B_m\) and \(J(2m,m)\).  Thus there is no direct
specialization to (1.1)--(2.1); any use of detachment would still need a
new equality-coupling argument.

## 3. Exact simultaneous-colouring reduction

The missing conjunction has an exact formulation in the language of
simultaneous edge colouring.

### Theorem 3.1 (two-detachment equivalence)

There is a two-balanced one-factorization of \(B_m\) if and only if there
is a two-detachment \(J^\eta\) of \(J(2m,m)\) and a common
\(d\)-edge-colouring of the shared edge set \(E\) which is proper both on
\(B_m\) and on \(J^\eta\).

Here a two-detachment replaces every \(X\in\mathcal X\) by two clones
\(X^0,X^1\), and assigns each end of each Johnson edge to one of the two
clones.

#### Proof

Suppose first that \(c\) is two-balanced.  At a fixed \(X\) and colour
\(j\), there are at most two incident edges.  If there are two, send their
\(X\)-ends to different clones; if there is one, send it to either clone.
Do this independently for every \((X,j)\).  Then no clone is incident with
two edges of one colour, so \(c\) is proper on the resulting detachment.
It was already proper on \(B_m\).

Conversely, if \(c\) is proper on both graphs, then at most one edge of
colour \(j\) meets each clone \(X^0,X^1\).  Hence at most two meet the
original \(X\).  Properness at the degree-\(d\) vertices of \(B_m\), with
exactly \(d\) colours, makes every colour a perfect matching. \(\square\)

The conflict graph for a fixed detachment is

\[
             \Lambda_\eta=L(B_m)\cup L(J^\eta),        \tag{3.1}
\]

with common vertex set \(E\).  The problem is exactly whether some
detachment has \(\chi(\Lambda_\eta)=d\).

This is an edge-correspondence version of simultaneous edge colouring:
the two graphs have a common abstract edge index set, although the two
copies of an indexed edge have different endpoint pairs.  General
simultaneous-edge-colouring theorems do not reach the exact boundary even
in their standard, common-vertex formulation.  For two arbitrary graphs
of maximum degree \(\Delta\), Bousquet and Durain prove an upper bound
\(3\Delta/2+4\); this does not furnish the exact \(d\)-colour conclusion
required in (3.1), and it does not select the detachment.

### Corollary 3.2 (a finite clique target)

Let \(\mathscr P_2\) be the set of perfect matchings \(P\) of \(B_m\)
whose Johnson lift has maximum degree at most two.  Form the disjointness
graph \(\mathscr D_m\) on \(\mathscr P_2\), joining \(P,Q\) when
\(P\cap Q=\varnothing\).  Then

\[
 \boxed{\ \text{two-balanced one-factorization}
         \iff K_d\subseteq\mathscr D_m.\ }             \tag{3.2}
\]

Indeed \(d\) pairwise disjoint perfect matchings contain
\(d|\mathcal L|=|E(B_m)|\) edges and therefore partition all diamonds.
This is an exact auxiliary-graph reduction, with no LP or balancing
relaxation hidden in it.

## 4. Cap two is not acyclicity

Let \(\mathscr F\subseteq\mathscr P_2\) consist of matchings whose
Johnson lifts are forests.  The factorization route proves the Catalan
Linear Matching assertion only if

\[
       \text{some }K_d\text{ in }\mathscr D_m
       \text{ meets }\mathscr F,                       \tag{4.1}
\]

or if a subsequent colour-preserving switch turns one of its vertices
into a member of \(\mathscr F\).  Neither (3.2) nor any equitable-colouring
theorem includes this condition.

The two-detachment formulation makes the distinction particularly clear:
each colour is a matching in \(J^\eta\), but after identifying
\(X^0,X^1\) its projection is merely a graph of maximum degree two.  It
may contain cycles.

## 5. Exact small replay

Run

```text
python3 scratch/audit_two_balanced_one_factorization_sat_m2_m4_20260731.py 2 3
```

The script builds the literal diamond/Johnson incidence, emits the direct
SAT encoding, and independently replays the returned colour classes.

At \(m=2\), exhaustive enumeration gives nine perfect matchings, of which
six have forest lifts.  Their disjointness graph has exactly four
\(K_3\)'s: three contain one cyclic and two forest factors, while one
contains three cyclic factors.  Thus cap-two factorization does not make
acyclicity automatic, although a suitable factorization does contain an
acyclic colour.

At \(m=3\), the replay finds a two-balanced six-factorization with five
acyclic factors and one cyclic factor.  This is finite evidence only; it
does not extrapolate to all \(m\).

Frozen output:

```text
scratch/two_balanced_one_factorization_m2_m3_20260731.audit.json
```

## 6. Verdict and the exact next theorem

The literature search changes the route as follows.

* Ordinary bipartite equitable colouring is exactly the already-known
  one-factorization of \(B_m\); it cannot see the rectangles.
* Equitable colouring of the Johnson graph gives the optimal local
  \(1/2\) profile, but cannot see the two diamond shores.
* The natural combined constraint hypergraph contains the determinant-two
  triangle (2.5), so de Werra's unimodular-hypergraph theorem does not
  apply.
* The exact remaining cap-two assertion is the existential
  two-detachment simultaneous-colouring theorem of Theorem 3.1, or
  equivalently the clique assertion (3.2).
* Acyclicity is the additional marked-clique condition (4.1), not part of
  the balancing theorem.

Accordingly, the strongest clean theorem to target on this lane is:

> **Catalan simultaneous-factorization theorem.**  For every \(m\ge2\),
> the graph \(\mathscr D_m\) contains a \(K_d\) meeting
> \(\mathscr F\).

Its cap-two-only precursor drops the phrase “meeting \(\mathscr F\)”.
This theorem is stronger than the direct ordered-four-transversal theorem,
because it constructs all \(d\) colours simultaneously.  No source checked
in this audit proves it.

## References (primary sources)

1. D. de Werra, *Equitable colorations of graphs*, RAIRO 5 (1971), 3--8,
   https://www.numdam.org/item/M2AN_1971__5_3_3_0/ .
2. A. J. W. Hilton and D. de Werra, *A sufficient condition for equitable
   edge-colourings of simple graphs*, Discrete Math. 128 (1994), 179--201,
   https://doi.org/10.1016/0012-365X(94)90112-0 .
3. N. Bousquet and B. Durain, *A note on the simultaneous edge coloring*,
   Discrete Math. 343 (2020), 111781,
   https://arxiv.org/abs/2001.01463 .
4. A. Bahmanian and C. A. Rodger, *Multiply Balanced Edge Colorings of
   Multigraphs*, https://arxiv.org/abs/1710.03836 .
