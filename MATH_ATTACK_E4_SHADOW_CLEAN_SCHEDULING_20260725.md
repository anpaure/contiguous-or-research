# Fourth-wave E: shadow-clean scheduling, seam cycles, and geometric Hall obstruction

Date: 2026-07-25  
Method: pure mathematics only

## 0. Verdict

The shadow-clean scheduling lemma is not proved.  No counterexample to the
contiguous-OR conjecture, overload MWB, or labelled synchronization is
obtained.

This attack produces four new exact advances.

1. Exact zero-defect packetization of prescribed balanced flags has a
   polynomial-size anchored integer-flow formulation with one packet per
   first-label anchor, exact `n`-cycle connectivity, and packetwise point
   equations.  It is an MILP characterization, not a polynomial-time Hall
   theorem.
2. In the radius-one residence corridor, every shadow-clean schedule has a
   complete **seam-cycle normal form**.  Rowwise residence choices are
   disjoint adjacent departure transpositions.  Exact ownership forces the
   selected seams to be a union of directed cycles in one factor-dependent
   functional digraph.  Balanced prefixes are then an explicit integer
   vector condition on those same cycles.  This preserves one labelled owner
   permutation and exact `n`-cycles throughout.
3. For arbitrary residence displacement, every shadow-clean schedule with
   total residence defect `Delta` transports the canonical depth-`q` target
   histogram to its balanced target histogram at total Johnson cost exactly
   `Delta`, for every `q<=K`.  Hence a polynomial integral min-cost flow
   `T_q(F)` is a lower bound on `Delta`.  Its dual is an explicit
   1-Lipschitz Hall--Kantorovich certificate.
4. The ordered `(K-1)` deletion types form a directed Euler multigraph.  Its
   weak components give a polynomial component-isotropy lower bound on the
   residence defect of every exact-prefix rainbow `n`-cycle schedule.  The
   bound is robust under failed overlaps and is attained by an explicit
   endpoint-switch packet.

The second theorem is a quantitative obstruction applying to **every**
low-defect shadow-clean schedule.  It is strictly stronger rankwise than the
unlabelled overload distance.  It does not by itself give a universal lower
bound, because the exact factor may be chosen.

The natural attempt to add the packet-forced point margins to this min-cost
flow is not directly totally unimodular: its bonus-set incidence matrix
contains a determinant-`2` minor at every relevant central rank.  This rules
out the raw TU/laminar formulation, but not an extended formulation.

## 1. Setup

Put

\[
n=2m+1,\qquad \Omega=\binom{[n]}m,\qquad
W=|\Omega|,\qquad B=\frac Wn,
\]

and, for fixed `A`,

\[
K=\lceil A\sqrt m\rceil,qquad
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,qquad
S_K=\sum_{q=1}^K\frac1{c_q}.
\tag{1.1}
\]

A shadow-clean schedule consists of `B` labelled cyclic rows

\[
(X_{p,j})_{j\in\mathbb Z_n},\qquad 1\le p\le B,
\]

with first-deletion labels `g_{p,j}` such that:

1. `j\mapsto g_{p,j}` is a coordinate bijection on every row;
2. `X_{p,j}\setminus X_{p,j-1}=\{g_{p,j}\}`;
3. the actual prefix is

   \[
   d_t(X_{p,j})=g_{p,j-t+1},\qquad 1\le t\le K;
   \tag{1.2}
   \]

4. the canonical shadows

   \[
   W_{p,j}=\{g_{p,j},g_{p,j-1},\ldots,g_{p,j-m+1}\}
   \tag{1.3}
   \]

   are pairwise distinct.

There are `W` shadows, so condition 4 makes them one exact oriented wreath
factor `F`.  The actual owners are also exactly the members of `Omega`, once
each.  Thus the row successor map on the actual owners is one common
permutation whose cycles all have length `n`.

Let `r_{p,i}` be the residence length of coordinate `g_{p,i}` in its actual
row.  Define

\[
\Delta=\frac12\sum_{p,i}|r_{p,i}-m|.
\tag{1.4}
\]

For slot `v=(p,j)`, put

\[
C_q(v)=\{g_{p,j},g_{p,j-1},\ldots,g_{p,j-q+1}\},
\]

\[
L_q(v)=W_{p,j}\setminus C_q(v),\qquad
Q_q(v)=X_{p,j}\setminus C_q(v).
\tag{1.5}
\]

The actual flags are balanced through `K` precisely when every rank-`(m-q)`
set occurs among the `Q_q(v)` either `c_q` or `c_q+1` times.

### Lemma 1.1 (zero-defect rigidity)

One has `Delta=0` if and only if `X_{p,j}=W_{p,j}` at every slot.  Therefore
exact length-`m` residence leaves no rounding freedom once the coordinate
cycles are fixed: balanced prefixes then exist if and only if the canonical
histograms of `F` are already balanced.

#### Proof

Residence `r_{p,i}=m` for every coordinate gives (1.3) as the actual owner
incidence formula.  Conversely, the canonical windows give residence `m`.
The final assertion follows from (1.5).  QED.

