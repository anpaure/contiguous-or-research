# Partial-annulus SCD paths: the exact two-matching seam gate and coarse-power obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and let

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
 \qquad 0<a<b.
\]

This note audits the layerwise path-cover route to the corrected partial
annulus problem.  It proves four exact facts.

1. At one adjacent pair of lower ranks, an SCD provider matching always
   has a second, disjoint inclusion matching.  The two matchings give a
   directed partial permutation whose arcs expose every target of the
   next lower rank exactly once.

2. The unmatched outgoing and incoming shores both have the exact size

   \[
    d_q=N_q-N_{q+1}
       ={2q+1\over m+q+1}N_q.
   \]

   Completion to a target-layer permutation is equivalent to one ordinary
   Johnson-graph Hall system between these two shores.  The resulting
   seam arcs are exactly the unavoidable duplicate occurrences at the
   next depth.

3. Before those seam arcs are inserted, the number of directed path
   components, with isolated vertices counted as paths, is exactly
   \(d_q\), apart from any directed-cycle components.  At the first
   annular step,

   \[
    d_{q_0}
      =(2ae^{-a^2}+o(1)){W\over\sqrt m}
      =(2ab e^{-a^2}+o(1)){W\over H}.
   \]

   Thus an active-edge-only SCD path forest is at the critical
   \(\Theta(W/H)\) scale, not at \(o(W/H)\).  The corrected slack is
   precisely what can escape this cut: every one of the \(d_{q_0}\)
   nonprovider phases must be used as a seam source, and every residual
   incoming port must be used as a seam target.

4. A permutation cycle cover is still not a family of physical
   cyclic-order packets.  Its cycles must all have length \(2m\), and on
   each cycle the deleted-coordinate word must be a permutation of the
   ground set with every inserted coordinate occurring exactly
   \(m-q\) positions later.  Moreover, independent solutions at different
   depths need not be projections of one common history.

There is also an exact obstruction for a proposed SCD flag assignment.
For a complement-closed owner set and a lower depth-\(q\) target map
\(\phi_q\), the two antipodal targets reconstruct a middle-owner map

\[
 P_q(X)=\phi_q(X)\cup\bigl(X^c\setminus\phi_q(X^c)\bigr).
\]

In every physical packet with successor \(\sigma\), necessarily

\[
 \boxed{P_q=\sigma^q.}
\]

This gives exact cycle-length, complement, and root constraints stated
below.  It is a real test on a fixed SCD, but not a universal no-go: one
exception per eventual \(2m\)-packet costs only \(O(W/m)=o(W)\).

The note therefore neither proves nor disproves the corrected partial
annulus theorem.  It identifies its first exact positive Hall layer and
the first two genuinely nonlayerwise gates: the residual seam factor and
the common physical history.

## 1. Floor and overload ledger

A union of length-\(n\) packets contains a multiple of \(n\) middle
occurrences.  Thus the phrase "exactly \(N_{q_0}\) occurrences partitioned
into \(2m\)-cycles" is literally possible only when

\[
                         n\mid N_{q_0}.
\]

The floor-corrected packet mass is

\[
 K=\left\lfloor{N_{q_0}\over n}\right\rfloor,
 \qquad T=nK,
 \qquad \rho=N_{q_0}-T,
 \qquad 0\le\rho<n.                              \tag{1.1}
\]

Omitting these \(\rho\) SCD providers can remove at most \(\rho\)
designated lower and \(\rho\) designated upper targets at every depth.
Thus its complete signed annular repair bill is at most

\[
                 2\rho(H-q_0+1)=O(m^{3/2})=o(W). \tag{1.2}
\]

Equation (1.2) corrects the arithmetic; it does not construct the packet
factor on the remaining providers.

For any family of \(K\) packets, let \(a_q(R)\) be the occurrence load of
a rank-\((m-q)\) target \(R\), let

\[
 h_q=N_q-|\{R:a_q(R)>0\}|,
\]

and let

\[
 o_q=\sum_R(a_q(R)-1)_+.
\]

Every packet has exactly \(n\) distinct targets at each proper depth, so
\(\sum_Ra_q(R)=T\).  Hence the exact identity is

\[
                 \boxed{o_q-h_q=T-N_q.}           \tag{1.3}
\]

At the base depth,

\[
                         h_{q_0}=\rho+o_{q_0}.     \tag{1.4}
\]

