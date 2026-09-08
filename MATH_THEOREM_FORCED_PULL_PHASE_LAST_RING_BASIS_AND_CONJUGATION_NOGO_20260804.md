# Forced pull phases, the exact last-ring basis criterion, and a conjugation no-go

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional for one fixed pairwise-disjoint tree-compatible
pull system.  The theorem gives an exact necessary-and-sufficient criterion
for modifying its pull spanning tree around a prescribed occurrence bank
while keeping one coherent ring pull as the final Hamiltonizing switch.  It
also proves that cycling through all synchronous coordinate rotations of a
fixed canonical system cannot be a universal cure.  It does **not** prove
that the current upper reservoir satisfies the criterion, and it does not
construct a typed common cap.

## 0. Setting

Let `F_0` be a spanning two-factor of a graph `G`.  Let `H` be a connected
labelled multigraph on the components of `F_0`.  Every label `e in E(H)`
carries an alternating circuit

\[
                 Z_e=O_e\mathbin{\dot\cup}N_e,
 \qquad O_e\subseteq F_0,
 \qquad N_e\cap F_0=\varnothing .                 \tag{0.1}
\]

Assume the two standard canonical properties.

1. The complete physical supports `Z_e` are pairwise edge-disjoint.
2. Every graphic forest `A subseteq E(H)` is tree-compatible: toggling the
   circuits in `A` gives a spanning two-factor `F_A`, and the components of
   `F_A` are canonically indexed by the connected components of the spanning
   forest `(V(H),A)`.  Equivalently, each selected forest edge performs one
   independent component merger, so

   \[
                       |\operatorname{Comp}(F_A)|
                         =|V(H)|-|A|.               \tag{0.2}
   \]

   This is the precise meaning of contracting `A` used below; it must not be
   confused with asking whether the ambient graph quotient `H/A` is
   connected (which it always is when `H` is connected).

Fix one distinguished nonloop label `g`.  It will be the coherent
three-ring pull.  Let `D` be a **common** occurrence-labelled physical edge
bank which is required in both states, and assume

\[
                         D\cap Z_g=\varnothing .     \tag{0.3}
\]

The three old ring edges `O_g` and three new ring edges `N_g` are therefore
kept separate from `D`.  The unchanged ring stubs and every private upper
witness may be included in `D`.

## 1. A protected bank forces its pull phase

Define the forced installation set

\[
 A_D=\{e\in E(H)-\{g\}:D\cap N_e\ne\varnothing\}. \tag{1.1}
\]

Call `D` **accessible** when

\[
 D\setminus F_0\subseteq
       \bigcup_{e\in E(H)-\{g\}}N_e .              \tag{1.2}
\]

Call it **phase-consistent** when

\[
                    D\cap O_e=\varnothing
                    \qquad(e\in A_D).              \tag{1.3}
\]

Finally, after (1.2)--(1.3), define the residual deletion labels

\[
 B_D=\{e\in E(H)\setminus(A_D\cup\{g\}):
                         D\cap O_e\ne\varnothing\}. \tag{1.4}
\]

### Theorem 1.1 (forced-phase normal form)

Let `A subseteq E(H)-{g}` be a graphic forest.  Then

\[
                         D\subseteq F_A             \tag{1.5}
\]

if and only if all of the following hold:

1. `D` is accessible;
2. `A_D subseteq A`;
3. `D cap O_e=emptyset` for every `e in A`.

Consequently, every pull set which installs `D` contains `A_D`; when `D` is
accessible and phase-consistent, `A_D` is the unique inclusion-minimal such
set.  In particular, `D` has a forest phase cover if and only if it is
accessible and phase-consistent and `A_D` is a graphic forest.

#### Proof

Take an edge `p in D-F_0`.  Accessibility is necessary.  Pairwise
disjointness of the complete pull supports implies that `p` belongs to at
most one new phase `N_e`.  Thus the unique label installing `p` must belong
to `A`; doing this for every such `p` gives `A_D subseteq A`.

Every edge of `D cap F_0` is initially present.  It survives precisely when
no selected pull removes it, which is condition 3.  Condition 3 also rules
out selecting a pull which deletes one protected old edge while installing
another protected new edge.

Conversely, under the three conditions, every edge of `D-F_0` is installed
by its forced label in `A_D`, every edge of `D cap F_0` survives, and no
other selected circuit can touch an installed edge because complete circuit
supports are pairwise disjoint.  Hence (1.5) holds.

Taking `A=A_D` proves sufficiency in the final statement.  Necessity and
minimality follow from the first paragraph. \(\square\)

The theorem removes a misleading freedom.  Once the literal bank and the
static pull system are fixed, choosing a different spanning tree cannot
change the phases forced by the nonfactor edges of the bank.

## 2. Exact last-ring spanning-tree criterion

Put

\[
                         J_D=A_D\cup\{g\}.           \tag{2.1}
\]

### Theorem 2.1 (last-ring graphic basis theorem)

