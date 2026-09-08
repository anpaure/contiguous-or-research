# Thread A: AEC via Graver circuits, raw flow, and neutral signature absorption

Date: 2026-07-29

Status: exact minimal-generator theorem; exact raw completion-flow theorem;
quantitative sufficient absorption theorem for AEC; and a general-odd audit
of the full phase-labelled circuit space based at an MMM factor.  The
absorption hypotheses are not proved for general odd `k`, so AEC remains
open.

Primary audited inputs:

* `THREAD_A_GENERAL_ODD_K_MMM_SHADOW_PATH_DECORATION_RECURSION_20260729.md`;
* `MATH_THEOREM_DECORATED_MMM_ALTERNATING_SWITCH_AND_K15_SUPPORT_OBSTRUCTION_20260729.md`;
* `MATH_AUDIT_MMM_GLUING_SWITCH_PARAMETRIZATION_20260729.md`;
* `K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md`; and
* `MATH_K13_EXACT_1719_CERTIFICATE_20260728.md`.

## 0. Outcome

Fix

\[
 k=2m+1\ge5,\qquad r=m+1,\qquad
 N=\operatorname {Cat}_m,\qquad W=kN,
\tag{0.1}
\]

and let

\[
 G=\overline M_k=(\mathcal L\sqcup\mathcal U,E)
\tag{0.2}
\]

be the full phase-labelled quotient middle-level incidence multigraph.
Parallel phase edges are retained as distinct edges.  Let \(F_0\) be an MMM
connected spanning 2-factor and \(B\) the full two-shore vertex-edge
incidence matrix.

This note proves five things.

1. The exact minimal conformal generators of the owner-factor switch space
   are the signed simple even cycles of \(G\).  Relative to \(F_0\), the
   applicable atoms are precisely the simple cycles alternating between
   \(F_0\) and its complement.  Parallel 2-cycles are genuine atoms.
2. A spanning-tree fundamental cycle basis gives the smallest
   \(\mathbb Z\)-basis, of size

   \[
      \beta=(m-1)N+1,
      \tag{0.3}
   \]

   but is not a conformal or independently toggleable basis.  A concrete
   \(K_{3,3}\) factor already has five indispensable feasible circuits but
   cycle rank four.
3. Raw owner-factor completion is exactly a bipartite integral flow problem.
   That blanket total-unimodularity proof stops at the first
   diamond/upper-colour coupling: a universal \(3\times3\) minor has
   determinant two.
4. A neutral two-terminal circuit-packet library proves AEC whenever its
   candidate-list size \(L\), conflict degree \(\Delta\), and exact
   witness-reserve ledgers satisfy

   \[
       L\ge2e\Delta
       \tag{0.4}
   \]

   and the inequalities in Theorem 6.1 below.
5. The full phase-labelled circuit space of \(G\), based at an MMM factor,
   satisfies all raw algebraic hypotheses, but no current theorem supplies
   the neutral two-terminal localization, list expansion, or
   singleton-witness preservation required in item 4.
   Indeed, a new near-bijection lemma proves that almost every accepted
   quotient start is simultaneously a unique upper-\(q1\) and lower-\(q2\)
   witness.  Constant-density private dump reservoirs are therefore
   impossible.

Thus ordinary cycle-space dimension, total unimodularity of \(B\), and
fractional circuit flow do not prove AEC.  The sharp surviving route is a
global target-balanced packing of context-evaluated compound circuits.

## 1. The raw switch fibre

Write \(x_0=\mathbf1_{F_0}\), and define

\[
 \mathcal Z(F_0)=
 \left\{
 z\in\mathbb Z^E:
 Bz=0,\quad -x_0\le z\le\mathbf1-x_0
 \right\}.
\tag{1.1}
\]

The inequalities in (1.1) say exactly that \(x_0+z\) is binary.  Since
\(B(x_0+z)=2\mathbf1\), every element of \(\mathcal Z(F_0)\) is another
owner-exact spanning 2-factor, without a connectivity assertion.

For integer vectors \(u,z\), write

\[
 u\sqsubseteq z
\tag{1.2}
\]

when \(u,z\) lie in the same closed orthant and
\(|u_e|\le|z_e|\) for every edge.  A conformal decomposition is a sum in
which every summand is \(\sqsubseteq z\).

## 2. Exact minimal circuit generators

For a simple even cycle \(C\) of the bipartite multigraph \(G\), choose one
of its two cyclic orientations and let

\[
 g_C\in\{-1,0,1\}^{E}
\tag{2.1}
\]

be its alternating signed incidence vector.  A pair of parallel edges is
treated as a simple cycle of length two.

### Theorem 2.1 (Graver and support-minimal generators)

The Graver basis and the primitive support-minimal nonzero integer circuits
of \(B\) are exactly

