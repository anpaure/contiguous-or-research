# Protected upper-exact Catalan forests after a fixed geodesic bank:
# the forward atlas, graphic rank, pull-tree absorption, and the exact residual gate

**Date:** 2026-08-03  
**Scope:** pure all-parameter owner/immediate-upper mathematics  
**Status:** unconditional all-`m` rank and forward-atlas theorems; exact
conditional pull/absorber theorems; exact scoped SCD obstructions.  No finite
candidate evidence, all-width source chronology, compiler, or full all-`m`
construction is claimed.

## 0. Outcome

Put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

\[
 W=|\mathcal L|=|\mathcal O|,\qquad
 U=|\mathcal U|,\qquad
 C=W-U=\operatorname {Cat}_m.                       \tag{0.1}
\]

Fix `H` resource-disjoint pivot-rich collared geodesics of length `3d`.
When their predecessor incidences are a matching and

\[
                         3Hd\le m-1,                 \tag{0.2}
\]

they extend to a perfect predecessor matching `M_0`; their successor
incidences become `H` vertex-disjoint directed paths `P` with distinct upper
colours.  This is the fixed protected bank throughout the note.

The following progress is uniform in `m`.

1. **Graphic rank is globally full.**  For every perfect `M_0`, the complete
   rooted-link digraph is strongly connected.  Hence its graphic matroid has
   rank `W-1`, and every protected pivot forest `P` extends to a graphic
   spanning tree.  Graphic rank by itself is never the global obstruction.

2. **Every upper colour crosses every order in both directions.**  Choose any
   strict total order `phi` extending the directed paths of `P`.  Every
   `R in mathcal U` has at least one `phi`-increasing and one
   `phi`-decreasing rooted occurrence.  Thus the complete increasing atlas is
   simultaneously pivot-containing, upper-surjective, and a DAG for every
   `m`.

3. **The graphic and connector-cycle rows disappear on that face, but so does
   the apparent matching freedom.**  Inside the increasing atlas, the desired
   protected upper-exact Catalan forest plus its `C-1` connector path is
   equivalent to one set `Q` of `W-1` incidences which has distinct tails,
   distinct heads, contains `P`, and covers all `U` upper colours.  For a
   *fixed strict order*, however, such a set is forced to be the consecutive
   Hamilton path in that order.  Thus the genuine residual choice is the
   Hamilton order itself (or, equivalently, the full-atlas selector), not a
   positive-density matching inside one frozen forward atlas.

4. **A single upper-surjective cycle also collapses both stages.**  If a
   protected middle-level Hamilton cycle covers every upper colour, choose
   one representative of every colour, including `P`, and delete any
   nonrepresentative cycle edge.  The representatives are the upper-exact
   Catalan forest and the other `C-1` path edges are its connector tree.

5. **Absorption can be made rank-exact.**  When a closed gain-one packet has
   one protected-private macro-link after the background forest is
   contracted, simultaneous repair is exactly Rado's graphic rank system.
   If the macro-links are modes of a fixed prepared SCD/middle-level pull
   tree, this reduces further to ordinary Hall between missing tasks and
   pull-tree edges.  This is an exact all-`m` induction interface, not an
   assertion that the required physical modes already exist.

6. **Two canonical shortcuts remain closed.**  The lexical GMN factor plus
   its canonical pull tree has a positive upper-colour floor for `m>=12`.
   The standard four-row SCD paired-ear grammar has an independent rooted
   `z`-cut obstruction for every `m>=6`.  Hence neither construction may be
   cited as the missing protected host.

The live theorem is therefore smaller and sharper than a generic
``graphic forest'' statement: build a protected upper-surjective Hamilton
order in the full rooted atlas, or build a task-decorated protected pull
tree.  All graphic topology after either certificate is automatic.  A strict
order chosen in advance is only a certificate for one already specified
Hamilton path.

## 1. Rooted occurrence ground and the fixed pivot bank

Fix a perfect incidence matching

\[
                         M_0:\mathcal L\longrightarrow\mathcal O. \tag{1.1}
\]

For an incidence `e=LV` outside `M_0`, define

\[
 t(e)=L,\qquad h(e)=M_0^{-1}(V),\qquad
 u(e)=M_0(L)\cup V.                                  \tag{1.2}
\]

Thus `lambda(e)=t(e)->h(e)` is a rooted link and
`u(e) in mathcal U` is its immediate-upper colour.  Parallel and oppositely
oriented rooted occurrences remain distinct labelled elements.

Let

\[
 V^j_0,V^j_1,\ldots,V^j_{3d}\qquad(1\le j\le H)      \tag{1.3}
\]

be resource-disjoint pivot-rich geodesics, and put

\[
 L^j_i=V^j_i\cap V^j_{i+1}.                          \tag{1.4}
\]

Their predecessor and successor incidence banks are

\[
 P_0=\{L^j_iV^j_i\},\qquad P_1=\{L^j_iV^j_{i+1}\}. \tag{1.5}
\]

