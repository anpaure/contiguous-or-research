# The exact Catalan linear-path collar and the Hall-one connector face

Date: 2026-07-31  
Status: exact path-interface theorem, exact bounded-debt partition--Hall
min--max, and exact conditional graphic--gammoid theorem on the prepared
socket face; not an unconditional all-`m` connector-existence theorem

## 0. Verdict

The residence and deep-shadow effects of joining two oriented Catalan path
fragments have a finite exact collar.  For residence threshold

\[
                         h=d+1,
\]

the run part consists, for every coordinate, of its capped prefix length,
capped suffix length, and the bit saying that the coordinate occupies the
whole fragment.  For shadow depth at most `r`, one adds the first and last
`r` literal middle vertices and a bitset of already served targets.  These
data compose associatively.

The two global endpoints are genuine exemptions.  A final Hamilton path uses
`K-1`, not `K`, connector seams; its first and last positive runs may be
short; and no suffix--prefix window wrapping around the two ends exists.

There is also an exact useful connector theorem.  After a bounded service
core is contracted, suppose the remaining blocks are preoriented, every
available connector is context-robust for residence and already passes the
private/aligned palette--linkage tests, and the connector digraph is acyclic.
Then a component-spanning Hamilton path exists if and only if

\[
                  |N^+(X)|\mathrel{\ge}|X|-1
                  \qquad(X\subseteq V).             \tag{0.1}
\]

This is the exact Hall deficiency-one row.  The unmatched right copy and
unmatched left copy in the resulting bipartite matching are exactly the two
global endpoints.  Acyclicity is essential: three vertices with the two arcs
`a->b,b->a` satisfy (0.1) but have no spanning path.

Before the service core is fixed, a bounded bank whose witnesses cross one
seam has an exact partition--Hall min--max: assign every debt to the head of
its intended witnessing seam, filter the connector graph by whole assigned
fibres, and apply Hall.  More general bounded-depth witnesses use at most the
sum of their depths in seams, so exhaustive bounded-core contraction reduces
them to Hall-one.

Off the preoriented face, Edmonds' graphic--gammoid cuts are again exact only
when a prepared private socket gammoid represents **joint** port-disjoint
realizability.  General two-port seam matchings are not a matroid, so this
qualification cannot be omitted.

Thus the all-`m` problem is not a scalar run-capacity problem.  It is the
construction of a residence-compatible service core and a connector
catalogue satisfying either (0.1) on an acyclic face or a comparably strong
Hamiltonicity condition.

## 1. Exact residence collar

Let

\[
             P=(p_1,\ldots,p_s)
\]

be a nonempty oriented path in `J(2m,m)`.  Call `P` **internally
`h`-resident** if every positive coordinate run which meets neither endpoint
has length at least `h`.

For a coordinate `x`, define

\[
\begin{aligned}
 \lambda_x(P)&=\min\{h,\text{length of the initial }x\text{-run of }P\},\\
 \rho_x(P)&=\min\{h,\text{length of the terminal }x\text{-run of }P\},\\
 \omega_x(P)&={\bf1}[x\in p_i\text{ for every }i].
                                                        \tag{1.1}
\end{aligned}
\]

An absent endpoint run has length zero.  Write

\[
       {\cal R}_h(P)=((\lambda_x(P),\rho_x(P),\omega_x(P)))_{x\in[2m]}.
                                                        \tag{1.2}
\]

Only threshold comparisons and capped additions are used below, so capping
at `h` loses no information.

### Theorem 1.1 (exact two-fragment seam criterion)

Let `P,Q` be internally `h`-resident oriented paths with disjoint vertex
sets, and suppose their exposed endpoints are Johnson adjacent.  Their
linear concatenation `PQ` is internally `h`-resident if and only if, for
every coordinate `x`,

\[
 \rho_x(P)+\lambda_x(Q)=0,
 \quad\hbox{or}\quad
 \omega_x(P)\vee\omega_x(Q),
 \quad\hbox{or}\quad
 \rho_x(P)+\lambda_x(Q)\ge h.                         \tag{1.3}
\]

When (1.3) holds, its new collar is

