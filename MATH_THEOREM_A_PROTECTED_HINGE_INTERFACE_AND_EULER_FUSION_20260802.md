# Protected hinge interfaces: exact one-copy rounding and Euler fusion

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotors  
**Status:** exact conditional theorem and sharp minimal obstructions.  This
note does not construct the canonical all-`k` table.

## 0. Scope and corrected input

The only stationary pull-clock input allowed here is
`MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md`, whose valid
ratio directions are

\[
 A_\delta/A_{\delta+1}\geq\rho,\qquad
 \Delta_{j+1}/\Delta_j\leq\rho,\qquad \theta=1/\rho.
\]

That theorem proves rational clockability.  Nothing below rounds an average
over different owner/target tables.  Instead, the results identify exactly
when one fixed table remains integral after literal residence histories and
named upper witnesses have been compiled into its hinges.

## 1. Completed protected interfaces

Let `V` be a finite interface-state set.  An interface state may contain a
literal order-`d` de Bruijn state, clipped run ages, endpoint types, and any
other finite boundary datum.  Let `P` be a fixed protected physical packet
bank and put

\[
 \eta=\partial P,\qquad \eta(V)=0.                    \tag{1.1}
\]

Let `I` be the free occurrence roles.  Role `i` owns a fixed, disjoint
resource block: in particular its owner labels and named lower-target
payload do not depend on its endpoint choice.  It has nonempty tail and head
sets `A_i,H_i subset V`.

Call these data a **completed protected hinge table** when, for every

\[
                         (a,h)\in A_i\times H_i,      \tag{1.2}
\]

there is a connected physical packet `K_i(a,h)` satisfying all of the
following.

1. Its contracted boundary is `1_h-1_a`.
2. It uses exactly the fixed resource block of role `i`.
3. Its internal residence/history audit passes, and equality of consecutive
   interface states is sufficient for safe physical concatenation.
4. It contains the same declared named upper-witness tickets `U_i`, with
   their occurrence-level guards, for every pair in (1.2).
5. Its exterior replacement signature is one for which the frozen exterior
   bank is certified safe.  Thus crossing upper witnesses are either fixed
   in `P`, carried literally in a macro packet, or protected by an explicit
   boundary-signature theorem; no crossing witness is implicit.
6. Its internal physical occurrences are private to that role, except for
   the declared contracted interface states.  Thus contracted weak
   connectivity lifts to physical weak connectivity without an undeclared
   collision or identification.

Assume that the resource blocks of `P` and the free roles use every required
owner and named lower target exactly once, and that

\[
                  U(P)\cup\bigcup_{i\in I}U_i        \tag{1.3}
\]

contains the required protected upper bank.

The word *completed* is load-bearing.  A relation of legal endpoint pairs
whose tail and head projections are `A_i,H_i`, but which is not their full
Cartesian product, is not a completed hinge.

### Lemma 1.1 (literal finite residence interface)

Signed coordinate residence at least `d+1` has an exact finite interface on
the relevant physical binary membership trace.  For every coordinate retain
its current membership bit and its current run age clipped at `d+1`.
Repeating the bit increments the age, capped at `d+1`; changing the bit is
allowed exactly when the old clipped age is `d+1`, after which the new age is
one.  A cyclic state walk is accepted if and only if every nonconstant
positive and zero run has length at least `d+1`; a constant coordinate cycle
uses the fixed clipped-age state `d+1` and is accepted.  This state is not
inferred merely from endpoint owner masks: it must be carried by the literal
physical trace being concatenated.

#### Proof

At a change of bit the completed run ends.  The transition rule accepts it
exactly when its true length is at least `d+1`; clipping loses no information
relevant to that predicate.  Every finite cyclic run ends at such a change,
including the run crossing an arbitrary linear cut.  Constant coordinate
cycles never change and are accepted.  \(\square\)

Thus residence itself causes no failure of network integrality once the
literal packet menus contain a common Cartesian product in this expanded
state space.  The substantive question is whether such a product survives
the simultaneous owner, target, upper-witness and exterior guards.

## 2. Exact protected Hoffman theorem

For `X subset V`, define

\[
 \ell_A(X)=|\{i:A_i\subseteq X\}|,
 \qquad
 r_H(X)=|\{i:H_i\cap X\ne\varnothing\}|.             \tag{2.1}
\]

### Theorem 2.1 (protected one-copy hinge rounding)

A completed protected hinge table has a physical selection choosing one
packet `K_i(a_i,h_i)` from every role, balancing the fixed bank,

\[
                  \sum_i({\bf1}_{h_i}-{\bf1}_{a_i})=-\eta,    \tag{2.2}
\]

and retaining every declared owner, lower target, upper witness and
residence/history guard if and only if

