# From the saturated coatom Pluecker lattice to physical lift and terminal common-cap return

> **Correction, 2026-08-01.**  The native identity-cap basis and formal
> four-block `C8` source relation remain valid.  The literal Klein
> `0110<->1001` concatenation is not a simple-owner/strict-q1 carrier;
> see `scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py`.
> Therefore Theorem 2.2's physical strict-rainbow conclusion is conditional
> on a nonliteral quotient weave which removes the audited owner/palette
> multiplicities while retaining the native basis.  It may not be used as
> an unconditional physical CBC lift.

Date: 2026-08-01  
Lane: Thread D, additive-constant terminal compiler  
Status: exact separation theorem, exact disjunctive Hall/return formula, and
two exact cancellation interfaces.  No all-dimensional physical planting or
bounded-compiler theorem is claimed.

## 0. Verdict

The authoritative algebraic input is

`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`.

For one filler ordering `pi`, the complete lower action is the
antisymmetric maximal-chain signature

\[
 A(\pi)_t=e_{P_t(\pi)}-e_{S_t(\pi)},\qquad 1\le t<d,
\]

and the integer span of all such common-order signatures is the saturated
lattice `U_d`.  At depth two, labelled Johnson squares generate the complete
fixed-coordinate-degree lattice.  The new endpoint-planted one-block-order
breaker lies outside this common-order module: it preserves the complete
safe upper/residence interface while changing the reflected pair current by
one pair-layer Johnson square.  Varying labels makes those breaker currents
span the complete fixed-degree extreme pair-current kernel.  More strongly,
allowing every internal adjacent block twist gives a pure Johnson square at
each chosen depth and spans the saturated direct product of all depthwise
fixed-degree lattices.  Consequently the old reflection law is not a
safe-move invariant and there is no remaining formal coupled-depth quotient.

This note isolates what remains after that closure.

1. **Physical lift.**  A formal integer expression in packet signatures is
   not a walk in a carrier.  The required packet must be present, with the
   required orientation, at the current word.  Even at `q=2`, an induced
   occurrence-labelled `C_6` is a sharp obstruction to square-only
   reachability.
2. **Cancellation beyond one filler flag.**  Opposite common-order
   commutators on two filler cores cancel the forced reflected companion and
   leave a `q=2` core transfer.  More decisively, a single-block adjacent
   twist breaks that companion law.  For zero total action, the strict
   lower-rainbow prepared-slot primitive is the four-packet twisted cube;
   the shorter three-packet triangle repeats q1 socket colours.
3. **Nonlinear compiler.**  Restoring every unaddressed lower occurrence
   counter does not restore a compiler.  For a fixed complete cap/trace
   state the terminal condition is a bipartite matching, but the actual
   compiler is a **disjunction** over such states.  The exact residual defect
   after any packet circuit is the minimum, over compatible cap states, of a
   Hall deficiency.  Taking the union of their edge sets is unsound.

For one canonical packet this formula specializes to the previously proved
return-Hall deficiency `2(d-1)-nu(R)`.  Its local trace-guarded return graph
is empty, so the local deficiency is `2(d-1)`.  Serial moves remove every
intermediate compiler obligation, but they do not remove this terminal
address/cap gate.

## 1. The safe carrier groupoid, not the catalogue lattice

Let `Gamma^+` be the enlarged safe-carrier graph.  Its vertices are resident,
upper-safe simple Johnson chronologies, and an oriented edge

\[
                            e:T\longrightarrow T'
\]

is one literally planted reversible coatom replacement.  Let