For every \(q>q_0\), and all sufficiently large \(m\), one has
\(T>N_q\), and therefore

\[
                         h_q=o_q-(T-N_q).          \tag{1.5}
\]

Thus the unavoidable duplicates \(T-N_q\) are not defects.  The desired
aggregate condition \(\sum h_q=o(W)\) says that overload must exceed its
rankwise floor baseline by only \(o(W)\) over the whole annulus.

Uniformly for \(q=x\sqrt m+O(1)\), with bounded \(x\),

\[
 {N_q\over W}=e^{-x^2+o(1)}.                     \tag{1.6}
\]

Consequently the unavoidable positive duplicate mass satisfies

\[
 \sum_{q=q_0+1}^{H}(T-N_q)
  =W\sqrt m\left(
       \int_a^b(e^{-a^2}-e^{-x^2})\,dx+o(1)
     \right).                                    \tag{1.7}
\]

It is \(\Theta(W\sqrt m)\).  A successful construction must retain that
large baseline while making the excess in (1.5) only \(o(W)\).

## 2. One adjacent pair of ranks

Fix \(q\ge1\), put

\[
 k=m-q,
 \qquad
 V=\binom{[n]}k,
 \qquad
 U=\binom{[n]}{k-1}.
\]

Thus \(|V|=N_q\) and \(|U|=N_{q+1}\).

Fix a full SCD \(\mathcal D\) of \(B_n\).  Every \(u\in U\) lies on a
unique chain, and that chain has a unique member of rank \(k\).  Denote it
by

\[
                         p(u)\in V.               \tag{2.1}
\]

Then \(u\subset p(u)\), and \(p:U\to V\) is injective.

### Theorem 2.1 (second inclusion matching)

There is an injection \(s:U\to V\) satisfying

\[
                         u\subset s(u),
 \qquad                  s(u)\ne p(u)             \tag{2.2}
\]

for every \(u\in U\).

#### Proof

Make a bipartite graph from \(U\) to \(V\), joining \(u\) to every
rank-\(k\) superset except \(p(u)\).  Every left vertex has degree

\[
 (n-k+1)-1=n-k=m+q,                               \tag{2.3}
\]

whereas a right vertex is incident with at most

\[
                         k=m-q                    \tag{2.4}
\]

allowed edges.  Therefore, for every \(A\subseteq U\),

\[
 (m+q)|A|
   \le (m-q)|N(A)|.
\]

Since \(q\ge1\), this gives \(|N(A)|\ge|A|\), in fact strict inequality
for nonempty \(A\).  Hall's theorem supplies the injection \(s\).
\(\square\)

For each \(u\), the two distinct rank-\(k\) sets \(p(u),s(u)\) have
intersection exactly \(u\).  Direct the corresponding Johnson edge as

\[
                         p(u)\longrightarrow s(u).             \tag{2.5}
\]

Because both \(p\) and \(s\) are injective, these active arcs have
outdegree and indegree at most one.  Every rank-\((k-1)\) target occurs as
an edge intersection exactly once.

Define the residual shores

\[
 A_{\rm out}=V\setminus p(U),
 \qquad
 B_{\rm in}=V\setminus s(U).                    \tag{2.6}
\]

They have the common exact size

\[
 \boxed{
 |A_{\rm out}|=|B_{\rm in}|=d_q=N_q-N_{q+1}.}    \tag{2.7}
\]

Using

\[
 {N_{q+1}\over N_q}={m-q\over m+q+1},            \tag{2.8}
\]

this is

\[
 \boxed{
 d_q={2q+1\over m+q+1}N_q.}                      \tag{2.9}
\]

### Corollary 2.2 (the critical active-path count)

The directed graph (2.5) is a disjoint union of directed paths, isolated
vertices, and directed cycles.  The number of path components, counting
isolated vertices and not counting directed cycles, is exactly

\[
                         d_q=N_q-N_{q+1}.          \tag{2.10}
\]

#### Proof

In any graph of maximum indegree and outdegree one, a path component with
\(v\) vertices has \(v-1\) edges and a cycle component has \(v\) edges.
The graph (2.5) has \(N_q\) vertices and \(N_{q+1}\) edges.  Subtracting
edges from vertices therefore counts precisely the path components.
\(\square\)

At \(q=q_0\), equations (1.6) and (2.9) give

