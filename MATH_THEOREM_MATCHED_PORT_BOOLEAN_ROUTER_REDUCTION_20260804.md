# Matched-port reduction for a regular incidence factor

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical routing theorem.  It strictly
weakens the full-active-port suffix hypothesis when the terminal suffixes
lie on a one-step Boolean face.  It does not construct the literal
claim-to-port prefixes or the one-step sink occurrences in the current
all-dimensional carrier.

## 0. Result

Let

\[
                         B=(G,P;E)
\]

be a bipartite incidence factor with

\[
 h\ge1,
 \qquad
 \deg_B(g)=h\quad(g\in G),
 \qquad
 \deg_B(p)\le h\quad(p\in P).                         \tag{0.1}
\]

Assume that every incidence \(gp\) has a literal prefix from the claim
start \(s_g\) to the physical port \(p\).  The complete prefix family is
private in the following literal sense: interiors share no physical
unit-capacity resource; prefixes may share only the common start of one
claim or the common terminal gate of one physical port; and every prefix
is present in one fixed cap/guard/phase state and avoids the fixed
compensation linkage and the protected capacity bank.

The degree conditions supply a matching \(\mu\) of the claims to physical
ports.  Fix one such matching.  Suppose its selected port set
\(Q=\mu(G)\) carries pairwise distinct rank-\(s\) Boolean values.  Suppose
every selected incidence \(g\mu(g)\) has at least \(L\) legal typed
one-coordinate extensions, all represented by available one-step sink
occurrences in the same fixed state; when one extension value lies in two
selected menus, the one retained occurrence for that value is required to
be legal for both selected incidences.  Let \(F\) be the forbidden
sink-value bank.  Thus the menu-rich/distinct-value property is a
hypothesis on the chosen matching; the degree count alone does not select
a matching with those additional properties.  A simpler sufficient
special case is that every factor port has a distinct value and every
incidence has the stated menu.

If

\[
                         |G|\le L,
 \qquad                  |F|\le L-1,                  \tag{0.2}
\]

then every claim has a pairwise vertex-disjoint literal route to a
distinct legal sink.

The proof first matches claims to distinct ports using only (0.1), and
then applies Boolean-shadow Hall only to those \(|G|\) selected ports.
Consequently one does **not** need:

* full suffix rank of the complete active port set \(P\);
* one suffix for every unused factor port;
* a terminal type accepted by every gain incident with an unused port; or
* the degree-weighted fractional suffix flow on all of \(P\).

For a bounded task bank, this reduces the remaining literal theorem to one
incidence matching plus one small Boolean shadow matching.

Section 2.3 gives a joint strengthening in which selected Boolean values
may repeat with bounded multiplicity.  In particular, two coordinatewise
matched banks can be routed in one shared Hall instance even when the same
value occurs once in each coordinate.

## 1. The factor already matches the gains to distinct ports

### Lemma 1.1 (degree-balanced Hall)

Under (0.1), \(B\) has a matching saturating \(G\).

#### Proof

For \(X\subseteq G\), every one of the \(h|X|\) incidences out of \(X\)
ends in \(N_B(X)\).  Since every vertex of \(N_B(X)\) has total degree at
most \(h\),

\[
 h|X|=e_B(X,N_B(X))
       \le\sum_{p\in N_B(X)}\deg_B(p)
       \le h|N_B(X)|.
\]

Thus \(|N_B(X)|\ge|X|\) for every \(X\), and Hall's theorem gives a
matching \(\mu:G\to P\). \(\square\)

Put

\[
                         Q=\mu(G).                     \tag{1.1}
\]

Then \(|Q|=|G|\).  Only the prefixes

\[
                         Q_{g,\mu(g)}:s_g\leadsto\mu(g) \tag{1.2}
\]

will be retained.  Prefix privacy for the full incidence factor therefore
implies privacy for this subfamily.

All assumptions below are imposed on this fixed matching.  Lemma 1.1
guarantees that a saturating matching exists, but, if only some incidences
are menu-rich or only some port choices have distinct Boolean values, the
existence of a matching inside that eligible subgraph is a separate Hall
condition.

## 2. Incidence-specific Boolean suffix matching

For \(g\in G\), write \(p_g=\mu(g)\), and let its Boolean value also be
denoted by \(p_g\in\binom{[k]}s\).  Let

\[
 A_g\subseteq[k]\setminus p_g,
 \qquad
 N_g=\{p_g\cup\{a\}:a\in A_g\}.                      \tag{2.1}
\]

