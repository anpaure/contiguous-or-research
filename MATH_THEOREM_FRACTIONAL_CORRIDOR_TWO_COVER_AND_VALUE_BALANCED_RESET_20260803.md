# Fractional corridor two-covers and value-balanced compiler reset

**Date:** 2026-08-03

**Status:** unconditional fixed-child network and compiler theorems, followed
by a conditional regenerative implication with explicit constants.  The
theorems do not construct an all-dimensional bilateral bank, the required
literal corridors, an occurrence-equivariant ray host, or a regenerative
child.  In particular, bilateral occurrence support by itself does not imply
the corridor hypotheses below.

## 0. Outcome

After a coherent terminal module bank has been selected and one compensation
linkage has been fixed, the remaining supplier gate is a single-source-bank
flow problem.  It need not be verified by enumerating every Rado cut.

For every gain claim `u`, let `P_u` be a family of **actual complete residual
paths** from the private claim vertex of `u`, through one of its legal ports,
to an unused supplier sink.  If nonnegative path weights satisfy

\[
 \sum_{P\in P_u}w_{uP}=\eta
 \quad(u\in G),
 \qquad
 \sum_{u,P:\,a\in P}w_{uP}\le1
 \quad(a\text{ every unit capacity}),                 \tag{0.1}
\]

then every gain subfamily `Y` has strict-gammoid rank at least
`ceil(eta |Y|)`.  At `eta=1`, every gain is integrally serviceable.

A particularly concrete certificate is:

> every gain has `h` actual alternative complete paths, and every unit
> capacity lies on at most `b` of all displayed paths.

It gives

\[
                  \eta={h\over\max\{h,b\}}.           \tag{0.2}
\]

Thus two alternatives per gain with **combined congestion at most two** give
`eta=1`.  The displayed paths may intersect; max-flow integrality reroutes
them to a disjoint linkage.  This is weaker than demanding a preselected
disjoint corridor bank.

The lower compiler has an analogous exact certificate, but it is an
occurrence-level matching statement.  After the unaffected reference edges
are fixed, its exact casualty is the Hall deficiency of the actual final
destroyed-demand--fresh-cell graph.  Value-by-value domination makes this
deficiency zero only on the value-exact face where every equal-value
demand--cell pair is legal.  An aligned closed birail circulation supplies
the required value equality only after its formal signed action has been
lifted to actual distinct cells in one terminal cap/guard state and that
value-exact incidence hypothesis has been verified.

Finally, an occurrence-level transitive symmetry turns one legal cross-ray
edge into a perfect cross matching.  Combining these three certificates
with the existing complete-potential row gives an explicit one-step reset:

\[
 \Phi'\le
 B_0+\beta+e_G+e_{\rm comp}+e_{\rm ray}+e_{\rm other}, \tag{0.3}
\]

when all but `B_0` units of potential become gains, the compensation anchor
loses at most `beta`, the two-corridor certificate has at most `e_G`
exceptional gains, and the displayed compiler exceptions are exhaustive.

Equation (0.3) is an unconditional implication.  No current theorem
supplies its geometric hypotheses uniformly in the dimension.

## 1. Fixed residual claim network

Start with one fully materialized and replayed child and one coherent private
module bank.  Fix an independent compensation anchor `I` and one literal
linkage `L_I` routing it.  Delete every capacity and supplier sink used by
`L_I`.  The remaining vertex-split directed network is denoted by `D_I`, and
its unused sink bank by `T_I`.

For each gain claim `u`, retain its private indegree-zero claim vertex `x_u`
and its arcs to the actual residual legal port menu.  Claim-to-port prefixes
are private; all shared resources occur downstream as unit-capacity split
vertices.  Sink capacity is also represented by a unit vertex or a unit arc.
These are exactly the capacity-faithful hypotheses required by the strict-
gammoid construction.  Every structural zero is represented by the absence
of a path or arc; no completion of a projected menu is allowed.

A **literal residual corridor** for `u` is a complete directed path in
`D_I` from `x_u` to `T_I`.  It is an alternative way to service the single
claim `u`.  If the physical semantics require two phase paths
simultaneously to service one task, that task is not represented by one
strict-gammoid claim and the results below do not apply without first
retaining its paired state as a capacity-faithful gadget.

## 2. Fractional corridors are an exact hereditary rank certificate

### Theorem 2.1 (fractional-corridor criterion)

Let `G` be a finite gain-claim set in `D_I`, and let `0<=eta<=1`.  Suppose
there are nonnegative weights on literal residual corridors such that

\[
 \sum_{P\in {\cal P}_u}w_{uP}=\eta
 \qquad(u\in G),                                      \tag{2.1}
\]

and, for every finite unit-capacity vertex or arc `a` of `D_I`, including
the supplier sinks,

\[
 \sum_{u\in G}\sum_{P\in {\cal P}_u:\,a\in P}w_{uP}
 \le1.                                                \tag{2.2}
\]

Then, for every `Y subseteq G`,

\[
 \boxed{r_{D_I}(Y)\ge \lceil\eta|Y|\rceil.}           \tag{2.3}
\]

Consequently, before fixing the anchor,

\[
 r_{\cal N}(I\cup Y)-|I|\ge\eta|Y|.                  \tag{2.4}
\]

At `eta=1`, all of `I union G` is independent.

#### Proof

Restrict the weighted path family to `Y`.  Add a super-source with a
capacity-one arc to every `x_u`, and a super-sink after the unit-capacity
sink terminals.  The path weights form a feasible fractional flow of value
`eta |Y|`: (2.1) gives the flow leaving each selected claim start, and
(2.2) gives every internal and sink capacity constraint.

All network capacities are integral.  Hence the maximum flow value is an
integer at least `ceil(eta |Y|)`, and an integral maximum flow decomposes
into that many vertex-disjoint claim-to-sink paths starting at distinct
claim vertices.  This is precisely (2.3).  The deleted anchor linkage is
disjoint from the residual paths, so restoring it proves (2.4).  This is
only a one-way implication: rank in the fixed residual network can be
smaller than matroid-contraction rank because contraction may reroute the
anchor.  At `eta=1`, (2.3) gives rank `|Y|` for every `Y`, in particular
for `G`.
\(\square\)

### Proposition 2.2 (cut equivalence)

Fix the literal child, the anchor linkage and its deleted capacities and
sinks, the residual claim menus, and the unused unit-capacity sink bank.
Normalize every claim-private prefix into an infinite-capacity arc from
`x_u` to its addressed residual menu ports; all shared physical resources
remain as their actual unit-capacity split vertices or arcs.  Attach every
unused supplier sink to one supersink by its explicit unit-capacity terminal
arc.

For a set `W` of normalized base-network vertices not containing the
supersink, let `c_I(W)` be the total capacity of base-network arcs leaving
`W`, including those terminal sink arcs, and put

\[
 t_G(W)=|\{u:\text{ every residual menu port of }u\text{ lies in }W\}|.
\]

For fixed `eta`, a weighted corridor family satisfying (2.1)--(2.2) exists
if and only if every such finite-capacity trapped-menu cut satisfies

\[
                         c_I(W)\ge\eta t_G(W).        \tag{2.5}
\]

Thus (2.1)--(2.2) are a path-form certificate for the anchored Rado row,
not a stronger asymptotic assumption.

#### Proof

Necessity follows by sending the paths of each trapped claim across the cut:
they contribute weight `eta`, while each crossed unit capacity carries total
weight at most one.

