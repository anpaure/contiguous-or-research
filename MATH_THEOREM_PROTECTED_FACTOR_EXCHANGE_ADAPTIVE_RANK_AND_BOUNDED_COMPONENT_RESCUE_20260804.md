# Protected factor exchange, adaptive graphic rank, and bounded-component pull rescue

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical exchange and min--max
reductions, plus an exact bounded-component consequence for any connected
tree-compatible pull host.  No search or computational construction is
used.  The result does not assert that an arbitrary prescribed wedge bank
lies in the canonical GMN factor, nor that a bounded number of factor
components alone gives an additive-constant OR word.

## 0. Main results

Let `G=ML_m`, let

\[
 N=|V(G)|=2{2m-1\choose m},
\]

let `D` be a degree-at-most-two protected edge bank, and let `Z` be a fixed
forbidden edge bank disjoint from `D`.

There are three exact conclusions.

### A. Protected factor completions have one exchange class

Any two spanning two-factors of `G` which contain `D` and avoid `Z` are
connected by a sequence of alternating-circuit switches, every one of
which preserves `D` and avoids `Z`.

This removes an abstract reachability obstruction once arbitrary
alternating circuits are allowed.  It does not say that a prescribed local
pull catalogue contains those circuits, or that the number of factor
components decreases at each switch.

### B. Exact adaptive factor-rank formula

For a degree-at-most-two bank `P` and fixed forbidden set `Z`, let
`delta_star(P,Z)` be the exact guarded Ore--Ryser deficiency from the
protected extension theorem.  Thus

\[
 \delta_\star(P,Z)=0
 \iff P\text{ extends to a spanning two-factor avoiding }Z.
\tag{0.1}
\]

Define

\[
 \begin{split}
 \rho(D,Z)=\max\{|R|:\;&R\subseteq E(G)-Z\text{ is a graphic forest},\\
                 &\Delta(D\cup R)\le2,\quad
                   \delta_\star(D\cup R,Z)=0\}.
 \end{split}
\tag{0.2}
\]

If the protected completion family is nonempty, then

\[
 \boxed{
 \min_{F\supseteq D,\ F\cap Z=\varnothing}
       |\operatorname{Comp}(F)|
   =N-\rho(D,Z).}
\tag{0.3}
\]

Hence a protected Hamilton factor exists exactly when
`rho(D,Z)=N-1`; a protected factor with at most `c` components exists
exactly when `rho(D,Z)>=N-c`.

Formula (0.3) is the exact joint/adaptive topology gate.  It correlates a
large graphic forest with the residual `b`-factor cut, rather than fixing a
two-factor first and testing one pull host afterward.

### C. Static disconnection still gives a bounded factor

Suppose one completion `F` has a connected tree-compatible pull host `H`.
Let

\[
 B_D=\{e\in E(H):O_e\cap D\ne\varnothing\},
 \qquad H_D=H-B_D,
\tag{0.4}
\]

and let every factor edge belong to at most `lambda` pull old phases.
A maximal forest of `H_D` switches `F` to a protected factor with exactly

\[
 |\operatorname{Comp}(H_D)|
 \le1+|B_D|
 \le1+|D|\lambda
\tag{0.5}
\]

components.  For `p` full protected wedges, `|D|=2p`, so

\[
 \boxed{c\le1+2p\lambda.}
\tag{0.6}
\]

Thus failure of the protected-pull connectivity cut is not catastrophic.
For an absolute number of tasks and bounded pull load it leaves only an
absolute number of factor cycles.  If `p=Theta(d)`, however, (0.6) gives
only `O(d)`, not `O(1)`.

## 1. Protected alternating-circuit exchange

Let

\[
 \mathfrak F(D,Z)
 =\{F:\ F\text{ is a spanning two-factor of }G,
          D\subseteq F,\ F\cap Z=\varnothing\}.
\tag{1.1}
\]

