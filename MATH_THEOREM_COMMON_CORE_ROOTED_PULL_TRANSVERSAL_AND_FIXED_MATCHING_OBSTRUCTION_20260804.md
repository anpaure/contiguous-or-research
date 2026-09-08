# Common-core component transversals: rooted pull closure and the fixed-matching obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction and exact closure theorem
for a fixed transparent pull host.  It sharpens the forest-complement gate
from global connectivity to rooted component coverage, and shows that after
one perfect matching is fixed the unrestricted problem is exactly a rooted
cycle-cover problem.  It does not prove that the current common-history ring
admits the required rooted transparent pull host.

No computation, search, or solver output is used.

## 0. Setting

Let `G` be a finite graph, let `F` be a spanning two-factor of `G`, and let
`D subseteq F` be a protected occurrence-labelled edge bank.  Let
`S subseteq D` be the common-core hinge/port bank.  Write `mathcal C(F)` for
the cycle components of `F`, and put

\[
 R_S(F)=\{C\in\mathcal C(F):E(C)\cap S\ne\varnothing\}.
\tag{0.1}
\]

Let `H` be a tree-compatible pull host on vertex set `mathcal C(F)`.  Thus an
edge of `H` represents an alternating circuit whose switch merges the two
factor components at its endpoints, and every graphic forest of host edges
can be switched simultaneously or in any leaf order, with component effect
equal to contraction of that forest.

Delete every pull whose old or new occurrence support meets `D`, and denote
the resulting **transparent host** by

\[
 H_D=H-\{e:\operatorname{supp}(e)\cap D\ne\varnothing\}.
\tag{0.2}
\]

All switches below therefore preserve every occurrence of `D`, in particular
every hinge in `S`.

## 1. Exact rooted-pull theorem

Define

\[
 q_0(F,S,H_D)
 =\#\{K\in\operatorname{Comp}(H_D):V(K)\cap R_S(F)=\varnothing\}.
\tag{1.1}
\]

### Theorem 1.1 (rooted maximal-forest closure)

Choose in every component of `H_D` a spanning tree, and switch the union `T`
of those trees.  The resulting protected factor `F_T` satisfies

\[
 \boxed{c_S(F_T)=q_0(F,S,H_D),}
\tag{1.2}
\]

where `c_S` is the number of factor cycles disjoint from `S`.  Consequently,
within the fixed tree-compatible pull host, a protected switch sequence
reaches a factor with forest complement `F'\setminus S` if and only if

\[
 \boxed{
  \text{every component of }H_D\text{ contains a member of }R_S(F).
 }
\tag{1.3}
\]

#### Proof

Tree compatibility says that switching `T` contracts each connected component
of `H_D` to one factor component and performs no contraction between different
components of `H_D`.  Since every switch is `D`-transparent, the set of
`S`-occurrences in the factor component created from `K` is exactly the union
of the `S`-occurrences in the old factor components indexed by `V(K)`.
Therefore the new component is disjoint from `S` exactly when
`V(K) cap R_S(F)` is empty.  This proves (1.2).

If (1.3) holds, (1.2) gives `c_S(F_T)=0`; the exact cycle-transversal identity
then gives `beta(F_T\setminus S)=0`, so `F_T\setminus S` is a forest.

Conversely, if one component `K` of `H_D` is rootless, no switch drawn from
this fixed host joins a factor component indexed by `K` to one outside `K`.
Every factor obtainable by these switches consequently retains at least one
component made solely from the old rootless components in `K`; that component
is disjoint from `S`.  Thus no such sequence has forest complement. \(\square\)

This is strictly weaker than requiring `H_D` to be connected.  Several
transparent-host components are harmless provided each has a hinge root.

### Corollary 1.2 (exact rooted cut criterion)

Condition (1.3) is equivalent to

\[
 \boxed{
  \delta_{H_D}(X)\ne\varnothing
  \quad\text{for every nonempty }X\subseteq
       \mathcal C(F)\setminus R_S(F).
 }
\tag{1.4}
\]

Here `delta_(H_D)(X)` is the host edge cut leaving `X`.

#### Proof

If `K` is a rootless component of `H_D`, take `X=V(K)`.  Conversely, if a
nonempty root-free `X` has empty cut, it is a union of components of `H_D`,
all of which are rootless. \(\square\)