Assume the lower vertices, **all** owner vertices (including every terminal
owner), and transition upper colours are distinct across the whole bank.
Under (0.2), the protected
small-matching extension theorem gives a perfect `M_0` containing `P_0`.
For every such extension,

\[
 \lambda(P_1)=
 \bigcup_{j=1}^H
 (L^j_0\longrightarrow L^j_1\longrightarrow\cdots
   \longrightarrow L^j_{3d}),                       \tag{1.6}
\]

where the last rooted vertex is `M_0^{-1}(V^j_{3d})`.  Hence `P:=P_1` is a
directed forest and its upper colours are distinct.  Designate one of these
directed paths as the rooted pivot path; the other members of the fixed bank
are protected internal paths.

Only this owner/immediate-upper bank is used below.  The geodesic's
all-width monotone-insertion witnesses, residence collar, and lower rays do
not automatically survive an arbitrary global reordering; those rows need
literal occurrence transport in any later source theorem.

## 2. The complete rooted graph has full graphic rank

Let `Gamma(M_0)` be the directed multigraph on `mathcal L` containing all
arcs (1.2), and let `G` be its underlying labelled graphic matroid.

### Theorem 2.1 (strong rooted connectivity)

For every `m>=2` and every perfect `M_0`, `Gamma(M_0)` is strongly
connected.  Consequently

\[
                         r_G(E)=W-1.                  \tag{2.1}
\]

If `P` is any protected rooted forest, then

\[
            r_{G/P}(E-P)=W-1-|P|,                    \tag{2.2}
\]

so `P` extends to a graphic spanning tree.

#### Proof

The middle-level incidence graph is connected: on the rank-`m` shore one
may perform Johnson swaps, and the intervening rank-`m-1` intersection gives
the corresponding two-edge incidence walk.  Contract every edge of the
perfect matching `M_0`.  The resulting undirected multigraph is precisely
the underlying graph of `Gamma(M_0)`, so it is connected.

At a rooted vertex `L`, exactly one of the `m` incidence edges leaving the
lower set `L` belongs to `M_0`; the other `m-1` give outgoing rooted arcs.
Likewise, the owner `M_0(L)` has `m-1` other lower facets, giving `m-1`
incoming rooted arcs.  Hence every rooted vertex is balanced:

\[
                         d^+(L)=d^-(L)=m-1.           \tag{2.3}
\]

In the condensation DAG of a weakly connected balanced digraph, a source
strong component has no incoming arc.  Summing `d^+-d^-` over that component
shows it has no outgoing arc either.  Weak connectivity then forces the
condensation to have one vertex.  Thus `Gamma(M_0)` is strongly connected.

A connected graph on `W` vertices has graphic rank `W-1`, proving (2.1).
Every forest in a connected graph extends to a spanning tree; equivalently,
contracting its `|P|` independent edges gives (2.2).  \(\square\)

For the pivot bank, the available graphic rank after contraction exceeds
the upper-exact forest demand by exactly

\[
 (W-1-|P|)-(U-|P|)=C-1.                              \tag{2.4}
\]

Those `C-1` units are exactly the eventual connector-tree rank.  This
identity also shows what Theorem 2.1 does **not** prove: it gives no upper
representatives and no tail/head matching.

## 3. A universal pivot-containing forward atlas

Choose a strict total order `phi` on `mathcal L`.  Call an occurrence
`e` **forward** when

\[
                         \phi(t(e))<\phi(h(e)),       \tag{3.1}
\]

and write `E^+(phi)` for the forward occurrence ground.

### Theorem 3.1 (every upper colour has both orientations)

For every `R in mathcal U` and every strict total order `phi`, the
colour-`R` occurrence family contains at least one forward and at least one
backward rooted arc.

#### Proof

For each rank-`m` facet `T subset R`, put

\[
                         L_T=M_0^{-1}(T).             \tag{3.2}
\]

There is a unique `a_T in T-L_T`.  Define

\[
                         T^+=R-\{a_T\}.              \tag{3.3}
\]

Then `L_T subset T^+`, `T^+ ne T`, and the incidence `L_T T^+` has upper
colour

\[
                         T\cup T^+=R.                \tag{3.4}
\]

Its rooted arc is `L_T -> L_(T^+)`.  Thus the `m+1` facets of `R` carry a
loopless functional digraph `T mapsto T^+`.  Every finite functional
digraph has a directed cycle.  Along such a cycle a strict total order
cannot decrease on every arc and cannot increase on every arc.  The cycle
therefore contains both a forward and a backward occurrence.  \(\square\)

### Corollary 3.2 (protected upper-surjective DAG ground)

Choose `phi` to be any linear extension of the directed pivot forest `P`.
Then

\[
                  P\subseteq E^+(\phi),\qquad
                  u(E^+(\phi))=\mathcal U,           \tag{3.5}
\]

and every selected arc in `E^+(phi)` increases one common potential.

This closes, for every `m`, the simultaneous **availability plus graphic
orientation** row.  It does not choose distinct tails and heads.  In
particular, `E^+(phi)` is generally a large DAG, not an incidence matching.

