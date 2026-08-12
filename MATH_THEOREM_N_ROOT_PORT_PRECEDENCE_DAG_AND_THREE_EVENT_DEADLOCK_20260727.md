# Root-port packet precedence: the exact DAG criterion, cycle cuts, and a three-event owner-feasible deadlock

Date: 2026-07-27

Method: pure mathematics. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Let

\[
 n=2m,\qquad M=m+H,\qquad
 \mathcal U=\binom{[n]}M,\qquad N=|\mathcal U|.
\]

An oriented root-port packet with core \(C\in\binom{[n]}{M-2}\)
and distinct \(x,y,a\notin C\) has the three local arcs

\[
\begin{array}{rcl}
C+xy&:&x\longrightarrow y,\\
C+ya&:&y\longrightarrow a,\\
C+ax&:&a\longrightarrow x.
\end{array}
\tag{0.1}
\]

This note proves four exact facts.

1. For a signed-flag matching, chronological realizability is exactly a
   local one-trail condition plus acyclicity of one explicitly defined
   packet-precedence digraph. With prescribed initial roots there is no
   further ordering freedom.
2. If a local component is a directed cycle, one must choose a root and
   omit its wrap precedence edge. Thus the uncut union of all local
   successor arcs is not the correct precedence graph.
3. Every packet merely permutes its three lower predecessor owners.
   Hence the complete predecessor-load vector, including injectivity, is
   invariant at every prefix of any legal schedule.
4. Local trails and a feasible predecessor matching do **not** imply
   acyclicity. An explicit three-packet, six-top configuration has six
   distinct initial predecessor owners but forces

   \[
                      e_1\prec e_2\prec e_3\prec e_1.
   \tag{0.2}
   \]

The exact surviving deterministic gate is therefore a context-decorated
selection whose precedence digraph has feedback number \(o(N)\), followed
by a proof that the retained local components are long. Neither
Pippenger--Spencer flag matching nor point-margin Euler balance supplies
this.

## 1. Local port graphs

Let \(\mathcal E\) be a collection of oriented packets. Call
\(\mathcal E\) **flag-simple** if no signed flag \((U,z)^+\) and no signed
flag \((U,z)^-\) occurs in two packets. Equivalently, \(\mathcal E\) is a
matching in the six-uniform signed root-port flag hypergraph.

For a top \(U\in\mathcal U\), define \(G_U(\mathcal E)\) to be the
directed graph on the labels of \(U\) having one event-labelled arc

\[
                         t_U(e)\longrightarrow h_U(e)
\tag{1.1}
\]

for every packet \(e\) incident with \(U\). Flag-simplicity gives

\[
                         d^+_{G_U}(z),d^-_{G_U}(z)\le 1.
\tag{1.2}
\]

Consequently every nontrivial weak component of \(G_U\) is a directed
path or a directed cycle.

Fix an initial root choice

\[
                    r_0(U)\in U\qquad(U\in\mathcal U).
\tag{1.3}
\]

The local family at \(U\) is **root-traversable** if either it is empty,
or all its arcs form one component and:

* in the path case, \(r_0(U)\) is the initial vertex; or
* in the cycle case, \(r_0(U)\) is a vertex of the cycle.

In either nonempty case, iteration from \(r_0(U)\) gives a unique linear
list

\[
                  e_{U,1},e_{U,2},\ldots,e_{U,d_U}.
\tag{1.4}
\]

For a cycle, (1.4) traverses every arc once and stops upon returning to
\(r_0(U)\); the wrap relation \(e_{U,d_U}\prec e_{U,1}\) is not imposed.

### Definition 1.1 (rooted packet-precedence digraph)

The digraph \(D(\mathcal E,r_0)\) has vertex set \(\mathcal E\), and for
every top \(U\) it contains the precedence arcs

\[
                 e_{U,i}\longrightarrow e_{U,i+1}
                 \qquad(1\le i<d_U).
\tag{1.5}
\]

Parallel copies of the same precedence relation are harmless and may be
identified.

## 2. Exact topological-schedule theorem

### Theorem 2.1 (root-port chronology criterion)

