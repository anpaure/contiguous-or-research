# Compound residence augmentation: packet-builder duality, pair/triple interaction, and the exact regenerative hypothesis

**Date:** 2026-08-02

**Lane:** local frozen-artifact mathematics

**Status:** exact finite formulation and conditional regenerative theorem; no
all-dimension supply theorem, upper/source/compiler closure, or new search
result is claimed.

## 1. Result and proof-safe calibration

There are two distinct facts to separate.

1. For any declared finite catalogue of two- or three-circuit proposals, there
   is an exact bounded-depth packet-builder network.  It includes simultaneous
   overlapping proposals whose individual halves are not factors.  A negative
   closed packet is exactly a negative root-to-commit path.  If no such path
   exists, either a reachability Farkas cut proves that no closed packet exists,
   or a min-cost-flow potential proves that every closed packet in the declared
   catalogue has nonnegative residence delta.
2. This alternative is not an expansion theorem.  Uniform descent follows only
   after a regenerative negative-return hypothesis in the complete lifted
   state.  Tight cap cycles give the smallest obstruction to deriving that
   hypothesis from cap completeness and bounded local degree.

The locally frozen `k=17` chronology is

\[
  5372\longrightarrow4199\longrightarrow4165\longrightarrow4148
  \longrightarrow4131\longrightarrow4080\longrightarrow4029             \tag{1.1}
\]

positive physical runs of lengths at most three.  The number `3944` is not a
frozen short-run endpoint: it is the invariant number of protected physical
rows.  Every numerical statement below uses `4029` as the current authenticated
short-run value and `3944` as the protected-row count.

The endpoint files authenticate exact rank-eight facets, degree-two rank-nine
owners, all rank-ten caps, the protected bank, nonzero quotient voltage, and one
physical cycle.  They do not authenticate residence zero, ranks 11--17, a
source antecedent, a terminal compiler, or a universal word.

## 2. The exact algebra: integer kernel first, graphic cycle space only on a face

Let `E` be the row-option universe.  An option `e` has one lower facet `f(e)`,
two owner endpoints `u(e),v(e)`, one immediate-upper cap `c(e)`, and any named
protected/deeper labels.  A factor vector `x in {0,1}^E` satisfies

\[
 \sum_{e:f(e)=f}x_e=1,\qquad
 \sum_{e:u(e)=w\text{ or }v(e)=w}x_e=2.                    \tag{2.1}
\]

For two exact factors `x,x'`, their signed difference `z=x'-x` lies in the
integer kernel of the facet--owner matrix in (2.1).  A row-option column has one
facet entry and two owner entries.  This matrix is not, in general, a graphic
incidence matrix, and neither total unimodularity nor a single-matroid exchange
theorem is assumed here.  The safe full-master language is **integer-kernel
move** (with support-minimal moves as its circuits), not graphic cycle, unless
an additional face reduction is proved.

There is a useful exact graphic reduction on the endpoint-retaining face.  If a
row change keeps owner `a` and replaces moving owner `b` by `c`, orient the
change as an arc `b -> c` in the state-relative owner-exchange digraph.  For a
facet-compatible multiset of such changes, owner exactness is precisely

\[
                         Bz=0,                              \tag{2.2}
\]

where `B` is the directed node--arc incidence matrix.  Thus the moving-owner
changes form a nonnegative integral circulation and decompose into directed
cycles.  A quotient `C6` or `C8` is respectively a directed cycle of three or
four row changes.  Facet capacity, row atomicity, cap coverage, protection,
topology, voltage, and residence remain additional constraints; (2.2) does not
make them matroidal.

This explains both the value and the limit of cycle-space language in the
frozen paired catalogues.  The endpoint-retaining quotient pairs live in an
honest graphic circulation projection.  The physical overlapping
star--octahedral face requires literal row-set composition and is not justified
by (2.2) alone.

## 3. Proposal semantics and the packet builder

Fix a protected factor `F`, a depth `d`, a primitive catalogue `Q(F)`, a support
bound `h`, and a packet size `s` (here `s=2` or `3`).  Let `Phi_d` be a fixed
nonnegative integer potential which gives positive weight to every prohibited
short run.  It may be a sign/length-weighted count or a sufficiently large-base
scalarization of the finite-carrier lexicographic tuple
`(N_+,D_+,N_0,D_0)`.  Every catalogue must declare one of the following
semantics.

