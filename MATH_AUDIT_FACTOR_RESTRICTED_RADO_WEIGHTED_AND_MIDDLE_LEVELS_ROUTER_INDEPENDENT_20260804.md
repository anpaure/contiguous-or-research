# Independent audit: factor-restricted Rado and the Middle Levels router

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md`  
**Audited theorem SHA-256:**
`09acd8673956a2e43ec97d1d67ff01d4e3ceb1ea230af0e796a762b84d142906`  
**Verdict:** **PASS after two conservative scope clarifications.**  The
sink set in the corridor is now explicitly disjoint from the active port
set, and the bidirected copy is explicitly required to live in the
type-safe expanded network.  No computation or finite search was used.

**Formatting rebind.**  The earlier audit bytes had SHA-256
`1da4f4ac009b769acddd54560688ff081b876d55f88d9483147b682b8327c6bf`.
They contained one missing backslash in the audit's reproduction of
`h|H_B(U)|\le\sum_{p\in U}\deg_B(p)`.  The current audit restores that
single formatting character.  The audited theorem itself is unchanged at
SHA-256 `09acd8673956a2e43ec97d1d67ff01d4e3ceb1ea230af0e796a762b84d142906`;
no hypothesis, inequality, proof step, conclusion, or scope statement has
changed.

## 1. Literal architecture

For each claim `g`, the displayed architecture first chooses one port from
the menu `N_B(g)`, traverses its private prefix, and then uses the residual
suffix network.  The physical port gate has unit capacity, so chosen ports
are distinct.  A chosen port set is suffix-linkable exactly when it is
independent in the strict gammoid `Gamma`.

The privacy and type assumptions in Section 1 are sufficient for
concatenation: prefix interiors do not consume suffix resources, each
claim start has total capacity one, every port has one physical capacity
gate, and every suffix available from a port is legal for every incidence
using that port.

## 2. Exact Rado and deficiency formulas

Rado's theorem applied to the menu family gives, for `S subseteq G`,

\[
 S\text{ is fully routed}
 \iff
 r_\Gamma(N_B(X))\ge |X|
 \quad(X\subseteq S).
\]

The maximum number of represented claims is

\[
 \min_{X\subseteq S}
 \bigl(|S\setminus X|+r_\Gamma(N_B(X))\bigr).
\]

For `S=G`, subtraction from `|G|` gives exactly

\[
 \delta_B=\max_{X\subseteq G}
 \bigl(|X|-r_\Gamma(N_B(X))\bigr).
\]

Thus the theorem's deficiency is exact for the displayed architecture, not
merely sufficient.

## 3. Trapped-menu form

For

\[
 H_B(U)=\{g:N_B(g)\subseteq U\},
\]

Rado implies

\[
 |H_B(U)|\le r_\Gamma(N_B(H_B(U)))\le r_\Gamma(U).
\]

Conversely, taking `U=N_B(X)` gives

\[
 X\subseteq H_B(U),qquad
 |X|\le |H_B(U)|\le r_\Gamma(U).
\]

This proves the claimed equivalence.

In the node-split suffix network, define `U_C` to include every port whose
every route to the typed sink bank meets cut `C`, including a port whose
own capacity gate is in `C`.  Then

\[
 r_\Gamma(U_C)\le\operatorname{cap}(C).
\]

For the converse, a minimum `U`-to-sink cut has capacity
`r_\Gamma(U)` and satisfies `U\subseteq U_C`.  Hence the all-cut condition

\[
 |H_B(U_C)|\le\operatorname{cap}(C)
\]

is exactly equivalent to the trapped-menu rank inequalities.  The
definition including cut port gates is essential and is present in the
frozen theorem.

## 4. Fractional incidence interface and integrality

If all claims are integrally linked, their chosen incidences give weights
`x_gp` satisfying the theorem's equations.  Conversely, if

\[
 d_p=\sum_gx_{gp},qquad d(U)\le r_\Gamma(U),
\]

then `d` lies in the strict-gammoid independence polytope.  Expressing it
as a convex combination of independent port sets and averaging one suffix
linkage for each set gives a feasible fractional suffix flow with injection
`d`.  The private prefix flows have exactly the same port totals.

After adjoining one unit super-source arc to each claim start, the combined
physical network has integral capacities.  A value-`|G|` integral max flow
therefore saturates every claim arc and yields one disjoint legal path per
claim.  This proves that Theorem 3.1 is equivalent to Rado, not a weaker
fractional relaxation.

## 5. Degree-weighted and scaled-flow certificate

For a left-`h`-regular/right-at-most-`h` factor, the uniform choice

\[
 x_{gp}=1/h,qquad d_p=\deg_B(p)/h
\]

satisfies

\[
 d_p\le1,qquad d(P)=|G|.
\]

Thus `d(U)\le r_\Gamma(U)` is sufficient by Theorem 3.1.  The direct
trapped-menu calculation is also exact:

\[
 h|H_B(U)|\le\sum_{p\in U}\deg_B(p)=h d(U).
\]

Multiplying every suffix node, port, and sink capacity by `h`, and giving
port `p` integer supply `deg_B(p)`, converts the same condition into one
ordinary max-flow request of value

\[
 \sum_p\deg_B(p)=h|G|.
\]

Division by `h` recovers the fractional injection vector; multiplication
gives the converse.  The claimed scaled max-flow equivalence and cut
directions are correct.

The port-fan corollary follows because

\[
 d(U)\le |U|,qquad d(U)\le d(P)=q=|G|.
\]

Hence rank at least `min(|U|,q)` suffices even if the full port set is
dependent.

## 6. Vertex connectivity of `ML_m`

The graph between ranks `m-1` and `m` of `[2m-1]` is `m`-regular and has
equal shore size

\[
 W={2m-1\choose m}.
\]

The cited middle-shadow theorem gives

\[
 |N(A)|-|A|\ge\min(m-1,W-|A|)
\]

on either shore.  If a set `S=S_L\mathbin{\dot\cup}S_U`, `|S|\le m-1`, disconnected
the graph, every residual component would meet both shores because every
remaining vertex retains a neighbour.  For one component with shores
`A,C`, another component forces

\[
 W-|A|\ge |S_L|+1,qquad W-|C|\ge |S_U|+1.
\]

Applying the shadow inequality on both shores and adding gives

\[
 |S|\ge
 \min(m-1,W-|A|)+\min(m-1,W-|C|)>|S|,
\]

a contradiction.  The endpoint case in which one of `|S_L|,|S_U|`
equals `m-1` is handled because the other minimum contributes at least
one.  Hence connectivity is at least `m`; deleting all `m` neighbours of
one vertex proves equality.

## 7. Deletion and the corridor fan

Deleting `f<m` vertices from an `m`-connected graph leaves connectivity at
least `m-f`: any further deletion of fewer than `m-f` vertices would be a
deletion of fewer than `m` vertices in the original graph.

In a bidirected `q`-connected graph, disjoint sets `U,T` with `|T|>=q`
have at least `min(|U|,q)` vertex-disjoint `U`-to-`T` paths.  Otherwise a
set-Menger separator of smaller size would leave at least one vertex of
each of `U,T` while deleting fewer than `q` vertices, contradicting
connectivity.

Therefore, after deleting `F`, the inequality

\[
 q+|F|\le m
\]

makes `ML_m-F` at least `q`-connected and supplies the port-fan rank
condition.  The frozen theorem now explicitly requires:

* a capacity-faithful bidirected copy in the type-safe expanded network;
* active ports represented by distinct physical port gates;
* at least `q` distinct legal sink vertices, disjoint from the ports;
* every directed path in the copy to be a legal typed suffix for its
  starting port.

Under exactly those hypotheses, Corollary 5.3 follows.

## 8. Scope verdict

The result does **not** prove that the current parent chronology supplies
the corridor.  The small protected-factor theorem supplies only an
abstract incidence factor, not a capacity-faithful port map, private
literal prefixes, or the typed suffix copy.  In two occurrence coordinates,
separate corridor proofs are insufficient unless both are embedded in one
complete cap state with all shared resources allocated and product closure
proved.

The theorem therefore weakens the router target exactly as claimed, but it
does not prove `nu(k)<=B(k)+O(1)` or `nu(k)=B(k)`.

**Final independent verdict: PASS.**