Thus a positive theorem which literally enforces length-`m` residence must
choose the factor and the balanced canonical prefixes simultaneously.  A
nontrivial repair theory must allow small residence defect.

## 1A. Exact anchored residence-flow formulation

There is an exact polynomial-size formulation of zero residence defect.  Its
integrality is the issue.

Put

\[
g(X)=d_1(X).
\]

A necessary first-label margin is

\[
|g^{-1}(a)|=B\qquad(a\in[n]).
\tag{1A.1}
\]

Define the labelled owner compatibility digraph `Gamma_K` by an arc `X->Y`
when

\[
Y\setminus X=\{g(Y)\},\qquad
d_{t+1}(Y)=d_t(X)\quad(1\le t<K).
\tag{1A.2}
\]

Fix a coordinate `a_*` and use the `B` owners

\[
\mathcal P=g^{-1}(a_*)
\]

as packet anchors.  Introduce binary variables `y_{pX}` and `z_{p,XY}` for
anchors `p\in\mathcal P`, owners `X`, and arcs `X\to Y`, together with nonnegative flow
variables `f_{p,XY}`.

### Theorem 1A.1 (anchored exact-packet MILP)

The prescribed labelled prefixes partition into exact oriented wreath
packets if and only if the following system is feasible:

\[
\sum_{p\in\mathcal P}y_{pX}=1,qquad y_{p,p}=1,
\tag{1A.3}
\]

\[
\sum_{X:g(X)=a}y_{pX}=1
\qquad(p\in\mathcal P, a\in[n]),
\tag{1A.4}
\]

\[
\sum_{Y:X\to Y}z_{p,XY}
=\sum_{Y:Y\to X}z_{p,YX}=y_{pX},
\tag{1A.5}
\]

\[
\sum_{X:a\in X}y_{pX}=m
\qquad(p\in\mathcal P, a\in[n]),
\tag{1A.6}
\]

\[
0\le f_{p,XY}\le(n-1)z_{p,XY},
\tag{1A.7}
\]

and, for `X!=p`,

\[
\sum_{Y:Y\to X}f_{p,YX}
-\sum_{Y:X\to Y}f_{p,XY}=y_{pX},
\tag{1A.8}
\]

while at the anchor

\[
\sum_{Y:p\to Y}f_{p,pY}
-\sum_{Y:Y\to p}f_{p,Yp}=n-1.
\tag{1A.9}
\]

Here `y,z` are binary.  If the given prefixes already form a balanced common
nested resolution, feasibility preserves that balance exactly.

#### Proof

For fixed `p`, (1A.4) chooses exactly one owner of every first-label color,
hence exactly `n` owners.  Equation (1A.3) partitions all labelled owners and
places the unique `a_*`-colored anchor in its own packet.  The degree equations
(1A.5) make the selected arcs a disjoint union of directed cycles.

The flow (1A.7)-(1A.9) sends one unit from `p` to each other selected owner.
A selected directed cycle not containing `p` would have total net demand
strictly positive but no entering selected arc, contradicting its summed flow
equations.  Thus the selected subgraph is one directed cycle of length `n`.

List it as `X_j`, with entrant `g_j=g(X_j)`.  The support law in (1A.2) and
the rainbow color equation imply that each coordinate enters exactly once
and hence occupies one cyclic interval.  Its residence length is

\[
r_a=\sum_{X:a\in X}y_{pX}=m
\]

by (1A.6).  Therefore

\[
X_j=\{g_j,g_{j-1},\ldots,g_{j-m+1}\}.
\]

The overlap identities in (1A.2) give

\[
d_t(X_j)=g_{j-t+1}\qquad(t\le K),
\]

so this is precisely an exact wreath packet carrying the prescribed flags.

Conversely, use its packet membership and successor arcs for `y,z`.  On each
cycle, send `n-1,n-2,...,1` units successively away from the anchor; these
flows satisfy (1A.7)-(1A.9).  QED.

The system has polynomial size in its explicit owner compatibility graph.
It is an exact integer-flow characterization, not a proof that the LP
relaxation is integral.

## 2. Radius-one departure permutations

Fix one row and write

\[
\tau(i)=i+r_i\pmod n
\]

for its departure permutation.  In the radius-one corridor, put

\[
r_i=m+\delta_i,qquad \delta_i\in\{-1,0,1\}.
\tag{2.1}
\]

Since the row has `nm` coordinate-owner incidences,

\[
\sum_i\delta_i=0.
\tag{2.2}
\]

### Lemma 2.1 (adjacent-transposition normal form)

If `i\mapsto i+delta_i` is a permutation of `Z_n` and (2.2) holds, then its
nonfixed points are disjoint adjacent transpositions.  Equivalently, there is
a matching `M` in the cyclic graph on `Z_n` such that every edge
`\{i,i+1\}\in M` has

\[
\delta_i=1,\qquad \delta_{i+1}=-1,
\tag{2.3}
\]

and all other `delta`'s vanish.

#### Proof