\[
 d_{q_0}
 =(2ae^{-a^2}+o(1)){W\over\sqrt m}
 =(2ab e^{-a^2}+o(1)){W\over H}.                \tag{2.11}
\]

Thus opening these active paths separately has a \(\Theta(W)\) collar
toll.  The active matching is useful only if its residual shores can be
fused without opening the paths.

## 3. The exact residual-seam Hall theorem

Let \(J(n,k)\) be the Johnson graph on \(V\).  Form the bipartite residual
seam graph \(\mathcal J_{p,s}\) with left shore \(A_{\rm out}\), right
shore \(B_{\rm in}\), and an edge

\[
 x_Ly_R
 \quad\Longleftrightarrow\quad
 |x\cap y|=k-1.                                  \tag{3.1}
\]

### Theorem 3.1 (two-layer SCD seam completion)

The active arcs (2.5) extend to a permutation \(\sigma\) of \(V\) all of
whose arcs are Johnson edges if and only if

\[
 \boxed{
 |N_{\mathcal J_{p,s}}(A)|\ge|A|
 \quad\text{for every }A\subseteq A_{\rm out}.} \tag{3.2}
\]

When (3.2) holds, every rank-\((k-1)\) target occurs at least once among
the intersections \(x\cap\sigma x\), and the total overload above one is
exactly \(d_q\).

#### Proof

Condition (3.2) is Hall's criterion for a bijection

\[
                         \eta:A_{\rm out}\to B_{\rm in}       \tag{3.3}
\]

along Johnson edges.  Define

\[
 \sigma(p(u))=s(u)\quad(u\in U),
 \qquad
 \sigma(x)=\eta(x)\quad(x\in A_{\rm out}).       \tag{3.4}
\]

The sources in (3.4) partition \(V\), and so do the targets
\(s(U)\dot\cup B_{\rm in}\).  Thus \(\sigma\) is a permutation.  The
active edge indexed by \(u\) has intersection \(u\), so the active arcs
already expose every member of \(U\) exactly once.  The \(d_q\) seam arcs
add \(d_q\) further occurrences and no new target labels, because all
rank-\((k-1)\) labels have already appeared.  Hence their aggregate
overload is exactly \(d_q\).

Conversely, any completion of the prescribed active arcs must send every
unused source in \(A_{\rm out}\) bijectively to an unused target in
\(B_{\rm in}\).  If every added arc is a Johnson edge, this bijection is a
perfect matching of \(\mathcal J_{p,s}\), and Hall gives (3.2).
\(\square\)

Theorem 2.1 is unconditional; Theorem 3.1 is not.  Cardinality equality
of the residual shores does not imply (3.2).  The second matching \(s\)
must be chosen in correlation with the SCD parent matching so that every
residual Johnson cut expands.

There is no seam surplus at this layer.  The \(d_q\) unused outgoing
phases and \(d_q\) unused incoming ports are exactly the \(d_q\) baseline
duplicates forced by \(N_q-N_{q+1}\).  Losing a positive fraction of them
to unmatched shores recreates a \(\Theta(W/H)\) path count at the first
annular step.

## 4. The cycle-type and physical-residence gates

A perfect seam matching makes a permutation, but the corrected packet
problem asks for ordinary cyclic-order packets of length \(n\).

### Proposition 4.1 (cycle-type gate)

A permutation of a target occurrence set of size \(T\) can be partitioned
into length-\(n\) cycles only if

\[
                         n\mid T,                              \tag{4.1}
\]

and its cycle type is exactly

\[
                         (n)^{T/n}.                            \tag{4.2}
\]

In particular, the number of cycles must be \(T/n\); that scalar count is
not sufficient unless every cycle has length \(n\).

Even (4.2) is not sufficient for physical cyclic intervals.

### Proposition 4.2 (exact interval-cycle characterization)

Let

\[
 X_0,X_1,\ldots,X_{n-1},X_n=X_0
\]

be a directed length-\(n\) Johnson cycle of rank-\(k\) sets, and write

\[
 X_{i+1}=X_i-\{x_i\}+\{y_i\}.                    \tag{4.3}
\]

The cycle is the rank-\(k\) interval cycle of one directed cyclic order
of \([n]\) if and only if

1. \(x_0,x_1,\ldots,x_{n-1}\) are all distinct; and
2. with indices modulo \(n\),

   \[
                            y_i=x_{i+k}.           \tag{4.4}
   \]

In that case the cyclic coordinate order is

