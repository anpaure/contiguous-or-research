# Boolean residence repair by closed packets: expansion, return duality, and the sharp supply obstruction

**Date:** 2026-08-02  
**Lane:** A, pure mathematics with authenticated `k=17` calibration  
**Status:** exact conditional descent theorem and exact min--max obstruction.
The unconditional bounded-`C6/C8` monotone-supply assertion is false.  No
all-dimension existence theorem is claimed.

## 1. Result and scope

Let `F` be an exact Boolean-diamond factor: every middle owner has degree two,
every lower facet is used once, every required immediate-upper cap is covered,
and a named protected row bank is fixed.  Residence repair cannot in general be
performed by one connected, cap-safe `C6` or `C8`; the small exact factor in
Section 5 already refutes such an unconditional assertion.  At a genuinely
large Boolean state, the authenticated `k=17` round-48 factor closes the
complete **endpoint-retaining directed** single-`C6/C8` face: it contains no
move decreasing the lexicographic positive-run potential.  Nevertheless two
`C8`s in that class form a closed packet and give

\[
 (N_+,D_+,N_-,D_-)
   =(4199,6511,8874,18819)
       \longmapsto(4165,6460,8806,18632).                 \tag{1.1}
\]

Here `N_+` and `N_-` count positive and zero runs of length at most three, and
`D_+`, `D_-` are their total depth-three deficits.  For this authenticated
endpoint-retaining escape, the correct atom is a **closed circuit packet**, not
an individually monotone circuit.  A proof-safe general supply theorem must
therefore allow such packets.

This note proves three reusable statements.

1.  An exact weighted packet-expansion inequality is sufficient, and in its
    unrestricted weighted form equivalent, to the existence of a decreasing
    closed packet.
2.  A finite lifted return automaton has an exact alternative: either it has a
    decreasing accepting path or it has a Bellman--Ford/Farkas potential
    certifying that every allowed return costs at least the causal gain.
3.  A uniform bounded low-cost return hypothesis, regenerated after each
    packet, gives monotone owner-count-neutral residence descent.  This is the
    weakest proof-safe all-`k` supply hypothesis isolated here.

The note also proves that cap completeness and bounded local degrees do not
imply bounded return length, even in a Boolean-diamond exchange minor.

The fixed-host nonflat escape is closed independently: its exact all-cut value
is `G_2=36`, whereas scalar feasibility needs `G_2>=20610`, and the forced loss
is at least `48548>7401`.  Consequently the causal move in any future supply
theorem must rethread an actual short-run cluster.  Exporting deadline
particles from that fixed chronology cannot satisfy the hypothesis below.

Deep upper shadows, source binding, the terminal compiler, and an exterior
linearization are preserved only if their literal resources are included in
the accepting state.  Residence descent by itself does not settle them.

## 2. Protected factors, packets, and exact defect tokens

Fix a depth `d`.  A protected factor state records:

* its selected phase-labelled Boolean-diamond rows;
* the owner degrees and lower-facet multiplicities;
* the immediate-upper cap loads `M_F(U)`;
* the protected rows;
* the retained-path endpoint involution, quotient components and voltages; and
* the signed coordinate traces in every changed finite-port collar.

A **primitive circuit** is a state-relative alternating `C6` or `C8` whose
new rows are legal Boolean-diamond rows.  A **packet**

\[
                    P=(Q_1,\ldots,Q_t)                    \tag{2.1}
\]

is an ordered sequence of applicable primitive circuits.  It is
`(s,B)`-closed if:

1. at most `s` primitive circuits are used and the prescribed support guard is
   obeyed;
2. every prefix is owner/facet-exact inside the declared temporary resource
   envelope, and every temporary cap or other resource debt is explicitly
   stored;
3. the final state has exact owner degrees and lower palette, fixes the
   protected bank, has `M_{F^P}(U)>=1` for every required cap, and has no more
   component debt than `F` (with the required final lift voltage); and
