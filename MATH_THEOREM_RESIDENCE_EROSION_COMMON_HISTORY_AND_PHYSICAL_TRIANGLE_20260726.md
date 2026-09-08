# Residence-safe erosion flags: quotient-chain integrality and a physical determinant-two triangle

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Let \(E\) be the endpoint set of an exact residence-safe Johnson middle
chronology, and for \(0\le q\le H\) put

\[
 \Phi_q(t):=\bigcap_{i=0}^{q}M_{t+i}
 \in\binom{[2m+1]}{m-q}.
 \tag{0.1}
\]

The exact common-history system asks for nested endpoint sets

\[
 E=A_0\supseteq A_1\supseteq\cdots\supseteq A_H
 \tag{0.2}
\]

such that \(\Phi_q|_{A_q}\) is a bijection onto the complete
rank-\((m-q)\) layer for every \(q\).

This note proves four facts.

1. The system is a flag of bases of rank-one partition matroids.  If
   these matroids form a quotient chain, equivalently if every
   \(\Phi_{q+1}\) is a function of \(\Phi_q\), then a common-history
   integral flag exists.  The same proof gives an approximate theorem on
   any quotient core losing only \(o(W)\) target images.

2. For two adjacent depths, the exact criterion is ordinary Rado--Hall:
   the occurrence graph between the two target layers must have a
   matching saturating the lower layer.  For three depths, there is an
   exact stronger criterion: a three-coordinate matching saturating the
   deepest layer must have a two-coordinate projection extendible to a
   matching saturating the middle layer.  Separate adjacent Hall
   matchings omit precisely this extendibility state.

3. Residence safety does **not** force the quotient-chain property or
   total unimodularity.  For every sufficiently large \(m\), with
   \(H=A\sqrt m+O(1)\), there is an explicit simple cyclic Johnson
   chronology in which every nonconstant positive residence has length
   exactly \(H+1\), and whose actual erosion-column matrix contains

   \[
   \begin{pmatrix}
   1&1&0\\
   1&0&1\\
   0&1&1
   \end{pmatrix}.
   \tag{0.3}
   \]

   The construction uses three prescribed erosion checkpoints joined by
   FIFO buffer blocks.  Thus the determinant-two minor is physical, not
   a fictitious collection of nested set chains.

4. The physical triangle has only \(O(H)\) owners.  It proves that no
   theorem based solely on local Johnson adjacency, exact erosion ranks,
   and \((H+1)\)-residence can assert TU.  It does **not** prove a
   positive-density integrality gap in a full middle-layer factor.  The
   surviving constant-one alternative is therefore sharp: find an
   \(o(W)\)-loss quotient/laminar core, prove a stronger global
   common-history matching theorem, or amplify and force physical
   triangles in the actual factor.

## 1. Partition-matroid formulation

For each \(q\), partition the endpoint set by the fibres

\[
 \mathcal P_q:=\{\Phi_q^{-1}(T):
 T\in\operatorname {im}\Phi_q\}.
 \tag{1.1}
\]

Let \(\mathcal M_q\) be the partition matroid on \(E\) in which an
independent set contains at most one endpoint from every block of
\(\mathcal P_q\).  If \(\Phi_q\) is onto the entire target layer, its
bases have size

\[
 N_q:=\binom{2m+1}{m-q}.
 \tag{1.2}
\]

Then (0.2) is exactly a chain in which \(A_q\) is a base of
\(\mathcal M_q\).

For two matroids \(\mathcal N,\mathcal M\) on the same ground set, with
\(r(\mathcal N)\le r(\mathcal M)\), say here that \(\mathcal N\) is a
**partition quotient** of \(\mathcal M\) when every independent set of
\(\mathcal N\) is independent in \(\mathcal M\).  For the rank-one
partition matroids used here, this is exactly the usual quotient induced
by coarsening the blocks.  No assertion about arbitrary matroids is
needed below.

### Lemma 1.1 (partition quotients are fibre coarsenings)

The following are equivalent.

