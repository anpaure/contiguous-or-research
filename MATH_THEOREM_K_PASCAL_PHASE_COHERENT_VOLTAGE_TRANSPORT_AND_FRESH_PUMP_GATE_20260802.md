# Phase-coherent Pascal voltage transport and the fresh-pump gate

**Date:** 2026-08-02
**Status:** unconditional fixed-cover fragment/phase calculus, exact
phase-coherent Pascal recurrence, and exact obstruction to functorially
transporting the natural cyclic voltage from dimension `k` to dimension
`k+2`.  The final induction statement is conditional on one child-native
unit-voltage seed and on complete zero-holonomy repair tickets.  No host,
upper-shadow, source, residence, or compiler existence is claimed.

## 0. Outcome

There are two distinct questions which must not be conflated.

1. **Fixed-cover transport.**  Once two Pascal child fragments are already
   expressed in one cyclic child cover, a literal phase-coherent closing-port
   rectangle has zero seam displacement.  If the two opened child cycles have
   voltages `v_0,v_1`, the crossed parent cycle has voltage

   \[
                              v'=v_0+v_1.               \tag{0.1}
   \]

   One crossed quotient port role (and its developed orbit) may remain as
   the unique protected aperture port.  Thus a
   live unit-voltage child plus a zero-voltage companion transports the unit
   exactly.  Two identical unit-voltage children transport `2v`, which is a
   unit for every odd, including composite, modulus.

2. **Dimension-changing phase lift.**  The natural cyclic deck groups in a
   same-parity step are `C_k` and `C_(k+2)`.  No homomorphism between them
   carries a generator to a generator for `k>=3`.  Therefore an old unit
   voltage is not automatically a child unit voltage.  The child must expose
   one child-native phase lift (equivalently one fresh voltage pump), unless
   the recursion has deliberately retained one common deck action across the
   two dimensions.

After the one child-native seed is present, every later repair may use a
fixed-`z` ticket, provided **the whole completed ticket**, including cap
backups, history collars, aperture discharge, and topology seams, has zero
holonomy.  The number `O(d)` of such tickets introduces no further voltage
condition.  Their cap and history coordinates remain governed by the
cap/history product monoid.

The persistent rank-`(r-2)` aperture is compatible with this recurrence, but
its debt count does not certify its holonomy.  Its closing edge can be carried
as the unique Pascal port; any exterior discharge/opening sidecar must either
have zero total seam displacement or be included in the one child-native
pump.

## 1. Open-cycle voltage potential

Fix a regular cyclic cover with additive deck group

\[
                              G=\mathbb Z_n.             \tag{1.1}
\]

Choose one representative of every quotient vertex.  An oriented quotient
edge `e:u->v` has gain `delta(e) in G`, meaning that its lift starting at
phase `g` ends at phase `g+delta(e)`.  For an oriented path `P`, let

\[
                         \lambda(P)=\sum_{e\in P}\delta(e). \tag{1.2}
\]

Let `P:s leadsto t` be an oriented path and let `e:t->s` be a distinguished
closing edge.  Define its **ported voltage potential** by

\[
                         \omega(P,e)=\lambda(P)+\delta(e). \tag{1.3}
\]

This is exactly the voltage of the quotient cycle `Pe`.  Its development has

\[
                         \gcd(n,\omega(P,e))             \tag{1.4}
\]

physical components.  In particular the developed cycle is connected iff

\[
                         \omega(P,e)\in(\mathbb Z_n)^\times. \tag{1.5}
\]

Changing the quotient section adds a coboundary to `lambda(P)` and the
opposite coboundary to `delta(e)`, so (1.3) is gauge invariant.

The distinguished edge is the correct place to store the persistent Pascal
aperture.  Opening the cycle deletes `e` but retains the potential (1.3) as
part of the boundary state.

## 2. The exact phase-coherent rectangle law

For `i=0,1`, let

\[
              P_i:s_i\leadsto t_i,\qquad e_i:t_i\to s_i \tag{2.1}
\]

be two disjoint ported child cycles.  Put

\[
 p_i=\lambda(P_i),\qquad a_i=\delta(e_i),\qquad
 v_i=p_i+a_i.                                           \tag{2.2}
\]

Suppose the ordinary Boolean closing-port square supplies crossed edges

\[
       f_{01}:t_0\to s_1,\qquad f_{10}:t_1\to s_0,      \tag{2.3}
\]

with gains `b_01,b_10`.  The crossed output cycle is

\[
                         C'=P_0f_{01}P_1f_{10}.          \tag{2.4}
\]

