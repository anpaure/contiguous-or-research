# Terminal ECO Hamiltonization, post-glue equivalence, and transparent repair

Date: 2026-07-31  
Status: exact independent audit of the post-glue equivalence and the two
central construction routes; exact project-\(m=4,5\) calibration; no
all-dimension decorated-Hamilton theorem and no residence, RSB, socket,
voltage, or compiler claim

## 0. Scope correction and verdict

Fix the paper parameter \(m\ge2\), and put

\[
 \Omega=[2m-1],\qquad
 Q={2m-1\choose m-1},\qquad
 P={2m-1\choose m-2},\qquad
 K=Q-P=\operatorname {Cat}_m.                       \tag{0.1}
\]

The canonical MMM factor is a two-factor of the middle-levels graph
\({\rm ML}(2m-1)\).  The earlier private-collar architecture asked one joint
decoration to survive while its factor components were glued.  That is a
valid recursive sufficient condition, but it is not necessary for the
**central** Catalan linear-matching theorem.

One useful sufficient construction factors into two terminal stages.

### Stage A: undecorated ECO Hamiltonization

Choose one pairwise port-disjoint, strict, component-faithful ECO incidence
hypertree on the canonical factor.  Toggle its atoms literally.  The only
required conclusion is one Hamilton cycle \(C\) of
\({\rm ML}(2m-1)\).  No upper transversal, gap matching, forced owner,
occurrence router, or common decorated cube is required.

This is an ECO-specific way to produce the starting Hamilton cycle, not a
necessary central gate.  The ordinary Middle Levels theorem already gives
some Hamilton cycle in every dimension.

### Stage B: post-glue terminal repair

Starting from \(C\), apply an arbitrary literal circuit/rethread packet
whose endpoint \(C^*\) is again a Hamilton cycle.  Only at \(C^*\) choose a
joint alternating turn-occurrence SDR.  Its binary trace must lie on the
forest side of the exact trace criterion.

Then \(C^*\) lifts to a Catalan linear matching: a spanning path forest in
\(J(2m,m)\) with exactly \(K\) components, using every rank-\((m-1)\)
intersection colour and every rank-\((m+1)\) union colour exactly once.

Thus the proof-safe central order is

\[
 \boxed{
 \text{strict disjoint ECO Hamiltonization}
 \longrightarrow
 \text{Hamilton-safe terminal circuit repair}
 \longrightarrow
 \text{one final forest-side Catalan decoration}.}                \tag{0.2}
\]

This bypasses forced-owner and occurrence-router preservation **during the
ECO gluing stage**.  It does not bypass the final occurrence-level matching
problem, and it does not preserve any downstream residence or RSB state.

The raw project-\(m=5\) result must therefore be read in two different ways.
It closes raw **decoration-preserving** ECO recursion, since every minimal
raw endpoint initially misses the same three colours on each shore.  It does
not close raw **undecorated Hamiltonization**.  Indeed the standard two-ECO
Hamilton endpoint followed by the three-\(C10\) packet is the exact finite
positive instance of (0.2).

There is a further exact simplification.  The symmetric difference of any
two two-factors decomposes into alternating circuits, and toggling those
circuits successively stays within two-factors.  Consequently, after *any*
Hamilton cycle has been obtained,

\[
 \boxed{
 \text{a post-glue repair to an accepting endpoint exists}
 \iff
 \text{some accepting decorated Hamilton cycle exists}.}         \tag{0.3}
\]

Intermediate factors need not be Hamiltonian or decorated.  Thus the
weakest exact missing theorem in this middle-levels-resolvable lane is the
**Decorated Middle Levels Theorem**: one forest-side Catalan-decorated
Hamilton cycle exists for every \(m\).  Raw ECO Hamiltonization and a named
repair packet are useful construction certificates, not additional
existential gates.

## 1. Stage A: literal strict ECO Hamiltonization

Let \(F_0\) be a spanning two-factor of \({\rm ML}(2m-1)\), and let
\(\mathcal V\) be its component set.  An ECO atom \(t\) has three old
factor edges \(E_0(t)\), three new edges \(E_1(t)\), and a six-vertex port
set.  Put

