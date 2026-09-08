# Lane S: port-rooted middle-level path factors, exact Hall cuts, and the monodromy gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input is
used.

## 0. Outcome

The corrected Section-17 interface is used throughout: the selected Dyck set
must be an endpoint of the infinity-cut Johnson geodesic.  Ordinary
Dyck transversality is never used as a substitute for this port condition.

Let \(J\) have size \(2r\), let

\[
 \mathcal X=\binom Jr,\qquad
 \mathcal Y=\binom J{r+1},\qquad
 \mathcal D=\mathcal D_r,
 \qquad N=|\mathcal D|=\operatorname{Cat}_r,
\]

and put

\[
 \overline{\mathcal D}
   =\{J\setminus P:P\in\mathcal D\}.
\]

The authoritative local target, Theorem 17.3 of the plateau audit, is a
vertex partition of the middle-levels inclusion graph \(M(J)\) into the
\(N\) prescribed paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r=J\setminus P,qquad P\in\mathcal D.       \tag{0.1}
\]

This note proves the following exact refinements and audits.

1. The full problem is equivalently a clean rainbow path-menu exact cover.
2. It is equivalently an integral spanning \(b\)-factor together with an
   explicit family of prescribed-pair cut inequalities.  These inequalities
   are the exact missing monodromy constraints.
3. The degree part alone has a necessary-and-sufficient capacitated
   Gale--Hall criterion and is integral.
4. An acyclic Ordered-Hall condition, including unique complement
   reachability, is a genuine sufficient construction theorem.
5. All its Hall inequalities verify symbolically on the canonical Catalan
   layers.  This recovers the canonical factor, not a new recursive family.
6. The corrected \(r=2\) counterexample fails the endpoint Hall cut already
   at the singleton \(\{23\}\).
7. Correct endpoint degrees still do not force complement monodromy: an
   explicit spanning simple \(b\)-factor at \(r=3\) has a nontrivial
   three-cycle on the roots and violates one pair cut by exactly two.
   Ranks \(1,2\) are rigid, so this separation is minimal.
8. The uniform rectangle switch in
   `MATH_THEOREM_DYCK_TRANSVERSAL_RECTANGLE_FACTOR_20260726.md` really does
   preserve the stronger port condition.  Its variable incidence support is
   one residual \(8\)-cycle with exactly two degree-feasible choices, and both
   have identity complement monodromy.
9. Marginal Hall cannot simply be rounded in the full path menu: after all
   paths internally using another Dyck port have been removed, the rank-four
   path-resource matrix still contains a determinant-\(2\) minor.
10. The restored four-row Tamari packet has an exact remaining-root Hall
   deficit of three, so it cannot be completed to a port-transversal factor.

Thus the port correction does not invalidate the isolated rectangle factor,
but it does invalidate any argument which uses only exact \(X/Y\) histograms,
ordinary transversality, or independently feasible entrance and exit
matchings.  The growing recursive gate is an integral paired-path packing
problem, not an ordinary matching problem.

## 1. Exact counts and literal wreath realizability

The Catalan identity gives

\[
 |\mathcal X|=\binom{2r}{r}=(r+1)N,
 \qquad
 |\mathcal Y|=\binom{2r}{r+1}=rN.                         \tag{1.1}
\]

Every nonempty Dyck word begins with \(1\), whereas its bitwise complement
begins with \(0\).  Hence

\[
             \mathcal D\cap\overline{\mathcal D}=\varnothing. \tag{1.2}
\]

The same statement holds after the affine coordinate relabelling inherited
from an outer recursive context.

### Proposition 1.1 (geodesic enumeration)

For fixed \(P\in\mathcal D\), there are exactly \((r!)^2\) Johnson
geodesics

\[
                   P=X_0,X_1,\ldots,X_r=J\setminus P.     \tag{1.3}
\]

#### Proof

At each of the \(r\) steps one element originally in \(P\) is removed and
one element originally in \(J\setminus P\) is inserted.  Geodesicity forces
every element of \(P\) to be removed exactly once and every element of its
complement to be inserted exactly once.  Conversely, an arbitrary ordering
of the \(r\) removals and an arbitrary ordering of the \(r\) insertions
define a geodesic.  The two orders are independent. \(\square\)

### Proposition 1.2 (the graph path is a literal wreath)

Every path (1.3), after inserting

\[
 Y_t=X_t\cup X_{t+1},\qquad
 Z_t=\{\infty\}\cup(J\setminus Y_t),                      \tag{1.4}
\]

gives a literal cyclic-order wreath

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{r-1},X_r.                     \tag{1.5}
\]

#### Proof

Write

\[
 X_{t+1}=X_t-\{p_{t+1}\}+\{q_{t+1}\}.
\]

By Proposition 1.1, \(p_1,\ldots,p_r\) enumerate \(P\) and
\(q_1,\ldots,q_r\) enumerate \(J\setminus P\).  On the edge
\(X_tZ_t\), the unique omitted coordinate is \(q_{t+1}\); on the edge
\(Z_tX_{t+1}\), it is \(p_{t+1}\).  On the closing edge \(X_rX_0\), it
is \(\infty\).  Thus the omitted-coordinate sequence is

\[
 q_1,p_1,q_2,p_2,\ldots,q_r,p_r,\infty,                  \tag{1.6}
\]

