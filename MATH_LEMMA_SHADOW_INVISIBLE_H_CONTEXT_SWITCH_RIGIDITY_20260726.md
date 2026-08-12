# Shadow-invisible switching in the Johnson 2-factor normal form

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let (F) be a path or cycle factor in a Johnson graph, and attach to every
oriented (q)-window its lower intersection and upper union.  There is an
exact finite-context characterization of a switch which preserves all
signed traces through depth (H).

Three consequences are immediate.

1. A nontrivial ordinary two-edge switch can never preserve both signed
   depth-one trace multisets.  In particular, the familiar switch inside
   one clique (K_R) preserves the lower first shadow but necessarily
   changes the upper first shadow.
2. The smallest signed-depth-one-invisible reconnection uses three old and
   three new edges.  It is the octahedral (J(4,2)) trade displayed in
   Section 4.
3. No nontrivial shadow-invisible reconnection of any arity is supported
   inside one physical split-pair cube packet.  The lower depth-one target
   already determines a cube edge uniquely.

Consequently neither pairwise switching of the product-SCD paths nor
within-packet switching of diverse-compiler cycles can supply the needed
component collapse.  A surviving construction must use simultaneous
three-or-more-edge trades crossing packet boundaries, and must satisfy the
full (H)-context identity below.  No abundance theorem for such trades is
proved here.

## 1. Edge flags determine every higher trace

Let

\[
             X_0,X_1,\ldots,X_t
\]

be a path in (J(N,m)).  For the edge (e_i=X_{i-1}X_i), put

\[
       \ell_i=X_{i-1}\cap X_i,\qquad
       u_i=X_{i-1}\cup X_i.                         \tag{1.1}
\]

### Lemma 1.1 (meet/join word)

For every (q\le t),

\[
 \bigcap_{j=0}^{q}X_j=\bigcap_{i=1}^{q}\ell_i,
 \qquad
 \bigcup_{j=0}^{q}X_j=\bigcup_{i=1}^{q}u_i.        \tag{1.2}
\]

#### Proof

Every (X_j) with (0<j<q) occurs in the two adjacent edge
intersections and unions, while the endpoint vertices occur in the first
and last edge.  Associativity of intersection and union gives (1.2).
\(\square\)

Thus the complete signed trace system of a factor is the meet/join
(q)-deck of its edge-flag word.  Return-freeness is the additional rank
condition that the two sets in (1.2) have sizes (m-q) and (m+q).

## 2. Exact (H)-context signature of a port pairing

Cut a collection of pairwise vertex-disjoint factor edges.  Assume first
that consecutive cut edges on every old and new component are separated
by at least (H) retained edges.  Thus a protected window contains at
most one cut edge.  Each exposed endpoint (v) retains an external path
pointing away from the cut.  Write

\[
 \ell_{v,1},\ell_{v,2},\ldots,\ell_{v,H-1},
 \qquad
 u_{v,1},u_{v,2},\ldots,u_{v,H-1}                  \tag{2.1}
\]

for the lower and upper edge flags encountered along that external path.
Put

\[
 L_v(r)=\bigcap_{i=1}^{r}\ell_{v,i},\qquad
 U_v(r)=\bigcup_{i=1}^{r}u_{v,i},                  \tag{2.2}
\]

with (L_v(0)=[N]) and (U_v(0)=\varnothing).

If (v,w) are reconnected by a Johnson edge, write

\[
       \ell(vw)=v\cap w,\qquad u(vw)=v\cup w.      \tag{2.3}
\]

For (1\le q\le H) define the signed seam signature

\[
\begin{aligned}
 \Sigma_{q}^{-}(v,w)
   &=\multiset_{r+s=q-1}
       \left\{L_v(r)\cap\ell(vw)\cap L_w(s)\right\},\\
 \Sigma_{q}^{+}(v,w)
   &=\multiset_{r+s=q-1}
       \left\{U_v(r)\cup u(vw)\cup U_w(s)\right\}.
                                                               \tag{2.4}
\end{aligned}
\]

