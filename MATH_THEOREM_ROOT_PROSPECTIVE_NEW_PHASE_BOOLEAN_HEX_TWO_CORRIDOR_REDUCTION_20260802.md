# Prospective new-phase Boolean hex and the exact two-corridor reduction

**Date:** 2026-08-02  
**Lane:** root synthesis of the twisted-`C6` pump and augmented-corridor lanes  
**Status:** unconditional local/resource/topology reduction.  Existence of the
residual guarded two-corridor completion is not claimed.

## 0. Verdict

The functional-partner codegree and three-component-escape conditions are
needed only when one first completes an **old-phase** factor and then searches
inside it for a switchable Boolean hex.  They are not intrinsic to a
prospective construction.

Choose one literal Boolean hex before the ambient factor is completed and
prescribe its three **new-phase** edges directly.  The old phase is retained
only as a resource and voltage witness.  Because the two phases have identical
typed owner, lower, immediate-upper, tail, and head multisets, fixing the new
phase leaves exactly the same residual degree and immediate-palette demands as
fixing the old phase.

After opening the distinguished pump edge, the required one-cycle topology is
equivalent to two directed residual corridors with fixed endpoints.  Thus the
post-hoc rows

\[
 \kappa_e>0,\qquad \text{positive component escape}
\]

are replaced by one prospective row:

> complete a literal, resource-faithful, history-compatible two-root/two-sink
> corridor around three prescribed new-phase edges.

This is a strict reduction, not a solution of that corridor row.

The reduction is stated for one **physical** pump edge and is intentionally
non-equivariant.  If a construction insists on selecting an entire free
rotation orbit of hexes, deleting the pump-edge orbit creates several pump
fragments and the two-corridor normal form must be replaced by the corresponding
multi-corridor system.  No orbit-closed conclusion is claimed here.

## 1. The two phases

Use the notation of the twisted-`C6` partner theorem.  Let

\[
 e:E\to F
\]

be the selected nonprivate pump edge, and for one prospectively chosen pair
`(b,c)` let the other two old edges be

\[
 o_1:A_b\to B_{bc},\qquad o_2:C_{bc}\to D_c.
\]

The opposite Boolean-hex phase is

\[
 n_1:A_b\to F,\qquad
 n_2:C_{bc}\to B_{bc},\qquad
 n_3:E\to D_c.                                      \tag{1.1}
\]

All six owners are distinct on the authenticated Cartesian fan.  The two
three-edge phases have the same tail and head multisets,

\[
 \{A_b,C_{bc},E\},\qquad \{B_{bc},D_c,F\},           \tag{1.2}
\]

and the same lower and immediate-upper colour multisets.  Consequently their
complete **central** typed resource vectors agree:

\[
             \mathbf r(e,o_1,o_2)=\mathbf r(n_1,n_2,n_3).       \tag{1.3}
\]

Here `r` records owner out-capacity, owner in-capacity, immediate lower and
upper colours, and every occurrence-labelled tail/head token represented in
the prospective host model.  It does not identify the three old seam
occurrences with the three new seam occurrences.  Directed-history states,
edge-private tokens, and any seam-specific sidecar resource are outside
`r` and must be tested on the prescribed new phase itself.  In the
authenticated Cartesian hex the selected pump edge is nonprivate; this does
not make its directed history automatic.

## 2. Exact residual-demand invariance

### Theorem 2.1 (direct new-phase planting)

Let `b` be any integral target vector for the typed resources in (1.3), and
let `H` be one explicitly common remaining literal host, for example after
deleting the union of all old-phase-specific and new-phase-specific forbidden
options.  After fixing either the old phase or
the new phase, the residual resource equation on `H` is the same:

\[
 \sum_{f\in H}x_f\mathbf r(f)
   =b-\mathbf r(e,o_1,o_2)
   =b-\mathbf r(n_1,n_2,n_3).                         \tag{2.1}
\]