\[
 \operatorname {Gr}(B)
 =
 \{\pm g_C:C\text{ is a phase-labelled simple even cycle of }G\}.
\tag{2.2}
\]

Relative to \(F_0\), the support-minimal feasible switches are exactly

\[
 \mathcal G(F_0)=
 \left\{
 g_C:
 C\text{ alternates between }F_0\text{ and }E\setminus F_0,
 \quad g_C<0\text{ on }F_0
 \right\}.
\tag{2.3}
\]

Every \(z\in\mathcal Z(F_0)\) has an edge-disjoint conformal decomposition

\[
 z=\sum_{i=1}^{t}g_{C_i},
 \qquad C_i\in\mathcal G(F_0).
\tag{2.4}
\]

Conversely, every edge-disjoint family from \(\mathcal G(F_0)\) has a
binary owner-exact sum.  Finally, \(\mathcal G(F_0)\) is indispensable:
every conformal generating set for all of \(\mathcal Z(F_0)\) must contain
every member of (2.3).

#### Proof

Multiply every row of \(B\) indexed by \(\mathcal L\) by \(-1\).  This turns
\(B\) into the directed node-edge incidence matrix \(D\), with all quotient
edges oriented from \(\mathcal L\) to \(\mathcal U\).  Hence

\[
 \ker_{\mathbb Z}B=\ker_{\mathbb Z}D.
\tag{2.5}
\]

Given nonzero \(z\in\ker_{\mathbb Z}D\), direct an edge forward when
\(z_e>0\), backward when \(z_e<0\), and give it multiplicity \(|z_e|\).
Flow conservation makes the resulting directed multigraph balanced at
every vertex.  It therefore contains a directed simple cycle.  The cycle
vector \(g_C\) satisfies \(g_C\sqsubseteq z\).  Subtract it and iterate.
This proves conformal simple-cycle generation.

A nonzero circulation supported on a proper subset of a simple cycle is
impossible: deleting any absent edge leaves a path endpoint with nonzero
imbalance.  Thus \(g_C\) is conformally indecomposable.  Conversely, unless
a primitive circulation is one simple cycle, the preceding extraction
gives a proper conformal summand.  This proves (2.2).

For \(z\in\mathcal Z(F_0)\), every coordinate has magnitude at most one, so
its conformal cycles are edge-disjoint.  Every negative edge belongs to
\(F_0\), while every positive edge lies outside \(F_0\); conservation around
each cycle makes these signs, and therefore factor membership, alternate.
This gives (2.3)--(2.4).  Toggling an edge-disjoint family removes and adds
the same number of incidences at every visited vertex, hence remains binary
and degree two.  Since \(g_C\) itself is feasible and conformally
indecomposable, every universal conformal generating set must contain it.
\(\square\)

The cycles in (2.4) may share vertices but not edges.  Any subfamily can be
toggled in any order: at a shared vertex the negative and positive edges of
an untoggled circuit are still respectively present and absent.

### Corollary 2.2 (sharp raw support bounds)

Let

\[
 a=\bigl|\{e:z_e=-1\}\bigr|.
\tag{2.6}
\]

Then

\[
 |\operatorname {supp}z|=2a\le4N.
\tag{2.7}
\]

If the circuits in (2.4) have lengths \(2\ell_i\), then

\[
 \sum_i\ell_i=a,\qquad
 t\le a\le2N,\qquad
 \sum_i|C_i|=2a\le4N,\qquad
 |C_i|\le2N.
\tag{2.8}
\]

If the used support has no parallel pair, then \(\ell_i\ge2\) and
\(t\le a/2\).

#### Proof

Both \(F_0\) and \(F_0+z\) contain \(2N\) quotient incidence edges.
Summing either shore of \(Bz=0\) shows that the positive and negative
supports have the same size \(a\).  The remaining assertions follow from
the edge-disjoint cycle decomposition and the fact that a simple cycle on
\(2N\) vertices has length at most \(2N\).  \(\square\)

### Proposition 2.3 (dynamic chordless generation)

If an \(F\)-alternating simple cycle \(C\) has a chord joining two
nonconsecutive cycle vertices, its toggle can be implemented by two strictly
shorter legal alternating toggles, the second evaluated relative to the
factor produced by the first.  Iterating shows that cycles with no
nonconsecutive chord, together with parallel 2-cycles, dynamically generate
the raw factor fibre.

This is not a conformal decomposition relative to the original factor, and
the intermediate factors need not be connected, resident, unit-voltage, or
shadow-complete.

#### Proof

