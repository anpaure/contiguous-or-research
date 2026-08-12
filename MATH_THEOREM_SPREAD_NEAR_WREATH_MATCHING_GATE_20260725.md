# A spread near-wreath matching is enough for prime-cycle smoothing

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The pre-smoothing object does not need balanced shadows, near-rainbow
shadows, or even a pointwise polylogarithmic load cap.  It is enough to
have a random middle-disjoint family of almost all wreath packets whose
two-packet inclusion probabilities are at most a subpolynomial multiple
of the independent scale.

More precisely, let `D` be the number of wreath packets containing one
fixed middle set.  If a distribution on middle-disjoint families `P` of
`R` packets satisfies

\[
 nR=W-L,\qquad L\le Wm^{-1/2+o(1)},
\tag{0.1}
\]

and

\[
 \Pr(E,E'\in P)\le {K_m\over D^2}
 \quad(E\ne E'),
 \qquad K_m=m^{o(1)},
\tag{0.2}
\]

then, in prime dimension, some realization of `P` and some coordinate
prime cycle have aggregate orbit-mass floor `o(W)` through every fixed
Gaussian window `q<=A sqrt(m)`.

The remaining packet theorem has an exact star quotient.  Fixing one
coordinate changes the packet matching problem into an `m`-uniform
matching problem with relative pair codegree `O(m^-2)`, together with a
conflict graph encoding overlaps on the complementary side.  A spread
conflict-free near-perfect matching in this quotient would prove (0.1)--
(0.2).

This note proves the reduction.  It does not prove the spread matching
lemma.

## 1. Exact packet degrees

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B={W\over n}.
\]

Let `mathcal W` be the set of unoriented wreath packets, each packet being
the `n` length-`m` cyclic intervals of one cyclic coordinate order.  Write

\[
 D={m!(m+1)!\over2}.
\tag{1.1}
\]

Every middle set lies in exactly `D` packets, and hence

\[
 |\mathcal W|=BD.
\tag{1.2}
\]

At depth `q`, put

\[
 N_q=\binom n{m-q},\qquad \lambda_q={W\over N_q}.
\]

Every packet contains exactly `n` distinct cyclic intervals of length
`m-q`.  Coordinate transitivity and double counting therefore show that
every fixed depth-`q` target belongs to exactly

\[
 \boxed{d_q=\lambda_qD}
\tag{1.3}
\]

packets.  In particular, `d_q=O_A(D)` uniformly for
`q<=A sqrt(m)`.

## 2. Pair spread gives subpolynomial shadow energy

Let `P` be a random middle-disjoint family of exactly `R` packets.  At
depth `q`, let

\[
 \mu_q(S)=\#\{E\in P:S\text{ is a depth-}q\text{ interval of }E\},
\]

and put

\[
 T=nR=W-L,\qquad \lambda'_q={T\over N_q},\qquad
 f'_q=\mu_q-\lambda'_q\mathbf1.
\]

### Theorem 2.1 (spread-to-energy transfer)

Assume (0.2).  Uniformly for `q<=A sqrt(m)`,

\[
 \boxed{\mathbb E\|f'_q\|_2^2=O_A(K_mW).}
\tag{2.1}
\]

#### Proof

The factorial pair moment is

\[
 P_q(P)=\sum_S\binom{\mu_q(S)}2
       =\sum_{\{E,E'\}\subseteq P}
          |I_q(E)\cap I_q(E')|,
\tag{2.2}
\]

where `I_q(E)` is the set of the `n` depth-`q` intervals of `E`.
Using (0.2) and then (1.3),

\[
\begin{aligned}
 \mathbb EP_q(P)
 &\le {K_m\over D^2}
       \sum_S\binom{d_q}{2}\\
 &\le {K_mN_q\lambda_q^2\over2}
  ={K_mW\lambda_q\over2}
  =O_A(K_mW).
\end{aligned}
\tag{2.3}
\]

Since the total depth mass is deterministically `T`,

\[
 \|f'_q\|_2^2
 =T+2P_q(P)-{T^2\over N_q}
 \le W+2P_q(P).
\tag{2.4}
\]

Take expectations and use `K_m>=1`.  This proves (2.1). \(\square\)

The pointwise pair-spread hypothesis is stronger than necessary.  The
proof uses only the aggregate conclusions

\[
 \mathbb EP_q(P)=O_A(K_mW)
 \quad(q\le A\sqrt m).
\tag{2.5}
\]

## 3. Joint averaging: one matching and one cycle suffice

Assume now that `n` is prime.  For a coordinate `n`-cycle `sigma`, let
`Pi_sigma` denote averaging over its cyclic subgroup.  The exact conjugacy
class identity gives, for every centered rank function (point margins are
not required),

\[
 \mathbb E_\sigma\|\Pi_\sigma f'_q\|_2^2
 \le {1\over n}\|f'_q\|_2^2.
\tag{3.1}
\]

Let

\[
 \mathfrak D_{\sigma,q}(P)
 =\sum_{\text{target orbits }O}(n-t_{O,q})_+,
\tag{3.2}
\]

where `t_(O,q)` is the total occurrence mass on `O`.  This is the exact
token-level floor left after independent movement around the prime-cycle
orbits.

### Theorem 3.1 (random spread near-factor smoothing)

Suppose (0.1)--(0.2) hold with

\[
 K_m=m^{o(1)}.
\]

For every fixed `A`, some realization `P` and one coordinate `n`-cycle
`sigma` satisfy

\[
 \boxed{
 \sum_{q\le A\sqrt m}\mathfrak D_{\sigma,q}(P)=o(W).}
\tag{3.3}
\]

#### Proof

The proof averages over `P` and `sigma` jointly, so it does not require a
single preselected matching to satisfy a uniform energy bound at every
depth.

Put `delta=L/W`.  Choose

\[
 Q=m^{1/4+o(1)}
\tag{3.4}
\]

large enough that

\[
 Q\ge (K_mm)^{1/4},\qquad Q\ge2\sqrt{m\delta}.
\tag{3.5}
\]

Choose a fixed constant `C=C(A)` large enough for the surplus estimate
below.  For the shallow depths `q<=CQ`, the orbit floor obeys

\[
 \mathfrak D_{\sigma,q}(P)
 \le (N_q-T)_++\sqrt{N_q}\|\Pi_\sigma f'_q\|_2.
\tag{3.6}
\]

Summing through `CQ`, then using Cauchy--
Schwarz, Jensen, (3.1), and Theorem 2.1, gives

\[
 \mathbb E_{P,\sigma}\sum_{q\le CQ}\mathfrak D_{\sigma,q}(P)
 \le O(QL)+O_A\left(QW\sqrt{K_m/m}\right)=o(W).
\tag{3.7}
\]

For depths `q>CQ`, the exact
central-binomial product and (3.5) give

\[
 \lambda'_q-1\ge c_A{q^2\over m}.
\tag{3.8}
\]

The surplus-sensitive orbit inequality is

\[
 \mathfrak D_{\sigma,q}(P)
 \le {\|\Pi_\sigma f'_q\|_2^2
          \over4(\lambda'_q-1)}.
\tag{3.9}
\]

Consequently (3.1), Theorem 2.1, and
`sum_(q>Q)q^(-2)=O(1/Q)` give

\[
 \mathbb E_{P,\sigma}\sum_{q>CQ}
 \mathfrak D_{\sigma,q}(P)
 =O_A(K_mW/Q)=o(W).
\tag{3.10}
\]

Indeed, under (0.1), `K_m=m^(o(1))`, and (3.4), the three normalized
errors in (3.7)--(3.10) are

\[
 Q\delta=m^{-1/4+o(1)},\qquad
 Q\sqrt{K_m/m}=m^{-1/4+o(1)},\qquad
 K_m/Q=m^{-1/4+o(1)}.
\]

Thus the joint expectation is `o(W)`, and one deterministic pair
`(P,sigma)` attains at most that expectation. \(\square\)

## 4. Exact star quotient of the packet matching problem

Fix a coordinate `v`, and split the middle layer as

\[
 \mathcal P_v=\{X:v\in X\},\qquad
 \mathcal Q_v=\{X:v\notin X\}.
\]

Every wreath packet contains exactly `m` members of `P_v` and `m+1`
members of `Q_v`.  Define an `m`-uniform multihypergraph `H_v` on
`P_v`: the edge corresponding to a packet `E` is `E cap P_v`.  Put a
conflict between two packet edges precisely when their `Q_v` traces
intersect.

### Proposition 4.1 (quotient equivalence)

A packet family is middle-disjoint if and only if its traces form a
matching in `H_v` and contain no conflict.  A conflict-free matching of
size `B` is an exact wreath factor.

#### Proof

The two conditions say respectively that no middle owner in `P_v` and no
middle owner in `Q_v` is repeated.  This is exactly middle-disjointness.
At size `B`, the selected packets contain `mB=|P_v|` distinct `P_v`
owners and `(m+1)B=|Q_v|` distinct `Q_v` owners, so they partition the
whole middle layer. \(\square\)

Every `P_v` vertex has degree `D`.  If distinct `A,B in P_v` have
Johnson distance `d`, their packet codegree is

\[
 {\deg(A,B)\over D}
 ={2\over\binom md\binom{m+1}d}.
\tag{4.1}
\]

Because `A` and `B` both contain `v`, one has `1<=d<=m-1`, and hence

\[
 \boxed{\Delta_2(H_v)\le {2D\over m(m+1)}.}
\tag{4.2}
\]

Thus the star quotient improves the relative pair codegree from the
`Theta(1/m)` disjoint-pair scale in the full packet hypergraph to
`O(1/m^2)`.  The conflict graph has the elementary maximum-degree bound

\[
 \Delta(\mathcal C_v)\le(m+1)D,
\tag{4.3}
\]

because a packet has `m+1` owners on the `Q_v` side and each belongs to
`D` packets.

## 5. The exact remaining matching statement

The following statement is sufficient for Theorem 3.1 and hence for the
prime-cycle orbit-mass step.

### Spread conflict-free star matching lemma (open)

There is a distribution on conflict-free matchings `P` in `H_v` such
that

\[
 |P|\ge B-Bm^{-1/2+o(1)}
\tag{5.1}
\]

deterministically (or after conditioning on a positive-probability event),
and

\[
 \Pr(E,E'\in P)\le {m^{o(1)}\over D^2}
\tag{5.2}
\]

for every two distinct packet edges.

By Proposition 4.1 this is a distribution on genuine middle-disjoint
wreath rows.  Theorems 2.1 and 3.1 then supply one such near-factor and
one common prime coordinate cycle with aggregate orbit floor `o(W)` on
every fixed Gaussian window.

The star codegree (4.2) is at the desired `m^-2` scale, but (5.1)--(5.2)
do not follow merely from that number: the `Q_v`-conflict system and the
growing edge size `m` must be controlled simultaneously.  No such theorem
is claimed here.

## 5A. Exact complement-geodesic quotient of the high-codegree backbone

The only pair codegrees of relative order `1/m` in the full packet
hypergraph have a rigid source.  They can be bundled before any nibble is
run.

Fix `v` and put `U=[n] minus {v}`.  Linearize a packet at `v` as

\[
 (v,a_1,\ldots,a_{2m}).
\]

Its `m+1` middle intervals avoiding `v` are

\[
 Q_i=\{a_{i+1},\ldots,a_{i+m}\},\qquad 0\le i\le m,
\tag{5A.1}
\]

and put `Z_i=U minus Q_i`.  Then

\[
 Z_0,Z_1,\ldots,Z_m
\tag{5A.2}
\]

is a Johnson geodesic from `Z_0` to its complement: consecutive vertices
have distance one and `Z_m=U minus Z_0`.  If

\[
 C_i=Z_{i-1}\cap Z_i\qquad(1\le i\le m),
\tag{5A.3}
\]

then the `m` middle intervals containing `v` are exactly

\[
 \{v\}\cup C_1,\ldots,\{v\}\cup C_m.
\tag{5A.4}
\]

Conversely, every Johnson geodesic from an `m`-set `Z` in `U` to
`U minus Z` determines one packet, with reversal giving the same
unoriented packet.  Thus packets are precisely complement geodesics with
their rank-`m-1` edge colours.

### Proposition 5A.1 (exact backbone degrees)

Let an **endpoint atom** be an unordered complementary pair
`{Z,U minus Z}`.  Then:

1. there are `(m+1)B/2` endpoint atoms;
2. every endpoint atom supports exactly `(m!)^2` packets;
3. every incidence flag `(C subset Z)`, with `|C|=m-1` and `|Z|=m`, is
   incident with exactly `(m!)^2` packet geodesic edges;
4. every packet belongs to one endpoint atom and contains `2m` incidence
   flags, two at each of its `m` coloured edges.

#### Proof

There are `binom(2m,m)/2=(m+1)B/2` antipodal pairs.  From a specified
endpoint to its complement, a shortest path is determined independently
by the order in which the `m` old elements are removed and the `m` new
elements are inserted.  This gives `(m!)^2` geodesics, and choosing a
canonical member of the unordered endpoint atom removes the reversal
ambiguity.

For the flag count, double-count packet--edge-end incidences.  There are
`BD` packets and `2m` flags per packet.  There are

\[
 \binom{2m}{m-1}(m+1)=m(m+1)B
\]

flags.  Their common degree is therefore

\[
 {2mBD\over m(m+1)B}={2D\over m+1}=(m!)^2.
\]

The remaining statements follow from (5A.1)--(5A.4). \(\square\)

The disjoint-pair codegree in the full packet hypergraph is exactly

\[
 {2D\over m+1}=(m!)^2.
\tag{5A.5}
\]

Such a disjoint pair must lie in `Q_v`, and it is precisely one endpoint
atom.  Every other pair has relative codegree at most
`2/[m(m+1)]`.  Hence all relative-`Theta(1/m)` codegree has been
identified with the endpoint-atom partition; off this backbone the
relative codegree is `O(m^-2)`.

There is also an exact spread proposal before owner conflicts are imposed.
Independently activate every endpoint atom with probability `2/(m+1)`;
at an active atom choose one of its `(m!)^2` geodesics uniformly.  Then
every packet has marginal probability

\[
 {2\over(m+1)(m!)^2}={1\over D},
\tag{5A.6}
\]

and two packets have joint probability zero when they share their endpoint
atom and exactly `1/D^2` when their endpoint atoms are distinct.  The
expected number of proposed rows is `B`.

This proposal already has the ideal pair spread.  Its defect is solely
that different proposed geodesics may reuse an internal `Q_v` vertex or
an edge colour `C`, i.e. a middle owner on one of the two star sides.
Consequently the spread matching gate can equivalently be read as a
conflict-resolution theorem for independently proposed complement
geodesics.  No high-codegree pair remains hidden inside that formulation.

## 6. Exact overlap mass and the first nibble bite

The maximum codegree alone is pessimistic for the star trace.  The large
codegrees occur on only a linear number of pairs inside one packet path.
This gives an exact aggregate estimate.

For a packet `E`, let `E_v=E cap P_v`.  Ordered by consecutive cyclic
starts, `E_v` is a path of `m` middle sets.  Two members separated by `s`
path steps have Johnson distance `s`.  Hence

\[
 \boxed{
 {1\over D}\sum_{\{X,Y\}\subseteq E_v}\deg(X,Y)
 =\sum_{s=1}^{m-1}(m-s)
   {2\over\binom ms\binom{m+1}s}
 =O(1/m).}
\tag{6.1}
\]

Indeed, the `s=1` term is less than `2/m`.  For
`2<=s<=m-1`,

\[
 \binom ms\binom{m+1}s\ge {m^2(m+1)\over2},
\]

so all remaining terms sum to `O(1/m)`.

For the full packet, its `n` middle owners are the length-`m` intervals
of one cyclic order.  There are exactly `n` unordered pairs at every
circular separation `1<=s<=m`.  Therefore

\[
 \boxed{
 {1\over D}\sum_{\{X,Y\}\subseteq E}\deg(X,Y)
 =n\sum_{s=1}^{m}
   {2\over\binom ms\binom{m+1}s}=O(1).}
\tag{6.2}
\]

The only constant-order contribution is `s=m`, namely
`2n/(m+1)<4`; the other terms are `O(1/m)` in total.

Let `N(E)` be the set of all packets sharing at least one middle owner
with `E`, including `E` itself.  Bonferroni and (6.2) give an absolute
constant `C` such that

\[
 \boxed{(n-C)D\le |N(E)|\le nD.}
\tag{6.3}
\]

Likewise, the packet neighbourhood generated only by `E_v` has size

\[
 \boxed{mD-O(D/m)\le
 \left|\bigcup_{X\in E_v}\{F:X\in F\}\right|
 \le mD.}
\tag{6.4}
\]

These estimates justify one complete random-greedy bite without any
fixed-uniformity black box.  Sample every packet independently with

\[
 p={\theta\over nD},
\tag{6.5}
\]

where `theta>0` is fixed, and retain a sampled packet exactly when no
other sampled packet intersects it in a middle owner.  The retained rows
form a genuine middle matching.  Uniformly in `E`,

\[
\begin{aligned}
 \Pr(E\text{ retained})
 &=p(1-p)^{|N(E)|-1}\\
 &= {\theta e^{-\theta+o(1)}\over nD}.
\end{aligned}
\tag{6.6}
\]

Thus the expected number of retained rows in one bite is

\[
 \boxed{
 \mathbb E|P_1|={\theta e^{-\theta+o(1)}\over n}B.}
\tag{6.7}
\]

Moreover, for distinct packets,

\[
 \boxed{
 \Pr(E,E'\in P_1)\le p^2
 ={\theta^2\over n^2D^2}.}
\tag{6.8}
\]

So the desired spread scale is automatic for one bite.  The obstruction
is not time zero: one bite covers only `Theta(1/n)` of the middle layer.

To reach leave `m^(-1/2+o(1))`, the natural trajectory requires
`Theta(n log m)` bites.  At residual vertex density `u`, the formal
pseudorandom recurrence is

\[
 d(u)=Du^{n-1},\qquad
 {\Delta_2(u)\over d(u)}\le {2+o(1)\over mu}.
\tag{6.9}
\]

At the stopping density `u=m^(-1/2+o(1))`, the right side is still
`m^(-1/2+o(1))`, while Stirling's formula gives

\[
 \log d(u)=(1+o(1))m\log m,
\tag{6.10}
\]

so the residual degrees remain enormous.  Equations (6.9)--(6.10) are
favourable numerical scales, but they are not a proof: one must establish
the survival-conditioned degree recurrence and cumulative pair spread.

The exact dynamic theorem left by this calculation is:

> **Hereditary packet-nibble lemma.**  Through residual density
> `m^(-1/2+o(1))`, the actual conflict-free packet nibble retains the
> recurrence (6.9) with summable exceptional mass and ends with
> `Pr(E,E' selected)<=m^(o(1))/D^2`.

The first-bite identities (6.1)--(6.8) prove that neither the star-side
maximum codegree nor the full packet's disjoint-neighbour pairs obstruct
the start of this recurrence.  What is missing is its hereditary,
conditioned version.

## 7. Exact status

Proved:

* the packet and target degrees (1.1)--(1.3);
* pair spread implies expected Gaussian-window energy
  `O_A(K_mW)`;
* joint matching/cycle averaging removes the need for a factor which is
  good at every depth separately;
* a leave `Wm^(-1/2+o(1))` and spread loss `m^(o(1))` are sufficient;
* the exact conflict-free star quotient and its `O(m^-2)` pair codegree;
* the edgewise overlap-mass estimates and one complete spread nibble bite.

Still unproved:

* the spread conflict-free star matching lemma;
* after orbit-floor smoothing, the separate row-power lift which realizes
  the token moves while retaining almost all middle ownership.
