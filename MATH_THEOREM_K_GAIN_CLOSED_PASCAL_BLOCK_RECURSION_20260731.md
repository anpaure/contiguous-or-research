# Gain-closed Pascal bulk glue: the closed-subcycle obstruction

Date: 2026-07-31  
Status: exact architecture-specific impossibility theorem, exact conditional
partner/pivot formulas, and topology monodromy; no obstruction to larger or
non-gain-closed rethreadings

## 0. Main result

The most tempting all-\(K\) repair of the published one-port splice is
**gain closure**: make the \(B\) distinguished child labels and \(K\)
direct labels disjoint and exhaustive, and use the \(K\) new gains to fill
exactly the direct-label bank.  Locally this is perfect: every new direct
edge acquires a contiguous equal-colour gain partner.

Globally it is impossible.

Let \(P=\{r_i\}\) be the \(K\) physical ports and
\(\mathcal X=\{x_i\}\) the \(K\) direct labels.  The selected port row
\(r_i\) has central-cycle neighbours \(x_i\) and \(y_i\).  Exact gain
closure says \(\{y_i\}=\mathcal X\).  Hence every vertex of
\(P\cup\mathcal X\) has both central-cycle neighbours inside
\(P\cup\mathcal X\).  It is a nonempty union of whole cycle components.
The central child is one Hamilton cycle, so this forces
\(P\cup\mathcal X\) to be the entire cycle and \(K=A\), contradicting
\(A=B+K\) with \(B>0\).

This **closed alternating-subcycle obstruction** is stronger than the
known one-port deficiency \(K-1\): even \(K\) distinct locally legal ports
cannot realize the natural exact complement.

There is an exact mixed-partner replacement.  If \(Y\) is the gain bank
and \(X\) the direct bank, put

\[
 t=|X\setminus Y|=|Y\setminus X|.
\]

Then the selected ports and direct labels cut exactly \(t\) balanced
alternating intervals out of the central Hamilton cycle.  The
\(K-t\) labels in \(X\cap Y\) receive automatic gain partners, while the
\(t\) labels in \(X\setminus Y\) must receive retained tagged-child
partners.  Necessarily \(t\ge1\).  This interval law is the smallest
nonvacuous state for a modified recursion.

The remaining block-partner, colour-forest, pivot, and monodromy formulas
below identify the other gates.  An escape must carry the \(t\) retained
partner ports, use a larger switch, or rethread the central child
nonlocally.

Independently, any all-\(K\) bank with parallel orientation has component
permutation \(\alpha^{-1}\beta\), which is even.  If such a bank is
connected, \(K\) must be odd.  This parity result applies beyond gain
closure, but only to the parallel-oriented subfibre.

## 1. The two Pascal sectors

Put

\[
 n=2m-1,\qquad k=m-1,
\]

and let \(z\) be the new coordinate.  Set

\[
 A=\binom nk,\qquad B=\binom n{k-1},\qquad
 K=A-B=\operatorname{Cat}_m.
\tag{1.1}
\]

Let \(C_0\) be a tight enumeration of levels \(k,k+1\) of \(Q_n\).
Since the two levels have equal size, it alternates.  Let \(C_1\) be a
tight enumeration of levels \(k-1,k\).  Suppressing its lower vertices
gives a Hamilton cycle on the \(A\) rank-\(k\) states with exactly \(K\)
direct Johnson edges.

Orient the \(i\)-th direct edge locally as

\[
 d_i=r_i s_i,\qquad x_i=r_i\cup s_i.
\tag{1.2}
\]

Here \(r_i\) is the proposed vertical port and \(s_i\) the other endpoint.
Suppose \(C_0\) contains \(r_i-x_i\), and let \(y_i\) be the other
rank-\((k+1)\) neighbour of \(r_i\) on \(C_0\).  The Pascal square is

\[
 \{r_i0-x_i0,\ r_i1-s_i1\}
 \longmapsto
 \{r_i0-r_i1,\ x_i0-s_i1\}.
\tag{1.3}
\]

After suppressing lower rows, it creates

\[
 D_i=x_i0-s_i1,\qquad E_i=y_i0-r_i1.
\tag{1.4}
\]