The nonconsecutive chord divides \(C\) into two odd-edge paths, each of
length at least three, because \(G\) is bipartite.
Along each path the two endpoint edges have the same factor status, while
the statuses for the two paths are opposite.  Exactly one path, together
with the chord in its current status, is alternating.  Toggle that shorter
cycle.  The chord status reverses, so the other path together with the same
chord is now alternating.  Toggle it.  Every edge of \(C\) is toggled once,
the chord twice, and hence the net change is exactly the \(C\)-toggle.
\(\square\)

## 3. A fundamental basis is exact globally but not conformally

Choose a spanning tree \(T\) of \(G\).  For each chord \(f\notin T\), let
\(c^f\) be the signed fundamental-cycle vector normalized by
\(c^f_f=1\).

### Theorem 3.1 (global integer parametrization)

The vectors

\[
 \{c^f:f\notin T\}
\tag{3.1}
\]

form a \(\mathbb Z\)-basis of \(\ker_{\mathbb Z}B\).  Every switch has the
unique representation

\[
 z=\sum_{f\notin T}\alpha_f c^f,\qquad
 \alpha_f=z_f.
\tag{3.2}
\]

It belongs to \(\mathcal Z(F_0)\) exactly when

\[
 0\le x_{0,e}+\sum_{f\notin T}\alpha_f c^f_e\le1
 \qquad(e\in E).
\tag{3.3}
\]

For \(G=\overline M_k\), the number of basis vectors is

\[
 \beta=|E|-|V|+1=(m-1)N+1.
\tag{3.4}
\]

#### Proof

Subtract \(\sum_{f\notin T}z_fc^f\) from \(z\).  The residual circulation
is supported on the tree and hence vanishes by successive leaf deletion.
The distinct chord coordinates give uniqueness.  Condition (3.3) is
exactly binary feasibility.  The count (3.4) follows from Section 4 below.
\(\square\)

The basis is globally coupled through all inequalities (3.3).  It is not an
independent switch or absorption basis.

### Proposition 3.2 (minimal conformal counterexample)

Let \(G=K_{3,3}\), with shores
\(\{\ell_0,\ell_1,\ell_2\}\) and \(\{u_0,u_1,u_2\}\), and let

\[
 F_0=\{\ell_i u_j:i\ne j\}.
\tag{3.5}
\]

Then \(F_0\) is a 6-cycle and has five indispensable feasible alternating
circuits:

* three 4-cycles, one for each pair \(\{i,j\}\); and
* two 6-cycles, corresponding to the two cyclic orders on three symbols.

But \(\beta(K_{3,3})=9-6+1=4\).  Hence every fundamental basis omits an
indispensable feasible circuit, which cannot be expressed as a conformal
sum of the basis elements.

#### Proof

The complement of (3.5) is the three-edge diagonal matching.  Choosing two
diagonal edges and the two cross edges between their endpoints gives the
three alternating 4-cycles.  The diagonal matching together with either of
the two off-diagonal cyclic perfect matchings gives the two alternating
6-cycles.  Theorem 2.1 makes all five indispensable, while every cycle basis
has cardinality four.  \(\square\)

Thus the correct answer to “minimal generating set” has two meanings.

* A fundamental basis of \(\beta\) cycles is the smallest
  \(\mathbb Z\)-basis for a final global ILP.
* The full Graver family of simple alternating cycles is the unique minimal
  universal conformal catalogue for legal binary toggles.

AEC needs the second notion, or a context-dependent sequential Markov
system.  A fixed \(\mathrm{GF}(2)\) basis is weaker still: an even binary
subgraph can meet a vertex in two old or two new edges and change its degree
from two to zero or four.

## 4. What the MMM quotient supplies unconditionally

### Theorem 4.1 (regularity, dimension, and a disjoint circuit atlas)

The phase-labelled quotient graph \(G\) is connected and
\((m+1)\)-regular on both shores.  Consequently

\[
 |V(G)|=2N,\qquad |E(G)|=(m+1)N,\qquad
 \operatorname {rank}\ker_{\mathbb Z}B=(m-1)N+1.
\tag{4.1}
\]

Write the even cycle \(F_0\) as the disjoint union of its two alternating
perfect matchings

\[
 F_0=M_0\sqcup M_1.
\tag{4.2}
\]

For \(m\ge2\), the complement \(G-F_0\) is an
\((m-1)\)-regular bipartite multigraph and therefore has a 1-factorization

\[
 G-F_0=P_1\sqcup\cdots\sqcup P_{m-1}.
\tag{4.3}
\]

For every \(i\in\{0,1\}\) and \(j\in[m-1]\), the graph

\[
 M_i\cup P_j
\tag{4.4}
\]

is a vertex-disjoint union of simple \(F_0\)-alternating circuits.
Toggling any subcollection in one fixed pair \((i,j)\) gives another
owner-exact 2-factor.  Every complement edge occurs in one such atlas for
each \(i\).

#### Proof

