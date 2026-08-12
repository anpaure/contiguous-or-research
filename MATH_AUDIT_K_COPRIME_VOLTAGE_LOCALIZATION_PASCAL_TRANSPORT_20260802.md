# Independent audit: coprime-voltage localization, zero-holonomy tickets, and Pascal transport

**Date:** 2026-08-02  
**Status:** proof audit.  The fixed-modulus localization theorem passes.  A
same-parity Pascal transport does not follow from it; an exact child-native
phase-lift certificate is necessary.

This note audits
`MATH_THEOREM_COPRIME_VOLTAGE_LOCALIZATION_AND_ZERO_HOLONOMY_REPAIR_20260802.md`
against the heptagonal circuit, the cap/history product monoid, and the
persistent one-aperture interface.  It makes no upper-deck, host-exposure,
residence, or compiler existence claim.

## 1. Fixed-modulus fragment identity

Let a free cyclic cover have deck group `G=Z_n`.  Fix a section of the
quotient vertices, and write `delta(e) in G` for the voltage of an oriented
edge.  Suppose a directed quotient cycle `F` is cut at oriented edges
`e_0,...,e_(t-1)`, its retained directed fragments are used without reversal,
and new oriented seams `f_0,...,f_(t-1)` concatenate those fragments into one
directed quotient cycle `F'`.  Then

