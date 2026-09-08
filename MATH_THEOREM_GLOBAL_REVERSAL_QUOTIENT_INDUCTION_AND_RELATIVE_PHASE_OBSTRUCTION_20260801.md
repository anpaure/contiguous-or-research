# Global reversal is an exact induction gauge, but it cannot change relative phase or invariant defect

**Date:** 2026-08-01  
**Lane:** same-parity Pascal regeneration / complete-reversal reset  
**Status:** exact reversal-quotient induction theorem and exact scope
separation.  The complete-reversal packet needs no local role converter in
an orientation-free prospective induction.  Global reversal supplies no
Hall gain, no component fusion, no safe opening, and no independent packet
phase choices.

## 0. Outcome

The complete reset-return packet has endpoint states

\[
                         H_3=\operatorname{rev}(H_0).          \tag{0.1}
\]

If the exterior chronology is held fixed, replacing \(H_0\) by \(H_3\)
is a genuine local phase switch and needs the recorded attachment return and
two predecessor returns.  If instead the **entire word and all of its
certificates** are reversed, (0.1) is only a change of representative.
Every interval, derivative cell, residence run and compiler edge is carried
bijectively to its reflected address.

This gives the following proof-safe simplification.

\[
 \boxed{\text{A same-parity induction may be formulated modulo global
 reversal; then }H_0\text{ and }H_3\text{ are one state.}}     \tag{0.2}
\]

On that quotient, the middle role-conversion step and the two endpoint
q-gon rethreads are unnecessary **provided the transition asks only for an
orientation class**.  One chooses the convenient representative before
constructing the child exterior.

There are three exact limitations.

1. A global reversal is an isomorphism, so every reversal-invariant defect
   (upper holes, matching deficiency, component count, sidecar size) is
   unchanged.  It is not an actuator.
2. With \(c\) independently orientable components or packets, one global
   reversal removes only one common bit.  The \(c-1\) relative phase bits
   remain.
3. Reversal preserves a completed linear word, but it does not repay targets
   lost when a cyclic component is opened.  The absolute safe-cut/ambient
   duplicate problem remains.

Thus global reversal removes the need for a **local phase-common exterior**
in a one-component prospective construction.  It does not construct the
one-component upper-complete host which is presently missing.

## 1. Exact reversal of a source word

Let

\[
                         A=(A_0,\ldots,A_{n-1})                \tag{1.1}
\]

be a word of nonempty subsets, and put

\[
                         ({\cal R}A)_i=A_{n-1-i}.              \tag{1.2}
\]

For an interval \(I=[i,j]\), write

\[
                         I^*=[n-1-j,n-1-i].                   \tag{1.3}
\]

### Lemma 1.1 (literal interval reflection)

For every interval \(I\),

\[
 \bigcup_{t\in I}({\cal R}A)_t
       =\bigcup_{t\in I^*}A_t.                               \tag{1.4}
\]

For every \(q\ge0\),

\[
 (D^q{\cal R}A)_i=(D^qA)_{n-q-1-i}.                         \tag{1.5}
\]

Consequently reversal preserves, exactly:

* the complete interval-OR and interval-intersection decks, including
  widths and multiplicities;
* every derivative-row inventory;
* every coordinate run length and signed residence inequality;
* every maximal erosion envelope, after reflecting its address; and
* every target--cell incidence relation whose cell predicate, cap and guard
  data are transported functorially by interval reflection.

#### Proof

The substitution \(u=n-1-t\) maps \(I\) bijectively to \(I^*\), proving
(1.4).  Apply it to \([i,i+q]\) to obtain (1.5).  All listed structures
are defined by these intervals or by coordinate traces, which are merely
reversed. \(\square\)

### Corollary 1.2 (certificate transport)

Suppose a target \(S\) is assigned to cell \([i,j]\) in a compiler
matching.  Assign it to \([n-1-j,n-1-i]\) after reversal.  This transports
the entire matching, all cap values attached functorially to its source
letters, and every protected witness occurrence.

The functorial qualification is necessary: a predicate that names an
absolute left address, or a guard that is deliberately not reflected, is
not covered by this corollary.  Under pure reversal the target value \(S\)
is fixed.  If reversal is composed with a ground-set permutation \(\pi\),
the corresponding target is \(\pi(S)\); hence the target family and every
prepared pin must also be \(\pi\)-closed.

