# Correlated hex planting and sparse rerouters: an exact conditional cover-down theorem

Date: 2026-07-31  
Status: exact deterministic completion theorem, exact bank--colour density
reduction, and exact outer/slot invariants for sparse rerouting.  No
positive-density planting theorem or all-parameter construction is claimed.

## 0. Result

The suspended transparent hex and the sparse `ell`-cycle have complementary
roles.

* A planted hex is a gain-one boundary packet

  \[
                         O_i\longrightarrow N_i,
       \qquad |O_i|=2,quad |N_i|=3,                 \tag{0.1}
  \]

  whose uncovered boundary is one complete four-resource target atom `T_i`.
* A sparse `ell`-cycle is count-neutral.  It preserves the two outer
  palettes and changes only its physical pairing and noncommon slot bank.

Consequently sparse rerouters cannot create target-colour alignment after a
DP colour has been chosen.  The DP outer leave must already be the lower and
upper projection of a planted target subbank.  Rerouters may then align the
off phases, literal slots, and physical topology.

The exact conditional theorem below says that if this correlated planting
state exists, simultaneous activation of the hexes closes the side factor.
Across a family of recursively chosen endpoint-bank/common-`Q` states, if
such plantable DP colour records have density `a_n`, then one has planted
leave size at most

\[
                              h\le {\eta_n\over a_n}P.          \tag{0.2}
\]

This is the correct quantitative target.  Neither the quadratic formal
hex count nor the linear unpunctured packet packing proves `a_n>0`.

For a fixed five-cycle rerouter the theorem applies uniformly for `n>=8`.
More generally it applies for every `ell>=5,n>=2ell-2`.  The smaller
parameters remain finite base cases or require a different planted
count-neutral packet.

## 1. Balanced host and planted hex bank

Fix an admissible common basis `Q`.  Choose, as an explicit bank decision,
a slot set `S_0` of the affine-baseline cardinality and work in the balanced
host

\[
                         \widehat G_Q=G_Q-S_0,                  \tag{1.1}
\]

whose lower, upper, and slot shores have orders `(P,P,2P)`.  The cardinality
of `S_0` is forced; its location is not.

Let `K` be the already frozen physical scaffold, with its incidences deducted
from the residual slots.

A planted hex record is a triple

\[
                      \mathcal P_i=(T_i,O_i,N_i),               \tag{1.2}
\]

where `T_i` is the designated atom, `O_i` is the two-atom off phase, and
`N_i` is the three-atom on phase from the suspended transparent-hex theorem.
Its literal resource identity is

\[
       \operatorname{res}(N_i)
        =\operatorname{res}(O_i)\mathbin{\dot\cup}
          \operatorname{res}(T_i).                              \tag{1.3}
\]

Assume the complete supports of distinct planted records are
resource-disjoint.  Thus the targets form a matching and all switches
commute once their off phases are present.

For `I` a packet-index set write

\[
 T_I=\mathbin{\dot\bigcup}_{i\in I}\operatorname{res}(T_i),
 \quad O_I=\mathbin{\dot\bigcup}_{i\in I}O_i,
 \quad N_I=\mathbin{\dot\bigcup}_{i\in I}N_i.                  \tag{1.4}
\]

Write `D(T_I),V(T_I),S(T_I)` for the lower, upper, and literal-slot
projections of `T_I`.

## 2. Exact action of a sparse rerouter

Let `R` be a sparse `ell`-cycle with old phase

\[
                    R^0=\{(D_i,V_i):i\in\mathbb Z_\ell\}
\]

and new phase

\[
                    R^1=\{(D_{i+1},V_i):i\in\mathbb Z_\ell\}.
\]

Its common owners are `H_i`; its old-only owners are `P_i`; and its
new-only owners are `Q_i`.  After fixing literal slots, define its covered
slot displacement