* **Ordered sequential semantics.**  A primitive is a partial transition on
  the current literal state.  Applicability is tested after every materialized
  prefix; that prefix may carry only the debts explicitly allowed by the
  transition domain.
* **Fixed-base batch semantics.**  A primitive is a pair of pending removal and
  addition sets.  A tuple is composed by a declared canonical rule, such as
  union of removals followed by union of additions.  No individual proposal is
  asserted to be a factor.

The semantics may not be silently mixed.  In particular, a complete sequential
depth-three theorem must regenerate state-relative primitives after a materialized
prefix.  Enumerating only pairs or triples of circuits active at the root is a
smaller fixed-base face unless commutation and completeness are separately
proved.

A packet-builder state stores at least

\[
 \Sigma=(j,\mathcal K,D,A,R,\mathcal I,\Theta),             \tag{3.1}
\]

where:

* `j<=s` is the number of proposals and `K` is their ordered word under
  sequential semantics, or their canonical tuple/set under batch semantics;
* `D,A` are the actual pending row removals and additions, not merely marginal
  degree vectors;
* `R` is the exact affected-resource ledger, including cap loads, protected
  collisions, used support, and any allowed prefix debt;
* `I` is the retained-path port interface needed for component and voltage
  replay; and
* `Theta` is the exact depth-`d` trace-transfer profile on that interface.

Proposal arcs add one primitive and have cost zero.  Under batch semantics a
proposal prefix need not represent a factor; under sequential semantics every
prefix must lie in the declared transition domain.  The empty proposal list is
not a packet: a **commit arc** is permitted only at a state with `1<=j<=s`, and
exists only if the declared composition gives a literal selected-row set `F^P`
satisfying all final gates:

1. every facet once and every owner at degree two;
2. every protected row unchanged;
3. every required cap has positive load;
4. the required component count and lift voltage hold; and
5. every optional deep-shadow, source, or compiler row named in this solve also
   holds.

The commit cost is the exact endpoint delta

\[
                  C(P)=\Phi_d(F^P)-\Phi_d(F).              \tag{3.2}
\]

This terminal-commit construction is essential for the frozen mixed physical
pair face: an individually duplicate star or octahedral phase may have no
literal owner cycle, while the simultaneous pair repairs the collision.
Assigning it a fictitious intermediate residence value would make the answer
depend on an arbitrary extension of `Phi_d`.

## 4. Exact union-port evaluation

The global residence cost is nonlinear in a list of root-computed primitive
deltas, but it is local to the union of changed ports.

### Lemma 4.1 (retained-path contraction)

Let `F` and a committed `F'` be degree-two factors, and let `J` be the old
selected adjacencies absent from `F'`.  Cutting `J` decomposes the affected
part of `F` into retained paths.  The new adjacencies pair their ports.  The
following data determine exactly:

* the components of `F'`;
* the signed voltage of each quotient component; and
* `Phi_d(F')-Phi_d(F)`:

1. the retained path/involution on the ports;
2. the new port matching, including the orientation in which each retained
   path is traversed;
3. the signed voltage carried by each retained path and new connector; and
4. for every coordinate, the truncated binary-word transfer of every retained
   path through run age `d+1`.

#### Proof

Contract every retained path to a decorated port edge.  Its union with the new
port matching is a disjoint union of alternating port cycles, exactly the
components of `F'`.  Summing the signed decorations around each port cycle gives
its voltage.

For a binary trace, scan a retained path with state `(bit,age)`, clipping age at
`d+1`; on a bit change, charge the completed run if its length is at most `d`.
Split the result into (i) the fixed charge of completed runs strictly internal
to the path and (ii) a normalized finite boundary transformation recording its
first/last bits, clipped boundary ages, and constant-path flag.  Reversal swaps
the boundary roles.  The internal charge is unchanged by port re-pairing and
cancels from the old/new delta; it may be stored as a separate integer check.
Composition of the normalized transformations along a port cycle, followed by
cyclic closure, supplies every boundary correction and therefore counts every
short trace component exactly.  Summing over coordinates proves the claim.
\(\square\)