Every cycle of the permutation uses only loops and edges of the underlying
coordinate cycle.  A permutation cycle of length at least three must
therefore be the whole cyclic graph, oriented entirely forward or entirely
backward; a proper induced subgraph is a path and has no cycle.  These two
possibilities have `sum_i delta_i=n` and `-n`, respectively, contradicting
(2.2).  Every remaining nontrivial permutation cycle is an adjacent
transposition, and distinct permutation cycles are vertex-disjoint.  QED.

For a transposition (2.3), coordinate `g_i` stays one owner too long and
`g_{i+1}` leaves one owner too early.  The only changed owner slot is

\[
j=i+m,
\]

where

\[
X_j=W_j-\{g_{i+1}\}+\{g_i\}.
\tag{2.4}
\]

## 3. Exact seam-cycle theorem

Return to the fixed oriented factor `F`.  Its slot set is

\[
\mathcal V=[B]\times\mathbb Z_n.
\]

Every slot `v=(p,j)` is a possible seam.  Put `i=j-m` and define

\[
a_v=g_{p,i},\qquad b_v=g_{p,i+1},
\]

\[
J_v=W_v-\{b_v\}+\{a_v\}.
\tag{3.1}
\]

Because the shadows of `F` cover `Omega` exactly, there is a unique slot
`phi(v)` satisfying

\[
W_{\phi(v)}=J_v.
\tag{3.2}
\]

Thus `phi` defines a functional digraph `D_F` on `mathcal V`.  It has no
loops, since `J_v!=W_v`.

Two seam slots in one factor row conflict when their indices are consecutive
modulo `n`; their corresponding adjacent transpositions would share an
arrival coordinate.  Call `S\subseteq\mathcal V` **row-independent** when it
contains no such pair.

For `q<=m-1`, both `a_v` and `b_v` lie outside the deletion core `C_q(v)`.
Define the seam target and its histogram-change vector by

\[
M_q(v)=L_q(v)-\{b_v\}+\{a_v\},
\tag{3.3}
\]

\[
\omega_v
=\sum_{q=1}^K
  \bigl(e_{(q,M_q(v))}-e_{(q,L_q(v))}\bigr).
\tag{3.4}
\]

Let `mu^F` be the vector of all canonical target histograms through depth
`K`, and let `mathcal B` be the product of the balanced boxes

\[
c_q\le b(q,T)\le c_q+1,qquad
\sum_Tb(q,T)=W.
\tag{3.5}
\]

### Theorem 3.1 (radius-one shadow-clean seam cycles)

Assume `K<=m-1`.  Radius-one shadow-clean schedules with shadow factor `F`
are in bijection with sets `S\subseteq\mathcal V` satisfying

\[
\boxed{
S\text{ is row-independent},\qquad \phi(S)=S.}
\tag{3.6}
\]

The schedule is balanced through `K` if and only if, in addition,

\[
\boxed{
\mu^F+\sum_{v\in S}\omega_v\in\mathcal B.}
\tag{3.7}
\]

For the corresponding schedule,

\[
\boxed{\Delta=|S|.}
\tag{3.8}
\]

Every row remains one exact labelled `n`-cycle, and the same owner
permutation is used at every depth.

#### Proof

Given a radius-one schedule, Lemma 2.1 gives disjoint adjacent
transpositions in every row.  Record their changed slots in `S`.  This is
row-independent, and (2.4) says that the actual owners are

\[
X_v=
\begin{cases}
W_{\phi(v)},&v\in S,\\
W_v,&v\notin S.
\end{cases}
\tag{3.9}
\]

The unselected actual owners are exactly the shadows indexed by
`\mathcal V\setminus S`.  Hence all actual owners occur exactly once if and only
if the multiset `phi(S)` is exactly `S`.  In that event `phi` restricts to a
bijection of `S`, which is (3.6).

Conversely, let (3.6) hold.  Apply the adjacent departure transposition
associated with every `v in S`.  Row-independence makes these transpositions
disjoint, so Lemma 2.1 gives a legal radius-one residence schedule.  Equation
(3.9) and `phi(S)=S` show that the actual owners are again exactly `Omega`,
once each.  Reading consecutive slots in each original row therefore defines
one common owner permutation with `B` cycles of length `n`.

Each transposition contributes

\[
\frac12(|1|+|-1|)=1
\]

to the residence defect, proving (3.8).  For `q<=m-1`, the deleted labels at
the changed slot have arrival indices

\[
i+m-q+1,\ldots,i+m,
\]

so neither `i` nor `i+1` is deleted.  Therefore its actual target is exactly
(3.3), while every unselected target remains canonical.  Summing these
changes gives (3.7), which is plainly equivalent to fiber balance.  QED.

### Corollary 3.2 (polynomial seam-cycle catalog)

The condition `phi(S)=S` says exactly that `S` is a union of directed cycles
of the functional digraph `D_F`.  These cycles can be listed in time linear
in `|mathcal V|=W`.  Delete every directed cycle which contains an internal
row conflict, and put a conflict edge between two remaining cycles whenever
their union has a row conflict.  Then radius-one owner-preserving schedules
are exactly stable sets in this cycle-conflict graph; balance is the vector
condition (3.7), and cost is the sum of the selected cycle lengths.

