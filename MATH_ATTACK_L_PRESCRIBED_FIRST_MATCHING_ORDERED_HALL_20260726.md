# Prescribed-first port completion: exact Hall duality, monodromy cycles, and Ordered-Hall

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

Audit: the ordinary/capacitated Hall identities, cycle and pair-cut
criteria, metric Ordered-Hall step, triangular reachability, interval
uncrossing, clean-support degree/shadow formulas, and the fractional cut
dual were independently re-derived. The literal omitted-coordinate lift
and the rank-three forced row/column interval obstruction were also checked
independently. All corrections from those audits are incorporated below.

## 0. Outcome

Let \(r\ge1\), let \(J\) have size \(2r\), and put

\[
 \mathcal X=\binom Jr,\qquad
 \mathcal Y=\binom J{r+1},\qquad
 \mathcal D=\mathcal D_r,\qquad
 \overline{\mathcal D}
   =\{J\setminus P:P\in\mathcal D\},\qquad
 N=\operatorname {Cat}_r.
\]

There are two meanings of a prescribed first matching.

* A **root-first matching** prescribes only the first edge out of every
  \(P\in\mathcal D\).
* A **complete first matching** prescribes the entire upward incidence
  matching
  \[
       M^\uparrow:
       \mathcal X\setminus\overline{\mathcal D}
             \longrightarrow\mathcal Y.
  \]

The second is the stronger and cleaner problem. This note proves:

1. “Balanced” must mean that \(M^\uparrow\) is a bijection: every lower
   source and every \(Y\)-resource is used exactly once. Balance of an
   insertion-label histogram is weaker and is not enough.
2. After a balanced \(M^\uparrow\) is fixed, completion of the degree
   ledger is exactly one bipartite perfect-matching problem. Ordinary Hall,
   its two-parameter cut form, its weighted Farkas dual, and the assignment
   LP are all equivalent. The LP is integral.
3. The selected second matching has an exact endpoint permutation
   \(T\). It gives the required port factor if and only if every cycle of
   \(T\) contains exactly one Dyck root. Root-free cycles are internal
   cycles; cycles containing several roots are precisely wrong endpoint
   monodromy.
4. The pair-cut inequalities are exactly the missing global condition for
   an integral second matching. They give an exact integer program and a
   fractional cut dual, but no integrality theorem for that strengthened
   relaxation. Ordinary Hall proves the degree and \(Y\)-resource ledgers
   and nothing about these cuts.
5. There is a stronger Ordered-Hall theorem than the previously recorded
   acyclic-support version. Hall plus **unique diagonal complement
   reachability** gives the exact defect identity (4.3); no separate
   acyclicity hypothesis is needed. At zero defect, the Catalan edge count
   rules out long paths and internal cycles.
6. If either the allowed exits or, after transposition, the predecessor
   Catalan stars are intervals in one common order, all exponentially many
   Hall inequalities reduce exactly to trapped-interval inequalities. The
   same holds for cyclic intervals.
7. This interval theorem is genuinely conditional. At \(r=3\), for every
   balanced first matching in the full clean support, forced triples rule
   out a common interval order on either shore. Independently, consecutive
   intervals in the standard Catalan root order can all pass while a
   nonconsecutive two-root Hall cut fails.

Thus the strongest proved completion route is:

\[
\boxed{
\begin{array}{c}
\text{balanced prescribed }M^\uparrow\\
+\ \text{Hall or exact interval Hall for }M^\downarrow\\
+\ \text{unique diagonal root--complement reachability}
\end{array}
\Longrightarrow
\text{one literal }\mathcal D_r\text{-port factor}.}
\]

The remaining construction problem is to exhibit a profile-changing
balanced first matching whose residual exit graph has a verifiable Hall
certificate and triangular complement reachability.

## 1. Two matching coordinates

The Catalan identities give

\[
 |\mathcal X|=(r+1)N,\qquad |\mathcal Y|=rN.
\]

Here \(\mathcal D\cap\overline{\mathcal D}=\varnothing\): under the
standard Dyck-set convention every member of \(\mathcal D\) contains
coordinate \(1\), whereas its complement does not.

Set

\[
 L=\mathcal X\setminus\overline{\mathcal D},\qquad
 R=\mathcal X\setminus\mathcal D,\qquad
 I=\mathcal X\setminus
      (\mathcal D\cup\overline{\mathcal D}).
                                                        \tag{1.1}
\]

Then

\[
                         |L|=|R|=|\mathcal Y|=rN.       \tag{1.2}
\]

A port path factor, oriented from \(P\) to \(\overline P\), alternates
between two perfect incidence matchings

\[
 M^\uparrow:L\longrightarrow\mathcal Y,\qquad
 M^\downarrow:\mathcal Y\longrightarrow R.             \tag{1.3}
\]

The incidence pair \(x\subset Y\supset z\) is the contraction of the
literal odd-graph two-edge segment

\[
 x\;--\;Z_Y\;--\;z,
 \qquad Z_Y=\{\infty\}\cup(J\setminus Y).              \tag{1.3a}
\]

Thus retaining one \(Y\)-resource exactly once is the same as retaining its
literal intermediate odd-graph vertex exactly once.

### Lemma 1.1 (omitted-coordinate reconstruction is literal)

Let \(\Omega\) have size \(2r+1\), and let
\(V_0,V_1,\ldots,V_{2r}\) be cyclically indexed \(r\)-subsets with
\(V_i\cap V_{i+1}=\varnothing\). Let \(c_i\) be the unique coordinate
omitted by the edge \(V_iV_{i+1}\):

\[
 V_i\mathbin{\dot\cup}V_{i+1}=\Omega\setminus\{c_i\}. \tag{1.3b}
\]

If \(c_0,c_1,\ldots,c_{2r}\) are all distinct, then they enumerate
\(\Omega\). Define the derived cyclic coordinate order

\[
 \pi=(c_1,c_3,\ldots,c_{2r-1},c_0,c_2,\ldots,c_{2r}), \tag{1.3c}
\]

which reads the omitted-coordinate indices in steps of two modulo
\(2r+1\). Then exactly

\[
 V_i=\{c_{i+1},c_{i+3},\ldots,c_{i+2r-1}\},          \tag{1.3d}
\]

with subscripts modulo \(2r+1\). These are precisely the ordinary
length-\(r\) cyclic intervals of \(\pi\), so the cycle is its literal
wreath.

#### Proof

Fix \(j\). Coordinate \(c_j\) is absent from both \(V_j\) and
\(V_{j+1}\). On the next edge, whose omitted coordinate is the distinct
\(c_{j+1}\), it must belong to \(V_{j+2}\). More generally, on every edge
indexed \(k\ne j\), equation (1.3b) puts \(c_j\) in exactly one of
\(V_k,V_{k+1}\); hence its membership alternates until returning to the
edge indexed \(j\).
Thus

\[
 c_j\in V_i
 \quad\Longleftrightarrow\quad
 i-j\pmod{2r+1}\in\{2,4,\ldots,2r\}.
\]