For a fixed set of `m<=h` cuts, coordinates with the same vector of truncated
path transfers are indistinguishable.  They may be grouped into a histogram on
at most `|T_d|^m` transfer types, where `T_d` is the finite set of **normalized
boundary** transformations just defined; unbounded internal integer charges are
stored separately and cancel from the matching comparison.  This gives a
bounded-dimensional interface depending on `d` and `h`; its multiplicities
still depend on the ambient dimension.  It is not a claim that the total state
count is dimension independent.

There is one important incremental caveat.  A later proposal can introduce a
new cut inside a path already summarized by an earlier proposal.  Therefore an
exact builder must retain the actual proposal/row set, as in (3.1), or pre-split
the carrier at every potential seam in the declared envelope.  Endpoint
summaries alone are Markov-sufficient only after the complete union of cuts is
fixed.

### Corollary 4.2 (bounded exact commit state)

For fixed `d,s,h`, a commit can be checked using a bounded number of row, cap,
port-matching, voltage, and transfer-profile coordinates, together with integer
multiplicities and the actual pending rewrite mask.  Thus the two/three-circuit
problem has an exact finite state expansion for every fixed carrier.  No
cap-only or component-only quotient is exact, because it forgets the trace
transfer cross terms.

## 5. The exact min-cost-flow/Farkas alternative

Let `G^b=(V,E)` be the finite packet-builder DAG.  Its root is
`sigma=(F,emptyset)`.  Every valid commit state has a zero-cost arc to a common
sink `tau`.  Let `N` be the head-minus-tail node--arc incidence matrix and put

\[
                         b=e_\tau-e_\sigma.                 \tag{5.1}
\]

### Theorem 5.1 (two/three-circuit packet alternative)

Exactly one of the following cases holds.

1. `tau` is unreachable.  There is no closed packet in the declared catalogue
   and composition semantics.
2. `tau` is reachable and the unit-flow optimum

   \[
      \mu_s=\min\{c^Tx:Nx=b,\ x\ge0\}                     \tag{5.2}
   \]

   is negative.  An integral optimum is a negative closed packet of at most
   `s` proposals.
3. `tau` is reachable and `mu_s>=0`.  There is a real potential `y` satisfying

   \[
      y_v-y_u\le c_{uv}\quad(u\to v\in E),\qquad
      y_\tau-y_\sigma=\mu_s\ge0.                           \tag{5.3}
   \]

   It certifies that every closed packet in the declared builder has
   nonnegative cost.

If case 1 holds, put `y=0` on vertices reachable from `sigma` and `y=1`
outside.  Then

\[
                     N^Ty\le0,\qquad b^Ty=1,               \tag{5.4}
\]

which is an exact Farkas infeasibility certificate for (5.2).

#### Proof

When the sink is reachable, every feasible unit flow decomposes into
root-to-sink paths.  The node--arc incidence matrix is totally unimodular, so an
optimal extreme point is integral; acyclicity makes it one builder path.  Its
only nonzero semantic charge is the exact commit cost (3.2).  Hence (5.2) is
exactly the minimum closed-packet delta.

The dual of (5.2) is

\[
 \max\{y_\tau-y_\sigma:y_v-y_u\le c_{uv}\ (u\to v)\}.     \tag{5.5}
\]

Strong network-flow duality gives cases 2 and 3.  If the sink is unreachable,
no arc leaves the reachable set, so the cut potential in (5.4) satisfies the
displayed inequalities and separates `b` from the nonnegative flow cone.
\(\square\)

The earlier sequential Bellman--Ford theorem remains correct, but its
endpoint-difference costs telescope:

\[
 \sum c(u,v)=\Phi_d(F_{\rm end})-\Phi_d(F),                \tag{5.6}
\]

and `y(F')=Phi_d(F')` canonically saturates every physical reduced-cost row.
Thus its substantive content is exact lifted reachability and acceptance, not
an automatic expansion principle.  In the builder lift, pending proposal states
are deliberately not assigned fictitious factor potentials, and the union cost
is charged only at commit.

## 6. Pair and triple interaction on commuting valid subsets

There is a useful closed formula when fixed-base proposals commute and every
subset commit is at least a literal degree-two factor (it may be cap-incomplete
or disconnected).  Put

\[
 C(S)=\Phi_d(F^S)-\Phi_d(F),\qquad C(\varnothing)=0.        \tag{6.1}
\]

For two proposals define

\[
 \delta_i=C(i),\qquad
 \kappa_{ij}=C(ij)-C(i)-C(j).                              \tag{6.2}
\]

