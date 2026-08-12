# A full rotation orbit of packet currents cancels exactly by necklace-class balance

**Date:** 2026-08-05  
**Method:** Reynolds averaging on literal target currents; no computation or
search  
**Status:** unconditional algebraic criterion.  It is weaker than
output-to-next-input telescoping and may therefore be easier to satisfy.
It does not prove that all rotated packets coexist in one simple factor.

## 1. Literal current module

Let a finite group `G` act on a finite literal target set `T`.  Work in the
free abelian group `Z[T]`.  For a signed packet current

\[
                         \Delta=\sum_{S\in{\cal T}}c_S[S],       \tag{1.1}
\]

define its full orbit current

\[
                         R_G\Delta=\sum_{g\in G}g\Delta.         \tag{1.2}
\]

### Theorem 1.1 (orbit-balance criterion)

The following are equivalent.

1. `R_G Delta=0` in `Z[T]`.
2. For every target orbit `O in T/G`,

   \[
                              \sum_{S\in O}c_S=0.                \tag{1.3}
   \]

#### Proof

Fix `U in T` with orbit `O`.  The coefficient of `[U]` in (1.2) is

\[
 \sum_{g\in G}c_{g^{-1}U}
   =|\operatorname{Stab}_G(U)|\sum_{S\in O}c_S.                 \tag{1.4}
\]

Thus every coefficient vanishes exactly when (1.3) holds on every orbit.
`square`

For cyclic coordinate rotation, the orbits `O` are ordinary binary
necklace classes.  A full rotation orbit of a packet therefore has zero
target current exactly when its old-only and new-only targets have the same
total multiplicity in every necklace class.

## 2. Typed and occurrence-refined versions

Let each current term also carry a finite physical type `t`—for example
depth, width, compiler-cell class, phase, or cap role—and suppose `G`
preserves types.  Apply Theorem 1.1 to the target set of pairs `(S,t)`.
Then the orbit family admits a type-preserving cancellation exactly when

\[
              \sum_{S\in O}c_{S,t}=0
              \quad\hbox{for every necklace orbit `O` and type `t`.} \tag{2.1}
\]

When (2.1) holds, equal positive and negative multiplicities give a
bijection between old and new occurrences inside every `(O,t)` class.
This is enough to transport an occurrence matching provided no additional
address-specific capacity is required.  If physical addresses themselves
are load-bearing, they must be included in the type and (2.1) becomes the
correspondingly stronger test.

Complementation commutes with coordinate rotation.  Hence orbit balance
for every lower target current implies orbit balance for the paired upper
complement current.

## 3. Relation to serial handoff

The one-step rotated handoff

\[
                         D^+=\rho^sD^-                           \tag{3.1}
\]

is sufficient for orbit cancellation, but it is not necessary.  Equation
(3.1) pairs the entire output deck of one packet with the entire input deck
of the next.  Theorem 1.1 only asks that, after all rotated copies are
summed, the signed multiplicity in each necklace class vanish.

Thus there are two increasingly weak rotation routes:

1. **serial telescoping:** literal output-to-next-input equality;
2. **orbit balance:** equality only after aggregating the whole packet
   orbit, refined by every load-bearing physical type.

The second route may survive even when adjacent rotated packets have no
literal state handoff.

## 4. Application to the q3 flag current

For one q2-neutral clean `C6`, the first genuine left-only current is

\[
 \Delta_3=
   \sum_{i\in\mathbb Z_3}
   \left([K-\{d,e_{i-1}\}+a_i]-[K-\{d,e_i\}+a_i]\right).       \tag{4.1}

A full cyclic-coordinate orbit of this packet has zero q3 current if and
only if, in every binary necklace class, the number of new members of
(4.1) equals the number of old members.  Equality of all three flags
`e_i` is the pointwise special case; necklace-class balance is strictly
weaker in principle.

The same test must be imposed on the complete triangular history current,
not only on (4.1), to obtain an all-depth theorem.

## 5. Exact remaining physical theorem

An orbit-balanced current is only a formal target statement.  To turn it
into a carrier rethread one still needs:

1. a simultaneous or serial realization of the selected rotated packet
   copies in which every intermediate/final owner has degree two;
2. the exact endpoint permutation and component reduction;
3. type-refined balance for compiler/common-cap occurrences;
4. residence and source compatibility; and
5. a protected linear opening.

Nevertheless Theorem 1.1 gives a finite, exact invariant for the proposed
rotation strategy: calculate the signed necklace-class vector of one
packet.  A nonzero entry is a rigorous no-go for the full orbit; a zero
vector closes the complete formal target-current row before physical
packing is considered.