Thus the remaining topology row is a rooted cut statement, not unrooted pull
connectivity.

### Corollary 1.3 (rank form)

Adjoin a new vertex `omega` to `H_D` and add an edge `omega C` for every
`C in R_S(F)`.  Call the resulting graph `widehat H`.  Then

\[
 \boxed{
 q_0(F,S,H_D)
 =|\mathcal C(F)|-r_{\rm gr}(E(\widehat H)).
 }
\tag{1.5}
\]

In particular, rooted pull closure is equivalent to

\[
 r_{\rm gr}(E(\widehat H))=|\mathcal C(F)|.
\tag{1.6}
\]

#### Proof

All components of `H_D` which contain a root are joined through `omega` into
one component of `widehat H`; every rootless component remains separate.
Thus `widehat H` has `q_0+1` components on `|mathcal C(F)|+1` vertices, and
its graphic rank is `|mathcal C(F)|-q_0`. \(\square\)

### Theorem 1.4 (exact rooted protected-pull inequality)

For `X subseteq mathcal C(F)`, put

\[
 b_D(X)=|\{e\in\delta_H(X):\operatorname{supp}(e)\cap D\ne\varnothing\}|.
\tag{1.7}
\]

Then rooted pull closure is equivalent to

\[
 \boxed{
  |\delta_H(X)|>b_D(X)
  \quad
  (\varnothing\ne X\subseteq\mathcal C(F)\setminus R_S(F)).
 }
\tag{1.8}
\]

For a protected occurrence `p in D`, define its rooted-cut pull load

\[
 \ell_X(p)=|\{e\in\delta_H(X):p\in\operatorname{supp}(e)\}|.
\tag{1.9}
\]

The directly checkable stronger inequalities

\[
 \boxed{
  |\delta_H(X)|>
  \sum_{p\in D}\ell_X(p)
  \quad
  (\varnothing\ne X\subseteq\mathcal C(F)\setminus R_S(F))
 }
\tag{1.10}
\]

therefore suffice.

#### Proof

The transparent cut leaving `X` has size

\[
 |\delta_{H_D}(X)|=|\delta_H(X)|-b_D(X).
\]

Apply Corollary 1.2.  Every forbidden pull counted by `b_D(X)` contains at
least one protected occurrence, so the union bound gives

\[
 b_D(X)\le\sum_{p\in D}\ell_X(p),
\]

and (1.10) implies (1.8). \(\square\)

The distinction from the old unrooted protected-pull inequality is exact:
(1.8) is required only for sets containing no hinge-bearing factor
component.

### Corollary 1.5 (two-sided root shielding)

Assume `H` is connected, `R_S(F)` is nonempty, and every forbidden pull
edge has both endpoints in `R_S(F)`.  Then rooted pull closure holds.

#### Proof

Let `K` be a component of `H_D`.  If it is all of `H`, it contains a root.
Otherwise some original host edge leaves `K`; because `K` is a component
after deletion, that edge is forbidden.  Its endpoint in `K` is a root by
hypothesis.  Thus every component of `H_D` is rooted, and Theorem 1.1
applies. \(\square\)

For the common-history ring this gives a concrete prospective placement
target: it is enough to place hinge roots at both factor-component endpoints
of every pull invalidated by the complete protected reservoir.  This is
stronger than necessary, but unlike raw pull abundance it composes
immediately.

### Corollary 1.6 (root capacity and two-stage placement)

If the ring supplies `h` hinge-root factor components, rooted pull closure
necessarily requires

\[
 \boxed{|\operatorname{Comp}(H_D)|\le h.}
\tag{1.11}
\]

Now split the protected bank as `D=D_0 union S`.  Let `H_0` be the host after
deleting the pulls invalidated by the background bank `D_0`.  Suppose:

1. every component of `H_0` contains a selected ring root; and
2. every additional pull invalidated by `S` has both endpoints among the
   selected ring roots.

Then rooted pull closure holds for the complete bank `D`.

#### Proof

