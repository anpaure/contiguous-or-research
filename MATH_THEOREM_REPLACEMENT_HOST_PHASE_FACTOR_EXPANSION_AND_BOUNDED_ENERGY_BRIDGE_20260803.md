# Replacement-host phase factors, bounded collision energy, and the pull-clock bridge

**Date:** 2026-08-03

**Status:** proof-complete abstract factor theorems and exact scope audit.  This
note strengthens the replacement-host route in three ways: it gives a
complete phase-separated Hall/Haxell/LLL factor criterion after the actual
boundary is fixed; it proves that bounded total collision energy leaves only
a bounded common exceptional shore; and it proves a bare factorization of the
odd-central owner incidence graph into rank-adjacent owner allocations.  It
does **not** construct a protected replacement host, a bounded boundary, a
fixed-host pull-clock pushforward, or an integral chronology.  No fixed `P*`
instance or computational artifact is changed.

Throughout, `phi in {0,1}` is the s7 owner phase.  A local B5 materialization
mode, when present, is a separate axis and is fixed before this note applies.

## 1. Quantifier-safe replacement packet

Let `S` be a set of ticket roles.  For the finite K17 gate, `|S|=1748`.
A **fixed replacement packet** consists of the following data, chosen in the
displayed order.

1. Choose one new physical target table `H`, one origin parent, one exact
   outer materialization `mu`, and one admissible common-basis/owner parameter
   `sigma`.  The parameter may induce different phase owner maps
   `Omega^0_sigma,Omega^1_sigma`; the special case of one common owner map is
   allowed.
2. Choose a boundary role set `A subseteq S`, the actual phase boundary
   witnesses `W_0(Y),W_1(theta Y)`, and a complete exterior-fixed boundary
   conjugacy `theta`.  Every owner pin, endpoint aperture, source, cell,
   address, directed history, reset, residence, supplier, upper/common-cap
   and non-evicted compiler value read by the exterior is in the literal
   boundary closure.  The boundary is called bounded only when this closure
   has uniformly bounded literal serialization size.
3. Delete every candidate meeting its phase boundary.  For each bulk role
   `s in S^o:=S-A` and phase `phi`, form the finite set

   \[
                 {\cal P}_{\phi,s}(H,\mu,\sigma,Y)          \tag{1.1}
   \]

   of complete occurrence-labelled rank-adjacent tickets.  A candidate
   includes both physical endpoint hosts, their actual inverse sources, all
   five physical cells, actual addresses, histories, flags and every other
   capacity-one resource used by simultaneous composition.
4. Join two candidates of different roles in the phase conflict graph
   `Gamma_phi` exactly when they cannot coexist.  Assume the explicitly
   audited **composition closure**: every independent transversal of
   `Gamma_phi`, together with `W_phi`, is a valid phase-local private ticket
   factor.

The host, `mu`, `sigma`, local mode and actual boundary are therefore fixed
before any candidate distribution or matching is chosen.  A convex
combination over different hosts, owner allocations or boundary values is
not a point of this packet.

The two bulk transversals are chosen independently.  They need not pair or
carry corresponding tickets across phases.  Their identities can be erased
only under the already-proved universal interior/exterior factorization; the
only cross-phase object is the complete boundary transported by `theta`.

### Lemma 1.1 (identity-core inverse decoupling)

Suppose the exact outer matching has a disjoint decomposition

\[
                     \mu=\operatorname{id}_{K}
                         \mathbin{\dot\cup}\mu_{\rm red}, \tag{1.2}
\]

all ticket endpoint hosts lie in `K`, and every movable short/free inverse
choice lies in the disjoint reduced matching `mu_red`.  Then distinct
endpoint hosts have distinct actual sources, every such source pin is
`h -> h`, and changing either phase-local ticket factor neither deletes nor
redirects an edge of `mu_red`.

#### Proof

For `h in K`, (1.2) gives `mu^(-1)(h)=h`; injectivity of the identity gives
source privacy.  The two matching summands have disjoint source and receiver
shores, so endpoint selection inside `K` does not touch `mu_red`.  \(\square\)

Without (1.2), actual inverse sources remain separate resources in every
candidate footprint; receiver-host privacy is not a substitute for inverse
authentication.

## 2. What bare owner allocation does and does not cost

Put `k=2r-1`, `r>=2`, and let `G_r` be the middle incidence graph

\[
 L={ [2r-1]\choose r-1},\qquad
 R={ [2r-1]\choose r},\qquad
 AB\in E(G_r)\Longleftrightarrow A\subset B.          \tag{2.1}
\]