4. this displayed order has temporary component excess at most `B`.

Cap-multiset preservation is a useful sufficient condition, but is not part
of the definition.  Prefix cap holes may also be allowed if their complete
labelled debt is stored in the temporary state and discharged at the end.

Fix one positive weight function on the state-independent universe of all
physical trace-component tokens.  A nonconstant component token is labelled
by its coordinate, sign, and unoriented bracket owner-edge sequence.  If a
temporarily disconnected factor component is constant in that coordinate,
use instead a **whole-component token**, canonically labelled by the unoriented
cyclic edge sequence of that component.  Weights depending only on sign and
length are a special case.  For every coordinate and sign, distinguish cyclic
short-run occurrences by these labels.  Let `D(F)` be the resulting multiset
of occurrences of length at most `d`.  Put

\[
                  \Phi_w(F)=\sum_{\omega\in D(F)}w_\omega. \tag{2.2}
\]

Compare `D(F^P)` and `D(F)` in the common occurrence-labelled universe and
cancel equal tokens.  Write `K(P)` for the remaining killed multiset and
`B(P)` for the remaining born multiset, and extend `w` additively to such
multisets.

### Lemma 2.1 (finite-port exactness)

If a packet changes the old adjacency set `J`, every old run bracket whose
complete adjacency subpath avoids `J` survives unchanged.  An old
whole-component token also survives if its component avoids `J`.  Every killed
or born token meeting `J` is determined exactly by the retained trace
components incident with the cut ports and by the old and new port matchings.
This includes whole-component tokens created or destroyed when components
split or join.  Hence

\[
 \Phi_w(F)-\Phi_w(F^P)=w(K(P))-w(B(P)).                  \tag{2.3}
\]

#### Proof

Deleting `J` cuts each signed trace into retained constant-trace intervals.
An uncut constant component stays as its canonical whole-component token.
No other trace boundary can change.  Adding the new adjacencies joins the cut
intervals according to the new port matching.  The lengths and signs of all
new components, including a newly constant whole cycle, are therefore the
sums of their retained interval weights.
Cancel the components joined identically before and after.  The uncancelled
old and new components are exactly `K(P)` and `B(P)`, which gives (2.3).
\(\square\)

The lemma must be applied to the **union** of the packet ports.  Summing
independently computed primitive deltas is not valid when two circuits
interlace along a retained component.

## 3. The exact packet-expansion inequality

Let `P_{s,B}(F)` be any finite catalogue of `(s,B)`-closed packets.  Give its
members nonnegative weights `lambda_P`.  Define the killed coverage and born
load

\[
 a_\omega=\sum_P\lambda_P\,\operatorname{mult}_{K(P)}(\omega),
 \qquad
 b_\eta=\sum_P\lambda_P\,\operatorname{mult}_{B(P)}(\eta). \tag{3.1}
\]

### Theorem 3.1 (weighted closed-packet expansion)

If

\[
       \sum_{\omega\in D(F)}w_\omega a_\omega
       >\sum_\eta w_\eta b_\eta,                         \tag{3.2}
\]

then some `P in P_{s,B}(F)` satisfies

\[
                         \Phi_w(F^P)<\Phi_w(F).           \tag{3.3}
\]

Conversely, if (3.3) holds for one packet, (3.2) holds by taking its catalogue
weight to be one and all other weights zero.  Thus (3.2), with arbitrary
packet weights, is an exact existence criterion rather than a probabilistic
relaxation.

#### Proof

By Lemma 2.1,

\[
\begin{aligned}
 \sum_P\lambda_P\bigl(\Phi_w(F)-\Phi_w(F^P)\bigr)
   &=\sum_\omega w_\omega a_\omega-
     \sum_\eta w_\eta b_\eta.
\end{aligned}                                             \tag{3.4}
\]

The right side is positive, so at least one summand with positive packet
weight is positive.  The converse is immediate.  \(\square\)

