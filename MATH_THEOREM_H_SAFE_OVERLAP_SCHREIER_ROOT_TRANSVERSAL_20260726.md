# The \(H\)-safe overlap digraph as a Schreier--de Bruijn object

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
                         \Omega=\binom{[2m]}m,\qquad W=|\Omega|.
                                                                  \tag{0.1}
\]

An \(H\)-safe rooted path is

\[
 e=(X_0,X_1,\ldots,X_H),\qquad
 X_t=X_{t-1}-a_t+b_t,                                  \tag{0.2}
\]

where \(a_1,\ldots,a_H\in X_0\) are distinct and
\(b_1,\ldots,b_H\in X_0^c\) are distinct.  Regard \(e\) as a de Bruijn arc
from its \(H\)-state prefix to its \(H\)-state suffix.  The resulting
overlap digraph \(\mathcal D_H\) is regular Eulerian:

\[
 \begin{aligned}
 |\mathcal E_H|&=W(m)_{\underline H}^2,\\
 |\mathcal V_H|&=W(m)_{\underline{H-1}}^2,\\
 d^+(v)=d^-(v)&=(m-H+1)^2.                            \tag{0.3}
 \end{aligned}
\]

It is also a homogeneous \(S_{2m}\)-object.  The arc set is one transitive
orbit \(S_{2m}/(S_{m-H}\times S_{m-H})\), the root set is
\(S_{2m}/(S_m\times S_m)\), and prefix/suffix are equivariant incidence
maps.  Thus \(\mathcal D_H\) is a Schreier correspondence equipped with the
usual de Bruijn shift.

There is an exact symmetric fractional solution of the root-transversal
problem.  Give every arc weight

\[
                         x_e={(m)_{\underline H}^{-2}}.            \tag{0.4}
\]

Then every \(m\)-set has total root weight one, every overlap state has equal
weighted indegree and outdegree, and every signed depth-\(q\) target has load

\[
                         {W\over N_q},\qquad
 N_q=\binom{2m}{m-q}.                                  \tag{0.5}
\]

The integral problem is therefore not a fractional Euler question.  It is
the colored circulation

\[
                         Rx=\mathbf1_\Omega,\qquad Bx=0,\qquad
                         x\in\{0,1\}^{\mathcal E_H},                \tag{0.6}
\]

where \(R\) records the root \(X_0\) and \(B\) is the directed
prefix--suffix incidence matrix.  Integral solutions are exactly
root-transversal cyclically \(H\)-safe path covers.  Appending the signed
target rows gives the complete quota problem.

Two exact conclusions result.

1. At \(H=1\), (0.6) is an ordinary regular bipartite matching problem and
   has a Latin resolution into \(m^2\) integral root permutations.
2. For every \(H\ge1\), no \(S_{2m}\)-equivariant integral root section
   exists when \(m>1\).  The stabilizer \(S_m\times S_m\) of one root acts
   transitively on its \(m^2\) first Johnson moves, so it fixes none.  Hence
   orbit averaging cannot be rounded by selecting a canonical orbit
   representative.  Any positive construction must break the full symmetry
   through a Latin resolution, a smaller regular group, or absorption.

There is also a signed-target lattice invariant.  For an integral cyclic
cover, let \(d_u\) be the number of selected transitions deleting coordinate
\(u\).  Cyclicity makes this also the number inserting \(u\).  If
\(S_{q,u}^-\) and \(S_{q,u}^+\) are the total occurrences of signed
depth-\(q\) targets containing \(u\), then

\[
 \boxed{
 S_{q,u}^-={W\over2}-qd_u,\qquad
 S_{q,u}^+={W\over2}+qd_u.}                            \tag{0.7}
\]

Consequently every simultaneous balanced quota table must obey

\[
 \boxed{
 S_{q,u}^-+S_{q,u}^+=W,\qquad
 {S_{q,u}^+-S_{q,u}^-\over2q}=d_u\in\mathbb Z_{\ge0}}
                                                                  \tag{0.8}
\]