In particular, if `g_seam(F)` is the length of the shortest internally
row-independent directed cycle of `D_F`, every noncanonical radius-one
shadow-clean schedule satisfies

\[
\Delta\ge g_{\rm seam}(F).
\tag{3.10}
\]

This is an exact quantitative obstruction, although `g_seam(F)` need not be
large.

The raw cycle-selection family is a matroid precisely when its conflict graph
is a disjoint union of cliques.  Indeed, stable sets of a cluster graph form a
partition matroid.  Conversely, an induced path `u-v-w` violates exchange
between the stable sets `\{v\}` and `\{u,w\}`.  Thus a direct matroidal or
polymatroidal Hall theorem is unavailable whenever this conflict graph has an
induced three-vertex path.  This does not exclude an extended formulation.

### Corollary 3.3 (cost of a seam solution)

If `S` satisfies (3.6)-(3.7), then, relative to `F`, at most `|S|` labelled
owners can disagree at any depth `q<=K`.  Hence

\[
\sum_{q=1}^K\frac{e_q(F,P)}{c_q}
\le |S|S_K.
\tag{3.11}
\]

Thus a balanced seam solution with

\[
|S|=o(W/S_K)
\tag{3.12}
\]

proves the desired labelled bound.  Since `S_K=O_A(sqrt(m))`, the simpler
condition `|S|=o(W/sqrt(m))` is sufficient.

## 4. A geometric obstruction for every low-defect schedule

The preceding section used radius one.  The next theorem has no displacement
restriction.

For `k=m-q`, let `J(n,k)` carry its graph distance

\[
d_J(R,T)=k-|R\cap T|=\frac12|R\mathbin\triangle T|.
\tag{4.1}
\]

Let

\[
\mu_q^F(R)=|\{v:L_q(v)=R\}|
\tag{4.2}
\]

be the canonical factor histogram.  Define `T_q(F)` to be the minimum of

\[
\sum_{R,T}d_J(R,T)x_{R,T}
\tag{4.3}
\]

over nonnegative transports satisfying

\[
\sum_Tx_{R,T}=\mu_q^F(R),
\tag{4.4}
\]

and

\[
c_q\le\sum_Rx_{R,T}\le c_q+1.
\tag{4.5}
\]

The total mass in (4.4) makes the sink mass in (4.5) equal to `W`
automatically.

### Theorem 4.1 (Johnson--Hall transport obstruction)

The program (4.3)-(4.5) has an integral optimum.  If

\[
W=c_qN_q+\rho_q,
\]

then

\[
\boxed{
T_q(F)=
\max_{\varphi:\,\operatorname{Lip}_{J}\varphi\le1}
\left[
\sum_R\mu_q^F(R)\varphi(R)
-c_q\sum_T\varphi(T)
-\operatorname{Top}_{\rho_q}(\varphi)
\right],}
\tag{4.6}
\]

where `Top_rho(varphi)` is the sum of the `rho` largest values of `varphi`
on the rank-`k` layer.

Every shadow-clean schedule with shadow factor `F` and residence defect
`Delta` satisfies

\[
\boxed{T_q(F)\le\Delta\qquad(1\le q\le K).}
\tag{4.7}
\]

More strongly,

\[
\boxed{
\sum_{q=1}^K\frac{T_q(F)}{c_q}
\le S_K\Delta.}
\tag{4.8}
\]

#### Proof

The constraints (4.4)-(4.5) are a transportation network with integral
supplies and integral lower and upper sink capacities.  Network total
unimodularity gives an integral optimum.

For a fixed sink histogram `b`, Kantorovich duality on the finite Johnson
metric gives

\[
\min_x\sum d_Jx
=\max_{\operatorname{Lip}_J\varphi\le1}
  \sum_R\varphi(R)(\mu_q^F(R)-b(R)).
\]

The balanced sink polytope is a translated hypersimplex.  For fixed
`varphi`, its maximum scalar product is

\[
\max_b\sum_Tb(T)\varphi(T)
=c_q\sum_T\varphi(T)+\operatorname{Top}_{\rho_q}(\varphi).
\]

Finite-dimensional minimax therefore gives (4.6).  Adding a constant to
`varphi` changes neither side, so the Lipschitz feasible set may be normalized
at one vertex to make it compact.

Now take any shadow-clean schedule.  Put

\[
\kappa_v=d_J(W_v,X_v).
\]

The actual and canonical coordinate-incidence intervals have the same arrival
position and lengths `r_{p,i}` and `m`.  Double-counting their symmetric
differences gives the coarea identity

\[
\sum_v\kappa_v
=\frac12\sum_{p,i}|r_{p,i}-m|=\Delta.
\tag{4.9}
\]

Both `W_v` and `X_v` contain the complete visible core `C_K(v)`, hence also
`C_q(v)`.  Removing this common core preserves symmetric difference, so

\[
d_J(L_q(v),Q_q(v))=d_J(W_v,X_v)=\kappa_v.
\tag{4.10}
\]

Counting the slot pairs `(L_q(v),Q_q(v))` gives an integral transport from
`mu_q^F` to the actual depth-`q` histogram.  That histogram is balanced, and
the transport cost is `sum_v kappa_v=Delta`.  This proves (4.7).  Multiply by
`1/c_q`, sum over `q`, and use (4.9) to obtain (4.8).  QED.

