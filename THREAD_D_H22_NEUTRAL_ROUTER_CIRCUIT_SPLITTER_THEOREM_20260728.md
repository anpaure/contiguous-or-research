# Hall 22: neutral-router groupoid and DM-circuit splitter theorem

Date: 2026-07-28

Status: exact `H23 -> H23 -> H22` remote circuit discharge; exact
common-controller augmentation on the critical DM atlas; proved regenerative
routing theorem and a two-colour sufficient condition.  Full transitivity of
the physical neutral braid groupoid is not proved.  Its occurrence-preserving
subgroup cannot itself create an incident cell at any of the seven isolated
`1/0` components; this does not exclude routing to a context where a later
nonneutral creator acts.

## 0. Main conclusion

The authoritative Hall descent is

\[
 H23\xrightarrow{\operatorname{RF}(3799,4497,6039)}H23^{\rm port}
 \xrightarrow{\operatorname{FR}(740,4051,6137)}H22.       \tag{0.1}
\]

The first braid is not a disguised local improvement.  It rotates two
compiler shores inside the `161/160` DM component rooted at `24610`, keeps
that component at rank 160, and makes the second braid physically legal.
The second braid makes no component-restricted incidence-signature change in
the `24610` component.  It acts remotely on the `2/1` component

\[
                              C=\{4877,4909\},                    \tag{0.2}
\]

replacing its one component-restricted shore `C` by the two
component-restricted singleton shores `\{4877\}` and `\{4909\}`.  This
discharges the whole circuit and raises the global matching rank by one.

The correct general object is therefore not a globally acting neutral braid
group.  Braid legality depends on the current carrier, and a protected
common-controller pin family must move with the carrier.  The natural object
is a **partial transformation groupoid on decorated carriers**.

There is a rigorous induction theorem for that groupoid: if the neutral orbit
of every residual rooted DM circuit meets a clean splitter locus, with the
protected common-controller matching transported at every step, then one may
discharge the circuits one at a time without losing the deck, residence, or
protected shadows.  A connected context-independent safe-swap graph is a
concrete sufficient condition for this orbit hypothesis.

For the exact H22 carrier, the residual obstruction has a particularly small
port alphabet.

* All 22 positive-DM components are transversal-matroid circuits of excess
  one and have a simultaneous native atlas omitting only their root.
* The 15 nonloop circuits all contain a root two-shore.  There are only two
  port colours: six `(root rank 4, cell depth 0)` circuits and nine
  `(root rank 6, cell depth 2)` circuits.
* The other seven circuits are isolated `1/0` components.  Any neutral
  subgroup which preserves the full target-occurrence vector fixes their
  zero degree, so it cannot route an existing root-edge splitter to them.
  The currently known way past that invariant is a distinct
  creator-and-compensator macro.

Thus a two-colour regenerative transitivity theorem would reduce H22 to the
seven-loop floor H7.  A separate clean creator theorem is required for
H7 to H0.  The present exact data prove one rank-six splitter route, not those
two transitivity statements.

## 1. Exact carrier audit

The canonical artifacts are:

| state | file | SHA-256 | matching / deficiency | DM shore |
|---|---|---|---:|---:|
| H23 | `scratch/k15_segment_braid_hall23.json` | `8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d` | `16360 / 23` | `1007/984` |
| portal | `scratch/k15_segment_braid_hall23_portal.json` | `9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6` | `16360 / 23` | `1007/984` |
| H22 | `scratch/k15_segment_braid_hall22.json` | `c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798` | `16361 / 22` | `1005/983` |

Each state is an exact permutation of all 6435 rank-eight owners, a Johnson
path, and depth-three resident.  Its maximal erosion controller is everywhere
nonzero and reconstructs the central path.  Every upper support layer at
depths `q=1,...,7` is complete.  The lower-hole vectors are

\[
 (4,19,6,1,0,0,0)\longrightarrow(4,19,6,1,0,0,0)
 \longrightarrow(4,18,6,1,0,0,0).                 \tag{1.1}
\]