The physical middle-level graph is connected, so its quotient is connected.
The central cyclic action is free, and every physical central vertex has
degree \(m+1\); hence the quotient has the same degree when phase-parallel
edges are counted separately.  This proves (4.1), since row-signing \(B\)
gives the incidence matrix of a connected graph and therefore rank
\(2N-1\).

Every bipartite 2-factor splits into its two alternating perfect matchings.
After removing them, every vertex has degree \(m-1\).  A positive-degree
regular bipartite multigraph has a perfect matching: for a set \(S\) on one
shore, the \(d|S|\) incident edges end in \(N(S)\), whose total incident
capacity is at most \(d|N(S)|\), proving Hall.  Remove the matching and
repeat to get (4.3).  The union of two disjoint perfect matchings is
2-regular and alternates between them, proving (4.4).  \(\square\)

For calibration,

\[
\begin{array}{c|c|c}
k&N&\beta\\ \hline
11&42&169\\
13&132&661\\
15&429&2575
\end{array}
\tag{4.5}
\]

This atlas proves abundant raw circuits and exact Boolean subcubes.  It does
not prove that the toggled factor is connected or that the circuits have
separated phase-labelled shadow collars.

### Theorem 4.2 (full-lattice voltage saturation)

Fix a quotient section, orient every phase edge from \(\mathcal L\) to
\(\mathcal U\), and let \(\alpha(e)\in\mathbb Z_k\) be its phase increment.
Define

\[
 \chi:\ker_{\mathbb Z}B\longrightarrow\mathbb Z_k
\tag{4.6}
\]

by

\[
 \chi(z)=\sum_{e\in E}\alpha(e)z_e\pmod k.
\tag{4.7}
\]

This is independent of the section: a section change adds a vertex
coboundary, whose pairing with the circulation \(z\) vanishes.  Then
\(\chi\) is surjective.  Hence its neutral kernel has index \(k\) and the
same free rank \(\beta\).

#### Proof

The physical middle-level graph is the connected \(C_k\)-voltage lift of
\(G\).  Fix a quotient vertex and one of its physical lifts.  Connectivity
gives, for every sheet \(g\in C_k\), a physical path from the chosen lift to
its translate by \(g\).  Its quotient is a closed walk of voltage \(g\).
Every closed walk is an integer sum of directed simple cycles and
backtracks, the latter having voltage zero.  Thus the simple-cycle lattice
maps onto every \(g\in\mathbb Z_k\).  The kernel of a surjection onto a
finite group has index \(k\) and unchanged free rank.  \(\square\)

This is only a lattice statement.  It does not supply a binary
\(F_0\)-sign-compatible neutral packet, still less a packet with protected
shadow signatures.

## 5. Exact flow boundary and the first chronology obstruction

### Theorem 5.1 (raw factor completion by max flow)

Let \(P\subseteq E\) be a legal partial edge set with \(d_P(v)\le2\), let
\(A\subseteq E\setminus P\) be the allowed residual edges, and put

\[
 b_v=2-d_P(v).
\tag{5.1}
\]

There is a binary set \(Q\subseteq A\) such that \(P\cup Q\) has degree two
at every quotient owner if and only if

\[
 \sum_{v\in\mathcal L}b_v
 =
 \sum_{v\in\mathcal U}b_v
\tag{5.2}
\]

and, for every \(X\subseteq\mathcal L\) and
\(Y\subseteq\mathcal U\),

\[
 b(X)-b(Y)
 \le
 e_A\bigl(X,\mathcal U\setminus Y\bigr).
\tag{5.3}
\]

#### Proof

Use the network

\[
 s\longrightarrow\mathcal L\longrightarrow\mathcal U\longrightarrow t,
\tag{5.4}
\]

with capacities \(b_v\) on the outside arcs and capacity one on each allowed
middle edge.  For the cut whose source side is
\(\{s\}\cup X\cup Y\), the capacity is

\[
 b(\mathcal L\setminus X)
 +e_A(X,\mathcal U\setminus Y)+b(Y).
\]

It is at least the required flow value \(b(\mathcal L)\) exactly when
(5.3) holds.  Max-flow/min-cut proves feasibility, and integral capacities
give a binary middle-edge flow.  \(\square\)

Thus raw owner completion is completely integral.  The diamond contraction
already destroys this blanket TU route.

### Proposition 5.2 (universal determinant-two diamond minor)

Fix one physical lower middle set \(L\) and three distinct coordinates
\(a,b,c\notin L\).  In the unquotiented physical diamond formulation, let a
diamond column \(xy\) mean that the two extensions
\(L+x,L+y\) are chosen over \(L\).  On upper-degree rows
\(L+a,L+b,L+c\) and columns \(ab,bc,ca\), the incidence matrix is

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
\qquad
 \det=2.
