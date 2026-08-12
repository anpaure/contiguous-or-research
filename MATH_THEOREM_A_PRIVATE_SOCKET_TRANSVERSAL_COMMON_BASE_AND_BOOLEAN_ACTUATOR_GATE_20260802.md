# Private socket tickets, the exact cotransversal common-base criterion, and
# the Boolean actuator gate

**Date:** 2026-08-02  
**Lane:** A, central common-base/reset and movable-bottom recoupling  
**Status:** exact conditional matroid theorem and proof-safe scope audit of the
known Boolean `C6/C8/C10` actuators.  No literal `1S` socket bank, common-state
cycle cover, residence, upper-shadow, topology, source, compiler, or word is
claimed.

## 0. Verdict

Let `E` be the hard-slot ground and let `f` be the number of short slots.
The bottom-token theorem proves that the outer-feasible short sets are the
bases of the rank-`f` cotransversal matroid

\[
                 M_{\rm short}=(M/\mathcal F)^* .       \tag{0.1}
\]

There is an equally exact second matroid for any stated ticket subatlas in
which socket completion really factors through a bipartite ticket--slot
graph in both directions.  If `T` is a set of `f` distinguishable tickets and
`A_t\subseteq E` is a fixed menu for ticket `t`, then

\[
 I\subseteq E\text{ is independent}
 \quad\Longleftrightarrow\quad
 I\text{ can be matched to distinct tickets in }T              \tag{0.2}
\]

defines a transversal matroid `M_sock`.  Its bases are exactly the
socket-complete short sets provided the physical ticket modes satisfy both
directions of the private-composition axiom in Section 2.  The resulting
outer-plus-socket face has a feasible short bank exactly when

\[
 r_{M_{\rm short}}(X)+
 r_{M_{\rm sock}}(E-X)\ge f
 \qquad(X\subseteq E).                                  \tag{0.3}
\]

This specializes the conditional interface in the bottom-token note to the
explicit matching rank

\[
             r_{M_{\rm sock}}(Y)=\nu_\Gamma(T,Y),        \tag{0.4}
\]

where `Gamma` is the ticket--slot graph.

The present Boolean interval actuators do **not** yet realize this face.
The hub `C6`, the one-aperture parity-breaking `C8`, and the saturated
`B5 C10`, in their movable-bottom realizations, use only real
bottom-to-hard-slot edges in both phases.  Hence they preserve the set of
dummy-matched hard slots occurrencewise.  They are exact circuits inside a
fixed fibre of the map

\[
       \{\text{bottom perfect matchings}\}\longrightarrow
       \{\text{short sets}\},                           \tag{0.5}
\]

not ticket edges for a second matroid on short slots.  In particular, the
`C8` aperture is a missing interval of a saturated resource fibre, not a
bottomless hard slot.  The combined `C10+C6` absorber has the same issue.

Thus the Boolean circuits are useful as internal mode routers after a short
set has been chosen, but they do not prove `M_sock`.  The missing bridge is
a **dummy-bearing completed ticket**: it must bind one named short slot to a
complete Boolean actuator, have a fixed selection-independent menu, and be
private from all other chosen tickets in every literal capacity/state row.

## 1. The outer cotransversal matroid

Use the notation of
`MATH_THEOREM_K17_BOTTOM_TOKEN_PERFECT_MATCHING_AND_COMPOUND_RELAY_CIRCUITS_20260802.md`.
Let `M` be the transversal matroid on

\[
                  \mathcal F\mathbin{\dot\cup}E          \tag{1.1}
\]

induced by the real bottom tokens, and assume \(\mathcal F\) is independent.
A set `S\subseteq E`, `|S|=f`, is the short set of an exact outer table if
and only if

\[
               \mathcal F\mathbin{\dot\cup}(E-S)         \tag{1.2}
\]

is a basis of `M`.  Equivalently, `E-S` is a basis of \(M/\mathcal F\), so
`S` is a basis of (0.1).  This is the exact outer condition; no socket or
state compatibility is used.

The fundamental exchanges of `M_short` are precisely the dummy-bearing
alternating paths/circuits of the augmented bottom matching.  A circuit
containing no dummy is invisible in (0.1): it changes a bottom assignment
without changing `S`.

## 2. Exact private-ticket hypothesis

Let `T` be a set of `f` distinguishable socket obligations.  A **private
ticket presentation** on `E` consists of a bipartite graph

\[
                        \Gamma\subseteq T\times E        \tag{2.1}
\]

and one completed literal mode \(\mu_{t,e}\) for every \(te\in\Gamma\), subject
to the following conditions.

1. **Unary short signature.**  Mode \(\mu_{t,e}\) declares `e` short and
   makes no demand on the short/long status of another ground element.
2. **Fixed menu.**  Membership `e in A_t:=N_Gamma(t)` is determined before
   any other ticket is chosen.  It is not changed by a common history,
   orientation, cap, or another selected mode.