The first is direct.  The second is distinguished by the lower row
\(r_i0\).  Their colour pairs are

\[
\begin{array}{c|cc}
 &\text{lower colour}&\text{upper colour}\\ \hline
 D_i&s_i&z+x_i,\\
 E_i&r_i&z+y_i.
\end{array}
\tag{1.5}
\]

## 2. Gain-closed child data

Let \(\mathcal R\) be the set of the \(B\) distinguished union labels in
the projected \(C_1\), and put

\[
 \mathcal X=\{x_i:i\in[K]\}.
\]

### Definition 2.1

The tagged child is **gain-closed** when

\[
 \mathcal R\mathbin{\dot\cup}\mathcal X
 =\binom{[n]}{k+1}.
\tag{2.1}
\]

Thus every old upper target appears exactly once in the projected child:
on a distinguished edge if it lies in \(\mathcal R\), and on a direct
edge if it lies in \(\mathcal X\).

For the central child define \(q_0(r)\) as the union of the two upper
neighbours of its lower row \(r\).

### Lemma 2.2 (sectorwise palette equivalence)

Assume (2.1) and distinct ports \(r_i\).  The distinguished upper palette
after all squares is exact if and only if

\[
 \{q_0(r):r\notin\{r_i:i\in[K]\}\}
   =\binom{[n]}{k+2}
\tag{2.2}
\]

and

\[
 \{y_i:i\in[K]\}=\mathcal X
\tag{2.3}
\]

as multiplicity-one identities.

#### Proof

The untagged upper targets are precisely the old rank-\((k+2)\) sets and
can only be supplied by unswitched \(C_0\) rows, giving (2.2).

The tagged targets are \(z+q\), for all old rank-\((k+1)\) sets \(q\).
The retained \(C_1\) bank supplies exactly \(\mathcal R\), while the
switched rows supply exactly the gains \(y_i\).  By (2.1), the missing
complement is \(\mathcal X\), proving (2.3). \(\square\)

### Theorem 2.3 (closed alternating-subcycle obstruction)

For every \(m\ge2\), no choice of \(K\) distinct ports can satisfy
(2.3) on the alternating Hamilton cycle \(C_0\).  Consequently no
gain-closed all-\(K\) Pascal-square common refinement exists.

This conclusion uses neither (2.2), fragment topology, lower-floor
conditions, nor the directed-repair pivot.

#### Proof

Put

\[
 \mathcal P=\{r_i:i\in[K]\},\qquad
 \mathcal X=\{x_i:i\in[K]\}.
\]

Every \(r_i\in\mathcal P\) has exactly the two \(C_0\)-neighbours
\(x_i,y_i\).  Both belong to \(\mathcal X\) by (2.3), and they are
distinct because \(C_0\) is a simple alternating cycle.

Conversely, every \(x\in\mathcal X\) occurs once as a designated
\(x_i\) and once as a gain \(y_j\), because both banks in (2.3) are
multiplicity one.  Its corresponding neighbours \(r_i,r_j\) are
distinct: equality would give \(i=j\) by port injectivity, and then
\(x_i=y_i\), contrary to the two distinct neighbours of \(r_i\).
Thus both \(C_0\)-neighbours of every \(x\in\mathcal X\) lie in
\(\mathcal P\).

It follows that the subgraph induced by
\(\mathcal P\mathbin{\dot\cup}\mathcal X\) is two-regular and has no
edge to its complement.  Since \(C_0\) is one cycle and the induced
subgraph is nonempty, it must equal all of \(C_0\).  Hence

\[
 |\mathcal P|=|\mathcal X|=A.
\]

But \(|\mathcal P|=|\mathcal X|=K\), while
\(A=B+K>K\) for \(m\ge2\).  Contradiction. \(\square\)

Equivalently, exact gain closure asks a proper subset of the edges of one
Hamilton alternating cycle to close into a two-regular subcycle.  This is
the smallest extra state missed by the separate palette counts.  With
\(y_i=x_{\sigma(i)}\), the forbidden induced subgraph is exactly the
alternating two-factor whose components are the cycles of \(\sigma\).

