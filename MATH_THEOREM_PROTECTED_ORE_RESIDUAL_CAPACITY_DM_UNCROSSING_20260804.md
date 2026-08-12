# Protected Ore as residual-capacity Hall surplus and its canonical DM shores

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It rewrites the
protected Ore margin as one capacitated Hall surplus, proves submodularity
and exact uncrossing, identifies the unique minimal and maximal
maximum-deficiency shores by residual-network closure, and derives strong
local density constraints for the constant-spread reservoir.  On the
co-small side it reduces failure to unpaid residual capacity on full and
almost-full owner cliques.  It does not
prove that either canonical shore is shifted or initial colex; it isolates
the exact DM-component reachability test for the existence of a shifted
maximum-deficiency shore.

No computation, search, or solver result is used.

## 0. Residual network

Put

\[
 \mathcal L=\binom{[2m-1]}{m-1},
 \qquad
 \mathcal U=\binom{[2m-1]}m,
\]

and let `P` be any subgraph of the Middle-Levels incidence graph with
maximum degree at most two.  Delete the protected edges and write

\[
 G_P=(\mathcal L,\mathcal U;E(ML_m)\setminus E(P)).
\tag{0.1}
\]

The residual demand of a lower vertex and residual capacity of an owner
are

\[
 r_x=2-d_P(x),
 \qquad
 c_U=2-d_P(U).
\tag{0.2}
\]

For `A subseteq mathcal L`, put

\[
 r(A)=\sum_{x\in A}r_x,
 \qquad
 d_A(U)=|N_{G_P}(U)\cap A|,
\tag{0.3}
\]

and define its residual-capacity supply by

\[
 \kappa_P(A)=\sum_{U\in\mathcal U}\min\{c_U,d_A(U)\}.
\tag{0.4}
\]

## 1. Exact Hall-surplus identity

### Theorem 1.1 (protected margin equals residual Hall surplus)

For every lower cut `A`,

\[
 \boxed{
 \mu_P(A):=\sigma(A)-\lambda_P(A)
 =\kappa_P(A)-r(A).}
\tag{1.1}
\]

Consequently, if

\[
 \delta(P)=\max_{A\subseteq\mathcal L}
             \bigl(r(A)-\kappa_P(A)\bigr),
\tag{1.2}
\]

then `delta(P)` is exactly the residual `b`-matching deficiency, and `P`
extends to a spanning two-factor if and only if

\[
 \boxed{\delta(P)=0.}
\tag{1.3}
\]

#### Proof

Fix an owner `U` and write

\[
 a_U=|N_{ML_m}(U)\cap A|,
 \quad e_U=e_P(U,A),
 \quad p_U=e_P(U,\mathcal L\setminus A).
\]

Then

\[
 c_U=2-e_U-p_U,
 \qquad d_A(U)=a_U-e_U,
\]

and hence

\[
 \min\{c_U,d_A(U)\}+e_U
 =\min\{2-p_U,a_U\}.
\tag{1.4}
\]

Summing (1.4), and using

\[
 r(A)=2|A|-\sum_Ue_U,
\]

gives

\[
 \kappa_P(A)-r(A)
 =\sum_U\min\{2-p_U,a_U\}-2|A|.
\]

The right side is exactly `sigma(A)-lambda_P(A)` by the protected Ore
ledger.  This proves (1.1).

The residual bipartite graph asks for a simple `b`-matching of lower
degrees `r_x` and owner degrees `c_U`.  The total lower demand equals the
total owner capacity because both are `2|mathcal L|-|E(P)|`.  The
capacitated Hall theorem therefore gives (1.2)--(1.3). \(\square\)

## 2. Submodularity and uncrossing

### Theorem 2.1 (submodular protected margin)

The function `mu_P` is submodular:

\[
 \boxed{
 \mu_P(A)+\mu_P(B)
 \ge\mu_P(A\cap B)+\mu_P(A\cup B).}
\tag{2.1}
\]

Equivalently, the deficiency function

\[
 \Delta_P(A)=r(A)-\kappa_P(A)=-\mu_P(A)
\tag{2.2}
\]

is supermodular.

#### Proof

For each owner, `d_A(U)` is a modular set function of `A`, and
`t mapsto min(c_U,t)` is nondecreasing and concave on the nonnegative
integers.  Therefore

\[
 A\longmapsto\min\{c_U,d_A(U)\}
\]

is submodular.  Summing over owners and subtracting the modular function
`r(A)` proves (2.1). \(\square\)

Assume now that `delta(P)>0`, and let

