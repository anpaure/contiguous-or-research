# Detached SCD ears give exact q1 resources, while all-width inheritance requires component source blocks and path-contact cuts

Date: 2026-08-01  
Lane: A, SCD long-ear support / ordinary-sector all-width and common-`Q`
integration  
Status: exact audit conditional on detached injective/acyclic owner maps;
exact all-width path-label criterion; exact component maximal-source and
terminal-socket criterion; exact regular connector-repeat design and
physical component-cycle criterion; exact obstruction to one unchanged
global old-ground full block.  No all-`m` SCD source serialization is
claimed.

## 0. Verdict

Assume the four owner maps in
`MATH_THEOREM_SCD_GLOBAL_SEED_LONG_EAR_EXACT_PALETTES_AND_OWNER_MAP_GATE_20260801.md`
have been detached so that their rooted support is a linear forest.  The
ear grammar then supplies exactly the following data automatically:

1. all middle owners;
2. every rank-`(m+1)` upper edge colour exactly once;
3. `W-C` distinct internal rank-`(m-1)` lower labels; and
4. one canonically unused lower sink label on each of the `C` path
   components.

This is a complete q1 resource ledger, not a source word.

For upper width `q>=2`, exact inheritance is equivalent to a labelled
q-edge path condition.  Already q2 adds a quadratic contact cut not implied
by owner-map injectivity or acyclicity.  For lower common-`Q`, one whole
directed forest component is the smallest matching-closed unit.  It has a
literal source iff a maximal-erosion word reconstructs all owner rows and
the one terminal lower socket.  A three-owner depth-2 path shows that
linear ownership, distinct upper labels and a perfect inclusion matching do
not imply this condition.

The unrestricted componentwise maximal source inherits the whole internal
lower intersection tower, not just q1.  Common caps can shrink that source:
even after every q1 lower cell is reimposed, a depth-two cell can then be
strictly smaller than the corresponding owner intersection.  Thus the ear
grammar supplies the deeper lower compiler only on its uncut maximal-source
face.

Positively, every component which passes the source test is a genuine
jump-time full block: its whole internal interval deck is preserved and its
edge colours become pairwise-distinct child owners.  Negatively, the `C`
components cannot be joined unchanged by old-ground Johnson edges.  Their
q1 upper palette is already saturated, so every such connector duplicates
an existing child owner.  The repetitions are not arbitrary: after adding
the deleted endpoint edge they form a `C`-block regular upper multidesign of
coordinate degree `2 Cat_(m-1)`.  Abstract regular designs always exist,
but a literal braid is an exact coloured one-cycle assignment on the
component ports and obeys additional graphic cuts.  The surviving
construction is therefore a tagged inter-component weave or a simultaneous
edge-release/rethread, with the component source rows retained.

The controlled-leave Catalan packet bank remains a valid spread local
reservoir, and deleting its isolated off-providers loses no deep path
witness.  Its frozen balanced residual-forest face is nevertheless
coordinate-cocycle impossible.  For all sufficiently large `m`, two
swapped strata repair the singleton coordinate ledger exactly, but the
resource-disjoint typed packet bank exists.  Its decorated-factor
completion is open, and the packets are basis-incompatible with the frozen
four-row `M_0`.  Thus the reservoir can support this programme only through
a jointly selected basis/factor/braid; its present leaf activation is not a
component braid.

## 1. Exact rooted forest ledger

Let

\[
 \Omega=G\mathbin{\dot\cup}\{a,z\},\qquad
 |\Omega|=2m-1,
\]

and put

\[
 W={2m-1\choose m},\qquad C=\operatorname {Cat}_m.
                                                               \tag{1.1}
\]

Let

\[
 M_0:\binom{\Omega}{m-1}\longrightarrow\binom{\Omega}{m}
                                                               \tag{1.2}
\]

be the fixed four-row inclusion matching.  Contract every physical owner
head to its root under `M_0`.  Under the detached-map hypothesis, the
selected SCD ear support is a directed graph on the `W` lower roots with
indegree and outdegree at most one, no directed cycle, and `W-C` arcs.
It is therefore a union of exactly `C` directed paths.

Write one component as

\[
 L_0\longrightarrow L_1\longrightarrow\cdots
        \longrightarrow L_t,                         \tag{1.3}
\]

and put

\[
 O_i=M_0(L_i),\qquad 0\le i\le t.                 \tag{1.4}
\]

### Theorem 1.1 (automatic q1 resource partition)

For every `i<t`,

\[
 O_i\cap O_{i+1}=L_i,\qquad
 U_i:=O_i\cup O_{i+1}.                               \tag{1.5}
\]

Across all components, the `U_i` are pairwise distinct and form the
complete rank-`(m+1)` layer.  The selected internal lower labels are
`L_0,...,L_(t-1)`, while `L_t` is the unique unused lower root of this
component.  Hence globally

\[
 \binom{\Omega}{m-1}
 =
 \{\text{internal edge labels}\}
 \mathbin{\dot\cup}
 \{\text{one terminal sink label per component}\}. \tag{1.6}
\]

#### Proof

The rooted arc `L_i -> L_(i+1)` means
\(L_i\subset M_0(L_i)\) and \(L_i\subset M_0(L_{i+1})\).
The two physical owners are distinct rank-`m` sets, so their intersection
is exactly the rank-`(m-1)` set `L_i`.  The exact-palette theorem gives
pairwise distinct complete upper colours `U_i`.

In the directed path (1.3), precisely `L_0,...,L_(t-1)` are used as
tails.  Its sink `L_t` is the sole unused root.  Summing over the `C`
components gives (1.6). \(\square\)

Theorem 1.1 identifies lower target labels and owner edges.  It does not
place any of those labels on source intervals.

## 2. Exact arbitrary-width upper criterion

