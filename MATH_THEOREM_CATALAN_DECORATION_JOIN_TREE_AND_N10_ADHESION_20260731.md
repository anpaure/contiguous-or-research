# Decoration relations form an exact owner-hull join tree

Date: 2026-07-31  
Status: exact relational closure and leaf-extension theorem; exact canonical
`n=10` separator audit; no all-dimension accepting-state theorem

## 0. Verdict

The terminal joint alternating-SDR problem, and likewise a transparent
multi-state gluing problem after all state variables are exposed, is an
acyclic constraint problem once the interface is normalized correctly.

For every factor state and typed turn colour, introduce one
**owner-selector** variable whose value is the block in which that colour is
matched in that state, and place it on the entire minimal subtree joining the
blocks which own candidate occurrences of that colour.  A terminal problem
has one such state.  A fixed-decoration transparent recursion additionally
keeps the selected-occurrence bits common to adjacent states.  Add the finite
occurrence-port and trace-fragment variables used by
the transparent-hexagon test.  The bags then satisfy the running-intersection
property.  Consequently the exact feasible-decoration relation is computed
by the ordinary two-pass join-tree messages

\[
 M_{x\to y}=\pi_{S_{xy}}\left(
     R_x\Join\!\!\bigJoin_{z\in N(x)\setminus\{y\}} M_{z\to x}
                               \right).                 \tag{0.1}
\]

An accepting joint decoration exists if and only if the root join is
nonempty.  This is stronger than the earlier bottom-up composition statement:
it gives the minimal named palette separator, an exact semijoin algorithm,
and a local sufficient induction hypothesis.  Namely, if every processed
leaf relation is surjective onto its parent separator, then it can be peeled
without constraining the parent.  A root witness then extends to one global
joint alternating SDR through the whole transparent gluing tree.

The theorem also makes the obstruction quantitative.  For two-owner
colours, separator size is exactly demand-path congestion.  In the canonical
lexicographic MMM tree at paper parameter `n=10`, the edge

```text
10101010101010111000  --  10101010101010110100
```

has `21` crossing upper colours, `1` crossing lower colour, and two physical
chronology edges.  Thus the exact natural palette interface there already
has width `22`, up from width `8` at `n=9`.  This disproves any extrapolation
of the small `n<=9` tables to a tiny fixed interface.  It does **not** prove
that the minimum possible width over all gluing trees is unbounded.

The remaining recursive theorem is now exact:

> choose the MMM/ECO decomposition and local correlated decoration relations
> so that their owner-hull messages survive semijoin reduction (or, more
> strongly, every leaf-extension message is separator-surjective).

Separate turn surjectivity and scalar edgewise transparency do not imply this.

## 1. Normalized owner-hull bags

Let `T` be a tree of component blocks and first fix one factor state `s`.
Every candidate turn occurrence in that state is owned by one block.  Treat
upper and lower turn colours as different typed variables.  For a typed
colour `c`, let

\[
 O_s(c)=\{x\in V(T):x\text{ owns a candidate occurrence of }c
                                      \text{ in state }s\},
 \qquad H_s(c)=\operatorname {Hull}_T O_s(c).          \tag{1.1}
\]

Introduce the selector

\[
                         w_{s,c}\in O_s(c),            \tag{1.2}
\]

whose value is the unique owner block in which the turn edge incident with
`c` is selected in state `s`.  Put this named selector in every bag indexed
by a vertex of `H_s(c)`.  When `|O_s(c)|=2` it is one bit.  This owner-selector formulation
is important: partial matching degrees on two processed sides must **add**,
so identifying those degrees by an ordinary natural join would be wrong.
The single state-specific selector turns the additive degree-one condition into
equality of one named variable.

For a terminal fixed factor there is only one state and these are all the
palette variables.  To transport one fixed selected occurrence set through a
gluing schedule, repeat (1.1)--(1.2) for every live factor state and also keep
one global bit `z_p` for every selected occurrence `p`.  A local transition
requires `w_(s,c)` to choose an occurrence with `z_p=1` in state `s`, and
similarly in the next state.  Thus a colour is allowed to move between owner
blocks when the local turn palette is permuted.  Using one unindexed selector
for all states would be an incorrect strengthening of transparency.

At every physical chronology cut, also put in both incident bags:

* the exact open/turn/residual status of each exposed occurrence;
* the orientation and first/last selected shore types of every exposed
  fragment; and
* the finite trace summary (capped zero-run length, one-run parity,
  homogeneous flag and breaker flag) needed by the binary-trace theorem.

Normalize the decomposition so that an occurrence is never forgotten before
the last glue which can change one of its two chronology neighbours.  Let
`B_x` be the resulting bag at `x`, and