with the same \(d_u\) for every depth and
\(\sum_ud_u=W\).  Quotas balanced independently at different signed ranks
need not satisfy this cocycle.  The symmetric fractional table has
\(d_u=W/(2m)\); an exactly coordinate-symmetric integral table is therefore
impossible unless \(2m\mid W\).

The exact positive target is a **Latin--Euler resolution** of the arc orbit:
color all \(H\)-safe arcs with \((m)_{\underline H}^2\) colors so that every
root sees each color once and every color class is Eulerian, while its signed
target histograms lie in the prescribed floor/ceiling quota polytopes.  This
is equivalent to decomposing the symmetric circulation into integral
root-transversal cycle covers.  Such a resolution is proved for \(H=1\);
for \(H\ge2\) it remains open.  The stabilizer obstruction and (0.8) are the
first invariants every proposed group or Latin construction must pass.

## 1. The homogeneous path and signature spaces

Write

\[
 (m)_{\underline k}=m(m-1)\cdots(m-k+1).
\]

For a fixed root \(X_0\), choose an ordered \(H\)-tuple of deleted elements
from \(X_0\) and an ordered \(H\)-tuple of inserted elements from \(X_0^c\).
This gives exactly

\[
                         D_H=(m)_{\underline H}^2                 \tag{1.1}
\]

rooted \(H\)-safe paths.  Conversely, the path determines the two ordered
tuples, so this parametrization is bijective.

An overlap state is a path of \(H\) middle states, hence has \(H-1\)
transitions.  Therefore

\[
                         |\mathcal V_H|
 =W(m)_{\underline{H-1}}^2.                           \tag{1.2}
\]

At such a state, \(2(H-1)\) coordinates have changed recently.  The current
set contains exactly \(m-H+1\) coordinates which may safely be deleted, and
its complement contains exactly \(m-H+1\) coordinates which may safely be
inserted.  Thus the number of safe forward extensions is
\((m-H+1)^2\).  Reversing the history gives the same number of predecessors,
proving (0.3).

Let \(G=S_{2m}\).  Fix a canonical path with ordered deleted tuple
\((1,\ldots,H)\), ordered inserted tuple
\((m+1,\ldots,m+H)\), and two unordered residual sets of size \(m-H\).
Its stabilizer is

\[
                         L=S_{m-H}\times S_{m-H}.       \tag{1.3}
\]

Hence \(\mathcal E_H\cong G/L\).  The root stabilizer is

\[
                         K=S_m\times S_m,               \tag{1.4}
\]

so \(\Omega\cong G/K\).  Similarly, the signature stabilizer is
\(S_{m-H+1}\times S_{m-H+1}\).  The root, prefix, and suffix maps are
\(G\)-equivariant.  The shift is not one fixed group element; it is the
equivariant de Bruijn correspondence between the two signature projections.

This distinction matters.  Transitivity proves exact fractional symmetry,
but it does not supply a \(G\)-equivariant section of the root projection.

## 2. Symmetric Euler circulation and signed loads

Let \(R\) be the root-incidence matrix

\[
                         R_{X,e}=\mathbf1_{\{X_0(e)=X\}},          \tag{2.1}
\]

and let \(B\) be the directed incidence matrix of the overlap graph,

\[
                         B_{\theta,e}
 =\mathbf1_{\{\operatorname{pref}(e)=\theta\}}
  -\mathbf1_{\{\operatorname{suff}(e)=\theta\}}.       \tag{2.2}
\]

### Theorem 2.1 (symmetric root-normalized circulation)

The constant vector (0.4) satisfies

\[
                         Rx=\mathbf1_\Omega,\qquad Bx=0.          \tag{2.3}
\]

At each depth \(1\le q\le H\), both signed target histograms are the
constant vector \(W/N_q\).

#### Proof

Every root has exactly \(D_H\) outgoing path arcs, proving \(Rx=\mathbf1\).
Every signature has the same number \((m-H+1)^2\) of incoming and outgoing
extensions, and all arcs have the same weight, so \(Bx=0\).

The group \(S_{2m}\) is transitive on each signed target layer.  The trace
map from rooted paths to

