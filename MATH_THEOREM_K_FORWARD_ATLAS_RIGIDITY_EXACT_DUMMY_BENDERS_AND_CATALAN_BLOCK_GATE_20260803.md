# The forward-atlas gate after rigidity:
# exact dummy Benders, orbit/Latin limits, and the Catalan block interface

**Date:** 2026-08-03  
**Scope:** pure all-parameter mathematics on the rooted Boolean middle-level
occurrence ground.  No finite candidate calculation, approximate matching
theorem, endpoint-matroid assumption, or all-width source chronology is used.

## 0. Outcome

Fix `m>=2`.  Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

\[
 W=|\mathcal L|=|\mathcal O|,\qquad
 U=|\mathcal U|,\qquad
 C=W-U=\operatorname {Cat}_m .                    \tag{0.1}
\]

Fix a perfect predecessor matching `M_0` and a resource-independent protected
directed forest `P` whose upper colours are distinct.  The direct residual
problem is to extend `P` to a directed Hamilton path on `mathcal L` which
covers every colour in `mathcal U`.

The exact conclusions are these.

1. A strict forward order chosen in advance leaves no matching problem.  Its
   only possible endpoint-near-perfect selection is the consecutive path in
   that order.  Thus every protected path must be a contiguous interval, not
   merely respected by a linear extension.
2. The genuine selector lives in the full rooted atlas.  After fixing the two
   omitted endpoint copies, it is exactly a perfect matching in a
   colour--tail--head hypergraph with one token for each uncovered upper colour
   and `C-1` labelled dummy tokens.
3. Eliminating the dummy tokens gives an exact Benders theorem.  For a
   colour-to-head injection `eta`, extension is equivalent to

   \[
             b_\eta(X)\le |N(X)|-|X|\qquad(X\subseteq T).       \tag{0.2}
   \]

   Hence the exact deficit is

   \[
      \delta^*=\min_\eta\max_{X\subseteq T}
        \bigl(b_\eta(X)-(|N(X)|-|X|)\bigr)_+.                  \tag{0.3}
   \]

   This is zero exactly when the endpoint-near-perfect upper-surjective
   partial-permutation selector exists for the fixed omissions.  For fixed
   `eta`, separation is one ordinary bipartite min-cut.  Subtour elimination
   is still separate.
4. All zero-slack cuts compile exactly to Dulmage--Mendelsohn/alternating-SCC
   allowedness.  Positive-slack cuts are the irreducible joint correlation;
   individual endpoint allowedness is not sufficient.
5. The full atlas has strong exact expansion.  Every colour family `A` has

   \[
      \nu(E_A)\ge
      \left\lceil{(m+1)|A|\over m-1}\right\rceil
      =|A|+\left\lceil{2|A|\over m-1}\right\rceil.             \tag{0.4}
   \]

   After a protected bank of `p` arcs and the two omissions, every possible
   matching-rank obstruction is confined to

   \[
                  |A|\le p(m-2)+\left\lfloor{m-1\over2}\right\rfloor. \tag{0.5}
   \]

6. High symmetry does not turn the fixed-forward problem into a flow.  A
   strict order has trivial stabilizer; more generally, a group-invariant DAG
   with a nontrivial vertex orbit cannot contain a directed Hamilton path.
   Orbit averaging is exact fractionally, but an explicit abstract even-order
   loopless cyclic family has integral orbit margins and no integral literal
   lift.
7. Complement Latinization is an exact reformulation of the upper-exact
   forest, but its uniform fractional transversal does not lift by a generic
   Latin theorem.  The table is not Latin in the required sense, and forcing
   that property is already impossible in an infinite parameter class.
8. Every possible path obeys an exact integer colour coboundary and an
   all-subset skip-turn tensor.  Fixed-`M_0` endpoint-neutral literal pulls are
   exactly neutral in the aggregate coordinate vector of the colours.  Thus
   any induction has a typed boundary state which graphic rank cannot see.
9. The fixed pivot bank nevertheless causes no one-colour raw aperture
   obstruction: under `3Hd<=m-1`, every unused upper colour has a completely
   resource-free two-facet turn.  Simultaneously packing those turns remains
   the global difficulty.
10. In its audited planting range, the q1-neutral C8 input closes scalar
    topology parity.  More sharply, the Boolean endpoint graph is C4-free, a
    C6 cannot splice exactly two completed components, and an interlaced C8 is
    the smallest endpoint-neutral pairwise splice.  A support-disjoint
    interlaced-C8 spanning tree is an exact all-subtour absorber certificate.

The proof-safe route left open is therefore either a full-atlas literal
solution of (0.2), followed by the C8-tree or terminal-moving absorption of
Section 12, or a coarse ordered-block Catalan induction which carries the exact
endpoint and colour-coboundary state.  There is no nontrivial orbit
transportation or positive-density matching inside one frozen strict forward
atlas.

## 1. Rooted occurrence ground

For a nonmatching incidence `e=LV`, where

\[
        L\in\mathcal L,\qquad V\in\mathcal O,\qquad L\subset V,
        \qquad V\ne M_0(L),
\]

put

\[
 t(e)=L,\qquad h(e)=M_0^{-1}(V),\qquad
 u(e)=M_0(L)\cup V.                                \tag{1.1}
\]

The complete set of these labelled occurrences is the **full rooted atlas**
`E`.  Every rooted vertex has `m-1` outgoing and `m-1` incoming occurrences.
Every upper colour has exactly `m+1` occurrences.

Let `P subset E` have distinct tails, distinct heads, and distinct upper
colours, and suppose its rooted links form a directed forest.  Write

\[
                              p=|P|.                \tag{1.2}
\]

The desired complete owner-layer object is a set `Q superset P` satisfying

\[
 |Q|=W-1,\qquad |t(Q)|=|h(Q)|=W-1,\qquad
                         u(Q)=\mathcal U,            \tag{1.3}
\]

whose unique path component is required to contain every vertex.  Once this
holds, choosing one representative of each upper colour, with the protected
members chosen for their colours, gives the upper-exact Catalan forest; the
other `C-1` path edges are its connector tree.

## 2. A fixed strict forward atlas is rigid

Let `phi` be a strict total order on `mathcal L`, and retain only the
occurrences

\[
                         E^+(\phi)=\{e:\phi(t(e))<\phi(h(e))\}. \tag{2.1}
\]