Let `F` be the resulting physical owner forest.  For an edge `e=uv`
write

\[
                         \lambda(e)=u\cup v.         \tag{2.1}
\]

### Theorem 2.1 (path-label criterion)

For \(q\ge1\) and \(X\in\binom{\Omega}{m+q}\), the forest has a width-`q`
upper witness for `X` iff it contains a q-edge path
`e_1,...,e_q` such that

\[
 \lambda(e_j)\subseteq X\quad(1\le j\le q),
 \qquad
 \bigcup_{j=1}^q\lambda(e_j)=X.                    \tag{2.2}
\]

#### Proof

If the owner path is `V_0,...,V_q`, then

\[
 \bigcup_{j=0}^qV_j
 =
 \bigcup_{j=1}^q(V_{j-1}\cup V_j)
 =
 \bigcup_{j=1}^q\lambda(e_j).                      \tag{2.3}
\]

Thus the owner interval has value `X` exactly under (2.2). \(\square\)

The q1 case is Theorem 1.1 and the exact-palette theorem.  No q2 or deeper
condition follows from edge-colour bijectivity alone.

### Corollary 2.2 (exact q2 contact cut)

For \(X\in\binom{\Omega}{m+2}\), put

\[
 d_X(v)=|\{e\ni v:\lambda(e)\subseteq X\}|,
 \qquad
 a_X(F)=\sum_{v\in V(F)}{d_X(v)\choose2}.          \tag{2.4}
\]

Then `X` has a q2 witness iff

\[
                              a_X(F)\ge1.             \tag{2.5}
\]

#### Proof

A q2 witness is exactly two incident edges whose two rank-`(m+1)`
labels lie in `X`.  The labels are distinct, and two distinct
rank-`(m+1)` facets of a rank-`(m+2)` set have union `X`.  Formula
(2.4) counts precisely these incident pairs. \(\square\)

The four detached owner-map conditions control degrees and cycles but do
not contain (2.5).  Higher widths require the full path system (2.2).

### Proposition 2.3 (smallest hypothesis-level counterexample)

Let `m=3`, `Omega=Z_5`, and for `i in Z_5` put

\[
 A_i=\Omega\setminus\{i,i+1\},\qquad
 B_i=\Omega\setminus\{i,i+2\}.                    \tag{2.6}
\]

The five isolated Johnson edges `A_iB_i` use all ten owners, form a
linear forest with `C=Cat_3=5` components, have every rank-four upper
colour exactly once, and use five distinct rank-two lower colours.  Yet the
rank-five target `Omega` has no q2 witness.

#### Proof

The complements of the `A_i` are the five cyclic adjacent pairs and the
complements of the `B_i` are the five cyclic diagonals, so the ten owners
are distinct.  Moreover

\[
 A_i\cup B_i=\Omega\setminus\{i\},\qquad
 A_i\cap B_i=\{i+3,i+4\}.                          \tag{2.7}
\]

These give all five upper colours and five distinct lower colours.  The
forest has no two-edge path, so (2.5) fails for `Omega`. \(\square\)

This refutes implication from the detached-map hypotheses alone.  It is not
asserted to be a realization of the fixed SCD ear formulas.  Indeed the
standard `m=3` SCD candidate happens to pass q2: the paths

\[
 a01-a02-az2,\qquad a12-az1-az0                   \tag{2.8}
\]

each have full-five-set union.  The first actual all-`m` SCD-ear failure,
if any, is not identified here.

## 3. Exact source criterion for one component

Fix a component owner path

\[
                         P=(O_0,\ldots,O_t)           \tag{3.1}
\]

and parent depth `h`.  A source block has positions
`0,...,t+h`; owner row `i` uses positions `i,...,i+h`.  Define

\[
 K_p(P)=
 \bigcap_{\max(0,p-h)\le i\le\min(t,p)}O_i,
 \qquad 0\le p\le t+h.                             \tag{3.2}
\]

### Theorem 3.1 (component maximal-source iff)

There is a nonempty-letter source word
`Q_0,...,Q_(t+h)` with

\[
                   \bigcup_{p=i}^{i+h}Q_p=O_i
                   \qquad(0\le i\le t)             \tag{3.3}
\]

iff

\[
 K_p(P)\ne\varnothing\quad(0\le p\le t+h),
 \qquad
 O_i=\bigcup_{p=i}^{i+h}K_p(P)\quad(0\le i\le t).
                                                               \tag{3.4}
\]

When (3.4) holds, `Q_p=K_p(P)` is the unique componentwise-largest
source.  Coordinatewise, owner reconstruction in (3.4) says that every
internal maximal positive run in an owner trace has length at least
`h+1`; leading and trailing positive runs may be clipped.  Nonemptiness
of every `K_p` is an independent condition.

#### Proof

Any feasible `Q_p` belongs to every owner window using position `p`,
so \(Q_p\subseteq K_p(P)\).  Thus an empty `K_p` or a missed coordinate in
(3.4) is impossible.  Conversely, the maximal word in (3.2) is nonempty
and reconstructs every owner exactly when (3.4) holds.  The trace statement
is the coordinatewise form of the same intersection test. \(\square\)

### Lemma 3.2 (internal lower q1 cells are then automatic)

If (3.4) holds, then for every `i<t`,

\[
 \bigcup_{p=i+1}^{i+h}K_p(P)
 =O_i\cap O_{i+1}=L_i.                              \tag{3.5}
\]

#### Proof

Every position in the displayed interval lies in owner windows `i` and
`i+1`, giving containment in their intersection.  Conversely take a
coordinate \(x\in O_i\cap O_{i+1}\).  Reconstruction of `O_i` and
`O_(i+1)` supplies maximal positions carrying `x` in
`[i,i+h]` and `[i+1,i+h+1]`.  If either position lies in their common
part, it proves the claim.  The only remaining possibility uses both outer
positions `i` and `i+h+1`.  Membership in both corresponding maximal
intersections then implies membership at position `i+1`, which lies in
the common part. \(\square\)

