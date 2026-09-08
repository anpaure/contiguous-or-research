# Equivariant Middle-Levels factors and the literal suffix-router gate

**Date:** 2026-08-03

**Status:** unconditional fixed-child theorems and a uniform symbolic
counterexample.  No finite search is used.  The note does not construct the
required post-compensation child in every dimension.

## 0. Outcome

An abstract regular Middle-Levels incidence factor closes only the
claim-to-port Hall row.  It becomes a literal supplier theorem precisely
after two further statements have been proved in the **same fixed
post-compensation child**:

1. every selected factor incidence has a capacity-faithful addressed prefix;
2. the resulting full claim--prefix--suffix network has no deficient
   quotient cut.

For an equivariant node-split child the second condition is an exact finite
orbit-quotient max-flow calculation.  If a cyclic action of order
\(\kappa\) is free on every addressed claim, port, sink, capacity and arc
orbit, the literal claim deficiency is a multiple of \(\kappa\).  Hence

\[
       \text{literal claim deficiency}<\kappa
       \quad\Longrightarrow\quad
       \text{every gain is serviceable}.             \tag{0.1}
\]

Connectivity does not supply the strict inequality in (0.1).  A connected,
free-equivariant Middle-Levels incidence router can feed a single free orbit
of unit bottlenecks; its exact deficiency is \(\kappa\), the smallest
positive value allowed by free-orbit rigidity.  Thus the missing theorem is
a quotient **capacity/expansion** theorem, not another connectivity theorem.

## 1. The one fixed literal network

Fix one fully materialized child, one literal compensation linkage, and all
compiler, ray, reset and boundary reservations.  Delete their used
capacities and sinks.  Nothing below may vary the child, anchor, phase,
address, cap, deadline or coalescing state from one cut to another.

Let

\[
                         B=(G,P;E)                    \tag{1.1}
\]

be an abstract incidence graph.  In the Middle-Levels application, `G` is
an addressed family on the rank-\((m-1)\) shore and `P` an addressed family
on the rank-\(m\) shore.  Assume

\[
             \deg_B(g)=h\quad(g\in G),
             \qquad
             \deg_B(p)\le h\quad(p\in P).            \tag{1.2}
\]

The following data are the minimal semantic lift from (1.1) to a flow
problem.

1. **Occurrence injection.**  Every vertex and incidence selected in `B`
   is one named occurrence in the fixed child.  Two abstract copies are not
   silently identified with one physical address.
2. **Capacity-faithful prefixes.**  For every `gp in E`, there is a directed
   addressed prefix gadget from the private claim start `x_g` to `p`.
   Every capacity is node-split, and the state expansion forbids switching
   between occurrence identities at a shared physical vertex.  Edge-private
   prefix interiors, with only `x_g` and the terminal `p` shared between
   prefixes and with no suffix-network contact before `p`, are a clean
   sufficient form.
3. **One suffix state space.**  From the ports onward there is one fixed
   directed state-expanded suffix network to one fixed unused sink bank.
   Claim identity is either irrelevant after a port or is retained in the
   suffix state.  A port path in one representation cannot be combined with
   a prefix in another.
4. **Exact capacities.**  Every physical unit resource is represented once
   by a split arc or an endpoint quota.  A unit source arc selects each gain,
   and a unit terminal arc prices each unused sink.  Parallel physical arcs
   remain distinct.

Call the resulting node-split directed network \({\cal N}_B\).  By
construction, its integral claim-to-sink flows are exactly simultaneous
literal claim corridors.  This last equivalence is the meaning of
capacity-faithful; an unaddressed projection is not enough.

## 2. Exact lift theorem

### Theorem 2.1 (regular factor plus exact literal quotient cut)

Let \({\cal N}_B\) satisfy Section 1.  Add a fixed supersource with one unit
arc to every `x_g` and a fixed supersink after the unit sink-terminal arcs.
Suppose a finite group \({\cal A}\) acts by automorphisms of this exact
directed multigraph, fixes the two supervertices, and preserves all arc
capacities and identities.  Let \(\overline{\cal N}_B\) be the arc-orbit
quotient: an arc orbit \({\cal O}\) has capacity

\[
                         C_{\cal O}
                         =\sum_{a\in{\cal O}}c(a).   \tag{2.1}
\]

Then the following quantities are equal:

\[
\begin{aligned}
 p_B
 &=\text{maximum number of simultaneously serviceable gains},\\
 &=\text{maximum integral flow in }{\cal N}_B,\\
 &=\text{maximum fractional flow in }\overline{\cal N}_B. \tag{2.2}
\end{aligned}
\]

In particular, every gain is serviceable if and only if every quotient cut
\(W\) with \(\bar s\in W\), \(\bar t\notin W\), satisfies