### Theorem 2.1 (complete bare owner factorization)

The graph `G_r` is the disjoint union of `r` perfect matchings.  In
particular, it supplies `r` exact rank-adjacent one-copy owner allocations.
For K17 this gives nine bare allocations on the 24,310 roots and owners.

#### Proof

Both shores have the same size.  Every `(r-1)`-set has `r` rank-`r`
supersets, and every rank-`r` set contains `r` `(r-1)`-sets, so `G_r` is
`r`-regular.  For `X subseteq L`, edge counting gives

\[
                  r|X|\le r|N(X)|.
\]

Hall supplies a perfect matching.  Removing it leaves an `(r-1)`-regular
balanced bipartite graph.  Repeating proves the decomposition.  \(\square\)

This strengthens the bare owner-existence row but does not construct the
replacement packet of Section 1.  Protected common-basis representation
edges, boundary pins, phase-local ticket positivity, state arcs and
chronology can delete owner incidences.  After those deletions, extension is
again governed by the residual Hall family; Theorem 2.1 does not make the
chosen packet admissible.

## 3. Exact one-shore criterion

Suppose one injective predecessor assignment is fixed in each phase and the
completed candidates form a **right-private atlas**: candidates belonging to
distinct roles and distinct successor hosts have disjoint complete resource
footprints and have no other relational conflict.  Equivalently, inside this
atlas every residual incompatibility between distinct roles is exactly
equality of the successor host.  Let `G_phi` be the resulting
role--successor graph.

### Theorem 3.1 (phase-separated Hall factor)

The packet has a complete private factor in both phases if and only if

\[
       |N_{G_\phi}(X)|\ge |X|
       \quad(X\subseteq S^o,\ \phi=0,1).               \tag{3.1}
\]

The phase matchings may be different.

#### Proof

A private factor uses distinct successors and hence gives a matching
saturating `S^o`; Hall proves necessity.  Conversely, take a saturating
matching in each phase.  Injective fixed predecessors, distinct matched
successors and right-privacy make the complete selected footprints
disjoint.  They already avoid the fixed boundary.  Apply the argument
separately in the two phases and adjoin `W_phi`.  \(\square\)

If

\[
 h_\phi=|S^o|-\nu(G_\phi)
       =\max_X\bigl(|X|-|N_{G_\phi}(X)|\bigr),          \tag{3.2}
\]

then maximum matchings leave sets `U_phi` of sizes `h_phi` unmatched.  The
common deletion `U_0 union U_1` has size at most `h_0+h_1` and leaves both
phase graphs saturable.  Turning that deletion into a boundary still
requires one jointly valid pair of phase boundary completions for the whole
deleted set, with conjugate complete closures jointly disjoint from the
realized bulk.  Per-role completions certified in isolation do not suffice.

The exact Hall family is the weakest criterion on a complete right-private
atlas.  A sharp scalar sufficient condition is

\[
        \delta_\phi>0,\qquad \delta_\phi\ge\Delta_\phi, \tag{3.3}
\]

where `delta_phi` is minimum role degree and `Delta_phi` is maximum successor
load.  Indeed
`delta_phi|X| <= e(X,N(X)) <= Delta_phi|N(X)|`.  If
`delta_phi<Delta_phi`, the complete bipartite graph from `Delta_phi` roles to
only `delta_phi` successors shows that no stronger conclusion follows from
these two scalars alone.

If the unpinned atlas has minimum menu degree `delta^raw_phi`, there are `b`
fixed boundary/connector blocks, each block deletes at most `lambda_phi`
distinct successor neighbours from any one role, and the post-deletion
maximum successor load is `Delta_phi`, then the explicit boundary form is

\[
              \delta^{\rm raw}_\phi-b\lambda_\phi
                    \ge\Delta_\phi>0.                  \tag{3.4}
\]

This is the weakest sharp surrogate available from those scalar menu/load
bounds alone; the full Hall family (3.1) may hold when (3.4) fails.

## 4. Full packet factors beyond one-shore privacy

Ordinary endpoint Hall is unsound when two different successors can still
share a cell, address or history resource.  This section works in the full
conflict graph of Section 1.

For a rational role-normalized law `x` on one phase packet, put

\[
 \lambda_x(c)=\sum_{d\sim c}x_d.                       \tag{4.1}
\]

### Theorem 4.1 (weighted Haxell factor)

If `lambda_x(c)<=1/2` for every positive candidate `c`, then the phase has
an independent transversal and hence a complete private factor.