### Corollary 3.2 (list/load row)

For the same nonnegative packet weighting `lambda` as in (3.1), suppose a
proof-safe enumeration gives nonnegative bounds

\[
                 a_\omega\ge L_\omega,
       \qquad   b_\eta\le U_\eta.                         \tag{3.5}
\]

where `eta` ranges over the finite born-token union.  Then the deterministic
inequality

\[
       \sum_{\omega\in D(F)}w_\omega L_\omega
       >\sum_\eta w_\eta U_\eta                          \tag{3.6}
\]

forces a decreasing packet.

The lower list `L_omega` must already subtract protected-row conflicts,
critical-cap failures, incompatible port states, and unavailable topology
returns.  A lower bound on raw Boolean circuit degree alone is not (3.5).

### Proposition 3.3 (a Robin--Hood sufficient subclass)

Assume the union port matching of a closed packet changes each affected
signed run-length vector by pairwise-disjoint transfers, or by a sequential
T-transform decomposition in which every step satisfies

\[
              (a,b)\longmapsto(a+t,b-t),
       \qquad a\le d,\quad b-t\ge d+1,\quad t>0,          \tag{3.7}
\]

and leaves every other run length unchanged.  Then the packet strictly
decreases

\[
       \Phi_d(F)=\sum_{x,\sigma}\sum_{R}
                   (d+1-|R|)_+.                          \tag{3.8}
\]

#### Proof

At each disjoint or sequential step, the long run remains outside the deficit
range.  The short run's deficit drops from `d+1-a` to
`(d+1-a-t)_+`, a positive decrease.  Sum over the valid decomposition.
\(\square\)

This subclass is deliberately stronger than Theorem 3.1.  The authenticated
paired escape uses compensated, interlaced port changes and need not decompose
into independently legal Robin--Hood primitives.

## 4. The lifted return theorem and its exact dual

Raw expansion does not say whether a causal defect-killing primitive can be
closed.  The correct object is a lifted state graph.

Fix `F`, a support/length envelope, and all resources which must hold at the
end.  Let `Gamma_F` be the finite directed graph whose vertices contain enough
information to make the next primitive and its exact delta Markovian:

* the actual changed row map (or an equivalent injective encoding);
* the residual step/support budget, cumulative used-row guard, and peak
  topology debt;
* current scarce-cap loads and any explicit backup tickets;
* the protected-row guards;
* the retained-path pairing, component and voltage state; and
* the signed finite-port trace state, including all open run ages.

If deeper upper targets or compiler cells are required, their current loads
are also coordinates of the vertex.  An arc is one applicable primitive
circuit, and its cost is

\[
                  c(u,v)=\Phi_w(F_v)-\Phi_w(F_u).         \tag{4.1}
\]

Use a layered graph, with the layer equal to the number of primitives already
used, so every path obeys the fixed length envelope even if the same residual
resource state recurs.  Let `s` be the unchanged state `F`, and let `A` be
the accepting states whose
final owner, facet, cap, protected, topology and optional extra rows are all
valid.  Trim the graph to vertices reachable from `s` and able to reach an
accepting state, and replace `A` by the accepting vertices surviving the trim.

### Theorem 4.1 (rooted return alternative)

Exactly one of the following holds.

1. There is an `s`-to-`A` path of negative total cost.  Its primitive sequence
   is a decreasing closed packet.
2. There is a real potential `pi` on the trimmed vertices such that

   \[
       c(u,v)+\pi(u)-\pi(v)\ge0                           \tag{4.2}
   \]

   for every physical arc and

   \[
                         \pi(a)\ge\pi(s)                  \tag{4.3}
   \]

   for every `a in A`.

The second alternative is an exact obstruction, not merely a sufficient
certificate.

#### Proof