a permutation of \(J\sqcup\{\infty\}\).  The standard omitted-coordinate
description of a minimum odd-graph cycle now gives a cyclic order whose
length-\(r\) windows are exactly (1.5).  Hence no abstract graph cycle is
being substituted for a literal wreath.  For completeness, the states are
distinct: \(X_t\) contains exactly \(r-t\) elements of \(P\), while
\(Y_t\) contains exactly \(r-t\) elements of \(P\); for \(s<t\), the
element \(p_{s+1}\) lies in \(Y_s\setminus Y_t\).  Thus the \(Y_t\), and
hence the \(Z_t\), are pairwise distinct. \(\square\)

## 2. The clean path-menu exact-cover theorem

A candidate path for \(P\) is **clean** when none of its internal
\(X\)-states lies in
\(\mathcal D\cup\overline{\mathcal D}\).  Cleanliness is necessary in a
complete port-transversal factor: all \(2N\) members of those two endpoint
families are already exhausted by the prescribed endpoints.

For a clean geodesic

\[
 \gamma=(P=X_0,X_1,\ldots,X_r=J\setminus P)
\]

define its nonprivate resource set

\[
 R(\gamma)=
 \{X_1,\ldots,X_{r-1}\}\mathbin{\dot\cup}
 \{X_{t-1}\cup X_t:1\le t\le r\}.                       \tag{2.1}
\]

It has \(2r-1\) elements.  Indeed the internal \(X_t\) are distinct by
their number \(r-t\) of surviving elements of \(P\), and for \(s<t\) the
element \(p_{s+1}\) belongs to \(Y_s\setminus Y_t\), so all \(r\)
\(Y\)-colours are distinct.  The full nonprivate resource universe is

\[
 \mathcal R=
 \bigl(\mathcal X\setminus
       (\mathcal D\cup\overline{\mathcal D})\bigr)
 \mathbin{\dot\cup}\mathcal Y,
 \qquad |\mathcal R|=(2r-1)N.                            \tag{2.2}
\]

Let \(\Gamma_P\) be any nonempty allowed menu of clean geodesics for root
\(P\).

### Theorem 2.1 (exact rooted path-menu matching)

A \(\mathcal D\)-port-transversal local factor using only paths in the
menus \(\Gamma_P\) exists if and only if one can select one
\(\gamma_P\in\Gamma_P\) for every \(P\in\mathcal D\) so that the sets
\(R(\gamma_P)\) are pairwise disjoint.

#### Proof

In a path factor, internal states and \(Y\)-vertices belong to unique
paths, so disjointness is necessary.  Conversely, the selected paths have
private and mutually distinct prescribed endpoints.  Their nonprivate
resource sets are disjoint and have total size

\[
                  N(2r-1)=|\mathcal R|.                  \tag{2.3}
\]

They therefore partition \(\mathcal R\).  Together with the prescribed
endpoints, the paths partition every vertex of \(M(J)\), and Theorem 17.3
reconstructs the required port-transversal literal factor. \(\square\)

Equivalently, with binary variables \(z_{P,\gamma}\), the exact equations
are

\[
 \sum_{\gamma\in\Gamma_P}z_{P,\gamma}=1
       \quad(P\in\mathcal D),                             \tag{2.4}
\]

and

\[
 \sum_{P,\gamma:\rho\in R(\gamma)}z_{P,\gamma}=1
       \quad(\rho\in\mathcal R).                         \tag{2.5}
\]

This is a coloured uniform-hypergraph exact matching problem.  Ordinary
set-union Hall inequalities are necessary but are not sufficient for a
general hypergraph of this rank.

### Proposition 2.2 (weighted fractional Hall criterion)

Let \(A\) be the \(0\)-\(1\) matrix of (2.4)--(2.5), including both the
root rows and the resource rows.  The fractional system

\[
                         Az=\mathbf1,qquad z\ge0          \tag{2.6}
\]

is feasible if and only if, for every real weight vector
\(w=(w_\rho)_{\rho\in\mathcal R}\),

\[
 \boxed{
 \sum_{\rho\in\mathcal R}w_\rho
 \ \ge\
 \sum_{P\in\mathcal D}
       \min_{\gamma\in\Gamma_P}
       \sum_{\rho\in R(\gamma)}w_\rho.}                 \tag{2.7}
\]

#### Proof

Farkas' lemma says that (2.6) is feasible exactly when

\[
 \sum_Pa_P+\sum_\rho w_\rho\ge0                          \tag{2.8}
\]

for every \((a,w)\) satisfying

\[
 a_P+\sum_{\rho\in R(\gamma)}w_\rho\ge0
       \quad(P\in\mathcal D,\ \gamma\in\Gamma_P).       \tag{2.9}
\]

For fixed \(w\), the smallest admissible \(a_P\) is the negative of the
minimum in (2.7).  Substitution in (2.8) gives precisely (2.7). \(\square\)

If \(A\) were totally unimodular, (2.7) would be sufficient for an
integral factor.  Section 9 proves that the port-clean Catalan path matrix
is already non-TU at \(r=4\).

## 3. Exact paired \(b\)-factor and pair-cut normal form

Define a demand on the vertices of \(M(J)\) by