\[
                     S_{xy}=B_x\cap B_y              \tag{1.3}
\]

for an edge `xy` of `T`.

### Lemma 1.1 (running intersection)

For every named variable `q`, the set of bags containing `q` is connected in
`T`.

#### Proof

For a state-indexed turn colour this set is its owner hull by construction, hence is a
subtree.  An exposed occurrence or trace fragment is placed on the unique
contiguous interval of the decomposition from the first cut which exposes it
through the last glue which can alter it.  Normalization makes that interval
connected.  All finite summary coordinates are attached to the same
fragment. \(\square\)

In one fixed state, when every colour has at most two owners, a colour with owners `u,v` occurs
on exactly the `u--v` path.  Hence the number of typed colour bits in
`S_{xy}` is

\[
 a_s(xy)=\#\{c:xy\in P_T(O_s(c))\},                \tag{1.4}
\]

the exact labelled demand-path congestion.

## 2. Local correlated relations

For each block `x`, let `R_x` contain every assignment to `B_x` which is
realized by some internally complete partial augmented matching in that
block, together with the literal local chronology transfer.

The word **correlated** is essential.  One tuple simultaneously records

1. the upper and lower named owner selectors;
2. occurrence matching statuses;
3. fragment endpoint types; and
4. the trace summary after the local transparent-glue reconnection.

If a fixed selected occurrence set is to be transported through a hexagon,
`R_x` also contains the common `z_p` variables, the state-indexed selectors,
the exact equality of the selected local turn-colour multisets on both
shores, and the retained-fragment boundary-alternation test.  If the
weaker decorate-last relation is used, `R_x` may quantify over new local
representatives instead.  The join theorem below applies to either relation;
mixing the two quantifier orders does not.

Interior augmented vertices have matching degree exactly one.  If `x` owns
candidates of colour `c` in state `s`, the local relation selects exactly one
such turn edge when `w_(s,c)=x`, and selects none when `w_(s,c)!=x`.
Equality of each state-indexed selector on all bags of its hull therefore
enforces global colour degree exactly one in that state.
Exposed occurrence degrees are still added locally when child edge sets are
joined; a sum exceeding one is rejected, and an occurrence has degree exactly
one when it is forgotten.

## 3. Exact join-tree theorem

Root `T` at `r`.  For every directed edge `x->y`, define the message (0.1),
where natural join identifies every equally named separator variable and
projection forgets all nonseparator variables.

### Theorem 3.1 (owner-hull semijoin closure)

The global feasible-decoration relation is

\[
                 \Join_{x\in V(T)}R_x.              \tag{3.1}
\]

It is nonempty with an accepting cyclic trace if and only if

\[
 R_r\Join\!\!\bigJoin_{z\in N(r)}M_{z\to r}         \tag{3.2}
\]

contains an accepting root tuple.  Every root tuple in (3.2) extends by
back-substitution to one global joint alternating SDR, and every global SDR
restricts to one such root tuple.

#### Proof

Induct on a rooted subtree.  For a leaf, its message is exactly the
projection of its local feasible relation.  At an internal vertex, compatible
child witnesses have disjoint interiors.  The natural join enforces equality
of every shared owner selector and every shared occurrence/trace variable.
The local relations enforce matching degree at most one on exposed
occurrences and exact degree one when an occurrence is forgotten.  Literal concatenation of
the stored fragments is associative and the finite run summary is exact at
each seam.  Therefore the unprojected join is precisely the set of feasible
partial decorations of the whole subtree; projecting gives (0.1).

At the root no exterior variable remains.  The same induction says (3.2) is
exactly the set of global augmented perfect matchings with their closed trace
summary.  Choosing stored child witnesses in reverse order reconstructs a
global decoration.  Restriction proves the converse. \(\square\)

This is the standard acyclic-join phenomenon, but Lemma 1.1 is what makes it
applicable: every shared turn colour remains named on the full path between
its owners.  Projecting a colour before its hull is exhausted destroys the
running-intersection property and is exactly the error in scalar
"some decoration survives this edge" arguments.

### Corollary 3.2 (state bound from owner congestion)

For one fixed factor state, suppose `S_e` has crossing colours `c` and
`p(e)` exposed physical objects,
each represented by one of at most `q` finite matching/trace states.  Then

\[
 |M_e|\le\left(\prod_{c:e\in H_s(c)}|O_s(c)|\right)q^{p(e)}. \tag{3.3}
\]

