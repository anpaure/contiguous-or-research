# Self-audit: finite Apéry shoulder critical-chain layer-cake reduction

**Date:** 2026-08-04
**Audited theorem:**
`MATH_THEOREM_APERY_FINITE_SHOULDER_CRITICAL_CHAIN_LAYER_CAKE_REDUCTION_20260804.md`
**Audited theorem SHA-256:**
`0e0df7a4d691bc6e73e0fba481fdeeceb43668f0fb8d1a69c02f7fc699cdc2e1`
**Method:** independent line-by-line algebraic replay.  No numerical search,
solver, or remote computation was used.

## 1. Verdict

**GO as an unconditional reduction.**

The theorem proves four exact statements:

1. the formal Apéry clock is a supersolution for every original Bellman
   edge, and the physical deficit obeys an exact min-plus recursion;
2. every critical denomination makes the deficits nonincreasing along its
   arithmetic chains;
3. the complete finite shoulder equals an exact integral of derivative
   prefix trains;
4. the net shoulder debt is the necessary and sufficient scalar for a
   positive formal clock to be overturned.

It does **not** prove that the debt is always smaller than the formal
margin.  Its abstract one-chain example correctly shows that no such sign
can follow from critical-chain monotonicity alone.

## 2. Setup and dependency replay

The theorem uses the established definitions

\[
 V_m=\max_j(c_j+V_{m-j}),
 \qquad
 W_m=m\lambda+\beta_{m\bmod g},
\]

where `d_j=c_j-j lambda<=0`, `beta` is the maximum reduced residue-walk
weight, and `g` is the gcd of the critical denominations.  The frozen
all-slot Apéry theorem supplies

\[
                         0\le V_m\le W_m,
 \qquad V_m=W_m\quad(m\ge n(n-1)).
\]

Therefore all discrepancy sums in the new theorem are literally finite.
No interchange of conditionally convergent series occurs.

The two branches defining `K` agree at `A`:

\[
 1-e^0-e^{-4A^2}=-e^{-4A^2}.
\]

Their derivatives also agree there and equal

\[
                         4Ae^{-4A^2}.
\]

Thus use of the fundamental theorem of calculus across `A` is valid.

## 3. Supersolution and min-plus recursion

Fix `m>=j` and put `r=m mod g`.  Concatenating an attaining walk to
`m-j mod g` with edge `j` gives

\[
 \beta_r\ge\beta_{(m-j)\bmod g}+d_j.
\]

Restoring the linear term gives exactly

\[
                         W_m-W_{m-j}-c_j\ge0.
\]

So the sign of `sigma_(m,j)` is correct.

Next,

\[
 \begin{aligned}
 V_m
 &=\max_j(c_j+W_{m-j}-\Delta_{m-j})\\
 &=W_m-\min_j(W_m-W_{m-j}-c_j+\Delta_{m-j}).
 \end{aligned}
\]

Subtracting from `W_m` gives precisely

\[
 \Delta_m=\min_j(\sigma_{m,j}+\Delta_{m-j}).
\]

The conversion from maximum to minimum and every sign were replayed.

## 4. Critical-chain replay

If `h` is critical, then `c_h=h lambda`.  Since `g` divides `h`,

\[
 W_{m+h}
 =(m+h)\lambda+\beta_{m\bmod g}
 =W_m+c_h.
\]

Hence `sigma_(m+h,h)=0`, and the `j=h` candidate in the exact min-plus
recursion gives

\[
                         \Delta_{m+h}\le\Delta_m.
\]

The decomposition `m=r+qh`, `0<=r<h`, is unique.  Along it,

\[
 W_{r+qh}=W_r+q c_h,
\]

and the deficits form a nonincreasing sequence which is eventually zero.
The physical gap identity

\[
 V_{r+(q+1)h}-V_{r+qh}
 =c_h+\delta_{r,q}-\delta_{r,q+1}
\]

therefore has the claimed lower bound `c_h`.

## 5. Layer-cake and sign audit

For every physical/formal pair, `0<=V=x-delta<=x`.  Thus

\[
 K(x-\delta)-K(x)
 =-\int_0^\delta K'(x-t)\,dt.
\]

Because `delta_(r,q)` is nonincreasing, at fixed height `t` the active
indices are exactly an initial segment.  Therefore

\[
 \sum_{q:\delta_{r,q}>t}K'(x_r+qL-t)
 =J_{L,N_r(t)}(x_r-t).
\]

Endpoint choices `>` versus `>=` affect only a measure-zero set of heights.
All nonzero deficit sets are finite, so the reordered formula is exact.

Writing `J=J_+-(-J)_+` gives

\[
 -\int J
 =\int(-J)_+-\int J_+,
\]

which verifies

\[
 \mathcal H=\mathfrak C_h-\mathfrak D_h,
 \qquad
 \mathfrak S_h=\mathfrak D_h-\mathfrak C_h=-\mathcal H.
\]

Hence

\[
 \Phi(V)=\Phi(W)-\mathfrak S_h.
\]

For `Phi(W)>0`, the equivalence

\[
 \Phi(V)\le0
 \iff
 \mathfrak S_h\ge\Phi(W)
\]

is exact, including the equality case.  The theorem correctly uses
`>=`, not a strict inequality.  Likewise, `J<=0` implies `H>=0`, so the
prefix-slope transport criterion has the correct orientation.

## 6. Sharpness and scope audit

For an abstract chain with `x>zeta`, let

\[
 \delta_0=x-\zeta,
 \qquad \delta_q=0\quad(q\ge1).
\]

This sequence is nonnegative, nonincreasing, and eventually zero.  It
also gives an expanded first physical gap.  Its shoulder contribution is

\[
 K(\zeta)-K(x)<0
\]

because `K` is strictly increasing to the right of its unique minimizer.
Thus the theorem is correct to reject a monotonicity-only proof.

The source explicitly states that this abstract profile is not claimed to
satisfy the full Bellman slack recursion.  Therefore it is a no-go for a
proof method, not a counterexample to Bellman positivity.

The final programme statement is also scoped correctly:

* positive formal one-defect branches still require the new scalar bound
  for their physical shoulders;
* endpoint-critical, delayed/overshooting carry, and multidefect formal
  branches are not closed;
* no OR-word upper bound follows from this theorem alone.

## 7. Frozen dependency hashes

| role | file | SHA-256 |
|---|---|---|
| physical Bellman/Apéry conductor | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| exact formal cyclic clock | `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md` | `324f040f5604767fc867c78806c8a7ab7524d6ed82cabe77bc3e2e0ea36121ba` |
| all-grid shoulder trichotomy | `MATH_THEOREM_ALL_GRID_MINIMAL_COUNTEREXAMPLE_APERY_DESCENT_TRICHOTOMY_20260804.md` | `8ed0ae35fe1a3bbd52824bca67240155868ed1e3a268b1f582aba944e081b4b2` |
| one-defect classification | `MATH_THEOREM_APERY_ONE_DEFECT_GAP_CLASSIFICATION_AND_AFFINE_EXCLUSION_20260804.md` | `9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e` |
| all-period long-wrap closure | `MATH_THEOREM_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_20260804.md` | `24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd` |

## 8. Final audit conclusion

The theorem is proof-safe and materially sharpens the finite-shoulder
gate.  It does not close that gate: the remaining mathematical task is to
use the exact cross-denomination slack recursion to prove

\[
 \mathfrak S_h(V\mid W)<\Phi(W)
\]

on the relevant positive formal branches, or to isolate a realizable
slack system where the reverse inequality holds.
