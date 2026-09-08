# K17 four-flag address drift, exact reset demand, and the correlated Hall gate

**Date:** 2026-08-02  
**Status:** exact abstract reduction.  The numerical matching values quoted in
Section 5 are pairwise-projection values; they are not a simultaneous
state-selection certificate.  No residence, upper-shadow, source, compiler,
or final-word claim is made.

## 1. Ordered long flags

For a long row

\[
 L\subset M\subset U\subset T,\qquad
 K=M\setminus L,\quad \{p\}=U\setminus M,
\]

put \(B=K\cup Y\) and \(A=\{p\}\cup Z\), where
\(Y\subseteq L\) and \(Z\subseteq M\).  The four exact interval-address
classes, in their drift order, are

\[
\begin{array}{c|c|c}
q&\text{address}&\text{state}\ \\ \hline
0&12/1&(L,B,A),\\
1&12/2&(B,L,A),\\
2&23/2&(A,L,B),\\
3&23/3&(A,B,L).
\end{array}                                                    \tag{1.1}
\]

The complete long-to-long compatibility predicate is the literal shift
predicate: if \(g\) is the source state and \(h\) the target state, then

\[
                    g_2=h_1,\qquad g_3=h_2,             \tag{1.2}
\]

together with the frozen owner equation.

The four-normal-form calculation gives the **address-drift lemma**

\[
             g\text{ has flag }\alpha, h\text{ has flag }\beta,
             \quad g\longrightarrow h
             \quad\Longrightarrow\quad \alpha\leq\beta .     \tag{1.3}
\]

For completeness, substituting the four rows of (1.1) into (1.2) gives

\[
\begin{array}{c|c}
(\alpha,\beta)&\text{forced repetition}\ \\ \hline
(1,0)&L_j=L_i,\\
(2,0)&L_j=L_i,\\
(2,1)&L_j=B_i,\ B_j=L_i,\text{ hence }M_j=M_i,\\
(3,0)&B_j=L_i,\ L_j=B_i,\text{ hence }M_j=M_i,\\
(3,1)&L_j=L_i,\\
(3,2)&L_j=L_i.
\end{array}                                                   \tag{1.4}
\]

Distinct rows in the exact target-chain partition cannot share an
\(L\)-target or an \(M\)-target.  A same-row arc is separately excluded:
every first cell of a long-row state lies in \(U_i\), so it cannot enlarge
\(U_i\) to the strict owner \(T_i\).  Thus (1.3) is about literal states,
not merely the observed zero entries of a finite matrix.

It follows immediately that every directed cycle consisting only of long
roles has constant flag: around such a cycle

\[
              q_0\leq q_1\leq\cdots\leq q_{r-1}\leq q_0.
                                                               \tag{1.5}
\]

In particular, a full-chain reinsertion which remains in class \(q=3\)
does not create a reset.  A strict descent can occur only across a short
role or across a certified macro which leaves the long four-flag class.

## 2. Exact socket count in a cycle cover

Let \({\cal L}\) and \({\cal S}\) be the long and short roles.  For the
frozen K17 table,

\[
                    |{\cal L}|=18,663,\qquad
                    |{\cal S}|=5,647.                         \tag{2.1}
\]

Fix a directed cycle cover and let

\[
 b=|E({\cal S},{\cal L})|.
\]

Counting entrances and exits of \({\cal L}\) in a permutation gives the
exact identity

\[
             b=|E({\cal S},{\cal L})|
              =|E({\cal L},{\cal S})|
              =|{\cal L}|-|E({\cal L},{\cal L})|.             \tag{2.2}
\]

After deleting the short vertices, the long subgraph is a disjoint union
of constant-flag directed cycles and exactly \(b\) directed long paths.
Equivalently, the mixed cycles contain exactly \(b\) maximal nonempty long
blocks and \(b\) maximal nonempty short blocks.  Every short block consumes
at least one short role, so

\[
                              b\leq5,647.                       \tag{2.3}
\]

This \(b\), rather than the number of nonzero entries in the aggregate
flag matrix, is the exact number of socket blocks demanded by a proposed
cycle cover.  Treating all 5,647 raw short roles as 5,647 independent
one-vertex sockets is an additional construction hypothesis: consecutive
short roles contract to one socket block unless independent ports have been
certified.

## 3. Threshold reset vector

For \(t=0,1,2\), define

\[
 D_t=\#\{\text{selected long arcs }\alpha\to\beta:
                         \alpha\leq t<\beta\}.                 \tag{3.1}
\]

Thus \(D_t\) is the number of selected long arcs which drift upward across
the address cut \(\{0,\ldots,t\}\mid\{t+1,\ldots,3\}\).

Let \(a_q\) be the number of short-to-long entrances at flag \(q\), and
let \(c_q\) be the number of long-to-short exits at flag \(q\).  Balance of
the flag classes gives, for every cut,

\[
                 \sum_{q\leq t}a_q-\sum_{q\leq t}c_q=D_t.
                                                               \tag{3.2}
\]

A downward socket from an exit of flag \(v\) to an entrance of flag \(u\),
where \(u<v\), resets precisely the nonempty interval of cuts