Thus component source realizability turns the `W-C` abstract lower labels
into literal common-`Q` cells.  The unused sink `L_t` is not automatic.
To host it at the terminal boundary one must additionally impose

\[
                         \bigcup_{p=t+1}^{t+h}Q_p=L_t. \tag{3.6}
\]

### Lemma 3.3 (full maximal lower tower, and its capped failure)

For any source realizing the owner rows, its literal depth-`q` common cell
under the consecutive owners `O_i,...,O_(i+q)` is

\[
 D_{i,q}(Q)=\bigcup_{p=i+q}^{i+h}Q_p,
 \qquad 1\le q\le\min(h,t-i).                       \tag{3.7}
\]

It always satisfies

\[
 D_{i,q}(Q)\subseteq\bigcap_{j=0}^q O_{i+j}.         \tag{3.8}
\]

For the unrestricted maximal source `Q_p=K_p(P)` of Theorem 3.1, equality
holds in (3.8) for every `q`.  For a capped source, equality at `q=1` is
one of the imposed rows in Section 4.  Even when all these q1 equalities
hold, equality in (3.8) need not hold for `q>=2`.

#### Proof

Every position `p` in `[i+q,i+h]` belongs to each owner window
`[i+j,i+j+h]`, `0<=j<=q`, proving (3.8).

Now use the maximal word and take a coordinate `x` in the right side of
(3.8).  Let `[a,b]` be the maximal positive owner-trace run containing
`i,...,i+q`.  If neither end is clipped, Theorem 3.1 gives
`b-a+1>=h+1`.  Therefore

\[
 [i+q,i+h]\cap[a+h,b]\ne\varnothing.               \tag{3.9}
\]

Any position in this intersection is used only by owners in `[a,b]`, so
its maximal letter contains `x`.  At a clipped left or right end the same
argument uses respectively `p=i+q` or
`p=max(i+q,a+h)`.  Hence the maximal word attains equality for every `q`.

For capped failure take `h=2` and the five nonempty letters

\[
 Q_0=\{a\},\quad Q_1=\{x,b\},\quad Q_2=\{y\},\quad
 Q_3=\{x,c\},\quad Q_4=\{d\}.                       \tag{3.10}
\]

They give the simple rank-four Johnson path

\[
 O_0=abxy,\qquad O_1=bcxy,\qquad O_2=cdxy.           \tag{3.11}
\]

Both q1 rows are exact:

\[
 Q_1\cup Q_2=bxy=O_0\cap O_1,qquad
 Q_2\cup Q_3=cxy=O_1\cap O_2.                       \tag{3.12}
\]

But

\[
 D_{0,2}(Q)=Q_2=\{y\}
 \subsetneq \{x,y\}=O_0\cap O_1\cap O_2.            \tag{3.13}
\]

The coordinate `x` is carried by two separated source occurrences.  Thus
the owner chronology and every q1 cell fail to determine the deeper common
cell. \(\square\)

Consequently the owner-only maximal component source inherits all internal
lower flags automatically.  A compiler which adds caps, terminal sockets
or exterior mandatory bits must either prove that those restrictions leave
the relevant maximal letters unchanged, or add the rows (3.7), or their
assigned target versions, to its single maximal-word system.  The four-ear
q1 palette alone does not justify that capped inheritance.

### Corollary 3.4 (the deepest lower row forces interior maximality)

If a capped source realizes the complete internal lower tower through
depth `h`, then

\[
                              Q_p=K_p(P)
                              \qquad(h\le p\le t).    \tag{3.14}
\]

Indeed, put `i=p-h,q=h` in (3.7).  The literal lower cell is the singleton
source position `Q_p`, whereas its required owner-intersection value is

\[
                 \bigcap_{j=p-h}^{p}O_j=K_p(P).       \tag{3.15}
\]

Thus any interior cap which deletes even one coordinate of `K_p(P)`
necessarily destroys a deeper lower flag, although every q1 row may still
survive.  Any source-position freedom not ruled out by this depth-`h` row
is confined to

\[
                         [0,h-1]\cup[t+1,t+h],       \tag{3.16}
\]

whose two clipped banks may overlap when `t<h-1`.  Owner reconstruction,
shallower rows, caps and exterior rows can still force positions in this
union; (3.16) is a location bound, not a freedom guarantee.

## 4. Exact component common-`Q` system and first cut

For every component impose the owner rows (3.3), all internal rows (3.5),
and the terminal sink row (3.6).  With point caps `C_p`, define

\[
 P_p=C_p
 \cap\!\!\bigcap_{i:p\in[i,i+h]}O_i
 \cap\!\!\bigcap_{j:p\in[j+1,j+h]}L_j,           \tag{4.1}
\]

where the second lower intersection includes `j=t`.  Frozen exterior
contributions and mixed boundary rows are inserted exactly as in Theorem
5.1 of
`MATH_THEOREM_A_ORDINARY_SECTOR_SEMANTIC_EXPORT_AND_COMMONQ_MATCHING_GATE_20260801.md`.

### Theorem 4.1 (owner/lower component block iff)

A nonempty source realizes all owner, internal lower and terminal sink rows
iff every `P_p` is nonempty, contains its mandatory subset, and the word
`Q_p=P_p` reconstructs every row (3.3), (3.5), and (3.6), including all
fixed exterior contributions.

#### Proof

This is frozen-prefix relative maximal erosion applied to the displayed
row family.  Any feasible source is componentwise contained in `P`; hence
the maximal word is feasible iff it reconstructs every row. \(\square\)

