# Prospective direct-new-phase pump: exact residual Ore--Ryser extension

**Date:** 2026-08-02  
**Lane:** K, protected pump/corridor planting  
**Status:** unconditional owner/lower-`q1` two-factor extension for
`d=O(sqrt(m))` and all sufficiently large `m`, with explicit finite
inequalities.  The two-corridor order/history, integer background charge,
deeper upper deck and compiler are separate gates.

## 0. Outcome

Put

\[
        k=2m-1,
        \qquad p=3k=3(2m-1).
\tag{0.1}
\]

Fix the developed twisted-three-run pump and one nonprivate physical pump
edge.  Choose one literal Cartesian Boolean hex at that edge prospectively,
and prescribe the **new** three-edge phase in the desired final factor.  By
the direct-new-phase theorem, the old and new phases have the same declared
central resource vector.  The Ore argument below uses only its undirected
owner/lower projection; orientation, histories and sidecars are not part of
this equivalence.  The owner/lower residual problem may therefore be solved
on the equivalent face

\[
   \text{closed pump}\quad+\quad
   \text{the two old partner edges}\quad+\quad Q_A,
\tag{0.2}
\]

where `Q_A` is the opened fixed-`z` seven-ear incidence path.  This face
deletes the equal pump shores and leaves an ordinary protected residual
Ore--Ryser problem.

The protected incidence count is

\[
       q_*:=|E(Q_A)|+4=52d+66.                         \tag{0.3}
\]

The extra four are the incidence lifts of the two old projected partner
edges.  Equivalently, the direct face consists of the open pump plus three
new projected edges, so it has `6k+4` protected middle-level incidences in
the pump/hex block: six more than the open pump and four more than the
closed pump.  The old phase is only a demand witness; it is not required to
occur in the final topology.

Let

\[
\begin{aligned}
 D&=(m-1)(m-2),\\
 G_*&={m-1\over m-2}(2p+q_*),\\
 B_*&={2m^2G_*\over2m-1},\\
 c_m&={(m-2)(m-3)\over m(m-1)},\\
 a_m&={m^2-10m+12\over4(m-1)}.
\end{aligned}                                          \tag{0.4}
\]

If

\[
\begin{gathered}
 m\ge10,qquad q_*\le m-3,qquad
 B_*\le {m+2\choose3},                                 \tag{0.5}\\
 a_m(m-2)(m-3)\ge q_*,                                 \tag{0.6}\\
 c_m\left(p+{D\over2}\right)\ge2p+q_*,               \tag{0.7}
\end{gathered}
\]

and the local banks are separated by

\[
 3k\sum_{j=0}^{2d+5}{m\choose j}{m-1\choose j}
       <{2m-2\choose m},
 \qquad m\ge\max\{3d+4,2d+13\},                       \tag{0.8}
\]

then **every** residual Ore--Ryser shore inequality holds.  Hence the
closed pump plus the protected bank in (0.2) extends to a spanning
owner/lower-`q1` two-factor.  Replacing the old local phase by the new local
phase gives a degree-two owner/lower projection containing the three new
projected edges.  It does not orient those edges or certify their literal
history/private-sidecar state.

For every fixed `C`, conditions (0.5)--(0.8) hold for all sufficiently
large `m` whenever `d<=C sqrt(m)`: the ball in (0.8) is subexponential in
`m`, while its right side is exponential.  Thus the owner/lower residual
gate is unconditionally closed in the requested asymptotic regime.  This is
not a two-corridor or one-cycle theorem.

## 1. A residual-safe literal partner exists

Write the chosen pump edge as

\[
 E=L\cup\{z_0\}\longrightarrow H=L\cup\{a_0\},
 \qquad U=L\cup\{a_0,z_0\}.                            \tag{1.1}
\]

For `b in L` and `c notin U`, the two conceptual old partners are

\[
\begin{aligned}
 A_b&=U-\{b\}\longrightarrow B_{bc}=L-\{b\}+\{a_0,c\},\\
 C_{bc}&=L-\{b\}+\{z_0,c\}\longrightarrow D_c=L\cup\{c\}.
\end{aligned}                                          \tag{1.2}
\]

Their lower facets are

\[
             I_1=H-\{b\},
             \qquad I_2=L-\{b\}+\{c\}.               \tag{1.3}
\]

### Lemma 1.1 (owner/lower-safe pair supply)

For the twisted-three-run pump, every pump owner contains at most three
pump facets and every pump facet is contained in at most three pump owners.
Every external owner contains at most one pump facet, and every external
facet is contained in at most one pump owner.

Consequently, for every target pump edge and every `m>=8`, at least

\[
                         (m-7)(m-3)>0                 \tag{1.4}
\]

pairs `(b,c)` make all four owners in (1.2) external to the pump owner bank
and both facets in (1.3) external to the pump facet bank.

