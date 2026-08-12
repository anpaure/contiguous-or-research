# Cyclic packet orbits telescope whenever rotation carries each output state to the next input state

**Date:** 2026-08-05  
**Method:** equivariant occurrence-deck coboundary calculus; no computation
or search  
**Status:** unconditional serial theorem and exact orbit-length arithmetic.
It turns coordinate rotation into a possible global fan-current canceller,
but does not prove that the PBBS packet outputs satisfy the required
rotated handoff or that the resulting serial rethread fuses components.

## 1. Physical rotation and fan state are different actions

Let `rho` be cyclic rotation of the `n` ground-set coordinates.  It acts on
literal owners, source letters, histories, and target occurrences.  Let a
packet `P` have complete occurrence-labelled input and output fan states

\[
                         D^-(P),\qquad D^+(P),                 \tag{1.1}
\]

so its signed target current is

\[
                         \partial P=D^+(P)-D^-(P).             \tag{1.2}
\]

The coordinate action `rho` must not be confused with the physical
three-strand permutation `tau`, nor with the internal relative fan voltage
which shifts one history against another.  The theorem below uses only the
literal coordinate action on the complete states (1.1).

## 2. Exact orbit telescoping

Fix an integer step `s` and put

\[
                         L={n\over\gcd(n,s)}.                   \tag{2.1}
\]

Let

\[
                         P_t=\rho^{ts}P_0,qquad 0\leq t<L.    \tag{2.2}
\]

These are occurrence-labelled rotated copies; equality below includes all
left/right histories, target labels after rotation, source occurrences,
and required halo state.

### Theorem 2.1 (cyclic orbit coboundary)

Assume the one-step handoff identity

\[
                         D^+(P_0)=\rho^sD^-(P_0).              \tag{2.3}
\]

Then the full rotation orbit has zero signed current:

\[
                         \boxed{\sum_{t=0}^{L-1}\partial P_t=0.} \tag{2.4}
\]

The equality holds occurrence by occurrence after the cyclic handoff
bijection, at every depth and simultaneously for complementary upper
targets.

#### Proof

Apply `rho^{ts}` to (2.3):

\[
 D^+(P_t)=\rho^{(t+1)s}D^-(P_0)=D^-(P_{t+1}),                 \tag{2.5}
\]

with `t` taken modulo `L`.  Substituting (1.2) into the left side of
(2.4), every output cancels the next input.  Since `rho^{Ls}=1`, the final
output cancels the initial input.  Complementation commutes with coordinate
rotation, proving the upper statement. `square`

### Corollary 2.2 (rotated conjugacy form)

More generally, it is enough that a literal intersite transport `J`
satisfy

\[
                         J D^+(P_0)=\rho^sD^-(P_0),             \tag{2.6}
\]

and that its rotated copies compose around the orbit with trivial terminal
holonomy.  Thus exact set equality at adjacent physical sites can be
replaced by a certified occurrence transport, but equality merely of rank
histograms cannot.

## 3. Serial overlap is allowed

Theorem 2.1 is a theorem about a serial reconfiguration, not necessarily a
simultaneous packing of disjoint local switches.  Suppose the output factor
after applying `P_t` literally exposes the input phase of `P_(t+1)` and no
already-consumed edge is required again.  Then the packets may share the
handoff owners or boundary states: those shared objects are the terminal
state of one move and the initial state of the next, not two simultaneously
claimed resources.

Therefore an equality such as

\[
                         Q_0(t)=P_0(t-1)                       \tag{3.1}
\]

is not by itself a collision obstruction.  It is potentially the exact
serial handoff needed by (2.3).  What must be checked is stronger and
literal:

1. the entire output edge/owner phase equals the next input phase;
2. both complete history sides and their occurrence tags match;
3. every intermediate factor remains degree two and owner-simple; and
4. the final factor closes after `L` steps.

This distinguishes a useful moving packet from an invalid simultaneous
overlap.

## 4. Rotation-length arithmetic

If the `L` sites can instead be interpreted as an aligned positive family
on the same three old components, their topological return action is
translation by `L` in `Z_3`.  Such an aligned orbit fuses the components
exactly when

\[
                              3\nmid L.                         \tag{4.1}
\]

For `n=3^a u` with `3` not dividing `u`, a rotation step with
`gcd(n,s)=3^a` has orbit length `u`, hence passes (4.1), provided `u>1` and
the literal handoff exists.  If `n` is a pure power of three, every
nontrivial cyclic-rotation orbit has length divisible by three.  Then a
rotation-only aligned construction needs either a fixed state, a second
actuator, or a non-aligned serial topology calculation.

The topology clause is deliberately conditional: overlapping serial moves
need not have the same endpoint permutation as a disjoint aligned family.
For a serial orbit, its exact endpoint permutation must be multiplied from
the intermediate factors.

## 5. Exact remaining orbit lemma

The cyclic-orbit route reduces to the following concrete statement.

> **Moving-soliton handoff lemma.**  In the PBBS factor, find a positive
> clean-`C6` packet `P` and a nonzero rotation step `s` such that its output
> factor and complete fan state are the rotated input factor and state of
> the next packet, as in (2.3), and such that one full serial orbit has a
> topology-changing endpoint permutation while every intermediate factor
> is simple.

The number `L` of reconfiguration moves may grow with the dimension without
affecting additive word length: the moves relabel and rethread a fixed
factor rather than append source positions.  Thus an orbit theorem could
prove an additive bound even when no bounded local phase breaker exists.

What remains unproved is precisely the literal handoff and the serial
topology.  Rotation equivariance alone only says that rotated copies of a
legal packet are legal; it does not say that one packet output equals the
next rotated input.

## 6. Scope

Proved:

1. exact all-depth cancellation under a rotated output-to-input handoff;
2. why serial boundary overlap may be useful rather than fatal;
3. the exact rotation-orbit length and the aligned mod-three topology gate;
4. why a growing number of zero-length-change moves is compatible with an
   additive-constant theorem.

Not proved:

1. the PBBS moving-soliton handoff;
2. the endpoint permutation of an overlapping serial orbit;
3. collision-free intermediate factors and compiler/common-cap transport;
4. `nu(k)<=B(k)+O(1)`.