The previously established colour-cycle argument remains useful: every upper
colour has both a forward and a backward occurrence for every `phi`.  It is
only an availability statement.

### Theorem 2.1 (consecutive-path rigidity)

Write

\[
                         v_1<_\phi v_2<_\phi\cdots<_\phi v_W.
\]

If `Q subseteq E^+(phi)` has `W-1` members and distinct tails and heads, then

\[
                   Q=\{v_i\longrightarrow v_{i+1}:1\le i<W\}. \tag{2.2}
\]

In particular, there is at most one such `Q`.

#### Proof

Tail/head injectivity gives indegree and outdegree at most one.  An undirected
cycle in `Q` would consequently be oriented coherently, which is impossible
because every selected arc strictly increases `phi`.  Thus `Q` is a forest.
It has `W` vertices and `W-1` edges, so it is connected and is one directed
Hamilton path.  Its vertex sequence is strictly increasing and contains every
vertex, hence is exactly `v_1,...,v_W`.  \(\square\)

### Corollary 2.2 (exact fixed-order test)

A fixed `phi` solves (1.3) if and only if

* every consecutive arc in (2.2) is a legal rooted occurrence;
* the consecutive colour list covers `mathcal U`;
* every protected arc is one of the consecutive arcs; and
* the designated root is `v_1`.

Thus a protected path must occur as a contiguous block.  Merely taking a
linear extension of `P` is insufficient.  Conversely, the union of the sets
(2.2) over all strict orders is exactly the family of directed Hamilton paths
in the full atlas.  Choosing `phi` after the path therefore restates, rather
than relaxes, the original problem.

## 3. Exact full-atlas dummy-token formulation

Fix an omitted tail `tau notin t(P)` and omitted head
`rho notin h(P)`.  Delete the protected endpoint copies and put

\[
 T=\mathcal L-(t(P)\cup\{\tau\}),\qquad
 H=\mathcal L-(h(P)\cup\{\rho\}),                  \tag{3.1}
\]

\[
 n=|T|=|H|=W-p-1,\qquad
 \mathcal C_0=\mathcal U-u(P),\qquad
 D=C-1.                                             \tag{3.2}
\]

Then

\[
                         |\mathcal C_0|+D=n.         \tag{3.3}
\]

Introduce `D` labelled dummy tokens `d_1,...,d_D`.  Form a tripartite
hypergraph on

\[
                         T\ \dot\cup\ H\ \dot\cup\
                         (\mathcal C_0\dot\cup\{d_1,\ldots,d_D\}).
\]

For every residual occurrence `e` whose tail and head lie in `T,H`, insert

* `(t(e),h(e),u(e))` if `u(e)` lies in `\mathcal C_0`; and
* `(t(e),h(e),d_j)` for every dummy `d_j`.

### Theorem 3.1 (exact dummy perfect matching)

The hypergraph above has a perfect matching if and only if there is an
endpoint-near-perfect, upper-surjective partial permutation satisfying the
three displayed equations in (1.3), containing `P`, and omitting the copies
`(tau,rho)`.  It need not yet be Hamiltonian.

#### Proof

A perfect hypergraph matching selects one residual occurrence at every tail
and head.  It uses exactly one occurrence of every uncovered actual colour;
the dummy-labelled occurrences account for the other `D=C-1` edges.  Adding
`P` gives `W-1` endpoint-independent occurrences and covers every upper
colour.

Conversely, from any extension choose one residual representative for each
colour in `\mathcal C_0`.  There are exactly `D` residual selected occurrences
left, and they may be bijectively labelled by the dummies.  \(\square\)

### Lemma 3.2 (path plus cycles)

Every endpoint-near-perfect selection supplied by Theorem 3.1 is the disjoint
union of exactly one directed path component and zero or more directed cycles.
Its graphic nullity is exactly its number of cycles.

#### Proof

Indegree and outdegree are at most one, so every component is a directed path
or cycle.  If there are `k` path components, the total number of edges is
`W-k`; (1.3) gives `k=1`.  Each cycle contributes one to nullity.  \(\square\)

This is the precise reason that the full-atlas selector is genuine while a
fixed forward selector is not: the full selector must also eliminate its
permutation cycles.

There is an exact fractional base on the unrooted cycle-first face.  Restore
both omitted endpoint copies and use `C` dummies rather than `C-1`, so all
three shores have size `W`.

### Proposition 3.3 (exact full-unrooted fractional selector)

The complete unprotected cycle-selector hypergraph has a fractional perfect
matching.

#### Proof

Give every actual-colour occurrence weight `1/(m+1)`.  Every actual token has
load one, while every tail and head receives

\[
                         {m-1\over m+1}={U\over W}.  \tag{3.4}
\]

For each of the `C` dummy tokens, give every one of the `W(m-1)`
occurrence-labelled copies weight `1/[W(m-1)]`.  This saturates that dummy and
adds `1/W` at every tail and head.  The total endpoint load is

\[
                         {U\over W}+{C\over W}=1.    \tag{3.5}
\]

\(\square\)

This audited semiregular point is scoped to the full unprotected, unrooted
cycle selector.  Root/terminal deletions and protected structural zeros may
destroy it, and it contains no subtour information.

## 4. Exact Benders elimination of the dummies

For `h` in `H` and `R` in `\mathcal C_0`, define

\[
 P_{hR}=\{t\in T:\hbox{the occurrence }t\to h
                         \hbox{ has colour }R\},    \tag{4.1}
\]

and let

\[
 P_h=\{t\in T:\hbox{there is a residual occurrence }t\to h\}. \tag{4.2}
\]

For `X subseteq T`, put

\[
 N(X)=\{h\in H:P_h\cap X\ne\varnothing\},\qquad
 s(X)=|N(X)|-|X|.                                  \tag{4.3}
\]

Choose an injection

\[
 \eta:\mathcal C_0\longrightarrow H,\qquad
                         P_{\eta(R),R}\ne\varnothing.          \tag{4.4}
\]

It specifies the head at which each actual token will be used; the other
heads receive dummy tokens.  Define

\[
 b_\eta(X)=
 |\{R:\eta(R)\in N(X),\ P_{\eta(R),R}\cap X=\varnothing\}|.   \tag{4.5}
\]

