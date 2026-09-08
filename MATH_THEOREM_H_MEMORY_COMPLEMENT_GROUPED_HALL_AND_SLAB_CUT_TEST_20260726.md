# \(H\)-memory grouped Hall with complement symmetry: endpoint closure, alternating augmentations, and the slab test of the mixed-profile cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Use the exact one-sided target

\[
 \mathfrak H
 =\sum_{q\le H,\epsilon,T}(1-L_q^\epsilon(T))_+,
\tag{0.1}
\]

or equivalently the full linear repeat excess from
MATH_AUDIT_CPCR_ONE_SIDED_L1_WEAKENING_20260726.md. The chronology state
space is the \(H\)-memory de Bruijn automaton from
MATH_THEOREM_N_H_MEMORY_KERNEL_SHADOW_UNLOCKING_20260726.md.

This note proves four exact statements.

1. A grouped collection of owner-disjoint safe path blocks is an
   \(H\)-state-valid owner successor exactly when its total endpoint
   boundary vanishes. If groups and options are closed under coordinate
   complementation, selecting complement-paired options gives exact
   lower/upper complement symmetry.
2. For an endpoint-separated connector catalogue, complement symmetry
   reduces the closure problem to a perfect matching on complement
   orbits. Ordinary Hall is necessary and sufficient. Any two closures
   differ by alternating cycles in that quotient graph.
3. A group replacement is a legal \(L^1\) augmentation exactly when its
   whole group differences have zero memory boundary, are complement
   closed, and cover more common-background zeros than the old groups.
   Reversing the removed memory arcs turns every legal difference into an
   Eulerian residual circulation, but its cycle decomposition is not
   automatically group-valid.
4. Cross-parent \(Q_{R+1}\)-slab choices do invalidate the static
   mixed-profile \(1/2\)-cut as a formal state invariant: each complete
   old/new slab resolution is already a zero-boundary \(H\)-memory
   circuit, and it may change the literal target neighborhood. However,
   the audited slab theorem supplies no expansion or augmenting-path
   abundance on the cut's zero set. It therefore does not prove that a
   linear cut can be beaten.

This last insufficiency is exact. Two complement-symmetric abstract
automata can have the same endpoint graph, the same two-state
cross-parent option pattern, equal option masses, and zero boundary in
every option, while one retains a \(1/2\)-hole cut in every state and the
other has a zero-hole state. Thus endpoint connectivity, complement
symmetry, Hamming-two parent reachability, and option mass do not decide
the target question.

The minimal positive statement is an **augmenting-union theorem**: every
state with \(\Omega(W)\) holes must admit a complement-closed,
owner-disjoint family of whole slab/path replacements whose endpoint
boundary is zero and whose new target union covers more of the common
background zero set by a quantitatively linear amount. This is a
state-valid grouped theorem, not ordinary raw Hall.

## 1. The \(H\)-memory automaton and complement

Let \(\Gamma_H\) be the safe Johnson paths

\[
                         \gamma=(X_0,\ldots,X_H).
\tag{1.1}
\]

The memory-state set is

\[
 \Sigma_{H-1}
 =\{(X_0,\ldots,X_{H-1}):
      (X_0,\ldots,X_{H-1})\text{ is safe}\}.
\tag{1.2}
\]

Every \(\gamma\) is a directed automaton arc

\[
 \operatorname{pre}\gamma=(X_0,\ldots,X_{H-1})
 \longrightarrow
 \operatorname{suf}\gamma=(X_1,\ldots,X_H).
\tag{1.3}
\]

Let \(A\) be the root matrix and \(M\) the state-incidence matrix

\[
 A_{X,\gamma}={\bf1}_{\{X_0=X\}},
\qquad
 M_{\sigma,\gamma}
 ={\bf1}_{\{\operatorname{pre}\gamma=\sigma\}}
  -{\bf1}_{\{\operatorname{suf}\gamma=\sigma\}}.
\tag{1.4}
\]