#### Proof

The three-run signature table gives internal incidence degree two away
from threshold slack zero and degree at most three at threshold.  Its
external-cross-degree-one conclusion is Lemma 1.1 of
`MATH_THEOREM_K_TWISTED_C6_RESIDUAL_ORE_CURVATURE_AND_POLYNOMIAL_CORE_20260802.md`.

Exclude a label `b` if either `E-{b}` or `H-{b}` is a pump facet.  There
are at most six such labels.  If `b` survives, then `A_b,C_bc` cannot be
pump owners: either would share the external facet `E-{b}` with `E`.
Likewise `B_bc` cannot be a pump owner, and `I_1` is external, because both
statements are controlled by `H-{b}`.

The target facet `L` is contained in at most three pump owners, two of
which are `E,H`.  Thus at most one allowed `c` makes `D_c` a further pump
owner.  Exclude it.  If `I_2` were then a pump facet, the external owner
`D_c` would contain the two pump facets `L,I_2`, contradicting external
cross-degree one.  There remain at least `m-7` choices of `b` and `m-3`
choices of `c`.  \(\square\)

The lemma concerns owner/lower resources.  Avoidance of a separately
protected immediate-upper or history bank is an additional finite filter.
The independent literal census in the audit found a positive fully
immediate-`q1`-safe menu in every tested case, but that finite fact is not
used as an all-`m` upper theorem.

## 2. Exact phase accounting

Let `P_closed` be the closed pump incidence cycle.  Let `O_hex` be the four
incidences lifting the two old partner edges in (1.2), and let `N_hex` be
the six incidences lifting the three new edges

\[
       A_b\to H,qquad C_{bc}\to B_{bc},qquad E\to D_c. \tag{2.1}
\]

### Lemma 2.1 (four-incidence residual cost)

On owner and lower-facet degrees,

\[
            P_{closed}\mathbin{\dot\cup}O_{hex}
       \quad\text{and}\quad
            (P_{closed}-e)\mathbin{\dot\cup}N_{hex}    \tag{2.2}
\]

have the same demand vector.  The first presentation deletes the closed
pump shores and leaves precisely four protected residual incidences.

#### Proof

The two Boolean-hex phases have identical tail and head owner multisets and
identical three lower-facet multisets.  Each selected projected edge uses
two incidences at its lower facet.  Hence the six incidences on either side
of the local phase give identical owner degrees and saturate the same three
lower vertices.  In particular the opposite phase cannot be selected a
second time by a residual completion: all of its lower vertices already
have residual demand zero.  \(\square\)

The common-host qualification is essential for seam-specific resources.
Equation (2.2) is exact for owner/lower incidence, and the full direct-phase
theorem supplies the analogous equality for its declared central resource
vector.  It does not identify histories, seam IDs, private tokens, or an
edge-specific sidecar.

By the stronger anchor choice

\[
  d_J(X,O_P)>2d+5,                                     \tag{2.3}
\]

the opened seven-ear bank is also owner/lower-disjoint from the selected
partner bank.  Every partner owner is within one Johnson step of a pump
owner.  If a local and partner facet were equal, their incident owners would
be within one further Johnson step.  Since local owners lie within `2d+3`
of `X`, a collision would put `X` within `2d+5` of a pump owner.  The
deterministic packing proof from 2648K therefore remains valid after replacing its radius
`2d+4` by `2d+5`; for `d=O(sqrt(m))` this changes no asymptotic conclusion.
Thus

\[
       Q^\circ=Q_A\mathbin{\dot\cup}O_{hex}            \tag{2.4}
\]

is two-bounded and has size (0.3).

## 3. Verification of every Ore--Ryser shore

Delete the closed pump facet and owner shores `F_P,O_P`.  For the protected
bank `Q^circ`, put

\[
                 b(v)=2-d_{Q^\circ}(v).               \tag{3.1}
\]

For `S subseteq L-F_P`, put

\[
 T=(L-F_P)-S,
 \qquad A=F_P\mathbin{\dot\cup}T.                     \tag{3.2}
\]

For a rank-`m` owner `Y`, define

\[
 j_A(Y)=|\{x\in A:x\subset Y\}|,
 \qquad c_A(Y)=(j_A(Y)-m+2)_+.                        \tag{3.3}
\]

Let

\[
\begin{aligned}
 \kappa(A)&=2|A|-\sum_Yc_A(Y),\\
 \rho_{O_P}(A)&=\sum_{Y\in O_P}c_A(Y),\\
 \omega_{Q^\circ}(A)&=
   \sum_{Y\notin O_P}(q_T(Y)-c_A(Y))_+.
\end{aligned}                                          \tag{3.4}
\]

The exact complementary Ore identity is