For a full lower tower, prescribe target rows

\[
                 \bigcup_{p=i+q}^{i+h}Q_p=T_{i,q}    \tag{4.1a}
\]

for every required `(i,q)`, and intersect their targets into (4.1) at all
incident positions.  The same maximal-word iff remains exact, because its
proof uses only intersection of row targets.  On the fixed
owner-intersection face

\[
                         T_{i,q}=\bigcap_{j=0}^qO_{i+j},           \tag{4.1b}
\]

Corollary 3.4 gives severe rigidity: every interior depth-`h` row forces
the capped source letter back to `K_p(P)`.  Reassigned depth-`h` targets do
not have that consequence.  Any remaining freedom on the fixed face is
only confined to the clipped union (3.16); it is not guaranteed there.

There is a useful necessary cut.  Put

\[
                         a_i=O_i\setminus L_i.        \tag{4.2}
\]

Owner row `i` and lower row `i` force `a_i` into source position `i`.
Every earlier lower row containing that position then gives

\[
 a_i\subseteq
 \bigcap_{j=\max(0,i-h)}^{i-1}L_j
 \qquad(1\le i\le t).                              \tag{4.3}
\]

Condition (4.3) is not implied by owner linearity.

### Proposition 4.2 (minimal depth-2 common-source obstruction)

On `[5]`, let

\[
 L_0=12,\quad L_1=13,\quad L_2=14,
\qquad
 O_0=125,\quad O_1=123,\quad O_2=134.               \tag{4.4}
\]

These are a valid directed owner path with distinct upper colours, and the
partial assignments extend to a perfect inclusion matching.  Nevertheless
there is no depth-2 source satisfying the owner, internal-lower and terminal
sink rows.

#### Proof

The intersections are

\[
 O_0\cap O_1=L_0,\qquad O_1\cap O_2=L_1,          \tag{4.5}
\]

and the upper colours `1235,1234` are distinct.  A perfect extension is

\[
\begin{array}{c|cccccccccc}
L&12&13&14&15&23&24&25&34&35&45\\ \hline
M_0(L)&125&123&134&135&235&124&245&234&345&145.
\end{array}                                          \tag{4.6}
\]

But \(a_2=\{3\}\not\subseteq L_0\), violating (4.3).  Equivalently, the rows

\[
 Q_1\cup Q_2=12,\qquad Q_3\cup Q_4=14,\qquad
 Q_2\cup Q_3\cup Q_4=134                            \tag{4.7}
\]

force \(3\in Q_2\subseteq12\), a contradiction. \(\square\)

This is a hypothesis-level obstruction to the owner-map theorem, not a
claim that the fixed SCD formulas realize (4.4).

After adding deeper compiler occurrences `M`, the exact residual
coordinate sets are

\[
 A_x(M)=\{p:x\in P_p\}
 \setminus
 \bigcup_{(T,c)\in M:x\notin T}I_c.                \tag{4.8}
\]

Every required owner, lower, terminal or mixed row must retain one position
in `A_x(M)` for each positive coordinate `x`, and every source position
must retain a nonempty coordinate.  These are precisely the positive-cover
and empty-position cuts from the ordinary-sector theorem.

## 5. Conditional componentwise jump full blocks

### Theorem 5.1 (component jump/deck inheritance)

Suppose every detached component passes Theorem 4.1, and first ignore rows
which cross between components.  Use its common source at parent depth
`h`.  At child depth `H=h+1`, its owner windows are

\[
 V_i=O_i\cup O_{i+1}=U_i,\qquad 0\le i<t.         \tag{5.1}
\]

They are pairwise distinct across all components.  Within a component,
consecutive `V_i` are Johnson neighbours, so each component becomes a
simple child owner-path fragment.  Every source interval lying wholly
inside that component block retains exactly its old OR value after the
jump.  Hence every chosen old upper or lower witness supported internally
in a component, including any Ferrers row/column witness, transports with
zero common-`Q` damage.

For signed child threshold `h+2`, every internal parent zero gap must have
length at least `h+3`; clipped runs and gaps remain boundary conditions.

#### Proof

The window identity gives (5.1).  The exact upper palette makes all `U_i`
globally distinct.  Two consecutive `U_i,U_(i+1)` both contain the
rank-`m` owner `O_(i+1)`; distinctness therefore makes them Johnson
neighbours.  The source letters and their order are unchanged, so every
internal interval OR is unchanged.  Adjacent Boolean OR enlarges an
internal parent positive run by one and shortens an internal zero gap by
one, proving the residence statement. \(\square\)

Theorem 5.1 is the strongest automatic full-block consequence of the ear
grammar.  It is conditional on an actual component source, not merely the
owner forest.

## 6. Exact obstruction to one unchanged global full block

### Theorem 6.1 (upper-palette saturation cut)

The `C` detached SCD components cannot be joined into one unchanged
old-ground parent owner path whose jump lift is simple while all
`W-C` forest edges are retained.

#### Proof

Every old-ground Johnson connector has a rank-`(m+1)` upper colour.  The
forest already uses every such colour exactly once.  Hence any added
connector duplicates the colour of an existing edge; after the jump both
edges become the same child owner.

Equivalently, a parent Hamilton path on all `W` old-ground owners has
`W-1` edges, but there are only

\[
 {2m-1\choose m+1}=W-C                              \tag{6.1}
\]

possible old-ground child owners.  Since `C>1`, a simple jump lift is
impossible. \(\square\)

Thus every one-block construction must release/reroute old edges or use
new-coordinate tagged connectors.  The latter cease to be literal
old-ground full-block transport at exactly the mixed seams.

There is also an exact source-length ledger.  If component `q` contains
`n_q` owners, its depth-`h` source block has `n_q+h` letters.  Keeping
all `C` blocks disjoint therefore uses