Add a zero-cost analytic reset arc `a -> s` for every accepting state.  The
physical layered graph is acyclic, so every directed cycle in the augmented
graph uses at least one reset.  Decompose such a cycle at its reset arcs into
`s`-to-`A` paths.  Its total cost is the sum of their costs, so a negative
cycle contains a negative accepting path.  Conversely, one negative accepting
path followed by its reset is a negative cycle.

The standard finite no-negative-cycle potential theorem gives (4.2) on the
physical arcs.  Its inequality on `a -> s` is exactly (4.3).  Conversely,
summing (4.2) along a path and using (4.3) proves that every accepting path
has nonnegative cost.  \(\square\)

The theorem remains sound after quotienting states only when the quotient is
Markov-sufficient for every listed resource and for (4.1).  A cap-only or
component-only quotient cannot certify residence, because it forgets the
retained trace intervals which create nonlinear cross terms.

### Corollary 4.2 (bounded causal breaker and return)

Suppose that whenever `Phi_w(F)>C`, there is a primitive causal breaker
`q:s->v` with cost `-g<0` which cuts an adjacency of an actual short-run
bracket.  Suppose further that `v` has a path of at most `R` additional
primitive circuits to an accepting state, of total cost strictly less than
`g`.  Then `q` followed by that return is a closed packet of size at most
`R+1` and strictly decreases `Phi_w`.

If the construction class is closed under these packets and the same
hypothesis regenerates after every repair, integer descent terminates at a
state with `Phi_w<=C`.  For `C=0` this gives residence without adding owners.
For fixed `C`, it gives a bounded central residence debt; a separate bounded
absorber and the remaining literal shadow/compiler rows are still required
for a `B(k)+O(1)` word.

#### Proof

The combined cost is `-g+c_return<0`, so Theorem 4.1 gives the claimed packet.
Positive integer weights make every descent at least one.  Iteration must
therefore terminate.  \(\square\)

The substantive missing all-`k` theorem is precisely a uniform, regenerative
bound on this **lifted** return, not a bound on raw circuit distance.

## 5. Cap-flow closure and why local expansion is insufficient

There is an exact simpler projection when every primitive loses one cap unit
at `u` and gains one at `v`.  Orient it `u -> v` and put

\[
                         b(U)=M_F(U)-1.                   \tag{5.1}
\]

### Lemma 5.1 (unconstrained unit-cap final safety)

Assume in this lemma that selected transfer arcs are jointly selectable apart
from the cap inequalities; row compatibility, protection, topology and trace
guards are omitted.

A selected arc multiset `S` is finally cap-safe iff

\[
             \operatorname{out}_S(U)-\operatorname{in}_S(U)
                    \le b(U)\qquad\hbox{for every }U.     \tag{5.2}
\]

If a prescribed causal arc is `q:u->v` and `b(u)=0`, the least cap-only
closure containing `q` has size

\[
  1+\min\left\{
       \operatorname{dist}(v,u),
       \min_{s:b(s)>0}\operatorname{dist}(s,u)
     \right\}.                                            \tag{5.3}
\]

An infinite distance is ignored.

#### Proof

Equation (5.2) is the identity
`M_{F^S}(U)=M_F(U)-out_S(U)+in_S(U)>=1`.
In a minimal feasible directed subgraph containing `q`, the deficit at `u`
is returned either by continuing the unit emitted at `v` along a path back to
`u`, or by a path from a cap with spare unit `b(s)>0` to `u`.  Removing cycles
and branches not used by one of these paths only decreases the support.
Shortest paths give equality in (5.3).  \(\square\)

For the physical problem, (5.3) is only a cap-projection lower bound.  Its
exact analogue is the shortest accepting return path in the Section 4 lift.
A short cap return may have the wrong endpoint pairing or may create more
residence debt than it repays.

### Counterexample 5.2 (unbounded cap return at degree two)