\[
                         I(u,v)=\{u,u+1,\ldots,v-1\}.           \tag{3.3}
\]

There are six nonempty interval types.  Neutral sockets have types
\((q,q)\), one for each of the four endpoint flags.  If upward short
bridges are forbidden, and \(y_{uv}\) is the number of sockets of type
\((u,v)\), then the exact cut equation is

\[
       \sum_{0\leq u<v\leq3}y_{uv}{\bf1}_{\{u\leq t<v\}}=D_t
       \quad(t=0,1,2).                                      \tag{3.4}
\]

If upward short bridges are allowed, (3.4) must instead use signed
downward-minus-upward columns.  Omitting that sign is not proof-safe.

### Theorem 3.1 (minimum anonymous reset supply)

The minimum number of nonneutral interval sockets whose columns sum to
\(D=(D_0,D_1,D_2)\) is

\[
 \boxed{\rho(D)=D_0+(D_1-D_0)_+ +(D_2-D_1)_+}
                                                               \tag{3.5}
\]

or, equivalently,

\[
 \rho(D)=\max\{D_0,D_1,D_2,D_0+D_2-D_1\}.                    \tag{3.6}
\]

Consequently every completion by the 5,647 short roles satisfies

\[
                         \rho(D)\leq b\leq5,647.               \tag{3.7}
\]

#### Proof

Read the three cut loads from left to right.  Every one of the \(D_0\)
units present at cut zero starts an interval there.  If
\(D_1>D_0\), at least \(D_1-D_0\) further intervals must start at cut one;
if \(D_2>D_1\), at least \(D_2-D_1\) further intervals must start at cut
two.  This proves the lower bound in (3.5).

It is attained by continuing as many live intervals as possible across
each next cut, ending the excess when the load decreases and starting
exactly the deficit when it increases.  This constructs a multiset of the
six intervals with coverage vector exactly \(D\).  Expanding the two
positive parts gives (3.6).  Neutral sockets fill any unused part of the
budget \(b\).  \(\square\)

The same number is the minimum even if signed upward intervals are allowed:
append zeros at both ends of the load sequence.  Its discrete derivative
has total positive mass \(\rho(D)\), and every signed interval transports
one unit from a positive boundary to a negative boundary.  Upward sockets
can change which types occur, but cannot lower their total number.

For fixed endpoint marginals, use variables \(y_{uv}\),
\(0\leq u\leq v\leq3\), and impose

\[
 \sum_{v\geq u}y_{uv}=a_u,
 \qquad
 \sum_{u\leq v}y_{uv}=c_v.                                  \tag{3.8}
\]

Equation (3.2) is exactly the dominance condition for a transportation
with \(u\leq v\), so (3.8) has an integral solution.  Its minimum number
of off-diagonal entries is again \(\rho(D)\).  Notice that a single
undifferentiated neutral type loses the four marginal equations in (3.8).

## 4. Capacitated socket Hall criterion

First freeze the selected long states and the unmatched long path
endpoints.  Let \({\cal B}\) be the set of certified socket blocks to be
used.  For each socket \(s\), let \(P_s\) be its menu of types
\((u,v)\), including the appropriate neutral types.  Fix nonnegative type
counts \(y_{uv}\) satisfying (3.8), and suppose

\[
                         \sum_{u\leq v}y_{uv}=|{\cal B}|.       \tag{4.1}
\]

Replace each type \((u,v)\) by \(y_{uv}\) identical slots.  There is an
assignment of every physical socket to one allowed type, with exactly the
prescribed counts, if and only if

\[
 \boxed{
 |X|\leq\sum_{(u,v)\in N(X)}y_{uv}
 \quad\text{for every }X\subseteq{\cal B},}
                                                               \tag{4.2}
\]

where \(N(X)=\bigcup_{s\in X}P_s\).  This is ordinary capacitated Hall,
or equivalently a unit-capacity max flow from socket roles to type bins.

Criterion (4.2) assigns only flag types.  Each socket must still attach to
one specific unmatched exit and one specific unmatched entrance.  Two
separate endpoint Hall tests are sufficient only after the socket's
left- and right-end menus factor as a Cartesian product for the already
fixed rectangle/type.  Without that factorization, endpoint attachment is
a joint correlated matching problem, not two independent flows.

There is a second useful Hall form which does not first choose type counts.
For a fixed state selection, let \(H\) be a bank of long heads,
\(N_L(X)\) its compatible long predecessors, and \(N_S(X)\) its compatible
socket predecessors.  If socket \(s\) has independently certified capacity
\(c_s\), then all heads in \(H\) can receive distinct predecessors if and
only if

\[
 \boxed{
 |X|\leq |N_L(X)|+\sum_{s\in N_S(X)}c_s
 \quad\text{for every }X\subseteq H.}                         \tag{4.3}
\]

This is the min-cut criterion in the network

\[
 \text{source}\to(\text{long/socket predecessor})
 \to(\text{long head})\to\text{sink}.                         \tag{4.4}
\]

