# Leaf-peelable transparent gluing: the exact collar state and the first obstruction

Date: 2026-07-31  
Status: exact state-composition theorem; exact grouped-graphic formulation;
positive standard-plane-tree calibration through `m=4`; smallest frozen
transition obstruction to the one-bit leaf-peelable state.  No all-`m`
existence theorem is claimed.

## 0. Verdict

For a fixed alternating decoration, leaf peelability has a clean local
gluing rule.  Cut the old matching edges at all active hexagons, delete the
gap vertices which cross those cuts, and contract every component of the
remaining gap forest.  Each new bridge gap is then a star from a new gap
vertex to the contracted lower-colour components which occur in that gap.
The post-glue gap graph is a forest if and only if this attachment multigraph
is a forest.  Since transparency already carries a perfect matching, the
forest certificate also gives uniqueness of that matching and recovery of
its edges by successive leaf peeling (the peeling order itself need not be
unique).

Thus a finite proof-sufficient collar state, with the interior reduced to
exactly the information used by the transition test, is

\[
 \boxed{(
   \text{exact palette ownership (internal banks and port owners)},
   \text{fragment endpoint mark types},
   \text{residual matching},
   \text{boundary-colour connectivity partition},
   \text{per-fragment protected trace bits}) .}
 \tag{0.1}
\]

The one-bit state "the old gap graph is a forest" is not closed under all
transparent toggles.  The first loss already occurs at the frozen `m=3`
fixture.  The transparent toggle

\[
                 H=1,\qquad (a,b,c)=(1,3,4)           \tag{0.2}
\]

carries a decoration whose Hamilton-cycle gap graph is a forest with one
perfect matching to a two-component factor containing the four-cycle

\[
 g_{12\to17}-4-g_{17\to12}-16-g_{12\to17}.           \tag{0.3}
\]

The two directed gaps have the same selected-`A` endpoint pair but are
distinct occurrence vertices; each sees colours `4` and `16`.  The new graph
has two perfect matchings.  This is the smallest general transparent-toggle
obstruction in the frozen `m=2,3,4` fixtures and the smallest possible
bipartite cycle.  Its inverse is a component-merging repair, not a failure of
the recursive merge direction.

The first Hamilton-to-Hamilton loss in those fixtures occurs at `m=4`, at

\[
                 H=66,\qquad (a,b,c)=(0,3,4),         \tag{0.4}
\]

where the new gap `g_(67,100)` attaches to colours `65` and `68` already
connected through the retained gap `g_(67,76)`, producing

\[
 g_{67,100}-68-g_{67,76}-65-g_{67,100}.              \tag{0.5}
\]

Unlike the `m=3` local double-gap obstruction, this decision depends on
connectivity through the retained core.  It is the finite witness that the
boundary-colour connectivity partition, or equivalent information, cannot
be discarded.

The standard plane-tree factors nevertheless have a nonempty exact state
family in every tested dimension `m=2,3,4`.  At `m=4` the unique standard
plane-tree glue has an explicit common leaf-peelable decoration and a
protected `0^4` socket.  This is a finite base calculation, not an induction:
all-`m` nonemptiness of the exact state remains the missing theorem.

## 1. The componentwise gap graph

Let `F` be a middle-levels two-factor on the two shores

\[
       \binom{[2m-1]}{m-1},\qquad \binom{[2m-1]}m,
\]

and let `D=(D_A,D_B)` be selected occurrences such that

1. the selected turn colours are globally bijective on both shores; and
2. selected shore types alternate on every component of `F`; and
3. every component contains a selected occurrence of each shore type.

The third condition is the marked-component state used here.  An entirely
unmarked factor cycle would leave a cyclic residual matching choice rather
than the forced path matching, and must be represented by an additional
state; none of the finite certificates below uses that extension.

On each factor component, consecutive selected `A`-vertices define cyclic
gaps of `B`-positions.  The componentwise gap graph `Gamma(F,D_A)` has one
vertex for every such gap, one vertex for every lower turn colour, and an
edge whenever that colour occurs in the gap.

Alternation puts exactly one selected `B`-vertex in every gap.  Global lower
palette bijectivity therefore supplies a distinguished perfect matching