For three define the third interaction

\[
 \begin{aligned}
 \kappa_{123}={}&C(123)-C(12)-C(13)-C(23)\\
                 &+C(1)+C(2)+C(3).                        \tag{6.3}
 \end{aligned}
\]

### Theorem 6.1 (exact compound interaction criterion)

A commuting pair is a negative closed packet if and only if its simultaneous
commit passes every final gate and

\[
                   \delta_1+\delta_2+\kappa_{12}<0.        \tag{6.4}
\]

A commuting triple is a negative closed packet if and only if its simultaneous
commit passes every final gate and

\[
 \delta_1+\delta_2+\delta_3+
 \kappa_{12}+\kappa_{13}+\kappa_{23}+\kappa_{123}<0.       \tag{6.5}
\]

#### Proof

Equations (6.4) and (6.5) are Möbius inversion on the subset lattice, followed
by the definition of a negative accepted commit.  \(\square\)

Consequently individually nonnegative primitives can form a negative pair when
the union-port interaction `kappa_12` is sufficiently negative.  All three
singletons and all three pairs can be nonnegative while a triple is negative if
the genuine three-way term closes the deficit.  Resource and topology gates are
not encoded by the scalar inequalities: cap deltas must close in the literal
row map, and the port matching must give the required component/voltage state.

This interaction language must not be extended beyond its hypotheses.

* For noncommuting sequential rewrites, use ordered builder paths; subset
  notation is ambiguous.
* If a singleton is not a literal degree-two factor, `C(i)` and its Möbius terms
  have no canonical geometric meaning.  Use the atomic terminal-commit cost.
* Primitive deltas computed on separate port sets cannot be added when the
  retained paths interlace.  Lemma 4.1 must be applied to their union.

These are precisely the phenomena seen in the frozen paired and mixed faces.

## 7. The smallest bounded-packet obstruction

Cap completeness and bounded local degree do not imply a two- or
three-circuit return.

### Proposition 7.1 (minimal simple tight-cap-cycle obstruction to `s=3`)

Let four required caps `u_0,u_1,u_2,u_3` each have load one.  Primitive `q_i`
removes one unit from `u_i` and adds one unit to `u_(i+1)` (indices modulo four).
If `x_i in {0,1}` records whether `q_i` is chosen, final cap safety is

\[
                    1-x_i+x_{i-1}\ge1,                    \tag{7.1}
\]

or `x_i<=x_(i-1)` for all `i`.  Hence all four `x_i` are equal.  The only safe
packets are the empty packet and the full four-cycle.  No nonempty packet of at
most three primitives closes, even though every cap has transfer indegree and
outdegree one.

Within the family of simple unit-transfer directed cycles, this is the smallest
obstruction to `s=3`: cycles of length at most three close within the allowed
budget.  Assigning total negative abstract cost to the full four-cycle shows, at
the cap-projection builder level, that a negative long return can coexist with a
depth-three reachability obstruction (5.4).  This is not a literal residence
packet until the remaining factor/topology/trace gates and geometric
realizability are supplied.  More generally, a tight directed cycle of length
`s+1` obstructs a uniform `s`-packet theorem in this projection.

The frozen closed-packet theorem embeds the same linear phenomenon as a
Boolean-diamond exchange minor of growing support.  That embedding is a
restricted face, not a proved protected spanning-factor extension.  At the
opposite small boundary, the depth-two Middle Levels triangle is a full
no-alternative factor with positive residence debt.  These two examples show
why neither raw local degree nor Boolean geometry alone supplies regeneration.

## 8. The exact additional expansion hypothesis

For a construction class `C`, support/debt bounds `h,B`, and `epsilon>0`,
define the regenerative negative lifted radius

\[
 \begin{aligned}
 \rho^-_{C,h,B,\epsilon}(F)=\min\{|P|:
   &P\text{ is an accepted closed packet of support at most }h,\\
   &P\text{ has prefix debt at most }B,\\
   &\Phi_d(F^P)\le\Phi_d(F)-\epsilon,\\
   &F^P\in C\text{ and all declared downstream rows return}\}.
                                                               \tag{8.1}
 \end{aligned}
\]

with value infinity if no such packet exists.  This definition uses the full
row/cap/protected/topology/voltage/trace lift, not its cap projection.