\[
\begin{aligned}
 \lambda_x(PQ)
   &=\begin{cases}
       \min\{h,\lambda_x(P)+\lambda_x(Q)\},&\omega_x(P),\\
       \lambda_x(P),&\text{otherwise},
     \end{cases}\\
 \rho_x(PQ)
   &=\begin{cases}
       \min\{h,\rho_x(P)+\rho_x(Q)\},&\omega_x(Q),\\
       \rho_x(Q),&\text{otherwise},
     \end{cases}\\
 \omega_x(PQ)&=\omega_x(P)\omega_x(Q).                \tag{1.4}
\end{aligned}
\]

#### Proof

Every old internal run remains unchanged.  The only affected positive run
is the one, if any, touching the new seam.  Its two pieces have lengths
`rho_x(P)` and `lambda_x(Q)`, with a zero piece when that endpoint omits
`x`.  Their uncapped total is below `h` exactly when the displayed capped
sum is below `h`.

This seam run reaches the surviving left endpoint exactly when `P` is all
`x`, and reaches the surviving right endpoint exactly when `Q` is all `x`.
It is therefore newly internal exactly when the sum is positive and both
`omega` bits vanish.  This proves (1.3).  Reading the initial and terminal
runs of the concatenated word gives (1.4).  \(\square\)

### Definition 1.2 (context-robust seam)

A Johnson seam from `P` to `Q` is **context-robustly `h`-safe** when

\[
       \rho_x(P)+\lambda_x(Q)=0
       \quad\hbox{or}\quad
       \rho_x(P)+\lambda_x(Q)\ge h                  \tag{1.5}
\]

for every `x`.

This is the pairwise condition which does not spend either outer-endpoint
exemption.  It is equivalent to the three familiar rows:

* a coordinate lost at the seam has left suffix at least `h`;
* a coordinate gained at the seam has right prefix at least `h`; and
* a coordinate common to the two seam vertices has combined suffix--prefix
  length at least `h`.

Consequently any sequence of internally resident blocks joined only by
context-robust seams is internally resident, independently of which two
outer endpoints survive.  Condition (1.5) is deliberately stronger than
the exact condition (1.3).

### Corollary 1.3 (finite run transducer)

The maps (1.3)--(1.4) are associative because they reconstruct the literal
collar of concatenation.  Equivalently, each coordinate has the exact state
space

\[
                     \{\partial,0,1,\ldots,h\},       \tag{1.6}
\]

where `h` means "at least `h`" and `partial` means that the current positive
run began at the global left endpoint.  Start in `partial`.  On a `1`, a
state `j` increments with saturation at `h`, while `partial` stays
`partial`; on a `0`, states `1,...,h-1` reject and all other states become
zero.  At the end, every state is accepting, because a final open positive
run meets the global right endpoint.

This automaton is an exact linear-word test.  Initializing in zero or
requiring a terminal state in `{0,h}` incorrectly removes one or both global
endpoint exemptions.

## 2. The exact two-endpoint ledger

Use the standard Catalan notation

\[
 M={2m\choose m},\qquad
 N={2m\choose {m-1}},\qquad
 K=M-N=\operatorname {Cat}_m.
\]

An exact-palette Catalan path forest has `K` components and `2mK`
coordinate runs before joining.  Every Johnson seam between different
components merges exactly `m-1` runs.  Therefore a Hamilton **path**, using
exactly `K-1` seams, has

\[
                R_{\rm path}=(m+1)K+m-1              \tag{2.1}
\]

coordinate runs.

### Proposition 2.1 (exact boundary count)

A Hamilton path through all rank-`m` subsets of `[2m]` has exactly `2m`
boundary positive runs and hence

\[
             R_{\rm int}=(m+1)K+m-1-2m               \tag{2.2}
\]

internal positive runs.

#### Proof

Each endpoint is an `m`-set, so the two endpoint incidences contribute
`2m` boundary runs with multiplicity.  If the prefix and suffix occurrences
of one coordinate belonged to the same run, that coordinate would occur in
every middle vertex.  This is impossible because the Hamilton path visits
all rank-`m` sets, including sets which omit it.  Thus the `2m` endpoint
incidences are `2m` distinct boundary runs.  Subtract from (2.1). \(\square\)

