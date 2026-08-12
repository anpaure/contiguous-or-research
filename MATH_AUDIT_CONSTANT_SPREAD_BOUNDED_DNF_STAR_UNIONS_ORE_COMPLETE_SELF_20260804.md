# Self-audit: bounded monotone DNF unions of principal stars

**Date:** 2026-08-04  
**Verdict:** author self-audit **GO**, pending independent review.  No
computation, search, or solver result is used.

Audited theorem:
`MATH_THEOREM_CONSTANT_SPREAD_BOUNDED_DNF_STAR_UNIONS_ORE_COMPLETE_20260804.md`,
Original audited SHA-256
`602b2f952c79de04aac9f18881b7cd82317af1fd7a9d3c3779aa59c4650f6905`.
The independently patched theorem has SHA-256
`26dd7101b25bd4b1ddc6bd8daace1620cfb5805b0e58828b5180d1b70967e1e2`;
the patches make the implicit margin notation and `d=O(sqrt(m))` premise
explicit and sharpen scope wording, without changing the proof.

## 1. Local fibre and current

At an owner `U`, a clause `C_i` accepts deletion `x` exactly when
`C_i subseteq U` and `x notin C_i`.  The union of accepted deletion sets
is `U minus J_U`, where `J_U` is the intersection of active cores.  Thus
`a_U=m-|J_U|`, and protected loss is exactly the number of protected
deletions in `J_U`.  Since `J_U` lies in every active core, union loss is
at most the sum of individual star losses.  The exact cancellation sum is
restricted to owners with a nonempty active-clause set; otherwise the
indicator `h_U(x)=|I(U)|` would read `0=0` and be spurious.

## 2. Slack inclusion--exclusion

Every active owner fibre has size at least two, so
`sigma/2=|N(A)|-|A|`.  Intersections of lower and upper principal stars
have the union of their cores.  Inclusion--exclusion gives (2.4).

For `1<=q<=m-2`, direct division gives

\[
 {\delta_{q+1}\over\delta_q}
 ={(m-q)(q+1)\over q(2m-q-1)}\le1.
\]

The endpoint `delta_m=1<=delta_(m-1)=m-1` completes monotonicity.

## 3. High-core regime

After redundant nested clauses are deleted, the cores form an antichain.
Assign every negative even inclusion--exclusion term to one participating
core.  Its union strictly enlarges that core, so its value is at most
`delta_(c_i+1)<=2rho_i delta_i/m`.  Each core receives at most
`2^(h-1)` terms.  When all `rho_i/m<=alpha_h`, the definition of
`alpha_h` makes the total even tax at most half of the singleton sum.
Therefore `sigma>=sum_i delta_i`.

Since every `delta_i/A_i=c_i/rho_i>=16`, one gets
`sigma>=16|A|`.  The antichain has at least two stars and their union has
at least `2m+1` members, so the global `15|A|+2m` loss bound closes the cut.

## 4. Entropic regime

Avoid one chosen coordinate from each nonempty core.  This leaves at least
`binom(2m-1-h,m-1)` lower vertices outside the DNF, a fraction at least
`3^(-h)` under (3.1) and for large `m`.  The Johnson spectral inequality
then gives `sigma>=4*3^(-h)|A|/m`.

Choose a core with maximal `rho_*`.  The DNF contains its star of size
`A_*`, and every individual path count is at most `N_(rho_*)`.  For
`alpha=rho_*/m`, the exact entropy gap has second derivative bounded below
and is at least `alpha^2/ln 2`.  Hence

\[
 \log_2(A_*/N_*)\ge\kappa m/4^h-O(\log m).
\]

Condition `4^h(h+log m)=o(m)` makes this dominate the factors
`hm3^h`.  It also ensures `rho_*>=d`, so the high-tail term is already
contained in `H_(rho_*)(m)`.

## 5. Lipschitz tail check

For `h` singleton cores, the DNF complement is the complete lower layer
on `2m-1-h` coordinates.  Subtracting the analogous upper complement
gives `sigma=2h binom(2m-1-h,m-1)/m`.  The next singleton clause has the
exact size in (4.5).  Even the impossible best case `margin=sigma` gives
Lipschitz radius smaller than that next term by `Theta(m^2/h)`.  Therefore
geometric term decay does not justify a head-plus-Hamming-tail proof.

## 6. Scope

The proof is uniform over the core geometry and ranks through every width
with `4^h(h+log m)=o(m)`, including
`h<=(1/2-epsilon)log_2 m`.  It does not prove larger-width DNFs, general
Macaulay families with unbounded generator count, global component
placement, or the common cap.
