# Swapped SCD phase components only transfer endpoint current between the two distinguished coordinates

Date: 2026-08-01  
Lane: Thread D / flexible SCD detachment / paired-ear and connector repair  
Status: **exact correction to the paired-palette ledger, an exact
component-selection theorem for the coloured symmetric difference, and an
all-dimensional two-coordinate obstruction for swap-closed packets when
`m>=6`.  The authenticated `m=4,...,8` forests are audited component by
component.  No obstruction to a non-swap-closed, three-parent, or
basis-changing rethread is claimed.**

## 1. Why the apparent two-unit paired packet has only one proved unit

Write

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I=\operatorname {Cat}_m-2c.
\]

For a short chain `S<L=S+x`, put

\[
 A=aS,\qquad B=zS,\qquad C=L.
\]

The exact paired-palette packet consumes the short `azL` provider and the
direct intact `zU` provider and occupies one ordinary missing-`aW` target
row.  In rooted form it inserts

\[
 B\longrightarrow C\longrightarrow P(U),
 \qquad A\longrightarrow Q(V),                    \tag{1.1}
\]

with upper colours `azL,zU,aW`.  It is a three-edge replacement for two
provider rows plus one target row.

It is tempting to compare (1.1) with three old *main* edges and charge both

* the newly used `z`-lower `B`, and
* the released `z`-head of the direct `zU` provider.

That comparison omits the auxiliary edge belonging to the old ordinary
`aW` target option.  Every ordinary option has one auxiliary lower tail
containing `z`.  Replacing the complete ordinary target row by (1.1)
replaces that old `z`-tail by `B`; it does not create an additional
`z`-hole exemption.  The only new marginal effect is that the direct
`zU` provider tail `P(U)` is replaced by `C->P(U)`, so one short root `C`
ceases to be a hole of type `M_0(C)=C+z`.  Equivalently,

\[
 H_z=c+I,\qquad t_z=c-r,\qquad S_z=c+r             \tag{1.2}
\]

after `r` pair packets.  Hence

\[
                         \boxed{\Delta\kappa_z=1}  \tag{1.3}
\]

per packet, where `kappa_z=S_z-H_z+1`.

Keeping the old auxiliary edge while moving only its main edge would be a
different three-provider rethread.  It is not implied by the paired-ear
identity and must be audited as a new physical packet, including its third
provider, lower-tail, head and graphic rows.  Thus it cannot be used to
upgrade (1.3) for the present grammar.

Consequently `r<=c` leaves the exact residual cut

\[
 I-1-c={m-5\over m+1}c-1>0\qquad(m\ge6).           \tag{1.4}
\]

This is the scoped paired-bank no-go.  The rest of this note asks whether
an entire component of the opposite distinguished-coordinate phase can do
better.

## 2. Coloured symmetric-difference components

Let `F=F(a,z)` be any directed, upper-exact, lower-injective SCD phase
forest on the rank-`m` owners, and let `pi` exchange `a` and `z`.  Put

\[
                         F^\pi=\pi F=F(z,a).        \tag{2.1}
\]

Both forests are literal and have the same complete upper palette.  Colour
the arcs of `F-F^pi` red and those of `F^pi-F` blue.  Merge a connected
component with its `pi`-image if necessary; call the resulting object a
**swap-closed component orbit** `K`.  Write `R_K,B_K` for its red and blue
arcs.

For an upper colour `R`, lower colour `L`, and physical owner `v`, define

\[
\begin{aligned}
 \delta^U_K(R)&=|\{e\in B_K:\cup e=R\}|-
                 |\{e\in R_K:\cup e=R\}|,\\
 \delta^L_K(L)&=|\{e\in B_K:\cap e=L\}|-
                 |\{e\in R_K:\cap e=L\}|,\\
 \delta^S_K(q)&=\sum_{v\ni q}
  \bigl({\bf1}_{d^-_{F^\pi}(v)=0}-
        {\bf1}_{d^-_F(v)=0}\bigr),                 \tag{2.2}
\end{aligned}
\]

where the last sum is over owners touched by `K`; isolated owners count as
sources.  Since a red used lower removed from the support becomes a hole,

\[
 \delta^H_K(q)=
 |\{e\in R_K:q\in\cap e\}|-
 |\{e\in B_K:q\in\cap e\}|.                       \tag{2.3}
\]