\[
                         \mu_D\subseteq E(\Gamma).     \tag{1.1}
\]

### Lemma 1.1 (the forest certificate)

If `Gamma(F,D_A)` is a forest, then `mu_D` is its unique perfect matching,
and repeatedly deleting a degree-one vertex together with its matched
neighbour deletes the whole graph.

#### Proof

The symmetric difference of two perfect matchings is a disjoint union of
even cycles, so a forest has at most one perfect matching.  Conversely, a
nonempty forest has a leaf.  Its only incident edge belongs to every perfect
matching.  Delete that matched pair and induct.  This proves the claim.
\(\square\)

The word **leaf-peelable** below refers to the strong audited condition that
the gap graph is a forest (and hence has the conclusions of Lemma 1.1), not
merely to existence or uniqueness of a perfect matching.  No converse to
Lemma 1.1 is needed or claimed.

## 2. The exact finite collar state

Fix a compatible collection of pairwise edge-disjoint incidence hexagons,
and cut the three old factor edges at every currently active hexagon.  The
affected factor components become retained paths; untouched components remain
closed accepted blocks.  Relative to these cuts, store the following data.

For a single transition, edge-disjointness is enough.  For a multi-toggle DP,
use the stronger **prepared common-core** hypothesis: all prospective old
bridge gaps are cut at the outset, their deletions are choice-independent,
and no toggle changes an internal occurrence-gap or attachment atom belonging
to another toggle.  All connectivity states below are then taken relative to
that one common core.  Ordinary edge-disjointness of the physical hexagons
alone does not imply this stronger gap compatibility.

### 2.1 Palette ownership

At component level, store the exact two owned-colour banks and the occurrence
which owns each colour, split into an internal frozen bank and port
occurrences.  At every hexagon port `v`, store its shore, its
selected/unselected bit, and, when selected, its exact current owner colour
`tau_F(v)`.  Composition requires disjoint union of child banks, and the root
bank must be the full palette on each shore.  Only the port owners can change
under a collar toggle.

For checking one toggle against an already global decoration, the state
quotients to the two selected local multisets together with the marked port
identities.  The identities are needed if later collars overlap; for a
pairwise disjoint gluing tree the two multisets suffice after the global
banks have been checked once.

### 2.2 Trace boundary

For each retained path store

\[
              (\epsilon^-,\epsilon^+)\in
              \{A,B,\bot\}^2,                       \tag{2.1}
\]

the shore types of its first and last selected vertices, with `\bot` for an
empty selected trace.  These are exactly the bits used by the transparent-
hexagon theorem.  In a reconnection, empty fragments are suppressed before
consecutive nonempty endpoint types are compared.

### 2.3 Residual gap matching

Delete from `Gamma` every **bridge-gap vertex**, meaning a gap whose cyclic
interval crosses a cut.  Retain the forced matching on all internal gaps.
Store the exact set `R` of lower colours left unmatched.  For a proposed
reconnection `rho`, store for every new bridge gap `g`

* its exact lower-colour neighbourhood `N_rho(g)`; and
* the colour `nu_rho(g)` owned by its unique selected `B`-vertex.

The matching test is simply

\[
    \nu_\rho(g)\in N_\rho(g),\qquad
    \nu_\rho:\{\text{new bridge gaps}\}\longrightarrow R
    \text{ is a bijection}.                          \tag{2.2}
\]

For one already global fixed decoration, transparent preservation of the
lower palette and mark alternation implies (2.2), so it may be omitted as a
redundant check.  It is needed in a bottom-up component DP, where child states
carry only partial palette banks and partial matchings.

### 2.4 Boundary connectivity

Let `Gamma^circ` be the graph after the old bridge-gap vertices are deleted.
It is a forest whenever the input state is leaf-peelable.  For one
reconnection let

\[
 C_\partial=\bigcup_g N_\rho(g).
\]

Store only the partition `pi` of `C_partial` induced by connected components
of `Gamma^circ`.  A colour not otherwise incident with the core is a
singleton block.  Interior components disjoint from `C_partial` need only
one accept bit; their literal shape is irrelevant to every collar
transition.

