# K17 h1 full-q1 strict-Pareto compound-fan theorem

**Date:** 2026-08-02  
**Status:** exact theorem with an independently authenticated endpoint at
`(R,D)=(1948,1761)` in both openings.  The finite depth-three/depth-four
actuator design is hash-bound below, but no search output is yet promoted by
this document.  It therefore asserts neither a finite witness nor an
exhaustive bounded-depth obstruction.

## 0. Frozen endpoint and actuator design

The authenticated endpoint is `checkpoint_joint_res1948_deep1761`.  The
independent freeze reports:

```text
model       daee344e2a85a757657ee380e3ab6d66ed8b5f2bf61e3e6c69bd81ba146dae1e
passive     b68460b63f8d9b03e05915e5b275704e742d66b7fc6d15d477348e60bd4a47fc
independent 1295f30545d5b1a88bce0516620a57f3bc5c51ada58741849e71d39588f8e5be
manifest    cec59a55725aafed927b15ec4c2f34936c3f8e9aaa0d2f3245c3fed9b68cd2a7
```

Both openings have residence `1948`, deeper count `1761`, and rank-10-through-
17 hole vector

```text
[0,1497,261,3,0,0,0,0].                                 (0.1)
```

The independent endpoint replay passes full q1, frozen guards, exact degrees
and normalized boundary, and connected topology.  Direct parent/child opening
comparison has zero literal upper-deck losses.  The endpoint equals the final
three `B+C+D` promotions.  A selected-batch TSV in the manifest also lists an
earlier `A` row and is overinclusive as a displacement provenance record;
therefore that TSV is not used here to authenticate the endpoint lineage.

The reviewed finite actuator is

```text
scratch/k17_h1_joint_res1948_compound_20260802/
  search_k17_joint1948_phi_overlap_depth34_20260802.cpp
SHA-256 9858281810547337715c9785e9a48fee20e9c270cf81efd8e9c8529c806c2a40
```

It passed independent source review for a sampled **strong-face** run only
when `require_prefix_deck_containment=1` and the symmetric root arguments are
`1948,1948,1761,1761`.  Flag zero instead implements the weaker terminal-debt
semantics of Section 1.1.  A sampled miss is not a cut, and its
`min_witness_depth` parameter is a threshold rather than a proof of global
minimum depth.

## 1. Hard state, overlap, and closed packets

Let `X` be the exact hard face.  A state in `X` retains the materialized
factor together with every coordinate needed to decide the next move:

```text
(selected incidences, rebuilt pair variables, frozen guards,
 ordinary and opened full-q1 provider rows, exact facet/owner/cap rows,
 protected incidences, connected topology, opening histories,
 port/cap/topology debts, terminal-closure tickets, R, D).
```

Here `R` is residence and `D` is the declared deeper-upper objective.  Both
are nonnegative integers.  Any history or ticket not injectively determined
by the factor is a genuine state coordinate.  Aggregate objective values or
root labels alone are not a Markov-complete quotient.

At an actual tail `F`, a primitive schema gives a signed incidence vector
`z in {-1,0,1}^E`, negative on selected deletions and positive on unselected
insertions.  It is an arc only when

```text
F' = F+z is Boolean, the circuit is alternating at F, and F' is in X.  (1.1)
```

The complete declared primitive catalogue is regenerated at every retained
tail.  Supports may overlap.  Thus this graph strictly contains a
root-disjoint batch graph unless the complete catalogue itself proves that
all overlaps are redundant.

An ordered packet is a path

```text
F_0 -> F_1 -> ... -> F_t.                               (1.2)
```

It is **strict-prefix legal** when every `F_i` lies in `X`.  It is **closed**
when the terminal tickets and exposed ports have their declared zero/accepting
values.  Closed does not mean `F_t=F_0`; the factor must change if either
objective changes.

Write `q_i` for the support of `z_i` modulo two.  The endpoint cycle-space
projection is

```text
y(F_t)=y(F_0) xor q_1 xor ... xor q_t.                  (1.3)
```

Repeated incidences therefore cancel in the projection.  Equation (1.3)
preserves every linear parity ledger satisfied by the circuits, but it does
not decide Boolean occupancy, nonlinear provider rows, connectivity, or
prefix legality.  Those are exactly why (1.2), rather than only its XOR, is
the proof object.

### 1.1 Literal upper-deck containment in both openings

