# Audit of the coupled-insertion compact two-size rail absorber and its nested port lattice

**Date:** 2026-08-07  
**Audited note:**
`MATH_THEOREM_COUPLED_INSERTION_COMPACT_TWO_SIZE_RAIL_ABSORBER_20260807.md`

## 1. Verdict

The numerical and positivity claims in Lemma 1.1 and Theorem 2.1 are
correct as stated.  In particular, for every (1\leq \ell<M-2), each
state has exactly (2\ell-1) exclusive named values, and at the owner
width (q=d+1) this is exactly (2d+1) ports per state.

There are two qualifications.

1. The exclusive values over successive widths are not literally two
   nested chains.  They form two triangular left/right extension cones.
   This distinction matters when one tries to embed a prescribed
   multi-width leave.
2. The note constructs one exact atomic switch but does not identify its
   generated lattice with the full admissible leave lattice.  A collection
   of gadgets can absorb only a sum of these coherent insertion currents,
   and positive absorption additionally requires a collision-free
   realization of that sum.

The phrase “an (O(d)) named footprint at every width” should also be read
as applying to the owner width and to any other protected widths
(\ell=O(d)).  The exact footprint at width \(\ell\) is
(2\ell-1), which is not (O(d)) when \(\ell\) itself is much larger than
(d).

## 2. Exact one-cut port coordinates

Fix a directed cut of the base cycle and write the local cyclic order as

\[
 \cdots,a_2,a_1\mid b_1,b_2,\cdots,
\]

where the cut edge is (a_1b_1).  For (r,s\geq0), put

\[
 L_r=\{a_r,\ldots,a_1\},\qquad
 R_s=\{b_1,\ldots,b_s\},
\]

with (L_0=R_0=\varnothing).  At width \(\ell\), define

\[
 \begin{aligned}
 Z_{\ell,r}&=\{z\}\cup L_r\cup R_{\ell-1-r},
       &&0\leq r\leq \ell-1,\\
 E_{\ell,r}&=L_r\cup R_{\ell-r},
       &&1\leq r\leq \ell-1.
 \end{aligned}
\tag{2.1}
\]

The (Z_{\ell,r}) are exactly the \(\ell\) new intervals containing
(z).  The (E_{\ell,r}) are exactly the \(\ell-1\) old intervals
crossing the cut edge.  Hence, for a fixed core (B), the signed insertion
current is

\[
 g_\ell(B,\gamma)
 =\sum_{r=0}^{\ell-1}{\bf e}_{B\cup Z_{\ell,r}}
  -\sum_{r=1}^{\ell-1}{\bf e}_{B\cup E_{\ell,r}},
\tag{2.2}
\]

where \(\gamma\) records the base order and its cut.

This also gives the precise nesting.  Every (Z_{\ell,r}) has the two
one-coordinate extensions

\[
 Z_{\ell+1,r},\qquad Z_{\ell+1,r+1},
\]

and every (E_{\ell,r}) has the two extensions

\[
 E_{\ell+1,r},\qquad E_{\ell+1,r+1}.
\]

Thus each exclusive family is a triangular interval cone indexed by
((\ell,r)), not a freely selectable list of ports and not a single chain.

## 3. The exact coupled current

Let a frame be

\[
 F=(D,x,y,z,\tau,\gamma_x,\gamma_y)
\]

with the data of Theorem 2.1.  The two cuts \(\gamma_x,\gamma_y\) lie in
the same base cycle \(\tau\), but may be chosen independently.  The
width-(\ell) state difference is exactly

\[
 \boxed{
 \Delta_\ell(F)
 =g_\ell(D+x,\gamma_x)-g_\ell(D+y,\gamma_y).}
\tag{3.1}
\]

Equivalently, its positive and negative supports are

