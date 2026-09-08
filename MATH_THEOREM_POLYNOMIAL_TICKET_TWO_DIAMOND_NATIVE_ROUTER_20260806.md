# Polynomial ticket banks have two disjoint native interval-diamond routers

**Date:** 2026-08-06  
**Method:** normalized Boolean matching, Kruskal--Katona, and the
Aharoni--Haxell rainbow-matching theorem; no computation or search  
**Status:** unconditional occurrence-selection theorem, with a conditional
typed-cap corollary.  It proves that a polynomial labelled family of
lower-set tickets, allowing `o(r)` copies of one value, can be assigned two
pairwise resource-disjoint native `q1` interval diamonds whose upper
terminals contain the ticket value.  This
closes the two-coordinate suffix router whenever terminal legality is
exactly containment acceptance in those diamonds and the upper occurrence
may retain its old witness role.  It does not prove that the remaining
PBBS ticket types have this acceptance relation, nor that a frozen
background leaves the selected lower ports available.  On the stronger
universal polarized-socket face, arbitrary polynomial value multiplicity is
allowed, but state-aware socket acceptance remains a premise.

## 1. Native diagonal and ticket menus

Put `n=2r-1`.  Let

\[
 A_0,A_1,\ldots,A_{W-1}
\]

be a cyclic literal source word with the flat `q1` diagonal

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,\qquad
 P_i=T_i\cap T_{i+1},\qquad
 R_i=T_i\cup T_{i+1},                                      \tag{1.1}
\]

where the `T_i` are rank `r`, the `P_i` are rank `r-1`, and
the rank-`r+1` row is upper-surjective:

\[
 \{R_i:i\in\mathbb Z_W\}\supseteq { [n]\choose r+1}.       \tag{1.2}
\]

Retain the literal interval addresses

\[
 p_i=[i+1,i+d],\qquad o_i=[i,i+d],\qquad
 q_i=[i,i+d+1].                                             \tag{1.3}
\]

The native interval diamond at index `i` is

\[
 p_i-o_i-q_i,qquad p_i-o_{i+1}-q_i.                        \tag{1.4}
\]

Its finite occurrence footprint is

\[
                         \Xi_i=\{p_i,o_i,o_{i+1},q_i\}.     \tag{1.5}
\]

Thus `Xi_i` and `Xi_j` are disjoint whenever the two cycle edges
`o_i o_(i+1)` and `o_j o_(j+1)` are disjoint.

Let `F` be a labelled family of nonempty tickets `x`.  Write `S(x)` for
the value of ticket `x`, and assume

\[
                         |S(x)|\le r-1,
 \qquad                  |F|\le r^A,
 \qquad \mu_r:=\max_S|\{x\in F:S(x)=S\}|=o(r).            \tag{1.6}
\]

for one fixed constant `A`.  Define the native terminal menu

\[
                         I(x)=\{i:S(x)\subseteq R_i\}.      \tag{1.7}
\]

The set of cycle edges with indices in `I(x)` is denoted `E(x)`.  Tickets
with the same value have the same raw menu but remain distinct labelled
demands.

## 2. Polynomial Boolean families have linear-factor terminal expansion

### Lemma 2.1 (one-rank expansion)

For every fixed `A` there is a constant `c_A>0` such that, for all
sufficiently large `r`, every family

\[
 \mathcal X\subseteq {[2r-1]\choose s},\qquad
 s\le r-1,\qquad 1\le|\mathcal X|\le r^A
\]

has at least

\[
                         c_A r^2|\mathcal X|               \tag{2.1}
\]

distinct rank-`r+1` supersets.

#### Proof

The Boolean lattice has the normalized matching property.  Since

\[
 {2r-1\choose s}\le {2r-1\choose r-1},
\]

Hall gives an injective containment matching from `mathcal X` to a family

\[
 \mathcal Y\subseteq {[2r-1]\choose r-1},\qquad
 |\mathcal Y|=|\mathcal X|.                                \tag{2.2}
\]

Every rank-`r+1` superset of a member of `mathcal Y` is also a superset of
the corresponding member of `mathcal X`.

