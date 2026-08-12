# Audit of the MNW second-relay one-context carry

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_SECOND_RELAY_ONE_CONTEXT_CARRY_20260807.md`  
**Verdict:** algebraic statement PASS; literal factor switch remains
conditional on the explicitly strengthened prepared-prism lemma.

## 1. Rotation is not an automorphism of the selected factor

Let `rho` rotate two terminal coordinates to the front.  Although

\[
 rho(B_8 10)=10B_8,
\]

`rho` does not preserve the canonical MSW incidence-path factor.

Indeed, its rank-`m` degree-one vertices are exactly

\[
                         D_m\cup\overline{D_m}.
\]

For `m>=3`, take `x=1^m0^m in D_m`.  Then

\[
 rho(x)=00\,1^m0^{m-2}
\]

is not Dyck, while its complement

\[
 11\,0^m1^{m-2}
\]

falls below height zero during the block of `m` zeros and is not Dyck.
Thus `rho(x)` is not an endpoint of the canonical factor.  Since an
automorphism of the selected path factor must preserve its degree-one
vertices, `rho` is not such an automorphism.

This agrees with the cut-rigidity theorem: a global coordinate rotation
produces a conjugate factor, not a local relay in the original one.

**Result:** direct cyclic-rotation shortcut FAILS.

## 2. Natural and desired contexts

For a root `10 X v`, MSW concatenation fully exchanges the prefix `10`
before entering the `X` block.  The fixed prefix state is therefore `01`,
while the suffix state is `U(v)`.  The canonical boundary is exactly

\[
                         (Z_B)_{01,U(v)}.
\]

The terminal target is `10 B8 v`, so its desired boundary is
`(Z_B)_(10,U(v))`.  The two rank-one prefix contexts differ by one Johnson
move.

**Result:** PASS.

## 3. Chain identity and the count 24

`Z_B` is the sum of four alternating incidence hexagons.  Before
cancellation this expression has `4*6=24` signed incidence occurrences.
Applying the context-transport identity to each occurrence across the one
move `01->10` gives at most 24 signed transport hexagons.  Repeated or
cancelled incidences can only lower that number.

The theorem uses the unsimplified expression, so it does not require every
coefficient of the simplified circulation to be `+-1`.

**Result:** PASS.

## 4. Suffix support-disjointness

Every owner and colour of the base packet and every auxiliary vertex of a
transport hexagon has the form

\[
                         R\cup U(v),
\]

where `R` uses only the fixed prefix and base coordinates.  No transport
face changes a suffix coordinate.  If `v != v'`, then `U(v) != U(v')`, so
restriction to the suffix coordinates separates every vertex, incidence,
and hexagon in the two prisms.

Thus the algebraic carries for all suffixes are pairwise support-disjoint
and commute.

**Result:** PASS.

## 5. Turn-faithful closure needed one explicit strengthening

The carried boundary current has the correct q2 values when the untouched
mate at every changed owner is the contextual copy of the base mate.
However, the two negative targets of the four-hex macro are safe because of
*other*, untouched provider occurrences.  Mate fidelity at changed owners
alone does not logically guarantee that those spare providers exist in the
current rethreaded factor.

The theorem has therefore been strengthened to require literal contextual
copies of the two spare-provider turns, untouched throughout the sweep.
Under this added row, base support closure transports exactly.

**Result:** PASS after stated correction.

## 6. Exact remaining physical premise

The incidence-lattice equality does not imply that its signed hexagons can
be toggled from the factor state left by the gamma-alpha relay.  A literal
proof must still plant, simultaneously in every suffix fibre,

1. the required source/destination boundary phases in the **current**
   rethreaded factor;
2. complementary transport-rail phases and an alternating sweep order;
3. the untouched turn mates and the two spare providers;
4. the required component interface; and
5. avoidance of the protected pivot/stem bank.

The theorem now names exactly this as the one-prefix prepared-prism lemma.
Nothing in the algebraic audit proves it automatically.

**Result:** literal realization OPEN, with a precise host condition.

**Overall verdict:** the terminal cylinder has an exact constant-size,
suffix-disjoint algebraic carry.  It is not yet an unconditional q2 factor
repair; the sole remaining row is the strengthened one-prefix prepared
prism.
