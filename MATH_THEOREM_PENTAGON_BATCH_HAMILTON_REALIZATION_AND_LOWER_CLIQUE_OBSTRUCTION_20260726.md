# Physical pentagon batches: a linear Hamilton realization and the lower-clique obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
        \Omega=[2m+1],\qquad {\cal M}=\binom\Omega m,qquad
        W=|{\cal M}|,qquad m\ge7.                         \tag{0.1}
\]

The preceding trade theorem proved that complemented six-coordinate
pentagons generate the full integer kernel of the upper point-incidence
map while preserving middle degrees and the exact lower load.  This note
separates algebraic generation from physical occurrence.

There are two sharp results.

### Positive physical realization

Fix one six-set \(D\subseteq\Omega\).  For every

\[
                  K\in\binom{\Omega\setminus D}{m-3},          \tag{0.2}
\]

put the old complemented-pentagon five-path forest in the twenty-owner
fibre

\[
                  {\cal F}_K=\{K\cup A:A\in\binom D3\}.        \tag{0.3}
\]

All these prescribed forests extend simultaneously to **one Hamilton
cycle of \(J(2m+1,m)\)**.  Moreover, replacing the old table by the new
table independently in any subfamily of fibres leaves one Hamilton cycle.

The number of independently switchable fibres is

\[
 F=\binom{2m-5}{m-3}
    =\left({1\over64}+o(1)\right)W.                            \tag{0.4}
\]

Their upper supports are disjoint.  Switching all fibres therefore gives
the literal kernel motion

\[
                 \|\Delta u\|_1=6F
                    =\left({3\over32}+o(1)\right)W,            \tag{0.5}
\]

and a defect-aligned subfamily can decrease upper repeat excess by as much
as

\[
                         3F=\left({3\over64}+o(1)\right)W.    \tag{0.6}
\]

Thus \(\Omega(W)\) pentagon-kernel motion is physically realizable while
preserving one cycle.  The unresolved issue is not Hamilton topology.
The constructed Hamilton cycle is not proved lower-complete.

### Sharp obstruction to an unconditional prescribed-forest theorem

For a partial linear forest \(P\) and a lower colour
\(R\in\binom\Omega{m-1}\), define its residual clique capacity on

\[
                         Q_R=\{R+x:x\in\Omega\setminus R\}     \tag{0.7}
\]

by the residual degrees \(c_P(X)=2-d_P(X)\).  If \(P\) does not already
use colour \(R\), every lower-complete \(2\)-factor extending \(P\) must
have at least two distinct vertices \(X\in Q_R\) with \(c_P(X)>0\).
More generally the required further \(R\)-edges must fit a simple
\(b\)-matching in the clique on \(Q_R\) with capacities \(c_P\).

This condition is genuinely stronger than all point margins.  For every
large \(m\), one can choose only \(m+2\) pairwise owner-disjoint old
pentagon forests so that

* every owner of one clique \(Q_R\) is an internal degree-two vertex;
* none of the prescribed edges has lower colour \(R\).

No lower-complete \(2\)-factor, hence no lower-complete Hamilton cycle,
contains this batch.  Every individual pentagon trade is nevertheless
owner-neutral, lower-neutral, and upper point-neutral.

Consequently an unrestricted “every disjoint point-compatible pentagon
forest extends” theorem is false, already for an \(O(m)\) batch.  A
positive defect-aligned theorem must impose the residual-clique condition
and a global analogue of it.  The fixed-six-set linear bank passes the
Hamilton-topology gate, but lower-complete extension of that bank remains
the precise colour gate.

## 1. The local twenty-cycle containing the old pentagon

Suppress the common \((m-3)\)-set \(K\).  The five old complemented-
pentagon paths on \(\binom D3\) are

\[
\begin{array}{c|cccc}
1&456&245&235&123\\
2&356&345&234&124\\
3&346&236&126&125\\
4&246&146&136&135\\
5&256&156&145&134.
\end{array}                                                   \tag{1.1}
\]

They partition all twenty local owners.  Denote their initial and terminal
ports by

\[
\begin{array}{c|ccccc}
i&1&2&3&4&5\\ \hline
p_i&456&356&346&246&256\\
q_i&123&124&125&135&134.
\end{array}                                                   \tag{1.2}
\]

Add the five port edges

\[
 p_2q_4,\qquad q_2q_3,\qquad p_3p_1,\qquad
 q_1q_5,\qquad p_5p_4.                                      \tag{1.3}
\]

Every displayed pair is Johnson-adjacent.  After contracting the five
old paths, the edges (1.3) form the cycle

