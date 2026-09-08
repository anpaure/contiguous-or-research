# Automatic protected-turn occurrence lift and regenerative owner area

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional support-level occurrence theorem and
nonmonotone layer-projection theorem, followed by an exact sufficient
regenerative occurrence invariant.  The current Pascal/common-cap
construction does not yet prove the owner-area or selection-stable typing
premises.

## 0. Main conclusion

There are two separate questions in the current cap gate.

1. Does a selected protected wedge become a literal source--owner--q1
   occurrence path after the Middle-Levels factor is completed?
2. How much of the prospective wedge atlas can a frozen common-cap
   background destroy?

The first question has an unconditional positive answer.  If a selected
wedge bank is extended to a factor, the selected edges themselves force the
required turn occurrences and both literal containments.  No full
prospective occurrence atlas has to be materialized simultaneously.

For the second question, no per-path rank monotonicity is needed.  If the
frozen background has (f) distinct rank-(m) owner values in its Boolean
owner--q1 incidence footprint, then all q1 terminal values adjacent to that
footprint number at most

\[
                         (m-1)f.
\tag{0.1}
\]

Thus an (O(m)) owner footprint automatically propagates to an
(O(m^2)) q1-terminal footprint, regardless of how the background paths
snake inside those two layers.

Combined with the audited two-layer wedge theorem, this gives a particularly
small regenerative target: a selection-stable typed turn atlas, linear
distinct owner area, explicitly priced hidden holes, and nonaccumulation.

## 1. Automatic occurrence lift of a protected wedge bank

Fix distinct lower turns

\[
 L_1,\ldots,L_p\in{[2m-1]\choose m-1}.
\]

At (L_i), choose a full wedge

\[
 w_i=(L_i;\{a_i,b_i\})
\]

with owners and q1 terminal

\[
 U_i^0=L_i\cup\{a_i\},\qquad
 U_i^1=L_i\cup\{b_i\},\qquad
 Z_i=L_i\cup\{a_i,b_i\}.
\tag{1.1}
\]

Assume all (2p) owner values and all (p) terminal values are pairwise
distinct.  Let (M) be the (2p)-edge incidence bank

\[
 M=\{L_iU_i^0,L_iU_i^1:1\le i\le p\}.
\]

Assume an incumbent protected bank (P_*) is degree-compatible with (M)
and

\[
                         |P_*|+2p\le m-2.
\tag{1.2}
\]

The small protected-factor theorem extends (P_*\cup M) to a spanning
two-factor (Phi) of the Middle-Levels graph.

### Theorem 1.1 (selected paths materialize automatically)

In every such completion (Phi), the turn at (L_i) has exactly the two
owners (U_i^0,U_i^1), and its canonical q1 occurrence has value (Z_i).
Consequently the serialized occurrence complex contains the two literal
paths

\[
 x_i\longrightarrow u_i^0\longrightarrow z_i,
 \qquad
 x_i\longrightarrow u_i^1\longrightarrow z_i.
\tag{1.3}
\]

The selected turns are pairwise nonconsecutive in every factor component.
Hence choosing either one of the two paths at each selected turn gives
pairwise vertex-disjoint paths in the serialized source/owner/q1 complex.

#### Proof

The two protected incidences exhaust the degree of (L_i) in the factor.
Suppressing the lower shore therefore makes (U_i^0,L_i,U_i^1) the
selected turn.  Its q1 value is their union, which is exactly (Z_i).
The protected-factor occurrence theorem supplies the source and owner
addresses and the first literal containment; the canonical turn-diamond
construction supplies the second containment and the q1 address.  This
proves (1.3).

Two consecutive lower turns share their intervening owner.  All selected
owner values are distinct, so no two selected turns are consecutive.  The
sources are distinct, any chosen owner belongs to the globally distinct
(2p)-set, and the q1 occurrences have distinct values (Z_i).  Therefore
the chosen paths are pairwise disjoint.  □

### Exact boundary

Theorem 1.1 proves occurrence **existence and containment labels** in the
serialized factor.  It does not prove that those nodes survive a frozen
background, that their arcs have the required phase/type in one common-cap
state, or that (z_i) is an unused legal sink.  Those are activation
predicates on already materialized local paths, not missing occurrence
objects.

The cycle-aligned wedge-linkage theorem strengthens this conclusion: the
selected owner-to-q1 edge can be chosen to be exactly one edge of the raw
Boolean full-port linkage.  Thus Boolean linkage, wedge selection and q1
occurrence materialization can be correlated before the cap-survival test;
the remaining issue is genuinely typed survival/regeneration.

## 2. Nonmonotone owner-to-terminal footprint propagation

Let

\[
 \mathcal U={ [2m-1]\choose m},
 \qquad
 \mathcal Z={ [2m-1]\choose m+1}
\]

and let (B) be their Boolean containment graph.  Every (U\in\mathcal U)
has exactly (m-1) neighbours in the rank-(m+1) shore.

Let Q be any physical background subnetwork.  Project its
rank-(m) and rank-((m+1)) occurrence nodes to Boolean values and call the
resulting sets