\[
 \boxed{\ell_A(X)-r_H(X)\leq\eta(X)
        \quad\text{for every }X\subseteq V.}          \tag{2.3}
\]

In particular, a rational root-conditioned circulation supported on the
completed rectangles of one fixed exact table has an integral protected
one-copy rounding on that same table.

#### Proof

At the contracted interface level this is exactly the polymatroid
intersection/Hoffman theorem: possible aggregate tail counts and head counts
are the integral transversal-polymatroid bases generated by the lists
`A_i` and `H_i`; their required difference is `eta`.  Its closed-cut family
is (2.3), and an integral common base decomposes into one tail and one head
choice per role.

Cartesian completion (1.2) turns every independently chosen pair into a
literal physical packet.  Items 2 and 4 of Section 1 make all resource and
witness rows invariant rolewise.  Item 3 makes every state-matched
concatenation residence/history safe, and item 5 protects the frozen
exterior.  Hence the contracted integral circulation lifts physically with
all declared guards.  Necessity is the usual closed-cut count.  \(\square\)

The theorem does not say that arbitrary upper coverage can be checked only
at endpoints.  It says that a *chosen named witness bank* can be made part
of the packet payload.  A witness crossing independently selected packets
must first be made local by a macro, fixed in `P`, or justified by a proved
boundary signature.

## 3. Exact component and sidecar criteria

For a state set `V_*` containing the interface support of `P`, restrict each
menu to `A_i cap V_*` and `H_i cap V_*`.

### Theorem 3.1 (exact at-most-`c` component criterion)

For an integer `c>=1`, a completed physical selection whose **exact
non-isolated contracted state support** is `V_*` and which has at most `c`
weak components exists if and only if
there are packets `R`, chosen from pairwise distinct free roles, such that

1. every packet of `R` has both endpoints in `V_*`, and `P union R` spans
   `V_*` and has at most `c` weak components;
2. after deleting the roles of `R`, all restricted menus are nonempty; and
3. with

   \[
                       \eta_R=\eta+\partial R,        \tag{3.1}
   \]

   every residual Hoffman inequality (2.3) holds.

For `c=1` this is an exact protected connected-rounding criterion.  Its
physical support has a rooted Euler circuit, so its route sidecar is zero.

#### Proof

Theorem 2.1 rounds the residual roles with boundary `-eta_R`.  Adding `P`
and `R` balances the support, and residual packets cannot increase the
number of components of a spanning support.  Connected physical packets
lift contracted connectedness.

Conversely, in every component of a physical solution take a spanning tree
after contracting the already fixed components of `P`.  Let `R` be the
distinct free-role packets appearing in those forests.  The remaining
selected packets prove all residual Hoffman cuts.  \(\square\)

This theorem explains the exact role of a protected spanning skeleton.  A
connected *fractional support* is not enough; Section 5 gives the smallest
counterexample.

If `Q` ranges over an exact atlas of allowed guard-safe uncoloured sidecar
packets, Theorem 3.1 also gives the exact bounded-sidecar union of faces:
fix `Q`, replace `P` by `P union Q`, shift `eta` by `partial Q`, and apply
the connected criterion.  Thus the minimum allowed sidecar cost is the
minimum cost of a `Q` for which some reserved skeleton has feasible residual
cuts.  This statement is exact only relative to the declared sidecar atlas.

An `O(1)` component bound alone is weaker.  In the order-`d` de Bruijn
metric, the states `0^d` and `1^d` have overlap zero, so joining their two
loop components costs `d` reset letters.

## 4. Protected component fusion

Let `F` be an integral completed selection.  Choose one unprotected selected
packet

\[
                         K_{i_t}(a_t,h_t)              \tag{4.1}
\]

from each of `q` distinct components.  Let `pi` be a `q`-cycle.

### Theorem 4.1 (completed-hinge `q`-fusion)

If

\[
                         h_{\pi(t)}\in H_{i_t}         \tag{4.2}
\]

for every `t`, replacing (4.1) by

\[
                         K_{i_t}(a_t,h_{\pi(t)})       \tag{4.3}
\]

fuses the `q` components into one and preserves, literally, every owner,
named lower target, declared upper witness, residence/history interface and
protected packet.

#### Proof

The tails are fixed and the heads are cyclically permuted, so the complete
state boundary is unchanged.  Every replacement remains in the same
role's completed rectangle, so all rolewise resources and protected guards
are unchanged.  Removing one selected arc from an Euler component leaves
its underlying support connected.  The cyclic reconnection joins the `q`
retained component blocks into one.  \(\square\)

Consequently an adaptive supply of such fusions until one component remains
gives a protected zero-sidecar carrier.  A static sufficient certificate is
a component spanning tree of simultaneously admissible fusions whose
removed packets are distinct and whose simultaneous deletion leaves every
old component connected.

