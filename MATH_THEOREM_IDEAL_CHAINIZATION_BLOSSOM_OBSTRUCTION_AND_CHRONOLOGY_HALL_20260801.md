# Ideal owner slots do not integrally chainize: the first blossom and the exact chronology-Hall lift

Date: 2026-08-01  
Status: unconditional abstract counterexample and exact fixed-chronology
equivalence.  The counterexample is an owner-containment instance, but not
the complete strict lower ideal of a Boolean lattice.  It therefore refutes
an inference from slot Hall or fractional owner chains alone; it does not
refute a chainization theorem using the additional structure of the full
Boolean ideal.

## 0. Model

Let \(P\) be a family of lower targets, ordered by strict inclusion, and let
\({\cal T}\) be a family of owners.  A target \(S\) is eligible for an owner
\(T\) when \(S\subset T\).

A **depth-\(Q\) integral owner-chain factor** partitions \(P\) into at most
one inclusion chain of length at most \(Q\) for each owner, with every member
of the chain contained in its owner.  Empty owner chains are allowed.

The corresponding fractional factor consists of weights \(z_{T,C}\geq0\)
on eligible chains \(C\), including the empty chain, such that

\[
 \sum_C z_{T,C}=1\quad(T\in{\cal T}),\qquad
 \sum_{T,C:S\in C}z_{T,C}=1\quad(S\in P).             \tag{0.1}
\]

Ordinary labelled slots remember only \(|C|\leq Q\), not that the targets
in one fibre must be comparable.

There are three distinct levels of obstruction already at \(Q=2\):

* two incomparable targets and one universal owner are the trivial width
  obstruction, despite two labelled slots;
* a three-target chain together with one target incomparable to it, and two
  universal owners, has width two and satisfies every antichain-to-owner
  Hall row, but cannot be covered by two chains of size two (the long
  component must be split and the isolated target needs its own chain);
* even the exact fractional chain LP can be feasible while the integral
  factor fails.  The smallest such example is the six-target blossom in
  Section 2.

The middle example is a literal equal-rank containment instance: take
\(\{1\}\subset\{1,2\}\subset\{1,2,3\}\), the incomparable target
\(\{4\}\), and owners \(\{1,2,3,4,5\}\) and
\(\{1,2,3,4,6\}\).  Thus ordinary slot Hall plus ordinary chain-cover
width still misses the bounded-piece row.

## 1. An arbitrary additive integrality gap

### Theorem 1.1 (component-rounding obstruction)

Fix integers \(Q\geq2\) and \(C\geq0\) with \(Q>C+1\), and put

\[
                         L=Q+C+1,\qquad W=L.          \tag{1.1}
\]

There is an inclusion-poset owner instance with \(Q L=QW\) targets and
\(W\) owners for which:

1. the ordinary \(Q\)-slot containment graph has a saturating matching;
2. (0.1) has an exact fractional solution using chains of length exactly
   \(Q\);
3. no integral owner-chain factor has maximum length \(Q+C=L-1\).

Consequently neither exact slot Hall nor exact fractional nested
chainization implies integral depth \(D+O(1)\), even when
\(D=\lceil |P|/W\rceil\), without another structural hypothesis.

#### Construction

Take \(Q\) mutually incomparable components

\[
 {\cal C}_i:S_{i,1}\subset S_{i,2}\subset\cdots\subset S_{i,L}
 \qquad(1\leq i\leq Q),                              \tag{1.2}
\]

each a total chain of length \(L\).  Every owner contains every target.
Thus the ordinary slot graph is complete and its two shores have equal
cardinality \(QL=QW\).

This is a literal set-containment instance.  Choose pairwise disjoint sets
\(X_i=\{x_{i,1},\ldots,x_{i,L}\}\), put

\[
 S_{i,t}=\{x_{i,1},\ldots,x_{i,t}\},
 \quad U=\bigcup_iX_i,
 \quad T_j=U\cup\{y_j\}\quad(1\leq j\leq W).        \tag{1.3}
\]

The \(T_j\) have one common rank, contain every target, and targets from
different \(i\)'s are incomparable.

#### Fractional factor