For sufficiency, attach a super-source to every claim vertex by an arc of
capacity `eta`, and ask for flow value `eta |G|`.  Consider an arbitrary
finite cut and fix its base-network source side `W`.  A claim vertex can lie
on the source side only when all of its infinite-capacity menu arcs end in
`W`.  If all its ports lie in `W`, moving that claim vertex to the source
side removes its capacity-`eta` source arc and crosses no infinite arc.
Hence every finite cut normalizes, without increasing capacity, by putting
`x_u` on the source side exactly for the `t_G(W)` trapped claims.  The
normalized cut has capacity

\[
             \eta(|G|-t_G(W))+c_I(W).
\]

It has value at least `eta |G|` exactly when (2.5) holds.  Max-flow/min-cut
in this one fixed network gives the fractional flow, and path decomposition
gives (2.1)--(2.2).
\(\square\)

The equivalence is for one fixed residual network after the anchor linkage
has been deleted.  It does not permit a different child, guard, cap state,
or representation for different cuts.

### Corollary 2.3 (uniform path multiplicity versus congestion)

Suppose every gain claim has `h>=1` displayed literal residual corridors,
counted with their actual paths, and every unit capacity belongs to at most
`b>=1` displayed corridors in total.  Then Theorem 2.1 holds with

\[
                  \boxed{\eta={h\over\max\{h,b\}}.}   \tag{2.6}
\]

#### Proof

Give every displayed path weight `1/max{h,b}`.  Each claim receives total
weight (2.6), and every capacity receives load at most
`b/max{h,b}<=1`.  Apply Theorem 2.1. \(\square\)

### Corollary 2.4 (congestion-two bilateral certificate)

Suppose each gain has two actual alternative complete residual paths and
the combined multiset of all displayed paths has unit-capacity congestion
at most two.  Then all gain claims are jointly linkable, even if the
displayed paths themselves intersect.

#### Proof

Use `h=b=2` in Corollary 2.3.  The half-weighted paths form a unit flow per
claim; integral max flow produces a disjoint linkage. \(\square\)

The adjective `bilateral` is justified only when the two paths really arise
from the two named source sides in the same residual claim network.  Two
phasewise occurrence tuples, two helper hosts, or two abstract Hall edges
are not by themselves paths.  Conversely, if one phase alone already gives
a vertex-disjoint complete path for every gain, that phase alone proves full
rank and the half-weighting is redundant.

### Corollary 2.5 (two-phase partial-cover fusion)

Let `G_0,G_1 subseteq G`.  For each `phi in {0,1}`, suppose there is one
literal complete residual path `P_u^phi` for every `u in G_phi`, and the
paths are pairwise unit-capacity-disjoint **within that phase**.  Cross-phase
intersections are unrestricted.  If

\[
                             G_0\cup G_1=G,           \tag{2.7}
\]

then

\[
 r_{\cal N}(I\cup Y)-|I|\ge\left\lceil{|Y|\over2}\right\rceil
 \qquad(Y\subseteq G).                               \tag{2.8}
\]

More sharply, put `E=G minus (G_0 intersect G_1)`.  Then

\[
 r_{\cal N}(I\cup Y)-|I|
 \ge
 \left\lceil |Y|-{|Y\cap E|\over2}\right\rceil
 =|Y|-\left\lfloor{|Y\cap E|\over2}\right\rfloor
 \ge |Y|-\left\lfloor{|E|\over2}\right\rfloor.     \tag{2.9}
\]

Thus two phasewise disjoint **partial** path families whose union covers the
gain bank give `eta=1/2,gamma=0`.  If all but `e` gains occur in both phase
families, they instead give the sharper
`eta=1,gamma=floor(e/2)`.

#### Proof

Give every displayed path weight `1/2`.  Within each phase a capacity has
load at most `1/2`, so the union of the two phases has load at most one.
Every claim in the union receives at least `1/2`; a claim in the intersection
receives one.  Restriction to `Y` therefore has value

\[
 {1\over2}|Y\setminus(G_0\cap G_1)|
   +|Y\cap G_0\cap G_1|
 =|Y|-{1\over2}|Y\cap E|.
\]

Apply the integral-flow argument of Theorem 2.1. \(\square\)

This is the nonredundant phasewise use.  If both phase families contain all
gains, either one alone is already a full linkage.  If service of one claim
requires both phase paths simultaneously, the single-claim strict-gammoid
model still does not apply.

### Corollary 2.6 (bounded exceptional gains)

If Corollary 2.3 holds for `G minus E`, where `|E|<=e`, then

\[
 r_{\cal N}(I\cup Y)-|I|
 \ge\eta|Y|-\eta e\qquad(Y\subseteq G).               \tag{2.10}
\]

Thus the anchored parameters may be taken as `gamma=eta e`.  In the
congestion-two case, at least `g-e` gains are serviceable together with the
anchor.

#### Proof

Restrict to `Y minus E` and use
`|Y minus E|>=|Y|-e` in Theorem 2.1. \(\square\)

### Corollary 2.7 (full-corridor catalogue saturation)

Suppose one fixed capacity-faithful atlas exposes, for every gain claim,
`L` complete literal residual paths.  A claim-private start or prefix may
belong to all `L` paths of that claim.  Suppose every **nonprivate** unit
capacity belongs to at most `Delta` displayed paths in the union of the
catalogues.  Then Theorem 2.1 holds with

\[
                  \eta={L\over\max\{L,\Delta\}}.     \tag{2.11}
\]

In particular, if `Delta<=L`, every gain claim is jointly linkable.

#### Proof

Every private capacity has path multiplicity at most `L`; every shared
capacity has multiplicity at most `Delta`.  Apply Corollary 2.3 with
`h=L` and `b=max{L,Delta}`. \(\square\)

Consequently the often proposed scaling

\[
                L_k\ge a k^2,
 \qquad
                \Delta_k\le b k d(k),                \tag{2.12}
\]

for positive constants `a,b` and `d(k)=Theta(sqrt(k))`, closes the residual
supplier Rado gate for all sufficiently large `k`--**provided** `L_k` counts
complete paths in one capacity-faithful fixed-child atlas and `Delta_k`
counts every nonprivate physical capacity on those same paths.  Raw local
packet multiplicity, paths living in different child representations, or a
catalogue omitting compiler/history capacities does not satisfy this
hypothesis.

This replaces an independent-transversal or local-lemma selection at the
supplier stage by one fractional-flow certificate followed by integral max
flow.  It does not replace the nonmatroidal task of constructing the fixed
capacity-faithful atlas in the first place.

### Theorem 2.8 (fractional port-suffix router)

Let `B=(G,P;E)` be left `h`-regular, with right degrees
`d_p=deg_B(p)<=h`.  Suppose every edge `up` has a directed literal prefix from
`x_u` to `p`; apart from the common claim start `x_u`, all these edge
prefixes are capacity-disjoint.  Let `D_suf` be a directed unit-capacity
suffix network from the ports to unused unit-capacity supplier sinks,
disjoint from the prefix interiors.

If `D_suf` admits a fractional flow routing demand

\[
                              {d_p\over h}             \tag{2.13}
\]

from every port `p` to the sink bank simultaneously, then every claim in
`G` is jointly linkable.

Equivalently, write `c_suf(W)` for a finite sink-avoiding suffix cut and let
`P(W)` be the ports on its source side.  The exact sufficient-and-necessary
suffix condition is

\[
             \boxed{c_{\rm suf}(W)\ge
                    \sum_{p\in P(W)}{d_p\over h}}
 \qquad(W).                                           \tag{2.14}
\]

#### Proof

Send `1/h` units from `x_u` down every one of its `h` edge-private
prefixes.  Each claim emits one unit, every prefix capacity has load at most
`1/h`, and port `p` receives exactly `d_p/h`.  Continue this flow through
the hypothesized suffix flow.  The result is a feasible fractional claim-
to-sink flow of value `|G|`; Theorem 2.1 and integral max flow give a full
claim linkage.