\[
                         c_{\rm orb}(W)\ge |G|.       \tag{2.3}
\]

The abstract regularity (1.2) implies

\[
                         |N_B(X)|\ge|X|
                         \qquad(X\subseteq G),        \tag{2.4}
\]

but does not imply (2.3).

#### Proof

The capacity-faithful definition identifies integral flows with literal
corridor packings.  Average any feasible flow over \({\cal A}\).  Conversely,
if `z_O` is a quotient flow, put `f(a)=z_O/|O|` for `a in O`.  Projection of
an arc orbit onto either endpoint orbit has constant fibre size, so quotient
conservation divided by the endpoint-orbit size is conservation at each
literal vertex.  Orbit capacity (2.1) gives every original capacity bound.
Thus full and quotient maximum-flow values agree.  Integral max flow proves
(2.2), and max-flow/min-cut proves (2.3).

For (2.4), count factor incidences:

\[
 h|X|=e_B(X,N_B(X))\le h|N_B(X)|.
\]

This count sees no suffix separator, proving only the stated abstract Hall
row. \(\square\)

### Exact normalized cut form

When the prefix interiors are edge-private, contract them to infinite-
capacity claim-to-port menu arcs.  For a quotient-invariant suffix vertex
set `W`, let `t_orb(W)` be the total number of literal gains whose complete
residual menu lies in `W`, and let `c_suf,orb(W)` count every finite suffix
capacity leaving `W`, including unit sink-terminal arcs.  Normalizing an
arbitrary finite cut at the claim vertices gives the equivalent condition

\[
              \boxed{c_{\rm suf,orb}(W)\ge t_{\rm orb}(W)\quad(W).} \tag{2.5}
\]

Indeed a claim vertex lies on the source side of a finite normalized cut
exactly when all its infinite menu arcs enter `W`; every other claim pays
its unit supersource arc.  This is the literal trapped-menu cut.  Omitting
sink arcs, history capacities, or a shared prefix vertex makes (2.5)
unsound.

### Exact separated Rado form

Let \(\Gamma_{\rm suf}\) be the strict gammoid on `P` induced by the fixed
suffix network.  Under the edge-private, prefix--suffix-separated hypothesis
of Section 1, every gain is serviceable if and only if

\[
              \boxed{r_{\Gamma_{\rm suf}}(N_B(X))\ge|X|
                     \qquad(X\subseteq G).}          \tag{2.5a}
\]

This is Rado's transversal theorem: select one distinct port for each gain
so that the selected port set is suffix-linkable, then concatenate the
edge-private prefixes with that linkage.  Conversely, every full literal
flow determines such a transversal.  Condition (2.5a), the normalized cuts
(2.5), and the complete-network cuts (2.3) are three exact descriptions of
the same gate on this edge-private face.

Regularity replaces `r_Gamma(N_B(X))` only by the cardinality bound
`|N_B(X)|>=|X|`; it supplies no lower bound on suffix-gammoid rank.

### Corollary 2.2 (modular full-port sufficient condition)

Assume the clean edge-private prefix form.  Let \(\Gamma_{\rm suf}\) be the
strict gammoid on the complete port bank in the fixed suffix network and put

\[
 C_P=|P|-r_{\Gamma_{\rm suf}}(P).                    \tag{2.6}
\]

Then at least \(|G|-C_P\) gains are serviceable.  In particular,
\(C_P=0\) lifts the abstract regular factor to a full literal supplier
router.

If a cyclic post-compensation action of order \(\kappa\) acts freely on the
port bank, sink bank, internal addressed vertices, and every finite-capacity
arc orbit of the complete suffix network, then

\[
                         C_P\equiv0\pmod\kappa.      \tag{2.7}
\]

Hence the apparently weaker estimate \(C_P<\kappa\) already implies
\(C_P=0\) and full service.

#### Proof

The router in (1.2) has Hall deficiency zero by (2.4).  Rado's theorem, or
the port-corank transfer inequality, leaves at most `C_P` gains.  Under a
free action, every arc-orbit capacity in the suffix quotient is a multiple
of `kappa`; scaling by `kappa` leaves an integral max-flow problem.  Both
suffix rank and `|P|` are multiples of `kappa`, proving (2.7). \(\square\)

Full-port saturation is sufficient, not necessary.  The sharpest test is
still (2.3), because a full claim linkage may use a router-good proper subset
of ports even when the complete port bank has positive corank.

### Corollary 2.3 (free-orbit claim rigidity)

If the cyclic action of order \(\kappa\) is free on every addressed gain,
port, sink, internal-capacity and finite-capacity arc orbit of
\({\cal N}_B\), then