\[
 \mathfrak D
 =\{A\subseteq\mathcal L:\Delta_P(A)=\delta(P)\}
 =\operatorname*{argmin}_A\mu_P(A).
\tag{2.3}
\]

### Corollary 2.2 (canonical maximum-deficiency shores)

The family `mathfrak D` is closed under union and intersection.  Hence it
has unique inclusion-minimal and inclusion-maximal members

\[
 \boxed{
 A^-:=\bigcap_{A\in\mathfrak D}A,
 \qquad
 A^+:=\bigcup_{A\in\mathfrak D}A.}
\tag{2.4}
\]

Both are nonempty proper subsets of `mathcal L`.

#### Proof

If `A,B` both minimize `mu_P`, submodularity gives

\[
 \mu_P(A\cap B)+\mu_P(A\cup B)
 \le2\min\mu_P.
\]

Neither term can be below the minimum, so both equal it.  Iteration proves
closure and (2.4).  Finally `mu_P(emptyset)=mu_P(mathcal L)=0`, whereas
the common minimum is `-delta(P)<0`. \(\square\)

## 3. Dulmage--Mendelsohn residual closure

Form the flow network

\[
 s\longrightarrow\mathcal L\longrightarrow\mathcal U
 \longrightarrow t
\tag{3.1}
\]

with capacities `r_x` on `s x`, capacity one on every residual incidence
`x U in E(G_P)`, and capacities `c_U` on `U t`.  Put

\[
 R=\sum_{x\in\mathcal L}r_x.
\]

### Theorem 3.1 (exact cut projection)

For a fixed lower shore `A`, the minimum capacity of a network cut whose
source-side lower vertices are exactly `A` is

\[
 \boxed{R-r(A)+\kappa_P(A)=R+\mu_P(A).}
\tag{3.2}
\]

Thus the minimum flow-cut value is `R-delta(P)`, and the lower projections
of its minimum cuts are precisely the members of `mathfrak D`.

#### Proof

Once the source-side lower set is `A`, one owner `U` may be put on the
source side at cost `c_U`, or on the sink side at cost `d_A(U)`.  These
choices are independent over owners.  Their optimum is
`min(c_U,d_A(U))`.  The source arcs crossing from excluded lower vertices
cost `R-r(A)`.  Summation proves (3.2), and Theorem 1.1 gives the remaining
claims. \(\square\)

Fix any maximum flow `f` and let `mathcal R_f` be its directed residual
network.  Define

\[
 S^-={\rm Reach}_{\mathcal R_f}(s),
 \qquad
 S^+=V\setminus\{v:v\leadsto t\text{ in }\mathcal R_f\}.
\tag{3.3}
\]

### Theorem 3.2 (canonical DM-shore closure)

The two extremal deficient shores are

\[
 \boxed{
 A^-=S^-\cap\mathcal L,
 \qquad
 A^+=S^+\cap\mathcal L.}
\tag{3.4}
\]

They are independent of the chosen maximum flow.

Equivalently, `A^-` is obtained by the following local alternating
closure:

1. start with every lower vertex having an unsent demand unit;
2. from a reached lower vertex traverse every unused residual incidence;
3. from a reached owner traverse every used incidence backwards; and
4. repeat to closure.

No reached owner has unused sink capacity, since that would create an
augmenting path.  Dually, `A^+` is the complement of the reverse
alternating closure seeded by owners with unused sink capacity.

#### Proof

Every minimum-cut source side contains no positive residual arc leaving
it.  It therefore contains every vertex reachable from `s` and excludes
every vertex from which `t` is reachable.  Conversely `S^-` and `S^+` are
themselves residual-closed source sides separating `s` from `t`, so both
are minimum cuts.  They are respectively the intersection and union of
all minimum-cut source sides.  Project to the lower shore and use Theorem
3.1 and Corollary 2.2.  The listed traversal rules are exactly the positive
residual arcs of the network. \(\square\)

## 4. Exact local and block irreducibility

For `x in A`, define

\[
 e_A(x)=
 |\{U:xU\in E(G_P),\ d_A(U)\le c_U\}|.
\tag{4.1}
\]

For `y notin A`, define

\[
 u_A(y)=
 |\{U:yU\in E(G_P),\ d_A(U)<c_U\}|.
\tag{4.2}
\]

### Lemma 4.1 (one-vertex residual marginals)

One has

\[
 \boxed{
 \mu_P(A\setminus\{x\})-\mu_P(A)=r_x-e_A(x),}
\tag{4.3}
\]

and

\[
 \boxed{
 \mu_P(A\cup\{y\})-\mu_P(A)=u_A(y)-r_y.}
\tag{4.4}
\]