\tag{5.5}
\]

Hence the physical contracted diamond/upper-degree matrix is not totally
unimodular for every \(k\ge5\).

This is not an infeasibility theorem, nor a claim that every further
symmetry quotient retains this particular minor.  It proves that integrality
of the raw physical bipartite edge flow cannot simply be inherited after the
two incidences at each lower owner are grouped into one successor diamond.

### Proposition 5.3 (circuit shadow columns are context-dependent)

At a physical lower owner \(L\), suppose the current diamond uses outside
coordinates \((a,b)\).  Let one circuit change \(a\) to \(c\), and a second
change \(b\) to \(d\).  The actual combined upper-\(q1\) change is

\[
 e_{L\cup\{c,d\}}-e_{L\cup\{a,b\}}.
\tag{5.6}
\]

The sum of the two changes evaluated independently at the original diamond
is instead

\[
 \bigl(e_{L\cup\{c,b\}}-e_{L\cup\{a,b\}}\bigr)
 +
 \bigl(e_{L\cup\{a,d\}}-e_{L\cup\{a,b\}}\bigr),
\tag{5.7}
\]

which differs from (5.6).  Sequential evaluation is exact because the
second change becomes

\[
 e_{L\cup\{c,d\}}-e_{L\cup\{c,b\}}.
\tag{5.8}
\]

Therefore even upper-\(q1\) target effects are not fixed additive columns on
individual inclusion-edge circuits unless the circuits are lower-owner
disjoint or are evaluated sequentially in their current context.  At
higher depth, the suffix-prefix cross terms of the signature semigroupoid
give the same obstruction more strongly.

## 6. A quantitative neutral circuit-packet absorption theorem

Fix a maximum shadow depth \(H\le m\), a residence delay \(d\), and put

\[
 h=\max\{H,d\}.
\tag{6.1}
\]

All witness counts below are **quotient based-witness-orbit counts** on the
actual target orbits.  This convention automatically handles short
composite-\(k\) target orbits: one quotient witness orbit covers its whole
physical target orbit, with the stabilizer multiplicity supplied by the
lift.

A **neutral serial circuit packet** \(A\) consists of an equivariant
replacement of one or more disjoint half-open intervals of the physical
lift of \(F_0\), satisfying all of the following.

1. Each replacement is a path through exactly the same upper states and
   lower owners as the old interval.
2. It has the same phase-labelled entry and exit as the old interval.
3. Its difference from the old factor is a sign-compatible compound of the
   Graver circuits in Theorem 2.1.
4. Replacing the intervals preserves the single quotient cycle and has
   voltage increment zero.
5. Its complete old and new \(H\)-shadow and \(d\)-residence collar
   signatures have been evaluated by the half-open signature semigroupoid.

Let \(I_h(A)\) be the set of quotient orbits of physical based starts whose
complete **input state/dart word** for some depth-\(H\) shadow test or
depth-\(d\) residence test differs after applying \(A\), whether or not the
test's final set-valued output happens to remain equal.  Twisted
quotient-lap and physical cyclic seams are included.  Two candidate packets
conflict if their declared replacement-interval position sets overlap, their
\(I_h\)-sets intersect, or their terminal edge supports are incompatible.
The first clause is separate and necessary: an unchanged subsegment of a
declared interval need not itself contain the start of a changed test word.

For a target token \(t=(\varepsilon,q,[T])\), let \(w_0(t)\) be its quotient
witness count in \(F_0\), and let

\[
 \Delta_A(t)=w_A(t)-w_0(t)
\tag{6.2}
\]

be the exact one-packet signature difference.  Partition the quotient
orbits of initial physical based residence violations into rotation-invariant
clusters \(\mathcal R\), let
\(\mathcal Z\) be the target tokens with \(w_0(t)=0\), and put

\[
 \mathcal O=\mathcal R\sqcup\mathcal Z.
\tag{6.3}
\]

### Theorem 6.1 (neutral packet absorption)

Suppose that for every obligation \(o\in\mathcal O\) there is a candidate
list \(\mathcal A_o\), the lists are pairwise disjoint, and every list has
the same cardinality \(L\).  Assume:

1. If \(o=t\in\mathcal Z\), every \(A\in\mathcal A_t\) satisfies

   \[
      \Delta_A(t)\ge1
      \tag{6.4}
   \]

   and creates no new residence violation.
2. If \(o=R\in\mathcal R\), every \(A\in\mathcal A_R\) deletes exactly the
   violations in \(R\), creates none, and leaves every residence test
   outside \(R\) unchanged.
3. For every initially covered target token \(t\),

   \[
   \boxed{
    \sum_{o\in\mathcal O}
       \max_{A\in\mathcal A_o}
       \bigl(-\Delta_A(t)\bigr)_+
       \le w_0(t)-1.}
   \tag{6.5}
   \]