Assume `D` is accessible and phase-consistent.  There is a spanning tree
`T` of `H` satisfying

\[
 J_D\subseteq T,
 \qquad
 T\cap B_D=\varnothing                              \tag{2.2}
\]

if and only if

\[
 \boxed{
   J_D\text{ is a graphic forest}
   \quad\text{and}\quad
   (H-B_D)/J_D\text{ is connected}.}                \tag{2.3}
\]

Equivalently, writing `r_gr` for graphic rank, the second condition is

\[
 r_{\rm gr}^{H/J_D}
   \bigl(E(H)\setminus(B_D\cup J_D)\bigr)
     =|V(H)|-1-|J_D|.                               \tag{2.4}
\]

When (2.3) holds, define

\[
                 F^-=F_{T-\{g\}},
 \qquad          F^+=F_T .                          \tag{2.5}
\]

Then:

1. `F^-` has exactly two components and contains `D union O_g`;
2. `F^+` is Hamiltonian and contains `D union N_g`;
3. the transition `F^- -> F^+` is exactly the one pull `g` and uses no
   additional physical position.

Conversely, every realization obtained inside this fixed pull system by a
spanning tree with `g` as the final switch satisfies (1.2)--(1.4) and
(2.3).  Thus (2.3) is exact for the canonical **last-`g` scheme**, not only
a sufficient cut condition.

#### Proof

If `T` exists, every subset of a tree is a forest, so `J_D` is independent.
Contracting `J_D` in `T` leaves a spanning tree of `(H-B_D)/J_D`; hence the
quotient is connected.

Conversely, choose a spanning tree of the connected quotient in (2.3) and
lift its edges.  Adjoining the forest `J_D` gives a spanning tree `T` of
`H-B_D`, proving (2.2).  This is ordinary graphic basis extension.

The set `T-{g}` is a spanning forest with exactly two components.  Tree
compatibility therefore makes `F^-` a two-factor with exactly two cycles.
Theorem 1.1 and avoidance of `B_D` show that it contains `D`.  Since `g` is
not toggled and all other circuit supports are disjoint from `Z_g`, it also
contains `O_g`.

Adding `g` completes the spanning tree.  Tree compatibility makes `F^+`
one Hamilton cycle.  Equation (0.3) and pairwise support disjointness preserve
`D`, while the toggle replaces `O_g` by `N_g`.  No vertex or position is
added.

For the converse, a last-`g` spanning tree must install every nonfactor edge
of `D`, so Theorem 1.1 forces `A_D`.  It cannot select a label in `B_D` and
must contain `g`.  Its existence therefore implies exactly the two graphic
conditions in (2.3). \(\square\)

### Corollary 2.2 (exact cut form)

Under accessibility and phase consistency, the last-ring construction
exists exactly when `J_D` is a forest and every nontrivial vertex partition
of the contracted host `(H/J_D)` has a crossing edge outside `B_D`.

Thus there are three logically distinct failures:

\[
 \boxed{
 \text{inaccessible protected edge} ;\quad
 \text{cycle among forced pull labels} ;\quad
 \text{cographic cut killed by protected old edges}.}
\tag{2.6}
\]

Changing only the unused part of the pull spanning tree can repair only the
third failure.

## 3. Interface with the three-ring reservoir

For the coherent common-history three-ring, take `g` to be its standard
all-six-coherent pull.  Put into `D`:

1. the three unchanged lower stubs;
2. every private clipped-resident upper-cone witness path; and
3. every other physical occurrence required unchanged through the ring
   toggle.

The old and new seam edges are `O_g` and `N_g`.  If this `D` satisfies
(1.2)--(1.4) and (2.3), Theorem 2.1 simultaneously supplies the exact bare
factor chronology required by the reservoir theorem:

\[
 2\text{ components with the old ring and }D
 \ \xrightarrow{g}\
 1\text{ Hamilton component with the new ring and }D. \tag{3.1}
\]

The independent reservoir theorem then transports the strict-lower deck and
protects every target in the ring's upper damage cone.  It still needs the
ambient pre-toggle upper-completeness hypothesis for targets outside that
cone.  Theorem 2.1 does not manufacture that hypothesis.

This is the exact quantifier bridge between the canonical topology theorem
and an independently designed reservoir: the independent paths must first
form one accessible, phase-consistent forced pull forest `A_D`, and their
protected base edges must leave the contracted residual host connected.

## 4. Typed common-cap scope

The preceding statements are physical edge theorems.  They do not identify
two equal Boolean masks with one occurrence and do not infer a cap route from
an owner incidence.

For one **already fixed common** typed occurrence/cap state `Theta`, required
verbatim in both ring phases, declare a residual pull label forbidden whenever
its switch invalidates any named typed occurrence, prefix, suffix, capacity
unit, or cap route of `Theta`.  More precisely, put

\[
 B_{D,\Theta}\subseteq E(H)\setminus J_D,
 \qquad B_D\subseteq B_{D,\Theta},                  \tag{4.1}
\]

