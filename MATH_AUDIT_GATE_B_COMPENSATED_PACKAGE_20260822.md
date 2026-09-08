# Hostile audit of the compensated Gate-B package

**Date:** 2026-08-22

## 1. Verdict

The finite Haar-exposure obstruction, the complete-`r=4` compensated
surjectivity theorem, the exact first-blocker/Palm recursions, and the
qualitative all-`r` Specht--Gram reduction survive hostile review.

Two normalization overstatements were found and repaired.  Positivity of
the raw all-`r` Gram Schur complement does **not** by itself give a
polynomial-size nonnegative perturbation of the uniform law, whose atoms
have mass `1/b!`.  Moreover `bar eta=eta/b!` cannot be polynomially bounded
below through all modules when the shallow output has standard Euclidean
norm: even the unconstrained top depth-two module has exponentially small
Fisher singular value.  The corrected reduction uses relative shallow
density, separates the explicit unconstrained orbit eigenvalue from the
dimensionless compensated angle, and retains the additional coordinatewise-
delocalization bound needed for nonnegativity at a useful amplitude.

No theorem in the audited package proves the stopped positive Gate-B tail.

## 2. Claims which survive exactly

1. For an actual first-blocker cell, the pair mass, collision multiplier,
   and Palm law obey the displayed exact deletion recursions.  If a whole
   bite deletes at most `Z_0/8`, every sequential cell has current fraction
   at most `1/8`; hence the correct collision-budget factor is `64/49` and
   the capacity-forcing reverse factor is `49/64`.

2. The balanced-rate LP and dual are correct.  With a positive baseline,
   the compensated polytope `B lambda=B lambda^0` has the baseline in its
   relative interior.  The entropy tilt is differentiable at zero and has
   strict first derivative unless the objective lies in `row(B)`.

3. The single-cell collision and fixed-hole-support logarithms have exact
   predictable compensators.  Their martingale claims require the support
   to be fixed before the process and the stopping time to be bounded.  The
   stopped Chernoff proof is valid after inserting the predictable factors
   `1_(n<tau)`.  Nothing here licenses conditioning on the terminal hole set.

4. For the puncture-averaged `r=4` Haar direction,

   \[
   A\delta=0,\qquad
   \partial_{4,2}(\widetilde P\delta)_M=425J,
   \qquad
   \partial_{3,2}(\widetilde P\delta)_L=8832J.
   \]

   Therefore its full `S_9` orbit span cannot be both exposure-null and
   Haar-current-active.  The step-two-to-consecutive orientation is correct.

5. In the complete `r=4` catalogue, over `Q`,

   \[
   \operatorname {rank}B=417,\qquad
   \operatorname {rank}Q=28,\qquad
   \operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}=444.
   \]

   The modular calculation is a valid rational lower bound because a
   nonzero minor modulo the prime `1000003` is a nonzero integer minor.
   The three explicit `B` row relations, the eight independent Hamiltonian
   degree relations, and the shared constant row give matching rational
   upper bounds.  Hence
   `Q(ker B)` is exactly the 27-dimensional balanced pair-current space.

6. The symmetrized dimension-free `C_8` seed is rank-`r` and
   rank-`(r-1)` null and rank-`(r-2)` active.  At `r=4` its puncture average
   is exposure-detected with the same constants as the Haar direction.
   The complete-state `72`-column local bank has full column rank after
   stacking `A` and `widetilde P`, so it contains no nonzero compensated
   perturbation.  This local obstruction is compatible with the global
   `r=4` surjectivity theorem.

7. In the complete all-`r` catalogue, the configuration space is the left
   regular representation, rooted exposure is right convolution by the
   invariant duplicate kernel, and every relevant constraint/objective
   source is a multiplicity-one two-row permutation module.  Consequently
   the qualitative compensated-current question reduces, on each
   `V_(b-j,j)`, to whether one shallow multiplicity vector lies outside the
   span of four constraint vectors.  The Gram Schur complement tests this
   exactly.

8. A subsequent exact `r=5`, depth-two certificate gives rational ranks
   `1581,155,1735`; hence the compensated kernel surjects onto the full
   154-dimensional balanced triple-current space
   `V_(9,2) direct-sum V_(8,3)`.  On the same complete catalogue, the
   auxiliary full cyclic tests give `(rank Q_2,rank[B;Q_2])=(45,1625)`
   and `(rank Q_4,rank[B;Q_4])=(320,1900)`.  Thus the kernel also
   surjects onto every balanced pair current and every balanced four-set
   current.  Equivalently, all nontrivial modules present at each tested
   rank `k=2,3,4` have positive qualitative Gram complement.  These finite
   tests supply no asymptotic norm bound.

## 3. Normalization and positivity boundary

Under the isometric convention

\[
 \Phi_\lambda(v\otimes u)(g)
 =\sqrt{\dim V_\lambda/b!}\,\langle v,gu\rangle,
\]

an unscaled matrix-coefficient row carries the multiplicity factor
`sqrt(b!/dim V_lambda)`.  If `eta` is the standard-Euclidean squared
singular value of the compensated shallow map, then the uniform-law Fisher
input norm has squared singular value `bar eta=eta/b!`.  This quantity is
exponentially small on the top depth-two module even before compensation.

If `theta` is the unconstrained Fisher eigenvalue, `p` is the uniform
shallow-target marginal, and
`alpha=eta/||m||^2` is the dimensionless squared sine from the four
constraint directions, then the relative-density compensated eigenvalue is

