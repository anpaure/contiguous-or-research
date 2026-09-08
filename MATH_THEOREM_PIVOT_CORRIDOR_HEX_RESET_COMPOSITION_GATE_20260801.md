# Pivot corridors transport the reset signature, but a Boolean hex cannot close its attachment return

Date: 2026-08-01

Status: exact projection-level composition audit.  A bidirectional private
Johnson path has precisely the one-attachment/two-predecessor boundary
signature of an opened rolling reset.  The noncanonical pivot-rich path is
therefore the correct *shape* for a relocation corridor.  Even granting a
literal two-phase planting of such corridors, a terminal ternary Boolean
hex cannot close the transported signature: its old and new phases have
identical head--owner columns.  The first failure is the attachment
projection, before residence, arbitrary-width OR or compiler safety.

## 1. A bidirectional path has the exact three-return signature

Let

\[
              V_0\to V_1\to\cdots\to V_\ell
\]

be a simple Johnson path, put `U_i=V_i union V_(i+1)`, and suppose both
orientations have literal flag lifts.  In the forward and reverse phases
the head--owner columns are respectively

\[
 \mathcal A^+=\{(V_{i+1},U_i):0\le i<\ell\},\qquad
 \mathcal A^-=\{(V_i,U_i):0\le i<\ell\}.             \tag{1.1}
\]

Their symmetric difference is one alternating path with head endpoints
`V_0,V_l`.  The predecessor projections are

\[
 \mathcal P^+=\{V_i^-V_{i+1}^+:0\le i<\ell\},\qquad
 \mathcal P^-=\{V_{i+1}^-V_i^+:0\le i<\ell\}.        \tag{1.2}
\]

Their symmetric difference is the union of the two index-parity paths.
Thus a bidirectional path transports exactly one attachment endpoint pair
and two predecessor-parity endpoint pairs.  Every `U_i` is used once in
each phase, so literal owner capacity is exact.

The pivot-rich geodesic and its collar provide a simple, doubly-rainbow
owner path with private internal resources.  This makes them a valid
candidate for the physical support of (1.1)--(1.2).  The pivot theorem by
itself proves only one collared owner chronology, not a common ambient
two-phase flag table; below we grant the stronger bidirectional lift.  The
composition still fails.

## 2. The ternary Boolean hex is attachment-inert

Use the Boolean hex notation

\[
\begin{array}{lll}
A=S+a+u,&B=S+a+c,&C=S+c+u,\\
D=S+b+c,&E=S+b+u,&F=S+a+b,
\end{array}
\]

with phases

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\}.                       \tag{2.1}
\]

Write

\[
 o_1=S+a+c+u,\qquad o_2=S+b+c+u,\qquad
 o_3=S+a+b+u.                                        \tag{2.2}
\]

Then the complete head--owner projections are

\[
 \boxed{
 \alpha(O)=\{(B,o_1),(D,o_2),(F,o_3)\}=\alpha(N).}   \tag{2.3}
\]

The hex is nontrivial only in its predecessor projection:

\[
 \pi(O)=\{A^-B^+,C^-D^+,E^-F^+\},\qquad
 \pi(N)=\{A^-F^+,C^-B^+,E^-D^+\},                   \tag{2.4}
\]

whose symmetric difference is the alternating `C_6`.

### Theorem 2.1 (first projection mismatch)

No collection of private bidirectional pivot corridors followed solely by
one complete Boolean-hex toggle `O <-> N` is a compatible three-return lift
for an opened rolling reset.

#### Proof

After the corridor differences cancel the reset boundary at the reset
endpoints, they export one nonzero attachment-path boundary at their far
endpoints.  Equation (2.3) says that the terminal hex contributes zero to
the attachment symmetric difference.  Hence that boundary remains open.
The predecessor `C_6` in (2.4) may rewire or close predecessor paths, but a
compatible literal lift requires both projection systems to close
simultaneously.  It therefore fails first in the head--owner projection.
`square`

This is stronger than a marginal-count objection: the three literal
head--owner columns are occurrencewise the same in the two hex phases.

## 3. Opening the hex does not give a balanced repair

The only old and new atoms with a common owner are

\[
 (A\to B,C\to B),\quad(C\to D,E\to D),\quad
 (E\to F,A\to F).                                    \tag{3.1}
\]

Each pair also has the same head.  Hence deleting one atom in each phase
while retaining the same owner set either leaves the attachment projection
unchanged or, if different owners are deleted, exports owner endpoints as
well as head endpoints.  It never creates the required alternating return
with common owner inventory and two distinct head endpoints.

The gain form

\[
             \{A\to B,C\to D\}\longmapsto N          \tag{3.2}
\]

adds the missing full column `(F,o_3)` and is a legitimate one-unit rainbow
augment when that entire atom is free.  It is not a phase-balanced reset
return: the two sides have different cardinality and owner inventories.

Thus the exact missing terminal packet is attachment-active.  It must have
the same owner set in both phases but two different head assignments, while
its predecessor projection closes the two parity returns.  The standard
Boolean hex does not have that property.

## 4. Independent audit of ternary three-cycle fusion

Suppose the old edges in (2.1) lie on three distinct directed cycles.
Deleting them leaves paths

\[
                   B\leadsto A,\quad D\leadsto C,
                   \quad F\leadsto E.
\]

The new edges concatenate them as

\[
 B\leadsto A\to F\leadsto E\to D\leadsto C\to B,
\]

one directed cycle.  Hence the theorem in
`MATH_THEOREM_BOOLEAN_HEX_THREE_CYCLE_FUSION_AND_TERNARY_CONTRACTION_20260801.md`
is correct: `3 -> 1`, so the cycle count changes by `-2`, and its parity is
invariant.  Component-disjoint packets commute.

The projection audit sharpens its scope.  The fusion is achieved entirely
by changing the predecessor tail--head matching (2.4); the head--owner
attachment matching is literally fixed by (2.3).  It therefore solves the
central topology row but cannot double as the reset attachment return.

## 5. Relation to the frozen support-three commutator shell

`MATH_THEOREM_A_K17_2E919_CRITICAL_SHORE_SUPPORT3_COMMUTATOR_ESCAPE_20260801.md`
enumerates primitive triples in `C_ov(F)` which factor through overlapping
support-two moves and can change the frozen common attachment-state graph.
The Boolean hex's suffix/flag action is an indispensable cubic on a
structural-zero `C_6`, so it lies outside that enumerated shell.  The
present theorem adds a different separation: on its three selected atoms,
the complete `O <-> N` toggle has zero head--owner action.  Therefore it
cannot itself supply the opened reset's attachment alternating path.

The support-three commutator winners and the Boolean hex solve complementary
rows: the former are attachment-active but have no proved chronology,
upper-deck or reset lift; the latter is a literal resource/topology cubic
but attachment-inert.  A positive reset splice must combine those two
features in one physical packet, or compose the Boolean hex with a separate
attachment-active return whose owner endpoints are fully balanced.

## 6. Exact remaining composition

The pivot-corridor idea remains useful after this no-go.  Its corrected
target is

\[
 \boxed{\text{private bidirectional pivot corridors}}
 \; + \;
 \boxed{\text{attachment-active balanced terminal circuit}}
 \; + \;
 \boxed{\text{optional Boolean-hex topology fusion}}.
\]

The terminal circuit must change the head assignment of a fixed owner bank;
the Boolean hex may then be used separately to merge three physical cycles.
Residence, arbitrary-width OR current and common-cap safety remain further
guards after this literal projection gate is met.