For a fixed component \({\cal C}_i\), use every \(Q\)-element subchain with
aggregate weight

\[
                         \omega=
          \binom{L-1}{Q-1}^{-1}.                     \tag{1.4}
\]

Each target lies in \(\binom{L-1}{Q-1}\) such subchains, hence receives
aggregate weight one.  The total chain weight used by one component is

\[
 \binom LQ\omega=\frac LQ.                           \tag{1.5}
\]

Across the \(Q\) components it is \(L=W\).  Give every owner \(1/W\) of
this aggregate distribution.  Then each owner has total weight one and
each target has total weight one, proving (0.1).

#### Integral obstruction

No inclusion chain meets two different components.  Since
\(|{\cal C}_i|=L>Q+C\), every component needs at least two integral owner
chains.  Hence an integral factor needs at least \(2Q\) owners, whereas

\[
                         W=Q+C+1<2Q.                 \tag{1.6}
\]

This proves the theorem.  Notice that for each fixed proposed additive
constant \(C\), choosing \(Q>C+1\) defeats depth \(D+C\).

## 2. The smallest obstruction is two half-integral triangles

Set \(Q=2,C=0\).  The construction is two incomparable three-element
chains and three universal owners.  Its six targets exactly fill the six
ordinary labelled slots.

For each three-chain, put weight \(1/2\) on each of its three two-element
subchains.  The two components use total chain weight three, and
symmetrizing this distribution over the three owners gives an exact
fractional factor.  Integrally, each three-chain needs two depth-two chains,
so four owners are necessary.

This is the first nonbipartite matching obstruction.  At depth two and with
universal owners, let \(G_P\) be the comparability graph of \(P\).  Covering
\(n\) targets with \(W\) chains of size at most two is equivalent to finding
a matching of size at least \(n-W\) in \(G_P\).  The fractional owner-chain
LP only gives the fractional matching relaxation.  Indeed, if \(x,y,e\)
are the aggregate weights on pair, singleton and empty atoms, target
coverage and owner mass give

\[
 n=2x(E)+y(P),\qquad W=x(E)+y(P)+e,
 \quad\text{so}\quad x(E)=n-W+e\geq n-W.             \tag{2.1}
\]

Here

\[
                         G_P=K_3\sqcup K_3.           \tag{2.2}
\]

The half-edge solution has value three, but the maximum integral matching
has value two.  Equivalently, each triangle violates the Edmonds odd-set
row

\[
                 x(E(A))\leq\frac{|A|-1}{2}
                 \qquad(|A|\text{ odd}).             \tag{2.3}
\]

Two triangles are minimal: one odd triangle contributes only a half unit
of matching gap, whereas the demanded matching cardinality \(n-W\) is
integral.  By the half-integrality theorem for the fractional matching
polytope, its nonintegral extreme components are vertex-disjoint odd cycles.
An integral shortfall at an integer demand first requires two such
components; the shortest choice is two triangles, on six targets.

Thus there is no general uncrossing argument from the fractional chain
atoms to an integral factor.  The missing row is already a blossom row at
depth two.

## 3. Normalized matching and an SCD are not enough

Rank the targets in (1.2) by \(t\).  Every rank has \(Q\) elements and the
cover graph between consecutive ranks is a perfect matching.  Hence the
target poset satisfies normalized matching with equality and is itself the
union of \(Q\) symmetric chains.  Appending the universal owner layer also
preserves the normalized-matching inequality.

Nevertheless Theorem 1.1 fails integral depth \(Q+C\).  Therefore neither
normalized matching nor the existence of a Greene--Kleitman/SCD-style
chain partition controls the **number of pieces created when long chains
are cut to the deadline depth**.  A repair must correlate the cuts by
actual cross-chain chronology edges.

For a disjoint union of total-chain components of sizes \(\ell_i\), with
universal owners, the exact depth-\(R\) endpoint demand is

\[
                 \kappa_R(P)=
                 \sum_i\left\lceil\frac{\ell_i}{R}\right\rceil. 
                                                               \tag{3.1}
\]

An integral factor exists if and only if \(\kappa_R(P)\leq W\).  In the
family above, at \(R=Q+C=L-1\),