### Theorem 4.1 (exact source--column Benders theorem)

The injection `eta` extends to a perfect dummy-token matching if and only if

\[
                         b_\eta(X)\le s(X)
                         \qquad(X\subseteq T).        \tag{4.6}
\]

Equivalently, if `G_eta` is the bipartite tail--head graph in which the head
`eta(R)` keeps only the predecessors `P_{eta(R),R}` and every dummy head keeps
all of `P_h`, then

\[
 \delta(\eta):=\max_{X\subseteq T}(b_\eta(X)-s(X))_+
                         =n-\nu(G_\eta).             \tag{4.7}
\]

#### Proof

The neighbourhood of `X` in `G_eta` is obtained from `N(X)` by losing exactly
the `b_eta(X)` actual-token heads counted in (4.5).  Therefore

\[
                         |N_{G_\eta}(X)|=|N(X)|-b_\eta(X).      \tag{4.8}
\]

Hall's theorem turns `|N_{G_eta}(X)|>=|X|` into (4.6).  The equality (4.7) is
the bipartite matching-deficiency form of Hall's theorem.  \(\square\)

### Corollary 4.2 (sharp literal min--max)

Let the minimum range over the injections (4.4), and set it to infinity if no
such injection exists.  Then

\[
 \boxed{\quad
 \delta^*=\min_\eta\max_{X\subseteq T}
     \bigl(b_\eta(X)-(|N(X)|-|X|)\bigr)_+ .\quad}    \tag{4.9}
\]

The endpoint/colour selector exists exactly when `delta^*=0`.  For a fixed
`eta`, the inner maximum is a standard min-cut or maximum-matching
calculation; no claim is made that minimizing over `eta` is a network matrix.

An exact binary master uses variables `y_Rh`, with `y_Rh=0` when
`P_{hR}` is empty:

\[
 \sum_hy_{Rh}=1,\qquad \sum_Ry_{Rh}\le1,             \tag{4.10}
\]

\[
 \sum_{\substack{R,\ h\in N(X)\\P_{hR}\cap X=\varnothing}}
      y_{Rh}\le |N(X)|-|X|\qquad(X\subseteq T).       \tag{4.11}
\]

Equations (4.10)--(4.11) are an exact finite master, not an assertion that its
linear relaxation is integral.

## 5. Tight-cut compression and the positive-slack remainder

Assume the uncoloured residual endpoint graph

\[
                         G=(T,H;\{th:t\in P_h\})     \tag{5.1}
\]

has a perfect matching.  Call `X subseteq T` **tight** when
`|N(X)|=|X|`.  Tight sets are closed under union and intersection.  Moreover,
if `h` lies in both of two tight-set neighbourhoods, then it also lies in the
neighbourhood of their intersection.

For `h in H`, define its tight kernel

\[
 K_h=\bigcap\{X:X\hbox{ is tight and }h\in N(X)\}.  \tag{5.2}
\]

The family is nonempty because `T` belongs to it.

### Theorem 5.1 (zero-slack cuts are exactly allowedness)

For an endpoint edge `th`, the following are equivalent.

1. `th` belongs to some perfect matching of `G`.
2. `t in K_h`.
3. Deleting `t,h` leaves a graph satisfying Hall's inequalities.

Consequently, a colour--head pair `(R,h)` survives every zero-slack Benders
cut if and only if

\[
                         P_{hR}\cap K_h\ne\varnothing,          \tag{5.3}
\]

equivalently, it contains an endpoint edge belonging to a perfect matching.

#### Proof

For an edge `th`, Hall can fail after deleting `t,h` precisely when there is a
tight set `X` with `h in N(X)` and `t notin X`.  This proves the equivalence of
the first three statements.

Finite intersections of tight sets whose neighbourhoods contain `h` remain
tight and retain `h` in their neighbourhood.  Therefore a set `P_{hR}` meets
every such tight set exactly when it meets their intersection `K_h`.  The
zero-slack instance of (4.11) is exactly this condition.  \(\square\)

Given one perfect matching, the same allowed edges are recognized by the
usual directed alternating-SCC test: an edge is already matched, or its two
endpoint copies lie in one alternating strongly connected component.  Thus
all zero-slack rows compile to a literal deletion pass.  The inequalities with
`s(X)>0` are not implied by individual allowedness and remain genuinely joint.

A useful necessary localization is the following.  For `X subseteq T`, let
`J_X` be the bipartite graph from actual colours to heads, joining `R` to `h`
when `P_{hR}\cap X` is nonempty.  Since only `D` selected tails can carry dummy
tokens, every solution satisfies

\[
                         \nu(J_X)\ge |X|-D.          \tag{5.4}
\]

This is a pruning inequality, not a sufficient rainbow theorem.

## 6. Exact full-atlas endpoint expansion

For `A\subseteq\mathcal U`, let `E_A` be all rooted occurrences whose colour
lies in `A`, viewed as a bipartite graph between tail and head copies.

### Theorem 6.1 (colour-family matching-rank expansion)

For every nonempty `A`,

\[
 \nu(E_A)\ge
 \left\lceil{(m+1)|A|\over m-1}\right\rceil
 =|A|+\left\lceil{2|A|\over m-1}\right\rceil.       \tag{6.1}
\]

#### Proof

Each upper colour has exactly `m+1` occurrences, while the degree of every
tail and every head in the complete rooted atlas is `m-1`.  Hence
`|E_A|=(m+1)|A|` and `\Delta(E_A)\le m-1`.  By König's line-colouring theorem,
the edges of `E_A` split into at most `m-1` matchings.  One of them has the
size in (6.1).  \(\square\)

Delete the `p` protected tail and head copies and the omitted tail and head.
For a family `A\subseteq\mathcal C_0`, a protected tail deletion destroys at
most `m-2` `A`-edges: its protected outgoing edge has a colour outside `A`.
The same holds for a protected head.  Each omission destroys at most `m-1`
`A`-edges.  Therefore

\[
 |E_A^{\rm res}|\ge
 (m+1)|A|-2p(m-2)-2(m-1).                            \tag{6.2}
\]

### Corollary 6.2 (explicit large-family rank floor)

\[
 \nu(E_A^{\rm res})\ge
 \max\!\left(0,
 \left\lceil{(m+1)|A|-2p(m-2)-2(m-1)\over m-1}\right\rceil\right). \tag{6.3}
\]

