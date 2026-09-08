# Middle-Levels turn diamonds: capacity-faithful owner aliases and the exact product obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem in the serialized
owner/q1 occurrence complex, followed by an exact activation corollary and a
sharp two-coordinate no-go.  No search or computational construction is
used.  The theorem removes the need for private halfport capacity when one
claim chooses one of the two factor incidences.  It does not prove that the
named q1 occurrences are active, unused, or terminal-type legal in a given
common cap, and it does not prove cross-coordinate product closure.

## 0. Main conclusion

An oriented component of a Middle-Levels two-factor is

\[
 U_0-L_0-U_1-L_1-\cdots-U_{\ell-1}-L_{\ell-1}-U_0.
\tag{0.1}
\]

Each lower turn `L_j` has two owner halfports `U_j,U_(j+1)` and one
occurrence-labelled upper-turn cell

\[
 Z_j=(C,j;,U_j\cup U_{j+1}).
\tag{0.2}
\]

There are two literal containment paths

\[
 L_j\longrightarrow U_j\longrightarrow Z_j,
 \qquad
 L_j\longrightarrow U_{j+1}\longrightarrow Z_j.
\tag{0.3}
\]

Although the two factor halfports at an owner alias the same owner-cell
occurrence, choosing the left path at every turn, or the right path at every
turn, gives one pairwise capacity-disjoint path for every lower claim.  Each
owner cell and each upper-turn occurrence is then used exactly once.

Thus, for one claim per lower turn, owner-cell aliasing is harmless: a
component orientation bit selects a capacity-faithful owner transversal.
The full active-port suffix-rank hypothesis is unnecessary on this canonical
turn-diamond face.

For two simultaneous occurrence coordinates the conclusion changes
sharply.  Two unit demands per lower turn cannot both traverse one shared
unit-capacity owner shore; the owner shore is a cut of size `ell` for
`2ell` demands.  Exact routing requires globally owner-disjoint selected
banks, owner capacity two, or physically separate occurrence-coordinate
layers.  Even after the owner obstruction is removed, the two canonical
paths at one turn share `Z_j`, so their terminal occurrence must likewise
be split or replaced by two distinct typed sinks.

## 1. The canonical occurrence diamond

Fix a component `C` and indices modulo `ell`.  Since

\[
 U_j=L_j\cup\{a_j\},\qquad
 U_{j+1}=L_j\cup\{b_j\},\qquad a_j\ne b_j,
\tag{1.1}
\]

put

\[
 R_j=U_j\cup U_{j+1}=L_j\cup\{a_j,b_j\}.
\tag{1.2}
\]

The occurrence `Z_j=(C,j;R_j)` is the q1 upper interval at the `j`-th
turn.  The address `(C,j)` is part of the occurrence: equal values `R_j`
at different turns remain different occurrences.

Introduce three occurrence-node types:

\[
 x_j=(C,j,L_j),\qquad u_j=(C,j,U_j),\qquad z_j=Z_j.
\tag{1.3}
\]

Here `u_j` is the unique owner-cell occurrence of the factor vertex `U_j`;
the notation `(C,j)` records its position, not a second copy.  Give every
node unit capacity.  The canonical turn-diamond arcs are

\[
 x_j\to u_j\to z_j,
 \qquad
 x_j\to u_{j+1}\to z_j.
\tag{1.4}
\]

Both arcs are literal containments, with rank sequence

\[
                         m-1\longrightarrow m\longrightarrow m+1.
\tag{1.5}
\]

The first step is exactly the incidence-skeleton prefix.  The second adds
the other coordinate at that turn.  No interior occurrence besides the
displayed owner cell is used.

## 2. Exact one-coordinate router

### Theorem 2.1 (two canonical private routings)

For each bit `epsilon_C in {0,1}`, define

\[
 P_j^{(0)}:x_j\to u_j\to z_j,
 \qquad
 P_j^{(1)}:x_j\to u_{j+1}\to z_j.
\tag{2.1}
\]