#### Proof

Removing `x` lowers the capped owner contribution by one exactly when its
current residual degree is at most its positive cap; this is (4.1).
Adding `y` raises it by one exactly when the current degree is below cap;
this is (4.2).  The demand changes by `r_x` or `r_y`, respectively.
Substitute in (1.1). \(\square\)

### Theorem 4.2 (irreducible extremal shores)

Every `x in A^-` satisfies

\[
 \boxed{e_{A^-}(x)\le r_x-1.}
\tag{4.5}
\]

In particular,

\[
 \boxed{d_P(x)\le1\qquad(x\in A^-).}
\tag{4.6}
\]

Every `y notin A^+` satisfies

\[
 \boxed{u_{A^+}(y)\ge r_y+1.}
\tag{4.7}
\]

More generally, for every nonempty `B subseteq A^-`,

\[
 \boxed{
 r(B)>
 \sum_U\left[
  \min\{c_U,d_{A^-}(U)\}
  -\min\{c_U,d_{A^-}(U)-d_B(U)\}
 \right],}
\tag{4.8}
\]

while for every nonempty `C subseteq mathcal L setminus A^+`,

\[
 \boxed{
 \sum_U\left[
  \min\{c_U,d_{A^+}(U)+d_C(U)\}
  -\min\{c_U,d_{A^+}(U)\}
 \right]>r(C).}
\tag{4.9}
\]

#### Proof

Removing any nonempty subset from `A^-` cannot leave another minimizer,
by its inclusion minimality.  Hence

\[
 \mu_P(A^-\setminus B)>\mu_P(A^-).
\]

Expanding this inequality with (1.1) gives (4.8); its singleton case is
(4.5).  If `r_x=0`, (4.5) is impossible, proving (4.6).

The maximality of `A^+` similarly makes every nonempty addition strictly
increase `mu_P`; expansion gives (4.9), whose singleton case is (4.7).
\(\square\)

Thus `A^-` is not merely a maximum-deficiency shore.  Every one of its
vertices is locally indispensable, and every nonempty internal block has
strictly more residual demand than the capped capacity it releases.

## 5. Consequence for the constant-spread reservoir

Now specialize to the frozen constant-spread bank.  Besides

\[
 \ell_P(x)=\lambda_P(\{x\})\le10,
\tag{5.1}
\]

its private/high endpoint exposure satisfies

\[
 e_P^{\rm priv}(x)\le10.
\tag{5.2}
\]

Let `t_top(x)` count deterministic top-bank endpoint owners `U` such that
`x subset U` and the unique protected incidence at `U` is not `Ux`.
There are exactly `2m` top endpoints, so

\[
 \boxed{
 \sum_{x\in\mathcal L}t_{\rm top}(x)
 \le2m(m-1).}
\tag{5.3}
\]

### Theorem 5.1 (capacity-closed Johnson core)

If the constant-spread bank has positive extension deficiency, its unique
minimal shore `A^-` satisfies

\[
 \boxed{
 d_{J[A^-]}(x)\ge2m-32-t_{\rm top}(x)
 \qquad(x\in A^-).}
\tag{5.4}
\]

In particular, outside a fixed exceptional bank of at most `2m(m-1)`
lower vertices,

\[
 \boxed{d_{J[A^-]}(x)\ge2m-32.}
\tag{5.5}
\]

#### Proof

Fix `x in A^-`.  By (4.5), at most `r_x-1` residual owner-neighbours of
`x` are not overloaded.  At every other residual owner `U`,

\[
 d_{A^-}(U)\ge c_U+1.
\]

After accounting for `x` itself, that owner supplies at least `c_U`
distinct Johnson neighbours of `x` in `A^-`.  Different owners over `x`
give disjoint Johnson-neighbour sets.

Among the residual owners over `x`, those of protected degree two are
counted by the singleton loss (5.1), and hence number at most ten.  Those
of protected degree one whose protected edge is not `Ux` are endpoint
exposures; at most ten are private/high and `t_top(x)` are top endpoints.
Therefore

\[
 \sum_{U:xU\in E(G_P)}c_U
 \ge2(m-d_P(x))-20-10-t_{\rm top}(x).
\]

Discarding at most `r_x-1=1-d_P(x)` exceptional owner rows costs at most
two each.  Since `r_x=2-d_P(x)`, the dependence on `d_P(x)` cancels and
gives (5.4).  Equation (5.3) proves (5.5). \(\square\)

