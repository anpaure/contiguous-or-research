# Independent audit V1: cap-aware protected-wedge activation and exact menu threshold

**Date:** 2026-08-04  
**Verdict:** **GO**.  No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md`,
SHA-256
`ae4ce45555394121fcf1e7df7840c86a0786b840dedcf96ca414ef9d33c7f188`.

No separate author self-audit was present at freeze time.

## 1. Exact one-wedge cross-menu profile

Fix `w=(L;{a,b})` and a distinct lower turn `L'`.  A shared owner is
possible precisely when

\[
 L'=L-x+a
 \quad\text{or}\quad
 L'=L-x+b
\]

for some `x in L`.  The two alternatives cannot both hold.  In the first
case the extension back to the shared owner is `x`, so all and only the
`m-1` pairs containing `x` form the owner-conflict star.

A terminal conflict requires `L' subset L+a+b`.  Deleting `{a,b}` gives
the excluded turn `L`.  Deleting one external and one internal coordinate
gives one of the owner-star cases, and its terminal pair already contains
the star coordinate.  Deleting two internal coordinates gives

\[
 L'=L-\{x,y\}+\{a,b\}
\]

and the unique conflicting pair `{x,y}`.  These exhaust all rank possibilities.
Thus one prior wedge forbids either one full vertex star, one singleton edge,
or nothing in another full menu, and never more than `m-1` candidates.

## 2. Exact prefix-deletion number

Identify a full menu with `E(K_m)`.  If `t` among `q` previous conflict sets
are stars, their union has at most

\[
 B_t(m)={m\choose2}-{m-t\choose2}
\]

edges.  The remaining `q-t` singleton sets add at most `q-t` edges.  Since

\[
 B_{s+1}(m)-B_s(m)=m-s-1\ge1
 \qquad(s\le q-1\le m-2),
\]

one has

\[
 B_t(m)+q-t\le B_q(m).
\]

The closed form is correct:

\[
 B_q(m)
 ={m\choose2}-{m-q\choose2}
 ={q(2m-q-1)\over2}.
\]

The equality construction is valid.  With distinct `x_j in L_0` and
distinct `c_j,e notin L_0`, the wedges

\[
 L_j=L_0-x_j+c_j,
 \qquad
 w_j=(L_j;\{x_j,e\})
\]

have pairwise distinct two owner values and pairwise distinct terminals.
At `L_0`, wedge `w_j` forbids exactly the star at `c_j`.  The `q` distinct
stars have union `B_q(m)`.  Thus the cardinality threshold is sharp for a
conflict-free prefix.

For `q=p-1`, this becomes

\[
 B_{p-1}(m)={(p-1)(2m-p)\over2}.
\]

## 3. Greedy packing and factor completion

After `i-1` choices, the preceding bound applies to the whole menu at the
next lower turn, hence also to its active sub-menu.  The strict inequality

\[
 |W_i^c|>B_{i-1}(m)
\]

leaves an active nonconflicting wedge.  Induction gives pairwise distinct
`2p` owner values and pairwise distinct `p` terminal values.  The uniform
row with `B_{p-1}` implies all ordered rows by monotonicity.

The selected wedge incidence bank contains `2p` edges and has degree two at
each selected lower turn and degree one at every selected owner.  If its
union with the incumbent bank is degree-compatible and has at most `m-2`
edges, the frozen small protected-factor theorem applies exactly.

Two consecutive lower turns of a factor share their intervening owner.
Since selected turns have disjoint selected owner pairs, they cannot be
consecutive in any completion.

## 4. Automatic private direct routing

Every retained wedge is active on at least one side.  Choose any active side.
The lower source occurrences are distinct, the chosen owner belongs to the
globally distinct owner bank, and the terminal belongs to the globally
distinct terminal bank.  The source, owner, and terminal layers are disjoint,
their physical capacities are assumed value-faithful, and each direct branch
has empty interior.  The resulting routes are therefore pairwise
vertex-disjoint without a suffix gammoid choice.

This conclusion is statewise: it relies essentially on the theorem's fixed
cap/guard/phase/occurrence state and completion-stability premise.

## 5. Directed active-side counts

If `e_i` is the number of directed active branches and `b_i` the number of
unordered pairs active in both orientations, then

\[
 |W_i^c|=e_i-b_i\ge\lceil e_i/2\rceil.
\]

Hence `e_i>2B_{p-1}(m)` is sufficient.  If `L_{0,i}` active owner
coordinates each have at least `L_{1,i}` direct typed partners, then
`e_i>=L_{0,i}L_{1,i}`, proving the product criterion.  With all `m` owner
coordinates active, the required fan is strictly below `2(p-1)` partners
per owner, as displayed.

These products cannot mix counts obtained in different cap states; the
theorem explicitly retains that restriction.

## 6. Sharp common-owner-star obstruction

For one owner `U` and lower turns `L_i=U-x_i`, activating only

\[
 L_i\longrightarrow U\longrightarrow U+b
 \qquad(b\notin U)
\]

gives exactly `m-1` active wedges at each source.  Every branch uses the same
unit owner `U`, so no two-source joint selection is possible.  At `p=2`,

\[
 B_1(m)=m-1,
\]

which proves sharpness of the strict menu inequality.  The associated
physical port bank has suffix rank one, so the factor-restricted Rado cut
detects rather than repairs the obstruction.

Conversely, large suffix-gammoid rank alone does not create direct terminal
partners.  With one private terminal per each of `m` ports there are at most
`m` active wedges, while

\[
 m\le B_{p-1}(m)
 \qquad(p\ge3, m\ge3).
\]

Thus the theorem correctly separates the new active-menu premise from all
previous gammoid marginal statements.

## 7. Scope

The result is an exact packing/routing theorem in one already materialized,
completion-stable state.  It does not establish that a Pascal child exposes
the menu threshold, that prospective branches survive completion, or that
topology, residence, regeneration, and transported-phase requirements hold.

The independent V1 verdict is **GO** at the hash listed above.