The signed endpoint current of `K` is therefore

\[
             \boxed{\delta\kappa_K(q)=
                    \delta^S_K(q)-\delta^H_K(q).}  \tag{2.4}
\]

There is a more local equivalent formula.  For a rooted physical arc `e`,
let `ell(e)` be its lower intersection and let `h(e)` be its physical head
owner.  Define

\[
 j_q(e)={\bf1}_{q\in\ell(e)}-{\bf1}_{q\in h(e)}.           \tag{2.4a}
\]

Inserting `e` removes one lower hole when `q in ell(e)` and consumes one
source ticket when `q in h(e)`.  Therefore every switch block satisfies

\[
 \boxed{\delta\kappa_K(q)=
   \sum_{e\in B_K}j_q(e)-\sum_{e\in R_K}j_q(e).}   \tag{2.4b}
\]

Formula (2.4b) remains valid when old and new arcs share vertices.  It is
the clean way to prevent a released head and a replaced lower row from
being counted twice.

### Theorem 2.1 (exact component-toggle criterion)

Starting from `F`, choose component orbits by binary variables `y_K` and
replace their red arcs by their blue arcs.  The result is an upper-exact,
lower-injective directed linear forest if and only if all four following
systems hold.

1. **Upper palette:**

   \[
             \sum_K y_K\delta^U_K(R)=0
             \quad\text{for every upper colour }R.           \tag{2.5}
   \]

2. **Lower injection:** for every lower colour `L`,

   \[
       0\le {\bf1}_{L\text{ used by }F}
          +\sum_Ky_K\delta^L_K(L)\le1.             \tag{2.6}
   \]

3. **Rooted degree:** every owner has selected indegree and outdegree at
   most one.
4. **Graphic row:** after the red deletions, the selected blue arcs are
   independent in the contracted graphic matroid; equivalently the final
   support has no directed cycle.

For every coordinate `q`, its connector current changes exactly by

\[
                 \kappa_q(F_y)=\kappa_q(F)+
                    \sum_Ky_K\delta\kappa_K(q).     \tag{2.7}
\]

#### Proof

Equations (2.5) and (2.6) are respectively the exact signed upper and lower
incidence ledgers.  The red/blue component orbits contain every changed
arc, so the unchanged background contributes identically on both sides.
The degree and graphic rows are the exact characterization of a directed
linear forest once palettes are fixed.  Finally (2.7) is the definition of
source and hole current, summed over the vertex-disjoint changed supports.
No marginal-Hall approximation is used.  \(\square\)

This is the smallest proof-safe master for the swap lane.  Individual
component feasibility does not remove (2.5), and individual acyclicity
does not remove the joint contracted graphic cuts.

## 3. A swap-closed component creates no two-coordinate current

### Lemma 3.1 (current transfer, not current creation)

For every swap-closed component orbit,

\[
 \delta\kappa_K(q)=0\quad(q\notin\{a,z\}),
 \qquad
 \boxed{\delta\kappa_K(a)+\delta\kappa_K(z)=0.}    \tag{3.1}
\]

#### Proof

The involution `pi` fixes every ordinary coordinate and preserves the
pointwise weight

\[
                         {\bf1}_{a\in X}+{\bf1}_{z\in X}.     \tag{3.2}
\]

A swap-closed orbit has `B_K=pi(R_K)`.  Formula (2.4a) gives

\[
 j_q(\pi e)=j_q(e)\quad(q\notin\{a,z\}),
 \qquad
 j_a(\pi e)+j_z(\pi e)=j_a(e)+j_z(e).              \tag{3.3}
\]

Sum (3.3) over the red arcs and use (2.4b).  This proves (3.1) without any
assumption that the arcs have disjoint endpoint tickets.  \(\square\)

Thus a component with positive `z` current pays for it with the same
negative `a` current.  The `2x2` endpoint accounting is not an absorber;
it is a current transporter.

## 4. The standard SCD phase has insufficient `a+z` current

Let `D_long` be the number of selected reversed-D `a`-options whose
provider is a long chain.  Equivalently, if `A_C` is the aligned-long count
and `p` the short-D count, then

\[
                         D_{\rm long}=E-A_C-p.       \tag{4.0}
\]

The exact ledger is