#### Proof

Clear a common denominator `N` and replace candidate `c` by `Nx_c` labelled
clones.  Every role part has size `N`; a clone of `c` has degree
`N lambda_x(c)<=N/2`.  Haxell's `2 Delta` independent-transversal theorem
gives one clone from every role part.  Projection gives the claimed
transversal.  \(\square\)

The theorem rounds pairwise packing only.  It does not preserve an arbitrary
signed flag quota, state-balance equation, residual outer/supplier matching,
or Euler/subtour row unless that requirement was fixed before candidate
formation, encoded in composition closure, or separately repaired.

There is also a useful nonuniform local-lemma certificate.  Write
`d_s=|P_s|`, let `c_st` be the number of conflict edges between parts `s,t`,
and put

\[
             \eta_s=\sum_{t\ne s}{c_{st}\over d_sd_t}. \tag{4.2}
\]

### Theorem 4.2 (pair-mass LLL factor)

Assume `d_s>=1` for every role.  If

\[
       \eta_s+\eta_t\le {1\over4}
       \quad\hbox{whenever }c_{st}>0,                  \tag{4.3}
\]

then the phase has an independent transversal.

#### Proof

Choose one candidate uniformly and independently in every part.  For every
conflict edge between parts `s,t`, let `A` be the event that both endpoints
are chosen.  Then `p_A=1/(d_sd_t)`.  Use the dependency graph joining events
that share a role and set `z_A=2p_A`.  The total neighbouring `p`-mass is at
most `eta_s+eta_t`, so the total neighbouring `z`-mass is at most `1/2`.
Moreover (4.3) implies `p_A<=1/8`, hence `0<=z_A<=1/4`.  Therefore

\[
 z_A\prod_{B\sim A}(1-z_B)
 \ge 2p_A\left(1-\sum_{B\sim A}z_B\right)
 \ge p_A.                                                \tag{4.4}
\]

The asymmetric Lovasz local lemma avoids every conflict event.  \(\square\)

For prescribed candidate laws/certificates, Theorems 4.1 and 4.2 are
incomparable: the first controls every positive candidate's weighted
neighbourhood, while the second controls conflict-event mass through the two
incident roles.  This is not an existential separation over all laws: an
already known integral transversal gives a point-mass law satisfying
Theorem 4.1.

### Corollary 4.3 (boundary erosion and resource codegree)

Index capacity resources by types `j`.  Suppose the fixed phase boundary
uses `b_(phi,j)` distinct type-`j` resources, and one such resource occurs in
at most `ell_(phi,s,j)` raw candidates of role `s`.  Assume every
bulk--boundary incompatibility is witnessed by one of these counted
resources; otherwise its deletion load must be added as another type.
Boundary pruning deletes at most

\[
            e_{\phi,s}
             :=\sum_j b_{\phi,j}\ell_{\phi,s,j}          \tag{4.5}
\]

candidates from that role.

After pruning, trim every part to `D_phi` candidates.  Suppose a retained
candidate uses at most `q_(phi,j)` type-`j` resources, every such resource
occurs in at most `L_(phi,j)` retained candidates, and every conflict is
witnessed by a counted resource.  Then

\[
       \Delta(\Gamma_\phi)
       \le\sum_jq_{\phi,j}(L_{\phi,j}-1).               \tag{4.6}
\]

Consequently the two inequalities

\[
 D_\phi\ge1,\qquad L_{\phi,j}\ge1
       \quad\hbox{for every type used by a retained candidate}, \tag{4.7a}
\]

and

\[
 |{\cal P}^{\rm raw}_{\phi,s}|
       \ge D_\phi+e_{\phi,s}\quad(s\in S^o),
 \qquad
 D_\phi\ge
       2\sum_jq_{\phi,j}(L_{\phi,j}-1)                 \tag{4.7b}
\]

give a complete phase factor.  If (4.7a)--(4.7b) hold in both phases, the two
factors coexist sequentially with their independently chosen bulk and the
fixed conjugate boundary.

#### Proof

Equation (4.5) is the union bound over boundary resources.  A candidate has
at most `L_(phi,j)-1` rivals through each of its at most `q_(phi,j)`
type-`j` resources, proving (4.6).  The first inequality in (4.7b) leaves at
least `D_phi` candidates per part.  Haxell applies because every retained
part has size at least twice the maximum conflict degree.  \(\square\)