In particular, `nu(E_A^res)>=|A|` whenever

\[
                         2|A|>2p(m-2)+(m-1).         \tag{6.4}
\]

Every failure of this matching-rank inequality is therefore confined to
(0.5).  The matching certified by (6.3) may repeat colours, so this is not a
rainbow-selector theorem.

Two exact unprotected endpoint facts sharpen the boundary further.

### Proposition 6.3 (unprotected colour projections)

When `p=0`, after deleting arbitrary omitted tail and head copies, the
actual-colour-to-head graph satisfies Hall; so does the symmetric
actual-colour-to-tail graph.

#### Proof

Put `a=|A|` and `d=m-1`.  The omitted tail removes at most one occurrence of
each fixed colour, hence at most `a` `A`-edges.  The omitted head removes at
most `d` further edges.  Thus at least

\[
                         ma-d                         \tag{6.5}
\]

`A`-edges survive.  Their maximum degree on either endpoint shore is `d`, so
either colour projection has at least

\[
 \left\lceil{ma-d\over d}\right\rceil
   =a+\left\lceil{a\over d}\right\rceil-1\ge a      \tag{6.6}
\]

neighbours.  This is Hall on both projections.  \(\square\)

### Proposition 6.4 (uncoloured omitted-endpoint criterion)

The complete uncoloured tail--head graph is `(m-1)`-regular, possibly
disconnected.  After deleting a tail `tau` and a head `rho`, it has a perfect
matching if and only if the two deleted copies lie in the same connected
component.

#### Proof

Different components would acquire opposite shore imbalances, proving
necessity.  In a connected regular bipartite component, every nonempty proper
left set has `|N(X)|>=|X|+1`; equality would isolate a balanced component.
Deleting one right vertex therefore preserves Hall for every proper left set.
All untouched regular components retain perfect matchings.  \(\square\)

Propositions 6.3 and 6.4 solve the two projections separately.  Their
correlation is exactly what (4.9) retains.

## 7. Why high symmetry does not yield the desired flow

### Theorem 7.1 (strict-order stabilizer collapse)

Every automorphism of `(M_0,phi,P)` fixes every rooted vertex and occurrence.
For coordinate-permutation automorphisms it is the identity on `[2m-1]`.

#### Proof

A finite strict linear order has no nonidentity automorphism, so every rooted
vertex is fixed.  Fixed ordered endpoints determine their unique occurrence
`L M_0(H)`.  The coordinate action on the nontrivial rank layer is faithful.
\(\square\)

There is a stronger obstruction to replacing `phi` by a symmetric DAG.

### Lemma 7.2 (an invariant DAG has no intra-orbit path)

If a finite group `G` acts on a finite DAG and `x,gx` are distinct, then no
directed path joins `x` to `gx`.

#### Proof

Translate a hypothetical path successively by powers of `g`.  Since `g` has
finite order, their concatenation is a directed closed walk and contains a
directed cycle.  \(\square\)

A Hamilton path makes every pair of vertices comparable by reachability.
Hence a `G`-invariant DAG containing one has only singleton vertex orbits.
Nontrivial symmetry can be retained only in the full cyclic atlas, in a weak
block potential with internal modes, or before an asymmetric opening.

There is one exact positive orbit theorem on the cycle-first face.  Suppose a
nontrivial cyclic deck group `C_g` acts freely and the rooted occurrence ground
is represented as a regular voltage cover of its quotient.  Choose a spanning
invariant one-in, one-out factor.  It is one literal Hamilton cycle if and only
if its quotient factor is one directed Hamilton cycle and the total voltage
`v in C_g` around that quotient cycle generates `C_g`.

Indeed, a quotient cycle of voltage `v` lifts to `g/ord(v)` cycles, each of
length multiplied by `ord(v)`.  Thus the lift is one cycle exactly when
`ord(v)=g`.  By contrast, a free invariant Hamilton **path** is impossible:
every invariant edge set has size divisible by `g`, whereas `W-1` is not.
Consequently a free-orbit construction must be cycle-first and then make one
explicit symmetry-breaking opening.  This criterion proves connectivity only;
colour coverage and pivot feasibility remain separate.  A one-copy protected
pivot is itself noninvariant unless its whole orbit is planted, and planting
that orbit is necessary rather than sufficient.

Orbit averaging does give an exact invariant **fractional** formulation.  If
`Omega` ranges over occurrence orbits and `A` over resource orbits, a constant
weight `z_Omega` produces the exact literal load

\[
                         \sum_\Omega d_{A\Omega}z_\Omega.       \tag{7.1}
\]

Integral orbit totals do not by themselves lift: the remaining fibre is

\[
 \{x\in\{0,1\}^{E}:Ax=b,\ Bx=n\}.                   \tag{7.2}
\]

Complete Cartesian orbit cells lift by partitioning the literal resource
blocks.  A private-resource face reduces exactly to bipartite transportation
only when every literal colour task owns a distinct literal tail and every
permitted task--head adjacency gives a legal triple with that owned tail.
Alternatively, a genuinely full Cartesian task--tail--head cell lifts.  Mere
pairwise completeness of the task--tail and task--head projections is not
enough: a three-way parity correlation may remain.  The Boolean atlas has
neither property in general, because an endpoint pair determines its one
colour.

### Theorem 7.3 (generic loopless orbit-lift obstruction)

For every even `n>=4`, take tail and head copies of `Z_n`, retain the arcs

\[
                         t\to t+1,\qquad t\to t+2,              \tag{7.3}
\]

and colour `t->h` by `t+h mod n`.  Diagonal translation preserves the ground;
the colours have two parity orbits.  Half-weight on all `2n` arcs gives literal
load one on every tail, head, and colour, and the two edge-orbit totals are the
integers `n/2,n/2`.  Nevertheless no integral endpoint-perfect selection uses
every colour once.

#### Proof

An integral selection is a permutation `pi` of `Z_n`.  If its colours are all
distinct, then modulo `n`

\[
 \sum_t(t+\pi(t))=2\sum_{t\in\mathbb Z_n}t=0,
\]

whereas the sum of all colours is `n/2`.  \(\square\)

