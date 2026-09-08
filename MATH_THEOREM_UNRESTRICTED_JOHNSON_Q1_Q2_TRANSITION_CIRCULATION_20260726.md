# Unrestricted Johnson transitions at depths one and two

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, finite search, or
fixed packet atlas is used.

## 0. Outcome

Put

\[
 \Omega=[2m],\qquad \mathcal X=\binom{\Omega}{m},\qquad
 W=|\mathcal X|.
\]

There is an exact transition-circulation formulation of the unrestricted
Johnson \(2\)-factor problem. In this formulation the completely symmetric
fractional point has all of the following properties simultaneously:

* exact middle ownership;
* exact flow conservation, hence fractional cycle consistency;
* delay two at every transition;
* uniform lower and upper depth-one load
  \[
                  c_1={m+1\over m}={W\over\binom{2m}{m-1}};
  \]
* uniform lower and upper depth-two load
  \[
             c_2={(m+1)(m+2)\over m(m-1)}
                ={W\over\binom{2m}{m-2}}.
  \]

Consequently no fractional Hall inequality, or nonnegative weighted dual
inequality, separates the unrestricted catalogue already at \(q=1,2\).
The obstruction is integral and cyclic, not marginal.

There is also an exact positive local fact: two-sided injectivity of the
depth-one colours forces delay two automatically at every degree-two owner.
Thus the existing two-sided-rainbow Johnson forest has valid depth-two
traces at all its internal vertices.

On the other hand, simply adding depth-two collision conflicts to the
known depth-one four-graph nibble does not work. If its degree scale is
\(D=\Theta(m^2)\), then a fixed depth-two wedge has

\[
                         \Theta(m^4)=\Theta(D^2)
\]

resource-disjoint competing wedges with the same lower depth-two colour.
Hence the mixed conflict codegree satisfies

\[
                         \Delta_{4,2}=\Omega(D^2),
\]

whereas the conflict-free matching theorem requires a power saving
\(D^{2-\beta}\). This is a sharp obstruction to that direct black-box
extension, not an obstruction to the desired Johnson factor itself.

The minimum remaining depth-two theorem is therefore an **integral
quota-rainbow circulation theorem** for the transition digraph below.
It cannot be replaced either by marginal Hall or by treating the derived
depth-two colours as a sparse conflict system.

Sections 8--15 now give the general-depth extension.  For every
\(1\le H\le m\), safe histories form a balanced de Bruijn digraph with

\[
 |V|=W(m)_{H-1}^2,qquad |E|=W(m)_H^2,qquad
 d^+=d^-=(m-H+1)^2.
\]

It is strongly connected whenever \(3H\le m+2\), hence has one exact
Euler tour in that whole linear window, and its edges always split into
\((m-H+1)^2\) exact cycle covers.  The uniform circulation balances every
signed target through depth \(H\) exactly at its mean \(W/\binom{2m}{m-q}\).
The remaining integral obstruction is an owner-cycle transversal.  In the
growing range \(H=o(m^{1/3})\), total near-coverage of the signed target
layers is already sufficient for \(o(W)\) aggregate quota discrepancy.

## 1. Directed arcs and legal transitions

A directed Johnson arc is written

\[
 (X;a,b):\quad X\longrightarrow X-a+b,\qquad
 X\in\mathcal X,\quad a\in X,\quad b\notin X.
\tag{1.1}
\]

Let \(\mathcal A\) be the set of these arcs. Thus

\[
                            |\mathcal A|=Wm^2.
\tag{1.2}
\]

It is convenient to parametrize a consecutive pair of arcs by its middle
owner. A transition centred at \(Y\in\mathcal X\) is

\[
 \tau=(Y;x,y;c,d),\qquad
 x,c\in Y,\quad y,d\notin Y,\quad x\ne c,\quad y\ne d,
\tag{1.3}
\]

and means

\[
       Y-x+y\longrightarrow Y\longrightarrow Y-c+d.
\tag{1.4}
\]

The inequalities in (1.3) are exactly the delay-two condition. Indeed,
the first step adds \(x\) and deletes \(y\), viewed in forward chronology,
while the second deletes \(c\) and adds \(d\). Thus neither coordinate
changed by the first step is changed back by the second.

There are exactly

\[
                         K=m^2(m-1)^2
\tag{1.5}
\]

legal transitions centred at each \(Y\).

Regard the transitions as directed edges of a digraph \(\mathcal D_2\)
whose vertices are the directed arcs \(\mathcal A\): the tail of (1.3) is
the first arc in (1.4), and its head is the second arc.

## 2. Exact integral circulation equivalence

For \(z\in\{0,1\}^{\mathcal T}\), where \(\mathcal T\) is the transition
set, impose

\[
 \sum_{\tau:\operatorname{cent}(\tau)=Y}z_\tau=1
                         \qquad(Y\in\mathcal X),
\tag{2.1}
\]

and, for every directed Johnson arc \(\alpha\),

\[
 \sum_{\tau:\operatorname{head}(\tau)=\alpha}z_\tau
 =
 \sum_{\tau:\operatorname{tail}(\tau)=\alpha}z_\tau.
\tag{2.2}
\]

### Theorem 2.1 (transition-circulation normal form)

The integral solutions of (2.1)--(2.2) are in bijection with oriented
spanning \(2\)-factors of \(J(2m,m)\) having delay two at every vertex.
The directed cycles of the selected transitions are precisely the oriented
cycles of the \(2\)-factor.

#### Proof

