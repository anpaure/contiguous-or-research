# Prospective tight-pivot planting in the canonical GMN pull family:
# an exact coloured auxiliary-tree model and a linear upper-colour obstruction

Date: 2026-08-01  
Lane: R, prospective protected pivot / canonical pulls / owner-layer colour  
Status: exact formulation, conditional graphic--Rado theorem, and unconditional
construction-specific no-go for every `m>=12`.  No full contiguous-OR or
compiler theorem is claimed.

## 0. Outcome

The fixed-`M_0` counterexample in
`MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md`
forces the quantifiers to be prospective: a tight split-pivot path, its
matching phase, and the global connector bank must be selected together.
The canonical Gregor--Mütze--Nummenpalo (`GMN`) pull family does admit an
exact prospective formulation.  The uncoloured part is a labelled graphic
spanning-tree problem, but the upper-colour part is a local turn-state cover,
not a colour attached independently to each pull.

That exact model has a sharp asymptotic obstruction.  Put

\[
                         r=m-1,
 \qquad W_r=\binom{2r+1}{r},
 \qquad C_r=\operatorname {Cat}_r=\frac{W_r}{2r+1}.
\tag{0.1}
\]

The canonical GMN construction begins with the union `F_01` of the `0`- and
`1`-lexical perfect matchings.  Its immediate-upper turn map omits exactly

\[
 M_r=W_r\frac{(r-2)(r-3)}{2(r+2)(2r-1)}                 \tag{0.2}
\]

rank-`(r+2)` colours.  A factor-alternating `C_6` changes at most three turn
values.  A canonical pull spanning tree uses at most `C_r-1` pulls.  Hence
every Hamilton cycle obtainable by the canonical pull-tree scheme omits at
least

\[
                         M_r-3(C_r-1).                  \tag{0.3}
\]

This is positive for every `r>=11`, equivalently every `m>=12`; at `r=11`
the exact lower bound is `1941`.  Thus no correlated choice of a canonical
GMN pull spanning tree can make the projected upper colours surjective in
the all-dimensional range, even before a pivot prefix is prescribed.
Planting a literal prefix inside the same factor only restricts the tree.
Opening the resulting cycle cannot add a turn colour.

The viable prospective route is therefore not

> lexical factor + canonical pull spanning tree,

but one of the following genuinely broader operations:

1. choose a nonlexical base factor (for example, one with complete upper
   support) and prove a new compatible connector theorem;
2. allow noncanonical packets changing a linear number of lower turn slots;
   or
3. use explicitly charged cross-boundary contiguous-OR witnesses outside the
   projected turn map.

The last alternative is not ruled out here, but it is not projected
upper-colour surjectivity and must be audited at literal addresses.

## 1. The canonical pull variables

Work in the middle-levels incidence graph

\[
 G_r=Q_{2r+1}\left[\binom{[2r+1]}r\cup
                         \binom{[2r+1]}{r+1}\right].    \tag{1.1}
\]

Let `F_01` be the lexical spanning two-factor and let `H_r` be the labelled
GMN auxiliary multigraph: its vertices are the components of `F_01` and its
labelled edges are the canonical flippable pairs.  For a pull label `g`, let
`C_g` be its factor-alternating incidence hexagon, and write

\[
 O_g=C_g\cap F_{01},\qquad N_g=C_g\setminus F_{01}.    \tag{1.2}
\]

Canonical pull hexagons are pairwise edge-disjoint and noninterleaving in
the sense required by the GMN merge theorem.  They may share vertices.

For each label introduce `y_g in {0,1}`.  If `b_e` is the incidence vector
of `F_01`, the final incidence vector is exactly

\[
 x_e=b_e+
       \sum_{g:e\in N_g}y_g-
       \sum_{g:e\in O_g}y_g.                           \tag{1.3}
\]

Edge-disjointness makes at most one summand in (1.3) nonzero.  The selected
labels form a canonical pull spanning tree exactly when

\[
\begin{aligned}
 &\sum_{g\in E(H_r)}y_g=|V(H_r)|-1,\\
 &\sum_{g\in E_{H_r}(S)}y_g\le |S|-1
               &&(\varnothing\ne S\subseteq V(H_r)).
\end{aligned}                                         \tag{1.4}
\]

