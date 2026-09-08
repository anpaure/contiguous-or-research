# K17 exact Pareto Benders cuts: signed supplier Hall and short-basis component pricing

**Date:** 2026-08-02  
**Status:** proof-complete outer/Benders reduction.  One phase-zero
one-component candidate is independently frozen, and one protected private
H-short bank is independently frozen.  Neither is a `1S-ROTS` certificate.
No fixed-table SAT, atomic relay, residence, upper-shadow, topology,
common-cap, compiler, or word claim is made.

## 1. Exact Pareto face

Let `R` be the `18,646` real bottom tokens, `F` the `1,748` free hosts, and
`H` the `18,646` hard hosts.  An outer solution is a matching `mu` which
saturates `R` and `F` in the exact containment graph.  Write

\[
 S(\mu)=H-N_\mu(R)
\]

for its `1,748` dummy/short hard hosts.  Equivalently, `S(mu)` is a basis of

\[
                         M_{\rm short}=(M/F)^*.       \tag{1.1}
\]

Materializing `mu` gives a lower table `T(mu)`.  There are three disjoint
short-role classes:

\[
 \mathcal W_{\rm fixed}\ (3899),\qquad
 \mathcal W_F\ (1748),\qquad
 \mathcal W_H=S(\mu)\ (1748).                       \tag{1.2}
\]

The first class has a fixed two-target payload.  A free-host payload is
selected by its real assignment `x_(u,F)`.  A hard-short payload is selected
by `s_v`.  Thus the full short-role census is `7,395`, while the fixed/free
part invisible to H-only dummy pricing already has size `5,647`.

For owner phase `p in {0,1}`, let `G_p(mu)` be its exact union-supplier
projection: the demanded shore is the `16,898` active hard heads
`H-S(mu)`, and the other shore consists of physical supplier-role
identities.  Define

\[
 P_p(\mu)=\nu(G_p(\mu)),
\]

let `Z_p(mu)` be the number of all `7,395` short roles having no exact
common-state socket record in phase `p`, and let `Omega_p(mu)` be the number
of occurrence-labelled exact socket records.

For the originally declared phase-0 strict face, the target was

\[
 \boxed{P_0(\mu)=16898,\qquad Z_0(\mu)\le5968,
                         \qquad \Omega_0(\mu)\ge2189.} \tag{1.3}
\]

Terminal reattachment requires the supplier row in **both** phases:

\[
                         P_0(\mu)=P_1(\mu)=16898.     \tag{1.4}
\]

These are catalogue objectives only.  Even (1.3)--(1.4) do not select one
compatible socket per short role and therefore do not give a `1S-ROTS`
certificate.

The independently replayed round-47 table has

\[
 (P_0,Z_0,\Omega_0)=(16898,5969,2188).               \tag{1.5}
\]

The independently reproduced weighted nonzero-bank basis has materialized
table SHA

```text
3886de626d55d4393d3f71f51fa9799488608f26eb977a8ff60e7be39cfac7cd
```

The latest complete two-phase autopsy supersedes its earlier H-only scalar
pricing.  Its phasewise zero counts, split as
`(fixed,free,hard-dummy)`, are

\[
 (3170,1535,788),\qquad (3193,1542,762),              \tag{1.6}
\]

while its supplier deficiencies are respectively `121` and `131`.
Consequently H-only dummy costs cannot close the Pareto face: most zero
roles are fixed or free and change only through their endpoint placement
edges.  The materialized table itself is independently reproduced;
artifact binding for the new full two-phase autopsy remains external to
this proof, so (1.6) is calibration rather than a theorem premise.

## 2. Symmetric-difference component theorem

Let `mu_0,mu_1` be two outer matchings.  Delete common edges and colour the
remaining edges by their matching.

### Theorem 2.1 (exact path/cycle product face)

The symmetric difference

\[
                         \mu_0\mathbin\triangle\mu_1
\]

is a vertex-disjoint union of alternating even cycles and alternating
paths.  Every path has both endpoints in `H`, with one endpoint in
`S(mu_0)-S(mu_1)` and the other in `S(mu_1)-S(mu_0)`.  Flipping any subset
of these components produces another exact outer matching.

A path flip changes the short basis by exactly one fundamental exchange in
`M_short`.  A cycle flip leaves the short basis unchanged and is a
same-basis payload fibre circuit.

#### Proof

Every real token and every free host is saturated in both matchings, so its
degree in the symmetric difference is zero or two.  A hard host has degree
zero, one, or two; its degree is one exactly when it is occupied in one
matching and short in the other.  Hence every noncyclic component is an
alternating path with the stated hard endpoints.  Alternating a component
preserves degree one at every real token and free host and capacity at most
one at every hard host.  Disjoint components may therefore be flipped in
any subset.

Relative to `mu_0`, a path makes one previously occupied hard endpoint
short and fills one previously short endpoint.  It changes

\[
 S(\mu_0)\quad\text{to}\quad S(\mu_0)-f+e
\]

for `f in S(mu_0)` and `e notin S(mu_0)`.  Since the flipped matching is an
outer witness, `f` belongs to the fundamental circuit
`C_(M_short)(e,S(mu_0))-e`.  A cycle has no hard endpoint, so its short set
is unchanged.  \(\square\)

### Scope

The Boolean product of the round-47/weighted components is an exact finite
candidate family, not a without-loss-of-generality representation of all
outer matchings.  Moreover socket and supplier records can join physical
rows lying in different matching components.  Their gains are therefore
not additive merely because the matching components are disjoint; every
selected packet must be materialized and its interactions recomputed.

## 3. Exact dynamic supplier and socket variables

For each phase `p` and possible occurrence-labelled supplier record `r`, let
`P_p(r)` be the set of selected outer mode literals (`X/P/S`) which
materialize it.  In the ordinary outer matching these supports are finite
and positive: exact-one mode rows make omitted alternatives false
automatically.  Introduce

\[
 \lambda^p_r\Longleftrightarrow
             \bigwedge_{e\in P_p(r)}z_e.                       \tag{3.1}
\]

The exact linearization is

\[
 \lambda^p_r\le z_e\quad(e\in P_p(r)),\qquad
 \lambda^p_r\ge1-|P_p(r)|+\sum_{e\in P_p(r)}z_e.    \tag{3.2}
\]

For supplier identity `u` and hard head `v`, put

\[
 a^p_{uv}\Longleftrightarrow
       \bigvee_{r:\operatorname{sup}(r)=u,
                    \operatorname{head}(r)=v}\lambda^p_r,     \tag{3.3}
\]

encoded in both directions.  These equivalences are load-bearing: retaining
an old record after its payload mode disappears, or omitting a newly created
record, makes the Hall cut below unsound.