Thus the router preserves every lower support, while the splitter loses none
and gains the depth-two target `4877`.  Deeper multiplicities do change;
(1.1) is a support statement, not an incidence-multiset identity.  The same
seven zero targets survive all three states.

After cancelling common full cell-shore signatures as multisets, the neutral
transition has 18 noncommon multiplicities, common rank 16350, and contracted
boundary rank `10 -> 10`.  The splitter has 41 noncommon multiplicities,
common rank 16343, and contracted rank `17 -> 18`.  These are multiset
replacement counts, not counts of indexed physical positions.  With rows
indexed by compiler graphs and columns by canonical DM shores, both ordered
H23, portal, H22, the cross-gap matrix is

\[
 \begin{pmatrix}
 23&23&22\\
 23&23&22\\
 22&22&22
 \end{pmatrix}.                                             \tag{1.2}
\]

Applying the second braid directly to H23 is not legal: two proposed seams
have Johnson XOR weight eight, five internal residence runs fail, shallow
targets `20952` and `20944` are lost, and the central erosion reconstruction
fails at start 737.  After the neutral router the corresponding new seams are
Johnson edges.  Hence the first arrow of (0.1) is a genuine legality router.

## 2. The exact remote algebra

### 2.1 The neutral associator

Inside the component rooted at `24610`, put

\[
\begin{aligned}
A&=\{24610,24611,24674,24675\},\\
B&=\{24614,24615,24678,24679\},\\
C&=\{28707,28770,28771\}.
\end{aligned}                                                \tag{2.1}
\]

These blocks are disjoint.  The neutral braid replaces the two restricted
cell shores

\[
                         B,\quad A\cup C                       \tag{2.2}
\]

by

\[
                         C,\quad A\cup B.                      \tag{2.3}
\]

Every target in \(A\cup B\cup C\) has the same **component-restricted**
occurrence count before and after this replacement.  The component matching
rank remains 160.  This is a packet associator or basis rotation: it changes
which targets share a cell, but not this restricted point-incidence vector or
the component rank.  The improving braid then leaves this entire restricted
signature unchanged.  Full cell neighbourhoods also contain exterior
targets, so (2.2)--(2.3) alone is not a theorem that every global target
degree is fixed.

Occurrence preservation alone does not imply preservation of every
transversal-matroid rank function.  The rank-neutrality in (0.1) is part of
the exact carrier certificate, and must be required of any purported neutral
generator.

There is nevertheless an exact statewise port-routing identity.  For

\[
 T'=\operatorname{RF}(r,s,t)T
   =T_{[0,r)}\,\overleftarrow{T_{[s,t]}}\,
     T_{[r,s)}\,T_{(t,W)},
\]

the new chronology is Johnson precisely when its three new seams satisfy

\[
 T_{r-1}\sim T_t,\qquad T_s\sim T_r,\qquad
 T_{s-1}\sim T_{t+1}.
\]

An old oriented edge at positions `(x,x+1)` in the reversed block appears in
reverse orientation across new cut

\[
                              u=r+t-x.
\]

For the actual router, `(r,s,t,x,u)=(3799,4497,6039,5787,4051)`.
Thus the neutral braid installs exactly the oriented edge needed at the
second braid's cut 4051.  The identity proves ideal port transport; the three
seam tests, residence collars, shadow ledger, matching complement, and
common-controller cocycle decide whether that transport is a legal neutral
arrow.

### 2.2 The remote splitter

Before the improving braid, the component in (0.2) has one right vertex with
restricted shore `\{4877,4909\}`.  Afterwards it has the two restricted
shores

\[
                             \{4877\},\qquad\{4909\}.           \tag{2.4}
\]

The physical cells are

| target | cell | depth | start | native trace |
|---:|---:|---:|---:|---:|
| `4877` | `7178` | 1 | 740 | `4877` |
| `4909` | `13614` | 2 | 739 | `4909` |