An oriented delay-two \(2\)-factor has one predecessor and one successor at
every owner \(Y\), hence selects the unique transition formed by those two
arcs. Every used directed arc is outgoing at its tail owner and incoming at
its head owner, so (2.1)--(2.2) hold.

Conversely, (2.1) says that every owner selects one incoming and one outgoing
arc. For a fixed directed arc \(\alpha=(X,Y)\), at most one selected
transition can have tail \(\alpha\), since such a transition is centred at
\(Y\); at most one can have head \(\alpha\), since such a transition is
centred at \(X\). Thus (2.2) says that \(\alpha\) is used on both ends or on
neither end. Every owner consequently has one consistent predecessor and
one consistent successor. The selected arcs are disjoint directed cycles
covering \(\mathcal X\). Condition (1.3) gives delay two. The constructions
are inverse. \(\square\)

This is the promised Euler formulation: the hard integrality is not merely
choosing one local transition at every owner; the choices must form one
common circulation on the directed-arc states.

### Theorem 2.2 (exact Euler resolution of all legal transitions)

The full transition set \(\mathcal T\) admits an explicit partition into
\((m-1)^2\) directed cycle covers of the arc-state set \(\mathcal A\).
Every transition in every cover has delay two.

#### Proof

For each owner \(Y\), choose arbitrary bijections

\[
 \iota_Y:Y\longrightarrow\mathbb Z_m,\qquad
 \kappa_Y:\Omega\setminus Y\longrightarrow\mathbb Z_m.
\]

Fix \((r,s)\in(\mathbb Z_m\setminus\{0\})^2\). An incoming arc ending at
\(Y\) has the unique form

\[
                         Y-x+y\longrightarrow Y
\]

with \(x\in Y\), \(y\notin Y\). Send it to the outgoing arc

\[
                         Y\longrightarrow Y-c+d,
\]

where

\[
 \iota_Y(c)=\iota_Y(x)+r,\qquad
 \kappa_Y(d)=\kappa_Y(y)+s.
\tag{2.3}
\]

Because \(r,s\ne0\), this is a legal transition. For fixed \(Y,r,s\),
(2.3) is a bijection from the \(m^2\) incoming arcs at \(Y\) to its
\(m^2\) outgoing arcs. Taking all \(Y\) therefore defines a permutation
\(\Phi_{r,s}\) of \(\mathcal A\), and its cycles are a directed cycle cover
in \(\mathcal D_2\).

Conversely, a legal transition from local label \((x,y)\) to \((c,d)\)
has the unique nonzero shift pair

\[
 r=\iota_Y(c)-\iota_Y(x),\qquad
 s=\kappa_Y(d)-\kappa_Y(y).
\]

Hence the \((m-1)^2\) covers partition \(\mathcal T\). \(\square\)

In particular, the symmetric point (4.1) below has the exact Euler
decomposition

\[
 z={1\over m^2(m-1)^2}
       \sum_{r,s\ne0}\mathbf 1_{E(\Phi_{r,s})}.
\tag{2.4}
\]

This is not yet a convex decomposition into owner \(2\)-factors:
each \(\Phi_{r,s}\) uses \(m^2\), rather than one, transitions at every
owner. Extracting one owner visit while retaining whole \(\Phi_{r,s}\)
cycles is itself an exact cycle-transversal problem. Formula (2.4)
pinpoints the loss between Euler integrality on all arc states and the
required owner integrality.

## 3. Physical colours

For \(\tau=(Y;x,y;c,d)\), its incoming and outgoing depth-one colours are

\[
 \begin{array}{ll}
 L_1^{\rm in}(\tau)=Y-x,&U_1^{\rm in}(\tau)=Y+y,\\
 L_1^{\rm out}(\tau)=Y-c,&U_1^{\rm out}(\tau)=Y+d.
 \end{array}
\tag{3.1}
\]

Its depth-two colours are

\[
 L_2(\tau)=Y-\{x,c\},
 \qquad
 U_2(\tau)=Y\cup\{y,d\}.
\tag{3.2}
\]

These are literal intersections and unions of the three middle sets in
(1.4). In an integral circulation, a used depth-one arc occurs once as an
outgoing arc and once as an incoming arc. We count its depth-one colour on
the outgoing side only.

### Lemma 3.1 (two-sided depth-one rainbow forces delay two)

Let \(G\subseteq J(2m,m)\) have maximum degree two and have no repeated
lower or upper depth-one colour. At every degree-two vertex, the two
incident edges form a legal delay-two transition.

#### Proof

At \(Y\), write the incident edge labels as \((x,y)\) and \((c,d)\), with
\(x,c\in Y\) and \(y,d\notin Y\). If \(x=c\), both edges have lower colour
\(Y-x\). If \(y=d\), both have upper colour \(Y+y\). Either equality
contradicts the corresponding rainbow condition. Hence \(x\ne c\) and
\(y\ne d\), which is (1.3). \(\square\)

Thus the known \(W-o(W)\)-edge two-sided-rainbow linear forest already
produces \(W-o(W)\) valid depth-two transitions. What it does not control
is the distribution of the colours (3.2).

## 4. The exact symmetric fractional solution

Put

\[
                    z_\tau={1\over m^2(m-1)^2}
                    \qquad(\tau\in\mathcal T).
\tag{4.1}
\]

### Theorem 4.1 (simultaneous exact fractional balance at \(q=1,2\))

The vector (4.1) satisfies the fractional versions of (2.1)--(2.2). Its
load on every lower and upper depth-one target is