Thus \(Mz=0\) is exact endpoint balance. With the sign convention in
(1.4), the boundary of a directed path from \(\sigma\) to \(\tau\) is
\(e_\sigma-e_\tau\).

Coordinate complementation defines fixed-point-free involutions

\[
 \bar X=[2m]\setminus X,\qquad
 \bar\gamma=(\bar X_0,\ldots,\bar X_H),\qquad
 \bar\sigma=(\bar X_0,\ldots,\bar X_{H-1}).
\tag{1.5}
\]

It preserves arc direction:

\[
 \operatorname{pre}\bar\gamma
   =\overline{\operatorname{pre}\gamma},
\qquad
 \operatorname{suf}\bar\gamma
   =\overline{\operatorname{suf}\gamma}.
\tag{1.6}
\]

The signed traces satisfy

\[
 L_q(\bar\gamma)=[2m]\setminus U_q(\gamma),
\qquad
 U_q(\bar\gamma)=[2m]\setminus L_q(\gamma).
\tag{1.7}
\]

Hence a complement-invariant path selection has exact typed symmetry

\[
 L_q^-(T)=L_q^+([2m]\setminus T).
\tag{1.8}
\]

## 2. Grouped path blocks and the exact endpoint theorem

Partition the retained owner roots into owner-disjoint groups
\(\mathcal O_g\), closed under a group involution
\(g\mapsto\bar g\). For every option \(\omega\in\Omega_g\), let

\[
                         z_{g,\omega}\in
 \mathbb Z_{\ge0}^{\Gamma_H}
\tag{2.1}
\]

be a union of safe directed automaton paths satisfying

\[
                         Az_{g,\omega}
                         ={\bf1}_{\mathcal O_g}.
\tag{2.2}
\]

Its endpoint boundary is

\[
                         b_{g,\omega}=Mz_{g,\omega}.
\tag{2.3}
\]

Assume the catalogue is complement closed:

\[
 z_{\bar g,\bar\omega}=\overline{z_{g,\omega}},
\qquad
 b_{\bar g,\bar\omega}=\overline{b_{g,\omega}}.
\tag{2.4}
\]

One deterministic grouped selection is

\[
                         z(\boldsymbol\omega)
 =\sum_gz_{g,\omega_g}.
\tag{2.5}
\]

### Theorem 2.1 (state-valid complement-symmetric endpoint/path cover)

Suppose the owner groups partition the retained owner set.

1. The selection (2.5) is an integral \(H\)-safe owner successor if and
   only if

   \[
                         \sum_gb_{g,\omega_g}=0.
   \tag{2.6}
   \]

2. It is complement invariant if and only if, on every two-element group
   orbit,

   \[
 z_{\bar g,\omega_{\bar g}}
 =\overline{z_{g,\omega_g}}.
   \tag{2.7}
   \]

   In a catalogue with duplicate option columns identified, this is
   \(\omega_{\bar g}=\bar\omega_g\). A self-complementary compound group
   must use an invariant option.
3. Under (2.6), the selected path blocks concatenate into directed memory
   cycles. Under (2.7), those cycles and their trace loads occur in
   complement orbits and satisfy (1.8).

#### Proof

Equation (2.2) and the owner partition give

\[
                         Az(\boldsymbol\omega)
                         ={\bf1}.
\]

By (2.3),

\[
                         Mz(\boldsymbol\omega)
                         =\sum_gb_{g,\omega_g}.
\]

The \(H\)-memory overlap theorem says that a nonnegative integral path
vector with \(Az={\bf1}\) is an owner successor exactly when \(Mz=0\).
This proves the first assertion. A finite directed multigraph with equal
indegree and outdegree at every vertex decomposes into directed cycles,
proving the third assertion without complement.

Condition (2.7) is exactly invariance of the selected column vector under
the involution (2.4). Equations (1.7)--(1.8) then give the stated trace
symmetry. \(\square\)

The theorem separates two constraints which must not be conflated.
Owner-disjointness gives \(Az={\bf1}\); it does not give endpoint balance.
Complement pairing gives (1.8); it also does not give endpoint balance.