For opening `o in {0,1}`, let `C_o(F)` be the literal set of upper targets
covered by the opened chronology of `F`, retaining target identities rather
than only their rank counts.  There are two proof-safe semantics, and an audit
must name which one it uses.

The **strong prefix-containment face** requires

```text
C_o(F_0) subseteq C_o(F_i)       for o=0,1 and every prefix i. (1.4)
```

Equivalently, for every initially covered target `U`, the fixed-ticket row is

```text
chi_(o,U)(F_i)=1[U in C_o(F_i)] = 1                     (1.5)
```

at every prefix.  An audit can express the same condition as

```text
|C_o(F_0) \ C_o(F_i)|=0.                                (1.6)
```

It must materialize or hash-check the literal target bitset; rank histograms
alone cannot establish (1.4).

The weaker **terminal-containment debt face** allows temporary losses but
retains the exact lost-target ticket

```text
B_o(F_i)=C_o(F_0) \ C_o(F_i)                             (1.6a)
```

in every lifted state and accepts only when

```text
B_0(F_t)=B_1(F_t)=empty.                                 (1.6b)
```

It does not certify prefix containment.  A terminal-debt witness cannot be
reported as a strong-face witness even if the same terminal happens to pass
(1.4).

For every rank `r`, (1.4) implies

```text
h_(o,r)(F_i) <= h_(o,r)(F_0),                            (1.7)
```

and hence it implies nonincrease of every declared deep-hole sum.  The
converse is false.  A state can lose one previously covered target and gain
two different targets of the same rank, improving the hole count while
violating (1.4).  Thus two-opening literal containment is strictly stronger
than per-rank or aggregate deep nonincrease.  In terminal-debt mode this
implication applies only at `F_t`; intermediate rank counts may rise or fall.

## 2. Exact terminal commit at the joint root

Fix the delegated root values

```text
R_0=1948,             D_0=1761,             R_0+D_0=3709. (2.1)
```

For a terminal state put

```text
dR=R-R_0,             dD=D-D_0.                         (2.2)
```

The requested strict Pareto commit is exactly

```text
dR <= 0,              dD <= 0,              dR+dD <= -1. (2.3)
```

The last inequality is equivalent to “at least one coordinate is strict”
because the objectives are integral.  Hence no lexicographic convention is
hidden in (2.3).

Define the root-anchored scalar

```text
M = R_0+D_0+1 = 3710,
J_0(F) = M((dR)_+ +(dD)_+) + dR+dD,       x_+=max(x,0). (2.4)
```

### Theorem 2.1 (exact scalarization of the Pareto corner)

For every state with nonnegative integer `R,D`,

```text
J_0(F)<0    if and only if    F satisfies (2.3).         (2.5)
```

#### Proof

If `dR,dD<=0`, the penalty in (2.4) vanishes, so `J_0=dR+dD`;
negativity is exactly the strict inequality in (2.3).

If `dR>=1`, then `dD>=-D_0`, and therefore

```text
J_0 >= M+1-D_0 = 1950 > 0.                              (2.6)
```

If `dD>=1`, similarly

```text
J_0 >= M+1-R_0 = 1763 > 0.                              (2.7)
```

These bounds also cover the case in which both increments are positive.
Thus a state outside the nonpositive quadrant cannot have negative `J_0`,
which proves (2.5).  \(\square\)

The large value `3710` is a convenient safe choice, not a claim of a minimal
big-M constant.

### 2.1 Two-opening OR target used by the finite actuator

If residence and deep counts are retained separately in the two openings,
write their root values as `(R_(o,0),D_(o,0))`.  Put

```text
M_or = 1+max_(o=0,1)(R_(o,0)+D_(o,0)),
J_open,o(F)=M_or((dR_o)_+ +(dD_o)_+) + dR_o+dD_o,
J_or(F)=min(J_open,0(F),J_open,1(F)).                    (2.8)
```

When both root pairs are `(1948,1761)`, `M_or=3710`.  Applying Theorem 2.1
opening by opening gives

```text
J_or(F)<0
iff there exists o with dR_o<=0, dD_o<=0, dR_o+dD_o<=-1. (2.9)
```

