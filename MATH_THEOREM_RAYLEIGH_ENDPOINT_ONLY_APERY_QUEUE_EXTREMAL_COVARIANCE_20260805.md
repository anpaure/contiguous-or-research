# The endpoint-only Apéry queue is a sharp half-average extremizer with negative centered covariance

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact obstruction.  A legitimate saturated
first-minimum Bellman family attains equality in the cyclic half-average
theorem and has no finite shoulder, while its centered periodized covariance
is strictly negative and grows linearly with the number of residues.  Thus
the positive zeroth mode cannot be completed by asserting that the centered
term is nonnegative or dimension-free.  The complete formal functional of
this family remains strictly positive.

## 1. The endpoint-only family

Let `zeta` be the unique minimum of the Rayleigh signed-tail kernel `K`, and
put

\[
 M=K(0),\qquad C(h)=\sum_{q\ge0}K(qh).
\tag{1.1}
\]

For an integer `N>=2`, consider the table

\[
 c_0=0,\qquad c_j=0\ (1\le j<N),\qquad c_N=\zeta.
\tag{1.2}
\]

### Theorem 1.1

The table (1.2) is a nonnegative internally superadditive saturated
first-`zeta` table.  Its maximum-density data are

\[
 \lambda={\zeta\over N},\qquad S=\{N\},\qquad g=N,
 \qquad P=g\lambda=\zeta.
\tag{1.3}
\]

For `0<=r<N`, its Apéry data and exact Bellman clock are

\[
 \beta_r=-r\lambda,\qquad s_r=0,\qquad d_r=r\lambda,
\tag{1.4}
\]

\[
 V_{qN+r}=U_{qN+r}=q\zeta.
\tag{1.5}
\]

In particular the availability shoulder vanishes identically.

#### Proof

Internal superadditivity is immediate: every proper entry is zero and the
only nonzero inequality has `c_N=zeta>=0`.  The proper-partition value at
`N` is zero, so endpoint saturation gives `c_N=max{zeta,0}=zeta`.
The endpoint is the first `zeta` crossing.

Every proper denomination has density zero, while denomination `N` has
density `zeta/N`; hence (1.3).  Delete the critical denomination-`N`
steps from a residue walk: they are zero-cost residue loops.  Every
remaining proper step `j<N` has reduced cost `lambda j`, and the remaining
ordinary capacity is congruent to `r mod N`.  Its least possible
nonnegative value is `r`, attained for `r>0` by the one-step denomination
`r` (and for `r=0` by the empty walk).  The minimum cost is therefore
`r lambda`.  This proves (1.4).

At capacity `qN+r`, use `q` endpoint denominations and fill the remainder
with zero-valued denominations.  No configuration can use more than `q`
endpoint denominations.  Its value is therefore exactly `q zeta`, proving
(1.5).  Thus `V=U` and the shoulder is zero. \(\square\)

## 2. Exact equality in the cyclic half-average bound

The maximum displacement is

\[
 \Delta=(N-1)\lambda.
\tag{2.1}
\]

Moreover

\[
 {1\over N}\sum_{r=0}^{N-1}d_r
 ={\lambda\over N}{N(N-1)\over2}
 ={\Delta\over2}.
\tag{2.2}
\]

Thus the constant `1/2` in the cyclic half-average theorem is attained for
every `N`, not only on the group of order two.

The counting queue on one period is the front-loaded staircase

\[
 w_N(x)=\sum_{r=1}^{N-1}{\bf1}_{[0,r\lambda)}(x),
 \qquad 0\le x<\zeta,
\tag{2.3}
\]

and

\[
 \overline w_N={N-1\over2}.
\tag{2.4}
\]

## 3. Exact centered covariance

Let

\[
 Q_\zeta(x)=\sum_{q\ge0}-K'(q\zeta+x)
\tag{3.1}
\]

and define the centered covariance

\[
 \mathcal C_N=
 \int_0^\zeta (w_N-\overline w_N)Q_\zeta.
\tag{3.2}
\]

### Theorem 3.1

One has the exact identities

\[
 \boxed{\Phi(U)=N C(\zeta),}
\tag{3.3}
\]

\[
 \boxed{
 \mathcal C_N
 =N C(\zeta)-C(\zeta/N)-{M(N-1)\over2}.}
\tag{3.4}
\]

Furthermore,

\[
 \boxed{\mathcal C_N<0\qquad(N\ge9).}
\tag{3.5}
\]

More quantitatively,

\[
 \mathcal C_N<{9-N\over200}.
\tag{3.6}
\]

#### Proof

Equation (1.5) gives exactly `N` copies of every point `q zeta`, so (3.3)
follows.  Apply the zeroth-mode identity to mesh
`lambda=zeta/N`.  Equations (2.4) and (3.3) give (3.4).

The authenticated rational Rayleigh bounds are

\[
 M=K(0)<{9\over100},\qquad K(\zeta)<-{1\over20},
\tag{3.7}
\]

and every `K(q zeta)` with `q>=2` is negative.  Hence

\[
 C(\zeta)<M-{1\over20},
\qquad
 C(\zeta)-{M\over2}
 <{M\over2}-{1\over20}<-{1\over200}.
\tag{3.8}
\]

The all-mesh arithmetic-comb theorem gives `C(zeta/N)>0`.  Rewriting
(3.4) as

\[
 \mathcal C_N
 =N\left(C(\zeta)-{M\over2}\right)
   +{M\over2}-C(\zeta/N)
\tag{3.9}
\]

and using `M/2<9/200` proves (3.6), hence (3.5). \(\square\)

The total formal value nevertheless remains positive:

\[
 \Phi(U)=N C(\zeta)>N{377\over108000}>0.
\tag{3.10}
\]

Thus the negative centered covariance is not a counterexample to formal
Bellman positivity.  It is an exact obstruction to separating the proof
into a positive mean plus a harmless centered error.

## 4. Sharp lesson for the remaining analytic gate

This family simultaneously has:

1. the largest allowed period `P=zeta`;
2. equality in `mean(w)>=Delta/(2 lambda)`;
3. zero finite shoulder;
4. centered covariance of order `-N`;
5. a positive complete phase train of order `+N`.

Therefore no valid all-price proof can use only queue area, the maximum
displacement, or a dimension-free lower bound on the centered covariance.
It must retain phase-train structure.  A proof-safe next target is a lower
bound for the **combined** quantity

\[
 C(\lambda)+M\overline w+\mathcal C_P(w)=\Phi(U),
\tag{4.1}
\]

over the cyclically superadditive Apéry cone, or an exchange theorem showing
that its minimum is attained on a controlled family of phase trains.  The
endpoint-only family is a mandatory equality-scale calibration for any such
bound.

## 5. Dependencies

1. `MATH_THEOREM_RAYLEIGH_APERY_DEFECT_QUEUE_AND_ZEROTH_MODE_RESERVE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`.
