# Atomic FIFO portal tiles and the balanced-doublet reduction

**Date:** 2026-08-06  
**Method:** literal FIFO algebra, Johnson-square routing, and bipartite
orientation bookkeeping; no computation or search  
**Status:** unconditional local construction and sharp local aperture.  A
fixed compound header supports `d-1` independent, regenerative square
portals with all lower and owner occurrences private.  This is best possible
for the canonical punctured-duplicate header.  Fair portal orientations
preserve any unordered two-mark cylinder without dimension-dependent loss,
and opposite-oriented portal doublets enforce the sharp colour cap with only
a `sqrt(2)` cylinder cost.  What is not proved is the integral packing of
these tiles into the global lower/owner macro factor.

## 1. The exact compound-state normal form

Put `t=r-d`, and let a punctured macro have `h in {2,3}` FIFO copies.  At
the first internal lower state write

\[
 V=S_1,
 \qquad R_c=T_1^c\setminus V\quad(1\le c\le h).
 \tag{1.1}
\]

Thus `|V|=t`, `|R_c|=d`, and `V\cap R_c=\varnothing`.  The complete portal
state is

\[
 Z(V;R_1,\ldots,R_h)
   :=\{V\}\mathbin{\dot\cup}
       \{V\cup R_c:1\le c\le h\},
 \tag{1.2}
\]

where the braces denote literal lower/owner resources, not coordinate sets.

Suppose the first two insertions are `(u,v)`, so the old mark is `v`, and
put

\[
                         H=V\cup\{v\}.
 \tag{1.3}
\]

Then `u in V`, `v notin V`, and the first insertion switch has the exact
form

\[
 \boxed{
 (Z(H-v;R_1,\ldots,R_h),v)
       \longleftrightarrow
 (Z(H-u;R_1,\ldots,R_h),u).}
 \tag{1.4}
\]

In particular, both the `(t+1)`-set `H` and every owner-tail set `R_c` are
invariants of an aligned portal route.

### Lemma 1.1 (compound portals are hole walks)

For a fixed header `(H;R_1,...,R_h)`, the possible compound states are the
vertices

\[
                         z_x=(Z(H-x;R_1,\ldots,R_h),x),
                         \qquad x\in H,
 \tag{1.5}
\]

and a first-insertion switch is precisely an edge `z_v z_u` of the complete
graph on `H`.  The output phase of `v -> u` is literally the input phase of
an aligned next switch beginning at `u`.

#### Proof

The lower switch replaces `u` by `v`.  Every level-one owner is the disjoint
union of that lower state and its unchanged queue tail `R_c`, so it undergoes
the same replacement.  The mark changes from the second insertion `v` to
the new second insertion `u`.  This is (1.4).  Conversely, any two distinct
holes `u,v in H` give the two first insertions in the opposite order.  Hence
the state graph is the complete graph on the holes.  \(\square\)

This is more rigid than an arbitrary Johnson-square network: the common
`(t+1)`-union and the full owner-tail header cannot change along an aligned
route.

## 2. The invariant second row gives a sharp aperture

Use the canonical punctured-duplicate header

\[
 R_c=\{a\}\mathbin{\dot\cup}Y_c,
 \qquad |Y_c|=d-1,
 \tag{2.1}
\]

where the `Y_c` are mutually disjoint and `a` is the common first lower
deletion.  If the order of the queue after the first transition is

\[
                         (x_2^c,x_3^c,\ldots,x_d^c,a),
 \tag{2.2}
\]

then the second owner is

\[
                         T_2^c=H\cup(R_c-\{x_2^c\}).
 \tag{2.3}
\]

Notice that it is unchanged by the first-insertion switch.

### Theorem 2.1 (sharp canonical header aperture)

An owner-disjoint family of macros using one canonical header
`(H;R_1,...,R_h)` has size at most `d-1`.  This remains true even if all
deeper FIFO orders are allowed to vary arbitrarily.