The inequalities treat loops and parallel two-cycles correctly.

### Proposition 1.1 (forced/forbidden prospective topology)

Suppose literal protected-incidence requirements, including a proposed
tight-pivot segment, force a label set `A` to be selected and a label set
`Z` to be omitted through (1.3).  Ignoring colours and all nonedge resources,
there is a canonical pull spanning tree containing `A` and avoiding `Z` if
and only if

1. the protected incidence equations are mutually consistent;
2. `A` is a labelled graphic forest in `H_r-Z`; and
3. `(H_r-Z)/A` is connected.

#### Proof

Necessity is inherited from every spanning tree.  For sufficiency, contract
the forest `A`.  A spanning tree of the connected contracted multigraph,
together with `A`, is the required labelled spanning tree.  The canonical
edge-disjoint/noninterleaving theorem then permits all corresponding pulls.
No shared-vertex resource is protected by this argument.  \(\square\)

Literal occurrence provenance is essential here.  Equality of owner masks,
turn colours, or an abstract Johnson `C_6` does not identify a canonical GMN
pull label or its six old/new incidence edges.  To protect a complete
boundary turn rather than only the displayed path edges, impose its desired
`0/1` incidence pattern on the whole boundary footprint.  A later pull can
share a boundary vertex without sharing a protected path edge.

## 2. Exact upper-colour linearization

For a lower vertex `L`, let `delta(L)` be its incident middle-levels edges.
The final factor chooses exactly two of them.  For every unordered pair
`{e,f} subset delta(L)`, introduce a binary variable
`z_(L,{e,f})`.  Link it to (1.3) by

\[
\begin{aligned}
 &\sum_{\{e,f\}\subseteq\delta(L)}z_{L,\{e,f\}}=1,\\
 &\sum_{\{e,f\}\ni e}z_{L,\{e,f\}}=x_e
                         &&(e\in\delta(L)).
\end{aligned}                                         \tag{2.1}
\]

If `V(e),V(f)` are the two rank-`(r+1)` endpoints, define

\[
                    \kappa(L,\{e,f\})=V(e)\cup V(f).
\tag{2.2}
\]

This is a rank-`(r+2)` set.  Projected immediate-upper surjectivity is
exactly

\[
 \sum_{L,\{e,f\}:\kappa(L,\{e,f\})=R}z_{L,\{e,f\}}\ge1
        \qquad\left(R\in\binom{[2r+1]}{r+2}\right).    \tag{2.3}
\]

### Theorem 2.1 (exact coloured auxiliary-tree formulation)

Equations (1.3)--(1.4), (2.1)--(2.3), and the literal forced/forbidden rows
of a protected packet are necessary and sufficient for a canonical GMN
pull-tree Hamilton cycle containing that packet and covering every projected
upper colour.

If a specified selected cycle edge is deleted to make a Hamilton path, the
corresponding destroyed endpoint turn must be excluded from (2.3).  A
protected segment becomes a literal global prefix only when the opening is
the exterior edge immediately preceding its chosen orientation.  Merely
containing its internal incidence edges is insufficient to prescribe the
global endpoint.

#### Proof

Equation (1.3) is precisely simultaneous symmetric difference with the
selected edge-disjoint hexagons.  The tree rows (1.4) and the canonical GMN
merge theorem give one Hamilton cycle.  At each lower vertex, (2.1) chooses
exactly its two final incidences, and (2.2) is the union of its two adjacent
rank-`(r+1)` owners.  Hence (2.3) is exactly upper surjectivity.  These steps
reverse verbatim.  Cutting a cycle edge creates no new adjacency, so it can
only destroy, never create, a turn witness.  \(\square\)

The local states in (2.1) are load-bearing.  A pull is not assigned one
context-free signed upper-colour vector: two canonical hexagons may share a
lower vertex, and the colour at that vertex depends jointly on its two final
neighbours.  A per-pull signed delta is valid only in a turn-disjoint bank or
after the other incident state has been frozen.

