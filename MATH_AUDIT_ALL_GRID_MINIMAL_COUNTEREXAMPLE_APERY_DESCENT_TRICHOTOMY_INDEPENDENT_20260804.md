# Independent audit: all-grid minimal-counterexample Apéry descent trichotomy

**Date:** 2026-08-04  
**Verdict:** **PASS after a citation-scope clarification.**  Exact
domination, uniform stabilization, finite correction localization, the
quantitative adverse-shoulder bound, and the three-way minimal-counterexample
split all replay.  The theorem is a reduction only; it does not sign any of
the three remaining branches.

## 1. Audited bytes

| role | file | SHA-256 |
|---|---|---|
| audited theorem, clarified current bytes | `MATH_THEOREM_ALL_GRID_MINIMAL_COUNTEREXAMPLE_APERY_DESCENT_TRICHOTOMY_20260804.md` | `8ed0ae35fe1a3bbd52824bca67240155868ed1e3a268b1f582aba944e081b4b2` |
| first-crossing, saturation, and conductor theorem | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| cyclic Apéry exact-clock theorem | `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md` | `324f040f5604767fc867c78806c8a7ab7524d6ed82cabe77bc3e2e0ea36121ba` |
| least-critical endpoint theorem | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complete positivity through grid five | `MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| affine no-descent witness | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |

The supplied pre-audit theorem hash was
`884a0b2258a4352d11955bb1cd62d5aba8da72044bf1a21b0b7507b6ab6e198c`.
The only change makes explicit that the formal period `g` need not be an
original denomination and proves that the cyclic exact-clock argument
still applies.  It also records why the strict-descent prefix necessarily
contains every formal Apéry generator.  No assertion changed.

## 2. Exact domination and stabilization

Let `r=m mod g`.  For any exact fill of capacity `m`, subtracting
`lambda m` from its value leaves the sum of reduced edge weights.
Critical denominations are zero-weight loops modulo `g`; deleting them
leaves a residue walk from zero to `r`.  Its weight is at most `beta_r`.
Therefore

\[
 V_m\le \lambda m+\beta_r=qP+s_r=W_m.
\]

This argument does not require `g` itself to lie in the critical set.  The
formal size-`g` generator of value `P=g lambda` is legitimate because
concatenation of residue walks proves the carry and noncarry cyclic
superadditivity inequalities for the `s_r`; the resulting formal table has
exact clock `W_(qg+r)=qP+s_r`.

The all-slot Apéry theorem gives

\[
 V_m=\lambda m+\beta_{m\bmod g}
 \qquad(m\ge n(n-1)).
\]

Since the right side is `W_m`, equality holds for every `m>=T` with
`T=n(n-1)`.  Absolute convergence of both positive-period Gaussian tails
then permits termwise subtraction, leaving precisely the finite head

\[
 \mathcal H(V,W)=\sum_{m<T}(K(V_m)-K(W_m)).
\]

## 3. Kernel shoulder and quantitative correction

For `0<t<1`, differentiation gives

\[
 {K'(At)\over2A}
 =h_0(1+t)-h_0(1-t),
 \qquad h_0(u)=u e^{-\pi u^2/4}.
\]

Its sign is the sign of
`2 arctanh(t)-pi t`, the negative of
`f(t)=pi t-2 arctanh(t)`.  Here `f(0)=0`, `f'(0)=pi-2>0`,

\[
 f''(t)=-{4t\over(1-t^2)^2}<0,
\]

and `f(t)->-infinity` as `t->1`.  Strict concavity gives one positive
zero, hence one compact minimum `zeta`.  The tail derivative is positive,
so this is the global minimum.  Since `K(A)=-e^{-pi}<0` and `K` rises from
`zeta` to `A` and then to zero from below, `K(x)<0` for every `x>zeta`.

If `W_m<=zeta`, domination `0<=V_m<=W_m` and decrease of `K` imply

\[
 K(V_m)-K(W_m)\ge0.
\]

Thus only the finite set
`D={m<T:W_m>zeta}` can contribute adversely.  On that set,

\[
 K(V_m)-K(W_m)\ge K(\zeta)-K(W_m)\ge K(\zeta),
\]

which proves

\[
 \mathcal H(V,W)\ge |D|K(\zeta).
\]

When `Phi(W)>0>=Phi(V)`, one also has
`H=Phi(V)-Phi(W)<=-Phi(W)`.  Since `K(zeta)<0`, combining the two bounds
and reversing the sign correctly gives

\[
 |D|\ge {\Phi(W)\over-K(\zeta)}.
\]

## 4. Exhaustive minimal-counterexample split

After first-crossing normalization and endpoint saturation, choose a
nonpositive table of minimum grid `n`.  Positivity through grid five gives
`n>=6`.

### Endpoint-critical case

If the least maximum-density index is `h=n`, every lower density is
strictly smaller.  The least-critical endpoint theorem therefore forces
the saturated endpoint to be exactly `c_n=A`.  This is branch A.

### Lower-critical cases

If `h<n`, then `g<=h` and

\[
 P=g\lambda\le h\lambda=c_h<A.
\]

Internal superadditivity gives `V_n=c_n>=A`; domination then gives
`W_n>=A`, so the first crossing `N` of `W` satisfies `N<=n`.
Furthermore `s_r<P<A` for `0<r<g` and `W_g=P<A`, hence `N>g`.  The
prefix through `N` therefore contains the complete formal Apéry table.
Because `W` is superadditive, adjoining denominations of value `W_j`
cannot improve its clock, so this prefix still has exact Bellman clock
`W`.

- If `N<n`, a nonpositive `Phi(W)` would be a smaller first-crossing
  counterexample, contrary to minimality.  Hence `Phi(W)>0`; any original
  nonpositivity must come from the explicit finite shoulder correction.
  This is branch B.
- If `N=n`, the inequalities `W_m<A` for `m<n` and `W_n>=A` are exactly
  the displayed quotient-residue carry system.  Re-extending the smaller
  subthreshold period table returns grid `n`, so there is no grid descent.
  This is branch C.

The alternatives `h=n`, `h<n,N<n`, and `h<n,N=n` are mutually exclusive
and exhaustive because `N<=n`.  Thus the claimed trichotomy is complete.

## 5. Scope boundary

The theorem proves neither endpoint-threshold positivity, periodic carry
positivity, nor domination of the finite negative shoulder by the smaller
clock margin.  It supplies an exact induction architecture and a finite
quantitative obstruction.  In particular it does not prove universal
Bellman positivity and has no direct implication for the independent
common-cap/router or OR-word construction.