For fixed `epsilon_C`, the paths

\[
 \{P_j^{(\epsilon_C)}:0\le j<\ell\}
\tag{2.2}
\]

are pairwise vertex-disjoint.  They use every lower source, every owner
cell, and every upper-turn sink exactly once.

Moreover, among routings which send every `x_j` to its own `z_j` through
one of its two adjacent owners, these are the only two unit-capacity
routings.

#### Proof

For `epsilon_C=0`, the owner used by `P_j^(0)` is `u_j`; for
`epsilon_C=1`, it is `u_(j+1)`.  In either case `j` maps bijectively to the
owner index.  The sources `x_j` and occurrence-labelled sinks `z_j` are
also pairwise distinct.  Hence the paths are pairwise vertex-disjoint and
use all three shores exactly once.

Conversely, encode a routing choice by a cyclic binary word `c_j`, where
`c_j=0` chooses `u_j` and `c_j=1` chooses `u_(j+1)`.  The owner `u_j` is
chosen by both adjacent claims precisely when

\[
                         c_{j-1}=1,\qquad c_j=0.
\tag{2.3}
\]

A unit-capacity routing therefore has no cyclic `1 -> 0` transition.  A
cyclic binary word with no such transition is constant.  Hence all choices
are zero or all are one, giving exactly the two routings in (2.2).
\(\square\)

### Corollary 2.2 (protected subbanks and side parity)

Let `S` be any set of lower turns.  Restricting either family (2.2) to
`j in S` gives pairwise disjoint routes for every claim in `S`.

If selected claims prescribe which of their two halfports must be used, a
restricted canonical routing exists exactly when all prescriptions in one
component agree with one common bit `epsilon_C`.  Components containing no
prescribed claim have a free bit.

This is the same one-bit parity obstruction as factor orientation.  It is
not a new suffix-Hall obstruction.

## 3. Exact owner-alias resolution

At owner `U_j`, the two factor halfports are the plus side of turn `j-1`
and the minus side of turn `j`.  If halfports are treated as separate
formal ports, both exist.  If they are identified with their one physical
owner-cell occurrence `u_j`, they share one unit gate.

Theorem 2.1 selects exactly one of those two halfports at every owner.
Therefore the quotient from halfports to owner cells is capacity-faithful
for the selected one-coordinate router:

\[
 \boxed{
 \text{selected load at every owner-cell alias}=1.
 }
\tag{3.1}
\]

This is stronger than saying merely that the abstract right degree is at
most two, and weaker than requiring all halfports to be independent.  The
unused halfport at an owner consumes no capacity.

For an arbitrary fixed incidence-ticket bank `H`, with every ticket forced
to use its named owner occurrence, collapsing halfports to unit owner cells
is capacity-faithful if and only if

\[
                         d_H(U)\le1
 \qquad\text{for every owner }U.
\tag{3.2}
\]

If an owner has physical capacity `c(U)` instead, the exact condition is
`d_H(U)<=c(U)`.  This elementary quotient test is the correct boundary for
simultaneously required fixed tickets; Theorem 2.1 avoids it by selecting
only one of the two candidate tickets at each claim.

## 4. Activation in a common cap

The factor serialization proves the set values, occurrence addresses, and
literal containments in (1.4).  To turn Theorem 2.1 into a common-cap
linkage after a fixed compensation linkage, require one **activated
turn-diamond embedding**:

1. the selected lower claim occurrences, owner-cell occurrences, and q1
   upper-turn occurrences are present as unit-capacity nodes in one fixed
   cap/guard/phase/occurrence state;
2. the two literal containment arcs in every selected path are legal in
   that same state;
3. the fixed compensation linkage and protected background use none of the
   selected nodes or arcs;
4. every selected `z_j` is an unused sink occurrence of a terminal type
   legal for its claim, or begins a separately certified private tail to
   such a sink; and
