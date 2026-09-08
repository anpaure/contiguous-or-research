# Bichromatic paired-SCD obstruction and the exact open-path closure gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

Let \(G_m\) be the incidence graph between

\[
 \mathcal L=\binom{[2m]}{m-1}\qquad\text{and}\qquad
 \mathcal M=\binom{[2m]}m.
\]

It is \((m+1,m)\)-biregular.  In every proper full
\((m+1)\)-edge-colouring, each lower vertex sees all colours and each
middle vertex misses exactly one colour.

This gives an exact no-go for the proposed use of the complement-symmetric
\(B_4\) paired-SCD seed.

* The union of any two colour classes has middle degrees only \(1\) and
  \(2\).  A paired-SCD central incidence factor has degree \(2\) on
  \(N_1\) active middle owners and degree \(0\) on the
  \(\mathrm{Cat}_m\) common singleton owners.  Therefore it can never
  equal a bichromatic subgraph of a full edge-colouring.  In particular the
  closed \(B_4\) seed is not two colour classes of a full 3-edge-colouring.
* A bichromatic subgraph instead consists of cycles and exactly
  \(\mathrm{Cat}_m\) open paths.  Their \(2\mathrm{Cat}_m\)
  endpoints split equally according to the two missing colours.
* Converting it to the incidence lift of a lower-rainbow Johnson 2-factor
  requires at least

  \[
   \mathrm{Cat}_m
  \]

  edge replacements, equivalently symmetric difference at least
  \(2\mathrm{Cat}_m\).  For every proposed choice of omitted endpoints,
  attainment is equivalent to a literal endpoint-closure matching.  The
  clean one-sided choice has one especially simple Hall graph.
* If \(\tau\) is the original pairing of path endpoints and
  \(\sigma\) is the closure matching, the new components are governed
  exactly by the cycles of \(\tau^{-1}\sigma\).  Hall feasibility alone
  does not give the required \(o(W/H)\) component count.
* A contextual \(B_4\) copy can occur only as an **open** local object:
  each of its two locally omitted owner states must carry at least one of
  the two selected colours through an exterior facet.  Thus a family of
  disjoint six-owner \(B_4\) contexts pays at least two exterior selected
  incidences per context.  Overlapping contexts can align those ports, so
  this local toll does not imply more than the global sharp Catalan toll
  without an overlap bound.

Even after the closure matching is found, upper rainbowness and equal-radius
lower/upper half-chain gluing remain separate conditions.  Twisted
complement invariance of the resulting Johnson factor is a sufficient
condition for upper rainbowness, but it is not supplied by the edge-colour
degrees.

## 1. Missing-colour partition in a full edge-colouring

Put

\[
 W=\binom{2m}m,\qquad
 N_1=\binom{2m}{m-1}=\frac{m}{m+1}W,\qquad
 C=W-N_1=\frac{W}{m+1}=\mathrm{Cat}_m.
 \tag{1.1}
\]

Let

\[
 \chi:E(G_m)\to[m+1]
 \tag{1.2}
\]

be a proper edge-colouring using all \(m+1\) colours.  Since every
\(R\in\mathcal L\) has degree \(m+1\), it is incident to one edge
of every colour.  Since every \(X\in\mathcal M\) has degree \(m\),
its incident edges have distinct colours and there is a unique missing
colour \(\mu(X)\).

For \(c\in[m+1]\), define

\[
 E_c=\{X\in\mathcal M:\mu(X)=c\}.
 \tag{1.3}
\]

### Lemma 1.1 (exact missing-colour census)

The families \(E_1,\ldots,E_{m+1}\) partition \(\mathcal M\),
and

\[
 |E_c|=C\qquad(c\in[m+1]).
 \tag{1.4}
\]

#### Proof

