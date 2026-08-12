# Whole-transversal stationary coupling for truncated rotors

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome and exact boundary

Let

\[
 W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H},\qquad
 M=m+H,\qquad T=MN_H,
\tag{0.1}
\]

where \(H\) is the calibrated first crossing

\[
 {W\over N_H}\ge M.
\tag{0.2}
\]

Thus \(T\le W\), and in the calibrated regime \(T=W-o(W)\). Let
\(Q=o(m)\) be the truncated-rotor depth; in the intended application

\[
 Q=\left\lceil\sqrt{m(\log\log m+\gamma)}\right\rceil,
 \qquad \gamma\to\infty,
 \qquad \gamma=o(\log\log m).
\tag{0.3}
\]

This note proves the following exact statements.

1. Fix an integral multiset of rooted flag columns and resolve each
   column as a truncated rotor state. There is a legal fixed-top Markov
   coupling having exactly that multiset as its stationary measure if
   and only if a **weighted Hall inequality** holds at every top. The
   coupling can be chosen integral: after labeling repeated occurrences,
   it is one legal successor permutation. At state multiplicity \(a\),
   its projected transition probabilities have denominator dividing
   \(a\).

2. Rotor chronology gives a simpler necessary condition which is not
   visible in rank loads. At every fixed top, the multiplicity of an
   ordered consecutive \(k\)-block in the queue is independent of its
   queue position. In particular all \(2Q\) queue-coordinate histograms
   must agree. Departure, arrival, and every queue-slot flux then agree
   coordinatewise.

3. A legal successor permutation factors the prescribed columns into
   directed cycles. Cutting one edge in every cycle gives literal rotor
   paths. If the total number of resulting components is \(C\), their
   exact compiled length is

   \[
     T+(2Q+1)C.
   \tag{0.4}
   \]

   Thus the exact reset requirement is

   \[
     (2Q+1)C=o(W).
   \tag{0.5}
   \]

4. There is an all-orders sufficient law for (0.5). Suppose the legal
   successor permutation \(\sigma_U\) at each top has a distribution for
   which every specified directed simple cycle of length \(\ell\) has
   probability at most

   \[
     {\theta_U\over(M)_\ell}.
   \tag{0.6}
   \]

   Here \((M)_\ell=M(M-1)\cdots(M-\ell+1)\).

   Then

   \[
     \mathbb E\,c(\sigma_U)\le \theta_U H_M,
     \qquad H_M=\sum_{j=1}^{M}{1\over j}.
   \tag{0.7}
   \]

   Consequently the balanced columns admit a deterministic legal path
   factorization of length \(W+o(W)\) whenever

   \[
     (2Q+1)H_M\sum_U\theta_U=o(W).
   \tag{0.8}
   \]

   In particular, a uniform bound \(\theta_U\le\theta\) is enough when

   \[
     \theta\,{Q\log M\over M}=o(1).
   \tag{0.9}
   \]

5. For the uniform law on all legal successor permutations, (0.6) is an
   exact permanent-ratio condition on principal minors of the legal
   adjacency matrix. It is a genuine **whole-transversal** condition,
   not a pairwise marginal estimate.

The balanced Boolean-flow theorem supplies the prescribed columns but does
not presently supply the fixed-top queue stationarity, weighted Hall, or
cycle law (0.6). Therefore the results below are a conditional integral
factorization theorem and an exact obstruction test. They do not prove
coefficient one by themselves.

## 1. From a rooted flag column to a rotor state

Fix a top \(U\in\binom{[2m]}M\). A full rooted flag column \(c\) contains
a nested chain

\[
 F_{m-H}(c)\subset F_{m-H+1}(c)\subset\cdots
 \subset F_M(c)=U,
 \qquad |F_r(c)|=r.
\tag{1.1}
\]

Its radius-\(Q\) resolution is

\[
 L(c)=F_{m-Q}(c),
\tag{1.2}
\]

\[
 z_i(c)=F_{m-Q+i}(c)\setminus F_{m-Q+i-1}(c)
 \qquad(1\le i\le2Q),
\tag{1.3}
\]

and

