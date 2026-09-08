# Glue first, decorate last: an exact central Catalan reduction

Date: 2026-07-31  
Status: exact central-CLMT implication, exact path-backbone integrality, and
exact project-`m=5` calibration; no all-`m` supply, residence, shadow-braid,
or compiler theorem

## 0. Verdict

For the **central Catalan linear-matching problem**, a decoration need not
survive the ECO component glues.

There is a strictly weaker two-stage sufficient architecture.

1. Starting from the canonical middle-levels factor, choose a
   pairwise-disjoint, prefix-strict ECO incidence hypertree and execute it
   only as a physical component merger.  This produces one Hamilton cycle.
2. On that Hamilton cycle, execute a terminal alternating-circuit packet.
   It need not carry any accepting decoration at intermediate prefixes.  It
   is enough that the final Hamilton cycle has one Catalan decoration whose
   binary trace is a forest.

The second condition gives a perfect diamond matching whose physical lift
is a spanning `Cat_m`-path forest.  Thus it is a Catalan linear matching.

This route bypasses forced-owner alignment and the ownership-indexed local
channel oracle **during the ECO gluing stage**.  Those rows remain necessary
for the stronger repair-first/private-collar recursion, where one fixed
decoration and its occurrence routes must survive every glue.  They are not
logical prerequisites for the one-shot central CLMT implication proved
here.

There is one essential correction to the informal formulation.  A joint
alternating SDR alone is not enough: its binary trace can have the unique
cycle characterized by the decorated-cycle theorem.  The terminal packet
must produce a **forest Catalan decoration**, equivalently a joint
alternating SDR passing the binary-trace forest test.

For unrestricted alternating circuits, the second stage is not an
additional existential gate.  The symmetric difference of any two spanning
two-factors decomposes into alternating circuits.  Consequently, after any
raw Hamiltonization, a terminal repair packet exists if and only if some
Hamilton cycle with an accepting forest decoration exists.  The weakest
missing theorem in this middle-levels-supported lane is therefore the
**Decorated Middle Levels Theorem**, not a transparent-glue theorem or a
local-channel theorem.

The project-`m=5` three-`C10` construction already has exactly this order.
Two disjoint standard ECO atoms first join the three canonical components
into one Hamilton cycle.  The three `C10` circuits then give the exact
deficit staircase

\[
        (3,3,3)\longrightarrow(2,2,2)
        \longrightarrow(1,1,1)\longrightarrow(0,0,0),
\]

and the final cycle has a joint alternating SDR with forest trace.

## 1. Physical ECO Hamiltonization without a decoration

Let `F` be a simple spanning two-factor of a middle-levels graph, and let
`V` be its set of cycle components.  An ECO atom `Z` is an alternating
six-cycle.  Write

\[
 O_Z=E(Z)\cap E(F),\qquad N_Z=E(Z)\setminus E(F),
\]

so that `O_Z` and `N_Z` are the two three-edge matchings of the hexagon.
Let

\[
 S_Z=\{C\in V:C\text{ contains an edge of }O_Z\}.
\]

The component--atom incidence graph of a family `T` is the bipartite graph

\[
 B(V,T),\qquad CZ\in E(B)\iff C\in S_Z.                 \tag{1.1}
\]

### Definition 1.1 (prefix-strict ECO incidence hypertree)

A family `T` is a prefix-strict physical ECO incidence hypertree for `F`
when:

1. the six-vertex supports of its atoms are pairwise disjoint;
2. `B(V,T)` is a tree; and
3. in a hyperleaf order `Z_1,...,Z_s` of that incidence tree, every literal
   toggle

   \[
              F_j=F_{j-1}\mathbin\triangle E(Z_j),
              \qquad F_0=F,                            \tag{1.2}
   \]

   is an alternating degree-two move and merges the one already exposed
   block with the `|S_{Z_j}|-1` new branches, without a simultaneous split.

Condition 3 is a six-port physical phase test, not a decoration condition.
For a three-touch atom it is the clean three-component merge.  For a
two-touch atom it includes the doubled-side pairing test; the wrong pairing
can produce a four-cycle plus a two-cycle instead of a merge.  Thus the word
`strict` cannot be replaced by support connectivity alone.