Every component of `H_D` lies in one component of `H_0`.  If no additional
ring pull leaves it, it inherits a root from that `H_0` component.  Otherwise
one deleted ring pull leaves it, and the endpoint of that pull inside the
component is a root by hypothesis 2.  Thus every final component is rooted.
The numerical necessity (1.11) is immediate because distinct host components
need distinct root vertices. \(\square\)

There is an exact Hall form for the first row.  Let the components of `H_0`
be `K_1,...,K_q`, let the ring have labelled roles `1,...,h`, and join `K_j`
to role `i` when role `i` has a fully legal occurrence whose factor component
lies in `K_j`.  Assuming those occurrence choices have no additional
cross-role conflict, one distinct ring role can be placed in every `K_j` if
and only if

\[
 \boxed{|N(J)|\ge|J|\quad(J\subseteq[q]).}
\tag{1.12}
\]

This is ordinary Hall applied from host components to ring roles.  It is only
the background-component placement row; the two-sided shielding of the new
ring-deleted pulls remains separate.

## 2. Hypergraph/circuit form

The same conclusion is not specific to two-component pulls.  Suppose a
tree-compatible transparent alternating circuit may meet `t>=2` distinct
factor components and its switch contracts those `t` components to one.
Make a hypergraph `mathcal H_D` on `mathcal C(F)` whose hyperedges are these
transparent circuit supports.

### Theorem 2.1 (rooted hypertree closure)

Suppose `mathcal H_D` contains a rooted Berge forest in which every
hyperedge introduces at least one previously unabsorbed component and meets
the already absorbed part in exactly one component, and which covers every
vertex of `mathcal C(F)`.  Then there is a leaf-ordered family of transparent
circuits which produces a factor every component of which meets `S`.

#### Proof

Order each rooted Berge tree away from a chosen root.  Apply the circuit
switches in leaf-to-root order (or the reverse order under the stated
tree-compatibility convention).  Each switch merges its newly introduced
vertices into the unique older component and never touches `D`.  Induction
shows that the component represented by every processed rooted subtree
contains its root hinge.  At termination every original factor component has
been absorbed into a rooted component. \(\square\)

For Middle-Levels incidence hexagons this gives the exact local target: a
protected `C_6` catalogue need not Hamiltonize the whole factor graph; it
only has to supply a rooted spanning Berge forest after the circuits touching
the protected reservoir are deleted.  Connectivity of the incidence graph
alone is not asserted to supply such a forest: overlapping circuit supports
may meet an already contracted component more than once and can then split it.

## 3. Fixed-perfect-matching normal form

The rooted cut condition is still a genuine integral topology requirement.
This becomes transparent after fixing one perfect matching.

Let `G=(L,U;E)` be bipartite with `|L|=|U|`.  Let a spanning two-factor be
written as a disjoint union

\[
 F=M_0\mathbin{\dot\cup}M_1
\tag{3.1}
\]

of perfect matchings.  Fix `M_0`.  For `u in U`, let `mu_0(u)` be its matched
vertex in `L`.  Define the directed successor graph `A_(M_0)` on `L` by

\[
 x\longrightarrow y
 \quad\Longleftrightarrow\quad
 x\,M_0(y)\in E\setminus M_0,
\tag{3.2}
\]

with the required protected and forbidden incidences deleted or forced in the
obvious occurrence-labelled way.

Every second perfect matching `M_1` is a directed cycle cover `pi` of
`A_(M_0)`, via

\[
 \pi(x)=\mu_0(M_1(x)).
\tag{3.3}
\]

Suppose the hinge bank is exactly root-supported on a set `R subseteq L`:
both factor incidences at every `r in R` belong to `S`, and every edge of
`S cap F` is incident with a member of `R`.

### Theorem 3.1 (rooted cycle-cover equivalence)

Under (3.1)--(3.3), factor components are in bijection with cycles of `pi`,
and

