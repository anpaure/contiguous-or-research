# Independent audit of the conjugate-SCD hybrid and colored-component route

Date: 2026-08-01  
Lane: R / `F(a,z)` versus `F(z,a)`  
Verdict: **the four-shore colored-component theorem is valid after precise
overlay and topology qualifications; the unrestricted per-upper hybrid is
an exact undirected forest master, not a rooted/common-`M_0` theorem.**

## 1. Per-upper hybrid

Let `|Omega|=2m-1`.  For each upper colour `R`, choose one of the two
Johnson occurrences `e_0(R),e_1(R)` supplied by the conjugate forests.  The
chosen support is an upper-exact, lower-injective spanning Catalan path
forest exactly when:

1. each lower colour is used at most once;
2. each owner has degree at most two; and
3. every nonempty owner set `X` spans at most `|X|-1` chosen edges.

The last row is the graphic-matroid row.  Equivalently, after deleting the
old occurrences of a packet, simultaneously contract every remaining
forest component, retain loops and parallel edges, and require the inserted
edges to be graphic-independent.

This does not select a rooted chronology.  Directed indegree/outdegree and
cycle rows make a directed linear forest, but a mixed conjugate selection
still needs the residual Hall extension to one common predecessor matching
`M_0`.

The raw owner-edge overlay is also insufficient.  Exact upper-preserving
closed toggles are binary kernel vectors of the owner-incidence plus
used-lower occurrence matrix.  Inclusion-minimal nonzero binary kernels
are only candidate packet atoms.  Ordinary integer/matroid circuits may
have nonunit or mixed-sign coefficients; a zero column is a singleton
no-op; and a legal packet may be a union of several disjoint atoms.

## 2. Endpoint-hole projection

For a selected forest `F`, define the coordinate free-slot vector

\[
 E_t(F)=\sum_T(2-d_F(T))\mathbf1_{t\in T}.
\]

An isolated owner contributes two slots.  If `H_t(F)` is the number of
unused lower colours containing `t`, then every upper-paired switch obeys

\[
                         \Delta E_t=\Delta H_t,
 \qquad E_t-H_t=2\operatorname{Cat}_{m-1}.                  \tag{2.1}
\]

Thus the positive two-stratum cocycle is a correct necessary coordinate
projection.  It neither supplies a binary conjugate-column solution nor a
rooted source matching.

## 3. Exact four-shore component cube

Now retain the rooted `M_0` relation in each phase.  Close every directed
path by a typed dummy carrying its unused lower colour, terminal owner,
source owner, and a private upper label.  Pair red dummies with their
coordinate-swapped blue dummies by the same upper label.  Each augmented
phase is then perfect on four shores: lower colours, typed tails, typed
heads, and true-plus-dummy upper colours.

Build the **two-copy colored incidence overlay**.  Coincident physical
atoms remain distinct red and blue copies.  Every resource joins its unique
red and blue atoms.  On a resource edge the selection bits sum to one, so
this equality propagates across an overlay component.  Therefore every
perfect factor supported on the two phases is obtained by choosing one
whole colour per connected component, and different components switch
independently.

For a dummy `d`, put

\[
 w_t(d)=\mathbf1_{t\in\operatorname{source}(d)}
        -\mathbf1_{t\in\operatorname{hole}(d)}.
\]

The red-to-blue component signature is

\[
 \Delta\kappa_t(\Gamma)
 =\sum_{d\in D^+\cap\Gamma}w_t(d)
  -\sum_{d\in D^-\cap\Gamma}w_t(d),
 \qquad \kappa_t=S_t-H_t+1.                                \tag{3.1}
\]

Equivariant dummy pairing makes every dummy-containing component invariant
under colour swap composed with `(a z)`.  Hence

\[
 \boxed{\Delta\kappa_a(\Gamma)+\Delta\kappa_z(\Gamma)=0},
 \qquad
 \Delta\kappa_q(\Gamma)=0\quad(q\notin\{a,z\}).             \tag{3.2}
\]

For component bits `x_i`, let
`D=sum_i x_i Delta kappa_z(Gamma_i)`.  The two special cuts hold exactly
when

\[
                 -\kappa_z(F^- )\le D\le\kappa_a(F^-).       \tag{3.3}
\]

In particular, `kappa_a+kappa_z<0` is an unconditional obstruction before
topology.

## 4. Exact topology qualification

Every selected augmented factor is a directed permutation.  Removing its
dummies gives a directed linear forest if and only if every permutation
cycle contains a selected dummy.

The corresponding lazy clause is formed only from a phase-labelled,
component-consistent all-real directed cycle.  If a candidate demands red
and blue atoms from the same overlay component, no component assignment
can realize it and it is omitted.  Coincident physical arcs remain colored
copies.  For a realizable cycle `Q`, at least one phase-sensitive component
must choose the opposite phase.  These clauses are necessary and
sufficient.

## 5. Consequence for the saved SCD fibres

The authenticated `m=4,...,9` bases have invariant sums

\[
                     -1,-12,-41,-163,-639,-2468.
\]

Their overlays contain respectively `4,8,28,80,185,489` nonzero transfer
components, almost all individually forest-safe, and abundant unit
transfers.  Nevertheless (3.2) fixes the negative sum, so no component
subset can pass both special connector cuts.

This closes the proposed neutral conjugate route on those fibres.  A live
construction must do at least one of the following:

* start from a base with `kappa_a+kappa_z>=0`;
* add a literally audited packet with positive total gain
  `Delta(kappa_a+kappa_z)>0`; or
* leave the two-phase four-shore cube, change the dummy/source basis, and
  pay the full common-`M_0`, lower, owner, and graphic rows.

For the standard phase grammar, if `c=Cat_(m-1)`,
`I_m=Cat_m-2c`, and `D_long` is the number of reversed long-`D`
choices, then

\[
 \kappa_z=1-I_m,qquad
 \kappa_a=c-D_{\rm long}+1.
\]

Consequently any external actuator bank must satisfy the sharp necessary
total-current row

\[
 \sum_P\Delta(\kappa_a+kappa_z)(P)
       \ge I_m-c+D_{\rm long}-2.                              \tag{5.1}
\]

Only after (5.1) is paid can the neutral component subset-sum (3.3)
redistribute current.  The selected augmented permutation must then satisfy
the component-consistent cycle-hit clauses of Section 4; total current and
graphic feasibility are independent obligations.

The paired short ear supplies only one `z`-cut unit after its displaced
ordinary provider is restored.  Neutral conjugate components can
redistribute that current but cannot create the missing total current.

Residence, deeper shadows, and common-cap compilation are not consequences
of this central owner/palette theorem.