\[
 \sum_{x\in S}b(x)\le
 \sum_{Y\notin O_P}\min\{b(Y),d(Y,S)\}
 \quad\Longleftrightarrow\quad
 \kappa(A)+\rho_{O_P}(A)
      \ge2p+\omega_{Q^\circ}(A).                     \tag{3.5}
\]

This is an equivalence for every shore, not a relaxation.

### Theorem 3.1 (direct-new-phase residual extension)

Under (0.5)--(0.8), inequality (3.5) holds for every `S`.  Hence an
integral residual `b`-factor exists, and adjoining the fixed bank gives a
spanning owner/lower-`q1` two-factor whose degree-preserving local switch
contains the underlying three new Boolean-hex projected edges.

#### Proof

Apply Theorem 5.1 of the residual-curvature theorem with
`Q=Q^circ` and `q=q_*`.  Its proof is integral: an edge-minimal failed
extension yields (3.5); small shores follow from residual minimum degree
`m-1` and same-shore codegree one, Tanner localization makes one full shore
at most `B_*`, and the two opposite Lovasz--Kruskal--Katona estimates give
respectively the coefficients `a_m` and `c_m`.  Conditions (0.5)--(0.7)
contradict the two possible localized shores.  Ore--Ryser then gives the
integral factor.

Finally apply Lemma 2.1 and replace the conceptual old local phase by the
new local phase in the undirected owner/lower projection.  The resulting
graph is still degree two at every owner and lower facet.  Orientation and
new-seam legality remain the state-expanded corridor row of Section 4.
\(\square\)

For a literally frozen four-sided depth-`d` corridor collar, add its exact
incidence cost to `q_*`.  In the usual disjoint long-collar presentation
this is at most `8d`, so one may use

\[
                       q_{collar}=60d+66.             \tag{3.6}
\]

The same theorem applies after replacing `q_*` by `q_collar`.  If histories
are kept as finite endpoint states rather than frozen edges, no such extra
Ore cost is charged.

## 4. Charge and history: exact separation

Prospective new-phase planting removes the post-hoc mutual-codegree and
three-component-escape quantifiers.  It does **not** make the following two
rows consequences of Ore--Ryser.

1. The six directed collar tests must accept one common pair of residual
   corridors.  Their exact obstruction is the two-root/two-sink Hall-damage
   value `Delta_hex` in Section 8 of
   `MATH_THEOREM_ROOT_PROSPECTIVE_NEW_PHASE_BOOLEAN_HEX_TWO_CORRIDOR_REDUCTION_20260802.md`.
2. The two conceptual nonpump closure paths must have zero total integer
   charge in one common lift.  The local Boolean-hex identity then preserves
   the pump's normalized charge.

There are two exact sufficient charge structures.  On the contracted
corridor graph, if the accepted edge weight has an additive representation

\[
                       \omega(u,v)=a(u)+b(v)           \tag{4.1}
\]

whose demand-weighted constant is zero, every residual factor has zero
background charge.  Alternatively, a fixed-point-free charge-reversing
involution and a quotient factor give zero by paired cancellation.  These
are Theorems 2.1 and 3.1 of
`MATH_THEOREM_K_CYCLIC_COBOUNDARY_ZERO_BACKGROUND_CHARGE_AND_PAIRED_ORBIT_HOST_20260802.md`.

No condition involving only unweighted degree, codegree, or expansion can
replace (4.1): arbitrarily regular codegree-one bipartite supports admit a
weighting for which every perfect matching has charge one.  Thus the minimal
remaining charge obstruction is a nonzero constant on the entire
alternating-cycle fibre, not an Ore shore.

In the explicitly one-physical-edge, non-equivariant presentation, the
two-corridor theorem already proves physical one-cycle topology.  Coprime
quotient voltage must not be invoked unless an equivariant quotient
development is separately restored; here the pump's `+1` is only the
normalized integer regenerative charge.

## 5. Scope

Closed here, unconditionally for `d=O(sqrt(m))` and sufficiently large
`m`:

* existence of an owner/lower-safe literal partner pair;
* exact direct/old phase demand equivalence;
* the protected-edge extension for `q=52d+66` (or any larger declared
  `q=O(d)` satisfying (0.5)--(0.7)); and
* every residual Ore--Ryser shore inequality.

Still open and not implied by this theorem:

* a role-separated two-root/two-sink completion with one common history
  state;
* zero integer background charge unless (4.1) or the paired-orbit criterion
  is built into that completion;
* the deeper upper deck, exterior source chronology, residence beyond the
  encoded collars, and terminal common-cap/compiler feasibility.

Thus the exact next gate is no longer functional partner supply or residual
owner/lower Hall.  It is A's capacity-/charge-faithful two-corridor Hall
problem with the physical history state carried in the same table.