#### Proof

Fix one copy `c`.  Pairwise owner-disjointness requires the second owners
(2.3) to be distinct.  The map

\[
                         x\longmapsto H\cup(R_c-\{x\})
 \tag{2.4}
\]

is injective, while `x_2^c` must lie in the `(d-1)`-set `Y_c`: the common
deletion `a` is the last queue symbol in (2.2), not its head.  Hence there
are at most `d-1` macros.  Later permutations cannot change (2.3), so the
bound is absolute for this header.  \(\square\)

Thus the factorial FIFO tail orbit does not permit a macroscopic number of
arcs through one header.  Its correct use is to realize a mesoscopic bank of
order `d`, and this is sharp.

There is a second, independent guard bound.  For a portal edge `v -> u`,
let `g` be its second lower deletion.  The invariant second lower state is

\[
                              S_2=H-g.                    \tag{2.5}
\]

Consequently the guards of different macros are distinct and cannot be a
hole used by any current or alternative portal state.  A route forest with
`m` arcs and `p` state components therefore needs at least

\[
                              2m+p                        \tag{2.6}
\]

labels in `H`: `m+p` state holes and `m` guards.  For independent one-edge
portals it needs `3m` labels.  In the central regime `t+1 >> d`, this guard
bound is weaker than Theorem 2.1.

## 3. An explicit atomic tile of rank `d-1`

Assume `d>=4`, choose

\[
                              q\le d-1,
                              \qquad 3q\le t+1.           \tag{3.1}
\]

Inside a `(t+1)`-set `H`, choose pairwise distinct labels

\[
                    v_1,\ldots,v_q,
                    u_1,\ldots,u_q,
                    g_1,\ldots,g_q.                       \tag{3.2}
\]

Choose the canonical tails (2.1).  For every `i` and every copy `c`, choose
the first head `x_2^{i,c}` so that, for fixed `c`, these `q` labels are
distinct members of `Y_c`.  Complete each of them to an arbitrary ordering
of `Y_c` in (2.2).

For macro `i`, use

\[
 \begin{aligned}
 S_0^i&=H-\{u_i,v_i\}+\{a\},\\
 a_1^i&=a,            & b_1^i&=u_i,\\
 a_2^i&=g_i,          & b_2^i&=v_i.
 \end{aligned}                                             \tag{3.3}
\]

Choose a fresh private label `p_i` for `b_3^i`, and keep `p_i` in every
later lower state.  The remaining deletions are distinct members of the
initial lower state, the remaining insertions are fresh, and the terminal
insertions distinguish the `h` copies.  Finally, choose a private initial
FIFO head `x_1^{i,c}` for every `(i,c)`.

All of these choices fit whenever

\[
                         k-t\ge (2h+3)d+O(h),             \tag{3.4}
\]

which holds throughout the asymptotic central regime.  The constant in
(3.4) is deliberately inessential; the construction uses only `O_h(d)`
labels outside `H`.

### Theorem 3.1 (atomic independent-portal tile)

The `q` macros in (3.3) may be completed so that:

1. all current compound bundles and all alternative compound bundles are
   pairwise equal only at a deliberately identified route junction;
2. in the independent-portal version displayed above, the `2q` bundles
   are pairwise disjoint and every alternative bundle is initially free;
3. every lower and owner resource outside those bundles is private;
4. every subset of the `q` switches is simultaneously legal; and
5. after any sequence of switches the unused switches retain the same
   properties, while each used switch is reversibly regenerated.

Thus the literal portal max-flow rank of one canonical header is `d-1`,
and this attains Theorem 2.1.

#### Proof

The current and alternative first lower states are

\[
                         H-v_i,qquad H-u_i.               \tag{3.5}
\]

They are all distinct by (3.2).  The current and alternative level-one
owners are obtained by adjoining `R_c`, so they are also distinct.  If
`c\ne c'`, equality is impossible because the nonempty private parts
`Y_c,Y_{c'}` are disjoint.  Hence all compound bundles in the independent
version are disjoint.