For raw one-copy short roles, \(c_s=1\).  A scalar capacity greater than
one is valid only for a macro with that many independently routable ports;
several correlated ports require the macro's joint configuration instead.

If every short predecessor were universal, (4.3) would reduce to

\[
 \max_{X\subseteq H}\bigl(|X|-|N_L(X)|\bigr)_+\leq5,647.      \tag{4.5}
\]

Actual socket neighborhoods cannot be replaced by this raw-count test.

## 5. Frozen-table projection numbers

For the 18,646 hard long heads, the existing pairwise union projection has
the flag-pair role counts

\[
\begin{pmatrix}
4827&4407&5770&14488\\
0&1196&2295&5668\\
0&0&1276&4528\\
0&0&0&4738
\end{pmatrix}.                                               \tag{5.1}
\]

The zeros below the diagonal agree with (1.3).  The matrix contains 49,193
projected role pairs, but these aggregate counts do not determine either a
matching or a reset vector.

The maximum projected matching from the 18,663 long suppliers into the
18,646 hard heads is 14,844.  Hence the exact long-only Hall deficiency of
this relaxation is

\[
                18,646-14,844=3,802.                           \tag{5.2}
\]

Thus every physical completion needs at least 3,802 short-to-hard
predecessors.  Under the deliberately optimistic assumption that all short
roles are universal, 3,802 is attainable and leaves only

\[
                         5,647-3,802=1,845                      \tag{5.3}
\]

raw socket units for the other breaks.  In the actual problem, (5.2) is a
lower bound, not an existence certificate.

Combining the adjacency and drift ledgers, every actual selected cover on
this state class must therefore obey

\[
             \boxed{\max\{3,802,\rho(D)\}\leq b\leq5,647.}     \tag{5.4}
\]

The two lower bounds are not additive: a short block used to repair the
role-level Hall deficit may simultaneously carry a nonneutral flag reset.

A reported all-row union-projection matching into the same hard bank is
18,115, leaving 531 hard heads uncovered.  Once independently replayed,
this is a direct failure of (4.3), even before same-role correlation:

\[
                         18,646-18,115=531.                     \tag{5.5}
\]

The raw inequality \(3,802<5,647\) therefore does not discharge the socket
gate; the missing supply is localized on a Hall shore.

## 6. Same-role correlation and the exact cycle-cover master

Pairwise projection is only a relaxation.  A projected incoming edge of a
role may require one state/rectangle, while its projected outgoing edge may
require another.  These cannot be combined in one literal cycle cover.

For each role \(r\), let \(Q_r\) be its exact state or rectangle choices.
A choice \(q\in Q_r\) fixes the role's head and its correlated tail menu.
For every legal literal compatibility between configurations, introduce an
arc variable \(x_e\), and introduce selector variables \(z_{rq}\).  The
exact one-copy correlated cycle-cover constraints are

\[
\begin{aligned}
 &z_{rq}\in\{0,1\},\qquad \sum_{q\in Q_r}z_{rq}=1,\\
 &\sum_{e\text{ out of }(r,q)}x_e=z_{rq},\qquad
  \sum_{e\text{ into }(r,q)}x_e=z_{rq},\\
 &x_e\in\{0,1\}.
\end{aligned}                                                 \tag{6.1}
\]

For a fixed selector \(z\), (6.1) reduces to an ordinary bipartite
perfect-matching/max-flow problem.  Equivalently, a correlated cycle cover
exists if and only if there is one global selector \(q_r\in Q_r\) for every
role such that the resulting literal compatibility graph satisfies Hall on
every head shore.  Taking the union of the graphs over different selectors
before testing Hall is not equivalent.

Explicitly, for a fixed selector put a capacity-one arc from a flow source
to every role-tail copy, all legal capacity-one tail-to-head compatibility
arcs, and a capacity-one arc from every role-head copy to the flow sink.
Give a compatibility arc cost one precisely when it is short-to-long and
cost zero otherwise.  If \(N=|{\cal L}|+|{\cal S}|=24,310\), then

\[
 \boxed{
 \begin{array}{c}
 \text{a cycle cover with at most 5,647 socket blocks exists}\\
 \Longleftrightarrow\\
 \text{for some one-choice-per-role selector, the integral flow has value
 }N\\
 \text{and its minimum cost is at most }5,647.
 \end{array}}                                                \tag{6.2}
\]

Integrality is automatic after the selector is frozen.  The minimum cost is
the exact \(b\) in (2.2); in a full one-copy matching its upper bound by
\(|{\cal S}|\) is automatic, but retaining the cost exposes the actual
number of long blocks and remains necessary when socket macros have other
capacities or costs.  The complete proof-safe gate is therefore:

1. one correlated rectangle/state choice per role;
2. a full integral matching/circulation satisfying the literal endpoint
   equalities;
3. minimum socket cost at most 5,647;
4. the threshold ledger (3.1)--(3.8); and
5. any required component-merging constraints beyond a cycle cover.

Passing a projected Hall test proves none of items 1, 4, or 5.  Failing a
complete projection, on the other hand, is already a valid obstruction for
the state class projected.