\[
 \begin{aligned}
 P_\ell(F)
 &=\{D+x\cup Z^x_{\ell,r}:0\leq r\leq\ell-1\}\\
 &\quad\cup
   \{D+y\cup E^y_{\ell,r}:1\leq r\leq\ell-1\},\\[2mm]
 N_\ell(F)
 &=\{D+x\cup E^x_{\ell,r}:1\leq r\leq\ell-1\}\\
 &\quad\cup
   \{D+y\cup Z^y_{\ell,r}:0\leq r\leq\ell-1\}.
 \end{aligned}
\tag{3.2}
\]

The (x\bar y) and \(\bar x y\) signatures make the two shores disjoint;
within either shore, the (Z)-ports contain (z) while the (E)-ports do
not.  Therefore there are no hidden coincidences and

\[
 |P_\ell(F)|=|N_\ell(F)|=\ell+(\ell-1)=2\ell-1.
\tag{3.3}
\]

Formula (3.2) is the exact named leaf package switched by one gadget.  A
single gadget cannot switch an arbitrary proper subset of these ports:
all widths and all entries in their two triangular cones change together.

At the owner width (q), (3.2) specializes to the promised

\[
 q+(q-1)=2q-1=2d+1
\]

positive owners and the same number of negative owners.  This verifies the
claimed compact owner footprint exactly.

## 4. Incidence calculation and a sharp cross-width obstruction

Let

\[
 \pi_\ell({\bf e}_S)={\bf 1}_S\in\mathbb Z^k
\]

be the ground-coordinate incidence map on rank-(c+\ell) named values.
For a long-versus-short insertion pair with common core (B), the two full
cyclic decks give

\[
 \begin{aligned}
 \pi_\ell(g_\ell(B,\gamma))
 &=(n+1){\bf1}_B+\ell({\bf1}_{T_0}+e_z)
   -n{\bf1}_B-\ell{\bf1}_{T_0}\\
 &={\bf1}_B+\ell e_z.
 \end{aligned}
\tag{4.1}
\]

Consequently

\[
 \boxed{
 \pi_\ell(\Delta_\ell(F))
 =({\bf1}_{D+x}+\ell e_z)
  -({\bf1}_{D+y}+\ell e_z)
 =e_x-e_y,}
\tag{4.2}
\]

independently of \(\ell\).  This supplies a direct proof of (2.3) in the
audited note.

It also gives a genuine obstruction.  For any integer sum (L) of coupled
insertion switches, there is one vector (v\in\mathbb Z^k) such that

\[
 \boxed{
 \pi_\ell(L_\ell)=v
 \quad\text{for every protected width }\ell.}
\tag{4.3}
\]

Moreover \(\sum_i v_i=0), and the coefficient sum of every (L_\ell) is
zero.  Thus a proposed multi-width signed leave whose ground-coordinate
residue changes with the width is not in the coupled-insertion lattice,
even if every layer separately satisfies its usual scalar balance.

At width one, the triangular cones collapse and (3.1) becomes

\[
 \boxed{
 \Delta_1(F)
 ={f e}_{D+x+z}-{f e}_{D+y+z}.}
\tag{4.4}
\]

This is a genuine named unit difference between adjacent vertices of the
Johnson graph on rank-(c+1) sets.  Varying (D,z,x,y) therefore generates
the entire augmentation-zero lattice at width one, because that Johnson
graph is connected.  The strength of (4.4) does not propagate freely to
the owner width: the same generator necessarily carries the whole
(2q-1)-port package (3.2) there.

## 5. The exact nested insertion lattice

For a protected width set (W\subseteq\{1,\ldots,M-3\}), let

\[
 \mathcal A_W
 =\bigoplus_{\ell\in W}
   \mathbb Z^{\binom{[k]}{c+\ell}}.
\]

The algebraic output of the construction is precisely the image lattice

\[
 \boxed{
 \mathcal L_{\rm ins}(W)
 =\left\langle
   (\Delta_\ell(F))_{\ell\in W}:
   F\text{ is a legal coupled-insertion frame}
  \right\rangle_{\mathbb Z}
 \subseteq\mathcal A_W.}
\tag{5.1}
\]