This abstract even-`n` example is not a Boolean instance, whose coordinate
size `2m-1` is odd.  It proves that generic orbit balance, biregularity, and
fractional marginals do not imply a literal lift; it does not exclude a
Boolean-specific normality or integrality theorem.  Any such theorem must use
more than these marginal hypotheses.

## 8. The Latin-transversal route and its exact limit

Complement the fixed first matching `M_0` to the perfect incidence matching

\[
 \mu:{[2m-1]\choose m-1}\longrightarrow {[2m-1]\choose m},
 \qquad B\subset\mu(B),                              \tag{8.1}
\]

and write `mu(B)=B+alpha(B)`.  For a row
`C in {[2m-1] choose m-2}` and a column `B=C+{b}`, define the symbol

\[
                         A_\mu(C,B)=C+\{\alpha(B)\}.             \tag{8.2}
\]

### Theorem 8.1 (exact complement Latinization)

An upper-exact rooted Catalan forest is exactly a choice of one cell in every
row `C` such that

* the selected columns `B` are distinct;
* the selected symbols `A_mu(C,B)` are distinct; and
* the directed graph `B->A_mu(C,B)` is acyclic.

A protected owner geodesic whose predecessor incidences are installed in
`mu` becomes a prescribed directed path of cells.

This is a partial Latin transversal with a graphic condition, not a Latin
square.  For every fixed `mu`, weight `1/(m+1)` on every cell gives row load
one, column load `(m-1)/(m+1)`, symbol load at most `m/(m+1)`, and satisfies
every graphic-forest inequality.  Thus the relaxation is universally
feasible while the integral correlation remains.

The exact obstruction is structural: rows may repeat symbols.  Columns are
automatically symbol-injective, because for fixed `B` the symbol
`A_mu(B-{b},B)` uniquely misses `b` from `B`.  Requiring rows also to have the
natural local-Latin property would force a
Steiner system `S(m-2,m-1,2m-2)`: for a fixed symbol `a`, the columns `B` with
`alpha(B)=a` would have to cover every `(m-2)`-set avoiding `a` exactly once.
Every `(m-3)`-set would then lie in `(m+1)/2` such blocks, which is impossible
for every even `m>=4`.
The translation-covariant affine class
`alpha(B)=v+sum_{x in B}c_x` also fails incidence legality for `m>=4`.
Therefore ordinary Latin-square transversal theorems do not apply directly to
this table, and generic approximate transversal results are irrelevant to the
exact protected problem.  Full proofs of the equivalence, fractional graphic
rows, Steiner obstruction, and affine-class obstruction appear in
`MATH_THEOREM_BORN_LINEAR_COMPLEMENT_LATIN_PIVOT_AND_CYCLIC_QUOTIENT_20260801.md`.

## 9. Exact colour coboundary and the all-subset workload

Suppose a solution path is written as the alternating middle-level path

\[
 V_1-L_1-V_2-L_2-\cdots-V_W-L_*,                    \tag{9.1}
\]

where all `m`-sets `V_i` occur once, all `(m-1)`-sets except the terminal
`L_*` occur as intersections `L_i=V_i\cap V_{i+1}`,
`M_0(L_i)=V_i`, and `M_0(L_*)=V_W`.  Put

\[
                         R_i=V_i\cup V_{i+1}.        \tag{9.2}
\]

Let `q_R` be the number of indices with `R_i=R`; upper-surjectivity says
`q_R>=1`.  For a transition, write

\[
 V_i=L_i+\{x_i\},\qquad V_{i+1}=L_i+\{y_i\}.        \tag{9.3}
\]

For `S subseteq [2m-1]`, `|S|=j`, let `X_S` count the transitions for which

\[
 \{x_i,y_i\}\subseteq S,\qquad S-\{x_i,y_i\}\subseteq L_i.    \tag{9.4}
\]

Use the convention that an out-of-range binomial coefficient is zero, and put

\[
 K_j=2{2m-1-j\choose m-j}
       -{2m-1-j\choose m-1-j}
       -{2m-1-j\choose m+1-j}.                      \tag{9.5}
\]

### Theorem 9.1 (all-subset transition identity)

For every `S`,

\[
 \boxed{
 \sum_{R\supseteq S}(q_R-1)
  =K_j+\mathbf1_{S\subseteq L_*}
       -\mathbf1_{S\subseteq V_1}
       -\mathbf1_{S\subseteq V_W}+X_S .}           \tag{9.6}
\]

#### Proof

For one transition, inclusion--exclusion in
`R_i=V_i\cup V_{i+1}` gives

\[
 \mathbf1_{S\subseteq R_i}
 =\mathbf1_{S\subseteq V_i}+\mathbf1_{S\subseteq V_{i+1}}
  -\mathbf1_{S\subseteq L_i}
  +\mathbf1_{\{x_i,y_i\}\subseteq S,
             S-\{x_i,y_i\}\subseteq L_i}.          \tag{9.7}
\]

Summing uses every owner twice except the two endpoint owners and every lower
set once except `L_*`.  Subtracting the number
`{2m-1-j choose m+1-j}` of upper sets containing `S` yields (9.6).  \(\square\)

For a singleton `S={z}`, the last term is zero and (9.6) becomes

\[
 \sum_{R\ni z}(q_R-1)
  =2\operatorname {Cat}_{m-1}
    +\mathbf1_{z\in L_*}-\mathbf1_{z\in V_1}
                         -\mathbf1_{z\in V_W}.       \tag{9.8}
\]

Define the terminal added point

\[
                         a_*=V_W-L_*=M_0(L_*)-L_*.   \tag{9.9a}
\]

Then (9.8) is the vector identity

\[
 \boxed{
 \sum_R(q_R-1){\bf1}_R
 =2\operatorname {Cat}_{m-1}{\bf1}
   -{\bf e}_{a_*}-{\bf1}_{V_1}.}                    \tag{9.9}
\]

For an owner `m`-set `S`, the left side of (9.6) is nonnegative and
`K_m=3-m`.  Hence every solution obeys the local workload floor

\[
 \boxed{
 X_S\ge m-3+\mathbf1_{S=V_1}+\mathbf1_{S=V_W}.}     \tag{9.10}
\]

Thus every owner must be skipped by at least `m-3` selected upper-clique
turns, with one extra at either endpoint.  A reflected Gray code or SCD
recurrence which tracks only distinct intersections does not automatically
satisfy this tensor.

