# Pascal transport of one coprime-voltage seed and the aperture phase gate

**Date:** 2026-08-02  
**Status:** exact fixed-modulus theorem, exact obstruction to naive
same-parity transport, and a conditional all-odd induction interface.
No upper-deck, residence, source, or compiler existence claim is made.

## 0. Verdict

The voltage pump can be localized after a child has been built in its own
cyclic cover.  More precisely, one child-native unit-voltage quotient cycle
followed by any number of complete, same-orientation, one-cycle tickets of
zero total seam displacement stays physically connected.

That statement does **not** transport a pump from modulus \(n\) to modulus
\(n+2\).  For odd \(n\), every homomorphism
\(\mathbb Z_n\to\mathbb Z_{n+2}\) is trivial.  The same-parity Pascal splice
must therefore export either

1. a child-native unit-voltage certificate; or
2. a coherent integer phase lift whose total is a unit for every later odd
   modulus.

The clean dimension-uniform version of item 2 has lifted voltage
\(\pm 2^a\), in particular \(\pm1\), and every completed later ticket has
zero **integer** displacement.

The persistent rank-\((r-2)\) aperture carries one lower target debt, but it
does not carry a voltage certificate.  Its exact extra state is the
displacement of the open path together with the phase menu of legal closing
seams.  A fresh pump is necessary precisely when this menu has no
unit-producing closure.

## 1. Oriented fragment and open-path identities

Let a quotient graph have a free cyclic cover with deck group
\(G=\mathbb Z_n\).  Fix a section and orient every used edge.  Write
\(\delta(e)\in G\) for the edge voltage and

\[
                 \omega(P)=\sum_{e\in P}\delta(e)
\tag{1.1}
\]

for an oriented path.

### Lemma 1.1 (closed fragment localization)

