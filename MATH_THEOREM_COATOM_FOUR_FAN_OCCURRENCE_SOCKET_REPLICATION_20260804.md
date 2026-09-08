# Four phase-common coatom fans give literal occurrence-socket replication

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional occurrence-level construction inside the canonical
mixed-coatom tensor.  It supplies a linear bank of distinct physical q1
terminal occurrences, despite repeated Boolean terminal values, and an
exact capacity-faithful fan routing.  External product typing, task-to-fan
binding, suffix acceptance, and regeneration remain open.

## 0. Setting

Use the fixed-active common-boundary atlas at owner rank `r` and depth
`delta>=2`.  Its ordered filler is

\[
 F=(f_0,\ldots,f_{n-1}),\qquad n=\delta+2,
\tag{0.1}
\]

and every active triple `V` is expanded into the coatom block

\[
 B(V)=(O_0(V),\ldots,O_{n-1}(V)),\qquad
 O_i(V)=K\cup V\cup(F\setminus\{f_i\}).
\tag{0.2}
\]

Put

\[
                         Z(V)=K\cup V\cup F.
\tag{0.3}
\]

The two active phases are

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

They agree at the four block positions

\[
                  \mathcal V_*=\{Iab,Cd,Ic,ab\}.
\tag{0.4}
\]

The same ordered filler (0.1) is used at every block in both phases.

## 1. One exact occurrence fan

For `0<=i<n-1`, define the lower turn

\[
 L_i(V)=O_i(V)\cap O_{i+1}(V)
       =Z(V)\setminus\{f_i,f_{i+1}\}.
\tag{1.1}
\]

Let

\[
 z_i(V)=(\text{block address }V, i; Z(V))
\tag{1.2}
\]

denote the physical q1 interval occurrence between the two consecutive
owner occurrences `O_i(V),O_(i+1)(V)`.

### Theorem 1.1 (coatom fan)

The block `B(V)` contains the alternating incidence path

\[
 O_0(V)-L_0(V)-O_1(V)-\cdots-L_{n-2}(V)-O_{n-1}(V).
\tag{1.3}
\]

Its `n-1=delta+1` q1 occurrences `z_i(V)` are pairwise distinct physical
capacities.  They all have the same Boolean value `Z(V)`, while the lower
values `L_i(V)` and owner values `O_i(V)` are respectively pairwise
distinct.

#### Proof

Equations (0.2) and (1.1) show that consecutive owners contain the displayed
rank-`r-1` lower set and differ by exchanging `f_i` and `f_(i+1)`.  Their
union is (0.3).  Distinct `i` give distinct deleted singleton or adjacent
pair, proving distinctness of the owner and lower values.  The occurrence
address in (1.2) contains `i`, so the q1 cells are physically distinct even
though their Boolean values agree.  \(\square\)

### Theorem 1.2 (exact capacity-faithful fan router)

For every turn introduce the two canonical routes

\[
 P_i^0:L_i(V)\longrightarrow O_i(V)\longrightarrow z_i(V),
 \qquad
 P_i^1:L_i(V)\longrightarrow O_{i+1}(V)\longrightarrow z_i(V).
\tag{1.4}
\]

A choice `epsilon=(epsilon_0,...,epsilon_(n-2))` gives pairwise
vertex-disjoint routes for all `n-1` claims if and only if `epsilon` is
nondecreasing.  Hence the fan has exactly `n` complete unit-capacity
routings, including the all-left and all-right routings.

#### Proof

Sources and occurrence-labelled sinks are already pairwise distinct.  An
internal owner `O_i(V)`, `1<=i<=n-2`, is used twice precisely when the left
turn chooses right and the right turn chooses left:

\[
                         \epsilon_{i-1}=1,
 \qquad \epsilon_i=0.
\]

Thus capacity faithfulness is equivalent to the absence of a `1 -> 0`
transition, namely to nondecreasing `epsilon`.  A nondecreasing binary word
of length `n-1` is determined by its cut and has exactly `n` possibilities.
Every such routing uses `n-1` distinct owners and leaves exactly one owner
unused.  \(\square\)

This is the path analogue of the two constant routings on a cyclic
Middle-Levels component.  The additional cut position is genuine endpoint
flexibility, not extra capacity at any one owner.