In particular, every residual Ore--Ryser, Hall, exact-palette, and
capacity-faithful state-table condition formulated on this same declared host
and depending only on the residual vector is unchanged.

#### Proof

Equation (1.3) makes the two right sides in (2.1) identical.  Every listed
residual condition is a property of the same host with the same residual
integer demands.  \(\square\)

### Scope

Resource-vector equality alone does not prove that two phase-conditioned
literal option hosts are identical: private-edge exclusions and history guards
can differ.  The common-host hypothesis in Theorem 2.1 is therefore
load-bearing.  It is harmless for the prospective route, which uses only the
new-phase-conditioned host.

The theorem does not identify the topology or chronology of a completion.
Nor does it make directed-history guards automatic: those depend on the paths
adjacent to the three prescribed new seams.  They must be included in the
literal corridor state table.  The point is that there is no additional
partner-overlap question once `(b,c)` and (1.1) are fixed prospectively.

## 3. Exact topology normal form

Delete `e=E->F` from the developed pump component.  Denote the resulting
directed pump path by

\[
                       P_3:F\leadsto E.                \tag{3.1}
\]

The new phase (1.1) can be inserted into a spanning directed cycle precisely
through two residual paths of the following orientation:

\[
             Q_1:D_c\leadsto C_{bc},\qquad
             Q_2:B_{bc}\leadsto A_b.                 \tag{3.2}
\]

### Theorem 3.1 (two-corridor equivalence)

Assume the interiors of `P_3,Q_1,Q_2` are pairwise disjoint and together with
the six displayed endpoint owners cover every owner exactly once.  Then

\[
 A_b\xrightarrow{n_1}F
 \xrightarrow{P_3}E
 \xrightarrow{n_3}D_c
 \xrightarrow{Q_1}C_{bc}
 \xrightarrow{n_2}B_{bc}
 \xrightarrow{Q_2}A_b                              \tag{3.3}
\]

is one directed spanning cycle.

Conversely, every directed spanning cycle containing `P_3` and all three
new-phase edges decomposes uniquely, after deleting those fixed pieces, into
the two paths in (3.2).

#### Proof

Concatenation in (3.3) is endpoint-compatible, closes at `A_b`, and by the
disjoint-cover hypothesis visits each owner once.  Hence it is a spanning
cycle.

Conversely start at `A_b`.  The prescribed outgoing edge forces `A_b->F`,
then the fixed pump path forces traversal through `E`, and `E->D_c` is forced.
In a single spanning cycle the next prescribed new edge encountered must be
`C_bc->B_bc`; otherwise the walk would close through `A_b` before using every
prescribed edge.  The intervening segment is `Q_1`.  The remaining segment
from `B_bc` back to `A_b` is `Q_2`.  Unique successor and predecessor at every
owner make the decomposition unique.  \(\square\)

### Corollary 3.2 (ordered Hall formulation)

Partition the residual fragments into two blocks.  Put root `D_c` and sink
`C_bc` in the first block, and root `B_bc` and sink `A_b` in the second.
Fix a forward order in each block and retain only within-block joins
consistent with its order.  Delete the two sink tails and the two root heads.
A capacity-faithful perfect matching in the resulting block-diagonal balanced
split table is equivalent to the two paths (3.2).  Thus its exact feasibility
condition is ordinary Hall on that augmented table, together with every
explicit resource and history state encoded in the table.

The partition and the two forward orders are sufficient rather than
necessary data.  Minimizing over all such partitions/orders is exhaustive,
because any valid pair `(Q_1,Q_2)` supplies its own two vertex blocks and
orders.  Without the block roles, a perfect split-table matching may swap the
two sinks or contain extra directed cycles and is not by itself a proof of
(3.2).

## 4. Voltage is preserved without an old-phase factor

Assign literal lift phases `lambda(V)` to the six owner occurrences.  Every
direct seam has displacement

\[
                         \delta(X,Y)=\lambda(Y)-\lambda(X).
\]

