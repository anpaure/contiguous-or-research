# Conjugate SCD forests reduce two-stratum repair to a coloured hybrid forest

Date: 2026-08-01  
Lane: R / `F(a,z)` versus `F(z,a)` / external endpoint-current actuators  
Status: exact terminal hybrid formulation, exact switch and graphic
criteria, and exact signed-gain classification.  For the equivariantly
closed conjugate-component cube, the sharper sum-cocycle theorem cited in
Section 7 proves a neutral-switch no-go on the saved `m=4,...,9` fibres.
No all-dimensional positive-gain packet supply is proved.

## 0. Outcome

Let `F_0=F(a,z)` be an upper-exact, lower-injective Catalan owner forest,
and let `F_1=F(z,a)` be its coordinate-conjugate forest on the same physical
owner layer.  For every upper colour `R`, write `e_i(R)` for its unique
edge in `F_i`.

The correct hybrid operation is **not** to toggle arbitrary connected
components of `F_0 triangle F_1`.  Such a component need not be alternating
at owner vertices, need not contain both occurrences of each upper colour,
and may create a cycle.  The exact choice is one bit per upper colour,
followed simultaneously by lower, owner-degree and graphic rows.

This gives a prospective escape from the fixed-`M_0` `z` cut because it may
change the lower-owner basis and the endpoint current macroscopically.  The
two-stratum cocycle theorem proves that a compatible endpoint/hole degree
vector exists abstractly.  It does not prove that this vector lies in the
integral column span of the particular conjugate pair.

## 1. The exact two-factor hybrid master

Let `|Omega|=2m-1`, let `V=binom(Omega,m)` be the owner set, and let
`mathcal U` and `mathcal L`
be the rank-`(m+1)` and rank-`(m-1)` colour layers.  For `i=0,1` and
`R in mathcal U`, let