### Theorem 2.4 (mixed-partner interval law)

Drop gain closure, but retain:

* \(K\) distinct direct labels
  \(\mathcal X=\{x_i:i\in[K]\}\);
* \(K\) distinct ports
  \(\mathcal P=\{r_i:i\in[K]\}\);
* the designated matching edges \(r_i-x_i\) of \(C_0\); and
* \(K\) distinct gains \(\mathcal Y=\{y_i:i\in[K]\}\), where \(y_i\)
  is the other \(C_0\)-neighbour of \(r_i\).

Put

\[
 t=|\mathcal X\setminus\mathcal Y|
  =|\mathcal Y\setminus\mathcal X|.
\tag{2.5}
\]

Then the induced graph

\[
 H=C_0[\mathcal P\mathbin{\dot\cup}\mathcal X]
\]

is the disjoint union of exactly \(t\) balanced alternating paths.  It has

\[
 |V(H)|=2K,\qquad |E(H)|=2K-t.
\tag{2.6}
\]

Every path has one endpoint in
\(\mathcal X\setminus\mathcal Y\) and one endpoint \(r_i\in\mathcal P\)
whose external neighbour \(y_i\) lies in
\(\mathcal Y\setminus\mathcal X\).  In particular,

\[
 t\ge1.
\tag{2.7}
\]

If the tagged distinguished palette is exact, so that

\[
 \mathcal R\mathbin{\dot\cup}\mathcal Y
   =\binom{[n]}{k+1},
\tag{2.8}
\]

then precisely the \(K-t\) direct labels in
\(\mathcal X\cap\mathcal Y\) have gain partners.  The remaining \(t\)
labels in \(\mathcal X\setminus\mathcal Y\) lie in \(\mathcal R\) and
must use retained distinguished partners.  Their physical incidence with
the new direct edges is an additional block-coherence condition.

#### Proof

Every port \(r_i\) contributes its designated edge \(r_i-x_i\) to \(H\).
It contributes its other incident edge exactly when
\(y_i\in\mathcal X\).  Since the gain bank is squarefree, this happens
for exactly

\[
 |\mathcal X\cap\mathcal Y|=K-t
\]

ports.  This proves (2.6).  The designated edges form a perfect matching
of \(H\), so every path component of \(H\) is balanced.

The graph \(H\) has maximum degree two.  It has no cycle component: such
a component would be edge-closed in the one cycle \(C_0\), hence would
equal all of \(C_0\), impossible because
\(|\mathcal P|=|\mathcal X|=K<A\).  Therefore \(H\) is a forest, and

\[
 c(H)=|V(H)|-|E(H)|=t.
\]

A direct-label vertex \(x\in\mathcal X\) has degree one exactly when it
does not occur as a gain, namely when
\(x\in\mathcal X\setminus\mathcal Y\).  A port \(r_i\) has degree one
exactly when \(y_i\notin\mathcal X\), in which case
\(y_i\in\mathcal Y\setminus\mathcal X\).  Balancedness pairs one endpoint
of each type on every path.  Nonemptiness of \(H\) and acyclicity give
\(t=c(H)\ge1\).

Finally, under (2.8), a direct label in
\(\mathcal X\cap\mathcal Y\) has its unique distinguished occurrence in
the gain bank, while a direct label in
\(\mathcal X\setminus\mathcal Y\) is absent from \(\mathcal Y\) and hence
belongs to \(\mathcal R\).  The counts are \(K-t\) and \(t\),
respectively. \(\square\)

The two extremes are now exact.  Gain closure is the forbidden value
\(t=0\).  The rooted retained-partner fibre of
MATH_THEOREM_K_BLOCK_COHERENT_PASCAL_BULK_GLUE_20260731.md has
\(t=K\).  A viable recursion may use any \(1\le t\le K\), but it must
carry these \(t\) central intervals and their retained-partner incidence
data as part of its induction state.

### Corollary 2.5 (exact mixed block-partner condition)

Assume the exact tagged palette (2.8).  For a direct edge
\(d_i=r_i s_i\) of label \(x_i\):