\[
                 |G|-p_B\equiv0\pmod\kappa.         \tag{2.8}
\]

Consequently

\[
                         |G|-p_B<\kappa
                         \quad\Longrightarrow\quad
                         p_B=|G|.                    \tag{2.9}
\]

#### Proof

All finite arc-orbit capacities in \(\overline{\cal N}_B\) are multiples
of `kappa`.  Divide the quotient flow program by `kappa`; it is an integral
capacitated max-flow problem, so `p_B` is a multiple of `kappa`.  Freeness
on the gain bank makes `|G|` a multiple of `kappa`. \(\square\)

The fixed supervertices are harmless; their incident unit-arc **orbits**
must still be free.  If compensation leaves only a stabilizer of order `d`,
the modulus in (2.8) is `d`, not the parent order.

## 3. Middle-Levels specialization

Put \(\kappa=2m-1\) and let \(C_\kappa\) rotate the coordinates of
\([\kappa]\).  Its action on both shores

\[
                 { [\kappa]\choose m-1},
                 \qquad
                 { [\kappa]\choose m}               \tag{3.1}
\]

is free.  Indeed, if a nonidentity rotation of order `d` fixes a set, its
coordinate cycles show that `d` divides the set's rank.  But

\[
 \gcd(2m-1,m-1)=\gcd(2m-1,m)=1,
\]

so `d=1`.

Thus any invariant addressed incidence router on these shores has free
claim and port orbits.  A protected abstract two-factor, or the full
\(m\)-regular Middle-Levels incidence graph, supplies (2.4).  To invoke
Corollary 2.2 or 2.3 one must still prove, after fixing compensation:

* occurrence-labelled factor edges have capacity-faithful prefixes;
* the sink and internal state/capacity orbits are also free or are removed
  as an explicit boundary bank; and
* the exact quotient cut deficit is below one quotient unit.

Middle-Levels connectivity proves none of these three bullets.

## 4. Sharp free-equivariant bottleneck counterexample

The next construction shows that free-orbit symmetry and Middle-Levels
connectivity alone do not imply even a near-full literal router.

### Theorem 4.1 (connected ML incidence, free symmetry, deficiency
\(\kappa\))

For every \(m\ge3\), put \(\kappa=2m-1\) and work modulo \(\kappa\).  Define
rank-\((m-1)\) sets

\[
\begin{aligned}
 A_i&=\{i,i+1,\ldots,i+m-2\},\\
 A'_i&=(A_i\setminus\{i+m-2\})\cup\{i+m\}.
                                                        \tag{4.1}
\end{aligned}
\]

Let