Uniqueness of \(\mu(X)\) gives the partition.  A fixed colour class
is a matching which saturates \(\mathcal L\), so it contains
\(N_1\) edges and reaches \(N_1\) distinct middle vertices.  It
therefore misses exactly \(W-N_1=C\) middle vertices. \(\square\)

Fix two distinct colours \(c,d\), and let \(H_{c,d}\) be their
union.

### Theorem 1.2 (bichromatic path normal form)

In \(H_{c,d}\),

\[
 \deg(R)=2\quad(R\in\mathcal L),
 \tag{1.5}
\]

and

\[
 \deg(X)=
 \begin{cases}
 1,&X\in E_c\dot\cup E_d,\\
 2,&X\notin E_c\dot\cup E_d.
 \end{cases}
 \tag{1.6}
\]

Consequently \(H_{c,d}\) is a disjoint union of even cycles and
exactly \(C\) paths.  Every path has one endpoint in \(E_c\) and one
endpoint in \(E_d\).

#### Proof

Equation (1.5) follows because every lower vertex sees both colours.  A
middle vertex misses exactly one colour, which proves (1.6).  A finite graph
of maximum degree two is a union of paths and cycles.  There are \(2C\)
degree-one vertices, hence \(C\) paths.

Along a bichromatic path the edge colours alternate.  Both endpoints lie on
the middle shore, so the path length is even; its two end edges have
opposite colours.  The endpoint incident only with colour \(d\) lies in
\(E_c\), and the endpoint incident only with \(c\) lies in
\(E_d\). \(\square\)

## 2. Degree-defect incompatibility with a paired SCD

Let \(\Gamma\) be the central Johnson 2-factor of a paired SCD, on
the active owner set \(A\subset\mathcal M\).  Its lower-incidence
lift is obtained by replacing every edge \({X,Y}\) by

\[
 X\ --\ (X\cap Y)\ --\ Y.
 \tag{2.1}
\]

Because every lower colour occurs exactly once,

\[
 |A|=N_1,\qquad
 \deg_{\widetilde\Gamma}(R)=2\quad(R\in\mathcal L),
 \tag{2.2}
\]

while

\[
 \deg_{\widetilde\Gamma}(X)=
 \begin{cases}
 2,&X\in A,\\
 0,&X\in\mathcal M\setminus A.
 \end{cases}
 \tag{2.3}
\]

The zero set has size \(C\).

### Theorem 2.1 (no bichromatic paired-SCD factor)

For every \(m\ge1\), no lower-incidence lift of a paired-SCD central
factor equals the union of two colour classes in a full proper
\((m+1)\)-edge-colouring of \(G_m\).

#### Proof

By (1.6), a bichromatic subgraph has positive degree at every middle
vertex.  By (2.3), a paired-SCD lift has degree zero at exactly \(C>0\)
middle vertices. \(\square\)

For \(m=2\), the cyclic \(B_4\) seed has four active middle states
and the two common singletons \(13,24\).  Its incidence lift is the
8-cycle

\[
 14\ --1\ --12\ --2\ --23\ --3\ --34\ --4\ --14,
 \tag{2.4}
\]

with degree zero at \(13\) and \(24\).  Theorem 2.1 says that this
cannot be two colour classes of any full 3-edge-colouring of
\(G_2\).  The conclusion is independent of how the three colours are
named and of the complement-reversal symmetry of the seed.

## 3. The sharp edit toll

Let \(F\) be any subgraph of \(G_m\) satisfying

\[
 \deg_F(R)=2\quad(R\in\mathcal L),\qquad
 \deg_F(X)\in\{0,2\}\quad(X\in\mathcal M).
 \tag{3.1}
\]

The degree sum forces exactly \(C\) middle vertices to have degree zero.

### Theorem 3.1 (minimum distance from two colour classes)

For every such \(F\),

\[
 |E(F)\triangle E(H_{c,d})|\ge2C.
 \tag{3.2}
\]