* if \(x_i\in\mathcal X\cap\mathcal Y\), let \(j\) be the unique index
  with \(y_j=x_i\); its unique distinguished partner is
  \(E_j=x_i0-r_j1\), which is automatically adjacent to
  \(D_i=x_i0-s_i1\);
* if \(x_i\in\mathcal X\setminus\mathcal Y\), its unique distinguished
  partner is the retained \(C_1\)-occurrence of label \(x_i\), and literal
  contiguity holds exactly when that occurrence is incident with \(s_i1\).

In the first case \(r_j=s_i\) is the projected-multiedge degeneration
(3.3) and must be excluded for a simple Johnson factor.

#### Proof

The tagged palette partitions into retained labels \(\mathcal R\) and
gain labels \(\mathcal Y\).  A label in the intersection
\(\mathcal X\cap\mathcal Y\) has the unique gain occurrence displayed
above, sharing \(x_i0\) with \(D_i\).  A label in
\(\mathcal X\setminus\mathcal Y\) is absent from the gain bank and hence
belongs to \(\mathcal R\).  A tagged retained edge cannot meet the
zero-sector endpoint \(x_i0\), so it meets \(D_i\) exactly when it contains
the other endpoint \(s_i1\).  Equality of both gain/direct outer endpoints
gives (3.3). \(\square\)

### Theorem 2.6 (mixed all-\(K\) square master)

Under the distinct direct-label/gain hypotheses of Theorem 2.4, fix the
two parent cycles and one orientation \(d_i=r_i s_i\) of every direct
edge.  The all-\(K\) Pascal-square output is a literal cap-two
common-refinement Hamilton cycle if and only if:

1. \(r_i-x_i\in E(C_0)\) for every \(i\), and the \(r_i\) are distinct;
2. the unswitched \(C_0\) rows enumerate the no-\(z\) upper palette;
3. the retained \(C_1\) labels and gains \(y_i\) enumerate the tagged
   upper palette;
4. every direct label obeys Corollary 2.5, with no gain/direct
   projected-multiedge degeneration; and
5. the fragment graph \(\mathfrak F\) of Section 4 is connected.

Its complete lower occurrence profile is \(1^{N-K}2^K\) exactly when the
\(s_i\) are distinct.  Its upper occurrence profile is at that floor
exactly when the direct labels \(x_i\) are distinct.

#### Proof

Condition 1 is local square legality and simple vertical-port
compatibility.  Conditions 2--3 are the two sectorwise palette
bijections; the lower distinguished palette is automatic because every
lower row remains present once.  Corollary 2.5 is necessary and sufficient
for literal block adjacency.  Section 4 proves that Condition 5 is
necessary and sufficient for the degree-two output to be one component.

The common transversal already supplies every lower and upper colour once.
The \(K\) complementary direct occurrences have lower labels \(s_i\) and
upper labels \(z+x_i\).  The two floor statements are exactly their
injectivity. \(\square\)

### Corollary 2.7 (mixed three-facet pivot dichotomy)

Assume the mixed master and orient every doubled block so that its
distinguished partner is outgoing.

* If \(x_i=y_j\) has a gain partner, then
  \[
  (X_i,d_i,h_i;U_i)
   =\bigl(x_i,\ z+(r_j\cap s_i),\ r_j;\ z+x_i\bigr).
  \tag{2.10}
  \]
* If \(x_i\in\mathcal X\setminus\mathcal Y\) has a retained partner
  \(s_i1-c_i1\), where \(s_i\cup c_i=x_i\), then
  \[
  (X_i,d_i,h_i;U_i)
   =\bigl(z+s_i,\ c_i,\ z+(s_i\cap c_i);\ z+x_i\bigr).
  \tag{2.11}
  \]

In both cases \(X_i\) is the omitted middle state, \(d_i\) is the
contracted base colour, \(h_i\) is the selected repair colour, and \(U_i\)
is the host.  A directed floor repair requires the \(d_i\) to be distinct
and disjoint from the \(h_i\), and all block signs to agree.  Those
conditions are not implied by the mixed interval law.

#### Proof

In the gain case the block is

\[
 (z+s_i)-x_i-(z+r_j).
\]