The record universe must cover every mode allowed by the declared outer
scope.  The frozen phase-0 catalogue is complete for ordinary `X/P/S`
placements.  A generalized compound-relay mode requires its own records and
cannot be inferred from the ordinary catalogue.

The same support semantics handles all three short classes.  For a ticket
`g` attached to a fixed old short role, `P_p(g)` contains only the selected
predecessor/successor endpoint modes.  For a free role `F`, it additionally
contains the unique selected `x_(u,F)` which fixes its lower payload.  For a
hard-dummy role `v`, it additionally contains `s_v`.  Hence the actual
primitive Benders variables are real placement edges, not merely the
identity of the hard short basis.

## 4. Signed supplier-Hall cuts

For a fixed phase `p` and physical hard-head set `Q subseteq H`, define

\[
 n^p_{Q,u}\Longleftrightarrow\bigvee_{v\in Q}a^p_{uv}.         \tag{4.1}
\]

Thus `n^p_(Q,u)` counts supplier `u` once, no matter how many records it has
into `Q`.  Let `s_v` be the hard-short bit.  The exact Hall row is

\[
 \boxed{
   \sum_{v\in Q}(1-s_v)-\sum_u n^p_{Q,u}\le0.}        \tag{4.2}
\]

### Theorem 4.1 (exact projection separator)

The phase-`p` union-supplier projection is perfect on all `16,898` active
hard heads if and only if (4.2) holds for every `Q subseteq H`.  A maximum
matching and minimum alternating Hall shore separate this family exactly.

#### Proof

The active demand contained in `Q` is `Q-S(mu)`, of size
`sum_(v in Q)(1-s_v)`.  Equations (3.3)--(4.1) make
`sum_u n^p_(Q,u)` exactly the cardinality of its distinct supplier
neighborhood.  Therefore (4.2) is Hall's inequality.  Hall's theorem and
bipartite matching integrality give the equivalence and the min-cut
separator.  \(\square\)

Let `mu*` be a current table and put

\[
 d_{p,Q}^*=\sum_{v\in Q}(1-s_v^*)-
                   \sum_u n_{Q,u}^{p,*}.             \tag{4.3}
\]

Subtracting (4.2) from (4.3) gives the exact **signed acceptance cut**

\[
 \boxed{
 \sum_{v\in Q}(s_v-s_v^*)
 +\sum_u(n^p_{Q,u}-n_{Q,u}^{p,*})\ge d_{p,Q}^*.}     \tag{4.4}
\]

The four signs in (4.4) are essential:

* shortening a currently active head contributes `+1`;
* reactivating a currently short head contributes `-1`;
* adding the first new supplier neighbor contributes `+1`;
* losing the last old supplier neighbor contributes `-1`.

Counting supplier records instead of distinct supplier identities is
incorrect.  So is a cut which counts only gains and ignores lost last
providers.  If `d_(p,Q)^*=0`, (4.4) is the exact nonnegative-charge condition
for a tight shore.  If `d_(p,Q)^*>0`, it requires at least the whole current
deficiency in net signed repair.

Equivalently, (4.4) can be written entirely as signed gain/loss events:

\[
\begin{split}
 &\sum_{v\in Q:s_v^*=0}s_v
 +\sum_{u:n_{Q,u}^{p,*}=0}n^p_{Q,u}\\
 &\quad-
 \sum_{v\in Q:s_v^*=1}(1-s_v)
 -\sum_{u:n_{Q,u}^{p,*}=1}(1-n^p_{Q,u})
 \ge d_{p,Q}^*.                                      \tag{4.5}
\end{split}
\]

This is the exact row to emit in `X/P/S` space after substituting the
bidirectional activation DNFs (3.1)--(4.1).

One separated shore does not rule out takeover by a previously slack shore.
The proof-safe loop is therefore:

1. solve the current outer/Pareto master;
2. materialize and recompute both complete supplier graphs;
3. if either phase matching is deficient, extract a maximum Hall shore `Q`
   in that phase and add (4.4) with exact activations (3.1)--(4.1);
4. repeat.

The loop is finite because the outer matching set is finite and every failed
incumbent violates its newly added row.  This proves termination of the
separator, not existence of a Pareto-feasible table.

## 5. Exact all-role ticket DNF and Pareto cuts

For phase `p`, let `b_g^p` be the exact activation of common-state ticket
`g`, encoded as in (3.1)--(3.2), and put

\[
 c_w^p\Longleftrightarrow
       \bigvee_{g:\operatorname{short}(g)=w}b_g^p.    \tag{5.1}
\]

The three role classes have different mode semantics:

\[
 short_w=
 \begin{cases}
 1,&w\in\mathcal W_{\rm fixed},\\
 \sum_u x_{uF}=1,&w=F\in\mathcal W_F,\\
 s_v,&w=v\in H.
 \end{cases}                                         \tag{5.2}
\]

For a free role, the equality in the middle of (5.2) is always one, but the
selected literal `x_(u,F)` remains in every ticket DNF because it determines
the lower payload.  The exact zero and ticket counts are

\[
\boxed{
\begin{aligned}
 Z_p={}&
 \sum_{w\in\mathcal W_{\rm fixed}}(1-c_w^p)
 +\sum_{F\in\mathcal W_F}(1-c_F^p)
 +\sum_{v\in H}(s_v-c_v^p),\\
 \Omega_p={}&\sum_g b_g^p.
\end{aligned}}                                       \tag{5.3}
\]

Thus H-only dummy pricing sees only the last zero summand and is not an
exact Pareto objective.  Real bottom placement edges `x/p` can create or
destroy tickets for all `5,647` fixed/free roles through their own free
payload and their predecessor/successor endpoint modes.

At incumbent `*`, a phasewise target `Z_p<=B_p` is exactly the signed cut

\[
\begin{split}
 &\sum_{w\in\mathcal W_{\rm fixed}\cup\mathcal W_F}
       (c_w^p-c_w^{p,*})\\
 &\quad+
 \sum_{v\in H}\bigl[(c_v^p-c_v^{p,*})-(s_v-s_v^*)\bigr]
 \ge Z_p^*-B_p.                                      \tag{5.4}
\end{split}
\]

and a target `Omega_p>=K_p` is

\[
                         \sum_g(b_g^p-b_g^{p,*})
                         \ge K_p-\Omega_p^*.          \tag{5.5}
\]

Equations (5.1)--(5.5) give proof-safe linear lexicographic objectives,
subject to the hard Hall family (4.2) in both phases.  A per-hard-slot degree
or flag mask is only an additive pricing surrogate; it does not equal
(5.3), because fixed/free roles and shared endpoint placements dominate the
current zero census.

