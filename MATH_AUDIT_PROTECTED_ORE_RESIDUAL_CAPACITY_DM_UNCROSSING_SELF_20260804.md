# Self-audit: protected Ore residual-capacity DM uncrossing

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md`

This audit is purely deductive and uses no search or computation.

## 1. Hall-surplus algebra

At one owner write `e=e_P(U,A)` and
`p=e_P(U,L-A)`.  The residual owner cap and residual incidence count are

\[
 c=2-e-p,
 \qquad d=a-e.
\]

Adding `e` to both arguments of a minimum gives

\[
 \min(c,d)+e=\min(2-p,a).
\]

After summation, `sum e` cancels the protected part of the lower demand
`2|A|-sum e`.  The result is exactly the frozen local expression for
`sigma-lambda`.  This verifies equation (1.1) owner by owner.

The lower residual demands and owner residual capacities have the same
total:

\[
 \sum_x(2-d_P(x))=2|\mathcal L|-|E(P)|
 =\sum_U(2-d_P(U)).
\]

Thus saturation of every lower demand is equivalent to saturation of
every owner capacity, and the max-flow deficiency is exactly (1.2).

## 2. Submodularity and lattice direction

For a fixed owner, `d_A(U)` is modular and `min(c_U,t)` is concave and
nondecreasing, so its composition is submodular.  Therefore `kappa-r` is
submodular and `r-kappa` is supermodular.  The inequality direction in
(2.1) is consequently correct.

For two minimizers, submodularity puts the sum of the intersection and
union values below twice the minimum.  Each term is individually at least
the minimum, so both are minimizers.  Hence maximum-deficiency shores form
a lattice, with the displayed unique intersection and union extremes.

## 3. Flow-cut projection

For a cut with source-side lower set `A`:

* omitted lower vertices cost `R-r(A)` through source arcs;
* placing owner `U` on the sink side costs `d_A(U)`;
* placing it on the source side costs `c_U`.

Owner choices are independent, producing `min(c_U,d_A(U))`.  This verifies
the cut capacity `R+mu(A)`.

In the residual graph of a maximum flow, every minimum-cut source side is
closed under outgoing residual arcs.  The reachable set from `s` is the
smallest such source side, while the complement of the set that can reach
`t` is the largest.  Both are themselves closed `s`--`t` cuts and hence
minimum.  Their lower projections therefore agree with the lattice
extremes.  This also proves independence from the chosen maximum flow.

## 4. Local marginal signs

When `x in A` is removed, an owner cap drops by one exactly if
`d_A(U)<=c_U`; when `y notin A` is added, it rises exactly if
`d_A(U)<c_U`.  Subtracting or adding the corresponding lower demand gives
(4.3)--(4.4).

Every proper subset of the unique minimal minimizer has strictly larger
`mu`, yielding (4.8); every proper superset of the unique maximal minimizer
does likewise, yielding (4.9).  Their singleton cases give (4.5) and
(4.7).  If `r_x=0`, (4.5) would read `e(x)<=-1`, so no protected-degree-two
lower vertex belongs to `A^-`.

## 5. Constant-spread density ledger

Fix `x in A^-`.  It has `m-d_P(x)` residual owner neighbours.  Among
them:

* protected-degree-two owners are counted exactly by the singleton loss,
  so there are at most ten;
* protected-degree-one owners whose protected incidence is not `Ux` are
  endpoint exposures, at most ten outside the top bank plus
  `t_top(x)` inside it.

Therefore

\[
 \sum_{U:xU\in G_P}c_U
 \ge2(m-d_P(x))-30-t_{\rm top}(x).
\]

At most `r_x-1=1-d_P(x)` owner rows are not overloaded, and discarding one
such row loses at most two neighbour units.  The result is

\[
 2(m-d_P(x))-30-t_{\rm top}(x)-2(1-d_P(x))
 =2m-32-t_{\rm top}(x).
\]

At an overloaded residual owner, after counting `x` itself there are at
least `c_U` other selected residual facets.  Each is a Johnson neighbour,
and different owners give different neighbours because two adjacent lower
sets have a unique union owner.  Thus no double counting occurs.

Each of the `2m` deterministic top endpoints contributes to
`t_top(x)` for at most its other `m-1` lower facets.  Hence the total
exception budget is at most `2m(m-1)`, proving (5.3)--(5.5).

## 6. Co-small incidence-lift reduction

For an incidence lift of owner paths, every protected lower vertex has
degree two.  The minimal-shore exclusion (4.6) therefore places the entire
protected lower bank `Z_P` in `C=L-A^-`.  Consequently every protected
edge points into `C`, so

\[
 D_P(C)=|E(P)|,
 \qquad p_U=d_P(U),
 \qquad \operatorname{def}_P(C)=2|C|-|E(P)|.
\]

At a full complement clique, `theta-R` is `2-d_P(U)`; at an almost-full
clique it is one precisely when the owner is unprotected.  These are
exactly the two terms of `Omega_P(C)`.  Substitution in the frozen
co-small identity proves (6.4) in both directions.  Also
`2|Z_P|=|E(P)|`, giving (6.5).

For `C=Z_P dotcup B`, an owner is full exactly when the optional occupancy
fills its forced gap, and almost full exactly when it leaves one gap:

\[
 d_C(U)=m\iff b_U=g_U,
 \qquad
 d_C(U)=m-1\iff b_U=g_U-1.
\]

Substitution gives (6.9), while
`2|C|-|E(P)|=2|B|` gives the exact failure threshold (6.10).

## 7. Exchange identity and scope

Equation (7.1) is the sum of one removal marginal and one addition
marginal at the intermediate set.  A maximum-deficiency shore minimizes
`mu`, so this value is nonnegative and is zero exactly when the exchange
stays in the minimizer lattice.

The forced-element correction is essential.  Every member of `A^-`
belongs to every minimizer, so an exchange deleting such a member can
never preserve the minimum.  This rules out a naive bubble-sort argument
starting at `A^-`.

For the corrected global criterion, contract residual strongly connected
components.  A minimum-cut source side is exactly a successor-closed set
of components containing the source component and excluding the sink
component.  Adding one implication arc from each lower vertex to every
elementary downward shift enforces shiftedness of the lower projection.
Therefore a shifted minimizer exists exactly when the augmented successor
closure of the source omits the sink.  This proves both directions of
(7.3), and that closure is visibly the unique minimal shifted source side.

The theorem correctly does not infer colex from shiftedness.  Even a
shifted capacity-closed shore still needs a separate extremal
classification to reach initial colex.  This is consistent with the
frozen warning that capped-shadow shifted minimizers need not already be
colex.

## 8. Mechanical checks

At freeze time, display-math delimiter balance is zero, no hidden control
byte is present, and `git diff --check` reports no whitespace errors.