The set \(N_g\) may depend on the selected incidence \(gp_g\); it need
not be a type-common menu for the other gains adjacent to \(p_g\).  Assume

\[
                         |N_g|\ge L.                   \tag{2.2}
\]

### Lemma 2.1 (selected-menu overlap)

For distinct gains \(g,g'\),

\[
                         |N_g\cap N_{g'}|\le1.         \tag{2.3}
\]

#### Proof

The selected ports have distinct rank-\(s\) values.  An \((s+1)\)-set
containing both values exists only when their union has rank \(s+1\), and
then that union is the unique possibility.  Restricting the two upper
shadows to the typed menus cannot increase their intersection. \(\square\)

### Lemma 2.2 (Boolean suffix Hall)

If (0.2) and (2.2) hold, there is an injection

\[
 \phi:G\longrightarrow\binom{[k]}{s+1}\setminus F,
 \qquad \phi(g)\in N_g.                               \tag{2.4}
\]

#### Proof

If `G` is empty the assertion is vacuous.  Assume it is nonempty.  Hall's
condition for the empty subfamily is automatic, so below take nonempty
`X`; then `x>=1` and `L>=1` follows from `|G|<=L`.

For \(X\subseteq G\), put \(x=|X|\).  Lemma 2.1 and the first two terms
of inclusion-exclusion give

\[
 \left|\bigcup_{g\in X}N_g\right|
 \ge xL-\binom x2.                                    \tag{2.5}
\]

After deleting \(F\), it is enough to prove

\[
 xL-\binom x2-|F|\ge x.                               \tag{2.6}
\]

The difference between the left and right sides is

\[
 q(x)=x(L-1)-\binom x2-|F|.
\]

This is concave on \([1,|G|]\).  At the two endpoints,

\[
 q(1)=L-1-|F|\ge0,
\]

and, using \(|G|\le L\),

\[
 q(|G|)
 \ge (|G|-1)\left(L-1-{|G|\over2}\right)\ge0.
\]

For `|G|=1` the last product is zero.  For `|G|>=2`, the inequalities
`|G|<=L` and `L>=2` give
`L-1-|G|/2 >= L/2-1 >=0`.  Thus the displayed endpoint bound includes
all small cases.

Hence (2.6) holds for every \(X\), and Hall's theorem proves (2.4).
\(\square\)

### Theorem 2.3 (bounded-multiplicity grouped Boolean Hall)

The selected physical ports may repeat their Boolean **value** when the
repetitions are treated in one joint Hall instance.  Let `U` be a set of
selected occurrence tickets.  Every ticket `u` has a rank-`s` base value
`p(u)` and an incidence-specific menu

\[
 N_u\subseteq\{p(u)\cup\{a\}:a\notin p(u)\},
 \qquad |N_u|\ge L.
\tag{2.7}
\]

Suppose there are `T` distinct base values and every value occurs on at
most the positive integer `rho` tickets.  If

\[
 \boxed{
 |F|\le L-\rho,
 \qquad
 T(L-\rho)-\binom T2-|F|\ge0,}
\tag{2.8}
\]

then there is an injection

\[
 \phi:U\longrightarrow\binom{[k]}{s+1}\setminus F,
 \qquad \phi(u)\in N_u.
\tag{2.9}
\]

In particular, the simpler conditions

\[
 \boxed{T\le L-\rho,\qquad |F|\le L-\rho}
\tag{2.10}
\]

imply (2.8).

#### Proof

The empty ticket set is trivial.  Fix a nonempty `X subseteq U`, let `t`
be the number of base-value groups met by `X`, and, for each such group
`v`, put

\[
 M_v=\bigcup_{u\in X:\,p(u)=v}N_u.
\]

Because the group is nonempty, `|M_v|>=L`.  If `v` and `w` are distinct
rank-`s` values, their full one-step upper shadows intersect in at most the
single value `v union w`; hence \(|M_v\cap M_w|\le1\).  The first two
terms of inclusion-exclusion give

\[
 \left|\left(\bigcup_{u\in X}N_u\right)\setminus F\right|
 \ge tL-\binom t2-|F|.
\tag{2.11}
\]

On the other hand `|X|<=rho t`.  Thus Hall follows if

\[
 q_\rho(t):=t(L-\rho)-\binom t2-|F|\ge0
 \qquad(1\le t\le T).
\tag{2.12}
\]

This is concave in `t`.  Its first endpoint is nonnegative by
`|F|<=L-rho`, and its other endpoint is exactly the second inequality in
(2.8).  This proves (2.9).

Under (2.10), the second endpoint obeys

\[
 \begin{aligned}
 q_\rho(T)
 &\ge T(L-\rho)-\binom T2-(L-\rho)\\
 &=(T-1)\left(L-\rho-{T\over2}\right)\ge0.
 \end{aligned}
\]

For `T=1` the product is zero; for `T>=2`, use `T<=L-rho`.
\(\square\)

### Corollary 2.4 (joint two-coordinate suffix Hall)

Suppose two occurrence coordinates are matched separately to physical
ports, and within each coordinate the selected Boolean values are
distinct.  Across the union of both selected banks, every value then has
multiplicity at most two.  If all menus and forbidden capacities are
evaluated in one common materialized state and

\[
 T\le L-2,
 \qquad
 |F|\le L-2,
\tag{2.13}
\]

then all selected occurrences in both coordinates have one simultaneous
matching to distinct legal upper values outside `F`.

This is a **single** shared-capacity Hall instance, not two marginal
matchings.  Any extra nonseparable compatibility required between the two
representatives of one logical ticket must already be encoded in the
menus or proved separately; the corollary resolves the shared suffix
capacity only.

## 3. Literal matched-port router

Fix one physical sink occurrence \(r(Y)\) for every retained value

\[
                         Y\in\bigcup_gN_g-F.           \tag{3.1}
\]

Require:

1. \(r(Y)\) lies in the same materialized cap/guard/phase state;
2. it has a terminal type legal for the selected incidence \(gp_g\)
   whenever \(Y\in N_g\);
3. distinct values have distinct unit-capacity sink occurrences;
4. \(F\) contains every value whose **chosen occurrence** `r(Y)` is
   occupied by the fixed compensation linkage, a selected prefix, or a
   protected bank; and
5. after node-splitting every physical unit-capacity resource, the
   one-step arc \(p_g\to r(Y)\) has no additional shared interior.

### Theorem 3.1 (matched-port Boolean router)

Under (0.1)--(0.2), prefix privacy, (2.2), and the five literal conditions
above, every gain in \(G\) has a route to a distinct legal sink,
simultaneously with the fixed compensation linkage.

#### Proof

Lemma 1.1 chooses distinct ports \(p_g\).  Lemma 2.2 chooses distinct sink
values \(\phi(g)\), hence distinct physical sink occurrences
\(r(\phi(g))\).  Concatenate

\[
 Q_{g,p_g}
 \quad\hbox{with}\quad
 p_g\longrightarrow r(\phi(g)).                       \tag{3.2}
\]

The selected prefixes are mutually private and already avoid the fixed
compensation/protected capacities.  Their terminal ports are distinct.
The suffixes have distinct endpoints and no shared interior capacity, and
the forbidden bank removes every remaining collision at a chosen sink
occurrence.  Thus the concatenations are pairwise vertex-disjoint and
typed legal. \(\square\)

### Corollary 3.2 (literal grouped router)

Replace the distinct-value hypothesis by Theorem 2.3.  Fix one physical
sink occurrence `r(Y)` for every retained upper value, legal for every
selected ticket whose menu contains `Y`, and impose conditions 1, 3--5
above jointly on the complete ticket bank.  If the selected literal
prefixes are also jointly private, after allocating one unit of source
capacity to every selected occurrence ticket, then the injection (2.9)
concatenates with those prefixes to give pairwise vertex-disjoint literal
routes for all tickets.

In the two-coordinate case, this conclusion is valid only when prefixes,
sink occurrences, the forbidden bank, and every shared physical capacity
are priced jointly across both coordinates.  Separate applications of
Theorem 3.1 do not imply it.

## 4. Middle-Levels specialization

Let the selected factor ports be distinct \(m\)-sets of a
\((2m+1)\)-element ground set.  If terminal typing forbids at most \(c\)
of the \(m+1\) extension labels on every selected incidence, then

\[
                         L=m+1-c.                     \tag{4.1}
\]

For a nonempty claim bank assume `0<=c<=m`, so `L>=1`.

In the convention where `ML_q` is the containment graph between ranks
`q-1` and `q` of a `(2q-1)`-set, these ports are the lower shore of
`ML_(m+1)`.  This parameter shift is why the unrestricted Boolean degree
here is `m+1`, not `m-1`.

### Corollary 4.1

Every claim in a left-\(h\)-regular/right-at-most-\(h\) literal factor is
routable whenever

\[
                         |G|\le m+1-c,
 \qquad                  |F|\le m-c,                  \tag{4.2}
\]

provided the matched prefixes and one-step sink occurrences are
materialized as above.

In particular, if

\[
 |G|=O(d(m)),\qquad |F|=O(d(m)),
 \qquad d(m)=\Theta(\sqrt m),                          \tag{4.3}
\]

and \(c\) is fixed, then (4.2) holds for all sufficiently large \(m\).
More generally, if

\[
 |G|\le C_Gd(m),\qquad |F|\le C_Fd(m),
\]

it is enough that

\[
 m+1-c\ge\max\{C_Gd(m),C_Fd(m)+1\}.
\tag{4.4}
\]

For a selected occurrence bank with Boolean-value multiplicity at most
`rho`, Theorem 2.3 instead gives the sufficient conditions

\[
 T\le m+1-c-\rho,
 \qquad
 |F|\le m+1-c-\rho.
\tag{4.5}
\]

In particular, for the joint two-coordinate case `rho=2`, it is enough
that

\[
 T\le m-1-c,
 \qquad
 |F|\le m-1-c,
\tag{4.6}
\]

with every occurrence and capacity interpreted in the one shared Hall
instance of Corollary 2.4.

After an explicit injection of the logical gains into the chosen shore,
the abstract small protected-factor theorem supplies the degree hypotheses
of Lemma 1.1.  It does not select the menu-rich matching or identify the
abstract right vertices with physical occurrences.  What remains physical
is therefore:

* materialize the selected matching prefixes;
* retain distinct Boolean values on the selected right-shore vertices, or
  verify the bounded-multiplicity grouped conditions of Theorem 2.3;
  and
* retain linearly many incidence-typed one-step sink occurrences after
  the background and prefix capacities are removed.

It is not necessary to link the whole neighbourhood \(N_B(G)\) or to
prove full active-port gammoid rank.

## 5. Relation to the exact factor-restricted Rado theorem

The factor-restricted Rado condition

\[
 r_\Gamma(N_B(X))\ge|X|\qquad(X\subseteq G)           \tag{5.1}
\]

remains the exact boundary for an arbitrary suffix network.  The theorem
above proves (5.1) on a special one-step Boolean face by first choosing a
matching \(\mu\) and then linking only \(\mu(G)\).  It is therefore a
sufficient specialization, not a replacement for Rado in the presence of
unbounded or unpriced duplicate port values, multi-step shared interiors,
or candidate-dependent cap rematerialization.

The gain over the previous full-port Boolean theorem is the quantifier:

\[
 \boxed{
 \text{match gains to ports first, then route only the matched ports.}}
\]

This removes unused factor ports and their type-compatibility obligations
from the literal suffix theorem.

The Boolean expansion calculation in Lemma 2.2 is the existing small-port
one-step theorem applied to the selected bank `Q`; it is not a new shadow
inequality.  The new reduction is the order of quantifiers: use the
degree-balanced factor to retain one physical port per gain, discard the
unused ports, and only then materialize/check the Boolean suffix bank.

This weakening is strict.  For example, let every gain have two private
degree-one ports.  Give one port per gain a distinct Boolean value and a
menu satisfying Section 2, and make the other port a loop in the suffix
gammoid.  The good ports form a saturating matching and the theorem routes
all gains, while the full factor port set is dependent (indeed it contains
all the loop ports), so full-port rank fails.

## 6. Scope and dependencies

This note uses no finite computation.  It proves the matched-port routing
step after one complete literal state and its incidence prefixes are fixed.
If the menu-rich/distinct-value incidences do not already contain the fixed
saturating matching used in Section 2, selecting such a matching remains a
separate correlated matching problem.
It does not construct an owner-exact chronology, upper deck, residence
system, common cap, or regenerative next state, and therefore does not by
itself prove \(\nu(k)\le B(k)+O(1)\).

| role | file |
|---|---|
| exact factor-restricted Rado and degree-weighted forms | `MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md` |
| full-port one-step Boolean Hall theorem | `MATH_THEOREM_SMALL_PORT_BOOLEAN_ONE_STEP_PRIVATE_ROUTER_20260804.md` |
| fixed-state regular factor/private router theorem | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` |
