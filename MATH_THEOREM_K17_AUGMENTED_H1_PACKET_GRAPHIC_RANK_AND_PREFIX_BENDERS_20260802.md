# K17 augmented-`h1` packet topology: graphic rank and prefix Benders

**Date:** 2026-08-02  
**Status:** unconditional formulation theorem.  It gives an exact topology
gate for a selector of closed `C6`, octahedral `C8`, and star-`C8` packet
exchanges.  It does not assert that the current carrier is resident, close
any deeper-upper row, or supply a source, opening, or compiler.

## 1. Literal state and the corrected topology object

Let `V` be the `48620` vertices of the augmented `h1` incidence graph and
let `M,D` be its distinguished lower vertices.  Every accepted literal
edge state `z` must satisfy

\[
 \deg_z(M)=1,\qquad \deg_z(D)=3,\qquad
 \deg_z(v)=2\quad(v\notin\{M,D\}).                 \tag{1.1}
\]

Consequently `|E(z)|=|V|`; this is not a two-factor.  The required object is
the connected unicyclic lollipop of the augmented-incidence reduction.

A closed packet `p` has selected-edge removals `R_p` and insertions `A_p`
with signed degree balance

\[
 |R_p\cap\delta(v)|=|A_p\cap\delta(v)|
 \quad(v\in V).                                    \tag{1.2}
\]

For action-disjoint packets and selector variables `x_p`, the literal state
is

\[
 z_e=b_e-\sum_{p:e\in R_p}x_p+\sum_{p:e\in A_p}x_p. \tag{1.3}
\]

If actions overlap, (1.3) must be replaced by an exact edge-state channel;
one may not add packet deltas arithmetically through an unresolved overlap.
All topology statements below concern the reconstructed physical state,
not merely a quotient representative.

## 2. Exact global rank theorem

Let `r_gr` be graphic-matroid rank and `kappa(z)` the number of connected
components of the spanning graph selected by `z`.  Since

\[
 r_{\rm gr}(E(z))=|V|-\kappa(z),                    \tag{2.1}
\]

the exact global topology row is

\[
 \boxed{r_{\rm gr}(E(z))=|V|-1.}                   \tag{2.2}
\]

Under (1.1), (2.2) is equivalent to saying that `z` is the required
lollipop.  A spanning-tree certificate is an equivalent extended
formulation: choose `t_e<=z_e` in the graphic base polytope with
`t(E)=|V|-1`.

For every nonempty proper `U subset V`, degree parity gives

\[
 z(\delta(U))\equiv
   \mathbf1_{M\in U}+\mathbf1_{D\in U}\pmod 2.     \tag{2.3}
\]

Thus an exact cut formulation of (2.2), in the presence of the integral
degree rows, is

\[
 z(\delta(U))\ge
 \eta(U):=
 \begin{cases}
  1,&|U\cap\{M,D\}|=1,\\
  2,&|U\cap\{M,D\}|\in\{0,2\}.
 \end{cases}                                       \tag{2.4}
\]

The safe generic connectivity row is `z(delta(U))>=1`; the strengthening
to two is valid only on a shore having no `M-D` imbalance.  In particular,
one must not import the all-shores `>=2` condition from an ordinary
two-factor master.

### Structural consequence

In any integral state satisfying (1.1), `M` and `D` lie in the same
component: every component contains an even number of odd-degree vertices.
If the state has `1+t` components, the component containing `M,D` is a
lollipop and the other `t` components are cycles.  Its topology-rank
deficiency is exactly

\[
 (|V|-1)-r_{\rm gr}(E(z))=t.                       \tag{2.5}
\]

Hence a packet union which "splits the factor" has created one or more
detached cycle components; each such component supplies an even-boundary
cut of right-hand side two.

## 3. Exact component delta of a packet union

For a current connected lollipop `F` and any compatible packet union `S`,
put

\[
 R_S=\bigcup_{p\in S}R_p,\quad
 A_S=\bigcup_{p\in S}A_p,\quad H_S=F-R_S.           \tag{3.1}
\]

Define the fragmentation rank and the addition rank by

\[
 s_F(R_S):=r(F)-r(H_S)=\kappa(H_S)-1,               \tag{3.2}
\]

\[
 \rho_{H_S}(A_S):=r(H_S\cup A_S)-r(H_S).            \tag{3.3}
\]

Then

\[
 \boxed{\kappa((F-R_S)\cup A_S)-1
       =s_F(R_S)-\rho_{H_S}(A_S).}                  \tag{3.4}
\]

Equivalently, contract every component of `H_S` and retain the inserted
edges `A_S`.  The resulting endpoint multigraph has exactly as many
components as the new literal state.  Thus the union is topology-safe if
and only if

\[
 \rho_{H_S}(A_S)=s_F(R_S)=\kappa(H_S)-1.            \tag{3.5}
\]

For the current lollipop, let `b` of the distinct removed edges be bridges
and let `c` be on its unique cycle.  Then

\[
 s_F(R_S)=b+\max(c-1,0).                            \tag{3.6}
\]

The bridge/cycle roles are state-dependent and must be rebuilt after every
accepted prefix.

### Why individual circuit safety does not compose

For each packet separately, the equality