For the cut form, add a super-source arc of capacity `d_p/h` to every port
and ask to saturate all of them.  A cut with suffix part `W` has capacity

\[
 \sum_{p\notin P(W)}{d_p\over h}+c_{\rm suf}(W).
\]

It has at least the total demand precisely under (2.14).  Max-flow/min-cut
proves the equivalence. \(\square\)

This theorem permits the suffix flow to split and recombine at ports.  That
is legitimate because all claim-specific, all-or-none packet state has
already been closed in the private prefixes; downstream supplier flow is a
single-commodity capacity problem.  If claim identity is still read after a
port, the suffix is not capacity-faithful and the theorem does not apply.
The uniform port demands `d_p/h` are a convenient sufficient certificate,
not a necessary condition for full claim linkage: a nonuniform fractional
assignment on the edges of `B` may avoid a bad port.  The exact unrestricted
condition is feasibility of unit flow from every claim in the entire
claim--`B`--suffix network, equivalently the corresponding Rado cuts.

### Corollary 2.9 (duplicated-router fixed-suffix certificate)

Let `B=(G,P;E)` be a bipartite graph such that every `u in G` has degree
exactly `h>=1` and every `p in P` has degree at most `h`.  In one fixed
residual claim network suppose:

1. every edge `up` has a directed literal prefix from `x_u` to `p`;
2. apart from the common claim start `x_u`, the prefixes belonging to
   distinct edges have disjoint capacity and are disjoint from the suffix
   interiors below; and
3. every port `p` has one directed suffix `R_p` to an unused sink.

Count sink terminals as unit capacities and define the **degree-weighted
suffix congestion**

\[
 C_R=\max_a\sum_{p:\,a\in R_p}\deg_B(p),             \tag{2.15}
\]

where `a` ranges over every unit capacity in the suffix bank.  Then the
claim bank has hereditary rank parameter

\[
                  \boxed{\eta={h\over\max\{h,C_R\}}.} \tag{2.16}
\]

In particular, if `C_R<=h`, all claims in `G` are jointly linkable.
Pairwise vertex-disjoint suffixes ending at distinct sinks are a sufficient
special case.

#### Proof

For each `up in E`, concatenate its private prefix with `R_p`.  This gives
`h` complete paths for each claim.  A claim-private start lies on `h` paths;
an edge-private prefix capacity lies on one; and every capacity of `R_p`
lies on

\[
                \sum_{p:\,a\in R_p}\deg_B(p)
\]

displayed paths.  Hence the complete path catalogue has congestion at most
`max{h,C_R}`.  Apply Corollary 2.3.  If suffixes are pairwise disjoint and
have distinct sinks, every sum contains at most one term and is at most
`h`.  
\(\square\)

In the disjoint-suffix case there is also a direct Hall proof: degree
counting gives a matching of `G` into `P`, and the matched private prefixes
followed by the disjoint suffixes form the linkage.  The fractional proof is
useful because (2.15) permits controlled overlaps and is the same certificate
that survives for a nonuniform weighted catalogue.

Unweighted suffix congestion at most `s` gives only
`C_R<=hs` and hence `eta>=1/s`; it does not give full linkage when `s>1`.
This loss is sharp already at `h=s=2`: take `B=K_(2,2)` and make the two
port suffixes pass through one common unit vertex before ending at distinct
sinks.  Both claims have two alternatives and the suffix congestion is two,
but every complete path uses the common vertex, so the claim rank is one.

### Theorem 2.10 (router transfers total port corank)

Keep the edge-private capacity-faithful claim-to-port prefixes of Theorem
2.8.  Let `P_B=N_B(G)`, and let `Gamma` be the suffix strict-gammoid
restriction on the port ground `P_B`: a port set is independent exactly when
it has a vertex-disjoint suffix linkage to unused sinks.  Put

\[
 D_B=\max_{X\subseteq G}(|X|-|N_B(X)|)_+,
 \qquad
 C_B=|P_B|-r_\Gamma(P_B).                            \tag{2.17}
\]

Then the maximum number of jointly serviceable gain claims is at least

\[
                         \boxed{|G|-D_B-C_B.}         \tag{2.18}
\]

Consequently a router of Hall deficiency `O(1)` and a suffix port bank of
total corank `O(1)` give bounded claim deficiency; no separate all-subfamily
Rado audit is needed.  In the left-`h`-regular/right-degree-at-most-`h`
setting of Theorem 2.8, `D_B=0`.

#### Proof

By definition,

\[
                         |N_B(X)|\ge|X|-D_B.          \tag{2.19}
\]

For every `Y subseteq P_B`, the elementary matroid
rank inequality gives

\[
 r_\Gamma(Y)
 \ge r_\Gamma(P_B)-|P_B\setminus Y|
 =|Y|-C_B.                                            \tag{2.20}
\]

Rado's deficient-transversal formula for the claim menus now yields

\[
\begin{aligned}
 r_{\rm claim}(G)
 &=\min_{X\subseteq G}
   \bigl(|G\setminus X|+r_\Gamma(N_B(X))\bigr)\\
 &\ge\min_{X\subseteq G}
   \bigl(|G\setminus X|+|N_B(X)|-C_B\bigr)\\
 &\ge |G|-D_B-C_B.
\end{aligned}
\]

The private-prefix/capacity-faithful hypotheses turn the independent Rado
transversal into literal simultaneous claim service. \(\square\)

If `B` is left `h`-regular and every right degree is at most `h`, then

\[
 h|X|=e_B(X,N_B(X))\le h|N_B(X)|,
\]

so `D_B=0`, proving the stated specialization.

The quantity `C_B` can be read from one maximum suffix flow on the complete
port bank.  It is a sufficient global certificate because matroid nullity
is monotone under restriction.  Without a fixed suffix gammoid--for example,
if different port sets require different child representations--the rank
inequality (2.20) is undefined.

### Corollary 2.11 (Middle-Levels two-factor router interface)

Let `ML_m` be the rank-`(m-1)`/rank-`m` containment graph on `[2m-1]`, and
let `P_prot subseteq ML_m` be 2-bounded with

\[
                         |E(P_{\rm prot})|\le m-2.    \tag{2.21}
\]

The small protected-factor theorem supplies a spanning two-factor `B`
containing `P_prot`.  Orient its incidence edges from the rank-`(m-1)` shore
to the rank-`m` shore.  If, in one fixed residual literal child,

* the desired gain claims are identified with vertices on the first shore;
* every selected incidence of `B` is realized as an edge-private directed
  claim-to-port prefix; and
* the rank-`m` port vertices have pairwise disjoint directed suffixes to
  distinct unused supplier sinks,

then all those gain claims are jointly serviceable.

#### Proof

The abstract existence of `B` is the small protected-factor theorem.  Its
restriction to the desired claim vertices is left 2-regular and right
degree at most two.  Apply Corollary 2.9 with `h=2`. \(\square\)

More generally, if the factor is realized by edge-private prefixes and the
suffix gammoid on the complete rank-`m` port shore has corank at most `C`,
then all but at most `C` gain claims are serviceable by Theorem 2.10.  Thus
the supplier consequence of the protected factor needs only one near-full
port-rank certificate, not private suffixes for every port.

This corollary separates the remaining geometry sharply.  The protected-
factor theorem proves the abstract router even while forcing any declared
2-bounded bank of at most `m-2` incidences.  It does **not** orient those
incidences as literal supplier prefixes, supply the disjoint suffix router,
or make the resulting two-factor upper-complete, resident, common-cap legal,
or regenerative.  Those are additional hypotheses, not consequences of
the Middle-Levels factor.

### Theorem 2.12 (equivariant suffix flow equals orbit-quotient flow)