For a boundary of uniformly bounded literal size, (4.5) is `O(1)` only when
the local loads `ell_(phi,s,j)` are themselves uniformly bounded.  Pair
codegree alone is insufficient: two parts can form `K_(D,D)` while every
candidate pair shares at most one privately named resource.

### Theorem 4.4 (full-footprint hypergraph expansion)

For one phase, let `H_s` be the hypergraph whose edges are the complete
resource footprints of the candidates of role `s`, after boundary pruning.
Suppose every footprint has size at most the absolute constant `R>=2`.  If

\[
 \nu\!\left(\bigcup_{s\in I}{\cal H}_s\right)
       >(2R-3)(|I|-1)\qquad(\varnothing\ne I\subseteq S^o), \tag{4.8}
\]

then the phase has a complete private factor.

#### Proof

Pad smaller footprints by candidate-private dummy resources.  This changes
neither pairwise disjointness nor matching numbers.  Equation (4.8) is the
Aharoni--Haxell rainbow-matching hypothesis for rank `R`, so it gives one
pairwise disjoint footprint from every role family.  Composition closure
turns these footprints into the required tickets.  \(\square\)

The rank `R` must count every literal capacity-one resource.  A growing
address or history list cannot be hidden in one formal coordinate.  Apply
(4.8) separately in the two phases; no cross-phase bulk pairing is needed.

## 5. Bounded collision energy gives a bounded common shore

The full-factor bounds above are stronger than is needed for a bounded
sidecar.  For one role-normalized phase law define

\[
 M_x=\sum_{\{c,d\}\in E(\Gamma)}x_cx_d.                \tag{5.1}
\]

### Theorem 5.1 (two-phase bounded-energy deletion)

Let `x^0,x^1` be role-normalized laws on the two fixed phase packets.  There
is a common role set `E subseteq S^o` with

\[
                  |E|\le\lfloor M_{x^0}\rfloor
                         +\lfloor M_{x^1}\rfloor       \tag{5.2}
\]

such that each phase has an independent transversal on `S^o-E`.

If the roles of `E` possess one jointly certified pair of phase-valid
boundary completions whose complete closures are conjugate and jointly
disjoint from the restricted bulk factors, adjoining them gives complete
1,748-ticket factors with an enlarged boundary.  Individual certificates
for each exceptional role are not enough.

#### Proof

In phase `phi`, choose candidates independently according to `x^phi`.  The
expected number of selected conflict edges is exactly `M_(x^phi)`.  Some
choice therefore has at most `floor(M_(x^phi))` conflict edges.  Delete one
selected endpoint from every such edge; at most one role is lost per edge,
and the remaining selection is independent.  Let `E` be the union of the
two phase deletion sets and restrict both selections to its complement.
This proves (5.2).  The final assertion is composition closure plus the
hypothesized boundary completions.  \(\square\)

If conflicts are witnessed by shared resources and
`L_x(u)=sum_(c:u in R(c))x_c`, then

\[
                  M_x\le {1\over2}\sum_uL_x(u)^2.      \tag{5.3}
\]

Indeed the unordered pair mass charged to resource `u` is at most
`L_x(u)^2/2`, and charging a conflict to all its shared resources only
overcounts.  Thus bounded square-load energy in both phases is enough for a
bounded static exceptional shore.  It is not by itself a terminal
completion theorem.

### Corollary 5.2 (common allocation by owner-factor averaging)

Let `Omega_1,...,Omega_r` be the factorization from Theorem 2.1.  Suppose
**as an additional host hypothesis** that, for each `j`, there is a fixed
replacement packet `P_j` in the sense of Section 1 whose common structural
allocation is `Omega_j`.  The packet may have its own actual boundary
`Y_j`, but all `Y_j` lie in the allowed conjugate boundary class and have
one uniform literal size bound.  Thus every packet separately respects the
order “allocation, then actual boundary, then menus”; no boundary pin is
silently required to lie in all edge-disjoint owner factors.

For phase `phi` and packet `j`, let `Z_(phi,j)` be the roles with empty
pruned menus; on every other role choose a probability law and let
`M_(phi,j)` be its collision energy.

If

\[
 {1\over r}\sum_{j=1}^r\sum_{\phi=0}^1
       \bigl(|Z_{\phi,j}|+M_{\phi,j}\bigr)\le C,       \tag{5.4}
\]

then one common allocation `Omega_j` supports independent phase banks on a
common role set omitting at most `floor(C)` roles.

#### Proof

Some `j` has the summand in (5.4) at most `C`.  First omit the zero-menu
roles in both phases.  Apply the proof of Theorem 5.1 to the remaining laws
and take the union of the two deletion sets.  The number omitted is at most