The left and right boundary states are exchanged.  Prefix rays become
reversed suffix rays, predecessor and successor roles exchange, and an
ordered endpoint pair \((L,R)\) becomes \((R,L)\).  No target value is
renamed under pure reversal; under the optional permutation it is transported
as stated above.

This is an isomorphism of occurrence systems, not equality at fixed physical
addresses.

## 2. The weakest reversal-closed induction state

An **oriented complete state** at dimension \(k\) is a tuple

\[
 {\sf S}=(A,T,{\cal W},{\cal M},{\cal E},\Xi),              \tag{2.1}
\]

where:

* \(A\) is the source word and \(T=D^dA\) is its selected owner chronology;
* \({\cal W}\) is the complete chosen upper-witness bank;
* \({\cal M}\) is the occurrence-labelled lower compiler matching;
* \({\cal E}\) is the ordered endpoint/interface data; and
* \(\Xi\) is the bounded carried sidecar and every named guard needed by
  the next transition.

No field may be omitted merely because its marginal count is correct.
Define \({\cal R}_k{\sf S}\) by reversing \(A,T,{\cal W},{\cal M}\) as in
Section 1, swapping the two endpoint roles in \({\cal E}\), and reflecting
every occurrence address in \(\Xi\).  If the same-parity step introduces
an unordered fresh coordinate pair \(\{x,y\}\), allow the gauge action to
include

\[
                              x\longleftrightarrow y.          \tag{2.2}
\]

This is a ground-set automorphism and does not rename any old target.

Every directed topological datum is transported as well.  In particular,
reversal preserves the underlying path or cycle and its component count,
but negates an oriented voltage.  Thus a nonzero or coprime-voltage
condition is invariant, whereas a named signed voltage must be reflected
as part of \(\Xi\).

The **reversal-quotient state** is the orbit

\[
                         [{\sf S}]=\{{\sf S},{\cal R}_k{\sf S}\}. \tag{2.3}
\]

This is the weakest state on which orientation has genuinely been forgotten:
all occurrence data are retained, but left/right and forward/reverse are
stored only up to simultaneous reflection.

## 3. Reversal-quotient induction

Let \({\cal A}_k\) be a class of admissible complete states and let
\({\cal T}_k\subseteq{\cal A}_k\times{\cal A}_{k+2}\) be a same-parity
transition relation.

### Theorem 3.1 (reversal-quotient induction lemma)

Assume:

1. **state closure:** \({\cal R}_k{\cal A}_k={\cal A}_k\);
2. **transition equivariance:**

   \[
    ({\sf S},{\sf S}')\in{\cal T}_k
      \Longrightarrow
    ({\cal R}_k{\sf S},{\cal R}_{k+2}{\sf S}')\in{\cal T}_k; \tag{3.1}
   \]

3. **orbit-totality:** for every admissible orbit \([{\sf S}]\), at least
   one of its two representatives has a transition to some admissible child;
4. **invariant debt:** the charged length and terminal sidecar size are
   unchanged by \({\cal R}_k\).

Then \({\cal T}_k\) induces a left-total relation on quotient states.  A
base state in each parity therefore yields an existential induction through
every later dimension with the same length and sidecar bounds.  No local
phase switch between the two representatives of an orbit is required.

#### Proof

Define

\[
 [ {\sf S} ]\;\overline{\cal T}_k\;[ {\sf S}' ]
 \quad\Longleftrightarrow\quad
 \exists\,{\sf S}_0\in[{\sf S}],\ {\sf S}'_0\in[{\sf S}']:
 ({\sf S}_0,{\sf S}'_0)\in{\cal T}_k .
\]

Equivariance makes this existential definition independent of which
representative is displayed: the reflected transition has the reflected
child in the same child orbit.  Orbit-totality makes
\(\overline{\cal T}_k\) left-total.  Different transitions may lead to
different child orbits, so no uniqueness or canonical quotient function is
claimed or needed.  Choose one successor orbit at each dimension.
Condition 4 transports the quantitative bound. \(\square\)

### Remark 3.2 (equivariance is often automatic prospectively)

If a transition is stated existentially in terms of containment, union,
intersection, interval addresses, and an unordered pair of fresh coordinates,
then reflecting the completed construction proves (3.1).  An explicit
left-to-right formula need not be pointwise symmetric: its reflected formula
is the construction for the other representative.

What is not automatic is orbit-totality for an orientation-specific external
socket.  A theorem which only accepts a named right socket must either be
proved also in reflected form or must keep that orientation as real state.

## 4. Application to the complete-reversal packet

For the resident q-port converter,

\[
 H_3={\cal R}H_0,
 \qquad H_2={\cal R}H_1.                                  \tag{4.1}
\]

For the reset-return packet, its two phases are likewise opposite
orientations of one complete component.  Section 1 transports every
internal derivative and compiler occurrence.

### Theorem 4.1 (role conversion collapses in the quotient)

Suppose the same-parity transition requires only one terminal orientation
class of the complete touched component, and all exterior data belong to the
same globally reflected state.  Then

\[
                         [H_0]=[H_3],\qquad[H_1]=[H_2].       \tag{4.2}
\]

In particular, the constant-support serial history

\[
 H_0\longrightarrow H_1\longrightarrow H_2\longrightarrow H_3             \tag{4.3}
\]

is unnecessary as an induction-state conversion.  One chooses the required
representative of \([H_0]\) and constructs/reverses the complete exterior
with it.

The opened rolling-reset attachment path and its two predecessor parity
paths also reverse together.  Hence their three external returns are not
needed to compare the two representatives of one complete globally reversed
state.

#### Proof

Equation (4.2) is the definition of the quotient.  By Lemma 1.1, reversing
the full exterior transports every crossing interval and every compiler
edge as well as the packet.  The attachment and predecessor paths are parts
of the same directed occurrence system, so they reverse rather than becoming
unmatched. \(\square\)

This theorem is exactly the deferred-switching mode of the phase-common q1
host, strengthened from the packet component to the complete induction
state.  It does not assert that an arbitrary fixed exterior may be left in
place.

### Corollary 4.2 (no cross-phase intersection is required)

Let \(G^+\) and \(G^-\) be the complete occurrence-labelled compiler graphs
of two globally reversed representatives.  Reversal gives a bipartite-graph
isomorphism

\[
                              G^+\cong G^-.                    \tag{4.4}
\]

An admissible quotient state therefore needs a perfect matching in one
representative, not a perfect matching in the fixed-address intersection
\(G^+\cap G^-\).  The same statement holds for a maximal cap word and for
the chosen arbitrary-width upper-witness bank: choose them in one phase and
reflect them with the state.

Thus the phase-common residual Hall condition appearing in a literal local
switch theorem is strictly stronger than the terminal condition needed by a
reversal-quotient induction.

#### Proof

Corollary 1.2 maps every edge of a matching in \(G^+\) to one edge of a
matching in \(G^-\), and conversely.  Cap words and upper witnesses are
transported by the same address reflection.  No object is required to occupy
the same address in both representatives.  If the gauge also permutes fresh
coordinates, this is an isomorphism after applying that permutation to the
target shore; it requires the accepted target family to be invariant under
that permutation. \(\square\)

## 5. Compatibility with the known Pascal boundary state

The presently used semantic state rows are reversal-closed after the
following identifications.

1. A B1 q1 path has one missing colour contained in both endpoints.  Swapping
   the endpoints leaves it B1.
2. A prefix and suffix Ferrers bank are exchanged.  Their rank counts and
   target values are unchanged.
3. A terminal compiler matching is reflected cellwise by Corollary 1.2.
4. A clipped residence profile \((\ell,r)\) becomes \((r,\ell)\).
5. The fresh Pascal coordinates \(x,y\), or \(\alpha,\gamma\), may be
   swapped together with the two reflected sectors.
6. The split-core one-sided state with a packet prefix and a terminal
   nonowner at the right reflects to the equally valid packet-suffix state
   with the nonowner at the left.  The local formulas reflect; a global
   exterior theorem must accept one of these two representatives.

Therefore none of the scalar deadline, target, residence, B1, or semantic
Ferrers equations has an absolute orientation.  The existing conditional
regenerative theorem asks for one terminal plus construction and allows a
new terminal matching; it does not intrinsically require a local switch
against a frozen exterior.

The word **semantic** is load-bearing.  A particular prepared host may expose
only one of the two sockets, and a particular frozen cap may distinguish
their physical addresses.  Those are orbit-totality questions, not failures
of reversal invariance.

## 6. Exact obstructions

### Theorem 6.1 (global reversal cannot be an augmenting move)

Let \(\delta({\sf S})\) be any defect defined invariantly from the complete
state, including:

* the number of missing upper targets;
* terminal matching or strict-gammoid deficiency;
* number of factor components;
* sidecar cardinality; or
* number of unsupported literal targets.

Then

\[
                         \delta({\cal R}{\sf S})=\delta({\sf S}). \tag{6.1}
\]

Thus replacing \(H_0\) by \(H_3\) through global reversal cannot repair a
Hall shore or merge components.  Any positive functional-cut gain from the
packet necessarily compares two phases against the **same fixed exterior**
and is therefore a relative, not gauge, operation.

#### Proof

Lemma 1.1 and Corollary 1.2 give isomorphisms of every defining incidence
graph and preserve component counts.  Directed voltages change sign; this
preserves their zero/nonzero status, order and coprimality, but not a
prescribed signed value. \(\square\)

### Theorem 6.2 (relative-phase obstruction)

Suppose a state contains \(c\) separately orientable components or protected
packets, with phase vector

\[
                         \varepsilon\in{\mathbb F}_2^c.       \tag{6.2}
\]

If every transported component label is fixed individually, global reversal
acts by

\[
                         \varepsilon\longmapsto
                         \varepsilon+{\bf1}.                 \tag{6.3}
\]

Hence the quotient retains \(c-1\) independent relative phase bits.  In
particular, for \(c>1\) a selective flip \(\varepsilon\mapsto
\varepsilon+e_i\) is not a global reversal.

More generally reversal may permute the component labels by an involutive
permutation matrix \(P\).  Then its exact action is

\[
                         \varepsilon\longmapsto
                         {\bf1}+P\varepsilon .              \tag{6.4}
\]

This still has orbits of size at most two, so one global reversal removes
at most one simultaneous binary choice.  The particular coordinate
invariants \(\varepsilon_i+\varepsilon_c\) below apply to the setwise-fixed
case \(P=I\); they need not be literal invariants for general \(P\).

#### Proof

For \(P=I\), the orbit of \(\varepsilon\) under (6.3) has at most the two
elements \(\varepsilon,\varepsilon+{\bf1}\).  The invariants
\(\varepsilon_i+\varepsilon_c\), \(1\le i<c\), form a basis of the quotient
phase space.  For general involutive \(P\), (6.4) is itself an involution,
so every orbit again has size at most two; the asserted one-global-bit bound
follows without choosing the displayed basis. \(\square\)

Consequences:

* independently oriented Catalan components still need a connector/orientation
  theorem;
* several reset tasks whose required phases are not synchronized still need
  local converters;
* reversing one packet inside a frozen remainder is not gauge; and
* a constraint which asks the attachment role to flip while one predecessor
  role stays fixed is not reversal-covariant.

### Proposition 6.3 (absolute opening debt survives)

Let a cyclic packet be opened at one edge and embedded in a final linear
word.  Global reversal bijects the cut-crossing interval family to its
reflection but does not create noncrossing witnesses.  Hence the
\(d(2d-1)\) packet-internal self-supply loss remains an absolute opening
ledger until ambient duplicate witnesses repay it.

This does not contradict Lemma 1.1: that lemma reverses one already completed
linear word.  It does not identify a cyclic interval crossing the deleted
edge with an interval of the opened path.

## 7. Revised induction target

The weakest same-parity target no longer needs a switch-ready local phase
pair.  It is:

> **Reversal-quotient regenerative host lemma.**  In each sufficiently
> large dimension, every admissible reversal orbit with bounded sidecar has
> some representative which extends to a child complete state with bounded
> sidecar; the child state is recorded only up to simultaneous reversal of
> its entire chronology, endpoint interface, witnesses and compiler.

For a one-component carrier this removes the three-return role-conversion
gate entirely.  The remaining requirements are exactly:

1. construct one upper-complete resident coefficient-one child host;
2. give one representative a terminal compiler of bounded deficiency;
3. repay the absolute opening/cut ledger; and
4. regenerate the same reversal-orbit interface.

If the host has \(c>1\) components, add a relative-orientation/connector
certificate for its \(c-1\) surviving phase bits.

This is strictly weaker than a phase-common fixed-exterior host and strictly
stronger than marginal existence of the two packet orientations.  It is the
correct use of complete reversal as a gauge.
