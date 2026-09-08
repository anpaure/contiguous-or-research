# Audit of the repair-first private ECO composition gate

Date: 2026-07-31  
Status: exact theorem-scope audit and corrected conditional composition
theorem; no all-dimension repair or compatible-ECO-hypertree existence claim

## 0. Verdict

The correct implication is post-repair and occurrence-labelled:

\[
\begin{split}
 &\text{prepared factor }F^*+\text{a component-faithful ECO incidence
 hypertree}\ \\
 &\quad+\text{one joint owner-aligned decoration}
 +\text{one simultaneous occurrence linkage} \\
 &\hspace{35mm}\Longrightarrow
 \text{one connected factor carrying that decoration}.             \tag{0.1}
\end{split}
\]

This implication is exact once the hypotheses below are made literal.  Four
scope separations are load-bearing.

1. The upper-turn transversal consists of the **lower-shore** occurrences
   \(L_a,L_b,L_c\).  The forced lower-colour representatives occur at the
   **upper-shore** ports \(U_{ab},U_{bc},U_{ca}\), with the cyclicly shifted
   owners in (1.2) below.
2. Pairwise compatibility is insufficient.  An arbitrary-order theorem
   needs one subsetwise literal Boolean cube and subsetwise component
   faithfulness.  A prescribed-order theorem needs the corresponding
   assertions only on its prefixes.
3. One simultaneous named route per atom is enough for a fixed execution.
   The weight \(r_t-1\) and a kill-cost lower bound enter only when one also
   claims router resilience under deletions.
4. The ECO family must be chosen on the repaired factor, or its complete
   decorated transition signature must be transported through the repair.
   It is not without loss of generality to preserve a raw canonical ECO
   tree.

The new fixed-rotation collision theorem is useful but stops strictly before
(0.1): an independent set in its path forest simultaneously removes physical
port repetitions and the two local forced-owner repetitions.  It does not
imply global turn-palette surjectivity, existence of the upper transversal,
distinct gap owners, owner alignment, an incidence hypertree, or occurrence
routing.

The raw \(m=5\) census makes this boundary sharp.  All 648 canonical minimal
ECO Hamiltonizing sequences already have disjoint physical ports and disjoint
forced faces, yet every endpoint misses the same three upper and three lower
period-three colours.  Thus no upper transversal exists.  The order

\[
 \boxed{\text{controlled repair/rethread}\ \longrightarrow\
        \text{collision-free ECO hypertree}\ \longrightarrow\
        \text{owner-aligned residual Hall}\ \longrightarrow\
        \text{private/laminar occurrence routing}}                 \tag{0.2}
\]

is not cosmetic.  The middle two choices may be co-designed, but neither may
be inferred from the raw collision-free catalogue.

## 1. Owner-shore and cyclic-owner audit

For an ECO atom write

\[
\begin{array}{lll}
 L_a=H+a,&L_b=H+b,&L_c=H+c,\\
 U_{ab}=H+a+b,&U_{bc}=H+b+c,&U_{ca}=H+c+a .
\end{array}                                                       \tag{1.1}
\]

Let \(I\) be an upper-turn transversal, represented by its literal
lower-shore occurrences.  Hence the selected upper occurrences required by
this atom are

\[
                         L_a,L_b,L_c\in I.                         \tag{1.2a}
\]

Let \(g_{ab},g_{bc},g_{ca}\) be the \(I\)-gaps containing the lower-turn
occurrences at \(U_{ab},U_{bc},U_{ca}\).  With common external upper-delete
label \(e\), the forced gap--colour edges are

\[
 F_t=\{(g_{ab},H-e+b),\ (g_{bc},H-e+c),\ (g_{ca},H-e+a)\}.         \tag{1.2b}
\]

The cyclic shift in (1.2b) follows from the old matching phase

\[
                 L_aU_{ca},\qquad L_bU_{ab},\qquad L_cU_{bc}.     \tag{1.3}
\]

It may not be replaced by the unshifted pointwise assignment.  If the
gap--lower-colour graph \(\Gamma_I\) is a forest with perfect matching
\(M\), the exact owner test is

\[
                 \{L_a,L_b,L_c\}\subseteq I,
                 \qquad F_t\subseteq M.                           \tag{1.4}
\]