\[
 \sum_\phi\bigl(|Z_{\phi,j}|+\lfloor M_{\phi,j}\rfloor\bigr)
 \le \left\lfloor
       \sum_\phi(|Z_{\phi,j}|+M_{\phi,j})\right\rfloor
 \le\lfloor C\rfloor.                                  \tag{5.5}
\]

\(\square\)

The extra packet-family premise in Corollary 5.2 is load-bearing.  A
compressed-normal common-basis fibre need not contain an entire bare
one-factorization, and a boundary-pinned residual family need not be closed
under arbitrary owner switches.  The bare factors do not themselves supply
the packet-specific bounded boundaries.  No such admissible packet family
is known for the replacement host.

## 6. Exact pull-clock and rotor interface

The newly pasted reversed-ratio pull-clock derivation is retracted by
`MATH_AUDIT_PULL_CLOCK_URGENT_SIGN_RETRACTION_AND_ROTOR_FALLBACK_20260803.md`.
The authoritative corrected sign/cost proof survives, and the independent
monotone-rotor theorem separately proves the same rank-only fractional
membership.  Thus the proof-safe fractional input is a rational literal
trace circulation obtained only after averaging over owners, private sets,
orders, cores and payload tables.  It enters the packet model only through a separate
one-host literal pushforward

\[
 \pi_\phi:\Omega_{\rm trace}\longrightarrow
       \bigcup_{s\in S^o}{\cal P}_{\phi,s}(H,\mu,\sigma,Y), \tag{6.1}
\]

constructed separately for `phi=0,1`, preserving roles, physical cells,
sources, actual addresses and boundary histories.  In addition, the pushed
weights must have total one in every role, load at most one on every actual
capacity resource, and satisfy every displayed boundary, balance and history
row `B_Yx=b_Y`.  These are the full one-host pushforward hypotheses, not
consequences of a bare label map.  Under all of them, pushing trace weights
through (6.1) gives the required law on the one fixed packet.  The existence
of such maps and weights is **UNPROVED**.

Once such a law exists, the implications proved above are precisely:

\[
\begin{array}{c}
 \max_c\lambda_{x^\phi}(c)\le1/2
       \Longrightarrow \hbox{complete static phase factor},\\[2mm]
 M_{x^0}+M_{x^1}=O(1)
       \Longrightarrow \hbox{common }O(1)\hbox{ static defect}.
\end{array}                                               \tag{6.2}
\]

Neither implication preserves an omitted balance equation.  The integral
rotor theorem applies on a different positive face: one exact owner-payload
table, payload-transparent Cartesian tail/head rectangles, and all fixed-
table Hoffman cuts give a totally unimodular one-copy selector.  A selected
static bank from Sections 4--5 need not lie on that rectangle face.

Accordingly the chronological alternatives remain:

1. include the complete ticket/private rows in one verified Cartesian
   Hoffman face;
2. reserve a distinct-role spanning skeleton and verify every residual
   Hoffman cut; or
3. prove a literal fusion preserving owner, resource, boundary, upper,
   residence and compiler rows.

All three are **UNPROVED** for a replacement host.  Fractional connected
support does not imply any of them.

## 7. The weakest current replacement-host targets

For the static 1,748-ticket layer, the following targets are now exact or
proved sufficient.

### Full-factor target

Construct one packet of Section 1 such that, in each phase, either

* the complete right-private atlas satisfies the exact Hall family (3.1);
  or
* the full conflict graph satisfies Theorem 4.1, Theorem 4.2, or the explicit
  post-boundary resource inequalities (4.7a)--(4.7b), or its complete footprints
  satisfy the hypergraph expansion (4.8).

This gives two complete phase-local factors.  Within the right-private
branch, (3.1) is necessary and sufficient; the sharp degree/load surrogate
is the boundary-eroded form of (3.3).

### Bounded-sidecar target

It is enough instead to construct one packet and phase laws satisfying

\[
                   M_{x^0}+M_{x^1}=O(1),               \tag{7.1}
\]

or the owner-averaged zero-plus-energy row (5.4), together with phase-valid
jointly conjugate terminal completions for the omitted common shore.  This is the
weakest aggregate sufficient condition proved here: it requires neither
uniform menu thickness nor pointwise conflict expansion.  It is not claimed
necessary.

The actual **UNPROVED replacement-host expansion lemma** is therefore:

> Uniformly along one compatible all-dimensional spine, construct a new
> compressed-normal common-basis host, exact inverse outer parent, common
> structural owner allocation, and bounded complete boundary for which the
> full-factor target holds, or for which (7.1) holds and every exceptional
> shore has one jointly valid bounded conjugate terminal completion.

Common-basis normality, nonempty projected flag menus and bounded pair
codegree do not imply this lemma.  The fixed-`P*` no-go is neither modified
nor used as evidence against a new host.

## 8. Conditional route to `B(k)+O(1)`

Assume the unproved replacement-host expansion lemma of Section 7, the
complete boundary factorization/conjugacy, and an integral connected
chronology on the same packet.  Assume additionally the already-scoped
requirements needed by the regenerative compiler: endpoint aperture and
reset, physical birail cross matchings and zero-block collapse, the literal
monotone pivot with its two owner-legal rays, residence and upper/source
legality, bounded total compiler eviction, and a compatible odd spine with
even terminal children.

All of these witnesses are required simultaneously on the same selected
host, boundary and spine; separate existential witnesses are not composed.

Under exactly those hypotheses, the existing regenerative accounting gives

\[
                         \nu(k)\le B(k)+a+C_{\rm term}, \tag{8.1}
\]

where `a` is the complete literal boundary/connector/compiler serialization
charge and `C_term` is the terminal casualty bound.  Uniform constants imply
`B(k)+O(1)`.

This implication is conditional.  The present note proves only the static
factor and bounded-defect arrows.  It proves no unconditional
`B(k)+O(1)`, no `B+1`, and no new exact value of `nu(k)`.

## 9. Proof-status ledger

The following statements are **PROVED**.

1. Identity-core endpoints are source-private and do not erode the disjoint
   reduced inverse matching (Lemma 1.1).
2. The bare odd-central incidence graph has `r` rank-adjacent owner factors
   (Theorem 2.1).
3. On a complete right-private atlas, separate phase Hall is exact and a
   common deletion of size at most `h_0+h_1` suffices (Section 3).
4. Weighted Haxell, pair-mass LLL and the explicit boundary/resource-load
   inequalities, as well as the full-footprint Aharoni--Haxell expansion,
   each give complete static factors (Section 4).
5. Total collision energy gives a common two-phase bounded defect; the
   factorization-average form (5.4) chooses one common bare allocation under
   its explicit admissibility hypothesis (Section 5).
6. Bulk phase tickets need not correspond once complete bounded-boundary
   erasure is available.

The following statements are **UNPROVED**.

1. A new protected replacement common-basis table, compatible inverse outer
   parent and admissible common owner parameter with the required menus.
2. A uniformly bounded complete cross-phase boundary and terminal
   completions for an exceptional shore.
3. Any Hall, Haxell, LLL, pointwise weighted-load, or `O(1)` collision-energy
   estimate on an actual all-dimensional replacement family.
4. The one-host pull-clock maps (6.1), preservation of balance under packet
   rounding, and a connected integral chronology.
5. The replacement-host residence, upper/source/common-cap, compiler and
   physical birail compatibility rows.
6. Any unconditional asymptotic conclusion for `nu(k)`.

## 10. Proof-bearing inputs

```text
MATH_THEOREM_REPLACEMENT_HOST_ONE_SHORE_HALL_AND_BOUNDED_BOUNDARY_CONJUGACY_20260803.md
MATH_THEOREM_FRACTIONAL_PULL_CLOCK_PHASE_TICKET_MEMBERSHIP_AND_WEIGHTED_CONFLICT_ROUNDING_20260803.md
MATH_THEOREM_FRESH_TICKET_BOUNDARY_ERASURE_AND_BOUNDED_RESET_STATE_20260802.md
MATH_THEOREM_CORRECTED_PULL_CLOCK_PACKING_AND_FRACTIONAL_TRACE_CIRCULATION_20260801.md
MATH_AUDIT_PULL_CLOCK_URGENT_SIGN_RETRACTION_AND_ROTOR_FALLBACK_20260803.md
MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md
MATH_THEOREM_A_INTEGRAL_COLOURED_ROTOR_ONECOPY_MINMAX_AND_RAINBOW_FUSION_20260802.md
MATH_THEOREM_ROTOR_ODD_COATOM_ONECOPY_AND_PROTECTED_OWNER_CIRCUITS_20260802.md
MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md
```

The decisive matching, clone, local-lemma, boundary-erosion and collision-
energy steps were independently rederived before this note was frozen.  No
finite or external computational assertion is made.
