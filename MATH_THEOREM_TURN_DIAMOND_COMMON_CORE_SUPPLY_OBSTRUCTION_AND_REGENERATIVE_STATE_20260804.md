# Turn diamonds do not supply a common history: the exact regenerative state and component-transversal gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical nonimplication, exact
component-hitting criterion on the fixed-edge guarded-factor face, and a
minimal sufficient regenerative-state formulation.  No search or
computational construction is used.  The current Pascal/turn-diamond and
promotion/common-core theorems do **not** prove the required common
`d-O(1)` completed-hinge supply.

## 0. Verdict

The answer to the supply question is presently **no**.

The protected Middle-Levels factor and turn-diamond theorems provide:

* occurrence-labelled incidence halfports;
* lower turns, rank-`m` owners, singleton incidence labels, and q1 terminal
  values;
* component orientation parity; and
* an exact protected opening-loss ledger.

They explicitly do not provide an order-`d` literal source history, a
residence boundary state, an upper-witness bank, a common-cap state, or a
compiler state at those halfports.  Consequently they cannot imply that
the residual factor components expose completed hinges with one common
history core.

The promotion common-core atlas does not close this gap.  Its `2H`-set
`Q_U` is a coordinate-containment core: the retained promotion phases have
their central `2H`-words in `U-Q_U`, not in `Q_U`.  Moreover the core,
orders, tail word, and phase tags are selected separately for each top.
The theorem supplies local literal paths and separate rankwise Hall
matchings, but no globally common ordered de Bruijn state and no occurrence
in every rescued factor component.

The scalar scale is ample:

\[
 H=(1+o(1))\sqrt{m\log m},
 \qquad d=\Theta(\sqrt m),
 \qquad H/d\longrightarrow\infty.
\tag{0.1}
\]

Thus local word length is not the obstruction.  The obstruction is the
correlated occurrence-level quantifier.

The exact missing theorem is a **Guarded Common-Core Component
Transversal**: choose one actual common ordered history and full guard
signature, form its occurrence bank `S`, and choose the factor so that