An **alternating circuit switch** replaces the red phase of a closed
edge-distinct alternating trail by its blue phase.  The trail may revisit a
vertex, but at every vertex it uses the same number of red and blue
incidences.

### Theorem 1.1 (protected factor-exchange connectivity)

If `F,F' in mathfrak F(D,Z)`, then `F` can be transformed into `F'` by
edge-disjoint alternating-circuit switches.  Every intermediate graph lies
in `mathfrak F(D,Z)`.

#### Proof

Colour the edges of `F-F'` red and the edges of `F'-F` blue.  At every
vertex,

\[
 d_{F-F'}(v)=2-d_{F\cap F'}(v)=d_{F'-F}(v).
\tag{1.2}
\]

Pair red and blue incidences at each vertex.  Following these local pairs
decomposes `F triangle F'` into edge-disjoint closed alternating trails.

Toggle the trails one at a time.  At each vertex of one trail, equally many
present red edges are removed and absent blue edges are inserted.  Degree
two is therefore preserved, and no multiple edge is created.  The trails
are edge-disjoint, so an untoggled trail still has its red phase present and
its blue phase absent after all earlier toggles.

Every edge of `D` belongs to `F cap F'`, so no switched trail contains it.
Every edge used by a trail belongs to `F union F'`, which is disjoint from
`Z`.  Hence all intermediate two-factors contain `D` and avoid `Z`.  After
all trails are toggled the result is `F'`. \(\square\)

### Corollary 1.2

If a protected Hamilton factor exists, every protected two-factor
completion can reach one by protected alternating-circuit switches.

The corollary is not a monotone descent theorem.  A path to a Hamilton
factor may temporarily increase the number of components, and one
alternating circuit can be arbitrarily long.  Replacing “alternating
circuit” by a fixed local `C_6`/pull catalogue is a genuine restriction.

## 2. Exact adaptive graphic-rank completion

For a spanning subgraph `J` of `G`, let `r_gr(J)` be its graphic-matroid
rank.  If `F` is a spanning two-factor, then

\[
 r_{\rm gr}(F)=N-|\operatorname{Comp}(F)|.
\tag{2.1}
\]

The guarded Ore--Ryser theorem gives the exact extension test (0.1) for
every fixed `P,Z`.  No asymptotic expansion estimate is used below.

### Theorem 2.1 (joint adaptive forest-rank formula)

Assume `mathfrak F(D,Z)` is nonempty.  Then (0.3) holds.

#### Proof

Let

\[
 c_*=\min_{F\in\mathfrak F(D,Z)}|\operatorname{Comp}(F)|.
\]

Choose a minimizing factor `F_*`.  A spanning forest of its components has
exactly `N-c_*` edges; call it `R_*`.  Then

\[
 R_*\subseteq F_*,\qquad
 \Delta(D\cup R_*)\le2,
\]

and `F_*` itself proves
`delta_star(D union R_*,Z)=0`.  Hence

\[
                         \rho(D,Z)\ge N-c_*.
\tag{2.2}
\]

Conversely, let `R` attain `rho(D,Z)`.  By its defining extension cut,
there is a factor `F in mathfrak F(D,Z)` containing `R`.  Since `R` is a
forest,

\[
 r_{\rm gr}(F)\ge |R|=\rho(D,Z),
\]

and therefore, by (2.1),

\[
 |\operatorname{Comp}(F)|
   =N-r_{\rm gr}(F)
   \le N-\rho(D,Z).
\tag{2.3}
\]

Thus `c_*<=N-rho(D,Z)`.  Inequality (2.2) gives the reverse inequality,
so equality holds. \(\square\)

### Corollary 2.2 (exact Hamilton and bounded-component rows)

Under the same nonemptiness hypothesis:

\[
 \begin{aligned}
 &\exists\text{ a Hamilton factor containing }D\text{ and avoiding }Z
       &&\iff \rho(D,Z)=N-1,\\
 &\exists\text{ such a factor with at most }c\text{ components}
       &&\iff \rho(D,Z)\ge N-c.
 \end{aligned}
\tag{2.4}
\]

This is strictly more adaptive than the static protected-pull cut.  It
ranges simultaneously over all degree-compatible forests and all factor
completions.  Its difficulty is also explicit: forest selection and the
exact Ore--Ryser extension cut are correlated.  The extendable-forest
family is not asserted to be a matroid.

## 3. Protected partition deficiency of a static host

Return to a factor `F` with component set `mathcal C` and a connected
tree-compatible host `H`.  For a partition `Pi` of `mathcal C`, write
`E_J(Pi)` for the edges of a graph `J` whose endpoints lie in different
blocks of `Pi`.

Define the **protected partition deficiency**

\[
 \operatorname{ppd}(F,D,H)
 =\max_{\Pi}
    \bigl(|\Pi|-1-|E_{H_D}(\Pi)|\bigr).
\tag{3.1}
\]

The one-block partition ensures this maximum is nonnegative.

### Lemma 3.1

\[
 \boxed{
 \operatorname{ppd}(F,D,H)
 =|\operatorname{Comp}(H_D)|-1
 =r_H(E(H))-r_H(E(H_D)).}
\tag{3.2}
\]

#### Proof

Let `q=|Comp(H_D)|`.  For any partition `Pi`, restrict it to each connected
component of `H_D`.  If that component meets `s` blocks, connectedness
supplies at least `s-1` cross-block edges.  Summing gives

\[
                         |E_{H_D}(\Pi)|\ge|\Pi|-q.
\]

Hence the expression in (3.1) is at most `q-1`.  Equality is attained by
the partition into the `q` connected components of `H_D`.

Because `H` is connected,

\[
 r_H(E(H))=|\mathcal C|-1,
 \qquad
 r_H(E(H_D))=|\mathcal C|-q,
\]

which proves the rank identity. \(\square\)

Static `PPC` is exactly `ppd=0`.  The bounded-component relaxation is
`ppd<=c-1`.

### Theorem 3.2 (maximal transparent-forest rescue)

Let `T` be a maximal graphic forest of `H_D`, meaning a spanning tree in
each connected component of `H_D`.  Apply its pull switches.  The resulting
factor:

1. contains `D`;
2. has exactly `1+ppd(F,D,H)=|Comp(H_D)|` components; and
3. contains every additionally prescribed pull set `A subseteq E(H_D)`
   whenever `A` is a graphic forest, by choosing `T` to extend `A`.

#### Proof

Every edge of `T` is `D`-transparent.  Tree compatibility makes all
switches legal and makes their component effect contraction of `T`.
Since `T` spans each component of `H_D`, precisely one factor component
remains for every component of `H_D`.  Lemma 2.1 of the static protected
pull theorem preserves `D`.  If `A` is prescribed, graphic-basis extension
inside each component of `H_D` extends it to such a maximal forest. \(\square\)

### Corollary 3.3 (deletion and wedge bounds)

If every factor edge belongs to at most `lambda` old pull phases, then

\[
 \begin{aligned}
 |\operatorname{Comp}(H_D)|
   &\le1+|B_D|\\
   &\le1+|D|\lambda.
 \end{aligned}
\tag{3.3}
\]

For `p` full wedges this is (0.6).

#### Proof

Deleting one edge raises the number of connected components by at most
one, so connectedness of `H` gives the first inequality.  For the second,
count incidences `(d,e)` with `d in D cap O_e`: every forbidden pull
contributes at least one, and every protected factor edge contributes at
most `lambda`.  Apply Theorem 3.2. \(square\)

The bound is sharp from the scalars alone: if `H` is a tree and `B_D`
consists of `b` distinct edges, then `H_D` has exactly `b+1` components.
No total abundance elsewhere in `H` improves that cut.

Combining Theorem 2.1 with Theorem 3.2 gives the adaptive-rank certificate

\[
 \rho(D,\varnothing)
 \ge N-|\operatorname{Comp}(H_D)|
 \ge N-1-|D|\lambda.
\tag{3.4}
\]

## 4. A joint-selection theorem when lower turns are mobile

The static-host quantifier obstruction says that a fixed factor supports
only one wedge at a prescribed lower turn.  It does not apply when each
logical role may choose its lower turn from a large menu.

Fix a two-factor `F`.  For every lower vertex `L`, let `w_F(L)` be its
unique factor-supported full wedge.  Let `S_i` be a menu of eligible lower
vertices for role `i`, `1<=i<=p`.  Let `R subseteq F` be a fixed factor-edge
bank which no selected wedge may meet, and delete from every `S_i` each
lower endpoint of an edge in `R`.  Call the retained menu `S_i'`.

Put

\[
                         \Delta_m={m+1\choose2}+2.
\tag{4.1}
\]

### Theorem 4.1 (factor-supported mobile-turn wedge packing)

If

\[
                         |S_i'|>(p-1)\Delta_m
                         \qquad(1\le i\le p),
\tag{4.2}
\]

then one can choose distinct `L_i in S_i'` such that the supported wedges
`w_F(L_i)` have pairwise distinct owners and pairwise distinct q1 terminal
values.  Their protected edge bank lies in `F` and avoids `R`.

Since at most `|R|` lower vertices are deleted from a raw menu,

\[
 |S_i|>|R|+(p-1)\Delta_m
\tag{4.3}
\]

is a simple sufficient condition.

#### Proof

Fix one supported wedge at `L`, with factor owners `U_1,U_2` and terminal
value `Z=U_1 union U_2`.

Every supported wedge with terminal value `Z` is rooted at an
`(m-1)`-subset of the `(m+1)`-set `Z`.  There are exactly

\[
                         {m+1\choose m-1}={m+1\choose2}
\]

such lower roots, including `L` itself.

Each owner `U_j` has factor degree two.  Besides `L`, it is incident with
at most one other lower root in `F`.  Thus at most two further roots have a
supported wedge sharing an owner with `w_F(L)`.  Some may already occur in
the terminal-conflict family, so the total number of conflicting supported
roots is at most `Delta_m`.

Greedily process the roles.  Each earlier choice excludes at most
`Delta_m` candidates from the next retained menu, hence all earlier choices
exclude at most `(p-1)Delta_m`.  The strict inequality (4.2) leaves a
candidate.  Terminal conflict includes equality of the root itself, so the
chosen roots are distinct.  The construction uses the two factor edges at
each root and the prefilter makes them disjoint from `R`. \(square\)

### Corollary 4.2 (fixed-task mobile-root bounded factor)

Suppose `F` has a connected tree-compatible host of load `lambda`, and the
role menus satisfy (4.2).  The selected supported wedges followed by the
maximal transparent pull forest produce a factor with at most

\[
                         1+2p\lambda
\]

components while retaining all selected owners and q1 terminal values.

For fixed `p` and full lower-turn menus, (4.2) holds for all sufficiently
large `m`, since the number of lower turns is exponential while
`Delta_m=Theta(m^2)`.  This corollary does **not** apply to roles whose
lower turn or wedge value is prescribed in advance.

## 5. What bounded components do and do not buy

If `p` and `lambda` are absolute constants, Corollary 3.3 gives an
`O(1)`-component owner factor.  If `p=O(d)` and `lambda=O(1)`, it gives only
`O(d)` components.  Since `d=Theta(sqrt(m))` in the OR-word application,
that is not an additive-constant conclusion.

Even `O(1)` factor components do not by themselves give an `O(1)` literal
sidecar.  For order-`d` history states `u,v`, the exact chronology-only
joining cost is

\[
 \delta_d(u,v)=d-\operatorname{ov}(u,v),
\tag{5.1}
\]

and two states with zero suffix--prefix overlap cost `d` letters.  Thus two
components can already require an unbounded reset.

The minimal existing downstream bridge has two forms.

### 5.1 Zero-cost completed-hinge fusion

The protected completed-hinge theorem says that if one unprotected packet
`K_{i_t}(a_t,h_t)` is chosen from each residual component and a cyclic
permutation `pi` satisfies

\[
                         h_{\pi(t)}\in H_{i_t}
\tag{5.2}
\]

with every declared owner, palette, residence, upper-witness, and cap guard
compiled into the completed rectangles, then cyclically permuting the heads
fuses all components with zero route sidecar.

### 5.2 Bounded-cost overlap tour

More generally, a literal sidecar needs an accepted ordering of component
ports whose total overlap-routing cost, including every physical guard, is
`O(1)`.  Component count alone controls the number of joins, not their
cost.

At the immediate-upper extraction layer there is a separate bounded
interface: a factor with `c` components reduces the exact
component-omission Hall row to at most `2^c-1` cuts.  Those cuts are still
not automatic.

Therefore the implication needed for `B(k)+O(1)` is not

\[
                         c(F)=O(1)\Longrightarrow O(1)\text{ sidecar}.
\]

It is

\[
 \boxed{
 c(F)=O(1)
 +\text{ completed-hinge fusion or an }O(1)\text{-cost guarded overlap tour}
 +\text{ bounded omission/compiler deficiency}.}
\tag{5.3}
\]

## 6. Exact frontier

What is now unconditional:

1. the protected two-factor completion space has one alternating-circuit
   exchange class;
2. the best achievable component count has the exact adaptive rank formula
   (0.3);
3. a static connected pull host always gives the bounded rescue
   `1+|D|lambda`, even when protected `PPC` fails; and
4. in the mobile-turn regime, a large role menu can be planted directly in
   a chosen factor and then receives that bounded rescue.

What remains open for the general prescribed-wedge problem:

1. prove `rho(D,Z)>=N-O(1)` directly from the Boolean structure, or choose a
   factor/host pair attaining that rank;
2. when `p=O(d)`, improve the crude deletion bound by correlated selection
   or redundant cut expansion;
3. compile full residence/upper/compiler resources into the protected
   switch state; and
4. supply the completed-hinge or bounded-overlap fusion required by (5.3).

The exact joint/adaptive replacement for static `PPC` is therefore the
forest-rank condition

\[
                         \rho(D,Z)\ge N-c,
\]

while the weakest unconditional consequence of a connected bounded-load
static host is

\[
                         c\le1+|D|\lambda.
\]

## 7. Dependencies

| role | file |
|---|---|
| exact guarded Ore--Ryser extension cut | `MATH_THEOREM_L_ORBIT_WEIGHTED_ACTUATOR_PLANTING_AND_GUARDED_STAR_CUT_20260801.md` |
| protected wedges and fixed-turn packing | `MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md` |
| exact fixed-host protected pull cut | `MATH_THEOREM_PROTECTED_WEDGE_STATIC_PULL_CUT_AND_HOST_LIFT_REDUCTION_20260804.md` |
| static pull-tree compatibility and graphic extension | `MATH_THEOREM_PRESELECTED_PORTAL_FOREST_EXTENSION_AND_PULL_HOST_LIFT_GATE_20260801.md` |
| bounded-component omission Hall | `MATH_THEOREM_K_PCS_BOUNDED_FACTOR_COMPONENT_OMISSION_HALL_AND_RESIDENT_COLLAR_20260802.md` |
| completed-hinge fusion and exact component/sidecar criteria | `MATH_THEOREM_A_PROTECTED_HINGE_INTERFACE_AND_EULER_FUSION_20260802.md` |
| exact overlap-distance sidecar obstruction | `MATH_THEOREM_A_UNSATURATED_HINGE_SKELETON_DAMAGE_AND_TWO_SWITCH_EXPANSION_20260802.md` |