Indeed, edge-disjointness implies that at most two pull labels can touch one
lower turn: one through each of its two old factor edges.  If two co-selectable
labels `g,h` do so, write `kappa_empty,kappa_g,kappa_h,kappa_gh` for the four
possible turn colours.  A context-free additive colour-count delta exists at
that turn only if

\[
 [\kappa_{gh}]-[\kappa_g]-[\kappa_h]+[\kappa_\varnothing]=0
\tag{2.4}
\]

in the free abelian colour group.  Generically the old neighbours are
`L+a,L+b` and the two replacements are `L+c,L+d`; then (2.4) is

\[
 [L+c+d]-[L+b+c]-[L+a+d]+[L+a+b],                    \tag{2.5}
\]

which is nonzero when the four displayed colours are distinct.  Thus a
static signed-flow invariant on auxiliary labels requires a new modularity
theorem; it does not follow from canonical edge-disjointness.

## 3. A conditional graphic--Rado route for a different prepared family

The preceding exact system is not ordinary matroid intersection.  There is,
however, a useful sufficient theorem when prepared colour witnesses are
private under every later pull.

Let `A` be a forced forest and `Z` a forbidden set.  Contract `A` in the
graphic matroid of `H-Z`.  Let `D` be the upper colours not already supplied
by immutable baseline occurrences.  For each `R in D`, let `E_R` be a set of
admissible pull labels with the following **hereditary witness property**:

* selecting `g in E_R` creates a specified occurrence of colour `R`; and
* that occurrence, every immutable baseline witness, and every protected
  packet incidence survives every allowed spanning-tree completion
  containing `A union {g}`.

### Theorem 3.1 (private-witness graphic--Rado completion)

Assume

\[
 r_{\mathrm{gr}/A}\left(\bigcup_{R\in Y}E_R\right)\ge |Y|
                    \qquad(Y\subseteq D),             \tag{3.1}
\]

and assume the allowed auxiliary graph remains connected after contracting
`A` and every independent representative set supplied by (3.1).  Then there
is an allowed pull spanning tree containing `A` whose final factor covers
all colours in `D` and preserves every protected occurrence.

#### Proof

Rado's theorem applied to the contracted graphic matroid gives distinct
labels `g_R in E_R` such that `{g_R:R in D}` is graphic-independent.
Together with `A` they form a forest.  By the assumed residual connectivity,
extend that forest to a spanning tree.  The hereditary witness property
preserves the designated witness of each missing colour and every baseline
and protected witness through the completion.  \(\square\)

This is a prospective theorem: lists, the protected phase, and the tree are
chosen jointly.  It is deliberately stronger than necessary because it
assigns a distinct pull to each missing colour.  Without the hereditary
private-witness condition, (3.1) is not sound; later pulls can alter the
other neighbour at a shared lower turn.  The arbitrary fixed-`M_0`
counterexample is a separate warning that graphic independence and distinct
colours alone do not guarantee owner-path extendibility.

## 4. The lexical capacity cut

For `L in binom([2r+1],r)`, let its two neighbours in `F_01` be
`V_0(L),V_1(L)` and put

\[
                         \Phi(L)=V_0(L)\cup V_1(L).    \tag{4.1}
\]

Under `r=m-1`, this is exactly the immediate-upper owner colour in
`ML_m`.  The exact lexical defect theorem proves (0.2).

### Lemma 4.1 (three-slot Lipschitz bound)

After any ordered sequence of `s` factor-alternating incidence-hexagon
switches, the image of the resulting turn map can gain at most `3s` colours
that were absent from `Phi`.

#### Proof

One alternating hexagon contains three lower vertices.  Symmetric difference
changes the selected incident pair only at those vertices, so at most three
map values change.  Replacing one map value enlarges its image by at most
one.  Sum this bound along the ordered sequence; no independence or
nonoverlap assumption is needed.  \(\square\)

### Theorem 4.2 (canonical GMN upper-colour no-go)

For every `r>=11` (`m>=12`), every Hamilton cycle obtained from `F_01` by a
canonical GMN pull spanning tree omits at least