\[
                          c_1={m+1\over m},
\tag{4.2}
\]

and its load on every lower and upper depth-two target is

\[
                          c_2={(m+1)(m+2)\over m(m-1)}.
\tag{4.3}
\]

#### Proof

Equation (2.1) follows from (1.5). Fix a directed arc. Once it is the
incoming arc of a transition, the outgoing deleted coordinate has \(m-1\)
choices and the outgoing added coordinate has \(m-1\) choices. Thus its
outflow is

\[
                 (m-1)^2z_\tau={1\over m^2}.
\]

The same count backwards gives inflow \(1/m^2\), proving (2.2).

Fix \(S\in\binom{\Omega}{m-1}\). A directed Johnson arc of lower colour
\(S\) is obtained by choosing an ordered pair of distinct elements of
\(\Omega\setminus S\), so there are \(m(m+1)\) such arcs. Each can be the
outgoing arc of \((m-1)^2\) legal transitions. Hence its total load is

\[
 m(m+1)(m-1)^2z_\tau={m+1\over m}.
\]

The identical count inside a fixed \((m+1)\)-set proves the upper formula.

Now fix \(R\in\binom{\Omega}{m-2}\). A transition with \(L_2(\tau)=R\)
has a centre

\[
                          Y=R\cup\{x,c\},
\]

where the unordered pair \(\{x,c\}\) has
\(\binom{m+2}{2}\) choices. Its order has two choices, and the ordered
distinct pair \((y,d)\) outside \(Y\) has \(m(m-1)\) choices. The number of
such transitions is therefore

\[
 \binom{m+2}{2}\,2m(m-1)
   =(m+1)(m+2)m(m-1).
\]

Multiplication by (4.1) gives (4.3). Complementing every set proves the
upper formula. \(\square\)

Since

\[
 \binom{2m}{m-1}=W{m\over m+1},
 \qquad
 \binom{2m}{m-2}=W{m(m-1)\over(m+1)(m+2)},
\tag{4.4}
\]

the loads in (4.2)--(4.3) are exactly \(W/N_q\), not merely asymptotic.

### Corollary 4.2 (no fractional Hall cut at the first two depths)

Consider the LP consisting of nonnegative transition weights, exact centre
equations (2.1), flow conservation (2.2), and unit lower-cover constraints
for all four target layers \(m-2,m-1,m+1,m+2\). It is feasible. Therefore
no valid linear Hall dual can give positive deficit for the unrestricted
catalogue at \(q=1,2\).

More explicitly, for arbitrary nonnegative target weights \(w_t\), using
the outgoing-side convention for depth one, the symmetric circulation gives

\[
 \sum_{\tau}z_\tau
   \sum_{t\text{ claimed by }\tau}w_t
 =c_1\sum_{t:q=1}w_t+c_2\sum_{t:q=2}w_t
 \ge\sum_t w_t.
\tag{4.5}
\]

This conclusion concerns the exact unrestricted fractional polytope. It
does not assert that (4.1) is a convex combination of integral owner
\(2\)-factors satisfying the target constraints.

## 5. Exact first-moment laws for an integral balanced candidate

The next identities are useful tests for any proposed integral rounding.
Assume \(m\ge6\), so \(1<c_1,c_2<2\). Let an integral delay-two \(2\)-factor
cover every target at depths one and two with multiplicity at most two.
For each sign and depth, let \(\mathcal B_q^\pm\) be the family of targets
having multiplicity two. Then

\[
 |\mathcal B_q^\pm|=W-\binom{2m}{m-q}.
\tag{5.1}
\]

For a coordinate \(j\in\Omega\), let \(r_j\) be the number of directed
factor transitions which delete \(j\). Equivalently it is the number of
\(1\to0\) runs of the membership word of \(j\) around all factor cycles.
Then

\[
                         \sum_{j\in\Omega}r_j=W.
\tag{5.2}
\]

Put \(C=W/(m+1)\) and

\[
                         A={3mW\over(m+1)(m+2)}.
\tag{5.3}
\]

### Proposition 5.1 (bonus-family point degrees)

For every coordinate \(j\),

\[
 \begin{aligned}
  \deg_{\mathcal B_1^-}(j)&=C-r_j,
  &\deg_{\mathcal B_1^+}(j)&=r_j,\\
  \deg_{\mathcal B_2^-}(j)&=A-2r_j,
  &\deg_{\mathcal B_2^+}(j)&=C+2r_j.
 \end{aligned}
\tag{5.4}
\]

#### Proof

Across all middle owners, coordinate \(j\) is present \(W/2\) times. The
number of adjacent \(11\) pairs in its cyclic membership words is
\(W/2-r_j\); the number of depth-one windows containing \(j\) on the upper
side is \(W/2+r_j\). The point degrees of the complete target layers are

\[
 \binom{2m-1}{m-2}={W\over2}-C,
 \qquad
 \binom{2m-1}{m}={W\over2}.
\]

Subtracting these baseline contributions proves the first line of (5.4).

Delay two forbids membership runs of length one. On every nonconstant
factor cycle, a \(1\)-run of length \(s\) therefore contributes \(s-2\)
all-one triples. A cycle on which \(j\) is constantly present contributes
its full length and contributes zero to \(r_j\). Summing both kinds of
cycles gives \(W/2-2r_j\). The analogous statement for zero-runs shows
that the number of upper depth-two windows containing \(j\) is
\(W/2+2r_j\). Finally,