\[
                         (x_0,x_1,\ldots,x_{n-1}),              \tag{4.5}
\]

and

\[
                         X_i=\{x_i,\ldots,x_{i+k-1}\}.         \tag{4.6}
\]

#### Proof

For a cyclic interval cycle, shifting the length-\(k\) interval deletes
its first coordinate and inserts the coordinate \(k\) positions later,
so the conditions are necessary.

Conversely, every coordinate is deleted once and, by (4.4), inserted
once.  The unique insertion of \(x_j\) occurs at transition \(j-k\), and
its unique deletion occurs at transition \(j\).  Therefore \(x_j\) is
present precisely in the \(k\) cyclic states with starts
\(j-k+1,\ldots,j\).  Equivalently, the coordinates present in state
\(X_i\) are exactly \(x_i,\ldots,x_{i+k-1}\), proving (4.6).
\(\square\)

The residence condition (4.4) is independent of the Johnson seam Hall
cuts.  A generic length-\(n\) Johnson cycle may delete every coordinate
once but give the coordinates unequal residence lengths; it is then not a
cyclic-order packet.

For \(k=m-q_0\), a physical target interval cycle reconstructs its middle
owner cycle by

\[
                         M_i=\{x_i,\ldots,x_{i+m-1}\}.          \tag{4.7}
\]

Those owners are distinct and antipodal inside one packet.  Distinct
target packets can nevertheless give the same middle owner; global owner
disjointness is an additional matching condition not contained in
Theorems 2.1 or 3.1.

## 5. Independent layers are not one history

Suppose a common middle-owner packet has lower targets

\[
                         F_q(i)=\bigcap_{j=0}^{q}M_{i+j}.
\]

Then necessarily

\[
 \boxed{
 F_{q+1}(i)=F_q(i)\cap F_q(i+1).}                \tag{5.1}
\]

At occurrence level the phase successor must also commute with this
projection:

\[
 \sigma_{q+1}\bigl(F_q(i)\cap F_q(i+1)\bigr)
  =F_q(i+1)\cap F_q(i+2).                         \tag{5.2}
\]

Thus applying Theorem 3.1 independently to every adjacent rank can choose
different providers for the same nested flag and different successors
after projection.  It proves all rankwise Hall cuts, but not (5.1)--(5.2),
not the no-recycling history through \(H\), and not the residence equation
(4.4).  The common-history coupling is the precise unsplittable part of
the annulus problem.

## 6. A coarse-power obstruction for a prescribed SCD flag map

Let \(G\subseteq\binom{[n]}m\) be complement closed.  Suppose
\(\phi_q(X)\subset X\), \(|\phi_q(X)|=m-q\), is a proposed lower target
at every \(X\in G\).  Define

\[
 P_q(X)=\phi_q(X)
       \cup\bigl(X^c\setminus\phi_q(X^c)\bigr).   \tag{6.1}
\]

The two terms are disjoint and have sizes \(m-q\) and \(q\), so \(P_q(X)\)
is a middle set.  Also

\[
                         P_q(X^c)=P_q(X)^c.        \tag{6.2}
\]

### Theorem 6.1 (antipodal coarse-power law)

Suppose \(G\) is partitioned into physical length-\(n\) cyclic-order
packets with successor \(\sigma\), so

\[
                         \sigma^mX=X^c.           \tag{6.3}
\]

If \(\phi_q(X)\) is the actual forward depth-\(q\) intersection at every
phase, then

\[
                         \boxed{P_q(X)=\sigma^qX.}              \tag{6.4}
\]

#### Proof

On one packet write

\[
 X_i=\{z_i,z_{i+1},\ldots,z_{i+m-1}\}.
\]

Its forward intersection is

\[
 \phi_q(X_i)
   =\{z_{i+q},\ldots,z_{i+m-1}\}.                \tag{6.5}
\]

At the antipodal phase,

\[
 X_i^c\setminus\phi_q(X_i^c)
   =\{z_{i+m},\ldots,z_{i+m+q-1}\}.              \tag{6.6}
\]

The union of (6.5) and (6.6) is the length-\(m\) interval beginning at
\(i+q\), namely \(X_{i+q}=\sigma^qX_i\).
\(\square\)

Put

\[
 g=\gcd(n,q),\qquad d=\gcd(m,q),\qquad C(X)=X^c.
\]

### Corollary 6.2 (root and cycle constraints)