Solving this condition for the coordinates lying in fixed \(V_i\) gives
(1.3d). Consecutive entries of \(\pi\) advance the \(c\)-subscript by two,
so every set in (1.3d) is an ordinary block of \(r\) consecutive entries
of \(\pi\); as \(i\) varies, all \(2r+1\) starting positions occur.
\(\square\)

Fix a prescribed upward edge assignment

\[
                         a:L\longrightarrow\mathcal Y,
                         \qquad x\subset a(x).           \tag{1.4}
\]

### Definition 1.2 (balanced)

The first matching \(a\) is **balanced** when it is bijective. Equivalently,

\[
 d_a(x)=1\quad(x\in L),\qquad
 d_a(Y)=1\quad(Y\in\mathcal Y).                         \tag{1.5}
\]

The second equality is an exact \(Y\)-resource condition. Prescribing one
edge out of every \(x\) does not imply it. Only after (1.5) is imposed is
the assignment in (1.4) a matching on both shores.

For \(x\in L\), define its allowed exits

\[
 A_a(x)=
 \{z\in R:z\subset a(x),\ z\ne x,\ 
               \text{and the incidence is allowed}\}.  \tag{1.6}
\]

The exclusion \(z=x\) applies when \(x\in I\). It prevents selecting the
same undirected incidence \(x-a(x)\) in both matchings, which would create
an immediate backtrack and would give degree one rather than degree two in
the simple inclusion graph. Since \(x\) and every allowed \(z\ne x\) are
distinct \(r\)-subsets of the same \((r+1)\)-set \(a(x)\), they differ by
exactly one deletion and one insertion; every contracted edge is therefore
a genuine Johnson edge.

Let

\[
 H_a\subseteq L\times R,\qquad
 xz\in E(H_a)\Longleftrightarrow z\in A_a(x).           \tag{1.7}
\]

A second matching is now exactly a perfect matching

\[
                         \sigma:L\longrightarrow R
                         \quad\text{in }H_a.             \tag{1.8}
\]

It installs the down incidence \(a(x)-\sigma(x)\). Since \(a\) and
\(\sigma\) are bijections, every \(Y\)-vertex and every member of \(R\)
is used once.

## 2. The strongest ordinary Hall and LP-dual theorem

For \(S\subseteq L\) and \(z\in R\), write

\[
 d_S(z)=|\{x\in S:z\in A_a(x)\}|.
\]

### Theorem 2.1 (prescribed-first matching completion)

For a balanced first matching \(a\), the following are equivalent.

1. There is a simple second perfect matching \(\sigma\) in \(H_a\).
2. For every \(S\subseteq L\),
   \[
                         |N_{H_a}(S)|\ge |S|.           \tag{2.1}
   \]
3. For every \(S\subseteq L\) and \(B\subseteq R\),
   \[
   \boxed{
      |S|\le e_{H_a}(S,R\setminus B)+|B|.}             \tag{2.2}
   \]
4. For every \(S\subseteq L\),
   \[
   \boxed{
      |S|\le
      \sum_{z\in R}\min\{1,d_S(z)\}.}                  \tag{2.3}
   \]
5. For every real weight vector \(w=(w_z)_{z\in R}\),
   \[
   \boxed{
      \sum_{z\in R}w_z
       \ge
      \sum_{x\in L}\min_{z\in A_a(x)}w_z.}             \tag{2.4}
\]

In (2.4) we use \(\min\varnothing=+\infty\). Thus an empty exit set makes
the condition fail, as it should.

The exact matching deficiency is

\[
\boxed{
 \delta(H_a)=
 \max_{S\subseteq L}\bigl(|S|-|N_{H_a}(S)|\bigr)_+.}   \tag{2.5}
\]

#### Proof

Use the network

\[
                 s\longrightarrow L\longrightarrow R
                   \longrightarrow t
\]

with unit capacities. A cut whose source side contains \(S\subseteq L\)
and \(B\subseteq R\) has capacity

\[
             |L\setminus S|+e_{H_a}(S,R\setminus B)+|B|. \tag{2.6}
\]

Requiring every cut to have capacity at least \(|L|\) is exactly (2.2).
Minimizing independently over membership of each \(z\) in \(B\) gives
(2.3), whose right side is \(|N(S)|\). Thus (2.1)--(2.3) are equivalent,
and max-flow/min-cut gives (1). Integral capacities give an integral
matching. The same cut calculation with a maximum flow of value
\(|L|-\delta\) gives (2.5).

For (2.4), necessity follows from any perfect matching:

\[
 \sum_{z\in R}w_z
 =\sum_{x\in L}w_{\sigma(x)}
 \ge\sum_{x\in L}\min_{z\in A_a(x)}w_z.
\]

Conversely, if Hall fails at \(S\subseteq L\), take
\(w_z=1\) on \(N(S)\) and \(w_z=0\) off \(N(S)\). Every \(x\in S\) then
has minimum weight one, while all other minima are nonnegative. Hence the
right side of (2.4) is at least \(|S|>|N(S)|\), which is its left side.
Thus (2.4) fails. This is the explicit Farkas separation. The bipartite
assignment matrix is totally unimodular, so fractional feasibility is
equivalent to an integral perfect matching. \(\square\)

This is the strongest conclusion ordinary Hall can provide: it completes
both matching degree ledgers and uses every \(Y\)-resource once. It says
nothing about which sink is joined to which root.

### Corollary 2.2 (min-cost LP dual, conditional on feasibility)

If the equivalent Hall conditions of Theorem 2.1 hold, then for arbitrary
real costs \(c_{xz}\) on \(H_a\), the minimum-cost second matching equals

\[
\min_{\substack{q\ge0\\
 \sum_zq_{xz}=1\\
 \sum_xq_{xz}=1}}
 \sum_{xz\in E(H_a)}c_{xz}q_{xz}
=
\max_{\substack{\alpha_x+\beta_z\le c_{xz}\\xz\in E(H_a)}}
 \left(\sum_{x\in L}\alpha_x+\sum_{z\in R}\beta_z\right). \tag{2.7}
\]

The primal optimum is attained by an integral perfect matching, and the
dual optimum is attained. No integrality of the dual potentials is asserted
for arbitrary real costs. Thus any additive objective on the second edges
can be optimized exactly after \(M^\uparrow\) is fixed and Hall feasibility
has been certified. Nonadditive monodromy is not represented by this dual.

### Theorem 2.3 (general capacitated degree completion)

Let lower demands \(b_x\) and resource capacities \(c_z\) be nonnegative
integers with

\[
                         \sum_xb_x=\sum_zc_z.
\]

An allowed simple bipartite support \(H\subseteq L\times R\) contains an
integral subgraph with degrees \(b_x,c_z\) if and only if, for every
\(S\subseteq L\) and \(B\subseteq R\),

\[
\boxed{
 b(S)\le e_H(S,R\setminus B)+c(B).}                    \tag{2.8}
\]

Equivalently, for every \(S\subseteq L\),

\[
\boxed{
 b(S)\le\sum_{z\in R}\min\{c_z,d_S(z)\}.}              \tag{2.9}
\]

The exact flow deficiency is