If the global occurrence catalogue is not materialized, a fixed-table value
of `Z_p` or `Omega_p` permits only the complete positive assignment no-good,
or a smaller **signed** assumption core proved against the complete global
activation formula.  A local dependency halo or stale provider count by
itself is not a valid Benders cut.

For one zero role `w`, its proof-safe escape condition is the literal DNF

\[
 \boxed{
 c_w^p=
 \bigvee_{g\in\mathcal G_w^p}
       \bigwedge_{e\in P_p(g)}z_e.}                  \tag{5.6}
\]

For fixed/free `w`, (5.6) is specifically a cut on real placement edges.
If a complete catalogue proves every conjunction in (5.6) incompatible
with the outer rows, then `w` is globally zero in that declared scope.
Otherwise a current zero supplies no hard unit: one of its complete DNF
terms may be activated by a future rematching.

## 6. Fundamental-circuit pricing

Fix a current short basis `S` and a real-bottom matching witnessing it.  For
`e notin S`, delete the matched edge entering hard host `e` and run one
alternating reachability search from the exposed real bottom.  Its reachable
currently short hard hosts are exactly

\[
 C_{M_{\rm short}}(e,S)-e.                            \tag{6.1}
\]

For every `f` in (6.1), an alternating path gives a literal rematching and
the feasible exchange `S-f+e`.  This is the exact pricing neighborhood; no
atomic relay variable is involved.

For an alternating path `P`, materialize its matching `mu_P`.  Its exact
charge against a separated phase-`p` shore is

\[
 \Gamma_{p,Q}(P)=
 \sum_{v\in Q}(s_v(\mu_P)-s_v(\mu))
 +\sum_u(n^p_{Q,u}(\mu_P)-n^p_{Q,u}(\mu)).           \tag{6.2}
\]

It passes that shore exactly when

\[
                         \Gamma_{p,Q}(P)\ge d_{p,Q}(\mu). \tag{6.3}
\]

Different alternating paths realizing the same endpoint exchange can move
different internal bottoms and hence have different charges, zeros, and
ticket counts.  Fundamental-circuit membership prices feasible endpoint
exchanges; it does not make the nonlinear supplier/socket objective modular.
The exact price tuple is obtained only after replay:

\[
 \left(
 16898-P_0(\mu_P),16898-P_1(\mu_P),
 Z_0(\mu_P),Z_1(\mu_P),-\Omega_0(\mu_P),-\Omega_1(\mu_P)
 \right).                                                        \tag{6.4}
\]

Cycle components from Theorem 2.1 must also be retained: they keep `S`
fixed but can change both supplier and socket activations.  When several
paths/cycles are flipped together, recompute (6.2) and (5.3) on their union;
do not sum stale singleton scores unless their full activation supports are
proved disjoint.

## 7. Exact finite next step and scope

Use round 47 as the projection-perfect endpoint and the weighted table as
the catalogue-improved endpoint.  Decompose their two real matchings as in
Theorem 2.1.  The builder may search the resulting component product face,
with (4.2) hard and (5.3) lexicographic, while a fresh matching/min-cut
separates any new Hall shore.  This is a proof-safe exact subproblem.

On the declared phase-0 face, component `603` is the first strict candidate:

\[
                         (P_0,Z_0,\Omega_0)=(16898,5967,2207). \tag{7.1}
\]

The candidate is independently frozen under

```text
scratch/k_rots_k17_joint_1s_20260802/pareto_component603_frozen/
```

with load-bearing hashes

```text
component table       54b8063b4f39afb8ffccabadb88f04b65edaa0a4321c343f84f15918d75f24f4
full audit            4ac8f356e7c4b6eb48b10f90210678981b097ba7db67756e8074d106c212dadb
coordinate-DP audit   cb8364c67dd8f486aadd2986231f579cb758fe02e2ffc7de522ab3293606c57b
flip ledger           ea6ef70c52a7f077d4443d5b406d23febf752784c5d2b590d5f28f0029f8426b
```

Its exact scope is phase 0 and one alternating component only.  It gives no
phase-1, common-cycle, residence, upper, or compiler inference.

Failure of that component product proves only that this two-endpoint face is
empty.  A global verdict requires all `M_short` fundamental exchanges and
same-basis fibre circuits, with every accepted candidate literally
materialized.  Passing (1.3) still leaves the common-address cycle cover,
both owner phases, reattachment to the authoritative carrier, residence,
upper shadows, topology, common-cap/compiler feasibility, and the word.

## 8. Protected private H-short bank corollary

The independently verified bank under

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
```

contains exactly `1,748` hard short roles and one retained exact phase-0
ticket for each.  Its certificate has:

```text
selected tickets                                  1748
distinct predecessor endpoint hosts               1748
distinct successor endpoint hosts                 1748
hosts common to the two endpoint shores               0
forced dynamic host-token placement edges         3495
fixed soft-long endpoint                               1
```

The selected short set is a basis of `M_short`, all endpoint tokens are
injective, and the forced edges extend to a complete outer matching.  The
load-bearing hashes are

```text
manifest
80e1c40c74d4e3f14b738d22ef6c0a1f90926c765da30bde0669ecf2d29f25ba

independent theorem audit
dfaa7a5682861945f2de680076e86ce70fac2be5f35b3fe9783916c3903eec92

selected tickets
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1