\[
 \binom{2m-1}{m-3}={W\over2}-A,
 \qquad
 \binom{2m-1}{m+1}={W\over2}-C.
\]

Subtracting the complete-layer baselines gives the second line. \(\square\)

In particular, depth one forces \(0\le r_j\le C\). The depth-two point
laws are compatible with this whole interval and yield no contradiction.
Thus the first moment is not the missing obstruction.

## 6. Why the direct conflict-system extension loses a full power

Recall the standard depth-one lifted hypergraph. Its resources are all
lower depth-one colours, all upper depth-one colours, and two clones
\(X^0,X^1\) of every middle owner. A lifted Johnson edge uses its two
colours and one clone at each endpoint. A matching projects to a
two-sided-rainbow graph of maximum degree two. Its degree scale is

\[
                              D=\Theta(m^2).
\tag{6.1}
\]

Two matched lifted edges using \(X^0,X^1\) form a wedge centred at \(X\).
By Lemma 3.1 the wedge is delay two and has the depth-two colours (3.2).
One might try to forbid two wedges with the same depth-two colour as a
four-edge conflict. The following exact lower bound shows why the usual
conflict-free nibble cannot do this.

### Proposition 6.1 (critical depth-two collision fibre)

For all \(m\ge6\), there is a fixed legal lifted wedge such that the number
of legal wedges, each resource-disjoint from the fixed wedge and having the
same lower depth-two colour, is at least

\[
                 \binom{m-2}{2}(m-4)(m-5)=\Theta(m^4).
\tag{6.2}
\]

Consequently the four-conflict system has

\[
                              \Delta_{4,2}=\Omega(D^2).
\tag{6.3}
\]

#### Proof

Fix pairwise distinct coordinates \(a,c,b,d\) and an \((m-2)\)-set \(R\)
disjoint from them. Let

\[
 X=R\cup\{a,c\},
\]

and take the two edges at \(X\) which delete \(a,c\) and add \(b,d\),
respectively. Choose complementary owner clones at \(X\). This is a legal
wedge of lower depth-two colour \(R\).

Let

\[
 K=\Omega\setminus(R\cup\{a,c,b,d\}),
 \qquad |K|=m-2.
\]

Choose \(\{u,v\}\in\binom K2\), put \(Y=R\cup\{u,v\}\), and choose an
ordered distinct pair

\[
                      (s,t)\in(K\setminus\{u,v\})^2.
\]

Use at \(Y\) the edges deleting \(u,v\) and adding \(s,t\), respectively,
with complementary clones at \(Y\). It is a legal wedge and its lower
depth-two colour is again \(R\).

All of its lower and upper depth-one colours differ from those of the fixed
wedge: the new non-\(R\) coordinates lie in \(K\), while every fixed upper
colour contains coordinates from \(\{a,c,b,d\}\). Its three middle owners
also avoid both \(a\) and \(c\), whereas the corresponding fixed owners
contain at least one of them. Thus the two lifted wedges are resource
disjoint. There are exactly the number of choices displayed in (6.2).

After fixing the two lifted hyperedges of the first wedge, each new wedge
completes them to a four-edge colour-collision conflict. This proves
(6.3). Conversely, for fixed \(R\), there are only
\(\binom{m+2}{2}\) possible centres, \(m(m-1)\) projected wedges at a
centre, and at most eight compatible clone lifts. Thus the full collision
fibre is \(O(m^4)\), so the order in (6.2) is sharp. \(\square\)

The standard conflict-free matching hypothesis at this mixed codegree is

\[
                         \Delta_{4,2}\le D^{2-\beta}
\]

for some fixed \(\beta>0\). Proposition 6.1 misses it by a polynomial
factor. Random thinning severe enough to restore the hypothesis would also
thin the target supply at the critical \(W\)-occurrence scale.

This is not a projective-plane or Hall counterexample: the symmetric
circulation of Section 4 proves that the collision fibre has abundant
fractional escape. It says that the escape must be coordinated through
the common Euler circulation, rather than imposed as independent forbidden
submatchings on the depth-one nibble.

## 7. The exact remaining \(q=1,2\) gate

Let \(N_q=\binom{2m}{m-q}\). The minimum finite statement which would
settle the first two depths is:

> Find an integral solution of (2.1)--(2.2) for which, for each
> \(q\in\{1,2\}\) and each sign, all but \(o(W)\) of the \(N_q\) physical
> targets have positive load, and the total excess above balanced floor
> quotas is \(o(W)\). Preferably the selected circulation has \(o(W/H)\)
> cycles after the growing-depth constraints are added.

Theorem 4.1 proves every linear marginal inequality for this statement.
Proposition 6.1 proves that the existing depth-one conflict-free nibble does
not round it. No integral quota-rainbow circulation, and no integral Hall
cut refuting one, is proved here. This is the sharp verified boundary at
\(H=2\); Sections 8--15 extend the exact fractional and Euler structure but
do not remove this integral gate.

## 8. General depth: safe paths and the de Bruijn state graph

The transition formalism extends exactly to every \(1\le H\le m\).  The
right states are safe Johnson histories, rather than individual directed
arcs.

Write a directed Johnson path as

\[
 P=(X_0,X_1,\ldots,X_\ell),
 \qquad
 X_{i+1}=X_i-a_i+b_i.
\tag{8.1}
\]

Call it **\(H\)-safe** if, in every interval of at most \(H\) consecutive
transitions, all change labels

\[
 a_i,b_i
\]

are pairwise distinct.  Let \(\mathcal P_j\) be the set of safe directed
paths having exactly \(j\) transitions.  Define the safe-path de Bruijn
digraph \(\mathcal D_H\) by

