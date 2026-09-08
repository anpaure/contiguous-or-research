# Phase-switched companion matchings suffice for full row control

## Status

The state-closed companion hypothesis in
`MATH_THEOREM_INVERSE_PAIR_COMPANION_GRAPH_GROUP_AND_Q1_SQUARE_TRANSITIVITY_20260806.md`
is stronger than the abstract group argument needs.  This note gives the
proof-safe weakening.

Companion edges need not coexist in one factor.  They may occur in finitely
many guarded phase fibres, provided that the transports to those fibres are
reversible and reusable after every preceding closed excursion.  If the
union of the transported matchings is connected, the resulting closed
phase excursions generate the full product of perfect row-order groups.

Two qualifications are load-bearing.

1. A phase is a complete occurrence-labelled guarded fibre, not just an
   unlabelled factor or an owner set.  All provider, cap, and inverse-
   transport data not designated as controlled row frames belong to the
   phase state.
2. Closed control excursions have zero net protected current.  Full row
   control therefore implies a dynamic q1 square **atlas** only after a
   marked literal inverse move is exposed.  It does not by itself imply a
   nonzero net q1 current or a positive coverdown.

This is an abstract physical-interface theorem.  It does not construct the
required guarded phases.

## 1. Guarded phase fibres and closed excursions

Let `G` be a perfect group and let `V` be a finite set of tracked rows.  A
**guarded phase fibre** `P_alpha` is a family of complete occurrence-
labelled factor states with the same protected external interface.  The
tracked row-order frames are the controlled coordinates; every other
named occurrence, provider ticket, cap resource, and inverse-transport
guard is part of the phase datum.

Fix a reference fibre `P_0`.  For each phase `alpha`, assume there is a
reversible guarded transport

\[
       T_\alpha:{\cal P}_0\longrightarrow {\cal P}_\alpha .       \tag{1.1}
\]

Here (1.1) means a bijection of the relevant fibres, not merely one path
between two initial states.  Both `T_alpha` and `T_alpha^{-1}` must remain
literal and guard-safe after every local loop used below.  The transport
may permute tracked row names or conjugate their coordinate frames.  Fix
those identifications once and use them to identify every controlled
action with the common product `G^V`.

Suppose phase `alpha` exposes a matching `M_alpha` on the common abstract
set `V`.  For every edge `uv in M_alpha` and every `g in G`, assume there
is a uniformly legal guarded loop

\[
 L_{\alpha,uv}(g):{\cal P}_\alpha\longrightarrow {\cal P}_\alpha
                                                               \tag{1.2}
\]

which preserves the complete external interface and whose action after
transport to the reference frame is

\[
                         D_{uv}(g).                    \tag{1.3}
\]

With the usual right-to-left convention for composition, the corresponding
closed excursion based in the reference fibre is

\[
 E_{\alpha,uv}(g)
   =T_\alpha^{-1}\circ L_{\alpha,uv}(g)\circ T_\alpha .          \tag{1.4}
\]

The opposite order `T_alpha L T_alpha^{-1}` is type-incorrect when
`T_alpha:P_0 -> P_alpha`.  Condition (1.3) already includes any row-name
permutation or group automorphism induced by the transport.

The fibre formulation is essential.  It says that the excursion (1.4) may
be followed by an excursion through another phase: after the first one,
all transports and inverse transports required for the next word are still
literal.  Time-zero availability at one representative state is not
enough.

## 2. Generation theorem

### Theorem 2.1 (connected union of phase matchings)

Let

\[
                         \Gamma=\bigcup_\alpha M_\alpha .        \tag{2.1}
\]

After the fixed common row/frame identifications, assume `Gamma` is
connected and has at least three vertices.  Then the closed excursions
(1.4) generate

\[
                         G^V.                           \tag{2.2}
\]

#### Proof

By (1.3)--(1.4), the reference action of the available excursion on an
edge `uv` is exactly `D_uv(g)`.  Hence the excursions provide every
edge-diagonal generator on the union graph `Gamma`, even though the edges
need not coexist physically.

Choose a length-two path `u-v-w` in `Gamma`.  The commutator of
`D_uv(g)` and `D_vw(h)` is supported only at `v`, where it acts by
`[g,h]` (up to the harmless inverse convention).  Since `G` is perfect,
these commutators generate an isolated copy of every element of `G` at
`v`.  Multiplying an edge-diagonal action by the inverse isolated action
at one endpoint propagates isolated copies along a spanning tree.  Thus
every coordinate copy of `G` is generated independently, giving (2.2).
\(\square\)