Thus the exact terminal predicate for that actuator is the conjunction of
(2.9) with literal deck containment in **both** openings.  The minimum in
(2.8) encodes an OR of two Pareto corners; it does not claim strict Pareto
improvement in both openings.  If the latter is desired, all four coordinate
increments must be put in one four-coordinate positive-part scalar instead.

On a finite lifted graph `J_or` is simply a node value, so using

```text
c(u,v)=J_or(v)-J_or(u)                                   (2.10)
```

retains the telescoping min-cost/Bellman--Ford theorem below.

## 3. Exact bounded-state fan and the BF/Farkas alternative

Fix a physical depth `L`.  Form the layered graph `Gamma_L(F_0)` whose
vertices are the Markov-complete hard states `(i,F)` reachable after exactly
`i<=L` primitive moves.  Add only state-relative arcs satisfying (1.1).
From every nonroot **closed** state add a zero-cost analytic arc to a sink
`tau`; analytic arcs do not consume physical depth.

Give every physical arc `u->v` the cost

```text
c(u,v)=J_0(v)-J_0(u).                                   (3.1)
```

Costs telescope.  Since `J_0(F_0)=0`, every source-to-sink path ending at
`F` has cost exactly `J_0(F)`.

Let `N` be the head-minus-tail node-arc incidence matrix, `s=(0,F_0)`, and
`b=e_tau-e_s`.  Define

```text
mu_L = min {c^T f : Nf=b, f>=0}.                        (3.2)
```

### Theorem 3.1 (strict compound fan)

If `tau` is reachable, (3.2) has an integral path optimum and

```text
mu_L<0                                                        (3.3)
```

if and only if the exact depth-`L` fan contains a strict-prefix-legal closed
packet satisfying (2.3).

Equivalently, add a zero-cost reset arc `rho:tau->s`, require circulation,
and fix `f_rho=1`.  The fixed reset is necessary: without it the zero
circulation is feasible, and a negative accepting cycle can be scaled.

#### Proof

The physical graph is layered and acyclic.  Its unit-flow polytope is a
network polytope and hence integral.  A path cost is its terminal `J_0` by
telescoping.  Theorem 2.1 identifies negative cost with (2.3).  Adding or
deleting the fixed unit reset gives the normalized-circulation equivalence.
\(\square\)

### Theorem 3.2 (exact local certificate)

Exactly one applicable case holds.

1. If `tau` is unreachable and `S` is the source-reachable set, no arc leaves
   `S`.  The vector `z=-1_S` satisfies

   ```text
   N^T z <= 0,                 b^T z = 1,                (3.4)
   ```

   which is a Farkas certificate that (3.2) is infeasible.
2. If `tau` is reachable and `mu_L<0`, an integral strict compound packet
   exists.
3. If `tau` is reachable and `mu_L>=0`, there is a Bellman--Ford potential
   `pi` satisfying

   ```text
   pi[v]-pi[u] <= c(u,v),
   pi[tau]-pi[s] = mu_L >= 0.                            (3.5)
   ```

   It certifies that every closed packet in the exact enumerated fan is
   nonnegative.

For this telescoping graph an explicit optimal dual is

```text
pi(F)=J_0(F),              pi(tau)=min_closed J_0.       (3.6)
```

Physical inequalities in (3.5) are equalities, and every sink inequality is
`pi(tau)<=J_0(F)`.  Thus an exhaustive frozen node/arc list plus its minimum
terminal value is already a compact proof of the bounded local cut.

#### Proof

For (3.4), no arc leaves the reachable set.  With the head-minus-tail
convention, every arc has dot product at most zero with `z`, whereas
`(e_tau-e_s)^Tz=1`; a feasible unit flow would give `1<=0`.  The other cases
are network integrality and primal--dual alternatives for (3.2).  Equation
(3.6) follows directly from (3.1).  \(\square\)

## 4. What depth three and depth four mean

Let `mu_l` use analytic sink arcs from every closed state in layers
`1,...,l`, with the convention `mu_l=+infinity` when none is reachable.
Then `mu_l` is nonincreasing in `l`.  “Every root primitive is blocked” has
the precise objective meaning

```text
mu_1 >= 0.                                                (4.1)
```

It says nothing by itself about `mu_2,mu_3,mu_4`.

A globally minimal strict triple is certified by

```text
mu_2 >= 0 > mu_3.                                        (4.2)
```

Its own ordered prefixes necessarily have

```text
J_0(F_1)>=0,           J_0(F_2)>=0,           J_0(F_3)<0. (4.3)
```

