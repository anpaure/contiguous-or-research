# Independent audit: q2 Pascal turn-section lift and endpoint completion

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_Q2_PASCAL_TURN_SECTION_LIFT_AND_CANONICAL_ENDPOINT_COMPLETION_20260805.md`  
**Audited theorem SHA256:**
`9052840c6f521760b8b095502b2aca6b3e71d941df25c96cae9a31eb60865227`  
**Method:** independent symbolic audit of the cyclic indices, Pascal counts,
degrees, components, palettes, endpoint roles, and residual
independent-transversal equivalence; pure mathematics, with no solver or
search  
**Verdict:** **GO after two narrow wording corrections.**  The theorem proves
exactly the displayed conditional implication.  It does not prove existence
of a q2-complete turn section.

## 1. Corrections found and incorporated

The pre-audit version had two statements that were too broad.

1. It said that every isolated A-state receives one owner containing `z` and
   one avoiding `z`.  A singleton selected run can instead be isolated by the
   deleted edges from its two neighbouring omitted runs and receive the two
   distinct A-bank owners `U_(a-1),U_a`.  The only property needed by the
   owner-path lift is that the two oriented endpoint roles receive distinct
   unused owners containing the state.  The theorem now says precisely this.
2. The conflict-graph formulation referred to all adjacent turn occurrences.
   A middle-levels Hamilton cycle may have `Y_i=Y_(i+1)`; such a pair has
   intersection rank `r-2`, not a class `D` of rank `r-3`.  The theorem now
   restricts the conflict-graph vertices to adjacent pairs with distinct turn
   labels, equivalently those whose intersection has rank `r-3`.

Neither correction changes a construction, count, or implication.

## 2. Pascal and Catalan ledger

Let

\[
 P={2r-1\choose r-1},\qquad Q={2r-1\choose r-2},\qquad
 C={1\over r+1}{2r\choose r}.
\]

Then

\[
 {Q\over P}={r-1\over r+1},\qquad {2r\choose r}=2P,
 \qquad P-Q={2P\over r+1}=C.
\]

The A- and Z-sectors of the rank-`(r-1)` child layer have orders `P` and
`Q`.  A spanning `C`-component forest on their union must have

\[
 P+Q-C=2Q
\]

edges.  The construction has exactly

\[
 |F_A|=P-C=Q,\qquad |F_Z|=Q-s,\qquad |F_{cross}|=s.
\]

The rank-`r` owner layer has `2P=2Q+2C` members.  Thus the `2Q` distinct
internal unions leave exactly `2C` endpoint owners.  All scalar identities
and both Pascal sector decompositions are correct.

## 3. Selected-turn forest, including repeated turn labels

The projected cycle edge

\[
 e_i=X_iX_{i+1}
\]

has intersection `Y_(i+1)` and union `U_i`.  At the centre `X_i`, the two
turn labels are `Y_i,Y_(i+1)`.  Consecutive labels in the original turn word
need not be distinct.  However, if `i,i+1` are both in the section `S`, then
they are distinct because `S` contains exactly one occurrence of each
`Y`-label.  They are therefore two distinct facets of `X_i`, so

\[
 Y_i\cup Y_{i+1}=X_i,\qquad |Y_i\cap Y_{i+1}|=r-3.
\]

Consequently the Z-edge at an `SS` adjacency has intersection
`z+(Y_i intersection Y_(i+1))` and union `z+X_i`.  The selected occurrence
positions biject with all Z-sector vertices.  The restriction of a proper
subset of one cycle to its selected adjacencies is one path per cyclic
selected run, including a one-vertex path when a run has length one.
Therefore `F_Z` is a spanning `s`-component linear forest with `Q-s` edges.
Distinct centres `X_i` give distinct unions, and the q2 section hypothesis is
exactly the asserted containing-`z` intersection coverage.

## 4. Exact omitted-run surgery

For a cyclic omitted run

\[
 p\in S,\quad d_1,\ldots,d_\ell\notin S,\quad
 a=d_\ell+1\in S,
\]

the ordinary representative deletion would remove

\[
 e_{d_1-1},\ldots,e_{d_\ell-1}.
\]

The theorem instead removes

\[
 e_{d_1-1},\ldots,e_{d_{\ell-1}-1},e_{d_\ell}.
\]

Thus it changes only

\[
 \text{retain }e_{d_\ell-1},\qquad
 \text{delete }e_{d_\ell}.
\]

The restored edge has intersection `Y_(d_ell)`.  The newly deleted edge has
intersection `Y_a`, and the cross edge

\[
 X_{d_\ell}--(z+Y_a)
\]

has the same intersection because `Y_a subset X_(d_ell)`.  Hence every
selected avoiding-`z` target remains covered; retaining an omitted occurrence
may introduce a duplicate label, but the theorem asserts coverage rather than
intersection injectivity.

The case `ell=1` is valid: the left list is empty, `e_(d_ell-1)` is retained,
and only `e_(d_ell)` is deleted.  The construction is cyclic-index invariant,
so a run crossing index zero gives the same local calculation.

## 5. Degrees, acyclicity, and components

The `C` omitted positions produce `C` distinct A-edge deletions.  Hence `F_A`
is a spanning `C`-component linear forest with `Q` edges.  For every omitted
run, `X_(d_ell)` has A-degree one because `e_(d_ell)` is deleted and
`e_(d_ell-1)` is retained.  The run-start Z-state has degree at most one.
The cross edge therefore raises neither endpoint above degree two.

Each Z-component is used by exactly one cross edge, at its initial endpoint.
Before that edge it is disjoint from the A-side, so adding the edge cannot
make a cycle even if several different Z-components attach to the same
A-component.  Starting from `C+s` components and adding `s` such joins leaves
exactly `C` components.  This remains valid for one selected cyclic run
(`s=1`) and for a selected run of length one.

## 6. Union injectivity and intersection coverage

The A-edge unions are distinct members of the `U_i` bank.  The containing-`z`
unions have the following mutually exclusive cyclic adjacency types:

* an `SS` index `i` supplies the Z-edge union `z+X_i`;
* a `DS` index `d_ell` supplies the cross-edge union `z+X_(d_ell)`.

The types are disjoint, the `X_i` are distinct, and the A-bank avoids `z`.
Thus every edge union is distinct.

The Z-intersection bank is complete by the q2 section condition.  On the
A-side, the run calculation in Section 4 replaces only the selected
occurrence `Y_a` by an omitted occurrence and then restores `Y_a` on the cross
edge.  Therefore every avoiding-`z` rank-`(r-2)` target remains represented.
No intersection-once assertion is required or proved.

## 7. Endpoint roles and canonical owners

One omitted run of length `ell` leaves the A-bank owners

\[
 U_{d_1-1},\ldots,U_{d_{\ell-1}-1},U_{d_\ell}
\]

unused.  Its unused Z-bank indices are the `SD` and `DD` indices

\[
 p,d_1,\ldots,d_{\ell-1},
\]

so the unused Z-bank owners are

\[
 z+X_p,z+X_{d_1},\ldots,z+X_{d_{\ell-1}}.
\]

These are `2ell` distinct owners.  The run leaves `2ell-1` unconsumed
A-endpoint roles after the cross attachment and one terminal Z-endpoint role.
The theorem assigns:

* `z+X_p` to the terminal role at `z+Y_p`;
* `z+X_j` to the right role at `X_j` for
  `j=d_1,...,d_(ell-1)`;
* `U_(j-1)` to the other role of each corresponding deleted left edge; and
* `U_(d_ell)` to the role at `X_a` of the right deleted edge.

Every containment is literal, and the cyclic index banks for different runs
are disjoint.  Consecutive deleted edges can make one physical A-state carry
two oriented endpoint roles; they receive distinct indexed owners.  In
particular:

* an isolated A-state inside one left deletion block receives one Z-bank and
  one A-bank owner;
* a singleton selected run isolated by its neighbouring deletions can receive
  the two distinct A-bank owners `U_(a-1),U_a`;
* an isolated Z-state has one cross attachment and one remaining endpoint
  role.

Hence all `2C` roles are assigned bijectively to all `2C` unused owners.

Along a nontrivial state path, use edge unions at internal owner positions and
the assigned owners at its two ends.  Two consecutive distinct rank-`r`
owners containing the same rank-`(r-1)` state intersect exactly in that state.
For a one-vertex state path, the two role owners are distinct by the preceding
bijection.  Therefore every component lifts, and all rank-`r` owners occur
exactly once globally.

## 8. Exact audit of the residual section gate

Equations (5.1) select exactly one occurrence from each turn-label class.
Given (5.1), an adjacent witness survives exactly when `x_i x_(i+1)=1`, so
(5.2) is precisely q2 coverage.

For the independent-transversal form, retain only adjacent pairs with
distinct endpoint labels.  Give such a pair the unique class

\[
 D=Y_i\cap Y_{i+1}\in{\Gamma\choose r-3}.
\]

Two witness pairs conflict exactly when they force two different occurrence
indices from one `Y`-label class.  An independent transversal choosing one
witness in every `D`-class therefore forces at most one occurrence per
`Y`-class and extends arbitrarily to a full one-occurrence section.  Conversely
any q2-complete section supplies one mutually compatible witness for every
`D`.  This proves exact equivalence, not just sufficiency.

Equivalently, deleting all but one occurrence from each repeated `Y`-class
deletes exactly `P-Q=C` positions, and q2 coverage says that this deletion set
is not a vertex cover of the witness-edge graph of any `D`-colour.

## 9. Licensed scope

The corrected theorem proves

\[
 \boxed{
 \text{q2-complete odd turn section}
 \Longrightarrow
 \text{even owner-once q2-complete Catalan path factor}.}
\]

It does not prove existence of the section, any `q>=3` row, residence, a
literal lower compiler, or an all-dimensional universal word.

**Final independent verdict:** **GO**, under exactly the theorem's displayed
hypotheses and scope.