If the internal run lengths are `a_i` and the boundary run lengths are
`b_1,...,b_{2m}`, the exact mass ledger is

\[
       \sum_i a_i+\sum_{j=1}^{2m}b_j=mM,
       \qquad a_i\ge h,\qquad b_j\ge1.               \tag{2.3}
\]

There is no lower bound `h` on the `b_j`.  A cyclic closure would add a
`K`-th seam, merge another `m-1` runs, and delete the endpoint exemptions;
it is a different problem.  In particular, a proof may use a Hamilton cycle
existence theorem and then delete an edge, but the accepted object and every
coverage audit must be the resulting linear path.

### Proposition 2.2 (exact occurrence-port topology)

Give each of the `K` path components two occurrence-labelled endpoint ports,
even when both ports belong to the same singleton middle vertex.  Let `R` be
the graph of legal connector seams between distinct components on these
`2K` ports.  A set \(S\subseteq E(R)\) joins the intact components into one
Hamilton path if and only if

1. `S` is a port matching of size `K-1`; and
2. after contracting the two ports of each original component, the edges of
   `S` form a connected graph.

In that event the contracted graph is automatically a path, and the two
ports unmatched by `S` are exactly the global endpoints.

#### Proof

A connector can use an endpoint port at most once, so every physical joining
gives a port matching.  A spanning linear joining uses `K-1` connectors and
is connected after component contraction.

Conversely, a port matching gives contracted degree at most two.  A connected
contracted multigraph on `K` vertices and `K-1` edges is a tree; a tree of
maximum degree two is a path.  Expanding its vertices by the original path
components gives one Hamilton path.  A matching of size `K-1` consumes
`2K-2` of the `2K` occurrence ports, leaving exactly its two ends. \(\square\)

This proposition is why ordinary component-graphic rank is not by itself an
exact connector condition: it does not impose the matching row on physical
ports.

### Corollary 2.3 (the exact two-endpoint Tutte row)

The port graph `R` has enough disjoint seams for a linear joining, namely a
matching of size at least `K-1`, if and only if

\[
                  o(R-U)\le |U|+2
                  \qquad(U\subseteq V(R)),            \tag{2.4}
\]

where `o` counts odd connected components.  Indeed, Tutte--Berge gives

\[
 \nu(R)=\frac12\left(2K-
       \max_{U\subseteq V(R)}(o(R-U)-|U|)\right).      \tag{2.5}
\]

The `+2` in (2.4) is precisely the allowance for the two globally unmatched
endpoint ports.  A cyclic closure would require the stronger perfect-matching
row with `+0`.  Condition (2.4) handles port capacity only; Proposition 2.2
still requires the selected matching to be connected after component
contraction.

## 3. Exact bounded-depth shadow service

Fix a maximum depth `r` and a finite debt bank `D`.  Its entries may be
written as `(q,lower,A)` or `(q,upper,A)`, where `1<=q<=r`.  A consecutive
window of `q+1` middle vertices serves the lower target given by their
intersection and the upper target given by their union.

For a word `P`, retain

\[
   \operatorname{pre}_r(P),\quad
   \operatorname{suf}_r(P),\quad
   \operatorname{Svc}_D(P),                            \tag{3.1}
\]

where the first two entries are the first and last at most `r` literal
vertices, and the last is the subset of `D` already witnessed inside `P`.

### Lemma 3.1 (service composition)

For two linearly concatenated words,

\[
 \operatorname{Svc}_D(PQ)=
 \operatorname{Svc}_D(P)\cup\operatorname{Svc}_D(Q)
 \cup\operatorname{Cross}_D(P,Q),                    \tag{3.2}
\]

where `Cross_D(P,Q)` is obtained from the literal windows

\[
       \operatorname{suf}_{a}(P),
       \operatorname{pre}_{q+1-a}(Q),
       \qquad 1\le a\le q,\quad q\le r,              \tag{3.3}
\]

whenever both pieces exist.  Hence

