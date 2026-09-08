# Minimal K2,2 voltage arithmetic: dyadic amplifier and fresh-pump no-go

**Date:** 2026-08-02  
**Status:** exact fixed-cover arithmetic and a sharp obstruction for the
minimal coherent one-aperture face.  This note does not construct the
Boolean Pascal ports, an upper-complete host, residence, or a compiler.

## 0. Verdict

A phase-coherent Pascal `K_(2,2)` is a voltage **adder**, not a voltage
pump.  If its two ported child fragments have parent-native potentials
`v_0,v_1`, its retained aperture closes with potential

\[
                         v_{\rm out}=v_0+v_1.             \tag{0.1}
\]

Consequently two equal, co-oriented child potentials `w` give `2w`.
Starting from a parent-native potential `+1` or `-1`, a balanced binary
recursion gives `+2^a` or `-2^a`; this is a unit modulo every odd modulus,
including every odd composite modulus.

The same square cannot create that seed.  Its only voltage-changing
coordinate is the holonomy around the old-versus-crossed square, and a
common simultaneous lift of its four endpoints forces that holonomy to
zero.  Thus the minimal coherent face discharges the fresh-pump row if and
only if the two child potentials already have the desired sum.  A genuine
fresh pump requires a nonzero-holonomy square, a larger phase actuator, or
a separately constructed parent-native child potential.

The accepted closure must be exported as one correlated tuple containing
the cap/bi-history state, the closed potential, and the literal private
edge.  The three marginals are not interchangeable.

## 1. Complete arithmetic of the port square

Work in a regular cyclic cover with deck group `G=Z_N`.  For `i=0,1`, let

\[
 P_i:s_i\longrightarrow t_i,\qquad e_i:t_i\longrightarrow s_i
                                                               \tag{1.1}
\]

be a ported child path and its old closing edge.  Write

\[
 p_i=\delta(P_i),\qquad a_i=\delta(e_i),\qquad v_i=p_i+a_i.    \tag{1.2}
\]

Let the two crossed edges be

\[
 f_{01}:t_0\longrightarrow s_1,qquad
 f_{10}:t_1\longrightarrow s_0                                  \tag{1.3}
\]

with gains `b_(01),b_(10)`.  Retain `f_(10)` as the private closing edge.
The new open path is `P_0 f_(01) P_1`, and its closed potential is

\[
 \begin{aligned}
 \kappa
   &=p_0+b_{01}+p_1+b_{10}\\
   &=v_0+v_1+h_\square,\\
 h_\square
   &:=b_{01}+b_{10}-a_0-a_1.
 \end{aligned}                                                   \tag{1.4}
\]

All four quantities `v_0,v_1,h_square,kappa` are invariant under a change
of quotient section.  In particular, translating any endpoint lift cannot
change the pump coordinate `h_square`.

### Lemma 1.1 (the sole square constraint)

The old and crossed edges in (1.1)--(1.3) use one simultaneous choice of
the four physical endpoint lifts if and only if

\[
                              h_\square=0\quad\text{in }Z_N.     \tag{1.5}
\]

There is no further phase equation on the minimal square.

#### Proof

If the four endpoint phases are `q(t_i),q(s_i)`, then

\[
\begin{array}{ll}
a_0=q(s_0)-q(t_0),&a_1=q(s_1)-q(t_1),\\
b_{01}=q(s_1)-q(t_0),&b_{10}=q(s_0)-q(t_1).
\end{array}                                                     \tag{1.6}
\]

Their alternating sum is zero.  Conversely choose `q(t_0)` arbitrarily,
propagate through three edges of the square, and use (1.5) to verify the
fourth.  A connected four-cycle has cycle rank one, so this is its only
constraint.  \(\square\)

For prescribed **integer** edge lifts, the identical proof over `Z` says
that a simultaneous integer endpoint potential exists exactly when the
integer alternating sum is zero, not merely a multiple of `N`.  Modular
condition (1.5) permits one to alter an edge representative by a multiple
of `N` and obtain a locally exact lift.  Such an alteration is not a
cross-dimension certificate unless the chosen representative is also the
one exported by the global lift convention.

### Corollary 1.2 (coherent square is neutral)

On the common-endpoint face, (1.4) reduces to (0.1).  Therefore the square
contains no phase variable capable of changing `v_0+v_1`.

This is sharp.  If common-endpoint coherence is relaxed, the same algebra
allows arbitrary `h_square` at the voltage-graph level.  To force a target
unit `u`, the required square holonomy is exactly

\[
                             h_\square=u-v_0-v_1.       \tag{1.7}
\]

A Boolean realization of (1.7) is precisely a fresh phase pump; it is not a
consequence of the ordinary port comparator.

## 2. Exact dyadic amplifier

### Theorem 2.1 (equal-sibling recurrence)

Suppose a balanced binary Pascal hierarchy is built in the final cover so
that:

1. every pair of siblings has the same parent-native lifted potential `w`;
2. both sibling paths are used in the same orientation;
3. every splice square satisfies (1.5); and
4. every completed later repair ticket has zero total holonomy.