complete outer matching
179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
```

This is a sufficient retained-witness subbank; it is not a completeness or
no-go theorem for all global tickets.

### Exact protected-face Pareto start

Materializing the exhibited complete outer extension gives the fixed phase-0
table

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_h_outer_materialized.tsv
SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

The independent relaxed-nine audit, SHA-256
`5c14e0834829ab3c27c83be817259d8bc9e2395ab1e9a94b84713d740d4cb29f`,
gives

\[
 P_0=16796\quad(\text{deficiency }102),\qquad
 \Omega_0=3878,qquad Z_0=4708,                       \tag{8.0}
\]

with the exact zero split

\[
 3187\ (\text{fixed}),\qquad1521\ (F),\qquad0\ (H).
\]

Equivalently, all `1,748` protected H tickets survive literally and every
remaining zero lies among the `5,647` fixed/free roles.  The socket summary
and ticket files have SHA-256 values

```text
socket summary   bc7415c669ee58213934405de696d23411359450d59bbdbb2705e4fbf3c4df67
socket triples   6e4f41c30b8aa9d9cbb599343d055d1ff14387137d3e0575b3f01ad5ea7d2217
```

This is the exact Pareto starting point for the protected face.  It is one
fixed residual completion and its `P_0` value is the union/menu projection;
it is not a common-state cycle factor.  The residual master must restore the
`102` supplier units while selecting literal tickets for all `5,647`
fixed/free roles, not merely improve the `4,708` zero count.

### Abstract short eligibility is not a typed bank

Let

\[
 \mathcal A_0=\{v\in H:\mathcal G_0(v)\ne\varnothing\}
\]

be the `10,167`-element phase-zero local nonzero bank.  Membership
`v in A_0` asserts only that `v` has at least one individually legal ticket.
Even requiring a set `S subset A_0` of size `1,748` to be a basis of
`M_short` does **not** assert that its tickets can be chosen simultaneously.

Write `B:=S_H`.  The protected certificate is the stronger typed object
`(B,tau,E_B;mu_B)`, where `tau(v)` is one occurrence-labelled ticket for
every `v in S_H`, `E_B` is its set of `3,495` forced movable endpoint
assignments, and `mu_B` is a complete outer matching witnessing that this
protected partial assignment extends.  Thus `mu_B` is a positive reference
witness, not a residual edge set which must remain pinned.  The data satisfy:

1. `S_H` is an `M_short` basis;
2. the predecessor hosts of the `tau(v)` are injective and disjoint from
   `B`;
3. the successor hosts are injective, disjoint from `B`, and disjoint from
   all predecessor hosts;
4. their movable bottom-token assignments form `E_B`, are injective, and
   belong to `mu_B`; and
5. every ticket carries the literal predecessor/successor flags and short
   address used by the state equations below.

Thus Theorem 8.1 fixes `B`, `tau`, `E_B`, and the fixed soft endpoint, not
merely the abstract basis `B subset A_0`.  It may pin `mu_B` for a
fixed-table subface, or reopen every residual edge while retaining `E_B`;
the witness `mu_B` proves that the latter face is nonempty.  This distinction
prevents an ordinary `M_short`-basis or nonzero-bank computation from being
misread as a composable socket bank.

### Theorem 8.1 (exact residual phase-0 state master)

Fix the protected H-short ticket bank `B`.  After contracting it, the long
roles are

\[
 L=(H\setminus B)\mathbin{\dot\cup}L_{\rm soft},
 \qquad |L|=16898+17=16915.
\]

In particular, a hard row in `B` may not reappear as a long endpoint.  Let

\[
 \mathcal W_R=\mathcal W_{\rm fixed}\mathbin{\dot\cup}\mathcal W_F,
 \qquad |\mathcal W_R|=5647,                         \tag{8.1}
\]

and let `G_R` be the complete occurrence-labelled phase-0 ticket catalogue
for these residual short roles on this protected materialization.  It must
be regenerated after contraction, or equivalently filtered so that both
endpoint hosts belong to `L` and every protected host--token assignment is
retained.  Write `P_B,Q_B` for the protected predecessor/successor host
sets.  For long role `h` and flag `a`, let `O^B_(h,a)` and `I^B_(h,a)` be the fixed protected
outgoing/incoming stub indicators.  They are binary, and no long host has a
protected stub on both shores in this certificate.

Use variables

* `z_(h,a)` for the selected flag of each long role;
* `r_g` for each residual ticket `g in G_R`;
* `e_c` for each exact direct long--long flag transition `c`.

The exact residual equations are

\[
 \sum_a z_{h,a}=1                                      \tag{8.2}
\]

for every `h in L`.  If `v` is a protected endpoint, let `a_B(v)` be its
literal predecessor or successor flag.  The protected flag units are

\[
 z_{v,a_B(v)}=1\qquad(v\in P_B\cup Q_B).              \tag{8.2a}
\]

They are load-bearing: a protected host may use its opposite directed port
later, but only with this already selected physical flag.

\[
 \sum_{g\in G_R:\operatorname{short}(g)=w}r_g=1       \tag{8.3}
\]

for every `w in W_R`, and, for every `(h,a)`,

\[
\boxed{
\begin{aligned}
 O^B_{h,a}
 +\sum_{g:\operatorname{pred}(g)=(h,a)}r_g
 +\sum_{c:\operatorname{tail}(c)=(h,a)}e_c &=z_{h,a},\\
 I^B_{h,a}
 +\sum_{g:\operatorname{succ}(g)=(h,a)}r_g
 +\sum_{c:\operatorname{head}(c)=(h,a)}e_c &=z_{h,a}.
\end{aligned}}                                        \tag{8.4}
\]

Every residual ticket and direct arc also carries its exact outer-mode DNF
implications from Section 3.  If the emitted complete outer matching is
pinned, these implications reduce to catalogue filtering.  If only the
`3,495` forced endpoint edges and the short basis are pinned, the remaining
outer matching stays variable and (3.1)--(3.3) must be retained in both
directions.

Equations (8.2)--(8.4) select exactly

\[
 1748+5647=7395\text{ socket hyperarcs},\qquad
 16915-7395=9520\text{ direct arcs}.                  \tag{8.5}
\]

They are necessary and sufficient for a relaxed-nine phase-0 contracted
common-state cycle cover extending `B` within the declared outer/catalogue
scope.

#### Proof

Every protected ticket already consumes one outgoing and one incoming
long-state stub.  Cross-disjointness and token injectivity make these fixed
consumptions mutually compatible.  Equation (8.3) chooses one exact common
state for each remaining short role.  Equations (8.2) and (8.4) choose one
common flag and exactly one incoming and outgoing contracted incidence for
each long role.  Contract every selected long--short--long ticket to one
directed arc; together with the selected direct transitions, the degree rows
give a directed cycle cover.  Conversely, any such labelled cover supplies
values satisfying the displayed degree rows and literal ticket selections.
Summing either side of (8.4) gives
(8.5).  \(\square\)

### Corollary 8.2 (exact reduced Benders interface)

The H-short intersection problem is closed on this protected face.  The
only remaining phase-0 state columns are:

1. the `5,647` fixed/free role DNFs (5.6);
2. the residual long--long flag transitions in (8.4); and
3. the phase-0 **selected-state** supplier activation and Hall rows
   (9.8)--(9.10), required at value `16,898`.

The Section 4 rows remain exact for the outer-mode union projection used in
the Pareto screen, but they do not by themselves require all supplier edges
to coexist with one selected `z/r/e` state.  That extra coupling is exactly
why the selected parent is retained in (9.8).

Before the long flags and one predecessor endpoint per residual role are
fixed, the `5,647` ticket layer is a typed three-partite hypermatching, not
one ordinary flow.  After those branches, the successor choice is a
bipartite Hall flow; after all tickets are fixed, the residual long--long
row is a second bipartite Hall flow.  No joint total-unimodularity claim is
made.

If the particular emitted complete outer matching fails the residual rows,
retain the protected bank and its `3,495` forced placement edges but reopen
the unforced outer matching.  Static extendability is guaranteed by the
certificate; signed Hall separation (4.4) and the full fixed/free DNFs then
choose another extension.  A failure is scoped to this protected retained-
witness face.

The theorem gives a cycle cover, not one common cycle.  Subtour joining,
phase 1, physical chronology/replay, residence, upper shadows, topology,
common-cap/compiler feasibility, and the word remain separate.

## 9. Exact residual cycle-fibre activation cuts

The protected typed data `(B,tau,E_B)` fix the short basis but deliberately do not
pin the arbitrary residual edges of its complete outer matching.  Contract
the forced set `E_B`, fix one residual perfect matching `mu_*`, and take any
pairwise vertex-disjoint family
`C` of `mu_*`-alternating even cycles.  A bit `b_C` chooses whether cycle
`C` is flipped.  Every bit vector therefore gives an exact residual outer
matching `mu(b)`.  This is a declared cycle-fibre subproblem, not a
without-loss-of-generality description of all residual matchings.

For every occurrence-labelled primitive `q`--a fixed/free ticket, a direct
long--long transition, or a supplier occurrence--let `L(q)` be the complete
set of outer-cycle and flag literals required to materialize it.  Introduce

\[
 \lambda_q\Longleftrightarrow\bigwedge_{\ell\in L(q)}\ell. \tag{9.1}
\]

The exact linearization is

\[
 \lambda_q\le\ell\quad(\ell\in L(q)),\qquad
 \lambda_q\ge1-|L(q)|+\sum_{\ell\in L(q)}\ell.        \tag{9.2}
\]

A support which asks for both orientations of the same alternating cycle is
empty and is deleted; so is a support requiring an outer edge absent from
every matching in the declared fibre.  The protected tickets have
`lambda=1` because all
their outer edges and flags are pinned.  For every residual short role `w`,
the exact availability and selection rows are

\[
 c_w\Longleftrightarrow\bigvee_{g\in\mathcal G_w}\lambda_g,
 \qquad c_w=1,
 \qquad \sum_{g\in\mathcal G_w}y_g=1,
 \qquad y_g\le\lambda_g.                              \tag{9.3}
\]

Thus a zero-role Benders cut is not `S subset A_0`; it is the literal DNF
`sum_g lambda_g >= 1` in the current cycle fibre.

After tickets are selected, define the binary unused long-port indicators

\[
\begin{aligned}
 o_h&=1-O^B_h-\sum_{g:\operatorname{pred}(g)=h}y_g,\\
 i_k&=1-I^B_k-\sum_{g:\operatorname{succ}(g)=k}y_g.
\end{aligned}                                         \tag{9.4}
\]

Here `O^B_h,I^B_k` are the protected consumptions summed over their uniquely
fixed flags.  For a direct transition `c:h->k`, let

\[
 \eta_c\Longleftrightarrow \lambda_c\wedge o_h\wedge i_k,
 \qquad
 n_{X,k}\Longleftrightarrow
   \bigvee_{c:\,\operatorname{tail}(c)\in X,
                  \operatorname{head}(c)=k}\eta_c.     \tag{9.5}
\]

With selected direct-edge bits `d_c`, the exact residual degree rows are

\[
 d_c\le\eta_c,qquad
 \sum_{c:\operatorname{tail}(c)=h}d_c=o_h,qquad
 \sum_{c:\operatorname{head}(c)=k}d_c=i_k.             \tag{9.6}
\]

Projecting out the `d_c` gives the exact residual long--long Hall family

\[
 \boxed{
   \sum_{h\in X}o_h\le\sum_k n_{X,k}
   \qquad(X\subseteq L).}                             \tag{9.7}
\]

This form allows the available-port shore itself to change with the ticket
selection.  Omitting `o_h` or `i_k` from (9.5) would count transitions whose
port has already been consumed and would make (9.7) unsound.

Finally, assign every physical source role to its unique selected outgoing
primitive in the contracted cover: a protected or residual ticket owns its
internal short source and its predecessor-long source, while a direct edge
owns its tail-long source.  The supplier-record universe must be completely
cloned over every possible such owner primitive and every compatible head
state.  In particular `parent(r)` must own the outgoing incidence of
`sup(r)`; it may not be an arbitrary selected primitive having the same
flag.  With this convention, a supplier occurrence `r` is active only when
both its literal outer/state DNF and its parent selected primitive are
active.  Put

\[
 \kappa_r\Longleftrightarrow
   \lambda_r\wedge\pi_{\operatorname{parent}(r)},       \tag{9.8}
\]

where `pi` is `1` for a protected ticket, `y_g` for a residual ticket, and
`d_c` for a long--long transition.  Define

\[
 a^0_{uv}\Longleftrightarrow
   \bigvee_{r:\operatorname{sup}(r)=u,
                \operatorname{head}(r)=v}\kappa_r,
 \qquad
 n^0_{Q,u}\Longleftrightarrow\bigvee_{v\in Q}a^0_{uv}. \tag{9.9}
\]

Because the protected face fixes the short set `S_H`, its exact supplier
cuts are

\[
\boxed{
   |Q\setminus S_H|\le\sum_u n^0_{Q,u}
   \qquad(Q\subseteq H).}                            \tag{9.10}
\]

### First instantiated selected-state cut

For the protected-face Pareto start (8.0), the independently replayed
alternating shore `Q_*` has `109` active hard heads and only `7` distinct
union/menu supplier identities.  Its literal head file has SHA-256
`5b0afdc17d4be1e05bc51f459e8c2fe299959dbfdc279f13a409557ba0712255`.
Since `S_H` is fixed and `Q_* subset H-S_H`, the first selected-state
Benders row is simply

\[
                 \boxed{\sum_u n^0_{Q_*,u}\ge109.}    \tag{9.11}
\]

Let `n^*_(Q_*,u)` be the seven baseline union/menu activations.  Subtracting
their sum gives the equivalent signed pricing form

\[
 \boxed{
   \sum_u\bigl(n^0_{Q_*,u}-n^*_{Q_*,u}\bigr)\ge102.} \tag{9.12}
\]

There is no head-short term: the protected face fixes the active head shore.
The absolute cut (9.11), rather than the baseline's union/menu states, is
load-bearing.  In particular, losing one of the seven old identities must be
paid by one additional new selected-state identity.

On the residual short shore, the baseline supports exactly
`5647-4708=939` fixed/free roles.  If `c_w^*` denotes that baseline support
indicator, the aggregate consequence of the literal rows (9.3) is

\[
 \boxed{
   \sum_{w\in\mathcal W_R}(c_w-c_w^*)\ge4708.}        \tag{9.13}
\]

This is equivalent to `c_w=1` for every one of the `5,647` roles only when
combined with the individual upper bounds `c_w<=1`; the separate literal
DNF rows in (9.3) are the proof-safe formulation.  The baseline count
`Omega_0=3878` is only a menu statistic and cannot replace (9.3).

### Theorem 9.1 (cycle-fibre equivalence)

Within the declared phase-zero cycle fibre, the protected bank extends to a
target-exact contracted cycle factor with all `5,647` residual short roles
supported and supplier matching `16,898/16,898` if and only if the exact
outer-cycle rows, flag/endpoint rows, (9.1)--(9.6), the selected-parent
activation rows (9.8)--(9.9), and all cuts (9.10) are feasible.  If supplier
coupling is temporarily omitted, projecting the
direct-edge bits out of (9.6) gives exactly (9.7).  For the full theorem the
`d_c` variables must be retained through (9.8)--(9.10), or replaced by an
exact **joint** projection: (9.7) alone proves only that some residual direct
matching exists, not that one of them has the required supplier graph.

#### Proof

Fixing the cycle and flag bits makes every `lambda_q` the exact primitive
availability indicator.  Equation (9.3) is therefore equivalent to choosing
one literal ticket for each residual short role.  The graph induced by
(9.5) is exactly the bipartite graph on the remaining outgoing and incoming
long ports.  Equations (9.6) choose its perfect matching; Hall's theorem
makes (9.7) the exact projected separator.  The selected matching together
with the protected and residual tickets gives indegree and outdegree one at
every contracted role, hence a cycle factor.  Equations (9.8)--(9.9) are the
exact selected supplier graph, and Hall's theorem makes (9.10) equivalent to
saturating the `16,898` active heads.  The converse reads the same variables
from any such factor.  \(\square\)

The theorem does not impose a subtour cut.  It certifies a cycle factor only;
one common cycle, phase 1, residence, upper shadows, physical replay, and the
terminal compiler remain open.

## 10. Correlated rank-seven `P2--H--H` columns

The fixed-role master of Sections 8--9 cannot see an exact escape which
changes which rank-seven target occupies a `P2` bottom and two `H` middles.
Such an escape must be a **table column**, not a favourable socket score on
the old table.  This section gives the exact smallest column language and
the corresponding regenerated master.

### 10.1 The complete row-shadow catalogue

Fix a length-two row

\[
                         S_0\subset R_0,
 \qquad |S_0|=7,\quad |R_0|=8.                       \tag{10.1}
\]

For each `a in S_0`, put

\[
 b=R_0\setminus S_0,\qquad C=S_0\setminus\{a\},
 \qquad S_1=C\cup\{b\}.                             \tag{10.2}
\]

Because the lower target table is exact, there is at most one physical row
whose `H` middle is `S_1`.  If there is none, reject this `a`.  Otherwise let
its root be `R_1` and put `c=R_1-S_1`.  Define

\[
 S_2=C\cup\{c\},\qquad R_2=C\cup\{a,c\}.            \tag{10.3}
\]

Again there is at most one `H` row whose middle is `S_2`.  Retain the triple
only if that row has root `R_2` and its two old bottoms obey

\[
                         B_1\subset S_2,qquad
                         B_2\subset S_0.             \tag{10.4}
\]

Then the column is

\[
\begin{aligned}
 &(S_0,R_0)+(B_1,S_1,R_1)+(B_2,S_2,R_2)\\
 &\quad\longmapsto
 (S_1,R_0)+(B_1,S_2,R_1)+(B_2,S_0,R_2).              \tag{10.5}
\end{aligned}
\]

#### Lemma 10.1 (complete support-three enumeration)

Every alternating `P2--H--H` six-cycle through (10.1) occurs exactly once
in (10.2)--(10.5).  Hence there are at most seven row-shadow columns per
rank-seven `P2` row.  The authenticated K17 table has `785` such rows, so
there are at most

\[
                         7\cdot785=5495               \tag{10.6}
\]

before bottom, protection, phase-state, and supplier filters (and at most
`7*623=4361` when restricted to the old rank-seven union-zero roles).

#### Proof

In a rank-seven/rank-eight incidence six-cycle, the first new middle is
obtained from `R_0` by deleting one element `a` of `S_0`; the added element
is the unique `b=R_0-S_0`.  This gives (10.2) uniquely.  Exact target use
then fixes the first `H` row and its third point `c`.  The third rank-seven
vertex and its required root are forced by (10.3), after which exact target
use fixes the second `H` row.  The remaining strict-chain conditions are
exactly (10.4).  Conversely these equations are the Boolean hexagon on
`C union {a,b,c}`, so (10.5) is an alternating six-cycle.  \(\square\)

This is a row-shadow enumeration only.  It does not assert that any retained
triple has a common phase socket, respects the private bank, or improves a
global objective.

For the authenticated fixed K17 table, an independent complete replay of
this enumeration gives a sharper one-shot census.  Among the `623`
rank-seven roles in the old two-phase union-zero set there are

\[
\begin{array}{c|r|r}
\text{filter}&\text{columns}&\text{zero roles incident to a column}\\ \hline
\text{row-shadow closure}&364&290\\
\text{plus both bottom containments}&180&168\\
\text{plus protected row/host disjointness}&118&116.
\end{array}                                           \tag{10.6a}
\]

No zero role has more than three raw row-shadow columns.  Thus a single
packing chosen from this fixed protected-row-clean catalogue can touch at
most `116` of the `623` named roles.  In fact the `118` row-clean columns
have exactly two row-conflict pairs, and an independently replayed exact
maximum packing has size `116` and uses `348` physical rows.  This remains
an upper bound before phase sockets and complete occurrence-resource
conflicts.  The C6 layer is therefore a harvest/absorber bank, not a complete
fixed-table role repair.  This is a **one-shot fixed-table** obstruction only: a
selected C6 changes two `H` middles and a serial recatalogue can create new
row-shadow columns.  It is not a serial-C6 no-go, and “row-clean” is weaker
than the protected-safe definition below because forced outer edges and
phase witnesses have not yet been replayed.

There is nevertheless an exact stronger obstruction to a **move-each-defect**
version of fixed-root suffix repair.  Admit all `19448` rank-seven slots,
delete every lower-bottom constraint, and put an arc `u->v` when the current
rank-seven label at `u` fits the fixed rank-eight root at `v`.  The resulting
assignment digraph has `136136` nonidentity arcs, `421` strongly connected
components, and one component of size `18953`.  Among the `623` old
rank-seven union-zero P2 roles, `461` lie in nontrivial components and `162`
are singleton components.  Therefore those `162` target labels cannot move
in any fixed-root target reassignment, regardless of circuit length.

This does **not** prove that their socket zeros persist.  Moving other `H`
middles can create new endpoint modes for an unchanged P2 role, which is why
the complete regenerated DNF (10.10) remains load-bearing.  The SCC theorem
forces global three-level/root recoupling only for an architecture which
repairs every named zero by moving that zero's own rank-seven target.  It is
not an absolute fixed-root ROTS no-go.

### 10.2 Protected and mutually composable columns

For a candidate `g`, let `R(g)` be its three physical rows and let
`Sigma(g)` contain every occurrence-labelled resource whose incidence is
changed or consumed by the column: moved target occurrences, changed `H`
middle hosts, owner/root/palette occurrences, and any outer or state endpoint
used by its declared witness.  Call `g` **protected-safe** when

1. its three new chains are strict and its named target multiset is the old
   one;
2. every protected ticket in `(B,tau,E_B)` remains literal;
3. every forced edge in `E_B`, and the fixed soft endpoint, remains legal
   after the changed `H` ceilings are substituted; and
4. every declared phase witness is recomputed on the changed table.

Let `G_B` be the complete protected-safe catalogue.  A proof-safe directly
composable face uses bits `x_g` with

\[
 x_g+x_h\le1
 \quad\text{whenever}\quad
 R(g)\cap R(h)\ne\varnothing
 \ \text{or}\ 
 \Sigma(g)\cap\Sigma(h)\ne\varnothing.              \tag{10.7}
\]

The resource clause is deliberate: row-disjoint columns can still compete
for a named outer/state occurrence.  Within (10.7), the final target table
is unambiguous and independent of application order.

For each physical row `i`, introduce one-hot state literals `z_(i,s)` for
its old state and every selected column state.  They are fixed by

\[
 z_{i,g}=x_g\ (i\in R(g)),\qquad
 z_{i,0}=1-\sum_{g:i\in R(g)}x_g.                    \tag{10.8}
\]

Every outer containment edge `e` must now have an activation

\[
 A_e\Longleftrightarrow
 \bigvee_{\sigma:\ e\text{ is legal in row-state tuple }\sigma}
       \bigwedge_{(i,s)\in\sigma}z_{i,s}.             \tag{10.9}
\]

The outer matching uses only edges with `A_e=1`, pins `E_B`, and satisfies
the ordinary token/right degree rows.  Equation (10.9), not the old
containment graph, is load-bearing whenever an `H` middle changes.

Likewise, regenerate the complete fixed/free ticket, direct-transition, and
supplier catalogues over the row-state tuples.  For every occurrence-labelled
primitive `q`, replace (9.1) by

\[
 \lambda_q\Longleftrightarrow
 \left(\bigwedge_{(i,s)\in Z(q)}z_{i,s}\right)
 \wedge
 \left(\bigwedge_{\ell\in L(q)}\ell\right),          \tag{10.10}
\]

where `Z(q)` is its complete table-state support and `L(q)` contains its
outer, flag, endpoint, and address literals.  Records inherited from the old
table but false after a selected C6 have `lambda=0`; newly created records
must be present as distinct clones.  The exact-one ticket rows (9.3), unused
ports (9.4), direct matching (9.5)--(9.7), and selected-parent supplier rows
(9.8)--(9.10) are then imposed without change.

### Theorem 10.2 (exact disjoint-column master)

Assume `G_B` is complete for the row/resource-disjoint face (10.7), and all
outer, ticket, direct, and supplier records are completely cloned as in
(10.9)--(10.10).  Then this master is feasible if and only if some table
obtained from the protected baseline by a mutually compatible set of these
rank-seven C6 columns admits a phase-zero target-exact contracted cycle
factor, all `5647` fixed/free tickets, the protected `1748`-ticket bank, and
a selected-state supplier matching of size `16898`.

#### Proof

A chosen disjoint column set fixes exactly one literal state of every row by
(10.8), and each protected-safe column preserves the named target deck and
the protected bank.  Equation (10.9) is exactly the resulting outer graph,
so its degree rows choose precisely an outer completion extending `E_B`.
Equation (10.10) makes each later primitive active exactly in the selected
table, outer matching, and flag/address state.  The proof of Theorem 9.1 now
applies verbatim.  Conversely, read the selected C6s, row states, outer
matching, tickets, direct edges, and supplier matching from any such literal
factor.  \(\square\)

The theorem is not a completeness claim for overlapping C6 packets.  Such a
packet requires a larger simultaneous table-state column, not the sum of
per-C6 objective deltas.

### 10.3 Authenticated positive column and the 693-route separation

The literal rows

```text
16269,16267,16271

