# Protected Catalan--pivot connectors: a literal overlap theorem and the exact remaining gate

**Date:** 2026-08-02  
**Lane:** K, protected Catalan/pivot synthesis  
**Status:** unconditional composition and an exact sufficient-subclass
reduction.  The theorem
below proves that a literal upper-tower/residence-decorated Catalan forest
plus a guarded Catalan port path gives the required protected owner
chronology.  It does not construct that joint forest/path for all `m`.

## 0. Outcome

Put

\[
 W={2m-1\choose m},\qquad U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m.                           \tag{0.1}
\]

For the depth-`d` source ledger in this note write `B=W+d`.

The sharp pivot collar supplies a literal depth-`d` block whose final
owner row is a simple Johnson path of `3d+1` owners, whose immediate lower
and upper transition colours are injective, whose internal positive runs
in the owner traces have length at least `d+1`, and whose monotone insertion transports every
old interval-OR occurrence at every width.  Its singleton and two nested
rays have the exact zero-damage lower-compiler ledger.  Choosing the
predecessor matching phase turns its successor incidences into one rooted
directed path.  These are unconditional local facts.

The global owner-layer target has an exact forced decomposition.  An
upper-exact rooted Catalan forest has `U` links and therefore `C` directed
path components.  Joining it without deleting an upper representative uses
exactly `C-1` free-port links.  Because every component has only one free
head and one free tail, this ``connector tree'' is necessarily a directed
Hamilton path, not a branching tree.

There is a source-level qualification which is absent from the abstract
rooted-link statement.  A Johnson path component need not possess a common
depth-`d` antecedent, and an abstract free-port incidence need not splice two
antecedents without creating `d` extra middle windows.  A clean sufficient
physical port is a **literal `d`-overlap port**: the last `d` source letters of the
first component are literally the first `d` letters of the second.  Such a
splice has no source-position charge and produces exactly the concatenated
owner paths.  More general jointly rethreaded temporal scaffolds are not
claimed to admit this decomposition.

Under that literal port condition, three global rows become local and
compose exactly.

1. Every selected interval witness contained in one component survives at
   every width.
2. Residence is decided by the finite prefix/suffix **owner-run** history at
   each seam.
3. An address-disjoint compiler matching using component-internal cells and
   the pivot rays survives the quotient, and the displayed concatenated word
   is one common-cap witness.

This yields the protected Catalan--pivot connector theorem below.  Its
central existential hypothesis on this overlap subclass is a jointly selected immediate-upper-exact
rooted Catalan forest, literal component antecedents carrying a complete
upper-witness atlas, and a guarded Hamilton path in their overlap-port
digraph.  The stationary pull-clock theorem proves a fractional rank/trace
circulation only; it does not imply any of these three integral correlations.

The exact more general aperture law is

\[
                  \sum_K g_K+\sum_e(d-o_e)=1,          \tag{0.2}
\]

where `g_K` is the number of declared nonowner cells in component fragment
`K` and `o_e` is the literal source overlap at connector `e`.  The theorem
below is the clean `sum_K g_K=1`, `o_e=d` for every connector branch of
(0.2).  The alternative row-length branch has no component nonowner and
exactly one `(d-1)`-overlap connector.  That deficient overlap inserts one
depth cell between the two owner blocks and therefore breaks their claimed
consecutive free-port transition unless a separate owner-preserving bypass
is proved.  It is not a direct Hamilton-owner certificate and is not
covered by the full-overlap lemma below.

## 1. Rooted Catalan and pivot coordinates

Let `ML_m` be the incidence graph between ranks `m-1` and `m` of
`[2m-1]`.  Fix a perfect incidence matching `M_0`.  For an incidence
`e=LV` outside `M_0`, define

\[
 \operatorname {up}_{M_0}(e)=M_0(L)\cup V,
 \qquad
 \lambda_{M_0}(e):L\longrightarrow M_0^{-1}(V).       \tag{1.1}
\]

A rooted Catalan forest is a matching `Q_0` outside `M_0` such that

* `|Q_0|=U`;
* `up_(M_0)` is a bijection from `Q_0` to the rank-`m+1`
  colours; and
* the labelled links `lambda_(M_0)(Q_0)` form a forest.

Its links have indegree and outdegree at most one.  Hence they form exactly
`C` directed path components, counting isolates.

Let

\[
 V_0,V_1,\ldots,V_{3d}                                \tag{1.2}
\]

be the sharp pivot collar and `L_i=V_i cap V_(i+1)`.  Select the correlated
predecessor phase

\[
                  M_0(L_i)=V_i.                        \tag{1.3}
\]