\[
 b(X)=
 \begin{cases}
  1,&X\in\mathcal D\cup\overline{\mathcal D},\\
  2,&X\in\mathcal X\setminus
          (\mathcal D\cup\overline{\mathcal D}),
 \end{cases}
 \qquad
 b(Y)=2\quad(Y\in\mathcal Y).                            \tag{3.1}
\]

For \(S\subseteq V(M(J))\), let

\[
 \kappa_{\mathcal D}(S)=
 \#\bigl\{P\in\mathcal D:
       |\{P,J\setminus P\}\cap S|=1\bigr\}.             \tag{3.2}
\]

Thus \(\kappa_{\mathcal D}(S)\) is the number of prescribed complement
pairs separated by \(S\).

### Theorem 3.1 (exact paired-factor cut theorem)

For an edge set \(F\subseteq E(M(J))\), the following are equivalent.

1. \(F\) is the union of the \(N\) paths (0.1), and those paths partition
   every vertex of \(M(J)\).
2. The exact degree equations
   \[
                         d_F(v)=b(v)\quad(v\in V(M(J)))   \tag{3.3}
   \]
   hold, and every vertex set satisfies the prescribed-pair cuts
   \[
       \boxed{|F\cap\delta(S)|\ge\kappa_{\mathcal D}(S)
          \quad(S\subseteq V(M(J))).}                    \tag{3.4}
   \]

#### Proof

Suppose first that \(F\) is a desired path factor.  Equation (3.3) is
immediate.  Every prescribed path whose endpoints are separated by \(S\)
must use at least one edge of \(\delta(S)\).  Distinct paths are
edge-disjoint, so these crossing edges prove (3.4).

Conversely, (3.3) makes every component of \(F\) a path or a cycle.  Its
degree-one vertices are exactly the \(2N\) members of
\(\mathcal D\cup\overline{\mathcal D}\), so it has exactly \(N\) path
components.  Let \(K\) be one such component and take \(S=V(K)\).  Then

\[
                         F\cap\delta(S)=\varnothing.
\]

By (3.4), \(\kappa_{\mathcal D}(S)=0\).  Since \(K\) contains exactly
two degree-one vertices, they must be one prescribed pair
\(P,J\setminus P\).

The demand totals on the two shores are

\[
 \sum_{X\in\mathcal X}b(X)
 =2N+2\bigl((r+1)N-2N\bigr)=2rN,
 \qquad
 \sum_{Y\in\mathcal Y}b(Y)=2rN.                         \tag{3.5}
\]

Consequently

\[
 |F|=\frac12\sum_{v\in V(M(J))}b(v)=2rN.                \tag{3.6}
\]

The distance in \(M(J)\) between \(P\) and \(J\setminus P\) is
\(2r\): every two-edge step changes at most one element of the current
\(r\)-set, and all \(r\) elements must be changed.  The \(N\) prescribed
path components therefore use at least \(2rN\) edges.  Equality (3.6)
forces every one of them to have length exactly \(2r\), and leaves no edge
for a cycle component.  Thus they are precisely the paths (0.1). \(\square\)

### Corollary 3.2 (virtual complement-edge form)

Adjoin the fixed virtual matching

\[
 Q=\{\{P,J\setminus P\}:P\in\mathcal D\}.               \tag{3.7}
\]

Then (3.3) says that \(F\cup Q\) is a spanning \(2\)-factor.  The desired
objects are exactly those \(2\)-factors in which every cycle contains
exactly one virtual edge of \(Q\).  The inequalities (3.4) are the exact
pair-separation, or subtour-elimination, constraints.

Theorem 3.1 is integral: it characterizes the desired \(0\)-\(1\) edge
sets.  It does **not** assert that the linear relaxation obtained by adding
(3.4) to the degree polytope is integral.

## 4. What ordinary capacitated Hall proves

Let \(G\subseteq M(J)\) be an allowed incidence support.  For
\(A\subseteq\mathcal X\) and \(B\subseteq\mathcal Y\), write
\(e_G(A,\mathcal Y\setminus B)\) for the number of allowed inclusion
edges between those sets, and put \(b(B)=2|B|\).

### Theorem 4.1 (exact Gale--Hall criterion for the degree ledger)

The support \(G\) contains a simple integral \(b\)-factor satisfying
(3.3) if and only if

\[
 \boxed{
 b(A)\le e_G(A,\mathcal Y\setminus B)+2|B|
 \quad(A\subseteq\mathcal X,\ B\subseteq\mathcal Y).}    \tag{4.1}
\]

Equivalently, for every \(A\subseteq\mathcal X\),

\[
 \boxed{
 b(A)\le
 \sum_{Y\in\mathcal Y}\min\{2,d_A^G(Y)\},}             \tag{4.2}
\]

where \(d_A^G(Y)=|N_G(Y)\cap A|\).

#### Proof

Use the network

\[
 s\longrightarrow\mathcal X\longrightarrow\mathcal Y
   \longrightarrow t
\]

with capacities \(b(X)\), \(1\) on every allowed inclusion edge, and
\(2\), respectively.  A cut whose source side contains precisely
\(A\) on the \(\mathcal X\)-shore and \(B\) on the
\(\mathcal Y\)-shore has capacity