### Corollary 4.2 (relation to overload)

Let

\[
O_q^{\rm dist}(F)
=\frac12\min_{b\in\mathcal B_q}
\|\mu_q^F-b\|_1,
\tag{4.11}
\]

where `mathcal B_q` is the set of integral balanced histograms at rank
`m-q`.  Then

\[
\boxed{
O_q^{\rm dist}(F)\le T_q(F)
\le (m-q)O_q^{\rm dist}(F).}
\tag{4.12}
\]

#### Proof

Every unit moved off the diagonal costs at least one, so any transport costs
at least half the `ell^1` change of its marginals.  This proves the lower
bound.  Choose a balanced `b` attaining (4.11).  Exactly
`O_q^{dist}` units must be moved.  The diameter of `J(n,m-q)` is `m-q`, so
transporting those units arbitrarily from surplus to deficit sites costs at
most `(m-q)O_q^{dist}`.  QED.

The quantity in (4.11) is the exact floor/ceiling overload distance.  Thus
`T_q` refines overload by charging the Johnson distance through which every
correcting unit must travel.

Consequently, a necessary condition for the shadow-clean lemma on the fixed
window is the existence of one exact factor `F` with

\[
\sum_{q\le K}\frac{T_q(F)}{c_q}=o(W).
\tag{4.13}
\]

If the left side is `Omega(W)` for a proposed factor, (4.8) forces
`Delta=Omega(W/S_K)`, excluding every low-defect schedule over that factor.
Formula (4.6) supplies an explicit polynomially checkable certificate.

## 4A. Prefix-type Euler components

The Johnson transport obstruction starts from a proposed shadow factor.  The
next obstruction is computable directly from the balanced deletion words and
applies before a shadow factor has been found.

Assume `K>=2`.  For every owner define its ordered head and tail types

\[
h(X)=(d_1(X),\ldots,d_{K-1}(X)),\qquad
t(X)=(d_2(X),\ldots,d_K(X)).
\tag{4A.1}
\]

Make a directed multigraph `D_K` whose vertices are ordered `(K-1)`-types and
whose owner-edge is

\[
t(X)\longrightarrow h(X).
\tag{4A.2}
\]

If `sigma X` is the successor of `X`, the exact visible overlap law is

\[
t(\sigma X)=h(X).
\tag{4A.3}
\]

Thus a `sigma`-cycle with no failed overlaps is literally a directed
edge-circuit of `D_K`.

For a type `s`, put

\[
A_s=|\{X:h(X)=s\}|,\qquad
B_s=|\{X:t(X)=s\}|,
\]

and define

\[
\eta_K=\frac12\sum_s|A_s-B_s|.
\tag{4A.4}
\]

Let `mathfrak H` be the weak components of `D_K`.  Write `Omega_H` for the
owner-edges of component `H` and

\[
I_H(x)=|\{X\in\Omega_H:x\in X\}|.
\tag{4A.5}
\]

Define the component point-bias

\[
\boxed{
\mathfrak B_K
=\frac12\sum_{H\in\mathfrak H}\sum_{x\in[n]}
\left|I_H(x)-\frac{m|\Omega_H|}{n}\right|.}
\tag{4A.6}
\]

### Theorem 4A.1 (Euler Hall and component-isotropy obstruction)

The following statements hold.

1. The owner-edges can be partitioned into directed circuits obeying every
   visible overlap if and only if

   \[
   A_s=B_s\qquad\text{for every type }s.
   \tag{4A.7}
   \]

2. Over arbitrary owner permutations, with no restriction on orbit lengths,
   the minimum possible number of failed overlaps (4A.3) is exactly
   `eta_K`.
3. If an exact-overlap schedule consists of rainbow cycles of length `n`,
   then

   \[
   n\mid|\Omega_H|\qquad(H\in\mathfrak H)
   \tag{4A.8}
   \]

   and its residence defect satisfies

   \[
   \boxed{\Delta\ge\mathfrak B_K.}
   \tag{4A.9}
   \]

4. More generally, let `T` be the number of failed overlaps in a rainbow
   arrival/support schedule whose owner permutation still has only cycles of
   length `n`.  Then

   \[
   T\ge\eta_K,
   \tag{4A.10}
   \]

   and

   \[
   \boxed{
   \Delta+m(m+1)T\ge\mathfrak B_K.}
   \tag{4A.11}
   \]

#### Proof

The indegree of type `s` in `D_K` is `A_s`, and its outdegree is `B_s`.
A finite directed multigraph decomposes into directed circuits exactly when
every vertex has equal indegree and outdegree.  This proves part 1.

For an arbitrary successor permutation, a successful join ending at type
`s` pairs an owner with head `s` to an owner with tail `s`.  There can be at
most `min(A_s,B_s)` such pairs.  Hence at least

\[
W-\sum_s\min(A_s,B_s)
=\frac12\sum_s|A_s-B_s|=\eta_K
\]

