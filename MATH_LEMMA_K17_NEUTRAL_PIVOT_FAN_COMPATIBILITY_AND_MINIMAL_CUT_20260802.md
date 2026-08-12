# Neutral-pivot alternating fans: exact compatibility lemma and minimal cut

**Date:** 2026-08-02  
**Status:** exact finite-state/factor-exchange lemma and projection no-go.  The
authenticated K17 bridge squares calibrate the definitions, but the abstract
counter-cut below is not asserted to occur in the frozen K17 component.  No
source, arbitrary-upper, compiler, resident-factor, word, or value claim is
made.

## 1. Literal state and primitive currents

Let `X` be a hard face of materialized factors.  A state `F in X` contains the
complete incidence vector `y(F)`, the rebuilt pair vector

\[
                 p_{L,\{T,H\}}(F)=y_{L,T}(F)y_{L,H}(F),       \tag{1.1}
\]

all ordinary, guard, and opened-provider loads, the exact exceptional
seam/history atoms, the protected-edge state, the complete augmented-incidence
partition, and both opened trace states.  A
physical primitive is an alternating C6 or a declared C8 in its *current*
state.  Thus applicability is not inherited from a catalogue at an earlier
state.

For every positive hard row `j`, let `P_j` be its literal provider-atom set
(ordinary pair atoms and, where applicable, exceptional opened seam/history
atoms) and

\[
                         n_j(F)=\sum_{q\in P_j}q(F).           \tag{1.2}
\]

This notation includes all 19,412 ordinary rows, the two literal 19,448
opened decks, and the accumulated positive guard rows.  Rows of other signs
are retained literally in `X`; they are not replaced by (1.2).

For a current-state move `C:F->F'`, define the exact killed and born provider
sets