A globally minimal strict quadruple is certified by

```text
mu_3 >= 0 > mu_4,                                        (4.4)
```

and its three proper prefixes have nonnegative `J_0`.  Conditions (4.2) and
(4.4) are stronger than checking only the prefixes of one displayed witness:
they rule out every shorter path in the declared exhaustive fan.

There are two different senses in which a constituent can be root-blocked.

* It is **objective-blocked** when its root arc exists but its root endpoint
  has nonnegative `J_0`.
* It is **activation-blocked** when no root arc exists, but a preparer can
  make that schema alternating and hard-legal at a later state.

In the strong phrase “every constituent alone is blocked,” each constituent
must merely lack a negative hard-legal root singleton.  At least the first
constituent of any strict-prefix packet must still have a hard-legal root
arc.  If every primitive is activation-blocked at the root, no ordered packet
can start.

## 5. Exact provider and activation inequalities

Let `P(U)` be the exact provider family for a required positive row `U`.
Providers may be quadratic pair variables or higher typed monomials.  Put

```text
n_U(F)=sum_(p in P(U)) 1[p is live at F].                (5.1)
```

Full coverage of `U` is the cut `n_U(F)>=1`.  On transition `i`, define the
state-relative sets

```text
L_(U,i)={p:p live at F_(i-1), p dead at F_i},
G_(U,i)={p:p dead at F_(i-1), p live at F_i}.             (5.2)
```

Then the exact prefix ledger is

```text
n_U(F_i)=n_U(F_0)
          +sum_(j<=i)(|G_(U,j)|-|L_(U,j)|) >= 1          (5.3)
```

for every required row `U` and every physical prefix `i`.  Because (5.2)
uses state transitions, a provider that disappears and later returns is
charged once in each direction; there is no double counting.

For a fixed schema `B`, let `B^-` be its required selected deletions and
`B^+` its required unselected insertions.  Its exact occupancy deficit is

```text
a_B(F)=sum_(e in B^-)(1-y_e(F)) + sum_(e in B^+)y_e(F).  (5.4)
```

Subject to its static geometry, `B` is alternating at `F` exactly when
`a_B(F)=0`.  A preparer path activates `B` when it drives (5.4) to zero while
maintaining (5.3) and every other hard row.

### Lemma 5.1 (multi-preparer provider handoff)

Let `A_1,...,A_r,B`, with `r+1<=L`, be state-relative primitives.  Suppose:

1. every preparer prefix is in `X` and satisfies (5.3);
2. after the preparers, `a_B=0` and the head of `B` is in `X`;
3. all terminal tickets close; and
4. the terminal has `J_0<0`.

Then `A_1;...;A_r;B` is an accepted strict compound packet.  This remains
true when `B` has no root arc and when the supports overlap.

Conversely, within the declared fan, every accepted packet whose last move is
`B` necessarily satisfies these four conditions.  Thus (5.3)--(5.4), plus
the remaining hard-state predicates, are the exact depth-three/depth-four
test; “provider handoff” is a mechanism, not an extra relaxation.

#### Proof

Conditions 1--2 are precisely prefix and terminal hard legality, condition 3
is terminal acceptance, and Theorem 2.1 converts condition 4 to the strict
joint objective.  Necessity follows by reading the corresponding coordinates
of any accepted lifted path.  \(\square\)

A useful sufficient special case starts with a last provider `p_old`.  The
preparers keep `p_old` live while planting all missing halves of a replacement
`p_new`; the final move may then delete `p_old` because `p_new` is live.  For
quadratic `p=y_a y_b`, planting the two halves in different preparers is a
genuine depth-three/depth-four phenomenon invisible to a root-only provider
count.

### 5.1 Exact prefix topology cuts

Let `H(F_i)=(V,E_i)` be the complete selected incidence graph at prefix `i`.
Connectivity is not a terminal-only row.  It is equivalent to the graphic
matroid rank condition

```text
rank_graphic(E_i)=|V|-1,                                 (5.5)
```

or, exactly, to all nontrivial shore inequalities

```text
k_W(F_i)=sum_(e in delta(W)) y_e(F_i) >= 1
for every empty != W != V and every prefix i.            (5.6)
```

For transition `j`, let `A_(W,j)` and `L_(W,j)` be the numbers of crossing
incidences inserted and deleted at the actual tail.  Then