1. \(\mathcal M_{q+1}\) is a quotient of \(\mathcal M_q\).
2. Every block of \(\mathcal P_q\) is contained in a block of
   \(\mathcal P_{q+1}\).
3. There is a map

   \[
   f_q:\operatorname {im}\Phi_q
   \longrightarrow\operatorname {im}\Phi_{q+1}
   \tag{1.3}
   \]

   such that

   \[
   \Phi_{q+1}=f_q\circ\Phi_q.
   \tag{1.4}
   \]

#### Proof

If a block \(P\in\mathcal P_q\) meets two different
\(\mathcal P_{q+1}\)-blocks, two endpoints in those intersections form
an independent set of \(\mathcal M_{q+1}\) but a dependent set of
\(\mathcal M_q\).  Thus 1 implies 2.  Conversely, if every fine block is
contained in one coarse block, endpoints chosen from different coarse
blocks necessarily lie in different fine blocks, proving 1.  Conditions
2 and 3 are the same statement written in terms of fibre maps.
\(\square\)

### Theorem 1.2 (common-history quotient-chain theorem)

Suppose every \(\Phi_q\) is onto and

\[
 \mathcal M_H\text{ is a quotient of }\mathcal M_{H-1},
 \ldots,
 \mathcal M_1\text{ is a quotient of }\mathcal M_0.
 \tag{1.5}
\]

Then the exact common-history system (0.2) has an integral solution.

#### Proof

Choose an arbitrary base \(A_H\) of \(\mathcal M_H\).  By the quotient
property it is independent in \(\mathcal M_{H-1}\), so it extends to a
base \(A_{H-1}\) of that partition matroid.  Repeat upward.  At stage
\(q\), the already chosen \(A_{q+1}\) is independent in
\(\mathcal M_q\), and every independent set of a matroid extends to a
base.  This produces (0.2).  \(\square\)

The theorem is stronger than solving every adjacent matching separately:
it gives one common history through all depths.  Its hypothesis is also
stronger, and actual erosion maps need not satisfy it.

### Corollary 1.3 (defective quotient core)

Let \(E'\subseteq E\), put

\[
 \mathcal T'_q:=\Phi_q(E'),
 \tag{1.6}
\]

