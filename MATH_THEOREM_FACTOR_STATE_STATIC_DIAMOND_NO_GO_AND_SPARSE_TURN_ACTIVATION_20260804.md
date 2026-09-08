# Factor-state static-diamond no-go and exact sparse-turn activation

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional theorem in the currently proved serialized
Middle-Levels occurrence interface, plus a sharp logical obstruction to the
proposed static-good-diamond abundance lemma.  It does not rule out a richer
common cap containing nonfactor Hasse arcs or additional occurrence copies.

## 0. Verdict

The proposed fixed-state hypothesis

\[
 \text{every gain has }\Theta(m)\text{ active direct owner ports, each with
 }\Theta(m)\text{ active direct sinks}
\tag{0.1}
\]

does not follow from the actual protected-factor/occurrence construction.
On its canonical turn-diamond face it is impossible:

\[
 \boxed{L_0\le2,\qquad L_1\le2,\qquad L_1^{\rm own}\le1.}
\tag{0.2}
\]

The quadratic full-wedge menu is prospective.  Once a factor is fixed, the
degree-two equation chooses exactly one wedge at a lower turn, leaving its
two sides and one own-q1 terminal.

This does **not** block routing.  For a selected subbank of factor turns,
the exact fixed-state routing condition is a one-dimensional monotone-side
condition.  If the gain occurrences can be selected on pairwise
nonconsecutive turns, any locally active side works.  Thus only
`O(number of gains)` eligible turn occurrences per gain are sufficient; a
linear bank of ports behind one frozen source is unnecessary.

## 1. The certified factor-state occurrence complex

Fix an oriented component of a Middle-Levels two-factor:

\[
 U_0-L_0-U_1-L_1-\cdots-U_{\ell-1}-L_{\ell-1}-U_0,
\tag{1.1}
\]

with indices modulo `ell`.  Its certified occurrence nodes are

\[
 x_j=(C,j,L_j),\qquad u_j=(C,j,U_j),\qquad
 z_j=(C,j,U_j\cup U_{j+1}),
\tag{1.2}
\]

and its two canonical branches are

\[
 P_j^0:x_j\longrightarrow u_j\longrightarrow z_j,
 \qquad
 P_j^1:x_j\longrightarrow u_{j+1}\longrightarrow z_j.
\tag{1.3}
\]

The addresses in (1.2), not merely their Boolean values, are the physical
occurrences.  Equal values at different addresses remain separate unless a
later cap quotient explicitly identifies them.

Fix one residual cap/guard/phase/occurrence state `c`, after deleting the
compensation linkage and protected capacities.  For each turn define

\[
 A_j(c)=\{\epsilon\in\{0,1\}:P_j^\epsilon
  \text{ is active, typed legal, and disjoint from the deleted bank in }c\}.
\tag{1.4}
\]

All activation statements below refer to this one already materialized
state.

## 2. Exact collapse of a prospective wedge menu

### Theorem 2.1 (factor-state degree obstruction)

Suppose the only certified direct gain-to-owner prefixes at `x_j` are the
incidence-skeleton arcs of the fixed factor.  Then `x_j` has at most two
candidate owner occurrences.  In the complete certified factor-q1
incidence complex, an owner occurrence belongs to its two adjacent turns and
therefore has at most two direct q1 sink occurrences.  If suffixes are
restricted to the canonical own-q1 turn diamond, each selected incidence
has exactly one candidate sink occurrence, namely `z_j`, and the two
branches share it.

Consequently any state-first good-diamond parameters on this certified face
satisfy

\[
 L_0\le2,\qquad L_1\le2,\qquad L_1^{\rm own}\le1.
\tag{2.1}
\]

#### Proof

The spanning two-factor has degree two at every lower vertex.  Its two
incidences at `L_j` are precisely `L_j--U_j` and `L_j--U_(j+1)`, and the
occurrence lift creates one direct halfport for each.  There is no third
factor incidence at that source occurrence.

The owner `u_j` lies only in the q1 turns `z_(j-1)` and `z_j`; similarly
`u_(j+1)` lies only in `z_j` and `z_(j+1)`.  Hence the complete certified
factor-q1 sink degree is at most two.  The canonical q1 cell of the selected
turn is the single occurrence `z_j`, whose value is `U_j union U_(j+1)`.
Each of its two owner occurrences has the one displayed own-turn arc to
`z_j`.  This proves all three bounds. \(\square\)

### Corollary 2.2 (the full-wedge menu is not a frozen neighbourhood)

