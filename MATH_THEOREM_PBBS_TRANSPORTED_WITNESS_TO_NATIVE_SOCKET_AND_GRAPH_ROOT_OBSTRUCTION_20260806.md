# Transported PBBS witnesses admit native sockets; graph roots do not

**Date:** 2026-08-06  
**Method:** literal occurrence coinstantiation, matching on the native
owner cycle, and the exact common-history transport maps; no computation or
search  
**Status:** unconditional final-word converter once two exact upstream
witnesses have already been materialized.  It applies to prospectively
decorated clean-`C6` and split-common-history PBBS moves.  It does not turn
an arbitrary graph-factor repair root into a source occurrence.  The global
PBBS problem is thereby reduced from terminal socket capacity to construction
of one resident antecedent carrying a two-coordinate exact witness atlas.

## 1. Fixed literal diagonal

Let `A=(A_i)_(i in Z_W)` be one cyclic nonzero source word with deadline
`d` and flat `q1` diagonal

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,\qquad
 P_i=T_i\cap T_{i+1},\qquad
 R_i=T_i\cup T_{i+1},                                  \tag{1.1}
\]

where the `T_i` are distinct rank-`r` owners and the `P_i` are distinct
rank-`r-1` lower turns.  Retain the native interval addresses

\[
 p_i=[i+1,i+d],\qquad o_i=[i,i+d],\qquad
 q_i=[i,i+d+1].                                        \tag{1.2}
\]

Thus index `i` carries the literal diamond

\[
 p_i-o_i-q_i,\qquad p_i-o_{i+1}-q_i.                  \tag{1.3}
\]

Let `B` be a labelled ticket bank.  Ticket `b` already has two exact
upstream interval occurrences

\[
 x_b^0,x_b^1\in {\cal C}(A),\qquad
 \operatorname {OR}_A(x_b^e)=X_b^e.                   \tag{1.4}
\]

Assume all `2|B|` upstream addresses are distinct.  The values may repeat;
the logical ticket and occurrence-coordinate labels remain part of the
record.

Call an occurrence address **noncoalescibly forbidden** when some already
fixed role uses its physical capacity in a way which is not merely the same
literal occurrence fact.  Ordinary facts

\[
 \operatorname {OR}(p_i)=P_i,\qquad
 \operatorname {OR}(o_i)=T_i,\qquad
 \operatorname {OR}(q_i)=R_i                         \tag{1.5}
\]

are coalescible with the corresponding native-diamond assertions and are
not forbidden for that reason alone.  Let `D` be a set of noncoalescibly
forbidden interval addresses.

## 2. Polynomial avoidance on the native cycle

### Lemma 2.1 (one address forbids at most two seams)

One fixed interval address belongs to at most two native footprints

\[
                         \Xi_i=\{p_i,o_i,o_{i+1},q_i\}. \tag{2.1}
\]

Consequently the number of owner-cycle edges whose footprints meet a set
`D` is at most `2|D|`.

#### Proof

The three address types have lengths `d,d+1,d+2`.  An address of length
`d` is at most one `p_i`, and an address of length `d+2` is at most one
`q_i`.  An address of length `d+1` is at most one owner `o_j`, and that
owner lies in exactly the two footprints `Xi_(j-1),Xi_j`.  Every other
length lies in no footprint.  This proves the claim. \(\square\)

### Theorem 2.2 (universal native-socket avoidance)

If

\[
                         2|B|+2|D|<\lfloor W/2\rfloor, \tag{2.2}
\]

then one may assign two native footprints

\[
                         \Xi_{i_0(b)},\Xi_{i_1(b)}      \tag{2.3}
\]

to every `b in B` so that all assigned footprints are pairwise disjoint and
avoid `D`.

In particular (2.2) holds for every polynomial-size ticket and forbidden
bank for all sufficiently large `r`.

#### Proof

Delete from the owner cycle every edge whose footprint meets `D`.  By
Lemma 2.1 at most `2|D|` edges are deleted.  A maximum matching of the
original `W`-cycle has size `floor(W/2)`.  Deleting one graph edge destroys
at most one member of that fixed matching, so the residual graph has a
matching of size at least

\[
                         \lfloor W/2\rfloor-2|D|.
\]

Under (2.2) choose `2|B|` members of this matching and biject them with the
labelled pairs `(b,e)`, `e in {0,1}`.  Vertex-disjoint owner-cycle edges
have disjoint complete footprints. \(\square\)

The estimate is deliberately insensitive to ticket values.  The exact
target identities remain upstream in (1.4); the native footprints carry
only a reversible occurrence-role code.

## 3. Direct-literal polarized conversion

### Definition 3.1 (passive native socket)

For `(b,e)`, a selected native footprint is **passive** when its socket
record

1. retains the upstream fact `(x_b^e,X_b^e)`;
2. records the logical ticket, occurrence coordinate, cut/role, and one
   polarity bit;
3. asserts on every native address only its existing fact in (1.5);
4. adds no membership, absence, endpoint, guard, chronology, or capacity
   condition to those facts; and
5. is not used to choose a further sink, topology edge, or regenerative
   continuation.

This is the terminal direct-literal semantics.  It is stronger than bare
containment and weaker than an active gain-to-sink gammoid route.

### Theorem 3.2 (transported-witness native-socket converter)

Assume (2.2), and suppose the ticket bank has the exact upstream witnesses
(1.4).  In a final literal OR-word certificate every ticket admits two
simultaneous passive native sockets, with no additional source position and
no additional occurrence capacity beyond the selected complete footprints.

Ordinary owner, lower-`q1`, and upper-`q1` uses of the selected native
addresses coinstantiate the sockets at zero additional capacity charge.