and suppose the restricted fibre partitions on \(E'\) form a quotient
chain through depths \(1,\ldots,H\).  Then there are nested sets

\[
 A'_H\subseteq\cdots\subseteq A'_1\subseteq E'
 \tag{1.7}
\]

such that \(\Phi_q|_{A'_q}\) is a bijection onto \(\mathcal T'_q\).
Set \(A_0=E\); endpoints in \(E\setminus E'\) simply receive radius
zero, so exact middle ownership is retained.
Consequently the aggregate target deficiency is exactly

\[
 \sum_{q=1}^{H}(N_q-|\mathcal T'_q|).
 \tag{1.8}
\]

In particular, a quotient core satisfying

\[
 \sum_{q=1}^{H}(N_q-|\Phi_q(E')|)=o(W)
 \tag{1.9}
\]

proves the required near-SCD grouping theorem.

#### Proof

Apply Theorem 1.2 to the restricted positive-depth partition matroids,
whose complete target sets are now the images \(\mathcal T'_q\).  Add
all endpoints at depth zero.  Formula (1.8) merely counts the omitted
positive-depth targets.  \(\square\)

Thus “delete \(o(W)\) endpoints” is not the right standalone metric.
The required metric is the all-depth image loss (1.9).

## 2. Exact two- and three-depth common-history criteria

For adjacent depths \(q,q+1\), form the bipartite occurrence graph
\(G_{q,q+1}\) with shores

\[
 \mathcal T_q=\binom{[2m+1]}{m-q},
 \qquad
 \mathcal T_{q+1}=\binom{[2m+1]}{m-q-1},
 \tag{2.1}
\]

and one edge labelled \(t\) from \(\Phi_q(t)\) to \(\Phi_{q+1}(t)\).
Parallel endpoint labels are retained.

### Theorem 2.1 (two-depth Rado--Hall theorem)

Assume every target on both shores occurs.  There are
\(A_{q+1}\subseteq A_q\subseteq E\) such that

\[
 \Phi_q|_{A_q}\text{ and }\Phi_{q+1}|_{A_{q+1}}
 \text{ are bijective}
 \tag{2.2}
\]

if and only if \(G_{q,q+1}\) has a matching saturating
\(\mathcal T_{q+1}\), equivalently

\[
 \boxed{
 |N(\mathcal B)|\ge|\mathcal B|
 \quad\text{for every }\mathcal B\subseteq\mathcal T_{q+1}.}
 \tag{2.3}
\]

#### Proof

The endpoints in \(A_{q+1}\) give a matching: their
\(\Phi_{q+1}\)-values are all different, and because
\(A_{q+1}\subseteq A_q\), their \(\Phi_q\)-values are also different.
This proves necessity.

Conversely, choose endpoint labels on a matching saturating the lower
shore and call that set \(A_{q+1}\).  For every as-yet unused
\(q\)-target, choose one arbitrary endpoint occurrence.  Different
\(q\)-targets have disjoint endpoint fibres, so these choices extend
\(A_{q+1}\) to the required \(A_q\).  Hall's theorem gives (2.3).
\(\square\)

For three consecutive depths, let \(\mathcal H_{q,q+1,q+2}\) be the
three-partite occurrence hypergraph whose endpoint \(t\) has trace

\[
 (\Phi_q(t),\Phi_{q+1}(t),\Phi_{q+2}(t)).
 \tag{2.4}
\]

### Theorem 2.2 (exact three-depth extension theorem)

Assume every target in the three displayed layers has an endpoint
occurrence.  Then there are nested bijective transversals

\[
 A_{q+2}\subseteq A_{q+1}\subseteq A_q
 \tag{2.5}
\]

if and only if there is a set \(F\) of endpoint hyperedges such that

1. \(F\) saturates \(\mathcal T_{q+2}\);
2. no two edges of \(F\) agree in their \(q\)- or \((q+1)\)-coordinate;
   and
3. the projected matching

   \[
   \{(\Phi_q(t),\Phi_{q+1}(t)):t\in F\}
   \tag{2.6}
   \]

   extends in \(G_{q,q+1}\) to a matching saturating
   \(\mathcal T_{q+1}\).

#### Proof

Given (2.5), take \(F=A_{q+2}\).  Conditions 1 and 2 follow from the
three bijections, while the endpoint edges indexed by
\(A_{q+1}\) give the extension in 3.

Conversely, take \(A_{q+2}=F\), extend its projection as in 3, and choose
one endpoint label on every added graph edge to obtain \(A_{q+1}\).
The projected matching already uses distinct \(q\)-targets, so Theorem
2.1 extends it to \(A_q\).  \(\square\)

Theorem 2.2 is a genuine common-history theorem: the deepest choice is
made in the three-coordinate occurrence hypergraph, and only choices
whose complete two-coordinate projection is extendible are allowed.
Separate solutions of (2.3) at the two seams do not imply condition 3.

For \(H>2\), iteration retains the complete trace prefix

\[
 (\Phi_1(t),\ldots,\Phi_q(t)).
 \tag{2.7}
\]

This is an exact finite-state formulation, but not an ordinary
single-commodity flow or a fixed pairwise Hall system.

## 3. A buffered residence-safe interpolation cycle

The next lemma supplies physical test chronologies.

### Lemma 3.1 (FIFO buffer cycle)

Let \(k\ge2\), let \(K\) be a fixed core, and let

\[
 V_1,V_2,V_3,B_{12},B_{23},B_{31}
 \tag{3.1}
\]

be \(k\)-sets, where the three buffers are pairwise disjoint and are
disjoint from \(V_1\cup V_2\cup V_3\).  Give every displayed set an
ordered listing.  There is a cyclic Johnson chronology of the
\((|K|+k)\)-sets which visits

\[
 K+V_1, K+B_{12}, K+V_2, K+B_{23}, K+V_3, K+B_{31}
 \tag{3.2}
\]

in that cyclic order, uses \(k\) transitions between consecutive
displayed states, and has the following properties.

1. On a leg \(K+X\to K+Y\), transition \(i\) deletes the \(i\)-th
   element of the listing of \(X\) and inserts the \(i\)-th element of
   the listing of \(Y\).
2. Every nonconstant positive coordinate residence has length exactly
   \(k\).
3. Apart from the identified endpoints of consecutive legs, all owners
   are distinct.

#### Proof

Use the stated coordinate swaps on each of the six legs.  At an
intermediate state of \(X\to Y\), the variable part is

\[
 \{x_{i+1},\ldots,x_k\}
 \mathbin{\dot\cup}
 \{y_1,\ldots,y_i\}.
 \tag{3.3}
\]

At every displayed state, use the same listing for the incoming and
outgoing leg.  Thus a coordinate inserted in position \(i\) on the
incoming leg is removed in position \(i\) on the outgoing leg.  It is
present in exactly \(k\) consecutive owners.  Coordinates of \(K\) are
constant-positive.

An interior state on a buffer leg contains a nonempty proper subset of
that leg's buffer, which no nonadjacent leg uses.  On the two legs
incident with one buffer, the buffer subsets are respectively a proper
prefix and a proper suffix of its ordered listing; they cannot be equal.
The only states with no buffer coordinate are the three distinct
\(K+V_i\), and the only full-buffer states are the three distinct
\(K+B_{ij}\).  This proves owner distinctness.  \(\square\)

The same proof permits the \(V_i\) to overlap arbitrarily.  Their common
coordinates simply have separate positive runs, each of length \(k\),
because every intervening buffer is disjoint from their union.

## 4. A physical determinant-two erosion triangle

Take

\[
 k:=H+1,
 \qquad H\ge3,
 \qquad m\ge3k+2,
 \qquad n=2m+1.
 \tag{4.1}
\]

Choose a fixed core \(K\) of size \(m-k\), a set
\(S\subseteq[n]\setminus K\) of size \(k-3\), and an element
\(c\in S\).  Outside \(K\cup S\), choose six distinct
coordinates

\[
 u,v,w,r_1,r_2,r_3.
 \tag{4.2}
\]

Put

\[
 \begin{aligned}
 V_1&=S\cup\{u,v,r_1\},\\
 V_2&=S\cup\{u,v,r_2\},\\
 V_3&=S\cup\{u,w,r_3\}.
 \end{aligned}
 \tag{4.3}
\]

There remain at least \(3k\) coordinates outside
\(K\cup V_1\cup V_2\cup V_3\), because

\[
 |[n]\setminus K|=m+k+1
 \quad\text{and}\quad
 |V_1\cup V_2\cup V_3|=k+3.
 \tag{4.4}
\]

Choose three disjoint \(k\)-set buffers there.  Order the three special
sets so that their first three coordinates are

\[
 \begin{array}{c|ccc}
 V_1&r_1&v&c\\
 V_2&r_2&u&v\\
 V_3&r_3&w&u.
 \end{array}
 \tag{4.5}
\]

Apply Lemma 3.1.  The resulting cycle has \(6k\) owners, all distinct,
and every nonconstant residence has length

\[
 k=H+1.
 \tag{4.6}
\]

Let \(t_i\) be the checkpoint with owner \(K+V_i\), and put

\[
 C:=K\cup S.
 \tag{4.7}
\]

The first three erosion targets at these checkpoints are

\[
 \begin{array}{c|ccc}
 &\Phi_1&\Phi_2&\Phi_3\\ \hline
 t_1&C+u+v&C+u&(C-c)+u\\
 t_2&C+u+v&C+v&C\\
 t_3&C+u+w&C+u&C.
 \end{array}
 \tag{4.8}
\]

### Theorem 4.1 (physical non-TU minor)

The natural whole-column incidence matrix of this residence-safe erosion
catalogue contains the minor

\[
 \boxed{
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},}
 \tag{4.9}
\]

whose determinant is \(-2\).

#### Proof

Take the three columns which select the depth-3 prefixes at
\(t_1,t_2,t_3\).  Take the row for \(C+u+v\) at depth 1, the row for
\(C+u\) at depth 2, and the row for \(C\) at depth 3.  Table (4.8) gives
exactly (4.9).  Lemma 3.1 and (4.6) verify that all three columns belong
to one actual simple residence-safe Johnson cycle.  \(\square\)

The same table shows failure of the quotient property.  The endpoints
\(t_1,t_2\) lie in one \(\Phi_1\)-fibre but have different
\(\Phi_2\)-values, while \(t_1,t_3\) lie in one \(\Phi_2\)-fibre but
have different \(\Phi_3\)-values.

On the three displayed rows, assigning weight \(1/2\) to each displayed
column solves the three unit equations, whereas no zero-one choice of
those three columns does.  This is the literal odd-cycle relaxation
behind the determinant.  Other endpoint columns and shorter-radius
columns may repair that restricted subsystem, so Theorem 4.1 is a
non-TU certificate, not yet a global integrality-gap theorem.

For fixed \(A\), condition \(m\ge3(H+1)+2\) holds for all sufficiently
large \(m\).  The example therefore lives at the Gaussian depth scale,
not only at fixed \(H\).

## 5. What the physical triangle does and does not prove

Theorem 4.1 closes one possible positive argument:

> exact Johnson adjacency, exact erosion ranks, long coordinate
> residences, and nested target columns do not imply total
> unimodularity of the common-history column matrix.

It also shows why adjacent-depth information is insufficient.  After
deleting any one of the three displayed target rows, the remaining two
unit equations have zero-one solutions on these columns; all three rows
together have only the half-integral solution on this restricted
support.  This is a statement about the displayed residual subsystem,
not a claim that the small cycle covers either complete Boolean layer.

However, the cycle has only

\[
 6(H+1)=O(\sqrt m)
 \tag{5.1}
\]

owners.  A coefficient-one obstruction would require much more:

1. embed a positive-density owner-disjoint family of these gadgets in
   the actual complete middle chronology;
2. prove that the three target rows in each gadget cannot be served by
   outside endpoint occurrences; and
3. show that repairing or deleting the gadgets costs \(\Omega(W)\) in
   aggregate target incidence.

None of these amplification statements follows from the local minor.
Conversely, a positive proof need not establish TU.  It is enough to find
a quotient core as in Corollary 1.3, or any nested integral selection
with aggregate deficiency \(o(W)\).

## 6. Exact surviving constant-one gate

The strongest proved positive common-history theorem is the quotient-core
criterion

\[
 \exists E'\subseteq E:
 \begin{cases}
 \Phi_{q+1}|_{E'}=f_q\circ\Phi_q|_{E'}& (q<H),\\
 \displaystyle
 \sum_{q=1}^{H}(N_q-|\Phi_q(E')|)=o(W).
 \end{cases}
 \tag{6.1}
\]

Under (6.1), Corollary 1.3 gives the required integral nested endpoint
flags, and the residence-safe erosion word literalizes them with no
additional rounding.  Together with the separately audited component
linearization condition \(HC=o(W)\), this is a coefficient-one
completion criterion.

Without a quotient core, the exact formulation is the iterated
common-history matching problem of Theorem 2.2 and (2.7).  Pairwise Hall
cuts (2.3) remain necessary but are not a complete multidepth dual.

Theorem 4.1 proves that a universal TU shortcut is false even for a
single physical Gaussian-safe cycle.  What remains open is an
asymptotic theorem about the **actual complete chronology**:

* either its common-history system has an integral solution with
  \(o(W)\) aggregate holes;
* or it contains a forced, outside-isolated, positive-density family of
  odd-cycle residuals.

That is the precise constant-one gate.  The local physical triangle
decides the algebraic question, but not the asymptotic one.