\[
 ({\cal R}_h,\operatorname{pre}_r,\operatorname{suf}_r,
   \operatorname{Svc}_D)                              \tag{3.4}
\]

is an exact associative finite collar.

#### Proof

Every window of `PQ` lies wholly in `P`, wholly in `Q`, or crosses their
unique new seam.  A crossing length-`q+1` window has the unique form (3.3),
and uses at most `q<=r` vertices from either side.  This proves (3.2).
Truncating the new literal prefix and suffix gives an exact update of
(3.1); associativity again follows from literal concatenation. \(\square\)

The literal collar is important.  A depth-`q` witness can cross as many as
`q` component seams when short components intervene.  A catalogue of
one-seam providers is therefore a sufficient restriction, not an exact
description of bounded-depth service.

If `|D|=b`, choose one final witness window for every debt target.  The union
of the seams crossed by these windows has at most

\[
                         \sum_{t\in D}q(t)\le br       \tag{3.5}
\]

edges and is a directed linear forest inside the final path.  Thus bounded
debt always has a bounded **service-core certificate**, even though the
number of other residence-balancing seams need not be bounded.

## 4. Exact Hall-one completion on the acyclic robust face

Take a residence-safe service core, concatenate each of its directed path
components, and contract them to nonempty oriented blocks `V`.  Assume:

1. an available arc `u->v` means that the exposed vertices are Johnson
   adjacent and the seam satisfies the context-robust condition (1.5);
2. every arc has already passed the fixed-decoration, private gap, linkage,
   and boundary-reachability tests, and those acceptances are
   selection-independent on this face; and
3. the resulting simple digraph `G=(V,A)` is acyclic, for example because
   every arc increases one fixed topological potential.

Let `B_G` be the bipartite graph with a left and right copy of `V`, and an
edge `u_L v_R` for every arc `u->v`.

### Theorem 4.1 (Hall-one path theorem)

Under the preceding hypotheses, the following are equivalent.

1. The blocks can be joined into one internally `h`-resident Hamilton path.
2. `B_G` has a matching of size `|V|-1`.
3. The Hall-one inequalities

   \[
                    |N^+(X)|\ge |X|-1
                    \qquad(X\subseteq V)              \tag{4.1}
   \]

   hold.

Every target served in the contracted service core remains served.

#### Proof

The bipartite deficiency formula gives

\[
 \nu(B_G)=|V|-\max_{X\subseteq V}(|X|-|N^+(X)|),      \tag{4.2}
\]

so items 2 and 3 are equivalent.  A matching gives every block at most one
selected successor and at most one selected predecessor.  Since `G` is
acyclic, the selected arcs form a disjoint directed path cover rather than
a union containing directed cycles.  A size-`|V|-1` cover has one component,
hence is a spanning path.  Conversely the arcs of a spanning directed path
form such a matching.

Every retained seam is context-robust, so repeated application of Theorem
1.1 preserves residence.  Joining blocks neither changes their internal
windows nor the service-core order, so its target witnesses survive.
\(\square\)

In the matching of Theorem 4.1, the unique unmatched right copy is the block
with no predecessor and the unique unmatched left copy is the block with no
successor.  They are the two global endpoints; there is no edge between
them in the accepted construction.

### Corollary 4.2 (prescribed endpoints)

For prescribed distinct start and end blocks `s,t`, there is a Hamilton
path from `s` to `t` if and only if

\[
 |N^+(X)\setminus\{s\}|\ge |X|
       \qquad(X\subseteq V\setminus\{t\}).            \tag{4.3}
\]

Indeed, this is Hall's theorem for a perfect matching from the left copies
`V\{t}` to the right copies `V\{s}`.  Acyclicity turns the matching into the
unique spanning path-cover component.

### Corollary 4.3 (directed Dirac sufficient condition)

The acyclicity hypothesis may be replaced by a density hypothesis when only
a sufficient theorem is wanted.  If a robust connector digraph on `n>=2`
contracted blocks has

\[
              d^+(v)\ge n/2,\qquad d^-(v)\ge n/2
              \quad(v\in V),                          \tag{4.4}
\]