joins fail.  Conversely, independently match `min(A_s,B_s)` heads and tails
of each type and pair all remaining left and right owners arbitrarily.  This
is a perfect matching between predecessor and successor copies of the owner
set and hence an owner permutation with exactly `eta_K` failed joins.  This
proves part 2 and (4A.10).  Orbit-length and support constraints may increase
the minimum, never decrease it.

Under exact overlap, every owner cycle is a directed edge-circuit and is
contained in one weak component `H`.  If every cycle has length `n`, its
edges partition `Omega_H` into `|Omega_H|/n` cycles, proving (4A.8).

For a rainbow cycle `C`, put

\[
s_C(x)=|\{X\in C:x\in X\}|.
\]

The unique entrant labelled `x` resides in exactly `s_C(x)` owners of the
cycle, so

\[
\Delta_C=\frac12\sum_x|s_C(x)-m|.
\tag{4A.12}
\]

For the cycles contained in component `H`,

\[
\sum_{C\subset H}s_C(x)=I_H(x),
\qquad
\#\{C:C\subset H\}=\frac{|\Omega_H|}{n}.
\]

The coordinatewise triangle inequality now gives

\[
\sum_{C\subset H}\Delta_C
\ge\frac12\sum_x
\left|I_H(x)-\frac{m|\Omega_H|}{n}\right|.
\]

Summing over components proves (4A.9).

For the robust statement, discard every `n`-cycle containing a failed join.
At most `T` cycles, hence at most `nT` owners, are removed.  The half-`ell^1`
change in the bias vector of one component after removing owner `X` is at
most

\[
\frac12\left\|\mathbf1_X-\frac mn\mathbf1\right\|_1
=\frac{m(n-m)}n=\frac{m(m+1)}n.
\tag{4A.13}
\]

Thus removing all bad cycles changes `mathfrak B_K` by at most
`m(m+1)T`.  Every remaining cycle lies inside one type component, so (4A.9)
applies to the remaining system.  Its residence defect is at most the total
`Delta`, proving (4A.11).  QED.

Theorem 4A.1 is a genuinely polynomial Hall obstruction: the type counts,
weak components, divisibilities, and point biases are obtained by one scan of
the owner words.  Owner support and exact-arrival restrictions only delete
type-compatible joins, so they cannot invalidate any lower bound above.

For exact-prefix shadow-clean scheduling, `T=0`.  Therefore the necessary
conditions sharpen to

\[
A_s=B_s\text{ for all }s,\qquad
n\mid|\Omega_H|\text{ for all }H,
\qquad
\mathfrak B_K=o(W/S_K).
\tag{4A.14}
\]

Fiber balance alone does not visibly imply the last two componentwise laws.

### Proposition 4A.2 (sharp endpoint-switch packet)

Let `K<=m-2` and put

\[
h=m-K-1.
\]

There is one simple rainbow `n`-cycle with exact visible overlap, pairwise
distinct canonical middle shadows, uniform deletion columns, and pairwise
distinct depth-`q` targets for every `q<=K`, but with

\[
\boxed{\Delta=\mathfrak B_K=h=m-K-1.}
\tag{4A.15}
\]

#### Proof

Use the arrival order `g_i=i` on `Z_n`.  Start with canonical residence `m`
and exchange the two canonical departure slots of arrivals `0` and `h`.
The resulting residence vector is

\[
r_0=m+h,qquad r_h=m-h=K+1,qquad
r_i=m\quad(i\ne0,h).
\tag{4A.16}
\]

The departure map is still a permutation, its residence sum is `nm`, and its
minimum residence is `K+1`; the exact residence classification therefore
gives a legal cycle through depth `K`.  If

\[
W_j=\{j-m+1,\ldots,j\},
\]

the actual owners are

\[
X_j=
\begin{cases}
W_j-\{h\}+\{0\},&m\le j\le m+h-1,\\
W_j,&\text{otherwise}.
\end{cases}
\tag{4A.17}
\]

All indices in the exceptional range are ordinary representatives between
`0` and `2m`; the interval in (4A.17) contains `h` and excludes `0`.
Its replacement has a visible gap at `h`, so it is not a cyclic `m`-interval.
The two interval endpoints determine `j`, proving that all exceptional sets
are distinct from one another and from the canonical owners.  Hence the
actual cycle is simple and its canonical shadows are distinct.

At depth `q<=K`, the exceptional target is similarly

\[
\{j-m+1,\ldots,j-q\}-\{h\}+\{0\}.
\tag{4A.18}
\]

The interval still contains `h`, because `j-q>=m-K=h+1`.  The same gap and
endpoint argument proves that these targets are pairwise distinct and do not
collide with the canonical interval targets.  Since
`d_t(X_j)=j-t+1`, every deletion column is a coordinate permutation and all
overlap identities hold.

All owner-edges of the cycle lie in one weak type component.  Its point
incidences are the residence vector (4A.16), so (4A.6) gives

\[
\mathfrak B_K
=\frac12(|h|+|-h|)=h=\Delta.
\]

This proves sharpness.  QED.