Let `D_suf` be one fixed finite directed suffix network from an addressed
port bank `P` to an addressed supplier-sink bank `T`.  Represent every
vertex capacity by a node-split capacity arc.  Add a fixed supersource `s`
with one unit-capacity arc `s p` for each `p in P`, and a fixed supersink
`t` with one unit-capacity terminal arc `z t` for each `z in T`.  Every
physical capacity, including port, internal, and sink capacity, must occur
exactly once in this directed multigraph.

Suppose a finite group \(\mathcal G\) acts on the addressed directed
multigraph and its arc identities such that:

1. `s` and `t` are fixed;
2. `P`, `T`, their source arcs, and their terminal arcs are invariant;
3. tail, head, and integer arc capacity are preserved; and
4. every node-split pair is carried equivariantly, with
   `g(v^-)=g(v)^-` and `g(v^+)=g(v)^+`.

Parallel arcs remain distinct elements under this action.  For every arc
orbit `O`, put

\[
                         C_O=\sum_{a\in O}c(a),      \tag{2.22}
\]

and retain one directed quotient arc `O` from the tail-vertex orbit of `O`
to its head-vertex orbit.  The quotient is a directed multigraph and may
have loops.  Let `F_orb` be the optimum of

\[
\begin{aligned}
 \max\quad &\operatorname{val}(z),\\
 \text{subject to}\quad
 &0\le z_O\le C_O &&(O\text{ every arc orbit}),\\
 &\sum_{O:\,\operatorname{head}(O)=K}z_O
   =\sum_{O:\,\operatorname{tail}(O)=K}z_O
   &&\left(K\notin\bigl\{\{s\},\{t\}\bigr\}\right), \tag{2.23}
\end{aligned}
\]

where `val(z)` is net quotient flow out of the fixed source orbit.  Then

\[
 \boxed{
 F_{\rm orb}=F_{\rm suf}=r_{\Gamma_{\rm suf}}(P),
 \qquad
 C_B=|P|-F_{\rm orb}.}                              \tag{2.24}
\]

Here `F_suf` is the ordinary maximum flow in the full node-split network and
`Gamma_suf` is its strict gammoid on `P`.  In particular, the full-port
suffix corank is exactly the orbit-quotient flow deficit.

#### Proof

First average any feasible full-network flow `f` over the group:

\[
 \bar f(a)={1\over|\mathcal G|}
            \sum_{g\in\mathcal G}f(g^{-1}a).        \tag{2.25}
\]

The average is feasible, invariant, and has the same value, because the
action fixes `s,t` and preserves every capacity.  Thus some maximum flow is
invariant.

For any full-network flow, invariant or not, define

\[
                           z_O=\sum_{a\in O}f(a).    \tag{2.26}
\]

Summing vertex conservation over a vertex orbit gives the quotient
conservation equation; arcs internal to that orbit appear once on both
sides.  The orbit capacity is exactly (2.22).  Hence (2.26) maps every full
flow to a quotient flow of the same value, proving
`F_suf<=F_orb`.

Conversely, let `z` be a quotient flow and define, for `a in O`,

\[
                              f(a)={z_O\over|O|}.    \tag{2.27}
\]

Capacity is respected because capacity is constant on `O`, so
`C_O=|O|c(a)`.  Fix a vertex orbit `K`.  For an arc orbit `O` whose head is
in `K`, the head projection `O to K` is an equivariant surjection.  All its
fibres therefore have the same size, namely `|O|/|K|`; this remains true in
the presence of stabilizers and parallel arcs.  Thus every vertex of `K`
receives exactly `z_O/|K|` flow from `O`.  The same argument at tails shows
that every vertex of `K` emits `z_O/|K|`.  Dividing the quotient conservation
equation by `|K|` proves conservation at each original vertex.  A quotient
self-loop contributes equally to both sides and causes no exception.
Therefore (2.27) is a feasible full-network flow of the same value, proving
`F_orb<=F_suf`.

The source-arc orbits are in bijection with the port orbits and have total
capacities equal to their port-orbit sizes; the same statement holds for
sink orbits and terminal arcs.  Thus quotienting neither loses nor creates
endpoint quota.  Finally, unit source arcs choose distinct ports, unit
terminal arcs choose distinct sinks, and the split arcs enforce internal
vertex-disjointness.
Integral max flow therefore identifies `F_suf` with the maximum size of an
independent port set in the suffix strict gammoid.  Equation (2.24) follows.
\(\square\)

The theorem applies only to an automorphism group of the **fixed residual
network**.  Deleting a compensation linkage can break the parent symmetry;
one must either choose an invariant deletion or use the stabilizer of the
materialized residual state.  Symmetry of target values, menus in different
children, or a quotient which forgets addressed capacity is insufficient.
Unconstrained routing arcs may be given any common invariant integral
capacity at least `|P|`; their orbit capacities are treated exactly as in
(2.22).

### Corollary 2.13 (quotient certificate for router corank)

In Theorem 2.10, suppose its fixed suffix port network satisfies Theorem
2.12 and the quotient flow has value at least `|P_B|-C`.  Then `C_B<=C`, so
at least

\[
                              |G|-D_B-C              \tag{2.28}
\]

gain claims are jointly serviceable.  If the quotient saturates all port
source arcs, then `C_B=0`; a left-regular/right-degree-bounded router then
services every gain claim.

#### Proof

Equation (2.24) gives `C_B=|P_B|-F_orb<=C`; substitute this in (2.18).
\(\square\)

### Corollary 2.14 (free cyclic suffix-corank divisibility)

In Theorem 2.12, suppose \(\mathcal G=C_\kappa\) is cyclic of order
`kappa`, its action is free on `P`, on `T`, on every internal addressed
vertex orbit, and on every finite-capacity arc orbit, including source,
terminal, and node-split capacity arcs.  Arc capacities are invariant
integers.  Then

\[
                 F_{\rm orb}\equiv0\pmod\kappa,
 \qquad
                 C_B=|P|-F_{\rm orb}\equiv0\pmod\kappa. \tag{2.29}
\]

Consequently, if `0<=C_B<kappa`, then `C_B=0` and the complete port bank is
suffix-linkable.

#### Proof

Every nontrivial vertex and capacity-bearing arc orbit has size `kappa`.
For an arc orbit `O`, invariance of capacity gives

\[
                         C_O=\kappa c_O
\]

for an integer `c_O`.  Put `z_O=kappa y_O` in the quotient program (2.23).
After division by `kappa`, the constraints are precisely an ordinary
directed max-flow program on the orbit multigraph, with integral capacities
`c_O` and the same orbit-conservation equations.  Its optimum is integral
by max-flow integrality.  Hence the unscaled optimum `F_orb` is a multiple
of `kappa`.  The free port action makes `|P|` a multiple of `kappa`, proving
(2.29). \(\square\)

The fixed supersource and supersink are harmless exceptions: they carry no
physical unit capacity, while their incident source and terminal **arc**
orbits are required to be free.  A fixed or short finite-capacity arc, a
fixed sink, or a non-equivariant node-split gadget invalidates the divisibility
conclusion unless it is removed and charged separately.

## 3. Exact final occurrence graph and value-balanced special face

Fix one reference lower compiler matching `M_0` and one final cap, guard,
address, deadline, and coalescing state.  Let `D` be the set of
occurrence-labelled demands whose edges of `M_0` are destroyed in that final
state.  Let `F` be a set of actual fresh final cell occurrences, disjoint
from every retained matching cell and every separately reserved hard-task
cell.

Form the exact final bipartite graph

\[
                    H_{\rm fin}=(D,F;E_{\rm fin}),
\]

