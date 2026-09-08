# Stateful full-status continuations: exact queue degree, lifted Hall, and the endpoint history cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
                         H=\sqrt m\,\omega(m),
 \qquad \omega(m)\longrightarrow\infty,
 \qquad H=o(m).                                      \tag{0.1}
\]

There is a sharp distinction between a continuation in the full
split-status cube and a continuation which must land at another endpoint
of W's product-SCD path atlas.

1.  **The raw status cube is robust.**  In a status cell (Q_e), recent
    insertion and removal queues of total size (r) forbid at most (r)
    pair axes.  Hence every state has at least (e-r) legal one-step
    continuations and

    \[
                          (e-r)_{\ell}                \tag{0.2}
    \]

    legal ordered geodesic continuations of length (ell\le e-r).
    Outside (e^{-\Omega(m)}W) middle owners, (e\ge m/3).  Thus an
    arbitrary history of size at most (2H) leaves at least (m/4)
    one-step choices and at least ((m/4)_H) legal (H)-step words.

2.  **The queue lift has exact Hall.**  If the last (r) used status
    axes are included in the state, the legal-transition digraph is
    ((e-r))-in/((e-r))-out regular.  It therefore has an integral cycle
    cover.  This is a theorem on the lifted history space; it uses every
    physical owner ((e)_r) times and is not an owner-disjoint middle
    factor.

3.  **Endpoint restriction can erase all of that degree.**  In one
    status cell the endpoint continuation graph is the induced cube graph
    on the W endpoint ports.  After an arbitrary history, its exact Hall
    condition is Hall in this induced graph after deleting the history's
    direction set.  A singleton port of endpoint degree at most (r) is
    isolated by a realizable (r)-label history.  Thus a theorem robust
    against *every* (O(H))-history requires minimum endpoint degree
    greater than (H), before any nonsingleton Hall cut is considered.

4.  **The audited cross-control seam family fails this test by a factor
    ω.**  Uniformly for every fixed coordinate pairing and every
    central start stratum

    \[
                   c=m/2-y\sqrt m+O(1),\qquad
                   0<\epsilon\le y\le B<\infty,       \tag{0.3}
    \]

    at least half of the strict (A\)-controlled endpoint ports have at
    most

    \[
                         (8B+o(1))\sqrt m              \tag{0.4}
    \]

    cross-control status continuations.  The analogous statement holds
    with (A,B) interchanged and at the opposite endpoint.  Since
    (H/\sqrt m\to\infty), an allowed state-dependent history isolates
    every one of these ports.  The previously proved
    Θ\((\sqrt m)\) average seam abundance therefore does **not**
    upgrade to arbitrary-history Hall.

5.  Same-control endpoint seams may have linear degree and are not closed
    by (0.4).  Their exact full-menu graph is a union of two complete
    rectangles.  If (U_A,U_B) are its two boundary-coordinate sets,
    the minimum number of physical labels which kills every closer-centre
    continuation is

    \[
                  \boxed{\min\{m-c,|U_A|+|U_B|\}}.    \tag{0.5}
    \]

    Thus the precise remaining local statistic is whether
    (|U_A|+|U_B|\gg H) on almost all endpoint ports, together with the
    corresponding cellwise Hall expansion.  No existing SCD census or
    status marginal proves this.

Accordingly, the full status menu solves state memory before the endpoint
condition, but it does not solve stateful W-path fusion.  There is a
genuine low-complexity history cut on the only previously audited
cross-control family; the same-control sector is the exact surviving
escape.

## 1. The exact insertion/removal queue law in one status cell

Fix a perfect matching

\[
                         P_1,\ldots,P_e              \tag{1.1}
\]

of the split coordinates of one status cell.  At an owner (X), write
(p_j(X)) for the present endpoint of (P_j) and (a_j(X)) for its
absent endpoint.  Toggling axis (j) performs the Johnson swap

\[
                         p_j(X)\longmapsto a_j(X).   \tag{1.2}
\]

