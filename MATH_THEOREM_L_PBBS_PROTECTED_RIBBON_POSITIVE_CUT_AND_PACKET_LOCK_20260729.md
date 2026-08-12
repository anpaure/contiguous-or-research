# Protected ribbon positive cuts, packet locks, and the exact PBBS extraction gate

Date: 2026-07-29

Status: exact quantifier correction; exact ribbon/genus component formula;
exact mixed-integer circulation/forest formulation; smallest nonloop
threshold-relevant protected connected-switch local minimum; exact additive compensation-flow
theorem; conditional PBBS descent criteria.  No literal PBBS local minimum is
constructed, and no universal PBBS positive-cut theorem is claimed.

## 1. Result and scope

This note audits the positive-cut property left in Section 7 of
`MATH_THEOREM_L_PBBS_COMPONENT_REDUCTION_AND_BOUNDARY_CAPACITY_20260729.md`.
There are two inequivalent meanings of that property.

* If an exchange may be an **arbitrary protected rematching**, positive cut
  is not a local theorem.  It is exactly the assertion that the present
  matching is not a global minimum of component count in the fixed protected
  fibre.  The all-state assertion above two components is equivalent to the
  existence of a protected factor with at most two components.
* If an exchange must be **one connected alternating circuit**, the assertion
  is genuinely local, but it is false for general protected matching fibres.
  A smallest nonloop six-row example below is a protected local minimum with three
  components even though a protected packet of two alternating `C6`'s reaches
  one component.

The exact topological statistic is a ribbon-surface Euler characteristic.  If
`pi` is a packet on `s` marked ports, `rho` is the old-fragment return
permutation, `t=c(rho)`, `o` is the number of orbits of
`<pi,rho>`, `b` is the cycle rank of the packet--component incidence graph,
and `g` is the total ribbon genus, then the fusion gain is

\[
 \boxed{\Gamma_F(\pi)
 =c(F)-c(F\pi)=t-o-b+2g.}                         \tag{1.1}
\]

For one connected alternating circuit this specializes to

\[
 \boxed{\Gamma_F(\pi)=2t-s-1+2g.}                \tag{1.2}
\]

Consequently every protected connected circuit with

\[
                         s\le 2t-2                 \tag{1.3}
\]

is automatically an improving cut.  In particular, a protected circuit
using one port in each of at least two old components always improves.

Formula (1.1) also proves why a generic potential/flow proof cannot finish
the PBBS theorem.  Protection may require mutually compensating circuits,
while `g` may be created only by their compound cyclic interleaving.  The
missing PBBS input is therefore a **protected negative-circuit extraction
theorem**, or the weaker plateau-escape version stated in Section 9.  It must
couple literal chronology accessibility to the ribbon topology; deck Hall
flow or all-depth support alone does not provide it.

## 2. Static protected fibre and the quantifier correction

Let `X,Y` have the same finite cardinality.  Fix a perfect matching

\[
                         M_0:X\longrightarrow Y
\]

and an absolute protected fibre `Fcal` of allowed perfect matchings
`P:X -> Y`.  Membership in `Fcal` means that all fixed requirements pass:

1. every immutable short-deck load has its required lower bound;
2. the exact residence test passes;
3. every required lower and upper target has a literal chronological
   witness; and
4. any other fixed owner or collar constraint in the carrier definition
   passes.

Put

\[
  \sigma_P=M_0^{-1}P,\qquad
  \kappa(P)=c(\sigma_P),\qquad
  \kappa_* = \min_{Q\in\mathcal F}\kappa(Q).       \tag{2.1}
\]

For `P,Q in Fcal`, there is a unique permutation

\[
                         \pi=P^{-1}Q               \tag{2.2}
\]

such that `Q=P pi`.  On the support of `pi`, let `rho_P(pi)` send a marked
port to the next marked port on its old `sigma_P`-cycle.
For the identity rematching, use the empty-support convention
`c(rho_P(id))=c(id rho_P(id))=0`.

### Theorem 2.1 (arbitrary-packet PC is global minimality)

For every `P in Fcal`,

\[
 \min_{\pi:\,P\pi\in\mathcal F}
 \left[c(\pi\rho_P(\pi))-c(\rho_P(\pi))\right]
       =\kappa_* -\kappa(P).                       \tag{2.3}
\]