The identical tail/head multisets give the Boolean-hex identity

\[
 \delta(A_b,F)+\delta(C_{bc},B_{bc})+\delta(E,D_c)
 =\delta(A_b,B_{bc})+\delta(C_{bc},D_c)+\delta(E,F).   \tag{4.1}
\]

This is an identity of the prospective occurrence labels; it does not require
the three old edges to belong to a completed factor.  Therefore, if the
conceptual old pump closure `P_3+(E->F)` has unit voltage and the two
conceptual partner closures

\[
 Q_1+(C_{bc}\to D_c),\qquad Q_2+(A_b\to B_{bc})       \tag{4.2}
\]

have total integer voltage zero, the direct new-phase cycle has that same
unit total voltage.  Indeed its voltage equals the sum of these three
conceptual old closure voltages by (4.1).  No old-phase factor needs to be
physically realized, but the two partner-closure charges still depend on the
chosen corridors and are not certified by the local hex alone.

For one finite `Z_n` cover, a total voltage coprime to `n` (in particular
`1 mod n`) proves a single lifted cycle.  The stronger common **integer** lift
is needed only when zero background charge is carried as an exact regenerative
invariant rather than merely as a residue modulo `n`.

## 5. History and protected-resource interface

Direct new-phase planting removes the aggregate history-loss question over a
post-hoc candidate family.  For one chosen `(b,c)`, the exact six positive and
negative seam tests are simply finite constraints on the collars of
`P_3,Q_1,Q_2`.  A prospective construction may choose those collars jointly.

Likewise, a collision with a common anchor no longer deletes an entire
candidate atlas: the one chosen hex and its full `O(d)` collar are placed in
the protected bank before residual completion.  The residual theorem must
avoid that bank literally; raw aggregate degree is not a substitute.

## 6. Consequence for the general construction programme

For the prospective route, it is unnecessary to prove any of the following:

1. a linear mutual functional codegree in an already completed owner factor;
2. a positive fraction of partner pairs lying on three suitable old cycles;
3. an `O(d)` union bound over post-hoc option-dependent collars.

It is sufficient to prove one combined completion statement.

### Prospective guarded two-corridor lemma

For all sufficiently large odd hosts, one can choose a literal Boolean hex,
open the unit-voltage pump path, retain the prescribed new phase (1.1), and
complete the residual owner/palette demands by paths (3.2) such that

* the split table is capacity-faithful;
* all six directed-history seam tests pass;
* the background integer charge is zero;
* the protected upper/deep-shadow tickets survive; and
* the resulting lower source/common-cap interface has bounded regenerative
  defect.

Together with the already proved pump and local-ticket identities, this lemma
would close the functional-partner and component-fusion part of the
same-parity construction.

## 7. Remaining gap

No theorem currently proves the prospective guarded two-corridor lemma.
The exact unresolved object is a two-root/two-sink version of the residual
Ore--Ryser/augmented-Hall completion with a fixed `O(d)` occurrence bank and
the charge/upper/compiler states carried in the same literal table.

The reduction is nonetheless useful: it shows that positive post-hoc partner
codegree and component escape are artefacts of an avoidable order of
quantifiers.  A direct final-phase construction has one fewer correlated
existence layer.

## 8. Exact augmented-Hall damage row for the two corridors

The two-corridor gate has a literal cut certificate.  Fix one prospective
hex `(b,c)`, the protected pump path `P_3`, a partition and two orders as in
Corollary 3.2, and all endpoint state roles.  The three prescribed new seams
must already avoid every private token; their central demand (1.3), and the
complete demand of `P_3` and every other protected ticket, is subtracted
before the residual table is formed.

Let

\[
 B_0^{(2)}=(L_0^{(2)},R_0^{(2)},E_0^{(2)})            \tag{8.1}
\]