Contracting its centre \(x_i\) gives base intersection
\(z+(s_i\cap r_j)\), while the outgoing selected edge has lower colour
\(r_j\), proving (2.10).

In the retained case the block is

\[
 x_i-(z+s_i)-(z+c_i).
\]

Contracting centre \(z+s_i\) gives base intersection \(c_i\), while the
outgoing retained edge has lower colour \(z+(s_i\cap c_i)\), proving
(2.11).  The floor and sign qualifications are the directed defect
transport identity read on these \(K\) triples. \(\square\)

For the conditional gain-closed formulas below, let \(\sigma\) be the
permutation of \([K]\) defined by

\[
 y_j=x_{\sigma(j)}.
\tag{2.9}
\]

## 3. Conditional gain-closed block formula

By Theorem 2.3 the hypotheses below have no global Hamilton instance for
\(m\ge2\).  The formulas are retained because they are exact local
identities and show what a non-gain-closed or larger-switch escape must
replace.

### Theorem 3.1 (gain-closed block partner)

Assume (2.1)--(2.3).  For every \(i\), put
\(j=\sigma^{-1}(i)\).  Then the unique distinguished occurrence of upper
colour \(z+x_i\) is

\[
 E_j=x_i0-r_j1.
\tag{3.1}
\]

It is adjacent to the direct occurrence

\[
 D_i=x_i0-s_i1
\tag{3.2}
\]

at the common middle state \(x_i0\).  Hence every doubled upper colour
forms a literal contiguous block.

If \(r_j=s_i\), the two projected occurrences have the same endpoints.
In the full tight enumeration they form the isolated three-vertex
component

\[
 x_i0-s_i0-s_i1-x_i0.
\tag{3.3}
\]

Thus a simple projected Johnson two-factor requires

\[
 r_{\sigma^{-1}(i)}\ne s_i\qquad(i\in[K]).
\tag{3.4}
\]

For a nontrivial spanning one-cycle output, (3.4) follows automatically
from connectedness.

#### Proof

By (2.3), \(x_i\) occurs exactly once among the gains, namely at
\(j=\sigma^{-1}(i)\).  By (2.1), it is absent from the retained
distinguished bank.  Therefore (3.1) is the unique distinguished partner.
Equations (3.1)--(3.2) share \(x_i0\), proving contiguity.

If \(r_j=s_i\), the retained central incidence
\(x_i0-r_j0\), the vertical edge \(r_j0-r_j1\), and the direct edge
\(x_i0-s_i1\) are exactly (3.3), and all three vertices have degree two
inside it.  Conversely, distinct outer endpoints give two distinct
Johnson occurrences sharing only \(x_i0\). \(\square\)

This is the positive closure absent from the one-port construction:
palette complement itself supplies all \(K\) physical block partners.

## 4. Exact physical topology

This section no longer assumes gain closure: it applies to any compatible
all-\(K\) square bank.  It therefore remains a nonvacuous topology test
for mixed retained/gain partner constructions.

Physical compatibility first requires the ports \(r_i\) and direct labels
\(x_i\) to be distinct.  Then the removed incidences, the vertical edges,
and the new cross edges in (1.3) are all distinct.  (Without squarefree
direct labels, distinct ports alone preserve degree only in a transition
multigraph: two direct edges with a common endpoint and common union can
request the same new cross edge.)  Delete all selected edges from the two
tagged parent cycles, contract the resulting \(K+K\) path fragments, and
retain the \(2K\) cross-sector edges.  Let \(\mathfrak F\) be this
two-regular bipartite fragment graph.

### Lemma 4.1 (component criterion)

The switched output is a physical two-factor.  Its components correspond
to the components of \(\mathfrak F\).  It is one cycle if and only if
\(\mathfrak F\) is connected.

#### Proof

Every switch removes and adds one incident edge at each of its four
physical endpoints.  Distinct ports prevent repeated vertical edges, and
distinct direct labels prevent repeated new cross edges, so degree two is
preserved in the simple physical graph.  Every contracted fragment has two
boundary ports, paired by the new edges.  Expansion of a path fragment
preserves components. \(\square\)