old  81416-81417 ; 73216-81409-81413 ; 81408-81412-81420
new  81409-81417 ; 73216-81412-81413 ; 81408-81416-81420
```

are an instance of (10.5).  Independent replay verifies exact target/root/
owner/histogram preservation, all `1748` private tickets, the complete
`18646`-edge protected outer matching, and one literal socket in each owner
phase.  The phase-zero witness has `(q,a,b)=(8,2,2)` and the phase-one witness
has `(7,0,0)`.  A second replay verifies that the raw warm-47 supplier
matching remains `16898/16898`; its three changed selected masks remain
nonzero.  These are separate frozen certificates, not one selected-state
cycle factor.

The abstract 693-exchange outer-zero route is also separate.  Its final hard
short basis intersects this protected basis in only `311` of `1748` rows,
and its materialized table retains only `557` of the `3495` forced dynamic
placements in `E_B`.  Thus that exact route endpoint is outside this exact
protected face.  This is not a no-go for another 693-style route or another
private bank.

The independent sources and frozen outputs for these two scoped checks are
listed in the companion audit.  No one-cycle, phase-one common state,
residence, upper-shadow, physical source, common-cap/compiler, or word claim
is made here.

## 11. Global chain/root recoupling: determinant two and exact branch flow

The restricted C6 master leaves the current receiver-root bank fixed.  The
natural enlargement is still small enough to have an exact two-block flow
description.

Let `L` be the occurrence-labelled top shore exported by an exact
chainization of the targets below rank seven, let `M` be the rank-seven
target shore, and let `R` be the rank-eight root shore.  Use binary variables

```text
y_lm  for a legal lower-to-middle link,
y_lr  for a legal lower-to-root link,
x_mr  for a legal middle-to-root link.
```

The undecorated chain partition is exactly

\[
\begin{aligned}
 \sum_m y_{lm}+\sum_r y_{lr}&=1 &&(l\in L),\\
 \sum_r x_{mr}&=1 &&(m\in M),\\
 \sum_l y_{lr}+\sum_m x_{mr}&=1 &&(r\in R),\\
 \sum_l y_{lm}&\le1 &&(m\in M).                     \tag{11.1}
\end{aligned}
\]

These are one bipartite b-matching: the left shore is
`L_out dotcup M_out`, the right shore is `M_in dotcup R_in`, and the three
variable classes are its edges.  Thus (11.1) is totally unimodular.

For a first marginal screen, let `p_mr=1` when the short role created by
choosing `m->r` has at least one admissible occurrence-labelled ticket in
the current declared state catalogue.  If `m` receives no lower predecessor,
its chosen root edge must be positive, giving

\[
 E_m:\qquad
 \sum_l y_{lm}+\sum_{r:p_{mr}=1}x_{mr}\ge1.          \tag{11.2}
\]

### Proposition 11.1 (the positivity coupling is not TU)

Suppose the legal table contains `y_lm`, `y_lr`, and a positive `x_mr` for
one triple `(l,m,r)`.  On rows `(E_m,A_l,C_r)`--where `A_l` is the first
degree row of (11.1) and `C_r` is its root-degree row--these three columns
contain

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad \det=2.                                      \tag{11.3}
\]

Hence the natural marginal-positive chain matrix is not totally unimodular.
The base b-matching theorem cannot be cited as an integral proof after
(11.2) is added.

This is a matrix obstruction, not an infeasibility theorem.  The exact
conditional problems remain bipartite flows.

### Theorem 11.2 (exact alternating branch-flow formulation)

Fix an integral `x` satisfying its middle degrees and root capacities.  Let

\[
 R_x=\{r:\sum_m x_{mr}=0\},\qquad
 V_x=M\mathbin{\dot\cup}R_x,\qquad
 D_x=R_x\mathbin{\dot\cup}
     \{m:\sum_{r:p_{mr}=1}x_{mr}=0\}.                \tag{11.4}
\]

Then a compatible `y` exists if and only if the bipartite graph of legal
`y_lm,y_lr` edges has a matching which saturates all `L` and every mandatory
right vertex in `D_x`.  Equivalently, after adjoining
`|V_x|-|L|` dummy left vertices complete to the optional right shore
`V_x-D_x`, the augmented bipartite graph has a perfect matching.
Thus ordinary Hall (or one lower-bound maxflow) is necessary and sufficient.
For K17, `x` matches all `19448` middles to distinct roots, so

\[
 |R_x|=24310-19448=4862,qquad |V_x|=24310,qquad
 |V_x|-|L|=2533.                                    \tag{11.4a}
\]

Thus the dummy construction is literal.  In another cardinality regime one
must first require `|V_x|>=|L|`, or use the lower-bound flow directly.

Conversely, fix an integral `y` satisfying every lower-target degree equation
and the right-receiver capacity inequalities inherited from (11.1).  Put

\[
 S_y=\{m:\sum_l y_{lm}=0\},\qquad
 R_y=\{r:\sum_l y_{lr}=0\}.                          \tag{11.5}
\]

A compatible `x` exists if and only if the bipartite graph between `M` and
`R_y`, using all legal `m->r` edges for `m notin S_y` and only edges with
`p_mr=1` for `m in S_y`, has a perfect matching.  Again ordinary Hall is
necessary and sufficient.  Here “perfect” means both shores: in particular
`|R_y|=|M|` is necessary.  Equivalently, if
`t=|{(l,m):y_lm=1}|`, compatibility forces

\[
 t=|L|+|M|-|R|=16915.                               \tag{11.5a}
\]

#### Proof

Once `x` is fixed, every unused root must be filled by `y`, every middle
whose selected `x` edge is not positive must receive a lower predecessor,
and every lower occurrence must be used once.  All other middle-input
vertices have capacity at most one.  This is precisely the mandatory-right
matching in (11.4).  The dummy completion matches every unused optional
right vertex to a dummy and therefore turns it into an ordinary perfect
matching without changing the real matching.

Once `y` is fixed, (11.1) leaves exactly `R_y` for the middle outputs.
Every middle is used once; (11.2) restricts exactly the rows in `S_y` to
positive edges.  This is the perfect matching in (11.5).  \(\square\)

### 11.1 Exact selected-state and protected-bank version

The constant `p_mr` is only a marginal screen.  In the exact ROTS master it
must be replaced by

\[
 c_{mr}\Longleftrightarrow
 \bigvee_{g\in\mathcal G(m,r)}\lambda_g,              \tag{11.6}
\]

where every `lambda_g` is the complete table-state/outer/flag/address DNF
from (10.10).  The selected `x_mr` of a short middle must choose one active
ticket `g`, not merely an edge with a stale `p_mr=1`.  Put

\[
 s_m=1-\sum_l y_{lm}
\]

and introduce a ticket-selection bit `t_mrg` for every
`g in G(m,r)`.  The exact coupling is

\[
 \sum_{r,g\in\mathcal G(m,r)}t_{mrg}=s_m,
 \qquad t_{mrg}\le x_{mr},
 \qquad t_{mrg}\le\lambda_g.                        \tag{11.7}
\]

The selected `t` bits, rather than the availability OR `c_mr`, consume the
shared endpoint/resource capacities and own the supplier parent in
(9.8).  For the retained
private-H face, every protected short `m in B` pins its exhibited `x` edge,
has no selected lower predecessor, fixes its ticket in `tau`, and retains
the `3495` forced outer assignments `E_B` plus the fixed soft endpoint.
Any global root recoupling which changes one of those protected rows leaves
this face and must select and replay a new private bank.

Equations (11.4)--(11.5) are exact conditional flows for the **marginal**
`p`-screen.  In the selected-state master, after table/outer/flag state and
a resource-compatible `t` assignment are fixed, the residual `y` row is a
mandatory-right Hall flow.  After `y` and the state literals are fixed, the
joint `(x,t)` completion reduces to the restricted `x` matching only when
the ticket choices have no remaining shared-resource conflict; otherwise
(11.7) is retained in the Benders master.  After both are fixed, the
selected-parent supplier graph must still satisfy (9.8)--(9.10).  This is an
exact decomposition with a ticket-hypermatching master, not a proof that the
joint three-layer system is integral.

The current finite obstruction is therefore sharply localized.  The
projection-perfect round-47 table closes the marginal lower supplier row,
but no complete post-role-move catalogue of the `5647` fixed/free common-
state DNFs exists yet.  The protected materialization starts at supplier
deficiency `102` and fixed/free zero count `4708`; the branch flows above
must be separated only after those DNFs are regenerated on the selected
chain/root table.