\[
 G=\{A_i:i\in\mathbb Z_\kappa\}
   \mathbin{\dot\cup}
   \{A'_i:i\in\mathbb Z_\kappa\},                  \tag{4.2}
\]

The union is disjoint: the `A_i` are cyclic intervals, whereas `A'_i`
contains the block `i,...,i+m-3` together with the separated point `i+m`
and is not a cyclic interval for `m>=3`.

let `P` be every rank-`m` set containing some member of `G`, and let `B` be
the induced containment incidence graph.  Then:

1. `B` is `C_kappa`-invariant and connected;
2. every gain has degree `h=m`, every port has degree at most `m`, and all
   gain, port and incidence orbits are free;
3. there is a connected, capacity-faithful, free-equivariant literal suffix
   realization whose exact maximum claim flow is `kappa` although
   `|G|=2kappa`.

Hence its exact literal deficiency is

\[
                              |G|-p_B=\kappa,         \tag{4.3}
\]

the smallest positive defect compatible with (2.8).

#### Proof

Every gain has exactly

\[
                    \kappa-(m-1)=m
\]

rank-`m` supersets, all included in `P`; a rank-`m` port has only `m`
rank-`(m-1)` subsets in total.  This proves the degree row.  Put

\[
 U_i=A_i\cup A_{i+1},
 \qquad
 V_i=A_i\cup A'_i.
\]

Both have rank `m`.  The incidences through `U_i` connect all `A_i` in one
cycle, and `V_i` connects `A'_i` to `A_i`.  Thus `B` is connected.  The
rotation action is free by Section 3; an incidence stabilizer would fix its
endpoints, so incidence orbits are free as well.

Every port orbit is free.  Choose an equivariant phase map

\[
                         \varphi:P\to\mathbb Z_\kappa \tag{4.4}
\]

by assigning phase zero to one representative of each port orbit and
rotating; choose representatives so that `varphi(U_i)=i`.

Realize every incidence `gp` as an edge-private claim-to-port prefix.  Add
one free orbit of unit bottleneck vertices `b_i`, represented by split arcs

\[
                         b_i^-\longrightarrow b_i^+ \tag{4.5}
\]

of capacity one.  Direct every port \(p\) to \(b_{\varphi(p)}^-\).  From
\(b_{\varphi(p)}^+\), add an arc to a private sink `t_p`, followed by its unit
terminal arc.  Finally add the invariant cycle arcs

\[
                         b_i^+\longrightarrow b_{i+1}^-              \tag{4.6}
\]

to make the suffix support weakly connected.  Every vertex and finite arc
orbit, apart from the bookkeeping supervertices, is free.  Prefix interiors
are private and meet the suffix only at their declared ports, so this is a
capacity-faithful child.

Every claim-to-sink path crosses at least one split arc in (4.5).  Those
`kappa` unit arcs form a cut, so `p_B<=kappa`.  Conversely the paths

\[
             A_i\longrightarrow U_i\longrightarrow b_i
                 \longrightarrow t_{U_i}
                 \qquad(i\in\mathbb Z_\kappa)        \tag{4.7}
\]

are pairwise vertex-disjoint, so `p_B>=kappa`.  This proves (4.3).
\(\square\)

After division by the free orbit size, the quotient has two units of gain
demand and one unit of bottleneck capacity.  Its unique relevant separator
therefore has deficiency one.  The literal deficiency `kappa` is exactly
that quotient defect lifted through the free action; it is not caused by
disconnectedness or a short orbit.

The same downstream bottleneck can be attached to the full connected
\(m\)-regular Middle-Levels graph or to any supplied connected equivariant
factor with more than one gain orbit.  Thus strengthening abstract
connectivity, even to one component, cannot replace the quotient cut row.

### Corollary 4.2 (spanning regular-factor counterexample)

Take `G` and `P` to be the complete two shores in (3.1), and take
`B=ML_m`.  This is a connected spanning `m`-regular bipartite factor: its
two-step lower-shore projection is the connected Johnson graph
`J(kappa,m-1)`.  Use the same equivariant phase map and suffix bottleneck
(4.4)--(4.6).  The bottleneck cut still has capacity `kappa`, and the
`kappa` paths in (4.7) still exist.  Therefore

\[
 p_B=\kappa,
 \qquad
 |G|-p_B={\kappa\choose m-1}-\kappa>0.              \tag{4.8}
\]

Thus even a connected **spanning regular Middle-Levels factor**, with free
coordinate action and a connected equivariant suffix support, does not lift
without the quotient capacity row.  The two-orbit construction of Theorem
4.1 is the sharp refinement whose defect is the first allowed positive
multiple `kappa`.

## 5. Strongest honest sufficient theorem

### Theorem 5.1 (equivariant ML-factor literal-router criterion)

An abstract left-`h`-regular/right-degree-at-most-`h` Middle-Levels factor
in one post-compensation child gives a full literal supplier router under
either of the following proof-safe alternatives.

1. **Exact alternative.**  It has the occurrence-labelled capacity-faithful
   realization of Section 1, and every orbit quotient cut satisfies (2.3),
   equivalently (2.5) in the edge-private form.
2. **Modular suffix alternative.**  Its prefixes are edge-private, its fixed
   suffix network is equivariant and free of order `kappa`, and its full-port
   suffix corank is strictly smaller than `kappa`.
3. **Modular full-network alternative.**  The complete literal network is
   equivariant and free of order `kappa`, and any independent argument gives
   literal claim deficiency strictly smaller than `kappa`.

Alternative 1 is necessary and sufficient for the fixed capacity-faithful
network.  Alternatives 2 and 3 are convenient stronger hypotheses whose
conclusions follow from free-orbit divisibility.  None can be replaced by
abstract factor connectivity.

#### Proof

Alternative 1 is Theorem 2.1.  Alternative 2 is Corollary 2.2 together with
`C_P<kappa`, which forces `C_P=0`.  Alternative 3 is Corollary 2.3.  Theorem
4.1 refutes connectivity as a replacement. \(\square\)

## 6. Exact remaining mathematical target

The protected Middle-Levels factor theorem already supplies the abstract
incidence row while forcing a bounded protected bank.  The all-dimensional
literal theorem still needs one of the following equivalent kinds of input
after compensation:

* an exact orbit-quotient cut proof for the complete state-expanded claim
  network;
* a full-port suffix quotient flow, which is stronger but modular; or
* under free cyclic symmetry, any uniform bound below one orbit on the
  corresponding literal deficiency.

The counterexample shows why a proof based only on a connected factor,
Hamiltonicity, or free coordinate rotation cannot work.  It must establish
capacity expansion across every addressed quotient separator, with fixed
boundary and short-orbit resources removed and priced separately.