Let the cap-transfer graph be a directed cycle of length `L`, with `b=0` at
every cap.  By (5.2), the only cap-safe selected subsets are the empty set and
the whole cycle (for multisets, every nonzero feasible circulation contains a
whole-cycle copy).  Thus every nonempty closed packet has at least `L`
primitives even though every cap has indegree and outdegree one.  Cap
completeness and bounded nonzero local degree cannot imply a
dimension-uniform packet size.

### Proposition 5.3 (a Boolean-diamond long-circuit minor)

Let `L>=3`, let `|K|=m-2`, and choose distinct elements
`b,a_0,...,a_{L-1}` outside `K`, with indices modulo `L`.  Thus the ambient
ground set is assumed to contain these elements (in `[2m-1]` one may take
`L<=m`).  Put

\[
 C_i=K+a_i,\qquad
 R_i=K+a_i+b,\qquad
 T_i=K+a_i+a_{i+1}.                                      \tag{5.4}
\]

At facet `C_i`, replace the legal row `{R_i,T_i}` by
`{R_i,T_{i-1}}`.  Work in the restricted face in which all incidences outside
these `L` rows are fixed.  If `z_i` says whether row `i` is replaced,
exact owner degree at `T_i` gives

\[
                            z_i=z_{i+1}.                  \tag{5.5}
\]

Therefore the only degree-preserving choices are none or all `L`.  The full
switch is cap-multiset exact because

\[
 \{K+b+a_i+a_{i+1}:i\}_{\rm multi}
 =\{K+b+a_{i-1}+a_i:i\}_{\rm multi}.                     \tag{5.6}
\]

Hence Boolean diamond geometry itself contains alternating circuits of support
growing with `m`.  This is a local exchange minor; no assertion is made here
that every such minor extends to a protected spanning factor.

At the opposite small boundary, at depth `d=2` the unique owner triangle
`12-13-23-12` on `[3]` is exact in the lower palette and the sole cap `123`,
has positive runs of length two, and has no alternative row.  Thus some
genuine expansion hypothesis is necessary even before asymptotics.

## 6. The authenticated `k=17` paired escape

Fix the deterministic decoder traversal orientation; reversing a quotient
cycle negates its displayed voltage and changes none of the lift counts.  In
this convention the round-48 seed is one quotient cycle of voltage six and one
physical cycle.  Its exact residence vector is

\[
                         (4199,6511,8874,18819).          \tag{6.1}
\]

The complete state-relative **one-endpoint-retaining directed**
single-circuit catalogue has:

\[
\begin{array}{c|r|r|r|r}
 &\text{all}&\text{cap-safe}&\text{connected}&N_+\text{-improving}\\ \hline
 C6&1888&63&30&0\\
 C8&6259&59&24&0.
\end{array}                                               \tag{6.2}
\]

Moreover the lexicographically best connected cap-safe single circuit is the
unchanged seed for the tuple `(N_+,D_+,N_-,D_-)`.  Thus, after choosing a
base `B` larger than every possible cumulative lower-coordinate variation,

\[
             \Phi_B=B^3N_+ +B^2D_+ +BN_-+D_-            \tag{6.3}
\]

has no decreasing protected connected single `C6/C8`.

Within the same endpoint-retaining directed class, the exhaustive
facet-disjoint-pair catalogue contains `8,147` circuits and
`32,769,892` facet-disjoint pairs.  Of these, `7,294` are finally cap-safe,
`1,073` are cap-multiset exact, `2,249` are finally connected, and exactly
four beat the seed lexicographically.  Two of those four strictly lower
`N_+`; the other two keep `N_+=4199` and lower `D_+`.

The best packet uses the eight row substitutions

```text
9094  9113
34592 34607
15722 15716
8135  8121
895   907
19523 19548
9995  9985
915   919
```

and consists of the quotient `C8`s

\[
\begin{array}{c|c|c}
 &\text{facet rows}&\text{moving-owner cycle}\\ \hline
 A&(4827,21147,7017,4347)&4859\to21211\to21357\to8041\to4859,\\
 B&(975,9159,5063,999)&1999\to9167\to13255\to5095\to1999.
\end{array}                                               \tag{6.4}
\]