\[
 S_t=\{V\in\mathcal V:E(V)\cap E_0(t)\ne\varnothing\},
 \qquad r_t=|S_t|.                                  \tag{1.1}
\]

Only positive-rank atoms with \(r_t\in\{2,3\}\) belong to the bank.  An
\(r_t=1\) toggle is a neutral rethread or split candidate and is not a
component-hypertree edge.

A family \(\mathcal T\) is a **terminal ECO bank** when:

1. the six-port sets of distinct atoms are disjoint;
2. every \(E_0(t)\) lies in \(F_0\), so all toggles are simultaneously
   literal and commute;
3. the component--atom incidence graph

   \[
    B(\mathcal V,\mathcal T),\qquad Vt\in E(B)\iff V\in S_t,       \tag{1.2}
   \]

   is a tree; and
4. the atoms are strict and component-faithful on the resulting cube:
   whenever the current blocks meeting \(S_t\) are distinct, toggling
   \(t\) merges exactly those blocks and splits none.

For a ternary atom whose old edges lie on three distinct current cycles,
item 4 is automatic.  For a binary atom, two old edges can lie on one
cycle, and the literal doubled-side pairing must be checked; support size
two alone is not enough.

### Theorem 1.1 (terminal ECO Hamiltonization)

For a terminal ECO bank,

\[
                 C=F_0\mathbin\triangle
                   \mathop{\triangle}_{t\in\mathcal T}
                       \bigl(E_0(t)\cup E_1(t)\bigr)              \tag{1.3}
\]

is one Hamilton cycle of \({\rm ML}(2m-1)\).  Every ordering of the atoms
is a valid component-progressing execution.

#### Proof

Port disjointness makes all local symmetric differences commute and leaves
every pending old matching present.  Hence every subset state is a spanning
two-factor.

We prove the required physical/incidence correspondence by induction.  For
a processed set \(A\subseteq\mathcal T\), let \(B_A\) be the subgraph of
\(B(\mathcal V,\mathcal T)\) containing every component vertex and just the
atom nodes in \(A\).  The induction invariant is:

> the physical components of the subset factor are in bijection with the
> connected components of \(B_A\), via their original component vertices.

It is true for \(A=\varnothing\).  Let \(t\notin A\).  No two vertices of
\(S_t\) can lie in one component of \(B_A\): a path between them in
\(B_A\), together with their two incidences through the unused node \(t\),
would be a cycle in the full incidence tree.  By the induction invariant,
the physical blocks meeting \(S_t\) are therefore distinct.  Strict
component faithfulness merges exactly those blocks and splits none, which
is exactly the change in connected-component partition from \(B_A\) to
\(B_{A\cup\{t\}}\).  This proves the invariant and also shows that every
atom order is valid.

The incidence tree identity is

\[
                    \sum_{t\in\mathcal T}(r_t-1)
                         =|\mathcal V|-1.                         \tag{1.4}
\]

Therefore the component count falls from \(|\mathcal V|\) to one.  The
final two-factor is connected, hence is one Hamilton cycle. \(\square\)

No decoration or router statement occurs in the proof.  The router was a
selection/composition device for carrying one decoration through a family
of alternatives; it is not needed to certify a displayed set of commuting
literal factor toggles.

## 2. Stage B: a terminal Hamilton repair packet

Let

\[
                    C=C^{(0)},C^{(1)},\ldots,C^{(s)}=C^*          \tag{2.1}
\]

be a sequence of literal spanning two-factors on the same middle-levels
vertices.  For each \(j\), let \(R_j\) be an even circuit alternating with
\(C^{(j-1)}\), and put

\[
                    C^{(j)}=C^{(j-1)}\triangle R_j.               \tag{2.2}
\]

Call the sequence a **terminal Hamilton repair packet** when \(C^*\) is a
Hamilton cycle.  A Hamilton-safe packet, in which every \(C^{(j)}\) is
Hamilton, is a convenient stronger certificate but is not needed by the
serial implication.  The circuits may overlap earlier ECO ports and need
not commute with Stage A; only the literal sequential transitions and the
terminal Hamilton property matter.