where `dc in E_fin` exactly when the occurrence-labelled demand `d` may be
assigned to the addressed cell `c` under all final literal, cap, guard,
deadline, and common-state constraints.  Every pairwise capacity conflict
must be represented by a shore vertex or by a capacity-faithful gadget.  If
two individually legal edges can still be jointly incompatible through an
unrepresented resource, an ordinary matching graph is not the final
compiler object and the theorem below does not apply to that projection.

### Theorem 3.1 (exact background-preserving compiler repair)

Holding every unaffected edge of `M_0` fixed, the exact number of destroyed
demands that must remain unmatched is

\[
 \boxed{
 e_{\rm comp}:=|D|-\nu(H_{\rm fin})
 =\max_{X\subseteq D}\bigl(|X|-|N_{H_{\rm fin}}(X)|\bigr).} \tag{3.1}
\]

Consequently there is a final compiler matching retaining every unaffected
edge of `M_0` and all but exactly `e_comp` of the demands in `D`.

#### Proof

The retained background cells and the separately reserved cells are absent
from `F`, so any matching in `H_fin` may be adjoined to the unaffected part
of `M_0`.  Conversely, every repair which holds that background fixed is a
matching in `H_fin`.  Thus the maximum number repaired is
`nu(H_fin)`.  The second equality is the bipartite deficiency form of
Hall's theorem. \(\square\)

This is exact on the stated background-preserving face.  A global rematching
which releases additional edges of `M_0` can only improve the casualty, but
requires its own larger final occurrence graph.

For each demand or cell occurrence, write `v(.)` for its literal target
value, and put

\[
 D_S=\{d\in D:v(d)=S\},\qquad F_S=\{c\in F:v(c)=S\},
 \qquad a_S=|D_S|,\quad f_S=|F_S|.                  \tag{3.2}
\]

### Corollary 3.2 (value-exact fibre formula)

Suppose the final repair graph is exactly the disjoint union of complete
equal-value fibres,

\[
 E_{\rm fin}=\mathop{\dot\bigcup}_S D_S\times F_S.  \tag{3.3}
\]

Then

\[
                  \boxed{e_{\rm comp}=\sum_S(a_S-f_S)_+.} \tag{3.4}
\]

In particular, `f_S>=a_S` for every `S` gives zero casualty.

#### Proof

The maximum matching in the complete fibre `D_S times F_S` has size
`min(a_S,f_S)`, and the fibres are vertex-disjoint.  Substitute their total
matching size into (3.1). \(\square\)

This includes the unique-target-by-value face as the case `a_S<=1`, while
also allowing explicitly tracked multiplicities.  If `H_fin` merely
**contains** every complete equal-value fibre and may have extra edges, the
right side of (3.4) is an upper bound on `e_comp`, not necessarily equality.
If even one required equal-value incidence is structurally absent, value
counts alone give no such bound; one must use (3.1).

### Corollary 3.3 (cell-multiset cancellation on a value-exact face)

Suppose the complete actual old-only changed-cell bank `O` and the available
actual new-only bank `F` satisfy

\[
             \sum_{c\in O}[v(c)]=\sum_{c\in F}[v(c)] \tag{3.5}
\]

in the free abelian group on literal target values, every destroyed matched
demand belongs to the occurrence bank indexed by `O`, and the corresponding
repair graph satisfies the value-exact hypothesis (3.3).  Then
`e_comp=0`.

#### Proof

Equation (3.5) gives equality of the value multiplicities of `O` and `F`.
The destroyed demand bank is a submultiset of `O`, so `f_S>=a_S` for every
`S`.  Apply Corollary 3.2. \(\square\)

For a serial aligned birail circulation, summing the packet currents gives
formal equality (3.5) on every audited depth when the active-label walk is
closed.  Corollary 3.3 applies only if all of the following have also been
proved.

1. The signed summands are the complete actual old-only and new-only cell
   banks after composing the serial changes; intermediate overlaps are
   cancelled with their exact multiplicities.
2. Every surviving new cell is a distinct physical address in one common
   final cap/guard/deadline state.
3. Every unaffected reference edge remains legal, and every destroyed
   reference edge is in the declared old-only bank.
4. Fresh cells reserved for other hard tasks are removed before (3.5) is
   asserted, or their old target assignments are released and included in
   the same value ledger.
5. The final occurrence graph on these banks is value-exact as in (3.3), or
   its exact deficiency has separately been bounded by (3.1).

Under these hypotheses, aligned closed birail telescoping makes the compiler
casualty zero on the audited lower rows.  Without the fifth hypothesis,
signed value cancellation is not an occurrence-incidence theorem.

### Corollary 3.4 (permutation-rotor compiler transport)

Let `V` be finite and let `sigma_0,sigma_1` be permutations of `V`.  Suppose
one completed literal rotor has actual changed-cell actions

\[
 \lambda_{x,\phi}
   =U_\phi(\sigma_\phi x)-U_\phi(x)
 \qquad(x\in V,\ \phi\in\{0,1\})                   \tag{3.6}
\]

in the free abelian group on literal cell values.  Then its total changed-
cell value current is zero.  If the aggregate old-only and new-only cells
satisfy the five actual-address/final-legality/value-exact hypotheses
following Corollary 3.3, the rotor contributes zero lower-compiler
casualties on these rows.  Without value-exactness, its casualty is instead
the occurrence-graph deficiency (3.1).

#### Proof

For either phase,

\[
 \sum_{x\in V}U_\phi(\sigma_\phi x)
 =\sum_{x\in V}U_\phi(x)
\]

because `sigma_phi` is a permutation.  Summing (3.6) over both phases gives
zero current.  On the value-exact face, the actual-cell hypotheses identify
this equality with (3.5), so Corollary 3.3 transports the matching.  In the
general face, Theorem 3.1 is the applicable exact statement. \(\square\)

This is the compiler consequence of completed bilateral rotor
coboundaries.  It does not follow from helper permutations alone: (3.6)
must hold in one common literal value group, the actual final cell lift must
be proved, and occurrence-level structural zeros must be priced.

## 4. Occurrence-equivariance closes the zero-block cross matchings

The zero-block theorem reduces the canonical ray Hall defect to perfect
matchings in two balanced cross graphs.  The following gives a simple
structural-zero-safe sufficient condition.

### Lemma 4.1 (cross-list degree/load criterion)

Let `H=(A,B;E)` be bipartite.  If

\[
       \deg(a)\ge L\quad(a\in A),
 \qquad
       \deg(b)\le\Delta\quad(b\in B),                 \tag{4.1}
\]

and `L>=Delta>0`, then `H` has a matching saturating `A`.

#### Proof

For every `X subseteq A`, count the edges from `X` to its neighborhood:

\[
             L|X|\le e(X,N(X))\le\Delta|N(X)|.
\]

Thus `|N(X)|>=|X|`; Hall's theorem applies. \(\square\)

This is the ray analogue of Corollary 2.7.  On balanced shores, total edge
count forces equality in the degree/load comparison, so this criterion is
essentially regularity rather than an entropy gap.  Parallel physical
realizations with the same right ticket do not increase the simple-graph
degree unless their distinct capacity is represented by distinct shore
vertices.  Degrees in an unaddressed target-value projection do not
qualify.

### Lemma 4.2 (transitive invariant cross graph)

Let `H=(A,B;E)` be a bipartite graph with `|A|<=|B|`.  Suppose a finite group
`Gamma` acts transitively on `A`, transitively on `B`, and preserves `E`.
If `E` is nonempty, then `H` has a matching saturating `A`.

Here a shore vertex is the complete addressed occurrence consumed on that
side of a cross ticket.  Selecting an edge consumes only its two endpoint
vertices, or else every additional capacity must already be encoded into
one endpoint state.  With an unencoded edge-specific shared resource, an
ordinary graph matching is not the physical selection problem and this
lemma supplies only its endpoint projection.