For literal order-`d` trace arcs, (4.2) includes equality of the internal
de Bruijn spine.  The completed-interface hypothesis additionally includes
all residence and upper-ticket guards; spine equality alone does not.

## 5. Sharp smallest obstructions

### Proposition 5.1 (smallest non-Cartesian protected guard)

Let `V={0,1}`.  Let the protected bank be the arc `1->0`, so

\[
                         \eta={\bf1}_0-{\bf1}_1.      \tag{5.1}
\]

There is one free role.  Before an upper-witness guard it has the full
rectangle `A=H=V`, and the unguarded protected balance is completed by
`0->1`.  Suppose its designated upper witness survives exactly on

\[
                         E=\{(0,0),(1,1)\}.           \tag{5.2}
\]

Both the tail and head projections of `E` are all of `V`, but no
witness-safe choice cancels (5.1).  Thus separate tail/head filtering gives
a false positive.  No example with one interface state can have a nonzero
boundary, so two states and one role are minimal.

This is the exact reason endpoint-correlated residence or upper guards must
be fixed into actual Cartesian completed hinges, not merely projected onto
tail and head menus.

### Proposition 5.2 (smallest connected fractional-support obstruction)

Let `V={0,1,2}` and `P` be empty.  Role `i` has fixed head `i` and tail lists

\[
                         A_0=\{0,1\},\quad
                         A_1=\{0,2\},\quad
                         A_2=\{1,2\}.                 \tag{5.3}
\]

There are exactly two balanced integral selectors, with tail assignments

\[
                         (1,0,2),\qquad (0,2,1).      \tag{5.4}
\]

Each is a directed two-cycle plus one loop, hence has two weak components.
Their half-sum is a rational balanced circulation whose positive support is
weakly connected.  Therefore connected fractional support does not imply a
connected integral selector, even for genuine completed rectangles.

The example is minimal in state-bank size.  Indeed, on a two-state completed
hinge circulation polytope maximize total mass on crossing arcs.  Connected
rational support has strictly positive crossing objective.  The protected
Hoffman polytope is integral, so an integral optimum also has positive
integer crossing mass.  Balance on two states forces equal crossing mass in
both directions; hence its underlying support is connected.  Thus no
two-state completed-rectangle system can exhibit connected rational support
but only disconnected integral selectors.

The missing condition in (5.3) is exactly Theorem 3.1: every attempted
distinct-role spanning skeleton leaves an infeasible residual Hoffman cut.

## 6. Consequence for the live rotor gate

The protected theorem reduces the desired one-copy Euler rounding to the
following concrete, nonfractional certificate.

1. Choose one exact triangular owner/target table.
2. Assign a literal named provider for every upper target that must survive,
   and compile residence histories and exterior signatures into completed
   hinge rectangles.
3. Prove the Hoffman cuts after reserving either a connected distinct-role
   skeleton or an `O(1)`-component skeleton with an `O(1)` exact overlap
   tour.

Alternatively, first obtain any integral completed selector and exhibit an
adaptive completed-hinge fusion sequence from Theorem 4.1.

`MATH_THEOREM_A_UNSATURATED_ONECOPY_HINGE_AND_PROTECTED_COMPLETION_GATE_20260802.md`
removes the forced-owner repeat for every strict lower chain at owner rank at
least three.  That construction is only a one-sided literal rectangle.  In
fact, a single order-`d` de Bruijn transition with fixed depth-one suffix
payload has a unique head for each literal tail, so no better one-edge
two-sided Cartesian completion exists.  The live positive object is
therefore a protected multi-edge hinge macro (or a correlated selector
proved integral without Cartesian completion).

The finite `k=17` descent passed through independently replayed three-hole
and one-hole factors and has since reached an independently replayed
connected factor with all `19,412/19,412` required ordinary q1 colours.
This is strong evidence for the circulation actuator, but it does not
establish any completed-hinge hypothesis above: its passive literal replay
has 5,584 cyclic short ordinary residence components, while the best
reported linear opening has 5,586 short positive runs and 1,848 upper holes.
The newer all-opening endpoint adapter is stricter still: it reports 22/22
opened q1 holes (21 cyclic), short-run counts 5,586/5,587, and therefore
emits no common-cap instance.  Residence, ranks above q1, source, and compiler must still be
assigned to literal packets whose full endpoint products are safe.  Fixing
`h=O(1)` exceptional provider packets into `P` costs only `O(1)` protected
roles, but the shifted Hoffman cuts and the protected spanning skeleton
remain the exact gates.

Accordingly this note proves a protected integral fusion theorem, not
`B(k)+O(1)`.  Its smallest exact failure modes show that neither marginal
endpoint lists nor connected fractional support can close that gap.