then the directed Dirac--Ghouila-Houri theorem gives a Hamilton cycle.
Delete any one of its **residual** connector arcs.  The result is the desired
Hamilton path; the two vertices exposed by the deletion are its global
endpoints.  No wraparound shadow window or cyclic residence condition is
claimed.

For fixed `b,r`, one may enumerate the at most `br`-edge service cores from
(3.5), contract each, and apply either Theorem 4.1 or Corollary 4.3.  This is
an exact bounded enumeration followed by a polynomial test on the stated
robust-completion face.

The adjective *bounded* here means that both the debt cardinality `b` and
the maximum debt depth `r` are bounded.  Bounded cardinality alone does not
make the service core dimension-independent when its witness depths grow.

### Theorem 4.4 (one-seam debt partition--Hall min--max)

Retain the acyclic robust connector graph `G` of Theorem 4.1 and prescribe
distinct start and end blocks `s,t`.  Let `D_1` be a debt bank such that each
accepted witness is required to cross exactly one residual seam.  For an arc
`u->v`, let `Svc(u,v)` be the subset of `D_1` witnessed by its literal
prefix--suffix collar.

Put

\[
                  L=V\setminus\{t\},\qquad
                  R=V\setminus\{s\},\qquad n=|V|-1. \tag{4.5}
\]

For a map `psi:D_1->R`, retain the bipartite edge `u_L v_R` exactly when

\[
                 \psi^{-1}(v)\subseteq\operatorname{Svc}(u,v),          \tag{4.6}
\]

and call the resulting graph `G_psi`.  Then an internally `h`-resident
Hamilton path from `s` to `t` which services every member of `D_1` by one of
its selected seams exists if and only if

\[
 \boxed{
 \max_{\psi:D_1\to R}\ min_{X\subseteq L}
       \bigl(|L\setminus X|+|N_{G_\psi}(X)|\bigr)=n.}                  \tag{4.7}
\]

Equivalently, for some `psi`, every Hall row

\[
                       |N_{G_\psi}(X)|\ge |X|
                       \qquad(X\subseteq L)                           \tag{4.8}
\]

holds.  One seam may service an arbitrary number of debts in the same
fibre.  If `|D_1|=b` is bounded, (4.7) is decided by at most `n^b`
bipartite max-flow computations.  If the two global endpoints are not
prescribed, maximize additionally over the ordered pairs \(s\ne t\).

#### Proof

Fix `psi`.  The inner minimum in (4.7) is the bipartite matching min--max
formula, so it equals the maximum matching size of `G_psi`.  Equality with
`n` is therefore equivalent to a perfect matching from `L` to `R`.
Acyclicity turns that degree cover into one spanning path from `s` to `t`,
as in Corollary 4.2.  For every head `v`, its unique incoming selected seam
contains all debts in `psi^{-1}(v)` by (4.6), so all debts are served.

Conversely, take an accepted path.  For every debt choose one selected seam
which witnesses it and assign the debt to that seam's head.  The path's
connector matching is then contained in `G_psi` and saturates both shores,
proving (4.7).  Residence follows from the robust arc filter. \(\square\)

The theorem remains exact for a fixed nonrobust state-expanded catalogue:
replace each block by one frozen exact collar-state option, initialize the
root in the left-boundary state `partial`, accept every nonrejected terminal
state, and retain only state-equality arcs.  Unresolved alternative options
restore a colourful/partition correlation and are outside the two-shore
Hall formula.

### Corollary 4.5 (bipartite Dirac filler after reserved services)

Let the two shores in (4.5) have size `n`.  Suppose `p` pairwise
tail/head-disjoint arcs of `G` collectively service the whole debt bank,
with every reserved arc lying in \(L\times R\)--in particular, none has tail `t`
or head `s`.  Delete their `p` distinct tails and `p` distinct heads.  If
the residual balanced bipartite connector graph has minimum degree at least

\[
                              \left\lceil{n-p\over2}\right\rceil,       \tag{4.9}
\]

then the reserved arcs extend to the required Hamilton path.  In particular,
it is enough that the original filler graph have minimum degree at least
\(\lceil(n+p)/2\rceil\).

