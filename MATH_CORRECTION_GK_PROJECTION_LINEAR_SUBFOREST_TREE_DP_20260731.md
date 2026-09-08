# Corrected Greene--Kleitman projection linear-subforest theorem

Date: 2026-07-31  
Status: exact finite dynamic-programming theorem; asymptotic analysis now
completed in the companion switch/plane-tree theorem

## 1. Scope and correction

Let \(T_m\) be the Greene--Kleitman central projection forest on
\(W=\binom{2m}{m}\) middle sets, oriented from every non-root vertex toward
its projection parent.  It has \(\operatorname{Cat}_m\) roots and
\(W-\operatorname{Cat}_m\) edges.

The earlier assertion that every linear subforest of \(T_m\) retains at
most \(W/2\) edges is false.  Deleting the outgoing edge of a vertex can
leave two of its incoming child edges, as the elementary star example
already shows.  Thus neither the former \(W/2\) bound nor the derived
\((1/2-o(1))W\) replacement estimate may be used.

What follows is the exact replacement optimization.  Since \(T_m\) is a
forest, an edge subset is a linear forest if and only if every vertex has
degree at most two.

## 2. Exact rooted-tree recurrence

For a vertex \(v\), let \({\cal C}(v)\) be its children.  For
\(p\in\{0,1\}\), define \(F_v(p)\) to be the maximum number of retained
edges in the subtree rooted at \(v\), not counting the edge from \(v\) to
its parent, conditional on that parent edge being absent when \(p=0\) and
present when \(p=1\).

For each child \(u\), put

\[
 B_v=\sum_{u\in{\cal C}(v)}F_u(0),\qquad
 g_u=1+F_u(1)-F_u(0).                                  \tag{2.1}
\]

If \(g_{(1)}\ge g_{(2)}\ge\cdots\) are these gains in decreasing order,
then

\[
 \boxed{
 F_v(p)=B_v+
 \sum_{i=1}^{2-p}\max(0,g_{(i)})
 }
                                                               \tag{2.2}
\]

with nonexistent gains omitted.  Therefore the exact maximum number of
retained projection edges is

\[
 R_m=\sum_{r\text{ root of }T_m}F_r(0).                \tag{2.3}
\]

### Proof

Fix the state of the parent edge.  If the edge \(vu\) is omitted, the
optimal contribution of the child subtree is \(F_u(0)\).  If it is retained,
the contribution is \(1+F_u(1)\), so its marginal gain is \(g_u\).
The degree-two constraint leaves exactly \(2-p\) child-edge slots at \(v\).
Child subtrees are otherwise disjoint, so an optimum selects the largest
positive gains that fit.  This proves (2.2) by induction from the leaves.
Summing the root states proves (2.3).  Every selected subgraph is acyclic
because it lies in \(T_m\), hence degree at most two is equivalent to being
a linear forest. \(\square\)

## 3. Exact finite replay

Direct reconstruction of the projection from the unmatched-parenthesis
normal form, followed by (2.2), gives:

| \(m\) | projection edges | \(R_m\) | minimum deleted original edges |
|---:|---:|---:|---:|
| 2 | 4 | 4 | 0 |
| 3 | 15 | 13 | 2 |
| 4 | 56 | 44 | 12 |
| 5 | 210 | 159 | 51 |
| 6 | 792 | 588 | 204 |
| 7 | 3003 | 2188 | 815 |

In particular, the corrected values for \(m=3,\ldots,7\) are

\[
                         13,44,159,588,2188,             \tag{3.1}
\]

strictly above the obsolete values \(10,35,126,462,1716\).

The deterministic audit is
`scratch/audit_gk_projection_linear_subforest_tree_dp_20260731.py`; it
reconstructs all middle masks, projection parents and DP states without a
solver.  Its canonical payload is
`ea462f62da4d54c8c0c6e904e4ac63b7155b2df251411c813edc3af67b5ecb2f`.

## 4. Exact conclusion and completed asymptotics

For each finite \(m\), at least

\[
 W-\operatorname{Cat}_m-R_m                              \tag{4.1}
\]

original projection edges must be removed before the projection forest is
linear.  The table evaluates this exact quantity through \(m=7\).

The required plane-tree analysis has subsequently been completed in
`MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md`.
Writing \(\Delta_m=W-\operatorname{Cat}_m-R_m\), it proves

\[
 {\Delta_m\over m\operatorname{Cat}_m}
 \longrightarrow0.356895867892\ldots .
\]

Thus the corrected edit barrier is \(\Theta(W)\).  The separate radius-drop
obstruction in `GK_PROJECTION_COUNTS.md` remains valid and is unaffected by
this correction.