\[
 \boxed{
  F\setminus S\text{ is a forest}
  \iff
  \text{every cycle of }\pi\text{ meets }R.
 }
\tag{3.4}

Equivalently, the selected successor arcs with both endpoints in `L\setminus
R` are independent in the graphic matroid of the underlying directed
multigraph.

#### Proof

Starting at `x in L`, traverse its `M_1` edge to `M_0(pi(x))` and then the
`M_0` edge backwards to `pi(x)`.  Thus one circuit of `F` is exactly one
cycle of `pi` with every step subdivided by its upper vertex.

Since the two incidences at a root in `R` lie in `S`, deleting `S` breaks
precisely the factor cycles which meet `R`.  A factor cycle disjoint from `R`
survives.  This proves (3.4).  On `L\setminus R`, a subgraph of a permutation
has indegree and outdegree at most one, so an undirected graphic circuit is
exactly a directed permutation circuit (including the parallel-edge
interpretation of a directed two-cycle). \(\square\)

This is the exact fixed-`M_0` version of the common-core component
transversal.  It is a perfect-matching/cycle-cover constraint plus one
rooted graphic-independence constraint; it is not an ordinary Hall row.

### Corollary 3.2 (head-swap effect)

Suppose a transparent alternating square replaces

\[
 \pi(x)=a,qquad\pi(y)=b
\]

by `pi'(x)=b, pi'(y)=a`.  If `a,b` lie in different cycles of `pi`, the
switch merges those cycles.  If they lie in the same cycle, it splits that
cycle into two.  In particular a local transparent switch is an improving
move for `c_S` only after its cycle incidence is known.

#### Proof

The new permutation is obtained by composing `pi` with the transposition
`(a b)` on its values.  A transposition merges two permutation cycles when
its points lie in different cycles and splits one cycle when they lie in the
same cycle. \(\square\)

The analogous `2t`-edge alternating circuit composes the successor
permutation with a `t`-cycle on the affected heads.  Hence raw `C_6` abundance
does not imply monotone component descent; the circuits must have the rooted
incidence pattern of Theorem 2.1.

## 4. Sharp abstract obstruction

### Theorem 4.1

The fixed-matching rooted factor problem contains directed Hamiltonicity as
the special case `|R|=1`.  Consequently factor extendability, ordinary Hall,
and abstract alternating-circuit connectivity do not by themselves imply a
forest complement.

#### Proof

Given a loopless directed graph `Q` on vertex set `L`, take a disjoint copy
`U={u_y:y in L}` and fix

\[
 M_0=\{y u_y:y\in L\}.
\]

For every arc `x to y` of `Q`, put the bipartite edge `x u_y` in `G`.
Then `A_(M_0)=Q`.  A perfect matching `M_1` is exactly a directed cycle cover
of `Q`.  With one root `r`, condition (3.4) says that this cycle cover has
only one cycle, hence is a directed Hamilton cycle through `r`.

The bipartite matching condition can therefore hold while the rooted
cycle-cover condition fails.  Alternating-circuit connectivity merely says
that any two existing perfect matchings lie in one exchange class; it does
not create a rooted cycle cover when none exists. \(\square\)

The theorem is a structural reduction, not a complexity assumption: it gives
an explicit faithful embedding of an arbitrary successor digraph.

## 5. Consequence for the common-history hinge ring

For the cyclic common-history ring, each hinge lower vertex is saturated by
its two protected incidence edges.  Hence in every protected factor
completion it is a root in the sense of Theorem 3.1.

The exact topology target can now be stated in either of two equivalent
host-specific forms:

1. choose a factor completion for which the `D`-transparent pull host has no
   rootless component; or
2. in a fixed-perfect-matching slice, choose the residual perfect matching so
   every successor cycle contains a ring root.

The first form has the exact all-cut statement (1.4).  The second has the
exact forest statement (3.4).  Either one gives

\[
 \eta_{\mathcal F}(S)=0
\]

after the relevant protected switches.  Neither follows from the already
proved protected Ore extension alone.

For a factor component `C`, let `mathcal L(C)` be its lower-shore vertices and
write

\[
 \partial^-\mathcal L(C)
 =\{K\in{[2m-1]\choose m-2}:K\subset L
       \text{ for some }L\in\mathcal L(C)\}.
\tag{5.1}
\]

### Theorem 5.1 (exact panchromatic-core criterion)

Let `F` have `c` components.  A size-`m` common-core ring can place at least
one hinge root in every component of `F` if and only if

\[
 \boxed{
  c\le m
  \quad\text{and}\quad
  \bigcap_{C\in\mathcal C(F)}
     \partial^-\mathcal L(C)\ne\varnothing.
 }
\tag{5.2}
\]

#### Proof

The ring roots are

\[
 I_i=K\cup\{a_i\},
\]

where the complement of `K` has `m+1` elements and exactly one of them,
`b`, is omitted from the `m` labels `a_i`.  If the ring hits every factor
component, then `c<=m` and its core `K` lies in every shadow in (5.2).

Conversely, choose `K` in the displayed intersection.  For each component
choose one extension `K+x_C` on its lower shore.  These labels `x_C` are
automatically distinct, because one lower vertex belongs to only one factor
component.  Since `c<=m`, at least one of the `m+1` labels outside `K` is not
among the chosen representatives; use it as `b` and use every other label as
one of the `a_i`.  The resulting punctured star contains every chosen
representative and hence hits every component. \(\square\)

Thus the ring-placement row is not an arbitrary Hall problem: it is exactly
the existence of one **panchromatic `(m-2)`-core** for the component colouring
of the lower layer.

### Corollary 5.2 (explicit shadow-expansion condition)

Put `M=binom(2m-1,m-2)`.  If `c<=m` and

\[
 \boxed{
  \sum_{C\in\mathcal C(F)}
    \left(M-|\partial^-\mathcal L(C)|\right)<M,
 }
\tag{5.3}
\]

then a common-core ring component transversal exists.

#### Proof

Choose an `(m-2)`-core uniformly.  The probability that component `C` is
missed is

\[
 1-{|\partial^-\mathcal L(C)|\over M}.
\]

By the union bound, (5.3) makes the probability of missing at least one
component strictly below one.  Hence some core lies in every shadow, and
Theorem 5.1 applies. \(\square\)

This is an unconditional probabilistic root-placement theorem under one
explicit expansion inequality.  What is not currently proved is that a
protected Ore completion can be chosen so that its component shadows satisfy
(5.3).

### Proposition 5.3 (dense permutation benchmark)

Let `W` objects be partitioned into the cycles of a uniformly random
permutation, and fix a marked set of size `h`.  The probability every cycle
meets the marked set is exactly

\[
 {h\over W}.
\tag{5.4}
\]

For a uniformly random derangement, that probability is at least

\[
 {h(W-h)\over W(W-1)}.
\tag{5.5}
\]

Consequently, in the complete successor model on the lower layer, the
expected number of panchromatic Johnson stars of size `m+1` is exactly
`m-1` for a uniform permutation and at least

\[
 (m-1){W-m-1\over W-1}
\tag{5.6}
\]

for a uniform derangement.

#### Proof

Delete the unmarked elements from a permutation every cycle of which meets
the marked set.  This leaves an arbitrary permutation of the `h` marked
elements.  Conversely, insert the `W-h` unmarked labels as `h` ordered
possibly empty lists, one after each marked label.  The number is

\[
 h!\,(W-h)!{W-1\choose h-1}=h(W-1)!,
\]

which proves (5.4).

An unmarked fixed point is already forbidden by the cycle-hit condition.
For each marked label, the number of cycle-hit permutations fixing it is
`(h-1)(W-2)!`.  The union bound therefore leaves at least

\[
 h(W-1)!-h(h-1)(W-2)!=h(W-h)(W-2)!
\]

cycle-hit derangements.  Divide by `!W<=W!` to obtain (5.5).

There are `binom(2m-1,m-2)=W(m-1)/(m+1)` Johnson stars, each with
`h=m+1` marked vertices.  Linearity of expectation gives (5.6) and the
exact permutation expectation. \(\square\)

The dense benchmark shows that panchromatic cores are not intrinsically
rare.  It is not a Middle-Levels factor theorem: admissible successor arcs
there form a sparse occurrence-labelled subgraph, and the protected
reservoir changes its perfect-matching distribution.

### Theorem 5.4 (component count alone cannot place a common-core ring)

For every `m>=14`, there is a spanning two-factor of `ML_m` containing two
distinguished cycle components such that no common-core hinge ring can place
a hinge root in both components.  Thus even a bound of at most `m` factor
components would not by itself imply the ring component transversal.

#### Proof

Choose two `(m-2)`-sets `H_0,H_1` with

\[
 |H_0\cap H_1|=m-4,
\]

and choose disjoint triples `A={a_1,a_2,a_3}` and
`B={b_1,b_2,b_3}` outside `H_0 union H_1`.  This uses

\[
 |H_0\cup H_1|+6=m+6\le2m-1
\]

coordinates for `m>=7`.

On core `H_0`, take the incidence hexagon whose lower vertices are
`H_0+a_i`; on core `H_1`, take the incidence hexagon whose lower vertices
are `H_1+b_j`.  The two `C_6` cycles are vertex-disjoint.  Their union has
twelve edges and maximum degree two.  Since `12<=m-2` for `m>=14`, the
small protected-factor theorem extends their union to a spanning two-factor
of `ML_m`.  Each prescribed hexagon is already saturated and hence remains
a separate factor component.

Every lower vertex in the first hexagon meets every lower vertex in the
second in exactly `m-4` coordinates.  Thus no cross pair is adjacent in
`J(2m-1,m-1)`.

By contrast, the lower roots of a common-core ring have the form

\[
 I_i=K\cup\{x_i\},\qquad |K|=m-2,
\]

so every two distinct ring roots are Johnson adjacent.  If a ring hit both
distinguished factor components, two of its roots would form a cross pair
between their lower shores, a contradiction. \(\square\)

This obstruction is geometric, not scalar.  It proves that the desired
factor cannot be selected first using only a component-count objective; its
component lower shores must admit one common-core clique transversal.

There is one further scope boundary.  Forest complement guarantees at least
one ring hinge in every final factor component.  A fixed cyclic head shift
on all ring hinges fuses those components only when its induced permutation
on the cut path pieces is one cycle.  Joint all-pairs completed hinges avoid
this extra ordering row; the current cyclic ring supplies a particular
head-shift relation, so its final permutation must still be checked or
prepared jointly.

## 6. Narrowest remaining lemma

After protected factor extension, the topology problem is reduced to:

> **Rooted transparent-pull lemma.**  The factor and the ring occurrence
> placement can be chosen so that, after deleting every pull circuit touching
> the complete protected reservoir, every component of the remaining pull
> host contains a ring-hinge factor component.

By Corollary 1.2 this is exactly the family of cuts

\[
 \delta_{H_D}(X)\ne\varnothing
 \qquad
 (\varnothing\ne X\subseteq\mathcal C(F)\setminus R_S(F)).
\tag{6.1}
\]

This is weaker than transparent-host connectivity and stronger than raw pull
abundance.  A proof may use the particular Middle-Levels hex/pull geometry;
Theorem 4.1 shows that no host-free Hall argument can replace it.

The constant-spread reservoir presently supplies no estimate for the left
side of (1.8).  Its protected Ore inequalities are cuts in the
Middle-Levels incidence graph, whereas (1.8) is a cut in the quotient graph
of factor components and pull occurrences.  There is no proved map sending
the former cut slack to the latter.  Moreover the canonical GMN pull host has
bridges.  If the old phase of one such bridge is protected and all hinge
roots lie on one side, deleting that pull leaves a rootless host component.
Thus neither global constant occurrence load nor factor extendability
verifies (1.8); one needs joint root placement, two-sided shielding as in
Corollary 1.5, or a genuinely redundant pull host.  In particular, the
current load estimate does not even imply the necessary root-capacity bound
`|Comp(H_D)|<=m` for the `m`-hinge ring.

## 7. Scope

This note proves:

* the exact rooted defect after maximal transparent pull switching;
* an exact rooted cut and graphic-rank criterion;
* the exact rooted cut-load inequality and a two-sided shielding theorem;
* the root-capacity obstruction and a two-stage Hall placement criterion;
* the exact panchromatic-core criterion and a shadow-expansion theorem;
* the exact dense-permutation benchmark for panchromatic cores;
* a two-hexagon obstruction to factor-first ring placement;
* the corresponding rooted Berge-forest theorem for larger circuits;
* the fixed-perfect-matching rooted cycle-cover normal form; and
* a sharp obstruction to deriving topology from factor extension alone.

It does **not** prove (6.1) for the current constant-spread reservoir, does
not prove that the ring's fixed cyclic rethread has the final one-cycle
permutation on an arbitrary rooted factor, and does not close the common cap.