\[
 \sigma(e)=\bigl({\cal L}_q(T')-{\cal L}_q(T)\bigr)_{q=2}^d
                                                               \tag{1.1}
\]

be its complete signed lower-occurrence action.  Let `Gamma^com` be the
common-order canonical subgraph.  For that subgraph, every edge label is a
labelled image of an element of `U_d`.  Since a walk may change cores and
filler frames, define the global common-order module

\[
 U^{\rm glob}_{k,r,d}=\sum_\phi \phi_*(U_d),                    \tag{1.1a}
\]

where `phi` ranges over valid labelled common-order packet embeddings into
the global occurrence deck.  Every edge of `Gamma^com` lies in this module
and obeys the common-order reflected pair-degree constraints.

The enlarged graph `Gamma^+` also contains the endpoint-planted
single-block-order breaker.  Its label is not constrained by `U_d` and does
not preserve the reflected pair current.  Put

\[
 V^{\rm cat}_{k,r,d}=\operatorname{span}_{\mathbb Z}
          \{\sigma(e):e\text{ is an allowed enlarged-catalogue edge}\}.
                                                               \tag{1.1b}
\]

### Proposition 1.1 (telescoping physical action)

For every directed safe walk

\[
 W=(T_0,T_1,\ldots,T_s)
\]

one has

\[
 \sum_{i=0}^{s-1}\sigma(T_i,T_{i+1})
       =\bigl({\cal L}_q(T_s)-{\cal L}_q(T_0)\bigr)_{q=2}^d.
                                                               \tag{1.2}
\]

Thus the actions physically reachable from `T_0` in `Gamma^+` form the set

\[
 {\cal A}(T_0)=\{({\cal L}_q(T)-{\cal L}_q(T_0))_{q=2}^d:
                     T\in\operatorname{Comp}_{\Gamma^+}(T_0)\}
       \subseteq V^{\rm cat}_{k,r,d}.                            \tag{1.3}
\]

For a walk restricted to `Gamma^com`, the stronger inclusion in
`U^(glob)_(k,r,d)` and the reflected pair invariant hold.  They need not
hold in `Gamma^+`.

There is no converse inclusion in general.

#### Proof

Equation (1.2) telescopes coordinatewise.  Each summand is an enlarged
catalogue column by definition of `V^(cat)`, proving (1.3); common-order
summands lie in the smaller labelled flag module.  The reverse
inclusion would assert availability and orderability of every formal
generator; neither follows from an integer-span calculation.  For example,
a carrier with no planted slot has reachable action set `{0}` although the
catalogue lattice is nonzero.  A nontrivial occurrence-labelled obstruction
is given next. \(\square\)

### Proposition 1.2 (the first nonnegative physical obstruction)

Let the physically allowed `q=2` occurrence support be an induced bipartite
cycle `C_6`.  Give every support vertex degree one.  The two alternating
perfect matchings have the same row and column degrees, hence their
difference is in the saturated Pluecker lattice, but no supported Johnson
square is available.  They are disconnected by square packets.

More generally, all even occurrence circuits connect every nonnegative
degree fibre.  Squares alone connect every such fibre exactly when the
support is chordal bipartite, provided the square atlas is
**regeneratively transparent**: after every preceding switch, every square
invoked by the decomposition remains a literal safe packet lift at the
current occurrence assignment.

#### Proof

The two alternating matchings of an induced `C_6` are the whole degree-one
fibre.  An induced `C_6` has no four-cycle, hence there is no supported
square move.  For the general statement, color the positive and negative
copies of the discrepancy between two tables.  Equal degrees decompose the
discrepancy into alternating even circuits.  Chords split a circuit
conformally until only squares remain.  Conversely, any induced even cycle
of length at least six gives the same degree-one obstruction. \(\square\)

This is the exact distinction between a catalogue Markov lattice and an
occurrence-labelled physical Markov basis.

The even-circuit assertion is an abstract nonnegative table theorem.  To
promote it to carrier reachability, every chordless circuit used by the
decomposition must itself have a literal regenerative safe macro; a signed
circuit vector in the support graph is not automatically a packet.

## 2. Common-order cancellation and the reflection-breaking extension

Inside the common-order subcatalogue, the complement relation in one flag
forces a depth-two square to carry a reflected deep companion.  It can be
removed by mixing flags, or bypassed by the planted block-order breaker.

### 2.1 Two-core commutator

Assume `d>=3`.  (At `d=2`, the two reflected layers coincide and the
adjacent swap gives twice one `q=2` square, not a two-core transfer.)

Write

\[
 F=I\mathbin{\dot\cup}\{x,y\},\qquad |I|=d-2,
\]

and compare filler orders `(x,y,I)` and `(y,x,I)`.  Their signature
difference vanishes at every layer except `t=1,d-1`.  After physical target
embedding it is the pair

\[
 Q_G(a,b;x,y)\quad(q=d),\qquad
 Q_{G\cup I}(a,b;x,y)\quad(q=2),                     \tag{2.1}
\]

with the same orientation, where

\[
 Q_R(a,b;x,y)=e_{R+a+x}+e_{R+b+y}-e_{R+b+x}-e_{R+a+y}.
                                                               \tag{2.2}
\]

Use a second internal core `J` with the opposite commutator.  The common
deep square cancels and the total action is

\[
 Q_{G\cup I}(a,b;x,y)-Q_{G\cup J}(a,b;x,y)            \tag{2.3}
\]

at `q=2`, and zero at every other depth.

Equation (2.3) is an exact **cross-flag algebraic cancellation**.  It is a
physical move only if all four packet phases occur in an orderable safe
macro (or as a safe serial walk).  Lattice saturation does not provide
those four slots.

### 2.2 Owner-disjoint active-label triangle

There is also a literal prepared-slot zero-action macro.  Fix a common
internal flag and third active label `c`, and use the three ordered active
pairs

\[
                         (x,y),\quad(y,z),\quad(z,x).           \tag{2.4}
\]

Give the packets private extreme fillers and one private active label each.
The resulting complete owner sets are pairwise disjoint.  At every depth,
the one-packet action is a potential difference

\[
                    \Delta_q(a,b\mid c)=v_q(ca)-v_q(cb),       \tag{2.5}
\]

so

\[
 \Delta_q(x,y\mid c)+\Delta_q(y,z\mid c)
                     +\Delta_q(z,x\mid c)=0
             \qquad(1\le q\le d).                              \tag{2.6}
\]

Each replacement separately preserves its owners, immediate palette,
complete interval-OR deck, simple topology, and residence.  Thus (2.6) is a
coefficientwise all-depth cancellation on three owner-disjoint prepared
slots.  However, the rows repeat one lower-q1 socket colour at each flag
vertex, so they cannot be inserted unchanged into a strict lower-rainbow
bank.  The explicit construction uses
`r+11` coordinates and hence fits a `2r` middle-level ground whenever

\[
                           r\ge\max\{d+4,11\}.                   \tag{2.6a}
\]

Three is minimal in the pairwise-owner-disjoint common-flag canonical
ansatz.  Two cancelling packets must be inverse on the same active edge;
their common depth-two union is the same upper-screen owner, so two distinct
slots collide.  Applying the inverse to the same slot is only a backtrack.

The two mechanisms have different scope.  The two-core commutator can
transport a `q=2` square between filler cores while cancelling all deeper
action, but its physical four-slot lift is open.  The triangle is
owner-disjoint but not strict-rainbow compatible.  The four-packet twisted
cube below removes that palette collision.

### Theorem 2.1 (the triangle carries a zero-defect native partial basis)

In the prepared owner-disjoint triangle, fix `2<=q<=d`.  Each packet has
its two native maximal-erosion cells, so the three slots supply six distinct
physical cells.  In either endpoint phase:

1. the six cell values are six distinct lower targets;
2. the set of six target values is the same in the two phases;
3. phase change permutes them by the two opposite directed 3-cycles on the
   prefix and suffix profiles; and
4. assigning every current target to its native cell changes no source
   letter and is therefore jointly trace-safe.

Consequently the `6(d-1)` deep support-difference obligations have a
zero-defect partial compiler matching in both endpoint phases, on the same
physical cell set.  The `q=1` cells are three closed two-column hinges.

#### Proof

For one packet and one depth, the native cell value is the union of the
maximal-erosion letters on that cell.  Every such letter is a subset of the
union, so capping the cell by its value fixes every source letter on the
cell.  All native caps at all depths therefore coexist: each is an identity
operation on the source word.

Across the active pairs `(x,y),(y,z),(z,x)`, the prefix targets carry
`x,y,z` once each, and the suffix targets carry `x,y,z` once each.  Phase
change rotates the prefix occurrences in one direction and the suffix
occurrences in the other, exactly as in (2.5)--(2.6).  Private slots make
the physical cells distinct.  For different depths the target ranks
`r-q` differ, and the native intervals have different endpoints or lengths;
hence neither targets nor cells collide across depths.  This proves all four assertions and the
partial matching statement. \(\square\)

The theorem is stronger than unaddressed counter cancellation, but it is
still only a non-strict-rainbow partial basis.  Exterior targets may lose or gain trace-guarded
incidences when the packet chronologies change, and their caps must coexist
with one another.  Extending the native basis is exactly the residual
common-cap problem of Section 4.

### 2.3 Rainbow-compatible twisted cube

Use four common-order packets whose active/filler roles are the four faces
of the authenticated twisted cube: two use one neutral filler order and two
use its reverse.  They have pairwise-disjoint owner sets, complete q1
intersection palettes, and adjacent-union supports.  Their all-depth actions
satisfy

\[
                           \Delta_q^0+\Delta_q^1
                              +\Delta_q^2+\Delta_q^3=0
                    \qquad(1\le q\le d).                        \tag{2.6b}
\]

The construction uses `r+14` coordinates and fits a `2r` ground for

\[
                           r\ge\max\{d+4,14\}.                   \tag{2.6c}
\]

### Theorem 2.2 (strict-rainbow prepared-slot absorber)

If a strict lower-rainbow safe carrier contains the four certified old
slots with collision-free exterior attachments, the four replacements can
be made in any order.  Every intermediate carrier preserves the full safe
owner/palette/upper/residence interface, and the terminal lower occurrence
counter agrees coefficientwise with the initial counter at every depth.

At each `2<=q<=d`, the eight native maximal-erosion cells carry the same
eight distinct target values in the two endpoint phases, permuted by the
cube cancellation pairing.  Because every native target is the union of
the source letters on its cell, these eight assignments are identity caps.
Hence the twisted cube has a zero-defect native partial compiler basis of
size `8(d-1)` on the same physical cell set in both phases.

#### Proof

The owner, q1-palette, adjacent-union and all-depth counter statements are
the twisted-cube theorem.  Pairwise resource disjointness makes the four
certified replacements order-independent.  For the final assertion, apply
the native-cell identity from Theorem 2.1 packet by packet.  At fixed depth
the eight values are explicitly

```text
A-profile: E000, E100, E111, E011;
B-profile: E110, E010, E001, E101,
```

in the notation of the twisted-cube theorem; the eight cube triples are
distinct.  Equation (2.6b) permutes this set between phases.  Different
depths have different target ranks and different native intervals.  Thus
all `8(d-1)` target and cell vertices are distinct, while each native cap
fixes every source letter on its own cell. \(\square\)

This is the current strict physical zero-action primitive.  It still needs
global slot planting and extension of the native partial basis through the
nonlinear exterior compiler bank.

### 2.4 Prepared-slot packing kernel

There is an exact finite physical criterion before one tackles regenerative
serial reuse.  Let `P` be a catalogue of individually certified packet
slots in one carrier.  Let `A` have their complete all-depth signed actions
as columns.  Let `K` be the conflict graph which joins two slots whenever
they share an owner/resource or one replacement can alter the other's
certified fragment or collar.

Call a macro **`K`-resource-disjoint** when it is required, by definition,
to choose a stable set of this conservative conflict graph.  This is a
prepared-slot subclass of all orderable macros; a pair joined in `K` might
still admit a benign, more delicate sequential interaction outside this
subclass.

### Theorem 2.3 (order-independent physical zero-action macro)

Within this prepared-slot catalogue, a subset of slots is a
`K`-resource-disjoint order-independent zero-action macro if and only if its
indicator `x` satisfies

\[
                  x\in\{0,1\}^{P},\qquad Ax=0,
                  \qquad x_p+x_{p'}\le1\quad(pp'\in E(K)).      \tag{2.7}
\]

Equivalent resource rows may replace the pairwise conflict inequalities.

#### Proof

The stable-set inequalities make every selected certified replacement
disjoint from every other selected fragment, owner bank, and collar.  Thus
no toggle invalidates another slot, they may be applied in any order, and
their total occurrence action is the column sum `Ax`.  Hence (2.7) is
sufficient.  Conversely, a macro in this declared
`K`-resource-disjoint ansatz cannot contain a conflict edge, and zero terminal
action forces its column sum to vanish. \(\square\)

The saturated lattice describes the unrestricted integer span of columns.
The physical prepared-slot problem is its intersection with a `0/1`
packing face.  The triangle is a size-three owner-feasible point but
violates the strict q1-palette rows; the twisted cube is a size-four feasible
point after those rows are included.  The formal two-packet inverse relation
is cut off by one owner-conflict row.  Serial
regeneration can be strictly stronger than (2.7), because resources may be
reused after the current carrier is recomputed.

### 2.5 Exact common-order companion-kernel formulation

The two-core construction is the first case of an exact finite criterion.
Fix one paired layer `t,d-t` with `1<=t<d/2` and a library `C_t` of adjacent-swap
commutators on a common filler ground `F`.  Let `L_t` and `L_(d-t)` be the
zero-sum integer lattices on the `t`- and `(d-t)`-subsets of `F`, with the
fixed active/core embedding understood.  For `c in C_t`, write its two
nonzero layer actions as

\[
                         (g_c,h_c)\in L_t\oplus L_{d-t}.         \tag{2.8}
\]

Define integer column maps

\[
 G:\mathbb Z^{C_t}\to L_t,\quad e_c\mapsto g_c,
 \qquad
 H:\mathbb Z^{C_t}\to L_{d-t},\quad e_c\mapsto h_c.            \tag{2.9}
\]

Then the exact **formal** cancellation lattice visible in layer `t` while
the reflected companion vanishes is

\[
                              G(\ker_{\mathbb Z}H).              \tag{2.10}
\]

For `z` in this lattice, the minimum separated-commutator cost, when every
named commutator is treated as an indivisible two-packet macro, is

\[
 \tau_t(z)=2\min\{\|n\|_1:Hn=0,\ Gn=z,\ n\in\mathbb Z^{C_t}\}. \tag{2.11}
\]

The factor two appears because one atomic commutator is a difference of two
packet phases.  If different commutators share literal packet phases, an
unrestricted packet word may cancel those phases and cost less than
(2.11); no such cross-atom discount is included in `tau_t`.  If two columns
have the same companion `h`, then `n=e_c-e_(c')` is a generic four-packet
companion cancellation; it is
exactly the two-core transfer (2.3) only when the two columns are the
specific cores `I,J` used there.

Equations (2.10)--(2.11) become a physical reachability theorem only under a
regenerative lift hypothesis: every signed commutator used by `n` must be
available at the current carrier, and after it is applied the remaining
word must still be orderable.  Simultaneous use additionally requires
owner/resource packing; a serial regenerative atlas may reuse resources.

#### Proof

A coefficient vector `n` has zero reflected action exactly when `Hn=0`,
and its surviving layer action is then `Gn`.  Each unit of `|n_c|` uses the
two packet phases defining that oriented commutator, giving (2.11).
Physicality is an additional lift property and is not encoded by the two
integer column maps. \(\square\)

### Corollary 2.4 (fixed-frame companion cancellation is trivial)

If every commutator in `C_t` uses one fixed filler frame, let

\[
 {\cal C}:L_t\longrightarrow L_{d-t},\qquad
                 e_X-e_Y\longmapsto e_{F-X}-e_{F-Y}             \tag{2.12}
\]

be the complement isomorphism.  The flag reflection law gives

\[
                              H=-{\cal C}\,G.                    \tag{2.13}
\]

Therefore `ker(H)=ker(G)` and

\[
                              G(\ker H)=\{0\}.                   \tag{2.14}
\]

So a nonzero action with its reflected companion cancelled cannot be built
inside one fixed filler frame.  It must genuinely mix cores/frames, as in
(2.3), or use a packet family with a different depth profile.  This is a
reflection obstruction, not an unsaturated-lattice obstruction.

For a finite physical library this gate is exactly computable.  If `K_H`
is an integral kernel basis for `H`, then the companion-free transfer
lattice is the integer image of `G K_H`; Smith normal form of that matrix
gives all residual ranks and congruences.  Any resulting index belongs to
the restricted **physical cross-frame library**, not to the saturated
single-flag lattice `U_d`.

### 2.6 The planted block-order breaker kills the extreme reflection-current quotient

Return now to the **current endpoint-planted schedule** with upper screens
at transitions `{0,2,4,6,8,10}`.  Keep the planted first `Iab` omission
order

```text
p,f1,...,fd,f0
```

and swap `f1,f2` only in the label-attached `Ica` block, in both packet
phases.  The authenticated breaker preserves the owner deck, simple
topology, both q1 palettes, the complete interval-OR support, endpoints and
the depth-`d` run floor.  Its reflected pair-current defect is

\[
 B(f_0,p;f_1,f_2)
  =e_{f_0f_1}-e_{f_0f_2}-e_{pf_1}+e_{pf_2}.                    \tag{2.15}
\]

For a coordinate set `Omega`, define

\[
 \partial_2:\mathbb Z^{\binom{\Omega}{2}}\longrightarrow
       \mathbb Z^\Omega,qquad e_{xy}\longmapsto e_x+e_y.       \tag{2.16}
\]

### Theorem 2.5 (full fixed-degree extreme-current span)

Assume `d>=3`, `r>=d+4`, and an ambient ground of at least `r+5`
coordinates, so every prescribed choice of the four displayed roles extends
to fresh labels for the remaining packet template.  The integer span of the
**extreme** `q=2` versus `q=d` pair-current defects of all relabelled
one-block breakers is exactly

\[
                              \ker_{\mathbb Z}\partial_2.       \tag{2.17}
\]

The lattice is saturated.  Hence the common-order extreme reflected pair
current has no residual congruence or linear invariant after the breaker
catalogue is admitted, beyond its forced coordinate degrees.

#### Proof

Every vector (2.15) has zero coordinate degrees.  Conversely, prescribe any
four distinct coordinates `u,v,x,y` to the roles `f0,p,f1,f2` and relabel
the remaining packet roles with fresh coordinates.  The resulting safe
breaker has reflected defect

\[
                    e_{ux}-e_{uy}-e_{vx}+e_{vy},                \tag{2.18}
\]

an arbitrary Johnson square in the pair layer.  The uniform-degree lattice
theorem at `s=2` says that these squares generate
`ker_Z(partial_2)` integrally. \(\square\)

For one fixed aperture pair `(f0,p)`, relabelling the two swapped internal
roles `(f1,f2)` through a label bank generates

\[
 (e_{f_0}-e_p)\otimes
       \{z\in\mathbb Z^{\{f_1,\ldots,f_d\}}:\sum z_i=0\},       \tag{2.19}
\]

with root-to-label differences giving a triangular integral basis.  This is
a catalogue of separately labelled first-adjacent twists, not a claim that
arbitrary adjacent positions in one fixed block have the same defect.
Varying the aperture labels gives all squares in (2.18).

Theorem 2.5 is a catalogue-span theorem.  It does not say that a fixed safe
carrier contains the prescribed breaker slots in a serially usable order.
By itself it concerns only the extreme reflected pair-current projection;
the single frozen `s=1` breaker does not close every intermediate paired
depth.

### 2.7 All internal block twists give the full product

The internal-twist theorem strengthens the single breaker.  Swap any
adjacent internal omissions `f_s,f_(s+1)`, `1<=s<=d-1`, in the attached
`Ica` block.  If `C_s` is its correction relative to the common-order
packet, then the four-column role-swap commutator

\[
                         C_s-(p\ b)C_s
\]

cancels every depth except `q=s+1`, where it leaves an arbitrary
coefficient-one Johnson square.  Consequently, under

\[
                         r\ge d+4,\qquad k\ge r+4,
\]

the enlarged signed catalogue satisfies

\[
 \boxed{
 \operatorname{span}_{\mathbb Z}(\text{common-order packets and all
 relabelled internal twists})
   =\bigoplus_{q=2}^d\ker_{\mathbb Z}\partial_{r-q}.}           \tag{2.20}
\]

This full-product lattice is saturated.  If `k>=r+5`, comparing two twists
which differ only in a fresh extreme role `p'` gives the same isolator with
two columns, and the common-order columns are redundant.  Thus the complete
formal coupled-depth quotient is zero once all safe internal twists are
admitted.

The fresh-role twist pair shares all planted upper-screen owners and cannot
occupy two owner-disjoint slots.  The sharp role-swap commutator uses four
signed columns from two labellings; within each labelling its twisted and
common-order columns have coincident owner sets.  Thus it has no
simultaneous owner-disjoint four-slot lift, and no serial lift is proved.
Equation (2.20) is therefore signed catalogue algebra, not a physical
serial theorem.  The exact next target is a regenerative or triangular
resource-disjoint lift of these pure-square differences.

### 2.8 Exact finite physical action-matrix gate

Let `P` be any finite **physically present** library of common-order packets,
commutators, and block-order breakers.  Let

\[
 A:\mathbb Z^P\longrightarrow
       \bigoplus_{q=2}^d\mathbb Z^{{\cal T}_q}                  \tag{2.21}
\]

be its complete action matrix.  For a selected coordinate set `J`, split
`A=(A_J,A_rest)`.  The exact formal lattice isolated on `J` is

\[
                         A_J(\ker_{\mathbb Z}A_{rest}).          \tag{2.22}
\]

An integral kernel basis `K_rest` makes this the image of `A_J K_rest`, so
Smith normal form gives every rank and congruence of the finite atlas.  The
common-order companion formula (2.10) is the two-layer special case.  The
unrestricted labelled twist catalogue has the full span (2.20), while a
finite carrier atlas may have a smaller image.

As before, (2.22) is physically reachable only when its signed columns have
a regenerative safe lift or a resource-compatible prepared-slot packing.

## 3. Exact nonlinear compiler state

Fix a terminal safe carrier `T`.  Let `L` be the set of required lower
target obligations and `C` the set of physical source cells which may serve
them.  A **complete cap state** `theta` records every global choice needed
before the remaining target-to-cell selection is a matching problem:

* the nonzero source antecedent/common cap;
* all fixed pins and boundary choices;
* the middle-row trace equalities;
* residence and protected upper witnesses; and
* every other choice whose compatibility is shared by more than one
  target-cell incidence.

Let `Theta(T)` be the set of legal complete cap states.  For
`theta in Theta(T)`, let

\[
 G_\theta(T)=(L,C;E_\theta)                                  \tag{3.1}
\]

be the graph of incidences which are literally legal under that **same**
state.  Structural zeros caused by exact erosion, nonzeroness, or a fixed
pin are absent from `E_theta`.

There is also a direct selector description which does not enumerate cap
states.  Let `bar E_p` be the pinned maximal envelope and let
`x_(S,C) in {0,1}` select target `S` on cell `C`.  The maximal cap forced by
the selection is

\[
 A_p(x)=\bar E_p\cap
       \bigcap_{(S,C):x_{S,C}=1,\ p\in C}S.                     \tag{3.1a}
\]

The selection is a literal compiler if and only if it is a target-cell
**target-saturating** matching,

\[
 \sum_C x_{S,C}=1\quad(S\in L),\qquad
 \sum_S x_{S,C_0}\le1\quad(C_0\in C),                          \tag{3.1b}
\]

and

\[
\begin{aligned}
 A_p(x)&\ne\varnothing &&\quad\text{for every source position }p,\\
 \bigcup_{p\in D}A_p(x)&=R &&\quad\text{for every protected row }(R,D),\\
 \bigcup_{p\in C}A_p(x)&=S &&\quad\text{for every selected }(S,C).
\end{aligned}                                                  \tag{3.1c}
\]

Indeed, (3.1a) is the coordinatewise largest word compatible with all
selected caps.  If it fails one equality, no smaller word can restore the
missing coordinate; if it passes, it is the required compiler.  This is
the exact nonlinear replay hidden inside `Theta(T)`.

### Theorem 3.1 (disjunctive common-cap matching formula)

The exact terminal compiler deficiency is

\[
 \boxed{
 \lambda(T)=|L|-\max_{\theta\in\Theta(T)}\nu(G_\theta(T))
 =\min_{\theta\in\Theta(T)}
       \max_{X\subseteq L}\bigl(|X|-|N_{G_\theta(T)}(X)|\bigr)_+ .}
                                                               \tag{3.2}
\]

If `Theta(T)` is empty, set `lambda(T)=+infinity`.

#### Proof

For a fixed complete cap state, all shared nonlinear choices have been
resolved.  The remaining problem is exactly a bipartite matching, so Hall's
deficiency theorem gives

\[
 |L|-\nu(G_\theta)=\max_{X\subseteq L}
                         (|X|-|N_{G_\theta}(X)|)_+.
\]

The compiler may choose the best legal cap state, yielding (3.2). \(\square\)

### Proposition 3.2 (the union graph is unsound)

It is in general false that

\[
 \lambda(T)=|L|-\nu\!\left(\bigcup_{\theta}G_\theta(T)\right).
                                                               \tag{3.3}
\]

The smallest counterexample has targets `r_1,r_2`, cells `c_1,c_2`, and
two cap states.  In state zero, only `r_1` has incidences, to both cells.  In
state one, only `r_2` has incidences, to both cells.  Each legal graph has
matching rank one, while their union has a perfect matching.

Thus fixed coordinate degrees, complete unaddressed target multiplicities,
and even the marginal union of all trace-guarded incidences do not imply a
common compiler.  The nonlinear obstruction is the quantifier order

\[
                  \exists\theta\;\exists M\subseteq E_\theta,
\]

not a matching in `union_theta E_theta`.

### Proposition 3.3 (literal two-position common-cap obstruction)

The failure occurs in the exact interval compiler, not only in an abstract
disjunction.  Take positions `0,1`, one middle row on both positions with

\[
                   E_0=E_1=T=\{o,a,x\},                         \tag{3.4}
\]

the two singleton source cells, and lower targets

\[
                         S_0=\{o\},\qquad S_1=\{o,x\}.           \tag{3.5}
\]

Every one of the four target-cell incidences is individually exact.  The
marginal graph is `K_(2,2)` and has two perfect matchings.  Nevertheless,
every perfect matching caps the two positions by `S_0,S_1` in some order,
so their union is `{o,x}` and the protected middle bit `a` disappears.  No
exact common compiler exists.

Thus a complete Pluecker rectangle can connect the two marginal perfect
matchings while the exact compiler subset of that fibre is empty.  In the
state formulation of Theorem 3.1, the four marginal edges do not coexist in
one legal complete state.  Equivalently, the two perfect-matching diagonals
are minimal forbidden sets in the cap-conflict clutter.

For later separation it is useful to state that clutter exactly.  Let
`E_marg` contain every individually sound incidence, and let `F_cap` be the
inclusion-minimal **matching-compatible** subsets of `E_marg` which are not
jointly contained in any `E_theta`.  A target-saturating marginal matching
`M` is a literal common-cap compiler if and
only if

\[
       \sum_{e\in F}1_{\{e\in M\}}\le |F|-1
                  \qquad(F\in {\cal F}_{cap}).                   \tag{3.6}
\]

The matching matrix is totally unimodular; the added conflict rows need not
be.  A declared co-selectable guarded bank certifies that every matching
inside the bank avoids this clutter.  On such a certified bank ordinary
Hall is sufficient and exact; merely checking individually guarded edges is
not.

## 4. Exact return theorem for an arbitrary packet circuit

Now let a safe serial packet walk end at `T_1`.  It may be a zero-action
twisted cube, a block-order breaker, a two-core transfer, or an arbitrary
safe walk.  Let `M_0` be any protected terminal target-cell matching which
must remain fixed during residual completion; it may contain exterior,
native packet, or boundary incidences.  Put

\[
 D=L\setminus V_L(M_0),\qquad C_0=C\setminus V_C(M_0).          \tag{4.1}
\]

Define

\[
 \Theta(T_1;M_0)=\{\theta\in\Theta(T_1):M_0\subseteq E_\theta\}.
                                                               \tag{4.2}
\]

### Theorem 4.1 (circuit return/common-cap Hall)

Conditional on retaining `M_0`, the minimum number of terminal lower
obligations left unmatched is exactly

\[
 \boxed{
 \delta(T_1;M_0)=|D|-
   \max_{\theta\in\Theta(T_1;M_0)}
       \nu\bigl(G_\theta(T_1)[D,C_0]\bigr).}                    \tag{4.3}
\]

Equivalently,

\[
 \delta(T_1;M_0)=\min_{\theta\in\Theta(T_1;M_0)}
   \max_{X\subseteq D}
      \bigl(|X|-|N_{G_\theta(T_1)[D,C_0]}(X)|\bigr)_+.         \tag{4.4}
\]

If no cap state retains `M_0`, the conditional problem is infeasible.

#### Proof

Every retained edge of `M_0` occupies one target and one cell.  Under a cap
state in (4.2), completing `M_0` is therefore exactly the problem of
matching the residual targets `D` into the residual cells `C_0`.  Apply
Hall's theorem for each fixed state and minimize over the compatible
states. \(\square\)

### Corollary 4.2 (address transport is sufficient, not necessary)

Suppose some compatible terminal cap state admits a permutation of residual
cells which carries one complete old residual matching to legal terminal
edges.  Then `delta(T_1;M_0)=0`.

Equality of unaddressed occurrence counters alone does not imply this cell
permutation and does not imply zero deficiency.

### Corollary 4.2a (zero-action macros have zero intrinsic native return cost)

For the prepared triangle, take `M_0` to include the native partial basis of
Theorem 2.1.  Then none of the `6(d-1)` changed-support obligations belongs
to the residual shore `D`.  Hence the triangle's intrinsic return
deficiency on its primary packet bank is zero.  Formula (4.3) tests only
extension to the exterior target bank (and any other nonnative compiler
tasks) under one common cap state.

This is the exact gain over three unrelated zero-sum columns: the triangle
supplies a literal address transport on the primary bank, not merely equal
unaddressed counters.

For the strict-rainbow twisted cube, use instead the `8(d-1)`-cell basis of
Theorem 2.2.  The same conclusion holds and all global q1 palette rows are
preserved.  This is the physically relevant version for a lower-rainbow
carrier.

### Corollary 4.3 (the one-packet U5 formula)

For one canonical packet, freeze the phase-invariant exterior matching and
the closed `q=1` hinge.  The residual obligations are the
`m=2(d-1)` old deep targets, and the freed exterior cells define the
trace-guarded return graph `R`.  With one fixed co-selectable cap state,
(4.3) becomes

\[
                         \delta=m-\nu(R).                         \tag{4.5}
\]

The local maximal-erosion audit proves `E(R_loc)=emptyset`; hence

\[
                   \delta_{loc}=2(d-1).                           \tag{4.6}
\]

This is a physical trace obstruction, not an algebraic one.  Every tempting
local return cap deletes a complete maximal-erosion occurrence of a filler
coordinate, and further caps cannot restore it.

### Theorem 4.4 (fixed-state augmenting-linkage drift)

There is a complementary dynamic form of the same gate.  A **carryable
guard schema** `rho` is an endpoint-relative boundary/pin/trace policy which,
for every carrier `U` in the route, instantiates a co-selectable incidence
graph `H_rho(U)` on the same target and cell shores.  Unlike a terminal
complete state `theta`, it does not assert that one literal antecedent has
two different derivatives.

Fix such a schema across `T -> T'`, and let `M` be a maximum matching of
`H_rho(T)`.  Delete from `M` the `ell` edges absent from `H_rho(T')`,
obtaining `M^-`.  Let `alpha` be the maximum number of pairwise
vertex-disjoint `M^-`-augmenting paths in `H_rho(T')`.  Then

\[
 \boxed{
 \delta_\rho(T')-\delta_\rho(T)=\ell-\alpha,}
 \qquad
 \delta_\rho(U)=|L|-\nu(H_\rho(U)).                             \tag{4.7}
\]

For a serial route on common shores carrying the same schema `rho`, choose a
terminal maximum matching after every augmentation.  The identity telescopes:

\[
 \delta_\rho(T_s)-\delta_\rho(T_0)
          =\sum_{i=0}^{s-1}(\ell_i-\alpha_i).                    \tag{4.8}
\]

#### Proof

The matching `M^-` has size `nu(H_rho(T))-ell`.  Its symmetric difference
with a maximum matching of `H_rho(T')` decomposes into alternating cycles,
balanced paths, and exactly

\[
             \nu(H_\rho(T'))-|M^-|
\]

pairwise vertex-disjoint augmenting paths.  This number is `alpha` by
maximality, which gives (4.7).  Summing consecutive fixed-state identities
gives (4.8). \(\square\)

This is a strong sufficient tracking interface, not a necessity for the
terminal-only route.  If the carryable schema changes, the terms do not
automatically telescope; one must use the global minimum in (4.3) at the
terminal carrier or export an explicit schema-regeneration rule.  More
precisely, suppose transition `T_(i-1)->T_i` is evaluated in `rho_(i-1)` and
the schema is then changed at `T_i` to `rho_i`.  Put

\[
 \kappa_i=\delta_{\rho_i}(T_i)
             -\delta_{\rho_{i-1}}(T_i).                         \tag{4.9}
\]

Provided every displayed state is legal on the carriers where it is used
and the shores are identified, the exact regenerated identity is

\[
 \delta_{\rho_s}(T_s)-\delta_{\rho_0}(T_0)
       =\sum_{i=1}^{s}(\ell_i-\alpha_i+\kappa_i).                \tag{4.10}
\]

Thus a changing-state proof must bound the regeneration charges `kappa_i`;
they are not supplied by Pluecker cancellation.

### Corollary 4.5 (exact breaker/compiler linkage score)

Let `T->T'` be one physically planted single-block-order breaker and fix a
carryable guard schema on both endpoint carriers.  With `ell_B` the old
matched incidences destroyed by the breaker and `alpha_B` the maximum
disjoint augmenting linkage in the new incidence graph,

\[
             \delta_\rho(T')-\delta_\rho(T)
                         =\ell_B-\alpha_B.                       \tag{4.11}
\]

Hence a breaker is `rho`-deficiency-improving exactly when
`alpha_B>ell_B`.  This need not improve global terminal deletion number,
which may optimize over a different complete cap state.  Theorem 2.5 proves
only that the extreme common-order
reflected-pair current ceases to be an invariant of the relabelled breaker
catalogue; it gives no sign or magnitude control on `alpha_B-ell_B`.
A positive-surplus breaker in a given carrier remains an occurrence-labelled
linkage problem.

## 5. Terminal-only serial theorem

No compiler is required at an intermediate carrier.  Let

\[
                         T_0\to T_1\to\cdots\to T_s             \tag{5.1}
\]

be a safe walk.  Each step preserves the owner deck, interval-OR support,
simple topology, and residence.  Assume `T_0` is upper-complete, and suppose
the terminal word admits a protected terminal matching `M_0` with

\[
                         \delta(T_s;M_0)\le C.                   \tag{5.2}
\]

### Theorem 5.1 (physical walk plus terminal return)

Under these hypotheses the terminal carrier has compiler deletion number at
most `C`.  In the exact compiler transfer theorem this yields

\[
                              \nu(k)\le B(k)+C.                  \tag{5.3}
\]

No matching or cap state is required for `T_1,...,T_(s-1)`.

#### Proof

Safe serial replacement preserves all noncompiler hypotheses and upper
coverage at every step.  The matching counted in (4.3), together with
`M_0`, is one legal terminal compiler under a single complete cap state and
misses at most `C` lower obligations.  Apply the terminal compiler transfer
bound. \(\square\)

The useful quantifier order is therefore

```text
choose a physically available safe packet;
recompute the next physical packet;
...
choose one terminal cap state and one terminal matching.
```

It is not necessary to preserve an intermediate matching.  It is necessary
to preserve physical carrier legality and to solve the final disjunctive
return problem.

## 6. The smallest live uniform lemma

After flag-lattice saturation, a sufficient regenerative export is the
following physical statement.

> There is an absolute `C` such that every recursive child contains a safe
> serial packet walk, starting from its exported resident upper-complete
> carrier, whose terminal word admits a protected terminal matching `M_0`
> and a complete common-cap state with residual Hall deficiency at most
> `C`.  A common-order subwalk remains in its reflected pair-degree fibre,
> but planted block-order breakers may change that current.  The full
> breaker/common-order action must satisfy the chosen terminal occurrence
> ledger, or one may use the strict-rainbow zero-action twisted cube.

This lemma has three genuinely independent parts.

1. **Packet availability/orderability:** a walk in the safe-carrier graph,
   not a formal sum in `U_d`.
2. **Address regeneration:** enough exterior trace-guarded cells to make the
   return deficiency bounded.
3. **Common-cap compatibility:** all chosen return edges occur under one
   complete cap state.

The current catalogue proves none of these uniformly.  It does prove that
there is no fourth, hidden fixed-flag lattice-index gate.  Theorem 2.5
removes the extreme reflected-pair obstruction, and (2.20) closes the entire
formal coupled-depth span once all internal twists are admitted.

## 7. Exact scope

Proved here or imported from named exact dependencies:

* the enlarged safe-walk action telescopes in the full catalogue module,
  while only the common-order subwalk lies in the reflected flag module;
* circuit-completeness, rather than lattice span, is the exact
  occurrence-labelled nonnegative reachability condition;
* the two-core commutator cancels the reflected companion algebraically;
* the frozen one-block breaker defects span the complete fixed-degree
  extreme pair-current kernel integrally, and all internal twists span the
  full product of the depthwise fixed-degree occurrence lattices;
* the four-packet twisted cube is a strict-rainbow all-depth zero-action
  macro with a zero-defect native partial compiler basis;
* the complete common-cap compiler is a disjunction of matching problems;
* (4.3)--(4.4) are necessary and sufficient after a protected terminal
  matching is fixed; and
* the canonical packet has local return deficiency `2(d-1)`.

Not proved:

* that an arbitrary recursive carrier contains the required twisted cube,
  breaker sequence, or four-slot cross-core macro;
* that every abstract Johnson square has a safe occurrence-labelled lift in
  one carrier;
* that the formal pure-depth differences from (2.20) have an owner-disjoint
  or regenerative physical lift in an arbitrary carrier;
* that a terminal cap state with bounded return deficiency exists uniformly;
* that address transport follows from occurrence-counter cancellation; or
* any all-`k` additive-constant or exact theorem.

Dependencies:

* `MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`;
* `MATH_THEOREM_COATOM_SINGLE_BLOCK_ORDER_REFLECTION_BREAKER_20260801.md`;
* `MATH_THEOREM_THREAD_D_COATOM_INTERNAL_BLOCK_TWIST_FULL_PRODUCT_SPAN_20260801.md`;
* `MATH_THEOREM_K_COATOM_OCCURRENCE_PLUCKER_REACHABILITY_AND_COMPANION_CANCELLATION_20260801.md`;
* `MATH_THEOREM_AD_COATOM_TRIANGLE_PHYSICAL_FLAG_CANCELLATION_20260801.md`;
* `MATH_THEOREM_AD_COATOM_TWISTED_CUBE_RAINBOW_FLAG_ABSORBER_20260801.md`;
* `MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md`;
* `MATH_THEOREM_SERIAL_COATOM_SAFE_SEARCH_AND_FINAL_COMPILER_REDUCTION_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md`; and
* `MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md`.

## 8. Lightweight audit

The lightweight wrapper replay

```text
scratch/audit_threadD_coatom_physical_lift_common_cap_20260801.py
scratch/threadD_coatom_physical_lift_common_cap_20260801.audit.json
```

checks for `2<=d<=10` the common-order triangle and native-basis identities,
verifies both the abstract disjunctive-union and literal two-position
common-cap counterexamples, and exhaustively checks the fixed-state residual
matching identity underlying Theorem 4.1 on all bipartite terminal graphs
with at most three residual targets and three cells.  It also hash-pins and
validates the PASS statuses of the independent breaker, all-internal-twist,
and twisted-cube replays; those three source audits, rather than this wrapper,
perform the literal packet/span checks.