For a family \(\mathcal T\), the union \(F=\bigcup_tF_t\) must itself be a
matching.  The condition \(F\subseteq M\) then proves the simultaneous
extension.  On a nonforest gap graph, (1.4) must be replaced by the exact
vertex-disjoint alternating-cycle criterion; forced-colour injectivity alone
does not suffice.

Consequently the sentence “the three upper ports lie in \(I\)” is unsafe:
the literal members of \(I\) are the three \(L\)-ports.  The three
\(U\)-ports provide the forced lower occurrences.

## 2. The exact subsetwise state

Let \(F^*\) be the prepared post-repair degree-two factor.  For every selected
atom \(t\), let \(O_t\) and \(N_t\) be its declared old and new three-edge
matchings.  A **decorated common cube** is a family indexed by every
\(X\subseteq\mathcal T\), consisting of a literal factor \(F_X\), a transported
decoration \(D_X\), and protected auxiliary state, with the following
properties.

1. \(F_\varnothing=F^*\), and \(F_X\) is the literal simultaneous toggle of
   \((O_t,N_t)\) for \(t\in X\).  Every \(F_X\) is a simple spanning
   degree-two factor.
2. For every \(t\notin X\), its declared old/new matching phase, all six
   port occurrences, its external neighbours and common labels \((d_t,e_t)\)
   are still the declared ones in \(F_X\).  Thus the next toggle remains
   physically available and coherent.
3. \(D_X\) is the literal transparent transport of one occurrence-labelled
   decoration: it contains the prescribed ports, uses the declared owner
   edges, and preserves the protected turn colours.  This is stronger than
   equality of unlabelled colour multisets.
4. If \(\mathcal V\) is the component set of \(F^*\), the component partition
   of \(F_X\) is exactly the connected-component partition of the incidence
   graph on \(\mathcal V\cup X\).  Isolated vertices of \(\mathcal V\) are
   retained.  This is component faithfulness.
5. Every claimed gap, trace, reachability, residence, deeper-shadow,
   socket/voltage or compiler invariant is supplied as part of this same
   subset-indexed state, rather than inferred from pairwise disjointness.

Pairwise vertex-disjoint atoms often make item 1 automatic, but do not make
items 3--5 automatic.  Conversely, if only one fixed ordering
\(t_1,\ldots,t_s\) is needed, it is sufficient to provide this state on the
prefixes \(\{t_1,\ldots,t_j\}\).  That weaker certificate proves no
arbitrary-order statement.

If the bipartite incidence graph \(B(\mathcal V,\mathcal T)\) is a tree and
\(r_t\) is the number of distinct base components incident with \(t\), then

\[
                     \sum_{t\in\mathcal T}(r_t-1)=|\mathcal V|-1. \tag{2.1}
\]

Component faithfulness implies that every order is component-progressing,
and the full toggle is connected.

## 3. Fixed execution theorem

### Theorem 3.1 (repair-first fixed ECO execution)

Assume the following data are given on a prepared factor \(F^*\).

1. A selected ECO family \(\mathcal T\) whose incidence graph is a tree and
   which has the decorated common cube of Section 2 (or the prefix version
   for one declared order).
2. One upper transversal \(I\) and one gap perfect matching \(M\).  On the
   forest face, every selected atom obeys (1.4); off the forest face, the
   union of forced edges is carried by one explicitly specified perfect
   matching obtained through vertex-disjoint alternating cycles.
3. One simultaneous occurrence realization for all selected atoms.  For
   example, it suffices to give each atom a distinct protected source and a
   distinct protected sink, together with pairwise internally
   vertex-disjoint named source--sink routes, and to verify that the atomic
   transfer is executable along those routes.

Then toggling all atoms produces one connected factor carrying the same
joint decoration and all protected invariants included in the common cube.

#### Proof

The owner condition installs every selected lower representative in the
same gap perfect matching, while the \(L\)-ports belong to the same upper
transversal.  The decorated common cube therefore transports the decoration
through every toggle.  Equation (2.1) and component faithfulness give one
component at the endpoint.  The simultaneous occurrence realization
executes all atomic transfers without a resource collision.  No deletion
claim is used.  \(\square\)

In particular, one route per ternary atom is enough in Theorem 3.1.  Arity
three is not a fixed-execution obstruction.

