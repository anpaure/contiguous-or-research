# Audit of q2-neutral clean-C6 loose-forest completion

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_Q2_NEUTRAL_C6_LOOSE_FOREST_GRAPHIC_COMPLETION_20260805.md`  
**Method:** independent component/omission replay; no computation or search  
**Verdict:** **PASS**, under the stated physical-disjointness and
current-state neutrality hypotheses.

## 1. One connector

Cutting one selected directed edge from each of three distinct cycles
leaves three paths.  The cyclic clean-C6 reconnection concatenates those
paths into one cycle.  Removed and inserted edges are all selected, so no
omission is created or consumed.  Therefore

\[
 o(C')=o(C_0)+o(C_1)+o(C_2).
\]

The output is hit exactly when an input is hit.  q1 and q2 preservation is
literal from the selected common-deletion C6 hypothesis.

## 2. Loose-tree ordering

Delete a connector node from the incidence tree.  Its three incident
branches are disjoint.  Processing the two branches away from a chosen
root first collapses each branch internally but cannot join it to either
other branch, because the connector itself has not been used.  The three
old shores at that connector therefore remain on three distinct current
cycles.  The one-connector lemma applies.  Induction gives one output
cycle per loose tree.

Pairwise vertex-disjoint physical supports are the exact persistence
condition needed here: edge-disjointness alone would not prevent an
earlier switch from changing a later companion row.  The source states the
stronger, sufficient condition.

## 3. Forest and two-switch criterion

Partitioning all factor cycles into hit-rooted loose trees makes the sum of
input omissions positive in every output block, so every output component
is hit.  The q2 Pascal two-factor lift then applies.

After the explicit first rigid-edge C6, `Pi_12` and `Pi_21` lie on the two
distinct unhit output cycles.  A physically disjoint second connector with
one old edge in each path and one on a hit donor therefore sees three
distinct current cycles.  It merges them and inherits the donor's positive
omission.  This proves Corollary 5.1 exactly.

For Corollary 4.2, hit-rootedness is not used in the serial loose-tree
argument.  Every loose-tree block still contracts to exactly one cycle and
its omission count is the sum over that block.  Hence a partition into `b`
blocks leaves at most one unhit output per block, so at most `b` total.
Combining this with the independently proved bounded-defect q2 Pascal lift
charges at most `2b` at the q2/owner interface.  This is an implication;
existence of a `b=O(1)` physically disjoint PBBS loose forest remains open.

The theorem is an implication, not an existence proof for the required
PBBS loose forest or straddling second connector.  It makes no q3,
residence, or common-cap assertion.  Its stated scope is correct.
