# Labelled even capacity-two sectors are edge-extendable and strictly Hall

**Date:** 2026-08-05  
**Method:** root the coordinate-pair scan at a prescribed edge; no
computation  
**Status:** unconditional labelled theorem.  Every literal edge belongs to
a perfect matching, so every proper nonempty Hall set has one unit of
strict slack.  Descent through an odd rotational quotient is not proved;
folded edge orbits are the exact remaining boundary.

## 1. Sector and local paths

Let

\[
 \mathcal T_{2m,R}
 =\left\{t\in\{0,1,2\}^{\mathbb Z_{2m}}:
                 \sum_i t_i=R\right\},
 \qquad R\text{ odd}.
\tag{1.1}
\]

Join two states when one token is moved between cyclically adjacent
coordinates.  This graph is bipartite under

\[
                         \chi(t)=\sum_i i t_i\pmod2.
\tag{1.2}
\]

On one ordered coordinate pair, the fixed-local-mass graphs have the
following matchings:

\[
\begin{array}{c|c|c}
\text{mass}&\text{selected edges}&\text{quiet residue}\\ \hline
0&\varnothing&00\\
1&01-10&\varnothing\\
2&20-11&02\\
2&02-11&20\\
3&12-21&\varnothing\\
4&\varnothing&22.
\end{array}
\tag{1.3}
\]

For local mass two either of the two displayed rows may be chosen.  In
both choices every quiet state has even local mass.

## 2. A prescribed edge chooses the rooted scan

### Theorem 2.1 (literal edge extendability)

Every edge of `T_(2m,R)` belongs to a perfect matching.

#### Proof

Fix a literal edge `e=tt'`.  Its moved coordinate boundary belongs to one
of the two alternating perfect matchings of the coordinate cycle
`C_(2m)`.  Use that coordinate perfect matching and order its `m` pairs so
that the pair supporting `e` is first.

On the first coordinate pair choose the row of (1.3) containing `e`.  If
its local mass is two, choose as quiet residue the endpoint of the local
three-vertex path opposite `e`.  On every other pair choose either
mass-two row arbitrarily.

For a global state, scan the coordinate pairs in the declared order and
apply (1.3) at the first pair whose local state is not quiet.  Such a pair
always exists: if every pair were quiet, every pair would have even local
mass, contradicting the odd total `R`.

The operation changes no earlier pair.  At the active pair it exchanges
the two endpoints of one selected local edge, and both endpoints are
nonquiet.  Rescanning therefore selects the same pair and reverses the
move.  The rule is a fixed-point-free involution and hence a perfect
matching.

For `t,t'`, the first coordinate pair is nonquiet and its selected local
edge is exactly `e`.  Thus the global perfect matching contains `e`.
\(\square\)

The construction also covers a wrap edge: every edge of the even
coordinate cycle belongs to one alternating coordinate matching, and the
parity (1.2) toggles across the wrap because `2m-1` is odd.

## 3. Strict Hall expansion

The labelled token graph is connected whenever `R` is in the nontrivial
range; odd `R` excludes the two singleton extreme sectors.  One may move
tokens successively along the connected coordinate cycle from any surplus
coordinate to any deficit coordinate, never exceeding capacity two at the
chosen deficit.

### Corollary 3.1 (one unit of proper Hall slack)

Let `L,Rho` be the two shores of `T_(2m,R)`.  For every nonempty proper
set `U subsetneq L`,

\[
                         |N(U)|\ge |U|+1.
\tag{3.1}
\]

The symmetric statement holds on `Rho`.

#### Proof

Theorem 2.1 supplies a perfect matching, so ordinary Hall gives
`|N(U)|>=|U|`.  Suppose equality held.  Put

\[
                         X=U\cup N(U).
\]

No edge goes from `U` to `Rho setminus N(U)` by definition.  Since the
token graph is connected and `U` is proper and nonempty, some edge joins
`N(U)` to `L setminus U`.

No perfect matching can contain that boundary edge: after using it, all
`|U|` vertices of `U` would have only `|N(U)|-1=|U|-1` remaining possible
mates.  This contradicts Theorem 2.1, which puts every literal edge in
some perfect matching.  Therefore equality is impossible and (3.1)
follows.  \(\square\)