#### Proof

Transitivity and invariance make every vertex of `A` have one common degree
`d_A` and every vertex of `B` one common degree `d_B`.  Double counting gives

\[
                 d_A|A|=d_B|B|,
\]

and nonemptiness gives both degrees positive.  For `X subseteq A`, all
`d_A|X|` incident edges end in `N(X)`, whose vertices receive at most
`d_B|N(X)|` edges.  Therefore

\[
 |N(X)|\ge {d_A\over d_B}|X|={|B|\over|A|}|X|\ge|X|.
\]

Hall's theorem gives a matching saturating `A`. \(\square\)

It is enough to have one legal seed edge whose full `Gamma`-orbit is an
occurrence-level legal graph with the two transitive shore actions.  On
equal shores this is also the equality case `L=Delta` of Lemma 4.1.

### Theorem 4.3 (exact orbit-quotient matching reduction)

Let a finite group `Gamma` preserve a bipartite graph `H=(A,B;E)`.  Write

\[
 A=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_p,
 \qquad
 B=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_q
\]

for its vertex orbits.  Form the orbit support graph `Q` by putting
`ij in E(Q)` exactly when `E(A_i,B_j)` is nonempty.  Then `nu(H)` equals the
optimum of the transportation problem

\[
\begin{aligned}
 \maxquad &\sum_{ij\in E(Q)}z_{ij},\\
 \text{subject to}\quad
 &z_{ij}\ge0,\\
 &\sum_jz_{ij}\le|A_i|\quad(1\le i\le p),\\
 &\sum_iz_{ij}\le|B_j|\quad(1\le j\le q).
                                                        \tag{4.2}
\end{aligned}
\]

In particular, `H` has a matching saturating `A` if and only if the orbit
support graph admits a transportation flow with row sums `|A_i|` and column
sums at most `|B_j|`.

#### Proof

Any matching in `H` gives a feasible transportation solution by counting
its edges between each pair of orbits, so the right side of (4.2) is at
least `nu(H)`.

Conversely, fix a feasible `z`.  For every supported orbit pair `ij`, give
each edge of `E(A_i,B_j)` weight

\[
                         {z_{ij}\over |E(A_i,B_j)|}.
\]

Invariance and transitivity within each vertex orbit make the block
`H[A_i,B_j]` biregular.  Hence every vertex of `A_i` receives total weight
`z_{ij}/|A_i|` from that block, and every vertex of `B_j` receives
`z_{ij}/|B_j|`.  The row and column constraints in (4.2) therefore make the
combined edge weights a fractional matching of value `sum z_ij` in `H`.
The bipartite matching polytope is integral, so `H` has an integral matching
of at least that value.  This proves equality. \(\square\)

Thus an invariant occurrence graph with many structural zeros need not be
complete or even transitive on an entire shore.  Its full matching defect is
already visible in the much smaller orbit-support transportation problem.
All physical capacities must still be represented in the occurrence graph
before taking the quotient.

Applied to the exact final compiler graph, if `tau(Q)` denotes the optimum
in (4.2), Theorem 3.1 becomes the exact identity

\[
                         e_{\rm comp}=|D|-\tau(Q).   \tag{4.3}
\]

Thus bounded orbit-transportation deficiency is by itself a bounded
common-cap certificate; no complete value fibre and no enumeration of the
unquotiented Hall shores is required.

### Corollary 4.4 (equivariant compiler-fibre transport)

In the exact final compiler graph of Section 3, suppose that for every value
`S` with `D_S` nonempty, `f_S>=a_S` and `H_fin[D_S,F_S]` contains a nonempty
subgraph invariant under a group acting transitively on `D_S` and
transitively on `F_S`.  Then `e_comp=0`.

#### Proof

Apply Lemma 4.2 separately to every value fibre to obtain a matching
saturating `D_S`.  The fibre shores are disjoint, so the union of these
matchings saturates `D`; Theorem 3.1 gives `e_comp=0`. \(\square\)

This is strictly weaker than the complete-value-fibre hypothesis (3.3), but
it is still occurrence-level.  A symmetry of target values alone, or an
orbit graph that forgets cell addresses or shared capacities, does not meet
the hypothesis.  In particular, a closed birail or permutation-rotor value
coboundary can use this corollary instead of Corollary 3.2 when its final
addressed equal-value occurrence graphs have the stated transitivity.

### Corollary 4.5 (equivariant zero-block closure)

Let the canonical ray shores be

\[
 L=L_0\mathbin{\dot\cup}L_+,
 \qquad
 R=R_0\mathbin{\dot\cup}R_+,
 \qquad
 |L_0|=|L_+|=|R_0|=|R_+|.
\]

If each actual occurrence graph `H[L_0,R_+]` and `H[L_+,R_0]` has a
nonempty invariant transitive subgraph as in Lemma 4.2, both have perfect
matchings and the ray Hall defect is zero.

The action must preserve occurrence addresses, cap/guard state, and the
two-cell meaning of every cross ticket; the graph contains only pairs which
coexist in one terminal state.  Distinct matched shore vertices must mean
distinct consumed physical cells, with no hidden edge-specific capacity.
Transitivity of target **values** or of an unaddressed quotient is
insufficient.

If deleting at most `e_ray` exceptional paired indices leaves this canonical
cross-matched state, and the exceptional indices themselves receive
distinct physical pairs, they contribute at most `e_ray` terminal ray
deficiency.  Indeed deleting pairs cannot increase any southwest corner
count of the zero-defect canonical pairing, while adding back `e_ray`
arbitrary pairs increases every corner count by at most `e_ray`.

### Corollary 4.6 (free cyclic matching-deficiency divisibility)

In Theorem 4.3, suppose \(\mathcal G=C_\kappa\) is cyclic of order
`kappa`, preserves both addressed shores, and acts freely on every left and
right vertex orbit.  Then

\[
                      \nu(H)\equiv0\pmod\kappa,
 \qquad
                      |A|-\nu(H)\equiv0\pmod\kappa. \tag{4.4}
\]

Equivalently, the exact matching deficiency is a nonnegative multiple of
`kappa`; any bound strictly below `kappa` forces a matching saturating `A`.

#### Proof

Every vertex orbit `A_i` and `B_j` has size `kappa`.  In the transportation
program (4.2), put `z_ij=kappa y_ij`.  After division by `kappa`, one obtains
the ordinary fractional-matching program on the orbit support graph `Q`,
with unit capacity at each quotient-shore vertex.  That polytope is integral,
so its optimum is the integer `nu(Q)`.  Therefore

\[
                         \nu(H)=\kappa\nu(Q).
\]

Also `|A|=kappa p`, where `p` is the number of left vertex orbits, which
proves (4.4). \(\square\)

This applies verbatim to the router deficiency `D_B`, the exact compiler
deficiency `e_comp`, and each addressed cross-ray matching deficiency when
their respective shores are invariant unions of free occurrence orbits.
Freeness of target **values** is insufficient if occurrence addresses have
short stabilizers or if the graph includes fixed boundary vertices.

## 5. Explicit reset consequence

Assume the complete-potential accounting row

\[
                    \Phi'\le\Phi+q-p+c_{\rm ns}.     \tag{5.1}
\]

Fix one materialized child and suppose:

1. the bank has `g` genuine gain claims with

   \[
                         g\ge\alpha\Phi-B_0;          \tag{5.2}
   \]

2. an independent compensation anchor has size at least `q-beta`;
3. after deleting one anchor linkage, Corollary 2.3 holds outside an
   exceptional gain set of size at most `e_G`, with parameter
   `eta=h/max{h,b}`;