\[
 \max_{S,B}
 \bigl(b(S)-e_H(S,R\setminus B)-c(B)\bigr)_+.          \tag{2.10}
\]

#### Proof

Give \(s\to x\) capacity \(b_x\), every allowed \(xz\) capacity one, and
\(z\to t\) capacity \(c_z\). The cut calculation is (2.8); minimization
over \(B\) gives (2.9), and integral flow proves sufficiency. \(\square\)

If a prescribed first-edge family has upper loads \(0\le a_Y\le2\), the
undirected degree problem has residual capacities \(2-a_Y\) and, after
transposing/relabeling the shores so that the capacity resources are the
\(Y\)-vertices, falls under Theorem 2.3. But it is not a completion into two
alternating perfect matchings: a \(Y\) with \(a_Y=2\) has no down edge,
while one with \(a_Y=0\) needs two. Hence \(Y\)-balance (1.5) is a separate
prerequisite, not a consequence of Hall on lower vertices. If some
\(a_Y>2\), even the undirected degree ledger is already impossible.

### Proposition 2.4 (exact clean-support degrees and Catalan-shadow Hall)

Let \(r\ge1\), let \(a:L\to\mathcal Y\) be balanced (hence bijective), and
assume that the support is the full clean support: the only forbidden exits
are the port exclusions \(z\notin R\) and the immediate backtrack \(z=x\).
Relabel the left shore through \(a\), so its vertices are
\(Y\in\mathcal Y\), with owner \(x_Y=a^{-1}(Y)\). Put

\[
 \rho(Y)=|\{P\in\mathcal D:P\subset Y\}|.             \tag{2.11}
\]

Then the exact row and column degrees are

\[
 d^+(Y)=r+1-\rho(Y)-\mathbf 1_{\{x_Y\in I\}},         \tag{2.12}
\]

and

\[
 d^-(z)=
 \begin{cases}
 r-1,&z\in I,\\
 r,&z\in\overline{\mathcal D}.
 \end{cases}                                          \tag{2.13}
\]

In particular the exact edge ledger is

\[
 \sum_{Y\in\mathcal Y}d^+(Y)
 =\sum_{z\in R}d^-(z)
 =(r^2-r+1)N.                                         \tag{2.13a}
\]

For \(U\subseteq\mathcal Y\), define its lower shadow and its private
deleted-owner count by

\[
\begin{aligned}
 \partial^-U
   &=\{z\in\mathcal X:z\subset Y\text{ for some }Y\in U\},\\
 d_U(z)&=|\{Y\in U:z\subset Y\}|,\\
 \pi_a(U)
   &=|\{z\in I:a(z)\in U,\ d_U(z)=1\}|.              \tag{2.14}
\end{aligned}
\]

The fixed first matching has a degree-feasible second matching if and only
if the following exact Catalan-shadow inequalities hold for every
\(U\subseteq\mathcal Y\):

\[
\boxed{
 |\partial^-U|-|\mathcal D\cap\partial^-U|-\pi_a(U)
    \ge |U|.}                                         \tag{2.15}
\]

#### Proof

Before the backtrack deletion, row \(Y\) sees every non-Dyck \(r\)-subset
of \(Y\), of which there are \(r+1-\rho(Y)\). If its owner is internal,
the owner is one of these resources and its edge is deleted; if its owner
is a root, that owner was already absent from \(R\). This proves (2.12).

Every \(z\in R\) has exactly \(r\) upper supersets in \(\mathcal Y\). If
\(z\in I\), precisely the edge from its own assigned upper set \(a(z)\) is
deleted. If \(z\in\overline{\mathcal D}\), it has no owner because it does
not belong to \(L\). This proves (2.13), and summing over
\(|I|=(r-1)N\) internal resources and \(N\) terminals proves (2.13a).

For a row family \(U\), its neighborhood before the backtrack deletions is
\(\partial^-U\setminus\mathcal D\). A resource \(z\) disappears from that
neighborhood after the deletions exactly when \(z\in I\), its assigned edge
\(a(z)z\) lies in the row family, and that edge was its unique incidence
from \(U\), namely when \(a(z)\in U\) and \(d_U(z)=1\). Hence

\[
 |N(U)|=|\partial^-U|-|\mathcal D\cap\partial^-U|-\pi_a(U).
\]

Hall's theorem, after relabeling \(L\) by the bijection \(a\), is exactly
(2.15). \(\square\)

Formula (2.15) is stronger than a degree estimate: it records both the
Catalan port loss and the private edge removed by the prescribed first
matching. It is still an exponential family in general; balance alone
does not supply an uncrossing rule.

### Corollary 2.5 (exact private-owner obstruction and deficiency)

In the full clean support, define the non-Dyck shadow surplus

\[
 s_{\mathcal D}(U)
   =|\partial^-U\setminus\mathcal D|-|U|.             \tag{2.16}
\]

Then a balanced first matching has a degree-feasible second matching if
and only if

\[
\boxed{
                         \pi_a(U)\le s_{\mathcal D}(U)
                         \quad(U\subseteq\mathcal Y).} \tag{2.17}
\]

Moreover its exact matching deficiency is

\[
\boxed{
 \delta(H_a)=max_{U\subseteq\mathcal Y}
       \bigl(\pi_a(U)-s_{\mathcal D}(U)\bigr)_+.}      \tag{2.18}
\]

#### Proof

Under the bijection \(a:L\to\mathcal Y\), every left family is uniquely
\(a^{-1}(U)\). Proposition 2.4 gives

\[
 |U|-|N_{H_a}(a^{-1}(U))|
   =\pi_a(U)-s_{\mathcal D}(U).
\]

Now apply Theorem 2.1 and its exact deficiency formula (2.5). \(\square\)

Thus degree Hall fails precisely when a Catalan upper family has more
private internal owners than its non-Dyck lower-shadow surplus. Endpoint
monodromy remains absent from this scalar obstruction.

## 3. Exact monodromy after the Hall completion

Define the fixed bijection

\[
 \iota:R\longrightarrow L,\qquad
 \iota(z)=
 \begin{cases}
 z,&z\in I,\\
 P,&z=\overline P,\ P\in\mathcal D.
 \end{cases}                                           \tag{3.1}
\]

For a second perfect matching \(\sigma\), put

\[
                              T_\sigma=\iota\circ\sigma
                              \in\operatorname {Sym}(L). \tag{3.2}
\]

After contracting every fixed edge \(x-a(x)\), the selected down edge
becomes a directed Johnson arc

\[
                              x\longrightarrow\sigma(x). \tag{3.3}
\]

Let \(Q_\sigma\) be this arc set on \(\mathcal X\).

### Theorem 3.1 (cycle-monodromy criterion)

The two matchings \(a,\sigma\) form a
\(\mathcal D_r\)-port complement-path factor if and only if

\[
\boxed{\text{every cycle of }T_\sigma
       \text{ contains exactly one member of }\mathcal D.} \tag{3.4}
\]

#### Proof

Follow one cycle of \(T_\sigma\). At an internal state
\(z\in I\), the identification \(\iota(z)=z\) simply continues the
physical directed path. When \(\sigma(x)=\overline P\), the map
\(\iota\) closes the physical sink \(\overline P\) virtually back to its
prescribed root \(P\).

