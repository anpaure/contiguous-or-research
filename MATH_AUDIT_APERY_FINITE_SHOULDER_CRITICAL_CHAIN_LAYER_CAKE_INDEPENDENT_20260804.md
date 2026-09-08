# Independent audit: finite Apéry shoulder layer cake

**Date:** 2026-08-04  
**Source:**
`MATH_THEOREM_APERY_FINITE_SHOULDER_CRITICAL_CHAIN_LAYER_CAKE_REDUCTION_20260804.md`  
**Source SHA-256:**
`0e0df7a4d691bc6e73e0fba481fdeeceb43668f0fb8d1a69c02f7fc699cdc2e1`  
**Method:** independent symbolic replay; no search or numerical
enumeration.

## Verdict

**GO, with reduction-only scope.**  The exact min-plus deficit recurrence,
critical-chain monotonicity, and layer-cake identity all replay.  The result
does not show that the shoulder correction is nonnegative.  It proves
instead that the remaining obstruction is one exact debt-minus-credit
integral constrained by the full cross-denomination slack system.

## 1. Min-plus recurrence

For

\[
 W_m=m\lambda+\beta_{m\bmod g},\qquad
 \Delta_m=W_m-V_m,
\]

append denomination `j` to a reduced Apéry walk attaining the residue of
`m-j`.  Maximality of the Apéry weight gives

\[
 W_m\ge W_{m-j}+c_j,
\]

so every displayed slack

\[
 \sigma_{m,j}=W_m-W_{m-j}-c_j
\]

is nonnegative.  Substituting `V_(m-j)=W_(m-j)-Delta_(m-j)` into the
Bellman maximum yields exactly

\[
 \Delta_m=\min_j\{\sigma_{m,j}+\Delta_{m-j}\}.
\]

No inequality is lost in this step.

If `h` is critical, then `c_h=h lambda`, `g|h`, and hence
`W_(m+h)=W_m+h lambda`.  The `h`-edge slack is zero, so the recurrence gives

\[
 \Delta_{m+h}\le\Delta_m.
\]

Partitioning indices modulo `h` therefore gives exact formal arithmetic
chains `x_r+qL` and nonincreasing, eventually zero deficit chains
`delta_(r,q)`.  Eventual zero follows from the frozen Apéry conductor
identity `V_m=W_m` for all sufficiently large `m`.

## 2. Layer-cake replay

For one chain, the fundamental theorem of calculus gives

\[
 K(x_r+qL-\delta_{r,q})-K(x_r+qL)
 =-\int_0^{\delta_{r,q}}K'(x_r+qL-t)\,dt.
\]

The domain is valid because `V_(r+qh)>=0`, hence
`delta_(r,q)<=x_r+qL`.  Only finitely many deficits are nonzero, so the
sum-integral interchange is finite.  Monotonicity of each deficit chain
means that, at height `t`, the active indices are the initial segment
`q=0,...,N_r(t)-1`.  Thus the complete correction is

\[
 \mathcal H(V,W)
 =-\sum_{r=0}^{h-1}\int_0^{\delta_{r,0}}
   \sum_{q=0}^{N_r(t)-1}K'(x_r-t+qL)\,dt.
\]

This is exactly the source's derivative-prefix train
`J_(L,N_r(t))(x_r-t)` and proves the claimed layer-cake identity.

Splitting each integrand into positive and negative parts consequently
gives, without approximation,

\[
 \mathcal H=\mathfrak C_h-\mathfrak D_h,
 \qquad
 \mathfrak S_h:=\mathfrak D_h-\mathfrak C_h=-\mathcal H,
\]

and therefore

\[
 \Phi(V)=\Phi(W)-\mathfrak S_h.
\]

When `Phi(W)>0`, physical nonpositivity is equivalent to
`mathfrak S_h>=Phi(W)`.  If every active derivative prefix is nonpositive,
then `mathfrak D_h=0`, so `H>=0`; the source correctly labels this only as
a sufficient transport criterion.

## 3. Sharp logical limitation

The abstract one-chain profile with one positive deficit moving a formal
point `x>zeta` to the unique kernel minimizer `zeta` is nonnegative,
nonincreasing, and eventually zero, yet contributes

\[
 K(\zeta)-K(x)<0.
\]

Therefore `V<=W`, eventual equality, and critical-chain monotonicity alone
cannot force a favorable shoulder.  The source does not claim this profile
is Bellman-realizable; it uses it only to prove that a completion must
exploit the cross-denomination recurrence, which is logically correct.

## 4. Scope

The audit confirms the exact reduction

\[
 \Delta_m=\min_j(\sigma_{m,j}+\Delta_{m-j})
 \quad\Longrightarrow\quad
 \Phi(V)=\Phi(W)-\mathfrak S_h(V\mid W).
\]

It does not prove `mathfrak S_h<Phi(W)`, eliminate finite shoulders,
settle multidefect formal clocks, prove universal Bellman positivity, or
imply `nu(k)<=B(k)+O(1)`.
