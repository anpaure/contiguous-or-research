# Protected Middle-Levels router/suffix factor separation

**Date:** 2026-08-03  
**Status:** unconditional **abstract Middle-Levels incidence factorization**
after the already-proved protected two-factor extension.  It removes a
separate Hall gate for an unpinned third incidence factor.  It does **not**
identify that factor with the post-anchor supplier/compiler suffix network,
whose right vertices, capacities, and sinks are different occurrence-level
resources.  It also does not construct the required gain-labelled router,
make the router connected, or prove the protected Catalan--pivot theorem.

## 1. Set-up

Let

\[
 G=\operatorname {ML}(2m-1)
   =Q_{2m-1}\!\left[\binom{[2m-1]}{m-1}
                 \cup\binom{[2m-1]}m\right].
\]

The graph `G` is an `m`-regular bipartite graph.  Let `P` be a protected
incidence bank to which the protected two-factor extension theorem applies;
in the pivot application, `P` is the phase-aligned incidence image of the
sharp geodesic collar.  Thus there is a spanning two-factor

\[
                         R\subseteq G,
                         \qquad P\subseteq R.                 \tag{1.1}
\]

The result below begins only after (1.1).  In particular it does not infer
the gain, port, upper-colour, or residence rows from two-factor extension.

## 2. Exact phase criterion inside the router

Every component of `R` is an even cycle.  Give the edges of one component
their alternating parity `0,1`.  Reversing the choice at that component
interchanges the two parities.

### Lemma 2.1 (phase-pin criterion)

Suppose a set of protected incidences in `R` is prescribed to lie in one of
the two matching phases.  A global phase choice exists if and only if, on
each component of `R`, every two prescribed incidences have prescribed bits
whose xor equals their edge-distance parity on that component.

When the criterion holds, a component containing a pin has a unique phase
choice and an unpinned component has two choices.

#### Proof

On an even cycle an alternating two-colouring is unique up to global colour
swap.  Fixing one edge therefore fixes the colour of every other edge, and
the displayed parity condition is necessary and sufficient.  Components are
independent.  \(\square\)

In particular, a contiguous protected path with its natural alternating
predecessor/successor prescription is consistent; one pin fixes the phase of
its whole factor component.

After a feasible choice write

\[
                         R=M^-\mathbin{\dot\cup}M^+.             \tag{2.1}
\]

Both `M^-` and `M^+` are perfect incidence matchings.  They are the exact
two rails of the terminal gain-to-port router.  If an abelian gain is
attached to an oriented router component, reversing an unpinned component
negates its component gain.  Hence, after the pinned components are fixed,
the attainable aggregate gains are exactly

\[
             \gamma_{\rm pin}+\sum_{i\in I}\epsilon_i\gamma_i,
             \qquad \epsilon_i\in\{+1,-1\},                     \tag{2.2}
\]

where `I` indexes the unpinned components.  Formula (2.2), rather than a
claim of automatic primitive voltage, is the exact remaining gain row.

## 3. The suffix matching is automatic

### Theorem 3.1 (router--suffix factor separation)

Assume `m>=3`.  For every spanning two-factor `R` in (1.1), there is a
perfect incidence matching

\[
                         S\subseteq E(G)\setminus E(R).          \tag{3.1}
\]

More strongly,

\[
        E(G)\setminus E(R)
          =S_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}S_{m-2}
                                                                    \tag{3.2}
\]

for perfect matchings `S_1,...,S_(m-2)`.  Consequently

\[
                         M^-,\quad M^+,\quad S_j                 \tag{3.3}
\]

are three pairwise edge-disjoint perfect matchings, and every suffix edge is
disjoint from the complete router, not merely from the protected pivot.

#### Proof

Every vertex of `G` has degree `m`, and every vertex of the spanning
two-factor `R` has degree two.  Therefore

\[
                         H:=G-E(R)
\]

is an `(m-2)`-regular bipartite graph.  By Koenig's line-colouring theorem,
the edge set of an `r`-regular bipartite graph is a disjoint union of `r`
perfect matchings.  Apply this with `r=m-2`; any factor in (3.2) is the
required suffix `S`.  Equation (2.1) gives the other two factors.  \(\square\)

### Corollary 3.2 (protected pivot interface)

Whenever the protected two-factor theorem embeds the pivot incidence bank
`P` into `R`, the following rows may be selected in this order:

1. select the terminal gain/port router `R` containing `P`;
2. choose its component phases subject only to Lemma 2.1 and (2.2);
3. choose a suffix perfect matching in `G-R`.