The endpoint qualification is essential.  A common potential alone does
not make an arbitrary edge set a forest: `1->2,1->3,2->3` is a DAG whose
underlying graph is a triangle.  It becomes enough after tail and head
injectivity, because then every vertex on an undirected cycle would have
one incoming and one outgoing selected arc, making the cycle directed.

### Lemma 3.3 (fixed-order rigidity)

Write the rooted vertices as

\[
                         v_1<_\phi v_2<_\phi\cdots<_\phi v_W.
\]

If `Q subseteq E^+(phi)` has `W-1` edges and distinct tails and heads, then

\[
                         Q=\{v_i\longrightarrow v_{i+1}:1\le i<W\}. \tag{3.6}
\]

Consequently such a `Q` exists if and only if every consecutive rooted arc in
(3.6) is a legal occurrence.  It contains a protected arc only if the two
ends of that arc are consecutive in `phi`.

#### Proof

Tail/head injectivity gives indegree and outdegree at most one.  A component
containing an undirected cycle would therefore orient that cycle coherently,
contradicting strict increase of `phi`.  Hence `Q` is a forest.  Its `W-1`
edges make it connected, so it is one directed Hamilton path.  The vertices
along that path increase strictly in `phi`; because the path uses every
vertex, their order is exactly `v_1,...,v_W`.  This proves (3.6).  \(\square\)

Thus merely taking a linear extension of `P` is not enough for the complete
path: every component of `P` must appear as a contiguous block.  The union
over all strict orders is exactly the original family of directed Hamilton
paths, so the fixed-forward reformulation is a verification device rather
than a new selector theorem.

## 4. Exact collapse of the forest and connector stages

For an incidence set `Q`, let `r_t(Q),r_h(Q),r_u(Q)` be its ranks in the
tail, head, and upper-colour partition matroids.  Thus

\[
 r_t(Q)=|t(Q)|,\qquad r_h(Q)=|h(Q)|,\qquad
 r_u(Q)=|u(Q)|.                                      \tag{4.1}
\]

### Theorem 4.1 (forward-face protected Catalan path equivalence)

Fix `M_0`, `P`, and a linear extension `phi` as above.  The following are
equivalent.

1. Inside `E^+(phi)` there is a protected upper-exact rooted Catalan forest
   `Q_0 superset P` and `C-1` free-port connectors `Q_1` whose union is one
   directed spanning path whose first vertex is the first vertex of the
   designated protected pivot path.
2. There is `Q subseteq E^+(phi)` such that
   \[
   P\subseteq Q,\qquad |Q|=W-1,\qquad
   r_t(Q)=r_h(Q)=W-1,\qquad r_u(Q)=U,                \tag{4.2}
   \]
   and the first vertex of the designated pivot path is the unique vertex
   of indegree zero in `Q`.

Given Item 2, one obtains Item 1 by choosing the edges of `P` as the
representatives of their distinct upper colours, choosing one edge of `Q`
for every other upper colour, and calling the resulting `U`-edge set
`Q_0`; put `Q_1=Q-Q_0`.

#### Proof

In Item 2, the tail and head rank equalities say that `Q` is an incidence
matching missing one tail and one head.  If its underlying rooted graph had
an undirected cycle, tail/head injectivity would orient that cycle
coherently, contradicting the strict increase of `phi`.  Hence `Q` is a
forest.  It has `W-1` edges on `W` rooted vertices, so it is connected; the
degree conditions make it one directed Hamilton path.

The representative choice described after (4.2) is possible because
`r_u(Q)=U` and the colours of `P` are distinct.  The set `Q_0` is a subset
of a path, hence an incidence matching and a forest.  It has one occurrence
of every upper colour and

\[
                         c(Q_0)=W-U=C                 \tag{4.3}
\]

components.  The remaining set has

\[
                         |Q_1|=W-1-U=C-1              \tag{4.4}
\]

edges.  Deleting `Q_1` from the Hamilton path gives precisely the `C`
path components of `Q_0`; consequently the edges of `Q_1` join consecutive
components into their directed free-port Hamilton path.

Conversely, `Q=Q_0 dotcup Q_1` in Item 1 is a directed Hamilton path, has
distinct tails and heads, contains `P`, and covers every upper colour
through `Q_0`.  It therefore satisfies (4.2).  \(\square\)

Theorem 4.1 is an exact equivalence, but Lemma 3.3 shows that for fixed `phi`
its Item 2 is a deterministic consecutive-path check.  The genuine
colour--tail--head near-perfect matching lives in the full rooted atlas (or in
a coarse ordered-block atlas retaining internal choices).  Its
endpoint-feasible sets are not one matroid.  Even on an acyclic subground,
Indeed, with

\[
 a=1\to3,\qquad b=1\to4,\qquad c=2\to3,             \tag{4.5}
\]

both `{a}` and `{b,c}` have distinct tails and heads, but neither `b` nor
`c` augments `{a}`.  Thus an Edmonds/Rado theorem cannot be invoked for all
of (4.2) without an additional alignment.