Then the successor incidences contract to the directed protected path

\[
 L_0\longrightarrow L_1\longrightarrow\cdots
       \longrightarrow L_{3d-1}\longrightarrow
       M_0^{-1}(V_{3d}),                               \tag{1.4}
\]

and carry the distinct upper colours `V_i union V_(i+1)`.  Thus the pivot
is already common-independent in tail, head, immediate-upper and graphic
resources.  What remains is its correlated extension, not another local
pivot identity.

## 2. Literal component states

Let `K` be an oriented directed component of `Q_0`, with owner word

\[
                         T(K)=(T_0,\ldots,T_{n_K-1}).   \tag{2.1}
\]

A **literal depth-`d` state** for `K` consists of the following data.

1. A bit `epsilon(K) in {0,1}` and a nonzero source block
   \[
 A(K)=(A_0,\ldots,A_{n_K+d+\epsilon(K)-1}).            \tag{2.2}
   \]
   If `epsilon(K)=0`, its consecutive `(d+1)`-unions are exactly
   (2.1).  If `epsilon(K)=1`, they are (2.1) together with one declared
   controlled nonowner cell at the outer end of the block.  The state
   records whether that cell precedes or follows (2.1).
2. The ordered prefix and suffix rails
   \[
          p(K)=(A_0,\ldots,A_{d-1}),\qquad
          s(K)=(A_{n_K+\epsilon(K)},\ldots,
                 A_{n_K+d+\epsilon(K)-1}).             \tag{2.3}
   \]
3. The product owner-history state `rho_(d+1)(T(K))`: for every coordinate
   it records the first and last owner bits, leading and trailing positive-
   run lengths clipped at `d+1`, the all-one flag, and whether every
   internal owner run has length at least `d+1`.
4. A set `Omega(K)` of occurrence-labelled interval witnesses wholly
   contained in `A(K)`.
5. A set `Pi(K)` of occurrence-labelled compiler pins assigned to distinct
   interval cells wholly contained in `A(K)`.

The state is **internally accepted** when every non-boundary positive run in
the owner word `T(K)` has length at least `d+1`, every witness and pin has
its declared literal value, and the displayed source block obeys its
componentwise caps.

Two oriented states `K,K'` have a **literal overlap port** `K -> K'` when