The invariant initial lower states contain `a` and miss the distinct pair
`{u_i,v_i}`.  The invariant second states are the distinct sets `H-g_i`,
and (3.2) separates both families from (3.5).  Starting at the third
transition, every lower state of macro `i` contains its private `p_i`, so
no two such lower paths meet and none meets an earlier state.

At level two, (2.3) and the distinct choices of `x_2^{i,c}` separate all
owners for a fixed copy.  Different copies are separated by their private
tail banks.  Starting at level three, `p_i` separates different macros;
the remaining tail or the terminal insertion separates different copies.
Private `x_1^{i,c}` separates the level-zero owners.  The number of
tail labels and continuation labels used is `O_h(d)`, so these choices can
be made under (3.4).

It follows that the invariant bank avoids every alternative bundle and
that distinct alternatives do not collide.  The exact simultaneous-toggle
criterion therefore permits every subset of the switches.  A switch merely
interchanges which of its two disjoint bundles is occupied, so it remains
available in reverse and has no effect on any other portal.  This proves
all five assertions.  \(\square\)

The same proof realizes a path

\[
                         z_{v_0}\to z_{v_1}\to\cdots
                         \to z_{v_q}                       \tag{3.6}

by identifying the alternative bundle of one macro with the current bundle
of the next.  Only one copy of every intermediate resource is used.  The
guard and second-owner arguments are unchanged.  Toggling a suffix moves
the unique free compound state to any prescribed vertex of the path and
transports exactly one unit of mark load.

## 4. Exact cylinder preservation at the orientation layer

For one unoriented portal occurrence write

\[
                  \bar\alpha=(T_2,\{u,v\}),              \tag{4.1}
\]

and let its two oriented marked states be

\[
                  \alpha^+=(T_2,u,v),
                  \qquad \alpha^-=(T_2,v,u).             \tag{4.2}
\]

Because the independent tile is a product of literal involutions, it may
be oriented by independent fair coins after the unoriented resources have
been chosen.

### Theorem 4.1 (orientation does not cost a growing cylinder)

Suppose an unoriented selection law satisfies, conditionally on every
allowed separator history,

\[
 \mathbb E\!\left[\prod_{j=1}^m
       1_{\{\bar\alpha_j\ \operatorname{selected}\}}\mid\mathcal F\right]
        \le \bar\vartheta^m                         \tag{4.3}
\]

for distinct owner occurrences and all `m<=C_0d`.  Independently fairly
orient every selected portal in an atomic tile.  Then

\[
 \mathbb E\!\left[\prod_{j=1}^m
       1_{\{\alpha_j\ \operatorname{selected}\}}\mid\mathcal F\right]
        \le (\bar\vartheta/2)^m.                         \tag{4.4}
\]

The assertion is hereditary after any stopped exposure of tile states, for
every subsequent cylinder consisting of still-unexposed occurrences.

#### Proof

Conditional on the unoriented selection and on every previously exposed
coin, the unexposed atomic portals are still independent fair involutions.
Every compatible prescribed orientation contributes a factor `1/2`.
Multiplying (4.3) by `2^{-m}` proves (4.4).  After a stopping time the coins
on the unexposed portals are still independent and fair, proving the stated
hereditary form.  \(\square\)

Thus the physical companion orientation is not the source of a
dimension-dependent cylinder loss.  The remaining marked-cylinder input is
the unordered pair law (4.3).

There is also a cap-forcing variant which uses no global orientation flow.
Pair two resource-disjoint atomic portals with the same unordered coordinate
pair `{u,v}` and require opposite orientations.  Call this a **balanced
doublet**.  It contributes exactly one mark to `u` and one mark to `v`.

### Corollary 4.2 (balanced doublets)

Let `D` be the multigraph on `[k]` whose edges are balanced doublets.  If

\[
                              \Delta(D)\le L,              \tag{4.5}
\]

then every mark load is at most `L`, identically in the choices of the
doublet orientations.  If the two opposite orientations of each doublet
are chosen by independent fair coins, then for every compatible family of
`m` prescribed portal orientations the conditional probability is at most

\[
                              (2^{-1/2})^m.                \tag{4.6}
\]

The same estimate holds after a **doublet-closed** stopping history, meaning
that the history exposes either both members of a doublet or neither.  It is
not asserted after exposing exactly one member, because its mate is then
forced.

Consequently an unordered cylinder of intensity `\bar\vartheta` becomes an
oriented cylinder of intensity at most

\[
                              {\sqrt2\over2}\bar\vartheta.
 \tag{4.7}
\]

#### Proof

Every incident doublet contributes one mark at a coordinate, proving
(4.5).  In one doublet, one prescribed orientation has probability `1/2`;
two compatible prescribed orientations also have probability `1/2`.
These are bounded by `2^{-1/2}` and `(2^{-1/2})^2`, respectively.  Different
doublets use independent coins.  Multiply over the doublets and then by the
unordered cylinder.  A doublet-closed exposure leaves the unexposed
doublet coins independent and fair, proving the stopped form.  \(\square\)

The fixed loss `sqrt(2)` is harmless for the bottom Haxell theorem, which
allows any absolute cylinder constant.

Balanced doublets also admit the exact global fractional ledger.  Let
`M=binom(k,t)`, `W=binom(k,r)`, and `rho=W/M`.  For `h in {2,3}`, let
`D_h` be the complete labelled coordinate orbit of one resource-disjoint
balanced doublet made from two `h`-fold macros.  Such a template exists by
applying Theorem 3.1 with `q=1` to two headers containing the same port pair
and at Johnson distance greater than `2d`.  This is possible under the
central ground-set inequality.  Every lower or owner resource of one macro
then remains distinct from every resource of the other; orient the two port
pairs oppositely.

### Theorem 4.3 (exact balanced-doublet fractional factor)

Assume

\[
                         2\le {\rho d\over d+1}\le3.       \tag{4.8}
\]

The union of the two doublet orbits `D_2,D_3` has a fractional factor for
which

\[
 \boxed{
 \begin{array}{c}
 \text{every rank-}t\text{ lower load}=1,\\
 \text{every rank-}r\text{ owner load}=1,\\
 \text{every coordinate mark load}=M/(kd),\\
 \text{every marked level-two owner marginal}=1/[r(d+1)].
 \end{array}}                                             \tag{4.9}
\]

Every fractional edge is already a literal atomic portal pair and is
colour-balanced before any orientation is chosen.

#### Proof

For fixed `h`, give every member of `D_h` weight

\[
                              {M\over2d|D_h|}.             \tag{4.10}
\]

A doublet contains `2d` common lower resources, so the total weighted lower
incidence is `M`.  Coordinate transitivity makes it uniform on the
`M`-element lower layer, giving lower load one.

The total weighted owner incidence is

\[
 {M\over2d}\,2h(d+1)={Mh(d+1)\over d},                   \tag{4.11}
\]

so the owner marginal is

\[
                              \eta_h={h(d+1)\over\rho d}. \tag{4.12}
\]

Use the same convex coefficients as for the ordinary `2/3` macro factor,

\[
 \lambda_3={\rho d\over d+1}-2,
 \qquad
 \lambda_2=3-{\rho d\over d+1}.                          \tag{4.13}
\]

They are nonnegative, sum to one, and make
`lambda_2 eta_2+lambda_3 eta_3=1`; the lower marginal remains one.

Finally, every balanced doublet contributes one mark to each endpoint of
its port edge.  Its total weighted mark incidence is therefore

\[
                              {M\over2d}\,2={M\over d}.   \tag{4.14}
\]

Coordinate transitivity divides this equally among the `k` coordinates,
giving `M/(kd)`.

A doublet has `2h` level-two owner occurrences carrying its two marks.
Thus its total weighted marked-owner mass is `hM/d`.  After the mixture,
the weighted mean multiplicity is

\[
                         2\lambda_2+3\lambda_3
                         ={\rho d\over d+1}.              \tag{4.15}
\]

The coordinate group is transitive on the `Wr` pointed owner occurrences,
so their common marginal is

\[
 {[(\rho d)/(d+1)]M/d\over Wr}={1\over r(d+1)}.          \tag{4.16}
\]

The atomic and balance assertions are part of the doublet template.
\(\square\)

Theorem 4.3 is stronger than a post-hoc port orientation at the fractional
level: the sharp colour row is built into every superedge.  It is not an
integral matching theorem.  Its superedges have twice the growing macro
rank, and no existing rounding result supplies the required `O(1/d)` leave
and hereditary unordered cylinder.

## 5. The exact remaining host and its maximum codegrees

The sharp integral host is now explicit.  Put

\[
                              L=\left\lceil{M\over kd}\right\rceil
 \tag{5.1}
\]

and make `L` private slots `(s,j)` for every coordinate `s`.  For a
balanced doublet `D in D_h` with port edge `{u,v}` and every `(i,j) in
[L]^2`, make one augmented hyperedge containing

* the `2d` lower resources of `D`;
* the `2h(d+1)` owner resources of `D`; and
* the two slots `(u,i),(v,j)`.

Call the resulting typed hypergraph `B_h`.  Its edge rank is

\[
                              R_h=2d+2h(d+1)+2,
 \tag{5.2}
\]

so `R_2=6d+6` and `R_3=8d+8`.

### Theorem 5.1 (slot-augmented doublet factor)

Give every edge above a doublet in `D_h` weight

\[
                    {\lambda_hM\over2d|D_h|L^2}.          \tag{5.3}
\]

Then every lower and owner resource has load one, while every coordinate
slot has load

\[
                              {L_*\over L},
                              \qquad L_*={M\over kd}.      \tag{5.4}
\]

Consequently any matching in `B_2 union B_3` projects to resource-disjoint
literal macros whose balanced-doublet port multigraph has maximum degree at
most `L`; after opposite orientation, its mark cap is automatically `L`.

#### Proof

Splitting the weight in Theorem 4.3 equally among `L^2` slot pairs does not
change a lower or owner load.  A fixed slot `(s,i)` occurs over every base
doublet incident with `s`, and the other endpoint has `L` possible slots.
The complete coordinate orbit has `2|D_h|/k` incident doublets at `s`.
Thus its load from orbit `h` is

\[
 {2|D_h|L\over k}
 {\lambda_hM\over2d|D_h|L^2}
       ={\lambda_hM\over kdL}.                            \tag{5.5}
\]

Summing over `h` gives (5.4).  In an integral matching no slot is repeated,
so at most `L` selected doublets are incident with a coordinate.  Balanced
doublets then give the mark assertion.  \(\square\)

For fixed `h`, before the harmless `2/3` orbit replication, the three
degrees are exactly

\[
 \begin{aligned}
 D_L^{(h)}&={2d|D_h|L^2\over M},\\
 D_O^{(h)}&={2h(d+1)|D_h|L^2\over W},\\
 D_S^{(h)}&={2|D_h|L\over k}.
 \end{aligned}                                             \tag{5.6}
\]

They differ only by fixed factors in the central regime, since
`L/L_*=1+o(1)`.  Rationally replicating the two typed orbits according to
the weights (5.3) makes the weighted lower, owner, and (when `L=L_*`) slot
degrees equal.  This is an exact regularization, not a matching theorem.

### Proposition 5.2 (maximum pair-codegree scale)

Uniformly over distinct resource vertices of the slot-augmented doublet
host,

\[
 {\operatorname{codeg}(x,y)\over
       \min\{\deg(x),\deg(y)\}}
   =O\!\left({d\over k^2}
             +{1\over kL}
             +{d\over {k-t\choose d}}\right).
 \tag{5.7}
\]

In the central regime this is `O(d/k^2)=O(d^{-3})`.  More precisely:

1. two lower vertices or two owner vertices have normalized codegree
   `O(d/k^2)`;
2. a lower-owner pair has normalized codegree at most
   `O(d/binom(k-t,d))` (and symmetrically with `binom(r,d)` from the owner
   side);
3. two slots over the same coordinate have codegree zero, while slots over
   distinct coordinates have normalized codegree exactly
   `1/[L(k-1)]`; and
4. a lower-slot or owner-slot pair has normalized codegree `O(1/(kL))`
   from the lower/owner side and an exponentially smaller bound from the
   slot side.

#### Proof

Fix a lower vertex `S`.  Its stabilizer is transitive on the lower vertices
at Johnson distance `ell`, an orbit of size

\[
                         {t\choose\ell}{k-t\choose\ell}.
 \tag{5.8}
\]

A doublet through `S` has only `2d-1` other lower vertices.  Summing its
codegrees over a distance orbit and using transitivity bounds the ratio by
`(2d-1)` divided by (5.8), whose minimum nontrivial value is
`t(k-t)=Theta(k^2)`.  The same argument for the at most `2h(d+1)-1`
other owners uses the owner orbit
`binom(r,ell)binom(k-r,ell)` and gives the same order.

For a lower-owner pair, the stabilizer orbit with
`q=|S\setminus T|` has size

\[
                         {t\choose q}{k-t\choose d+q}.    \tag{5.9}
\]

All co-occurring values in the fixed doublet template have `q=O(d)`.  In
the central range (5.9) is increasing there, so it is at least
`binom(k-t,d)`.  There are only `O(d)` owner roles.  Reversing the shores
gives `binom(r,d)`.

For distinct coordinates `u,v`, coordinate transitivity puts exactly
`|D_h|/binom(k,2)` base doublets over their port pair.  Once both slot
indices are fixed there is no remaining slot multiplicity.  Division by
`D_S^{(h)}=2|D_h|L/k` gives `1/[L(k-1)]`; two slots over one coordinate
cannot belong to one edge.

Finally, conditioned on a fixed lower or owner resource, at most two port
labels occur in an edge.  Double counting over the `Theta(k)` coordinates
in either membership orbit gives `O(1/k)` base incidence, and fixing one
of its `L` slots contributes the additional factor `1/L`.  From the slot
side a doublet has only `O(d)` lower/owner roles among an exponential shore.
Combining the four cases proves (5.7).  \(\square\)

Thus the new host has the same excellent pair-codegree scale as the old
path host, and every selected edge is already colour-safe.  Nevertheless
its rank is `Theta(d)` and the required relative leave is `Theta(1/d)`.
The polynomial partial-matching extension theorem concerns rank-two
middle-level incidence matchings and does not apply to `B_h`.  The audited
fixed-rank nibble theorems do not have constants uniform in this simultaneous
rank/error regime and do not export the stopped unordered cylinder.  A new
correlated growing-rank rounding lemma is therefore still genuinely needed.

For completeness, (5.7) gives only the coarse higher-codegree consequence

\[
                         {\Delta_j\over\Delta}
                         =O(d/k^2)\qquad(j\ge2),           \tag{5.10}
\]

by retaining any pair among the prescribed vertices.  A power-decaying
hierarchy uniform in `j=O(d)` has not been proved for the complete doublet
orbit.  That hierarchy, or a direct stopped-route substitute, is part of
the remaining rounding lemma; it must not be inferred from the pair bound.

The apparent two-macro clustering of a doublet does, however, have the
correct marked merger scale.  Choose the template headers `H,H'` with

\[
                         |H\setminus H'|=|H'\setminus H|=3d
 \tag{5.11}
\]

while keeping the common port pair inside `H\cap H'`.  Choose the two tail
banks cross-disjoint outside `H\cup H'`: every level-two tail of the first
macro is disjoint from every level-two tail of the second.  Then a pointed
level-two owner on one side and one on the other have Johnson distance

\[
                              j_*=4d-1.                   \tag{5.12}
\]

### Proposition 5.3 (doublet partner aperture)

Fix one unoriented pointed state

\[
                         \bar\alpha=(T,\{u,v\})           \tag{5.13}
\]

in the complete coordinate orbit of the separated doublet template.  Given
that `bar(alpha)` is one half of a selected template, any prescribed pointed
state `bar(beta)` on the other half has conditional orbit probability at
most

\[
 {h\over
   {r-2\choose j_*}{k-r\choose j_*}}
       =\exp[-\Omega(d\log d)].                           \tag{5.14}
\]

uniformly for `h in {2,3}`.  Thus making a balanced doublet does not lose
the required same-superedge merger scale.

#### Proof

Both pointed owners contain the fixed port labels `u,v`.  Once `T,u,v` are
fixed, the stabilizer

\[
                 \operatorname{Sym}(T-\{u,v\})
                 \times\operatorname{Sym}([k]\setminus T)
 \tag{5.15}
\]

is transitive on the rank-`r` sets containing `u,v` at Johnson distance
`j_*` from `T`.  Their number is the denominator in (5.14).  The partner
macro has only `h` level-two owner roles, giving the numerator.  Since
`j_*=Theta(d)`, `r,k-r=Theta(k)`, and `k=Theta(d^2)`, the binomial product
is `exp[Omega(d log d)]`.  \(\square\)

Proposition 5.3 is a static orbit aperture.  A stopped integral selector
must preserve it conditionally; the proposition does not supply that
hereditary statement.

## 6. What is closed and what remains

The structural premise behind the square router now has an explicit local
solution:

* aligned compound phases are exact hole states in a complete graph;
* `d-1` fully independent portals can be planted under one canonical FIFO
  header;
* all lower, level-zero, level-two, and deeper owner occurrences can be
  made private;
* the tile has hereditary literal max-flow rank `d-1`; and
* portal orientation costs no dimension-dependent marked-cylinder factor;
  and
* the balanced-doublet orbit has one exact lower/owner/colour fractional
  factor.

The sharp obstruction is equally explicit: one canonical header cannot
support more than `d-1` selected macros because its invariant second-owner
row has only `d-1` possible omissions.  Therefore a global construction
needs `Theta(M/d^2)` distinct headers; one giant common-header router is
impossible.

What remains is the following strictly global statement.

> **Atomic portal-tile packing lemma.**  Round the exact balanced-doublet
> fractional factor (or, equivalently, the joint `2/3` macro factor plus a
> residual portal bank)
> to an owner-disjoint family with `O(M/d)` lower leave which can be
> partitioned into canonical atomic tiles (and `O(M/d)` separator
> remnants), so that either
>
> 1. the resulting portal network has the all-cut flow needed to eliminate
>    every sharp-cap overload, or
> 2. all but the remnants occur in balanced doublets whose port multigraph
>    has maximum degree at most `L=ceil(M/(kd))`.
>
> The unordered marked states must satisfy a fixed-factor cylinder through
> order `O(d)` after every separator exposure; if the doublet orientation
> law is used, those exposures must be doublet-closed.  The terminal queue
> state must remain component-joinable.

The local theorem does **not** prove this packing lemma.  In particular,
one may not select an entire `d`-macro tile as one indivisible matching
edge and then cite Theorem 4.1: that would correlate the inclusion of its
different macros and can destroy the required root cylinder.  Tiles must be
planted inside, or coupled to, a macro selection law which already has the
unordered fixed-factor cylinder.  The exact remaining difficulty is thus
global correlated packing, not compound-bundle alignment or FIFO portal
privacy.