Thus a cycle containing no Dyck root is exactly a portless internal
directed cycle of \(Q_\sigma\). A cycle containing roots
\(P_1,\ldots,P_k\) records \(k\) physical root-to-sink paths whose endpoint
monodromy cyclically permutes those roots. It is correct precisely when
\(k=1\), in which case the physical path runs from \(P\) to
\(\overline P\).

Therefore (3.4) is necessary and sufficient for all physical components
to be the prescribed paths, with no internal cycle. Each Johnson path
\(P\to\overline P\) then has at least \(r\) arcs, while

\[
                         |Q_\sigma|=|L|=rN.
\]

The \(N\) paths use at least \(rN\) arcs, so all have exactly \(r\) arcs
and exhaust \(Q_\sigma\). \(\square\)

The cycle test is finite and exact once \(\sigma\) is known. It is not a
linear Hall condition.

### Theorem 3.2 (exact prescribed-pair cuts)

For \(S\subseteq\mathcal X\), put

\[
\begin{aligned}
 \kappa_{\mathcal D}(S)
 &=\#\{P\in\mathcal D:
      |\{P,\overline P\}\cap S|=1\},\\
 \kappa^+_{\mathcal D}(S)
 &=\#\{P\in\mathcal D:P\in S,\ \overline P\notin S\}.
\end{aligned}                                         \tag{3.5}
\]

Here \(Q_\sigma\cap\delta(S)\) counts selected directed arcs having
endpoints on opposite sides of the cut while ignoring their orientation;
if both opposite arcs occur, they are counted separately.

For a perfect second matching \(\sigma\), each of the following is
equivalent to the port-factor conclusion:

\[
\boxed{
 |Q_\sigma\cap\delta(S)|
     \ge\kappa_{\mathcal D}(S)
 \quad(S\subseteq\mathcal X),}                         \tag{3.6}
\]

or

\[
\boxed{
 |\delta^+_{Q_\sigma}(S)|
     \ge\kappa^+_{\mathcal D}(S)
 \quad(S\subseteq\mathcal X).}                         \tag{3.7}
\]

#### Proof

In a correct factor, every prescribed path whose endpoints are separated
by \(S\) contributes a distinct crossing arc, proving necessity.

Conversely, take the vertex set \(S\) of a directed path component from
\(P\) to \(\overline Q\). It has no outgoing arc. If \(Q\ne P\), then
\(P\in S\) but \(\overline P\notin S\), contradicting (3.7). The
undirected argument with (3.6) is identical. Thus every path has the
correct sink. The edge-count argument in Theorem 3.1 then excludes all
cycles and excess length. \(\square\)

### Theorem 3.3 (exact cut integer program and fractional dual)

For every allowed arc \(xz\in E(H_a)\), let \(q_{xz}\) be its selection
variable. A literal port-factor completion exists if and only if the
following integer system is feasible:

\[
\begin{aligned}
 \sum_{z\in A_a(x)}q_{xz}&=1 &&(x\in L),\\
 \sum_{x:z\in A_a(x)}q_{xz}&=1 &&(z\in R),\\
 \sum_{\substack{x\in S,\ z\notin S\\xz\in E(H_a)}}q_{xz}
   &\ge \kappa^+_{\mathcal D}(S)
       &&(S\subseteq\mathcal X),\\
 q_{xz}&\in\{0,1\}.                                  \tag{3.8}
\end{aligned}
\]

For real arc costs \(c_{xz}\), relax the last line to \(q_{xz}\ge0\).
Whenever this fractional system is feasible, its minimum cost equals

\[
\boxed{
\max
 \left\{
  \sum_{x\in L}\alpha_x+\sum_{z\in R}\beta_z
   +\sum_{S\subseteq\mathcal X}
       \kappa^+_{\mathcal D}(S)\gamma_S:
 \begin{array}{l}
  \alpha_x+\beta_z+
   \displaystyle\sum_{S:x\in S,\ z\notin S}\gamma_S
       \le c_{xz}\quad(xz\in E(H_a)),\\[2mm]
  \gamma_S\ge0,\quad \alpha_x,\beta_z\in\mathbb R
 \end{array}
 \right\}.}                                           \tag{3.9}
\]

#### Proof

The first two lines of (3.8), together with integrality, say exactly that
the selected arcs are a perfect second matching. The third line is (3.7),
so Theorem 3.2 proves the integer equivalence. Formula (3.9) is the ordinary
linear-programming dual: \(\alpha,\beta\) correspond to the two degree
equalities and the nonnegative \(\gamma_S\) to the directed pair-cut lower
bounds. \(\square\)

The fractional relaxation of (3.8), together with its dual (3.9), is the
strongest immediate linear cut certificate supplied by this reduction.
Its primal matrix is no longer a plain bipartite assignment matrix, and no
total-unimodularity or integrality assertion is justified. Thus an optimum
of the fractional relaxation of (3.8), or its dual certificate (3.9), does
not by itself produce an integral monodromy-safe matching.

Consequently

\[
\boxed{\text{ordinary Hall}
\iff\text{degree and }Y\text{-resource completion},}
\]

whereas

\[
\boxed{\text{Hall plus (3.6) or (3.7)}
\iff\text{literal port-path completion}.}
\]

The latter is an exact characterization of integral \(0\)-\(1\) matchings.
No claim is made that adding all pair cuts to the assignment LP preserves
integrality.

## 4. A stronger Ordered-Hall theorem

### Theorem 4.1 (metric Ordered-Hall; no acyclicity hypothesis)

Let \(\vec G\) be a finite simple directed graph with pairwise disjoint
source and terminal sets

\[
 \mathsf S=\{s_1,\ldots,s_N\},\qquad
 \mathsf T=\{t_1,\ldots,t_N\},
\]

such that no arc enters \(\mathsf S\) and no arc leaves \(\mathsf T\).
Form its successor bigraph

\[
 (V(\vec G)\setminus\mathsf T)_L
 \longleftrightarrow
 (V(\vec G)\setminus\mathsf S)_R,                    \tag{4.1}
\]

putting in the edge \(u_Lv_R\) exactly when \(u\to v\) is an allowed arc.
Assume:

1. the successor bigraph satisfies Hall on its left shore (the two shores
   have equal size because \(|\mathsf S|=|\mathsf T|\));
2. the unique perfect matching of the \(\mathsf S\)-to-\(\mathsf T\)
   reachability graph is \(s_i\mapsto t_i\);
3. for integers \(\ell_i\ge0\), every directed
   \(s_i\)-to-\(t_i\) path has length at least \(\ell_i\), where length is
   counted in arcs.

Put

\[
 \Delta=|V(\vec G)|-N-\sum_{i=1}^N\ell_i.             \tag{4.2}
\]

Then \(\Delta\ge0\). Every perfect matching of the successor bigraph
selects \(N\) paths \(P_i:s_i\leadsto t_i\), together with some disjoint
directed cycles \(C_1,\ldots,C_k\), and obeys the exact defect identity