The multiset is unoriented: exchanging (v,w) replaces (r) by (s).

### Theorem 2.1 (exact flag-preserving switch criterion)

Let (M_0,M_1) be two perfect matchings of the same exposed port set,
assume every edge of both matchings is a Johnson edge, and assume the
separation condition above in both resulting factors.  Replacing
(M_0) by (M_1) preserves the complete lower and upper trace multisets
through depth (H) if and only if, for every (q\le H),

\[
 \biguplus_{vw\in M_0}\Sigma_q^-(v,w)
 =\biguplus_{vw\in M_1}\Sigma_q^-(v,w),
 \qquad
 \biguplus_{vw\in M_0}\Sigma_q^+(v,w)
 =\biguplus_{vw\in M_1}\Sigma_q^+(v,w).           \tag{2.5}
\]

If all new windows must remain literal depth-(q) flags, every set in
the first equality must additionally have size (m-q), and every set in
the second equality size (m+q).

#### Proof

Windows avoiding the cut edges are unchanged.  A (q)-window using a
new edge (vw) contains uniquely (r) external edges on the (v)-side
and (s=q-1-r) on the (w)-side.  Lemma 1.1 gives exactly (2.4).
Therefore (2.5) is necessary and sufficient.  The last assertion is the
definition of return-freeness. \(\square\)

This is the promised phase-free (H)-context formulation.  It also shows
why equality at the cut edge alone is insufficient: depth (q) tests all
(q) possible splits of the two collars.

If protected windows can contain two or more cut edges, (2.5) remains a
necessary one-cut marginal condition but is no longer sufficient.  The
exact general criterion is equality of the complete meet/join (q)-decks
of the two reconnected edge-flag words, by Lemma 1.1.  Thus close-packed
switches require a genuine multi-seam identity rather than independent
port checks.

## 3. Rigidity of ordinary two-edge switches

For a Johnson edge (e=XY), call

\[
                         (\ell(e),u(e))             \tag{3.1}
\]

its joint depth-one flag.  A joint flag determines the edge uniquely:
if (L\subset U), (|L|=m-1), (|U|=m+1), then the two endpoints are
the two (m)-sets strictly between (L) and (U).

### Theorem 3.1 (signed two-switch rigidity)

Let (A,B,C,D) be four distinct (m)-sets such that

\[
 AB,\ CD,\ AD,\ CB
\]

are Johnson edges.  If

\[
\begin{aligned}
 \{A\cap B,C\cap D\}&=\{A\cap D,C\cap B\},\\
 \{A\cup B,C\cup D\}&=\{A\cup D,C\cup B\},       \tag{3.2}
\end{aligned}
\]

then the new edge set equals the old edge set.  Hence a nontrivial
two-edge switch cannot be signed-depth-one invisible, and therefore
cannot be (H)-context invisible for any (H\ge1).

#### Proof

Write the old flags as ((L_1,U_1),(L_2,U_2)).  If the permutations in
the two equalities (3.2) agree, then each new joint flag is an old joint
flag, so uniqueness of the edge from its joint flag makes the switch
inert.

Suppose the permutations disagree.  Then, after relabelling, the new
joint flags are ((L_1,U_2)) and ((L_2,U_1)).  Thus every (L_i) is
contained in every (U_j).  If either (L_1=L_2) or (U_1=U_2), joint
flag uniqueness again makes the edge set inert.  Otherwise put

\[
 t=|L_1\setminus L_2|\ge1,\qquad
 s=|U_1\setminus U_2|\ge1.
\]

The containments imply

\[
 m-1+t=|L_1\cup L_2|
 \le |U_1\cap U_2|=m+1-s,
\]

so (t+s\le2).  Hence (t=s=1) and

\[
              X=L_1\cup L_2=U_1\cap U_2            \tag{3.3}
\]