The adjective “physical” needs care.  Without (3.4), the full transition
graph is still degree two, but its rank-\((k+1)\) projection contains two
occurrences of the same Johnson edge and the isolated component (3.3).
That is a projected multiedge degeneration, not a simple spanning Johnson
two-factor.

### Theorem 4.2 (parallel-orientation monodromy)

Orient both parent cycles and suppose every selected edge is traversed as

\[
 r_i0\longrightarrow x_i0\quad\text{in }C_0 0,
 \qquad
 r_i1\longrightarrow s_i1\quad\text{in }C_1 1.
\tag{4.1}
\]

Let \(\alpha\) be the cyclic successor permutation of the cuts on \(C_0\)
and \(\beta\) the cyclic successor permutation of the cuts on \(C_1\).
Then the output components are the cycles of

\[
 \pi=\alpha^{-1}\beta.
\tag{4.2}
\]

In particular, the output is connected if and only if \(\pi\) is a
\(K\)-cycle.  Since \(\alpha,\beta\) are \(K\)-cycles, \(\pi\) is even.
Therefore

\[
 \boxed{\text{parallel-oriented connected bulk glue}
        \ \Longrightarrow\ K\text{ is odd}.}
\tag{4.3}
\]

#### Proof

After deleting a \(C_0\) cut, the forward fragment runs from \(x_i0\) to
\(r_{\alpha(i)}0\).  After deleting a \(C_1\) cut, the forward fragment
runs from \(s_i1\) to \(r_{\beta(i)}1\).

Starting at \(x_i0\), traverse the new head--head edge to \(s_i1\), the
\(C_1\) fragment to \(r_{\beta(i)}1\), the new tail--tail edge to
\(r_{\beta(i)}0\), and the \(C_0\) fragment backwards to
\(x_{\alpha^{-1}\beta(i)}0\).  This is (4.2), and each orbit is exactly
one output component.

Both successor permutations have sign \((-1)^{K-1}\), so
\(\operatorname{sgn}\pi=+1\).  A \(K\)-cycle has sign
\((-1)^{K-1}\), which is positive only for odd \(K\). \(\square\)

Condition (4.1) is strong.  If some selected incidence is traversed in
the opposite local direction, the correct state space is the signed
two-sheeted port permutation and the parity conclusion need not hold.
Thus (4.3) requires a twist for even \(K\); it does not prohibit twisted
gain-closed glues.

## 5. Formal gain-closed criterion

### Theorem 5.1 (necessary and sufficient gates)

Fix gain-closed child data (2.1) and restrict to all-direct-edge Pascal
squares (1.3).  The output is a literal cap-two common-refinement Hamilton
cycle if and only if:

1. for every \(i\), an orientation \(d_i=r_i s_i\) is chosen with
   \(r_i-x_i\in E(C_0)\);
2. the \(r_i\) are pairwise distinct;
3. (2.2)--(2.3) hold; and
4. \(\mathfrak F\) is connected.

Under these conditions (3.4) is automatic.  The full lower and upper
occurrence-load profiles are both \(1^{N-K}2^K\) if and only if, in
addition,

\[
 s_i\ne s_j\qquad(i\ne j).
\tag{5.1}
\]

For \(m\ge2\), Theorem 2.3 says that the gain-closed side of this formal
equivalence is empty.  The theorem is an exact diagnostic decomposition,
not an existence result.

#### Proof

The selected incidence and port injectivity are exactly local legality and
simple degree preservation.  Lemma 2.2 is necessary and sufficient for
the upper palette; the lower distinguished palette is automatic because
every lower row appears once.  Theorem 3.1 gives literal blocks.
Lemma 4.1 gives one-cycle topology and excludes (3.3).  These prove the
first equivalence.

The \(K\) unselected direct occurrences have lower colours \(s_i\).
The selected common transversal already contains every lower colour once,
so its full lower profile is at the floor exactly when the \(s_i\) are
distinct.  The direct upper labels \(z+x_i\) are already distinct, giving
the upper floor. \(\square\)

This is stronger than the known \(K-1\) theorem.  The old theorem says the
printed one-port glue has too few cross rows.  The present theorem says
exactly what a \(K\)-port replacement must satisfy, and proves that in the
gain-closed sector no separate contiguity search remains.