\[
 \sum_{q=1}^C(n_q+h)=W+hC,                           \tag{6.2}
\]

whereas one `W`-owner source line would have `W+h` letters.  Raw
component placement costs

\[
                              h(C-1).                 \tag{6.3}
\]

Eliminating this cost requires exact overlap of component boundary states
or a tagged trace-Euler weave; it is not a consequence of forest
acyclicity.

## 7. Controlled-leave reservoir and the minimal exterior upper bank

The controlled-leave construction reserves \(C\) mutually
resource-disjoint packets.  Its packet identity, resource disjointness and
spread/local-load theorem remain valid.  Its frozen one-stratum balanced
residual forest does not: the coordinate-cocycle theorem forces the unused
lower family to contain the distinguished coordinate \(a\) exactly
\(2C-2\operatorname {Cat}_{m-1}>C\) times.  Thus the following activation
analysis is a conditional interface for a cocycle-repaired or mixed-stratum
reservoir, not a completion of the frozen residual host.

For all sufficiently large `m` there is now an exact minimum coordinate
repair.  Two swapped active strata `(alpha,beta)` and `(beta,alpha)` admit
a `C`-packet endpoint vector and a simple `C`-set unused-lower family
satisfying every singleton coordinate cocycle; one stratum is impossible
for every `m>=3`.  In fact the same theorem constructs an exact
resource-disjoint typed two-stratum packet/hole bank.  What remains open is
its completion to the physical decorated two-factor, as proved in
`MATH_THEOREM_TWO_STRATUM_PACKET_COORDINATE_COCYCLE_FEASIBILITY_20260801.md`.

The physical packet support is equivalently a decorated spanning
two-factor: every packet prescribes a three-edge path `D-A-C_0-B`, its
middle edge is marked, and every factor cycle must meet a marked edge.
Deleting all `C` marked edges gives the desired `C`-component upper-exact
forest.  This support cannot be grafted post hoc onto the frozen four-row
SCD matching `M_0`: the target edge `C_0-B` has lower colour `aS`, while
`M_0(aS)=A` is neither endpoint.  Hence integration with the explicit SCD
forest is necessarily basis-changing or jointly selected, not a union of
the two frozen supports.  This exact interface is proved in
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_EQUIVALENCE_AND_FIXED_M0_PHASE_NOGO_20260801.md`.

Before activation, each packet contains an
isolated off-provider edge

\[
                         A---C_0.                    \tag{7.1}
\]

A hypothetical cocycle-feasible balanced residual forest would consist of
\(C\) paths with endpoint bank \(B\cup D\).  Activation deletes (7.1)
and adds

\[
                         C_0---B,\qquad A---D.       \tag{7.2}
\]

Thus every packet attaches two new leaves but does not merge two residual
components.

### 7.1 Exact exterior target bank

For a physical owner forest `F`, define its width-`q` value deck

\[
 \mathcal W_q(F)=
 \left\{
   \bigcup_{e\in P}\lambda(e):
   P\text{ is a q-edge path in }F
 \right\},                                         \tag{7.3}
\]

and its missing exterior bank

\[
 \mathcal E_q(F)=
 \binom{\Omega}{m+q}\setminus\mathcal W_q(F).     \tag{7.4}
\]

If a rethread deletes an edge set `D_0`, define the casualty bank

\[
 \mathcal B_q(F,D_0)=
 \left\{
 X\in\mathcal W_q(F):
 \text{every q-path witness of }X\text{ meets }D_0
 \right\}.                                         \tag{7.5}
\]

### Theorem 7.1 (minimal exterior-service criterion)

Suppose a rethread retains every old q-path avoiding `D_0`, and let
`N_q` be its genuinely new q-edge paths.  It is width-`q` complete and
loses no old width-`q` target iff

\[
 \mathcal E_q(F)\cup\mathcal B_q(F,D_0)
 \subseteq
 \left\{
   \bigcup_{e\in P}\lambda(e):P\in N_q
 \right\}.                                         \tag{7.6}
\]

#### Proof

A target outside \(\mathcal E_q\) has an old witness.  Such a witness
survives unless all its witnesses meet `D_0`, which is exactly membership
in \(\mathcal B_q\).  Every initially missing or newly unwitnessed target
must therefore occur on a new path, and this condition is plainly
sufficient. \(\square\)

### Corollary 7.1A (edge-additive braids have zero upper casualty)

Suppose the braid only orders or reverses whole path components and adds
connector edges; no internal component edge is deleted.  Then every old
q-edge path survives, so for every `q`

\[
 \mathcal W_q(F_{\rm braid})
 =\mathcal W_q(F)\cup
   \{\text{values of q-paths crossing a new connector}\}.       \tag{7.7}
\]

In particular its casualty bank is empty at every width.  It is complete
through the full upper tower `1<=q<=m-1` iff every old missing bank
`E_q(F)` is served by a connector-crossing path.  If `F` was already
all-width upper-complete, any literal edge-additive component braid loses
no arbitrary-width target and needs no exterior repair bank at all.

This statement is at owner-chronology level.  A physical source braid must
also keep each component source block contiguous and unchanged; otherwise
the assertion that its internal interval witnesses survive is no longer
automatic.

Thus for a q1-exact forest the unique minimal semantic exterior bank
through width `H` is the graded set

\[
 \mathfrak E_H(F)=
 \mathop{\dot\bigcup}_{q=2}^{H}\{q\}\times\mathcal E_q(F).       \tag{7.7a}
\]

No already-covered target belongs in this bank: its chosen internal path
survives.  With `s` junctions, a necessary aggregate address bound is

\[
 |\mathfrak E_H(F)|
 \le s\sum_{q=2}^{H}q
 =s\left({H(H+1)\over2}-1\right).                  \tag{7.7b}
\]

For the full upper tower take `H=m-1`.  The bound counts path addresses,
not distinct values; collisions can only make the actual service capacity
smaller.

For a pure endpoint braid with `s` new junctions and unchanged component
interiors, at most `q` q-edge paths cross one junction.  Hence

\[
 |\mathcal E_q(F)\cup\mathcal B_q(F,D_0)|\le qs   \tag{7.8}
\]

is a necessary address cut.  With one junction per component join,
`s=C-1`.

The controlled-leave activation has an especially clean loss ledger.
Because every deleted off-provider (7.1) is an isolated edge,

\[
                         \mathcal B_q(F,D_0)=\varnothing
                         \qquad(q\ge2).              \tag{7.9}
\]

Each of the `2C` added leaf edges creates at most one new q-path for a
fixed `q`.  Therefore activation preserves every residual-forest deep
witness and adds at most `2C` new width-`q` addresses.  It follows that
the controlled leave is **deep-loss-free**, but it proves no upper
completeness beyond q1: neither (7.4) nor the contact cuts (2.5) are
controlled by the balanced residual-forest theorem.

### 7.2 Minimal boundary signature state

Let a component have oriented edge labels
`u_1,...,u_r`.  For a cutoff `H`, define its endpoint upper signatures

\[
 \Sigma_H(P)=
 \left(
  \bigcup_{j=1}^a u_j,\quad
  \bigcup_{j=r-a+1}^r u_j
 \right)_{0\le a\le\min(H,r)},                    \tag{7.10}
\]

with the empty union recorded as empty.  If two components are joined by
an edge of label `u_*`, every q-path value crossing that junction is
exactly

\[
 \left(\bigcup\text{last }a\text{ left labels}\right)
 \cup u_*
 \cup
 \left(\bigcup\text{first }b\text{ right labels}\right),
 \qquad a+b+1=q.                                    \tag{7.11}
\]

For a path crossing several junctions, (7.11) is concatenated: take a
suffix of the first component, every intervening connector label, the full
edge-label words of wholly traversed intermediate components, and a prefix
of the last component.  Their edge counts sum to `q`, and their set-union
is the path value.  A component wholly traversed by a path of width at most
`H` has at most `H` edges, so its total union is already the terminal entry
of (7.10).

Thus the ordered component/connector list together with all `Sigma_H`
determines the complete exterior upper deck through width `H`.  Conversely,
every signature entry can affect a crossing value, so no endpoint-only or
total-union state determines (7.11) in general.  This is the minimal
proof-safe upper state for a component braid; it has `O(H)` signatures per
component even though it determines `O(H^2)` crossing addresses over all
widths.

### 7.3 Exact endpoint common-`Q` alignment

The endpoint bank `B union D` from the controlled-leave theorem is a
physical owner statement.  A literal source extension needs a lower socket
alignment as well.

For a realized component source `Q_0,...,Q_(t+h)`, define its lower
boundary rays

\[
 \Lambda_h(P)=
 \left(
   \bigcup_{p=0}^{\ell-1}Q_p,
   \quad
   \bigcup_{p=t+h-\ell+1}^{t+h}Q_p
 \right)_{1\le\ell\le h}.                           \tag{7.12a}
\]

Once a literal seam word is fixed, every clipped lower source interval
crossing that seam is the union of one suffix ray, its consecutive seam
letters, and one prefix ray.  Hence (7.12a), together with the seam word,
is a sufficient `O(h)` lower boundary signature.  The terminal q1 socket
below is only one entry of this state, not the whole all-depth lower
interface.

### Theorem 7.2 (one-ended leaf extension)

Let a realized depth-`h` component source end at owner `O`, and let its
fixed suffix socket be

\[
                         R=\bigcup_{p=t+1}^{t+h}Q_p. \tag{7.12}
\]

Let `O'` be a proposed adjacent leaf owner.  Keeping the old source block
fixed, one new source letter extends it to `O'` iff