Hence the arbitrary-packet positive-cut property

\[
 \mathrm{PC}_{\rm all}(P):\quad
 \exists\pi, P\pi\in\mathcal F,
 \quad c(\pi\rho_P(\pi))<c(\rho_P(\pi))           \tag{2.4}
\]

holds if and only if `kappa(P)>kappa_*`.  More generally, for every integer
threshold `B`,

\[
 \left[
  \forall P\in\mathcal F,\quad
  \kappa(P)>B\Longrightarrow\mathrm{PC}_{\rm all}(P)
 \right]
 \quad\Longleftrightarrow\quad
                         \kappa_*\le B.             \tag{2.5}
\]

#### Proof

The map `Q -> P^{-1}Q` is a bijection between `Fcal` and all protected
rematchings from `P`.  The exact cut--join identity gives

\[
 \kappa(P\pi)-\kappa(P)
   =c(\pi\rho_P(\pi))-c(\rho_P(\pi)).              \tag{2.6}
\]

Taking the minimum over `Q=P pi in Fcal` proves (2.3) and (2.4).  If
`kappa_*<=B`, a jump from any state above `B` to a minimizer is a positive
cut.  Conversely, if `kappa_*>B`, a global minimizer itself lies above `B`
and has no positive cut.  This proves (2.5).  `square`

Thus Theorem 7.2 of the preceding note is logically correct as written, but
with arbitrary rematchings its hypothesis already contains its desired
topological endpoint.  It is not a local-minimum reduction.

The genuine circuit-local property is

\[
 \mathrm{PC}_{\rm circ}(P):\quad
 \exists\pi\text{ with one nontrivial cycle},\quad
 P\pi\in\mathcal F,\quad
 \kappa(P\pi)<\kappa(P).                           \tag{2.7}
\]

Equivalently, form the graph whose vertices are protected matchings and whose
edges are connected alternating-circuit exchanges.  Orient an edge toward
lower `kappa`.  Property (2.7) says that `P` is not a sink.

## 3. The ribbon Euler identity

Fix one exchange packet `pi` with support `S`, and put

\[
 s=|S|,\qquad k=c(\pi),\qquad t=c(\rho),\qquad
 h=c(\pi\rho).                                      \tag{3.1}
\]

Here the cycles counted by `k` are exactly the connected alternating
circuits in the matching difference, while the cycles counted by `t` are
the old factor components touched by the packet.  Let

\[
 o=\#\operatorname{Orb}\langle\pi,\rho\rangle       \tag{3.2}
\]

on `S`.

Construct a bipartite incidence multigraph `B(pi,rho)` as follows.

* Its black vertices are the cycles of `pi`.
* Its white vertices are the cycles of `rho`.
* Every `x in S` is an edge joining its `pi`-cycle to its `rho`-cycle.
* The cyclic orders of half-edges at black and white vertices are induced by
  `pi` and `rho`, respectively.

Its connected components are precisely the orbits in (3.2).  Its first
Betti number is

\[
 b=s-(k+t)+o.                                        \tag{3.3}
\]

### Theorem 3.1 (ribbon/genus formula)

There is a nonnegative integer `g`, the sum of the genera of the orientable
ribbon components, such that

\[
 \boxed{k+t+h=s+2o-2g.}                             \tag{3.4}
\]

Consequently

\[
 \boxed{
 \begin{aligned}
 \kappa(P\pi)-\kappa(P)&=b-t+o-2g,\\
 \Gamma_P(\pi):=\kappa(P)-\kappa(P\pi)&=t-o-b+2g.
 \end{aligned}}                                     \tag{3.5}
\]

#### Proof

Thicken `B(pi,rho)` according to the stated cyclic orders.  A boundary
traversal beginning at the black half-edge labelled `x` crosses its edge,
turns at the white vertex according to `rho`, crosses back, and turns at the
black vertex according to `pi`.  The induced two-step boundary permutation
on black half-edges is therefore

\[
                         x\longmapsto\pi\rho(x).     \tag{3.6}
\]

Thus the ribbon thickening has `h=c(pi rho)` boundary components.  Cap every
boundary component by a disk.  This gives `o` closed connected orientable
surfaces.  With `k+t` vertices, `s` edges, `h` faces, and total genus `g`,
Euler's formula gives