4. every non-supplier casualty is exhausted by the exact final occurrence-
   graph deficiency `e_comp` of Theorem 3.1, the ray exceptions of
   Corollary 4.5, and one additional declared boundary set of size
   `e_other`, so

   \[
       c_{\rm ns}\le e_{\rm comp}+e_{\rm ray}+e_{\rm other}. \tag{5.3}
   \]

### Theorem 5.1 (fractional-corridor contraction)

Under clauses 1--4,

\[
 \boxed{
 \Phi'\le
 (1-\alpha\eta)\Phi+
 \eta B_0+\beta+\eta e_G+
 e_{\rm comp}+e_{\rm ray}+e_{\rm other}.}            \tag{5.4}
\]

#### Proof

Corollary 2.6 and the anchor give

\[
                  p\ge q-\beta+\eta(g-e_G).
\]

Substitute this and (5.3) in (5.1), then use (5.2). \(\square\)

### Corollary 5.2 (congestion-two one-step reset)

If `alpha=1`, every nonexceptional gain has two actual residual corridors
of combined congestion at most two, and all displayed additive quantities
are bounded, then

\[
 \boxed{
 \Phi'\le
 B_0+\beta+e_G+e_{\rm comp}+e_{\rm ray}+e_{\rm other}.} \tag{5.5}
\]

If the same child class and constants regenerate, the complete potential is
uniformly bounded.  A terminal repair theorem may then append the bounded
literal casualty set once, yielding `B(k)+O(1)`.

This is the sharp useful meaning of a **regenerating bilateral corridor
bank** in the current strict-gammoid architecture: after the joint physical
bank and anchor are fixed, almost every gain has two actual alternative
complete residual paths whose *combined* unit-capacity congestion is at most
two.  Neither source bilaterality nor two separate phase Hall matchings imply
this statement.

### Corollary 5.3 (two-phase partial-cover contraction)

Under clauses 1, 2, and 4 of Theorem 5.1, replace clause 3 by the literal
two-phase partial-cover hypothesis of Corollary 2.5.  Then

\[
 \boxed{
 \Phi'\le
 (1-\alpha/2)\Phi+{B_0\over2}+\beta+
 e_{\rm comp}+e_{\rm ray}+e_{\rm other}.}            \tag{5.6}
\]

In particular, at `alpha=1` this is a regenerated factor-`1/2`
contraction.  Unlike Corollary 5.2, it does not require two corridors for
every claim; it requires two phasewise capacity-disjoint partial families
whose union covers every claim in the same fixed residual network.

#### Proof

Corollary 2.5 gives the anchored rank row with `eta=1/2,gamma=0`.
Substitute it in the proof of Theorem 5.1. \(\square\)

### Corollary 5.4 (router-corank reset)

Under clauses 1, 2, and 4 of Theorem 5.1, suppose the gain claims have an
exact capacity-faithful claim-to-port router with Hall deficiency `D_B`, and
the fixed suffix port gammoid has total corank `C_B`, as in Theorem 2.10.
Then

\[
 \boxed{
 \Phi'\le
 (1-\alpha)\Phi+B_0+\beta+D_B+C_B+
 e_{\rm comp}+e_{\rm ray}+e_{\rm other}.}            \tag{5.7}
\]

At `alpha=1`, bounded router deficiency and bounded total suffix corank give
one-step bounded reset.  For a literal Middle-Levels two-factor router,
`D_B=0`; only the one global suffix-port corank remains on the supplier
side.

#### Proof

Theorem 2.10 gives at least `g-D_B-C_B` gain routes in addition to the
anchor, so

\[
                 p\ge q-\beta+g-D_B-C_B.
\]

Substitute in (5.1), use (5.3), and then use `g>=alpha Phi-B_0`.
\(\square\)

### Corollary 5.5 (exact equivariant residual-gate bound)

Fix one materialized child, one compensation linkage, one final
cap/guard/address/deadline/coalescing state, and all cross-gate resource
reservations.  Delete the compensation resources and every resource
reserved for another gate **before** forming the following objects.

1. Let `B=(G,P;E)` be the actual capacity-faithful claim-to-port router,
   with `g=|G|` and `P=N_B(G)`.
   Suppose it is invariant under an action on its addressed shores and
   edges.  Let `tau_B` be the optimum of its orbit-support transportation
   problem (4.2).
2. Let the fixed residual suffix network be equivariant as in Theorem 2.12,
   and let `F_orb` be its exact orbit-quotient maximum flow.
3. Let `H_fin=(D,F;E_fin)` be the exact background-preserving final compiler
   graph, invariant on addressed demand and cell occurrences.  Let
   `tau_comp` be the optimum of its orbit-support transportation problem.
4. Let \(H_{0+}=H[L_0,R_+]\) and \(H_{+0}=H[L_+,R_0]\) be the two exact addressed
   zero-block cross graphs, invariant after every compiler and supplier
   reservation.  Their four shores are disjoint, and every further capacity
   consumed by an edge is represented in an endpoint/gadget so that a
   matching in each graph coexists with the other selected objects.  Let
   `tau_0+` and `tau_+0` be their orbit-transportation optima.

Define the exact quotient deficits

\[
\begin{aligned}
 \delta_{\rm rt}   &=|G|-\tau_B,\\
 \delta_{\rm suf}  &=|P|-F_{\rm orb},\\
 \delta_{\rm comp} &=|D|-\tau_{\rm comp},\\
 \delta_{\rm ray}  &=(|L_0|-\tau_{0+})
                     +(|L_+|-\tau_{+0}).             \tag{5.8}
\end{aligned}
\]

Treat each unmatched ray obligation counted by `delta_ray` as one declared
terminal casualty; no unproved pairing of the exceptional obligations is
assumed.  Under clauses 1 and 2 of Theorem 5.1 and with all remaining
non-supplier casualties exhausted by these compiler/ray casualties and an
explicit set of size `e_other`, one has

\[
 \boxed{
 \Phi'\le(1-\alpha)\Phi+B_0+\beta
 +\delta_{\rm rt}+\delta_{\rm suf}
 +\delta_{\rm comp}+\delta_{\rm ray}+e_{\rm other}.} \tag{5.9}
\]

#### Proof

Theorem 4.3 applied to the router gives

\[
 D_B=|G|-\nu(B)=|G|-\tau_B=\delta_{\rm rt}.
\]

Theorem 2.12 gives

\[
 C_B=|P|-r_{\Gamma_{\rm suf}}(P)
    =|P|-F_{\rm orb}=\delta_{\rm suf}.
\]

Hence Theorem 2.10 services at least
`g-delta_rt-delta_suf` gain claims.  Theorem 4.3 applied to `H_fin`, together
with Theorem 3.1, gives exact compiler casualty `delta_comp`.  Applied to the
two cross graphs, it gives matchings of sizes `tau_0+` and `tau_+0`; by the
explicit cross-gate capacity hypothesis their union is physically valid,
and declaring every unmatched left obligation a casualty costs at most the
displayed quantity `delta_ray`.  Substitute these four losses into
(5.1), use the compensation anchor of size `q-beta`, and then use
`g>=alpha Phi-B_0`. \(\square\)

At `alpha=1`, bounded orbit-quotient deficits give a one-step bounded reset.
If all five displayed quotient programs saturate their source/left shores and
`e_other=0`, then

\[
                              \Phi'\le B_0+\beta.     \tag{5.10}
\]

There is no quotient-to-physics assumption hidden here: the orbit programs
are fractional certificates **inside one already materialized physical
network/graph**, and ordinary max-flow or bipartite-matching integrality
returns literal paths or addressed cell edges in that same state.