4. The conflict graph on all candidate packets, after deleting edges
   internal to one list, has maximum degree \(\Delta\).
5. If \(\Delta>0\), then

   \[
      L\ge2e\Delta.
      \tag{6.6}
   \]

   If \(\Delta=0\), only \(L\ge1\) is required.

Then one may choose one packet \(A_o\in\mathcal A_o\) for every obligation
so that their simultaneous switch is an owner-exact connected strict
spiral, retains the unit voltage of \(F_0\), is \(d\)-delay resident, and
contains every forced lower and upper fixed-depth state path through \(H\).

#### Proof

Choose one packet uniformly and independently from each list.  For every
conflict edge whose endpoints lie in distinct lists, let the bad event be
that both endpoints are selected.  It has probability \(L^{-2}\).  An event
involving lists \(i,j\) is dependent only on events involving \(i\) or
\(j\).  At most \(L\Delta\) conflict edges meet each list.  Writing \(D\)
for the dependency degree, exclusion of the event itself gives
\(D\le2L\Delta-2\).  Hence

\[
 eL^{-2}(D+1)
 \le
 \frac{e(2L\Delta-1)}{L^2}
 =
 \frac{2e\Delta}{L}-\frac e{L^2}
 <1
\tag{6.7}
\]

under (6.6).  The symmetric Lovász local lemma gives a conflict-free
transversal.

Because the selected \(I_h\)-sets are disjoint, no depth-\(H\) shadow window
or depth-\(d\) residence test meets two selected packets.  The exact
semigroupoid ledgers therefore add:

\[
 w_{\mathrm{final}}(t)
 =
 w_0(t)+\sum_{o\in\mathcal O}\Delta_{A_o}(t).
\tag{6.8}
\]

For \(t\in\mathcal Z\), its assigned packet contributes at least one.
Every other one-packet delta for \(t\) is nonnegative because \(w_0(t)=0\);
disjoint influence prevents another packet from destroying the assigned
witness.  If \(w_0(t)>0\), (6.5) and (6.8) leave at least one witness.
The residence clauses remove the partitioned initial violations and create
none.

Each packet replaces every one of its intervals by an equal-length path
through the same state and owner sets with the same phase-labelled terminals.
The selected interval families are disjoint by the interval-position clause
of the conflict relation; their complete influence sets are disjoint by its
\(I_h\)-clause.  These replacements therefore preserve one
quotient cycle and exact ownership.  Their voltage increments are zero, so
the final voltage is the original unit.  The lift is consequently one
physical strict spiral.  \(\square\)

### Corollary 6.2 (local multiplicity form)

Let the conflict resources consist of every declared replacement-interval
position, the based influence positions, and every phase-labelled terminal
edge/incidence resource whose double use would make two packets incompatible.
Suppose every candidate uses at most

\[
 s
\tag{6.9}
\]

such resources, every conflict is witnessed by a shared resource, and every
resource belongs to at most \(\kappa\) candidates.  Then

\[
 \Delta\le s(\kappa-1).
\tag{6.10}
\]

Thus

\[
 L\ge2es(\kappa-1)
\tag{6.11}
\]

together with (6.4)--(6.5) is sufficient.

#### Proof

For one candidate \(A\), sum over its at most \(s\) conflict resources.
At each resource there are at most \(\kappa-1\) other candidates, proving
(6.10).  Apply Theorem 6.1.  \(\square\)

Within the zero-voltage NSAP framework, nonneutral raw repairs can be
admitted by pairing them with disjoint compensation packets of opposite
voltage modulo \(k\), followed by a fresh audit of the whole compound against
(6.2)--(6.5).  For a general directed packet \(A\), define its **factor
voltage increment**

\[
 \omega(A)=
 v(\hbox{new coherently oriented replacement})
 -
 v(\hbox{old oriented interval})
 \pmod k,
\]

from its phase-labelled half-open path signature.  If packets overlap or are
applied sequentially, this increment is recomputed in the actual current
orientation.  It is not, in general, the raw circulation voltage
\(\chi(A)\) of Theorem 4.2.  Thus, writing \(v_0\) for the voltage of the
initial coherently oriented quotient cycle, the exact terminal test is

\[
 \gcd\!\left(v_0+\sum_A\omega(A),k\right)=1.
\tag{6.12}
\]

Opposite-charge pairing is sufficient, not necessary.  For composite `k`,
a merely nonzero residual charge is never an adequate substitute for the
gcd test.

Taking \(H=m\), Theorem 6.1 is a quantitative sufficient theorem for
`AEC(k,d)`.  It is not a necessary condition.

## 7. The near-bijection obstruction