Let ({\cal I}\subseteq X) be the recent insertion queue and
({\cal R}\subseteq[2m]\setminus X) the recent removal queue.  A new
swap is geodesically legal relative to these queues exactly when

\[
                   p_j(X)\notin{\cal I},\qquad
                   a_j(X)\notin{\cal R}.             \tag{1.3}
\]

Indeed, deleting a recent insertion or reinserting a recent removal is
precisely a coordinate cancellation.

### Lemma 1.1 (sharp raw degree)

Put

\[
 B_X({\cal I},{\cal R})
 =\{j:p_j(X)\in{\cal I}\text{ or }a_j(X)\in{\cal R}\}. \tag{1.4}
\]

Then

\[
 |B_X({\cal I},{\cal R})|
 \le |{\cal I}|+|{\cal R}|,                         \tag{1.5}
\]

and the exact legal one-step degree is

\[
                         e-|B_X({\cal I},{\cal R})|. \tag{1.6}
\]

Both bounds are sharp.

#### Proof

Every physical label lies in one matched pair, so one queue label forbids
at most one status axis.  This proves (1.5).  Conditions (1.3) are
necessary and sufficient independently on every split pair, proving
(1.6).  Equality in (1.5) occurs when all queue labels lie in different
pairs and have the appropriate present/absent orientation. \(\square\)

### Lemma 1.2 (all finite continuations)

Let (b=|B_X({\cal I},{\cal R})|).  For every
(0\le\ell\le e-b), the number of ordered length-(ell) status-cube
paths which use distinct initially legal axes is exactly

\[
                         (e-b)_{\ell}.               \tag{1.7}
\]

Every such path is geodesic and remains compatible with the evolving
queues.

#### Proof

Choose and order (ell) axes from the (e-b) legal axes.  Distinct
matched pairs have disjoint physical labels.  Toggling one chosen axis
therefore changes neither the legality nor the orientation data of any
other chosen axis.  The newly inserted and removed labels can only forbid
reuse of the axis just taken, and reuse was excluded.  Conversely every
return-free status path has an ordered list of distinct axes. \(\square\)

For a uniformly chosen middle owner under one fixed ambient coordinate
pairing, the number (e) of split pairs is a binomial-(1/2) variable
before conditioning on rank.  Hence

\[
 {1\over W}\#\{X:|X|=m,\ e(X)<m/3\}
 \le(2m+1)e^{-m/36}.                                \tag{1.8}
\]

The factor (2m+1) is the reciprocal lower bound for the probability of
the central rank.  Equations (0.1), (1.6), and (1.8) prove the raw degree
claims in Section 0.

## 2. Exact Hall on the lifted queue space

Fix (0\le r<e).  Let

\[
 {\cal S}_{e,r}
 =\{(x;q_1,\ldots,q_r):x\in Q_e,\ q_1,\ldots,q_r
                         \text{ are distinct axes}\}.          \tag{2.1}
\]

There is a directed transition

\[
 (x;q_1,\ldots,q_r)
 \longrightarrow
 (x\triangle\{j\};q_2,\ldots,q_r,j)                \tag{2.2}
\]

for every (j\notin\{q_1,\ldots,q_r\}).

### Theorem 2.1 (regular queue Hall)

The digraph (2.2) has indegree and outdegree exactly (e-r).  Hence its
tail--head bipartite graph has a perfect matching, and there is a
permutation of ({\cal S}_{e,r}) every one of whose transitions avoids
the last (r) axes.

#### Proof

The outdegree is immediate.  Given a head
((y;q_2,\ldots,q_r,j)), the preceding owner must be
(x=y\triangle\{j\}), while the forgotten oldest axis (q_1) may be any
of the (e-r) axes outside
({q_2,\ldots,q_r,j}).  Thus the indegree is also (e-r).  Every
finite regular bipartite graph has a perfect matching by edge counting in
Hall's condition. \(\square\)

Every orbit of the resulting permutation is a legal stateful word.  But

\[
                         |{\cal S}_{e,r}|=2^e(e)_r,  \tag{2.3}
\]