\[
 e_i(R)=\{T_i(R),T'_i(R)\},\qquad
 \ell_i(R)=T_i(R)\cap T'_i(R).                              \tag{1.1}
\]

For `x_R in {0,1}`, put

\[
 E(x)=\{e_{x_R}(R):R\in\mathcal U\}.                         \tag{1.2}
\]

### Theorem 1.1 (necessary and sufficient terminal rows)

The set `E(x)` is an upper-exact, lower-injective Catalan path forest if
and only if

\[
\begin{aligned}
 &\sum_{R:\ell_{x_R}(R)=K}1\le1
       &&(K\in\mathcal L),                                    &&\tag{1.3a}\\
 &d_{E(x)}(T)\le2
       &&(T\in V),                                             &&\tag{1.3b}\\
 &|E(x)[X]|\le |X|-1
       &&(\varnothing\ne X\subseteq V).                       &&\tag{1.3c}
\end{aligned}
\]

When these rows hold, the forest has exactly `Cat_m` components.

#### Proof

Equation (1.2) chooses exactly one occurrence of every upper colour, so
upper exactness is automatic.  Rows (1.3a) and (1.3b) are precisely lower
injection and physical degree two.  Row (1.3c) is the graphic-matroid
criterion.  Finally `|E(x)|=binom(2m-1,m+1)=|V|-Cat_m`, so an acyclic
spanning graph has exactly `Cat_m` components.  The converse is immediate.
\(\square\)

For a rooted literal chronology, replace (1.3b) by separate combined
indegree/outdegree rows on the directed occurrences and replace (1.3c) by
a strict order or directed cycle cuts.  Because `F_0` and `F_1` use
conjugate lower-owner maps, this is no longer the frozen-`M_0` connector
model.

## 2. Exact packet and graphic criterion

For `A subseteq mathcal U`, toggling the corresponding upper occurrences
means

\[
 F_0\longmapsto
 F_A=F_0-\{e_0(R):R\in A\}
          +\{e_1(R):R\in A\}.                              \tag{2.1}
\]

The upper palette is preserved literally because every removed edge is
paired with the same named upper colour.

### Theorem 2.1 (no-new-cycle test)

Assume the lower and owner rows (1.3a)--(1.3b) hold for `F_A`.  Put

\[
 F^-=F_0-\{e_0(R):R\in A\}.                                  \tag{2.2}
\]

Then `F_A` is a forest if and only if the inserted blue edges are
independent in the graphic matroid of the multigraph obtained by
simultaneously contracting every component of `F^-` (retaining loops and
parallel edges).

#### Proof

The graph `F^-` is a subforest.  Adding an edge creates a cycle exactly
when its contracted endpoints already lie in the same component created by
previous additions.  This is precisely graphic independence in the
contracted multigraph.  \(\square\)

Thus even a degree-preserving whole packet can split and merge components
or create a cycle.  Palette transparency and topology are distinct rows.

## 3. What the coloured symmetric difference does provide

Colour edges of `F_0-F_1` red and edges of `F_1-F_0` blue.  At an owner
`T`, let `d_0(T),d_1(T)` be the two coloured degrees.

### Lemma 3.1 (alternating decomposition boundary)

The coloured symmetric difference is a disjoint union of alternating
circuits only if

\[
                         d_0(T)=d_1(T)\quad(T\in V).             \tag{3.1}
\]

If (3.1) holds, pairing red and blue half-edges at every owner decomposes
it into alternating circuits.  Without (3.1), the same pairing decomposes
it into alternating circuits **and** open alternating trails; the unmatched
ends of the latter carry the owner-degree current.

#### Proof

Every alternating circuit uses equally many red and blue incidences at
each visited vertex, proving necessity.  Under (3.1), pair the two colour
classes locally and follow pairs until they close.  With imbalance, the
unpaired half-edges are exactly trail ends.  \(\square\)

This ordinary decomposition still does **not** preserve upper colours.
A proof-safe packet must additionally be closed under the involution

\[
                         e_0(R)\longleftrightarrow e_1(R).       \tag{3.2}
\]

Therefore every genuine closed `0/1` packet is a kernel vector of the
occurrence matrix whose columns are

\[
 \Delta_R=
  (\chi_{\partial e_1(R)}-\chi_{\partial e_0(R)},
   e_{\ell_1(R)}-e_{\ell_0(R)}).                              \tag{3.3}
\]

Owner-balanced, hole-preserving `0/1` packets satisfy

\[
                         \sum_{R\in A}\Delta_R=0.               \tag{3.4}
\]

Open trails correspond to a prescribed nonzero boundary in (3.4).
Inclusion-minimal nonzero **feasible binary kernels** are candidate packet
atoms, still subject to the graphic and directed rows.  General closed
packets can be unions of several such atoms and need not themselves be
circuits.  An ordinary integer/matroid circuit may use nonunit or
mixed-sign coefficients and therefore need not be a physical C6/C8/long
switch; a zero column can even give a singleton no-op.  Connected
components of the raw edge overlay are not enough either.

## 4. Endpoint--hole cocycle under an upper-paired switch

Let `H(x)` be the unused lower family of a feasible hybrid.  Define its
free endpoint-slot degree vector coordinatewise by

\[
 E_t(x)=\sum_{T\in V}(2-d_{E(x)}(T))\mathbf1_{t\in T};          \tag{4.0}
\]

thus an isolated owner contributes two slots.  For one edge,
coordinatewise,

\[
 \chi_T+\chi_{T'}=\chi_{T\cap T'}+\chi_{T\cup T'}.              \tag{4.1}
\]

The upper term cancels between `e_0(R)` and `e_1(R)`.  Consequently every
upper-paired switch satisfies

\[
                         \Delta E=\Delta H.                     \tag{4.2}
\]

Equivalently, it preserves

\[
                         E-H=2\operatorname {Cat}_{m-1}\mathbf1. \tag{4.3}
\]

This is why swapped strata can repair the old one-stratum degree
obstruction: endpoint and hole currents move together.  It is also why
the cocycle alone cannot select a physical hybrid.

The exact remaining integral column condition for a desired boundary `b`
in the owner-incidence plus **used-lower occurrence space** is

\[
                         \sum_R x_R\Delta_R=b,qquad x_R\in\{0,1\}, \tag{4.4}
\]

together with (1.3).  The free-endpoint/hole coordinate boundary is a
signed coordinate projection of this equation, not the vector `b` itself.
At the fractional level every weight vector
`lambda` gives the necessary Farkas inequality

\[
 \lambda\cdot b\le
       \sum_R\max\{0,\lambda\cdot\Delta_R\}.                   \tag{4.5}
\]

The two-stratum degree theorem proves feasibility in the full abstract
packet/hole bank, not (4.4) for these particular conjugate columns.

## 5. Directed endpoint-current gain

For a directed packet `P`, let `tau_z(P)` be the number of selected lower
tails containing `z`, and let `eta_z(P)` be the number of selected physical
heads containing `z`.  Relative to the old support,

\[
 \Delta H_z=-\Delta\tau_z,qquad
 \Delta S_z=-\Delta\eta_z.                                    \tag{5.1}
\]

Hence its exact signed connector gain is

\[
 \boxed{g_z(P)=\Delta\kappa_z
       =\Delta\tau_z-\Delta\eta_z.}                            \tag{5.2}
\]

This classifies prospective tight-augmenter/C6/C8 actuators.

* A closed packet preserving both tail and head multisets has `g_z=0`.
* A packet using one additional `z`-tail and neutral on heads has gain one.
* A packet releasing one used `z`-head and neutral on tails has gain one.
* Gain two means exactly `Delta tau_z-Delta eta_z=2`.  The balanced
  one-plus-one signature (one additional `z`-tail and one fewer used
  `z`-head) is the smallest mixed mechanism, but two tail services or two
  head releases are algebraically possible and must be judged by their
  full resource ledgers.

Thus an ordinary closed alternating C6/C8 cannot repair the residual cut
merely by being a circuit.  A closed conjugate component can have positive
gain in `z`, but Section 7 shows that it then loses exactly the same amount
in `a`.  Positive **total two-coordinate** gain requires a packet outside
that neutral component cube: equivalently an external tail/head/provider
boundary, a changed dummy pairing, or a different base factor.  Raw menu
counts do not prove supply; the tail, head, upper, lower and graphic
resources must be disjoint in the final simultaneous packet.

The audited short paired-ear layer illustrates the distinction.  Its
first-stage provider rethread gives one net unit; its second D-short
relocation gives zero after restoring the displaced `aU` service.  The
full short bank therefore leaves `I_m-1-Cat_(m-1)` units for `m>=6`.

## 6. Two-stratum prospective theorem and exact remaining gate

The abstract swapped-stratum theorem supplies, for sufficiently large
`m`, a simple lower-hole family and endpoint degree vector satisfying
(4.3), and a resource-disjoint packet bank.  A phase-compatible planted
version supplies an exact partial incidence matching.  It still requires
the residual Hall row extending that partial matching to one owner basis.

For the direct conjugate-forest route, the weakest exact missing theorem
at the undirected central level is:

> There exists `x in {0,1}^{mathcal U}` satisfying the lower, owner and
> graphic rows (1.3), whose endpoint/hole boundary lies in the feasible
> two-stratum fibre, and whose directed path components admit the required
> source orientation or a positive-gain external trail bank.

This avoids requiring either frozen forest itself to be connected and is
strictly stronger than the coordinate cocycle; no converse implication to
either frozen-forest problem is asserted.  It is not yet a rooted/common-`M_0`
master: after the hybrid is selected, its directed source/head bank still
needs the residual Hall extension to one owner basis.  A proof may use long
alternating trails; bounded C6/C8 packets are not required.  Residence,
deeper shadows and common-cap compilation remain outside this central
owner/palette theorem.

## 7. Exact conjugate-component specialization

There is one important specialization in which the component language is
fully honest.  Close every directed path of both forests by a typed dummy
carrying its missing lower colour, terminal owner, source owner and a
private upper label.  The augmented red and blue systems are then perfect
on four shores.  Connected components of their four-shore incidence
symmetric difference switch independently.

With equivariant dummy labels, every such component `Gamma` obeys

\[
              \Delta\kappa_a(\Gamma)+\Delta\kappa_z(\Gamma)=0. \tag{7.1}
\]

Hence these neutral switches transfer slack between `a` and `z` but never
create total slack.  The exact proof and authenticated `m=4,...,9` census
are in

`MATH_THEOREM_TWO_SWAPPED_SCD_COLORED_COMPONENT_TRANSFER_AND_SUM_COCYCLE_NOGO_20260801.md`.

All six saved base fibres have negative `kappa_a+kappa_z`; therefore no
subset of their neutral components can make both directed connector cuts
nonnegative, even before graphic cuts.  The same theorem gives the exact
topology row: after dummy augmentation every hybrid is a directed
permutation, and deleting dummies is acyclic iff every permutation cycle
contains a dummy.  An all-real cycle produces one lazy phase-flip clause.

This does not contradict the positive undirected two-stratum degree
theorem.  It separates its missing directed ingredient sharply: a new base
with nonnegative total slack or a packet with positive
`Delta kappa_a+Delta kappa_z` is necessary.  More neutral conjugate
switching cannot close the lane.