Before factor selection, a lower value `L` has `binom(m,2)` possible full
wedges.  After a factor is fixed, exactly one of those wedges is present at
the occurrence of `L`.

#### Proof

A full wedge consumes the two factor incidences at `L`.  Two distinct
wedges use at least three distinct incidences there, contradicting degree
two.  Conversely the two neighbours of `L` in the fixed factor determine
one unordered wedge. \(\square\)

Thus the prospective quadratic wedge count cannot be cited as a large
active menu after the chronology and its occurrence state have been frozen.

### Corollary 2.3 (sharp logical nonimplication)

The protected-factor theorem, its occurrence lift, and the canonical
turn-diamond theorem do not imply static good-diamond abundance.

#### Proof

Given any protected factor, materialize exactly the occurrence nodes and
arcs in (1.2)--(1.3), make all of them active and typed legal, and place the
fixed compensation linkage on a disjoint capacity bank.  This state realizes
every certified factor and turn-diamond assertion, but Theorem 2.1 gives
`L_0=2,L_1^(own)=1`.  Hence a conclusion with either parameter tending to
infinity cannot be derived from those hypotheses. \(\square\)

This is a scoped model obstruction, not a claim that the real common cap
cannot be enriched with nonfactor Hasse arcs, replicated source layers, or
additional typed sinks.  Such an enrichment is exactly a new theorem.

## 3. Exact routing on a selected set of turns

Let `S` be a set of selected turn indices in one component.  Seek choices

\[
                         c_j\in A_j(c)\qquad(j\in S)
\tag{3.1}
\]

so that the corresponding branches `P_j^(c_j)` are pairwise
vertex-disjoint.

### Theorem 3.1 (selected-turn monotone-side criterion)

The choices in (3.1) give pairwise disjoint canonical routes if and only if

\[
 \boxed{
  (j-1,j\in S)\Longrightarrow(c_{j-1},c_j)\ne(1,0).}
\tag{3.2}
\]

If `S` is a proper subset of the component, its maximal cyclically
consecutive runs are ordinary directed paths.  On every such run, a legal
routing exists exactly when:

1. every `A_j(c)` is nonempty; and
2. no turn forced to side one precedes a later turn forced to side zero.

Equivalently, with the convention that a missing maximum is `-infinity`
and a missing minimum is `+infinity`, every run satisfies

\[
 \boxed{
  \max\{t:A_t(c)=\{0\}\}
  <
  \min\{t:A_t(c)=\{1\}\}.}
\tag{3.3}
\]

Each run in (3.3) is reindexed as `1,...,r` in its forward cyclic order;
the original residues modulo `ell` are not compared across the chosen gap.

If `S` is the complete cyclic component, a routing exists exactly when

\[
                         \bigcap_{j=0}^{\ell-1}A_j(c)\ne\varnothing.
\tag{3.4}
\]

#### Proof

The sources `x_j` and occurrence-labelled sinks `z_j` are distinct.  The
only possible collision is at an owner `u_j`.  It is used from the left by
turn `j-1` precisely when `c_(j-1)=1`, and from the right by turn `j`
precisely when `c_j=0`.  This proves (3.2).

On a directed path, (3.2) says the binary choices are nondecreasing.  Such a
word exists under the allowed sets precisely when no forced one occurs
before a forced zero, which is (3.3); choose a threshold between the last
forced zero and the first forced one.  On a directed cycle, a nondecreasing
cyclic binary word is constant, giving (3.4). \(\square\)

### Corollary 3.2 (two useful sufficient faces)

1. If `S` is independent in the cycle graph and every `A_j(c)` is nonempty,
   then all selected claims route privately; each may use either allowed
   side independently.
2. If one bit `epsilon_C` belongs to every `A_j(c)` for the selected turns
   of a component, choosing that bit throughout gives a private routing.

The minimal local obstruction is also exact: two consecutive selected turns
with the earlier one forced to side one and the later one forced to side zero
cannot route, although each has an individually active branch.

For several factor components, apply Theorem 3.1 independently.  Occurrence
addresses from different components are disjoint.  A later quotient which
identifies equal values across addresses needs a separate capacity ledger.

## 4. A sparse active-turn transversal

The selected turns need not be fixed in advance.  Let `G` be `p` logical
tasks whose semantics permit alternative source occurrences.  For every
task `g`, let `T_g` be a menu of turn occurrences at which the task has at
least one branch active and typed legal in the same state `c`.  A turn
occurrence conflicts with itself and with its two cyclic neighbours, so it
conflicts with at most three members of any other menu.

### Theorem 4.1 (greedy independent-turn selection)

If