\[
 \boxed{
 \sum_{i=1}^N\bigl(|E(P_i)|-\ell_i\bigr)
    +\sum_{j=1}^k|E(C_j)|=\Delta.}                    \tag{4.3}
\]

In particular, if \(\Delta=0\), the selected arcs form a spanning directed
path cover consisting of the \(N\) paths \(s_i\leadsto t_i\), each of
length exactly \(\ell_i\), and there is no selected directed cycle.

#### Proof

A successor perfect matching gives outdegree one at every nonterminal,
indegree one at every nonsource, no incoming arc at a source, and no
outgoing arc at a terminal. Its weak components are therefore
source-to-terminal paths and directed cycles. (A source trajectory cannot
enter a cycle, because its first repeated vertex would then have two
selected predecessors.) The path components pair all sources bijectively
with all terminals, and that pairing is a perfect matching of the full
reachability graph. Hypothesis 2 makes it \(s_i\mapsto t_i\).

The matching selects exactly \(|V(\vec G)|-N\) arcs, so

\[
 |V(\vec G)|-N
   =\sum_i|E(P_i)|+\sum_j|E(C_j)|.
\]

Subtracting \(\sum_i\ell_i\) proves (4.3), including \(\Delta\ge0\).
When \(\Delta=0\), every nonnegative summand in (4.3) vanishes, proving
the final assertion. \(\square\)

Quantitatively, (4.3) says that at most \(\Delta\) selected arcs lie on
cycle components and that the total path-length excess above the prescribed
endpoint distances is at most \(\Delta\). This is the only defect that the
metric Ordered-Hall step leaves for a near-factor application.

This theorem also applies verbatim after a clean prescribed prefix is
contracted: if the residual successor count equals the sum of the labelled
residual endpoint distances, unique diagonal reachability itself removes
both long paths and residual cycles. A separate acyclicity assumption is
then redundant. In particular, for \(r\ge2\), after prescribing
\(P-U_P-Q_P\) in rank \(r\), the residual middle-level graph has
\((2r-1)N\) vertices, \(N\) labelled source--terminal pairs, and
distance lower bound \(2(r-1)\) per pair; hence

\[
 (2r-1)N-N=2(r-1)N.
\]

So residual successor Hall plus unique diagonal reachability completes
that prefix without any acyclic-support hypothesis as well. This strictly
strengthens the sufficient theorem recorded in
`MATH_ATTACK_S_BALANCED_FIRST_EDGE_COMPLETION_THEOREM_AND_CUT_20260726.md`.

Let \(\vec H_a\) be the full allowed contracted digraph on
\(\mathcal X\), with arcs

\[
                              x\longrightarrow z
                         \quad(z\in A_a(x)).            \tag{4.4}
\]

No arc enters \(\mathcal D\), and no arc leaves
\(\overline{\mathcal D}\). Form the reachability graph

\[
 \mathscr R_a\subseteq
    \mathcal D\times\overline{\mathcal D},              \tag{4.5}
\]

joining \(P\) to \(\overline Q\) when \(\vec H_a\) has a directed path
from the former to the latter.

### Corollary 4.2 (prescribed-first Ordered-Hall)

Assume:

1. \(H_a\) satisfies the Hall conditions of Theorem 2.1; and
2. the unique perfect matching of \(\mathscr R_a\) is
   \[
                              P\longmapsto\overline P.  \tag{4.6}
   \]

Then every second perfect matching of \(H_a\), and in particular at least
one, has union with \(a\) equal to a literal
\(\mathcal D_r\)-port factor.

#### Proof

Apply Theorem 4.1 to \(V=\mathcal X\), sources \(\mathcal D\), terminals
\(\overline{\mathcal D}\), and \(\ell_P=r\). Its successor bigraph is
exactly \(H_a\), and

\[
 |\mathcal X|-N=rN=\sum_{P\in\mathcal D}\ell_P.
\]

Thus Hall gives \(N\) cycle-free Johnson geodesics \(P\to\overline P\).
Along a length-\(r\) Johnson geodesic from \(P\) to
\(\overline P\), each of the \(r\) coordinates of \(P\) is removed exactly
once and each of the \(r\) coordinates of \(\overline P\) is inserted
exactly once. Writing the successive swaps as
\(X_t=X_{t-1}-\{p_t\}+\{q_t\}\), the lifted two-edge segments (1.3a) have
omitted-coordinate sequence

\[
 q_1,p_1,q_2,p_2,\ldots,q_r,p_r,\infty,
\]

where the final \(\infty\) is omitted by the closing edge
\(\overline P--P\). This is a permutation of
\(J\sqcup\{\infty\}\). The derived coordinate order (1.3c) is exactly

\[
 (p_1,p_2,\ldots,p_r,q_1,q_2,\ldots,q_r,\infty).
\]

Lemma 1.1 therefore gives its literal length-\(r\) cyclic-window wreath,
not merely an abstract graph path. \(\square\)

The cyclic coordinate order may depend on \(P\), as permitted in a wreath
factor; no common order across distinct components is asserted.

This improves the earlier acyclic-support Ordered-Hall theorem:
acyclicity is convenient but redundant once unique complement reachability
and the exact Catalan edge count are available.

### Proposition 4.3 (triangular reachability is exact)

Assume all diagonal reachabilities \(P\leadsto\overline P\) are present.
Make a digraph \(K_a\) on \(\mathcal D\) by

\[
 P\longrightarrow Q
 \quad\Longleftrightarrow\quad
 P\leadsto\overline Q,\quad P\ne Q.                   \tag{4.7}
\]

The complement matching is the unique perfect matching of
\(\mathscr R_a\) if and only if \(K_a\) is acyclic. Equivalently, there is
an ordering

\[
                         P_1,\ldots,P_N                \tag{4.8}
\]

such that

\[
 P_i\leadsto\overline P_j,\quad i\ne j
 \quad\Longrightarrow\quad i<j.                       \tag{4.9}
\]

#### Proof

A directed cycle in \(K_a\) replaces the diagonal matching on its roots
by the cyclically shifted matching. Conversely, the symmetric difference
of any second perfect matching with the diagonal matching contains an
alternating cycle, which gives a directed cycle in \(K_a\).

If \(K_a\) is acyclic, a topological ordering gives (4.9). Conversely,
(4.9) forbids a directed cycle. \(\square\)

A particularly checkable sufficient form is

\[
 N_{\mathscr R_a}(P_i)
   \subseteq
 \{\overline P_i,\overline P_{i+1},\ldots,\overline P_N\},
 \qquad
 \overline P_i\in N_{\mathscr R_a}(P_i).               \tag{4.10}
\]

Any perfect matching \(\pi\) in this upper-triangular graph satisfies
\(\pi(i)\ge i\) for every \(i\); summing gives equality everywhere, so
\(\pi=\mathrm{id}\).

### Corollary 4.4 (edgewise monotone-order certificate)

Suppose the roots are ordered \(P_1,\ldots,P_N\), every diagonal path
\(P_i\leadsto\overline P_i\) exists in \(\vec H_a\), and there is a map