Together with the frozen low-expansion localization, this confines any
remaining obstruction to a small or co-small, maximum-deficiency,
residual-capacity-closed family with dense Johnson neighbourhoods.  This
is strictly narrower than an arbitrary positive-defect cut.

## 6. Exact co-small consequence for an incidence-lift bank

Assume now that `P` is the incidence lift of a family of simple owner
paths.  Every protected lower vertex then has degree exactly two; all other
lower vertices have degree zero.  Put

\[
 Z_P=\{x\in\mathcal L:d_P(x)=2\}.
\tag{6.1}
\]

Suppose the minimal deficient shore is co-small, and write

\[
 C=\mathcal L\setminus A^-.
\]

For an owner put `d_C(U)=|N(U) cap C|`, and define the unpaid near-clique
capacity

\[
 \Omega_P(C)
 =\sum_{U:d_C(U)=m}(2-d_P(U))
  +|\{U:d_C(U)=m-1,\ d_P(U)=0\}|.
\tag{6.2}
\]

### Theorem 6.1 (co-small minimal-shore criterion)

Every co-small minimal deficient shore satisfies

\[
 \boxed{Z_P\subseteq C,}
\tag{6.3}
\]

and

\[
 \boxed{
 \Omega_P(C)>2|C|-|E(P)|.}
\tag{6.4}
\]

In particular,

\[
 \boxed{|C|\ge {|E(P)|\over2}.}
\tag{6.5}
\]

Conversely, any `C` containing `Z_P` whose unpaid load satisfies

\[
 \Omega_P(C)\le2|C|-|E(P)|
\tag{6.6}
\]

has a safe complementary cut.

#### Proof

Theorem 4.2 excludes every protected-degree-two lower vertex from `A^-`,
proving (6.3).  Since every protected edge has its lower endpoint in
`Z_P`, all protected incidences point into `C`.  Therefore

\[
 D_P(C)=|E(P)|,
 \qquad
 \operatorname{def}_P(C)=2|C|-|E(P)|,
 \qquad
 p_U=e_P(U,C)=d_P(U).
\tag{6.7}
\]

Use the frozen exact co-small criterion

\[
 \theta(C)>\operatorname{def}_P(C)+R_P(C).
\]

At a full owner `d_C(U)=m`, the difference between its contribution two
to `theta` and its rebate `p_U` is `2-d_P(U)`.  At an almost-full owner
`d_C(U)=m-1`, the difference is one exactly when `d_P(U)=0` and zero
otherwise.  Hence

\[
 \theta(C)-R_P(C)=\Omega_P(C).
\]

Substitution proves (6.4), while (6.3) and
`2|Z_P|=|E(P)|` prove (6.5).  Reversing the exact criterion proves the
converse (6.6). \(\square\)

Write the optional complement as

\[
 B=C\setminus Z_P,
\]

and for every owner define its forced gap and optional occupancy

\[
 g_U=m-|N(U)\cap Z_P|,
 \qquad
 b_U=|N(U)\cap B|.
\tag{6.8}
\]

### Corollary 6.2 (exact gap-saturation form)

The unpaid load is

\[
 \boxed{
 \Omega_P(C)
 =\sum_U\left[
  (2-d_P(U))\mathbf1_{\{b_U=g_U\}}
  +\mathbf1_{\{d_P(U)=0\}}
   \mathbf1_{\{b_U=g_U-1\}}
 \right],}
\tag{6.9}
\]

where an indicator with the impossible value `g_U-1=-1` is zero.  Since
`2|Z_P|=|E(P)|`, the complementary cut fails exactly when

\[
 \boxed{\Omega_P(Z_P\cup B)>2|B|.}
\tag{6.10}
\]

#### Proof

Because `B` and `Z_P` are disjoint, `d_C(U)=m` is equivalent to
`b_U=g_U`, while `d_C(U)=m-1` is equivalent to `b_U=g_U-1`.  Substitute
these equivalences in (6.2).  The right side of (6.4) becomes

\[
 2|C|-|E(P)|=2|B|.
\]

This proves both displays. \(\square\)

Thus the co-small problem no longer involves all complement vertices.
After the forced bank `Z_P` is inserted, only two structures can create
deficiency: residual-capacity units on completely filled owner cliques,
and unprotected owner cliques missing exactly one facet.  Equation (6.10)
identifies the remaining task as a concrete gap-saturation inequality on
the optional bank `B`.

## 7. Exact compression-transfer barrier

Let `x in A` and `y notin A`, and put

\[
 A'=A\setminus\{x\}\cup\{y\}.
\]

### Theorem 7.1 (protected exchange identity)