## 2. Four phase-common fans in one packet

### Theorem 2.1 (literal four-fan bank)

In both tensor phases, at the same physical addresses, the four blocks in
`mathcal V_*` supply

\[
                         4(\delta+1)
\tag{2.1}
\]

distinct lower-turn occurrences, the same number of distinct q1 terminal
occurrences, and four pairwise distinct terminal values

\[
                         \{Z(V):V\in\mathcal V_*\}.
\tag{2.2}
\]

The four fan incidence paths are pairwise vertex-disjoint.  Choosing any
one of the `n` routings independently in each fan gives
`4(delta+1)` pairwise vertex-disjoint native source--owner--q1 paths which
are pointwise present in both phases.

#### Proof

The active blocks in (0.4) occur at the same macro positions in `P` and
`Q`; their ordered filler expansions are therefore identical pointwise.
The four active triples are distinct.  The common contribution `K union F`
is disjoint from the active universe by the tensor hypotheses, so adjoining
it is injective on active triples and the four sets in (2.2) are distinct.

The mixed-coatom theorem proves that the complete owner word is simple and
that all adjacent lower seam colours are distinct.  Hence owners and lower
turns from different selected blocks do not collide.  Physical q1
occurrences in different blocks have different block addresses.  Theorem
1.2 supplies a disjoint routing inside each block, and the cross-block
distinctness makes their union disjoint.  Pointwise block identity makes
the entire union phase-common.  \(\square\)

### Corollary 2.2 (the shared-value unit cut is genuinely replicated)

For every selected `V`, the `delta+1` nodes `z_i(V)` are distinct unit
terminal capacities carrying the same Boolean value `Z(V)`.  Therefore a
common-cap model whose vertices are the literal occurrence nodes does not
have the one-unit `Z(V)` cut: its capacity at that displayed value inside
the fan is `delta+1`.

This corollary is invalid in a quotient which identifies all occurrences
having the same Boolean value.  Such a quotient must retain one capacity
`delta+1` at the value node, or it loses the literal word's physical
capacity.

### Corollary 2.3 (prepared polarized-socket bank)

Fix, for example, the all-left routing in every fan and call its
`4(delta+1)` routes `mathcal Q`.  Each route `q in mathcal Q` contains a
literal nested pair of distinct occurrences

\[
 r_q=(\text{owner occurrence }O_i(V)),\qquad v_q=z_i(V),
 \qquad \operatorname{val}(r_q)=O_i(V)\subset Z(V)
                         =\operatorname{val}(v_q),
\tag{2.3}
\]

and the pairs `(r_q,v_q)` are mutually capacity-disjoint.

Let `mathcal T` be any set of logical folded-ray tickets.  Join a ticket to
`q` when its exact upstream ray witnesses coexist with that route and the
fixed cap/phase/guard state accepts the polarized code on (2.3).  If this
acceptance graph has a matching saturating `mathcal T`, then the
deterministic polarized-socket theorem gives a simultaneous two-coordinate
linkage for all tickets in `mathcal T`.  No further native terminal
replication is required.

In particular, if `|mathcal T|=h` and every ticket accepts at least `h`
members of `mathcal Q`, such a matching exists.  Indeed, every nonempty
subfamily of at most `h` tickets has a neighbourhood containing the
neighbourhood of any one of its members and hence of size at least `h`.
Hall's theorem applies.  Consequently a fixed number of tasks is matchable
whenever each accepts a fixed positive fraction of the fan bank and
`delta` is sufficiently large.

The acceptance premise includes the exact upstream witnesses and product
type.  The corollary proves the physical nested-pair capacity row, not that
premise.

### Corollary 2.4 (phase-regenerative socket reservoir)

The identity map on physical addresses identifies the entire four-fan
occurrence complex in phase zero with the one in phase one.  Thus toggling
the mixed-coatom packet neither deletes nor relabels any fan source, owner,
q1 occurrence, or native route.

Consequently, any complete terminal predicate which depends only on these
phase-common occurrence records and a phase-normalized role field has the
same ticket-to-fan acceptance graph in both phases.  The fan bank is then a
phase-regenerative socket reservoir: it is still present after every toggle
of that packet.

This is persistence, not duplicated capacity.  A terminal matching may use
each occurrence only once, and persistence does not make the new whole word
an old phase for a different packet parameter.