\[
 b(\mathcal X\setminus A)
 +e_G(A,\mathcal Y\setminus B)+2|B|.                     \tag{4.3}
\]

The total required flow is \(b(\mathcal X)=2rN\), equal to the total
sink capacity.  Max-flow/min-cut gives (4.1), and integral capacities give
an integral edge selection.  Minimizing the right side of (4.1)
independently at each \(Y\) gives (4.2). \(\square\)

This theorem settles exactly the unlabelled ownership ledger.  It does not
imply (3.4).  The first invalid inference in a scalar Hall argument is

\[
 \text{integral degree factor}
 \quad\not\Longrightarrow\quad
 \text{prescribed complement endpoint pairing}.          \tag{4.4}
\]

Proposition 7.2 below gives a fully saturated simple witness to (4.4) at
the minimal rank \(r=3\).

### Proposition 4.2 (endpoint Hall after an unrooted factor)

Suppose a vertex partition \(\mathcal Q\) of \(M(J)\) into \(N\)
length-\(2r\) complement paths has already been built, but its endpoints
have not been assigned to \(\mathcal D\).  Form a bipartite graph with
left shore \(\mathcal D\) and right shore the components of
\(\mathcal Q\), joining \(P\) to a component exactly when \(P\) is an
endpoint of that component.

Then \(\mathcal Q\) is \(\mathcal D\)-port-transversal if and only if

\[
                         |N(A)|\ge |A|
              \quad\text{for every }A\subseteq\mathcal D. \tag{4.5}
\]

#### Proof

There are \(N\) roots and \(N\) components.  A matching saturating
\(\mathcal D\) assigns each root to a distinct component on which it is an
endpoint.  The other endpoint of that complement path is automatically
\(J\setminus P\).  Conversely, a port-transversal orientation supplies
such a perfect matching. \(\square\)

In this special graph every \(P\) lies in only one path component.  Because
the components are complement paths and
\(\mathcal D\cap\overline{\mathcal D}=\varnothing\), (4.5) simply says
that every Dyck set is an endpoint, not an internal state; two Dyck roots
cannot be absorbed by one complementary endpoint pair.  This is exactly
the distinction missed by ordinary transversality.

## 5. A genuine sufficient Ordered-Hall theorem

The pair cuts can be enforced structurally by retaining endpoint labels in
an acyclic support.

Let \(\vec G\) be an acyclic directed subgraph obtained by orienting some
edges of \(M(J)\).  Assume no arc enters \(\mathcal D\) and no arc leaves
\(\overline{\mathcal D}\).  Put

\[
 \mathcal U=\mathcal X\mathbin{\dot\cup}\mathcal Y.
\]

Form the successor bipartite graph

\[
 B_{\vec G}:
 (\mathcal U\setminus\overline{\mathcal D})_L
 \longleftrightarrow
 (\mathcal U\setminus\mathcal D)_R,                     \tag{5.1}
\]

where \(u_Lv_R\) is an edge exactly when \(u\to v\) is an arc of
\(\vec G\).  Both shores of (5.1) have size \(2rN\).

Also form the reachability graph \(R_{\vec G}\) from
\(\mathcal D\) to \(\overline{\mathcal D}\): join \(P\) to
\(J\setminus Q\) when \(\vec G\) has a directed path from the former to
the latter.

### Theorem 5.1 (Ordered-Hall complement-path theorem)

Assume

\[
 |N_{B_{\vec G}}(S)|\ge |S|
 \quad\text{for every }
 S\subseteq(\mathcal U\setminus\overline{\mathcal D})_L, \tag{5.2}
\]

and assume that the unique perfect matching of \(R_{\vec G}\) is

\[
                         P\longmapsto J\setminus P.       \tag{5.3}
\]

Then \(\vec G\) contains a vertex partition of the form (0.1).

#### Proof

Hall's theorem applied to (5.1) gives a perfect matching.  Select the
corresponding directed arcs.  Every vertex outside
\(\overline{\mathcal D}\) has one selected successor, and every vertex
outside \(\mathcal D\) has one selected predecessor.  Since
\(\vec G\) is acyclic, these arcs form a spanning directed path cover,
with sources exactly \(\mathcal D\) and sinks exactly
\(\overline{\mathcal D}\).

Its source-to-sink pairing is a perfect matching in \(R_{\vec G}\), so
(5.3) makes it the complement matching.  There are \(N\) paths and
\(2rN\) selected arcs.  Each prescribed complement path has length at
least \(2r\); hence all have length exactly \(2r\).  They are the paths
(0.1). \(\square\)

### Proposition 5.2 (triangular test for the reachability condition)

Assume every diagonal reachability \(P\leadsto J\setminus P\) is present.
Make a digraph on \(\mathcal D\) with an off-diagonal arc

\[
 P\longrightarrow Q
 \quad\Longleftrightarrow\quad
 P\leadsto J\setminus Q,qquad P\ne Q.                   \tag{5.4}
\]

Then the complement matching is the unique perfect matching of
\(R_{\vec G}\) if and only if the digraph (5.4) is acyclic.

#### Proof

A directed cycle in (5.4) replaces the diagonal matching on its vertices
by a cyclically shifted perfect matching.  Conversely, the symmetric
difference of any second perfect matching with the diagonal matching
contains an alternating cycle, which gives a directed cycle in (5.4).
\(\square\)