One useful aligned face is exact.  Suppose every residual upper-colour menu
has one private tail, those tails are distinct and avoid `t(P)`, and all
candidates using protected heads are deleted before selection.  Then an
upper-exact forest containing `P` exists inside the forward atlas exactly
when

\[
 \left|\bigcup_{R\in A}h(E_R)-h(P)\right|\ge |A|
 \qquad(A\subseteq\mathcal U-u(P)).                  \tag{4.6}
\]

This is ordinary Hall from colours to heads.  Tail privacy gives the other
endpoint partition and the common potential gives graphic independence.
The head-private version is symmetric.

### Theorem 4.2 (fixed-forest connector rank and Hall collapse)

Fix one upper-exact `Q_0 subseteq E^+(phi)` and contract its `C` directed
path components.
Ignoring ports, a labelled connector bank has full graphic rank exactly
when

\[
                         r_{G_C}(E_{\rm conn})=C-1,   \tag{4.7}
\]

equivalently its component graph is connected.  With a prescribed
connector forest `J`, the exact rank condition is

\[
 r_{G_C/J}(E_{\rm conn}-J)=C-1-|J|.                 \tag{4.8}
\]

Now restrict to connector arcs increasing the same potential `phi`.  Let
`K_*` be the required initial component.  A physical connector path exists
exactly when the bipartite free-port graph satisfies

\[
 |N^-(Y)|\ge |Y|
 \qquad(Y\subseteq\operatorname {Comp}(Q_0)-\{K_*\}). \tag{4.9}
\]

For a protected connector path fragment `J`, first require that `J` is
itself forward and endpoint-independent and that it does not use `K_*` as a
destination.  Then delete its used source and destination copies and impose
the same Hall inequalities on the residual copies.

#### Proof

Equations (4.7)--(4.8) are the spanning-tree rank criterion in the graphic
matroid of the component multigraph.  Under the potential restriction,
Hall selects distinct outgoing ports for all nonroot incoming components.
The selected `C-1` arcs have distinct sources and destinations.  Along each
`Q_0` component, `phi` increases from its free incoming head to its free
outgoing tail.  A component cycle would therefore concatenate strict
increases along the components and their forward connector arcs and return
to its start, which is impossible.  Thus the connectors are a forest of
`C-1` edges on `C` vertices, hence one component path starting at `K_*`.
Necessity is immediate from any such path.
\(\square\)

The component endpoints and the connector atlas depend on the chosen
`Q_0`.  Therefore the exact two-stage quantifier remains

\[
 \exists Q_0\quad[
   \text{upper representative condition for }Q_0
   \ \wedge\ \text{connector Hall in }D(Q_0)].       \tag{4.10}
\]

Two separately feasible Hall systems do not justify an arbitrary first
choice.  Theorem 4.1 avoids (4.10) only by selecting the complete path `Q`
at once.

## 5. The single-cycle and transparent-pull route

### Theorem 5.1 (upper-surjective cycle birth)

Let `S` be an occurrence-labelled incidence matching whose rooted links
form one spanning directed cycle.  Assume

\[
 P\subseteq S,\qquad u(S)=\mathcal U,                 \tag{5.1}
\]

and the upper colours on `P` are distinct.  Then there are sets
`Q_0 superset P` and `Q_1` such that

* `Q_0` is an upper-exact rooted Catalan forest with `C` components;
* `|Q_1|=C-1`; and
* `Q_0 dotcup Q_1` is one directed Hamilton path containing `P`.

If a particular cycle edge `e_* notin P` is required as the opening, the
same conclusion holds with `S-e_*` exactly when another occurrence of
`u(e_*)` survives.  In particular, the designated pivot path becomes the
global prefix when `e_*` is its entering cycle edge.

#### Proof

Choose the protected edge of `P` as representative for each of its upper
colours, and choose one edge of `S` for every remaining colour.  Call the
`U` representatives `Q_0`.  Since `U<W`, `Q_0` is a proper subset of one
cycle and hence a forest; it has `C=W-U` components.

Choose `e_* in S-Q_0` and set

\[
                         Q_1=S-Q_0-e_*.              \tag{5.2}
\]

Then `|Q_1|=C-1`, and `S-e_*` is one directed Hamilton path.  Contracting
the components of `Q_0` makes `Q_1` their connector path.  A prescribed
`e_*` can be excluded from `Q_0` precisely when its colour has another
occurrence.  \(\square\)

This is the strongest clean SCD/middle-level target: construct a
pivot-containing upper-surjective Hamilton cycle with a safe duplicate at
the intended opening.  Middle-level Hamiltonicity alone does not imply the
upper-surjective clause.

### Corollary 5.1a (fixed-forest one-cycle opening)

Let `Q_0 superset P` already be an upper-exact directed path forest with
`C` components, and let a free-port matching `R` make `Q_0 dotcup R` one
directed cycle.  Then, for every `e in R`,