The exact change in residual Hall surplus is

\[
 \boxed{
 \mu_P(A')-\mu_P(A)
 =r_x-e_A(x)+u_{A\setminus\{x\}}(y)-r_y.}
\tag{7.1}
\]

In particular, if `A` is a maximum-deficiency shore, then the right side
is nonnegative; the exchange preserves maximum deficiency if and only if
it is zero.

#### Proof

Apply the removal identity (4.3), followed by the addition identity (4.4)
at `A setminus {x}`. \(\square\)

For an ordinary coordinate compression, `y` is obtained from `x` by
replacing a larger coordinate by a smaller one.  The unprotected capped
shadow is monotone under this move, but (7.1) contains four
occurrence-labelled residual terms.  The constant-spread estimates
(5.1)--(5.3) bound their aggregate frequency; they do not determine the
sign of (7.1) for a specified inversion.

There is an important forced-element correction.  If `A=A^-`, then every
`x in A^-` belongs to every maximum-deficiency shore.  Hence no exchange
which deletes `x` can have zero value in (7.1).  Forced inversions of the
minimal shore must be repaired by **adding** their shifted images in a
larger member of the DM lattice, not by exchanging away the forced source.

The full min-cut lattice makes this exact.  Contract the strongly
connected components of the residual network `mathcal R_f` of a maximum
flow.  Its condensation is a directed acyclic graph `Q_f`.  Let `q_s` and
`q_t` be the components of `s` and `t`.  A minimum-cut source side is
exactly a successor-closed union of components containing `q_s` and
omitting `q_t`.

For a fixed coordinate order, augment `Q_f` as follows.  Whenever lower
vertices `x,y` satisfy that `y` is an elementary downward coordinate shift
of `x`, add the implication arc

\[
 [x]\longrightarrow[y].
\tag{7.2}
\]

Write `Q_f^sh` for this augmented digraph.

### Theorem 7.2 (exact shifted-DM reachability criterion)

There exists a shifted maximum-deficiency shore if and only if

\[
 \boxed{q_t\text{ is not reachable from }q_s\text{ in }Q_f^{\rm sh}.}
\tag{7.3}
\]

When (7.3) holds, the successor closure of `q_s` in `Q_f^sh` is the unique
minimal shifted minimum-cut source side; its lower projection is a shifted
maximum-deficiency shore.

#### Proof

A source side of a minimum flow cut is precisely a union of residual SCCs
which contains `q_s`, excludes `q_t`, and is closed under every original
condensation arc.  Its lower projection is shifted precisely when it is
also closed under every implication (7.2).  Thus it is exactly a
successor-closed set in the augmented digraph containing `q_s` and
excluding `q_t`.

Such a set exists if and only if the successor closure of `q_s` omits
`q_t`, which is (7.3).  That closure is contained in every other feasible
closed set, proving minimality and uniqueness. \(\square\)

Consequently the DM closure does **not** presently force `A^-` or `A^+`
to be shifted, initial colex, or a two-sided Boolean interval.  The first
remaining transfer theorem is now the concrete no-path assertion (7.3)
for the constant-spread residual network.

Even (7.3) would produce only a shifted capacity-closed shore.  Capped-
shadow shifting does not classify every shifted extremizer.  A second
extremal theorem would still have to turn that shifted DM shore into an
initial-colex/Macaulay shore, or classify it directly inside another
already-safe family.  If that second theorem produced an initial-colex
minimizer, the localized initial-colex closure would immediately rule out
`delta(P)>0`.

Thus the arbitrary-cut gap has two exact layers: exclude a shift-
implication path from the forced source component to the forbidden sink
component, then classify the resulting shifted capacity-closed shore.
Alternatively one may classify the irreducible core (4.8) directly.

## 8. Dependencies

| role | file | SHA-256 |
|---|---|---|
| protected Ore weighted-boundary ledger | `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md` | `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891` |
| exact co-small degree/rebate criterion | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| constant-spread all-cut and endpoint estimates | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| capped-shadow compression theorem | `MATH_THEOREM_CAPPED_LOWER_SHADOW_COMPRESSION_AND_PARTIAL_COLEX_OBSTRUCTION_20260804.md` | `6e138117e2310bcc8087d3cc67cb07bd1702f0674b1ac1369298205b4fc1610f` |
| localized initial-colex closure | `MATH_THEOREM_LOCALIZED_INITIAL_COLEX_PROTECTED_ORE_COMPLETE_20260804.md` | `1c1ca29979c511534bfaf3adfa558be5ba9bfec5d6b93dcc33d6e44451e0c96a` |