\[
 V(\mathcal D_H)=\mathcal P_{H-1},
 \qquad
 E(\mathcal D_H)=\mathcal P_H.
\tag{8.2}
\]

For

\[
 e=(X_0,\ldots,X_H)\in\mathcal P_H,
\]

its tail and head are respectively

\[
 (X_0,\ldots,X_{H-1}),
 \qquad
 (X_1,\ldots,X_H).
\tag{8.3}
\]

We label the edge by its terminal owner

\[
                         \operatorname{own}(e)=X_H.
\tag{8.4}
\]

At \(H=2\), this is a one-step cyclic reindexing of Sections 1--2: an
edge is a legal two-transition wedge and a vertex is a directed Johnson
arc.  The terminal-owner convention is more convenient at general depth
because every depth-\(q\) target is read from the last \(q\) transitions of
one edge.

### Lemma 8.1 (safety is exactly simultaneous correct rank)

For a Johnson path, the following are equivalent.

1. Every subpath of at most \(H\) transitions is safe.
2. For every such subpath
   \(X_s,X_{s+1},\ldots,X_{s+q}\),

   \[
   \left|\bigcap_{i=0}^qX_{s+i}\right|=m-q,
   \qquad
   \left|\bigcup_{i=0}^qX_{s+i}\right|=m+q.
   \tag{8.5}
   \]

#### Proof

In a safe \(q\)-path no inserted label can later be deleted and no deleted
label can later be reinserted.  Hence all deleted labels are distinct
members of the initial owner, all inserted labels are distinct members of
its complement, and

\[
 \bigcap_{i=0}^qX_{s+i}
 =X_s\setminus\{a_s,\ldots,a_{s+q-1}\},
\]

\[
 \bigcup_{i=0}^qX_{s+i}
 =X_s\cup\{b_s,\ldots,b_{s+q-1}\}.
\]

This proves (8.5).  Conversely, consider the first repeated change label in
a subpath.  Its first and second changes have opposite directions.  A
delete--insert return makes the upper union miss one of its required new
labels; an insert--delete return makes the lower intersection miss one of
its required distinct deletions.  Thus one equality in (8.5) fails on the
interval between the two changes.  \(\square\)

Use the falling factorial

\[
                         (m)_j=m(m-1)\cdots(m-j+1).
\]

### Theorem 8.2 (exact size and regularity)

Put

\[
                         r=m-H+1.
\tag{8.6}
\]

Then

\[
 |V(\mathcal D_H)|=W(m)_{H-1}^2,
 \qquad
 |E(\mathcal D_H)|=W(m)_H^2,
\tag{8.7}
\]

and every vertex has indegree and outdegree exactly

\[
                         d_H=r^2=(m-H+1)^2.
\tag{8.8}
\]

#### Proof

From a fixed initial owner, a safe \(j\)-path chooses an ordered
\(j\)-tuple of distinct original elements to delete and an ordered
\(j\)-tuple of distinct complementary elements to insert.  This gives
\((m)_j^2\) paths and proves (8.7).

Now fix a state ending at \(X\).  Its last \(H-1\) transitions have inserted
\(H-1\) labels currently in \(X\) and deleted \(H-1\) labels currently
outside \(X\).  They are precisely the locked labels.  A safe extension
may delete any of the remaining \(r\) elements of \(X\), and may insert any
of the remaining \(r\) elements outside \(X\).  This gives \(r^2\)
extensions.  Reversing every history proves the identical indegree.
\(\square\)

The queue update behind this proof is explicit.  If the recent deleted and
inserted queues, from oldest to newest, are

\[
 (p_1,\ldots,p_{H-1}),
 \qquad
 (q_1,\ldots,q_{H-1}),
\]

and the next free swap is \(c\mapsto d\), then the new queues are

\[
 (p_2,\ldots,p_{H-1},c),
 \qquad
 (q_2,\ldots,q_{H-1},d).
\tag{8.9}
\]

Thus the only memory is a pair of length-\((H-1)\) cooldown queues.

## 9. Strong connectivity in a linear window

Regularity alone does not imply that \(\mathcal D_H\) is connected.  A
buffer flush supplies a direct proof in a nontrivial linear range.

### Lemma 9.1 (safe flush)

Let a safe history end at \(X\).  Suppose that

\[
 E\subseteq X,\qquad F\subseteq\Omega\setminus X,
 \qquad |E|=|F|=H,
\]

and all labels in \(E\cup F\) are free.  Order them as

\[
 E=(e_1,\ldots,e_H),\qquad F=(f_1,\ldots,f_H).
\]

Then the \(2H\)-transition word

\[
 e_1\mapsto f_1,\ldots,e_H\mapsto f_H,
 f_1\mapsto e_1,\ldots,f_H\mapsto e_H
\tag{9.1}
\]

is safe, returns to \(X\), and leaves a final history whose changed labels
all lie in \(E\cup F\).

#### Proof

The first block uses only free labels and has no repetition.  Every label is
used again exactly \(H\) transitions after its first use.  No interval of
\(H\) transitions contains both occurrences.  The second block reverses
the first, and the final \(H-1\) transitions use only \(E\cup F\).
\(\square\)

### Theorem 9.2 (strong connectivity)

If

\[
                         3H\le m+2,
\tag{9.2}
\]

then \(\mathcal D_H\) is strongly connected.

#### Proof