Theorem 5.1 is deliberately a sufficient theorem, not a claim that every
useful substitution admits such an acyclic support.  Its value is that all
three obligations are explicit: Hall saturation, exact \(Y\)-vertex use,
and complement monodromy.

## 6. Symbolic verification on the canonical Catalan layers

Orient every canonical MSW path from its Dyck port to its complementary
port.  For every nonterminal \(X\)-state let \(g(X)\) be the next
\(Y\)-vertex, and for every \(Y\)-vertex let \(h(Y)\) be the next
\(X\)-state.  Exact canonical ownership makes

\[
 g:\mathcal X\setminus\overline{\mathcal D}
      \longrightarrow\mathcal Y,
 \qquad
 h:\mathcal Y\longrightarrow
      \mathcal X\setminus\mathcal D                    \tag{6.1}
\]

inclusion-preserving bijections.  Put \(f=h\circ g\).  If

\[
 L_t=f^t(\mathcal D),\qquad C_t=g(L_t),                  \tag{6.2}
\]

then

\[
 \mathcal X=\mathop{\dot\bigcup}_{t=0}^{r}L_t,
 \qquad
 \mathcal Y=\mathop{\dot\bigcup}_{t=0}^{r-1}C_t,
 \qquad |L_t|=|C_t|=N,                                  \tag{6.3}
\]

with

\[
 L_0=\mathcal D,\qquad L_r=\overline{\mathcal D},
 \qquad f^r(P)=J\setminus P.                            \tag{6.4}
\]

These are the canonical Chung--Feller flaw layers.

The ordinary Hall cuts verify symbolically, not by finite inspection.  For
every \(S\subseteq\mathcal X\setminus\overline{\mathcal D}\),

\[
                         g(S)\subseteq N(S),
 \qquad |g(S)|=|S|,                                      \tag{6.5}
\]

and for every \(T\subseteq\mathcal Y\),

\[
                         h(T)\subseteq N(T),
 \qquad |h(T)|=|T|.                                      \tag{6.6}
\]

Thus both incidence matchings pass every Hall cut.  If the directed
support is restricted to the canonical arcs, its successor graph has a
unique perfect matching and its source-to-sink reachability graph is
diagonal.  Theorem 5.1 therefore reproduces the canonical
\(\mathcal D\)-port-transversal factor.

Explicitly, a mixed left-shore set in (5.1) has the form
\(S_X\mathbin{\dot\cup}S_Y\).  Its neighbor set contains
\(g(S_X)\mathbin{\dot\cup}h(S_Y)\); the two images lie on opposite right
shores, so they are disjoint and have total size
\(|S_X|+|S_Y|\).  Hence (6.5)--(6.6) verify the full mixed Hall condition
(5.2), not only its two pure-shore restrictions.

The roots split by first return at position \(2j\):

\[
 \mathcal D_{r,j}
 =\{1u0v:u\in\mathcal D_{j-1},\ v\in\mathcal D_{r-j}\},
 \qquad
 |\mathcal D_{r,j}|
 =\operatorname{Cat}_{j-1}\operatorname{Cat}_{r-j}.     \tag{6.7}
\]

Indeed \(u\) and \(v\) are chosen independently.  Summing (6.7) gives
the Catalan convolution \(N\).  In the canonical endpoint graph of
Proposition 4.2, every set \(A\subseteq\mathcal D\) has
\(|N(A)|=|A|\); in particular a union of first-return classes has the
exact size obtained by summing (6.7).

This symbolic verification proves that the Hall theorem has the correct
Catalan normalization and all floor-free constants.  It only recovers the
canonical trajectory.  It does not prove that an arbitrary
profile-changing support has diagonal reachability.

## 7. The corrected \(r=2\) counterexample and its exact failed cut

Let

\[
 J=\{1,2,3,4\},\qquad \mathcal D=\{23,24\}.              \tag{7.1}
\]

The cyclic orders in corrected Section 17 yield the two middle-level paths

\[
 12-123-23-234-34,
 \qquad
 24-124-14-134-13.                                      \tag{7.2}
\]

The \(X\)-vertices in (7.2) are all six two-sets exactly once, and the
\(Y\)-vertices are

\[
                         123,234,124,134,                 \tag{7.3}
\]

all four three-sets exactly once.  The first path contains \(23\), and the
second contains \(24\), so ordinary \(\mathcal D\)-transversality holds.

However, the ports of the first path are \(12,34\); its selected Dyck set
\(23\) is internal.  In the endpoint graph of Proposition 4.2,

\[
                         N(\{23\})=\varnothing,            \tag{7.4}
\]

so the singleton Hall cut fails by one.  Equivalently, in the correct
degree system (3.1),

\[
 d_F(23)=2\ne1=b(23),
 \qquad
 d_F(12)=1\ne2=b(12).                                    \tag{7.5}
\]

Thus this counterexample does not merely have the wrong orientation; it
does not enter the port-correct \(b\)-factor polytope at all.  This is the
first exact invalid implication in the old argument:

\[
 \text{exact }X/Y\text{ ledgers plus ordinary transversality}
 \quad\not\Longrightarrow\quad
 \text{port-rooted complement paths}.                    \tag{7.6}
\]