## 4. Consequence for actual receiver Hall

On the labelled cover, the invisible-bicycle inequality from

`MATH_REDUCTION_ACTUAL_EVEN_RECEIVER_HALL_TO_INVISIBLE_BICYCLE_ESCAPE_20260805.md`

has at least one unit of ordinary slack for every proper nonempty shore
set.  Hence every cut whose invisible endpoint multigraph has bicircular
surplus at most one is automatically safe on such a set.  A labelled Hall
obstruction must have one of the following forms:

1. a zero-shore cut `U=emptyset`, which is exactly failure of the initial
   receiver endpoint-list SDR;
2. at least two total units of invisible empty-list/bicycle surplus on one
   proper nonempty cut; or
3. an initially empty job shore.

For `U=L`, every job with a nonempty `A`-shore is visible, so there is no
additional whole-shore obstruction.  Thus, after initial endpoint packing
and nonempty menus are established, only surplus at least two remains on
the labelled cover.

## 5. Quotient boundary

Let an odd cyclic stabilizer act on the labelled sector.  It preserves the
bipartition, but Theorem 2.1's scan begins at the prescribed literal
coordinate pair and is not generally equivariant.  Several literal edge
orbits can project to one simple quotient edge with cancellation in an
invariant skew operator; the standard example `Q_3/C_3=P_4` shows that an
arbitrary quotient edge need not be extendable even when every literal
edge is.

Therefore this note does **not** assert strict Hall after quotienting.  A
sufficient descent theorem would be either:

1. every receiver-relevant quotient edge is Clifford-active; or
2. every proper quotient Hall set lifts to a proper invariant literal
   Hall set with at least one full orbit of slack.

Neither statement is proved here.

There is, however, an exact semiregular descent.

### Theorem 5.1 (semiregular quotient strict Hall)

Let an odd subgroup `H<=C_(2m)` preserve one background sector and act
semiregularly on all its token states.  Then every nonempty proper shore
set `bar U` in the quotient sector satisfies

\[
                         |N(\bar U)|\ge|\bar U|+1.
\tag{5.1}
\]

In particular this holds when

\[
                         \gcd(R,|H|)=1.
\tag{5.2}
\]

#### Proof

Lift `bar U` to the union `U` of its literal `H`-orbits.  Neighbourhood
commutes with taking the full orbit lift.  Semiregularity makes every
vertex orbit have size `|H|`, so

\[
 |U|=|H||\bar U|,
 \qquad
 |N(U)|=|H||N(\bar U)|.
\tag{5.3}
\]

The lift is proper and nonempty.  Corollary 3.1 says

\[
 |H|\bigl(|N(\bar U)|-|\bar U|\bigr)
   =|N(U)|-|U|\ge1.
\]

The left side is a multiple of `|H|`; it is therefore at least `|H|`,
which proves (5.1).

For (5.2), a nonidentity rotation of order `d` partitions the coordinate
set into cycles of length `d`.  A fixed token state is constant on every
such cycle, so its total mass is divisible by `d`.  Every `d` divides
`|H|`; coprimality excludes all nonidentity stabilizers.  \(\square\)

Thus the strict-slack problem is localized to genuinely periodic sectors
for which the token mass and rotational stabilizer share an odd divisor.
All aperiodic background sectors, and all coprime periodic sectors, inherit
the labelled unit of slack.

## 6. Scope

Proved:

1. every literal edge of every even capacity-two sector extends to a
   perfect matching;
2. exact one-unit strict Hall expansion on every proper labelled cut; and
3. semiregular/coprime quotient descent of that strict slack; and
4. automatic payment of any single invisible-bicycle surplus unit on a
   proper nonempty cut in those sectors.

Not proved:

1. descent of edge extendability or strict Hall in the remaining
   nonsemiregular periodic sectors;
2. payment of two or more simultaneous invisible bicycle units;
3. the odd wrap-current theorem; or
4. the complete protected receiver extension.