Let a directed quotient cycle \(F\) be cut at oriented seams
\(e_1,\ldots,e_t\).  Retain every resulting path with its orientation and
reconnect the same paths by seams \(f_1,\ldots,f_t\) into one directed
quotient cycle \(F'\).  Then

\[
 V(F')-V(F)
   =\sum_{j=1}^t\delta(f_j)-\sum_{j=1}^t\delta(e_j)
   =:\sigma .
\tag{1.2}
\]

The identity is gauge invariant.

#### Proof

Every retained oriented path occurs once in both cycle sums, so those terms
cancel.  A section change adds a coboundary.  Its sum on either closed cycle
is zero. \(\square\)

The same-orientation and one-output-cycle assumptions are load-bearing.  A
reversed retained path contributes \(-2\omega(P)\) in addition to the seam
ledger.  A cycle cover has one voltage per component, not one global
voltage.

### Lemma 1.2 (framed open path)

Fix quotient endpoints \(u,v\).  If an internal rethread changes a directed
\(u\)-to-\(v\) path \(P\) into \(P'\), retaining the oriented fragments,
then

\[
                       \omega(P')-\omega(P)=\sigma
\tag{1.3}
\]

with the same signed seam formula.  If a legal closing seam
\(c:v\to u\) is then selected, the closed voltage is

\[
                            V=\omega(P)+\delta(c).
\tag{1.4}
\]

Although the two summands in (1.4) depend on the section, their sum does
not.

## 2. Complete zero-holonomy tickets

The fixed-label central \(C_{14}\) has zero seam displacement: its old
seams are \(y_i\to x_i\), its new seams are \(y_i\to x_{i+1}\), and
permutation of the seven \(x\)-endpoints gives

\[
 \sum_i\bigl(g(x_{i+1})-g(y_i)\bigr)
 =\sum_i\bigl(g(x_i)-g(y_i)\bigr).
\tag{2.1}
\]

This is only the central circuit.  A completed repair ticket can also
contain cap backups, history collars, aperture discharge, an opening, and
topology joins.  Its actual displacement is

\[
\sigma_{\rm comp}
 =\sigma_{C_{14}}+\sigma_{\rm backup}+\sigma_{\rm hist}
  +\sigma_{\rm ap}+\sigma_{\rm join}.
\tag{2.2}
\]

Cap equality and history acceptance do not force (2.2) to vanish.

### Theorem 2.1 (one pump at a fixed modulus)

Suppose a quotient one-cycle in a free \(\mathbb Z_n\)-cover has voltage
\(v\) with \(\gcd(n,v)=1\).  Apply any finite sequence of completed tickets,
each of which

1. retains every fragment orientation;
2. outputs one quotient cycle; and
3. has \(\sigma_{\rm comp}=0\) in \(\mathbb Z_n\).

Then every intermediate and terminal quotient cycle has voltage \(v\), and
every physical development is one cycle.

#### Proof

Lemma 1.1 preserves \(v\) after each ticket.  A quotient cycle of voltage
\(v\) in a free cyclic cover develops into \(\gcd(n,v)\) physical cycles.
\(\square\)

Thus \(O(d)\) later repairs cost no additional voltage pumps once their
**completed** tickets satisfy the three displayed conditions.  Central
fixed-\(z\) holonomy zero alone is not enough.

Nor may one replace the one-cycle hypothesis by a component-count
argument.  If a ticket merges components of voltages \(v_1,\ldots,v_s\),
its output voltage is their signed oriented sum plus the complete seam
displacement.  In \(\mathbb Z_9\), merging voltages \(1\) and \(2\) with
zero seam displacement gives voltage \(3\), hence three physical cycles.
Such a ticket must carry the whole oriented fragment/component voltage
vector and prove that its merged total is a unit.  Theorem 2.1 applies only
inside one already declared oriented quotient cycle.

## 3. The exact cap/history/phase product state

At one fixed modulus, label a completed packet by

\[
  \mathfrak t=
  \bigl(\sigma;\Delta,b;\mathcal R_d^+,\mathcal R_d^-;
        \mathcal P_{\rm priv}\bigr).
\tag{3.1}
\]

Here \(\sigma\) is its complete seam displacement, \((\Delta,b)\) is its
cap-prefix state, \(\mathcal R_d^\pm\) are its phase-labelled positive and
negative history relations, and \(\mathcal P_{\rm priv}\) records the
literal resources and fragment order needed for a valid topology.

For serial packets \(A\) then \(B\),

\[
\begin{aligned}
 \sigma_{AB}&=\sigma_A+\sigma_B,\\
 \Delta_{AB}&=\Delta_A+\Delta_B,\\
 b_{AB}&=\max\{b_A,b_B-\Delta_A\},\\
 \mathcal R_{AB}^{\pm}
   &=\mathcal R_B^{\pm}\circ\mathcal R_A^{\pm}.
\end{aligned}
\tag{3.2}
\]

The resource and topology row is literal union plus compatibility, rather
than a scalar operation.  Formula (3.2) is therefore a product monoid on
labels, while the physically realizable tickets form a correlated
subsystem of that product.  In particular one may not combine a
zero-holonomy core, a cap backup, and an accepting history ticket chosen
independently.

Across a dimension change, (3.2) is not even a formal composition until
the Pascal node exports reindexing maps for the cap coordinates and both
history state spaces.  A coherent phase lift transports only the voltage
factor; it does not identify \((\Delta,b)\) or
\(\mathcal R_d^\pm\) across different alphabets.

A regenerative completed ticket has

\[
 \sigma=0,\qquad \Delta=0,\qquad b\le s,
\tag{3.3}
\]

and both history relations return the entrance state to the declared joint
guard domain.  The private topology row must still certify one output
path/cycle.

## 4. Same-parity Pascal transport has a phase obstruction

The natural cyclic deck group changes from \(\mathbb Z_n\) to
\(\mathbb Z_{n+2}\).

### Theorem 4.1 (no equivariant generator transport)

For odd \(n\), every homomorphism

\[
                     \phi:\mathbb Z_n\longrightarrow\mathbb Z_{n+2}
\tag{4.1}
\]

is trivial.  Consequently no equivariant phase embedding carries a
generator of the child cover to a generator of the parent cover.

#### Proof

The order of the image divides both \(n\) and \(n+2\).  Since
\(\gcd(n,n+2)=1\), the image has order one. \(\square\)

Equivalently, an affine phase rule
\(\phi(j+1)=\phi(j)+a\) obeys \(na=0\pmod{n+2}\), hence \(a=0\).
This is an architecture-specific obstruction to a functorial cyclic lift,
not a no-go for a symmetry-breaking Pascal construction.

Even retaining the same integer representative is not automatically safe:
\(5\) is a unit modulo \(13\) but not modulo \(15\).

### Proposition 4.2 (literal two-child phase equation)

Let two child cycles be opened and embedded as oriented parent paths
\(\widehat P_0,\widehat P_1\) in the parent \(\mathbb Z_{n+2}\)-cover.
Let \(s_{01},s_{10}\) be the crossed Pascal seams.  The parent voltage is

\[
 V_{n+2}
   =\omega_{n+2}(\widehat P_0)+\omega_{n+2}(\widehat P_1)
      +\delta_{n+2}(s_{01})+\delta_{n+2}(s_{10}).
\tag{4.2}
\]

The ordered-rail equality and Boolean cap containments of the private
Pascal port theorem make the two crossed seams literal, but do not
determine any term of (4.2).  Hence the current port record
\((\lambda;c\mid P,T)\) is not a phase-complete induction state.

The missing datum is a parent-native phase-labelled fragment record, not a
component count or a supply estimate.

### Theorem 4.3 (phase-coherent Pascal rectangle)

Work entirely in the parent \(\mathbb Z_{n+2}\)-cover.  For
\(i=0,1\), let \(P_i:s_i\to t_i\) be an oriented child fragment and
\(e_i:t_i\to s_i\) its old closing edge.  Put

\[
 v_i=\omega(P_i)+\delta(e_i).
\tag{4.3}
\]

Let the crossed edges be \(f_{01}:t_0\to s_1\) and
\(f_{10}:t_1\to s_0\).  Then

\[
 V_{\rm cross}=v_0+v_1+\sigma_\square,\qquad
 \sigma_\square=
   \delta(f_{01})+\delta(f_{10})
      -\delta(e_0)-\delta(e_1).
\tag{4.4}
\]

The four edges admit one common choice of physical lifts of
\(t_0,s_0,t_1,s_1\) if and only if

\[
 \delta(f_{01})+\delta(f_{10})
    =\delta(e_0)+\delta(e_1).
\tag{4.5}
\]

On this phase-coherent face, \(V_{\rm cross}=v_0+v_1\).  Hence a
parent-native unit plus a zero companion transports the unit exactly; two
equal parent-native units give \(2v\), also a unit for every odd parent
modulus.

#### Proof

Equation (4.4) is obtained by adding the two path and two crossed-seam
voltages.  If the endpoint phases are \(q(t_i),q(s_i)\), both sides of
(4.5) equal

\[
 q(s_0)+q(s_1)-q(t_0)-q(t_1).
\]

Conversely, fix the phase of \(t_0\), propagate along \(e_0,f_{10},e_1\),
and use (4.5) to verify \(f_{01}\).  Thus all four endpoint lifts are
consistent. \(\square\)

Boolean ordered-rail/cap compatibility does not imply (4.5); it is one
additional phase row.  If \(f_{10}\) is retained as the next aperture
closure, the opened crossed path retains the gauge-invariant potential
\(V_{\rm cross}\).  Its exterior discharge and eventual opening still
belong to the complete ledger.

## 5. A dimension-uniform sufficient seed

There is a clean conditional way around Theorem 4.1.  It deliberately
breaks cyclic equivariance and carries integer, rather than merely modular,
phase data.

### Definition 5.1 (coherent lifted Pascal port)

A same-parity Pascal splice is coherently phase lifted if it supplies:

1. distinguished integer lifts of every retained parent fragment and seam
   voltage in (4.2);
2. one parent-native quotient cycle whose total lifted voltage is an
   integer \(w\); and
3. for every completed later ticket, the exact integer version of
   (2.2) is zero.

This is an explicit certificate, not a gauge-invariant consequence of the
child quotient.  The distinguished sections and representatives are part
of the port state.

Exact integer zero is essential here.  A displacement \(2n\) is zero
modulo \(n\), but after the step \(n=13\) to \(15\) it changes a lifted seed
\(1\) into \(27\equiv12\pmod {15}\), which is not a unit.

### Theorem 5.2 (dyadic lifted-seed induction)

Assume every same-parity Pascal node exports a coherent lifted port with
the same nonzero integer total

\[
                              w=\pm2^a
\tag{5.1}
\]

for some fixed \(a\ge0\), and every later completed ticket has zero lifted
displacement.  Then reduction modulo every later odd dimension gives a
unit-voltage quotient cycle.  All developed carriers are connected,
including at composite dimensions.

#### Proof

Every odd modulus is coprime to \(2^a\).  Exact integer-zero ticket
displacement preserves \(w\), so Theorem 2.1 applies after reduction at
each node. \(\square\)

The choice \(w=\pm1\) is the smallest and strongest interface.

### Proposition 5.3 (sharpness for a fixed lifted total)

Along the unbounded same-parity sequence of all sufficiently large odd
moduli, a fixed nonzero integer \(w\) is a unit at every node if and only if
\(|w|\) is a power of two.

#### Proof

The forward implication forbids every odd prime divisor \(p\) of \(w\),
because the sequence contains an odd multiple of \(p\).  The reverse
implication is immediate. \(\square\)

This does not prove that the Boolean Pascal construction exports (5.1).
It isolates a concrete all-dimension target stronger than choosing an
unrelated unit residue at every node.

## 6. The persistent aperture phase criterion

Let \(P:u\to v\) be the single protected open path left by the Pascal
aperture.  After filtering by literal Boolean adjacency, cap-prefix
feasibility, both history guards, private-resource disjointness, and the
declared opening, let

\[
  D_{\rm acc}(P)
   =\{\delta(c):c:v\to u\text{ is an accepting legal closure}\}
   \subseteq\mathbb Z_n .
\tag{6.1}
\]

Its gauge-invariant closure-total set is

\[
                    K_{\rm acc}(P)=\omega(P)+D_{\rm acc}(P).
\tag{6.2}
\]

This marginal set is sufficient only after a deterministic terminal
cap/history guard has been fixed.  In the general relational state, closure
phase is correlated with terminal cap slack, positive and negative history,
and the private closure edge.  The exact exported object is therefore a
relation

\[
 \mathcal C_{\rm ap}\subseteq
   \mathcal S_{\rm cap/hist}\times\mathbb Z_n
                    \times\mathcal E_{\rm priv},
\tag{6.3}
\]

whose middle entry is the gauge-invariant closure total.  Serial
composition existentially joins on the **same** cap/history state.  Taking
independent marginals of \(\mathcal C_{\rm ap}\) is not sound.

### Theorem 6.1 (exact aperture unit test)

The aperture closes to one physical developed cycle without a fresh pump
if and only if

\[
                 K_{\rm acc}(P)\cap\mathbb Z_n^\times
                 \ne\varnothing .
\tag{6.4}
\]

#### Proof

For \(d_0\in D_{\rm acc}(P)\), Lemma 1.2 gives closed voltage
\(\omega(P)+d_0\).  Its development is connected exactly when this sum is a
unit modulo \(n\). \(\square\)

Condition (6.4) is gauge invariant because a section change translates
\(\omega(P)\) and every element of \(D_{\rm acc}(P)\) by opposite endpoint
coboundaries.

If (6.4) fails, a zero-holonomy internal ticket which preserves the framed
endpoints **and** regenerates the same accepting closure-total set cannot
repair the failure.  A zero-holonomy ticket can nevertheless change the
answer by consuming or creating a closure edge or changing a history guard.
Thus the protected object is \(K_{\rm acc}\), or one chosen unit closure,
not merely the open-path displacement.  A repair outside that protected
face is exactly an endpoint/closure-menu rebuild and must be audited as
such.

For composite \(n\), a useful sufficient form is that
\(D_{\rm acc}(P)\) contains a translated interval of length \(j(n)\), where
\(j(n)\) is the Jacobsthal function: the least length for which every
integer interval contains a number coprime to \(n\).  No current Pascal
theorem supplies such phase diversity.

The one-aperture lower theorem exports the debt count, an exterior target
occurrence, and the ordered Boolean port.  It does not export
\(K_{\rm acc}(P)\).  Thus the exact protected aperture record must be
enlarged to

\[
 (\lambda;c\mid P,T;\
   \mathcal C_{\rm ap}\text{ or a protected accepting unit closure};\
   \Delta,b,\mathcal R_d^+,\mathcal R_d^-).
\tag{6.5}
\]

If a packet reverses the aperture, it must also export the literal endpoint
swap and the involution
\((\omega,D_{\rm acc})\mapsto(-\omega,-D_{\rm acc})\); this is not covered
by same-orientation localization.

## 7. Composite dimensions and stabilizers

Write \(n=2r-1\).  The cyclic action on rank-\(r\) owners, and likewise on
rank-\((r-1)\) lower facets, is free even when \(n\) is composite: a
nontrivial stabilizer of order \(h>1\) would force \(h\mid n\) and \(h\)
to divide the relevant rank, contradicting the corresponding gcd-one
identity.

The same statement need not hold for cap resources of rank \(r+1\), since

\[
                  \gcd(2r-1,r+1)=\gcd(3,r+1).
\tag{7.1}
\]

Hence the voltage factor may be evaluated on the free owner cover, but cap
currents at three-stabilizer dimensions must be expanded physically or
weighted by stabilizer/coset phase.  A quotient cap balance which ignores
that distinction is not a completed-ticket certificate.

## 8. Exact remaining induction lemma

The missing row can now be stated without a component or abundance
shortcut.

> **Phase-lifted private Pascal aperture lemma.**  At every same-parity
> node, choose the two child embeddings, crossed private ports, surviving
> aperture, cap backups, history collars, and topology joins jointly so
> that:
>
> 1. the parent fragments and seams have a child-native coherent integer
>    lift of total \(\pm1\) (or another fixed dyadic total);
> 2. the lower one-copy owner/target payload and ordered port equations
>    remain exact;
> 3. the surviving aperture satisfies (6.4), and an accepting unit closure
>    or its full correlated relation \(\mathcal C_{\rm ap}\) is protected
>    through every later ticket, with its exterior discharge and declared
>    opening included;
> 4. every later fixed-\(z\) repair is a **completed** ticket with zero
>    lifted displacement and an accepting cap/history product state; and
> 5. every dimension step exports the cap-coordinate and history-state
>    reindexing maps, and every prefix remains one oriented path/cycle with
>    literal private resources.

Under these hypotheses Theorems 2.1, 5.2, and 6.1 prove the full voltage
and lower phase induction, with one pump paid ancestrally rather than once
per dimension or repair.

What is not proved is precisely item 1 (or, more weakly, a parent-native
unit in (4.2)) together with the correlated physical realization of item
4.  The current private Pascal record, stationary pull-clock types, and
one-debt aperture theorem do not contain those data.  Therefore a fresh
voltage pump or a closure-menu-changing rebuild is required exactly at the
first node where the parent-native unit row or protected aperture test
(6.4) fails.

## 9. Scope

The theorem closes, conditionally and exactly:

1. voltage transport inside one fixed free cover;
2. serial use of any number of complete zero-holonomy repairs;
3. the composite-modulus connectedness test;
4. the cap/history/phase composition law; and
5. the exact no-pump test for the persistent aperture.

It does not construct:

1. the phase-lifted Pascal port of Section 8;
2. a completed fixed-\(z\) ticket whose backups and collars also have zero
   displacement;
3. arbitrary-width upper coverage or exterior crossing-window repair;
4. ambient residence;
5. one-star consolidation; or
6. the terminal common-cap compiler.

Accordingly this is a proof-safe reduction of the remaining induction row,
not an all-\(k\) upper bound.

## 10. Source chain

The fixed-cover localization used here is proved in
[MATH_THEOREM_K17_ORIENTATION_FREE_SHORT_RUN_CLAUSES_AND_VOLTAGE_LOCALIZATION_20260802.md](MATH_THEOREM_K17_ORIENTATION_FREE_SHORT_RUN_CLAUSES_AND_VOLTAGE_LOCALIZATION_20260802.md).
The phase-coherent rectangle is independently derived in
[MATH_THEOREM_K_PASCAL_PHASE_COHERENT_VOLTAGE_TRANSPORT_AND_FRESH_PUMP_GATE_20260802.md](MATH_THEOREM_K_PASCAL_PHASE_COHERENT_VOLTAGE_TRANSPORT_AND_FRESH_PUMP_GATE_20260802.md).
The cap/history factors and the persistent aperture come from
[MATH_THEOREM_K_HEPTAGONAL_CAP_HISTORY_PRODUCT_MONOID_AND_REGENERATIVE_SELECTOR_GATE_20260802.md](MATH_THEOREM_K_HEPTAGONAL_CAP_HISTORY_PRODUCT_MONOID_AND_REGENERATIVE_SELECTOR_GATE_20260802.md)
and
[MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md](MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md).
The independent scope audit is
[MATH_AUDIT_K_COPRIME_VOLTAGE_LOCALIZATION_PASCAL_TRANSPORT_20260802.md](MATH_AUDIT_K_COPRIME_VOLTAGE_LOCALIZATION_PASCAL_TRANSPORT_20260802.md).