## 3. Exact Hall theorem for an endpoint-separated connector atlas

There is one useful case in which endpoint closure is genuinely an
ordinary Hall problem.

Start with a complement-paired family of owner-disjoint open path blocks.
Let \(\mathcal E^+\) be the multiset of their head endpoints and
\(\mathcal E^-\) the multiset of their tail endpoints. Assume
complementation acts freely on both multisets.

A connector orbit consists of a safe connector path from
\(h\in\mathcal E^+\) to \(t\in\mathcal E^-\), together with its
complement path from \(\bar h\) to \(\bar t\). Assume:

1. every connector orbit has a reserved owner set disjoint from the base
   paths and from every other connector orbit which may be selected with
   it;
2. selecting endpoint-disjoint connector orbits is sufficient for owner
   disjointness; and
3. every connector option is a whole common all-depth path block; and
4. every perfect endpoint matching uses, together with the fixed base
   paths, one fixed partition of the retained owner roots. For example,
   the connector owner group may be attached to its head orbit and be
   independent of the chosen tail orbit.

Call this an **endpoint-separated atlas**. Form the bipartite quotient
graph

\[
 \mathcal K^\complement
 =(\mathcal E^+/\complement,\mathcal E^-/\complement;E),
\tag{3.1}
\]

where one edge is one complement orbit of legal connectors.

### Theorem 3.1 (complement-quotient Hall and augmenting paths)

An endpoint-separated atlas has a complement-symmetric state-valid
closure if and only if

\[
 |S|\le |N_{\mathcal K^\complement}(S)|
 \qquad
 \text{for every }
 S\subseteq\mathcal E^+/\complement.
\tag{3.2}
\]

Given a partial closure, the usual alternating-path search in
\(\mathcal K^\complement\) either augments it by one endpoint orbit or
returns a set \(S\) violating (3.2). Any two complete closures differ by
a disjoint union of even alternating cycles in
\(\mathcal K^\complement\).

#### Proof

A matching edge in the quotient selects two complementary connectors and
uses both members of one head orbit and both members of one tail orbit.
Thus a quotient perfect matching is exactly a complement-symmetric
endpoint closure. Hall's theorem gives (3.2), and its standard
alternating-path proof gives either an augmentation or a deficient set.
The symmetric difference of two perfect matchings is a disjoint union of
even alternating cycles. Lifting each quotient edge orbit restores the
two complementary connector paths, so every lifted closure satisfies
Theorem 2.1. \(\square\)

### Exact scope

The endpoint-separated hypothesis is substantive. If two connector
choices use the same slab or share a frame variable, endpoint-disjoint
matching edges may still be incompatible. The problem then becomes a
grouped hypergraph matching problem; Hall on (3.1) is no longer
sufficient. Shared slab, selector, rank-matching, and compiler variables
must be frozen first or represented as indivisible master groups.

The endpoint atlas must also be designed correlatively. The independent
per-root theorem in
MATH_THEOREM_N_H_MEMORY_NEAR_ROUNDING_AND_NESTED_HASH_GATE_20260726.md
shows that independently sampled \(H\)-windows retain at most
\(W/(m)_{H-1}^2\) roots in expectation after enforcing memory balance.
Thus Hall in (3.2) cannot be postponed until after independent local
sampling; the connector neighborhoods themselves must be built into the
common state law.

## 4. State-valid grouped augmentations and the one-sided objective

Fix a complement-symmetric state-valid selection
\(\boldsymbol\omega^0\). Let \(S\) be a complement-closed family of
owner-disjoint groups and choose alternatives \(\omega_g^1\). Put

\[
 \delta_S
 =\sum_{g\in S}
    \bigl(z_{g,\omega_g^1}-z_{g,\omega_g^0}\bigr).
\tag{4.1}
\]

Root balance is automatic:

\[
                         A\delta_S=0.
\tag{4.2}
\]

For a typed colour \(c=(q,\epsilon)\), let
\(I_{g,a,c}\) be the target support of option \(a\). Remove the old
changed groups and call the remaining load \(B_{S,c}\). Put