\[
 K_j(C\mid F)=\{q\in P_j:q(F)=1, q(F')=0\},\qquad
 N_j(C\mid F)=\{q\in P_j:q(F)=0, q(F')=1\}.             \tag{1.3}
\]

Then

\[
 n_j(F')=n_j(F)-|K_j(C\mid F)|+|N_j(C\mid F)|.           \tag{1.4}
\]

The conditioning in (1.3) is essential.  If a pivot changes one selected
slot `a->a'` at a lower root and a later quench changes the complementary
slot `b->b'`, the terminal pair current is

\[
                    [a',b']-[a,b],                       \tag{1.5}
\]

not the sum of two deltas evaluated at the root state.

For opening `omega in {0,1}`, let `D_omega(F)` be the complete typed multiset
of length-one and length-two components, including coordinate, ordered port,
and bracket history.  Put `R_omega(F)=|D_omega(F)|`.  Component equality is
typed equality, not equality of lengths alone.

## 2. Exact alternating-circuit fan lemma

Let `A` be a pivot applicable at `F`, put `G=AF`, let `B` be a quench
applicable at `G`, and put `H=BG`.  The quench need not be applicable at `F`.
For every positive row define its post-pivot survivor count under the quench

\[
                  s_j(A,B)=n_j(G)-|K_j(B\mid G)|.        \tag{2.1}
\]

Its *critical demand set* is

\[
                 J(A,B)=\{j:s_j(A,B)=0\}.               \tag{2.2}
\]

For `j in J(A,B)`, define the subset of compatible terminal **pair** sockets

\[
 \Gamma_j(A,B)=
 \{(L,\{T,H\}):p_{L,\{T,H\}}\in
      N_j(B\mid G)\}.                                    \tag{2.3}
\]

The definition is literal: a socket belongs to `Gamma_j` only when its lower
root, two owners, union target, guard membership, and opened-history role all
match row `j`.  Merely planting an incidence at the same root is insufficient.
An exceptional born seam/history atom remains in `N_j` but is not called a
pair socket and hence is not placed in `Gamma_j`.

### Lemma 2.1 (strict neutral-pivot fan)

The ordered pair `A;B` is a strict, negative, two-opening fan on `X` if the
following conditions hold.

1. `A` is alternating at `F`, `B` is alternating at `G`, and both preserve
   every exact linear degree/owner row and every protected incidence.
2. `G` satisfies every hard row and has the required augmented-incidence
   topology.
3. For every positive row `j`,

   \[
      n_j(G)\ge1,\qquad
      s_j(A,B)+|N_j(B\mid G)|\ge1.                       \tag{2.4}
   \]

   Equivalently, every `j in J(A,B)` has `N_j(B|G) != empty`; every
   noncritical row has a surviving provider.  When the replacement mechanism
   is restricted to planted pair variables, this becomes
   `Gamma_j(A,B) != empty`.
4. Every other literal hard predicate holds at `H`, and for every nontrivial
   topology shore `W`,

   \[
                  \sum_{e\in\delta(W)} y_e(H)\ge1.      \tag{2.5}
   \]

5. The pivot is residence-neutral and the union-port replay of the pair is
   strictly negative in both openings:

   \[
       R_\omega(G)=R_\omega(F),\qquad
       R_\omega(H)<R_\omega(F),\quad \omega=0,1.         \tag{2.6}
   \]

Then `F->G->H` is a literal hard-face path and a strict residence descent.

#### Proof

Alternation gives the linear rows.  Condition 2 gives the first physical
prefix.  Equation (1.4) and (2.4) give every positive provider/guard/opened
row at the second prefix; the remaining signs, protection, and topology are
covered by conditions 1 and 4.  Thus both prefixes lie in `X`.  Equation
(2.6), evaluated on the complete materialized trace rather than primitive
root deltas, gives the claimed descent.  \(\square\)

At the frozen seed13 interaction square, the unique critical row is
one-based guard row 12669, with target `U=24300`.  The pivot plants
`y42197`, the quench plants `y42195`, and
`p387503=y42195*y42197` lies in `Gamma_12669`; hence (2.4) closes the row.
The same pair also transports a typed short component to a socket consumed by
the quench.  This is one exact instance of the lemma, not its universal
hypothesis.

## 3. The socket-cover condition and its Hall specialization

For a compound quench, let `P(A,B)` be all terminal provider atoms born during
the materialized packet, including any exact seam/history atoms, and form the
zero-one compatibility matrix

\[
 M_{j,p}=1[p\in P_j],\qquad j\in J(A,B),\ p\in P(A,B).   \tag{3.1}
\]

For a *fixed* materialized pair, terminal provider legality is exactly

\[
       \sum_{p\in P(A,B)}M_{j,p}\ge1
       \quad(j\in J(A,B)).                               \tag{3.2}
\]

For a multi-primitive quench, the analogous matrix inequality must hold at
every materialized prefix; a terminal cover cannot repair an illegal earlier
state under strict semantics.

If sockets are being selected, their indicator `x` must additionally lie in
the circuit-coherent set `C_F`: all selected sockets must be realizable by
one common alternating pivot/quench path with its owner, protection, and
topology equations.  The exact selectable condition is therefore

\[
                  Mx\ge\mathbf 1,\qquad x\in C_F.        \tag{3.3}
\]

Scalar provider loads determine neither `M` nor `C_F`.

Only in the special case where each demand must use a distinct unit-capacity
socket does (3.3) reduce to an ordinary matching condition.  After collapsing
rows that one literal satisfies simultaneously, Hall's inequalities are

\[
               |N(J')|\ge |J'|\qquad(J'\subseteq J).    \tag{3.4}
\]

Without the exclusivity assumption, (3.4) is not the right theorem: one pair
literal can simultaneously satisfy an ordinary row, a guard row, and one row
in each opened deck.  The general object is the typed cover (3.3).

The smallest provider obstruction is the one-row/one-socket zero
neighborhood

\[
                     J=\{j\},\quad P=\{p\},\quad
                     M_{j,p}=0.                         \tag{3.5}
\]

It says exactly that a pivot planted a half-incidence, but the resulting pair
has the wrong owner union, history, or guard membership for the row destroyed
by the quench.

### Corollary 3.1 (what multiplicity actually buys)

At an ordinary lower root there is one selected pair atom.  Hence a primitive
touching `m` ordinary roots kills at most `m` pair providers of any one
ordinary target.  For a fixed candidate quench `B`, either of the following
candidate-relative inequalities removes its ordinary last-provider cut:

\[
       n_U(G)>|K_U(B\mid G)|,
       \qquad\hbox{or more coarsely}\qquad n_U(G)>m.     \tag{3.6}
\]

Thus multiplicity at least four protects an ordinary row from any single C6,
and multiplicity at least five protects it from any single four-root
star-C8.  These bounds concern only loss of ordinary pair providers.  They do
not produce an alternating circuit or a negative trace socket, and they do
not certify the exceptional opened targets: those require the exact
orientation-specific seam/history witness transversal.  For a compound path,
(3.6) must be checked at every materialized prefix (or replaced by a valid
bound on the union of all prefix killer sets).

## 4. Scalar multiplicity and connectedness do not imply a fan

Define the coarse projection

\[
 \pi(F)=\bigl(R_0(F),R_1(F),(n_j(F))_{j\in H^+},
               \#\operatorname{comp}(F)\bigr),          \tag{4.1}
\]

where `H^+` is the complete family of positive ordinary, guard, and opened
rows.  Thus even the entire vector of positive hard-row multiplicities is
retained; only provider identities and ports are forgotten.

### Proposition 4.1 (typed-twin no-go)

Existence of a strict neutral-pivot/negative-quench fan is not determined by
`pi(F)`.  In particular, positive residence, arbitrary prescribed positive
q1 multiplicities, and one-component topology do not guarantee such a fan.

#### Construction and proof

Take two exact-degree exchange gadgets with identical selected counts,
identical fixed connected spines, identical trace cardinalities, and identical
provider-load vectors.  In each gadget:

* a pivot `A` leaves an old sole provider `p_old=y_r*y_d` alive and is neutral
  in both opened residences;
* after `A`, a quench `B` is alternating, deletes `y_d`, plants `y_b`, and
  removes one typed short component without birthing another; and
* auxiliary alternating triangles balance every root and owner current and
  fixed spine edges keep all displayed prefixes connected.  Concretely, a
  desired selected-slot substitution is completed to a C6 by two private
  roots and owners: toggle the old perfect matching of a `3 by 3` incidence
  block to its cyclic shift.  A protected augmented spine disjoint from these
  private balance ports makes connectivity invariant.

In the **compatible twin**, `A` plants `y_a` and the literal
`p_new=y_a*y_b` belongs to the threatened row `j`.  In the **twisted twin**,
it plants an owner/history-compatible incidence count but of type `y_a'`, for
which `p'=y_a'*y_b` does not belong to row `j`.  All scalar values before the
quench are the same.  The compatible endpoint has the handoff

\[
                  p_{old}:1\to0,\qquad p_{new}:0\to1,   \tag{4.2}
\]

and Lemma 2.1 accepts it.  The twisted endpoint has

\[
                  p_{old}:1\to0,\qquad p':0\to1,
                  \qquad n_j:1\to0,                     \tag{4.3}
\]

and is rejected.  All other q1 rows can be given any prescribed common
positive multiplicity by adjoining untouched provider pairs.  If `j` is an
accumulated guard row rather than a q1 row, *every* q1 multiplicity can be
made arbitrarily large without changing the obstruction.  The scalar guard
load is still one in both root twins, so even the enlarged projection (4.1)
cannot distinguish them.  Unused exchange
ports may be protected or given selected-state no-goods, so the displayed
fan is the only declared candidate in the finite gadget.

Thus the two root states have equal (4.1) but different fan answers.  The
difference is the single entry (3.5), which `pi` discards.  \(\square\)

The construction is a factor/exchange countermodel to an implication from
the coarse hypotheses.  It is not an assertion that either twin embeds in the
current K17 Pascal incidence geometry.

Three independent losses of information remain even if provider slack makes
(3.2) automatic.

1. **Alternation.** Positive residence does not imply that any C6/C8 is
   alternating at a port incident to a defect.
2. **Trace absorption.** `R_omega>0` records a token count, not adjacency of a
   token to a quench that merges it without a compensating birth.
3. **Topology.** Connectedness gives only one selected crossing of every
   shore.  A proposed move may delete the unique crossing.  The exact margin
   is (2.5), not the initial component count.

Consequently high q1 multiplicity removes only provider-loss cuts.  It cannot
by itself supply an alternating port, a typed trace absorber, guard slack, or
a topology-preserving shore crossing.

## 5. Smallest exact accepting cut

Build the two-layer fan graph `G_F` as follows.  Its root is `F`.  The first
layer contains every hard-legal neutral pivot endpoint `G=AF`.  From each
such `G`, regenerate every current-state quench and retain an arc only when
its physical head is hard legal.  Add an accepting sink `t` from a retained
head exactly when both opened residences are strictly below their values at
`F` (or when the declared vector acceptance rule holds).

There are two minimal obstructions.

* Without assuming a pivot exists, a positive state with no hard-legal
  outgoing primitive gives the one-vertex closed shore `S={F}`.
* After requiring a positive-length neutral pivot and a geometrically
  negative quench proposal, the smallest obstruction has two reachable legal
  states `F->G`.  The only quench proposal from `G` has the zero-neighborhood
  (3.5), a guard failure, or a topology shore with zero terminal crossing, so
  its head is not in `X`.  Then `S={F,G}` is closed.  Two legal vertices are
  necessary because a positive-length pivot must have a legal head, so this
  obstruction is minimal in reachable-state count under that requirement.

Let `N` be the head-minus-tail incidence matrix of the retained hard-legal
fan graph, and let `b=e_t-e_F`.  For either closed reachable shore `S` above,

\[
                   z=-\mathbf1_S,qquad N^Tz\le0,
                   \qquad b^Tz=1.                       \tag{5.1}
\]

This is the exact Farkas certificate that no unit `F`-to-`t` flow exists.
The inequality holds because there is no retained arc leaving `S`; arcs
entering `S` have negative reduced incidence.  If `t` is reachable but no
accepted path has negative cost, the corresponding obstruction is instead a
Bellman--Ford potential

\[
                 \rho(v)-\rho(u)\le c(u,v),
                 \qquad \rho(t)-\rho(F)\ge0.            \tag{5.2}
\]

Rejected geometric proposals are not silently discarded in an audit: each
boundary proposal is labelled by an exact alternation, provider/guard,
protection, topology-shore, opened-history, or trace-acceptance certificate.
An empty sampled portfolio is not (5.1).

## 6. Exact additional expansion hypothesis

The missing hypothesis is not a lower bound on scalar q1 multiplicity.  It is
a product expansion statement.

For a hard state `F`, let `K_F^lit` be the bipartite compatibility graph whose
left vertices are hard-legal neutral pivots and whose right vertices are all
state-relative quench spokes in the declared circuit family.  Join `A` to
`B` exactly when:

1. `B` is alternating after `A`;
2. the circuit-coherent typed cover (3.3) holds for every ordinary, guard,
   and both-opened critical row;
3. every remaining literal hard predicate, protected incidence, and
   topology-shore inequality holds at both prefixes.

Label such an edge by its exact two-opening trace current and let `E_R(K_F^lit)`
be the subset for which the current is strictly negative in both openings.

Then a strict two-face fan exists **if and only if**

\[
                             |E_R(K_F^{lit})|>0.         \tag{6.1}
\]

For a renewal family `Y`, the exact uniform hypothesis is

\[
 \forall F\in Y,\quad \max(R_0(F),R_1(F))>0
       \Longrightarrow |E_R(K_F^{lit})|>0
       \text{ and the chosen head lies in }Y.            \tag{6.2}
\]

Under (6.2), the nonnegative integer `max(R_0,R_1)` decreases at every
commit, so repeated regeneration terminates at residence zero.  Proposition
4.1 proves that (6.2) cannot be replaced by positivity, q1 provider-load
bounds, and connectedness alone.

For a second payload coordinate `U(F)` (for example a declared deeper-upper
hole count), label every compatibility edge by

\[
       c(A,B)=\bigl(R_0(H)-R_0(F),R_1(H)-R_1(F),
                    U(H)-U(F)\bigr).                     \tag{6.3}
\]

The two-objective accepting graph is obtained from the same literal graph
`K_F^lit` by changing only the terminal rule: coordinatewise
descent, lexicographic descent, or a bounded mixed-radix scalar must be stated
explicitly.  A provider-safe residence edge need not be an upper-safe edge.
Thus adding an upper payload coordinate strengthens, rather than repairs, the
need for product expansion.

## 7. K17 scope

The frozen K17 data prove several nonempty compatibility edges: the seed13
provider square, the 2025 neutral bridge followed by its regenerated quench,
and the residence-1994 activated C6/star-C8 pair.  The strict 2025 singleton
floor also proves that the coarse invariants do not force a negative
*primitive*.  No frozen exhaustive condensation or fan graph currently
proves that the minimal closed shore of Section 5 occurs—or cannot occur—in
the full guarded K17 component.  Establishing (6.2), or producing a complete
reachable-shore certificate (5.1), remains the exact finite alternative.