so this theorem repeats every physical owner ((e)_r) times.  Projecting
one state per owner is a new complete-mapping/section problem; regularity
of the lift does not solve it.

## 3. Endpoint ports: the exact robust-Hall formulation

Fix one ternary status word (eta) with (e=e(\eta)) stars.  Let
(E_\eta\) be the multiset of W product-SCD endpoint ports in its
orientation cube (Q_e).  An ordinary nonzero-length path contributes one
port at an endpoint owner; a zero-length path contributes two formal ports
at the same owner.

Ignoring the degree-two exceptional ports for notation, put

\[
                         G_\eta=Q_e[E_\eta].         \tag{3.1}
\]

If a history meets the physical pairs indexed by
(J\subseteq[e]), delete every edge of those directions and write
(G_\eta-J).

### Proposition 3.1 (exact arbitrary-history Hall test)

A matching which saturates the chosen endpoint shore after every history
using at most (r) status directions exists if and only if

\[
 |N_{G_\eta-J}(S)|\ge |S|                          \tag{3.2}
\]

for every endpoint family (S), every status cell (eta), and every
(J\subseteq[e]) with (|J|\le r).  For port demand two, replace (3.2)
by the standard capacitated bipartite (b)-matching cuts with unit edge
capacity.

For a fixed (S), define its directional blocker number

\[
 \kappa_\eta(S)
 =\min\{|J|:|N_{G_\eta-J}(S)|<|S|\}.               \tag{3.3}
\]

Then robust Hall through history size (r) is exactly

\[
                         \min_{\eta,S}\kappa_\eta(S)>r.        \tag{3.4}
\]

In particular, for one port (x),

\[
                         \kappa_\eta(\{x\})=d_{G_\eta}(x).     \tag{3.5}
\]

#### Proof

Equation (3.2) is Hall's theorem after the indicated direction deletion.
Taking the minimum history which violates one cut gives (3.3)--(3.4).
At one cube vertex, distinct incident edges have distinct directions.
Deleting all its incident directions isolates it, and fewer directions do
not, proving (3.5). \(\square\)

The history in (3.5) is not merely formal.  Suppose the candidate seams
insert the distinct absent labels (u_1,\ldots,u_d).  Choose distinct
present labels (v_1,\ldots,v_d\).  The Johnson geodesic

\[
 X+\{u_1,\ldots,u_d\}-\{v_1,\ldots,v_d\}
 \longrightarrow X                                  \tag{3.6}
\]

which successively swaps (u_i\mapsto v_i) realizes
({u_1,ldots,u_d}) as the recent removal queue.  It blocks every
candidate insertion (u_i).  The deletion-queue version is symmetric.
Thus every singleton blocker of size at most (H) is a literal history
cut.

## 4. Exact coordinate graph of closer-centre endpoint seams

The endpoint condition has a useful two-rectangle normal form.  Work
below the centre.  Let

\[
 X=(I,J),\qquad |I|=c,\quad |J|=m-c,quad c<m/2,     \tag{4.1}
\]

be a low endpoint controlled by the (A)-chain, so (I) is a chain
bottom of start (c).  Define

\[
 U_A(X)=\{u\in A\setminus I:I+u
                    \text{ is a chain bottom of start }c+1\}, \tag{4.2}
\]

\[
 U_B(X)=\{v\in J:J-v
                    \text{ is a chain top of start }c+1\}.    \tag{4.3}
\]

A cross swap toward the centre has the form

\[
                         (I,J)\longmapsto(I+u,J-v).  \tag{4.4}
\]

### Theorem 4.1 (two-rectangle endpoint normal form)

Put (L=A\setminus I), (R=J), and (n=|L|=|R|=m-c).  The full
coordinate graph of swaps (4.4) landing at another low endpoint is

\[
 \boxed{
 K_{U_A,R}\ \cup\ K_{L,U_B}.}                       \tag{4.5}
\]

If (a=|U_A|) and (b=|U_B|), its maximum matching number and minimum
vertex-cover number are both

\[
                         \boxed{\min\{n,a+b\}}.      \tag{4.6}
\]

