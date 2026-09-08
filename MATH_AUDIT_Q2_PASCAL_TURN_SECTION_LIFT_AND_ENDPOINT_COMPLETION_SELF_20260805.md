# Self-audit: q2 Pascal turn-section lift and endpoint completion

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_Q2_PASCAL_TURN_SECTION_LIFT_AND_CANONICAL_ENDPOINT_COMPLETION_20260805.md`  
**Method:** independent re-derivation of every binomial count, local edge
identity, component count, palette statement, and endpoint-owner assignment;
no computation, search, or solver  
**Verdict:** **GO**, under exactly the displayed `r>=3` and q2-complete
turn-section hypotheses.  No existence claim for the turn section is
licensed.

## 1. Binomial ledger

Put

\[
 P={2r-1\choose r-1},\quad Q={2r-1\choose r-2},\quad
 C={1\over r+1}{2r\choose r}.
\]

Since

\[
 {Q\over P}={r-1\over r+1},\qquad
 {2r\choose r}=2P,
\]

one has

\[
 P-Q={2P\over r+1}=C.
\]

The rank-`(r-1)` child layer has order

\[
 {2r\choose r-1}=P+Q=2P-C.
\]

A `C`-component spanning forest on this layer must therefore have

\[
 P+Q-C=2Q
\]

edges.  This agrees with the theorem's three edge banks:

\[
 |E(F_A)|=P-C=Q,qquad |E(F_Z)|=Q-s,qquad
 |E_{cross}|=s.
\]

The total rank-`r` owner bank has order

\[
 {2r\choose r}=2P=2Q+2C.
\]

Thus `2Q` internal union owners leave exactly `2C` endpoint owners.  Every
global scalar identity in the theorem is correct.

## 2. Middle-level indexing

Write the Hamilton cycle as

\[
 X_i,U_i,X_{i+1},\qquad U_i=X_i\cup X_{i+1}.
\]

Its projected A-edge is

\[
 e_i=X_iX_{i+1},qquad e_i\text{ has lower colour }Y_{i+1},
\]

where

\[
 Y_i=X_{i-1}\cap X_i.
\]

The turn edge centred at `X_i` joins `Y_i` to `Y_(i+1)`.  If both
occurrences are selected, they are distinct: the section selects only one
occurrence of any one `Y`-label.  They are two distinct rank-`(r-2)`
facets of the rank-`(r-1)` set `X_i`; hence

\[
 Y_i\cup Y_{i+1}=X_i,qquad |Y_i\cap Y_{i+1}|=r-3.
\]

Therefore its lifted Z-edge has union `z+X_i` and intersection
`z+(Y_i intersection Y_(i+1))`.  Distinct turn indices have distinct
centres `X_i`, so all retained Z-unions are distinct.

## 3. One omitted-run audit

Fix the cyclic local pattern

\[
 p\in S,quad d_1,\ldots,d_\ell\notin S,quad
 a=d_\ell+1\in S,qquad p=d_1-1.
\]

All indices below are cyclic.  The theorem deletes

\[
 e_{d_1-1},e_{d_2-1},\ldots,e_{d_{\ell-1}-1},e_{d_\ell}.
\]

There are `ell-1` left-block edges and one right-boundary edge, hence
exactly `ell` deletions.  The ordinary one-occurrence deletion would have
deleted

\[
 e_{d_1-1},\ldots,e_{d_\ell-1}.
\]

Thus the surgery changes only

\[
 \text{retain }e_{d_\ell-1},qquad
 \text{delete }e_{d_\ell}.
\]

The retained edge has lower colour `Y_(d_ell)`.  The newly deleted edge
has lower colour `Y_a`, and the cross edge

\[
 X_{d_\ell}--(z+Y_a)
\]

also has lower colour `Y_a`.  Hence the run surgery preserves every
avoiding-`z` lower target represented by the section.

The endpoint `X_(d_ell)` is safe for the cross edge: `e_(d_ell)` was
deleted but `e_(d_ell-1)` was explicitly retained, so its A-degree is one.
The vertex `z+Y_a` is the first vertex of one selected run and hence has
Z-degree zero or one.  The cross edge raises both degrees by one but never
above two.

Different omitted runs have distinct run-starts, last omitted positions,
Z-components, and A-owner endpoints.  Adding their cross edges one by one
always joins a previously unattached Z-component to an A-containing
component.  Even if two cross edges use the two ends of one A-path, each
still joins different current components and no cycle is created.

## 4. Component and palette audit

Deleting `C>=1` distinct edges from the A-cycle gives exactly `C` path
components, including isolated vertices as one-vertex paths.  The selected
positions form `s` cyclic runs, so `F_Z` has exactly `s` path components.
Each of the `s` cross edges joins one different Z-component to the A-side.
Thus the final component number is

\[
 C+s-s=C.
\]

The avoiding-`z` union colours are a subset of the distinct `U_i`.  The
containing-`z` colours used by Z-edges correspond to binary adjacencies
`SS`; those used by cross edges correspond to `DS`.  A cyclic adjacency
has only one type, so these two index banks are disjoint.  Their centres
`X_i` are distinct.  The two Pascal union sectors are disjoint because one
contains `z` and one does not.  Therefore every edge union is distinct.

The avoiding-`z` lower palette is preserved by the calculation in Section
3.  The containing-`z` lower palette is complete exactly by the section
hypothesis

\[
 \forall D\in{\Gamma\choose r-3}\quad
 \exists i,i+1\in S:\ Y_i\cap Y_{i+1}=D.
\]

No stronger conclusion is used.

## 5. Endpoint roles and unused colours per omitted run

For one omitted run of length `ell`, the unused avoiding-`z` owners are

\[
 U_{d_1-1},\ldots,U_{d_{\ell-1}-1},U_{d_\ell},
\]

exactly `ell` colours.  The `z`-containing turn labels have these binary
types:

* `SD` at centre `X_p`;
* `DD` at centres `X_(d_1),...,X_(d_(ell-1))`;
* `DS` at centre `X_(d_ell)`.

Only `SS` and `DS` are used internally/crosswise.  Hence the unused
containing-`z` colours are

\[
 z+X_p,z+X_{d_1},\ldots,z+X_{d_{\ell-1}},
\]

also exactly `ell` colours.

On the Z-side, the selected run ending at `Y_p` contributes one unjoined
endpoint role.  It is contained in `z+X_p`.

On the A-side, the left deleted block has `ell-1` edges and therefore
`2(ell-1)` endpoint roles.  For each
`j=d_1,...,d_(ell-1)`, assign

\[
 U_{j-1}\text{ to the role at }X_{j-1},\qquad
 z+X_j\text{ to the role at }X_j.
\]

At an internal isolated vertex of a consecutive deletion block these are
the two different endpoint roles, one facing each missing edge.  The right
deleted edge has roles at `X_(d_ell)` and `X_a`; the cross consumes the
first, and `U_(d_ell)` is assigned to the second.  The A-side therefore
uses exactly

\[
 2(ell-1)+1=2ell-1
\]

roles and colours.  Together with the one Z-role, the run contributes
`2ell` endpoint roles and all `2ell` unused owners.

If a selected run has length one, one physical vertex may carry two
endpoint roles belonging to the omitted gaps on its two sides.  The
assignments above use the two oriented roles separately.  If an A-owner is
isolated by deletions from the two neighbouring gap blocks, the same
oriented-role convention applies.  Thus shared physical vertices do not
cause a collision of endpoint **occurrences**.

Summing over omitted runs gives `2C` roles and `2C` owners.  Cyclic indices
partition the colour banks, so the assignments are injective.  Every
assignment is a literal containment.  This proves the endpoint-owner
bijection.

## 6. Owner-path lift

For a final state path

\[
 L_1-L_2-\cdots-L_t,
\]

put the matched endpoint owners at the two ends and put
`L_i union L_(i+1)` at every internal owner position.  Adjacent owners are
distinct rank-`r` supersets of the same rank-`(r-1)` state `L_i`; therefore
their intersection is exactly `L_i`.  Internal owners are pairwise
distinct by union injectivity, endpoint owners are the complementary bank,
and the endpoint assignment is bijective.  Hence every rank-`r` owner
occurs exactly once.

For a one-vertex path, the two endpoint roles receive two distinct missing
owners containing that state.  In the explicit assignment, any isolated
A-state gets distinct oriented colours, and an isolated Z-state receives
one cross attachment plus one remaining endpoint owner.  Thus the lift is
also valid in all degenerate path-length cases.

## 7. Audit of the residual section gate

The equations

\[
 \sum_{i:Y_i=Y}x_i=1
\]

are exactly the one-occurrence section condition.  Given them, an adjacent
edge `(i,i+1)` is retained exactly when `x_i x_(i+1)=1`, so the covering
inequalities in the theorem are exactly the q2 condition, with no
relaxation.

For the conflict-graph reformulation, two selected witness edges are
compatible precisely when every common `Y`-label is represented by the
same occurrence position.  Compatible witnesses therefore force at most
one occurrence in each `Y`-class and extend arbitrarily to a full section.
Conversely a full section supplies compatible witnesses for every covered
`D`-class.  Hence the independent-transversal statement is equivalent,
not merely sufficient.

## 8. Licensed conclusion and exclusions

The proof licenses the implication

\[
 \boxed{
 \text{q2-complete odd turn section}
 \Longrightarrow
 \text{even owner-once q2-complete Catalan path factor}.}
\]

It does not license existence of the turn section, q3 or higher rows,
residence, a literal lower compiler, or an all-`k` OR word.  The theorem's
status line and Scope section state all five exclusions explicitly.

**Final self-audit verdict:** GO.