\[
                         Q=Q_0\cup(R-\{e\})          \tag{5.3a}
\]

is a directed Hamilton path.  After contracting `Q_0`, the bank
`R-\{e\}` is a connector spanning tree and

\[
                         r_{\rm gr/Q_0}(R-\{e\})=C-1. \tag{5.3b}
\]

Every selected upper occurrence and every protected edge survives
literally.  Only the endpoint, source, and compiler legality of the chosen
opening `e` remains to be checked.

#### Proof

Deleting one edge from a directed spanning cycle gives a directed spanning
path.  The `C-1` remaining free-port edges connect all `C` contracted
`Q_0` components without a cycle, hence form their graphic basis.  No edge
of `Q_0` is changed.  \(\square\)

For a two-factor `F` with `q` components, let a certified binary pull join
two components without splitting another.  Its **macro-edge** joins those
two component vertices.  If a pull family is hereditarily available in a
parent-before-child order, then a set of pulls merges `F` to one component
exactly when its macro-edges form a graphic basis:

\[
                         r_{\rm pull}(T)=q-1.          \tag{5.3}
\]

Every protected occurrence and upper task must either be avoided or
transported by an explicit occurrence bijection.  Palette equality without
occurrence transport is not transparency.

### Theorem 5.2 (decorated prepared-pull-tree absorber)

Let `F` be a spanning two-factor containing `P`, and let `T` be a fixed
tree on its `q` factor components.  Root `T` and assume that every tree edge
`z` has a family of physical pull modes with the following properties.

1. Every mode replaces the same installed local off state, has the same
   macro-edge `z`, external phase and ports, returns every declared non-task
   resource/state, avoids the complete protected footprint, and is a strict
   merger in the fixed parent-before-child order.
2. Every `z` has one fixed neutral mode preserving the complete eligible
   upper-task multiplicity vector.
3. A gain mode labelled by a missing task `R` has delta exactly `{R}` on
   the initially missing-task shore, preserves a fixed reserve occurrence
   of every old task, and preserves every gain installed in another module.
4. One module uses one mode and is credited with at most one primary missing
   task; within this construction class, a missing task is counted as
   repaired only by a mode for which it is primary.
5. For every task--tree-edge adjacency below, one concrete gain mode is
   fixed in advance.  Every matching of such adjacencies, completed by
   neutral modes on the unused tree edges, is a simultaneously legal
   one-mode-per-module assignment, and every later pull remains literal for
   every earlier mode choice.

Make the bipartite graph `B_T` joining a missing task `R` to a tree edge
`z` when the universally compatible fixed gain mode in Item 5 exists.
Within this declared construction
class, a protected upper-covering Hamilton factor exists if and only if

\[
                         |N_{B_T}(A)|\ge |A|
             \qquad(A\subseteq\mathcal H),           \tag{5.4}
\]

where `mathcal H` is the missing-task set.  Its exact residual defect is

\[
          \max_{A\subseteq\mathcal H}(|A|-|N_{B_T}(A)|). \tag{5.5}
\]

#### Proof

Hall selects distinct tree edges for all missing tasks.  Use the
corresponding gain mode on those edges and the neutral mode on every other
edge of `T`.  The complete macro-edge set remains exactly `E(T)`, so it has
graphic rank `q-1`; hereditary strictness merges all factor cycles into one.
Private resource closure and the fixed reserves preserve every old task,
while the gain modes supply all missing tasks.  The pivot bank is avoided
literally.

Conversely, in the stated one-primary-task/one-mode construction class,
different repaired tasks must be assigned to different tree modules.  Their
assignment is a matching in `B_T`, so Hall is necessary and (5.5) is its
deficiency formula.  \(\square\)

Let `b` be the number of ineligible turns in the resulting Hamilton cycle.
Let `p_cut` be the number of turn positions forbidden as an opening by the
**complete** protected footprint, including the `3Hd` pivot turns, fixed
reserve occurrences, and any pull/packet state which must survive literally.
If every upper task occurs and `W-b>U`, then at least

\[
                         C-b+1                       \tag{5.6}
\]

eligible occurrence positions belong to repeated task classes.  Therefore,
if

\[
                         C-b+1>p_{\rm cut},           \tag{5.7}
\]

one redundant occurrence lies outside the complete cut-forbidden bank.
Deleting its
nonpredecessor incidence opens the cycle without losing an upper task or a
pivot edge.  Theorem 5.1 then identifies the upper-exact Catalan forest and
connector tree inside that path.

In the bare owner-layer specialization where the pivot is the only
cut-forbidden bank, `p_cut=3Hd`.  It is unsound to use that smaller value
when absorber modes or reserve witnesses add protected turn positions.

This counting argument guarantees protected containment, not a prescribed
pivot prefix.  To make the designated pivot path the prefix, its unique
entering cycle edge must itself be an eligible redundant provider (and pass
the declared physical cut guards); one then opens at that particular edge.

