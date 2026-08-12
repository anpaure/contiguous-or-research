# Two incidence phases repair the root-path `C6` balance defect

**Date:** 2026-08-07  
**Method:** literal degree balance in a union of two perfect matchings  
**Status:** unconditional switching lemma and exact reduction.  It does not
construct the required second phase.  It shows that the correction in
`MATH_CORRECTION_GK_ROOT_PATH_C6_SYMMETRIC_DIFFERENCE_NONALTERNATING_20260807.md`
can be repaired by one ordered two-SDR host, provided the root-edge packets
lift in alternating phases with the stated privacy.  Thus the physical
root-path gate and the MNW ordered-two-SDR gate can be attacked as one
correlated host problem.

## 1. Phase-resolved packets

Let `G=(L,R;E)` be bipartite and let

\[
                         F=M_0\mathbin{\dot\cup}M_1                 \tag{1.1}
\]

be the union of two edge-disjoint perfect matchings.  Hence `F` is a
spanning simple two-factor, with one selected edge of each phase at every
vertex.

A **phase-`c` balanced packet** is a pair of edge sets

\[
                         (O^c,N^c),\qquad c\in\{0,1\},              \tag{1.2}
\]

such that

1. `O^c subset M_c` and `N^c subset E-F`;
2. for every vertex `v`,

   \[
               d_{O^c}(v)=d_{N^c}(v)\in\{0,1\};                   \tag{1.3}
   \]

3. the graph `O^c union N^c` is an even alternating circuit, or a
   disjoint union of such circuits.

An ordinary matched `C6` is the basic example: its three old edges lie in
one matching phase and its three cross edges lie outside the two-factor.
Condition 1 explicitly excludes the otherwise dangerous possibility that
a cross edge of one packet is already occupied by the other phase.

Consider a family `A` of phase-resolved packets.  Call it **locally
simple** when

* no old edge occurs in two packets;
* no new edge occurs in two packets; and
* at every vertex, at most one packet of each phase is incident.

Packets of opposite phase may share a vertex.  This is the overlap needed
at an internal root.

## 2. Simultaneous two-phase switching

### Theorem 2.1 (balanced union switch)

For a locally simple family `A`, put

\[
 O=\mathop{\dot\bigcup}_{A\in\mathcal A}O_A,
 \qquad
 N=\mathop{\dot\bigcup}_{A\in\mathcal A}N_A,
 \qquad
 F'=(F-O)\mathbin{\dot\cup}N.                       \tag{2.1}
\]

Then `F'` is a spanning simple two-factor.

### Proof

Fix a vertex `v`.  Sum (1.3) over all packets incident with `v`.  Local
simplicity makes both sums literal edge counts, so