\[
 Z_{S,c}=\{T:B_{S,c}(T)=0\},
\tag{4.3}
\]

\[
 U_{S,c}^0=\bigcup_{g\in S}I_{g,\omega_g^0,c},
\qquad
 U_{S,c}^1=\bigcup_{g\in S}I_{g,\omega_g^1,c}.
\tag{4.4}
\]

### Theorem 4.1 (exact state-valid augmenting-circuit theorem)

The grouped replacement is a legal complement-symmetric \(H\)-memory
augmentation if and only if

\[
 \boxed{
 M\delta_S=0,\qquad
 \delta_S=\bar\delta_S,}
\tag{4.5}
\]

with the new options satisfying every additional fixed-fibre or cap row
of the chosen state model.

For every such replacement,

\[
 \boxed{
 \mathfrak H(\boldsymbol\omega^1)
 -\mathfrak H(\boldsymbol\omega^0)
 =
 \sum_c\left(
   |Z_{S,c}\cap U_{S,c}^0|
  -|Z_{S,c}\cap U_{S,c}^1|
 \right).}
\tag{4.6}
\]

Hence it is an improving augmentation exactly when the new whole-option
unions cover more common-background zeros than the old unions.

#### Proof

The group replacement preserves every root by (4.2) and remains
nonnegative because complete old options are removed and complete new
options inserted on the same owner groups. Theorem 2.1 makes
\(M\delta_S=0\) necessary and sufficient for memory-state validity.
Complement invariance is exactly the second equation in (4.5).
Additional cap or fibre equations are independent rows and must be
checked literally.

After the changed old groups are removed, a target is missing exactly
when it belongs to \(Z_{S,c}\) and lies outside the corresponding old or
new union. Subtraction gives (4.6). \(\square\)

### Residual alternating paths

Reverse every removed old automaton arc and keep every inserted new arc
forward. Equation \(M\delta_S=0\) says that this nonnegative residual
multigraph is Eulerian, so it decomposes into directed residual cycles.
These are the automaton-level alternating augmenting circuits.

There is a crucial grouping warning. A residual cycle may use only part
of a slab or compiler option. Such a cycle is not itself a legal move.
The legal augmentation is the entire family \(S\) of whole group
differences. Thus ordinary augmenting paths in the memory graph certify
endpoint balance only after group indivisibility has been checked.

Likewise, the absence of an improving single alternating cycle does not
imply global optimality. Formula (4.6) is a union score with intersections
of every order; several zero-gain or negative-gain cycles can form one
positive compound augmentation.

## 5. Cross-parent slabs in the \(H\)-memory state graph

Consider one legal \(Q_{R+1}\)-slab. Its old resolution and its new
resolution are each exact owner factors into closed diverse-order
compiler cycles. Let their \(H\)-memory column vectors be \(z_{t,0}\)
and \(z_{t,1}\). Then

\[
 Az_{t,0}=Az_{t,1}={\bf1}_{\mathcal O_t},
\qquad
 Mz_{t,0}=Mz_{t,1}=0.
\tag{5.1}
\]

Therefore

\[
 \delta_t=z_{t,1}-z_{t,0}
\quad\text{satisfies}\quad
 A\delta_t=M\delta_t=0.
\tag{5.2}
\]

When \(t\) and its coordinate complement are owner-disjoint, pairing them
gives

\[
                         \delta_t+\bar\delta_t,
\tag{5.3}
\]

an exact complement-symmetric state-valid augmenting circuit. If the slab
orbit is self-complementary, one instead needs a complement-invariant
resolution of that compound group.

Thus the \(H\)-memory endpoint equations do not remove the cross-parent
slab choices. Slabs genuinely enlarge the legal state graph by
zero-boundary cross-parent circuits. At one signed depth, a slab replaces
one image of size \(2s\), \(s=2^R\), by another. Its hole reduction is
at most \(2s\), and is exactly the one-slab instance of (4.6).

What the slab theorem does not give is a lower bound on