Complement `mathcal Y`.  This gives a rank-`r` family `mathcal Z` of the
same size.  Rank-`r+1` supersets of `mathcal Y` correspond bijectively to
rank-`r-2` members of the two-step lower shadow of `mathcal Z`.

Write

\[
                         |\mathcal Z|={x\choose r}
\]

in the Lovasz real-binomial notation.  Choose the integer
`a=ceil(A)+2`.  For sufficiently large `r`,

\[
 {r+a\choose r}={r+a\choose a}\ge r^A,
\]

so `x<=r+a`.  The Lovasz form of Kruskal--Katona gives

\[
 |\partial_{r-2}\mathcal Z|
 \ge {x\choose r-2}
 = {x\choose r}
   {r(r-1)\over(x-r+1)(x-r+2)}.                            \tag{2.3}
\]

Because `x-r<=a`, the last ratio is at least

\[
 {r(r-1)\over(a+1)(a+2)}.
\]

Taking, for example,

\[
                         c_A={1\over2(a+1)(a+2)}
\]

for all sufficiently large `r` proves (2.1).  \(\square\)

### Corollary 2.2 (distinct-value mixed-rank expansion)

For every set `X` of distinct nonempty ticket values of ranks below `r`,
with `|X|<=r^A`,

\[
 \left|\bigcup_{S\in X}\{i:S\subseteq R_i\}\right|
                         \ge c_A r|X|.                     \tag{2.4}
\]

#### Proof

One of the at most `r-1` rank layers of `X` contains at least
`|X|/(r-1)` tickets.  Lemma 2.1 gives at least
`c_A r^2|X|/(r-1)>=c_A r|X|` distinct rank-`r+1` supersets of that layer.
By upper surjectivity choose one distinct occurrence index for every such
value.  All those indices lie in the union in (2.4).  \(\square\)

The polynomial hypothesis is load-bearing.  The complete rank-`r-1`
layer has only a comparable number of rank-`r+1` supersets, so no uniform
linear expansion is possible at exponential ticket density.

## 3. Two diamonds per ticket

Make two labelled clones `x^0,x^1` of every ticket `x`.  For a clone `c`
let `H_c` be the graph on the owner occurrences whose edge set is `E(x)`.
Every `H_c` is a subgraph of the owner cycle

\[
                         o_0o_1\cdots o_{W-1}o_0.          \tag{3.1}
\]

### Theorem 3.1 (two-diamond native router)

For every fixed `A` and all sufficiently large `r`, there are indices

\[
                         i_0(x),i_1(x)\in I(x)             \tag{3.2}
\]

for all `x in F` such that all cycle edges

\[
 o_{i_e(x)}o_{i_e(x)+1},\qquad x\in F,\ e\in\{0,1\},      \tag{3.3}
\]

are pairwise vertex-disjoint.  Consequently all `2|F|` literal diamond
footprints `Xi_(i_e(x))` are pairwise disjoint.

#### Proof

Apply the Aharoni--Haxell Hall theorem to the family of graph edge sets
`{H_c}`.  Its graph case says that a rainbow matching exists if, for every
subfamily `J`,

\[
 \nu\left(\bigcup_{c\in J}H_c\right)>2(|J|-1).             \tag{3.4}
\]

Let `Y` be the set of underlying labelled tickets represented in `J`, and
let `X=\{S(x):x\in Y\}` be their set of distinct values.  Then

\[
             |Y|\ge |J|/2,
 \qquad      |X|\ge {|Y|\over\mu_r}\ge {|J|\over2\mu_r}. \tag{3.5}
\]

By Corollary 2.2, the union graph has at least

\[
                         c_A r|X|
                         \ge {c_A r\over2\mu_r}|J|         \tag{3.6}
\]

distinct edges of the cycle.  Any `m`-edge subgraph of a cycle has a
matching of size at least `(m-1)/2`.  Since `mu_r=o(r)`, for sufficiently
large `r` the matching number in (3.6) is greater than `2(|J|-1)`.  This proves
(3.4), and Aharoni--Haxell supplies one edge from every cloned menu, all
pairwise disjoint.