### Proposition 7.2 (degree Hall and complement monodromy first separate at \(r=3\))

For the standard family

\[
 \mathcal D_3=\{123,124,125,134,135\},                  \tag{7.7}
\]

the following five vertex-disjoint paths partition all vertices of
\(M([6])\):

\[
\begin{aligned}
 K_1={}&123-1236-136-1346-146-1246-126-1256-156-1456-456,\\
 K_2={}&124-1234-234-2346-236-2356-256,\\
 K_3={}&125-1235-235-2345-345-3456-346,\\
 K_4={}&135-1356-356,\\
 K_5={}&134-1345-145-1245-245-2456-246.
\end{aligned}                                             \tag{7.8}
\]

Their edge union \(F\) is therefore a simple integral \(b\)-factor with
the correct endpoint set
\(\mathcal D_3\cup\overline{\mathcal D}_3\), but its endpoint map is

\[
\begin{aligned}
 123&\longmapsto\overline{123},
 &125&\longmapsto\overline{125},\\
 124&\longmapsto\overline{134},
 &134&\longmapsto\overline{135},
 &135&\longmapsto\overline{124}.
\end{aligned}                                             \tag{7.9}
\]

Thus the last three roots have nontrivial three-cycle monodromy.  Moreover,
for

\[
                         S=V(K_4)=\{135,1356,356\},       \tag{7.10}
\]

one has

\[
                         |F\cap\delta(S)|=0,
 \qquad                  \kappa_{\mathcal D_3}(S)=2.     \tag{7.11}
\]

This is the smallest possible rank for such a separation.

#### Proof

Every consecutive pair in (7.8) is an inclusion edge.  Its lower-shore
vertices are

\[
\begin{aligned}
 &123,124,125,126,134,135,136,145,146,156,\\
 &234,235,236,245,246,256,345,346,356,456,
\end{aligned}                                             \tag{7.12}
\]

all twenty three-subsets of \([6]\).  Its upper-shore vertices are

\[
\begin{aligned}
 &1234,1235,1236,1245,1246,1256,1345,1346,1356,1456,\\
 &2345,2346,2356,2456,3456,
\end{aligned}                                             \tag{7.13}
\]

all fifteen four-subsets.  Hence (7.8) is a spanning simple \(b\)-factor,
and its displayed endpoints give (7.9).

The set (7.10) is an entire component, so no selected edge leaves it.  It
contains \(135\) but not its complement \(246\), and it contains
\(356=\overline{124}\) but not \(124\).  No other prescribed pair is
separated.  This proves (7.11).

For \(r=1\), the factor is forced.  For \(r=2\), with
\(\mathcal D_2=\{12,13\}\), the two internal lower vertices \(14,23\)
have ambient degree two and demand two, so all four of their incidences are
forced.  Each \(Y\)-vertex then needs one endpoint incidence.  The residual
endpoint--\(Y\) support is the cycle

\[
              12-123-13-134-34-234-24-124-12.            \tag{7.14}
\]

Its two perfect matchings give, respectively, the complement path pairs

\[
\begin{aligned}
 &12-123-23-234-34,
 &&13-134-14-124-24,\\
 \text{or }\quad
 &13-123-23-234-24,
 &&34-134-14-124-12.
\end{aligned}                                             \tag{7.15}
\]

Both have complement monodromy.  Thus ranks \(1,2\) are rigid and
\(r=3\) is minimal. \(\square\)

## 8. Port audit of the uniform rectangle switch

Fix \(r\ge2\) and put

\[
 R=\{5,7,\ldots,2r-1\}.
\]

Use the shorthand

\[
 \begin{array}{lll}
 A=12R,&B=14R,&C=34R,\\
 D=13R,&E=23R,&F=24R.
 \end{array}                                             \tag{8.1}
\]

The two canonical paths begin

\[
                         A,B,C,\ldots,
 \qquad
                         D,E,F,\ldots,                    \tag{8.2}
\]

and the switched paths begin

\[
                         A,E,C,\ldots,
 \qquad
                         D,B,F,\ldots.                    \tag{8.3}
\]

All later states are unchanged.  The roots \(A,D\) and the final
complementary endpoints are therefore literally fixed.  In particular,
the roots remain the first states of the infinity-cut geodesics; they are
not merely distinguished internal owners.

The old and new \(Y\)-vertex multisets are both

\[
                 \{123R,124R,134R,234R\}.                \tag{8.4}
\]

The state multiset is unchanged because \(B,E\) are exchanged.  After the
unchanged tails and all other canonical paths are adjoined, Theorem 17.3
directly proves that (8.3) gives a
\(\mathcal D_r\)-port-transversal exact factor.  The proof does not rely
on ordinary transversality.  Exact \(X\)-ownership and the fact that all
Dyck sets already occur as fixed roots also prevent a second Dyck state in
any row.  Directly, \(E\) omits coordinate \(1\), while \(B\) has negative
Dyck height after its third bit.

There is a stronger support audit.  The four common incidences through
the exchanged internal vertices are

\[
 B-124R,\quad B-134R,
 \qquad
 E-123R,\quad E-234R.                                    \tag{8.5}
\]