\[
 R_U(c)=U\setminus F_{m+Q}(c).
\tag{1.4}
\]

Thus

\[
 \omega(c)=(L(c);z_1(c),\ldots,z_{2Q}(c);R_U(c))
\tag{1.5}
\]

is a valid truncated quotient state:

\[
 |L|=m-Q,\qquad |R_U|=H-Q,
\tag{1.6}
\]

and its displayed parts partition \(U\).

A rotor edge chooses \(x\in L\), \(y\in R_U\), and sends

\[
 (L;z_1,\ldots,z_{2Q};R_U)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2Q-1};R_U-y+z_{2Q}).
\tag{1.7}
\]

Write \(\omega\to\eta\) when (1.7) holds for some \(x,y\).
The top \(U\) is invariant, so every coupling condition below must hold
separately inside each top.

The integral balanced top-rooted flow has exactly \(M\) columns at every
top and \(T\) columns in total. Its middle load is at most one, because

\[
 {T\over W}={MN_H\over W}\le1.
\tag{1.8}
\]

Hence all its middle owners are distinct. In particular, its \(M\)
resolved states at one top are distinct. We nevertheless formulate the
transport theorem with arbitrary integer state multiplicities; no
singleton assumption is needed.

## 2. Weighted Hall is equivalent to a stationary legal coupling

Fix one top \(U\). Let \(\Omega_U\) be the finite set of resolved states
which occur in the prescribed column multiset, and let

\[
 a(\omega)\in\mathbb Z_{\ge0},\qquad
 s_U=\sum_{\omega\in\Omega_U}a(\omega).
\tag{2.1}
\]

For \(\mathcal A\subseteq\Omega_U\), put

\[
 N^+(\mathcal A)
 =\{\eta\in\Omega_U:\omega\to\eta
       \text{ for some }\omega\in\mathcal A\}.
\tag{2.2}
\]

### Theorem 2.1 (fixed-multiplicity stationary transport)

The following are equivalent.

1. There is a Markov kernel \(K_U\) on \(\Omega_U\), supported on legal
   rotor edges, for which

   \[
     \pi_U(\omega)={a(\omega)\over s_U}
   \tag{2.3}
   \]

   is stationary.

2. There is a nonnegative integral edge flow \(f_U(\omega,\eta)\),
   supported on legal rotor edges, with

   \[
   \sum_\eta f_U(\omega,\eta)=a(\omega),
   \qquad
   \sum_\omega f_U(\omega,\eta)=a(\eta).
   \tag{2.4}
   \]

3. For every \(\mathcal A\subseteq\Omega_U\),

   \[
     \boxed{
     \sum_{\omega\in\mathcal A}a(\omega)
     \le
     \sum_{\eta\in N^+(\mathcal A)}a(\eta).}
   \tag{WH}
   \]

When these conditions hold, one may take

\[
 K_U(\omega,\eta)
 ={f_U(\omega,\eta)\over a(\omega)}
 \quad(a(\omega)>0).
\tag{2.5}
\]

Thus every entry in row \(\omega\) has denominator dividing
\(a(\omega)\). After replacing each state by \(a(\omega)\) labeled
copies, \(f_U\) is the projection of one perfect matching, equivalently
one deterministic legal successor permutation of all \(s_U\)
occurrences.

#### Proof

Suppose first that \(K_U\) exists. Put

\[
 g(\omega,\eta)=a(\omega)K_U(\omega,\eta).
\tag{2.6}
\]

The row sums of \(g\) are \(a(\omega)\), and stationarity of (2.3) says
that its column sums are \(a(\eta)\). For a set \(\mathcal A\), all mass
leaving \(\mathcal A\) enters \(N^+(\mathcal A)\); hence (WH) follows.

Conversely, form a bipartite network with a left and a right copy of
\(\Omega_U\). Give the source-to-left-\(\omega\) arc capacity
\(a(\omega)\), every legal left-\(\omega\)-to-right-\(\eta\) arc capacity
\(s_U\), and the right-\(\eta\)-to-sink arc capacity \(a(\eta)\).
The max-flow min-cut theorem says that a flow of value \(s_U\) exists
exactly when (WH) holds. All capacities are integral, so an integral
maximum flow exists. Its middle-arc values give (2.4). Formula (2.5)
then gives a legal kernel, and