The word “singleton” in (2.4) is component-relative.  The full compiler
neighbourhoods of cells 7178 and 13614 have sizes eight and four,
respectively.  This causes no problem: restriction to the old positive DM
component is what controls its one-unit deficit, while the native traces give
the literal pins.  In the exact endpoint certificate, the physical compiler
agrees with the maximal controller on both intervals, so their positive hits
are realized as well.

The final DM shore is exactly the old shore with `4877,4909` removed.  No
other DM target is added or removed.

### 2.3 Cumulative common-controller regeneration

The common-controller statement persists across both authoritative component
discharges, not merely across (0.1).  Take the old H24 critical shore of 1168
targets.  Let `P` be the final H22 maximal erosion controller.  Choose a
physical compiler `A` by coordinatewise pinning of `P`, and use:

* the 983 native pins of the active H22 DM shore;
* all 161 pins of the previously discharged `20516` component, with cell
  6261 repinned from native child `20517` to root `20516`; and
* the two native pins in Section 2.2.

These three cell families and their target sets are pairwise disjoint.  The
only physical-letter change from `P` is

\[
                         A_{6261}:20517\longmapsto20516.         \tag{2.5}
\]

Every central four-window union is unchanged, and the only other selected interval
through position 6261 keeps union `22565`.  Hence one nonzero physical compiler
realizes

\[
                              983+161+2=1146                    \tag{2.6}
\]

distinct pins on the old 1168-target H24 shore.  Its cumulative common-pin
defect, and in this certificate its restricted matching defect, is exactly
22, with unresolved targets precisely the H22 roots.  This is not the old
shore's raw neighbourhood gap in the final graph: that gap is 21.  The result
is an exact two-step regeneration certificate, not a lift of a global
16361-edge maximum matching.

The distinction \(A\subseteq P\) is forced, not cosmetic.  For coordinate zero,
the maximal H22 controller has incidence 2145, satisfying the exact
law \(p_x\equiv\binom{14}{7}\equiv0\pmod 3\), whereas (2.5) gives physical
incidence 2144.
Thus the repinned compiler cannot itself be the erosion Johnson controller.

## 3. Circuits, native atlases, and clean ears

Let `G=(L,R;E)` be a bipartite compiler graph and let `M_G` be the transversal
matroid on `L`: a set is independent when it can be matched into `R`.

### Lemma 3.1 (unit DM component is a circuit)

Suppose a closed connected positive DM component has left shore `C`, right
shore `D`, with `N_G(C)=D` and `|C|=|D|+1`.  Suppose the restricted maximum
matching saturates `D`, has a unique exposed vertex `e_0` in `C`, and every
vertex of `C` is reachable from `e_0` by an alternating even path.  Then `C`
is a circuit of `M_G`.

#### Proof

The matching saturates `D` and leaves `e_0` exposed.  For any \(x\in C\),
flip the matching along an alternating path from `e_0` to `x`.  The new
matching still saturates `D` and now leaves `x` exposed.  Hence `C-{x}` is
independent for every `x`.  Since `|C|>|D|`, `C` itself is dependent.  It is
therefore a circuit.  \(\square\)

This is the matching-theoretic content of the exact DM decomposition; it is
also checked directly for every H22 component by deleting each possible
exposed target and recomputing the restricted matching.

### Lemma 3.2 (every closed nonloop unit circuit has an abstract split)

Let `(C,D)` be a closed unit component with `N(C)=D`,
`|D|=|C|-1`, and suppose every `C-{x}` matches bijectively onto `D`.
Choose a cell `y in D` and a target `x in N(y)`.  If `y` is replaced by two
cells with restricted shores

\[
                        \{x\},\qquad N(y)-\{x\},                 \tag{3.1}
\]

then the resulting restricted graph matches all of `C`.

#### Proof