This is a one-packet obstruction, not a balanced simple-owner resolution on
all of `Omega`.  Symmetrizing it gives a uniform multicover, not one copy of
each middle owner.  Thus it proves sharpness and defeats purely local
laminar criteria, but is not a conjectural counterexample.

## 5. Packet-forced point margins and the direct TU obstruction

The polynomial flow `T_q(F)` deliberately relaxes the coordinate point
margins.  A genuine common `n`-cycle schedule has stronger sink constraints.
For `k=m-q`, each coordinate occurs in exactly `B` deletion words at each
position, and it occurs in `mB` middle owners.  Hence its actual depth-`q`
incidence is

\[
kB.
\tag{5.1}
\]

Write a balanced histogram as

\[
b(T)=c_q+h(T),\qquad h(T)\in\{0,1\}.
\]

Its high-target family has size `rho_q`, and (5.1) is equivalent to the exact
degree law

\[
\sum_{T\ni x}h(T)=D_q
=kB-c_q\binom{n-1}{k-1}
=\frac{k\rho_q}{n}
\qquad(x\in[n]).
\tag{5.2}
\]

The middle expression proves in particular that `D_q` is an integer.

Define `T_q^{pr}(F)` by adding (5.1) to the sink constraints in (4.3)-(4.5),
with `+infinity` if no such integral sink exists.  Every shadow-clean schedule
satisfies

\[
\boxed{\Delta\ge T_q^{\rm pr}(F)\ge T_q(F).}
\tag{5.3}
\]

The first inequality follows from the same slot transport used in Theorem
4.1.

### Proposition 5.1 (determinant-`2` point-margin minor)

For every `2<=k<=n-3`, the natural high-target incidence matrix in (5.2) is
not totally unimodular.

#### Proof

Choose a `(k-2)`-set `R` and three coordinates `a,b,c` outside it.  On the
point rows `a,b,c` and the three high-target columns

\[
R\cup\{a,b\},\qquad
R\cup\{a,c\},\qquad
R\cup\{b,c\},
\]

the incidence matrix is

\[
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix},
\]

whose determinant is `-2`.  QED.

For fixed `A` and `q<=A sqrt(m)`, the rank `k=m-q` lies in this range for all
large `m`.  Therefore the direct transportation-plus-point-margin matrix is
not TU throughout the Gaussian window.  Adding the visibly laminar prefix
rows does not remove this square minor.  This proves only a no-go for the raw
variables; a larger TU extension or a different combinatorial theorem remains
possible.

The same obstruction occurs directly in the anchored packet equations.
Assume `K<=m-2`, choose a common `(m-2)`-set `C`, and choose three coordinates
`a,b,c` outside it.  The owners

\[
X_{ab}=C\cup\{a,b\},\qquad
X_{bc}=C\cup\{b,c\},\qquad
X_{ac}=C\cup\{a,c\}
\tag{5.4}
\]

can be given the same legal ordered `K`-prefix inside `C`.  On the packet
point rows `a,b,c`, their assignment columns give

\[
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix},
\tag{5.5}
\]

again of determinant `2`.  The three equations with right side one have the
unique solution `(1/2,1/2,1/2)`.  Thus even inside one common-prefix fiber,
the natural packetwise point subsystem of Theorem 1A.1 is not TU.

## 5A. Factorial hidden-queue obstruction to local Hall states

There is a separate obstruction to enforcing residence by a polynomial
cut-local state expansion.

Put

\[
s=m-K.
\]

At one visible cut, the recent deletion prefix

\[
(d_1,\ldots,d_K)
\]

is ordered, while the older coordinates

\[
R=X\setminus\{d_1,\ldots,d_K\},\qquad |R|=s,
\]

are visible only as an unordered set.  Exact residence nevertheless requires
a specific ordered continuation on `R`; the next hidden deletion letter and
all later ones depend on that order.

### Theorem 5A.1 (factorial local-memory lower bound)

Any cut-local path-state network which recognizes exact length-`m` residence
from the visible ordered `K`-prefix and unordered residual set must have at
least

\[
s!
\tag{5A.1}
\]

states over some single visible cut state.  This holds for deterministic
networks and, by the fooling-set bound, for nondeterministic path networks.

#### Proof

Write `R=\{u_1,\ldots,u_s\}`.  For every permutation `pi\in S_s`, choose an
exact cyclic history whose hidden required continuation order is

\[
u_{\pi(1)},\ldots,u_{\pi(s)}
\]

at the cut, while its visible prefix and residual set are the fixed data
above.  Such a history is obtained by placing these coordinates in that order
immediately before the visible recent arrivals in the cyclic coordinate
word.  Its valid continuation must remove the residual coordinates in the
same order.

If `rho!=pi`, splice the history with hidden order `rho` to the continuation
for `pi`.  At the first position at which the orders differ, the continuation
removes a coordinate which is not the oldest resident, so exact residence
fails.  The history/continuation pairs therefore form a fooling set of size
`s!`, proving (5A.1).  QED.

For `K<=A sqrt(m)`, one has `s>=m/2` for all large `m`, and

\[
s!\ge(m/4)^{m/4}>W^C
\tag{5A.2}
\]