The invariance required after compensation is exactly this:

* the residual node-split supplier network, including every port, unused
  sink, source/terminal arc, capacity arc, and parallel arc identity;
* the router shores, menus, and edge-private prefix incidences if
  `delta_rt` is to be read from its quotient;
* the destroyed-demand bank, fresh-cell bank, exact final compiler edges,
  retained-background set, and reserved-cell set;
* the four addressed ray shores and their exact legal cross edges; and
* every final cap, guard, phase, deadline, flag, and coalescing datum on
  which any one of those incidences depends.

Setwise invariance under the stabilizer of the fixed residual state is
enough; pointwise invariance is unnecessary.  A parent action which moves
the compensation linkage, a symmetry between different child
representations, or an action only on target values does not satisfy the
corollary.

### Corollary 5.6 (free-orbit rigidity: bounded defect forces saturation)

In Corollary 5.5, suppose the post-compensation action is cyclic of order
`kappa` and satisfies the free-orbit hypotheses of Corollaries 2.14 and 4.6
on the suffix network, router, compiler graph, and both cross-ray graphs.
Write

\[
 \delta_{0+}=|L_0|-\tau_{0+},
 \qquad
 \delta_{+0}=|L_+|-\tau_{+0},
\]

so `delta_ray=delta_0+ + delta_+0`.  Then

\[
 \delta_{\rm rt},\ \delta_{\rm suf},\ \delta_{\rm comp},\
 \delta_{0+},\ \delta_{+0}
                  \in\kappa\mathbb Z_{\ge0}.        \tag{5.11}
\]

Consequently, if

\[
 \delta_{\rm rt}+\delta_{\rm suf}+\delta_{\rm comp}
 +\delta_{0+}+\delta_{+0}<\kappa,                   \tag{5.12}
\]

then every equivariant residual gate saturates exactly.  Bound (5.9)
collapses to

\[
 \boxed{
 \Phi'\le(1-\alpha)\Phi+B_0+\beta+e_{\rm other}.}   \tag{5.13}
\]

At `alpha=1`, only the explicitly nonfree boundary terms remain.  In
particular, any dimension-independent bound on the sum in (5.12) forces all
five equivariant defects to vanish for every `kappa` larger than that bound.

#### Proof

Corollary 4.6 applied to the router, compiler, and two ray graphs gives the
four matching divisibilities.  Corollary 2.14 gives suffix-corank
divisibility.  Their sum is a nonnegative multiple of `kappa`; if it is
strictly smaller than `kappa`, it is zero, and each nonnegative summand is
zero.  Substitute into (5.9). \(\square\)

For the coordinate-rotation action `C_k`, the modulus is `k` only after
freeness has been proved on the **addressed occurrence objects** in the
fixed residual state.  The following are genuine failure modes.

* In composite dimensions, periodic target sets can have short rotation
  orbits even when the central owner layers are free.  Adding an occurrence
  address may restore freeness, but this must be checked rather than inferred
  from the target value.
* A linear opening, seam, pivot, bare coordinate, root, deadline flag,
  compensation path, or reserved boundary cell can have a proper stabilizer
  or be fixed.  Such resources must be isolated into `B_0`, `beta`, or
  `e_other`, or the modulus drops.
* If only a residual stabilizer `C_h` survives compensation, the conclusion
  is divisibility by `h`, not by the parent order `k`.
* More generally, the same scaling proof gives only the common divisor of
  the relevant shore-orbit sizes or arc-orbit total capacities.  A single
  unit fixed resource reduces that common divisor to one.

The fixed supersource and supersink do not cause this failure because they
are bookkeeping vertices, not finite physical capacities; their incident
unit arc orbits still must be free.

## 6. Quantifier and scope audit

The order of construction is load-bearing:

\[
 \boxed{
 \text{select joint crossed options}
 \to\text{materialize and replay one child}
 \to\text{fix the compensation linkage}
 \to\text{form residual literal paths and cells}
 \to\text{apply the theorems}.}                       \tag{6.1}
\]

The following shortcuts are invalid.

1. **Two phase tuples are not two corridors.**  A tuple must be extended to
   a complete path in the same residual supplier network.
2. **Paired demand is not a gammoid element.**  If service requires both
   paths at once, the claim must be expanded into an exact paired-state
   gadget before Theorem 2.1 is used.
3. **Separate phasewise Hall is not joint option selection.**  It can fail
   before the residual network exists.
4. **Value equality is not occurrence incidence.**  Section 3 needs the
   exact final destroyed-demand--fresh-cell graph.  Value counts suffice
   only on the verified value-exact fibre face.
5. **Target equivariance is not occurrence equivariance.**  Lemma 4.1 must
   act on the addressed legal cross graph.
6. **Private module interiors do not bound supplier congestion.**  A common
   unit separator can lie on every corridor.  The bound `b` is a separate
   global theorem.
7. **A fixed-child reset is not regeneration.**  The output must lie in the
   same authenticated parent class with the same constants on one compatible
   spine.
8. **Parent symmetry is not residual symmetry.**  The orbit-flow theorem
   applies only to automorphisms of the materialized node-split network after
   the anchor capacities and sinks have been deleted.
9. **Orbit support is not an unpriced quotient.**  Arc-orbit total capacities,
   parallel arc identities, terminal arcs, and node-split capacity arcs all
   remain in (2.23); forgetting any of them can overstate suffix rank.
10. **A small nonzero free-orbit defect is an audit alarm.**  Under the
    hypotheses of Corollary 5.6 no residual defect can lie strictly between
    zero and `kappa`; observing one proves that some addressed orbit is short,
    some finite capacity was fixed, or the claimed post-anchor action is not
    an automorphism of the exact residual object.

## 7. Exact present boundary

The following are proved here.

* the exact fractional-corridor/rank implication and its cut equivalence;
* the `h`-paths versus congestion-`b` rank bound;
* the congestion-two full-linkage corollary;
* the two-phase partial-cover factor-`1/2` rank corollary;
* the full-corridor catalogue saturation criterion;
* the duplicated-router, port-corank transfer, and protected Middle-Levels
  factor interfaces;
* the exact group-orbit quotient for an equivariant node-split suffix max
  flow, hence for full-port suffix-gammoid rank and corank;
* free-cyclic-orbit divisibility of suffix corank and matching deficiencies,
  and the resulting `<kappa` exact-saturation criterion;
* the exact background-preserving occurrence-graph compiler deficiency;
* the value-fibre formula and zero-casualty permutation-coboundary corollary
  on a verified value-exact face;
* the cross-list degree/load, occurrence-transitive, and exact orbit-quotient
  matching criteria;
* the explicit contraction/reset bounds (5.4)--(5.5); and
* the partial-cover and router-corank reset bounds (5.6)--(5.7), and the
  fully substituted equivariant residual-gate and free-orbit rigidity bounds
  (5.9) and (5.13).

The following remain unproved in the OR-word construction.

* an extensive terminally closed crossed-option bilateral bank;
* two literal complete residual corridors per nonexceptional gain with
  combined congestion two after anchoring compensation, or the weaker
  capacity-faithful router with bounded Hall defect and bounded total suffix
  port corank;
* an actual-cell lift of the aligned closed birail current in one final cap
  state, including the repeated lower-q1 socket repair and the required
  value-exact occurrence incidences (or a direct bound on (3.1));
* occurrence-equivariant legal cross-ray graphs, or any other bounded-defect
  physical cross matching;
* bounded exhaustive exterior/compiler casualties;
* `g>=Phi-O(1)` exposure; and
* regeneration and the even terminal transfer.

Accordingly, no unconditional `B(k)+O(1)`, `B(k)+1`, or new finite value of
`nu(k)` is claimed.