By hypothesis, choose a matching of `C-{x}` bijectively onto `D`.
It matches `y` to some \(w\ne x\), so \(w\in N(y)-\{x\}\).  Keep every other
matching edge, match `x` to the first new cell, and match `w` to the second.
\(\square\)

This removes every abstract matching obstruction inside a nonloop unit
circuit.  It says nothing about realizing (3.1) by physical seams, retaining
the exterior matching, or satisfying the common-controller ledger.

### Lemma 3.3 (root-ear discharge)

Let `C` be a circuit with distinguished root `rho`.  Suppose
\(\mu\cup\eta\) is an old maximum matching, where \(\mu\) matches
\(C-\{\rho\}\) and \(\eta\) is the cell-disjoint exterior part.  If a legal braid produces a new
unused cell `e` adjacent to `rho` and retains cell-disjoint copies of
\(\mu\) and \(\eta\), then the new global matching rank is at least one larger.

#### Proof

Add the edge `rho e` to the retained copy of \(\mu\cup\eta\).  The cells are
disjoint, so their union is a matching of size `nu(G)+1`.  \(\square\)

A component-restricted split

\[
                   \{\rho,x\}\longmapsto\{\rho\},\{x\}         \tag{3.2}
\]

is the cleanest realization of Lemma 3.3.

### Lemma 3.4 (exact native-pin extension test)

Let `P` be a fixed erosion controller and let a physical interval cell `I`
have native trace

\[
                         \tau_P(I)=\bigcup_{p\in I}P_p.          \tag{3.3}
\]

Let \(\widehat H_x\) be the positions still allowed for coordinate `x` after all
negative constraints of an existing common-controller certificate.  Adding
the unused pin `I -> tau_P(I)` creates no new negative exclusion.  It extends
the certificate if and only if

\[
                 \widehat H_x\cap I\ne\varnothing
                 \qquad(x\in\tau_P(I)).                         \tag{3.4}
\]

#### Proof

For a coordinate `x` outside `tau_P(I)`, no controller state in `I` contains
`x`, so forbidding `I` for that coordinate removes no controller occurrence.
For `x` in `tau_P(I)`, the new pin needs one surviving allowed occurrence in
`I`, which is exactly (3.4).  No other condition changes.  \(\square\)

The two pins in the table in Section 2.2 are native and distinct.  They
use physical letters equal to the maximal controller on their intervals and
pass (3.4) simultaneously;
the exact certificate therefore extends the H23 native atlas without changing
the endpoint physical compiler.  Native status alone would not imply this for an arbitrary
pre-existing pin family: its negative constraints might already have removed
every allowed hit in `I` for some positive coordinate.

## 4. Exact H22 port classification

### Theorem 4.1 (H22 circuit atlas)

For each canonical H22 component `C`, define its distinguished native root by

\[
                              \rho_C=\bigcap_{S\in C}S.
\]

Then:

1. the `1005/983` positive DM shore is the disjoint union of exactly 22
   excess-one transversal-matroid circuits;
2. on every circuit `C_rho`, the native traces of its right cells are
   distinct and equal exactly to `C_rho-{rho}`;
3. every nonloop circuit contains at least one root two-shore; and
4. those nonloop root ports have exactly two colours:

\[
\begin{array}{c|c|c|l}
\text{root rank}&\text{cell depth}&\text{count}&\text{roots}\\ \hline
4&0&6&449,960,1920,8217,8218,24610\\
6&2&9&1103,2420,2676,4213,7504,9524,17683,18970,19568.
\end{array}                                                     \tag{4.1}
\]

The seven loop circuits are

\[
2575,5801,13616,13620,17738,21641,29776.             \tag{4.2}
\]

Five have root rank six and two have root rank seven.

#### Proof