\[
 \boxed{\kappa_z=1-I,\qquad
 \kappa_a=c-D_{\rm long}+1.}                        \tag{4.1}
\]

Indeed, the `a`-containing hole count is `E-A_C`, while the number of
short holes whose matching owner adds `a` is `c-p`.  Thus

\[
 S_a=2c-(c-p)=c+p,
 \qquad
 \kappa_a=S_a-(E-A_C)+1=c-D_{\rm long}+1.           \tag{4.2}
\]

A swap-closed selection can only transfer some integer current `k` from
`a` to `z`.  Passing both coordinate cuts therefore requires the sharp
interval

\[
 \boxed{I-1\le k\le c-D_{\rm long}+1.}             \tag{4.3}
\]

Equivalently, it requires

\[
                         D_{\rm long}\le c-I+2.     \tag{4.4}
\]

But `D_long>=0` and `I>c+2` for every `m>=6`, so (4.4) is impossible.
Equivalently,

\[
 \kappa_a+\kappa_z=c-D_{\rm long}-I+2<0.           \tag{4.5}
\]

Combining (3.1) and (4.3) proves:

### Corollary 4.1 (swap-component no-go)

For `m>=6`, no union of swap-closed components from
`F(a,z) triangle F(z,a)` can make both the `a`- and `z`-coordinate
connector Hall rows nonnegative, even if every palette, degree and graphic
row is otherwise feasible.

The conclusion is stronger than the one-unit paired-bank count but has a
different scope.  It rules out only the two-phase coordinate-swap lattice.
A packet involving a third parent, a non-swap-closed component, or a
basis-changing lower/source actuator can change the sum in (4.5) and is
not excluded.

There is no conflict with
`MATH_THEOREM_TWO_STRATUM_PACKET_COORDINATE_COCYCLE_FEASIBILITY_20260801.md`.
That construction changes the lower/provider basis through two active
strata and a Kneser circulation.  Its packets are not unions of columns
`new=pi(old)` inside one `F triangle pi F` support, so Lemma 3.1 does not
apply to them.

## 5. Exact finite audit

`scratch/audit_threadD_scd_swapped_phase_components_20260801.py` performs
a solver-free replay on the authenticated flexible-detachment witnesses.
It materializes both oriented physical forests, includes isolated owners
as source and terminal tickets, decomposes the complete directed symmetric
difference, and independently toggles every component.

For `m=4,...,8` it finds respectively

\[
                         4,7,15,25,49              \tag{5.1}
\]

connected components.  Every one is already swap-closed and every one has
current vector supported only on `a,z`, with zero coordinate sum as in
(3.1).  The numbers of components which individually preserve the upper
palette, lower injection and graphic row and have positive `z` current are

\[
                         2,1,4,10,21.               \tag{5.2}
\]

Their positive gains range from one to four, but every gain `k` is exactly
the transfer `(-k,+k)` on `(a,z)`.  The frozen current pairs are

\[
 (\kappa_a,\kappa_z)=
 (2,-3),(1,-13),(6,-47),(1,-164),(-68,-571).        \tag{5.3}
\]

Hence none of the five frozen swap lattices can satisfy both coordinate
cuts.  This finite table is an audit of the theorem, not its proof.

## 6. Surviving repair gate

The exact next actuator must escape at least one hypothesis of Lemma 3.1.
Equivalently it must supply **positive total current**

\[
                         \Delta(\kappa_a+\kappa_z)>0,          \tag{6.1}
\]

while still satisfying the signed upper/lower rows (2.5)--(2.6), rooted
degree, and graphic independence.  A third-parent palette rethread is the
smallest live typed possibility.  Recounting two tickets of the same
paired target/provider row is not.

More sharply, for this base forest any external selected packet bank
`mathcal P` must satisfy the necessary joint row

\[
 \boxed{\sum_{P\in\mathcal P}
   \bigl(\Delta\kappa_a(P)+\Delta\kappa_z(P)\bigr)
   \ge I-c+D_{\rm long}-2.}                         \tag{6.2}
\]

After (6.2) is paid, the neutral swapped components may distribute the
resulting total current between `a` and `z`, subject to the exact interval
(4.3), palette rows, rooted capacities and graphic cuts.  Thus (6.2), not
raw packet supply or a one-coordinate gain count, is the correct first row
of a joint external-packet plus conjugate-component master.