is an (m)-set.  The vertex (X) is an endpoint of both old edges
having flags ((L_1,U_1)) and ((L_2,U_2)).  This contradicts the
assumption that (AB) and (CD) are disjoint factor edges. \(\square\)

In particular, if (AB) and (CD) lie in the same clique (K_R), the
usual two-switch preserves two copies of the lower target (R), but its
upper unions cannot also be preserved unless the switch is inert.

### Theorem 3.2 (direction-pair histogram is forced)

Let two spanning Johnson factors have the same lower depth-one multiset,
the same upper depth-one multiset, and the same owner degrees.  Then they
have the same number of edges in every physical direction pair
\(\{a,b\}\).

#### Proof

Put \(f_{ab}(S)={\bf1}_{\{a,b\}\subseteq S}\).  For an edge \(XY\),
write \(L=X\cap Y\) and \(U=X\cup Y\).  Directly,

\[
 {\bf1}_{U\setminus L=\{a,b\}}
 =f_{ab}(L)+f_{ab}(U)-f_{ab}(X)-f_{ab}(Y).          \tag{3.4}
\]

Summing (3.4) over either factor, the first two terms depend only on its
two signed depth-one trace multisets.  The last two terms depend only on
owner degrees.  All three ledgers agree by hypothesis, so every
direction-pair count agrees. \(\square\)

Thus the octahedral trade below does not change which physical axes are
used: it only reassigns the same three axes to different lower/upper
flags.  More generally, any proposed trace-invisible trade which creates
a new direction pair is impossible at every arity.

## 4. The minimal signed-depth-one trade

The two-edge rigidity is sharp.  Let (C) be an ((m-2))-set and let
(a,b,c,d) be four coordinates outside (C).  Abbreviate

\[
                         xy=C\cup\{x,y\}.
\]

Consider the two matchings of the same six owners

\[
\begin{aligned}
 M_0&=\{ac\!\! -\! ad,\ ab\!\!-\!bd,\ bc\!\!-\!cd\},\\
 M_1&=\{ab\!\! -\! ad,\ ac\!\!-\!cd,\ bc\!\!-\!bd\}.       \tag{4.1}
\end{aligned}
\]

Their lower flag multisets are both

\[
               \{C+a,C+b,C+c\},                    \tag{4.2}
\]

and their upper flag multisets are both

\[
 \{C+a+b+d,\ C+a+c+d,\ C+b+c+d\}.                 \tag{4.3}
\]

The union (M_0\cup M_1) is an alternating (6)-cycle in the
octahedron (J(4,2)).  Thus three old edges are sufficient, while
Theorem 3.1 proves that two are not.

There is also a useful product-grid calibration.  If

\[
                         d\in B_*,\qquad a,b,c\in A_*,
\]

then every edge in (4.1) can be oriented from the owner containing (d)
to the owner not containing (d), and every such edge increases
(|X\cap A_*|) by one.  Therefore this minimal trade remains inside the
globally coordinate-monotone category.

It follows from the sharp monotone width theorem that applying any
collection of these forward trades to the extremal product-SCD diagonal
cover cannot reduce its number

\[
                 \binom m{\lfloor m/2\rfloor}^2
\]

of paths.  A component-reducing trade in that construction must introduce
genuinely mixed orientation or leave the monotone category.

The trade (4.1) is only a depth-one result.  At higher depth its six
external collars must satisfy (2.5); no such collar theorem follows from
the octahedral identity.

### Proposition 4A (directed-link characterization)

For an \((m-2)\)-set \(C\) and \(d\notin C\), form the partial directed
link graph \(D_{C,d}\) on the coordinates outside \(C\cup\{d\}\).  Put
an arc \(x\to y\) when the oriented factor contains

\[
                         C\cup\{d,x\}
                 \longrightarrow C\cup\{x,y\}.                 \tag{4A.1}
\]

The old matching \(M_0\) in (4.1), oriented from the \(d\)-shore to the
non-\(d\) shore, is exactly a directed triangle