### Regenerative lifted expansion `RLE(d;s,h,B,epsilon)`

For every `F in C` with `Phi_d(F)>0`, there is an accepted packet `P` such that:

1. `|P|<=s` and the changed support is at most `h`;
2. every declared prefix debt is at most `B`;
3. `Phi_d(F^P)<=Phi_d(F)-epsilon`;
4. `F^P` lies again in `C`; and
5. every downstream row needed for the final construction is either preserved
   or included literally in the accepting commit.

### Theorem 8.1 (regenerative descent)

If `Phi_d` is integer valued, `epsilon>=1`, and `RLE` holds, repeated committed
packets reach residence zero after at most
`ceil(Phi_d(F_0)/epsilon)` iterations, without changing the owner count.

#### Proof

Every commit stays in `C`, so the hypothesis reapplies.  The nonnegative integer
potential falls by at least `epsilon` at each step and therefore terminates.
At a terminal state it cannot be positive, since that would supply another
packet.  Since every prohibited short run has positive weight, zero potential
is residence zero for the declared defect family.  \(\square\)

With the same class and resource declarations, the exact
necessary-and-sufficient form of `RLE` is

\[
 \sup\{\rho^-_{C,h,B,\epsilon}(F):F\in C,\ \Phi_d(F)>0\}
       \le s.                                                \tag{8.2}
\]

A stronger, more checkable sufficient hypothesis is a closed-packet list/load
expansion: weight only packets that already satisfy items 1, 2, 4, and 5, and
require their weighted killed-token coverage to exceed the born-token load by
at least `epsilon` per unit packet weight.  Averaging then selects a packet
satisfying item 3.  Counts of raw circuits before cap, protection, topology,
and trace-return filtering do not establish this inequality.

The missing general theorem is therefore a uniform bound on **negative lifted
return**, not merely a short cycle in the owner-exchange graph or a short path
in the cap-transfer graph.

## 9. Frozen `k=17` calibration

For the lexicographic tuple `(N_+,D_+,N_0,D_0)`, the authenticated endpoints are:

| state | exact tuple |
|---|---:|
| connected `c68b` seed | `(5372,8245,8976,18938)` |
| `greedy48` | `(4199,6511,8874,18819)` |
| `paired_escape001` | `(4165,6460,8806,18632)` |
| `paired_escape002` | `(4148,6426,8636,18394)` |
| `paired_escape003` | `(4131,6392,8670,18411)` |
| `floor004` | `(4080,6290,8602,18360)` |
| `paired_escape005` | `(4029,6205,8721,18479)` |

The relevant exact finite faces are:

| carrier and face | final feasible candidates | improving candidates |
|---|---:|---:|
| `greedy48`, single endpoint-retaining quotient `C6/C8` | `30+24` connected | `0` lex-improving |
| `greedy48`, disjoint quotient `C6/C8` pairs | `2249` connected | `4` lex-improving |
| post-`escape001` strict floor after neutral-`N_+` singles, disjoint quotient pairs | `2569` connected | `17` |
| `paired_escape002`, disjoint quotient pairs | `2614` connected | `2` |
| `greedy48`, physical star-`C8` singles | `102` connected cap-complete | `0` |
| `greedy48`, physical octahedral-`C8` singles | `85` connected cap-complete | `0` |
| `greedy48`, facet-disjoint complementary oct+oct | `7038` connected cap-complete | `0` |
| `paired_escape003`, complete indexed/shared-facet star+oct | `16320` connected cap-complete | `0` |

The best `greedy48` pair is `C8+C8`.  One half alone has 19 physical
components.  The other remains connected but changes `N_+` from `4199` to
`4233`.  Their union is one cycle and reaches `4165`.  In reverse order the
component chronology is `1->1->1`, while the residence chronology is
`4199->4233->4165`.  Thus this authenticated witness requires compound
lookahead and temporary lex-primary residence debt; it does not prove that
topology debt is unavoidable.

The next best pair is a cleaner topology interaction: both constituents are
cap-safe and each has two physical components alone, while their union is one
cycle and reaches `4148`.  The following best `C6+C8` pair has standalone cap
holes `1+0` and is finally cap-safe; applying the safe half first shows that cap
debt is present in one order but is not proved unavoidable.