### Theorem 1.2 (undecorated ECO Hamiltonization)

If `T` is a prefix-strict physical ECO incidence hypertree for `F`, then

\[
                   F_T=F\mathbin\triangle
                        \mathop{\triangle}_{Z\in T}E(Z)            \tag{1.3}
\]

is one spanning Hamilton cycle.

#### Proof

Pairwise disjoint alternating supports ensure that every `F_j` in (1.2) is
a simple spanning two-factor.  At step `j`, strictness decreases the number
of components by exactly `|S_{Z_j}|-1`.

Since the incidence graph is a tree,

\[
 \sum_{Z\in T}|S_Z|
      =|V|+|T|-1,
 \qquad
 \sum_{Z\in T}(|S_Z|-1)=|V|-1.                       \tag{1.4}
\]

Starting with `|V|` components, (1.4) and the strict decrement therefore
leave exactly one.  A connected simple spanning two-factor is a Hamilton
cycle.  Pairwise disjointness also makes the final symmetric difference
independent of the notation used for the hyperleaf order.  \(\square\)

No turn representative, gap matching, owner edge, occurrence channel, or
router resilience statement occurs in this theorem.

## 2. The integral path-backbone selector

Theorem 1.2 still needs an integral incidence hypertree.  There is an exact
positive face when its ordinary component backbone is a path.

Let

\[
                         A=v_0v_1\cdots v_N
\]

be a fixed path on the old components.  A binary ECO atom is a one-edge
tile and a ternary atom is a two-adjacent-edge tile.  More generally write
the induced interval tile of an allowed atom `t` as

\[
                 Q_t=\{e_{a_t+1},\ldots,e_{b_t}\},
                 \qquad 0\le a_t<b_t\le N.            \tag{2.1}
\]

Assume the bank has already been filtered for literal alternation, strict
phase, pairwise physical compatibility, and any other **fixed unary** row.

### Theorem 2.1 (path tile selection is integral)

The exact-cover relaxation

\[
 {\cal P}_A=\left\{x\ge0:
     \sum_{t:a_t<i\le b_t}x_t=1\quad(1\le i\le N)
                  \right\}                            \tag{2.2}
\]

is integral.  Its integral points are exactly the ECO incidence hypertrees
tiling the path `A`.

#### Proof

Make a directed acyclic multigraph on `0,1,...,N`, with one arc
`a_t -> b_t` for every labelled tile.  Subtracting two consecutive equations
of (2.2) gives flow conservation at each internal node; the first and last
equations give unit source outflow and unit sink inflow.  Conversely, every
unit source--sink flow crosses each path cut once and therefore satisfies
(2.2).  Thus (2.2) is exactly a unit-flow polytope.  Its matrix is a network
matrix, so every vertex is integral.  An integral unit flow is one directed
`0`-to-`N` path, whose arcs partition the backbone edges.  \(\square\)

This is sufficient, not without loss.  At `K_(1,3)`, the three ternary
pair-of-arm tiles have matrix

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad |\det|=2,                                    \tag{2.3}
\]

and unique fractional cover `(1/2,1/2,1/2)` but no integral cover.  More
generally, every nonpath tree contains the same degree-three obstruction
after forcing singleton tiles on all other edges.  Hence paths are exactly
the trees whose **abstract connected-subtree tile matrices** have universal
cover integrality for arity at most three under arbitrary unary filtering.
This does not assert that the determinant-two subcatalogue occurs in every
literal ECO bank on every nonpath backbone.

If collision phases or other finite boundary data must be selected jointly,
replace node `i` by states `(i,sigma)` and replace a tile by every authenticated
transfer arc

\[
                         (a_t,\sigma)\longrightarrow(b_t,\tau).    \tag{2.4}
\]

The product graph is still acyclic and its unit-flow polytope is still
integral.  This is an exact extended formulation.  It does **not** prove
that the required state family is uniformly bounded or that the ECO bank
supplies a source--sink path.

For the central glue-first route, ownership-indexed local-channel maxflow is
not part of this state.  If one wants a regenerative/private execution,
per-atom maxflow can be a unary filter only when all `Q`-state networks and
their unit semantics are frozen and the selected banks are globally
private.  Two locally feasible atoms may otherwise share one capacity-one
router vertex and fail simultaneously.