Let \(O\) be the number of \(C_k\)-orbits of rank-\((m+2)\) targets.
Complementation gives the same number at rank \(m-1\).

### Theorem 7.1 (orbit slack and simultaneous unique starts)

One has

\[
\boxed{
 O=
 \frac1k\left[
 \binom{k}{m+2}
 +
 2\,\mathbf1_{3\mid k}
 \binom{k/3}{(m+2)/3}
 \right].}
\tag{7.1}
\]

Suppose an equivariantly oriented factor/successor is upper-\(q1\) complete
and, with \(d\ge1\), lower-\(q2\) complete.  Each side gives a surjection
from the \(N\) quotient starts onto these \(O\) target orbits.  Put

\[
 S=N-O.
\tag{7.2}
\]

Then

\[
 S=
 \frac{2N}{m+2}
 -
 \frac{2}{k}\mathbf1_{3\mid k}
 \binom{k/3}{(m+2)/3}
 \le\frac{2N}{m+2},
\tag{7.3}
\]

and at least

\[
\boxed{N-4S}
\tag{7.4}
\]

quotient starts are simultaneously the unique quotient witness of both
their upper-\(q1\) and lower-\(q2\) target orbits.

#### Proof

A nonidentity rotation can fix a rank-\((m+2)\) set only when its cycle
length divides both \(k\) and \(m+2\).  Since

\[
 \gcd(k,m+2)=\gcd(k,3),
\]

the only possibility is cycle length three.  When \(3\mid k\), exactly two
rotations have order three, and each fixes

\[
 \binom{k/3}{(m+2)/3}
\]

sets.  Burnside gives (7.1).  Since

\[
 \frac1k\binom{k}{m+2}
 =
 N\frac m{m+2},
\]

equation (7.3) follows.

For a surjection from \(N\) starts onto \(O\) targets, the surplus
\(S=N-O\) equals the sum of `fibre size - 1`.  A fibre of size \(a\ge2\)
contains at most \(2(a-1)\) starts.  Hence at most \(2S\) starts belong to
nonsingleton fibres, and at least \(N-2S\) are unique.  Apply this to both
maps and intersect the two unique-start sets to obtain (7.4).  The
lower-\(q2\) map has the claimed target rank because \(d\ge1\) forbids an
inserted coordinate from being deleted on the next transition.  \(\square\)

Since \(S=O(N/m)\), all but \(O(N/m)\) quotient starts are simultaneously
rigid on these two labels.  An absorber cannot reserve a positive-density
set of starts on which both labels may simply be discarded.

### Corollary 7.2 (physical singleton floor)

For either complete physical target map, the \(W\) based occurrences cover

\[
 T=\binom{k}{m+2}=\frac{m}{m+2}W
\tag{7.5}
\]

targets.  At least

\[
 2T-W=\frac{m-2}{m+2}W
\tag{7.6}
\]

targets have load one.

#### Proof

If \(s\) target fibres are singleton, then

\[
 W\ge s+2(T-s)=2T-s.
\]

Rearrange.  \(\square\)

This obstruction directly audits the reserve inequality (6.5).  For every
quotient target orbit with \(w_0(t)=1\), its right side is zero.  Therefore
**every candidate in every absorber list** must preserve that target.
In a complete upper-\(q1\) map there are at least \(2O-N\) singleton target
orbits, and simultaneous lower-\(q2\) completeness gives (7.4).  Raw circuit
rank does not provide this target-balanced list abundance.

The exact artifacts agree:

* `k=11`: the upper histogram `1^198 2^132` attains (7.6) exactly, giving
  18 singleton quotient target orbits;
* `k=13`: `1^936 2^273 3^78` gives 72 singleton quotient orbits, versus the
  lower bound 66;
* `k=15`: \(N=429\), \(O=335\), and complete quotient slack is \(94\).
  The canonical factor has 38 holes and repeat excess \(132\); filling the
  holes must convert at least \(132-94=38\) repeat slots into new target
  orbits, recovering the exact 38-orbit repair lower bound.

## 8. Audit of the full phase-labelled circuit space based at MMM

The audit splits cleanly into what is proved and what is not.

### Proved

1. **Raw generation.**  Theorem 2.1 gives all binary owner-factor switches,
   and Theorem 4.1 supplies explicit disjoint circuit atlases.
2. **Raw reachability.**  Any two exact owner factors are connected by an
   edge-Hamming-monotone sequence of at most \(2N\) simple alternating
   toggles.  Decorated validity of intermediate factors is not asserted.
3. **Raw completion.**  Theorem 5.1 gives exact integral cut conditions.
4. **Voltage lattice.**  The full cycle-voltage map is onto and has a
   rank-\(\beta\) neutral kernel.