\[
 |Z_{t,c}\cap I_{t,1,c}|
 -|Z_{t,c}\cap I_{t,0,c}|.
\tag{5.4}
\]

Nor does Hamming-two parent-label reachability imply that many
owner-disjoint slabs have positive, weakly overlapping gains in (5.4).
The endpoint state graph is enlarged, but its target-labelled expansion
is unproved.

## 6. Test of the static mixed-profile \(1/2\)-cut

In the static graph, let \(\mathcal A\) be the ordinary target family and
\(U\) its common source reservoir:

\[
                         |\mathcal A|=2KM,\qquad
                         |U|=KM.
\tag{6.1}
\]

Every state whose target incidences remain in this fixed graph has at
least \(KM\) holes in \(\mathcal A\). Once slab choices are admitted, the
relevant exact quantity is no longer \(|N(\mathcal A)|\). It is the
maximum target union over state-valid complement-symmetric grouped
resolutions.

For a compound slab/path replacement \(S\), define its cut escape score

\[
 \operatorname{Esc}_{\mathcal A}(S)
 =\sum_c\left(
 |Z_{S,c}\cap U_{S,c}^1\cap\mathcal A_c|
 -|Z_{S,c}\cap U_{S,c}^0\cap\mathcal A_c|
 \right).
\tag{6.2}
\]

By Theorem 4.1 this is exactly the reduction of the
\(\mathcal A\)-supported hole count, including all overlap corrections
through the unions. Beating the static cut to \(o(W)\) requires

\[
                         \operatorname{Esc}_{\mathcal A}(S)
                         \ge KM-o(W)
\tag{6.3}
\]

along one legal state change or a legal sequence evaluated with its
updated backgrounds.

The universal bound \(\operatorname{Esc}_{\mathcal A}(S)\le2s|S|\) at
one colour shows again that a linear repair needs
\(\Omega(W/2^R)\) slabs. This is dense but is the permitted slab scale.
No contradiction follows.

### Theorem 6.1 (the current slab axioms do not decide the \(1/2\)-cut)

For every \(d,L\ge1\), there are two complement-symmetric abstract
grouped \(H\)-memory catalogues with:

1. \(2d\) owner-disjoint two-state cross-parent groups;
2. zero memory boundary in every option;
3. equal option image size \(2L\);
4. the same complement-quotient endpoint graph and the same option
   adjacency pattern; and
5. arbitrary prescribed abstract Hamming-two labels on every option
   switch;

such that:

* in the **trapped catalogue**, every state misses at least half of the
  \(4dL\) typed targets;
* in the **escaped catalogue**, one state covers all \(4dL\) typed
  targets.

#### Proof

Partition the typed target universe into \(2d\) complement-paired blocks

\[
                         P_1,\ldots,P_{2d},
 \qquad |P_j|=2L.
\tag{6.4}
\]

Each \(P_j\) contains \(L\) lower targets and their \(L\) complementary
upper targets. Give every group two closed, complement-paired automaton
path options. Because each option is a union of closed paths, every
boundary is zero. Assign the same abstract parent labels and the same
two-option adjacency graph in the two catalogues.

In the trapped catalogue, let both option images of every group lie among

\[
                         P_1,\ldots,P_d.
\tag{6.5}
\]

The options may permute these \(d\) blocks nontrivially, but every state
has target union contained in (6.5), of size at most \(2dL\).

In the escaped catalogue, give group \(j\) an alternative whose image is
\(P_j\). Choosing all alternatives covers all \(2d\) blocks and hence all
\(4dL\) typed targets.

All endpoint, complement, option-count, image-mass, and abstract
parent-label data listed in the theorem agree. Only the literal
target-incidence labels differ. \(\square\)

Theorem 6.1 is an abstract sufficiency countermodel, not a literal
compiler construction. It proves that state connectivity and
complement-symmetric endpoint Hall do not imply target expansion. A
physical answer requires literal control of (6.2).

## 7. The exact sufficient augmenting-path theorem

The preceding results isolate a checkable positive statement.

### Theorem 7.1 (state-valid augmenting-union criterion)

