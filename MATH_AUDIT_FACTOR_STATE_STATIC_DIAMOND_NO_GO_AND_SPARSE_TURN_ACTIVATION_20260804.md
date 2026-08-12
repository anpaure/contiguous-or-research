# Audit: factor-state static-diamond no-go and sparse-turn activation

**Date:** 2026-08-04  
**Method:** independent symbolic audit; pure mathematics, no finite search  
**Audited theorem:**
`MATH_THEOREM_FACTOR_STATE_STATIC_DIAMOND_NO_GO_AND_SPARSE_TURN_ACTIVATION_20260804.md`  
**Verdict:** **GO**, with the source-flexibility and full-q1-degree scopes
made explicit in the audited theorem.

## 1. Fixed-factor degree ledger

At one lower turn `L_j`, a spanning two-factor has exactly the two incident
owners `U_j,U_(j+1)`.  The occurrence lift supplies exactly those two
certified direct prefix halfports.  Hence the current proved interface has
prefix degree two, independently of the size of the ambient Middle-Levels
star.

An owner occurrence `u_j` belongs to only the two adjacent q1 turns
`z_(j-1),z_j`, so its full certified factor-q1 sink degree is at most two.
Under the own-turn semantics used by the canonical turn router, either
branch at `L_j` ends at the one occurrence `z_j`; its sink degree is one.
Thus

\[
 L_0\le2,\qquad L_1\le2,\qquad L_1^{\rm own}\le1
\]

is exact for the stated certified faces.  It does not constrain extra
nonfactor arcs or replicated occurrence layers not supplied by the current
factor theorem.

The prospective-wedge collapse is also exact.  A wedge consumes both factor
edges at its lower endpoint.  Two different wedges there would require at
least three distinct edges, so one fixed factor contains exactly one wedge
at that lower vertex.

## 2. Logical nonimplication

Materializing only the canonical factor nodes and own-turn arcs, while
placing compensation on a disjoint bank, satisfies every occurrence-lift
and turn-diamond statement used as input.  Its active menu sizes remain
`2` and `1`.  This is a valid countermodel to any deduction of divergent
static menu size from those hypotheses alone.  It is deliberately not a
nonexistence theorem for a richer cap.

## 3. Selected-turn collision criterion

For selected turn `j`, side zero uses owner `u_j` and side one uses
`u_(j+1)`.  An owner `u_j` can therefore be used twice only by the pair of
adjacent selected turns `j-1,j`, and exactly for the side pattern `(1,0)`.
Sources and own-turn sinks have distinct occurrence addresses.  Hence

\[
 (j-1,j\in S)\Longrightarrow(c_{j-1},c_j)\ne(1,0)
\]

is necessary and sufficient.

On a path run this says that the chosen bits are nondecreasing.  An allowed
nondecreasing word exists exactly when every allowed set is nonempty and no
forced one precedes a forced zero.  On a full cycle, a cyclic nondecreasing
binary word is constant, so the intersection of all allowed-side sets must
be nonempty.  The theorem's run and cycle criteria are therefore exact.

This criterion assumes occurrence-address capacities.  If equal Boolean
values at different turns are identified later, another quotient-capacity
condition is required; the theorem states that boundary.

## 4. Greedy independent-turn transversal

One chosen turn forbids only itself and its two neighbours in any other
set-valued candidate menu.  After `j` choices it deletes at most `3j`
candidates from the next menu.  Strict menu size greater than `3(p-1)` thus
supports a greedy independent transversal.  Pairwise nonconsecutive turns
have disjoint two-owner neighbourhoods, and their source and q1 sink
addresses are already distinct, so arbitrary locally active branches are
private.

The theorem correctly limits this statement to source-flexible logical
tasks.  If a gain has one prescribed lower Boolean source and there are no
occurrence copies, a spanning factor contains that source once; its turn
menu has size at most one.  In that fixed-source case the selected-turn
criterion, not the greedy transversal, is the relevant theorem.

For a forbidden occurrence bank, a source or own-q1 sink touches one
canonical turn and an owner touches two.  Removing every touched turn loses
at most `2|F|` candidates, proving the stated sufficient inequality.  Hidden
flags, shared arcs, or noncanonical cap resources are outside that count and
must be included before defining an active candidate menu.

## 5. Exact revised frontier

On the current canonical factor face, static `Theta(m)` good-diamond
abundance is the wrong target.  There are two proof-safe alternatives:

1. for fixed-source gains, jointly choose the protected wedge factor and one
   common cap state that activates one typed branch of every selected wedge;
2. for genuinely source-flexible tasks, expose more than `3(p-1)` active
   compatible turn occurrences in one state and use the independent-turn
   transversal.

Neither activation statement follows from the current Pascal factor or cap
theorems.  Two-coordinate routing additionally needs source, owner, and
terminal multiplicity or genuinely disjoint product layers.  Accordingly
the audited theorem is a sharp obstruction and narrower reduction, not an
all-dimensional construction.