\[
                   (k+t)-s+h=2o-2g,                 \tag{3.7}
\]

which is (3.4).  In particular `g` is an integer and is nonnegative.  The
cut--join identity

\[
 \kappa(P\pi)-\kappa(P)=-t+h                       \tag{3.8}
\]

together with (3.3)--(3.4) gives (3.5).  `square`

The term `2g` is a genuine fusion resource.  It is invisible to raw counts
of packet blocks and touched components.  It can arise already for one
circuit and can also increase nonadditively when several circuits are
combined.

### Corollary 3.2 (one connected circuit)

If `pi` is one `s`-cycle, then `k=o=1`, `b=s-t`, and

\[
 \boxed{
 \Gamma_P(\pi)=2t-s-1+2g
              =t-1-(s-t)+2g.}                      \tag{3.9}
\]

It is an improving cut if and only if

\[
                         2t+2g>s+1.                 \tag{3.10}
\]

In particular:

1. `s<=2t-2` implies strict improvement without any genus information;
2. `s=2t-1` is neutral at genus zero and improving at every positive genus;
3. if exactly one marked port lies in each touched old component, then
   `s=t`, `rho=id`, `g=0`, and the gain is `t-1`.

#### Proof

A single cycle of `pi` is transitive on `S`, so `o=1`.  Substitution in
(3.3) and (3.5) gives (3.9).  If one port lies in each touched component,
`rho=id`; hence `pi rho=pi` has one cycle and the gain is `t-1`.  `square`

### Corollary 3.3 (exact local-minimum inequalities)

At a protected packet-local minimum, every protected packet satisfies

\[
                         b\ge t-o+2g.               \tag{3.11}
\]

At a protected connected-switch local minimum, every protected circuit
satisfies

\[
                 s-t\ge t-1+2g,
 \qquad\text{equivalently}\qquad
                 s\ge2t-1+2g.                      \tag{3.12}
\]

Thus a local minimum contains no protected component-simple circuit touching
two or more components.  More generally, every protected genus-`g` circuit
must revisit its touched components at least `t-1+2g` times beyond their
first visits.

#### Proof

Nonnegative component derivative in (3.5) gives (3.11); specialize with
`k=o=1` to obtain (3.12).  `square`

Equations (3.11)--(3.12), rather than a signed Gram estimate, are the sharp
topological obstruction at a protected local minimum.

## 4. Exact circulation and forest formulation

Relabel the right shore by the current matching `P`.  Put an allowed arc

\[
                         x\longrightarrow y          \tag{4.1}
\]

whenever the replacement edge `(x,P(y))` is available.  An integral binary
circulation `z` with

\[
 \sum_{y\ne x}z_{xy}=\sum_{y\ne x}z_{yx}\le1
 \quad (x\in X)                                     \tag{4.2}
\]

is a vertex-disjoint family of directed cycles, hence an exchange packet.
Conversely every exchange packet has this form.

When a support `S` is fixed in advance, the circulation must additionally
satisfy the exact support equations

\[
 \sum_{y\ne x}z_{xy}=
 \sum_{y\ne x}z_{yx}=
 \begin{cases}
 1,&x\in S,\\
 0,&x\notin S.
 \end{cases}                                        \tag{4.3}
\]

For an immutable additive deck colour `a`, define

\[
 D_{a,xy}=
  {\bf1}_{\{\ell(x,P(y))=a\}}
  -{\bf1}_{\{\ell(x,P(x))=a\}}.                     \tag{4.4}
\]

The exact deck-capacity row is

\[
                  \lambda_P(a)+\sum_{x,y}D_{a,xy}z_{xy}
                  \ge b_a,                          \tag{4.5}
\]

where `b_a=1` for ordinary completeness and may be any fixed integral quota.

There is also an exact graphic-rank formulation of the cut objective.  For a
fixed selected support `S`, let `E_tau` be the undirected edge multiset

\[
            E_\tau=\{\{x,\tau(x)\}:x\in S\},
 \qquad \tau=\pi\rho.                               \tag{4.6}
\]

Loops are allowed and have graphic rank zero.  Since the components of this
functional graph are the cycles of `tau`,

\[
 \operatorname{rk}_{\rm gr}(E_\tau)=s-c(\tau).      \tag{4.7}
\]