For two-owner colours this becomes `2^{a_s(e)}q^{p(e)}`, with `a_s(e)` exactly
(1.4).  Thus a uniform bound on demand-path congestion and exposed chronology ports gives a genuine
dimension-independent finite-state recursion.  Bounded local hexagon size
alone does not.  In a transparent multi-state recursion, (3.3) is multiplied
over the state-indexed selectors simultaneously live at the cut; the
terminal `n=10` audit below concerns one state only.

### Corollary 3.3 (separator-surjective leaf induction)

For a nonroot vertex `x` with parent `y`, call the processed subtree
**extension-surjective** when

\[
                         M_{x\to y}=\mathcal A_{xy}, \tag{3.4}
\]

where `A_xy` is the full set of separator assignments allowed by the bare
owner-selector, occurrence-degree and trace typing rules.

If every child subtree is extension-surjective and the root relation contains
one accepting tuple, then the whole gluing tree has an accepting global
decoration.

#### Proof

Equation (3.4) means peeling that subtree deletes no parent assignment.
Delete leaves successively.  The root relation is unchanged, so its accepting
tuple survives.  Theorem 3.1 back-substitutes one witness through every
deleted leaf. \(\square\)

This is a proof-sufficient all-dimension target stronger than mere local
nonemptiness.  It is also the exact point at which an owner-path congestion
lemma can be used: only the assignments on the demand paths crossing one
leaf edge must be extended.  No independent upper/lower Hall argument is
valid unless it proves the correlated surjectivity (3.4).

## 4. Why pairwise transparency fails and the join succeeds

In the authenticated `ML(7)` two-toggle example, each adjacent pair of
Hamilton cycles has hundreds of common linear decorations, but the triple
intersection is empty.  The two disjoint hexagons both constrain upper colour
`122`.  Scalar nonemptiness projects this named coordinate after the first
toggle and therefore accepts both edges separately.

In the owner-hull join tree, the selector for colour `122` lies in every bag on
the path between its two occurrence owners.  The first message and the second
message impose incompatible values on the same separator coordinate, so
their natural join is empty.  This is the smallest exact witness that (3.4)
cannot be replaced by "every leaf relation is nonempty."

The one-hexagon repair of that `ML(7)` cycle demonstrates the positive side:
changing the local relation, rather than projecting the conflict away,
restores a nonempty root join.

## 5. Canonical `n=10` adhesion stress test

Use the lexicographically first potential-decreasing heavy-root MMM gluing
tree and keep original plane-tree components as occurrence owners, exactly as
in the earlier `n<=9` owner-hull audit.  At `n=10` the canonical factor has
`854` plane-tree components.  On the displayed tree edge, one side contains
`333` components and the other `521`.

The crossing upper-demand multiplicities are

\[
                         2,1^{19},                   \tag{5.1}
\]

so there are `21` named upper colours on `20` owner pairs.  The lower demand
multigraph contributes the one tree-edge colour, and the final chronology
crosses the cut in two physical edges.  Therefore

\[
                       a_+(e)=21,\qquad a_-(e)=1.    \tag{5.2}

This is an exact cut value, not a maximum-over-all-trees statement.  It has
two consequences.

1. The natural exact relation on this canonical tree must retain the effects
   of 22 named palette vertices at this separator; a fixed handful of local
   hexagon bits is not the correct interface.
2. The finite sequence of maximum canonical upper adhesions through `n=9`,
   `0,1,1,2,2,3,3,7`, did not reveal the `n=10` jump.  Any uniform-width
   claim needs a proof and cannot be inferred from those fixtures.

The audit does not prove that all `2^22` bit patterns occur, nor that every
exact implementation needs `2^22` states.  Functional dependence may compress
the relation.  It proves only the exact named-variable separator and its
literal demand congestion.

## 6. What remains

The formal recursion is now closed.  The all-dimension existence statement is
not.  Any successful proof may establish one of the following, in decreasing
strength:

1. a palette-private decorated 2-factor, making all intercomponent palette
   separators empty;
2. a transparent MMM/ECO tree satisfying separator-surjective leaf extension;
3. a controlled-congestion tree whose exact messages can be shown nonempty by
   a structural Hall/augmenting-path theorem; or
4. directly, nonemptiness of the root join without a width bound.

The new theorem rules out only a proof which replaces these correlated
messages by separate turn surjectivity or one Boolean per glue.  It does not
rule out a different gluing tree, terminal redecorating, or the weaker
decorated-two-factor route.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_decoration_join_tree_n10_adhesion_20260731.py
```

The script reconstructs the canonical `n=10` base factor, its `854` original
plane-tree owners, the lexicographically first potential-decreasing gluing
tree, the final Hamilton factor, both typed owner-demand multigraphs, and the
displayed cut.  It verifies (5.1)--(5.2) literally.  The computation is
choice-specific and makes no all-`n` or optimal-tree-width claim.