\[
 d_R=\sum_{i\in\mathbb Z_\ell}
       (\mathbf e_{\xi_{Q_i}}-\mathbf e_{\xi_{P_i}}).           \tag{2.1}
\]

### Proposition 2.1 (outer invariance and exact slot transport)

If a legal whole-phase switch replaces `R^0` by `R^1` in a matching `F`,
then

\[
 L_D(F')=L_D(F),\qquad L_V(F')=L_V(F),                \tag{2.2}
\]

and

\[
                         L_S(F')=L_S(F)-d_R.          \tag{2.3}
\]

For a legal sequence `Gamma` of whole rerouters, (2.3) telescopes with

\[
                         d_\Gamma=\sum_{R\in\Gamma}\pm d_R,    \tag{2.4}
\]

where the sign records the switched direction.

#### Proof

The two phases are perfect matchings of the same `ell` lower and `ell`
upper colours, proving (2.2).  Their `H_i` slots agree; the `P_i` slots are
removed and the `Q_i` slots are inserted, proving (2.3).  Successive covered
incidence differences telescope. `square`

Thus rerouting is confined to one fixed outer-leave fibre.  This is the
first exact obstruction to post-hoc planting.

### Corollary 2.2 (slot-displacement fibre)

Fix a finite private rerouter catalogue `R_1,...,R_m`, all initially in
their declared old phases, and let `Delta` have columns `d_(R_j)`.  If the
switches commute, a binary selection `y` transports the slot leave to a
desired vector `S` exactly when

\[
                         \Delta y=L_S(F)-S,qquad
                         y\in\{0,1\}^m.               \tag{2.5}
\]

In particular every integer row vector `lambda` with `lambda Delta=0`
must satisfy

\[
                    \lambda(L_S(F)-S)=0.              \tag{2.6}
\]

Equation (2.6) is only a necessary lattice obstruction; the exact condition
is the binary fibre (2.5), together with phase availability and physical
guards.

## 3. Deterministic correlated-planting theorem

Let `F` be a matching in the balanced host with `K union p(F)` a physical
forest and

\[
                              |F|=P-h.                \tag{3.1}
\]

Let `Gamma` be a legal sequence of count-neutral sparse rerouters, including
the exterior graphic checks, and put `F'=Gamma(F)`.  Thus
`K union p(F')` is also a forest.

### Theorem 3.1 (planted target completion)

Suppose there is an index set `I` with `|I|=h` such that:

1. **outer planting**
   \[
     L_D(F)=\{D(T_i):i\in I\},\qquad
     L_V(F)=\{V(T_i):i\in I\};                      \tag{3.2}
   \]
2. **rerouter reachability** every whole switch in `Gamma` is present and
   legal when used, and the final matching contains `O_I`;
3. **slot alignment**
   \[
                         L_S(F')=S(T_I);              \tag{3.3}
   \]
4. **resource privacy** the untouched part `F'-O_I` is disjoint from every
   on-state resource in `N_I`;
5. **physical graphic row** after deleting `p(O_I)` and contracting every
   component of the retained physical forest `K union p(F'-O_I)`, the edges
   `p(N_I)` are loopless and independent in the quotient graphic matroid;
6. **recursive reserve row** the completed occurrence graphs, and every
   macro-state deliberately exported to the recursion, satisfy all four
   cumulative prefix-reserve inequalities on both shores; and
7. **protected cap/compiler row** every nonparallel outer circuit avoids the
   protected pointwise-cap bottoms, and every separately declared compiler
   guard has zero aggregate displacement or a proved regeneration.

Then

\[
                         F^*=(F'-O_I)\cup N_I         \tag{3.4}
\]

is an exact outer-perfect slot matching of size `P`, its union with `K` is a
physical forest, and it therefore has an automatic
existential Boolean common cap.  Its final occurrence state passes the
declared cumulative reserve guard.

If this side row is used inside the three-sector recursion, imposing in
addition the one-complement-reset-per-augmented-cycle condition makes it a
valid residual-factor row.  That topology condition is not implied by
(3.2)--(3.3).

#### Proof

Rerouters preserve size and the two outer leaves, so `|F'|=P-h` and (3.2)
still holds.  The balanced host then gives slot-leave size `2h`.  The target
bank `T_I` has exactly `h` lower, `h` upper and `2h` literal slot resources.
Equations (3.2)--(3.3) therefore give the full resource equality

\[
                              L(F')=T_I.              \tag{3.5}
\]

Using `O_I subset F'`, resource privacy, and the disjoint identities (1.3),
the simultaneous switches cover every host resource exactly once.  They add
one atom per packet, so (3.4) has size `P`.  Hypothesis 5 proves physical
acyclicity after the switch.  Exact outer saturation, slot matching, and
physical acyclicity imply the existential Boolean common cap.  Hypotheses
6--7 give the logically separate reserve and compiler conclusions. `square`

### Corollary 3.2 (outer-alignment obstruction)

No sequence of sparse count-neutral rerouters can repair a failure of
(3.2).  Hence a DP colour whose lower or upper leave is not the projection
of one planted target subbank cannot be completed by this architecture,
regardless of its slot displacement, affine flux, or number of available
rerouters.

This is why the body, `Q`, and target bank must be chosen together.

## 4. Exact menu and cut hypotheses

There is first an exact outer target-selection cut.  Given lower and upper
hole banks `D_0,V_0`, form the bipartite graph `J_Q(D_0,V_0)` in which
`D-V` is an edge when at least one legal suspended-hex macro has a target
atom over the outer pair `(D,V)`.  Slot lifts are retained as parallel macro
records but suppressed in this outer graph.

### Proposition 4.1 (outer target Hall cut)

Assume `|D_0|=|V_0|=h`.  There is a target-atom family whose two outer
projections are exactly `D_0,V_0` if and only if `J_Q(D_0,V_0)` has a
perfect matching, equivalently

\[
                         |N_{J_Q}(X)|\ge|X|
                              \qquad(X\subseteq D_0).             \tag{4.1}
\]

#### Proof

Distinct target atoms must use distinct lower and upper resources, so their
outer pairs form a matching.  Exact coverage of both hole banks makes it
perfect.  The converse and the cut formulation are Hall's theorem. `square`

Count-neutral rerouting leaves `D_0,V_0` fixed, so a violated row in (4.1)
cannot be repaired downstream.

For a target atom `T`, let `L_T` be a list of pre-certified **macro keys**.
A key specifies:

* one legal suspended-hex embedding with target `T`;
* the off phase to be planted;
* a finite whole-rerouter sequence placing that off phase and solving its
  declared slot displacement; and
* its complete protected, occurrence, and physical guard signature.

The following strong private-menu condition reduces simultaneous planting
to ordinary Hall and is sufficient for Theorem 3.1.

1. Distinct macro keys have resource-disjoint complete supports whenever
   they belong to different target lists.
2. For every target subfamily `J`,

   \[
                         \left|\bigcup_{T\in J}L_T\right|\ge |J|. \tag{4.2}
   \]

Hall chooses distinct keys, and cross-list privacy makes the selected
macros commute.  Without privacy, (4.2) is not sufficient: packet-support
conflicts form a hypergraph rather than a partition matroid.

The local quadratic count `2n(n-2)` does not imply (4.1).  For a fixed
target `T=(D,V)`, all suspended-hex options meet the owner transversal

\[
                              \mathcal W_T=\{V-b:b\in D\}.       \tag{4.2}
\]

If every residual slot at these owners is protected, `L_T` is empty.  A
frozen pointwise cap map can likewise delete every orientation.  These are
exact zero-list cuts, not probabilistic shortages.

For the rerouter layer, (2.5) is the exact private-catalogue alignment cut.
For the physical layer, hypothesis 5 of Theorem 3.1 is equivalently

\[
 r_{\rm gr}(p(N_I)\text{ in }K\cup p(F'-O_I)\text{ contracted})
                              =|p(N_I)|.              \tag{4.3}
\]

If each macro suppresses to one quotient ear, Rado's inequalities

\[
 r_{\rm gr}\!\left(\bigcup_{T\in J}\Sigma_T\right)\ge |J|
                          \qquad(J\subseteq I)        \tag{4.4}
\]

are sufficient and necessary for choosing one graphic-independent ear per
menu.  An arbitrary multi-edge macro does not reduce to (4.4) without this
ear-suppression hypothesis.

## 5. Bank-flexible density theorem

Let `B_n` be a finite family of recursive states.  A state contains a parent
endpoint bank, a compatible common basis `Q`, a **designated planted
subbank** `I_b` with its off phase `O_(I_b)` preloaded, an optional private
rerouter bank, and protected resource/atom sets `Z_b,R_b`.  Different
subbank choices may be expanded into different states.  The reduced host
deletes the complete supports
`res(N_(I_b))=res(O_(I_b)) dotcup T_(I_b)`, while the preloaded off
phase is adjoined afterwards.  Colour that reduced host and pad to the common
DP palette size

\[
       K_D=D+s,qquad D=2(n+1)(n+2).                  \tag{5.1}
\]

For a padded colour `M_(b,i)`, fix one cycle pruning, adjoin the preloaded off
phase, and write

\[
 F_{b,i}=M_{b,i}\cup O_{I_b},\qquad
 \widehat\delta_{b,i}=P-|F_{b,i}|.                  \tag{5.2}
\]

Put

\[
 \eta_n=\rho_n+{D\max_b|Z_b|+\max_b|R_b|\over K_DP}
                    +{1\over L+1}.                  \tag{5.3}
\]

Call `(b,i)` **correlated-plantable** when its pruned forest admits `Gamma`
satisfying Theorem 3.1 with `I=I_b`, and with

\[
                         |I_b|=\widehat\delta_{b,i}.  \tag{5.4}
\]

Let `a_n` be the density of correlated-plantable pairs in
`B_n times [K_D]`.

### Theorem 5.1 (correlated-planting density payoff)

If `a_n>0`, one correlated-plantable pair has

\[
                         |I_b|\le {\eta_n\over a_n}P. \tag{5.5}
\]

Consequently a planted reserve of order at least the right side is
quantitatively large enough for the selected record.  If
`eta_n/a_n ->0`, the selected off bank has order `o(P)` and the protected
reserve theorem leaves a `P-o(P)` bulk outside its closed support.

#### Proof

The padded whole-colouring ledger, deletion bound, and cycle pruning give

\[
 {1\over K_D}\sum_i\widehat\delta_{b,i}\le\eta_nP
\]

for every state `b`.  Sum over states and restrict the nonnegative total to
the correlated-plantable subset.  Its minimum is at most the total divided
by `a_n|B_n|K_D`, proving (5.5).  Equation (5.4) identifies deficiency with
the number of gain-one activations.  Adjoining the preloaded off phase can
only lower `P-|M_(b,i)|`, so the same padded upper bound remains valid for
`P-|F_(b,i)|`. `square`

There is an exact self-reserve correction when the states are stratified by
planted-bank size.  Fix `h` and let every state in `B_(n,h)` plant exactly
`h` packets.  Suppose

\[
 |Z_b|\le z_0+w_Zh,qquad |R_b|\le r_0+w_Rh,          \tag{5.6}
\]

where `w_Z,w_R` are the protected resource/atom costs per planted macro.
Put

\[
 \eta_n^0=\rho_n+{Dz_0+r_0\over K_DP}+{1\over L+1},
 \qquad
 \theta_n={Dw_Z+w_R\over K_D}.                       \tag{5.7}
\]

### Corollary 5.2 (density must beat the planting tax)

If correlated-plantable pairs have density `a_(n,h)` in the fixed-`h`
state layer, then

\[
                    (a_{n,h}-\theta_n)h\le\eta_n^0P. \tag{5.8}
\]

In particular, when `a_(n,h)>theta_n`,

\[
                         h\le {\eta_n^0P\over
                                      a_{n,h}-\theta_n}.         \tag{5.9}
\]

#### Proof

In one fixed-`h` state the total padded deficiency is at most
`K_D eta_n^0 P+(Dw_Z+w_R)h`.  Sum over the states.  Every aligned pair in
this layer has deficiency exactly `h`, so the aligned contribution is
`a_(n,h)|B_(n,h)|K_Dh`.  Compare the two totals and divide by
`|B_(n,h)|K_D`. `square`

Since `K_D=D+s`,

\[
                         \theta_n=w_Z+o(1)+{w_R\over D+s}.       \tag{5.10}
\]

Thus the blunt protected-**resource** deletion estimate is fatal for a
closed constant-size packet: already `w_Z>=2` makes
`a_(n,h)>theta_n` impossible because `a_(n,h)<=1`.  The literal hex support
has twelve host resources before any owner closure.  This does not prove
that correlated planting is impossible; it proves that deleting its whole
support and then applying the maximum-degree DP ledger cannot certify it.

The viable density proof must charge the **actual** atom loss of a
planting-aware colouring, share the protected cost across many targets, or
condition the colour construction so that off phases and target omissions
are native rather than created by host-resource deletion.  Hiding the
support inside an undifferentiated `o(P)` term conceals this exact
self-reserve obstruction.

The linear unpunctured packet theorem supplies more than `P/54` disjoint raw
hex supports, and uniform common-basis marginals preserve `1-O(1/n)` of a
fixed prepacked bank.  These facts show that reserve cardinality can be
linear.  They do not prove positive `a_n`, the outer equality (3.2), the
binary slot fibre (2.5), or compatibility with the favourable-`Q` capacity
cuts.  A sufficient quantitative capacity row is the right side of (5.9)
at most the surviving packet-bank order (for the crude raw bank, at most
`P/54`); this remains conditional on a planting-aware loss estimate strong
enough to replace the vacuous closed-resource value in (5.10).

## 6. Conditional recursive consequence and exact open row

Assume authenticated finite base states below parameter eight.  If for every
`n>=8` there is one correlated-plantable record satisfying Theorem 3.1,
the optional one-reset topology row, and the downstream compiler guard, then
these records form a valid bank-flexible recursive chain.  At no point is an
extension of every parent or every common basis required.

The weakest new existence theorem is therefore:

> construct a positive-density family of joint bank--`Q`--DP colour records
> whose **outer** leave is a planted target subbank, and prove private macro
> Hall, binary slot-displacement reachability, final graphic independence,
> and cumulative reserve for that same record.

The sharp obstruction is equally explicit.  Count-neutral rerouters are
trapped in one outer-leave fibre; owner-transversal or protected-cap cuts may
empty a target's hex menu; and a nonzero left-kernel evaluation in (2.6)
blocks all private rerouter combinations.  Thus neither marginal DP density,
formal absorber abundance, nor cumulative reserve alone implies correlated
planting.

No exact all-`n` side factor, AGCF recursion, compiler, or `nu=B` conclusion
is claimed.

## 7. Authenticated inputs

```text
MATH_THEOREM_CATALAN_SUSPENDED_TRANSPARENT_HEX_ABSORBER_AND_BLOCKERS_20260731.md
  SHA 40bbd681c8476a00c4cda52742fbbf733fd5c3c8b740d43d2c0cae77f277a79a
MATH_THEOREM_CATALAN_SPARSE_FIVE_CYCLE_PHYSICAL_SWITCH_20260731.md
  SHA 719104b056ca9d2b94636643d2799b74dc2d9bc3dc759de08b8a2fc11c813dd3
```