Since both graphs have \(2N_1\) edges, at least \(C\) old edges
must be removed and at least \(C\) new edges added.  Equality in
(3.2) is possible only when the degree-zero set of \(F\) is contained
in \(E_c\dot\cup E_d\).

#### Proof

Let \(Z\) be the degree-zero set of \(F\), so \(|Z|=C\), and
put \(P=E_c\dot\cup E_d\), so \(|P|=2C\).  If
\(t=|Z\cap P|\), the \(\ell^1\)-distance between the two
middle-degree vectors is

\[
 t+2(C-t)+(2C-t)=4C-2t\ge2C.
 \tag{3.3}
\]

Every edge in the symmetric difference contributes to exactly one middle
vertex, so its size is at least (3.3).  Both lower degree sums are
\(2N_1\), proving the replacement statement.  Equality requires
\(t=C\), i.e. \(Z\subseteq P\). \(\square\)

For the isolated \(B_4\) seed this says that at least two edge
replacements, or four incidences in symmetric difference, are necessary.
For vertex-disjoint closed six-owner \(B_4\) contexts to which the edit
is required to be internal, the bound adds: at least two replacements per
context.  Cross-context routing is the only way to avoid paying this local
bound independently.

## 4. Exact optimal closure graph

The lower bound \(C\) has an exact general attainment criterion.  Put

\[
 P=E_c\dot\cup E_d.
 \tag{4.0}
\]

For each \(v\in P\), let \(r(v)\) be its unique neighbour in
\(H_{c,d}\).  Fix a proposed degree-zero set \(Z\subseteq P\) of size
\(C\).  Define the bipartite graph \(K_Z\) with left shore consisting of
the \(C\) removal tokens indexed by \(z\in Z\), right shore
\(P\setminus Z\), and

\[
 z\sim y
 \quad\Longleftrightarrow\quad
 r(z)\subset y\quad\text{and}\quad r(z)\ne r(y).
 \tag{4.1}
\]

The left vertices are tokens even when two selected endpoints have the
same lower neighbour.  The inequality excludes an incidence already
present in \(H_{c,d}\).

### Theorem 4.1 (general optimal closure equivalence)

There is a factor satisfying (3.1), with degree-zero set exactly \(Z\),
at symmetric difference \(2C\) from \(H_{c,d}\), if and only if
\(K_Z\) has a perfect matching.  Given such a matching \(\sigma\), remove
every edge \(zr(z)\), \(z\in Z\), and add every edge
\(r(z)\sigma(z)\).

#### Proof

Every \(z\in Z\) loses its sole selected edge, and every
\(y\in P\setminus Z\) gains one edge.  At a lower vertex, the number of
new incidences equals the number of removal tokens having that lower
neighbour, so its degree is restored to two.  Matching on the right prevents
two gains at one middle endpoint, and (4.1) prevents adding an edge already
present.  Thus a perfect matching gives the required factor.

Conversely, equality in Theorem 3.1 permits no symmetric-difference edge at
a middle vertex outside \(P\), and forces precisely one removal at every
\(z\in Z\) and one addition at every \(y\in P\setminus Z\).  Preservation
of every lower degree pairs the removed lower-endpoint tokens with the
added incidences, producing a perfect matching in \(K_Z\). \(\square\)

For component bookkeeping it is convenient to use the one-sided choice
\(Z=E_c\).  Orient every
path of \(H_{c,d}\) from its endpoint in \(E_c\) to its endpoint in
\(E_d\).  For \(x\in E_c\), let \(r_d(x)\) be its unique
neighbour in \(H_{c,d}\); the edge has colour \(d\).  For
\(y\in E_d\), let \(r_c(y)\) be its unique neighbour; its edge
has colour \(c\).

Both maps are injective because each colour class is a matching.  In this
case \(K_Z\) is the endpoint-closure graph \(K_{c\to d}\) with shores
\(E_c,E_d\):