Indeed, a balanced bipartite graph on `q+q` vertices with minimum degree at
least `q/2` satisfies Hall: for `|X|<=q/2`, its neighbourhood has size at
least `q/2`; for `|X|>q/2`, a missed right vertex would have degree at most
`q-|X|<q/2`.  Apply this with `q=n-p`, unite the resulting matching with the
reserved arcs, and use acyclicity as in Theorem 4.1.

### Theorem 4.6 (prepared private-socket graphic--gammoid face)

Let `A` be any already accepted residence-safe service forest and contract
its directed path components to `q` nonempty macroblocks, each exposing
exactly its two path-end ports.  Fix two distinct literal free ports
`p_- ,p_+` on distinct blocks as the intended global endpoints.  Let `E_A`
be the residual connector labels which

1. avoid `p_- ,p_+`;
2. are literal Johnson seams passing the context-robust run and shadow
   filters; and
3. pass the fixed-decoration, gap, linkage, and reachability guards on one
   prepared common face.

Let `M_C^A` be the graphic matroid of their macroblock edges.  Assume the
prepared socket/resource relation is genuinely a gammoid `M_L^A` whose
independent sets are **exactly** the jointly realizable port-disjoint label
sets, including the compatible traversal/orientation from `p_-` to `p_+`
and every shared H0--H5 linkage/reachability resource.  Then the following
are equivalent:

1. the service forest extends to one resident Hamilton path with global
   endpoints `p_- ,p_+`;
2. `M_C^A` and `M_L^A` have a common independent set of size `q-1`;
3. for every \(X\subseteq E_A\),
   \[
        r_C^A(X)+r_L^A(E_A\setminus X)\ge q-1.                      \tag{4.10}
   \]

#### Proof

Edmonds' theorem gives the equivalence of items 2 and 3.  A size-`q-1`
graphic-independent set spans all `q` macroblocks, because the cut
`X=E_A` forces graphic rank `q-1`.  Socket-gammoid independence makes its
seams port-disjoint.  Hence every block has degree at most two.  The
spanning tree is therefore a path.  Its `q-1` seams consume `2q-2` distinct
ports; since `p_- ,p_+` were forbidden and are distinct, precisely those two
remain as the global endpoints.  The prepared filters preserve residence,
the service core, decoration, and linkage.

Conversely, the residual seams of such a path are a graphic spanning tree
and are jointly realizable by the declared socket gammoid, giving item 2.
\(\square\)

If `M_L^A` is represented by one fixed vertex-capacitated router `N`, let
`K_Y` retain exactly the component edges whose label sources still reach the
sink bank after deleting router vertices `Y`.  The rank family (4.10) then
collapses exactly to

\[
                         c(K_Y)\le |Y|+1
                         \qquad(Y\subseteq V(N)),                     \tag{4.10a}
\]

by the router-resilience theorem.  This replacement is valid only because
the same prepared gammoid already represents the joint selectable labels.

The gammoid hypothesis is a real restriction, not terminology.  General
two-port seam-disjoint sets are graph matchings and fail matroid exchange:
on consecutive port pairs `12,23,34`, the independent sets `{23}` and
`{12,34}` admit no exchange from the larger to the smaller.  Outside a
private/aligned representation, use the Tutte--Berge port row and correlated
connectivity/service state instead of (4.10).

### Corollary 4.7 (coherent transparent merge supply is separate)

On item 2189's private/aligned, reachability-redundant face, suppose a later
postrepair catalogue consists of actual **component-merging** all-six
incidence hexagons.  Retain a label only when its three lower ports have one
common external insertion label and its three upper ports have one common
external deletion label.  Require one and the same label set `S` such that

1. the component edges of `S` form a spanning tree;
2. the union of the forced ports of `S` extends to one joint alternating
   decoration by the residual forced-port gap--Hall matching; and
3. writing `K_Y^S` for the graph retaining those edges of `S` whose sources
   still reach the sink bank after deleting router vertices `Y`,
   \[
                       c(K_Y^S)\le |Y|+1
                       \qquad(Y\subseteq V(N)).                       \tag{4.11}
   \]