Therefore

\[
 \boxed{
 \Gamma_P(\pi)=
 \operatorname{rk}_{\rm gr}(E_{\pi\rho})
 -\operatorname{rk}_{\rm gr}(E_\rho).}              \tag{4.8}
\]

As `rk(E_rho)=s-t`, positive cut is equivalent to the existence of a forest
`J subseteq E_(pi rho)` with

\[
                         |J|\ge s-t+1.               \tag{4.9}
\]

Equivalently, introduce forest variables `y_e`, indexed by the individual
edge copies of the multigraph, and impose

\[
 \begin{aligned}
  0&\le y_e\le {\bf1}_{\{e\in E_{\pi\rho}\}},\\
  \sum_{e\in E(U)}y_e&\le |U|-1
       &&(\varnothing\ne U\subseteq S),\\
  \sum_e y_e&\ge s-t+1.                             \tag{4.10}
 \end{aligned}
\]

Conditional on a fixed integral `tau`, the forest subsystem is integral.
Thus, for fixed `S`, (4.2)--(4.5), an exact mixed-integer encoding of the
matching-to-fragment relation `tau=pi rho`, (4.10), and the exact chronology
oracle form a fail-closed mixed-integer positive-cut master.  No total
unimodularity or integrality of the joint `z`--`tau`--chronology relaxation is
claimed.

There are two important limitations.

1. If `S` varies, `rho` is the next-selected-port permutation and itself
   depends on `S`.  One must either enumerate/branch on `S` or encode this
   next-occurrence relation exactly.
2. Residence and arbitrary-width lower/upper witness survival are not
   generally additive rows like (4.5).  For two packets,

   \[
    \Delta_T(\pi_1\pi_2)
      =\Delta_T(\pi_1)+\Delta_T^{P\pi_1}(\pi_2),     \tag{4.11}
   \]

   and the second term need not equal `Delta_T^P(pi_2)`.  A protected window
   may meet both surgery collars.  These predicates require the combined
   associative fragment-summary automaton or a full physical replay.  They
   become additive only under a separately proved collar-separation theorem.

Thus (4.2)--(4.11) is an exact potential/flow recasting, but it does not create
the missing protected circulation.

### Proposition 4.1 (reversibility obstruction to a direction-free potential)

Let `V` be a state function on the protected connected-circuit exchange
graph.  If `V(Q)<=V(P)` for every legal switch `P -> Q`, with no external
orientation of the switch, then `V` is constant on every connected component
of that graph.

#### Proof

Every protected circuit switch is reversible: the inverse switch takes `Q`
back to `P` and both endpoints remain protected.  Applying the assumed
inequality in both directions gives `V(P)=V(Q)` on every edge.  `square`

Thus the ribbon gain is an exact **edge certificate**, not a scalar state
invariant that forces an available edge.  Any successful PBBS descent theorem
must prove protected expansion or impose a reference-dependent orientation.

## 5. Smallest nonloop threshold-relevant protected circuit local minimum

The following example shows that even topologically perfect `C6` cuts can be
locked by exact integral deck capacity.

Let

\[
 X=Y=\mathbb Z_6,\qquad M_0=\mathrm{id},\qquad
 P=(0\ 1)(2\ 3)(4\ 5).                              \tag{5.1}
\]

Put

\[
 \pi_E=(0\ 2\ 4),\qquad
 \pi_O=(1\ 3\ 5),\qquad
 Q=P\pi_E\pi_O.                                     \tag{5.2}
\]

The four perfect matchings obtained by the two partial choices are

\[
 \begin{aligned}
 P&=(0\ 1)(2\ 3)(4\ 5),\\
 P_E=P\pi_E&=(0\ 3\ 2\ 5\ 4\ 1),\\
 P_O=P\pi_O&=(0\ 1\ 2\ 3\ 4\ 5),\\
 Q=P\pi_E\pi_O&=(0\ 3\ 4\ 1\ 2\ 5).
 \end{aligned}                                      \tag{5.3}
\]

All are nonloop, and

\[
          \kappa(P)=3,\qquad
          \kappa(P_E)=\kappa(P_O)=\kappa(Q)=1.       \tag{5.4}
\]