## 3. Terminal decoration repair

Fix

\[
 Q={2m-1\choose m-1},\qquad
 P={2m-1\choose m-2},\qquad
 K=Q-P=\operatorname {Cat}_m.                         \tag{3.1}
\]

Write a Hamilton cycle of `ML(2m-1)` as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.                \tag{3.2}
\]

Its two turn words are

\[
       \ell_i=A_i\cap A_{i+1},
       \qquad u_i=B_{i-1}\cup B_i.                    \tag{3.3}
\]

A **forest Catalan decoration** is a pair of occurrence sets `(I,J)` such
that:

1. `i -> u_i` bijects `I` with all rank-`m+1` targets;
2. `j -> ell_j` bijects `J` with all rank-`m-2` targets;
3. the selected `A`- and `B`-occurrences alternate cyclically; and
4. the associated binary mark trace is a forest.

The fourth row is equivalently the failure of the unique cyclic case:
every positive zero-run has length two and every maximal one-run has odd
length.

### Theorem 3.1 (terminal decorated-cycle implication)

Let `H` be a Hamilton cycle.  Let `C_1,...,C_r` be a literal packet of
alternating even circuits, and put

\[
 H_j=H_{j-1}\mathbin\triangle E(C_j),\qquad H_0=H.     \tag{3.4}
\]

Assume the packet is physically legal and `H_r` is Hamilton.  If `H_r`
has a forest Catalan decoration, then `H_r` supports a Catalan linear
matching: a perfect diamond matching whose physical lift is a spanning
linear forest with exactly `K=Cat_m` path components.

No decoration is required on `H_0,...,H_(r-1)`.

#### Proof

The two turn bijections and cyclic alternation are exactly the hypotheses
of the decorated-cycle/perfect-diamond equivalence.  They produce a perfect
matching of the lower--upper diamond graph supported by the two turn families
and the forced residual cross matching.

Its physical lift has maximum degree two and

\[
              |V|=2Q,\qquad |E|=P+Q.                 \tag{3.5}
\]

The binary-trace theorem says row 4 is exactly acyclicity of this physical
lift.  It is therefore a spanning linear forest, and Euler's identity gives

\[
              \#\text{paths}=|V|-|E|=Q-P=K.           \tag{3.6}
\]

This is precisely the supported Catalan linear matching.  \(\square\)

### Corollary 3.2 (glue-first/decorate-last theorem)

If a canonical middle-levels factor has

1. a prefix-strict pairwise-disjoint ECO incidence hypertree, and
2. on the resulting Hamilton cycle, a terminal circuit packet whose endpoint
   has a forest Catalan decoration,

then a Catalan linear matching exists.

This implication is exact within the declared middle-levels-supported
architecture.  It does not claim that every abstract Catalan linear matching
has such a representation.

### Theorem 3.3 (alternating-circuit universality)

Let `F` and `F'` be any two spanning two-factors of the same graph.  Then

\[
                         F\mathbin\triangle F'
       =Z_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}Z_s            \tag{3.7}
\]

for edge-disjoint closed circuits, in the closed alternating-trail/
transition-state sense, which alternate between edges of
`F\F'` and edges of `F'\F`.  Toggling them successively takes `F` to `F'`
through spanning two-factors.  Every unprocessed circuit remains alternating
after every earlier toggle.

#### Proof

Colour `F\F'` red and `F'\F` blue.  At every vertex the red and blue
degrees agree, because both `F` and `F'` have degree two.  Pair red and blue
half-edges at each vertex and follow the pairings.  This partitions the
coloured graph into closed alternating trails; split a trail at repeated
transition states to obtain (3.7).  On toggling one circuit, every incident
vertex loses one red edge and gains one blue edge, so degree two is
preserved.  Edge-disjointness leaves every later circuit alternating.  At
the end exactly the red edges have been removed and the blue edges inserted.
\(\square\)

### Corollary 3.4 (post-glue repair equivalence)

Fix **any** Hamilton cycle `C_0` of `ML(2m-1)`.  The following are
equivalent.

1. Some Hamilton cycle `C_*` of `ML(2m-1)` has a forest Catalan
   decoration.