\[
             M_r-3(C_r-1)>0                           \tag{4.2}
\]

rank-`(r+2)` projected upper colours.  At `r=11` the bound is exactly
`1941`.

The same conclusion holds after prescribing any protected auxiliary forest
inside that spanning tree, and after opening the cycle into a path.

#### Proof

If `p_r` is the number of lexical factor components, a spanning tree uses
`p_r-1` pulls.  Plane-tree indexing gives

\[
                     p_r-1\le C_r-1.                  \tag{4.3}
\]

Lemma 4.1 and the initial defect (0.2) yield (4.2).  Moreover

\[
 M_r-3C_r
 =\frac{W_r(2r^3-21r^2-11r+18)}
        {2(r+2)(2r-1)(2r+1)}.                         \tag{4.4}
\]

The cubic numerator equals `18` at `r=11`.  Its derivative
`6r^2-42r-11` is positive for every real `r>=11`, so (4.4) is positive
there.  Adding the `3` in `M_r-3(C_r-1)` proves strict positivity.  Direct
substitution at `r=11` gives `1941`.

A prescribed forest reduces the set of available spanning trees but does
not increase their number of pulls.  Deleting a cycle edge creates no new
turn and therefore cannot repair an omitted colour.  \(\square\)

For `3<=r<=10`, the lower bounds `M_r-3(C_r-1)` are respectively

\[
 -12,-36,-101,-276,-734,-1856,-4209,-7069.            \tag{4.5}
\]

Thus this Catalan-capacity argument gives no positive missing-colour
conclusion in those finite parameters; it is not evidence of feasibility.
The `m=3` fixed-`M_0` protected counterexample has `r=2` and is logically
separate from the lexical defect theorem.

### Corollary 4.3 (bounded noncanonical prefix edits do not cure the defect)

If, before at most `C_r-1` hexagon pulls, a noncanonical planted prefix
changes at most `q` lower-turn states relative to `F_01`, the final cycle
still omits at least

\[
                         M_r-q-3(C_r-1)                \tag{4.6}
\]

upper colours.  Hence every `q=o(W_r)` planted packet leaves a linear
defect as `r` tends to infinity.

This corollary concerns the projected turn map only.  A literal
contiguous-OR word may obtain the same rank-`(r+2)` mask from an explicitly
audited crossing interval elsewhere.  Such witnesses are outside (4.6) and
must be charged and occurrence-labelled rather than inferred from the pull
tree.

## 5. The live prospective owner formulation

The tight pivot itself has a valid prospective phase independent of the
lexical pull-tree no-go.  Let

\[
 V_0,V_1,\ldots,V_\ell,qquad
 L_i=V_i\cap V_{i+1},qquad \ell=3h,                  \tag{5.1}
\]

be its simple Johnson owner path with distinct `L_i`.  Put every predecessor
incidence `L_i V_i` into a perfect matching `M_0`.  When `ell<=m-1`, that
partial matching extends to a perfect matching, and the successor incidences
contract in `D_(M_0)` to the forced directed path

\[
                         L_0\to L_1\to\cdots\to L_\ell.
\tag{5.2}
\]

On the occurrence-labelled arc ground set of `D_(M_0)`, the exact remaining
upper-exact Catalan forest is a common independent set of size `U-ell` in
the four contractions

\[
 M_{\rm tail}/P,\quad M_{\rm head}/P,
 \quad M_{\rm graphic}/P,\quad M_{\rm upper}/P.       \tag{5.3}
\]

This is a four-matroid correlation, not an Edmonds two-matroid intersection.
Equivalently, one may first construct an upper-surjective directed linear
forest containing (5.2), select one occurrence of every upper colour within
it, and then use an acyclic component connector reservoir.  For an
unspecified endpoint, the exact connector cut is one-defect Hall

\[
                         |N(X)|\ge |X|-1.              \tag{5.4}
\]

For the pivot component to be the prescribed global prefix, delete its
incoming port and require ordinary Hall saturating every other incoming
component.  If both endpoints are prescribed, delete the chosen start
incoming and end outgoing ports and require a perfect residual port
matching.

