# Feasible-decoration relations compose; scalar transparent edges do not

Date: 2026-07-31  
Status: exact finite-boundary composition theorem for the minimal central
matching-plus-trace state; exact vertex-disjoint two-toggle obstruction in
`ML(7)`; no bounded-width or all-dimension accepting-state theorem

## 0. Verdict

The Decorated Middle Levels target does not require one arbitrarily chosen
SDR to survive the standard MMM gluing recursion.  The exact bottom-up
object is a **relation of all feasible boundary matching and trace states**.
That relation composes by natural join and existential projection.

For a normalized gluing tree node (x), let (B_x) contain every augmented-
graph vertex and trace endpoint incident with both the processed subtree and
its exterior.  The node relation records:

1. which vertices of (B_x) are already matched internally;
2. at every boundary occurrence, whether its eventual mark is already
   forced to be a turn mark, forced to be residual, or is still open; and
3. the finite binary-run summary of every open trace fragment.

Every interior augmented vertex is already matched exactly once.  The
relation contains **all** jointly realizable tuples, not independent
projections of the three rows.

These relations compose exactly.  At the root, nonemptiness with empty
matching boundary and an accepting cyclic trace is equivalent to a terminal
joint Catalan decoration on the linear-forest face.

There are two sharp qualifications.

* This is finite for every finite boundary, but the state count depends on
  the actual augmented-graph adhesion.  The standard MMM recursion has not
  been proved to have uniformly bounded decoration adhesion.
* Replacing the relation by one Boolean per glue--"this hexagon is
  transparent for some decoration"--is false already in `ML(7)`.  Two
  vertex-disjoint hexagons are individually transparent through hundreds of
  linear decorations, but no one decoration survives both.

Thus the feasible-decoration relation **does** compose, while its scalar
nonempty projection does not.  The missing induction theorem is nonemptiness
of the correlated root relation (or a structural bounded-width subclass),
not another local hexagon transfer rule.

## 1. The augmented matching interface

Fix a final or partially assembled Middle Levels factor.  Its augmented
occurrence graph ({\cal A}) is bipartite and has the standard property

\[
 \operatorname {PM}({\cal A})
 \longleftrightarrow
 \{\text{joint alternating upper/lower turn SDRs}\}.    \tag{1.1}
\]

The turn edge chosen at an occurrence says that the occurrence is marked;
an incidence edge says it is residual.  Hence a perfect matching also
determines the cyclic binary mark trace.

Let a rooted tree decompose the factor chronology and all augmented edges.
For a node (x), write (E_x) for the augmented edges introduced in its
subtree.  Its boundary is

\[
 B_x=\{v:v\text{ is incident with an edge of }E_x
                 \text{ and with an edge outside }E_x\}.          \tag{1.2}
\]

The decomposition is **normalized** when every chronology edge whose later
toggle can change a turn is exposed at the same boundary.  Thus no forgotten
interior occurrence can acquire a new neighbour later.

A partial matching (M_x\subseteq E_x) is internally complete when every
vertex outside (B_x) incident with (E_x) is matched exactly once and
every boundary vertex has matching degree at most one.

## 2. Exact boundary relation

For an internally complete (M_x), record the following boundary datum.

* (d_x(v)\in\{0,1\}) is the matching degree already used at
  (v\in B_x).
* If (v) is a chronology occurrence, record
  (\eta_x(v)\in\{\mathsf T,\mathsf R,\mathsf O\}): it is already matched
  through a turn edge, already matched through an incidence edge, or is
  open.  The first two cases force the mark bit `1` or `0`.
* Cut the cyclic mark word at every open occurrence and every chronology
  port exposed to an ancestor.  For each oriented decided fragment retain:
  its first and last bit; the prefix and suffix zero-run lengths in
  categories `1,2,3+`; the prefix and suffix one-run parities; a homogeneous
  bit; and a breaker bit recording whether the fragment already contains a
  zero-run of length other than two or an even one-run.

Call the resulting tuple (\sigma_x(M_x)), and define

\[
                  \Sigma_x=\{\sigma_x(M_x):
                       M_x\text{ internally complete}\}.          \tag{2.1}
\]

This is a relation, because several tuples--and several witnesses for one
tuple--may coexist.  It does not choose one SDR.

The run alphabet is finite.  When equal boundary bits are concatenated,
zero lengths use capped addition into `3+` and one lengths add modulo two.
When unequal bits meet, both boundary runs close and update the breaker.
The homogeneous bit prevents the prefix and suffix of one run from being
counted twice.  At the root, the cyclic trace is on the physical-forest side
exactly when the breaker is true after the final suffix--prefix join.

## 3. Relational closure

Suppose a parent node (x) has children (y_1,\ldots,y_s), disjoint
interiors, and a finite local augmented edge set (E_x^\circ).  The local
MMM hexagon also specifies how the open chronology fragments are oriented
and concatenated.

### Theorem 3.1 (feasible-decoration relation composition)

The parent relation (\Sigma_x) is obtained exactly as follows.

1. Choose one tuple from every (\Sigma_{y_i}) and one matching in the
   local edge set (E_x^\circ).
2. Reject if any identified boundary vertex is matched twice.
3. Every vertex forgotten at (x) must now be matched exactly once.
4. Join the child trace fragments in the literal local chronology and apply
   the finite run operation of Section 2.
5. Retain the matching/mark/trace data on (B_x), and existentially forget
   the child-boundary data.

At the root, (B_x=\varnothing).  The relation contains an accepting state
if and only if the assembled factor has a perfect augmented matching whose
binary trace is on the linear-forest side.