\[
                         2-3-1-5-4-2.                         \tag{1.4}
\]

### Lemma 1.1 (local prescribed Hamilton cycle)

The fifteen old path edges together with (1.3) form a Hamilton cycle
\(C_*\) of \(J(6,3)\).  In particular, the old pentagon forest is a
literal prescribed subforest of one local cycle.

#### Proof

The paths in (1.1) are vertex-disjoint and exhaust \(\binom D3\).
The physical adjacencies in (1.3) follow from the intersections

\[
 356\cap135=35,\quad124\cap125=12,\quad
 346\cap456=46,\quad123\cap134=13,\quad
 256\cap246=26.
\]

Equation (1.4) shows that the five contracted paths are connected and
two-regular.  Expanding them gives one twenty-cycle. \(\square\)

The old internal table uses every local two-set as a lower colour exactly
once.  Hence all five port edges in (1.3) repeat already represented local
lower colours.  Removing any of them does not erase local lower support.

## 2. Hamiltonizing the complete fixed-six-set bank

Let

\[
                 G=J(\Omega\setminus D,m-3).                   \tag{2.1}
\]

Its vertices are the carriers \(K\) in (0.2).  The induced subgraph on
owners meeting \(D\) in three points is the Cartesian product

\[
                         G\square J(6,3).                      \tag{2.2}
\]

We use the elementary cyclic-combination Gray code for combinations:
every nontrivial Johnson graph has a Hamilton cycle, hence a Hamilton path.
Choose a Hamilton path

\[
                         K_1,K_2,\ldots,K_F                    \tag{2.3}
\]

of \(G\).  Put a copy of \(C_*\) in every fibre \(K_i\).

For an edge \(ab\) of \(C_*\) and adjacent carriers \(K_i,K_{i+1}\),
the four owners

\[
 K_i+a,\quad K_i+b,\quad K_{i+1}+a,\quad K_{i+1}+b             \tag{2.4}
\]

form a Cartesian Johnson square.  Replacing the two fibre edges by the
two carrier edges merges the two cycles containing them.

### Theorem 2.1 (one carrier-layer Hamilton cycle)

There is a Hamilton cycle \(C_3\) on every owner satisfying
\(|X\cap D|=3\) which contains all fifteen prescribed old path edges in
every fibre \({\cal F}_K\).

#### Proof

Use two distinct port edges of (1.3), alternately, along the carrier path
(2.3).  At step \(i\), remove the two copies of the chosen port edge in
the current large cycle and the next fibre cycle, and add the two carrier
edges of (2.4).  The switch is a Cartesian rectangle and merges two
disjoint cycles into one.

At an internal fibre, the switches on its left and right use different
port edges, so neither asks for an edge already removed.  No switch touches
an internal edge of (1.1).  Induction along (2.3) produces one cycle on all
\(20F\) owners and retains every prescribed pentagon path. \(\square\)

This already embeds \(F=(1/64+o(1))W\) disjoint pentagons in one physical
cycle on \((5/16+o(1))W\) owners.

## 3. Extending the carrier-layer cycle to all owners

For \(0\le t\le6\), let

\[
             {\cal V}_t=\{X\in{\cal M}:|X\cap D|=t\}.          \tag{3.1}
\]

The induced layer graph is

\[
 J(6,t)\square J(2m-5,m-t),                                  \tag{3.2}
\]

where a trivial Johnson factor is interpreted as one vertex.  Every layer
has a Hamilton cycle: both nontrivial Johnson factors have cyclic
combination Gray codes, and the Cartesian product of two Hamilton cycles
has a Hamilton cycle.  For the last assertion, place one copy of the first
factor cycle over every vertex of a Hamilton path in the second factor and
merge successive copies by Cartesian rectangles, alternating two edges of
the first cycle exactly as in Theorem 2.1.  This is the usual serpentine
traversal of the product torus.

We need the following elementary splice.

### Lemma 3.1 (adjacent-layer rectangle splice)

Let \(C_t\) and \(C_{t+1}\) be disjoint Hamilton cycles on
\({\cal V}_t\) and \({\cal V}_{t+1}\).  Suppose \(C_t\) contains an edge

\[
 X=A\cup K\longleftrightarrow
 X'=A\cup(K-r+s)                                             \tag{3.3}
\]

which changes only outside coordinates.  Choose

\[
 d\in D\setminus A,qquad o\in K\cap(K-r+s),                  \tag{3.4}
\]