Let \(P\) and \(Q\) be two states.  Write \(X\) for the terminal owner of
\(P\), and \(Y\) for the initial owner of \(Q\).  In the history \(P\),
let

\[
 I_P\subseteq X,qquad O_P\subseteq\Omega\setminus X
\]

be respectively the \(H-1\) recently inserted and recently deleted labels.
They are locked.

Put \(r=m-H+1\).  Choose

\[
 Y_*\subseteq Y\setminus O_P,qquad |Y_*|=r.
\]

This is possible because \(|O_P|=H-1\).  Choose an \(m\)-set \(Z\)
containing \(I_P\cup Y_*\) and avoiding \(O_P\).  Since

\[
 |I_P|+|Y_*|=(H-1)+(m-H+1)=m,
\]

overlap only creates extra room, and such a \(Z\) exists.  In particular,

\[
 |Z\cap Y|=|Z^c\cap Y^c|\ge r.
\tag{9.3}
\]

Take a direct Johnson path from \(X\) to \(Z\), changing every coordinate
of \(X\triangle Z\) once.  It never changes a label in
\(I_P\cup O_P\), because \(Z\) agrees with \(X\) on those labels.  Hence
it follows \(P\) safely.

At \(Z\), at most \(H-1\) members of \(Z\cap Y\) and at most \(H-1\)
members of \(Z^c\cap Y^c\) are locked.  By (9.2)--(9.3), each agreement
class has at least

\[
 r-(H-1)=m-2H+2\ge H
\]

free labels.  Choose free

\[
 E\subseteq Z\cap Y,qquad F\subseteq Z^c\cap Y^c,qquad
 |E|=|F|=H,
\]

and perform the flush (9.1).  Now take the direct path from \(Z\) to
\(Y\).  Its change labels lie in \(Z\triangle Y\), disjoint from
\(E\cup F\), so this concatenation is safe.

It remains to install the prescribed state \(Q\).  Let

\[
 D_Q\subseteq Y,qquad A_Q\subseteq\Omega\setminus Y
\]

be the deleted and inserted labels in the \(H-1\) transitions of \(Q\).
At the current history ending at \(Y\), choose \(H\) free inside labels
avoiding \(D_Q\), and \(H\) free outside labels avoiding \(A_Q\).  There
are at least

\[
 m-2(H-1)\ge H
\]

choices on each side by (9.2).  Flush on these two sets.  Its final history
is disjoint from all change labels of \(Q\), so appending the prescribed
\(H-1\) transitions of \(Q\) is safe.  The final de Bruijn state is exactly
\(Q\).  Thus every ordered pair of states is joined by a directed path.
\(\square\)

The connectivity range is not merely fixed depth: it contains every
\(H=o(m)\), every Gaussian \(H=O(\sqrt m)\), and indeed all
\(H\le(m+2)/3\).  It cannot be extrapolated blindly to \(H=m\).  There
\(d_H=1\); the unique continuation changes each label again exactly \(m\)
steps later, and the state graph splits into deterministic \(2m\)-cycles.

## 10. Exact Euler and cycle-cover resolutions

### Theorem 10.1 (Euler resolution of the safe catalogue)

For every \(1\le H\le m\), every weak component of \(\mathcal D_H\) has an
Euler circuit containing each of its safe \(H\)-paths exactly once.  If
\(3H\le m+2\), the whole digraph has one Euler circuit.

Moreover, for every \(H\), the full edge set admits an exact partition into

\[
                         d_H=(m-H+1)^2
\tag{10.1}
\]

directed cycle covers of the state set \(\mathcal P_{H-1}\).

#### Proof

By Theorem 8.2 every vertex is balanced.  In a finite balanced digraph,
each weak component is a union of strongly connected Eulerian components;
equivalently, the condensation has no nontrivial source or sink, so the
weak component is strongly connected after isolated zero-degree vertices
are discarded.  Hence every nonempty weak component is Eulerian.  Theorem
9.2 gives one component in the stated range.

For the second assertion, take a left and a right copy of the state set and
replace every directed edge by the corresponding left--right bipartite
edge.  The resulting bipartite graph is \(d_H\)-regular.  Hall's theorem
gives a perfect matching; deleting it preserves regularity.  Induction
partitions the graph into \(d_H\) perfect matchings.  Each matching is a
permutation of the state set, hence a directed cycle cover of
\(\mathcal D_H\).  \(\square\)

The first paragraph uses the standard balanced-component fact, whose short
proof is worth recording.  In the acyclic condensation, a source component
has no incoming edge.  Summed indegree equals summed outdegree on that
component, so it has no outgoing edge either.  Remove it and repeat.

Neither Euler resolution is yet an owner factor.  The full Euler circuit
contains

\[
                         K_H=(m)_H^2
\tag{10.2}
\]

edges labelled by each owner.  Each cycle cover in Theorem 10.1 contains

\[
                         (m)_{H-1}^2
\tag{10.3}
\]

state visits ending at each owner.  The desired coefficient-one object must
retain exactly one.  This is the precise cycle-transversal loss.

## 11. Integral circulation equivalence at general depth

For \(z\in\{0,1\}^{E(\mathcal D_H)}\), impose the owner equations

\[
 \sum_{e:\operatorname{own}(e)=Y}z_e=1
                         \qquad(Y\in\mathcal X),
\tag{11.1}
\]

and state-flow conservation

\[
 \sum_{e:\operatorname{head}(e)=v}z_e
 =
 \sum_{e:\operatorname{tail}(e)=v}z_e
                         \qquad(v\in\mathcal P_{H-1}).
\tag{11.2}
\]