#### Proof

Choose the pairwise disjoint footprints by Theorem 2.2.  The target
identities are certified at the upstream addresses and are not replaced by
the comparable native values.  The ticket label and occurrence role fix the
polarity metadata.  By passivity, the socket assertion at each native
address is precisely the already true fact (1.5).  Repeating one literal
occurrence fact in a compound record does not create a second physical
demand.  Hence ordinary diagonal roles and socket roles coinstantiate.

Different tickets and coordinates have disjoint selected footprints, so
no two compound records share a new finite capacity.  Source labels on the
Hasse incidences in (1.3) are semantic edge labels, not node-priced source
positions.  Therefore the complete bank is simultaneous and uses the same
word `A`. \(\square\)

### Corollary 3.3 (no terminal-type gate on the final branch)

Under Theorem 3.2, the polarity field may be reconstructed from the ticket
and role or erased.  It is not an additional acceptance predicate in the
definition of a universal OR word.

If a socket carries an active gain, compensation, prescribed sink,
topology, guard, or child-continuation service, passivity fails and this
corollary does not apply.  The corresponding complete active route must
then be proved in the residual occurrence network.

## 4. PBBS moves to which the converter applies

### Theorem 4.1 (clean-`C6` transported witnesses)

Fix a prospectively decorated clean PBBS `C6` with its common-history
source blocks.  Let `Phi` be its exact occurrence bijection on every
strict-lower interval cell.  If an old ticket has two distinct exact
strict-lower witness cells `x_b^0,x_b^1`, then

\[
                         \Phi(x_b^0),\Phi(x_b^1)       \tag{4.1}
\]

are two distinct exact upstream witnesses after the move.  Any polynomial
bank of such tickets therefore satisfies the upstream premise of Theorem
3.2 once the decorated move lies in the final flat-`q1` word.

#### Proof

The clean-`C6` common-history theorem gives a bijection preserving interval
width, address multiplicity, and exact OR value on the complete strict-lower
deck.  It is injective on physical addresses.  Apply it to the two selected
cells of every ticket, then apply Theorem 3.2. \(\square\)

### Theorem 4.2 (split-common-history transported witnesses)

For a split role-zero PBBS block, every old strict-lower interval meets at
most one endpoint screen.  The exact split map sends it to the identical
relative address in one of the two half-blocks, preserving width and exact
OR value and using disjoint physical fragments.  Hence the conclusion of
Theorem 4.1 holds verbatim for every ticket whose two upstream witnesses
belonged to the old block.

These two applications are local and literal.  They do not assert that an
arbitrary factor-completion root had such witnesses before the move.

## 5. Sharp graph-root obstruction

### Proposition 5.1 (owner trace does not determine upstream tickets)

There is no construction which, from the owner trace or the owner/`q1`
factor alone, assigns the exact upstream witnesses required by Theorem 3.2.
Already at deadline one the nonzero words

\[
 A=(\{b\},\{a\},\{c\}),\qquad
 A'=(\{a,b\},\{a\},\{a,c\})                         \tag{5.1}
\]

have the same owner path

\[
                         DA=DA'=(\{a,b\},\{a,c\}),    \tag{5.2}
\]

but different strict-lower decks: `A` has singleton witnesses for `{b}`
and `{c}`, while `A'` has neither.

#### Proof

Both adjacent unions in (5.1) are (5.2).  In `A'`, every interval
containing `b` or `c` also contains `a`; the two singleton targets are
therefore absent. \(\square\)

Thus a completion component, a repair incidence, a Johnson route, or a
coded port is not yet a logical compiler ticket.  It becomes one only after
one source word and its exact interval atlas have been fixed.

There is a second PBBS-specific limitation.  The canonical one-sided
gap-potential section gives occurrence-labelled owner intersections at all
depths, but only the first `d` intersection depths have the automatic source
interval realization

\[
 \bigcap_{j=0}^{q}T_{i+j}
   =\bigcup_{h=q}^{d}P_{i+h},\qquad q\le d.           \tag{5.3}
\]

For `q>d`, no source interval follows from the owner-intersection label.
Moreover the one-sided section does not supply the phase-shifted second
coordinate.  Therefore it cannot, by itself, satisfy the two-witness premise
of Theorem 3.2 for the global compiler bank.

## 6. Revised exact PBBS frontier

For prospectively decorated local PBBS moves, terminal **socket supply** and
passive terminal **type acceptance** are no longer independent gates.  Once
their two exact strict-lower witnesses are transported, Theorem 3.2 supplies
as many private native sockets as any polynomial repair bank needs.

The global missing statement is instead:

> **Two-coordinate PBBS antecedent-atlas lemma.**  Construct one resident
> flat-`q1` PBBS source word in which every residual logical ticket has two
> distinct exact upstream interval witnesses, all local common-history maps
> agree with those witnesses, and the complementary ordinary target atlas
> remains exact.

On the final direct-literal branch this lemma, together with the already
proved upper-witness and topology rows, eliminates the typed terminal gate.
On a regenerative induction branch one must additionally prove that the
socket type is passive for the child continuation; otherwise the active
typed router remains necessary.

The distinction is load-bearing:

\[
 \boxed{
 \text{exact transported source witnesses}
 \Longrightarrow\text{private passive native sockets},
 }
\]

but

\[
 \boxed{
 \text{graph repair roots or coded ports alone}
 \not\Longrightarrow\text{source witnesses}.
 }
\]

## 7. Dependencies

The proof uses the literal native diamonds, occurrence-fact coalescence,
passive-type elimination, clean-`C6` common-history transport, split
common-history transport, and maximal-antecedent row identity established in
the corresponding August 3--6 theorem notes.