Assume there are numbers \(\eta_m=o(1)\) and
\(0<\alpha_m\le1\) such that,
for every complement-symmetric state-valid path cover \(z\) with

\[
                         \mathfrak H(z)>\eta_mW,
\tag{7.1}
\]

there is a complement-closed owner-disjoint family \(S\) of whole
path/slab/compiler replacements satisfying

\[
 A\delta_S=M\delta_S=0,
\qquad
 \delta_S=\bar\delta_S,
\tag{7.2}
\]

all other active state rows, and

\[
 \sum_c\left(
 |Z_{S,c}\cap U_{S,c}^1|
 -|Z_{S,c}\cap U_{S,c}^0|
 \right)
 \ge\alpha_m\mathfrak H(z).
\tag{7.3}
\]

If the same hypothesis remains available after each augmentation, then
after at most

\[
                         O\!\left(
 {1\over\alpha_m}\log{H\over\eta_m}
 \right)
\tag{7.4}
\]

augmentations one obtains a complement-symmetric state-valid cover
\(z^\ast\) with

\[
                         \mathfrak H(z^\ast)\le\eta_mW=o(W).
\tag{7.5}
\]

#### Proof

Theorem 4.1 and (7.3) give

\[
                         \mathfrak H(z+\delta_S)
 \le(1-\alpha_m)\mathfrak H(z).
\]

Iterate until (7.1) fails. Geometric decay gives (7.4), and every
intermediate state remains legal by (7.2); here
\(\mathfrak H(z)\le|\mathcal V|\le2HW\) initially. \(\square\)

The theorem is stated for direct hole descent. By the exact mass identity,
the same iteration drives the repeat excess to \(o(W)\). It uses no
quadratic covariance.

For the final constant-one theorem one must additionally retain the owner
leave and component/path-interface budget. These can be added as active
rows or as an amortized toll in (7.3); endpoint balance alone does not
control the number of final memory cycles.

## 8. Certified boundary

Proved:

1. the exact endpoint-boundary characterization of grouped \(H\)-memory
   path covers;
2. the complement-quotient Hall theorem and its alternating-path/cycle
   augmentation;
3. the exact group-valid \(L^1\) augmenting-circuit formula;
4. every complete cross-parent slab switch is a zero-boundary
   \(H\)-memory circuit, and complement-paired slabs preserve symmetry;
5. the static mixed-profile cut is not a slab invariant;
6. the audited slab axioms do not imply enough target-labelled expansion
   to beat that cut; and
7. the quantitative augmenting-union criterion which would suffice.

Not proved:

1. an endpoint-separated owner-disjoint connector atlas of the required
   scale;
2. positive target escape (6.3) for the literal diverse-order slab
   catalogue;
3. group-valid lifts of enough residual automaton cycles;
4. persistence of the descent hypothesis after earlier slabs consume
   owners and target rows; or
5. the constant-one theorem.

Cross-parent slabs enlarge the \(H\)-memory state graph enough to remove
the static cut as a formal invariant, but current reachability is not
target-labelled expansion. The exact remaining theorem is the
complement-symmetric, group-valid augmenting-union statement (7.1)--(7.3).

## 9. Projection-free moving-frame specialization

MATH_THEOREM_PROJECTION_FREE_MOVING_FRAME_UNION_DUAL_AND_LITERAL_CUT_20260726.md
specializes the union gate to complete moving-frame overlays. If an
overlay splits into independently choosable whole component orbits
\(K\), with typed supports \(J_K^0,J_K^1\), fair recombination has exact
missing expectation

\[
 \sum_{t:c_t=0}2^{-d_t}.
\]

This is the required literal augmenting quantity; endpoint degrees and
fixed moments do not determine it. Coordinate projection-freeness alone
does not force it to be small. In the canonical connected pair-status
atlas, integral owner rigidity selects one global frame and the physical
full-pair strata give a positive-density missing cut, despite zero raw
occurrence deficit under the full coordinate average. In the
whole-support configuration LP the deficit remains positive: the
all-ones weight on the protected target layer is already a dual
certificate.