Thus an **abstract ML incidence** suffix matching must not be included as an
additional simultaneous Hall gate in the protected-router theorem.  All
incidence-edge competition with that abstract factor disappears after the
router is fixed.

For the explicit collared pivot of depth `d`, the protected owner path has
`3d` Johnson turns and hence `6d` Middle-Levels incidences.  Therefore the
existing small protected-factor theorem applies whenever

\[
                              6d\le m-2.                         \tag{3.4}
\]

In that range the complete geometric output

\[
      \boxed{\text{phase-aligned pivot inside a two-rail router}
             \ +\ \text{one router-disjoint suffix factor}}
                                                                    \tag{3.5}
\]

is unconditional.  Since the deadline depth in the OR application is
`Theta(sqrt(m))`, (3.4) holds for every sufficiently large `m`.  This is a
geometric incidence statement only: upper-task labels and voltage remain
as stated in Sections 2 and 5.

The same conclusion applies after a terminal sequence of pull operations:
recompute `S` in the complement of the **terminal** two-factor.  It does not
assert that one previously frozen suffix survives intermediate pulls.

### Corollary 3.3 (a fixed protected bank)

Let `P_1,...,P_H` be a fixed number of pairwise incidence-vertex-disjoint
collared banks.  More generally, assume their union

\[
                         P=P_1\cup\cdots\cup P_H
\]

is 2-bounded and belongs to the scope of the protected two-factor extension
theorem.  If

\[
                         |E(P)|\le m-2,                         \tag{3.6}
\]

then there is a spanning two-factor `R` containing all banks, and `G-R`
contains a perfect matching `S`.  After an alternating phase is selected on
each component of `R`, this gives

\[
                  R=M^-\mathbin{\dot\cup}M^+,
                  \qquad S\cap R=\varnothing .                  \tag{3.7}
\]

For `H` depth-`d` pivot collars, each having `6d` incidence edges, the
concrete sufficient inequality is

\[
                             6Hd\le m-2.                         \tag{3.8}
\]

Every fixed `H` therefore satisfies (3.8) for all sufficiently large `m`.

The phase qualification is exact.  Local alternating pins inside each
collar are necessary, but if two banks land on one final factor component,
their *relative* prescribed phase must also pass Lemma 2.1.  Uncoloured
two-factor extension alone does not prove that extra parity row.  If only
the two rail names local to each bank matter, they may be renamed after the
terminal factor is known; if globally named `M^-`/`M^+` roles matter, the
parity row is load-bearing.

Nor does (3.7) itself give claim-to-port-to-sink linkages.  A two-factor has
cycles, not exposed sinks, and the factor `S` ends at ML owner vertices, not
at unused post-anchor supplier/compiler resources.  To obtain the latter one
must additionally:

1. open/orient the relevant router components at literal port occurrences;
2. map the chosen `S` incidences into valid residual occurrence arcs; and
3. prove vertex-disjoint linkage to the actual unused sink bank.

Those three statements constitute the missing **occurrence lift** of the
abstract separation theorem.

## 4. What additional suffix requirements cost

The automatic conclusion is exactly one unpinned suffix factor.  If a
matching `A` of suffix incidences is prescribed in advance, its extension
is governed by the ordinary residual Hall system

\[
 |N_{H-V(A)}(X)|\ge |X|
 \quad
 \left(X\subseteq
   \binom{[2m-1]}{m-1}\setminus V(A)\right),          \tag{4.1}
\]

where `H=G-R` and matched left/right vertices of `A` are deleted.  This is
necessary and sufficient.  It is not a consequence of regularity of `H`.

There are two useful safe faces.

* With no suffix pins, Theorem 3.1 applies.
* A single allowed suffix edge lies in some perfect matching of a regular
  bipartite graph: delete its endpoints and verify Hall by the standard
  regular-degree count, or equivalently take a one-factorization containing
  that edge.

Two individually extendable pins need not extend jointly.  On an even cycle
`C_(2q)`, the only two perfect matchings are its alternating phases.  Two
disjoint edges of opposite parity are each extendable but are not jointly
extendable.  For example, an 8-cycle can occur as the `(m-2)`-regular
complementary factor in a 4-regular bipartite host.  Hence any theorem with
two or more prescribed suffix incidences must retain (4.1), or must plant
the pins inside one declared complementary factor.

This is the sharp quantifier boundary:

\[
 \boxed{
 \text{terminal router first}\Longrightarrow
 \text{a disjoint suffix is free};
 \qquad
 \text{suffix pins first}\Longrightarrow
 \text{residual Hall is real}.}
\]

## 5. The exact three-neighbour palette supplied by the suffix