## 6. Conditional gain-closed colour dynamics

Assume (5.1), and let \(Q\) be the distinguished common transversal.
At doubled upper \(z+x_i\), its \(Q\)-neighbour is
\(r_{\sigma^{-1}(i)}\), while the nonmatching direct neighbour is \(s_i\).

Because the port and other-endpoint maps are injective, define a partial
permutation on \([K]\) by

\[
 \rho(i)=\sigma(j)
 \quad\Longleftrightarrow\quad
 s_i=r_j.
\tag{6.1}
\]

### Lemma 6.1 (exact forest criterion)

The common-transversal occurrence graph is a balanced linear forest if
and only if the partial permutation \(\rho\) has no directed cycle.
Its alternating-cycle components are in bijection with the directed
cycles of \(\rho\).

#### Proof

Starting with the nonmatching direct edge at upper \(z+x_i\), move to its
lower endpoint \(s_i\).  If \(s_i\) is not a port, its \(Q\)-edge ends at
an untagged singleton upper colour and the alternating component stops.
If \(s_i=r_j\), that \(Q\)-edge is the gain occurrence \(E_j\), whose
upper colour is

\[
 z+y_j=z+x_{\sigma(j)}.
\]

The next nonmatching edge is therefore indexed by \(\sigma(j)=\rho(i)\).
Injectivity makes this a disjoint union of directed paths and cycles.
The occurrence graph is obtained by attaching the endpoint matching edges
to these paths/cycles.  Hence it is a balanced forest exactly when no
directed cycle occurs. \(\square\)

This condition concerns uniqueness and leaf peeling of the common-colour
matching.  A common refinement can exist when \(\rho\) has cycles; then
the incidence graph has multiple transversals.

## 7. Conditional gain-closed repair pivot

For direct block \(i\), put \(j=\sigma^{-1}(i)\).  Its common middle
endpoint, selected lower colour, unselected lower colour, and upper colour
are

\[
 X_i=x_i,\qquad h_i=r_j,\qquad
 \alpha_i=s_i,\qquad U_i=z+x_i.
\tag{7.1}
\]

The contracted base colour is

\[
 d_i=(h_i\cap\alpha_i)
       \cup\bigl(U_i\setminus(h_i\cup\alpha_i)\bigr)
     =z+(r_j\cap s_i).
\tag{7.2}
\]

### Corollary 7.1 (directed floor-repair gate)

Under Theorem 5.1 and (5.1), the selected squares give the literal repair
triples

\[
 \bigl(x_i,\ z+(r_{\sigma^{-1}(i)}\cap s_i),\
       r_{\sigma^{-1}(i)};\ z+x_i\bigr),
\qquad i\in[K].
\tag{7.3}
\]

They form a three-shore perfect matching exactly when the \(d_i\) in
(7.2) are pairwise distinct.  The duplicate and hole shores are then
automatically disjoint because every \(d_i\) contains \(z\) and every
\(h_i\) avoids \(z\).

They give a uniform directed repair exactly when all doubled blocks have
one cyclic sign.  Leaf peeling of the full occurrence-labelled repair
atlas is the further pivot-unitriangular condition; it does not follow
from Lemma 6.1.

#### Proof

The \(X_i,U_i,h_i\) are pairwise distinct by (2.1), port injectivity, and
the bijection \(\sigma\).  Formula (7.2) is the exact Boolean-diamond
pivot.  Thus only collision of the \(d_i\) can prevent (7.3) from covering
all three \(K\)-shores.  Common cyclic sign is precisely the outgoing or
incoming choice at every hosted block.  The final statement compares two
different incidence structures: Lemma 6.1 peels the colour graph, while
the full repair atlas also contains alternative token/host occurrences.
\(\square\)

## 8. Relation to the abstract forest and the published recursion

The conditional gain-closed ledger separates four objects that generic
counting conflates.

* \(\mathfrak F\) controls physical cycle topology.
* The partner permutation \(\sigma\) controls literal cap-two adjacency.
* The partial permutation \(\rho\) controls the abstract common-colour
  forest.