These incidences really are forced, rather than being chosen by convention:
the support degree of each of \(B,E\) is exactly its demand two.  Every
untouched vertex outside the displayed two-row slab also has support degree
equal to its demand, so all of its incidences are forced.  In particular,
when \(r>2\), the common outgoing incidences after \(C,F\) are forced from
their untouched \(Y\)-endpoints.  (For \(r=2\), \(C,F\) are already the
terminal ports.)  After deleting all these forced incidences, the residual
demand is one at each vertex of the single cycle

\[
 \boxed{
 A-124R-F-234R-C-134R-D-123R-A.}                         \tag{8.6}
\]

An even cycle has exactly two perfect matchings.  In (8.6) they give
precisely the old and new decompositions.  Including the forced incidences,
they connect the same two boundary pairs:

\[
 \begin{array}{lll}
 \text{old:}&A-124R-B-134R-C,&D-123R-E-234R-F,\\
 \text{new:}&A-123R-E-234R-C,&D-134R-B-124R-F.
 \end{array}                                             \tag{8.7}
\]

Thus every degree-feasible choice in this isolated support preserves the
continuations \(A\leadsto C\) and \(D\leadsto F\).  The tails after
\(C,F\) are fixed, so complement monodromy is the identity.

Here “degree-feasible” means a simple incidence \(b\)-factor.  If the two
incidence matchings \(\mathcal X\to\mathcal Y\) and
\(\mathcal Y\to\mathcal X\) are toggled independently, there are formally
four marginal choices.  The two off-diagonal choices select one incidence
twice (respectively \(B-124R\) or \(B-134R\)) and create an alternating
two-cycle; they are not simple path factors.  The two diagonal choices are
exactly (8.2) and (8.3).

All Gale--Hall inequalities also hold without enumeration.  If \(F_0\)
is the canonical factor and \(G\) is the union support, then for every
\(S\subseteq\mathcal X\),

\[
 b(S)=\sum_{Y\in\mathcal Y}e_{F_0}(S,\{Y\})
 \le \sum_{Y\in\mathcal Y}\min\{2,d_S^G(Y)\}.            \tag{8.7a}
\]

This is exactly (4.2).  The residual-cycle argument supplies the extra
pair rigidity which the scalar inequality does not contain.

More generally, index the old path cores and let \(\alpha\) send each start
index to the core to which that start is newly attached, while \(\beta\)
sends each end index to the core to which that end is newly attached.  The
new endpoint permutation is

\[
                              \beta^{-1}\alpha.           \tag{8.8}
\]

The rectangle is safe because both attachment permutations are the same
transposition.  Overlapping rectangles require equality of the accumulated
start and end permutations; the degree Hall inequalities do not record
this condition.

The rectangle also shows why freezing \(Y\)-colours phase by phase is too
strong.  For \(r=2\), its phase-colour pairs change as

\[
 \{124,123\},\ \{134,234\}
 \quad\longrightarrow\quad
 \{123,134\},\ \{234,124\}.                             \tag{8.9}
\]

Only the aggregate \(Y\)-vertex ledger is invariant, as required by
Theorem 17.3.

## 9. Two exact failures of marginal Hall rounding

### Proposition 9.1 (fixed entrance and exit matchings collide)

Use the standard order \(J=[2r]\) and assume \(r\ge2\).  Every
\(P\in\mathcal D_r\) contains \(1\) and omits \(2r\).  Hence

\[
 e(P)=P\cup\{2r\},
 \qquad
 x(P)=(J\setminus P)\cup\{1\}                            \tag{9.1}
\]

are respectively legal first and last \(Y\)-colours for a
\(P\)-to-\(J\setminus P\) geodesic.  The maps \(e\) and \(x\) are each
injective, so the two marginal endpoint matchings separately satisfy Hall.

Nevertheless,

\[
                         |e(\mathcal D_r)\cap x(\mathcal D_r)|
                         =2^{r-1}.                         \tag{9.2}
\]

#### Proof

The equality \(e(P)=x(Q)\) is equivalent to

\[
                 Q=\{1\}\cup([2,2r-1]\setminus P).       \tag{9.3}
\]

For a Dyck set \(P\), write

\[
                         h_P(t)=2|P\cap[t]|-t.
\]

For the set \(Q\) in (9.3),

\[
                         h_Q(t)=2-h_P(t)
                  \quad(1\le t\le2r-1).                  \tag{9.4}
\]

Thus \(Q\) is Dyck exactly when \(P\) has height at most two.  A primitive
Dyck excursion of semilength \(s\) and height at most two is uniquely

\[
                              1(10)^{s-1}0.
\]

An arbitrary height-at-most-two Dyck path is a concatenation of these
primitive excursions, and their semilengths form a composition of \(r\).
There are \(2^{r-1}\) compositions.  Since both maps in (9.1) are
injective, this proves (9.2). \(\square\)

The \(2^{r-1}\) overlaps are duplicate demands on literal \(Y\)-vertices.
Therefore these two **specified fixed** endpoint matchings \(e\) and \(x\)
cannot be imposed simultaneously.  The calculation does not obstruct all
variable entrance/exit matchings; it proves that a joint, variable-colour
construction is necessary.

### Proposition 9.2 (the clean path-menu matrix is not TU)

At \(r=4\), take \(P=1234\) and \(J\setminus P=5678\).  Consider the
three geodesics