## 4. The separate deletion-resilient theorem

For deletion robustness, work in an explicit atomic-availability model.
Give atom \(t\) weight

\[
                              w_t=r_t-1.                         \tag{4.1}
\]

Its private bank \(R_t\) contains every **internal deletable** router vertex
which can affect that atom.  The banks are disjoint.  Atom sources and its
dedicated sink terminals are protected, excluded from every deletion set,
and distinct across atoms.  Availability of \(t\) depends only on
\(Y\cap R_t\).  Let \(t\) be dead when no complete atomic occurrence
transfer remains, and put

\[
 \kappa_t=\min\{|Y\cap R_t|:t\text{ is dead}\},                  \tag{4.2}
\]

with \(\kappa_t=\infty\) if the atom cannot be killed internally.

Deleting dead atom vertices from the selected incidence tree gives the
exact identity

\[
 c(\mathcal H_Y)-1=\sum_{t\text{ dead}}w_t.                       \tag{4.3}
\]

Here \(\mathcal H_Y\) is the selected atomic skeleton only.  Extra catalogue
connections can reduce its component count, so (4.3) is not an identity for
an unspecified larger router graph.

Under the private-bank hypotheses,

\[
                           \kappa_t\ge w_t\quad(t\in\mathcal T)   \tag{4.4}
\]

is sufficient for

\[
                           c(\mathcal H_Y)\le |Y|+1               \tag{4.5}
\]

for every internal deletion set.  It is also necessary for robustness of
this isolated atomic skeleton: choose a minimum kill set inside one bank;
all other atoms remain available, and (4.3) gives
\(c-1=w_t>\kappa_t=|Y|\) if (4.4) fails.

Protected-terminal Menger theory may certify (4.4) only in the special case
where the atom remains executable whenever any one complete source--sink
route survives.  Then \(w_t\) internally vertex-disjoint routes give
\(\kappa_t\ge w_t\).  If a source or sink is deletable, one deletion may kill
all routes.  If an atomic transfer requires several simultaneous subroutes,
ordinary one-source Menger connectivity is not its kill criterion.

Thus a ternary atom needs kill cost two only for (4.5).  A single named route
still proves the fixed execution of Theorem 3.1.

## 5. What a preliminary repair must preserve

There are two different, exact interfaces.

### 5.1 Repair-first recomputation (the live route)

No raw ECO atom need survive.  The repair must output a literal factor
\(F^*\) on which the following are freshly verified:

1. complete enough upper and lower turn-occurrence palettes to supply the
   chosen upper transversal and its gap perfect matching;
2. the actual post-repair ECO atoms, including their old/new matchings,
   external neighbours, common labels and component supports;
3. a collision-free incidence hypertree with the decorated common cube;
4. owner alignment or the exact residual alternating-cycle matching; and
5. one simultaneous private/laminar occurrence realization.

Only downstream invariants claimed in the conclusion—residence, deeper
shadows, sockets/voltage and compiler state—must additionally be included in
the common state.  This interface is the one consistent with the raw
\(m=5\) obstruction.

### 5.2 Transport of a preselected family (a sufficient subclass)

If one insists on carrying a named family through a repair, the repair must
preserve, for every selected atom, the complete decorated transition
signature

\[
 \Sigma_t=(\text{six occurrence addresses};O_t,N_t;
 \text{external neighbours};H,a,b,c,d,e;
 \text{old/new phase};F_t;\text{router terminals and bank}).     \tag{5.1}
\]

It must also preserve the family-level data:

* the subsetwise literal factor/decoration cube;
* the subsetwise component partition, not merely each individual component
  effect;
* the actual \(I\)-gap addresses and matching owners of the \(U\)-ports;
* the simultaneous route linkage, or the stronger kill-cost data if
  robustness is claimed; and
* every protected downstream invariant used later.

Preserving the six port vertices and common labels alone is insufficient:
a remote rethread may change their external neighbours, their cyclic gaps,
the matching phase or component interleaving.  Conversely, preserving
(5.1) is only a sufficient transport condition, not a without-loss-of-
generality normalization.  A successful repair may have to destroy the raw
tree and create a new one.

## 6. Exact effect of the new ECO collision and counterexample theorems