For a prepared family, replace `C_partial` by the fixed future interface

\[
 C_\ast=\bigcup_{\rho\text{ allowed later}}\ \bigcup_g N_\rho(g),
 \tag{2.3}
\]

and store `pi` on all of `C_*` from the start.  Storing it only on the current
collar is not sufficient for associative future composition.  If no future
collar family is declared, the full lower-colour set is a finite, though
larger, safe interface.

### 2.5 Protected forest-face bits

For every retained fragment store a bit `beta_P`.  It is one when that
fragment contains a trace breaker protected from all future collars: for
example, four consecutive unmarked physical positions, or a bracketed even
marked run.  For a proposed reconnection, every output cycle must contain at
least one fragment with `beta_P=1`.  Equivalently, OR the fragment bits
separately on each prospective output component and require every resulting
component bit to be one.

For a component merge, the literal-breaker condition is automatic if at
least one input component carries `beta=1`: the merged component inherits
that protected fragment.  Thus a rooted schedule which always merges the
next component into one witness-containing active component propagates a
single literal witness.  Acceptance only by an exact boundary automaton is
not automatically inherited and must be recomputed.  For a split, one global
bit is not enough: the new component not containing its witness needs a
separate breaker.  If no literal breaker is reserved, replace the fragment
bits by the exact capped zero-run and one-run-parity boundary automaton on
every prospective output component.  One unqualified global Boolean is not
exact.

For fixed `m` and a fixed finite collar set this state is finite.  It is not
a constant anonymous state: the exact colour labels and their connectivity
partition are essential.  The obstruction in Section 5 proves that the
one bit "currently acyclic" is insufficient, and the `m=4` obstruction
specifically detects connectivity through the retained core.

## 3. Exact composition

From `pi` and the new gap neighbourhoods form the **attachment multigraph**
`A_rho`.  Its left vertices are the new bridge gaps.  Its right vertices are
the blocks of `pi`.  For every `c in N_rho(g)`, put one edge from `g` to the
block `[c]_pi`.  Multiplicity is retained: two colours of one new gap lying
in the same core component give parallel attachment edges.

### Theorem 3.1 (collar-state composition)

Assume the internal state is accepted.  A reconnection `rho` produces
another leaf-peelable decorated state with the protected forest flag if and
only if all of the following hold.

1. The selected local turn-colour multisets agree before and after,
   separately on the two shores.
2. After empty fragments are suppressed, the endpoint types (2.1) are
   opposite across every new seam between consecutive nonempty fragments.
3. The residual assignment (2.2) is a bijective matching.
4. The attachment multigraph `A_rho` is a forest.
5. On every output component, at least one protected fragment witness remains
   outside the changed collars (or that component's exact trace automaton
   accepts).

The output connectivity partition is obtained by taking connected
components of `A_rho` and merging the corresponding blocks of `pi`.  Under
the prepared common-core hypothesis of Section 2, with `pi` stored on
`C_*`, these transitions compose associatively.  No associativity claim is
made from physical edge-disjointness alone.

#### Proof

Conditions 1 and 2 are exactly the transparent-polygon criterion, hence
preserve the two palette bijections and componentwise alternation.  Condition
3 extends the internal matching to a perfect matching of the new gap graph.

The graph `Gamma^circ` is a forest.  Contract each of its tree components.
Every new edge is then precisely an edge of `A_rho`.  A cycle in the new gap
graph which uses an attachment contracts to a cycle of `A_rho`; conversely a
cycle of `A_rho` expands through the unique core-tree paths to a cycle in the
new gap graph.  Core components themselves contain no cycle.  Thus the new
gap graph is a forest exactly under condition 4.  Lemma 1.1 now gives the
unique matching and its recovery by successive leaf peeling.  Condition 5
keeps every output component's binary trace off its unique cycle face.

For a prepared family, the attachment atoms and predeleted core are fixed and
only union of blocks of `C_*` is used.  Performing two compatible
reconnections in either order therefore gives the same partition and
matching state.  This proves the scoped associativity assertion. \(\square\)

### Corollary 3.2 (private-socket closure)