\[
                         \widehat\sigma^2=\alpha\theta/p^2.
\]

The shallow orbit factor `theta/p^2` now has a closed exact binomial sum.
The first unknown complete-catalogue scalar is `alpha`, equivalently the
normalized five-vector Gram determinant.

Even a polynomial lower bound on `bar eta` is only an `L^2` statement.
For a quantitatively useful perturbation of `lambda_G^0=1/b!`, one also
needs a right inverse satisfying a bound of the form

\[
 \|\delta/\lambda^0\|_\infty\le r^C\|j\|_*.
\]

For each fixed finite `r`, a nonzero kernel direction always admits some
sufficiently small nonnegative amplitude.  The audit found no uniform or
polynomial lower bound for that amplitude.

## 4. Exact remaining Gate-B gap

At the symmetric complete state one must prove polynomial lower bounds for
the relative-density products `alpha theta/p^2` and a coordinatewise-
delocalized simultaneous right inverse through the required shallow band.
Along the actual nonsymmetric stopped residual,
one must then preserve the analogous constrained singular values and
Gate-A load bounds, or invoke a negligible priority cleanup.

Finally the selected laws must accumulate `Omega(log(1/x))` predictable
exact collision or fixed-support protection gain and align it with terminal
holes while avoiding accepted hits.  The negative alternative remains a
stopped proof that both the signed first-blocker and quadratic budgets are
`o(log(1/x))`, which would rule out the full-survivor route.

## 5. Replayed checks and hashes

All of the following passed:

```text
python3 scratch/verify_gate_b_first_blocker_collision_budget_20260822.py
python3 scratch/verify_gate_b_first_blocker_cell_collision_dichotomy_20260822.py
python3 scratch/verify_compensated_haar_exposure_detection_20260822.py
python3 scratch/verify_complete_r4_compensated_q2_surjectivity_20260822.py
python3 scratch/verify_all_r_compensated_gibbs_orientation_20260822.py
python3 scratch/verify_depth_two_fisher_scale_obstruction_20260822.py
python3 scratch/verify_gate_b_pair_potential_common_blocker_drift_20260822.py
python3 scratch/verify_gate_b_palm_collision_transport_20260822.py
python3 scratch/audit_punctured_weighted_bite_two_edge_obstruction_20260822.py
clang++ -std=c++20 -O3 -march=native -pthread \
  scratch/verify_complete_r5_compensated_q2_surjectivity_20260822.cpp \
  -o /tmp/verify_complete_r5_compensated_q2_surjectivity_20260822
/tmp/verify_complete_r5_compensated_q2_surjectivity_20260822
```

Audited source hashes after repair:

```text
72e3526997a7871ddfd01196df9d4ff1fa88653831f2b759adcc5f7857f3d47f  MATH_REDUCTION_GATE_B_FIRST_BLOCKER_COLLISION_BUDGET_AND_SIGNED_MIXING_GATE_20260822.md
1fc725fc08b1d5218aadafc76c552b8c098f26dbbc9a0626ff99818199325af1  MATH_OBSTRUCTION_COMPENSATED_HAAR_EXPOSURE_DETECTS_Q2_20260822.md
5b1597132cb75458535ab3dcb0364b828d845c9e12c96729d2e3245c15764164  MATH_THEOREM_COMPLETE_R4_COMPENSATED_Q2_CURRENT_SURJECTIVITY_20260822.md
9978b3df3b79cb2380550cf40f7e349ec84d7f9150d0dc72bc8c2eeb8c9dc897  MATH_REDUCTION_ALL_R_COMPENSATED_GIBBS_SPECHT_GRAM_GATE_20260822.md
547db22bfdd31197a81bb7d30da93d360cff40be91f97b11e96c733bc5467093  MATH_THEOREM_COMPLETE_R5_COMPENSATED_Q2_CURRENT_SURJECTIVITY_20260822.md
91faaa3f1344227aeea8c40921693a7bbe5049efaa5e084f56353bcaa52f1bc6  MATH_OBSTRUCTION_STANDARD_OUTPUT_FISHER_SCALE_AND_DIMENSIONLESS_GRAM_GATE_20260822.md
c7a177e658f07e00660747035efe1eacbad969e9c96e847b759a5975a34b9754  scratch/verify_gate_b_first_blocker_collision_budget_20260822.py
1eae4c480c9c5526bb02a3840e62486d9e756afab52b1b209a01071d7912f6f3  scratch/verify_compensated_haar_exposure_detection_20260822.py
a279f2d5d364c66956bc4f331df5d95f1a0efa08059da92692b4c031d9d80569  scratch/verify_complete_r4_compensated_q2_surjectivity_20260822.py
c5de6bde99259d8fd913c75d46672d6491c0265825702cce75bd4196cb16172f  scratch/verify_all_r_compensated_gibbs_orientation_20260822.py
71f1de2d49ee56a57723460e94d1e9bae158a027bf003ab3fc59a9d1dcf99f10  scratch/verify_complete_r5_compensated_q2_surjectivity_20260822.cpp
670a2b0e558dbc50ae35873594c51169a8c3a7f13cc86849b1a0a339e3615494  scratch/verify_depth_two_fisher_scale_obstruction_20260822.py
```

`MASTER_HANDOFF.md` was not edited.