There is also an exact matrix form.  Let `mathsf T,mathsf H` be the tail and
head incidence matrices, `mathsf O` the owner-coordinate matrix,
`mathsf L` the lower-coordinate matrix, and `mathsf U` the upper-colour
coordinate matrix.  For every occurrence,

\[
                         \mathsf U
 = (\mathsf O-\mathsf L)\mathsf T+\mathsf O\mathsf H.          \tag{9.11}
\]

### Corollary 9.2 (fixed-`M_0` endpoint-neutral literal pulls are coordinate-neutral)

Every signed pull `z` satisfies

\[
 \mathsf Tz=\mathsf Hz=0\quad\Longrightarrow\quad
                         \mathsf Uz=0.               \tag{9.12}
\]

Thus, in one fixed-`M_0` occurrence ground, an endpoint-neutral literal SCD
absorber may redistribute colour identities only inside the kernel of the
colour-coordinate map.  This is coordinate-incidence neutrality, not equality
of the full `q_R` profile.  Any change in (9.9) must be paid for by an explicit
endpoint boundary, such as moving `L_*`.  A pull which changes or re-roots
`M_0` changes all four matrices and needs a separate occurrence-transport
identity.

The abstract repeat-colour degree vector (9.9) is itself feasible for every
`m>=3`: it has a realization by `(m+1)`-sets with multiplicity at most two.
Thus the sharp obstruction is not the unlabelled colour multiset; it is its
simultaneous realization by literal endpoint-compatible occurrences.  A full
proof of this bounded-multiplicity statement and the Smith-lattice form of
(9.11) is recorded in the companion orbit note.

## 10. A protected raw-turn aperture for every unused colour

Now let `P` arise from `H` resource-disjoint owner geodesics of length `3d`,
with distinct owner vertices, lower intersections, terminal predecessor roots,
and transition upper colours, where `d>=1`, and assume

\[
                              3Hd\le m-1.            \tag{10.1}
\]

### Theorem 10.1 (protected residual-turn aperture)

For every upper colour `R` not used by `P`, there are distinct `x,y in R`
such that the raw turn

\[
       (R-\{x\})\;--\;(R-\{x,y\})\;--\;(R-\{y\})   \tag{10.2}
\]

uses no protected owner vertex, transition lower intersection, or terminal
predecessor root.

#### Proof

Along one protected path, two owner facets of `R` cannot be consecutive,
because their transition colour would be `R`.  They cannot occur at distance
two.  If the middle owner were another `R`-facet, one of the adjacent colours
would be `R`; otherwise both adjacent lower intersections would equal the
intersection of the two `R`-facets, contradicting lower-resource
injectivity.  Hence one protected `3d`-edge path contains at most `d+1`
facets of `R`.

Let `a<=H(d+1)` be the total number of protected owner facets of `R`, and put
`r=m+1-a`.  There are `binom(r,2)` pairs of unprotected facets.  Among the
`3Hd` protected lower intersections, at least `2a-e` are incident with a
deleted facet, where `e<=2H` counts possible protected path endpoints.
There are also at most `H` terminal predecessor roots to avoid.  Therefore at
most

\[
                         b\le3Hd-2a+3H              \tag{10.3}
\]

protected lower sets can block pairs of surviving facets.

The difference `binom(m+1-a,2)-(3Hd-2a+3H)` is nonincreasing with `a` in the
present range, so it is smallest at `a=H(d+1)`.  There (10.1) gives

\[
                         r\ge Hd+2,\qquad b\le Hd+H, \tag{10.4}
\]

Since `Hd>=H`, one has `binom(Hd+2,2)>Hd+H`; hence
`binom(r,2)>b`.  Some pair yields (10.2).  \(\square\)

The theorem is deliberately pre-`M_0`: it proves that the protected bank does
not exhaust any single upper colour at the raw Johnson-turn level.  It does
not install all chosen predecessor incidences into one perfect matching and
does not pack turns for different colours simultaneously.

## 11. The exact coarse-block induction interface

The strict-order failure has one clean inductive repair.  Partition the rooted
vertices into nonempty blocks

\[
                         \mathcal L=B_1\dot\cup\cdots\dot\cup B_q,          \tag{11.1}
\]

allow a genuine internal occurrence ground `D_i` on each `B_i`, and allow
cross-block arcs only from `B_i` to `B_j` when `i<j`.

### Theorem 11.1 (ordered-block factorization)

A directed Hamilton path in this block-monotone ground exists exactly when
there are

* a directed Hamilton path through each internal ground `D_i`; and
* one legal connector from the terminal of the `B_i` path to the initial
  vertex of the `B_{i+1}` path for every `i<q`.

Every global path visits each block contiguously and visits the blocks in the
order `B_1,...,B_q`.

#### Proof

Block indices along a directed path are nondecreasing.  A spanning path cannot
leave a block and later return, so its intersection with each block is one
contiguous internal Hamilton path.  It must cross between each consecutive
pair of nonempty blocks.  The converse is concatenation.  \(\square\)

This is the exact place where an SCD/Catalan recurrence may retain symmetry:
the potential is strict only between blocks, while internal choices remain.
Each protected pivot path may be installed as a contiguous internal block; a
designated pivot is the global prefix only when it begins the internal path of
`B_1`.  The theorem is path-topological.  Upper-surjectivity additionally
requires, for every `R`,

\[
 q_R=\sum_i q_{i,R}
      +\sum_{i=1}^{q-1}\mathbf1_{u(c_i)=R}\ge1,      \tag{11.2}
\]

where `c_i` is the chosen connector, and every protected arc must be allocated
to one internal path or connector.  A valid recurrence must pass at least the
following boundary state:

* the initial and terminal rooted vertices and their literal resource copies;
* the protected entry/exit incidences;
* the upper-colour multiplicity vector subject to (9.6)--(9.10); and
* the endpoint-neutral trade class imposed by (9.11); and
* if `M_0` is built recursively, compatible predecessor assignments and owner
  image sets on all block interfaces.

Theorem 11.1 assumes one global fixed `M_0`; block paths built under unrelated
predecessor matchings cannot simply be concatenated.  Graphic-matroid rank
alone omits the typed rows above.  Theorem 10.1 supplies local colour apertures
for such a recurrence, but no all-`m` simultaneous block recurrence is
asserted here.