\[
                         \boxed{F\setminus S\text{ is a forest}.}
\tag{0.2}

If `S` is one jointly completed all-pairs hinge class, (0.2) immediately
gives zero-cost fusion.  If it is a common guarded `K`-router and the factor
has `O(1)` components, it gives an `O(1)` overlap tour.

## 1. The factor projection forgets the required state

Let `Phi` be a spanning two-factor of `ML_m`.  Its protected occurrence
lift records for an incidence edge `L--U` the tuple

\[
 (\text{component},\text{turn index},\text{side},L,U,U-L).
\tag{1.1}
\]

Call this the **turn projection**.  A full literal port state would
additionally record at least

\[
 (\text{order-}d\text{ history},\text{residence boundary},
   \text{upper witnesses},\text{cap},\text{compiler}).
\tag{1.2}

### Theorem 1.1 (component-history projection obstruction)

No statement depending only on the turn projection can imply a connected
completed-hinge compatibility graph between distinct factor components.

More precisely, if `Phi` has components `C_1,...,C_c`, then its turn
projection has a state expansion in which every port on `C_i` carries a
component tag `tau_i`, and cross-component hinge compatibility requires
tag equality.  For pairwise distinct tags, every incidence, owner, q1,
orientation, and protected-opening statement remains unchanged, while the
component compatibility graph has only loops.

#### Proof

The data in (1.1) contain no history or guard coordinate.  Adjoin an
independent tag coordinate to every occurrence and make every local
incidence prefix preserve it.  Forgetting the tag recovers exactly the
original turn projection, so all theorems stated solely in that projection
remain true.

If a cross-component completed hinge requires equality of the full state,
then `C_i` can connect to `C_j` only when `tau_i=tau_j`.  Distinct tags
therefore leave only same-component compatibility. \(\square\)

This is a sharp logical nonimplication, not a Boolean nonexistence theorem.
It says the missing state cannot be reconstructed from owner/q1 incidence
data; it must be selected or transported by an additional literal theorem.

## 2. A mask core is not a history core

The word “core” occurs in two inequivalent senses.

* A **containment core** is a coordinate set included in every mask of a
  family.
* A **history core** is an ordered literal word which is simultaneously a
  suffix of every exit history and a prefix of every entry history.

### Proposition 2.1 (literal separation)

Let `Q` be any coordinate set and suppose there are `2d` distinct
coordinates

\[
 a_1,\ldots,a_d,b_1,\ldots,b_d\notin Q.
\]

Define literal histories

\[
 u=(Q\cup\{a_1\},\ldots,Q\cup\{a_d\}),
 \qquad
 v=(Q\cup\{b_1\},\ldots,Q\cup\{b_d\}).
\tag{2.1}
\]

Every letter, hence every interval union, contains `Q`, but

\[
                         \operatorname{ov}(u,v)=0.
\tag{2.2}

Thus even letterwise containment of one common coordinate core does not
give one letter of literal history overlap.

#### Proof

All letters contain `Q`.  Since all `a_i,b_j` are distinct, no letter in
`u` equals a letter in `v`.  A nonzero suffix--prefix overlap would in
particular equate its first pair of corresponding letters, impossible.
\(\square\)

At the promotion scale, `H=o(m)` and `d=O(sqrt(m))`, so the ambient ground
set has room for the separation in Proposition 2.1.  More importantly, the
actual promotion theorem makes the central retained word avoid `Q_U`; it
never identifies `Q_U` with a de Bruijn history word.

## 3. Exact common-core component deficiency

Let `G=(V,E)` be a finite occurrence-labelled host.  Fix a protected
degree-at-most-two bank `D`, a disjoint fixed forbidden edge bank `Z`, and
let

\[
 \mathfrak F(D,Z)
 =\{F:\ F\text{ is a spanning two-factor},
          D\subseteq F,\ F\cap Z=\varnothing\}.
\tag{3.1}
\]

Let `xi=(R,theta)` be one proposed regenerative state, where `R` is an
ordered history core and `theta` is its full guard signature.  Let

\[
                         S_\xi\subseteq E
\tag{3.2}
\]

be the occurrence bank of ports carrying exactly that state and the
declared hinge/connector semantics.

For a graph `J`, write

\[
                         \beta(J)=|E(J)|-|V(J)|+\kappa(J)
\tag{3.3}
\]

for its graphic nullity, with isolated vertices counted in `kappa`.
Define

\[
 \eta(D,Z;\xi)
 =\min_{F\in\mathfrak F(D,Z)}\beta(F\setminus S_\xi).
\tag{3.4}
\]

### Theorem 3.1 (exact component-transversal identity)

For every `F in mathfrak F(D,Z)`,

\[
 \beta(F\setminus S_\xi)
 =\#\{C\in\operatorname{Comp}(F):E(C)\cap S_\xi=\varnothing\}.
\tag{3.5}
\]

Consequently

\[
 \boxed{
 \eta(D,Z;\xi)=0
 \iff
 \text{some protected factor has an }S_\xi\text{-port in every component}.}
\tag{3.6}
\]

#### Proof

Every component of `F` is a cycle.  A component disjoint from `S_xi`
survives as a cycle in `F-S_xi` and contributes one nullity unit.  Deleting
at least one `S_xi` edge from a component breaks its cycle into paths and
isolated vertices, contributing zero.  Nullity adds across factor
components. \(\square\)

Thus the supply problem is not a post hoc matching of ports to components.
It is a correlated factor-selection condition: `F-S_xi` must be a forest.

## 4. Exact fixed-edge factor-extension form

Specialize here to `G=ML_m`, or to a fixed bipartite occurrence expansion
for which the displayed `delta_star` is the exact residual `b`-factor
deficiency.  On this fixed-edge guarded face, Theorem 3.1 has an exact
Ore--Ryser formulation.

For a degree-at-most-two protected bank `P` and forbidden edge bank `Y`
disjoint from it, let

\[
                         \delta_\star(P,Y)=0
\tag{4.1}

mean the exact guarded Ore--Ryser condition for extending `P` to a spanning
two-factor avoiding `Y`.

### Theorem 4.1 (forest-supported common-core extension)

Assume `mathfrak F(D,Z)` is nonempty.  Then `eta(D,Z;xi)=0` if and only if
there is a graphic forest

\[
 R_0\subseteq E\setminus(S_\xi\cup Z)
\tag{4.2}
\]

such that

\[
 D\setminus S_\xi\subseteq R_0
\tag{4.3}
\]

and, with

\[
 Y_{R_0}
 =Z\cup\bigl(E\setminus(R_0\cup S_\xi)\bigr),
\tag{4.4}
\]

one has

\[
                         \boxed{\delta_\star(D,Y_{R_0})=0.}
\tag{4.5}
\]

#### Proof

Suppose `eta=0` and choose a witnessing factor `F`.  Put

\[
                         R_0=F\setminus S_\xi.
\]

Theorem 3.1 makes `R_0` a forest.  It avoids `S_xi` and `Z`, contains
`D-S_xi`, and `F` is a two-factor containing `D` while avoiding
`Y_(R_0)`.  Hence (4.5) holds.

Conversely, (4.5) supplies a two-factor `F` containing `D` and using only
edges of `R_0 union S_xi` outside the already forbidden bank.  Therefore

\[
                         F\setminus S_\xi\subseteq R_0,
\]

which is a forest.  Theorem 3.1 gives `eta=0`. \(\square\)

This criterion is exact only when every nonfactor guard has already been
compiled into the fixed protected/forbidden edge state.  Selection-dependent
cap or compiler conflicts require a larger occurrence-state host.

## 5. Positive implication from the missing state

Suppose `|R|=d-K` for an absolute `K` and `theta` includes every hard
boundary guard.

### Theorem 5.1 (common-core transversal closes topology)

Assume `eta(D,Z;xi)=0`.

1. If `S_xi` is one jointly all-pairs completed-hinge class, some witnessing
   factor fuses to one spanning cycle with zero additional positions.
2. If every `S_xi` port has a product-separable guarded connector of charge
   at most `K` to every other `S_xi` port, and a witnessing factor has at
   most `C` components, then it opens and joins into one protected path with
   added charge at most

   \[
                         A+(C-1)K,
   \tag{5.1}
   \]

   where `A` is total opening charge.

#### Proof

By Theorem 3.1, choose one `S_xi` port in every factor component.  In item
1, any cyclic permutation of the selected occurrence-labelled hinge heads
is jointly legal; the completed-hinge permutation theorem fuses all
components without adding a position.  In item 2, any linear component
order has at most `C-1` guarded joins of charge at most `K`; apply the exact
guarded overlap-tour theorem. \(\square\)

This is the strongest implication available from the present theory.  The
unproved content is the existence of `xi,S_xi` satisfying the hypotheses.

## 6. What the promotion atlas actually supplies

At the calibrated promotion scale it is proved that:

1. each top has a coordinate core `Q_U` of size `2H` and a literal
   core-safe promotion path of length
   `L=m-3H+1`;
2. every mask on that local path contains `Q_U`;
3. each signed rank separately has an integral matching for the same fixed
   coordinate cores; and
4. the complete local catalogue has an exact symmetric fractional point.

These statements are useful but do not imply Theorem 5.1:

* `Q_U` is not an ordered history suffix/prefix;
* `Q_U` and the tail word vary with `U`;
* separate rank matchings are not nested on one phase;
* the local paths are not selected into one owner-disjoint global atlas;
* no theorem places one occurrence of one state `xi` in every residual
  factor component; and
* no theorem makes those occurrences one jointly completed guard product.

Numerically, `L>>d` and `H>>d`, so a local path has ample aperture for a
`d`-letter subword.  The missing row is equality and component coverage of
one such subword, not its length.

## 7. Minimal regenerative state extension

For a component orientation fixed in advance, the smallest proof-safe
export is

\[
 \Xi=
 (R;\theta_{\rm res},\theta_{\rm upper},\theta_{\rm occ},
       \theta_{\rm cap},D_{\rm comp},\mathcal H),
\tag{7.1}
\]

where:

1. `R` is the actual ordered length-`d-K` history core;
2. `theta_res` is the complete clipped residence/age boundary;
3. `theta_upper` is the protected arbitrary-width witness signature;
4. `theta_occ` names the physical halfports and their capacity aliases;
5. `theta_cap` is the common cap/product state;
6. `D_comp` is a complete bounded compiler-damage signature, sufficient in
   place of transporting an entire terminal matching; and
7. `mathcal H` is the jointly completed hinge/head relation.

If component orientation is chosen later, `Xi` must instead carry the two
orientation images `Xi^+,Xi^-` together with the one-bit component parity
constraint.  An absolute root index or transported phase not acted on by
that one bit remains a separate state coordinate.

Every field is load-bearing:

* removing `R` permits zero-overlap component histories;
* removing the residence or upper state permits a seam to destroy a named
  run or witness;
* removing occurrence identity aliases distinct halfports at one owner;
* removing cap state permits the invariant-flag obstruction;
* removing joint completion permits individually legal hinges to consume
  one common capacity unit; and
* removing the forest-complement row permits an entire component to contain
  no exported port.

## 8. Exact next lemma

The remaining theorem can now be stated without ambiguity.

### Guarded Common-Core Forest-Complement Lemma `GCCFC(K,B)`

There are absolute constants `K,B` such that, in every sufficiently large
dimension, the protected Pascal child admits a state `Xi`, an occurrence
bank `S_Xi`, and a guarded factor `F` satisfying:

1. `|R|=d-K`;
2. `F-S_Xi` is a forest;
3. the selected `S_Xi` hinges have a Hamilton completed-hinge compatibility
   digraph, or a product-separable guarded overlap tour of total charge at
   most `B`;
4. all residence and arbitrary-width upper gates survive; and
5. the complete final compiler damage and remaining target-repair charge is
   at most `B`.

`GCCFC(K,B)` plus bounded task birth implies

\[
                         \nu(k)\le B(k)+O(1)
\]

by Theorem 5.1 and bounded compiler eviction.  The present
Pascal/turn-diamond and promotion/common-core results prove none of Items
1--3 in one common occurrence-labelled factor; this lemma is a genuine new
construction theorem, not a repackaging of an existing result.

## 9. Dependencies

| role | file |
|---|---|
| exact protected ML occurrence lift and its scope | `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md` |
| turn-diamond wedge packing | `MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md` |
| promotion coordinate-core atlas | `MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md` |
| audit of promotion common-history gap | `MATH_AUDIT_PROMOTION_GLOBAL_COMMON_HISTORY_20260726.md` |
| common-core forest-complement reduction | `MATH_THEOREM_COMMON_CORE_CYCLE_TRANSVERSAL_AND_FOREST_COMPLEMENT_20260804.md` |
| completed-hinge and guarded overlap-tour bridge | `MATH_THEOREM_BOUNDED_COMPONENT_COMPLETED_HINGE_AND_GUARDED_OVERLAP_TOUR_20260804.md` |
| exact guarded Ore--Ryser factor extension | `MATH_THEOREM_L_ORBIT_WEIGHTED_ACTUATOR_PLANTING_AND_GUARDED_STAR_CUT_20260801.md` |
| bounded compiler eviction | `MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md` |
