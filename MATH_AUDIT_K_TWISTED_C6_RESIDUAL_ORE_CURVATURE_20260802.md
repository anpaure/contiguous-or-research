# Independent audit: twisted-`C6` residual Ore curvature

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K_TWISTED_C6_RESIDUAL_ORE_CURVATURE_AND_POLYNOMIAL_CORE_20260802.md`  
**Verdict:** PASS.  The explicit arithmetic conditions imply a complete
residual owner/lower-`q1` factor theorem; the finite replay remains only a
calibration of the literal pump.

## 1. Independent cut derivation

Let `F,O` be the two deleted pump shores, let

\[
 S\subseteq L-F,
 \quad T=(L-F)\setminus S,
 \quad A=F\dot\cup T,
\]

and put `j_A(Y)=|N(Y) cap A|`.  Since every right vertex has full degree
`m`, its degree from `S` before deleting protected edges is `m-j_A(Y)`.
Thus the missing capacity-two amount is exactly

\[
 c_A(Y)=(j_A(Y)-m+2)_+.
\]

If `q_T(Y)` protected edges go from `T` to `Y`, direct cancellation of the
protected edges from `S` gives the complementary Ore term

\[
 q_T(Y)+(c_A(Y)-q_T(Y))_+
 =c_A(Y)+(q_T(Y)-c_A(Y))_+.
\]

Summing proves independently that the cut is feasible exactly when

\[
 \kappa(A)+\rho_O(A)\ge2|F|+\omega_Q(A).
\]

This also checks the signs: the protected bank contributes nonnegative
**waste**, not a credit.

## 2. Degree/codegree algebra

For `s=|S|`, residual minimum degree `m-1` and same-shore codegree one give

\[
 u\ge{(m-1)^2s\over m+s-2}
\]

reached right vertices.  Substitution in

\[
 \min(2,j)\ge1+{j-1\over m-1}
\]

reproduces

\[
 {\cal M}_P(S)\ge{s((m-2)^2-s)\over m+s-2}.
\]

After subtracting `m-3`, the cleared numerator factors as

\[
 (s-1)((m-2)(m-3)-s).
\]

For the complementary calculation, a zero-`S` right vertex contributes at
least `C(m-1,2)` pairs of `T`, and a one-`S` vertex at least
`C(m-2,2)`.  Same-shore codegree one then gives

\[
 2a+b\le{2t(t-1)\over(m-1)(m-2)},
\]

which is the theorem's second local bound.

Finally, the central incidence singular values are `m,m-1`.  Tanner's
formula simplifies to

\[
 g(S)\ge
 { (2m-1)|S|(N-|S|)
   \over (2m-1)|S|+(m-1)^2N},
\]

and the denominator is at most `m^2N`; this verifies the localization
constant in the theorem.

## 3. Independent audit of the localized-core closure

There are only two cases after spectral localization.

1. If `s=|S|` is the smaller full shore, complementing `S` gives a rank-`m`
   family of size `s`.  Under `s<=C(m+2,3)<C(m+3,m)`, the real-binomial
   parameter is below `m+3`, so Lovasz--Kruskal--Katona gives upper-shadow
   ratio at least `m/4`.  Substitution into the truncated-degree inequality
   gives the full coefficient `m(m+2)/[4(m-1)]`.  External cross-degree one
   deletes at most `s`, and subtracting the left demand `2s` leaves exactly

   \[
      a_m={m^2-10m+12\over4(m-1)}.
   \]

2. If `a=N-s=|A|` is the smaller shore, let `u` count complete owner stars
   in `A`.  The inverse shadow inequality gives `u<=3a/m`.  If `v` counts
   stars missing one facet, incidence counting gives
   `m u+(m-1)v<=ma`.  Therefore

   \[
    2a-(2u+v)\ge
    {(m-2)(m-3)\over m(m-1)}a=c_ma.
   \]

These are precisely the two coefficients in (0.15)--(0.16).  Since a
minimal protected obstruction has margin below `q`, the two estimates
contradict it.  No probabilistic rounding or integral-gap assumption is
used after Ore--Ryser.

The zero-complete-star branch is included separately: when `u=0`, the
bound `u<=3a/m` is immediate and no real-binomial parameter for zero is
invoked.  The small-`S` margin is asserted only for nonempty `S`; the empty
Ore cut is tautological.

## 4. Literal finite replay

The independent standard-library C++ replay is

```text
scratch/audit_k_pump_residual_ore_small_20260802.cpp
```

It performs two checks.

1. For every `1<=d<=8` and slack `s in {0,1,3}` representable in 64 bits,
   it reconstructs the literal developed pump, enumerates every incident
   owner/facet, removes the pump shores, and verifies maximum external
   cross-degree one on both sides.
2. At the smallest admissible instance `d=1,m=7,n=13`, it independently
   builds the full residual containment graph and runs an integral
   capacity-two max flow.  The output is

```text
PASS_EXTERNAL_CROSS_DEGREE d=1..8 slack=0,1,3
C=1 residual_conditions_hold_after_m=2821 (audited_through_200000)
C=2 residual_conditions_hold_after_m=10933 (audited_through_200000)
n=13 r=7 residual=1677 flow=3354/3354 max_deleted_neighbors=1,1 mincut_reachable=0,0
PASS_SMALL_RESIDUAL_TWO_FACTOR
```

The two arithmetic rows independently evaluate (0.14)--(0.16) with
`d=floor(C sqrt(m))`; they are finite stress checks, not the asymptotic
proof.  The finite flow is calibration only.  It is not used as an all-`m`
proof and does not include the opened seven-ear protected bank.

## 5. Scope confirmation

The theorem does claim that the anchored polynomial core is empty under
its explicit inequalities, and hence for `q=52d+62`, `d=O(sqrt(m))`, at all
sufficiently large `m`.  It makes no ternary-partner, history, topology,
upper-shadow, source, or compiler claim.