3. **Private composition (soundness).**  For every matching
   \(Q\subseteq\Gamma\), the modes \(\{\mu_{t,e}:te\in Q\}\) compose literally.
   Their union violates no occurrence, owner, palette, state, history, cap,
   topology-port, guard, or other capacity-one row.  A sufficient, stronger
   condition is that all mode-dependent footprints of distinct ticket
   identities are disjoint and that the only shared capacity is the hard
   slot `e`.
4. **Private decomposition (completeness).**  Every socket-complete state in
   the declared subatlas with short set `S` decomposes into modes
   \(\mu_{t,e}\) giving a matching in `Gamma` which saturates `T` and has slot
   shore exactly `S`.

Soundness alone gives a valid transversal **sufficient subface**.  The
completeness clause is required before a failed common-base cut can be
called an impossibility theorem for the declared physical class.

### Theorem 2.1 (private sockets form a transversal matroid)

Under Conditions 1--3, the short-slot sets obtainable from partial private
ticket assignments are exactly the independent sets of the transversal
matroid `M_sock=M[Gamma]` on `E`:

\[
 I\in\mathcal I(M_{\rm sock})
 \quad\Longleftrightarrow\quad
 \text{there is a matching of }I\text{ into }T.            \tag{2.2}
\]

Its rank function is (0.4).  If `Gamma` has a matching saturating `T`, then
`r(M_sock)=f`.  Under Condition 4 as well, its rank-`f` bases are exactly
the socket-complete short sets of the declared physical subatlas.

#### Proof

The matchable subsets of one shore of a bipartite graph are the independent
sets of its transversal matroid.  Conditions 1--3 lift every such matching
to a jointly legal family of literal modes, so every independent set has a
physical realization.  Conversely, Condition 4 maps every complete
physical realization back to a matching saturating `T`.  A matching
saturating `T` has `f` distinct slot endpoints, and every rank-`f` matching
uses every ticket.  This proves all statements.  \(\square\)

### Corollary 2.2 (exact common-base criterion)

Assume the exact outer theorem and all four private-ticket conditions.  An
outer-feasible socket-complete short set exists if and only if (0.3) holds.
Equivalently,

\[
       r_{M_{\rm short}}(X)+\nu_\Gamma(T,E-X)\ge f
       \qquad(X\subseteq E).                         \tag{2.3}
\]

#### Proof

Both matroids have rank `f`.  The desired set is a common basis.
Edmonds' matroid-intersection min--max theorem says that their maximum
common independent-set size is

\[
        \min_{X\subseteq E}
        \bigl(r_{M_{\rm short}}(X)+r_{M_{\rm sock}}(E-X)\bigr).
\]

It equals `f` exactly under (0.3); substitute (0.4) for (2.3). \(\square\)

This theorem is an existence/min--max statement.  A circuit-complete
physical absorber additionally needs every matroid-intersection exchange
path used by the construction to lift to literal protected packet moves.
Neither matroid intersection nor ticket privacy alone supplies that lift.

### Corollary 2.3 (forced-long actuator support)

Let \(P\subseteq E\) be a hard-slot bank which a planted Boolean actuator
requires to remain occupied by real bottoms in every phase.  Then its short
set must avoid \(P\).  The exact private common-base criterion is therefore
applied on \(E-P\) to the deletion minors

\[
          M_{\rm short}\backslash P,
          \qquad M_{\rm sock}\backslash P.          \tag{2.4}
\]

Such a short set of size \(f\) exists if and only if both deletion minors
have rank \(f\) and

\[
 r_{M_{\rm short}\backslash P}(X)+
 r_{M_{\rm sock}\backslash P}((E-P)-X)\ge f
 \qquad(X\subseteq E-P).                            \tag{2.5}
\]

In particular, a movable-bottom `C8` phase reserves its four fixed suffix
slots as long.  A literal bottom-layer realization of the combined
`C10+C6` replacement reserves its eight changed real-bottom slots, and any
additional unchanged support required by the planted module must also be
added to \(P\).  This does not make either actuator a socket ticket: it
only lets a separately proved private ticket matroid be selected away from
the actuator footprint.

#### Proof

Forcing \(P\) long is exactly the condition \(S\cap P=\varnothing\) on
the short basis.  Independent sets avoiding \(P\) are the independent sets
of the deletion minor.  A common short basis avoiding \(P\) is therefore a
size-\(f\) common independent set of the two deletion minors.  Edmonds'
formula gives (2.5), while rank \(f\) of both minors is necessary and also
follows from the cut system by taking \(X=E-P\) and \(X=\varnothing\).
\(\square\)

## 3. Why per-slot eligibility is not enough

Individual socket menus do not imply a transversal matroid when tickets
share a state choice.  The smallest useful abstract obstruction has

\[
       E=\{1,2,3,4\},\qquad T=\{a,b\}.               \tag{3.1}
\]

Suppose every element is individually eligible, but a common binary state
requires both selected slots to lie in `{1,2}` in state zero or both to lie
in `{3,4}` in state one.  The complete feasible short sets are then

\[
                         \{1,2\},\ \{3,4\}.          \tag{3.2}
\]