This support-first/acyclic-Hall route is the weakest exact prospective
owner theorem currently left open.  It is not supplied by the canonical
lexical GMN pull family for `m>=12` because of Theorem 4.2.

### Theorem 5.1 (exact jointly prospective decomposition)

Let `P_0,P_1` be the predecessor/successor shores of the pivot path (5.1),
with distinct upper transition colours.  The following are equivalent.

1. There is an upper-surjective alternating Hamilton path whose first
   protected segment is the prescribed orientation of `P_1`.
2. There is a jointly chosen triple `(M_0,Q_0,J)` such that:
   * `M_0` is a perfect incidence matching containing `P_0`;
   * `Q_0` contains `P_1`, has distinct tails, distinct heads and no
     undirected rooted-link cycle, contains exactly one occurrence of every
     rank-`(m+1)` upper colour, and has the first pivot root `L_0` as the
     initial vertex of its component;
   * if the `C=Cat_m` directed path components of `Q_0` are contracted,
     `J` is a matching between their free outgoing and free incoming ports,
     has size `C-1`, contains no component cycle, and leaves the component
     containing `P_1` as its unique source.

Here an edge of `J` is a literal occurrence-labelled arc of `D_(M_0)`, not
an abstract adjacency between components.

#### Proof

Given (2), `Q_0 union J` has `W-1` arcs, tail and head degrees at most one,
and is one directed spanning path by the component conditions.  It contains
one protected representative of every upper colour, so it is
upper-surjective.  Expanding `M_0` gives the required alternating incidence
path, and the unique-source condition places the protected component first.

Conversely, start with the Hamilton path in (1).  For every upper colour of
`P_1`, retain its prescribed occurrence.  For every other upper colour,
retain one occurrence on the Hamilton path.  The retained set `Q_0` is a
subset of a path, hence has distinct tails and heads and is acyclic.  It has
`U` edges and therefore `W-U=C` components.  The other `W-1-U=C-1` path
edges are exactly `J`; after contraction they match free ports and join the
components into one directed path from the protected component.  \(\square\)

This theorem identifies the exact correlation hidden by the phrase
"choose protected tickets and then extend": `M_0`, the protected path, all
upper representatives, and all component ports belong to one quantified
object.

### Theorem 5.2 (rooted connector-flow invariant)

Fix a prospective pair `(M_0,Q_0)` from Theorem 5.1, and let `K_*` be the
component containing the protected pivot.  Let `A(Q_0)` be a reservoir of
literal connector arcs from the free outgoing port of one component to the
free incoming port of another.  Suppose its component digraph is acyclic.
Then a connector set `J` as in Theorem 5.1 exists if and only if

\[
 |N^-(Y)|\ge |Y|
       \qquad\bigl(Y\subseteq\operatorname {Comp}(Q_0)\setminus\{K_*\}\bigr),
\tag{5.5}
\]

where the incoming copy of `K_*` is deleted and `N^-(Y)` denotes the
available outgoing component ports adjacent to `Y`.

If the terminal component `K^*` is also prescribed, delete its outgoing
copy as well; the exact condition is ordinary Hall for a perfect matching
between the remaining `C-1` outgoing and `C-1` incoming copies.

#### Proof

Condition (5.5) is Hall's theorem for a matching saturating every incoming
component except `K_*`.  It selects `C-1` arcs with component indegree one
away from `K_*` and outdegree at most one everywhere.  Acyclicity forbids a
disjoint directed cycle.  Every finite component not reached from `K_*`
would have a source, but `K_*` is the only component with indegree zero.
Thus all components form one path from `K_*`.  Necessity is immediate.
The two-endpoint variant is identical.  \(\square\)

This is the exact flow invariant requested by the prospective route.  It
simultaneously enforces head injectivity and topology.  Upper surjectivity is
not re-solved by the flow: it is protected by the occurrence-labelled
`Q_0` chosen in the outer common-basis step.

### 5.3 When pull-tree labels implement the connector flow

A canonical pull label is not automatically an arc of `A(Q_0)`.  Call a
pull label **`Q_0`-transparent** when its literal toggle has all of the
following properties.