The chosen owner edges are precisely (3.3).  Distinct indices give
distinct `p_i` and `q_i`, while disjoint owner edges give distinct
`o_i,o_(i+1)`.  Formula (1.5) proves disjointness of the complete literal
footprints.  \(\square\)

This proof is deliberately occurrence-level.  Repeated upper values do
not cause a collision because their interval addresses remain distinct.

### Corollary 3.2 (clonewise structural-zero robustness)

For each clone `c=x^e` let `I'(c) subseteq I(x)` be its actually accepted
menu; the two occurrence coordinates of one ticket need not have identical
structural zeros.
The conclusion of Theorem 3.1 still holds if

\[
                         |I(x)\setminus I'(x^e)|=o(r)       \tag{3.7}
\]

uniformly over `x in F` and `e in {0,1}`.

#### Proof

For a clone subfamily `J`, choose one represented clone `c_S=x_S^e` for
each distinct value `S` in its value set `X`.  The union of the accepted
menus in `J` contains the union of these chosen menus.  Relative to the raw
distinct-value union this removes at most

\[
 \sum_{S\in X}|I(x_S)\setminus I'(c_S)|=o(r)|X|
\]

from the union menu.  Corollary 2.2 therefore remains
`(c_A-o(1))r|X|`.  Inequality (3.5), `mu_r=o(r)`, and the
cycle-matching calculation in Theorem 3.1 are unchanged.  \(\square\)

In particular, `O(d)` phase, collar, or guard exclusions per ticket are
harmless in the central regime `d=Theta(sqrt(r))`.  This does not cover a
common forbidden bank which happens to contain an entire ticket menu, nor
does it prove that a typed rejection has ticketwise size `O(d)`.

### Corollary 3.3 (universal socket face)

Let `F` be any labelled ticket family with `|F|<=r^A`, with no restriction
on repeated values.  If every ticket accepts every native interval diamond
as a routing socket, then two pairwise footprint-disjoint diamonds can be
assigned to every ticket.

#### Proof

The owner cycle has `W=binom(2r-1,r)` vertices and hence a matching of size
`floor(W/2)`.  For sufficiently large `r`,

\[
                         2|F|\le 2r^A<\lfloor W/2\rfloor.
\]

Choose `2|F|` edges of that matching and biject them with the two labelled
occurrence coordinates of the tickets.  Formula (1.5) makes the complete
diamond footprints disjoint.  \(\square\)

This corollary is relevant to polarized-socket semantics, in which the
ticket's exact target values remain certified by separate upstream
occurrences and the native nested pair carries only a reversible role code.
It is not relevant until that complete product type is accepted literally.

## 4. Conditional two-coordinate cap corollary

### Corollary 4.1 (native containment face)

Fix one common cap, phase, guard, and background state.  Suppose that for
every labelled ticket `x in F`:

1. any native diamond with `S(x) subseteq R_i` is a legal complete terminal
   route for either occurrence coordinate of `x`;
2. its terminal `q_i` may retain the already installed upper-witness role
   for `R_i` while terminating that ticket;
3. the finite capacities of every selected diamond are available after
   the fixed background, or the background coinstantiates the same literal
   roles; and
4. the two occurrence coordinates have no further cross-ticket constraint
   once their finite diamond footprints are disjoint.

Then the two-coordinate terminal Rado deficiency of `F` is zero.

#### Proof

Use Theorem 3.1 and assign the two selected diamonds of `x` to its two
occurrence coordinates.  Each route is legal by condition 1.  Condition 2
keeps the old upper service at zero additional terminal cost.  Theorem 3.1
gives pairwise disjoint finite capacities across both systems; conditions
3 and 4 therefore give global product closure in the one fixed state.
Every ticket is linked in both coordinates, so the common independent set
has size `|F|` and the deficiency is zero.  \(\square\)

### Corollary 4.2 (conditional polarized-socket face)

Fix one common cap, phase, guard, and background state.  Let `F` be any
polynomial labelled ticket bank.  Suppose every ticket already contains
its required exact upstream target occurrences, and suppose every native
pair `(p_i,q_i)` is accepted as its complete polarized socket in either
occurrence coordinate.  Suppose also that the selected footprints avoid
the frozen background, or coinstantiate precisely the same occurrence
facts, and that disjoint footprints give global product closure.  Then the
two-coordinate terminal deficiency of `F` is zero.