Theorem 5.2 is an exact all-`m` interface.  Its missing Boolean statement is
to co-locate gain-one modes with a prepared SCD/middle-level pull edge while
preserving macro signature, phase, inverse persistence, occurrence reserves,
and complete-footprint privacy.

## 6. Graphic-Rado absorption before a pull tree

There is a second exact form when repair packets are selected before the
topology basis is fixed.

Let `F^- superset P` be a prepared spanning forest containing one installed,
pairwise-private off-fragment `D_i` for every missing task `i in I`.  An
option `A_(i,a)` replaces `D_i`.  For a partial transversal `X`, put

\[
 F_X=\left(F^- -\bigcup_{(i,a)\in X}D_i\right)
                  \cup\bigcup_{(i,a)\in X}A_{i,a}.   \tag{6.0}
\]

Assume the complete physical option system has **unit-link normal form**:

1. every option is closed, supplies exactly the target resource of `i`,
   preserves fixed old-task reserves, and avoids the complete protected
   footprint;
2. every partial transversal `X` is a legal simultaneous replacement in
   all phase, tail/head, capacity, and non-topological rows;
3. `|F_X|=|F^-|+|X|`; and
4. there is one labelled quotient graph `Gamma` and one nonloop macro-edge
   `ell(i,a)` per option such that, for **every** partial transversal,
   \[
   r_{\rm gr}(F_X)-r_{\rm gr}(F^-)
        =r_{\rm gr,Gamma}(\{\ell(i,a):(i,a)\in X\}). \tag{6.0a}
   \]

Pairwise-disjoint two-attachment internal corridors are sufficient for
Item 4 only when every off/on replacement also has the same internal
relative rank and attachment partition, plus exactly the displayed new
two-component link.  The all-transversal identity itself is the
load-bearing hypothesis.  Let `L_i` be the parallel-labelled macro-edge
family of task `i`.

### Theorem 6.1 (protected unit-link Rado absorber)

One option per task can be selected so that the physical union remains a
forest containing `P` if and only if

\[
 r_{\rm gr}\!\left(\bigcup_{i\in J}L_i\right)\ge |J|
                         \qquad(J\subseteq I).        \tag{6.1}
\]

The maximum number of simultaneously absorbed tasks is

\[
 \min_{J\subseteq I}
   \left(|I-J|+r_{\rm gr}\!\left(\bigcup_{i\in J}L_i\right)\right). \tag{6.2}
\]

Every forest-compatible selection of `s` tasks lowers the component count
by exactly `s`.

#### Proof

By (6.0a), a partial transversal leaves a forest precisely when its
macro-edges are independent: `F^-` is a forest, and Item 3 says that every
selected option contributes one net physical edge.  Thus the problem is
exactly an independent transversal of the families `L_i` in the graphic
matroid of `Gamma`.  Rado's theorem gives (6.1), and its deficiency form
gives (6.2).  For an independent `s`-set, (6.0a) raises literal graphic rank
by `s`; on the fixed spanning vertex set this lowers the literal component
count by exactly `s`.  \(\square\)

If the options for `J` touch only `v_J` quotient vertices and induce
`kappa_J` nontrivial component blocks, then

\[
 r_{\rm gr}\!\left(\bigcup_{i\in J}L_i\right)
                       \le v_J-\kappa_J.             \tag{6.3}
\]

Thus every successful connected `|J|`-task absorber must reach at least
`|J|+1` quotient components.  An option whose two attachments project to
one quotient vertex is a loop and earns no rank, regardless of how many
literal packet realizations it has.

If all macro-links lie in a fixed forest backbone `T`, define the
**deduplicated** list

\[
 \overline L_i=\{e\in E(T):
      \text{task }i\text{ has a fixed clean realization of }e\}. \tag{6.3a}
\]

Choose the listed realizations so that the all-transversal hypotheses above
hold.  Then (6.1) is ordinary Hall from tasks to distinct underlying edges
of `T`.  A convenient sufficient condition is:

\[
 \min_i |\overline L_i|\ge\lambda,\qquad
 \max_{e\in E(T)}|\{i:e\in\overline L_i\}|\le\mu,\qquad
                         \lambda\ge\mu\ge1.          \tag{6.4}
\]

Indeed, double counting task--edge incidences gives
`lambda|J|<=mu|N(J)|`.  If every frozen protected resource deletes at most
`Delta` **distinct underlying backbone links** from one task list, a
pre-protection deduplicated list size `lambda_0` remains sufficient under

\[
                         \lambda_0-|P_{\rm res}|\Delta\ge\mu. \tag{6.5}
\]

Raw absorber multiplicity cannot replace these quantities.  In particular,
the canonical gain-one catalogue size `2(m-1)(m-2)` and its literal resource
load `2(m-1)` do not prove (6.4): many packets may contract to parallel
copies of one macro-edge and have total graphic rank one.

The unit-link and privacy hypotheses are load-bearing.  Bundles of several
edges do not form a matroid in general, and a degree cap coupled across
packets also destroys the augmentation axiom.  Those cases require a
separate physical selector, not the Rado conclusion (6.1).