Take the allowed variable-edge graph to be `G=P union Q`.  Since the relative
permutation `pi_E pi_O` has two disjoint three-cycles, `G` is the disjoint
union of two bipartite alternating `C6`'s.  Its perfect matchings are exactly

\[
                         P, P_E, P_O, Q.           \tag{5.5}
\]

Give every allowed edge one of two immutable deck colours `a,b`:

* on even rows, colour the `P`-edge `a` and the `Q`-edge `b`;
* on odd rows, colour the `P`-edge `b` and the `Q`-edge `a`.

Require both colours.  The exact loads are

\[
\begin{array}{c|cc|c}
\text{matching}&\lambda(a)&\lambda(b)&\kappa\\ \hline
P   &3&3&3\\
P_E &0&6&1\\
P_O &6&0&1\\
Q   &3&3&1.
\end{array}                                         \tag{5.6}
\]

### Theorem 5.1 (minimal nonloop packet-locked local minimum)

With deck completeness as protection, the protected fibre in `G` is exactly
`{P,Q}`.  The state `P` has three components and has no protected connected
alternating-circuit neighbour, while the protected two-`C6` packet `P -> Q`
has fusion gain two.  No nonloop example above the stopping threshold two can
use fewer than six rows.  Here “nonloop” means that the initial matching `P`
is edge-disjoint from `M_0`, equivalently `M_0^{-1}P` is fixed-point-free.

#### Proof

Equation (5.5) lists every perfect matching.  Equation (5.6) shows that
exactly `P,Q` cover both colours.  The only connected exchanges from `P` are
the two alternating `C6`'s, and both fail one deck colour.  Their product is
protected and changes `kappa` from three to one.

For minimality, if `M_0^{-1}P` is fixed-point-free, every one of its cycles
has length at least two.  More than two components therefore require at least
`2+2+2=6` points.  `square`

This proves minimality only in shore size under the stated fixed-point-free
and above-two hypotheses.  It does not assert minimality in number of deck
colours, packet size, or literal PBBS physical size.

Each forbidden `C6` is component-simple: it takes one port from each of the
three old components.  Corollary 3.2 gives gain two before protection is
considered.  Thus the obstruction is not weak topology; it is an exact
resource deadlock.

No chronological predicates are imposed in this abstract fibre; equivalently,
any extra abstract chronology predicates are universal on its four states.
Therefore the example
refutes any connected-PC theorem deduced only from the general fixed-matching
and additive-load axioms.  It is **not** a literal PBBS counterexample:
the two colours in (5.6) have not been embedded as Johnson target labels, and
no physical PBBS chronology realizing this six-row gadget is asserted.

The example does not refute `PC_all`: the compound matching `Q` witnesses
`PC_all(P)`.  This is exactly the distinction in Theorem 2.1.

## 6. A second obstruction: compound genus synergy

The failure above comes from nonhereditary protection.  Even if every partial
matching is protected, component topology itself need not admit a descending
constituent.

Let `M_0=id` on ten points and put

\[
 \begin{aligned}
 P&=(0\ 8)(1\ 9)(2\ 3\ 4\ 5\ 6\ 7),\\
 \pi_1&=(0\ 2\ 6\ 4),\\
 \pi_2&=(1\ 3\ 7\ 5).
 \end{aligned}                                      \tag{6.1}
\]

The supports of `pi_1,pi_2` are disjoint.

Take the allowed variable-edge graph to be

\[
                         G=P\cup P\pi_1\pi_2.       \tag{6.2}
\]

It consists of the two alternating `C8` components indexed by `pi_1,pi_2`,
together with the two forced shared edges.  Hence its only perfect matchings
are the four choices of those two circuit blocks.  Direct multiplication gives

\[
 \begin{aligned}
 P\pi_1&=(0\ 3\ 4\ 8)(1\ 9)(2\ 7)(5\ 6),\\
 P\pi_2&=(0\ 8)(1\ 4\ 5\ 9)(2\ 3)(6\ 7),\\
 P\pi_1\pi_2&=(0\ 3\ 2\ 7\ 6\ 5\ 9\ 1\ 4\ 8).
 \end{aligned}                                      \tag{6.3}
\]

All four matchings are nonloop.  Declare all of them protected.  Their
component counts on the exchange square are