\[
 \sum_\omega \pi_U(\omega)K_U(\omega,\eta)
 ={1\over s_U}\sum_\omega f_U(\omega,\eta)
 ={a(\eta)\over s_U}.
\tag{2.7}
\]

Finally expand every state into \(a(\omega)\) copies. Join every left
copy of \(\omega\) to every right copy of \(\eta\) whenever
\(\omega\to\eta\). An integral flow (2.4) splits into a perfect matching
of this expanded graph, and conversely. Identifying its left and right
vertex sets turns that matching into a permutation of the labeled
occurrences. \(\square\)

For the actual balanced flow, \(a(\omega)=1\). The theorem then says that
the stationary kernel may be chosen deterministic. Weighted Hall is not
a fractional relaxation in this case: it is exactly the existence of a
legal successor permutation of the \(M\) prescribed columns at that top.

### Corollary 2.2 (exact Hall deficiency)

In the expanded occurrence graph let \(\nu_U\) be the maximum matching
size. Then

\[
 \Delta_U:=s_U-\nu_U
 =\max_{\mathcal A\subseteq\Omega_U}
 \left(
   \sum_{\omega\in\mathcal A}a(\omega)
   -\sum_{\eta\in N^+(\mathcal A)}a(\eta)
 \right)_+.
\tag{2.8}
\]

In particular \(\Delta_U>0\) is an exact obstruction to a stationary
coupling, and at least \(\Delta_U\) left occurrences remain unmatched in
every partial legal successor assignment.

#### Proof

This is the deficiency form of the bipartite max-flow min-cut theorem
applied to the same network. \(\square\)

## 3. Queue-block stationarity is an unavoidable fixed-top invariant

Weighted Hall contains a chronology constraint which can be tested before
any matching calculation.

For an ordered \(k\)-tuple
\(\mathbf u=(u_1,\ldots,u_k)\) of distinct coordinates of \(U\), define

\[
 Q_{j,k}(\mathbf u)
 =\sum_{\omega\in\Omega_U}a(\omega)
   \mathbf1\!\left[
    (z_j(\omega),\ldots,z_{j+k-1}(\omega))=\mathbf u
   \right]
\tag{3.1}
\]

for \(1\le j\le2Q-k+1\).

### Theorem 3.1 (queue-block conservation)

If the equivalent conditions of Theorem 2.1 hold, then, for every
\(1\le k\le2Q-1\) and every \(\mathbf u\),

\[
 \boxed{
 Q_{1,k}(\mathbf u)=Q_{2,k}(\mathbf u)=\cdots
 =Q_{2Q-k+1,k}(\mathbf u).}
\tag{QS}
\]

In particular the multiplicity histogram of \(z_i\) is independent of
\(i\).

Let \(d_U(u)\) and \(b_U(u)\) be respectively the total integral edge-flow
mass in (2.4) on transitions whose departure is \(x=u\) and whose arrival
is \(y=u\). Then, for every coordinate \(u\in U\),

\[
 \boxed{
 d_U(u)=b_U(u)
 =\sum_\omega a(\omega)\mathbf1[z_i(\omega)=u]
 \quad(1\le i\le2Q).}
\tag{3.2}
\]

#### Proof

On every legal edge \(\omega\to\eta\), (1.7) gives

\[
 (z_{j+1}(\eta),\ldots,z_{j+k}(\eta))
 =(z_j(\omega),\ldots,z_{j+k-1}(\omega)).
\tag{3.3}
\]

Sum (3.3), as an indicator identity, with weights
\(f_U(\omega,\eta)\). The row sums in (2.4) give
\(Q_{j,k}(\mathbf u)\), while the column sums give
\(Q_{j+1,k}(\mathbf u)\). Iteration proves (QS).

Also \(z_1(\eta)=x\) on every edge. Row and column conservation therefore
give

\[
 d_U(u)=\sum_\eta a(\eta)\mathbf1[z_1(\eta)=u].
\tag{3.4}
\]