### Corollary 2.2 (phase-switched row-role control)

Take `G=A_(2m+1)`.  If the phase loops realize the separated-double-swap
generators needed to obtain every element of `G` on each exposed matching
edge, then the reference phase orbit realizes every injective assignment
of the `m+1` named roles of a q1 square on every tracked row.

#### Proof

Theorem 2.1 gives independent `A_(2m+1)` actions.  The alternating group is
transitive on injective assignments of at most `2m-1` named roles: if a
chosen realizing permutation is odd, transpose two unnamed positions.
A q1 square names `m+1<=2m-1` roles. \(\square\)

### Corollary 2.3 (marked q1 square atlas; extra hypothesis)

Assume, in addition, the following marked-generator condition.  After any
closed control word used to arrange the roles, one can expose one literal
native inverse-pair generator occurrence, and its occurrence carries the
standard four-term q1 current on the labels currently occupying those
roles.  Then the **dynamic occurrence atlas** contains every q1 square and
its signed span is the complete coordinate-balanced lattice.

This conclusion concerns the marked local occurrence.  To deduce a net
factor difference, a compiler repair, or a positive coverdown, one needs
one further statement: the marked current survives the subsequent guard
closure (or is absorbed with a priced residual).  The zero-current closed
excursions of Theorem 2.1 alone cannot supply that conclusion.

#### Proof

Use Corollary 2.2 to place the labels of any prescribed square into the
roles of the marked generator.  Its literal occurrence emits that square.
The integer square-generation theorem then says that all such squares
span the coordinate-balanced lattice. \(\square\)

## 3. Relation to the Tamari and Dyck-context switches

The port-restored four-row associator fixes its four endpoint pairs while
changing their internal exchange-token orders.  Abstractly it has the
right form for a transport between phase fibres, but that assertion is
strictly weaker than the hypotheses above.  The base packet audited in
`MATH_THEOREM_TAMARI_BASE_COMPANION_EDGE_PRESERVATION_20260806.md`
preserves its sole internal companion edge `A--L` and only transports that
edge to a different inverse slot.  It therefore supplies a slot-changing
candidate, not a connected union of companion matchings.

Likewise, the aligned-Dyck-context switch of
`MATH_ATTACK_LANE_F_MSW_CHUNG_FELLER_LAYERED_PHASE_SWITCH_20260726.md`,
Theorem 5.1, is a reversible exact transport at the owner and immediate-
upper-palette level: its two cuts cancel in aggregate and its endpoints
are fixed.  A Dyck-suffix-lifted sequence of four such switches can be
used as a `T_alpha` only after one verifies, for the entire sequence,

1. preservation of the complete all-width/provider/cap interface;
2. literal inverse transport after the local companion loop;
3. a genuinely different transported companion matching; and
4. the marked-generator condition of Corollary 2.3 if q1 current, rather
   than row control alone, is claimed.

The common-context theorem proves none of these four rows automatically.
It proves a candidate phase transport, not the phase-switched companion
lemma itself.

The all-dimensional tensor in
`MATH_THEOREM_TENSORED_FOUR_ROW_TAMARI_WREATH_TRANSPORT_20260806.md`
preserves central shores and endpoints and is therefore another valid
candidate transport.  Its present audited companion graph is still the
single edge `A--L`.  A valid application of Theorem 2.1 must add at least
one of:

1. another associator whose transported row identification creates a
   genuinely different companion edge;
2. external helper rows which are companions of `C` or `D` in another
   phase; or
3. a larger exact trade which switches the companion graph itself.

There is no requirement that all companion edges coexist in one phase.
There is, however, an unavoidable requirement that their guarded closed
excursions coexist **serially** in one reference fibre.

## 4. Exact remaining interface

The group-theoretic statement is now proof-safe:

\[
 \boxed{
 \begin{array}{c}
 \text{reusable reversible guarded phase transports}\\
 +\text{ connected union of transported companion matchings}\\
 +\text{ every edge supplies all diagonal generators}
 \end{array}
 \Longrightarrow G^V.}
\]

For q1 current, append the marked-generator hypothesis.  The prospective
`S_8` orbit in
`MATH_THEOREM_TAMARI_TENSOR_COMPLETE_CHORD_RAIL_CURRENT_20260806.md`
cancels the associator chord current algebraically in constant size, but
it does not yet construct these reusable literal phase transports or the
marked closing absorber.