Consequently an arbitrary physical-label history of the size in (4.6)
kills every closer-centre continuation, even if every possible cross pair
is allowed.  For one fixed perfect matching of (A) to (B), the blocker
can only be smaller.

#### Proof

The new owner is a product-SCD endpoint exactly when its (A)-component
is a bottom or its (B)-component is a top.  These are respectively the
conditions (u\in U_A) and (v\in U_B), proving (4.5).

The set (U_A\cup U_B) is a vertex cover of size (a+b), while either
whole shore is a cover of size (n).  Conversely, if (a+b\le n), match
the (a) vertices of (U_A) into (R\setminus U_B) and the (b)
vertices of (U_B) into (L\setminus U_A); the inequalities needed are
(a\le n-b) and (b\le n-a).  This gives a matching of size (a+b).
If (a+b\ge n), first match (L\setminus U_A) into (U_B), possible
because (n-a\le b), and then match the remaining (U_A) vertices to
the remaining right vertices.  This is a perfect matching of size (n).
Kőnig's theorem proves (4.6). \(\square\)

The same theorem holds above the centre, at high endpoints, and with the
two halves interchanged.  Formula (4.6) is the promised exact history
statistic: raw split-axis abundance says nothing about (a+b).

For a uniformly random coordinate pairing (phi:A\to B), the expected
number of its pair edges lying in (4.5) is exactly

\[
 {n(a+b)-ab\over m}.                                \tag{4.7}
\]

This follows because every coordinate edge belongs to a uniform random
perfect matching with probability (1/m).  Equation (4.7) is only a
first moment.  It neither gives a minimum degree for one (phi) nor any
Hall expansion after histories.

## 5. A uniform history cut for the audited cross-control sector

Let

\[
 n_c=\binom mc-\binom m{c-1}.                       \tag{5.1}
\]

Write ({\cal B}_c^A) for the (n_c) (A)-chain bottoms of rank (c),
and ({\cal T}_{c+1}^B) for the (n_{c+1}) (B)-chain tops of rank
(m-c-1).  The strict (A)-controlled low endpoint ports at stratum
(c) number

\[
                         n_c\binom m{c-1}.           \tag{5.2}
\]

Indeed the second component can be any rank-((m-c)) set except one of
the (n_c) chain tops, and
(inom mc-n_c=inom m{c-1}).

Fix an arbitrary coordinate pairing (phi:A\to B).  A cross-control
seam is one for which the new endpoint is controlled by its (B)-chain.
Its total number is at most

\[
 E_c^{A\to B}(\phi)
 =\sum_{u\in A}
   |\{I\in{\cal B}_c^A:u\notin I\}|
   |\{T\in{\cal T}_{c+1}^B:\phi(u)\notin T\}|.      \tag{5.3}
\]

The equality counts all (A)-controlled ports, including the negligible
tied subfamily; hence it is an upper bound for the strict subfamily.

### Theorem 5.1 (cross-control arbitrary-history cut)

For every pairing (phi), the average cross-control degree over the
strict ports in (5.2) is at most

\[
 \bar d_c(\phi)
 \le {m n_{c+1}\over\binom m{c-1}}.                 \tag{5.4}
\]

Uniformly under (0.3),

\[
                         \bar d_c(\phi)
 \le(4B+o(1))\sqrt m.                               \tag{5.5}
\]

Therefore at least half of those ports have degree at most
((8B+o(1))\sqrt m), and each such port is isolated by a realizable
history of that size.  In particular no cross-control endpoint matching
is robust against every history of size (H).

#### Proof

Each of the two factors in a summand of (5.3) is at most (n_c) and
(n_{c+1}), respectively.  Hence

\[
                         E_c^{A\to B}(\phi)
 \le m n_c n_{c+1}.                                 \tag{5.6}
\]

Divide by (5.2) to get (5.4).  The exact identities

\[
 n_{c+1}=\binom m{c+1}{m-2c-1\over m-c},\qquad
 {\binom m{c+1}\over\binom m{c-1}}
 ={(m-c+1)(m-c)\over c(c+1)}                       \tag{5.7}
\]