\[
 d_{F'}(v)
 =d_F(v)-\sum_A d_{O_A}(v)+\sum_A d_{N_A}(v)
 =2.                                                 \tag{2.2}
\]

The old and new edge banks are separately disjoint, and `N` is disjoint
from `F`; hence `F'` has no repeated edge.  Thus it is a spanning simple
two-factor.  \(\square\)

The theorem deliberately does not assert that `O union N` is one
alternating cycle relative to `F`.  That stronger statement is false for
the one-phase root-path symmetric difference.  Degree balance is the exact
condition needed to obtain the new two-factor.

## 3. Alternating phases along a root path

Let

\[
                         U_0U_1\cdots U_t                         \tag{3.1}
\]

be a simple path in a root-rotation graph.  Give edge `U_(i-1)U_i` phase

\[
                         c_i=i\pmod2.                              \tag{3.2}
\]

Suppose that for every path edge and its assigned phase there is a
phase-resolved paired-root packet with the following literal overlap
rules.

1. At an internal root `U_i`, the two adjacent packets use the two
   different selected incidences

   \[
                         f_{U_i}^{0}\in M_0,
                         \qquad f_{U_i}^{1}\in M_1.                \tag{3.3}
   \]

2. Their two new cross incidences at the shared root are distinct and lie
   outside `F`.
3. Away from shared consecutive roots, all old and new incidences are
   private.

### Corollary 3.1 (two-phase root-path lift)

Under these hypotheses, all path packets may be applied simultaneously
and the result is a spanning simple two-factor.

### Proof

At an internal root, the two packets have opposite phases by (3.2), so
their old edges are the distinct edges (3.3); hypothesis 2 makes their new
edges distinct.  At every other used vertex there is only one incident
packet.  Hypothesis 3 supplies global edge privacy.  The family is locally
simple, and Theorem 2.1 applies.  \(\square\)

This is the exact local repair of the `0,0` defect in the correction note.
In a single matching phase, the shared selected edge cancels and two new
cross edges remain.  In two phases, the two packets instead remove the two
different old edges at the shared root and install the two different new
edges:

\[
                         (1_0,1_1)\longmapsto(1'_0,1'_1).           \tag{3.4}
\]

No higher circuit is required merely for degree balance.

## 4. Currents and protected ledgers

Let `partial_q(A)` denote any additive signed occurrence current of a
packet at width `q` (lower palette, upper palette, or a protected witness
ledger).  For a locally simple family,

\[
                         \partial_q(\mathcal A)
                         =\sum_{A\in\mathcal A}\partial_q(A).       \tag{4.1}
\]

Consequently:

* if every packet is `q`-neutral, their two-phase union is `q`-neutral;
* if the negative support of every packet has a private retained provider,
  those providers remain valid after the union; and
* occurrence-labelled protection is preserved whenever the old/new banks
  are disjoint from the protected bank.

These statements are just additivity plus literal privacy.  They do not
derive privacy from uncoloured Hall data.

Topology needs one additional, separate input.  When adjacent packets
share a vertex and remove both phase edges there, their individual
two-break permutations do not compose independently.  One must compute the
**combined occurrence-level socket reconnection permutation** of the whole
locally simple family and require that this combined permutation has the
claimed forest-merge rank.  The fact that the projected root edges form a
forest is not sufficient by itself.  Theorem 2.1 supplies degree
preservation but does not certify this combined component action.

## 5. Ordered-two-SDR formulation

An ordered two-SDR is exactly an ordered pair `(M_0,M_1)` of edge-disjoint
perfect incidence matchings.  Therefore the following single host
statement is sufficient for both the corrected root topology and the MNW
annulus.

> **Joint phase-resolved ordered-two-SDR host.**  Construct an ordered
> two-SDR which extends the finite coloured MNW annulus pattern and, on
> every selected Catalan-rotor root path, supplies the paired-root packet
> for successive root edges in alternating phases, with private new edges,
> the prescribed component reconnections, and the protected
> upper/residence/compiler tickets.

If this host exists, Corollary 3.1 supplies the physical two-factor along
every root path, while the static-annulus theorem supplies the carried B8
upper relay and its marked seam.  Thus the correction does not logically
force an unrelated third packet technology: it can be absorbed into the
same two-phase incidence object already required by the upper lane.

This is a reduction, not an existence proof.  In particular:

1. the original GK successor matching supplies only one phase;
2. an arbitrary second perfect matching need not reproduce the literal
   paired-root `C6` identities;
3. uncoloured degree-two Hall does not prescribe the successor order or
   the alternating root phases; and
4. the ten-bit MNW module presently lacks a complete occurrence-labelled
   `(P_0,P_1,N,omega)` ledger.

There is also a sharp same-facet obstruction.  On the standard GK facets,
every hexagon for a root edge contains one phase-zero matching edge on one
of its two parities.  Declaring that parity old makes the two matchings
intersect; declaring the other parity old puts a nominally new edge inside
the original two-factor.  Thus the second phase cannot be obtained merely
by recolouring the same standard-facet `C6`.  It must use different
phase-specific facets or occurrence copies, a larger packet, or a global
switch which removes the reused phase-zero edge at the same time.  This is
proved in
`MATH_AUDIT_TWO_PHASE_ROOT_PATH_BALANCE_AND_SAME_HEXAGON_NOGO_20260807.md`.

The exact remaining local question is therefore sharper than “find a
higher alternating circuit”:

\[
 \boxed{\text{lift each required root edge in its assigned phase inside
 one protected ordered two-SDR.}}                    \tag{5.1}
\]

## 6. Scope audit

* No one-phase root-path symmetric difference is called alternating.
* No serial use of two `C6`s sharing one selected edge is used.
* Theorem 2.1 proves only degree-two feasibility; component action is an
  explicit combined-socket hypothesis.
* Cross edges are required to avoid both matching phases, not merely the
  phase being toggled.
* The theorem makes no claim that the joint ordered-two-SDR host exists.