The canonical alternating decomposition gives 22 closed connected components
with `N(C)=D` and sizes `|C|=|D|+1`; Lemma 3.1 proves the circuit assertion.
Taking the union of the controller letters in each right cell gives 983 distinct native
traces, and componentwise these are exactly all targets except the displayed
intersection root `rho_C`.  In particular, the native atlas itself is a
matching exposing `rho_C`; it need not be the same maximum matching used to
start the alternating-reachability proof.  Inspecting the root incidences gives nine depth-zero
two-shores in each rank-four component and one, two, or four depth-two
two-shores in each nonloop rank-six component.  The seven remaining roots
have degree zero.  The complete exact certificate is reconstructed by
`scratch/audit_threadD_h22_circuit_router_ports.py`.  \(\square\)

Thus the nonzero Hall obstruction is not short of candidate ears.  It is
short of physically legal routes that expose one of those ears at a splitter
station while carrying the entire decorated atlas.

## 5. The neutral-router groupoid

A **decorated carrier** is a tuple

\[
                         X=(T,P,A,\mathcal F,\mathcal L),         \tag{5.1}
\]

where:

* `T` is an exact middle-owner chronology;
* `P` is its nonzero maximal erosion controller and reconstructs `T`;
* `A` is one nonzero physical compiler with \(A_p\subseteq P_p\), whose central
  windows reconstruct `T`;
* `F` is a cell-disjoint, target-injective family of pins realized by this
  same `A`; and
* `L` records the protected residence and signed shadow supports.

A braid word `g:X -> Y` is a **neutral arrow** when it is invertible as a
segment rearrangement and satisfies all of the following:

1. the endpoint deck and Johnson chronology remain exact;
2. the residence and protected-support ledger `L` is unchanged;
3. the compiler matching rank and the residual root set are unchanged; and
4. `(A,F)` is transported or reselected as a physical common-controller
   certificate with the same target set and size.  The cells may be rebased;
   pointwise cell identity is not required.

Legal arrows are state-dependent, so these objects and arrows form a
groupoid `N`, not a single group acting on every carrier.  Loops at one
decorated carrier form its isotropy group, but the useful H23 router is a
transporter between two different objects.

The common-controller datum has an exact route cocycle.  For a coordinate
`a`, define the positions forbidden by a pin face `F` by

\[
 Z_a(\mathcal F)=
 \bigcup_{(I,S)\in\mathcal F:\,a\notin S} I.                    \tag{5.2}
\]

For the following cocycle projection, equip a neutral arrow `g:X -> Y` with
a functorial **reference** bijection `theta_g` of controller positions,
including an explicit convention on the seam collar.  It may be identity
indexing or marked-segment transport; it is not required to carry a rebased
source pin interval to its endpoint interval.  Require

\[
                         \theta_{hg}=\theta_h\circ\theta_g.
\]

Put

\[
 \omega_a(g)=Z_a(\mathcal F_X)\mathbin\triangle
              \theta_g^{-1}Z_a(\mathcal F_Y).                   \tag{5.3}
\]

For composable arrows `g,h`, direct cancellation of the intermediate
forbidden set gives

\[
 \omega_a(hg)=\omega_a(g)\mathbin\triangle
               \theta_g^{-1}\omega_a(h).                       \tag{5.4}
\]

Thus two routes to the same undecorated port can carry different literal pin
states.  Vanishing of (5.3) is only a necessary projection: the surviving
positive-hit sets in Lemma 3.4, physical-compiler nonzeroness, and central
reconstruction must also be transported.  If the reference bijection does
carry every pin interval with its target label, then (5.3) vanishes; otherwise
it records precisely the forbidden-set part of the rebasing defect.  This is
why both the physical compiler and full pin face belong in (5.1).

For a residual root `rho`, let `Ready_rho` be the set of decorated carriers
admitting a legal splitter which:

* applies Lemma 3.3 to `C_rho`;
* loses no protected support and preserves residence;
* extends or rebases the common-controller pin family to cover `rho`; and
* regenerates the native-atlas form on every remaining circuit while
  retaining the exterior matching.

The exact routing criterion is

\[
                 \operatorname{Orb}_{\mathcal N}(X)
                 \cap \operatorname{Ready}_{\rho}\ne\varnothing.       \tag{5.5}
\]