#### Proof

Restrict any global perfect matching to the edge sets of the child
subtrees and the local edge set.  Each restriction is internally complete,
their matching degrees are compatible, and every forgotten vertex is used
once.  Cutting the literal cyclic mark trace at the declared ports gives
exactly the child fragment summaries, so restriction produces a tuple
accepted by Steps 1--5.

Conversely, compatible child matchings and the local matching have disjoint
edge sets and matching degree one at every forgotten vertex.  Induction over
the tree therefore glues them to one matching of all processed augmented
vertices, with precisely the declared open boundary degrees.  The trace
operation is literal concatenation, hence associative and exact because
only the runs meeting a seam can change.  At the empty root boundary the
matching is perfect, and the final cyclic run test is exactly the binary-
trace forest criterion. \(\square\)

If (b_x=|B_x|) and (f_x) trace fragments remain open, the number of
syntactic states is at most

\[
                       3^{b_x}\,T^{f_x},              \tag{3.1}
\]

for one absolute finite run alphabet (T).  This is a finite-boundary
theorem, not a proof that (b_x+f_x=O(1)) in the standard MMM recursion.
Every turn-colour vertex with occurrences on both sides of a recursion cut
belongs to (B_x); projecting it away can identify states with different
exterior completion behaviour.

### Corollary 3.2 (what an induction still needs)

An all-dimension proof follows if the standard MMM recursion can be equipped
with normalized interfaces for which:

1. the relations (2.1) can be generated recursively;
2. one accepting root tuple survives; and
3. either the interfaces are uniformly bounded, or a structural argument
   proves nonemptiness without enumerating their full tables.

Theorem 3.1 proves composition, not Item 2 or a width bound.

## 4. Exact `ML(7)` failure of scalar edgewise transparency

Let (C_0) be the authenticated positive decorable `ML(7)` cycle in
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`.
Toggle the incidence hexagon

\[
                  Z_1=(H=34;(2,3,4))                 \tag{4.1}
\]

to obtain (C_1), and then toggle

\[
                  Z_2=(H=96;(0,1,4))                 \tag{4.2}
\]

to obtain (C_2).  Their physical port sets are disjoint:

\[
 \begin{aligned}
 V(Z_1)&=\{38,42,46,50,54,58\},\\
 V(Z_2)&=\{97,98,99,112,113,114\}.                  \tag{4.3}
 \end{aligned}
\]

All three factors are Hamilton cycles.  Let ({\cal D}(C)) denote the set
of Catalan decoration vertex-set pairs of (C).  Exact enumeration gives

\[
\begin{array}{c|r}
\text{set}&\text{size}\\ \hline
{\cal D}(C_0)&1728\\
{\cal D}(C_1)&7776\\
{\cal D}(C_2)&11340\\
{\cal D}(C_0)\cap{\cal D}(C_1)&576\\
{\cal D}(C_1)\cap{\cal D}(C_2)&1620\\
{\cal D}(C_0)\cap{\cal D}(C_1)\cap{\cal D}(C_2)&0.
\end{array}                                           \tag{4.4}
\]

Every decoration in the two pairwise intersections is on the linear-forest
side on both adjacent cycles.  Every one of the `11,340` terminal
decorations of (C_2) is also on the linear-forest side.

### Proposition 4.1 (nonempty edge labels do not compose)

The Boolean statement

\[
 \text{“toggle }Z\text{ has some common linear decoration”}       \tag{4.5}
\]

is not closed under even two vertex-disjoint toggles.  Therefore a gluing
tree whose every edge separately passes (4.5) need not carry one common
decoration.

#### Proof

Both pairwise intersection rows in (4.4) are nonempty and consist entirely
of linear decorations, while the triple intersection is empty. \(\square\)

At the palette level, the obstruction is already visible on the common
base cycle: the all-six face of (Z_1) forces the lower occurrence `50`,
the all-six face of (Z_2) forces `98`, and both have upper turn colour
`122`.  A single upper-turn SDR cannot select both.  The complete counts in
(4.4) show that the obstruction persists for the full common-decoration
sets, not only one displayed all-six witness.

The relation (2.1) detects this conflict because the shared colour vertex
`122` remains on the boundary until both subproblems have been joined.  A
scalar nonempty projection forgets it.

## 5. Consequence for the weakest central target

There are now three precisely separated statements.

1. **Terminal existence:** one decorated Hamilton cycle with linear trace.
   By the post-glue repair theorem this is the weakest central target.
2. **Relational MMM induction:** a normalized standard recursion whose
   correlated relations (\Sigma_x) have a nonempty accepting root.  This
   is a proof-sufficient route to Item 1 and does not freeze an SDR.
3. **One transparent SDR through a gluing tree:** the diagonal subrelation
   in which the same decoration is retained at every edge.  It is strictly
   stronger, and Proposition 4.1 shows that edgewise diagonal nonemptiness
   is not enough to construct it.

Theorem 3.1 closes the formal composition question for Item 2.  The first
remaining mathematical obstruction is constructive: prove a uniformly
nonempty root relation, preferably through a bounded-adhesion or
palette-private MMM recursion.  Without such a theorem, “carry the whole
feasible relation” is an exact algorithmic reformulation, not yet an
all-dimension proof.

## 6. Audit

Run

```text
python3 scratch/audit_catalan_feasible_decoration_relation_ml7_20260731.py
```

The audit reconstructs (C_0,C_1,C_2), verifies both disjoint incidence
hexagons and all Hamilton identities, enumerates every decoration in (4.4),
checks the empty triple intersection, and checks the linear-trace statement.