```text
k_W(F_i)=k_W(F_0)
          +sum_(j<=i)(A_(W,j)-L_(W,j)) >= 1.             (5.7)
```

Equation (5.7) is the exact topology-debt ledger.  It must be checked for all
shores and all ordered prefixes, just as (5.3) must be checked for every
provider row.

Singleton safety and incidence-disjointness do not imply (5.7).  Singleton
safety gives only

```text
k_W(F_0)+A_(W,j)-L_(W,j) >= 1             for each j,    (5.8)
```

whereas a batch needs the sum in (5.7).  For example, a shore with four
selected crossing incidences can meet two support-disjoint circuits, each of
which internalizes two different crossing incidences and inserts none across
that shore.  Each singleton leaves cut value two and can remain connected,
but their composition leaves cut value zero and disconnects the two shores:

```text
4-2=2,                 4-2=2,                 4-2-2=0.  (5.9)
```

This cut pattern is realized by degree-preserving alternating switches, not
just by arbitrary edge deletion.  For one switch on bipartite vertices
`x_1,x_2` and `y_1,y_2`, put `x_1,y_2` in `W` and `x_2,y_1` outside.  The old
edges `x_1y_1,x_2y_2` cross the shore, while the new edges
`x_1y_2,x_2y_1` are internal, one on each side.  A vertex-disjoint second
switch has the same effect on two other crossing edges.  If both shore
interiors are connected, each singleton graph is connected and their union
of switches has exactly the two shore components.

Disjoint supports prevent two circuits from toggling the same incidence; they
do not prevent their distinct deleted incidences from lying in the same
global cut.  Equivalently, connectivity belongs to the graphic-matroid rank
state, not merely to the binary cycle-space projection (1.3).

Thus, if an authenticated six-circuit attempt is connected through prefix
five and its sixth head has exactly two components, the rejecting certificate
is a shore `W` equal to one component with `k_W(F_6)=0`.  The sixth schema is
not an arc at that tail even if it is singleton-safe at the root.  This
rejects that ordered batch only; the audit should freeze `W` and every prefix
value in (5.7).  It does not prove that every ordering or every overlapping
repair packet is blocked.

A strong sufficient composition rule is to preserve one common spanning tree
through every prefix.  The exact, less restrictive rule is (5.7), which may
spend cut slack only after another circuit has restored it.

### 5.2 Saturated-chain criterion for commuting columns

Suppose `m` fixed circuit columns have commuting, support-disjoint toggles and
remain alternating whenever any of the other columns have been applied.  For
`I subseteq [m]`, let

```text
F_I=F_0 xor (xor_(j in I) q_j),
A={I:F_I satisfies the complete declared hard state}.   (5.10)
```

The family `A` includes the chosen containment semantics and all provider,
topology, protection, and ticket rows; it is not merely an incidence-feasible
set system.

### Lemma 5.2 (exact disjoint-column packet test)

A set `I` can be committed as an ordered strict-prefix packet using each of
its columns once if and only if the directed Hasse graph of `A` contains a
saturated chain

```text
empty=I_0 subset I_1 subset ... subset I_t=I,
|I_j\I_(j-1)|=1.                                        (5.11)
```

It is a strict objective packet exactly when its terminal additionally has
negative `J_0` (or negative `J_or` for the two-opening OR target).

#### Proof

An ordering of the columns has prefix supports `I_0,...,I_t`; strict-prefix
legality is exactly membership of every one of these subsets in `A`.
Conversely, the unique added element on every Hasse arc supplies the circuit
order.  Commutation makes `F_I` independent of the chosen order.  The final
scalar condition is Theorem 2.1 or (2.9).  \(\square\)

Consequently, feasibility of all singletons and of the terminal XOR does not
by itself prove a packet when `|I|>=3`: the necessary intermediate subsets
may be absent from `A`.  The smallest abstract pattern is

```text
A={empty,{1},{2},{3},{1,2,3}},                           (5.12)
```

which has safe singletons and a safe terminal but no saturated chain to the
terminal.  Provider rows and topology cuts can remove such intermediate
subsets.  For topology specifically, subset `I` must satisfy every inequality

```text
k_W(F_0)+sum_(j in I)(A_(W,j)-L_(W,j)) >= 1.             (5.13)
```