This is an exact, non-asymptotic description: its columns are the explicit
vectors (2.1)--(3.2).  In particular:

* one gadget absorbs exactly (P(F)) against the reserve (N(F)), or the
  reverse package;
* a collection of gadgets can algebraically absorb a signed named leave
  (L) exactly when (L\in\mathcal L_{\rm ins}(W));
* actual positive absorption requires a representation of (L) by legal
  frames for which the component occurrences, common reserve, and all
  uncancelled named ports can be chosen disjointly.

The last bullet is stronger than lattice membership.  An integer
representation may reuse a named target, may cancel only formally, or may
use mutually incompatible cores/orders.  Theorem 2.1 proves neither this
positive realization nor the equality of (5.1) with any larger “full
lattice” defined only by rank and coordinate balances.

For owner-only data, membership in the projected lattice is concretely

\[
 L_q\in
 \left\langle
 \begin{aligned}
 &\sum_{r=0}^{q-1}{\bf e}_{D+x\cup Z^x_{q,r}}
 +\sum_{r=1}^{q-1}{\bf e}_{D+y\cup E^y_{q,r}}\\[-1mm]
 &-\sum_{r=1}^{q-1}{\bf e}_{D+x\cup E^x_{q,r}}
 -\sum_{r=0}^{q-1}{\bf e}_{D+y\cup Z^y_{q,r}}
 \end{aligned}
 \right\rangle_{\mathbb Z,F}.
\tag{5.2}
\]

Formula (5.2), rather than coordinate balance alone, is the currently
proved owner port lattice.

## 6. What named leaves are presently certified absorbable

The construction certifies the following classes, with increasing levels
of strength.

1. **One atomic package.**  The exact family (P_\ell(F)) at every
   protected width can be exchanged for (N_\ell(F)), simultaneously, for
   any legal frame (F).  The reverse exchange is equally valid.
2. **Disjoint unions of atomic packages.**  If legal frames have disjoint
   physical occurrences and their named exclusive supports are disjoint,
   the union of their switches is a positive absorber.
3. **Internally paired sums.**  More general sums are valid if every port
   not assigned to the external leave is paired with an identical named
   port in another gadget and the resulting physical construction remains
   disjoint.  Establishing such a pairing is exactly the missing
   port-embedding lemma.

In contrast, the present theorem does **not** certify absorption of:

* an arbitrary selection of at most (2q-1) owner values;
* an arbitrary owner leave with ground residue (e_x-e_y);
* independently prescribed leaves at different widths; or
* every element satisfying only augmentation and coordinate-incidence
  conditions (4.3).

Those conclusions would require a generation theorem for (5.1), followed
by a robust positive/disjoint realization theorem.

## 7. Coupled safe-order existence remains available

Coupling does not destroy the elementary avoidance argument.  Choose
\(\tau\) uniformly and the two insertion cuts uniformly and independently.
The short order is uniform on (T_0), and each inserted order is marginally
uniform on (T_0\cup\{z\}).  Hence, for forbidden ticket families
\(\mathcal F_{i,\ell}\) in the four component roles with toggle sizes
\(N_i\in\{n,n+1\}), the union bound

\[
 \sum_i\sum_\ell
 |\mathcal F_{i,\ell}|
 \frac{N_i}{\binom{N_i}{\ell}}<1
\tag{7.1}
\]

guarantees at least one coupled safe choice.  Independence of the four
orders is not needed for this bound.  This is an existence statement only;
it does not supply the robust expansion or multiplicity needed by a global
absorber embedding.

## 8. Bottom line

The compactness theorem survives audit.  Its exact local content is the
coherent current (3.1), with the explicit triangular port packages (3.2).
It gives a true named unit at width one and exactly (2d+1) owner ports per
state, but those are tied together across widths by the constant-incidence
law (4.3) and by the common cut geometry.  The next theorem must show that
the relevant global leave lies in the lattice (5.1) and admits a disjoint
positive realization; neither statement follows from the local count
alone.