give

\[
 {m n_{c+1}\over\binom m{c-1}}
 ={m(m-c+1)(m-2c-1)\over c(c+1)}.                  \tag{5.8}
\]

Substitute (0.3) to obtain (4y\sqrt m+O_B(1)), uniformly for
(y\in[\epsilon,B]), proving (5.5).  Markov's inequality gives the
half-port assertion.  At one port the candidate status directions are
distinct, so Proposition 3.1 and the realizability construction (3.6)
give the history cut.  Finally (0.1) eventually makes
((8B+o(1))\sqrt m<H). \(\square\)

The chain-start local limit density

\[
                         4y e^{-2y^2},\qquad y>0,    \tag{5.9}
\]

shows that any fixed interval ([\epsilon,B]) carries a positive fraction
of endpoint ports.  Thus Theorem 5.1 is not confined to a negligible
extreme tail.

## 6. Full collars and the exact remaining codegree

A seam edge can avoid the current queues and still fail after entering
the next W path.  For an endpoint port (x), candidate seam (e), and
integer (t\), let (K_t(e)) be the physical labels used by the seam and
the first (t) edges of the proposed continuation, with insertion and
removal types retained.  Define

\[
 \Delta_t(x;z)=|\{e:z\in K_t(e)\}|,
 \qquad
 \Delta_t^{\max}(x)=\max_z\Delta_t(x;z).            \tag{6.1}
\]

For a correctly typed history (F), the surviving degree satisfies the
exact union-bound certificate

\[
 d_{F,t}(x)
 \ge d_t(x)-\sum_{z\in F}\Delta_t(x;z)
 \ge d_t(x)-|F|\Delta_t^{\max}(x).                  \tag{6.2}
\]

The corresponding exact obstruction is the collar transversal number

\[
 \tau_t(x)=\min\{|F|:F\cap K_t(e)\ne\varnothing
                         \text{ for every candidate }e\}.     \tag{6.3}
\]

There is a continuation after every history of size (r) if and only if

\[
                         \tau_t(x)>r.                \tag{6.4}
\]

At (t=0), (6.3) reduces to the endpoint direction blocker.  For the
full cross-pair menu in Theorem 4.1 it is exactly (4.6).  For one fixed
pair frame it is at most the endpoint degree and gives the singleton cut
of Proposition 3.1.

No audited theorem bounds Δ in (6.1), τ in (6.3), or the
nonsingleton robust-Hall cuts uniformly over W endpoints.  In particular,
the raw estimate (e-O(H)=\Theta(m)) cannot be substituted for the
endpoint degree (d_t(x)).

## 7. Precise proved and conditional boundary

The following are proved.

* Full split-status cells have deterministic linear residual degree after
  every (O(H))-label history and superpolynomially many legal
  (H)-step geodesic words.
* The complete queue-state lift has an integral legal cycle cover.
* Literal endpoint fusion is governed by direction-deleted cellwise Hall,
  not by split-axis abundance.
* The closer-centre endpoint menu has the exact two-rectangle form (4.5)
  and exact history cover (4.6).
* Every fixed pair frame has a positive central family of cross-control
  ports isolated by allowable (O(\sqrt m)\) histories.  Hence the
  Θ\((\sqrt m)\) abundance theorem is quantitatively insufficient for
  (H=\sqrt m\,\omega).

The surviving positive route must use the same-control rectangles with

\[
                         |U_A(x)|+|U_B(x)|\gg H       \tag{7.1}
\]

on almost every port, then prove all cellwise cuts (3.2) after every
history and all collar transversals (6.4) through the changing sequence
of Θ\((\omega)\) path segments.  Even those local statements would
still need an owner-disjoint global cycle selection.  None follows from
the current status-cube or product-SCD censuses.

Thus the stateful audit gives both a positive raw-cube theorem and a
genuine endpoint history cut.  It does not prove or disprove the final
same-control bulk-fusion escape.