They violate basis exchange: from the first basis and element `1`, neither
replacement by `3` nor replacement by `4` is feasible.  Thus (3.2) is not
the basis family of any matroid.

This counterexample is not asserted to occur in the K17 table.  It proves
the logical boundary: a shared common-state, flag, or cap choice may destroy
matroidality even when every slot has a nonempty local menu.  To use
Corollary 2.2 one must prove private composition or prove matroidality by
some other exact argument.

## 4. Projection of alternating bottom circuits to short sets

For an augmented bottom perfect matching `P`, write

\[
       S(P)=\{e\in E:e\text{ is matched to a dummy in }P\}. \tag{4.1}
\]

### Lemma 4.1 (dummy-free circuits are short-set loops)

Let \(P_0\triangle P_1\) contain an alternating circuit `C`.  If `C` has no
dummy vertex, then flipping `C` leaves `S(P)` unchanged.  More generally,
only hard slots incident with a changed dummy edge can enter or leave the
short set.

#### Proof

A hard slot is short exactly when its matched edge has a dummy endpoint.
On a dummy-free circuit, both alternating incident matching edges at every
hard slot have real bottom endpoints.  Flipping the circuit therefore
leaves every short indicator unchanged.  Outside the circuit the matching
is unchanged. \(\square\)

### Theorem 4.2 (the known Boolean actuators do not supply `M_sock`)

The movable-bottom hub `C6`, hub `C8`, and saturated `B5 C10` of
`MATH_THEOREM_A_BOTTOM_RELAY_INTERVAL_ACTUATOR_PROJECTION_AND_K17_C10_NOGO_20260802.md`
are dummy-free alternating circuits.  Consequently:

1. both phases have the same short set occurrencewise;
2. the circuits are loops under projection (0.5), although they are
   nontrivial circuits inside the perfect-matching fibre;
3. none supplies a unary ticket--short-slot edge `te` for (2.1); and
4. any product of these circuits still preserves the short set.

The one-aperture `B5 C8` does not change this conclusion.  Its aperture is
the omitted fifth interval/lower role of a saturated five-diamond resource
fibre.  Both displayed `C8` phases still occupy the same four hard suffix
slots by four real bottoms.  No dummy edge, and hence no selected short
slot, is present.

The planted `C10+C6` forest absorber is a private binary **phase** module
when complete footprints of different copies are disjoint.  It is not a
private short-slot ticket: its old and new modes do not bind a dummy to one
hard slot.  Its hypercube exchange theorem is therefore orthogonal to the
transversal matroid required in Corollary 2.2.

#### Proof

The three bottom-relay formulas are respectively cyclic matchings between
`r=3,4,5` real bottom tokens and `r` fixed hard suffix slots.  Apply Lemma
4.1.  The aperture statement follows from the explicit `C8` formula, and
the combined absorber's theorem contains no dummy/short declaration.
\(\square\)

For the frozen K17 suffix table, the exact native census (`246 C6`,
`16 C8`, `0 C10`) therefore counts internal assignment circuits, not
private socket tickets.  The zero `C10` count is a further frozen-table
obstruction to that particular combined absorber, but it is not needed for
the matroidal conclusion above.

## 5. The exact missing actuator

The weakest direct bridge from the Boolean circuit atlas to `M_sock` is a
**private dummy-bearing actuator bank**.  For each proposed edge `te` of
`Gamma` it must provide one compound mode with all of the following literal
properties.

1. It contains a bottom-matching alternating path/circuit which binds a
   dummy to `e`; thus `e`, rather than a resource-fibre aperture, is the
   selected short slot.
2. It closes its complete lower/co-middle/fixed-middle/upper interval deck;
   the co-middle equality of the Boolean relay theorem is only one of these
   required rows.
3. Its terminal state, history, cap, orientation, and guard record is
   independent of the other ticket choices, or is carried inside a
   ticket-private footprint.
4. Distinct ticket identities compose exactly as in Section 2.

A Boolean `C6/C8/C10` may occur inside such a compound actuator as an
internal resource-neutral rotor.  It cannot replace Item 1.  Attaching an
unproved shared-state socket after the rotor does not establish Item 3.

If every ticket has exactly one preplanted private short slot, `Gamma` is a
matching and `M_sock` has a unique basis.  This is a valid but rigid special
case.  A useful common-base theorem needs sufficiently rich fixed menus
`A_t` while retaining private composition.  Constructing those menus, or
proving that the actual shared-state socket family is matroidal by a
different representation, is the remaining gate.

## 6. Scope ledger

Proved here:

* the exact private-ticket hypotheses giving a transversal socket matroid;
* the explicit cotransversal--transversal common-base inequality;
* a minimal shared-state counterexample showing why local eligibility is
  insufficient;
* the kernel/loop status of every present movable-bottom Boolean actuator;
* the precise dummy-bearing compound bridge still required.

Not proved here:

* a rank-`1748` private ticket graph for K17;
* matroidality of the actual common-state socket system;
* a lift of common-base exchange paths to protected Boolean circuits;
* compatible topology, residence, upper shadows, reset, source, compiler,
  or word chronology.