\[
 h:\mathcal X\longrightarrow[N]                     \tag{4.11}
\]

such that

\[
 h(P_i)=h(\overline P_i)=i,qquad
 h(x)\le h(z)quad\text{for every allowed arc }x\to z. \tag{4.12}
\]

Then \(\mathscr R_a\) has the diagonal complement matching as its unique
perfect matching. Consequently, if \(H_a\) also satisfies Hall, every
second perfect matching gives a literal port factor.

#### Proof

If \(P_i\leadsto\overline P_j\), monotonicity along the path gives
\(i=h(P_i)\le h(\overline P_j)=j\). Thus every off-diagonal reachability
has \(i<j\), while all diagonal reachabilities are present. This is
(4.9), so Proposition 4.3 and Corollary 4.2 apply. \(\square\)

The potential is only sufficient, but it is locally checkable on allowed
arcs; no selected matching or global cycle enumeration is needed once
(4.12) is verified.

## 5. Exact interval and cyclic-interval Hall

The Hall family in Theorem 2.1 is exponential in general. It collapses to
interval cuts under a genuine convexity hypothesis.

### Theorem 5.1 (trapped-interval Hall)

Let jobs \(q\in Q\) have nonempty allowed resource sets \(I_q\), each an
interval in one common linear order

\[
                         1<2<\cdots<M.
\]

Let resource \(j\) have integer capacity \(c_j\), with

\[
                         |Q|\le\sum_{j=1}^Mc_j.
\]

There is an assignment of every job to an allowed resource, respecting
the capacities, if and only if for every interval \([a,b]\),

\[
\boxed{
 \#\{q:I_q\subseteq[a,b]\}
       \le\sum_{j=a}^bc_j.}                            \tag{5.1}
\]

#### Proof

Necessity is immediate. For sufficiency, suppose Hall fails for a job
family \(S\). Its allowed union

\[
                         U=\bigcup_{q\in S}I_q
\]

is a disjoint union of maximal resource intervals
\(J_1,\ldots,J_t\). Since each \(I_q\) is connected, it lies wholly in one
\(J_i\). Partition \(S\) accordingly as \(S_1,\ldots,S_t\). If every
\(|S_i|\) were at most the capacity of \(J_i\), their sum would show that
\(S\) is not deficient. Hence one \(J_i\) violates (5.1). \(\square\)

With unit capacities, (5.1) is

\[
                 \#\{q:I_q\subseteq[a,b]\}\le b-a+1.  \tag{5.2}
\]

### Corollary 5.2 (cyclic intervals)

The same theorem holds for resources cyclically ordered and every \(I_q\)
a cyclic interval, provided total demand does not exceed total capacity.
It is enough to check every proper cyclic interval and the whole circle.

#### Proof

If a deficient union is proper, decompose it into maximal cyclic interval
components and repeat the proof of Theorem 5.1. If it is the whole circle,
total demand not exceeding total capacity prevents deficiency. \(\square\)

Thus on \(M\) resources the exact certificate has
\(M(M+1)/2\) nonempty linear cuts, or at most
\(M(M-1)+1\) nonempty cyclic cuts including the whole circle.

### Corollary 5.3 (the transposed Catalan interval inequalities)

For a balanced first matching \(a\), order the \(Y\)-resources as
\(Y_1,\ldots,Y_{rN}\), thereby ordering their owners
\(a^{-1}(Y_1),\ldots,a^{-1}(Y_{rN})\). For \(z\in R\), put

\[
 B_a(z)=\{Y\in\mathcal Y:z\in A_a(a^{-1}(Y))\}.       \tag{5.3}
\]

If every \(B_a(z)\) is a nonempty interval in this common order, then a
second perfect matching exists if and only if, for every interval
\([i,j]\),

\[
\boxed{
 |\{z\in R:B_a(z)\subseteq\{Y_i,\ldots,Y_j\}\}|
       \le j-i+1.}                                    \tag{5.4}
\]

The identical statement holds for a cyclic order and cyclic intervals.
There one checks every proper cyclic interval and the whole circle (the
whole-circle inequality is automatic equality in this balanced unit-capacity
setting).

In the full clean support of Proposition 2.4,

\[
 B_a(z)=
 \begin{cases}
  \{Y\supset z\}\setminus\{a(z)\},&z\in I,\\
  \{Y\supset z\},&z\in\overline{\mathcal D},
 \end{cases}                                          \tag{5.5}
\]

so (5.4) is a literal, checkable Catalan-star interval family.
Formula (5.5) describes the stars exactly; it does not assert that a common
linear or cyclic interval order exists.

For any \(U\subseteq\mathcal Y\), put
\(T_a(U)=\{z\in R:B_a(z)\subseteq U\}\). Since

\[
 T_a(U)=R\setminus N_{H_a}(a^{-1}(\mathcal Y\setminus U)),
\]

the full-clean shadow formula gives the exact identity

\[
\boxed{
 |T_a(U)|-|U|
   =\pi_a(\mathcal Y\setminus U)
      -s_{\mathcal D}(\mathcal Y\setminus U).}        \tag{5.6}
\]

Thus each trapped interval inequality (5.4) is exactly a
private-owner/Catalan-shadow inequality for the complementary row family,
not merely a degree estimate.

#### Proof

Transpose the second-matching bigraph: jobs are now \(z\in R\), resources
are the owners indexed by \(Y\), and the allowed resource interval of job
\(z\) is \(B_a(z)\). Apply Theorem 5.1 or Corollary 5.2 with unit
capacities. Formula (5.5) is exactly the column description in the proof of
Proposition 2.4. Finally, with \(V=\mathcal Y\setminus U\) and
\(|R|=|\mathcal Y|\),

\[
 |T_a(U)|-|U|=|V|-|N_{H_a}(a^{-1}(V))|,
\]

and Corollary 2.5 proves (5.6). \(\square\)

### Theorem 5.4 (Ordered-Interval-Hall port completion)

Suppose a balanced prescribed first matching \(a\) has these properties.

1. The degree Hall condition has one of the following two interval
   certificates:
   
   (a) every exit set \(A_a(x)\) is nonempty and is an interval in one
   linear or cyclic order of \(R\), and all corresponding inequalities
   (5.1) hold with unit capacities; or
   
   (b) every predecessor set \(B_a(z)\) is nonempty and is an interval in
   one linear or cyclic order of \(\mathcal Y\), and all corresponding
   inequalities (5.4) hold (equivalently, in the full clean support, the
   complementary Catalan-shadow inequalities given by (5.6) hold).
2. The root-to-complement reachability graph is triangular as in
   (4.10), after a simultaneous ordering of the roots; it is enough to
   supply the edgewise monotone potential (4.11)--(4.12).

Then \(a\) extends to a literal \(\mathcal D_r\)-port factor.

#### Proof

In case 1(a), Theorem 5.1 or Corollary 5.2 gives the second perfect
matching. In case 1(b), Corollary 5.3 gives it. Condition 2 gives unique
diagonal reachability by Proposition 4.3, and Corollary 4.2 completes the
factor. \(\square\)

