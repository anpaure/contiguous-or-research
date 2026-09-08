# Audit of the trapped-colour Hall normal form

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_UNION_RAINBOW_RETHREAD_TRAPPED_COLOUR_HALL_NORMAL_FORM_20260807.md`  
**Method:** exact cycle-incidence and repeat-surplus audit; no search  
**Verdict:** `GO`.

## 1. Incident-edge and trapped-colour identities

For `S subseteq V(K)`, the cycle degree sum gives

\[
 |N_K(S)|=2|S|-|E(K[S])|
 =|S|+\bigl(|S|-|E(K[S])|\bigr).
\]

This remains valid at `S=V(K)`, where the parenthetical term is zero.

If `n_a=|N_K(S) cap E_a|`, then

\[
 \min(\mu_a-1,n_a)=n_a-1_{\{n_a=\mu_a\}}.
\]

The colour classes partition the cycle edges, so summing gives exactly
`|N_K(S)|-tau_K(S)`.  Substitution into capacitated Hall yields (2.3)
without loss.

## 2. Complementary repeat-surplus form

Let `T=V(K)\S`.  The edges outside `N_K(S)` are precisely `E(K[T])`.
A colour is untrapped exactly when at least one of its occurrences lies in
that exterior induced edge set.  Therefore

\[
 \tau_K(S)=|\mathcal A|-|i(E(K[T]))|.
\]

Writing `R=|E(K)|-|A|`, the available capacity is

\[
 \begin{aligned}
 |N_K(S)|-\tau_K(S)
 &=|E(K)|-|E(K[T])|-|\mathcal A|+|i(E(K[T]))|\\
 &=R-\bigl(|E(K[T])|-|i(E(K[T]))|\bigr)\\
 &=R-\operatorname {rep}_K(T).
 \end{aligned}
\]

Hence capacity at least `|X|` is equivalent to

\[
 \operatorname {rep}_K(T(X))\le R-|X|.
\]

Corollary 2.4 is exact.  The formula counts repeated **occurrences** via
`|E|-|colours|`, not merely the number of repeated colour classes.

## 3. Singleton and protected scopes

For omitted `U`, its `m` facets form an independent set in `K`: an edge
between two would have union `U`, contradicting omission.  Thus its
incident bank has `2m` edges and singleton Hall fails exactly when all
`2m` incident occurrences belong to globally singleton, pairwise-distinct
intersection colours.  The hinge interpretation is correct.

For a protected deletion minor, occurrences removed from the deletion
ground set must be priced explicitly.  The source does so with

\[
 c_a=\min(\mu_a-1,|E_a\cap E'|),
\]

and the network cut (4.1).  It correctly declines to reuse the unrestricted
trapped-count formula in this case.

No construction claim is made, so no correction is required.