5. **No fixed linear signature matrix.**  Proposition 5.3 proves that
   circuit target effects must be evaluated in context unless owner
   supports are disjoint.
6. **No positive-density private-witness reservoir.**  Theorem 7.1 leaves
   only \(O(N/m)\) quotient slack at the first two nontrivial shadow gates.

### Not proved

For the full phase-labelled circuit space based at \(F_0\), no theorem
supplies:

1. phase-neutral two-terminal packet localization;
2. \(L\) candidates for every missing target orbit and residence cluster;
3. the conflict ratio \(L/\Delta\ge2e\);
4. the singleton-witness reserve inequality (6.5); or
5. context-compatible inverse-voltage compensation for nonneutral repairs.

These failures of proof are substantive.  The cycle rank \(\beta\) counts
linear circulation directions, not phase-labelled path alternatives.  A
fractional mixture may take the first edge of a witness from one factor and
the next edge from another; it does not produce one literal successor path.

The finite artifacts further calibrate the gap.

* At `k=11`, the full phase-labelled circuit space contains an accepting
  endpoint, but it differs from the audited canonical MMM carrier on
  `41/42` lower choices (with the known unfrozen canonical-payload caveat).
  This proves global circuit power, not local list expansion.
* The complete natural MMM gluing-tree/parallel-label family fails the joint
  `k=11` gates.  This rules out NSAP only when every terminal transversal is
  confined to that enumerated factor family.  Compounds of those directions
  outside an MMM labelled spanning tree, and unrestricted Graver compounds,
  are not excluded.
* At `k=15`, the full binary cycle-space dimension is 2575.  The natural MMM
  parametrization exposes at most 131 gluing supports and 14 parallel-label
  supports, hence its outputs lie in an \(\mathbb F_2\)-affine subspace of
  dimension at most 145.  This is an \(\mathbb F_2\) comparison, not a
  rank-145 claim over \(\mathbb Z\) or \(\mathbb R\).  Its failure cannot be
  promoted to a full-space no-go.
* The canonical `k=15` factor needs at least 38 changed lower choices, so no
  terminal factor whose contracted lower-owner support differs from that
  canonical factor at no more than 37 owners can pass.  Temporary supports in a
  sequential route are not bounded by this statement.
* The exact `k=13` optimum uses two quotient components and a physical seam;
  it does not verify strict AEC.

Thus the full phase-labelled circuit space based at an MMM factor satisfies
the algebraic generation, dimension, raw-flow, and voltage-rank parts of the
proposed route.  It is neither proved nor refuted to satisfy its decisive
signature-expansion hypotheses for general odd `k`.

## 9. Exact remaining hypothesis and adversarial audit

The sufficient remaining statement exposed here is strictly more explicit
than AEC.

> **Neutral signature absorber packing `NSAP(k,H,d)`.**  Relative to an MMM
> unit-voltage strict factor, construct neutral serial circuit-packet lists
> satisfying (6.4)--(6.6), with exact context-evaluated semigroupoid
> signatures on every actual target orbit.

By Theorem 6.1,

\[
 \operatorname {NSAP}(k,m,d)
 \quad\Longrightarrow\quad
 \operatorname {AEC}(k,d).
\tag{9.1}
\]

Every remaining hypothesis is explicit:

1. **physical packet existence:** owner-exact two-terminal alternatives;
2. **phase control:** zero total packet voltage;
3. **residence control:** exact deletion of the assigned defect cluster and
   no new defect;
4. **target expansion:** one list for every missing target orbit;
5. **conflict expansion:** \(L\ge2e\Delta\);
6. **reserve:** inequality (6.5) for every already-covered orbit.

The main adversarial checks are as follows.

* A fundamental cycle basis cannot replace the Graver catalogue
  (Proposition 3.2).
* Raw max-flow integrality cannot be lifted through diamonds
  (Proposition 5.2).
* Fixed circuit signature columns are false even at upper `q=1`
  (Proposition 5.3).
* The local-lemma constant includes the full event dependency count in
  (6.7).
* Composite target stabilizers are handled by quotient witness-orbit counts.
* Composite voltage is handled by exact phase neutrality; a merely nonzero
  residual charge is not accepted.
* The reserve condition is not cosmetic: Theorem 7.1 forces it to preserve
  an asymptotically full family of singleton labels.
* Chordless dynamic generation is not claimed to preserve decorated
  validity at intermediate factors.
* The natural MMM family is kept distinct from the full rank-\(\beta\)
  circuit lattice.

No theorem presently proves NSAP for the full phase-labelled circuit space
based at an MMM factor.  The minimal open geometric task on this route is to
construct phase-neutral two-terminal compound packets whose
context-evaluated signatures preserve the singleton
upper-\(q1\)/lower-\(q2\) labels while expanding over all remaining
residence and deeper-shadow obligations.