### Lemma 6.2 (local cycle-to-path rectangle absorber)

Suppose a connector partial permutation contains one nontrivial directed
path and one directed cycle.  Choose a path arc `b->b'` and a cycle arc
`a->a'` so that the complete old/new four-arc footprint is disjoint from
the protected bank.  Delete the two old arcs.  If the clean cross arcs

\[
                         a\to b',\qquad b\to a'       \tag{6.6}
\]

are legal, replacing the two old arcs by the two cross arcs splices the
cycle into the path, preserves every tail/head capacity and both path
endpoints, and raises relative graphic rank by one.

#### Proof

After the untouched support is contracted, the opened old cycle is one
block while the deleted path arc separates the anchor path into two blocks.
The deleted cycle arc is therefore a loop of relative rank zero, and the
deleted path arc has relative rank one.  The two cross arcs successively
join the three blocks and have relative rank two.  The rank-transfer
identity gives gain one.  The displayed replacement uses the same two tails
and the same two heads, so endpoint capacities and the exterior path
endpoints are unchanged.  \(\square\)

Hereditary serial access to one clean rectangle per residual cycle is a
complete cycle absorber once a nontrivial anchor path exists.  A singleton
anchor needs a separate first-insertion base case.  SCD/ECO component
connectivity does not by itself supply these literal rectangles.

### Theorem 6.3 (exact protected connector rank transfer)

Let `B=Q_0 dotcup R` be a rooted cycle cover in which `Q_0` is the fixed
upper-exact protected forest and `R` is the remaining free-port matching.
Choose `D subseteq R`, `|D|=t`, put `T=B-D`, and let `A` be an endpoint-safe
replacement with `|A|=t`.  Here **endpoint-safe** means that `A` saturates
exactly the tails and heads freed by `D`, that `T union A` is again a rooted
cycle cover, that every added edge is a legal free-port connector disjoint
from `Q_0`, and that the full old/new footprint avoids or exactly returns
every protected resource.  Write

\[
             \rho_T(X)=r_{\rm gr}(T\cup X)-r_{\rm gr}(T). \tag{6.7}
\]

Then

\[
 \nu(T\cup A)-\nu(B)=\rho_T(D)-\rho_T(A),            \tag{6.8}
\]

where `nu(X)=|X|-r_gr(X)`.  If `D` meets exactly `h` old factor cycles and
the replacement has exactly `z` cycles on the touched vertices, then

\[
             \rho_T(D)=t-h,\qquad
             \rho_T(A)=t-z,\qquad
             \Delta c=z-h.                           \tag{6.9}
\]

In particular, an `h`-cycle-to-one absorber is exact precisely when

\[
                         \rho_T(A)=t-1.              \tag{6.10}
\]

No edge of `Q_0` is deleted because `D subseteq R`; all selected upper
occurrences and the protected pivot survive literally by the endpoint-safe
compatibility hypothesis on `A`.

#### Proof

Both terminal sets have the same cardinality.  Express their graphic ranks
relative to the common untouched support `T` and subtract their nullities;
this gives (6.8).  In each of the `h` touched old cycles, restoring its
deleted edges joins all broken path pieces with `d_j-1` rank units and uses
its last edge to close the cycle.  Summing gives `rho_T(D)=t-h`.  The same
count for the `z` new cycles gives `rho_T(A)=t-z`.  Substitution proves
(6.9)--(6.10).  \(\square\)

### Corollary 6.4 (`C_6` parity obstruction)

A connector-only, `Q_0`-avoiding, single alternating `C_(2s)` matching
toggle composes the rooted connector permutation by an `s`-cycle.  Therefore

\[
                         \Delta c\equiv s-1\pmod2.   \tag{6.11}
\]

In particular, every such `C_6` pull (`s=3`) preserves the parity of the
factor-cycle count.  A `C_6`-only descent can reach one cycle only if its
actual initial cycle count `c(R)` is odd.  If `R` is a componentwise
self-closure, so that `c(R)=C=Cat_m`, this condition becomes Catalan oddness.
Since

\[
             v_2(\operatorname {Cat}_m)=s_2(m+1)-1, \tag{6.12}
\]

this happens exactly when `m=2^q-1`.  For every other `m`, a complete pull
architecture from that componentwise start needs at least one
parity-changing module, such as an
endpoint-safe `C_8` pull, a matching-phase change with odd relative
connector permutation, or a direct path-opening operation outside the
cycle-only grammar.

#### Proof

The sign of an `s`-cycle is `(-1)^(s-1)`, whereas the connector permutation
on the `C` contracted `Q_0` components with `c` cycles has sign
`(-1)^(C-c)`.  Comparing signs before and after the pull gives (6.11).
Also

\[
 v_2\binom{2m}{m}=s_2(m),
\]

and subtracting `v_2(m+1)` from the Catalan quotient gives
`s_2(m)-v_2(m+1)=s_2(m+1)-1`.  This is zero exactly when `m+1` is a power
of two.  \(\square\)