\[
                         a\longrightarrow c
                          \longrightarrow b
                          \longrightarrow a                       \tag{4A.2}
\]

in \(D_{C,d}\); the new matching reverses that triangle.  Thus a positive
installation requires a directed link triangle plus synchronized
external contexts.

This condition is sparse on average.  If an oriented 2-factor on
\(\binom{[2m]}m\) has \(W\) arcs, each arc contributes to exactly \(m-1\)
link graphs, while the number of pairs \((C,d)\) is

\[
                         \binom{2m}{m-2}(m+2).
\]

Hence the exact average number of link arcs is

\[
 {W(m-1)\over\binom{2m}{m-2}(m+2)}
                         ={m+1\over m}.                         \tag{4A.3}
\]

No triangle scarcity theorem follows from this mean alone, since link
arcs may cluster.  It does show that triangle abundance is a structural
property and not a marginal consequence of factor degree.

#### Proof

The three old directed edges in (4.1) give respectively
\(a\to c\), \(c\to b\), and \(b\to a\); the new edges give the reverse
arcs.  For the count, an oriented Johnson edge \(X\to Y\) has
\(d=X\setminus Y\), \(y=Y\setminus X\), and one representation (4A.1)
for every \(x\in X\cap Y\), with
\(C=(X\cap Y)\setminus\{x\}\).  There are \(m-1\) choices.  The displayed
binomial ratio simplifies to \((m+1)/m\). \(\square\)

### Theorem 4.1 (two-type collar lift to every depth)

The octahedral trade (4.1) has a literal signed \(H\)-context-invisible
lift whenever \(H=o(m)\), for all sufficiently large \(m\).

Partition its six ports as

\[
 {\cal V}_0=\{ab,ac,bc\},\qquad
 {\cal V}_1=\{ad,bd,cd\}.                         \tag{4.4}
\]

Choose pairwise distinct coordinates

\[
 z_i^0,z_i^1\in C,\qquad
 e_i^0,e_i^1\notin C\cup\{a,b,c,d\},
 \qquad 1\le i\le H-1,                             \tag{4.5}
\]

with the four displayed families mutually disjoint where their ambient
sets overlap.  This is possible once \(2(H-1)\le m-2\).  Attach to every
port \(xy\in{\cal V}_\tau\) the outward rail

\[
 X_{xy,t}^{\tau}
  =\left(C\setminus\{z_1^\tau,\ldots,z_t^\tau\}\right)
     \cup\{e_1^\tau,\ldots,e_t^\tau\}\cup\{x,y\},
 \qquad 0\le t\le H-1.                             \tag{4.6}
\]

Keep all rail edges fixed and replace only the central matching \(M_0\)
by \(M_1\).  Then every window through depth \(H\) is return-free on both
shores, and the complete lower and upper trace multisets are identical
before and after the trade.

#### Proof

The union \(M_0\cup M_1\) is bipartite with shores (4.4); every old and
new central edge joins a type-zero port to a type-one port.  A
\(q\)-window containing a central edge uses \(r\) rail edges on the
type-zero side and \(s=q-1-r\) on the type-one side.

If the central edge has lower flag \(C+x\), its lower \(q\)-flag is

\[
 \left(C\setminus
       \{z_1^0,\ldots,z_r^0,z_1^1,\ldots,z_s^1\}\right)\cup\{x\}.
                                                               \tag{4.7}
\]

If its upper flag is \(C\cup Q\), where \(Q\) is the corresponding
three-element subset of \(\{a,b,c,d\}\), its upper \(q\)-flag is

\[
 C\cup Q\cup
       \{e_1^0,\ldots,e_r^0,e_1^1,\ldots,e_s^1\}.                \tag{4.8}
\]

For fixed \(r,s\), (4.7) depends on the central edge only through its
lower flag and (4.8) only through its upper flag.  Equations
(4.2)--(4.3) therefore give equality of the old and new multisets for
every \(r,s,q\).