Write the terminal Hamilton cycle as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,                     \tag{2.3}
\]

where \(|A_i|=m-1\), \(|B_i|=m\), and
\(A_i\subset B_i\supset A_{i+1}\).  Its turn colours are

\[
 \ell_i=A_i\cap A_{i+1},qquad
 u_i=B_{i-1}\cup B_i.                               \tag{2.4}
\]

A terminal mark pair \((I,J)\), with
\(I,J\subseteq\mathbb Z_Q\), is **CLMT-accepting** when:

1. \(i\mapsto u_i\) is a bijection from \(I\) to
   \({\Omega\choose m+1}\);
2. \(j\mapsto\ell_j\) is a bijection from \(J\) to
   \({\Omega\choose m-2}\);
3. the marked \(A\)- and \(B\)-positions alternate in cyclic order; and
4. the induced binary mark trace is on the forest side:
   either some positive unmarked run has length at least four, or some
   maximal run of consecutive marks has even length.

Items 1--3 are the joint alternating SDR.  Item 4 is load-bearing.  Without
it the associated physical degree-two graph can contain one cycle.  An
augmented perfect matching or two turn surjections alone is therefore not a
complete Stage-B certificate.

### Theorem 2.1 (terminal decoration lift)

If \(C^*\) has a CLMT-accepting mark pair, then it determines a spanning
path forest \(L(C^*,I,J)\) in \(J(2m,m)\) such that:

1. every rank-\((m-1)\) intersection colour is used exactly once;
2. every rank-\((m+1)\) union colour is used exactly once;
3. the number of edges is

   \[
                         P+Q=mK;                                  \tag{2.5}
   \]

4. the number of vertices is \(2Q=(m+1)K\); and
5. the number of path components is exactly \(K\).

#### Proof

Items 1--3 of the accepting definition are precisely a Catalan decoration
of the terminal middle-levels cycle.  The decorated-cycle/perfect-diamond
equivalence supplies one perfect lower--upper diamond matching.  Its
physical lift has maximum degree two, uses both colour shores bijectively,
and has \(P+Q\) edges on \(2Q\) vertices.

The exact binary-trace theorem says that this lift has a cycle if and only
if every positive unmarked run has length two and every maximal marked run
has odd length.  Item 4 is exactly the negation, so the lift is a forest.
Euler's identity gives

\[
                 2Q-(P+Q)=Q-P=K                              \tag{2.6}
\]

components. \(\square\)

This is the middle-levels-resolvable sufficient subclass of Catalan linear
matchings.  No claim is made that every Catalan linear matching arises from
one Hamilton cycle.

## 3. Exact serial implication

### Theorem 3.1 (terminal ECO plus final repair implies CLMT)

For a fixed \(m\), assume:

1. the canonical MMM factor has a terminal ECO bank \(\mathcal T\); and
2. its Hamilton endpoint \(C\) has a terminal Hamilton repair packet whose
   endpoint \(C^*\) has a CLMT-accepting mark pair.

Then a Catalan linear matching exists at parameter \(m\).

#### Proof

Theorem 1.1 gives the literal Hamilton cycle \(C\).  The repair packet gives
the literal terminal Hamilton cycle \(C^*\).  Theorem 2.1 lifts its final
decoration to the required spanning \(K\)-path rainbow forest. \(\square\)

The quantifiers are serial:

\[
  \exists\mathcal T\quad
  \exists\text{ repair packet depending on }C(\mathcal T)\quad
  \exists(I,J)\text{ only on the terminal }C^*.                   \tag{3.1}
\]

There is no common-decoration quantifier over the ECO cube.  In particular,
the raw ECO atoms need not expose any forced owner edges which extend to
the final \((I,J)\).

### Theorem 3.2 (alternating closed-trail universality)