The physical no-go faces do not imply a three-circuit no-go.  The mixed audit
also shows why the builder must permit pending invalid singletons: among its
overlapping proposals, a duplicate incidence in one half can be removed by the
other half before the terminal literal commit.

Two provenance limits are material.

1. The full frozen round-48 pair table is not present locally, and the current
   local generator has drifted from the frozen source.  The local aggregate
   JSON and promoted witness are authenticated, but no new independent
   exhaustive-pair claim is added here.
2. The `floor004` and `paired_escape005` endpoints are independently replayed,
   but no local `paired004`/`paired005` census or patch authenticates the
   transition mechanism between them.  Equation (1.1) is an endpoint
   chronology, not a claim that every displayed arrow is a locally auditable
   two-circuit packet.

## 10. Exact implementation design before any heavy search

A proof-producing depth-three implementation should freeze the following
objects before a large run.

1. **Catalogue semantics.**  Hash the primitive generator, carrier, protected
   bank, and either the ordered transition rule or the fixed-base batch rule.
2. **Complete joins.**  State whether triples are root-active only,
   sequentially regenerated, facet-disjoint, or overlap-complete.  Use cap-debt
   and shared-facet indices only with a proof that their necessary keys are
   exhaustive.
3. **Literal builder state.**  Retain primitive keys and actual pending row
   masks.  Do not merge states on cap debt or port summaries alone.
4. **Exact commit replay.**  Recheck row existence, one facet each, owner
   degree two, protected rows, all cap multiplicities, components, voltage,
   direct residence scan, and the independent transition-gap scan.
5. **Dual output.**  If no commit is reachable, export the reachable-set cut.
   If commits exist but none is negative, export a normalized potential for
   every materialized builder arc.  A depth-two potential is not a depth-three
   certificate unless every depth-three state and arc is included.
6. **Independent reconstruction.**  Rebuild every promoted factor from the
   row patch rather than trusting cached marginal deltas.  For an exhaustive
   no-go, independently replay every emitted final row and audit completeness
   of the proposal join.
7. **Scope lock.**  Do not infer deeper-upper, source, compiler, exterior, or
   universal-word feasibility unless those literal resources were coordinates
   of the accepting commit.

This design is complete enough for an audited local implementation.  It does
not justify launching a broad upper/source/compiler campaign before the
depth-three builder, commit replay, and dual formats exist and pass on the
frozen pair fixtures.

## 11. Frozen references

The statements above are calibrated against:

* `MATH_THEOREM_A_BOOLEAN_RESIDENCE_CLOSED_PACKET_EXPANSION_AND_LIFTED_RETURN_DUALITY_20260802.md`;
* `MATH_AUDIT_K17_C68B_RESIDENCE_LOCAL_FLOORS_AND_PAIRED_TOPOLOGY_DEBT_20260802.md`;
* `MATH_AUDIT_K17_GREEDY48_PHYSICAL_STAR_C8_RESIDENCE_NOGO_20260802.md`;
* `MATH_AUDIT_K17_GREEDY48_PHYSICAL_OCTAHEDRAL_C8_SINGLE_PAIR_RESIDENCE_NOGO_20260802.md`;
* `MATH_AUDIT_K17_PAIRED_ESCAPE003_MIXED_STAR_OCTAHEDRAL_C8_PAIR_RESIDENCE_NOGO_20260802.md`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/round048.audit.json`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_c6c8.audit.json`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired002.audit.json`;
* `scratch/h3_k17_paired_escape003_independent_20260802/paired003.audit.json`;
* `scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.audit.json`;
* `scratch/k17_greedy48_physical_octahedral_c8_20260802/pc8_oct_single.audit.json`;
* `scratch/k17_greedy48_physical_octahedral_c8_pairs_20260802/pc8_oct_pairs.audit.json`;
* `scratch/k17_paired_escape003_physical_mixed_c8_pairs_20260802/pc8_mixed_escape003.audit.json`; and
* `scratch/k17_marker58_residence_round2_20260802/paired_escape005.residence.audit.json`.

The numerical table and the finite `C4` calculation are independently rebound
by `scratch/audit_k17_compound_packet_builder_design_20260802.py`, with frozen
output in `scratch/k17_compound_packet_builder_design_20260802.audit.json`.

No SSH, remote read, solver launch, C/C++ compilation, or new exhaustive
enumeration was used in deriving this formulation.