## 3. Protected factor planting

The full alternating incidence path (1.3) has `2(delta+1)` edges and
maximum degree two.  The four-fan bank therefore has

\[
                         8(\delta+1)
\tag{3.1}
\]

incidence edges and maximum degree two.

### Corollary 3.1

In the `ML_m` specialization, if an incumbent protected bank `P_*` is
degree-compatible and

\[
                         |E(P_*)|+8(\delta+1)\le m-2,
\tag{3.2}
\]

then all four fans extend simultaneously to a spanning two-factor.  Every
displayed `z_i(V)` remains the literal q1 turn occurrence at its protected
lower vertex.

For `delta=Theta(sqrt(m))`, (3.2) holds for every fixed-size incumbent bank
in all sufficiently large dimensions.

#### Proof

Theorem 2.1 gives cross-fan vertex-disjointness, while (1.3) has maximum
degree two inside one fan.  Thus the union with `P_*` satisfies the degree
premise by hypothesis and the edge premise by (3.2).  Apply the small
protected-factor theorem.  At every protected lower turn its two incidences
exhaust factor degree two, so the completed factor's q1 occurrence is the
one in (1.2).  \(\square\)

### Corollary 3.2 (fixed packet bank)

Suppose `H` prospectively planted packets have pairwise vertex-disjoint
four-fan banks.  Their union contains `4H(delta+1)` occurrence-distinct
native routes and `8H(delta+1)` protected incidence edges.  Hence it embeds
with any degree-compatible incumbent whenever

\[
                         |E(P_*)|+8H(\delta+1)\le m-2.
\tag{3.3}
\]

For every fixed `H` and `delta=Theta(sqrt(m))`, this holds in all
sufficiently large dimensions.  The prospective fixed-bank theorem gives
one sufficient way to choose the packets without noncommon-token collisions;
its private-common-skeleton premise remains necessary here.

## 4. What multiplicity row this closes

The earlier single-wedge analysis was forced to treat the common Boolean
terminal `Z_*` as one unit until a physical replication theorem was given.
Theorem 2.1 supplies that theorem inside a fixed mixed-coatom packet:

\[
 \boxed{
  \text{four phase-common fans, each with }\delta+1
  \text{ occurrence-distinct native q1 sockets}.}
\]

In particular, any fixed number of native one-coordinate claims can be
assigned distinct source, owner, and terminal occurrences in this bank for
all sufficiently large `delta`, provided their external type/guard records
accept the chosen fan addresses.

## 5. Exact remaining boundary

This construction does not yet prove a product-typed regenerative packet.

1. **Task binding.**  It does not show that the canonical folded-ray
   obligations, or arbitrary Pascal tasks, satisfy the acceptance edges in
   Corollary 2.3.
2. **Terminal type.**  A native q1 socket does not by itself encode the two
   incomparable folded-C8 target values.  The polarized-socket theorem still
   requires exact upstream ray witnesses and accepted role polarity.
3. **Suffixes and compensation.**  No theorem here attaches private typed
   suffixes, proves survival after the fixed compensation linkage, or
   coinstantiates the transported background.
4. **Whole packet.**  Protecting the four fans does not plant the other
   eight active blocks and eleven screens.  U1--U4 remain properties of the
   whole `12delta+35` packet.
5. **Regeneration.**  The block bank is pointwise fixed by the one tensor
   toggle.  It survives that toggle, but no forward fresh packet atlas is
   exported after use; the fixed-incumbent fibre remains one.
6. **Opening and global topology.**  A subsequent linear opening must avoid
   the protected lower turns (or explicitly pay its exact occurrence loss),
   and arbitrary two-factor completion does not give the required connected
   upper-decorated carrier.

Thus literal terminal multiplicity is no longer missing on this prepared
face.  The hard rows are now the typed task-to-fan incidence and the
regenerative whole-host construction.

## 6. Dependencies

- `MATH_THEOREM_H2_COATOM_TENSOR_FIXED_ACTIVE_MENU_AND_HOST_QUANTIFIER_20260801.md`
- `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`
- `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md`
- `MATH_THEOREM_MIDDLE_LEVELS_TURN_DIAMOND_CAPACITY_ROUTER_20260804.md`
- `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