Although an unpinned suffix is free, using it to repair immediate-upper
tasks is an additional, sharply describable covering problem.

Fix one factor `S` from (3.2).  At a lower root `L`, write

\[
 M^-(L)=L+a_L,\qquad M^+(L)=L+b_L,\qquad S(L)=L+c_L.
\]

The three labels are distinct, because the three perfect matchings are
edge-disjoint.  Hence the three pairwise turns at `L` have the three
distinct upper values

\[
       L+a_L+b_L,\qquad L+b_L+c_L,\qquad L+c_L+a_L.    \tag{5.1}
\]

Thus `R union S` supplies a literal triangle of upper-turn options at every
lower root, while retaining three globally disjoint incidence matchings.

For an upper value `U`, let `E_U(R)` be the set of complement incidences
`Lc` with the following property: one of the two router neighbours at `L`
is a facet of `U`, and `L+c` is the other facet, so one of the two suffix
turns in (5.1) equals `U`.  Then a suffix factor `S` repairs every upper
value missing from the router exactly when

\[
                         S\cap E_U(R)\ne\varnothing
       \qquad(U\text{ missing from }R).                \tag{5.2}
\]

The size of this repair bank has an exact formula.  For
`L subset U`, `|L|=m-1`, let `t_U(L)` be the number of the two router
neighbours of `L` which are facets of `U`, and let `mu_R(U)` be the number
of router turns whose upper value is `U`.  Then

\[
       \sum_{L\subset U}t_U(L)=2(m+1),
       \qquad
       \mu_R(U)=|\{L:t_U(L)=2\}|.                       \tag{5.3}
\]

Indeed, `U` has `m+1` middle facets, and every such middle vertex has its
two router incidences from lower sets contained in `U`.  Every lower root
with `t_U(L)=1` supplies exactly one edge of `E_U(R)`, while roots with
`t_U(L)=0` or `2` supply none.  Consequently

\[
                   |E_U(R)|=2(m+1)-2\mu_R(U).            \tag{5.4}
\]

In particular, for every missing upper value,

\[
                   \boxed{|E_U(R)|=2(m+1).}              \tag{5.5}
\]

There is an equally exact base-rail refinement.  Fix one router phase
`M_0`, and let

\[
 E_U^{0}(R)=\{Lc\in H:M_0(L)\cup(L+c)=U\}.               \tag{5.6}
\]

If `U` is missing from the router, then

\[
                         \boxed{|E_U^{0}(R)|=m+1}.         \tag{5.7}
\]

To see this, take each of the `m+1` middle facets `V` of `U` and put
`L=M_0^{-1}(V)`.  Then `L subset V subset U`; if `c` is the unique element
of `U-V`, the incidence `L--(L+c)` is not in `M_0`.  It is not in the other
router phase either, since that would make the router turn at `L` equal
`U`.  Hence it lies in `H` and belongs to (5.6).  The construction is
reversible and the facets are distinct.

Equation (5.2) is exact.  It is not implied by Theorem 3.1: regularity gives
a perfect matching in the complement but does not make one perfect matching
meet every named edge family `E_U(R)`.  Equivalently, the gain-to-port
router theorem should export either

* a suffix factor already satisfying (5.2), or
* a separate occurrence-labelled hitting certificate for the missing
  upper tasks.

This distinguishes the row which is now closed from the row which remains:

\[
 \boxed{
   \text{existence of a disjoint suffix PM is automatic, but
   upper-decorated choice of that PM is not.}}                    \tag{5.8}
\]

## 6. The exact shared-rail Hamiltonian gate

The three-factor conclusion of Theorem 3.1 has a useful exact strengthening
criterion.  It also shows why regularity alone does not merge router
connectivity with suffix routing.

Fix a phase

\[
                         R=M_0\mathbin{\dot\cup}M_1
\]

and put `H=G-R`.  Regard each perfect matching as a bijection from the lower
shore `L` to the upper shore `U`.  For an edge `xv` of `H`, define the
directed contracted arc

\[
                         x\longrightarrow M_0^{-1}(v).          \tag{6.1}
\]

Let `D_(M_0,H)` be the resulting directed graph on the lower shore.

### Theorem 6.1 (shared-rail triple-factor equivalence)

For the fixed protected two-factor and phase above, the following are
equivalent.

1. There is a perfect matching `S` in `H` such that `M_0 union S` is one
   Hamilton cycle of `G`.