2. An alternating-circuit packet takes `C_0` through two-factors to a
   terminal Hamilton cycle with a forest Catalan decoration.

Theorem 3.3 proves `1 -> 2`; the reverse direction reads the terminal
state.  Intermediate factors need not be Hamilton and need not carry any
decoration.  Requiring every `C10` prefix to be Hamilton-safe, as in the
finite `m=5` fixture, is a useful constructive strengthening but is not part
of the existential equivalence.

## 4. The exact project-`m=5` post-glue reading

The frozen `m=5` audit supplies Corollary 3.2 literally.

The canonical factor has component orders

\[
                            36,72,144.                 \tag{4.1}
\]

Use the two standard ECO atoms

\[
 \begin{aligned}
  Z_0 &: 11001010\leftrightarrow10101010,\\
  Z_1 &: 11001100\leftrightarrow10101100.
 \end{aligned}                                        \tag{4.2}
\]

Their six-port banks are respectively

\[
 \{83,85,87,89,91,93\},
 \qquad
 \{51,53,55,57,59,61\},                              \tag{4.3}
\]

so they are vertex- and edge-disjoint.  Relative to the three canonical
components their supports are `{0,2}` and `{1,2}`.  Hence the component--atom
incidence graph is the path

\[
                  0-Z_0-2-Z_1-1.                     \tag{4.4}
\]

Each one-atom state has two components, of orders `(72,180)` or `(36,216)`,
and toggling both atoms gives one Hamilton cycle of order `252`.  This is
Stage A.

Starting from that Hamilton cycle, the three displayed vertex-disjoint
`C10` circuits in the frozen repair audit are alternating and Hamilton-safe
at every prefix.  They give the deficit staircase in Section 0.  At the
last state, the exact augmented occurrence graph has a perfect matching of
size `210`; its selected sets have `|I|=|J|=84`, and the binary trace is a
forest.  Theorem 3.1 therefore gives `Cat_5=42` physical paths.  This is
Stage B.

This calibration must not be confused with the separate repaired-pre-glue
statement.  In the post-glue reading, the **two standard atoms** in (4.2)
Hamiltonize first and the three `C10` circuits repair the resulting cycle.
The later fixed-rotation audit instead commutes the disjoint supports to
exhibit one-atom repair-first endpoints.  Both are true, but they certify
different quantifier orders.

## 5. Comparison with repair-first private collars

The two architectures have different strengths.

| row | glue first, decorate last | repair first, private collar |
|---|---|---|
| ECO topology | strict disjoint incidence hypertree | strict common-cube hypertree |
| decoration during glues | none | one transported joint decoration |
| owner alignment | not needed during Stage A | literal forced owners at every selected atom |
| local channels | not needed for central CLMT | all ownership states plus global private/laminar composition |
| repair obligation | terminal packet on the chosen Hamilton cycle | preliminary packet exporting a compatible bank |
| output | one central CLMT | central CLMT plus a candidate regenerative collar state |
| residence/deep shadows/compiler | not implied | still not implied unless separately exported |

Thus glue-first/decorate-last is genuinely weaker as a **central
certificate**.  It allows the final decoration to depend globally on the
Hamilton cycle and discards it after constructing the CLMT.

The two existence hypotheses are not equivalent.  A terminal repair may
depend on the chosen glue tree and fail before gluing; a preliminary repair
may destroy every undecorated strict hypertree unless owner-compatible glues
are chosen afterward.  They may be reordered only under an explicit common-
cube/commutation hypothesis: disjoint supports, preservation of the required
old edges, and literal legality of every prefix in the new order.  Equality
of final symmetric differences alone does not certify prefix legality.

The repaired fixed-rotation `m=5` interface also needs one wording caution.
It preserves the same marked occurrence sets and the unique-matching
property, but the pointwise gap matching is re-derived after a toggle and
need not equal the old matching.  This has no effect on the post-glue
theorem, which chooses its decoration only at the terminal Hamilton cycle.

### 5.1 Transparent gluing is a stronger constructive route

The repaired `ML(7)` example makes the quantifier distinction literal.  A
hexagon toggle preserves one **fixed** decoration exactly when:

1. the selected local turn-colour multisets agree before and after the
   toggle, separately on the two shores; and
2. after the three retained fragments are reconnected, the last selected
   shore type on each nonempty fragment is opposite the first selected
   shore type on the next fragment.

These are the exact palette and boundary-alternation tests.  A recursive
transparent gluing tree must carry one joint alternating SDR and impose
both tests at every glue; separate turn rainbows, an arbitrary frozen SDR,
or an arbitrary gluing tree do not suffice.

The complete `ML(7)` neighbourhood separates this stronger route from the
minimal existential route:

\[
 31\text{ alternating hexagons},\quad
 16\text{ Hamilton outputs},\quad
 10\text{ decorable outputs},\quad
 6\text{ outputs with a common forest decoration}.                \tag{5.1}
\]

The ten decorable outputs are available to the post-glue endpoint search.
Only the six common rows are transparent transfers of one already chosen
decoration.  One ordinary hexagon repairs the explicit gap--Hall
counterexample to a decorable `ML(7)` cycle, so the minimal route is already
strictly more permissive in the first nontrivial fixture.

Leaf-peelable transparent gluing remains an excellent recursive sufficient
construction: it gives finite local transfer rules and a deterministic
residual matching.  It is not a necessary interface for central existence.

## 6. The weakest exact missing theorem

For a constructive ECO implementation one may still pursue two statements:

**A. Undecorated ECO Hamiltonization.**  The canonical factor has a
pairwise-disjoint prefix-strict ECO incidence hypertree.  A fixed component
path is especially useful because its tile selector is integral by
Theorem 2.1.

**B. Terminal Hamilton repair.**  The resulting Hamilton cycle has a legal
alternating-circuit packet whose endpoint admits a forest Catalan
decoration.

Connected ECO two-section supply does not imply A, and separate two-turn
surjectivity does not imply B.  But by Corollary 3.4, once any Hamilton
cycle is available, B has exactly the same existential content as the
accepting endpoint.  Hence A+B is not the weakest theorem statement.

The weakest exact missing theorem in the present trace lane is:

> **Decorated Middle Levels Theorem.**  For every `m>=2`,
> `ML(2m-1)` contains a Hamilton cycle with a Catalan decoration whose
> binary trace is on the linear-forest side.

A leaf-peelable decorated cycle and a transparent leaf-peelable gluing tree
are stronger recursive targets.  A prescribed period-three filter bank is
stronger again: the authenticated repaired `m=5` cycle is decorable while
none of the `729` complete complement-paired filter banks is supported on
it.  Thus exceptional filters should be read from the terminal matching or
chosen jointly with it, not imposed as a prerequisite for the minimal
theorem.

The Decorated Middle Levels Theorem is sufficient for the central Catalan
linear matching **inside the middle-levels-resolvable architecture**.  It is
not claimed necessary for an arbitrary Catalan linear matching, since an
abstract diamond matching need not admit a Hamilton middle-levels support.

For the full coefficient-one word theorem, even A+B is only the central
layer.  Residence, all deeper interval shadows, sockets/voltage, Pascal
reachability, and the integral lower compiler must be certified on the final
chronology.  A terminal circuit packet can change each of them.  Therefore
this note proves no RSB preservation and no all-`k` statement.

## 7. Provenance

The central equivalence and binary-trace criterion are in
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`.
The transparent six-port criterion and its `ML(7)` census are in
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`.
The exact alternating-circuit equivalence and period-three support gate are
in `MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_AND_PERIOD3_SUPPORT_GATE_20260731.md`.
The exact path selector and branching obstruction are in
`MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md` and
`MATH_AUDIT_AD_ECO_COMPONENT_TREE_TILING_AND_BRANCH_OBSTRUCTION_20260731.md`.
The finite post-glue packet is replayed by
`scratch/audit_catalan_standard_m5_three_c10_private_repair_20260731.py`.
The commuting repair-first fixed-rotation endpoint is independently replayed
by `scratch/audit_catalan_m5_repair_fixed_rotation_eco_integration_20260731.py`.

No numerical claim in Section 4 depends on a SAT or probabilistic search.
The frozen audits reconstruct the factors, physical circuits, component
orders, occurrence matching, and binary trace literally.