\[
 \begin{array}{c|cccc}
 I&\varnothing&\{1\}&\{2\}&\{1,2\}\\ \hline
 \kappa(P_I)&3&4&4&1.
 \end{array}                                        \tag{6.4}
\]

Hence `P` is a strict connected-circuit local minimum above two: both atomic
switches are uphill, but their compound drops directly from three to one.

For either single circuit,

\[
             s=4,\quad t=2,\quad o=1,\quad b=2,
             \quad g=0,\quad \Gamma=-1.             \tag{6.5}
\]

For the compound packet,

\[
             s=8,\quad k=2,\quad t=3,\quad o=1,
             \quad b=4,\quad g=2,\quad \Gamma=2.    \tag{6.6}
\]

Thus compound ribbon genus reverses both adverse atomic derivatives.  This
rules out a proof based only on protected subcube closure or on an additive
sum of atomic topological gains.

Again, (6.1) is a generic protected matching-fibre obstruction, not a PBBS
embedding.

## 7. Exact additive compensation flow

The deck lock in Section 5 has a precise flow interpretation.

At a current matching `P`, let each additive protected target `u` have bound
`b_u` and slack

\[
                         s_u=\lambda_u(P)-b_u\ge0.   \tag{7.1}
\]

Let `C_1,...,C_m` be pairwise row-disjoint alternating circuits, so their
matching effects commute and their deck derivatives add.  Thus, for every
`I subseteq [m]`,

\[
 \lambda_u\!\left(P\oplus\bigoplus_{i\in I}C_i\right)
   =\lambda_u(P)+\sum_{i\in I}d_{iu}.               \tag{7.2}
\]

Write

\[
 d_{iu}=\lambda_u(P\oplus C_i)-\lambda_u(P),\qquad
 p_{iu}=\max(d_{iu},0),\qquad
 m_{iu}=\max(-d_{iu},0).                            \tag{7.3}
\]

A **payment certificate** consists of nonnegative integers
`a_(iu), f_(jiu)` satisfying `f_(iiu)=0` and

\[
 \begin{aligned}
  \sum_i a_{iu}&\le s_u,\\
  \sum_i f_{jiu}&\le p_{ju} &&(j,u),\\
  a_{iu}+\sum_j f_{jiu}&\ge m_{iu} &&(i,u).
 \end{aligned}                                      \tag{7.4}
\]

The variable `a_(iu)` pays demand from initial slack; `f_(jiu)` pays demand
of circuit `i` using supply created by circuit `j`.  Orient `j -> i` whenever
some `f_(jiu)>0`.

### Theorem 7.1 (prefix-feasible packet iff acyclic payment)

The circuits admit an order in which every prefix satisfies every additive
deck bound if and only if they admit a payment certificate whose dependency
digraph is acyclic.

#### Proof

Suppose first that (7.4) has an acyclic dependency graph, and take a
topological order.  For any prefix `K`, every payment arc entering a member of
`K` comes from a member of `K`.  Hence, for each target `u`,

\[
 \begin{aligned}
 \sum_{i\in K}m_{iu}
 &\le \sum_{i\in K}a_{iu}
     +\sum_{i,j\in K}f_{jiu}\\
 &\le s_u+\sum_{j\in K}p_{ju}.
 \end{aligned}                                      \tag{7.5}
\]

Therefore

\[
             s_u+\sum_{i\in K}d_{iu}\ge0,          \tag{7.6}
\]

which is prefix feasibility.

Conversely, take a prefix-feasible order.  Regard initial slack as
distinguishable tokens.  When `C_i` executes, consume `m_(iu)` available
tokens of target `u` and then create `p_(iu)` new tokens.  Since
`p_(iu)m_(iu)=0` coordinatewise, prefix feasibility after `C_i` guarantees
that the required tokens existed before its negative update.  Record whether
each consumed token came from initial slack or from an earlier circuit.  This gives
`a,f` satisfying (7.4), and every payment arc points forward in the chosen
order.  The dependency graph is therefore acyclic.  `square`

Every source of an acyclic payment graph is individually deck-feasible,
because all its demands are paid from initial slack.

In the six-row example, the bounds are one, the current loads are `(3,3)`,
and the two circuit derivatives are

\[
                    d_E=(-3,+3),\qquad
                    d_O=(+3,-3).                    \tag{7.7}
\]