* The pivot triples (7.3) control directed repair and its full atlas.

The canonical branching BTK/GK forest is not reconstructed here.  An
abstract balanced forest does not determine \(\sigma\), \(\mathfrak F\),
or the pivot labels.

The published Theorem 15 splice produces one cross row, whereas sector
balance requires \(K\); this is the earlier deficiency \(K-1\).  Merely
replacing it by \(K\) squares removes only that scalar defect.
Theorem 2.3 proves that the most direct attempt to close the label ledger,
namely (2.3), traps the proposed ports and labels in a forbidden proper
alternating subcycle.

Therefore a viable recursion must enlarge the induction state in at least
one of the following ways:

* use the mixed partner graph of Theorem 2.4, carrying its
  \(t\ge1\) balanced central intervals and exactly \(t\) retained partner
  incidences;
* allow gains outside the direct bank, followed by an additional transport
  layer;
* use a larger switch whose changed central rows are not closed under both
  incident Hamilton edges; or
* rethread the central child before declaring the \(K\) port rows.

For any such escape, the independent conditions \(\mathfrak F\), the
partial colour permutation, and the three-facet pivot remain relevant.

The parity theorem shows that an induction invariant demanding parallel
orientation at every port is already too strong whenever \(K\) is even.
Any viable uniform theorem must retain at least one bit of signed/twisted
port state.

## 9. Audited calibration and scope

The constant-size replay

* scratch/audit_k_block_coherent_pascal_local_obstructions_20260731.py;
* scratch/k_block_coherent_pascal_local_obstructions_20260731.audit.json

checks the local gain-partner formula with

\[
 x=123,\qquad s=12,\qquad r=23,\qquad z=6.
\]

It verifies the two Johnson occurrences

\[
 123-(126),\qquad 123-(236),
\]

their common upper colour \(1236\), their common middle endpoint \(123\),
and the contracted pivot

\[
 26=z+(12\cap23).
\]

This is deliberately a one-square calibration.  By Theorem 2.3 it cannot
extend to a global gain-closed Hamilton bank.  The same replay contains the
centre-only and free-port bow-tie
obstructions for the rooted partner fibre.

It also replays Theorem 2.4 on a five-by-five alternating cycle with
\(K=3\), obtaining

\[
 |\mathcal X\setminus\mathcal Y|=2,\qquad
 |V(H)|=6,\qquad |E(H)|=4,\qquad c(H)=2,
\]

with balanced component shore sizes \((1,1)\) and \((2,2)\).

The independent authenticated audit
MATH_AUDIT_K_GMM_BLOCK_CONTIGUITY_SMALL_FIXTURES_20260731.md supplies a
useful scope check.  All \(24\) common refinements at \(m=2\) are literal
contiguous cap-two cycles, but their all-\(K\) Pascal atlas has matching
rank \(1<2\).  The positive and mixed \(m=3\) common refinements have
maximum single-coordinate direct-cross count \(3<5\).  Thus known small
common refinements need not belong to any one-coordinate all-\(K\) square
fibre.  This is consistent with Theorem 2.3: the local gain formula is
valid, but the globally exact gain-closed bank is empty.

Proved:

* the closed alternating-subcycle obstruction, excluding exact gain
  closure for every \(m\ge2\);
* the exact \(t\)-interval mixed-partner law and \(t\ge1\);
* the nonvacuous mixed all-\(K\) necessary-and-sufficient master;
* conditional automatic literal block contiguity under the formally exact
  gain palette;
* the exact nondegeneracy condition;
* the formal necessary-and-sufficient ledger inside that empty subfibre;
* exact fragment monodromy and its parallel-orientation parity;
* the partial-permutation colour-forest criterion; and
* the exact gain/retained three-facet pivot dichotomy.

Not proved:

* an all-\(m\) mixed retained/gain construction satisfying the
  \(t\)-interval master;
* an outside-bank transport layer that avoids the closed-subcycle theorem;
* connected twisted monodromy in every dimension;
* distinct pivot labels and uniform sign in every dimension; or
* pivot-unitriangularity of the full repair atlas.