The coherent-hex theorem supplies local fixed-decoration transparency, the
forced-port matching supplies the common decoration, and (4.11) says that
all edges of the already chosen tree `S` are jointly routable.  Item 2189
orders that same tree.  Thus the exact transparent-merge supply target is

\[
 \boxed{
  \text{coherent merging edges}
  +\text{ one forced-port residual Hall witness}
  +\text{ router resilience}.}                       \tag{4.12}
\]

If the forced-port union of the **entire** catalogue already has one common
decoration, one may instead impose router resilience on the full ground and
let the common-basis theorem choose `S`.  Without that stronger preparation,
full-ground resilience plus a separately force-compatible tree does not
establish that the same tree passes both rows.

This corollary is not a statement about the physical Johnson connector arcs
of Theorems 4.1--4.6.  A transparent hexagon which merely rethreads one
Hamilton component has a loop as its component effect and supplies no edge
of the merge graph `K`.

## 5. Sharp scope obstructions

### 5.1 Endpoint exemptions make robust safety nonnecessary

Let `h=3`, and let `P=(X),Q=(Y)` be singleton paths with Johnson-adjacent
middle sets.  The two-vertex word `XY` has no internal positive run, so it
is residence-valid.  For each of the `m-1` common coordinates, however,
the robust sum in (1.5) is `1+1=2<3`.  The exact criterion (1.3) accepts
because both singleton `omega` bits are one.  Thus robust arcs are a clean
sufficient face, not a necessary condition for a linear answer.

### 5.2 Hall-one without acyclicity permits a cycle cover

Take three blocks `a,b,c` and only the arcs `a->b,b->a`.  For every
\(X\subseteq\{a,b,c\}\) one has `|N^+(X)|>=|X|-1`; the two arcs are a
size-two bipartite matching.  They form a directed 2-cycle and leave `c`
isolated, so no spanning path exists.  This is minimal: on two vertices a
size-one matching arc is already a spanning path.

Hence a Hall row by itself cannot replace the acyclicity/graphic or
reachability state.  This is the path analogue of the reciprocal boundary
arc obstruction after repair.

### 5.3 Graphic spanning rank alone does not impose a path

The three edges of the four-vertex star form a graphic spanning tree, but
the centre has degree three.  They cannot be connectors between intact path
components, each of which exposes only two ports.  A component-spanning
graphic basis must therefore be supplemented by port matching/degree-two
and no-cycle correlation.  On the preoriented DAG face Theorem 4.1 supplies
exactly that correlation; off that face it is not another ordinary graphic
rank row.

The separate literal fixture
`MATH_THEOREM_CATALAN_CONNECTOR_PORT_TUTTE_COUNTEREXAMPLE_20260731.md`
makes this obstruction sharp on a Johnson interface: six components have
complete contracted graph, fifteen individually robust seams, and a complete
abstract service-Hall projection, while their occurrence-port graph is
`K_2 sqcup K_{1,4} sqcup K_5` and has matching number four instead of the
required five.  Thus outside the preoriented face the first missing min--max
row is already Tutte--Berge on physical ports.

### 5.4 Marginal linkage filtering is conditional

Theorem 4.1 treats palette, gap, gammoid linkage, and no-`H->T`
reachability as an exact selection-independent filter on connector arcs.
If two arcs compete for an internal linkage vertex, change each other's
fixed decoration, or change boundary reachability, their individually
accepted projections do not define `G`.  One must instead carry the
correlated collar state of the ordered-gluing theorem.  Hall-one must not be
applied to an unsound marginal compression.

### 5.5 Rethread certificates are not merge certificates

The repaired positive `ML(7)` cycle has six shared-decoration transparent
hexagons, but they are Hamilton rethreads.  All fifteen hexagons which split
that Hamilton cycle into two components have zero common componentwise
decoration, already failing the palette row.  They therefore provide no
positive component-merging catalogue for (4.11).  The positive `m=4`
component merge is the separate fixture of item 2171.

Accordingly, neither the 608 endpoint seams in the replay below nor the six
transparent `ML(7)` rethreads may be counted as coherent merge edges without
a literal component-effect audit.  The residence/connector and transparent-
merge catalogues can share boundary state, but their certificates are
logically distinct.

