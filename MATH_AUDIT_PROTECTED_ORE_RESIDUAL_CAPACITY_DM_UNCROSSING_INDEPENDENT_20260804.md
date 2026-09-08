# Independent audit: protected Ore residual-capacity DM uncrossing

**Date:** 2026-08-04  
**Verdict:** **GO**.  No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md`,
SHA-256
`487379349fbdebbe282650f36b17fed8ff64b1ae069cbdc55948b557906d268d`.

Author self-audit:
`MATH_AUDIT_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_SELF_20260804.md`,
SHA-256
`d079f58536c16f8f3d86b91110d8d86bb38f44a12f300b84e775825dea2da9f3`.

## 1. Exact Hall-surplus identity

At an owner, let `e=e_P(U,A)` and `p=e_P(U,L-A)`.  Then

\[
 c_U=2-e-p,
 \qquad
 d_A(U)=a_U-e,
\]

so

\[
 \min(c_U,d_A(U))+e=\min(2-p,a_U).
\]

Summing and using

\[
 r(A)=2|A|-\sum_Ue_P(U,A)
\]

gives exactly the frozen ownerwise expression for
`sigma(A)-lambda_P(A)`.  Hence

\[
 \mu_P(A)=\kappa_P(A)-r(A).
\]

The total lower demand and owner capacity both equal
`2|L|-|E(P)|`.  Capacitated bipartite Hall/max-flow therefore identifies
`max_A(r(A)-kappa_P(A))` with the exact unsent residual demand.  Since the
empty shore has deficiency zero, extension is equivalent to `delta(P)=0`.

## 2. Submodularity, min-cut projection, and DM extremes

For each owner, `d_A(U)` is modular and `min(c_U,d_A(U))` is the composition
of that modular count with a nondecreasing concave function.  It is
submodular.  Thus `mu=kappa-r` is submodular and its minimizers are closed
under intersection and union.  When the minimum is negative, neither the
empty nor full lower shore is a minimizer, so the two lattice extremes are
nonempty and proper.

For a network cut whose source-side lower shore is `A`, excluded source arcs
cost `R-r(A)`.  Each owner independently costs either `d_A(U)` on the sink
side or `c_U` on the source side.  Its optimized cost is therefore

\[
 R-r(A)+\kappa_P(A)=R+\mu_P(A).
\]

This proves both directions of the projection statement: every shore has an
owner placement attaining that value, and a global minimum cut must use an
optimal owner placement for its projected shore.

For any maximum flow, the vertices reachable from `s` form the least
residual-closed minimum-cut source side.  The complement of the vertices
which can reach `t` is the greatest one.  Their lower projections are the
intersection and union of all projected minimum shores, respectively, and
therefore equal `A^-` and `A^+`.  This also proves independence from the
chosen maximum flow.  The listed forward-unused/backward-used traversal is
exactly residual reachability.

## 3. Strict removal and addition blocks

Removing `x` lowers the capped supply at precisely those residual owner rows
with `d_A(U)<=c_U`, while adding `y` raises it precisely at rows with
`d_A(U)<c_U`.  This gives the two one-vertex marginal identities with their
stated signs.

Because `A^-` is the unique inclusion-minimal global minimizer, deleting any
nonempty `B subseteq A^-` strictly raises `mu`.  Expanding this strict
inequality gives (4.8).  Its singleton case is

\[
 e_{A^-}(x)<r_x,
\]

and integrality yields `e_{A^-}(x)<=r_x-1`.  Consequently a vertex with
`r_x=0`, equivalently protected degree two, cannot lie in `A^-`.

The dual argument for the unique maximal minimizer makes every nonempty
addition strict and gives (4.9) and
`u_{A^+}(y)>=r_y+1`.  No non-strict minimizer is lost in either direction.

## 4. Constant-spread Johnson-density ledger

Fix `x in A^-`.  It has `m-d_P(x)` residual owner neighbours.  Starting
with capacity two per such row:

* at most ten residual rows have protected owner degree two, since every
  such row is counted by the singleton loss of `x`; these cost at most
  twenty capacity units;
* at most ten private/high endpoint rows have protected degree one and their
  protected edge different from `Ux`; these cost at most ten units; and
* the deterministic top endpoint rows contribute exactly the remaining
  correction `t_top(x)`.

Hence

\[
 \sum_{U:xU\in G_P}c_U
 \ge2(m-d_P(x))-30-t_{\rm top}(x).
\]

Irreducibility says at most

\[
 r_x-1=1-d_P(x)
\]

of these rows are not overloaded.  Discarding each at worst capacity two
leaves

\[
 2(m-d_P(x))-30-t_{\rm top}(x)-2(1-d_P(x))
 =2m-32-t_{\rm top}(x).
\]

At an overloaded row, after `x` itself there are at least `c_U` other
selected residual facets.  They are Johnson neighbours of `x`; different
owners over `x` yield disjoint neighbour sets because a Johnson-adjacent
pair has a unique union owner.  Thus the capacity sum is a genuine Johnson
degree lower bound, not a count with multiplicity.

Each of the `2m` deterministic top endpoint owners contributes to
`t_top(x)` for at most its other `m-1` lower facets.  Therefore

\[
 \sum_xt_{\rm top}(x)\le2m(m-1),
\]

and at most that many vertices have positive top correction.  Equations
(5.4)--(5.5) follow.

## 5. Exchange identity and scope

The protected exchange formula is exactly the removal marginal at `A`
plus the addition marginal at `A-{x}`.  A maximum-deficiency shore globally
minimizes `mu`, so the exchange value is nonnegative and vanishes exactly
when the exchanged shore remains in the minimizer lattice.

The theorem correctly stops there.  Aggregate endpoint bounds do not fix
the sign of a prescribed coordinate compression, and even a sequence of
zero exchanges would establish shiftedness rather than initial-colex form.
The separate compression-transfer and shifted-extremizer classification
rows remain open.

The independent verdict is **GO** at the hashes listed above.