\[
 V(F')-V(F)=\sum_i\delta(f_i)-\sum_i\delta(e_i).       \tag{1.1}
\]

This is an identity: the retained-fragment sums cancel term by term.  It is
also gauge invariant.  Changing the section adds a vertex coboundary to each
edge voltage, and the coboundary sum on either closed cycle is zero.

The orientation hypothesis is load-bearing.  If a retained fragment is
reversed, its contribution changes sign and must be entered separately in
the full fragment ledger.  Likewise (1.1) does not apply if the output is a
cycle cover rather than the declared one quotient cycle.

Consequently a serial word of one-cycle rethreads preserves a seed voltage
`v` exactly when the sum of the **complete-ticket** seam displacements is
zero.  Requiring every prefix displacement to be zero is a stronger
sufficient condition which keeps every intermediate developed factor
connected.

## 2. Fixed-`z` heptagon

For the phasewise fixed-label `C14`, orient the old seam in row `i` as

\[
 y_i\longrightarrow x_i
\]

and the new seam as

\[
 y_i\longrightarrow x_{i+1}.
\]

If `g(w)` is the fibre coordinate of the chosen endpoint representative,
then

\[
 \begin{aligned}
 \sum_i\delta(y_i,x_i)
   &=\sum_i(g(x_i)-g(y_i)),\\
 \sum_i\delta(y_i,x_{i+1})
   &=\sum_i(g(x_{i+1})-g(y_i)).
 \end{aligned}                                          \tag{2.1}
\]

The sums agree because `i -> i+1` permutes the seven `x` endpoints.  Hence
the central fixed-`z` circuit has zero seam displacement.  Together with the
odd step-two retained-path order, this proves a one-cycle, zero-holonomy
central rethread.

There is one essential scope boundary.  A **completed** ticket contains the
central `C14` plus any cap backups, history collars, aperture discharge, and
topology joins.  Equation (2.1) proves zero displacement only for the central
`C14`.  The auxiliary seams have their own displacement.  Therefore

\[
 \sigma_{\rm complete}
  =\sigma_{C14}+\sigma_{\rm backup}
   +\sigma_{\rm history}+\sigma_{\rm aperture}
   +\sigma_{\rm join}                                  \tag{2.2}
\]

must be checked, and the required value is zero.  Cap balance and acceptance
of the history relation do not imply (2.2).  For example, in `Z_9`, a seed
of voltage `1` followed by a central zero-holonomy circuit and an otherwise
legal auxiliary seam word of displacement `2` has terminal voltage `3`, so
its development has three components.

Thus the theorem's phrase "topology-safe zero-holonomy family" is a valid
hypothesis only when it refers to the whole completed ticket, not merely its
fixed-`z` core.

## 3. Composite modulus

For a free `Z_n` cover, a quotient cycle of voltage `v` develops into

\[
                       \gcd(n,v)                         \tag{3.1}
\]

physical cycles.  Hence the correct connectedness condition for arbitrary,
possibly composite `n` is

\[
                         v\in (\mathbb Z_n)^\times.      \tag{3.2}
\]

Nonzero voltage alone is insufficient; `v=3` in `Z_9` is the smallest
relevant example.  The audit therefore confirms the composite-`n` wording
of the localization note **on a free-orbit face**.

If owners, facets, or endpoints have stabilizers, the ordinary regular-cover
development formula (3.1) is unavailable.  One must expand physically or
carry stabilizer/coset phase.  The theorem's opening free-action hypothesis
is therefore essential and must not be dropped in an all-composite-`k`
application.

## 4. Why a Pascal child does not inherit the phase seed formally

A same-parity dimension step changes the natural cyclic deck group from
`Z_n` to `Z_(n+2)`.  There is no nontrivial group-homomorphic transport of a
generator between these two covers.

Indeed the image of any homomorphism

\[
                 \phi:\mathbb Z_n\longrightarrow\mathbb Z_{n+2}          \tag{4.1}
\]

has order dividing

\[
                    \gcd(n,n+2)=\gcd(n,2).               \tag{4.2}
\]

For odd `n` the image is trivial.  For even `n` it has order at most two,
and no image element generates `Z_(n+2)` for `n>=4`.  Thus an equivariant
parent generator cannot be functorially carried to a child generator.

Even preserving the same integer voltage is not enough.  Voltage `3` is
coprime to `7` but not to `9`.  The child must be supplied with a
**child-native phase lift**: oriented child fragments and seams with total

\[
 v_{n+2}=\sum_e\widetilde\delta(e)\pmod{n+2},
 \qquad \gcd(n+2,v_{n+2})=1.                           \tag{4.3}
\]

After (4.3), zero-holonomy complete tickets preserve the seed.  Without
(4.3), the missing object is exactly one fresh voltage pump (or an equivalent
child-native rephasing).  This is not a raw-abundance issue: it is a change
of deck group.

A particularly clean sufficient interface would export, in every child, a
distinguished section in which the protected seed has voltage `+1` or `-1`.
That would satisfy (4.3) for every modulus.  Existence of such an aligned
section is not proved by the Pascal port or aperture theorems.

## 5. Product state with cap, history, and the persistent aperture

At a fixed modulus, let `v` be the current host-cycle voltage and let
`sigma` be a packet's seam displacement.  The proof-safe protected host
state and packet label are at least

\[
 \begin{split}
 &\text{host: }(v;s;Q_*,J,o_J,e_{\rm open};\mathcal P),\\
 &\text{packet: }(\sigma;\Delta,b;
             \mathcal R_d^+,\mathcal R_d^-;\mathcal P_{\rm pkt}).
 \end{split}                                             \tag{5.1}
\]

Here `(Delta,b)` is the exact cap-prefix state, the two relations are
phase-correct positive/negative histories, and the
remaining fields record the persistent aperture, its missing colour and
exterior occurrence, the declared opening, and private resources.
Packet concatenation and its action on the host are exact:

\[
 \begin{aligned}
 \sigma_{AB}&=\sigma_A+\sigma_B\pmod n,
       &v'&=v+\sigma_{AB}\pmod n,\\
 \Delta_{AB}&=\Delta_A+\Delta_B,\\
 b_{AB}&=\max\{b_A,b_B-\Delta_A\},\\
 \mathcal R_{AB}^{\pm}&=\mathcal R_B^{\pm}
                         \circ\mathcal R_A^{\pm}.
 \end{aligned}                                          \tag{5.2}
\]

The one-aperture theorem proves that the **debt count** remains one under
rank/depth suspension and that its positive pivot history is a
constant-output reset.  It proves neither `sigma_aperture=0` nor a child
voltage lift.  The exterior `J` occurrence and the actual opening may change
the seam bank, so their contribution must be included in `v` through (1.1).

Accordingly the persistent aperture is compatible with voltage localization
under either of the following exact alternatives:

1. its entire completed aperture/pivot macro is a one-cycle rethread with
   zero seam displacement; or
2. its audited displacement is carried as `sigma` in (5.1), and the
   terminal host voltage is a unit modulo the child modulus.

The first alternative is the regenerative one desired by the proposed
induction.  It remains a host-planting lemma, not a consequence of the
one-debt relay.

## 6. Proof-safe induction statement

The strongest conclusion supported by the audited results is conditional.

> **Child-native seed plus zero-holonomy return.**  At every same-parity
> Pascal step, suppose the child contains one protected quotient one-cycle
> on a free `Z_(n+2)` face with a child-native unit voltage (4.3).  Suppose
> the persistent aperture is embedded with its exterior discharge and
> opening, and every later cap/history/upper repair is a complete one-cycle
> ticket of total displacement zero.  Then all repairs preserve the child
> voltage, including for composite `n+2`, and the final developed carrier is
> one physical cycle.

The proof is repeated application of (1.1).  Cap-prefix feasibility and
history acceptance are checked simultaneously by (5.2); they are logically
independent of the voltage row.

The exact remaining induction lemma is therefore not central heptagon
supply.  It is the correlated construction of

1. one child-native unit-voltage protected seed;
2. the persistent aperture/exterior opening;
3. balanced cap backups and bi-history tickets; and
4. zero **total** displacement for every completed later ticket.

Failure of item 1 requires a fresh voltage pump.  Failure of item 4 means
the fixed-`z` central circuit was completed by a nonzero-holonomy sidecar and
must be balanced by another ticket; it cannot be called a zero-holonomy
repair.

## 7. Verdict

The voltage-localization theorem, its fixed-`z` central application, and its
free-cover composite-modulus statement are correct.  They prove that one
coprime child-native seed suffices **within a fixed child modulus**.

They do not transport that seed through a same-parity Pascal dimension
change.  The sharp formal obstruction is (4.2).  Nor do they prove that a
completed fixed-`z` ticket is zero-holonomy; equation (2.2) is the missing
audit.  The persistent aperture carries one target debt but no automatic
phase certificate.  These are precisely the two rows that must be added to
the cap/history product recurrence.

## 8. Independent addendum: rectangle sum, dyadic lift, and aperture menu

A second derivation checked the strengthened induction interface in
MATH_THEOREM_K_PASCAL_COPRIME_SEED_TRANSPORT_AND_APERTURE_VOLTAGE_GATE_20260802.md.

For two opened child fragments expressed in one parent-native cover, direct
edge summation gives

\[
 V_{\rm cross}=v_0+v_1+
 \delta(f_{01})+\delta(f_{10})-\delta(e_0)-\delta(e_1).
\tag{8.1}
\]

The four old/crossed edges use one common choice of physical endpoint lifts
exactly when the last four terms in (8.1) sum to zero.  Thus the
phase-coherent rectangle law \(V_{\rm cross}=v_0+v_1\) is exact.  A
parent-native unit plus zero, or two equal units over an odd modulus, gives
a unit parent.  This remains a parent-native statement and does not evade
Section 4.

The proposed coherent integer lift also passes.  If one fixed nonzero
integer \(w\) is reduced modulo every sufficiently large odd dimension,
then it is a unit at every node exactly when \(|w|=2^a\).  An odd prime
divisor of \(w\) divides a later odd modulus; conversely powers of two are
coprime to every odd modulus.  Exact integer-zero completed-ticket
displacement preserves this property.  Modular zero at the old dimension
does not: displacement \(26\) is zero modulo \(13\), but changes lifted
voltage \(1\) to \(27\equiv12\pmod {15}\).

For a framed aperture path, the intrinsic phase object is not its open
displacement alone.  If \(D_{\rm acc}\) is the legal closing-gain menu, the
gauge-invariant set is

\[
                        K_{\rm acc}=\omega(P)+D_{\rm acc}. \tag{8.2}
\]

The no-pump test is exactly

\[
                        K_{\rm acc}\cap\mathbb Z_n^\times
                        \ne\varnothing.                 \tag{8.3}
\]

Zero holonomy preserves (8.3) only when the framed endpoints and accepted
closure menu are also protected.  A zero-current rethread can expose or
consume a closure edge or alter its terminal history guard.  With
nondeterministic terminal histories, the exact state is consequently a
relation among cap/history state, closure total, and the private closing
edge; independent marginals are insufficient.

Finally, zero seam current is not a multi-component shortcut.  Merging
component voltages \(1\) and \(2\) in \(\mathbb Z_9\) with zero seam
current gives voltage \(3\) and three developed cycles.  Either every
ticket acts within the declared one-cycle, or the full signed component
voltage vector must be carried and its merged total proved to be a unit.

With these qualifications, the strengthened theorem passes.  The smallest
unproved row is a parent-native phase-lifted Pascal splice exporting a
dyadic total, a correlated accepting unit aperture closure, cap/history
reindexing, and completed fixed-\(z\) tickets of zero total integer
displacement.