Suppose each toggle is allocated a disjoint set of private singleton colour
blocks such that its attachment bundle together with those blocks is a tree
which meets the nonprivate retained core and all earlier bundles in at most
one contracted vertex.  Then the gap-forest condition is automatic.  In
particular, a bundle which can be successively leaf-peeled through private
colours before reaching at most one old nonprivate core component cannot
create a gap cycle.

This is the useful leaf-peelable sufficient face.  It is stronger than
transparency, but it avoids carrying a global Hall family.

### Corollary 3.3 (distinct-component insertion)

Order the new bridge-gap vertices arbitrarily.  The attachment multigraph is
a forest if and only if, when each gap vertex is inserted, its incident
colours lie in pairwise distinct current connectivity blocks.  The insertion
then merges exactly those blocks.

#### Proof

A star added to a forest creates a cycle exactly when two of its leaves were
already connected.  Induct over the gap vertices. \(\square\)

Thus if every factor-component merge is aligned with a merge of distinct gap
components, the factor gluing tree is simultaneously a gap-attachment tree
and leaf-peelability preservation is automatic.

## 4. The exact grouped-graphic boundary

Let `T` be a prepared family of compatible transparent toggles.  The
preparation deletes their private old sockets, so the contracted gap core is
fixed, and the atomic edge bundles `B_t` are pairwise disjoint as edge sets
(they may share contracted core endpoints).  Assume, as in the standard
plane-tree gluing tree, that each toggle
joins two factor components; a genuine three-component hex would instead
give a hypergraphic component constraint.  There are two graphic objects.

* `M_comp` is the graphic matroid of the auxiliary factor-component graph;
  a Hamiltonizing gluing set must be a basis of it.
* The atomic attachment edges lie in the graphic matroid `M_gap` of the
  contracted gap-attachment multigraph.  A toggle `t` contributes a whole
  bundle `B_t` of atomic edges.

The exact gap-independent toggle families are

\[
 \mathcal I_{\rm gap}
  =\{S\subseteq T:\bigcup_{t\in S}B_t
                   \text{ is independent in }M_{\rm gap}\}.             \tag{4.1}
\]

Hence the gluing-tree question is a common-independence problem between
`M_comp` and the **grouped pullback** (4.1), together with the palette,
matching, and protected-trace tests.

The preparation hypothesis is substantive.  Without private predeletions,
toggle `t` has both an old socket bundle `B_t^0` and a new attachment bundle
`B_t^1`, and the exact test is

\[
 E^\circ\cup
 \bigcup_{t\notin S}B_t^0\cup
 \bigcup_{t\in S}B_t^1
 \quad\text{is graphic-independent}.                \tag{4.1a}
\]

This is a grouped two-choice basis-exchange system.  It does not reduce to
(4.1), much less to matroid intersection, unless the old sockets can be
deleted or contracted independently of `S`.

After palette, residual-matching, boundary, and trace admissibility have been
frozen into `T`, a canonical sufficient face on which the remaining problem
is ordinary intersection of two graphic matroids is:

* after suppressing private series paths and leaf trees, each toggle has one
  effective nonloop attachment edge.

Then `t -> B_t` identifies (4.1) with a graphic matroid on toggle labels.
Absent extra special structure, this one-effective-edge reduction is the
only generally justified ordinary two-graphic formulation.  If every toggle
has a disjoint pair of genuine effective edges, the gap side is an instance
of graphic matroid parity, not automatically an ordinary second matroid; the
factor-component graphic constraint remains additional unless it is
automatic or aligned with the pairs.  Arbitrary stars or larger bundles can
give grouped graphic independence which is not a matroid; no generic matroid
claim is valid.

The distinction is real.  In a multigraph take three disjoint two-edge
groups