This is both necessary and sufficient for a neutral-router-plus-splitter
discharge of `rho` within the stated move class.

## 6. Regenerative routing theorem

### Theorem 6.1 (decorated neutral-router induction)

Let `X_0` be a decorated carrier whose residual DM shore is the disjoint union
of `d` unit circuits.  Assume the following regenerative orbit property.

For every decorated descendant `X` with residual root set `R(X)` and every
\(\rho\in R(X)\), condition (5.5) holds; moreover a splitter chosen at the
resulting ready object produces a decorated descendant with root set
`R(X)-{rho}`.

Then the circuits can be discharged in any prescribed order.  After `d`
splitters the compiler graph has no residual DM deficit, and the final
maximal controller admits one physical compiler `A` simultaneously realizing
the transported final pin family.  Every intermediate carrier preserves the
exact deck, residence, and protected supports.

#### Proof

Induct on `|R(X)|`.  For the chosen root `rho`, use (5.5) to reach a ready
object by neutral arrows.  Neutrality preserves the root set, matching rank,
ledger, and size and target set of the common-controller certificate.  Apply
the splitter.  Lemma 3.3 raises the matching rank by one; the regenerative
hypothesis returns an object of the same class with root set
`R(X)-{rho}`.  The pin family remains literal by definition, and every added
native pin passes the exact surviving-hit test in Lemma 3.4 as part of the
splitter certificate.  Repeat.  After `d` steps no circuit and
hence no Hall deficit remains.  \(\square\)

The quantifier over decorated descendants is essential.  Transitivity of an
unlabelled braid action at the initial carrier does not suffice: earlier pins
and discharged circuits may destroy later routes.

### Corollary 6.2 (two-colour H22 reduction)

Suppose the regenerative orbit property is proved for the two nonloop port
colours in (4.1), with one clean splitter seed of each colour in the same
reachable decorated H22 class.  Then all 15 nonloop H22 circuits can be
discharged and the deficiency falls from 22 to the seven-loop floor.

The already discharged root `20516` is a rank-four prototype, and the
`4877` splitter is a rank-six prototype.  This does not yet prove the
corollary: the former seed was certified in the preceding H24 orbit and used
a nonnative child-to-root deletion, whereas the latter is native in the H23
orbit.  A same-orbit regenerative certificate is still required.

## 7. A concrete transitivity amplifier

The orbit hypothesis in Theorem 6.1 has a useful sufficient condition which
does not appeal to a generic matching or nibble theorem.

### Theorem 7.1 (connected safe-swap routing)

Fix a decorated state with `n` same-colour packet ports.  Let `K` be a graph
on their positions.  Suppose that for every edge of `K` there is a
context-independent certified neutral braid word which swaps the two packet
labels, fixes all other labels, and transports the protected pin face.  If
`K` is connected, these words generate the full symmetric group `S_n` on the
ports.  If each individual orientation flip is also certified, they generate
the signed group

\[
                              C_2^n\rtimes S_n.                  \tag{7.1}
\]

Consequently any unused same-colour port can be routed to a fixed splitter
station.  After freezing used ports, the same conclusion holds provided the
induced safe-swap graph on the unused ports remains connected.

#### Proof

Edge transpositions of a connected graph generate `S_n`: along a path one
conjugates adjacent edge transpositions to exchange its endpoints, and all
transpositions generate `S_n`.  Independent flips give the normal subgroup
`C_2^n`, on which `S_n` acts by permuting coordinates, proving (7.1).  The
last statement applies the same argument to the pointwise stabilizer of the
frozen positions.  \(\square\)

The word “context-independent” carries the physical burden.  It requires the
new seams, all depth collars, the common-controller face, and the matching
complement to remain legal in every allowed surrounding order.  Abstract
block permutations do not imply it.  The single router in (0.1) supplies one
edge in such a Schreier graph, not its connectivity.

## 8. Exact obstruction at the zero components