\[
 D_{\mathcal U},\qquad D_{\mathcal Z}.
\]

Let (E_{\mathcal Z}\subseteq D_{\mathcal Z}) consist of the terminal
values for which no occurrence in Q is joined inside Q by a Boolean
containment edge to an occurrence whose value
lies in (D_{\mathcal U}).  These are the terminal-only exceptions.

### Theorem 2.1 (owner-area propagation)

Writing

\[
 f=|D_{\mathcal U}|,\qquad e=|E_{\mathcal Z}|,
\]

one has

\[
 \boxed{
 |D_{\mathcal Z}|\le(m-1)f+e.
 }
\tag{2.1}
\]

No connectedness, disjointness, orientation, acyclicity, or rank
monotonicity of Q is required.

#### Proof

Every nonexceptional (Z\in D_{\mathcal Z}\setminus E_{\mathcal Z}) is a
rank-((m+1)) superset of at least one (U\in D_{\mathcal U}).  Hence

\[
 D_{\mathcal Z}\setminus E_{\mathcal Z}
 \subseteq
 \bigcup_{U\in D_{\mathcal U}}N_B(U).
\]

Every neighbourhood on the right has size (m-1).  The union bound gives
(2.1).  Equal Boolean values at different physical addresses only decrease
the projection size.  □

### Corollary 2.2 (arbitrary path banks)

If Q is a union of alternating owner--terminal paths and every
terminal occurrence lies on an incidence edge of its path, then (e=0).
Thus

\[
                         |D_{\mathcal Z}|\le(m-1)|D_{\mathcal U}|.
\tag{2.2}
\]

Singleton terminal paths, remote non-Boolean tails, and terminal resources
introduced without an adjacent owner occurrence must be counted in (e).

This is exactly where the earlier snake obstruction stops being relevant:
a path may visit its owner values in any order and may revisit ranks, but
only the union of its distinct owner values enters (2.2).

## 3. The still weaker task-incidence energy invariant

A global footprint is not actually necessary.  For each source (L_i),
let (R_i) be the set of owner-side coordinates unavailable in one fixed,
selection-stable cap state.  Let (S_i) be its unavailable q1-terminal
pairs, and let (H_i) be any additional fully priced hidden wedge holes.
Assume every inactive wedge belongs to

\[
 {R_i\choose2}\cup S_i\cup H_i.
\tag{3.1}
\]

Put

\[
 r_i=|R_i|,\qquad t_i=|S_i|+|H_i|,
\]

and define the two aggregate energies

\[
                         I=\sum_i r_i,
 \qquad                  J=\sum_i t_i.
\tag{3.2}
\]

Let

\[
 T={m-p+1\choose2}.
\]

For any integer (R) with (1\le R\le m) and

\[
 S_R=T-{R-1\choose2}>0,
\]

define

\[
 C_R(I,J)=
 \left\lfloor{I\over R}\right\rfloor+
 \left\lfloor{J\over S_R}\right\rfloor.
\tag{3.3}
\]

### Theorem 3.1 (layer-energy activation)

All but at most

\[
                         \boxed{\min_R C_R(I,J)}
\tag{3.4}
\]

sources have active wedge menus larger than the exact simultaneous packing
threshold (B_{p-1}(m)).  The retained sources therefore admit a globally
owner/terminal-distinct wedge bank.  Under (1.2), that bank extends to a
factor, and Theorem 1.1 gives its literal private occurrence paths.

#### Proof

At source (i), (3.1) leaves at least

\[
 {m\choose2}-{r_i\choose2}-t_i
\]

active wedges.  A source can fail the strict (B_{p-1}) row only if

\[
                         {r_i\choose2}+t_i\ge T.
\tag{3.5}
\]

If (r_i<R), (3.5) forces (t_i\ge S_R).  Thus every failing source lies
in

\[
 \{i:r_i\ge R\}\cup\{i:t_i\ge S_R\}.
\]

The two aggregate sums (3.2) and Markov counting give (3.3)--(3.4).
The exact active-wedge packing theorem and Theorem 1.1 finish the proof.
□

### Corollary 3.2 (linear/quadratic energy)

Fix constants (A,D,C).  If

\[
 p\le C\sqrt m,qquad I\le Am,qquad J\le Dm^2,
\tag{3.6}
\]

then, for all sufficiently large (m), at most

\[
                         \boxed{\lfloor2A\rfloor+\lfloor4D\rfloor}
\tag{3.7}
\]

sources are omitted.

#### Proof

Take (R=\lfloor m/2\rfloor+1).  Then (R>m/2), and for
(p=O(\sqrt m)),

\[
 S_R={m-p+1\choose2}-{\lfloor m/2\rfloor\choose2}
 \ge m^2/4
\]

eventually.  Substitute (3.6) into (3.3).  □

The energy condition is strictly weaker than bounding the number of paths,
their lengths, or even their total global footprint: damage far from every
required source star has zero weight in (3.2).

## 4. From owner area to the energy bound

