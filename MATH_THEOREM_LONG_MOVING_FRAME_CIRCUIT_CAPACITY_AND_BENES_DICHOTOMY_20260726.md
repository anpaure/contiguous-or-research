# Long moving-frame compounds: capacity and the Beneš dichotomy

Date: 2026-07-26

This note continues the literal four-slab audit.  It is conditional on a
valid literal packet compiler.  The statements about matching-status owner
components are independent of that compiler.

## 1. Weighted long-path necessity

Let a legal state be partitioned into owner-disjoint compound components
(C).  Let (w_C) be the owner mass of (C).  Assume that its nonlinear
threshold interaction graph has degree at most (Delta): every elementary
slab derivative can have common literal targets with derivatives from at
most (Delta) other slabs in the compound.  For every interacting packet
pair choose one inconsistent alternating frame path and let
(\ell_C) bound the lengths of these chosen paths.

The defect-path transversal theorem and the exact direction count imply
that at signed depth (q<R), the total cooperative gain of (C), beyond
the sum of its one-slab gains, is at most

\[
O\!\left(\Delta {q\ell_C\over R}w_C\right).
\tag{1.1}
\]

Indeed, a common target must vary a direction on the chosen defect path;
one direction occurs in the support of exactly a (q/R) fraction of the
packet starts.  Charge every threshold holonomy term to one interacting
pair.  Bounded interaction degree prevents multiple charging by more than
(O(\Delta)).

Summing owner-disjoint components gives:

### Theorem 1.1 (moving-frame length requirement)

If all elementary slab moves are nonimproving and a compound family lowers
the depth-(q) hole count by at least (b_qW), then

\[
\boxed{
{1\over W}\sum_Cw_C\ell_C
 \ge c\,{b_qR\over\Delta q}
}
\tag{1.2}
\]

for an absolute (c>0).

Thus bounded-degree Eulerian compounds which repair a linear defect at
depth (q) require owner-mass-weighted frame paths of length
(\Omega(R/q)).  One common construction intended to repair a linear
depth-one defect must use paths of weighted length (Omega(R)).  Merely
having (H) stages or (O(\log R)) routing depth is not the relevant
quantity; the relevant quantity is the alternating-cycle length of the
input and output pair frames.

## 2. Exact owner cost of a long alternating circuit

Let (mathcal A) be the matching frames used by a compound and let

\[
G_{\mathcal A}=(V,\bigcup_{M\in\mathcal A}M)
\]

be their coordinate union graph.  Every matching-status recoupling moves
one selected coordinate along an edge of this graph.  Hence it preserves

\[
\bigl(|X\cap B|\bigr)_{B\in\operatorname{Comp}(G_{\mathcal A})}.
\tag{2.1}
\]

Conversely, on every connected coordinate component (B), the simple
exclusion graph on its (k)-subsets is connected.  Therefore the common
owner components are exactly the fibres of (2.1).

For one alternating path or even cycle on (t) coordinate vertices, the
owner component at occupancy (k) contains

\[
\binom tk
\tag{2.2}
\]

states on those coordinates.  At central occupancy this is

\[
\binom t{\lfloor t/2\rfloor}
=2^{t-O(\log t)}.
\tag{2.3}
\]

Thus the long paths forced by (1.2) are not independent local switches in
the matching-status model.  They merge exponentially many owner states
into one exact recoupling component.  If the circuit spans all physical
coordinates, the global middle-rank constraint fixes its occupancy and the
entire middle layer is one component.

This is a statewise owner invariant, not an entropy heuristic.

## 3. Eulerian closure does not remove the invariant

An alternating even circuit is Eulerian in the direction-exchange
projection, and a closed compound cancels its first direction marginal at
every depth.  Nevertheless, Eulerianity does not alter (2.1): every move
remains an exclusion move inside the same coordinate component.

Consequently a long Eulerian frame circuit has the exact dichotomy:

1. If it is kept as many small componentwise choices, its frame components
   remain short and Theorem 1.1 gives (o(W)) correction capacity.
2. If its matching union contains the required (Omega(R/q))-length
   components, the owner choices coalesce into the large occupancy fibres
   (2.2).  When the union is connected, only one global status-component
   frame choice remains.

The second branch is precisely the connected case of the moving-frame
integrality theorem: a global selected pair frame has a linear Gaussian
target deficit even though the symmetric fractional frame mixture has no
deficit.

## 4. What a Beneš network does and does not supply

A classical Beneš network can route a permutation with an (R)-cycle using
(O(\log R)) switch stages.  Hence switching depth by itself is not a
geometric obstruction to the length requirement (1.2): the union of the
input and output matchings can have an alternating cycle of length
(\Theta(R)).

The obstruction is exact ownership of the independently programmable
switches.

* The currently proved (Q_4) multilayer bank composes only because its
  prefix-displacement intervals are disjoint.  It gives many exact bits,
  but it does not route the conjugated matchings at crossing layers and
  proves no arbitrary Beneš network.
* At a crossing of two independently controlled layers, the local owner map
  admits only twelve of the sixteen formal two-switch states.  Thus formal
  (2\times2) switch programmability does not tensor across crossings.
* If all matching layers of a multiscale Beneš atlas are admitted so that
  their wire graph is connected, the owner-component classification (2.1)
  makes the whole middle layer one status component.  Componentwise
  rounding then selects one global frame, returning the known linear Hall
  deficit.

Therefore the proposed Beneš escape cannot be obtained by combining
independent local switch bits in the canonical matching-status recoupling
model.  A Beneš diagram proves abstract permutation reachability; it does
not prove a fragmented exact owner factor.

## 5. Capacity/no-go theorem for the canonical route

Combining Sections 1--4 gives the following exact boundary.

### Theorem 5.1 (long-circuit capacity dichotomy)

Consider an owner-disjoint, bounded-interaction family of compound slab
circuits built from pair-frame status recouplings.

1. If its owner-mass-weighted alternating path length is
   (o(R/q)), it can correct only (o(W)) holes at signed depth (q).
2. If it has the (Omega(R/q)) path length needed for linear correction,
   those paths lie in matching-union components whose central owner fibres
   have size (2^{\Omega(R/q)}).
3. If the admitted matching union is connected in order to route all
   positive-density frame cuts, the integral status selector has one global
   middle-owner component and suffers the existing (Omega(W)) Gaussian
   deficit.

Hence no canonical status-cell Beneš/Eulerian compound simultaneously has

\[
\begin{gathered}
\text{linear one-sided correction capacity,}\qquad
\text{independently selectable owner-disjoint components,}\qquad
\text{and all-cut moving-frame transport.}
\end{gathered}
\tag{5.1}
\]

## 6. Surviving escape

The theorem does not rule out a finer cycle-factor overlay inside one large
status component.  Such an escape must prove all of the following, none of
which follows from a Beneš wiring diagram:

1. an exact crossing-layer Latin theorem producing the required long output
   frame cycles;
2. cycle-level ownership components much smaller than the occupancy fibres
   (2.2);
3. a strict fragmentation inequality for their literal all-depth effects;
4. threshold holonomy of the favourable sign, common through every
   protected depth.

This is the precise remaining version of the multiscale Beneš proposal.
The ordinary matching-status implementation is obstructed; a genuinely
finer owner overlay remains open.