2. The directed graph `D_(M_0,H)` has a directed Hamilton cycle.
3. There are zero-one variables `s_(xv)`, indexed by `xv in E(H)`, satisfying
   the perfect-matching equations

   \[
      \sum_{v:xv\in H}s_{xv}=1,
      \qquad
      \sum_{x:xv\in H}s_{xv}=1,                                \tag{6.2}
   \]

   and, for every nonempty proper `X` contained in the lower shore, the
   subtour inequality

   \[
      \sum_{\substack{x\in X,\ xv\in H\\M_0^{-1}(v)\notin X}}
                    s_{xv}\ge 1.                               \tag{6.3}
   \]

The same equivalence holds with `M_1` in place of `M_0`.

#### Proof

A perfect matching `S` defines the permutation

\[
                     \pi_S=M_0^{-1}\circ S
\]

of the lower shore.  Contracting every edge of `M_0` identifies the cycles
of the two-factor `M_0 union S` with the cycles of `pi_S`.  Thus the union is
Hamiltonian exactly when `pi_S` is one cycle, which is exactly a directed
Hamilton cycle in (6.1).  Equations (6.2) say that the selected arcs form a
permutation.  A permutation has more than one cycle exactly when the vertex
set of one of its cycles is a nonempty proper set with no selected arc
leaving it.  This proves the equivalence with (6.3).  \(\square\)

Consequently the desired three factors

\[
   M_0,\quad M_1,\quad S,
   \qquad
   P\subseteq M_0\cup M_1,
   \qquad
   M_0\cup S\text{ Hamiltonian}                                \tag{6.4}
\]

exist if and only if one can first choose a protected two-factor and a
phase satisfying Lemma 2.1, and then satisfy (6.2)--(6.3) in its complement.
This is the exact triple-factor formulation requested by the shared-router
architecture.  Requiring *both* `M_0 union S` and `M_1 union S` to be
Hamiltonian imposes two simultaneous families of subtour inequalities and
is strictly stronger.

The obstruction is topological, not ordinary Hall.  The regular graph `H`
always supplies (6.2), but not (6.3).  In particular, if a nonempty proper
set `X` has no outgoing arc in `D_(M_0,H)`, every complementary perfect
matching preserves `X`.  Strong connectivity of `D_(M_0,H)` is necessary
but, as for general directed graphs, is not sufficient for a directed
Hamilton cycle.  At `m=3`, the complement is one-regular and `S` is forced;
the criterion reduces exactly to asking whether its forced permutation is
one cycle.  Thus no consequence of regularity can replace the subtour row.

## 7. Full-factor macro connectivity is automatic

There is nevertheless a stronger positive statement if *all* factors may
be used as labelled macro transitions, rather than selecting one suffix
factor once.

### Theorem 7.1 (transitive factor-generator theorem)

Let `K=(A,B;E)` be any connected `t`-regular bipartite graph with a
one-factorization

\[
                         E=N_0\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}N_{t-1}.
\]

Identify `B` with `A` through `N_0`, and put

\[
                         \sigma_j=N_0^{-1}\circ N_j
                         \quad(1\le j<t).                       \tag{7.1}
\]

Then the permutation group generated by
`sigma_1,...,sigma_(t-1)` acts transitively on `A`.  Moreover, the directed
labelled multigraph having the arcs

\[
                         x\longrightarrow\sigma_j(x)
                         \quad(x\in A,\ 1\le j<t)               \tag{7.2}
\]

is balanced and weakly connected.  Hence it has one directed Euler circuit.

#### Proof

Contract every edge of `N_0`.  Connectivity of `K` survives contraction,
and the non-`N_0` edges become precisely the underlying undirected edges of
(7.2).  Thus (7.2) is weakly connected.  Each `sigma_j` is a permutation,
so colour `j` contributes one incoming and one outgoing arc at every
vertex.  The whole directed multigraph is therefore balanced and hence
Eulerian.

The orbit of a vertex under the group generated by the `sigma_j` is exactly
its connected component in the undirected Schreier graph (7.2): a backward
traversal uses `sigma_j^{-1}`.  Since that graph is connected, there is one
orbit.  \(\square\)

Apply this to the complete factorization

\[
              G=M^-\mathbin{\dot\cup}M^+
                   \mathbin{\dot\cup}S_1\mathbin{\dot\cup}\cdots
                   \mathbin{\dot\cup}S_{m-2}.                  \tag{7.3}
\]

Taking `N_0=M^-`, the protected router generator `M^+` together with all
complement generators `S_j` has a transitive action and one Eulerian macro
tour.  Thus **abstract rotor connectivity is automatic when the full
factor-generator bank is admitted**.