All collar directions in (4.5) are mutually disjoint across the two
types and avoid the four central coordinates.  Hence no coordinate is
used twice in a protected window, proving both lower and upper
return-freeness.  Windows avoiding the central matching are unchanged.
\(\square\)

The two collar types are essential.  Giving all six rails one common
direction word would repeat every collar coordinate on the two sides of
a central edge and create both a positive and a negative residence.
The bipartition of the alternating octahedral \(6\)-cycle supplies
exactly the separation needed to avoid that failure.

Theorem 4.1 proves local feasibility, not abundance.  To reduce a
factor's component count, its three old central edges and six rails must
already occur in the factor (or be installed by a larger owner trade),
and the matching replacement must have positive joining rank.  No theorem
below forces \(\Theta(W/\sqrt m)\) disjoint copies in either the
product-SCD or rank-twisted compiler factor.

### Proposition 4.2 (exact component rank and zero direction cocycle)

Orient all central edges from \({\cal V}_1\) to \({\cal V}_0\).  Index the
old arcs as \(u_i\to v_i\), \(i\in\{1,2,3\}\), and the new arcs as

\[
                         u_i\longrightarrow v_{\pi(i)},          \tag{4.9}
\]

where \(\pi\) is a \(3\)-cycle.  After deleting the three old arcs, let
\(\tau\in{\mathfrak S}_3\) be the outside-connection permutation: the
unchanged directed remainder starting at \(v_i\) ends at \(u_{\tau(i)}\).
Then the exact component reduction is

\[
                  r_{\rm join}=c(\tau)-c(\tau\pi),              \tag{4.10}
\]

where \(c(\rho)\) is the number of cycles of a permutation.  In
particular, if the three old arcs lie in three distinct factor cycles,
then \(\tau={\rm id}\) and the trade merges all three into one:
\(r_{\rm join}=2\).

The old and new central direction multisets are both

\[
                         \{\{a,d\},\{b,d\},\{c,d\}\}.             \tag{4.11}
\]

With the displayed orientation, both delete \(d\) and insert each of
\(a,b,c\) once.  Hence the trade has zero direction-count and run-vector
cocycle.  There is no orientation-marginal obstruction to positive
joining rank.

#### Proof

Following a new arc \(u_i\to v_{\pi(i)}\) and then the unchanged outside
path sends \(i\) to \(\tau(\pi(i))\).  Components meeting the gadget are
therefore the cycles of \(\tau\pi\); before the switch they are the cycles
of \(\tau\).  This proves (4.10).  Formula (4.11) is read directly from
(4.1). \(\square\)

### Proposition 4.3 (isolated-collar packing ceiling)

Suppose a family of lifted octahedral trades is owner-disjoint and
\(H\)-separated, so that every cut port has its own length-\((H-1)\)
context rail.  If it contains \(s\) trades, then

\[
                         6Hs\le W,\qquad
             \sum r_{\rm join}\le2s\le {W\over3H}.               \tag{4.12}
\]

Since \(H/\sqrt m\to\infty\),

\[
                         {W\over3H}=o(W/\sqrt m).                \tag{4.13}
\]

Thus isolated lifted gadgets cannot collapse the
\(\Theta(W/\sqrt m)\) product-SCD components, even if every gadget has
maximum joining rank.  More generally, an isolated \(k\)-edge matching
trade has \(2k\) context arms, uses at least \(2kH\) owner incidences, and
has joining rank at most \(k-1\); all owner-disjoint isolated trades have
total rank less than \(W/(2H)\).

#### Proof

The six rails in Theorem 4.1 contain \(H\) owners including their central
ports.  Owner-disjointness gives the first inequality.  A matching trade
on six ports changes the number of components by at most two, giving the
second.  The general statement is identical: reconnecting \(k\) cut
edges can merge at most \(k\) old components into one. \(\square\)