Let \(\mathcal E\) be flag-simple and let \(r_0\) be prescribed. There is
a chronological execution of every packet of \(\mathcal E\), exactly
once, starting from \(r_0\), if and only if

1. \(G_U(\mathcal E)\) is root-traversable for every \(U\); and
2. \(D(\mathcal E,r_0)\) is acyclic.

When these conditions hold, every topological ordering of
\(D(\mathcal E,r_0)\) is a legal chronological execution.

#### Proof

Suppose first that a legal execution exists. Restrict its event order to
the packets incident with one top \(U\). Immediately before each such
packet, the current root must be its tail; immediately afterwards it is
its head. Thus consecutive incident packets concatenate, and all incident
arcs form one directed trail from \(r_0(U)\). By (1.2), that trail is one
path or one cycle and its linear order is exactly (1.4). The global event
order respects every relation (1.5), so the precedence digraph is
acyclic.

Conversely, take a topological ordering of \(D(\mathcal E,r_0)\). For a
fixed top \(U\), its restriction is necessarily (1.4). Hence, when
\(e_{U,i}\) is reached, precisely the preceding \(i-1\) local arcs have
already been executed, so the current root at \(U\) is
\(t_U(e_{U,i})\). This holds simultaneously at all three tops of the
packet. The packet is therefore applicable. Induction through the
topological order executes the entire family. \(\square\)

### Corollary 2.2 (source peeling and an exact obstruction certificate)

Repeatedly execute any packet which is next in all three of its local
lists. This peeling process removes every packet if and only if a schedule
exists. If it stalls, the unexecuted precedence digraph contains a directed
cycle.

#### Proof

The exposed packets are exactly the sources of the current precedence
digraph. A finite digraph is acyclic if and only if repeated source
deletion exhausts it. \(\square\)

Thus a stalled directed cycle is a checkable physical obstruction, not a
failure of an averaging estimate.

## 3. The owner-load invariant

Associate to a rooted top \((U,z)\) its lower predecessor owner

\[
                              p(U,z)=U\setminus\{z\}.
\tag{3.1}
\]

For the packet (0.1), the three predecessor owners before the move are

\[
                           C+y,\qquad C+a,\qquad C+x,
\tag{3.2}
\]

and afterwards they are

\[
                           C+x,\qquad C+y,\qquad C+a.
\tag{3.3}
\]

### Lemma 3.1 (exact predecessor-load conservation)

Every root-port packet preserves, pointwise, the complete histogram

\[
 L(P)=|\{U:p(U,r(U))=P\}|,
 \qquad P\in\binom{[n]}{M-1}.
\tag{3.4}
\]

In particular, if the initial predecessor map is injective, it remains
injective after every prefix of any legal schedule.

#### Proof

Equations (3.2)--(3.3) show that the packet permutes the same three
predecessor sets and fixes every other one. \(\square\)

This proves that point-margin or owner Euler balance is necessary but says
nothing about whether the packet precedence relation is acyclic.

## 4. An exact root-port three-event deadlock

Assume

\[
                         M\ge4,\qquad n-M+1\ge3.
\tag{4.1}
\]

Choose an \((M-1)\)-set \(B\), distinct

\[
                    z_1,z_2,z_3\in B,
                    \qquad a,b,c\notin B,
\tag{4.2}
\]

and define

\[
\begin{array}{lll}
 U_a=B+a, & U_b=B+b, & U_c=B+c,\\
 V_{ac}=B-z_1+a+c,&
 V_{ab}=B-z_2+a+b,&
 V_{bc}=B-z_3+b+c.
\end{array}
\tag{4.3}
\]

Take the three oriented packets

\[
\begin{array}{rcl}
 e_1&=&e(B-z_1;c,z_1,a),\\
 e_2&=&e(B-z_2;a,z_2,b),\\
 e_3&=&e(B-z_3;b,z_3,c),
\end{array}
\tag{4.4}
\]

where \(e(C;x,y,a)\) has the orientation (0.1). Their local arcs are