For a target `S`, let

\[
              d_S=|\{\text{compiler cells whose shore contains }S\}|.  \tag{8.1}
\]

Call a neutral arrow **occurrence-neutral** when it preserves every `d_S` in
(8.1).  Every word in the subgroupoid generated by such arrows preserves the
entire target-degree vector and, in particular, the zero set.  The restricted
identity (2.2)--(2.3) explains the name but, because the physical cells have
exterior neighbours, does not by itself prove that an arbitrary physical
associator is globally occurrence-neutral.

### Proposition 8.1 (zero-incidence obstruction)

No occurrence-neutral router word can move a positive root-edge splitter to
any target in (4.2).  A circuit with `d_S=0` can leave the zero floor only
through a generator whose signed incidence derivative is positive at `S`.

#### Proof

Equation (8.1) is invariant under every generator and therefore under their
compositions.  A root-edge splitter requires a cell incident with `S`, so it
cannot occur in an orbit with `d_S=0`.  \(\square\)

The proposition does not forbid a neutral word from routing the chronology
to a *creator-ready context* while `d_S` remains zero.  It says only that the
subsequent creator is genuinely non-occurrence-neutral at `S`.

Thus “the neutral braid group routes a splitter to every remaining circuit”
is false for the occurrence-neutral subgroup.  A broader Hall-neutral
groupoid could in principle contain a degree-creating arrow, but none is
currently certified.  With the known primitives, the correct architecture
has two layers:

1. neutral routing plus root-edge splitting for the 15 positive circuits;
2. creator plus compensating rank repair for the seven loops.

There is already an exact finite example of the second layer:

\[
 (22,7)\xrightarrow{\operatorname{FF}(882,2606,3222)}(23,6)
 \xrightarrow{\operatorname{RF}(1500,4943,6184)}(22,6).        \tag{8.2}
\]

The first arrow creates a candidate for `2575` while temporarily losing one
matching rank and some lower support; the second restores the Hall rank and
all lost supports.  The final carrier has lower-hole vector
`(4,18,6,1,0,0,0)` and all upper layers complete.

### 8.1 Exact one-braid boundary and the zero-six common controller

The current-source exhaustive one-braid scan sharpens the scope of (8.2).
Both scans use `scratch/search_k15_segment_braid_native.cpp` at SHA-256
`889379685f55e1938f24fceffd889951332966fe547021874b5482b1c2fa7d29`.
From canonical `(22,7)`, exactly 9164 parameterized FF/RF/FR/RR move
encodings are simultaneously resident and all-upper-safe.  This count
includes the repeated `RR(a,a,a)` identity encodings; it is not a count of
distinct neighbour carriers.  None gives H21, and none gives `(22,6)`.  The
move `FF(882,2606,3222)` is the unique zero-reducing neighbour and has score
`(23,6)`.  Thus no one-braid Hall-neutral zero creator exists at this state.

At the final `(22,6)` carrier, 9073 parameterized encodings pass the same
safety tests.  None gives H21, and none gives zero count five at any Hall
score.  Hence both ends
of (8.2) are one-braid local minima in the relevant Pareto directions; the
creator/compensator composition is genuinely necessary within this
catalogue.

The `(22,6)` carrier is `scratch/k15_segment_braid_hall22_zero6.json`, SHA-256
`bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778`.

There is an exact critical-shore common-controller lift at `(22,6)`.  The new
nonzero component is

\[
                         \{2575,2607\}/\{17342\}.                \tag{8.3}
\]

Cell 17342 has depth two, start 4467, and native trace `2607`.  Retargeting it
to `2575` deletes zero-based coordinate 5 on positions 4467--4469; all 984
selected DM-shore pins, every central window, and physical-word nonzeroness pass
the exact test.  This serves `2575` but displaces `2607`, so it does not
discharge (8.3) or improve Hall rank.  It is not a global 16361-pin
certificate.  Here too the maximal controller `P` is fixed: the three changed
rank-five letters are physical `A` letters pinned down to rank four.