This Euler tour is also abstractly immediate-upper complete.  Consecutive
macro arcs meet at a lower root `L` through the base incidence `N_0(L)`;
choosing the outgoing generator edge `N_j(L)` therefore realizes the upper
turn `N_0(L) union N_j(L)`.  By (5.7), every upper value missed by
`M^- union M^+` has exactly `m+1` complement-generator arcs producing it.
The Euler circuit uses every one of those arcs once.

This does not imply Theorem 6.1.  The Euler tour in (7.2) has
`(t-1)|A|` arcs and uses every contracted owner once for every nonbase
factor.  In literal incidence language its macros repeatedly use the base
matching as the return identification.  It therefore does not give a
one-owner-once chronology, a one-copy universal word, or a capacity-feasible
occurrence lift.  Nor does it preserve named upper witnesses, residence, or
common-cap tickets.  Passing from Theorem 7.1 to a length-`|A|` selector is
exactly the Hamilton/subtour problem in Theorem 6.1.

## 8. High connectivity of the full contracted macro host

The full Middle-Levels host also gives a fixed-task routing theorem which is
stronger than mere transitivity.  It uses the already-proved sharp
middle-shadow surplus

\[
 |N(X)|-|X|\ge \min\{m-1,W-|X|\}                       \tag{8.1}
\]

on either shore, where `W` is the shore size.

### Theorem 8.1 (Middle-Levels vertex connectivity)

For `m>=2`,

\[
                         \kappa(ML(2m-1))=m.             \tag{8.2}
\]

#### Proof

The neighbours of one vertex form a cut of size `m`, so `kappa<=m`.
Suppose a set `C=C_L union C_U` of fewer than `m` vertices disconnects the
graph.  No remaining component is a single-shore component, since every
vertex has `m` neighbours.  Choose a component whose lower shore `A` has
minimum size, and let `B` be its upper shore.  Then `A` and `B` are
nonempty, `|A|<=W/2`, and `|B|<=W-1`.  Since there are no edges from this
component to another one,

\[
 N(A)\subseteq B\cup C_U,
 \qquad
 N(B)\subseteq A\cup C_L.
\]

Apply (8.1).  Its surplus for `A` is at least `m-1`, while its surplus for
the proper nonempty set `B` is at least one.  Therefore

\[
 |B|+|C_U|\ge |A|+m-1,
 \qquad
 |A|+|C_L|\ge |B|+1.
\]

Adding gives `|C|>=m`, a contradiction.  \(\square\)

Fix any perfect matching `N_0` and contract it, obtaining the undirected
multigraph `K=G/N_0` on one shore.  Removing `z` contracted vertices removes
only `2z` original vertices.  Theorem 8.1 therefore gives

\[
                         \kappa(K)\ge\lceil m/2\rceil.    \tag{8.3}
\]

Consequently, after forbidding a contracted vertex bank `Z`, any two
disjoint sets `A,B` outside `Z`, each of size `h`, have `h` mutually
vertex-disjoint set-to-set paths whenever

\[
                         |Z|+h\le\lceil m/2\rceil.        \tag{8.4}
\]

This is immediate from (8.3), the inequality
`kappa(K-Z)>=kappa(K)-|Z|`, and Menger's theorem.  In particular, a fixed
number of abstract claims can be routed to a flexible sink bank while
avoiding any fixed `O(sqrt(m))` protected contracted bank, for all
sufficiently large `m`.

The scope remains important.  These are undirected paths in the **full**
contracted incidence host.  They may mix all factor labels and traverse a
generator opposite to its declared occurrence direction.  They do not lie
in one complementary perfect matching, enforce prescribed claim-to-sink
pairs, or respect literal supplier capacities.  Thus (8.4) is an abstract
flexible-port routing theorem, not the post-anchor gammoid lift omitted in
Corollary 3.3.

## 9. Consequence for the protected Catalan--pivot programme

The immediate geometric target can be reduced to the following object:

> construct a phase-orientable spanning two-factor containing the protected
> pivot bank and realizing the required gain-to-port state.

Once that object exists, no additional theorem is needed to obtain one
disjoint suffix matching.  The still-open rows are therefore:

* construction of the labelled router itself (including its port/gain
  occurrence data);
* consistency/primitive-voltage selection in the signed set (2.2), if a
  primitive lift rather than a componentwise router is required;
* upper-task decoration and, if required, transparent Hamiltonization of
  the router; and
* deeper shadows, residence, compiler, and regeneration.

Bare existence of an abstract ML suffix factor is no longer one of those
open rows.  Its upper-decorated selection, its Hamiltonian shared-rail
selection, and its literal occurrence-level supplier/compiler lift remain
open.