\[
 x\sim y
 \quad\Longleftrightarrow\quad
 r_d(x)\subset y\quad\text{and}\quad r_d(x)\ne r_c(y).
 \tag{4.2}
\]

### Corollary 4.2 (one-sided optimal closure)

The following are equivalent.

1. There is a subgraph \(F\) satisfying (3.1), having degree-zero set
   exactly \(E_c\), and obtained from \(H_{c,d}\) by exactly \(C\)
   edge replacements.
2. The graph \(K_{c\to d}\) has a perfect matching
   \(\sigma:E_c\to E_d\).

Given \(\sigma\), the factor is

\[
 F_\sigma
 =H_{c,d}
  -\{\,x r_d(x):x\in E_c\,\}
 +\{\,r_d(x)\sigma(x):x\in E_c\,\}.
 \tag{4.3}
\]

Hence optimal closure is equivalent to the literal Hall inequalities

\[
 |N_{K_{c\to d}}(S)|\ge|S|\qquad(S\subseteq E_c).
 \tag{4.4}
\]

#### Proof

Suppose \(\sigma\) is a perfect matching.  Formula (4.3) removes the
sole selected edge at each \(x\in E_c\), so those vertices acquire
degree zero.  Every \(y\in E_d\) receives one new edge and goes from
degree one to degree two.  Each lower vertex in the image of \(r_d\)
loses one edge and receives one, while all other degrees are unchanged.
The second clause of (4.2) prevents a duplicate edge.  Thus (3.1) holds and
there are exactly \(C\) replacements.

Conversely, equality in Theorem 3.1 with zero set \(E_c\) forces every
\(x\in E_c\) to lose its sole edge, every \(y\in E_d\) to gain one
edge, and no other middle degree to change.  Lower degrees remain two, so
the lower endpoints \(r_d(x)\) of the deleted edges must be precisely
the lower endpoints of the added edges.  The added incidences therefore
give a bijection \(\sigma:E_c\to E_d\) satisfying (4.2).  Hall's
theorem gives the equivalence with (4.4). \(\square\)

Proper edge-colour degrees alone do not imply (4.4): the condition concerns
the literal incidences between one colour's freed lower endpoints and the
other colour's missing middle set.  It is the exact additional expansion
gate for the open bichromatic route.

## 5. Exact component permutation

Let

\[
 \tau:E_c\to E_d
 \tag{5.1}
\]

send each \(E_c\)-endpoint to the \(E_d\)-endpoint of its original
\(H_{c,d}\)-path.  This is a bijection by Theorem 1.2.

### Theorem 5.1 (component formula)

For a perfect closure matching \(\sigma\), the components of
\(F_\sigma\) which contain the former open paths are in bijection
with the cycles of

\[
 \pi=\tau^{-1}\circ\sigma:E_c\to E_c.
 \tag{5.2}
\]

All original cycle components of \(H_{c,d}\) remain unchanged.  Hence

\[
 \operatorname{comp}(F_\sigma)
 =\operatorname{cyc}(H_{c,d})+\operatorname{cyc}(\tau^{-1}\sigma),
 \tag{5.3}
\]

where \(\operatorname{cyc}(H_{c,d})\) counts only its original cycle
components.

#### Proof

Delete the first edge of the path indexed by \(x\).  The remaining path
has endpoints \(r_d(x)\) and \(\tau(x)\).  The new edge indexed by
\(x\) joins \(r_d(x)\) to
\(\sigma(x)=\tau(\pi(x))\).  Thus following old path pieces and
new edges advances the path index by \(\pi\), and each cycle of
\(\pi\) gives one new component.  Formula (4.3) does not touch old
cycle components. \(\square\)

Therefore the desired component bound is the strengthened matching
problem

\[
 \operatorname{cyc}(H_{c,d})
 +\operatorname{cyc}(\tau^{-1}\sigma)
 =o(W/H).
 \tag{5.4}
\]