The earlier putative free cell `5617` is not an alternative.  In this carrier
it is a depth-zero cell with envelope `2574`; coordinate pinning cannot add
the missing bit to obtain rank-six target `2575`.  The corrected target is a
graded split: create a distinct **depth-one native** cell for `2575` while
retaining a **depth-two native** cell for `2607`.  After reserving both cells
and both targets, the exact exterior-rank requirement is `16360`.  The full
forced-pair min-cut and collar-current theorem is recorded in
`THREAD_D_H22_GRADED_2575_2607_FORCED_PAIR_MINCUT_20260728.md`.

The exact next finite target is therefore a two-braid plateau-router plus
splitter from `(22,6)`, preferably on one of its six `2/1` circuits:

\[
\begin{gathered}
\{2420,2932\},\ \{2575,2607\},\ \{2676,10868\},\\
\{9524,9588\},\ \{17683,21779\},\ \{19568,27760\}.
\end{gathered}                                                  \tag{8.4}
\]

## 9. What is proved and the precise next theorem

The H23-to-H22 pair proves all of the following.

* A neutral braid can be a necessary legality router for a remote splitter.
* The router can preserve the exact DM root set and transport the same
  984-target native common-controller basis.
* The splitter can augment that basis to 985 simultaneous native pins while
  discharging one circuit and losing no protected support.
* Together with the preceding `20516` discharge, the final pinned physical
  compiler `A` realizes 1146 pins on the old 1168-target H24 shore, missing
  exactly the current 22 roots.  Common-controller regeneration therefore
  survives two successive component discharges.
* The relevant local port types at H22 collapse to two nonloop colours.

The common-controller statement is presently confined to the nested critical
shores: 985 of the H23 shore's 1007 targets, and cumulatively 1146 of the H24
shore's 1168 targets, are simultaneously pinned in the H22 endpoint.  Neither
is a global 16361-target literal-word certificate.  Any full induction must
carry an exterior pin face as part of the decoration in (5.1).

The sharp next theorem is therefore:

> Construct, on the decorated H22 class, a safe-swap Schreier graph which
> remains connected within each of the two colours in (4.1) after every
> prior root discharge; place one regenerative clean splitter station in
> each colour orbit; and transport the exterior common-controller face.

That theorem would give H7 by Corollary 6.2.  To reach H0 one must add a
rank-six and rank-seven zero-creator orbit, or a compound creator/compensator
which generalizes (8.2).  A proof of unlabelled carrier connectivity, or a
single additional neutral pair, is insufficient.

## 10. Exact audit artifacts

* `scratch/audit_k15_segment_braid_descent.py`;
* `scratch/k15_segment_braid_h22_router_splitter_audit_20260728.json`;
* `scratch/audit_k15_h22_router_splitter_structure.py`;
* `scratch/audit_k15_h22_router_splitter_common_q.py`;
* `scratch/k15_h22_router_splitter_common_q_certificate.json`;
* `scratch/audit_k15_h22_cumulative_h24_common_q.py`;
* `scratch/k15_h22_cumulative_h24_common_q_certificate.json`;
* `scratch/k15_hall22_native_dm_pins_certificate.json`;
* `scratch/audit_threadD_h22_circuit_router_ports.py`;
* `scratch/k15_segment_braid_hall23.json`;
* `scratch/k15_segment_braid_hall23_portal.json`;
* `scratch/k15_segment_braid_hall22.json`;
* `scratch/k15_segment_braid_hall23_zero6_from22.json`;
* `scratch/k15_segment_braid_hall22_zero6.json`;
* `scratch/threadD_h22_one_braid_scan_20260728.txt`;
* `scratch/threadD_h22_zero6_one_braid_scan_20260728.txt`;
* `scratch/audit_threadD_h22_zero6_common_q.py`;
* `scratch/threadD_h22_zero6_common_q_certificate_20260728.json`.