If a leaf potential is `epsilon`, then a node `a` levels above its leaves
has potential

\[
                            2^a\epsilon.                \tag{2.1}
\]

For `epsilon=+1` or `-1`, every such node develops to one cycle over every
odd modulus.

#### Proof

Corollary 1.2 doubles the potential at each binary node.  Zero-holonomy
tickets preserve it.  Finally `gcd(N,2^a)=1` for odd `N`.  \(\square\)

The hypothesis is parent-native.  It is not inherited functorially from a
cycle in `Z_(N-2)`, because every homomorphism
`Z_(N-2) -> Z_N` is trivial when `N` is odd.  Thus Theorem 2.1 is an exact
amplifier theorem, not a construction of its first seed or of equal sibling
phase charts.

### Proposition 2.2 (normalization and state size)

After a successful splice over odd `N`, multiplication of all phase labels
by the inverse of `2` is a deck-generator relabelling and normalizes
voltage `2w` back to `w`.  It must be applied simultaneously to every
phase-labelled cap/history transition and to the private closing-edge
orbit.

Hence the dyadic exponent need not be an independent finite-state control
coordinate: one may store one normalized group element and the same
correlated product relation.  This normalization does not construct equal
sibling charts at the next Pascal node.

An assertion about the **integer** value `2^a`, rather than its residue,
also needs a fixed infinite-cover or canonical signed-lift convention.
Arbitrary integer representatives of a `Z_N` edge gain may be changed by
multiples of `N`.  Without a cross-node lift convention, only the modular
unit statement is intrinsic.

## 3. Composite-modulus obstruction is genuine

Connected children do not suffice.  In `Z_9`, the unit child potentials
`1` and `2` yield `3` on a coherent square, so the output has three physical
components.

Even allowing either child orientation does not always repair the sum.  In
`Z_15`, take

\[
                               v_0=1,\qquad v_1=4.       \tag{3.1}
\]

The four oriented sums are

\[
                              \pm1\pm4\in\{5,-3,3,-5\}, \tag{3.2}
\]

each divisible by `3` or `5`.  Thus no co-orientation or reversal of this
minimal coherent face develops to one cycle.

A global change of deck generator multiplies both child potentials and
their sum by one unit.  It preserves the gcd obstruction and the ratio
`v_1/v_0`; it cannot turn (3.2) into a unit.  Endpoint gauge changes preserve
each closed potential and `h_square`.  These are exact, not coordinate,
obstructions.

The weakest arithmetic sibling hypothesis is therefore

\[
                            v_0+v_1\in Z_N^\times.       \tag{3.3}
\]

Equality `v_0=v_1 in Z_N^times` is a simple dimension-uniform sufficient
form because `N` is odd.

## 4. Correlated aperture state

Let `S` be the joint cap/positive-history/negative-history state space.
For one selected literal chronological word, let `s_out` be its terminal
state and retain `f_(10)` as its private closure.  The proof-safe exported
record is the single tuple

\[
                         (s_{\rm out},\kappa,f_{10}),    \tag{4.1}
\]

or, before all local choices have been fixed, a relation

\[
             \mathcal A\subseteq S\times Z_N\times E_{\rm priv}. \tag{4.2}
\]

The accepting closure set is

\[
 \mathcal A_{\rm acc}
   =\{(s,\kappa,e)\in\mathcal A:s\text{ is jointly accepting and }
                                  \gcd(N,\kappa)=1\}.    \tag{4.3}
\]

The aperture closes without a fresh pump exactly when
`A_acc` is nonempty.  Projection to three separate nonempty marginals is
not sufficient: the unit total, accepting history, and private edge must
belong to the same tuple.

On an equal-sibling coherent splice, selecting the literal crossed edge
`f_(10)` automatically pins the voltage entry of that same word to `2w`.
Serial fixed-`z` tickets preserve (4.1) only if their **completed** seam
ledger is zero and they preserve `f_(10)` or export a declared successor in
the same relation.

This uses a constant number of state fields.  It does not imply that the
relation has bounded cardinality, nor that the required tuple exists in a
Boolean host.

## 5. Sharp remaining interface

For the minimal coherent one-aperture face, the child-native voltage row is
exactly the following.

> Choose two literal, cap/history-compatible child tuples in one parent
> phase chart whose potentials have unit sum; equivalently, choose equal
> co-oriented unit potentials.  Cross them through a common-endpoint
> `K_(2,2)` and retain one literal crossed edge as the private closure.

If this row holds, the square amplifies the seed dyadically and the
cap/history/private-edge correlation is (4.1).  If it fails, no gauge,
endpoint translation, reversal in the `Z_15` example, or zero-holonomy
later ticket can repair it.  The smallest escape is a Boolean-legal square
with the nonzero holonomy (1.7), which is exactly a fresh voltage pump, or a
larger gadget that changes one child potential before the coherent splice.

Thus the minimal common-endpoint `K_(2,2)` does not discharge the fresh-pump
existence lemma unconditionally.  It gives the exact O(1)-field dyadic
amplifier once a parent-native equal-sibling seed has been constructed.