This is the desired checkable Ordered-Hall theorem. Its interval
hypothesis must be proved for the proposed Catalan support; it is not a
formal consequence of balance.

## 6. The root-first problem and Catalan interval cuts

Suppose only the root-first edges are prescribed:

\[
 \eta:\mathcal D\longrightarrow\mathcal Y,\qquad
 P\subset\eta(P),
                                                        \tag{6.1}
\]

and assume \(\eta\) is injective. Put

\[
                         E=\eta(\mathcal D).            \tag{6.2}
\]

To extend these edges to a balanced complete upward matching, one must
match

\[
 I=\mathcal X\setminus
       (\mathcal D\cup\overline{\mathcal D})
 \quad\text{to}\quad
 \mathcal Y\setminus E.                                \tag{6.3}
\]

Both shores have size \((r-1)N\).

### Theorem 6.1 (exact \(Y\)-resource extension criterion)

The root-first matching extends to a complete balanced \(M^\uparrow\) if
and only if, for every \(A\subseteq I\),

\[
\boxed{
 |\partial^+A\setminus E|
   =|\partial^+A|-|E\cap\partial^+A|
   \ge |A|.}                                           \tag{6.4}
\]

Equivalently,

\[
\boxed{
 |E\cap\partial^+A|
   \le|\partial^+A|-|A|.}                              \tag{6.5}
\]

The exact number of internal owners left unmatched by the best extension
is

\[
\boxed{
 \delta_Y(E)=\max_{A\subseteq I}
 \bigl(|A|+|E\cap\partial^+A|-|\partial^+A|\bigr)_+.} \tag{6.5a}
\]

#### Proof

This is Hall's theorem in the residual inclusion graph
\(I\leftrightarrow\mathcal Y\setminus E\). Its standard exact deficiency
formula is
\(\max_A(|A|-|\partial^+A\setminus E|)_+\), which is (6.5a).
\(\square\)

Balance of the inserted-coordinate counts of the root edges does not
determine \(|E\cap\partial^+A|\) and therefore does not imply (6.5).
This is the exact first \(Y\)-resource obstruction.

### Proposition 6.2 (sharp insertion balance does not imply
\(Y\)-balance)

At \(r=3\), prescribe the root-first edges

\[
\begin{array}{c|c|c}
P&\eta(P)&\text{inserted coordinate}\\ \hline
123&1234&4\\
124&1234&3\\
125&1256&6\\
134&1345&5\\
135&1235&2.
\end{array}                                           \tag{6.6}
\]

The insertion histogram uses each coordinate \(2,3,4,5,6\) exactly once
and coordinate \(1\) zero times, so it is as evenly spread as possible.
Nevertheless \(1234\) is used twice. Thus \(\eta\) is not injective and
cannot extend to a balanced complete first matching.

#### Proof

Every displayed upper set contains its root, so all five incidences are
literal. The histogram and repeated resource are read directly from the
table. Any complete first matching uses every \(Y\)-resource at most once,
so no extension is possible. \(\square\)

There is a natural checkable Catalan subfamily. Let

\[
 L_t=f^t(\mathcal D),\qquad1\le t\le r-1,              \tag{6.7}
\]

be the internal canonical Chung--Feller layers, and order the roots as
\(P_1,\ldots,P_N\). For intervals \(I_t\subseteq[N]\), put

\[
 A(\mathbf I)=
 \bigcup_{t=1}^{r-1}
 \{f^t(P_i):i\in I_t\}.                                \tag{6.8}
\]

The layers are disjoint, so (6.5) gives the necessary Catalan interval
inequalities

\[
\boxed{
 |E\cap\partial^+A(\mathbf I)|
 \le|\partial^+A(\mathbf I)|
      -\sum_{t=1}^{r-1}|I_t|.}                         \tag{6.9}
\]

Single-layer intervals give \(O(rN^2)\) explicitly checkable inequalities.
Using one common interval in every layer gives another \(O(N^2)\) family.
In the lexicographic Dyck order, recursive Dyck prefix cylinders are
intervals and may be substituted for arbitrary intervals. A fixed
nonnegative Dyck prefix of length \(\ell\) and terminal height \(h\) has,
with \(t=2r-\ell\), exactly

\[
 \binom{t}{(t-h)/2}-\binom{t}{(t-h)/2-1}              \tag{6.10}
\]

completions when \(t\equiv h\pmod2\), and zero otherwise (with the usual
convention that out-of-range binomial coefficients vanish).
Indeed, an unrestricted suffix has \((t-h)/2\) up-steps, and reflection at
the first visit to height \(-1\) counts the bad suffixes by the second
binomial coefficient.
Product-of-Catalan counts apply only when a cylinder
decomposes into independent complete Dyck blocks and free Dyck suffixes.

Equation (6.9) is necessary. No uncrossing theorem presently makes it
sufficient for arbitrary Catalan supports.

## 7. Why Catalan interval cuts do not suffice automatically

### Proposition 7.1 (no interval orientation for any full clean
\(r=3\) residual graph)

Let \(r=3\), and let \(a:L\to\mathcal Y\) be any balanced first matching
with the full clean residual support of Proposition 2.4. Then neither of
the following is possible:

1. a linear or cyclic order of \(R\) in which every row exit menu
   \(A_a(x)\) is an interval;
2. a linear or cyclic order of \(\mathcal Y\) in which every predecessor
   menu \(B_a(z)\) is an interval.

#### Proof

At \(r=3\),

\[
 \mathcal D=\{123,124,125,134,135\},\qquad
 \overline{\mathcal D}=\{456,356,346,256,246\}.       \tag{7.1}
\]

Write \(x_Y=a^{-1}(Y)\). The upper set \(2456\) has three terminal facets
\(456,256,246\) and the unique \(L\)-facet \(245\); hence balance and
incidence force \(x_{2456}=245\). Similarly \(x_{3456}=345\). The upper
set \(1456\) has terminal facet \(456\) and three internal facets
\(145,146,156\), so its owner is one of those three. Consequently its
three relevant row menus are

\[
\begin{aligned}
 A_a(x_{2456})&=\{456,256,246\},\\
 A_a(x_{3456})&=\{456,356,346\},\\
 A_a(x_{1456})&=\{456\}\cup
   (\{145,146,156\}\setminus\{x_{1456}\}).           \tag{7.2}
\end{aligned}
\]

They are three triples with common resource \(456\) and six other
pairwise distinct resources.

For the transposed orientation, terminal resources have no owners, so
(5.5) gives

\[
\begin{aligned}
 B_a(456)&=\{1456,2456,3456\},\\
 B_a(256)&=\{1256,2356,2456\},\\
 B_a(246)&=\{1246,2346,2456\}.                       \tag{7.3}
\end{aligned}
\]

These again are three triples with one common point, now \(2456\), and
six other pairwise distinct points; they are independent of \(a\).

Finally, three length-three intervals containing one common position lie
inside the five positions at cyclic/linear distance at most two from that
position. They can therefore contain at most four other distinct points,
whereas either display requires six. This contradiction proves both
claims, linearly and cyclically. \(\square\)

Nor can one repair convexity by ordering the roots instead.