## 12. Boolean circuit absorption after the q1-neutral C8 rebase

The audited owner-layer input
`MATH_THEOREM_PROTECTED_COMMON_EXTERIOR_C8_ODD_SOCKET_AND_FORWARD_ORDER_COLLAPSE_20260803.md`,
SHA-256

\[
 \mathtt{82a5613de47fd99c7eb10ccdac9f1bab5bd2c8a7bded09dbb3839431c5f5b55d}, \tag{12.1}
\]

supplies a prospectively plantable common-exterior `C8` whose two phases have
the same immediate-upper multiset and opposite topology parity.  Hence scalar
odd-parity availability is no longer the issue.  The question is whether
literal circuits can be interlaced through the components of an actual
three-partite selector.

Let `Q` be a perfect dummy-token selector from Theorem 3.1.  Complete its
unique path by one **formal** terminal-to-root edge.  The resulting permutation
`hat Q` is a disjoint union of directed cycles.  The formal edge has no colour
token and will never be toggled.

### 12.1 Exact alternating-circuit calculus

Let `mathcal B(M_0)` be the bipartite graph on tail and head copies of
`mathcal L`, with

\[
             t h\in E(\mathcal B(M_0))
        \quad\Longleftrightarrow\quad
             t\subset M_0(h),\qquad t\ne h.          \tag{12.2}
\]

Relabelling a head `h` by its owner `M_0(h)` identifies this with the Boolean
rank-`(m-1)`/rank-`m` incidence graph after deleting `M_0`.

Take a literal alternating `C_{2s}` whose selected phase and replacement phase
are

\[
 e_i=t_i\to h_i,\qquad e_i'=t_{i+1}\to h_i
                         \qquad(i\bmod s).           \tag{12.3}
\]

Deleting the `e_i` cuts the affected completed components into directed
strands.  Define `theta in S_s` by

\[
 \theta(i)=j
 \quad\Longleftrightarrow\quad
 \hbox{the old strand beginning at }h_i
 \hbox{ ends at }t_j,                               \tag{12.4}
\]

and put `sigma(j)=j-1 mod s`.

### Theorem 12.1 (exact circuit component formula)

The number of old completed components touched by the circuit is
`c(theta)`.  After toggling to the replacement phase, their number is

\[
                              c(\sigma\theta).       \tag{12.5}
\]

#### Proof

Within each old component, its cut strands cyclically permute their freed
heads and tails, so the cycles of `theta` are exactly the old components.
After the strand from `h_i` reaches `t_{theta(i)}`, the new phase continues to
`h_{sigma(theta(i))}`.  The new completed components are therefore exactly the
cycles of `sigma theta`.  \(\square\)

A circuit toggle is a valid three-partite trade when its tokens can be
transported from the old phase to the new: an actual token `R` must land on a
new occurrence of colour `R`, while a labelled dummy may land on any new
occurrence.  Equality of the two literal upper-colour multisets is a sufficient
condition for every current actual/dummy token labelling to transport.
Every such fixed-`M_0` endpoint-neutral toggle is automatically neutral in the
coordinate aggregate by (9.11).  The common-exterior C8 is stronger: it
preserves the complete literal upper-colour multiset.

### Corollary 12.2 (sharp Boolean splice floor)

The graph `mathcal B(M_0)` is `C4`-free, because two distinct `(m-1)`-sets
cannot both be facets of two distinct `m`-sets.  Consequently:

1. no literal two-edge endpoint rectangle exists;
2. every nontrivial endpoint-neutral trade has support at least `C6`;
3. a `C6` with its three old edges in three distinct components has
   `theta=id` and merges `3` components to `1`;
4. a `C6` cannot merge exactly two components; and
5. an interlaced `C8`, whose old edges `e_1,e_3` lie in one component and
   `e_2,e_4` in another, has

   \[
      \theta=(13)(24),\qquad \sigma=(1432),\qquad
      \sigma\theta\hbox{ a four-cycle},             \tag{12.6}
   \]

   and therefore merges those two components into one.

For Item 4, a two-component `C6` has `theta` equal to a transposition and a
fixed point; multiplying by the three-cycle `sigma` again has two cycles.
Thus an interlaced `C8` is the smallest endpoint-neutral pairwise splice in
the literal Boolean selector.  Unlike the endpoint-moving bridge below, it
preserves both the root and terminal.

The physical circuit screen is also finite-symbolic.  Every simple Boolean
`C6` has the star form

\[
 L_i=A+\{x_i\},\qquad O_i=A+\{x_i,x_{i+1}\}
                         \quad(i\bmod3),             \tag{12.6a}
\]

with `|A|=m-2` and pairwise distinct petals `x_i` outside `A`.  Every simple
Boolean `C8` is either the analogous four-petal star, or the octahedral form

\[
 K+ac,\quad K+bc,\quad K+bd,\quad K+ad              \tag{12.6b}
\]

on the lower shore, with consecutive owners given by the unions,
`|K|=m-3`, and pairwise distinct `a,b,c,d` outside `K`.  The alternative
top-clique Johnson four-cycle is excluded because its consecutive owner unions
repeat.  Put `h_i=M_0^{-1}(O_i)`.  Both alternating phases are literal rooted
occurrences exactly when

\[
                         h_i\notin\{L_i,L_{i+1}\}
                         \qquad\hbox{for every }i.   \tag{12.6c}
\]

Their old and new literal colours are respectively

\[
 M_0(L_i)\cup O_i,\qquad M_0(L_{i+1})\cup O_i.       \tag{12.6d}
\]

Thus containment of the displayed old phase in the current `Q`, avoidance of
the formal edge, (12.6c), component interlacing, protected-footprint avoidance,
and a four-token matching from the old list to the new list are a complete
local C8 test when every token assignment outside this support is frozen.  If
global representative relabelling is allowed, failure of that local token
matching is not a global no-go.  The common-exterior theorem hash-bound in
(12.1) makes the two lists in (12.6d) equal as multisets, so its token test is
automatic.

### Theorem 12.3 (prepared interlaced-C8 tree absorber)

Let `mathscr C` be the completed components of `hat Q`.  Suppose a tree `T` on
`mathscr C` is equipped as follows.  For every tree edge `AB`, there is a
token-compatible literal `C8` satisfying:

* its old phase consists alternately of two selected arcs in `A` and two in
  `B`;
* its old phase avoids the formal edge and every protected arc of `P`; and
* the complete literal supports of the `C8` circuits for distinct tree edges
  are pairwise disjoint.

Then toggling the tree circuits in a leaf-contraction order turns `hat Q` into
one directed Hamilton cycle.  Deleting the untouched formal edge gives a
directed Hamilton path with the original root and terminal, containing `P`
and every actual upper-colour token.

#### Proof

At every step, the endpoints of the next tree edge lie in two distinct current
supercomponents: the previously toggled tree edges form a forest.  The four
old phase arcs split `2+2` between those supercomponents, so Corollary 12.2
merges them.  Full support disjointness leaves all unused circuit phases
available.  Token transport preserves the perfect three-partite matching, and
avoidance preserves `P` and the formal edge.  After `|mathscr C|-1` toggles one
completed component remains.  Removing the formal edge proves the claim.
\(\square\)

If a pre-reserved bank of pairwise support-disjoint interlaced C8s is given,
Theorem 12.3 reduces exactly to connectivity of its auxiliary graph on
`mathscr C`.  Without pre-reserved disjointness, the gate is a
support-disjoint spanning-tree problem, not ordinary flow.  The audited
common-exterior C8 makes each suitable planted socket token-compatible, but
does not prove the interlacing or spanning-tree supply.

### Corollary 12.4 (cycle-first safe opening)

The same theorem applies to an integral full-unrooted selector with `C` dummy
tokens: use its directed cycle components directly, without a formal edge.  A
support-disjoint interlaced-C8 tree produces one upper-surjective Hamilton
cycle.  Deleting any dummy-labelled, nonprotected cycle edge gives a directed
Hamilton path while retaining every actual upper-colour token.  A designated
protected pivot becomes the global prefix exactly when its entering cycle edge
is such a safe dummy (equivalently, its literal colour has another actual
representative after relabelling).

Thus Proposition 3.3 plus an **integral** selector and a C8 tree is a complete
cycle-first certificate.  The proposition alone supplies only its fractional
first row.

A looser prepared `{C6,C8}` hypertree gives the companion exact count.  If it
uses `n_6` joins of three fresh components and `n_8` joins of four, then

\[
                    |\mathscr C|-1=2n_6+3n_8.        \tag{12.7}
\]

The C8 input supplies the odd reduction; hence parity is closed.  For two
components specifically, the interlaced `2+2` C8 of (12.6), rather than a
loose four-component join, is the exact splice.

### 12.2 The endpoint-moving dummy bridge

There remains a cheaper terminal-free face.  The exact outgoing head aperture
of a terminal `z` is

\[
 N^+(z)=\{M_0^{-1}(z+\{x\}):x\notin z,\ z+\{x\}\ne M_0(z)\},
 \qquad |N^+(z)|=m-1.                               \tag{12.8a}
\]

Let a disjoint cycle contain a dummy-labelled edge `a->b`, and suppose
`b in N^+(z)`, equivalently the literal occurrence `z->b` exists.  Replace

\[
                         a\to b\quad\hbox{by}\quad z\to b.       \tag{12.8}
\]

The dummy label is transported to the new occurrence.  The cycle opens at
`b`, is appended to the path, and the new terminal is `a`.  Endpoint capacities
and the root are preserved, but the omitted tail changes from `z` to `a`.
Thus (12.8) is exact only when the final terminal is free; a prescribed
terminal requires the endpoint-neutral C8 mechanism or another return trade.
Writing `alpha(x)=M_0(x)-x`, its literal colour-coordinate change is exactly

\[
 {\bf1}_{u(z\to b)}-{\bf1}_{u(a\to b)}
             ={\bf e}_{\alpha(z)}-{\bf e}_{\alpha(a)},          \tag{12.8b}
\]

which is precisely the terminal-boundary change required by (9.9).

For a fixed physical `Q`, a representative forest containing `P` exists
exactly under the graphic Rado inequalities

\[
 r_{\rm gr/P}\!\left(\bigcup_{R\in A}F_R\right)\ge |A|
       \qquad(A\subseteq\mathcal C_0),               \tag{12.9}
\]

where

\[
 F_R=\{e\in Q-P:u(e)=R\}.
\]

When (12.9) holds, actual/dummy labels may be reassigned within `Q` so that
the actual-token edges plus `P` are a forest; every cycle then contains a
dummy-edge **candidate** for (12.8).  It is eligible only when its head `b`
also satisfies the literal bridge condition `z\subset M_0(b)` for the current
terminal `z`.  This is a conditional test on the selected literal `Q`, not a
post-hoc guarantee for every Benders solution.

Finally, the ordinary unweighted count of all labelled-dummy matchings is
divisible by `(C-1)!`, which is even for `m>=3`.  This observation says nothing
about symmetry-broken or weighted algebraic certificates, and the audited C8
already closes the separate topology-parity row.

## 13. Exact boundary of the progress

The following are now closed uniformly in `m`:

* fixed-strict-order rigidity and the collapse of its orbit symmetry;
* the exact full-atlas dummy-token formulation;
* the Benders min--max (4.9) and its zero-slack SCC compression;
* full-atlas colour-family endpoint expansion and the small-family obstruction
  floor (0.5);
* the failure of symmetry margins to imply a literal integral lift;
* the exact Latin reformulation and the reason a generic Latin theorem does
  not apply;
* the integer colour coboundary, all-subset workload, and endpoint-neutral
  fixed-`M_0` pull law;
* a resource-free raw turn for every colour outside the fixed pivot bank;
* the no-rectangle/C6 obstruction and the exact interlaced-C8 pairwise splice;
  and
* the prepared C8-tree absorber theorem, with the audited q1-neutral socket
  closing scalar topology parity in its planting range.

The all-parameter construction itself remains open.  It is exactly the
positive-slack part of (4.11), coupled either to a token-compatible
support-disjoint C8 spanning tree (or a terminal-splice chain), or equivalently
to an ordered-block Catalan recurrence carrying the typed boundary state of
Section 11.  Semiregularity, the expansion floor (6.3), and parity closure do
not by themselves produce that literal absorber bank.  No global no-go is
claimed, and no endpoint matroidality, approximate matching, or unproved
symmetry lift has been used.