\[
 \rho_{F-R_p}(A_p)=s_F(R_p)                         \tag{3.7}
\]

does not imply (3.5) for a union of packets.  The contraction `F-R_S` is
different from every contraction `F-R_p`, and graphic rank has
state-dependent, submodular marginals.  Action-disjointness preserves the
degree rows, but it does not make the endpoint-splice permutation
transitive.  Several local splices can close a proper subcollection of the
cut path pieces into a detached cycle.

Therefore the reported sixth individually safe disjoint circuit which
split the carrier is not a contradiction: its individual certificate was
relative to a stale/coarser state.  If it were tested literally against
the five-packet prefix, (3.4) would return a positive component delta and
(2.2) would fail.

## 4. Exact lazy separator and max-closure integration

The DM/max-closure selector may retain its provider-shore and two-objective
rows, but topology is a separate graphic-rank Benders oracle:

1. solve the current packet master;
2. reconstruct every physical edge state `z_e` exactly;
3. verify (1.1), then compute the connected components;
4. if connected, accept the topology row;
5. otherwise, for every decoded component `C` not containing `M`, add

\[
 z(\delta(C))\ge
 \begin{cases}
  1,&D\in C,\\
  2,&D\notin C.
 \end{cases}                                       \tag{4.1}
\]

For a degree-exact integral incumbent only the second case can occur, but
retaining both cases makes the separator fail-closed.  With explicit
edge-state literals the weaker clause

\[
 \bigvee_{e\in\delta(C)}z_e                         \tag{4.2}
\]

already excludes the incumbent; the parity row strengthens it to the
correct pseudo-Boolean lower bound.  A packet-only disjunction is sound
only after exact channeling to the edge states, because a packet may both
insert and delete edges of the same cut.

Integer separation is one connected-components computation.  Fractional
separation is also polynomial: use an `M-D` minimum cut for the right-hand
side-one family and contract `M,D` before a global minimum cut for the
right-hand-side-two family.

The rank oracle is polynomial, but the image of multi-edge signed packet
columns is not itself a graphic matroid and component delta is not a fixed
additive packet cost.  Thus a scalar topology penalty inside the
max-closure network is not exact in general.  The proof-safe composition is
DM/max-closure in the master plus the rank oracle as lazy Benders
separation.  Finiteness of the packet master and exclusion of every
disconnected integer incumbent prove termination and exactness.

If the master is orbit/voltage compressed, (2.2) is imposed on the literal
physical expansion.  Quotient connectedness alone is not a substitute;
an independently proved voltage-lift criterion would also be required.

## 5. Prefix-safe materialization

For an ordered compound packet `p_1,...,p_m`, let `F_i` be the exact state
after the first `i` packets.  A materialized chain of connected carriers is
valid if and only if

\[
 r(F_i)=|V|-1\qquad(0\le i\le m).                   \tag{5.1}
\]

Equivalently, for every step, with
`H_i=F_{i-1}-R_{p_i}`,

\[
 \rho_{H_i}(A_{p_i})=\kappa(H_i)-1.                 \tag{5.2}
\]

This is strictly stronger than checking every packet against `F_0`.
Bridge/cycle roles, endpoint components, q1 seam roles, and topology rank
are all recomputed at each prefix.  If only the final simultaneous union is
part of the theorem, only its final rank is logically necessary; a search
which claims a sequence of valid carriers must impose every row (5.1).

Stage-indexed edge states and a copy of separator (4.1) at every prefix give
an exact SAT/ILP formulation.

## 6. Smallest proof-safe neutral pivot

Let `c_F(p)=(Delta R,Delta H)` be the exact replayed residence/all-upper
cost, and let `T(F)` be the exact current family of maximum DM provider
shores.  Write `gamma_F(q)` for the minimum signed provider-survival value
of a quench `q` over `T(F)`; the acceptance threshold is zero for survival
and one when the residual rank must increase by one.

A neutral pivot `p` is useful for a strict quench `q` only if

\[
\begin{aligned}
 c_F(p)&=(0,0),\\
 r(F_p)&=|V|-1,\\
 c_{F_p}(q)&\preceq(0,0),\quad c_{F_p}(q)\ne(0,0),\\
 \gamma_{F_p}(q)&\text{ meets the required DM threshold},\\
 r(F_{p,q})&=|V|-1.                                 \tag{6.1}
\end{aligned}
\]

All palettes, upper-closure rows, and literal state gates remain hard in
both endpoint replays.  To certify that `p` genuinely breaks the current
obstruction rather than merely accompanying an already legal quench, also
require that `q` misses the threshold at `F`.

The smallest neutral pivot is the lexicographic minimum of

\[
 (|\operatorname{rootSupp}(p)|,\ |R_p|+|A_p|)       \tag{6.2}
\]

over pairs `(p,q)` satisfying (6.1), with literal prefix reconstruction.
If a proposed `q` currently detaches cycle components `C_1,...,C_t`, then
every final state must satisfy

\[
 z_{p,q}(\delta(C_j))\ge2\quad(1\le j\le t),        \tag{6.3}
\]

but these old component rows are only necessary; the final rank check in
(6.1) is the complete condition.  This criterion combines the DM reachable
shore and the topology shore without pretending that either is an
additive local score.