### Theorem 2.1 (ported fragment recurrence)

The exact output voltage is

\[
 V(C')=v_0+v_1+\sigma_\square,\qquad
 \sigma_\square=b_{01}+b_{10}-a_0-a_1.                 \tag{2.5}
\]

If `f_10` is retained as the parent closing port, then the parent open path

\[
                         P'=P_0f_{01}P_1                \tag{2.6}
\]

exports the same potential:

\[
                         \omega(P',f_{10})=V(C').       \tag{2.7}
\]

#### Proof

Summing the gains in (2.4) gives

\[
 p_0+b_{01}+p_1+b_{10}
 =(p_0+a_0)+(p_1+a_1)
   +(b_{01}+b_{10}-a_0-a_1),
\]

which is (2.5).  Equation (2.7) is the same sum with the last edge declared
to be the closing port.  \(\square\)

### Lemma 2.2 (literal four-endpoint coherence)

Assume the four quotient edges in (2.1)--(2.3) are Boolean-legal.  They can
be realized using one common choice of physical lifts of the four endpoint
vertices

\[
                         t_0,s_0,t_1,s_1                \tag{2.8}
\]

if and only if

\[
                         b_{01}+b_{10}=a_0+a_1.          \tag{2.9}
\]

Consequently every literal phase-coherent `K_(2,2)` port square has
`sigma_square=0`.

#### Proof

If the four endpoint phases are `q(t_i),q(s_i)`, then

\[
\begin{aligned}
 a_i&=q(s_i)-q(t_i),\\
 b_{01}&=q(s_1)-q(t_0),\\
 b_{10}&=q(s_0)-q(t_1).
\end{aligned}                                           \tag{2.10}
\]

Adding the last two identities and the first two identities proves (2.9).

Conversely set `q(t_0)=0`, `q(s_0)=a_0`, and

\[
 q(t_1)=a_0-b_{10},\qquad q(s_1)=q(t_1)+a_1.           \tag{2.11}
\]

Then the `f_10` and old-edge gains are correct, while (2.9) gives
`q(s_1)-q(t_0)=b_01`.  Thus all four edges use the same endpoint lifts.
\(\square\)

Boolean port compatibility alone is weaker than Lemma 2.2: four quotient
options may exist but use incompatible translates.  The phase equation
(2.9) is therefore a necessary additional row of a same-parity port
selector.

## 3. Coprimality under a Pascal splice

Under the phase-coherent hypothesis, Theorem 2.1 becomes

\[
                              v'=v_0+v_1.               \tag{3.1}
\]

### Corollary 3.1 (exact unit criterion)

The crossed parent develops to one physical cycle exactly when

\[
                              \gcd(n,v_0+v_1)=1.        \tag{3.2}
\]

In particular:

1. if `v_0` is a unit and `v_1=0`, then the parent transports `v_0`
   unchanged;
2. if `v_0=v_1=v` and `n` is odd, then `2v` is a unit, even when `n` is
   composite; and
3. if `n` is even and both children carry the same unit `v`, then `2v` is
   not a unit.

More generally, two unrelated unit voltages need not have unit sum: in
`Z_9`, `1+2=3` is not a unit.  Thus “both children connected” is not an
adequate voltage interface; the ordered port state must retain their actual
voltages or monodromies.

Item 1 is the clean asymmetric regenerative face.  The neutral companion
need not be connected before the splice; connectedness is asserted only for
the crossed parent cycle certified by (3.2).

### Corollary 3.2 (one persistent aperture)

Suppose the private Pascal splice freezes `f_01` into the parent path and
retains `f_10` as the distinguished aperture port.  If the two old aperture
port roles are consumed by the rectangle and the lower debt relay identifies
the new role with the single carried aperture token, then the quotient output
has:

* one, not two, live aperture ports;
* voltage potential `v_0+v_1`; and
* the occurrence-labelled phase record needed to test (2.9) at the next
  splice.

The next splice must still pass (2.9) against its new companion; this is not
automatic from the present splice.

This is a voltage/topology statement.  The rank-`(r-2)` support and exterior
`J`-discharge conditions are the separate hypotheses of the one-aperture
Pascal theorem.

## 4. Zero-holonomy completed tickets after the seed

Let a one-cycle host have voltage `v`.  A complete repair ticket `Q` cuts
old seams `e_j`, retains every intervening path in its declared orientation,
and inserts new seams `f_j`.  Put

\[
              \sigma(Q)=\sum_j\delta(f_j)-
                                  \sum_j\delta(e_j).    \tag{4.1}
\]

The fragment-localization theorem gives

\[
                              v_{\rm new}=v+\sigma(Q).  \tag{4.2}
\]

The fixed-`z` central `C14` has zero displacement.  A **completed** ticket is
zero-holonomy only when

\[
 \sigma_{C14}+\sigma_{\rm backup}+\sigma_{\rm history}
 +\sigma_{\rm aperture}+\sigma_{\rm join}=0.           \tag{4.3}
\]

Cap balance or history acceptance alone does not imply (4.3).

### Theorem 4.1 (one pump, arbitrarily many zero tickets)

Suppose a fixed child cover contains one protected one-cycle of unit voltage
`v`.  Apply any serial family of complete tickets such that every prefix

1. remains one quotient cycle;
2. preserves the protected aperture port or exports its declared successor;
   and
3. has zero total displacement in the sense of (4.3).

Then every prefix and the final carrier have voltage `v` and develop to one
physical cycle.  The number of tickets may be `O(d)` or larger.

#### Proof

Apply (4.2) at every prefix.  \(\square\)

The one-aperture debt count remaining equal to one does not prove item 3.
If its exterior discharge or opening contributes displacement `alpha`, the
true final voltage is `v+alpha`.  The aperture is harmless exactly when
`alpha=0`, or it acts as part of the one voltage pump exactly when
`v+alpha` is a unit.

## 5. Coupling to the cap/history product monoid

At a fixed modulus, a proof-safe protected state may be written

\[
 \Xi=(v;z,b;\mathcal R_d^+,\mathcal R_d^-;
             \mathfrak p_{\rm ap};\mathcal T),          \tag{5.1}
\]

where `v` is the ported voltage potential, `(z,b)` is the exact cap
current/prefix-debt state, the two relations are phase-correct positive and
negative history relations, `p_ap` is the occurrence-labelled aperture
port, and `T` is the opening/topology record.

For a serial complete ticket `Q`, the exact update is

\[
\begin{aligned}
 v'&=v+\sigma(Q),\\
 z'&=z+z_Q,\\
 b'&=\max\{b,b_Q-z\},\\
 \mathcal R'^{\pm}&=\mathcal R_Q^{\pm}
                         \circ\mathcal R^{\pm}.         \tag{5.2}
\end{aligned}
\]

For the binary Pascal operation, the voltage coordinate uses (2.5), the
history coordinate is the literal composition

\[
 \mathcal R(P_0f_{01}P_1f_{10}),                       \tag{5.3}

\]

and the cap coordinate uses the prefix ledger of that same chronological
word.  Thus phase coherence, cap backups, and boundary histories are not
three interchangeable checks: they are three coordinates of one selected
occurrence word.

A regenerative fixed-`z` ticket at a prepared joint history state
`H_*=(H_*^+,H_*^-)` has

\[
 \sigma(Q)=0,\qquad z_Q=0,qquad b_Q\le s,qquad
 (H_*^+,H_*^+)\in\mathcal R_Q^+,\qquad
 (H_*^-,H_*^-)\in\mathcal R_Q^-.                       \tag{5.4}
\]

Such a ticket acts trivially on the live voltage, cap load, and designated
history boundary, although it may use nonzero cap slack internally.

## 6. Composite moduli and stabilizers

The free-cover statements above are already valid for every composite
`n`; the relevant condition is being a unit, not merely being nonzero.

There is a useful extension when all vertices of the protected cycle have
one common stabilizer `H<=Z_n` and every selected edge is a functional
translation on the common phase fibre.  Replace `Z_n` by

\[
                             \overline G=Z_n/H.          \tag{6.1}
\]

All formulas in Sections 1--5 hold in `overline G`.  The development is one
cycle exactly when the reduced voltage generates `overline G`.

If stabilizers vary, a scalar voltage is not a proof-safe state.  For a
phase-functional open path `P:s->t`, retain its phase bijection

\[
                         \Phi_P:F_s\longrightarrow F_t. \tag{6.2}

\]

The closed monodromy is

\[
                         M(P,e)=\Phi_e\circ\Phi_P.      \tag{6.3}

\]

and the physical components are the cycles of `M`.  Under the crossed
splice the exact new monodromy is

\[
 M'=\Phi_{f_{10}}\circ\Phi_{P_1}\circ
       \Phi_{f_{01}}\circ\Phi_{P_0}.                   \tag{6.4}

\]

The scalar addition law is the regular-translation specialization of
(6.4).  A stabilizer-aware “zero-holonomy” ticket must leave `M` conjugate
to its old value, not merely have a formally zero sum of arbitrarily chosen
representative gains.  If some edges are not phase-functional, the complete
phase relation or a literal physical replay is required.

This is exactly the stabilizer-coset field already required by the directed
history state.  The same coset choice must be used in (6.4) and in the
history transition; choosing them independently is invalid.

## 7. The same-parity modulus obstruction

The preceding transport theorem is a fixed-cover theorem.  It does not map
the natural cyclic quotient in one dimension to the natural cyclic quotient
two dimensions later.

### Theorem 7.1 (no functorial generator transport)

For `k>=3`, no group homomorphism

\[
                         \phi:C_k\longrightarrow C_{k+2} \tag{7.1}

\]

sends a generator to a generator.

#### Proof

The image order divides both `k` and `k+2`, hence divides

\[
                         \gcd(k,k+2)=\gcd(k,2).         \tag{7.2}

\]

For odd `k` the image is trivial.  For even `k` it has order at most two,
which is smaller than `k+2`.  \(\square\)

Therefore the parent voltage `v_k` has no canonical child image.  Even
reusing the same integer can lose coprimality: `3` is a unit modulo `7` but
not modulo `9`.

### Corollary 7.2 (minimal fresh-pump obstruction)

A same-parity induction based on the natural full rotations must supply, at
each new modulus, one of the following.

1. A child-native protected seed with voltage

   \[
                         v_{k+2}\in(\mathbb Z_{k+2})^\times; \tag{7.3}
   \]

2. a child-native rephasing of the inherited protected fragment whose
   audited ported potential satisfies (7.3); or
3. a common cyclic deck action deliberately retained across the two
   dimensions, together with its stabilizer-aware monodromy certificate.

In alternatives 1--2 this is exactly one fresh voltage pump per dimension,
not one pump per later repair task.  Theorem 4.1 then localizes every later
topology requirement to zero-holonomy completed tickets.

The cleanest prospective phase interface is a child section in which the
seed potential is `+1` or `-1`; this is a unit for every modulus.  Neither
the Pascal port square, the stationary pull clock, nor the one-aperture debt
relay constructs such a section.

## 8. Exact conditional induction and remaining lemma

### Theorem 8.1 (protected Pascal seed plus fixed-`z` repairs)

Fix one same-parity child modulus `n`.  Assume:

1. two protected child fragments and their closing ports live in one free
   (or common-stabilizer) cyclic child cover;
2. their Boolean port square is literal and phase coherent in the sense of
   Lemma 2.2;
3. `v_0+v_1` generates the child phase fibre;
4. one crossed port is the unique persistent aperture, with its exterior
   `J` occurrence and opening included in the audited seam ledger;
5. the cap/history product word is prefix-cap-safe and has an accepting
   bidirectional boundary state; and
6. every later fixed-`z` repair is a complete, one-cycle, zero-holonomy
   ticket satisfying the regenerative product conditions (5.4), and
   preserves the declared protected port/resources.

Then the final child is one physical cycle, has the same generating
voltage as the crossed seed, carries exactly one aperture port, and retains
the accepted cap/history state throughout all later repairs.

#### Proof

Items 1--3 and Theorem 2.1 give one crossed quotient cycle with generating
voltage.  Corollary 3.2 exports one aperture.  Item 4 places every aperture
sidecar seam inside that same voltage calculation.  The cap/history claims
follow from (5.2).  Item 6 and Theorem 4.1 preserve the generating voltage
and return the protected cap/history boundary after every later ticket.
\(\square\)

This theorem closes the fragment/phase algebra.  Its smallest missing
existence row is now precise:

> **Child-native pump-and-port lemma.**  In each same-parity Pascal child,
> expose one phase-coherent protected port square whose summed child
> potential is a generator of the child phase fibre, whose surviving port is
> the persistent rank-`(r-2)` aperture, and whose same occurrence word admits
> the balanced cap backups and bidirectional history tickets.

If this lemma fails only in the voltage coordinate, one fresh twisted
heptagonal pump suffices; all `O(d)` subsequent repairs may stay on the
fixed-`z` zero-holonomy face.  If it fails in the common occurrence word,
raw central packet abundance does not repair it.

Upper shadows beyond the immediate cap row, source/envelope transport,
one-star word-length consolidation, the terminal common-cap compiler, and
existence of the global Pascal host remain separate gates.  No `B+1`,
`B+O(1)`, or exact formula follows from this note alone.