\[
                         |T_g|>3(p-1)\qquad(g\in G),
\tag{4.1}
\]

then one can choose `t_g in T_g` so that the chosen turns are pairwise
distinct and pairwise nonconsecutive within every factor component.  The
chosen active branches are then pairwise vertex-disjoint.

#### Proof

Process the gains in any order.  Each previously chosen turn deletes from
the next menu only itself and its two neighbours, at most three candidates.
After fewer than `p` choices, fewer than or equal to `3(p-1)` candidates are
forbidden, so (4.1) leaves a choice.  The selected set is independent in
every component cycle.  Apply Corollary 3.2. \(\square\)

This is asymptotically much weaker than (0.1).  For `p=O(d)` it requires
only `O(d)` active candidate **turn occurrences** per gain, not
`Theta(m)` active ports behind one frozen source occurrence.

The source-flexibility qualification is essential.  A spanning factor has
one vertex for each rank-`(m-1)` value.  If a gain is required to start at
one fixed Boolean source value and no occurrence copies are supplied, it has
only that one turn occurrence; Theorem 4.1 then does not apply.  Its exact
gate is Theorem 3.1 (or the protected-wedge activation lemma below).

There is a crude forbidden-bank form.  Suppose every gain has `L` raw
claim-compatible active turn occurrences before a fixed occurrence bank
`F` is reserved.  In the canonical complex, a forbidden source or q1 sink
lies in one turn diamond and a forbidden owner lies in two.  Deleting every
turn diamond meeting `F` therefore leaves at least

\[
                         L-2|F|
\tag{4.2}
\]

candidates per gain.  Hence

\[
                         L>3(p-1)+2|F|
\tag{4.3}
\]

suffices.  This count is only for occurrence nodes in the displayed
canonical complex; shared flags, arcs, or hidden cap resources must be
charged separately in the definition of `T_g`.

## 5. Relation to protected wedge selection

The protected full-wedge theorem already selects, prospectively, one wedge
per distinct lower gain so that all selected owner values and q1 terminal
values are distinct, then protects those wedges in a spanning two-factor.
For that bank there is no remaining inter-gain owner or terminal matching:
if one branch of every selected wedge is active in one common cap state, the
resulting routes are automatically private.

Accordingly the weakest factor-based completion statement is not static
linear diamond abundance.  It is:

> **Protected-wedge activation lemma.**  The prospective conflict-free wedge
> bank and its factor completion can be chosen together with one residual
> cap/guard/phase/occurrence state in which every selected wedge retains one
> active typed branch, every selected source and q1 terminal occurrence is
> present, and the bank avoids the compensation linkage.

This lemma has one existential choice per gain, not a large frozen
neighbourhood.  It is still unproved: the existing wedge theorem selects
Boolean values and factor incidences, while the common-cap theorem requires
literal occurrence activation after all guards are fixed.

Alternatively, for the pre-assignment Pascal tasks which genuinely have
multiple legal source anchors, Theorem 4.1 gives the following fixed-state
target:

> **Sparse active-turn lemma.**  In one materialized residual state, every
> source-flexible one-coordinate task has more than `3(p-1)`
> claim-compatible active turn
> occurrences.

Either lemma closes the one-coordinate private prefix/own-q1 routing row.
Neither follows from separate marginal prefix and suffix abundance.

## 6. Source and product multiplicity remain sharp

The preceding theorems route one unit claim per selected turn.  If two
occurrence-coordinate claims share the one unit source `x_j`, that source is
a cut of capacity one for demand two.  If the source is copied but both
branches must traverse one owner layer or terminate at the one occurrence
`z_j`, the owner and terminal shores give the corresponding capacity cuts.

Thus a two-coordinate theorem still requires one of:

* physically separate source, owner, and terminal layers;
* sufficient capacity at every shared occurrence; or
* globally owner- and terminal-disjoint selected banks with two source
  units and one common product-closed state.

The static abundance of unused Boolean values cannot repair a missing
physical source unit.

## 7. Exact scope

This note proves:

* the exact degree-two/degree-one collapse of the current fixed factor face;
* a model showing that current factor and turn-diamond theorems cannot imply
  static linear good-diamond abundance;
* the exact activation criterion for an arbitrary selected turn subbank;
* a greedy `3(p-1)` fixed-state active-turn transversal; and
* the narrower protected-wedge and sparse-active-turn lemmas which would
  close the actual one-coordinate routing row.

It does not prove either remaining activation lemma for the current Pascal
child, authenticate transported phase one, create a second source layer, or
establish the upper deck, residence, common compiler, topology, or
regeneration.