and put \(\phi(Z)=Z-o+d\) on the two endpoints.  If \(C_{t+1}\)
contains \(\phi(X)\phi(X')\), then replacing the two parallel layer
edges by

\[
                         X\phi(X),\qquad X'\phi(X')             \tag{3.5}
\]

merges \(C_t,C_{t+1}\) into one Hamilton cycle on their union.

The downward analogue removes one common \(D\)-coordinate and inserts one
outside coordinate absent from both endpoints.

#### Proof

The four displayed owners form a Johnson square.  Removing one edge from
each of two disjoint cycles produces two paths; the cross-pairing (3.5)
joins those paths into one cycle. \(\square\)

Every outside-type edge of one fixed layer lies in a Hamilton cycle of
that layer.  Indeed, some Hamilton cycle must use an outside edge in order
to visit more than one outside-coordinate fibre, and the group
\(S_D\times S_{\Omega\setminus D}\) is transitive on outside-type edges.

### Theorem 3.2 (full Hamilton prescribed-bank extension)

The union of all old pentagon path forests in (0.2)--(0.3) extends to a
Hamilton cycle \(C\) of \(J(2m+1,m)\).

#### Proof

The construction of \(C_3\) introduces many outside-type carrier edges;
reserve two distinct such edges.  Starting with the first, apply Lemma 3.1
successively to layers \(4,5,6\).  At each new layer choose a Hamilton
cycle containing the translated incoming edge.  Before the next splice,
choose a different outside-type edge remaining in that new layer.  Such
an edge exists: a Hamilton cycle in a nontrivial outside-coordinate
product must enter and leave every outside fibre, so it uses at least two
outside-type edges; the splice deletes only the translated incoming one.

Starting from the second reserved edge of \(C_3\), use the downward form
of Lemma 3.1 successively for layers \(2,1,0\).  The inequalities
\(m\ge7\) ensure that the required common-present or common-absent outside
coordinate exists at every step.  Each operation merges two disjoint
cycles and touches only a reserved carrier/layer edge, never an internal
edge of (1.1).  After six splices there is one cycle on
\(\bigcup_{t=0}^6{\cal V}_t={\cal M}\), containing every prescribed old
pentagon path. \(\square\)

## 4. Simultaneous physical kernel motion

The new complemented-pentagon table has the same five row endpoints as
the old table.  It also has the same owner-degree and lower-colour ledgers.
Therefore replacing one local table leaves the quotient cycle obtained by
contracting its five paths unchanged.

Different carriers \(K\) have disjoint owners, lower targets, and upper
targets.  Hence:

### Theorem 4.1 (linear independent switches in one Hamilton cycle)

For every subfamily \({\cal A}\subseteq\binom{\Omega\setminus D}{m-3}\),
replace the old table by the new table in exactly the fibres indexed by
\({\cal A}\).  The result is again one Hamilton cycle.  Its lower-load
vector is unchanged, and its upper change is the disjoint sum of the
pentagon kernel vectors.

In particular, switching all \(F\) fibres proves (0.5).  If each selected
fibre is defect-aligned with descent margin \(\gamma_K\), then

\[
                  R^+(C_{\rm new})
                   =R^+(C)+\sum_{K\in{\cal A}}\Delta_KR^+,
 \qquad
                  \Delta_KR^+\le-\gamma_K.                    \tag{4.1}
\]

Thus a fully margin-three bank proves (0.6), while a margin-one bank gives
descent \(|{\cal A}|\).

This theorem closes the topological realization question for a linear
fixed-frame bank.  It does not assert that the ambient cycle \(C\) covers
every lower target.  Since every switch preserves the complete lower-load
vector, lower completeness must be installed in the extension before the
switches are used.

## 5. The exact residual lower-clique condition

Fix a lower colour \(R\in\binom\Omega{m-1}\).  Every Johnson edge of
colour \(R\) lies in the clique on

\[
                         Q_R=\{R+x:x\notin R\},qquad |Q_R|=m+2. \tag{5.1}
\]

Let \(P\) be a prescribed maximum-degree-two forest and put

\[
                         c_P(X)=2-d_P(X)\in\{0,1,2\}.           \tag{5.2}
\]

### Theorem 5.1 (lower-colour residual capacity)

Suppose an extending \(2\)-factor must add \(a_R\) further edges of lower
colour \(R\).  Then the complete graph on \(Q_R\), after deleting already
forbidden edges, must contain a simple \(b\)-matching of size \(a_R\) with
vertex capacities \(c_P(X)\).

In particular, if \(P\) contains no \(R\)-edge and is to extend to a
lower-complete factor, then

\[
                  |\{X\in Q_R:c_P(X)>0\}|\ge2.                 \tag{5.3}
\]

#### Proof

Every new \(R\)-edge joins two distinct members of \(Q_R\), and its
incidence at \(X\) consumes one of the \(c_P(X)\) residual degree slots.
The set of all new \(R\)-edges is exactly the asserted capacitated simple
matching.  For one required edge, two positive-capacity endpoints are
necessary. \(\square\)

This condition is local but nonlinear.  It is invisible to the global
point-incidence margins of the signed pentagon trade lattice.

## 6. A point-compatible pentagon forest with no lower-complete extension

Fix one lower target \(R\).  For each owner

\[
                         X_x=R+x,qquad x\in\Omega\setminus R, \tag{6.1}
\]

we shall choose one old pentagon fibre in which \(X_x\) is an internal
degree-two owner, no fibre edge has lower colour \(R\), and all chosen
fibres are owner-disjoint.

Choose

\[
 A\in\binom R3,qquad C\in\binom{\Omega\setminus X_x}3,qquad
 D=A\cup C,qquad K=X_x\setminus A.                           \tag{6.2}
\]

Then \(x\notin D\), and the fibre \(\{K+B:B\in\binom D3\}\) contains
\(X_x=K+A\).  Relabel the six coordinates so that the local state \(A\)
is one of the ten internal states of (1.1).

### Lemma 6.1 (disjoint blocked-clique bank)

For all sufficiently large \(m\), the choices in (6.2) can be made for
all \(m+2\) owners \(X_x\) so that the resulting twenty-owner fibres are
pairwise disjoint.

#### Proof

For a fixed \(X_x\), the number of candidate fibres is

\[
                         \binom{m-1}{3}\binom{m+1}{3}
                          =\Theta(m^6).                        \tag{6.3}
\]

If a second owner \(Y\ne X_x\) belongs to such a fibre, then
\(d_J(X_x,Y)=d\le3\), the symmetric difference is forced into \(D\),
and the remaining choices are at most

\[
                         O(m^{6-2d})=O(m^4).                   \tag{6.4}
\]

After fewer than \(m+2\) fibres have been chosen, their union contains
only \(O(m)\) owners.  Hence at most \(O(m^5)\) candidates meet the
previous union, strictly fewer than (6.3).  A greedy choice succeeds.

Furthermore a fibre chosen for \(X_x\) contains no other member of
\(Q_R\): to contain all of \(R=(R\setminus A)\cup A\), its local
three-set must equal \(A\), giving the unique owner \(X_x\).  Thus a later
clique owner was not consumed earlier. \(\square\)

### Theorem 6.2 (residual-clique obstruction beyond point margins)

Let \(P_R\) be the union of the \(m+2\) old five-path pentagon forests
from Lemma 6.1.  Then no lower-complete \(2\)-factor of \(J(2m+1,m)\)
contains \(P_R\).

#### Proof

Every owner \(X_x\in Q_R\) is an internal vertex of its prescribed path,
so \(d_{P_R}(X_x)=2\).  It has no residual degree slot.

In a chosen fibre, \(X_x\) is the unique owner containing \(R\).  An edge
of lower colour \(R\) would require two such owners, so no prescribed fibre
edge has colour \(R\).  Thus \(P_R\) does not represent \(R\), while
the left side of (5.3) is zero.  Theorem 5.1 forbids a lower-complete
extension. \(\square\)

Each old/new pentagon replacement in this batch has zero middle, lower,
and upper-point margins.  Hence Theorem 6.2 is a genuine physical
obstruction beyond the complete linear invariant classification.

## 7. Exact surviving theorem

The results distinguish three levels.

1. **Lattice:** pentagons generate every point-neutral upper correction.
2. **Hamilton topology:** Theorems 2.1--4.1 physically realize
   \((1/64+o(1))W\) independent pentagons and
   \((3/32+o(1))W\) upper \(L^1\)-motion inside one full Hamilton cycle.
3. **Protected lower completeness:** arbitrary prescribed forests fail by
   Theorem 6.2.  The fixed-six-set bank has no topological obstruction, but
   no lower-complete extension is proved.

The sharp next statement is therefore:

> **Clique-slack prescribed-pentagon extension.**  Given a disjoint,
> defect-aligned pentagon forest satisfying every residual lower-clique
> \(b\)-matching condition of Theorem 5.1, together with the corresponding
> global cut conditions after its path components are contracted, extend
> it to a lower-complete Hamilton Johnson cycle while retaining a linear
> subfamily of the prescribed gadgets.

Theorem 6.2 proves that some hypothesis of this form is indispensable.
Theorem 4.1 proves that, once the protected-colour extension exists,
\(\Omega(W)\) simultaneous kernel motion and preservation of one cycle are
fully compatible.