### Proposition 7.2 (no convex Catalan root order)

For \(r=3\), write

\[
 A=123,\quad B=124,\quad C=125,\quad D=134,\quad E=135.
\]

The root neighborhoods of the four \(Y\)-vertices
\(1234,1235,1245,1345\) are

\[
                     \{A,B,D\},\quad\{A,C,E\},
                     \quad\{B,C\},\quad\{D,E\}.        \tag{7.4}
\]

There is no linear or cyclic order of \(A,B,C,D,E\) in which all four sets
are intervals (respectively cyclic intervals).

#### Proof

The first two three-sets intersect only in \(A\). If both are length-three
intervals in an order of five points, they must be the first three and
last three positions, meeting at the middle position occupied by \(A\).
Thus \(B,D\) lie on one side of \(A\), while \(C,E\) lie on the other.
The pair \(\{B,C\}\) cannot then be adjacent, contradicting its being an
interval. For a cyclic order, at most one of the two cross-side pairs
\(\{B,C\}\) and \(\{D,E\}\) can use the single wraparound adjacency, so
the same contradiction holds. \(\square\)

There is also a direct failure of consecutive root Hall cuts.

### Proposition 7.3 (all consecutive cuts pass but Hall fails)

In the standard order \(A,B,C,D,E\), restrict the legal root-first
\(Y\)-menus to

\[
\begin{aligned}
 A&\to1235,\\
 B&\to\{1245,1246\},\\
 C&\to1235,\\
 D&\to1346,\\
 E&\to1356.
\end{aligned}                                         \tag{7.5}
\]

Every consecutive root interval has at least its cardinality of
neighbors, but

\[
                              N(\{A,C\})=\{1235\}.      \tag{7.6}
\]

Hence Hall fails.

#### Proof

Singletons pass. For consecutive pairs the neighbor-set sizes are
\(3,3,2,2\). The consecutive triples have neighbor sets

\[
\begin{aligned}
 N(ABC)&=\{1235,1245,1246\},\\
 N(BCD)&=\{1235,1245,1246,1346\},\\
 N(CDE)&=\{1235,1346,1356\}.
\end{aligned}
\]

The two consecutive four-sets have four and five neighbors, and the whole
order has five. Thus every consecutive cut passes. Equation (7.6) is a
deficit-one nonconsecutive cut. Every displayed edge is a literal
inclusion edge. \(\square\)

This particular deficit example concerns general Catalan menus. It does
not show that consecutive root cuts fail for the narrower support obtained
by deleting one specially balanced first matching from the full Boolean
incidence graph. It does prove that standard root intervals alone cannot be
promoted to a general sufficiency theorem. Proposition 7.1 separately
rules out genuine row/column interval convexity of that full-clean residual
support at \(r=3\).

## 8. Hall does not imply monodromy, even with an acyclic selected support

At \(r=3\), consider the following contracted Johnson paths, where every
arc is labelled by its unique selected \(Y\)-resource:

\[
\begin{array}{c|l}
123&
123\xrightarrow{1236}136\xrightarrow{1346}146
\xrightarrow{1246}126\xrightarrow{1256}156
\xrightarrow{1456}456\\
124&
124\xrightarrow{1234}234\xrightarrow{2346}236
\xrightarrow{2356}256\\
125&
125\xrightarrow{1235}235\xrightarrow{2345}345
\xrightarrow{3456}346\\
135&
135\xrightarrow{1356}356\\
134&
134\xrightarrow{1345}145\xrightarrow{1245}245
\xrightarrow{2456}246.
\end{array}                                           \tag{8.1}
\]

The fifteen displayed source states are exactly \(L\), the fifteen labels
are every member of \(\mathcal Y\), and the fifteen target states are
exactly \(R\). Thus the predecessor incidences define a balanced prescribed
first matching \(a\), and the successor incidences define a perfect second
matching. Hall holds, even if the allowed exit support is restricted to
these selected edges. The selected directed graph is a union of paths and
is acyclic.

Nevertheless the endpoint map is

\[
\begin{aligned}
 123&\longmapsto\overline{123},&
 125&\longmapsto\overline{125},\\
 124&\longmapsto\overline{134},&
 134&\longmapsto\overline{135},&
 135&\longmapsto\overline{124}.
\end{aligned}                                         \tag{8.2}
\]

The last three roots have a nontrivial three-cycle monodromy. Therefore

\[
\boxed{
\text{balanced first matching}
+\text{ ordinary Hall}
+\text{ acyclic selected support}
\not\Longrightarrow
\text{complement monodromy}.}                         \tag{8.3}
\]

The unique/triangular reachability hypothesis in Corollary 4.2 is genuinely
additional. This is an exact counterexample in the allowed-support model
of (1.6). It does not assert that the obstruction survives after every
unused Boolean incidence is restored; in that larger graph a different
second matching may exist.

## 9. Precise proved and open boundary

The following statements are proved.

1. A balanced complete first matching reduces the entire degree completion
   to one integral assignment LP, with exact Hall, cut, weighted-dual,
   deficiency, and min-cost formulations. In the full clean support the
   exact degrees are (2.12)--(2.13), and Hall is exactly the
   Catalan-shadow/private-owner family (2.15), with exact deficiency
   (2.18).
2. The endpoint condition is exactly the cycle rule (3.4), equivalently
   the prescribed-pair cuts (3.6)--(3.7). These yield the exact integer
   formulation (3.8) and the fractional cut dual (3.9), without a proved
   integrality theorem for the strengthened relaxation.
3. Metric Ordered-Hall gives the exact defect identity (4.3). At zero
   defect, Hall plus unique diagonal reachability suffices without a
   separate acyclicity assumption, both for a complete prescribed first
   matching and for the clean prescribed-prefix residual problem. The
   edgewise monotone potential (4.11)--(4.12) is a local certificate for
   the required triangular reachability.
4. Under an independently verified interval or cyclic-interval
   representation on either shore, the trapped inequalities (5.1) or the
   transposed Catalan-star inequalities (5.4) are necessary and sufficient
   for the second matching.
5. A root-first prescription has the exact \(Y\)-resource extension cuts
   (6.4)--(6.5) and deficiency (6.5a). Proposition 6.2 gives a sharply
   balanced insertion histogram which nevertheless repeats a \(Y\)-resource.
6. At \(r=3\), Proposition 7.1 rules out both row- and column-interval
   representations for every balanced full-clean residual graph \(H_a\).
   Proposition 7.2 gives a separate root-incidence nonconvexity, and
   consecutive root intervals do not detect every Hall deficit in general
   literal Catalan menus. The obstruction is rank-specific; it does not
   rule out a structured interval representation at growing \(r\).
7. In the allowed-support model, balanced Hall completion and even acyclic
   selected paths do not imply complement monodromy.

What remains unproved is the constructive input needed for coefficient
one: a profile-changing balanced \(M^\uparrow\) for which either the full
Hall family is verified or the residual exits admit a genuine interval
model, and whose root reachability is triangular. Balance alone proves
none of these properties.

No coefficient-one conclusion follows from the present theorem.