## 6. Consequence for the all-`m` programme

The all-`m` seam identity supplies aggregate residence margin, but it does
not imply any of the Hall rows (4.1), any Dirac degree bound, or the existence
of a bounded nonrobust residence core.  The exact sufficient induction target
exposed here is:

1. a Catalan path forest with exact immediate palettes;
2. an internally `h`-resident rethread;
3. a bounded literal service core covering the prescribed deep-shadow debt;
4. after contraction, either an acyclic context-robust catalogue satisfying
   Hall-one or a context-robust catalogue satisfying a Hamiltonicity theorem;
5. separately, a postrepair transparent **merge** catalogue satisfying the
   coherent-edge, forced-port Hall, and router-resilience rows (4.12), with
   no rethread label silently counted as a merge;
6. private/aligned fixed-decoration and linkage data for every retained
   physical connector and transparent merge; and
7. the lower compiler on the resulting **linear** order.

The frozen `m=5` rethread supplies items 1--2 and a debt bank of size 21.
Items 2190--2191 now prove more than noncertification: its fixed 42 path
bodies cannot be joined on the endpoint-only residence face, even before
the 21 deep debts.  A further interior/socket actuator is necessary before
Theorems 4.1 or 4.4 can succeed on that base.  Separately, the finite
repaired `ML(7)` rethread census does not supply item 5; item 2171 remains
the positive merge fixture.

## 7. Replay

Run

```text
python3 scratch/audit_catalan_linear_path_collar_interface_20260731.py
```

against the frozen `m=5` residence-clean forest.  It checks (1.3)--(1.4)
and (3.2) literally on all 608 oriented Johnson endpoint seams.  The replay
finds 138 exact two-fragment-safe seams and 114 context-robust seams, and
also verifies the three-vertex Hall-one counterexample.

The frozen replay JSON is
`scratch/catalan_linear_path_collar_interface_20260731.audit.json`, SHA-256
`9025af4bbb327c949a7ae6cb5403a3e07a47bae6e395041193d70dd75eda8188`;
its canonical payload SHA-256 is
`063592fbadb987548f5b0ee2aadb526f224dce40aae337f6370fd2686aa5b6bd`.

The sharp port obstruction is independently replayed in
`MATH_THEOREM_CATALAN_CONNECTOR_PORT_TUTTE_COUNTEREXAMPLE_20260731.md`,
SHA-256
`6f6187de002b8fbc1d0e2accbdc7cbe59863eb0ce6c623db4028b924b266b4bd`.

## 8. Authoritative scope inputs

This theorem uses, without broadening them:

* the all-`m` seam identity in
  `MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md`,
  SHA-256
  `e1e0ddae1289a91d6912e07e0b1e1ca7f2728eb1640e7f3c6e08b18d48e96d48`;
* the finite residence-clean forest and its endpoint-only no-go in
  `MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md`
  and
  `MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_SOCKET_DEAD_COMPONENT_NOGO_20260731.md`,
  SHAs
  `dcb9b98e02580202f6dc94eaa4c3c009afe1c0638feab48a31bdf9f3e6c9d82e`
  and
  `083dcb456e629a1fa8abb47797ba2ade17ce8fe108d007bc444a4e80b3093cfc`;
* the router-resilience criterion
  `MATH_THEOREM_CATALAN_TRANSPARENT_ROUTER_RESILIENCE_CRITERION_20260731.md`,
  SHA-256
  `a1d57054a256a247a424171a31050f7060522257e266665cb414664c7b7874e0`;
* the coherent all-six local theorem
  `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`,
  SHA-256
  `3c4a3254f12acd8cf44cad8a9b4086f4e7e34d00bd325c26deaa5794f51228b1`;
  and
* the forced-port extension theorem
  `MATH_THEOREM_CATALAN_FORCED_PORT_GAP_HALL_20260731.md`, SHA-256
  `a33bbcc03fb9602030006c13ed0a2494679291dc7a3d2a7938555c02ab5d25f2`.