A perfect matching in \(K_{c\to d}\) need not satisfy (5.4).

## 6. The contextual \(B_4\) port toll

Fix four coordinates \(B=\{1,2,3,4\}\) and an exterior
\((m-2)\)-set \(S\) disjoint from \(B\).  The local active owners
are

\[
 S+14,\quad S+12,\quad S+23,\quad S+34,
 \tag{6.1}
\]

and the two local omitted states are \(S+13,S+24\).  The four local
lower rows are \(S+1,\ldots,S+4\).  Suppose the eight incidences of
the local 8-cycle (2.4), translated by \(S\), alternate colours
\(c,d\).

### Proposition 6.1 (two exterior ports per closed local seed)

Each of \(S+13\) and \(S+24\) is incident in \(H_{c,d}\) to at
least one lower facet obtained by deleting a coordinate of \(S\).
Consequently the local seed forces at least two selected-colour incidences
outside its four-row interface.

#### Proof

The local facets of \(S+13\) are \(S+1\) and \(S+3\).  Their
\(c,d\)-edges in the local 8-cycle go to active owners, so neither edge
to \(S+13\) has colour \(c\) or \(d\).  But a middle vertex misses
only one colour; hence \(S+13\) has at least one incident edge of colour
\(c\) or \(d\), and it must delete a coordinate of \(S\).  The
same argument uses local facets \(S+2,S+4\) for \(S+24\).
\(\square\)

For \(P\) six-owner contexts with pairwise disjoint local owner sets,
these ports have distinct middle endpoints, so there are at least \(2P\)
exterior selected incidences.  If the contexts overlap in their locally
omitted states, the same physical port may discharge several local
requirements; the valid lower bound is then the number of distinct omitted
owners.  Therefore a bounded-context linear toll requires an overlap bound.
This is precisely how a contextual/open recursion can evade independent
local payment: it must identify and route the omitted-state ports across
contexts before closing them globally.

At global scale Theorem 1.2 shows that coherent routing can reduce the open
defect to exactly \(2C\) endpoints, and Theorem 3.1 leaves only the sharp
\(C=\Theta(W/m)\) replacement toll.  Achieving that reduction is not a
formal consequence of tensoring the \(B_4\) seed; it is the global
edge-colouring and endpoint-Hall problem (4.4).

## 7. Upper rainbowness and the exact surviving scope

Every factor \(F_\sigma\) projects to a Johnson 2-factor on
\(\mathcal M\setminus E_c\) whose intersection colours are all
members of \(\mathcal L\), once each.  Nothing above controls its union
colours.

There is one useful sufficient symmetry.  Let

\[
 \theta(X)=\rho([2m]\setminus X)
 \tag{7.1}
\]

for a coordinate permutation \(\rho\).  If the projected Johnson
edge set is \(\theta\)-invariant, then lower rainbowness implies upper
rainbowness.  Indeed, for every Johnson edge \(e\),

\[
 L(\theta e)=\rho([2m]\setminus U(e)).
 \tag{7.2}
\]

Thus equal upper colours would give equal lower colours after applying
\(\theta\), and hence equal edges.  Since both colour sets have size
\(N_1\), the upper map is bijective.

The \(B_4\) seed has exactly such a twisted complement symmetry.  A
global open-path closure must preserve it, or prove upper rainbowness by a
different argument.  Even a doubly-rainbow Johnson factor is not yet a full
paired SCD: the lower and upper half-chain paths must have equal radii on
every matched central edge.

The proved boundary is therefore:

* a closed paired-SCD seed is never literally bichromatic in a full edge
  colouring;
* the optimal open repair costs at least \(C\) replacements and is
  equivalent, after choosing the omitted endpoints, to the corresponding
  endpoint Hall system; the one-sided version is (4.4);
* component control is the cycle constraint (5.4);
* upper rainbowness and radius-compatible half-chain gluing remain
  independent exact gates.