Each develops as one 136-edge physical alternating circuit.  Both are
individually cap-safe, but neither preserves the complete cap multiplicity
vector.  Applied alone, `A` changes topology

\[
 (1430,V6)\longmapsto(1323,V0)+(88,V3)+(19,V6),          \tag{6.5}
\]

which is 19 physical components.  Applied alone, `B` stays connected but
worsens `N_+` from `4199` to `4233`.  Their union restores one quotient cycle
of voltage five and gives (1.1).  In particular

\[
        \Delta(N_++N_-)=-102,qquad
        \Delta(D_++D_-)=-238.                            \tag{6.6}
\]

By `Z_17` symmetry, every coordinate changes identically:

\[
 (0,136,111)\to(0,135,110),\qquad
 (207,171,144)\to(204,170,144)                           \tag{6.7}
\]

for positive runs and zero gaps of lengths `1,2,3` respectively.

There is an important order correction.  The stored order `A,B` has topology
`1->19->1`.  The audit field named
`best_second_physical_components_if_first` actually evaluates `B` alone.
Direct prefix replay shows that the reverse order `B,A` realizes
`1->1->1`; facet-disjointness supplies commutation but does not by itself
prove this topology statement.  That order incurs the temporary
positive-residence increase `4199->4233->4165`.  Thus this witness proves the
need for a packet and for temporary **lex-primary positive-run** debt, but it
does not force temporary topology debt.  Indeed `B` alone improves the
equal-weight total signed count, so this conclusion is specific to the
lexicographic potential (6.3).  The general lifted theorem allows either kind
of temporary debt.

The eight removed edge orbits occur in the strict cyclic order

\[
                  B_3,A_1,B_2,A_2,B_0,A_3,B_1,A_0.      \tag{6.8}
\]

The gain is therefore a retained-path interlacing effect of the union, not a
sum of two support-local residence deltas.  This is the concrete reason that
Theorem 3.1 must count closed packets after union replay.

## 7. Causality and the fixed-host no-go

### Lemma 7.1 (short-bracket causality)

Let an old positive short run have bracket

\[
                         0\,1^\ell\,0,
                \qquad 1\le\ell\le d.                   \tag{7.1}
\]

and analogously let a zero gap have bracket `1 0^ell 1`.  If its complete
internal owner-adjacency subpath and both trace-changing
boundary adjacencies remain consecutive in the new chronology, the same
short token survives.  Hence every residence repair must rethread at least
one of the `ell+1` selected factor adjacencies in the bracket's causal
closure.  This is necessary only: cutting such an adjacency need not kill the
token.

#### Proof

All letter values on the displayed subpath and both boundary changes are
unchanged, so its maximal positive trace component is still exactly the same
`ell` consecutive positions.  The zero-gap statement follows by complementing
the trace.  \(\square\)

For the authenticated connected double-`C6` marker58 chronology, every cut in
both orientations has `G_2=36`.  The exact two-gap inequality then applies to
every monotone three-particle schedule.  Feasibility with slack `7401` would
require `G_2>=20610`; the exact two-gap inequality gives loss at least

\[
                       2(24310-36)=48548.                \tag{7.2}
\]

Therefore boundary deadline particles alone cannot make this fixed chronology
satisfy the monotone three-particle source gate.  A simultaneous rethread may
still use them after a genuine circuit breaker.  The all-`k` supply theorem,
if true, must select circuits which actually cut and re-pair the short-run
clusters, while jointly returning the cap, topology, voltage, shadow, and
compiler state.

## 8. Exact remaining theorem

The strongest correct dimension-uniform target left by this analysis is the
following conditional statement.

### Regenerative closed-return hypothesis `RCR(d;s,B)`

For every protected Boolean factor in the construction class with positive
integer residence potential, the exact lifted graph contains an accepting
path such that:

1. the path has at most `s` primitives;
2. its total cost is at most `-1` and every prefix has component excess at
   most `B` and lies in the declared resource envelope;
3. the returned factor lies in the same class, so the statement regenerates;
4. every deep-shadow and compiler row needed downstream is either fixed or
   explicitly included in the accepting state.

Because every current defect token has positive weight, Lemma 7.1 implies
that any negative accepting path automatically cuts a current defect bracket.
Corollary 4.2 is a stronger convenient subclass in which the causal primitive
already has negative cost.  `RCR` itself permits neutral or worsening
preparatory primitives; this is essential for paired escapes.

### Corollary 8.1

`RCR(d;s,B)` implies owner-count-neutral descent to residence zero.  If the
remaining accepted central/palette/compiler debt is bounded independently of
the dimension and has a bounded physical absorber, it yields the corresponding
`B(k)+O(1)` construction.

The proof is direct iteration, equivalently Theorem 4.1 at every regenerated
state.  What is **not** proved is `RCR` for all Boolean dimensions.
Counterexample 5.2 shows that cap completeness and bounded local degree do not
give a bounded cap-return radius; it has no residence costs and is not by
itself an `RCR` counterexample.  Proposition 5.3 shows, at the exchange-minor
level, why local
degree/cap/codegree data alone cannot certify a bounded Markov basis; without
a spanning extension it is not a full-factor no-go.  The authenticated pair
proves only that the required return exists at one nontrivial state.

Accordingly the next proof target is a planted or recursive **short lifted
return bank** with literal causal coverage and bounded born-token load.  An
ordinary expansion theorem which ignores the return state, or a fixed-host
deadline export, cannot close the problem.

## 9. Authenticated provenance

The numerical statements in Section 6 are frozen by:

* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/round048.model`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/round048.audit.json`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/c68b.greedy48.independent.audit.json`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_c6c8.audit.json`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_c6c8.best.patch.tsv`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_escape001.model`;
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_escape001.verify.audit.json`; and
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_escape001.residence.audit.json`.

The quotient labels and phase replay additionally use

* `scratch/r2_k17_marker58_upper_q1_double_fusion_replay_20260802/marker58_upper_q1_quotient.map.tsv`,
  SHA `7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3`;
* `scratch/r2_k17_marker58_upper_q1_double_fusion_replay_20260802/k17_marker_orbit.witness.tsv`,
  SHA `88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403`;
* `scratch/search_k17_c68b_double_fusion_residence_c6c8_20260802.cpp`,
  SHA `5304b45a499c7c0e2c858129c32942e980780f12046e2883542abeb5f0ae6672`; and
* `scratch/k17_c68b_double_fusion_residence_greedy_20260802/paired_escape001.SHA256SUMS`,
  SHA `9fd256ab3b87bdb40a0612d6c57bfdd68126a6bde0f6bb20ba548edfe290fd92`.

The aggregate pair counts are frozen locally in `paired_c6c8.audit.json`.
The frozen pair generator and complete emitted pair table are retained on the
H100 campaign root with respective SHAs
`11904b9e38d8762d6409427dd36fec981bfad5758d21ff9dd88dc9b8f47af128`
and
`f21814e1f09d710cfa6163381b871c421a54e9f1b2099eb076a167035323914d`.
The table is `greedy_residence/paired_c6c8.tsv` and is not copied into this
workspace.  The current local working pair-generator source has since drifted
and is not cited as the generator of the frozen aggregate.  Accordingly the
local JSON is authenticated but is not, by itself, an independently replayable
exhaustive pair list.

The fixed-host obstruction used in Section 7 is frozen in
`MATH_THEOREM_V_K17_DEADLINE_PARTICLE_RETHREAD_AND_MARKER58_NONFLAT_NOGO_20260802.md`
and the corresponding H3 source-fibre theorem.  The present note does not
alter or broaden their scopes.