\[
 \bigcap_{j=0}^qX_j,\qquad \bigcup_{j=0}^qX_j
                                                                  \tag{2.4}
\]

is equivariant.  Its total weighted mass is
\(\sum_X(Rx)_X=W\).  Hence the mass is constant on the \(N_q\) targets and
equals \(W/N_q\). \(\square\)

Thus all signed ranks and the de Bruijn flow are simultaneously correct
fractionally.  The remaining issue is selecting one integral arc of every
root color.

## 3. Exact root-transversal cycle-cover system

Let \(A_q^\pm\) be the occurrence matrices of the signed traces (2.4).
For prescribed occurrence vectors \(b_q^\pm\), the exact integral system is

\[
 \begin{aligned}
 Rx&=\mathbf1_\Omega,\\
 Bx&=0,\\
 A_q^\pm x&=b_q^\pm\qquad(1\le q\le H),\\
 x&\in\mathbb Z_{\ge0}^{\mathcal E_H}.               \tag{3.1}
 \end{aligned}
\]

The root equation makes every integral variable binary.  If balanced quotas
may be chosen adaptively, replace the third line by

\[
                         A_q^\pm x\in\mathcal B_q^\pm,             \tag{3.2}
\]

where \(\mathcal B_q^\pm\) is the floor/ceiling polytope of total mass
\(W\).

### Theorem 3.1 (integral solutions are safe root cycle covers)

Integral solutions of the first two lines of (3.1) are in bijection with
collections of cyclically \(H\)-safe root paths which use every middle root
exactly once.  The remaining lines impose their literal signed occurrence
quotas.

#### Proof

The equation \(Bx=0\) makes the selected overlap arcs an Eulerian directed
multigraph.  Decompose it into directed circuits.  Consecutive arcs on one
circuit have matching length-\(H\) prefix and suffix histories, so their
roots form one cyclically \(H\)-safe middle path.  The root equation says
that every \(m\)-set roots exactly one selected arc, hence occurs exactly
once over all circuits.

Conversely, the length-\(H\) windows of such cyclic paths give selected
overlap arcs.  Every root occurs once and every signature occurs equally
often as a prefix and suffix.  Target occurrence is literal by definition.
\(\square\)

This is a colored circulation, not an ordinary uncolored Euler problem.
Dropping \(R\) leaves the network matrix \(B\); adding one root-color row to
every arc is the complete integrality gate.

## 4. The depth-one Latin theorem

When \(H=1\), overlap signatures are just middle owners and an arc is one
directed Johnson edge.  The root equation selects one outgoing edge at every
owner, while Euler balance selects one incoming edge.

### Theorem 4.1 (Latin resolution at depth one)

The complete directed Johnson graph on \(\Omega\) decomposes into

\[
                              m^2                              \tag{4.1}
\]

root-transversal directed cycle covers.

#### Proof

Split every owner into a tail copy and a head copy.  Join the tail \(X\) to
the head \(Y\) when \(X,Y\) are Johnson neighbours.  This bipartite graph is
\(m^2\)-regular.  By the integral bipartite matching theorem it decomposes
into \(m^2\) perfect matchings.  Each matching is a permutation of
\(\Omega\) supported on Johnson edges, hence a directed cycle cover.
\(\square\)

This proves that root colors do not obstruct integrality at depth one.  The
new difficulty for \(H\ge2\) is that one chosen arc consumes an entire
overlap history, so matching its head affects the root choices at several
other signatures.

There is a useful comparison which holds at every depth.  Split each
signature into a prefix copy and a suffix copy and join the two copies by
the path arcs.  This bipartite multigraph is
\((m-H+1)^2\)-regular, so it decomposes into
\((m-H+1)^2\) perfect matchings.  Equivalently, the uncolored overlap
digraph always has an integral resolution into one-in/one-out signature
factors.  A factor in this resolution contains

\[
                 |\mathcal V_H|=W(m)_{\underline{H-1}}^2
                                                                  \tag{4.2}
\]