\[
\begin{array}{c|ccc}
 &\text{first shared top}&\text{second shared top}&\text{private top}\\ \hline
e_1&U_c:c\to z_1&U_a:z_1\to a&V_{ac}:a\to c\\
e_2&U_a:a\to z_2&U_b:z_2\to b&V_{ab}:b\to a\\
e_3&U_b:b\to z_3&U_c:z_3\to c&V_{bc}:c\to b.
\end{array}
\tag{4.5}
\]

Prescribe the six initial roots

\[
\begin{array}{lll}
r_0(U_a)=z_1,&r_0(U_b)=z_2,&r_0(U_c)=z_3,\\
r_0(V_{ac})=a,&r_0(V_{ab})=b,&r_0(V_{bc})=c.
\end{array}
\tag{4.6}
\]

### Theorem 4.1 (three-event owner-feasible precedence cycle)

The packets (4.4) are flag-simple. Every one of their six local port
graphs is root-traversable. Their six initial predecessor owners are
pairwise distinct. Nevertheless

\[
                  D(\{e_1,e_2,e_3\},r_0)
                  = (e_1\to e_2\to e_3\to e_1),
\tag{4.7}
\]

so no chronology exists.

#### Proof

At the three shared tops, (4.5)--(4.6) give the forced local lists

\[
 U_a:e_1,e_2,\qquad
 U_b:e_2,e_3,\qquad
 U_c:e_3,e_1.
\tag{4.8}
\]

Each private top has a one-event list. The only repeated local flag label
at a shared top is the head of the first event and the tail of the second,
which use opposite signs. Thus the packet family is flag-simple.

The six initial predecessor sets are

\[
\begin{array}{lll}
B-z_1+a,&B-z_2+b,&B-z_3+c,\\
B-z_1+c,&B-z_2+a,&B-z_3+b.
\end{array}
\tag{4.9}
\]

They are pairwise distinct: each is recovered from the ordered data
consisting of its missing \(z_i\) and its unique outside label. Finally,
(4.8) is exactly the directed cycle (4.7), so Theorem 2.1 forbids a
schedule. \(\square\)

The obstruction is not caused by an owner collision. It is a genuine
three-way wait cycle among locally legal root transitions. Each of the
three columns is an allowed root-port packet type. This statement is at
the root-port incidence level: it does not assert that one can assign
simultaneously compatible \(\omega/\eta\) core words to the six tops.
That additional context condition can only further restrict a positive
construction and is kept explicitly open in Section 7.

### Lemma 4.2 (extension of the six prescribed owners)

Put

\[
             \rho={M\over n-M+1}.
\tag{4.10}
\]

If

\[
                       (\rho-1)(M-6)\ge6,
\tag{4.11}
\]

then the six owner edges (4.9) extend to an injective predecessor choice
on every top in \(\mathcal U\). In particular, for
\(n=2m,M=m+H\), condition (4.11) holds for every fixed \(A>0\) and all
sufficiently large \(m\) whenever \(H\ge A\sqrt m\).

#### Proof

Consider the inclusion bipartite graph between rank \(M\) and rank
\(M-1\). Every left vertex has degree \(M\), and every right vertex has
degree \(n-M+1\). For every nonempty left family \(\mathcal S\), edge
counting and the neighborhood of one member give

\[
              |\Gamma(\mathcal S)|
              \ge \max\{M,\rho|\mathcal S|\}.
\tag{4.12}
\]

Delete the six already matched vertices on each shore. If
\(|\mathcal S|\le M-6\), then

\[
              |\Gamma'(\mathcal S)|\ge M-6\ge|\mathcal S|.
\]

If \(|\mathcal S|>M-6\), (4.11)--(4.12) give

\[
 |\Gamma'(\mathcal S)|
 \ge\rho|\mathcal S|-6
 \ge|\mathcal S|.
\]

Hall's theorem completes the six prescribed edges to a matching
saturating the entire rank-\(M\) shore. For \(n=2m,M=m+H\),

\[
 \rho-1={2H-1\over m-H+1},
\]

so (4.11) follows in the stated regime. \(\square\)

Thus Theorem 4.1 occurs inside a full predecessor-owner baseline,
not merely inside an isolated partial table.