1. It performs the declared merge between two free component ports.
2. Every selected turn occurrence of `Q_0` outside its support is unchanged.
3. On its support it gives a colour-preserving bijection from destroyed
   selected representative occurrences to new representative occurrences.
4. It preserves the occurrence-level pivot segment and the declared start
   port.

In addition, the pull must be certified relative to the same fixed
decomposition `M_0 union Q`: it either leaves `M_0` fixed and changes only
the connector shore, or comes with a literal decomposition isomorphism that
transports `M_0,Q_0` and their rooted ports.  A generic canonical GMN pull
does not satisfy this merely because it is factor-alternating.

For a family of labels, transparency is **joint** when these bijections are
simultaneously realizable.  Pairwise edge-disjointness alone is insufficient
because labels may meet at a lower vertex.  Turn-disjoint individually
transparent labels are jointly transparent; more generally one must supply
the local pair states (2.1) or an explicit common representative-token
flow.

### Corollary 5.3 (transparent pull-flow completion)

Suppose an allowed auxiliary graph of pull labels is jointly
`Q_0`-transparent under every spanning-tree subset used below, projects to
an acyclic component reservoir satisfying (5.5), and contains a spanning
tree extending the already forced auxiliary forest without violating the
literal occurrence interface.  Suppose moreover that the Hall-selected
connector labels can be included in such a spanning tree.  Then selecting
that Hall matching and a compatible auxiliary-tree completion gives an
upper-surjective Hamilton path with the pivot as its prescribed prefix.

#### Proof

Joint transparency transports the one-per-colour representative tokens of
`Q_0` injectively through all selected pulls.  Theorem 5.2 supplies the
component path with distinct free heads and tails.  The compatible
pull-tree completion supplies the physical factor merge, and the protected
start port supplies the opening.  \(\square\)

Thus there is a clean exchange/flow invariant, but it is an invariant of
**full turn occurrences plus component ports**, not of uncoloured GMN
labels.  In the canonical lexical family, Theorem 4.2 proves that no
spanning label choice can satisfy this invariant for `m>=12`: some
representative-token conservation or upper-cover row must fail.

The arbitrary-`M_0` pivot phase (5.1)--(5.3) and the fixed lexical GMN
factor therefore cannot be chosen independently and then superposed.  A
positive pull implementation must construct one common occurrence-level
factor decomposition from the outset.

## 6. Independent audit and exact scope

1. **Parameter translation.**  `2r+1=2m-1`, so `r=m-1`; the rank-`(r+2)`
   opposite triple is exactly the rank-`(m+1)` immediate-upper owner colour.
2. **Exact threshold.**  The numerator in (4.4) is negative through `r=10`,
   equals `18` at `r=11`, and is strictly increasing thereafter.  The exact
   `r=11` integer margin is `1941`.
3. **Adaptive pulls do not evade the bound.**  Lemma 4.1 is telescopic and
   makes no independence assumption.  Correlating the prefix and tree cannot
   repair more than three omitted image values per pull.
4. **Tree versus colour state.**  GMN edge-disjointness proves (1.3) and
   graphic extendibility.  It does not make turn colours additive because
   hexagons may share lower vertices.  The pair variables (2.1) are therefore
   required.
5. **Opening scope.**  Cyclic rerooting changes nothing.  Deleting a physical
   edge cannot add a turn colour.  A new endpoint connector must instead be
   charged as another lower-slot edit.
6. **What is not ruled out.**  The theorem does not obstruct PBBS, a
   nonlexical `M_0`/factor, noncanonical long switches, or extra
   cross-boundary OR witnesses.  It also proves no residence, deeper-shadow,
   common-cap, compiler, or regenerative statement.

The decisive arithmetic and parameter translation were independently
audited against
`MATH_THEOREM_LEXICAL_MIDDLE_LEVELS_OPPOSITE_TRIPLE_DEFECT_20260726.md` and
`MATH_AUDIT_PBBS_VERSUS_LEXICAL_MIDDLE_LEVELS_HAMILTONIZATION_20260726.md`.