for every fixed constant `C`, since `W<=2^{2m+1}`.  Hence no
polynomial-size cut-local hidden-state network can enforce residence on the
Gaussian window.  This does not exclude the global anchored MILP, an
algebraic extended formulation, or a theorem which reasons about whole
cycles at once.

## 6. What remains

The seam-cycle theorem gives a concrete sufficient replacement for the
original shadow-clean lemma.

### Unproved lemma SCYCLE-A

For every fixed `A` and all sufficiently large `m`, there is one oriented
exact factor `F` such that its seam functional digraph admits a
row-independent invariant set `S` satisfying the balanced vector condition
(3.7) and

\[
|S|=o(W/S_K).
\tag{6.1}
\]

By Corollary 3.3, SCYCLE-A proves the stronger labelled common-owner bound.
It is more restrictive than the general shadow-clean lemma because it uses
only radius-one departure transpositions.

Theorem 4A.1 gives a still earlier necessary gate: the chosen balanced words
must have an Eulerian type graph, component sizes divisible by `n`, and

\[
\mathfrak B_K=o(W/S_K).
\tag{6.2}
\]

Even after this componentwise isotropy holds, Theorem 4.1 exposes another
necessary precursor for any more general proof:
choose one exact factor for which the geometric transport condition (4.13)
holds, and then lift all rankwise min-cost transports to one common owner
permutation with exact `n`-cycles.  Rankwise flow integrality does not perform
this lift.  The lift must simultaneously enforce:

1. one interval of coordinate residence in every row;
2. exact ownership of all middle sets;
3. one common nested prefix for every owner;
4. all floor/ceiling target fibers; and
5. the point-regular bonus laws (5.2).

No theorem establishing this lift is proved here.

## 7. Adversarial audit

The principal steps were independently checked with the following scope
corrections.

1. **Departure normalization.**  The permutation in Lemma 2.1 is
   `i\mapsto tau(i)-m=i+delta_i`.  The two global cyclic shifts are locally
   allowed but have defect sums `+n` and `-n`; the exact incidence identity
   (2.2) excludes them.
2. **One changed owner per seam.**  A transposition of departures `i,i+1`
   changes only slot `i+m`, replacing `g_{i+1}` by `g_i`.  Disjoint
   transpositions therefore give (3.9) without interference.
3. **Exact ownership.**  The equality `phi(S)=S` is a multiset statement.
   Since `S` is a set and every shadow owner is unique, it forces `phi` to be
   a bijection on `S`; selected actual owners and unselected actual owners are
   then disjoint and jointly equal `Omega`.
4. **Truncation endpoint.**  Formula (3.3) requires `q<=m-1`.  At `q=m`, the
   shortened coordinate `b_v` is itself the missing deletion letter, so the
   radius-one construction is no longer a legal full word.
5. **One common permutation.**  The seam operation changes owner labels at
   slots, not the cyclic slot order.  After (3.6), every owner occurs once,
   so advancing one slot defines a genuine permutation of `Omega` with exact
   `n`-cycles.  All depths use that same permutation.
6. **Transport cost.**  Equation (4.10), not merely an inequality, holds
   because the complete visible core lies in both the actual and shadow
   owner.  Therefore every rank uses the same total cost `Delta`.
7. **Dual sign.**  The balanced sink chooses its `rho_q` bonus entries at the
   largest values of `varphi` when maximizing `b dot varphi`; hence the dual
   subtracts `Top_{rho_q}(varphi)`.  If the canonical histogram is already
   balanced, this makes every dual value nonpositive and the optimum zero, as
   required.
8. **TU claim.**  Proposition 5.1 refutes only the natural incidence
   formulation.  A determinant-`2` minor cannot rule out a polynomial
   algorithm, a regular-hypergraph theorem, or a totally unimodular extended
   formulation.
9. **Type-component triangle inequality.**  Exact overlap keeps every packet
   inside one weak component of `D_K`; the component bias is computed from
   the fixed labelled owner supports, not from a relabelled multicover.  The
   robust constant in (4A.11) is `m(m+1)` because one removed owner changes
   half-`ell^1` bias by `m(m+1)/n` and at most `nT` owners are discarded.
10. **Endpoint-switch scope.**  Proposition 4A.2 is a simple one-packet
   example and attains the component bound exactly.  Its symmetric orbit is
   only a multicover; no embedding into a balanced one-copy owner universe is
   claimed.
11. **Factorial-state scope.**  Theorem 5A.1 rules out networks whose state at
   a cut stores only polynomially many refinements of the visible prefix and
   residual set.  It does not rule out the global anchored MILP or a
   nonlocal algebraic extension.
12. **No global obstruction claimed.**  The geometric cost `T_q(F)` may be
   small for a well-chosen factor.  No `Omega(W)` lower bound uniform over all
   exact factors is proved.

The audited conclusion is therefore limited but exact: zero-defect
packetization has a polynomial anchored MILP but no direct TU relaxation;
the type components and Johnson transport give polynomial quantitative
obstructions to every low-defect schedule; and exact owner preservation in
the first nontrivial corridor is a cycle-selection problem, not an ordinary
laminar matching.  The unresolved step is the common cyclic lift in Section
6.