The \(L\)-update is \(L'=L-x+y\). Summing the change of
\(\mathbf1[u\in L]\) over a stationary edge flow gives
\(-d_U(u)+b_U(u)=0\). Finally the \(R_U\)-update is
\(R_U'=R_U-y+z_{2Q}\), so stationarity gives

\[
 -b_U(u)+\sum_\omega a(\omega)
   \mathbf1[z_{2Q}(\omega)=u]=0.
\tag{3.5}
\]

Combine these identities with the \(k=1\) case of (QS). \(\square\)

This condition is fixed-top and ordered. Exact global load balance of the
sets \(F_r(c)\) does not by itself imply (QS) separately in every top, nor
does it control the consecutive queue-word counts with \(k\ge2\). A
balanced-flow construction intended for stationary rotor transport must
therefore impose (QS), or prove weighted Hall directly.

## 4. Integral path factorization and exact reset cost

Work on the expanded set \(V_U\) of \(s_U\) labeled occurrences. A
partial matching \(P\) in the legal successor bipartite graph becomes a
directed graph on \(V_U\) in which every vertex has indegree and outdegree
at most one. Its components are directed paths, directed cycles, and
isolated vertices. Let \(c(P)\) be its number of directed-cycle
components.

### Proposition 4.1 (exact component formula)

The number of components of \(P\) is

\[
 p(P)=s_U-|P|+c(P).
\tag{4.1}
\]

Deleting one edge from every directed cycle turns all components into
legal directed paths and leaves their number equal to \(p(P)\). Hence the
minimum legal path-factor component count is exactly

\[
 p_U^*=\min_P\bigl(s_U-|P|+c(P)\bigr),
\tag{4.2}
\]

where the minimum is over all partial legal matchings.

If weighted Hall holds and \(P\) is a perfect matching, then

\[
 p(P)=c(P).
\tag{4.3}
\]

#### Proof

Every path or isolated component has one more vertex than edge, while
every cycle has equally many vertices and edges. Summing these identities
gives (4.1). Removing one edge from each of the \(c(P)\) cycles decreases
both \(|P|\) and \(c(P)\) by \(c(P)\), so (4.1) is unchanged and all
components become paths. Conversely every vertex-disjoint legal path
factor supplies such an acyclic partial matching. This proves (4.2), and
(4.3) is immediate when \(|P|=s_U\). \(\square\)

The Hall deficiency gives the unconditional lower bound

\[
 p_U^*\ge\Delta_U,
\tag{4.4}
\]

but Hall alone gives no useful upper bound on the number of cycles in a
perfect matching.

### Proposition 4.2 (literal compilation ledger)

Let the prescribed balanced family have \(T\) state occurrences in total,
and choose a legal path factor at every top. If the total number of path
components is

\[
 C=\sum_U p_U,
\tag{4.5}
\]

then all prescribed radius-\(Q\) flags compile literally in a word of
length

\[
 \boxed{L=T+(2Q+1)C.}
\tag{4.6}
\]

No prescribed rank load changes under the factorization.

#### Proof

A directed rotor path with \(\ell\) state endpoints is initialized by the
\(2Q+2\) nonzero masks which expose its first state. Each of its remaining
\(\ell-1\) states costs one further mask. Its exact length is therefore

\[
 2Q+2+(\ell-1)=\ell+2Q+1.
\tag{4.7}
\]

Sum (4.7) over the \(C\) components. The sum of their endpoint counts is
\(T\), proving (4.6). Reordering columns into paths neither deletes nor
duplicates any state occurrence, so every flag multiplicity is unchanged.
\(\square\)

Since \(T\le W\), the reset term is \(o(W)\) precisely under

\[
 (2Q+1)C=o(W).
\tag{4.8}
\]

In particular it is enough to have \(C=o(W/Q)\).

## 5. Matching-covered components and an exact rational denominator

Weighted Hall always gives a cycle cover, but a stationary kernel need not
be irreducible. The exact irreducible decomposition can also be read from
the legal occurrence graph.

Assume Hall on \(V_U\). Let \(E_U^*\) be the set of legal directed edges
which belong to at least one perfect matching, and let

\[
 \kappa_U=\#\{\text{strong components of }(V_U,E_U^*)\}.
\tag{5.1}
\]

### Theorem 5.1 (matching-covered stationary decomposition)

1. Every edge of \(E_U^*\) has both endpoints in the same strong
   component. In particular there are no \(E_U^*\)-edges between the
   components counted by \(\kappa_U\).

2. Every doubly stochastic legal coupling on the labeled occurrences has
   at least \(\kappa_U\) closed communicating classes.

3. There is a rational doubly stochastic legal coupling with exactly
   \(\kappa_U\) communicating classes and common denominator

   \[
     D_U\le 1+2(s_U-\kappa_U).
   \tag{5.2}
   \]

4. Multiplying this coupling by \(D_U\) gives a directed integral
   Eulerian multigraph. It has exactly \(\kappa_U\) Euler circuits, total
   length \(D_U s_U\), and visits every prescribed occurrence exactly
   \(D_U\) times as a tail.

#### Proof

If \(e=v\to w\) lies in a perfect matching, identify that matching with
its permutation \(\sigma\) of \(V_U\). The edge \(v\to w\) lies on one
directed cycle of \(\sigma\), so \(v,w\) are in the same strong component
of \(E_U^*\). This proves the first assertion.

Every doubly stochastic matrix is a convex combination of permutation
matrices. If one of its entries is positive, at least one permutation in
a Birkhoff decomposition uses that edge; hence every positive support edge
lies in \(E_U^*\). The first assertion then forces at least
\(\kappa_U\) closed classes.

For every non-singleton strong component \(C\), choose a root and the union
of one in-arborescence and one out-arborescence. This is a strongly
connected spanning set with at most \(2|C|-2\) edges. Let \(F\) be the
union of these sets over all components. Then

\[
 |F|\le2(s_U-\kappa_U).
\tag{5.3}
\]

Choose one base perfect matching \(P_0\). For each \(e\in F\), choose a
perfect matching \(P_e\) containing \(e\), which is possible by the
definition of \(E_U^*\). The average of \(P_0\) and the \(|F|\) matrices
\(P_e\) is doubly stochastic, has denominator

\[
 D_U=1+|F|\le1+2(s_U-\kappa_U),
\tag{5.4}
\]

and has strongly connected support inside every component. A singleton
component receives its loop from \(P_0\), because no matching-covered edge
can leave it. Thus the average has exactly \(\kappa_U\) communicating
classes.

The sum of the \(D_U\) permutation matrices has indegree and outdegree
\(D_U\) at every occurrence. Its support is strongly connected in every
one of the \(\kappa_U\) pieces. Each piece therefore has an Euler circuit.
Their total edge count is \(D_U s_U\), and the outdegree identity gives
exactly \(D_U\) visits at every occurrence. \(\square\)

This theorem is an exact stationary-measure factorization, but its scale
factor can be as large as \(2M-1\). Repeating every column \(D_U\) times
is not acceptable for coefficient one. The unscaled problem is therefore
to find one perfect matching with few cycles, not merely an irreducible
rational average of many perfect matchings.

## 6. A whole-transversal law with logarithmically many cycles

Assume now that the \(M\) balanced columns at a fixed top are distinct and
that Hall holds. Let \(\mathfrak M_U\) be the set of legal successor
permutations. A probability law \(\mathbb P_U\) on
\(\mathfrak M_U\) is a whole-transversal law. Its average transition
matrix is automatically doubly stochastic, so the uniform measure on the
prescribed columns is stationary.

For \(1\le\ell\le M\), a directed simple \(\ell\)-cycle is a cyclically
ordered list

\[
 \mathcal C=(v_1,\ldots,v_\ell),
 \qquad v_i\to v_{i+1},\quad v_\ell\to v_1,
\tag{6.1}
\]

of distinct columns, modulo cyclic rotation. Write
\(\mathcal C\subset\sigma\) when all its successor equations occur in
\(\sigma\).

### Theorem 6.1 (cycle-cylinder criterion)

Suppose that, for some \(\theta_U\ge0\),

\[
 \boxed{
 \mathbb P_U(\mathcal C\subset\sigma)
 \le {\theta_U\over(M)_\ell}}
\tag{CT}
\]

for every directed simple \(\ell\)-cycle \(\mathcal C\) and every
\(1\le\ell\le M\). Then

\[
 \boxed{
 \mathbb E_U c(\sigma)\le\theta_UH_M.}
\tag{6.2}
\]

For a family of tops satisfying (CT), there is a deterministic choice of
one legal successor permutation at every top with total cycle count

\[
 C\le H_M\sum_U\theta_U.
\tag{6.3}
\]

#### Proof

For every permutation \(\sigma\), its number of cycles is the exact
cylinder sum

\[
 c(\sigma)=
 \sum_{\ell=1}^{M}
 \sum_{\substack{\mathcal C\text{ directed simple}\\|\mathcal C|=\ell}}
 \mathbf1[\mathcal C\subset\sigma].
\tag{6.4}
\]

There are at most

\[
 {(M)_\ell\over\ell}
\tag{6.5}
\]

directed simple cycles of length \(\ell\) on \(M\) labeled vertices. Take
expectations in (6.4), apply (CT), and sum:

\[
 \mathbb E_Uc(\sigma)
 \le\sum_{\ell=1}^{M}{(M)_\ell\over\ell}
       {\theta_U\over(M)_\ell}
 =\theta_UH_M.
\tag{6.6}
\]

Choose the permutations independently over the tops. Their expected total
cycle count is at most the right side of (6.3), so at least one
deterministic choice attains that bound. \(\square\)

### Corollary 6.2 (exact reset accounting under the whole law)

Under (CT), the radius-\(Q\) portions of all balanced columns compile in
length

\[
 L\le T+(2Q+1)H_M\sum_U\theta_U.
\tag{6.7}
\]

Thus (0.8) implies \(L\le W+o(W)\). If
\(\theta_U\le\theta\) for all \(U\), then, since

\[
 N_H\le {W\over M},
\tag{6.8}
\]

one has

\[
 L\le W+(2Q+1)\theta {W\over M}H_M.
\tag{6.9}
\]

Consequently

\[
 \boxed{\theta\,{Q\log M\over M}=o(1)}
\tag{6.10}
\]

is sufficient. In particular \(\theta=O(1)\) gives

\[
 C=O(N_H\log M)=O(W\log M/M)=o(W/Q)
\tag{6.11}
\]

in the regime (0.3).

#### Proof

Apply Theorem 6.1, cut one edge in every chosen permutation cycle, and use
Proposition 4.2. Equations (6.8)--(6.11) follow from the crossing
inequality (0.2), \(H_M\le1+\log M\), and
\(Q\log M/M=o(1)\). \(\square\)

The conclusion preserves the prescribed multiplicities at every compiled
rank \(m-Q,\ldots,m+Q\) exactly: every selected state column occurs once,
and only its predecessor and successor in the factorization have changed.
There is no temporal accumulation of pairwise marginal errors. The rotor
word does not by this argument expose the portions of the abstract columns
outside the radius-\(Q\) band.

### Proposition 6.3 (permanent form of the whole law)

Let \(A_U\) be the \(M\times M\) zero-one legal adjacency matrix, and use
the uniform law on its legal successor permutations. For a directed
simple cycle \(\mathcal C\) with vertex set \(S\),

\[
 \boxed{
 \mathbb P_U(\mathcal C\subset\sigma)
 ={\operatorname{per}A_U[V_U\setminus S,V_U\setminus S]
   \over \operatorname{per}A_U}.}
\tag{6.12}
\]

Here the permanent of the empty matrix is \(1\). Therefore (CT) follows
from the principal-minor inequalities

\[
 \operatorname{per}A_U[V_U\setminus S,V_U\setminus S]
 \le {\theta_U\over(M)_{|S|}}\operatorname{per}A_U
\tag{6.13}
\]

for every vertex set \(S\) which supports a directed simple cycle.

#### Proof

Once the successor equations on \(\mathcal C\) are fixed, all rows and all
columns indexed by \(S\) have been used exactly once. The remaining
successor choices are in bijection with perfect matchings of the principal
complement \(A_U[V_U\setminus S,V_U\setminus S]\). Divide their number by
the total number \(\operatorname{per}A_U\) of legal permutations.
\(\square\)

Condition (6.13) is not established for the actual balanced columns. It
controls cylinder events of every order up to \(M\), whereas the previous
pairwise propagation estimates control only bounded-order marginals. This
is precisely why (6.13), if proved for a suitably chosen balanced flow,
would avoid temporal iteration.

## 7. A local zero-edge family and what it does not prove

The following example shows that top multiplicity, full nestedness, and
distinct middle owners do not by themselves imply even one legal
successor. It is not claimed to have the global floor/ceiling balance of
the calibrated Boolean flow.

Assume \(m-Q\ge2\) and \(H-Q\ge2\), as holds in the intended regime. Fix
a top \(U\), and fix distinct coordinates

\[
 Z=(z_1,\ldots,z_{2Q}).
\tag{7.1}
\]

Put \(C_0=U\setminus Z\). Since

\[
 \binom{|C_0|}{m-Q}
 =\binom{M-2Q}{m-Q}\ge M
\tag{7.2}
\]

for all sufficiently large \(m\), choose \(M\) distinct subsets
\(L_1,\ldots,L_M\subset C_0\) of size \(m-Q\), and put

\[
 R_i=C_0\setminus L_i,
 \qquad
\omega_i=(L_i;z_1,\ldots,z_{2Q};R_i).
\tag{7.3}
\]

For completeness, if \(N=M-2Q\), then both \(m-Q\) and \(H-Q\) lie
between \(2\) and \(N-2\). Hence unimodality gives
\(\binom N{m-Q}\ge\binom N2\), and
\(\binom N2\ge M\) eventually because \(Q=o(M)\).

Their middle owners

\[
 X_i=L_i\cup\{z_1,\ldots,z_Q\}
\tag{7.4}
\]

are distinct. Each central chain extends to a full nested flag column:
delete \(H-Q\) elements below \(L_i\), and add the \(H-Q\) elements of
\(R_i\) above \(L_i\cup Z\), in arbitrary orders.

Nevertheless there is no edge \(\omega_i\to\omega_j\). Indeed a successor
of \(\omega_i\) has second queue coordinate \(z_1\), while every
\(\omega_j\) has second queue coordinate \(z_2\ne z_1\). Equivalently,
the first and second slot histograms violate (QS). Thus its Hall
deficiency is \(M\).

This example is only a local sanity obstruction. It does not refute the
existence of a specially chosen globally balanced flow whose columns obey
(QS), weighted Hall, and (CT). It proves that those properties must come
from additional ordered, fixed-top structure and cannot be inferred from
the owner count or nested-column property alone.

## 8. Precise surviving theorem gate

Let \(\mathcal C\) be an integral balanced top-rooted flag flow with exactly
\(M\) columns at every top. The following statement is now rigorously
sufficient for the truncated hard band:

> **Balanced whole-transversal rotor law.** Resolve the columns of
> \(\mathcal C\) as in Section 1. For every top \(U\), their legal
> adjacency graph satisfies Hall and admits a law on legal successor
> permutations satisfying (CT), with
>
> \[
> (2Q+1)H_M\sum_U\theta_U=o(W).
> \tag{8.1}
> \]

Under this statement, Theorem 6.1 and Proposition 4.2 give an integral
legal rotor path factorization which preserves every balanced flag
multiplicity in the compiled radius-\(Q\) band and has total reset cost
\(o(W)\).

The unresolved part is not a one-round transversal and not pairwise
pseudorandom propagation. It is the construction of the balanced flow
with the fixed-top ordered invariants (QS), Hall, and a small-cycle
whole-transversal law. Conversely, failure of (QS) or a positive Hall
deficiency (2.8) is an exact obstruction to the stationary-coupling route.
Even when Hall holds, the unscaled coefficient-one ledger still requires
few cycles in one integral successor permutation; the rational
irreducibility theorem of Section 5 does not remove that requirement.