### Lemma 4.3 (bounded-coordinate root-capacity ceiling)

Let \(r_0\) be any injective predecessor choice on all rank-\(M\) tops,
and let \(Q\subseteq[n]\) have size \(q\). Then the number

\[
                    b_Q=|\{U:r_0(U)\in Q\}|
\tag{4.13}
\]

of roots lying in \(Q\) satisfies the exact bound

\[
                    \boxed{
                    b_Q\le {q(2M-n)\over n}\,N.}
\tag{4.14}
\]

For \(n=2m,M=m+H\), this is

\[
                              b_Q\le {qH\over m}N.
\tag{4.15}
\]

#### Proof

Let \(\mathcal I\subseteq\binom{[n]}{M-1}\) be the image of the
injective predecessor map, so \(|\mathcal I|=N\). Deleting a root in
\(Q\) lowers intersection with \(Q\) by one, while deleting a root
outside \(Q\) does not. Hence

\[
 b_Q
 =\sum_{U\in\binom{[n]}M}|U\cap Q|
  -\sum_{P\in\mathcal I}|P\cap Q|.
\tag{4.16}
\]

Put \(R=\binom n{M-1}\). The first sum is \(qMN/n\), and the sum over
the entire rank \(M-1\) is \(q(M-1)R/n\). Since \(\mathcal I\) omits
exactly \(R-N\) sets and every omitted set contributes at most \(q\),

\[
 \sum_{P\in\mathcal I}|P\cap Q|
 \ge {q(M-1)R\over n}-q(R-N).
\tag{4.17}
\]

Using

\[
                         {R\over N}={M\over n-M+1},
\tag{4.18}
\]

the right side of (4.17) simplifies to \(qN(n-M)/n\). Substitution in
(4.16) gives (4.14). \(\square\)

### Corollary 4.4 (fixed-seed deadlocks cannot give a linear critical obstruction)

Suppose pairwise top-disjoint copies of Theorem 4.1 all use their six
labels in one fixed set \(Q\) of size six and are aligned with one full
injective initial predecessor baseline. If there are \(g\) copies, then

\[
                           6g\le b_Q,
 \qquad
                           g\le {H\over m}N.
\tag{4.19}
\]

Thus for \(H=O(\sqrt m)\), every such fixed-six-coordinate obstruction
has only \(o(N)\) copies and can be removed within the requested
\(o(N)\) event scale. A lower bound of order \(N\) must use a
coordinate-diffuse or growing-size family of precedence cycles. Theorem
4.1 proves that acyclicity is an independent statewise constraint; it
does not by itself disprove an asymptotic \(o(N)\)-feedback theorem.

## 5. Free cycle cuts when the initial roots are not prescribed

Suppose every local graph is already one path or one cycle, but roots on
the cyclic tops may still be chosen. Let \(A_U\) be the set of successor
precedence incidences around the local directed cycle at \(U\). Choosing
the root at \(U\) is equivalent to choosing exactly one incidence in
\(A_U\) as the omitted wrap edge.

Let \(D_0\) contain all path precedence arcs and every cyclic successor
arc before cuts. Introduce variables \(z_\alpha\in\{0,1\}\), one for each
optional cyclic incidence \(\alpha\), with \(z_\alpha=1\) meaning that
\(\alpha\) is cut.

### Proposition 5.1 (exact partitioned cycle-transversal program)

A choice of roots on all cyclic tops yields a topological schedule if and
only if

\[
 \sum_{\alpha\in A_U}z_\alpha=1
 \qquad\text{for every cyclic top }U,
\tag{5.1}
\]

and

\[
 \sum_{\alpha\in Z}z_\alpha\ge1
 \qquad\text{for every directed cycle }Z\text{ of }D_0,
\tag{5.2}
\]

where path-precedence arcs have fixed value zero.

#### Proof

Equation (5.1) makes exactly one root cut on every local cycle. The
resulting precedence graph is \(D_0\) with precisely those arcs removed.
It is acyclic exactly when the removed arcs meet every directed cycle,
which is (5.2). \(\square\)