\[
 A=\{uv,xy\},\quad
 B=\{uv',pq\},\quad
 C=\{xy',rs\},                                      \tag{4.2}
\]

where `uv'` is parallel to `uv`, `xy'` is parallel to `xy`, and all other
endpoints are fresh.  The group sets `{A}` and `{B,C}` are independent, but
neither `{A,B}` nor `{A,C}` is independent.  The exchange axiom therefore
fails on these group labels.  Thus even pair-bundle feasible sets need not be
a matroid; the general formulation is parity, while special pair systems may
still collapse to an ordinary matroid.

There are two simplifying faces.

1. **Private socket.**  Corollary 3.2 makes `I_gap=2^T`; only the
   factor-component tree remains.
2. **Aligned one-edge image.**  If factor components inject into contracted
   gap components and every factor edge maps to the corresponding single gap
   edge, every factor forest maps to a gap forest.  The two graphic
   constraints then coincide.

Without one of these faces, “choose the published gluing tree” is not a
proof of gap-forest preservation.

## 5. The first exact transition obstructions

### 5.1 Smallest general transition: an `m=3` split

Use the frozen `m=3` Hamilton cycle

```text
3 7 5 13 9 11 10 26 24 25 17 21 20 28 12 14 6 22 18 19
```

and select

\[
 D_A=\{3,9,12,17,24\},\qquad
 D_B=\{11,13,19,25,28\}.                             \tag{5.1}
\]

Toggle (0.2), replacing

\[
 \{(3,19),(9,11),(17,25)\}
 \quad\text{by}\quad
 \{(3,11),(9,25),(17,19)\}.                          \tag{5.2}
\]

All six ports are marked.  The selected local upper palette is
`{15,23,29}` and the selected local lower palette is `{2,8,16}` on both
sides, and the fragment boundary types pass the transparent-hexagon test.
The output factor cycles are

```text
3 7 5 13 9 25 24 26 10 11
6 14 12 28 20 21 17 19 18 22
```

The old gap profiles are

\[
                    2(1,1,1)+(3,3,5),                \tag{5.3}
\]

with one perfect matching.  In the second output component, the two
selected `A`-vertices are `12` and `17`.  Its two directed cyclic gaps are
different occurrence vertices and have neighbourhoods

\[
 N(g_{12\to17})=\{4,16\},\qquad
 N(g_{17\to12})=\{2,4,16\}.                          \tag{5.4}
\]

They therefore contain the four-cycle (0.3).  The new profiles are

\[
                       (1,1,1)+(4,4,8),               \tag{5.5}
\]

and there are two perfect matchings.  Both sides are valid decorations and
both physical lifts are linear forests.  On the split side the second
component has the protected unmarked run `18,22,6,14`, while the first passes
the exact trace test through the bracketed even marked run `13,9,25,24`.
Only leaf peelability is lost.  This topology statement is a direct
per-output-component check; it does not rely on one global protected bit.

This example also explains why gap vertices must be occurrence-labelled.
Naming a gap only by its unordered endpoint pair would identify
`g_(12->17)` with `g_(17->12)` and incorrectly erase the cycle.

At each of the five frozen `m=3` split toggles there are twelve common
decorations.  Exactly eight are leaf-peelable on both sides; the remaining
four are leaf-peelable only on the Hamilton side.  Hence every inverse
component-merging glue still has a nonempty accepted state family.  The
obstruction is to automatic bidirectional closure of the one-bit state, not
to existence of a safe `m=3` merge.

### 5.2 Smallest Hamilton-preserving transition: `m=4`

Use the frozen decorable `ML(7)` cycle and the common decoration recorded in
`scratch/decorable_ml7_gluing_20260731.audit.json` under
`acyclicity_counterexample`.  Toggle the hexagon (0.4).  All six hexagon
vertices are marked, the two local palette multisets agree, and the boundary
mark types alternate.  Thus this is a transparent transition for the fixed
decoration.

Before the toggle the gap graph is a forest and has one perfect matching.
After the toggle the changed gap edges include

\[
\begin{array}{c|c}
 \text{new gap}&\text{new incident colours}\\ \hline
 g_{67,100}&65,68,80,\\
 g_{73,74}&72.
\end{array}                                          \tag{5.6}
\]

The retained gap `g_(67,76)` is incident with both `65` and `68`.  In the
cut core, therefore, `65` and `68` lie in the same block of `pi`.  The two
edges from `g_(67,100)` to that block are parallel in `A_rho`, yielding
exactly the cycle (0.5).  The new component profile contains

\[
                         (7,7,14),                    \tag{5.7}
\]

and the new graph has two perfect matchings.  It is decorable and its
physical lift is still a linear forest; only the stronger leaf-peelable
state is lost.

This is an oriented fixed-decoration loss.  The inverse toggle repairs that
same decoration.  For this `H=66` toggle, 72 of its 144 common decorations
are leaf-peelable on both sides.  It is therefore not a “bad toggle” and not
an existence obstruction.  More broadly, the authoritative census gives
leaf-peelable common decorations for every one of its six transparent
Hamilton toggles; what fails is automatic preservation for an arbitrary
common decoration.

## 6. Positive standard-plane-tree calibration

Use the Merino--Mička--Mütze parameter `n=m-1`, so the physical ground-set
size is `2n+1=2m-1`.

### 6.1 `m=2`

There is one plane-tree component and no glue.  The frozen six-cycle with
`I=J={0}` has one gap-colour edge, its matching is unique, and its trace has
a protected zero-run of length four.

### 6.2 `m=3`

There is again one plane-tree component and no glue.  The standard factor
cycle

```text
3 11 10 14 12 13 9 25 17 21 5 7 6 22 20 28 24 26 18 19
```

has the leaf-peelable decoration

\[
 D_A=\{3,5,9,10,20\},\qquad
 D_B=\{7,11,14,25,28\}.                              \tag{6.1}
\]

Its gap-forest profiles are

\[
                3(1,1,1)+(2,2,3),                   \tag{6.2}
\]

and its trace contains a protected `0^4`.  The separate frozen `m=3`
fixture has the connected profile `(5,5,9)` and gives the same positive
state conclusion.

### 6.3 `m=4`: the first nontrivial standard glue

The standard base factor has two components of lengths `28` and `42`.  Its
unique potential-decreasing plane-tree label is

\[
                        x=110010,\qquad y=101010.      \tag{6.3}
\]

The physical incidence hexagon replaces

\[
 \{(19,27),(21,23),(25,29)\}
 \quad\text{by}\quad
 \{(19,23),(21,29),(25,27)\}.                        \tag{6.4}
\]

On both the two-component factor and the joined Hamilton cycle, take

\[
\begin{split}
D_A={}&\{7,11,13,19,21,25,26,35,37,38,41,42,50,56,73,76,81,82,84,100,104\},\\
D_B={}&\{23,27,29,39,43,46,51,53,54,58,77,78,89,90,99,101,102,105,108,114,116\}.
\end{split}                                          \tag{6.5}
\]

All six ports are marked.  The selected local upper palette is

\[
                         \{87,91,93\},                \tag{6.6}
\]

and the selected local lower palette is

\[
                         \{18,20,24\}                 \tag{6.7}
\]

on both sides of the toggle.  After deleting the old matching, the three
retained fragments have endpoint mark types

\[
                         A\!-!A,\quad B\!-!B,\quad A\!-!B,             \tag{6.8}
\]

and the new seams join opposite types.

The only changed gap sockets relevant to leaf peeling are

\[
\begin{array}{c|c|c}
 &\text{gap}&\text{colour neighbourhood}\\ \hline
\text{old}&g_{19,26}&\{18\}\\
\text{old}&g_{21,84}&\{20\}\\
\text{new}&g_{19,84}&\{18,20\}\\
\text{new}&g_{21,26}&\{20,24\}.
\end{array}                                          \tag{6.9}
\]

The retained socket `g_(25,26)` has neighbourhood `{24}`.  The old selected
matching uses `18,20,24` at `B`-ports `27,23,29`; the new matching uses the
same colours at ports `23,29,27`.  On the new side, leaf peeling forces

\[
          18-g_{19,84},\qquad
          20-g_{21,26},\qquad
          24-g_{25,26}                               \tag{6.10}
\]

in that order.  After the two old singleton gap vertices are deleted and the
retained core is contracted, the entire new attachment multigraph is the path

\[
 [18]-g_{19,84}-[20]-g_{21,26}-[24].                 \tag{6.10a}
\]

Thus the unique standard glue lies on the private-socket face of Corollary
3.2.  The base gap forest has profiles

\[
                 15(1,1,1)+3(2,2,3),                \tag{6.11}
\]

and the joined gap forest has profiles

\[
          12(1,1,1)+3(2,2,3)+(3,3,5).               \tag{6.12}
\]

Finally, the length-28 base component contains the protected unmarked run

\[
                         98,106,74,75                 \tag{6.13}
\]

and the length-42 base component contains the protected bracketed even marked
run

\[
                         7,39,38,54.                  \tag{6.14}
\]

Both are disjoint from the six ports.  After the component-merging glue, the
run (6.13) remains a protected `0^4` in the joined Hamilton cycle.  Hence
(6.5) is a complete accepted collar state for the first nontrivial standard
plane-tree join, including the per-component input topology guard.

## 7. Exact missing theorem and scope

The exact recursive target exposed by this note is:

> **Leaf-peelable transparent gluing-tree theorem.**  For every `m`, the
> standard middle-levels plane-tree factor admits one global pair of
> alternating turn transversals which marks every factor component, one
> literal protected trace breaker on every initial component, and a Hamiltonizing
> compatible gluing tree prepared on one common gap core, such that every
> palette/boundary transition is transparent and the union of its contracted
> gap-attachment bundles is graphic-independent.  Equivalently under this
> prepared merge-only schedule, every intermediate gap graph is
> leaf-peelable and every intermediate physical component retains an accepted
> trace state.

There is a particularly sharp sufficient strengthening suggested by the
standard `m=4` path (6.10a).

> **All-six-marked private-triple conjecture.**  The decoration and a rooted
> standard plane-tree gluing tree can be chosen jointly so that every used
> hexagon has all six ports marked and its three selected lower owner colours
> can be ordered `c_1,c_2,c_3` with post-cut attachment
> \[
>        [c_1]-g_1-[c_2]-g_2-[c_3].
> \]
> The first two colour blocks are private to that glue, the path meets the
> previously retained nonprivate gap core in at most the terminal block
> `[c_3]`, different glue paths have disjoint private blocks, and the exact
> upper-owner palettes and boundary types are transparent.  A rooted
> witness-containing component also carries the protected trace breaker
> through every merge.

If true, Corollary 3.2 makes the gap-graphic constraint automatic: leaf peel
`c_1`, then `c_2`, then attach at `c_3`, exactly as in (6.10).  The `m=4`
certificate proves the first nontrivial instance.  No simultaneous `m=5`
private-triple assignment has been audited here, so this is an explicitly
open strengthening, not part of the frozen theorem.

On the aligned one-effective-edge face, this becomes ordinary two-matroid
intersection seeking a basis of `M_comp` which is independent in `M_gap`;
the ranks need not agree, so “common basis” is not the right generic phrase.
On the private-socket face the gap constraint is free and one seeks only the
factor-component basis.  In general it is the grouped problem (4.1), with
parity already appearing for two-edge bundles.

Theorem 3.1 proves that this statement would be sufficient.  Section 6
proves its first three finite cases.  Neither proves that an accepting state
exists for every `m`, nor that the published deterministic gluing tree is
transparent for some decoration.  The frozen obstructions prove that one
cannot establish it by carrying only two turn rainbows, a fixed arbitrary
SDR, or a one-bit leaf-peelability flag.

This remains a theorem about the middle-levels-resolvable sufficient
subclass.  It does not assert that an arbitrary Catalan linear matching has a
middle-levels resolution, and it does not use the retracted Greene--Kleitman
`W/2` bound.

## 8. Audit

Run

```text
python3 scratch/audit_catalan_leaf_peelable_transparent_gluing_state_20260731.py
```

The audit does not repeat the frozen `m=4` hexagon census.  It reconstructs
only the deterministic standard factors for `m=2,3,4`, replays the one
standard `m=4` plane-tree glue and certificate (6.5), checks the exact collar
data (6.6)--(6.14), checks the five small `m=3` inverse transitions for the
minimality statement, and replays the two frozen four-cycle obstructions
(0.2)--(0.5).

Its frozen stdout is

```text
scratch/catalan_leaf_peelable_transparent_gluing_state_20260731.audit.json
```