### Theorem 11.1 (safe-history circulation normal form)

The integral solutions of (11.1)--(11.2) are in bijection with oriented
spanning \(2\)-factors of \(J(2m,m)\) for which every cyclic subpath of at
most \(H\) transitions is safe.  Consequently every lower and upper target
window through depth \(H\) has the correct rank.

#### Proof

All incoming edges of a fixed state \(v\) have terminal owner equal to the
terminal owner of \(v\).  Hence (11.1) permits at most one selected incoming
edge at \(v\), and (11.2) permits at most one selected outgoing edge.  The
selected de Bruijn edges are therefore vertex-disjoint directed cycles.
Their overlap reconstructs cyclic Johnson owner trajectories.  Equation
(11.1) says that every middle owner occurs exactly once as a terminal owner,
so those trajectories form a spanning \(2\)-factor.  Every length-\(H\)
history is safe, and Lemma 8.1 gives all asserted ranks.

Conversely, take at each owner of an \(H\)-safe oriented factor the
length-\(H\) history ending there.  Consecutive histories overlap in a
state of \(\mathcal D_H\), giving (11.2), and every owner contributes once,
giving (11.1).  The constructions are inverse.  \(\square\)

This theorem should be compared with Theorem 2.1.  The hard condition is
still not local safety: it is selecting a common integral circulation which
is simultaneously a transversal of all owner classes.

## 12. Simultaneous exact fractional balance at every depth

For an edge

\[
 e=(X_0,\ldots,X_H)
\]

and \(1\le q\le H\), define its terminal lower and upper targets by

\[
 L_q(e)=\bigcap_{i=H-q}^{H}X_i,
 \qquad
 U_q(e)=\bigcup_{i=H-q}^{H}X_i.
\tag{12.1}
\]

Lemma 8.1 gives their ranks \(m-q\) and \(m+q\).

Put

\[
                         z_e^*={1\over K_H}={1\over(m)_H^2}.
\tag{12.2}
\]

### Theorem 12.1 (all-depth symmetric circulation)

The vector \(z^*\) satisfies the fractional forms of (11.1)--(11.2).
For every \(1\le q\le H\), every lower rank-\((m-q)\) target and every
upper rank-\((m+q)\) target has exactly the same load

\[
 \boxed{
 c_q={W\over\binom{2m}{m-q}}
     ={(m+q)!(m-q)!\over(m!)^2}
     =\prod_{i=1}^q{m+i\over m-q+i}.}
\tag{12.3}
\]

#### Proof

There are \((m)_H^2=K_H\) safe backward \(H\)-histories ending at each
owner, so (11.1) holds.  Every state has \(d_H\) incoming and \(d_H\)
outgoing edges of the same weight, giving (11.2).

The symmetric group on \(\Omega\) acts transitively on each target layer,
preserves safety, and preserves \(z^*\).  Hence the load is constant on that
layer.  The total weighted edge mass is

\[
 |E(\mathcal D_H)|z_e^*=WK_H/K_H=W.
\]

Division by the layer size gives \(c_q\).  Complementation proves the same
upper load; the two layer sizes are equal.  \(\square\)

If \(F_1,\ldots,F_{d_H}\) are the cycle covers in Theorem 10.1, then the
general exact Euler decomposition of the symmetric point is

\[
 z^*={1\over K_H}\sum_{j=1}^{d_H}\mathbf1_{E(F_j)}.
\tag{12.4}
\]

Thus no nonnegative weighted target inequality separates the unrestricted
safe catalogue at any collection of depths \(q\le H\).  As at \(H=2\),
(12.4) is not a convex decomposition into owner \(2\)-factors: its total
coefficient is \(d_H/K_H=1/(m)_{H-1}^2\), and every cover overuses every
owner by the reciprocal factor.

## 13. The exact cycle-transversal and quota-rounding gates

For a directed cycle \(C\) of \(\mathcal D_H\), define

\[
 a_Y(C)=\#\{e\in C:\operatorname{own}(e)=Y\},
\tag{13.1}
\]

and, for every signed target \(t=(q,\varepsilon,S)\), define

\[
 a_t(C)=\#\{e\in C:T_q^\varepsilon(e)=S\},
\tag{13.2}
\]

where \(T_q^-=L_q\) and \(T_q^+=U_q\).

### Theorem 13.1 (cycle-transversal equivalence)

An \(H\)-safe oriented spanning \(2\)-factor is equivalent to a collection
\(\mathscr C\) of directed cycles of \(\mathcal D_H\) satisfying

\[
                         \sum_{C\in\mathscr C}a_Y(C)=1
                         \qquad(Y\in\mathcal X).
\tag{13.3}
\]

Its signed target loads are exactly

\[
                         \mu_t=\sum_{C\in\mathscr C}a_t(C).
\tag{13.4}
\]

#### Proof

Decompose the selected circulation in Theorem 11.1 into its directed
cycles.  This gives (13.3)--(13.4).  Conversely, (13.3) prevents two
selected cycles from sharing a state: a shared state would give two incoming
edges with the same terminal owner.  Hence their union is a \(0\)-\(1\)
circulation satisfying (11.1), and Theorem 11.1 applies.  \(\square\)

This is an exact hypergraph transversal problem on the owner-incidence
vectors of safe de Bruijn cycles.  Strong connectivity and the Euler tour
do not imply (13.3).