\[
                         O\cap O'=R                 \tag{7.13}
\]

and the complete screened cap at the new position permits a nonempty
entering letter `E` with

\[
                         O'\setminus R\subseteq E\subseteq O'. \tag{7.14}
\]

The prefix version is symmetric.

#### Proof

The shared length-`h` row remains the fixed union `R`, so exact lower
q1 forces (7.13).  The new owner row is \(R\cup E=O'\), equivalent to
(7.14); conversely these equations construct the extension. \(\square\)

For packet (7.2), the two new edge intersections are its declared old and
new lower colours.  They must equal the exported prefix/suffix sockets of
the residual paths incident with `B,D`.  Slot saturation names the
physical endpoints but does not impose these equalities or the rooted
orientation.  For the frozen packet bank the incident leaves are named, so
each residual path has only a binary orientation test: its two endpoint
sockets must match the two fixed incident packet lower colours in one
orientation or after reversal.  A general endpoint matching arises only if
leaves may be reassigned.

The exact **q1 endpoint-alignment** refinement is therefore:

> orient every residual path and attach its two named packet leaves so that the
> two endpoint socket labels equal the two incident packet lower colours,
> then pass the entering-letter caps (7.14).

After appending a leaf, one must still impose the new terminal unused-lower
socket if that leaf is the directed sink, every lower/mixed/boundary row
through the entering letter, and one joint maximal-word test when both ends
of a component are extended.  Hence Theorem 7.2 is an exact one-edge q1
extension lemma, not by itself a complete common-`Q` packet theorem.

### 7.4 Exact connector-repeat design and physical port cycle

Put

\[
                         c=\operatorname {Cat}_{m-1}.             \tag{7.15}
\]

The vague instruction “recycle an old upper colour” has an exact global
form.  The coordinate calculation and abstract existence theorem are also
frozen independently in
`MATH_THEOREM_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md`; the
physical port-cycle and all-width integration below are the additional
rows needed here.

### Theorem 7.3 (connector cocycle and regular repeat design)

Suppose a Hamilton path on all rank-`m` owners uses every rank-`(m-1)`
lower colour except `K_0`, and every rank-`(m+1)` upper colour at least
once.  Let `R` be the multiset of upper occurrences beyond the first copy
of every upper colour, and let `T^-`,`T^+` be the endpoint owners.  Then
`|R|=C-1` and, coordinatewise,

\[
 d_{\mathcal R}(q)
 =2c+\mathbf 1_{q\in K_0}
     -\mathbf 1_{q\in T^-}-\mathbf 1_{q\in T^+}.      \tag{7.16}
\]

If the endpoints are adjacent and

\[
 K_0=T^-\cap T^+,
 \qquad R_0=T^-\cup T^+,                              \tag{7.17}
\]

then

\[
 d_{\mathcal R}(q)=2c-\mathbf 1_{q\in R_0}.           \tag{7.18}
\]

Consequently

\[
                 \mathcal Q=\mathcal R\mathbin{\dot\cup}\{R_0\} \tag{7.19}
\]

is a `C`-block rank-`(m+1)` multidesign of constant coordinate degree
`2c`.  Conversely, for every prescribed `R_0` and every `m>=3`, an
abstract multidesign (7.19) exists.

#### Proof

For one Johnson edge, the two owner incidence indicators equal the sum of
its lower-intersection and upper-union indicators.  Summing over the path
at coordinate `q` gives

\[
 2{2m-2\choose m-1}
 -\mathbf 1_{q\in T^-}-\mathbf 1_{q\in T^+}
 =\left({2m-2\choose m-2}-\mathbf 1_{q\in K_0}\right)
  +\left({2m-2\choose m}+d_{\mathcal R}(q)\right).    \tag{7.20}
\]

The constant remainder is

\[
 2{2m-2\choose m-1}-{2m-2\choose m-2}
                     -{2m-2\choose m}=2c,            \tag{7.21}
\]

which proves (7.16).  Endpoint adjacency gives

\[
 \mathbf 1_{T^-}+\mathbf 1_{T^+}
 =\mathbf 1_{K_0}+\mathbf 1_{R_0},                   \tag{7.22}
\]

and hence (7.18).  Also

\[
 (W-1)-{2m-1\choose m+1}=C-1,
 \qquad C(m+1)=2(2m-1)c.                             \tag{7.23}
\]

This proves the size and regularity of `Q`.

For abstract existence, reserve `R_0` and make a bipartite incidence graph
between the `2m-1` coordinates and `C-1` labelled block vertices.  Give
every block degree `m+1`, every coordinate in `R_0` degree `2c-1`, and
every other coordinate degree `2c`.  The degree sums agree by (7.23).
Gale--Ryser holds: for at most `m+1` coordinate vertices the requested sum
is at most `2ct<=(C-1)t`, since `2c<=C-1` for `m>=3`; for a larger set the
right side is already the total block degree.  Reading the neighbourhood
of each labelled block vertex gives (7.19).  Equal neighbourhoods are
allowed because this is a multidesign. \(\square\)

The exact owner/q1 realization is a coloured component-cycle problem.
For each fixed directed forest component let `s_i,t_i` be its source and
sink owner.  Form the directed port graph

\[
 i\longrightarrow j
 \quad\Longleftrightarrow\quad t_i\sim s_j
 \text{ in }J(2m-1,m),                              \tag{7.24}
\]

and colour this arc by

\[
                 \bigl(t_i\cap s_j,\ t_i\cup s_j\bigr).          \tag{7.25}
\]

### Theorem 7.4 (exact owner/q1 port-cycle criterion)

An edge-additive braid of the `C` directed components into a Hamilton path
whose endpoint owners are Johnson-adjacent with intersection `K_0` and
union `R_0`, and with every missing lower colour used except `K_0`, exists
iff the port graph has a directed one-factor which

1. is one `C`-cycle;
2. uses every missing lower colour exactly once;
3. has upper-colour multiset `Q` from (7.19); and
4. contains a distinguished arc of colour `(K_0,R_0)`.

Deleting the distinguished arc gives the Hamilton path.  If component
reversal is permitted, first expand each component into its allowed
orientation states, impose exactly one selected state per original
component, and require the one-cycle on those selected states.  The
cycle-cover degree equations together with the usual directed subtour cuts
are an exact finite formulation.

#### Proof

Add the edge joining the two endpoints of any desired Hamilton path.  The
components are then cyclically ordered; the added connector at every sink
chooses one source, so these connectors are a directed one-factor and form
one cycle.  Their lower colours are precisely the `C` labels missing from
the component interiors, while Theorem 7.3 gives their upper multiset.
The closing edge is the distinguished `(K_0,R_0)` arc.  Conversely, expand
the component paths along a one-cycle and delete that distinguished arc.
All owner degrees and both q1 ledgers are then exactly as required.
\(\square\)

Regularity of `Q` is not sufficient for Theorem 7.4.  For a family `A` of
upper colours, write `mu_Q(A)` for the number of blocks of `Q`, counted
with multiplicity, which belong to `A`, and let

\[
 \Phi(\mathcal A)=
 \{T\in{\Omega\choose m}:T\subset U
       \text{ for some }U\in\mathcal A\}.            \tag{7.26}
\]

If `Phi(A)` is a proper nonempty owner set, every physical realization
obeys the graphic cut

\[
 \boxed{\quad
 \mu_{\mathcal Q}(\mathcal A)
 \le |\Phi(\mathcal A)|-|\mathcal A|-1.
 \quad}                                               \tag{7.27}
\]

Indeed, the upper-exact old forest contributes one `A`-coloured edge per
member of `A`, the connector cycle contributes `mu_Q(A)`, and all these
edges lie in the subgraph induced by `Phi(A)`.  A proper induced subgraph
of a Hamilton cycle is a path forest and has at most `|Phi(A)|-1` edges.
For one colour `U`, (7.27) reads

\[
                         \mu_{\mathcal Q}(U)\le m-1.  \tag{7.28}
\]

There are regular abstract designs which violate this.  At `m=4`, on
`Omega=[7]`, put

\[
 U=12345,\qquad R_0=12367,                            \tag{7.29}
\]

and take `Q` to be four copies of `U`, one copy of `R_0`, and the nine
blocks

\[
 67\cup S,\qquad S\in{[5]\choose3}\setminus\{123\}.  \tag{7.30}
\]

It has `C=14` blocks and every coordinate has degree `10=2c`, but
`mu_Q(U)=4>3=m-1`.  Thus even the exact regular connector cocycle leaves a
genuine physical graphic/ordering obstruction.

Indeed, coordinates `1,2,3` occur in the four copies of `U`, in `R_0`,
and in five of the nine last blocks; coordinates `4,5` occur four plus six
times; and coordinates `6,7` occur in `R_0` and all nine last blocks.

Finally, Theorems 7.3--7.4 are q1 statements.  For the all-width braid the
chosen cyclic order must additionally make its crossing paths satisfy
(7.6), as computed from the component signatures (7.10)--(7.11), and all
seams must pass the common-`Q` system of Section 7.3 simultaneously.
Coordinate regularity has no implication at width at least two.

### 7.5 Sharp pivot and integrated braid scope

A fixed sharp pivot lying wholly inside one component is automatically
protected by Theorem 5.1.  The spread-reservoir theorem already tolerates a
fixed resource-disjoint protected bank of order \(O(\sqrt m)\), so the
solved pivot introduces no new asymptotic resource row here.

The frozen one-stratum residual state is already impossible by the
coordinate cocycle.  Any **forest-first** use of that frozen reservoir must
change its residual signature by at least
\(C-2\operatorname {Cat}_{m-1}\) coordinate units, for example by mixing
the second swapped stratum.  For all sufficiently large `m`, the
two-stratum theorem performs this repair exactly at singleton-coordinate
level.  A joint basis-plus-decorated-factor-plus-connector selection could
avoid exposing the forbidden intermediate residual family, but then the
prescribed typed packet paths, decorated-factor completion, the regular
multidesign of Theorem 7.3 and the physical cuts (7.24)--(7.27) must be
imposed inside the same selection.  Abstract
existence of `Q`, or the two-stratum degree vector alone, is not a physical
repair of the frozen forest.

The controlled packets themselves do not braid the \(C\) paths: (7.2)
only extends their leaves.  To reduce the component count, the additional
`C-1` path connectors must realize `Q-{R_0}`; after restoring the
distinguished closing arc, the completed component cycle realizes the
exact palette `Q`.  The isolated off-provider bank is attractive because
(7.9) makes its deletion
deep-loss-free, but the present one-to-two identity attaches two leaves
rather than joining two paths.  A valid braid still has to satisfy
simultaneously:

1. the one-cycle port assignment and q1 palette of Theorem 7.4;
2. endpoint socket alignment (7.13)--(7.14);
3. the exterior service criterion (7.6), computed from (7.10)--(7.11);
4. all capped lower target rows (4.1a) and clipped crossing rows, with
   interior maximality (3.14) on the fixed owner-intersection tower;
5. common-`Q` positive-cover and nonempty-position cuts; and
6. signed residence at every junction.

No such all-`m` cocycle-feasible packet braid is proved by the
controlled-leave or SCD-ear theorems.

## 8. Smallest surviving matching-closed block

Call an edge bank **matching-closed** when it retains every already-selected
forest predecessor and successor incident with each of its owner-map images;
cutting such an edge is a release/rethread and lies outside this definition.
The owner-map successor and predecessor relations close any selected SCD
ear edge to its entire directed component.  Therefore the smallest
matching-closed candidate full block containing that edge is precisely its
whole component, equipped with:

1. the owner rows (3.3);
2. the full maximal internal lower tower of Lemma 3.3, or every prescribed
   capped target row (4.1a) explicitly;
3. the one terminal sink socket (3.6);
4. the maximal common-`Q` test of Theorem 4.1;
5. the path-contact upper rows (2.2) for every target assigned to that
   component; and
6. signed residence from Theorem 5.1, the upper endpoint signatures
   (7.10), and the full clipped prefix/suffix lower source rays (7.12a).

No bounded ear-local block can certify intervals crossing an owner-map
attachment, and no unchanged global old-ground block exists by Theorem
6.1.  The exact remaining SCD theorem is consequently:

> construct component source blocks passing Theorem 4.1, the capped lower
> target rows (4.1a), and all required path-contact rows; then select one coloured
> port cycle satisfying Theorem 7.4 and the graphic cuts (7.27), whose
> ordered boundary signatures cover the exact missing banks (7.6), while
> preserving one simultaneous common-`Q` source, all clipped crossing
> lower rows, and signed residence.

This theorem is strictly downstream of the solved immediate palettes and
the assumed owner-map detachment.  A controlled-leave reservoir may enter
only after its frozen coordinate-cocycle defect is repaired, or through a
joint forest-plus-connector selection which never imposes that impossible
intermediate face.  The theorem is also distinct from a standalone
sidecar: all rail length must be
absorbed inside the already-budgeted component sectors or their
boundary-state weave.  The regular repeat design solves the singleton
connector cocycle, but not this physical/all-width/common-cap theorem.