\[
                 \kappa_R(P)-W=2Q-L=Q-C-1.           \tag{3.2}
\]

Each new directed cross-component splice can reduce the number of path
pieces by at most one.  Hence at least \(Q-C-1\) such splices are necessary.
They are also sufficient in this universal-owner example when supplied as
an acyclic successor system with piece indegree/outdegree at most one and
merged length at most \(R\).  Explicitly, split every component into one
singleton piece and one \(R\)-piece.  Put

\[
                         M=Q-C-1.                    \tag{3.3}
\]

Order \(M+1=Q-C\) singleton pieces into one cross-component path using
\(M\) compatible splices.  Its length is \(Q-C\leq R=Q+C\); all \(R\)-pieces
and remaining singletons stay separate.  The resulting number of paths is
\(2Q-M=W\).  This is the sharp **splice debt** hidden by scalar slot Hall.

## 4. Exact repair after a chronology is supplied

The correct integral object becomes bipartite once a physical time order is
part of the state.

Fix \(R\geq1\) and a map

\[
                              \tau:P\longrightarrow[R].         \tag{4.1}
\]

Construct a bipartite graph \(B_\tau\).  Its left shore is a copy \(P_L\)
of all targets.  Its right shore is a disjoint union \(P_R\sqcup{\cal T}\).
Put edges

\[
 \begin{aligned}
 S_L&\longrightarrow S'_R
       &&\text{if }S\subset S'\text{ and }\tau(S)<\tau(S'),\\
 S_L&\longrightarrow T
       &&\text{if }S\subset T.
 \end{aligned}                                                   \tag{4.2}
\]

### Theorem 4.1 (fixed-chronology Hall equivalence)

There is an owner-chain factor of depth at most \(R\) whose order is
strictly increasing in \(\tau\) if and only if \(B_\tau\) has a matching
saturating \(P_L\).  Equivalently, for this fixed chronology the exact
min--max condition is

\[
                  |A|\leq |N_{B_\tau}(A)|
                  \qquad\text{for every }A\subseteq P.          \tag{4.3}
\]

#### Proof

Given a chain factor, match each nonterminal target to the next target of
its chain and match the terminal target to its owner.  Right targets and
owners are used at most once, so this is a matching saturating \(P_L\).

Conversely, orient every matched target--target edge from its left endpoint
to its right endpoint.  Every target has outdegree one, every target has
indegree at most one, and every owner has indegree at most one.  A directed
cycle of targets is impossible because \(\tau\) strictly increases on each
target edge.  The components are therefore directed target paths ending at
distinct owners.  Along a path the targets form an inclusion chain, and it
has at most \(R\) members because their \(\tau\)-values strictly increase in
\([R]\).  Its last target is contained in the terminal owner, so transitivity
puts the whole path under that owner.  This is the required factor.  Hall's
theorem gives (4.3).  \(\square\)

The existential version is also exact: every depth-\(R\) owner-chain factor
defines such a \(\tau\) by numbering positions in each chain.  What is not
automatic is a single \(\tau\) for which (4.3) holds.  Selecting \(\tau\)
is precisely the chronology/correlation gate discarded by the independent
slot and symmetric fractional arguments.

## 5. Proof-safe consequence for the Boolean problem

The abstract no-go does **not** show that the complete Boolean strict lower
ideal fails at depth \(d+O(1)\).  It shows exactly what a positive Boolean
theorem must use beyond items 2416ROOT--2417ROOT:

1. a rank-/endpoint-time assignment \(\tau\) with at most \(d+O(1)\)
   times;
2. the chronology Hall inequalities (4.3), or an explicit matching in
   \(B_\tau\);
3. owner containment at the terminal arcs; and
4. afterward, serialization compatible with the upper language and
   residence.

Greene--Kleitman chains can be a source of pieces, but their mere existence
does not pay the splice debt.  The required additional input is an
owner-compatible matching of cut-piece tails to later-time heads (a
layered path factor).  In the full Boolean lattice, Johnson/diamond
exchanges are plausible sources of those splice arcs; normalized matching
alone is not a proof that the required correlated matching exists.