#### Proof

Apply Corollary 3.3 and assign the two selected footprints to the two
occurrence coordinates.  The exact target identities remain on the
upstream occurrences; the selected nested pairs supply only the accepted
role code.  The remaining premises make all deterministic complete bundles
coexist in the one fixed state.  \(\square\)

The hypotheses are exactly the semantic boundary of the deterministic
polarized-socket theorem.  In particular, this corollary does not turn an
arbitrary source occurrence into `p_i`, does not manufacture an upstream
witness, and does not show that the actual PBBS terminal predicate accepts
an arbitrary native pair.

### Corollary 4.3 (factor-wide polarized diagonal)

The polynomial bound is unnecessary when the tickets already have an
injective assignment to native ports.  More precisely, let `F` be any
ticket bank with `|F|<=W` and let

\[
                         \phi:F\hookrightarrow\mathbb Z_W
\]

be injective.  Suppose ticket `x` has its exact upstream target
occurrences and accepts `(p_(phi(x)),q_(phi(x)))` as its deterministic
polarized socket in the fixed state.  If the background coinstantiates or
avoids these occurrences and the two occurrence systems have product
closure, then every ticket routes simultaneously.

#### Proof

The pairs `(p_i,q_i)` are pairwise capacity-disjoint as `i` varies.  Apply
the deterministic polarized-socket theorem to the assigned complete
records.  \(\square\)

In particular, if a balanced claim factor already matches every claim to
a distinct q1 port and the actual PBBS terminal predicate accepts this
polarized code, no polynomial damage repair or alternative-port expansion
is needed at the suffix layer.  Whether that predicate identification is
valid is the exact semantic audit left below.

## 5. Exact PBBS interface left to audit

There are now two logically different interfaces, and they must not be
mixed.

1. **Polarized-socket interface.**  Exact target identity remains on
   already materialized upstream occurrences.  The pair `(p_i,q_i)` stores
   only the reversible occurrence-role code.  If this is the actual PBBS
   predicate, Corollary 4.3 closes the whole injectively ported bank.
2. **Strict claim-to-sink interface.**  A ticket must physically enter
   `p_i` and then use the native suffix to `q_i`.  In this model one must
   exhibit a complete claim-to-`p_i` prefix in the fixed state; neither
   `S(x) subseteq R_i` nor the existence of an upstream target occurrence
   supplies that prefix.

The first interface is a deterministic conjunction theorem; the second is
a gammoid path theorem.  A proof may use either one after its literal PBBS
semantics is verified, but may not use the target witnesses from the first
as if they were paths in the second.

The polynomial-component theorem reduces the PBBS repair bank to
`r^O(1)` labelled tickets.  Canonical ray banks may repeat one envelope
`d-1=Theta(sqrt(r))=o(r)` times, so (1.6) includes their value multiplicity.
This is exactly the density regime of Theorem 3.1.  The theorem
above removes both an abstract two-coordinate Hall obstruction and a
possible shortage of disjoint native interval diamonds.  It does **not**
yet prove the PBBS cap gate, because the following semantic identification
must be checked literally:

\[
 \boxed{\text{PBBS residual ticket }x\text{ accepts the native diamond
 precisely when its named target }S(x)\text{ is contained in }R_i.} \tag{5.1}
\]

If (5.1) holds and the transported background admits the dual roles in
Corollary 4.1, the typed suffix rank row closes for the polynomial bank.
If phase, envelope, or occurrence identity imposes additional structural
zeros, those zeros must be inserted into `I(x)` and the expansion proof
repeated.  Value-level containment alone may not be cited for that step.

## 6. Dependencies

The literal diamond identities and the source-free one-coordinate router
are in
`MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`.
The rainbow-matching input is the graph case of Aharoni--Haxell,
*Hall's theorem for hypergraphs*, Journal of Graph Theory 35 (2000),
83--88.  The Boolean expansion uses the normalized matching property and
the Lovasz form of Kruskal--Katona.