arcs, not \(W\), and generally uses many arcs rooted at the same middle
set.  Thus this signature-scale Latin theorem resolves the Euler constraint
exactly while leaving the root-transversal constraint completely exposed.

## 5. No fully symmetric integral section

### Theorem 5.1 (stabilizer obstruction)

For \(m>1\), there is no \(S_{2m}\)-equivariant map

\[
                         s:\Omega\longrightarrow\mathcal E_H             \tag{5.1}
\]

such that \(s(X)\) is rooted at \(X\).  In particular, the symmetric
circulation of Theorem 2.1 cannot be rounded by selecting one canonical
arc in each root fibre and taking its full group orbit.

#### Proof

Fix \(X\in\Omega\).  Its stabilizer is
\(K_X\cong S_X\times S_{X^c}\).  Equivariance would force \(s(X)\) to be
fixed by \(K_X\).  But the first transition of \(s(X)\) selects an ordered
pair

\[
                         (a_1,b_1)\in X\times X^c.      \tag{5.2}
\]

The stabilizer is transitive on \(X\times X^c\), and when \(m>1\) no such
pair is fixed by all of \(K_X\).  Thus no rooted path in the fibre over
\(X\) is \(K_X\)-fixed, a contradiction. \(\square\)

The obstruction is stronger than the absence of a preferred coordinate:
it applies to every construction obtained from one orbit representative
under the full symmetric group.  It does not rule out a symmetry-breaking
Latin coloring or an action of a smaller group whose root stabilizers have
fixed path states.

## 6. Signed coordinate-star cocycle

Let an integral solution of (3.1) be fixed, without yet prescribing its
target histograms.  For coordinate \(u\), let \(d_u\) and \(i_u\) be the
numbers of selected root transitions which respectively delete and insert
\(u\).

### Lemma 6.1 (cyclic deletion--insertion balance)

\[
                              d_u=i_u,\qquad
                              \sum_ud_u=W.              \tag{6.1}
\]

#### Proof

On every selected middle cycle, the indicator of membership of \(u\)
returns to its initial value.  Hence the number of \(1\to0\) transitions
equals the number of \(0\to1\) transitions.  Sum over cycles.  Every one of
the \(W\) root transitions deletes exactly one coordinate, proving the
second identity. \(\square\)

For \(1\le q\le H\), let

\[
 S_{q,u}^\pm
 =\sum_{T\ni u}(A_q^\pm x)_T                         \tag{6.2}
\]

be the signed coordinate-star occurrence totals.

### Theorem 6.2 (simultaneous-depth star invariant)

Every integral root-transversal cyclic cover satisfies (0.7)--(0.8).

#### Proof

Among all roots, exactly \(W/2\) contain \(u\).  A lower depth-\(q\) trace
fails to contain \(u\), despite its root containing \(u\), exactly when its
\(q\)-transition window contains the deletion of \(u\).  Cyclic
\(H\)-safety makes these events disjoint within one window.  Notice also
that every selected circuit has length greater than \(H\): a shorter
period repeats a coordinate change inside an \(H\)-window, while a period
exactly \(H\) would have to return after exchanging two disjoint nonempty
sets of coordinates.  Every selected
deletion transition belongs to exactly \(q\) cyclic windows of length
\(q\), so

\[
                         S_{q,u}^-={W\over2}-qd_u.      \tag{6.3}
\]

Similarly, every insertion of \(u\) adds it to exactly \(q\) upper
depth-\(q\) windows whose roots did not contain it.  Lemma 6.1 gives

\[
                         S_{q,u}^+={W\over2}+qi_u
                                  ={W\over2}+qd_u.      \tag{6.4}
\]

The assertions in (0.8) follow. \(\square\)

The invariant is stated in occurrence capacity, not distinct-target support.
It therefore remains valid when several selected windows hit the same
target.  It is a literal lattice obstruction on the quota rows of (3.1).

For the symmetric fractional circulation, equivariance gives
\(d_u=W/(2m)\).  Hence a demand for exact coordinate symmetry in one
integral factor requires