\[
\begin{aligned}
 \gamma_1&:1234,2345,2356,2567,5678,\\
 \gamma_2&:1234,2345,3457,4567,5678,\\
 \gamma_3&:1234,2346,3456,4567,5678.
\end{aligned}                                             \tag{9.5}
\]

Their \(Y\)-lists are

\[
\begin{aligned}
 \gamma_1&:(12345,23456,23567,25678),\\
 \gamma_2&:(12345,23457,34567,45678),\\
 \gamma_3&:(12346,23456,34567,45678).
\end{aligned}                                             \tag{9.6}
\]

Every internal state in (9.5) omits \(1\), so none is Dyck.  Their
complements are

\[
 1678,1478,1348,1268,1238,1578,1278,                     \tag{9.7}
\]

as repetitions are removed; each violates the Dyck prefix condition.
Thus all three columns survive the mandatory deletion of paths which use
another member of
\(\mathcal D_4\cup\overline{\mathcal D}_4\) internally.

On the three resource rows

\[
                         12345,\qquad45678,\qquad23456,
\]

the incidence columns of \(\gamma_1,\gamma_2,\gamma_3\) form

\[
 \begin{pmatrix}
 1&1&0\\
 0&1&1\\
 1&0&1
 \end{pmatrix},                                          \tag{9.8}
\]

whose determinant is \(2\).  Hence the cleaned matrix in
(2.4)--(2.5) is not totally unimodular.  It is also not balanced, because
(9.8) has odd order and exactly two ones in every row and every column.

The three resource rows alone have the familiar half-solution
\(z_1=z_2=z_3=1/2\), but that vector does not satisfy the root equation,
whose sum would be \(3/2\).  The exact conclusion is therefore limited and
rigorous: a generic TU or balanced-matrix rounding proof for the full
port-clean path menu is impossible.  Additional Catalan structure would be
needed.

## 10. The exact remaining-root Hall cut for partial packets

### Lemma 10.1 (a completable \(k\)-packet uses exactly \(k\) Dyck states)

Let \(\mathcal P\) be a fixed family of \(k\) vertex-disjoint prescribed
paths which is extendable to a complete
\(\mathcal D_r\)-port-transversal factor.  Then the union of its
\(X\)-states contains exactly \(k\) members of \(\mathcal D_r\), namely
its \(k\) initial ports.

#### Proof

A complete factor has \(N\) paths and exactly \(N\) Dyck states.  Its
\(N\) distinct initial ports already exhaust those states, so no Dyck state
can occur internally.  Quantitatively, if the fixed packet consumes
\(c\) Dyck states, the remaining \(N-k\) path slots have only \(N-c\)
available roots.  Their root-side Hall condition requires

\[
                         N-c\ge N-k.                      \tag{10.1}
\]

Thus \(c\le k\), while the \(k\) prescribed ports give \(c\ge k\).
\(\square\)

The port-restored rank-four Tamari packet
\(\mathcal P^\star\) in
`MATH_ATTACK_E_FOUR_ROW_TAMARI_ASSOCIATOR_20260726.md` has \(k=4\) but
uses the seven Dyck states

\[
 1237,1245,1246,1247,1256,1257,1347.                     \tag{10.2}
\]

The ten remaining paths consequently have only seven unused Dyck roots.
The root Hall deficit is exactly

\[
                              10-7=3.                     \tag{10.3}
\]

Thus rowwise restoration of four complementary endpoint pairs is not
enough: that packet cannot be contained in a full port-transversal factor.
This agrees with Proposition 7.3 of the associator report and is now an
immediate cut in the authoritative path-factor normal form.

## 11. Precise proved and open boundary

The following statements are proved.

1. The local substitution problem, including literal wreath realizability,
   is exactly the clean rooted path-menu matching of Theorem 2.1.
2. Integral edge sets solving it are exactly the \(b\)-factors satisfying
   all pair cuts (3.4).
3. The projected degree ledger has the exact integral Gale--Hall theorem
   4.1.
4. Ordered Hall plus unique complement reachability is sufficient and
   verifies symbolically for the canonical Catalan layers.
5. Ordinary transversality fails before the correct endpoint-degree
   constraints in the audited \(r=2\) example.
6. Even after the endpoint degrees are corrected, ordinary Gale--Hall is
   strictly weaker than the pair cuts: the explicit \(r=3\) factor (7.8)
   has a three-cycle endpoint monodromy and fails (3.4) by exactly two.
   This separation is impossible for \(r\le2\).
7. The uniform isolated rectangle switch fixes both physical ports and has
   only two degree-feasible residual choices, both complement-paired.  Its
   construction is therefore valid under the corrected Section-17
   interface.
8. Fixed marginal entrance/exit Hall systems have an exact
   \(2^{r-1}\) joint colour collision, and the clean rank-four path matrix
   has a determinant-\(2\) obstruction to generic TU rounding.
9. The four-row Tamari packet fails completion by an exact root Hall deficit
   of three.

What remains unproved is a growing, profile-changing support for which an
integral \(b\)-factor satisfies all pair cuts (3.4), or equivalently a
clean path-menu exact matching with the required global recursive shadow
effect.  For an atlas of overlapping switches, one must prove equality of
the accumulated start and end attachment permutations, not merely
histogram cancellation.  No constant-one conclusion follows here.