Let \(F,F'\) be any two spanning two-factors of the same graph.  Then
\(F\triangle F'\) decomposes into edge-disjoint closed trails alternating
between \(F\setminus F'\) and \(F'\setminus F\).  Toggling these trails
successively transforms \(F\) into \(F'\), and every intermediate graph is
a spanning two-factor.  If the ambient graph is bipartite, the trails may
be recursively split into simple alternating even cycles.

#### Proof

Colour \(F\setminus F'\) red and \(F'\setminus F\) blue.  At each vertex
the red and blue degrees agree, because both factors have degree two.  Pair
red and blue half-edges at every vertex and follow the pairings.  This
decomposes the symmetric difference into edge-disjoint closed alternating
trails.  In a bipartite graph, a repeated vertex cuts such a trail into two
even closed alternating trails, so recursion gives simple alternating even
cycles.  In a general nonbipartite graph this last simple-cycle conclusion
need not hold, and the closed-trail formulation is the exact one.

Toggling one trail removes and inserts equally many incident edges at every
visited vertex, so every vertex retains degree two.  Since the trails are
edge-disjoint, every unprocessed red edge is still present and every
unprocessed blue edge is still absent; hence the remaining trails stay
alternating.  After all toggles the factor is \(F'\). \(\square\)

Intermediate factors need not be connected.  Requiring a Hamilton cycle at
every prefix is a stronger routing normal form, not an existential
necessity.

### Corollary 3.3 (post-glue repair equivalence)

Fix any Hamilton cycle \(C_0\) of \({\rm ML}(2m-1)\).  The following are
equivalent.

1. Some Hamilton cycle of \({\rm ML}(2m-1)\) has a CLMT-accepting mark pair.
2. An alternating-circuit packet transforms \(C_0\), through two-factors,
   into a terminal Hamilton cycle with a CLMT-accepting mark pair.

#### Proof

Item 2 implies Item 1 by reading its endpoint.  For Item 1 implies Item 2,
apply Theorem 3.2 to \(C_0\) and the accepting Hamilton cycle. \(\square\)

Thus circuit realization is not an additional existential gate.  Since the
ordinary Middle Levels theorem supplies \(C_0\), the weakest exact missing
statement in this architecture is simply existence of the accepting
terminal Hamilton cycle.

### Corollary 3.4 (ECO-specific sufficient reduction)

To prove the central Catalan linear-matching theorem for all \(m\), it is
sufficient to prove independently for every \(m\):

* **A\(_m\):** the canonical factor has a pairwise-disjoint strict ECO
  incidence hypertree; and
* **B\(_m(C)\):** the resulting Hamilton cycle admits a terminal circuit
  repair to a CLMT-accepting Hamilton cycle.

Stage B may depend on the Stage-A endpoint.  A uniform repair packet which
works for every possible Stage-A endpoint is not required.

This two-stage ECO reduction is stronger than necessary.  By Corollary 3.3,
one may replace both bullets by the single **Decorated Middle Levels
Theorem**:

> for every \(m\ge2\), \({\rm ML}(2m-1)\) has a Hamilton cycle with a
> CLMT-accepting mark pair.

This is the weakest missing theorem in the middle-levels-resolvable route.
It remains a sufficient architecture for Catalan linear matching, not a
normal form for every possible Catalan linear matching.

## 4. Project-\(m=5\) is the exact positive base

At project \(m=5\), the canonical factor has three components.  The two
standard coherent ECO atoms used in the frozen standard construction are
port-disjoint strict merges and form an incidence tree.  Their raw endpoint
is a Hamilton cycle.  It initially misses the lower colours

\[
                         \{73,146,292\}                            \tag{4.1}
\]

and the complementary upper colours

\[
                         \{219,365,438\}.                          \tag{4.2}
\]

Thus it has no decoration before repair.  This is not a failure of Stage A.

The three frozen, pairwise vertex-disjoint \(C10\) circuits form a
Hamilton-safe terminal packet.  Their exact deficit staircase is

\[
              (3,3,3)\to(2,2,2)\to(1,1,1)\to(0,0,0),             \tag{4.3}
\]

where the coordinates are lower-palette deficit, upper-palette deficit, and
joint alternating-SDR deficiency.  The endpoint has a forced perfect
augmented matching of order 210, an alternating \(84+84\) mark pair, and a
binary trace on the forest side.  Theorem 3.1 therefore gives the project-
\(m=5\) Catalan linear matching in the literal post-glue order

\[
        \text{two ECO glues}\longrightarrow\text{three }C10
        \text{ repairs}\longrightarrow\text{terminal decoration}. \tag{4.4}
\]

The same circuits are disjoint from the two ECO collars, so the existing
audit can commute them before the glues and prove the stronger repair-first
private-collar theorem.  That commutation, the common forced-port
decoration on all four cube states, and the compiled \(g_1\) router arc are
surplus for the central implication (4.4).  They remain valuable for a
recursive prepared-state induction.

Hence the raw project-\(m=5\) census now has the exact interpretation:

\[
 \boxed{
 \text{raw decoration-preserving ECO is false, but raw undecorated ECO
 Hamiltonization plus terminal repair is true}.}                  \tag{4.5}
\]

## 5. The two exact routes and their strength

### 5.1 Minimal existential route

Corollary 3.3 shows that the minimal route stores only one accepting
terminal Hamilton cycle.  It does not require during the construction:

* a common upper transversal on earlier factors;
* a gap--lower-colour matching or owner alignment through glues;
* preservation of occurrence representatives through any ECO prefix;
* private/laminar occurrence-router channels;
* a repair packet disjoint from or commuting with earlier glues; or
* decoration validity on any nonterminal state.

Even Stage A is optional once ordinary Middle Levels Hamiltonicity is used.
The phrase “post-glue repair packet” is only a way of exhibiting the target
cycle; Theorem 3.2 proves that its existence is equivalent to the target
cycle itself.

Likewise, a preassigned exceptional filter bank is not part of the weakest
terminal statement.  At project \(m=5\), the authenticated accepting cycle
supports none of the 729 complete complement-paired period-three banks from
the explicit filter construction.  The terminal decoration nevertheless
exists.  Thus exceptional filters must either be chosen jointly with the
terminal Hamilton cycle or read from its final matching; fixing them first
is a strictly stronger support/Hall route.

### 5.2 Recursive transparent-gluing route

The transparent route is a stronger sufficient induction.  It starts with a
componentwise joint decoration and asks every gluing hexagon to preserve the
same selected occurrence sets.  For one hexagon this is exact if and only if:

1. the selected local turn-colour multisets agree before and after,
   separately on both shores; and
2. after the three retained path fragments are reoriented by the new
   matching, the last selected shore type of each nonempty fragment and the
   first selected shore type of the next fragment are opposite.

A protected trace breaker, or the exact bit excluding the unique cycle
face, preserves linearity.  If leaf-peelability is carried, the changed gap
edges must additionally form a loopless forest after the unchanged gap
forest is contracted.

Thus the recursive sufficient theorem is

\[
 \boxed{
 \text{one componentwise joint alternating SDR}
 +\text{ one dynamically transparent gluing tree}
 \Longrightarrow\text{ one accepting decorated Hamilton cycle}.} \tag{5.1}
\]

Separate lower/upper rainbows, an arbitrary frozen SDR, and an arbitrary
Middle Levels gluing tree do not imply (5.1).  The exact \(m=4\) census
locates the gap: among 31 alternating hexagons, 16 yield Hamilton cycles,
10 of those endpoints are decorable, and only 6 admit a common forest
decoration.  One incidence-hex toggle repairs the explicit nondecorable
\({\rm ML}(7)\) cycle, illustrating the terminal route; the six common rows
show that the transparent route is nonempty but strictly more constrained.

### 5.3 Repair-first private collar

The repair-first private collar strengthens the transparent route further
by demanding a leaf-forest owner matching, component-faithful merge state,
and private/laminar occurrence routing on the same labels.  These data are
useful for a leaf-peelable recursion and for stable downstream sockets, but
they are not a necessary interface for the minimal central existence
theorem.

A terminal construction may overlap and destroy every earlier collar.  A
repair-first construction may create atoms whose raw component effects do
not Hamiltonize the unprepared factor.  The global antecedents are therefore
not comparable without a literal commutation/transport certificate.

### 5.4 Exact project-\(m=5\) comparison

The three-\(C10\) circuits are disjoint from the two standard ECO collars,
so their symmetric differences commute.  But the selected component banks
on the two sides are different.

* In terminal order, the raw factor has component orders \(36,72,144\), and
  the strict path-incidence tree is \(\{g_0,g_1\}\); both atoms are needed
  to reach one 252-cycle.
* After the repair, the preglue factor has component orders \(120,132\), and
  either singleton \(\{g_0\}\) or \(\{g_1\}\) already Hamiltonizes it.
  Selecting both is a dependent parallel/rethread state, not the same
  incidence tree.

Hence the fixture proves both architectures and endpoint commutation, but
not by reversing one common selected hypertree.  The common forced-port
decoration and compiled \(g_1\) route are surplus for the terminal proof and
essential data for the stronger repair-first interpretation.

## 6. What remains downstream

The conclusion of Theorem 3.1 concerns only the central Catalan
linear-matching gate.  It does not produce a literal contiguous-OR word.

1. A terminal circuit repair may change deep upper/lower flags.  Turn
   palettes are only the immediate two shores; all-depth RSB support must be
   replayed or guarded at \(C^*\).
2. The resulting \(K\)-path forest can have short internal coordinate runs.
   Residence is a separate run-redistribution problem.
3. The path components still need compatible endpoints, sockets, and
   primitive-voltage closure.
4. The erosion letters, staircase deadlines, and common-\(Q\) compiler Hall
   state must be built on the final literal chronology.

After the decoration, physical diamond lift, and connector chronology have
all been fixed, suppose two literal rank-\(m\) owner chronologies on the same
occurrences differ by \(s\) seams.  Then the exact boundary-window theorem
limits the depth-\(q\) signed occurrence delta to at most \(qs\) old and
\(qs\) new boundary occurrences.  The support of the alternating circuits
in the middle-levels graph does **not** by itself determine this physical
\(s\): representative choices and path closure intervene.  Even when \(s\)
is known, the bound is a localization ledger, not a coverage theorem; one
removed occurrence may be the unique witness of its target.

Thus the next downstream alternatives are exactly:

* regenerate the complete RSB/residence/compiler state after Stage B; or
* require the terminal packet to export protected occurrence spans and the
  exact physical-seam halo guards.

## 7. Exact proved/open boundary

Proved:

1. strict disjoint ECO incidence hypertree \(\Rightarrow\) one undecorated
   Hamilton middle-levels cycle;
2. terminal Hamilton repair plus a forest-side Catalan decoration
   \(\Rightarrow\) one Catalan linear matching;
3. alternating-circuit universality for two-factors and the exact post-glue
   equivalence;
4. the exact transparent-hex transfer interface and its relation to the
   minimal terminal route;
5. the project-\(m=4,5\) route comparison; and
6. the precise strength comparison with the repair-first private collar.

Open:

1. the weakest central gate: the Decorated Middle Levels Theorem in every
   \(m\);
2. as a stronger recursive route, a joint alternating SDR plus a dynamically
   transparent, trace-safe gluing tree (leaf-peelable if that stronger state
   is desired);
3. as an optional ECO-specific construction, a raw strict disjoint
   incidence hypertree in every dimension;
4. quantitative short/local normal forms for reaching an accepting terminal
   cycle, although circuit existence itself is automatic;
5. residence and all-depth RSB preservation/regeneration;
6. sockets/voltage and the common-\(Q\) compiler; and
7. the contiguous-OR coefficient-one theorem.

## 8. Dependencies

* `MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`
* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`
* `MATH_THEOREM_CATALAN_ECO_COMPATIBLE_HYPERTREE_PRIVATE_COLLAR_20260731.md`
* `MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`
* `MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`
* `MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_AND_PERIOD3_SUPPORT_GATE_20260731.md`
* `MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md`