Suppose the selection-stable cap atlas factors through global damaged value
sets (D_{\mathcal U},D_{\mathcal Z}), as in the audited two-layer
footprint theorem.  If

\[
 |D_{\mathcal U}|\le A_0m,qquad
 |E_{\mathcal Z}|\le E_0m^2,
\tag{4.1}
\]

then Theorem 2.1 gives

\[
 |D_{\mathcal Z}|
 \le(A_0+E_0)m^2.
\tag{4.2}
\]

The two-layer incidence-energy bounds then imply (3.6), with constants
depending only on (A_0,E_0,C), provided the separately priced hidden-hole
sum is also O(m^2).  Therefore a linear owner projection plus a quadratic
exceptional-terminal/hidden bank is sufficient; no separate bound on
ordinary q1 terminals is needed.

At the physical occurrence level, it is enough to prove the aggregate
layer-area rows

\[
 |\pi_m(\operatorname{cap}\mathcal Q)|\le A_0m,
 \qquad
 |E_{\mathcal Z}|\le E_0m^2,
\tag{4.3}
\]

where the map pi_m projects rank-(m) capacity occurrences to Boolean owner
values.  Equation (2.1) supplies the q1 projection automatically.

## 5. Selection-stable activation is the exact remaining occurrence row

The support-level path (1.3) exists after factor completion.  To use the
prospective menu before choosing that completion, the common-cap interface
must satisfy the following one-way implication.

> **Selection-stable activation.**  In one fixed cap/guard/phase state,
> every wedge outside the cover (3.1), whenever protected and extended to
> a compatible Middle-Levels factor, has at least one canonical path in
> (1.3) which survives the frozen background and is a typed legal route to
> an unused sink (or to a certified private tail).  For every
> owner/terminal-distinct selected bank, the resulting local routes and any
> tails coexist: all nonendpoint capacities are private, or every possible
> hidden collision was already charged to the sets H_i.

This condition is weaker than materializing every candidate branch at
once.  Only the ultimately selected (O(\sqrt m)) paths need physical
capacity.  It is stronger than value-level eligibility in different cap
states: all selected paths must coexist in the one stated state.

A sufficient local form is that source survival, owner availability,
terminal availability, arc typing and sink acceptance depend only on the
fixed state and the local tuple

\[
                         (L_i,U_i^0,U_i^1,Z_i),
\]

not on the unprotected part of the factor completion, and that any tails
are endpoint-factorized and private across distinct local tuples.  Then
Theorem 1.1 turns every selected local certificate into its canonical
physical occurrences.

## 6. Weak regenerative occurrence invariant

The cap-side induction needs only the following state, rather than a
monotone compensation linkage or a full pre-materialized suffix gammoid.

> **Regenerative owner-area invariant (ROA).**  There are absolute
> constants (A,E,C,C_0) such that every same-parity transition:
>
> 1. exposes at most (p\le C\sqrt m) required wedge tasks plus at most
>    (C_0) deleted-source exceptions;
> 2. has a selection-stable activation atlas as in Section 5;
> 3. after freezing its background, has distinct owner projection at most
>    (Am), at most (Em^2) terminal-only/hidden wedge exceptions, and a
>    degree-compatible protected-factor budget;
> 4. satisfies the remaining phase, two-coordinate product, upper,
>    residence and topology guards for the selected bank; and
> 5. exports a fresh state satisfying the same constants, rather than
>    adjoining its footprint to every ancestral footprint.

### Theorem 6.1 (ROA closes the cap contribution)

Under ROA, the one-coordinate common-cap/wedge row contributes only an
absolute number of terminal casualties at every dimension.  The bound is
obtained by (2.1), the two-layer footprint theorem (or directly by Theorem
3.1), and the (C_0) source exceptions.  The selected paths themselves are
materialized by Theorem 1.1.

Consequently, if the already separated carrier, upper, residence,
compiler and topology rows also regenerate with bounded defect, ROA implies

\[
                         \nu(k)\le B(k)+O(1).
\]

The theorem is conditional only on the enumerated regenerative rows; it
does not infer them from the present Pascal child.

## 7. Necessity of an owner-area or energy premise

The number of compensation paths cannot replace ROA item 3.  A single
simple path in an unrestricted occurrence network may snake through an
arbitrarily large family of rank-(m) owner capacities.  By arranging those
owners to cover complete source stars, it can make the task-incidence
energy (I) arbitrarily large.

Thus one must control at least one of:

1. the distinct owner projection;
2. the weighted task-incidence energy (I); or
3. an equivalent residual rank/cut certificate.

This is a sharp logical boundary.  Rank monotonicity is one sufficient way
to obtain such control, but Theorems 2.1 and 3.1 show it is not the needed
invariant.

## 8. Dependencies

- `MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md`
- `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md`
- `MATH_THEOREM_MIDDLE_LEVELS_TURN_DIAMOND_CAPACITY_ROUTER_20260804.md`
- `MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md`
- `MATH_THEOREM_TWO_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`
- `MATH_THEOREM_CYCLE_ALIGNED_WEDGE_LINKAGE_FACTOR_MATERIALIZATION_20260804.md`