## 7. What SCD and canonical pulls do—and do not—supply

The forward atlas of Section 3 is compatible with the SCD philosophy: one
common monotone order makes graphic independence automatic after endpoint
selection.  Raw SCD chains also keep distinct rank-`m` roots distinct before
component merging.  But Lemma 3.3 says a strict order on individual roots
leaves only its consecutive path.  An inductive construction must therefore
search over the order, or retain genuine internal choices inside coarse
ordered blocks; no positive-density matching remains in one frozen strict
atlas.

The standard four-row SCD seed and its long ears close the scalar upper and
lower palettes exactly, but the cross-facet owner maps need not be injective.
The fixed-`M_0`, exact-upper, palette-preserving retained-provider
two-stage short-ear packet grammar cannot repair the resulting rooted
connector cut.  With

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I_m=\operatorname {Cat}_m-2c
     ={2(m-2)\over m+1}c,                             \tag{7.1}
\]

the exact `z`-cut requires at least `I_m-1` active short-chain rethreads,
while there are at most `c`.  For every `m>=6`,

\[
 I_m-1-c={m-5\over m+1}c-1>0.                       \tag{7.2}
\]

Thus that exact resource-disjoint two-stage packet grammar is
all-dimensionally closed from `m=6` onward, independently of its anonymous
capacity-two projections.  This does not rule out a different short-ear
mode carrying additional typed cut credit.

For completeness, the still-open canonical two-provider marginal has an
exact all-`m` SCD normal form.  Write `u,d` for Dyck up/down steps.  Every
boundary demand has the unique successive-first-hit decomposition

\[
                         A\,d\,B\,d\,C\,d\,E,        \tag{7.3}
\]

with `A,B,C,E` Dyck words.  Its two canonical short providers are

\[
 uAuBdCdE,\qquad uAdBuCdE.                          \tag{7.4}
\]

Under the ordered-plane-forest dictionary, (7.4) is one **root-edge
slide**: choose a later root `y`, move it below the first root `x`, make the
intervening root forest the child forest of `y`, and make the old children
of `y` the following children of `x`.  Conversely every child of the first
root gives a reverse slide.  Hence a forest `F` has canonical-provider
degree

\[
 d_H(F)=(\#\text{ roots of }F-1)
        +(\#\text{ children of its first root}).     \tag{7.5}
\]

The anonymous capacity-two question for this marginal is exactly whether
every edge subfamily `Y` of the root-slide graph satisfies

\[
                         |Y|\le2|V(Y)|.              \tag{7.6}
\]

It remains open all-`m`; so does the larger unrestricted reverse
containment marginal.  The displayed slide is not the literal Dyck
right-arm/comb cover relation, and no graph isomorphism has been proved;
equality of their edge counts is insufficient.  Even a proof of (7.6)
would not repair the typed physical deficit (7.2).

The canonical lexical GMN route is also closed.  With `r=m-1`, the lexical
base factor misses `M_r` upper colours; a canonical incidence-hex pull can
create at most three formerly absent turn colours, and a pull spanning tree
uses at most `C_r-1` pulls.  Hence every resulting cycle misses at least

\[
                         M_r-3(C_r-1)>0              \tag{7.7}
\]

for every `r>=11`, i.e. `m>=12`.  Prescribing a protected pull forest only
reduces the available pull choices and does not invalidate this lower bound.

Accordingly, SCD/middle-level pulls remain useful in one precise role: a
prepared topology basis whose modes are already occurrence-transparent, or
whose task gains satisfy Theorem 5.2.  They cannot be credited with upper
repair from component connectivity alone.

## 8. Exact remaining all-parameter theorem

At the owner/immediate-upper level, either of the following would close the
protected Catalan forest plus connector path for every parameter in its
stated range.

1. **Hamilton-order/full-atlas route.**  For a correlated `M_0`, find a
   protected directed Hamilton path `Q` in the full rooted atlas which covers
   every upper colour.  Equivalently, find its vertex order `phi`; then `Q` is
   the forced consecutive path of Lemma 3.3 inside `E^+(phi)`.  Theorem 4.1
   provides the upper-exact Catalan forest and connector path with no separate
   graphic theorem.
2. **Prepared pull route.**  Build an upper-defective protected factor and a
   mode-rich transparent pull tree satisfying (5.4), followed by the safe
   opening inequality (5.7).  Theorems 5.1--5.2 then produce the same
   owner-layer object.

The exact unresolved correlation is therefore endpoint supply, not graphic
rank.  On the direct route it is the full-atlas three-partite
colour--tail--head matching together with elimination of permutation cycles.
On the pull route it is the physical
co-location of gain-one task modes with a protected, phase-valid,
hereditarily strict pull basis.

Finally, no owner-layer Hall theorem proves a literal all-width source
chronology.  Pairwise legal component overlap ports may identify source
addresses through a short intervening block.  A deeper theorem must carry a
globally consistent path automaton (addresses, cap state, pins, and clipped
owner history) or independently replay the complete final chronology.