There is an equally precise polyhedral sufficient condition.  Let \(B_H\)
be the state--edge incidence matrix, \(C_H\) the owner--edge matrix, and
\(Q_H\) the signed-target--edge matrix.  Put

\[
 d_q=\lfloor c_q\rfloor.
\]

Consider

\[
 \begin{array}{rcl}
 B_Hz&=&0,\\
 C_Hz&=&\mathbf1,\\
 d_q\le (Q_Hz)_t&\le&d_q+1
       \quad(t\text{ of depth }q),\\
 0\le z&\le&1.
 \end{array}
\tag{13.5}
\]

The symmetric point (12.2) is feasible in (13.5).  Therefore either of the
following would give an exact simultaneous floor/ceiling factor through
depth \(H\):

1. the system (13.5) is box-TDI for these integral right-hand sides;
2. the augmented matrix \((B_H,C_H,Q_H)\) has the corresponding integer
   decomposition/rounding property at \(z^*\).

These are sufficient conditions, not assertions.  The ordinary incidence
matrix \(B_H\) is totally unimodular, but appending the owner and nested
target rows is exactly the unresolved operation.  Theorem 12.1 proves
fractional feasibility; it does not prove either rounding property.

For prescribed rather than mobile high-quota targets, replace the two
inequalities in (13.5) by

\[
                         Q_Hz=\beta,
\tag{13.6}
\]

where each depth-\(q\) coordinate of \(\beta\) is \(d_q\) or \(d_q+1\)
and its total on each fixed signed depth layer is \(W\).  In cycle language,
the exact condition is

\[
 \sum_Ca_Y(C)x_C=1,qquad
 \sum_Ca_t(C)x_C=\beta_t,qquad
 x_C\in\{0,1\}.
\tag{13.7}
\]

This isolates the common signed-quota obstruction without pretending that
rankwise fractional Hall solutions select the same cycles.

## 14. A nontrivial growing-depth reduction

Although integral rounding remains open already at \(H=2\), the quota
arithmetic simplifies in a genuine growing window.

Uniformly for \(q\le H=o(\sqrt m)\), (12.3) gives

\[
 \log c_q={q^2\over m}+O\!\left({q^3\over m^2}\right),
\tag{14.1}
\]

so \(d_q=1\) and

\[
 W-\binom{2m}{m-q}
 =\left({q^2\over m}
   +O\!\left({q^3\over m^2}+{q^4\over m^2}\right)\right)W.
\tag{14.2}
\]

Summing both signs and all depths gives

\[
 2\sum_{q=1}^H
 \left(W-\binom{2m}{m-q}\right)
 =\left({2\over3}+o(1)\right){H^3\over m}W.
\tag{14.3}
\]

Consequently, if

\[
                         H=o(m^{1/3}),
\tag{14.4}
\]

the total number of unavoidable high-quota units over all signed layers is
\(o(W)\).

### Corollary 14.1 (near-cover is enough below the cubic threshold)

Let \(H=o(m^{1/3})\), and suppose an owner-transversal collection of safe
de Bruijn cycles satisfies

\[
 \sum_{q=1}^H\sum_{\varepsilon\in\{-,+\}}
 \#\{S:\mu_q^\varepsilon(S)=0\}=o(W).
\tag{14.5}
\]

Then its total \(L^1\) discrepancy from some simultaneous family of
balanced floor/ceiling signed quotas is \(o(W)\).

#### Proof

At each signed depth there are exactly \(W\) occurrences, because the
factor has one safe based window ending at each owner.  If \(h_q^\varepsilon\)
targets are missing, the excess above load one is exactly

\[
 W-\binom{2m}{m-q}+h_q^\varepsilon.
\tag{14.6}
\]

Choose the high-quota locations to minimize distance from the actual load
vector.  Moving one unit of surplus or filling one hole costs at most two in
\(L^1\).  Hence the total discrepancy is at most twice the sum of (14.6)
and the holes.  Equations (14.3)--(14.5) make this \(o(W)\).  \(\square\)

Thus the first genuinely growing integral target can be stated without
individual upper quotas:

> For some \(H\to\infty\) with \(H=o(m^{1/3})\), find an owner-transversal
> collection of safe de Bruijn cycles whose total number of lower and upper
> target holes through depth \(H\) is \(o(W)\).

The safe catalogue itself is regular, strongly connected, Eulerian, and
fractionally exact throughout this window.  The only missing theorem is the
integral owner-cycle transversal with near-cover.  At Gaussian depth the
sparse-bonus simplification (14.3) is no longer available, and the full
box-quota rounding condition (13.5), or an equivalent signed discrepancy
theorem, is genuinely necessary.

## 15. Updated boundary

The general-depth extension proves:

1. exact safe-history/de Bruijn normal form for every \(H\le m\);
2. degree \((m-H+1)^2\) and exact state/edge counts;
3. strong connectivity for \(3H\le m+2\);
4. one Euler circuit in that range and \((m-H+1)^2\) exact cycle covers at
   every depth;
5. simultaneous uniform fractional target loads \(c_q\) for every
   \(q\le H\);
6. an exact owner-cycle-transversal formulation and a box-TDI integral
   rounding gate;
7. the growing reduction \(H=o(m^{1/3})\), where total near-cover alone
   implies \(o(W)\) signed quota discrepancy.

It does **not** produce the owner transversal.  Eulerizing every safe path
uses each owner \((m)_H^2\) times, and one cycle cover uses each owner
\((m)_{H-1}^2\) times.  Removing this multiplicity while retaining whole
cycles and common signed quotas is the exact unresolved integral theorem.