\[
                              s(K)=p(K')                 \tag{2.4}
\]

letter by letter, the terminal and initial owners give the desired unused
free-port incidence, and the following guards hold.

* The composed owner-history states contain no forbidden short run.
* No two selected pin cells become the same physical interval after the
  overlap identification.
* Every declared boundary pin and every connector lower/q1 colour has its
  literal value.
* Any exported upper, voltage, charge or compiler coordinate has the
  declared increment.  In the zero-change face used below that increment is
  zero.

This definition deliberately includes physical addresses.  Equality of set
values or equality of unlabelled palettes does not make a literal port.

## 3. The literal overlap lemma

### Lemma 3.1 (exact `d`-overlap concatenation)

Let `A=A(K)` and `B=A(K')` satisfy (2.4), and identify their common
`d`-letter rail.  Write the resulting block as `A star_d B`.  Then:

1. its number of depth-`d` windows is
   `n_K+n_(K')+epsilon(K)+epsilon(K')`;
2. its depth row is the concatenation of the two declared depth rows; in
   particular its rank-`m` owner subsequence is `T(K)T(K')` whenever any
   controlled nonowner lies at an outer, rather than glued, end;
3. every interval occurrence contained in `A` or in `B` remains an interval
   occurrence with the same literal OR;
4. its only newly internal owner-coordinate runs are those crossing the
   boundary between `T(K)` and `T(K')`, and their legality is decided by
   the two owner-history states; and
5. every address-disjoint pin in `Pi(K) union Pi(K')` remains a distinct
   literal pin.

#### Proof

The length is

\[
 (n_K+d+\epsilon(K))+(n_{K'}+d+\epsilon(K'))-d
 =n_K+n_{K'}+d+\epsilon(K)+\epsilon(K'),
\]

so the displayed number of consecutive `(d+1)`-windows follows.  The first
declared depth row is that of `A`; the remaining row is that of `B`, because
the last `d` letters of `A` are literally its first `d` letters.  This
proves items 1--2.  The outer-end condition keeps the controlled nonowner
outside the owner concatenation.

The quotient map is order preserving on each block and only identifies
equal boundary letters.  Hence an old interval remains an interval and its
OR is unchanged, proving item 3.  An owner-coordinate run strictly inside
one component is unchanged.  A newly internal run crosses the component
boundary; its length is the trailing owner-run length of `T(K)` plus the
leading owner-run length of `T(K')`, with all-one fragments propagated
under iteration.  Endpoint bits, clipped lengths and the all-one flag
determine whether this creates `0 1^t 0` with `t<=d`.  This proves item 4.
Item 5 is exactly the physical-cell
injectivity guard in the port definition.  \(\square\)

For more than two blocks, pairwise port legality is not sufficient.  Put

\[
 b_1=0,\qquad b_{i+1}=b_i+n_{K_i}+\epsilon(K_i),       \tag{3.1a}
\]

and give source position `u` of block `K_i` the global address `b_i+u`.
When `n_(K_i)+epsilon(K_i)<d`, the source images of nonadjacent blocks may
overlap through the intervening block.  Thus the sentence “no nonadjacent
blocks are identified” would be false, already for an isolated component
with `n_K=1`.

Call an iterated overlap **globally consistent** when all letters assigned
to one global address are equal and cap-compatible, every named pin keeps
its required global interval address (with no unintended pin collision),
and the complete owner-history automaton accepts the resulting global owner
word.
Under this condition the iterated quotient is associative, every component
maps order-preservingly to the global line, and Lemma 3.1 applies
inductively.  Global consistency, rather than pairwise equality alone, is
the path-level composition guard used below.

## 4. Protected Catalan--pivot connector theorem

Let `mathcal K` be the `C` components of a rooted Catalan forest `Q_0`
containing the protected path (1.4).  Give every component a nonempty menu
of literal states from Section 2.  Let `D_lit(Q_0)` be the directed
state-expanded port graph: its vertices are literal states, partitioned by
their physical component, and its arcs are the literal overlap ports.

### Theorem 4.1 (literal protected Catalan connector)

Assume one can choose one state for every component and order the chosen
states

\[
                         K_1,K_2,\ldots,K_C             \tag{4.1}
\]

so that:

1. `K_i -> K_(i+1)` is a zero-increment literal overlap port for every
   `i<C`, and the complete iterated overlap is globally consistent in the
   sense following (3.1a);
2. the component containing the pivot collar is `K_1`, the collar is a
   prefix of `T(K_1)`, and its free first head is the global root;
3. the union of the occurrence atlases `Omega(K_i)` contains at least one
   witness for every required upper target at every width;
4. the union of the pin banks `Pi(K_i)`, together with the pivot singleton
   and two-ray pins, is address-disjoint and saturates the declared lower
   target bank; and
5. `sum_i epsilon(K_i)=1`; that unique controlled nonowner/boundary cell is
   at the outer end of `K_1` or `K_C`, and the exterior aperture ticket
   required by the `B+1` ledger is included in the corresponding boundary
   state.

Then the iterated overlap

\[
             A(K_1)\star_d A(K_2)\star_d\cdots
                    \star_d A(K_C)                     \tag{4.2}
\]

has the following properties.

* Its owner row is one Hamilton owner path containing the pivot collar.
* Every immediate-upper colour is present, already through `Q_0`.
* Every required upper target at every width is present through the atlas in
  item 3.
* Every internal positive run in the owner chronology has length at least
  `d+1`.
* Every declared lower pin, including the pivot two rays, occurs at a
  distinct physical cell in one literal source word.
* The connector adds no source positions beyond the component accounting.
  Since `sum_i n_(K_i)=W` and item 5 gives one controlled nonowner depth
  cell, the final source length is `W+d+1=B+1`, not `B+C`.

Thus, after the ordinary terminal maximal-cap check for the displayed pin
bank, (4.2) is a protected upper-complete resident `B+1` chronology on the
declared rows.

#### Proof

The rooted Catalan forest has exactly `C` components.  Each selected port
uses the unique free tail of its predecessor and unique free head of its
successor.  The path (4.1) therefore adds `C-1` links without reusing a
tail or head.  Its union with `Q_0` is a spanning directed link path.  Upon
expanding `M_0`, this is the asserted owner Hamilton path.  The protected
prefix criterion follows from its free first head and the forced path
(1.4).

Apply Lemma 3.1 successively in the globally consistent quotient.  It proves the exact owner count, zero
connector charge, preservation of every internal witness and pin, and
residence at every newly internal seam.  Since `Q_0` contains one occurrence
of every immediate-upper colour, no connector deletion can remove that
palette.  Items 3--4 then give the full upper atlas and lower matching.
The concatenated literal word witnesses all displayed caps and pins
simultaneously; the terminal maximal-cap criterion is precisely the stated
remaining check.  Item 5 supplies the already-audited one-credit boundary
ledger.  \(\square\)

### Corollary 4.2 (DAG/Hall form)

Fix one state per component and let `D` be an acyclic subgraph of their
literal overlap-port graph.  If the pivot component is `K_*` and

\[
 |N_D^-(Y)|\ge |Y|
 \qquad
 (Y\subseteq\mathcal K\setminus\{K_*\}),              \tag{4.3}
\]

then `D` contains a directed Hamilton path starting at `K_*`.  If its
states also satisfy items 3--5 of Theorem 4.1 **and the selected path's
complete iterated overlap is globally consistent in the sense following
(3.1a)**, all conclusions follow.

#### Proof

Hall selects distinct incoming arcs for all nonroot components.  Acyclicity
excludes a directed cycle.  There are `C-1` arcs, every nonroot has
indegree one, and no tail is used twice, so the result is one directed
Hamilton path.  Apply Theorem 4.1.  \(\square\)

The tail-injectivity in the last sentence is part of the bipartite port
matching: left vertices are the outgoing component copies.  Omitting that
shore would make (4.3) insufficient.

The added global-consistency clause is load-bearing.  Hall and acyclicity
prove only the owner-layer Hamilton path.  They do not prevent nonadjacent
short component blocks from identifying one source address, nor do they
check the resulting cap, pin, or owner-history state.  Equivalently, one may
replace `D` by a state-expanded path automaton whose accepted paths certify
that clause; pairwise legal overlap arcs alone do not certify it.

## 5. Equivalent direct owner-layer form and the switch alternative

Ignoring source literalization for one paragraph, Theorem 4.1 has the exact
owner-layer compression

\[
 \boxed{
 M_0\text{ perfect},\quad Q\text{ a matching of size }W-1,quad
 \operatorname {up}_{M_0}(Q)=\binom{[2m-1]}{m+1},\quad
 \lambda_{M_0}(Q)\text{ a tree},\quad P_1\subseteq Q.} \tag{5.1}
\]

The tree in (5.1) is a path because its indegree and outdegree are at most
one.  Selecting one occurrence of every upper colour inside `Q` recovers
`Q_0`; the remaining `C-1` links are precisely the connector path.  Thus
the forest-plus-connector decomposition is lossless at the owner layer.

There is a second sufficient topology route.  Complete a compatible
partition two-factor and choose a protected-compatible family of binary
pulls and ternary Boolean hexes whose component footprints form a spanning
incidence tree.  If their complete exported state includes the literal
source-rail/antecedent state, clipped owner-history, upper-witness and
compiler ledgers and has total increment zero,
the protected safe-switch composition theorem merges the factor to one
cycle while preserving those rows.  A final opening still needs a witness-
transparent cut.  Residual Ore/LKK expansion proves only the marginal
factor; it supplies neither the safe-switch incidence tree nor the
transparent opening.

Even under those hypotheses, a literal `B+1` conclusion additionally needs
the one-credit source-length/aperture equation and a compiler-typed final
opening.  The switch-tree theorem alone is only a topology/state transport
theorem.

The direct overlap-port path of Theorem 4.1 avoids that last cut and is
therefore the cleaner `B+1` interface.

## 6. Exact obstructions to deleting hypotheses

### 6.1 Abstract incidence is not a source port

An incidence edge between the terminal and initial owners verifies one
Johnson transition only.  Concatenating two length-`n_i+d` source blocks
without a `d`-letter overlap creates `d` additional depth windows.  Hence
an owner-layer connector does not prove the charge, owner multiplicity or
source factorability rows of Theorem 4.1.

### 6.2 Immediate upper is not the upper tower

The bijection `up(Q_0)` covers rank `m+1` only.  One cut of a cyclic owner
chronology can hit a linearly nested family of higher upper witnesses.
Therefore upper-exactness of `Q_0` does not imply item 3.  The internal
occurrence atlas, or an equivalent exact final replay, is necessary.

### 6.3 Local pivot transparency is chronology-relative

Monotone insertion transports every old interval in one fixed source order.
If the ambient Catalan construction later reorders owner fragments, that
transport theorem no longer identifies the old witnesses.  The pivot must
be planted prospectively inside the literal component state, or the final
upper atlas must be rebuilt after the reordering.

### 6.4 Internal residence is not boundary residence

The active pivot runs have length exactly `d+1`, but its far-left and
far-right flags are clipped.  Their validity after embedding is exactly an
endpoint-history condition.  Owner/q1 protection alone does not extend
those runs.

### 6.5 Fractional pull-clock is not integral forest/path selection

The corrected pull-clock theorem gives a stationary fractional marked-trace
circulation with the exact rank marginals.  It may repeat owners, repeat
named targets and have arbitrarily many components.  It therefore proves
none of the one-state-per-component, upper-atlas, Hamilton-port or literal
overlap conditions in Theorem 4.1.  The sharp protected-contraction
six-cycle example likewise shows that uniform common-base marginals do not
force extension through a prescribed collar.

## 7. The exact remaining lemmas

The local pivot theorem is no longer missing.  A complete all-`m`
construction needs the following genuinely separate statements.

### `PCF(m,d)` -- protected chronology-coherent Catalan forest

Choose correlated `M_0,Q_0` containing the pivot path so that every
component of `Q_0` has a literal depth-`d` state and the union of its
internal atlases covers the full required upper tower.  The state menus must
include the pivot prefix orientation and its exterior aperture ticket.

This strengthens the known immediate-upper rooted-Catalan problem by source
factorability, residence histories and all-width occurrences.  Neither the
four separate matroid ranks nor the fractional pull-clock proves it.

### `GOP(m,d)` -- guarded overlap-port path

For one solution of `PCF(m,d)`, select one literal state per component and a
directed Hamilton path through the `C` components using zero-charge
`d`-overlap ports, starting at the pivot component and satisfying all seam
source-rail, owner-history and address-injectivity guards.  Equivalently,
expose an acyclic
subreservoir satisfying (4.3).

This is the Catalan-scale connector theorem.  Ordinary connectivity is
insufficient, and a state-forgetting port graph can pass Hall while every
one-state-per-component lift fails.

### `CAP(m,d)` -- terminal compiler/cap and one-credit discharge

The component-internal pin banks and pivot rays must extend to the complete
lower target matching in one maximal common cap.  The unique aperture colour
must be the global boundary colour or have a separate exterior occurrence,
and the final source must contain exactly one active pivot star/nonowner
credit.

The local two-ray release/transport matching proves the pivot contribution
to this lemma with zero old damage.  It does not prove the ambient target
matching after a new Catalan chronology is selected.

Under `PCF+GOP+CAP`, Theorem 4.1 and the one-credit pivot ledger give the
desired protected `B+1` construction.  For a theorem concerned only with
the central owner/residence/upper chronology **within the literal-overlap
architecture**, `PCF+GOP` is the exact missing combined lemma and `CAP`
remains downstream.  The weaker prospective architecture is the prepared
Hamilton scaffold `PCPS(m,d)`: there the forest and connector are extracted
after the final chronology is built, and no componentwise `d`-overlap
factorization is required.

## 8. Dependency and scope audit

This note uses only the following proved inputs.

* `MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`
  for the literal pivot collar, all-width monotone transport, ray ledger and
  clipped-run scope.
* `MATH_THEOREM_A_MONOTONE_PIVOT_INSERTION_ZERO_DAMAGE_COMMONQ_20260801.md`
  for exact band transport and the local common-cap statement.
* `MATH_THEOREM_TIGHT_PIVOT_PHASE_PATH_AND_SUPPORT_FIRST_CATALAN_CONNECTOR_20260801.md`
  for the correlated predecessor phase and upper-exact forest/path
  decomposition.
* `MATH_THEOREM_THREAD_D_PIVOT_RICH_BPLUS1_PROTECTED_CATALAN_PATH_GATE_20260801.md`
  for the exact `U+(C-1)=W-1` owner-layer ledger and prefix criterion.
* `MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_CONNECTOR_BIRTH_AND_PREPARED_SCAFFOLD_GATE_20260802.md`
  for the weaker prospective alternative in which a final Hamilton
  scaffold is constructed first and the forest/connector are born inside
  it.
* `MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_HISTORY_APERTURE_AND_RESIDENCE_GATE_20260802.md`
  for the exact general overlap/one-credit law (0.2), its finite history
  state and the component-internal witness criterion.
* `MATH_THEOREM_K_PROTECTED_SAFE_SWITCH_TREE_AND_HYPERTREE_COMPOSITION_20260802.md`
  for the optional factor-and-switch fusion route.
* `MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md` only for its
  stated fractional circulation.  No integral consequence is imported.

The theorem does not assert the existence of `PCF`, `GOP` or `CAP`, does
not improve the current finite `k=17` upper bound, and does not infer
`nu(k)=B(k)+1` or `nu(k)=B(k)`.  Its new unconditional content is the
literal `d`-overlap composition theorem and the proof-safe identification
of the source/history/upper-atlas rows missing from the older abstract
Catalan connector.  It is stronger than, and must not be substituted for,
the prospective prepared-scaffold gate when no literal overlap
factorization is available.