This is the correct global cut problem. Cutting every local cycle at an
independently chosen minimum priority does not prove (5.2).

For comparison, if a local path has \(d\) events, a uniformly random
global priority respects its fixed order with probability \(1/d!\). If a
local cycle has \(d\) events and its cut may be chosen afterwards, exactly
\(d\) of the \(d!\) relative orders are compatible, giving probability

\[
                              {1\over(d-1)!}.
\tag{5.3}
\]

Thus independent random priorities are not a plausible high-probability
construction when typical local trails have length \(\Theta(M)\). A
successful priority must be built together with the packet selection.

## 6. Quantitative component and feedback obstructions

For fixed roots and root-traversable local families, let

\[
                  \tau(\mathcal E,r_0)
                  =\tau_{\rm FVS}(D(\mathcal E,r_0))
\tag{6.1}
\]

be the minimum number of packet events whose deletion makes the
precedence digraph acyclic. Any collection of \(s\) vertex-disjoint
directed cycles gives the exact lower bound

\[
                         \tau(\mathcal E,r_0)\ge s.
\tag{6.2}
\]

There is a separate local obstruction. Let \(\ell_U\) be the largest
number of arcs in one weak component of \(G_U(\mathcal E)\). Any subfamily
whose local events form one trail at every top satisfies

\[
                         3|\mathcal E'|
                         \le\sum_{U\in\mathcal U}\ell_U.
\tag{6.3}
\]

Indeed every packet contributes one local arc at each of three tops, and
deletion cannot join two old components.

Apply (6.3) to the inverse-doublet matching constructed in
`MATH_THEOREM_ROOT_PORT_FLAG_DOUBLET_AND_CONTEXT_COALESCENCE_OBSTRUCTION_20260727.md`.
If its unsigned triangle matching has \(K\) triangles, then

\[
                         K=(1-o(1)){MN\over6},
\qquad |\mathcal E|=2K,
\tag{6.4}
\]

and \(\ell_U\le2\). Therefore every locally one-trail subfamily obeys

\[
                         |\mathcal E'|\le {2N\over3},
\tag{6.5}
\]

so deletion alone must remove at least

\[
             2K-{2N\over3}
             =\left({M-2\over3}-o(M)\right)N
             =\Omega(MN)
\tag{6.6}
\]

events. If a replacement scheme changes \(s\) original occurrences,
then at least \(K-s\) inverse doublets remain intact. A connected local
family can contain intact doublets at at most one per top, hence at most
\(N/3\) of them globally. Consequently

\[
                         s\ge K-{N\over3}
                         =\left({M-2\over6}-o(M)\right)N.
\tag{6.7}
\]

This independently closes sparse post-processing of an arbitrary
near-perfect flag matching. It does not rule out selecting a coherent
anti-doublet family from the start.

## 7. Exact proved and open boundary

Proved here:

1. the necessary-and-sufficient rooted precedence-DAG theorem;
2. the correct wrap-cut treatment of local directed cycles;
3. exact preservation of every predecessor-owner load;
4. an explicit owner-feasible three-event directed deadlock, extendable
   to a full predecessor matching at the critical scale;
5. the exact bounded-coordinate capacity ceiling, showing that a fixed
   seed cannot yield a linear critical feedback obstruction;
6. the exact partitioned cycle-transversal formulation when roots are
   free;
7. the feedback-cycle lower bound and sharp \(\Omega(MN)\) doublet
   component obstruction.

Not proved:

1. a selection of \(\Theta(MN)\) packet events whose local graphs have
   one \(M-o(M)\)-edge trail on all but \(o(N)\) tops;
2. an \(o(N)\) feedback set for such a selection;
3. compatibility of the topological schedule with the common oriented
   core-order signatures and full \(\omega/\eta\) contexts; or
4. an installation in one exact middle factor with all protected shadow
   columns retained.

The deterministic target is therefore not an unstructured flag matching
followed by random priorities. It is a single integral selection in which
long local trails, owner roots, packet contexts, and the cycle-transversal
constraints (5.1)--(5.2) are imposed simultaneously.