The initial slack is `(2,2)`.  Circuit `E` needs at least one unit of `a`
from `O`, while `O` needs at least one unit of `b` from `E`.  Thus every
payment graph contains the directed cycle

\[
                         E\longrightarrow O
                         \longrightarrow E.          \tag{7.8}
\]

No deck-feasible first circuit exists, although the whole packet is exactly
balanced.

Theorem 7.1 applies exactly to additive lower bounds.  An additive upper
bound can be included as a second resource with slack `U_u-lambda_u(P)` and
derivative `-d_(iu)`; equality uses both directions.  Deck acyclicity gives
no chronology implication: it does not exclude a whole packet repairing a
residence or upper-window failure made by its constituents.  Exact PBBS use
requires fragment-summary or literal physical verification after each
proposed source circuit.

## 8. Two exact extraction lemmas

The preceding examples isolate two independent hypotheses: protection must
expose an atom, and topology must make some exposed atom descend.

### Theorem 8.1 (supermodular protected-atom extraction)

Let a packet decompose into pairwise disjoint permutation cycles
`pi_1,...,pi_m`, and put

\[
 P_I=P\prod_{i\in I}\pi_i,\qquad
 f(I)=\kappa(P_I).                                   \tag{8.1}
\]

Assume:

1. every singleton `P_{\{i\}}` is fully protected; and
2. `f` is supermodular on the Boolean cube, in the convention

   \[
    f(A)+f(B)\le f(A\cup B)+f(A\cap B).              \tag{8.2}
   \]

If `f([m])<f(varnothing)`, then some protected singleton circuit strictly
decreases component count.

#### Proof

For a supermodular function, marginal increments increase with the base set:

\[
 f(S\cup\{i\})-f(S)
       \ge f(\{i\})-f(\varnothing)                  \tag{8.3}
\]

whenever `i notin S`.  If every singleton increment were nonnegative, then
telescoping (8.3) along any order of `[m]` would give
`f([m])>=f(varnothing)`, a contradiction.  The extracted singleton is fully
protected by hypothesis.  `square`

Neither hypothesis is automatic.

* The six-row `C6+C6` example satisfies the topological conclusion one would
  want--each atom is strongly descending--but neither singleton is protected.
* The ten-row example has every singleton protected, but (8.2) fails since

  \[
                       4+4\nleq 3+1.                 \tag{8.4}
  \]

Thus endpoint protection plus a lower packet endpoint does not imply local
descent.

### Theorem 8.2 (cut-rooted acyclic saturation)

Suppose every reachable fully protected state `P` with `kappa(P)>2` admits a
row-disjoint packet and an acyclic payment certificate with a source circuit
`C` such that:

1. its ribbon data satisfy

   \[
                         2t_C+2g_C>s_C+1;            \tag{8.5}
   \]

2. exact fragment-summary or literal replay proves that the matching
   \(P\oplus C\) preserves every nonadditive protected predicate, including
   residence, every required lower/upper chronological target, and every
   nonadditive owner/compiler/carrier condition.

Then a protected connected alternating circuit strictly reduces component
count at every state above two, and iteration reaches at most two components.

#### Proof

A source of the payment DAG is deck-feasible by Theorem 7.1.  Hypothesis 2
makes it fully protected.  Equation (8.5) and Corollary 3.2 make it strictly
component-decreasing.  Reapply the hypothesis after each step.  Since
component count is a nonnegative integer, the process reaches at most two
components.  `square`

A convenient stronger version replaces (8.5) by `s_C<=2t_C-2`; a
component-simple protected `C6` through three old components is the basic
case.  An ordered loose ternary fusion forest is precisely an iterated
instance of this stronger condition.

Theorem 8.2 is a real additional condition, not a consequence of packet
feasibility.  The deck gadget violates acyclic payment, while the displayed
two-circuit packet in the four-state genus gadget has no cut-positive source.

## 9. The weaker neutral-router theorem

Strict descent at the current vertex is stronger than necessary for
component reduction.  Let `G_circ` be the fully protected connected-circuit
exchange graph.  For an integer `j`, let `G_j^0` be its subgraph induced by
states with `kappa=j`, retaining only neutral edges.

### Theorem 9.1 (plateau escape)