be the raw block-diagonal forward split table.  It has one tail role for
every nonsink residual fragment and one head role for every nonroot residual
fragment.  Parallel literal joins remain distinct.  Filter an option when
either endpoint-history automaton rejects it or it uses a zero-residual
join/port occurrence.  Positive-capacity shared resources must be encoded by
an exact state gadget or retained in the full master.  Write `F_a` for the
forbidden options deleted by this filtering for the fixed candidate `a`.

For `S subseteq L_0^(2)`, define

\[
\begin{aligned}
 D_a^{(2)}(S)
   &=\{v\in N_{0,a}^{(2)}(S):E_{0,a}^{(2)}(S,v)\subseteq F_a\},\\
 \kappa_a^{(2)}(S)
   &=|N_{0,a}^{(2)}(S)|-|S|.                          \tag{8.2}
\end{aligned}
\]

### Theorem 8.1 (two-root/two-sink Hall-damage identity)

On a fixed capacity-faithful state expansion, the two required corridors
exist with every encoded occurrence and endpoint-history row if and only if

\[
          |D_a^{(2)}(S)|\le \kappa_a^{(2)}(S)
          \qquad(S\subseteq L_0^{(2)}).               \tag{8.3}
\]

If the residual background charge described in Section 4 is
matching-independent, its
integer value is checked once.  Otherwise (8.3) is necessary and sufficient
only for the uncharged encoded corridors; the zero-charge row must be encoded
in the expanded state or solved jointly.

#### Proof

For every shore,

\[
 N_{B_a^{(2)}}(S)=N_{0,a}^{(2)}(S)-D_a^{(2)}(S).      \tag{8.4}
\]

Hall's theorem is therefore exactly (8.3).  A perfect matching restricts in
each forward block to one directed spanning path, giving `Q_1,Q_2`.
Theorem 3.1 then gives one final cycle.  Conversely any such corridor pair
gives the perfect matching and hence (8.3).  Capacity faithfulness supplies
the encoded resource rows; Section 4 gives the charge qualification.
\(\square\)

Let `A_2` be any nonempty declared family of pump-disjoint, capacity-faithful and
charge-faithful literal candidates, including the hex, two-block partition,
orders, endpoint states, and protected bank.  Put

\[
 \Delta_{\rm hex}
   =\min_{a\in A_2}\ \max_{S\subseteq L_a^{(2)}}
       \bigl(|D_a^{(2)}(S)|-\kappa_a^{(2)}(S)\bigr).  \tag{8.5}
\]

The empty shore makes the inner maximum nonnegative.  Hence a prospective
new-phase completion within `A_2` exists exactly when

\[
                         \Delta_{\rm hex}=0.          \tag{8.6}
\]

This is an unrestricted equivalence only after `A_2` is proved exhaustive:
it must contain the literal partition, orders, and state restriction induced
by every valid physical corridor pair.  The weighted destroyed-head bounds
of the pump-first augmented-table theorem apply verbatim with `B_0^(2)`.

### Proposition 8.2 (the cyclic-order row cannot be dropped)

Untyped Hall on a table with two roots and two sinks is insufficient.  Suppose
the only residual paths pair

\[
                  D_c\leadsto A_b,\qquad
                  B_{bc}\leadsto C_{bc}.             \tag{8.7}
\]

The corresponding two-by-two split table has a perfect matching.  But with
the fixed new seams, the first path closes

\[
 A_b\to F\leadsto E\to D_c\leadsto A_b,
\]

while the second closes `C_bc->B_bc leadsto C_bc`.  The result is two cycles,
not (3.3).  In the correct role-separated table these crossed options are
absent and Hall fails.  Thus the two designated endpoint pairings, or an
equivalent role-state expansion, are logically necessary.

There is an independent history obstruction: the six directed seam tests
may be marginally feasible under different endpoint states but have no common
state assignment.  Such a candidate is absent from `A_2`; an unexpanded
tail/head matching cannot certify it.  Direct new-phase planting removes the
old-factor component-escape gate, but it does not remove this common-history
or zero-charge correlation.