This Boolean-lattice reduction is valid only for commuting fixed columns.
Activated or overlapping schemas are order-dependent and must remain in the
full lifted-state graph of Section 3.

## 6. Why an unlifted two-resource flow is not exact

For an **integral path**, telescoping edge increments give the exact terminal
constraints

```text
sum_e dR_e f_e <= 0,
sum_e dD_e f_e <= 0,
sum_e(dR_e+dD_e)f_e <= -1.                               (6.1)
```

Adding (6.1) directly to a fractional unit-flow relaxation can destroy
integrality.  The smallest pattern has two parallel terminal branches with
increments

```text
(-2,+1)             and             (+1,-2).             (6.2)
```

Neither endpoint is Pareto accepted, but half a unit on each path has average
`(-1/2,-1/2)` and satisfies all three inequalities in (6.1).  Therefore a
scalar Hall projection or a side-constrained unlifted flow is not a proof of
an accepting path.

There are two proof-safe formulations:

1. retain endpoint coordinates in the state and connect the sink only from
   states satisfying (2.3), reducing the question to exact reachability; or
2. use the scalar (2.4) on the ordinary integral min-cost network (3.2).

## 7. Finite escape versus uniform regeneration

The inequality `mu_L(F_0)<0` proves one finite packet at one root.  It does
not imply that the same schemas, providers, or accepting fan survive at its
endpoint.

Let `Y subseteq X` be closed under committed packet endpoints and let `T` be
a declared terminal family.  The exact additional expansion hypothesis is

```text
for every F in Y\T reachable by commits,
the freshly regenerated Gamma_L(F) has mu_L^F<0,          (7.1)
```

where `J_F` is rebuilt from the current `(R(F),D(F))`, not kept anchored at
the original root, and the analytic sink is attached only to closed endpoints
in `Y`.  State completeness, hard legality of every physical prefix, ticket
closure, endpoint return to `Y`, and the same uniform depth `L` are part of
(7.1).

The literal deck anchor must also be rebased at every commit.  If committed
states are `F^(0),F^(1),...`, renewal requires

```text
C_o(F^(n)) subseteq C_o(F^(n+1))       for o=0,1.        (7.1a)
```

In strong mode the same current-anchor containment holds at every physical
prefix of commit `n+1`; in terminal-debt mode it need hold only at that
commit's terminal.  Keeping only the original `C_o(F^(0))` anchor would allow
a later packet to discard targets gained by an earlier packet and therefore
would not prove regenerative literal containment.  The two current anchor
bitsets are consequently part of the renewal state.

### Theorem 7.1 (regenerative strict-Pareto descent)

Under (7.1), repeated commits reach `T`.  If `R_min,D_min` are valid lower
bounds on `Y`, at most

```text
(R(F_0)-R_min)+(D(F_0)-D_min)                            (7.2)
```

committed packets occur before arrival.

#### Proof

Every regenerated packet is coordinatewise nonincreasing and decreases at
least one integral coordinate.  Hence `R+D` falls by at least one per commit
and is bounded below by `R_min+D_min`.  An infinite sequence outside `T`
would contradict (7.2).  \(\square\)

The smallest counterexample to deriving renewal from one finite witness has
two macro-states: `F` has one strict packet to `F'`, while `F'` is hard-legal
but has no accepting outgoing packet.  Thus no theorem confined to the fan at
`F` can prove (7.1).  Endpoint closure and uniform freshly regenerated
negative expansion are the exact missing hypotheses.

## 8. Required finite calibration and exclusions

Section 0 completes the canonical-root authentication.  To promote a
**positive** depth-three/depth-four result at `(1948,1761)`, a new freeze must
add the ordered packet, every independently replayed prefix, the terminal
model/full-formula audit, the chosen containment mode, and a stable manifest
hashing them.  Every prefix replay must include all provider values (5.3),
topology, protection, and tickets, plus either strong containment (1.4) or the
exact debt bitsets (1.6a) with terminal closure (1.6b).

A **negative local cut** needs strictly more: the exact primitive-catalogue
scope, a Markov-complete node list and complete state-relative arc list through
the declared depth, and the exhaustive reachable cut/potential (3.4)--(3.6).
A sampled miss supplies none of that completeness.

No source antecedent, compiler, universal word, completeness beyond a
properly frozen declared primitive/depth fan, or uniform regenerative
expansion is asserted.