There is a protected connected-circuit path from every state to a state with
at most two components, along which `kappa` never increases, if and only if
every neutral connected component of `G_j^0`, for every `j>2`, has an
incident protected edge to a state of smaller component count.

#### Proof

Contract each neutral component.  Every remaining nonincreasing edge strictly
lowers the integer `kappa`.  The stated exit condition lets one descend from
each contracted vertex above two; iteration terminates.  Conversely, any
nonincreasing path leaving a neutral component above two must use such a
strictly descending incident edge.  `square`

This is the exact formulation if PBBS requires a neutral legality router
before a splitter.  It is weaker than `PC_circ` at every state and stronger
than arbitrary-packet global minimality.  The strict ten-row genus example
fails even this criterion at its initial state.

## 10. PBBS consequence and the precise remaining boundary

For a literal PBBS-derived fixed-`M0` factor, define a circuit or packet to be
**endpoint-protected** only after all of the following have passed:

1. every immutable short-deck inequality;
2. exact residence at every physical lift;
3. every required fixed lower and upper layer;
4. arbitrary-width upper intervals and the corresponding lower-intersection
   oracle; and
5. any common-owner/compiler pins included in the chosen carrier class.

Then the following statements are proved.

1. Arbitrary-packet positive cut is equivalent to not being a global
   component minimizer in that fixed protected fibre.
2. Every endpoint-protected packet has the exact gain (1.1).
3. Every endpoint-protected connected circuit has the exact gain (1.2).
4. A protected circuit with at most `2t-2` marked ports in total across its
   `t` touched components necessarily descends.
5. At a connected-switch local minimum, every protected circuit obeys the
   exact revisit lower bound (3.12).
6. Generic protected matching axioms do not imply circuit descent: the
   six-row capacity lock and ten-row genus synergy are exact obstructions.

The following are not proved.

1. The six-row or ten-row obstruction has not been embedded into the literal
   PBBS Johnson chronology.
2. It is not known that a PBBS protected fibre contains a circuit or packet
   violating the local-minimum inequalities (3.11)--(3.12) at every state
   above two components.
3. It is not known that PBBS deck compensation has an acyclic cut-rooted
   payment, or that its neutral plateaux have descending exits.
4. No universal PBBS reduction to two components is currently proved from
   all-depth support, residence, and short-deck completeness.  The generic
   matching-fibre abstractions of those hypotheses are insufficient, but the
   present examples do not settle their literal PBBS specialization.

Accordingly the sharp live theorem is one of the following genuinely extra
PBBS assertions.

### Atomic protected ribbon expansion

For every reachable state `P` with `kappa(P)>2`, there is a fully protected
connected alternating circuit with

\[
                         2t+2g>s+1.                 \tag{10.1}
\]

The genus-free sufficient target is `s<=2t-2`.

### Packet protected ribbon expansion

For every such state, there is a fully protected packet with

\[
                         b<t-o+2g.                  \tag{10.2}
\]

This is exact topologically, but if arbitrary packet size is allowed at once,
Theorem 2.1 shows that its all-state form is equivalent to existence of the
desired at-most-two-component endpoint.

### Neutral protected ribbon expansion

Every protected neutral plateau above two has a fully protected descending
exit satisfying (10.1).

Any one of the atomic or neutral assertions yields monotone PBBS component
reduction.  To prove it, one must use a PBBS-specific chronology mechanism
that excludes both closed compensation SCCs and compound-genus-only fusion.
The cut--join arithmetic, the all-depth support theorem, and a static Hall
count do not exclude either obstruction.

This is the precise proved/conditional boundary of the positive-cut lane.

## 11. Independent proof audit

Three independent adversarial proof audits checked the quantifiers, product
conventions, ribbon Euler characteristic, graphic-rank sign, both explicit
permutation gadgets, the payment-token equivalence, supermodular marginal
direction, and plateau-escape quantifiers.  The audit corrections incorporated
above were:

1. genus may arise for one circuit as well as nonadditively in a packet;
2. the ten-row obstruction requires its stated four-matching allowed graph;
3. the six-row minimality is only the nonloop shore-size statement;
4. the circulation master must pin its selected support; and
5. only the forest block conditional on integral `tau` is asserted integral.

After those corrections the independent audits found no remaining sign,
composition, quantifier, or theorem-scope defect.  No computational search is
used in any proof in this note.
