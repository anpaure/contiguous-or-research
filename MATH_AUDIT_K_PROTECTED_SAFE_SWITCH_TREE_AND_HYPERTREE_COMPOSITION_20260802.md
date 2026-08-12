# Audit: protected safe-switch tree and hypertree composition

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K_PROTECTED_SAFE_SWITCH_TREE_AND_HYPERTREE_COMPOSITION_20260802.md`  
**Verdict:** PASS, with the theorem's explicit hereditary-applicability and
extended-support hypotheses.  Projected LKK expansion is not a switch-supply
theorem.

## 1. Component arithmetic

For a switch family `T`, its incidence graph has

\[
 |V(T)|+|T|\quad\hbox{vertices},\qquad
 \sum_{e\in T}|e|\quad\hbox{edges}.                  \tag{1.1}
\]

Thus it is a tree exactly when it is connected and

\[
 \sum_e(|e|-1)=|V(T)|-1.                             \tag{1.2}
\]

Applying the same count to every nonempty subfamily gives the forest
inequality

\[
 \sum_{e\in A}(|e|-1)\le |\cup A|-1.                \tag{1.3}
\]

Rooting the incidence tree gives the claimed application order.  Each
rank-`r` packet meets one accumulated component and `r-1` untouched
components, so a certified maximum merger decreases component count by
`r-1`.  Summing (1.2) leaves one component.  The converse count is equally
exact once every applied packet is known to make its maximum decrease.

For rank two, (1.2)--(1.3) are the ordinary spanning-tree equations.  For
rank three, they are

\[
 |V|=2|T|+1,\qquad 2|A|\le|\cup A|-1,               \tag{1.4}
\]

the loose-hypertree equations already used in the corrected k17 `C6`
component theorem.

## 2. Checks against the literal switch calculus

The corrected incidence-`C6` stub theorem permits component changes

\[
                       -2,-1,0,+1,+2.                \tag{2.1}
\]

Therefore a raw alternating hex is not automatically a rank-three edge.
The new theorem correctly admits it only after the three deleted owner
adjacencies are certified to lie on distinct current cycles, in which case
the exact cyclic closure gives `Delta c=-2`.

Likewise a general `C6/C8` pull is not automatically a rank-two edge.  Its
two-component maximum-merger phase must be certified.  This matches the
general retained-stub formula rather than the retracted parity shortcut.

Marked-arc preservation also checks literally: the protected bank is
disjoint from every extended support, so no deleted arc, born arc, collar or
resource witness used by the switch touches a marked contraction.  Exact-one
physical-fibre selection is retained because old and new phases have the
same fibre and degree vectors.

## 3. Two sharp failures of weaker formulations

### 3.1 Connected ternary 2-section

The triples

\[
 123,\quad124,\quad125                              \tag{3.1}
\]

have a connected 2-section.  After toggling any one triple, each remaining
triple has two old components already fused, so its three-distinct-component
hypothesis fails.  Algebraically, two triples have union size four and
violate `2*2 <= 4-1`.  Hence ordinary connectivity cannot replace the
incidence-tree row.

### 3.2 Marginal LKK projection

Start from any projected owner/lower two-factor with at least two
components.  Add the component ID to each admissible history state and
permit only component-ID-preserving transitions.  This leaves every
owner/lower incidence, degree, codegree, protected demand and LKK shore
unchanged, while every cross-component safe-switch list becomes empty.
Thus no statement expressed only in those projected quantities can imply
safe-switch connectivity.

This obstruction is logical and scoped: it does not say that the intended
Boolean history table has such component labels.  It proves that a new
Boolean correlation theorem is required.

## 4. Interaction audit

The following implications are valid only with their indicated hypotheses.

| Proposed implication | Verdict | Required row |
|---|---:|---|
| connected binary auxiliary graph -> one cycle | conditional GO | choose a spanning tree with mutually compatible literal packets |
| connected ternary 2-section -> one cycle | NO | replace by a compatible spanning incidence hypertree |
| pairwise disjoint deleted edges -> commuting switches | NO | disjoint extended occurrence supports or hereditary applicability |
| individual palette/history safety -> batch safety | NO | exact additive final ledger or context-independent supports |
| residual LKK expansion -> cross-component pulls | NO | independent protected switch-basis supply |
| compatible spanning switch basis -> marked one-cycle factor | GO | maximum-merger semantics and exact-one fibre preservation |

For finite-memory histories, disjoint complete history collars are a
proof-sufficient extended support.  Arbitrary-width interval decks and
common-cap compiler rows are not automatically collar-local; they require a
separate additive theorem or literal final replay.  The composition theorem
does not silently promote them to local resources.

## 5. Exact remaining theorem

After the residual Ore extension, it is enough to prove one of:

1. a conflict-compatible labelled spanning tree of protected-safe binary
   maximum mergers; or
2. a conflict-compatible spanning incidence hypertree of protected-safe
   ternary maximum mergers (plus one parity sidecar when the component count
   has the wrong parity).

The direct-new-phase arcs must be part of the protected extended state.
This switch-basis existence is strictly stronger than marginal factor
existence and is the first unproved row of the cycle-factor alternative.