For one fixed rotation of the canonical ECO catalogue, the physical-port,
lower-owner and upper-owner collision graphs are the same path forest

\[
                  1p100v\longrightarrow 1p010v,                  \tag{6.1}
\]

with \(\operatorname{Cat}_{n-2}\) edges.  Hence one independent set removes
all three kinds of local repetition simultaneously.  This is a genuine
three-for-one conflict compression.

It does not prove that the retained component hyperedges contain an
incidence hypertree; independence may disconnect the component two-section.
Even if a hypertree survives, it does not manufacture missing global turn
colours.  At raw project \(m=5\), every one of the 648 topology-safe minimal
ECO sequences is already collision-free but has palette sizes \(81<84\) on
both shores, with missing orbits

\[
 \mathcal R^+=\{219,365,438\},\qquad
 \mathcal R^-=\{73,146,292\}.                                   \tag{6.2}
\]

Thus the smallest exact obstruction is before residual Hall: there is no
upper transversal.  Any theorem whose antecedent begins with the raw
canonical ECO hypertree and then asserts existence of its decoration is
false.  The surviving target is a **repair-conditioned independent
hypertree** selected jointly with the post-repair decoration.

## 7. Replay against the rewritten AD theorem

The rewritten
`MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md`, audited at
SHA-256

```text
1af842f094a30dd50696f73c1c357a01b669dfb44a5bdddee7c4f35d033c6cb9
```

passes every load-bearing scope check in this audit.

1. Equations (1.4)--(1.6) use the correct shores and the correct cyclic
   owner assignment: \(I\) contains the \(L\)-ports, while the forced lower
   occurrences lie at the \(U\)-ports.
2. Definition 5 requires a literal common cube on every subset, component
   faithfulness on every subset, preservation of the occurrence-labelled
   decoration and protected state, and one subset-closed simultaneous
   occurrence realization.  Thus pairwise compatibility is not being used
   as a surrogate for the global cube.
3. Theorem 5.1 is a fixed-execution statement and explicitly needs only one
   named private route per atom, including a ternary atom.  Theorem 6.2 is a
   separate deletion-resilience theorem with exact weight \(r_t-1\).
4. Section 6 restricts deletions to internal unprotected vertices, uses
   complete disjoint failure banks, and scopes necessity to the bare selected
   incidence-tree backbone.  It does not claim that the private-bank normal
   form is necessary in a larger catalogue.
5. Proposition 7.1 records the full transition signature needed to transport
   a preselected family and then states the safer general rule: repair first
   and recompute the atoms, owners and routes.
6. Section 8 incorporates the raw project-\(m=5\) no-transversal theorem and
   correctly labels the finite ECO hypertrees as static all-at-once evidence,
   not subsetwise-cube certificates.
7. The path-tiling integrality theorem and its branching determinant-two
   obstruction are independent of the owner/router conclusions and are
   correctly scoped to a prefiltered mutually compatible bank.

No substantive or remaining scope failure was found.  The final rewrite also
closes the two minor ambiguities found in the penultimate audit: it defines
\(\lambda_t=\infty\) for an internally unkillable atom and distinguishes the
one-way Menger lower bound from equality; and it requires distinct protected
sources as well as sinks and carries both terminals in the transport
signature.

## 8. Proved and open boundary

Proved here, from the frozen antecedent theorems:

1. the exact shore convention and cyclic owner map (1.2);
2. the minimal subsetwise state needed for arbitrary-order composition;
3. fixed execution under one simultaneous occurrence linkage;
4. the exact, separate private-bank kill-cost criterion for deletion
   resilience; and
5. the two correct preliminary-repair interfaces.

Still open:

1. an all-\(m\) controlled repair which restores the required palette and
   deeper protected state;
2. after that repair, a collision-independent ECO subfamily which is also an
   incidence hypertree;
3. one post-repair upper transversal and residual lower matching owning its
   forced ports;
4. a simultaneous node-private or laminar occurrence linkage; and
5. residence, all-depth shadow, socket/voltage and compiler closure in the
   same prepared state.

The sharp remaining obstruction is therefore not coherent ECO abundance.
It is the integral correlation of repair, independent hypertree selection,
owner alignment and occurrence routing.

## 9. Dependencies

* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`
* `MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md`
* `MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md`
* `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`