\[
                              2m\mid W.                \tag{6.5}
\]

Independent floor/ceiling choices on the lower and upper layers can violate
the first equality or the divisibility in (0.8), even though each signed
quota vector separately has the correct total mass.  A valid quota selector
must choose all depths and both signs from one common integer vector
\((d_u)\), together with the higher-order overlap constraints not recorded
by coordinate stars.

For example, take \(m=3\) and \(H=2\).  Then \(W=20\), and the six lower
depth-two targets are singletons.  Floor/ceiling balance would give each
singleton load \(3\) or \(4\).  But (0.7) says that its load is

\[
                              10-2d_u,                 \tag{6.6}
\]

which is even.  Hence all six loads would have to be \(4\), contradicting
their total mass \(20\).  Thus the symmetric Euler circulation can be
fractionally perfect while the balanced integral quota system is empty;
this failure is caused by the common cyclic chronology, not by a scalar
capacity deficit.

## 7. Latin--Euler resolution

Let

\[
                              D_H=(m)_{\underline H}^2.
\]

### Theorem 7.1 (exact Latin resolution criterion)

The following are equivalent.

1. The complete \(H\)-safe arc set decomposes into \(D_H\) integral
   root-transversal Eulerian subgraphs.
2. There is a coloring

   \[
                              \lambda:\mathcal E_H\to[D_H]        \tag{7.1}
   \]

   such that:

   * for every root \(X\), the \(D_H\) arcs rooted at \(X\) receive all
     colors exactly once; and
   * for every color \(c\) and signature \(\theta\), the number of
     color-\(c\) arcs with prefix \(\theta\) equals the number with suffix
     \(\theta\).

Under either condition, every color class is a cyclically \(H\)-safe
root-transversal cover.  It is quota-balanced precisely when its signed
histograms lie in all the polytopes \(\mathcal B_q^\pm\).

#### Proof

Color the arcs by their part in a decomposition to obtain item 2.
Conversely, the root condition gives one arc of each color at every root,
and the signature condition makes each color class Eulerian.  Apply Theorem
3.1 separately to every color. \(\square\)

A resolution in Theorem 7.1 would be a Birkhoff theorem for this
root-colored de Bruijn correspondence.  Theorem 4.1 proves it for \(H=1\).
Theorem 5.1 shows that it cannot be obtained by assigning colors as full
\(S_{2m}\)-orbits of one rooted arc.

To include target balance, one needs the stronger orthogonal resolution

\[
                         A_q^\pm\mathbf1_{\lambda^{-1}(c)}
                         \in\mathcal B_q^\pm
 \quad(c\in[D_H],\ 1\le q\le H).                     \tag{7.2}
\]

The average over all colors is exactly the symmetric fractional vector
\((W/N_q)\mathbf1\), but averaging does not imply (7.2) color by color.
The star invariant (0.8) is the first necessary lattice condition for such
an orthogonal resolution.

## 8. Precise surviving gate

The group action proves all scalar degree and fractional Euler identities.
It does not provide the integral root section because the root stabilizer
has no fixed path.  Ordinary Euler decomposition ignores root colors, while
ordinary rootwise matching ignores signature balance.

The exact remaining alternatives are:

1. construct the Latin--Euler coloring (7.1), probably using a
   symmetry-breaking chain of subgroups or a quasigroup operation on ordered
   deletion/insertion tuples;
2. prove directly that the colored circulation polytope

   \[
       \{x\ge0:Rx=\mathbf1,\ Bx=0\}                  \tag{8.1}
   \]

   has an integral point satisfying the common signed quota lattice (0.8);
   or
3. exhibit a further signed potential or congruence separating
   \(\mathbf1_\Omega\) from the integral semigroup.

No such \(H\ge2\) Latin resolution is proved here.  What is proved is the
exact Schreier/de Bruijn model, its symmetric fractional solution, the
depth-one integral theorem, the impossibility of fully equivariant rounding,
and the simultaneous-depth signed-star invariant.  These isolate the root
constraint, rather than Euler balance or scalar target capacity, as the
integrality gate.