5. equal values at different `(C,j)` addresses remain distinct physical
   capacities.  Any value quotient must be priced separately.

### Corollary 4.1 (capacity-faithful matched-port router)

If one choice of the component bits activates the corresponding paths for
all selected claims, those claims have pairwise vertex-disjoint literal
routes to distinct legal sinks, simultaneously with the fixed compensation
linkage.

#### Proof

Theorem 2.1 gives disjointness inside every component, and different factor
components have disjoint owner/q1 occurrence addresses.  The activation
hypotheses make the abstract nodes literal, preserve their capacities, and
separate them from the fixed linkage.  The selected terminal occurrences
are distinct by their turn addresses and legal by item 4. \(\square\)

For this canonical face, no strict-gammoid full-port rank or Boolean
one-step Hall theorem remains: the complete route bank is displayed.
However, activation item 4 is a real cap premise.  Factor serialization
names `Z_j`; it does not prove that `Z_j` is free, typed as required, or
accepted by the terminal compiler.

## 5. Sharp two-coordinate boundary

### Theorem 5.1 (shared-owner cut no-go)

Suppose every lower turn of one component supplies two simultaneous unit
demands, and every demand path must pass through one of the component's
`ell` unit-capacity owner-cell occurrences.  Then no simultaneous linkage
of all `2ell` demands exists.

#### Proof

The owner shore is a vertex cut of total capacity `ell` separating the
`2ell` source units from every terminal.  Max-flow/min-cut gives linkage
size at most `ell`. \(\square\)

The no-go persists independently of the number of abstract halfport names:
two names which alias one owner cell still cross one capacity-one gate.

### Theorem 5.2 (exact product-layer repair)

If the two occurrence coordinates have physically disjoint unit-capacity
copies of every source, owner, and upper-turn terminal occurrence, then
Theorem 2.1 applies independently in the two layers.  Any two component
bits `epsilon_C^0,epsilon_C^1` give `2ell` pairwise disjoint routes in the
product network.

More generally, for a prescribed two-coordinate incidence bank
`H=H_0 dotcup H_1` in one physical owner layer, owner capacity is resolved
exactly when

\[
                         d_H(U)\le c(U)
\tag{5.1}
\]

at every owner.  In particular, globally right-disjoint coordinate banks
have owner load one.  This removes the owner obstruction but does not remove
either of the following independent requirements:

* two unit sources when both coordinate tickets at one lower turn must be
  routed; and
* two distinct terminal capacities.  The two canonical branches at one
  turn both end at the same unit occurrence `z_j`, so a simultaneous pair
  needs occurrence-coordinate copies, terminal capacity two, or different
  typed sinks.

Finally, two separately valid coordinate linkages combine only if the fixed
cap state supplies global product closure and all cross-coordinate shared
capacities have been split or allocated.  Marginal application of Theorem
2.1 cannot prove that condition.

## 6. Exact frontier

The protected Middle-Levels factor plus occurrence serialization now gives
unconditionally:

\[
 \boxed{
 \text{one canonical capacity-faithful turn-diamond router per component}
 }
\]

for one claim choosing one factor incidence.  It also gives the exact
component parity of that choice and the sharp owner-alias load.

What remains external is narrower than a generic suffix router on this
face, but it is still physical:

1. activate the named lower, owner, and q1 upper-turn occurrences after the
   compensation linkage;
2. certify the terminal type of the q1 upper-turn occurrences, or attach
   private typed tails;
3. provide source and terminal multiplicity for conjunctive two-coordinate
   tickets; and
4. prove common-state product closure.

If the required terminal sinks are not the canonical q1 upper-turn
occurrences, or if suffixes are genuinely multi-step, the prior full-rank,
one-step Boolean Hall, or typed candidate-list theorems remain necessary.

## 7. Dependencies

| role | file |
|---|---|
| occurrence addresses, owner aliases, and phase parity | `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md` |
| fixed-state regular factor/router theorem | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` |
| two-coordinate product boundary | `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md` |