and include every residual label which touches or invalidates one of the
fixed resources of `Theta`.  Suppose the complete forced family
`J_D=A_D\cup\{g\}` is jointly valid in that same common state; in particular,
the final ring pull `g` must preserve `Theta` (apart from the explicitly
phase-specific ring edges, which are not part of `Theta`).  If

\[
 J_D\text{ is a forest},
 \qquad
 (H-B_{D,\Theta})/J_D\text{ is connected},           \tag{4.2}
\]

then the proof of Theorem 2.1 preserves `Theta` verbatim.

Equation (4.2) is a conditional one-state topology test.  Because `Theta` is
fixed occurrence by occurrence, avoidance is closed under unions of residual
pull supports; no unproved marginal-to-joint inference is being made.  No
theorem here
asserts that the `I_bc/I_ca` sockets, the background compiler, and their
typed cap routes coexist in such a `Theta`; that is still a separate
existence theorem.

## 5. Synchronous conjugation is not a universal escape

The fixed-host local aperture theorem says that at one lower vertex `I`, as
a graphic pull forest varies, at most four owner wedges are accessible.
This remains true after conjugating the complete factor/pull system.

### Theorem 5.1 (finite-conjugate wedge obstruction)

Let `mathfrak H={H_1,...,H_s}` be `s` conjugates of one canonical
factor/pull system on `ML_m`.  At a fixed lower vertex `I`, the union of all
wedges accessible from these systems has size at most `4s`.

If

\[
                         \binom m2>4s,               \tag{5.1}
\]

there is a literal complete common-history three-ring, and for all
sufficiently large `m` its clipped upper-cone reservoir, whose protected old
ring phase has no phase cover in any member of `mathfrak H`.

#### Proof

Each conjugated system exposes at most four wedges at `I`, so their union
has size at most `4s`.  The lower vertex `I` has `m` owner neighbours and
therefore `binom(m,2)` possible wedges.  Under (5.1), choose an inaccessible
pair

\[
                         I+x,\qquad I+y.             \tag{5.2}
\]

Choose `a in I`, put `B=I-{a}`, use `b=x` as the common external label, and
take `y` to be the cyclic predecessor of the active ring label `a`.  A third active label is
available outside `B union {a,x,y}`.  Then the distinguished hinge has lower
port `I` and owner wedge exactly (5.2).  Partition `B` into the common
depth-`d` history when `d<=m-2`.  This is a literal three-ring.

Every phase cover containing the ring must expose its wedge at `I`, which no
member of `mathfrak H` can do.  The clipped private reservoir can be built
over the already fixed ring by the independent upper-cone construction; it
does not alter this forced hinge. \(\square\)

### Corollary 5.2 (all cyclic rotations still fail universally)

The rotational canonical factor is invariant under the `2m-1` synchronous
cyclic coordinate rotations.  Taking `s<=2m-1` in Theorem 5.1 gives

\[
 \binom m2>4(2m-1)
 \qquad(m\ge17).                                    \tag{5.3}
\]

Hence, from `m=17` onward, there is a valid three-ring reservoir which is
inaccessible in every synchronous cyclic conjugate of a fixed canonical
pull system.

This does not contradict the coherent-ring Hamilton theorem: that theorem
chooses the ring **from** a canonical pull before completing the tree.
Corollary 5.2 proves that the opposite quantifier order—first freeze an
arbitrary ring/reservoir, then rotate the whole canonical tree—cannot be a
general protected-extension theorem.

## 6. Consequence for the current frontier

The topology/reservoir mismatch is now an exact static-host decision:

\[
 \boxed{
 \text{forced occurrence phase }A_D
 +\text{ graphic independence of }A_D\cup\{g\}
 +\text{ one residual cographic rank test}.}
\tag{6.1}
\]

There is no remaining choice of phases after `D` is fixed.  The unused
spanning-tree labels are the only flexible part.

Therefore the shortest positive theorem is not “an `o(W)` bank fits after
rotating the Mütze tree.”  It is:

> choose the clipped reservoir and the coherent ring jointly inside the
> canonical phase union so that their forced labels form a forest and their
> protected old incidences leave the contracted pull host connected.

Alternatively one must enlarge the move system beyond the pairwise-disjoint
canonical pulls.  Cap typing remains an additional simultaneous-state row,
as recorded in Section 4.

## 7. Dependencies

- `MATH_THEOREM_COHERENT_SINGLE_PULL_THREE_RING_HAMILTON_PLANTING_20260804.md`
- `MATH_THEOREM_THREE_RING_CLIPPED_UPPER_CONE_RESERVOIR_AND_ALLWIDTH_TRANSPARENCY_20260804.md`
- `MATH_THEOREM_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_20260804.md`
- `MATH_THEOREM_PRESELECTED_PORTAL_FOREST_EXTENSION_AND_PULL_HOST_LIFT_GATE_20260801.md`