If a proposed map \(\phi_q\) is realized exactly by physical packets,
then \(P_q\) is a permutation of \(G\) satisfying

\[
 P_qC=CP_q,                                           \tag{6.7}
\]

\[
 P_q^{\,m/d}=C^{q/d},                                \tag{6.8}
\]

and its cycle type is

\[
 \boxed{
 \left({n\over g}\right)^{g|G|/n}.}                 \tag{6.9}
\]

#### Proof

Equations (6.7)--(6.8) follow from \(P_q=\sigma^q\) and
\(C=\sigma^m\):

\[
 P_q^{m/d}=\sigma^{qm/d}
           =(\sigma^m)^{q/d}=C^{q/d}.
\]

On each length-\(n\) cycle of \(\sigma\), its \(q\)-th power has exactly
\(g\) cycles, each of length \(n/g\), proving (6.9).
\(\square\)

These conditions are necessary, not sufficient: one still needs a common
\(n\)-cycle root satisfying the physical coordinate-residence equations.

There is a stable approximate Hall consequence.  Suppose a fixed proposed
map \(\phi_q\) disagrees with the actual packet target map on a phase set
\(E\subseteq G\), \(|E|=e\).  Then on

\[
                         G\setminus(E\cup C E)
\]

the proposed \(P_q\) agrees with the injective map \(\sigma^q\).  Hence,
for every \(A\subseteq G\),

\[
 \boxed{
 |P_q(A)|\ge |A|-2e.}                              \tag{6.10}
\]

Equivalently,

\[
 \max_{A\subseteq G}(|A|-|P_q(A)|)\le2e.           \tag{6.11}
\]

Thus a linear collision defect of the coarse map excludes an
\(o(W)\)-exception realization of that fixed SCD assignment.  Wrong cycle
structure alone is weaker: one exceptional phase in each eventual packet
can break every coarse-power component, and that costs only
\(O(W/m)=o(W)\).

## 7. Why no scalar or codegree obstruction appears

Let \(\Omega^+\) be the directed cyclic orders on \([n]\), modulo
rotation.  A fixed \(r\)-set is a cyclic interval in exactly

\[
                         r!(n-r)!                              \tag{7.1}
\]

orders.  Give every order the weight

\[
                   {1\over(m-q_0)!(m+q_0)!}.                  \tag{7.2}
\]

Then every base-depth target has load one, every depth-\(q\) target has
load

\[
                         {N_{q_0}\over N_q}\ge1,              \tag{7.3}
\]

every middle owner has load

\[
                         {N_{q_0}\over W}<1,                  \tag{7.4}
\]

and the total packet mass is

\[
                         {N_{q_0}\over n}.                    \tag{7.5}
\]

Thus every unaugmented linear capacity or Farkas cut passes at the
corrected partial mass.  The complete band packet hypergraph also has
maximum normalized pair codegree

\[
                         {2\over m-H+1}=O(m^{-1}).              \tag{7.6}
\]

Neither fact proves the desired integral theorem.  The annulus contains
\(\Theta(W\sqrt m)\) target cells, so the required absolute \(o(W)\)
leave is a relative \(o(m^{-1/2})\) error.  Ordinary small-codegree
matching control does not supply that precision, and it does not impose
the common-history equations (4.4) and (5.1).

## 8. Exact boundary

Proved:

1. the exact floor correction (1.1)--(1.5);
2. an unconditional second inclusion matching for every adjacent annular
   pair of ranks, Theorem 2.1;
3. the exact critical active-path count \(N_q-N_{q+1}\);
4. the residual Johnson seam Hall criterion, Theorem 3.1;
5. the exact cycle-type and coordinate-residence tests;
6. the failure of independent layerwise matchings to create one
   all-depth history; and
7. the coarse-power/root obstruction for every prescribed complement-
   paired SCD target map.

Not proved:

1. a choice of the second matching whose residual shores satisfy (3.2);
2. a seam factor giving only length-\(2m\) components;
3. the physical residence equation (4.4) on those components;
4. simultaneous projection consistency through all
   \(q_0\le q\le H\); or
5. global owner disjointness of the reconstructed middle cycles.

The exact remaining positive route is therefore narrower than a generic
SCD matching theorem.  It must choose the second inclusion matchings and
all residual seams jointly so that they form a common family of
coordinate-residence \(2m\)-cycles, while the SCD designated targets are
preserved at every depth except for aggregate \(o(W)\) exceptions.