Consequently a successful installation must be close-packed or
sequentially state-dependent: many central trades must share context
rails, and their combined multi-seam meet/join deck must cancel globally.
Packing independent \(H\)-collared copies reaches only the
\(W/H\) scale, whereas the required product-path joining rank is
\(W/\sqrt m\).

## 5. Absolute rigidity inside one split-pair packet

Let a physical (Q_R) packet use disjoint coordinate pairs

\[
                       \{x_i^0,x_i^1\},\qquad 1\le i\le R,
\]

with all other coordinates fixed.  Every packet owner chooses exactly
one endpoint of each pair.

### Theorem 5.1 (packet lower-shadow injectivity)

Within one packet, the map

\[
       e\longmapsto\ell(e)                         \tag{5.1}
\]

from Johnson edges to lower depth-one targets is injective.  Consequently
any edge-set replacement supported wholly inside one packet and
preserving the lower depth-one multiset has exactly the same edge set.
It cannot join compiler cycles.

#### Proof

For an edge in direction (i), its lower intersection contains neither
endpoint of pair (i), and contains one specified endpoint from every
other active pair.  Hence the lower target recovers (i), all spectator
orientation bits, and therefore the unique edge. \(\square\)

The upper target gives the dual proof.  This rules out invisible switches
of every arity inside a diverse-compiler packet, not only ordinary
two-switches.  A useful compiler-cycle join must cross packet or atlas
boundaries.  The existing (Q_{R+1}) slab trade does cross a parent
boundary, but it replaces two (Q_R) packets by two (Q_R) packets and
has a nonzero literal trace derivative; it is not a shadow-invisible
cycle join.

## 6. Exact positive switch-packing lemma

The preceding results identify the object an eventual construction must
pack.

### Lemma 6.1 (invisible trade packing)

Let (F) have (p) path/cycle components.  Suppose one can apply a
sequence of owner-disjoint or sequentially compatible matching trades

\[
                         M_i\longrightarrow M_i'
\]

such that:

1. every trade satisfies the (H)-context identities (2.5), the
   return-free rank conditions, and the cut supports are (H)-separated;
   alternatively, for close-packed trades, the full meet/join deck
   identity from the paragraph after Theorem 2.1 is verified directly;
2. every trade preserves the owner set and factor degrees; and
3. at its time of application, trade (i) decreases the component count
   by (r_i\ge1).

Then the final factor has exactly

\[
                         p-\sum_i r_i               \tag{6.1}
\]

components and exactly the same complete signed trace multiset through
depth (H) as (F).

In particular, if

\[
             \sum_i r_i=p-o(W/H),                  \tag{6.2}
\]

the component condition is solved with zero additional shadow defect.

#### Proof

The degree and owner assertions make every intermediate object a factor.
Theorem 2.1 preserves every protected trace multiset at each step, so the
property telescopes.  Component counts telescope by assumption 3. \(\square\)

For the product-SCD diagonal cover,

\[
 p=\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.
                                                               \tag{6.3}
\]

Thus (6.2) requires (Theta(W/\sqrt m)) useful trade rank.  Theorems 3.1
and 5.1 show that pairwise path switches and within-packet compiler
switches contribute none.  Forward octahedral trades contribute no net
rank by the monotone-width obstruction.  The exact remaining possibility
is an abundance theorem for mixed-orientation, cross-packet,
three-or-more-edge trades whose external collars obey (2.5)
simultaneously for every (q\le H).

## 7. Boundary

Proved here:

* the exact (H)-context/flag criterion;
* complete rigidity of signed-invisible ordinary two-switches;
* a minimal three-edge depth-one trade and its exact two-type collar lift
  through every protected depth;
* complete lower-shadow rigidity inside a split-pair packet; and
* the exact switch-packing implication.

Not proved:

* positive-density packing of the lifted octahedral trades in the
  two-colour product-SCD
  factor; or
* a cross-packet compiler trade system of total joining rank
  (Theta(W/\sqrt m)).

Hence shadow-invisible joining is not a pairwise seam mechanism.  It is a
multi-port context-coboundary problem.
